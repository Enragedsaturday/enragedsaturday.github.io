# LINT-10 packet brief (em-dash renovation — S1 A7/A8, RULING P4-16(e))

You fix every HIGH row in your packet manifest (_run/s9/p4/campaign/lint10/<packet>.json).
Rule: a BLOCK (paragraph or single list item) may carry AT MOST ONE em-dash (U+2014), and no
sentence may carry two or more. En-dashes in ranges are fine and NOT yours to touch.

## Rewrite doctrine (in order of preference)
1. Drop a parenthetical em-dash pair into actual parentheses, or a comma pair, when the
   aside is short: "the rule — announced in Katz — governs" -> "the rule (announced in
   Katz) governs" or ", announced in Katz,".
2. Split the sentence at the em-dash when what follows is an independent clause:
   " — the Court reasoned..." -> ". The Court reasoned...".
3. Use a colon when the em-dash introduces an elaboration/list.
4. Keep the SINGLE most rhetorically load-bearing em-dash in a block when the block had
   several — you don't have to purge all of them, just get within budget.

## Hard constraints
- NEVER edit text inside direct quotations (straight or curly double quotes) or blockquote
  lines — those are exempt from the count; if a flagged block's em-dashes are all inside
  quotes, file an escalation row (lint masking question), do not edit.
- NEVER touch the controlled authority-weight label strings (they contain sanctioned
  em-dashes: "Binding — SCOTUS" etc.) or citation text.
- Legal meaning, emphasis, and the instructor voice must survive exactly. If a rewrite
  would change nuance, prefer doctrine #4 (keep one, restructure around it).
- Frontmatter `holding:` strings count when the lint flags them — same doctrine applies.
- Do not introduce new lint violations (no new banned lexicon, no >3-case walls).

## Procedure per file
Fix all flagged blocks -> re-run `python3 scripts/lint/lint10_emdash.py "<file>"` -> expect
0 highs for that file (lows/mediums not yours). After all files: run the lint over your
full file list; report before/after. Output: _run/s9/p4/campaign/<packet>-fixes.jsonl (one
row per block: file, line, blocks_before/after counts, technique used) + <packet>-summary.md
(coverage: rows assigned/fixed/escalated). WRITE-SCOPE: your manifest's files + _run/s9/p4/.

## Concurrency addendum (after CAMP-C01)
NEVER `git stash`/`git checkout` shared paths — other fleet lanes are editing the tree
concurrently. For a HEAD baseline, use `git show HEAD:<file>` into a scratch mirror. Your
writes must be per-file read-modify-write on your manifest files only.
