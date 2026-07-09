#!/usr/bin/env python3
"""S9 Lane P0-B — Thread P freeze (spec S9 R5).

Deterministically extract the BUILT corpus's CONCLUSIONS (what the corpus
CLAIMS, with NO judgment of correctness) into a frozen, hash-stamped
``thread-P.json`` + ``thread-P.sha256`` sidecar. Thread P is the baseline the
Thread-N blind re-derivation is later reconciled against; every P item must be
dispositioned by the concordance (the no-regression floor).

Extraction (spec R5):
  * per case  (page frontmatter + lake record): holding/disposition,
    treatment on taught points, homes/roles, split positions.
  * per doctrine page: case-set (homed cases + roles) + split calls.

Partition (deterministic, covers 100% of built content pages):
  * case row     <=> frontmatter ``type: case``.
  * doctrine row <=> every other ``content/**/*.md`` page (index/reference/hub/
    practical/craft/none included; each row records its ``type`` so downstream
    can scope doctrine-grain re-derivation). This makes the floor == the build
    page count and guarantees zero silent absences at the page grain.

Freeze semantics:
  * item ``p_id`` is derived from the page's repo-relative path (stable
    identity: same page => same id across content edits and across re-runs).
  * ``content_hash`` = sha256 over the canonical JSON of the sorted ``items``
    array (compact, sort_keys, utf-8). It lands in BOTH the header and the
    ``.sha256`` sidecar. The ``generated`` timestamp is metadata and is NOT
    hashed, so the freeze hash is idempotent on unchanged corpus content.

Constraints: Python stdlib only; content/lake are read-only; deterministic
(no nondeterminism in ids or in the hashed body).

Usage:
  build_thread_p.py [--content DIR] [--lake DIR] [--out FILE] [--repo DIR]
                    [--now ISO8601] [--report]
  build_thread_p.py --self-test
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import subprocess
import sys

SCHEMA = "s9.thread-p.v1"
LANE = "P0-B"
MODEL = "claude-opus-4-8"

# --------------------------------------------------------------------------
# Minimal YAML-subset parser (frontmatter only; single-line scalars).
# Handles: block maps, block sequences (scalar items + map items, incl. nested
# sequences), inline flow lists, quoted/plain scalars, bools, ints.
# --------------------------------------------------------------------------


class MiniYAMLError(Exception):
    pass


def _scalar(tok: str):
    """Parse a single scalar token (already whitespace-stripped)."""
    if tok == "" or tok == "~" or tok == "null":
        return None
    if tok == "[]":
        return []
    if tok == "{}":
        return {}
    if tok.startswith("[") and tok.endswith("]"):
        return _flow_list(tok[1:-1])
    if len(tok) >= 2 and tok[0] == tok[-1] and tok[0] in ("'", '"'):
        inner = tok[1:-1]
        if tok[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\\\", "\\")
        else:
            inner = inner.replace("''", "'")
        return inner
    if tok in ("true", "True"):
        return True
    if tok in ("false", "False"):
        return False
    if re.fullmatch(r"-?\d+", tok):
        try:
            return int(tok)
        except ValueError:
            return tok
    return tok


def _flow_list(body: str):
    """Split a flow-list body on top-level commas (respecting quotes)."""
    out, buf, depth, quote = [], [], 0, None
    for ch in body:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ("'", '"'):
            quote = ch
            buf.append(ch)
        elif ch in "[{":
            depth += 1
            buf.append(ch)
        elif ch in "]}":
            depth -= 1
            buf.append(ch)
        elif ch == "," and depth == 0:
            out.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        out.append(tail)
    return [_scalar(x) for x in out if x != ""]


def _split_key(line: str):
    """Split 'key: value' respecting a quoted value that may contain ':'.

    Returns (key, value_str) or None if the line is not a mapping entry.
    """
    m = re.match(r"^([^\s:][^:]*?):(\s|$)", line)
    if not m:
        return None
    key = m.group(1).strip()
    rest = line[m.end(1) + 1:]
    return key, rest.strip()


def parse_yaml(lines):
    """Parse a list of raw frontmatter lines into a Python object."""
    rows = []
    for raw in lines:
        if raw.strip() == "" or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        rows.append((indent, raw.rstrip("\n")))
    val, idx = _parse_block(rows, 0, rows[0][0] if rows else 0)
    if idx != len(rows):
        raise MiniYAMLError("trailing unparsed frontmatter lines at %d" % idx)
    return val


def _parse_block(rows, i, indent):
    if i >= len(rows):
        return None, i
    _, content = rows[i]
    stripped = content.lstrip(" ")
    if stripped.startswith("- "):
        return _parse_seq(rows, i, indent)
    if stripped == "-":
        return _parse_seq(rows, i, indent)
    return _parse_map(rows, i, indent)


def _parse_map(rows, i, indent):
    out = {}
    while i < len(rows):
        cur_indent, content = rows[i]
        if cur_indent < indent:
            break
        if cur_indent > indent:
            raise MiniYAMLError("unexpected indent in map: %r" % content)
        kv = _split_key(content.lstrip(" "))
        if kv is None:
            raise MiniYAMLError("expected mapping entry: %r" % content)
        key, vstr = kv
        if vstr != "":
            out[key] = _scalar(vstr)
            i += 1
        else:
            # value is a nested block (deeper indent) or null.
            if i + 1 < len(rows) and rows[i + 1][0] > indent:
                child_indent = rows[i + 1][0]
                sub_stripped = rows[i + 1][1].lstrip(" ")
                if sub_stripped.startswith("- ") or sub_stripped == "-":
                    # a sequence may be indented at the SAME indent as the key
                    # in canonical YAML, but here children are deeper; handle
                    # both by delegating to _parse_block at the child indent.
                    val, i = _parse_block(rows, i + 1, child_indent)
                else:
                    val, i = _parse_block(rows, i + 1, child_indent)
                out[key] = val
            elif i + 1 < len(rows) and rows[i + 1][0] == indent and \
                    rows[i + 1][1].lstrip(" ").startswith("- "):
                # sequence at same indent as its key.
                val, i = _parse_seq(rows, i + 1, indent)
                out[key] = val
            else:
                out[key] = None
                i += 1
    return out, i


def _parse_seq(rows, i, indent):
    out = []
    while i < len(rows):
        cur_indent, content = rows[i]
        if cur_indent != indent:
            break
        stripped = content.lstrip(" ")
        if not (stripped.startswith("- ") or stripped == "-"):
            break
        if stripped == "-":
            # item body is a nested block on following deeper lines.
            if i + 1 < len(rows) and rows[i + 1][0] > indent:
                val, i = _parse_block(rows, i + 1, rows[i + 1][0])
                out.append(val)
            else:
                out.append(None)
                i += 1
            continue
        after = stripped[2:]
        item_indent = indent + 2  # column where the item content begins
        kv = _split_key(after)
        if kv is not None:
            # sequence item is a mapping; reconstruct its first line and any
            # continuation lines that are indented past item_indent.
            block = [(item_indent, (" " * item_indent) + after)]
            i += 1
            while i < len(rows) and rows[i][0] >= item_indent and \
                    not rows[i][1].lstrip(" ").startswith("- ") or \
                    (i < len(rows) and rows[i][0] > item_indent):
                # include deeper-or-equal map keys and any nested seq/maps
                if rows[i][0] < item_indent:
                    break
                block.append(rows[i])
                i += 1
            val, _ = _parse_map(block, 0, item_indent)
            out.append(val)
        else:
            out.append(_scalar(after))
            i += 1
    return out, i


# --------------------------------------------------------------------------
# Frontmatter + wikilink helpers
# --------------------------------------------------------------------------


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def split_frontmatter(text):
    """Return (frontmatter_lines, body_text, body_start_line[1-based])."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return [], text, 1
    for j in range(1, len(lines)):
        if lines[j].strip() == "---":
            fm_lines = lines[1:j]
            body = "\n".join(lines[j + 1:])
            return fm_lines, body, j + 2
    return [], text, 1


def frontmatter(text):
    fm_lines, body, body_start = split_frontmatter(text)
    if not fm_lines:
        return {}, body, body_start
    try:
        data = parse_yaml(fm_lines)
    except MiniYAMLError as exc:
        raise MiniYAMLError("frontmatter parse: %s" % exc)
    if not isinstance(data, dict):
        data = {}
    return data, body, body_start


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def wikilink_target(raw):
    """Extract the resolvable target from a raw '[[Target|display]]' string."""
    s = raw.strip()
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1)
    s = s.split("|", 1)[0]
    s = s.split("#", 1)[0]
    return s.strip()


def build_link_index(pages):
    """pages: list of (relpath, frontmatter). Returns resolver dict."""
    stem, title, alias = {}, {}, {}
    for rel, fm in pages:
        st = os.path.splitext(os.path.basename(rel))[0]
        stem.setdefault(st, []).append(rel)
        t = fm.get("title")
        if isinstance(t, str):
            title.setdefault(t, []).append(rel)
        al = fm.get("aliases")
        if isinstance(al, list):
            for a in al:
                if isinstance(a, str):
                    alias.setdefault(a, []).append(rel)
    return {"stem": stem, "title": title, "alias": alias}


def resolve_link(target, index):
    for key in ("stem", "title", "alias"):
        hits = index[key].get(target)
        if hits and len(hits) == 1:
            return hits[0]
        if hits and len(hits) > 1:
            return None  # ambiguous
    return None


# --------------------------------------------------------------------------
# Split-call extraction (doctrine pages)
# --------------------------------------------------------------------------

SPLIT_SIGNAL_RE = re.compile(
    r"\bcircuit split\b"
    r"|\bsplit of authority\b"
    r"|\bcircuits?\b.{0,40}\bsplit"
    r"|\bsplit\b.{0,40}\bcircuit"
    r"|\bsplitting from\b"
    r"|\bcircuits?\s+(?:fractur|are divided|divide)"
    r"|\bunresolved\b.{0,40}\bsplit\b"
    r"|\bthe split\b",
    re.IGNORECASE,
)

CIRCUIT_LABEL_RE = re.compile(
    r"\*\*(Binding in-circuit|Persuasive[^*]*|Binding — SCOTUS)[^*]*\*\*"
)
CIRCUIT_ORD_RE = re.compile(
    r"—\s*((?:\d+(?:st|nd|rd|th)|D\.C\.|Fed\.|2d|3d)\s*Cir\.)"
)


def _is_case_path(p):
    return isinstance(p, str) and p.startswith("cases/")


def extract_splits(body, body_start, link_index):
    signal_lines = []
    circuit_positions = []
    for off, line in enumerate(body.split("\n")):
        lineno = body_start + off
        if SPLIT_SIGNAL_RE.search(line):
            txt = line.strip()
            if txt:
                signal_lines.append({"line": lineno, "text": txt})
        lab = CIRCUIT_LABEL_RE.search(line)
        wls = WIKILINK_RE.findall(line)
        if lab and wls and ("in-circuit" in lab.group(0) or "Persuasive" in lab.group(0)):
            ordm = CIRCUIT_ORD_RE.search(line)
            # Prefer the first wikilink on the line that resolves to a case
            # page (a case-table row may cross-reference a doctrine page first).
            chosen_tgt, chosen_path = None, None
            for w in wls:
                tgt = wikilink_target("[[" + w + "]]")
                path = resolve_link(tgt, link_index)
                if _is_case_path(path):
                    chosen_tgt, chosen_path = tgt, path
                    break
            if chosen_tgt is None:
                chosen_tgt = wikilink_target("[[" + wls[0] + "]]")
                chosen_path = resolve_link(chosen_tgt, link_index)
            circuit_positions.append({
                "case": chosen_tgt,
                "resolved_case_path": chosen_path,
                "label": lab.group(0).strip("* "),
                "circuit": ordm.group(1).strip() if ordm else None,
                "line": lineno,
            })
    return {
        "has_split_signal": bool(signal_lines),
        "signal_lines": signal_lines,
        "circuit_positions": circuit_positions,
    }


# --------------------------------------------------------------------------
# Item builders
# --------------------------------------------------------------------------

NEGATIVE_FIELD_II = {
    "overruled", "abrogated", "superseded", "superseded_by_statute",
    "questioned", "criticized", "limited", "called_into_doubt",
}


def pid(kind, rel):
    h = hashlib.sha256(rel.encode("utf-8")).hexdigest()[:12]
    return "P-%s-%s" % (kind[0], h)


def compact_point_overrides(pos):
    out = []
    for po in pos or []:
        if not isinstance(po, dict):
            continue
        by = []
        for b in po.get("by") or []:
            if isinstance(b, dict):
                by.append({
                    "name": b.get("name"),
                    "cite": b.get("cite"),
                    "cluster_id": b.get("cluster_id"),
                    "field_ii": b.get("field_ii"),
                })
        out.append({
            "point": po.get("point"),
            "point_label": po.get("point_label"),
            "field_i_validity": po.get("field_i_validity"),
            "s3_binding_status": po.get("s3_binding_status"),
            "by": by,
            "scope_note": po.get("scope_note"),
        })
    return out


def build_case_item(rel, fm, link_index, lake_dir):
    tr = fm.get("treatment") or {}
    homes = []
    for h in fm.get("homes") or []:
        if not isinstance(h, dict):
            continue
        page = h.get("page")
        homes.append({
            "page": page,
            "role": h.get("role"),
            "resolved_path": resolve_link(wikilink_target(page), link_index)
            if isinstance(page, str) else None,
        })
    related = [r for r in (fm.get("related") or []) if isinstance(r, str)]

    lake_block = None
    lref = fm.get("lake") or {}
    rid = lref.get("record_id") if isinstance(lref, dict) else None
    if isinstance(rid, str):
        lpath = os.path.join(lake_dir, rid + ".json")
        if os.path.exists(lpath):
            rec = json.load(open(lpath, encoding="utf-8"))
            ltr = rec.get("treatment") or {}
            f2 = {}
            for e in ltr.get("edges") or []:
                k = e.get("field_ii")
                f2[k] = f2.get(k, 0) + 1
            lake_block = {
                "record_id": rec.get("record_id"),
                "status": rec.get("status"),
                "cluster_id": (rec.get("identity") or {}).get("cluster_id"),
                "lead_opinion_id": (rec.get("identity") or {}).get("lead_opinion_id"),
                "court_level": (rec.get("identity") or {}).get("court_level"),
                "field_i_validity": ltr.get("field_i_validity"),
                "varies_by_point": ltr.get("varies_by_point"),
                "point_overrides": compact_point_overrides(ltr.get("point_overrides")),
                "treatment_edge_count": len(ltr.get("edges") or []),
                "treatment_edge_field_ii": {k: f2[k] for k in sorted(f2)},
                "treatment_edges_all_proposed": all(
                    (e.get("proposed") is True) for e in (ltr.get("edges") or [])
                ) if ltr.get("edges") else None,
            }
        else:
            lake_block = {"record_id": rid, "status": lref.get("status"),
                          "missing_lake_file": True}

    holding = fm.get("holding")
    return {
        "p_id": pid("case", rel),
        "kind": "case",
        "path": rel,
        "title": fm.get("title"),
        "citation": fm.get("citation"),
        "court": fm.get("court"),
        "court_level": fm.get("court_level"),
        "year": fm.get("year"),
        "weight_label": fm.get("authority_weight"),
        "holding": holding,
        "holding_present": isinstance(holding, str) and holding.strip() != "",
        "treatment": {
            "field_i_validity": tr.get("field_i_validity"),
            "as_of_content": tr.get("as_of_content"),
            "as_of_treatment": tr.get("as_of_treatment"),
            "varies_by_point": tr.get("varies_by_point"),
            "scope_note": tr.get("scope_note"),
            "point_overrides": compact_point_overrides(tr.get("point_overrides")),
        },
        "homes": homes,
        "related": related,
        "lake": lake_block,
    }


def build_doctrine_item(rel, fm, body, body_start, reverse_homes, link_index):
    linked = set()
    for m in WIKILINK_RE.finditer(body):
        tgt = wikilink_target("[[" + m.group(1) + "]]")
        p = resolve_link(tgt, link_index)
        if p and p.startswith("cases/") or (p and "/cases/" in ("/" + p)):
            linked.add(p)
    homed = sorted(reverse_homes.get(rel, []), key=lambda x: x["case_path"])
    return {
        "p_id": pid("doctrine", rel),
        "kind": "doctrine",
        "path": rel,
        "title": fm.get("title"),
        "type": fm.get("type"),
        "topic": fm.get("topic"),
        "status": fm.get("status"),
        "jurisdiction": fm.get("jurisdiction"),
        "amendment": fm.get("amendment"),
        "weight": fm.get("weight"),
        "case_set": {
            "homed_cases": homed,
            "homed_count": len(homed),
            "linked_case_count": len(linked),
        },
        "split": extract_splits(body, body_start, link_index),
    }


# --------------------------------------------------------------------------
# Corpus walk + freeze
# --------------------------------------------------------------------------


def iter_markdown(content_root):
    for dirpath, _dirs, files in os.walk(content_root):
        for name in sorted(files):
            if name.endswith(".md"):
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, content_root)
                yield rel.replace(os.sep, "/"), full


def build(content_root, lake_dir):
    # Pass 1: parse every page's frontmatter, classify, index.
    pages = []          # (rel, fm, body, body_start, is_case)
    index_pages = []    # (rel, fm) for the link index
    for rel, full in iter_markdown(content_root):
        text = read_text(full)
        fm, body, body_start = frontmatter(text)
        is_case = fm.get("type") == "case"
        pages.append((rel, fm, body, body_start, is_case))
        index_pages.append((rel, fm))
    link_index = build_link_index(index_pages)

    # Pass 2a: build reverse-homes index (case -> doctrine home + role).
    reverse_homes = {}
    for rel, fm, _body, _bs, is_case in pages:
        if not is_case:
            continue
        for h in fm.get("homes") or []:
            if not isinstance(h, dict):
                continue
            page = h.get("page")
            if not isinstance(page, str):
                continue
            dpath = resolve_link(wikilink_target(page), link_index)
            if dpath is None:
                continue
            reverse_homes.setdefault(dpath, []).append({
                "case_path": rel,
                "case_title": fm.get("title"),
                "role": h.get("role"),
            })

    # Pass 2b: emit items.
    items = []
    for rel, fm, body, body_start, is_case in pages:
        if is_case:
            items.append(build_case_item(rel, fm, link_index, lake_dir))
        else:
            items.append(build_doctrine_item(
                rel, fm, body, body_start, reverse_homes, link_index))
    items.sort(key=lambda it: (it["kind"], it["path"]))
    return items


def canonical(items):
    return json.dumps(items, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def content_hash(items):
    return hashlib.sha256(canonical(items).encode("utf-8")).hexdigest()


def summarize(items):
    cases = [i for i in items if i["kind"] == "case"]
    docs = [i for i in items if i["kind"] == "doctrine"]
    by_type = {}
    for d in docs:
        t = d.get("type") or "none"
        by_type[t] = by_type.get(t, 0) + 1
    missing_holding = sum(1 for c in cases if not c["holding_present"])
    varies = sum(1 for c in cases
                 if (c["treatment"] or {}).get("varies_by_point") is True)
    with_po = sum(1 for c in cases
                  if (c["treatment"] or {}).get("point_overrides"))
    doc_with_split = sum(1 for d in docs if d["split"]["has_split_signal"])
    homed_docs = sum(1 for d in docs if d["case_set"]["homed_count"] > 0)
    return {
        "case": len(cases),
        "doctrine": len(docs),
        "total_p_items": len(items),
        "doctrine_by_type": {k: by_type[k] for k in sorted(by_type)},
        "cases_missing_holding": missing_holding,
        "cases_varies_by_point": varies,
        "cases_with_point_overrides": with_po,
        "doctrine_with_split_signal": doc_with_split,
        "doctrine_with_homed_cases": homed_docs,
    }


def git_head(repo):
    try:
        out = subprocess.run(
            ["git", "-C", repo, "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except Exception:
        return None


def freeze(items, repo, now_iso):
    chash = content_hash(items)
    header = {
        "schema": SCHEMA,
        "generated": now_iso,
        "lane": LANE,
        "model": MODEL,
        "corpus_head": git_head(repo),
        "content_hash": chash,
        "hash_covers": "items[] canonical JSON (sort_keys, compact, utf-8); "
                       "excludes this header so the freeze hash is idempotent "
                       "on unchanged corpus content",
        "counts": summarize(items),
        "no_regression_floor": len(items),
    }
    return header, chash


def write_freeze(items, out_path, repo, now_iso):
    header, chash = freeze(items, repo, now_iso)
    doc = dict(header)
    doc["items"] = items
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    side = out_path.rsplit(".", 1)[0] + ".sha256"
    with open(side, "w", encoding="utf-8") as fh:
        fh.write(chash + "  " + os.path.basename(out_path) + "\n")
    return header, side


# --------------------------------------------------------------------------
# Self-test (committed fixtures)
# --------------------------------------------------------------------------

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "fixtures", "thread_p")


def _write_fixtures():
    corpus = os.path.join(FIX, "corpus")
    lake = os.path.join(FIX, "lake")
    for sub in ("cases", "doctrine"):
        os.makedirs(os.path.join(corpus, sub), exist_ok=True)
    os.makedirs(lake, exist_ok=True)

    alpha = """---
title: "Fixture Alpha v. State"
type: case
citation: "1 F.4th 1 (9th Cir. 2021)"
court: "United States Court of Appeals for the Ninth Circuit"
court_level: circuit
year: 2021
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: caution
  as_of_content: 2026-06-30
  as_of_treatment: 2026-06-30
  varies_by_point: true
  scope_note: "Split anchor; the forensic-search point is contested."
  point_overrides:
    - point: fixture.forensic-search
      point_label: "Forensic device search standard"
      field_i_validity: superseded
      s3_binding_status: bound
      by:
        - name: Fixture Beta v. United States
          cluster_id: 999001
          cite: 2 F.4th 2
          field_ii: limited
      scope_note: "Replaced by Beta's two-step test."
lake:
  record_id: Fixture Alpha v. State
  status: verified
homes:
  - page: "[[Fixture Doctrine]]"
    role: "Key — Anchor"
  - page: "[[Missing Doctrine]]"
    role: "Related (cross-doctrine)"
related: ["[[Fixture Beta v. United States]]"]
aliases: []
holding: "A forensic search of a device seized at the border requires reasonable suspicion."
---

Body of Alpha. See [[Fixture Beta v. United States|Beta]].
"""

    beta = """---
title: "Fixture Beta v. United States"
type: case
citation: "2 F.4th 2 (11th Cir. 2022)"
court: "United States Court of Appeals for the Eleventh Circuit"
court_level: circuit
year: 2022
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-30
  as_of_treatment: 2026-06-30
  varies_by_point: false
  scope_note: "The outlier position."
  point_overrides: []
lake:
  record_id: Fixture Beta v. United States
  status: verified
homes:
  - page: "[[Fixture Doctrine]]"
    role: "Key — Progeny / Refinement"
related: []
aliases: []
holding: "No individualized suspicion is required for a forensic device search."
---

Body of Beta.
"""

    gamma = """---
title: "Fixture Gamma v. Doe"
type: case
citation: "3 U.S. 3 (1799)"
court: "U.S. Supreme Court"
court_level: scotus
year: 1799
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: unverified
  as_of_content: 2026-06-30
  as_of_treatment: 2026-06-30
  varies_by_point: false
  point_overrides: []
lake:
  record_id: fixture-gamma-v-doe--999003
  status: not_found
homes: []
related: []
aliases: []
---

Body of Gamma. No holding in frontmatter (edge case).
"""

    doctrine = """---
title: "Fixture Doctrine"
type: doctrine
topic: "Fixture Doctrine"
status: draft
jurisdiction: "Federal (U.S. Const. amend. IV)"
amendment: "U.S. Const. amend. IV"
weight: 20
aliases: ["Fixture Doctrine"]
related: ["[[Two Definitions of Search]]"]
---

**The test up front.** The forensic-device question is an unresolved circuit split.

- ***[[Fixture Alpha v. State|Alpha]]* (9th Cir. 2021)** — anchors the split. **Binding in-circuit — 9th Cir.**
- ***[[Fixture Beta v. United States|Beta]]* (11th Cir. 2022)** — the outlier. **Binding in-circuit — 11th Cir.**

SCOTUS has not resolved the split.
"""

    docindex = """---
title: "Fixture Section"
type: index
status: draft
---

Landing page. Links to [[Fixture Doctrine]].
"""

    files = {
        os.path.join(corpus, "cases", "Fixture Alpha v. State.md"): alpha,
        os.path.join(corpus, "cases", "Fixture Beta v. United States.md"): beta,
        os.path.join(corpus, "cases", "Fixture Gamma v. Doe.md"): gamma,
        os.path.join(corpus, "doctrine", "Fixture Doctrine.md"): doctrine,
        os.path.join(corpus, "doctrine", "index.md"): docindex,
    }
    for p, c in files.items():
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(c)

    lakes = {
        "Fixture Alpha v. State": {
            "record_id": "Fixture Alpha v. State", "status": "verified",
            "identity": {"cluster_id": 999000, "lead_opinion_id": 999900,
                         "court_level": "circuit"},
            "treatment": {
                "field_i_validity": "caution", "varies_by_point": True,
                "point_overrides": [{
                    "point": "fixture.forensic-search",
                    "point_label": "Forensic device search standard",
                    "field_i_validity": "superseded",
                    "s3_binding_status": "bound",
                    "by": [{"name": "Fixture Beta v. United States",
                            "cluster_id": 999001, "cite": "2 F.4th 2",
                            "field_ii": "limited"}],
                    "scope_note": "Replaced.",
                }],
                "edges": [
                    {"citing_case": {"name": "Later Case A"},
                     "field_ii": "questioned", "field_iii": "mentioned",
                     "point": None, "proposed": True},
                    {"citing_case": {"name": "Later Case B"},
                     "field_ii": "criticized", "field_iii": "mentioned",
                     "point": None, "proposed": True},
                ],
            },
        },
        "Fixture Beta v. United States": {
            "record_id": "Fixture Beta v. United States", "status": "verified",
            "identity": {"cluster_id": 999001, "lead_opinion_id": 999901,
                         "court_level": "circuit"},
            "treatment": {"field_i_validity": "good_law",
                          "varies_by_point": False,
                          "point_overrides": [], "edges": []},
        },
    }
    for rid, rec in lakes.items():
        with open(os.path.join(lake, rid + ".json"), "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False, indent=1)
    return corpus, lake


def _check(cond, msg):
    if not cond:
        raise AssertionError(msg)


def self_test():
    # 1) MiniYAML unit checks.
    y = parse_yaml([
        'a: "x: y"',
        'b: [true, false, 3, "[[C|d]]"]',
        'c:',
        '  - point: p1',
        '    by:',
        '      - name: N1',
        '        cite: 2 F.4th 2',
        '  - point: p2',
        'd: 7',
        'e: false',
    ])
    _check(y["a"] == "x: y", "quoted-colon scalar: %r" % y.get("a"))
    _check(y["b"] == [True, False, 3, "[[C|d]]"], "flow list: %r" % y.get("b"))
    _check(isinstance(y["c"], list) and len(y["c"]) == 2, "seq-of-maps len")
    _check(y["c"][0]["point"] == "p1", "seq item key")
    _check(y["c"][0]["by"][0]["name"] == "N1", "nested seq name")
    _check(y["c"][0]["by"][0]["cite"] == "2 F.4th 2", "nested seq scalar w/ spaces")
    _check(y["c"][1]["point"] == "p2", "second seq item")
    _check(y["d"] == 7 and y["e"] is False, "int/bool scalars")

    # 2) build against fixtures.
    corpus, lake = _write_fixtures()
    items = build(corpus, lake)
    summ = summarize(items)
    _check(summ["case"] == 3, "case count %r" % summ)
    _check(summ["doctrine"] == 2, "doctrine count %r" % summ)
    _check(summ["total_p_items"] == 5, "floor %r" % summ)
    _check(summ["cases_missing_holding"] == 1, "missing holding %r" % summ)
    _check(summ["cases_varies_by_point"] == 1, "varies %r" % summ)
    _check(summ["cases_with_point_overrides"] == 1, "point_overrides %r" % summ)

    by_id = {it["p_id"]: it for it in items}
    _check(len({it["p_id"] for it in items}) == 5, "p_id uniqueness")

    alpha = next(i for i in items if i.get("title") == "Fixture Alpha v. State")
    _check(alpha["holding_present"] is True, "alpha holding present")
    _check(alpha["treatment"]["point_overrides"][0]["by"][0]["name"]
           == "Fixture Beta v. United States", "alpha point_override.by")
    _check(alpha["homes"][0]["resolved_path"] == "doctrine/Fixture Doctrine.md",
           "alpha home resolved: %r" % alpha["homes"][0])
    _check(alpha["homes"][1]["resolved_path"] is None,
           "alpha missing-home unresolved -> None")
    _check(alpha["lake"]["treatment_edge_count"] == 2, "alpha lake edge count")
    _check(alpha["lake"]["treatment_edges_all_proposed"] is True,
           "alpha edges all proposed")
    _check(alpha["lake"]["cluster_id"] == 999000, "alpha lake cluster")

    gamma = next(i for i in items if i.get("title") == "Fixture Gamma v. Doe")
    _check(gamma["holding_present"] is False, "gamma holding absent")
    _check(gamma["lake"]["status"] == "not_found" or
           gamma["lake"].get("missing_lake_file"),
           "gamma lake missing handled: %r" % gamma["lake"])

    doc = next(i for i in items if i.get("title") == "Fixture Doctrine")
    _check(doc["split"]["has_split_signal"] is True, "doctrine split signal")
    cs = {c["case_title"] for c in doc["case_set"]["homed_cases"]}
    _check(cs == {"Fixture Alpha v. State", "Fixture Beta v. United States"},
           "doctrine case_set: %r" % cs)
    _check(doc["case_set"]["homed_count"] == 2, "homed_count")
    _check(doc["case_set"]["linked_case_count"] >= 2, "linked case count")
    circs = {(c["case"], c["circuit"]) for c in doc["split"]["circuit_positions"]}
    _check(("Fixture Alpha v. State", "9th Cir.") in circs,
           "circuit position Alpha: %r" % circs)
    _check(("Fixture Beta v. United States", "11th Cir.") in circs,
           "circuit position Beta: %r" % circs)
    _check(all(_is_case_path(c["resolved_case_path"])
               for c in doc["split"]["circuit_positions"]),
           "circuit positions resolve to case pages")

    # 3) idempotency: rebuild -> identical content_hash + identical items bytes.
    items2 = build(corpus, lake)
    _check(content_hash(items) == content_hash(items2), "hash idempotent")
    _check(canonical(items) == canonical(items2), "canonical idempotent")

    # 4) freeze header carries the hash; sidecar matches; timestamp not hashed.
    h1, _ = freeze(items, corpus, "2026-07-09T00:00:00Z")
    h2, _ = freeze(items, corpus, "2030-01-01T00:00:00Z")
    _check(h1["content_hash"] == h2["content_hash"],
           "freeze hash independent of timestamp")
    _check(h1["content_hash"] == content_hash(items), "header hash == body hash")
    _check(h1["no_regression_floor"] == 5, "floor in header")

    print("SELF-TEST PASS: 5 P items (3 case / 2 doctrine); MiniYAML, "
          "reverse-homes, splits, lake-merge, idempotent freeze all OK.")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description="S9 P0-B Thread P freeze (R5)")
    ap.add_argument("--content", default="content")
    ap.add_argument("--lake", default="_overhaul2/lake/cases")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default="_run/s9/thread-P.json")
    ap.add_argument("--now", default=None,
                    help="override the freeze timestamp (ISO8601)")
    ap.add_argument("--report", action="store_true",
                    help="print a JSON summary to stdout")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    now_iso = args.now or _dt.datetime.now(_dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")
    items = build(args.content, args.lake)
    header, side = write_freeze(items, args.out, args.repo, now_iso)
    if args.report:
        print(json.dumps({
            "out": args.out,
            "sidecar": side,
            "content_hash": header["content_hash"],
            "counts": header["counts"],
            "no_regression_floor": header["no_regression_floor"],
        }, ensure_ascii=False, indent=2))
    else:
        print("froze %d P items -> %s (sha256 %s)" % (
            header["no_regression_floor"], args.out, header["content_hash"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
