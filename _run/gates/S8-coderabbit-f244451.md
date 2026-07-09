# CodeRabbit gate — S8 @ f244451 (base: 4c47b72)

- run: 2026-07-09T18:28:46Z
- cli: 0.6.5
- mode: --plain --type committed --base-commit 4c47b72 
- scope: .coderabbit.yaml path filters (code only)

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 5s elapsed
Preparing review... 11s elapsed
[2m────────────────────────────────────────[22m
[38;2;215;93;44mCodeRabbit Review[39m

[2mDiff      : [22mcommitted changes only
[2mCompare   : [22mHEAD [2m→[22m main
[2mDirectory : [22mcr-gate-S8-qNmSkD
[2m────────────────────────────────────────[22m

[38;2;215;93;44m(\(\[39m
[38;2;215;93;44m(• .•)[39m  GPU fans at max RPM: ready to blow away regressions.

Preparing sandbox... 14s elapsed
Summarizing changes... 23s elapsed
Summarizing changes... 1m 05s elapsed - still working
Summarizing changes... 2m 05s elapsed - still working
Finishing analysis tools... 2m 14s elapsed - still working
Writing review comments... 2m 14s elapsed - still working
Writing review comments... 3m 05s elapsed - still working

[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Maintainability & Code Quality][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/fixtures/mentions/zones_exempt.md:15[36m[4mscripts/s8/fixtures/mentions/zones_exempt.md[24m[39m[2m:[22m[36m15-17[39m]8;;

  Label the fenced block.

  This fixture will trigger MD040 because the inner code fence has no
  language tag. If the goal is just to exercise zone handling, mark it as
  [36mtext[39m so the sample stays lint-clean.


  ♻️ Proposed fix

  [31m-[39m

  +

  [2m Terry v. Ohio[22m
  [2m [22m

  ```


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/assemble_ledger.py:384[36m[4mscripts/s8/assemble_ledger.py[24m[39m[2m:[22m[36m384-395[39m]8;;

  [36mjoin()[39m should fail closed on an empty in-scope universe.

  The universe only includes mentions with a truthy [36mcaption_key[39m (Line 391
  [36mif not cap: continue[39m). If every mention lacks [36mcaption_key[39m (schema
  drift) or no mentions landed, [36muniverse[39m is empty, all four checks count
  [36m0[39m, and [36mclean[39m becomes [36mTrue[39m (Line 484). A gate that emits [36mclean[39m for
  zero verified captions defeats the R1 proof. Add an explicit fail-closed
  sentinel:


  🛡️ Proposed guard in join()

  [2m     violations = [][22m
  [2m [22m
  [32m+    # Fail closed: an empty in-scope universe is never a proof of R1.[39m
  [32m+    if not universe:[39m
  [32m+        violations.append({[39m
  [32m+            "check": "E-empty-universe",[39m
  [32m+            "detail": "no in-scope caption mentions in the ledger; refusing to "[39m
  [32m+                      "certify R1 clean (missing/empty mentions or absent caption_key)"})[39m
  [32m+[39m
  [2m     # R1 Check A — a page-backed caption may not have a plain mention.[22m

  Also add [36m"E_empty_universe"[39m to the [36mchecks[39m block so CI surfaces it.




  As per path instructions: "Flag any path where an exception or empty
  result could be recorded as a verified state."


  Also applies to: 483-485


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/assemble_ledger.py:265[36m[4mscripts/s8/assemble_ledger.py[24m[39m[2m:[22m[36m265-269[39m]8;;

  Missing [36mmentions[39m rows should be a gap, not a clean join.
  [36msrc["mentions"][39m falls back to [36m[][39m, so an absent/empty mention set
  reaches [36mjoin()[39m as an empty universe and returns [36mclean: True[39m over
  nothing. Mirror the embeds guard here or abort before assembling the
  ledger. [36mscripts/s8/assemble_ledger.py:265-269[39m

Writing review comments... 5m 38s elapsed - still working - 3 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/zones.py:287[36m[4mscripts/s8/zones.py[24m[39m[2m:[22m[36m287-320[39m]8;;

  Ignore [36m|[39m inside [36m[[...]][39m when computing the first-cell span

  [36m_first_cell_spans_of_case_table[39m treats every unescaped pipe as a column
  boundary, so an aliased wikilink in the first cell (`[[Terry v.
  Ohio|Terry]][36m) gets truncated at the inner [39m|` instead of the real table
  boundary. That leaves the tail of the link outside [36mcasecell[39m and
  available to the linkers.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/shingles.py:371[36m[4mscripts/s8/shingles.py[24m[39m[2m:[22m[36m371-373[39m]8;;

  Read errors don't fail the run — violates fail-closed requirement for gate
  tooling.

  [36msweep()[39m swallows per-file exceptions into [36mstats["read_errors"][39m but
  simply omits that file's blocks (Lines 371-373). [36mmain()[39m (Lines 485-491)
  then always [36mreturn 0[39m, even when [36mread_errors[39m is non-empty. A file that
  fails to parse (encoding issue, torn read, etc.) is silently excluded from
  both source and prose detection, and the script still reports success —
  exactly the "exception/empty result recorded as a verified state" pattern
  to avoid in this pipeline.


  🔒 Proposed fix: propagate read errors as a failing exit code

  [2m     hits, stats = sweep(content_root)[22m
  [2m     write_report(hits, stats, out_path)[22m
  [2m     print(json.dumps({"report": out_path, "summary": {[22m
  [2m         k: v for k, v in stats.items() if k != "read_errors"}}, ensure_ascii=False))[22m
  [2m     if stats["read_errors"]:[22m
  [2m         print("read_errors: " + json.dumps(stats["read_errors"], ensure_ascii=False))[22m
  [31m-    return 0[39m
  [32m+        return 1[39m
  [32m+    return 0[39m

  As per path instructions, "Prioritize: fail-closed behavior (errors must
  never pass silently as success)... Flag any path where an exception or
  empty result could be recorded as a verified state."





  Also applies to: 485-491


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/shingles.py:393[36m[4mscripts/s8/shingles.py[24m[39m[2m:[22m[36m393-399[39m]8;;

  [36mos.makedirs("")[39m crashes when [36m--out[39m has no directory component.

  [36mos.path.dirname(out_path)[39m returns [36m""[39m for a bare filename, and
  [36mos.makedirs("", exist_ok=True)[39m raises [36mFileNotFoundError[39m regardless of
  [36mexist_ok[39m. The default path always has a directory, but `--out
  somefile.jsonl` is a reachable CLI invocation per this module's own usage
  docs.


  🛡️ Proposed fix

  [2m def write_report(hits, stats, out_path):[22m
  [31m-    os.makedirs(os.path.dirname(out_path), exist_ok=True)[39m
  [32m+    out_dir = os.path.dirname(out_path)[39m
  [32m+    if out_dir:[39m
  [32m+        os.makedirs(out_dir, exist_ok=True)[39m

Writing review comments... 8m 04s elapsed - still working - 6 findings so far
Writing review comments... 9m 04s elapsed - still working - 6 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Security & Privacy][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/lint/lint28_fragments.py:42[36m[4mscripts/lint/lint28_fragments.py[24m[39m[2m:[22m[36m42-50[39m]8;;

  Host whitelist is broader than the documented S2 R14 list — undermines the
  authority-source gate.

  [36mALLOWED_HOST_SUFFIXES[39m mixes narrow entries ([36mscholar.google.com[39m,
  [36mlaw.cornell.edu[39m, [36mpress-pubs.uchicago.edu[39m) with their bare parent
  domains ([36mgoogle.com[39m, [36mcornell.edu[39m, [36muchicago.edu[39m). Since [36m_host_ok[39m
  accepts any host that [36mendswith("." + s)[39m, the bare-domain entries make
  the narrow ones dead code and let any subdomain of
  [36mgoogle.com[39m/[36mcornell.edu[39m/[36muchicago.edu[39m pass — e.g. [36mdrive.google.com[39m,
  [36madmissions.cornell.edu[39m — not just Scholar/LII/press-pubs as the
  docstring (lines 12-16) describes. In a verified legal-authority pipeline
  this host check exists specifically to constrain fragments to trusted
  mirrors; the broad suffixes silently widen that trust boundary.


  Proposed fix

  [2m ALLOWED_HOST_SUFFIXES = ([22m
  [2m     "courtlistener.com",[22m
  [2m     "justia.com",[22m
  [31m-    "scholar.google.com", "google.com",[39m
  [31m-    "law.cornell.edu", "cornell.edu",[39m
  [32m+    "scholar.google.com",[39m
  [32m+    "law.cornell.edu",[39m
  [2m     "supremecourt.gov",[22m
  [2m     "bailii.org", "commonlii.org",[22m
  [31m-    "press-pubs.uchicago.edu", "uchicago.edu",[39m
  [32m+    "press-pubs.uchicago.edu",[39m
  [2m )[22m

  As per path instructions, this pipeline should prioritize "correctness of
  comparison/normalization logic" and treat any weakening of the
  verified-authority gate as a priority fix.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_terms.py:550[36m[4mscripts/s8/link_terms.py[24m[39m[2m:[22m[36m550-552[39m]8;;

  Non-atomic writes risk corrupting content files on crash.

  Both [36mrun()[39m (Line 550-552) and [36mrun_unlink()[39m (Line 472-474) open the
  target markdown file directly in [36m"w"[39m mode and write the new text. If the
  process is killed or crashes mid-write (OOM, signal, disk full), the file
  is left truncated/corrupted with no way to recover the original content.
  Given this pipeline is described as a "verified legal-authority pipeline"
  that touches [36mcontent/.md[39m directly, a partial write on any single page
  corrupts the corpus.

  Write to a temp file in the same directory and [36mos.replace()[39m into place
  so each file update is all-or-nothing.


  🛡️ Proposed fix (apply to both write sites)

  [31m-            if write:[39m
  [31m-                with open(path, "w", encoding="utf-8") as fh:[39m
  [31m-                    fh.write(new_text)[39m
  [32m+            if write:[39m
  [32m+                tmp = path + ".tmp"[39m
  [32m+                with open(tmp, "w", encoding="utf-8") as fh:[39m
  [32m+                    fh.write(new_text)[39m
  [32m+                os.replace(tmp, path)[39m

  As per path instructions, "Build/gate tooling for a verified
  legal-authority pipeline. Prioritize: fail-closed behavior... Flag any
  path where an exception or empty result could be recorded as a verified
  state."


  Also applies to: 472-474


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_terms.py:201[36m[4mscripts/s8/link_terms.py[24m[39m[2m:[22m[36m201-230[39m]8;;

  Unreadable pages silently vanish from the index, masking the real error as
  "page does not resolve."

  [36mexcept OSError: continue[39m (Line 210-211) drops any file that fails to
  read (permissions, encoding, transient I/O) with no logging. Downstream,
  [36mvalidate_register[39m will then report that term's target as `"target page
  does not resolve"` — indistinguishable from an actually-deleted page. For
  a pipeline whose whole purpose is to fail loudly and surface real
  problems, a transient/permission read failure being reported identically
  to "page genuinely missing" hides the true root cause from whoever reads
  the dead-target report.


  🛡️ Proposed fix

  [2m         try:[22m
  [2m             text = c.read_text(path)[22m
  [31m-        except OSError:[39m
  [31m-            continue[39m
  [32m+        except OSError as exc:[39m
  [32m+            print("WARN: could not read %s for term index: %s" % (rel, exc),[39m
  [32m+                  file=sys.stderr)[39m
  [32m+            continue[39m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/fragments.py:358[36m[4mscripts/s8/fragments.py[24m[39m[2m:[22m[36m358-365[39m]8;;

  Output ledger written non-atomically.

  Rows are written directly to [36mout_path[39m with [36mopen(out_path, "w", ...)[39m.
  If the process is killed or errors mid-write (disk full, OOM, SIGKILL), a
  partial/corrupt [36ms8-fragments.jsonl[39m is left in place with no signal that
  it's incomplete — downstream consumers (e.g. [36massemble_ledger.py[39m) could
  treat it as a complete, verified artifact.


  🛡️ Write to a temp file then atomically rename

  [2m     os.makedirs(os.path.dirname(out_path), exist_ok=True)[22m
  [31m-    with open(out_path, "w", encoding="utf-8") as fh:[39m
  [31m-        for r in rows:[39m
  [31m-            fh.write(json.dumps(r, sort_keys=True) + "\n")[39m
  [32m+    tmp_path = out_path + ".tmp"[39m
  [32m+    with open(tmp_path, "w", encoding="utf-8") as fh:[39m
  [32m+        for r in rows:[39m
  [32m+            fh.write(json.dumps(r, sort_keys=True) + "\n")[39m
  [32m+    os.replace(tmp_path, out_path)[39m

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" for [36mscripts/[39m build/gate
  tooling.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/fragments.py:295[36m[4mscripts/s8/fragments.py[24m[39m[2m:[22m[36m295-335[39m]8;;

  Missing/misconfigured lake path silently produces a "successful" empty
  run.

  If [36mcases_dir[39m doesn't exist or is empty (e.g. bad [36m--cases-dir[39m,
  misconfigured [36m$CSSI_LAKE_ROOT[39m fallout), [36mglob.glob[39m returns [36m[][39m with no
  error, and [36mrun()[39m happily writes an empty-but-well-formed output with
  exit code 0. Downstream tooling has no way to distinguish "genuinely zero
  matched pinpoints" from "the pipeline is broken/misconfigured."


  🛡️ Fail loudly when the source directory is missing

  [2m def load_matched_pinpoints(cases_dir=LAKE_CASES):[22m
  [2m     """[(record_id, pin_id, lead_opinion_id, star_marker, quote)] over the whole[22m
  [2m     lake, matched-fidelity only, in stable (record, pin) order."""[22m
  [32m+    if not os.path.isdir(cases_dir):[39m
  [32m+        raise FileNotFoundError("cases_dir not found: %s" % cases_dir)[39m
  [2m     out = [][22m
  [2m     for path in sorted(glob.glob(os.path.join(cases_dir, "*.json"))):[22m

  As per path instructions, this is exactly the "empty result... recorded as
  a verified state" failure mode [36mscripts/[39m tooling must avoid.


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/caption_index.py:148[36m[4mscripts/s8/caption_index.py[24m[39m[2m:[22m[36m148-170[39m]8;;

  Silent alias-parse failure returns an empty list with no signal.

  If the inline-JSON alias form is malformed, the [36mexcept Exception: pass[39m
  (152-158) falls through to block-form parsing; if that also finds nothing,
  [36mparse_aliases[39m silently returns [36m[][39m. A page with real, malformed aliases
  in frontmatter is then indistinguishable from a page with no aliases at
  all — the docstring calls case pages "the WIKILINK TRUTH," so silently
  losing aliases weakens that authority without any trace.

  As per path instructions, exceptions/empty results in this pipeline should
  not pass as an unremarkable, "verified" empty state; consider logging when
  the inline form fails to parse as JSON but the frontmatter block still
  contains an [36maliases:[39m key that yields nothing.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/caption_index.py:233[36m[4mscripts/s8/caption_index.py[24m[39m[2m:[22m[36m233-236[39m]8;;

  Year-suffixed variant bug: adds the stem to its own variant set instead of
  the bare form.

  The comment says the year-suffixed stem "is itself a variant of the bare
  form," but the code adds [36mstem[39m to [36me["variants"][39m, i.e. the entry's own
  key is added to its own variant set. Downstream (line 356-357), `if nv in
  stem_norms: continue[36m always skips this because [39m_norm(stem)` is trivially
  already a stem norm — so this is a no-op. The bare form ([36mm.group(1)[39m) is
  never registered as a variant, so a case page like `"Davis v. United
  States (2011)"[36m with no sibling [39m"Davis v. United States"` page can never
  be auto-linked by its bare-form caption in prose — the entire point of
  this block.

  As per path instructions, this is a correctness bug in the
  comparison/normalization logic that a fail-closed pipeline should get
  right (here the failure mode is safe — the mention just stays unlinked —
  but the intended feature is silently broken).


  🐛 Proposed fix

  [2m         m = re.match(r"^(.*\S)\s*\(\d{4}\)$", stem)[22m
  [2m         if m:[22m
  [31m-            e["variants"].add(stem)[39m
  [32m+            e["variants"].add(m.group(1))[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/caption_index.py:245[36m[4mscripts/s8/caption_index.py[24m[39m[2m:[22m[36m245-265[39m]8;;

  Lake JSON parse failures are silently dropped with no counter or log.

  [36mexcept Exception: continue[39m (lines 254-255) drops malformed lake records
  before [36mn_lake[39m is even incremented — unlike the captionless case a few
  lines below, which is explicitly tracked via [36mn_lake_skipped[39m. A
  corrupted/unreadable lake identity file for a real case currently vanishes
  from the index with zero signal in [36mdoc["sources"][39m or the printed
  summary, so a broken lake record and an absent one are indistinguishable
  in the output.

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state" — this build script should
  surface parse failures (a counter, a warning print, or aggregating and
  failing the build) rather than silently continuing, especially since this
  file feeds the R1-R3 linker as the resolution truth.


  🛠️ Proposed fix

  [32m+    n_lake_errors = 0[39m
  [2m     for fn in lake_files:[22m
  [2m         try:[22m
  [2m             d = json.load(open(os.path.join(LAKE_DIR, fn), encoding="utf-8"))[22m
  [2m         except Exception:[22m
  [32m+            n_lake_errors += 1[39m
  [32m+            print(f"WARN: failed to parse lake record {fn}", file=sys.stderr)[39m
  [2m             continue[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/remediate_pins.py:312[36m[4mscripts/s8/remediate_pins.py[24m[39m[2m:[22m[36m312-320[39m]8;;

  Corrupted/malformed JSONL header is silently treated the same as "no
  header ever written," bypassing the fail-closed count-invariant check.

  [36m_read_jsonl_header[39m catches any exception during [36mjson.loads[39m and returns
  [36mNone[39m (Line 319-320), which [36mverify()[39m treats identically to the artifact
  simply not existing (Line 393-395, 408-412). That is by design when
  there's genuinely no prior [36m--write[39m run — but if a previous run crashed
  mid-write leaving a truncated/corrupt header line, this silently degrades
  [36mVERIFY[39m from "compare pin_refs_before/after" to "skip the check," and the
  tool can still print [36mVERIFY: PASS[39m as long as [36munqueued[39m/[36munresolved[39m are
  0 (Line 414-416). For a tool whose whole purpose is fail-closed
  verification of a legal-authority corpus, an exception reading its own
  audit artifact should be surfaced as a distinct failure rather than
  silently downgraded to "no baseline."

  As per path instructions, "Flag any path where an exception or empty
  result could be recorded as a verified state."


  🛠️ Proposed fix: distinguish "missing" from "corrupt"

  [2m def _read_jsonl_header():[22m
  [2m     if not os.path.exists(JSONL):[22m
  [31m-        return None[39m
  [32m+        return None, False[39m
  [2m     with open(JSONL, encoding="utf-8") as fh:[22m
  [2m         first = fh.readline()[22m
  [2m     try:[22m
  [31m-        return json.loads(first)[39m
  [31m-    except Exception:[39m
  [31m-        return None[39m
  [32m+        return json.loads(first), False[39m
  [32m+    except Exception:[39m
  [32m+        return None, True  # existed but unparsable — do not treat as "no baseline"[39m

  [31m-    header = _read_jsonl_header()[39m
  [32m+    header, header_corrupt = _read_jsonl_header()[39m
  [32m+    if header_corrupt:[39m
  [32m+        print("    baseline                      : (jsonl header CORRUPT — treating as FAIL)")[39m
  [2m     ...[22m
  [31m-    ok = (len(unqueued) == 0 and len(unresolved) == 0 and[39m
  [31m-          (baseline is None or pin_refs_now == baseline))[39m
  [32m+    ok = (len(unqueued) == 0 and len(unresolved) == 0 and not header_corrupt and[39m
  [32m+          (baseline is None or pin_refs_now == baseline))[39m

  Also applies to: 393-416


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/remediate_pins.py:62[36m[4mscripts/s8/remediate_pins.py[24m[39m[2m:[22m[36m62-84[39m]8;;

  Quote-opening heuristic doesn't verify the quoted text itself starts a
  sentence.

  [36m_begins_new_sentence[39m treats any opening quote character as sufficient
  evidence of a new sentence, without checking that the character following
  the quote is itself uppercase. A mid-sentence quotation continuation that
  happens to start with a lowercase word right after an opening quote (e.g.
  [36m^pin-1 "continuing the same sentence in lowercase..."[39m) would be
  misclassified as a sentence boundary and mechanically split — which is
  exactly the "genuinely mid-sentence" case the tool is supposed to fail
  closed on (Line 17-19 docstring).

  Given this tool guarantees pin anchors never move relative to sentence
  boundaries in a legal-citation corpus, a false positive here silently
  changes block structure around a citation.


  🛠️ Proposed tightening

  [2m     c = s[i][22m
  [2m     if c.isupper():[22m
  [2m         return True[22m
  [2m     if c in _OPEN_QUOTES:[22m
  [31m-        return True[39m
  [32m+        # look one more char past the quote for an uppercase start[39m
  [32m+        j = i + 1[39m
  [32m+        if j < n and s[j].isupper():[39m
  [32m+            return True[39m
  [32m+        return False[39m
  [2m     return False[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_cases.py:869[36m[4mscripts/s8/link_cases.py[24m[39m[2m:[22m[36m869-916[39m]8;;

  [36mmain()[39m returns 0 even when adjudicated resolutions fail to apply.

  In the [36m--apply-resolutions[39m branch, [36mres["bad_target"][39m (invalid/typo'd
  stem in the resolution file) and [36mres["stale"][39m (matched text no longer
  found near the recorded line) both represent resolutions that failed to
  apply, yet [36mmain()[39m unconditionally [36mreturn 0[39ms. A CI/orchestrator gate
  relying on this exit code will see success even though some
  human-adjudicated links were silently dropped. Same issue in the default
  [36mrun()[39m branch (line 931) — though queued ambiguity there is an expected
  outcome rather than an application failure, [36mbad_target[39m/[36mstale[39m
  specifically indicate a real error condition.

  As per path instructions, this is a "build/gate tooling for a verified
  legal-authority pipeline" where "errors must never pass silently as
  success."


  🔧 Proposed fix

  [2m     if apply_res:[22m
  [2m         idx = Index.load(index_path)[22m
  [2m         res = apply_resolutions(apply_res, idx, idx.page_stems, write=write,[22m
  [2m                                 ledger_out=ledger_out)[22m
  [2m         _print_resolution_report(res)[22m
  [2m         print("mode:", "WRITE" if write else "DRY-RUN",[22m
  [2m               "| ledger ->", os.path.relpath(ledger_out, ROOT))[22m
  [2m         if report_json:[22m
  [2m             with open(report_json, "w", encoding="utf-8") as fh:[22m
  [2m                 json.dump({k: (v if isinstance(v, (int, list)) else v)[22m
  [2m                            for k, v in res.items()[22m
  [2m                            if k in ("samples", "stale", "bad_target",[22m
  [2m                                     "base_rows", "ledger_total")},[22m
  [2m                           fh, ensure_ascii=False, indent=1)[22m
  [31m-        return 0[39m
  [32m+        return 1 if (res["bad_target"] or res["stale"]) else 0[39m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Functional Correctness][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/lint/lint7_glossary.py:73[36m[4mscripts/lint/lint7_glossary.py[24m[39m[2m:[22m[36m73-132[39m]8;;

  [36mskip_phrases[39m from term-register.v2 is never consulted by the
  coverage/banned scan.

  [36mload_register()[39m reads [36mcanonical[39m, [36mroute[39m, [36mtarget[39m, [36mmatch[39m, and
  [36mbanned_variants[39m, but drops [36mskip_phrases[39m entirely. Several `route:
  citing[36m rows (e.g. [39mvacated[36m, [39mreporter[36m in [39mterm-register.yml`) rely on
  [36mskip_phrases[39m to suppress linking for a specific sense of the surface
  (physical "vacated the room", "Washington Post reporter"). Since
  [36mcheck_file()[39m's coverage scan (Lines 253-260) has no way to see these
  exclusions, it will flag those occurrences as MEDIUM "routed term left
  unlinked" — directing authors to link text the register documents as a
  defect if linked. This is a real gap not covered by the self-test fixtures
  either.





  ♻️ Sketch fix

  [2m             rx = _bound_rx(surfaces)[22m
  [2m             if rx is not None:[22m
  [32m+                sp = term.get("skip_phrases")[39m
  [32m+                if isinstance(sp, str):[39m
  [32m+                    sp = [sp][39m
  [32m+                skip_phrases = [s.strip().lower() for s in sp[39m
  [32m+                                if isinstance(s, str) and s.strip()] if isinstance(sp, list) else [][39m
  [2m                 routed.append({[22m
  [2m                     "canonical": canonical,[22m
  [2m                     "route": route,[22m
  [2m                     "target": term.get("target"),[22m
  [2m                     "surfaces": surfaces,[22m
  [2m                     "surface_rx": rx,[22m
  [32m+                    "skip_phrases": skip_phrases,[39m
  [2m                 })[22m

  and in [36mcheck_file[39m, before emitting a coverage violation, check whether
  the matched surface sits inside one of [36mrt["skip_phrases"][39m in the
  surrounding text and [36mcontinue[39m if so.



  Also applies to: 216-261


[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_cases.py:169[36m[4mscripts/s8/link_cases.py[24m[39m[2m:[22m[36m169-182[39m]8;;

  Keep year-suffixed captions in [36mknown_re[39m
  [36mcaption_index.py[39m emits exact captions like `Mathis v. United States
  (1968)[36m and [39mUnited States v. Smith (2024)[36m in [39mlink_captions`, but the
  [36m\([^)]\)\s$[39m filter removes them from the detector. That makes those
  exact mentions invisible to auto-linking; preserve them in the alternation
  or add a bare alias first.

Writing review comments... 14m 16s elapsed - still working - 19 findings so far

[2m────────────────────────────────────────────────────────────────────────[22m
  [33mminor[39m [2m[Stability & Availability][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_cases.py:196[36m[4mscripts/s8/link_cases.py[24m[39m[2m:[22m[36m196-200[39m]8;;

  [36m_PARTY[39m is backtracking-heavy on long non-matching runs. The repeated
  alternation in [36mscripts/s8/link_cases.py:196-200[39m grows superlinearly on
  inputs like a long chain of capitalized tokens without a [36mv.[39m; tighten the
  repeated chunk or switch the generic matcher to a more linear form.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31mmajor[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_pincites.py:394[36m[4mscripts/s8/link_pincites.py[24m[39m[2m:[22m[36m394-409[39m]8;;

  Doctrine overlap-skip drops the edit with no audit trail, unlike the
  case-page pass.

  The case-page apply loop (Lines 272-275) journals [36mplain:overlap-skip[39m
  when an edit is discarded due to overlap. The doctrine apply loop's
  equivalent [36mcontinue[39m (Line 399) records nothing — the computed edit for
  that pincite silently vanishes with no ledger/journal row at all, breaking
  the audit-trail completeness this "verified" pipeline otherwise maintains.

  🩹 Proposed fix

  [2m     for p_s, p_e, repl, rid, pin_id, action, before, rule, fragment in edits:[22m
  [2m         if last is not None and p_e > last:[22m
  [32m+            journ.append(_j(rid, pin_id, "plain:overlap-skip"))[39m
  [32m+            ledger.append(_l(rid, pin_id, "plain:overlap-skip", None))[39m
  [2m             continue[22m


[2m────────────────────────────────────────────────────────────────────────[22m
  [31m[1mcritical[22m[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_pincites.py:471[36m[4mscripts/s8/link_pincites.py[24m[39m[2m:[22m[36m471-509[39m]8;;

  Critical: [36m--limit[39m doesn't gate the ledger, only the file write.

  [36mall_ledger.extend(ledger)[39m / [36mall_journ.extend(journ)[39m (Lines 495-496)
  run for every file with a validated fragment, before the [36m--limit[39m check
  (Line 504) decides whether the file is actually written. Running `--write
  --limit=N[36m will therefore persist [39mlinked-external` ledger rows (into the
  canonical [36ms8-link-ledger.rows.jsonl[39m) for files beyond [36mN[39m that were
  never actually mutated on disk — the ledger falsely claims those pincites
  are wired.

  Given this is a "verified legal-authority pipeline," a ledger row claiming
  a citation is linked when the file content was never touched is exactly
  the kind of "verified state that wasn't actually verified" the pipeline
  must avoid.


  🐛 Proposed fix

  [31m-        all_ledger.extend(ledger)[39m
  [31m-        all_journ.extend(journ)[39m
  [31m-        if new_text != text:[39m
  [31m-            changed_files += 1[39m
  [31m-            for row in ledger:[39m
  [31m-                if row["action"].startswith("linked") and len(diffs) < 10000:[39m
  [31m-                    diffs.append({"file": rel, "pin_id": row["pin_id"],[39m
  [31m-                                  "form": row.get("form"), "before": row.get("before"),[39m
  [31m-                                  "after": row.get("after")})[39m
  [31m-            if write and (limit is None or changed_files <= limit):[39m
  [31m-                with open(f, "w", encoding="utf-8") as fh:[39m
  [31m-                    fh.write(new_text)[39m
  [32m+        if new_text != text:[39m
  [32m+            within_limit = limit is None or changed_files < limit[39m
  [32m+            if write and within_limit:[39m
  [32m+                with open(f, "w", encoding="utf-8") as fh:[39m
  [32m+                    fh.write(new_text)[39m
  [32m+            elif write:[39m
  [32m+                # limit reached this run: do NOT claim these edits as applied[39m
  [32m+                for row in ledger:[39m
  [32m+                    row["action"] = "plain:limit-skipped"[39m
  [32m+                for row in journ:[39m
  [32m+                    row["action"] = "plain:limit-skipped"[39m
  [32m+            changed_files += 1[39m
  [32m+            for row in ledger:[39m
  [32m+                if row["action"].startswith("linked") and len(diffs) < 10000:[39m
  [32m+                    diffs.append({"file": rel, "pin_id": row["pin_id"],[39m
  [32m+                                  "form": row.get("form"), "before": row.get("before"),[39m
  [32m+                                  "after": row.get("after")})[39m
  [32m+        all_ledger.extend(ledger)[39m
  [32m+        all_journ.extend(journ)[39m

  Note this path isn't exercised by [36m--self-test[39m (which calls
  [36mwire_case_page[39m directly), so it would slip through CI.


[2m────────────────────────────────────────────────────────────────────────[22m
  [31m[1mcritical[22m[39m [2m[Data Integrity & Integration][22m
  [2m→[22m ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-S8-qNmSkD/scripts/s8/link_pincites.py:563[36m[4mscripts/s8/link_pincites.py[24m[39m[2m:[22m[36m563-582[39m]8;;

  Gate the pincite ledger behind [36m--write[39m
  [36mscripts/s8/link_pincites.py:576-578[39m rewrites [36mLEDGER_OUT[39m even in
  dry-run mode, so a preview can overwrite the rows that
  [36mscripts/s8/assemble_ledger.py[39m later consumes. There’s also no row field
  that distinguishes “computed” from “applied.” Gate the ledger write behind
  [36mwrite[39m, or emit dry-run rows to a separate artifact with an explicit
  applied flag.


[2m────────────────────────────────────────[22m
[38;2;215;93;44mReview complete[39m
[2m23 findings ✔[22m

[2mCritical 2[22m
[2mMajor    15[22m
[2mMinor    6[22m

[2m939 files reviewed:[22m
[2m- _overhaul2/lake/cases/Adams v. Williams.json[22m
[2m- _overhaul2/lake/cases/Aguilar v. Texas.json[22m
[2m- _overhaul2/lake/cases/Alderman v. United States.json[22m
[2m- _overhaul2/lake/cases/Arizona v. Evans.json[22m
[2m- _overhaul2/lake/cases/Arizona v. Fulminante.json[22m
[2m- _overhaul2/lake/cases/Arizona v. Hicks.json[22m
[2m- _overhaul2/lake/cases/Arizona v. Mauro.json[22m
[2m- _overhaul2/lake/cases/Ashcraft v. Tennessee.json[22m
[2m- _overhaul2/lake/cases/Ashcroft v. al-Kidd.json[22m
[2m- _overhaul2/lake/cases/Bailey v. United States.json[22m
[2m... and 929 more files[22m
[2m────────────────────────────────────────[22m

[2mPrint all AI prompts:[22m coderabbit review --show-prompts
```
