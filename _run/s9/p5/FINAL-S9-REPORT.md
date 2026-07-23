# CSSI — S9 Verification & Release-Gate Report (FINAL)

**Phase:** S9 (Verification Pipeline & Release Gate), overhaul-2 EXECUTE, branch `overhaul2/execute`
**Report packet:** P5-REPORT · **lane/model:** `claude-opus-4-8` · **compiled:** 2026-07-22
**Status:** release gate assembled; every box PASS or logged-open; **G8 human publish pause not yet reached** (P6).

This is the run's definitive record, written for the instructor. Every count below is traceable to a
named artifact on disk; the paths are collected in `_run/s9/p5/FINAL-S9-REPORT-sources.json`. Nothing
here re-adjudicates a prior verdict — S9's own rulings (`_run/s9/p4/P4-RULINGS.md`) are treated as law.

---

## 1. Executive summary

S9 was the verification layer for the whole rebuilt corpus: 610 case pages, 79 doctrine pages, the
point registry, the lake of case records, the glossary, and the site navigation. Its job was not to
author anything but to **prove** what the earlier phases (S1–S8) built — every legal assertion, cite,
quote, holding, treatment badge, and cross-page claim — through an adversarial three-lane panel, a
blind concordance re-derivation, a 30-check lint roster, and a set of coverage instruments, all
recorded in a machine-checked ledger.

**What S9 verified.** Every tracked assertion in the corpus was enumerated (24,619 items across 9
object classes) and carried to a verdict — either an adversarial panel judgment, a blind Thread-N
re-read, or a green lint. 2,331 findings were raised and **all 2,331 were adjudicated** (zero
verdict-less findings). The panel ran with proven blindness: Thread-P was frozen and hash-stamped
*before* any blind re-read began, and no reviewer manifest disclosed a sibling vote.

**What S9 changed.** Adjudication produced **498 owed fixes (227 UPHELD + 271 MODIFIED); every one is
terminally FIXED.** These ranged from mechanical (pincite re-harvests, stale re-projections, home-role
mirror corrections) to substantive holding corrections that were reader-facing — e.g. Mitcham
(independent-source → inevitable-discovery), Perez (Chadwick/Gant miscite), Loera (affirmance basis),
Trent (an unpublished 6th-Circuit decision that had been rendered as binding), and the Oliver "in rural
areas" quote truncation. A discovery tripwire fired and pulled in 4 newly-decided circuit cases. A
known-red lint baseline (~3,300 style highs across LINT-3/10/11/12/16 etc.) was swept to zero. One
genuine mis-keyed case (Chapman v. California) was re-keyed to the correct merits opinion.

**What it guarantees now.** On the publish-blocking severity (HIGH), the corpus is clean: the lint
roster runs 0 HIGH across LINT-2..30 (`run_all.py` 2026-07-22 09:25:59, exit 0), the machine ledger
reconciles 0 HIGH with 0 open escalations (`check_ledger.py` 09:24:56), the R6 contradiction sweep
found 0 hits across 437 shared-point pairs, and all 79 doctrine pages clear the brief-quality composite
with 0 banned-layer (officer-BLUF) findings. The remaining open items are logged, not silent: 3 open
`_review-needed/` escalations for the user, the serial CourtListener identity batch (LINT-1) still
running, and the G8 human publish pause, which by design fires last (P6).

**Bottom line for the release decision:** the R13 release gate is satisfiable — every one of the 15
boxes is PASS or a logged, gate-compatible open item. What remains before the Vercel push is (a) the
LINT-1 serial-CL identity batch's result, (b) the drift re-check at the gate (R14.8), and (c) the
user's go-ahead at the G8 pause. Sources: `_run/s9/p4/campaign/R13-GATE-TABLE.md`,
`_run/s9/p5/P5-R14A-summary.md`, `_run/s9/p5/P5-R14B-summary.md`, `_run/o2-execute/JOURNAL.md` (S9).

---

## 2. Accuracy summary (the numbers)

### Adjudication

- **Assertion inventory:** 24,619 items / 9 object classes — case 3,826 · doctrine 985 · glossary 42 ·
  index 610 · lake-record 2,944 · ledger-row 15,943 · nav 179 · reference 10 · registry 80. 0 duplicate
  ids. (`_run/s9/assertion-inventory.json`; R13 R2 row.)
- **Findings raised:** 2,331. **Findings adjudicated:** 2,331 (bijective; 0 findings-without-adjudication).
- **Verdict split** (`_run/s9/p5/R14-1-fp-accounting.json`):

  | verdict | count |
  |---|---|
  | UPHELD | 227 |
  | MODIFIED | 271 |
  | DISMISSED | 1,831 |
  | ESCALATE | 2 |
  | **total** | **2,331** |

  The false-positive rate (DISMISSED / total) is **78.55%** — high because the panel was tuned as an
  adversarial refuter (default-to-refute), so most raised findings are correctly dismissed on evidence.
  **DISMISSED findings without a logged reason: 0** — all 1,831 carry a non-empty `adjudicated_holding`.

- **Fixes:** 498 owed fixes (= 227 UPHELD + 271 MODIFIED) ⇔ 498 fix chains, all terminal-**FIXED**
  (`_run/s9/p5/R14-7-escalations.json`). Loop distribution: 455 at loop-1, 21 at loop-2, 22 at loop-3
  (the `under_review`-blocked promotions). The `fixes.jsonl` file carries 541 rows total = 498 FIXED +
  1 FIXED-WITH-RESIDUAL + 42 intermediate NOT-FIXED rows, **each superseded by a later FIXED — 0
  NOT-FIXED terminals.** (R13 R4 row; `check_ledger.py` 2026-07-22 09:24:56.)

### Concordance (Thread-P vs. Thread-N, R5)

Thread-P (the frozen answer key) = **724 items (609 case + 115 doctrine)**, content-hash `8e51d0c8…`,
git-immutable since the P0 commit. It was frozen **~2h27m (8,849 s) before** the earliest blind
Thread-N read, proving blindness by timestamp. (`_run/s9/reconciliation-summary.json`; R13 R5 row;
`_run/s9/p5/R14-4-blindness.json`.)

- **Case concordance classes:** CONCORDANT-STRONG **460** · CONCORDANT-WEAK **48** · DISCORDANT-candidate
  **98** · UNREADABLE **3** (= 609).
- **Double-verified:** the blind Thread-N unblock arc raised STRONG concordance from 298 → **460
  (+162 double-verified)** and drove UNREADABLE 200 → 3. (`_run/o2-execute/JOURNAL.md`, P2 reconciliation.)
- **Discordances resolved:** the P2 discordance pass adjudicated **112 candidates from cached evidence
  (0 CL calls): 111 benign** (76 caption-variance + correctly-keyed cluster-collision watches + no-caption
  + N-blind-unread + already-resolved) **and 1 genuine mis-key — Chapman v. California**, re-keyed from a
  2016 cert-denial cluster to the 1967 merits opinion (386 U.S. 18, cluster 107359 / lead 9423348),
  UPHELD + FIXED. (`_run/s9/P2-DISCORDANCE-DISPOSITIONS.jsonl`; finding F-S9-P2-CHAPMANCAL.)
- **No-regression floor:** declared 724 / dispositioned 724 / join-miss 0 / **0 silent absences**.
- **Doctrine concordance:** CONCORDANT-WEAK 65 · DISCORDANT-candidate 14 · N-SKIP-DISPOSITION 36 (= 115).

### Blindness audit (R14.4)

Freeze hash `8e51d0c8…6433c8` reproduces from the canonical `items[]` and is attested identically in
**all 1,357 opus-lens groups and 3,945 codex manifests**. 2,121 panel attestations all assert
`independent="isolated review; no sibling votes/adjudications disclosed"` and
`recorded_before_reconciliation=true`; all **6,881 panel votes** carry
`recorded_before_other_votes_read=true`; **0 contaminated manifests.** (`_run/s9/p5/R14-4-blindness.json`.)

### Panel calibration table (R14.1 — prompt-tuning signal, never auto-suppression)

Per-lane vote behavior, joining each lane's vote verdict against the final adjudication
(`_run/s9/p5/R14-1-fp-accounting.json`):

| Lane | votes | refute-rate | refute-precision (refuted→DISMISSED) | stands-precision (stands→UPHELD/MOD) | read |
|---|---|---|---|---|---|
| codex-A | 2,291 | 32.6% | **97.7%** (729/746; 17 overruled) | 29.7% | conservative refuter — rarely refutes, near-perfect when it does, but 70% of what it lets "stand" is dismissed by quorum |
| codex-B | 2,294 | 63.7% | 79.3% (1160/1462; 302 overruled) | 21.3% | most trigger-happy false-refuter (302 refutes overruled) |
| claude-opus-panel | 2,296 | 81.7% | 92.4% (1732/1875; 143 overruled) | **79.8%** | the designed adversarial refuter — highest refute-rate and best-calibrated on both axes |

The three lenses are complementary: codex-A's precision + codex-B's sensitivity + the opus lens's
balance produced the 2-of-3 quorum that killed the 1,831 false positives while sustaining 498 real fixes.

---

## 3. Negative-treatment census + splits / frontier table

### Negative-treatment census — 18 records (the "reversal-of-fortune" watch)

Every lake record whose `field_i_validity` is not `good_law`/`unverified` — **7 superseded + 11 caution**
(`_run/s9/p5/MAINTENANCE-HANDOFF.md` §1; source: lake `treatment.field_i_validity`):

| case | status | limiting case(s) |
|---|---|---|
| Aguilar v. Texas | superseded | Illinois v. Gates (abrogated) |
| Gouled v. United States | superseded | Warden v. Hayden (overruled) |
| Jones v. United States | superseded | Rakas / Salvucci (overruled) |
| Michigan v. Jackson | superseded | Montejo v. Louisiana (overruled) |
| Olmstead v. United States | superseded | Katz v. United States (overruled) |
| Spinelli v. United States | superseded | Illinois v. Gates (abrogated) |
| Wolf v. Colorado | superseded | Mapp v. Ohio (overruled) |
| Boyd v. United States | caution | Warden v. Hayden (limited) |
| Coolidge v. New Hampshire | caution | Horton v. California (limited) |
| Escobedo v. Illinois | caution | Miranda / Kirby / Moran v. Burbine (limited) |
| Mathis v. United States (1968) | caution | Howes v. Fields (limited) |
| Monroe v. Pape | caution | Monell (limited) |
| New York v. Belton | caution | Arizona v. Gant (limited) |
| Oregon v. Elstad | caution | Missouri v. Seibert (limited) |
| Saucier v. Katz | caution | Pearson v. Callahan (limited) |
| Thornton v. United States | caution | Arizona v. Gant (limited) |
| United States v. Agurs | caution | United States v. Bagley (limited) |
| United States v. Chadwick | caution | California v. Acevedo (limited) |

Each is on a 90-day citator-alert cadence (bucket A, next re-check **2026-09-28**), the highest-priority
decay bucket (`_run/s9/p5/MAINTENANCE-HANDOFF.md` §2).

### Taught splits / frontier table (including the P4 movements)

The verification surfaced live circuit disagreements the corpus teaches; the P4 tripwire updated three
of them (rulings P4-07/09/11):

| split / frontier question | how the corpus stood at build | P4 movement (case, court, date) | side |
|---|---|---|---|
| **Hash-match private-search** (does a matched hash defeat REP / require a warrant?) | strict side 9th vs. permissive 5th/6th named on *Private and Foreign Searches* | **United States v. Lowers** (4th Cir., 2026-03-10, published) — hash value does not defeat REP; warrant required absent prior human view | strict (4th joins) |
| | | **United States v. Brillhart** (11th Cir., 2026-07-09) — human-seeded hash match = private search | permissive (11th joins) |
| **Canine sniff at an apartment common hallway** (curtilage?) | corpus flagged only the state-case curtilage split + May-Shaw | **United States v. Eric Johnson** (4th Cir., 2025-08-05, published) — sniff in common hallway did not intrude curtilage; *opposite* 7th Cir. Whitaker | opens the federal Whitaker↔Johnson split |
| **Post-Bruen gun possession as reasonable suspicion** | uncatalogued | **United States v. Wilson** (5th Cir., 2025-07-17, published) — visible *lawful* possession alone cannot ground RS ("presumptively lawful nationwide") | new frontier node |

All four were ingested as born-draft lake stubs (citations pending on CL) with split-map narrative
edits on the affected pages; case pages were not created (frontier-stub depth). Sources: `_run/s9/p4/P4-RULINGS.md`
P4-07/08/09/11; `_run/s9/p4/campaign/` tripwire artifacts (TW-DIFF / I5-DIFF).

---

## 4. The tripwire narrative (FIRED → EXECUTED → CLOSED)

R7's fail-closed tripwire: *any two-key-real, gate-passing case that S6's coverage logs do not account
for triggers a full 13-category re-run.* It fired once and was closed in one full pass.

- **FIRED (RULING P4-07).** Predicate: **United States v. Lowers** (4th Cir., 2026-03-10, published,
  cluster 10807484, docket 24-4546). Two-key-real (independent codex-web + Claude-web, CL-confirmed
  incl. holding read). It takes a position in the taught hash-match private-search split — doctrine-grain
  content the corpus states — yet predates the build by ~4 months and appears in **no** S6 artifact. That
  is a discovery miss, not currency drift → fail-closed.
- **EXECUTED (RULINGS P4-08, P4-09).** The full **13-category frontier re-run** ran at I5 depth,
  dual-model (3 I5 units already run this phase + 10 fresh codex web lanes + Claude coverage): **270 raw
  candidate rows → 220 distinct** (`TW-DIFF.json` / `I5-DIFF.json`), then a diff lane vs. S6 logs and the
  corpus, then serial-CL verification of every not-accounted find.
- **CLOSED (RULING P4-09).** The remedy ran once, in full. Dispositions: **2 additional pre-build
  discovery misses** (Eric Johnson, Wilson — see §3); **2 floored with reasons** (Williams — Hudson
  reaffirmance, fully covered; Gonzalez-Arocho — fact-bound good-faith win, uniform per S6); currency
  citers (31 post-build) + companion Brillhart routed to R7.1/R12 **watch, not misses**; single-key flags
  (Klein v. Martin, Gonzalez cert-statement) → relevance-gate referrals.

**The 4 ingested cases:** Lowers, Brillhart, Eric Johnson, Wilson — 4 born-draft lake stubs + split-map
edits, **far below the >10-page human-pause threshold**, so no pause fired. No further re-run is owed:
the fail-closed remedy ran exactly once, as specified. (`_run/s9/p4/P4-RULINGS.md`; `_run/o2-execute/JOURNAL.md` P4.)

---

## 5. The release gate (R13) — 15 boxes, final statuses

Rule: R13 passes iff every box is PASS *or* a logged `_review-needed/` escalation (gate-compatible).
Statuses below reflect the P5 adjudications (rulings P5-01..04) applied on top of the assembled evidence
table `_run/s9/p4/campaign/R13-GATE-TABLE.md`.

| Box | final status | basis |
|---|---|---|
| **R1 — panel** | PASS | Machine panel invariants green; 21 sub-quorum findings documented (RULING P5-01(ii)); black-letter ≥2-approval inside inv2 (green). |
| **R2 — inventory** | **PASS** (RULING P5-03) | 24,619 items decompose exactly: panel-scoped 7,459/7,459 covered (0 verdict-less); 154 lint-governed structural residuals are R14(6)'s domain; implicit-group-PASS + lint coverage satisfies "zero verdict-less". |
| **R3 — 10-gate** | PASS | G1–G10 + dimension fields on all 2,331 findings; per-item G2 fixture committed (knock-and-talk flashlight). |
| **R4 — machine ledger** | PASS | `check_ledger.py` 09:24:56 = HIGH 0, resolved-escalations 22, open 0; findings 2,331 == adjudications 2,331; self-test green (F-DEMO-001). |
| **R5 — concordance** | PASS | Freeze hash reproduces + git-immutable + frozen-before-N; no-regression floor 724/724; 0 silent absences. (Benign sidecar nit, §9.) |
| **R6 — checklist sweep** | PASS | 437/437 shared-point pairs examined, **0 contradiction hits.** |
| **R7 — completeness** | PASS | 5 instruments ran dual-model; tripwire fired → executed → closed (§4); >10-page pause not triggered. |
| **R8 — lint roster** | **PASS** | `run_all.py` 09:25:59 (exit 0): TOTAL 895 / **HIGH 0** / 884 med / 11 low; LINT-2..30 all 0 HIGH; 14 self-test gates PASS. **LINT-1 (CL identity) = PASS — 4,425 refs verified cluster-first under the builder credential; 5 wrong-cluster URLs found+fixed (MCP-confirmed canonical ids); 40 adjudicated false-positive rows documented (COH17-GATE-SLICE.md); pass-sample 10/10 CONFIRM** — serial-CL gate only, under the builder credential (§6/§9). |
| **R9 — S8 handoff** | PASS | Carat-leak 0; shingle scope proven; 188/188 ambiguity re-reviews; 231/231 fragments traced; deep-link landing PASS in real Chrome. |
| **R10 — coherence** | PASS | Callout↔registry deep-equal conflict resolved as **Amendment A2**; 80/80 nodes measured; override slugs 13/13; LINT-12 = 0, LINT-14 = 0. |
| **R11 — per-spec samples** | PASS | 75/75 mermaid rendered + inspected; the one failed sample (Lange T3) re-opened its class → FIX-T3 swept and resolved. |
| **R12 — maintenance handoff** | **PASS** (artifact now on disk) | `MAINTENANCE-HANDOFF.json` (schema-valid) + `.md` emitted 2026-07-22; 6 sections, all counts derived. **GH#2 filing is PENDING at P6 publish** (logged). |
| **BRIEF — composite** | **PASS** (RULING P5-02(a)) | 76 substantive doctrine pages PASS, 0 open-high, 0 banned-layer; the 3 FLAGs are section-parent `index.md` hubs, convention-exempt (rules live on paneled child pages). |
| **WHITE — unbannered** | PASS | LINT-6 HIGH 0; 151 files carry ⚪, all bannered; RULING P4-14 rendered-sample verification. No ⚪ reaches a reader unbannered. |
| **G8 — publish pause** | **SCHEDULED (P6)** | Human gate sequenced after the release-go-ahead, before the Vercel push. Not-yet-due, logged so it is never silently skipped. |

**Headline:** 14 boxes PASS (R2, R12, and the BRIEF composite promoted by the P5 rulings; R8 carries
LINT-1 as a pending serial splice); **G8 scheduled for P6.** 0 boxes BLOCKED.

**LINT-1 serial batch — current state.** The serial-CL identity check is running under the builder
credential (RULING P5-04). The live ledger `_run/s9/p5/lint1-ledger.json` has processed 77 rows so far
with **3 candidate HIGH mismatches** pending the gate-slice adjudication: *Alasaad v. Wolf* (opinion
4855246 → cluster names "Moore v. State"), *Alvarez v. City of Brownsville* (opinion 4536189 → names a
different case), and *Barnes v. Felix* (opinion 10584846 → HTTP 404). These are the cluster≠opinion-id
class (LAW-02); the Claude MCP gate lane independently re-judges every LINT-1 violation + a 20-row sample
of its passes (RULING P5-04(a)). The 803 false-401 rows from the CL v4 auth change are preserved but not
counted (`_run/s9/p5/lint1-ledger.INVALID-401s.json`; §9).

---

## 6. Self-audit results (R14 — all 8 checks)

The self-audit is the meta-layer: it audits the pass's own accounting, blindness, coverage, sampling,
and escalations. Checks 1/4/5/7 = `_run/s9/p5/P5-R14A-summary.md`; checks 2/3/6 = `_run/s9/p5/P5-R14B-summary.md`.

| # | check | result | evidence |
|---|---|---|---|
| 1 | False-positive accounting | **PASS** | 2,331 adjudications; 0 DISMISSED-without-reason; per-lane calibration surfaced (§2). `R14-1-fp-accounting.json` |
| 2 | Adjudication sampling re-check (20 UPHELD/MODIFIED legal fixes, independent lane) | **PASS — 20/20 CONFIRM** | `R14-2-sample.jsonl` |
| 3 | Pass-sample re-read (10 zero-finding pages, cached primary text) | **PASS — 10/10 CONFIRM** | `R14-3-passreread.jsonl` |
| 4 | Blindness audit (manifest diffs) | **PASS** | Freeze hash proven + frozen-before-N + 0 contamination (§2). `R14-4-blindness.json` |
| 5 | Inventory completeness (zero verdict-less) | **PASS** | 7,459/7,459 panel-scoped covered; 154 lint-governed residuals deferred to (6). `R14-5-completeness.json` |
| 6 | Lint spot-verification (6 green lints × 3 samples + firing negative controls) | **PASS with 1 discrepancy → resolved** | `R14-6-lintspot.jsonl`; see below |
| 7 | Escalation audit (nothing dropped at loop cap) | **PASS** | 498 chains all FIXED; 22/22 loop-cap chains documented; 2 ESCALATE carry routing files. `R14-7-escalations.json` |
| 8 | **Drift re-check at the gate** (pending markers + currency re-confirmed immediately pre-publish) | **SCHEDULED at publish (P6/R15)** | Marker-poll ran at P4 (holcomb fired); the *immediate-pre-publish* re-confirmation is a P6 step. `_run/s9/p4/marker-poll-p4.jsonl` |

**The check-6 discrepancy (found, then fixed).** R14B's hand-check contradicted a green LINT-6: its
dual-date guarantee passed on the literal string `"null"` because the stdlib YAML-subset parser reads
`as_of_content: null` as a non-blank token. That left **7 unbannered `verified`/`good_law` pages** (Karo,
County of Riverside v. McLaughlin, Conner, Mathis, Basher, Florida v. Riley, Leary) with a placeholder
content-date passing a check that should have fired. Packet **P5-DATES** resolved it: added a shared
`is_null_token` helper + a banner-aware `_blank_date` predicate (so bannered stubs still legitimately
defer dates), backfilled all 7 records' `as_of_content` from `identity.date_decided` (the Buie
precedent), re-projected the 7 pages, and added 2 fixtures. Post-fix: **LINT-6 = 0 HIGH corpus-wide,
self-test 6/6, full roster still 0 HIGH.** (`_run/s9/p5/P5-DATES-summary.md`, `_run/s9/p5/P5-DATES-fixes.jsonl`.)

---

## 7. Escalations register (open items for the user)

Three `_review-needed/` files remain genuinely OPEN and gate-compatible (logged, never silent). Two
other files that were still marked open at gate-assembly time were adjudicated CLOSED by RULING P5-02(b)
(lint3-chatrie → measured-subsumed; batch4-duplicate-CL-lane → resolved-by-completion). Source:
`_run/s9/p5/MAINTENANCE-HANDOFF.md` §5; `_run/s9/p4/P4-RULINGS.md` P5-02.

| file | what it is | what it needs |
|---|---|---|
| `_review-needed/s9-p2-delgado-inbox.md` | **INS v. Delgado** (466 U.S. 210, cluster 111148) — a coverage gap; the case is not ingested. | Route through the S6 R8 born-draft pipeline (INGEST recommended). |
| `_review-needed/s9-p2-entrap2-r7-routing.md` | **Outrageous-government-conduct** viability — an R7 absence-sweep question on the Entrapment page. | Spawn an Entrapment-page finding *only if* a grounded circuit divide emerges. |
| `_review-needed/threadN-lyle-unread.md` | **United States v. Lyle** (lead 8415374) — unread on all 3 blind Thread-N sweeps (2/1218 = 0.16%); carried under the R5 no-regression floor, not silently lost. | A single-lane blind re-read retry in a quiet window. |

The 2 ESCALATE adjudications (F-S9-P2-DELGADO, F-S9-P2-ENTRAP2) map exactly to the first two files;
Lyle is carried as an R5 floor disposition. No escalation is unrouted (`_run/s9/p5/R14-7-escalations.json`).

---

## 8. Maintenance handoff pointer

The ongoing-maintenance seed is emitted as a schema-valid machine artifact plus a human summary,
**filed to GH#2 (`Enragedsaturday/cssi` issue #2) at publish (P6)** on gate-pass + go-ahead:

- **Machine:** `_run/s9/p5/MAINTENANCE-HANDOFF.json` (`s9.maintenance-handoff.v1`, self-describing `_schema`).
- **Human:** `_run/s9/p5/MAINTENANCE-HANDOFF.md`.

Six sections: (1) **CL citator-alert seed list** — 72 rows across 6 sub-blocks (12 marker-poll incl.
Carter/Noem/Lange + holcomb superseding-text watch, 3 I4-triage watches, 31 post-build recency citers,
companion Brillhart, 7 cite-pending clusters, the 18-case negative census); (2) **dual-date decay
schedule** — 4 buckets (negative-treatment 90 d → 2026-09-28; good-law 180 d → 2026-12-27; content
re-verify 365 d → 2027-06-30; null-treatment stubs re-derive at S6); (3) **fragment re-validation
queue** — 231 traced + a 117-row pin-upgrade queue (37 cases) + the Entick unmonitorable note;
(4) **deck-rebuild precondition** — 57 decks / 1,773 cards, LINT-25 = 0 unresolved stems (measured PASS);
(5) **open `_review-needed/` register** — 9 files with per-file what-remains; (6) **P5-handoff notes** — 9.

### P5-handoff notes (carried forward, non-blocking)

1. **COH-B registry-notes — 62** (16 pincite-drop + 45 different-authority + 1 scope-divergence);
   registry cites poorer-not-wrong; **0 registry edits owed** (informational).
2. **Secondary-home placement convention** (Amendment A3): soft relations accepted; 3 unrendered Key
   declarations narrowed (Moore-Bush, Cortez, Sokolow). Open question: a corpus-wide narrow-vs-add sweep?
3. **S1 §3.1 / S2 SD9 conflict** (P4-20(b)): weight labels derive from court level; overruled status
   lives in field_i + badges + Historical prose. Built convention stands; an S1-side text reconcile is owed.
4. **+36 LINT-7 register-coverage mediums** from de-hyphenation (S8 coverage-linker class, non-blocking).
5. **Haynes v. Washington scope_note variant + Satterfield L80 medium** — data-hygiene normalization owed.
6. **5th-Cir Wilson caption collision** — *United States v. Wilson* (9th Cir. 2021, cluster 5296785) vs.
   the 5th Cir. 2025 post-Bruen stub (cluster 10636220); caption/slug disambiguation owed.
7. **Ledger regen-durability** — keep `ledger-exceptions.jsonl` + the reconstruction provenance durable
   across future regens (P5-01 reconstructed 2 orphan findings + 21 sub-quorum rows).
8. **LINT-2 mediums census — 683** block-quotations without a nearby pincite across 207 files (0 high,
   non-blocking maintenance editorial backlog).
9. **Out-of-remit referrals** — Loper Bright (correctly absent), ABA Formal Op. 512, AI-citation-sanctions
   material, Klein v. Martin (AEDPA), Gonzalez cert-statement: instructor-reference candidates, not S6 R8 draft.

---

## 9. Run-mechanics appendix

### Phases

| phase | what happened | key dates |
|---|---|---|
| P0 | Assertion inventory (24,619) · Thread-P freeze (724, hash-stamped) · lint-roster codification (LINT-3 rebuilt lake-driven; LINT-30 = R4 invariant script) | 2026-07-09 |
| P1 | Panel fan-out (2 codex + 1 opus lens, 1,357 groups) · Thread-N blind reads (1,218 pairs) · opus 3rd-lens (1,357/1,357) | 2026-07-09..07-19 |
| P2 | R5 reconciliation (leg-C unblock; floor 724/724) · panel-findings adjudication (2,329 → 2,331 adjudicated) | 2026-07-11, 2026-07-19 |
| P3 | Fix fleet: 498 owed → 476 FIXED + 22 escalated, then loop-3 all FIXED | 2026-07-19 |
| P4 | Sweeps (Mermaid/R6/S8H/COH/I1-I5) · tripwire fired→closed · known-red lint campaign → 0 HIGH | 2026-07-20..07-22 |
| P5 | R13 gate assembly · R14 self-audit · LINT-30 ledger tidy · LINT-1 serial batch · this report | 2026-07-22 |
| P6 | Publish → verify-live → retire legacy pipeline (G8 human pause first) | **pending** |

### Lane / model separation (writer ≠ checker, enforced structurally)

- **Thin orchestrator (Fable):** ledger, specs, statuses, and **every legal verdict / ruling** — no
  content edits.
- **Finders:** codex panel lanes + codex Thread-N blind reads (case-grain); the o2-opus-xhigh lens
  (doctrine-grain 3rd lens). Reviewers never edit.
- **Evidence-prep + fixers:** `o2-opus-xhigh` (`claude-opus-4-8`) worker lanes.
- **Re-review:** a non-author model (codex or Fable) — e.g. P3 sample 6/6 PASS, P4 codex 34/34 CONFIRM.
- **Serial-CL:** the only lane allowed live CourtListener — the builder REST credential + the Claude MCP
  marker/tripwire lane. All calls logged.

### Serial-CL ledger totals

- **Claude MCP lane:** ~30 calls (identity-slice 77, markers, tripwire verifications) —
  `_run/s9/p4/p4-cl-calls.log`.
- **Builder token (REST, codex-invoked):** I4 batch 539 + recency 11 + star-refetch 59 + second-source 53
  + promo-identity 20; plus P3's 2 sanctioned Katz-concurrence calls (`_run/s9/p3/p3-cl-calls.log`).

### Honesty items (recorded, not hidden)

- **Chapman re-key.** The one genuine concordance mis-key: `chapman-v-california` pointed at a 2016
  cert-denial cluster (8428427); re-keyed to the 1967 merits opinion 386 U.S. 18 (cluster 107359 / lead
  9423348) via 1 sanctioned prime CL call + cache-only re-key (F-S9-P2-CHAPMANCAL). (Separately, the P1
  identity slice caught `illinois-v-fisher` accepted onto the *wrong* case — In re Mirsky, a DC bar
  matter — on a docket-number coincidence; cured by a sanctioned caption re-key.)
- **Vote-semantics cutover.** The panel machine emitted per-*assertion* verdicts while the checker + signed
  demo read a vote's verdict as being about the *finding*. RULING flipped the mapping (refuted↔stands),
  recorded the cutover (`vote-semantics-cutover.json`), and normalized 32 pre-cutover rows in place. A
  downstream gap from that cutover — 2 finding rows (Gates, Brinegar) left unpersisted while their
  adjudications survived — was reconstructed at P5 from the pilot source (RULING P5-01(i)), restoring
  findings 2,329 → **2,331 == 2,331 adjudications**.
- **The 401 event.** The Claude MCP CourtListener token hard-expired mid-phase (pause #8, 2026-07-09);
  CL-dependent work halted and elevated (user-only re-auth), independent work continued, and the identity
  slice resumed post-re-auth. At P5 the CL v4 API began refusing unauthenticated requests (401); the
  LINT-1 batch runs under the builder credential per Amendment A1(3), and the 803 false-401 rows are
  preserved as evidence, **not counted** (`_run/s9/p5/lint1-ledger.INVALID-401s.json`; RULING P5-04(b)).
- **Limit-event resumes.** Codex hit a ChatGPT rolling usage cap (pauses #8/#9: 403 after ~1h50m at
  conc-18, ~5h recovery) → multi-window drain, every driver killed clean at checkpoint, ledger-truth
  recomputed at relaunch. Claude hit its own weekly quota mid opus-3rd-lens (wave-32) → resumed on reset.
  A P4 monthly-limit event killed 10 lanes on 2026-07-20 → all resumed from transcript, **zero work lost.**
- **Invalid-run preservations.** The P4 recency query form had a bug (`filed_after` must be an API param,
  not a query string); the invalid run was **preserved** and re-run correctly. Likewise the 803 false-401
  LINT-1 rows are kept as an INVALID artifact rather than deleted, so the diff is auditable.

---

*Compiled by packet P5-REPORT (`claude-opus-4-8`), WRITE-SCOPE `_run/s9/p5/` only, no live CL. This
report asserts no legal proposition without a verified pincite and re-adjudicates no prior verdict; it is
an evidence-linked record of what S9 did. Machine index of every cited artifact:
`_run/s9/p5/FINAL-S9-REPORT-sources.json`.*


---
## PUBLISHED (P6, 2026-07-23)
- **Deploy:** main d50a62a9 → b99b4ab6 (fast-forward) → pushed → Vercel production READY.
  Live: https://cssi-search-and-seizure.vercel.app
- **Verify-live:** 10-page curl sweep all 200 (one 308 trailing-slash redirect); internal dirs
  (_run/_overhaul2/_review-needed/scripts) 404 ✓; corrected McNeely cluster id live; Mitcham
  corrected holding live in the Case Index; hash-split page carries Lowers/Brillhart.
  Browser dogfood: hard-load deep-link lands centered+tinted IN PRODUCTION (the FIX-A2 fix);
  search live w/ highlights + the Smith (2024) retarget target; flashcards 1,176/26 intact;
  Horton correctly un-bannered post-promotion. Fragment visual leg: a real user-gesture click
  fired from the live page; observation blocked by extension domain permissions (CAPTCHA on
  07-21, permission wall on 07-23) — mechanical trace 231/231 verbatim stands; recommend a
  human click-through spot-check. Mobile leg: capture viewport fixed in tooling — responsive
  CSS verified at S4; recommend a phone spot-check.
- **S4 R8 retirement EXECUTED + re-verified:** com.cssi.quartz launchd agent booted out +
  plist removed; :8787 connection-refused ✓; serve-public.py + redeploy.sh git-rm'd;
  /cssi-ingest re-pointed to the content/-canonical git→Vercel flow (0 legacy refs);
  vault frozen w/ _FROZEN-README.md marker.
- **R12 handoff FILED:** https://github.com/Enragedsaturday/cssi/issues/2#issuecomment-5055868436
- **Standing flag:** the separate flashcard-rebuild run remains owed (decks frozen, attested).
