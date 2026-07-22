# CAMP-WB2 summary — LINT-11 Wave B, class B2 (Sources-note pin-conversion provenance)

Lane `CAMP-WB2` · model `claude-opus-4-8` · branch `overhaul2/execute`
Governing law: **S1 A2** (pipeline-vocab ban; provenance → HTML comment / frontmatter / S9 ledger,
never rendered spec-refs) · `scripts/lint/lint11_pipeline_vocab.py` · design report
`_run/s9/p4/campaign/CAMP-A3-legacy-design.md` (5 worked reword shapes).

## Result

| | HIGH violations |
|---|---|
| Before (`lint11 content`) | **227** |
| After | **152** |
| Removed by CAMP-WB2 | **75** (token-diff: removed 75 / added 0) |

Self-test `lint11 --self-test` = **PASS** (lint source untouched). No new violations introduced
(added=0). `152 = 123 B1 (index roster) + 14 FP + 13 B3 + 2 B4` — every survivor is a non-B2 class
owned by another lane; **zero B2 rows remain**.

## Coverage of the B2 row list (deterministic)

62 rendered Sources/provenance lines across **57 files**; **75 flagged tokens** removed
(S2×44, R5×14, S7×11, S6×2, R14×1, S1×1, L6×1, SR-5×1 — matches the design report's B2 token tally
exactly, minus the 2 R15 rows re-routed to B3, see boundary note). Full per-row record with
before/after in `CAMP-WB2-fixes.jsonl`.

| Subclass | Rows | Disposition | Reword template |
|---|---|---|---|
| **S2-A1** slip-style pin | 29 | reword | `…so the pin is slip-style per S2 A3` → `…so the pin is slip-style` (reason already stated in prose; drop dangling spec-ref) |
| **S2-A2** slip-precedent trailer | 9 | reword | `…no reporter cite assigned yet (S2 A3 slip precedent)` → `…no reporter cite assigned yet` (trailer is redundant of the plain sentence; drop) |
| **S2-special** | 6 | reword | Carter/Lewis: `the slip form is per S2 A3` / `(S2 A3 slip render)` → `so the pin cites the slip opinion`. Youngblood: build-jargon parenthetical (`the lake identity year…; flagged for S2`) → `the "(1989)" parenthetical follows CourtListener's recorded filing-date year`. Nance/Tanzin/Uzuegbunam: drop `; cluster <id> → opinion <id>` + `per S2 A3`, keep `slip-only — …page equality not asserted` |
| **R5/S7 T3-family** | 15 | reword | `post-2020 slip pins paraphrased per S7 R5 T3` → `…paraphrased rather than page-cited`; `pinpoint: 462 — CAP star page verified, S7 R5 T1` → `…verified`; `(case-level cite: R5 T3)` → `(case-level cite; interior pinpoints paraphrased rather than page-cited)`; EA108 `current-Term slip pins stand, S1 R14 / S7 R5 T4` → `current-Term slip pins stand`; EA115 drop `owed S6 home_row discharged` |
| **S6 status table** | 1 | reword | Suing Federal Officers: `Slip-only; treatment pending S6 promotion.` → `Slip-only; later treatment not yet catalogued.` |
| **pure-provenance → HTML comment** | 2 | html-comment | Michigan v. Jackson (`(Cluster/opinion located via the L6 ladder…)`) and Gastiaburo (`(Lead opinion id 6929715; …unrelated opinion id — see SR-5 note.)`): whole note is build lookup/id-disambiguation with zero reader value → relocated verbatim into an inline `<!-- provenance: … -->` comment on the same line (lint masks comments; audit trail preserved, not destroyed) |

All rewrites preserve every element of citation content — party names, reporters, pinpoints,
holdings, court, docket numbers, and the `…string-matched to the CL opinion text 2026-07-07`
verification dates. No legal text around the notes was altered.

## Boundary decisions (for orchestrator adjudication)

1. **The 2 R15 "treatment audit" rows are B3, not B2 — not touched.** The design report's B2 token
   tally lists `R15×2`, but all six live R15 hits (Ashcraft, Brendlin, Jacobson, Kuhlmann, Taylor,
   Van Leeuwen — all at `## Treatment & subsequent history`) are body-prose treatment-audit
   narrative, neither Sources-line nor pin-conversion. Report §4 itself files "R15 treatment audit
   narrative refs" under **B3**. Routing them to B3 (the editorial-pass lane) avoids scope collision.
   This is the entire gap between the report's "77 rows / 64 lines / 59 files" and my
   **75 tokens / 62 lines / 57 files**; after-count is 152 rather than 150 for exactly this reason.
2. **FP tokens co-located on B2 lines left untouched.** Landor:79 keeps its `pending Cl`
   (from *S​pending Cl​ause*, the class-3 regex defect the report routes to a lint-owner word-boundary
   fix); I removed only the `S2` spec-ref on that line. Loines/Christensen keep their `wrapper`/`R11`
   FP/B3 hits on other lines.
3. **Internal CourtListener cluster/opinion integer IDs** inside mixed-value notes (Nance, Tanzin,
   Uzuegbunam, Community Caretaking:128) were dropped in the reword rather than preserved — they are
   pure DB keys (the cluster id is already in the bullet's URL; provenance lives in the S9 ledger).
   Whole-note pure-provenance (Jackson, Gastiaburo) was **relocated** to an HTML comment instead of
   dropped, per the task's move-to-comment path.

## Residue (not CAMP-WB2's — for reference)

The 152 survivors: **B1** index-roster provenance (123, `content/index.md`), **FP** semantic
false-positives (14: `pending Cl`×8, `wrapper`×4, `split from`×1, `placeholder`×1 — allowlist/regex
lane), **B3** body-prose rule refs (13, incl. the 6 R15 treatment-audit rows), **B4**
`No standalone case page` (2, Entrapment:100–101). None are B2.

## Artifacts
- `_run/s9/p4/campaign/CAMP-WB2-fixes.jsonl` — 62 rows (file, line, flagged_tokens_removed,
  disposition, technique, before, after; `{lane, model}` on every row)
- 57 content files edited (see fixes.jsonl `file` column)
