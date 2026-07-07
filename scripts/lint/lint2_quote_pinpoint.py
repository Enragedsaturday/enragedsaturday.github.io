#!/usr/bin/env python3
"""
LINT-2 — quote / pinpoint presence.   Enforces S1 L1 (two-key rule) + D7.

Every block quotation (a Markdown blockquote) and every substantial inline
quotation ("…") must have an accompanying pinpoint cite NEARBY (same line or a
few lines around). A quote with no pinpoint should be de-quoted or pinned.

Heuristics (deterministic, tolerant of the pre-overhaul corpus):
  - A pinpoint cite = a reporter pincite ("547 U.S. at 403", "569 U.S. 1, 6")
    detected by _common.PINCITE_RE within a small window of the quote.
  - Inline quotes shorter than MIN_INLINE_WORDS words are ignored (single
    quoted terms like "search" or "open fields" are not assertions).
  - Quotes inside code fences and the frontmatter are ignored.

Severity: medium (de-quote/pin is a content fix, not a build-breaker).
Usage:    python3 lint2_quote_pinpoint.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-2"
MIN_INLINE_WORDS = 6      # only flag inline quotes at least this long
WINDOW = 2                # lines of context to search for a pinpoint

# inline quotation: straight or curly double quotes, non-greedy
INLINE_QUOTE_RE = re.compile(r"[\"“]([^\"”]{1,400}?)[\"”]")


def _pinpoint_near(body_lines, i):
    lo = max(0, i - WINDOW)
    hi = min(len(body_lines), i + WINDOW + 1)
    window = " ".join(body_lines[lo:hi])
    return bool(c.PINCITE_RE.search(window))


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i
        stripped = line.lstrip()

        # block quotation
        if stripped.startswith(">"):
            content = stripped.lstrip(">").strip()
            if not content:
                continue
            # if the blockquote itself or its context carries a pinpoint, ok
            if _pinpoint_near(body_lines, i):
                continue
            # also accept a pinpoint inside the blockquote run a couple lines on
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "block quotation without a nearby pinpoint cite "
                "(de-quote or add reporter pincite) [L1]"))
            continue

        # inline quotations
        masked = c.mask_links_and_code(line)
        for m in INLINE_QUOTE_RE.finditer(masked):
            quote = m.group(1).strip()
            if len(quote.split()) < MIN_INLINE_WORDS:
                continue
            # quote with a pinpoint on the same line or adjacent lines is fine
            if c.PINCITE_RE.search(line) or _pinpoint_near(body_lines, i):
                continue
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "inline quotation (%d words) without a nearby pinpoint cite "
                "[L1]: \"%s\"" % (
                    len(quote.split()),
                    (quote[:60] + "…") if len(quote) > 60 else quote)))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


def self_test():
    """Fixtures for the ¶-pin extension (W6 Ruckman escalation): a paragraph-pinned
    quote passes; the identical quote unpinned still fails. Also re-checks the
    reporter-pincite and `at N` forms so the ¶ alternative did not regress them."""
    import tempfile
    results = []

    def check(label, cond):
        results.append((label, bool(cond)))
        sys.stderr.write("[lint2 self-test] %-44s -> %s\n" % (label, "OK" if cond else "FAIL"))

    def viols(body):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write("---\ntitle: t\n---\n\n# t\n\n" + body + "\n")
            p = f.name
        try:
            return check_file(p)
        finally:
            os.remove(p)

    quote = ('As the court held: "Without belaboring the matter, we decline to hold that '
             'the instant case comes within the ambit of the Fourth Amendment."')
    # ¶-pinned inline quote passes (Ruckman shape)
    check("¶ N pin clears the inline quote",
          not viols(quote + " — 806 F.2d 1471 (10th Cir. 1986) (majority op. ¶ 9). ^pin-9"))
    # ¶¶ N–M range pin passes
    check("¶¶ N–M range pin clears the quote",
          not viols(quote + " — 749 F.3d 192 (3d Cir. 2014) (¶¶ 12–14)."))
    # identical quote with NO pin still fails
    check("unpinned inline quote still fails",
          any(v["lint"] == LINT for v in viols(quote)))
    # ¶-pinned block quote passes; unpinned block quote fails
    check("¶ pin clears a block quotation",
          not viols("> Some substantial quoted passage of the opinion here.\n\nSee id. ¶ 7."))
    check("unpinned block quotation still fails",
          any(v["lint"] == LINT for v in viols("> Some substantial quoted passage of the opinion here.")))
    # regression guards: the pre-existing pincite forms still clear
    check("reporter pincite `vol Rep p, pin` still clears",
          not viols(quote + " 569 U.S. 1, 6."))
    check("`at N` pincite still clears",
          not viols(quote + " 547 U.S. at 403."))

    ok = all(v for _l, v in results)
    sys.stderr.write("[lint2 self-test] %s (%d/%d)\n"
                     % ("PASS" if ok else "FAIL", sum(v for _l, v in results), len(results)))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
