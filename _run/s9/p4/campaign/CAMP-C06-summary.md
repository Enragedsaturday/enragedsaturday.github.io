# CAMP-C06 — LINT-10 em-dash renovation (coverage summary)

Packet: `_run/s9/p4/campaign/lint10/C06.json` · lane `{claude, claude-opus-4-8}`

## Coverage
- **Files assigned:** 51 (all `content/cases/*.md`)
- **Lint rows assigned:** 263 HIGH (block + sentence rows; manifest `row_total`)
- **Distinct flagged blocks/lines:** 137
- **Fixed:** 137 / 137 blocks (all 263 rows cleared)
- **Escalated:** 0 (no block had em-dashes located *only* inside direct quotations / blockquotes; every flagged block carried at least one countable em-dash that was fixable in-place)

## Before / after (LINT-10 over the 51 packet files)
- Before: `263 high, 0 medium, 0 low`
- After:  `0 high, 0 medium, 0 low`
- Self-test (`--self-test`): PASS

## Techniques (ledger `CAMP-C06-fixes.jsonl`, 137 rows)
- **typeA-colon-role-label (36):** "Appears on" role labels `[[Page]] — *Key — X*` → `*Key: X*`. The inner em-dash becomes a colon, leaving the single wikilink→label em-dash. Mirrors the established corpus convention (`*Key: Anchor*` / `*Key: Progeny / Refinement*` already appear 100+ times; the exact `*Key: Anchor (foundational origin)*` already exists).
- **typeB-bracket-link-source (39):** Sources bullets `- *Case*, cite — URL — pinpoints…` → `- [*Case*, cite](URL) — pinpoints…`, absorbing the cite→URL em-dash into a markdown link per STYLE §6 / S5 R12 (bracketed-link format). Matches 157 existing bracketed Sources lines, which retain the single ` — pinpoint(s):` em-dash. (Includes 2 rows for Howard Davis L71: the bracket step + an inner `holding — quotes` → `holding; quotes` step.)
- **typeC-prose (62):** parenthetical em-dash asides → parentheses (or commas at clause boundaries); a few splits (`Yes — …`/`No — …`/`remedy — …` → period), one intro-em-dash → colon (Hanlon), one quote-attribution → `(*Id.*)` (Buie). Doctrine order preserved; the single load-bearing / contrast dash kept where present (e.g. Alderman L60 keeps `— not surveillance aimed at someone else`). Status-banner blocks (Blue, Cole, Perez-Rodriguez, Landor) left with their banner em-dash and the *other* em-dash de-dashed.

## Hard-constraint compliance
- **No edits inside quotations/blockquotes.** Quote-adjacent fixes (Dalia L55, Buie L55, Crews L55, Hanlon L53, Rodriguez L55, Blue L64, Jimeno L53, Lange L55) restructured only the surrounding prose; verbatim quoted text is byte-preserved. 3 lines (Jimeno L53, Lange L55, Rodriguez L55) still carry em-dashes *inside* quotations — exempt (masked) and correctly uncounted.
- **Controlled authority-weight labels untouched** (`Binding — SCOTUS`, etc.).
- **Citation text untouched** — reporter/pincite strings unchanged; only surrounding delimiters altered.
- **No new lint violations introduced.** All 29 lints re-run over the 51 files: 0 new HIGHs. LINT-2 (13 med) and LINT-7 (1 med) violation sets are byte-identical to the `git show HEAD:` baseline (0 added / 0 removed). LINT-1's `ValueError: … 'null'` reproduces identically on the HEAD mirror (pre-existing frontmatter data issue, not from these edits).

## Write scope
Only manifest files (`content/cases/*.md`) + `_run/s9/p4/campaign/` outputs. Per-file read-modify-write; no `git stash`/`checkout`.

## Artifacts
- `_run/s9/p4/campaign/CAMP-C06-fixes.jsonl` (137 rows)
- `_run/s9/p4/campaign/CAMP-C06-summary.md` (this file)
