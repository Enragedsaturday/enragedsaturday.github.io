# CAMP-A2 — LINT-7 banned-variant normalization (S9 P4)

**Lane** `CAMP-A2` · **model** `claude-opus-4-8` · **write-scope** `content/` (25 LINT-7-flagged files) + `_run/s9/p4/`
**Ruling** P4-16 (user-sanctioned baseline campaign). **Register** `scripts/lint/term-register.yml` = canonical.

## Coverage (deterministic 52/52)
- **assigned** 52 high-severity LINT-7 banned-variant rows (authoritative harvest: `python3 scripts/lint/lint7_glossary.py content`, high-severity only)
- **examined** 52 · **fixed** 52 · **skipped** 0
- **Result: LINT-7 high on the 25 touched files 52 → 0** (whole-`content` high also 0; only pre-existing/coverage mediums remain).
- Total edits applied **57** = 52 rendered highs + **5 in-scope frontmatter `holding:` durability fixes** (Case-Index source, see §Case Index).

Applied via a two-phase validating applier (`apply_fixes.py`-pattern): phase 1 asserts every `old` string occurs **exactly once** in its file (all 57 passed); phase 2 writes all-or-nothing. Per-row before/after in `CAMP-A2-fixes.jsonl` (57 rows).

## Variant → canonical (all per register)
| banned variant | canonical | route | count | coverage side-effect |
|---|---|---|---|---|
| `inevitable-discovery` | `inevitable discovery` | page | 25 (20 body + 3 index + 2 fm) | +23 coverage MEDIUM |
| `patdown` | `pat-down` | **skip** | 11 | none (skip never flags) |
| `knock and talk` | `knock-and-talk` | page | 9 | +8 coverage MEDIUM |
| `stop and frisk` | `stop-and-frisk` | **skip** | 6 | none |
| `knock and announce` | `knock-and-announce` | page | 3 | +3 coverage MEDIUM |
| `totality of circumstances` | `totality of the circumstances` | glossary | 2 | +2 coverage MEDIUM |
| `search-incident-to-arrest doctrine` | `search incident to arrest` | page | 1 | none (relinked — see J1) |

## Hard-rule compliance
- **(i) Quotes/blockquotes never edited.** Each of the 52 hits was re-checked against the lint's own zone masking (`zones.compute_zones` + `_blank_blockquotes` + `_blank_wikilink_targets`). All 52 sit in **editable prose**. Same-line variants *inside* double quotes were correctly masked/exempt and left untouched — e.g. Arizona v. Johnson's quoted `'stop and frisk'`, Neugin's & Soto-Peguero's quoted `"inevitable discovery"`, Walker's `"is not considered a search"`. **Zero** genuinely-quote-flagged rows → **zero quote escalations**.
- **(ii) Wikilink TARGETS never changed** — only display-side/prose surfaces. Existing canonical links (`[[Knock and Talk|knock-and-talk]]`, `[[Inevitable Discovery and Independent Source|inevitable discovery]]`, etc.) left intact.
- **(iii) Case/pluralization preserved** — all 52 hits were lowercase base forms (word-bounded regex excludes `patdowns`/etc.); minimal hyphen↔space swaps.

## Case Index (generated file — durability note)
`content/legal-system-research-and-reference/Case Index.md` Holding cells are **regenerated** from each case's frontmatter `holding:` (`build_case_index.py::page_rows → read_holding`; carry-forward applies only to UNVERIFIABLE/UNCONFIRMED caption rows, not these). So the 10 flagged index rows are direct-edited (in scope, clears the highs now) **and** their source split in/out of scope:

- **5 IN-scope sources** → frontmatter `holding:` **also fixed** (durable; survives a FIN-INDEX regen): Florida v. J.L. (stop and frisk), United States v. Walker (knock and talk), United States v. Rideau (patdown), State v. Mitcham (inevitable-discovery), United States v. Loera (inevitable-discovery).
- **5 OUT-of-scope sources** → frontmatter NOT touched (violates write-scope); direct index edit is a **stopgap a regen will revert**. See ESCALATION E1.

**No `build_case_index.py` regen was run** (whole-table rewrite = out of a surgical 52-fix scope, and it would revert the 5 out-of-scope direct edits anyway). Table column integrity re-verified: 0 malformed rows.

## Escalations
```json
[
 {"row":"p4.escalation.v1","packet":"CAMP-A2","class":"case-index-generated-source-out-of-scope",
  "claim":"5 Case Index Holding cells are generated from the frontmatter holding: of a case OUTSIDE CAMP-A2 write-scope; the direct Case Index edit clears the high now but a build_case_index.py (FIN-INDEX) regen reverts it from the unfixed source",
  "rows":[
    {"index_line":94,"source":"content/cases/Carroll v. Carman.md","variant":"knock and talk"},
    {"index_line":176,"source":"content/cases/French v. Merrill.md","variant":"knock and talk"},
    {"index_line":546,"source":"content/cases/United States v. Meyer.md","variant":"knock and talk"},
    {"index_line":204,"source":"content/cases/Haynes v. Washington.md","variant":"totality of circumstances"},
    {"index_line":577,"source":"content/cases/United States v. Satterfield.md","variant":"inevitable-discovery"}],
  "recommendation":"dispatch a follow-up packet to fix the 5 source frontmatter holding: fields (then FIN-INDEX regen), OR accept the direct Case Index edit with regen deferred until those sources are fixed",
  "lane":"CAMP-A2","model":"claude-opus-4-8"},
 {"row":"p4.judgment.v1","packet":"CAMP-A2","class":"compound-modifier-relink","id":"A16",
  "file":"content/cases/United States v. Anchondo.md","line":65,
  "claim":"'search-incident-to-arrest doctrine' is the only banned variant carrying a trailing noun; a literal token-swap ('the search incident to arrest of Chimel') is ungrammatical. The register bans the hyphenation, not the word 'doctrine'. Normalized to '[[Search Incident to Arrest|search incident to arrest]] doctrine of [[Chimel v. California]]' — de-hyphenated canonical noun phrase, kept 'doctrine', linked to match the identical pattern used twice more on the same line (also avoids spawning a coverage MEDIUM)",
  "confirm":"orchestrator to confirm the relink is acceptable vs. a plainer de-hyphenation",
  "lane":"CAMP-A2","model":"claude-opus-4-8"}
]
```

## Reported — NOT CAMP-A2's class (register-coverage review-flag)
De-hyphenating banned variants into their **route:page/glossary canonical surfaces** makes each *unlinked* occurrence a MEDIUM `routed term '…' left unlinked` (S8 R7/R13b, D1 every-occurrence). This produced **+36 new MEDIUM** rows (whole-content MEDIUM 129 → 165), **all within the 25 touched files, none outside, zero new HIGH**:
- 23 `inevitable discovery` · 8 `knock-and-talk` · 3 `knock-and-announce` · 2 `totality of the circumstances`.

These belong to the S8 coverage/linker lane, **not** CAMP-A2 (per brief). `stop-and-frisk` (6) and `pat-down` (11) are route:skip and correctly produced no coverage flag; `search incident to arrest` was relinked (A16) so produced none.

## Note — knock-and-announce verb usage (deterministic per register)
3 hits (Richards `need never knock and announce`, Wilson `failed to knock and announce`, Destruction of Evidence `knock and announce their presence`) are **verb** uses. The register lists `knock and announce` as a banned variant with **no verb carve-out** (contrast `pat-down`, which explicitly exempts the verb `pat down the outer clothing`). LINT-7 flagged them; normalized to `knock-and-announce` per register-as-canonical. Recorded for visibility; no re-adjudication owed.

## Method / evidence
- Harvest: `lint7_glossary.py content` high-severity rows (52).
- Editability + case/plural verified by re-running the lint's exact masking pipeline (`scripts/s8/zones.py`) per hit.
- Register semantics from `scripts/lint/term-register.yml` (canonical/route/target).
- Case Index generation confirmed by reading `scripts/build_case_index.py` (`page_rows`/`read_holding`) + matching Florida v. J.L. cell to its frontmatter `holding:`.
- No CourtListener / no lake reads needed (pure register-driven text normalization).
