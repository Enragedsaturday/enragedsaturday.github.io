# Builder work order — PACKET A execution (re-keys + alias-folds), 2026-07-06

User approved all four packet-A groups (`_run/s6-fabrications.md` dispositions section;
`_run/o2-execute/DISPOSITIONS-2026-07-06.md`). This session executes Groups 1+2. Group 3
(West/White removals) is ORCHESTRATOR scope — do not touch those two rows beyond what §Scope
says. Repo: /Users/johngalt/Projects/cssi-quartz, branch overhaul2/execute (start from HEAD;
commit nothing — the orchestrator commits at the gate).

## Scope

The re-key universe = every manifest row with `status: fabrication_suspected` (25 at HEAD)
EXCEPT `united-states-v-west--10653830` and `united-states-v-white--10349533` (approved
removals, orchestrator lane) → **23 rows**. Ground truth is the manifest, not this prose:
enumerate at start, report the roster. Cross-reference each row to its dual-leg web
verification: `_run/o2-execute/s6-webverify-codex.jsonl` (full keys: caption, citation,
court, date, docket, sources) ∥ `s6-webverify-claude.jsonl` + `s6-webverify-claude-batches.jsonl`
(independent leg). A row with no webverify match: ESCALATE in the report, do not guess keys.

## Step 1 — land the recovered keys (offline, journaled)

The 23 rows are thin caption-only seeds; the manifest roster keys lack the
docket/citation the ladder needs. Add a bounded offline step (new flag, e.g.
`--apply-web-keys <jsonl>`, self-tested + fixtured like every ingest.py surface):
- Input: a small JSONL you assemble from the webverify legs — one row per record_id:
  `{record_id, expected_citation, docket, year, court, date_decided, source: "s6-webverify
  dual-leg 2026-07-06"}` . Where the two legs disagree on a key, STOP for that row and
  escalate in the report (the orchestrator adjudicated 4 divergences already — only
  arkansas-v-sanders should need special handling; see below).
- Effect: updates ONLY those roster search-key fields on the named manifest rows
  (fabrication_suspected rows only — refuse any other status), journals per-row
  `{step: "packet-a.web-keys", before, after, provenance}`. Record ids untouched.
- **arkansas-v-sanders--10601315**: the stub matched the WRONG case entirely (2024
  Gov.-Sanders prison-board suit, cluster 10601315). Real case: Arkansas v. Sanders,
  442 U.S. 753 (1979), docket 77-1497 (overruled by California v. Acevedo — dead-law
  history framing per D2). Apply keys for the REAL case; the readjudication reset wipes the
  wrong-cluster identity; expect the ladder to land 442 U.S. 753's cluster. If the terminal
  record_id suffix should change with the corrected cluster, follow the same rename+journal
  path the F-S2-33 Timbs correction used.
- **Small/Lyle/Moore-Bush cluster-id nuances** (packet A Group-4 note): artifact cluster ids
  differ between sources (e.g. Small 10593041 vs 4684957 — cluster-vs-sibling id). Do not
  pre-resolve; let the ladder terminate authoritatively and report which id won per row.

## Step 2 — readjudicate through the serial lane (CL, paced)

`--readjudicate-file` the 23 (single serial lane, pacing ≤14/min as every prior session;
`--session-minutes 90`, resumable). Expected: rows land `verified_identity` (or an honest
terminal state with the full rung trail — report any). Zero new fabrication_suspected
without escalation. Watch-list framing notes to carry into the journal (no page work here):
trupiano = dead law (overruled by Rabinowitz); state-v-weaver framing caution (holding is
scope-of-consent); milam-v-united-states = the 1924 4th Cir. case (conflation hazard vs the
1974 9th Cir. Milam); united-states-v-daniels = 10th Cir. 2024, NOT the 5th Cir. Bruen
Daniels.

## Step 3 — alias-folds (Group 2; ledger/lake only, no content/ writes)

Follow the s6-dedupe-pointer pattern journaled at S2 close (Chatrie page/stub):
1. **morse-v-french** → alias-fold into the French v. Merrill litigation row (15 F.4th 116
   (1st Cir. 2021), cert. denied sub nom. Morse v. French, 143 S. Ct. 301 (2022)). Ledger
   alias state + journal; the Morse caption survives as the cert-posture reference at
   mention sites (S7 prose concern, not yours).
2. **carroll-v-carman ↔ carman-v-carroll** → one litigation: SCOTUS per curiam Carroll v.
   Carman, 574 U.S. 13 (2014) is the page-candidate row; the 3d-Cir. caption (749 F.3d 192)
   alias-folds into it.
3. **united-states-v-chatrie stub** → fold into the existing Chatrie v. United States PAGE
   row's history thread (the stub's cluster 10881683 is the SCOTUS merits; the 4th-Cir. en
   banc below (136 F.4th 100) enters as Lower-court developments at authoring). Terminal
   state `folded-alias` with pointer; no separate page candidate survives.

## Acceptance / report

Self-test green + new fixtures for the key-landing step; per-row table (record_id · old
status · keys applied · terminal status · cluster id · calls); alias-folds journaled with
pointers; cumulative CL calls + pacing evidence (zero 429s expected); manifest distribution
after (fabrication_suspected should be exactly 2: West + White, awaiting orchestrator
removal). Escalations listed explicitly. Write the report to
`_run/o2-execute/PACKET-A-REKEY-REPORT.md`.
