#!/usr/bin/env python3
"""
LINT-23 — order / weight.  S3 · R10 + A8(c) (alias LINT-S3-order; S9 R8 roster
row 23).  Realizes Amendment A8(c) EXACTLY.

Intra-category order is authored, not alphabetical, and (per A8, user decision
2026-07-03) is encoded via a frontmatter `weight:` field — filenames/slugs carry
no ordering numbers. This lint enforces the ONE fail condition A8(c) defines:

  * Every in-scope file carries a `weight:` that is a POSITIVE INTEGER.
    Missing weight, or a non-positive / non-integer weight => HIGH.

Gap spacing (the 10/20/30 convention) and tie values are ADVISORY ONLY — they
NEVER fail and produce NO output (A8(c): "a normative gap rule would fail
legitimate mid-gap inserts"; ties break alphabetically by slug and are legal).

SCOPE (A8(c)) — every explorer-listed content page under `content/`, and every
category and sub-umbrella `index.md`.

EXCLUSIONS — single-sourced with the explorer `filterFn` in `quartz.layout.ts`
(A8(c): "the lint reads the SAME exclusion list as the filterFn, single-sourced").
The filterFn drops top-level slug segments {tags, about, cases}; A8(c) adds the
site root `content/index.md` (not an explorer node). `content/cases/**` (incl.
`cases/index.md`, the R13(d) router landing) is covered by the `cases` segment.
  >>> If quartz.layout.ts's filterFn changes, update EXPLORER_EXCLUDED_SEGMENTS
  >>> to match — this constant IS the single source mirrored from that filterFn.

SELF-TEST (S1 A3): `python3 lint23_order_weight.py --self-test` over the labeled
`fixtures/lint-23-*.md` pages (filename suffix `-pass` / `-fail`).

Usage:
  python3 lint23_order_weight.py [glob ...]
  python3 lint23_order_weight.py --self-test
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-23"

# SINGLE SOURCE — mirrors quartz.layout.ts `categoryExplorer.filterFn`:
#     node.slugSegment !== "tags" && !== "about" && !== "cases"
# (A8(c): the lint reads the same exclusion list as the filterFn.)
EXPLORER_EXCLUDED_SEGMENTS = frozenset({"tags", "about", "cases"})

_POSITIVE_INT_RE = re.compile(r"^\d+$")


def _first_segment_slug(rel):
    """The top-level slug segment of a content-relative path (mirrors Quartz's
    `slugSegment` for the first level): the first path component, with a trailing
    `.md` stripped for a top-level FILE (e.g. `about.md` -> `about`)."""
    first = rel.split("/")[0]
    if first.endswith(".md"):
        first = first[:-3]
    return first


def _in_scope(rel):
    """True iff this content-relative path is an explorer-listed page or a
    category/sub-umbrella index.md that A8(c) requires to carry `weight:`."""
    if rel == "index.md":                                  # site root master index
        return False
    if _first_segment_slug(rel) in EXPLORER_EXCLUDED_SEGMENTS:  # tags/about/cases
        return False
    return True


def _weight_ok(weight):
    """A8(c): weight must be a positive integer. Accept int or a digit string."""
    if isinstance(weight, bool):
        return False
    if isinstance(weight, int):
        return weight > 0
    if isinstance(weight, str):
        s = weight.strip()
        return bool(_POSITIVE_INT_RE.match(s)) and int(s) > 0
    return False


def check_weight(path):
    """The A8(c) positive-integer-weight check for a single in-scope file."""
    fm, _body, _start = c.split_frontmatter(c.read_text(path))
    weight = fm.get("weight")
    if not _weight_ok(weight):
        return [c.make_violation(
            LINT, path, 1, c.HIGH,
            "missing or non-positive-integer `weight:` (found %r) — every "
            "explorer-listed page and every category/sub-umbrella index.md "
            "carries a positive-integer weight [R10/A8(c)]" % (weight,))]
    return []


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        rel = os.path.relpath(path, c.CONTENT_ROOT).replace(os.sep, "/")
        if _in_scope(rel):
            out.extend(check_weight(path))
    return out


# --------------------------------------------------------------------------
# self-test — labeled fixtures (filename suffix -pass / -fail)
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-23-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-23-*.md fixtures\n")
        return 1
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_weight(f)
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
