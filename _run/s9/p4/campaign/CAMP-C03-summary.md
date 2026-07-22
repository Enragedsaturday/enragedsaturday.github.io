# CAMP-C03 — LINT-10 em-dash renovation summary

- packet: CAMP-C03
- lane: o2-execute · model: claude-opus-4-8
- spec: S1 A7/A8, RULING P4-16(e); lint `scripts/lint/lint10_emdash.py`

## Coverage
| metric | count |
|---|---|
| files in manifest | 52 |
| flagged rows (block + sentence messages) | 264 |
| distinct flagged blocks | 139 |
| blocks fixed | 139 |
| blocks escalated | 0 |
| edits applied | 143 |

Every distinct flagged block (139) is fixed; escalations 0. Edit count (143) exceeds
block count because four multi-em-dash blocks needed two edits each (Ex parte Jackson L74,
LaDuke L60, US v. Giordano L68, US v. Maez L61) plus US v. Smith (2024) L66.

## Before / after (LINT-10 highs, this file set)
| state | LINT-10 highs |
|---|---|
| before (reconstructed pre-edit) | 264 |
| after (current) | 0 |

Reconstructed by reversing this packet's edits; matches manifest `row_total` exactly.

## Technique distribution (per block, before→after em-dash count)
| before→after | blocks | dominant technique |
|---|---|---|
| 2 → 1 | 91 | appears-on separator → colon; sources separator → semicolon; keep-one split/colon/comma |
| 2 → 0 | 33 | parenthetical pair → parentheses / comma pair (doctrine #1) |
| 3 → 1 | 11 | keep the load-bearing em-dash (opener or pincite), restructure the rest |
| 4 → 1 | 2 | LaDuke L60, US v. Smith (2024) L66 |
| 4 → 0 | 2 | US v. Giordano L68, US v. Maez L61 |

Doctrine applied in order of preference: (1) em-dash pair → parentheses/commas; (2) split
at em-dash before an independent clause → period; (3) colon for elaboration/list/quote intro;
(4) keep the single most load-bearing em-dash (quote pincite `— <cite>`, or a bold-lead/status
opener) and restructure the rest. Controlled authority-weight labels ("Binding — SCOTUS" etc.),
citation text, en-dash ranges, and text inside quotations/blockquotes/[!rule] callouts were left
untouched. No em-dash inside a direct quotation was edited, so no lint-masking escalation arose.

## Recurring patterns
- Appears-on role items `- [[Page]] — *Key — Role*` → `- [[Page]]: *Key — Role*` (outer
  page/role separator → colon; the taxonomy role label kept verbatim, mirroring frontmatter `role:`).
- Sources citation lines `*Case*, cite — url — pinpoints:` → `... url; pinpoints:` (second
  separator → semicolon; the `cite — url` em-dash and all citation text preserved).
- Rule answer openers `No — the rule …` / `**Fifth Amendment** — …` → `No. The rule …` /
  `**Fifth Amendment.** …`, keeping the quote pincite em-dash.
- Status/treatment blocks: kept the `**Status: Unverified — …**` (and `**Overruled — …**`)
  bold-lead opener; restructured the trailing prose em-dashes.

## Verification
- `lint10_emdash.py` over all 52 manifest files: 0 highs (was 264).
- Full non-CL suite (`run_all.py`) over the 52 files: no NEW highs introduced by this packet.
  - Pre-existing, NOT this packet: LINT-3 `content/seizures/Traffic Stops.md:40` (a 6-case
    wall at line 40; present in HEAD baseline; my only edit to that file is a colon swap at
    line 95). LINT-30 (25) fires on the `_run/s9` ledger reconciliation invariants — not a
    content file, out of this packet's write-scope.
- No new banned lexicon; no new >3-case walls; legal meaning, emphasis, and instructor voice
  preserved (punctuation-only restructuring).

## Escalations
None.

## Outputs
- `_run/s9/p4/campaign/CAMP-C03-fixes.jsonl` (139 rows: file, line, blocks_before, blocks_after, technique)
- `_run/s9/p4/campaign/CAMP-C03-summary.md` (this file)
