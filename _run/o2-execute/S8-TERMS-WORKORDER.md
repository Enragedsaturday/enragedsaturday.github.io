# S8 work order — R7 term routing + R8 glossary expansion (lane: o2-opus-xhigh)

**Read first:** spec R7 + R8 (+ §5 Method 5–6) · the O1 seed `_overhaul/ledger/S7-term-map.md`
(routing semantics already reasoned — consume as seed, then RETIRE: this lane's register
columns become the one artifact) · `scripts/lint/term-register.yml` (v1 — you extend it) ·
`content/legal-system-research-and-reference/Common Legal Terms.md` (37 anchors) ·
`content/legal-system-research-and-reference/Reading and Citing Cases.md` (citing-route
anchors) · `scripts/s8/zones.py` (frozen contract).

## Deliverable 1 — term-register v2 (routing columns)

Extend `scripts/lint/term-register.yml` → `schema: term-register.v2`, preserving every v1
field/entry. New per-term fields:
- `route: page | glossary | citing | skip`
- `target:` wikilink target — `route:page` ⇒ `[[Doctrine Page]]`; `route:glossary` ⇒
  `Common Legal Terms#anchor`; `route:citing` ⇒ `Reading and Citing Cases#anchor`
- `match:` optional additional surface forms/inflections (regex-free literal list;
  matching is case-insensitive + word-bounded)
- `eponym: true` where the term embeds a case name (Terry stop, Miranda warnings, Katz
  test, Brady material, Franks hearing, Batson challenge, Garrity warning, Monell claim,
  Bivens action, Edwards rule, Massiah rule, …) — the case-mention linker consults this
  flag (spec R3: register eponyms route as TERMS).
Seed the routes from the O1 map: §A ⇒ route:glossary rows; §C ⇒ route:page rows; §D ⇒
route:citing rows; §E ⇒ route:skip rows (the officer-vernacular skip-list is register
DATA, instructor-editable). The map's first-occurrence wiring is DEAD — D1 inverted it:
every occurrence links.

## Deliverable 2 — `scripts/s8/link_terms.py`

- Outside R2 zones (import zones.mask), link every occurrence of every routed term:
  `route:page` ⇒ `[[Target|matched surface text]]` (pipe preserves inflection);
  `route:glossary`/`citing` ⇒ `[[Common Legal Terms#anchor|surface]]` etc.;
  `route:skip` ⇒ never.
- Zone (g): a term's own page never self-links (glossary terms never link ON Common Legal
  Terms; a page-routed term never links on its target page).
- Adjectival/compound uses inside citation history follow their zone (d) — the zone module
  already exempts them. "qualified-immunity grounds" inside a parenthetical stays plain.
- Overlap rule: case-mention links already in the text (this lane runs AFTER the mention
  pass) are masked; a term nested inside a wikilink display is never re-linked; longest-
  match wins when register terms overlap (search incident to arrest > arrest).
- Anchor verification: every route target anchor must exist (build a heading→slug map with
  Quartz's slugger convention: lowercase, spaces→-, punctuation dropped); a register row
  whose anchor is dead = FAIL loudly, do not link, report.
- Emits the R12 terms section source: `_run/o2-execute/s8-term-rows.jsonl` (per-page
  register coverage counts + per-link rows). Dry-run default / `--write` / idempotent /
  `--self-test` + fixtures `scripts/s8/fixtures/terms/` (inflection piping, zone exemption,
  self-page, longest-match, dead-anchor refusal, skip-list).

## Deliverable 3 — R8 glossary candidates (adjudication input, NOT auto-authored)

Sweep S7-final prose (outside zones) for non-vernacular terms of art with NO page home and
NO glossary entry. Emit `_run/o2-execute/S8-GLOSSARY-CANDIDATES.md`: term · occurrences
(file:line, ≤5 samples) · proposed route (glossary w/ draft PURE-DEFINITION text — zero
citations, zero case-tied propositions — or page/citing/skip) · rationale. **Do NOT write
glossary entries or register rows for new terms — the orchestrator adjudicates the list,
then you apply the approved subset** (glossary entries + `### Term` anchors + register rows
+ wiring). Also audit the existing 37 entries for the pure-definition rule; report any
entry carrying a citation or case-tied proposition.

## Execution steps

1. Register v2 + link_terms.py + self-tests green.
2. Dry-run corpus-wide; report per-route link counts + 10 sample diffs + the candidates
   file + the 37-entry audit. **STOP for orchestrator adjudication** (routes GO/adjust +
   glossary approvals).
3. On GO: `--write` corpus-wide (one pass), apply approved glossary additions, re-run
   link_terms for the new rows, `npx quartz build` green.

## Constraints

COMMIT NOTHING · zero CL · stdlib only (yaml via existing repo pattern — check how
lint7 reads the register today) · touch only `scripts/s8/**`, `scripts/lint/term-register.yml`,
`Common Legal Terms.md` (approved entries only), content edits of exactly the link form,
`_run/o2-execute/` artifacts. Density tuning = register edits, never per-page exceptions
(SD10). No term both glossary-routed and page-routed (R8 check).
