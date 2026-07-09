#!/usr/bin/env python3
"""
S8 exemption-zone catalog + block segmentation (spec S8 R2).

THE ONE CATALOG, ENCODED ONCE. The corpus linker and the LINT-5/LINT-7 rewrites
both import this module; the case-mention / term passes never edit inside a zone,
and the pin remediator (`remediate_pins.py`) drives its block segmentation off
`iter_blocks` here.

    ---- FROZEN PUBLIC API (do not rename / re-sign; downstream lanes bind it) ----
    ZONE_KINDS
    compute_zones(text, *, page_stem=None) -> list[dict]   # {start,end,kind}
    mask(text, zones=None, fill=" ")       -> str          # offset-preserving
    is_exempt(offset, zones)               -> bool
    iter_blocks(text)                      -> list[dict]    # {start,end,kind}

Zone semantics (spec R2, verbatim intent):
  (a) headings                          -> kind "heading"
  (b) code fences + mermaid blocks      -> kind "code"
  (c) direct quotations  "…" / “…”      -> kind "quote"
  (d) citation strings (reporter runs,
      `— *Id.* at 37.` lines, and
      parenthetical history)            -> kind "citation"
  (e) `## Sources` sections entire      -> kind "sources"
  (f) frontmatter + HTML comments       -> kind "frontmatter" / "comment"
  (g) selfpage  (the term's own page;
      no span math needed beyond
      handing the stem back — when
      `page_stem` is given we mark the
      literal self-title occurrences)   -> kind "selfpage"
  (h) the sanctioned Case cells of the
      S5 R6 case tables (first column
      of a `| Case | … |` table)        -> kind "casecell"

Python 3 stdlib only. READ-ONLY: this module never writes to content/.

Run `python3 scripts/s8/zones.py --self-test` to exercise the fixtures under
`scripts/s8/fixtures/zones/` (repo convention: cf. scripts/s7/survey.py).
"""

from __future__ import annotations

import os
import re
import sys

ZONE_KINDS = (
    "heading",
    "code",
    "quote",
    "citation",
    "sources",
    "frontmatter",
    "comment",
    "selfpage",
    "casecell",
)

# --------------------------------------------------------------------------
# Line helpers
# --------------------------------------------------------------------------

def _lines(text: str):
    """[(start, end)] char spans for each physical line (end excludes '\\n')."""
    out = []
    i = 0
    n = len(text)
    while i < n:
        j = text.find("\n", i)
        if j == -1:
            out.append((i, n))
            break
        out.append((i, j))
        i = j + 1
    return out


def _line_text(text: str, span) -> str:
    return text[span[0]:span[1]]


# --------------------------------------------------------------------------
# Block segmentation  (iter_blocks) — shared by the pin remediator and the
# later shingle detector.
# --------------------------------------------------------------------------

BLOCK_KINDS = ("para", "listitem", "blockquote", "table", "heading", "code", "frontmatter")

_RE_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_RE_FENCE_CLOSE = re.compile(r"^\s*(`{3,}|~{3,})\s*$")
_RE_HEADING = re.compile(r"^\s{0,3}#{1,6}(?:\s|$)")
_RE_LISTITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])(\s+)")
_RE_BLOCKQUOTE = re.compile(r"^\s{0,3}>")
_RE_TABLE_DELIM = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(?:\|\s*:?-{1,}:?\s*)*\|?\s*$")


def iter_blocks(text: str) -> list:
    """Segment `text` into contiguous blocks.

    Returns [{start, end, kind}] in document order, kind in BLOCK_KINDS.
    `end` is the offset just past the last non-newline char of the block
    (trailing newline excluded); blank separator lines belong to no block.
    """
    lines = _lines(text)
    L = len(lines)
    blocks = []
    idx = 0

    # frontmatter: a leading `---` fence closed by the next `---`
    if L and _line_text(text, lines[0]).strip() == "---":
        k = 1
        while k < L and _line_text(text, lines[k]).strip() not in ("---", "..."):
            k += 1
        if k < L:
            blocks.append({"start": lines[0][0], "end": lines[k][1], "kind": "frontmatter"})
            idx = k + 1

    while idx < L:
        ls, le = lines[idx]
        line = text[ls:le]

        if line.strip() == "":
            idx += 1
            continue

        # code fence
        m = _RE_FENCE.match(line)
        if m:
            fence = m.group(1)
            fchar = fence[0]
            k = idx + 1
            end_line = L - 1
            while k < L:
                l2 = _line_text(text, lines[k])
                m2 = _RE_FENCE_CLOSE.match(l2)
                if m2 and m2.group(1)[0] == fchar and len(m2.group(1)) >= len(fence):
                    end_line = k
                    break
                k += 1
            else:
                end_line = L - 1
            blocks.append({"start": ls, "end": lines[end_line][1], "kind": "code"})
            idx = end_line + 1
            continue

        # heading
        if _RE_HEADING.match(line):
            blocks.append({"start": ls, "end": le, "kind": "heading"})
            idx += 1
            continue

        # table (header row + delimiter row + body rows)
        if "|" in line and idx + 1 < L:
            nxt = _line_text(text, lines[idx + 1])
            if "-" in nxt and _RE_TABLE_DELIM.match(nxt):
                k = idx + 2
                while k < L:
                    l2 = _line_text(text, lines[k])
                    if l2.strip() == "" or "|" not in l2:
                        break
                    k += 1
                end_line = k - 1
                blocks.append({"start": ls, "end": lines[end_line][1], "kind": "table"})
                idx = end_line + 1
                continue

        # blockquote
        if _RE_BLOCKQUOTE.match(line):
            k = idx
            while k < L:
                l2 = _line_text(text, lines[k])
                if l2.strip() == "" or not _RE_BLOCKQUOTE.match(l2):
                    break
                k += 1
            end_line = k - 1
            blocks.append({"start": ls, "end": lines[end_line][1], "kind": "blockquote"})
            idx = end_line + 1
            continue

        # list item (one block per marker; indented / lazy lines continue it)
        m = _RE_LISTITEM.match(line)
        if m:
            indent = len(m.group(1))
            k = idx + 1
            while k < L:
                l2 = _line_text(text, lines[k])
                if l2.strip() == "":
                    break
                l2indent = len(l2) - len(l2.lstrip())
                m2 = _RE_LISTITEM.match(l2)
                if m2 and l2indent <= indent:
                    break
                if _RE_HEADING.match(l2) or _RE_FENCE.match(l2) or _RE_BLOCKQUOTE.match(l2):
                    break
                k += 1
            end_line = k - 1
            blocks.append({"start": ls, "end": lines[end_line][1], "kind": "listitem"})
            idx = end_line + 1
            continue

        # paragraph
        k = idx + 1
        while k < L:
            l2 = _line_text(text, lines[k])
            if l2.strip() == "":
                break
            if (
                _RE_HEADING.match(l2)
                or _RE_FENCE.match(l2)
                or _RE_BLOCKQUOTE.match(l2)
                or _RE_LISTITEM.match(l2)
            ):
                break
            k += 1
        end_line = k - 1
        blocks.append({"start": ls, "end": lines[end_line][1], "kind": "para"})
        idx = end_line + 1

    return blocks


# --------------------------------------------------------------------------
# Zone computation (compute_zones)
# --------------------------------------------------------------------------

_RE_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_RE_QUOTE_STRAIGHT = re.compile(r'"[^"\n]*"')
_RE_QUOTE_CURLY = re.compile("“[^”\n]*”")

# reporter volume/page runs: `799 F.3d 1361`, `533 U.S. 27, 34 (2001)`,
# `799 F.3d at 1364`, `338 U.S. 27–28`, `127 S. Ct. 1769, 1777`.
_REPORTER_TOKEN = (
    r"(?:U\.\s?S\.|S\.\s?Ct\.|L\.\s?Ed\.(?:\s?2d)?"
    r"|F\.\s?Supp\.(?:\s?(?:2d|3d))?|F\.\s?App'?x|F\.\s?(?:2d|3d|4th)?"
    r"|[A-Z][A-Za-z]{0,4}\.(?:\s?(?:2d|3d|4th))?)"
)
_RE_REPORTER = re.compile(
    r"\b\d{1,4}\s+" + _REPORTER_TOKEN + r"\s+(?:at\s+)?\d{1,4}"
    r"(?:\s*,\s*\d{1,4}(?:\s?[–-]\s?\d{1,4})?)*"
    r"(?:\s*\((?:[A-Za-z0-9.'’\s]*\s)?\d{4}\))?"
)
# `— *Id.* at 37.`, `— *Id.*`, `— Id. at 37`
_RE_ID_CITE = re.compile(
    r"\*?Id\.?\*?(?:\s+at\s+\d{1,4}(?:\s?[–-]\s?\d{1,4})?)?\.?",
)
_RE_ID_CITE_LINE = re.compile(
    r"[—-]\s*\*?Id\.?\*?(?:\s+at\s+\d{1,4}(?:\s?[–-]\s?\d{1,4})?)?\.?",
)
# parenthetical subsequent-history / signal phrases
_RE_PAREN_HIST = re.compile(
    r"\((?:"
    r"per\s+curiam|en\s+banc|reh'g[^)]*|rev'd[^)]*|aff'd[^)]*|cert\.[^)]*"
    r"|(?:cert\.\s+)?denied[^)]*|vacated[^)]*|overrul[^)]*|abrogat[^)]*"
    r"|supersed[^)]*|quoting[^)]*|citing[^)]*|internal[^)]*|emphasis[^)]*"
    r"|cleaned\s+up|plurality[^)]*|dissenting[^)]*|concurring[^)]*"
    r"|[A-Za-z0-9.'’\s]*Cir\.\s*\d{4}"
    r")\)",
    re.IGNORECASE,
)
_RE_PAREN_YEAR = re.compile(r"\(\d{4}\)")


def _add(zones, start, end, kind):
    if end > start:
        zones.append({"start": start, "end": end, "kind": kind})


def _normalize(zones):
    """Sort + clip to non-overlapping (union coverage preserved)."""
    if not zones:
        return []
    zones = sorted(zones, key=lambda z: (z["start"], -z["end"]))
    out = []
    max_end = -1
    for z in zones:
        s, e, k = z["start"], z["end"], z["kind"]
        if s < max_end:
            s = max_end
        if e <= s:
            continue
        out.append({"start": s, "end": e, "kind": k})
        if e > max_end:
            max_end = e
    return out


def _row_pipe_positions(row):
    """Offsets of the `|` column delimiters in a table row.

    A delimiter pipe is one that is NOT escaped (`\\|`) AND does NOT sit inside a
    `[[...]]` wikilink. An aliased wikilink in a cell (`[[Terry v. Ohio|Terry]]`)
    carries a DISPLAY pipe that is a caption alias, never a column boundary; the
    R11 sweep escapes it (`\\|`) but a raw one must not truncate the cell either
    (CR-S8-4). Wikilink-internal pipes are blanked before the delimiter scan.
    """
    buf = list(row)
    for m in re.finditer(r"\[\[.*?\]\]", row):
        for i in range(m.start(), m.end()):
            if buf[i] == "|":
                buf[i] = "\x00"
    return [m.start() for m in re.finditer(r"(?<!\\)\|", "".join(buf))]


def _first_cell_spans_of_case_table(text, block):
    """Yield (start, end) char spans of first-column data cells of a case table."""
    seg = text[block["start"]:block["end"]]
    rel_lines = _lines(seg)
    if len(rel_lines) < 2:
        return
    header = seg[rel_lines[0][0]:rel_lines[0][1]]
    # split header on delimiter pipes (unescaped, outside wikilinks); drop empty
    # edges from a leading/trailing pipe
    hpipes = _row_pipe_positions(header)
    hcells = []
    prev = 0
    for pp in hpipes + [len(header)]:
        hcells.append(header[prev:pp])
        prev = pp + 1
    cells = [c.strip() for c in hcells]
    trimmed = [c for c in cells if c != ""]
    if not trimmed or trimmed[0].lower() != "case":
        return
    # data rows start after the delimiter row (row index 1)
    for li in range(2, len(rel_lines)):
        rs, re_ = rel_lines[li]
        row = seg[rs:re_]
        if "|" not in row:
            continue
        # locate column-delimiter pipe positions within the row (unescaped, and
        # NOT the display pipe of an aliased wikilink in the cell — CR-S8-4)
        pipes = _row_pipe_positions(row)
        if not pipes:
            continue
        # first cell = between the leading pipe (if any) and the next pipe
        if row.lstrip().startswith("|"):
            if len(pipes) < 2:
                continue
            c_start = pipes[0] + 1
            c_end = pipes[1]
        else:
            c_start = 0
            c_end = pipes[0]
        abs_start = block["start"] + rs + c_start
        abs_end = block["start"] + rs + c_end
        yield abs_start, abs_end


def compute_zones(text: str, *, page_stem=None) -> list:
    """Zones as {start,end,kind} char-offset dicts, sorted, non-overlapping."""
    zones = []

    blocks = iter_blocks(text)

    # (f) frontmatter, (b) code, (a) heading, (h) casecell — off the segmenter
    heading_blocks = []
    for b in blocks:
        if b["kind"] == "frontmatter":
            _add(zones, b["start"], b["end"], "frontmatter")
        elif b["kind"] == "code":
            _add(zones, b["start"], b["end"], "code")
        elif b["kind"] == "heading":
            heading_blocks.append(b)
            _add(zones, b["start"], b["end"], "heading")
        elif b["kind"] == "table":
            for cs, ce in _first_cell_spans_of_case_table(text, b):
                _add(zones, cs, ce, "casecell")

    # (f) HTML comments
    for m in _RE_COMMENT.finditer(text):
        _add(zones, m.start(), m.end(), "comment")

    # (e) `## Sources` sections entire (heading -> next same/higher heading | EOF)
    def _heading_level(b):
        s = text[b["start"]:b["end"]].lstrip()
        return len(s) - len(s.lstrip("#"))

    for i, b in enumerate(heading_blocks):
        htext = text[b["start"]:b["end"]].lstrip("#").strip()
        if htext.lower() == "sources":
            lvl = _heading_level(b)
            end = len(text)
            for nb in heading_blocks[i + 1:]:
                if _heading_level(nb) <= lvl:
                    end = nb["start"]
                    break
            _add(zones, b["start"], end, "sources")

    # Build a working mask that blanks frontmatter/code/comment so quote /
    # citation / selfpage detection never fires inside them.
    protect = _normalize(
        [z for z in zones if z["kind"] in ("frontmatter", "code", "comment")]
    )
    masked = _apply_mask(text, protect, " ")

    # (c) direct quotations
    for rx in (_RE_QUOTE_STRAIGHT, _RE_QUOTE_CURLY):
        for m in rx.finditer(masked):
            _add(zones, m.start(), m.end(), "quote")

    # (d) citation strings
    for rx in (_RE_REPORTER, _RE_ID_CITE_LINE, _RE_PAREN_HIST, _RE_PAREN_YEAR):
        for m in rx.finditer(masked):
            _add(zones, m.start(), m.end(), "citation")

    # (g) selfpage — literal occurrences of the page's own title/stem
    if page_stem:
        stem = page_stem.strip()
        if stem:
            pat = re.compile(r"(?<![\w])" + re.escape(stem) + r"(?![\w])")
            for m in pat.finditer(masked):
                _add(zones, m.start(), m.end(), "selfpage")

    return _normalize(zones)


# --------------------------------------------------------------------------
# mask / is_exempt
# --------------------------------------------------------------------------

def _apply_mask(text, zones, fill):
    if not zones:
        return text
    buf = list(text)
    for z in zones:
        for i in range(z["start"], min(z["end"], len(buf))):
            if buf[i] != "\n":
                buf[i] = fill
    return "".join(buf)


def mask(text: str, zones=None, fill: str = " ") -> str:
    """Same-length text with zone spans blanked (newlines preserved)."""
    if zones is None:
        zones = compute_zones(text)
    return _apply_mask(text, zones, fill)


def is_exempt(offset: int, zones) -> bool:
    for z in zones:
        if z["start"] <= offset < z["end"]:
            return True
    return False


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

_FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "zones")


def _load(name):
    with open(os.path.join(_FIX, name), encoding="utf-8") as fh:
        return fh.read()


def _covering_kind(zones, off):
    for z in zones:
        if z["start"] <= off < z["end"]:
            return z["kind"]
    return None


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    def exempt_as(text, sub, kind, page_stem=None, occ=0):
        zs = compute_zones(text, page_stem=page_stem)
        off = _nth_index(text, sub, occ)
        check(off >= 0, f"substring not found: {sub!r}")
        if off >= 0:
            got = _covering_kind(zs, off)
            check(got == kind, f"expected {sub!r} exempt as {kind}, got {got}")

    def not_exempt(text, sub, page_stem=None, occ=0):
        zs = compute_zones(text, page_stem=page_stem)
        off = _nth_index(text, sub, occ)
        check(off >= 0, f"substring not found: {sub!r}")
        if off >= 0:
            check(not is_exempt(off, zs), f"expected {sub!r} NOT exempt, but it was ({_covering_kind(zs, off)})")

    # (a) heading
    t = _load("heading.md")
    exempt_as(t, "Katz v. United States", "heading", occ=0)   # in the ## heading
    not_exempt(t, "Katz v. United States", occ=1)             # in body prose

    # (b) code + mermaid
    t = _load("code.md")
    exempt_as(t, "Terry v. Ohio", "code", occ=0)              # inside fenced code
    exempt_as(t, "seizure --> arrest", "code", occ=0)         # inside mermaid fence
    not_exempt(t, "Terry v. Ohio", occ=1)                     # body prose

    # (c) quotes  (the workorder's example: caption inside a quote stays exempt)
    t = _load("quote.md")
    exempt_as(t, "Terry v. Ohio", "quote", occ=0)             # inside the quotation
    not_exempt(t, "Terry v. Ohio", occ=1)                     # same caption outside links

    # (d) citations
    t = _load("citation.md")
    exempt_as(t, "799 F.3d 1361", "citation")
    exempt_as(t, "533 U.S. 27, 34 (2001)", "citation")
    exempt_as(t, "Id.* at 37", "citation")
    exempt_as(t, "per curiam", "citation")
    not_exempt(t, "5:04 a.m.")                                # near-miss: a time, not a cite
    not_exempt(t, "Katz v. United States")                   # near-miss: a caption

    # (e) Sources section entire
    t = _load("sources.md")
    not_exempt(t, "Terry v. Ohio", occ=0)                    # body prose above Sources
    exempt_as(t, "Terry v. Ohio", "sources", occ=1)          # inside ## Sources

    # (f) frontmatter + comment
    t = _load("frontmatter.md")
    exempt_as(t, "Terry v. Ohio", "frontmatter", occ=0)      # in the YAML block
    not_exempt(t, "Terry v. Ohio", occ=1)                    # body prose
    t = _load("comment.md")
    exempt_as(t, "Terry v. Ohio", "comment", occ=0)          # inside <!-- -->
    not_exempt(t, "Terry v. Ohio", occ=1)                    # body prose

    # (g) selfpage
    t = _load("selfpage.md")
    exempt_as(t, "Curtilage", "selfpage", page_stem="Curtilage", occ=1)  # self-mention
    not_exempt(t, "Open Fields", page_stem="Curtilage")                  # other term links

    # (h) casecell
    t = _load("casecell.md")
    exempt_as(t, "Terry v. Ohio", "casecell", occ=0)         # first col of a case table
    not_exempt(t, "Katz v. United States")                   # Holding column links
    not_exempt(t, "de novo")                                 # a NON-case table's first col

    # (h') casecell w/ ALIASED wikilink in the first cell (CR-S8-4): the display
    # pipe inside `[[Target|alias]]` is NOT a column boundary, so the TAIL after
    # the alias stays inside casecell (was truncated at the inner `|`). Both the
    # raw display pipe and the R11-escaped `\|` form must span the whole cell.
    t = _load("casecell_aliased.md")
    exempt_as(t, "progeny", "casecell", occ=0)               # tail after raw `|` alias
    exempt_as(t, "Katz", "casecell", occ=0)                  # alias text itself
    exempt_as(t, "line", "casecell", occ=0)                  # tail after escaped `\|`
    not_exempt(t, "reasonable expectation of privacy")       # Holding column stays live

    # mixed
    t = _load("mixed.md")
    zs = compute_zones(t, page_stem="Curtilage")
    check(any(z["kind"] == "quote" for z in zs), "mixed: no quote zone")
    check(any(z["kind"] == "citation" for z in zs), "mixed: no citation zone")
    check(any(z["kind"] == "heading" for z in zs), "mixed: no heading zone")
    check(any(z["kind"] == "sources" for z in zs), "mixed: no sources zone")
    # non-overlap invariant
    prev = -1
    for z in zs:
        check(z["start"] >= prev, "mixed: zones overlap / unsorted")
        prev = z["end"]

    # mask is length-preserving and blanks a quoted caption
    t = _load("quote.md")
    m = mask(t)
    check(len(m) == len(t), "mask changed length")
    off = _nth_index(t, "Terry v. Ohio", 0)
    check(m[off:off + 5] == "     ", "mask did not blank the quoted caption")

    if failures:
        print("zones.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("zones.py --self-test: PASS (9 zone kinds + mixed + mask)")
    return 0


def _nth_index(text, sub, n):
    start = -1
    for _ in range(n + 1):
        start = text.find(sub, start + 1)
        if start == -1:
            return -1
    return start


def main(argv):
    if "--self-test" in argv:
        return _self_test()
    print(__doc__.strip())
    print("\nUsage: zones.py --self-test")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
