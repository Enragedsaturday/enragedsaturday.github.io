#!/usr/bin/env python3
"""
LINT-25 — flashcard-deck stem preservation.  S3 · R14 / A2 (alias LINT-S3-deck;
S9 R8 roster row 25).  FAIL-CLOSED.  Realizes A2's resolution rule EXACTLY.

The O1 flashcard deck is frozen and references pages by a path-less slug STEM in
each card's `"page"` field (the sole join key — cards carry no wiki URLs). R3
re-homings, R9 renames, and the de-numbering can silently break it. This lint
resolves the deck against the moved tree.

EXTRACTION SET (A2): the union of `page` values across `flashcard-src/decks/*.json`.

RESOLUTION RULE (A2): after normalization (lowercase kebab; STEM-only, so folder
re-parenting / renumbering alone breaks nothing — only a filename-stem rename
does), every extracted stem must match either
  (i)  the final slug segment of an emitted page (a content-page filename stem), OR
  (ii) a BARE-STEM `aliases:` entry on some page (an alias with no `/`).
An unresolved AND unacknowledged stem => HIGH.

ACCEPTED-BREAKAGE (A2): any stem knowingly left unresolved is recorded in a table
appended to S3 Appendix B (schema `| deck_stem | card_count | successor_page |
reason | user_ack |`); rows carrying a `user_ack` are honored (not flagged).
Currently none is expected (P1 reported 44/44). If no such table exists in the
spec, the acknowledged set is empty.

Not scoped by `paths`.

SELF-TEST (S1 A3): `python3 lint25_deck.py --self-test` over the `fixtures/
lint-25-*` fixtures (a fixture content tree + resolving / non-resolving decks).

Usage:
  python3 lint25_deck.py
  python3 lint25_deck.py --self-test
"""

import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-25"

DECKS_REL = os.path.join("flashcard-src", "decks")
S3_SPEC_REL = os.path.join("_overhaul2", "specs", "S3-taxonomy.spec.md")


def normalize_stem(s):
    """A2 normalization: lowercase kebab, stem-only. Whitespace/underscores ->
    hyphens; apostrophe variants folded; collapse repeated hyphens."""
    t = (s or "").strip().lower().replace("’", "'")
    t = re.sub(r"[\s_]+", "-", t)
    t = re.sub(r"-+", "-", t)
    return t.strip("-")


def deck_stems(decks_dir):
    """Union of `page` stems across every deck JSON (A2 extraction set)."""
    stems = set()
    for f in sorted(glob.glob(os.path.join(decks_dir, "*.json"))):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        cards = d if isinstance(d, list) else d.get("cards") if isinstance(d, dict) else None
        if not isinstance(cards, list):
            continue
        for card in cards:
            if isinstance(card, dict) and isinstance(card.get("page"), str):
                p = card["page"].strip()
                if p:
                    stems.add(p)
    return stems


def resolution_targets(content_root):
    """A2 resolution targets: normalized final-slug-segment (filename stem) of
    every page + normalized BARE-STEM aliases entries."""
    targets = set()
    for p in glob.glob(os.path.join(content_root, "**", "*.md"), recursive=True):
        stem = os.path.splitext(os.path.basename(p))[0]
        targets.add(normalize_stem(stem))
        try:
            fm, _b, _s = c.split_frontmatter(c.read_text(p))
        except OSError:
            continue
        al = fm.get("aliases")
        als = al if isinstance(al, list) else ([al] if isinstance(al, str) and al.strip() else [])
        for a in als:
            if isinstance(a, str) and a.strip() and "/" not in a:  # bare stem only
                targets.add(normalize_stem(a))
    return targets


def acknowledged_stems(spec_path):
    """Parse the S3 Appendix B accepted-breakage table (if present) and return
    the set of normalized deck_stems whose row carries a non-empty user_ack."""
    acked = set()
    if not os.path.isfile(spec_path):
        return acked
    body_lines = c.read_text(spec_path).split("\n")
    for hidx, header_cells, rows in c.iter_tables(body_lines):
        norm_hdr = [h.strip().lower() for h in header_cells]
        if "deck_stem" not in norm_hdr or not any("user_ack" in h for h in norm_hdr):
            continue
        stem_col = norm_hdr.index("deck_stem")
        ack_col = next(i for i, h in enumerate(norm_hdr) if "user_ack" in h)
        for ridx in rows:
            cells = c.split_table_row(body_lines[ridx])
            if stem_col < len(cells) and ack_col < len(cells):
                if cells[ack_col].strip():
                    acked.add(normalize_stem(cells[stem_col]))
    return acked


def check_decks(decks_dir, content_root, spec_path=None):
    """A2 check. Returns violations (fail-closed on unresolved, unacknowledged
    stems)."""
    stems = deck_stems(decks_dir)
    if not stems:
        return [c.make_violation(
            LINT, decks_dir, 1, c.HIGH,
            "no deck `page` stems extracted from %s — the frozen deck's join key "
            "is absent (fail-closed) [R14/A2]" % c.relpath(decks_dir))]
    targets = resolution_targets(content_root)
    acked = acknowledged_stems(spec_path) if spec_path else set()
    out = []
    for s in sorted(stems):
        n = normalize_stem(s)
        if n in targets:
            continue
        if n in acked:
            out.append(c.make_violation(
                LINT, decks_dir, 1, c.LOW,
                "deck stem %r is unresolved but ACKNOWLEDGED (accepted-breakage "
                "table, user_ack) — deferred to flashcard rebuild run #2 [R14/A2]"
                % s))
            continue
        out.append(c.make_violation(
            LINT, decks_dir, 1, c.HIGH,
            "deck stem %r resolves to no emitted page (final slug segment) nor a "
            "bare-stem alias, and is not acknowledged — a frozen card now points "
            "nowhere (fail-closed) [R14/A2]" % s))
    return out


def run(paths=None):  # noqa: ARG001 (roster signature; scoping arg ignored)
    return check_decks(os.path.join(c.REPO_ROOT, DECKS_REL),
                       c.CONTENT_ROOT,
                       os.path.join(c.REPO_ROOT, S3_SPEC_REL))


# --------------------------------------------------------------------------
# self-test — fixture content tree + resolving / non-resolving decks
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    content = os.path.join(fixdir, "lint-25-content")
    decks_pass = os.path.join(fixdir, "lint-25-decks-pass")
    decks_fail = os.path.join(fixdir, "lint-25-decks-fail")
    for req in (content, decks_pass, decks_fail):
        if not os.path.isdir(req):
            sys.stderr.write("[self-test] FAIL: missing fixture dir %s\n" % req)
            return 1
    ok = True

    def check(desc, decks_dir, expect):
        nonlocal ok
        viols = check_decks(decks_dir, content, None)
        n_high = sum(1 for v in viols if v["severity"] == c.HIGH)
        passed = (n_high == 0) if expect == "pass" else (n_high >= 1)
        ok = ok and passed
        sys.stderr.write("[self-test] %-34s expect=%-4s -> %s (%d high)\n" % (
            desc, expect, "OK" if passed else "MISMATCH", n_high))
        if not passed:
            for v in viols:
                sys.stderr.write("             [%s] %s\n" % (v["severity"], v["message"]))

    check("stems resolve (stem + alias)", decks_pass, "pass")
    check("unresolvable stem", decks_fail, "high")

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
