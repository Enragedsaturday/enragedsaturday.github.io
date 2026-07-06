# CodeRabbit gate — S2 @ 50ef21f (base: main)

- run: 2026-07-06T09:29:54Z
- cli: 0.6.4
- mode: --plain --type committed --base main 
- scope: .coderabbit.yaml path filters (code only)

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 14s elapsed
Preparing review... 23s elapsed
[2m────────────────────────────────────────[22m
[38;2;215;93;44mCodeRabbit Review[39m

[2mDiff      : [22mcommitted changes only
[2mCompare   : [22mHEAD [2m→[22m main
[2mDirectory : [22mcr-gate-S2-TiJ7c1
[2m────────────────────────────────────────[22m

[38;2;215;93;44m(\(\[39m
[38;2;215;93;44m(• .•)[39m  Unix was not designed to stop its users from doing stupid things, as that would also stop them from doing clever things.

Preparing sandbox... 26s elapsed
Summarizing changes... 47s elapsed
Summarizing changes... 1m 14s elapsed - still working
Summarizing changes... 2m 14s elapsed - still working
Summarizing changes... 3m 14s elapsed - still working
Summarizing changes... 4m 15s elapsed - still working
Summarizing changes... 5m 15s elapsed - still working
Summarizing changes... 6m 15s elapsed - still working
Finishing analysis tools... 6m 43s elapsed - still working
Writing review comments... 6m 43s elapsed - still working
Writing review comments... 7m 15s elapsed - still working
Writing review comments... 8m 15s elapsed - still working

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint14_pagerecord.py:28[36m[4mscripts/lint/lint14_pagerecord.py[24m[39m[2m:[22m[36m28-36[39m]8;;

  Corrupt/duplicate lake records fail silently instead of failing closed.

  [36mload_records()[39m swallows [36mJSONDecodeError[39m with a bare [36mcontinue[39m (no
  diagnostic), and also silently overwrites entries when two lake files
  share the same [36mrecord_id[39m (dict key collision at line 35). Since this
  lint only inspects markdown pages, a corrupted or duplicate-keyed record
  with no referencing page will never surface as a violation — an
  exception/empty state is effectively treated as a non-issue.

  Consider emitting a [36mc.make_violation[39m (or at least a hard failure) for
  unparsable JSON and for duplicate [36mrecord_id[39m values, so corruption in the
  lake can't pass unnoticed.





  Proposed fix sketch

  [2m def load_records():[22m
  [2m     records = {}[22m
  [32m+    violations = [][39m
  [2m     for path in sorted(glob.glob(os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases", "*.json"))):[22m
  [2m         try:[22m
  [31m-            record = json.load(open(path, encoding="utf-8"))[39m
  [31m-        except json.JSONDecodeError:[39m
  [31m-            continue[39m
  [31m-        records[record.get("record_id")] = (path, record)[39m
  [31m-    return records[39m
  [32m+            with open(path, encoding="utf-8") as fh:[39m
  [32m+                record = json.load(fh)[39m
  [32m+        except json.JSONDecodeError as exc:[39m
  [32m+            violations.append(c.make_violation(LINT, path, 1, c.HIGH, "unparsable lake record JSON: %s" % exc))[39m
  [32m+            continue[39m
  [32m+        rid = record.get("record_id")[39m
  [32m+        if rid in records:[39m
  [32m+            violations.append(c.make_violation([39m
  [32m+                LINT, path, 1, c.HIGH,[39m
  [32m+                "duplicate record_id=%r also defined in %s" % (rid, c.relpath(records[rid][0]))))[39m
  [32m+        records[rid] = (path, record)[39m
  [32m+    return records, violations[39m

  As per path instructions: "Flag any path where an exception or empty
  result could be recorded as a verified state."


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/run_all.py:3[36m[4mscripts/lint/run_all.py[24m[39m[2m:[22m[36m3-10[39m]8;;

  Docstring roster is stale — it omits LINT-18 through LINT-25.

  The [36mLINTS[39m list (Lines 62-75) now registers LINT-18,19,20,21,22,23,24,25,
  but the module docstring still advertises only
  "LINT-2,3,4,5,6,7,8,9,10,12,13,14 + LINT-26". For an audited fail-closed
  gate runner, the roster description should match what actually executes.





  📝 Suggested docstring update

  [31m-Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8,9,10,12,13,14 + LINT-26) over[39m
  [31m-content/. Fixture self-tests for LINT-10/12/13/14 run first, fail-closed. The[39m
  [32m+Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8,9,10,12,13,14,18,19,20,21,[39m
  [32m+22,23,24,25,26) over content/. Fixture self-tests for LINT-10/12/13/14 run[39m
  [32m+first, fail-closed. The[39m
  [2m full numeric roster LINT-1…30 is codified at S9 (S9 R8); rows land here as[22m
  [2m their owning specs execute.[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/docs/STANDARDS.md:549[36m[4mdocs/STANDARDS.md[24m[39m[2m:[22m[36m549-552[39m]8;;

  Label this fenced block.

  This code fence has no language tag, which trips markdownlint (MD040) and
  weakens renderer consistency. A neutral tag like [36mtext[39m is enough.


  ♻️ Proposed fix

  [31m-[39m

  +

  [2m field_i_validity ∈ { good_law 🟢 | history 🔵 | caution 🟡 | questioned 🟠 |[22m
  [2m                      superseded 🔴 | unverified ⚪ }[22m
  [31m-[39m

  +

  


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/authority_db.py:639[36m[4mscripts/s2/authority_db.py[24m[39m[2m:[22m[36m639-651[39m]8;;

  [36mverify_roundtrip[39m reports success on an empty [36mcases[39m table.

  If the [36mcases[39m table has no rows, the loop body never executes, [36merrors[39m
  stays empty, and the function returns [36mTrue[39m — reporting a verified
  roundtrip for a DB that contains no records. Per path instructions this
  pipeline must fail closed and never record an empty result as a verified
  state. A vacuous pass here would mask a build that silently produced
  nothing.

  As per path instructions: "Flag any path where an exception or empty
  result could be recorded as a verified state."





  🛡️ Proposed fix to fail closed on empty result

  [2m def verify_roundtrip(path=None):[22m
  [2m     path = path or db_path()[22m
  [2m     conn = sqlite3.connect(path)[22m
  [2m     rows = conn.execute("SELECT record_id, record_path, record_json FROM cases ORDER BY record_id").fetchall()[22m
  [2m     conn.close()[22m
  [32m+    if not rows:[39m
  [32m+        raise RuntimeError("verify_roundtrip: no rows in cases; refusing to report success on empty DB")[39m
  [2m     errors = [][22m
  [2m     for rid, rel, record_json in rows:[22m

Writing review comments... 9m 58s elapsed - still working - 4 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/components/scripts/casetable.inline.ts:143[36m[4mquartz/components/scripts/casetable.inline.ts[24m[39m[2m:[22m[36m143-194[39m]8;;

  Case-name sort can pick up the injected treatment-pill anchor instead of
  the case name.

  [36mquerySelector("a, em, i")[39m returns the first matching element in document
  order within the cell. When the case name itself is plain text (no
  link/em/i — plausible per the comment "before S6 wires [[links]]") and
  [36minjectCaseMeta[39m appends a treatment pill `` (line 163), that pill becomes
  the only anchor in the cell, so the sort value becomes the treatment label
  text instead of the case name — silently breaking the case-column sort for
  exactly the rows this logic was meant to protect (per the code's own
  comment: "the injected meta line must not pollute order").


  🐛 Proposed fix: exclude elements inside the injected meta span

  [2m       case "case":[22m
  [2m         // sort by the case NAME only — the injected meta line must not pollute order[22m
  [31m-        return ([39m
  [31m-          row.cells[col]?.querySelector("a, em, i")?.textContent ??[39m
  [31m-          txt[39m
  [31m-        )[39m
  [31m-          .toLowerCase()[39m
  [31m-          .trim()[39m
  [32m+        return (() => {[39m
  [32m+          const cell = row.cells[col][39m
  [32m+          if (!cell) return txt.toLowerCase().trim()[39m
  [32m+          const meta = cell.querySelector(".casetable-case-meta")[39m
  [32m+          for (const el of cell.querySelectorAll("a, em, i")) {[39m
  [32m+            if (!meta || !meta.contains(el)) return (el.textContent ?? txt).toLowerCase().trim()[39m
  [32m+          }[39m
  [32m+          return txt.toLowerCase().trim()[39m
  [32m+        })()[39m

  Also applies to: 266-273


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/_overhaul2/scripts/audit_cases.py:623[36m[4m_overhaul2/scripts/audit_cases.py[24m[39m[2m:[22m[36m623-626[39m]8;;

  Sanity gate uses [36massert[39m, which is stripped under [36mpython -O[39m.

  [36massert_no_page_collisions[39m is the last-line guarantee that no roster row
  aliases an existing case page. If this script is ever invoked with [36m-O[39m
  (or [36mPYTHONOPTIMIZE[39m), the assertion is compiled out and a colliding
  roster would be emitted silently as a "PASS". Prefer an explicit raise so
  the check cannot be optimized away.





  🛡️ Proposed fix

  [2m def assert_no_page_collisions(roster, index: PageIndex):[22m
  [2m     for row in roster:[22m
  [31m-        assert index.match(row["norm"], row["caption"]) is None, ([39m
  [31m-            f"roster row matches an existing case page: {row['caption']}")[39m
  [32m+        if index.match(row["norm"], row["caption"]) is not None:[39m
  [32m+            raise AssertionError([39m
  [32m+                f"roster row matches an existing case page: {row['caption']}")[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/components/scripts/casetable.inline.ts:162[36m[4mquartz/components/scripts/casetable.inline.ts[24m[39m[2m:[22m[36m162-174[39m]8;;

  Treatment pill falls back to a dead [36m#[39m link when [36mgoodLawHref[39m is
  missing.

  [36mindex.goodLawHref[39m is optional on [36mCaseIndex[39m (line 32). If the embedded
  data island omits it (stale build, partial migration, malformed JSON), the
  pill still renders as a clickable [36ma.internal[39m pointing at [36m"#"[39m, causing
  an unexpected scroll-to-top on click rather than degrading gracefully.


  🛡️ Proposed fix: don't render as a link when the target is unknown

  [31m-  if (rec.treatment && !hasTreatmentCol) {[39m
  [31m-    const pill = document.createElement("a")[39m
  [32m+  if (rec.treatment && !hasTreatmentCol) {[39m
  [32m+    const pill = document.createElement(index.goodLawHref ? "a" : "span")[39m
  [2m     ...[22m
  [31m-    pill.href = index.goodLawHref ?? "#"[39m
  [32m+    if (index.goodLawHref && pill instanceof HTMLAnchorElement) pill.href = index.goodLawHref[39m

  As per path instructions, this file should prioritize accessibility for
  [36mquartz/[39m.


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint16_casetables.py:20[36m[4mscripts/lint/lint16_casetables.py[24m[39m[2m:[22m[36m20-22[39m]8;;

  Replace the Unicode union symbol.

  Ruff flags [36m∪[39m here (RUF002). Reword this prose in ASCII so the file stays
  lint-clean.


  Suggested edit

  [31m-#  * OPINION-LINK HOST (R17): every opinion link's host ∈ CourtListener ∪ the[39m
  [32m+#  * OPINION-LINK HOST (R17): every opinion link's host ∈ CourtListener or the[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint16_casetables.py:244[36m[4mscripts/lint/lint16_casetables.py[24m[39m[2m:[22m[36m244-245[39m]8;;

  Fail closed on empty opinion-link hosts
  [36m_host()[39m returns [36m""[39m for relative or scheme-less URLs, so `if host and
  not _host_ok(host)` lets malformed opinion links pass. Reject empty hosts
  here:

  [31m-                    if host and not _host_ok(host):[39m
  [32m+                    if not host or not _host_ok(host):[39m

Writing review comments... 12m 03s elapsed - still working - 9 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/_common.py:441[36m[4mscripts/lint/_common.py[24m[39m[2m:[22m[36m441-442[39m]8;;

  [36mis_table_row[39m should ignore masked pipes too. [36miter_tables[39m treats a
  prose line like [36mSee [[Page|alias]]...[39m or `[36mSee [39mx | y``` as a table
  header when followed by a separator row, because it only checks raw `"|"
  in line[36m. Reuse the same pipe-masking logic as [39msplit_table_row` so
  wikilinks and code spans do not trigger table detection.

Writing review comments... 13m 23s elapsed - still working - 10 findings so far
Writing review comments... 14m 23s elapsed - still working - 10 findings so far
Writing review comments... 15m 23s elapsed - still working - 10 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint15_skeleton.py:175[36m[4mscripts/lint/lint15_skeleton.py[24m[39m[2m:[22m[36m175-195[39m]8;;

  Misleading "missing" message when callout is present but after the first
  H2.

  Line 184's condition folds two distinct cases into one message:
  [36mcallout_line is None[39m (truly absent) and [36mcallout_line >= first_h2_line[39m
  (callout exists, just placed after the first H2 section). Both currently
  emit "missing the '> [!rule]' ... callout", which is inaccurate for the
  second case and could confuse authors trying to fix the violation.


  🐛 Proposed fix to separate the two cases

  [31m-    if callout_line is None or callout_line >= first_h2_line:[39m
  [31m-        out.append(c.make_violation([39m
  [31m-            LINT, path, start, c.HIGH,[39m
  [31m-            "doctrine skeleton: missing the '> [!rule]' black-letter callout in "[39m
  [31m-            "the header zone (R1/R2 — opens every doctrine page, before the "[39m
  [31m-            "first H2)"))[39m
  [32m+    if callout_line is None:[39m
  [32m+        out.append(c.make_violation([39m
  [32m+            LINT, path, start, c.HIGH,[39m
  [32m+            "doctrine skeleton: missing the '> [!rule]' black-letter callout in "[39m
  [32m+            "the header zone (R1/R2 — opens every doctrine page, before the "[39m
  [32m+            "first H2)"))[39m
  [32m+    elif callout_line >= first_h2_line:[39m
  [32m+        out.append(c.make_violation([39m
  [32m+            LINT, path, start + callout_line, c.HIGH,[39m
  [32m+            "doctrine skeleton: '> [!rule]' callout appears after the first H2 "[39m
  [32m+            "— it must be in the header zone, before the first H2 [R1]"))[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/project.py:38[36m[4mscripts/s2/project.py[24m[39m[2m:[22m[36m38-48[39m]8;;

  Lake records missing [36mrecord_id[39m are silently dropped.

  If a record lacks [36mrecord_id[39m, it's skipped from [36mrecords[39m/[36mrecord_paths[39m
  with no warning or count. Any case page pointing to that record will then
  hit [36mif not record: continue[39m in [36mdry_run_or_write[39m and never get
  projected, with no diagnostic surfaced anywhere in the gate/summary
  output.

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" — the A13 gate can report
  PASS while some lake records are effectively invisible to the pipeline.


  🛡️ Proposed fix

  [2m def load_records(lake_root=None):[22m
  [2m     lake_root = lake_root or os.path.join(REPO_ROOT, LAKE_REL)[22m
  [2m     records = {}[22m
  [2m     record_paths = {}[22m
  [32m+    skipped = [][39m
  [2m     for path in sorted(glob.glob(os.path.join(lake_root, "cases", "*.json"))):[22m
  [2m         record = load_json(path)[22m
  [2m         rid = record.get("record_id")[22m
  [2m         if rid:[22m
  [2m             records[rid] = record[22m
  [2m             record_paths[rid] = path[22m
  [32m+        else:[39m
  [32m+            skipped.append(path)[39m
  [32m+    if skipped:[39m
  [32m+        sys.stderr.write("warning: %d lake record(s) missing record_id: %s\n" % (len(skipped), ", ".join(skipped)))[39m
  [2m     return records, record_paths[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/project.py:436[36m[4mscripts/s2/project.py[24m[39m[2m:[22m[36m436-448[39m]8;;

  [36m--dry-run[39m flag is defined but never used.

  [36margs.dry_run[39m (Line 439) is parsed but nothing in [36mmain()[39m reads it —
  [36mdry_run_or_write[39m is always called with [36mwrite=args.write[39m. Since dry-run
  is already the default, [36m--dry-run[39m is a silent no-op, and passing both
  [36m--write --dry-run[39m together gives no indication that [36m--dry-run[39m was
  ignored.


  🛡️ Proposed fix

  [2m     args = parser.parse_args(argv)[22m
  [32m+    if args.dry_run and args.write:[39m
  [32m+        parser.error("--write and --dry-run are mutually exclusive")[39m
  [2m     if args.self_test:[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint15_skeleton.py:196[36m[4mscripts/lint/lint15_skeleton.py[24m[39m[2m:[22m[36m196-202[39m]8;;

  [36m.title()[39m produces the wrong canonical heading text for multi-word
  sections.

  [36m"key cases".title()[39m yields [36m"Key Cases"[39m, but the actual canonical
  heading used throughout the fixtures is [36m"## Key cases"[39m (lowercase
  "cases"). The violation message would tell an author to add a heading that
  doesn't match the checker's own expected form.


  🐛 Proposed fix using explicit display names

  [31m-# F-S5-09 — the REQUIRED doctrine H2 sections (absent = HIGH). Optional sections[39m
  [31m-REQUIRED_DOCTRINE_H2 = ("the brief", "key cases", "sources")[39m
  [32m+# F-S5-09 — the REQUIRED doctrine H2 sections (absent = HIGH). Optional sections[39m
  [32m+REQUIRED_DOCTRINE_H2 = ("the brief", "key cases", "sources")[39m
  [32m+REQUIRED_DOCTRINE_H2_DISPLAY = {[39m
  [32m+    "the brief": "The Brief",[39m
  [32m+    "key cases": "Key cases",[39m
  [32m+    "sources": "Sources",[39m
  [32m+}[39m

  [2m     for req in REQUIRED_DOCTRINE_H2:[22m
  [2m         if req not in h2_norms:[22m
  [2m             out.append(c.make_violation([22m
  [2m                 LINT, path, start, c.HIGH,[22m
  [2m                 "doctrine skeleton: missing required '## %s' section [R1]"[22m
  [31m-                % req.title()))[39m
  [32m+                % REQUIRED_DOCTRINE_H2_DISPLAY[req]))[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint21_binding.py:136[36m[4mscripts/lint/lint21_binding.py[24m[39m[2m:[22m[36m136-145[39m]8;;

  Bound row with empty [36mnodes[39m silently bypasses resolution.

  The bound-slug check at Line 168 only tests `if slug in slug_map:
  continue[36m, without verifying [39mslug_map[slug][36m is non-empty. A [39mbound[]`
  row like [36m{s2_point: "foo", nodes: []}[39m (or [36mnodes[39m omitted) puts [36m"foo"[39m
  into [36mslug_map[39m with an empty list (Line 144), so any live lake override
  for that slug is treated as "bound live" and skipped — even though it
  resolves to zero registry nodes. This contradicts the stated invariant
  "(a) every ... slug ... resolves to >= 1 registry node id via the map" and
  the fail-closed goal called out in the docstring (Lines 11-16). The
  dangling-node check (b) can't catch this either, since an empty [36mnodes[39m
  list contributes nothing to [36mmapped_nodes[39m.

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."





  🐛 Proposed fix

  [2m     for slug, cluster, src in lake_overrides:[22m
  [31m-        if slug in slug_map:[39m
  [32m+        if slug in slug_map and slug_map[slug]:[39m
  [2m             continue  # bound live (its nodes were dangling-checked above)[22m

  Also applies to: 166-181


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s5/convert_tables.py:526[36m[4mscripts/s5/convert_tables.py[24m[39m[2m:[22m[36m526-565[39m]8;;

  Per-page errors never fail the process — exit code always 0.

  [36mmain()[39m catches any per-page exception, records it in [36mreports[39m (Line
  534) with only [36m{"page", "error"}[39m — no [36m"changed"[39m, [36m"actions"[39m, or
  [36m"deferred"[39m keys, an inconsistent report shape versus successful pages —
  and then [36mcontinue[39ms. But the function unconditionally calls [36msys.exit(0)[39m
  at Line 565 regardless of whether any page errored. A gate/CI script that
  checks this tool's exit code will see success even when pages failed to
  convert, which is exactly the failure mode the pipeline's path
  instructions call out to avoid: errors must never pass silently as
  success.

  Similarly, if [36mpaths[39m ends up empty (e.g. a glob typo), the run still
  reports "0 page(s)... 0 actions · 0 deferred" and exits 0 —
  indistinguishable from a genuinely clean run.


  🚦 Proposed fix: propagate per-page failures to the exit code

  [2m     apply = args.apply[22m
  [2m     paths = list(c.iter_markdown_files(args.pages))[22m
  [2m     reports = [][22m
  [2m     n_changed = 0[22m
  [32m+    n_errors = 0[39m
  [2m     for path in paths:[22m
  [2m         try:[22m
  [2m             report, new_text = convert_page(path)[22m
  [2m         except Exception as e:  # never die on one bad page[22m
  [2m             reports.append({"page": c.relpath(path), "error": str(e)})[22m
  [2m             sys.stderr.write("[convert] ERROR %s: %s\n" % (c.relpath(path), e))[22m
  [32m+            n_errors += 1[39m
  [2m             continue[22m
  [36m@@[39m
  [2m     sys.stderr.write([22m
  [2m         "\n[convert] %d page(s): %d would change%s · %d action(s) · %d deferred\n" % ([22m
  [2m             len(paths), n_changed, "" if apply else " (dry-run)",[22m
  [2m             total_actions, total_defer))[22m
  [31m-    sys.exit(0)[39m
  [32m+    sys.exit(1 if n_errors else 0)[39m

  As per path instructions, "fail-closed behavior (errors must never pass
  silently as success)" should be prioritized for this build/gate tooling.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/project.py:283[36m[4mscripts/s2/project.py[24m[39m[2m:[22m[36m283-294[39m]8;;

  Surface unmatched case pages instead of skipping them

  [36mif not record: continue[39m drops case pages with stale or deleted
  [36mrecord_id[39ms from [36mpage_results[39m and the summary, so the projection can
  look clean while the lake/page mapping is out of sync. Track these as
  unmatched and surface them in the returned result.


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/styles/custom.scss:17[36m[4mquartz/styles/custom.scss[24m[39m[2m:[22m[36m17-27[39m]8;;

  Missing blank line before comments fails lint.

  Lines 20, 22, 90, and 100 place a [36m//[39m comment directly after a
  declaration/brace with no blank line, tripping
  [36mscss/double-slash-comment-empty-line-before[39m.


  🔧 Proposed fix

  [2m     flex: 1 1 auto;[22m
  [2m     min-height: 0;[22m
  [32m+[39m
  [2m     // contain belongs HERE (the scroll container) so the explorer doesn't scroll the page[22m
  [2m     overscroll-behavior: contain;[22m
  [32m+[39m
  [2m     // and this must actually BE the scroll container: stock `div:has(> .overflow)`[22m

  [2m     }[22m
  [32m+[39m
  [2m     // horizontal tick into the row — 0.95rem aligns with row centers[22m
  [2m     // (file rows ≈0.975rem, folder rows ≈0.95rem — audit CODE-06; was 0.85rem)[22m
  [2m     &::after {[22m

  [2m     }[22m
  [32m+[39m
  [2m     // last item: run stops at the tick → └ elbow[22m
  [2m     &:last-child::before {[22m

  Also applies to: 90-100


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/components/styles/casetable.scss:139[36m[4mquartz/components/styles/casetable.scss[24m[39m[2m:[22m[36m139[39m]8;;

  Value-keyword-case lint error.

  [36mcurrentColor[39m should be lowercase [36mcurrentcolor[39m per
  [36mvalue-keyword-case[39m.


  🔧 Proposed fix

  [31m-      background: currentColor;[39m
  [32m+      background: currentcolor;[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/components/styles/casetable.scss:6[36m[4mquartz/components/styles/casetable.scss[24m[39m[2m:[22m[36m6-10[39m]8;;

  Empty SCSS comment fails lint.

  The standalone [36m//[39m on Line 6 is flagged by [36mscss/comment-no-empty[39m and
  will fail the stylelint gate.


  🔧 Proposed fix

  [2m // S3 · R4 #2 / R8 — sortable + filterable case table. The static markdown table is[22m
  [2m // untouched until JS runs, and the existing `.table-container { overflow-x: auto }`[22m
  [2m // keeps the fallback horizontally scrollable on mobile.[22m
  [31m-//[39m
  [2m // S5 — the ONE table schema (NUM-07): narrow columns are pinned, holding/relevance[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz.layout.ts:30[36m[4mquartz.layout.ts[24m[39m[2m:[22m[36m30-33[39m]8;;

  Scope the explorer exclusions to top-level nodes

  [36mfilterFn[39m runs on every trie node, so this also hides any nested
  folder/page named [36mabout[39m, [36mtags[39m, or [36mcases[39m. Restrict it to the
  top-level entries only so future nested content with those names doesn’t
  disappear from the explorer.


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/quartz/components/styles/treatmentBadge.scss:5[36m[4mquartz/components/styles/treatmentBadge.scss[24m[39m[2m:[22m[36m5-9[39m]8;;

  Empty SCSS comment fails lint.

  Same [36mscss/comment-no-empty[39m issue as flagged in [36mcasetable.scss[39m —
  standalone [36m//[39m on Line 5.


  🔧 Proposed fix

  [2m // S3 · R4 #1 — treatment badge (colored, good-law axis) + authority-weight label[22m
  [2m // (neutral outline, separate axis). The two axes are kept visually distinct.[22m
  [31m-//[39m
  [2m // S5 — the pill renders the Field-I COMPOSITE (PRACTICES §2): good-law · history ·[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/project.py:215[36m[4mscripts/s2/project.py[24m[39m[2m:[22m[36m215-250[39m]8;;

  [36mmissing_treatment_status[39m should block projection. [36mok_to_project[39m only
  checks [36munmapped[39m, so pages with neither [36mfield_i_validity[39m nor [36mstatus[39m
  still pass the gate and flow through [36mdry_run_or_write()[39m. Fold
  [36mmissing_treatment_status[39m into the refusal path or move those pages to
  [36mreview[39m.

Writing review comments... 17m 36s elapsed - still working - 23 findings so far
Writing review comments... 18m 36s elapsed - still working - 23 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31m[1mcritical[22m[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/ingest.py:2701[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m2701-2771[39m]8;;

  Treatment migration seeding mutates [36mtreatment.field_i_validity[39m before
  the fail-closed status gate, so [36mnot_found[39m/[36mblocked[39m records can end up
  with a non-[36munverified[39m treatment validity.

  In [36mprocess_page_record[39m, when identity resolution fails, the code sets
  status to [36mnot_found[39m or [36mblocked[39m (both in [36mFAIL_CLOSED_STATUSES[39m) and
  then unconditionally calls `seed_treatment_from_migration(record_json,
  source_record, migration)` (lines 3969-3971). Inside that function,
  [36mtreatment.update({"field_i_validity": field_i, ...})[39m (lines 2729-2737)
  runs unconditionally, and the only status-transition guard is `if
  record_json.get("status") == "verified":` (line 2738) — which does not
  match [36mnot_found[39m/[36mblocked[39m. The result: a record whose CourtListener
  identity could never be confirmed is persisted with a populated
  [36mtreatment.field_i_validity[39m (e.g. [36m"good_law"[39m) instead of
  [36m"unverified"[39m, even though [36mstatus[39m correctly stays fail-closed.
  [36mseed_preseeded_treatment[39m (lines 2668-2699) has the same ordering problem
  — [36mtreatment["field_i_validity"] = field_i[39m at line 2678 runs before the
  [36mset_record_status[39m gate at line 2686.

  Downstream consumers reading [36mtreatment.field_i_validity[39m (e.g. a UI
  treatment badge) could show a validity signal for a case whose very
  existence in CourtListener was never confirmed — directly undermining the
  fail-closed identity gate this pipeline is built around. No self-test
  currently exercises "identity resolves to not_found/blocked while
  [36mlegacy_treatment_status[39m is present," which is why this slipped through.


  🛡️ Proposed fix

  [2m             if seed_treatment_from_migration(record_json, source_record, migration):[22m
  [31m-                changed = True[39m
  [32m+                changed = True[39m
  [2m             changed = True[22m
  [2m             record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("S2 treatment derivation proposed only")[22m
  [2m             write_case_record(paths, record_json)[22m
  [2m             return record_json[22m

  Guard the seed instead at the top of
  [36mseed_treatment_from_migration[39m/[36mseed_preseeded_treatment[39m:

  [2m def seed_treatment_from_migration(record_json, source_record, migration):[22m
  [2m     if record_json.get("stub"):[22m
  [2m         return False[22m
  [32m+    if record_json.get("status") in FAIL_CLOSED_STATUSES:[39m
  [32m+        return False[39m
  [2m     legacy = {...}[22m

  As per path instructions for [36mscripts/[39m: "Flag any path where an exception
  or empty result could be recorded as a verified state."


  Also applies to: 3957-3974


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/s2/ingest.py:3469[36m[4mscripts/s2/ingest.py[24m[39m[2m:[22m[36m3469-3481[39m]8;;

  Silent JSON/OS error swallow in [36mmanifest_rows_by_record_id[39m weakens
  [36mrepair_migration_refs[39m's fail-closed lookup classification.

  If [36m_manifest.json[39m fails to parse (or a transient OS error occurs), this
  returns [36m{}[39m silently rather than surfacing the failure.
  [36mbuild_completed_case_lookup[39m then falls back to
  [36mrecord.get("source")[39m/[36mrecord.get("stub")[39m for [36msource[39m/[36mstub[39m, which can
  silently misclassify a record's [36mlookup_class[39m ("page" vs "frontier") in
  [36mcase_lookup_class[39m. Since [36mresolve_controlling_case[39m's single-page-match
  branch trusts [36mlookup_class[39m to disambiguate duplicates, a
  misclassification here could cause [36mrepair_migration_refs[39m to silently
  pick the wrong controlling-case reference and write it into
  [36mpoint_overrides[39m/[36medges[39m instead of failing closed with an error, which
  is exactly the failure mode this repair script is meant to prevent.

  🛡️ Proposed fix

  [2m def manifest_rows_by_record_id(paths):[22m
  [2m     if not os.path.exists(paths.manifest):[22m
  [2m         return {}[22m
  [31m-    try:[39m
  [31m-        manifest = read_json(paths.manifest)[39m
  [31m-    except (OSError, json.JSONDecodeError):[39m
  [31m-        return {}[39m
  [32m+    manifest = read_json(paths.manifest)[39m
  [2m     return {[22m

  As per path instructions for [36mscripts/[39m: "fail-closed behavior (errors
  must never pass silently as success)."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint9_carat_leak.py:51[36m[4mscripts/lint/lint9_carat_leak.py[24m[39m[2m:[22m[36m51-63[39m]8;;

  Fill character choice defeats the mid-line detection it's meant to fix.

  [36mfill()[39m blanks wikilinks/inline-code to [36m'x'[39m characters specifically so
  a trailing anchor+wikilink combo isn't misread as end-of-line (per the
  docstring rationale). But [36m'x'[39m is itself in [36mBLOCK_ANCHOR_RE[39m's character
  class ([36m[A-Za-z0-9-]*[39m), so when a wikilink/code span immediately follows
  a real anchor, the regex match extends through the fill and reaches the
  true end of the (rstripped) line — triggering the "end-of-line anchor...
  LEGAL" branch. This is the exact scenario the docstring says this design
  correctly flags as mid-line.

  Example: [36mSee rule ^pin-3[[Terry v. Ohio]][39m (wikilink is the last thing on
  the line, immediately adjacent to the anchor). In real Obsidian/Quartz
  rendering, [36m^pin-3[39m is not the last token on the line (the wikilink
  follows it with no separating whitespace), so it should leak/render
  literally and be flagged HIGH. Instead:
  - [36m_mask_links_and_code[39m produces [36mSee rule ^pin-3xxxxxxxxxxxxxxxxx[39m
  - [36mBLOCK_ANCHOR_RE[39m matches [36m^pin-3xxxxxxxxxxxxxxxxx[39m as one token (x's
  are alnum)
  - [36mm.end() == len(masked)[39m → classified as legal end-of-line anchor →
  false negative, the leak is silently missed.

  Use a fill character outside the anchor's character class (non-space,
  non-alnum/hyphen) so masked regions still block rstrip but can't be
  absorbed into the anchor match.





  🐛 Proposed fix

  [2m def _mask_links_and_code(line):[22m
  [2m     """Blank inline-code spans and [[wikilinks]] to same-length NON-space filler.[22m
  
  [2m     Unlike _common.mask_links_and_code (which blanks to SPACES), we fill with[22m
  [31m-    'x' so that (a) a '^' inside a masked wikilink [[Page#^pin-3]] is not seen,[39m
  [32m+    a non-word filler so that (a) a '^' inside a masked wikilink [[Page#^pin-3]] is not seen,[39m
  [2m     AND (b) a real anchor that is FOLLOWED by a wikilink/code span is correctly[22m
  [2m     treated as mid-line (blanking to spaces + rstrip would wrongly make it look[22m
  [2m     end-of-line and hide the leak)."""[22m
  [2m     def fill(m):[22m
  [31m-        return "x" * (m.end() - m.start())[39m
  [32m+        return "#" * (m.end() - m.start())[39m
  [2m     line = c.INLINE_CODE_RE.sub(fill, line)[22m
  [2m     line = c.WIKILINK_RE.sub(fill, line)[22m
  [2m     return line[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S2-TiJ7c1/scripts/lint/lint12_drift.py:47[36m[4mscripts/lint/lint12_drift.py[24m[39m[2m:[22m[36m47-55[39m]8;;

  Violation message reports the wrong file as having drift.

  [36m"S2 managed frontmatter drift in %s"[39m is formatted with
  [36mc.relpath(record_path)[39m (the lake JSON record), not [36mc.relpath(path)[39m
  (the actual markdown page with the drift). The lake record path is then
  repeated a second time later in the same message ("Edit the lake record,
  not frontmatter: %s"). The page path never appears in the message text
  itself (only implicitly inside [36m_project_command(path)[39m), which will
  confuse whoever reads the CI output.





  🐛 Proposed fix

  [2m         "S2 managed frontmatter drift in %s; differing fields: %s. Edit the "[22m
  [2m         "lake record, not frontmatter: %s. Re-project with: %s"[22m
  [31m-        % (c.relpath(record_path), shown, c.relpath(record_path), _project_command(path)),[39m
  [32m+        % (c.relpath(path), shown, c.relpath(record_path), _project_command(path)),[39m


[2m────────────────────────────────────────[22m
[38;2;215;93;44mReview complete[39m
[2m27 findings ✔[22m

[2mCritical 1[22m
[2mMajor    15[22m
[2mMinor    11[22m
[2m────────────────────────────────────────[22m

[2mPrint all AI prompts:[22m coderabbit review --show-prompts
```
