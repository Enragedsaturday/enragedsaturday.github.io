#!/usr/bin/env python3
"""For a file, print each flagged line: raw text + masked em-dash count + positions."""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..','..','..','..','..','..','..'))
# import the lint's masking directly
LINTDIR = "/Users/johngalt/Projects/cssi-quartz/scripts/lint"
sys.path.insert(0, LINTDIR)
import importlib.util
spec = importlib.util.spec_from_file_location("lint10", os.path.join(LINTDIR, "lint10_emdash.py"))
lint10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint10)
import _common as c

def main(path, want_lines):
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body = lint10._mask_html_comments(body)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    # map: for each block, compute masked em positions per line
    for block in lint10._iter_blocks(body_lines, fenced):
        # block is list of (line_index, text); file line = start + line_index
        block_lines = [start + li for (li, _t) in block]
        if not any(fl in want_lines for fl in block_lines):
            continue
        parts = [t for (_li, t) in block]
        block_text = "\n".join(parts)
        masked = lint10._mask_block(block_text)
        emct = masked.count(lint10.EMDASH)
        print("### BLOCK file-lines %s  masked_em=%d" % (block_lines, emct))
        for (li, t) in block:
            fl = start + li
            raw_em = t.count(lint10.EMDASH)
            print("  L%d raw_em=%d | %s" % (fl, raw_em, t))
        print()

if __name__ == "__main__":
    path = sys.argv[1]
    want = set(int(x) for x in sys.argv[2:])
    main(path, want)
