# S2 builder work order (Wave 1 — Codex lane)

The law: `_overhaul2/specs/S2-authority-database.spec.md` (R1–R15 + Amendments A1–A15) +
`_overhaul2/CL-DATA-INVENTORY.md` + `docs/STANDARDS.md` (L4′, SR-6, §3.1/§3.2). This work order
condenses the operative constraints; on any conflict the spec wins. Orchestrator = the EXECUTE
thread; builder = Codex gpt-5.5 xhigh.

## Environment facts (EXECUTE-time, journal-worthy)

- **Pool root:** `CSSI_LAKE_ROOT=/Users/johngalt/cssi-lake` (env-overridable constant per A10).
  The spec's `/Volumes/AIStore2/cssi-lake` is TCC-blocked this run (journal: Wave-0 deviation).
  Dirs exist: `cache/http/`, `progeny/`, `text/`, `journal/`, `logs/`, `db/`.
- **Token:** `~/.config/cssi/cl-token` (mode 600). The builder lane EXCLUSIVELY owns it (L4′).
  Every logged call records consumer identity + credential fingerprint (sha256 of token, first 12
  hex chars — never the token itself).
- **Roster seed (A12):** 457 = `content/cases/*.md` stems · no-page roster =
  `python3 _overhaul2/scripts/audit_cases.py --format json` (89 rows; §c placeholders excluded by
  the script; `LLC v. John Doe` row = ignore per S6-SEED §c).
- **Rate:** token-bucket ≤14 req/min + jitter; ~1,000/hr ceiling; backoff on 429/5xx;
  `analyze_citations` ≤60/min with job_id/resume.

## Deliverable 1 — lake scaffold (Method step 1)

`_overhaul2/lake/`: 
- `_schema.json` — JSON Schema for `s2.v1` (R1 blocks: identity · citations · pinpoints ·
  treatment · progeny · off_cl_links · provenance; top-level `schema_version`, `status` enum
  {draft, under_review, verified, verified_identity, not_found, fabrication_suspected, blocked};
  `stub: true` for frontier stubs (A6); optional `pinpoints[].fragment` +
  `fragment_validated_at` (A14); `pinpoints[].pinpoint_status ∈ {star-verified, slip-only}` (A3);
  treatment block per R5 (field_i_validity enum, as_of_content, as_of_treatment, composite_basis,
  composite_basis_ref (A8), varies_by_point, point_overrides[] with s3_binding_status, edges[]
  with field_ii/field_iii); progeny per R4/A5 (indexed_citing_opinions + count_source +
  per_sibling + complete_query + citation_count); per-field provenance on judgment fields (R8).
  Schema asserts: no `content/cases/` stem contains `--`; record_id global uniqueness (A6).
- `_advisory.json` — A1's namespaced advisory notes (cluster 10881683 Chatrie MUST-ingest, cluster
  10813527 Zorn MUST-ingest, opinion 10881683 Harmon valid-unrelated, opinion 10813527 Strike 3
  valid-unrelated, with the O1 root-cause note). NON-BLOCKING. No `_denylist.json` anywhere.
- `_reporter-precedence.json` — A2's committed precedence table (SCOTUS: U.S. > S. Ct. > L. Ed.;
  CoA: F. chain; district: F. Supp. chain; state: official > regional > other), seeded from
  Bluebook T1.
- `_treatment-migration.json` — A13's mechanical encoding of S1 A4 (docs/STANDARDS.md §3.2):
  good→good_law · limited→caution+override(varies) · overruled→superseded+overruled-edge ·
  abrogated→superseded+abrogated-edge · criticized→caution(default)/questioned(on-point binding).
  REVIEW reserved for (a) unmapped legacy value, (b) undeterminable edge metadata.
- `_manifest.json` — roster: 457 page stems + the S6-SEED entries (A6 stub record_ids:
  `slugify(case_name)--<cluster_id>` once resolved; `--u<sha1[:8]>` for not_found), per-case
  status + counts.
- `README.md` — store contract, the three stores, the "edit the lake, not frontmatter" rule.

## Deliverable 2 — `scripts/s2/ingest.py` (Method step 2; Python 3 stdlib ONLY)

- **Typed CL client (A1):** `get_cluster(cluster_id)` / `get_opinion(opinion_id)`; NO code path
  from a cluster id to `/opinions/`; every `get_opinion` arg traceable in the journal to its
  source array (`sub_opinions[]` | search `sibling_ids[]` | search `opinions[].id`), labeled.
- **Pacing:** token bucket ≤14/min + jitter; exponential backoff 429/5xx; hourly-ceiling guard.
- **Cache:** `sha1(url)` → `$CSSI_LAKE_ROOT/cache/http/`; identity/cluster reads cacheable;
  treatment-lane searches DELIBERATELY uncached (A9c); opinion text → `text/<opinion_id>.txt`
  (24h server cache acknowledged).
- **Journal (A9):** `$CSSI_LAKE_ROOT/journal/s2-ingest-<run>.jsonl` — per-case per-step rows;
  per-lane status `pending | partial(cursor) | complete`; session budget checkpoints (calls this
  session / cumulative / remaining vs ceiling) at start+end; `logs/cl-calls.log` with consumer
  identity + credential fingerprint per line (L4′).
- **Sessions:** `--session-minutes N` (clean exit at a checkpoint boundary when elapsed>N),
  `--resume` (default behavior: consult journal; NEVER re-run a complete lane; resume partial
  lanes from cursor; cache-hit identity steps skip network).
- **Per-case pipeline:** R2 identity (citation-disambiguated two-key: search by case_name+court,
  match by expected cite from the page frontmatter/Case Index; confirm party-name-in-text via
  lead-opinion text; four edge cases (a)–(d) with statuses + provenance.warnings) → R3 cites
  (official via `_reporter-precedence.json`; ties/unlisted → select nothing, journal,
  under_review) + pinpoint harvest from the existing page (star-verified | slip-only per A3) →
  R4 progeny (complete OR'd query; indexed_citing_opinions + count_source; full list →
  `progeny/<slug>.jsonl`) → R6 three-lane treatment (lane 1 bounded per A4:
  binding_jurisdiction_filter + stat_Published + order_by dateFiled desc + 200-cap, cap hits
  journaled; lane 2 top-25 cited; lane 3 server-side `filed_after = build_date − 3 years` (A9b,
  A11)); negative events PROPOSED (staged), only landing under S9 two-reviewer; saturation stop →
  R8 provenance stamps.
- **Frontier stubs (R11):** identity + fabrication-check + official cite + off-CL link ONLY;
  statuses verified_identity | not_found | fabrication_suspected; NO treatment/progeny.
- **Off-CL links (R14):** whitelist = Justia, Google Scholar, Cornell LII, official court site.
- **Migration gate (A13):** the projector (Deliverable 3, later step) refuses to run while any
  observed legacy value lacks a mapping entry.
- **Smoke mode:** `--smoke <slug>` runs ONE case end-to-end (Terry) with full journaling, for the
  pre-run review + live validation. Budget ≤40 calls.

## Sequencing (wave 1)

1. Codex authors Deliverables 1+2 (this order). NO live CL calls while authoring except none —
   authoring is offline; schema/scaffold from spec + inventory.
2. Orchestrator commits; 2nd Codex lane reviews READ-ONLY against the spec (pacing math, resume
   logic, typed-fetcher rule, A-amendment conformance); findings adjudicated; loop-cap-3.
3. Live smoke (`--smoke terry-v-ohio`, ~≤40 calls) under the builder token; verify record +
   journal + cache + pacing; then `--smoke chatrie-v-united-states` (the A1 must-ingest guard).
4. Full run launched as background sessions (`--session-minutes 150`), relaunched on exit until
   `_manifest.json` shows roster complete. Budget checkpoints reviewed at each relaunch.
5. Then: SQLite loader (R13 + A5/A7 meta hashes) · projector + serializer (R12, gated by A13) ·
   LINT-12/13/14 · R15 build-QA (2nd-Codex ≥1-in-10 spot-check + Claude treatment audit).

## Boundaries

- No page authoring (S6), no linking (S8), no prose (S7). Stubs stay stubs.
- The Claude MCP credential is NOT the builder's; never referenced in ingest.py.
- Writer ≠ checker: the builder never flips its own records to `verified` past the structural
  gates; R15 lanes do.
