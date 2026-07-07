# R8 authoring-pipeline build report — `scripts/s6/mint_page.py`, 2026-07-07

Builder lane: `claude-opus-4-8` (O2 EXECUTE, branch `overhaul2/execute`, from HEAD `d28e200`).
Scope: BUILD the S6 R8 promotion/mint CLI only. **Committed nothing. Zero CL/network calls.
No real-lake mutation** (the `--write` path was exercised only inside private temp sandboxes and
against fixtures). No page prose authored.

Writer≠checker: this report + the diff go to the review lane; the orchestrator commits.

> **LOOP-2 APPLIED (2026-07-07, post-`R8-PIPELINE-ADJUDICATION.md`).** All four escalations
> adjudicated. The Case-Index and homes-page **write surfaces were removed**; the ledger was
> **enriched** for S7 materialization + the generator. Sections 1–5 below are updated in place;
> **§8 records the loop-2 delta**; §6 escalations are annotated with their dispositions.
>
> **LOOP-3 APPLIED (2026-07-07, post-`r8-pipeline-review-ledger.json`, FINAL loop).** The
> writer≠checker review returned **12 findings, all UPHELD**; every fix applied. Completion
> detection is now **lake-derived** with crash-tail **roll-forward** + `wedged-partial-state`
> refusal; the stub gate, manifest cross-check + record flip, homes/roles bijection, and global
> record_id uniqueness are all wired fail-closed; commit-time rollback is now covered by a
> failure-injection test. **§9 records the loop-3 delta.** Final: **self-test 36/36 PASS ·
> specimen PASS.**

---

## 1. Files created

| Path | What |
|---|---|
| `scripts/s6/__init__.py` | package marker |
| `scripts/s6/mint_page.py` | the mint/promotion CLI + library (dry-run default, `--write` guarded, self-tested) |
| `scripts/s6/fixtures/stub-fixture-alpha.json` | SCOTUS `verified_identity` stub — happy path |
| `scripts/s6/fixtures/stub-fixture-collision.json` | 9th-Cir. stub, caption collides with an existing page — R9 disambiguation |
| `scripts/s6/fixtures/stub-fixture-wrongstatus.json` | `not_found` stub — wrong-status refusal |
| `scripts/s6/fixtures/stub-fixture-history.json` | `superseded/not_current` stub — history-class |
| `scripts/s6/fixtures/manifest-fixture.json` | sandbox manifest (`renames: []`) |
| `scripts/s6/fixtures/worklist-fixture.json` | sandbox worklist (4 rows, mirrors the real row shape) |
| `scripts/s6/fixtures/worklist-missing-home.json` | worklist whose home points at a nonexistent page (missing-home refusal) |
| `scripts/s6/fixtures/home-key-r6.md` | doctrine page — a `homes[]` **existence** target (schema now irrelevant) |
| `scripts/s6/fixtures/home-related-r6.md` | doctrine page — a `homes[]` **existence** target |
| `scripts/s6/fixtures/existing-collision-page.md` | a pre-existing `Fixture Collision Case.md` case page |
| `scripts/s6/fixtures/payload-alpha.md` | born-conformant payload (content frontmatter + `placements[]` + BIRAC body) |
| `scripts/s6/fixtures/payload-collision.md` | payload whose H1 = the disambiguated stem |
| `scripts/s6/fixtures/payload-history.md` | PRACTICES §7 history-rendered payload |
| `scripts/s6/fixtures/payload-bad-skeleton.md` | BIRAC-broken payload (missing `## Issue`) — lint-fail rollback |

*(Loop-2 removed three now-unused fixtures: `case-index-r6.md`, `home-legacy.md`,
`worklist-legacy-home.json` — the index/homes write surfaces they exercised are gone.)*

No files outside `scripts/s6/` were modified (the `_run/o2-execute/JOURNAL.md` change in the working
tree is the orchestrator's own adjudication journaling, not this lane's). **Reuse, not reimplementation:** projection comes
entirely from `scripts/s2/project.py::project_record` + `scripts/s2/serializer.py`
(`compose_projected_frontmatter`, `dumps_frontmatter`, `managed_subset`, `diff_paths`); table/section
parsing + schema constants from `scripts/lint/_common.py`; the staged-state lints invoke
`lint15_skeleton.check_file`, `lint16_casetables.check_file`, `lint14_pagerecord.check_page`
directly. The s2 projector self-test still passes (no regression).

---

## 2. CLI surface

```
python3 scripts/s6/mint_page.py --row <record_id> --payload <body.md>            # dry-run (default)
python3 scripts/s6/mint_page.py --row <record_id> --payload <body.md> --as-of <ISO> --write
python3 scripts/s6/mint_page.py --validate-only --row <record_id> --payload <body.md>
python3 scripts/s6/mint_page.py --self-test
python3 scripts/s6/mint_page.py --specimen-test
```

Flags: `--row`, `--payload`, `--as-of <ISO>` (required with `--write`), `--write` (guarded),
`--born-status {under_review,draft}` (default `under_review`), `--worklist`, `--lake-root`,
`--content-root`, `--ledger`, `--summary-json`, `--validate-only`, `--self-test`, `--specimen-test`.

**Exit codes:** `0` = dry-run clean / `--write` committed / `already-authored` no-op / self+specimen
pass. `2` = any refusal (worklist-absent, wrong-status, missing-citation, payload-invalid,
staged-lint-failed, home-page-missing, stem-collision, as-of-required, …) — each printed as
`REFUSED [<code>]: <message>` and available via `--summary-json`. `1` = self-test/specimen failure.

**Machine-readable refusal codes (loop-3):** `worklist-absent`, `no-lake-record`, `wrong-status`,
`not-a-stub`, `record-missing-citation`, `history-class-mismatch`, `stem-contains-double-dash`,
`stem-collision-distinct-case`, `record-id-collision`, `homes-roles-desync`,
`manifest-missing-record`, `wedged-partial-state`, `payload-invalid`, `staged-lint-failed`,
`home-page-missing`, `as-of-required`. *(Retired in loop-2: `case-index-not-r6-converted`,
`home-not-r6-converted`, `placement-missing`.)* A `--write` on a crash-tail row reports **RECONCILED**
(exit 0) rather than a refusal.

---

## 3. What one invocation does (all-or-nothing)

Given a worklist `--row` + a `--payload`, `plan_mint()` builds and validates the plan; `--write`
`commit_plan()`s it. **Loop-2 atomic commit** (index/homes writes removed): (1)
`content/cases/<stem>.md`; (2) lake rename (write `<stem>.json`, remove `<record_id>.json`); (3)
`_manifest.json` rename entry + record flip; (4) ledger append **last**. In-memory backups +
reverse-order rollback (including ledger truncation and rename restore) on any failure. Staging +
lints run inside a temp mirror — the real tree is never touched until the commit phase. The **only**
file the CLI creates in `content/` is the born case page; the Case Index is regenerated by
`scripts/build_case_index.py` per wave batch, and the homes-page Key/Related rows are materialized by
S7 from the ledger. Every `homes[]` target is still existence-checked (`home-page-missing` refusal).

Verified end-to-end (fixture sandbox commit): the born page carries the S2-projected data
frontmatter + worklist-derived `homes`/`aliases` + payload `related`/`tags`/`holding`, born
`lake.status: under_review`, exact BIRAC skeleton — **LINT-15/16/14 = 0/0/0**. No Case Index or homes
page is written. The lake record is renamed (`record_id`=stem, `stub` dropped, status→born-status),
the manifest carries the rename entry, and the enriched ledger `authored` row is appended (see §8).

---

## 4. Design decisions (where the order left latitude)

**Payload interface.** The work order calls the payload "the authored page body (everything below the
frontmatter)". Realized as: the payload is a full markdown file; the CLI takes the **body** from below
the frontmatter and reads the author's **frontmatter** for the content-owned preserved fields —
`related`, `tags`, `holding`, optional `aliases`, and a `placements[]` block. The CLI **owns the data
frontmatter** (from the S2 projection — the R7 boundary is enforced at the frontmatter level, the
author cannot drift weight/treatment/dates/cite) and **generates** `title`/`type`/`homes`/`aliases`
from the worklist (ground truth). `placements[]` supplies the per-home row cells (a Key row's holding
cell — falls back to the `holding` first sentence; a Related row's `tag`+relevance `cell`+
`primary_home`), because those cells are authored content, not derivable data. The CLI refuses if the
payload H1 ≠ the computed stem.

**Stem rule (A6/R9).** Stem = caption. Collision with a *distinct* existing case page →
`caption (year)`, then `caption (court year)`; refuse if neither is free. Refuse a caption carrying the
reserved `--`. Standing exhibit: the two-Smiths → `United States v. Smith (2024)`.

**Status-acceptance set.** Mint iff the **lake record** is `stub: true` AND `status ∈ {verified_identity,
verified, verified_off_cl}`. All 148 signed rows are `verified_identity`; `verified` covers the
re-key-gated packet-B rows (Wyman/GM-Leasing/Verdugo — `packetb-dispositions.jsonl`) and a re-promoted
record; `verified_off_cl` covers the A17 English-corpus elevations. Everything else
(`not_found`, `fabrication_suspected`, `folded-alias`, bare `under_review`) is refused.

**Born status.** Default `under_review` (see Escalation 1). `--born-status draft` selects R8's literal
word; because stock LINT-14 skips draft pages, draft mode runs an explicit draft-inclusive page↔record
binding sub-check so the staged binding is still validated. R15 renders the identical ⚪ banner for both.

**Staged-lint semantics.** The **new page** must be absolutely clean — zero LINT-15 (case) + LINT-16
findings at **any** severity (LINT-15's BIRAC drift is MEDIUM, so a HIGH-only gate would let a
mis-sequenced page through) + zero LINT-14 binding findings. **Touched existing files** (Case Index,
homes) are validated by a **location-independent violation-signature delta**: no NEW signature vs the
pre-insert baseline. This is required because the ambient corpus is mid-restructure red (legacy tables,
`## Recent developments`); the delta guarantees the inserted row introduces no regression, while the
R6-target gate guarantees the row itself is sanctioned.

**Determinism.** `--as-of <ISO>` is required for `--write` (validated ISO); the promoted record's
`provenance.date_modified`/`projected_at` derive from it; the ledger `ts`/`as_of` derive from it. No
wall-clock read feeds any journaled value.

**History class (D2/PRACTICES §7).** For `special: [history-render]` rows the CLI verifies the lake
record's Field-I is a history/superseded class (not `good_law`) so the page cannot fight the banner
(`history-class-mismatch` refusal otherwise). The payload authors the verb + forward-pointer + demotion.

---

## 5. Test results

- **Self-test (`--self-test`): PASS, 21/21 (loop-2).** Covers: worklist-absent refusal · wrong-status
  refusal · happy-path plan (**no index/home file writes** + alias + born `under_review`) · commit
  (page created, lake renamed to stem, **no Case Index written, home page unmodified**, enriched ledger
  `authored` row carrying cite/year/opinion + `home_rows` role_class + `Extends` relevance-tag hint +
  Key `holding_cell_hint`) · idempotent `already-authored` no-op on re-run · collision disambiguation →
  `Fixture Collision Case (2021)` · history-class plan · bad-skeleton lint-fail **rollback with no
  partial write** · **missing-home target refusal** (`home-page-missing`). Private temp sandboxes only.
- **Specimen test (`--specimen-test`): PASS.** Over the live `United States v. Smith (2024)`:
  (a) the payload-body validator passes on the page body (0 errors); (b) LINT-15/16 on the live page
  are 0/0; (c) `project_record(smith_record)` **deep-equals** the page's managed frontmatter (0 diffs,
  the only permitted delta being `lake.status`).
- **Real-data dry-runs (no writes):** a real no-citation stub (`alasaad-v-wolf--4855246`) → clean
  `record-missing-citation` refusal; a worklist-absent row → exit 2; `--write` without `--as-of` →
  clean `as-of-required` refusal (exit 2). The only working-tree change outside `scripts/s6/` is the
  orchestrator's own `JOURNAL.md` adjudication entry (not this lane's).

---

## 6. ESCALATIONS — all adjudicated (`R8-PIPELINE-ADJUDICATION.md`, 2026-07-07)

> **E1 → RATIFIED** (`under_review` default stands; `draft` stays as the unused escape hatch — no
> code change). **E2 + E3 → NO corpus-wide convert-first**; instead the CLI's **Case-Index insertion
> surface was removed** (single writer = `scripts/build_case_index.py`, regenerated per wave batch)
> and the **homes-page row insertion was ledger-deferred to S7** (S7 materializes Key/Related rows
> from `s6-authored-ledger.jsonl` at per-page conversion). **E4 → separate lane** (`--enrich-citations`
> ingest surface over the 80 record_ids); the `record-missing-citation` fail-close stays as built.
> The original escalation text is preserved below for the record.

**E1 — Born status: R8 "draft" vs S6 §8 "under_review".** R8's prose says pages are born
`lake.status: draft`; S6 §8 says the specimen "carries `under_review` until the gates pass". These
diverge for LINT-14: `draft` pages are *skipped* by the stock page↔record gate, so a literal-draft mint
would make the work order's mandated "LINT-14 page↔record against the staged state" a no-op. I defaulted
to **`under_review`** (LINT-14-meaningful; R15 renders the same ⚪ banner) and exposed `--born-status
draft` (with a draft-inclusive binding sub-check). **Needs ratification** of the default, or a directive
to flip it.

**E2 — The Case Index + every homes page are still in LEGACY (pre-S5-converter) schema; R6 row
insertion is impossible until `convert_tables.py` runs.** Confirmed on the branch: the live Case Index
is the 5-col `| Case | Holding | Good law | Home page(s) | CourtListener |`, and homes pages
(e.g. `Border Searches.md`, TPD `index.md`) carry 5-/6-col legacy Key/Related tables + `## Recent
developments`. The Smith specimen itself was inserted into the **legacy** Case Index (row 451) and was
**not** inserted into any homes-page Key table. The CLI **fail-closes** on legacy targets
(`case-index-not-r6-converted` / `home-not-r6-converted`) rather than guess a legacy row (which would
require authoring banned data cells — weight/treatment/dates — into the cells, violating R7). **This is
a hard sequencing dependency:** S5 `convert_tables.py` must run on the Case Index + every `homes[]`
page *before* the R8 authoring wave inserts rows, **or** the orchestrator must direct a legacy-adaptive
insertion mode (not built — I declined to author legacy data cells). Which path?

**E3 — Work order says "Case-Index row = R6 schema 3", but the live index + the specimen used the legacy
5-col schema.** Same root as E2. The CLI targets R6 schema-3 (the S3-regenerated end state) and refuses
legacy. Confirm that convert-first is the intended plan (so the tool never has to emit a legacy row).

**E4 (readiness, not a spec conflict) — 80 of the 148 signed stubs have no projected citation yet.**
Their `citations` lane is still `pending`, so `project_record` yields an empty `citation`, and the CLI
fail-closes with `record-missing-citation` (a born page cannot carry its header-line/Sources cite
without it). The S2 builder lane must populate citations for those 80 records before they can mint. The
68 with citations are mintable now (subject to E2/E3).

---

## 7. What I did NOT cover (journal-grade)

- **No real promotions / no real-lake mutation / no committed pages** — only fixture sandboxes + dry-runs.
- **The 58 non-page placements** (`R8-NONPAGE-LEDGER.json`) — separate lane (work order out-of-scope).
- **LINT-17** (R12 CI lint) — separate work order.
- **R11 ledger fold** — the CLI appends the `authored` row to `s6-authored-ledger.jsonl`; folding it
  into `_run/s6-coverage-ledger.json` is R11's later step, not built here.
- **`verified_off_cl` minting** — **ADJUDICATED-DEFERRED** (`R8-PIPELINE-ADJUDICATION.md` §Deferred):
  accepted by the status gate, but the born-status override drops the projector's `off_cl_links`
  branch, so an off-CL record's `opinion_url` in the ledger would come out empty. No `verified_off_cl`
  row exists in the 148; the fix rides the next `scripts/s6/` touch or before any A17 page routes
  through R8. Not handled this loop, by design.
- **The R5 point-status table** in a `varies_by_point` page body is authored by the payload; the CLI
  projects `point_overrides` into frontmatter but does not reconcile the body table against the lake
  (S9's coherence gate owns that). LINT-16 treats the point-status table as its carve-out.
- **"Appears on" ↔ homes cross-check**: the CLI generates `homes[]` frontmatter from the worklist but
  does not assert the payload's `## Appears on` body section lists each home (soft; addable).
- **CodeRabbit gate**: not run here — `scripts/s6/` is queued for the standing S6-code review on PR #3
  (RUNBOOK §5), per the work order's process note.

*(Loop-2 retired two prior not-covered items: grouped Key-cases sub-table selection is moot — the CLI
no longer writes homes rows, so it becomes S7 materialization guidance; the R6 schema-3 Case Index
flip is owed at S7/S8 with the generator change, per the adjudication.)*

---

## 8. Loop-2 delta (post-adjudication amendments applied)

**Surfaces REMOVED from the CLI (E2/E3):**
- The **Case-Index row insertion** (and refusal `case-index-not-r6-converted`). The Case Index has a
  single writer — `scripts/build_case_index.py`, regenerated per wave batch — which reads exactly what
  the mint already produces (payload-merged `holding:` frontmatter + projected `homes` + opinion URL).
- The **homes-page Key/Related row insertion** (and refusal `home-not-r6-converted`, plus the now-moot
  `placement-missing`). S7 materializes those rows from `s6-authored-ledger.jsonl` when it converts each
  home page. The `homes[]` **existence** validation (`home-page-missing`) is **KEPT**.
- Consequently the atomic commit no longer touches `content/` beyond the born case page, and the
  staged-lint step now validates only the born page (touched-file delta list is empty). The
  location-independent delta machinery remains in place for that empty set (no behavior change; still
  correct if a future touched-file surface returns).

**Ledger ENRICHED for downstream materialization (E2/E3(b)):** the `authored` row now carries, in
addition to the loop-1 fields, everything S7 needs to write a schema-1/2 row and the generator needs
for the index — `cite` (display, with year), `year`, `court`, `authority_weight`, `opinion_url`,
`holding`, `primary_home`, and a `home_rows[]` array: per worklist home `{home, role, role_class,
schema}` plus, for Key `holding_cell_hint` (payload placement → else `holding` first sentence) and for
Related `relevance_tag_hint` (payload tag → else the R6 tag extracted from the worklist `note`) +
`relevance_cell_hint` + `primary_home`. Also `worklist_note` verbatim. Verified in the self-test
(`ledger carries cite + year`, `home_rows carry role_class + tag hint`, `carries opinion_url`).

**Payload interface change:** `placements[]` is now **optional** (S7 authors the final relevance/holding
text at conversion). When present, its `cell`/`tag`/`primary_home` are folded into the ledger
`home_rows` hints. `related`/`tags`/`holding` in the payload frontmatter are unchanged.

**Tests changed:** self-test **19/19 → 21/21** — dropped the two "index/home row inserted + clean"
assertions and the legacy-home refusal; added "no index/home file writes", "no Case Index written",
"home page unmodified", three ledger-enrichment assertions, and a `home-page-missing` refusal.
Fixtures removed: `case-index-r6.md`, `home-legacy.md`, `worklist-legacy-home.json`; added:
`worklist-missing-home.json`. Specimen test unchanged — still **PASS**.

**Unchanged (E1, E4):** born-status default `under_review` (ratified; `draft` escape hatch retained);
`record-missing-citation` fail-close (E4 citation enrichment is a parallel S2 lane).

---

## 9. Loop-3 delta (review findings F-R8-01…12, all UPHELD, all fixed)

- **F-R8-01 (HIGH) — stub gate wired.** `if not record.get("stub"): return refuse(REFUSE_NOT_A_STUB…)`
  — R8 mints only from stubs; a page-backed record is refused, never promoted-over. Defense-in-depth:
  the lake-rename skips the `os.remove` when `old == new` (a same-stem rename can never delete a record).
- **F-R8-02 (HIGH) — completion is now LAKE-DERIVED, with roll-forward.** `plan_mint` classifies the
  on-disk state (old json / promoted `<stem>.json` via the `provenance.s6_promotion` marker / page /
  manifest entry / ledger row) into **fresh / already-authored / crash-tail-reconcile /
  wedged-partial**. A crash-tail (page + lake-rename landed, manifest/ledger did not) **rolls forward**
  the missing steps 4–5, journaled `terminal: reconciled`; anything else half-committed refuses
  `wedged-partial-state`. The ledger is still written **last** (never a fabricated authored claim); the
  `os.remove` orphan is closed by recording the rollback marker **before** the remove. Idempotency no
  longer keys on the mutable manifest `renames`.
- **F-R8-03 (MED) — manifest cross-check + record-flip test.** Plan-time fail-closed
  `REFUSE_MANIFEST_MISSING_RECORD` when the row's lake record is absent from the manifest; a self-test
  asserts the post-commit manifest gained the rename entry AND the flipped record.
- **F-R8-04 (MED) — manifest treated as authoritative.** On promotion the record's stale fields are
  refreshed (`slug`/`title`/`caption`/`record_id_status`/`source`/`lane_status.identity`), and a
  file-level `s6_mutations[]` provenance stamp is appended **without** touching `generated_*`/`build_id`.
- **F-R8-05 (MED) — commit-time failure-injection test.** Monkeypatches `_append_ledger` to write a
  partial line then raise mid-commit, asserting page (absent), old lake record (byte-restored), new lake
  record (removed), manifest (byte-restored), and ledger (truncated to pre-size) are all restored.
- **F-R8-06 (MED) — homes/roles bijection, fail-closed.** `homes_roles_desync()` refuses any home
  without a role (or role without a home / blank / duplicate) — no silent `Key` default. Verified across
  all 148 signed worklist rows (0 desync after the coordinator's Gaetjens fix).
- **F-R8-07 (LOW)** — court-fallback stem built from non-empty parts (`Caption (ca9)`, never
  `Caption (ca9 )`); redundant `.rstrip()` removed.
- **F-R8-08 (LOW)** — every `## Sources` bullet must now be the bracketed `- [...](...)` form (a plain
  or em-dash bullet is rejected), not just the retired em-dash form.
- **F-R8-09 (LOW)** — each `home_rows[]` entry denormalizes `stem` (= `record_id_after`, the Case-cell
  wikilink target, NOT `caption`) and `cite`, so S7 needs no row-level join.
- **F-R8-10 (LOW)** — dead code removed: the unused `import datetime as dt` (the file's only wall-clock
  module — its absence is the determinism guarantee), the unused `created` list, the redundant
  `.rstrip()`, and the now-unused `SOURCES_BULLET_BAD_RE`.
- **F-R8-11 (LOW)** — no code change (worklist data; the `home-page-missing` gate stays as-is). The
  `Emergency Aid.md` home readiness blocker is a wave-sequencing item for the orchestrator.
- **F-R8-12 (LOW)** — plan-time global record_id uniqueness: `global_record_id_conflict()` refuses
  `record-id-collision` if a foreign lake record already holds `record_id == stem`.

**Tests:** self-test **21/21 → 36/36** — added non-stub, homes/roles-desync, manifest-missing,
record-id-collision, commit-time failure-injection rollback (6 assertions), crash-tail reconcile (3),
wedged-partial, and manifest rename-entry + record-flip + provenance + denorm-stem/cite assertions.
Specimen test unchanged — still **PASS**. No new fixture files (loop-3 variants are built in-sandbox).

**Not mine in the working tree:** the ~40 `_overhaul2/lake/**`, `_manifest.json`, `scripts/s2/ingest.py`
(+509 lines = the `--enrich-citations` surface), `R8-WORKLIST.json` (Gaetjens fix), and `JOURNAL.md`
modifications are the **parallel E4 citations-enrichment lane** + orchestrator journaling — this lane
touched only `scripts/s6/**` and this report, and mutated no real-lake data (self-tests run in temp
sandboxes; dry-runs never write).

---

## 10. Addendum — schema/mint coherence fix (2026-07-07, W1-blocking)

The recovery lane (`R8-CITE-RECOVERY-REPORT.md`, finding 1) surfaced that every record the mint
promotes carries `provenance.s6_promotion` (the F-R8-02 completion marker), but
`_overhaul2/lake/_schema.json` `definitions.provenance` is `additionalProperties: false` — so the
15 records W1 had minted all FAILED LINT-13, blocking W1's batch-close gate.

**Fix (additive, this lane):** added an **optional** `s6_promotion` property to
`definitions.provenance.properties` matching the exact on-disk shape the CLI writes (verified against
`promote_record` + a real minted record, `Nieves v. Bartlett.json`):
`{from_record_id: string, to_record_id: string, as_of: string, born_status: string∈{under_review,
draft}}`, itself `additionalProperties: false` with all four keys required. It is NOT added to
`provenance.required` (a non-promoted record has no marker). The recovery lane's uncommitted
`web_leg`/`web_legs` extensions were left intact (edited additively, not clobbered).

**Manifest side:** LINT-13 validates the manifest only for `record_id` uniqueness + JSON parse (no
schema validation), so the manifest's `s6_mutations[]` + rename entries (15 present from W1) need no
schema coverage — LINT-13 reads 0 with them present. No manifest schema change made.

**Coverage:** two auto-discovered LINT-13 fixtures — `lint-13-record-s6promotion-pass.json` (a real
minted record WITH the marker → 0 viol) and `lint-13-record-s6promotion-malformed-fail.json`
(off-enum `born_status` → 1 viol). LINT-13 `--self-test` PASS.

**Before/after (full real lake):** LINT-13 **15 → 0** violations; all 15 (now 15) `s6_promotion`
records pass; every prior violation was the `s6_promotion` `additionalProperties` rejection and no
other violation changed, so the total delta vs pre-W1 (zero minted records → zero such violations)
is **0**. Files touched: `_overhaul2/lake/_schema.json` + the two fixtures + this addendum (no
lake-record writes, no `scripts/s2/`).

---

## 11. Addendum — LINT-6 / R15 banner-state coherence (2026-07-07, W1-blocking)

W1's batch report flagged **LINT-6 ×15 HIGH** on the minted pages. Verified (not assumed) by running
LINT-6 on the 15 minted content pages: every one is check **(d)** —
`treatment is 'unverified' but the page is not draft: true — unverified must never reach a reader
unbannered [R2]`. Root cause: these GAP/sweep stubs are identity-only (SD10; treatment not yet
derived) so `field_i_validity: unverified`, and the mint (adjudicated E1) projects that plus
`lake.status: under_review`.

**Reconciliation with the specs — amend LINT-6 (not the mint):** S5 R15 renders the ⚪ banner for a
case page whose `lake.status ∈ {draft, under_review}` **or** whose Field-I is `unverified`. The
minted pages carry BOTH → the R15 banner renders → the reader IS bannered → S1 R2 ("⚪ never reaches a
reader unbannered") is satisfied. LINT-6 (d) was testing the literal `draft: true` key, which (i) is
NOT R15's banner driver, and (ii) `draft: true` would EXCLUDE the page from the Quartz build (hide
it) — not the design. The lint's real invariant is "an unverified page carries the R15 banner-driving
state." **Mint is spec-conformant; the gap is in LINT-6.**

**Change:** added `_banner_driven(fm)` (True iff `draft: true` OR `lake.status ∈ {draft,
under_review}`) and replaced the two `not draft` conditions in check (d) (the unverified-unbannered
HIGH and the ⚪-in-table MEDIUM) with `not _banner_driven(fm)`. The legacy `draft: true` signal is
preserved (still accepted); the verified-page checks are unchanged (a verified page with no
banner-driver still fires). Added a `--self-test` (LINT-6 had none) + three fixtures:
`lint-6-minted-underreview-pass.md` (minted shape → 0 HIGH), `lint-6-draft-flag-pass.md`
(legacy `draft: true` → 0 HIGH), `lint-6-unverified-unbannered-fail.md` (unverified + `lake.status:
verified` + no draft → 1 HIGH).

**Before/after (full corpus):** LINT-6 **15 → 0** HIGH; all 15 cleared are the check-(d)
unverified-unbannered on the minted pages, **0 newly introduced, 0 other deltas** (the 15 were the
only LINT-6 violations in the corpus). Files touched: `scripts/lint/lint6_treatment_status.py` + the
three fixtures + this addendum (no mint change, no lake/content writes, no `scripts/s2/`).

---

## 12. Addendum — slip-only support (S2 A3 slip precedent, 2026-07-07)

The mint must support **slip-only** rows — real cases (mostly OT2025) whose reporter cite does not
exist yet — instead of hard-refusing `record-missing-citation` (which conflated "no cite exists yet"
with "cite missing/unverified"). Adjudicated per R8-CITE-RECOVERY-WORKORDER §R3.3 follow-up.

**Trigger = explicit marker, never inference.** The mint keys off `citations.slip_only: true` on the
lake record — never off an absent citation. `record-missing-citation` is UNCHANGED for unmarked rows
(self-tested: `unmarked no-cite row still refuses`).

**Stamp surface (delivered, self-tested; NOT run on real records this session).**
`scripts/s6/stamp_slip_only.py` — bounded, journaled, dry-run default, `--write` guarded, `--as-of`
required. It stamps `citations.slip_only: true` + a `citations.slip_only_provenance` trail
(`{source, note, as_of, by, legs[]}`) onto EXACTLY the slip-only allowlist —
`_run/o2-execute/R8-R3-web-cites.jsonl` rows with `slip_only: true` (**15**: Mendoza, Carter,
Robinson, Larson, Davis, Holcomb, Hunt, Ruiz, Lee, Zorn, District of Columbia v. R.W., Landor,
Olivier, Konan, GEO Group). It **refuses** any record_id not in the allowlist, any record already
carrying a real citation, and is idempotent (already-stamped → no-op). Self-test 7/7 (incl. a
stamped record validating clean against the live LINT-13 schema). **Placement note:** the coordinator
said `scripts/s2` is free, but `git status` shows `M scripts/s2/project.py` (the repair lane's
uncommitted CR-13/14 work), so per the coordinator's own "confirm no other lane's uncommitted
scripts/s2 work" gate I kept the standalone in `scripts/s6/` (its own lane, alongside `mint_page.py`)
rather than adding to `scripts/s2/ingest.py`; the orchestrator may relocate it later.

**Mint slip cite (PROPOSED — flagged for ratification).** S2 A3 sanctions slip *pinpoints*, not a
slip citation display; S5 R3's header line sanctions no slip form. I implemented the Bluebook slip
form behind the marker: `derive_slip_cite` → **`No. <docket>, slip op. (<court> <year>)`** (e.g.
`No. 23-1197, slip op. (U.S. 2026)` for Landor), injected into the born page's `citation`
frontmatter, the Case-cell, and the authored-ledger `cite` + `home_rows[].cite`. If a marked
record's identity lacks a docket AND a court/year, the mint refuses with a distinct
`record-slip-identity-incomplete` (never a degenerate `slip op. ()`).

**Readiness (surfaced, not blocking):** after stamping, **6 of 15 mint now** (docket+court+year
present: Robinson, D.C. v. R.W., Landor, Olivier, Konan, GEO Group); **9 need identity completion
first** (docket/court/year absent on the record — the JSONL notes have them, the identity block does
not: Mendoza, Carter, Larson, Davis, Holcomb, Hunt, Ruiz, Lee, Zorn) — an S2 identity task, distinct
from the slip marker.

**LINT-13/16.** Schema extended additively: `citations.slip_only` (boolean) + `slip_only_provenance`
(object) added to `definitions.citations.properties`, NOT to `required`, `web_legs`/`if-then`
untouched — full-lake LINT-13 stays **0**; a stamped record validates clean. Fixtures:
`lint-13-record-slip-only-pass.json` (0 viol) + `lint-13-record-slip-only-malformed-fail.json`
(missing-`by` → 1 viol). LINT-16: a slip born page has no case tables (only the R5 carve-out), and
the slip cite carries no ISO-date/weight token, so LINT-16 passes (mint self-test stages LINT-15/16/14
on the born page → clean). Mint self-test **41/41**, specimen PASS.

**EXACT ready-to-run stamp command (at the next orchestrator gate, after W2 pauses):**
```
python3 scripts/s6/stamp_slip_only.py --allowlist _run/o2-execute/R8-R3-web-cites.jsonl --as-of 2026-07-07 --write
```
(Dry-run — same without `--write` — was run this session: 15 targets, 0 written, 0 refused.)
Files touched: `_overhaul2/lake/_schema.json`, `scripts/s6/{mint_page.py, stamp_slip_only.py}`, and
fixtures (`scripts/s6/fixtures/{stub-fixture-slip.json, payload-slip.md}`,
`scripts/lint/fixtures/lint-13-record-slip-only-{pass,malformed-fail}.json`) + this addendum. No real
lake-record writes, no `content/`, no `scripts/s2/`.

---

## 13. Addendum — slip-cite drift fix, project.py is the single source (2026-07-07, W3 escalation)

LINT-12 slip-cite drift on **Carter v. United States**: the mint's slip path wrote the derived slip
cite into the born page's `citation` frontmatter, but `project_record` returned `''` (the record's
citations block is empty by design for slip rows), so the drift lint fired page-vs-projection.

**Fix (single source, chosen direction):** `derive_slip_cite` / `slip_court_abbr` /
`record_is_slip_only` MOVED into `scripts/s2/project.py` (verified `scripts/s2` free first);
`citation_with_year` now derives the slip form when a record carries `citations.slip_only: true` and
has no reporter cite, so the projector and the S6 mint agree. The slip form is NEVER written into
`citations.display` — the marker is the truth, both consumers derive. `scripts/s6/mint_page.py` now
imports these from `s2project` (no circular import: project.py imports nothing from s6) and DROPPED
its slip-cite injection — the projection carries the slip cite through `assemble_frontmatter`
naturally. Projector self-test gains a slip assertion (marked record → slip cite; unmarked citeless →
`''`); the stamp self-test was made robust to a live record that the real gate run has already
stamped.

**Carter before/after:** LINT-12 on Carter **1 → 0**. The projector re-projection of Carter is a
confirmed **no-op** (dry-run: `refused=False, pages_changed=0`) — the page already carried the correct
slip cite from the mint, so no `content/` write was needed (zero page diffs). Full-corpus LINT-12 **0**,
LINT-13 **0**.

**Tests:** projector `--self-test` PASS (+ slip assertion) · `--verify-idempotent` PASS · mint
`--self-test` **41/41** · specimen PASS · stamp `--self-test` **7/7** · LINT-13 self-test PASS. Files
touched: `scripts/s2/project.py`, `scripts/s6/{mint_page.py, stamp_slip_only.py}` + this addendum —
no `content/` write, no other lake writes, nothing committed.
