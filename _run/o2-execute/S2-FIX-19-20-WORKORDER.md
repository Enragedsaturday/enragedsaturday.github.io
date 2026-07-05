# S2 fix work order — F-S2-19 / F-S2-20 (session-4 finding: Commonwealth v. Herlth)

Orchestrator adjudication 2026-07-04. Session 4's one new flag (Commonwealth v. Herlth →
fabrication_suspected) is a false positive produced by two small normalization gaps. The
machinery around it behaved exactly as designed (fallback ladder ran all rungs, selected the
correct cluster 10870804 "Com. v. Herlth, J." / 2026 Pa. Super. 114 as best-so-far; fail-closed
precedence applied). Fix ONLY these two gaps; offline; no network; no commits.

## F-S2-19 — caption tokens: legal-caption abbreviation contraction (Bluebook-T6 class)

"Commonwealth v. Herlth" vs CL canonical "Com. v. Herlth, J." fails token containment because
"commonwealth" ≠ "com". Same class as Birchfield's cosmetic warning ("North Dakota" vs
"N. Dakota"). CL systematically abbreviates (Pa. captions are "Com. v. X" throughout), so this
recurs across the remaining ~463 rows.

Fix: inside `caption_token_set`, CONTRACT tokens to their abbreviated form via a small fixed
table (contraction is deterministic; expansion is ambiguous — do not expand). Table (token →
contracted): commonwealth→com; board→bd; education/educ→ed; school→sch; district→dist;
county/cnty/cty→co; township→twp; department/dept→dep; university/univ→univ; insurance/ins→ins;
company→co? — NO: company and county would collide; use county→cty and company→co;
north→n; south→s; east→e; west→w; united→u? — NO: leave "united"/"states" alone (too load-bearing
in "United States" captions; CL does not abbreviate them). Keep the table to exactly the listed
entries; document each. Ensure 1-char contracted tokens (n/s/e/w) survive any minimum-length
token filter AFTER contraction (i.e., filter before contraction only, or exempt table outputs).
Both input and canonical sides pass through the same contraction, so containment compares in
contracted space.

Fixtures: "Commonwealth v. Herlth" ↔ "Com. v. Herlth, J." MATCH; "Birchfield v. North Dakota" ↔
"Birchfield v. N. Dakota. William Robert Bernard" MATCH; "Board of Education v. Earls" ↔
"Board of Ed. v. Earls" MATCH; reversed-caption Adams/Williams still NO-MATCH; "County of Inyo"
↔ "Company of Inyo" NO-MATCH (county/company must not collide).

## F-S2-20 — normalize_cite: punctuation/case-insensitive comparison

Roster "2026 PA Super 114" vs CL "2026 Pa. Super. 114" fails equality on period/case styling of
the neutral reporter. Fix: in `normalize_cite` (or a comparison-key wrapper used by
`citation_matches_expected`), after the existing trailing-parenthetical strip, casefold and
remove periods, then collapse whitespace. Digits (volume/page) must still match exactly.
Fixtures: "2026 PA Super 114" == "2026 Pa. Super. 114"; "283 F.3d 1040" == "283 F. 3d 1040";
"403 U.S. 388" == "403 US 388"; "403 U.S. 388" != "403 U.S. 389".

## Expected post-fix outcome (for the session-5 readjudication)

Commonwealth v. Herlth → under_review via citation+party-text on cluster 10870804 (cite matches
once normalized; party already True; caption contained after T6 contraction).

## Acceptance

Full self-test suite green + the new fixtures; no behavior change for already-completed records
on resume (zero new calls, statuses unchanged); report files touched + self-test tail.
