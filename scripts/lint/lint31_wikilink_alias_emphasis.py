#!/usr/bin/env python3
"""
LINT-31 — emphasis inside a wikilink alias.   Guard for the MAINT-2 defect
class (found 2026-07-24 on the two Miranda doctrine pages).

Quartz converts [[wikilinks]] to links via mdast findAndReplace, which runs on
TEXT nodes AFTER micromark has parsed emphasis. `[[Target|*Alias*]]` is split
into text("[[Target|") + emphasis("Alias") + text("]]") before the wikilink
regex ever runs, so the link is never built and the reader sees the literal
"[[Target| Alias ]]" (60 live instances shipped this way). The house idiom is
emphasis OUTSIDE the link: `*[[Target|Alias]]*` — always renders.

Flags HIGH: any wikilink whose alias segment contains '*' or '_' emphasis
markers. Exemptions: inline code spans and fenced code blocks (documented
meta-prose like `[[Florida v. White]]` disambiguation notes), HTML comments.

Usage: python3 lint31_wikilink_alias_emphasis.py [glob ...]
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-31"

ALIAS_EMPHASIS_RE = re.compile(r"\[\[[^\]|\n]+\|[^\]\n]*[*_][^\]\n]*\]\]")
FENCE_RE = re.compile(r"^(```|~~~)")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
HTML_COMMENT_RE = re.compile(r"<!--[\s\S]*?-->")


def check_file(path):
    text = c.read_text(path)
    _fm, body, start = c.split_frontmatter(text)
    body = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    out = []
    in_fence = False
    for i, line in enumerate(body.split("\n"), start=start + 1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        scan = CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), line)
        for m in ALIAS_EMPHASIS_RE.finditer(scan):
            out.append(c.make_violation(
                LINT, path, i, c.HIGH,
                "emphasis marker inside wikilink alias — renders as literal "
                "'[[...]]' text (mdast findAndReplace never sees the split "
                "node); move emphasis outside: *[[Target|Alias]]* — got: %s"
                % m.group(0)[:80]))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
