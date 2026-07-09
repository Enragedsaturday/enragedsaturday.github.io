#!/usr/bin/env python3
"""
S8 duplicate-prose / restatement detector (spec S1 A3 · S8 R9).

THE EMBED BOUNDARY, ENCODED. R9 makes this detector the mechanical line between
"restate in your own words + link" and "embed the canonical block": prose that
would overlap a FOREIGN rule/pin block by >=25 contiguous tokens must embed
(embeds are the sanctioned way past the detector); below the threshold, link.

    ---- WHAT IT DETECTS ----
    (a) any PROSE block  x  any FOREIGN page's `^rule-*` callout block   -> kind "rule"
    (b) any PROSE block  x  any FOREIGN case page's `^pin-N` block        -> kind "pin"
    Same-page overlap is fine (a page may restate its own rule) -> never a hit.

    ---- TOKENIZATION / ZONE POLICY ----
    Block segmentation is `zones.iter_blocks` (frozen). PROSE blocks = para /
    listitem / blockquote blocks that are NOT themselves a rule-callout or a pin
    block, and that do not fall inside a `## Sources` section.

    Offset-preserving normalization (same length as the source, so char offsets
    -> exact line numbers survive):
      * embeds `![[...]]`               -> blanked  (EMBED-EXCLUDED BY CONSTRUCTION;
                                           an already-embedded block yields no tokens)
      * wikilink markup `[[t|disp]]`    -> only the rendered display text kept
      * markdown links `[txt](url)`     -> only `txt` kept
      * callout titles `[!rule] ...`    -> blanked (boilerplate)
      * block anchors `^rule-x`/`^pin-N`-> blanked (never tokens)
      * `## Sources` sections + HTML
        comments (R2 zones)             -> blanked

    DECISION (documented for adjudication): R2 `quote` and `citation` zones are
    NOT masked here. Flavor (b) is *defined by* re-typed direct quotations (which
    live inside `"..."` quote zones) and shared rule prose runs through inline
    citations; masking them would make the pinned-quote flavor undetectable. All
    other passes (case-mention / term linking) still honor those zones — this
    detector is the one place quoted text must participate in matching.

    ---- OUTPUT ----
    `_run/o2-execute/s8-shingle-report.jsonl`:
      one line per hit {file, line, overlap_tokens, source_page, source_anchor,
      kind, snippet}; final line {"_summary": {...}}.

Python 3 stdlib only. READ-ONLY vs content/. `--self-test` exercises the
fixtures under `scripts/s8/fixtures/shingles/`.

    python3 scripts/s8/shingles.py --self-test
    python3 scripts/s8/shingles.py [--content content] [--out <path>]
"""

from __future__ import annotations

import bisect
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zones  # noqa: E402  (frozen: iter_blocks / compute_zones / mask)

SHINGLE_K = 25  # spec S1 A3 / S8 R9: ">=25 overlapping tokens"

# Zone kinds blanked before tokenizing (structural, never restatable prose).
# NB: "quote" and "citation" are deliberately NOT here (see module docstring).
_MASK_ZONE_KINDS = ("sources", "comment", "frontmatter", "code")

_RE_TOKEN = re.compile(r"[A-Za-z0-9]+")
_RE_RULE_ANCHOR_LINE = re.compile(r"(?m)^\s*>\s*\^rule-([0-9A-Za-z][0-9A-Za-z-]*)\s*$")
_RE_PIN_END = re.compile(r"\^pin-([0-9A-Za-z]+)\s*$")


# --------------------------------------------------------------------------
# Offset-preserving normalization
# --------------------------------------------------------------------------

_RE_EMBED = re.compile(r"!\[\[.*?\]\]", re.DOTALL)
_RE_WIKILINK = re.compile(r"\[\[(.*?)\]\]", re.DOTALL)
_RE_MDLINK = re.compile(r"\[([^\]\n]*)\]\(([^)\n]*)\)")
_RE_CALLOUT_TITLE = re.compile(r"\[![A-Za-z]+\][^\n]*")
_RE_BLOCK_ANCHOR = re.compile(r"\^[A-Za-z]+-[0-9A-Za-z-]+")
_RE_HTML_TAG = re.compile(r"<[^>\n]+>")


def normalize_inplace(text: str) -> str:
    """Return a SAME-LENGTH string with markup/embeds blanked to spaces.

    Newlines are preserved (so line math survives); only the rendered display
    text of wiki/markdown links is kept, at its original offsets.
    """
    buf = list(text)

    def blank(a: int, b: int) -> None:
        for i in range(a, min(b, len(buf))):
            if buf[i] != "\n":
                buf[i] = " "

    # 1. embeds -> gone entirely (embed-excluded by construction)
    for m in _RE_EMBED.finditer(text):
        blank(m.start(), m.end())

    # 2. callout titles ([!rule] Black-letter rule ...) -> boilerplate
    for m in _RE_CALLOUT_TITLE.finditer(text):
        if buf[m.start()] == " ":
            continue
        blank(m.start(), m.end())

    # 3. bare block anchors (^rule-x / ^pin-N) -> never tokens
    for m in _RE_BLOCK_ANCHOR.finditer(text):
        if buf[m.start()] == " ":
            continue
        blank(m.start(), m.end())

    # 4. wikilinks -> keep only rendered display text at its offsets
    for m in _RE_WIKILINK.finditer(text):
        a, b = m.start(), m.end()
        if buf[a] == " ":  # already inside a blanked embed
            continue
        inner = m.group(1)
        if "|" in inner:
            disp_start = a + 2 + inner.rindex("|") + 1
            disp_end = b - 2
        else:
            base = inner.split("#", 1)[0]
            seg_rel = base.rfind("/") + 1
            disp_start = a + 2 + seg_rel
            disp_end = a + 2 + len(base)
        blank(a, disp_start)
        blank(disp_end, b)

    # 5. markdown links [text](url) -> keep text
    for m in _RE_MDLINK.finditer(text):
        a, b = m.start(), m.end()
        if buf[a] == " ":
            continue
        text_start = a + 1
        text_end = a + 1 + len(m.group(1))
        blank(a, text_start)
        blank(text_end, b)

    # 6. html tags
    for m in _RE_HTML_TAG.finditer(text):
        if buf[m.start()] == " ":
            continue
        blank(m.start(), m.end())

    return "".join(buf)


# --------------------------------------------------------------------------
# Tokenization with exact line numbers
# --------------------------------------------------------------------------

def _line_starts(text: str) -> list:
    starts = [0]
    i = text.find("\n")
    while i != -1:
        starts.append(i + 1)
        i = text.find("\n", i + 1)
    return starts


def tokenize(norm_slice: str, abs_base: int, line_starts: list):
    """[(norm, disp, line)] for word tokens in a normalized slice.

    `abs_base` is the slice's char offset in the whole file; `line_starts` maps
    absolute offset -> 1-based line via bisect.
    """
    out = []
    for m in _RE_TOKEN.finditer(norm_slice):
        disp = m.group(0)
        abs_off = abs_base + m.start()
        line = bisect.bisect_right(line_starts, abs_off)
        out.append((disp.lower(), disp, line))
    return out


# --------------------------------------------------------------------------
# Block model
# --------------------------------------------------------------------------

class Block:
    __slots__ = ("path", "full_slug", "start", "end", "kind", "anchor",
                 "toks_norm", "toks_disp", "toks_line", "raw", "block_kind")

    def __init__(self, path, full_slug, start, end, kind, anchor, toks, raw, block_kind):
        self.path = path
        self.full_slug = full_slug
        self.start = start
        self.end = end
        self.kind = kind                 # "rule" | "pin" | "prose"
        self.anchor = anchor             # "rule-x" | "pin-N" | None
        self.toks_norm = [t[0] for t in toks]
        self.toks_disp = [t[1] for t in toks]
        self.toks_line = [t[2] for t in toks]
        self.raw = raw
        self.block_kind = block_kind     # iter_blocks kind (para/listitem/...)


def _sources_zone_spans(zone_list):
    return [(z["start"], z["end"]) for z in zone_list if z["kind"] == "sources"]


def _inside(spans, off):
    for a, b in spans:
        if a <= off < b:
            return True
    return False


def process_file(path, content_root, is_case_fn):
    """Parse one file -> (sources, proses). Never raises on content quirks."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    rel = os.path.relpath(path, content_root)
    full_slug = rel[:-3] if rel.endswith(".md") else rel
    full_slug = full_slug.replace(os.sep, "/")
    stem = os.path.basename(full_slug)
    is_case = is_case_fn(full_slug)

    zone_list = zones.compute_zones(text, page_stem=stem)
    mask_zones = [z for z in zone_list if z["kind"] in _MASK_ZONE_KINDS]
    masked = zones.mask(text, mask_zones)
    norm = normalize_inplace(masked)
    line_starts = _line_starts(text)
    blocks = zones.iter_blocks(text)
    src_spans = _sources_zone_spans(zone_list)

    sources = []
    proses = []
    source_span_set = set()

    for b in blocks:
        s, e, bk = b["start"], b["end"], b["kind"]
        raw = text[s:e]

        # rule source: a `> ^rule-x` standalone anchor line inside a callout
        m_rule = _RE_RULE_ANCHOR_LINE.search(raw)
        if bk == "blockquote" and m_rule:
            toks = tokenize(norm[s:e], s, line_starts)
            if len(toks) >= SHINGLE_K:
                sources.append(Block(path, full_slug, s, e, "rule",
                                     "rule-" + m_rule.group(1), toks, raw, bk))
                source_span_set.add((s, e))
            continue

        # pin source: end-of-block `^pin-N`, case pages only
        if is_case and bk in ("para", "listitem", "blockquote"):
            m_pin = _RE_PIN_END.search(raw.rstrip())
            if m_pin:
                toks = tokenize(norm[s:e], s, line_starts)
                if len(toks) >= SHINGLE_K:
                    sources.append(Block(path, full_slug, s, e, "pin",
                                         "pin-" + m_pin.group(1), toks, raw, bk))
                source_span_set.add((s, e))  # never a prose block, even if short
                continue

    for b in blocks:
        s, e, bk = b["start"], b["end"], b["kind"]
        if bk not in ("para", "listitem", "blockquote"):
            continue
        if (s, e) in source_span_set:
            continue
        if _inside(src_spans, s):
            continue
        toks = tokenize(norm[s:e], s, line_starts)
        if len(toks) < SHINGLE_K:
            continue
        proses.append(Block(path, full_slug, s, e, "prose", None, toks,
                            text[s:e], bk))

    return sources, proses


# --------------------------------------------------------------------------
# Matching
# --------------------------------------------------------------------------

def build_index(sources):
    """shingle-tuple -> set(source index). k-gram over normalized tokens."""
    index = {}
    for si, src in enumerate(sources):
        t = src.toks_norm
        for i in range(len(t) - SHINGLE_K + 1):
            index.setdefault(tuple(t[i:i + SHINGLE_K]), set()).add(si)
    return index


def longest_common_run(a, b):
    """Longest common CONTIGUOUS token run. -> (length, a_start, b_start)."""
    if len(a) < SHINGLE_K or len(b) < SHINGLE_K:
        return 0, 0, 0
    prev = [0] * (len(b) + 1)
    best = best_ai = best_bj = 0
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                v = prev[j - 1] + 1
                cur[j] = v
                if v > best:
                    best, best_ai, best_bj = v, i, j
        prev = cur
    return best, best_ai - best, best_bj - best


def find_hits(sources, proses):
    """-> list of hit dicts (report schema) sorted by file/line."""
    index = build_index(sources)
    candidates = set()  # (prose_idx, source_idx)
    for pi, p in enumerate(proses):
        t = p.toks_norm
        for i in range(len(t) - SHINGLE_K + 1):
            hit_set = index.get(tuple(t[i:i + SHINGLE_K]))
            if hit_set:
                for si in hit_set:
                    if sources[si].path != p.path:  # FOREIGN only
                        candidates.add((pi, si))

    hits = []
    for pi, si in candidates:
        p, src = proses[pi], sources[si]
        length, a_start, b_start = longest_common_run(p.toks_norm, src.toks_norm)
        if length < SHINGLE_K:
            continue
        snippet = " ".join(p.toks_disp[a_start:a_start + length])
        hits.append({
            "file": p.path,
            "line": p.toks_line[a_start],
            "overlap_tokens": length,
            "source_page": src.full_slug,
            "source_anchor": src.anchor,
            "kind": src.kind,
            "snippet": snippet,
            # extra (not serialized to the report; used by proposals):
            "_prose_start_line": p.toks_line[0],
            "_prose_raw": p.raw,
            "_prose_block_kind": p.block_kind,
            "_prose_total_tokens": len(p.toks_norm),
            "_source_stem": os.path.basename(src.full_slug),
        })

    hits.sort(key=lambda h: (h["file"], h["line"], h["source_page"], h["source_anchor"]))
    return hits


# --------------------------------------------------------------------------
# Corpus sweep
# --------------------------------------------------------------------------

def _default_is_case(full_slug):
    return full_slug.startswith("cases/")


def iter_markdown(content_root):
    for dirpath, _dirs, files in os.walk(content_root):
        for fn in sorted(files):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def sweep(content_root, is_case_fn=_default_is_case, files=None):
    sources, proses, errors = [], [], []
    paths = list(files) if files is not None else list(iter_markdown(content_root))
    for path in paths:
        try:
            s, p = process_file(path, content_root, is_case_fn)
            sources.extend(s)
            proses.extend(p)
        except Exception as exc:  # torn mid-write read, encoding, etc.
            errors.append({"path": path, "error": repr(exc)})
    hits = find_hits(sources, proses)
    stats = {
        "files_scanned": len(paths),
        "rule_sources": sum(1 for s in sources if s.kind == "rule"),
        "pin_sources": sum(1 for s in sources if s.kind == "pin"),
        "prose_blocks": len(proses),
        "hits": len(hits),
        "hits_rule": sum(1 for h in hits if h["kind"] == "rule"),
        "hits_pin": sum(1 for h in hits if h["kind"] == "pin"),
        "read_errors": errors,
        "shingle_k": SHINGLE_K,
        "mask_zone_kinds": list(_MASK_ZONE_KINDS),
    }
    return hits, stats


_REPORT_FIELDS = ("file", "line", "overlap_tokens", "source_page",
                  "source_anchor", "kind", "snippet")


def write_report(hits, stats, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        for h in hits:
            fh.write(json.dumps({k: h[k] for k in _REPORT_FIELDS},
                                ensure_ascii=False) + "\n")
        fh.write(json.dumps({"_summary": stats}, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

_FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "shingles")


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # unit: normalize_inplace is length-preserving and blanks an embed
    src = 'x ![[cases/A#^pin-1]] y [[Foo#^pin-2|Bar]] z [text](http://u) w'
    got = normalize_inplace(src)
    check(len(got) == len(src), "normalize changed length")
    check("cases" not in got and "pin" not in got, "embed not blanked")
    check("Bar" in got and "Foo" not in got, "wikilink display not preserved")
    check("text" in got and "http" not in got, "md-link url not blanked")

    # unit: longest_common_run
    a = "one two three four five six".split() * 5
    b = ["zz"] + a[:30]
    length, a0, b0 = longest_common_run(a, b)
    check(length == 30, f"lcr length {length} != 30")
    check(a[a0] == b[b0], "lcr start misaligned")

    def is_case(slug):
        return os.path.basename(slug) == "case_pin"

    fixture_files = [os.path.join(_FIX, fn) for fn in sorted(os.listdir(_FIX))
                     if fn.endswith(".md")]
    hits, stats = sweep(_FIX, is_case_fn=is_case, files=fixture_files)

    got_pairs = {(os.path.basename(h["file"]), h["kind"], h["source_anchor"])
                 for h in hits}
    want_pairs = {
        ("restate_above.md", "rule", "rule-demo"),   # above-threshold rule restatement
        ("quote_restate.md", "pin", "pin-1"),        # quote-zone: re-typed pinned quote
    }
    check(got_pairs == want_pairs,
          f"hit set mismatch:\n   got  {sorted(got_pairs)}\n   want {sorted(want_pairs)}")

    for h in hits:
        check(h["overlap_tokens"] >= SHINGLE_K,
              f"hit below threshold: {h['file']} {h['overlap_tokens']}")

    # below-threshold, embed-excluded, same-page-excluded all yield NO hit
    for base in ("restate_below.md", "already_embed.md", "same_page.md"):
        check(all(os.path.basename(h["file"]) != base for h in hits),
              f"{base} should produce 0 hits (found one)")

    check(stats["rule_sources"] == 2, f"expected 2 rule sources, got {stats['rule_sources']}")
    check(stats["pin_sources"] == 1, f"expected 1 pin source, got {stats['pin_sources']}")

    if failures:
        print("shingles.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("shingles.py --self-test: PASS "
          "(normalize + lcr units; above/below threshold, embed-excluded, "
          "same-page-excluded, quote-zone handling)")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv):
    if "--self-test" in argv:
        return _self_test()

    content_root = "content"
    out_path = os.path.join("_run", "o2-execute", "s8-shingle-report.jsonl")
    if "--content" in argv:
        content_root = argv[argv.index("--content") + 1]
    if "--out" in argv:
        out_path = argv[argv.index("--out") + 1]

    hits, stats = sweep(content_root)
    write_report(hits, stats, out_path)
    print(json.dumps({"report": out_path, "summary": {
        k: v for k, v in stats.items() if k != "read_errors"}}, ensure_ascii=False))
    if stats["read_errors"]:
        print("read_errors: " + json.dumps(stats["read_errors"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
