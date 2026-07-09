#!/usr/bin/env python3
"""
LINT-8 — guardrails + mnemonics (TEACH-11).   Enforces S1 D6/R9 + S9 R8 #8.

Deterministic guardrails:
  (a) The apocryphal Holiday / McCall / Smith training "trio" must never be
      asserted. The REAL United States v. Smith (5th Cir. 2024 geofence case)
      is legitimate and is NOT flagged — only the apocryphal pattern is. The
      tell-tale of the fabricated trio is its other two members (Holiday and
      McCall) appearing as cases; a page that names a "Holiday" case AND a
      "McCall" case is flagged HIGH. (A bare "Smith" is never flagged.)
  (b) Mnemonics carry no citation: a mnemonic line (or a few lines around a
      "mnemonic" cue) that contains a reporter cite or a CourtListener link is
      flagged MEDIUM (a mnemonic is a teaching device, not a holding).
  (c) No inline "## Flashcards" heading on any page (decks live in the deck
      pipeline, never inline) — flagged HIGH.
  (d) TEACH-11 wikilink-target check (S9 R8 #8): a mnemonic/maxim's link target
      must EXIST and MATCH the register entry (S1 R9 / STYLE §5 Appendix B).
      A wikilink whose DISPLAY names a registered device (C.R.E.W., Three Golden
      Rules) but whose TARGET is broken or resolves to a page OTHER than the
      device's canonical register page = HIGH (the S7 04f "CREW mislink" class —
      passes naive text lints, caught by target resolution against the lake/corpus
      index).
  (e) TEACH-11 maxim-wording check (S9 R8 #8): the invertible Golden-Rule maxim
      is "probabilities, not possibilities" (Rule 3); the inverted wording
      "possibilities, not probabilities" = HIGH (the S7 04a "maxim inversion"
      class — passes naive text lints, caught by the register-wording invariant).

Usage: python3 lint8_guardrails.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-8"

FIXTURE = os.path.join(c.HERE, "fixtures")

# apocryphal-trio party markers (case-name patterns), excluding the real Smith
HOLIDAY_CASE_RE = re.compile(
    r"\b(?:v\.\s*Holiday|Holiday\s+v\.)", re.IGNORECASE)
MCCALL_CASE_RE = re.compile(
    r"\b(?:v\.\s*McCall|McCall\s+v\.)", re.IGNORECASE)

MNEMONIC_CUE_RE = re.compile(r"\bmnemonic", re.IGNORECASE)
FLASHCARDS_HEADING_RE = re.compile(r"^#{1,6}\s*flashcards\b", re.IGNORECASE)

# --- TEACH-11 register (S1 R9 Appendix B / STYLE §5): the registered devices
# that carry a canonical PAGE target. A device wikilink must resolve to exactly
# its canonical page (the mislink guard). Devices without a page home
# (N.E.R.D.S., Strive for Five, …) are not target-checked here (no home to hit).
REG_DEVICE_TARGET = {
    "crew": "CREW",
    "three golden rules": "Three Golden Rules",
}
_CREW_DISPLAY_RE = re.compile(r"^\s*c\.?\s?r\.?\s?e\.?\s?w\.?\s*$", re.IGNORECASE)
_GOLDEN_DISPLAY_RE = re.compile(
    r"^\s*(?:the\s+)?three\s+golden\s+rules?\s*$|^\s*golden\s+rules?\s*$",
    re.IGNORECASE)

# the Golden-Rule #3 maxim inverted (canonical: "probabilities, not possibilities")
MAXIM_INVERSION_RE = re.compile(
    r"possibilit(?:y|ies)\s*,?\s+not\s+probabilit", re.IGNORECASE)

_CORPUS_INDEX = None


def _device_of(text):
    if _CREW_DISPLAY_RE.match(text or ""):
        return "crew"
    if _GOLDEN_DISPLAY_RE.match(text or ""):
        return "three golden rules"
    return None


def _corpus_index():
    global _CORPUS_INDEX
    if _CORPUS_INDEX is None:
        _CORPUS_INDEX = c.build_corpus_index()
    return _CORPUS_INDEX


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    # (a) apocryphal trio: Holiday + McCall both present as cases on a page
    holiday_line = None
    mccall_line = None
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if holiday_line is None and HOLIDAY_CASE_RE.search(line):
            holiday_line = start + i
        if mccall_line is None and MCCALL_CASE_RE.search(line):
            mccall_line = start + i
    if holiday_line is not None and mccall_line is not None:
        out.append(c.make_violation(
            LINT, path, min(holiday_line, mccall_line), c.HIGH,
            "apocryphal Holiday/McCall(/Smith) case trio asserted "
            "(Holiday@%d, McCall@%d) — fabricated cases [D6]"
            % (holiday_line, mccall_line)))

    # (b)/(c) per-line checks
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i

        if FLASHCARDS_HEADING_RE.match(line.strip()):
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "inline '## Flashcards' heading — decks are generated, never "
                "inline [D6]"))

        if MNEMONIC_CUE_RE.search(line):
            lo, hi = i, min(len(body_lines), i + 3)
            window = " ".join(body_lines[lo:hi])
            if c.REPORTER_RE.search(window) or c.CL_ANY_URL_RE.search(window):
                out.append(c.make_violation(
                    LINT, path, lineno, c.MEDIUM,
                    "mnemonic appears with a citation/CL link nearby — "
                    "mnemonics carry no citation [D6]"))

        # (d) TEACH-11 wikilink-target check on registered devices
        for m in c.WIKILINK_RE.finditer(line):
            raw = m.group(1)
            parts = raw.split("|", 1)
            target_part = parts[0].split("#")[0].strip()
            anchor = ("#" in parts[0])
            display = parts[1].strip() if len(parts) > 1 else target_part
            device = _device_of(display) or _device_of(target_part)
            if not device:
                continue
            canonical = REG_DEVICE_TARGET[device]
            # a bare in-page anchor link [[#foo]] has no page part to resolve
            if not target_part and anchor:
                continue
            resolved = _corpus_index().resolve(target_part)
            if resolved is None:
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "mnemonic/maxim '%s' wikilinks a target that does not "
                    "resolve (%r) — must exist and match the register page "
                    "'%s' [TEACH-11]" % (display, target_part, canonical)))
            elif c.CorpusIndex.norm(resolved) != c.CorpusIndex.norm(canonical):
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "mnemonic/maxim '%s' wikilinks '%s' but the register page is "
                    "'%s' (mislink — passes naive text lints) [TEACH-11]"
                    % (display, resolved, canonical)))

        # (e) TEACH-11 maxim-wording inversion (Golden Rule #3)
        if MAXIM_INVERSION_RE.search(line):
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "inverted Golden-Rule maxim: the register wording is "
                "'probabilities, not possibilities' (S1 R9) [TEACH-11]"))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


def self_test():
    """TEACH-11 fixtures: the pass fixture is clean; the fail fixture fires HIGH
    on the CREW mislink, the broken-target mnemonic link, and the inverted maxim.
    Returns 0 on pass, 1 on failure."""
    errs = []
    passf = os.path.join(FIXTURE, "lint-8-teach11-pass.md")
    failf = os.path.join(FIXTURE, "lint-8-teach11-fail.md")
    for f in (passf, failf):
        if not os.path.exists(f):
            sys.stderr.write("[self-test] LINT-8: fixture missing: %s\n" % f)
            return 1
    pass_high = [v for v in check_file(passf) if v["severity"] == c.HIGH]
    if pass_high:
        errs.append("pass fixture fired %d HIGH (want 0): %s"
                    % (len(pass_high), [v["message"][:40] for v in pass_high]))
    fail_msgs = [v["message"] for v in check_file(failf)
                 if v["severity"] == c.HIGH and "TEACH-11" in v["message"]]
    have_mislink = any("mislink" in m for m in fail_msgs)
    have_broken = any("does not resolve" in m for m in fail_msgs)
    have_invert = any("inverted Golden-Rule" in m for m in fail_msgs)
    if not have_mislink:
        errs.append("fail fixture: expected a CREW mislink HIGH, got none")
    if not have_broken:
        errs.append("fail fixture: expected a broken-target HIGH, got none")
    if not have_invert:
        errs.append("fail fixture: expected an inverted-maxim HIGH, got none")
    if errs:
        for e in errs:
            sys.stderr.write("[self-test] LINT-8: %s\n" % e)
        return 1
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    c.cli_main(run, LINT)
