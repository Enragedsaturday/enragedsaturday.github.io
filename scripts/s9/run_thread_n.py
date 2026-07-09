#!/usr/bin/env python3
"""S9 P1 Thread-N production driver (orchestrator-authored, 2026-07-09).

Walks _run/s9/worklists/thread-n-cases.jsonl and runs every (record, lens) pair
through lane_runner.py --case-read (fresh codex exec per read, R1 isolation is
lane_runner's job). Concurrency-pooled, checkpoint/resume by reading the ledger
(a (case_id, lens) already present in thread-N-reads.jsonl is skipped), one
retry per failed read, progress + failures journaled. Deterministic order:
worklist order (R5 tiering) x lens A then B.

Usage: python3 scripts/s9/run_thread_n.py [--concurrency 6] [--limit N]
       [--ledger-dir _run/s9] [--dry-run]
Exit: 0 all reads present; 1 residual failures (listed in the log + retry file).
"""
import argparse, json, os, subprocess, sys, threading, queue, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKLIST = os.path.join(ROOT, "_run/s9/worklists/thread-n-cases.jsonl")
RUNNER = os.path.join(ROOT, "scripts/s9/lane_runner.py")
LOG = os.path.join(ROOT, "_run/s9/thread-n-driver.log")


def log(msg):
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def done_pairs(ledger_dir):
    path = os.path.join(ledger_dir, "thread-N-reads.jsonl")
    pairs = set()
    if os.path.exists(path):
        for l in open(path, encoding="utf-8"):
            try:
                r = json.loads(l)
            except Exception:
                continue
            cid = r.get("case_id") or r.get("record_id")
            lens = r.get("lens")
            if cid and lens and (r.get("parse_status") in (None, "ok", "repaired")):
                pairs.add((cid, lens))
    return pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0, help="max reads this run (0 = all)")
    ap.add_argument("--ledger-dir", default=os.path.join(ROOT, "_run/s9"))
    ap.add_argument("--timeout", type=int, default=1500)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    wl = [json.loads(l) for l in open(WORKLIST, encoding="utf-8")]
    have = done_pairs(args.ledger_dir)
    todo = []
    for row in wl:
        cid = row.get("record_id") or row.get("case_id")
        for lens in ("A", "B"):
            key = (row.get("case_id") or cid, lens)
            key2 = (cid, lens)
            if key in have or key2 in have:
                continue
            todo.append((cid, lens))
    if args.limit:
        todo = todo[: args.limit]
    log("thread-n driver: %d worklist rows, %d pairs already done, %d to run, concurrency %d"
        % (len(wl), len(have), len(todo), args.concurrency))
    if args.dry_run:
        for cid, lens in todo[:10]:
            log("would run: %s lens=%s" % (cid, lens))
        return 0

    q = queue.Queue()
    for item in todo:
        q.put(item)
    failures, flock = [], threading.Lock()

    def worker():
        while True:
            try:
                cid, lens = q.get_nowait()
            except queue.Empty:
                return
            for attempt in (1, 2):
                cmd = [sys.executable, RUNNER, "--case-read", cid, "--lens", lens,
                       "--run-id", "p1-prod", "--timeout", str(args.timeout),
                       "--ledger-dir", args.ledger_dir]
                p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
                if p.returncode == 0:
                    log("ok  %s lens=%s%s" % (cid, lens, " (retry)" if attempt == 2 else ""))
                    break
                log("FAIL %s lens=%s attempt=%d rc=%d %s"
                    % (cid, lens, attempt, p.returncode, (p.stderr or "")[-200:].replace("\n", " ")))
            else:
                with flock:
                    failures.append((cid, lens))
            q.task_done()

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(args.concurrency)]
    t0 = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    dt = time.time() - t0
    log("driver done in %.0fs; failures: %d" % (dt, len(failures)))
    if failures:
        fpath = os.path.join(args.ledger_dir, "thread-n-failures.jsonl")
        with open(fpath, "w", encoding="utf-8") as f:
            for cid, lens in failures:
                f.write(json.dumps({"case_id": cid, "lens": lens}) + "\n")
        log("failure list -> %s" % fpath)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
