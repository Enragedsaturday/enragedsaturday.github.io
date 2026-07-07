# PACKET A — re-key + alias-fold execution report (2026-07-06 session)

**Lane:** S2 BUILDER (`{lane: s2-builder, model: claude-opus-4-8}`).
**Substitution note:** the usual Codex builder was unavailable this session; this work was
executed by the substitute builder (Claude Opus 4.8). Same discipline held: every new code
surface ships with self-tests, the full `--self-test` suite was run green before any live-lake
write, and the diff is returned for the orchestrator's gate review (writer ≠ checker — no
self-certification).

Repo: `/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`, start HEAD `80d11a8`.
Nothing committed (orchestrator commits at the gate). No `content/` writes.

---

## 1. Roster enumerated from the manifest (ground truth, not prose)

`_overhaul2/lake/_manifest.json` at HEAD: **25** rows `status: fabrication_suspected`. The
re-key universe = 25 − 2 orchestrator-lane removals (`united-states-v-west--10653830`,
`united-states-v-white--10349533`, untouched) = **23 rows**.

Cross-referenced against the dual webverify legs (`s6-webverify-codex.jsonl` primary for keys;
`s6-webverify-claude.jsonl` + `-batches.jsonl` cross-check). Every one of the 23 had a
webverify match — none escalated for "no webverify match."

The 23 split (reconciling Group-1 "21 re-keys" + Group-2 "3 folds" over 23 rows — the
`carroll-v-carman` row is counted in **both** groups: it is re-keyed to the SCOTUS survivor
*and* is the fold-target of `carman-v-carroll`):

- **21 readjudicated** (Step 2): the 19 named Group-1 rows + `state-v-christensen` (unnamed
  "+2 convergent-REAL") + `carroll-v-carman` (SCOTUS re-key survivor).
- **2 folded away** (Step 3, not readjudicated): `morse-v-french--6536632`,
  `united-states-v-chatrie--10881683`.
- Plus `carman-v-carroll--8693292` (an existing `verified_identity` 3d-Cir. row, **not** a
  fabrication_suspected row) folds into the re-keyed `carroll-v-carman`.

---

## 2. Code surface added to `scripts/s2/ingest.py` (offline, self-tested, fixtured)

Two bounded offline flags (no CL calls; both early-return before `read_token`; both refuse to
combine with live/readjudicate/other-action flags):

1. **`--apply-web-keys <jsonl>`** — lands recovered dual-leg search keys onto the named roster
   rows. **Guard:** refuses any row whose `status != fabrication_suspected`; refuses unknown
   record_ids. Sets `expected_citation`/`citation`, `docket`, `year`, `date_decided`, and
   derives `court`/`court_level`/`circuit`/`state` from the web court string via a bounded
   normalizer (SCOTUS markers → scotus; reused `s6_candidate_court_fields` for COA circuits;
   compact state-token map for state courts). Journals per row
   `packet-a.web-keys {before, after, provenance, adjudicated_by, lane, model}`.
2. **`--apply-alias-folds <jsonl>`** — retires caption-duplicate stubs into a surviving
   litigation row. **Guards:** folding record must be a stub (`--` id) with status
   `fabrication_suspected` or `verified_identity`; survivor must exist and not itself be folded;
   no self-fold. Sets manifest row + case-record status → **`folded-alias`**, writes
   `folded_into` + `fold_provenance` on the manifest row, appends a `folded-alias` warning to
   the case record. Journals the `s6-dedupe-pointer` precedent shape
   (`{action, step: dedupe, status: pointer, passed_over_record_id, selected_record_id,
   controlling_case, lane, model}`) + a `packet-a.alias-fold` audit row.

**Schema:** `folded-alias` added to the two `status` enums in `_overhaul2/lake/_schema.json`
(top-level + the stub-conditional `if/then`). This is a spec-adjacent lake change (mirrors the
verified_off_cl / A17 extension pattern this build) — **flagged for orchestrator ratification.**
Schema-validity is proven by (a) the new ingest self-test asserting `folded-alias` is in the
live enum, and (b) the full **LINT-13** run passing with 3 real `folded-alias` records present.

**Self-tests added + registered:** `self_test_packet_a_web_keys_landing` (scotus/coa/state key
landing, court-field derivation, journal shape, + guards for non-fab and unknown ids) and
`self_test_packet_a_alias_fold` (fold of a fab stub and a verified_identity stub, case+manifest
status, pointer journal, live-schema enum assertion, + guards for self-fold and non-stub page).
**`python3 scripts/s2/ingest.py --self-test` → `self-test passed`** (full suite green,
pre-live).

Keys JSONL assembled at `_run/o2-execute/packet-a-web-keys.jsonl` (codex primary; filled from
the Claude leg where codex was silent — not a disagreement). Only one cross-leg divergence
surfaced and it was reconcilable, not an escalation (see §6). Folds spec at
`_run/o2-execute/packet-a-alias-folds.jsonl`.

---

## 3. Step 2 — readjudication through the serial CL lane (21 rows)

Invocation: `python3 scripts/s2/ingest.py --readjudicate-file _run/o2-execute/packet-a-readjudicate.txt --session-minutes 90`.
Single serial lane, default 14/min token bucket. **All 21 reset cleanly; live run exit 0.**

| # | old record_id | keys applied (cite · docket · court) | new record_id | cluster | terminal | calls |
|---|---|---|---|---|---|---|
| 1 | `arkansas-v-sanders--10601315` | 442 U.S. 753 · 77-1497 · U.S. | `arkansas-v-sanders--110119` | 110119 | verified_identity | 2 |
| 2 | `carroll-v-carman--8693292` | 574 U.S. 13 · 14-212 · U.S. | `carroll-v-carman--2750102` | 2750102 | verified_identity | 7 |
| 3 | `district-of-columbia-v-heller--3180743` | 554 U.S. 570 · 07-290 · U.S. | `district-of-columbia-v-heller--145777` | 145777 | verified_identity | 2 |
| 4 | `laduke-v-nelson--571489` | 762 F.2d 1318 · 83-3608 · 9th Cir. | `laduke-v-nelson--452994` | 452994 | verified_identity | 2 |
| 5 | `martin-v-united-states--10636952` | 605 U.S. 395 (2025) · 24-362 · U.S. | `martin-v-united-states--10776839` | 10776839 | verified_identity | 3 |
| 6 | `milam-v-united-states--10654082` | 296 F. 629 · — · 4th Cir. | `milam-v-united-states--8849836` | 8849836 | verified_identity | 2 |
| 7 | `robinson-v-commonwealth--10638592` | — · 1912-24-1 · Va. Ct. App. | `robinson-v-commonwealth--10793178` | 10793178 | **fabrication_suspected** | 6 |
| 8 | `state-v-christensen--10657325` | 517 S.W.3d 60 · W2014-00931-SC-R11-CD · Tenn. | `state-v-christensen--4381703` | 4381703 | verified_identity | 2 |
| 9 | `state-v-weaver--10675098` | 349 S.W.3d 521 · PD-1635-10 · Tex. Crim. App. | `state-v-weaver--2546485` | 2546485 | verified_identity | 2 |
| 10 | `trupiano-v-united-states--658600` | 334 U.S. 699 · 427 · U.S. | `trupiano-v-united-states--104576` | 104576 | verified_identity | 2 |
| 11 | `united-states-v-amos--10686575` | 88 F.4th 446 · 20-3298 · 3d Cir. | `united-states-v-amos--9452158` | 9452158 | verified_identity | 2 |
| 12 | `united-states-v-berkowitz--4520474` | 927 F.2d 1376 · — · 7th Cir. | `united-states-v-berkowitz--557342` | 557342 | verified_identity | 2 |
| 13 | `united-states-v-daniels--10534900` | 101 F.4th 770 · 22-1378 · 10th Cir. | `united-states-v-daniels--9500360` | 9500360 | verified_identity | 2 |
| 14 | `united-states-v-ganias--8429176` | 824 F.3d 199 · 12-240-cr · 2d Cir. en banc | `united-states-v-ganias--3207604` | 3207604 | verified_identity | 2 |
| 15 | `united-states-v-liddell--9232233` | 517 F.3d 1007 · 07-1337 · 8th Cir. | `united-states-v-liddell--1461978` | 1461978 | verified_identity | 2 |
| 16 | `united-states-v-mendez--10374557` | 103 F.4th 1303 · 23-1460 · 7th Cir. | `united-states-v-mendez--9524074` | 9524074 | verified_identity | 2 |
| 17 | `united-states-v-meyer--10292544` | — · 20-2958 · 8th Cir. | `united-states-v-meyer--5302394` | 5302394 | verified_identity | 2 |
| 18 | `united-states-v-perez--10661791` | 89 F.4th 247 · 22-1121 · 1st Cir. | `united-states-v-perez--9456060` | 9456060 | verified_identity | 2 |
| 19 | `united-states-v-reddick--9364250` | 900 F.3d 636 · 17-41116 · 5th Cir. | `united-states-v-reddick--4527853` | 4527853 | verified_identity | 2 |
| 20 | `united-states-v-verdugo-urquidez--9151048` | 494 U.S. 259 · 88-1353 · U.S. | `united-states-v-verdugo-urquidez--112382` | 112382 | verified_identity | 2 |
| 21 | `wyman-v-james--3121332` | 400 U.S. 309 · 69 · U.S. | `wyman-v-james--108223` | 108223 | verified_identity | 2 |

**Outcome: 20 verified_identity, 1 fabrication_suspected (robinson — escalated, §6).** Every
one of the 21 stubs re-keyed to a **corrected cluster** (all 21 record_ids changed suffix — the
original S6-seed clusters were wrong/unconfirmed thin seeds). Canonical caption + expected-cite
confirmed on all 20 verified rows (spot-checked; e.g. `daniels` → the 10th Cir. 2024 Daniels,
*not* the 5th Cir. Bruen Daniels; `milam` → the 1924 4th Cir. Milam, not the 1974 9th Cir.).

### Special row — `arkansas-v-sanders` (wrong-case re-key, F-S2-33 Timbs path)
The reset wiped the wrong-cluster identity (2024 Gov.-Sanders prison-board suit, cluster
10601315); with the corrected keys the ladder landed the **real** *Arkansas v. Sanders*,
442 U.S. 753 (1979), docket 77-1497 → cluster **110119**, `verified_identity`. Record_id
renamed `--10601315` → `--110119` automatically by the live run (same rename+journal path as
the Timbs `--4673515` → `--4591916` correction). Old shell removed (§5).

### Watch-list framing notes carried into the journal (no page work here — for S7)
- `trupiano` = **dead law** (overruled by *Rabinowitz*) — history framing.
- `state-v-weaver` = REAL but holding is **scope-of-consent**; the commercial-REP point is
  supporting reasoning (S7 prose note).
- `milam-v-united-states` = the **1924 4th Cir.** case (296 F. 629) — conflation hazard vs the
  1974 9th Cir. Milam; landed cluster 8849836, canonical "Milam v. United States".
- `united-states-v-daniels` = **10th Cir. 2024** (101 F.4th 770), NOT the 5th Cir. Bruen
  Daniels — confirmed by landed canonical + cite.

---

## 4. Step 3 — alias-folds (Group 2; ledger/lake only, no content/ writes)

`python3 scripts/s2/ingest.py --apply-alias-folds _run/o2-execute/packet-a-alias-folds.jsonl` →
**3 folds applied.** Each: manifest + case-record status → `folded-alias`, `folded_into`
pointer + `fold_provenance` on the manifest row, `s6-dedupe-pointer` journal row (precedent
shape) + `packet-a.alias-fold` audit row.

| folded stub (terminal `folded-alias`) | folded_into (survivor) | survivor status | rationale |
|---|---|---|---|
| `morse-v-french--6536632` | `French v. Merrill` (page row) | verified | *Morse v. French* = cert-denial sub nom of *French v. Merrill*, 15 F.4th 116 (1st Cir. 2021), cert. denied 143 S. Ct. 301 (2022). Morse caption survives as cert-posture reference at mention sites (S7 concern). |
| `united-states-v-chatrie--10881683` | `Chatrie v. United States` (page row) | under_review | Stub's cluster 10881683 = the SCOTUS merits already tracked by the page row; 4th-Cir. en banc below (136 F.4th 100 (2025)) enters as Lower-court developments at authoring. |
| `carman-v-carroll--8693292` | `carroll-v-carman--2750102` (re-keyed SCOTUS survivor) | verified_identity | SCOTUS per curiam *Carroll v. Carman*, 574 U.S. 13 (2014) is the page candidate; the 3d-Cir. caption (588 F. App'x 183 / 749 F.3d 192) alias-folds into it. Fold ran after Step 2 renamed carroll-v-carman to `--2750102`. |

---

## 5. Orphan-shell cleanup (F-S2-33 precedent)

All 21 re-keys renamed their record_id, leaving 21 empty `status: pending` reset shells at the
old ids (these would **fail LINT-13** — `pending` is not in the schema enum). Removed all 21 +
journaled one `s6-queue-correction / "removed re-key orphan files"` row (mirrors the
$8,850/Von Neumann precedent), `files_removed` listing all 21, `lane/model` = mine. Case-file ↔
manifest bijection restored: **662 case files = 662 manifest records.**

Incidental side effect of the resume-driven full-manifest pass: 5 page records
(`Case v. Montana`, `Chatrie v. United States`, `People v. Hughes`, `State v. Volle`,
`United States v. Morton`) were re-completed idempotently (timestamp-only touches). Because
re-projection to `content/` is out of bounds, these were reverted to HEAD (`git checkout HEAD`)
— zero content loss, and **LINT-12 drift cleared**.

---

## 6. Escalations

**One escalation: `robinson-v-commonwealth` (row 7).** Landed
`robinson-v-commonwealth--10793178`, **fabrication_suspected**.

- This is **not a fabrication.** The applied docket **1912-24-1** is an **exact match** to CL
  cluster 10793178, whose canonical caption is *"Commonwealth v. Robinson"* — **same docket,
  same court (Va. Ct. App.), same date (2026-04-07)** as our keys. It is unambiguously the same
  case with the **party order swapped** (criminal-appeal caption flip: our text cites
  "Robinson v. Commonwealth").
- It fail-closed to fabrication_suspected only because: (a) `canonical_name_match = False` on
  the party-order swap, and (b) no reporter cite to confirm (a not-yet-reported 2026 decision;
  `expected_citation` correctly left null), and (c) the ladder selected the cluster on the
  `case_name` rung, so `strong_key_match` was not set — even though the **docket rung would
  confirm the identical cluster**. Had it landed via the docket rung it would read
  `verified_identity` (the established `caption_mismatch_accepted_by_docket_number` class).
- **Recommendation (orchestrator gate call):** ratify as `verified_identity`
  (docket-confirmed, swapped-caption class) — a one-line adjudication that brings
  fabrication_suspected to the target **2**. Alternatively an F-S2-34-class ladder fix (confirm
  identity when the selected cluster's `docket_number` equals the roster docket key regardless
  of winning rung). Not self-certified here (writer ≠ checker).

**Leg-divergence (reconciled, not escalated): `martin-v-united-states`.** Codex gave the
placeholder `605 U.S. ___ (2025)`; the Claude/batches leg + the s6-fabrications packet gave the
paginated `605 U.S. 395 (2025)`. Same volume/reporter/year, same docket 24-362 — codex was
page-incomplete, not contradictory. Applied `605 U.S. 395 (2025)`; landed cluster 10776839,
`verified_identity`. No other cross-leg key disagreement in the 21.

---

## 7. CL calls + pacing

- **This session: 52 CL calls** (`calls this session: 52`, exit 0). Per-row: 2 for a clean
  citation/caption landing; 3–7 for the docket-rung / multi-rung cases (carroll-v-carman 7,
  robinson 6, martin 3). Sum of per-row `cl_calls` = 52 (matches).
- **Zero 429s. Zero transport stops.** Paced at the default 14/min single serial lane; the
  ~600 already-complete records were resume-skipped (0 calls, cache-served). No tier-probe
  regression to the old 5/min tier was observed; `--session-minutes 90` never came near expiry.
- Prior cumulative baseline was 17,441 CL calls (per commit `d134883`); **new cumulative
  ≈ 17,493.**

---

## 8. Final manifest distribution

| status | before (HEAD) | after |
|---|---|---|
| verified | 421 | 421 |
| verified_identity | 175 | **194** (+20 re-keys − 1 carman-v-carroll fold) |
| under_review | 35 | 35 |
| verified_off_cl | 2 | 2 |
| not_found | 4 | 4 |
| **fabrication_suspected** | **25** | **3** |
| **folded-alias** (new) | 0 | **3** |
| **total records** | 662 | 662 |

**`fabrication_suspected` = 3:** `robinson-v-commonwealth--10793178` (escalation, §6) +
`united-states-v-west--10653830` + `united-states-v-white--10349533` (the packet-A removal set,
orchestrator lane). **Target of exactly 2 (West + White) is met on all 23 rows except robinson**
— which is a docket-confirmed swapped-caption identity awaiting a one-line ratification, not a
real fabrication. On ratification, fabrication_suspected → 2.

`folded-alias` = 3: `morse-v-french--6536632`, `united-states-v-chatrie--10881683`,
`carman-v-carroll--8693292`.

---

## 9. Gates run (green) + working-set scope

- `scripts/s2/ingest.py --self-test` → **passed** (incl. 2 new packet-A self-tests), run before
  any live-lake write.
- **LINT-13** (schema + bijection) 0 violations; **LINT-6 / LINT-12 / LINT-14 / LINT-26**
  0 violations. lint13 `--self-test` PASS.
- **LINT-1 crashes on a pre-existing content/ frontmatter condition** (`opinion_id: null` in a
  content page never touched here) — out of scope, not a regression from this session.
- Working set (all within `scripts/s2/ingest.py` · the lake · the journal · `_run/o2-execute/`):
  `M scripts/s2/ingest.py`, `M _overhaul2/lake/_schema.json`, `M _overhaul2/lake/_manifest.json`,
  21×`D` orphan shells, 21×`??` re-keyed case records, 3×`M` fold case records, 4 new
  `_run/o2-execute/` artifacts. **No `content/` writes. Nothing committed.**

### Artifacts
- `scripts/s2/ingest.py` (new `--apply-web-keys`, `--apply-alias-folds`, 2 self-tests)
- `_overhaul2/lake/_schema.json` (`folded-alias` enum — flagged for ratification)
- `_run/o2-execute/packet-a-web-keys.jsonl`, `_run/o2-execute/packet-a-alias-folds.jsonl`,
  `_run/o2-execute/packet-a-readjudicate.txt`, `_run/o2-execute/packet-a-readjudicate.log`
- Journal: `/Users/johngalt/cssi-lake/journal/s2-ingest-s2-build-96d841cbb12e.jsonl`
  (21 `packet-a.web-keys`, 3 `packet-a.alias-fold`, 3 `s6-dedupe-pointer`, 1 orphan-removal —
  all carry `{lane: s2-builder, model: claude-opus-4-8}`).
