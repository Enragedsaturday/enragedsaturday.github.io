# S2 fix work order — F-S2-26 (Entick churn + A16 `verified_off_cl` implementation)

Orchestrator adjudication 2026-07-05 (user-approved amendment; spec text landed as **S2 § A16**
with R2/R12/R14 pointers). Two defects + one implementation. Offline except where noted; no
mid-session interruption required — apply at the normal fix-loop window between builder
sessions; the running session is unaffected (loaded code is in memory; spec/schema text is
inert to it).

## Defect 1 — terminal `not_found` re-processed every session (the Entick churn)

`ingest.py:3011`: the skip-if-done gate is `resume.step_complete(record_id, "identity") and
record_json["identity"].get("cluster_id")`. A terminal `not_found` never has a cluster_id, so
Entick re-enters identity resolution EVERY session (24 journal touches to date), lands in the
cannot-replay branch, appends the same warning pair, and rewrites the record. Fix: also skip
when `step_complete` and the loaded record's status is a terminal adjudicated `not_found`
(journal `skipped=True, terminal_not_found=True`). `--readjudicate` must still reset and re-run
such a record (existing semantics preserved).

## Defect 2 — provenance warning duplication

Warnings are appended unconditionally; Entick carries 3+ identical triplets. Fix: append-if-
absent for the fixed-vocabulary warning strings (dedupe on exact text). Historical duplicates on
Entick clean up in the Defect-3 readjudication reset; do NOT mass-rewrite other records.

## Implementation — A16 `verified_off_cl` (spec: S2 § A16)

1. **Schema:** add `verified_off_cl` to the `_schema.json` status enum; allow
   `identity_method: "off_cl"`; `off_cl_links[]` entries per A16 (url, source, confirmed
   {caption, cite, court, date}, checked_date). Self-test fixtures: a valid `verified_off_cl`
   record passes; one with <2 distinct sources or null `citations.official` fails.
2. **Elevation path:** `--elevate-off-cl <record_id> --adjudication <file>` — takes an
   orchestrator-prepared adjudication JSON (citations, off_cl_links, trail), verifies the A16
   shape (≥2 distinct whitelisted sources, official cite non-null), resets the churned shell
   (clearing duplicated warnings), writes the elevated record, journals the adjudication. The
   builder NEVER self-elevates: no adjudication file, no elevation.
3. **Treatment/progeny stance** per A16: CL-silent; `progeny.count_source: "off_cl_na"`.
4. **Note for the Method-6 lint builder** (not this fix loop): LINT-13 gains the A16 checks;
   LINT-14 (page↔record) accepts `verified_off_cl`.

## Entick readjudication (after the above lands)

Orchestrator (web lane, zero CL quota) verifies ≥2 R14-whitelisted sources confirming
caption/cite/court/date (19 How. St. Tr. 1029; 95 Eng. Rep. 807; Court of Common Pleas, 1765-11-02)
and prepares the adjudication file. **Whitelist caveat:** R14's list (Justia, Google Scholar,
Cornell LII, official court/reporter site) is US-centric; if two conforming sources cannot be
found for an English 1765 case, do NOT stretch a source to fit — surface a named whitelist-
extension decision to the user at the gate (e.g. BAILII as official-reporter-equivalent for
English cases) before elevating. Expected resting state: Entick `verified_off_cl`, cluster_id
null, warnings deduped, churn gone (Defect-1 skip active for any future terminal not_found).

## Acceptance

Self-test suite green + new fixtures (terminal-skip; dedupe; schema pass/fail pairs; elevation
path happy + reject cases); a no-op session over Entick post-fix journals `skipped=True` with
zero record rewrites; resume-stability unchanged; report files touched + fixture list +
self-test tail.
