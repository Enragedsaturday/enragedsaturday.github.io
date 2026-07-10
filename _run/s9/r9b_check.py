#!/usr/bin/env python3
"""S9 R9(b) — S8 link-ledger sample re-check + 100% adjudication applied-state check.

Lane: claude-fable-5-r9b. READ-ONLY over content/; writes only _run/s9/ outputs.

Checks (deterministic sample, offset 0):
  - mentions: every 10th row of _run/s8-link-ledger.json mentions, sorted by
    (file, line, caption_key or "")
  - pincites: every 10th row sorted by (file, pin_id or "", action)
  - embeds:   all 4
  - terms:    every 10th page key (sorted) of terms.pages
  - adjudications: ALL 187 rows of s8-adjudication-resolutions.jsonl
    (applied-state machine check here; merits review done by the lane on top)

Corpus moved after S8 (pin remediation, embeds, pipe escapes, date re-projections):
line drift expected -> re-anchor by matched_text; only semantic failures are DEFECT.
"""
import hashlib
import json
import os
import re
import sys

ROOT = "/Users/johngalt/Projects/cssi-quartz"
sys.path.insert(0, os.path.join(ROOT, "scripts", "s8"))
import zones as zmod  # frozen public API

LEDGER = os.path.join(ROOT, "_run", "s8-link-ledger.json")
RESOLUTIONS = os.path.join(ROOT, "_run", "o2-execute", "s8-adjudication-resolutions.jsonl")
CAPIDX = os.path.join(ROOT, "_run", "o2-execute", "s8-caption-index.json")
FRAGMENTS = os.path.join(ROOT, "_run", "o2-execute", "s8-fragments.jsonl")
REGISTER = os.path.join(ROOT, "scripts", "lint", "term-register.yml")
OUT = os.path.join(ROOT, "_run", "s9", "r9b-ledger-sample.jsonl")
LANE = "claude-fable-5-r9b"
MODEL = "claude-fable-5"

# ---------------------------------------------------------------- utilities

_WIKILINK = re.compile(r"!?\[\[([^\]\n]*?)\]\]")
_MDLINK = re.compile(r"\[[^\]\n]*\]\([^)\n]*\)")


def load_text(path_rel, cache={}):
    p = os.path.join(ROOT, path_rel)
    if path_rel not in cache:
        try:
            with open(p, encoding="utf-8") as fh:
                cache[path_rel] = fh.read()
        except FileNotFoundError:
            cache[path_rel] = None
    return cache[path_rel]


def line_of(text, off):
    return text.count("\n", 0, off) + 1


def wikilinks(text):
    """[(start, end, target_base, alias_or_None, line)] — alias split on first
    (possibly R11-escaped) pipe; target anchor (#...) stripped to target_base."""
    out = []
    for m in _WIKILINK.finditer(text):
        inner = m.group(1)
        mm = re.search(r"\\?\|", inner)
        if mm:
            tgt, alias = inner[: mm.start()], inner[mm.end():]
        else:
            tgt, alias = inner, None
        tgt = tgt.split("#", 1)[0].strip().rstrip("\\")
        out.append((m.start(), m.end(), tgt, alias, line_of(text, m.start())))
    return out


def occurrences(text, needle):
    """Word-bounded literal occurrences -> [(off, line)]."""
    pat = re.compile(r"(?<![\w])" + re.escape(needle) + r"(?![\w])")
    return [(m.start(), line_of(text, m.start())) for m in pat.finditer(text)]


def covering_kind(zlist, off):
    for z in zlist:
        if z["start"] <= off < z["end"]:
            return z["kind"]
    return None


def in_spans(off, spans):
    return any(s <= off < e for s, e, *_ in spans)


def page_stem(path_rel):
    return os.path.splitext(os.path.basename(path_rel))[0]


# ---------------------------------------------------------------- load inputs

with open(LEDGER, encoding="utf-8") as fh:
    LED = json.load(fh)
with open(CAPIDX, encoding="utf-8") as fh:
    IDX = json.load(fh)
RES = [json.loads(l) for l in open(RESOLUTIONS, encoding="utf-8") if l.strip()]
FRAGS = {}
for l in open(FRAGMENTS, encoding="utf-8"):
    r = json.loads(l)
    FRAGS[(r["record_id"], r["pin_id"])] = r

# term register: page-route target set (crude YAML scan; stdlib only)
PAGE_TARGETS = set()
cur = {}
for line in open(REGISTER, encoding="utf-8"):
    s = line.strip()
    if s.startswith("- canonical:"):
        cur = {}
    m = re.match(r"route:\s*(\S+)", s)
    if m:
        cur["route"] = m.group(1)
    m = re.match(r'target:\s*"?([^"#]+?)"?\s*$', s)
    if m and cur.get("route") == "page":
        PAGE_TARGETS.add(m.group(1).strip())

rows_out = []
findings = []


def emit(kind, key, verdict, detail=None):
    row = {"kind": kind, "key": key, "verdict": verdict,
           "lane": LANE, "model": MODEL}
    if detail:
        row["detail"] = detail
    rows_out.append(row)
    return row


ZC = {}


def zones_for(path_rel, text):
    if path_rel not in ZC:
        ZC[path_rel] = zmod.compute_zones(text, page_stem=page_stem(path_rel))
    return ZC[path_rel]


# ---------------------------------------------------------------- mentions

def check_mention(r, kind="mention"):
    key = "%s:%s:%s:%s" % (r["file"], r["line"], r["matched_text"], r["action"])
    text = load_text(r["file"])
    if text is None:
        return emit(kind, key, "DEFECT", "file missing")
    mt = r["matched_text"]
    action = r["action"]
    hint = r.get("line") or 0

    wl = wikilinks(text)

    if action == "linked":
        res = r.get("resolution") or {}
        tgt = res.get("target")
        method = res.get("method")
        mtpat = re.compile(r"(?<![\w])" + re.escape(mt) + r"(?![\w])")
        if tgt is None and method == "pre-existing":
            # "already inside a link", target unrecorded: matched caption sits
            # inside some wikilink span (target or alias portion)
            cands = [ln for s, e, t, a, ln in wl if mtpat.search(text[s:e])]
            if cands:
                d = min(abs(l - hint) for l in cands)
                return emit(kind, key, "OK",
                            None if d <= 10 else "drift %d lines" % d)
            return emit(kind, key, "DEFECT",
                        "pre-existing-link claim: matched_text no longer inside "
                        "any wikilink")
        cands = []
        for s, e, t, alias, ln in wl:
            if t != tgt:
                continue
            disp = alias if alias is not None else t
            ok = mtpat.search(disp) or disp == mt
            if not ok and method == "pre-existing":
                # scan-time caption matched the TARGET half of an existing
                # aliased link ([[Illinois v. Gates|Gates]])
                ok = mtpat.search(t)
            if ok:
                cands.append(ln)
        if cands:
            d = min(abs(l - hint) for l in cands)
            return emit(kind, key, "OK", None if d <= 10 else "drift %d lines" % d)
        anyt = [ln for s, e, t, a, ln in wl if t == tgt]
        if anyt:
            return emit(kind, key, "DEFECT",
                        "link(s) to target exist but none displays matched_text "
                        "(lines %s)" % anyt[:5])
        return emit(kind, key, "DEFECT", "no wikilink to %r in file" % tgt)

    if action.startswith("plain"):
        occ = occurrences(text, mt)
        plain_occ = [(o, ln) for o, ln in occ if not in_spans(o, wl)]
        md = list((m.start(), m.end()) for m in _MDLINK.finditer(text))
        really_plain = [(o, ln) for o, ln in plain_occ
                        if not any(s <= o < e for s, e in md)]
        extra = None
        if action == "plain:no-page":
            capk = r.get("caption_key")
            ent = IDX.get("entries", {}).get(capk) if capk else None
            if ent and ent.get("page_stem") and ent.get("terminal") == "authored":
                return emit(kind, key, "DEFECT",
                            "caption %r is page-backed/authored in caption index "
                            "but row says plain:no-page" % capk)
            if ent:
                extra = "terminal=%s" % ent.get("terminal")
        if really_plain:
            d = min(abs(ln - hint) for _, ln in really_plain)
            det = None if d <= 10 else "drift %d lines" % d
            if extra and det:
                det += "; " + extra
            return emit(kind, key, "OK", det)
        if plain_occ:
            return emit(kind, key, "OK", "occurrence inside an external md link "
                        "(not a case wikilink); claim holds")
        if occ:
            lns = sorted({ln for _, ln in occ})
            return emit(kind, key, "DEFECT",
                        "all occurrences now inside wikilinks (lines %s)" % lns[:5])
        return emit(kind, key, "DEFECT", "matched_text no longer found in file")

    if action == "exempt:selfpage":
        stem = page_stem(r["file"])
        tgt = (r.get("resolution") or {}).get("target")
        if tgt and tgt != stem:
            return emit(kind, key, "DEFECT",
                        "selfpage target %r != page stem %r" % (tgt, stem))
        occ = occurrences(text, mt)
        plain_occ = [(o, ln) for o, ln in occ if not in_spans(o, wl)]
        if plain_occ:
            return emit(kind, key, "OK")
        if occ:
            return emit(kind, key, "DEFECT", "self-mention now inside a wikilink")
        return emit(kind, key, "DEFECT", "matched_text no longer found in file")

    if action.startswith("exempt:"):
        want = action.split(":", 1)[1]
        zs = zones_for(r["file"], text)
        occ = [(m.start(), line_of(text, m.start()))
               for m in re.finditer(re.escape(mt), text)]
        if not occ:
            return emit(kind, key, "DEFECT", "matched_text no longer found in file")
        occ.sort(key=lambda t: abs(t[1] - hint))
        kinds = []
        for o, ln in occ:
            k = covering_kind(zs, o)
            kinds.append((k, ln))
            if k == want:
                d = abs(ln - hint)
                return emit(kind, key, "OK", None if d <= 10 else "drift %d lines" % d)
        # exempt under a different kind still honors the never-link claim
        exempt_other = [(k, ln) for k, ln in kinds if k is not None]
        if exempt_other:
            return emit(kind, key, "OK",
                        "zone kind drifted: recorded %s, now %s (still exempt)"
                        % (want, exempt_other[0][0]))
        return emit(kind, key, "DEFECT",
                    "no occurrence sits in any exemption zone (recorded %s); "
                    "kinds seen: %s" % (want, kinds[:4]))

    return emit(kind, key, "DEFECT", "unknown action %r" % action)


# ---------------------------------------------------------------- pincites

def check_pincite(r):
    key = "%s:%s:%s" % (r["file"], r.get("pin_id"), r["action"])
    text = load_text(r["file"])
    if text is None:
        return emit("pincite", key, "DEFECT", "file missing")
    action = r["action"]
    pin = r.get("pin_id")

    if action == "linked-deep":
        after = r.get("after", "")
        rid = r["record_id"]
        pat = re.compile(r"\[\[" + re.escape(rid) + re.escape(after) + r"(\\?\||\]\])")
        if not pat.search(text):
            return emit("pincite", key, "DEFECT",
                        "no wikilink [[%s%s|...]] in file" % (rid, after))
        tpage = load_text("content/cases/%s.md" % rid)
        anchor = after.lstrip("#")  # ^pin-N
        if tpage is None or anchor not in tpage:
            return emit("pincite", key, "DEFECT",
                        "target page missing anchor %s" % anchor)
        return emit("pincite", key, "OK")

    if action == "linked-external" and "after" in r:
        after = r["after"]
        if after in text:
            return emit("pincite", key, "OK")
        m = re.search(r"\((https://www\.courtlistener\.com[^)]*)\)", after)
        if m and m.group(1) in text:
            return emit("pincite", key, "OK", "after drifted but href present")
        return emit("pincite", key, "DEFECT", "applied replacement not found: %r" % after[:80])

    # case-page rows keyed by pin anchor
    if pin:
        anchor = "^" + pin
        pat = re.compile(r"^(.*\S.*\s\^" + re.escape(pin) + r")\s*$", re.M)
        m = pat.search(text)
        if not m:
            return emit("pincite", key, "DEFECT", "pin anchor %s not found in file" % anchor)
        line = m.group(1)
        has_ext = "](https://www.courtlistener.com/" in line
        frag = FRAGS.get((r["record_id"], pin))
        if action == "linked-external":
            if not has_ext:
                return emit("pincite", key, "DEFECT",
                            "anchor line has no external CL link")
            if frag and frag.get("validated") and frag.get("fragment"):
                if frag["fragment"] not in line:
                    return emit("pincite", key, "DEFECT",
                                "validated fragment %r not in link href"
                                % frag["fragment"][:50])
            return emit("pincite", key, "OK")
        if action.startswith("plain"):
            if has_ext:
                return emit("pincite", key, "DEFECT",
                            "row says plain but anchor line carries an external link")
            if frag and frag.get("validated"):
                return emit("pincite", key, "DEFECT",
                            "fragments journal has a VALIDATED fragment yet row is plain")
            return emit("pincite", key, "OK")
    return emit("pincite", key, "DEFECT", "unhandled pincite shape")


# ---------------------------------------------------------------- embeds

def check_embed(r):
    key = "%s:%s%s" % (r["file"], r["target"], r.get("anchor") or "")
    text = load_text(r["file"])
    if text is None:
        return emit("embed", key, "DEFECT", "file missing")
    anchor = r.get("anchor") or ""
    needle = "![[%s#%s]]" % (r["target"], anchor)
    if needle not in text:
        return emit("embed", key, "DEFECT", "embed %r not found in source" % needle)
    tpage = load_text("content/%s.md" % r["target"])
    if tpage is None:
        return emit("embed", key, "DEFECT", "target page content/%s.md missing" % r["target"])
    if anchor and anchor not in tpage:
        return emit("embed", key, "DEFECT", "anchor %s missing on target page" % anchor)
    return emit("embed", key, "OK")


# ---------------------------------------------------------------- term pages

def check_term_page(page, rec):
    key = page
    text = load_text("content/" + page)
    if text is None:
        return emit("term-page", key, "DEFECT", "file missing")
    wl = wikilinks(text)
    n_gloss = sum(1 for m in re.finditer(r"\[\[Common Legal Terms#", text))
    n_cite = sum(1 for m in re.finditer(r"\[\[Reading and Citing Cases#", text))
    n_page = sum(1 for s, e, t, a, ln in wl if t in PAGE_TARGETS)
    want = rec.get("by_route") or {}
    probs = []
    if n_gloss < want.get("glossary", 0):
        probs.append("glossary %d<%d" % (n_gloss, want["glossary"]))
    if n_cite < want.get("citing", 0):
        probs.append("citing %d<%d" % (n_cite, want["citing"]))
    if n_page < want.get("page", 0):
        probs.append("page %d<%d" % (n_page, want["page"]))
    if probs:
        return emit("term-page", key, "DEFECT",
                    "recorded route counts exceed links now present: " + "; ".join(probs))
    return emit("term-page", key, "OK",
                "gloss %d/%d cite %d/%d page %d/%d (>= recorded; pre-existing "
                "S6/S7 links inflate current counts by design)"
                % (n_gloss, want.get("glossary", 0), n_cite, want.get("citing", 0),
                   n_page, want.get("page", 0)))


# ---------------------------------------------------------------- adjudications

def check_adjudication(r):
    """Applied-state check for a resolution row; merits reviewed by the lane."""
    key = "%s:%s:%s" % (r["file"], r["line"], r["matched_text"])
    tgt = r["resolution"]["target"]
    text = load_text(r["file"])
    if text is None:
        return emit("adjudication", key, "DEFECT", "file missing")
    mt = r["matched_text"]
    wl = wikilinks(text)
    if tgt == "plain":
        occ = occurrences(text, mt)
        plain_occ = [(o, ln) for o, ln in occ if not in_spans(o, wl)]
        if plain_occ:
            return emit("adjudication", key, "OK")
        if occ:
            return emit("adjudication", key, "DEFECT",
                        "resolved plain but all occurrences now inside wikilinks "
                        "(lines %s)" % sorted({ln for _, ln in occ})[:5])
        return emit("adjudication", key, "DEFECT", "matched_text vanished from file")
    # linked resolution
    cands = []
    for s, e, t, alias, ln in wl:
        if t != tgt:
            continue
        disp = alias if alias is not None else t
        if re.search(r"(?<![\w])" + re.escape(mt) + r"(?![\w])", disp) or disp == mt:
            cands.append(ln)
    if not cands:
        return emit("adjudication", key, "DEFECT",
                    "resolved to %r but no such wikilink displays %r" % (tgt, mt))
    if not os.path.exists(os.path.join(ROOT, "content", "cases", tgt + ".md")):
        return emit("adjudication", key, "DEFECT",
                    "resolved target page content/cases/%s.md does not exist" % tgt)
    return emit("adjudication", key, "OK")


# ---------------------------------------------------------------- lane semantic adjudications
#
# Rows whose MECHANICAL claim holds (the recorded link exists) but whose
# SEMANTIC claim fails on merits review: the wikilink points at the wrong
# case. Evidence gathered 2026-07-09 by the r9b lane (see findings).
SEMANTIC_OVERRIDES = {
    # bare [[Davis v. United States]] resolves to the 1994 Miranda
    # ambiguous-invocation page; these good-faith contexts mean Davis v.
    # United States (2011), 564 U.S. 229. Class: 4 prose + 3 frontmatter
    # instances corpus-wide (SIA Vehicles:23, Belton:87+48, Leon:67+33,
    # Sheppard:65+31); the 2011 page itself documents the bare-link trap.
    "content/cases/Massachusetts v. Sheppard.md:65:Davis v. United States:linked":
        "wrong-target: bare [[Davis v. United States]] = 1994 Miranda page, but "
        "context ('binding precedent' good-faith line) = Davis v. United States "
        "(2011); class instance (F-S9-R9B finding)",
    "content/cases/New York v. Belton.md:87:Davis v. United States:linked":
        "wrong-target: bare [[Davis v. United States]] = 1994 Miranda page, but "
        "context ('pre-Gant reliance on Belton') = Davis v. United States (2011); "
        "class instance (F-S9-R9B finding)",
    # [[Mathews v. United States|Mathews]] (485 U.S. 58, entrapment) linked in a
    # sentence whose 'Mathews' is Mathews v. Eldridge (424 U.S. 319, DP
    # balancing test named in the same sentence). Isolated instance.
    "content/cases/Culley v. Marshall.md:62:Mathews v. United States:linked":
        "wrong-target: [[Mathews v. United States|Mathews]] (1988 entrapment) "
        "linked where the sentence's Mathews = Mathews v. Eldridge balancing "
        "test; underlying caption error in prose (F-S9-R9B finding)",
}


def apply_overrides():
    for row in rows_out:
        det = SEMANTIC_OVERRIDES.get(row.get("key"))
        if det and row["kind"] == "mention":
            row["verdict"] = "DEFECT"
            row["detail"] = det


# ---------------------------------------------------------------- drive

def main():
    mentions = sorted(LED["mentions"],
                      key=lambda r: (r["file"], r.get("line") or 0,
                                     r.get("caption_key") or ""))
    sample_m = mentions[0::10]
    for r in sample_m:
        check_mention(r)

    pincites = sorted(LED["pincites"],
                      key=lambda r: (r["file"], r.get("pin_id") or "", r["action"]))
    sample_p = pincites[0::10]
    for r in sample_p:
        check_pincite(r)

    for r in LED["embeds"]:
        check_embed(r)

    tpages = sorted(LED["terms"]["pages"].keys())
    for pg in tpages[0::10]:
        check_term_page(pg, LED["terms"]["pages"][pg])

    for r in RES:
        check_adjudication(r)

    apply_overrides()

    with open(OUT, "w", encoding="utf-8") as fh:
        for row in rows_out:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    # summary
    from collections import Counter
    c = Counter((r["kind"], r["verdict"]) for r in rows_out)
    kinds = ["mention", "pincite", "embed", "term-page", "adjudication"]
    for k in kinds:
        ok, df = c.get((k, "OK"), 0), c.get((k, "DEFECT"), 0)
        print("%-13s checked %4d  OK %4d  DEFECT %d" % (k, ok + df, ok, df))
    print("TOTAL", len(rows_out))
    for r in rows_out:
        if r["verdict"] == "DEFECT":
            print("DEFECT:", json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
