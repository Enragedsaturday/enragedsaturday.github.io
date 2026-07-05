# S2 fix work order — F-S2-23 (session-10 finding: Peters v. New York)

Orchestrator adjudication 2026-07-05. Peters v. New York → fabrication_suspected is a
wrong-candidate rejection (fail-closed held). Peters is the companion case consolidated inside
Sibron v. New York, 392 U.S. 40 (1968) — CL has NO separately-captioned Peters cluster, so the
CORRECT resting state is the Sibron cluster via the F-S2-16 precedence (two-key PASS + caption
warning). The pipeline missed it for one bounded-fetch reason. Fix ONLY this; offline; no
commits.

## F-S2-23 — rungs spend cluster fetches on arbitrary top-N instead of citation-prefiltered rows

Evidence (cached response ddca4399…, citation rung for expected "392 U.S. 40"): the
citation= filter matched 14 fuzzy rows (reporter cross-matches like "40 S. Ct. 392",
"55 Empl. Prac. Dec. (CCH) 40,392"); Sibron v. New York (cluster 107730) is at rank 5 with
EXACTLY "392 U.S. 40" in its `citation` array — but the rung fetched clusters only for ranks
1–3 (R-01's cap), so the true cluster was never examined. The search response's per-row
`citation` array is already available at zero marginal cost.

Fix: in every identity search path (primary + all fallback rungs), when the roster row has an
expected_citation, PRE-FILTER result rows by exact `citation_compare_key` match between
normalize_cite(expected) and any entry of the result row's own `citation` array; spend the
≤3-per-rung cluster fetches on prefiltered rows FIRST (then, only if none prefilter-match, fall
back to the current top-N order). Journal the prefilter outcome per rung (matched-row count +
which cluster_ids were fetched because of it). Everything downstream (viability, scoring,
two-key, caption precedence, best-so-far) unchanged.

Fixture: a Peters-shaped citation rung — 14 rows, exact-citation row at rank 5 — must fetch the
rank-5 cluster within the 3-fetch budget, mark the rung viable, and resolve; apply_identity then
lands under_review + caption_mismatch_canonical via two-key PASS (companion-case shape:
input "Peters v. New York" vs canonical "Sibron v. New York"). A no-prefilter-match rung must
behave exactly as today (fixture: current top-3 behavior byte-stable).

## Expected post-fix outcome (session-11 readjudication)

Peters v. New York → under_review via citation+party-text on cluster 107730 (Sibron v. New
York), reason_code caption_mismatch_canonical, warning preserved — the honest consolidated-
companion resting state for S6/S9.

## Acceptance

Full self-test suite green + new fixtures; resume-stability unchanged for completed records;
report files touched + fixture list + self-test tail.
