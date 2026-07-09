#!/usr/bin/env python3
"""
LINT-3 — doctrine-page structure + N5 (extended).   Enforces S1 N5/N8/D10 + A2 + A9.

REBUILT lake-driven at S9 R8 (roster row 3) per the F-DEMO-001 adjudication
(_overhaul2/s9-demo/): the O1 45-char token-window N5 heuristic is DEAD — the live
panel killed the window patch (broke true positives two ways: over- AND
under-detection, COH-28). The N5 check is now SECTION-SCOPED and LAKE-DRIVEN
(court read from the S2 lake), keyed on the two structural homing signals S1 A2
concretized: a `Binding — SCOTUS` label and a SCOTUS case placed as a development
ENTRY (own-court SCOTUS cite/designation on the entry's lead), inside a frontier
section. Acceptance fixture: scripts/lint/fixtures/lint-3-n5.md (committed;
self_test asserts TP-1..4 fire HIGH, FP-1/FP-2 stay clean).

On every doctrine page (frontmatter type: doctrine) checks:
  (a) Section-order presence — brief-first ordering (S1 §3.I). LOW (informational).
  (c) A single controlling amendment in frontmatter (D10) — LOW.
  (b) N5 (rebuilt, lake-driven): inside a frontier section (`Recent developments`
      or its S5 R11 successor `Lower-court developments`, TEACH-08), fire HIGH on
      any line that:
        (i)  carries a `Binding — SCOTUS` label (the decisive homing signal), OR
        (ii) is a development ENTRY (bulleted/ordered list item) whose LEAD case is
             homed as SCOTUS — its own-court zone carries a U.S./S.Ct. reporter
             cite, an explicit `(SCOTUS …)` court designation, or a wikilink whose
             lake `court_level` is scotus — and is NOT suppressed by a lower-court
             parenthetical `(… Cir. …)` or a lake-confirmed lower court on the lead.
      A bare descriptive `SCOTUS` token on a circuit-subject line ("→ superseded by
      SCOTUS", "no SCOTUS") does NOT fire; a SCOTUS framework case merely MENTIONED
      in synthesis/disclaimer prose does NOT fire (the over-detection the O1 window
      lint could not avoid — killed here structurally).
  (d) A9 >3-cases-per-paragraph (fail-closed HIGH, S9 roster): a prose paragraph in
      the Explanation layer ("the Brief" — doctrine prose before the Key cases
      apparatus) that invokes MORE THAN 3 distinct cases converts to labeled
      bullets (S1 A9 / TEACH-07). Case density is countable via wikilink/CASE
      mentions, so the >3-case hard flag is fail-closed; the ~5-sentence /
      one-move soft caps stay advisory (not linted here).

Usage: python3 lint3_structure.py [glob ...]
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-3"

FIXTURE = os.path.join(c.HERE, "fixtures", "lint-3-n5.md")
LAKE_CASES_DIR = os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases")

# tolerant matching of the canonical section roles (substring on the slug)
BRIEF_HINTS = ("rule", "the-brief", "brief", "overview", "black-letter")
KEYCASES_HINTS = ("key-cases", "key-case")
# the frontier section: legacy `Recent developments` + its S7/S5-R11 successor
# `Lower-court developments` (TEACH-08). Both scoped; a surviving legacy heading
# is itself a LINT-15 rename violation, but N5 must still cover it.
FRONTIER_HINTS = ("recent-development", "recent-dev",
                  "lower-court-development", "lower-court-dev")
APPARATUS_HINTS = KEYCASES_HINTS + FRONTIER_HINTS + ("sources", "source")
SOURCES_HINTS = ("sources", "source")

AMENDMENT_TOKEN_RE = re.compile(
    r"\bamend(?:ment)?s?\.?\s*"
    r"((?:[IVXLC]+|\d+)(?:\s*[&/,]\s*(?:[IVXLC]+|\d+))*)", re.IGNORECASE)
ORDINAL_AMEND_RE = re.compile(
    r"\b(First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|"
    r"Eleventh|Twelfth|Thirteenth|Fourteenth)\s+Amendment", re.IGNORECASE)

# (i) the decisive homing label: "Binding — SCOTUS" (em/en-dash/hyphen)
BINDING_SCOTUS_RE = re.compile(r"Binding\s*[—–\-]\s*SCOTUS", re.IGNORECASE)

# (ii) an explicit SCOTUS COURT designation parenthetical — "(SCOTUS 2021)" — but
# NOT a negation disclaimer "(no SCOTUS)" / "(**no SCOTUS**; …)".
SCOTUS_DESIGNATION_RE = re.compile(
    r"\((?![^()]*\bno\b)[^()]*\bSCOTUS\b[^()]*\)", re.IGNORECASE)

# a LOWER-court parenthetical (own court = circuit): "(9th Cir. 2016)",
# "(D.C. Cir.)", "(Fed. Cir. 2020) (en banc)" — never a SCOTUS/Supreme paren.
_CIRCUIT_ORD = (r"\d{1,2}(?:st|nd|rd|th)|D\.?\s?C\.?|Fed\.|First|Second|Third|"
                r"Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|Eleventh")
LOWER_COURT_PAREN_RE = re.compile(
    r"\((?![^()]*(?:SCOTUS|Supreme))[^()]*\b(?:%s)\s+Cir\.[^()]*\)"
    % _CIRCUIT_ORD, re.IGNORECASE)

BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")

# a wikilink target that looks like a case ("X v. Y")
_CASE_TARGET_RE = re.compile(r"\sv\.?\s")


# --------------------------------------------------------------------------
# lake court index (court read from the S2 lake — the R8 #3 "court from the
# lake" requirement). Keyed by normalized filename stem AND identity.case_name /
# case_name_short. Value: court_level ("scotus"|"coa"|"district"|"state"|"other").
# --------------------------------------------------------------------------

_LAKE_COURT = None


def _norm_case(name):
    n = (name or "").strip().lower()
    n = re.sub(r"[*_`]", "", n)
    n = re.sub(r"\s+", " ", n)
    return n


def _load_lake_courts(lake_dir=LAKE_CASES_DIR):
    global _LAKE_COURT
    if _LAKE_COURT is not None:
        return _LAKE_COURT
    idx = {}
    for f in sorted(glob.glob(os.path.join(lake_dir, "*.json"))):
        try:
            with open(f, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        idy = d.get("identity") or {}
        lvl = idy.get("court_level")
        if not lvl and (idy.get("court_id") == "scotus"):
            lvl = "scotus"
        if not lvl:
            continue
        keys = [os.path.splitext(os.path.basename(f))[0],
                idy.get("case_name"), idy.get("case_name_short")]
        for k in keys:
            nk = _norm_case(k)
            if nk:
                idx.setdefault(nk, lvl)
    _LAKE_COURT = idx
    return idx


def _lead_court_level(target):
    """Lake court_level for a wikilink target (stripped of #anchor/|display), or
    None if the case is not in the lake."""
    tgt = target.split("|")[0].split("#")[0].strip()
    return _load_lake_courts().get(_norm_case(tgt))


def _amendments_in(text):
    found = set()
    for m in AMENDMENT_TOKEN_RE.finditer(text or ""):
        for tok in re.split(r"[&/,]", m.group(1)):
            tok = tok.strip()
            if tok:
                found.add(tok.upper())
    for m in ORDINAL_AMEND_RE.finditer(text or ""):
        found.add(m.group(1).capitalize())
    return found


def _has_any(slug, hints):
    return any(h in slug for h in hints)


# --------------------------------------------------------------------------
# case-reference scanning
# --------------------------------------------------------------------------

def _case_spans(line):
    """Return sorted [(start, end, target, is_wikilink)] of case references on a
    line: wikilink targets that look like a case, plus bare "X v. Y" CASE_RE
    matches not already inside a wikilink."""
    spans = []
    masked = list(line)
    for m in c.WIKILINK_RE.finditer(line):
        tgt = m.group(1).split("|")[0].split("#")[0].strip()
        if _CASE_TARGET_RE.search(tgt) or _lead_court_level(tgt) is not None:
            spans.append((m.start(), m.end(), tgt, True))
        # blank the wikilink so CASE_RE below does not double-match its text
        for i in range(m.start(), m.end()):
            masked[i] = " "
    for m in c.CASE_RE.finditer("".join(masked)):
        spans.append((m.start(), m.end(), m.group(0), False))
    spans.sort(key=lambda s: s[0])
    return spans


def _n5_line_fires(line):
    """Return (fires: bool, reason: str) for one frontier-section line."""
    # (i) the decisive homing label — fires anywhere (prose or entry)
    if BINDING_SCOTUS_RE.search(line):
        return True, "Binding — SCOTUS label"

    # (ii) SCOTUS case homed as a development ENTRY (list item only — synthesis/
    # disclaimer prose that merely MENTIONS a SCOTUS framework case is exempt)
    if not BULLET_RE.match(line):
        return False, ""
    spans = _case_spans(line)
    if not spans:
        return False, ""
    lead_start, lead_end, lead_tgt, lead_wl = spans[0]
    # lead window = from the lead case to the next distinct case (or EOL)
    nxt = None
    for s in spans[1:]:
        if s[0] > lead_end:
            nxt = s[0]
            break
    window = line[lead_start: nxt if nxt is not None else len(line)]

    # suppress: own court is a lower court (circuit paren, or lake-confirmed)
    if LOWER_COURT_PAREN_RE.search(window):
        return False, ""
    lead_lvl = _lead_court_level(lead_tgt) if lead_wl else None
    if lead_lvl in ("coa", "district", "state", "other"):
        return False, ""

    # fire signals on the lead's own-court zone. NOTE: a bare SCOTUS-court
    # wikilink is NOT a fire trigger — the corpus mentions SCOTUS framework cases
    # by wikilink pervasively and legitimately inside frontier synthesis prose and
    # circuit-development bullets (the over-detection the O1 window lint could not
    # avoid). The homing signal must be the entry's OWN-COURT SCOTUS cite or an
    # explicit (SCOTUS) designation. The lake court is used only to SUPPRESS (a
    # lower-court lead) and to confirm SCOTUS in the report layer.
    if c.US_REPORTER_RE.search(window) or c.SCT_REPORTER_RE.search(window):
        return True, "SCOTUS case homed as a development entry (own U.S./S.Ct. cite)"
    if SCOTUS_DESIGNATION_RE.search(window):
        return True, "SCOTUS case homed as a development entry ((SCOTUS) designation)"
    return False, ""


# --------------------------------------------------------------------------
# A9 — >3-cases-per-paragraph (the Brief / Explanation layer), fail-closed HIGH
# --------------------------------------------------------------------------

def _distinct_cases_in(lines):
    """Distinct case identities across a run of prose lines (union of case
    wikilinks + bare CASE_RE), normalized + deduped. Lines are JOINED before
    scanning so a soft-wrapped wikilink split across two lines is still one
    case."""
    joined = " ".join(ln.strip() for ln in lines)
    seen = set()
    for (_s, _e, tgt, _wl) in _case_spans(joined):
        seen.add(_norm_case(tgt))
    return seen


def _brief_paragraph_violations(path, body_lines, start, secs):
    """A9: prose paragraphs in the Explanation layer (sections before the case
    apparatus) with >3 distinct case invocations."""
    out = []
    fenced = c.fenced_line_numbers(body_lines)
    # explanation layer = sections before the first apparatus section
    brief_ranges = []
    hit_apparatus = False
    for s in secs:
        if _has_any(s["slug"], APPARATUS_HINTS):
            hit_apparatus = True
            break
        brief_ranges.append((s["start"], s["end"]))
    # pages with no apparatus heading: only take pre-apparatus sections found
    if not hit_apparatus and not brief_ranges and secs:
        brief_ranges = [(secs[0]["start"], secs[0]["end"])]

    for (lo, hi) in brief_ranges:
        para = []
        para_start = None
        for i in range(lo + 1, hi):
            if i in fenced:
                continue
            raw = body_lines[i]
            stripped = raw.strip()
            is_break = (not stripped
                        or c.HEADING_RE.match(raw)
                        or BULLET_RE.match(raw)
                        or stripped.startswith(">")
                        or stripped.startswith("|")
                        or stripped.startswith("<!--"))
            if is_break:
                if para:
                    _flush_para(out, path, start, para_start, para)
                para = []
                para_start = None
                continue
            if para_start is None:
                para_start = i
            para.append(raw)
        if para:
            _flush_para(out, path, start, para_start, para)
    return out


def _flush_para(out, path, start, para_start, para):
    cases = _distinct_cases_in(para)
    if len(cases) > 3:
        out.append(c.make_violation(
            LINT, path, start + para_start, c.HIGH,
            "Explanation-layer paragraph invokes %d distinct cases (>3) — convert "
            "the case wall to labeled bullets [S1 A9/TEACH-07]: %s"
            % (len(cases), ", ".join(sorted(cases))[:160])))


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    if fm.get("type") != "doctrine":
        return out
    body_lines = body.split("\n")
    secs = c.sections(body_lines)

    # (a) section-order presence
    slugs = [s["slug"] for s in secs]
    if secs:
        first = slugs[0]
        if not _has_any(first, BRIEF_HINTS):
            if _has_any(first, KEYCASES_HINTS) or _has_any(first, FRONTIER_HINTS):
                out.append(c.make_violation(
                    LINT, path, start + secs[0]["start"], c.LOW,
                    "brief-first violated: first section is '%s' (the teaching "
                    "brief should lead) [N8]" % secs[0]["title"]))
    for label, hints in (("Key cases", KEYCASES_HINTS),
                         ("Sources", SOURCES_HINTS)):
        if not any(_has_any(s, hints) for s in slugs):
            out.append(c.make_violation(
                LINT, path, start, c.LOW,
                "missing expected '%s' section [N8/D10]" % label))

    # (b) N5 — lake-driven, section-scoped
    fenced = c.fenced_line_numbers(body_lines)
    for s in secs:
        if not _has_any(s["slug"], FRONTIER_HINTS):
            continue
        for i in range(s["start"] + 1, s["end"]):
            if i in fenced:
                continue
            fires, reason = _n5_line_fires(body_lines[i])
            if fires:
                out.append(c.make_violation(
                    LINT, path, start + i, c.HIGH,
                    "%s in '%s' — SCOTUS holdings belong in Key cases [N5]"
                    % (reason, s["title"])))

    # (d) A9 — >3-cases-per-paragraph in the Brief
    out.extend(_brief_paragraph_violations(path, body_lines, start, secs))

    # (c) single controlling amendment in frontmatter
    fm_amend_field = (fm.get("amendment") or fm.get("controlling_amendment")
                      or fm.get("jurisdiction") or "")
    amendments = _amendments_in(fm_amend_field if isinstance(fm_amend_field, str)
                                else str(fm_amend_field))
    if not amendments:
        out.append(c.make_violation(
            LINT, path, start, c.LOW,
            "no controlling amendment found in frontmatter [D10]"))
    elif len(amendments) > 1 and not (fm.get("amendment")
                                      or fm.get("controlling_amendment")):
        out.append(c.make_violation(
            LINT, path, start, c.LOW,
            "multiple amendments named in frontmatter %s; declare a single "
            "controlling amendment [D10]" % sorted(amendments)))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


# --------------------------------------------------------------------------
# self-test — the committed acceptance fixture (F-DEMO-001 adjudicated semantics)
# --------------------------------------------------------------------------

def self_test():
    """Assert the rewritten N5 check on the committed fixture: TP-1..TP-4 fire
    HIGH, FP-1/FP-2 stay clean. Returns 0 on pass, 1 on failure."""
    errs = []
    if not os.path.exists(FIXTURE):
        sys.stderr.write("[self-test] LINT-3: fixture missing: %s\n" % FIXTURE)
        return 1
    text = c.read_text(FIXTURE)
    _fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    high_lines = set()
    for v in check_file(FIXTURE):
        if v["severity"] == c.HIGH:
            high_lines.add(v["line"])
    # locate the TP-*/FP-* bullet lines by marker
    want_fire, want_clean = {}, {}
    for i, ln in enumerate(body_lines):
        m = re.match(r"^\s*-\s+\*\*(TP-\d|FP-\d)", ln)
        if not m:
            continue
        lineno = start + i
        if m.group(1).startswith("TP"):
            want_fire[m.group(1)] = lineno
        else:
            want_clean[m.group(1)] = lineno
    for name, lineno in sorted(want_fire.items()):
        if lineno not in high_lines:
            errs.append("%s (line %d) must fire HIGH but did not" % (name, lineno))
    for name, lineno in sorted(want_clean.items()):
        if lineno in high_lines:
            errs.append("%s (line %d) must stay clean but fired HIGH" % (name, lineno))
    if len(want_fire) != 4 or len(want_clean) != 2:
        errs.append("fixture shape drift: found %d TP + %d FP markers (want 4 + 2)"
                    % (len(want_fire), len(want_clean)))

    # A9 >3-cases-per-paragraph fixtures (pass clean, fail fires HIGH)
    a9_pass = os.path.join(c.HERE, "fixtures", "lint-3-a9-pass.md")
    a9_fail = os.path.join(c.HERE, "fixtures", "lint-3-a9-fail.md")
    if os.path.exists(a9_pass):
        if any("A9" in v["message"] for v in check_file(a9_pass)):
            errs.append("A9 pass fixture fired (want clean)")
    else:
        errs.append("A9 pass fixture missing: %s" % a9_pass)
    if os.path.exists(a9_fail):
        if not any("A9" in v["message"] and v["severity"] == c.HIGH
                   for v in check_file(a9_fail)):
            errs.append("A9 fail fixture did not fire HIGH (want a >3-case flag)")
    else:
        errs.append("A9 fail fixture missing: %s" % a9_fail)

    if errs:
        for e in errs:
            sys.stderr.write("[self-test] LINT-3: %s\n" % e)
        return 1
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    c.cli_main(run, LINT)
