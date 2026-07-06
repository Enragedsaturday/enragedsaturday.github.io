# S2 fix work order — F-S2-33 (stub-session-2 findings: parentheticals, currency captions, ladder-continuation)

Orchestrator adjudication 2026-07-06. Session stopped at 37/89 on transport fetch_failed
(resumable, not a defect); 5 fabrication_suspected + 1 not_found among the processed rows, all
adjudicated as fix-or-known classes. The pseudo-row (a split DESCRIPTOR the orchestrator's
batch-2 assembly leaked as a case) is already removed + journaled — not builder scope. Offline;
no commits; scripts/s2/ingest.py.

## (a) Non-year parentheticals poison search params (extends F-S2-21)

"United States v. United States District Court (Keith)" and "United States v. Robinson (4th
Cir. en banc)" flow raw into case_name/q. Fix: at SEARCH-PARAM construction only (record ids
untouched), strip ANY trailing parenthetical — nickname, court-posture, or year (generalize
strip_trailing_year_parenthetical to strip_trailing_parenthetical for the search-param path
only; the year-specific variant stays for caption comparison where it matters). Fixtures:
Keith + Robinson-en-banc param shapes.

## (b) Ladder continuation when caption containment fails and stronger keys remain

Von Neumann (docket 84-1144) + $8,850 (docket 81-1062): a case_name-rung candidate was
accepted (year+court viability — the queue rows lacked usable citations) and flagged
fabrication_suspected WITHOUT the docket rung ever running, even though a docket was present.
Fix (viability refinement, extends F-S2-22): a candidate that FAILS caption containment is
NON-viable for ladder termination while any stronger-key rung (citation with a usable expected
cite, docket with a present docket) remains unrun; continue the ladder, keep best-so-far as
today. Expected effect: the docket rung finds the true clusters for both forfeiture cases
(their CL captions spell out the currency amount — "$8,850" vs "Eight Thousand Eight Hundred
Fifty Dollars"; docket keys bypass the caption entirely). Fixture: a stub with docket present +
case_name rung returning a containment-failing candidate must reach the docket rung.

## (c) Currency-caption tokenization (bounded; only if (b) leaves a residual)

Do NOT attempt general number-spelling equivalence. Only if the docket rung still cannot
terminate for a currency caption, add a minimal digit-grouping normalization ("$8,850" →
tokens ["8850"]; strip $ and commas) so containment can match CL captions that use digits.
Skip entirely if (b) suffices for both live rows — report which.

## Post-fix execution (same session as the fix loop close)

--readjudicate the 5: keith--108581 · robinson-4th-cir-en-banc--4385870 · timbs-v-indiana--4673515
(diagnose from its record whether (a)/(b) explains it — its queue row DID carry docket 17-1091;
report the root cause found) · von-neumann--466403 · 8-850-in-currency--423712. Then resume the
52 pending (--session-minutes 90). long-lake-township-v-maxon--ucb0bfc28 not_found: leave as-is
(state-court mention-only row; S6 ledger records it below-floor — do NOT readjudicate).

## Acceptance

Self-test suite green + new fixtures; the readjudicated 5 land verified_identity (or a
documented honest terminal state with the rung trail); the 52 pending complete; report
distribution + calls + the timbs root cause.
