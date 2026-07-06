# S6 Step 1a Roster Regeneration + Reconciliation

Local-only reconciliation for S6 method step 1a. No network calls and no CL REST calls were used in this lane.

## Inputs run/read

- Ran: `python3 _overhaul2/scripts/audit_cases.py --format both --out-md _run/o2-execute/S6-STEP1-ROSTER.md --out-json _run/o2-execute/S6-STEP1-ROSTER.json`
- Read: `_overhaul2/lake/_manifest.json`
- Read: `_overhaul2/S6-SEED.md`

## Count reconciliation

| Check | Current regenerated / manifest value | Baseline / expected | Reconciliation |
|---|---:|---:|---|
| `audit_cases.py` case_pages | 459 | 458 | Drift +1 = `content/cases/index.md`; excluding that index, actual case page paths match manifest at 458. |
| `audit_cases.py` raw distinct captions | 556 | n/a | Informational scanner total. |
| `audit_cases.py` roster rows | 94 | 94 scan rows in S2-close manifest / 89 roster rows in committed `S6-SEED.md` | Matches manifest pre-ignore scan count; committed seed is stale by +5 net roster rows. |
| `audit_cases.py` placeholders | 5 | 5 | No placeholder-count drift. |
| Seedable S6 stubs after ignore rows | 93 | 93 | 94 roster rows minus manifest ignore row `LLC v. John Doe`. |
| Manifest total records | 551 | 551 | PASS. |
| Manifest status split | verified=421; under_review=35; verified_identity=65; fabrication_suspected=25; not_found=5 | 421 / 35 / 65 / 25 / 5 | PASS. |

Manifest note on the row/page count delta: `_manifest.json` already says the current checkout had 458 case pages and `audit_cases.py` reported 94 roster rows before the LLC ignore-row exclusion. The present rerun still reports 94 roster rows, but now counts 459 `content/cases/*.md` files because `content/cases/index.md` is included by the scanner glob and excluded by the manifest page-record set.

## Drift attribution vs committed S6-SEED.md

Committed `S6-SEED.md` roster rows parsed: 89. Current regenerated roster rows: 94. Net roster drift: +5.

### Added roster rows

| Caption | Current row | Current sources | Manifest stub status | Stub record | S2-close note |
|---|---:|---|---|---|---|
| Carman v. Carroll | 6 | warrant-exceptions/Knock and Talk.md:69; warrant-exceptions/Knock and Talk.md:112 | verified_identity | `carman-v-carroll--8693292` | known caption-variant pair in S6 handoff |
| Carroll v. Carman | 7 | warrant-exceptions/Knock and Talk.md:28; warrant-exceptions/Knock and Talk.md:58; warrant-exceptions/Knock and Talk.md:69; warrant-exceptions/Knock and Talk.md:112 | fabrication_suspected | `carroll-v-carman--8693292` | known caption-variant pair in S6 handoff |
| Morgan v. Fairfield County | 23 | warrant-exceptions/Knock and Talk.md:64; warrant-exceptions/Knock and Talk.md:113 | not_found | `morgan-v-fairfield-county--u2812be2f` | S6 handoff not_found; web/second-source cross-check remains for S6 |
| Morse v. French | 24 | warrant-exceptions/Knock and Talk.md:111 | fabrication_suspected | `morse-v-french--6536632` | known caption variant of French v. Merrill cert-denial caption per S6 handoff |
| People v. Frederick | 25 | warrant-exceptions/Knock and Talk.md:67; warrant-exceptions/Knock and Talk.md:114 | verified_identity | `people-v-frederick--10579458` | newly surfaced by current prose scan |
| State v. Christensen | 29 | warrant-exceptions/Knock and Talk.md:66; warrant-exceptions/Knock and Talk.md:115 | fabrication_suspected | `state-v-christensen--10657325` | newly surfaced by current prose scan |

### Removed roster rows

| Caption | Prior seed row | Reconciliation |
|---|---:|---|
| United States v. Smith | 77 | No longer no-page: now page-backed at `content/cases/United States v. Smith (2024).md` with alias `United States v. Smith`; scanner drops it as an exact page match. Manifest page record `United States v. Smith (2024)` status `verified`. |

### Same caption, changed row details

| Caption | Prior seed detail | Current regenerated detail | Drift |
|---|---|---|---|
| United States v. Meyer | court/era `8th Cir. 2021`; mentions `4` | court/era `8th Cir. 2021`; mentions `3`; sources `warrant-exceptions/Knock and Talk.md:125; warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:76; warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:119` | mentions `4` -> `3` |

## R1 table: regenerated roster rows against current manifest stubs

S6-stub status counts only: {'not_found': 3, 'verified_identity': 65, 'fabrication_suspected': 25}. Manifest `not_found=5` includes two non-S6 page records (`Entick v. Carrington`, `Wilkes v. Wood`); S6 stubs account for 3 of the 5.

| Row | Caption | Manifest stub status | Stub record_id | Cluster | Manifest source_row_index | R1/S2-close disposition |
|---:|---|---|---|---:|---:|---|
| 1 | Alasaad v. Mayorkas | `not_found` | `alasaad-v-mayorkas--u782a2d04` |  | 1 | terminal/current miss or caption variant; no authoring from this stub |
| 2 | Alasaad v. Wolf | `verified_identity` | `alasaad-v-wolf--4855246` | 4855246 | 2 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 3 | Alvarez v. City of Brownsville | `verified_identity` | `alvarez-v-city-of-brownsville--9361139` | 9361139 | 3 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 4 | Arkansas v. Sanders | `fabrication_suspected` | `arkansas-v-sanders--10601315` | 10601315 | 4 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 5 | Beautiful Struggle v. Baltimore Police Dep't | `not_found` | `beautiful-struggle-v-baltimore-police-dep-t--uf407874b` |  | 5 | terminal/current miss or caption variant; no authoring from this stub |
| 6 | Carman v. Carroll | `verified_identity` | `carman-v-carroll--8693292` | 8693292 | 6 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 7 | Carroll v. Carman | `fabrication_suspected` | `carroll-v-carman--8693292` | 8693292 | 7 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 8 | Carter v. United States | `verified_identity` | `carter-v-united-states--10662535` | 10662535 | 8 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 9 | Chapman v. California | `verified_identity` | `chapman-v-california--8428427` | 8428427 | 9 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 10 | Commonwealth v. Serge | `verified_identity` | `commonwealth-v-serge--2074658` | 2074658 | 10 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 11 | District of Columbia v. Heller | `fabrication_suspected` | `district-of-columbia-v-heller--3180743` | 3180743 | 11 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 12 | Egbert v. Boule | `verified_identity` | `egbert-v-boule--6475794` | 6475794 | 12 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 13 | Frank v. Maryland | `verified_identity` | `frank-v-maryland--793662` | 793662 | 13 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 14 | G. M. Leasing Corp. v. United States | `verified_identity` | `g-m-leasing-corp-v-united-states--9017014` | 9017014 | 14 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 15 | Gaetjens v. Winnebago County | `verified_identity` | `gaetjens-v-winnebago-county--4899427` | 4899427 | 15 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 16 | Jimerson v. Lewis | `verified_identity` | `jimerson-v-lewis--9475670` | 9475670 | 16 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 17 | Johnson v. Glick | `verified_identity` | `johnson-v-glick--8903545` | 8903545 | 17 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 18 | Knight v. Jacobson | `verified_identity` | `knight-v-jacobson--778847` | 778847 | 18 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 19 | LaDuke v. Nelson | `fabrication_suspected` | `laduke-v-nelson--571489` | 571489 | 19 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 20 | LLC v. John Doe | **NO MANIFEST STUB** |  |  |  | **LOUD FLAG:** regenerated roster row has no S6 stub. Manifest exclusions list it as `s6_ignore_rows` / Section c ignore row. |
| 21 | Martin v. United States | `fabrication_suspected` | `martin-v-united-states--10636952` | 10636952 | 21 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 22 | Milam v. United States | `fabrication_suspected` | `milam-v-united-states--10654082` | 10654082 | 22 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 23 | Morgan v. Fairfield County | `not_found` | `morgan-v-fairfield-county--u2812be2f` |  | 23 | terminal/current miss or caption variant; no authoring from this stub |
| 24 | Morse v. French | `fabrication_suspected` | `morse-v-french--6536632` | 6536632 | 24 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 25 | People v. Frederick | `verified_identity` | `people-v-frederick--10579458` | 10579458 | 25 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 26 | Quantity of Copies of Books v. Kansas | `verified_identity` | `quantity-of-copies-of-books-v-kansas--107502` | 107502 | 26 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 27 | Robbins v. California | `verified_identity` | `robbins-v-california--2262192` | 2262192 | 27 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 28 | Robinson v. Commonwealth | `fabrication_suspected` | `robinson-v-commonwealth--10638592` | 10638592 | 28 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 29 | State v. Christensen | `fabrication_suspected` | `state-v-christensen--10657325` | 10657325 | 29 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 30 | State v. Demesme | `verified_identity` | `state-v-demesme--5035127` | 5035127 | 30 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 31 | State v. Karston | `verified_identity` | `state-v-karston--1767998` | 1767998 | 31 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 32 | State v. Larson | `verified_identity` | `state-v-larson--10657314` | 10657314 | 32 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 33 | State v. Weaver | `fabrication_suspected` | `state-v-weaver--10675098` | 10675098 | 33 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 34 | State v. Wint | `verified_identity` | `state-v-wint--8267547` | 8267547 | 34 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 35 | Trupiano v. United States | `fabrication_suspected` | `trupiano-v-united-states--658600` | 658600 | 35 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 36 | United States v. Aigbekaen | `verified_identity` | `united-states-v-aigbekaen--4680725` | 4680725 | 36 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 37 | United States v. Amos | `fabrication_suspected` | `united-states-v-amos--10686575` | 10686575 | 37 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 38 | United States v. Berkowitz | `fabrication_suspected` | `united-states-v-berkowitz--4520474` | 4520474 | 38 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 39 | United States v. Black | `verified_identity` | `united-states-v-black--10355347` | 10355347 | 39 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 40 | United States v. Brinkley | `verified_identity` | `united-states-v-brinkley--4805913` | 4805913 | 40 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 41 | United States v. Burgess | `verified_identity` | `united-states-v-burgess--9495745` | 9495745 | 41 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 42 | United States v. Camou | `verified_identity` | `united-states-v-camou--2759861` | 2759861 | 42 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 43 | United States v. Capers | `verified_identity` | `united-states-v-capers--5306116` | 5306116 | 43 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 44 | United States v. Carlton Williams | `verified_identity` | `united-states-v-carlton-williams--4522771` | 4522771 | 44 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 45 | United States v. Carpenter | `verified_identity` | `united-states-v-carpenter--10614578` | 10614578 | 45 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 46 | United States v. Castillo | `verified_identity` | `united-states-v-castillo--10322393` | 10322393 | 46 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 47 | United States v. Chatrie | `fabrication_suspected` | `united-states-v-chatrie--10881683` | 10881683 | 47 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 48 | United States v. Chavez | `verified_identity` | `united-states-v-chavez--10329331` | 10329331 | 48 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 49 | United States v. Cole | `verified_identity` | `united-states-v-cole--9623101` | 9623101 | 49 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 50 | United States v. Crumble | `verified_identity` | `united-states-v-crumble--4767477` | 4767477 | 50 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 51 | United States v. Cruz | `verified_identity` | `united-states-v-cruz--10662743` | 10662743 | 51 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 52 | United States v. Daniels | `fabrication_suspected` | `united-states-v-daniels--10534900` | 10534900 | 52 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 53 | United States v. Davis | `verified_identity` | `united-states-v-davis--10669954` | 10669954 | 53 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 54 | United States v. Ganias | `fabrication_suspected` | `united-states-v-ganias--8429176` | 8429176 | 54 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 55 | United States v. Hanapel | `verified_identity` | `united-states-v-hanapel--10038262` | 10038262 | 55 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 56 | United States v. Hay | `verified_identity` | `united-states-v-hay--9485331` | 9485331 | 56 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 57 | United States v. Holcomb | `verified_identity` | `united-states-v-holcomb--10670143` | 10670143 | 57 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 58 | United States v. Hunt | `verified_identity` | `united-states-v-hunt--10661637` | 10661637 | 58 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 59 | United States v. Kolsuz | `verified_identity` | `united-states-v-kolsuz--4499413` | 4499413 | 59 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 60 | United States v. Lee | `verified_identity` | `united-states-v-lee--10670779` | 10670779 | 60 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 61 | United States v. Lewis | `verified_identity` | `united-states-v-lewis--10640348` | 10640348 | 61 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 62 | United States v. Liddell | `fabrication_suspected` | `united-states-v-liddell--9232233` | 9232233 | 62 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 63 | United States v. Loera | `verified_identity` | `united-states-v-loera--10386176` | 10386176 | 63 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 64 | United States v. Loines | `verified_identity` | `united-states-v-loines--9357144` | 9357144 | 64 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 65 | United States v. Lyle | `verified_identity` | `united-states-v-lyle--8435375` | 8435375 | 65 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 66 | United States v. Maez | `verified_identity` | `united-states-v-maez--7355106` | 7355106 | 66 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 67 | United States v. Massenburg | `verified_identity` | `united-states-v-massenburg--223188` | 223188 | 67 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 68 | United States v. May-Shaw | `verified_identity` | `united-states-v-may-shaw--4743325` | 4743325 | 68 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 69 | United States v. Mayville | `verified_identity` | `united-states-v-mayville--4742862` | 4742862 | 69 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 70 | United States v. Mendez | `fabrication_suspected` | `united-states-v-mendez--10374557` | 10374557 | 70 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 71 | United States v. Mendoza | `verified_identity` | `united-states-v-mendoza--10131439` | 10131439 | 71 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 72 | United States v. Meyer | `fabrication_suspected` | `united-states-v-meyer--10292544` | 10292544 | 72 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 73 | United States v. Moore-Bush | `verified_identity` | `united-states-v-moore-bush--6476396` | 6476396 | 73 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 74 | United States v. Oliveras | `verified_identity` | `united-states-v-oliveras--9484364` | 9484364 | 74 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 75 | United States v. Payne | `verified_identity` | `united-states-v-payne--9494371` | 9494371 | 75 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 76 | United States v. Perez | `fabrication_suspected` | `united-states-v-perez--10661791` | 10661791 | 76 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 77 | United States v. Perez-Rodriguez | `verified_identity` | `united-states-v-perez-rodriguez--5067201` | 5067201 | 77 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 78 | United States v. Porter | `verified_identity` | `united-states-v-porter--10626686` | 10626686 | 78 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 79 | United States v. Reddick | `fabrication_suspected` | `united-states-v-reddick--9364250` | 9364250 | 79 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 80 | United States v. Ruckman | `verified_identity` | `united-states-v-ruckman--8699562` | 8699562 | 80 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 81 | United States v. Ruiz | `verified_identity` | `united-states-v-ruiz--10650477` | 10650477 | 81 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 82 | United States v. Small | `verified_identity` | `united-states-v-small--10593041` | 10593041 | 82 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 83 | United States v. Trent | `verified_identity` | `united-states-v-trent--4880705` | 4880705 | 83 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 84 | United States v. Vasquez-Algarin | `verified_identity` | `united-states-v-vasquez-algarin--3199633` | 3199633 | 84 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 85 | United States v. Verdugo-Urquidez | `fabrication_suspected` | `united-states-v-verdugo-urquidez--9151048` | 9151048 | 85 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 86 | United States v. West | `fabrication_suspected` | `united-states-v-west--10653830` | 10653830 | 86 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 87 | United States v. White | `fabrication_suspected` | `united-states-v-white--10349533` | 10349533 | 87 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 88 | United States v. Williams | `verified_identity` | `united-states-v-williams--10670874` | 10670874 | 88 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 89 | United States v. Wilson | `verified_identity` | `united-states-v-wilson--10664712` | 10664712 | 89 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 90 | United States v. Xiang | `verified_identity` | `united-states-v-xiang--9397097` | 9397097 | 90 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 91 | United States v. Young | `verified_identity` | `united-states-v-young--10687648` | 10687648 | 91 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 92 | Wyman v. James | `fabrication_suspected` | `wyman-v-james--3121332` | 3121332 | 92 | fail-closed frontier flag; S6 adjudicates before any authoring |
| 93 | Ziglar v. Abbasi | `verified_identity` | `ziglar-v-abbasi--4403804` | 4403804 | 93 | identity complete; S6 may gate/promote only after its R1/R2 checks |
| 94 | Zorn v. Linton | `verified_identity` | `zorn-v-linton--10813527` | 10813527 | 94 | identity complete; S6 may gate/promote only after its R1/R2 checks |

## Missing manifest stubs

**LOUD FLAG: missing regenerated-roster stubs exist.**

| Caption | Current sources | Flags | Manifest reconciliation |
|---|---|---|---|
| LLC v. John Doe | use-of-force-and-liability/Section 1983 Liability and Qualified Immunity.md:191 | incidental non-4A mention (Strike 3 Holdings BitTorrent docket, corrupted-CL-object warning for Zorn) — ignore | No stub in manifest. Manifest exclusion reason: `S6-SEED section c ignore row`; source_row_index `20`. |

## Manifest stubs not in regenerated roster

None. All 93 S6 manifest stubs map back to current regenerated roster rows after the LLC ignore exclusion.

## SEED section a rows: exact stubs and S2 conclusions

| Caption | Exact stub JSON | Manifest record_id | Status | Cluster | Official cite | Roster key | Identity fields from stub | What S2 concluded |
|---|---|---|---|---:|---|---|---|---|
| United States v. Mayville | `_overhaul2/lake/cases/united-states-v-mayville--4742862.json` | `united-states-v-mayville--4742862` | `verified_identity` | 4742862 | 955 F.3d 825 | `United States v. Mayville\|10th Cir. 2020\|4-what-is-a-seizure/Traffic Stops.md:96,4-what-is-a-seizure/Traffic Stops.md:147\|69` | case_name=United States v. Mayville; input_case_name=United States v. Mayville; absolute_url=/opinion/4742862/united-states-v-mayville/; identity_method=frontier-identity; expected_citation_found=True; canonical_name_match=True | S2 resolved a frontier identity stub as `verified_identity` with identity complete; fabrication_check remains `pending` and treatment/progeny were intentionally not derived pre-promotion. |
| United States v. Small | `_overhaul2/lake/cases/united-states-v-small--10593041.json` | `united-states-v-small--10593041` | `verified_identity` | 10593041 |  | `United States v. Small\|4th Cir. 2019\|3-what-is-a-search/Abandonment.md:75\|82` | case_name=United States v. SMALL; input_case_name=United States v. Small; absolute_url=/opinion/10593041/united-states-v-small/; identity_method=frontier-identity; expected_citation_found=False; canonical_name_match=True | S2 resolved a frontier identity stub as `verified_identity` with identity complete; fabrication_check remains `pending` and treatment/progeny were intentionally not derived pre-promotion. |
| United States v. Lyle | `_overhaul2/lake/cases/united-states-v-lyle--8435375.json` | `united-states-v-lyle--8435375` | `verified_identity` | 8435375 |  | `United States v. Lyle\|Binding in-circuit — 2d Cir.; narrows Byrd lawful-possession\|8-exclusionary-rule-remedies/Standing to Challenge a Search.md:79,8-exclusionary-rule-remedies/Standing to Challenge a Search.md:117\|65` | case_name=United States v. Lyle; input_case_name=United States v. Lyle; absolute_url=/opinion/8435375/united-states-v-lyle/; identity_method=frontier-identity; expected_citation_found=False; canonical_name_match=True | S2 resolved a frontier identity stub as `verified_identity` with identity complete; fabrication_check remains `pending` and treatment/progeny were intentionally not derived pre-promotion. |
| United States v. Moore-Bush | `_overhaul2/lake/cases/united-states-v-moore-bush--6476396.json` | `united-states-v-moore-bush--6476396` | `verified_identity` | 6476396 |  | `United States v. Moore-Bush\|1st Cir. 2022, en banc\|3-what-is-a-search/Curtilage.md:87,3-what-is-a-search/Curtilage.md:127,3-what-is-a-search/Fourth Amendment Framework.md:82,3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:59,3-what-is-a-search/Two Definitions of Search.md:80,3-what-is-a-search/Two Definitions of Search.md:129\|73` | case_name=United States v. Moore-Bush; input_case_name=United States v. Moore-Bush; absolute_url=/opinion/6476396/united-states-v-moore-bush/; identity_method=frontier-identity; expected_citation_found=False; canonical_name_match=True | S2 resolved a frontier identity stub as `verified_identity` with identity complete; fabrication_check remains `pending` and treatment/progeny were intentionally not derived pre-promotion. |

## Placeholder rows

Current placeholder rows: 5. Manifest excludes them under `exclusions.citation_format_placeholders`. Names: `Smith v. Jones`, `State v. Randolph`, `State v. Smith`, `Stern v. Florida`, `Stern v. State`.

## Bottom line

- Regenerated roster count matches the S2-close manifest scan count: 94 roster rows; after the manifest ignore row, 93 S6 stubs exist.
- The committed `S6-SEED.md` roster is stale against current content: +6 added rows, -1 removed row, and one same-caption mention-count drift (`United States v. Meyer`).
- The only regenerated roster row with no manifest stub is `LLC v. John Doe`; manifest intentionally excludes it as an ignore row, but it still violates the literal “every roster row has a stub” expectation.
- The four SEED §a watch-list rows are all current `verified_identity` S6 stubs, not `fabrication_suspected` or `not_found`; S6 still must perform its R1/R4 adjudication before author/remove decisions.
