#!/usr/bin/env python3
"""
LINT-18 — depth cap.  S3 · R1/R10 (alias LINT-S3-depth; S9 R8 roster row 18).

The controlled classification nests no deeper than *category → sub-umbrella →
page* (R1: "no node exceeds depth 3"; R10: "the depth lint fails on any 4th
level"). Measured as PATH SEGMENTS below `content/`:

    content/<category>/<page>.md                       depth 2  (page in a category)
    content/<category>/<sub-umbrella>/<page>.md         depth 3  (deepest allowed)
    content/<category>/<sub>/<sub2>/<page>.md           depth 4  -> HIGH (a 4th level)

i.e. FOLDER depth below content/ is capped at 2 (category + sub-umbrella); the
page path therefore has at most 3 segments. A 4th path level is a HIGH finding.

EXEMPT (task / R8 / R13(b)): `content/cases/**` (unlisted per R8, frozen per
R13(b)) and `content/tags/**` (Quartz tag pages) — neither is an explorer-listed
taxonomy node, so their nesting is not S3's to cap.

Not voice; pure path structure. HIGH throughout (the cap is a hard invariant).

SELF-TEST (S1 A3): `python3 lint18_depth.py --self-test` runs over the fixture
trees under `fixtures/lint-18/{ok,fail}/` (a synthetic content-root each) and
verifies the 4th-level page is flagged while shallower pages and cases/ pages
are not.

Usage:
  python3 lint18_depth.py [glob ...]
  python3 lint18_depth.py --self-test
"""

import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-18"

# path-segment count below content/ at which a page becomes a 4th level
MAX_PAGE_SEGMENTS = 3           # category/sub-umbrella/page  (folder depth <= 2)
# top-level segments exempt from the cap (not explorer-listed taxonomy nodes)
EXEMPT_TOP = ("cases", "tags")


def _check_path(path, content_root):
    """Return a HIGH violation if `path` nests below the category/sub-umbrella/
    page cap relative to `content_root`, else None. cases/ and tags/ exempt."""
    rel = os.path.relpath(path, content_root).replace(os.sep, "/")
    segs = rel.split("/")
    if segs and segs[0] in EXEMPT_TOP:
        return None
    if len(segs) > MAX_PAGE_SEGMENTS:
        folder_depth = len(segs) - 1
        return c.make_violation(
            LINT, path, 1, c.HIGH,
            "path nests %d folders below content/ (%s) — the tree caps nesting at "
            "category/sub-umbrella/page (folder depth <= 2, page <= 3 segments); "
            "this is a 4th level [R1/R10]" % (folder_depth, rel))
    return None


def check_tree(content_root, paths=None):
    """Depth-check every markdown page under `content_root` (or the scoped
    `paths`, resolved against `content_root`)."""
    out = []
    if paths:
        files = list(c.iter_markdown_files(paths))
    else:
        files = sorted(glob.glob(os.path.join(content_root, "**", "*.md"),
                                 recursive=True))
    for p in files:
        v = _check_path(p, content_root)
        if v:
            out.append(v)
    return out


def run(paths=None):
    return check_tree(c.CONTENT_ROOT, paths)


# --------------------------------------------------------------------------
# self-test — synthetic content-root fixture trees
# --------------------------------------------------------------------------

def self_test():
    base = os.path.join(c.HERE, "fixtures", "lint-18")
    ok_root = os.path.join(base, "ok")
    fail_root = os.path.join(base, "fail")
    if not os.path.isdir(ok_root) or not os.path.isdir(fail_root):
        sys.stderr.write("[self-test] FAIL: missing fixtures/lint-18/{ok,fail}\n")
        return 1
    ok = True

    ok_viols = check_tree(ok_root)
    passed = len(ok_viols) == 0
    ok = ok and passed
    sys.stderr.write("[self-test] %-28s expect=pass -> %s (%d viol)\n" % (
        "lint-18/ok tree", "OK" if passed else "MISMATCH", len(ok_viols)))
    for v in ok_viols:
        sys.stderr.write("             %s\n" % v["message"])

    fail_viols = check_tree(fail_root)
    # exactly the one 4th-level non-cases page is flagged; the deep cases/ page is not
    passed = len(fail_viols) == 1
    ok = ok and passed
    sys.stderr.write("[self-test] %-28s expect=1-high -> %s (%d viol)\n" % (
        "lint-18/fail tree", "OK" if passed else "MISMATCH", len(fail_viols)))
    for v in fail_viols:
        sys.stderr.write("             %s\n" % v["message"])

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
