# S6 CLOSE-OUT — coverage ledger (R11) + LINT-17 (R12)

Lane/model: `{lane: s6-coverage-ledger, model: claude-opus-4-8}`. Branch
`overhaul2/execute`, from HEAD `164f34e`. **Committed nothing** — orchestrator
commits at the gate. Zero CL calls (offline assembly + lint only).

Deliverables:
- `_run/s6-coverage-ledger.json` (R11) — programmatically assembled + machine-checked
- `_overhaul2/scripts/build_coverage_ledger.py` — the reproducible assembler
- `scripts/lint/lint17_coverage.py` (R12/LINT-17) + fixtures + run_all registration

---

## 1. Coverage ledger (R11) — partition proof

`build_coverage_ledger.py` assembles the ledger from the signed disposition
artifacts + the S2 lake manifest (the authoritative reconciliation base: 662
records = 604 page-backed + 58 page-less stubs). One row per distinct caption in
the **S6 candidate universe**, each with exactly one terminal state.

**Candidate-universe partition (`rows`, machine-checked, RESULT: PASS):**

| terminal | rows |
|---|---|
| authored | 145 |
| brief-mention | 55 |
| excluded-remit | 26 |
| folded-alias | 8 |
| watch | 3 |
| removed | 2 |
| unverifiable | 1 |
| **TOTAL** | **240** |

`authored 145 + brief-mention 55 + excluded-remit 26 + folded-alias 8 + watch 3 + removed 2 + unverifiable 1 = 240 distinct captions`

Machine checks (all green):
- **authored (145):** page file present **145/145**, lake record present **145/145**,
  manifest rename present **145/145**.
- **folded-alias (8):** every row names an existing survivor **8/8** (davis→Howard
  Davis · morse→French v. Merrill · carman→Carroll v. Carman · chatrie→Chatrie v.
  United States · alasaad-mayorkas→Alasaad v. Wolf · lombardo-stl→Lombardo v. City
  of St. Louis · king-brownback→Brownback v. King · villarreal-laredo→Villarreal v.
  Alaniz).
- **partition:** every caption exactly one terminal; **0 conflicts, 0 row-errors**.
  (The one live conflict — Villarreal v. City of Laredo, gated EXCLUDE vs packet-B
  fold — is resolved in favor of the packet-B panel, which supersedes the writer gate.)

**148-worklist reconciliation:** the R8 worklist's 148 page-rows re-derive exactly
= authored 145 + davis (folded-alias) 1 + holcomb (watch) 1 + zorn (unverifiable) 1.
The remaining 92 candidate-universe rows are the 58 R8-NONPAGE placements + 19 gated
EXCLUDE (dedup) + packet-B excludes + escalation terminals.

Terminal sources (all read-only, reproducible): `s6-authored-ledger.jsonl` (145) ·
`davis-fold.jsonl` + `packet-a-alias-folds.jsonl` (folds) · `s6-removals.jsonl` ·
`R8-NONPAGE-LEDGER.json` (noted-orders/mentions/escalations) · `gated.jsonl`
(EXCLUDE) · `packetb-dispositions.jsonl` · manifest stub statuses + W9 terminal
overrides (holcomb/zorn, davis-precedent in-row override, lake untouched).

Every row carries the R11 schema: `{caption, canonical, cluster_id|null, leg,
gate:{verdict,prong,rationale}, keys:{cl,independent}, terminal, pointer}`
(+ `page_backed`, `source`, and `survivor` on folds). Schema completeness verified
240/240.

## 2. NUM-04 (388-mention) reconciliation — status

**Reported honestly, not fabricated.** NUM-04's "388 distinct bare-mention
captions" is a **measured S8 input** (audit intake; 40/40 sample, ≥365 floor). It
does **not** exist as a machine artifact anywhere in the `coverage/` or `_run/`
trees (searched: no mention-universe file). Per R11 the 388 is a *ledger property*,
not a prose claim, so the ledger is built to be the join surface rather than
re-deriving a number that has no artifact:

- Every ledger row carries `page_backed` + `pointer`, so S8 can **link every
  mention whose caption has a page** (145 S6-authored + all pre-existing pages the
  caption resolves to) and **apply its own rule (opinion-link/plain) to the rest**.
- "The rest" (page-less bare mentions) is enumerated in a **frozen
  `corpus_mention_baseline`** section (§3) so S8 has the machine list; it is
  labeled explicitly as **LINT-17's own current-corpus scan, NOT the NUM-04 388**.

No 388-vs-ledger arithmetic is asserted, because the 388 has no machine artifact to
reconcile against — doing so would be numbers-by-assertion. S8 owns the final 388
join reading this ledger.

## 3. LINT-17 (R12) — coverage lint

`scripts/lint/lint17_coverage.py` (fail-closed HIGH). A prose party-v-party caption
that resolves to **no page** fails the build **unless** the coverage ledger records
a non-page terminal state for it. Resolution tiers: (1) `CorpusIndex.resolve` or a
token-subsequence page-title variant match (collapses official-long-form /
comma-company-fragment / trailing-token extraction artifacts to their page, without
substring false-cover — "United States v. White" is *not* covered by a "…Whitehead"
page); (2) the frozen ledger allowlist (non-authored `rows` + `corpus_mention_baseline`);
else (3) HIGH.

The allowlist is a **frozen snapshot** committed by the assembler, not regenerated
by the lint — so a NEW bare caption grown after S6 close is not self-allowlisted and
fails CI until it earns a page or a ledger disposition (the R12 class-2 defense).

**Self-test (9/9 PASS):** exact resolve · variant company-fragment · variant
trailing-overrun · ledger-allowlisted · **new-bare-caption fails** · no-substring-
false-cover · fold-not-covered-by-survivor · fixture-fail-has-missing ·
fixture-pass-no-missing. Wired into `run_all.py` LINTS + SELF_TESTS (fail-closed
gate), roster docstring updated. Fixtures: `fixtures/lint-17-fail.md` (synthetic
`Zzyzx v. Nowhere` → HIGH, exit 1) · `fixtures/lint-17-pass.md` (page-resolvable →
exit 0).

**Corpus-wide run: 0 violations, exit 0** (734 distinct party-v-party captions
scanned; allowlist 95 candidate-universe non-page + 58 baseline). `run_all.py`
confirms LINT-17 = 0 total / 0 high and the self-test gate emits 0 synthetic HIGH.
No content/ or quartz/ files were touched, so the `npx quartz build` surface is
unchanged from HEAD (W9 verified green).

## 4. corpus_mention_baseline — the honest residual (58)

Before the baseline, **58 real page-less captions** failed resolution. Triaged (no
silent special-casing):

- **5 = documented manifest exclusions** (`citation_format_placeholders`): Smith v.
  Jones, State v. Randolph, State v. Smith, Stern v. Florida, Stern v. State — all
  in `Reading and Citing Cases.md` as citation-FORMAT teaching examples, not
  authorities. Recorded `excluded-remit` (verdict `citation-format-placeholder`)
  from the signed manifest exclusion.
- **53 = legacy antecedent/companion bare-mentions** in *pre-S6* case-page prose
  (Barker v. Wingo, United States v. Rabinowitz, Oregon v. Hass, Bell v. Hood,
  Jackson v. Denno, Twining/Adamson, Colonnade Catering, Anderson v. Creighton,
  Bell v. Wolfish, …). These were **never in an S6 candidate leg** — they are the
  NUM-04 bare-mention residue R11 assigns to S8's plain-link rule. Recorded
  `brief-mention` (verdict `not-adjudicated (S8 plain-link)`) with the mention-site
  pointer. Freezing them keeps CI green **and** keeps the regression guard live.

**Escalations (3) — surfaced, NOT adjudicated (writer≠checker):** three page-less
captions clear the R2 field-relevance gate on their face and are D1-flip page
candidates the orchestrator/S9 should adjudicate:
- **Anderson v. Creighton** (QI clearly-established standard; `White v. Pauly.md`)
- **Bell v. Wolfish** (jail search reasonableness; `Florence v. County of Burlington.md`)
- **Colonnade Catering Corp. v. United States** (closely-regulated-industry
  administrative search; `United States v. Biswell.md`)

They are allowlisted `brief-mention` (they *are* currently bare mentions — true and
build-safe) with an `escalate` flag so they are not buried. The wider 53-row class
is likewise available for an S8/S9 sweep if the D1 flip is applied beyond the S6
candidate legs.

## 5. Carried-forward data findings (not mine to fix; writer≠checker)

From the W9 report §6, unchanged and re-flagged for the S9/repair lane: capers lake
`identity.docket` 09-2101 vs CL 07-1830-cr; castillo lake 22-50060 vs CL 21-50406;
capers/chavez best-effort star pincites to confirm. These are lake-field repairs,
not ledger/lint issues.

## 6. Files

- `_run/s6-coverage-ledger.json` — 240 candidate-universe rows + 58 baseline (298
  distinct captions), partition proof + counts embedded.
- `_overhaul2/scripts/build_coverage_ledger.py` — reproducible assembler (`--write`).
- `scripts/lint/lint17_coverage.py` — LINT-17.
- `scripts/lint/fixtures/lint-17-fail.md`, `lint-17-pass.md`.
- `scripts/lint/run_all.py` — LINT-17 registered (LINTS + SELF_TESTS + docstring).
