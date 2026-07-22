# CAMP-L12 summary — LINT-12 residual set (5 highs + 1 code defect)

Lane/model: CAMP-L12 / claude-opus-4-8. Branch `overhaul2/execute`.
WRITE-SCOPE: `scripts/lint/_common.py`, `scripts/s2/serializer.py` (+ self-test),
`_overhaul2/lake/cases/` (4 named records), affected content pages (re-projection only),
`_run/s9/p4/campaign/`. Writer != checker: outputs returned for machine adjudication.

Input: `FIX-A1-escalations.jsonl` (6 rows). Live LINT-12 at packet start = **5 highs**
(Roberson, Sanders, Frank, Kalkines, Trent); Gouled had already been reconciled to green by a
sibling lane (lake `varies_by_point` now `False`). Deterministic 6/6 dispositions below.

## Result: LINT-12 5 -> 1 ; LINT-13 stays 0 ; all self-tests green (2x deterministic)

| # | Row | Disposition | LINT-12 |
|---|---|---|---|
| 1 | Arizona v. Roberson (code) | FIXED — serializer round-trip | GREEN |
| 2 | Arkansas v. Sanders | FIXED — re-projected to convention | GREEN |
| 3 | Frank v. Maryland | FIXED — re-projected to convention | GREEN |
| 4 | Kalkines v. United States | FIXED — lake taxonomy + re-project | GREEN |
| 5 | Gouled v. United States | ALREADY-RESOLVED (sibling lane) | GREEN |
| 6 | United States v. Trent | NOT-FIXED (out-of-scope projector gap) | RED (1) |

Final live LINT-12 = **1 high (Trent only)**; LINT-13 = 0; `project.py --verify-idempotent` PASS;
serializer / project.py / lint12 / lint13 self-tests PASS.

## (1) Serializer round-trip code defect — Roberson (FIXED)

Root cause (studied both sides): `serializer.yaml_scalar` quotes managed strings via
`json.dumps`, writing a literal `"` as `\"`; the reader `_common._unquote` stripped only the
surrounding quotes and never unescaped `\"`. Any managed string with a literal double-quote (the
Roberson `scope_note` `("R15 treatment audit required")`) could never round-trip to equality — a
LINT-12 false positive AND a `project.py` idempotence failure (latent, not introduced by FIX-A1).

Fix (both in `scripts/lint/_common.py`):
- `_unquote`: for a double-quoted scalar, reverse the serializer's escaping **exactly** with
  `json.loads` (bare-strip fallback for hand-authored non-JSON double-quoted values).
- `_strip_inline_comment`: skip a backslash-escaped char inside `"..."` so an escaped quote no
  longer flips quote-state and wrongly exposes a later `#` as an inline comment (needed for the
  full quote+hash round-trip).
- `scripts/s2/serializer.py::self_test`: added a round-trip probe set (embedded quote; quote +
  hash + backslash; plain) plus a `diff_paths` value-idempotence assert.

Verified: Roberson LINT-12 GREEN; `--verify-idempotent` PASS; no content edit owed (page value
was already correct on disk). No corpus regression (LINT-12 5 -> 4 immediately after the code fix,
zero new reds; `json.loads` differs from a bare strip only when backslash escapes are present, and
in a managed scalar those come only from serializer output that should be unescaped).

## (2) Four substance rows — evidence-led; lake and page made to agree

**Convention finding (decisive).** `authority_weight` is DERIVED from `court_level` only
(S2 SD9; `project.py::authority_weight()` reads no stored weight field, no override, no
published/precedential flag — confirmed by grep across project/ingest/authority_db and the lake
schema). LINT-12 therefore compares page-parsed vs **projected-DERIVED** (not lake-stored). The
corpus's overruled/abrogated SCOTUS cases — Olmstead & Gouled (S1 A4 `overruled` list) and Aguilar
& Spinelli (`abrogated`) — ALL carry page `Binding — SCOTUS` and are LINT-12 green; the overruled
signal lives in `treatment.field_i_validity` (`superseded`), NOT in `authority_weight`. That is the
operative, lint-enforced convention.

- **Sanders + Frank (overruled-SCOTUS) — FIXED by re-projection, no lake edit.** Both are frontier
  stubs (`status: under_review`, `field_i_validity: unverified`, scope_note "treatment/progeny
  intentionally not derived until S6 promotion"). Their lake records were ALREADY convention-
  compliant (`court_level: scotus`, no stored weight — identical to the four exemplars); only the
  PAGE carried a premature hand-set `Historical` (CAMP-A1 had merely A8-normalized the label
  string, not adjudicated the tier). The S1 A4/§3.1 `overruled -> tier-6 (Historical)` downgrade
  applies only once the overruled treatment is DERIVED (S6 promotion) and is not projector-
  implementable under the court_level-only derivation. Re-projected each page to the convergent,
  exemplar-consistent `Binding — SCOTUS` (also swept the stale `opinion_id` null->id and
  `projected_at`). LINT-12 GREEN. Frontmatter-only diffs; no prose touched.

- **Kalkines (Court-of-Claims taxonomy) — FIXED by lake edit + re-project.** Cached opinion
  `8594616` confirms the U.S. Court of Claims delivered the opinion (473 F.2d 1391, Ct. Cl. 1973 —
  the "Kalkines warning"), the Federal Circuit predecessor whose precedent the Fed. Cir. adopted as
  binding (South Corp. v. United States, per the record's own scope_note). Page hand-set
  `Binding in-circuit — Fed. Cir.` was MORE correct than the lake's `other -> Historical` fall-
  through. Edited the lake identity `court_level: other -> coa`, `circuit: null -> "fed"` (court
  name `U.S. Court of Claims` + `court_id: cc` preserved; schema `court_level` enum admits `coa`,
  `circuit` is a free string), so the R10 derivation yields the page's accurate
  `Binding in-circuit — Fed. Cir.`. Re-projected the page (`court_level other->coa`, `circuit
  ''->fed`; authority_weight now matches). LINT-13 = 0; lint1/4/6/21/23 clean on the page.
  LINT-12 GREEN.

- **Trent (unpublished 6th Cir.) — NOT FIXABLE in write-scope; precise lint-semantics note.**
  The page value `Persuasive only — non-precedential` is authoritative (Wave-B unpublished
  downgrade, P4 marker-poll reconfirmed, CAMP-A1 A8-normalized) and must NOT be re-projected —
  doing so REGRESSES it to `Binding in-circuit — 6th Cir.`. LINT-12 compares page vs court_level-
  DERIVED, and tier-5 `Persuasive only — non-precedential` is derivable ONLY from
  `court_level: district` (factually false for a COA case; would also corrupt the projected
  `court`/`court_level`). No lake-schema home exists for the non-precedential fact:
  `identity.additionalProperties: false` forbids a `published`/`precedential` key (would break
  LINT-13), and a stored top-level `authority_weight` is ignored by the projector. **Convergence
  requires a `project.py` derivation enhancement (out of CAMP-L12 write-scope):** have
  `authority_weight()` return tier-5 when the record carries a sanctioned non-precedential/
  unpublished signal; that same single re-projection then also sweeps Trent's mechanical
  `opinion_id`/`projected_at` drift. Left page + lake UNCHANGED. `needs_orchestrator: true`.

## Lint-semantics note for the orchestrator (two adjudications owed)

1. **Trent (this packet's 1 residual RED).** Projector-derivation gap: no non-precedential/
   unpublished tier for a COA disposition. Needs a `project.py::authority_weight()` enhancement
   (honor an explicit non-precedential signal) — the only clean path to LINT-12 = 0 content-wide.
   Alternative (worse): a LINT-12 carve-out exempting adjudicated hand-overrides, which would
   silence a whole class of legitimate drift.
2. **S1 §3.1 vs S2 SD9 conflict (corpus-wide, latent, NOT this packet's reds).** S1 A4/§3.1 says an
   `overruled` case's authority-weight "moves to tier 6 (Historical)", but the projector is
   court_level-only, so the genuinely-overruled verified exemplars **Olmstead** and **Gouled** sit
   at `Binding — SCOTUS` (green because page==projector). Either (a) accept court-level weights
   corpus-wide (overruled status stays in `field_i_validity`) — the de-facto convention this packet
   applied to Sanders/Frank — or (b) enhance `project.py` to implement the §3.1 Historical downgrade
   from derived treatment and then re-project Olmstead/Gouled (and, post-S6, Sanders/Frank) to
   `Historical`. This is a spec/projector decision, not a lint-12-drift fix.

## Coverage (deterministic 6/6)

Assigned: 6 escalation rows. Examined: 6. Skipped: 0.
- FIXED: 4 (Roberson code; Sanders/Frank re-project; Kalkines lake+re-project).
- ALREADY-RESOLVED: 1 (Gouled — sibling lane; confirmed green).
- NOT-FIXED (out-of-scope, escalated): 1 (Trent — projector enhancement owed).

## Footprint / scope hygiene

- Edited: `scripts/lint/_common.py`, `scripts/s2/serializer.py`,
  `_overhaul2/lake/cases/Kalkines v. United States.json`,
  and via `project.py --write` (frontmatter only) `content/cases/{Arkansas v. Sanders,
  Frank v. Maryland, Kalkines v. United States}.md`.
- Did NOT touch: `scripts/s2/project.py` (derivation frozen — out of scope), the Trent lake record
  or page, `_overhaul2/points/registry.yaml`, any ledger. No CourtListener calls (lake + text cache
  only). No staging/commit. Many concurrent sibling-lane page writes are present in the shared tree
  and were left untouched.

## Outputs
- `_run/s9/p4/campaign/CAMP-L12-fixes.jsonl` — 6 rows (camp.fix.v1).
- `_run/s9/p4/campaign/CAMP-L12-summary.md` — this file.
