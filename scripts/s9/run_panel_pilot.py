#!/usr/bin/env python3
"""S9 R1 panel-review PILOT driver (orchestrator work-order, 2026-07-09).

Runs 3 diverse groups (1 case / 1 doctrine / 1 reference-index) x BOTH Codex
lenses through the LIVE panel-review lane, SERIALLY (the Thread-N fleet is at
concurrency 6 — this pilot stays single-file to avoid overload), under ONE
SHARED InvocationBudget(cap=6) so no repair re-run can exceed the <=6 live-codex
ceiling. Writes to a SEPARATE pilot ledger dir (never the production _run/s9
ledger). Prints a per-invocation summary; dumps a pilot report JSON at the end.
"""
import json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_runner as lr
import panel_review as pr

LEDGER = os.path.join(lr.REPO_ROOT, "_run", "s9", "panel-pilot")
PILOT_GROUPS = [
    ("content/cases/Adams v. Williams.md", "case"),
    ("content/foundations-and-the-fourth-amendment/Common Law Origins.md", "doctrine"),
    ("content/instructor-craft-and-study/Three Golden Rules.md", "reference"),
]
TIMEOUT = int(os.environ.get("PILOT_TIMEOUT", "900"))


def main():
    os.makedirs(LEDGER, exist_ok=True)
    budget = lr.InvocationBudget(cap=6)     # SHARED across all 6 invocations
    wl = pr.load_worklist_index()
    inv = pr.load_inventory_index()
    results = []
    t_start = time.time()
    for gid, klass in PILOT_GROUPS:
        for lens in ("A", "B"):
            t0 = time.time()
            tag = "%s[%s]" % (os.path.basename(gid), lens)
            print("[%s] START %s (budget used=%d/%d)"
                  % (time.strftime("%H:%M:%S"), tag, budget.used, budget.cap), flush=True)
            try:
                s = pr.run_panel_review(gid, lens, "pilot", budget,
                                        ledger_dir=LEDGER, timeout_s=TIMEOUT,
                                        worklist_idx=wl, inv_by_id=inv)
            except lr.AuthError as e:
                print("[%s] AUTH-FAIL %s: %s" % (time.strftime("%H:%M:%S"), tag, str(e)[:200]), flush=True)
                results.append({"group": gid, "lens": lens, "error": "auth", "detail": str(e)[:400]})
                continue
            except Exception as e:  # noqa: BLE001 — pilot must journal, not die
                print("[%s] ERROR %s: %r" % (time.strftime("%H:%M:%S"), tag, e), flush=True)
                results.append({"group": gid, "lens": lens, "error": repr(e)})
                continue
            dt = time.time() - t0
            print("[%s] DONE  %s parse=%s findings=%d votes=%d clean_attest=%s wall=%.1fs tokens=%s"
                  % (time.strftime("%H:%M:%S"), tag, s.get("parse_status"),
                     len(s.get("findings_emitted") or []), len(s.get("votes_emitted") or []),
                     s.get("clean_attestation"), dt, (s.get("tokens") or {}).get("total")),
                  flush=True)
            s["driver_wall_s"] = round(dt, 1)
            results.append(s)
    total = time.time() - t_start
    report = {"schema": "s9.panel-pilot-report.v1", "at": lr._now(),
              "ledger_dir": LEDGER, "budget_used": budget.used, "budget_cap": budget.cap,
              "total_wall_s": round(total, 1), "invocations": results}
    rp = os.path.join(LEDGER, "PILOT-REPORT.json")
    with open(rp, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print("\n[%s] PILOT COMPLETE: %d invocations, budget %d/%d, wall %.1fs -> %s"
          % (time.strftime("%H:%M:%S"), len(results), budget.used, budget.cap, total, rp), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
