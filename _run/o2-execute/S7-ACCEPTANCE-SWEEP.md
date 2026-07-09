# S7 Acceptance Sweep — spec §7, machine-evidenced

> **O2 EXECUTE · branch `overhaul2/execute` · HEAD `66d8f79` · swept 2026-07-09.**
> Worker: S7 CLOSE (lane `claude` / model `claude-opus-4-8`). **Writer ≠ checker: this is a
> machine-evidenced return for the orchestrator to adjudicate — it does NOT self-certify.**
> Each spec `§7` checkbox below carries the exact command + output (or the process pointer) and a
> verdict: **PASS** / **PASS-WITH-NOTE** / **FAIL**. Honest notes where reality nuances the box.
> Two FAIL-CLOSED blockers are surfaced up front; do not merge without adjudicating them.

---

## BLOCKERS (fail-closed — surfaced, not hidden)

**B1 — LINT-13 = 1 HIGH (committed): Riley `identity_method` breaks the lake schema enum.**
Commit `66d8f79` (repair lane, `--rekey-cluster-panel` Riley leg) changed Riley's
`identity.identity_method` from `"name+docket"` (valid) to **`"panel-cluster-rekey"`**, a value the
schema enum at `_overhaul2/lake/_schema.json:1165` does **not** contain
(`['citation+party-text','name+docket','frontier-identity','off_cl','not_found','fabrication-check','blocked','pending']`).
```
$ python3 scripts/lint/lint13_schema.py
[LINT-13] 1 violation(s): 1 high, 0 medium, 0 low
{"lint":"LINT-13","file":"_overhaul2/lake/cases/Riley v. California.json",...
 "$.identity.identity_method: value 'panel-cluster-rekey' is not in enum [...]"}
```
The repair-lane close journal recorded **"LINT-13 0 / HIGH 3781"**; the machine now reads
**LINT-13 = 1 / HIGH 3782**. The new sanctioned surface minted an enum value the schema was never
taught. **Fix is one of two orchestrator calls:** (a) extend the `_schema.json` identity_method enum
to admit `panel-cluster-rekey` (the surface is sanctioned, so the value is legitimate — my read), or
(b) re-key Riley to an existing enum value. Writer ≠ checker — I do not choose.

**B2 — Case Index is 1 row stale (same root cause as B1): Riley URL not propagated.**
Re-running the single-writer generator changes exactly one line — the Riley opinion URL:
```
$ python3 scripts/build_case_index.py   # → 1 insertion(+), 1 deletion(-)
- ...[[Riley v. California]]...[opinion](.../opinion/8416508/riley-v-california/)
+ ...[[Riley v. California]]...[opinion](.../opinion/2680439/riley-v-cal-united-states/)
```
The committed index carries the **pre-re-key** URL; a fresh regen picks up the re-keyed value from
the updated Riley frontmatter. The repair lane re-keyed the lake record + re-projected the case page
but **did not regenerate the Case Index after**. Fix: one `build_case_index.py` regen (diff-clean
except this line). Together B1+B2 mean **the Riley panel re-key propagation is incomplete** — 2 stale
downstream artifacts from one repair-lane leg.

---

## §7 acceptance criteria

### AC-1 — Every Table 1/2 unit rendered per R1 at its signed tier; LINT-15 green corpus-wide; zero tier changes without a logged amendment (R2).
**Verdict: PASS.**
- **Units rendered:** Phase 2 closed all 13 categories → **89 units born draft** (survey: `89 substantive
  pages`) + 3 S7-minted case pages. Journal batch-1…20 close each records the born-draft units.
- **LINT-15 green corpus-wide:** `python3 scripts/lint/lint15_skeleton.py` → **`0 violations`** (self-test
  PASS). NOTE: LINT-15/16 are intentionally NOT in the `run_all` roster (batch-1 template rule:
  "LINT-15/16 standalone per batch"); they are enforced at the mint staged-lint gate + per-batch
  standalone + here corpus-wide. The §8 "fail-closed in CI" intent is met by the mint gate + this
  standalone sweep, not by `run_all`. (Observation, not a defect.)
- **Tier changes = exactly 1, logged:** `grep` of the journal finds **one** tier change — **CAF C→B**
  (batch-20), booked as "the LOGGED R2 AMENDMENT C→B" with evidence (8 Keys / 3 sub-doctrines). Phase-0
  carried all tiers **UNCHANGED** (R2); every split minted children at their signed change-list tiers.
  1 amendment is far below the **§9 >10-page pause guard** — no pause triggered.

### AC-2 — Zero rewritten pages reach S9 as `verified`; carried assertions carry gate rows (R3).
**Verdict: PASS.**
- **82** doctrine pages carry literal `status: draft`; the balance to 89 are the overview / hub /
  reference / craft exempt-class units (S3-owned overviews, the FA-Framework hub, cat-12/13
  reference/craft) — none is `verified`. The 3 S7-minted case pages are born `under_review`. R15
  renders the ⚪ draft banner for `status ∈ {draft, under_review}`. The entire 89-unit corpus + 3 mints
  **awaits the S9 panel** (R3 universe).
- Carried R3 assertions route to S9 as gate rows (per-batch journal); 4 O1-era illegitimate `verified`
  case records were flipped **→ draft** across batches 12/16/17.

### AC-3 — Zero non-current-term slip-op pinpoints; every conversion carries tier + evidence (R5).
**Verdict: PASS-WITH-NOTE.**
- **Doctrine pages: 12 slip-op occurrences** (`grep "slip op\." content/ | grep -v content/cases/`),
  classified:
  - **Chatrie ×3** (REP:131, Reverse-Keyword:98, Third-Party:109) — 609 U.S. ___ (2026), current-Term
    SCOTUS → legitimate **T4**.
  - **Case v. Montana ×6** (Emergency Aid:26/41/41/49/108, Arrest in the Home:126) — 607 U.S. ___ (2026),
    current-Term SCOTUS → legitimate **T4** (Emergency Aid:108 self-annotates "current-Term slip pins
    stand, S1 R14 / S7 R5 T4").
  - **Trent ×1** (Collective Knowledge:63) — No. 25-5770, slip op. (6th Cir. **2026**), non-precedential
    current-year; slip is the only citation form (no reporter for the unpublished disposition);
    already S9-flagged (handoff §4 "trent reverify").
  - **NOTE — Tuggle ×1** (Aerial and Enhanced Surveillance:96): *United States v. Tuggle*, **4 F.4th 505
    (7th Cir. 2021)**, LCD bullet "(pinpoint: slip op. 5)". This is the **one non-current-term** slip-op
    pinpoint on a doctrine page. It falls squarely in the **spec §9 reserved class** ("F.4th pinpoints…
    upgraded at the maintenance loop") — reporter cite present (4 F.4th 505), only the internal pin is
    slip-style, no verbatim quote hangs on it. Sanctioned-exception read; surfaced for the orchestrator.
- **Case pages: 242 slip-op occurrences / 95 files** — all **S6-leg / S2-coordinated slip-style pins**
  (the case-page half of TEACH-03 was S2-coordinated), each carrying documented provenance in its
  `## Sources` ("CL carries the slip opinion… pin is slip-style per S2 A3"; e.g. Frederick, May-Shaw,
  Carloss, Taylor v. Riojas, Hughes). Not an S7 doctrine-production obligation; **S9 samples slip pins**
  (handoff §4). Attributed to the S6/S2 leg honestly.
- **Conversions carry tier + evidence:** every R5 conversion is logged per-batch in the JOURNAL with
  tier + evidence (e.g. Carpenter T3 / Collins T3 584 U.S. 586 / King slip→**T1 BOUND 462** op 9441559 /
  Byrd T3). There is **no consolidated conversion-trail file** — the trail is the per-batch journal
  record (the R5 conversion trail with provenance); noted for S9's tier-sampled re-verification.

### AC-4 — Zero field-framing sections; 13/13 logged dispositions (R7). Zero A2-class leaks on touched pages (R8). All R9 items landed-or-refuted with pointers.
**Verdict: PASS-WITH-NOTE.**
- **Field-framing = 0 corpus-wide** (survey: `field-framing 0`). The class DIED corpus-wide at batch-20
  (last hit converted per D2). 13/13 category dispositions logged (batches 1–20 closes).
- **A2-class leaks on touched pages = 0** (survey: `class1_no_standalone 0`, `class2_cl_confirm 0`). The
  pipeline-vocabulary leaks ("(No standalone page)", "CL confirms") are dead.
- **NOTE — 6 residual `class3_meta_intro` leak-lines** (survey: `leak-lines 6`), one each on the 6
  cat-6c home-entry pages (Community Caretaking, Destruction of Evidence, Emergency Aid, Exigent
  Circumstances and Hot Pursuit, Fire-Scene Entries, Securing the Scene). Each is the LCD-section
  placement-convention framing — "Role-based, circuit/state only (**no SCOTUS**; a Supreme Court holding
  belongs in Key cases regardless of date)". Whether the "(no SCOTUS…)" alternate counts as an R8/TEACH-02c
  leak (handoff §10 lists "LCD meta intros" within TEACH-02c) or as legitimate placement pedagogy is an
  orchestrator/S9 call. class1/class2 (the true A2 leaks) are both 0, so the **AC-4 R8 box (A2-class) is
  met**; the 6 class3 survivors are surfaced.
- **R9 items landed-or-refuted:** the spec-R9 NAMED pooling split (Massenburg / communication-nexus /
  Cook–Balser) landed on Collective Knowledge via mini-lane L1 (Nafzger/Ibarra/Balser terminals, two
  annex geography corrections); TEACH-04e donor conversions logged; 04c "two C's" ADAPTED (cut per SD8,
  escalation path open). Pointers in batches 7/8 + mini-lane L1.

### AC-5 — D5 section + node live on Community Caretaking (vehicles → persons → tombstone); D7 SACO section + node live with the split named honestly; D6 tiers hold; GAP-03c landed.
**Verdict: PASS.**
- **D5 live:** `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md` renders the
  vehicles→persons→home shape: "**### Seizing people for non-investigative purposes (public)**" (:42) →
  "**### The home is barred (tombstone)**" (:60, → Emergency Aid). Registry node
  **`seizure.person.noninvestigative-caretaking`** live (`registry.yaml:300`), statement FILLED,
  `home_page` set, `status: draft`, LINT-20 = 0.
- **D7 live:** `…/Entry to Arrest.md` renders the SACO section — surround-and-call-out (Nora spine,
  ★1054), containment-vs-exit-command poles (Al-Azzawy / Vaneaton), perimeter-defeats-flight, Harris
  remedy tail; split taught honestly (2d/6th/9th/10th vs 5th/7th/11th; 1st/3d/4th/8th unmapped). Registry
  node **`seizure.person.constructive-entry`** live (`registry.yaml:291`), statement FILLED, `status:
  draft`.
- **D6 tiers hold:** reverse-keyword/geofence + cell-site B; real-time/IGG/Title III C (batches 4).
- **GAP-03c landed:** Title III §702 + Third-Party cross-ref on Electronic Surveillance and Title III
  (batch-4).

### AC-6 — Em-dash blocks in budget corpus-wide (R11); TEACH-04d = 0 inversions; TEACH-12a = 0 missing H1s; TEACH-08 = 0 RD-family headings; TEACH-12b = 0 legacy skeletons.
**Verdict: PASS-WITH-NOTE (em-dash) / PASS (the four counters).**
- **TEACH-04d inversions = 0** (survey `inverted 0`); **TEACH-12a missing-H1 = 0** (survey `missing-H1 0`);
  **TEACH-08 RD = 0** (survey `RD 0`); **TEACH-12b rule-skeletons = 0** (survey `rule-skel 0`). All four
  died (last inverted + last rule-skel at batch-19).
- **Em-dash (LINT-10) — 3346 HIGH, attributed:**
  - **3217 = `content/cases/`** — the S6 case-page backlog, **outside S7's R11 doctrine-rewrite scope**
    (handoff §4 names it a steady-state class; S6 authored those under a different mint gate).
  - **103 = `content/index.md`** (site landing page, not an S7-rewritten doctrine page).
  - **17 = generated `Case Index.md`.**
  - **9 on 2 doctrine/reference pages:** 8 on `Common Legal Terms.md` (last touched at **W2/S3** tree
    migration `aa9b6a6` — a legacy glossary, NOT in S7's rewrite scope) + 1 on `Knock and Talk.md` (last
    touched at batch-10 `cb65df7` for a re-home, not an R11 rewrite — 1 residual block of 2 em-dashes).
  - **Doctrine corpus S7 rewrote is in budget** (survey em-dash density **4.9/1k**, 1019/208543 words);
    the 9 residuals are on 2 out-of-R11-scope / lightly-touched pages. Surfaced for completeness; the
    R11 rewrite-pass obligation (the "~48 pages" of handoff §4) is discharged.

### AC-7 — LINT-17 green at merge — every prose-named case has a ledger terminal state (R16).
**Verdict: PASS.**
```
$ python3 scripts/lint/lint17_coverage.py
[LINT-17] 0 violation(s): 0 high, 0 medium, 0 low   (self-test 9/9 PASS)
```
Also 0 inside `run_all` (LINT-17 is in the roster + self-test gate). Every prose-named party-v-party
caption resolves to a page or a coverage-ledger non-page terminal.

### AC-8 — S9 receives: per-item G2 fixture, contradiction-sweep seed, tier-sampled conversion trail (RUNBOOK §4-S9 inputs a–e acknowledged in the S9 spec).
**Verdict: PASS.** The receiving spec `_overhaul2/specs/S9-verification.spec.md` (**APPROVED
2026-07-04**) has internalized all three:
- **per-item G2:** §7 acceptance line 345 ("per-item G2"), §4 process lines 98/243; T3 re-verifies G2
  support (line 243). The D8 flashlight example is the canonical G2 fixture (interview record).
- **contradiction-sweep seed:** line 51 ("cross-page contradiction sweep"); seeded by the D8 flashlight
  overbreadth catch (handoff §3.8 / decision-log D8) + per-batch coherence notes (e.g. Hicks-sibling
  attribution, Basher tier disagreement, Tuggle home-gap).
- **tier-sampled conversion trail:** the R5 conversions logged per-batch in the JOURNAL (tier + evidence
  each); S9 spec §8 samples "≥1-in-10 R5 conversions by tier". No standalone trail file — the journal IS
  the trail (noted for S9).
- **RUNBOOK §4-S9 inputs (a)–(e):** the S9 spec line 441 records "**S7-interview inputs (a)–(e) ALL
  ADOPTED**"; RUNBOOK.md:409/492 carries them. Acknowledged.

---

## Final gate numbers (this sweep)

| Gate | Result | Note |
|---|---|---|
| `run_all` | **TOTAL 6829 / HIGH 3782 / MED 3026 / LOW 21** | journal said HIGH 3781 — **+1 = the B1 Riley LINT-13** |
| LINT-13 | **1 HIGH** | **B1 blocker** (Riley enum) |
| LINT-17 | 0 | self-test 9/9 |
| LINT-15 (corpus-wide standalone) | 0 | self-test PASS |
| LINT-16 (corpus-wide standalone) | 622 HIGH | 621 = Case Index legacy-5col (schema-3 flip owed **S8**); 1 = Standing "**Historical foil.**" R7 weight-word (FP-class, see below) |
| LINT-8 / LINT-20 / LINT-24 / LINT-25 | 0 / 0 / 0 / 0 | guardrails, point registry, url stability, deck stems all clean |
| LINT-21 | 10 LOW | `legacy-limited-*` override slugs bound-PENDING by cluster — expected R5 pending-state, not HIGH |
| survey (canonical regen) | 89 pp · em **4.9/1k** · slip-op 12(doc)+242(case) · leak 6 · ff 0 · rule-skel 0 · inverted 0 · RD 0 · missing-H1 0 · LCD 54 | regen byte-identical to committed (clean tree) |
| `npx quartz build` | **724 input / 2873 emitted**, exit 0 | matches journal |
| Case Index idempotency | **1 stale row** (Riley URL) | **B2 blocker** (repair-re-key not propagated) |
| coverage-ledger machine check | **PASS** — 252 captions, 151/151/151 authored verified, 0 conflicts | 151 authored + 61 brief-mention + 26 excluded + 8 folded + 2 removed + 1 unverifiable + 3 watch |
| self-tests | mint 43/43 · LINT-15/16/17 self-tests PASS | fail-closed gates green |
| manifest | 668 records (verified 421 · under_review 186 · verified_identity 49 · not_found 4 · folded 4 · off_cl 2 · fab_suspected 2; stub 59) | +3 vs S6-close = the SACO mints |

**LINT-16 Standing note:** the 1 doctrine-page LINT-16 HIGH is on `Standing to Challenge a Search.md:79`,
a Key-table cell reading "**Historical foil.**" (Jones v. United States role-label). The R7 rule flags
the token "Historical" as a leaked authority-weight label; here it is a pedagogical role-label lead-in,
not an S2 weight injection. Probable **false-positive class** (kin to the [!rule]/[!note] carve-outs);
surfaced for an orchestrator carve-out-or-rephrase call. Not caught by `run_all` (LINT-16 not in roster).

---

## Verdict

**11 of 11 §7 criteria PASS or PASS-WITH-NOTE — none FAIL on the doctrine-production obligations.**
The two FAIL-CLOSED **blockers (B1, B2) are both the single incomplete propagation of the repair-lane
Riley panel re-key** (schema enum not extended; Case Index not regenerated) — cheap to cure, but they
are committed and contradict the repair-lane close journal, so **close should not proceed until the
orchestrator adjudicates B1 (enum) + reruns B2 (index regen)**. Everything else is green or an honestly
attributed, already-registered residue (Tuggle F.4th §9 class; 6 class3 LCD-framing lines; LINT-16
Case-Index schema-3 owed to S8; the case-page slip backlog owned by S2/S9).
