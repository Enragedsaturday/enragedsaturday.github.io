#!/usr/bin/env python3
"""
LINT-26 — good-law target resolves.  S4 · R5 (alias LINT-S4-goodlaw-target;
S9 R8 roster row 26).  FAIL-CLOSED.

The treatment pill (page header `TreatmentBadge` + the casetable-injected table
badges) links to the "how we verify good law" methodology page via ONE exported
constant in `quartz/components/caseHelpers.ts`:

    export const GOOD_LAW_SLUG = "2-legal-system-research/Verifying-Good-Law" as FullSlug

S3's restructure re-homes that page at EXECUTE; when it moves, this constant is
the single edit. This lint guarantees the constant's target still resolves to a
real content page — so a stale constant (page renamed/moved without updating
`GOOD_LAW_SLUG`) fails the build instead of shipping a dead pill link.

Checks (either ⇒ HIGH, exit 1):
  (1) the `GOOD_LAW_SLUG` constant cannot be parsed from caseHelpers.ts
      (renamed / deleted / reshaped — the mechanism is unwired), OR
  (2) its slug value does not resolve to any page via the shared CorpusIndex.

Not a content scan: the `paths` scoping arg is accepted and ignored (the target
is a fixed source constant + the whole corpus).

Usage: python3 lint26_goodlaw_target.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-26"

# quartz/components/caseHelpers.ts, relative to the repo root
CASEHELPERS_REL = os.path.join("quartz", "components", "caseHelpers.ts")

# export const GOOD_LAW_SLUG = "…"  (single or double quoted)
CONST_RE = re.compile(
    r"""export\s+const\s+GOOD_LAW_SLUG\s*=\s*["']([^"']+)["']"""
)


def run(paths=None):  # noqa: ARG001 (roster signature; scoping arg ignored)
    src_path = os.path.join(c.REPO_ROOT, CASEHELPERS_REL)

    if not os.path.isfile(src_path):
        return [c.make_violation(
            LINT, src_path, 1, c.HIGH,
            "good-law target source missing: %s not found — the pill/anchor "
            "mechanism is unwired [S4 R5]" % CASEHELPERS_REL)]

    text = c.read_text(src_path)

    # locate the constant + its line number for an accurate report
    const_line = 1
    slug = None
    for i, line in enumerate(text.split("\n"), start=1):
        m = CONST_RE.search(line)
        if m:
            slug = m.group(1).strip()
            const_line = i
            break
    if slug is None:
        # fall back to a whole-file search in case of odd wrapping
        m = CONST_RE.search(text)
        if m:
            slug = m.group(1).strip()

    if not slug:
        return [c.make_violation(
            LINT, src_path, 1, c.HIGH,
            "exported constant GOOD_LAW_SLUG not found in %s — the good-law pill "
            "target is unresolvable (fail-closed) [S4 R5]" % CASEHELPERS_REL)]

    idx = c.build_corpus_index()
    stem = idx.resolve(slug)
    if stem is None:
        return [c.make_violation(
            LINT, src_path, const_line, c.HIGH,
            "GOOD_LAW_SLUG = \"%s\" does not resolve to any content page — the "
            "treatment pills point at a dead link; re-home the page or update the "
            "one constant (fail-closed) [S4 R5]" % slug)]

    # resolved — no violation
    return []


if __name__ == "__main__":
    c.cli_main(run, LINT)
