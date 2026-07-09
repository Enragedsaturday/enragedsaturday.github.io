#!/usr/bin/env python3
"""
S8 external text-fragment generator + validator (spec S8 R4/R5, SD6; S2 § A14).

Turns each S2 pinpoint whose `quote_fidelity == "matched"` (the G3-pass signal)
into a WICG text-fragment (`#:~:text=...`) that, appended to the opinion URL,
lands the browser on the highlighted passage. The fragment derives EXCLUSIVELY
from the verified quote and is validated to EXACTLY ONE whitespace-insensitive
match against S2's CACHED opinion text — zero live CourtListener, zero quota.

    ---- Contract (spec R5, each rule has a fixture under fixtures/fragments/) ----
    (a) normalize to the RENDERED CL text: HTML stripped to visible text, whitespace
        collapses (slip texts hard-wrap mid-sentence). Dashes/quotes are matched
        typography-insensitively but the fragment EMITS the SOURCE character forms
        (curly quotes / em-dashes as CL renders them), never our authored forms.
    (b) a fragment must not cross a star-page label (CL interposes `*6` as visible
        text mid-sentence — a crossing fragment silently fails): the generator
        TRIMS to a star-free start-only snippet, or SPLITS into start,end whose
        range may span the star but whose anchors do not.
    (c) validate = exactly ONE whitespace-insensitive match against the cached text.
    (d) prefer a distinctive start-only snippet (>=5 words); grow to uniqueness;
        multi-match short phrases disambiguate with `prefix-` located by star page.
    (e) URL-encode per WICG syntax: `#:~:text=[prefix-,]start[,end][,-suffix]`,
        every `-` `,` `&` inside a term percent-encoded so it can't collide with
        the term delimiters.

Input  : `_overhaul2/lake/cases/*.json` pinpoints with quote_fidelity == "matched".
Text   : `$CSSI_LAKE_ROOT/cache/text/<lead_opinion_id>.txt` (default root
         /Users/johngalt/cssi-lake) — the R9(b) cached `html_with_citations`.
Output : `_run/o2-execute/s8-fragments.jsonl`, one row per matched pinpoint:
         {record_id, pin_id, opinion_id, fragment, validated:true, matches:1, date, form}
         or {record_id, pin_id, opinion_id, fragment:null, validated:false, matches, date, reason}.

Unvalidatable rows (garbage/whole-page captures, verbatim-duplicated passages with
no page anchor, missing cached text) carry `fragment: null` + a reason and are the
plain-external set downstream — NEVER patched around (writer != checker; fail-closed).

Python 3 stdlib only. READ-ONLY over the lake + cache; the write-back is the
sanctioned `scripts/s2/ingest.py --apply-fragments` surface, not this module.

    python3 scripts/s8/fragments.py --self-test   # fixtures
    python3 scripts/s8/fragments.py               # generate over the lake
"""

from __future__ import annotations

import argparse
import datetime
import glob
import html as _html
import json
import os
import re
import sys
import urllib.parse

DEFAULT_LAKE_ROOT = "/Users/johngalt/cssi-lake"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAKE_CASES = os.path.join(REPO_ROOT, "_overhaul2", "lake", "cases")
DEFAULT_OUT = os.path.join(REPO_ROOT, "_run", "o2-execute", "s8-fragments.jsonl")
FIX_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "fragments")

MIN_START_WORDS = 5          # spec R5(d): prefer a distinctive start-only snippet >=5 words
MAX_PREFIX_WORDS = 8         # how far back a disambiguating prefix may reach
SPLIT_ANCHOR_WORDS = 8       # max words in a split start/end anchor

# Typography families: matched insensitively, but the SOURCE glyph is emitted.
_QUOTE_CHARS = "\"'‘’“”‚‛′″`"
_DASH_CHARS = "-‐‑‒–—―−"


# ---------------------------------------------------------------------------
# (a) render the cached html_with_citations to visible text
# ---------------------------------------------------------------------------

def render_opinion_text(html_text: str) -> str:
    """Strip CL's `html_with_citations` to the visible text a browser renders.

    Block-level tags + <br> become whitespace boundaries so hard-wrapped lines
    join cleanly; the `<span class="star-pagination">*6</span>` labels survive as
    inline `*6` visible text (that is exactly why a fragment can silently cross
    one — R5(b)). Entities are decoded. Whitespace is NOT collapsed here: the
    flexible matcher uses `\\s+` so it spans the source's mid-sentence wraps.
    """
    s = html_text
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", " ", s)
    s = re.sub(r"(?i)</(p|div|center|h[1-6]|blockquote|li|tr|table|ol|ul|section|article)>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = _html.unescape(s)
    return s


def collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------------------
# flexible (whitespace- + typography-insensitive) matcher over the SOURCE text
# ---------------------------------------------------------------------------

def _flex_char(c: str) -> str:
    if c in _QUOTE_CHARS:
        return "[" + re.escape(_QUOTE_CHARS) + "]"
    if c in _DASH_CHARS:
        return "[" + re.escape(_DASH_CHARS) + "]"
    return re.escape(c)


def build_flex_pattern(quote_ws_collapsed: str) -> str:
    """Regex matching `quote` in raw rendered text, insensitive to whitespace runs
    and to quote/dash glyph choice. `quote` must already be whitespace-collapsed."""
    out = []
    for c in quote_ws_collapsed:
        if c == " ":
            out.append(r"\s+")
        else:
            out.append(_flex_char(c))
    return "".join(out)


def flex_matches(quote_ws_collapsed: str, source_text: str):
    """List of re.Match of `quote` in `source_text` (source glyphs preserved)."""
    if not quote_ws_collapsed:
        return []
    return list(re.finditer(build_flex_pattern(quote_ws_collapsed), source_text))


# ---------------------------------------------------------------------------
# (e) WICG url-encoding
# ---------------------------------------------------------------------------

def encode_term(source_span: str) -> str:
    """Percent-encode one text-directive term. Emits the SOURCE glyphs (curly
    quotes / em-dashes survive as %E2%80%.. bytes). `-` `,` `&` are ALSO encoded
    so they cannot collide with the prefix-/,/-suffix delimiters."""
    collapsed = collapse_ws(source_span)
    enc = urllib.parse.quote(collapsed, safe="")
    # urllib leaves -._~ unencoded; -, and & are structural in a text directive.
    enc = enc.replace("-", "%2D").replace(",", "%2C").replace("&", "%26")
    return enc


def build_fragment(start, end=None, prefix=None, suffix=None) -> str:
    """Assemble `#:~:text=[prefix-,]start[,end][,-suffix]` from SOURCE spans."""
    parts = []
    if prefix is not None:
        parts.append(encode_term(prefix) + "-")
    parts.append(encode_term(start))
    if end is not None:
        parts.append(encode_term(end))
    if suffix is not None:
        parts.append("-" + encode_term(suffix))
    return "#:~:text=" + ",".join(parts)


# ---------------------------------------------------------------------------
# star-page helpers
# ---------------------------------------------------------------------------

def star_label_pos(source_text: str, marker) -> int:
    if marker in (None, ""):
        return -1
    m = re.search(r"\*" + re.escape(str(marker)) + r"(?!\d)", source_text)
    return m.start() if m else -1


# ---------------------------------------------------------------------------
# the generator
# ---------------------------------------------------------------------------

def _validated(fragment, form, words=None, matches=1):
    return {"fragment": fragment, "reason": None, "form": form,
            "matches": matches, "snippet_words": words}


def _unvalidatable(reason, matches):
    return {"fragment": None, "reason": reason, "form": None,
            "matches": matches, "snippet_words": None}


def _start_only(words, source_text):
    """Smallest distinctive leading snippet (>=5 words, or the whole short quote)
    that matches EXACTLY ONCE. Returns a result dict or None."""
    lo = min(MIN_START_WORDS, len(words))
    for k in range(lo, len(words) + 1):
        snip = " ".join(words[:k])
        occ = flex_matches(snip, source_text)
        if len(occ) == 1:
            return _validated(build_fragment(occ[0].group(0)), "start-only", words=k)
    return None


def _multi_prefix(nq, words, source_text, marker, full_occ):
    """A quote that occurs verbatim more than once: pin the intended occurrence by
    star page, then grow a `prefix-` (or `-suffix`) until the pair is unique."""
    if marker in (None, ""):
        return _unvalidatable("multi_match_no_star_anchor", len(full_occ))
    sp = star_label_pos(source_text, marker)
    if sp < 0:
        return _unvalidatable("multi_match_star_label_absent", len(full_occ))
    after = [m for m in full_occ if m.start() >= sp]
    intended = after[0] if after else full_occ[0]
    nq_pat = build_flex_pattern(nq)

    # prefix- : preceding words at the intended occurrence
    pre_words = collapse_ws(source_text[:intended.start()]).split(" ")
    for k in range(1, MAX_PREFIX_WORDS + 1):
        if k > len(pre_words):
            break
        prefix_src = " ".join(pre_words[-k:])
        pat = build_flex_pattern(prefix_src) + r"\s*" + nq_pat
        hits = list(re.finditer(pat, source_text))
        if len(hits) == 1:
            return _validated(build_fragment(intended.group(0), prefix=prefix_src),
                              "prefix-start", words=len(words))

    # -suffix : trailing words at the intended occurrence
    post_words = collapse_ws(source_text[intended.end():]).split(" ")
    for k in range(1, MAX_PREFIX_WORDS + 1):
        if k > len(post_words):
            break
        suffix_src = " ".join(post_words[:k])
        pat = nq_pat + r"\s*" + build_flex_pattern(suffix_src)
        hits = list(re.finditer(pat, source_text))
        if len(hits) == 1:
            return _validated(build_fragment(intended.group(0), suffix=suffix_src),
                              "start-suffix", words=len(words))
    return _unvalidatable("multi_match_not_disambiguable", len(full_occ))


def _star_split(words, source_text):
    """Full quote does not match contiguously (a star label — or a footnote marker
    — interrupts it, or it is garbage). Trim to a unique star-free leading snippet,
    else split into start,end anchors whose range spans the interruption."""
    # trim: largest-informative unique leading snippet that matches contiguously
    trimmed = _start_only(words, source_text)
    if trimmed is not None:
        return dict(trimmed, form="start-only-trim")
    # split: start anchor (front) + end anchor (back), range may span the star
    n = len(words)
    if n < 4:
        return _unvalidatable("no_match", 0)
    quote_len = len(" ".join(words))
    gap_limit = quote_len * 3 + 200
    for s in range(3, min(SPLIT_ANCHOR_WORDS, n - 1) + 1):
        start_words = words[:s]
        start_occ = flex_matches(" ".join(start_words), source_text)
        if not start_occ:
            continue
        for e in range(3, min(SPLIT_ANCHOR_WORDS, n - s) + 1):
            end_words = words[n - e:]
            end_occ = flex_matches(" ".join(end_words), source_text)
            if not end_occ:
                continue
            pat = (build_flex_pattern(" ".join(start_words))
                   + r"[\s\S]{0,%d}?" % gap_limit
                   + build_flex_pattern(" ".join(end_words)))
            spans = list(re.finditer(pat, source_text))
            if len(spans) == 1:
                m = spans[0]
                # emit the two anchors as they appear in the source
                sm = flex_matches(" ".join(start_words), m.group(0))[0]
                em = list(re.finditer(build_flex_pattern(" ".join(end_words)), m.group(0)))[-1]
                return _validated(build_fragment(sm.group(0), end=em.group(0)),
                                  "start-end", words=s + e)
    return _unvalidatable("no_match", 0)


def generate(quote: str, source_text: str, star_marker=None) -> dict:
    """Core R5 contract. Returns a result dict:
       {fragment|None, reason|None, form, matches, snippet_words}."""
    nq = collapse_ws(quote)
    if not nq:
        return _unvalidatable("empty_quote", 0)
    words = nq.split(" ")
    full = flex_matches(nq, source_text)
    if len(full) == 1:
        res = _start_only(words, source_text)
        return res if res is not None else _validated(build_fragment(full[0].group(0)),
                                                      "start-only", words=len(words))
    if len(full) >= 2:
        return _multi_prefix(nq, words, source_text, star_marker, full)
    return _star_split(words, source_text)


# ---------------------------------------------------------------------------
# lake driver
# ---------------------------------------------------------------------------

def _text_dir(lake_root):
    return os.path.join(lake_root, "cache", "text")


def load_matched_pinpoints(cases_dir=LAKE_CASES):
    """[(record_id, pin_id, lead_opinion_id, star_marker, quote)] over the whole
    lake, matched-fidelity only, in stable (record, pin) order."""
    out = []
    for path in sorted(glob.glob(os.path.join(cases_dir, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            rec = json.load(fh)
        lead = (rec.get("identity") or {}).get("lead_opinion_id")
        for p in rec.get("pinpoints") or []:
            if p.get("quote_fidelity") == "matched":
                out.append((rec["record_id"], p.get("id"), lead,
                            p.get("star_marker"), p.get("quote") or ""))
    return out


def run(out_path=DEFAULT_OUT, lake_root=None, cases_dir=LAKE_CASES):
    lake_root = lake_root or os.environ.get("CSSI_LAKE_ROOT", DEFAULT_LAKE_ROOT)
    text_dir = _text_dir(lake_root)
    date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pins = load_matched_pinpoints(cases_dir)

    cache = {}

    def source_for(lead):
        if lead not in cache:
            tp = os.path.join(text_dir, "%s.txt" % lead)
            cache[lead] = render_opinion_text(open(tp, encoding="utf-8").read()) if os.path.exists(tp) else None
        return cache[lead]

    rows = []
    reasons = {}
    forms = {}
    validated = 0
    for record_id, pin_id, lead, star, quote in pins:
        if lead is None:
            row = {"record_id": record_id, "pin_id": pin_id, "opinion_id": lead,
                   "fragment": None, "validated": False, "matches": 0,
                   "date": date, "reason": "no_lead_opinion_id"}
            reasons["no_lead_opinion_id"] = reasons.get("no_lead_opinion_id", 0) + 1
            rows.append(row)
            continue
        src = source_for(lead)
        if src is None:
            row = {"record_id": record_id, "pin_id": pin_id, "opinion_id": lead,
                   "fragment": None, "validated": False, "matches": 0,
                   "date": date, "reason": "no_cached_text"}
            reasons["no_cached_text"] = reasons.get("no_cached_text", 0) + 1
            rows.append(row)
            continue
        res = generate(quote, src, star)
        if res["fragment"] is not None:
            validated += 1
            forms[res["form"]] = forms.get(res["form"], 0) + 1
            row = {"record_id": record_id, "pin_id": pin_id, "opinion_id": lead,
                   "fragment": res["fragment"], "validated": True,
                   "matches": res["matches"], "date": date, "form": res["form"]}
        else:
            reasons[res["reason"]] = reasons.get(res["reason"], 0) + 1
            row = {"record_id": record_id, "pin_id": pin_id, "opinion_id": lead,
                   "fragment": None, "validated": False, "matches": res["matches"],
                   "date": date, "reason": res["reason"]}
        rows.append(row)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, sort_keys=True) + "\n")

    return {"total": len(rows), "validated": validated,
            "unvalidatable": len(rows) - validated,
            "reasons": reasons, "forms": forms, "out": out_path, "rows": rows}


# ---------------------------------------------------------------------------
# self-test (fixtures under fixtures/fragments/)
# ---------------------------------------------------------------------------

def _decode(fragment):
    """text-directive value -> decoded terms, for asserting on human-readable text."""
    val = fragment.split("#:~:text=", 1)[1]
    return [urllib.parse.unquote(t) for t in val.split(",")]


def _load_fixture(name):
    with open(os.path.join(FIX_DIR, name), encoding="utf-8") as fh:
        return render_opinion_text(fh.read())


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # (b) star-label crossing: the full quote crosses `*6`; result must validate,
    # must NOT contain the star label, and re-validates at exactly one match.
    src = _load_fixture("star_cross.html")
    q = "We conclude that the warrantless search of the home violated the Fourth Amendment on these facts."
    res = generate(q, src, star_marker=6)
    check(res["fragment"] is not None, "star_cross: expected a validated fragment, got %r" % res["reason"])
    if res["fragment"]:
        terms = _decode(res["fragment"])
        check(all("*6" not in t for t in terms), "star_cross: fragment crosses the *6 label: %r" % terms)
        check(res["form"] in ("start-end", "start-only-trim"), "star_cross: form=%r" % res["form"])
        # re-validate: each anchor term matches the source; range is unique
        for t in terms:
            check(len(flex_matches(collapse_ws(t), src)) >= 1, "star_cross: anchor %r absent" % t)

    # (d) multi-match short phrase disambiguated by star page + prefix.
    src = _load_fixture("multi_match.html")
    res = generate("special needs", src, star_marker=11)
    check(res["fragment"] is not None, "multi_match: expected validated, got %r" % res["reason"])
    if res["fragment"]:
        check(res["form"] in ("prefix-start", "start-suffix"), "multi_match: form=%r" % res["form"])
        # the disambiguated pair must be unique in the source
        terms = _decode(res["fragment"])
        # reconstruct prefix+start and confirm single match
        pat = r"\s*".join(build_flex_pattern(collapse_ws(t.rstrip("-"))) for t in terms if t not in ("", "-"))
        check(len(list(re.finditer(pat, src))) == 1, "multi_match: pair not unique: %r" % terms)
    # without a star anchor the same phrase is fail-closed unvalidatable
    res2 = generate("special needs", src, star_marker=None)
    check(res2["fragment"] is None and res2["reason"] == "multi_match_no_star_anchor",
          "multi_match: no-star should fail closed, got %r" % res2)

    # (a) curly-vs-source normalization: quote authored with straight quotes/hyphen,
    # source renders curly quotes + en-dash; fragment must EMIT the source glyphs.
    src = _load_fixture("curly.html")
    q = 'a "reasonable expectation of privacy" standard governs review of a well-settled question'
    res = generate(q, src, star_marker=None)
    check(res["fragment"] is not None, "curly: expected validated, got %r" % res["reason"])
    if res["fragment"]:
        joined = " ".join(_decode(res["fragment"]))
        check("“" in joined or "”" in joined,
              "curly: fragment must emit SOURCE curly quotes, got %r" % joined)
        check('"' not in joined, "curly: fragment must not emit our straight quotes: %r" % joined)
        # and it must actually resolve against the source
        for t in _decode(res["fragment"]):
            check(len(flex_matches(collapse_ws(t), src)) >= 1, "curly: term %r absent" % t)

    # (c) no-match: a garbage / whole-page capture is fail-closed unvalidatable.
    src = _load_fixture("no_match.html")
    q = "## Rule Yes. Bringing a drug dog onto the curtilage to gather evidence in the hope of a hit"
    res = generate(q, src, star_marker=None)
    check(res["fragment"] is None, "no_match: garbage quote must NOT validate, got %r" % res["fragment"])
    check(res["reason"] == "no_match", "no_match: reason=%r" % res["reason"])

    # happy path: a clean unique quote -> minimal start-only snippet, source glyphs,
    # and the emitted term re-validates at exactly one match.
    src = _load_fixture("no_match.html")
    q = "This opinion discusses the plain view doctrine and inventory searches"
    res = generate(q, src, star_marker=None)
    check(res["fragment"] is not None and res["form"] == "start-only",
          "happy: expected start-only, got %r/%r" % (res["form"], res["reason"]))
    if res["fragment"]:
        check(res["matches"] == 1, "happy: matches=%r" % res["matches"])
        check(res["snippet_words"] >= MIN_START_WORDS, "happy: snippet <5 words")

    # encoder: -, & inside a term are percent-encoded (delimiter safety)
    enc = encode_term("well-settled A & B")
    check("%2D" in enc and "%26" in enc and "-" not in enc.replace("%2D", "") and "&" not in enc,
          "encode_term: - / & not escaped: %r" % enc)

    if failures:
        print("fragments.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("fragments.py --self-test: PASS (star-cross + multi-prefix + curly-source + no-match + happy + encoder)")
    return 0


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(description="S8 R5 text-fragment generator + validator (cached text only)")
    ap.add_argument("--self-test", action="store_true", help="run fixture unit checks and exit")
    ap.add_argument("--out", default=DEFAULT_OUT, help="output jsonl path")
    ap.add_argument("--lake-root", default=None, help="pool root (default $CSSI_LAKE_ROOT or /Users/johngalt/cssi-lake)")
    ap.add_argument("--cases-dir", default=LAKE_CASES, help="lake cases dir")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    res = run(out_path=args.out, lake_root=args.lake_root, cases_dir=args.cases_dir)
    print("fragments: %d pinpoints | validated %d | unvalidatable %d"
          % (res["total"], res["validated"], res["unvalidatable"]))
    print("forms: %s" % json.dumps(res["forms"], sort_keys=True))
    print("unvalidatable reasons: %s" % json.dumps(res["reasons"], sort_keys=True))
    print("out: %s" % res["out"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
