# S2 fix work order — F-S2-24 (session-11 finding: Skinner v. Railway Labor Executives' Ass'n)

Orchestrator adjudication 2026-07-05. Skinner → fabrication_suspected is a false positive with
cite MATCHED (489 U.S. 602, cluster 112219 correct): containment failed ONLY on apostrophe
styling ("ass'n" vs CL's "Assn."), and the party-text key failed because the chosen last-word
term is the Bluebook abbreviation "ass'n", which never appears in opinion prose (the text says
"Association"). Same T6 family as F-S2-19. Three bounded extensions; fix ONLY these; offline;
no commits.

## F-S2-24 — apostrophe + association-family normalization, and abbreviation-aware party terms

1. **Apostrophe-normalized caption tokenization**: strip apostrophes in caption token
   normalization (input AND canonical sides identically): "ass'n" → "assn",
   "executives'" → "executives". (This alone flips Skinner's containment to PASS — the sides
   become identical token sets.)
2. **T6 table**: add the association family — association→assn (and ass'n→assn falls out of the
   apostrophe strip). Nothing else added.
3. **Abbreviation-aware party-text key**: keep last-word term selection, but match the term as a
   CANDIDATE SET: {original lowercase, apostrophe-stripped, T6-expanded full form(s) via reverse
   lookup on the contraction table}. Match if ANY candidate appears in the text. For Skinner:
   {"ass'n", "assn", "association"} → "association" in text → party key TRUE. Do NOT weaken to
   any-word-of-side matching.

Fixtures: Skinner caption ↔ "Skinner v. Railway Labor Executives' Assn." containment MATCH;
party key TRUE against text containing "Association" but not "ass'n"; reversed-caption
Adams/Williams still NO-MATCH; a term with no abbreviation expands to itself only (candidate
set = {word}); existing T6 fixtures unchanged.

## Expected post-fix outcome (session-12 readjudication)

Skinner v. Railway Labor Executives' Ass'n → under_review via citation+party-text on cluster
112219, no caption warning (containment passes).

## Acceptance

Full self-test suite green + new fixtures; resume-stability unchanged; report files touched +
fixture list + self-test tail.
