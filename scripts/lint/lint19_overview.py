#!/usr/bin/env python3
"""
LINT-19 — overview pages.  S3 · R2 (alias LINT-S3-overview; S9 R8 roster row 19).

R2: every category AND every sub-umbrella carries an authored overview — broad,
plain-English, an on-ramp to its children — and NO key-case tables (those live
on doctrine/case pages, S5/S7). The overview is stored as the node's `index.md`.

For every category / sub-umbrella `index.md` this enforces two things (HIGH):

  (1) NON-EMPTY BODY — more than frontmatter + a single stub line. Threshold:
      at least 2 non-heading, non-blank prose lines in the body (the pre-overhaul
      8-line "Category overview — see the pages in this section." stub has exactly
      one and fails).
  (2) NO CASE TABLE — no GFM table whose header row classifies as a Case-schema
      table (per `_common.classify_case_header`: any column resolves to the
      'case' role). Overviews route to children; case tables belong on entries.

SCOPE — the category + sub-umbrella overviews, i.e. every `index.md` under
`content/` EXCEPT the site root `content/index.md` (the master index, not a
taxonomy node) and `content/cases/index.md` (the R13(d) router landing, not an
overview).

SELF-TEST (S1 A3): `python3 lint19_overview.py --self-test` over the labeled
`fixtures/lint-19-*.md` pages (filename suffix `-pass` / `-fail`).

Usage:
  python3 lint19_overview.py [glob ...]
  python3 lint19_overview.py --self-test
"""

import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-19"

MIN_PROSE_LINES = 2  # >= 2 non-heading, non-blank body lines => not a stub


def _is_overview_index(path):
    """True iff `path` is a category / sub-umbrella index.md overview (i.e. an
    index.md in a SUBFOLDER of content/, excluding content/cases/)."""
    rel = os.path.relpath(path, c.CONTENT_ROOT).replace(os.sep, "/")
    if os.path.basename(rel).lower() != "index.md":
        return False
    if rel == "index.md":            # site root master index — not a taxonomy node
        return False
    if rel == "cases/index.md":       # ONLY the R13(d) router landing is exempt —
        return False                  # a nested content/cases/<x>/index.md overview
    return True                       # is still checked (spec exempts only the landing)


def check_overview_body(path):
    """The R2 body + no-case-table checks for a single overview index.md."""
    out = []
    text = c.read_text(path)
    _fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    # table lines (header + separator + data rows) — NOT authored on-ramp prose,
    # so they must not satisfy the non-stub threshold (a table-only body is a
    # stub). Collected once and reused for the no-case-table check.
    table_lines = set()
    case_table_viols = []
    for hidx, header_cells, rows in c.iter_tables(body_lines):
        table_lines.add(hidx)
        table_lines.add(hidx + 1)   # separator row
        table_lines.update(rows)
        kinds = [c.classify_case_header(h) for h in header_cells]
        if "case" in kinds:
            case_table_viols.append(c.make_violation(
                LINT, path, start + hidx, c.HIGH,
                "overview contains a case table %s — key-case tables live on "
                "doctrine/case pages, never on an overview [R2]" % header_cells))

    # (1) non-empty body: >= MIN_PROSE_LINES non-heading, non-blank, non-TABLE lines
    prose = 0
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if i in table_lines:
            continue
        if line.strip() == "":
            continue
        if c.HEADING_RE.match(line):
            continue
        prose += 1
    if prose < MIN_PROSE_LINES:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "overview body is a stub (%d non-heading, non-table prose line(s); "
            "needs >= %d) — every category + sub-umbrella carries an authored, "
            "on-ramp overview [R2]" % (prose, MIN_PROSE_LINES)))

    # (2) no case table
    out.extend(case_table_viols)
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        if _is_overview_index(path):
            out.extend(check_overview_body(path))
    return out


# --------------------------------------------------------------------------
# self-test — labeled fixtures (filename suffix -pass / -fail)
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-19-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-19-*.md fixtures\n")
        return 1
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_overview_body(f)
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
