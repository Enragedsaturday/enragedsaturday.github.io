#!/usr/bin/env python3
"""
S6 R11 coverage-ledger assembler (COH-15 reconciliation artifact).

Assembles `_run/s6-coverage-ledger.json` PROGRAMMATICALLY from the signed S6
disposition artifacts + the S2 lake manifest — one row per distinct caption in
the S6 candidate universe, each with EXACTLY ONE terminal state:

    authored | brief-mention | excluded-remit | unverifiable | removed |
    folded-alias | watch

Sources (all read-only; zero CL calls):
  - _run/o2-execute/s6-authored-ledger.jsonl        (145 authored)
  - _run/o2-execute/davis-fold.jsonl                (1 folded-alias)
  - _run/o2-execute/packet-a-alias-folds.jsonl      (3 folded-alias)
  - _run/o2-execute/s6-removals.jsonl               (2 removed)
  - _run/o2-execute/R8-NONPAGE-LEDGER.json          (58 non-page placements)
  - _run/s6-candidates/gated.jsonl                  (R2 gate: EXCLUDE terminals)
  - _run/o2-execute/packetb-dispositions.jsonl      (borderline excluded-remit)
  - _overhaul2/lake/_manifest.json                  (records + stub statuses)

Every `authored` row is machine-verified: page file present, lake record
present, manifest rename present. Folded rows name their survivor. Partition is
checked (every caption exactly one terminal) and the arithmetic printed.

Usage:  python3 _overhaul2/scripts/build_coverage_ledger.py [--write]
Exit 0 iff the partition + authored verifications pass.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
RUN = os.path.join(REPO, "_run")
O2 = os.path.join(RUN, "o2-execute")
CAND = os.path.join(RUN, "s6-candidates")
LAKE = os.path.join(REPO, "_overhaul2", "lake")
CASES = os.path.join(REPO, "content", "cases")

TERMINALS = {"authored", "brief-mention", "excluded-remit", "unverifiable",
             "removed", "folded-alias", "watch"}


def norm(name):
    n = (name or "").strip().lower()
    n = n.replace("’", "'").replace(" ", " ")
    n = re.sub(r"\s+", " ", n)
    return n


def load_jsonl(path):
    out = []
    with open(path, encoding="utf-8") as fh:
        for ln in fh:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            out.append(json.loads(ln))
    return out


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


class Ledger:
    def __init__(self):
        self.rows = {}          # norm-caption -> row dict
        self.conflicts = []     # (caption, terminal_a src_a, terminal_b src_b)

    def add(self, caption, canonical, terminal, *, cluster_id=None, leg=None,
            verdict=None, prong=None, rationale=None, cl=None, independent=None,
            pointer=None, survivor=None, source=None, aliases=None,
            page_backed=False, note=None):
        assert terminal in TERMINALS, "bad terminal %r" % terminal
        key = norm(caption)
        row = {
            "caption": caption,
            "canonical": canonical or caption,
            "cluster_id": cluster_id,
            "leg": leg,
            "gate": {"verdict": verdict, "prong": prong, "rationale": rationale},
            "keys": {"cl": cl, "independent": independent},
            "terminal": terminal,
            "pointer": pointer,
            "page_backed": page_backed,
            "source": source,
        }
        if survivor:
            row["survivor"] = survivor
        if aliases:
            row["aliases"] = aliases
        if note:
            row["note"] = note
        if key in self.rows:
            prev = self.rows[key]
            if prev["terminal"] != terminal:
                # authored wins over any non-page state (a caption with a page
                # is authored regardless of a same-caption mention/noted-order).
                order = {"authored": 0}
                pa = order.get(prev["terminal"], 1)
                na = order.get(terminal, 1)
                if na < pa:
                    self.conflicts.append((caption, prev["terminal"],
                                           prev.get("source"), terminal, source,
                                           "kept-new"))
                    self.rows[key] = row
                elif pa < na:
                    self.conflicts.append((caption, prev["terminal"],
                                           prev.get("source"), terminal, source,
                                           "kept-prev"))
                else:
                    self.conflicts.append((caption, prev["terminal"],
                                           prev.get("source"), terminal, source,
                                           "UNRESOLVED"))
            else:
                # same terminal from two sources: merge aliases/note, keep first
                if aliases:
                    prev.setdefault("aliases", [])
                    for a in aliases:
                        if a not in prev["aliases"]:
                            prev["aliases"].append(a)
            return
        self.rows[key] = row


def main():
    write = "--write" in sys.argv[1:]
    manifest = load_json(os.path.join(LAKE, "_manifest.json"))
    recs = {r["record_id"]: r for r in manifest["records"]}
    renames = {r["new"]: r["old"] for r in manifest["renames"]}
    stubs = {r["record_id"]: r for r in manifest["records"]
             if r.get("page_path") is None}

    L = Ledger()

    # ---- 1) authored (145) --------------------------------------------------
    authored = load_jsonl(os.path.join(O2, "s6-authored-ledger.jsonl"))
    for r in authored:
        cap = r["record_id_after"]
        rec = recs.get(cap, {})
        L.add(cap, cap, "authored",
              cluster_id=rec.get("cluster_id"),
              leg=r.get("leg"),
              verdict="INGEST", prong=r.get("prong"),
              rationale=(r.get("basis") or "") or "gate-passing named-in-prose (D1 flip)",
              cl="cluster %s (CL identity, R1 key-1)" % rec.get("cluster_id"),
              independent="web/reporter Rule-quote match (R8 mint key-2)",
              pointer=r.get("page"),
              page_backed=True,
              source="s6-authored-ledger.jsonl")

    # ---- 2) folded-alias ----------------------------------------------------
    def survivor_pointer(name):
        p = os.path.join("content", "cases", "%s.md" % name)
        return p if os.path.isfile(os.path.join(REPO, p)) else None

    for r in load_jsonl(os.path.join(O2, "davis-fold.jsonl")):
        rid = r["record_id"]
        rec = recs.get(rid, {})
        cap = rec.get("caption") or "United States v. Davis"
        L.add(cap, cap, "folded-alias", cluster_id=rec.get("cluster_id"),
              leg="frontier", verdict="fold", prong=None,
              rationale=r.get("source"),
              cl="cluster %s" % rec.get("cluster_id"), independent="R9/A18 duplicate-cluster guard",
              survivor=r["folded_into"], pointer=survivor_pointer(r["folded_into"]),
              source="davis-fold.jsonl")
    for r in load_jsonl(os.path.join(O2, "packet-a-alias-folds.jsonl")):
        rid = r["record_id"]
        rec = recs.get(rid, {})
        cap = rec.get("caption") or rid
        surv = r["controlling_case"]
        L.add(cap, cap, "folded-alias", cluster_id=rec.get("cluster_id"),
              leg="roster (packet-A §b)", verdict="fold", prong=None,
              rationale=r.get("source"),
              cl="cluster %s" % rec.get("cluster_id"), independent="packet-A group-2 adjudication",
              survivor=surv, pointer=survivor_pointer(surv),
              source="packet-a-alias-folds.jsonl")
    # alasaad successor-official fold (manifest not_found stub, R9)
    if "alasaad-v-mayorkas--u782a2d04" in stubs:
        L.add("Alasaad v. Mayorkas", "Alasaad v. Mayorkas", "folded-alias",
              cluster_id=None, leg="roster (R9 successor-official)",
              verdict="fold", prong=None,
              rationale="R9 successor-official fold: Mayorkas caption = same 1st-Cir. litigation as authored Alasaad v. Wolf",
              cl="not_found stub (CL identity unresolved on the Mayorkas caption)",
              independent="R9 alias rule",
              survivor="Alasaad v. Wolf", pointer=survivor_pointer("Alasaad v. Wolf"),
              source="manifest:not_found+R9")

    # ---- 3) removed ---------------------------------------------------------
    for r in load_jsonl(os.path.join(O2, "s6-removals.jsonl")):
        rid = r["record_id"]
        rec = recs.get(rid, {})
        cap = rec.get("caption") or r.get("caption") or rid
        L.add(cap, cap, "removed", cluster_id=rec.get("cluster_id"),
              leg=r.get("leg"), verdict="REMOVE", prong=None,
              rationale=r.get("basis"),
              cl="fabrication_suspected stub (both legs NOT-FOUND)",
              independent="dual-blind web exhausted (R4)",
              pointer="omissions-register tombstone; s7 re-anchor=%s" % r.get("s7_reanchor"),
              source="s6-removals.jsonl")

    # ---- 4) non-page ledger (R8-NONPAGE-LEDGER.json) ------------------------
    nonpage = load_json(os.path.join(O2, "R8-NONPAGE-LEDGER.json"))

    DISP2TERM = {
        "noted-order": "brief-mention",
        "brief-mention/bullet": "brief-mention",
        "watch": "watch",
        "fold": "folded-alias",
        "excluded-remit": "excluded-remit",
    }
    FOLD_SURVIVOR = {
        "Lombardo v. St. Louis": "Lombardo v. City of St. Louis",
        "King v. Brownback": "Brownback v. King",
    }
    for e in nonpage["noted_orders_watch_fold"]:
        cap = e["caption"]
        term = DISP2TERM[e["disposition"]]
        surv = FOLD_SURVIVOR.get(cap)
        L.add(cap, cap, term, cluster_id=None, leg=e.get("leg"),
              verdict=("fold" if term == "folded-alias" else
                       ("WATCH" if term == "watch" else "INGEST")),
              prong=e.get("prong"), rationale=e.get("note"),
              cl="sweep docket %s" % e.get("docket"),
              independent="official Term summary / order",
              pointer=e.get("target_node"),
              survivor=surv,
              source="R8-NONPAGE-LEDGER:noted_orders_watch_fold")

    for e in nonpage["mentions_and_bullets"]:
        rid = e.get("record_id")
        rec = recs.get(rid, {}) if rid else {}
        cap = rec.get("caption") or rid
        term = DISP2TERM.get(e["disposition"], "brief-mention")
        verdict = "EXCLUDE" if term == "excluded-remit" else "INGEST"
        L.add(cap, cap, term, cluster_id=e.get("cluster_id") or rec.get("cluster_id"),
              leg="mention/frontier", verdict=verdict, prong=None,
              rationale=e.get("note"),
              cl="cluster %s (verified_identity shell)" % (e.get("cluster_id") or rec.get("cluster_id")),
              independent="doctrine-node mention (S8 links)",
              pointer=e.get("target_node"),
              source="R8-NONPAGE-LEDGER:mentions_and_bullets")

    for e in nonpage["escalation_resolutions_2026_07_07"]:
        rid = e.get("record_id")
        rec = recs.get(rid, {}) if rid else {}
        cap = e.get("caption") or rec.get("caption") or rid
        term_raw = e["terminal"]
        term = {"excluded_remit": "excluded-remit",
                "watch_s7_deferred": "watch"}.get(term_raw, term_raw)
        L.add(cap, cap, term, cluster_id=rec.get("cluster_id"),
              leg="escalation-terminal", verdict=("EXCLUDE" if term == "excluded-remit" else "WATCH"),
              prong=None, rationale=e.get("note"),
              cl="cluster %s (verified_identity shell)" % rec.get("cluster_id"),
              independent=e.get("craft") or "S7-deferred adjudication",
              pointer=None, source="R8-NONPAGE-LEDGER:escalation_resolutions")

    # ---- 4b) W9 terminal overrides (davis precedent: in-row terminal_override,
    #          lake untouched) — documented in R8-WAVE-W9-REPORT.md §4 + the
    #          final 148-row table. Not in a JSONL, so encoded explicitly.
    if "united-states-v-holcomb--10670143" in stubs:
        rec = stubs["united-states-v-holcomb--10670143"]
        L.add(rec.get("caption") or "United States v. Holcomb",
              "United States v. Holcomb", "watch",
              cluster_id=rec.get("cluster_id"), leg="roster (W9)",
              verdict="WATCH", prong=None,
              rationale="cited opinion 132 F.4th 1118 WITHDRAWN by ca9 order 2025-09-11 (non-citable), no successor; page-less watch",
              cl="cluster 10670143 (verified_identity); withdrawn cluster 10365516",
              independent="ca9 No. 23-469 withdrawal order",
              pointer="ca9 No. 23-469 / withdrawn cluster 10365516",
              source="R8-WAVE-W9-REPORT.md:§4")
    if "zorn-v-linton--10813527" in stubs:
        rec = stubs["zorn-v-linton--10813527"]
        L.add(rec.get("caption") or "Zorn v. Linton",
              "Zorn v. Linton", "unverifiable",
              cluster_id=rec.get("cluster_id"), leg="roster (SEED §c residue)",
              verdict=None, prong="c",
              rationale="corrupt CL cluster 10813527 (Strike 3 text; nulls); real SCOTUS per curiam No. 25-297 but no usable cluster/cite; off-CL identity is S9-adjacent",
              cl="cluster 10813527 CORRUPT (data-escalation/unverifiable-pending)",
              independent="off-CL SCOTUS No. 25-297 (no usable machine cite)",
              pointer=None, source="R8-WAVE-W9-REPORT.md:§4")

    # ---- 5) gated EXCLUDE (R2 out-of-remit terminals) -----------------------
    for r in load_jsonl(os.path.join(CAND, "gated.jsonl")):
        if r.get("verdict") != "EXCLUDE":
            continue
        cap = r["caption"]
        # Villarreal captions are fully re-adjudicated in packet-B item 12
        # (panel supersedes the writer gate) — placed explicitly below.
        if cap.startswith("Villarreal"):
            continue
        L.add(cap, cap, "excluded-remit", cluster_id=None, leg=r.get("leg"),
              verdict="EXCLUDE", prong=r.get("prong"),
              rationale=r.get("rationale"),
              cl="gate-candidate (no lake row; sweep/gap leg)",
              independent="R2 officer-field-relevance gate",
              pointer=None, source="gated.jsonl:EXCLUDE")

    # ---- 6) packet-B excluded-remit (borderline; no page) -------------------
    PB_PAGE_TERMS = {"ingest-author", "ingest-author-own-page",
                     "ingest-author-all-three", "split", "referent-resolved",
                     "ingest-noted-order-mention"}
    for e in load_jsonl(os.path.join(O2, "packetb-dispositions.jsonl")):
        if "item" not in e:
            continue
        if e.get("terminal") != "excluded-remit":
            continue
        cap = e["caption"]
        L.add(cap, cap, "excluded-remit", cluster_id=None, leg="sweep (packet-B)",
              verdict="EXCLUDE", prong=(e.get("prong") if e.get("prong") != "none" else None),
              rationale=e.get("note"),
              cl="gate-candidate (borderline packet-B)",
              independent="user-delegated 3-agent panel (2026-07-06)",
              pointer=None, source="packetb-dispositions.jsonl")

    # Villarreal referent split (packet-B item 12): Texas 24-557 = excluded;
    # City of Laredo = alias of Villarreal v. Alaniz brief-mention row.
    L.add("Villarreal v. Texas", "Villarreal v. Texas", "excluded-remit",
          cluster_id=None, leg="gap GAP-04f (packet-B item 12)",
          verdict="EXCLUDE", prong=None,
          rationale="referent-resolved: No. 24-557, 6A no-consultation recess order = trial-side craft (REJECT stands)",
          cl="gate-candidate (no lake row)",
          independent="packet-B panel adjudication",
          pointer=None, source="packetb-dispositions.jsonl:item12")
    L.add("Villarreal v. City of Laredo", "Villarreal v. City of Laredo", "folded-alias",
          cluster_id=None, leg="gap GAP-04f (packet-B item 12)",
          verdict="fold", prong="c",
          rationale="5th-Cir en banc merits of the Laredo/Lagordiloca litigation = same identity as Villarreal v. Alaniz noted-order row; Lower-court-developments bullet",
          cl="one ledger identity with Villarreal v. Alaniz",
          independent="R9 same-litigation fold",
          survivor="Villarreal v. Alaniz", pointer=None,
          source="packetb-dispositions.jsonl:item12")

    # ---- 6c) S7 mini-lane L1 pooling dispositions (spec R9 named split) ------
    # The signed R9/§11 named horizontal-pooling split (Massenburg / communication-
    # nexus circuits / Cook-Balser) needs its page-less split members to carry
    # brief-mention terminals so LINT-17 lets the Collective Knowledge page name
    # them. Identity-verified via CourtListener MCP (SEARCH-first; 0 REST). Rows
    # flagged "assemble": false are documentation-only (identity corrections) and
    # are NOT assembled — e.g. the Cook identity note, which leaves the pre-existing
    # ledger row untouched (writer != checker on the coverage machinery).
    s7pool = os.path.join(O2, "S7-L1-POOLING-DISPOSITIONS.jsonl")
    if os.path.isfile(s7pool):
        for e in load_jsonl(s7pool):
            if e.get("assemble") is False:
                continue
            L.add(e["caption"], e.get("canonical") or e["caption"], e["terminal"],
                  cluster_id=e.get("cluster_id"), leg=e.get("leg"),
                  verdict=e.get("verdict"), prong=e.get("prong"),
                  rationale=e.get("rationale"),
                  cl=e.get("cl"), independent=e.get("independent"),
                  pointer=e.get("pointer"), aliases=e.get("aliases"),
                  note=e.get("note"),
                  source="S7-L1-POOLING-DISPOSITIONS.jsonl")

    # ---- 6c-2) S7 mini-lane L2 SACO/constructive-entry dispositions (D7) -----
    # The signed D7 SACO section names the constructive-entry split; its page-less
    # split members need brief-mention terminals so LINT-17 lets the Entry-to-Arrest
    # section name them. Identity-verified via CourtListener MCP (SEARCH-first; 0
    # REST). assemble=false rows are the 3 page-mint candidates (Nora/Al-Azzawy/
    # Vaneaton) blocked on the S2 REST identity leg — documentation-only, NOT
    # assembled (they enter as `authored` rows when the S2 builder resolves their
    # verified_identity stub and mint_page authors the staged payloads).
    s7saco = os.path.join(O2, "S7-L2-SACO-DISPOSITIONS.jsonl")
    if os.path.isfile(s7saco):
        for e in load_jsonl(s7saco):
            if e.get("assemble") is False:
                continue
            L.add(e["caption"], e.get("canonical") or e["caption"], e["terminal"],
                  cluster_id=e.get("cluster_id"), leg=e.get("leg"),
                  verdict=e.get("verdict"), prong=e.get("prong"),
                  rationale=e.get("rationale"),
                  cl=e.get("cl"), independent=e.get("independent"),
                  pointer=e.get("pointer"), aliases=e.get("aliases"),
                  note=e.get("note"),
                  source="S7-L2-SACO-DISPOSITIONS.jsonl")

    # ---- 6b) any remaining page_path=None manifest stub not yet placed ------
    # (verified_identity brief-mention shells whose caption did not text-match a
    # non-page-ledger record_id — belt-and-braces: place by manifest status.)
    STATUS2TERM = {
        "verified_identity": "brief-mention",
        "not_found": "brief-mention",
        "fabrication_suspected": "removed",
        "folded-alias": "folded-alias",
    }
    for rid, rec in stubs.items():
        cap = rec.get("caption") or rid
        if norm(cap) in L.rows:
            continue
        term = STATUS2TERM.get(rec.get("status"), "brief-mention")
        L.add(cap, cap, term, cluster_id=rec.get("cluster_id"),
              leg="lake-stub (manifest)", verdict=None, prong=None,
              rationale="manifest stub status=%s, page_path=None; placed by status" % rec.get("status"),
              cl="cluster %s / status %s" % (rec.get("cluster_id"), rec.get("status")),
              independent="manifest reconciliation",
              pointer=None, source="manifest:stub-residual")

    # ---- verification: authored rows ---------------------------------------
    v_page = v_rec = v_rename = 0
    for row in L.rows.values():
        if row["terminal"] != "authored":
            continue
        cap = row["caption"]
        if os.path.isfile(os.path.join(CASES, "%s.md" % cap)):
            v_page += 1
        else:
            row["_ERR"] = "missing page file"
        if cap in recs:
            v_rec += 1
        else:
            row["_ERR"] = (row.get("_ERR", "") + " missing lake record").strip()
        if cap in renames:
            v_rename += 1
        else:
            row["_ERR"] = (row.get("_ERR", "") + " missing manifest rename").strip()

    # ---- verification: folded rows name a survivor -------------------------
    fold_ok = fold_bad = 0
    for row in L.rows.values():
        if row["terminal"] != "folded-alias":
            continue
        if row.get("survivor"):
            fold_ok += 1
        else:
            fold_bad += 1
            row["_ERR"] = "folded-alias without survivor"

    # ---- partition proof ----------------------------------------------------
    from collections import Counter
    by_term = Counter(r["terminal"] for r in L.rows.values())
    total = len(L.rows)
    authored_n = by_term["authored"]

    errs = [r for r in L.rows.values() if r.get("_ERR")]

    out = {
        "generated": "2026-07-07",
        "lane": "s6-coverage-ledger",
        "model": "claude-opus-4-8",
        "spec": "S6 R11 (COH-15 joint reconciliation)",
        "terminal_enum": sorted(TERMINALS),
        "note": ("One row per distinct caption in the S6 candidate universe. "
                 "Assembled programmatically from the signed disposition artifacts + "
                 "the S2 lake manifest (build_coverage_ledger.py). NUM-04's 388-mention "
                 "reconciliation is a LEDGER PROPERTY: rows carry page_backed + pointer so "
                 "S8 links every mention whose caption has a page and applies opinion-link/"
                 "plain to the rest. The 388-caption bare-mention universe is a MEASURED S8 "
                 "input (NUM-04); it is not present as a machine artifact in the repo trees, "
                 "so it is not re-derived here (no fabricated reconciliation)."),
        "counts": {
            "total_rows": total,
            "by_terminal": dict(sorted(by_term.items())),
            "authored_verified": {"page_file": v_page, "lake_record": v_rec,
                                  "manifest_rename": v_rename, "of": authored_n},
            "folded_with_survivor": {"ok": fold_ok, "bad": fold_bad},
            "conflicts": len(L.conflicts),
            "errors": len(errs),
        },
        "partition_arithmetic": None,  # filled below
        "conflicts": [
            {"caption": c[0], "kept": c[5], "prev": {"terminal": c[1], "src": c[2]},
             "new": {"terminal": c[3], "src": c[4]}}
            for c in L.conflicts
        ],
        "rows": sorted(L.rows.values(), key=lambda r: (r["terminal"], r["caption"])),
    }

    # arithmetic string
    parts = " + ".join("%s %d" % (k, v) for k, v in sorted(by_term.items()))
    out["partition_arithmetic"] = "%s = %d distinct captions" % (parts, total)

    # ---- corpus_mention_baseline (R12/LINT-17 frozen snapshot) --------------
    # The page-less bare-mention captions the corpus prose carries that are NOT
    # in the S6 candidate universe above: NUM-04 residue R11 assigns to S8's
    # plain-link rule. Frozen here so LINT-17 goes green on the real corpus AND a
    # NEW bare caption (post-close) still fails. Built with LINT-17's own
    # extractor+page-coverage so the allowlist exactly covers the scan.
    sys.path.insert(0, os.path.join(REPO, "scripts", "lint"))
    import _common as lc  # noqa: E402
    import lint17_coverage as l17  # noqa: E402

    idx = lc.build_corpus_index()
    page_tokenlists = l17.build_page_tokenlists(idx)
    cu_allow = set()
    for r in L.rows.values():
        if r["terminal"] == "authored":
            continue
        cu_allow.add(lc.CorpusIndex.norm(r["caption"]))
        cu_allow.add(lc.CorpusIndex.norm(r["canonical"]))
        for a in r.get("aliases", []) or []:
            cu_allow.add(lc.CorpusIndex.norm(a))

    # documented manifest exclusions → recorded non-page terminals
    placeholders = {lc.CorpusIndex.norm(e["caption"]): e
                    for e in manifest["exclusions"].get("citation_format_placeholders", [])}
    ignore_rows = {lc.CorpusIndex.norm(e["caption"]): e
                   for e in manifest["exclusions"].get("s6_ignore_rows", [])}

    # field-relevant page-less landmarks flagged for D1-flip review (surfaced,
    # NOT adjudicated here — writer != checker; orchestrator/S9 decides).
    ESCALATE = {lc.CorpusIndex.norm(x) for x in [
        "Anderson v. Creighton", "Bell v. Wolfish",
        "Colonnade Catering Corp. v. United States"]}

    baseline = {}
    for path in lc.iter_markdown_files(None):
        text = lc.read_text(path)
        for cap in l17.extract_captions(text):
            n = lc.CorpusIndex.norm(cap)
            if l17.covered_by_page(cap, idx, page_tokenlists):
                continue
            if n in cu_allow:
                continue
            if n in baseline:
                baseline[n]["mentions"] += 1
                continue
            if n in placeholders:
                row = {"caption": cap, "canonical": cap, "cluster_id": None,
                       "leg": "manifest:exclusions.citation_format_placeholders",
                       "terminal": "excluded-remit",
                       "gate": {"verdict": "citation-format-placeholder",
                                "prong": None,
                                "rationale": "pedagogical citation-format example, not a real authority (manifest signed exclusion)"},
                       "pointer": (placeholders[n].get("sources") or [None])[0],
                       "mentions": 1, "source": "manifest:citation_format_placeholders"}
            elif n in ignore_rows:
                row = {"caption": cap, "canonical": cap, "cluster_id": None,
                       "leg": "manifest:exclusions.s6_ignore_rows",
                       "terminal": "excluded-remit",
                       "gate": {"verdict": "ignore-row", "prong": None,
                                "rationale": ignore_rows[n].get("reason")},
                       "pointer": None, "mentions": 1,
                       "source": "manifest:s6_ignore_rows"}
            else:
                row = {"caption": cap, "canonical": cap, "cluster_id": None,
                       "leg": "corpus-mention-scan (NUM-04 bare-mention residue)",
                       "terminal": "brief-mention",
                       "gate": {"verdict": "not-adjudicated (S8 plain-link)",
                                "prong": None,
                                "rationale": "page-less bare mention in pre-S6 prose; outside the S6 candidate legs; S8 applies its plain/opinion-link rule (R11 'the rest')"},
                       "pointer": lc.relpath(path), "mentions": 1,
                       "source": "corpus-mention-scan"}
                if n in ESCALATE:
                    row["escalate"] = ("field-relevant SCOTUS landmark, page-less "
                                       "— D1-flip page candidate; orchestrator/S9 to adjudicate")
            baseline[n] = row

    from collections import Counter as _Ctr
    base_terms = _Ctr(r["terminal"] for r in baseline.values())
    escal = [r for r in baseline.values() if r.get("escalate")]
    out["corpus_mention_baseline"] = sorted(baseline.values(),
                                            key=lambda r: r["caption"])
    out["counts"]["corpus_mention_baseline"] = {
        "total": len(baseline),
        "by_terminal": dict(sorted(base_terms.items())),
        "escalations": len(escal),
        "note": ("LINT-17 frozen allowlist tail: page-less bare-mention captions "
                 "outside the S6 candidate universe. NOT the NUM-04 388 (a measured "
                 "S8 input absent as a machine artifact) — this is LINT-17's own "
                 "corpus scan of the CURRENT prose."),
    }
    print("-" * 72)
    print("  corpus_mention_baseline: %d (%s) | escalations=%d"
          % (len(baseline),
             ", ".join("%s %d" % kv for kv in sorted(base_terms.items())),
             len(escal)))
    for r in escal:
        print("    ESCALATE %s" % r["caption"])

    # ---- report -------------------------------------------------------------
    print("=" * 72)
    print("S6 COVERAGE LEDGER — partition proof")
    print("=" * 72)
    for k, v in sorted(by_term.items()):
        print("  %-16s %4d" % (k, v))
    print("  %-16s %4d" % ("TOTAL", total))
    print("-" * 72)
    print("  partition: %s" % out["partition_arithmetic"])
    print("  authored verified: page=%d rec=%d rename=%d  (of %d)"
          % (v_page, v_rec, v_rename, authored_n))
    print("  folded-alias survivors: ok=%d bad=%d" % (fold_ok, fold_bad))
    print("  conflicts: %d   row-errors: %d" % (len(L.conflicts), len(errs)))
    if L.conflicts:
        print("-" * 72)
        for c in L.conflicts:
            print("  CONFLICT %-32s %s(%s) vs %s(%s) -> %s"
                  % (c[0][:32], c[1], c[2], c[3], c[4], c[5]))
    if errs:
        print("-" * 72)
        for r in errs:
            print("  ROW-ERR  %-40s %s" % (r["caption"][:40], r["_ERR"]))

    ok = (v_page == v_rec == v_rename == authored_n and fold_bad == 0
          and not errs and all(c[5] != "UNRESOLVED" for c in L.conflicts))

    if write:
        # strip internal _ERR before writing
        for r in out["rows"]:
            r.pop("_ERR", None)
        dest = os.path.join(RUN, "s6-coverage-ledger.json")
        with open(dest, "w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)
        print("-" * 72)
        print("  WROTE %s (%d rows)" % (dest, total))

    print("=" * 72)
    print("  RESULT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
