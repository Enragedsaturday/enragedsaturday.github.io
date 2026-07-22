# CAMP-C09 — LINT-10 em-dash renovation summary

- **Packet:** CAMP-C09 (LINT-10 em-dash budget, S1 A7/A8, RULING P4-16(e))
- **Lane / model:** claude / claude-opus-4-8
- **Files in manifest:** 51 (50 case pages + `content/cases/index.md`)
- **Write-scope honored:** only manifest files + `_run/s9/p4/` (per-file read-modify-write; no `git stash`/`git checkout`; concurrent-fleet-safe)

## Coverage

| metric | count |
|---|---|
| Manifest HIGH rows assigned (`row_total`) | 263 |
| — block-budget rows | 140 |
| — sentence-budget rows | 123 |
| Unique flagged blocks (file,line) | 140 |
| Blocks fixed | 140 |
| Blocks escalated (quote-masking) | 0 |
| Blocks NOT-FIXED (after > 1 em-dash) | 0 |

## Lint before / after (full manifest sweep, `scripts/lint/lint10_emdash.py`)

| | HIGH rows |
|---|---|
| before | 263 |
| after | **0** |

Every file independently re-linted to 0 high/0 medium/0 low.

## After-state of fixed blocks

- 48 blocks reduced to 0 em-dashes.
- 92 blocks reduced to exactly 1 em-dash (the single load-bearing dash kept per doctrine #4 — recurring `**Status: … —**` treatment lines, the `quote." — <pincite>` citation-attribution dash, and the `cite — URL` Sources separator).

## Technique distribution (one per block)

| technique | n | note |
|---|---|---|
| paren-pair | 49 | em-dash parenthetical pair → parentheses (doctrine #1) |
| source-paren | 34 | Sources line `cite — URL — pinpoint` → `cite — URL (pinpoint …)` |
| role-paren | 27 | "Appears on" role compound `*Key — X*` → `*Key (X)*` |
| comma | 11 | single dash → comma (answer opener / participial / appositive) |
| role-comma | 6 | role compound → comma where a nested paren would result (`*Key, X (…)*`) |
| colon | 4 | dash introducing elaboration → colon (doctrine #3) |
| source-split | 3 | Sources line second dash → sentence split (`… URL. Pinpoint …`) |
| semicolon | 2 | dash → semicolon between related clauses |
| paren-pair-x2 | 2 | two parenthetical pairs in one block (Peters L60, Grubbs L60) |
| comma-pair | 1 | parenthetical pair → comma pair (Alasaad L66) |
| paren-pair+comma | 1 | pair→parens plus a stray dash→comma (Padilla L58) |

## Hard-constraint compliance

- **No edits inside quotations/blockquotes.** Masked em-dashes inside direct quotes (e.g. Roberson L53, Goldey L60 `override'—…—state`, Nance L59, Yarborough L57) were left untouched; only unmasked prose dashes were restructured. No escalation was required because in every flagged block at least one countable em-dash sat outside the masked spans.
- **Controlled authority-weight labels untouched.** `Binding — SCOTUS`, `Binding in-circuit — …`, etc. never edited. The countable dash that precedes such a label (`*(as of …)* — **Binding …**`) was already within budget and not flagged.
- **Citation text preserved.** Reporter/volume/page and en-dash page-ranges (e.g. `548–549`, `623–624`, `513–515`) left intact; only field-separator/pinpoint punctuation was moved.
- **Frontmatter `holding:` strings** were not among the flagged blocks in this packet (none flagged); none edited.
- **No new lint violations introduced** — punctuation-only rewrites; no new banned lexicon, no >3-case walls; legal meaning, emphasis, and instructor voice preserved.

## Notes / judgment calls

- **Treatment header lines** (Frank L51, Robbins L53): the non-allowlisted string `**Overruled — rendered as history (…)**` carries a countable dash; kept that dash and converted the trailing ` — overruled by …` to `, overruled by …`.
- **`**Status: Unverified — …**` pages** (Alasaad, Goldey, Owen, Burgess, Chavez, Liddell, Lyle, Small, Manuel, Nance): kept the status-line dash uniformly and repaired the block's other dash, so the recurring rendered pattern stays consistent across the corpus.
- Manifest predicted a block-only row on a few lines whose two dashes actually straddle a `a.m.`/`S. Ct.` sentence boundary (Small L61, Manuel L79); fixes verified against live lint regardless of the predicted sentence-row.

## Outputs

- `_run/s9/p4/campaign/CAMP-C09-fixes.jsonl` (140 rows; `{lane, model}` = `claude`/`claude-opus-4-8`)
- `_run/s9/p4/campaign/CAMP-C09-summary.md` (this file)
