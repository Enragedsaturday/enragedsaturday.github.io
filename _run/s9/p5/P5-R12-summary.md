# P5-R12 summary — maintenance-handoff assembly

Lane **P5-R12** · model **claude-opus-4-8** · 2026-07-22 · WRITE-SCOPE `_run/s9/p5/` only (read everything).
Spec: **S9 R12** (user D6) + **PRACTICES §6.10**. Findings-only: gate adjudication + ticket closure are the orchestrator's.

## Outputs
- `_run/s9/p5/MAINTENANCE-HANDOFF.json` — machine artifact, schema-valid, self-describing `_schema` block (49 KB; JSON round-trip verified).
- `_run/s9/p5/MAINTENANCE-HANDOFF.md` — human summary.
- `_run/s9/p5/P5-R12-summary.md` — this file.

## Deterministic coverage (row counts per section)

### (1) CL citator-alert seed list — 72 seed rows across 6 sub-blocks
| sub-block | count | source |
|---|---|---|
| marker-poll rows (incl. Carter/Noem/Lange + holcomb superseding-text watch) | 12 | `_run/s9/p4/marker-poll-p4.jsonl` |
| I4-TRIAGE watch rows | 3 | `_run/s9/p4/out/I4-TRIAGE-watch.jsonl` |
| post-build recency citers | 31 | `TW-DIFF.json#recency_triage.survivors` |
| companion Brillhart 24-13232 | 1 | TW-DIFF recency (row 14) + I1-ORCH |
| cite-pending clusters | 7 | lake (Case v. Montana, Chatrie, Zorn, Lowers, Brillhart, Eric Johnson, Wilson) |
| negative-treatment census | 18 | lake `treatment.field_i_validity` ∉ {good_law, unverified} |

Negative census by status: **superseded 7, caution 11**. Each carries case + status + limiting case(s) + scope_note.
Overlaps recorded (not double-counted): Carter/Noem/Lange ⊂ marker-poll; Chatrie/Zorn/Case v. Montana ∈ marker-poll ∩ cite-pending; companion Brillhart ∈ recency.

### (2) Dual-date decay schedule — 4 cadence buckets
| bucket | records | cadence | next re-check |
|---|---|---|---|
| A negative-treatment (G6) | 18 | 90 d | 2026-09-28 |
| B good_law treatment-dated (G6) | 440 | 180 d | 2026-12-27 |
| C content re-verify (G3/G4) | 458 | 365 d | 2027-06-30 |
| D null-treatment stubs | 214 | none (re-derive at promotion) | — |
`as_of_treatment`: 457 @ 2026-06-30, 1 @ 2026-07-03, 214 null. `as_of_content`: 450 dated / 222 null. Source: 672 lake records.

### (3) Fragment re-validation queue — 231 + 117 + Entick
| component | count | source |
|---|---|---|
| S8H-B traced fragments | 231 (230 MATCH + 1 VARIANT; G3-pass 226; 2 mismatch_pin; 3 no_pin) | `S8H-B-fragment-trace.jsonl` |
| fragment attention rows (non-clean) | 5 | (derived) |
| pin-upgrade queue rows | 117 (37 distinct cases) | `R12-pin-upgrade-queue.jsonl` |
| Entick unmonitorable note | 1 | lake (no CL cluster) + RULING P4-06 |

### (4) Deck-rebuild precondition attestation — measured PASS
57 decks · 44 distinct stems · 1,773 cards · **LINT-25 = 0 unresolved** (ran `scripts/lint/lint25_deck.py`, exit 0). Stems resolve against current pages.

### (5) Open `_review-needed/` register — 9 files
States: **RESOLVED 2** (chatrie-correction, s9-p3-promotions) · **CLOSED 2** (deepequal→A2, lint-baseline-campaign) · **OPEN 4** (lint3-chatrie tool-precision [measured-subsumed], delgado-inbox, entrap2-r7, threadN-lyle) · **STALE/no-stamp 1** (batch4-duplicate-CL-lane). Each row carries a one-line what-remains.

### (6) P5-handoff notes — 9 notes
8 explicitly requested (COH-B registry-notes **62**; placement-convention question; S1 §3.1/SD9 clarification P4-20(b); +36 LINT-7 mediums; Haynes scope_note variant; 5th-Cir Wilson caption-collision; ledger regen-durability; LINT-2 mediums census **683** across 207 files) + 1 ruling-routed addition (out-of-remit referrals, P4-09(4)).

## GH#2 filing block
Recorded in-artifact (`gh2_filing_block`): repo `Enragedsaturday/cssi`, issue #2, attach both P5 files, status PENDING — the actual post/attach happens at P6 publish per R12/R15.

## Method / notes for the orchestrator
- All counts re-derived at P5 from live sources (deck stems, LINT-25, LINT-2 re-run; lake re-scanned); no hand-typed totals.
- LINT-2 census re-measured at **683 mediums / 207 files** (vs the per-category "25" cited in CAMP-C11 — that was a single-category slice, not the corpus census).
- `lint3-chatrie-recent-dev-false-positive.md` is stamped OPEN but current `lint3_structure.py` emits **zero** chatrie/SCOTUS N5 flags (campaign rebuild subsumed them) — flagged MEASURED-SUBSUMED for the orchestrator to close.
- `coverage/_ESCALATION-batch4-duplicate-CL-lane.md` carries no closure stamp; reported STALE (informational) rather than asserting closure (writer≠checker).
- Builder script (reproducible): `scratchpad/build_handoff.py` (out-of-tree; reads sources, emits the JSON).
- Nothing in this packet edits `content/`, the lake, the registry, or any ledger.
