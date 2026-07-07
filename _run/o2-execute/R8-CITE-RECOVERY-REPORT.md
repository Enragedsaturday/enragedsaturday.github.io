# R8 cite/identity recovery report (2026-07-07)

Lane/model: `{lane: s2-builder, model: claude-opus-4-8}`. Branch `overhaul2/execute`, from HEAD
`da8adb3`. **Committed nothing.** Work order: `R8-CITE-RECOVERY-WORKORDER.md`; authority
`R8-CITATIONS-ADJUDICATION.md`. Session constraint: **ZERO live CourtListener calls** (serial CL
lane owned by parallel W1). All CL-touching work delivered ready-to-run; all executed work was
web/offline or cache-served (0 network I/O, 0×429).

## Scope ground-truth
48 blocked rows partitioned R1(14)/R2(6)/R3(28). Investigation moved **carroll-v-carman** from
R1→R3 (it is the RIGHT per-curiam cluster missing only its `U.S.` cite, not a mis-key). Net:
**R1 = 13 re-keys, R2 = 6, R3 = 28 + carroll = 29.** Plus coordinator addendum: egbert +
CR-03/CR-15.

## Outcome summary (48 blocked)
| lane | n | outcome | mintable now |
|---|--:|---|--:|
| R1 re-keys | 13 | web-verified, JSONL **READY-PENDING-LANE-GRANT** (not applied) | 0 (pending) |
| R2 serializer-policy | 6 | enriched cache-served; cites landed | **6** |
| R3 web-dual-leg recovered | 10 | citations written (source `web-dual-leg` + 2 legs) | **10** |
| R3 slip-only | 15 | journaled `slip-only`, display empty (deferred mint handling) | 0 |
| R3 escalated | 4 | ambiguous/party-mismatch — write nothing, escalate | 0 |
**New mintable this session (excl. pending R1): 16 of 148.** Plus egbert (+1, separate scope).

---

## R1 — identity re-keys (13) — READY-PENDING-LANE-GRANT
Deliverables (do NOT touch the CL lane until granted):
- `_run/o2-execute/R8-R1-web-keys.jsonl` (13 rows; each dual-leg web-verified: caption, official
  cite, docket, court, date).
- `_run/o2-execute/R8-R1-readjudicate-ids.txt` (13 ids).
- Apply sequence under the lane grant (≤14/min, resumable):
  `--apply-web-keys R8-R1-web-keys.jsonl --web-keys-allow-verified-identity`
  then `--readjudicate-file R8-R1-readjudicate-ids.txt`.

Read-only readiness check: 13/13 resolve to `verified_identity`, court derivations correct
(scotus×11, coa/ca5 alvarez, coa/ca10 maez). All investigations confirmed genuine wrong-cluster
mis-keys (orders/cert/rehearing/companion/military/state), NOT cite gaps.

| record_id | verified merits cite | docket | date | was mis-keyed to | legs |
|---|---|---|---|---|---|
| austin-v-united-states--9140366 | 509 U.S. 602 | 92-6073 | 1993-06-28 | 510 U.S. 904 cert-grant | Cornell LII + Oyez |
| bennis-v-michigan--9159725 | 516 U.S. 442 | 94-8729 | 1996-03-04 | 517 U.S. 1163 rehearing | Cornell LII + Oyez |
| board-of-county-…-bryan-county-v-brown--9167020 | 520 U.S. 397 | 95-1100 | 1997-04-28 | 520 U.S. 1283 rehearing | Cornell LII + Oyez |
| scott-v-united-states--9020551 | 436 U.S. 128 | 76-6767 | 1978-05-15 | 439 U.S. 1046 cert-denial | Cornell LII + Oyez |
| united-states-v-giordano--109022 | 416 U.S. 505 | 72-1057 | 1974-05-13 | 416 U.S. 580 (Chavez companion) | Cornell LII + Oyez |
| g-m-leasing-corp-v-united-states--9017014 | 429 U.S. 338 | 75-235 | 1977-01-12 | 435 U.S. 923 rehearing | Cornell LII + Oyez |
| quantity-of-copies-of-books-v-kansas--107502 | 378 U.S. 205 | 449 | 1964-06-22 | 388 U.S. 452 (1967 per curiam) | Cornell LII + Oyez |
| alvarez-v-city-of-brownsville--9361139 | 904 F.3d 382 (5th Cir. en banc) | 16-40772 | 2018-09-18 | 139 S. Ct. 2690 cert-denial | FindLaw + Studicata |
| united-states-v-maez--7355106 | 872 F.2d 1444 (10th Cir.) | 88-1128 | 1989-04-19 | 76 M.J. 354 CAAF (wrong court) | Google Scholar + vLex |
| owen-v-city-of-independence--8922609 | 445 U.S. 622 | 78-1779 | 1980-04-16 | 623 F.2d 550 (8th Cir. remand) | Cornell LII + Oyez |
| united-states-v-donovan--347744 | 429 U.S. 413 | 75-212 | 1977-01-18 | 559 F.2d 1201 (6th Cir.) | Cornell LII + Oyez |
| frank-v-maryland--793662 | 359 U.S. 360 | 278 | 1959-05-04 | 441 F.3d 197 (unrelated 2006 4th Cir.) | Cornell LII + FindLaw |
| robbins-v-california--2262192 | 453 U.S. 420 | 80-148 | 1981-07-01 | Cal. state (Robbins v. Regents) | Cornell LII + FindLaw |

Note: giordano docket corrected to 72-1057; frank docket corrected 275→278; alvarez date corrected
to 2018-09-18; maez date 1989-04-19, docket 88-1128 — all by both legs. Every leg independent, no
Wikipedia, no CourtListener.

## R2 — serializer noise-reporter amendment (6) — DONE, MINTABLE
Signed serializer (`scripts/s2/ingest.py` `select_official_cite`) amended: a named
`OFFICIAL_SELECTION_NOISE_REPORTERS = {"Fla. L. Weekly Fed. S", "FED App."}` — these type-1
specialty reporters never compete for official selection (before, they hard-failed
`unlisted_reporter` before the real cite could rank). Everything else unchanged; still
fail-closes `same_rank_tie`/`unlisted_reporter` off the named list. Fixtured in
`self_test_precedence` (each named reporter + a not-on-list control + noise-only fail-closed).

`--enrich-citations` re-run over the 6 (cache-served, `--max-calls 0 --no-resume`): **enriched
6/6, cache-hits 6, network 0, CL calls 0.** All cites match the work-order expectations exactly
(source honestly `cluster.citations[]` — these were always cluster cites, just unblocked):

| row | cite |
|---|---|
| county-of-los-angeles-v-mendez--4395246 | 581 U.S. 420 |
| grady-v-north-carolina--2789928 | 575 U.S. 306 |
| manuel-v-city-of-joliet--4376986 | 580 U.S. 357 |
| united-states-v-james-daniel-good-real-property--112914 | 510 U.S. 43 |
| ziglar-v-abbasi--4403804 | 582 U.S. 120 |
| northrup-v-city-of-toledo-police-dept--2800431 | 785 F.3d 1128 |

## R3 — dual-leg web-cite recovery (28 + carroll = 29)
Schema + LINT-13 extended (mirrors the A17/A18 off_cl_links pattern): new `definitions.web_leg`
(source enum of approved publishers — **Wikipedia deliberately excluded**), `citations.web_legs`
array (`minItems:2`), and a conditional — **if any `all[]` entry has source `web-dual-leg`, then
`web_legs` is REQUIRED** — so a web-recovered cite can never masquerade as `cluster.citations[]`.
3 new fixtures (`webcite-pass`, `webcite-missing-legs-fail`, `webleg-wikipedia-fail`); lint13
self-test PASS, live keyword coverage OK, `citation.source` left an open string (a hard enum broke
existing fixtures). New offline surface `--apply-web-cites` (Phase-1 fail-closed: rejects <2 legs,
same-source legs, Wikipedia/unapproved sources, leg-cite disagreement, already-bearing rows,
out-of-scope status; self-tested).

### R3 recovered (10) — DONE, MINTABLE (each 2 independent cite-stating legs)
| record_id | cite | court_class | legs |
|---|---|---|---|
| carroll-v-carman--2750102 | 574 U.S. 13 | scotus | Google Scholar + Oyez |
| alasaad-v-wolf--4855246 | 988 F.3d 8 | coa | Google Scholar + vLex |
| united-states-v-kolsuz--4499413 | 890 F.3d 133 | coa | Google Scholar + FindLaw |
| united-states-v-moore-bush--6476396 | 36 F.4th 320 | coa | Google Scholar + vLex |
| united-states-v-wilson--10664712 | 13 F.4th 961 | coa | Google Scholar + Justia |
| united-states-v-cole--9623101 | 21 F.4th 421 | coa | Google Scholar + Justia |
| united-states-v-loines--9357144 | 56 F.4th 1099 | coa | Google Scholar + vLex |
| united-states-v-lyle--8435375 | 919 F.3d 716 | coa | Google Scholar + Justia |
| jimerson-v-lewis--9475670 | 94 F.4th 423 | coa | Justia + FindLaw |
| united-states-v-small--10593041 | 944 F.3d 490 | coa | Justia + vLex |
All 10 written with `source: web-dual-leg` + 2-leg trail; LINT-13 schema conformance verified
(0 violations); status untouched (`verified_identity`).

### R3 slip-only (15) — journaled, display empty, deferred to orchestrator mint decision
mendoza, carter, robinson, larson, davis, holcomb, hunt, ruiz, lee, zorn,
district-of-columbia-v-r-w, landor, olivier, konan, geo-group. Each has a two-source slip/docket
evidence trail in the journal (step `r8.web-cites`, status `slip-only`). Premise/court/date fixes
captured in the journal notes:
- **mendoza** — NOT "3d Cir. 2024"; actual 3d Cir. slip filed 2026-01-08, No. 25-1154.
- **davis** — 8th Cir. (not 4th), No. 23-2978, 2025-09-11.
- **ruiz** — CAAF (not a numbered circuit), No. 24-0158/MC; evidentiary appeal, not 4th Am.
- **zorn** — SCOTUS per curiam (not coa), No. 25-297, 607 U.S. ___.
- **robinson** — Va. Ct. App. published, issued 2026-04-07 (not Feb).
- **holcomb** — original 132 F.4th 1118 was WITHDRAWN 2025-09-11 and marked non-citable; no live cite.
- Hallucinated cites rejected by the two-source rule: `341 A.3d 1067` (carter), `56 F.4th` (hunt),
  `85 M.J. 203` (ruiz), `146 S. Ct. 916/926` (olivier/zorn).

### R3 escalated (4) — write nothing, needs orchestrator identity adjudication
- **united-states-v-young--10687648** — only pin-able 10th Cir. 2020 "Young" is a 5th-Am confession
  case, not 4th-Am; other 4th-Am Youngs are 2023. Ambiguous.
- **united-states-v-williams--10670874** — 9th Cir. "Williams" too common; candidate (419 F.3d 1029)
  is 2005 not 2006. Ambiguous.
- **united-states-v-lewis--10640348** — only findable 6th Cir. 2023 Lewis is *Edward Leonidas* Lewis,
  not *Raymond* Lewis (party mismatch). **Identity may itself be mis-keyed.**
- **united-states-v-black--10355347** — 707 F.3d 531 (4th Cir. 2013) is *Nathaniel* Black; *Eural*
  Black is a 7th Cir. compassionate-release case (No. 24-1191), not a 4th-Am search. **Identity
  likely mis-keyed** — the verified cluster probably points at the wrong case.

---

## Coordinator addendum (2026-07-07)
**CR-03 (`scripts/s2/ingest.py` `parse_circuit`):** DONE. Added CourtListener slugs `cadc`/`cafc`
(were dropping to None). Self-test in `self_test_binding_filters` (slugs + `binding_jurisdiction_filter`).

**CR-15 (empty dict serializes to bare `key:` → reparses null):** DONE, both sides mirrored to the
empty-list case: `scripts/s2/serializer.py` `dumps_frontmatter_body` now emits `key: {}`, and
`scripts/lint/_common.py` `_scalar` now parses `{}` → real empty dict (the parser already handled
`[]`→`[]`; the emit-only fix would have left residual `{}`-string-vs-dict drift). New
`serializer.py --self-test` proves dump→parse→`diff_paths` == [] end-to-end.

**egbert-v-boule--6475794 identity repair:** DONE cache-served. New bounded, journaled surface
`--repair-identity-from-cache` (client forced `max_calls=0` → cache-only; a miss journals
`queued-for-lane`, never touches the CL lane). Re-derived from the cached cluster (596 U.S. 482,
date_filed 2022-06-08): `court_level scotus`, `court "U.S. Supreme Court"`, `court_id scotus`,
`year 2022`, `date_decided 2022-06-08`. `authority_weight` now **"Binding — SCOTUS"** (false
"Historical" cleared); cite 596 U.S. 482 already present → **mintable in W9 tail.** Journal step
`r8.identity-repair` status `repaired`. (Docket 21-147 available from web if the orchestrator wants
to complete it via the lane-grant readjudicate; not blocking.)

---

## Findings surfaced (not fixed — writer≠checker / other lanes)
1. **HIGH / gate-blocking — 14 minted PAGE records fail LINT-13.** Every A6-promoted page written by
   the W1/mint lane carries `provenance.s6_promotion`, which `_schema.json` `definitions.provenance`
   (`additionalProperties:false`) rejects. Pre-existing (fails under committed HEAD schema too), NOT
   introduced by my writes (all my 17 records validate clean). Growing as W1 mints. Records:
   Brownback, Chiaverini, Culley, Dupree, FBI v. Fazaga, FBI v. Fikre, Goldey, Gonzalez, Lackey,
   Lombardo, Martin, Nieves, Thompson, Cooley. Observed shape:
   `{from_record_id, to_record_id, as_of, born_status}`. Proposed schema patch (orchestrator/s6
   lane to ratify): add `s6_promotion` object to `definitions.provenance.properties` with those four
   keys. I did NOT apply it (s6/mint lane owns the field; CR adjudication routes lint13/schema
   findings deliberately).
2. **Systemic SD10 residue — false "Historical" is NOT unique to egbert.** `authority_weight` reads
   `identity.court_level`; the ~30 SCOTUS-residue rows (youngblood, timbs, mendez, all R2 rows, etc.)
   carry `court_level "other"`/None → all project "Historical". egbert repaired here; the rest need a
   bulk `court_level` re-derive (a `--repair-identity-from-cache`-style pass, scotus branch is safe;
   coa/state need circuit/state derivation). Orchestrator decision.
3. **R3 escalations may be upstream identity mis-keys** (black, lewis party mismatches) — candidates
   for the R1 re-key machinery in a follow-up.

## Calls / self-tests / files
- **CL calls this session: 0. Network I/O: 0. 429s: 0.** R2 enrich + egbert repair cache-served
  (`--max-calls 0`); R3/R1 web legs via WebSearch/WebFetch; R1 readjudication deferred.
- Self-tests: `ingest.py --self-test` PASS (incl. new `self_test_apply_web_cites`,
  `self_test_repair_identity_from_cache`, extended `self_test_precedence`/`self_test_binding_filters`);
  `serializer.py --self-test` PASS; `lint13 --self-test` PASS; all other lint self-tests PASS
  (lint1's `--self-test` crash on a stale `'null'` opinion_id in live content is pre-existing,
  unrelated). Full-lake LINT-13: only the 14 `s6_promotion` finding above (all mine clean).
- Code (UNCOMMITTED): `scripts/s2/ingest.py` (R2 noise-list, `--apply-web-cites`,
  `--repair-identity-from-cache`, CR-03), `scripts/s2/serializer.py` (CR-15 + self-test),
  `scripts/lint/_common.py` (CR-15 parser parity), `_overhaul2/lake/_schema.json` (web_leg/web_legs),
  3 lint13 fixtures.
- Lake writes (UNCOMMITTED): 6 R2 + 10 R3 records + egbert (17 records) + `_manifest.json`
  (17 `official_cite`/identity mirrors, counts regenerated, 662 intact, statuses unchanged).
- Deliverables (ready-to-run): `R8-R1-web-keys.jsonl`, `R8-R1-readjudicate-ids.txt`,
  `R8-R3-web-cites.jsonl`, `R8-R2-enrich-ids.txt`.
- Journal (pool `s2-ingest-s2-build-96d841cbb12e.jsonl`): `r8.web-cites` (10 applied + 15 slip-only),
  `r8.enrich-citations` (6 enriched), `r8.identity-repair` (1 repaired).
