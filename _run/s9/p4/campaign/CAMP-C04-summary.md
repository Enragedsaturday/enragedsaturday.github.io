# CAMP-C04 — LINT-10 em-dash renovation (summary)

Lane: `claude` · model: `claude-opus-4-8` · brief: `_run/s9/p4/campaign/LINT10-PACKET-BRIEF.md` (RULING P4-16(e), S1 A7/A8)

## Coverage

| metric | value |
|---|---|
| files assigned | 52 |
| lint rows assigned (manifest `row_total`) | 264 |
| distinct flagged blocks | 140 |
| blocks fixed | 140 |
| lint rows fixed | 264 |
| escalated | 0 |
| LINT-10 highs before → after | **264 → 0** |

Per-file LINT-10 highs went to 0 for every one of the 52 files (verified by
re-running `scripts/lint/lint10_emdash.py` over the full file list; lint self-test
PASS). Masked block em-dash count after fix: 98 blocks at exactly 1, 42 at 0 — no
block over budget, no block worse than before. Row detail (one row per block, with
masked block em-dash count before/after + technique) in
`_run/s9/p4/campaign/CAMP-C04-fixes.jsonl`.

## Techniques (by frequency)

Mechanical (74 blocks) — CAMP-C01 conventions reused verbatim for corpus consistency:
- **T2-source (42)** — Sources bullets `*Case*, cite — url — pinpoint(s): …`: kept the
  `cite — url` em-dash, converted the pre-pinpoint em-dash to a period + capitalized the
  annotation (`… url. Pinpoints: …`). Handles both `pinpoint:` and `pinpoints:` variants,
  incl. the *Tanzin v. Tanvir* link-form Sources bullet. URLs, case names, reporters, pin
  ranges (en-dashes), CL opinion-id parentheticals untouched.
- **T1-role (32)** — Appears-on bullets `[[Page]] — *Key — Sub*`: kept the universal
  ` — ` link/role separator, converted the role tier→sub em-dash to a colon (`*Key: Sub*`).
  Role string is a rendered leaf (reconcile reads `homes[].role` from frontmatter, not the
  rendered line), so no cross-surface desync.

Prose / editorial (66 blocks), doctrine per block:
- **parenthetical em-dash pair → parentheses (#1) (40)** — the bulk of Background/Issue/
  Rule/Application blocks; also the Screws/Stansbury tight (no-space) em-dash pairs, and the
  Evans/Mendez/Oliveras aside-with-case-links (case counts unchanged, no new wall).
- **kept the single load-bearing em-dash (#4) (16)** — "quote — cite" doubles: parenthesized
  the first attribution, kept the load-bearing pincite (Scott/Muniz/Walter/Evans); ⚪-banner
  Status bullets: kept the `**Status: … —**` label em-dash, restructured the trailing one
  (Carter/Egbert/Gutierrez/Amos/Carlton Williams/Mendez/Meyer/Oliveras); Chadwick kept the
  `**Limited by** [[Case]] —` label separator; Groh kept the rhetorical tricolon dash; Meyer
  kept the pivot dash; Knock and Talk kept the intro elaboration dash.
- **appositive / participial pair → comma (#1) (7)**.
- **elaboration / label list → colon (#3) (2)** — Mendez forensic-split; Sandoval tent-case
  `Case — descriptor` labels → `Case: descriptor`.
- **independent clause → period-split (#2) (1)** — Carlton Williams treatment bullet.

## Hard-constraint compliance

- **Quotations never edited.** Blocks whose in-quote spans carry em-dashes/periods
  (Connally, Perry, Muniz, Scott, Egbert, Walter, Carter) were fixed only on the non-quoted
  em-dashes; every quoted span is byte-identical. Colons/parens/commas added sit outside the
  quote marks (verified: quote-pincite lint LINT-2 stays 0 high).
- **Controlled authority-weight labels untouched.** `**Binding — SCOTUS**`,
  `**Binding in-circuit — 10th Cir.**` etc. left intact (masked by the lint; those bullets
  reached budget via the non-label em-dash alone — e.g. Evans L64, Michigan v. Thomas L64,
  Walter L64 were not edited).
- **Citations preserved.** Case names, reporters, parallel cites, pin ranges (en-dashes),
  CourtListener URLs and opinion-ids unchanged. Frontmatter untouched (Ornelas L34
  `holding:` verified identical to HEAD).
- **Legal meaning, emphasis, instructor voice preserved**; role taxonomy words retained
  verbatim (only tier→sub punctuation changed).

## No new violations

Diffed the content-text lints HEAD-mirror (`git show HEAD:` per the concurrency addendum,
no checkout/stash) vs working tree over the 52 files: no regression on any of
LINT-2/3/4/5/8/9/11/12/23/24/28 (all 0 high in working; LINT-23's mirror-isolated count is
a cross-corpus artifact, real working count 0). **LINT-3 stays at its 2 pre-existing highs**
in `Knock and Talk.md` (L28 4-case wall, L36 5-case wall) — out of scope for this LINT-10
packet; the L36 em-dash fix (comma) added/removed no cases. No new banned lexicon (LINT-4 0),
no new pipeline vocab (LINT-11 0), no unbalanced parens on any edited line.

## Escalations

None. All 264 rows fell to authored prose or structured bullets outside quotations; no
all-em-dashes-inside-quotes block occurred (no lint-masking escalation triggered).
