# S2 fix work order — F-S2-27 (session-15 crash: frontier record filename overflow)

Orchestrator adjudication 2026-07-06. Session 15 ended early (225 calls) on
`OSError [Errno 63] File name too long` writing the frontier stub for
`UNRESOLVED:arkansas-v-sanders`: the top search candidate was the 2024 Arkansas state case
"Sarah Sanders, in her official capacity as Governor of Arkansas, … v. Arkansas Board of
Corrections …" (cluster 10601315), and the resolved-stub filename was built from the slug of
that FULL ~300-char canonical caption + cluster id — beyond the 255-byte filename limit at the
`.tmp` write. (The wrong-candidate match itself is NOT in scope: with the write fixed, the row
lands per existing fail-closed logic — likely fabrication_suspected, the honest S6-adjudication
state for a caption-only seed. Note the crash left an untracked partial
`cases/UNRESOLVED:arkansas-v-sanders.json` — your fix should leave the row resumable and the
partial file consistent or replaced.)

Context, no action needed: `alasaad-v-mayorkas--u782a2d04` not_found is adjudicated TRUE — CL
indexes the whole litigation as "Alasaad v. Wolf" (cluster 4855246, already verified_identity
via the sibling seed row); caption-variant dedupe is S6's class.

## F-S2-27 — bound frontier record ids/filenames to the spec's stub scheme

Per the spec's stub record_id scheme, stub ids derive from the INPUT caption
(`slugify(input caption) + "--" + cluster_id`, or `+ "--u" + sha1(normalized roster key)[:8]`
for not_found) — the input caption is the roster key ("arkansas-v-sanders"), NOT CL's canonical
caption. Fix the resolved-stub path to use the input-caption slug, and additionally hard-cap
the slug component of ANY record filename at 100 chars (defense in depth; the id suffix —
cluster id or --u hash — always preserved intact). Atomic .tmp writes inherit the bound.

Fixtures: a frontier stub whose canonical caption is 300+ chars gets record_id
`<input-slug>--<cluster_id>`, filename ≤ 120 bytes, .tmp path valid; record_id still parses to
caption+id form (spec check); not_found stub ids unchanged; existing frontier fixtures
unchanged.

## Acceptance

- Full self-test suite green + new fixtures.
- CONFIRM (by code inspection, stated in the report): the interrupted
  `UNRESOLVED:arkansas-v-sanders` row re-runs on normal resume next session WITHOUT a manual
  readjudicate (it checkpointed status=interrupted / reason=unhandled_exception). If it would
  NOT re-run automatically, add interrupted-status recovery to the resume path — scoped
  strictly to that.
- Resume-stability for completed records unchanged.
- Report files touched + fixture list + self-test tail + the resume confirmation.
