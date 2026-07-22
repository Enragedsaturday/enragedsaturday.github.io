# CAMP-WB1 — LINT-11 Wave-B (B1/B3/B4) + P4-17(b)/(d) execution

**Lane** `CAMP-WB1` · **model** `claude-opus-4-8` · **branch** `overhaul2/execute`
**Write-scope** `content/` (B1/B3/B4 files + 5 named case pages' frontmatter) ·
`scripts/lint/lint11_pipeline_vocab.py` + fixtures + `lint11-allowlist.json` · `_run/s9/p4/campaign/`
**Governing** CAMP-A3 legacy-design report (partition ii) · RULING **P4-17(b)** + **P4-17(d)** ·
S1 A2 · `scripts/lint/term-register.yml` (canonical)

## Ground-truth harvest (not the report's stale counts)
Authoritative harvest = `python3 scripts/lint/lint11_pipeline_vocab.py content` (high only) at packet
start: **152 highs**, which partition exactly into the report's classes:

| Class | Hits | Owner | Disposition |
|---|---|---|---|
| **B1** root-index roster (`content/index.md`, S3/S6/S7 ×41 lines) | 123 | WB1 | trailer → HTML comment |
| **B3** body-prose rule refs | 12 | WB1 | reword (drop id) |
| **B4** `No standalone case page` (`Entrapment.md` L100–101) | 2 | WB1 | drop meta-label |
| **FP** semantic false positives (pending-Cl ×8, wrapper ×4, split-from ×1, placeholder ×1) | 14 | WB1 | regex + allowlist |
| **FP (discovered, out-of-scope)** `State v. Christensen` docket `R11` | 1 | escalate | left as 1 residual |
| **B2** Sources-note pin-conversion provenance | **0** | WB2 | already drained at my start |
| **Total** | **152** | | |

Note on B2: the report projected B2=77, but ground truth shows **zero** Sources-note hits remaining —
the P4-authored + legacy Sources-note class was already fully drained before this packet (CAMP-A3
partition (i) / prior waves). So whole-`content` was already gated by WB1's classes + the one docket FP.

## Delta — my classes only (deterministic)
**LINT-11 highs 152 → 1.** I cleared **151** (B1 123 + B3 12 + B4 2 + FP 14). The **1 residual** is the
discovered `State v. Christensen` docket-number FP (escalated, not self-adjudicated — see §Escalation).
WB2 runs concurrently on B2 (which was already 0); it does not change my count (disjoint files).

Per-file re-scan after edits: all 11 WB1 scope files = **0** LINT-11 highs. `content/index.md` = 0
rendered `*placed by S3*` trailers, 41 masked `<!-- placed by S3 … -->` comments.

## B1 — root index roster (123 hits / 41 lines / `content/index.md`)
One identical template on 41 category-roster stub entries:
`- [[X]] — *placed by S3. S6 verifies cases, S7 authors prose.*`
Reworded per the report's shape #1 and the packet directive *"provenance that has no reader value moves
to HTML comments"*: the rendered italic pipeline trailer (S3 places / S6 verifies / S7 authors) is
**relocated verbatim into a same-line HTML comment** —
`- [[X]] <!-- placed by S3. S6 verifies cases, S7 authors prose. -->`.
Reader-facing output is a bare wikilink (tight front page, matching the already-bare entries like
Community Caretaking / Emergency Aid); the provenance is preserved (lossless, reversible) but masked
from render and from the lint (S1 A2 line 273 — HTML comment is the sanctioned home for state that need
not render). 41 edits clear 123 hits (S3+S6+S7 per line). No other class-1 token exists in `index.md`.

## B3 — body-prose rule refs (12 hits / 10 edits / 9 files)
All in narrative prose (Treatment sections / identity-note blockquotes / a Case-Index carry-forward
row), reworded by hand (not mechanically), legal meaning preserved, no new banned token introduced:

- **R15 treatment-audit refs ×6** (Ashcraft, Brendlin, Jacobson, Kuhlmann, Taylor, Van Leeuwen):
  `pending the R15 treatment audit` → `pending a treatment-history audit` (Ashcraft: `an R15 treatment
  audit is required` → `a treatment-history audit is required`). Report shape #4.
- **Florida v. Meyers** (L6/N1/SR-5, 3 hits, 1 edit): drop the provenance parenthetical
  `(L6 identity correction; SR-5/N1 caption fix)` from the caption/identity blockquote — the caption
  explanation stands on its own; which run flagged the fix has no reader value.
- **Florida v. White** (S4, 1 hit): drop `(S4 collisions ledger, Tier C)` from the identity note — the
  reader keeps the "distinct from the page-less unverifiable *United States v. White*" point.
- **Case Index** L494 (R10 + S7, 2 hits): Cruz/West/Jackson UNVERIFIABLE carry-forward row —
  `(R10 carry-forward)` → `(carried forward as an unverifiable caption)`; drop `at the S7 pass`.
  **Durable**: `build_case_index.py::flagged_rows` re-emits `cells[1]` (this Holding cell) verbatim on
  regen (recognized by the `UNVERIFIABLE` token in cell[0]), so the direct edit survives FIN-INDEX.

## B4 — `No standalone case page` meta-label (2 hits / `Entrapment.md`)
`(Binding in-circuit — 8th Cir.; no standalone case page)` → `(Binding in-circuit — 8th Cir.)`
(and the 1st-Cir. sibling). Report shape #5 — the S1 A8 weight label is reader-facing and kept; only
the editorial meta-label is dropped.

## P4-17(d) — lint FP handling (14 hits, no content edit)
- **Regex fix** (`lint11_pipeline_vocab.py`): class-3 `pending CL` gained a left word-boundary guard —
  `re.compile(r"(?<![A-Za-z])pending CL", re.IGNORECASE)`. The bare pattern fired inside
  `S|pending Cl|ause` (RLUIPA/§1983 pages). Clears all **8** pending-Cl FPs (Landor ×6, Case Index ×1,
  Suing Federal Officers ×1) — all confirmed to be "Spending Clause", none a status marker.
- **Allowlist seed** (`lint11-allowlist.json`, `adjudicated_hits`): the 5 report keys, wired to the
  committed exclusion design (`_load_allowlist` → per-hit `<relpath>:<match>` cleared under D10):
  `…Loines.md:wrapper`, `…Case Index.md:wrapper`, `…Plain View Doctrine.md:wrapper`,
  `…Robinson (4th Cir. en banc).md:split from`, `…CREW.md:placeholder`. Clears the **6** wrapper/
  split-from/placeholder FPs (physical cigar wrapper, circuit-split language, pedagogical placeholder).
- **Regression fixtures** (2, `scripts/lint/fixtures/`):
  `lint-11-class3-spending-clause-pass.md` (Spending Clause → 0 HIGH) and
  `lint-11-class3-pendingcl-fail.md` (genuine `pending CL` → 1 HIGH, guards against over-loosening).
- **Self-test: green** (`--self-test` exit 0; new fixtures OK; the existing class3-fail still fires on
  `CL-confirm pending` + `TODO`). The 14 FP rows drop **as designed** (not waived).

## P4-17(b) — 5 frontmatter `holding:` banned variants (durability, term-register canonical)
Frontmatter-only, per CAMP-A2's E1 escalation. These make the Case-Index source canonical so a
FIN-INDEX regen keeps CAMP-A2's rendered index cells clean (the E1 revert risk closes):

| page | holding: variant → canonical | register route |
|---|---|---|
| Carroll v. Carman | `'knock and talk'` → `'knock-and-talk'` | page |
| French v. Merrill | `'knock and talk'` → `'knock-and-talk'` | page |
| United States v. Meyer | `'knock and talk'` → `'knock-and-talk'` | page |
| Haynes v. Washington | `totality of circumstances` → `totality of the circumstances` | glossary |
| United States v. Satterfield | `inevitable-discovery` → `inevitable discovery` | page |

- **Carroll**: targeted `'knock and talk' exception` (holding) so the **verbatim SCOTUS quotation** on
  the body (`conduct a 'knock and talk' at any entrance`) is never edited (quote-preservation rule).
- **Haynes**: fixed the `holding:` occurrence only (`… totality of the circumstances and inadmissible`).
  A **co-located `scope_note` occurrence** (`… under the totality of circumstances`) carries the same
  variant but is **out of the sanctioned `holding:`-only scope** and not rendered where any lint scans;
  left untouched, flagged here for orchestrator awareness (matches CAMP-A2's holding:-only pattern).

## Verification
- `python3 scripts/lint/lint11_pipeline_vocab.py content` → **1 high** (Christensen R11 residual);
  all 11 WB1 scope files individually = 0.
- `python3 scripts/lint/lint11_pipeline_vocab.py --self-test` → **PASS** (exit 0).
- LINT-7 on the 5 frontmatter pages → **0 HIGH** (no regression; `holding:`/`scope_note` are masked from
  the prose scan). 1 pre-existing MEDIUM (`Satterfield` L80, body wikilink display `inevitable
  discovery` unlinked, S8-coverage-linker class per P4-17(e)) — **not introduced by this packet** (my
  edit touched only frontmatter L48; the git hunk confirms no body change).

## Escalation — 1 discovered docket FP (not self-adjudicated)
`content/cases/State v. Christensen.md` L52 `R11` is a **false positive**: `R11` is a substring of the
Tennessee docket `No. W2014-00931-SC-R11-CD` (Tenn. R. App. P. 11 application), not a rule ref. It is
**not** among the report's enumerated 14 FP nor sanctioned in P4-17(d), so per writer≠checker I did not
alter the (correct) docket, nor self-adjudicate a 6th allowlist entry. **Recommendation** (orchestrator
adjudicates): add `content/cases/State v. Christensen.md:R11` to `adjudicated_hits` (in-design, D10),
**or** add a docket-suffix `safe_context_patterns` entry for hyphen-embedded `-R\d{1,2}-` tokens. Until
then LINT-11 whole-content sits at **1 high** (this row).

## Notes on the concurrent working tree
The tree is a shared fleet workspace; other lanes wrote during this packet (e.g. CAMP-A1 LINT-10
em-dash edits landed in `content/index.md`; another lane reworded `S9 promotion` status prose in several
case pages). My read-modify-write applier preserved on-disk concurrent edits (verified: index.md carries
both my 41 comments and CAMP-A1's em-dash→colon edits; no clobber). No commit made (not requested).

## Coverage ledger
`CAMP-WB1-fixes.jsonl` — 77 rows: 58 content edits (B1 41 / B3 10 / B4 2 / FM 5) + 14 FP-clearance rows
+ 4 lint-change meta rows + 1 escalation row. Applied via a two-phase validating applier (phase-1
asserted every old-string's exact occurrence count — all 18 edit-specs passed; phase-2 all-or-nothing).

## Method / evidence
- Harvest + delta: `lint11_pipeline_vocab.py content` (before 152 / after 1) + per-file re-scan.
- FP contexts read and confirmed (8 Spending Clause; 4 physical cigar wrappers; 1 circuit-split
  "split from"; 1 pedagogical placeholder) before any suppression.
- Case-Index durability confirmed by reading `build_case_index.py::flagged_rows`/`_split_cells`.
- Register canonical forms from `scripts/lint/term-register.yml` (same doctrine as CAMP-A2).
- No CourtListener / no lake reads (pure text normalization + lint-code fix).
