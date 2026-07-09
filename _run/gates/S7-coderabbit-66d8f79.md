# CodeRabbit gate — S7 @ 66d8f79 (base: ef0adfa)

- run: 2026-07-09T06:01:56Z
- cli: 0.6.4
- mode: --plain --type committed --base-commit ef0adfa 
- scope: .coderabbit.yaml path filters (code only)

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
╔═══════════════════════════════════════════╗
║                                           ║
║   New update available! 0.6.4 -> 0.6.5    ║
║          Run: coderabbit update           ║
║                                           ║
╚═══════════════════════════════════════════╝

Connecting to CodeRabbit... 2s elapsed
Preparing review... 6s elapsed
[2m────────────────────────────────────────[22m
[38;2;215;93;44mCodeRabbit Review[39m

[2mDiff      : [22mcommitted changes only
[2mCompare   : [22mHEAD [2m→[22m main
[2mDirectory : [22mcr-gate-S7-RqpHOo
[2m────────────────────────────────────────[22m

[38;2;215;93;44m(\(\[39m
[38;2;215;93;44m(• .•)[39m  Git gud or git out.

Preparing sandbox... 8s elapsed
Summarizing changes... 18s elapsed
Summarizing changes... 1m 02s elapsed - still working
Finishing analysis tools... 2m 02s elapsed - still working
Writing review comments... 2m 02s elapsed - still working
Writing review comments... 2m 02s elapsed - still working
Writing review comments... 3m 02s elapsed - still working

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s2/ingest.py:5279[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m5279-5284[39m]8;;

  Refuse panel rekeys that produce no citation display.

  The expected cite guard checks membership in [36mblock["all"][39m, but a
  [36mclassify_citations()[39m result with no [36mdisplay[39m still reaches the write
  path and leaves [36mrow["official_cite"][39m stale. Fail closed before mutating
  the record.






  Proposed fix

  [2m     cluster_cite_keys = {citation_compare_key(c.get("cite")) for c in block["all"]}[22m
  [2m     if citation_compare_key(expect_cite) not in cluster_cite_keys:[22m
  [2m         raise SystemExit([22m
  [2m             "--rekey-cluster-panel refuses row %s: expected cite %r absent from cached target cluster %s citations %s"[22m
  [2m             % (record_id, expect_cite, target_cluster_id, sorted(cluster_cite_keys))[22m
  [2m         )[22m
  [32m+    if not block.get("display"):[39m
  [32m+        raise SystemExit([39m
  [32m+            "--rekey-cluster-panel refuses row %s: cached target cluster %s produced no citations.display"[39m
  [32m+            % (record_id, target_cluster_id)[39m
  [32m+        )[39m
  [36m@@[39m
  [31m-    if block.get("display"):[39m
  [31m-        row["official_cite"] = block["display"][39m
  [32m+    row["official_cite"] = block["display"][39m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


  Also applies to: 5319-5320


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s2/ingest.py:5099[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m5099-5103[39m]8;;

  Fail closed on malformed cached [36msub_opinions[39m.

  Line 5102 currently drops an [36mextract_opinion_id()[39m failure and may still
  rekey from a later opinion ID. A corrupt or partially parsed cached
  opinion list should queue/abort, not produce a verified rekey from
  incomplete ordering.






  Proposed fix

  [2m def harmonized_lead_from_cluster(cluster, cluster_id):[22m
  [36m@@[39m
  [2m     subs = [][22m
  [2m     for item in cluster.get("sub_opinions") or []:[22m
  [2m         try:[22m
  [2m             oid = extract_opinion_id(item, "cluster.sub_opinions[]")[22m
  [31m-        except ValueError:[39m
  [31m-            continue[39m
  [32m+        except ValueError as exc:[39m
  [32m+            raise ValueError("cached cluster has an unparsable sub_opinion: %s" % exc) from exc[39m
  [2m         if oid:[22m
  [2m             subs.append(int(oid))[22m

  Then catch this in the callers and queue/abort before writing.



  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s2/ingest.py:11654[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m11654-11656[39m]8;;

  Reject panel companion args without [36m--rekey-cluster-panel[39m.

  These options are otherwise silently ignored and the command can fall
  through to normal ingest, potentially consuming live CL budget instead of
  running the intended cache-only maintenance action.






  Proposed guard

  [32m+    if ([39m
  [32m+        args.rekey_cluster_target[39m
  [32m+        or args.rekey_cluster_expect_cite[39m
  [32m+        or args.rekey_cluster_evidence[39m
  [32m+    ) and not args.rekey_cluster_panel:[39m
  [32m+        raise SystemExit([39m
  [32m+            "--rekey-cluster-target/--rekey-cluster-expect-cite/--rekey-cluster-evidence "[39m
  [32m+            "require --rekey-cluster-panel"[39m
  [32m+        )[39m

  As per path instructions, prioritize "fail-closed behavior" and "API-quota
  safety."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s2/ingest.py:5121[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m5121-5150[39m]8;;

  Move lead normalization into phase 1 prevalidation.

  Line 5150 can raise after earlier records in the batch have already been
  written, despite the phase-1 all-batch validation contract. Validate
  [36midentity.lead_opinion_id[39m before any write and carry the normalized value
  into phase 2.






  Proposed fix

  [31m-        targets.append((record_id, row, record, int(cluster_id)))[39m
  [32m+        try:[39m
  [32m+            cluster_id = int(cluster_id)[39m
  [32m+        except (TypeError, ValueError):[39m
  [32m+            raise SystemExit("--rekey-lead-opinion-from-cache row %s has non-integer identity.cluster_id: %r"[39m
  [32m+                             % (record_id, cluster_id)) from None[39m
  [32m+        raw_lead = (record.get("identity") or {}).get("lead_opinion_id")[39m
  [32m+        try:[39m
  [32m+            current_lead = int(raw_lead) if raw_lead is not None else None[39m
  [32m+        except (TypeError, ValueError):[39m
  [32m+            raise SystemExit("--rekey-lead-opinion-from-cache row %s has non-integer identity.lead_opinion_id: %r"[39m
  [32m+                             % (record_id, raw_lead)) from None[39m
  [32m+        targets.append((record_id, row, record, cluster_id, current_lead))[39m
  [36m@@[39m
  [31m-    for record_id, row, record, cluster_id in targets:[39m
  [32m+    for record_id, row, record, cluster_id, current_lead in targets:[39m
  [2m         identity = record.get("identity") or {}[22m
  [31m-        current_lead = identity.get("lead_opinion_id")[39m
  [31m-        current_lead = int(current_lead) if current_lead is not None else None[39m

  As per path instructions, prioritize "fail-closed behavior" and
  "resumability/idempotence (journal + cache driven)."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/_overhaul2/scripts/build_coverage_ledger.py:339[36m[4m_overhaul2/scripts/build_coverage_ledger.py[24m[39m[2m:[22m[36m339-403[39m]8;;

  Missing S7 disposition files are silently skipped, no failure signal.

  Each of the three blocks only loads its JSONL [36mif os.path.isfile(path)[39m;
  there's no [36melse[39m branch, warning, or count recorded when a file is
  absent. The final [36mok[39m gate (Line 620) doesn't factor in whether these
  stages actually ran, so a renamed/missing/upstream-failed disposition file
  produces a quietly smaller ledger and the script still reports [36mPASS[39m.
  Given this is verified-legal-authority tooling, an empty/missing ingestion
  source should not be indistinguishable from "ingested zero rows because
  there legitimately were none."


  🛡️ Suggested fix: record presence/absence and surface it in the report

  [32m+    s7_stage_status = {}[39m
  [2m     s7pool = os.path.join(O2, "S7-L1-POOLING-DISPOSITIONS.jsonl")[22m
  [31m-    if os.path.isfile(s7pool):[39m
  [32m+    s7_stage_status["S7-L1-POOLING-DISPOSITIONS.jsonl"] = os.path.isfile(s7pool)[39m
  [32m+    if os.path.isfile(s7pool):[39m
  [2m         for e in load_jsonl(s7pool):[22m
  [2m             ...[22m

  Then include [36ms7_stage_status[39m in [36mout["counts"][39m and fold `not
  all(s7_stage_status.values())` (or an explicit expected-files check) into
  the [36mok[39m computation, so a missing file fails the run instead of passing
  silently.


  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/survey.py:475[36m[4mscripts/s7/survey.py[24m[39m[2m:[22m[36m475-486[39m]8;;

  Fail closed when the survey is empty.

  If discovery returns zero substantive pages, this still writes a
  valid-looking JSON and exits 0. In this pipeline that lets a
  discovery/path regression get recorded as success.


  ♻️ Proposed fix

  [2m     survey = build_survey()[22m
  [32m+    if survey["totals"]["pages"] == 0:[39m
  [32m+        raise RuntimeError("No substantive pages discovered")[39m
  [2m     if "--stdout" in argv:[22m

  As per path instructions, prioritize fail-closed behavior (errors must
  never pass silently as success) and flag any path where an empty result
  could be recorded as a verified state.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Security & Privacy][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/survey.py:480[36m[4mscripts/s7/survey.py[24m[39m[2m:[22m[36m480-486[39m]8;;

  Reject missing [36m--out[39m values and bound the path.

  A bare [36m--out[39m silently falls back to the default output, and a relative
  [36m../...[39m can escape [36mREPO_ROOT[39m. Both should error before writing.


  🔒️ Proposed fix

  [2m     if "--out" in argv:[22m
  [2m         i = argv.index("--out")[22m
  [31m-        if i + 1 < len(argv):[39m
  [31m-            out_path = argv[i + 1][39m
  [31m-            if not os.path.isabs(out_path):[39m
  [31m-                out_path = os.path.join(REPO_ROOT, out_path)[39m
  [32m+        if i + 1 >= len(argv):[39m
  [32m+            raise ValueError("--out requires a path")[39m
  [32m+        out_path = argv[i + 1][39m
  [32m+        if not os.path.isabs(out_path):[39m
  [32m+            out_path = os.path.join(REPO_ROOT, out_path)[39m
  [32m+        resolved = os.path.realpath(out_path)[39m
  [32m+        root = os.path.realpath(REPO_ROOT)[39m
  [32m+        if not resolved.startswith(root + os.sep):[39m
  [32m+            raise ValueError("out path must stay under the repository root")[39m
  [32m+        out_path = resolved[39m

  As per path instructions, prioritize fail-closed behavior (errors must
  never pass silently as success).

Writing review comments... 6m 07s elapsed - still working - 7 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/build_worklist.py:283[36m[4mscripts/s7/build_worklist.py[24m[39m[2m:[22m[36m283-306[39m]8;;

  Preserve T2 resolution failures instead of collapsing them to
  absent/special.

  Ambiguous duplicate basenames and missing special hosts both become `cur =
  None[36m; special rows still keep [39mstate` as
  [36min-page[39m/[36mretained-parent[39m/[36mcross-ref[39m, so the summary can count
  unresolved rows as special materialized rows.


  Proposed fix

  [32m+def resolve_unique_basename(by_base, basename):[39m
  [32m+    hits = by_base.get(basename, [])[39m
  [32m+    if len(hits) == 1:[39m
  [32m+        return hits[0], "basename-match"[39m
  [32m+    if len(hits) > 1:[39m
  [32m+        return None, "AMBIGUOUS:%s" % ";".join(hits)[39m
  [32m+    return None, "absent"[39m
  [32m+[39m
  [36m@@[39m
  [31m-            hits = by_base.get(page, [])[39m
  [31m-            cur = hits[0] if len(hits) == 1 else None[39m
  [31m-            kind = "in-page"[39m
  [32m+            cur, resolution = resolve_unique_basename(by_base, page)[39m
  [32m+            kind = "in-page" if cur else resolution[39m
  [36m@@[39m
  [31m-            hits = by_base.get(page, [])[39m
  [31m-            cur = hits[0] if len(hits) == 1 else None[39m
  [31m-            kind = "retained-parent"[39m
  [32m+            cur, resolution = resolve_unique_basename(by_base, page)[39m
  [32m+            kind = "retained-parent" if cur else resolution[39m
  [36m@@[39m
  [31m-            hits = by_base.get(page, [])[39m
  [31m-            cur = hits[0] if len(hits) == 1 else None[39m
  [31m-            kind = "cross-ref"[39m
  [32m+            cur, resolution = resolve_unique_basename(by_base, page)[39m
  [32m+            kind = "cross-ref" if cur else resolution[39m
  [36m@@[39m
  [31m-            hits = by_base.get(spec, [])[39m
  [31m-            cur = hits[0] if len(hits) == 1 else None[39m
  [32m+            cur, resolution = resolve_unique_basename(by_base, spec)[39m
  [2m             row = by_path.get(cur) if cur else None[22m
  [31m-            kind = classify_t2_state(row)[39m
  [32m+            kind = classify_t2_state(row) if cur else resolution[39m

  As per path instructions, [36mscripts/[39m must prioritize correctness of
  comparison/normalization logic.





  Also applies to: 431-435


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/build_worklist.py:223[36m[4mscripts/s7/build_worklist.py[24m[39m[2m:[22m[36m223-263[39m]8;;

  Validate split-landing overrides before marking T1 rows resolved.

  Line 224 returns hardcoded paths as resolved even when the survey has no
  matching row, so Line 261 can count a missing override as resolved with
  [36m(no survey row)[39m flags.


  Proposed fix

  [31m-def resolve_t1_current(n, old_rel, by_base):[39m
  [32m+def resolve_t1_current(n, old_rel, by_path, by_base):[39m
  [2m     if n in T1_SPLIT_LANDINGS:[22m
  [31m-        return T1_SPLIT_LANDINGS[n], "split-into-sub-umbrella-index-landing"[39m
  [32m+        cur = T1_SPLIT_LANDINGS[n][39m
  [32m+        if cur in by_path:[39m
  [32m+            return cur, "split-into-sub-umbrella-index-landing"[39m
  [32m+        return None, "override-missing:%s" % cur[39m
  [36m@@[39m
  [31m-        cur, how = resolve_t1_current(n, old_rel, by_base)[39m
  [32m+        cur, how = resolve_t1_current(n, old_rel, by_path, by_base)[39m

  As per path instructions, [36mscripts/[39m must flag any path where an exception
  or empty result could be recorded as a verified state.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/build_worklist.py:456[36m[4mscripts/s7/build_worklist.py[24m[39m[2m:[22m[36m456-486[39m]8;;

  Reject unknown CLI arguments.

  Line 482 ignores unrecognized flags, so a typo like [36m--stdotu[39m silently
  writes output files instead of failing closed.


  Proposed fix

  [32m+import argparse[39m
  [36m@@[39m
  [2m def main(argv):[22m
  [32m+    parser = argparse.ArgumentParser()[39m
  [32m+    parser.add_argument("--stdout", action="store_true")[39m
  [32m+    args = parser.parse_args(argv)[39m
  [36m@@[39m
  [31m-    if "--stdout" in argv:[39m
  [32m+    if args.stdout:[39m

  As per path instructions, [36mscripts/[39m tooling must use fail-closed
  behavior.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S7-RqpHOo/scripts/s7/build_worklist.py:487[36m[4mscripts/s7/build_worklist.py[24m[39m[2m:[22m[36m487-491[39m]8;;

  Write generated outputs atomically.

  Direct writes can leave partial [36ms7-worklist.json[39m or [36mS7-WORKLIST.md[39m
  artifacts if interrupted, which weakens rerun/resume safety.


  Proposed fix

  [32m+def atomic_write(path, text):[39m
  [32m+    tmp = path + ".tmp"[39m
  [32m+    with open(tmp, "w", encoding="utf-8") as f:[39m
  [32m+        f.write(text)[39m
  [32m+    os.replace(tmp, path)[39m
  [32m+[39m
  [36m@@[39m
  [31m-    with open(os.path.join(REPO_ROOT, OUT_JSON_REL), "w", encoding="utf-8") as f:[39m
  [31m-        json.dump(worklist, f, ensure_ascii=False, indent=2)[39m
  [31m-        f.write("\n")[39m
  [31m-    with open(os.path.join(REPO_ROOT, OUT_MD_REL), "w", encoding="utf-8") as f:[39m
  [31m-        f.write(md)[39m
  [32m+    atomic_write(os.path.join(REPO_ROOT, OUT_JSON_REL),[39m
  [32m+                 json.dumps(worklist, ensure_ascii=False, indent=2) + "\n")[39m
  [32m+    atomic_write(os.path.join(REPO_ROOT, OUT_MD_REL), md)[39m

  As per path instructions, [36mscripts/[39m tooling must prioritize
  resumability/idempotence.


[2m────────────────────────────────────────[22m
[38;2;215;93;44mReview complete[39m
[2m11 findings ✔[22m

[2mMajor    11[22m
[2m────────────────────────────────────────[22m

[2mPrint all AI prompts:[22m coderabbit review --show-prompts
```
