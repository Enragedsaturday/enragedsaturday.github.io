#!/usr/bin/env python3
"""
LINT-6 — treatment vocabulary (3-field, dual dates, glyphs).  S1 R2/R3 · A4/A6.

The corpus is MID-MIGRATION: legacy case pages still carry a single-axis
treatment.status + treatment.as_of; the S2 projector re-stamps them with the
3-field schema and a `lake:` frontmatter block. This lint encodes BOTH states.

  (a) NEW-schema page (frontmatter carries a `lake:` block): must carry
      treatment.field_i_validity in
      {good_law, history, caution, questioned, superseded, unverified} AND both
      treatment.as_of_content AND treatment.as_of_treatment non-blank. A legacy
      treatment.status key still present on a projected page = HIGH. Missing
      field_i (or out-of-enum value) or either date = HIGH.

  (b) LEGACY page (no `lake:` block, type: case): missing treatment.status or
      treatment.as_of = HIGH; a status NOT in the legacy enum
      {good, criticized, limited, abrogated, overruled} = HIGH; a well-formed
      legacy page gets ONE LOW informational: "legacy single-axis treatment —
      awaiting S2 projection (S1 A4 mapping)".

  (c) GLYPH (A6): character U+2B58 (HEAVY CIRCLE) anywhere in body OR
      frontmatter of any content file = HIGH — the canonical unverified glyph is
      U+26AA ⚪.

  (d) UNBANNERED-UNVERIFIED (R2): a page whose treatment (either schema)
      contains "unverified" while frontmatter lacks `draft: true` = HIGH
      (unverified must never reach a reader unbannered). Plus: U+26AA ⚪ in a
      body table cell on a non-draft page = MEDIUM (banner presence is judgment).

  (e) Every Case-Index row must carry a non-blank treatment cell (kept as-is):
      a blank cell = MEDIUM.

Usage: python3 lint6_treatment_status.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-6"

TREATMENT_HEADER_RE = re.compile(
    r"\b(treatment|good\s*law|good-law|status)\b", re.IGNORECASE)

# FIELD_I_ENUM — the machine enum for treatment.field_i_validity. These tokens
# follow the S2 record schema (S2 spec R5); they are the ONLY values valid as
# STORED frontmatter. PRACTICES §2's slash-composites (history/neutral,
# questioned/overruling_risk, superseded/not_current) are DISPLAY NAMES of these
# same underlying values — they are for rendering only and are INVALID as stored
# values. A stored 'history/neutral' etc. is out-of-enum here and fails (a).
FIELD_I_ENUM = {"good_law", "history", "caution",
                "questioned", "superseded", "unverified"}
LEGACY_ENUM = {"good", "criticized", "limited", "abrogated", "overruled"}

GLYPH_FORBIDDEN = "⭘"   # ⭘ HEAVY CIRCLE — forbidden (A6)
GLYPH_UNVERIFIED = "⚪"  # ⚪ MEDIUM WHITE CIRCLE — canonical unverified glyph


def _is_case_index(fm, path):
    if fm.get("type") == "index":
        return True
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    title = (fm.get("title") or "").lower() if isinstance(fm.get("title"), str) \
        else ""
    return stem == "case index" or title == "case index"


def _is_draft(fm):
    v = fm.get("draft")
    if isinstance(v, bool):
        return v
    return isinstance(v, str) and v.strip().lower() == "true"


# S5 R15 draft-state banner: a case page renders the top-of-content ⚪ unverified
# banner when its `lake.status` ∈ {draft, under_review} OR the top-level `draft`
# flag is set (the third R15 driver — Field-I `unverified` — IS the condition
# guarded by (d), so a SEPARATE banner-state signal is required there as
# defense-in-depth behind the S2 R12 publish gate). NOTE: the born-draft mint
# (adjudicated E1) emits `lake.status: under_review`, NOT `draft: true` — the
# latter would EXCLUDE the page from the Quartz build (hide it), which is not the
# design; the R15 banner + S2 R12 gate are.
LAKE_BANNER_STATUSES = {"draft", "under_review"}


def _banner_driven(fm):
    """True iff the page carries a banner-driving state per S5 R15 (a `draft: true`
    flag OR a `lake.status` ∈ {draft, under_review})."""
    if _is_draft(fm):
        return True
    lake = fm.get("lake")
    if isinstance(lake, dict):
        return str(lake.get("status", "")).strip().lower() in LAKE_BANNER_STATUSES
    return False


def _blank(v):
    return v is None or (isinstance(v, str) and not v.strip())


def _treatment(fm):
    t = fm.get("treatment")
    return t if isinstance(t, dict) else {}


def _check_new_schema(path, fm, start, out):
    """(a) projected page. Returns the Field-I validity value (for the R2 gate)."""
    t = _treatment(fm)
    field_i = t.get("field_i_validity")

    if "status" in t:                       # legacy single-axis key must be gone
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "legacy single-axis treatment.status still present on a projected "
            "page — must be gone post-projection [R2/A4]"))

    if _blank(field_i):
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "projected page missing treatment.field_i_validity [R2]"))
    elif str(field_i).strip().lower() not in FIELD_I_ENUM:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "treatment.field_i_validity '%s' not in {good_law, history, caution, "
            "questioned, superseded, unverified} [R2]" % field_i))

    if _blank(t.get("as_of_content")):
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "projected page missing treatment.as_of_content date [R3]"))
    if _blank(t.get("as_of_treatment")):
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "projected page missing treatment.as_of_treatment date [R3]"))
    return field_i


def _check_legacy(path, fm, start, out):
    """(b) pre-projection case page. Returns the legacy status value."""
    t = _treatment(fm)
    status = t.get("status")
    as_of = t.get("as_of")
    missing_status = _blank(status)
    missing_as_of = _blank(as_of)

    if missing_status:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "legacy case page missing non-blank treatment.status [R2/N13]"))
    if missing_as_of:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "legacy case page missing treatment.as_of check date [R2/N13]"))

    in_enum = (not missing_status) and \
        str(status).strip().lower() in LEGACY_ENUM
    if (not missing_status) and not in_enum:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "treatment.status '%s' not in the legacy enum {good, criticized, "
            "limited, abrogated, overruled} [A4]" % status))

    if in_enum and not missing_as_of:
        out.append(c.make_violation(
            LINT, path, start, c.LOW,
            "legacy single-axis treatment — awaiting S2 projection "
            "(S1 A4 mapping)"))
    return status


def _check_forbidden_glyph(path, text, out):
    """(c) U+2B58 anywhere in body or frontmatter of any content file."""
    for lineno, line in enumerate(text.split("\n"), start=1):
        if GLYPH_FORBIDDEN in line:
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "forbidden glyph U+2B58 — the canonical unverified glyph is "
                "U+26AA ⚪ [A6]"))


def _looks_like_table_row(line):
    s = line.strip()
    return s.startswith("|") or line.count("|") >= 2


def _check_unverified_glyph_in_tables(path, body, start, out):
    """(d) U+26AA ⚪ in a body table cell on a non-draft page = MEDIUM."""
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if GLYPH_UNVERIFIED in line and _looks_like_table_row(line):
            out.append(c.make_violation(
                LINT, path, start + i, c.MEDIUM,
                "unverified glyph ⚪ in a body table cell on a non-draft "
                "page — confirm the reader-facing banner is present [R2]"))


def _check_case_index(path, body, start, out):
    """(e) Case-Index rows must carry a non-blank treatment cell (unchanged)."""
    body_lines = body.split("\n")
    n = len(body_lines)
    i = 0
    while i < n:
        line = body_lines[i]
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:|\-]+\|?\s*$", body_lines[i + 1]):
            header = [x.strip() for x in line.strip().strip("|").split("|")]
            tidx = None
            for k, h in enumerate(header):
                if TREATMENT_HEADER_RE.search(h):
                    tidx = k
                    break
            j = i + 2
            while j < n and "|" in body_lines[j] and body_lines[j].strip():
                if tidx is not None:
                    cells = [x.strip() for x in
                             body_lines[j].strip().strip("|").split("|")]
                    cell = cells[tidx] if tidx < len(cells) else ""
                    if not cell:
                        out.append(c.make_violation(
                            LINT, path, start + j, c.MEDIUM,
                            "Case-Index row has a blank treatment cell "
                            "[N13/D3]"))
                j += 1
            i = j
        else:
            i += 1


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)

    # (c) forbidden glyph — every content file, body + frontmatter
    _check_forbidden_glyph(path, text, out)

    has_lake = isinstance(fm.get("lake"), dict) and bool(fm.get("lake"))
    banner_driven = _banner_driven(fm)

    validity = None
    if has_lake:
        validity = _check_new_schema(path, fm, start, out)      # (a)
    elif fm.get("type") == "case":
        validity = _check_legacy(path, fm, start, out)          # (b)

    # (d) unverified treatment must not render unbannered. The invariant is "an
    # unverified page carries the R15 banner-driving state," NOT the literal
    # `draft: true` key — a born-draft mint page (lake.status: under_review) IS
    # bannered by R15 and must pass here.
    if validity and "unverified" in str(validity).lower() and not banner_driven:
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "treatment is 'unverified' but the page carries no R15 banner-driving "
            "state (draft: true or lake.status ∈ {draft, under_review}) — "
            "unverified must never reach a reader unbannered [R2/S5 R15]"))
    if not banner_driven:
        _check_unverified_glyph_in_tables(path, body, start, out)

    # (e) Case Index blank-treatment
    if _is_case_index(fm, path):
        _check_case_index(path, body, start, out)
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test — labeled fixtures (filename suffix -pass / -fail). A -pass fixture
# yields zero HIGH; a -fail fixture yields >=1 HIGH. Covers the R15/R2 born-draft
# reconciliation: a minted-shape page (lake.status: under_review + Field-I
# unverified) PASSES; an unverified page with NEITHER banner signal FAILS.
# --------------------------------------------------------------------------

import glob  # noqa: E402


def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-6-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-6-*.md fixtures\n")
        return 1
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_file(f)
        n_high = sum(1 for v in viols if v["severity"] == c.HIGH)
        passed = (n_high == 0) if expect == "pass" else (n_high >= 1)
        ok = ok and passed
        sys.stderr.write("[self-test] %-40s expect=%-4s -> %s (%d high)\n" % (
            name, expect, "OK" if passed else "MISMATCH", n_high))
        if not passed:
            for v in viols:
                sys.stderr.write("             [%s] %s\n" % (v["severity"], v["message"]))
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
