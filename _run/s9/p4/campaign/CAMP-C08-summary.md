# CAMP-C08 — LINT-10 em-dash renovation (packet summary)

- packet: CAMP-C08
- lane: EXECUTE fleet worker / model claude-opus-4-8
- brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (S1 A7/A8, RULING P4-16(e))
- manifest: `_run/s9/p4/campaign/lint10/C08.json`

## Coverage
- files assigned: 51 (all `content/cases/*.md`)
- lint HIGH rows assigned (manifest row_total): 263
- flagged blocks (distinct file+line): 136
- blocks fixed: 136
- blocks escalated (lint-masking / quote-only): 0
- writes confined to manifest files + `_run/s9/p4/` (WRITE-SCOPE honored; per-file read-modify-write, no stash/checkout)

## Result (before -> after)
- HIGH em-dash violations over the 51 files: 263 -> 0
- verification via `scripts/lint/lint10_emdash.py <51 files>`: exit 0, `0 violation(s): 0 high, 0 medium, 0 low`
- every fixed block: em-dash count >=2 before -> <=1 after (invariant checked, 0 violations)
  - after-count distribution: 1 em-dash retained in 89 blocks, 0 in 47 blocks
  - before-count distribution: 128 blocks had 2, 8 blocks had 3

## Techniques (doctrine #1-#4)
| n | technique |
|---|---|
| 42 | sources line: cite/URL em-dash -> period split (keeps `URL — pinpoint`) |
| 38 | prose parenthetical em-dash pair -> parentheses |
| 31 | appears-on: inner role em-dash -> colon (outer `[[Page]] — *role*` kept) |
| 15 | prose parenthetical em-dash pair -> commas |
|  2 | prose quote-intro em-dash -> colon |
|  2 | prose appositive em-dash -> comma |
|  1 | prose answer em-dash -> colon |
|  1 | prose mid-sentence citation em-dash pair -> parentheses |
|  1 | prose aside em-dash -> parentheses |
|  1 | prose em-dash -> sentence split (period) |
|  1 | prose aside em-dash pair -> colon + comma |
|  1 | prose contrast em-dash -> comma |

## Hard-constraint compliance
- No edits inside direct quotations or blockquote/[!rule] lines; controlled authority-weight
  labels ("Binding — SCOTUS" etc.) and citation text untouched.
- En-dashes in ranges (e.g. `281–282`, `35–37`, `Miranda–Edwards–Minnick`) left intact.
- Unverified-status banners ("Status: Unverified — ...") kept as the single retained em-dash;
  only the neighboring prose em-dashes were renovated.
- Legal meaning, emphasis, and instructor voice preserved; no new banned lexicon, no >3-case walls.

## Artifacts
- `_run/s9/p4/campaign/CAMP-C08-fixes.jsonl` (136 rows: file, line, blocks_before, blocks_after, technique)
- `_run/s9/p4/campaign/CAMP-C08-summary.md` (this file)
