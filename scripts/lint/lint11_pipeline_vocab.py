#!/usr/bin/env python3
"""
LINT-11 — pipeline-vocab (TEACH-02b build; S9 R8 #11).

Bans editorial-pipeline vocabulary from reader-facing prose site-wide, per the
S1 A2 five-class pattern table (S1-standards.spec.md, Amendment A2). The five
classes:

  1  identifiers  — LINT-\\d+ / LINT-S2-*, rule refs [LNRG]\\d, SR-\\d, D-?\\d,
                    spec refs S1..S9  (committed exclusion list: S. Ct., §-numbered
                    statutes, docket formats + an adjudicated allowlist file)
  2  provenance   — "(re-homed|moved|merged|split|migrated) from"
  3  status       — "CL-confirm pending", "pending CL", "annotate-only",
                    "deferred to EXECUTE", "pending verification", TODO/TBD/FIXME
  4  meta-labels  — "(woven in)", "No standalone case page", "placeholder",
                    "this page intentionally"
  5a artifacts    — cl-calls.log, S6-SEED, RUNBOOK, PRACTICES, STANDARDS.md,
                    STYLE.md, *.spec.md, "wrapper"
  5b generic      — "data lake", "frontmatter", "lint" as OUR artifacts. The word
                    greps but the disqualifying intent is judgment-only, so 5b is
                    DEMOTED to CHECKLIST:D10 — a grep-assisted review sweep. It is
                    reported here as LOW (advisory), never a CI-failing HIGH.

Classes 1-5a are fail-closed HIGH. Scope = RENDERED PROSE ONLY: frontmatter,
HTML comments, code fences, and inline code spans are masked before matching, and
the About page (the one sanctioned methodology description) is allowlisted.

Usage: python3 lint11_pipeline_vocab.py [glob ...]   |   --self-test
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-11"
FIXTURE = os.path.join(c.HERE, "fixtures")
ALLOWLIST_FILE = os.path.join(c.HERE, "fixtures", "lint11-allowlist.json")

HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

# About page: the sanctioned methodology allowlist (by stem or title)
ABOUT_STEMS = {"about"}
ABOUT_TITLES = {"about this site"}

# ---- class patterns -------------------------------------------------------
CLASS1_RES = [
    re.compile(r"\bLINT(?:-S2)?-[0-9]+\b"),
    re.compile(r"\b[LNRG][0-9]{1,2}\b"),
    re.compile(r"\bSR-[0-9]\b"),
    re.compile(r"\bD-?[0-9]{1,2}\b"),
    re.compile(r"\bS[1-9]\b"),
]
CLASS2_RE = re.compile(r"\b(?:re-homed|moved|merged|split|migrated) from\b",
                       re.IGNORECASE)
CLASS3_RES = [
    re.compile(r"CL-confirm pending", re.IGNORECASE),
    re.compile(r"pending CL", re.IGNORECASE),
    re.compile(r"annotate-only", re.IGNORECASE),
    re.compile(r"deferred to EXECUTE", re.IGNORECASE),
    re.compile(r"pending verification", re.IGNORECASE),
    re.compile(r"\bTODO\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\bFIXME\b"),
]
CLASS4_RES = [
    re.compile(r"\(woven in\)", re.IGNORECASE),
    re.compile(r"No standalone case page", re.IGNORECASE),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
    re.compile(r"this page intentionally", re.IGNORECASE),
]
CLASS5A_RES = [
    re.compile(r"cl-calls\.log"),
    re.compile(r"\bS6-SEED\b"),
    re.compile(r"\bRUNBOOK\b"),
    re.compile(r"\bPRACTICES\b"),
    re.compile(r"\bSTANDARDS\.md\b"),
    re.compile(r"\bSTYLE\.md\b"),
    re.compile(r"\.spec\.md\b"),
    re.compile(r"\bwrapper\b"),
]
# 5b — advisory only (LOW), demoted to CHECKLIST:D10
CLASS5B_RES = [
    re.compile(r"\bdata lake\b", re.IGNORECASE),
    re.compile(r"\bfrontmatter\b", re.IGNORECASE),
    re.compile(r"\blint\b", re.IGNORECASE),
]

CLASS_LABELS = {
    "1": "identifier (rule/spec/lint ref)",
    "2": "provenance / re-homing note",
    "3": "pipeline status marker",
    "4": "editorial meta-label",
    "5a": "internal artifact name",
    "5b": "generic pipeline term (advisory)",
}


# built-in safe-context exclusions for class 1 (the committed exclusion list:
# reporter cites like "S. Ct.", §-numbered statutes, docket formats). A class-1
# hit whose surrounding context matches one of these is suppressed.
_DEFAULT_ALLOWLIST = [
    r"S\.\s?Ct\.",          # Supreme Court reporter
    r"L\.\s?Ed\.",          # Lawyers' Edition
    r"F\.\s?(?:2d|3d|4th)",  # Federal Reporter
    r"§\s?\d",              # statute section number
    r"No\.\s?\d",           # docket number "No. 25-885"
    r"\bNo\.\s?[0-9]{1,2}-[0-9]",  # docket "23-1399"
]


def _load_allowlist():
    """Committed exclusion list (safe contexts) + adjudicated per-hit allowlist.
    A hit clears ONLY via this file (each adjudicated under CHECKLIST:D10)."""
    pats = list(_DEFAULT_ALLOWLIST)
    adjudicated = []
    if os.path.exists(ALLOWLIST_FILE):
        try:
            with open(ALLOWLIST_FILE, encoding="utf-8") as f:
                d = json.load(f)
            pats += d.get("safe_context_patterns", [])
            adjudicated = d.get("adjudicated_hits", [])
        except (OSError, ValueError):
            pass
    return [re.compile(p) for p in pats], adjudicated


def _is_about(path, fm):
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    if stem in ABOUT_STEMS:
        return True
    title = (fm.get("title") or "").strip().lower()
    return title in ABOUT_TITLES


def _blank_keep_nl(m):
    return "".join("\n" if ch == "\n" else " " for ch in m.group(0))


def _mask_prose(body):
    """Mask HTML comments, fenced code, and inline code spans so only RENDERED
    prose remains (frontmatter is already stripped by the caller)."""
    body = HTML_COMMENT_RE.sub(_blank_keep_nl, body)
    lines = body.split("\n")
    fenced = c.fenced_line_numbers(lines)
    out = []
    for i, line in enumerate(lines):
        if i in fenced:
            out.append(" " * len(line))
        else:
            out.append(c.INLINE_CODE_RE.sub(_blank_keep_nl, line))
    return "\n".join(out)


def _context(line, start, end, width=18):
    a = max(0, start - width)
    b = min(len(line), end + width)
    return line[a:b].strip()


def check_file(path, allow_res=None, adjudicated=None):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    if _is_about(path, fm):
        return out  # methodology allowlist
    if allow_res is None:
        allow_res, adjudicated = _load_allowlist()
    adjudicated = adjudicated or []
    masked = _mask_prose(body)
    lines = masked.split("\n")

    def flagged(cls, m, i, line, sev):
        ctx = _context(line, m.start(), m.end())
        # class-1 committed exclusion list (reporter cites / statute / docket)
        if cls == "1" and any(r.search(ctx) for r in allow_res):
            return None
        # adjudicated per-hit allowlist (ANY class): a hit clears only via the
        # committed file, each entry adjudicated under CHECKLIST:D10 (S1 A2). This
        # is the sanctioned path for a semantic false positive (e.g. a physical
        # "wrapper", a legal "split from", an English "placeholder") — the lint
        # author never suppresses; the orchestrator adjudicates entries in.
        key = "%s:%s" % (c.relpath(path), m.group(0))
        if key in adjudicated:
            return None
        return c.make_violation(
            LINT, path, start + i, sev,
            "pipeline-vocab class %s (%s): %r [S1 A2 / S9 R8 #11]"
            % (cls, CLASS_LABELS[cls], m.group(0)))

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        for r in CLASS1_RES:
            for m in r.finditer(line):
                v = flagged("1", m, i, line, c.HIGH)
                if v:
                    out.append(v)
        for m in CLASS2_RE.finditer(line):
            out.append(flagged("2", m, i, line, c.HIGH))
        for r in CLASS3_RES:
            for m in r.finditer(line):
                out.append(flagged("3", m, i, line, c.HIGH))
        for r in CLASS4_RES:
            for m in r.finditer(line):
                out.append(flagged("4", m, i, line, c.HIGH))
        for r in CLASS5A_RES:
            for m in r.finditer(line):
                out.append(flagged("5a", m, i, line, c.HIGH))
        for r in CLASS5B_RES:
            for m in r.finditer(line):
                out.append(flagged("5b", m, i, line, c.LOW))  # advisory (D10)
    return [v for v in out if v]


def run(paths=None):
    allow_res, adjudicated = _load_allowlist()
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, allow_res, adjudicated))
    return out


def corpus_counts(paths=None):
    """Return {class: {high|low, count}} over the scanned corpus (report helper)."""
    counts = {k: 0 for k in CLASS_LABELS}
    for v in run(paths):
        m = re.search(r"class (\S+) ", v["message"])
        if m:
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    return counts


# --------------------------------------------------------------------------
# self-test — labeled fixtures (-pass / -fail); keys on HIGH severity so 5b
# advisories on a pass fixture do not trip it.
# --------------------------------------------------------------------------

def self_test():
    files = sorted(glob.glob(os.path.join(FIXTURE, "lint-11-*.md")))
    if not files:
        sys.stderr.write("[self-test] LINT-11 FAIL: no lint-11-*.md fixtures\n")
        return 1
    allow_res, adjudicated = _load_allowlist()
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_file(f, allow_res, adjudicated)
        nhigh = sum(1 for v in viols if v["severity"] == c.HIGH)
        passed = (nhigh == 0) if expect == "pass" else (nhigh > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-34s expect=%-4s -> %s (%d HIGH, %d total)\n"
                         % (name, expect, "OK" if passed else "MISMATCH",
                            nhigh, len(viols)))
        if not passed:
            for v in viols:
                sys.stderr.write("             %s\n" % v["message"])
    sys.stderr.write("[self-test] LINT-11 %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    if "--corpus-counts" in sys.argv[1:]:
        rest = [a for a in sys.argv[1:] if not a.startswith("-")]
        print(json.dumps(corpus_counts(rest or None), indent=2))
        sys.exit(0)
    c.cli_main(run, LINT)
