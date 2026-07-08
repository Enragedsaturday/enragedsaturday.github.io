#!/usr/bin/env python3
"""
S7 R15 step-1 mechanical pass — TEACH-08 (S5 R11 / user decision D5).

Rename the "Recent developments"-family H2 to the S5 standard
`## Lower-court developments` and MOVE the whole section (heading + verbatim
content block) to sit directly under `## The Brief`, above the case tables
(i.e. immediately before `## Key cases`).

Content moves VERBATIM — no prose edits, no SCOTUS-bullet relocation, no
meta-intro-line deletion (those are other passes). This pass only:
  (1) renames the exact H2 `## Recent developments` -> `## Lower-court developments`
  (2) permutes whole H2 section blocks so the section lands before Key cases.

Section blocks tile the body exactly (preamble + every H2-delimited block =
the original body), so permuting whole blocks preserves every line and all
inter-section whitespace byte-for-byte; only the one heading line changes.

FAIL-CLOSED guards (a page failing any is SKIPPED, never guessed):
  * exactly one exact-"recent developments" H2 (the "& subsequent treatment"
    variant is NOT matched -> those legacy rule-skeleton pages skip to their
    R3 rewrite),
  * a "the brief" H2 and a "key cases" H2 both present,
  * no pre-existing "lower-court developments" H2 (idempotency).

READ-ONLY unless --apply. Prints a per-page action line to stderr.

Usage:
  python3 scripts/s7/teach08.py                 # dry-run (report only)
  python3 scripts/s7/teach08.py --apply         # write the 33 clean pages
  python3 scripts/s7/teach08.py --apply FILE...  # scope to given files
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "lint"))
import _common as c  # noqa: E402

RD_EXACT = "recent developments"
LCD = "lower-court developments"
BRIEF = "the brief"
KEY = "key cases"

NEW_HEADING = "## Lower-court developments"


def _norm(t):
    return re.sub(r"\s+", " ", t.strip().lower())


def plan_page(text):
    """Return (new_text, action, detail). action in
    {'renamed+moved','skip'}; new_text is None on skip / no-op."""
    fm, body, start = c.split_frontmatter(text)
    lines = text.split("\n")
    front = lines[:start - 1]           # frontmatter incl. both --- delimiters
    body_lines = lines[start - 1:]      # == body.split("\n")

    h2 = [(i, _norm(txt)) for (i, lvl, txt) in c.iter_headings(body_lines)
          if lvl == 2]
    norms = [t for (_i, t) in h2]

    if norms.count(RD_EXACT) != 1:
        # zero exact-RD (e.g. only the "& subsequent treatment" variant) or >1
        variant = [t for t in norms if t.startswith("recent developments")]
        return None, "skip", (
            "no unique exact '## Recent developments' H2 (found RD-family: %r)"
            % variant)
    if LCD in norms:
        return None, "skip", "already has a '## Lower-court developments' H2"
    if BRIEF not in norms:
        return None, "skip", "no '## The Brief' anchor (legacy skeleton -> R3 rewrite)"
    if KEY not in norms:
        return None, "skip", "no '## Key cases' section to place the block above"

    # partition body into preamble + H2-delimited blocks (tiles body exactly)
    first = h2[0][0]
    preamble = body_lines[:first]
    blocks = []  # list of (norm_title, [lines])
    for idx, (i, t) in enumerate(h2):
        end = h2[idx + 1][0] if idx + 1 < len(h2) else len(body_lines)
        blocks.append((t, body_lines[i:end]))

    # locate blocks
    rd_pos = norms.index(RD_EXACT)
    key_pos = norms.index(KEY)

    # rename RD heading line (first line of the RD block), exact match assert
    rd_first = blocks[rd_pos][1][0]
    if rd_first.strip() != "## Recent developments":
        return None, "skip", "RD heading line not exactly '## Recent developments' (%r)" % rd_first
    blocks[rd_pos][1][0] = NEW_HEADING

    # already directly before Key cases? -> rename-only (no reorder needed)
    reordered = (rd_pos != key_pos - 1)

    rd_block = blocks.pop(rd_pos)
    # key_pos shifts left by one if RD was before it
    key_pos_new = norms.index(KEY)
    if rd_pos < key_pos_new:
        key_pos_new -= 1
    # rebuild norms list post-pop for a correct insert index
    new_blocks = blocks[:]
    # find key index in new_blocks
    ins = next(k for k, (t, _l) in enumerate(new_blocks) if t == KEY)
    new_blocks.insert(ins, rd_block)

    new_body_lines = list(preamble)
    for (_t, blk) in new_blocks:
        new_body_lines.extend(blk)

    new_text = "\n".join(front) + "\n" + "\n".join(new_body_lines)

    order_before = [t for (t, _l) in [(norms[j], None) for j in range(len(norms))]]
    order_after = [t for (t, _l) in new_blocks]
    action = "renamed+moved" if reordered else "renamed-only"
    detail = "before=%s  after=%s" % (order_before, order_after)
    if new_text == text:
        return None, "skip", "no-op (already conformant)"
    return new_text, action, detail


def main(argv):
    apply = "--apply" in argv
    files = [a for a in argv if not a.startswith("--")]
    if files:
        paths = [os.path.join(REPO_ROOT, f) if not os.path.isabs(f) else f
                 for f in files]
    else:
        paths = list(c.iter_markdown_files(None))

    changed = 0
    skipped = 0
    for path in paths:
        text = c.read_text(path)
        # cheap pre-filter: only pages carrying an RD-family heading
        if "recent developments" not in text.lower():
            continue
        new_text, action, detail = plan_page(text)
        rel = c.relpath(path)
        if new_text is None:
            skipped += 1
            sys.stderr.write("[teach08] SKIP  %-70s %s\n" % (rel, detail))
            continue
        changed += 1
        sys.stderr.write("[teach08] %-13s %-70s %s\n" % (action.upper(), rel, detail))
        if apply:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
    sys.stderr.write("[teach08] %s: %d changed, %d skipped (RD-family scanned)\n"
                     % ("APPLIED" if apply else "DRY-RUN", changed, skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
