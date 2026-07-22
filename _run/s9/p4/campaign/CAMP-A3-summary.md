# CAMP-A3 — summary (LINT-11 P4-authored reword + legacy design)

Packet: **CAMP-A3** · lane `CAMP-A3` · model `claude-opus-4-8` · branch `overhaul2/execute`
Authority: RULING **P4-16(d)** · S1 A2 · WRITE-SCOPE `content/` (P4-authored token lines) + `_run/s9/p4/`.
Deliverables: `CAMP-A3-fixes.jsonl` (197) · `CAMP-A3-legacy-design.md` · `CAMP-A3-summary.md`.

## Before / after (LINT-11 over `content/`)

| | HIGH highs | S9 tokens | co-located P4 tokens |
|---|---|---|---|
| Before | **405** | 165 | L2×4, L4×4, R13×4, N5×1 |
| After  | **227** | 0 | 0 |
| Removed | **178** | 165 | 13 |

405 → 227. Removed = 165 `S9` (the ruling's "165 P4-authored") + 13 pipeline tokens co-located on
the 5 mixed P4-authored sentences. Every legacy token class (`S7`/`S2`/`S6`/`S3`/`R5`/`pending Cl`/
`wrapper`/…) is **byte-for-byte unchanged** — legacy was not mass-edited. Lint self-test: **PASS**
(lint source untouched). Residue guard after apply: **0** (`T3/P4-12`, `, T3)`, `until S9 promotion`,
`pending S9`, `fix gate (R13) and S9`, `developments rule (N5)` all gone from content).

The nominal target was `~405 → ~240`. Actual remainder **227** = 240 − 13; the 13-row delta is the
`L2`/`L4`/`R13`/`N5` tokens that sit **on** the 5 P4-authored S9 sentences and cannot be left as
half-stripped prose — they are reworded under the task's "same for any other P4-authored token line".

## Partition & deterministic coverage

**The T3/P4-12 retirement tokens are NOT lint-caught** (`T3`,`P4-12` match no class-1 pattern:
`T`/`P` ∉ `[LNRG]`). Cross-check confirmed: FIX-T3 footprint (180 lines) ∩ 405 lint highs = **0**.
So the 405 lint highs and the retirement-note template are two disjoint P4-authored surfaces, exactly
per P4-16(d)'s two clauses ("165 P4-authored … tokens" + "retirement-note template … amended").

### Partition (i) — P4-AUTHORED — reworded now (197 fix rows / 195 lines / 172 files)

| Rule | Surface | Find → Replace | Lines | Lint-caught |
|---|---|---|---|---|
| R1 | ⚪ status/banner | `until S9 promotion` → `until machine verification is complete` | 154 | yes (154 S9) |
| R2 | treatment line | `pending S9` → `awaiting machine verification` | 7 | yes (7 S9) |
| R3a/R3b | recent-dev methodology | full-sentence reword (drops `serial CL, L2/L4 … fix gate (R13) and S9`) | 3 + 1 | yes (4 S9 + 4 L2 + 4 L4 + 4 R13) |
| R4 | methodology (6A) | `…-developments rule (N5).` → `…-developments rule.` | 1 | yes (1 N5) |
| R5 | Sources retirement | `retired per T3/P4-12` → `retired pending official-reporter pagination` | 3 | no |
| R6 | Sources retirement | `retired T3/P4-12` → `retired pending official-reporter pagination` | 26 | no |
| R7 | Sources conversion | `paraphrased, T3)` → `paraphrased)` (Lange) | 1 | no |
| R8 | Sources conversion | `conversion, T3)` → `conversion)` (Byrd) | 1 | no |

- (i-a) **S9 lines: 165/165 covered** (154 R1 + 7 R2 + 4 R3 = 165; R4 adds the co-located N5 on the
  6A line). One consistent "machine verification" template; methodology sentences reworded whole.
- (i-b) **Retirement/conversion notes: 30/30 covered** (29 RETIRE + 1 Byrd; Lange carries R5+R7).
  All 28 host files confirmed in the FIX-T3 footprint. Pincite numbers and all legal content
  preserved — only the `T3/P4-12` identifier phrase swapped for the plain-English reason.
- **Star-refetch provenance:** 0 occurrences in `content/` (they live only in `_run/.../star-refetch/`
  + FIX-T3 evidence). Nothing to reword.
- **"S7 research annex §11" retirement line:** 0 occurrences in `content/` (already retired per
  P4-12(d); grep `annex` = 0 files). Nothing to reword.

### Partition (ii) — LEGACY — design report only, **no edits** (see `CAMP-A3-legacy-design.md`)

227 remaining highs = **14 semantic false positives** the exclusion-list design intends excluded
(`pending Cl`×8 = "Spending Clause" regex-word-boundary defect; `wrapper`×4 = physical cigar wrapper;
`split from`×1 = legal circuit split; `placeholder`×1 = pedagogical) + **213 genuine leaks** (B1
root-index roster 123/41; B2 Sources pin-conversion provenance 77/64/59 — incl. the deferred `R5 T3`
family; B3 body-prose rule refs 11/8; B4 `No standalone case page` 2). Grounding: S1 A2 line 273/281
+ S7 R lines 138–139/253 — provenance belongs in HTML comments / frontmatter / S9 ledger / research
annex, never rendered prose; **no spec sanctions a Sources-note spec-ref** (grepped all 9 specs).

## Method

`python3 scripts/lint/lint11_pipeline_vocab.py content` (before → 405, after → 227). Partition by
matched-token histogram cross-referenced against the FIX-T3 footprint (`out/FIX-T3-fixes.jsonl`) and
full-line context. Applier: deterministic ordered string-replacement, one fix row per occurrence
(before/after ±40-char context), post-apply residue guard. Every replacement string pre-checked
against all five S1 A2 classes so no new banned token is introduced (confirmed: after-lint shows
zero new tokens; only removals).

## For the orchestrator (ambiguities / decisions taken)

1. **Scope call on co-located tokens.** The 4 recent-developments methodology sentences and the 6A
   `(N5)` are legacy-token-bearing but sit on P4-authored S9 sentences; I reworded them whole (can't
   ship half-stripped prose). This is why remainder is 227, not the nominal 240. If the orchestrator
   wants the strict "165-only" count, these 13 could instead be logged to Wave B — but the resulting
   prose would leak `R13`/`L2`/`L4`/`N5` mid-sentence. Recommend keeping as done.
2. **`R5 T3` family deferred to Wave B (partition ii).** It contains `T3` but carries legacy `S7`/`R5`
   spec-refs and is **not** in the FIX-T3 footprint (authored pre-FIX-T3), so it is legacy, not
   P4-authored. Documented as a B2 sub-class with a worked reword.
3. **Frontier-stub minor redundancy (3 lines).** `not machine-certified until machine verification is
   complete` (Al-Azzawy etc.) reads slightly redundant but is correct/clear; a future editorial pass
   could tighten to `not yet machine-certified`. Kept for template consistency.
4. **Two FP remedies exceed CAMP-A3 write-scope** (lint source): the `pending CL` word-boundary fix +
   the 5 `adjudicated_hits` seed are recommended in the design report for the lint-owner lane.
