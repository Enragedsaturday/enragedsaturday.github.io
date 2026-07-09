#!/usr/bin/env python3
"""
LINT-27 — table pipe-escaping (S8 R11, NUM-02).

Every wikilink inside a GFM table row must escape its display pipe as `\\|`.
Quartz self-heals an unescaped `|` at build (the live site renders today's
files), so this is SOURCE HYGIENE: an unescaped `[[Target|display]]` in a table
cell breaks in every other markdown surface, and S8's own pass injects piped
links into table cells at scale.

  CHECK — a `[[ ... | ... ]]` wikilink that sits on a GFM table row (header or
  body) and whose display pipe is a BARE `|` (not `\\|`) = HIGH. Wikilinks with an
  escaped display pipe (`[[Target\\|display]]`) pass; wikilinks with no display
  pipe pass; a display pipe on a wikilink OUTSIDE a table row is not this lint's
  concern (prose renders it fine).

The work list is re-derived at EXECUTE (spec R11 seed-not-gospel). Zones/tables via
`_common` (the shared GFM helpers). READ-ONLY.

Usage: python3 lint27_table_pipes.py [glob ...]   ( --self-test for the gate )
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-27"

_WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")


def _bare_pipe_in_wikilink(inner):
    """True iff the wikilink inner content carries an UNESCAPED display pipe."""
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "|":
            return True
        i += 1
    return False


def check_file(path):
    out = []
    text = c.read_text(path)
    _fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")

    table_line_idxs = set()
    for header_i, _cells, rows in c.iter_tables(body_lines):
        table_line_idxs.add(header_i)
        table_line_idxs.update(rows)

    for i in sorted(table_line_idxs):
        line = body_lines[i]
        for m in _WIKILINK_RE.finditer(line):
            if _bare_pipe_in_wikilink(m.group(1)):
                out.append(c.make_violation(
                    LINT, path, start + i, c.HIGH,
                    "unescaped display pipe in a table-row wikilink: [[%s]] — use "
                    "`\\|` in table cells [S8 R11/NUM-02]" % m.group(1)[:80]))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

FIXTURE = os.path.join(c.HERE, "fixtures")


def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        p = (got == want)
        ok = ok and p
        sys.stderr.write("[self-test] %-40s -> %s (got=%s want=%s)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    # unit: bare-pipe detector
    check("bare-pipe-detected", _bare_pipe_in_wikilink("Target|display"), True)
    check("escaped-pipe-ok", _bare_pipe_in_wikilink("Target\\|display"), False)
    check("no-pipe-ok", _bare_pipe_in_wikilink("Target#^pin-1"), False)

    vf = check_file(os.path.join(FIXTURE, "lint-27-fail.md"))
    check("fail-fixture-HIGH", sum(1 for v in vf if v["severity"] == c.HIGH), 2)
    vp = check_file(os.path.join(FIXTURE, "lint-27-pass.md"))
    check("pass-fixture-clean", vp, [])

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
