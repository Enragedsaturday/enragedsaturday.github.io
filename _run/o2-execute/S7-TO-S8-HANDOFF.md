# S7 → S8 Handoff — the linking/transclusion session reads this FIRST

> **O2 EXECUTE · branch `overhaul2/execute` · HEAD `66d8f79` (S7 close) · 2026-07-09.**
> S7 (doctrine production — R1 rendering, R5 conversions, R7/R8/R11 passes, D5/D7 nodes, the point-status
> tables) is COMPLETE across all 13 categories + the consolidated repair lane. This file is what the S8
> (linking / transclusion / Case-Index-schema) session consumes. Modelled on `S6-TO-S7-HANDOFF.md`.
>
> **Nothing here is a defect in S7 output** except the two blockers called out in §0/§6 (the incomplete
> Riley re-key propagation). These are the delivered artifacts, the obligations S7 deferred to S8, the
> standing decisions that bind S8, the items S7 accumulated for S9, and the lake state. Every claim traces
> to an artifact. **Zero CL from S8 authoring lanes** (the REST token is the S2 builder's). **COMMIT
> NOTHING** — the orchestrator reviews and commits.
>
> S8's inputs also live in `S7-ACCEPTANCE-SWEEP.md` (spec §7, machine-evidenced) and
> `S7-OWED-ROWS-ACCOUNTING.md` (the zero-drop proof). Read those two first for the gate detail.

---

## 0. The scoreboard S8 inherits

| Fact | Value | Pointer |
|---|---|---|
| Doctrine units born draft (all 13 cats) | **89** | survey `89 substantive pages`; batches 1–20 |
| S7-minted case pages (D7 SACO wave) | **3** (Nora / Al-Azzawy / Vaneaton) | `content/cases/`; born `under_review`; ledger 148→151 |
| Authored ledger rows / home_rows | **151 / 164** | `s6-authored-ledger.jsonl` (151 key + 13 related) |
| `run_all` lint arc | **8372 → 6829** total | Phase-0 baseline → S7 close |
| `run_all` HIGH arc | **5212 → 3782** | ⚠ journal said 3781; **+1 = B1 Riley LINT-13** (see §6) |
| Build | **724 input / 2873 emitted**, green | `npx quartz build`, exit 0 |
| Coverage ledger | **252 captions, PASS**, 0 conflicts | 151 authored + 61 brief-mention + 26 excluded + 8 folded + 2 removed + 1 unverifiable + 3 watch |
| Registry new placed nodes | **+4** (D5, D7, Bivens, Absolute) + statements filled | `registry.yaml` :291/:300/:775/:784; LINT-20 = 0 |
| Manifest | **668 records** (+3 SACO mints) | `_overhaul2/lake/_manifest.json` |

The 4 new nodes: `seizure.person.constructive-entry` (D7), `seizure.person.noninvestigative-caretaking`
(D5), `liability.federal-officer-suits` (Bivens/FTCA), `liability.absolute-immunity` — each with a filled
`statement`, `home_page`, and `status: draft`.

---

## 1. What S7 delivered

### 1.1 The template corpus (89 doctrine units, all 13 categories)
Born-again rewrites + splits + new authored pages at their signed change-list tiers, per the D1 pattern
(Brief move-order · Apply-it + pitfalls close · LCD · optional split-synthesis). Every page carries
`status: draft` (or the overview/hub/reference/craft exempt-class shaping) → renders the ⚪ banner; the R3
universe **awaits S9**. Splits/dissolutions map in `S7-OWED-ROWS-ACCOUNTING.md` §A.3.

### 1.2 The corpus passes — completed (survey-verified dead)
`python3 scripts/s7/survey.py`:
- **field-framing = 0** (died corpus-wide at batch-20)
- **rule-skeletons = 0** (last at batch-19)
- **inverted authority-labels = 0** (last at batch-19)
- **RD-family headings = 0** (TEACH-08 → "Lower-court developments"), **missing-H1 = 0** (TEACH-12a)
- **A2-class leaks (class1_no_standalone + class2_cl_confirm) = 0**. NOTE: **6 `class3_meta_intro`
  survivors** remain — the "(no SCOTUS; SCOTUS homes to Key cases)" LCD-framing on the 6 cat-6c
  home-entry pages. Orchestrator/S9 to rule whether that framing counts as a TEACH-02c leak or legitimate
  placement pedagogy (see acceptance-sweep AC-4).
- em-dash density **4.9/1k** on the doctrine corpus (the R11 "~48-page" rewrite obligation discharged);
  the LINT-10 3346 HIGH is **3217 S6 case-page backlog + 103 site index + 17 generated Case Index + 9 on 2
  out-of-scope/legacy pages** — not the doctrine rewrite (acceptance-sweep AC-6).

### 1.3 The R5 conversion trail (with provenance)
Every slip→tier conversion is logged **per batch in the JOURNAL** with tier + evidence (there is no
separate trail file — the journal IS the trail, for S9's tier-sampled re-verification). Anchors: Carpenter
T3 (585 U.S. 296) · Collins T3 (584 U.S. 586) · Chatrie T4 (current-Term) · **King slip→T1 BOUND 462**
(op 9441559) · Byrd T3 · Cotterman/Cano T3 · Perry T3 (L.Ed.2d-only) · Torres slip-refuted (T3, quotes
removed). Doctrine slip survivors are all current-Term T4 (Chatrie, Case v. Montana) or the single §9
F.4th class (Tuggle) + current-year unpublished (Trent) — see AC-3.

### 1.4 The point-status tables (R13)
Authored where the S2 projector surfaced `varies_by_point`: the **Belton→Gant** superseding table on SIA
Vehicles (auto-compartment SUPERSEDED / scope-containers GOOD; LINT-21 binding green) and the **Santana /
Lange** exemplar on Hot Pursuit (doorway ✓ · felony ✓ with the 594 U.S. 303–04 reservation · broad
reading limited at 313) + reconciling prose. Belton composite stays caution/varies.

### 1.5 Mnemonic placements (register-verbatim, LINT-8 = 0)
GR#3 (RS/PC ladder) · DOMINOES (Fruits & Attenuation) · Bandiero hot/fresh-pursuit (Hot Pursuit). The
"two C's" (04c) was CUT per SD8, not registered — escalation path stays journaled. CREW confirmed
three-justification (C/RE/W never four) against the signed register (batch-19).

---

## 2. What S8 inherits (S8's owned work)

### 2.1 The LINT-17 join surface + `corpus_mention_baseline` (the 388 join is S8's)
- LINT-17 is green (0) and its allowlist is a **frozen snapshot**; the coverage ledger is the join surface
  (every row carries `page_backed` + `pointer`). The **NUM-04 388 bare-mention join has no machine
  artifact** and is **S8's** (unchanged from S6 handoff §1.2).
- `corpus_mention_baseline` is now **57** (52 brief-mention + 5 excluded-remit) — it was 56 at S6-close and
  58 pre-W10; the drift is the mini-lane L1 pooling terminals + repair-lane regen (benign, see §6). This is
  LINT-17's own current-corpus scan, **NOT the 388**.

### 2.2 The plain-link / linking passes (S8 owns)
- **LINT-5 = 2767 MED** (`link-every-case` bare-name class) — the plain-link pass. Includes the **Sources
  bare-name class decision** (SD6 / S9(e): parentheticals routed to S9) and the wikilink-vs-plain-italic
  upgrade for terminals that later become pages. The 20 un-placed R8 brief-mentions (accounting §B.3) live
  here too.
- **LINT-7 = 136 HIGH** (`glossary wiring`) — the **register-exemption decision** S8/S9 owns: the
  page-title variant class (e.g. "Plain View Doctrine" vs canonical "plain-view doctrine", ~140 in
  baseline) was ruled a **known-false-positive class EXEMPT from zero-new-HIGH** (batch-6 J′) — lint-avoidance
  must never drive content. S8 decides the register carve-out vs the rename.
- **wikilink-vs-plain-italic upgrade path**: batch-13 established the TEACH-02c wikilink upgrade (device-split
  Border cases); S8 generalizes it for terminals-that-become-pages.

### 2.3 Case-Index schema-3 generator flip (was S7/S8-owed → now S8's)
The live index is still **legacy 5-col** (`| Case | Holding | Good law | Home page(s) | CourtListener |`);
the R6 schema-3 flip is owed to the **single-writer generator** `scripts/build_case_index.py` (handoff
§3.2). This drives **LINT-16 = 621 HIGH** on the generated index (acceptance-sweep AC-1/AC-6). **Before the
flip, S8 must first regenerate the current index once to clear the stale Riley URL row (blocker B2).**

### 2.4 Transclusion mechanics (per S3 R12)
Not exercised at S7 (doctrine prose stayed self-contained). S8 owns the transclusion wiring per S3 R12.

### 2.5 Residual generated-index lint
**LINT-4 = 1 HIGH** on `content/index.md:55` (the master-index inverted-label residual) — cured by the
S3-owned **A7(4) index regen**, S8-adjacent.

---

## 3. Standing decisions that bind S8

- **Template rules A–J′** (batches 1–7): split-batch re-points own its category index + alias collisions
  (A); no broken mid-line pin deep-links (B); LINT-15/16 standalone per batch, NOT in `run_all` (C); no bare
  weight-tier words in cells (D); plain-italic registry mirror is the S7 standard (E/F); **rule G** — dead
  index-framing Related rows DROP with the real primary kept, zero-drop binds only owed ledger home_rows;
  **rule H** — a ledger home_row discharges by page-presence, the presentational tier (Key-table vs LCD
  bullet) is the author's S5 call; **rule I** — zero em-dashes inside table cells (LINT-10 sums a table as
  one block); **rule J/J′** — net-additive batches judged zero-new-HIGH + explained baseline-class deltas;
  known-false-positive classes (LINT-7 page-title) EXEMPT when the apparatus is doctrinally correct.
- **Type conventions**: `overview` (S3-owned, no case table, LINT-19) · `hub` (router, owns no point — the
  SD1 exempt class, added as a LINT-15 EXEMPT_TYPE for FA Framework) · `reference`/`craft` (cat-12/13
  exempt) · `practical` (checklist body). These EXEMPT_TYPES are auditable frontmatter, not the
  `overview:true` hack.
- **Single-writer surfaces** (never hand-edit): `build_case_index.py` (the Case Index), the coverage-ledger
  assembler `build_coverage_ledger.py` (ledger pointers — S7 hand-edits were REVERTED by regen at batch-10),
  `project.py` (the `courtlistener` frontmatter block), the registry via its own tooling. **The mint
  (`mint_page.py`) is the only page-birth path** — no second mint; discoveries route through it (inherits
  the cluster-collision guard).
- **Body-only-finalization** (ratified): an author may clean its **own** fresh page's mechanical lint;
  **S9 certifies**. Writer ≠ checker holds.

---

## 4. The S9 register — CONSOLIDATED (swept from the whole S7 journal)

S9 owns adjudication (1 Claude + 2 Codex panel per S1 R12); these are **known-state**, not S8's to fix:

1. **R3 born-draft universe** — the **entire 89-unit doctrine corpus + the 3 minted case pages** are
   `draft`/`under_review` and **await the S9 panel**. No rewritten page reaches S9 as `verified`.
2. **Anchor-cleanup register (~60+ sites, the NUM-03 mid-line `^pin` class)** — machine floor **LINT-9 =
   298** corpus-wide. S7's rule-B stripped broken deep-**links** to these anchors; the visible mid-line
   anchors themselves remain (S9/S6-owned). Named doctrine targets accumulated across batches:
   Jacobsen/Brower/Chesternut/Hiibel/Kolender · Hensley/Adams/Sibron/Whren · Gerstein/McLaughlin · the
   batch-10 +21 · Horton/Brown · Ybarra + case-page set.
3. **Field-I `unverified → superseded`/promotion class** — history pages Sanders/Frank/Quantity/Robbins/
   Trupiano (W3) + Rochin (W8) render Historical + overruling verb + wikilinked successor + ⚪; the
   *treatment-status promotion* is S9. Plus Cooley, Grady (→Trespass, under_review honest), Daniels (→RS
   R3 catch), Lee/Milam/Verdugo-⚪, Frank/Bell/Wyman + device-split records, Frazier/Riley/Anchondo
   under_review class, the 4-per-batch R3 verified→draft flips.
4. **Treatment derivations** — **Maez** treatment enrich (cache absent, honest); **Konan / Landor** 2026
   holdings owed S2 treatment-derivation (carried at issue-altitude only, metadata re-keyed).
5. **Cook 3-step (honest-residue)** — the doctrinal *Donald* Cook (277 F.3d 82, 86 (1st Cir. 2002), cluster
   776186) vs the ledger's *Oshan* Cook (3165557); the panel-re-key cure hit a **cache miss** on cluster
   776186; the **3-step S2 work order is documented at source** in the `R8-NONPAGE-LEDGER` row note; the
   page prose already cites the correct Donald Cook. A duplicate-mint first attempt was REVERTED
   (fail-closed guard held).
6. **Optional 8th-Cir hunt** — IDENTITY CATCH #8: the R8-note "Conner (8th)" required-side was the **consent**
   Conner (127 F.3d 663), refused fail-closed; Satterfield carries the required side alone; the intended
   8th-Cir inevitable-discovery case is an **optional S2 hunt**.
7. **Quote-fidelity G3/G4 items** — Otis/Camden/Boyd quote-pins + Adams quote (downgraded, batch-18);
   the self-caught Gilbert "direct result of the illegal lineup" + McNeil "serve different interests"
   (refuted/paraphrased, batch-17); Carpenter/Chatrie/IGG T4 quotes carried as LINT-2 med honest.
8. **S.Ct-pagination / star-pin confirms** — Wearry/Turner/Connick/Rothgery/Montejo (batch-17);
   capers/castillo docket mismatches; Williams star-sparsity; Byrd/Cotterman/Cano T3 upgradeable; the
   **Tuggle F.4th slip-pin** (§9 class); Ruckman ¶-pin (disclosed LINT-2 medium).
9. **LINT-2 [!note]-callout FP class** — batch-19 candidate: mirror the [!rule] carve-out for [!note]
   callouts (LINT-2 = 259 MED includes this FP class + case-page quotes).
10. **LINT-3 N5 re-point** — the 2 Chatrie LINT-3 FPs left the renamed scope (batch-1c); N5 coverage is dark
    on renamed "Lower-court developments" sections until S9's roster job (S5 R11/§9). LINT-3 = 11 LOW now
    (incl. the Suing Federal Officers D10 "no controlling amendment" LOW).
11. **Contradiction-sweep seed** — the D8 flashlight overbreadth seed + per-batch coherence notes:
    Hicks-sibling attribution (batch-6), Basher vs Curtilage:82 tier disagreement (batch-1b), Tuggle home
    gap, Andreas sole-home Related semantics, al-Kidd URL divergence, Hicks URL 111831-vs-111834, Chadwick
    index-glyph good-vs-caution mapping.
12. **COH-27 pending-marker poll** — the felony hot-pursuit reservation (Lange assumed-without-deciding) +
    the SACO unmapped circuits (1st/3d/4th/8th) + Morgan-6th now-resolved (71 F.4th 540) + Knight-11th;
    re-poll at S9.
13. **S6-carried S9 items** (handoff §4, still open) — zorn (corrupt Strike-3 cluster, off-CL decision
    owed), holcomb (withdrawn opinion watch), trent (unpublished-6th reverify), youngblood (year quirk),
    Williams/capers/castillo star-confirms.
14. **RUNBOOK §4-S9 inputs (a)–(e)** — acknowledged as ADOPTED in the S9 spec (line 441); per-item G2 (§7),
    the contradiction sweep (§4), and the tier-sampled conversion trail are S9 process inputs. The **per-item
    G2 fixture** = the D8 flashlight enumeration; the **seed** and **trail** live in the journal/decision-log.

---

## 5. Data-lake state

### 5.1 Manifest status distribution (computed fresh)
```
$ python3 -c "…json.load(_manifest.json)…"     total: 668 records
```
| status | count |
|---|---|
| verified | 421 |
| under_review | 186 (35 pre-existing S9-owed + 148 S6 mints + 3 S7 SACO mints) |
| verified_identity | 49 (frontier shells, not paged) |
| not_found | 4 |
| folded-alias | 4 |
| verified_off_cl | 2 (Entick, Wilkes) |
| fabrication_suspected | 2 (removed West/White pair) |

`stub: true` on 59; `stub: false` on 609. Record base 665 (S6-close) → **668** = the 3 SACO
`--add-candidates` (Nora / Al-Azzawy / Vaneaton), R1-smoked `verified_identity` → minted `under_review`.

### 5.2 The S7-minted 3
`United States v. Nora` · `United States v. Al-Azzawy` · `United States v. Vaneaton` — the D7 SACO wave
(mini-lane L2; orchestrator ran the S2 builder leg with the token; worker stopped honestly at the
credential boundary). Born `under_review`; on the authored ledger (148→151); finalized body-only.

### 5.3 The re-keyed 7 (repair lane, consolidated register)
`--rekey-lead-opinion-from-cache` (6/6): **King** 216733→9441559 · **Thornton** 134746→9434613 ·
**Gaetjens** None→4703206 · **R.W.** None→11312795 (batch-8 flip discharged) · **Konan** None→11266325 ·
**Landor** None→11346052 (metadata only, holdings stay S9). `--rekey-cluster-panel` (1): **Riley** cluster
8416508→**2680439**, cite 572-U.S.-1055→134-S.Ct.-2473 (expect-cite guard passed). **Morgan** resolved on
the MCP lane (71 F.4th 540, 6th Cir. 2023, cluster 9409483 / lead 9404959). **⚠ The Riley leg's
propagation is incomplete — see §6 B1/B2.** `project.py --write` re-projected the 7 case pages.

---

## 6. Gaps / uncertainties (honest, surfaced — do not chase silently)

1. **BLOCKER B1 — Riley LINT-13 (committed, 1 HIGH).** `--rekey-cluster-panel` wrote
   `identity.identity_method: "panel-cluster-rekey"`, a value **not in the `_schema.json:1165` enum**. The
   repair-lane close journal recorded "LINT-13 0"; the machine reads **LINT-13 = 1**, and HIGH is **3782,
   not 3781**. Orchestrator call: extend the enum (the surface is sanctioned → the value is legitimate, my
   read) or re-key Riley to an existing value. **Blocks close.**
2. **BLOCKER B2 — Case Index stale Riley row (non-idempotent).** The committed index carries Riley's
   pre-re-key URL (`8416508`); a fresh `build_case_index.py` yields `2680439` (1-line diff). Same root cause
   as B1 — the re-key wasn't propagated to the single-writer index. Fix: one regen. **Blocks close.**
3. **HIGH-count of record** — use **run_all TOTAL 6829 / HIGH 3782**; the journal's 3781 is B1-stale by
   exactly 1.
4. **LINT-16 = 622 corpus-wide standalone** — 621 = the legacy-5col Case Index (schema-3 flip owed to S8,
   §2.3) + **1 doctrine FP**: `Standing to Challenge a Search.md:79` "**Historical foil.**" (Jones role-label
   collides with the R7 weight-word "Historical"). Probable FP-class; S9/orchestrator carve-out-or-rephrase.
   Not caught by `run_all` (LINT-16 not in its roster — by design, batch-1 rule C).
5. **~16 home_rows frontmatter-homed-but-not-body-materialized** (accounting §A.2) — live homes + Case
   Index rows + coverage terminals (**0 drops**), but no table row on the home page. Mostly **§1983
   out-of-remit satellites** (Dupree/Nance/Perttu/Gutierrez/Olivier; GEO/Fikre already documented
   out-of-scope) likely destined for excluded-remit re-terminals; a few overview-home (no-table) + history
   cases. S8/S9 to disposition.
6. **20 R8 brief-mentions un-placed** (accounting §B.3) — retained as coverage-ledger `brief-mention`
   terminals (LINT-17-legal); the S8 linking pass owns whether to prose-mention them.
7. **`corpus_mention_baseline` 57 (ledger) vs 56 (S6 handoff §5.4) vs 58 (pre-W10)** — the drift is the
   mini-lane L1 pooling terminals + repair-lane regen; the **machine ledger (57) is authoritative**. Benign,
   surfaced so S8 doesn't chase.
8. **The R5 conversion trail has no standalone file** — it is the per-batch journal record; if S9 wants a
   machine-sortable trail it must be assembled from the journal (or the slip-stamp journal
   `s6-slip-stamp-journal.jsonl` for the 15 slip-only stamps, a different set).

---

## 7. File pointer index

| Artifact | Path |
|---|---|
| This handoff | `_run/o2-execute/S7-TO-S8-HANDOFF.md` |
| Acceptance sweep (spec §7) | `_run/o2-execute/S7-ACCEPTANCE-SWEEP.md` |
| Owed-rows accounting (zero-drop) | `_run/o2-execute/S7-OWED-ROWS-ACCOUNTING.md` |
| S6→S7 handoff (model + prior state) | `_run/o2-execute/S6-TO-S7-HANDOFF.md` |
| Run journal (S7 section = L889–end) | `_run/o2-execute/JOURNAL.md` |
| Authored ledger (151 rows + home_rows) | `_run/o2-execute/s6-authored-ledger.jsonl` |
| Coverage ledger (252 captions) + assembler | `_run/s6-coverage-ledger.json` · `_overhaul2/scripts/build_coverage_ledger.py` |
| Non-page placements (58 + 3) | `_run/o2-execute/R8-NONPAGE-LEDGER.json` |
| Repair-lane dispositions | `_run/o2-execute/S7-RL-DISPOSITIONS.jsonl` · `S7-L1-POOLING-DISPOSITIONS.{md,jsonl}` |
| Canonical survey | `_run/o2-execute/s7-survey.json` (regen `scripts/s7/survey.py`) |
| Point registry (+4 nodes) | `_overhaul2/points/registry.yaml` |
| Case-Index generator (single writer) | `scripts/build_case_index.py` |
| Mint CLI (only page-birth path) | `scripts/s6/mint_page.py` |
| Lake schema (B1 enum lives here) | `_overhaul2/lake/_schema.json` |
| Live manifest | `_overhaul2/lake/_manifest.json` |
| S7 spec / S8 spec / S9 spec | `_overhaul2/specs/S7-doctrine-production.spec.md` · `S8-linking-glossary.spec.md` · `S9-verification.spec.md` |
