# CAMP-C11 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

## Coverage

| metric | value |
|---|---|
| files assigned | 51 |
| lint rows assigned (manifest `row_total`) | 263 |
| distinct flagged blocks | 140 |
| blocks fixed | 140 |
| lint rows fixed | 263 |
| escalated | 0 |
| LINT-10 highs before → after | **263 → 0** |

Per-file LINT-10 highs went to 0 for every one of the 51 files, verified by
re-running `scripts/lint/lint10_emdash.py` over the full manifest file list
(absolute paths; the lint resolves globs against the real repo root, so files
were passed explicitly). Block em-dash counts after: 96 blocks at exactly 1
(within budget), 44 blocks at 0. Row detail (one row per block, masked block
em-dash count before/after + technique) in `CAMP-C11-fixes.jsonl`.

## Techniques (by frequency, 140 blocks)

- **parens (#1) — 50.** Parenthetical em-dash pair → parentheses. The bulk of
  Issue/Rule/Application/Background asides. Where the closing dash abutted a main
  clause / participial / non-restrictive `which`, a comma was added after `)`.
- **T2-source — 39.** Sources bullets `*Case*, cite — url — pinpoints: …`: kept
  the `cite — url` em-dash, converted the pre-pinpoint em-dash to a period and
  capitalized the annotation (`. Pinpoints:` / `. Pinpoint:` / `. Interior
  pincite(s)` / `. Pinpoint given as`). URLs, reporters, pin ranges (en-dashes),
  cluster/opinion ids untouched. Two source lines carried a markdown-link cite
  `[cite](url) — pinpoint` (Burdeau L77, Moore-Bush L91); same period conversion.
- **T1-role — 33.** Appears-on bullets `[[Page]] — *Key — Sub*`: kept the
  universal ` — ` link/role separator, converted the role tier→sub em-dash to a
  colon (`*Key: Sub*`). Reconcile reads `homes[].role` from frontmatter, not the
  rendered leaf, so no cross-surface desync. Also covers non-`Key` tiers
  (`Recent application: illustrates …`, `Key: Historical (overruled by Katz)`).
- **comma (#1) — 12.** Appositive / relative / emphatic-answer em-dash → comma
  (`No — …` → `No, …`; `real estate — which …` → `real estate, which …`; the
  6 ⚪-status blocks below).
- **quote-cite-parens (#4) — 3.** `"quote" — cite … "quote" — cite` doubles:
  first attribution parenthesized, the load-bearing pincite kept
  (Anderson L65, Messerschmidt L57 with the nested `(quoting Leon)` flattened,
  Mullenix L55).
- **colon (#3) — 2.** Em-dash introducing an elaboration / quote → colon
  (Olmstead L55 `(Historical: …)`; Lee L64 quote intro).
- **period-split (#2) — 1.** Independent clause split (Fulminante L53
  `involuntary. Coercion may be mental …`).

Nine blocks carried **3** counted em-dashes (Burdeau L77, Chiaverini L60,
Havens L58, Lee L64/L73, Moore-Bush L83, Payner L58, Xiang L67/L70); each was
brought to ≤1 by combining the techniques above (the majority: parenthesize the
pair, keep one load-bearing citation/contrast em-dash).

## Hard-constraint compliance

- **Quotations never edited.** Only em-dashes OUTSIDE straight/curly double
  quotes were touched. Blocks whose parenthesized/comma'd asides *contain* quoted
  substrings (Beecher "kind of slumber", Graham "welfare check"/"reasonable
  belief"/"community caretaking", Olmstead "material things", Havens
  "ever engage[d] … McLeroth", Wilson, Xiang "applies with equal force …") kept
  those quoted spans byte-identical. In-quote em-dashes (Draper L53, Thompson L55,
  Lee L64, Olmstead L55) were masked/exempt and left intact. No lint-masking
  escalation (all-em-dashes-inside-quotes) block occurred, so **0 escalations**.
- **Controlled authority-weight labels untouched.** `Binding — SCOTUS`,
  `Binding in-circuit — …`, `Persuasive …` are masked by the lint and were never
  edited; Gaetjens L73's `Binding in-circuit — 7th Cir.` was preserved verbatim
  while only the role tier em-dash became a colon. (`Historical` is NOT a masked
  LINT-10 label; Olmstead L55/L71's descriptive `Historical` em-dashes were
  legitimately in scope and converted.)
- **Citations preserved.** Case names, reporters, parallel cites, pin ranges
  (en-dashes: 353–354, 627–628, 106–107, 36–38), slip-op pins, and CourtListener
  URLs unchanged. Frontmatter untouched (no `holding:` string was flagged in this
  packet).
- **Legal meaning / instructor voice preserved.** Role taxonomy words retained
  verbatim (only tier→sub punctuation changed); ⚪-banner framing kept.

## ⚪ status-line handling (6 blocks)

Per the ⚪-banner convention, the `**Status: … —**` (or `*(Historical: …)*`)
lead-in em-dash was kept and the block's OTHER em-dash restructured: Burdeau L71,
Rehberg L73, Lee L73, Moore-Bush L83, Warshak L75, Wilson L78.

## No new violations

Ran the full `scripts/lint/lint*.py` roster over the 51 working files vs a
HEAD-baseline mirror (`git show HEAD:<file>` into scratch, per the concurrency
addendum — no `git stash`/`checkout` of shared paths). No lint's high or medium
count rose. On the real working paths the only remaining findings are
**pre-existing mediums, unchanged**: LINT-2 quote_pinpoint 25, LINT-7 glossary 3
(neither is this packet's to fix). LINT-10 263→0; **0 highs across the entire
roster**. No new banned lexicon, no new >3-case walls, no structural breakage.
(A transient LINT-23 50→0 delta in the mirror comparison was a path artifact:
LINT-23 excludes `content/cases/**`, which the out-of-tree mirror copies fall
outside of; case pages correctly carry no `weight:` and score 0 highs on the real
paths.)

## Escalations

None. All 263 rows fell to authored prose or structured Appears-on/Sources
bullets outside quotations.
