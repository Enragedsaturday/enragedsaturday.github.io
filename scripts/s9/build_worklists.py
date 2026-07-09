#!/usr/bin/env python3
"""
S9 P1 work-queue partitioner (spec S9 R5 ordering; §9 batch-width lever).

Reads the FROZEN thread-P.json (R5) + the assertion inventory (R2) and emits the
three P1 worklists under `_run/s9/worklists/`:

  * thread-n-cases.jsonl   — 609 case-grain blind reads (Codex lanes), R5 tier
                             ORDERING (recency -> negatives -> rule-bearing ->
                             high-profile -> rest), batch width ~15. cached-text
                             presence is checked LEAD-OPINION-first; a case whose
                             lead opinion text is not in the pool is flagged
                             `no_cached_text` and routed to the live-CL identity
                             slice (NOT silently dropped) — e.g. Thornton (lead
                             opinion 9434613 is KNOWN-absent from the cache).
  * panel-review.jsonl     — paneled legal-assertion surfaces grouped per object
                             (existence/support/quote-fidelity/pincite/treatment/
                             black-letter), batched per page.
  * doctrine-rederive.jsonl — 115 doctrine-grain re-derivation items (the FABLE
                             lane runs these; this script only PARTITIONS them).

Freeze precondition (R5): thread-P.json's items[] must hash to its own
`content_hash` (imported from the sibling build_thread_p, never forked) before any
worklist is issued. A drifted freeze aborts.

Invariants self-checked (fail-closed, --self-test):
  * every thread-P case appears in exactly ONE thread-n-cases batch (partition);
  * case-row count == thread-P case count; doctrine-row count == doctrine count;
  * Thornton is present and flagged `no_cached_text` (the KNOWN-absent probe);
  * cached_text_present is consistent with the pool on disk.

Stdlib only. COMMIT NOTHING. Content/lake read-only. Zero CL.
"""

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import build_thread_p as btp  # noqa: E402  (import, don't fork — R5 canonicalizer)

POOL_ROOT = "/Users/johngalt/cssi-lake"
TEXT_DIR = os.path.join(POOL_ROOT, "cache", "text")

RUN_DIR = os.path.join(REPO_ROOT, "_run", "s9")
THREAD_P = os.path.join(RUN_DIR, "thread-P.json")
INVENTORY = os.path.join(RUN_DIR, "assertion-inventory.json")
WORKLIST_DIR = os.path.join(RUN_DIR, "worklists")

CASE_BATCH_WIDTH = 15      # spec §9 scaling lever
PAGE_BATCH_WIDTH = 12      # pages per panel-review batch
DOCTRINE_BATCH_WIDTH = 10  # FABLE lane batching

# tier ORDERING only (R5): recency -> negatives -> rule-bearing -> high-profile -> rest
TIER_ORDER = ("recency", "negatives", "rule-bearing", "high-profile", "rest")
RECENCY_YEAR = 2020        # decisions at/after this year lead the queue
NEG_VALIDITY = ("superseded", "caution")
NEG_OVERRIDE = ("superseded", "overruled", "abrogated")
HIGH_PROFILE_EDGES = 100   # treatment-edge prominence threshold
HIGH_PROFILE_HOMES = 3     # or homed on >=3 pages

# inventory kind -> panel dimension (the six paneled legal-assertion surfaces, R1).
# kinds NOT in this map are editorial/structural -> 1 reviewer + lints (D3), not
# the 3-lane panel.
PANEL_DIM = {
    "case_cite": "existence",
    "proposition": "support",
    "home_role": "support",
    "quote_pinpoint": "quote_fidelity",
    "link_pincite": "pincite",
    "treatment": "treatment",
    "treatment_override": "treatment",
    "weight_label": "treatment",
    "registry_callout_pair": "black_letter",
}
PANEL_DIMS = ("existence", "support", "quote_fidelity", "pincite",
              "treatment", "black_letter")


# --------------------------------------------------------------------------
# freeze verification (R5)
# --------------------------------------------------------------------------

def load_thread_p(path=THREAD_P):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    items = d["items"]
    recomputed = btp.content_hash(items)
    declared = d.get("content_hash")
    if recomputed != declared:
        raise SystemExit(
            "FROZEN-FAIL: thread-P items[] hash %s != header content_hash %s; "
            "refusing to issue worklists against a drifted freeze (R5)."
            % (recomputed, declared))
    return d, items


# --------------------------------------------------------------------------
# cached-text resolution (LEAD-OPINION first — the primary-read substrate)
# --------------------------------------------------------------------------

def cached_text_path(case, text_dir=TEXT_DIR):
    """Resolve a case to its cached LEAD-opinion text file, or None.

    The read substrate is the majority/lead opinion (S2 lake identity's
    `lead_opinion_id`), NOT the cluster docket or a sibling. A case with a null
    lead id or an absent `<lead>.txt` has no cached read text -> None (routed to
    the live-CL identity slice). Thornton (lead 9434613) is the KNOWN-absent
    probe: 9434613.txt is not in the pool even though its cluster text is."""
    lead = (case.get("lake") or {}).get("lead_opinion_id")
    if lead is None:
        return None
    p = os.path.join(text_dir, "%s.txt" % lead)
    return p if os.path.exists(p) else None


# --------------------------------------------------------------------------
# tier assignment (ORDERING ONLY — R5 stated limitation)
# --------------------------------------------------------------------------

def tier_of(case):
    """Return (tier_name, tier_rank). First match wins, in R5 priority order."""
    year = case.get("year") or 0
    tr = case.get("treatment") or {}
    fv = tr.get("field_i_validity")
    pos = tr.get("point_overrides") or []
    neg_override = any(po.get("field_i_validity") in NEG_OVERRIDE for po in pos)
    lake = case.get("lake") or {}
    edge = lake.get("treatment_edge_count") or 0
    homes = case.get("homes") or []
    anchor = any("Anchor" in (h.get("role") or "") for h in homes)

    if year >= RECENCY_YEAR:
        return ("recency", 0)
    if fv in NEG_VALIDITY or neg_override:
        return ("negatives", 1)
    if anchor:
        return ("rule-bearing", 2)
    if edge >= HIGH_PROFILE_EDGES or len(homes) >= HIGH_PROFILE_HOMES:
        return ("high-profile", 3)
    return ("rest", 4)


def _within_tier_key(case):
    """Deterministic intra-tier ordering: recency newest-first; high-profile most-
    cited-first; all tiers break ties by title (reproducible)."""
    tier, rank = tier_of(case)
    year = case.get("year") or 0
    edge = (case.get("lake") or {}).get("treatment_edge_count") or 0
    title = case.get("title") or ""
    if tier == "recency":
        return (rank, -year, title)
    if tier == "high-profile":
        return (rank, -edge, title)
    return (rank, title)


# --------------------------------------------------------------------------
# worklist builders
# --------------------------------------------------------------------------

def build_case_worklist(items):
    cases = [it for it in items if it.get("kind") == "case"]
    cases_sorted = sorted(cases, key=_within_tier_key)
    rows = []
    for ordinal, c in enumerate(cases_sorted):
        tier, rank = tier_of(c)
        lake = c.get("lake") or {}
        tp = cached_text_path(c)
        present = tp is not None
        batch = ordinal // CASE_BATCH_WIDTH
        flags = []
        if not present:
            flags.append("no_cached_text")
            flags.append("route:live-cl-identity")  # R5 identity slice, not dropped
        rows.append({
            "schema": "s9.worklist.case.v1",
            "case_id": c.get("p_id"),
            "record_id": lake.get("record_id"),
            "caption": c.get("title"),
            "citation": c.get("citation"),
            "cluster_id": lake.get("cluster_id"),
            "lead_opinion_id": lake.get("lead_opinion_id"),
            "court_level": c.get("court_level"),
            "year": c.get("year"),
            "tier": tier,
            "tier_rank": rank,
            "batch": batch,
            "batch_ordinal": ordinal,
            "cached_text_path": tp,
            "cached_text_present": present,
            "flags": flags,
            "lens_plan": ["A", "B"],
        })
    return rows


def build_doctrine_worklist(items):
    docs = [it for it in items if it.get("kind") == "doctrine"]
    docs_sorted = sorted(docs, key=lambda d: (d.get("type") or "", d.get("path") or ""))
    rows = []
    for ordinal, d in enumerate(docs_sorted):
        cs = d.get("case_set") or {}
        sp = d.get("split") or {}
        rows.append({
            "schema": "s9.worklist.doctrine.v1",
            "doctrine_id": d.get("p_id"),
            "path": d.get("path"),
            "title": d.get("title"),
            "type": d.get("type"),
            "topic": d.get("topic"),
            "homed_case_count": cs.get("homed_count") or cs.get("homed_count", 0),
            "split_signal": bool(sp.get("has_split_signal")),
            "batch": ordinal // DOCTRINE_BATCH_WIDTH,
            "batch_ordinal": ordinal,
            "lane": "claude-doctrine-grain",  # FABLE runs these, not the Codex lanes
        })
    return rows


def build_panel_worklist(inventory_items):
    """Group paneled legal-assertion surfaces per object, batched per page."""
    by_object = {}
    for it in inventory_items:
        dim = PANEL_DIM.get(it.get("kind"))
        if dim is None:
            continue  # editorial/structural — not a 3-lane-panel surface (D3)
        obj = it.get("object")
        rec = by_object.setdefault(obj, {
            "object": obj,
            "object_class": it.get("object_class"),
            "dimensions": {d: [] for d in PANEL_DIMS},
        })
        rec["dimensions"][dim].append(it.get("assertion_id"))
    objects = sorted(by_object.values(), key=lambda r: r["object"] or "")
    rows = []
    for ordinal, rec in enumerate(objects):
        total = sum(len(v) for v in rec["dimensions"].values())
        rows.append({
            "schema": "s9.worklist.panel.v1",
            "object": rec["object"],
            "object_class": rec["object_class"],
            "page_batch": ordinal // PAGE_BATCH_WIDTH,
            "page_ordinal": ordinal,
            "dimensions": rec["dimensions"],
            "counts": {d: len(rec["dimensions"][d]) for d in PANEL_DIMS},
            "total": total,
            "black_letter_needs_2_approvals": len(rec["dimensions"]["black_letter"]) > 0,
        })
    return rows


# --------------------------------------------------------------------------
# emission + verification
# --------------------------------------------------------------------------

def _write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")


def verify(case_rows, doctrine_rows, items, text_dir=TEXT_DIR):
    """Fail-closed partition + presence invariants. Returns (ok, report)."""
    errs = []
    n_case = sum(1 for it in items if it.get("kind") == "case")
    n_doc = sum(1 for it in items if it.get("kind") == "doctrine")

    # partition: every thread-P case in exactly one batch, no dup, no drop
    ids = [r["case_id"] for r in case_rows]
    if len(ids) != n_case:
        errs.append("case-row count %d != thread-P cases %d" % (len(ids), n_case))
    if len(set(ids)) != len(ids):
        errs.append("duplicate case_ids in worklist (partition broken)")
    p_ids = {it.get("p_id") for it in items if it.get("kind") == "case"}
    missing = p_ids - set(ids)
    extra = set(ids) - p_ids
    if missing:
        errs.append("%d thread-P cases missing from worklist: %s"
                    % (len(missing), sorted(missing)[:3]))
    if extra:
        errs.append("%d worklist cases not in thread-P: %s"
                    % (len(extra), sorted(extra)[:3]))
    # every ordinal maps to exactly one batch (structural)
    for r in case_rows:
        if r["batch"] != r["batch_ordinal"] // CASE_BATCH_WIDTH:
            errs.append("case %s batch/ordinal mismatch" % r["case_id"])
            break

    if len(doctrine_rows) != n_doc:
        errs.append("doctrine-row count %d != thread-P doctrine %d"
                    % (len(doctrine_rows), n_doc))

    # cached-text presence consistent with disk
    for r in case_rows:
        want = r["cached_text_present"]
        got = (r["cached_text_path"] is not None
               and os.path.exists(r["cached_text_path"]))
        if want != got:
            errs.append("case %s cached_text_present=%s but disk=%s"
                        % (r["record_id"], want, got))
            break

    # Thornton KNOWN-absent probe
    thornton = [r for r in case_rows if r["record_id"] == "Thornton v. United States"]
    if not thornton:
        errs.append("Thornton row missing")
    elif "no_cached_text" not in thornton[0]["flags"]:
        errs.append("Thornton not flagged no_cached_text (lead 9434613 should be absent)")
    elif "route:live-cl-identity" not in thornton[0]["flags"]:
        errs.append("Thornton not routed to live-cl-identity slice")

    n_batches = (len(case_rows) + CASE_BATCH_WIDTH - 1) // CASE_BATCH_WIDTH
    n_absent = sum(1 for r in case_rows if not r["cached_text_present"])
    tiers = {}
    for r in case_rows:
        tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    report = {
        "cases": len(case_rows),
        "case_batches": n_batches,
        "batch_width": CASE_BATCH_WIDTH,
        "no_cached_text": n_absent,
        "cached_text_present": len(case_rows) - n_absent,
        "tiers": {t: tiers.get(t, 0) for t in TIER_ORDER},
        "doctrine": len(doctrine_rows),
        "thornton_flagged": bool(thornton and "no_cached_text" in thornton[0]["flags"]),
    }
    return (not errs), {"errors": errs, "report": report}


def build_all(write=True):
    d, items = load_thread_p()
    inv = None
    if os.path.exists(INVENTORY):
        with open(INVENTORY, encoding="utf-8") as f:
            inv = json.load(f).get("items")
    case_rows = build_case_worklist(items)
    doctrine_rows = build_doctrine_worklist(items)
    panel_rows = build_panel_worklist(inv) if inv else []
    ok, vr = verify(case_rows, doctrine_rows, items)
    if write:
        _write_jsonl(os.path.join(WORKLIST_DIR, "thread-n-cases.jsonl"), case_rows)
        _write_jsonl(os.path.join(WORKLIST_DIR, "doctrine-rederive.jsonl"), doctrine_rows)
        if panel_rows:
            _write_jsonl(os.path.join(WORKLIST_DIR, "panel-review.jsonl"), panel_rows)
    vr["report"]["panel_objects"] = len(panel_rows)
    vr["report"]["panel_batches"] = (
        (len(panel_rows) + PAGE_BATCH_WIDTH - 1) // PAGE_BATCH_WIDTH if panel_rows else 0)
    vr["report"]["paneled_assertions"] = sum(r["total"] for r in panel_rows)
    return ok, vr, (case_rows, doctrine_rows, panel_rows)


# --------------------------------------------------------------------------
# self-test (no writes to the real worklists)
# --------------------------------------------------------------------------

def self_test():
    ok, vr, _ = build_all(write=False)
    for k, v in vr["report"].items():
        sys.stderr.write("[self-test] %-22s %s\n" % (k, v))
    if not ok:
        for e in vr["errors"]:
            sys.stderr.write("[self-test] ERROR: %s\n" % e)
    sys.stderr.write("[self-test] build_worklists %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--no-write", action="store_true",
                    help="compute + verify but do not write worklist files")
    args = ap.parse_args()
    if args.self_test:
        sys.exit(self_test())
    ok, vr, _ = build_all(write=not args.no_write)
    sys.stdout.write(json.dumps(vr, ensure_ascii=False, indent=2) + "\n")
    if not ok:
        sys.stderr.write("build_worklists: FAIL (invariants breached)\n")
        sys.exit(1)
    where = "(not written)" if args.no_write else WORKLIST_DIR
    sys.stderr.write("build_worklists: OK -> %s\n" % where)
    sys.exit(0)


if __name__ == "__main__":
    main()
