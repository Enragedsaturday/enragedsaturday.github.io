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
  * OPINION-LINK HOST (R17): every opinion link's host ∈ CourtListener or the
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
from urllib.parse import urlsplit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-16"

# R17 — opinion-link host whitelist (F-S5-06). An EXACT host set for the S2 R14
# fallback chain (CourtListener -> Justia -> Google Scholar -> Cornell LII). No
# broad `.gov`/`.us` suffix acceptance — `evil.us` / `evil.gov` must NOT pass.
OPINION_HOST_WHITELIST = frozenset({
    "www.courtlistener.com", "courtlistener.com",
    "law.justia.com", "supreme.justia.com",
    "scholar.google.com",
    "www.law.cornell.edu", "law.cornell.edu",
})
# EXTENSIBLE — official court/reporter hosts (R17 "official court/reporter site").
# Add vetted government court hosts here as the corpus needs them. Seed: the
# Supreme Court's own site. Kept as an exact-host set (apex + www) so it never
# widens into a broad `.gov` accept.
OFFICIAL_COURT_HOSTS = frozenset({
    "www.supremecourt.gov", "supremecourt.gov",
    "uscourts.gov",
})
# The federal Judiciary's per-court subdomains (ca9.uscourts.gov, cand.uscourts.gov,
# …) are all under the government-controlled `.uscourts.gov` zone — matched by
# suffix. This is the ONLY suffix accept (a specific, government-owned zone).
OFFICIAL_COURT_HOST_SUFFIXES = (".uscourts.gov",)

# R7 — authority-weight allowlist detection (S1 A8, full six tiers incl.
# 'Historical'). Sourced from the ONE canonical allowlist in _common (F-S5-07);
# see c.weight_label_in_cell.

# R7/R13 — Field-I / legacy treatment status tokens (whole-cell data values).
STATUS_TOKEN_RE = re.compile(
    r"^\**\s*(good law|good|limited|criticized|overruled|abrogated|superseded|"
    r"caution|questioned|history|unverified)\b", re.IGNORECASE)
ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

# the R5 carve-out table header (skipped)
R5_CARVEOUT = ["point of law", "status", "controlling authority"]

# F-S5-04 carve-out (RULING P4-16(b)) — the GENERATED master Case Index.
# `scripts/build_case_index.py` emits a richer 5-column index than the bare
# `| Case | Primary home | Opinion |` reference schema: it prints the projected
# one-line holding, the projected Good-law status glyph/token (S4-R10 REQUIRES a
# non-blank Good-law cell — "no blank treatment cell"), the home doctrine page(s),
# and the CourtListener opinion link. These cells are a projection of case-page
# frontmatter + the S8 term-linker, NOT authored data, so on the Case Index page
# (and ONLY there) this generated header is accepted, the authored-data-cell
# checks (treatment token / weight label / ISO date) do not apply to the generated
# columns, and a no-CL case may carry the generated "—" opinion sentinel (pre-CL
# English cases like Entick/Wilkes, page-less flagged-omit rows, and the index
# self-row all legitimately have no CourtListener opinion).
GENERATED_INDEX_HEADER = ["Case", "Holding", "Good law", "Home page(s)", "CourtListener"]
# the generated no-opinion sentinel: an Opinion cell that is empty or only dash
# characters (em/en dash, hyphen, minus) after markdown-stripping.
_NO_CL_SENTINEL_RE = re.compile(r"^[\s—–‒‐‑−-]*$")


def _host(url):
    """Extract the real host of an opinion link. Uses urllib.parse.urlsplit so
    URL userinfo (`https://www.courtlistener.com:x@evil.com/…`) cannot smuggle a
    whitelisted string past the R17 check — urlsplit().hostname returns the true
    host (`evil.com`), not the userinfo. Non-http(s) schemes and hostless URLs
    (`https:///…`) yield '' (rejected by the empty-host guard at the call site)."""
    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return ""
    if parts.scheme not in ("http", "https"):
        return ""
    return (parts.hostname or "").lower()


def _host_ok(host):
    if host in OPINION_HOST_WHITELIST or host in OFFICIAL_COURT_HOSTS:
        return True
    # ONLY the government-owned `.uscourts.gov` zone is accepted by suffix.
    return any(host.endswith(s) for s in OFFICIAL_COURT_HOST_SUFFIXES)


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


def _is_case_index_page(path, fm):
    """The reference/router Case Index is the ONLY page where the bare
    `| Case | Primary home | Opinion |` schema is accepted (F-S5-04)."""
    stem = os.path.splitext(os.path.basename(path))[0].strip().lower()
    if stem == "case index":
        return True
    title = fm.get("title")
    if isinstance(title, str) and title.strip().lower() == "case index":
        return True
    return False


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    identity = _page_identity(path, fm)
    is_index_page = _is_case_index_page(path, fm)

    # H2 section map (for the section-aware schema requirement, F-S5-04)
    secs = c.sections(body_lines)

    def _section_title_for(idx):
        for s in secs:
            if s["start"] <= idx < s["end"]:
                return s["title"]
        return None

    for hidx, header_cells, rows in c.iter_tables(body_lines):
        norm_header = [h.strip().lower() for h in header_cells]
        if norm_header == R5_CARVEOUT:
            continue  # R5 point-status table — the one sanctioned authored table
        kinds = [c.classify_case_header(h) for h in header_cells]
        if "case" not in kinds:
            continue  # not a case table

        hline = start + hidx

        # (1) SCHEMA — exact header AND section-appropriate (F-S5-04)
        sec_title = _section_title_for(hidx)
        required = c.section_schema_kind(sec_title)  # 'related'|'key'|'index'|None
        actual = c.schema_of_header(header_cells)     # exact schema key or None
        sec_label = sec_title.strip() if sec_title else "(no section)"
        # F-S5-04 (RULING P4-16(b)): the generated 5-column master-index header is
        # accepted on the Case Index page only (S4-R10 mandates the Good-law column).
        is_generated_index = is_index_page and header_cells == GENERATED_INDEX_HEADER
        if is_generated_index:
            pass  # generated master-index schema — no authored-header defect
        elif actual is None:
            if required is not None:
                want = c.CASE_TABLE_SCHEMAS[required][0]
                out.append(c.make_violation(
                    LINT, path, hline, c.HIGH,
                    "non-sanctioned Case-table header %s under '## %s' — this "
                    "section requires the %s schema %s [R6]"
                    % (header_cells, sec_label, required, want)))
            else:
                out.append(c.make_violation(
                    LINT, path, hline, c.HIGH,
                    "non-sanctioned Case-table header %s — must match a sanctioned "
                    "schema exactly (Key cases / Related / Case Index) [R6]"
                    % header_cells))
        elif required is not None and actual != required:
            want = c.CASE_TABLE_SCHEMAS[required][0]
            out.append(c.make_violation(
                LINT, path, hline, c.HIGH,
                "wrong schema for '## %s': found the %s schema %s, but this "
                "section requires the %s schema %s [R6]"
                % (sec_label, actual, header_cells, required, want)))
        elif required is None and actual == "index" and not is_index_page:
            out.append(c.make_violation(
                LINT, path, hline, c.HIGH,
                "Case Index schema %s is reserved for the Case Index page (or a "
                "'## Case Index' section) — use Key cases or Related here [R6]"
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

            # (2) authored-data tokens (R7/R13).
            # F-S5-04 (RULING P4-16(b)): skip on the generated Case Index — its
            # Good-law / Holding cells are projected (build_case_index.py) from
            # frontmatter, not authored. A leaked weight-label or ISO-date prefix
            # inside a projected holding is a source-frontmatter matter (fix the
            # case-page `holding:`, then regenerate), never an index-authoring defect.
            for cell in ([] if is_index_page else cells):
                wlbl = c.weight_label_in_cell(cell)  # full A8 allowlist incl. Historical
                if wlbl:
                    out.append(c.make_violation(
                        LINT, path, rline, c.HIGH,
                        "authored authority-weight label '%s' in a case-table "
                        "row — weight renders via injection, never a cell [R7]"
                        % wlbl))
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

            # (3) OPINION COLUMN ONLY (F-S5-08): exactly one opinion link
            # (F-S5-01), exact-case 'opinion' anchor (F-S5-05), whitelisted
            # host (F-S5-06/R17). Links in other columns are NOT opinion links.
            if opinion_col is not None and opinion_col >= len(cells):
                # SHORT ROW: iter_tables admits a row one cell shorter than the
                # header, so a row missing its Opinion cell would otherwise skip
                # every opinion check silently. Flag it (fail-closed).
                out.append(c.make_violation(
                    LINT, path, rline, c.HIGH,
                    "case-table row is missing its Opinion cell (%d cells, Opinion "
                    "is column %d) — every Key-cases/Related/Index row carries one "
                    "'opinion' link [R6/R17]" % (len(cells), opinion_col + 1)))
            elif opinion_col is not None:
                ocell = cells[opinion_col]
                links = list(c.MDLINK_URL_RE.finditer(ocell))
                # F-S5-04 (RULING P4-16(b)): on the generated Case Index a no-CL case
                # renders the "—" opinion sentinel (pre-CL English cases, page-less
                # flagged-omit rows, the index self-row). Accept 0 links iff the cell
                # is that generated sentinel; a real link is still anchor/host-checked
                # below, and a double-linked cell still fails.
                sentinel_ok = (is_index_page and len(links) == 0
                               and _NO_CL_SENTINEL_RE.match(_strip_md(ocell)))
                if len(links) != 1 and not sentinel_ok:
                    out.append(c.make_violation(
                        LINT, path, rline, c.HIGH,
                        "Opinion column must carry exactly one non-empty opinion "
                        "link, found %d [R6/R17]" % len(links)))
                for m in links:
                    anchor, url = m.group(1).strip(), m.group(2)
                    if anchor != "opinion":          # EXACT case (F-S5-05)
                        out.append(c.make_violation(
                            LINT, path, rline, c.HIGH,
                            "opinion link anchor text is '%s' — the one sanctioned "
                            "anchor text is exactly 'opinion' [R6/TEACH-13]"
                            % anchor))
                    host = _host(url)
                    if not host or not _host_ok(host):
                        # empty host = a hostless `https:///…` or non-http scheme;
                        # a non-empty host that is not whitelisted. Both fail R17.
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
