# MICRO-REPAIR-REPORT — O2 EXECUTE offline micro-repair lane

**Lane:** offline micro-repair (`claude-opus-4-8`). **Date:** 2026-07-07.
**Repo:** `/Users/johngalt/Projects/cssi-quartz` · branch `overhaul2/execute` · HEAD at start `a3a4d36`.
**Constraints honored:** zero CL calls (web-only research via WebSearch/WebFetch, no courtlistener.com);
**zero** lake / manifest / content mutations; **committed nothing.** Only two code files are dirty
(`scripts/s2/ingest.py`, `scripts/s6/mint_page.py`); `git status` shows lake/content clean.

Prepared gate mutations: `_run/o2-execute/GATE-MUTATIONS-PREPARED.md` (+ inputs `davis-fold.jsonl`,
`larson-web-cites.jsonl`).

---

## 1 — Cluster-collision mint guard (F-R8-13; the W5 Davis lesson) — DONE, tests green

**Bug.** `scripts/s6/mint_page.py` collision-checked only by page stem/filename (`choose_stem` +
F-R8-12 `global_record_id_conflict`, keyed on `record_id==stem`). A stub whose `identity.cluster_id`
already belongs to ANOTHER lake record under a DIFFERENT caption (an authored page) passes both checks
and silently double-pages the same opinion.

**Fix.** New plan-time, fail-closed refusal `cluster-collision` (`REFUSE_CLUSTER_COLLISION`):
- Helper `cluster_collision(lake_root, record_id, cluster_id)` scans every OTHER lake record for a
  matching `identity.cluster_id`; excludes our own stub and our own prior promotion (roll-forward
  safety). Null/absent cluster_id never collides (off-CL Entick/Wilkes and slip-only rows legitimately
  share "no cluster") — normalized via `_cluster_key`.
- Checked in `plan_mint` fresh-path **after** F-R8-12 (so a same-stem clash still reports as the more
  specific `record-id-collision`) and after the F-R8-03 manifest gate. Refusal names the conflicting
  record_id + path and directs an A18 fold instead of a mint.

**Fixture + self-test.** In `self_test` group **CC**: a page-backed `Foreign Cluster Twin` sharing
`fixture-history`'s cluster (900004) under a different caption → asserts `cluster-collision` +
`conflicting_record_id`. Group **CC2** control: with no twin the same row mints clean (guard does not
over-fire on distinct-cluster fixtures). Also fixed a latent fixture hazard: the slip `nocite` stub
reused the slip cluster (900700) — gave it its own `cluster_id` (900701) since it is a distinct case.

**Result:** `mint_page.py --self-test` → **PASS (43/43)** (was 41/41); `--specimen-test` → PASS.

**Real-data validation (read-only dry-run, no write):** `--row united-states-v-davis--4881258` now
`REFUSED [cluster-collision]: identity.cluster_id 4881258 already belongs to lake record 'United
States v. Howard Davis' … fold the duplicate (A18 folded-alias) instead of minting [A18/F-R8-13]`.
Exactly the W5 Davis double-page, now caught pre-mint. (Fold prepared — §5 / GATE-MUTATIONS file.)

---

## 2 — long-lake `parse_circuit` bare-year bug (`scripts/s2/ingest.py`) — DONE, tests green

**Bug.** The catch-all `re.search(r"(\d+)(?:st|nd|rd|th)?", text)` matched ANY digits with the ordinal
suffix optional, so a bare year became a fake circuit: `parse_circuit("Michigan (COA 2021; Sup. Ct.
2024)") → "ca2021"` (the `long-lake-township--ucb0bfc28` stub carries `circuit="ca2021"`).

**Fix (fail-closed).** Rewrote `parse_circuit`:
- D.C./Federal matched first (so `"D.C. Cir. 2021"` never reads as `ca<year>`).
- New `_circuit_in_range(n)`: only **1–11** map to `ca<n>`; anything else → `None`.
- `"ca<digits>"`, an ordinal token (`\b(\d+)(?:st|nd|rd|th|d)\b` — includes the legal `2d`/`3d`
  abbreviations), and a bare digit token all route through `_circuit_in_range`.
- A stray year (2021) → `None` (reported upstream), never `ca2021`.

**Regression caught + fixed in-session:** the first cut dropped `2d`/`3d` (Second/Third Cir. legal
abbreviations, no st/nd/rd/th) → broke `self_test_packet_a_web_keys_landing`. Added `d` to the ordinal
suffix set; re-verified.

**Self-test.** Added cases in `self_test_binding_filters()`: the long-lake court string → `None`;
`ca2021`/`2021`/`12th Cir.` → `None`; `9`→`ca9`, `11th Cir.`→`ca11`, `9th Cir. 2021`→`ca9` (ordinal
wins), `2d Cir. en banc`→`ca2`, `3d Cir.`→`ca3`; and `binding_jurisdiction_filter(circuit="ca2021")`
→ `AND court_id:(scotus)`. **`ingest.py --self-test` → self-test passed (exit 0).**

**Lake record fix — PREPARED NOTE (not applied; lake frozen this session).** The record
`_overhaul2/lake/cases/long-lake-township-v-maxon--ucb0bfc28.json` is `status: not_found`
(`reason_code: frontier_no_candidate_cluster`) — it is not mint-eligible, so the bad `circuit` never
projects a page. When the lake thaws, set `identity.circuit: null` (the fixed `parse_circuit` now
yields `None` for its court string; `court_level` should stay `coa` only if a real circuit is later
resolved — this is a Michigan **state** case (COA 2021 / Mich. Sup. Ct. 2024), so `court_level` is
also mis-set and belongs to the S2 identity lane, not this label fix). Prepared edit:
`identity.circuit "ca2021" → null`; leave the rest for the S2 identity re-key of this not_found stub.

---

## 3 — Holcomb investigation (web-only) — RECOMMENDATION: WATCH / non-page terminal

**Question.** The wiki (Warrant Requirement) cites `United States v. Holcomb`, **132 F.4th 1118** (9th
Cir. 2025) — a computer-search particularity / general-warrant opinion. Was it withdrawn for
rehearing/en banc, superseded by a later opinion, or vacated outright?

**Finding (two independent web sources).** The panel **WITHDREW its own opinion** to revise and
re-issue it — not an en-banc grant, not an outright case vacatur:
1. **FindLaw** (9th Cir., withdrawal notice, `caselaw.findlaw.com/court/us-9th-circuit/117692617.html`):
   *"The Opinion filed March 27, 2025, and appearing at 132 F.4th 1118 (9th Cir. 2025), is withdrawn.
   It may not be cited as precedent by or to this court or any district court of the Ninth Circuit …
   The court will file a new opinion in due course."* Petition for rehearing en banc **DENIED as moot**
   because of the withdrawal, with leave to re-file once the new opinion issues.
2. **Search corroboration** (criminallegalnews.org Aug-2025; the original opinion at Justia/FindLaw
   `117103763.html`, filed 2025-03-27, still shown) + the 9th Cir. withdrawal **order dated
   2025-09-11** (consistent with the S2-builder note already in the stub's `slip_only_provenance`:
   ca9 order withdrawing 132 F.4th 1118, non-citable).

As of 2026-07 there is **no superseding published opinion** (targeted searches for a 2026 amended/new
opinion found none; docket **No. 23-469** pending re-issuance).

**Recommendation: WATCH (demote to a non-page terminal; keep the wiki's page-less brief-mention).**
- **Not** re-key to a successor: no successor opinion exists yet (nothing to key to).
- **Not** mint a page: the only opinion (132 F.4th 1118) is withdrawn + non-citable; a page would
  assert a proposition on a withdrawn, non-precedential opinion (banned).
- **Not** remove/exclude: the case is live and the panel says a new opinion is coming — removal is
  premature.
- The wiki already treats Holcomb page-less (S6 roster: out-of-remit persuasive → brief-mention), so
  a WATCH terminal is a no-op for the reader.
- **Watch pointer for the S6 R11 terminal:** docket **9th Cir. No. 23-469**; the withdrawn opinion is
  CL cluster **10365516** (per `PRE-W5-AUDIT-REPORT.md:21`), NOT the current stub key **10670143**
  (which is the withdrawal ORDER). When the new opinion issues, re-key to the successor cluster + cite
  and re-evaluate for a page. (Aside, not this lane's fix: the stub's `official_selection.court_class`
  is erroneously `"state"` for a 9th-Cir. coa case — flag to the S2 identity lane.)

---

## 4 — Larson official-cite tiebreak (web-only) — determination + prepared enrich instruction

**Row.** `state-v-larson--1187724` = **State v. Larson, 159 Or. App. 34, 977 P.2d 1175 (1999)** (Or.
Ct. App., curtilage / apartment-common-area privacy; CA A96052; filed **1999-03-17**; appeal from
Multnomah County — matches the stub's `case_name_full`, `date_decided`, and trial docket). Identity is
**correct** (the PRE-W5 re-key was right). Enrichment produced `official_selection.reason =
"same_rank_tie"`, `display = null`.

**Root cause (traced through the corpus precedence).** For state courts,
`ingest.py::citation_rank` maps every CL-**type-2** cite to `reporter_classes.official = 1`
(`_reporter-precedence.json`). The cluster carries THREE cites: `159 Or. App. 34` (type 2 → rank 1),
`977 P.2d 1175` (type 3, regional → rank 2), and `1999 Ore. App. LEXIS 384` (a **LEXIS database** cite
CL also tags type 2 → rank 1). Two rank-1 cites with different text ⇒ `same_rank_tie` ⇒ no official
selected. The tie is **spurious** — the LEXIS cite is a vendor/database locator, not an official
reporter.

**Official-selection precedence for Oregon (answer to "Oregon official reports vs P.2d").** Oregon's
**official** reporter is the Oregon Reports, Court of Appeals — **Or. App.** (Bluebook T1; corpus
maps type-2 state-official → rank 1). **P.2d** (Pacific Reporter) is the West **regional** reporter,
rank 2. So **official = 159 Or. App. 34**; **parallel = 977 P.2d 1175**.

**Two independent sources (both lead with the Or. App. official form):**
1. **Justia** — `law.justia.com/cases/oregon/court-of-appeals/1998/a96052.html`: *"State v. Larson,
   159 Or App 34, 977 P2d 1175 (1999)."*
2. **Oregon Legislature official annotations** — `oregonlegislature.gov/bills_laws/ors/anc001.html`:
   cites *"State v. Larson, 159 Or App 34, 977 P2d 1175 (1999)"* (the State's own annotation leads
   with `159 Or App 34`, parallel `977 P2d 1175`) — best evidence that Or. App. is the official cite.

**Prepared instruction (NOT a lake write) — `_run/o2-execute/larson-web-cites.jsonl`:**
- **PREFERRED (S2-builder remit; preserves the P.2d parallel, auto-derived):** add the LEXIS/Westlaw
  vendor-database reporters (e.g. `"Ore. App. LEXIS"`, and the LEXIS/WL family generally) to
  `OFFICIAL_SELECTION_NOISE_REPORTERS` in `ingest.py` so the database cite never competes, then re-run
  `--enrich-citations` on `state-v-larson--1187724`. Result: `select_official_cite` returns the sole
  rank-1 cite `159 Or. App. 34`, `parallel = [977 P.2d 1175]`, `display = "159 Or. App. 34"`. This is
  a code change (flagged, not executed — the noise-reporter list is the S2 builder's signed surface).
- **ALTERNATIVE (no code change; drops the parallel):** `--apply-web-cites` with the prepared JSONL
  line (`cite: "159 Or. App. 34"`, `court_class: "state"`, `volume/reporter/page` split). Leg 1
  (Justia) is a confirmed approved source; **leg 2 needs a second APPROVED-source URL** (Google
  Scholar / Casemine / Fastcase — the Oregon Legislature source verifies the fact but is not in the
  tool's `WEB_CITE_LEG_SOURCES` allowlist). The tool fail-closes until a real, agreeing second leg is
  attached. This yields `display = "159 Or. App. 34"` but `parallel = []`.

---

## 5 — Prepared Davis fold + Reddick label — see GATE-MUTATIONS-PREPARED.md

Written to `_run/o2-execute/GATE-MUTATIONS-PREPARED.md` (exact precondition → apply → verify commands):

- **(a) Davis fold** — `united-states-v-davis--4881258` → **folded-alias** into `United States v.
  Howard Davis` (shared cluster 4881258; the double-page the F-R8-13 guard catches). Applied via the
  canonical `--apply-alias-folds _run/o2-execute/davis-fold.jsonl` (A18 folded-alias precedent; record
  kept-not-deleted, manifest gets `folded_into` + `fold_provenance`, journal gets the dedupe-pointer).
- **(b) Reddick label** — `united-states-v-reddick--4527853` circuit **ca5 → ca3** (+ court `5th Cir.`
  → `3d Cir.`) in both the lake record and the manifest. Identity otherwise clean; audit authority
  `PRE-W5-AUDIT-REPORT.md:81` (*"900 F.3d 636 = 3d Cir. Reddick private-search … should be ca3.
  Court-repair, not a re-key."*). Prepared as a fail-closed deterministic edit (cluster 4527853 is not
  cached, so `--repair-coa-state-from-cache` would queue-for-lane and is not usable offline).

---

## Test/verification summary

| Check | Result |
|---|---|
| `scripts/s6/mint_page.py --self-test` | **PASS 43/43** (was 41/41; +CC cluster-collision, +CC2 control) |
| `scripts/s6/mint_page.py --specimen-test` | **PASS** |
| `scripts/s2/ingest.py --self-test` | **PASS** (exit 0; +7 parse_circuit assertions) |
| real davis dry-run (read-only) | `REFUSED [cluster-collision]` → Howard Davis (cluster 4881258) |
| `parse_circuit("Michigan (COA 2021; Sup. Ct. 2024)")` | `None` (was `ca2021`) |
| `git status` | only `scripts/s2/ingest.py`, `scripts/s6/mint_page.py` dirty; lake/content clean; nothing committed |

## Files
- Code: `scripts/s6/mint_page.py` (F-R8-13 guard + fixtures/tests), `scripts/s2/ingest.py`
  (`parse_circuit` + tests).
- Prepared artifacts: `_run/o2-execute/GATE-MUTATIONS-PREPARED.md`,
  `_run/o2-execute/davis-fold.jsonl`, `_run/o2-execute/larson-web-cites.jsonl`.
