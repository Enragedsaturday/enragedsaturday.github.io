# R15 Treatment-Derivation Build-QA Audit — S2 Lake

- **lane** = `claude-treatment-audit`
- **model** = `claude-opus-4-8`
- **effort** = `xhigh`
- **mode** = read-only (no lake writes; this report is the sole artifact)
- **generated** = 2026-07-06
- **scope** = S2 spec R15 lighter build-QA pass — derivation MECHANICS + trail coherence only. The full 1-Claude+2-Codex per-proposition adversarial panel is S9's job; this pass does NOT re-derive legal conclusions.
- **inputs** = `_overhaul2/lake/cases/*.json` (551 records) · `_overhaul2/lake/_manifest.json` · builder journal `/Users/johngalt/cssi-lake/journal/s2-ingest-s2-build-96d841cbb12e.jsonl` (grepped by record_id/step, never read whole)

---

## 1. Census

### 1.1 Records / treatment coverage
| Bucket | Count |
|---|---:|
| Total records | 551 |
| Records with a `treatment{}` block | 551 |
| Records with a `treatment.derivation{}` (3 lanes executed) | 456 |
| — of which migration-seed composite basis | 454 |
| — of which principal-holding (pre-seeded, A13) | 2 (Belton, Smith 2024) |
| Records blocked from derivation (frontier / `unverified`, SD10) | 93 |
| Migration-seed but derivation empty/pending (not_found English cases) | 2 (Entick v. Carrington, Wilkes v. Wood) |

### 1.2 Lane completion (manifest `lane_status.treatment` + record `derivation`)
| Lane | complete | pending | records reviewed>0 | cap_hits |
|---|---:|---:|---:|---:|
| lane1_negative | 456 | 2 | 456 | **341** |
| lane2_top_cited | 456 | 2 | 456 | **411** |
| lane3_recency | 456 | 2 | **0** | 0 |

The 2 pending per lane = Entick v. Carrington + Wilkes v. Wood (`not_found` English cases, off-CL by nature — no CL cluster to scan; honest pending, not a defect). Manifest `lane_status.*.cursor` is null for all 458 (resume-cursor, distinct from the cap `final_cursor` that lives in `derivation`).

### 1.3 Proposed-event volume (all `proposed:true`; NONE auto-applied)
| Lane | Σ reviewed | Σ proposed_negative_events |
|---|---:|---:|
| lane1_negative | 75,349 | 3,876 |
| lane2_top_cited | 10,613 | 10,417 |
| lane3_recency | **0** | **0** |
| **Total edges emitted** | | **14,326** (all `proposed:true`, `field_iii:"mentioned"`) |

### 1.4 Composite (Field-I) distribution
`good_law` 440 · `caution` 11 · `superseded` 7 · `unverified` 93. All 18 non-`good_law`/non-`unverified` composites trace to A13 migration edges or principal-holding pre-seed — **none produced by a lane proposal** (see §2). Composite-basis: migration-seed 456 · principal-holding 2 · unverified 93.

### 1.5 Triage read-rate (journal `treatment.triage`, lane1 only)
73,909 triage decisions: **71,036 snippet-classified (96.1%)** / **2,873 escalated to full read (3.9%)**. Reasons: `no_negative_keyword_in_snippet` 71,034 · `binding_ambiguous_negative_keyword` 2,798 (→read) · `missing_snippet` 49 · `negative_keyword_near_target` 26 · `not_near_target` 2. Lane1 full-text reads (`hit_text`) = 2,823 (matches escalations). Lane2 reads top-N directly (`hit_text` = 4,371, no triage step — expected for the top-cited lane). **Lane3 has zero triage/hit_text/page steps** (see FLAG-C).

---

## 2. High-stakes rows — negative-treatment events

**Population.** Because lane 1's negative-keyword scan surfaces any citing case containing `overrul*/abrogat*/supersed*/vacat*/reversed` anywhere in text, **440 of 456 derived records carry ≥1 negative-treatment edge**. All were audited in aggregate for the R6/S9-boundary contract; the genuinely load-bearing rows (where a negative event actually shaped Field-I) are the **18 non-good composites**, given individual verdicts below.

**Core safety property — HELD (PASS).** Across all 14,326 edges: `proposed == true` on 100% (0 exceptions); `field_iii == "mentioned"` on 100%; no record's composite was flipped by a lane proposal. Every non-good composite is migration- or pre-seed-sourced. **No negative-treatment event was auto-applied — the S9 two-reviewer boundary is intact.** Auto-application suspects: 0.

### 2.1 The 18 composite-affecting rows (migration/pre-seed sourced)
| Record | Field-I | Basis | Event source | Verdict |
|---|---|---|---|---|
| Aguilar v. Texas | superseded | migration-seed | `migration:abrogated` ← Illinois v. Gates | FLAG-D (no ctrl cluster_id) |
| Gouled v. United States | superseded | migration-seed | `migration:overruled` ← Warden v. Hayden | FLAG-D |
| Jones v. United States | superseded | migration-seed | `migration:overruled` ← Rakas / Salvucci | FLAG-D |
| Michigan v. Jackson | superseded | migration-seed | `migration:overruled` ← Montejo v. Louisiana | FLAG-D |
| Olmstead v. United States | superseded | migration-seed | `migration:overruled` ← Katz v. United States | FLAG-D |
| Spinelli v. United States | superseded | migration-seed | `migration:abrogated` ← Illinois v. Gates | FLAG-D |
| Wolf v. Colorado | superseded | migration-seed | `migration:overruled` ← Mapp v. Ohio | FLAG-D |
| Boyd v. United States | caution | migration-seed | override + `migration:limited` ← Warden v. Hayden | FLAG-D |
| Coolidge v. New Hampshire | caution | migration-seed | override + `migration:limited` ← Horton v. California | FLAG-D |
| Escobedo v. Illinois | caution | migration-seed | override + limited ← Miranda/Kirby/Moran | FLAG-D |
| Mathis v. United States (1968) | caution | migration-seed | override + limited ← Howes v. Fields | FLAG-D |
| Monroe v. Pape | caution | migration-seed | override + limited ← Monell | FLAG-D |
| Oregon v. Elstad | caution | migration-seed | override + limited ← Missouri v. Seibert | FLAG-D |
| Saucier v. Katz | caution | migration-seed | override + limited ← Pearson v. Callahan | FLAG-D |
| Thornton v. United States | caution | migration-seed | override + limited ← Arizona v. Gant | FLAG-D |
| United States v. Agurs | caution | migration-seed | override + limited ← United States v. Bagley | FLAG-D |
| United States v. Chadwick | caution | migration-seed | override + limited ← California v. Acevedo | FLAG-D |
| **New York v. Belton** | caution / override superseded | principal-holding (pre-seed) | override ← Arizona v. Gant | **FLAG-B** (by[] corrupt) |
| **United States v. Smith (2024)** | good_law / override caution | principal-holding (pre-seed) | override ← Chatrie v. United States | **FLAG-B** (by[] corrupt) |

All 18 correctly carry `varies_by_point:true` where an override exists, valid Field-I/II vocabulary, `proposed`/migration provenance, and are NOT `verified` (correctly awaiting S9). Their sole defects are the missing controlling-case cluster_id (FLAG-D) and — for the 2 pre-seed rows — the malformed `by[]` (FLAG-B).

### 2.2 The 422 good_law-composite rows with proposed negative edges
Audited in aggregate: 100% `proposed:true`, controlling-hit `cluster_id` recorded on every lane-derived edge (14,306/14,306), snippet-or-read decision journaled with reason (`treatment.triage`), composite un-flipped. **COHERENT.**

---

## 3. Cap-hit roster (F-S2-09 contract)

**Contract:** every lane with `cap_hit:true` must carry `final_cursor` + `audit_needed:true` in `treatment.derivation[lane]`. Totals: **lane1 = 341, lane2 = 411** (lane1 cap-hitters ⊂ lane2 cap-hitters; union = 411 records). Lane3 = 0 (never reviewed enough to cap — see FLAG-C).

**Contract compliance: 749/752 lane-instances PASS.** All 341 lane1 cap-hits carry `final_cursor`+`audit_needed`+`audit_marker:"R15 treatment audit required"`. **3 lane2 cap-hits VIOLATE** (`cap_hit:true`, `reviewed:25=cap`, `audit_needed:true`, but `final_cursor:null`):

- **City of Ontario v. Quon** — lane2_top_cited
- **United States v. Anchondo** — lane2_top_cited
- **Vega v. Tekoh** — lane2_top_cited

→ **FLAG-A** (3 records). Consequence: these 3 cannot be resumed from their cap point; audit-flag itself is set, only the cursor is lost.

Full rosters (compact) are in the Appendix; the machine predicate is `derivation[lane].cap_hit == true`.

---

## 4. Random sample (30, stratified by court_level × roster position)

Seeded stratified draw (scotus 22 / coa 5 / state 2 / other 1). Verdict per row = 3 lanes present w/ terminal status ∧ all edges `proposed:true`+cluster_id ∧ cap lanes carry cursor ∧ as_of present.

**29 COHERENT / 1 FLAG.** The single FLAG independently re-surfaced a §3 violation:
- **City of Ontario v. Quon** [scotus] — lane2 cap_hit w/ null final_cursor (= FLAG-A).

Representative COHERENT rows: Arizona v. Johnson, Ashcraft v. Tennessee, Byars v. United States (39 edges/26 neg), Carpenter v. United States, Florida v. Harris, McNeil v. Wisconsin, United States v. Calandra, French v. Merrill [coa], United States v. Gastiaburo [coa], State v. Mansor [state], State v. Tarantino [state], Kalkines v. United States [other]. All: 3 lanes terminal, `proposed:true`, cluster_id present, as_of sane (`as_of_content ≤ as_of_treatment`, none future).

Corpus-wide sanity (all 456 derived): as_of problems **0**, missing lane **0**, non-terminal lane **0**.

---

## 5. Pre-seeded rows (A13 legacy migration) — provenance

Both principal-holding rows carry the migration stamp: `provenance.warnings = ["pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm"]` and `field_provenance` on `treatment.field_i_validity` (verifier `S2-BUILDER-AUTHORING`) + `point_overrides` (src `"S2 treatment derivation proposed only"`). **Provenance stamped: PASS. Overrides carried: yes, but structurally malformed —**

- **New York v. Belton** — override `point=search.vehicle.sia-recent-occupant`, Field-I `superseded`. `by = "[[Arizona v. Gant]]"` — a **stringified nested list, not an array of controlling-case objects**; Gant's cluster_id **145887** (named explicitly in R5's worked specimen) and cite are absent from the `by` object (`by_cite` sits as a sibling non-schema field). → **FLAG-B**.
- **United States v. Smith (2024)** — override `point=search.warrant.geofence-general-warrant`, Field-I `caution`. `by = "[[Chatrie v. United States]]"` (same corruption); additionally override `field_ii = ""` (empty verb). → **FLAG-B**.

The 10 legacy-`limited`→`caution` migration rows use well-formed `by[]` objects but with `cluster_id:null` / `cite:null` (name-only controlling case) → **FLAG-D**, not FLAG-B.

---

## 6. Systemic patterns

- **SYSTEMIC-1 (= FLAG-C) — lane3_recency inert corpus-wide.** The recency lane issued its search on all 456 derived records (455 `treatment.lane3_recency.search` calls, HTTP 200) but `reviewed=0` / `proposed_negative_events=0` / `cap_hit=false` on **every** record, including current-term and heavily-cited cases (Terry, Carpenter, Vega v. Tekoh, Chatrie). No `lane3` triage/hit_text/page steps exist in the journal — nothing was ever read or classified. The lane is nonetheless marked `complete`. This directly undercuts R6/A9/A11's stated rationale that lane 3 is the **only** lane structurally capable of catching fresh overrulings (lanes 1–2 are blind to near-zero-citation recent cases). Trail is honestly recorded (not silent), but substantive coverage of the recency lane is nil across the corpus.
- **SYSTEMIC-2 (= FLAG-D) — migration controlling-case identity unresolved.** All 12 migration/pre-seed overrides and all 20 `migration:*` edges name the controlling case by NAME only (`cluster_id:null`, `cite:null`), whereas R5's Check requires "every override names a controlling case with a cluster_id + Field-II verb + as_of." Verb + as_of are present; cluster_id/cite are not. The controlling cases (Mapp, Katz, Gant, Montejo, Warden v. Hayden, Horton, Miranda, Bagley, Acevedo, Seibert, Pearson, Monell, Salvucci, Rakas, Gates) are almost all in-corpus and trivially resolvable. Lane-derived edges are unaffected (all 14,306 carry cluster_id).
- **OBSERVATION (non-flag) — lane2 `proposed_negative_events` ≈ `reviewed`.** The top-cited lane counts nearly every reviewed hit as a "proposed_negative_event" (10,417 of 10,613). This over-proposes rather than under-proposes; since all edges are `proposed:true` and S9 filters, it is conservative and not a safety defect, but the counter is mislabeled for a non-negative-scan lane.

---

## 7. Flag summary

| Flag | Class | Instances | Records |
|---|---|---:|---|
| **FLAG-A** | F-S2-09 cap contract: lane2 `cap_hit:true` w/ `final_cursor:null` | 3 | City of Ontario v. Quon; United States v. Anchondo; Vega v. Tekoh |
| **FLAG-B** | Pre-seed `point_override.by[]` structural corruption (stringified nested list; no ctrl cluster_id; Smith override `field_ii=""`) | 2 | New York v. Belton; United States v. Smith (2024) |
| **FLAG-C** | lane3_recency inert corpus-wide (searched, reviewed 0, marked complete) — R6/A11 undercut | systemic | 456 derived |
| **FLAG-D** | Migration/pre-seed controlling-case `cluster_id`/`cite` absent (R5 Check deviation) | systemic | 18 (12 overrides + 20 edges) |

**PASS findings (for the record):** all 14,326 edges `proposed:true` (0 auto-applied — S9 boundary HELD); 749/752 cap-lanes contract-compliant; 456/456 derived records have 3 terminal lanes; as_of sanity 0 problems; migration provenance stamped on all 18 non-good composites + both pre-seed rows; triage read-decisions journaled with reason; lane-derived edges 14,306/14,306 carry cluster_id.

TREATMENT AUDIT: 4 FLAGS

---

## Appendix — full cap-hit rosters (F-S2-09 audit_needed set on each)

### lane1_negative — 341 records (all contract-compliant: final_cursor + audit_needed present)

Abel v. United States; Adams v. Williams; Agnello v. United States; Aguilar v. Texas; Alabama v. White; Alderman v. United States; Almeida-Sanchez v. United States; Andresen v. Maryland; Arizona v. Evans; Arizona v. Fulminante; Arizona v. Gant; Arizona v. Hicks; Arizona v. Johnson; Arizona v. Mauro; Arizona v. Roberson; Ashcraft v. Tennessee; Atwater v. City of Lago Vista; Banks v. Dretke; Beckwith v. United States; Berger v. New York; Berkemer v. McCarty; Bivens v. Six Unknown Named Agents; Board of Education v. Earls; Boyd v. United States; Brady v. Maryland; Brendlin v. California; Brewer v. Williams; Brigham City v. Stuart; Brinegar v. United States; Brosseau v. Haugen; Brower v. County of Inyo; Brown v. Illinois; Brown v. Mississippi; Brown v. Texas; Bumper v. North Carolina; Byars v. United States; Cady v. Dombrowski; California v. Acevedo; California v. Beheler; California v. Carney; California v. Ciraolo; California v. Greenwood; California v. Hodari D.; California v. Prysock; Camara v. Municipal Court; Cardwell v. Lewis; Carpenter v. United States; Carroll v. United States; Chambers v. Florida; Chambers v. Maroney; Chandler v. Miller; Chapman v. United States (1961); Chavez v. Martinez; Chimel v. California; City and County of San Francisco v. Sheehan; City of Canton v. Harris; City of Indianapolis v. Edmond; Colorado v. Bertine; Colorado v. Connelly; Colorado v. Spring; Cone v. Bell; Connecticut v. Barrett; Coolidge v. New Hampshire; Cooper v. California; Corley v. United States; County of Riverside v. McLaughlin; County of Sacramento v. Lewis; Cupp v. Murphy; Dalia v. United States; Davis v. Mississippi; Delaware v. Prouse; Devenpeck v. Alford; Dickerson v. United States; District of Columbia v. Wesby; Donovan v. Dewey; Doyle v. Ohio; Draper v. United States; Duckworth v. Eagan; Dunaway v. New York; Edwards v. Arizona; Elkins v. United States; Escobedo v. Illinois; Fare v. Michael C; Ferguson v. City of Charleston; Florida v. Bostick; Florida v. Harris; Florida v. Jardines; Florida v. Jimeno; Florida v. Royer; Florida v. Wells; Foster v. California; Franks v. Delaware; Frazier v. Cupp; Gardner v. Broderick; Garrity v. New Jersey; Georgia v. Randolph; Gerstein v. Pugh; Giglio v. United States; Gilbert v. California; Go-Bart Importing Co. v. United States; Gouled v. United States; Graham v. Connor; Griffin v. Wisconsin; Groh v. Ramirez; Hampton v. United States; Harlow v. Fitzgerald; Harris v. New York; Harris v. United States (1968); Hayes v. Florida; Haynes v. Washington; Heck v. Humphrey; Heien v. North Carolina; Henry v. United States (1959); Herring v. United States; Hester v. United States; Hiibel v. Sixth Judicial Dist. Court; Hill v. California; Hoffa v. United States; Hope v. Pelzer; Horton v. California; Howes v. Fields; Hudson v. Michigan; Hudson v. Palmer; Illinois v. Andreas; Illinois v. Caballes; Illinois v. Gates; Illinois v. Krull; Illinois v. Lafayette; Illinois v. McArthur; Illinois v. Perkins; Illinois v. Rodriguez; Illinois v. Wardlow; Immigration & Naturalization Service v. Lopez-Mendoza; Jacobson v. United States; Johnson v. United States; Jones v. United States; Katz v. United States; Kentucky v. King; Kingsley v. Hendrickson; Kirby v. Illinois; Kisela v. Hughes; Knowles v. Iowa; Kolender v. Lawson; Kuhlmann v. Wilson; Kyles v. Whitley; Kyllo v. United States; Lefkowitz v. Turley; Lego v. Twomey; Lo-Ji Sales, Inc. v. New York; Lynumn v. Illinois; Maine v. Moulton; Malley v. Briggs; Mallory v. United States; Malloy v. Hogan; Mancusi v. DeForte; Manson v. Brathwaite; Mapp v. Ohio; Marbury v. Madison; Marshall v. Barlow's Inc; Maryland v. Buie; Maryland v. Dyson; Maryland v. Garrison; Maryland v. King; Maryland v. Macon; Maryland v. Pringle; Maryland v. Shatzer; Maryland v. Wilson; Massachusetts v. Sheppard; Massiah v. United States; Mathews v. United States; Mathis v. United States (1968); McNabb v. United States; McNeil v. Wisconsin; Michigan Dept. of State Police v. Sitz; Michigan v. Chesternut; Michigan v. DeFillippo; Michigan v. Jackson; Michigan v. Long; Michigan v. Mosley; Michigan v. Summers; Michigan v. Tucker; Michigan v. Tyler; Mincey v. Arizona; Minnesota v. Dickerson; Minnesota v. Olson; Minnick v. Mississippi; Miranda v. Arizona; Missouri v. McNeely; Missouri v. Seibert; Monell v. Department of Social Services; Monroe v. Pape; Montejo v. Louisiana; Mooney v. Holohan; Moran v. Burbine; Muehler v. Mena; Mullenix v. Luna; Murray v. United States; Napue v. Illinois; Nardone v. United States; National Treasury Employees Union v. Von Raab; Navarette v. California; Neil v. Biggers; New Jersey v. T.L.O.; New York v. Belton; New York v. Burger; New York v. Class; New York v. Harris; New York v. Quarles; Nix v. Williams; North Carolina v. Butler; O'Connor v. Ortega; Ohio v. Robinette; Oliver v. United States; Olmstead v. United States; Oregon v. Bradshaw; Oregon v. Elstad; Oregon v. Mathiason; Ornelas v. United States; Orozco v. Texas; Patterson v. Illinois; Payton v. New York; Pearson v. Callahan; Pembaur v. City of Cincinnati; Pennsylvania Board of Probation and Parole v. Scott; Pennsylvania v. Labron; Pennsylvania v. Mimms; Pennsylvania v. Muniz; Peters v. New York; Plumhoff v. Rickard; Preston v. United States; Rakas v. Illinois; Rawlings v. Kentucky; Rhode Island v. Innis; Richards v. Wisconsin; Rodriguez v. United States; Rogers v. Richmond; Rothgery v. Gillespie County; Sabbath v. United States; Samson v. California; Schmerber v. California; Schneckloth v. Bustamonte; Scott v. Harris; Screws v. United States; See v. City of Seattle; Segura v. United States; Sgro v. United States; Sherman v. United States; Sibron v. New York; Silverman v. United States; Silverthorne Lumber Co. v. United States; Simmons v. United States; Skinner v. Railway Labor Executives' Ass'n; Smith v. Illinois; Smith v. Maryland; Soldal v. Cook County; Sorrells v. United States; South Dakota v. Opperman; Spano v. New York; Spinelli v. United States; Stanford v. Texas; Stansbury v. California; Steagald v. United States; Steele v. United States; Stoner v. California; Stovall v. Denno; Strickler v. Greene; Taylor v. Alabama; Tennessee v. Garner; Terry v. Ohio; Texas v. Brown; Texas v. Cobb; Thompson v. Keohane; Thornton v. United States; Townsend v. Sain; United States v. Agurs; United States v. Arvizu; United States v. Ash; United States v. Bagley; United States v. Biswell; United States v. Brignoni-Ponce; United States v. Calandra; United States v. Ceccolini; United States v. Chadwick; United States v. Classic; United States v. Cortez; United States v. Crews; United States v. Drayton; United States v. Dunn; United States v. Edwards; United States v. Gouveia; United States v. Harris (1971); United States v. Havens; United States v. Henry; United States v. Hensley; United States v. Jacobsen; United States v. Janis; United States v. Johns; United States v. Jones; United States v. Karo; United States v. Knights; United States v. Knotts; United States v. Leon; United States v. Martinez-Fuerte; United States v. Matlock; United States v. Mendenhall; United States v. Miller; United States v. Montoya de Hernandez; United States v. Patane; United States v. Payner; United States v. Place; United States v. Ramsey; United States v. Robinson; United States v. Ross; United States v. Russell; United States v. Salvucci; United States v. Santana; United States v. Sharpe; United States v. Sokolow; United States v. Ventresca; United States v. Wade; United States v. Watson; Vale v. Louisiana; Vernonia School District 47J v. Acton; Virginia v. Moore; Walder v. United States; Walter v. United States; Warden v. Hayden; Weeks v. United States; Welsh v. Wisconsin; White v. Pauly; Whiteley v. Warden; Whren v. United States; Wilson v. Arkansas; Wilson v. Layne; Winston v. Lee; Wolf v. Colorado; Wong Sun v. United States; Wyoming v. Houghton; Yarborough v. Alvarado; Ybarra v. Illinois; Zurcher v. Stanford Daily

### lane2_top_cited — 411 records (3 non-compliant, bolded in §3: City of Ontario v. Quon, United States v. Anchondo, Vega v. Tekoh)

Abel v. United States; Adams v. Williams; Agnello v. United States; Aguilar v. Texas; Alabama v. White; Alderman v. United States; Almeida-Sanchez v. United States; Andresen v. Maryland; Arizona v. Evans; Arizona v. Fulminante; Arizona v. Gant; Arizona v. Hicks; Arizona v. Johnson; Arizona v. Mauro; Arizona v. Roberson; Arkansas v. Sullivan; Ashcraft v. Tennessee; Ashcroft v. al-Kidd; Atwater v. City of Lago Vista; Bailey v. United States; Banks v. Dretke; Beckwith v. United States; Beecher v. Alabama; Benn v. Lambert; Berger v. New York; Berghuis v. Thompkins; Berkemer v. McCarty; Birchfield v. North Dakota; Bivens v. Six Unknown Named Agents; Board of Education v. Earls; Bobby v. Dixon; Bond v. United States; Boyd v. United States; Brady v. Maryland; Brendlin v. California; Brewer v. Williams; Brigham City v. Stuart; Brinegar v. United States; Brosseau v. Haugen; Brower v. County of Inyo; Brown v. Illinois; Brown v. Mississippi; Brown v. Texas; Bumper v. North Carolina; Byars v. United States; Byrd v. United States; Cady v. Dombrowski; California v. Acevedo; California v. Beheler; California v. Carney; California v. Ciraolo; California v. Greenwood; California v. Hodari D.; California v. Prysock; Camara v. Municipal Court; Caniglia v. Strom; Cardwell v. Lewis; Carpenter v. United States; Carroll v. United States; Chambers v. Florida; Chambers v. Maroney; Chandler v. Miller; Chapman v. United States (1961); Chavez v. Martinez; Chimel v. California; City and County of San Francisco v. Sheehan; City of Canton v. Harris; City of Indianapolis v. Edmond; City of Los Angeles v. Patel; City of Ontario v. Quon; Collins v. Virginia; Colorado v. Bertine; Colorado v. Connelly; Colorado v. Spring; Cone v. Bell; Connally v. Georgia; Connecticut v. Barrett; Connick v. Thompson; Coolidge v. New Hampshire; Cooper v. California; Corley v. United States; County of Riverside v. McLaughlin; County of Sacramento v. Lewis; Cupp v. Murphy; Dalia v. United States; Davis v. Mississippi; Delaware v. Prouse; Devenpeck v. Alford; Dickerson v. United States; District of Columbia v. Wesby; Donovan v. Dewey; Dow Chemical Co. v. United States; Doyle v. Ohio; Draper v. United States; Duckworth v. Eagan; Dunaway v. New York; Edwards v. Arizona; Elkins v. United States; Escobedo v. Illinois; Fare v. Michael C; Fellers v. United States; Ferguson v. City of Charleston; Fernandez v. California; Flippo v. West Virginia; Florence v. County of Burlington; Florida v. Bostick; Florida v. Harris; Florida v. J.L.; Florida v. Jardines; Florida v. Jimeno; Florida v. Meyers; Florida v. Powell; Florida v. Riley; Florida v. Royer; Florida v. Wells; Florida v. White; Foster v. California; Franks v. Delaware; Frazier v. Cupp; Gardner v. Broderick; Garrity v. New Jersey; Georgia v. Randolph; Gerstein v. Pugh; Giglio v. United States; Gilbert v. California; Go-Bart Importing Co. v. United States; Gooding v. United States; Gouled v. United States; Graham v. Connor; Griffin v. Wisconsin; Groh v. Ramirez; Hampton v. United States; Harlow v. Fitzgerald; Harris v. New York; Harris v. United States (1968); Hayes v. Florida; Haynes v. Washington; Heck v. Humphrey; Heien v. North Carolina; Henry v. United States (1959); Herring v. United States; Hester v. United States; Hiibel v. Sixth Judicial Dist. Court; Hill v. California; Hoffa v. United States; Hope v. Pelzer; Horton v. California; Howes v. Fields; Hudson v. Michigan; Hudson v. Palmer; Illinois v. Andreas; Illinois v. Caballes; Illinois v. Gates; Illinois v. Krull; Illinois v. Lafayette; Illinois v. Lidster; Illinois v. McArthur; Illinois v. Perkins; Illinois v. Rodriguez; Illinois v. Wardlow; Immigration & Naturalization Service v. Lopez-Mendoza; J.D.B. v. North Carolina; Jacobson v. United States; James v. Illinois; Johnson v. United States; Jones v. United States; Kansas v. Glover; Katz v. United States; Kaupp v. Texas; Kentucky v. King; Kingsley v. Hendrickson; Kirby v. Illinois; Kirk v. Louisiana; Kisela v. Hughes; Knowles v. Iowa; Kolender v. Lawson; Kuhlmann v. Wilson; Kyles v. Whitley; Kyllo v. United States; LaChance v. Erickson; Lefkowitz v. Turley; Lego v. Twomey; Lewis v. United States (1966); Lo-Ji Sales, Inc. v. New York; Los Angeles County v. Rettele; Lynumn v. Illinois; Maine v. Moulton; Malley v. Briggs; Mallory v. United States; Malloy v. Hogan; Mancusi v. DeForte; Manson v. Brathwaite; Mapp v. Ohio; Marbury v. Madison; Marshall v. Barlow's Inc; Maryland v. Buie; Maryland v. Dyson; Maryland v. Garrison; Maryland v. King; Maryland v. Macon; Maryland v. Pringle; Maryland v. Shatzer; Maryland v. Wilson; Massachusetts v. Sheppard; Massiah v. United States; Mathews v. United States; Mathis v. United States (1968); McNabb v. United States; McNeil v. Wisconsin; Messerschmidt v. Millender; Michigan Dept. of State Police v. Sitz; Michigan v. Chesternut; Michigan v. Clifford; Michigan v. DeFillippo; Michigan v. Fisher; Michigan v. Jackson; Michigan v. Long; Michigan v. Mosley; Michigan v. Summers; Michigan v. Thomas; Michigan v. Tucker; Michigan v. Tyler; Mincey v. Arizona; Minnesota v. Carter; Minnesota v. Dickerson; Minnesota v. Olson; Minnick v. Mississippi; Miranda v. Arizona; Missouri v. McNeely; Missouri v. Seibert; Mitchell v. Wisconsin; Monell v. Department of Social Services; Monroe v. Pape; Montejo v. Louisiana; Mooney v. Holohan; Moran v. Burbine; Muehler v. Mena; Mullenix v. Luna; Murray v. United States; Napue v. Illinois; Nardone v. United States; National Treasury Employees Union v. Von Raab; Navarette v. California; Neil v. Biggers; New Jersey v. T.L.O.; New York v. Belton; New York v. Burger; New York v. Class; New York v. Harris; New York v. Quarles; Nix v. Williams; North Carolina v. Butler; O'Connor v. Ortega; Ohio v. Robinette; Oliver v. United States; Olmstead v. United States; Oregon v. Bradshaw; Oregon v. Elstad; Oregon v. Mathiason; Ornelas v. United States; Orozco v. Texas; Patterson v. Illinois; Payton v. New York; Pearson v. Callahan; Pembaur v. City of Cincinnati; Pennsylvania Board of Probation and Parole v. Scott; Pennsylvania v. Bruder; Pennsylvania v. Labron; Pennsylvania v. Mimms; Pennsylvania v. Muniz; Perry v. New Hampshire; Peters v. New York; Plumhoff v. Rickard; Preston v. United States; Rakas v. Illinois; Rawlings v. Kentucky; Rhode Island v. Innis; Richards v. Wisconsin; Rivas-Villegas v. Cortesluna; Rodriguez v. United States; Rogers v. Richmond; Rothgery v. Gillespie County; Ryburn v. Huff; Sabbath v. United States; Safford Unified School District v. Redding; Salinas v. Texas; Samson v. California; Schmerber v. California; Schneckloth v. Bustamonte; Scott v. Harris; Screws v. United States; See v. City of Seattle; Segura v. United States; Sgro v. United States; Sherman v. United States; Shipley v. California; Sibron v. New York; Silverman v. United States; Silverthorne Lumber Co. v. United States; Simmons v. United States; Skinner v. Railway Labor Executives' Ass'n; Smith v. Cain; Smith v. Illinois; Smith v. Maryland; Soldal v. Cook County; Sorrells v. United States; South Dakota v. Opperman; Spano v. New York; Spinelli v. United States; Stanford v. Texas; Stansbury v. California; State v. Mansor; Steagald v. United States; Steele v. United States; Stoner v. California; Stovall v. Denno; Strickler v. Greene; Taylor v. Alabama; Taylor v. Riojas; Tennessee v. Garner; Terry v. Ohio; Texas v. Brown; Texas v. Cobb; Thompson v. Keohane; Thompson v. Louisiana; Thornton v. United States; Torres v. Madrid; Townsend v. Sain; Turner v. United States; United States v. Agurs; United States v. Anchondo; United States v. Arvizu; United States v. Ash; United States v. Bagley; United States v. Banks; United States v. Biswell; United States v. Brignoni-Ponce; United States v. Calandra; United States v. Ceccolini; United States v. Chadwick; United States v. Classic; United States v. Conner; United States v. Cortez; United States v. Crews; United States v. Drayton; United States v. Dunn; United States v. Edwards; United States v. Flores-Montano; United States v. Gooch; United States v. Gouveia; United States v. Grubbs; United States v. Harris (1971); United States v. Havens; United States v. Henry; United States v. Hensley; United States v. Jacobsen; United States v. Janis; United States v. Johns; United States v. Jones; United States v. Karo; United States v. Knights; United States v. Knotts; United States v. Leary; United States v. Leon; United States v. Martinez-Fuerte; United States v. Matlock; United States v. Mendenhall; United States v. Miller; United States v. Montoya de Hernandez; United States v. Padilla; United States v. Patane; United States v. Payner; United States v. Place; United States v. Ramirez; United States v. Ramsey; United States v. Rideau; United States v. Robinson; United States v. Ross; United States v. Russell; United States v. Salvucci; United States v. Santana; United States v. Sharpe; United States v. Sokolow; United States v. Van Leeuwen; United States v. Ventresca; United States v. Vinton; United States v. Wade; United States v. Watson; Utah v. Strieff; Vale v. Louisiana; Vega v. Tekoh; Vernonia School District 47J v. Acton; Virginia v. Moore; Walder v. United States; Walter v. United States; Warden v. Hayden; Wearry v. Cain; Weeks v. United States; Welsh v. Wisconsin; White v. Pauly; Whiteley v. Warden; Whren v. United States; Wilson v. Arkansas; Wilson v. Layne; Winston v. Lee; Wolf v. Colorado; Wong Sun v. United States; Wyoming v. Houghton; Yarborough v. Alvarado; Ybarra v. Illinois; Zurcher v. Stanford Daily
