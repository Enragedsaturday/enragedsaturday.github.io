# S2 fix work order — F-S2-31 (CodeRabbit S2 spec gate: the flip-gating set)

Orchestrator adjudication 2026-07-06 of `_run/gates/S2-coderabbit-50ef21f.md` (27 findings:
1 critical + 15 major + 11 minor). This work order = the S2-path subset that gates the
verified-flip. (RETRO-covered re-detections routed to the pending Dispatch A/B lanes; new
quartz/lint-lane items routed separately.) Offline; no commits; you own scripts/s2/ingest.py,
scripts/s2/project.py, scripts/s2/authority_db.py, scripts/lint/lint12_drift.py,
scripts/lint/lint14_pagerecord.py.

## CRITICAL (CONFIRMED LIVE — Entick + Wilkes carry field_i_validity=good_law on not_found)

ingest.py ~2668-2771 + ~3957-3974: `seed_treatment_from_migration` and
`seed_preseeded_treatment` mutate treatment.field_i_validity BEFORE the fail-closed status
check; not_found/blocked records keep the seeded validity. Fix: guard both seeds — return
False when record status ∈ FAIL_CLOSED_STATUSES; on such records treatment.field_i_validity
must be/remain "unverified". DATA REPAIR: a journaled one-shot (--repair-failclosed-treatment
or fold into the existing repair command) resets Entick + Wilkes treatment.field_i_validity →
"unverified" (provenance-stamped, F-S2-31). Fixture: identity→not_found + legacy treatment
present → validity stays unverified.

## Majors (all CONFIRMED by orchestrator adjudication)

1. lint14_pagerecord load_records: JSONDecodeError swallowed bare + duplicate record_id
   silently overwrites → both become HIGH violations (fail-closed).
2. authority_db verify_roundtrip: empty cases table returns True → raise on zero rows.
3. project.py load_records: records missing record_id silently dropped → surface (warning +
   count in summary; nonzero exit on --write).
4. project.py dry_run_or_write: case pages whose record_id resolves to no record are silently
   skipped → track as unmatched, surface in summary, fail the A13/ok_to_project gate on any.
5. project.py ok_to_project: missing_treatment_status pages currently pass → fold into the
   refusal path (or stage to review) — they must not silently project.
6. ingest.py manifest_rows_by_record_id: OSError/JSONDecodeError → silent {} → can misclassify
   lookup_class in the repair's page-vs-stub disambiguation → let the exception propagate
   (fail closed).

## Minors (fix — trivial, same files)

7. lint12 drift message names the record path where the PAGE path belongs (first %s) — swap.
8. project.py --dry-run parsed but unused → parser.error on --write --dry-run together.

## Acceptance

Full self-test sweep green (ingest, project, authority_db, lint12/13/14) + new fixtures for
critical/1/2/3/4/5; the two-record repair validated (Entick/Wilkes validity=unverified,
journaled); LINT-12=0 / LINT-13=0 / LINT-14=2 unchanged; report files touched + fixture list +
self-test tails.
