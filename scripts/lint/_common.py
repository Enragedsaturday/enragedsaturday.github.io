#!/usr/bin/env python3
"""
Shared helpers for the CSSI LINT roster (S1 §3.H).

Standard-library only (no pip installs). Every lint imports from this module.

Conventions established by the corpus (see S1 §3.A/3.B and S4 Appendix B):
  - wikilinks are [[Page]] / [[Page#anchor]] / [[Page#^block]] / [[Page|display]]
  - CourtListener opinion URLs look like
        https://www.courtlistener.com/opinion/<id>/<slug>/
  - case tables are GFM markdown tables
  - case names use the party-v-party pattern  "Foo v. Bar"
  - doctrine pages carry  type: doctrine ; case pages carry  type: case

These helpers are tolerant of the PRE-overhaul corpus state (they will report
many violations now — that is informational, not a failure) and keep working
after the S2 folder restructure (all scans are recursive over content/**/*.md).
"""

import glob as _glob
import json
import os
import re
import sys

# --------------------------------------------------------------------------
# repo / content discovery
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
# scripts/lint/_common.py -> repo root is two levels up
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
CONTENT_ROOT = os.path.join(REPO_ROOT, "content")


def iter_markdown_files(paths=None):
    """Yield absolute paths of markdown files to CHECK.

    `paths` may be None (default: every content/**/*.md), or a list of
    glob patterns / files / directories to scope to a subset. Directories
    and bare globs are expanded recursively; only *.md files are returned.
    """
    if not paths:
        pattern = os.path.join(CONTENT_ROOT, "**", "*.md")
        for p in sorted(_glob.glob(pattern, recursive=True)):
            yield p
        return

    seen = set()
    for raw in paths:
        cand = raw
        if not os.path.isabs(cand):
            cand = os.path.join(REPO_ROOT, raw)
        if os.path.isdir(cand):
            for p in sorted(_glob.glob(os.path.join(cand, "**", "*.md"),
                                      recursive=True)):
                if p not in seen:
                    seen.add(p)
                    yield p
        elif os.path.isfile(cand) and cand.endswith(".md"):
            if cand not in seen:
                seen.add(cand)
                yield cand
        else:
            # treat as a glob (relative to repo root if not absolute)
            for p in sorted(_glob.glob(cand, recursive=True)):
                if p.endswith(".md") and p not in seen:
                    seen.add(p)
                    yield p


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def relpath(path):
    try:
        return os.path.relpath(path, REPO_ROOT)
    except ValueError:
        return path


# --------------------------------------------------------------------------
# minimal YAML-subset frontmatter parser (stdlib only — no PyYAML)
# --------------------------------------------------------------------------

def split_frontmatter(text):
    """Return (frontmatter_dict, body_text, body_start_line).

    body_start_line is the 1-based line number in the ORIGINAL file where the
    body begins, so lints can report accurate line numbers against the body.
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, 1
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text, 1
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fm = parse_yaml_subset(fm_lines)
    return fm, body, end + 2


def _strip_inline_comment(value):
    # remove a trailing "  # comment" but not a '#' inside quotes
    out = []
    in_s = in_d = False
    i = 0
    while i < len(value):
        c = value[i]
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d:
            # only treat as comment if preceded by whitespace or start
            if i == 0 or value[i - 1] in " \t":
                break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _scalar(value):
    value = _strip_inline_comment(value).strip()
    if value == "":
        return ""
    # inline flow list  [a, b, c]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(x.strip()) for x in _split_flow(inner)]
    # inline flow map {a: b} -> keep raw (rare; not needed by lints), but an
    # EMPTY flow map {} must reparse to a real empty dict for parity with [] so
    # serializer output "key: {}" (CR-15) does not reparse as a phantom-drift
    # string ("{}") against a projected empty mapping.
    if value == "{}":
        return {}
    return _unquote(value)


def _split_flow(inner):
    parts = []
    buf = []
    depth = 0
    in_s = in_d = False
    for c in inner:
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        if c in "[{(" and not in_s and not in_d:
            depth += 1
        elif c in "]})" and not in_s and not in_d:
            depth -= 1
        if c == "," and depth == 0 and not in_s and not in_d:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(c)
    if buf:
        parts.append("".join(buf))
    return parts


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def parse_yaml_subset(lines):
    """Parse a restricted YAML subset sufficient for the case/doctrine schema:
    nested mappings, block sequences (scalars or mappings), and inline flow
    lists. Comments and blank lines are ignored. Good enough for the keys the
    lints read; not a general YAML implementation.
    """
    # drop blanks / pure comments
    cleaned = []
    for ln in lines:
        if ln.strip() == "" or ln.lstrip().startswith("#"):
            continue
        cleaned.append(ln.rstrip("\n"))
    pos = [0]

    def parse_block(min_indent):
        node = None  # could become dict or list
        while pos[0] < len(cleaned):
            line = cleaned[pos[0]]
            ind = _indent(line)
            if ind < min_indent:
                break
            stripped = line.strip()
            if stripped.startswith("- "):
                if ind < min_indent:
                    break
                if node is None:
                    node = []
                if not isinstance(node, list):
                    break
                pos[0] += 1
                rest = stripped[2:]
                if ":" in rest and not rest.startswith("[") \
                        and not rest.startswith("{"):
                    # list item that is itself a mapping; first key inline
                    key, _, val = rest.partition(":")
                    item = {}
                    item[key.strip()] = _scalar(val)
                    # subsequent keys of this mapping are indented deeper than
                    # the dash position
                    child_min = ind + 2
                    sub = parse_block(child_min)
                    if isinstance(sub, dict):
                        item.update(sub)
                    node.append(item)
                else:
                    node.append(_scalar(rest))
            elif ":" in stripped:
                if node is None:
                    node = {}
                if not isinstance(node, dict):
                    break
                key, _, val = stripped.partition(":")
                key = key.strip()
                val = val.strip()
                pos[0] += 1
                if val == "":
                    # could be nested mapping/sequence on following lines
                    child = parse_block(ind + 1)
                    node[key] = child if child is not None else ""
                else:
                    node[key] = _scalar(val)
            else:
                # unrecognized line; skip to avoid infinite loop
                pos[0] += 1
        return node

    result = parse_block(0)
    return result if isinstance(result, dict) else {}


def fm_get(fm, *path, default=None):
    """Safe nested getter:  fm_get(fm, 'treatment', 'status')."""
    cur = fm
    for key in path:
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return default
    return cur


# --------------------------------------------------------------------------
# regexes shared across lints
# --------------------------------------------------------------------------

# A party token: a capitalized word (may carry internal periods/apostrophes),
# optionally followed by capitalized words or common lowercase connectors.
_PARTY = (r"[A-Z][A-Za-z.&'’\-]*"
          r"(?:\s+(?:[A-Z][A-Za-z.&'’\-]*|of|the|and|for|ex|rel\.|et|al\.|"
          r"de|van|von|la|le|du|dos|in|re)){0,5}")

# party-v-party case name, e.g. "Florida v. Jardines", "United States v. Dunn"
CASE_RE = re.compile(r"(%s)\s+v\.\s+(%s)" % (_PARTY, _PARTY))

# reporter citation (volume Reporter firstpage), with optional pincite ", page"
_REPORTER = (r"U\.?\s?S\.?|S\.?\s?Ct\.?|L\.?\s?Ed\.?(?:\s?2d)?|"
             r"F\.?(?:\s?(?:2d|3d|4th))?|F\.?\s?Supp\.?(?:\s?(?:2d|3d))?|"
             r"F\.?\s?App'?x\.?|So\.?(?:\s?(?:2d|3d))?|P\.?(?:\s?(?:2d|3d))?|"
             r"N\.?[EW]\.?(?:\s?2d)?|A\.?(?:\s?(?:2d|3d))?|S\.?[EW]\.?(?:\s?2d)?|"
             r"Cal\.?(?:\s?(?:App|Rptr)\.?)?(?:\s?(?:2d|3d|4th|5th))?")
REPORTER_RE = re.compile(r"\b\d{1,4}\s+(?:%s)\s+\d" % _REPORTER)

# a pinpoint cite: "... at <page>", "vol Reporter first, <pin>", or a paragraph
# pin "¶ N" / "¶¶ N–M" (opinions whose CL text is paragraph-numbered with no
# reporter star-pagination — e.g. Ruckman "majority op. ¶ 9"; the O1-deferred
# Carroll/Benn ¶-pin false-positive class). Range dash = en/em/hyphen.
PINCITE_RE = re.compile(
    r"(?:\bat\s+\*?\d{1,4})"                                  # "at 838"
    r"|(?:\b\d{1,4}\s+(?:%s)\s+\d{1,4}\s*,\s*\d{1,4})"        # "569 U.S. 1, 6"
    r"|(?:¶¶?\s*\d{1,4}(?:\s*[–—-]\s*\d{1,4})?)"  # "¶ 9" / "¶¶ 12–14"
    % _REPORTER)

# U.S. Reports citation (strong SCOTUS signal): "547 U.S. 398"
US_REPORTER_RE = re.compile(r"\b\d{1,4}\s+U\.?\s?S\.?\s+\d{1,4}")
SCT_REPORTER_RE = re.compile(r"\b\d{1,4}\s+S\.?\s?Ct\.?\s+\d{1,4}")

# wikilinks:  [[Target]] | [[Target#anchor]] | [[Target|display]] | [[#anchor]]
WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")

# inline markdown link  [text](url)
MDLINK_RE = re.compile(r"\[([^\[\]]*)\]\(([^()\s]+)[^()]*\)")

# inline code span  `...`
INLINE_CODE_RE = re.compile(r"`[^`]*`")

# CourtListener opinion URL (capture the numeric id)
CL_OPINION_URL_RE = re.compile(
    r"https?://(?:www\.)?courtlistener\.com/opinion/(\d+)/[^\s)\]\"'>]*")
# any CL URL (opinion or otherwise)
CL_ANY_URL_RE = re.compile(
    r"https?://(?:www\.)?courtlistener\.com/[^\s)\]\"'>]+")


# --------------------------------------------------------------------------
# markdown structure helpers
# --------------------------------------------------------------------------

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def fenced_line_numbers(body_lines):
    """Return a set of 0-based line indexes that fall inside ``` code fences."""
    inside = False
    fence = None
    out = set()
    for i, line in enumerate(body_lines):
        s = line.lstrip()
        if not inside and (s.startswith("```") or s.startswith("~~~")):
            inside = True
            fence = s[:3]
            out.add(i)
            continue
        if inside:
            out.add(i)
            if s.startswith(fence):
                inside = False
                fence = None
    return out


def slugify(heading_text):
    """GitHub/Quartz-style heading slug: lowercase, strip markdown emphasis &
    punctuation, spaces -> hyphens."""
    t = heading_text.strip().lower()
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", t)
    t = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("&", " and ")
    t = re.sub(r"[^\w\s\-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t)
    return t


def iter_headings(body_lines, skip_fenced=True):
    """Yield (line_index, level, text) for ATX headings outside code fences."""
    fenced = fenced_line_numbers(body_lines) if skip_fenced else set()
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        m = HEADING_RE.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2).strip()


def sections(body_lines):
    """Split body into sections keyed by H2 headings.
    Returns a list of dicts: {title, slug, level, start, end} (line indexes).
    """
    heads = [(i, lvl, txt) for (i, lvl, txt) in iter_headings(body_lines)
             if lvl == 2]
    out = []
    for idx, (i, lvl, txt) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(body_lines)
        out.append({"title": txt, "slug": slugify(txt), "level": lvl,
                    "start": i, "end": end})
    return out


def mask_links_and_code(line):
    """Return the line with [[wikilinks]] and `code` spans blanked to spaces
    (same length), so bare-text scanners don't match inside them. Markdown
    links [text](url) are NOT masked (a CL link is not a case-page wikilink)."""
    def blank(m):
        return " " * (m.end() - m.start())
    line = INLINE_CODE_RE.sub(blank, line)
    line = WIKILINK_RE.sub(blank, line)
    return line


# --------------------------------------------------------------------------
# GFM table helpers (shared by S5's convert_tables + LINT-16)
# --------------------------------------------------------------------------

# a markdown link whose target is an absolute http(s) URL: [anchor](https://…)
MDLINK_URL_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
_TABLE_SEP_CELL_RE = re.compile(r"^:?-{1,}:?$")


def split_table_row(line):
    """Split a GFM table row into trimmed cell strings, honoring [[wikilink|pipes]]
    and `code | spans` (their pipes are NOT cell boundaries) and escaped \\| pipes.
    Bounding pipes yield empty edge cells, which are dropped."""
    s = line.strip()
    cells, buf = [], []
    depth_wiki = 0
    in_code = False
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch == "`":
            in_code = not in_code
            buf.append(ch)
            i += 1
            continue
        if not in_code and ch == "[" and i + 1 < n and s[i + 1] == "[":
            depth_wiki += 1
            buf.append("[[")
            i += 2
            continue
        if not in_code and ch == "]" and i + 1 < n and s[i + 1] == "]":
            if depth_wiki > 0:
                depth_wiki -= 1
            buf.append("]]")
            i += 2
            continue
        if ch == "\\" and i + 1 < n:
            buf.append(s[i:i + 2])
            i += 2
            continue
        if ch == "|" and not in_code and depth_wiki == 0:
            cells.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    cells.append("".join(buf))
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [x.strip() for x in cells]


def _has_cell_pipe(line):
    """True iff `line` carries a GFM cell-delimiter pipe — a top-level '|' that
    is NOT inside a [[wikilink]] (its display pipe), an inline `code` span, or
    escaped (\\|). Mirrors split_table_row's masking so prose such as
    ``See [[Page|alias]] ...`` or ``See `x | y` ...`` is not mistaken for a table
    row (which iter_tables would otherwise treat as a header if a separator-shaped
    line follows)."""
    depth_wiki = 0
    in_code = False
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if ch == "`":
            in_code = not in_code
            i += 1
            continue
        if not in_code and ch == "[" and i + 1 < n and line[i + 1] == "[":
            depth_wiki += 1
            i += 2
            continue
        if not in_code and ch == "]" and i + 1 < n and line[i + 1] == "]":
            if depth_wiki > 0:
                depth_wiki -= 1
            i += 2
            continue
        if ch == "\\" and i + 1 < n:
            i += 2
            continue
        if ch == "|" and not in_code and depth_wiki == 0:
            return True
        i += 1
    return False


def is_table_row(line):
    # A line is a GFM table row only if it carries an UNMASKED cell pipe — a '|'
    # outside wikilinks/code/escapes (F-S5-03 hardening; reuses split_table_row's
    # masking so wikilink display pipes and code-span pipes never trip detection).
    return line.strip() != "" and _has_cell_pipe(line)


def is_separator_row(line):
    cells = split_table_row(line)
    return len(cells) > 0 and all(
        _TABLE_SEP_CELL_RE.match(x.replace(" ", "")) for x in cells)


# F-S5-03 — a pipe-bearing line immediately after a table header+separator is a
# real DATA ROW only if its shape is table-row-like. A footnote definition
# ([^id]: … | …) or a trailing block anchor must NOT be swallowed as a row.
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:")
BLOCK_ANCHOR_ONLY_RE = re.compile(r"^\s*\^[A-Za-z0-9][A-Za-z0-9-]*\s*$")


def is_table_body_row(line, header_count):
    """True iff `line` is a valid GFM table DATA row for a table whose header
    has `header_count` cells (F-S5-03 row-shape validation):

      * it is a table row (contains an unescaped pipe, non-blank), AND
      * its cell count is within ±1 of the header, AND
      * it is NOT a footnote definition  `[^id]: …`, AND
      * it is NOT a block-anchor-only line  `^anchor`.

    This stops footnote definitions, trailing block anchors, and stray
    pipe-bearing prose that abuts a table from being consumed as table rows
    (which the converter would then rewrite and LINT-16 would mis-scan)."""
    if not is_table_row(line):
        return False
    if FOOTNOTE_DEF_RE.match(line):
        return False
    if BLOCK_ANCHOR_ONLY_RE.match(line):
        return False
    cells = split_table_row(line)
    return abs(len(cells) - header_count) <= 1


def iter_tables(body_lines):
    """Yield (header_line_index, header_cells, body_row_indexes) for every GFM
    table (header + separator + rows) outside fenced code blocks. Data rows are
    validated by row shape (see is_table_body_row) so footnote definitions and
    block anchors abutting a table are not mistaken for rows (F-S5-03)."""
    fenced = fenced_line_numbers(body_lines)
    i, n = 0, len(body_lines)
    while i < n:
        if (
            i not in fenced
            and is_table_row(body_lines[i])
            and i + 1 < n
            and (i + 1) not in fenced
            and is_table_row(body_lines[i + 1])
            and is_separator_row(body_lines[i + 1])
        ):
            header_cells = split_table_row(body_lines[i])
            hcount = len(header_cells)
            j = i + 2
            rows = []
            while (j < n and j not in fenced
                   and is_table_body_row(body_lines[j], hcount)):
                rows.append(j)
                j += 1
            yield i, header_cells, rows
            i = j
            continue
        i += 1


def _strip_md_header(text):
    t = text.strip().lower()
    t = re.sub(r"\*+", "", t)
    t = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", t)
    t = re.sub(r"[`_]", "", t)
    return t.strip()


def classify_case_header(text):
    """Classify a Case-table header cell into a column ROLE (S5 R6). The data
    columns are tested before the broad case/name test; order matters."""
    t = _strip_md_header(text)
    if "courtlistener" in t or re.search(r"\bcl\b", t) or "opinion" in t or "link" in t:
        return "opinion"
    if "primary home" in t or re.search(r"\bhome\b", t):
        return "home"
    if "relevance" in t or "why it matters" in t or "framed here" in t:
        return "relevance"
    if "holding" in t:
        return "holding"
    if "weight" in t or "authority" in t or "precedential" in t:
        return "weight"
    if "treatment" in t or "status" in t or "good law" in t or "good-law" in t:
        return "treatment"
    if re.search(r"\byear\b", t) or re.search(r"\bdate\b", t) or "decided" in t:
        return "year"
    if re.search(r"\b(case|name)\b", t):
        return "case"
    return "other"


# the three sanctioned Case-table schemas (S5 R6): key -> (headers, roles)
CASE_TABLE_SCHEMAS = {
    "key": (["Case", "Holding", "Opinion"], ["case", "holding", "opinion"]),
    "related": (
        ["Case", "Relevance here", "Primary home", "Opinion"],
        ["case", "relevance", "home", "opinion"],
    ),
    "index": (["Case", "Primary home", "Opinion"], ["case", "home", "opinion"]),
}


def classify_case_table(kinds):
    """Given the header column ROLES, return a sanctioned-schema key or None
    (None => not a sanctioned/recognizable case table). PURE role mapping —
    section context is applied separately (see section_schema_kind), so the
    mechanical converter keeps its role-only view of a table."""
    if "case" not in kinds:
        return None
    has = lambda k: k in kinds  # noqa: E731
    if has("home") and has("relevance"):
        return "related"
    if has("home") and not has("relevance") and not has("holding"):
        return "index"
    if has("holding") and not has("home"):
        return "key"
    return None


def schema_of_header(header_cells):
    """Return the sanctioned schema key ('key'|'related'|'index') iff
    header_cells EXACTLY equals that schema's header strings, else None."""
    for key, (hdrs, _roles) in CASE_TABLE_SCHEMAS.items():
        if header_cells == hdrs:
            return key
    return None


def section_schema_kind(section_title):
    """F-S5-04 — the section-aware schema requirement. Given the H2 title a
    case-table sits under, return the REQUIRED sanctioned schema key, or None if
    the section does not by itself constrain the schema:

        '## Related cases across doctrines'  -> 'related'  (needs 'Relevance here')
        '## Case Index'                      -> 'index'
        '## Key cases'                       -> 'key'

    The Case Index schema is otherwise reserved for the Case Index page (checked
    at the call site by page title/stem), so a bare '| Case | Primary home |
    Opinion |' inside a Related section is a mismatch, not a silently-accepted
    Case Index."""
    if not section_title:
        return None
    t = re.sub(r"\s+", " ", section_title.strip().lower())
    if "related cases" in t:
        return "related"
    if "case index" in t:
        return "index"
    if t == "key cases" or t.startswith("key cases"):
        return "key"
    return None


# --------------------------------------------------------------------------
# S1 A8 authority-weight allowlist — the ONE canonical copy (shared by LINT-4's
# exact validation and LINT-16's authored-data detection, F-S5-07). The six
# tiers, incl. 'Historical'; the two circuit-suffixed tiers carry a mandatory
# circuit suffix.
# --------------------------------------------------------------------------

WEIGHT_CIRCUIT_RE_SRC = (
    r"(?:1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|D\.C\.|Fed\.) Cir\.")
WEIGHT_EXACT_LABELS = frozenset({
    "Binding — SCOTUS",
    "Persuasive — state, illustrative",
    "Persuasive only — non-precedential",
    "Historical",
})
WEIGHT_BINDING_INCIRCUIT_RE = re.compile(
    r"^Binding in-circuit — %s$" % WEIGHT_CIRCUIT_RE_SRC)
WEIGHT_PERSUASIVE_OUTSIDE_RE = re.compile(
    r"^Persuasive \(outside circuit\) — %s$" % WEIGHT_CIRCUIT_RE_SRC)
WEIGHT_TIER_WORDS = ("binding", "persuasive", "historical")

# Detection LEADS for an authored weight LABEL leaking into a table cell
# (LINT-16 R7). Multi-word tier labels are distinctive substrings; the two
# circuit-suffixed tiers match on their fixed prefix (any '<tier> — <circuit>');
# the bare tier word 'Historical' matches only as a whole word to avoid firing
# on holding prose (e.g. 'the historical practice').
WEIGHT_LABEL_LEADS = (
    "Binding — SCOTUS",
    "Binding in-circuit —",
    "Persuasive (outside circuit) —",
    "Persuasive — state, illustrative",
    "Persuasive only — non-precedential",
    "Historical",
)
_HISTORICAL_WORD_RE = re.compile(r"\bHistorical\b")
# CR-06: fold every dash variant (hyphen-minus, unicode hyphens, en/em dashes,
# minus sign) to one form before matching, so a leaked label written with `-` or
# `–` instead of the canonical `—` can't slip past LINT-16 as clean. Both the cell
# and the lead are normalized identically, so internal hyphens (in-circuit,
# non-precedential) stay consistent and never cause a mismatch.
_DASH_NORM_RE = re.compile(r"[‐‑‒–—―−-]")


def _normalize_dashes(s):
    return _DASH_NORM_RE.sub("-", s)


def weight_label_in_cell(cell):
    """Return the S1 A8 authority-weight label authored into a table cell
    (LINT-16 R7), or None. Covers all six tiers including 'Historical'. Dash
    variants are normalized (CR-06) so a wrong-dash leak still matches."""
    norm_cell = _normalize_dashes(cell)
    for lead in WEIGHT_LABEL_LEADS:
        if lead == "Historical":
            if _HISTORICAL_WORD_RE.search(cell):
                return "Historical"
        elif _normalize_dashes(lead) in norm_cell:
            return lead
    return None


# --------------------------------------------------------------------------
# corpus index (pages + anchors + aliases) for link resolution
# --------------------------------------------------------------------------

class CorpusIndex:
    def __init__(self):
        self.page_by_norm = {}     # normalized name -> stem
        self.anchors = {}          # stem -> set(anchor slugs incl. ^blocks)
        self.alias_by_norm = {}    # normalized alias -> stem

    @staticmethod
    def norm(name):
        n = name.strip().lower()
        n = re.sub(r"\.md$", "", n)
        n = n.replace("’", "'")
        n = re.sub(r"\s+", " ", n)
        return n

    def resolve(self, target):
        """Resolve a wikilink target (page part, no #anchor) to a stem, or
        None. Tries basename, full relative path, alias, and slug forms."""
        if not target:
            return None
        cand = target.strip()
        # strip any leading path; Quartz resolves by basename for [[..]]
        base = cand.split("/")[-1]
        for key in (cand, base):
            n = self.norm(key)
            if n in self.page_by_norm:
                return self.page_by_norm[n]
            if n in self.alias_by_norm:
                return self.alias_by_norm[n]
        # slug fallback (e.g. [[two-definitions-of-search]])
        sl = slugify(base)
        return self._slug_lookup.get(sl)

    def has_anchor(self, stem, anchor):
        if stem not in self.anchors:
            return False
        a = anchor.strip()
        if a.startswith("^"):
            return a.lower() in self.anchors[stem]
        return slugify(a) in self.anchors[stem]


def build_corpus_index(root=None):
    """Index every page in content/ (always the FULL corpus, regardless of any
    scoping arg) so link/anchor resolution is correct even when a lint is
    scoped to a subset of files."""
    root = root or CONTENT_ROOT
    idx = CorpusIndex()
    idx._slug_lookup = {}
    for path in _glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        stem = os.path.splitext(os.path.basename(path))[0]
        try:
            text = read_text(path)
        except OSError:
            continue
        fm, body, _ = split_frontmatter(text)
        idx.page_by_norm[idx.norm(stem)] = stem
        idx._slug_lookup[slugify(stem)] = stem
        # title / topic as additional resolvable names
        for key in ("title", "topic"):
            val = fm.get(key)
            if isinstance(val, str) and val.strip():
                idx.alias_by_norm.setdefault(idx.norm(val), stem)
        aliases = fm.get("aliases")
        if isinstance(aliases, list):
            for al in aliases:
                if isinstance(al, str) and al.strip():
                    idx.alias_by_norm.setdefault(idx.norm(al), stem)
        elif isinstance(aliases, str) and aliases.strip():
            idx.alias_by_norm.setdefault(idx.norm(aliases), stem)
        # anchors: heading slugs + ^block ids
        anchors = set()
        body_lines = body.split("\n")
        for _, _, txt in iter_headings(body_lines):
            anchors.add(slugify(txt))
        for m in re.finditer(r"(?:^|\s)(\^[A-Za-z0-9][A-Za-z0-9-]*)\s*$",
                             body, flags=re.MULTILINE):
            anchors.add(m.group(1).lower())
        idx.anchors[stem] = anchors
    return idx


# --------------------------------------------------------------------------
# violation emission + CLI runner scaffold
# --------------------------------------------------------------------------

HIGH = "high"
MEDIUM = "medium"
LOW = "low"


def make_violation(lint, path, line, severity, message):
    return {
        "lint": lint,
        "file": relpath(path),
        "line": line,
        "severity": severity,
        "message": message,
    }


def emit(violations, stream=None):
    stream = stream or sys.stdout
    for v in violations:
        stream.write(json.dumps(v, ensure_ascii=False) + "\n")


def exit_code_for(violations):
    return 1 if any(v.get("severity") == HIGH for v in violations) else 0


def cli_main(run_fn, lint_name):
    """Standard CLI entrypoint: scope args -> run_fn(paths) -> JSON lines.
    Exits non-zero iff any high-severity violation is found."""
    args = sys.argv[1:]
    paths = args if args else None
    violations = run_fn(paths)
    emit(violations)
    n_high = sum(1 for v in violations if v["severity"] == HIGH)
    sys.stderr.write(
        "[%s] %d violation(s): %d high, %d medium, %d low\n" % (
            lint_name, len(violations), n_high,
            sum(1 for v in violations if v["severity"] == MEDIUM),
            sum(1 for v in violations if v["severity"] == LOW)))
    sys.exit(exit_code_for(violations))
