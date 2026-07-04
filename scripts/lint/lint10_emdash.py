#!/usr/bin/env python3
"""
LINT-10 — em-dash budget.   Enforces S1 R8 + Amendments A7/A8 (S9 R8 row 10).

Targets EM-DASHES (U+2014) ONLY. En-dashes (U+2013) in citation/page/date
ranges are a STYLE rule, never a lint target (A7); they are ignored here.

Budget (fail-closed, per A8):
  * >1 em-dash in a BLOCK (a paragraph or a single list item)  -> HIGH
  * >=2 em-dashes in a single SENTENCE                          -> HIGH
    (both can fire on the same block; distinct messages)
  Exactly 1 em-dash per block is within budget (OK).

Exemptions (masked BEFORE counting):
  (a) em-dashes inside DIRECT QUOTATIONS — spans inside straight ("...") or
      curly (“...”) double quotes, and any blockquote line ('>' ...);
  (b) CONTROLLED LABELS — the exact authority-weight label strings (A8),
      including the prefix forms that cover the mandatory circuit suffix;
  (c) frontmatter, fenced code, inline code, HTML comments.
  (d) BLACK-LETTER RULE CALLOUTS — any Obsidian callout of type [!rule] (a line
      beginning '> [!rule]' plus that callout's '> ' continuation lines) is
      EXEMPT from the em-dash budget: black-letter rule text is a NEVER-APPLY
      carve-out (S1 Appendix A / STYLE §3). Generic blockquotes are already
      exempt via (a)'s blockquote boundary in _iter_blocks, so '> [!rule]'
      callouts were ALREADY effectively exempt — this carve-out is made
      EXPLICIT (see RULE_CALLOUT_RE + the rule-callout tracking in _iter_blocks)
      so a future refactor of the blockquote handling cannot silently
      un-exempt black-letter rules.

Scope: rendered prose in content/**/*.md.

SELF-TEST (S1 A3): `python3 lint10_emdash.py --self-test` runs the lint over
`scripts/lint/fixtures/lint-10.md` (labeled known-pass/known-fail blocks) and
verifies each block's outcome; exit 0 on full match, else 1.

Usage:
  python3 lint10_emdash.py [glob ...]
  python3 lint10_emdash.py --self-test
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-10"

EMDASH = "—"  # — (U+2014)  — the ONLY character this lint counts

# Controlled authority-weight labels (A8 allowlist). The two ' — '-suffixed
# prefixes cover the circuit-suffixed forms (e.g. "Binding in-circuit — 9th
# Cir.") — masking the prefix removes their em-dash; the suffix carries none.
CONTROLLED_LABELS = [
    "Persuasive (outside circuit) — ",
    "Persuasive only — non-precedential",
    "Persuasive — state, illustrative",
    "Binding in-circuit — ",
    "Binding — SCOTUS",
]

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
STRAIGHT_DQUOTE_RE = re.compile(r'"[^"]*"')
CURLY_DQUOTE_RE = re.compile("“[^”]*”")   # “ ... ”
LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
BLOCKQUOTE_RE = re.compile(r"^\s*>")
# Obsidian [!rule] callout HEADER line (e.g. '> [!rule] Terry rule'). Its '> '
# continuation lines carry black-letter rule text — a NEVER-APPLY carve-out
# (S1 Appendix A / STYLE §3), EXEMPT from the em-dash budget. See _iter_blocks.
RULE_CALLOUT_RE = re.compile(r"^\s*>\s*\[!rule\]", re.IGNORECASE)
SENTENCE_END_RE = re.compile(r"[.!?]+(?=\s|$)")
EXPECT_RE = re.compile(r"<!--\s*expect:\s*([A-Za-z-]+)\s*-->")


def _blank_keep_nl(m):
    """Blank a match to same-length spaces, preserving newlines (keeps the
    char->line offset map intact)."""
    return "".join("\n" if ch == "\n" else " " for ch in m.group(0))


def _mask_html_comments(text):
    return HTML_COMMENT_RE.sub(_blank_keep_nl, text)


def _mask_block(text):
    """Blank the em-dash exemptions in a block's text (newline-preserving):
    inline code, controlled labels, then direct-quotation spans."""
    text = c.INLINE_CODE_RE.sub(_blank_keep_nl, text)
    for label in CONTROLLED_LABELS:
        if label in text:
            text = text.replace(label, " " * len(label))
    text = STRAIGHT_DQUOTE_RE.sub(_blank_keep_nl, text)
    text = CURLY_DQUOTE_RE.sub(_blank_keep_nl, text)
    return text


def _iter_blocks(body_lines, fenced):
    """Yield blocks as lists of (line_index, text).

    A block is a paragraph (contiguous non-blank prose lines) OR a single list
    item. Blank lines, fenced-code lines, and blockquote ('>') lines are
    boundaries and are themselves excluded (blockquotes = direct quotation).

    [!rule] callouts (black-letter rule text) are EXEMPT per S1 Appendix A /
    STYLE §3. Generic blockquote lines are already boundaries above, so a
    '> [!rule]' callout and its '> ' continuation lines are already effectively
    exempt; the `rule_exempt` clause below makes that carve-out EXPLICIT and
    self-standing — it marks rule-callout lines as boundaries on their own, so a
    future refactor that drops the general blockquote boundary cannot silently
    un-exempt black-letter rules."""
    block = []
    in_rule_callout = False
    for i, line in enumerate(body_lines):
        is_blockquote = bool(BLOCKQUOTE_RE.match(line))
        # Track whether we are inside an Obsidian [!rule] callout: it opens on a
        # '> [!rule]' header and continues through consecutive '> ' lines; any
        # non-blockquote line (incl. a blank line) closes it.
        if RULE_CALLOUT_RE.match(line):
            in_rule_callout = True
        elif not is_blockquote:
            in_rule_callout = False
        rule_exempt = in_rule_callout and is_blockquote
        boundary = (i in fenced) or (line.strip() == "") \
            or is_blockquote or rule_exempt
        if boundary:
            if block:
                yield block
                block = []
            continue
        if LIST_MARKER_RE.match(line):
            if block:
                yield block
            block = [(i, line)]
            continue
        block.append((i, line))
    if block:
        yield block


def _sentence_spans(text):
    spans = []
    start = 0
    for m in SENTENCE_END_RE.finditer(text):
        spans.append((start, m.end()))
        start = m.end()
    if start < len(text):
        spans.append((start, len(text)))
    return spans


def _check_block(path, start, block, out):
    # build block_text + a char-offset -> body-line-index map
    parts = []
    offsets = []  # (start_offset, line_index), ascending
    off = 0
    for (li, text) in block:
        offsets.append((off, li))
        parts.append(text)
        off += len(text) + 1  # +1 for the '\n' joiner
    block_text = "\n".join(parts)
    masked = _mask_block(block_text)

    def line_of(pos):
        li = offsets[0][1]
        for (start_off, lineno) in offsets:
            if start_off <= pos:
                li = lineno
            else:
                break
        return li

    em_positions = [m.start() for m in re.finditer(EMDASH, masked)]

    # block-level budget: >1 em-dash per block
    if len(em_positions) > 1:
        out.append(c.make_violation(
            LINT, path, start + line_of(em_positions[1]), c.HIGH,
            "em-dash budget: block has %d em-dashes (max 1 per paragraph / "
            "list item) [R8/A8]" % len(em_positions)))

    # sentence-level budget: >=2 em-dashes in a single sentence
    for (s0, s1) in _sentence_spans(masked):
        local = [p for p in em_positions if s0 <= p < s1]
        if len(local) >= 2:
            out.append(c.make_violation(
                LINT, path, start + line_of(local[1]), c.HIGH,
                "em-dash budget: sentence has %d em-dashes (>=2 forbidden) "
                "[R8/A8]" % len(local)))


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body = _mask_html_comments(body)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    for block in _iter_blocks(body_lines, fenced):
        _check_block(path, start, block, out)
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test (S1 A3): exercise the labeled fixture
# --------------------------------------------------------------------------

FIXTURE = os.path.join(c.HERE, "fixtures", "lint-10.md")


def _parse_expectations(body_lines, start):
    """From the RAW fixture body, pair each `<!-- expect: X -->` comment with
    the block that follows it. Return (expected, lo, hi) triples in ORIGINAL
    file line numbers (inclusive)."""
    exps = []
    i, n = 0, len(body_lines)
    while i < n:
        m = EXPECT_RE.search(body_lines[i])
        if not m:
            i += 1
            continue
        expected = m.group(1)
        j = i + 1
        while j < n and body_lines[j].strip() == "":
            j += 1
        lo = start + j
        while j < n and body_lines[j].strip() != "" \
                and not EXPECT_RE.search(body_lines[j]):
            j += 1
        hi = start + j - 1
        exps.append((expected, lo, hi))
        i = j
    return exps


def self_test():
    if not os.path.isfile(FIXTURE):
        sys.stderr.write("[self-test] FAIL: fixture missing at %s\n" % FIXTURE)
        return 1
    text = c.read_text(FIXTURE)
    _fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    exps = _parse_expectations(body_lines, start)
    if not exps:
        sys.stderr.write("[self-test] FAIL: no expectations found in fixture\n")
        return 1
    viols = check_file(FIXTURE)
    ok = True
    for (expected, lo, hi) in exps:
        here = [v for v in viols if lo <= v["line"] <= hi]
        has_block = any("block has" in v["message"] for v in here)
        has_sentence = any("sentence has" in v["message"] for v in here)
        if expected == "pass":
            passed = (len(here) == 0)
        elif expected == "fail-block":
            passed = has_block
        elif expected == "fail-sentence":
            passed = has_sentence
        elif expected == "fail":
            passed = (len(here) > 0)
        else:
            passed = False
        ok = ok and passed
        sys.stderr.write(
            "[self-test] lines %d-%d expect=%-13s -> %s (%d viol)\n" % (
                lo, hi, expected, "OK" if passed else "MISMATCH", len(here)))
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
