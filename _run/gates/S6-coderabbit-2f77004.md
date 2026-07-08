# CodeRabbit gate — S6 @ 2f77004 (base: da8adb3)

- run: 2026-07-08T01:04:35Z
- cli: 0.6.4
- mode: --plain --type committed --base-commit da8adb3 --dir /var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T//cr-gate-S6-5kcM49/scripts
- scope: .coderabbit.yaml path filters (code only) · restricted to scripts

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 3s elapsed
Preparing review... 5s elapsed
[2m────────────────────────────────────────[22m
[38;2;215;93;44mCodeRabbit Review[39m

[2mDiff      : [22mcommitted changes only
[2mCompare   : [22mHEAD [2m→[22m origin/HEAD~1
[2mDirectory : [22mcr-gate-S6-5kcM49/scripts
[2m────────────────────────────────────────[22m

[38;2;215;93;44m(\(\[39m
[38;2;215;93;44m(• .•)[39m  Expecto bugtronum!

Preparing sandbox... 6s elapsed
Summarizing changes... 15s elapsed
Summarizing changes... 1m 03s elapsed - still working
Summarizing changes... 2m 03s elapsed - still working
Finishing analysis tools... 2m 49s elapsed - still working
Writing review comments... 2m 49s elapsed - still working
Writing review comments... 3m 03s elapsed - still working

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/gates/coderabbit_gate.sh:34[36m[4mscripts/gates/coderabbit_gate.sh[24m[39m[2m:[22m[36m34-39[39m]8;;

  Guard doesn't catch multi-zero values like "00", "000".

  The pattern [36m0[39m only matches the literal string [36m"0"[39m. A value like
  [36mCR_GATE_TIMEOUT="00"[39m is all-digits (survives [36m[!0-9][39m) and isn't the
  literal string [36m0[39m, so it passes this guard — yet Perl's [36malarm[39m will
  coerce [36m"00"[39m to numeric [36m0[39m and cancel the timer, defeating exactly the
  guarantee this check is meant to enforce.


  🛡️ Proposed fix using arithmetic evaluation

  [2m case "$CR_GATE_TIMEOUT" in[22m
  [31m-  ''|*[!0-9]*|0) echo "coderabbit_gate: CR_GATE_TIMEOUT must be a positive integer (got '${CR_GATE_TIMEOUT}')" >&2; exit 2 ;;[39m
  [32m+  ''|*[!0-9]*) echo "coderabbit_gate: CR_GATE_TIMEOUT must be a positive integer (got '${CR_GATE_TIMEOUT}')" >&2; exit 2 ;;[39m
  [2m esac[22m
  [32m+if [ "$((10#$CR_GATE_TIMEOUT))" -le 0 ]; then[39m
  [32m+  echo "coderabbit_gate: CR_GATE_TIMEOUT must be a positive integer (got '${CR_GATE_TIMEOUT}')" >&2[39m
  [32m+  exit 2[39m
  [32m+fi[39m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" — here a zero-equivalent
  timeout could silently disable the hang-prevention alarm.

Writing review comments... 4m 30s elapsed - still working - 1 finding so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/lint/lint21_binding.py:302[36m[4mscripts/lint/lint21_binding.py[24m[39m[2m:[22m[36m302-310[39m]8;;

  New fail-closed test cases are only run if fixtures happen to exist.

  Unlike the required fixtures checked at lines 260-263 (which abort
  self_test with FAIL if missing), the new badstruct/non-string-node cases
  are gated behind [36mif os.path.isfile(...)[39m. If either fixture is later
  deleted or renamed, self_test silently stops exercising these two
  fail-closed paths and still reports PASS — exactly the kind of
  silent-success-on-missing-input this lint is designed to prevent for the
  binding map itself.


  ♻️ Make new fixtures mandatory like the others

  [31m-    for req in (reg, b_pass, b_dangle, b_emptynodes):[39m
  [32m+    b_badstruct = os.path.join(fixdir, "lint-21-binding-badstruct-fail.yaml")[39m
  [32m+    b_nonstr = os.path.join(fixdir, "lint-21-binding-nonstring-node-fail.yaml")[39m
  [32m+    for req in (reg, b_pass, b_dangle, b_emptynodes, b_badstruct, b_nonstr):[39m
  [2m         if not os.path.isfile(req):[22m
  [2m             sys.stderr.write("[self-test] FAIL: missing fixture %s\n" % req)[22m
  [2m             return 1[22m
  [36m@@[39m
  [31m-    b_badstruct = os.path.join(fixdir, "lint-21-binding-badstruct-fail.yaml")[39m
  [31m-    if os.path.isfile(b_badstruct):[39m
  [31m-        case("malformed bound/pending struct", b_badstruct, lake_bound, "high")[39m
  [31m-    b_nonstr = os.path.join(fixdir, "lint-21-binding-nonstring-node-fail.yaml")[39m
  [31m-    if os.path.isfile(b_nonstr):[39m
  [31m-        case("non-string node id", b_nonstr, lake_bound, "high")[39m
  [32m+    case("malformed bound/pending struct", b_badstruct, lake_bound, "high")[39m
  [32m+    case("non-string node id", b_nonstr, lake_bound, "high")[39m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" — an optional fixture check
  that quietly no-ops is the self-test analogue of that failure mode.


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:10587[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m10587-10594[39m]8;;

  Use a fresh empty record for leg-validation refusal tests.

  These cases run after [36mempty-coa--111[39m already received a citation, so
  they pass because of the “already-bearing” guard before
  [36mvalidate_web_legs(...)[39m. Duplicate-source/Wikipedia/disagreement
  validation is not actually tested.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:6381[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m6381-6416[39m]8;;

  Fail closed when the docket-fetch gate is passed without the repair
  action.

  [36m--repair-coa-state-allow-docket-fetch[39m is silently ignored unless
  [36m--repair-coa-state-from-cache[39m is present, so a mistaken invocation can
  fall through to the normal ingest path and consume calls.


  Proposed fix

  [2m     if args.records and not args.rerun_lane:[22m
  [2m         raise SystemExit("--records is only valid with --rerun-lane")[22m
  [32m+    if args.repair_coa_state_allow_docket_fetch and not args.repair_coa_state_from_cache:[39m
  [32m+        raise SystemExit("--repair-coa-state-allow-docket-fetch requires --repair-coa-state-from-cache")[39m
  [2m     if args.apply_web_cites:[22m

  As per path instructions, [36mscripts/[39m must prioritize “API-quota safety”
  and fail-closed gate behavior.






  Also applies to: 10965-10965


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:4924[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m4924[39m]8;;

  Fix the Ruff-blocking style findings.

  Rename ambiguous [36ml[39m, remove redundant single-item exception tuples, and
  split the semicolon statement so the lint gate can pass.






  Also applies to: 5102-5102, 5121-5121, 10571-10571, 10857-10857


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:975[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m975-1003[39m]8;;

  Refuse state derivations when no state can be derived.

  Both docket-authoritative and cache-only paths can return
  [36mdecision="write"[39m for [36mcourt_level="state"[39m with [36mstate=None[39m. That
  records an incomplete verified court identity instead of escalating.


  Proposed fix

  [2m         if level == "state" and state is None:[22m
  [2m             hint = roster_state or rep_state[22m
  [2m             if hint:[22m
  [2m                 state = hint[22m
  [2m                 notes.append("state filled from %s hint" % ("roster" if roster_state else "reporter"))[22m
  [32m+            else:[39m
  [32m+                return refuse("state-no-state docket-court=%s (no roster/reporter state hint)" % docket_court_id)[39m
  [2m         return write(level, circuit, state, label, auth["basis"], "docket-authoritative", notes)[22m
  [36m@@[39m
  [2m     if level == "state":[22m
  [2m         if roster_state and rep_state and roster_state != rep_state:[22m
  [2m             return refuse("roster-reporter-state-conflict roster=%s reporter=%s" % (roster_state, rep_state))[22m
  [31m-        return write("state", None, roster_state or rep_state, label, "roster+reporter(cache)",[39m
  [32m+        state = roster_state or rep_state[39m
  [32m+        if not state:[39m
  [32m+            return refuse("state-no-state-cache (regional/state reporter without state hint; fetch docket to resolve)")[39m
  [32m+        return write("state", None, state, label, "roster+reporter(cache)",[39m
  [2m                      "cache-only (no docket confirmation)")[22m

  As per path instructions, [36mscripts/[39m must prioritize “fail-closed
  behavior” and “Flag any path where an exception or empty result could be
  recorded as a verified state.”


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:4875[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m4875-4903[39m]8;;

  Require evidence before journaling slip-only as terminal.

  [36mslip_only: true[39m bypasses leg/evidence validation and journals a terminal
  [36mslip-only[39m outcome even when [36mlegs[39m/[36mevidence[39m is empty. That lets an
  empty result become a verified terminal state.


  Proposed fix

  [2m         if entry.get("slip_only"):[22m
  [32m+            evidence = entry.get("legs") or entry.get("evidence")[39m
  [32m+            if not evidence:[39m
  [32m+                raise SystemExit("--apply-web-cites row %s slip_only:true requires legs/evidence" % record_id)[39m
  [2m             plans.append(("slip", record_id, row, record, entry, None, None))[22m
  [2m             continue[22m

  As per path instructions, [36mscripts/[39m must prioritize “fail-closed
  behavior” and “Flag any path where an exception or empty result could be
  recorded as a verified state.”


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:5108[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m5108-5130[39m]8;;

  Do not write cache-only repairs after authoritative fetch failures.

  When [36mallow_docket_fetch[39m is enabled, a [36mFetchFailed[39m for docket/court
  currently falls through to [36mderive_coa_state_court(...)[39m; that can still
  write a repaired identity from weaker cache-only signals after an
  authoritative fetch error.


  Proposed fix

  [2m                 except FetchFailed as exc:[22m
  [31m-                    docket_fetch_note = "docket-fetch-failed:%s" % (getattr(exc, "status", None) or getattr(exc, "reason", None))[39m
  [31m-                    docket = None[39m
  [32m+                    _journal_coa_state_repair([39m
  [32m+                        journal, record_id=record_id, status="queued-for-lane",[39m
  [32m+                        reason="docket-fetch-failed:%s" % (getattr(exc, "status", None) or getattr(exc, "reason", None)),[39m
  [32m+                        cluster_id=cluster_id,[39m
  [32m+                    )[39m
  [32m+                    queued.append(record_id)[39m
  [32m+                    continue[39m
  [36m@@[39m
  [2m                 except FetchFailed as exc:[22m
  [31m-                    court_obj = None  # classify falls back to structural / state-slug; may escalate[39m
  [32m+                    _journal_coa_state_repair([39m
  [32m+                        journal, record_id=record_id, status="queued-for-lane",[39m
  [32m+                        reason="court-fetch-failed:%s" % (getattr(exc, "status", None) or getattr(exc, "reason", None)),[39m
  [32m+                        cluster_id=cluster_id,[39m
  [32m+                    )[39m
  [32m+                    queued.append(record_id)[39m
  [32m+                    continue[39m

  As per path instructions, [36mscripts/[39m must prioritize “fail-closed
  behavior” and “API-quota safety,” and must flag exception paths recorded
  as verified state.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:4945[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m4945-4963[39m]8;;

  Pre-validate the identity-repair batch before writing any row.

  Unlike [36mrepair_coa_state_from_cache[39m, this loop validates and writes per
  row. If a later record is out-of-scope or missing, earlier rows may
  already be repaired, so the batch does not fail closed.


  Proposed direction

  [2m     allow_statuses = tuple(allow_statuses)[22m
  [32m+    targets = [][39m
  [32m+    for raw_id in unique_preserve_order(record_ids):[39m
  [32m+        record_id = manifest.resolve_record_id(raw_id) or raw_id[39m
  [32m+        row = manifest.by_record_id.get(record_id)[39m
  [32m+        if not row:[39m
  [32m+            raise SystemExit("--repair-identity-from-cache record not found in manifest: %s" % raw_id)[39m
  [32m+        if row.get("status") not in allow_statuses:[39m
  [32m+            raise SystemExit("--repair-identity-from-cache refuses row %s (status=%s)" % (record_id, row.get("status")))[39m
  [32m+        record = load_case_record(paths, record_id)[39m
  [32m+        if record is None:[39m
  [32m+            raise SystemExit("--repair-identity-from-cache lake record missing on disk: %s" % record_id)[39m
  [32m+        cluster_id = (record.get("identity") or {}).get("cluster_id")[39m
  [32m+        if not cluster_id:[39m
  [32m+            raise SystemExit("--repair-identity-from-cache row %s has no identity.cluster_id" % record_id)[39m
  [32m+        targets.append((record_id, row, record, cluster_id))[39m
  [32m+[39m
  [2m     repaired = [][22m
  [2m     queued = [][22m
  [31m-    for raw_id in unique_preserve_order(record_ids):[39m
  [31m-        record_id = manifest.resolve_record_id(raw_id) or raw_id[39m
  [31m-        row = manifest.by_record_id.get(record_id)[39m
  [31m-        ...[39m
  [32m+    for record_id, row, record, cluster_id in targets:[39m

  As per path instructions, [36mscripts/[39m must prioritize “fail-closed
  behavior” and “resumability/idempotence (journal + cache driven).”


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s2/ingest.py:5155[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m5155-5183[39m]8;;

  Normalize repaired identity fields before writing.

  The writeback can duplicate years for cache-only labels like `9th Cir.
  2021[36m → [39m9th Cir. 2021 2021`, and it does not clear stale mutually
  exclusive fields such as [36mcircuit[39m on state repairs or [36mstate[39m on COA
  repairs.


  Proposed fix

  [2m         before = {f: identity.get(f) for f in fields}[22m
  [2m         identity["court_level"] = level[22m
  [36m@@[39m
  [31m-        if circuit:[39m
  [31m-            identity["circuit"] = circuit[39m
  [31m-        if level == "state" and state:[39m
  [31m-            identity["state"] = state[39m
  [32m+        identity["circuit"] = circuit if level == "coa" else None[39m
  [32m+        identity["state"] = state if level == "state" else None[39m
  [2m         if label:[22m
  [31m-            identity["court"] = ("%s %s" % (label, year)) if year else label[39m
  [32m+            label_has_year = bool(year and re.search(r"\b%s\b" % re.escape(str(year)), str(label)))[39m
  [32m+            identity["court"] = ("%s %s" % (label, year)) if year and not label_has_year else label[39m
  [36m@@[39m
  [31m-        if circuit:[39m
  [31m-            row["circuit"] = circuit[39m
  [32m+        row["circuit"] = identity.get("circuit")[39m
  [32m+        row["state"] = identity.get("state")[39m

Writing review comments... 6m 28s elapsed - still working - 10 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/lint/lint17_coverage.py:196[36m[4mscripts/lint/lint17_coverage.py[24m[39m[2m:[22m[36m196-246[39m]8;;

  [36mload_allowlist()[39m's fail-closed paths are untested.

  [36mself_test()[39m exercises [36mclassify()[39m against synthetic in-memory
  tokenlists/allow-sets and scans the fixtures, but never invokes
  [36mload_allowlist()[39m itself — so the missing-ledger, malformed-JSON, and
  (per the fix above) unknown-terminal fail-closed branches have no test
  coverage at all. For a script whose stated purpose is "FAIL-CLOSED" gating
  on a legal-authority pipeline, the actual ledger-parsing gate is the
  highest-value thing to self-test.

  Consider adding cases that write a temp ledger file (missing, malformed
  JSON, non-dict row, unknown [36mterminal[39m) and assert [36mload_allowlist()[39m
  returns an error rather than silently succeeding.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/lint/lint17_coverage.py:136[36m[4mscripts/lint/lint17_coverage.py[24m[39m[2m:[22m[36m136-163[39m]8;;

  Ledger allowlist loading is not fail-closed against malformed/unexpected
  data.

  Two gaps in the fail-closed contract this lint is supposed to enforce:

  1. [36mterminal[39m values are never validated against the known non-authored
  set documented in the module docstring (`brief-mention | excluded-remit |
  unverifiable | removed | folded-alias | watch[36m). Any row where [39mterminal
  != "authored"` — including a typo'd or unrecognized value — is silently
  added to the allowlist via [36m_add_allow[39m, letting an un-vetted ledger entry
  pass a caption as covered.
  2. Neither [36mled[39m nor individual [36mrow[39m entries are checked to be dicts. If
  the ledger JSON parses successfully but isn't shaped as expected (e.g.,
  [36mrows[39m contains a string/list, or the top-level document isn't an object),
  [36mled.get(...)[39m/[36mrow.get(...)[39m raises an uncaught [36mAttributeError[39m that
  crashes [36mrun()[39m (and the whole [36mrun_all.py[39m invocation, since callers
  don't wrap [36mrun_fn(paths)[39m in a try/except) instead of surfacing a clean
  HIGH violation.

  Also, [36mopen(path, encoding="utf-8")[39m isn't wrapped in a context manager —
  the handle is never explicitly closed.


  🔧 Proposed fix

  [32m+_NONAUTHORED_TERMINALS = {[39m
  [32m+    "brief-mention", "excluded-remit", "unverifiable",[39m
  [32m+    "removed", "folded-alias", "watch",[39m
  [32m+}[39m
  [32m+[39m
  [32m+[39m
  [2m def load_allowlist(ledger_path=None):[22m
  [2m     """Normalized caption/alias set of every NON-authored ledger row + every[22m
  [2m     frozen corpus_mention_baseline row. Returns (allowlist:set, error:str|None)."""[22m
  [2m     path = ledger_path or os.path.join(c.REPO_ROOT, LEDGER_REL)[22m
  [2m     if not os.path.isfile(path):[22m
  [2m         return set(), ("coverage ledger missing: %s not found — LINT-17 cannot "[22m
  [2m                        "allowlist non-page terminals [S6 R11/R12]" % LEDGER_REL)[22m
  [2m     try:[22m
  [31m-        led = json.load(open(path, encoding="utf-8"))[39m
  [32m+        with open(path, encoding="utf-8") as f:[39m
  [32m+            led = json.load(f)[39m
  [2m     except (OSError, json.JSONDecodeError) as exc:[22m
  [2m         return set(), "coverage ledger unreadable (%s): %s" % (LEDGER_REL, exc)[22m
  [32m+    if not isinstance(led, dict):[39m
  [32m+        return set(), "coverage ledger malformed (%s): expected a JSON object" % LEDGER_REL[39m
  [2m     allow = set()[22m
  [2m     for row in led.get("rows", []):[22m
  [31m-        if row.get("terminal") == "authored":[39m
  [32m+        if not isinstance(row, dict):[39m
  [32m+            return set(), "coverage ledger malformed (%s): non-dict row" % LEDGER_REL[39m
  [32m+        term = row.get("terminal")[39m
  [32m+        if term == "authored":[39m
  [2m             continue[22m
  [32m+        if term not in _NONAUTHORED_TERMINALS:[39m
  [32m+            return set(), ("coverage ledger row has unknown terminal state %r "[39m
  [32m+                           "[S6 R11]" % term)[39m
  [2m         _add_allow(allow, row)[22m
  [2m     for row in led.get("corpus_mention_baseline", []):[22m
  [32m+        if not isinstance(row, dict):[39m
  [32m+            return set(), "coverage ledger malformed (%s): non-dict baseline row" % LEDGER_REL[39m
  [2m         _add_allow(allow, row)[22m
  [2m     return allow, None[22m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" for [36mscripts/[39m.

Writing review comments... 8m 34s elapsed - still working - 12 findings so far
Writing review comments... 9m 34s elapsed - still working - 12 findings so far
Writing review comments... 10m 34s elapsed - still working - 12 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s6/stamp_slip_only.py:70[36m[4mscripts/s6/stamp_slip_only.py[24m[39m[2m:[22m[36m70-84[39m]8;;

  Malformed allowlist lines are silently dropped — no warning, no count.

  [36mexcept json.JSONDecodeError: continue[39m silently discards bad lines from
  the "enumerated, never a wildcard" allowlist (per the docstring). A
  corrupted or truncated line for one of the 15 real cases would simply
  vanish from [36mout[39m, and the affected [36mrecord_id[39m would later be refused
  with [36mREFUSE_NOT_IN_ALLOWLIST[39m — indistinguishable from "not intended to
  be stamped." The operator gets no signal that the source-of-truth file
  itself is malformed.


  🛡️ Proposed fix: surface parse failures instead of swallowing them

  [31m-            try:[39m
  [31m-                row = json.loads(line)[39m
  [31m-            except json.JSONDecodeError:[39m
  [31m-                continue[39m
  [32m+            try:[39m
  [32m+                row = json.loads(line)[39m
  [32m+            except json.JSONDecodeError as exc:[39m
  [32m+                sys.stderr.write("WARN: malformed allowlist line skipped: %s\n" % exc)[39m
  [32m+                continue[39m

  As per path instructions: "Flag any path where an exception or empty
  result could be recorded as a verified state."

Writing review comments... 11m 37s elapsed - still working - 13 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s6/mint_page.py:693[36m[4mscripts/s6/mint_page.py[24m[39m[2m:[22m[36m693-730[39m]8;;

  Fail-open exception handling defeats the collision guard's purpose.

  [36mexcept Exception: continue[39m silently skips any lake record whose JSON
  can't be read. If the file that actually collides on [36mcluster_id[39m is the
  one that's unreadable (corrupt/partial write/encoding issue), the scan
  reports "no collider" and the mint proceeds — exactly the double-paging
  failure mode (F-R8-13/Davis) this function exists to prevent. Every other
  [36mread_json[39m call in this file (e.g. line 853) is left unguarded and
  propagates fail-closed; this is the outlier. Ruff also flags the blind
  except (BLE001) and missing logging (S112).

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" — an
  unreadable-but-colliding record turning into a [36mNone, None[39m "no collision"
  result is exactly that.


  🔒 Proposed fail-closed fix

  [2m     for p in sorted(glob.glob(os.path.join(lake_cases_dir(lake_root), "*.json"))):[22m
  [2m         try:[22m
  [2m             rec = read_json(p)[22m
  [31m-        except Exception:[39m
  [31m-            continue[39m
  [32m+        except Exception as exc:[39m
  [32m+            # Fail-closed: an unreadable record could be the very one that[39m
  [32m+            # collides on cluster_id — silently skipping it risks a missed[39m
  [32m+            # double-page, which is the exact failure this guard prevents.[39m
  [32m+            raise RuntimeError([39m
  [32m+                "cluster-collision scan cannot verify %r is unique — unreadable "[39m
  [32m+                "lake record %s: %s" % (record_id, lint_common.relpath(p), exc)[39m
  [32m+            ) from exc[39m
  [2m         rid = rec.get("record_id")[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S6-5kcM49/scripts/s6/mint_page.py:1616[36m[4mscripts/s6/mint_page.py[24m[39m[2m:[22m[36m1616-1622[39m]8;;

  Frontmatter-injection assertion is tautological given the fixture body.

  [36mpayload-slip.md[39m already hard-codes [36m"No. 23-1197, slip op. (U.S. 2026)"[39m
  in its body (lines 12 and 36). Checking the whole rendered page [36mtext[39m for
  that substring passes even if the
  citation-derivation/frontmatter-injection path is completely broken — the
  assertion can't distinguish "derived and injected" from "already present
  in the payload body." This weakens the regression guard for the slip-cite
  feature this test is meant to cover.


  ✅ Proposed fix: assert on the derived projection directly

  [31m-        check("slip cite injected into frontmatter",[39m
  [31m-              "No. 23-1197, slip op. (U.S. 2026)" in (p.get("page", {}) or {}).get("text", ""))[39m
  [32m+        check("slip cite injected into frontmatter",[39m
  [32m+              p.get("projection", {}).get("citation") == "No. 23-1197, slip op. (U.S. 2026)")[39m


[2m────────────────────────────────────────[22m
[38;2;215;93;44mReview complete[39m
[2m15 findings ✔[22m

[2mMajor    12[22m
[2mMinor    3[22m
[2m────────────────────────────────────────[22m

[2mPrint all AI prompts:[22m coderabbit review --show-prompts
```
