#!/usr/bin/env python3
"""Post-pilot analysis for the S9 R1 panel-review pilot: parse rates,
findings/votes/attestations produced, per-group economics, and LINT-30 on the
pilot result dir. Read-only; no codex."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import check_ledger

LEDGER = os.path.join(os.path.dirname(os.path.dirname(HERE)),
                      "_run", "s9", "panel-pilot")
if len(sys.argv) > 1:
    LEDGER = sys.argv[1]


def _rows(name):
    p = os.path.join(LEDGER, name)
    out = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def main():
    rep_path = os.path.join(LEDGER, "PILOT-REPORT.json")
    report = json.load(open(rep_path)) if os.path.exists(rep_path) else {"invocations": []}
    invs = report.get("invocations", [])

    print("=== PARSE RATES / PRODUCTION (per invocation) ===")
    ok = 0
    for s in invs:
        if "error" in s:
            print("  %-40s lens=%s ERROR=%s" % (os.path.basename(s.get("group", "?")),
                                                s.get("lens"), s.get("error")))
            continue
        ps = s.get("parse_status")
        if ps in ("parsed", "repaired"):
            ok += 1
        print("  %-34s lens=%s parse=%-9s reviewed=%s/%s findings=%d votes=%d clean=%s wall=%.1fs tok=%s"
              % (os.path.basename(s.get("group", "?")), s.get("lens"), ps,
                 s.get("reviewed_count"), s.get("group_total_assertions"),
                 len(s.get("findings_emitted") or []), len(s.get("votes_emitted") or []),
                 s.get("clean_attestation"), s.get("driver_wall_s") or s.get("wall_clock_s") or 0,
                 (s.get("tokens") or {}).get("total")))
    n = len([s for s in invs if "error" not in s])
    print("  parse-ok: %d/%d (%.0f%%)" % (ok, n, 100.0 * ok / n if n else 0))

    findings = _rows("findings.jsonl")
    votes = _rows("votes.jsonl")
    attests = _rows("panel-attestations.jsonl")
    print("\n=== LEDGER TOTALS ===")
    print("  findings: %d   votes: %d   attestations: %d" % (len(findings), len(votes), len(attests)))
    print("  total wall: %.1fs   budget: %s/%s" % (report.get("total_wall_s", 0),
          report.get("budget_used"), report.get("budget_cap")))

    print("\n=== SAMPLE ROWS ===")
    if findings:
        print("  finding[0]:", json.dumps(findings[0], ensure_ascii=False)[:600])
    if votes:
        print("  vote[0]:", json.dumps(votes[0], ensure_ascii=False)[:600])
    if attests:
        print("  attestation[0]:", json.dumps(attests[0], ensure_ascii=False)[:600])

    print("\n=== LINT-30 on the pilot result dir ===")
    viols, status = check_ledger.check_ledger(LEDGER)
    nh = sum(1 for x in viols if x["severity"] == check_ledger.c.HIGH)
    print("  status=%s HIGH=%d" % (status, nh))
    for x in viols[:12]:
        print("   -", x["message"][:130])


if __name__ == "__main__":
    main()
