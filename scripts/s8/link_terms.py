#!/usr/bin/env python3
"""
S8 term-link pass (spec S8 R7 — four-way routing at every occurrence, D1).

Reads the routing columns of the S1 A3 term register
(`scripts/lint/term-register.yml`, schema term-register.v2) and links every
occurrence of every routed term OUTSIDE the R2 exemption zones:

    route: page      -> [[Doctrine Page|surface]]   (pipe preserves inflection;
                        a bare page whose surface == target renders [[Page]])
    route: glossary  -> [[Common Legal Terms#anchor|surface]]
    route: citing    -> [[Reading and Citing Cases#anchor|surface]]
    route: skip      -> never linked

Contract with the frozen zone catalog (`scripts/s8/zones.py`):
  * `zones.compute_zones(text, page_stem=…)` + `zones.mask(…)` blank every R2
    zone (headings, code, quotes, citations, Sources, frontmatter, comments,
    the page's own title, Case cells). The linker additionally masks existing
    [[wikilinks]] / [md](links) / `inline code` so the pass runs AFTER the
    case-mention pass without ever re-linking inside an existing link (overlap
    rule) — ordering therefore affects COUNTS only, never correctness.
  * `zones.iter_blocks(text)` gives table spans so a display pipe injected into
    a table cell is escaped `\\|` (R11 / NUM-02).

Self-page rule (zone g, generalized): a term never links on its target page —
glossary terms never link ON Common Legal Terms, a page-routed term never links
on its own doctrine page (compared by resolved FILE PATH, so index-hub stems
that collide across sections are handled correctly).

Longest-match wins when routed terms overlap (search incident to arrest > arrest).

Anchor verification (fail loud): every route target must resolve to a page, and
every #anchor must exist on it (Quartz slug convention via _common.slugify). A
register row whose target/anchor is DEAD is refused corpus-wide and reported —
never linked.

Emits the R12 terms-section source `_run/o2-execute/s8-term-rows.jsonl`
(per-page register-coverage counts + per-link rows).

Modes:  (default) dry-run report + jsonl   ·   --write   ·   --self-test
Constraints: Python 3 stdlib only. Zero CourtListener. Touches only content/**.md
(link-form edits) + scripts/s8/** + the _run/o2-execute artifact.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

_S8 = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_S8))
sys.path.insert(0, _S8)
sys.path.insert(0, os.path.join(_REPO, "scripts", "lint"))
import zones  # noqa: E402  (local module, same dir)
import _common as c  # noqa: E402  (sanctioned corpus slugger + yaml subset)

CONTENT = os.path.join(_REPO, "content")
RUN_DIR = os.path.join(_REPO, "_run", "o2-execute")
JSONL = os.path.join(RUN_DIR, "s8-term-rows.jsonl")
REGISTER = os.path.join(_REPO, "scripts", "lint", "term-register.yml")

LANE = "o2-opus-xhigh"
MODEL = "claude-opus-4-8"

ROUTES = ("page", "glossary", "citing", "skip")


# --------------------------------------------------------------------------
# register
# --------------------------------------------------------------------------

def _truth(v):
    return v is True or (isinstance(v, str) and v.strip().lower() == "true")


def _surface_regex(surface: str) -> re.Pattern:
    """Word-bounded, case-insensitive, whitespace-tolerant literal matcher.

    Internal whitespace tolerates runs (wrapped prose); boundaries reject
    adjacent alphanumerics so 'arrest' never fires inside 'arrests' and
    'pat-down' never fires inside 'pat-downs' (inflections go through `match`)."""
    words = [re.escape(w) for w in surface.split()]
    body = r"\s+".join(words) if words else re.escape(surface)
    return re.compile(r"(?<![A-Za-z0-9])" + body + r"(?![A-Za-z0-9])",
                      re.IGNORECASE)


class Term:
    __slots__ = ("canonical", "route", "target", "page_part", "anchor",
                 "eponym", "surfaces", "regexes", "dead")

    def __init__(self, canonical, route, target, eponym, surfaces):
        self.canonical = canonical
        self.route = route
        self.target = target
        self.eponym = eponym
        self.surfaces = surfaces
        self.regexes = [(_surface_regex(s), s) for s in surfaces]
        self.dead = None  # set to a reason string if target/anchor is dead
        if target:
            page, _, anchor = target.partition("#")
            self.page_part = page.strip()
            self.anchor = anchor.strip()
        else:
            self.page_part = ""
            self.anchor = ""


def load_register(path=REGISTER):
    text = c.read_text(path)
    data = c.parse_yaml_subset(text.split("\n"))
    rows = data.get("terms") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        raise ValueError("term register: no `terms:` list")
    terms = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        canonical = row.get("canonical")
        route = row.get("route")
        if not isinstance(canonical, str) or not canonical.strip():
            continue
        canonical = canonical.strip()
        surfaces = [canonical]
        m = row.get("match")
        if isinstance(m, str):
            m = [m]
        if isinstance(m, list):
            for s in m:
                if isinstance(s, str) and s.strip():
                    surfaces.append(s.strip())
        terms.append(Term(canonical, route, row.get("target"),
                          _truth(row.get("eponym")), surfaces))
    return terms, data.get("schema")


# --------------------------------------------------------------------------
# path-keyed page index (resolve target -> file path; anchors per path)
# --------------------------------------------------------------------------

class PageIndex:
    def __init__(self):
        self.name2paths = {}   # norm(name) -> set(relpath)
        self.slug2paths = {}   # slug(stem) -> set(relpath)
        self.anchors = {}      # relpath -> set(slug + ^block)

    def add(self, relpath, names, stem, anchors):
        for n in names:
            if n:
                self.name2paths.setdefault(c.CorpusIndex.norm(n), set()).add(relpath)
        self.slug2paths.setdefault(c.slugify(stem), set()).add(relpath)
        self.anchors[relpath] = set(anchors)

    def resolve_paths(self, page_name):
        if not page_name:
            return set()
        cand = page_name.strip()
        base = cand.split("/")[-1]
        for key in (cand, base):
            n = c.CorpusIndex.norm(key)
            if n in self.name2paths:
                return self.name2paths[n]
        return self.slug2paths.get(c.slugify(base), set())

    def has_anchor(self, relpath, anchor):
        anchors = self.anchors.get(relpath)
        if not anchors:
            return False
        a = anchor.strip()
        if a.startswith("^"):
            return a.lower() in anchors
        return c.slugify(a) in anchors


def build_page_index(content_root=CONTENT):
    idx = PageIndex()
    import glob as _glob
    for path in sorted(_glob.glob(os.path.join(content_root, "**", "*.md"),
                                  recursive=True)):
        rel = os.path.relpath(path, content_root)
        stem = os.path.splitext(os.path.basename(path))[0]
        try:
            text = c.read_text(path)
        except OSError:
            continue
        fm, body, _ = c.split_frontmatter(text)
        names = [stem]
        for key in ("title", "topic"):
            v = fm.get(key)
            if isinstance(v, str) and v.strip():
                names.append(v)
        al = fm.get("aliases")
        if isinstance(al, str):
            al = [al]
        if isinstance(al, list):
            names.extend([a for a in al if isinstance(a, str)])
        anchors = set()
        for _, _, txt in c.iter_headings(body.split("\n")):
            anchors.add(c.slugify(txt))
        for m in re.finditer(r"(?:^|\s)(\^[A-Za-z0-9][A-Za-z0-9-]*)\s*$",
                             body, flags=re.MULTILINE):
            anchors.add(m.group(1).lower())
        idx.add(rel, names, stem, anchors)
    return idx


def validate_register(terms, idx):
    """Mark each non-skip term dead if its target page / anchor does not resolve.
    Returns list of dead findings [{canonical, route, target, reason}]."""
    dead = []
    for t in terms:
        if t.route not in ("page", "glossary", "citing"):
            continue
        paths = idx.resolve_paths(t.page_part)
        if not paths:
            t.dead = "target page does not resolve: [[%s]]" % t.page_part
        elif t.anchor and not any(idx.has_anchor(p, t.anchor) for p in paths):
            t.dead = "dead anchor: #%s not found on [[%s]]" % (t.anchor, t.page_part)
        if t.dead:
            dead.append({"canonical": t.canonical, "route": t.route,
                        "target": t.target, "reason": t.dead})
    return dead


# --------------------------------------------------------------------------
# masking + planning
# --------------------------------------------------------------------------

def _blank(m):
    return re.sub(r"[^\n]", " ", m.group(0))


def _apply_full_mask(text, zones_list):
    """Zone mask (R2) plus existing wikilinks / md links / inline code — all
    offset-preserving so a term match in the mask maps 1:1 to `text`."""
    masked = zones.mask(text, zones_list)
    masked = c.INLINE_CODE_RE.sub(_blank, masked)
    masked = c.WIKILINK_RE.sub(_blank, masked)
    masked = c.MDLINK_RE.sub(_blank, masked)
    return masked


def combined_mask(text, page_stem):
    return _apply_full_mask(text, zones.compute_zones(text, page_stem=page_stem))


def _table_spans(text):
    return [(b["start"], b["end"]) for b in zones.iter_blocks(text)
            if b["kind"] == "table"]


# A physical line the sibling pincite/fragment lane OWNS: it carries a pincite
# citation string, an `^pin-N` block anchor, or a `[[Case#^pin-N]]` deep link.
# The coordination rule (orchestrator, 2026-07-09) forbids the term pass from
# TOUCHING such a line while that lane is live — even editing an unrelated term
# span on it churns the whole line and races the pincite writer. Guarded ON by
# default; `--allow-pincite-lines` disables (only on a de-conflicted re-run).
_PIN_TOKEN = re.compile(r"\^pin-[0-9A-Za-z]+")


def _protected_line_ranges(text, zones_list):
    """Return sorted [(start,end)] char spans of every physical line that carries
    a citation zone, an ^pin-N anchor, or a #^pin-N deep link."""
    prot_lines = set()
    for z in zones_list:
        if z["kind"] == "citation":
            a = text.count("\n", 0, z["start"])
            b = text.count("\n", 0, max(z["start"], z["end"] - 1))
            for ln in range(a, b + 1):
                prot_lines.add(ln)
    for m in _PIN_TOKEN.finditer(text):
        prot_lines.add(text.count("\n", 0, m.start()))
    if not prot_lines:
        return []
    line_spans = zones._lines(text)  # [(start,end)] per physical line
    return [line_spans[i] for i in sorted(prot_lines) if i < len(line_spans)]


def _line_no(text, off):
    return text.count("\n", 0, off) + 1


def build_link_plan(text, page_relpath, terms, idx, page_stem=None,
                    protect_pincite_lines=True):
    """Return (edits, records).

    edits   : [{start, end, repl, ...}] to splice into `text`.
    records : [{line, term, route, target, surface, action}] — action in
              {link, self-skip, skip-pincite-line}.
    """
    if page_stem is None:
        page_stem = os.path.splitext(os.path.basename(page_relpath))[0]
    zlist = zones.compute_zones(text, page_stem=page_stem)
    masked = _apply_full_mask(text, zlist)
    tspans = _table_spans(text)
    prot = _protected_line_ranges(text, zlist) if protect_pincite_lines else []

    # 1) gather candidates from every LIVE, non-skip term
    cands = []  # (start, end, term, surface)
    for t in terms:
        if t.route == "skip" or t.dead:
            continue
        for rx, _s in t.regexes:
            for m in rx.finditer(masked):
                cands.append((m.start(), m.end(), t))

    # 2) longest-match wins: leftmost, then longest, greedy non-overlap
    cands.sort(key=lambda x: (x[0], -(x[1] - x[0])))
    edits, records = [], []
    last_end = -1
    for start, end, t in cands:
        if start < last_end:
            continue  # overlaps an already-accepted (longer/earlier) match
        surface = text[start:end]
        # sibling-lane guard: never touch a pincite / ^pin- / deep-link line
        if prot and any(not (end <= a or b <= start) for (a, b) in prot):
            records.append({"line": _line_no(text, start), "term": t.canonical,
                            "route": t.route, "target": t.target,
                            "surface": surface, "action": "skip-pincite-line"})
            last_end = end
            continue
        # self-page guard (zone g, generalized by resolved path)
        paths = idx.resolve_paths(t.page_part)
        if page_relpath in paths:
            records.append({"line": _line_no(text, start), "term": t.canonical,
                            "route": t.route, "target": t.target,
                            "surface": surface, "action": "self-skip"})
            last_end = end
            continue
        # build link
        in_table = any(a <= start and end <= b for (a, b) in tspans)
        sep = "\\|" if in_table else "|"
        if t.anchor:
            link = "[[%s#%s%s%s]]" % (t.page_part, t.anchor, sep, surface)
        else:
            if surface == t.page_part:
                link = "[[%s]]" % t.page_part
            else:
                link = "[[%s%s%s]]" % (t.page_part, sep, surface)
        edits.append({"start": start, "end": end, "repl": link})
        records.append({"line": _line_no(text, start), "term": t.canonical,
                        "route": t.route, "target": t.target,
                        "surface": surface, "action": "link",
                        "start": start, "end": end, "repl": link})
        last_end = end
    return edits, records


def apply_edits(text, edits):
    for e in sorted(edits, key=lambda e: e["start"], reverse=True):
        text = text[:e["start"]] + e["repl"] + text[e["end"]:]
    return text


# --------------------------------------------------------------------------
# corpus walk
# --------------------------------------------------------------------------

def _md_files():
    for root, _dirs, files in os.walk(CONTENT):
        for fn in sorted(files):
            if fn.endswith(".md"):
                yield os.path.join(root, fn)


def _class_of(rel):
    if rel.startswith("cases" + os.sep) or rel == "cases":
        return "case"
    if os.path.basename(rel) == "flashcards.md":
        return "flashcards"
    if os.path.basename(rel) == "index.md":
        return "index"
    return "prose"


def run(write=False, sample=10, protect_pincite_lines=True):
    terms, schema = load_register()
    idx = build_page_index()
    dead = validate_register(terms, idx)

    by_route = {"page": 0, "glossary": 0, "citing": 0}
    by_class = {}
    by_term = {}
    self_skips = 0
    pincite_skips = 0
    files_scanned = 0
    files_touched = 0
    all_records = []      # (rel, record) for links only
    page_rows = []        # per-page coverage
    samples = []

    for path in _md_files():
        rel = os.path.relpath(path, CONTENT)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        files_scanned += 1
        edits, records = build_link_plan(text, rel, terms, idx,
                                         protect_pincite_lines=protect_pincite_lines)
        links = [r for r in records if r["action"] == "link"]
        skips = [r for r in records if r["action"] == "self-skip"]
        pincite_skips += sum(1 for r in records if r["action"] == "skip-pincite-line")
        self_skips += len(skips)
        if not links and not skips:
            continue
        cls = _class_of(rel)
        pr = {"page": 0, "glossary": 0, "citing": 0}
        for r in links:
            by_route[r["route"]] += 1
            pr[r["route"]] += 1
            by_term[r["term"]] = by_term.get(r["term"], 0) + 1
            all_records.append((rel, r))
        by_class[cls] = by_class.get(cls, 0) + len(links)
        if links:
            page_rows.append({"file": rel, "class": cls, "links": len(links),
                              "by_route": pr, "self_skips": len(skips)})
        if edits:
            files_touched += 1
            new_text = apply_edits(text, edits)
            if write:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
            if len(samples) < sample and links:
                samples.append((rel, links[0], text))

    total = sum(by_route.values())
    _emit_jsonl(write, schema, files_scanned, files_touched, total, by_route,
                by_class, by_term, self_skips, pincite_skips, dead, all_records,
                page_rows, protect_pincite_lines)

    # ---- report ----
    print("=== S8 term link pass (%s) ===" % ("WRITE" if write else "DRY-RUN"))
    print("register schema : %s   (%d terms)" % (schema, len(terms)))
    print("pincite-line guard: %s" % ("ON (skip sibling-lane lines)"
                                      if protect_pincite_lines else "OFF"))
    print("files scanned   : %d   (files with >=1 link: %d)" % (files_scanned, files_touched))
    print("links planned   : %d" % total)
    for r in ("page", "glossary", "citing"):
        print("  route:%-9s: %d" % (r, by_route[r]))
    print("self-skips (zone g): %d" % self_skips)
    print("pincite/pin/deep-link-line skips: %d" % pincite_skips)
    print("by file-class   : %s" % json.dumps(by_class))
    print("dead register targets (refused, NOT linked): %d" % len(dead))
    for d in dead:
        print("  ! [%s] route:%s target=%s — %s"
              % (d["canonical"], d["route"], d["target"], d["reason"]))
    print("\n--- links per term (desc) ---")
    for term, n in sorted(by_term.items(), key=lambda kv: (-kv[1], kv[0])):
        print("  %5d  %s" % (n, term))
    _print_samples(samples, sample)
    print("\nWROTE: %s" % os.path.relpath(JSONL, _REPO))
    if not write:
        print("(dry-run — content not modified; pass --write to apply)")
    return total, dead


def _print_samples(samples, n, pad=60):
    """Show a window centered on the exact edit offset (before / after)."""
    print("\n--- %d sample diffs (window around the edit) ---" % min(n, len(samples)))
    for rel, rec, old in samples[:n]:
        s, e = rec["start"], rec["end"]
        ls = old.rfind("\n", 0, s) + 1
        le = old.find("\n", e)
        if le == -1:
            le = len(old)
        w0 = max(ls, s - pad)
        w1 = min(le, e + pad)
        pre = old[w0:s]
        post = old[e:w1]
        before = old[w0:w1]
        after = pre + rec["repl"] + post
        lead = "…" if w0 > ls else ""
        tail = "…" if w1 < le else ""
        print("  %s:%d  [%s -> route:%s]" % (rel, rec["line"], rec["term"], rec["route"]))
        print("    -   %s%s%s" % (lead, before.replace("\n", " "), tail))
        print("    +   %s%s%s" % (lead, after.replace("\n", " "), tail))


def _emit_jsonl(write, schema, files_scanned, files_touched, total, by_route,
                by_class, by_term, self_skips, pincite_skips, dead, all_records,
                page_rows, protect_pincite_lines):
    os.makedirs(RUN_DIR, exist_ok=True)
    header = {
        "kind": "header",
        "lane": LANE, "model": MODEL, "tool": "link_terms",
        "date": datetime.date.today().isoformat(),
        "mode": "write" if write else "dry-run",
        "register_schema": schema,
        "pincite_line_guard": protect_pincite_lines,
        "counts": {
            "files_scanned": files_scanned,
            "files_touched": files_touched,
            "links": total,
            "by_route": by_route,
            "by_class": by_class,
            "by_term": by_term,
            "self_skips": self_skips,
            "pincite_line_skips": pincite_skips,
            "dead_targets": len(dead),
        },
    }
    with open(JSONL, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(header, ensure_ascii=False) + "\n")
        for d in dead:
            fh.write(json.dumps({"kind": "dead-target", **d}, ensure_ascii=False) + "\n")
        for pr in page_rows:
            fh.write(json.dumps({"kind": "page", **pr}, ensure_ascii=False) + "\n")
        for rel, r in all_records:
            fh.write(json.dumps({"kind": "link", "file": rel, "line": r["line"],
                                 "term": r["term"], "route": r["route"],
                                 "target": r["target"], "surface": r["surface"]},
                                ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# self-test  (hermetic — mini register + mini index, no live corpus)
# --------------------------------------------------------------------------

_FIX = os.path.join(_S8, "fixtures", "terms")


def _load(name):
    with open(os.path.join(_FIX, name), encoding="utf-8") as fh:
        return fh.read()


def _mini_terms():
    def T(canon, route, target, match=None, eponym=False):
        surfaces = [canon] + (match or [])
        return Term(canon, route, target, eponym, surfaces)
    return [
        T("curtilage", "page", "Curtilage"),
        T("de novo", "glossary", "Common Legal Terms#de-novo"),
        T("search incident to arrest", "page", "Search Incident to Arrest"),
        T("arrest", "page", "Arrest"),                     # overlaps SITA -> loses
        T("deadterm", "glossary", "Common Legal Terms#does-not-exist"),
        T("skipword", "skip", None),
    ]


def _mini_index():
    idx = PageIndex()
    idx.add("Curtilage.md", ["Curtilage"], "Curtilage", set())
    idx.add("Arrest.md", ["Arrest"], "Arrest", set())
    idx.add("SITA.md", ["Search Incident to Arrest", "SITA"], "SITA", set())
    idx.add("Common Legal Terms.md", ["Common Legal Terms"], "Common Legal Terms",
            {"de-novo"})   # NOTE: 'does-not-exist' deliberately absent
    return idx


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    terms = _mini_terms()
    idx = _mini_index()
    dead = validate_register(terms, idx)

    # dead-anchor refusal
    deadnames = {d["canonical"] for d in dead}
    check(deadnames == {"deadterm"},
          "dead-anchor: expected {'deadterm'}, got %s" % deadnames)

    def plan(fixture, rel):
        return build_link_plan(_load(fixture), rel, terms, idx)

    # 1) inflection piping
    edits, recs = plan("inflection.md", "inflection.md")
    out = apply_edits(_load("inflection.md"), edits)
    check("[[Curtilage|curtilage]]" in out, "inflection: lower 'curtilage' not piped")
    check("[[Curtilage]]" in out, "inflection: 'Curtilage' (==target) should be bare")
    check("[[Common Legal Terms#de-novo|de novo]]" in out,
          "inflection: 'de novo' glossary link missing")

    # 2) zone exemption — only the plain-prose occurrence links
    edits, recs = plan("zone_exempt.md", "zone_exempt.md")
    links = [r for r in recs if r["action"] == "link"]
    check(len(links) == 1 and links[0]["term"] == "de novo",
          "zone_exempt: expected exactly 1 'de novo' link, got %s"
          % [(r["term"], r["surface"]) for r in links])

    # 3) self-page — curtilage never links on Curtilage.md; de novo still does
    edits, recs = plan("selfpage.md", "Curtilage.md")
    acts = {r["term"]: r["action"] for r in recs}
    check(any(r["term"] == "curtilage" and r["action"] == "self-skip" for r in recs),
          "selfpage: curtilage should self-skip on Curtilage.md")
    check(not any(r["term"] == "curtilage" and r["action"] == "link" for r in recs),
          "selfpage: curtilage must NOT link on its own page")
    check(any(r["term"] == "de novo" and r["action"] == "link" for r in recs),
          "selfpage: de novo (foreign) should still link")

    # 4) longest-match — the whole SITA phrase links, not bare 'arrest'
    edits, recs = plan("longest.md", "longest.md")
    out = apply_edits(_load("longest.md"), edits)
    check("[[Search Incident to Arrest|search incident to arrest]]" in out,
          "longest: SITA phrase not linked whole")
    check("[[Arrest|arrest]]" not in out and "[[Arrest]]" not in out,
          "longest: bare 'arrest' inside SITA was wrongly linked")

    # 5) dead-anchor refusal — deadterm never links
    edits, recs = plan("deadanchor.md", "deadanchor.md")
    out = apply_edits(_load("deadanchor.md"), edits)
    check("does-not-exist" not in out and "[[Common Legal Terms#does" not in out,
          "deadanchor: dead-anchor term was linked")
    check(not any(r["term"] == "deadterm" for r in recs),
          "deadanchor: deadterm produced a record despite being dead")

    # 6) skip-list — skipword never links
    edits, recs = plan("skip.md", "skip.md")
    check(len(edits) == 0,
          "skip: skipword produced %d edits" % len(edits))

    # 7) idempotence — second pass on the written inflection text plans nothing
    edits, _ = plan("inflection.md", "inflection.md")
    out = apply_edits(_load("inflection.md"), edits)
    e2, _ = build_link_plan(out, "inflection.md", terms, idx)
    check(len(e2) == 0, "idempotence: second pass planned %d edits" % len(e2))

    # 8) table pipe-escape — a link inside a table cell escapes its display pipe
    edits, recs = plan("table.md", "table.md")
    out = apply_edits(_load("table.md"), edits)
    check("[[Common Legal Terms#de-novo\\|de novo]]" in out,
          "table: display pipe not escaped inside a table cell")

    if failures:
        print("link_terms.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("link_terms.py --self-test: PASS "
          "(inflection / zone / self-page / longest-match / dead-anchor / skip / "
          "idempotence / table-escape)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="S8 R7 term-link pass")
    ap.add_argument("--write", action="store_true", help="apply link edits corpus-wide")
    ap.add_argument("--self-test", action="store_true", help="run fixtures")
    ap.add_argument("--samples", type=int, default=10, help="sample diffs to print")
    ap.add_argument("--allow-pincite-lines", action="store_true",
                    help="DISABLE the sibling-lane guard (only on a de-conflicted re-run)")
    args = ap.parse_args(argv)
    if args.self_test:
        return _self_test()
    run(write=args.write, sample=args.samples,
        protect_pincite_lines=not args.allow_pincite_lines)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
