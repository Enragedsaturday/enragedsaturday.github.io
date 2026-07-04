#!/usr/bin/env python3
"""
LINT-16 — case-tables (S5 R6/R7/R13/R17).  'LINT-16 case-tables'.

For every GFM table that has a Case/Name column, enforces the drift-killer set:

  * SCHEMA (R6): the header row matches ONE of the three sanctioned schemas
    EXACTLY (string-for-string):
        | Case | Holding | Opinion |
        | Case | Relevance here | Primary home | Opinion |
        | Case | Primary home | Opinion |
  * NO AUTHORED DATA in rows (R7/R13): authority-weight allowlist labels, Field-I
    / legacy treatment status tokens, and date patterns grep to ZERO inside the
    rows — data renders via injection, never authored cells.
      CARVE-OUT: the R5 point-status table `| Point of law | Status | Controlling
      authority |` is the ONE sanctioned authored rendering (skipped entirely).
  * ONE ANCHOR TEXT (R6/TEACH-13): every opinion link's anchor text is `opinion`.
  * SELF-REFERENCE BAN (R6): a Related row whose Primary home is the CURRENT page
    is an error (it belongs in Key cases).
  * OPINION-LINK HOST (R17): every opinion link's host ∈ CourtListener ∪ the
    whitelisted fallbacks (Justia · Google Scholar · Cornell LII · official court
    sites) — implemented as the OPINION_HOST_WHITELIST constant below.

Violations are HIGH — R6/R7 make table drift structurally impossible. The
pre-overhaul + mid-restructure corpus lights up heavily (every unconverted table
fails the schema check); that is the expected red state until S7 runs
convert_tables.py. S9 wires this into CI.

SELF-TEST (S1 A3): `python3 lint16_casetables.py --self-test` over the labeled
`fixtures/lint-16-*.md` pages (filename suffix `-pass` / `-fail`).

Usage:
  python3 lint16_casetables.py [glob ...]
  python3 lint16_casetables.py --self-test
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-16"

# R17 — opinion-link host whitelist (a CONSTANT, per the spec). CourtListener plus
# the S2 R14 fallback order: Justia -> Google Scholar -> Cornell LII -> official
# court/reporter sites (allowed by government-domain suffix).
OPINION_HOST_WHITELIST = {
    "courtlistener.com", "www.courtlistener.com",
    "justia.com", "law.justia.com", "supreme.justia.com", "cases.justia.com",
    "scholar.google.com",
    "law.cornell.edu", "www.law.cornell.edu",
    "supremecourt.gov", "www.supremecourt.gov",
}
# official court/reporter sites (R17 "official court sites"): government domains.
OFFICIAL_HOST_SUFFIXES = (".uscourts.gov", ".gov", ".us")

# R7 — authority-weight allowlist label strings (S1 A8). Their presence in a case
# table row is authored data (the weight box injects it).
WEIGHT_LABEL_STRINGS = [
    "Binding — SCOTUS",
    "Binding in-circuit",
    "Persuasive (outside circuit)",
    "Persuasive only — non-precedential",
    "Persuasive — state, illustrative",
]

# R7/R13 — Field-I / legacy treatment status tokens (whole-cell data values).
STATUS_TOKEN_RE = re.compile(
    r"^\**\s*(good law|good|limited|criticized|overruled|abrogated|superseded|"
    r"caution|questioned|history|unverified)\b", re.IGNORECASE)
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

# the R5 carve-out table header (skipped)
R5_CARVEOUT = ["point of law", "status", "controlling authority"]


def _host(url):
    m = re.match(r"https?://([^/]+)", url.strip())
    if not m:
        return ""
    return m.group(1).lower().split(":")[0]


def _host_ok(host):
    if host in OPINION_HOST_WHITELIST:
        return True
    return any(host == s.lstrip(".") or host.endswith(s) for s in OFFICIAL_HOST_SUFFIXES)


def _strip_md(text):
    t = re.sub(r"\*+", "", text)
    t = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return t.strip()


def _page_identity(path, fm):
    """Normalized set of names that resolve to THIS page (for the self-ref ban)."""
    names = {os.path.splitext(os.path.basename(path))[0]}
    for key in ("title", "topic"):
        v = fm.get(key)
        if isinstance(v, str) and v.strip():
            names.add(v)
    aliases = fm.get("aliases")
    if isinstance(aliases, list):
        names.update(a for a in aliases if isinstance(a, str))
    elif isinstance(aliases, str) and aliases.strip():
        names.add(aliases)
    return {c.CorpusIndex.norm(n) for n in names}


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    identity = _page_identity(path, fm)

    for hidx, header_cells, rows in c.iter_tables(body_lines):
        norm_header = [h.strip().lower() for h in header_cells]
        if norm_header == R5_CARVEOUT:
            continue  # R5 point-status table — the one sanctioned authored table
        kinds = [c.classify_case_header(h) for h in header_cells]
        if "case" not in kinds:
            continue  # not a case table

        hline = start + hidx

        # (1) exact schema header
        if not any(header_cells == hdrs for (hdrs, _roles) in c.CASE_TABLE_SCHEMAS.values()):
            out.append(c.make_violation(
                LINT, path, hline, c.HIGH,
                "non-sanctioned Case-table header %s — must match a sanctioned "
                "schema exactly (Key cases / Related / Case Index) [R6]"
                % header_cells))

        # column roles for targeted checks
        col_of = {}
        for idx, k in enumerate(kinds):
            col_of.setdefault(k, idx)
        opinion_col = col_of.get("opinion")
        home_col = col_of.get("home")

        for ridx in rows:
            rline = start + ridx
            cells = c.split_table_row(body_lines[ridx])

            # (2) authored-data tokens (R7/R13)
            for cell in cells:
                for lbl in WEIGHT_LABEL_STRINGS:
                    if lbl in cell:
                        out.append(c.make_violation(
                            LINT, path, rline, c.HIGH,
                            "authored authority-weight label '%s' in a case-table "
                            "row — weight renders via injection, never a cell [R7]"
                            % lbl))
                        break
                if ISO_DATE_RE.search(cell):
                    out.append(c.make_violation(
                        LINT, path, rline, c.HIGH,
                        "authored date in a case-table row ('%s') — dates are "
                        "hover-only inside entries [R13]"
                        % ISO_DATE_RE.search(cell).group(0)))
                if STATUS_TOKEN_RE.match(cell) and (
                        ISO_DATE_RE.search(cell) or len(_strip_md(cell)) <= 25):
                    out.append(c.make_violation(
                        LINT, path, rline, c.HIGH,
                        "authored treatment-status token in a case-table row "
                        "('%s') — treatment renders via injection [R7]"
                        % _strip_md(cell)[:30]))

            # (3) opinion anchor text + (R17) host — check every md-url link in the row
            for cell in cells:
                for m in c.MDLINK_URL_RE.finditer(cell):
                    anchor, url = m.group(1).strip(), m.group(2)
                    if anchor.lower() != "opinion":
                        out.append(c.make_violation(
                            LINT, path, rline, c.HIGH,
                            "opinion link anchor text is '%s' — the one sanctioned "
                            "anchor text is 'opinion' [R6/TEACH-13]" % anchor))
                    host = _host(url)
                    if host and not _host_ok(host):
                        out.append(c.make_violation(
                            LINT, path, rline, c.HIGH,
                            "opinion link host '%s' is not CourtListener or a "
                            "whitelisted fallback (Justia/Scholar/Cornell/official "
                            "court site) [R17]" % host))

            # (4) self-reference ban (Related rows)
            if home_col is not None and home_col < len(cells):
                for wl in c.WIKILINK_RE.finditer(cells[home_col]):
                    target = wl.group(1).split("|")[0].split("#")[0].split("/")[-1]
                    if c.CorpusIndex.norm(target) in identity:
                        out.append(c.make_violation(
                            LINT, path, rline, c.HIGH,
                            "self-reference: Related row's Primary home '[[%s]]' is "
                            "the current page — it belongs in Key cases [R6]"
                            % target.strip()))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test — labeled fixtures (filename suffix -pass / -fail)
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-16-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-16-*.md fixtures\n")
        return 1
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_file(f)
        passed = (len(viols) == 0) if expect == "pass" else (len(viols) > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-32s expect=%-4s -> %s (%d viol)\n" % (
            name, expect, "OK" if passed else "MISMATCH", len(viols)))
        if not passed:
            for v in viols:
                sys.stderr.write("             %s\n" % v["message"])
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
