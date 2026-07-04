# S2 Ingest Builder

`ingest.py` builds the S2 authority lake from CourtListener REST API v4. It is
stdlib-only and owns the project token lane described by L4'.

## Paths

- Repo truth store: `_overhaul2/lake/`
- Default out-of-repo store: `/Users/johngalt/cssi-lake`
- Override store root: `CSSI_LAKE_ROOT=/path/to/cssi-lake`
- Token: `~/.config/cssi/cl-token`

The token is read at runtime only. Logs include the consumer identity and the
first 12 hex chars of the token sha256 fingerprint, never the token value.

## Sessions

Run a normal session:

```sh
python3 scripts/s2/ingest.py --session-minutes 150
```

The builder writes:

- `$CSSI_LAKE_ROOT/cache/http/<sha1(url)>.json`
- `$CSSI_LAKE_ROOT/text/<opinion_id>.txt`
- `$CSSI_LAKE_ROOT/progeny/<record-slug>.jsonl`
- `$CSSI_LAKE_ROOT/journal/s2-ingest-<run>.jsonl`
- `$CSSI_LAKE_ROOT/logs/cl-calls.log`
- `_overhaul2/lake/cases/<record_id>.json`
- `_overhaul2/lake/_manifest.json` status/count updates

`--session-minutes` exits only at a checkpoint boundary. Relaunch the same
command until the manifest shows the roster complete.

## Resume

Resume is on by default:

```sh
python3 scripts/s2/ingest.py --session-minutes 150 --resume
```

The journal is the resume source. Completed steps and completed treatment lanes
are not re-queued. Partial treatment lanes resume from the recorded cursor.
Treatment search requests are deliberately uncached; identity, cluster, progeny,
and opinion reads use the sha1 URL cache where allowed.

Use `--no-resume` only for a deliberate fresh run.

## Smoke

Run one case with the smoke budget:

```sh
python3 scripts/s2/ingest.py --smoke terry-v-ohio
```

Smoke mode selects a single manifest record by slug/title/record id and enforces
a 40-call session cap. The Chatrie guard can be exercised the same way:

```sh
python3 scripts/s2/ingest.py --smoke chatrie-v-united-states
```

## Offline Checks

Run unit checks without network or token access:

```sh
python3 scripts/s2/ingest.py --self-test
```

The self-test covers A6 record IDs, A2 reporter precedence including ties,
A4 binding lane filters for SCOTUS/CoA/district/state, token-bucket arithmetic,
and journal resume semantics for completed lanes.
