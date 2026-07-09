# S9 Thread-N doctrine-grain protocol (Fable lanes, per user D2; R5/R1 blindness)

**Lane model:** claude-fable-5 (general-purpose agents inherit the orchestrator model — the
EXECUTE wrapper assigns doctrine-grain re-derivation to Fable). **COMMIT NOTHING.** Zero CL.

## Blindness (R1/R5 — manifest-enforced by prompt + journaled; R14 audits)

A doctrine lane derives, for each assigned `type: doctrine` page topic, the case-set + split
calls the topic SHOULD carry — with NO access to:
- the doctrine page itself (`content/**` except `content/cases/` identity headers is OFF-LIMITS),
- `_run/s9/thread-P.json`,
- lake JUDGMENT fields: `treatment`, `progeny` — and page frontmatter entirely.
ALLOWED inputs (the manifest): the topic title + the S3 registry rows for that topic
(`_overhaul2/points/registry.yaml` — node ids, statements, home_page NAMES only as topic
identifiers) · lake `identity` blocks (caption, court, year, cluster) + `citations` ·
cached opinion text `/Users/johngalt/cssi-lake/cache/text/<opinion_id>.txt` (resolve via the
lake identity `lead_opinion_id`/`sibling_ids`). Write your manifest row FIRST to
`_run/s9/manifests/doctrine-<lane-id>.json`: {lane_id, lane_kind: "doctrine-rederive",
model: "claude-fable-5", doctrine_ids[], files_disclosed_pattern, fields_excluded, issued_at}.

## Per-topic output (append to `_run/s9/thread-N-doctrine.jsonl`)

{doctrine_id, title, lane, model, derived: {case_set: [{caption, cluster_id, role_claim:
anchor|rule-bearing|limiting|progeny|foil, one_line_basis}], splits: [{question,
positions: [{circuit_or_court, case, direction}], confidence}], negative_notes:
["no SCOTUS holding on X"...]}, method_note, derived_at}
Derive from the OPINIONS (cached text: holdings, what they cite, what they limit) — not from
memory alone; every case_set row needs a text-grounded one_line_basis. Where cached text is
missing for a candidate, say so (candidate_unverified: true) rather than dropping silently.
Work topic-by-topic; 15–25 cases per topic is typical; include only cases the TEXTS justify.

## Skip-disposition rows (orchestrator adjudication 2026-07-09)

Worklist rows with type ≠ doctrine (index/hub/craft/practical/reference/untyped, 36 rows)
are NOT re-derivation surfaces — emit {doctrine_id, disposition: "skip:not-a-doctrine-
conclusion-surface", covered_by: "panel+lints+index-checks"} rows so the no-regression floor
stays whole. The assigned lane for batch 0 emits these.
