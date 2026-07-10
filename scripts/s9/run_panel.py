#!/usr/bin/env python3
"""S9 R1 panel-review PRODUCTION driver (orchestrator work-order, 2026-07-09).

Walks the ratified v2 panel worklist (_run/s9/worklists/panel-review.v2.jsonl —
ledger-row dropped, registry sharded x3, reference/craft text-promoted) x lenses
A,B and runs every (group, lens) through lane_runner.py --panel-review (fresh
codex exec per lane; R1 isolation is the lane's job). Mirrors run_thread_n.py:
concurrency-pooled SUBPROCESSES, checkpoint/resume from the ledger, one retry per
failed lane, a failures file, progress journaled.

Checkpoint skip (run-id independent): a (group, lens) is DONE if a persisted
panel-results/<lane>.json exists for it OR a clean attestation OR a panel finding
row is present. A result whose parse_status is lane_error / no_review /
manifest_refused is NOT done -> a single automatic RE-DISPATCH cycle re-runs
those at the end.

--wait-for-fleet: poll _run/s9/thread-n-driver.log for the "driver done" line;
start at concurrency 2 while the Thread-N fleet still holds the codex pool, then
auto-ramp to 12 (a shared Semaphore gains permits) the moment the fleet drains.

Production ledger dir = _run/s9/ (findings/votes/attestations mix with the live
ledger; panel finding ids are deterministic so re-review is idempotent). The
pilot rows under _run/s9/panel-pilot/ are left untouched.

Usage:
  python3 scripts/s9/run_panel.py [--concurrency 12] [--initial-concurrency 2]
      [--wait-for-fleet] [--limit N] [--timeout 900] [--run-id prod]
      [--ledger-dir _run/s9] [--worklist ...v2.jsonl] [--dry-run] [--no-redispatch]
Exit: 0 all lanes done (or re-dispatched clean); 1 residual failures.
"""
import argparse, glob, json, os, subprocess, sys, threading, queue, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "s9"))
import panel_review as pr  # noqa: E402  (for _short + worklist/default paths)

RUNNER = os.path.join(ROOT, "scripts/s9/lane_runner.py")
DEFAULT_WORKLIST = os.path.join(ROOT, "_run/s9/worklists/panel-review.v2.jsonl")
DEFAULT_LEDGER = os.path.join(ROOT, "_run/s9")
FLEET_LOG = os.path.join(ROOT, "_run/s9/thread-n-driver.log")
LOG = os.path.join(ROOT, "_run/s9/panel-driver.log")
FAIL_STATES = ("lane_error", "no_review", "manifest_refused", "auth")


def log(msg):
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# --------------------------------------------------------------------------
# checkpoint state — read the ledger (run-id independent)
# --------------------------------------------------------------------------

def _iter_jsonl(path):
    if os.path.exists(path):
        for l in open(path, encoding="utf-8"):
            l = l.strip()
            if l:
                try:
                    yield json.loads(l)
                except ValueError:
                    continue


def ledger_state(ledger_dir):
    """Return (succeeded, failed): sets of (group_id, lens).
      succeeded = a parsed/repaired result, or a clean attestation, or a panel
                  finding row exists for (group, lens).
      failed    = a result exists but its best parse_status is a FAIL_STATE."""
    best = {}   # (group_id, lens) -> best parse_status seen

    def bump(key, status):
        rank = {"parsed": 3, "repaired": 3, "no_review": 1, "lane_error": 1,
                "manifest_refused": 1, "auth": 1}
        if key not in best or rank.get(status, 0) > rank.get(best[key], 0):
            best[key] = status

    for rf in glob.glob(os.path.join(ledger_dir, "panel-results", "*.json")):
        try:
            s = json.load(open(rf, encoding="utf-8")).get("summary", {})
        except (OSError, ValueError):
            continue
        g, lens, st = s.get("group_id"), s.get("lens"), s.get("parse_status")
        if g and lens:
            bump((g, lens), st or "no_review")
    # attestations + panel findings are hard proof of a parsed lane
    for a in _iter_jsonl(os.path.join(ledger_dir, "panel-attestations.jsonl")):
        g = a.get("group_id") or a.get("object")
        if g and a.get("lens"):
            bump((g, a["lens"]), "parsed")
    for f in _iter_jsonl(os.path.join(ledger_dir, "findings.jsonl")):
        if (f.get("found_by") or {}).get("register") != "panel-review.jsonl":
            continue
        lane = (f.get("found_by") or {}).get("lane", "")
        lens = lane.split("-")[-1] if lane.startswith("codex-") else None
        g = f.get("object")
        if g and lens in ("A", "B"):
            bump((g, lens), "parsed")

    succeeded = {k for k, v in best.items() if v in ("parsed", "repaired")}
    failed = {k for k, v in best.items() if v in FAIL_STATES and k not in succeeded}
    return succeeded, failed


def load_worklist(path):
    rows = list(_iter_jsonl(path))
    return rows


# --------------------------------------------------------------------------
# concurrency: a Semaphore that can ramp 2 -> 12 when the fleet drains
# --------------------------------------------------------------------------

def fleet_done():
    """The fleet is done iff NO run_thread_n.py driver process is alive. A stale
    'driver done' line from a prior (since-resumed) run must NOT trigger the ramp
    — the LIVE-process check is authoritative."""
    try:
        out = subprocess.run(["pgrep", "-f", "run_thread_n.py"],
                             capture_output=True, text=True)
        return not (out.returncode == 0 and out.stdout.strip())
    except Exception:  # noqa: BLE001 — pgrep missing -> fall back to the log
        if not os.path.exists(FLEET_LOG):
            return True
        try:
            lines = [l for l in open(FLEET_LOG, encoding="utf-8") if l.strip()]
        except OSError:
            return True
        # done only if the LAST journalled line is a 'driver done'
        return bool(lines) and "driver done" in lines[-1]


def ramp_monitor(sem, initial, target, stop_evt):
    """Bump the permit pool from `initial` to `target` once the fleet drains."""
    added = 0
    while not stop_evt.is_set():
        if fleet_done() and added < (target - initial):
            for _ in range(target - initial - added):
                sem.release()
            added = target - initial
            log("FLEET DRAINED -> ramping panel concurrency %d -> %d" % (initial, target))
            return
        stop_evt.wait(15)


# --------------------------------------------------------------------------
# one lane = one subprocess (isolation; a codex hang can't kill the driver)
# --------------------------------------------------------------------------

def run_lane(group, lens, args):
    for attempt in (1, 2):
        cmd = [sys.executable, RUNNER, "--panel-review", group, "--lens", lens,
               "--run-id", args.run_id, "--timeout", str(args.timeout),
               "--ledger-dir", args.ledger_dir, "--cap", "2",
               "--panel-worklist", args.worklist]
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if p.returncode == 0:
            # a lane_error/no_review returns 0 too (fail-closed, re-dispatchable);
            # rc==3 is a GENUINE auth stop (pause-#8) -> surface, do not retry.
            return True, (p.stdout or "")
        if p.returncode == 3:
            log("AUTH-STOP %s[%s] (pause-#8) rc=3 %s"
                % (os.path.basename(group), lens, (p.stderr or "")[-160:].replace(chr(10), " ")))
            return False, "auth"
        log("FAIL %s[%s] attempt=%d rc=%d %s"
            % (os.path.basename(group), lens, attempt, p.returncode,
               (p.stderr or "")[-160:].replace(chr(10), " ")))
    return False, "rc!=0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=12, help="target/max concurrency")
    ap.add_argument("--initial-concurrency", type=int, default=2)
    ap.add_argument("--wait-for-fleet", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--run-id", default="prod")
    ap.add_argument("--ledger-dir", default=DEFAULT_LEDGER)
    ap.add_argument("--worklist", default=DEFAULT_WORKLIST)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-redispatch", action="store_true")
    args = ap.parse_args()

    rows = load_worklist(args.worklist)
    succeeded, failed = ledger_state(args.ledger_dir)
    todo = []
    for r in rows:
        g = r["object"]
        for lens in ("A", "B"):
            if (g, lens) in succeeded:
                continue
            todo.append((g, lens))
    if args.limit:
        todo = todo[: args.limit]

    log("panel driver: %d groups, %d lanes total, %d already done, %d failed-pending, "
        "%d to run; worklist=%s conc %d->%d wait_for_fleet=%s"
        % (len(rows), len(rows) * 2, len(succeeded), len(failed), len(todo),
           os.path.basename(args.worklist),
           args.initial_concurrency if args.wait_for_fleet else args.concurrency,
           args.concurrency, args.wait_for_fleet))
    if args.dry_run:
        for g, lens in todo[:12]:
            log("would run: %s [%s]" % (g, lens))
        return 0
    if not todo and not (failed and not args.no_redispatch):
        log("nothing to do (all lanes done).")
        return 0

    # --- concurrency pool ---
    start = args.initial_concurrency if args.wait_for_fleet else args.concurrency
    sem = threading.Semaphore(start)
    stop_evt = threading.Event()
    mon = None
    if args.wait_for_fleet and start < args.concurrency:
        mon = threading.Thread(target=ramp_monitor,
                               args=(sem, start, args.concurrency, stop_evt), daemon=True)
        mon.start()

    def worker(q, failures, flock, tag):
        while True:
            try:
                g, lens = q.get_nowait()
            except queue.Empty:
                return
            sem.acquire()
            try:
                ok, why = run_lane(g, lens, args)
            finally:
                sem.release()
            if ok:
                log("ok  %s[%s]%s" % (os.path.basename(g), lens, tag))
            else:
                with flock:
                    failures.append((g, lens, why))
            q.task_done()

    def run_phase(pairs, tag=""):
        q = queue.Queue()
        for it in pairs:
            q.put(it)
        failures, flock = [], threading.Lock()
        nworkers = min(args.concurrency, max(1, len(pairs)))
        threads = [threading.Thread(target=worker, args=(q, failures, flock, tag),
                                    daemon=True) for _ in range(nworkers)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return failures

    t0 = time.time()
    fails = run_phase(todo, tag="")
    log("main pass done in %.0fs; lane failures this pass: %d" % (time.time() - t0, len(fails)))

    # --- one automatic RE-DISPATCH cycle for lane_error/no_review (+ this pass) ---
    if not args.no_redispatch:
        _s2, failed2 = ledger_state(args.ledger_dir)
        redispatch = sorted(failed2 | {(g, l) for g, l, _ in fails})
        # drop any that in fact succeeded on retry
        succ2, _f = ledger_state(args.ledger_dir)
        redispatch = [(g, l) for (g, l) in redispatch if (g, l) not in succ2]
        if redispatch:
            log("RE-DISPATCH cycle: %d lane(s) with lane_error/no_review" % len(redispatch))
            stop_evt.set()                 # ramp done; use full concurrency now
            for _ in range(args.concurrency):
                try:
                    sem.release()
                except ValueError:
                    break
            fails2 = run_phase(redispatch, tag=" (re-dispatch)")
        else:
            fails2 = []
    else:
        fails2 = fails

    stop_evt.set()
    succ_final, failed_final = ledger_state(args.ledger_dir)
    residual = sorted(failed_final)
    dt = time.time() - t0
    log("panel driver COMPLETE in %.0fs; lanes done=%d residual-failed=%d"
        % (dt, len(succ_final), len(residual)))
    if residual:
        fp = os.path.join(args.ledger_dir, "panel-failures.jsonl")
        with open(fp, "w", encoding="utf-8") as f:
            for g, lens in residual:
                f.write(json.dumps({"group": g, "lens": lens}) + "\n")
        log("residual failures -> %s" % fp)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
