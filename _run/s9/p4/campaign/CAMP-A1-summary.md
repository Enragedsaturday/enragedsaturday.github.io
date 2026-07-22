# CAMP-A1 — lint-baseline campaign packet summary

**Lane:** `{lane: CAMP-A1, model: claude-opus-4-8}` · **Branch:** overhaul2/execute
**Authority:** P4-WORKER-BRIEF.md; RULING P4-16 (a/b/c + LINT-4 rows); S1 (A8 lexicon), S2 (R2/R12/A16, `_schema.json`), S4-R10, S5-R6/R7/R13/R17, S6-R11/R12.
**Write-scope used:** `scripts/lint/lint16_casetables.py` + fixtures; `_run/s6-coverage-ledger.json`; `content/cases/Frank v. Maryland.md`, `content/cases/United States v. Trent.md`, `content/index.md` (LINT-4 pages); `_run/s9/p4/campaign/`. The 29 lake records were flipped then **reverted** (net-zero, see below).

## Deterministic coverage

| Task | Assigned | Examined | Fixed | Escalated / blocked | Skipped |
|---|---|---|---|---|---|
| P4-16(a) LINT-14 status flips | 29 records | 29 | 0 | 29 (schema/R2 blocker) | 0 |
| P4-16(c) LINT-17 ledger rows | 3 flagged + Eric-Johnson collision | 4 captions + 1 parallel | 4 rows | 1 finding (5th-Cir. Wilson) | 0 |
| P4-16(b) LINT-16 | 620 rows (619 index + 1 non-index) | 620 | 619 (carve-out) | 2 (Aug/Sandoval source; Standing FP) | 0 |
| LINT-4 rows | 4 | 4 | 4 | 0 | 0 |

## Per-lint before → after (final concurrent-tree snapshot)

| Lint | Before | After | Status |
|---|---|---|---|
| LINT-14 | 29 high | **29 high** | BLOCKED — escalated (flip conflicts with S2 R2 + `_schema.json`) |
| LINT-13 | 0 | **0** | held (verified_identity is schema-clean; `verified` would be 50 high) |
| LINT-17 | 3 high | **0** | FIXED (4 ledger rows) + self-test PASS |
| LINT-16 | 620 high | **1 high** | 619 fixed via carve-out; 1 residual (out-of-scope FP) + self-test 15/15 PASS |
| LINT-4 | 4 high | **0** | FIXED |
| LINT-12 | 5 high (pre-existing FIX-A1 set) | **5 high** | not regressed (Frank/Trent remain; strings now A8-valid) |

---

## (a) P4-16(a) — LINT-14 status flip: BLOCKED, escalated

The 29 page-backed promoted records (PROMO-FIX stage-1 list = the exact LINT-14 highs) were flipped `verified_identity -> verified` and re-projected (dry-run then `--write`; only `lake.status` changed, 29 pages). **The flip is not schema-legal and was reverted.**

- Flipping to `verified` fires committed `_overhaul2/lake/_schema.json` **allOf[1]** (`status==verified` requires `identity.party_name_in_text==true`, `identity.expected_citation_found==true`, `treatment.field_i_validity != "unverified"`).
- All 29 carry `party_name_in_text:false` + `reason_code:"two_key_not_satisfied"` + `identity_method:"pending"`; the 8 breadth-marked carry `field_i_validity:"unverified"` — which RULING P4-16(a) itself directs them to **keep**, and which `verified` categorically forbids.
- Empirical: flip -> **lint13 50 high**; revert -> **lint13 0**.
- **S2 R2 (signed spec):** "a record is `verified` only when ... the lead/combined text names the parties"; "100% of `verified` records pass the two-key." Forcing schema-legality would mean fabricating the two-key result (party-name-in-text) — banned ("no legal proposition without a verified pincite").
- P4-10 deliberately chose `verified_identity` for exactly this reason; PROMO-FIX loop-2 already flagged the class.

**Held state:** 29 records at `verified_identity` (lint13=0, schema-clean); lint14=29 is the honest gate state pending an orchestrator ruling. **Re-apply recipe** once ruled: single surgical text replace `  "status": "verified_identity",` -> `  "status": "verified",` in the 29 files (each has exactly one top-level occurrence), then `project.py --write` (projects `lake.status` only).

**Recommended remedy (spec-faithful):** the publish-gate defect is that `verified_identity` — a legitimate listed status (S2 R1 enum; the P4-14 reader-banner already models `{verified_identity, field_i unverified}`) — is absent from the R12/A16 accepted set `{verified, under_review, verified_off_cl}`. The clean fix is an **S2 A-amendment adding `verified_identity` to the publish gate + a lint14 amendment** (mirroring A16's `verified_off_cl` addition), NOT flipping identity-incomplete records to `verified`. Both are orchestrator/spec decisions outside CAMP-A1 write-scope.

## (b) P4-16(b) — LINT-16 Case-Index carve-out + real rows

**Amendment** (`scripts/lint/lint16_casetables.py`, gated strictly to `is_index_page`): the generated master Case Index (`build_case_index.py`) is a machine artifact whose Holding / Good-law / CourtListener cells are projected, not authored. Extended the F-S5-04 carve-out to (i) accept the generated 5-col header `['Case','Holding','Good law','Home page(s)','CourtListener']` (S4-R10 mandates a non-blank Good-law column), (ii) skip the section-2 authored-data-cell checks (treatment token / weight label / ISO date) on the generated page, (iii) accept the generated no-CL `—` opinion sentinel (pre-CL English cases Entick/Wilkes, page-less flagged-omit rows, the index self-row). **619 Case-Index highs -> 0.** Added pass fixture `lint-16-caseindex-generated-pass.md`; **self-test 15/15 PASS** (non-index fixtures `lint-16-historical-fail` / `lint-16-opinion-count-fail` still FAIL correctly).

Disposition of the task's "~10 REAL rows" (all on the generated Case Index):
- 610 authored-treatment-token `good`, 5 opinion-link-cardinality (`—` no-CL rows 97/150/400/494/618), 1 non-sanctioned 5-col header (18) -> **generated-artifact cells; resolved by the carve-out** (Case Index page, `build_case_index.py`, `_common.CASE_TABLE_SCHEMAS` all OUTSIDE CAMP-A1 write-scope).
- 2 `Binding in-circuit —` (461 August / 575 Sandoval) + 1 ISO date (494) -> carved at the lint; the **2 weight-label leaks are genuine SOURCE defects** in the `holding:` frontmatter of August/Sandoval. **ESCALATED** — `holding:` is author-owned/non-projected; editing it is a content/cases hand-edit outside "re-projection only". Fix per P4-16(e): edit the `holding:` frontmatter then FIN-INDEX regen.

**Residual: LINT-16 = 1** — `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:79`, `'**Historical foil.**'` (a Key-cases role-prefix) matches `_common.weight_label_in_cell`'s bare-`Historical` whole-word rule. This is a **detector false positive** (a real A8 `Historical` leak is `Historical —`/standalone, per fixture `lint-16-historical-fail`). NOT fixed: the page is neither `content/cases` nor a LINT-4 page, and `_common.py` (shared with LINT-4) is out of scope. I **declined a lint16-local permissive heuristic** because weakening a drift-killer lint is the wrong direction. Fix owed: a 1-word source reword on the Standing page OR a `_common` guard for `Historical <noun>`. (Note: the Standing page is concurrently sibling-modified.)

## (c) P4-16(c) — LINT-17 coverage-ledger terminals

Added **4 rows** to `_run/s6-coverage-ledger.json` (`ensure_ascii=False, indent=1`; counts + partition_arithmetic + folded_with_survivor updated: rows 252->256, brief-mention 61->64, folded-alias 8->9). **LINT-17 -> 0**, self-test PASS.

- **United States v. Lowers** -> `brief-mention`, cluster 10807484 (stub `united-states-v-lowers--10807484`), pointer Private and Foreign Searches.
- **United States v. Brillhart** -> `brief-mention`, cluster 10925245 (stub `united-states-v-brillhart--10925245`), pointer Private and Foreign Searches.
- **United States v. Luke Wilson** -> `folded-alias` -> survivor **United States v. Wilson** (cluster 5296785), pointer content/cases/United States v. Wilson.md. **DEVIATION flagged:** RULING P4-16(c) calls this "stub-backed", but the caption is the PAGE-BACKED 9th-Cir. United States v. Wilson (`case_name_full: "United States v. Luke Wilson"`, 13 F.4th 961) — NOT a P4 frontier stub. Fabricating a stub brief-mention was refused ("not found != fabricated"); the honest disposition is the fold. The caption appears only in the Terry Stops provenance comment (line 78).
- **United States v. Johnson** (= 4th-Cir. Eric Johnson) -> `brief-mention`, cluster 10648997 (stub `united-states-v-eric-johnson--10648997`), pointer Curtilage. **Collision noted:** the Curtilage prose writes `*United States v. Johnson*`, which previously silently allowlisted via the pre-existing `corpus_mention_baseline` row "United States v. Johnson" (cluster None, pointer content/cases/United States v. Vaneaton.md, source corpus-mention-scan) — an unrelated Johnson. The new row records the 4th-Cir. stub's own disposition.

**Finding (no row):** the **5th-Cir. Wilson stub (10636220)** caption "United States v. Wilson" on Terry Stops is the identical collision class — it silently resolves to the **authored** page-backed 9th-Cir. "United States v. Wilson" (cluster 5296785). A distinct same-caption ledger row is impossible (violates the ledger's one-row-per-caption / authored-wins invariant); the corpus manages it via distinguishing plain-text prose + the provenance comment. Recommend the orchestrator consider a first-class disambiguation home for the two Wilson cases.

**Durability note:** the ledger is a derived artifact of `_overhaul2/scripts/build_coverage_ledger.py` (out of scope). A regen from source artifacts would drop these 4 hand-added rows; recommend folding the P4-11 frontier-stub dispositions into the build source for durability.

## LINT-4 — authority-weight lexicon (S1 A8)

All 4 rows FIXED (**LINT-4 -> 0**), substance preserved, no invention:

| File:line | Before | After | Basis |
|---|---|---|---|
| Frank v. Maryland.md:13 (frontmatter) | `"Historical (formerly Binding — SCOTUS)"` | `"Historical"` | A8 tier 6 exact; annotation dropped, overrule history stays in the prose Treatment note |
| United States v. Trent.md:13 (frontmatter) | `"Persuasive only — unpublished 6th Cir. disposition"` | `"Persuasive only — non-precedential"` | A8 tier 5 exact; unpublished per curiam IS non-precedential; downgrade meaning kept |
| United States v. Trent.md:58 (prose header) | `**Persuasive only — unpublished 6th Cir. disposition**` | `**Persuasive only — non-precedential**` | same normalization |
| index.md:55 (prose) | `9th & 10th Cir. — Persuasive (outside circuit).` | `Persuasive (outside circuit) — 9th Cir. & 10th Cir.` | TEACH-04d inverted -> canonical tier-first; lane-(d) accepts the canonical prefix |

**Escalation caveat resolved (not triggered):** the A8 allowlist does NOT lack a string for the unpublished-circuit state — `Persuasive only — non-precedential` (tier 5) is the exact sanctioned tier for any non-precedential/unpublished disposition, so Trent normalizes rather than escalates.

**Projector note (finding):** `project.py::authority_weight` is court_level-only (`scotus->Binding — SCOTUS`, `coa->Binding in-circuit — Nth Cir.`); it does not model treatment downgrades (overruled -> Historical, unpublished -> non-precedential). So Frank/Trent's correct hand-authored weights legitimately differ from the projection — this is why they are the pre-existing FIX-A1 **LINT-12** escalations. Re-projecting them would REGRESS the substance; hand-editing the labels to A8-valid strings is correct. LINT-12 count unchanged (5).

---

## Concurrent-tree caveat (IMPORTANT for the orchestrator)

This session ran across ~2 days of wall-clock (2026-07-20 -> 07-22); the shared working tree accumulated **~250 concurrent sibling-lane modifications** (campaign waves A2/A3/B/C: LINT-7 glossary, LINT-11 vocab, LINT-3 case-walls, LINT-10 em-dash over 606 files; FIN-INDEX Case Index; spec/rulings/_review-needed files). **None of those are CAMP-A1's** and none were reverted. CAMP-A1's actual footprint:
- `scripts/lint/lint16_casetables.py` (+ new fixture `scripts/lint/fixtures/lint-16-caseindex-generated-pass.md`)
- `_run/s6-coverage-ledger.json`
- `content/cases/Frank v. Maryland.md` (1 line), `content/cases/United States v. Trent.md` (2 lines), `content/index.md` (1 line) — my LINT-4 edits verified intact (a sibling em-dash edit also touched index.md line 55; my TEACH-04d fix survived, lint4=0)
- `_run/s9/p4/campaign/CAMP-A1-fixes.jsonl`, `CAMP-A1-summary.md`
- 29 lake records + 29 case pages: flipped then reverted -> **net-zero from CAMP-A1** (lake confirmed clean).

## Escalations for the machine

1. **LINT-14 blocker (HIGH):** the 29 promoted records cannot be `verified` under committed `_schema.json` allOf[1] + S2 R2 without fabricating the two-key. Recommend an S2 A-amendment adding `verified_identity` to the R12/A16 publish gate + a lint14 amendment. Held at `verified_identity` (lint13=0).
2. **LINT-16 residual (1):** Standing:79 `weight_label_in_cell` false positive — needs a `_common` detector guard for `Historical <noun>` or a source reword (both out of scope).
3. **LINT-16 source defect:** August/Sandoval `holding:` frontmatter carry leaked `(Binding in-circuit — Nth Cir.)` prefixes — source fix owed (P4-16(e)), out of scope.
4. **LINT-17 Luke Wilson deviation:** dispositioned `folded-alias` (page-backed), not the ruling's "stub-backed brief-mention" — confirm.
5. **LINT-17 5th-Cir. Wilson collision:** no distinct ledger row possible (authored-caption collision); consider a disambiguation home.
6. **Ledger durability:** the 4 hand-added rows are not in `build_coverage_ledger.py` source; fold in for regen-safety.
