#!/usr/bin/env python3
"""P2 stands-modified tally pass (orchestrator ruling P2-SM-RULING).

A finding where >=2 panel lanes voted "stands-modified" has 2-of-3 agreement
on the MODIFIED pole: the defect is real in substance but overframed / needs
tightening rather than wholesale upholding. Verdict = MODIFIED, fix routed to
P3 as a tightening item. Findings without a >=2 SM agreement are untouched.

Default --dry-run stages rows to P2-SM-STAGED.jsonl + report; --write appends
to adjudications.jsonl. Idempotent; skips already-adjudicated findings.
"""
import json, sys, datetime, collections

RUN = "_run/s9"
PANEL = {"codex-A", "codex-B", "claude-opus-panel"}
RULING = "_run/s9/P2-SM-RULING.json"


def load_jsonl(path):
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def main():
    write = "--write" in sys.argv
    findings = {f["id"]: f for f in load_jsonl(f"{RUN}/findings.jsonl")}
    adjudicated = {a.get("finding_id") for a in load_jsonl(f"{RUN}/adjudications.jsonl")}
    triage = {t["finding_id"]: t for t in load_jsonl(f"{RUN}/P2-CLASS-TRIAGE.jsonl")}

    votes_by_fid = collections.defaultdict(dict)
    for v in load_jsonl(f"{RUN}/votes.jsonl"):
        lane = v.get("lane")
        fid = v.get("finding_id")
        if fid and lane in PANEL:
            votes_by_fid[fid][lane] = v.get("verdict")

    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    staged, skipped_patterns = [], collections.Counter()
    for fid, tally in sorted(votes_by_fid.items()):
        if fid in adjudicated or fid not in findings:
            continue
        n_sm = sum(1 for x in tally.values() if x == "stands-modified")
        if n_sm < 2:
            skipped_patterns[tuple(sorted(tally.values()))] += 1
            continue
        tr = triage.get(fid, {})
        staged.append({
            "schema": "s9.adjudication.v1",
            "finding_id": fid,
            "refute_tally": {
                "per-lane": tally,
                "rule": ">=2-of-3 stands-modified -> MODIFIED (P2-SM-RULING)",
                "result": f"{n_sm}x stands-modified agreement",
            },
            "verdict": "MODIFIED",
            "adjudicated_holding": [
                f"P2 SM tally adjudication (class={tr.get('class','?')}): defect real in substance "
                f"but overframed; adopt the tightening framing. {tr.get('one_line','')}".strip(),
                "fix routed to P3 as tightening item",
            ],
            "evidence": [
                {"kind": "tally", "ref": "votes.jsonl 3-lane quorum incl. P2 backfill"},
                {"kind": "ruling", "ref": RULING},
                {"kind": "triage", "ref": f"P2-CLASS-TRIAGE.jsonl {fid}"},
            ],
            "adjudicator": {"lane": "claude-fable-5-orchestrator", "model": "claude-fable-5",
                            "note": "P2 stands-modified tally pass"},
            "needs_cl": bool(tr.get("needs_cl")),
            "at": now,
        })

    report = {
        "staged_total": len(staged),
        "by_pattern": collections.Counter(
            "+".join(sorted(r["refute_tally"]["per-lane"].values())) for r in staged),
        "by_class": collections.Counter(
            triage.get(r["finding_id"], {}).get("class", "?") for r in staged),
        "written": write,
    }
    with open(f"{RUN}/P2-SM-STAGED.jsonl", "w") as fh:
        for r in staged:
            fh.write(json.dumps(r, sort_keys=True) + "\n")
    if write:
        with open(f"{RUN}/adjudications.jsonl", "a") as fh:
            for r in staged:
                fh.write(json.dumps(r, sort_keys=True) + "\n")
    report["by_pattern"] = dict(report["by_pattern"])
    report["by_class"] = dict(report["by_class"])
    with open(f"{RUN}/P2-SM-DRYRUN.json", "w") as fh:
        json.dump(report, fh, indent=1)
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
