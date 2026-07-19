#!/usr/bin/env python3
"""P2 individual-adjudication applier.

Input: a JSONL file of orchestrator verdicts, each row:
  {"finding_id": "...", "verdict": "UPHELD|DISMISSED|MODIFIED|ESCALATE",
   "holding": "one-line reasoned holding", "needs_cl": bool (optional)}

Wraps each into a full s9.adjudication.v1 row (attaching the live panel tally
+ provenance) and appends to adjudications.jsonl. ESCALATE rows are written to
_run/s9/_review-needed-P2.jsonl instead of adjudications (loop-cap protocol).
Idempotent: refuses finding_ids already adjudicated. Prints a summary.

Usage: apply_verdicts.py <verdicts.jsonl> [--dry-run]
"""
import json, sys, datetime, collections

RUN = "_run/s9"
PANEL = {"codex-A", "codex-B", "claude-opus-panel"}
VALID = {"UPHELD", "DISMISSED", "MODIFIED", "ESCALATE"}


def load_jsonl(path):
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def main():
    src = sys.argv[1]
    dry = "--dry-run" in sys.argv
    verdicts = load_jsonl(src)
    findings = {f["id"] for f in load_jsonl(f"{RUN}/findings.jsonl")}
    adjudicated = {a.get("finding_id") for a in load_jsonl(f"{RUN}/adjudications.jsonl")}
    votes_by_fid = collections.defaultdict(dict)
    for v in load_jsonl(f"{RUN}/votes.jsonl"):
        if v.get("lane") in PANEL and v.get("finding_id"):
            votes_by_fid[v["finding_id"]][v["lane"]] = v.get("verdict")

    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    rows, escalates, errors = [], [], []
    seen = set()
    for v in verdicts:
        fid, verdict = v.get("finding_id"), v.get("verdict")
        if fid in seen:
            errors.append((fid, "duplicate in input")); continue
        seen.add(fid)
        if verdict not in VALID:
            errors.append((fid, f"bad verdict {verdict}")); continue
        if fid not in findings:
            errors.append((fid, "unknown finding")); continue
        if fid in adjudicated:
            errors.append((fid, "already adjudicated")); continue
        tally = votes_by_fid.get(fid, {})
        refuted = sum(1 for x in tally.values() if x == "refuted")
        if refuted >= 2 and verdict == "UPHELD":
            errors.append((fid, "inv2 guard: >=2 refutes cannot be UPHELD")); continue
        base = {
            "schema": "s9.adjudication.v1",
            "finding_id": fid,
            "refute_tally": {"per-lane": tally,
                             "rule": "individual orchestrator adjudication (P2 escalate queue)",
                             "result": f"mixed tally; reasoned verdict {verdict}"},
            "verdict": verdict,
            "adjudicated_holding": [v.get("holding", "").strip()],
            "evidence": [
                {"kind": "tally", "ref": "votes.jsonl 3-lane quorum incl. P2 backfill"},
                {"kind": "packet", "ref": v.get("packet", "P2-ESCALATE-PACKETS")},
            ],
            "adjudicator": {"lane": "claude-fable-5-orchestrator", "model": "claude-fable-5",
                            "note": "P2 individual pass over escalate queue"},
            "needs_cl": bool(v.get("needs_cl")),
            "at": now,
        }
        if verdict == "ESCALATE":
            escalates.append(base)
        else:
            rows.append(base)

    if not dry:
        with open(f"{RUN}/adjudications.jsonl", "a") as fh:
            for r in rows:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
        if escalates:
            with open(f"{RUN}/_review-needed-P2.jsonl", "a") as fh:
                for r in escalates:
                    fh.write(json.dumps(r, sort_keys=True) + "\n")
    print(json.dumps({
        "input": len(verdicts), "applied": len(rows), "escalated": len(escalates),
        "errors": errors, "dry_run": dry,
        "verdict_mix": dict(collections.Counter(r["verdict"] for r in rows)),
    }, indent=1))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
