# CAMP-TRENT summary — RULING P4-20(a): Trent projector gap closed

Lane/model: CAMP-TRENT / claude-opus-4-8. Branch `overhaul2/execute`.
Authority: `_run/s9/p4/P4-RULINGS.md` RULING P4-20(a). Gap analysis:
`_run/s9/p4/campaign/CAMP-L12-summary.md` disposition 6 (Trent, the 1 residual LINT-12 RED,
`needs_orchestrator:true`). Writer != checker: outputs returned for machine adjudication.

WRITE-SCOPE honored exactly: `_overhaul2/lake/_schema.json`,
`_overhaul2/lake/cases/United States v. Trent.json`, `scripts/s2/project.py`,
`scripts/lint/fixtures/` (new fixture pair), `content/cases/United States v. Trent.md`
(re-projection only), `_run/s9/p4/campaign/`.

## Result: LINT-12 content-wide 1 -> 0 highs ; LINT-13 stays 0 ; all self-tests green

The unpublished/non-precedential fact is now an identity-grade signal the projector honors,
so Trent's authoritative page value (`Persuasive only — non-precedential`) and the projected
value CONVERGE — no drift, no page regression.

| Baseline | After |
|---|---|
| LINT-12 = 1 high (Trent) | **0 highs corpus-wide** |
| LINT-13 = 0 | 0 (672 records; only Trent carries the new field) |
| LINT-4 = 0 | 0 (page + corpus; A8 allowlist unchanged) |
| project.py --verify-idempotent | PASS |

## What P4-20(a) required, and what was done (5 coordinated edits)

**(1) Schema — OPTIONAL `identity.precedential_status`.** Added to the `identity` definition
(NOT in `identity.required`), `type: string`, enum = CL's precedential_status vocabulary
(`Published, Unpublished, Errata, Separate, In-chambers, Relating-to, Unknown`), with a
description tying it to this ruling. Optional => the 671 pre-P4-20 records with no such field
stay valid; only Trent carries it. No new JSON-Schema keyword introduced (enum/type already in
lint13's supported set), so lint13 keyword coverage is unchanged. **LINT-13 corpus = 0.**

**(2) Trent lake record.** `identity.precedential_status: "Unpublished"` (placed after
`court_level`, mirroring the schema). Added a `provenance.warnings` entry citing the P4
marker-poll evidence: CL cluster **10855903**, precedential_status **Unpublished**, polled
**2026-07-20** (`_run/s9/p4/marker-poll-p4.jsonl`, marker `trent-unpublished-6th`: citations=[],
date_modified 2026-05-07 unchanged). Bumped `provenance.date_modified`
`2026-07-10T20:54:54Z -> 2026-07-22T05:44:21Z` to honestly reflect this edit (the projector
derives `lake.projected_at` from this field).

**(3) `scripts/s2/project.py::authority_weight()`.** Read the function first, then added ONE
scoped guard at the top:

    if level in ("coa", "district") and identity.get("precedential_status") == "Unpublished":
        return "Persuasive only — non-precedential"

Minimal, and every other path is byte-identical: scotus/state/other/coa-published unchanged;
district already returned the same tier-5 string, so its behavior is unchanged too. An absent
signal (all other records) changes nothing corpus-wide. The returned string is byte-identical to
the A8 allowlist member (`scripts/lint/_common.py::WEIGHT_EXACT_LABELS`, U+2014 em-dash) and to
the value CAMP-A1 normalized onto Trent's page.

**(4) Re-projection.** Dry-run after the fix: `field_counts = {courtlistener.opinion_id: 1,
lake.projected_at: 1}` — `authority_weight` no longer drifts (projector now derives the page's
own value). `project.py --write "content/cases/United States v. Trent.md"` then swept the two
stale mechanical fields: `opinion_id null -> 11323299`, `projected_at 2026-07-07 -> 2026-07-22`.
Re-dry-run: `pages_changed = 0` (idempotent). Frontmatter-only diff; no prose, holding, or
treatment touched; the `authority_weight` string is unchanged on disk (it was already correct —
the fix made the projector AGREE, it did not rewrite the page value).

**(5) Fixture + self-tests.**
- `scripts/lint/fixtures/lint-13-record-precedential-status-pass.json` — coa/Unpublished record
  (mirrors Trent's shape) — validates clean (0 viol).
- `scripts/lint/fixtures/lint-13-record-precedential-status-fail.json` — invalid enum value
  `Depublished` — fails closed with exactly ONE violation, precisely on
  `$.identity.precedential_status` (proves the enum constrains the field).
- `project.py::self_test` — new P4-20(a) block asserts coa/Unpublished -> tier-5,
  coa/published -> `Binding in-circuit — 6th Cir.` (regression: absent signal unchanged),
  district -> tier-5, scotus+stray-flag -> `Binding — SCOTUS` (guard scoped to coa/district).

## Verification log

- `project.py --self-test` -> exit 0 (new line: `P4-20(a) precedential_status weight derivation
  -> OK (coa/unpub='Persuasive only — non-precedential' coa/pub='Binding in-circuit — 6th Cir.')`).
- `lint13 --self-test` -> exit 0; `lint-13-record-precedential-status-pass.json` 0 viol,
  `...-fail.json` 1 viol (enum). `lint12 --self-test` -> PASS. `lint4 --self-test` -> 0 viol.
- Corpus: `lint12_drift.py` = 0 highs; `lint13_schema.py` = 0; `lint4_lexicon.py` = 0.
- Page collateral (Trent): LINT-6 / LINT-16 / LINT-23 / LINT-26 = 0 each. LINT-1 is
  write-only/serial-CL-gate (not run — correct; no CourtListener calls made this lane).
- `project.py --verify-idempotent` -> PASS (corpus-wide double-project, second run 0 changes).

## Coverage (deterministic)

Assigned: 1 residual (Trent, CAMP-L12 assertion `ed2ab1579af4a974`). Resolved: 1
(FIXED via projector-derivation enhancement — the clean path CAMP-L12 identified as the only one
that yields LINT-12=0 content-wide without a carve-out). No adjudication performed (writer !=
checker); the fact basis is the sanctioned P4 marker-poll, not a fresh CL call.

## Footprint / scope hygiene

- Edited: `_overhaul2/lake/_schema.json`, `_overhaul2/lake/cases/United States v. Trent.json`,
  `scripts/s2/project.py`, and via `project.py --write` (frontmatter only)
  `content/cases/United States v. Trent.md`.
- Added: `scripts/lint/fixtures/lint-13-record-precedential-status-{pass,fail}.json`.
- Did NOT touch: any other lake record, any other content page, `_common.py`, `serializer.py`,
  the registry, or any ledger. No CourtListener calls (lake + marker-poll evidence only). No
  staging/commit. Many concurrent sibling-lane writes exist in the shared tree and were left
  untouched.

## Note for the orchestrator

RULING P4-20(a) is executed in full; the `needs_orchestrator:true` residual from CAMP-L12 is
discharged. P4-20(b)'s latent S1 §3.1 vs S2 SD9 conflict is untouched by design — this lane did
NOT implement any overruled -> Historical downgrade; weight labels still derive from court level
(plus, now, the non-precedential signal), and overruled/abrogated status stays in
`field_i_validity` + treatment badges + Historical prose, per the built convention. That spec
clarification remains the P5 handoff item P4-20(b) filed.

## Outputs
- `_run/s9/p4/campaign/CAMP-TRENT-fixes.jsonl` — 5 rows (camp.fix.v1).
- `_run/s9/p4/campaign/CAMP-TRENT-summary.md` — this file.
