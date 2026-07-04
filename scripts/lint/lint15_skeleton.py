#!/usr/bin/env python3
"""
LINT-15 — entry-model skeleton (S5 R1/R3/R10/R11).  'LINT-15 skeleton'.

Two page skeletons, checked structurally (never voice):

(a) DOCTRINE pages (frontmatter `type: doctrine`, not exempt):
      * H2 SEQUENCE per R1 — the canonical order
          The Brief · Lower-court developments · Key cases ·
          Related cases across doctrines · Visual · Sources
        Optional sections may be ABSENT, never REORDERED.
      * The `> [!rule]` black-letter callout is PRESENT and sits in the header
        zone (first block after the H1 / optional italic question line, before
        the first H2).
      * PITFALLS shape (R10): the sanctioned closing block is a
        `**Common pitfalls.**` bold-lead + bullets — no standalone pitfalls H2,
        no alternate bold lead-in.
      * Zero `## Recent developments` headings (R11) — flagged 'rename pending'
        at MEDIUM (S7 applies the rename+move via convert_tables.py; S9 raises
        this to HIGH once S7 completes).

(b) CASE pages (`type: case`): the EXACT BIRAC H2 sequence per R3 —
      Background · Issue · Rule · Application · Conclusion ·
      Treatment & subsequent history · Appears on · Sources

Exempt (R1): category/sub-umbrella OVERVIEWS + craft/reference pages and the
S3-tree index files (`index.md`) — no rule callout / table skeleton required.

Severity is MEDIUM throughout: the pre-overhaul + mid-restructure corpus lights
up structurally (informational, non-gating). S9 wires CI and raises the
gate-worthy rows (R11 rename, BIRAC drift) to HIGH at the roster codification.

SELF-TEST (S1 A3): `python3 lint15_skeleton.py --self-test` runs over the
labeled `fixtures/lint-15-*.md` pages (filename suffix `-pass` / `-fail`) and
verifies each yields the expected outcome.

Usage:
  python3 lint15_skeleton.py [glob ...]
  python3 lint15_skeleton.py --self-test
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-15"

# canonical doctrine H2 ordinals (R1). "recent developments" shares the frontier
# slot so a still-unrenamed page's order is still checked.
DOCTRINE_ORDINAL = {
    "the brief": 0,
    "lower-court developments": 1,
    "recent developments": 1,
    "key cases": 2,
    "related cases across doctrines": 3,
    "visual": 4,
    "sources": 5,
}

# exact BIRAC sequence (R3)
BIRAC = [
    "background",
    "issue",
    "rule",
    "application",
    "conclusion",
    "treatment & subsequent history",
    "appears on",
    "sources",
]

RULE_CALLOUT_RE = re.compile(r"^\s*>\s*\[!rule\]", re.IGNORECASE)
PITFALL_KEYWORDS_RE = re.compile(
    r"pitfall|common error|recurring.*error|field and analytical error", re.IGNORECASE
)
BOLD_LEAD_RE = re.compile(r"^\s*(?:[-*]\s+)?\*\*(?P<bold>.+?)\*\*")
CANON_PITFALL_BOLD = "common pitfalls."

EXEMPT_TYPES = {"overview", "reference", "craft", "category", "fixture", "index"}


def _norm_title(t):
    return re.sub(r"\s+", " ", t.strip().lower())


def is_exempt(path, fm):
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    if stem in ("index", "_index"):
        return True
    if str(fm.get("type", "")).lower() in EXEMPT_TYPES:
        return True
    if fm.get("overview") in (True, "true", "yes"):
        return True
    return False


def _h2_titles(body_lines):
    return [(i, _norm_title(txt))
            for (i, lvl, txt) in c.iter_headings(body_lines) if lvl == 2]


def check_doctrine(path, body, start):
    out = []
    body_lines = body.split("\n")
    h2s = _h2_titles(body_lines)
    first_h2_line = h2s[0][0] if h2s else len(body_lines)

    # --- rule callout: present + in the header zone (before the first H2) ---
    callout_line = None
    fenced = c.fenced_line_numbers(body_lines)
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if RULE_CALLOUT_RE.match(line):
            callout_line = i
            break
    if callout_line is None:
        out.append(c.make_violation(
            LINT, path, start, c.MEDIUM,
            "doctrine skeleton: missing the '> [!rule]' black-letter callout "
            "(R1/R2 — opens every doctrine page)"))
    elif callout_line >= first_h2_line:
        out.append(c.make_violation(
            LINT, path, start + callout_line, c.MEDIUM,
            "doctrine skeleton: '> [!rule]' callout is not in the header zone "
            "(must precede the first H2, after the H1/italic question) [R1]"))

    # --- H2 order (known sections never reordered) ---
    seq = [(i, t, DOCTRINE_ORDINAL[t]) for (i, t) in h2s if t in DOCTRINE_ORDINAL]
    for k in range(1, len(seq)):
        if seq[k][2] < seq[k - 1][2]:
            out.append(c.make_violation(
                LINT, path, start + seq[k][0], c.MEDIUM,
                "doctrine skeleton: '## %s' is out of canonical order (appears "
                "after '## %s') — sections may be absent but never reordered [R1]"
                % (seq[k][1], seq[k - 1][1])))

    # --- Recent developments heading (rename pending — R11) ---
    for (i, t) in h2s:
        if t == "recent developments":
            out.append(c.make_violation(
                LINT, path, start + i, c.MEDIUM,
                "R11 rename pending: '## Recent developments' -> "
                "'## Lower-court developments' + move above the case tables "
                "(convert_tables.py applies; S9 raises to HIGH once S7 completes)"))

    # --- pitfalls shape (R10) ---
    for (i, t) in h2s:
        if PITFALL_KEYWORDS_RE.search(t):
            out.append(c.make_violation(
                LINT, path, start + i, c.MEDIUM,
                "pitfalls shape: standalone pitfalls H2 '## %s' — the sanctioned "
                "form is a '**Common pitfalls.**' bold-lead closing the Brief [R10]"
                % t))
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        m = BOLD_LEAD_RE.match(line)
        if not m:
            continue
        bold = m.group("bold")
        if PITFALL_KEYWORDS_RE.search(bold) and _norm_title(bold) != CANON_PITFALL_BOLD:
            out.append(c.make_violation(
                LINT, path, start + i, c.MEDIUM,
                "pitfalls shape: non-standard lead-in '**%s**' — normalize to "
                "'**Common pitfalls.**' [R10]" % bold.strip()))

    return out


def check_case(path, body, start):
    out = []
    body_lines = body.split("\n")
    titles = [t for (_i, t) in _h2_titles(body_lines)]
    if titles != BIRAC:
        # locate the first point of divergence for a useful line number
        line = start
        h2s = _h2_titles(body_lines)
        for idx, (i, t) in enumerate(h2s):
            if idx >= len(BIRAC) or t != BIRAC[idx]:
                line = start + i
                break
        out.append(c.make_violation(
            LINT, path, line, c.MEDIUM,
            "BIRAC skeleton: case-page H2 sequence %s != the exact R3 order %s"
            % ([t for (_i, t) in h2s], BIRAC)))
    return out


def check_file(path):
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    ptype = str(fm.get("type", "")).lower()
    if ptype == "doctrine":
        if is_exempt(path, fm):
            return []
        return check_doctrine(path, body, start)
    if ptype == "case":
        return check_case(path, body, start)
    return []


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
    files = sorted(glob.glob(os.path.join(fixdir, "lint-15-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-15-*.md fixtures\n")
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
