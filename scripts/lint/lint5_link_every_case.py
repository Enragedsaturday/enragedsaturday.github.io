#!/usr/bin/env python3
"""
LINT-5 — link every PAGE-BACKED case + fail-closed wikilink/embed resolve.
S8 R13(a) rewrite of the S1-baseline lint (the ledger-aware bare-caption check).

R13(a) — what changed from the pre-S8 baseline (which flagged EVERY party-v-party
name as MEDIUM, 2767 hits, most of them false positives):

  (a) BARE-CAPTION check is now LEDGER-AWARE. A bare "Foo v. Bar" in prose is a
      MEDIUM only when its caption is PAGE-BACKED (a case page exists — S6
      `authored`/page-backed, or the S8 caption index carries a page_stem). A bare
      caption whose S6 disposition is a NON-PAGE terminal (brief-mention /
      excluded-remit / folded-alias / removed / unverifiable / watch) is a PASS —
      it is *supposed* to stay plain text (R1's ledger rule, not an exception). A
      bare caption that is neither page-backed nor a ledger terminal (a genuinely
      uncovered case, S9-inbox-routed) is also a PASS — there is no page to link.

  (b) R2 EXEMPTION ZONES are shared via `scripts/s8/zones.py` (the one catalog):
      headings, code/mermaid, direct quotations, citation strings, `## Sources`
      sections, frontmatter/comments, the term's own page, and the sanctioned Case
      cells of R6 tables never fire. Additionally, markdown-LINK TEXT `[name](url)`
      is masked — this kills the Sources false-positive class (57/59 of the mockup
      hits) where a case name lives inside a CourtListener markdown link.

  (c) BROKEN ANCHOR escalates MEDIUM -> HIGH (fail-closed): a wikilink whose page
      does not resolve is a dead link (HIGH); a `#anchor` / `#^block` that does not
      exist on a resolvable page is a broken anchor (HIGH). Deep links + embeds are
      load-bearing (R6/R9), so a dangling anchor blocks publish.

  (d) `![[embed]]` TARGETS must be FULL-SLUG (path-qualified — contain a `/`), per
      R9's embed grammar (name/alias targets silently fall back to a bare link). A
      non-full-slug embed = HIGH; an embed whose page/anchor does not resolve = HIGH.

Zones/ledger read-only. Falls back gracefully (one MEDIUM note, anchor/embed checks
still run) if the S6 ledger / caption index are absent.

Usage: python3 lint5_link_every_case.py [glob ...]   ( --self-test for the gate )
"""

import bisect
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

sys.path.insert(0, os.path.join(c.REPO_ROOT, "scripts", "s8"))
import zones  # noqa: E402  (frozen R2 catalog)

LINT = "LINT-5"

S6_LEDGER = os.path.join(c.REPO_ROOT, "_run", "s6-coverage-ledger.json")
CAPTION_INDEX = os.path.join(c.REPO_ROOT, "_run", "o2-execute", "s8-caption-index.json")

NONPAGE_TERMINALS = {"brief-mention", "excluded-remit", "folded-alias",
                     "removed", "unverifiable", "watch"}

# left "party" tokens that mark a non-case (defensive; mirrors the baseline).
_NON_CASE_LEFT = {"see", "cf", "e.g", "id", "compare", "accord", "but"}

_EMBED_RE = re.compile(r"!\[\[([^\[\]]+?)\]\]")


# --------------------------------------------------------------------------
# ledger authority
# --------------------------------------------------------------------------

def load_authority(s6_path=S6_LEDGER, ci_path=CAPTION_INDEX):
    """Return (pagebacked:set[norm], nonpage:set[norm], error:str|None)."""
    pagebacked, nonpage = set(), set()
    err = None
    if not os.path.isfile(s6_path) and not os.path.isfile(ci_path):
        return pagebacked, nonpage, (
            "S8 caption authority absent (S6 ledger + caption index both missing) "
            "— bare-caption ledger check degraded to anchor/embed checks only "
            "[S8 R13a]")
    if os.path.isfile(s6_path):
        try:
            led = json.load(open(s6_path, encoding="utf-8"))
            for r in led.get("rows", []):
                for k in (r.get("caption"), r.get("canonical")):
                    if not k:
                        continue
                    if r.get("page_backed") or r.get("terminal") == "authored":
                        pagebacked.add(c.CorpusIndex.norm(k))
                    elif r.get("terminal") in NONPAGE_TERMINALS:
                        nonpage.add(c.CorpusIndex.norm(k))
        except (OSError, json.JSONDecodeError) as exc:
            err = "S6 ledger unreadable: %s" % exc
    if os.path.isfile(ci_path):
        try:
            ci = json.load(open(ci_path, encoding="utf-8"))
            for cap, e in (ci.get("entries") or {}).items():
                if not isinstance(e, dict):
                    continue
                if e.get("page_stem") or e.get("terminal") == "authored" \
                        or "page" in (e.get("sources") or []):
                    pagebacked.add(c.CorpusIndex.norm(cap))
                elif e.get("terminal") in NONPAGE_TERMINALS:
                    nonpage.add(c.CorpusIndex.norm(cap))
        except (OSError, json.JSONDecodeError) as exc:
            err = "caption index unreadable: %s" % exc
    return pagebacked, nonpage, err


def _page_backed(caption, idx, pagebacked):
    n = c.CorpusIndex.norm(caption)
    if n in pagebacked:
        return True
    return idx is not None and idx.resolve(caption) is not None


# --------------------------------------------------------------------------
# offset helpers
# --------------------------------------------------------------------------

def _line_starts(text):
    starts = [0]
    i = text.find("\n")
    while i != -1:
        starts.append(i + 1)
        i = text.find("\n", i + 1)
    return starts


def _line_of(offset, starts):
    return bisect.bisect_right(starts, offset)


def _blank_spans(buf, spans):
    for a, b in spans:
        for i in range(a, min(b, len(buf))):
            if buf[i] != "\n":
                buf[i] = " "


# --------------------------------------------------------------------------
# per-file check
# --------------------------------------------------------------------------

def check_file(path, idx, pagebacked, this_stem=None):
    out = []
    text = c.read_text(path)
    if this_stem is None:
        this_stem = os.path.splitext(os.path.basename(path))[0]
    starts = _line_starts(text)
    zone_list = zones.compute_zones(text, page_stem=this_stem)
    nolink = [z for z in zone_list if z["kind"] in ("code", "comment", "frontmatter")]

    def exempt_nolink(off):
        return zones.is_exempt(off, nolink)

    # ---- (c)/(d) wikilink + embed resolution (fail-closed) ----
    embed_spans = []
    for m in _EMBED_RE.finditer(text):
        embed_spans.append((m.start(), m.end()))
        if exempt_nolink(m.start()):
            continue
        inner = m.group(1).strip().split("|", 1)[0].strip()
        page, _, anchor = inner.partition("#")
        page = page.strip()
        anchor = anchor.strip()
        lineno = _line_of(m.start(), starts)
        if "/" not in page:
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "embed target not full-slug (path-qualified): ![[%s]] — R9 embed "
                "grammar requires a full-slug target (name/alias silently falls "
                "back to a bare link) [S8 R13d]" % inner[:80]))
            continue
        stem = idx.resolve(page)
        if stem is None:
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "embed target does not resolve: ![[%s]] [S8 R9/R13d]" % inner[:80]))
        elif anchor and not idx.has_anchor(stem, anchor):
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "embed anchor not found on target: ![[%s]] [S8 R9/R13d]" % inner[:80]))

    for m in c.WIKILINK_RE.finditer(text):
        # skip the [[...]] that belongs to an ![[embed]] (handled above)
        if m.start() > 0 and text[m.start() - 1] == "!":
            continue
        if exempt_nolink(m.start()):
            continue
        inner = m.group(1).strip().split("|", 1)[0].strip()
        page, _, anchor = inner.partition("#")
        page = page.strip()
        anchor = anchor.strip()
        lineno = _line_of(m.start(), starts)
        if page == "":
            if anchor and not idx.has_anchor(this_stem, anchor):
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "broken anchor: same-page [[#%s]] not found on this page "
                    "[S8 R13c]" % anchor))
            continue
        stem = idx.resolve(page)
        if stem is None:
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "dead wikilink — blocks publish: [[%s]] does not resolve to a page "
                "[S8 R13c]" % page))
        elif anchor and not idx.has_anchor(stem, anchor):
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "broken anchor: [[%s#%s]] — anchor not found on target page "
                "[S8 R13c]" % (page, anchor)))

    # ---- (a)/(b) bare PAGE-BACKED captions ----
    # mask R2 zones, then blank embeds / wikilinks / markdown-links / inline code
    # so only genuinely-bare prose captions survive.
    buf = list(zones.mask(text, zone_list))
    _blank_spans(buf, embed_spans)
    _blank_spans(buf, [(m.start(), m.end()) for m in c.WIKILINK_RE.finditer(text)])
    _blank_spans(buf, [(m.start(), m.end()) for m in c.MDLINK_RE.finditer(text)])
    _blank_spans(buf, [(m.start(), m.end()) for m in c.INLINE_CODE_RE.finditer(text)])
    masked = "".join(buf)

    for m in c.CASE_RE.finditer(masked):
        left = m.group(1).strip()
        if left.lower().rstrip(".") in _NON_CASE_LEFT:
            continue
        name = m.group(0).strip()
        if not _page_backed(name, idx, pagebacked):
            continue  # non-page terminal or genuinely uncovered -> stays plain (PASS)
        out.append(c.make_violation(
            LINT, path, _line_of(m.start(), starts), c.MEDIUM,
            "bare page-backed case name '%s' is not a [[wikilink]] to its case "
            "page [S8 R1/R13a]" % name[:80]))
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    pagebacked, _nonpage, err = load_authority()
    out = []
    if err:
        out.append(c.make_violation(LINT, S6_LEDGER, 1, c.MEDIUM, err))
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx, pagebacked))
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
        sys.stderr.write("[self-test] %-42s -> %s (got=%s want=%s)\n"
                         % (name, "OK" if p else "MISMATCH", got, want))

    # (1) ledger authority: page-backed flags, non-page does not
    class _Idx:
        def resolve(self, t):
            return "X" if c.CorpusIndex.norm(t) in ("terry v. ohio",
                                                    "cases/terry v. ohio") else None
        def has_anchor(self, stem, a):
            return a in ("^pin-1", "here")
    idx = _Idx()
    pb = {c.CorpusIndex.norm("Mapp v. Ohio")}
    check("pagebacked-via-resolve", _page_backed("Terry v. Ohio", idx, pb), True)
    check("pagebacked-via-index", _page_backed("Mapp v. Ohio", idx, pb), True)
    check("nonpage-not-flagged", _page_backed("Chapman v. California", idx, pb), False)

    # (2) fixture files: fail set fires, pass set is clean
    def run_fx(name, stem):
        p = os.path.join(FIXTURE, name)
        return check_file(p, idx, pb, this_stem=stem)

    v_bare = run_fx("lint-5-bare-fail.md", "Doctrine")
    check("bare-pagebacked-fail-med",
          sum(1 for v in v_bare if v["severity"] == c.MEDIUM), 1)
    check("bare-pagebacked-fail-nohigh",
          sum(1 for v in v_bare if v["severity"] == c.HIGH), 0)

    v_anchor = run_fx("lint-5-anchor-fail.md", "Doctrine")
    check("anchor+deadlink+badembed-HIGH",
          sum(1 for v in v_anchor if v["severity"] == c.HIGH), 3)

    v_pass = run_fx("lint-5-pass.md", "Doctrine")
    check("pass-clean", v_pass, [])

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
