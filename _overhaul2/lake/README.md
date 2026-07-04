# S2 Authority Lake

This directory is the committed source of truth for S2 authority records.
Frontmatter in `content/cases/` is a generated projection. Edit the lake, not
frontmatter, once S2 projection lands.

## Stores

1. `_overhaul2/lake/` is the versioned truth store: schema, manifest, contract
   tables, and one future `cases/<record_id>.json` per case.
2. `$CSSI_LAKE_ROOT` is the out-of-repo build store. The S2 builder defaults to
   `/Users/johngalt/cssi-lake` for this run and creates `cache/http/`,
   `progeny/`, `text/`, `journal/`, `logs/`, and `db/`.
3. `$CSSI_LAKE_ROOT/db/authority.sqlite` is derived and rebuildable. It is not a
   source of truth.

## Contract

- Record schema version is `s2.v1`; records validate against `_schema.json`.
- There is no `_denylist.json`. `_advisory.json` is non-blocking institutional
  memory for the Chatrie/Zorn namespace issue.
- The only sanctioned official-citation precedence table is
  `_reporter-precedence.json`.
- The first treatment projection is gated by `_treatment-migration.json`.
- Page-backed `record_id` values are the `content/cases/*.md` filename stems.
- Frontier stubs receive A6 ids only after identity resolution:
  `slugify(cluster.case_name)--<cluster_id>` or
  `slugify(input caption)--u<sha1[:8]>` for not-found rows.
- `--` is reserved for stubs; LINT-13 enforces no page-backed case stem contains
  that namespace marker and that manifest/record ids are globally unique.

The live CourtListener API is touched only by `scripts/s2/ingest.py` under the
single builder credential lane described by L4'. Logs never contain the token;
they contain only the consumer identity and the first 12 hex characters of the
token sha256 fingerprint.
