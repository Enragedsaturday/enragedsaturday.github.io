# FIN-INDEX summary (S9 P4)

**Packet:** FIN-INDEX · **lane:** FIN-INDEX · **model:** claude-opus-4-8
**Deliverable:** `content/legal-system-research-and-reference/Case Index.md` =
fresh S4 regeneration (P2/P3-corrected holdings) **+** the S8 term-link pass
re-applied.

## Method — preferred path (scoped S8 term-linker re-run)

Drove the SIGNED S8 term-linker `scripts/s8/link_terms.py` as a library,
scoped to the Case Index only, via `_run/s9/p4/fin_index_build.py`:

1. `build_case_index.build()` — fresh regeneration from `content/cases/*.md`
   frontmatter (holdings are the SSOT; comes out plain, no term-links).
2. `link_terms.build_link_plan(regen, CI_REL, terms, idx, protect_pincite_lines=False)`
   then `apply_edits` — the exact S8 zone-mask / longest-match / table-pipe-escape /
   dead-target-refusal rule, no re-implementation.
3. Flagged-row override — the two adjudicated caption rows are forced to HEAD
   verbatim (they are already-S8-linked carry-forwards; the linker is idempotent
   on them so the override was a **no-op**, `flagged_overridden=[]`).

**Why this reproduces HEAD faithfully:**
- `scripts/lint/term-register.yml` is UNCHANGED since the S8 commit `f2444514`
  (most-recent commit on the register) → zero register drift.
- Empirical fidelity gate: on all **563 unchanged cells the linker output ==
  HEAD byte-for-byte** (`fidelity_fail=[]`). This proves faithful reproduction;
  changed cells then get the correct S8 treatment of the corrected text.
- Guard note: S8 linked the Case Index with the pincite-line guard OFF (each
  table ROW is one physical line and holdings carry `(YYYY)` citation zones);
  here guard on/off are empirically identical (244 = 244), and the run uses
  `protect_pincite_lines=False` to match documented S8 behavior.

Ledger cross-check: `_run/s8-link-ledger.json terms.pages[Case Index]` = 237
term-pass links (page 176 / glossary 40 / citing 21); the HEAD FILE carries 238
holding wikilinks (the +1 is an adjudicated-resolution link outside the term
pass). Both consistent with the reproduction.

## Coverage (deterministic)

- **Rows assigned/examined:** 612 data rows (610 case rows + 2 flagged) — all examined.
- **Skipped:** none.
- **Row-count invariant:** `content/cases/*.md` = **610** = 610 case rows; +2
  flagged carry-forward exception rows = **612**. `added=[]`, `removed=[]`.
- **4 frontier stubs excluded correctly:** the tripwire-arc stubs
  (Lowers / Brillhart / Eric-Johnson / Wilson-lake, commit `50022e25`) are LAKE
  records with **no `content/cases/` page**, so the generator's `content/cases/*.md`
  glob never emits them — 0 rows, as required. (`United States v. Wilson` the
  page is a distinct, page-backed case that IS in the index.)

## Verification results — all PASS

| Check | Result |
|---|---|
| Rows vs `content/cases` count | 610 case rows == 610 files; +2 flagged = 612 ✓ |
| Blank Good-law cells (N13) | **0** ✓ |
| Every Case cell a resolving wikilink | **all resolve** via Quartz PageIndex (title/slug); 0 truly unresolved ✓ |
| Mitcham / Perez / Loera corrected | Mitcham = **inevitable-discovery** (was independent-source); Perez = SIA/Eatherton; Loera = 10th-Cir out-of-scope ✓ |
| Term-link coverage vs HEAD | 563 unchanged cells reproduce HEAD exactly; delta only on the 47 changed cells, all logged ✓ |
| Dead register targets | **0** ✓ |
| Preamble (frontmatter + prose header) | **byte-identical to HEAD** ✓ |
| Idempotence | re-run of scoped linker on the written file plans **0** new edits (guard on & off) ✓ |
| Pipeline fixed point | two `--write` runs produce a byte-identical file (md5 stable; no concurrent frontmatter drift) ✓ |

## Term-link accounting

HEAD holding-links **238** → final **246** (page 177→182, glossary 40→42,
citing 21→22). Net +8 = **10 adds − 2 drops**, ALL on changed (P2/P3-corrected)
cells; unchanged cells contribute 0 delta.

**2 legitimate drops** (surface text removed by the holding correction; no
register surface survives — logged in `FIN-INDEX-droplog.jsonl`):
- `Arkansas v. Sanders` — `exigency` (rewrite: "…unless another warrant
  exception, independent of the automobile exception, applies…").
- `Coolidge v. New Hampshire` — `plain-view doctrine` (rewrite → "plain-view
  seizures / plain view"; neither is a register surface, so not re-linked).

**10 re-derived adds** (register rule re-applied to the corrected text — the
brief-sanctioned "re-derived from the ledger rule"; e.g. an unchanged cell
mentioning "exigency" WOULD be linked, so a corrected cell newly mentioning it
must be too, for consistency):
Carney (exigency), Florida v. Harris (totality-of-the-circumstances),
Franks v. Delaware (Franks hearing), Braxton (inevitable discovery),
Conner (exigency), Crumble (totality-of-the-circumstances),
Gooch (exigent circumstances), U.S. v. Jackson (good-faith exception),
Loera (good-faith exception), Wilson (vacated — correct judgment-sense:
"conviction was vacated"; the register skip-phrase guard correctly allowed it).

## The `flagged: 1` warning — explained + root-caused + fixed

HEAD carried **2** flagged carry-forward exception rows (self-help UNCONFIRMED;
Cruz/West/Jackson UNVERIFIABLE). The generator's `flagged_rows()` split cells
with naive `ln.split("|")`; the Cruz/West/Jackson holding had picked up an S8
term-link with an escaped display pipe
(`[[Reading and Citing Cases#reporter\|reporter]]`), inflating the cell count
past 5, so that row was **silently dropped** — only 1 survived (`flagged: 1`),
violating the generator's own "flagged rows never vanish" contract.

**R12-maintenance-visible fix** (`scripts/build_case_index.py`, +21/−1, minimal):
added `_split_cells()` (mirrors the frozen `zones._row_pipe_positions`: blanks
wikilink-internal pipes, ignores escaped `\|`, slices on delimiter pipes) and
used it in `flagged_rows()`. This is a bug fix to the splitter ONLY — term-link
enrichment was NOT ported into the generator (it remains the separate S8 pass).
After the fix, both flagged rows carry forward (now `flagged: 2`) and the
Cruz/West/Jackson row keeps its S8 links verbatim.

`python3 scripts/build_case_index.py --check` still reports **DIFF** — expected:
the generator regenerates PLAIN holdings; term-links are the S8 enrichment layer
re-applied after each regen (the established S4→S8 pipeline), not a defect.

## Reproduction

Deterministic, stdlib-only, zero CourtListener:
```
git checkout HEAD -- "content/legal-system-research-and-reference/Case Index.md"
python3 _run/s9/p4/fin_index_build.py --write
```
(Restoring HEAD first ensures both flagged carry-forward rows are the source;
the fixed generator now preserves them on any future regen without the restore.)

## Notes for the orchestrator

- The Case Index is a **derived artifact** of `content/cases/*.md` frontmatter.
  Sibling P4 lanes edited many case pages concurrently during this run; my
  written index is a fixed point of the frontmatter as of write time (md5 stable
  across re-runs). If case-holding edits continue, re-run the one-line pipeline
  above to re-snapshot — it will re-reproduce HEAD on unchanged cells and
  re-derive only the changed ones.
- Pre-existing, out-of-scope (unchanged vs HEAD, not fixed here): the
  `[[Case Index]]` self-row (from `content/cases/index.md`, blank holding/home)
  and three blank-holding case pages (`United States v. Al-Azzawy / Nora /
  Vaneaton`) — these have non-blank ("good") Good-law cells so N13 holds; the
  blank Holding is a case-page-frontmatter matter outside FIN-INDEX write-scope.

## Artifacts

- `content/legal-system-research-and-reference/Case Index.md` — final (written)
- `scripts/build_case_index.py` — R12 flagged-splitter fix
- `_run/s9/p4/fin_index_build.py` — the scoped-linker driver (reproducible)
- `_run/s9/p4/FIN-INDEX-fixes.jsonl` — 12 rows (10 add-link, 2 drop-link)
- `_run/s9/p4/FIN-INDEX-droplog.jsonl` — header + 2 drop records (full holdings)
- `_run/s9/p4/fin-index-report.json` — full machine report
- `_run/s9/p4/CI_HEAD.md` — HEAD snapshot used as the reproduction reference
