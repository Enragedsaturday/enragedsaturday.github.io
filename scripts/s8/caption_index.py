#!/usr/bin/env python3
"""
S8 caption index builder (spec S8 R1/R3 · work order Deliverable 1).

Merges THREE local sources (no CourtListener, stdlib only) into
`_run/o2-execute/s8-caption-index.json` — the resolution truth the R1-R3
linker (`link_cases.py`) consumes:

  1. Lake       `_overhaul2/lake/cases/*.json`   — identity.case_name(_short|_full),
                                                    input_case_name, status, record_id.
  2. Case pages `content/cases/*.md`             — stem + frontmatter `aliases:`
                                                    (the WIKILINK TRUTH: a mention
                                                    links only to an existing stem/alias).
  3. Coverage   `_run/s6-coverage-ledger.json`   — caption/canonical -> `terminal`
                                                    (the R1 ledger rule).

Model (verified against the corpus 2026-07-09):
  * 610 case pages are the link-target universe; page-existence drives linking.
  * The ledger's 252 captions are the S6 CANDIDATE universe, not the page census:
    151 `authored` rows are a subset of the pages; the other 101 rows are NON-PAGE
    terminals (`brief-mention` / `excluded-remit` / `folded-alias` / `removed` /
    `unverifiable` / `watch`) and are DISJOINT from every page stem/alias (0 conflicts).
    They are the fail-closed "keep PLAIN, never resurrect" set (R1 / COH-15).

Output per caption entry:
  {caption_key, page_stem|null, terminal|null, sources[], short_names[],
   variants[], record_status|null}
Plus derived lookups the linker binds:
  full_captions : {display_string -> caption_key}     (1:1 non-colliding)
  short_names   : {short_name    -> [caption_key...]}
  collision_map : {key -> {type: short-name|caption, pages:[...]}}  (>1 PAGE ⇒ ambiguous;
                  feeds the R3 ladder rung-3 fail-closed)

Short-name derivation: identity.case_name_short when present; else the surname of the
first NON-governmental party (United States v. X -> X; X v. State -> X). Single-token
frontmatter aliases (e.g. "Whren") are also short names; multi-word / "v."-bearing
aliases + case_name_full + input_case_name are full-caption variants.

Python 3 stdlib only. READ-ONLY on the corpus; writes only the one _run artifact.
Run `python3 scripts/s8/caption_index.py [--out PATH]`.
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAKE_DIR = os.path.join(ROOT, "_overhaul2", "lake", "cases")
CASES_DIR = os.path.join(ROOT, "content", "cases")
LEDGER = os.path.join(ROOT, "_run", "s6-coverage-ledger.json")
OUT = os.path.join(ROOT, "_run", "o2-execute", "s8-caption-index.json")

LANE = "s8-caption-index"
MODEL = "claude-opus-4-8"

NONPAGE_TERMINALS = (
    "brief-mention", "excluded-remit", "folded-alias",
    "removed", "unverifiable", "watch",
)

# --------------------------------------------------------------------------
# Governmental-party lexicon (for surname derivation)
# --------------------------------------------------------------------------

US_STATES = {
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
    "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
    "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
    "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
    "south dakota", "tennessee", "texas", "utah", "vermont", "virginia",
    "washington", "west virginia", "wisconsin", "wyoming",
    "district of columbia", "puerto rico",
}
_GOV_PREFIX = (
    "city of ", "county of ", "town of ", "township of ", "village of ",
    "state of ", "people of ", "commonwealth of ", "district of ",
    "department of ", "board of ",
)
_GOV_EXACT = {"united states", "united states of america", "people",
              "commonwealth", "state", "the people"}


def _is_governmental(party: str) -> bool:
    p = party.strip().lower().rstrip(".")
    if p in _GOV_EXACT:
        return True
    if p in US_STATES:
        return True
    if p.startswith("united states"):
        return True
    for pre in _GOV_PREFIX:
        if p.startswith(pre):
            return True
    return False


def _surname(party: str) -> str:
    """Last token of a party name (keeps internal hyphens/apostrophes)."""
    toks = party.strip().split()
    if not toks:
        return ""
    # drop trailing corporate/procedural noise tokens
    return toks[-1].strip(",")


def derive_short_name(caption: str):
    """Surname of the first non-governmental party, per the work-order convention.

    Returns None when the caption is not a two-party 'A v. B' form.
    """
    parts = re.split(r"\s+v\.\s+", caption)
    if len(parts) != 2:
        return None
    a, b = parts[0], parts[1]
    if not _is_governmental(a):
        return _surname(a)
    if not _is_governmental(b):
        return _surname(b)
    return _surname(a)


# --------------------------------------------------------------------------
# Parsing helpers
# --------------------------------------------------------------------------

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip()).casefold().rstrip(".")


_FM_ALIASES_INLINE = re.compile(r"^aliases:\s*(\[.*\])\s*$", re.M)


def _frontmatter(text: str):
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return ""
    return text[: end + 4]


def parse_aliases(text: str, source=None):
    fm = _frontmatter(text)
    if not fm:
        return []
    m = _FM_ALIASES_INLINE.search(fm)
    if m:
        try:
            arr = json.loads(m.group(1))
            return [str(a) for a in arr if str(a).strip()]
        except Exception as exc:
            # CR-S8-12: a page with a real but MALFORMED inline `aliases: [...]`
            # must not read as "no aliases" — case pages are the WIKILINK TRUTH,
            # so silently dropping their aliases weakens resolution without a
            # trace. Warn, then fall through to the block form.
            print("WARN: malformed inline aliases in %s: %s"
                  % (source or "<case page>", exc), file=sys.stderr)
    # block form:  aliases:\n  - "a"\n  - b
    out = []
    lines = fm.splitlines()
    for i, ln in enumerate(lines):
        if re.match(r"^aliases:\s*$", ln):
            for j in range(i + 1, len(lines)):
                m2 = re.match(r"^\s*-\s+(.*\S)\s*$", lines[j])
                if not m2:
                    break
                out.append(m2.group(1).strip().strip('"').strip("'"))
            break
    return [a for a in out if a]


def _looks_like_full_caption(s: str) -> bool:
    s = s.strip()
    if re.search(r"\sv\.\s", s):
        return True
    if re.match(r"^(In re|Ex parte|Matter of)\b", s):
        return True
    return False


def _is_short_token(s: str) -> bool:
    """A single surname-ish token (short name), not a full caption."""
    s = s.strip()
    if _looks_like_full_caption(s):
        return False
    # one or two words, first capitalized, no lowercase connectors implying a caption
    return bool(re.match(r"^[A-Z][A-Za-z.'’\-]*$", s))


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def build(cases_dir=None, lake_dir=None, ledger_path=None):
    cases_dir = cases_dir or CASES_DIR
    lake_dir = lake_dir or LAKE_DIR
    ledger_path = ledger_path or LEDGER
    entries = {}          # caption_key -> entry dict
    norm2key = {}         # normalized string -> caption_key (identity join)

    def get_entry(key):
        e = entries.get(key)
        if e is None:
            e = {
                "caption_key": key,
                "page_stem": None,
                "terminal": None,
                "sources": [],
                "short_names": set(),
                "variants": set(),
                "record_status": None,
                "record_id": None,
            }
            entries[key] = e
            norm2key.setdefault(_norm(key), key)
        return e

    def add_source(e, s):
        if s not in e["sources"]:
            e["sources"].append(s)

    # ---- Pass A: case pages (the wikilink truth) ----
    page_files = sorted(
        f for f in os.listdir(cases_dir) if f.endswith(".md")
    )
    n_pages = 0
    n_alias = 0
    for fn in page_files:
        stem = fn[:-3]
        n_pages += 1
        text = open(os.path.join(cases_dir, fn), encoding="utf-8").read()
        e = get_entry(stem)
        e["page_stem"] = stem
        add_source(e, "page")
        # a stem carrying a parenthetical year -> register the BARE form as a
        # variant (CR-S8-13). The bare caption ("Davis v. United States") is what
        # prose uses when only the "X (YYYY)" page exists; adding `stem` to its OWN
        # variant set was a no-op (it is already a stem norm, skipped downstream).
        # A genuine bare/year page pair is still fail-closed by the year-sibling
        # guard below, which routes the bare form to the ambiguity queue.
        m = re.match(r"^(.*\S)\s*\(\d{4}\)$", stem)
        if m:
            e["variants"].add(m.group(1))
        for a in parse_aliases(text, source=fn):
            n_alias += 1
            if _is_short_token(a):
                e["short_names"].add(a)
            else:
                e["variants"].add(a)
            norm2key.setdefault(_norm(a), stem)

    # ---- Pass B: lake identity ----
    lake_files = sorted(
        f for f in os.listdir(lake_dir) if f.endswith(".json")
    )
    n_lake = 0
    n_lake_skipped = 0
    n_lake_errors = 0
    for fn in lake_files:
        try:
            d = json.load(open(os.path.join(lake_dir, fn), encoding="utf-8"))
        except Exception as exc:
            # CR-S8-14: a corrupt/unreadable lake identity file for a real case
            # must not vanish with zero signal — this index feeds the R1-R3 linker
            # as resolution truth. Count + warn (unlike the tracked captionless
            # skip a broken record is a defect, not an expected placeholder).
            n_lake_errors += 1
            print("WARN: failed to parse lake record %s: %s" % (fn, exc),
                  file=sys.stderr)
            continue
        n_lake += 1
        idn = d.get("identity", {}) or {}
        rid = d.get("record_id")
        cname = idn.get("case_name")
        # not_found / caption-less placeholder records carry no display caption
        # (e.g. the slug-named `morgan-…--u2812…` not_found shells) — skip them:
        # they cannot form a linkable caption and the ledger owns their terminal.
        if not cname or not str(cname).strip():
            n_lake_skipped += 1
            continue
        # join to an existing page/entry by record_id or case_name
        key = None
        for probe in (rid, cname):
            if probe and _norm(probe) in norm2key:
                key = norm2key[_norm(probe)]
                break
        if key is None:
            key = cname
        e = get_entry(key)
        add_source(e, "lake")
        e["record_status"] = d.get("status")
        e["record_id"] = rid
        cshort = idn.get("case_name_short")
        cfull = idn.get("case_name_full")
        cinput = idn.get("input_case_name")
        if cshort and str(cshort).strip():
            if _is_short_token(cshort) or not _looks_like_full_caption(cshort):
                e["short_names"].add(str(cshort).strip())
            else:
                e["variants"].add(str(cshort).strip())
        for v in (cfull, cinput, cname):
            if v and _looks_like_full_caption(v) and _norm(v) != _norm(key):
                e["variants"].add(str(v).strip())
                norm2key.setdefault(_norm(v), key)

    # ---- Pass C: coverage ledger terminals ----
    # The ledger is the R1 AUTHORITY. Non-page terminals (brief-mention /
    # excluded-remit / folded-alias / removed / unverifiable / watch) are the
    # fail-closed "keep PLAIN, never resurrect" set: they win over any page
    # variant that happens to spell the same string (the folded-alias trap —
    # e.g. "Carman v. Carroll" must NOT link to the survivor "Carroll v. Carman").
    led = json.load(open(ledger_path, encoding="utf-8"))
    n_led = 0
    # ledger_nonpage: norm string -> {"display": caption, "terminal": t}
    ledger_nonpage = {}
    for row in led.get("rows", []):
        n_led += 1
        caption = row.get("caption")
        canon = row.get("canonical")
        term = row.get("terminal")
        # attach terminal to the merged entry (informational)
        key = None
        for probe in (caption, canon):
            if probe and _norm(probe) in norm2key:
                key = norm2key[_norm(probe)]
                break
        if key is None:
            key = caption or canon
        e = get_entry(key)
        add_source(e, "ledger")
        if e["terminal"] is None:
            e["terminal"] = term
        elif e["terminal"] != term:
            e.setdefault("terminal_alt", term)
        if term in NONPAGE_TERMINALS:
            for disp in (caption, canon):
                if disp and str(disp).strip():
                    ledger_nonpage.setdefault(
                        _norm(disp), {"display": disp, "terminal": term})

    # ---- Derive fallback short names (prefer lake / alias, else surname) ----
    for key, e in entries.items():
        if not e["short_names"]:
            ds = derive_short_name(key)
            if ds and _is_short_token(ds):
                e["short_names"].add(ds)

    # ---- Build linker lookups (exact-stem-wins + ledger fail-closed) ----
    stem_norms = {_norm(e["page_stem"]) for e in entries.values()
                  if e["page_stem"]}

    link_captions = {}          # display string -> page_stem   (auto-linkable)
    variant_owners = {}         # norm -> set(page_stem)  (non-stem variants)
    ambiguous_captions = {}     # norm -> {"display":..., "pages":[...]}

    for key, e in entries.items():
        stem = e["page_stem"]
        if not stem:
            continue
        # 1) the exact stem is authoritative and 1:1 (filesystem-unique)
        if _norm(stem) not in ledger_nonpage:
            link_captions[stem] = stem
        # 2) full-caption variants map to this stem unless a stem already owns
        #    the string, it is a ledgered non-page caption, or >1 page claims it
        for v in e["variants"]:
            if not _looks_like_full_caption(v):
                continue
            nv = _norm(v)
            if nv in ledger_nonpage:        # fail-closed: ledger keeps it plain
                continue
            if nv in stem_norms:            # exact stem already owns this string
                continue
            variant_owners.setdefault(nv, {})
            variant_owners[nv][stem] = v

    for nv, owners in variant_owners.items():
        if len(owners) == 1:
            (stem, disp), = owners.items()
            link_captions.setdefault(disp, stem)
        else:
            # a variant spelling claimed by >1 page and owned by no exact stem
            disp = sorted(owners.values())[0]
            ambiguous_captions[nv] = {"display": disp,
                                      "pages": sorted(owners.keys())}

    # Year-sibling ambiguity: a bare PAGE STEM "X" that also has a distinct
    # disambiguated sibling PAGE "X (YYYY)" is genuinely ambiguous in prose (the
    # year lives in the citation, which R2 masks) -> fail-closed, route the bare
    # form to the adjudication queue rather than auto-linking the wrong Davis.
    # (A mere "(YYYY)" alias of the SAME page is not a sibling and is fine.)
    all_stems = {e["page_stem"] for e in entries.values() if e["page_stem"]}
    for stem in sorted(all_stems):
        m = re.match(r"^(.*\S)\s*\(\d{4}\)$", stem)
        if m and m.group(1) in all_stems:
            base = m.group(1)
            ambiguous_captions[_norm(base)] = {
                "display": base, "pages": sorted({base, stem})}
            link_captions.pop(base, None)

    # plain_captions: the fail-closed keep-plain set (ledger non-page terminals)
    plain_captions = {v["display"]: v["terminal"]
                      for v in ledger_nonpage.values()}

    # ---- Short-name index: page owners (linkable) + plain owners (ledgered) ----
    short_index = {}            # norm short -> {"pages":set, "plain":set}
    for key, e in entries.items():
        stem = e["page_stem"]
        if not stem:
            continue
        for sn in e["short_names"]:
            ns = _norm(sn)
            short_index.setdefault(ns, {"pages": set(), "plain": set()})
            short_index[ns]["pages"].add(stem)
    for nv, meta in ledger_nonpage.items():
        disp = meta["display"]
        ds = derive_short_name(disp)
        if ds and _is_short_token(ds):
            ns = _norm(ds)
            short_index.setdefault(ns, {"pages": set(), "plain": set()})
            short_index[ns]["plain"].add(disp)

    collision_map = {}
    for ns, meta in short_index.items():
        if len(meta["pages"]) > 1:
            collision_map[ns] = {"type": "short-name",
                                 "pages": sorted(meta["pages"])}
    for nv, meta in ambiguous_captions.items():
        collision_map[nv] = {"type": "caption", "pages": meta["pages"]}

    # serialize entries (informational)
    out_entries = {}
    for key, e in entries.items():
        out_entries[key] = {
            "caption_key": key,
            "page_stem": e["page_stem"],
            "terminal": e["terminal"],
            "sources": e["sources"],
            "short_names": sorted(e["short_names"]),
            "variants": sorted(v for v in e["variants"]
                               if _looks_like_full_caption(v)),
            "record_status": e["record_status"],
        }

    short_names_out = {
        ns: {"pages": sorted(m["pages"]), "plain": sorted(m["plain"])}
        for ns, m in short_index.items()
    }
    full_captions = link_captions

    doc = {
        "generated_by": LANE,
        "model": MODEL,
        "spec": "S8 R1/R3 (caption resolution truth)",
        "sources": {
            "lake_records": n_lake,
            "lake_skipped_captionless": n_lake_skipped,
            "lake_parse_errors": n_lake_errors,
            "case_pages": n_pages,
            "case_page_aliases": n_alias,
            "ledger_captions": n_led,
        },
        "stats": {
            "total_entries": len(out_entries),
            "with_page": sum(1 for e in out_entries.values() if e["page_stem"]),
            "authored_terminal": sum(
                1 for e in out_entries.values()
                if e["terminal"] == "authored"),
            "lake_only_no_page_no_terminal": sum(
                1 for e in out_entries.values()
                if not e["page_stem"] and e["terminal"] is None
                and "lake" in e["sources"]),
            "link_caption_strings": len(link_captions),
            "plain_caption_strings": len(plain_captions),
            "short_name_keys": len(short_names_out),
            "ambiguous_caption_strings": len(ambiguous_captions),
            "collision_entries": len(collision_map),
            "short_name_collisions": sum(
                1 for v in collision_map.values()
                if v["type"] == "short-name"),
            "caption_collisions": sum(
                1 for v in collision_map.values() if v["type"] == "caption"),
        },
        "nonpage_terminal_enum": list(NONPAGE_TERMINALS),
        "entries": out_entries,
        "link_captions": link_captions,
        "plain_captions": plain_captions,
        "short_names": short_names_out,
        "ambiguous_captions": ambiguous_captions,
        "collision_map": collision_map,
    }
    return doc


# --------------------------------------------------------------------------
# self-test (hermetic — temp corpus, no live lake/pages)
# --------------------------------------------------------------------------

def _self_test():
    import io
    import tempfile
    import contextlib
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # ---- unit: parse_aliases warns + returns [] on malformed inline (CR-S8-12) ----
    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        got = parse_aliases('---\ntitle: X\naliases: [not valid json]\n---\nbody\n',
                            source="X.md")
    check(got == [], "CR-S8-12: malformed inline aliases should yield [], got %r" % got)
    check("malformed inline aliases in X.md" in buf.getvalue(),
          "CR-S8-12: no WARN emitted for malformed inline aliases")
    # a WELL-FORMED inline alias still parses (no regression)
    check(parse_aliases('---\naliases: ["Whren", "Whren v. US"]\n---\n') ==
          ["Whren", "Whren v. US"], "parse_aliases: well-formed inline broke")

    # ---- hermetic build() over a temp corpus (CR-S8-13, CR-S8-14) ----
    tmp = tempfile.mkdtemp()
    cases = os.path.join(tmp, "cases")
    lake = os.path.join(tmp, "lake")
    os.makedirs(cases)
    os.makedirs(lake)

    def page(stem, body="---\n---\nbody\n"):
        with open(os.path.join(cases, stem + ".md"), "w", encoding="utf-8") as fh:
            fh.write(body)

    # a YEAR-STEM page with NO bare sibling -> its bare form must auto-link
    page("Zeta v. State (2011)")
    # a genuine bare/year SIBLING pair -> the bare form must be fail-closed ambiguous
    page("Alpha v. State")
    page("Alpha v. State (2011)")
    # a corrupt lake record (CR-S8-14) + one good one
    with open(os.path.join(lake, "good.json"), "w", encoding="utf-8") as fh:
        json.dump({"record_id": "r1", "identity": {"case_name": "Zeta v. State"},
                   "status": "ok"}, fh)
    with open(os.path.join(lake, "broken.json"), "w", encoding="utf-8") as fh:
        fh.write("{ this is not valid json")
    ledger_p = os.path.join(tmp, "s6.json")
    with open(ledger_p, "w", encoding="utf-8") as fh:
        json.dump({"rows": []}, fh)

    buf = io.StringIO()
    with contextlib.redirect_stderr(buf):
        doc = build(cases_dir=cases, lake_dir=lake, ledger_path=ledger_p)
    lc = doc["link_captions"]
    amb = doc["ambiguous_captions"]

    # CR-S8-13: bare form of a lone year-stem page is an auto-linkable caption
    check("Zeta v. State" in lc and lc["Zeta v. State"] == "Zeta v. State (2011)",
          "CR-S8-13: bare form of a lone year-stem page not registered -> %s"
          % [k for k in lc if "Zeta" in k])
    # the OLD no-op behaviour (adding the stem to its own variants) never produced
    # this; assert the bare form was NOT wrongly left out
    check(_norm("Zeta v. State") in {_norm(k) for k in lc},
          "CR-S8-13: bare year-stem caption missing from link_captions")
    # year-sibling pair stays fail-closed (bare form ambiguous, not auto-linked)
    check(_norm("Alpha v. State") in amb,
          "CR-S8-13: genuine bare/year sibling not routed to ambiguity")
    check("Alpha v. State" not in lc,
          "CR-S8-13: ambiguous bare/year sibling must NOT be auto-linkable")

    # CR-S8-14: the broken lake record is counted + surfaced, not silently dropped
    check(doc["sources"]["lake_parse_errors"] == 1,
          "CR-S8-14: broken lake record not counted (%s)"
          % doc["sources"]["lake_parse_errors"])
    check("failed to parse lake record broken.json" in buf.getvalue(),
          "CR-S8-14: no WARN emitted for the broken lake record")
    check(doc["sources"]["lake_records"] == 1,
          "CR-S8-14: good lake record miscounted (%s)" % doc["sources"]["lake_records"])

    import shutil
    shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        print("caption_index.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("caption_index.py --self-test: PASS "
          "(alias-parse-warn / year-stem bare variant / year-sibling fail-closed / "
          "lake parse-error counter+warn)")
    return 0


def main(argv):
    if "--self-test" in argv:
        return _self_test()
    out = OUT
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]
    doc = build()
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=False)
        fh.write("\n")
    s = doc["stats"]
    print("s8-caption-index written:", out)
    print("  sources:", json.dumps(doc["sources"]))
    print("  entries:", s["total_entries"],
          "| with_page:", s["with_page"],
          "| authored:", s["authored_terminal"],
          "| lake_only_gray:", s["lake_only_no_page_no_terminal"])
    print("  link_captions:", s["link_caption_strings"],
          "| plain_captions:", s["plain_caption_strings"],
          "| short_name_keys:", s["short_name_keys"],
          "| ambiguous_captions:", s["ambiguous_caption_strings"])
    print("  collisions:", s["collision_entries"],
          "(short-name:", s["short_name_collisions"],
          "caption:", s["caption_collisions"], ")")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
