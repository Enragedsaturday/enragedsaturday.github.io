# PRE-W5 identity-audit + re-key report (2026-07-07)

- **Lane/model:** `{lane: s2-builder, model: claude-opus-4-8}` · Branch `overhaul2/execute`, from HEAD `f117593`. **Committed nothing** — orchestrator commits at the gate.
- **CL discipline:** single serial lane. **57 calls via ingest.py REST** (`--apply-web-keys` 0 + 22×`--readjudicate --smoke` ~2/row) + **~28 MCP cluster/search reads** (target verification). **0×429, 0×5xx.** Cache-first: all 77 pending clusters + 22 target clusters read; 77/77 pending clusters cache-served (0 CL), 2/22 targets cache-served, 20 targets fetched via MCP. Ledger `_overhaul/ledger/cl-calls.log` (delta 17785→17842). Journal step `r8.pre-w5-rekey`.
- **Method:** W4 zero-hit doctrine-term check on cached opinion text + the decisive signal — the **wiki's own `courtlistener.com/opinion/<cluster>/` links** in each home page's Sources block (the lead author's verified case choice) cross-checked against the manifest `court_era`/`sources` and each cluster's caption/cite/date via direct CL read.

---

## TASK 1 — Wholesale audit (86 rows: 77 W5–W8 pending + 9 W3/W4-skip standing-queue)

**Verdict tally: CLEAN 63 · MIS-KEY (wrong case) 20 · CITE-DUP-SWAP 2 · ESCALATE 1 · UNSURE 0.**

### W7/W8 frontier (41) — ALL CLEAN
Every W7/W8 row is a canonical SCOTUS/COA cluster whose CL `case_name` + citation + date + doctrinal home match conclusively (e.g. rochin 342 U.S. 165, timbs 586 U.S. 146, grady 575 U.S. 306, keith 407 U.S. 297, warshak 631 F.3d 266, robinson-4th-cir 846 F.3d 694 Shaquille Robinson en banc, northrup 785 F.3d 1128). The 6 already-re-keyed R1 SCOTUS rows (austin 112904, board 118104, scott 109860, owen 110236, donovan 109584, giordano 109020) confirmed correct. **No wrong-case risk; all 41 mintable (cite present).**

### W5/W6 roster (36) — 22 CLEAN · 13 re-keyed · 1 escalate
**CLEAN (22, identity already correct):** ganias(824 F.3d 199 en banc — "Border Searches" home is spurious, data note), hay(95 F.4th 1304), kolsuz(890 F.3d 133), maez(872 F.2d 1444), mendez(103 F.4th 1303, Border=77 confirmed), perez(89 F.4th 247), vasquez-algarin(821 F.3d 467), williams(435 F.3d 1148), xiang(67 F.4th 895), hanapel(112 F.4th 539), liddell(517 F.3d 1007), massenburg(654 F.3d 480), may-shaw(955 F.3d 563), mayville(955 F.3d 825), meyer(19 F.4th 1028), oliveras(96 F.4th 298), payne(99 F.4th 495), perez-rodriguez(13 F.4th 1), reddick(900 F.3d 636 — **circuit mislabel ca5, should be ca3; identity clean, data note**), young(964 F.3d 938), hunt(slip, abandoned-phone, home-matched), lewis(Edward Lewis, cite-empty, already-remapped).

**MIS-KEY re-keyed (13 of the W5/W6 set):** davis, loera, porter, trent, lee, ruckman, ruiz, wilson, mendoza, small, lyle + cite-dup swaps loines, moore-bush — see Task 2.

**ESCALATE (1): holcomb** — the wiki (Warrant Requirement) cites *United States v. Holcomb* at **132 F.4th 1118** = CL cluster **10365516** (2025-03-27, computer-search particularity), but that opinion was **WITHDRAWN** by a 9th Cir. order 2025-09-11 and marked non-citable; the frontier keyed the withdrawal-order cluster **10670143**. Orchestrator decision: (a) re-key identity to 10365516 + carry a withdrawn/non-citable treatment note, or (b) page-less mention (wiki already treats it page-less), or (c) exclude. **Not re-keyed or minted here.**

### W3/W4-skip standing queue (9) — ALL MIS-KEY, re-keyed
frederick, robinson, cole, larson, burgess, capers, castillo, chavez, crumble — see Task 2.

### NEW findings beyond the stated queue (the headline)
Six of the "known" queue rows plus two audit discoveries were **wrong-case mis-keys masked by a systematic flaw**:
- **COA-STATE's "cite-corroborated circuit corrections" were CIRCULAR.** For loera, porter, trent, ruckman (and davis via Task-3 R3-corroboration), the roster's `expected_citation` had itself been populated **from the mis-keyed cluster**, so matching it "corroborated" the wrong same-surname case. The wiki's own CL links prove the intended cases are different (loera→923 F.3d 907 not 135 F.4th 856; porter→No. 25-60163 ALPR not 142 F.4th 1140; trent→6th Cir. 2026 Mark Anthony Trent not 995 F.3d 1029 Charles Trent; ruckman→806 F.2d 1471 not 690 F. App'x 189; davis→997 F.3d 191 Howard Davis not the 8th-Cir. Justin Davis dog-sniff case).
- **lee** — frontier surname trap: cluster was "Timothy **Lee** Baker" (Lee = middle name); intended = *United States v. Lee*, 274 U.S. 559 (1927) SCOTUS searchlight case (`court_era`=1927).
- **ruiz** (task "investigate") — intended = *United States v. Ruiz*, 536 U.S. 622 (2002) SCOTUS (Brady-before-plea), not the CAAF namesake; `court_era`=2002 + Brady/Giglio home.
- **larson** (task "cite-empty + a/k/a") — actually a full wrong-case mis-key: intended = *State v. Larson*, 159 Or. App. 34, 977 P.2d 1175 (1999) curtilage, not the Iowa-2025 a/k/a cluster (`court_era`=1999).
- **loines, moore-bush** — right case but keyed to a **cite-empty duplicate cluster**; the wiki links the cite-bearing twin (loines 9357039=56 F.4th 1099; moore-bush 6476395=36 F.4th 320).

---

## TASK 2 — Re-keys (22 landed, all verified_identity + canonical_name_match=true)

Method: `--apply-web-keys _run/o2-execute/R8-PREW5-web-keys.jsonl --web-keys-allow-verified-identity` → per-row `--readjudicate <old> --smoke <old>` (scoped; NEVER `--readjudicate-file` post-mint). Identity-selection is deterministic: citation_match scores +100 (or docket_key_match +90 for cite-less slips), so the verified cite/docket lands the target. Each landed cluster verified == the wiki-linked target; 20 reset-orphan lake files removed (manifest auto-replaced the rows). **Bijection 662=662, status_counts unchanged (verified_identity 141), `ingest.py --self-test` green.**

| # | old record_id | → new record_id | cluster | verified case / cite |
|---|---|---|---|---|
| 1 | ...burgess--9495745 | burgess--172511 | 172511 | Burgess, 576 F.3d 1078 (10th Cir. 2009) |
| 2 | ...capers--5306116 | capers--180156 | 180156 | Capers, 627 F.3d 470 (2d Cir. 2010) |
| 3 | ...castillo--10322393 | castillo--9407477 | 9407477 | Castillo, 70 F.4th 894 (5th Cir. 2023) |
| 4 | ...chavez--10329331 | chavez--171034 | 171034 | Chavez, 534 F.3d 1338 (10th Cir. 2008) |
| 5 | ...crumble--4767477 | crumble--4456532 | 4456532 | Prentiss Crumble, 878 F.3d 656 (8th Cir. 2018) |
| 6 | ...lyle--8435375 | lyle--8443943 | 8443943 | Lyle, 919 F.3d 716 (2d Cir. 2019) |
| 7 | ...small--10593041 | small--4684957 | 4684957 | Dontae Small, 944 F.3d 490 (4th Cir. 2019) |
| 8 | ...cole--9623101 | cole--5307612 | 5307612 | Janhoi Cole, 21 F.4th 421 (7th Cir. 2021 en banc) |
| 9 | ...loera--10386176 | loera--4619076 | 4619076 | Loera, 923 F.3d 907 (10th Cir. 2019) |
| 10 | ...davis--10669954 | davis--4881258 | 4881258 | Howard Davis, 997 F.3d 191 (4th Cir. 2021) |
| 11 | ...porter--10626686 | porter--10810059 | 10810059 | Porter, No. 25-60163 (5th Cir. 2026) ALPR — slip |
| 12 | ...trent--4880705 | trent--10855903 | 10855903 | Mark Anthony Trent (6th Cir. 2026) — slip · **manual reconstruct** |
| 13 | ...lee--10670779 | lee--101118 | 101118 | *United States v. Lee*, 274 U.S. 559 (1927) SCOTUS |
| 14 | ...ruckman--8699562 | ruckman--480405 | 480405 | Frank William Ruckman, 806 F.2d 1471 (10th Cir. 1986) |
| 15 | ...ruiz--10650477 | ruiz--121166 | 121166 | *United States v. Ruiz*, 536 U.S. 622 (2002) SCOTUS |
| 16 | state-v-larson--10657314 | larson--1187724 | 1187724 | *State v. Larson*, 159 Or. App. 34, 977 P.2d 1175 (1999) |
| 17 | ...wilson--10664712 | wilson--5296785 | 5296785 | Luke Wilson, 13 F.4th 961 (9th Cir. 2021) |
| 18 | ...mendoza--10131439 | mendoza--10771114 | 10771114 | Ryan Mendoza, No. 25-1154 (3d Cir. 2026) — slip |
| 19 | people-v-frederick--10579458 | frederick--4396951 | 4396951 | People v. Michael Christopher Frederick (Mich. 2017) |
| 20 | robinson-v-commonwealth--10793178 | robinson--10838748 | 10838748 | Eddie Eugene Robinson v. Commonwealth (Va. Ct. App. 2026) ALPR · **slug-rename** |
| 21 | ...loines--9357144 | loines--9357039 | 9357039 | Aaron Loines, 56 F.4th 1099 (6th Cir. 2023) — cite-dup swap |
| 22 | ...moore-bush--6476396 | moore-bush--6476395 | 6476395 | Moore-Bush, 36 F.4th 320 (1st Cir. 2022 en banc) — cite-dup swap |

**Two rows needed hand-finishing (tool limitation on cite-less slips):**
- **trent**: docket 25-5770 collides on CL (readjudicate landed 10845649 "Elaine Smith v. Miami Valley Hosp."); the `case_name` rung did not surface "Mark Anthony Trent". Manually reconstructed the identity record from directly-verified cluster 10855903 (porter cite-less template). Provenance warning flags **S9 re-verify**.
- **robinson**: caption-precision retry landed the correct cluster 10838748 but under slug `eddie-eugene-...`; renamed record_id/caption back to `robinson-v-commonwealth--10838748`.

**ruiz investigation (task-requested):** RECOMMEND re-key to SCOTUS *United States v. Ruiz*, 536 U.S. 622 (2002) — the `court_era`=2002 + Brady/Giglio home + the wiki's explicit "*United States v. Ruiz*, 536 U.S. 622 (2002) (no pre-plea impeachment-disclosure duty; page-less)" prove the intent; the CAAF 2025 cluster (evidentiary, not 4th Am) was the surname trap. **Done.**

---

## TASK 3 — Deliverables + notes

- **`_run/o2-execute/R8-WORKLIST-rekey-remap-2.jsonl`** (22 rows): `old_record_id / new_record_id / new_cluster_id / cite / mintable / wave / wiki_pageless / canonical_name_match`. Lake is already re-keyed; orchestrator applies this to the signed `R8-WORKLIST.json`. All 22 `mintable:true`.
- **`_run/o2-execute/R8-PREW5-web-keys.jsonl`** (22 rows): the ready-to-apply web-keys used (kept for the audit trail / re-run).

### Escalations / data notes for the orchestrator
1. **holcomb** — withdrawn-opinion decision (above). Not re-keyed.
2. **page-vs-mention conflict** — many re-keyed + clean rows are **page-less in the wiki** (named in prose without a standalone page): burgess, capers, castillo, chavez, cole, loera, ruckman, ruiz, larson, trent, mendoza, robinson, frederick, loines (`wiki_pageless:true` in the remap). The signed worklist lists them as PAGE rows. Reconcile page vs brief-mention before minting (S7/orchestrator remit; identity is correct either way).
3. **reddick circuit mislabel** — identity clean (900 F.3d 636 = 3d Cir. Reddick private-search) but manifest `circuit=ca5`; should be **ca3**. Court-repair, not a re-key.
4. **larson cite display** — cluster 1187724 carries 977 P.2d 1175 + 159 Or. App. 34 but `official_selection.reason="same_rank_tie"` → `citations.display=null` (same class as the Weaver LEXIS quirk). Needs the state-reporter tiebreak / enrich before mint.
5. **ganias home** — "Border Searches" home is spurious (0 border hits; Ganias is over-retention/particularity). Identity correct; home is S7's call.
6. **long-lake `circuit=ca2021` bug** (I did NOT touch this code path): `long-lake-township-v-maxon--ucb0bfc28` (not_found, cluster None) carries bogus `circuit="ca2021"` + `court_level="coa"`. Root cause: `parse_circuit()` (ingest.py:549-551) has a catch-all `re.search(r"(\d+)...")` that maps ANY digit run to `ca<N>`, so a **year "2021"** became circuit "ca2021" for a Michigan **state** drone case. Fix: bound the fallback to circuit numbers 1–11 and require an ordinal/"cir" context (don't match bare 4-digit years). Out of the verified_identity scope; flagged for the S6/frontier lane.

### Readiness
- **W5/W6: 35/36 mintable** (identity + reporter cite or slip-derivable). 1 = holcomb escalate.
- **W7/W8: 41/41 mintable** (all clean, cite present).
- Bijection **662=662**, status_counts unchanged (verified_identity 141), `ingest.py --self-test` green.
