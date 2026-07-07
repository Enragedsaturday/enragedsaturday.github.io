# S2 citations-enrichment report — R8-mintable SD10 stubs (2026-07-07)

Work order: `_run/o2-execute/S2-ENRICH-CITATIONS-WORKORDER.md` (context: R8-PIPELINE-ADJUDICATION.md §E4).
Lane/model: `{lane: s2-builder, model: claude-opus-4-8}`. Branch `overhaul2/execute`, started from HEAD `d28e200`. **Committed nothing** — the orchestrator commits at the gate.

## Real scope
80 of the 148 signed `R8-WORKLIST.json` rows have a lake record lacking `citations.display` (matches the E4 estimate exactly). Ground-truthed against the lake, not the prose. All 80 are `verified_identity` with a non-null `identity.cluster_id`. Scope ids: `_run/o2-execute/R8-ENRICH-CITATIONS-IDS.txt`.

## Outcome partition (80 = 32 + 28 + 13 + 7)
| outcome | n | lake write | disposition |
|---|---:|---|---|
| **enriched** | 32 | citations block written | official cite selected from `cluster.citations[]`; `verified_identity` unchanged |
| **citations-empty** | 28 | none (honest) | cluster carries zero `citations[]` (CL data gap) — orchestrator adjudicates slip-cite handling |
| **no-display** | 13 | none (honest) | cluster has cites but the signed serializer selects no official — escalated below |
| **cite-mismatch** | 7 | none (honest) | verified cluster resolves to an orders/cert/rehearing/companion entry, not the merits — escalated below |
| already-bearing | 0 | — | (guarded + self-tested; none in scope) |
| refused-no-cluster | 0 | — | (guarded + self-tested; none in scope) |

Writes are bounded: **32 case records changed** (only the `citations` block + standard `provenance.date_modified`) + **32 `official_cite` mirrors** in `_manifest.json`. Verified: 0 status changes, 0 identity/treatment/other-field changes, 662 manifest records intact, no suspect cite shipped.

## Calls + cache
- Clusters fetched: **80** — **cache-hits: 80, network: 0, CL calls this session: 0**, cache-hit rate **100%**.
- Every cluster was already in the pool HTTP cache (`/Users/johngalt/cssi-lake/cache/http`, mtimes 2026-07-06). Single serial lane, pacing ≤14/min armed, `--session-minutes 30` bound, resumable cursor — never exercised because the run completed in seconds with zero live calls. **Zero 429 (no network I/O).**

## Journal
`/Users/johngalt/cssi-lake/journal/s2-ingest-s2-build-96d841cbb12e.jsonl`, step `r8.enrich-citations`. Per-row schema `{step, record_id, before, after, source:"cluster.citations[]", lane, model, court_class, court_class_source, ...}`. NOTE: the journal contains an earlier superseded pass (see "Court-class + mis-key methodology" below); read latest-per-record. Final per-record state is authoritative in this report.

## Court-class + mis-key methodology (builder judgment — flagged for ratification)
The work order assumed `cluster → citations → serializer` would just yield a display. Two lake-data realities forced principled builder judgment, both journaled per-row and surfaced here:

1. **Corrupt roster court fields.** The SD10 residue carries `court_level: "other"` on mis-normalized SCOTUS rows and `identity.court` values that are bare years ("1959", "2022"), doctrinal annotations ("Binding in-circuit — 2d Cir.…"), or "unknown". A plain `court_level` read dead-ends (the precedence table has no `"other"` class). I use a deterministic, exclusive, journaled court-class ladder (`derive_enrich_court_class`): `roster:court_level` (strict-4) → `identity:court-scotus-name` (exact SCOTUS label) → `identity:court-circuit-abbrev` (`\bCir\.`) → `cluster:us-reporter-exclusive` (a `U.S.` reporter is Supreme-Court-exclusive) → `default:state-permissive`. No rung can attach a facially-wrong cite: a mis-keyed/multi-reporter cluster falls to the `state` default where the **signed serializer fail-closes (`same_rank_tie`)** rather than guessing. Enriched court-class source split: 28 `scotus-name`, 3 `circuit-abbrev`, 1 `us-reporter-exclusive`. **I did NOT modify `classify_citations`/`select_official_cite` (signed serializer) or re-run identity.**

2. **Mis-key cross-check guard (new).** A verified `cluster_id` can point to an orders-list / cert-denial / rehearing / companion cluster whose faithful cite is the *wrong* cite for the record. The first (unguarded) pass would have written 7 such cites; I reverted it, added a guard (`roster expected_citation must be present in the verified cluster's citations`), and re-ran clean. The guard fails closed on the 5 roster-checkable mis-keys; 2 more with no roster ground-truth are held by a small documented builder-review set (`ENRICH_REVIEW_SUSPECTED_MISKEYS`, precedent `FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS`). All 7 escalated, no suspect cite shipped.

## Escalations

### A. cite-mismatch — suspected identity mis-key (7) — NEEDS ORCHESTRATOR RE-KEY
Verified cluster carries a real cite but it is not the record's merits cite. Left honest (display=null); **do not author until re-keyed.**
| record_id | cluster cite (candidate) | intended merits cite | signal |
|---|---|---|---|
| austin-v-united-states--9140366 | 510 U.S. 904 | 509 U.S. 602 (1993) | roster-expected-absent; orders entry (filed 1993-10-04, citation_count 0) |
| bennis-v-michigan--9159725 | 517 U.S. 1163 | 516 U.S. 442 (1996) | roster-expected-absent; orders (filed 1996-04-22, count 0) |
| board-of-county-commissioners-of-bryan-county-v-brown--9167020 | 520 U.S. 1283 | 520 U.S. 397 (1997) | roster-expected-absent; orders (filed 1997-06-16, count 0) |
| scott-v-united-states--9020551 | 439 U.S. 1046 | 436 U.S. 128 (1978) | roster-expected-absent; cert-denial (filed 1978-12-11, count 5) |
| united-states-v-giordano--109022 | 416 U.S. 580 | 416 U.S. 505 (1974) | roster-expected-absent; cluster is companion *U.S. v. Chavez* |
| g-m-leasing-corp-v-united-states--9017014 | 435 U.S. 923 | 429 U.S. 338 (1977) | builder-review (no roster cite); rehearing/orders (filed 1978-03-20, count 0, no scdb_id) |
| quantity-of-copies-of-books-v-kansas--107502 | 388 U.S. 452 | 378 U.S. 205 (1964) | builder-review (no roster cite); 1967 proceeding ≠ the 1964 search-and-seizure landmark |

### B. no-display — serializer selected no official (13) — two sub-classes
**B1. Signed serializer fail-closes despite a VALID official cite present (6).** The merits `U.S.`/`F.3d` cite is in the cluster, but `select_official_cite` returns None on the first unlisted *type-1* reporter (`Fla. L. Weekly Fed. S`, `FED App.`) before it can rank the good cite. Recoverable by an orchestrator serializer-policy call (skip unlisted type-1 rather than hard-fail) or a hand-selected cite — NOT a re-key:
- county-of-los-angeles-v-mendez--4395246 (has `U.S.` → 581 U.S. 420)
- grady-v-north-carolina--2789928 (has `U.S.` → 575 U.S. 306)
- manuel-v-city-of-joliet--4376986 (has `U.S.` → 580 U.S. 357)
- united-states-v-james-daniel-good-real-property--112914 (has `U.S.` → 510 U.S. 43)
- ziglar-v-abbasi--4403804 (has `U.S.` → 582 U.S. 120)
- northrup-v-city-of-toledo-police-dept--2800431 (has `F.3d` → 785 F.3d 1128; defeated by `FED App.`)

**B2. Suspected wrong-cluster / no rankable merits federal cite (7)** — like class A, likely need re-key:
- carroll-v-carman--2750102 (scotus; `S. Ct.`/`L. Ed. 2d` only, no `U.S.`; per curiam 574 U.S. 13)
- alvarez-v-city-of-brownsville--9361139 (5th Cir.; cluster is cert-denial `S. Ct.`/`L. Ed. 2d` only)
- united-states-v-maez--7355106 (military `M.J.`/`CAAF LEXIS` — wrong court entirely)
- owen-v-city-of-independence--8922609 (scotus 445 U.S. 622; cluster carries only `F.2d`)
- united-states-v-donovan--347744 (scotus 429 U.S. 413; cluster carries only `F.2d`)
- frank-v-maryland--793662 (scotus 359 U.S. 360; cluster carries `F.3d` — facially wrong cluster)
- robbins-v-california--2262192 (scotus 453 U.S. 420; cluster carries California state reporters)

### C. citations-empty (28) — CL data gap, adjudicate slip-cite handling (S2 A3 precedent)
Cluster has zero `citations[]` (`citation_count: 0`, CL source "C" = court-website ingest without a reporter feed). Left honest, no fabricated cite. Many are recent (2021–2026) but several are older published cases CL simply never enriched (e.g., alasaad-v-wolf = 988 F.3d 8 in reality; kolsuz = 890 F.3d 133). Cached cluster mtime 2026-07-06; orchestrator may force a live re-fetch if desired.
```
alasaad-v-wolf--4855246                        united-states-v-lyle--8435375
carter-v-united-states--10662535               united-states-v-mendoza--10131439
jimerson-v-lewis--9475670                       united-states-v-moore-bush--6476396
robinson-v-commonwealth--10793178               united-states-v-ruiz--10650477
state-v-larson--10657314                        united-states-v-small--10593041
united-states-v-black--10355347                 united-states-v-williams--10670874
united-states-v-cole--9623101                   united-states-v-wilson--10664712
united-states-v-davis--10669954                 united-states-v-young--10687648
united-states-v-holcomb--10670143               district-of-columbia-v-r-w--10845431
united-states-v-hunt--10661637                  landor-v-louisiana-department-of-corrections-and-public-safety--10878535
united-states-v-kolsuz--4499413                 olivier-v-city-of-brandon--10811625
united-states-v-lee--10670779                   postal-service-v-konan--10799651
united-states-v-lewis--10640348                 the-geo-group-inc-v-menocal--10800194
united-states-v-loines--9357144                 zorn-v-linton--10813527
```

## Enriched (32) — cite / record / court-class source
```
488 U.S. 51      arizona-v-youngblood--112156                       [scotus-name]
460 U.S. 325     briscoe-v-lahue--110885                            [scotus-name]
509 U.S. 259     buckley-v-fitzsimmons--112894                      [scotus-name]
256 U.S. 465     burdeau-v-mcdowell--99820                          [scotus-name]
467 U.S. 479     california-v-trombetta--111206                     [scotus-name]
96 U.S. 727      ex-parte-jackson--89759                            [scotus-name]
502 U.S. 21      hafer-v-melo--112657                               [scotus-name]
413 U.S. 483     heller-v-new-york--108853                          [scotus-name]
424 U.S. 409     imbler-v-pachtman--109387                          [scotus-name]
556 U.S. 586     kansas-v-ventris--145880                           [scotus-name]
585 U.S. 87      lozman-v-city-of-riviera-beach--4508137            [scotus-name]
367 U.S. 717     marcus-v-search-warrant--106287                    [scotus-name]
588 U.S. 109     mcdonough-v-smith--9231241                         [scotus-name]
434 U.S. 220     moore-v-illinois--109757                           [scotus-name]
566 U.S. 356     rehberg-v-paulk--626447                            [scotus-name]
413 U.S. 496     roaden-v-kentucky--108854                          [scotus-name]
342 U.S. 165     rochin-v-california--104943                        [scotus-name]
459 U.S. 553     south-dakota-v-neville--110832                     [scotus-name]
428 U.S. 465     stone-v-powell--109540                             [scotus-name]
586 U.S. 146     timbs-v-indiana--4591916                           [scotus-name]
461 U.S. 555     united-states-v-8-850-in-currency--110936          [scotus-name]
524 U.S. 321     united-states-v-bajakajian--118234                 [scotus-name]
384 U.S. 251     united-states-v-blue--107238                       [scotus-name]
440 U.S. 741     united-states-v-caceres--110049                    [scotus-name]
407 U.S. 297     united-states-v-united-states-district-court-keith--108581 [scotus-name]
474 U.S. 242     united-states-v-von-neumann--111551                [scotus-name]
429 U.S. 545     weatherford-v-bursey--109590                       [scotus-name]
491 U.S. 58      will-v-michigan-department-of-state-police--112293 [scotus-name]
596 U.S. 482     egbert-v-boule--6475794                            [us-reporter-exclusive]
773 F.3d 932     united-states-v-camou--2759861                     [circuit-abbrev]
654 F.3d 480     united-states-v-massenburg--223188                 [circuit-abbrev]
821 F.3d 467     united-states-v-vasquez-algarin--3199633           [circuit-abbrev]
```

## Self-tests
`python3 scripts/s2/ingest.py --self-test` → `self-test passed` (full suite, incl. new `self_test_enrich_citations`): happy-path enrich, already-bearing no-op, no-cluster refusal, out-of-scope refusal (SystemExit), unknown-id refusal (SystemExit), citations-empty, cite-mismatch guard (roster-expected-absent), resume skip, `--no-resume` re-process, and the court-class ladder rungs.

## Files
- Code: `scripts/s2/ingest.py` (`--enrich-citations` surface: `derive_enrich_court_class`, `enrich_citations`, `roster_expected_cite`, `ENRICH_REVIEW_SUSPECTED_MISKEYS`, guard, self-test). UNCOMMITTED.
- Lake writes (UNCOMMITTED): 32 records under `_overhaul2/lake/cases/` + `_overhaul2/lake/_manifest.json` (32 `official_cite` mirrors).
- Scope ids: `_run/o2-execute/R8-ENRICH-CITATIONS-IDS.txt`. Journal: pool `s2-ingest-s2-build-96d841cbb12e.jsonl`.

## Net effect on the R8 mint
32 previously-blocked SD10 stubs now carry `citations.display` and clear `record-missing-citation`. 48 remain blocked pending orchestrator adjudication: 28 slip-cite (empty), 6 serializer-policy (B1, valid cite present), 14 identity re-key (7 cite-mismatch + 7 no-display B2).
