#!/usr/bin/env python3
"""FIN-INDEX (S9 P4): fresh Case-Index regeneration + S8 term-link pass re-applied.

Preferred path: drive the SIGNED S8 term-linker (`scripts/s8/link_terms.py`)
scoped to the Case Index only, reusing its exact zone-mask / longest-match /
table-pipe-escape / dead-target rules. No re-implementation of the linking rule.

Reproduction facts (verified):
  * register `scripts/lint/term-register.yml` is UNCHANGED since the S8 commit
    (f2444514) -> scoped re-run reproduces HEAD on every unchanged cell.
  * S8 linked the Case Index with the pincite-line guard OFF; here guard on/off
    is empirically identical, but we call with protect_pincite_lines=False to
    match the documented S8 Case-Index treatment.

Pipeline (run with the working tree restored to HEAD so both flagged carry-
forward rows are present):
  gen.build() -> plain case rows (fresh P2/P3 holdings) + flagged rows verbatim
  scoped linker -> term-link the plain case-row holdings
  flagged override -> flagged rows forced to HEAD verbatim (adjudicated, already
                      S8-linked; never re-derived)

Modes: default = REPORT (no write). --write = write the Case Index + emit
FIN-INDEX-fixes.jsonl + FIN-INDEX-droplog.jsonl.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "scripts"))
sys.path.insert(0, os.path.join(REPO, "scripts", "s8"))
sys.path.insert(0, os.path.join(REPO, "scripts", "lint"))

import build_case_index as gen  # noqa: E402
import link_terms as lt         # noqa: E402
import zones                    # noqa: E402

CI_REL = "legal-system-research-and-reference/Case Index.md"
INDEX = os.path.join(REPO, "content", CI_REL)
HEAD_PATH = os.path.join(HERE, "CI_HEAD.md")
CASES_DIR = os.path.join(REPO, "content", "cases")

HEADER_RE = re.compile(r"^\|\s*Case\s*\|")
FLAG_RE = re.compile(r"UNVERIFIABLE|UNCONFIRMED")
_WL = re.compile(r"\[\[([^\]]*?)\]\]")


def split_row(row):
    pipes = zones._row_pipe_positions(row)
    if len(pipes) < 2:
        return None
    return [row[pipes[i] + 1:pipes[i + 1]].strip() for i in range(len(pipes) - 1)]


def _surface(inner):
    inner = inner.replace("\\|", "|")
    return inner.split("|")[-1] if "|" in inner else inner


def strip_links(cell):
    return _WL.sub(lambda m: _surface(m.group(1)), cell)


def parse_rows(text):
    out = {}
    for i, ln in enumerate(text.split("\n")):
        if not ln.startswith("|") or ln.startswith("|---") or HEADER_RE.match(ln):
            continue
        cells = split_row(ln)
        if not cells or len(cells) != 5:
            continue
        out[cells[0]] = {"holding": cells[1], "good": cells[2], "home": cells[3],
                         "cl": cells[4], "line": i + 1, "raw": ln}
    return out


def cell_links(holding):
    links = []
    for m in _WL.finditer(holding):
        inner = m.group(1).replace("\\|", "|")
        target, surface = (inner.rsplit("|", 1) if "|" in inner else (inner, inner))
        if target.startswith("Common Legal Terms#"):
            route = "glossary"
        elif target.startswith("Reading and Citing Cases#"):
            route = "citing"
        else:
            route = "page"
        links.append((route, target, surface))
    return links


def is_flagged(case_cell):
    return bool(FLAG_RE.search(case_cell))


def build_final():
    """Return (final_text, diag)."""
    regen_text, nrows, nflag, nbrief = gen.build()

    terms, schema = lt.load_register()
    idx = lt.build_page_index()
    dead = lt.validate_register(terms, idx)
    edits_off, _ = lt.build_link_plan(regen_text, CI_REL, terms, idx,
                                      protect_pincite_lines=False)
    edits_on, _ = lt.build_link_plan(regen_text, CI_REL, terms, idx,
                                     protect_pincite_lines=True)
    linked_text = lt.apply_edits(regen_text, edits_off)

    # flagged override: force flagged rows to HEAD verbatim (adjudicated carry-
    # forwards, already S8-linked; the linker must never re-derive them)
    head_text = open(HEAD_PATH, encoding="utf-8").read()
    head_flagged = {}
    for ln in head_text.split("\n"):
        if ln.startswith("|") and is_flagged(ln):
            cells = split_row(ln)
            if cells:
                head_flagged[cells[0]] = ln
    final_lines = linked_text.split("\n")
    flagged_overridden = []
    for i, ln in enumerate(final_lines):
        if ln.startswith("|") and is_flagged(ln):
            cells = split_row(ln)
            key = cells[0] if cells else None
            if key in head_flagged and final_lines[i] != head_flagged[key]:
                flagged_overridden.append(key)
                final_lines[i] = head_flagged[key]
    final_text = "\n".join(final_lines)

    diag = {"regen_rows": nrows, "flagged": nflag, "brief_mentions": nbrief,
            "schema": schema, "dead_targets": dead,
            "guard_off_links": len(edits_off), "guard_on_links": len(edits_on),
            "flagged_overridden": flagged_overridden, "head_text": head_text,
            "regen_text": regen_text}
    return final_text, diag


def main():
    write = "--write" in sys.argv[1:]
    final_text, diag = build_final()

    head_rows = parse_rows(diag["head_text"])
    regen_rows = parse_rows(diag["regen_text"])
    final_rows = parse_rows(final_text)

    # classify by comparing HEAD-stripped holding vs regen plain holding
    changed, unchanged, added, removed = [], [], [], []
    for case, r in regen_rows.items():
        if is_flagged(case):
            continue
        if case not in head_rows:
            added.append(case)
        elif strip_links(head_rows[case]["holding"]) == r["holding"]:
            unchanged.append(case)
        else:
            changed.append(case)
    for case in head_rows:
        if case not in regen_rows and not is_flagged(case):
            removed.append(case)

    # fidelity: unchanged cells must reproduce HEAD verbatim
    fidelity_fail = [c for c in unchanged
                     if final_rows[c]["holding"] != head_rows[c]["holding"]]

    # drop / add accounting (case rows only; flagged rows are verbatim)
    drops, adds = [], []
    for case in final_rows:
        if is_flagged(case):
            continue
        hset = set(cell_links(head_rows[case]["holding"])) if case in head_rows else set()
        fset = set(cell_links(final_rows[case]["holding"]))
        for L in hset - fset:
            drops.append({"case": case, "route": L[0], "target": L[1], "surface": L[2]})
        for L in fset - hset:
            adds.append({"case": case, "route": L[0], "target": L[1], "surface": L[2]})

    def totals(rows):
        n = {"page": 0, "glossary": 0, "citing": 0}
        for r in rows.values():
            for route, _t, _s in cell_links(r["holding"]):
                n[route] += 1
        return n

    head_tot, fin_tot = totals(head_rows), totals(final_rows)

    # verification metrics
    blanks = [c for c, r in final_rows.items() if r["good"].strip() == ""]
    case_pages = {os.path.splitext(f)[0] for f in os.listdir(CASES_DIR)
                  if f.endswith(".md")}
    unresolved_case = []
    for c in final_rows:
        if is_flagged(c):
            continue
        m = re.match(r"^\[\[([^\]|]+)\]\]$", c)
        if not m:
            unresolved_case.append(c)
        elif m.group(1) not in case_pages:
            unresolved_case.append(c)

    spot = {}
    for label, key in [("Mitcham", "[[State v. Mitcham]]"),
                       ("Perez", "[[United States v. Perez]]"),
                       ("Loera", "[[United States v. Loera]]"),
                       ("Aguilar", "[[Aguilar v. Texas]]"),
                       ("Evans", "[[Arizona v. Evans]]")]:
        if key in final_rows:
            spot[label] = final_rows[key]["holding"]

    R = {
        "regen_rows": diag["regen_rows"], "flagged": diag["flagged"],
        "brief_mentions": diag["brief_mentions"],
        "final_data_rows": len(final_rows),
        "cases_on_disk": len(case_pages),
        "flagged_rows_final": sum(1 for c in final_rows if is_flagged(c)),
        "changed_n": len(changed), "unchanged_n": len(unchanged),
        "added": added, "removed": removed,
        "fidelity_fail": fidelity_fail,
        "flagged_overridden": diag["flagged_overridden"],
        "guard_off_links": diag["guard_off_links"],
        "guard_on_links": diag["guard_on_links"],
        "head_tot": head_tot, "fin_tot": fin_tot,
        "head_total": sum(head_tot.values()), "fin_total": sum(fin_tot.values()),
        "n_drops": len(drops), "n_adds": len(adds),
        "drops": drops, "adds": adds,
        "dead_targets": diag["dead_targets"],
        "blank_goodlaw": blanks, "unresolved_case_cells": unresolved_case,
        "changed_cases": sorted(changed),
        "spotcheck": spot,
    }
    print(json.dumps(R, ensure_ascii=False, indent=1))

    if write:
        with open(INDEX, "w", encoding="utf-8") as fh:
            fh.write(final_text)
        # FIN-INDEX-fixes.jsonl: one row per applied term-link change vs HEAD
        with open(os.path.join(HERE, "FIN-INDEX-fixes.jsonl"), "w", encoding="utf-8") as fh:
            for a in adds:
                fh.write(json.dumps({"row": "fin-index.fix.v1", "op": "add-link",
                    "cell": a["case"], "route": a["route"], "target": a["target"],
                    "surface": a["surface"], "reason": "P2/P3-corrected holding; "
                    "S8 register re-derives this routed term on the fresh text",
                    "lane": "FIN-INDEX", "model": "claude-opus-4-8"},
                    ensure_ascii=False) + "\n")
            for d in drops:
                fh.write(json.dumps({"row": "fin-index.fix.v1", "op": "drop-link",
                    "cell": d["case"], "route": d["route"], "target": d["target"],
                    "surface": d["surface"], "reason": "surface text removed by "
                    "P2/P3 holding correction; no register surface survives in the "
                    "new text", "lane": "FIN-INDEX", "model": "claude-opus-4-8"},
                    ensure_ascii=False) + "\n")
        # drop log (human + machine): every HEAD link whose surface vanished
        with open(os.path.join(HERE, "FIN-INDEX-droplog.jsonl"), "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"row": "fin-index.droplog.v1", "kind": "header",
                "head_total_links": sum(head_tot.values()),
                "final_total_links": sum(fin_tot.values()),
                "unchanged_cells_reproduced": len(unchanged),
                "fidelity_fail": fidelity_fail}, ensure_ascii=False) + "\n")
            for d in drops:
                head_holding = head_rows[d["case"]]["holding"]
                fin_holding = final_rows[d["case"]]["holding"]
                fh.write(json.dumps({"row": "fin-index.droplog.v1", "kind": "drop",
                    "cell": d["case"], "dropped_link_surface": d["surface"],
                    "dropped_target": d["target"], "route": d["route"],
                    "head_holding": head_holding, "final_holding": fin_holding},
                    ensure_ascii=False) + "\n")
        print("WROTE", INDEX)
        print("WROTE", os.path.join(HERE, "FIN-INDEX-fixes.jsonl"))
        print("WROTE", os.path.join(HERE, "FIN-INDEX-droplog.jsonl"))


if __name__ == "__main__":
    main()
