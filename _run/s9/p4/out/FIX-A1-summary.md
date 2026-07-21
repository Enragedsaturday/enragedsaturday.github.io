# FIX-A1 summary — LINT-12 stale re-projection + substantive drift

Packet: FIX-A1 (WRITE-SCOPE: content/ case-page projected fields only + `_run/s9/p4/`)
Authority: RULING P4-05 (COH gate-c), triage rows A1 (136 mechanical class) + B3 (15 substantive).
Model/lane: claude-opus-4-8 / FIX-A1. Branch `overhaul2/execute`. Writer != checker: outputs returned for machine adjudication.

## Projector identity
The "S5 projector" named in RULING P4-05 is `scripts/s2/project.py` — the lake -> case-frontmatter
projector (the COH findings themselves prescribe `python3 scripts/s2/project.py --write <page>`).
`scripts/s5/` holds only `convert_tables.py` (an R5 table converter, not the projector). The projector
rewrites ONLY the managed frontmatter subset (`serializer.MANAGED_TOP_LEVEL`); it never touches body
prose or preserved frontmatter, is A13-gated, and is value-diff driven (writes only changed fields).

## Coverage (deterministic)
- Assigned: 151 LINT-12 highs (= COH-findings `lint12-drift`: 136 `reprojection-stale` + 15 `substantive-drift`).
- Examined: 151 / 151. Skipped: 0.
- Live LINT-12 reconciled to the harvested set exactly (151 == 151, zero delta) before any write.

## Part 1 — 136 mechanical (reprojection-stale)
- All 136 share one signature: `differing_fields = courtlistener.opinion_id, lake.projected_at`.
- Dry-run over exactly the 136: gate PASS, refused=false, 0 warnings/errors, field_counts
  `{courtlistener.opinion_id: 136, lake.projected_at: 136}`, ZERO pages with any extra field.
- Wrote via `project.py --write` (only the 136 paths; the 15 substantive were withheld from this batch).
- Per-file byte verification (git diff): all 136 = 2 added / 2 deleted lines, every changed line an
  `opinion_id:` or `projected_at:` frontmatter line, every hunk inside the top-60 frontmatter region.
  Pattern per RULING P4-05: `opinion_id: null -> <identity.lead_opinion_id>`; `projected_at` stale-date bump.
  No prose / non-projected field touched on any file.
- Result rows: 136 in `FIX-A1-fixes.jsonl` (subclass `reprojection-stale`).

## Part 2 — 15 substantive (individual review): 10 applied, 5 escalated (+1 code-defect escalation)
Field split: 9 `scope_note`, 4 `authority_weight`, 1 `varies_by_point` (Gouled), 1 `citation/parallel_cite` (Weaver).

APPLIED (10 — lake authoritative, page a stale projection; re-projected, diff limited to projected fields):
- 9 `scope_note`: Arizona v. Roberson, Brendlin v. California, Heien v. North Carolina, Jacobson v.
  United States, United States v. Martinez-Fuerte, United States v. Matlock, United States v. Ramsey,
  Taylor v. Riojas, United States v. Van Leeuwen. Page held either the generic migration placeholder
  ("Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.") or a note the lake
  *supersets* (Taylor/Van Leeuwen: page text preserved + appended R15 audit disclosure). The lake is the
  designated treatment source-of-truth and its value is strictly more conservative/complete; no page
  content lost. Re-projection propagates the lake value — no fresh legal judgment by FIX-A1.
- 1 `citation/parallel_cite`: State v. Weaver — lake holds the Bluebook-correct official cite
  (349 S.W.3d 521 (2011), regional reporter primary) with the LEXIS cite as parallel; page had them
  reversed (pre-backfill stale). Both cites remain present; only the primary/parallel roles swap to the
  lake's already-encoded assignment. Also carried the opinion_id/projected_at backfill.
- Verification: dry-run field_counts `{treatment.scope_note:9, citation:1, parallel_cite:1,
  courtlistener.opinion_id:1, lake.projected_at:1}`; per-file git diff confirmed every hunk inside the
  frontmatter block, no body/prose changed.
- Result rows: 10 in `FIX-A1-fixes.jsonl`.

ESCALATED (5 substance conflicts -> `FIX-A1-escalations.jsonl`; NOT edited — each needs a legal-substance call):
- authority_weight, overruled-SCOTUS convention: **Arkansas v. Sanders** (page "Historical" vs projector
  "Binding — SCOTUS"; overruled by Acevedo) and **Frank v. Maryland** (page "Historical (formerly Binding
  — SCOTUS)"; overruled by Camara). Does authority_weight carry overruled status or only court level?
- authority_weight, court taxonomy: **Kalkines v. United States** (page "Binding in-circuit — Fed. Cir."
  vs projector "Historical"; Court of Claims / Fed. Cir. predecessor). Page may be MORE correct than lake.
- authority_weight, unpublished — LAKE IS WRONG: **United States v. Trent** (page "Persuasive only —
  unpublished 6th Cir. disposition" is correct per Wave-B; projector wrongly derives "Binding in-circuit —
  6th Cir."). Re-projection would REGRESS the Wave-B correction. Fix owed on the LAKE side (out of scope).
- treatment.varies_by_point: **Gouled v. United States** (page false vs lake true; overruled in part by
  Warden v. Hayden). Flipping true implies an owed S5 R5 point-status table -> adjudicate with triage B4.

CODE-DEFECT ESCALATION (1 — discovered during the apply): **Arizona v. Roberson** (serializer round-trip).
- The scope_note fix WAS applied (page byte-equals the projector output; valid YAML; renders correctly).
- LINT-12 nonetheless stays RED for this one page: the writer `serializer._dump_yaml_lines` escapes a
  literal `"` as `\"` (correct YAML), but the reader `scripts/lint/_common.py::_unquote` (lines 173-177)
  strips only surrounding quotes and never unescapes `\"` -> `"`. Any managed string containing a literal
  double-quote (here scope_note's `("R15 treatment audit required")`) can never round-trip to equality,
  producing a LINT-12 false positive AND a projector idempotence failure (pre-existing/latent, not
  introduced by FIX-A1). Fix owed in `scripts/lint/_common.py` (or serializer emit style) — both outside
  FIX-A1 write-scope. No content edit owed; Roberson's page value is already correct.

## LINT-12 before / after (`scripts/lint/lint12_drift.py`, full corpus)
- BEFORE: 151 highs.
- After Part 1 (136 mechanical): 15 highs (== the substantive set exactly, zero collateral).
- After Part 2 (10 applied): **6 highs** remaining =
  - 5 intentional escalations (Sanders, Frank, Kalkines, Trent authority_weight + Gouled varies_by_point) — deliberately not edited, pending adjudication;
  - 1 Roberson — fix applied but red via the serializer round-trip false-positive (content already correct).
- Net: 151 -> 6, of which 0 are unaddressed defects: 145 mechanically fixed + 9 scope_note + 1 Weaver
  applied, 5 substance escalations, 1 code-defect escalation.

## Footprint / scope hygiene
- Touched: 146 `content/cases/*.md` pages (136 mechanical + 10 apply), managed frontmatter only.
- Did NOT touch: `_overhaul2/lake/`, `_overhaul2/points/registry.yaml`, any ledger, any `scripts/`.
- Concurrent sibling-lane writes observed in the shared tree and left untouched (NOT FIX-A1):
  `_run/s9/p4/P4-RULINGS.md`, `_run/s9/p4/p4-cl-calls.log`, `quartz/components/scripts/spa.inline.ts`,
  untracked `scripts/s9/p4_promo_identity.py`. No staging/commit performed.

## Outputs
- `_run/s9/p4/out/FIX-A1-fixes.jsonl` — 146 rows (136 mechanical + 10 apply).
- `_run/s9/p4/out/FIX-A1-escalations.jsonl` — 6 rows (5 substance + 1 serializer code-defect).
- `_run/s9/p4/out/FIX-A1-summary.md` — this file.
