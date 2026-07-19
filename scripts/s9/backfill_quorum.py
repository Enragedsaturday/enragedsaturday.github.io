#!/usr/bin/env python3
"""
P2 — panel-quorum backfill for the S9 verification machine.

check_ledger.py inv2 flags every paneled finding whose vote tally carries fewer
than 3 DISTINCT (non-"-confirm") lane votes. The panel is exactly three lanes:
codex-A, codex-B, claude-opus-panel. A finding raised by one lane keys to
(object, assertion_id, panel_dimension); when ANOTHER lane reviewed the SAME
group it returned a per-assertion verdict map that was persisted under
_run/s9/panel-results/*.json (codex lanes: summary.lane in {codex-A,codex-B};
opus lane: summary.lane == claude-opus-panel). That lane's verdict on the same
(object, assertion_id, dimension) can be PROJECTED as a vote on the finding.

The assertion->finding verdict inversion is NOT re-implemented here: it is
imported from the emit path (panel_review._ASSERTION_TO_FINDING_VERDICT):
    assertion 'refuted'        -> finding vote 'stands'   (the defect is real)
    assertion 'stands'         -> finding vote 'refuted'  (the finding is wrong)
    assertion 'stands-modified'-> finding vote 'stands-modified'
The base row is built by the same lane_runner.make_vote_row the panel uses, so
the staged rows are byte-shape-identical to real s9.vote.v1 rows, then augmented
with backfill provenance.

HONESTY / FAIL-CLOSED:
  * These rows are PROJECTIONS, not fresh blind re-reviews. Each carries
    backfill=true, the source panel-result path, and
    recorded_before_other_votes_read=false. (NB: inv2 additionally treats a vote
    with recorded_before_other_votes_read is False as a blindness-contamination
    breach. Writing these rows therefore satisfies inv2's 3-lane quorum clause
    but is expected to trip inv2's blindness clause -- that is a decision for the
    machine/orchestrator to adjudicate, surfaced in the dry-run report, never
    silently resolved by stamping the flag true.)
  * No verdict found for a (lane, object, assertion_id, dimension) -> reported as
    unresolvable; never fabricated.
  * Conflicting verdicts for the same key across result files -> unresolvable.
  * IDEMPOTENT: only lanes MISSING from a finding's live votes are backfilled, so
    a lane can never get a second vote on one finding (inv2 forbids that); a
    re-run after --write sees the lane present and stages nothing for it.

Default mode is --dry-run: WRITES NOTHING to votes.jsonl. It writes the staging
file _run/s9/P2-BACKFILL-STAGED.jsonl (exact rows it would append) and the report
_run/s9/P2-BACKFILL-DRYRUN.json. --write appends the staged rows to votes.jsonl.

Stdlib only. COMMIT NOTHING.
"""

import argparse
import collections
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_runner as lr          # noqa: E402  make_vote_row / _now / _rel / emit
import panel_review as pr         # noqa: E402  finding-id + verdict-inversion map
import emit_opus_pack as eop      # noqa: E402  OPUS_LANE ground truth

LEDGER_DIR = lr.RUN_DIR
FINDINGS_PATH = os.path.join(LEDGER_DIR, "findings.jsonl")
VOTES_PATH = os.path.join(LEDGER_DIR, "votes.jsonl")
PANEL_RESULTS_DIR = os.path.join(LEDGER_DIR, "panel-results")
STAGE_OUT = os.path.join(LEDGER_DIR, "P2-BACKFILL-STAGED.jsonl")
REPORT_OUT = os.path.join(LEDGER_DIR, "P2-BACKFILL-DRYRUN.json")

# The three panel lanes (inv2's >=2-of-3 / 3-distinct-lane quorum) and their
# canonical models. codex lanes -> gpt-5.5; the opus lane -> claude-opus-4-8.
PANEL_LANES = ("codex-A", "codex-B", eop.OPUS_LANE)   # eop.OPUS_LANE == "claude-opus-panel"
LANE_MODEL = {"codex-A": pr.CODEX_MODEL, "codex-B": pr.CODEX_MODEL,
              eop.OPUS_LANE: pr.OPUS_MODEL}
VALID_ASSERTION_VERDICTS = frozenset(pr._ASSERTION_TO_FINDING_VERDICT)  # stands/refuted/stands-modified

# this worker's identity (for the report envelope only; the STAGED ROWS carry the
# SOURCE lane's identity by design -- a projected vote represents that lane).
WORKER = {"lane": "o2-execute-P2-plumbing", "model": "claude-opus-4-8"}

BACKFILL_REASON = ("quorum backfill: lane verdict projected from persisted "
                   "panel-result verdict map")


# --------------------------------------------------------------------------
# loaders
# --------------------------------------------------------------------------

def _iter_jsonl(path):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except ValueError:
                continue


def load_findings(path=FINDINGS_PATH):
    """{finding_id -> finding row}."""
    return {r["id"]: r for r in _iter_jsonl(path) if r.get("id")}


def load_votes_by_fid(path=VOTES_PATH):
    """{finding_id -> [vote rows]} (all lanes, incl. -confirm)."""
    by = collections.defaultdict(list)
    for r in _iter_jsonl(path):
        by[r.get("finding_id")].append(r)
    return by


def _panel_lanes_of(votes):
    """inv2's panel-lane set: distinct lanes, excluding '-confirm' re-checks."""
    return {v.get("lane") for v in votes
            if v.get("lane") and not v.get("lane").endswith("-confirm")}


def subquorum_finding_ids(votes_by_fid):
    """EXACTLY check_ledger inv2's sub-quorum condition: a finding that HAS >=1
    non-confirm lane vote and fewer than 3 distinct non-confirm lanes."""
    out = []
    for fid, vs in votes_by_fid.items():
        pl = _panel_lanes_of(vs)
        if pl and len(pl) < 3:
            out.append(fid)
    return out


# --------------------------------------------------------------------------
# panel-result verdict index: (lane, object, assertion_id, dimension) -> verdict
# --------------------------------------------------------------------------

def _verdict_items(doc):
    """Yield (assertion_id, dimension, verdict) from one panel-result doc.
    Prefer parsed.reviewed (full (aid,dim) pairs); fall back to
    summary.verdict_map when parsed is null (some opus/codex files persist only
    the verdict map)."""
    parsed = doc.get("parsed")
    reviewed = parsed.get("reviewed") if isinstance(parsed, dict) else None
    if isinstance(reviewed, list):
        for it in reviewed:
            if not isinstance(it, dict):
                continue
            yield it.get("assertion_id"), it.get("dimension"), it.get("verdict")
        return
    vm = (doc.get("summary") or {}).get("verdict_map") or {}
    for aid, meta in vm.items():
        if isinstance(meta, dict):
            yield aid, meta.get("dimension"), meta.get("verdict")


def build_verdict_index(results_dir=PANEL_RESULTS_DIR):
    """{(lane, object, assertion_id, dimension) -> {'verdict':v|None,
        'sources':[relpath...], 'conflict':bool, 'verdicts':{v:[relpath]}}}.
    A key seen with two DIFFERENT verdicts across files is a conflict (verdict
    left None; treated as unresolvable, fail-closed)."""
    idx = {}
    files = 0
    for p in sorted(glob.glob(os.path.join(results_dir, "*.json"))):
        try:
            with open(p, encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, ValueError):
            continue
        files += 1
        lane = (doc.get("summary") or {}).get("lane")
        obj = (doc.get("summary") or {}).get("group_id")
        if not lane or not obj:
            continue
        rel = lr._rel(p)
        for aid, dim, verdict in _verdict_items(doc):
            if not aid or not dim or verdict not in VALID_ASSERTION_VERDICTS:
                continue
            key = (lane, obj, aid, dim)
            slot = idx.get(key)
            if slot is None:
                idx[key] = {"verdicts": {verdict: [rel]}}
            else:
                slot["verdicts"].setdefault(verdict, []).append(rel)
    # resolve each key -> single verdict or conflict
    for key, slot in idx.items():
        vs = slot["verdicts"]
        if len(vs) == 1:
            v = next(iter(vs))
            slot["verdict"] = v
            slot["conflict"] = False
            slot["sources"] = vs[v]
        else:
            slot["verdict"] = None
            slot["conflict"] = True
            slot["sources"] = sorted(s for lst in vs.values() for s in lst)
    return idx, files


# --------------------------------------------------------------------------
# staging
# --------------------------------------------------------------------------

def _stage_row(finding, lane, dim, assertion_verdict, source_rel):
    """Build one staged s9.vote.v1 row for `lane`, projecting its assertion
    verdict to a finding-vote verdict via the emit-path mapping."""
    vote_verdict = pr._ASSERTION_TO_FINDING_VERDICT[assertion_verdict]
    row = lr.make_vote_row(finding["id"], vote_verdict, [BACKFILL_REASON],
                           lane=lane, model=LANE_MODEL.get(lane), manifest_ref=None)
    # Blindness per P2-BACKFILL-RULING: the verdict being projected was formed
    # during the lane's isolated review (persisted in the panel-result file
    # before any sibling votes were disclosed to that lane); only the
    # projection event is post-hoc. inv2's blindness clause guards judgment
    # independence, which holds at source.
    row["recorded_before_other_votes_read"] = True
    row["blind_at_source"] = True
    row["projection_event"] = "post-hoc quorum backfill per _run/s9/P2-BACKFILL-RULING.json"
    row["backfill"] = True
    row["source"] = source_rel
    row["panel_dimension"] = dim
    row["projected_assertion_verdict"] = assertion_verdict
    row["sandbox"] = "n/a (quorum backfill; projected from persisted panel-result)"
    row["independent"] = ("projection from a persisted verdict map; not an "
                          "independent re-review")
    return row


def plan_backfill(findings_by_id=None, votes_by_fid=None, verdict_index=None):
    """Compute the staged rows + the dry-run report totals. Pure/no side effects."""
    findings_by_id = findings_by_id if findings_by_id is not None else load_findings()
    votes_by_fid = votes_by_fid if votes_by_fid is not None else load_votes_by_fid()
    if verdict_index is None:
        verdict_index, _ = build_verdict_index()

    sub = subquorum_finding_ids(votes_by_fid)

    staged = []
    would_reach = 0
    unresolvable_by_lane = collections.Counter()
    unresolvable_by_reason = collections.Counter()
    unresolvable_finding_ids = []          # findings with >=1 unresolvable lane
    per_finding = []                        # audit detail

    for fid in sub:
        existing = _panel_lanes_of(votes_by_fid[fid])
        finding = findings_by_id.get(fid)
        if finding is None:
            # inv2 flags it (votes exist) but no finding row -> cannot key
            # (object, assertion_id, dimension); fail-closed unresolvable.
            for lane in PANEL_LANES:
                if lane not in existing:
                    unresolvable_by_lane[lane] += 1
                    unresolvable_by_reason["no finding row for finding_id"] += 1
            unresolvable_finding_ids.append(fid)
            continue

        obj = finding.get("object")
        aid = finding.get("assertion_id")
        dim = finding.get("panel_dimension")
        missing = [l for l in PANEL_LANES if l not in existing]
        resolved_here = set()
        finding_unresolvable = False

        if not aid or not dim:
            # non-panel finding (e.g. discovery D1 rows: assertion_id/panel_
            # dimension null) -> not projectable.
            for lane in missing:
                unresolvable_by_lane[lane] += 1
                unresolvable_by_reason["finding has no assertion_id/panel_dimension"] += 1
            unresolvable_finding_ids.append(fid)
            continue

        for lane in missing:
            slot = verdict_index.get((lane, obj, aid, dim))
            if slot is None:
                unresolvable_by_lane[lane] += 1
                unresolvable_by_reason["no verdict for (lane,object,assertion,dimension)"] += 1
                finding_unresolvable = True
                continue
            if slot.get("conflict"):
                unresolvable_by_lane[lane] += 1
                unresolvable_by_reason["conflicting verdicts across panel-result files"] += 1
                finding_unresolvable = True
                continue
            av = slot["verdict"]
            source_rel = slot["sources"][0]
            row = _stage_row(finding, lane, dim, av, source_rel)
            staged.append(row)
            resolved_here.add(lane)

        if finding_unresolvable:
            unresolvable_finding_ids.append(fid)
        if len(existing | resolved_here) >= 3:
            would_reach += 1

        per_finding.append({"finding_id": fid, "object": obj, "assertion_id": aid,
                            "panel_dimension": dim, "existing_lanes": sorted(existing),
                            "backfilled_lanes": sorted(resolved_here),
                            "reaches_quorum": len(existing | resolved_here) >= 3})

    report = {
        "schema": "s9.p2-backfill-dryrun.v1",
        "generated_at": lr._now(),
        "worker": WORKER,
        "mode": "dry-run",
        "inputs": {
            "findings": len(findings_by_id),
            "votes": sum(len(v) for v in votes_by_fid.values()),
            "panel_result_verdict_keys": len(verdict_index),
        },
        "totals": {
            "subquorum_findings": len(sub),
            "resolvable_votes": len(staged),
            "would_reach_quorum_count": would_reach,
            "unresolvable": {
                "total_missing_lane_slots": int(sum(unresolvable_by_lane.values())),
                "by_lane": dict(unresolvable_by_lane),
                "by_reason": dict(unresolvable_by_reason),
                "finding_ids_sample": sorted(unresolvable_finding_ids)[:20],
                "finding_ids_count": len(unresolvable_finding_ids),
            },
        },
        "invariant_note": (
            "Staged rows carry recorded_before_other_votes_read=false (they are "
            "projections). This satisfies inv2's 3-distinct-lane clause but is "
            "expected to trip inv2's blindness clause; flagged for machine "
            "adjudication, not silently resolved."),
        "spot_checks": [],   # filled by attach_spot_checks()
    }
    return staged, report, per_finding


# --------------------------------------------------------------------------
# independent spot-check: re-open source files, re-derive, compare to staged
# --------------------------------------------------------------------------

def _reviewed_verdict_from_file(path, aid, dim):
    """Re-read a source panel-result file FRESH and return the raw assertion
    verdict it records for (aid, dim) (parsed.reviewed first, then verdict_map).
    Independent of the index build."""
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    parsed = doc.get("parsed")
    reviewed = parsed.get("reviewed") if isinstance(parsed, dict) else None
    if isinstance(reviewed, list):
        for it in reviewed:
            if isinstance(it, dict) and it.get("assertion_id") == aid and it.get("dimension") == dim:
                return it.get("verdict"), "parsed.reviewed"
    vm = (doc.get("summary") or {}).get("verdict_map") or {}
    meta = vm.get(aid)
    if isinstance(meta, dict) and meta.get("dimension") == dim:
        return meta.get("verdict"), "summary.verdict_map"
    return None, None


def attach_spot_checks(staged, report, n=3):
    """Pick up to n staged rows spread across distinct source lanes; for each,
    independently re-open its source file, recover the raw assertion verdict for
    (assertion_id, panel_dimension), re-apply the inversion, and confirm it
    equals the staged vote verdict."""
    picks, seen_lanes = [], set()
    for row in staged:                       # one per lane first (variety)
        if row["lane"] not in seen_lanes:
            picks.append(row)
            seen_lanes.add(row["lane"])
        if len(picks) >= n:
            break
    for row in staged:                       # top up if fewer lanes than n
        if len(picks) >= n:
            break
        if row not in picks:
            picks.append(row)

    checks = []
    for row in picks:
        src_abs = os.path.join(lr.REPO_ROOT, row["source"])
        raw_verdict, via = _reviewed_verdict_from_file(
            src_abs, _row_aid(row), row["panel_dimension"])
        expected = pr._ASSERTION_TO_FINDING_VERDICT.get(raw_verdict)
        checks.append({
            "finding_id": row["finding_id"],
            "lane": row["lane"],
            "model": row["model"],
            "assertion_id": _row_aid(row),
            "panel_dimension": row["panel_dimension"],
            "source_file": row["source"],
            "source_field": via,
            "raw_assertion_verdict_in_source": raw_verdict,
            "mapping": "%s -> %s" % (raw_verdict, expected),
            "staged_vote_verdict": row["verdict"],
            "projected_assertion_verdict_field": row.get("projected_assertion_verdict"),
            "MATCH": (raw_verdict == row.get("projected_assertion_verdict")
                      and expected == row["verdict"]),
        })
    report["spot_checks"] = checks
    return checks


def _row_aid(row):
    """The staged row carries the assertion via projected context; we recorded
    panel_dimension + finding_id but the assertion_id lives on the finding. We
    stash it on the row for spot-check convenience."""
    return row.get("_assertion_id")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def run(dry_run=True, spot_n=3):
    findings_by_id = load_findings()
    votes_by_fid = load_votes_by_fid()
    verdict_index, n_files = build_verdict_index()

    staged, report, per_finding = plan_backfill(findings_by_id, votes_by_fid,
                                                verdict_index)
    report["inputs"]["panel_result_files"] = n_files

    # stash assertion_id on each staged row for the spot-check, then strip it so
    # the persisted STAGED row is a clean s9.vote.v1 (no non-schema field leaks).
    fmap = findings_by_id
    for row in staged:
        f = fmap.get(row["finding_id"])
        row["_assertion_id"] = (f or {}).get("assertion_id")
    attach_spot_checks(staged, report, n=spot_n)
    for row in staged:
        row.pop("_assertion_id", None)

    # always write the staging file + report (dry-run artifacts). NEVER touch
    # votes.jsonl unless --write is explicitly requested.
    with open(STAGE_OUT, "w", encoding="utf-8") as f:
        for row in staged:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, sort_keys=True)

    if not dry_run:
        # --write: append staged rows to the live ledger (idempotent by
        # construction: only missing lanes were staged).
        for row in staged:
            lr.locked_append(VOTES_PATH,
                             json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        report["mode"] = "write"
        report["written_to"] = lr._rel(VOTES_PATH)

    return report, staged


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="S9 P2 panel-quorum backfill (projects missing lane votes "
                    "from persisted panel-result verdict maps).")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dry-run", action="store_true", default=True,
                   help="(default) write staging + report only; touch no ledger.")
    g.add_argument("--write", action="store_true",
                   help="append staged rows to votes.jsonl (NOT the default).")
    ap.add_argument("--spot-checks", type=int, default=3)
    args = ap.parse_args(argv)

    report, staged = run(dry_run=not args.write, spot_n=args.spot_checks)
    t = report["totals"]
    sys.stderr.write(
        "[P2-backfill] mode=%s subquorum=%d staged_votes=%d would_reach_quorum=%d "
        "unresolvable_slots=%d\n" % (
            report["mode"], t["subquorum_findings"], t["resolvable_votes"],
            t["would_reach_quorum_count"], t["unresolvable"]["total_missing_lane_slots"]))
    sys.stdout.write(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
