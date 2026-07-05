# S2 fix work order — F-S2-21 / F-S2-22 (session-8 finding: Lewis v. United States (1966))

Orchestrator adjudication 2026-07-05. Session 8's flag (Lewis v. United States (1966) →
fabrication_suspected) is a wrong-candidate rejection — fail-closed held correctly, but the
pipeline never surfaced the right cluster. Roster row is fully keyed: 385 U.S. 206 (1966),
SCOTUS, docket 36. The ladder selected United States v. Demko (cluster 107303, 385 U.S. 149,
also 1966-12-05 SCOTUS) as "viable," never reaching the citation rung that would have found
Lewis precisely. Two defects; fix ONLY these; offline; no network; no commits.

## F-S2-21 — year-disambiguator parenthetical poisons identity search params

Wiki disambiguated titles ("Lewis v. United States (1966)") flow RAW into
`identity_search_params`: the `case_name=` filter gets zero hits and the fallback `q=` gets
relevance noise. Roster has 8 such rows; 4 completed only by luck (right case happened to be in
the q-rung top-3), 3 still pending (Mathis v. United States (1968), United States v. Harris
(1971), United States v. Smith (2024)).

Fix: strip the trailing year parenthetical (reuse `strip_trailing_year_parenthetical`) from the
title/caption before building EVERY search param that carries it — the primary `case_name`, and
all fallback rungs (`q`, docket rung's implicit name use if any). The record_id / stored title
keep the disambiguator (identity of the roster row is untouched — search params only).
Fixture: params built for "Lewis v. United States (1966)" carry case_name/q "Lewis v. United
States" and keep court=scotus + 1966 date window.

## F-S2-22 — ladder viability too weak when an expected citation exists

Rung viability currently accepts year+court agreement alone, so a same-year same-court WRONG
case (Demko) terminates the ladder before the citation rung runs. When the roster row HAS an
expected_citation, a rung candidate that fails the citation match must NOT terminate the ladder;
the citation rung must get its chance. Year+court-only viability remains acceptable ONLY when
the roster row has no expected_citation (recent/no-cite rows per R2(b)). Best-so-far behavior
unchanged (non-citation-viable candidates are still retained as last resort after ALL rungs run,
flowing through the existing scoring + two-key + caption logic).

Fixture: a Lewis-shaped stub (expected cite present; q rung returns 3 same-year same-court
non-matching clusters; citation rung returns the true cluster) must resolve via the citation
rung to the true cluster with the q-rung candidates journaled as non-viable; a no-cite stub with
year+court agreement still terminates at the q rung as today.

## Expected post-fix outcome (session-9 readjudication)

Lewis v. United States (1966) → under_review via citation+party-text on the cluster whose
citations[] carry 385 U.S. 206 (docket 36 corroborates).

## Acceptance

Full self-test suite green + new fixtures; resume-stability for completed records (zero new
calls, statuses unchanged — including the 4 lucky-path disambiguated completions); report files
touched + fixture list + self-test tail.
