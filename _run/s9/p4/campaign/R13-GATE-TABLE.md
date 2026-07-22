# R13 RELEASE-GATE TABLE — evidence assembly (packet P5-GATE)

**Lane/model:** `P5-GATE` / `claude-opus-4-8` · **Generated:** 2026-07-22T09:26Z · **Write-scope:** `_run/s9/p4/campaign/` (read everything else).
**Nature:** verdicts stay the orchestrator's; `status_proposed` below is an evidence-cited *proposal*. No re-adjudication; deterministic coverage; gaps flagged, not papered.
**Governing:** `_overhaul2/specs/S9-verification.spec.md` R13 + the R2–R12 Check lines + Amendments A1/A2/A3.
**Live snapshots:** full lint roster `run_all.py` 2026-07-22 **09:25:59** (exit 0); `check_ledger.py` **09:24:56**. A sibling packet **P5-LEDGER** was concurrently editing the ledger during assembly (see R4).

## Headline

- **Boxes:** 15 total — **11 PASS**, **4 ESCALATED**, **0 BLOCKED**.
- **Lint roster (R8):** HIGH=0 across LINT-2..30 (+ LINT-15/16 standalone 0/0); LINT-1 = serial-gate-only.
- **Ledger (R4):** check_ledger HIGH=0, resolved-escalations=22, open-escalations=0; findings 2331 == adjudications 2331.
- **Concordance (R5):** thread-P frozen (hash reproduces; git-immutable; N-after-P); no-regression floor 724/724, 0 silent absences.
- **Contradiction sweep (R6):** 437/437 pairs, 0 hits. **Brief composite:** 76/79 doctrine pages PASS, 0 open-high, 0 banned-layer.
- **Escalations are gate-compatible** (R13 = every box PASS *or* a logged `_review-needed/` escalation). 5 open review-needed files (below).

## Gate boxes

| Box | status_proposed | Requirement (quoted, condensed) | Evidence (paths + counts) |
|---|---|---|---|
| **R1-panel** | PASS | Every legal-assertion surface reviewed by the full adversarial panel; ≥2-of-3 refute kills the assertion/finding as framed; black-letter rule text additionally requires ≥2 affirmative reviewer approvals. Check: every paneled finding has 3 lane votes with manifests; zero `resume` invocations. | votes.jsonl=6882 votes; panel-attestations.jsonl=1.9MB; _run/s9/manifests/ (3959 input-manifests); opus-reviews/ (374 Claude-lens packs, group_id-keyed) + panel-results/ (4071 codex packs). check_ledger inv2 (paneled→3 votes; ≥2-refute never plain-UPHELD) GREEN (HIGH=0, 09:24). 21 sub-quorum paneled findings are DOCUMENTED exceptions (_run/s9/ledger-exceptions.jsonl, RULING P5-01(ii)) — P2-adjudicated on evidence, reported non-high. |
| **R2-inventory** | ESCALATED | P0 deterministically extracts every tracked assertion from every object class ... Each item gets an `assertion_id`; zero items may end the run without a verdict. Check: the inventory enumerates every R9-class object; the completeness audit (R14.5) fails on any verdict-less item. | assertion-inventory.json = 24619 items across 9 R9-object-classes (case 3826 · doctrine 985 · glossary 42 · index 610 · lake-record 2944 · ledger-row 15943 · nav 179 · reference 10 · registry 80). Every FINDING is adjudicated: findings.jsonl 2331 == adjudications.jsonl 2331; 0 findings-without-adjudication. P4-LEDGER-BRIDGE.jsonl = 763 P4-sweep candidate rows joined via named artifacts (not the panel ledger). BUT check_ledger --completeness (09:24) fires 1 HIGH: '[inv5/completeness] 22318 inventory items without a verdict (R14.5)'. Only 2301 items are referenced by a found+adjudicated finding; the other 22318 carry NO explicit per-item verdict (they passed the panel/R5/gates with no finding = implicit-PASS, for which check_ledger --completeness has no representation). |
| **R3-10gate** | PASS | PRACTICES §3 runs per entry with PASS/FAIL/FLAG per gate G1–G10; G2 runs per enumeration item ... the corrected knock-and-talk flashlight pitfall is the committed fixture. Check: gate rows exist per proposition; a sampled enumeration shows per-item gate rows. | Findings carry `gate` (G1..G10) + `dimension` fields (2331 rows); opus-reviews reviewed[] carry per-assertion dimension/verdict/reasons. Per-item G2 fixture committed (knock-and-talk flashlight, commit 4b48a4a per spec). R11 SMP-S7 sample re-verifies G2 support by tier (T3 = paraphrase-vs-holding breadth). Enumeration per-item gate rows evidenced in the panel packs. |
| **R4-machine-ledger** | PASS | The signed ledger + the five reconciliation invariants checked by script, not agent, fail-closed in CI ... post-fix re-review by a model that did not author the fix. Check: the invariant script runs green at the gate; the demo instance validates against the schema. | FINAL check_ledger.py run 2026-07-22 09:24:56: `status=CHECKED HIGH=0 resolved-escalations=22 open-escalations=0`. findings 2331 == adjudications 2331 (inv5 count); 0 findings-without-adjudication; 2 former orphan adjudications reconstructed into findings.jsonl (RULING P5-01(i), Gates/Brinegar FP-log). self_test green (F-DEMO-001 validates clean; fail-fixture fires all 5). fixes.jsonl 541 rows (498 FIXED / 1 FIXED-WITH-RESIDUAL / 42 NOT-FIXED intermediate). |
| **R5-concordance** | PASS | Thread P frozen at P0, hash-stamped; Thread N blind for every case; fundamental discordance → panel + serial-evidence-cited adjudication naming what diverged and which stands; No-regression floor: every Thread-P item absent from N is dispositioned, never silently lost; zero silent absences. Check: t… | thread-P.json content_hash 8e51d0c8... REPRODUCES EXACTLY from items[] canonical JSON (json.dumps sort_keys,ensure_ascii=False,compact per build_thread_p.py:585-591); git-immutable since P0 commit a4e2ac32 (2026-07-09 15:51 EDT gen / 16:13 EDT commit); disk-bytes hash 45904bc5 == P0-commit blob (0 mutation). thread-N-reads.jsonl = 1947 reads, ALL recorded_before_reconciliation=true, earliest 2026-07-09T18:19 EDT (after freeze). reconciliation-summary.json: no_regression_floor {declared 724, dispositioned 724, floor_satisfied true, join_miss 0, 0 orphans}; case classes CONCORDANT-STRONG 460 / -WEAK 48 / DISCORDANT-candidate 98 / UNREADABLE 3; P2-DISCORDANCE-DISPOSITIONS.jsonl. |
| **R6-checklist-sweep** | PASS | Every entry's review form runs the checklist (framed/explained/cited/related/narrowed/expanded/good law/abrogated/current treatment); the contradiction sweep covers 100% of shared points. Check: checklist columns complete per object; the sweep's pair list covers 100% of shared points; every contradi… | pair-list.json = 437 pairs = 100% shared-point coverage (RULING P4-01: 7 registry-multi-host + 430 case-multi-home; B-PAIR-summary). Sweep executed PAIR-P1..P4 = 110+110+110+107 = 437/437 examined, 0 skipped, 0 HITs (0 cross-page semantic contradictions). Checklist answers carried in the opus-reviews reviewed[] + R3 gate fields per object. |
| **R7-completeness** | PASS | Five instruments, all finds routed two-key → relevance gate → S6 R8 → born draft → the panel; >10 new pages ⇒ human pause. Tripwire (fail-closed): any two-key-real, gate-passing case S6's logs do not account for ⇒ the full 13-category re-run fires. Check: per-instrument artifacts exist; every find h… | I1 currency: recency-queries.json (13 cats, 11 lanes, 162 keys) + marker-poll-p4.jsonl (12 rows; Carter-25-885 / Noem / Lange all UNCHANGED). I2 gap: I2-GAP (488 anchors, 7135 progeny, 520 candidates, 74 findings high20/med54). I3 dual-TOC: 80/80 registry points present, 142 TOC topics, 11 zero-home candidates. I4 absence: I4-TRIAGE 181/181 dispositioned, 0 MOVED-NEEDS-FIX. I5 frontier: 100 distinct cases, 61 NOT-ACCOUNTED. TRIPWIRE FIRED→EXECUTED→CLOSED (RULINGS P4-07/08/09): predicate US v. Lowers (4th 2026-03-10); all 13 categories re-ran dual-model (TW-DIFF 270→220 distinct); 4 born-draft stubs (Lowers/Brillhart/E.Johnson/Wilson) — below the >10-page pause. |
| **R8-lint-roster** | PASS | run_all.py (extended) runs 2–30 green on the finished corpus (1 at the serial gate); every row has fixtures. All run in CI fail-closed (HIGH blocks; the roster gates publish). | FINAL roster run_all.py 2026-07-22 09:25:59 (exit 0): TOTAL 895 / HIGH 0 / med 884 / low 11. LINT-2..30 ALL 0 HIGH; all 14 self-test gates PASS. LINT-15 skeleton + LINT-16 case-tables standalone = 0/0 HIGH (lint16 620→0 via the generated-index carve-out, RULING P4-16b). Non-high residue (non-blocking): LINT-2 683 med, LINT-5 23 med, LINT-7 157 med, LINT-3 11 low, LINT-30 21 med (the P5-01(ii) documented sub-quorum exceptions). Campaign CLOSED (RULINGS P4-15..21; _review-needed/s9-p4-lint-baseline-campaign.md). |
| **R9-s8-handoff** | PASS | NUM-03 pins/anchors clean; S8 ledger ≥1-in-10 + 100% of adjudicated ambiguity resolutions re-reviewed; fragments land end-to-end; zero fragments on tier-3 paraphrases; shingle scope proven; landing visuals pass. | S8H-A: LINT-9 carat-leak = 0 (self-test 2/2 PASS; corpus 0 high/med/low); shingle scope (LINT-29) proven (embeds excluded, raw restatements fire). S8H-B: 188/188 adjudicated ambiguity resolutions re-reviewed (100%); 1419/14184 mentions + 54/539 term-pages sampled (1-in-10); 231/231 `#:~:text=` fragments traced to lake quotes — 7 findings (2 low, 5 med, 1 needs_cl), zero landing miss. S8H-ORCH-browser-samples.md: SPA + hard-load deep-link landing PASS (centered + persistent tint), S4 popover/tooltip legs PASS (real Chrome @ localhost:8080). |
| **R10-coherence** | PASS | Callout↔registry deep-equal (Amendment A2: semantic equivalence + citation consistency); every override slug resolves; S2F-07b re-check; prose↔lake consistent; LINT-12/14 green; every REVIEW-marked migration row adjudicated. Check: deep-equal pass corpus-wide; zero unresolved slugs; zero un-adjudica… | COH packet: callout↔registry 80/80 nodes measured; override-slug 13/13 resolve; S2F-07b 10/10 provisional slugs, 0 1:N split. Deep-equal spec-vs-build conflict RESOLVED as S9 Amendment A2 (RULING P4-04, USER-APPROVED 2026-07-21); COH-B 78/78 dispositioned (15 DISMISS framing-tolerance, 62 registry-notes→P5, 1 callout ADD remedy.exclusionary). prose↔lake 609/610 (1 draft skipped), 11 defects adjudicated in fix waves. LINT-12=0 + LINT-14=0 in the FINAL roster (P4-05 re-projection class + campaign). A13 REVIEW-rows = 0 exist. |
| **R11-perspec-samples** | PASS | Per-spec samples clean or escalated-and-resolved; TEACH-03 conversions sampled BY TIER; Mermaid/visuals rendered + inspected against the page's rule. Check: sample logs per spec with escalation on any failure (a failed sample re-opens its class). | MER-P1..P5: 75/75 mermaid blocks rendered + visually Read, 75/75 faithful=PASS + legible, 0 findings. SMP-S6S7: S6 17 gate/floor verdicts + 2 pause packets (recorded USER dispositions) all CONFIRM; S7 34 tier samples = 33 CONFIRM + 1 DISCREPANCY (Lange T3 bound-pin). The Lange failure REOPENED the T3 class (R11) → T3-REOPEN (162 unprovenanced-pin assertions / 59 slip-only cases) → FIX-T3 executed the P4-12 ladder (star-refetch oracle; second-source harvest exhausted; page-side conversions; 43 content + 21 lake files). B45 placement convention (RULING P4-13). |
| **R12-maintenance-handoff** | ESCALATED | S9 emits, as machine artifacts: the CL citator-alert seed list, the dual-date decay schedule, the fragment re-validation queue, the deck-rebuild precondition attestation, and the open `_review-needed/` register — filed to GH#2 on publish. Check: the handoff artifact exists, is schema-valid, and GH#2… | No handoff artifact on disk yet (searched _run/s9/*handoff*, _run/s9/p4/*handoff*, _run/s9/maintenance* — none). Input material staged: marker-poll-p4.jsonl (watch seed), I4-TRIAGE-watch.jsonl (3 R12 watch adds), R12-pin-upgrade-queue.jsonl, the open _review-needed/ register (this table). |
| **BRIEF-composite** | ESCALATED | The blocking brief-quality composite on every doctrine page (an S1-conformant brief: rule callout verified, test up front, pitfalls, no banned layer — a page with perfect cites but a muddled brief FAILS). | 79 type=doctrine pages assembled from opus-reviews (Claude 3rd-lens) ∪ panel-results (codex) ∪ findings/adjudications. PASS 76 / FLAG 3. Per-page: (a) [!rule] callout 77/79 present; (b) panel-covered 76/79 (opus∪codex∪finding); (c) open-HIGH findings on 0/79 pages; banned-layer (officer-BLUF) findings 0/79 (corpus grep for BLUF/'bottom line up front' in doctrine pages = 0, confirming absence). Full sub-table below. |
| **WHITE-unbannered** | PASS | ⚪ never reaches a reader unbannered (LINT-6: ⚪ never unbannered). | FINAL roster LINT-6 (treatment-status presence) HIGH=0. 151 content files carry U+26AA; all pass the banner gate. RULING P4-14: the 21 post-promotion LINT-6 highs ruled lint-model false positives; lint6 _banner_driven amended to mirror caseHelpers.shouldDraftBanner (fieldI-unverified leg) + fixture; rendered behavior verified correct on sample (Youngblood/Egbert bannered via fieldI leg; Horton correctly un-bannered as good_law). Defense-in-depth via the S2 R12 publish gate. |
| **G8-publish-pause** | ESCALATED | The G8 publish pause (§0 register #6) precedes any production push. | G8 is a human gate sequenced at P6/R15 (publish → verify-live → retire), after the release-gate go-ahead. Not yet reached in the pipeline (this is P5 gate assembly). |

### Per-box notes

- **R1-panel (PASS):** Machine-checkable panel invariants green. 21 sub-quorum findings carry the P5-01(ii) documented-exception mechanism (panel era closed; re-paneling post-adjudication ruled theater). Black-letter ≥2-approval is inside inv2's remit (green).
- **R2-inventory (ESCALATED):** Inventory is complete (24619/9 classes) and every finding is adjudicated. The R14.5 completeness invariant, as coded, treats 'no finding' as 'no verdict' → 22318 flagged. ORCHESTRATOR CALL: adopt implicit-PASS semantics (clean item = verified via panel review + R5 concordance + clean gates) OR require explicit per-item verdict emission. Not a guessed assertion; a definitional gate question. P5-LEDGER is concurrently editing the ledger.
- **R3-10gate (PASS):** Gate machinery present and populated; deeper per-proposition exhaustiveness is R14's meta-audit. Supporting box (feeds R2/R4).
- **R4-machine-ledger (PASS):** TIMING: sibling P5-LEDGER drove LINT-30 to 0 DURING this assembly. The 09:17 roster (pre-amendment check_ledger) showed LINT-30=22 HIGH; check_ledger.py was amended ~09:19 (RULING P5-01: ledger-exceptions.jsonl + orphan reconstruction + escalation-absorption), and the 09:25 roster shows LINT-30 HIGH=0. check_ledger.py / findings.jsonl / ledger-exceptions.jsonl are git-modified/untracked (P5-LEDGER working tree, uncommitted).
- **R5-concordance (PASS):** SIDECAR NIT (benign, not a defect): thread-P.sha256 records the CONTENT hash 8e51d0c8 (build_thread_p.py:657, by design — docstring 'lands in BOTH header and .sha256 sidecar'), NOT `shasum -a 256 thread-P.json` (=45904bc5), so `shasum -c thread-P.sha256` cosmetically FAILS. Freeze integrity is independently witnessed by git immutability + the reproducing embedded content_hash. Carried escalation: United States v. Lyle (threadN-lyle-unread.md, OPEN) — both lenses unread (2/1218 = 0.16%), dispositioned candidate/unreadable per no-regression floor, not silently lost.
- **R6-checklist-sweep (PASS):** 437/437 pairs clean; the flashlight Knock-and-Talk×Plain-View exhibit and every negative-treatment / overruled-Historical leg verified consistent across homes. No contradiction hit → no adjudication owed.
- **R7-completeness (PASS):** All 5 instruments ran dual-model; tripwire evaluated on evidence and its remedy executed once in full then CLOSED (P4-09). Finds ledger-terminal via the P4 rulings; >10-page pause not triggered (4 stubs).
- **R8-lint-roster (PASS):** Roster green on HIGH (the publish-blocking severity). LINT-1 (CL identity) DELIBERATELY EXCLUDED here — serial-CL-gate-only under the builder credential (S9 A1.3); it runs at P6/R15's serial gate, not this dry run. Version skew logged in R4: the 09:17 roster showed LINT-30=22 HIGH pre-amendment; 09:25 shows 0.
- **R9-s8-handoff (PASS):** All handoff legs verified; the 7 S8H-B fragment findings are non-high enrichment (1 needs_cl routes to the serial lane). R9(c) lake-field-present check defers to next lake build per Amendment A1.2; zero-fragments-on-tier-3 unconditional and reported clean by S8H-B.
- **R10-coherence (PASS):** Deep-equal escalation (_review-needed/s9-p4-callout-registry-deepequal.md) CLOSED via Amendment A2. 62 registry-note cite-divergences are an informational P5-handoff set (registry cites poorer-not-wrong; no page defect).
- **R11-perspec-samples (PASS):** The one failed sample re-opened its class as the spec requires; the class was then swept and resolved (FIX-T3 / RULING P4-12). Escalated-and-resolved path exercised.
- **R12-maintenance-handoff (ESCALATED):** PENDING per P5 task assignment — the R12 maintenance-handoff artifact is being assembled by a sibling packet; not yet emitted, so not schema-checkable and GH#2 not yet referenced. Gate-compatible open item (not a defect); becomes PASS when the artifact lands.
- **BRIEF-composite (ESCALATED):** 0 substantive brief failures (0 open-high, 0 banned-layer, all 76 substantive pages PASS). The 3 FLAGs are all section-parent index.md landings: two-definitions-of-search/index.md + third-party-doctrine.../index.md (no [!rule] — their rules live on child registry-home pages, opus-covered; convention-exempt, mirrors COH-B hub dismissal + S5 overview convention) and the-exclusionary-rule/index.md (callout present, registry-home remedy.exclusionary, but the parent index was not individually paneled — its 3 child doctrine pages were). Flagged not silent; for orchestrator convention confirmation.
- **WHITE-unbannered (PASS):** LINT-6 green + P4-14 rendered-sample verification. No ⚪ reaches a reader unbannered.
- **G8-publish-pause (ESCALATED):** SCHEDULED (P6) — not-yet-due, not a defect. The user holds both human gates (release-gate go-ahead + publish pause); G8 fires before the Vercel production push per R15. Recorded as a logged open item so it is never silently skipped.

## Brief-quality composite — per doctrine page (79 type=doctrine pages)

Coverage = opus 3rd-lens (opus-reviews) ∪ codex panel-results ∪ ≥1 adjudicated finding. open-high = HIGH-severity findings on the page NOT terminally resolved (DISMISSED / FIXED / closed-escalation). banned-layer = officer-BLUF findings. **No page re-review performed — evidence assembly only.**

**Rollup:** 76 PASS / 3 FLAG · callout present 77/79 · panel-covered 76/79 · pages with open-high findings **0** · pages with banned-layer findings **0**.

| Doctrine page | callout | panel-covered | open-high | banned | proposed |
|---|:--:|:--:|:--:|:--:|:--:|
| confessions-interrogation-and-the-fifth-amendment/Due-Process Voluntariness of Confessions.md | y | y | 0 | 0 | PASS |
| confessions-interrogation-and-the-fifth-amendment/Miranda Waiver and Invocation.md | y | y | 0 | 0 | PASS |
| confessions-interrogation-and-the-fifth-amendment/Miranda and Custodial Interrogation.md | y | y | 0 | 0 | PASS |
| confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md | y | y | 0 | 0 | PASS |
| fair-trial-and-reliability-doctrines/Brady and Giglio.md | y | y | 0 | 0 | PASS |
| fair-trial-and-reliability-doctrines/Entrapment.md | y | y | 0 | 0 | PASS |
| fair-trial-and-reliability-doctrines/Eyewitness Identification.md | y | y | 0 | 0 | PASS |
| foundations-and-the-fourth-amendment/Common Law Origins.md | y | y | 0 | 0 | PASS |
| foundations-and-the-fourth-amendment/Fourth Amendment Recalibration.md | y | y | 0 | 0 | PASS |
| searches/Abandonment.md | y | y | 0 | 0 | PASS |
| searches/Aerial and Enhanced Surveillance.md | y | y | 0 | 0 | PASS |
| searches/Curtilage.md | y | y | 0 | 0 | PASS |
| searches/Electronic Surveillance and Title III.md | y | y | 0 | 0 | PASS |
| searches/Open Fields.md | y | y | 0 | 0 | PASS |
| searches/Plain View Doctrine.md | y | y | 0 | 0 | PASS |
| searches/Private and Foreign Searches.md | y | y | 0 | 0 | PASS |
| searches/Tents.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/Cell-Site Simulators.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/Investigative Genetic Genealogy.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/Real-Time Tracking.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/Reverse-Keyword and Geofence Warrants.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/Third-Party Doctrine and CSLI.md | y | y | 0 | 0 | PASS |
| searches/the-third-party-doctrine-and-digital-surveillance/index.md | n | n | 0 | 0 | FLAG |
| searches/two-definitions-of-search/Reasonable Expectation of Privacy.md | y | y | 0 | 0 | PASS |
| searches/two-definitions-of-search/Trespass.md | y | y | 0 | 0 | PASS |
| searches/two-definitions-of-search/index.md | n | n | 0 | 0 | FLAG |
| seizures/Collective Knowledge and the Fellow-Officer Rule.md | y | y | 0 | 0 | PASS |
| seizures/Seizure of Property.md | y | y | 0 | 0 | PASS |
| seizures/Seizure of the Person.md | y | y | 0 | 0 | PASS |
| seizures/Stop-and-Identify.md | y | y | 0 | 0 | PASS |
| seizures/Terry Stops and Reasonable Suspicion.md | y | y | 0 | 0 | PASS |
| seizures/Traffic Stops.md | y | y | 0 | 0 | PASS |
| seizures/arrests/Arrest and Arrest Warrants.md | y | y | 0 | 0 | PASS |
| seizures/arrests/Arrest in the Home.md | y | y | 0 | 0 | PASS |
| seizures/arrests/Prompt Probable-Cause Determination.md | y | y | 0 | 0 | PASS |
| standards-of-proof/Probable Cause.md | y | y | 0 | 0 | PASS |
| standards-of-proof/Reasonable Suspicion.md | y | y | 0 | 0 | PASS |
| standards-of-proof/The Proof Ladder.md | y | y | 0 | 0 | PASS |
| the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md | y | y | 0 | 0 | PASS |
| the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/Fruits and Attenuation.md | y | y | 0 | 0 | PASS |
| the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/Inevitable Discovery and Independent Source.md | y | y | 0 | 0 | PASS |
| the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md | y | y | 0 | 0 | PASS |
| the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md | y | n | 0 | 0 | FLAG |
| the-right-to-counsel/Lineups and the Right to Counsel.md | y | y | 0 | 0 | PASS |
| the-right-to-counsel/Sixth Amendment Right to Counsel.md | y | y | 0 | 0 | PASS |
| the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene.md | y | y | 0 | 0 | PASS |
| the-warrant/executing-a-warrant/Knock-and-Announce.md | y | y | 0 | 0 | PASS |
| the-warrant/executing-a-warrant/Scope Manner and Related Issues.md | y | y | 0 | 0 | PASS |
| the-warrant/getting-a-warrant/Franks Challenges.md | y | y | 0 | 0 | PASS |
| the-warrant/getting-a-warrant/Particularity.md | y | y | 0 | 0 | PASS |
| the-warrant/getting-a-warrant/Probable Cause in the Affidavit.md | y | y | 0 | 0 | PASS |
| the-warrant/getting-a-warrant/The Neutral and Detached Magistrate.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Absolute Immunity.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Civil Asset Forfeiture.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Malicious Prosecution under the Fourth Amendment.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Qualified Immunity.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Retaliatory Arrest.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Section 1983 Liability and Qualified Immunity.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Suing Federal Officers.md | y | y | 0 | 0 | PASS |
| use-of-force-and-liability/Use of Force.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/Consent Searches.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/Knock and Talk.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/Searching Effects and Containers.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Community Caretaking.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Destruction of Evidence.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Emergency Aid.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Entry to Arrest.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Fire-Scene Entries.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/home-entry-and-search/Securing the Scene.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/programmatic-and-special-needs-searches/Border Searches.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/programmatic-and-special-needs-searches/Special Needs and Administrative Searches.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-person/SIA Alcohol Tests.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-person/SIA Cell Phones.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-person/SIA Persons.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-vehicle/Automobile Exception.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-vehicle/Checkpoints and Roadblocks.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-vehicle/Inventory Searches.md | y | y | 0 | 0 | PASS |
| warrant-exceptions/searching-a-vehicle/SIA Vehicles.md | y | y | 0 | 0 | PASS |

**The 3 FLAGs (all section-parent `index.md` landings — gate-compatible, flagged for orchestrator convention confirmation):**
- `searches/the-third-party-doctrine-and-digital-surveillance/index.md` — no `[!rule]` callout; not individually panel-covered. (findings=0, open-high=0, banned=0)
- `searches/two-definitions-of-search/index.md` — no `[!rule]` callout; not individually panel-covered. (findings=0, open-high=0, banned=0)
- `the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md` — not individually panel-covered. (findings=0, open-high=0, banned=0)
  - *two-definitions-of-search/index.md* + *third-party-doctrine.../index.md*: section-parent landings; their `[!rule]` rules live on the child registry-home pages (Reasonable Expectation of Privacy / Trespass; CSLI / Cell-Site Simulators / Geofence / Real-Time Tracking / IGG) — all opus-covered with callouts. Convention-exempt (mirrors COH-B hub dismissal + S5 overview convention).
  - *the-exclusionary-rule/index.md*: registry-home `remedy.exclusionary`; callout PRESENT (COH-B PAGE-FIX add); the parent index was not individually paneled but its 3 child doctrine pages (Fruits & Attenuation / Inevitable Discovery & Independent Source / Good-Faith Exception) were.

## `_review-needed/` register (open/closed)

Open files appear as ESCALATED gate rows (gate-compatible). **Open = 5** (4 marked + 1 unmarked-stale); **Closed/Resolved = 4**.

| File | state | gate row | basis |
|---|---|---|---|
| `_review-needed/s9-p4-callout-registry-deepequal.md` | CLOSED | — | RESOLVED 2026-07-21 — user-approved S9 Amendment A2 (semantic-equivalence standard); COH-B terminal dispositions. |
| `_review-needed/s9-p4-lint-baseline-campaign.md` | CLOSED | — | CLOSED 2026-07-22 — lint campaign executed to completion (RULINGS P4-15..21); roster residue = documented P5 rows only. |
| `_review-needed/chatrie-scotus-2026-correction.md` | CLOSED | — | RESOLVED — S9 serial-CL adjudication (UPHELD-reframed); Chatrie page created + geofence framing reframed corpus-wide; 'Escalation CLOSED'. |
| `_review-needed/s9-p3-underreview-promotions.md` | CLOSED | — | RESOLVED — all 22 escalations closed (loop-3 22/22 FIXED, PROMO-FIX; queue_outstanding=0). Names 22 F-S9-PR ids now absorbed by check_ledger (P5-01(iii)). |
| `_review-needed/s9-p2-delgado-inbox.md` | OPEN | ESCALATED | OPEN routing — INS v. Delgado coverage gap (466 U.S. 210); batch through S6 R8 pipeline; no RESOLVED/CLOSED marker. |
| `_review-needed/s9-p2-entrap2-r7-routing.md` | OPEN | ESCALATED | OPEN routing — outrageous-government-conduct viability for the R7 absence sweep (Entrapment page); no RESOLVED/CLOSED marker. |
| `_review-needed/lint3-chatrie-recent-dev-false-positive.md` | OPEN | ESCALATED | OPEN tool-precision ticket (LINT-3 N5 SCOTUS-tag branch FP ×2 on Chatrie circuit-case entries); content verified correct; self-stated gate disposition = PASS-with-logged-escalation. |
| `_review-needed/threadN-lyle-unread.md` | OPEN | ESCALATED | OPEN escalation — US v. Lyle both Thread-N lenses unread (loop cap 3); carried per R5 no-regression floor (2/1218 = 0.16%); single-lane retry owed in a quiet window. |
| `_review-needed/coverage/_ESCALATION-batch4-duplicate-CL-lane.md` | OPEN-unmarked | ESCALATED | S5-era (2026-06-30) coordination stand-down note (duplicate CL lane on S5 Phase-B batch 4); the standing-down lane made no writes; no RESOLVED marker — likely stale/resolved-by-completion (corpus has 610 case pages). Flag for orchestrator disposition. |

