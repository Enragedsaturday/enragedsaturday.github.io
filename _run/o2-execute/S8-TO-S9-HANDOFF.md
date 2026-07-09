# S8 → S9 Handoff — the verification session reads this FIRST

> **O2 EXECUTE · branch `overhaul2/execute` · S8 closed 2026-07-09.** S8 (linking/transclusion/
> glossary: R1–R13) is COMPLETE — acceptance 9/9 machine-evidenced (`S8-ACCEPTANCE-SWEEP.md`,
> one PASS-WITH-NOTE on R10's visual sample, deliberately re-run at S9 R15). Modelled on
> `S7-TO-S8-HANDOFF.md`. Every claim traces to an artifact. Zero live CL was used by any S8 lane.

## 0. The scoreboard S9 inherits

| Fact | Value | Pointer |
|---|---|---|
| Case-mention links live | **6,058 linked** / 82 plain:no-page / 145 plain:adjudicated | `_run/s8-link-ledger.json` by_action |
| NUM-04 re-derivation | **644 distinct captions** (595 page-backed / 49 non-page) | `s8-coh15-join.json` (join CLEAN, A/B/C/D = 0) |
| Term links (S8 lane) | **2,429** (page 1511 · glossary 444 · citing 474); register v2 125 rows + skip_phrases | `s8-term-rows.jsonl` · `scripts/lint/term-register.yml` |
| Glossary | **42 anchors**, machine-audited pure-definition | `Common Legal Terms.md` |
| External pincites | **730** (182 case-page + 548 doctrine; 225 fragment-deep) + 16 r2 deep upgrades | `s8-link-ledger.rows.jsonl` · `S8-PINCITE-JOURNAL.jsonl` |
| Lake fragments | **182 applied** (`pinpoints[].fragment`), LINT-13 0 | lake journal `s2-ingest-…jsonl` (182 rows) |
| Pin anchors | mid-line 0 · **287/287 deep links resolve** | `remediate_pins --verify` |
| Embeds | **4** (3 rule shells + 1 pin), 4/4 full-slug resolve, both flavors render | `s8-embed-rows.jsonl` |
| run_all at close | **TOTAL 4184 / HIGH 3381** (new kit) | composition fully attributed in sweep |
| Build | 724 in / 2873 emitted, exit 0 | — |

## 1. What S9 MUST review (the S8 judgment surfaces)

1. **100% of adjudicated ambiguity resolutions** (spec §8 — mandatory): 187 rows in
   `s8-adjudication-resolutions.jsonl` (42 linked / 145 plain), each with rationale + decisive
   evidence. Highest-scrutiny set flagged by the resolution lane: August-*Mendez*
   (same-caption-different-case), Tanzin-*Smith* (Employment Div. v. Smith, off-candidate),
   Walker-*Taylor*, index-*Riley*→Florida-v.-Riley, Good-Faith-*Smith*, Knock-and-Talk-*Carman*
   (folded twin).
2. **The 16 rule-2 name-half upgrades** (`[[Case|d]]`→`[[Case#^pin-N|d]]`, ledger scope:doctrine
   method rows) — incl. the Jones "legitimately on premises" short-match (verified distinctive,
   flagged for sample).
3. **≥1-in-10 ledger row sample** across `_run/s8-link-ledger.json` (14,184 mention rows).
4. **Fragment spot-checks by following sampled links** (225 fragment-deep pincites; the
   browser text-fragment highlight is the check).
5. **R10 visual sample on a FOREGROUNDED browser** (S9 R15 dogfood): flash + persistent tint +
   **centered** landing, SPA + hard-load. S8 machine-verified the tint on both paths; the
   centering animation was unobservable in the occluded automation tab (0 rAF ticks — journaled,
   not a regression; code = user-signed mockup commits).

## 2. S9 register additions (swept from the S8 run)

1. **49-caption coverage inbox** — real cases cited in prose, in no index source (tagged
   `s9-coverage-inbox` in the resolutions; e.g. Barker v. Wingo ×3, Mitchell v. Forsyth,
   Mathews v. Eldridge, Jackson v. Denno…). S9 adjudicates ingest-vs-leave-plain; 5 pedagogical
   captions (State Citations and Conventions) + 2 detector artifacts tagged distinctly.
2. **Fragment fail-closed pair**: Thornton v. United States pin-622 (lead opinion 9434613 TEXT
   ABSENT from the pool — an S2 builder-token fetch order) · United States v. Rideau pin-1576
   (duplicate passage, no star anchor — needs a star-anchored re-pin or stays plain).
3. **The 784 `mismatch`-fidelity pinpoints** (incl. whole-page harvest garbage like Adams
   pin-147) — excluded from fragments by the G3 gate; the harvest-quality class is S2/S9's to
   re-derive if fragment coverage should grow.
4. **LINT-7 register carve-out question** (30 of 49 HIGH): `inevitable-discovery` (20) +
   `pat-down` (10) banned-variant hits may be legitimate compound-modifier hyphenation —
   register-content ruling, pre-existing class.
5. **Sanctioned-quote class (R9 boundary)**: 123 shingle hits (115 para + 8 listitem) ruled
   NOT-embed (inline-woven/list quotes with R4 links); the boundary is now LINT-29's law —
   rule-node overlap ≥25t always embeds; pin overlap embeds only when re-typed as a block quote.
6. **remediate_pins check-3 baseline** is epoch-bound (271 → 287 after the sanctioned r2
   upgrades); the steady-state anchor guard is LINT-5's broken-anchor=HIGH. Do not chase.
7. **LINT-10 3171 HIGH** = the S6 case-page em-dash backlog (pre-S8, S9-owed per S7 handoff) ·
   **LINT-12 160** drift class · **LINT-4 1** = the S3-owned A7(4) master-index regen.
8. **Commit-hygiene note**: d4c87b4 (R11 sweep) swept in the mentions lane's 42 resolution
   links + its `--apply-resolutions` tooling (concurrent working tree); journal records it.
   d4c87b4's build claim was corrected in a60dd12 (dev-server race; clean rebuild verified).

## 3. Standing decisions that bind S9 (made at S8, recorded in journal/decision log)

- **Page-existence drives linking; the S6 coverage ledger's non-page terminals are the
  fail-closed keep-plain override** (the ledger is S6's candidate universe, not the page
  census; 458 mentioned page-backed captions live outside its 252 rows — the join uses both).
- **Wrong-sense links are correctness defects, not density choices** — the register
  `skip_phrases` field is the sanctioned guard (SD10 untouched: density tuning stays
  register-data-only).
- **Whole-cite wrap on case pages** (`[*Id.* at 148](url)`) + the three approved pincite forms
  (clean / id-nopage / slip-paren), ledger-categorized for sampling.
- **Eponym phrases route as terms** — register `eponym: true` rows are the machine surface the
  mention linker consults.
- Single-writer surfaces unchanged (Case Index generator — the mentions lane's Case-Index edit
  was self-caught + reverted + guarded with EXCLUDE_RELPATHS).

## 4. File pointer index

| Artifact | Path |
|---|---|
| This handoff | `_run/o2-execute/S8-TO-S9-HANDOFF.md` |
| Acceptance sweep (spec §7) | `_run/o2-execute/S8-ACCEPTANCE-SWEEP.md` |
| Canonical link ledger (R12) | `_run/s8-link-ledger.json` (+ lane rows: `.rows.mentions.jsonl` 14,183 · `.rows.jsonl` 964 · `s8-term-rows.jsonl` · `s8-embed-rows.jsonl`) |
| COH-15 join (clean) | `_run/o2-execute/s8-coh15-join.json` (regen: `scripts/s8/assemble_ledger.py --join`) |
| Adjudication queue + resolutions | `_run/o2-execute/s8-adjudication-queue.jsonl` · `s8-adjudication-resolutions.jsonl` |
| Fragments + pincite journal | `_run/o2-execute/s8-fragments.jsonl` · `S8-PINCITE-JOURNAL.jsonl` |
| Pin remediation | `_run/o2-execute/S8-PIN-REMEDIATION.jsonl` · `S8-PIN-REVIEW-QUEUE.md` (dispositioned) |
| Shingle report + embed proposals | `_run/o2-execute/s8-shingle-report.jsonl` · `S8-EMBED-PROPOSALS.md` |
| S8 tooling | `scripts/s8/` (zones · remediate_pins · caption_index · link_cases · fragments · link_pincites · link_terms · shingles · assemble_ledger + fixtures) |
| Lint kit | `scripts/lint/` (lint5 · lint7 rewritten; lint27 · lint28 · lint29 new; run_all roster) |
| Term register (v2 + skip_phrases) | `scripts/lint/term-register.yml` |
| Work orders (audit trail) | `_run/o2-execute/S8-*-WORKORDER.md` (×6) |
