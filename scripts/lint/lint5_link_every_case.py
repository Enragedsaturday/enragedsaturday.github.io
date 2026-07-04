#!/usr/bin/env python3
"""
LINT-5 — link every named case + fail-closed wikilink resolve.  S1 R13 · N7/D13.

Two checks, using a page+anchor index built from the WHOLE corpus (so resolution
is correct even when this lint is scoped to a subset of files):

  (a) Bare case names: any party-v-party case name (e.g. "Foo v. Bar") in
      prose/tables that is NOT wrapped in a [[wikilink]] is flagged MEDIUM (it
      should link to its case page). Names inside [[...]] or code are ignored.
      A Markdown link to CourtListener does NOT satisfy N7.

  (b) Fail-closed wikilink resolve (S1 R13): every [[Target]] / [[Target#anchor]]
      / [[Target#^block]] / [[Target|display]] in content/**/*.md must resolve
      via CorpusIndex — the page part must resolve, and any #anchor / #^block
      must exist per has_anchor. An unresolvable page = HIGH ("dead wikilink —
      blocks publish"); a missing anchor on a resolvable page = HIGH ("broken
      anchor"). Exclusions: code fences and inline code; [[#local-anchor]]
      resolves against the current page.

This lint is intentionally ledger-unaware: S8 rewrites LINT-5 later to consult
the linking ledger. Implement NO S8 behavior now — this is the R13 fail-closed
baseline only.

Usage: python3 lint5_link_every_case.py [glob ...]
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-5"

# words that, as a left "party", indicate this is NOT a case (defensive)
_NON_CASE_LEFT = {"see", "cf", "e.g", "id", "compare", "accord", "but"}


def _in_code_span(pos, spans):
    return any(s <= pos < e for (s, e) in spans)


def check_file(path, idx):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    this_stem = os.path.splitext(os.path.basename(path))[0]

    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i

        # (b) fail-closed wikilink resolve — skip links inside inline code spans
        code_spans = [(m.start(), m.end())
                      for m in c.INLINE_CODE_RE.finditer(line)]
        for m in c.WIKILINK_RE.finditer(line):
            if _in_code_span(m.start(), code_spans):
                continue
            inner = m.group(1).strip()
            inner = inner.split("|", 1)[0].strip()      # drop |display
            page, _, anchor = inner.partition("#")
            page = page.strip()
            anchor = anchor.strip()
            if page == "":
                # same-page anchor [[#anchor]] resolves against THIS page
                if anchor and not idx.has_anchor(this_stem, anchor):
                    out.append(c.make_violation(
                        LINT, path, lineno, c.HIGH,
                        "broken anchor: same-page [[#%s]] not found on this page "
                        "[R13]" % anchor))
                continue
            stem = idx.resolve(page)
            if stem is None:
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "dead wikilink — blocks publish: [[%s]] does not resolve to "
                    "a page [R13]" % page))
                continue
            if anchor and not idx.has_anchor(stem, anchor):
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "broken anchor: [[%s#%s]] — anchor not found on target "
                    "page [R13]" % (page, anchor)))

        # (a) bare case names (mask out wikilinks + code so linked names skip)
        masked = c.mask_links_and_code(line)
        for m in c.CASE_RE.finditer(masked):
            left = m.group(1).strip()
            if left.lower().rstrip(".") in _NON_CASE_LEFT:
                continue
            name = m.group(0).strip()
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "bare case name '%s' is not a [[wikilink]] to its case page "
                "[N7/D13]" % (name[:80])))
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
