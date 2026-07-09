# S8 work order — R4/R5 split pincites + text fragments + lake write-back (lane: o2-opus-xhigh)

**Read first:** spec R4 + R5 (+ §5 Method 4, §9 item 1, the cross-spec S2 § A14 note at the
spec's tail) · exhibit `content/warrant-exceptions/Knock and Talk.md` lines 19–34 (both
halves wired; the byte forms) · `content/cases/Florida v. Jardines.md` +
`United States v. Walker.md` (case-page citation-line form) · `scripts/s8/zones.py`
(import; frozen contract) · precedent for sanctioned lake surfaces:
`scripts/s2/ingest.py` `--rekey-lead-opinion-from-cache` / `--rekey-cluster-panel`
(journaled, fail-closed, max_calls=0) and the S7 repair-lane journal entry (2026-07-09).

## The convention being wired (spec R4, exhibit-normative)

Quoted + pinned proposition in prose:
`"…quote…" *[[Case#^pin-N|Name]]*, 569 U.S. at [8](CL-URL#:~:text=FRAGMENT) (2013).`
— name-half internal pin-deep (kept from S5 R16), pincite page numbers external with the
validated fragment. Paraphrase (no pin): name page-level internal + pincite **plain
external** (opinion page URL, NO fragment — never invent). Case pages: each pinned block's
own citation line `— 569 U.S. at 6` → `— 569 U.S. at [6](CL-URL#:~:text=…)`. Table
`opinion` cells + LCD `[opinion]` markdown links stay page-level (untouched). *id./Id.*
chains: an `*[[Case#^pin-N|id.]]*` form is sanctioned (exhibit line 19); a plain `id.`
resolves to the immediately preceding case reference on the same page — wire only when that
resolution is unambiguous, else leave plain (fail-closed).

## Deliverable 1 — `scripts/s8/fragments.py` (R5 generator + validator)

- Input: lake records with `pinpoints[].quote_fidelity == "matched"` (the G3-pass signal;
  184 expected). Text source: `$CSSI_LAKE_ROOT/cache/text/<lead_opinion_id>.txt` (default
  root `/Users/johngalt/cssi-lake`) — **zero live CL, zero quota**.
- Contract per spec R5 (each rule has a fixture): (a) normalize to rendered CL text —
  whitespace collapses; dashes/quotes follow the SOURCE form, not our curly forms;
  (b) fragment text must not cross a star-page label (`*NNN` visible mid-text) — trim or
  split; (c) validate = exactly ONE whitespace-insensitive match against the cached text;
  (d) prefer a distinctive start-only snippet (≥5 words); long quotes → `start,end`;
  multi-match → add `prefix-`; (e) URL-encode per WICG text-fragment syntax
  (`#:~:text=[prefix-,]start[,end]`).
- Output: `_run/o2-execute/s8-fragments.jsonl` — one row per pinpoint:
  `{record_id, pin_id, opinion_id, fragment, validated: true, matches: 1, date}` or
  `{…, fragment: null, reason}` for unvalidatable (those get plain external pincites).
  `--self-test` + fixtures under `scripts/s8/fixtures/fragments/` (star-label crossing,
  multi-match prefix disambiguation, curly-vs-source quote normalization, no-match).

## Deliverable 2 — sanctioned S2 surface `--apply-fragments` in `scripts/s2/ingest.py`

The lake is single-writer; fragments land through a NEW sanctioned offline surface,
mirroring the repair-lane pattern (fail-closed, journaled, `max_calls=0`, self-tested):
- Consumes `s8-fragments.jsonl`; for each validated row, sets
  `pinpoints[].fragment` + `pinpoints[].fragment_validated_at` on the matching record/pin.
- Guards: record must exist; pin id must exist on the record; pin's `quote_fidelity` must
  be `matched` (refuse otherwise); journal every write to the lake journal (existing
  convention); idempotent.
- **Schema first:** add optional `fragment` (string) + `fragment_validated_at` (date) to
  the pinpoint block in `_overhaul2/lake/_schema.json` — additive, precedent = the B1 enum
  extension at S7 close. `python3 scripts/lint/lint13_schema.py` must be 0 after.
- Extend ingest self-tests for the new surface (the repair-lane surfaces show the shape).

## Deliverable 3 — `scripts/s8/link_pincites.py` (the wiring pass)

- **Case pages first:** for every end-of-block `^pin-N` whose fragment validated, wire the
  block's citation line (`— <cite> at <pages>` → external fragment link on the page
  numbers). Pin blocks without a validated fragment: leave the citation line untouched.
- **Doctrine-side:** outside R2 zones, find cite patterns adjacent to case links/mentions
  (`, 569 U.S. at 8` / `, 799 F.3d 1361, 1363 (11th Cir. 2015)` forms):
  1. name-half already `[[Case#^pin-N|…]]` → wire the pincite numbers with THAT pin's
     fragment (if validated) else plain external;
  2. name-half page-level/plain + the sentence carries a quotation → match the quoted span
     (whitespace-insensitive) against the case's pin quotes; UNIQUE match ⇒ upgrade the
     name-half to `#^pin-N` AND fragment-link the pincite; no/multi match ⇒ leave the
     name-half as-is + pincite plain external + journal row;
  3. paraphrase (no quotation in the citing sentence) ⇒ pincite plain external, name-half
     untouched (tier-3 downgrades NEVER get fragments — spec R4/R5 check).
- External URL = `https://www.courtlistener.com` + lake `identity.absolute_url`. Any other
  host must be on the S2 R14 whitelist (read it from the lake/_advisory or refuse + queue).
- Emits R12 rows (`s8-link-ledger.rows.jsonl`, action `linked-deep` / `linked-external` /
  `plain:*`) + journal `_run/o2-execute/S8-PINCITE-JOURNAL.jsonl`. Dry-run default,
  `--write`, idempotent, `--self-test` + fixtures (each rule above).

## Execution steps

1. fragments.py → self-test → run; report validated/unvalidatable split + 5 sample
   fragments (decoded) with their quotes.
2. Schema addition + `--apply-fragments` + ingest self-test green → apply → LINT-13 = 0,
   lake journal rows present. Report counts.
3. link_pincites.py self-test → dry-run on `content/cases/` → report 10 sample diffs →
   **STOP for orchestrator GO** → `--write` cases → dry-run doctrine set → report →
   **STOP for GO** → `--write` doctrine.
4. `npx quartz build` green; spot-render one case page + Knock and Talk.

## Constraints

COMMIT NOTHING · zero live CL (cached text only) · stdlib only · touch only
`scripts/s8/**`, `scripts/s2/ingest.py` (the one surface + tests), `_overhaul2/lake/`
(via the surface ONLY), `_run/o2-execute/` artifacts, and content edits of exactly the
citation-link form. Never edit quote text, never invent a page number, never fragment a
paraphrase. The `id.`-resolution ambiguity rule is fail-closed — when in doubt, plain.
