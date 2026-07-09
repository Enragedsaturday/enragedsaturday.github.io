#!/usr/bin/env python3
"""
S7 survey generator — the doctrine-corpus defect measurement machine (S7 spec
§5 step 1: "Regenerate survey + change-list against the post-S3/S5 tree ...
regenerate, don't hand-edit").

The committed `_overhaul2/S7-CHANGELIST.md` is the 2026-07-03 snapshot; the
`s7-survey.json` it cites was never committed. This script rebuilds that survey
machinery from its DEFINITION so the change-list can be regenerated against the
current (post-S3 restructure / post-S5 converter / post-S6 minting) tree.

READ-ONLY over content/. The script mutates NOTHING under content/; its only
side effect is writing the survey JSON to _run/o2-execute/s7-survey.json (its
declared deliverable) — pass --stdout to print instead of writing.

--------------------------------------------------------------------------
PARTITION (the changelist header rule, adapted to the post-S3 tree)
--------------------------------------------------------------------------
Substantive non-case pages only. Excluded:
  * content/cases/**            (S2/S6-owned; slip-op total reported SEPARATELY
                                 because change-list Table 3 TEACH-03 covers it)
  * content/index.md            (root master index — S3 A7(4)-owned)
  * content/about.md, content/flashcards.md
  * category / sub-umbrella index.md files that are NAVIGATIONAL STUBS
    (post-S3 they run 74-239 words; the changelist snapshot saw ~14-18 words).
INCLUDED: every other content page, PLUS the substantive sub-umbrella index.md
LANDING pages that now HOLD a split parent's prose. Post-S3 exactly three such
landings exist (the current homes of change-list Table 1 rows 6 / 8 / 28):
    content/searches/two-definitions-of-search/index.md                       (row 6)
    content/searches/the-third-party-doctrine-and-digital-surveillance/index.md(row 8)
    content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md (row 28)
They are separated from stubs by body word count: the distribution has a clean
gap (largest stub 239 words; smallest substantive landing 2,200 words), so the
INDEX_SUBSTANTIVE_WORDS threshold sits between them. content/index.md (2,771
words) is excluded by NAME regardless, being the generated master index.

--------------------------------------------------------------------------
FLAG DEFINITIONS (each derived from the changelist legend + pinned sites, and
calibrated against the live tree — see the module self-test and the Phase-0
report for the calibration hits)
--------------------------------------------------------------------------
  h1_present     : the first ATX heading in the body is level-1 `# Title`
                   (TEACH-12a; a page whose first heading is deeper is H1-missing)
  rule_skeleton  : an H2 heading whose text is exactly "Rule" (TEACH-12b legacy
                   skeleton). NOT the R1 black-letter `> [!rule]` callout.
  slip_ops       : count of `slip op.` occurrences (TEACH-03). Calibrated EXACT
                   vs the changelist per-page counts (Emergency Aid 8, §1983 9,
                   Exigent 7, ...).
  rd_heading     : an H2 in the "Recent developments" family is present
                   (TEACH-08). The S5 standard is "Lower-court developments";
                   `lcd_heading` records whether that migrated form is present.
  field_framing  : count of the field-framing / "apply it" angle section label
                   (TEACH-04e), keyed on the donor label "Field framing (the
                   'apply it' angle)" (Seizure of the Person). The sanctioned R1
                   `**Apply it.**` list is NOT a hit.
  leak_lines     : lines carrying pipeline-vocabulary (TEACH-02c), four classes:
                   (1) "(No standalone case page..." parenthetical annotation
                       template [calibrated = 23; case-sensitive to match the
                       baseline; lowercase Sources-line variants reported apart]
                   (2) "CL-confirm pending"           [calibrated = 10]
                   (3) LCD/RD meta-intro lines keyed on the "Role-tagged" /
                       "Role-based ... developments" lead (the meta-intro carries
                       it; a bare "(no SCOTUS)" alternate is rejected as prose-
                       ambiguous). Snapshot saw 5 sites; now proliferated.
                   (4) "(woven in)"
                   total = distinct lines matching >=1 class.
  inverted_labels: count of the inverted authority-weight order (TEACH-04d): an
                   em-dash immediately followed by a tier word ("— binding" /
                   "— persuasive"), e.g. "SCOTUS — binding". The canonical S1 A8
                   order ("Binding — SCOTUS") puts the court AFTER the dash and
                   is NOT counted. Calibrated 4/5 flagged pages exact.
  em_dashes      : raw count of U+2014 in the body (TEACH-05 baseline).
  words          : whitespace-token count of the body (post-frontmatter).
  emdash_per_1k  : em_dashes / words * 1000, rounded to 1 dp.

Usage:
  python3 scripts/s7/survey.py            # write _run/o2-execute/s7-survey.json
  python3 scripts/s7/survey.py --stdout   # print JSON to stdout, write nothing
  python3 scripts/s7/survey.py --out PATH # write to a chosen path
  python3 scripts/s7/survey.py --self-test
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
# reuse the canonical lint helpers (frontmatter parse, heading iteration, fenced
# code, file discovery) so measurement matches the lint roster exactly.
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "lint"))
import _common as c  # noqa: E402

OUT_REL = os.path.join("_run", "o2-execute", "s7-survey.json")

# body word count separating a navigational category/sub-umbrella index.md STUB
# (post-S3: <=239 words) from a substantive split-parent LANDING (>=2,200 words).
INDEX_SUBSTANTIVE_WORDS = 400

# named non-substantive pages (excluded regardless of size)
_NAMED_EXCLUDE = {"about.md", "flashcards.md"}

# --------------------------------------------------------------------------
# detectors (pure functions — unit-tested in self_test)
# --------------------------------------------------------------------------

_SLIP_RE = re.compile(r"slip op\.", re.IGNORECASE)
_FIELD_FRAMING_RE = re.compile(r"field framing", re.IGNORECASE)
# inverted authority-weight order: em-dash then a tier word (TEACH-04d).
_INVERTED_LABEL_RE = re.compile(r"—\s*(?:binding|persuasive)\b", re.IGNORECASE)

# class 1 keys on the "(No standalone case page…)" parenthetical annotation
# TEMPLATE (capitalized, paren-led) — reproduces the changelist's 23 pinned
# sites. The lowercase Sources-line variant family ("; no standalone case
# page)") is a separate annotation style, surfaced in the Phase-0 report, not
# folded in here (keeps class1 comparable to the 2026-07-03 baseline).
_LEAK_CLASS1_RE = re.compile(r"\(No standalone case page")
_LEAK_CLASS2_RE = re.compile(r"CL-confirm pending", re.IGNORECASE)
# class 3 keys ONLY on the "Role-tagged"/"Role-based" developments-intro lead
# (every meta-intro leak carries it). A bare "(no SCOTUS ...)" alternate was
# rejected: it false-positives on legitimate doctrinal prose (pole-camera "open
# (no SCOTUS resolution)"; the Brady-list "(No SCOTUS case creates the list)").
_LEAK_CLASS3_RE = re.compile(r"\brole-(?:tagged|based)\b", re.IGNORECASE)
_LEAK_CLASS4_RE = re.compile(r"\(woven in\)", re.IGNORECASE)

EMDASH = "—"


def _fm_body_lines(text):
    fm, body, _start = c.split_frontmatter(text)
    return fm, body, body.split("\n")


def _body_and_lines(text):
    _fm, body, lines = _fm_body_lines(text)
    return body, lines


def word_count(body):
    return len(body.split())


def emdash_count(body):
    return body.count(EMDASH)


def count_slip_ops(body):
    return len(_SLIP_RE.findall(body))


def count_field_framing(body):
    return len(_FIELD_FRAMING_RE.findall(body))


def count_inverted_labels(body):
    return len(_INVERTED_LABEL_RE.findall(body))


def first_heading(body_lines):
    """(level, text) of the first ATX heading in the body, or (None, None)."""
    for _i, level, txt in c.iter_headings(body_lines):
        return level, txt
    return None, None


def h1_present(body_lines):
    level, _txt = first_heading(body_lines)
    return level == 1


def has_rule_skeleton(body_lines):
    """True iff an H2 heading's text is exactly 'Rule' (legacy TEACH-12b
    skeleton) — never the R1 `> [!rule]` callout (a blockquote, not a heading)."""
    for _i, level, txt in c.iter_headings(body_lines):
        if level == 2 and txt.strip().lower() == "rule":
            return True
    return False


def rd_heading_text(body_lines):
    """Text of the first H2 in the 'Recent developments' family, or None."""
    for _i, level, txt in c.iter_headings(body_lines):
        if level == 2 and txt.strip().lower().startswith("recent developments"):
            return txt.strip()
    return None


def has_lcd_heading(body_lines):
    """True iff the S5-standard 'Lower-court developments' H2 is present
    (TEACH-08 already applied)."""
    for _i, level, txt in c.iter_headings(body_lines):
        if level == 2 and txt.strip().lower().startswith("lower-court developments"):
            return True
    return False


def count_leak_lines(body_lines):
    """Per-class line counts + the distinct-line total (TEACH-02c)."""
    c1 = c2 = c3 = c4 = total = 0
    for line in body_lines:
        m1 = bool(_LEAK_CLASS1_RE.search(line))
        m2 = bool(_LEAK_CLASS2_RE.search(line))
        m3 = bool(_LEAK_CLASS3_RE.search(line))
        m4 = bool(_LEAK_CLASS4_RE.search(line))
        c1 += m1
        c2 += m2
        c3 += m3
        c4 += m4
        if m1 or m2 or m3 or m4:
            total += 1
    return {"total": total, "class1_no_standalone": c1,
            "class2_cl_confirm": c2, "class3_meta_intro": c3,
            "class4_woven_in": c4}


def has_rule_callout(body_lines):
    """R1 black-letter `> [!rule]` callout present (authoring signal)."""
    return any(re.match(r"^\s*>\s*\[!rule\]", ln, re.IGNORECASE) for ln in body_lines)


def has_apply_it(body):
    """R1 sanctioned `**Apply it.**` list present (authoring signal)."""
    return bool(re.search(r"\*\*Apply it\.\*\*", body))


# --------------------------------------------------------------------------
# partition
# --------------------------------------------------------------------------

def _rel(path):
    return c.relpath(path).replace(os.sep, "/")


def is_case_page(rel):
    return rel == "content/cases" or rel.startswith("content/cases/")


def classify_partition(path, body):
    """Return 'substantive' | 'index_stub' | 'named' | 'root_index' | 'case'."""
    rel = _rel(path)
    if is_case_page(rel):
        return "case"
    base = os.path.basename(rel)
    if rel == "content/index.md":
        return "root_index"
    if base in _NAMED_EXCLUDE:
        return "named"
    if base == "index.md":
        if word_count(body) >= INDEX_SUBSTANTIVE_WORDS:
            return "substantive"
        return "index_stub"
    return "substantive"


# --------------------------------------------------------------------------
# survey build
# --------------------------------------------------------------------------

def measure_page(path, body, body_lines, status=None):
    em = emdash_count(body)
    wc = word_count(body)
    level, h1txt = first_heading(body_lines)
    rd = rd_heading_text(body_lines)
    return {
        "path": _rel(path),
        "h1_present": level == 1,
        "h1_text": h1txt if level == 1 else None,
        "rule_skeleton": has_rule_skeleton(body_lines),
        "slip_ops": count_slip_ops(body),
        "rd_heading": rd is not None,
        "rd_heading_text": rd,
        "lcd_heading": has_lcd_heading(body_lines),
        "field_framing": count_field_framing(body),
        "leak_lines": count_leak_lines(body_lines),
        "inverted_labels": count_inverted_labels(body),
        "em_dashes": em,
        "words": wc,
        "emdash_per_1k": round(em / wc * 1000, 1) if wc else 0.0,
        "diagnostics": {
            "has_rule_callout": has_rule_callout(body_lines),
            "has_apply_it": has_apply_it(body),
            "status": status,
        },
    }


def build_survey():
    rows = []
    excluded_index_stubs = []
    excluded_named = []
    included_index = []
    case_slip = 0
    case_count = 0
    for path in c.iter_markdown_files(None):
        text = c.read_text(path)
        fm, body, body_lines = _fm_body_lines(text)
        kind = classify_partition(path, body)
        rel = _rel(path)
        if kind == "case":
            case_count += 1
            case_slip += count_slip_ops(body)
            continue
        if kind == "index_stub":
            excluded_index_stubs.append(rel)
            continue
        if kind in ("named", "root_index"):
            excluded_named.append(rel)
            continue
        status = fm.get("status") if isinstance(fm, dict) else None
        row = measure_page(path, body, body_lines, status=status)
        rows.append(row)
        if os.path.basename(rel) == "index.md":
            included_index.append(rel)

    rows.sort(key=lambda r: r["path"])
    excluded_index_stubs.sort()
    excluded_named.sort()
    included_index.sort()

    tot_em = sum(r["em_dashes"] for r in rows)
    tot_wc = sum(r["words"] for r in rows)
    totals = {
        "pages": len(rows),
        "em_dashes": tot_em,
        "words": tot_wc,
        "emdash_per_1k_mean": round(tot_em / tot_wc * 1000, 1) if tot_wc else 0.0,
        "slip_ops": sum(r["slip_ops"] for r in rows),
        "leak_lines": {
            "total": sum(r["leak_lines"]["total"] for r in rows),
            "class1_no_standalone": sum(r["leak_lines"]["class1_no_standalone"] for r in rows),
            "class2_cl_confirm": sum(r["leak_lines"]["class2_cl_confirm"] for r in rows),
            "class3_meta_intro": sum(r["leak_lines"]["class3_meta_intro"] for r in rows),
            "class4_woven_in": sum(r["leak_lines"]["class4_woven_in"] for r in rows),
        },
        "inverted_labels": sum(r["inverted_labels"] for r in rows),
        "field_framing": sum(r["field_framing"] for r in rows),
        "missing_h1_pages": sum(1 for r in rows if not r["h1_present"]),
        "rule_skeleton_pages": sum(1 for r in rows if r["rule_skeleton"]),
        "rd_heading_pages": sum(1 for r in rows if r["rd_heading"]),
        "lcd_heading_pages": sum(1 for r in rows if r["lcd_heading"]),
    }

    return {
        "generated_by": "scripts/s7/survey.py",
        "spec": "S7 §5 step 1 (regenerate survey vs post-S3/S5 tree)",
        "source_changelist": "_overhaul2/S7-CHANGELIST.md (2026-07-03 snapshot)",
        "partition": {
            "index_substantive_words_threshold": INDEX_SUBSTANTIVE_WORDS,
            "substantive_pages": len(rows),
            "included_index_landings": included_index,
            "excluded_index_stubs": excluded_index_stubs,
            "excluded_named": excluded_named,
        },
        "case_pages": {"count": case_count, "slip_ops": case_slip},
        "totals": totals,
        "pages": rows,
    }


def write_survey(survey, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(survey, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")


def require_nonempty_survey(survey):
    """Fail closed: a survey with zero substantive pages means a discovery/path
    regression (the corpus is never legitimately empty). Never let that be written
    as a valid-looking success artifact."""
    if survey["totals"]["pages"] == 0:
        raise RuntimeError(
            "survey discovered 0 substantive pages — discovery/path regression, "
            "refusing to write an empty survey as success")
    return survey


def resolve_out_path(argv, default_path):
    """Resolve the --out override, fail-closed. A bare `--out` (no value) is an
    error, not a silent fall-back to the default; a resolved path must stay under
    REPO_ROOT so a relative `../..` cannot escape the repo."""
    if "--out" not in argv:
        return default_path
    i = argv.index("--out")
    if i + 1 >= len(argv):
        raise ValueError("--out requires a path")
    out_path = argv[i + 1]
    if not os.path.isabs(out_path):
        out_path = os.path.join(REPO_ROOT, out_path)
    resolved = os.path.realpath(out_path)
    root = os.path.realpath(REPO_ROOT)
    if resolved != root and not resolved.startswith(root + os.sep):
        raise ValueError("--out path must stay under the repository root: %r" % out_path)
    return resolved


# --------------------------------------------------------------------------
# self-test (S1 A3 convention) — pure-detector unit checks + fixture scans
# --------------------------------------------------------------------------

def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        p = got == want
        ok = ok and p
        sys.stderr.write("[self-test] %-42s -> %s (got=%r want=%r)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    # slip-op counting (case-insensitive, per-occurrence)
    check("slip-count", count_slip_ops("slip op. at 1; Slip Op. at 2; x"), 2)
    check("slip-none", count_slip_ops("no pincite here"), 0)

    # field-framing keyed on the label, NOT the sanctioned Apply-it list
    check("ff-donor", count_field_framing(
        '**Field framing (the "apply it" angle).** ask in order'), 1)
    check("ff-applyit-not-hit", count_field_framing("**Apply it.** 1. do X"), 0)

    # inverted authority-weight order — canonical order must NOT count
    check("inv-scotus", count_inverted_labels("| x | SCOTUS — binding | y |"), 1)
    check("inv-circuit", count_inverted_labels("9th Cir. — binding"), 1)
    check("inv-persuasive", count_inverted_labels("state — persuasive here"), 1)
    check("inv-canonical-binding", count_inverted_labels("Binding — SCOTUS"), 0)
    check("inv-canonical-persuasive",
          count_inverted_labels("Persuasive — state, illustrative"), 0)
    check("inv-canonical-incircuit",
          count_inverted_labels("Binding in-circuit — 9th Cir."), 0)

    # leak classes
    lk = count_leak_lines([
        "- (No standalone case page — annotate only.)",
        "something CL-confirm pending here",
        "Role-tagged, circuit/state only (no SCOTUS — never a development)",
        "Role-based circuit developments only",
        "**Limits (woven in).** text",
        "ordinary prose line",
    ])
    check("leak-class1", lk["class1_no_standalone"], 1)
    check("leak-class2", lk["class2_cl_confirm"], 1)
    check("leak-class3", lk["class3_meta_intro"], 2)  # Role-tagged + Role-based
    check("leak-class4", lk["class4_woven_in"], 1)
    check("leak-total", lk["total"], 5)

    # heading detectors
    check("h1-present", h1_present(["# Title", "text"]), True)
    check("h1-missing", h1_present(["## Rule", "# Later"]), False)
    check("h1-none", h1_present(["just text"]), False)
    check("rule-skel-yes", has_rule_skeleton(["## Rule", "x"]), True)
    check("rule-skel-plural-no", has_rule_skeleton(["## Rules", "x"]), False)
    check("rule-skel-brief-no", has_rule_skeleton(["## The Brief", "x"]), False)
    check("rd-present", rd_heading_text(["## Recent developments"]),
          "Recent developments")
    check("rd-subtreat", rd_heading_text(
        ["## Recent developments & subsequent treatment"]),
        "Recent developments & subsequent treatment")
    check("rd-absent-when-lcd", rd_heading_text(["## Lower-court developments"]), None)
    check("lcd-present", has_lcd_heading(["## Lower-court developments"]), True)

    # em-dash + words
    check("emdash-count", emdash_count("a — b — c"), 2)
    check("word-count", word_count("a — b — c"), 5)

    # authoring signals
    check("rule-callout", has_rule_callout(["> [!rule] Terry rule", "> text"]), True)
    check("apply-it", has_apply_it("**Apply it.**\n1. do X"), True)

    # fail-closed: empty survey must raise, non-empty passes through
    def _raises(fn):
        try:
            fn()
        except (RuntimeError, ValueError):
            return True
        return False
    check("empty-survey-raises",
          _raises(lambda: require_nonempty_survey({"totals": {"pages": 0}})), True)
    check("nonempty-survey-ok",
          require_nonempty_survey({"totals": {"pages": 3}})["totals"]["pages"], 3)

    # --out resolution: default when absent, fail-closed on bare flag / escape
    _dflt = os.path.join(REPO_ROOT, OUT_REL)
    check("out-default", resolve_out_path([], _dflt), _dflt)
    check("out-relative-under-root",
          resolve_out_path(["--out", "_run/x.json"], _dflt),
          os.path.join(os.path.realpath(REPO_ROOT), "_run", "x.json"))
    check("out-bare-flag-raises",
          _raises(lambda: resolve_out_path(["--out"], _dflt)), True)
    check("out-escape-raises",
          _raises(lambda: resolve_out_path(["--out", "../../etc/passwd"], _dflt)), True)
    check("out-abs-escape-raises",
          _raises(lambda: resolve_out_path(["--out", "/tmp/escape.json"], _dflt)), True)

    # ---- fixture-file integration scans ----
    for base, expect in (("legacy-page.md", {
            "h1_present": False, "rule_skeleton": True, "rd_heading": True,
            "lcd_heading": False, "slip_ops": 2, "field_framing": 1,
            "inverted_labels": 2,
            "leak": {"total": 3, "class1_no_standalone": 1,
                     "class2_cl_confirm": 1, "class3_meta_intro": 1,
                     "class4_woven_in": 0}}),
            ("brief-page.md", {
            "h1_present": True, "rule_skeleton": False, "rd_heading": False,
            "lcd_heading": True, "slip_ops": 0, "field_framing": 0,
            "inverted_labels": 0,
            "leak": {"total": 1, "class1_no_standalone": 0,
                     "class2_cl_confirm": 0, "class3_meta_intro": 0,
                     "class4_woven_in": 1}})):
        fx = os.path.join(HERE, "fixtures", base)
        if not os.path.isfile(fx):
            check("fixture-present:%s" % base, False, True)
            continue
        body, body_lines = _body_and_lines(c.read_text(fx))
        check("%s:h1" % base, h1_present(body_lines), expect["h1_present"])
        check("%s:rule-skel" % base, has_rule_skeleton(body_lines), expect["rule_skeleton"])
        check("%s:rd" % base, rd_heading_text(body_lines) is not None, expect["rd_heading"])
        check("%s:lcd" % base, has_lcd_heading(body_lines), expect["lcd_heading"])
        check("%s:slip" % base, count_slip_ops(body), expect["slip_ops"])
        check("%s:ff" % base, count_field_framing(body), expect["field_framing"])
        check("%s:inv" % base, count_inverted_labels(body), expect["inverted_labels"])
        check("%s:leak" % base, count_leak_lines(body_lines), expect["leak"])

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv):
    if "--self-test" in argv:
        return self_test()
    survey = require_nonempty_survey(build_survey())
    if "--stdout" in argv:
        sys.stdout.write(json.dumps(survey, ensure_ascii=False, indent=2) + "\n")
        return 0
    out_path = resolve_out_path(argv, os.path.join(REPO_ROOT, OUT_REL))
    write_survey(survey, out_path)
    t = survey["totals"]
    sys.stderr.write(
        "[s7-survey] %d substantive pages | em-dash %d / %d words (%.1f/1k) | "
        "slip-op %d | leak-lines %d | inverted %d | field-framing %d | "
        "missing-H1 %d | rule-skel %d | RD %d | LCD %d | case-pages %d (slip-op %d)\n"
        % (t["pages"], t["em_dashes"], t["words"], t["emdash_per_1k_mean"],
           t["slip_ops"], t["leak_lines"]["total"], t["inverted_labels"],
           t["field_framing"], t["missing_h1_pages"], t["rule_skeleton_pages"],
           t["rd_heading_pages"], t["lcd_heading_pages"],
           survey["case_pages"]["count"], survey["case_pages"]["slip_ops"]))
    sys.stderr.write("[s7-survey] wrote %s\n" % c.relpath(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
