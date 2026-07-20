#!/usr/bin/env python3
"""P3 fix applier — validates worker-emitted fix rows and appends to fixes.jsonl.

Input: one or more JSONL files of s9.fix.v1 rows emitted by fix workers.
Guards (fail the row, never the batch): finding must be in the P3 queue;
not already FIXED; status in {FIXED, NOT-FIXED}; author lane present and not
an adjudicator lane; change_summary + verification non-empty for FIXED rows.
NOT-FIXED rows are echoed to _run/s9/p3/notfixed-loop<N>.jsonl for the loop
protocol instead of the ledger? No — NOT-FIXED rows ARE ledger rows (they
document an attempt) but only a later FIXED row or an escalation closes the
finding. We append both, and report the outstanding set.

Usage: apply_fixes.py <rows.jsonl>... [--dry-run]
"""
import json, sys, collections, os

RUN = "_run/s9"


def load(path):
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def final_loop_verdict(fx):
    loops = fx.get("loops") or []
    if loops:
        return (loops[-1].get("re_review") or {}).get("verdict")
    s = fx.get("status")
    return s if s in ("FIXED", "NOT-FIXED") else None


def main():
    srcs = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    queue = {q["finding_id"] for q in load(f"{RUN}/p3/P3-QUEUE.jsonl")}
    existing = load(f"{RUN}/fixes.jsonl")
    already_fixed = {fx.get("finding_id") for fx in existing
                     if final_loop_verdict(fx) == "FIXED"}

    ok, bad = [], []
    seen_fixed = set()
    for src in srcs:
        for r in load(src):
            fid = r.get("finding_id")
            err = None
            if r.get("schema") != "s9.fix.v1":
                err = "bad schema"
            elif fid not in queue:
                err = "not in P3 queue"
            elif fid in already_fixed:
                err = "already FIXED in ledger"
            elif r.get("status") not in ("FIXED", "NOT-FIXED"):
                err = f"bad status {r.get('status')}"
            elif not (r.get("author") or {}).get("lane"):
                err = "missing author.lane"
            elif (r.get("author") or {}).get("lane") == "claude-fable-5-orchestrator":
                err = "adjudicator lane cannot author fixes (role separation)"
            elif r.get("status") == "FIXED" and fid in seen_fixed:
                err = "duplicate FIXED row in batch"
            elif r.get("status") == "FIXED" and not (r.get("change_summary") and r.get("verification")):
                err = "FIXED row missing change_summary/verification"
            if err:
                bad.append((src, fid, err))
            else:
                if r.get("status") == "FIXED":
                    seen_fixed.add(fid)
                ok.append(r)

    if not dry and ok:
        with open(f"{RUN}/fixes.jsonl", "a") as fh:
            for r in ok:
                fh.write(json.dumps(r, sort_keys=True) + "\n")

    now_fixed = already_fixed | {r["finding_id"] for r in ok if r["status"] == "FIXED"}
    outstanding = sorted(queue - now_fixed)
    print(json.dumps({
        "applied": len(ok),
        "by_status": dict(collections.Counter(r["status"] for r in ok)),
        "rejected": bad,
        "queue_outstanding": len(outstanding),
        "dry_run": dry,
    }, indent=1))
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
