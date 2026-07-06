#!/usr/bin/env python3
"""
LINT-9 — carat-leak (^pin-N).   Guard for S9 R8 #9 (S1 R13).

Obsidian block-reference anchors (^pin-3, ^abc-1, ...) are masked by Quartz
ONLY when the token is the LAST thing on its line. A block-ref token that
appears MID-LINE renders literally to the reader ("... blah ^pin-3 blah").
This lint flags every mid-line block anchor as HIGH.

Scope: content/**/*.md bodies (frontmatter skipped). Exemptions (masked before
scanning): inline code spans, fenced code blocks, HTML comments, wikilink
anchor references [[Page#^pin-3]] (those are LINKS, not leaked anchors), and
footnote syntax [^1] / [^note]: (a '^' immediately preceded by '[').

Legal (never flagged): a block anchor at end-of-line (after rstrip), including a
line whose only token is a block anchor.

NOTE: content remediation of the ~400 existing mid-line pins is S8 R6's job;
this lint is only the STEADY-STATE GUARD (S9 R8 #9). The corpus is expected RED
here until S8 completes — by design.

Usage: python3 lint9_carat_leak.py [glob ...]
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-9"

# A block-ref anchor token: '^' + one alnum + [alnum|hyphen]*.  The negative
# lookbehind excludes footnote syntax [^1] / [^note]: (a '^' right after '[').
BLOCK_ANCHOR_RE = re.compile(r"(?<!\[)\^[A-Za-z0-9][A-Za-z0-9-]*")

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def _blank_keep_nl(m):
    """Blank a match to same-length spaces, preserving any newlines so line
    numbers / column positions are unchanged."""
    return "".join("\n" if ch == "\n" else " " for ch in m.group(0))


def _mask_html_comments(text):
    return HTML_COMMENT_RE.sub(_blank_keep_nl, text)


def _mask_links_and_code(line):
    """Blank inline-code spans and [[wikilinks]] to same-length NON-word filler.

    Unlike _common.mask_links_and_code (which blanks to SPACES), we fill with a
    NON-WORD char ('#') so that (a) a '^' inside a masked wikilink [[Page#^pin-3]]
    is not seen, AND (b) a real anchor that is FOLLOWED by a wikilink/code span is
    correctly treated as mid-line (blanking to spaces + rstrip would wrongly make
    it look end-of-line and hide the leak).

    The filler MUST be outside BLOCK_ANCHOR_RE's char class [A-Za-z0-9-]: an 'x'
    filler is alnum, so `See rule ^pin-3[[Terry v. Ohio]]` masked to
    `See rule ^pin-3xxxxxxxxxxxxxxxxx` let the anchor match run through the fill to
    end-of-line — a false negative that hid a real mid-line leak. '#' stops the
    match at the anchor's true end so the mid-line leak is flagged."""
    def fill(m):
        return "#" * (m.end() - m.start())
    line = c.INLINE_CODE_RE.sub(fill, line)
    line = c.WIKILINK_RE.sub(fill, line)
    return line


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body = _mask_html_comments(body)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        masked = _mask_links_and_code(line).rstrip()
        if not masked:
            continue
        for m in BLOCK_ANCHOR_RE.finditer(masked):
            if m.end() == len(masked):
                # end-of-line anchor (incl. anchor-only line) is LEGAL
                continue
            out.append(c.make_violation(
                LINT, path, start + i, c.HIGH,
                "mid-line block anchor '%s' renders visibly — move it to "
                "end-of-line or delete [S9 R8 #9]" % m.group(0)))
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
    files = sorted(glob.glob(os.path.join(fixdir, "lint-9-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-9-*.md fixtures\n")
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
