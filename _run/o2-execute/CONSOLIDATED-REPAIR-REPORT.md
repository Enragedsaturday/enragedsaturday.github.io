# R8 consolidated-repair report (2026-07-07)

Lane/model: `{lane: s2-builder, model: claude-opus-4-8}`. Branch `overhaul2/execute`, from HEAD
`e9b5cf5`. **Committed nothing** — orchestrator commits at the gate. Granted the single serial CL
lane. MCP CourtListener lane returned `unauthorized` (session not mine) → all live CL was the REST
token via `scripts/s2/ingest.py` (proven working; the packet-A/R1 mechanism) + one direct REST read.
**CL calls this session: 35. 0×429. 0 5xx.** Cache reads (0-CL): 122 (Task 2) + 5 (ground-truth).

Ledger: 4 rows appended to `_overhaul/ledger/cl-calls.log` (the live ledger; the launch note's
`_overhaul2/ledger/cl-calls.log` does not exist — logged to the real one). Journal: all row-level
terminals in pool `s2-ingest-s2-build-96d841cbb12e.jsonl`.

---

## Task 1 — R1 identity re-keys (13) — DONE, all `verified_identity`
`--apply-web-keys R8-R1-web-keys.jsonl --web-keys-allow-verified-identity` (offline, 13 rows) then
**per-record** `--readjudicate <id> --smoke <id>` (scoped). 26 CL calls (2/row). 0×429.

**Deviation from the documented batch sequence (surfaced, not improvised):** the recovery report's
`--readjudicate-file` (unscoped) build loop calls `manifest.select(None)` = all 662 records. Since
packet-A ran that form, W1 added **15 `under_review` page records** with incomplete S2 lanes
(cit/pin/prog `pending`) that route to `process_page_record` → would re-fetch cluster+lead+progeny
+treatment (~30-70 CL calls each) **and overwrite the W1-authored lake records**. I scoped each
re-key with `--smoke <id>` (frontier/identity-only path) to avoid that collateral. Same terminal,
zero blast radius.

| record_id (old→new cluster) | merits cite | canonical | court |
|---|---|---|---|
| austin-v-united-states 9140366→**112904** | 509 U.S. 602 | ✓ | scotus |
| bennis-v-michigan 9159725→**118005** | 516 U.S. 442 | ✓ | scotus |
| board-…-bryan-county-v-brown 9167020→**118104** | 520 U.S. 397 | ✓ | scotus |
| scott-v-united-states 9020551→**109860** | 436 U.S. 128 | ✓ | scotus |
| united-states-v-giordano 109022→**109020** | 416 U.S. 505 | ✓ | scotus |
| g-m-leasing-corp-v-united-states 9017014→**109579** | 429 U.S. 338 | ✓ | scotus |
| quantity-of-copies-of-books-v-kansas 107502→**106878** | 378 U.S. 205 | ✓ | scotus |
| alvarez-v-city-of-brownsville 9361139→**4536189** | 904 F.3d 382 | ✓ | coa/ca5 (en banc) |
| united-states-v-maez 7355106→**521939** | 872 F.2d 1444 | ✓ | coa/ca10 |
| owen-v-city-of-independence 8922609→**110236** | 445 U.S. 622 | ✓ | scotus |
| united-states-v-donovan 347744→**109584** | 429 U.S. 413 | ✓ | scotus |
| frank-v-maryland 793662→**105880** | 359 U.S. 360 | ✓ | scotus |
| robbins-v-california 2262192→**110558** | 453 U.S. 420 | ✓ | scotus |

All 13 landed `verified_identity`, `canonical_name_match=true`, correct court derivation. Recovery
report's mis-key diagnoses were all correct (old clusters were cert-grant/rehearing/companion/
military/state, not the merits). **13 reset-orphan pending shells removed + journaled** (packet-A
precedent; `remove_frontier_partial_record` guards on draft/blocked only, so pending shells persist).
Bijection preserved (662; renames in place).

## Task 2 — bulk `court_level` re-derive (cache-first) — DONE, SCOTUS goal met
Ground-truthed scope from the lake: **133 records** carry `court_level ∈ {None,"other"}` (all project
`authority_weight="Historical"` via `project.py`). Fed the **122 `verified_identity`** ones to
`--repair-identity-from-cache` (forced `max_calls=0`, cache-only, **0 live CL calls**). The tool
self-arbitrates via the cached cluster (U.S.-Reports reporter is SCOTUS-exclusive):

- **64 repaired** → `court_level=scotus`, `court_id=scotus`, bare-year `court` fixed (e.g. ziglar
  `"2017"`→`"U.S. Supreme Court"`), year/date_decided from cluster. `authority_weight` Historical→
  **Binding — SCOTUS**. 0 cache-misses → paced-lane fallback not needed.
- **58 queued-for-lane** (41 coa + 17 state): tool refuses to guess circuit/state.

**Re-scan result: 0 verified_identity records with a U.S.-Reports cite still project "Historical."**
Task goal met. Journaled per row (`r8.identity-repair`).

Edge cases (SCOTUS-nominal but NOT clean merits, correctly left untouched):
- **zorn-v-linton--10813527** — SCOTUS per curiam (607 U.S. ___, No. 25-297) but CL cluster 10813527
  is **known-corrupt** (contains *Strike 3 Holdings* text; S9-ADJ). No U.S. cite → queued "state".
  Not a minted page. Escalate: needs off-CL identity or corrected cluster.
- **chapman-v-california--8428427** — cluster cite `137 S. Ct. 389` (2016) ≠ the *Chapman* merits
  (386 U.S. 18, 1967); a mis-keyed cert/orders cluster. Already packet-B **EXCLUDE-remit**. Not a page.

**Remaining scope (finding #2, orchestrator decision):** 41 coa + 17 state records still
`court_level="other"` → project "Historical". `--repair-identity-from-cache` can't fix them (needs
circuit/state derivation). Fix path: extend the repair tool for coa (map cluster `court`→circuit) OR
per-record readjudicate through the paced lane (R1 machinery correctly sets coa+circuit — see the 4
R3-esc re-keys below, which cleared 4 of these). Full queued list is in the journal.

## Task 3 — R3 escalations (black/young/williams/lewis) — ALL RESOLVED (re-keyed)
Ground-truthed the 4 current clusters from the **HTTP cache (0-CL)**: **all four are 2025 same-surname
cases** (young 2025-10-02, williams 2025-09-12, lewis Raymond-Lewis 2025-07-24, black Eural-Black
2025-03-12), but the roster `court_era` says 2020/2006/2023/2013. **Same frontier mis-key class:** the
roster `year` field was unset → no year filter → the search grabbed a recent same-surname case.
`canonical_name_match=true` was a false surname-only match. Dual-leg web-verified the intended cases
(zero-CL; each matches its doctrine home), then re-keyed via `--apply-web-keys R8-R3ESC-web-keys.jsonl`
+ per-record `--smoke` readjudicate (8 CL calls). This **resolves** the recovery report's
"ambiguous" escalations for young/williams (recovery report assessed young against 4A, but its home is
*Due-Process Voluntariness of Confessions*) and the Edward-vs-Raymond Lewis question (Edward is right).

| record (old→new cluster) | case (verified) | cite | home |
|---|---|---|---|
| black 10355347→**821235** | US v. **Nathaniel** Black (Terry/RS; reversed) | 707 F.3d 531 (4th Cir. 2013) | Terry Stops |
| young 10687648→**4766220** | US v. **Shane** Young (voluntariness; FBI false-judge deception) | 964 F.3d 938 (10th Cir. 2020) | Due-Process Voluntariness |
| williams 10670874→**793121** | US v. **Tashiri Wayne** Williams (Miranda two-step/*Seibert*) | 435 F.3d 1148 (9th Cir. 2006) | Miranda Waiver/Invocation |
| lewis 10640348→**9424185** | US v. **Edward Leonidas** Lewis (consent scope; reversed) | (CL cluster cite-empty) | Consent Searches |

All 4 `canonical_name_match=true`; `court_level` other→coa+circuit (Historical→Binding-in-circuit;
cleared 4 of the coa residue). 4 reset-orphans removed+journaled. Bijection 662. **lewis** lands
correct identity but CL cluster 9424185 carries no reporter cite → `citations-empty` (enrich via R3
web-cite, or slip-mint) — dual-leg web legs: FindLaw + Justia, panel Moore/Clay/Gibbons, docket
22-5593/5800, 2023-09-01. black/young/williams are re-key gates: `_run/o2-execute/R8-R3ESC-web-keys.jsonl`.

## Task 4 — CR-13 / CR-14 (`scripts/s2/project.py`) — DONE, self-tested, green
- **CR-13** `date_from_record`: today() fallback → **fail-closed** `ValueError` (missing/short
  `provenance.date_modified`). Verified all 662 lake records carry a valid `date_modified` first
  (dormant, no live break). Removed now-unused `import datetime as dt`.
- **CR-14** `dry_run_or_write`: **pre-validate `project_record()` for every matched record before any
  write** (mirrors the a13 gate's accumulate-then-refuse). A record that raises (bad/absent COA
  circuit, or CR-13 missing-date) now blocks the whole batch cleanly with `projection_errors` +
  exit-2, instead of crashing mid-`os.replace` loop with earlier pages already rewritten.
  `projection_errors` threaded through all return paths + `print_summary`.
- Regression tests added to `self_test()`: CR-13 (missing + short date raise; valid passes) and CR-14
  (bad-circuit batch refuses, `projection_errors` len 1, and the sibling good page is byte-unchanged =
  no partial write).

Results: `project.py --self-test` **9/9 OK** · `--verify-idempotent` **PASS** (0/0 changes) ·
full-corpus dry-run clean (473 new-form pages, 0 projection_errors, no false refusal) ·
`scripts/s6/mint_page.py --self-test` **PASS (37/37)** (imports `project_record`; unaffected).

## Task 5 — Gutierrez v. Saenz text — FOUND (W1 was MCP-blind, not textless)
Cluster 10776824 (606 U.S. 305, 2025-06-26) has ONE sub_opinion, **11243411**. W1's MCP
`read_document`/`search_document` read `html_with_citations` (len=0) → "no text". But the **`plain_text`
field is fully populated: 117,531 chars**, `type=010combined`, `page_count=54`, `extracted_by_ocr=false`
= the official U.S. Reports **preliminary print**, Vol 606 Part 1, pp. 305-356.
- **W9 method:** source the holding from opinion **11243411 `plain_text`** via REST `opinions/11243411/`
  (now cached into the ingest HTTP cache → future 0-CL), **NOT** `html_with_citations`.
- Held (syllabus, verbatim): *"Gutierrez has standing to bring his §1983 claim challenging Texas's
  postconviction DNA testing procedures under the Due Process Clause. Pp. 314-321."* Sotomayor, J.;
  disposition *"93 F.4th 267, reversed and remanded."* Star-paginated via 25 "Cite as: 606 U. S. NNN"
  markers → pincites map to real U.S. Reports pages. 1 CL call.

---

## Mintable count for W2 (reads straight off this)
148 worklist pages − 15 minted (W1) = **133 remaining.** Categorized against the current lake:

- **NEW MINTABLE = 122** (verified identity + pinnable citation, not yet minted). Includes the newly
  cleared: egbert (596 U.S. 482, repaired), gutierrez (text path found), R.W. (608 U.S. ___ slip),
  black/young/williams (re-keyed w/ cites), the 13 R1 re-keys, all 64 court_level-repaired SCOTUS.
- **11 still blocked** (`verified_identity`, citations-empty / R3 slip-only — need web-cite recovery
  or a slip/off-CL mint decision): Carter, Robinson (Commonwealth), State v. Larson, US v. Davis,
  Holcomb, Hunt, Lee, **Lewis (Edward — now correct identity)**, Mendoza, Ruiz, Zorn.
- 122 + 11 = 133 ✓

**W2 PREREQUISITE (blocking for 17 rows):** this session re-keyed 17 worklist page rows (13 R1 + 4
R3-esc); their signed-worklist `record_id`s are now **stale** (old ids removed). `mint_page.py`
`worklist_row()` + `lake_record_path()` match by **exact** record_id → W2 would `REFUSE_NO_LAKE_RECORD`.
Writer≠checker: I did **not** mutate the signed `R8-WORKLIST.json`. Ready-to-apply remap delivered:
`_run/o2-execute/R8-WORKLIST-rekey-remap.jsonl` (17 old→new `record_id`+`cluster_id`; 16 of the 122
mintable + lewis). Orchestrator applies at the gate. Until then, 106 of the 122 are dispatchable as-is.

## Integrity / escalations
- Bijection **662 manifest ↔ 662 lake files**, no dup ids, no orphan/missing files. status_counts
  stable (v_id 180, verified 421, under_review 50, off_cl 2, not_found 4, folded 3, fab 2).
- LINT-13 schema: **0 violations** over the full lake (self-test PASS). Re-keyed + repaired records
  schema-clean.
- **Escalations for the orchestrator:** (1) worklist remap (above, ready-to-apply). (2) 41 coa + 17
  state `court_level="other"` residue still project "Historical" — needs coa/state derivation. (3)
  zorn cluster 10813527 corrupt + chapman 8428427 mis-key (both not live pages). (4) lewis (Edward)
  citations-empty. (5) MCP CourtListener lane is unauthorized in this environment — the REST token via
  ingest.py is the only working CL path; wave lanes using MCP `read_document` will hit the same
  `html_with_citations`-empty blind spot as W1 hit on Gutierrez (recommend a plain_text fallback).

## Files (UNCOMMITTED)
- Code: `scripts/s2/project.py` (CR-13/14 + self-tests).
- Lake: 64 court_level-repaired records + 17 re-keyed records (new) − 17 orphans (deleted) +
  `_manifest.json` (counts regenerated, 662).
- Deliverables: `R8-R3ESC-web-keys.jsonl` (re-key gate, applied), `R8-WORKLIST-rekey-remap.jsonl`
  (ready-to-apply), this report.
- Ledger: 4 rows in `_overhaul/ledger/cl-calls.log`. Journal: `r8.identity-repair` (64 repaired + 58
  queued), `packet-a.web-keys`/`adjudication`/frontier rows (17 re-keys), `s6-queue-correction` (2
  orphan-removal batches: 13 + 4).
