# S2 fix loop 2 — review findings on the F-S2-16/17/18 diff (all UPHELD)

Read-only review lane (writer≠checker) verified the caption/precedence/normalize_cite/CLI work OK
but returned CLEAR-TO-RELAUNCH: no on three findings. Orchestrator adjudication: all three
UPHELD. Fix exactly these; do not expand scope; offline only; no commits.

## F-S2-16R-01 (HIGH) — fallback rungs unbounded + premature ladder stop (~ingest.py:1275)

Each fallback rung fetches clusters for `results[:10]` (1 search + up to 10 cluster calls — the
work order's envelope was ≤ ~4 added calls per zero-hit case), and `resolve_identity` stops on
ANY nonempty candidate set, so a `q=` rung returning unrelated hits starves the
citation/docket rungs that would have found the case precisely.

Fix: per rung, fetch clusters for at most the top 3 results; a rung only terminates the ladder
when it yields a VIABLE candidate — one with positive identity evidence (expected-citation match,
or year+court agreement); otherwise continue to the next rung, keeping the best-scored candidate
so far as a last resort after all rungs run. Journal per rung: result count, clusters fetched,
viable yes/no.

## F-S2-16R-02 (HIGH) — readjudication leaves stale payload (~ingest.py:2601)

`apply_readjudications` resets status/resume/method/reason but keeps the prior run's
identity/citations/pinpoints/progeny/treatment payload in the case JSON. If the rerun is
interrupted mid-identity, downstream code can consume the stale cluster_id — not fail-closed.

Fix: at reset time, rebuild the record's identity and ALL downstream sections from the empty
shell (preserve only roster-sourced fields: record_id, page/slug/title, expected citation,
court/year/docket, source metadata), and journal the field-level reset. Fixture: a fail-closed
stub that starts with a stale cluster_id must show empty identity after readjudication and
before any network call.

## F-S2-16R-03 (MED) — self-test gaps

Extend the fallback-ladder self-test: 10-hit `q=` rung with no viable candidate → asserts
bounded cluster calls (≤3 per rung), continuation to the citation rung, and `not_found` only
after every rung exhausts. Add the stale-payload readjudication fixture from R-02.

## Acceptance
Full self-test suite green including the new fixtures; report files touched + self-test tail +
confirmation that the session-4 launch line is unchanged.
