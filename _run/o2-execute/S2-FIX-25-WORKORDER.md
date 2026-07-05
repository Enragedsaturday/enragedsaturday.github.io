# S2 fix work order — F-S2-25 (CodeRabbit gate smoke run on the F-S2-24 diff)

Provenance 2026-07-05: first run of the standing spec-completion CodeRabbit gate (RUNBOOK §5
amendment; `_run/gates/SMOKE-coderabbit-f301fda.md`) over the F-S2-24 commit. 2 major findings,
both **CONFIRMED by code-reading adjudication** (Fable side-session; orchestrator may
re-adjudicate at pickup). Both are the mirror/completion of F-S2-24's cohort — same
fabrication_suspected-FP class that burned the session-11 Skinner adjudication. They affect the
remaining ~92 page rows (T–Z) + all 93 frontier-stub rows, so dispatch BEFORE the stub leg.
Bounded to `party_term_candidates` + `missing_party_terms`; offline; fixtures + self-test; no
behavior change outside the party-text key.

## F-S2-25 — party-term candidates: full→abbreviation direction + text-side apostrophe strip

1. **Full→abbreviation candidates (bounded).** `party_term_candidates` today expands only
   contraction→full (`assn` → adds `association`); a term that IS the full form (caption says
   "Association", text prints "Ass'n") generates no abbreviated candidate → party key false-fails.
   Add the forward direction: if the stripped term is a key in `CAPTION_TOKEN_CONTRACTIONS`, add
   its contraction as a candidate — **BUT NOT as a bare substring candidate**. The table contains
   1–2 char contractions (`co`, `n`, `s`, `e`, `w`, `ed`, `bd`) and 3-char forms that embed in
   common words (`com`, `dep`, `ins`); bare `candidate in text` would match nearly any opinion and
   flip the party key to a silent always-PASS (false-negative direction — worse than the FP it
   fixes). Bound it: abbreviation-direction candidates match **only on word boundaries**
   (`\b<candidate>\b` against the normalized text), while the existing original/stripped/full-form
   candidates keep their current containment semantics.
2. **Text-side apostrophe normalization.** `missing_party_terms` lowercases but never
   apostrophe-strips the opinion text; candidate `assn` cannot match text `ass'n`/`ass’n`
   (straight or curly glyph). Apply the same `strip_apostrophes` used on the candidate side:
   `lowered = strip_apostrophes((text or "").lower())`. (F-S2-24 normalized only the candidate
   side; both sides must share one normalization — same principle as the F-S2-19 comparison-key
   rule.)

Fixes 1+2 are complementary directions, not alternatives: term "association" + text "Ass’n"
needs BOTH (strip text → "assn"; forward candidate "assn" word-boundary match → TRUE).

## Fixtures

- term `association`, text containing only `Ass'n` (straight) → party key TRUE; same with curly
  `Ass’n` → TRUE.
- term `ass'n`, text containing only `Association` → TRUE (existing F-S2-24 direction preserved).
- term `company`, text containing `court` / `common` but NOT `co`/`company` as a word → FALSE
  (the `co` candidate must NOT substring-match; word-boundary guard proven).
- term `north`, text without the word `n`/`north` → FALSE (1-char contraction guarded).
- term with no table entry → candidate set unchanged from F-S2-24 behavior.
- Existing F-S2-24 fixtures (Skinner containment + party key) unchanged and green.

## Expected post-fix outcome

No readjudication required (no live row currently failed on this class); the fix de-risks the
T–Z page pass + the 93-stub frontier leg. Full self-test suite green + new fixtures;
resume-stability unchanged; report files touched + fixture list + self-test tail.

## Gate note

CodeRabbit's own proposed patch (artifact lines 67–80) implements fix 1 WITHOUT the word-boundary
bound — do not apply it verbatim; the bound above is the adjudicated form. Fix 2's proposed patch
is correct as-is.
