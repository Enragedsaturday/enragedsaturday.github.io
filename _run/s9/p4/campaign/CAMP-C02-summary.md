# CAMP-C02 — LINT-10 em-dash renovation summary

- Lane/model: `{lane: EXECUTE, model: claude-opus-4-8}`  (LINT-10 packet CAMP-C02; S1 A7/A8, RULING P4-16(e))
- Files in packet: **52**
- Manifest violation rows assigned (row_total): **264**  (distinct flagged blocks: **141**)
- Blocks fixed: **141 / 141**  → all 264 rows cleared
- Escalated (all-em-dashes-in-quotes masking question): **0**  (no flagged block had its em-dashes entirely inside quotations; the lint masks quoted em-dashes before counting, so every flagged block carried >1 countable em-dash outside quotes)
- Not-fixed / residue: **0**

## LINT-10 before / after (full packet file list)

| | HIGH violations |
|---|---|
| before | 264 |
| after | **0** |

Re-ran `python3 scripts/lint/lint10_emdash.py` over all 52 packet files: **0 highs** (0 violations of any severity). LINT-10 `--self-test`: PASS.
Per block, countable em-dashes went from 298 (sum) to 103 (sum); max after = 1 (≤1 budget satisfied for every block).

## Technique breakdown (one row per fixed block)

| technique | count |
|---|---:|
| aside->parentheses | 48 |
| inner-emdash->colon(label) | 33 |
| pinpoint->parenthetical | 27 |
| emdash->comma | 6 |
| split-sentence | 6 |
| emdash->colon | 5 |
| aside->commas | 4 |
| emdash->semicolon | 4 |
| emdash->parenthetical(short-cite) | 2 |
| emdash->parenthetical | 1 |
| emdash->parenthetical(merge) | 1 |
| emdash->comma+colon | 1 |
| pinpoint->parenthetical(reworded) | 1 |
| pinpoint->parenthetical+semicolon | 1 |
| pinpoint->parenthetical(merged) | 1 |
| **total** | **141** |

## Doctrine applied (brief §"Rewrite doctrine")

- **Relationship/appears-on labels** `[[Page]] — *Key — Role*` → `*Key: Role*` (inner em-dash→colon; keeps the structural link separator). Matches the already-sanctioned corpus form (Malley, N.C. v. Butler, Rothgery, Clifford). Two `*Related (X — Y)*` labels collapsed the same way (Knotts, Tuggle).
- **Citation source lines** `— URL — pinpoints: X.` → `— URL (pinpoints: X).` (doctrine #1; matches the sanctioned Graham v. Connor form). Complex-tail source lines split to a new sentence `— URL/. Pinpoints …` (matches 73 existing corpus instances, e.g. Kyllo, Rothgery) or merged into one parenthetical (Vinton, Chatrie).
- **Prose parenthetical asides** ` — aside — ` → `(aside)` or `, aside,` (doctrine #1), preserving legal meaning verbatim.
- **Independent-clause / elaboration em-dashes** → sentence split (doctrine #2), colon (doctrine #3), semicolon, or comma as grammar required.
- **Doctrine #4 (keep the single load-bearing em-dash)** used for blocks that carry a controlled/recurring banner (`**Status: Unverified — …**`, `**Good law — foundational.**`) or a post-quotation pincite attribution (`— *Id.* at N`, `— 139 S. Ct. at 687`): those were kept as the one allowed em-dash and the *other* em-dashes in the block were retired. Citation text itself was never altered.
- Two post-quote short-cites parenthesized (`— *Id.*` → `(*Id.*)`, Scott v. Harris L55, Bruder L53) where a block held two quote-attribution em-dashes and one had to yield; the cite content is untouched.

## Exemptions honored
- Never edited inside direct quotations or `[!rule]`/blockquote callouts.
- Controlled authority-weight labels left intact (e.g. `**Binding in-circuit — 4th Cir.**` in Curtilage.md L77 is masked/exempt and was preserved; only the adjacent prose em-dash was retired).
- En-dash ranges (e.g. `326–327`, `7–7`) untouched (A7 — style rule, not a LINT-10 target).

## Verification
- Deterministic applier: every edit validated to match exactly once and to drop the block to ≤1 countable em-dash before writing; all-or-nothing write.
- Wikilinks / URLs / markdown-links preserved on all 141 edited lines (diff vs `HEAD`); no double-spaces; no em-dash count increased.
- In-place edits only; write-scope respected — exactly the 52 packet files were written (sibling packets' concurrent edits in the shared tree are not mine).
