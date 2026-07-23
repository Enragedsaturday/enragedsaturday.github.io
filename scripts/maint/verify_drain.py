#!/usr/bin/env python3
"""MAINT-1 verify-drain — earn the missing two-key leg for under_review /
verified_identity lake records and promote what genuinely passes (S2 R2
fail-closed semantics; the P4-18 "earn the leg, never assume it" mechanism).

Pools
  A (drain): status in {under_review, verified_identity} AND citations.official
     present AND identity.lead_opinion_id present. Fetch the lead opinion text,
     string-match BOTH party names; if the cite leg flag is stale/false,
     recompute it from a cluster fetch. Both legs true -> status=verified.
  B (slip candidates): PAGED records (content/cases/<record_id>.md exists) with
     citations.official == null. Fetch cluster citations: if an official-class
     cite has appeared -> ledger row "cite_appeared" (NO hand-built citation
     blocks — that is S2 ingest's job; fail-closed, adjudicate). Otherwise earn
     the party-name leg from opinion text -> ledger row "slip_eligible".
     Statuses are applied later by --apply-slip (after the schema gains
     slip_opinion), reading this run's ledger.

Builder lane (codex-invoked): serial, one credential, paced 4.5s/request,
cached, resumable, journaled. Token ~/.config/cssi/cl-token (never printed).

Usage:
  python3 scripts/maint/verify_drain.py            # pools A+B, writes A promotions
  python3 scripts/maint/verify_drain.py --apply-slip  # apply slip_opinion from ledger

Outputs under _run/maint/verify-drain/:
  ledger.jsonl   one row per record examined (resumable key: record_id+phase)
  cache/         op-<id>.txt (extracted text), cluster-<id>.json
  cl-calls.log   appended batch journal
"""
import html
import json
import os
import re
import sys
import time
import urllib.request
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAKE = os.path.join(ROOT, "_overhaul2/lake/cases")
PAGES = os.path.join(ROOT, "content/cases")
RUN = os.path.join(ROOT, "_run/maint/verify-drain")
CACHE = os.path.join(RUN, "cache")
LEDGER = os.path.join(RUN, "ledger.jsonl")
LOG = os.path.join(RUN, "cl-calls.log")
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
API = "https://www.courtlistener.com/api/rest/v4"
PACE = 4.5
RUN_TAG = "2026-07-23 maint-1 verify-drain"

os.makedirs(CACHE, exist_ok=True)

STOPWORDS = {"the", "of", "and", "in", "re", "ex", "rel", "et", "al", "a", "an",
             "inc", "co", "corp", "llc", "ltd", "no",
             # descriptive caption noise, never party-identifying (MAINT-1 token repair)
             "etc", "individual", "officer", "officers", "badge", "warden", "sheriff",
             "superintendent", "commissioner", "director", "secretary", "agent", "agents"}
GENERIC_SIDES = {"united states", "state", "commonwealth", "people",
                 "district of columbia", "u.s.", "us"}


def read_token():
    tok = open(TOKEN_PATH).read().strip()
    if not tok:
        raise SystemExit("null token — refusing to run unauthenticated (CL 401s since 2026-07-22)")
    return tok


TOKEN = None


def cl_get(path, cache_file):
    """Cached, paced GET. Returns (parsed_json, fetched_live)."""
    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 2:
        return json.load(open(cache_file)), False
    req = urllib.request.Request(API + path, headers={"Authorization": f"Token {TOKEN}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    with open(cache_file, "w") as f:
        json.dump(data, f)
    time.sleep(PACE)
    return data, True


def opinion_text(opid):
    """Extracted searchable text for an opinion, cached."""
    txt_cache = os.path.join(CACHE, f"op-{opid}.txt")
    if os.path.exists(txt_cache) and os.path.getsize(txt_cache) > 50:
        return open(txt_cache, encoding="utf-8").read(), False
    data, fetched = cl_get(f"/opinions/{opid}/?fields=plain_text,html_with_citations,html,xml_harvard",
                           os.path.join(CACHE, f"op-{opid}.json"))
    raw = data.get("plain_text") or ""
    if len(raw.strip()) < 200:
        h = data.get("html_with_citations") or data.get("html") or data.get("xml_harvard") or ""
        raw = html.unescape(re.sub(r"<[^>]+>", " ", h))
    text = re.sub(r"\s+", " ", raw)
    with open(txt_cache, "w", encoding="utf-8") as f:
        f.write(text)
    return text, fetched


def norm(s):
    s = s.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def side_terms(side):
    """(full_phrase, [significant tokens]) for one caption side. MAINT-1 token
    repair: every significant token is a candidate, not one heuristic pick."""
    side = re.sub(r"[,.]+$", "", side.strip())
    phrase = norm(side)
    words = [re.sub(r"[^\w'\-]", "", w) for w in side.split()]
    toks = []
    for w in words:
        lw = w.lower().strip("'-")
        if len(lw) >= 3 and lw not in STOPWORDS and not lw.isdigit():
            toks.append(lw)
    return phrase, toks


def parties_in_text(case_name, text):
    """Body-text party evidence per side. Returns (n_sides_matched, total_sides,
    evidence list). A side matches on its full phrase or ANY significant token."""
    t = norm(text)
    sides = re.split(r"\s+v\.?\s+", case_name, maxsplit=1)
    if len(sides) == 1:  # In re X / Ex parte X — match the distinctive token
        sides = [re.sub(r"^(in re|ex parte|matter of)\s+", "", case_name, flags=re.I)]
    evidence, n_ok = [], 0
    for side in sides:
        phrase, toks = side_terms(side)
        hit = None
        if phrase and phrase in t:
            hit = "phrase"
        else:
            for tok in toks:
                if re.search(r"\b" + re.escape(tok) + r"\b", t):
                    hit = f"token:{tok}"
                    break
        evidence.append({"side": side.strip(), "matched": hit})
        n_ok += int(hit is not None)
    return n_ok, len(sides), evidence


def lead_bound_to_cluster(cluster_id, lead_id):
    """MAINT-1-R2 structural key: is the lead opinion in the cluster's own
    sub_opinions[] (live CL fetch, cached)?"""
    data, fetched = cl_get(f"/clusters/{cluster_id}/?fields=sub_opinions",
                           os.path.join(CACHE, f"cluster-subops-{cluster_id}.json"))
    subs = data.get("sub_opinions") or []
    ids = set()
    for s in subs:
        m = re.search(r"/opinions/(\d+)/", str(s))
        if m:
            ids.add(int(m.group(1)))
        elif isinstance(s, dict) and s.get("id"):
            ids.add(int(s["id"]))
    return int(lead_id) in ids, fetched


def party_leg(rec, text, fetch_counter):
    """Full MAINT-1 party-leg ladder. Returns (ok, rule, evidence)."""
    ident = rec["identity"]
    n_ok, n_sides, evidence = parties_in_text(ident.get("case_name") or rec["record_id"], text)
    if n_ok == n_sides:
        return True, "body-text", evidence
    canonical = ident.get("canonical_name_match") is True
    if not canonical:
        return False, None, evidence
    if n_ok >= 1:  # MAINT-1-R1 caption-leg fallback
        return True, "caption-leg (MAINT-1-R1)", evidence
    # MAINT-1-R2 structural fallback: zero body sides — require live sub_opinions bind
    bound, fetched = lead_bound_to_cluster(ident.get("cluster_id"), ident.get("lead_opinion_id"))
    fetch_counter.append(int(fetched))
    if bound:
        return True, "structural-leg (MAINT-1-R2)", evidence
    return False, None, evidence


def cite_leg_ok(rec, ident):
    """Cite leg: trusted flag, or MAINT-1-R3 web-dual-leg provenance."""
    if ident.get("expected_citation_found") is True:
        return True, "cluster.citations"
    off = (rec.get("citations") or {}).get("official") or {}
    if off.get("source") == "web-dual-leg":
        return True, "web-dual-leg (MAINT-1-R3)"
    return False, None


def cluster_official(cluster_id):
    """Fetch cluster citations; return (citations list, fetched_live)."""
    data, fetched = cl_get(f"/clusters/{cluster_id}/?fields=citations,case_name,precedential_status",
                           os.path.join(CACHE, f"cluster-{cluster_id}.json"))
    return data, fetched


def cite_leg_from_cluster(record, cluster_data):
    """Does cluster.citations[] carry the record's official cite?"""
    off = (record.get("citations") or {}).get("official") or {}
    want = (str(off.get("volume") or ""), norm(off.get("reporter") or ""), str(off.get("page") or ""))
    for c in cluster_data.get("citations") or []:
        got = (str(c.get("volume") or ""), norm(c.get("reporter") or ""), str(c.get("page") or ""))
        if got == want and want != ("", "", ""):
            return True
    return False


def load_ledger_keys():
    done = set()
    if os.path.exists(LEDGER):
        for line in open(LEDGER):
            try:
                r = json.loads(line)
                done.add((r["record_id"], r["phase"]))
            except Exception:
                pass
    return done


def write_record(path, rec):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2, sort_keys=False, ensure_ascii=False)
        f.write("\n")


def promote(rec, legs_note):
    rec["status"] = "verified"
    ident = rec["identity"]
    ident["party_name_in_text"] = True
    ident["expected_citation_found"] = True
    ident["reason_code"] = None
    prov = rec.setdefault("provenance", {})
    warns = prov.setdefault("warnings", [])
    warns.append(f"{RUN_TAG}: promoted to verified — {legs_note}")


def main():
    global TOKEN
    apply_slip = "--apply-slip" in sys.argv
    reexamine = "--reexamine" in sys.argv
    TOKEN = read_token()
    done = set() if reexamine else load_ledger_keys()
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    n_fetch = n_promoted = n_slip = n_examined = 0

    if apply_slip:
        rows = [json.loads(l) for l in open(LEDGER)] if os.path.exists(LEDGER) else []
        applied = 0
        for r in rows:
            if r.get("phase") != "slip" or r.get("disposition") != "slip_eligible":
                continue
            path = os.path.join(LAKE, r["record_id"] + ".json")
            rec = json.load(open(path), object_pairs_hook=OrderedDict)
            if rec.get("status") == "slip_opinion":
                continue
            rec["status"] = "slip_opinion"
            rec["identity"]["party_name_in_text"] = True
            rec["identity"]["reason_code"] = "recent_or_no_official_cite"
            rec.setdefault("provenance", {}).setdefault("warnings", []).append(
                f"{RUN_TAG}: status set to slip_opinion (no official reporter cite on CL; "
                f"party-name leg earned from opinion text)")
            write_record(path, rec)
            applied += 1
        print(f"APPLY-SLIP DONE: {applied} records set to slip_opinion")
        return

    with open(LEDGER, "a") as led:
        for fn in sorted(os.listdir(LAKE)):
            if not fn.endswith(".json"):
                continue
            path = os.path.join(LAKE, fn)
            rec = json.load(open(path), object_pairs_hook=OrderedDict)
            status = rec.get("status")
            if status not in ("under_review", "verified_identity"):
                continue
            rid = rec.get("record_id") or fn[:-5]
            ident = rec.get("identity") or {}
            official = (rec.get("citations") or {}).get("official")
            lead = ident.get("lead_opinion_id")
            paged = os.path.exists(os.path.join(PAGES, rid + ".md"))
            row = {"row": "maint1.draini.v1", "record_id": rid, "prior_status": status,
                   "paged": paged, "lane": "s2-builder-codex-rest",
                   "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

            if official and lead:
                phase = "drain"
                if (rid, phase) in done:
                    continue
                row["phase"] = phase
                n_examined += 1
                try:
                    cite_ok, cite_rule = cite_leg_ok(rec, ident)
                    if not cite_ok:
                        cdata, f1 = cluster_official(ident.get("cluster_id"))
                        n_fetch += int(f1)
                        cite_ok = cite_leg_from_cluster(rec, cdata)
                        cite_rule = "cluster.citations (recomputed)" if cite_ok else None
                        row["cite_leg_recomputed"] = cite_ok
                    text, f2 = opinion_text(lead)
                    n_fetch += int(f2)
                    extra_fetches = []
                    party_ok, party_rule, evidence = party_leg(rec, text, extra_fetches)
                    n_fetch += sum(extra_fetches)
                    row.update({"cite_leg": cite_ok, "cite_rule": cite_rule,
                                "party_leg": party_ok, "party_rule": party_rule,
                                "party_evidence": evidence, "text_chars": len(text)})
                    if cite_ok and party_ok:
                        promote(rec, f"cite leg via {cite_rule}; party leg via {party_rule} "
                                     f"(opinion {lead}: "
                                     f"{', '.join(e['matched'] or 'caption' for e in evidence)})")
                        write_record(path, rec)
                        row["disposition"] = "promoted_verified"
                        n_promoted += 1
                    else:
                        row["disposition"] = "not_promoted"
                except Exception as e:
                    row["disposition"] = "error"
                    row["error"] = str(e)[:300]
            elif not official and paged:
                phase = "slip"
                if (rid, phase) in done:
                    continue
                row["phase"] = phase
                n_examined += 1
                try:
                    cdata, f1 = cluster_official(ident.get("cluster_id"))
                    n_fetch += int(f1)
                    live_cites = cdata.get("citations") or []
                    official_class = [c for c in live_cites if c.get("type") in (1, 2, 3, 4, 5, 8)]
                    if official_class:
                        row["disposition"] = "cite_appeared"
                        row["live_citations"] = live_cites
                    elif lead:
                        text, f2 = opinion_text(lead)
                        n_fetch += int(f2)
                        # slip records lack a cite leg to pin the cluster, so the
                        # party leg stays strict full body-text (no R1/R2 fallback)
                        n_ok, n_sides, evidence = parties_in_text(ident.get("case_name") or rid, text)
                        party_ok = n_ok == n_sides
                        row.update({"party_leg": party_ok, "party_evidence": evidence,
                                    "text_chars": len(text)})
                        row["disposition"] = "slip_eligible" if party_ok else "slip_party_leg_failed"
                        n_slip += int(party_ok)
                    else:
                        row["disposition"] = "no_lead_opinion_id"
                except Exception as e:
                    row["disposition"] = "error"
                    row["error"] = str(e)[:300]
            else:
                continue
            led.write(json.dumps(row) + "\n")
            led.flush()

    with open(LOG, "a") as lg:
        lg.write(f"{t0} MAINT-1 verify-drain (builder lane, codex-invoked): {n_examined} records, "
                 f"{n_fetch} live fetches, {n_promoted} promoted, {n_slip} slip-eligible -> ledger.jsonl\n")
    print(f"DONE: examined={n_examined} fetches={n_fetch} promoted={n_promoted} "
          f"slip_eligible={n_slip}")


if __name__ == "__main__":
    main()
