# Thread-N re-read lane unblock (post builder leg C)

Lane: `{lane: s9-thread-n-unblock, model: claude-opus-4-8}` · run 2026-07-10 · branch `overhaul2/execute`
Zero live CourtListener calls (max_calls=0 by construction on the sanctioned cache-fed surface). No commits.

## Step 1 — lake-record lead WRITE via sanctioned surface
Ran `scripts/s2/ingest.py --rekey-lead-opinion-from-cache <rid>` × 187 (all leg-C `s9_legc_done.jsonl` rids, one invocation, 374 arg tokens).

Pre-flight status survey (phase-1 aborts the whole batch on any out-of-allow status): all 187 rids resolve in `_manifest.json`, all in the permitted set — **140 `under_review` + 47 `verified_identity`**, 0 outside allow, all currently null/blank lead. No abort risk.

Result:
```
lead-opinion re-keyed (cache-served): 187 | queued-for-lane: 0 | already-harmonized: 0 | refused-needs-panel: 0
journal: /Users/johngalt/cssi-lake/journal/s2-ingest-s2-build-96d841cbb12e.jsonl
```
- **187 re-keyed, 0 queued, 0 no-op, 0 refused.** Every cluster was cache-served (leg C reported `cluster_cache_hits: 187`); surface derived each harmonized lead from the cached cluster and wrote `identity.lead_opinion_id` to the lake record + `lead_opinion_id` to the manifest row.
- No refusals. (Surface refuses at batch granularity via SystemExit on bad status; pre-flight guaranteed none.)
- Projector note emitted by surface (not run here — out of scope): `project.py --write` re-projects affected case-page `courtlistener` blocks.

## Step 2 — verification (all 187, sample printed)
Compared lake `identity.lead_opinion_id` vs leg-C `lead` and checked `/Users/johngalt/cssi-lake/cache/text/<lead>.txt`:
- **187/187 lake lead == leg-C lead. 0 mismatches. 0 missing text files.** 184 text files >1KB.
- **Olivier v. City of Brandon**: lead 11278377 (matches leg-C), text file 36255 bytes. VERIFIED.
- Sample of 10 (all OK, lead-match + text>1KB): A Quantity of Copies of Books v. Kansas (9422858, 22551B), Alasaad v. Wolf (4659025, 47976B), Alvarez v. City of Brownsville (4313442, 126335B), Anderson v. Creighton (9431119, 33049B), Arizona v. Youngblood (9431483, 23304B), Arkansas v. Sanders (9427641, 43752B), Bell v. Wolfish (9427563, 144598B), Bennis v. Michigan (9433258, 36597B), Board of County Commissioners of Bryan County (9842136, 47374B).
- **3 short (<=1KB) but present** — genuine stub-length opinions, lead still matches leg-C, file exists: State v. Demesme (4848796, 197B), chapman-v-california (8398783, 154B), o-brien-v-united-states (9423374, 559B). Flagged for machine adjudication; not blocking.

## Step 3 — surgical worklist refresh
`_run/s9/worklists/thread-n-cases.jsonl` (609 rows). Backup: `_run/s9/worklists/thread-n-cases.jsonl.pre-refresh` (609 rows, written first).

Processed only the 156 `cached_text_present=false` rows; re-derived `lead_opinion_id` from the now-updated lake record identity, set `cached_text_path` to the TEXT_DIR file when it exists, set `cached_text_present` accordingly. Left the 453 present rows byte-identical (serialization confirmed round-trip stable under `json.dumps(sort_keys=True, ensure_ascii=False)`).

- **Rows cured (now present=true): 154.**
- **Rows still no-text: 2** — `Entick v. Carrington`, `Wilkes v. Wood`. Both `verified_off_cl` English cases with no CL cluster lead (the leg-C `skipped_pre` excluded-status skips). Correctly remain present=false → lane_runner routes them to the live-CL/off-lane identity slice, never fabricates a read. Not curable from cache; no action.
- Post-refresh distribution: **607 present=true / 2 present=false** (was 453/156).
- Diff safety: exactly 154 lines changed; only `cached_text_path`, `cached_text_present`, `lead_opinion_id` ever changed; **0 preserve violations** on case_id/batch/batch_ordinal/lens_plan/tier/tier_rank/record_id/caption/cluster_id/year/court_level/citation/flags/schema; case_id order identical (609 distinct case_ids intact — done-detection keying preserved).

## Step 4 — relaunch
Confirmed no `run_thread_n.py` and no `lane_runner.py --case-read` running. The live `lane_runner.py` processes are all `--panel-review` lanes owned by `run_panel.py` **pid 27009 (left untouched, confirmed alive)**; panel worklist `panel-review.v2.jsonl` not touched.

Relaunched: `nohup python3 scripts/s9/run_thread_n.py >> _run/s9/thread-n-relaunch.out 2>&1 &` (new pid 61461, concurrency 6 default).

First log line of the fresh run:
```
[16:58:57] thread-n driver: 609 worklist rows, 812 pairs already done, 406 to run, concurrency 6
```
**to-run = 406** — matches the pre-launch simulation exactly. Of the 406: **402 land on now-present rows (real-eligible)** ≈ 154 cured × 2 lenses (308) + ~94 pre-existing present rows with an incomplete lens; **4 are the 2 residual off-CL rows × 2 lenses** (will re-emit as harmless `no_cached_text` placeholders, not counted done). Before the refresh those 154 cured rows would all have burned as placeholders.

**Real-read verification (≥3 required):** within ~2 min, 4 fresh reads landed as REAL — parse `parsed`, wall_clock_s > 30, non-null substantive conclusions (dict of disposition/holding/identity/splits/support/treatment/notes/lens), run `p1-prod`. All are newly-cured records:

```
{"record_id":"District of Columbia v. R.W.","lens":"B","wall_clock_s":60.9,"parse_status":"parsed","attempts":1,"conclusions":8-key dict,"lead_opinion_id":11312795,"cached_text_path":".../11312795.txt","at":"2026-07-10T16:59:58-04:00"}
{"record_id":"District of Columbia v. R.W.","lens":"A","wall_clock_s":101.1,"parse_status":"parsed","attempts":1,"conclusions":8-key dict,"lead_opinion_id":11312795,"cached_text_path":".../11312795.txt","at":"2026-07-10T17:00:38-04:00"}
{"record_id":"Landor v. Louisiana Dept. of Corrections","lens":"B","wall_clock_s":128.9,"parse_status":"parsed","attempts":1,"conclusions":{"disposition":"affirmed","holding":"A Spending Clause statute cannot impose personal-capacity liability...","identity":{...},...},"lead_opinion_id":11346052,"cached_text_path":".../11346052.txt","at":"2026-07-10T17:01:06-04:00"}
```
(4th: Chatrie v. United States lens B, 132.9s, parsed, 8-key conclusions, lead 11349205.)

## Net
The thread-N re-read lane is unblocked: 187 lake leads written from cache (0 live calls), 154 worklist rows cured to present=true, driver now dispatching 406 pairs (402 real), and real reads are landing with substantive conclusions. Residuals: 2 off-CL rows (Entick, Wilkes) correctly non-readable; 3 short-text stubs flagged for adjudication.
