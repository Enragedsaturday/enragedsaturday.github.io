#!/usr/bin/env python3
"""
S8 pin-anchor remediation (spec S8 R6).

Quartz mints a block id only for an `^pin-N` anchor that ENDS its own block
(paragraph or list item). The corpus carries mid-block `^pin-N` definitions that
are simultaneously visible-text leaks and dead anchors (deep links resolve to
nothing). This tool splits each offending block so every pin ends its own block,
content order and wording BYTE-UNTOUCHED — the only edit is whitespace / blank
lines (and, for a list item, the same list marker to start the next item).

    Exhibit form  : content/cases/United States v. Walker.md
                    (each pinned quote = its own paragraph, `^pin-N` end-of-block)
    Defect form   : content/cases/Kyllo v. United States.md:61
                    (`^pin-37` mid-paragraph — dead anchor)

FAIL-CLOSED: if the run after the split point does not begin a new sentence or a
new quote (the pin sits genuinely mid-sentence), or the pin sits in a table row /
heading / blockquote / other structure a paragraph split cannot fix — DO NOT EDIT.
Queue it in `_run/o2-execute/S8-PIN-REVIEW-QUEUE.md` with file:line + a reason.

Modes:
    (default)      dry-run: report defects, planned edits, planned queue
    --write        apply edits; emit S8-PIN-REMEDIATION.jsonl + the review queue
    --verify       post-pass checks (mid-block==queued; refs resolve; ref count)
    --self-test    run the fixtures under scripts/s8/fixtures/pins/

Constraints: Python 3 stdlib only. Zero CourtListener. Touches only content/**.md
(whitespace-split edits) + the two _run/o2-execute/S8-PIN-* artifacts.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zones  # noqa: E402  (local module, same dir)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT = os.path.join(REPO, "content")
RUN_DIR = os.path.join(REPO, "_run", "o2-execute")
JSONL = os.path.join(RUN_DIR, "S8-PIN-REMEDIATION.jsonl")
QUEUE = os.path.join(RUN_DIR, "S8-PIN-REVIEW-QUEUE.md")

LANE = "o2-opus-xhigh"
MODEL = "claude-opus-4-8"

# A pin DEFINITION token: `^pin-N` whose caret is NOT preceded by `#`
# (a `#^pin-N` is a wikilink/embed REFERENCE, never a definition).
PIN_DEF = re.compile(r"(?<!#)\^pin-[0-9A-Za-z]+")
# A pin REFERENCE inside a wikilink or embed: [[Target#^pin-N]] / ![[Target#^pin-N]]
PIN_REF = re.compile(r"(!?)\[\[([^\]\n]*?)#(\^pin-[0-9A-Za-z]+)(?:\|[^\]\n]*)?\]\]")

_OPEN_QUOTES = "\"'“”‘’"


def _begins_new_sentence(tail: str) -> bool:
    """True iff the run after a split point starts a new sentence or a new quote.

    Skips leading emphasis markers (`*`/`_`/backtick) and one optional opening
    bracket/paren, then requires an uppercase letter or an opening quote. Anything
    else (lowercase, an em-dash continuation, a digit) is treated as mid-sentence.
    """
    s = tail.lstrip()
    i, n = 0, len(s)
    while i < n and s[i] in "*_`":
        i += 1
    if i < n and s[i] in "([":
        i += 1
        while i < n and s[i] in "*_`":
            i += 1
    if i >= n:
        return False
    c = s[i]
    if c.isupper():
        return True
    if c in _OPEN_QUOTES:
        return True
    return False


def _line_no(text: str, off: int) -> int:
    return text.count("\n", 0, off) + 1


def _list_marker(text: str, block) -> str:
    """The `indent + bullet + spaces` prefix of a list-item block's first line."""
    nl = text.find("\n", block["start"], block["end"])
    end = nl if nl != -1 else block["end"]
    first = text[block["start"]:end]
    m = zones._RE_LISTITEM.match(first)
    return m.group(0) if m else "- "


def find_defects(text: str):
    """Return (edits, queued).

    edits  : [{ws_start, ws_end, repl, line, pin, action}] — replace text[ws_start:ws_end]
             with repl.  (ws run between the pin token and the next sentence.)
    queued : [{line, pin, reason}]
    """
    edits = []
    queued = []
    for b in zones.iter_blocks(text):
        if b["kind"] in ("code", "frontmatter"):
            continue
        seg = text[b["start"]:b["end"]]
        for m in PIN_DEF.finditer(seg):
            tok_end = b["start"] + m.end()
            pin = m.group(0)
            after = text[tok_end:b["end"]]
            if after.strip() == "":
                continue  # end-of-block: OK, Quartz mints the id
            line = _line_no(text, b["start"] + m.start())

            if b["kind"] in ("heading", "table"):
                queued.append({"line": line, "pin": pin,
                               "reason": f"pin sits inside a {b['kind']} — a paragraph split cannot fix"})
                continue
            if b["kind"] == "blockquote":
                queued.append({"line": line, "pin": pin,
                               "reason": "pin sits inside a blockquote — a paragraph split cannot fix"})
                continue
            if not _begins_new_sentence(after):
                queued.append({"line": line, "pin": pin,
                               "reason": "pin sits mid-sentence — the run after it does not begin a new sentence or a new quote"})
                continue

            # splittable paragraph or list item: collapse the ws run to a block break
            ws_end = tok_end
            while ws_end < b["end"] and text[ws_end].isspace():
                ws_end += 1
            if b["kind"] == "para":
                edits.append({"ws_start": tok_end, "ws_end": ws_end, "repl": "\n\n",
                              "line": line, "pin": pin, "action": "split-para"})
            else:  # listitem
                marker = _list_marker(text, b)
                edits.append({"ws_start": tok_end, "ws_end": ws_end, "repl": "\n" + marker,
                              "line": line, "pin": pin, "action": "split-listitem"})
    return edits, queued


def apply_edits(text: str, edits) -> str:
    for e in sorted(edits, key=lambda e: e["ws_start"], reverse=True):
        text = text[:e["ws_start"]] + e["repl"] + text[e["ws_end"]:]
    return text


# --------------------------------------------------------------------------
# corpus walk
# --------------------------------------------------------------------------

def _md_files():
    for root, _dirs, files in os.walk(CONTENT):
        for fn in sorted(files):
            if fn.endswith(".md"):
                yield os.path.join(root, fn)


def _rel(path: str) -> str:
    return os.path.relpath(path, REPO)


def _count_pin_refs(text: str) -> int:
    return len(PIN_REF.findall(text))


def _end_of_block_defs(text: str):
    """Set of pin ids that are END-OF-BLOCK definitions in `text`."""
    ok = set()
    for b in zones.iter_blocks(text):
        if b["kind"] in ("code", "frontmatter"):
            continue
        seg = text[b["start"]:b["end"]]
        for m in PIN_DEF.finditer(seg):
            tok_end = b["start"] + m.end()
            if text[tok_end:b["end"]].strip() == "":
                ok.add(m.group(0))
    return ok


def _all_defs(text: str):
    return set(PIN_DEF.findall(text))


# --------------------------------------------------------------------------
# modes
# --------------------------------------------------------------------------

def run(write: bool):
    all_edits = []          # (relpath, edits)
    all_queue = []          # (relpath, {line,pin,reason})
    files_touched = 0
    total_defect_blocks = 0
    pin_refs_total = 0

    for path in _md_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        pin_refs_total += _count_pin_refs(text)
        edits, queued = find_defects(text)
        if not edits and not queued:
            continue
        rel = _rel(path)
        for e in edits:
            all_edits.append((rel, e))
        for q in queued:
            all_queue.append((rel, q))
        if edits:
            files_touched += 1
            if write:
                new_text = apply_edits(text, edits)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)

    total_defect_blocks = len(all_edits) + len(all_queue)

    print(f"block-level mid-block pin defects : {total_defect_blocks}")
    print(f"  splittable (edits)             : {len(all_edits)}  across {files_touched} files")
    print(f"  fail-closed (queued)           : {len(all_queue)}")
    print(f"pre-existing pin references       : {pin_refs_total}")
    print("action distribution:")
    dist = {}
    for _rp, e in all_edits:
        dist[e["action"]] = dist.get(e["action"], 0) + 1
    for k in sorted(dist):
        print(f"  {k:16s}: {dist[k]}")

    if write:
        _write_jsonl(all_edits, all_queue, pin_refs_total, total_defect_blocks)
        _write_queue(all_queue)
        print(f"\nWROTE: {_rel(path) if False else _rel(JSONL)}")
        print(f"WROTE: {_rel(QUEUE)}")
    else:
        print("\n(dry-run — no files written; pass --write to apply)")
        _preview(all_edits)

    return all_edits, all_queue, pin_refs_total


def _preview(all_edits, n=5):
    print(f"\nfirst {min(n, len(all_edits))} planned edits:")
    for rel, e in all_edits[:n]:
        print(f"  {rel}:{e['line']}  {e['pin']}  -> {e['action']}")


def _write_jsonl(all_edits, all_queue, pin_refs_total, total_defects):
    os.makedirs(RUN_DIR, exist_ok=True)
    header = {
        "lane": LANE,
        "model": MODEL,
        "tool": "remediate_pins",
        "date": datetime.date.today().isoformat(),
        "counts": {
            "mid_block_defects": total_defects,
            "edits_applied": len(all_edits),
            "queued": len(all_queue),
            "pin_refs_before": pin_refs_total,
        },
    }
    with open(JSONL, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(header, ensure_ascii=False) + "\n")
        for rel, e in all_edits:
            fh.write(json.dumps(
                {"file": rel, "line": e["line"], "pin": e["pin"], "action": e["action"]},
                ensure_ascii=False) + "\n")


def _write_queue(all_queue):
    os.makedirs(RUN_DIR, exist_ok=True)
    lines = [
        "# S8 pin-anchor review queue (R6 fail-closed)",
        "",
        f"> lane `{LANE}` · model `{MODEL}` · {datetime.date.today().isoformat()}",
        ">",
        "> Each row is a mid-block `^pin-N` definition the remediator refused to edit",
        "> because a whitespace paragraph split cannot fix it without touching wording",
        "> or structure. A writer lane resolves each; S9 reviews. NOT auto-edited.",
        "",
    ]
    if not all_queue:
        lines.append("_(empty — every mid-block pin was mechanically splittable.)_")
    else:
        for rel, q in all_queue:
            lines.append(f"- `{rel}:{q['line']}` — `{q['pin']}` — {q['reason']}")
    lines.append("")
    with open(QUEUE, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


_QUEUE_ROW = re.compile(r"^-\s+`([^`]+):(\d+)`\s+—\s+`(\^pin-[0-9A-Za-z]+)`\s+—\s+(.*)$")


def _read_queue():
    """Return set of (relpath, pin) currently queued."""
    out = set()
    if not os.path.exists(QUEUE):
        return out
    with open(QUEUE, encoding="utf-8") as fh:
        for line in fh:
            m = _QUEUE_ROW.match(line.rstrip("\n"))
            if m:
                out.add((m.group(1), m.group(3)))
    return out


def _read_jsonl_header():
    if not os.path.exists(JSONL):
        return None
    with open(JSONL, encoding="utf-8") as fh:
        first = fh.readline()
    try:
        return json.loads(first)
    except Exception:
        return None


def verify():
    queued = _read_queue()
    header = _read_jsonl_header()

    # Build stem -> path index and per-file end-of-block def sets.
    stem_index = {}
    eob_by_rel = {}
    alldefs_by_rel = {}
    refs = []           # (relpath, line, target, pin)
    pin_refs_now = 0
    mid_block_now = []  # (relpath, line, pin)

    for path in _md_files():
        rel = _rel(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        stem = os.path.splitext(os.path.basename(path))[0]
        stem_index.setdefault(stem, []).append(rel)
        eob_by_rel[rel] = _end_of_block_defs(text)
        alldefs_by_rel[rel] = _all_defs(text)
        pin_refs_now += _count_pin_refs(text)
        # references
        for m in PIN_REF.finditer(text):
            target = m.group(2).strip()
            pin = m.group(3)
            refs.append((rel, _line_no(text, m.start()), target, pin))
        # mid-block defects still present
        edits, q = find_defects(text)
        for e in edits:
            mid_block_now.append((rel, e["line"], e["pin"]))
        for qq in q:
            mid_block_now.append((rel, qq["line"], qq["pin"]))

    rel_by_stem = {s: v for s, v in stem_index.items()}

    def resolve(target):
        """Return list of candidate relpaths for a reference target."""
        cands = []
        if "/" in target:
            p = os.path.join(CONTENT, target + ".md")
            if os.path.exists(p):
                cands.append(_rel(p))
            stem = os.path.basename(target)
            cands.extend(rel_by_stem.get(stem, []))
        else:
            cands.extend(rel_by_stem.get(target, []))
        # de-dup preserving order
        seen = set()
        out = []
        for c in cands:
            if c not in seen:
                seen.add(c)
                out.append(c)
        return out

    # (1) mid-block pin defs == 0 (minus queued)
    unqueued = [(r, l, p) for (r, l, p) in mid_block_now if (r, p) not in queued]

    # (2) every reference resolves to an end-of-block def in its target file
    unresolved = []
    for rel, line, target, pin in refs:
        cands = resolve(target)
        ok = any(pin in eob_by_rel.get(c, set()) for c in cands)
        if not ok:
            exists_mid = any(pin in alldefs_by_rel.get(c, set()) for c in cands)
            why = "no target file" if not cands else (
                "def exists but is NOT end-of-block" if exists_mid else "no such pin def in target")
            unresolved.append((rel, line, target, pin, why))

    # (3) count of pre-existing pin references unchanged
    baseline = None
    if header and isinstance(header.get("counts"), dict):
        baseline = header["counts"].get("pin_refs_before")

    print("=== S8 R6 --verify ===")
    print(f"(1) mid-block pin defs total      : {len(mid_block_now)}")
    print(f"    queued (expected residue)     : {len(queued)}")
    print(f"    UN-queued (must be 0)         : {len(unqueued)}")
    for r, l, p in unqueued[:20]:
        print(f"      ! {r}:{l} {p}")
    print(f"(2) pin references scanned        : {len(refs)}")
    print(f"    UNRESOLVED (must be 0)        : {len(unresolved)}")
    for r, l, t, p, why in unresolved[:20]:
        print(f"      ! {r}:{l} -> [[{t}#{p}]] : {why}")
    print(f"(3) pin references now            : {pin_refs_now}")
    if baseline is not None:
        print(f"    baseline (jsonl header)       : {baseline}")
        print(f"    unchanged                     : {pin_refs_now == baseline}")
    else:
        print("    baseline                      : (no jsonl header; run --write first)")

    ok = (len(unqueued) == 0 and len(unresolved) == 0 and
          (baseline is None or pin_refs_now == baseline))
    print(f"\nVERIFY: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------

_FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures", "pins")


def _load(name):
    with open(os.path.join(_FIX, name), encoding="utf-8") as fh:
        return fh.read()


def _self_test():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    # 1) mid-paragraph split
    t = _load("midpara.md")
    edits, q = find_defects(t)
    check(len(edits) == 1 and edits[0]["action"] == "split-para",
          f"midpara: expected 1 split-para, got {[(e['pin'], e['action']) for e in edits]} q={q}")
    check(len(q) == 0, f"midpara: expected no queue, got {q}")
    out = apply_edits(t, edits)
    check("^pin-37\n\nIt therefore held" in out,
          "midpara: pin-37 not split onto its own paragraph")
    check("intimate details" in out and out.count("intimate details") == t.count("intimate details"),
          "midpara: wording changed")
    # idempotence
    e2, q2 = find_defects(out)
    check(len(e2) == 0, f"midpara: not idempotent, second pass planned {len(e2)} edits")

    # 2) list-item split
    t = _load("listitem.md")
    edits, q = find_defects(t)
    check(len(edits) == 1 and edits[0]["action"] == "split-listitem",
          f"listitem: expected 1 split-listitem, got {[(e['pin'], e['action']) for e in edits]} q={q}")
    out = apply_edits(t, edits)
    check("^pin-5\n- Second" in out, f"listitem: bad split -> {out!r}")
    e2, _ = find_defects(out)
    check(len(e2) == 0, "listitem: not idempotent")

    # 3) already-clean idempotence
    t = _load("clean.md")
    edits, q = find_defects(t)
    check(len(edits) == 0 and len(q) == 0,
          f"clean: expected 0 edits/0 queue, got edits={len(edits)} q={len(q)}")

    # 4) fail-closed mid-sentence -> queue
    t = _load("midsentence.md")
    edits, q = find_defects(t)
    check(len(edits) == 0, f"midsentence: expected 0 edits, got {[e['pin'] for e in edits]}")
    check(len(q) == 1 and "mid-sentence" in q[0]["reason"],
          f"midsentence: expected 1 mid-sentence queue row, got {q}")

    # 5) blockquote -> queue (structure a paragraph split can't fix)
    t = _load("blockquote.md")
    edits, q = find_defects(t)
    check(len(edits) == 0, f"blockquote: expected 0 edits, got {[e['pin'] for e in edits]}")
    check(len(q) == 1 and "blockquote" in q[0]["reason"],
          f"blockquote: expected 1 blockquote queue row, got {q}")

    if failures:
        print("remediate_pins.py --self-test: FAIL")
        for f in failures:
            print("  - " + f)
        return 1
    print("remediate_pins.py --self-test: PASS (midpara / listitem / clean / mid-sentence / blockquote)")
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="S8 R6 pin-anchor remediation")
    ap.add_argument("--write", action="store_true", help="apply edits + emit artifacts")
    ap.add_argument("--verify", action="store_true", help="post-pass verification")
    ap.add_argument("--self-test", action="store_true", help="run fixtures")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()
    if args.verify:
        return verify()
    run(write=args.write)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
