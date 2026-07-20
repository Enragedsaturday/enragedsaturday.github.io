#!/usr/bin/env python3
"""
S9 Lane P0-A — the assertion inventory (spec S9 R2, the exhaustiveness gate).

Deterministically extracts EVERY tracked assertion from every R2 object class and
emits `_run/s9/assertion-inventory.json`.  Each item carries a stable, content-hash
`assertion_id` — re-runs re-derive identical ids on unchanged content (spec R2:
"zero items may end the run without a verdict"; the downstream ledger joins by id).

Object classes (spec R2 / LEDGER-SCHEMA object_class enum):
    case · doctrine · reference · glossary · index · nav · lake-record ·
    ledger-row · registry

Assertion kinds (spec R2 list):
    case_cite · proposition · quote_pinpoint (+pinpoint_status +fragment) ·
    treatment / treatment_override · weight_label · home_role ·
    registry_callout_pair · mermaid · link_target · definition · index_row ·
    coverage_row · link_mention · link_pincite · link_embed · link_term_page

Stdlib only.  Read-only over content/, the lake, the S6/S8 ledgers, and the S3
registry.  Writes ONLY _run/s9/assertion-inventory.json (this lane's output).

Usage:
    python3 scripts/s9/build_inventory.py            # build -> _run/s9/assertion-inventory.json
    python3 scripts/s9/build_inventory.py --report   # build + human report to stderr
    python3 scripts/s9/build_inventory.py --self-test # fixtures self-test (no corpus, no write)
    python3 scripts/s9/build_inventory.py --stdout    # print JSON to stdout, do not write
    python3 scripts/s9/build_inventory.py --now <iso> # pin the header timestamp (determinism)
"""

import argparse
import glob as _glob
import hashlib
import json
import os
import re
import subprocess
import sys
import datetime

# --------------------------------------------------------------------------
# repo discovery
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))

LANE = "o2-opus-xhigh"
MODEL = "claude-opus-4-8"
SPEC = "S9 R2 (Lane P0-A)"
SCHEMA = "s9.assertion-inventory.v1"


class Roots:
    """The five read-only input roots.  Overridable for the fixtures self-test."""

    def __init__(self, base=None):
        base = base or REPO_ROOT
        self.content = os.path.join(base, "content")
        self.lake = os.path.join(base, "_overhaul2", "lake", "cases")
        self.s6_ledger = os.path.join(base, "_run", "s6-coverage-ledger.json")
        self.s8_ledger = os.path.join(base, "_run", "s8-link-ledger.json")
        self.registry = os.path.join(base, "_overhaul2", "points", "registry.yaml")
        self.base = base

    @classmethod
    def fixtures(cls):
        fx = os.path.join(HERE, "fixtures", "inventory")
        r = cls.__new__(cls)
        r.base = fx
        r.content = os.path.join(fx, "content")
        r.lake = os.path.join(fx, "lake", "cases")
        r.s6_ledger = os.path.join(fx, "s6-coverage-ledger.json")
        r.s8_ledger = os.path.join(fx, "s8-link-ledger.json")
        r.registry = os.path.join(fx, "points", "registry.yaml")
        return r


# ==========================================================================
# vendored YAML-subset frontmatter parser (stdlib only; no cross-lane import,
# so P0-A stays deterministic even while sibling lanes edit scripts/lint/).
# Mirrors scripts/lint/_common.py's tested parser.
# ==========================================================================

def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def split_frontmatter(text):
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
    fm = parse_yaml_subset(lines[1:end])
    body = "\n".join(lines[end + 1:])
    return fm, body, end + 2


def _strip_inline_comment(value):
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
            if i == 0 or value[i - 1] in " \t":
                break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


def _split_flow(inner):
    parts, buf = [], []
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


def _scalar(value):
    value = _strip_inline_comment(value).strip()
    if value == "":
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_unquote(x.strip()) for x in _split_flow(inner)]
    if value == "{}":
        return {}
    return _unquote(value)


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def parse_yaml_subset(lines):
    cleaned = []
    for ln in lines:
        if ln.strip() == "" or ln.lstrip().startswith("#"):
            continue
        cleaned.append(ln.rstrip("\n"))
    pos = [0]

    def parse_block(min_indent):
        node = None
        while pos[0] < len(cleaned):
            line = cleaned[pos[0]]
            ind = _indent(line)
            if ind < min_indent:
                break
            stripped = line.strip()
            if stripped.startswith("- "):
                if node is None:
                    node = []
                if not isinstance(node, list):
                    break
                pos[0] += 1
                rest = stripped[2:]
                if ":" in rest and not rest.startswith("[") \
                        and not rest.startswith("{"):
                    key, _, val = rest.partition(":")
                    item = {key.strip(): _scalar(val)}
                    sub = parse_block(ind + 2)
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
                    child = parse_block(ind + 1)
                    node[key] = child if child is not None else ""
                else:
                    node[key] = _scalar(val)
            else:
                pos[0] += 1
        return node

    result = parse_block(0)
    return result if isinstance(result, dict) else {}


def parse_yaml_file(path):
    """Parse a whole (frontmatter-less) YAML-subset file, e.g. the registry."""
    return parse_yaml_subset(read_text(path).split("\n"))


# ==========================================================================
# markdown helpers
# ==========================================================================

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
MDLINK_URL_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
RULE_CALLOUT_RE = re.compile(r"^>\s*\[!rule\]")
BLOCK_ANCHOR_RE = re.compile(r"^>\s*\^([A-Za-z0-9][\w-]*)\s*$")
LISTITEM_RE = re.compile(r"^\s*[-*]\s+")
# A genuine reporter citation is "<vol> <Reporter> <page>" (e.g. "540 U.S. 544",
# "997 F.3d 191"): a volume number, a reporter token, then a page number. Slip-/
# docket-only citation strings ("No. 23-1197, slip op. (U.S. 2026)") carry no
# reporter page and must NOT be counted as an official citation.
REPORTER_CITE_RE = re.compile(r"\b\d+\s+[A-Z][.A-Za-z0-9 ]*?\s\d+")


def slugify(text):
    t = text.strip().lower()
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*?([^*]*)\*\*?", r"\1", t)
    t = re.sub(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("&", " and ")
    t = re.sub(r"[^\w\s\-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-+", "-", t)
    return t


def fenced_line_numbers(lines):
    inside = False
    fence = None
    out = set()
    for i, line in enumerate(lines):
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


def iter_headings(lines):
    fenced = fenced_line_numbers(lines)
    for i, line in enumerate(lines):
        if i in fenced:
            continue
        m = HEADING_RE.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2).strip()


def first_wikilink(text):
    m = WIKILINK_RE.search(text)
    if not m:
        return None
    return m.group(1).split("|")[0].split("#")[0].strip()


def all_wikilinks(text):
    out = []
    for m in WIKILINK_RE.finditer(text):
        out.append(m.group(1).strip())
    return out


# --- GFM table parsing (self-contained; wikilink/code pipe aware) ---

_TABLE_SEP_CELL_RE = re.compile(r"^:?-{1,}:?$")


def split_table_row(line):
    s = line.strip()
    cells, buf = [], []
    depth = 0
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
            depth += 1
            buf.append("[[")
            i += 2
            continue
        if not in_code and ch == "]" and i + 1 < n and s[i + 1] == "]":
            if depth > 0:
                depth -= 1
            buf.append("]]")
            i += 2
            continue
        if ch == "\\" and i + 1 < n:
            buf.append(s[i:i + 2])
            i += 2
            continue
        if ch == "|" and not in_code and depth == 0:
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
    depth = 0
    in_code = False
    i, n = 0, len(line)
    while i < n:
        ch = line[i]
        if ch == "`":
            in_code = not in_code
            i += 1
            continue
        if not in_code and ch == "[" and i + 1 < n and line[i + 1] == "[":
            depth += 1
            i += 2
            continue
        if not in_code and ch == "]" and i + 1 < n and line[i + 1] == "]":
            if depth > 0:
                depth -= 1
            i += 2
            continue
        if ch == "\\" and i + 1 < n:
            i += 2
            continue
        if ch == "|" and not in_code and depth == 0:
            return True
        i += 1
    return False


def is_separator_row(line):
    cells = split_table_row(line)
    return len(cells) > 0 and all(
        _TABLE_SEP_CELL_RE.match(x.replace(" ", "")) for x in cells)


def iter_tables(lines):
    """Yield (header_idx, header_cells, [(row_idx, cells), ...]) for GFM tables."""
    fenced = fenced_line_numbers(lines)
    i, n = 0, len(lines)
    while i < n:
        if (i not in fenced and lines[i].strip() and _has_cell_pipe(lines[i])
                and i + 1 < n and (i + 1) not in fenced
                and is_separator_row(lines[i + 1])
                and _has_cell_pipe(lines[i + 1])):
            header = split_table_row(lines[i])
            hcount = len(header)
            j = i + 2
            rows = []
            while (j < n and j not in fenced and lines[j].strip()
                   and _has_cell_pipe(lines[j])):
                cells = split_table_row(lines[j])
                if abs(len(cells) - hcount) > 1:
                    break
                rows.append((j, cells))
                j += 1
            yield i, header, rows
            i = j
            continue
        i += 1


def iter_rule_callouts(lines):
    """Yield (start_idx, callout_text, anchor_or_None) for `> [!rule]` blocks."""
    fenced = fenced_line_numbers(lines)
    i, n = 0, len(lines)
    while i < n:
        if i not in fenced and RULE_CALLOUT_RE.match(lines[i]):
            j = i
            body_parts = []
            anchor = None
            while j < n and lines[j].startswith(">"):
                m = BLOCK_ANCHOR_RE.match(lines[j])
                if m:
                    anchor = "^" + m.group(1)
                else:
                    stripped = re.sub(r"^>\s?", "", lines[j])
                    body_parts.append(stripped)
                j += 1
            text = "\n".join(body_parts).strip()
            yield i, text, anchor
            i = j
            continue
        i += 1


def iter_mermaid(lines):
    """Yield (start_idx, block_text) for ```mermaid fenced blocks."""
    i, n = 0, len(lines)
    while i < n:
        s = lines[i].lstrip()
        if s.startswith("```") and "mermaid" in s.lower():
            j = i + 1
            block = []
            while j < n and not lines[j].lstrip().startswith("```"):
                block.append(lines[j])
                j += 1
            yield i, "\n".join(block).strip()
            i = j + 1
            continue
        i += 1


def relpath(path, base=REPO_ROOT):
    try:
        return os.path.relpath(path, base)
    except ValueError:
        return path


# ==========================================================================
# assertion-id + item construction
# ==========================================================================

def _canon(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def _hash(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


class Inventory:
    def __init__(self):
        self.items = []          # list of item dicts (assertion_id filled at finalize)
        self._seen = {}          # base_id -> count (collision disambiguation)

    def add(self, object_class, obj, kind, locator, payload):
        """Register one tracked assertion.

        assertion_id = sha256 over the CONTENT-derived tuple
        (object_class, obj, kind, locator, payload) — no wall-clock, no
        iteration counters — so unchanged content re-derives an identical id.
        Genuine content-identical duplicates within a run get a deterministic
        `occ` suffix (stable because insertion order is document/file order).
        """
        canon = _canon({
            "object_class": object_class,
            "object": obj,
            "kind": kind,
            "locator": locator,
            "payload": payload,
        })
        base_id = _hash(canon)
        occ = self._seen.get(base_id, 0)
        self._seen[base_id] = occ + 1
        if occ == 0:
            aid = base_id[:16]
        else:
            aid = _hash(canon + "|occ=" + str(occ))[:16]
        self.items.append({
            "assertion_id": aid,
            "object_class": object_class,
            "object": obj,
            "kind": kind,
            "locator": locator,
            "payload": payload,
        })
        return aid

    def finalize(self):
        # deterministic order independent of extraction order
        self.items.sort(key=lambda it: (it["assertion_id"], _canon(it)))
        return self.items


# ==========================================================================
# page classification
# ==========================================================================

def classify_page(rel, fm):
    """Return the R2 object_class for a content page (rel is content-relative)."""
    stem = os.path.splitext(os.path.basename(rel))[0]
    ptype = (fm.get("type") or "").strip()
    if ptype == "case":
        return "case"
    if stem == "Common Legal Terms":
        return "glossary"
    if stem == "Case Index":
        return "index"
    if ptype == "doctrine":
        return "doctrine"
    if rel == "index.md" or os.path.basename(rel) == "about.md":
        return "nav"
    if ptype == "index":
        return "nav"          # section landing / map pages
    return "reference"        # reference · practical · craft · hub · other


# ==========================================================================
# per-class extractors
# ==========================================================================

def norm_wikilink(val):
    """[[Page]] / [[Page|d]] / plain -> the bare page target."""
    if not isinstance(val, str):
        return val
    m = WIKILINK_RE.search(val)
    if m:
        return m.group(1).split("|")[0].split("#")[0].strip()
    return val.strip()


def has_official_citation(cite):
    """True only for a genuine reporter citation (volume · reporter · page).

    Mirrors the lake's citations.official/slip_only semantics from the
    frontmatter string alone: slip-/docket-only forms ("No. 23-1197, slip op.
    (U.S. 2026)") have official==null / slip_only==true and must read False.
    bool(cite.strip()) overcounted them because any non-empty string passed.
    """
    c = (cite or "").strip()
    if not c:
        return False
    low = c.lower()
    if "slip op" in low or low.startswith("no."):
        return False
    return bool(REPORTER_CITE_RE.search(c))


def extract_case_page(inv, rel, fm, body):
    oc = "case"
    title = fm.get("title") or os.path.splitext(os.path.basename(rel))[0]

    # case_cite — emitted for EVERY case that carries any citation data so the
    # exhaustiveness gate can verdict the cite (incl. the pages whose OFFICIAL
    # U.S. slot is unselected but whose official cite sits in parallel_cite; a
    # real S2 selection gap that must not silently vanish from the inventory).
    cite = str(fm.get("citation") or "")
    parallel = str(fm.get("parallel_cite") or "")
    neutral = str(fm.get("neutral_cite") or "")
    if cite.strip() or parallel.strip() or neutral.strip():
        inv.add(oc, rel, "case_cite", {"field": "citation"}, {
            "title": title,
            "citation": cite,
            "parallel_cite": parallel,
            "neutral_cite": neutral,
            "court": fm.get("court") or "",
            "year": fm.get("year"),
            "official_citation_present": has_official_citation(cite),
        })

    # proposition (the taught holding)
    holding = fm.get("holding")
    if isinstance(holding, str) and holding.strip():
        inv.add(oc, rel, "proposition", {"field": "holding"},
                {"title": title, "holding": holding})

    # weight_label
    aw = fm.get("authority_weight")
    if isinstance(aw, str) and aw.strip():
        inv.add(oc, rel, "weight_label", {"field": "authority_weight"},
                {"title": title, "authority_weight": aw})

    # treatment (base block) + per point_override
    tr = fm.get("treatment")
    if isinstance(tr, dict) and tr:
        base = {k: tr.get(k) for k in (
            "field_i_validity", "as_of_content", "as_of_treatment",
            "composite_basis", "composite_basis_ref", "varies_by_point",
            "scope_note")}
        inv.add(oc, rel, "treatment", {"field": "treatment"},
                {"title": title, **base})
        povr = tr.get("point_overrides")
        if isinstance(povr, list):
            for ov in povr:
                if not isinstance(ov, dict):
                    continue
                by = ov.get("by") if isinstance(ov.get("by"), list) else []
                by_norm = [{"name": b.get("name"), "cite": b.get("cite"),
                            "cluster_id": b.get("cluster_id"),
                            "field_ii": b.get("field_ii")}
                           for b in by if isinstance(b, dict)]
                inv.add(oc, rel, "treatment_override",
                        {"point": ov.get("point")}, {
                            "title": title,
                            "point": ov.get("point"),
                            "point_label": ov.get("point_label"),
                            "field_i_validity": ov.get("field_i_validity"),
                            "s3_binding_status": ov.get("s3_binding_status"),
                            "by": by_norm,
                        })

    # homes/roles
    homes = fm.get("homes")
    if isinstance(homes, list):
        for h in homes:
            if isinstance(h, dict) and h.get("page"):
                inv.add(oc, rel, "home_role",
                        {"home": norm_wikilink(h.get("page"))}, {
                            "title": title,
                            "home": norm_wikilink(h.get("page")),
                            "role": h.get("role") or "",
                        })

    # link_target — the CourtListener identity link
    cl = fm.get("courtlistener")
    if isinstance(cl, dict) and cl.get("opinion_url"):
        inv.add(oc, rel, "link_target", {"field": "courtlistener.opinion_url"}, {
            "title": title,
            "opinion_url": cl.get("opinion_url"),
            "cluster_id": cl.get("cluster_id"),
            "opinion_id": cl.get("opinion_id"),
            "identity_checked": cl.get("identity_checked"),
        })

    # generic body assertions (case pages rarely carry these, but stay honest)
    extract_page_body(inv, oc, rel, body)


def _row_is_case(header):
    if not header:
        return False
    h0 = re.sub(r"[^a-z ]", "", header[0].lower()).strip()
    return h0 == "case" or "case" in h0.split()


def extract_page_body(inv, oc, rel, body):
    """Callouts (propositions) · case-tables (case_cites) · mermaid blocks."""
    lines = body.split("\n")

    for start, text, anchor in iter_rule_callouts(lines):
        if not text:
            continue
        inv.add(oc, rel, "proposition",
                {"callout": anchor or ("line-" + str(start + 1))},
                {"anchor": anchor, "statement": text})

    for hidx, header, rows in iter_tables(lines):
        if not _row_is_case(header):
            continue
        for ridx, cells in rows:
            first = cells[0] if cells else ""
            case_tgt = first_wikilink(first)
            if not case_tgt:
                continue
            payload = {"case": case_tgt, "cells": cells, "header": header}
            inv.add(oc, rel, "case_cite", {"case": case_tgt, "table_line": ridx + 1},
                    payload)

    for start, block in iter_mermaid(lines):
        inv.add(oc, rel, "mermaid", {"line": start + 1},
                {"block_sha256": _hash(block), "lines": block.count("\n") + 1})


def extract_glossary(inv, rel, fm, body):
    oc = "glossary"
    lines = body.split("\n")
    heads = list(iter_headings(lines))
    for k, (i, lvl, txt) in enumerate(heads):
        if lvl != 3:
            continue
        end = len(lines)
        for (i2, lvl2, _t2) in heads[k + 1:]:
            if lvl2 <= 3:
                end = i2
                break
        definition = "\n".join(lines[i + 1:end]).strip()
        inv.add(oc, rel, "definition", {"term": txt, "slug": slugify(txt)},
                {"term": txt, "definition": definition})
    # a glossary is also a nav-ish reference; capture nothing else


def extract_case_index(inv, rel, fm, body):
    oc = "index"
    lines = body.split("\n")
    for hidx, header, rows in iter_tables(lines):
        if not _row_is_case(header):
            continue
        # map columns by role heuristics
        hnorm = [re.sub(r"[^a-z ]", "", c.lower()).strip() for c in header]

        def col(*names):
            for idx, hn in enumerate(hnorm):
                for nm in names:
                    if nm in hn:
                        return idx
            return None

        c_case = 0
        c_hold = col("holding")
        c_good = col("good law", "good", "status")
        c_home = col("home", "primary")
        c_cl = col("courtlistener", "opinion", "cl", "link")
        for ridx, cells in rows:
            case_tgt = first_wikilink(cells[c_case]) if cells else None
            if not case_tgt:
                continue

            def cell(idx):
                return cells[idx] if idx is not None and idx < len(cells) else None
            homes = all_wikilinks(cell(c_home) or "")
            inv.add(oc, rel, "index_row", {"case": case_tgt}, {
                "case": case_tgt,
                "holding": cell(c_hold),
                "good_law": cell(c_good),
                "homes": homes,
                "courtlistener": cell(c_cl),
            })


def extract_nav(inv, rel, fm, body):
    oc = "nav"
    lines = body.split("\n")
    fenced = fenced_line_numbers(lines)
    # internal placements: first wikilink of each list item
    for i, line in enumerate(lines):
        if i in fenced:
            continue
        if LISTITEM_RE.match(line):
            tgt = first_wikilink(line)
            if tgt:
                inv.add(oc, rel, "link_target",
                        {"kind": "nav-placement", "target": tgt, "line": i + 1},
                        {"target": tgt})
    # external references (dedup by URL, first line wins)
    seen = set()
    for i, line in enumerate(lines):
        if i in fenced:
            continue
        for m in MDLINK_URL_RE.finditer(line):
            url = m.group(2)
            if url in seen:
                continue
            seen.add(url)
            inv.add(oc, rel, "link_target",
                    {"kind": "external", "url": url},
                    {"url": url, "text": m.group(1)})


def extract_lake_record(inv, path, rec):
    oc = "lake-record"
    rid = rec.get("record_id") or os.path.splitext(os.path.basename(path))[0]
    obj = relpath(path)
    ident = rec.get("identity") or {}

    # case_cite (canonical, from the lake citations block) — emitted whenever any
    # citation data exists (display OR official OR the parallel `all` list), so a
    # record with an unselected official slot still yields a trackable cite.
    cits = rec.get("citations") or {}
    display = cits.get("display")
    official = cits.get("official")
    allc = cits.get("all") if isinstance(cits.get("all"), list) else None
    if display or official or allc:
        inv.add(oc, obj, "case_cite", {"record_id": rid}, {
            "record_id": rid,
            "display": display,
            "official": official,
            "all": allc,
            "official_selection_present": bool(display or official),
        })

    # identity / link_target (cluster + lead opinion + absolute_url)
    if ident:
        inv.add(oc, obj, "link_target", {"record_id": rid, "field": "identity"}, {
            "record_id": rid,
            "case_name": ident.get("case_name"),
            "cluster_id": ident.get("cluster_id"),
            "lead_opinion_id": ident.get("lead_opinion_id"),
            "absolute_url": ident.get("absolute_url"),
            "identity_method": ident.get("identity_method"),
        })

    # treatment
    tr = rec.get("treatment") or {}
    if tr:
        inv.add(oc, obj, "treatment", {"record_id": rid}, {
            "record_id": rid,
            "field_i_validity": tr.get("field_i_validity"),
            "as_of_content": tr.get("as_of_content"),
            "as_of_treatment": tr.get("as_of_treatment"),
            "varies_by_point": tr.get("varies_by_point"),
            "scope_note": tr.get("scope_note"),
        })

    # quote_pinpoint (the canonical quote+pinpoint+status+fragment source)
    for pp in rec.get("pinpoints") or []:
        if not isinstance(pp, dict):
            continue
        pin_id = pp.get("id")
        inv.add(oc, obj, "quote_pinpoint", {"record_id": rid, "pin_id": pin_id}, {
            "record_id": rid,
            "pin_id": pin_id,
            "quote": pp.get("quote"),
            "page": pp.get("page"),
            "star_marker": pp.get("star_marker"),
            "quote_fidelity": pp.get("quote_fidelity"),
            "pinpoint_status": pp.get("pinpoint_status"),
            "fragment": pp.get("fragment"),
        })


def extract_registry(inv, path):
    data = parse_yaml_file(path)
    obj = relpath(path)
    nodes = data.get("nodes") if isinstance(data, dict) else None
    if not isinstance(nodes, list):
        return
    for nd in nodes:
        if not isinstance(nd, dict) or not nd.get("id"):
            continue
        also = nd.get("also_on")
        also = also if isinstance(also, list) else []
        inv.add("registry", obj, "registry_callout_pair", {"id": nd.get("id")}, {
            "id": nd.get("id"),
            "label": nd.get("label"),
            "statement": nd.get("statement"),
            "home_page": nd.get("home_page"),
            "also_on": also,
            "status": nd.get("status"),
        })


def extract_s6_ledger(inv, path):
    if not os.path.exists(path):
        return
    data = json.loads(read_text(path))
    obj = relpath(path)
    for row in data.get("rows") or []:
        if not isinstance(row, dict):
            continue
        gate = row.get("gate") if isinstance(row.get("gate"), dict) else {}
        inv.add("ledger-row", obj, "coverage_row",
                {"caption": row.get("caption")}, {
                    "caption": row.get("caption"),
                    "terminal": row.get("terminal"),
                    "page_backed": row.get("page_backed"),
                    "pointer": row.get("pointer"),
                    "gate_verdict": gate.get("verdict"),
                })


def extract_s8_ledger(inv, path):
    if not os.path.exists(path):
        return
    data = json.loads(read_text(path))
    obj = relpath(path)

    for row in data.get("mentions") or []:
        if not isinstance(row, dict):
            continue
        res = row.get("resolution") if isinstance(row.get("resolution"), dict) else {}
        inv.add("ledger-row", obj, "link_mention",
                {"file": row.get("file"), "line": row.get("line"),
                 "matched_text": row.get("matched_text")}, {
                    "file": row.get("file"),
                    "line": row.get("line"),
                    "matched_text": row.get("matched_text"),
                    "action": row.get("action"),
                    "target": res.get("target"),
                    "method": res.get("method"),
                })

    for row in data.get("pincites") or []:
        if not isinstance(row, dict):
            continue
        inv.add("ledger-row", obj, "link_pincite",
                {"record_id": row.get("record_id"), "pin_id": row.get("pin_id"),
                 "file": row.get("file")}, {
                    "record_id": row.get("record_id"),
                    "pin_id": row.get("pin_id"),
                    "file": row.get("file"),
                    "form": row.get("form"),
                    "action": row.get("action"),
                    "scope": row.get("scope"),
                })

    for row in data.get("embeds") or []:
        if not isinstance(row, dict):
            continue
        inv.add("ledger-row", obj, "link_embed",
                {"file": row.get("file"), "line": row.get("line"),
                 "target": row.get("target"), "anchor": row.get("anchor")}, {
                    "file": row.get("file"),
                    "line": row.get("line"),
                    "target": row.get("target"),
                    "anchor": row.get("anchor"),
                    "full_slug": row.get("full_slug"),
                })

    terms = data.get("terms") if isinstance(data.get("terms"), dict) else {}
    pages = terms.get("pages") if isinstance(terms.get("pages"), dict) else {}
    for page_key in sorted(pages.keys()):
        info = pages[page_key]
        if not isinstance(info, dict):
            continue
        inv.add("ledger-row", obj, "link_term_page", {"page": page_key}, {
            "page": page_key,
            "class": info.get("class"),
            "links": info.get("links"),
            "by_route": info.get("by_route"),
        })


# ==========================================================================
# build
# ==========================================================================

def build_inventory(roots):
    inv = Inventory()

    # -- content pages --
    md_paths = sorted(_glob.glob(os.path.join(roots.content, "**", "*.md"),
                                 recursive=True))
    for path in md_paths:
        rel = relpath(path, roots.content)
        text = read_text(path)
        fm, body, _ = split_frontmatter(text)
        oc = classify_page(rel, fm)
        content_obj = "content/" + rel.replace(os.sep, "/")
        if oc == "case":
            extract_case_page(inv, content_obj, fm, body)
        elif oc == "glossary":
            extract_glossary(inv, content_obj, fm, body)
        elif oc == "index":
            extract_case_index(inv, content_obj, fm, body)
        elif oc == "nav":
            extract_nav(inv, content_obj, fm, body)
        else:  # doctrine · reference
            extract_page_body(inv, oc, content_obj, body)

    # -- lake records --
    lake_paths = sorted(_glob.glob(os.path.join(roots.lake, "*.json")))
    for path in lake_paths:
        try:
            rec = json.loads(read_text(path))
        except (ValueError, OSError):
            continue
        extract_lake_record(inv, path, rec)

    # -- registry --
    if os.path.exists(roots.registry):
        extract_registry(inv, roots.registry)

    # -- ledgers --
    extract_s6_ledger(inv, roots.s6_ledger)
    extract_s8_ledger(inv, roots.s8_ledger)

    return inv.finalize()


def corpus_head():
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                             capture_output=True, text=True, timeout=15)
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "unknown"


def counts_by(items, key):
    out = {}
    for it in items:
        out[it[key]] = out.get(it[key], 0) + 1
    return dict(sorted(out.items()))


def counts_class_kind(items):
    out = {}
    for it in items:
        k = it["object_class"] + "/" + it["kind"]
        out[k] = out.get(k, 0) + 1
    return dict(sorted(out.items()))


def assemble(items, now, head):
    body_hash = _hash("\n".join(_canon(it) for it in items))
    return {
        "schema": SCHEMA,
        "spec": SPEC,
        "generated": now,
        "lane": LANE,
        "model": MODEL,
        "corpus_head": head,
        "count": len(items),
        "counts_by_object_class": counts_by(items, "object_class"),
        "counts_by_kind": counts_by(items, "kind"),
        "counts_by_class_kind": counts_class_kind(items),
        "body_sha256": body_hash,
        "items": items,
    }


def write_doc(doc, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    header_keys = [k for k in doc if k != "items"]
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("{\n")
        for k in header_keys:
            fh.write("  " + json.dumps(k) + ": "
                     + json.dumps(doc[k], ensure_ascii=False, sort_keys=True)
                     + ",\n")
        fh.write('  "items": [\n')
        n = len(doc["items"])
        for idx, it in enumerate(doc["items"]):
            line = json.dumps(it, ensure_ascii=False, sort_keys=True)
            fh.write("    " + line + ("," if idx < n - 1 else "") + "\n")
        fh.write("  ]\n}\n")


# ==========================================================================
# self-test (fixtures only; no corpus read, no write)
# ==========================================================================

EXPECT_CLASS_KIND = {
    "case/case_cite": 1,
    "case/proposition": 1,
    "case/weight_label": 1,
    "case/treatment": 1,
    "case/treatment_override": 1,
    "case/home_role": 2,
    "case/link_target": 1,
    "doctrine/proposition": 1,
    "doctrine/case_cite": 3,
    "doctrine/mermaid": 1,
    "glossary/definition": 2,
    "index/index_row": 2,
    "nav/link_target": 3,           # 2 wikilinks + 1 external (CourtListener)
    "lake-record/case_cite": 1,
    "lake-record/link_target": 1,
    "lake-record/treatment": 1,
    "lake-record/quote_pinpoint": 2,
    "registry/registry_callout_pair": 1,
    "ledger-row/coverage_row": 2,
    "ledger-row/link_mention": 2,
    "ledger-row/link_pincite": 1,
    "ledger-row/link_embed": 1,
    "ledger-row/link_term_page": 1,
}


def self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    roots = Roots.fixtures()
    items1 = build_inventory(roots)
    ck = counts_class_kind(items1)

    # 1. per-class/kind counts exactly as designed
    for key, want in EXPECT_CLASS_KIND.items():
        got = ck.get(key, 0)
        check(got == want, "count %s: want %d got %d" % (key, want, got))
    extra = set(ck) - set(EXPECT_CLASS_KIND)
    check(not extra, "unexpected class/kind buckets: %s" % sorted(extra))
    total_want = sum(EXPECT_CLASS_KIND.values())
    check(len(items1) == total_want,
          "total items: want %d got %d" % (total_want, len(items1)))

    # 2. every item well-formed
    for it in items1:
        for f in ("assertion_id", "object_class", "object", "kind",
                  "locator", "payload"):
            check(f in it, "item missing field %s: %r" % (f, it))
        check(len(it["assertion_id"]) == 16, "id not 16 hex: %r" % it["assertion_id"])

    # 3. all ids unique
    ids = [it["assertion_id"] for it in items1]
    check(len(ids) == len(set(ids)), "duplicate assertion_ids present")

    # 4. id-stability: a second build re-derives identical ids + body hash
    items2 = build_inventory(roots)
    h1 = _hash("\n".join(_canon(it) for it in items1))
    h2 = _hash("\n".join(_canon(it) for it in items2))
    check(h1 == h2, "body_sha256 not stable across runs")
    check([it["assertion_id"] for it in items2] == ids,
          "assertion_id order/set not stable across runs")

    # 5. content-sensitivity: change a case citation -> that item's id changes,
    #    while an untouched item's id is unchanged (content-hash discipline)
    inv_a = Inventory()
    extract_case_page(inv_a, "content/cases/X.md",
                      {"title": "X", "citation": "1 U.S. 1 (1900)",
                       "holding": "H"}, "")
    inv_b = Inventory()
    extract_case_page(inv_b, "content/cases/X.md",
                      {"title": "X", "citation": "2 U.S. 2 (1901)",
                       "holding": "H"}, "")
    a_items = {it["kind"]: it for it in inv_a.finalize()}
    b_items = {it["kind"]: it for it in inv_b.finalize()}
    check(a_items["case_cite"]["assertion_id"]
          != b_items["case_cite"]["assertion_id"],
          "citation change did not change case_cite id")
    check(a_items["proposition"]["assertion_id"]
          == b_items["proposition"]["assertion_id"],
          "untouched holding id changed")

    # 6. collision disambiguation: two content-identical adds get distinct ids
    inv_c = Inventory()
    inv_c.add("x", "o", "k", {"l": 1}, {"p": 1})
    inv_c.add("x", "o", "k", {"l": 1}, {"p": 1})
    cids = [it["assertion_id"] for it in inv_c.finalize()]
    check(len(set(cids)) == 2, "collision disambiguation failed")

    if failures:
        sys.stderr.write("SELF-TEST FAIL (%d):\n" % len(failures))
        for f in failures:
            sys.stderr.write("  - " + f + "\n")
        return 1
    sys.stderr.write(
        "SELF-TEST PASS — %d items, %d class/kind buckets, ids stable+unique, "
        "content-sensitive, collision-safe\n" % (len(items1), len(ck)))
    return 0


# ==========================================================================
# CLI
# ==========================================================================

def main():
    ap = argparse.ArgumentParser(description="S9 P0-A assertion inventory (R2)")
    ap.add_argument("--self-test", action="store_true",
                    help="run the fixtures self-test (no corpus, no write)")
    ap.add_argument("--report", action="store_true",
                    help="print a human report (counts + samples) to stderr")
    ap.add_argument("--stdout", action="store_true",
                    help="print the JSON to stdout instead of writing the file")
    ap.add_argument("--now", default=None,
                    help="pin the header 'generated' timestamp (determinism)")
    ap.add_argument("--corpus-head", default=None,
                    help="override the corpus_head stamp")
    ap.add_argument("--out", default=None, help="output path override")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(self_test())

    roots = Roots()
    items = build_inventory(roots)
    now = args.now or datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    head = args.corpus_head or corpus_head()
    doc = assemble(items, now, head)

    out_path = args.out or os.path.join(REPO_ROOT, "_run", "s9",
                                        "assertion-inventory.json")

    if args.stdout:
        json.dump(doc, sys.stdout, ensure_ascii=False, sort_keys=True, indent=1)
        sys.stdout.write("\n")
    else:
        write_doc(doc, out_path)
        sys.stderr.write("wrote %s (%d items, body_sha256 %s)\n" % (
            relpath(out_path), len(items), doc["body_sha256"][:12]))

    if args.report:
        emit_report(doc)


def emit_report(doc):
    w = sys.stderr.write
    w("\n==== assertion inventory report ====\n")
    w("corpus_head: %s\n" % doc["corpus_head"])
    w("total items: %d   body_sha256: %s\n" % (doc["count"], doc["body_sha256"]))
    w("\n-- counts by object_class --\n")
    for k, v in doc["counts_by_object_class"].items():
        w("  %-14s %6d\n" % (k, v))
    w("\n-- counts by kind --\n")
    for k, v in doc["counts_by_kind"].items():
        w("  %-22s %6d\n" % (k, v))


if __name__ == "__main__":
    main()
