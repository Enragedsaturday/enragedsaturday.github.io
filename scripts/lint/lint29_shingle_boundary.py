#!/usr/bin/env python3
"""
LINT-29 — R9 transclusion boundary (the shingle detector as a CI gate).

Spec S8 R9 makes the S1 A3 shingle detector the mechanical line between "restate
in your own words + link" and "embed the canonical block". This lint wraps
`scripts/s8/shingles.py` (the frozen detector) and turns its cross-page overlaps
into severities:

  * a RULE-node overlap >=25 tokens outside an embed          -> HIGH
    (a page re-typing another page's black-letter `^rule-*` callout — must embed
    the rule shell `![[<full-slug>#^rule-...]]`, R9(a)).
  * a PIN overlap that is a RE-TYPED BLOCK QUOTE (>=25 tokens) -> HIGH
    (a `>` block-quote re-typing a passage a case page already pins — must embed
    the pin block `![[cases/<Case>#^pin-N]]`, R9(b)).
  * a PIN overlap woven INLINE (paragraph) or in a LIST item  -> EXEMPT
    (the adjudicated sanctioned class: short quoted snippets woven into a sentence
    stay ordinary quoted text + R4 links, R9's own carve-out).

Embeds are excluded from matching BY CONSTRUCTION (shingles.normalize blanks
`![[...]]`), so every hit is already "outside an embed". The detector runs over the
WHOLE corpus (cross-page sources must be complete); when scoped to a subset, only
hits IN the scoped files are reported. READ-ONLY, stdlib only.

Usage: python3 lint29_shingle_boundary.py [glob ...]   ( --self-test for the gate )
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

sys.path.insert(0, os.path.join(c.REPO_ROOT, "scripts", "s8"))
import shingles  # noqa: E402  (frozen detector)

LINT = "LINT-29"

_INLINE_EXEMPT_KINDS = ("para", "listitem")


def classify_hit(hit):
    """Return (severity, reason) or (None, reason) for one shingle hit."""
    kind = hit.get("kind")
    bk = hit.get("_prose_block_kind")
    if kind == "rule":
        return c.HIGH, ("rule-node restatement (%d tokens) of [[%s#^%s]] — embed "
                        "the rule shell instead of re-typing it [S8 R9a]"
                        % (hit["overlap_tokens"], hit["source_page"],
                           hit["source_anchor"]))
    if kind == "pin":
        if bk == "blockquote":
            return c.HIGH, ("re-typed block quote (%d tokens) of pinned passage "
                            "[[%s#^%s]] — embed the pin block instead [S8 R9b]"
                            % (hit["overlap_tokens"], hit["source_page"],
                               hit["source_anchor"]))
        if bk in _INLINE_EXEMPT_KINDS:
            return None, "inline-woven/list pin overlap (sanctioned R9 class)"
    return None, "unclassified overlap (not a rule/blockquote-pin restatement)"


def run(paths=None):
    hits, _stats = shingles.sweep(c.CONTENT_ROOT)
    scope = None
    if paths:
        scope = set(c.iter_markdown_files(paths))
    out = []
    for h in hits:
        if scope is not None and h["file"] not in scope:
            continue
        sev, reason = classify_hit(h)
        if sev is not None:
            out.append(c.make_violation(LINT, h["file"], h["line"], sev, reason))
    return out


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

FIXTURE = os.path.join(c.HERE, "fixtures", "lint-29", "content")


def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        p = (got == want)
        ok = ok and p
        sys.stderr.write("[self-test] %-46s -> %s (got=%s want=%s)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    # unit: classify_hit on synthetic hits
    check("rule-hit-HIGH",
          classify_hit({"kind": "rule", "_prose_block_kind": "para",
                        "overlap_tokens": 30, "source_page": "p",
                        "source_anchor": "rule-x"})[0], c.HIGH)
    check("pin-blockquote-HIGH",
          classify_hit({"kind": "pin", "_prose_block_kind": "blockquote",
                        "overlap_tokens": 30, "source_page": "cases/X",
                        "source_anchor": "pin-1"})[0], c.HIGH)
    check("pin-para-exempt",
          classify_hit({"kind": "pin", "_prose_block_kind": "para",
                        "overlap_tokens": 30, "source_page": "cases/X",
                        "source_anchor": "pin-1"})[0], None)
    check("pin-listitem-exempt",
          classify_hit({"kind": "pin", "_prose_block_kind": "listitem",
                        "overlap_tokens": 30, "source_page": "cases/X",
                        "source_anchor": "pin-1"})[0], None)

    # fixture sweep: a rule restatement (HIGH) + a re-typed blockquote pin (HIGH)
    # + an inline-woven pin (EXEMPT). Expect exactly 2 HIGH, 0 for the inline one.
    hits, stats = shingles.sweep(FIXTURE)
    viols = []
    for h in hits:
        sev, _r = classify_hit(h)
        if sev is not None:
            viols.append((os.path.basename(h["file"]), sev, h["kind"],
                          h.get("_prose_block_kind")))
    highs = [v for v in viols if v[1] == c.HIGH]
    kinds = {(v[0], v[2], v[3]) for v in highs}
    check("fixture-HIGH-count", len(highs), 2)
    check("fixture-rule-HIGH",
          any(k[1] == "rule" for k in kinds), True)
    check("fixture-blockquote-pin-HIGH",
          any(k[1] == "pin" and k[2] == "blockquote" for k in kinds), True)
    check("fixture-inline-pin-not-flagged",
          any(v[0] == "Pin Inline.md" for v in viols), False)

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
