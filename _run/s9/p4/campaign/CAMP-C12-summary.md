# CAMP-C12 — LINT-10 em-dash renovation (S1 A7/A8, RULING P4-16(e))

Lane: claude · model: claude-opus-4-8 · packet manifest: `_run/s9/p4/campaign/lint10/C12.json`

## Coverage

| metric | count |
|---|---|
| Files assigned | 52 |
| HIGH rows assigned (manifest `row_total`) | 263 |
| — block-level HIGH rows (distinct flagged blocks) | 139 |
| — sentence-level HIGH rows | 124 |
| Blocks fixed | 139 |
| Blocks escalated | 0 |
| HIGH rows remaining (combined lint, after) | 0 |

Before → after (LINT-10 HIGH, run over the full 52-file list in one invocation):
**263 → 0.** Every assigned file returns 0 highs; `scripts/lint/lint10_emdash.py` exit 0.

Per-block detail (file, line, blocks_before/after, technique) in
`_run/s9/p4/campaign/CAMP-C12-fixes.jsonl` (139 rows, one per block).

## Block-budget outcome

- 139 blocks brought within budget: 43 taken to 0 em-dashes, 96 reduced to exactly 1.
- Pre-fix block em-dash counts matched the manifest exactly: 132 blocks @2, 6 @3, 1 @4.

## Techniques (by block)

| technique | blocks |
|---|---|
| T2 sources — `cite — URL — pinpoints` → `cite — URL. Pinpoints:` (period split) | 38 |
| T1 appears-on — inner role em-dash → colon (`*Key — Sub*` → `*Key: Sub*`) | 36 |
| prose parenthetical pair → parentheses (#1) | 27 |
| prose parenthetical pair → commas (#1) | 16 |
| keep single load-bearing em-dash (#4) + neutralize the rest (3–4-dash blocks) | 7 |
| status-banner em-dash → period split (`Status: Unverified — …` → `… . …`) | 5 |
| prose single em-dash → comma (#1) | 5 |
| prose elaboration / list-intro em-dash → colon (#3) | 4 |
| sources intra-parenthetical em-dash → semicolon | 1 (Marcus L74 counted under keep-load-bearing) |

T1 colon form (`*Key: Sub*`) confirmed by coordinator as the C01/C02/C06 corpus
precedent; matches the committed C08/C10 sibling packets.

## Constraints honored

- No text inside direct quotations, blockquotes, `[!rule]` callouts, inline code, or
  controlled authority-weight labels (`Binding — SCOTUS`, `Persuasive only — non-precedential`,
  etc.) was edited. Em-dashes masked by those carve-outs were left intact — e.g. the
  reproduced source em-dash in Rochin's Sources note (`"stomach's contents—this course"`,
  inside quotes) and the quoted `totality of the circumstances—the whole picture—` in Cortez.
- En-dash ranges (page/date/reporter, e.g. `726–727`, `16–17`, `2061–2062`) untouched (A7).
- Where a block held 3–4 em-dashes, the single most rhetorically load-bearing em-dash was
  kept (doctrine #4) and the others restructured, rather than purging all.
- Legal meaning, emphasis, and instructor voice preserved; no new banned lexicon and no
  >3-case walls introduced (punctuation-only rewrites).

## Escalations

None. No block had all its em-dashes inside quotations (the only escalation trigger in the
brief), so no lint-masking escalation rows were filed.

## Write scope

Edits confined to the 52 manifest files under `content/cases/` plus these two artifacts under
`_run/s9/p4/`. Per-file read-modify-write only; no `git stash`/`checkout` of shared paths
(concurrency addendum).
