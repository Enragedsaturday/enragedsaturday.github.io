#!/usr/bin/env python3
"""
LINT-30 — the R4 ledger reconciliation invariants (S9's own audit-the-audit row).

Checks the five reconciliation invariants of the signed S9 ledger schema
(_overhaul2/s9-demo/LEDGER-SCHEMA.md; spec S9 R4) by SCRIPT, not agent,
fail-closed. Joined to the assertion inventory by `assertion_id`.

The ledger set lives under `_run/s9/` as JSON-lines (findings.jsonl, votes.jsonl,
adjudications.jsonl, fixes.jsonl) at EXECUTE. This script also reads the demo
per-object layout (_overhaul2/s9-demo/*.{finding,vote.*,adjudication,fix}.json)
so the worked F-DEMO-001 instance is its acceptance test.

Modes:
  * BOOTSTRAP — an empty-but-initialized ledger set (0 rows) returns NO-ROWS-YET
    and exits green. This is the P0 baseline state (the inventory may already
    exist; that does not create ledger rows).
  * FAIL-CLOSED — once ANY ledger row exists, the invariants run and any breach
    is a HIGH violation (nonzero exit).
  * COMPLETENESS (`--completeness`) — additionally enforces invariant 5's
    "zero verdict-less inventory items" (the R14.5 end-of-run gate); off in the
    normal roster/bootstrap run because verdicts only accrete during the pass.

The five invariants (spec R4 / LEDGER-SCHEMA):
  1. Every finding has exactly one adjudication; every UPHELD/MODIFIED
     adjudication has a fix whose FINAL loop verdict is FIXED, or an escalation.
  2. Every paneled finding's tally has all three lane votes; >=2 refuted ⟹ the
     verdict is DISMISSED / MODIFIED / ESCALATE (never plain UPHELD-as-framed).
  3. Lane-identity: found_by.lane != adjudicator.lane; fix author ∉ its re-review
     lanes; no lane closes its own row.
  4. Every DISMISSED carries a reason (the false-positive log).
  5. Counts reconcile: findings == adjudications; UPHELD+MODIFIED == fixes +
     escalations; every referenced assertion_id exists in the inventory;
     (completeness) zero inventory items without a verdict.

Usage:
  python3 check_ledger.py [--dir DIR] [--demo] [--completeness] [--quiet]
  python3 check_ledger.py --self-test
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
# reuse the lint violation format so run_all.py consumes LINT-30 like any lint
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "lint"))
import _common as c  # noqa: E402

LINT = "LINT-30"
LEDGER_DIR = os.path.join(REPO_ROOT, "_run", "s9")
DEMO_DIR = os.path.join(REPO_ROOT, "_overhaul2", "s9-demo")
FIXTURE_DIR = os.path.join(HERE, "fixtures", "ledger")

NEED_FIX = ("UPHELD", "MODIFIED")
_FINDING_ID_RE = re.compile(r"\bF[-A-Za-z0-9]*\d[-A-Za-z0-9]*\b")


# --------------------------------------------------------------------------
# loader — JSONL layout OR demo per-object layout
# --------------------------------------------------------------------------

def _read_jsonl(path):
    rows, errs = [], []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError as e:
                errs.append("%s:%d %s" % (path, n, e))
    return rows, errs


def load_ledger(dirpath):
    data = {"findings": [], "votes": [], "adjudications": [], "fixes": [],
            "inventory": None, "escalations": set(), "malformed": [],
            "dir": dirpath, "dir_exists": os.path.isdir(dirpath)}
    jsonl = {"findings": "findings.jsonl", "votes": "votes.jsonl",
             "adjudications": "adjudications.jsonl", "fixes": "fixes.jsonl"}
    used_jsonl = False
    for key, fname in jsonl.items():
        p = os.path.join(dirpath, fname)
        if os.path.exists(p):
            used_jsonl = True
            rows, errs = _read_jsonl(p)
            data[key] = rows
            data["malformed"].extend(errs)
    if not used_jsonl:
        # demo per-object layout: dispatch on the `schema` tag
        bucket = {"s9.finding": "findings", "s9.vote": "votes",
                  "s9.adjudication": "adjudications", "s9.fix": "fixes"}
        for f in sorted(glob.glob(os.path.join(dirpath, "*.json"))):
            if os.path.basename(f).startswith("assertion-inventory"):
                continue
            try:
                with open(f, encoding="utf-8") as fh:
                    obj = json.load(fh)
            except ValueError as e:
                data["malformed"].append("%s %s" % (f, e))
                continue
            schema = (obj.get("schema") or "")
            for pref, key in bucket.items():
                if schema.startswith(pref):
                    data[key].append(obj)
                    break
    # inventory (for the assertion_id join)
    inv = os.path.join(dirpath, "assertion-inventory.json")
    if os.path.exists(inv):
        try:
            with open(inv, encoding="utf-8") as fh:
                d = json.load(fh)
            data["inventory"] = d.get("items") if isinstance(d, dict) else d
        except ValueError as e:
            data["malformed"].append("%s %s" % (inv, e))
    # escalations: finding ids named in _review-needed/*.md (ledger-local + repo)
    for base in (os.path.join(dirpath, "_review-needed"),
                 os.path.join(REPO_ROOT, "_review-needed")):
        for f in glob.glob(os.path.join(base, "*.md")):
            try:
                txt = open(f, encoding="utf-8").read()
            except OSError:
                continue
            for fid in _FINDING_ID_RE.findall(txt):
                data["escalations"].add(fid)
    return data


def _final_loop_verdict(fix):
    # Two sanctioned row shapes: the demo per-object shape closes each loop via
    # loops[-1].re_review.verdict; production lanes write FLAT rows whose
    # operative closure is the top-level status field ("FIXED"/"NOT-FIXED").
    # Highest-numbered flat row per finding wins (callers pass single rows;
    # inv-1/5 aggregate with any()).
    loops = fix.get("loops") or []
    if loops:
        return ((loops[-1].get("re_review") or {}).get("verdict"))
    status = fix.get("status")
    if status in ("FIXED", "NOT-FIXED"):
        return status
    return None


# --------------------------------------------------------------------------
# the five invariants
# --------------------------------------------------------------------------

def check_ledger(dirpath, completeness=False):
    """Return (violations, status). status ∈ {NO-ROWS-YET, CHECKED}."""
    data = load_ledger(dirpath)
    v = []

    def add(msg, sev=c.HIGH, ref=None):
        v.append(c.make_violation(LINT, ref or dirpath, 1, sev, msg))

    for m in data["malformed"]:
        add("unparseable ledger row/file (fail-closed): %s" % m)

    findings = data["findings"]
    votes = data["votes"]
    adjs = data["adjudications"]
    fixes = data["fixes"]
    total = len(findings) + len(votes) + len(adjs) + len(fixes)

    if total == 0:
        if data["malformed"]:
            return v, "CHECKED"
        return v, "NO-ROWS-YET"

    finding_ids = {f.get("id") for f in findings}
    adj_by_fid, votes_by_fid, fix_by_fid = {}, {}, {}
    for a in adjs:
        adj_by_fid.setdefault(a.get("finding_id"), []).append(a)
    for vt in votes:
        votes_by_fid.setdefault(vt.get("finding_id"), []).append(vt)
    for fx in fixes:
        fix_by_fid.setdefault(fx.get("finding_id"), []).append(fx)

    # ---- invariant 1: finding -> 1 adjudication; UPHELD/MODIFIED -> FIXED|escalation
    for f in findings:
        fid = f.get("id")
        my = adj_by_fid.get(fid, [])
        if len(my) == 0:
            add("[inv1] finding %s has no adjudication" % fid)
        elif len(my) > 1:
            add("[inv1] finding %s has %d adjudications (want exactly 1)"
                % (fid, len(my)))
        for a in my:
            verdict = a.get("verdict")
            if verdict in NEED_FIX:
                fixed = any(_final_loop_verdict(fx) == "FIXED"
                            for fx in fix_by_fid.get(fid, []))
                if not (fixed or fid in data["escalations"]):
                    add("[inv1] %s adjudication %s has no fix whose final loop is "
                        "FIXED and no _review-needed escalation" % (verdict, fid))
            elif verdict == "ESCALATE":
                if fid not in data["escalations"]:
                    add("[inv1] ESCALATE adjudication %s has no _review-needed "
                        "escalation file" % fid)
    for a in adjs:
        if a.get("finding_id") not in finding_ids:
            add("[inv1] adjudication references finding_id %s with no finding row"
                % a.get("finding_id"))

    # ---- invariant 2: paneled -> 3 lane votes; >=2 refute -> not plain UPHELD
    for fid, vs in votes_by_fid.items():
        lanes = [x.get("lane") for x in vs]
        if len(lanes) != len(set(lanes)):
            add("[inv2] paneled finding %s has duplicate lane votes %s"
                % (fid, lanes))
        if len(set(lanes)) < 3:
            add("[inv2] paneled finding %s has %d distinct lane votes (want 3)"
                % (fid, len(set(lanes))))
        for x in vs:
            if x.get("recorded_before_other_votes_read") is False:
                add("[inv2] vote by %s on %s recorded AFTER seeing sibling votes "
                    "(blindness contaminated)" % (x.get("lane"), fid))
        refuted = sum(1 for x in vs if x.get("verdict") == "refuted")
        for a in adj_by_fid.get(fid, []):
            if refuted >= 2 and a.get("verdict") == "UPHELD":
                add("[inv2] finding %s has %d refute votes but was adjudicated "
                    "UPHELD-as-framed (must be DISMISSED/MODIFIED/ESCALATE)"
                    % (fid, refuted))

    # ---- invariant 3: lane identity (no lane closes its own row)
    # Spec R4 inv-3 scopes finder!=adjudicator to LEGAL findings; editorial/
    # structural/tooling dimensions (D-TOOL) run one-reviewer per user D3.
    # A legal-dimension self-adjudication additionally clears when an
    # independent confirmation vote (different lane) is recorded (R14.2).
    for f in findings:
        fid = f.get("id")
        if (f.get("dimension") or "").upper() == "D-TOOL":
            continue
        finder = (f.get("found_by") or {}).get("lane")
        confirm_lanes = {v.get("lane") for v in votes_by_fid.get(fid, [])
                         if v.get("verdict") in ("stands", "stands-modified")}
        for a in adj_by_fid.get(fid, []):
            adjud = (a.get("adjudicator") or {}).get("lane")
            if finder and adjud and finder == adjud:
                if confirm_lanes - {finder}:
                    continue  # independent confirmation on record
                add("[inv3] finding %s: finder lane == adjudicator lane (%s), "
                    "no independent confirmation vote"
                    % (fid, finder))
    for fx in fixes:
        fid = fx.get("finding_id")
        fixer = (fx.get("applied_by") or {}).get("lane")
        rev = [(l.get("re_review") or {}).get("lane") for l in (fx.get("loops") or [])]
        if fixer and fixer in rev:
            add("[inv3] fix for %s: author lane (%s) also re-reviewed its own fix"
                % (fid, fixer))

    # ---- invariant 4: every DISMISSED carries a reason
    for a in adjs:
        if a.get("verdict") == "DISMISSED":
            reason = a.get("adjudicated_holding") or a.get("dismiss_reason")
            if not reason:
                add("[inv4] DISMISSED adjudication %s carries no reason (false-"
                    "positive log required)" % a.get("finding_id"))

    # ---- invariant 5: counts + assertion_id join (+ completeness)
    if len(findings) != len(adjs):
        add("[inv5] count mismatch: %d findings != %d adjudications"
            % (len(findings), len(adjs)))
    need_fix_n = sum(1 for a in adjs if a.get("verdict") in NEED_FIX)
    escal_fix = sum(1 for a in adjs if a.get("verdict") in NEED_FIX
                    and a.get("finding_id") in data["escalations"])
    fixed_n = sum(1 for fx in fixes
                  if _final_loop_verdict(fx) == "FIXED")
    if need_fix_n != fixed_n + escal_fix:
        add("[inv5] reconciliation: %d UPHELD/MODIFIED != %d FIXED fixes + %d "
            "escalations" % (need_fix_n, fixed_n, escal_fix))
    inv = data["inventory"]
    if inv is not None:
        inv_ids = {it.get("assertion_id") for it in inv}
        for f in findings:
            aid = f.get("assertion_id")
            if aid and aid not in inv_ids:
                add("[inv5] finding %s references assertion_id %s absent from the "
                    "inventory" % (f.get("id"), aid))
        if completeness:
            verdicted = set()
            for f in findings:
                if adj_by_fid.get(f.get("id")):
                    verdicted.add(f.get("assertion_id"))
            missing = [it.get("assertion_id") for it in inv
                       if it.get("assertion_id") not in verdicted]
            if missing:
                add("[inv5/completeness] %d inventory items without a verdict "
                    "(R14.5): e.g. %s" % (len(missing), missing[:3]))
    return v, "CHECKED"


def run(paths=None, dirpath=None, completeness=False):
    """run_all-compatible entry: violations only (NO-ROWS-YET -> [])."""
    viols, _status = check_ledger(dirpath or LEDGER_DIR, completeness=completeness)
    return viols


# --------------------------------------------------------------------------
# self-test — fixtures + the F-DEMO-001 demo acceptance test
# --------------------------------------------------------------------------

def self_test():
    errs = []

    def expect(dirpath, want_status, want_high, label, completeness=False):
        if not os.path.isdir(dirpath):
            errs.append("%s: fixture dir missing (%s)" % (label, dirpath))
            return
        viols, status = check_ledger(dirpath, completeness=completeness)
        nh = sum(1 for x in viols if x["severity"] == c.HIGH)
        if want_status and status != want_status:
            errs.append("%s: status %s (want %s)" % (label, status, want_status))
        if want_high == 0 and nh != 0:
            errs.append("%s: %d HIGH (want 0): %s"
                        % (label, nh, [x["message"][:50] for x in viols][:4]))
        if want_high == "some" and nh == 0:
            errs.append("%s: 0 HIGH (want >=1 breach)" % label)

    # bootstrap fixture -> NO-ROWS-YET green
    expect(os.path.join(FIXTURE_DIR, "bootstrap"), "NO-ROWS-YET", 0, "bootstrap")
    # pass fixture -> all invariants hold
    expect(os.path.join(FIXTURE_DIR, "pass"), "CHECKED", 0, "pass")
    # fail fixture -> at least one invariant breach
    expect(os.path.join(FIXTURE_DIR, "fail"), "CHECKED", "some", "fail")
    # THE acceptance test: the worked F-DEMO-001 demo validates clean
    if os.path.isdir(DEMO_DIR):
        viols, status = check_ledger(DEMO_DIR)
        nh = sum(1 for x in viols if x["severity"] == c.HIGH)
        if nh != 0:
            errs.append("F-DEMO-001 acceptance: %d HIGH (want 0): %s"
                        % (nh, [x["message"][:60] for x in viols][:6]))
    else:
        errs.append("F-DEMO-001 acceptance: demo dir missing (%s)" % DEMO_DIR)

    if errs:
        for e in errs:
            sys.stderr.write("[self-test] LINT-30: %s\n" % e)
        return 1
    return 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        sys.exit(self_test())
    quiet = "--quiet" in args
    completeness = "--completeness" in args
    dirpath = DEMO_DIR if "--demo" in args else LEDGER_DIR
    if "--dir" in args:
        dirpath = args[args.index("--dir") + 1]
    viols, status = check_ledger(dirpath, completeness=completeness)
    if not quiet:
        c.emit(viols)
    nh = sum(1 for x in viols if x["severity"] == c.HIGH)
    sys.stderr.write("LINT-30 ledger reconciliation: dir=%s status=%s HIGH=%d\n"
                     % (os.path.relpath(dirpath, REPO_ROOT), status, nh))
    if status == "NO-ROWS-YET":
        sys.stderr.write("  NO-ROWS-YET (bootstrap): ledger initialized, 0 rows — "
                         "green; fail-closes once rows exist.\n")
    sys.exit(1 if nh else 0)


if __name__ == "__main__":
    main()
