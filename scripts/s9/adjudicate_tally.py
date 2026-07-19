#!/usr/bin/env python3
"""
S9 P2 tally-driven adjudication emitter (schema s9.adjudication.v1).

Reads the 3-lane panel vote quorum for every UNADJUDICATED finding and stages a
DISMISSED / UPHELD adjudication row per the machine rule ">=2-of-3 refute kills".

Verdict semantics are FINDING-semantics:
  vote "refuted"        -> the finding is wrong (defect not real)
  vote "stands"         -> the defect is real
  vote "stands-modified"-> the defect is real but the finding needs modification

Panel lanes (exactly three): codex-A, codex-B, claude-opus-panel.
Lanes ending in "-confirm" are NOT counted in the tally.

Staging rule (per-finding, over the 3 panel lanes):
  >= 2 lanes "refuted"      -> DISMISSED   (result "panel >=2-of-3 refute kills")
  else >= 2 lanes "stands"  -> UPHELD      (routed to P3 by class)
  anything else             -> NO row staged; recorded in the ESCALATE report.
    "anything else" = mixed 1-1-1 (refuted/stands/stands-modified), any
    stands-modified-dominant split with no 2-of-3 exact-"stands" majority, or
    an incomplete quorum (< 3 panel lanes voted).

Because DISMISSED is checked first and UPHELD requires >=2 exact "stands"
(hence <=1 refuted), no staged UPHELD can ever carry >=2 refute votes
(check_ledger inv2).

Dry-run (default) writes the staging file + JSON report; it appends NOTHING to
adjudications.jsonl. --write appends the staged rows to adjudications.jsonl.
Idempotent: any finding already present in adjudications.jsonl is skipped.
Stdlib only.
"""
import argparse
import collections
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S9 = os.path.join(ROOT, "_run", "s9")

FINDINGS = os.path.join(S9, "findings.jsonl")
VOTES = os.path.join(S9, "votes.jsonl")
ADJUDICATIONS = os.path.join(S9, "adjudications.jsonl")
TRIAGE = os.path.join(S9, "P2-CLASS-TRIAGE.jsonl")

STAGED_OUT = os.path.join(S9, "P2-ADJUDICATION-STAGED.jsonl")
REPORT_OUT = os.path.join(S9, "P2-ADJUDICATION-DRYRUN.json")

PANEL_LANES = ["codex-A", "codex-B", "claude-opus-panel"]
RULE = ">=2-of-3 refute kills"
ADJUDICATOR = {
    "lane": "claude-fable-5-orchestrator",
    "model": "claude-fable-5",
    "note": "P2 class-wide tally pass",
}


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def load_panel_votes(path):
    """finding_id -> {lane: verdict} restricted to the 3 panel lanes.

    "-confirm" lanes are excluded. If a (lane, finding) pair somehow appears
    more than once, the last-seen verdict wins.
    """
    votes = collections.defaultdict(dict)
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            lane = r.get("lane")
            if lane not in PANEL_LANES:
                continue
            votes[r["finding_id"]][lane] = r.get("verdict")
    return votes


def stage_finding(fid, lane_map, triage_row):
    """Return (verdict, row) if stageable, else (None, escalate_reason)."""
    present = [lane_map[l] for l in PANEL_LANES if l in lane_map]
    if len(present) < 3:
        return None, "quorum_incomplete"

    per_lane = {l: lane_map[l] for l in PANEL_LANES}
    n_refuted = sum(1 for v in present if v == "refuted")
    n_stands = sum(1 for v in present if v == "stands")

    if n_refuted >= 2:
        verdict = "DISMISSED"
        result = "panel >=2-of-3 refute kills"
    elif n_stands >= 2:
        verdict = "UPHELD"
        result = "panel >=2-of-3 stands (defect real); refute below 2-of-3 kill threshold"
    else:
        return None, "mixed_no_2of3"

    cls = triage_row.get("class")
    one_line = triage_row.get("one_line", "")
    holding = "P2 tally adjudication (class={}): {}".format(cls, one_line)
    if verdict == "UPHELD":
        holding = "{}; fix routed to P3 class queue {}".format(holding, cls)

    row = {
        "schema": "s9.adjudication.v1",
        "finding_id": fid,
        "refute_tally": {"per-lane": per_lane, "rule": RULE, "result": result},
        "verdict": verdict,
        "adjudicated_holding": [holding],
        "evidence": [
            {"kind": "tally", "ref": "votes.jsonl 3-lane quorum incl. P2 backfill"},
            {"kind": "triage", "ref": "P2-CLASS-TRIAGE.jsonl {}".format(fid)},
        ],
        "adjudicator": dict(ADJUDICATOR),
        "at": stage_finding.now,
        "needs_cl": triage_row.get("needs_cl"),
    }
    return verdict, row


def independent_recount(fid):
    """Fresh, isolated scan of votes.jsonl for one finding's panel refute count.

    Used by the in-script spot-check so the check does not reuse the staging
    computation's data structures.
    """
    lane_map = {}
    with open(VOTES) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if r.get("finding_id") == fid and r.get("lane") in PANEL_LANES:
                lane_map[r["lane"]] = r.get("verdict")
    refuted = sum(1 for l in PANEL_LANES if lane_map.get(l) == "refuted")
    stands = sum(1 for l in PANEL_LANES if lane_map.get(l) == "stands")
    return lane_map, refuted, stands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="append staged rows to adjudications.jsonl (default: dry-run)")
    args = ap.parse_args()

    stage_finding.now = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")

    already = {r["finding_id"] for r in load_jsonl(ADJUDICATIONS)}
    triage = {r["finding_id"]: r for r in load_jsonl(TRIAGE)}
    panel_votes = load_panel_votes(VOTES)

    staged = []
    escalate = []  # (fid, reason)
    for fid, trow in triage.items():
        if fid in already:
            continue  # idempotent
        lane_map = panel_votes.get(fid, {})
        verdict, payload = stage_finding(fid, lane_map, trow)
        if verdict is None:
            escalate.append((fid, payload))
        else:
            staged.append((verdict, payload))

    # ---- report aggregation ----
    dismissed = [p for v, p in staged if v == "DISMISSED"]
    upheld = [p for v, p in staged if v == "UPHELD"]

    def by_class(rows):
        c = collections.Counter()
        for p in rows:
            c[triage[p["finding_id"]].get("class")] += 1
        return dict(c)

    esc_reason = collections.Counter(r for _, r in escalate)
    esc_pattern = collections.Counter()
    for fid, _ in escalate:
        lm = panel_votes.get(fid, {})
        trip = tuple(sorted((lm.get(l) or "MISSING") for l in PANEL_LANES))
        esc_pattern[" / ".join(trip)] += 1

    # ---- in-script spot-checks: 2 DISMISSED + 2 UPHELD, independent recount ----
    spot_checks = []
    picks = [("DISMISSED", p) for p in dismissed[:2]] + [("UPHELD", p) for p in upheld[:2]]
    for want, p in picks:
        fid = p["finding_id"]
        lane_map2, refuted2, stands2 = independent_recount(fid)
        staged_tally = p["refute_tally"]["per-lane"]
        recomputed = (
            "DISMISSED" if refuted2 >= 2 else ("UPHELD" if stands2 >= 2 else "ESCALATE")
        )
        spot_checks.append({
            "finding_id": fid,
            "staged_verdict": p["verdict"],
            "independent_per_lane": lane_map2,
            "independent_refuted_count": refuted2,
            "independent_stands_count": stands2,
            "recomputed_verdict": recomputed,
            "tally_matches_staged": staged_tally == lane_map2,
            "verdict_matches": recomputed == p["verdict"],
            "result": "pass" if (staged_tally == lane_map2 and recomputed == p["verdict"]) else "fail",
        })

    # ---- inv2 guard: no staged UPHELD may carry >=2 refute votes ----
    inv2_fail = []
    for p in upheld:
        n_ref = sum(1 for v in p["refute_tally"]["per-lane"].values() if v == "refuted")
        if n_ref >= 2:
            inv2_fail.append(p["finding_id"])
    inv2_guard = "pass" if not inv2_fail else "fail"

    report = {
        "generated_at": stage_finding.now,
        "mode": "write" if args.write else "dry-run",
        "inputs": {
            "findings": FINDINGS, "votes": VOTES,
            "adjudications": ADJUDICATIONS, "triage": TRIAGE,
        },
        "already_adjudicated_skipped": len(already),
        "triage_total": len(triage),
        "staged_total": len(staged),
        "dismissed": len(dismissed),
        "upheld": len(upheld),
        "by_class": {"dismissed": by_class(dismissed), "upheld": by_class(upheld)},
        "escalate_count": len(escalate),
        "escalate_by_reason": dict(esc_reason),
        "escalate_pattern_detail": dict(esc_pattern),
        "escalate_finding_ids": [fid for fid, _ in escalate],
        "spot_checks": spot_checks,
        "inv2_guard": inv2_guard,
        "inv2_failures": inv2_fail,
    }

    # ---- outputs ----
    with open(STAGED_OUT, "w") as f:
        for _, p in staged:
            f.write(json.dumps(p) + "\n")
    with open(REPORT_OUT, "w") as f:
        json.dump(report, f, indent=2)

    if args.write:
        with open(ADJUDICATIONS, "a") as f:
            for _, p in staged:
                f.write(json.dumps(p) + "\n")
        sys.stderr.write("WROTE {} rows to {}\n".format(len(staged), ADJUDICATIONS))
    else:
        sys.stderr.write("DRY-RUN: nothing appended to adjudications.jsonl\n")

    sys.stderr.write(
        "staged={} (dismissed={} upheld={}) escalate={} inv2_guard={}\n".format(
            len(staged), len(dismissed), len(upheld), len(escalate), inv2_guard))
    print(json.dumps({
        "staged_total": len(staged), "dismissed": len(dismissed),
        "upheld": len(upheld), "escalate_count": len(escalate),
        "inv2_guard": inv2_guard,
        "staged_out": STAGED_OUT, "report_out": REPORT_OUT,
    }))


if __name__ == "__main__":
    main()
