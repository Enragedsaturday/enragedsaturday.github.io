#!/usr/bin/env python3
"""
S8 R12 — the link-ledger assembler + the COH-15 join (SD3).

Merges the S8 lane row files into the canonical `_run/s8-link-ledger.json`
(one machine artifact, deterministic, re-runnable) and — as the `--join`
subcommand — re-derives NUM-04's distinct bare-mention caption universe from the
ledger and joins it against the S6 coverage ledger to PROVE R1 by machine:

    every in-scope mention of a page-backed caption is linked (or queue-resolved);
    every plain mention cites a non-page terminal, an exemption zone, or a
    fail-closed (adjudicated) resolution; no linked mention resurrects a
    `removed`/`unverifiable` caption.

The join is a SCRIPT, not an agent (spec R12): it exits 1 on any join violation
so CI fails closed. Writer != checker — this lane emits the artifact + the
violation list; S9 samples >=1-in-10 rows + 100% of adjudicated rows and adjudicates.

    ---- LEDGER SECTIONS (spec R12) ----
    mentions[] : one row per case-mention occurrence
                 {file, line, matched_text, caption_key,
                  resolution:{target, method, rationale?}, action, lane, model}
                 method in {caption|page-scope|roster|corpus|pre-existing|zone|adjudicated}
                 action  in {linked|linked-deep|plain:no-page|plain:adjudicated|exempt:<zone>}
                 Adjudicated occurrences (from the ambiguity queue) join the
                 resolutions file -> method:"adjudicated" + the reviewer rationale.
    terms{}    : per-page register-coverage counts (from the term-linker rows).
    embeds[]   : every `![[` with its source anchor. THE FRESH CORPUS SCAN IS
                 AUTHORITATIVE; s8-embed-rows.jsonl (if present) adds provenance.
    pincites[] : the split-pincite cases+doctrine rows, scope-tagged.
    header     : {generated, lane, model, spec, scanned_head, counts, sources[], gaps[]}.

Python 3 stdlib only. READ-ONLY vs content/ (the embed scan reads, never writes).

    python3 scripts/s8/assemble_ledger.py            # assemble -> _run/s8-link-ledger.json
    python3 scripts/s8/assemble_ledger.py --join     # assemble (if needed) + COH-15 join
    python3 scripts/s8/assemble_ledger.py --self-test # fixtures (pass + fail)
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUN_DIR = os.path.join(REPO_ROOT, "_run")
O2_DIR = os.path.join(RUN_DIR, "o2-execute")
CONTENT_ROOT = os.path.join(REPO_ROOT, "content")

LANE = "o2-opus-xhigh"
MODEL = "claude-opus-4-8"

# Row sources (defaults; overridable for the self-test fixtures).
SRC = {
    "mentions": os.path.join(O2_DIR, "s8-link-ledger.rows.mentions.jsonl"),
    "pincites": os.path.join(O2_DIR, "s8-link-ledger.rows.jsonl"),
    "terms": os.path.join(O2_DIR, "s8-term-rows.jsonl"),
    "queue": os.path.join(O2_DIR, "s8-adjudication-queue.jsonl"),
    "resolutions": os.path.join(O2_DIR, "s8-adjudication-resolutions.jsonl"),
    "embeds": os.path.join(O2_DIR, "s8-embed-rows.jsonl"),
    "s6_ledger": os.path.join(RUN_DIR, "s6-coverage-ledger.json"),
    "caption_index": os.path.join(O2_DIR, "s8-caption-index.json"),
}
LEDGER_OUT = os.path.join(RUN_DIR, "s8-link-ledger.json")
JOIN_OUT = os.path.join(O2_DIR, "s8-coh15-join.json")

_EMBED_RE = re.compile(r"!\[\[([^\[\]]+?)\]\]")


# --------------------------------------------------------------------------
# io helpers
# --------------------------------------------------------------------------

def _load_jsonl(path):
    if not path or not os.path.exists(path):
        return None
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _load_json(path):
    if not path or not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _git_head():
    try:
        out = subprocess.check_output(
            ["git", "-C", REPO_ROOT, "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL)
        return out.decode().strip()
    except Exception:
        return None


def _iter_markdown(root):
    for dirpath, _dirs, files in os.walk(root):
        for fn in sorted(files):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


# --------------------------------------------------------------------------
# section builders
# --------------------------------------------------------------------------

def _norm_mention(r):
    """Pass an auto mention row through, guaranteeing the R12 schema keys."""
    res = r.get("resolution") or {}
    out = {
        "file": r.get("file"),
        "line": r.get("line"),
        "matched_text": r.get("matched_text"),
        "caption_key": r.get("caption_key"),
        "resolution": {
            "target": res.get("target"),
            "method": res.get("method"),
        },
        "action": r.get("action"),
        "lane": r.get("lane", LANE),
        "model": r.get("model", MODEL),
    }
    if res.get("rationale") is not None:
        out["resolution"]["rationale"] = res.get("rationale")
    return out


def build_adjudicated_rows(queue, resolutions):
    """Join the ambiguity queue occurrences x their resolutions into R12 mention
    rows (method:"adjudicated"). Keyed by (file, line, matched_text); duplicate
    keys are zipped in file order (queue and resolutions share the same key
    multiset). Missing queue is tolerated — resolutions carry file/line/text."""
    q_by_key = {}
    for q in (queue or []):
        key = (q.get("file"), q.get("line"), q.get("matched_text"))
        q_by_key.setdefault(key, []).append(q)

    rows = []
    for r in (resolutions or []):
        key = (r.get("file"), r.get("line"), r.get("matched_text"))
        qrow = None
        bucket = q_by_key.get(key)
        if bucket:
            qrow = bucket.pop(0)
        res = r.get("resolution") or {}
        target = res.get("target")
        is_plain = (target == "plain") or (target is None)
        action = "plain:adjudicated" if is_plain else "linked"
        row = {
            "file": r.get("file"),
            "line": r.get("line"),
            "matched_text": r.get("matched_text"),
            "caption_key": None if is_plain else target,
            "resolution": {
                "target": None if is_plain else target,
                "method": "adjudicated",
                "rationale": res.get("rationale"),
            },
            "action": action,
            "adjudication": {
                "candidates": (qrow or {}).get("candidates") if qrow else None,
                "reason": (qrow or {}).get("reason") if qrow else None,
                "confidence": res.get("confidence"),
                "evidence": r.get("evidence"),
                "s9_coverage_inbox": bool(r.get("s9-coverage-inbox")),
            },
            "lane": r.get("lane", LANE),
            "model": r.get("model", MODEL),
        }
        rows.append(row)
    return rows


def build_terms(term_rows):
    """{summary, pages{file->counts}} from the term-linker rows (header + pages)."""
    summary = None
    pages = {}
    for r in (term_rows or []):
        if r.get("kind") == "header":
            summary = {k: v for k, v in r.items()
                       if k not in ("kind", "lane", "model", "tool")}
        elif r.get("kind") == "page":
            pages[r.get("file")] = {
                "class": r.get("class"),
                "links": r.get("links"),
                "by_route": r.get("by_route"),
                "self_skips": r.get("self_skips"),
            }
    return {"summary": summary, "pages": pages}


def scan_embeds(content_root, provenance_rows=None):
    """AUTHORITATIVE fresh corpus scan of every `![[target#anchor]]` embed.
    Provenance rows (s8-embed-rows.jsonl) are merged in by (file, target) when
    present — the scan decides truth, the rows record which lane converted it."""
    prov = {}
    for pr in (provenance_rows or []):
        tgt = pr.get("target") or pr.get("embed")
        prov[(pr.get("file"), tgt)] = pr                       # exact rel-path key
        prov.setdefault((os.path.basename(pr.get("file") or ""), tgt), pr)  # basename fallback

    embeds = []
    for path in _iter_markdown(content_root):
        rel = os.path.relpath(path, REPO_ROOT)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        for ln, line in enumerate(text.split("\n"), start=1):
            for m in _EMBED_RE.finditer(line):
                inner = m.group(1).strip()
                target_full = inner.split("|", 1)[0].strip()
                page, _, anchor = target_full.partition("#")
                page = page.strip()
                anchor = anchor.strip()
                full_slug = "/" in page  # path-qualified per R9 embed grammar
                row = {
                    "file": rel,
                    "line": ln,
                    "target": page,
                    "anchor": anchor or None,
                    "full_slug": full_slug,
                }
                p = prov.get((rel, target_full)) or \
                    prov.get((os.path.basename(rel), target_full))
                if p:
                    row["provenance"] = {
                        "lane": p.get("lane"),
                        "model": p.get("model"),
                        "converted_from": p.get("converted_from") or p.get("before"),
                        "flavor": p.get("flavor") or p.get("kind"),
                    }
                embeds.append(row)
    return embeds


# --------------------------------------------------------------------------
# assemble
# --------------------------------------------------------------------------

def assemble(src=None, content_root=None, scanned_head=None):
    src = src or SRC
    content_root = content_root or CONTENT_ROOT

    auto = _load_jsonl(src["mentions"]) or []
    queue = _load_jsonl(src["queue"])
    resolutions = _load_jsonl(src["resolutions"])
    term_rows = _load_jsonl(src["terms"])
    pincites = _load_jsonl(src["pincites"]) or []
    embed_rows = _load_jsonl(src["embeds"])   # None if not landed yet

    gaps = []
    if embed_rows is None:
        gaps.append("s8-embed-rows.jsonl absent at assembly — embeds[] is the "
                    "authoritative fresh corpus scan with no provenance overlay; "
                    "the close re-run picks up the rows.")

    mentions = [_norm_mention(r) for r in auto]
    adjudicated = build_adjudicated_rows(queue, resolutions)
    mentions.extend(adjudicated)

    terms = build_terms(term_rows)
    embeds = scan_embeds(content_root, embed_rows)

    # action histogram
    action_hist = {}
    for m in mentions:
        action_hist[m["action"]] = action_hist.get(m["action"], 0) + 1

    ledger = {
        "generated": datetime.datetime.now(datetime.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lane": LANE,
        "model": MODEL,
        "spec": "S8",
        "scanned_head": scanned_head if scanned_head is not None else _git_head(),
        "counts": {
            "mentions_total": len(mentions),
            "mentions_auto": len(auto),
            "mentions_adjudicated": len(adjudicated),
            "mentions_by_action": action_hist,
            "terms_pages": len(terms.get("pages") or {}),
            "embeds": len(embeds),
            "embeds_full_slug": sum(1 for e in embeds if e["full_slug"]),
            "pincites": len(pincites),
        },
        "sources": [os.path.relpath(src[k], REPO_ROOT)
                    for k in ("mentions", "pincites", "terms", "queue",
                              "resolutions", "embeds", "s6_ledger", "caption_index")
                    if src.get(k)],
        "gaps": gaps,
        "mentions": mentions,
        "terms": terms,
        "embeds": embeds,
        "pincites": pincites,
    }
    return ledger


# --------------------------------------------------------------------------
# COH-15 join — R1 proof
# --------------------------------------------------------------------------

NONPAGE_TERMINALS = {"brief-mention", "excluded-remit", "folded-alias",
                     "removed", "unverifiable", "watch"}


def _build_join_surface(s6_ledger, caption_index):
    """Two authorities: S6 owns the non-page terminal disposition (R1's plain
    rule); the caption index owns page existence for the broader corpus (the S6
    candidate universe is a subset of all page-backed captions)."""
    s6 = {}
    for r in (s6_ledger or {}).get("rows", []):
        for k in (r.get("caption"), r.get("canonical")):
            if k:
                s6[k] = {"terminal": r.get("terminal"),
                         "page_backed": bool(r.get("page_backed"))}
    entries = (caption_index or {}).get("entries", {}) or {}

    def page_backed(cap):
        e = entries.get(cap)
        if e and (e.get("page_stem") or e.get("terminal") == "authored"
                  or "page" in (e.get("sources") or [])):
            return True
        s = s6.get(cap)
        return bool(s and s["page_backed"])

    def nonpage_terminal(cap):
        s = s6.get(cap)
        if s and s["terminal"] in NONPAGE_TERMINALS:
            return s["terminal"]
        e = entries.get(cap)
        if e and e.get("terminal") in NONPAGE_TERMINALS:
            return e["terminal"]
        return None

    return page_backed, nonpage_terminal


def join(ledger, s6_ledger, caption_index):
    """Re-derive the distinct caption universe from the ledger and prove R1.
    Returns the join-result dict (carries `violations` — empty == clean)."""
    page_backed, nonpage_terminal = _build_join_surface(s6_ledger, caption_index)
    mentions = ledger.get("mentions", [])

    # in-scope universe: captions with >=1 non-exempt mention carrying a caption
    universe = {}   # caption -> action Counter (dict)
    for m in mentions:
        act = m.get("action") or ""
        if act.startswith("exempt"):
            continue
        cap = m.get("caption_key")
        if not cap:
            continue
        universe.setdefault(cap, {})
        universe[cap][act] = universe[cap].get(act, 0) + 1

    violations = []

    # R1 Check A — a page-backed caption may not have a plain mention.
    for cap, acts in sorted(universe.items()):
        if page_backed(cap):
            plain = acts.get("plain:no-page", 0) + acts.get("plain:adjudicated", 0)
            if plain:
                violations.append({
                    "check": "A-authored-plain",
                    "caption": cap, "actions": acts,
                    "detail": "page-backed caption has an in-scope PLAIN mention "
                              "(R1: every in-scope mention of an authored caption "
                              "must be linked)"})

    # R1 Check B — every plain:no-page mention must cite a non-page terminal.
    for m in mentions:
        if m.get("action") == "plain:no-page":
            cap = m.get("caption_key")
            if not cap:
                continue
            term = nonpage_terminal(cap)
            if term is None:
                violations.append({
                    "check": "B-plain-uncited",
                    "caption": cap, "file": m.get("file"), "line": m.get("line"),
                    "rationale": (m.get("resolution") or {}).get("rationale"),
                    "detail": "plain:no-page mention whose caption is neither a "
                              "non-page terminal in S6 nor page-backed (R1: a plain "
                              "mention must cite a non-page terminal state)"})

    # R1 Check C — no linked mention resurrects a removed/unverifiable caption.
    for cap, acts in sorted(universe.items()):
        linked = acts.get("linked", 0) + acts.get("linked-deep", 0)
        term = nonpage_terminal(cap)
        if linked and term in ("removed", "unverifiable") and not page_backed(cap):
            violations.append({
                "check": "C-resurrected",
                "caption": cap, "terminal": term, "actions": acts,
                "detail": "linked mention targets a %s caption with no page "
                          "(R1/COH-15: never resurrect an unverifiable caption)" % term})

    # R1 Check D — a mentioned caption that is neither page-backed nor a known
    # non-page terminal is dangling (unclassifiable — fail closed).
    for cap, acts in sorted(universe.items()):
        if not page_backed(cap) and nonpage_terminal(cap) is None:
            violations.append({
                "check": "D-dangling",
                "caption": cap, "actions": acts,
                "detail": "caption mentioned in-scope but neither page-backed nor a "
                          "non-page terminal (dangling — no linkable page, no ledger "
                          "disposition)"})

    # NUM-04 re-derivation + partition
    n_page = sum(1 for c in universe if page_backed(c))
    n_nonpage = sum(1 for c in universe
                    if not page_backed(c) and nonpage_terminal(c))
    # occurrence tallies
    occ = {}
    for cap, acts in universe.items():
        for a, n in acts.items():
            occ[a] = occ.get(a, 0) + n

    result = {
        "generated": datetime.datetime.now(datetime.timezone.utc)
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "lane": LANE,
        "model": MODEL,
        "spec": "S8 R1/R12 (COH-15 join)",
        "scanned_head": ledger.get("scanned_head"),
        "num04": {
            "note": "distinct captions with >=1 in-scope (non-exempt) case mention "
                    "in the assembled ledger (auto mentions + adjudicated page "
                    "targets). The 388 audit seed is consumed seed-not-gospel "
                    "(NUM-04 ADOPT): the S7 89-unit doctrine build + every-occurrence "
                    "density grew the live universe; the machine number is what the "
                    "ledger re-derives, not the audit figure.",
            "distinct_captions": len(universe),
            "page_backed": n_page,
            "non_page_terminal": n_nonpage,
            "audit_seed": 388,
        },
        "occurrences_in_scope": occ,
        "checks": {
            "A_authored_plain": sum(1 for v in violations if v["check"] == "A-authored-plain"),
            "B_plain_uncited": sum(1 for v in violations if v["check"] == "B-plain-uncited"),
            "C_resurrected": sum(1 for v in violations if v["check"] == "C-resurrected"),
            "D_dangling": sum(1 for v in violations if v["check"] == "D-dangling"),
        },
        "clean": not violations,
        "violations": violations,
    }
    return result


# --------------------------------------------------------------------------
# self-test (fixtures under fixtures/assemble/)
# --------------------------------------------------------------------------

_FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "assemble")


def _fix_src():
    d = _FIX
    return {
        "mentions": os.path.join(d, "mentions.jsonl"),
        "pincites": os.path.join(d, "pincites.jsonl"),
        "terms": os.path.join(d, "terms.jsonl"),
        "queue": os.path.join(d, "queue.jsonl"),
        "resolutions": os.path.join(d, "resolutions.jsonl"),
        "embeds": os.path.join(d, "embeds.jsonl"),
        "s6_ledger": os.path.join(d, "s6-ledger.json"),
        "caption_index": os.path.join(d, "caption-index.json"),
    }


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    src = _fix_src()
    content_root = os.path.join(_FIX, "content")
    ledger = assemble(src=src, content_root=content_root, scanned_head="TEST")

    # --- assembler shape ---
    check(ledger["spec"] == "S8", "header spec != S8")
    acts = ledger["counts"]["mentions_by_action"]
    check(ledger["counts"]["mentions_adjudicated"] == 2,
          "expected 2 adjudicated rows, got %s" % ledger["counts"]["mentions_adjudicated"])
    # one adjudicated -> linked (page target), one -> plain:adjudicated
    adj = [m for m in ledger["mentions"] if m["resolution"].get("method") == "adjudicated"]
    check(any(m["action"] == "linked" and m["caption_key"] for m in adj),
          "adjudicated page-target row missing")
    check(any(m["action"] == "plain:adjudicated" for m in adj),
          "adjudicated plain row missing")
    check(all(m["resolution"].get("rationale") for m in adj),
          "adjudicated row missing joined rationale")
    # embeds: fresh scan is authoritative (2 in fixture content: one full-slug,
    # one bare) and the provenance overlay attaches to the matching one.
    check(ledger["counts"]["embeds"] == 2,
          "expected 2 scanned embeds, got %s" % ledger["counts"]["embeds"])
    check(sum(1 for e in ledger["embeds"] if not e["full_slug"]) == 1,
          "expected exactly one non-full-slug embed in fixture")
    check(any(e.get("provenance") for e in ledger["embeds"]),
          "embed provenance overlay did not attach")
    check(ledger["terms"]["pages"], "terms pages empty")
    check(ledger["counts"]["pincites"] == 2,
          "expected 2 pincite rows, got %s" % ledger["counts"]["pincites"])

    # --- join: CLEAN path ---
    s6 = _load_json(src["s6_ledger"])
    ci = _load_json(src["caption_index"])
    res_ok = join(ledger, s6, ci)
    check(res_ok["clean"] is True,
          "clean fixture should join clean; got %s" % res_ok["violations"])
    check(res_ok["num04"]["distinct_captions"] >= 2,
          "num04 distinct_captions too low")

    # --- join: FAIL path (each R1 check must fire) ---
    bad = {
        "scanned_head": "TEST",
        "mentions": [
            # A: page-backed caption left plain
            {"file": "f", "line": 1, "matched_text": "Terry v. Ohio",
             "caption_key": "Terry v. Ohio",
             "resolution": {"target": None, "method": "caption"},
             "action": "plain:no-page"},
            # B: plain mention whose caption is unknown (no terminal, no page)
            {"file": "f", "line": 2, "matched_text": "Ghost v. Nowhere",
             "caption_key": "Ghost v. Nowhere",
             "resolution": {"target": None, "method": "caption"},
             "action": "plain:no-page"},
            # C: linked mention resurrecting a removed caption
            {"file": "f", "line": 3, "matched_text": "West v. White",
             "caption_key": "West v. White",
             "resolution": {"target": "West v. White", "method": "pre-existing"},
             "action": "linked"},
        ],
    }
    bad_s6 = {
        "rows": [
            {"caption": "Terry v. Ohio", "terminal": "authored", "page_backed": True},
            {"caption": "West v. White", "terminal": "removed", "page_backed": False},
        ],
    }
    bad_ci = {"entries": {
        "Terry v. Ohio": {"page_stem": "Terry v. Ohio", "terminal": "authored",
                          "sources": ["page"]},
        "West v. White": {"terminal": "removed"},
    }}
    res_bad = join(bad, bad_s6, bad_ci)
    check(res_bad["clean"] is False, "bad fixture must not join clean")
    for want in ("A_authored_plain", "B_plain_uncited", "C_resurrected", "D_dangling"):
        check(res_bad["checks"][want] >= 1,
              "join fail-path did not fire check %s (%s)" % (want, res_bad["checks"]))

    if failures:
        print("assemble_ledger.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("assemble_ledger.py --self-test: PASS "
          "(assemble: mentions/adjudicated join/embeds-scan+provenance/terms/pincites; "
          "join: clean + A/B/C/D fail-paths)")
    return 0


# --------------------------------------------------------------------------
# cli
# --------------------------------------------------------------------------

def _write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


def main(argv):
    ap = argparse.ArgumentParser(description="S8 R12 ledger assembler + COH-15 join")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--join", action="store_true",
                    help="assemble + run the COH-15 join; exit 1 on any join violation")
    ap.add_argument("--out", default=LEDGER_OUT)
    ap.add_argument("--join-out", default=JOIN_OUT)
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    ledger = assemble()
    _write_json(args.out, ledger)
    print("ledger: %s" % os.path.relpath(args.out, REPO_ROOT))
    print("  mentions %d (auto %d + adjudicated %d) | embeds %d | pincites %d | terms pages %d"
          % (ledger["counts"]["mentions_total"], ledger["counts"]["mentions_auto"],
             ledger["counts"]["mentions_adjudicated"], ledger["counts"]["embeds"],
             ledger["counts"]["pincites"], ledger["counts"]["terms_pages"]))
    print("  by_action: %s" % json.dumps(ledger["counts"]["mentions_by_action"], sort_keys=True))
    if ledger["gaps"]:
        print("  gaps: %s" % json.dumps(ledger["gaps"]))

    if args.join:
        s6 = _load_json(SRC["s6_ledger"])
        ci = _load_json(SRC["caption_index"])
        if s6 is None or ci is None:
            print("JOIN ABORT: missing S6 ledger or caption index", file=sys.stderr)
            return 1
        result = join(ledger, s6, ci)
        _write_json(args.join_out, result)
        print("join: %s" % os.path.relpath(args.join_out, REPO_ROOT))
        print("  NUM-04 re-derived distinct captions: %d (page-backed %d, non-page %d; seed 388)"
              % (result["num04"]["distinct_captions"], result["num04"]["page_backed"],
                 result["num04"]["non_page_terminal"]))
        print("  checks: %s" % json.dumps(result["checks"], sort_keys=True))
        print("  clean: %s" % result["clean"])
        if not result["clean"]:
            print("  VIOLATIONS (%d):" % len(result["violations"]), file=sys.stderr)
            for v in result["violations"][:50]:
                print("    " + json.dumps(v, ensure_ascii=False), file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
