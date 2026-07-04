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
  (2) its slug value is not the EXACT Quartz FullSlug of any content page.
      Exact-route matching (F-S4-01): the constant is emitted as a raw href
      ("/" + GOOD_LAW_SLUG) and via resolveRelative — Quartz does NOT resolve
      it by basename like a wikilink, so a stale FOLDER PATH 404s in the build
      even though the page exists. We mirror quartz/util/path.ts sluggify()
      exactly (per segment: \\s→"-", &→"-and-", %→"-percent", strip ? and #;
      case preserved; .md dropped) and require set membership. A
      basename-resolvable-but-wrong-path constant reports the correct path in
      the violation message.

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

    # exact-route validation (F-S4-01): build the set of real Quartz FullSlugs
    exact_slugs = {}
    for page in c.iter_markdown_files(None):
        rel = os.path.relpath(page, c.CONTENT_ROOT)
        full_slug = _quartz_full_slug(rel)
        exact_slugs[full_slug] = rel

    if slug in exact_slugs:
        return []  # exact route exists — no violation

    # not an exact route: diagnose whether the page exists elsewhere
    idx = c.build_corpus_index()
    stem = idx.resolve(slug.split("/")[-1].replace("-", " "))
    hint = ""
    if stem is not None:
        for fs, rel in exact_slugs.items():
            if os.path.splitext(os.path.basename(rel))[0] == stem:
                hint = (" — the page exists at \"%s\"; update the one constant "
                        "to that exact path" % fs)
                break
    return [c.make_violation(
        LINT, src_path, const_line, c.HIGH,
        "GOOD_LAW_SLUG = \"%s\" is not the exact FullSlug of any content page "
        "(emitted as a raw href, so this 404s in the build)%s (fail-closed) "
        "[S4 R5]" % (slug, hint))]


def _quartz_full_slug(rel_md_path):
    """Mirror quartz/util/path.ts slugifyFilePath()+sluggify() for .md files:
    strip the extension, then per path segment: whitespace→'-', '&'→'-and-',
    '%'→'-percent', strip '?' and '#'; case preserved; '/' separators."""
    p = rel_md_path.replace(os.sep, "/")
    if p.endswith(".md"):
        p = p[:-3]
    segs = []
    for seg in p.split("/"):
        seg = re.sub(r"\s", "-", seg)
        seg = seg.replace("&", "-and-").replace("%", "-percent")
        seg = seg.replace("?", "").replace("#", "")
        segs.append(seg)
    slug = "/".join(segs).rstrip("/")
    if slug.endswith("_index"):
        slug = slug[: -len("_index")] + "index"
    return slug


if __name__ == "__main__":
    c.cli_main(run, LINT)
