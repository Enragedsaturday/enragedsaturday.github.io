# R8 Wave W10 report — LINT-17 first-catch mini-wave (2026-07-07)

Lane `r8-wave-author` · model `claude-opus-4-8` · branch `overhaul2/execute` (from HEAD d994871) ·
**committed nothing** (orchestrator commits the batch gate). Combined leg: S2 stub creation + R8
authoring for the three page-less, R2-clearing SCOTUS landmarks the orchestrator adjudicated as
page rows at **d1cc0df** (S6-CLOSEOUT §Escalations / LINT-17's first pre-CI catches).

## Per-caption outcome (3/3 minted, born under_review ⚪)

| Caption | Cluster | Cite (two-key) | Docket | Decided | Home(s) → role | Rule pincite |
|---|---|---|---|---|---|---|
| Anderson v. Creighton | 111953 | 483 U.S. 635 (1987) | 85-1520 | 1987-06-25 | Section 1983 Liability and Qualified Immunity → Key (particularized "clearly established") | *640 (Scalia); *641 |
| Bell v. Wolfish | 110075 | 441 U.S. 520 (1979) | 77-1829 | 1979-05-14 | Special Needs and Administrative Searches → Key (institutional-deference balancing); Search Incident to Arrest → Related | *559 (Rehnquist — the four *Wolfish* factors) |
| Colonnade Catering Corp. v. United States | 108077 | 397 U.S. 72 (1970) | 108 | 1970-02-25 | Special Needs and Administrative Searches → Key (closely-regulated industry) | *76, *77 (Douglas) |

All three: **minted** (`COMMITTED`), 0 staged mint-gate lint findings (LINT-13/14/15/16 = 0),
lake stub cleanly promoted (record_id → page stem, `stub` dropped, status `under_review`), page +
`s6-authored-ledger.jsonl` row + `_manifest.json` rename written by the CLI.

## Stub leg — path taken (standard machinery, reported per work order)

De-novo frontier stubs created entirely through existing `scripts/s2/ingest.py` bounded surfaces
(no hand-written records):
1. `--add-candidates _run/o2-execute/w10/candidates.jsonl` — offline seed of 3 pending frontier
   stubs (caption + leg `lint17-catch` + `expected_citation` + court). 0 CL.
2. `--smoke <slug>` ×3 — `process_frontier_record` ran the **R1 two-key identity** search (CL
   cluster located by caption; the expected citation as the independent key). All three:
   `canonical_name_match=true`, `expected_citation_found=true`, `reason_code=null`, single
   candidate (no namesake alternates). 2 CL calls each = **6 CL, 0×429**.
3. `--enrich-citations _run/o2-execute/w10/w10-record-ids.txt` — populated `citations.display`
   (+ selected U.S. official) from `cluster.citations[]`. **cache-hits 3, 0 network.**
4. `--repair-identity-from-cache` ×3 — forced `court_level=scotus`/`court_id=scotus` and set
   **authoritative `date_decided`/`year`** from the cached cluster (`date_filed`). **cache-served,
   0 CL.** This corrected Colonnade's date from my seed guess 1970-03-05 → CL-authoritative
   **1970-02-25**, later confirmed against the opinion caption ("Decided February 25, 1970").

Post-plumbing the 3 stubs projected clean (`Binding — SCOTUS`, cite-with-year) and passed
**LINT-13 = 0**. Dockets (85-1520 / 77-1829 / 108) were confirmed **on-read** from the CL
lead-opinion captions and written to `identity.docket` (with a provenance warning noting the
on-read source) so the projected header carries them.

## Authoring leg — on-read re-verification + verbatim quotes (CL MCP)

Identity re-verified and Rule/Application quotes string-matched **verbatim** against the CL opinion
text (`read_document`/`search_document` on the lead opinions 111953 / 110075 / 108077):
- **Anderson** — "The contours of the right must be sufficiently clear that a reasonable official
  would understand that what he is doing violates that right." (*640); the objective
  reasonable-officer question (*641).
- **Bell v. Wolfish** — the reasonableness-balancing test and the four *Wolfish* factors (*559).
- **Colonnade** — congressional inspection power over the closely-regulated liquor industry (*76);
  the statute authorized a fine, "not … forcible entries without a warrant" (*77).

Pages authored to the specimen/A-Quantity register (born-under_review ⚪ banner, honest
"not machine-certified" status notes; no officer-BLUF). Worklist rows added (`R8-WORKLIST.json`,
leg `lint17-catch`, basis `D1-flip`, in-row d1cc0df provenance; counts.pages 147→**151**,
`lint17_catches: 3`). W10 batch appended to `R8-WAVE-PLAN.json` (status `authored`, minted 3).

## Partition arithmetic (R11 coverage ledger, re-run `--write`)

**PASS.** authored **145 → 148**; TOTAL **240 → 243 distinct captions** (expected 243):
`authored 148 + brief-mention 55 + excluded-remit 26 + folded-alias 8 + removed 2 + unverifiable 1
+ watch 3 = 243`. authored-verified page=148 rec=148 rename=148; conflicts 0; row-errors 0.
`corpus_mention_baseline` 58 → **56** (escalations **3 → 0** — the three moved out to `authored`;
net −2 because Anderson's prose names the page-less antecedent *Mitchell v. Forsyth*, now a
legitimate NUM-04 brief-mention row, +1). All three targets classify as **`page`** (page-backed),
not allowlist.

## Build + lint delta

- `npx quartz build`: **SUCCESS** (719 input files, 2710 emitted, 0 errors; only the expected
  untracked-git-date warnings on the 3 new, uncommitted pages).
- `scripts/build_case_index.py`: rows 614 → **617** (+3 exactly; diff = my 3 rows).
- **LINT-17 corpus run: 0 high / 0 total — PASS**, with all three captions genuinely `page`-backed.
- **Mint-gate lints (LINT-13/14/15/16): 0** on the 3 pages (the enforced authoring gate).
- Other findings on the 3 new pages are **entirely pre-existing corpus-wide known-red classes**
  owned by S7/S8/S9 cleanup, at template-consistent density — **no new class, none mint-gate**:
  - **LINT-10** (em-dash budget): ~15 highs across the 3 pages. Fires on **598/~660 case pages**
    including the specimen *United States v. Smith (2024)* and the *A Quantity* / *Arkansas v.
    Sanders* under_review templates I was told to match. S7/S8 corpus cleanup.
  - **LINT-5** (bare case name not wikilinked): ~10 on the 3 pages + **3 newly-triggered on the
    reliance pages** (White v. Pauly, Florence, Biswell) — authoring the pages creates the link
    targets; wiring bare mentions is the **S8 linking pass** (I may not edit those pages). Known-red.
  - **LINT-9** (mid-line block anchor renders visibly): 1 (Colonnade `^pin-76`). Identical pattern
    to the reliance page **White v. Pauly `^pin-73`** (298 highs corpus-wide); tagged "[S9 R8 #9]"
    → S9 anchor-placement cleanup. Not re-milled: the CLI is a no-op on an already-authored row and
    editing a minted page is outside my lane.
  - **LINT-2** (inline quote without nearby pincite): 1 (Anderson, quoting White v. Pauly's "at a
    high level of generality"). Same class fires 3× on White v. Pauly (303 corpus-wide).

## Quote-fidelity self-check
All pinned quotes copied verbatim from the CL `html_with_citations` text with their star-page
pincites; Sources bullets carry the string-match note (2026-07-07). Treatment prose is honest to
the `unverified`/under_review status (⚪), not machine-certified — S9 certifies (writer≠checker).

## CL lane
**16 CL calls total, 0×429** (6 REST frontier-identity smokes; enrich + repair cache-served/0;
10 MCP reads/searches). Serial single-lane throughout; slightly above the ~10–15 estimate due to
Colonnade's multi-chunk opinion reads.

## Escalations / ambiguities
None blocking. Colonnade date discrepancy (seed vs cache) resolved by `--repair-identity-from-cache`
and confirmed against the opinion caption. §9 scope guard (>150 pages) crossed by design
(148→151 page rows) under the explicit orchestrator adjudication at d1cc0df.

## Files
- `content/cases/{Anderson v. Creighton,Bell v. Wolfish,Colonnade Catering Corp. v. United States}.md`
- `_overhaul2/lake/cases/{Anderson v. Creighton,Bell v. Wolfish,Colonnade Catering Corp. v. United States}.json` (promoted, under_review)
- `_overhaul2/lake/_manifest.json` · `_run/o2-execute/s6-authored-ledger.jsonl` (+3) · `_run/s6-coverage-ledger.json` (243)
- `_run/o2-execute/R8-WORKLIST.json` (+3 rows) · `_run/o2-execute/R8-WAVE-PLAN.json` (+W10) · `content/legal-system-research-and-reference/Case Index.md` (617)
- scratch: `_run/o2-execute/w10/{candidates.jsonl,w10-record-ids.txt,*-payload.md}`
