# S2 fix work order — F-S2-28 / F-S2-29 (R15 treatment-audit findings)

Orchestrator adjudication 2026-07-06 of the R15 Claude-lane treatment audit
(`_run/o2-execute/R15-TREATMENT-AUDIT.md`, 4 flags). The S9-boundary safety core HELD (14,326
edges all proposed-only). Two fix items; offline code + fixtures; the lane reruns happen in a
follow-up paced session; no commits.

## F-S2-28 — lane3_recency inert corpus-wide (audit FLAG-C) + lane2 cursor gaps (FLAG-A)

**Root cause (verified by code reading):** `lane_query` for lane3 (ingest.py:~2134) builds
`"%s AND filed_after:%s" % (query, filed_after)` — CourtListener's q-string parser has NO
`filed_after:` field, so the token matches zero documents; every lane3 search returned count=0
(455 HTTP-200 no-op calls), `reviewed=0` corpus-wide, lane marked complete. The separate
`filed_after` GET param the code also passes is the correct mechanism and is sufficient.

Fix (a): lane3's q = the bare `complete_query` (identical to lane2's q-shape); keep the
`filed_after` GET param + `order_by dateFiled desc` + snippet fields. Do NOT inject date syntax
into q. Fixture: lane3 params for a stub record carry q == complete_query and
filed_after == recency_window_start(); a regression fixture asserts no "filed_after:" substring
in any lane q-string.

Fix (b): add a lane-scoped rerun mechanism — `--rerun-lane <lane_name>` (repeatable,
optionally with `--records <id>` filters): resets that lane's status/cursor/derivation on
derived (under_review) records — journaled as an adjudication event citing F-S2-28 — and
re-runs ONLY that lane through the normal paced pipeline (other lanes untouched, resume-stable;
identity/citations/progeny never re-run). Estimated rerun cost: ~456 lane3 searches + triage
reads ≈ 500–900 calls (envelope headroom: 15,959 of ~23k used).

Fix (c) — FLAG-A: lane2 cap rows for City of Ontario v. Quon, United States v. Anchondo,
Vega v. Tekoh carry cap_hit+audit_needed but final_cursor:null (408 other lane2 caps have
cursors — not a design pattern). Diagnose the code path that dropped the cursor (likely a
boundary case: cap hit exactly at a page edge), fix it, add a fixture, and include these 3 in
the rerun via `--rerun-lane lane2_top_cited --records ...`.

## F-S2-29 — pre-seed/migration structural repairs (audit FLAGS B + D)

FLAG-B: the two A13 pre-seeded rows (New York v. Belton, United States v. Smith (2024)) store
`point_overrides[].by` as a STRINGIFIED nested list ("[[Arizona v. Gant]]") instead of an array
of controlling-case objects; Gant's cluster_id (145887, named in R5's worked specimen) absent;
Smith's override field_ii is "".

FLAG-D: all 12 migration/pre-seed overrides + 20 `migration:*` edges name their controlling
case by NAME ONLY (cluster_id:null, cite:null) — R5's Check requires cluster_id. (Lane-derived
edges are clean: 14,306/14,306 carry cluster_ids.)

Fix: a one-shot, journaled `--repair-migration-refs` pass: parse the stringified `by` values
back to arrays; resolve every migration-named controlling case to its cluster_id + official
cite FROM THE COMPLETED LAKE ITSELF (every controlling case is a page row now — resolve by
record lookup, zero CL calls; fail loudly listing any name that does not resolve to exactly one
record); fill Smith's field_ii from `_treatment-migration.json`; stamp repair provenance on
each touched record (adjudication event citing F-S2-29). Fixtures: stringified-by round-trip;
unresolvable name fails closed; already-well-formed override untouched byte-identically.

## Acceptance

Self-test suite green + all new fixtures; `--rerun-lane` and `--repair-migration-refs` fully
journaled with adjudication provenance; resume-stability for untouched lanes/records proven by
fixture; report files touched + fixture list + self-test tail + the FLAG-A root-cause note.
