# CAMP-C05 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

## Coverage

| metric | value |
|---|---|
| files assigned | 51 |
| lint rows assigned (manifest `row_total`) | 263 |
| distinct flagged blocks | 138 |
| blocks fixed | 138 |
| lint rows fixed | 263 |
| escalated | 0 |
| LINT-10 highs before → after | **263 → 0** |

Every one of the 51 files went to 0 LINT-10 highs (authoritative re-run of
`scripts/lint/lint10_emdash.py` over the full file list: exit 0, 0 high rows;
`--self-test` PASS). One row per block (masked block em-dash count before/after +
technique) in `_run/s9/p4/campaign/CAMP-C05-fixes.jsonl` (fields:
`file, line, block_em_before, block_em_after, technique`).

## Techniques (by frequency)

Mechanical (77 blocks):
- **T2-source (42)** — Sources bullets `*Case*, cite — url — pinpoints: …`: kept the
  `cite — url` em-dash, converted the pre-pinpoint em-dash to a period + capitalized the
  annotation (`… url. Pinpoints: …`). Matches the canonical single-dash Sources shape
  (cf. C01 *Arizona v. Mauro*). URLs, case names, reporters, pin ranges (en-dashes),
  slip-op/cluster→opinion notes untouched. Classic's `— interior pincite(s)` variant took
  the same period+cap transform.
- **T1-role (35)** — Appears-on `[[Page]] — *Key — Sub*` bullets: kept the universal
  ` — ` link/role separator, converted the role tier→sub em-dash to a colon (`*Key: Sub*`).
  Role string is a rendered leaf (reconcile reads `homes[].role` from frontmatter, not the
  rendered line), so no cross-surface desync; `*Key — Anchor*` → `*Key: Anchor*` likewise.
  `*Related (cross-doctrine)*` bullets (one em-dash = the separator) were already in budget
  and left untouched.

Prose / editorial (61 blocks), doctrine per block:
- **parenthetical em-dash pair → parentheses (36)** and **→ parentheses+comma (6)** —
  the bulk of Background / Issue / Rule / Application blocks; the `+comma` variant where the
  closing dash was the boundary before a `Because…`/result main clause (Carpenter L60,
  Lewis L58, Howes L60, Silverthorne L60, Harris L64, Tarantino L60).
- **em-dash pair → commas (4)** where parentheses would nest inside an existing parenthetical
  (Carpenter L68 *Chatrie* bullet, Tarantino L67) or read better as an appositive
  (Barnes L47, Hampton L53).
- **single appositive/contrast em-dash → comma (3)** (Dickerson L53, Monell L53, Hay L58).
- **elaboration em-dash → colon (1)** (Lackey L59, after a closing quote).
- **independent clause → period-split (3)** — emphatic `No —`/`Yes —` answers and one
  narrative split (Barnes L53, Fellers L53, Hay L67).
- **"quote — cite" doubles → doctrine #4 (2)** — Beheler L53/L55: first/second attribution
  parenthesized, the load-bearing explicit-page pincite (`— *Id.* at 112x …`) kept.
- **⚪-banner Status blocks (6)** — kept the `**Status: Unverified — …**` em-dash (the single
  budgeted dash), restructured the other(s): Trombetta L72 & Payne L76 (parens),
  Berkowitz L74 & Hay L73 (comma), Carpenter-remand L71 (period-split), Vasquez-Algarin L75
  (colon).

## Hard-constraint compliance

- **Quotations never edited.** Blocks carrying in-quote text (Beheler, Barnes, Carpenter,
  Christensen, Smith, Dickerson, Fellers, Hampton, Lackey, Monell, Winston) were fixed only
  on the non-quoted em-dashes; every straight-`"…"` span is byte-identical. All files use
  straight quotes/apostrophes (no curly), verified before editing.
- **Controlled authority-weight labels untouched.** `Binding — SCOTUS` (header + Treatment
  lines) is A8-masked and was never a target.
- **Citations preserved.** Case names, reporters, parallel cites, pin ranges (en-dashes:
  575–576, 725–726, 152–53, etc.), CourtListener URLs, and slip-op/cluster→opinion
  provenance notes unchanged. Frontmatter (incl. `holding:` and `homes[].role`) untouched.
- **Legal meaning, emphasis, instructor voice preserved**; bold/italic and `[[wikilink]]`
  markup intact; role-taxonomy words retained verbatim (only tier→sub punctuation changed).

## No new violations

Symmetric isolated diff of all 29 content lints (`lint1`…`lint29`) over the 51 files,
HEAD-snapshot vs working tree: the **only** lint whose output changed is LINT-10
(263 → 0 highs). Every other lint is byte-identical in outcome (0 new high/medium/low).
No new banned lexicon, no >3-case walls, no structural breakage.

## Escalations

None. No flagged block had all its em-dashes inside quotations, so no lint-masking
escalation arose; all 138 blocks fell to authored prose or structured bullets outside
quotations.
