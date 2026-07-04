#!/usr/bin/env python3
"""
LINT-7 — glossary wiring + term register.   Enforces S1 N11/R11 · A3 · D13.

Deterministic glossary-wiring checks (the automatable subset of S7·R10 a–d):
  (a) [[Common Legal Terms#x]] anchor targets resolve.
  (b) [[Reading and Citing Cases#x]] anchor targets resolve (the current corpus
      page is "Legal Research and Case Citations"; both names accepted until the
      S2 rename).
  (c) No glossary term is linked more than once per page — the 2nd+ link to the
      same glossary anchor on a page is flagged LOW.

Term register (R11/A3) — consumes scripts/lint/term-register.yml directly:
  (d) For every term with `banned_variants`, a banned variant appearing in
      RENDERED PROSE (word-bounded, case-insensitive) = HIGH. Skipped contexts:
      frontmatter, code fences, inline code, blockquote lines, and text inside
      double quotes (quoted text keeps its original form). Precision: a banned
      variant never fires where the text is actually the canonical hyphenated
      form (e.g. "stop and frisk" must NOT fire inside "stop-and-frisk") — the
      match boundaries reject adjacent hyphens/word-chars. A missing or
      unparseable register is itself ONE HIGH violation (fail-closed) — never a
      crash. `drift_set` is NOT machine-lintable and is ignored (CHECKLIST:D5).

This lint does NOT judge glossary coverage or definition accuracy (S1 §9,
CHECKLIST-only). S8 later adds ledger-aware glossary enforcement — no S8
behavior here.

Usage: python3 lint7_glossary.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-7"

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTER_PATH = os.path.join(HERE, "term-register.yml")

# the glossary pages this lint audits (normalized names)
GLOSSARY_NAMES = {
    "common legal terms",
    "reading and citing cases",
    "legal research and case citations",
}

_QUOTED_RE = re.compile(r'"[^"]*"|“[^”]*”')


def _is_glossary_target(page):
    return c.CorpusIndex.norm(page) in GLOSSARY_NAMES


def load_register(path=REGISTER_PATH):
    """Parse the term register. Returns (variants, error).

    variants: list of (compiled_regex, canonical) for every banned variant.
    error:    a message string if the register is missing/unparseable, else None.
    """
    try:
        text = c.read_text(path)
    except OSError:
        return [], ("term register missing at %s — fail-closed [term register]"
                    % c.relpath(path))
    try:
        data = c.parse_yaml_subset(text.split("\n"))
    except Exception:
        data = None
    terms = data.get("terms") if isinstance(data, dict) else None
    if not isinstance(terms, list) or not terms:
        return [], ("term register unparseable (no `terms:` list) — fail-closed "
                    "[term register]")

    variants = []
    for term in terms:
        if not isinstance(term, dict):
            continue
        canonical = term.get("canonical")
        if not isinstance(canonical, str) or not canonical.strip():
            continue
        banned = term.get("banned_variants")
        if isinstance(banned, str):
            banned = [banned]
        if not isinstance(banned, list):
            continue
        for variant in banned:
            if not isinstance(variant, str) or not variant.strip():
                continue
            # word-bounded AND no hyphen on either boundary, so the banned
            # variant never fires inside the canonical hyphenated compound.
            rx = re.compile(r"(?<![\w-])" + re.escape(variant.strip())
                            + r"(?![\w-])", re.IGNORECASE)
            variants.append((rx, canonical.strip()))
    return variants, None


def _rendered(line):
    """Blank inline code spans and double-quoted text so the term matcher only
    sees rendered, unquoted prose."""
    line = c.INLINE_CODE_RE.sub(" ", line)
    line = _QUOTED_RE.sub(" ", line)
    return line


def check_file(path, idx, variants):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    seen_targets = {}   # (stem_norm, anchor) -> first lineno

    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i

        # (a)/(b)/(c) glossary wiring
        for m in c.WIKILINK_RE.finditer(line):
            inner = m.group(1).strip().split("|", 1)[0].strip()
            page, _, anchor = inner.partition("#")
            page = page.strip()
            anchor = anchor.strip()
            if not _is_glossary_target(page):
                continue
            stem = idx.resolve(page)
            if anchor:
                if stem is None or not idx.has_anchor(stem, anchor):
                    out.append(c.make_violation(
                        LINT, path, lineno, c.MEDIUM,
                        "glossary anchor does not resolve: [[%s#%s]] [N11/D13]"
                        % (page, anchor)))
            key = (c.CorpusIndex.norm(page), anchor.lower())
            if key in seen_targets:
                out.append(c.make_violation(
                    LINT, path, lineno, c.LOW,
                    "glossary term linked more than once on this page "
                    "(first at line %d): [[%s%s]] [N11]" % (
                        seen_targets[key], page,
                        "#" + anchor if anchor else "")))
            else:
                seen_targets[key] = lineno

        # (d) term-register banned variants in rendered prose
        if variants and not line.lstrip().startswith(">"):
            scan = _rendered(line)
            for rx, canonical in variants:
                hit = rx.search(scan)
                if hit:
                    out.append(c.make_violation(
                        LINT, path, lineno, c.HIGH,
                        "banned variant '%s' — canonical form is '%s' "
                        "[term register]" % (hit.group(0), canonical)))
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    variants, reg_error = load_register()
    out = []
    if reg_error:
        out.append(c.make_violation(LINT, REGISTER_PATH, 1, c.HIGH, reg_error))
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx, variants))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
