#!/usr/bin/env python3
"""
LINT-7 — term register: coverage review + anchor resolution + banned variants.
S8 R13(b) rewrite (register-driven, term-register.v2 route/target/match columns).

R13(b) — what changed from the pre-S8 baseline:

  * DELETED — the old check (c), "no glossary term linked more than once per page"
    (first-occurrence-only). D1 INVERTED it: routing is now EVERY-occurrence
    density, so a repeated link is correct, not a LOW defect. The check cannot fire.

  * NEW (MEDIUM, review) — REGISTER COVERAGE. For every routed term (route:page |
    glossary | citing) in the v2 register, an occurrence of its canonical/`match`
    surface in rendered prose OUTSIDE the R2 zones that is NOT already inside a
    wikilink is a MEDIUM review item ("routed term left unlinked — should link
    per D1 every-occurrence"). Register-driven: surfaces come from the
    canonical/`match` columns; skip-route (officer-vernacular) terms never flag.

    THE PAGE-TITLE-VARIANT CARVE-OUT (handoff §2.2, the ~140-row known-FP class):
    a route:page term whose TARGET PAGE TITLE equals the term surface does NOT flag
    on its own target page (a term is never linked to its own home — R2 zone (g);
    the surface appears there as the page subject, not as a missed link). This kills
    the FP class MECHANICALLY (lint-avoidance never drives content — handoff rule J').

  * NEW (HIGH, fail) — DEAD REGISTER ANCHORS/TARGETS. Every routed term's `target`
    must resolve: the page part via CorpusIndex, and any `#anchor` / `#^block` on
    that page. A register row whose glossary/citing/page target stops resolving
    fails CI (S8 onward — spec R7/R8).

  * KEPT (HIGH) — the v1 BANNED-VARIANTS check: a banned spelling in rendered prose
    (word-bounded, case-insensitive) fails. Exempt contexts are the R2 zones
    (headings/code/quotes/citations/sources/frontmatter/self-page/case-cells) PLUS
    block quotes (R2(c): quoted opinion text keeps its original form). A missing /
    unparseable register is itself ONE HIGH (fail-closed), never a crash.

Zones shared via `scripts/s8/zones.py`. `drift_set` stays CHECKLIST:D5 (not machine-
lintable). Definition coverage/accuracy stays CHECKLIST (S1 §9).

Usage: python3 lint7_glossary.py [glob ...]   ( --self-test for the gate )
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

sys.path.insert(0, os.path.join(c.REPO_ROOT, "scripts", "s8"))
import zones  # noqa: E402  (frozen R2 catalog + iter_blocks)

LINT = "LINT-7"

HERE = os.path.dirname(os.path.abspath(__file__))
REGISTER_PATH = os.path.join(HERE, "term-register.yml")


# --------------------------------------------------------------------------
# register parsing (v2)
# --------------------------------------------------------------------------

def _bound_rx(surfaces):
    """One case-insensitive, word/hyphen-bounded alternation over `surfaces`
    (longest first so 'search incident to arrest' beats 'arrest')."""
    uniq = sorted({s.strip() for s in surfaces if s and s.strip()},
                  key=len, reverse=True)
    if not uniq:
        return None
    body = "|".join(re.escape(s) for s in uniq)
    return re.compile(r"(?<![\w-])(?:%s)(?![\w-])" % body, re.IGNORECASE)


def _skip_phrase_rx(phrase):
    """Word/hyphen-bounded matcher for a wrong-SENSE literal phrase (register
    `skip_phrases`). The inter-word separator tolerates whitespace AND emphasis
    markers (`*`/`_`) so 'Washington Post reporter' still spans the italic
    '*Washington Post* reporter' (mirrors link_terms._skip_phrase_regex)."""
    words = [re.escape(w) for w in phrase.split()]
    body = r"[\s*_]+".join(words) if words else re.escape(phrase)
    return re.compile(r"(?<![\w-])(?:%s)(?![\w-])" % body, re.IGNORECASE)


def load_register(path=REGISTER_PATH):
    """Return (banned, routed, error).

    banned : [(compiled_rx, canonical)] for every banned variant (bounded, no
             adjacent hyphen so it never fires inside the canonical compound).
    routed : [{canonical, route, target, surfaces, surface_rx}] for route in
             page|glossary|citing.
    error  : fail-closed message if the register is missing/unparseable, else None.
    """
    try:
        text = c.read_text(path)
    except (OSError, UnicodeDecodeError):
        return [], [], ("term register missing or unreadable at %s — fail-closed "
                        "[term register]" % c.relpath(path))
    try:
        data = c.parse_yaml_subset(text.split("\n"))
    except Exception:
        data = None
    terms = data.get("terms") if isinstance(data, dict) else None
    if not isinstance(terms, list) or not terms:
        return [], [], ("term register unparseable (no `terms:` list) — fail-closed "
                        "[term register]")

    banned, routed = [], []
    for term in terms:
        if not isinstance(term, dict):
            continue
        canonical = term.get("canonical")
        if not isinstance(canonical, str) or not canonical.strip():
            continue
        canonical = canonical.strip()

        bv = term.get("banned_variants")
        if isinstance(bv, str):
            bv = [bv]
        if isinstance(bv, list):
            for variant in bv:
                if isinstance(variant, str) and variant.strip():
                    rx = re.compile(r"(?<![\w-])" + re.escape(variant.strip())
                                    + r"(?![\w-])", re.IGNORECASE)
                    banned.append((rx, canonical))

        route = term.get("route")
        if route in ("page", "glossary", "citing"):
            surfaces = [canonical]
            match = term.get("match")
            if isinstance(match, str):
                match = [match]
            if isinstance(match, list):
                surfaces += [m for m in match if isinstance(m, str) and m.strip()]
            rx = _bound_rx(surfaces)
            if rx is not None:
                # CR-S8-18: carry the register's skip_phrases (wrong-SENSE literal
                # phrases the linker suppresses, e.g. 'vacated the room') so the
                # coverage scan does not flag an occurrence the register documents
                # as a defect if linked.
                sp = term.get("skip_phrases")
                if isinstance(sp, str):
                    sp = [sp]
                skip_phrases = [s.strip() for s in sp
                                if isinstance(s, str) and s.strip()] \
                    if isinstance(sp, list) else []
                routed.append({
                    "canonical": canonical,
                    "route": route,
                    "target": term.get("target"),
                    "surfaces": surfaces,
                    "surface_rx": rx,
                    "skip_phrases": skip_phrases,
                    "skip_rx": [_skip_phrase_rx(p) for p in skip_phrases],
                })
    return banned, routed, None


# --------------------------------------------------------------------------
# masking helpers (R2 zones + block quotes + links, offset-preserving)
# --------------------------------------------------------------------------

_WIKI = re.compile(r"\[\[[^\[\]]*?\]\]")
_EMB = re.compile(r"!\[\[[^\[\]]*?\]\]")


def _blank(buf, rx, text):
    for m in rx.finditer(text):
        for i in range(m.start(), min(m.end(), len(buf))):
            if buf[i] != "\n":
                buf[i] = " "


def _blank_blockquotes(buf, text):
    for b in zones.iter_blocks(text):
        if b["kind"] == "blockquote":
            for i in range(b["start"], min(b["end"], len(buf))):
                if buf[i] != "\n":
                    buf[i] = " "


def _blank_wikilink_targets(buf, text):
    """Blank the TARGET (page#anchor) portion of every `[[Target|display]]`,
    keeping the display text visible. A wikilink target is a page NAME (a proper
    noun / link address), never authored prose — so the page-title variant class
    ('[[Plain View Doctrine]]' referencing the real page vs the prose term-of-art
    'plain-view doctrine') is NOT a banned-variant defect (handoff §2.2, the
    ~140-row known-FP class). Display text after `|` IS rendered prose and stays
    visible (a piped '[[X|plain view doctrine]]' is still a real defect)."""
    for m in _WIKI.finditer(text):
        inner = text[m.start() + 2:m.end() - 2]
        pipe = inner.find("|")
        target_end = m.end() if pipe < 0 else (m.start() + 2 + pipe)
        for i in range(m.start(), min(target_end, len(buf))):
            if buf[i] != "\n":
                buf[i] = " "


def _line_starts(text):
    starts = [0]
    i = text.find("\n")
    while i != -1:
        starts.append(i + 1)
        i = text.find("\n", i + 1)
    return starts


def _toks(s):
    return re.findall(r"[a-z0-9]+", (s or "").lower().replace("-", " "))


def _sub(a, b):
    """True iff token list a is a contiguous sublist of b (or equal)."""
    if not a or len(a) > len(b):
        return False
    for i in range(len(b) - len(a) + 1):
        if b[i:i + len(a)] == a:
            return True
    return False


def _is_own_home(routed_term, stem, idx):
    """Page-title-variant carve-out: a route:page term on ITS target page whose
    title (stem) matches the term surface. Then the term is the page subject, not
    a missed link — do not flag (R2 zone (g))."""
    if routed_term["route"] != "page" or not routed_term["target"]:
        return False
    home = idx.resolve(routed_term["target"].split("#", 1)[0].strip()) if idx else None
    if home is None or home != stem:
        return False
    st = _toks(stem)
    return any(_sub(_toks(s), st) or _sub(st, _toks(s))
               for s in routed_term["surfaces"])


# --------------------------------------------------------------------------
# per-file check
# --------------------------------------------------------------------------

def check_file(path, idx, banned, routed, this_stem=None):
    out = []
    text = c.read_text(path)
    if this_stem is None:
        this_stem = os.path.splitext(os.path.basename(path))[0]
    starts = _line_starts(text)

    def line_of(off):
        import bisect
        return bisect.bisect_right(starts, off)

    zone_list = zones.compute_zones(text, page_stem=this_stem)

    # banned-variant scan surface: R2 zones + block quotes + embed targets +
    # wikilink TARGETS masked (the page-title FP class). Wikilink DISPLAY text and
    # markdown-link text stay visible — a banned form authored into rendered prose
    # is still a defect.
    banned_buf = list(zones.mask(text, zone_list))
    _blank_blockquotes(banned_buf, text)
    _blank(banned_buf, _EMB, text)
    _blank_wikilink_targets(banned_buf, text)
    banned_masked = "".join(banned_buf)
    for rx, canonical in banned:
        for m in rx.finditer(banned_masked):
            out.append(c.make_violation(
                LINT, path, line_of(m.start()), c.HIGH,
                "banned variant '%s' — canonical form is '%s' [term register]"
                % (m.group(0), canonical)))

    # register-coverage scan surface: additionally mask wikilinks/embeds/md-links/
    # inline code (a term inside a link IS linked -> not a coverage gap).
    cov_buf = list(banned_buf)
    _blank(cov_buf, _EMB, text)
    _blank(cov_buf, _WIKI, text)
    _blank(cov_buf, c.MDLINK_RE, text)
    _blank(cov_buf, c.INLINE_CODE_RE, text)
    cov_masked = "".join(cov_buf)
    for rt in routed:
        if _is_own_home(rt, this_stem, idx):
            continue
        # CR-S8-18: gather wrong-sense suppression spans (register skip_phrases);
        # a coverage match contained in one is correctly unlinked, not a gap.
        suppress = []
        for srx in rt.get("skip_rx", ()):
            for sm in srx.finditer(cov_masked):
                suppress.append((sm.start(), sm.end()))
        for m in rt["surface_rx"].finditer(cov_masked):
            if suppress and any(a <= m.start() and m.end() <= b for (a, b) in suppress):
                continue
            out.append(c.make_violation(
                LINT, path, line_of(m.start()), c.MEDIUM,
                "routed term '%s' (route:%s) left unlinked — link per D1 "
                "every-occurrence [S8 R7/R13b]" % (m.group(0), rt["route"])))
    return out


def dead_target_violations(idx, routed):
    """One HIGH per routed term whose target page/anchor does not resolve."""
    out = []
    for rt in routed:
        tgt = rt.get("target")
        if not tgt:
            out.append(c.make_violation(
                LINT, REGISTER_PATH, 1, c.HIGH,
                "routed term '%s' (route:%s) has no target — dead register row "
                "[S8 R7/R13b]" % (rt["canonical"], rt["route"])))
            continue
        page, _, anchor = tgt.partition("#")
        stem = idx.resolve(page.strip())
        if stem is None:
            out.append(c.make_violation(
                LINT, REGISTER_PATH, 1, c.HIGH,
                "dead register target: '%s' -> [[%s]] does not resolve "
                "[S8 R7/R13b]" % (rt["canonical"], page.strip())))
        elif anchor and not idx.has_anchor(stem, anchor.strip()):
            out.append(c.make_violation(
                LINT, REGISTER_PATH, 1, c.HIGH,
                "dead register anchor: '%s' -> [[%s#%s]] anchor not found "
                "[S8 R7/R13b]" % (rt["canonical"], page.strip(), anchor.strip())))
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    banned, routed, err = load_register()
    out = []
    if err:
        out.append(c.make_violation(LINT, REGISTER_PATH, 1, c.HIGH, err))
        return out
    out.extend(dead_target_violations(idx, routed))
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx, banned, routed))
    return out


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

FIXTURE = os.path.join(c.HERE, "fixtures")


def self_test():
    ok = True

    def check(name, got, want):
        nonlocal ok
        p = (got == want)
        ok = ok and p
        sys.stderr.write("[self-test] %-44s -> %s (got=%s want=%s)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    # (1) the DELETED first-occurrence rule cannot fire: repeated links are fine.
    #     -> asserted structurally below (no LOW ever emitted).

    class _Idx:
        def resolve(self, t):
            n = c.CorpusIndex.norm(t)
            return {"curtilage": "Curtilage",
                    "common legal terms": "Common Legal Terms",
                    "reading and citing cases": "Reading and Citing Cases"}.get(n)
        def has_anchor(self, stem, a):
            return a in ("de-novo", "en-banc")
    idx = _Idx()

    banned = [(re.compile(r"(?<![\w-])good faith exception(?![\w-])", re.I),
               "good-faith exception")]
    routed = [
        {"canonical": "curtilage", "route": "page", "target": "Curtilage",
         "surfaces": ["curtilage"], "surface_rx": _bound_rx(["curtilage"])},
        {"canonical": "de novo", "route": "glossary",
         "target": "Common Legal Terms#de-novo",
         "surfaces": ["de novo"], "surface_rx": _bound_rx(["de novo"])},
    ]

    def run_fx(name, stem):
        return check_file(os.path.join(FIXTURE, name), idx, banned, routed,
                          this_stem=stem)

    # banned variant fires HIGH; canonical does not; quoted form is exempt
    vb = run_fx("lint-7-banned-fail.md", "Doctrine")
    check("banned-variant-HIGH",
          sum(1 for v in vb if v["severity"] == c.HIGH), 1)
    check("no-LOW-ever", sum(1 for v in vb if v["severity"] == c.LOW), 0)

    # coverage: unlinked 'curtilage' MEDIUM; the linked one does not fire
    vc = run_fx("lint-7-coverage-fail.md", "Doctrine")
    check("coverage-unlinked-MEDIUM",
          sum(1 for v in vc if v["severity"] == c.MEDIUM), 1)
    check("coverage-no-HIGH",
          sum(1 for v in vc if v["severity"] == c.HIGH), 0)

    # carve-out: on Curtilage's own page, the 'curtilage' surface does NOT flag
    vh = run_fx("lint-7-coverage-fail.md", "Curtilage")
    check("page-title-carveout-suppresses",
          sum(1 for v in vh if "curtilage" in v["message"]), 0)

    # pass fixture: fully linked + canonical only -> clean
    vp = run_fx("lint-7-pass.md", "Doctrine")
    check("pass-clean", vp, [])

    # dead-target check: a routed term whose target does not resolve = HIGH
    dead = dead_target_violations(idx, [
        {"canonical": "phantom", "route": "page", "target": "No Such Page",
         "surfaces": ["phantom"], "surface_rx": _bound_rx(["phantom"])},
        {"canonical": "de novo", "route": "glossary",
         "target": "Common Legal Terms#de-novo",
         "surfaces": ["de novo"], "surface_rx": _bound_rx(["de novo"])},
        {"canonical": "bad anchor", "route": "glossary",
         "target": "Common Legal Terms#nope",
         "surfaces": ["bad anchor"], "surface_rx": _bound_rx(["bad anchor"])},
    ])
    check("dead-target-HIGH-count",
          sum(1 for v in dead if v["severity"] == c.HIGH), 2)

    # CR-S8-18: register skip_phrases suppress wrong-sense coverage flags. The
    # linked 'vacated' is masked (no flag); the wrong-sense 'vacated the room' is
    # suppressed by the skip_phrase; so WITH skip_phrases -> 0 MEDIUM, WITHOUT -> 1.
    routed_sp = [{"canonical": "vacated", "route": "citing",
                  "target": "Reading and Citing Cases#vacated",
                  "surfaces": ["vacated"], "surface_rx": _bound_rx(["vacated"]),
                  "skip_phrases": ["vacated the room"],
                  "skip_rx": [_skip_phrase_rx("vacated the room")]}]
    vs = check_file(os.path.join(FIXTURE, "lint-7-skipphrase.md"), idx, [], routed_sp,
                    this_stem="Doctrine")
    check("skipphrase-suppresses-wrong-sense",
          sum(1 for v in vs if v["severity"] == c.MEDIUM), 0)
    routed_nosp = [dict(routed_sp[0], skip_phrases=[], skip_rx=[])]
    vn = check_file(os.path.join(FIXTURE, "lint-7-skipphrase.md"), idx, [], routed_nosp,
                    this_stem="Doctrine")
    check("skipphrase-absent-flags-wrong-sense",
          sum(1 for v in vn if v["severity"] == c.MEDIUM), 1)

    # register loads clean from the real file (no fail-closed error)
    _b, _r, e = load_register()
    check("real-register-parses", e, None)

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
