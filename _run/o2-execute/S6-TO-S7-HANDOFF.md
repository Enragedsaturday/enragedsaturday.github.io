# S6 → S7 Handoff — the doctrine-production session reads this FIRST

> **O2 EXECUTE · branch `overhaul2/execute` · HEAD `2f77004` (W10 close) · 2026-07-07.**
> S6 (R8 case-page authoring + R11 coverage ledger + R12/LINT-17) is COMPLETE. This file is the
> input the S7 (doctrine-production) orchestration session consumes before it opens wave 3.
> Modelled on the O1 `_overhaul/ledger/S6-to-S9-handoff.md`; content is O2's.
>
> **Nothing here is a defect in S6 output.** These are the delivered artifacts, the obligations
> S6 deliberately *deferred to S7* (the R8 E2/E3 transitional amendment), the standing decisions
> that bind S7, the items S6 accumulated *for S9* (surfaced so S7 does not trip on them), and the
> data-lake state. Every claim traces to an artifact; uncertainties are flagged in §6.
>
> S7's own spec is `_overhaul2/specs/S7-doctrine-production.spec.md` (APPROVED 2026-07-03). Its
> gates name S6 as "R8 authoring pipeline + R11 coverage ledger" — this is that handoff.
> **Zero CL from S7 authoring lanes** (S7 spec R6; the REST token is the S2 builder's; the Claude
> MCP lane is interactive spot-checks only). **COMMIT NOTHING** here — the orchestrator commits.

---

## 0. The scoreboard S7 inherits

| Fact | Value | Pointer |
|---|---|---|
| Authored case pages (born `under_review`) | **148** | `content/cases/*.md`; `s6-authored-ledger.jsonl` (148 rows) |
| R11 coverage-ledger partition | **243 distinct captions** | `_run/s6-coverage-ledger.json` |
| Case Index rows | **617** | `content/legal-system-research-and-reference/Case Index.md` |
| Live lake manifest records | **665** | `_overhaul2/lake/_manifest.json` |
| Build | green, 719 input / 2710 emitted | JOURNAL W10 close |
| Mint-gate lints on every born page | LINT-14/15/16 = **0/0/0** corpus-wide | R8-WAVE-W10-REPORT |
| CL calls run-wide | ~17,500 (≈76% of the ~23k envelope), **0×429 across the entire run** | JOURNAL disposition/close |

R11 partition (machine-checked PASS, 0 conflicts, 0 errors):
`authored 148 + brief-mention 55 + excluded-remit 26 + folded-alias 8 + watch 3 + removed 2 + unverifiable 1 = 243`.

---

## 1. What S6 delivered

### 1.1 The 148 authored case pages
- Location `content/cases/<stem>.md`, stem = caption (A6/R9 disambiguation: collision with a
  *distinct* existing page → `caption (year)` → `caption (court year)`; standing exhibit
  `United States v. Smith (2024)`).
- **Born `lake.status: under_review`** — E1 RATIFIED (`R8-PIPELINE-ADJUDICATION.md` §E1). This is
  the schema-real status; the lake vocabulary has **no `draft` terminal**. R8's word "draft" means
  the S5 R15 *draft-banner family*: R15 renders the identical ⚪ banner when
  `lake.status ∈ {draft, under_review}` **OR** Field-I is `unverified`. **Do not expect literal
  `draft: true`** — that key would *hide* the page from the Quartz build (this is why LINT-6 was
  amended, not the mint; `R8-PIPELINE-BUILD-REPORT.md` §11).
- Every page carries the S2-projected data frontmatter (weight/treatment/dates/cite — R7-owned,
  the author cannot drift it), worklist-derived `homes`/`aliases`, exact BIRAC skeleton, verbatim
  pinned holding, R12 `## Sources` with corroboration trails.
- The authored-ledger row per page: `_run/o2-execute/s6-authored-ledger.jsonl` — carries `terminal`,
  `record_id_before/after`, `caption`, `cite`, `year`, `court`, `authority_weight`, `opinion_url`,
  `holding`, `leg`, `prong`, `basis`, `homes`, `roles`, `primary_home`, **`home_rows[]`** (see §2.1),
  `worklist_note`, `page`, `born_status`, `lints_run`, `lane/model`.

### 1.2 The R11 coverage ledger (243-caption partition)
- `_run/s6-coverage-ledger.json` — one row per distinct caption in the S6 candidate universe, each
  exactly one terminal. Assembled programmatically by `_overhaul2/scripts/build_coverage_ledger.py`
  (`--write`) from the signed disposition artifacts + the lake manifest — reproducible, not hand-edited.
- Machine checks green: authored page-file + lake-record + manifest-rename present **148/148**;
  folded-alias rows name an existing survivor **8/8**; **0 conflicts, 0 row-errors**.
- Row schema: `{caption, canonical, cluster_id|null, leg, gate:{verdict,prong,rationale},
  keys:{cl,independent}, terminal, pointer}` (+ `page_backed`, `source`, `survivor` on folds).
- **NUM-04 (388 bare-mention) handled honestly, NOT fabricated:** the 388 is a *measured S8 input*
  with **no machine artifact** in the repo; the ledger is built as the join surface (every row
  carries `page_backed` + `pointer`) rather than re-deriving a number that has no artifact. S8 owns
  the final 388 join. A frozen `corpus_mention_baseline` (§5.4) gives S8 the machine list — **labelled
  as LINT-17's own current-corpus scan, NOT the NUM-04 388.**

### 1.3 LINT-17 (R12) — the coverage lint
- `scripts/lint/lint17_coverage.py`, fail-closed HIGH, wired into `scripts/lint/run_all.py`
  (LINTS + SELF_TESTS). A prose party-v-party caption resolving to **no page** fails the build
  **unless** the coverage ledger records a non-page terminal for it.
- The allowlist is a **frozen snapshot** committed by the assembler — a NEW bare caption grown
  after S6 close is not self-allowlisted and fails CI until it earns a page or a ledger disposition
  (the R12 class-2 defense). **This is the R16 mechanism S7 lives under:** every case S7 newly names
  in prose must have an S6 ledger terminal before the branch merges — route discoveries through the
  mint (§1.4), which appends the ledger row and regenerates coverage.
- Self-test 9/9 PASS; corpus-wide run **0 violations / 734 captions scanned**.

### 1.4 The R8 pipeline entry point — `scripts/s6/mint_page.py` (S7 invokes THIS, no second mint)
S7's rewrite-time case discoveries go through the **same** pipeline; there is **no second
page-mint** (S7 spec §2.1 + R6; the S6 boundary). Contract:

- **CLI:** `python3 scripts/s6/mint_page.py --row <record_id> --payload <body.md> --as-of <ISO> --write`
  (dry-run is the default; `--validate-only`, `--self-test`, `--specimen-test` also). Exit 0 = clean
  dry-run / committed / `already-authored` no-op; 2 = refusal; 1 = self/specimen failure.
- **Payload contract:** the payload is a full markdown file. The CLI takes the **body** below the
  frontmatter and reads the author's frontmatter for content-owned preserved fields —
  `related`, `tags`, `holding`, optional `aliases`, and an **optional** `placements[]` block. The CLI
  **owns the data frontmatter** (S2 projection — author cannot drift weight/treatment/dates/cite) and
  **generates** `title`/`type`/`homes`/`aliases` from the worklist. `placements[]`, when present,
  supplies the per-home row cells that get folded into the ledger `home_rows[]` hints. **Refuses if
  payload H1 ≠ computed stem.** (`R8-PIPELINE-BUILD-REPORT.md` §4.)
- **Status-acceptance set:** mints iff the lake record is `stub: true` AND
  `status ∈ {verified_identity, verified, verified_off_cl}`. Everything else
  (`not_found`, `fabrication_suspected`, `folded-alias`, bare `under_review`) is refused.
- **All-or-nothing atomic commit** (index/homes writes REMOVED — see §3.2): (1) write
  `content/cases/<stem>.md`; (2) lake rename; (3) manifest rename+flip; (4) ledger append **last**.
  In-memory backups + reverse-order rollback; a crash-tail rolls forward and reports `RECONCILED`;
  anything else half-committed refuses `wedged-partial-state`.
- **16 machine-readable refusal codes** (loop-3): `worklist-absent`, `no-lake-record`,
  `wrong-status`, `not-a-stub`, `record-missing-citation`, `history-class-mismatch`,
  `stem-contains-double-dash`, `stem-collision-distinct-case`, `record-id-collision`,
  `homes-roles-desync`, `manifest-missing-record`, `wedged-partial-state`, `payload-invalid`,
  `staged-lint-failed`, `home-page-missing`, `as-of-required`.
- **Determinism:** `--as-of <ISO>` required for `--write`; no wall-clock read feeds any journaled
  value (the only datetime import was removed, F-R8-10).
- **Staged-lint gate:** the born page must be absolutely clean — LINT-15 (case) + LINT-16 at **any**
  severity + LINT-14 binding = 0, staged in a temp mirror before the real tree is touched.
- **Tests:** self-test **36/36 PASS**, specimen PASS (`United States v. Smith (2024)`:
  `project_record` deep-equals the page's managed frontmatter modulo `lake.status`).

### 1.5 The stamper — `scripts/s6/stamp_slip_only.py`
Stamps `citations.slip_only: true` + a `slip_only_provenance` trail onto EXACTLY the slip-only
allowlist (`_run/o2-execute/R8-R3-web-cites.jsonl` rows with `slip_only:true`); refuses any record
not on the allowlist or already carrying a real citation; idempotent. Self-test 7/7. It was
**executed at gate (15/15 stamped, 0 refused)**; the slip-header standard is ratified (§5.2).

### 1.6 The cluster-collision guard
The mint originally collision-checked by **stem only** — which nearly double-paged
`davis--4881258` (a duplicate of the already-authored *Howard Davis* page, same cluster
4881258 / 997 F.3d 191, caught in the W5 outage). The **cluster-collision mint guard** was added
(W6 micro-repair, 43/43; a real dry-run of the davis stub is now REFUSED `[cluster-collision]`).
**S7's discoveries inherit this guard** — a discovery whose cluster already backs a page is refused,
not minted twice.

---

## 2. Ledger-deferred obligations S7 MUST materialize

### 2.1 Home-page Key/Related rows — the R8 E2/E3 transitional amendment
**The mint does NOT write homes-page rows.** Adjudicated `R8-PIPELINE-ADJUDICATION.md` §E2/E3(b):
a corpus-wide convert-first at S6 would overturn S5 §5.2 ("S7 runs `convert_tables.py` **per-page**
during doctrine production — prose judgment stays human"). So:

- The mint's homes-page insertion surface + refusal `home-not-r6-converted` were **removed**; the
  `homes[]` **existence** check (`home-page-missing`) is **KEPT**.
- **S7 materializes the Key/Related rows from `s6-authored-ledger.jsonl` `home_rows[]` when it
  converts each home page with `convert_tables.py`** (S7 receives the ledger as input per R11 anyway).
- **Owed count: 158 `home_rows[]` across the 148 authored records (148 `key` + 10 `related`), 158
  homes total.** Each `home_rows[]` entry is **denormalized** so S7 needs no row-level join:
  `{home, role, role_class, schema, stem, cite}` + for Key `holding_cell_hint` (payload placement,
  else `holding` first sentence) + for Related `relevance_tag_hint` + `relevance_cell_hint` +
  `primary_home`. `stem` = `record_id_after` (the Case-cell wikilink target, F-R8-09).
- **R11-close expects zero dropped rows** — the coverage ledger's close-check gains an owed-homes
  accounting. As S7 converts each home page it discharges that page's owed rows; a silent drop is a
  reconciliation failure.
- **Per-page, never corpus-wide** (S5 §5.2). The Case Index has a *different* single writer (§3.2).

### 2.2 The 58 non-page placements — `R8-NONPAGE-LEDGER.json`
Prose bullets / mentions / split-blocks to **place during doctrine production** (NOT pages; each has
a terminal non-page state + `target_node`). Total **58** = **12** noted-orders/watch/fold + **44**
mentions/bullets + **2** split-blocks. Plus **3** escalation resolutions (2026-07-07):
- *Commonwealth v. Serge* → excluded-remit (citation-format specimen on the S8 page).
- *District of Columbia v. Heller* → excluded-remit (2A; corpus already annotates "not Fourth
  Amendment authority").
- **United States v. Cruz → `watch_s7_deferred`** (bare-caption trap: R1 identity passed, cluster
  10662743, but the capture's good-faith/bad-faith proposition linkage is deferred — **S7 owns this
  disposition**).

The two **split-blocks** are S7 prose:
- *Officer-created-danger / pre-seizure-reckless-conduct split* → `use-of-force-and-liability/Use of
  Force.md` (post-*Barnes v. Felix* open question; SCOTUS anchor *County of Los Angeles v. Mendez*
  is a page).
- *Inevitable-discovery active-pursuit split-block* →
  `the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md`.

> **Do not conflate the two "58"s.** This §2.2 is the **R8 non-page ledger** (58 S7 *prose* placements).
> The `corpus_mention_baseline` in §5.4 was 58 pre-W10 and is now **56** — that is an S8/LINT-17
> allowlist tail, not S7 work.

---

## 3. Standing amendments / decisions that bind S7

### 3.1 `convert_tables.py` per-page, never corpus-wide
S5 §5.2 (user decision — prose judgment stays human). Confirmed at E2/E3. S7 runs the converter on
each doctrine/home page as it rewrites it; the S6 mint deliberately did not force a corpus-wide
convert.

### 3.2 Case-Index schema-3 flip — owed at S7/S8, generator-owned
The mint's index-insertion surface was **removed**; the **single writer is
`scripts/build_case_index.py`**, regenerated per wave batch (idempotent, diff-clean). The live index
is still the **legacy 5-col** schema (`| Case | Holding | Good law | Home page(s) | CourtListener |`).
**The R6 schema-3 flip is owed to the S3-owned generator at S7/S8-time** — not S6's to force
(`R8-PIPELINE-ADJUDICATION.md` §Deferred). S7 regenerates the index after each rewrite batch that
touches Case rows.

### 3.3 CL MCP `plain_text` blind spot + the REST fallback method
The Claude MCP `read_document` uses `html_with_citations` and is **BLIND to `plain_text`**. Two S6
cases (Gutierrez, then again at W9) had no `html_with_citations` text; they were authored via the
**`plain_text` REST method** (Gutierrez: 117KB plain_text). The wave order was amended with this
fallback + a **stop-if-unauthorized rule** (the REST token is the S2 lane's — if S7 hits a
plain_text-only opinion, the read routes through the S2/REST lane, never a hand-fabricated holding).
(JOURNAL W2 consolidated-repair; W9 close.)

### 3.4 Serial-CL L4 discipline + outage protocol
One serial CL lane; ~15–25 rows/batch. **Outage protocol (proven at W5):** when the MCP lane dies
mid-batch, the agent **yields with a definitive handoff** (0 pages authored without pincites,
wave-plan left honestly pending, cached opinion→cluster map preserved); the orchestrator probes the
lane healthy and **RESUMES THE SAME AGENT** — no relaunch, no duplicate lane. Two CL outages were
survived this way across the run.

### 3.5 CodeRabbit spec-gate — S7 ships no code, so no gate
The standing RUNBOOK §5 amendment: the CodeRabbit gate fires at spec completion **over code paths
only, never over lake/content**. **S7 produces prose, not code** — so **no CodeRabbit gate applies
to S7's doctrine output.** (If S7 touches a script, that delta rides the standing code gate; the
prose corpus does not.)

### 3.6 Body-only-finalization — ratified class
Authors may fix **their own fresh pages'** incidental lint (LINT-9 pin placement, LINT-2 incidental
quotes, dead wikilinks) at author-time; **S9 certifies**. Ratified across W1–W8 (writer≠checker holds
— the fix is on the writer's own new page, the certification is S9's). S7 inherits this: an S7 author
may clean its own page's mechanical lint, never another page's.

### 3.7 S5 R5 point-status tables — S7 authors them
S7 authors the point-status table + reconciling prose for every `varies_by_point` case the S2
projector surfaces (the **11 `limited` + 7 `overruled/abrogated`** migrations, S5 Method 3),
consistent with the lake record. The **Santana** worked example (doorway ✓ · felony-pursuit ✓ with
*Lange*'s express reservation · broad reading limited by *Lange* 594 U.S. 303–04, 313) is the
committed exemplar (S7 spec R13, §11 research annex).

### 3.8 Officer-BLUF / field-application layer — banned project-wide
S1 §2.2 + R6. TEACH-04e migrates survivors to numbered `**Apply it.**` lists (genuine decision
sequences) or deletes them (BLUF-voice restatements). The layer stays dead.

---

## 4. S9-owed items accumulated during S6 (so S7 does not trip on them)

These are **S9's** to adjudicate; S7 should recognize them as known-state, not re-open or "fix":

- **History-pages Field-I `unverified → superseded` promotion** — the 5 W3 history-D2 renders
  (Sanders, Frank, Quantity, Robbins, Trupiano) + Rochin (W8) already **render Historical + the
  precise overruling verb + wikilinked successor + ⚪ banner**; the *treatment-status promotion* is
  S9 remit (JOURNAL W3).
- **trent** — unpublished-6th-Cir. reverify flag + hand-reconstructed docket-collision (pre-W5
  audit); S9-reverify.
- **capers / castillo** — lake `identity.docket` mismatches (capers 09-2101 vs CL 07-1830-cr;
  castillo 22-50060 vs CL 21-50406); **the page body uses the CL-correct value** — lake-field repair
  for the repair lane, not a page defect.
- **capers / chavez** — best-effort star pincites to confirm.
- **Williams** — star-pagination / star-sparsity confirm.
- **Ruckman** — stale docket `85-2801 → 85-2731`; minted with an adjudicated ¶-pin (¶ 9) carrying one
  disclosed LINT-2 medium (PINCITE_RE ¶-support was extended at W7; the O1-deferred FP class).
- **Youngblood** — lake year quirk (1989 vs decided 1988-11-29), flagged S2.
- **zorn** — corrupt Strike-3 cluster; terminal `unverifiable-pending`; the off-CL identity decision
  is owed (lake untouched, worklist in-row; belt-and-braces stamped-but-refuses-mint held).
- **holcomb** — WATCH: cites a **WITHDRAWN** opinion (132 F.4th 1118; the ca9 panel withdrew its own
  opinion, reh'g moot, **no successor as of 2026-07**); page-less watch terminal, pointer ca9 23-469 /
  cluster 10365516.
- **Endemic corpus lint classes (named owners):** **LINT-10** em-dash ×48 pages (S7's own R11
  rewrite pass owns this — budget ≤1 em-dash/block); **LINT-5** link-every-case ×46 (S8);
  **LINT-7** register drift (S3 renames + S7 prose). These are steady-state, not regressions.

---

## 5. Data-lake state

### 5.1 Manifest arithmetic
- **R11 reconciliation base (per the coverage-ledger note + closeout §1): 662 records** (604
  page-backed + 58 page-less stubs).
- **Live manifest now: 665 records** (`_overhaul2/lake/_manifest.json`; +3 = the W10 mini-wave
  additions Anderson v. Creighton / Bell v. Wolfish / Colonnade, added via `--add-candidates` then
  minted). **148 renames** recorded. Current status distribution:

  | status | count |
  |---|---|
  | verified | 421 |
  | under_review | 183 (35 pre-existing S9-owed + 148 minted pages) |
  | verified_identity | 49 (remaining frontier shells, not paged) |
  | not_found | 4 |
  | folded-alias | 4 |
  | verified_off_cl | 2 (Entick, Wilkes — A17 English-corpus elevation) |
  | fabrication_suspected | 2 (the removed West/White pair; ledger-terminal `removed`) |

  `stub: true` on 59 records; `stub: false` on 606.

### 5.2 Slip-only marker + Bluebook slip-header standard (ratified)
- **Trigger = explicit marker, never inference:** `citations.slip_only: true` on the lake record.
  `record-missing-citation` is UNCHANGED for unmarked rows.
- **The slip form is derived by `scripts/s2/project.py` (`derive_slip_cite`), the single source:**
  `No. <docket>, slip op. (<court> <year>)` (e.g. `No. 23-1197, slip op. (U.S. 2026)`). It is
  **NEVER written into `citations.display`** — the marker is the truth; the projector and the mint
  both derive it (the W3 Carter LINT-12 drift fix). **S9 will sample** slip pins.
- A slip-marked record lacking docket AND court/year refuses `record-slip-identity-incomplete`
  (never a degenerate `slip op. ()`).

### 5.3 Web-dual-leg citation provenance class
The R3 cite-recovery lane recovered citations CL lacked via a **dual-leg web method** (distinct
provenance source, mutually-blind legs), landed as a schema/LINT-13 extension (`web_legs`,
additive, `additionalProperties:false`). These rows carry their non-CL provenance explicitly
(`R8-R3-web-cites.jsonl`, `R8-CITE-RECOVERY-REPORT.md`). S7 treats them as any other cited row; the
provenance trail makes them auditable.

### 5.4 corpus_mention_baseline — the honest LINT-17 residual (S8, not S7)
`_run/s6-coverage-ledger.json` `corpus_mention_baseline`: **56** page-less bare-mention captions
(51 `brief-mention` legacy antecedents + 5 `excluded-remit` citation-format placeholders). This is
**LINT-17's own current-corpus scan**, explicitly **NOT the NUM-04 388** (§1.2). It is an S8
plain-link concern. (The S6-CLOSEOUT-REPORT §3/§4 narrative says **58/53** — that is the *pre-W10*
snapshot; the ledger was regenerated after W10 [3 escalations became pages, Anderson surfaced
*Mitchell v. Forsyth* as +1 brief-mention → 58−3+1 = 56]. The **machine ledger (56) is
authoritative**; see §6.)

### 5.5 Identity-repair surfaces added during the run (available to S7's mint lane)
`scripts/s2/ingest.py` gained (all writer≠checker, all live-validated): `--enrich-citations`
(bounded cluster-citation fetch), `--repair-identity-from-cache` (SCOTUS false-Historical +
military-namesake classes), `--repair-coa-state-from-cache` (docket-court_id-authoritative
circuit/state derivation, D.C. trap resolved, fail-closed on swaps/military/uncorroborated),
`--readjudicate` / `--readjudicate-file` (**unscoped file form is UNSAFE post-mint** — would
re-fetch minted pages; use the scoped `--smoke` per row), `--web-keys-allow-verified-identity`
(narrow opt-in), `--elevate-off-cl`. `scripts/s6/` gained `mint_page.py`, `stamp_slip_only.py`, and
the cluster-collision guard.

---

## 6. Gaps / uncertainties found while assembling this handoff

1. **Record-base drift 662 vs 665 (minor, benign).** The R11 coverage-ledger `note` and
   `S6-CLOSEOUT-REPORT.md` §1 cite the **662**-record reconciliation base; the **live manifest is
   665** (W10 added 3 via `--add-candidates`). The 243-partition and authored-148 counts are correct
   and machine-checked; only the prose "662" figure was not re-stamped to 665 after W10. Not a
   partition error — the 3 W10 pages are inside `authored 148`.
2. **corpus_mention_baseline 56 (ledger) vs 58/53 (closeout narrative).** The `S6-CLOSEOUT-REPORT.md`
   §3/§4 predates the W10 ledger regen (see §5.4 for the 58−3+1=56 reconciliation). The **machine
   ledger value 56 is authoritative**; the closeout prose is a stale snapshot. This is an S8 concern,
   surfaced here so S7/S8 don't chase the drift.
3. **"58" collision (documented, not a defect).** Two different 58s exist — the R8 non-page-ledger
   total (58 S7 prose placements, §2.2) and the pre-W10 baseline (now 56, §5.4). This handoff keeps
   them separate; downstream readers should too.
4. **Owed home_rows = 158, not 148.** The count S7 must discharge is the **`home_rows[]` total (158
   = 148 key + 10 related)**, not the page count (148). Ten pages carry a second (Related) home row.
   Verified directly against `s6-authored-ledger.jsonl`.
5. **NUM-04 388 has no machine artifact** (confirmed by S6, re-confirmed here) — S8 owns the join;
   S7 needs only the ledger's `page_backed`/`pointer` join surface. Not an S7 obligation.

---

## 7. File pointer index

| Artifact | Path |
|---|---|
| This handoff | `_run/o2-execute/S6-TO-S7-HANDOFF.md` |
| S7 spec (read its §2/R6/R10/R13/R16) | `_overhaul2/specs/S7-doctrine-production.spec.md` |
| Run journal (W1–W10 + close) | `_run/o2-execute/JOURNAL.md` |
| Authored ledger (148 rows + `home_rows[]`) | `_run/o2-execute/s6-authored-ledger.jsonl` |
| R11 coverage ledger (243 captions) | `_run/s6-coverage-ledger.json` |
| Coverage-ledger assembler | `_overhaul2/scripts/build_coverage_ledger.py` |
| Non-page placements (58 + 3 escalations) | `_run/o2-execute/R8-NONPAGE-LEDGER.json` |
| R8 pipeline adjudication (E1–E4) | `_run/o2-execute/R8-PIPELINE-ADJUDICATION.md` |
| R8 pipeline build report (contract) | `_run/o2-execute/R8-PIPELINE-BUILD-REPORT.md` |
| S6 close-out report | `_run/o2-execute/S6-CLOSEOUT-REPORT.md` |
| Mint CLI (S7 invokes this) | `scripts/s6/mint_page.py` |
| Slip-only stamper | `scripts/s6/stamp_slip_only.py` |
| Case-Index generator (single writer) | `scripts/build_case_index.py` |
| LINT-17 coverage lint | `scripts/lint/lint17_coverage.py` |
| Live lake manifest | `_overhaul2/lake/_manifest.json` |
| Slip / web-cite recovery source | `_run/o2-execute/R8-R3-web-cites.jsonl`, `R8-CITE-RECOVERY-REPORT.md` |
| Wave reports (per-batch detail) | `_run/o2-execute/R8-WAVE-W1..W10-REPORT.md`, `PRE-W5-AUDIT-REPORT.md` |
| Case Index (live, legacy 5-col) | `content/legal-system-research-and-reference/Case Index.md` |
| O1 precedent handoff (model) | `_overhaul/ledger/S6-to-S9-handoff.md` |
