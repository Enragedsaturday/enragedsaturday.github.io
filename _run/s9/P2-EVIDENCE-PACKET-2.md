# P2 Evidence Packet 2 — reconciliation discordance-candidates (112 + 1 supplementary)

**Lane:** S9 P2 evidence-prep (`claude-opus-4-8`). Evidence only — NO rulings, NO edits, NO re-keys. The orchestrator adjudicates.

**TIER PROBE: NOT TRIGGERED — 0 live CourtListener calls.** Every candidate resolved from cached opinion text (`/Users/johngalt/cssi-lake/cache/text/<lead>.txt`) + the known-FP register, per the cached-first discipline. No throttle risk incurred; `_run/s9/p2-evidence-cl-calls.log` unwritten (no calls). If the orchestrator wants the correct Chapman merits cluster/lead resolved live, that is a separate ~1-2 call job requiring a fresh tier probe.

## Bucket-disposition summary

| recommended_disposition | count | buckets |
|---|---|---|
| COSMETIC-caption-variance | 76 | 74 A + Go-Bart, Marcus (B) |
| CORRECTLY-KEYED | 16 | 13 C + Davis-2011, Davis-1994, Demesme (B) |
| COSMETIC-no-printed-caption | 6 | Camara, Flippo, Mathis-1968, Patterson, Larson, Anchondo (B) |
| N-BLIND-UNREAD | 10 | 10 D-doctrine |
| ALREADY-RESOLVED | 4 | 4 D-doctrine (prior P2 arc) |
| **MIS-KEY (supplementary)** | 1 | chapman-v-california (NOT among the 112) |

**Headline:** zero confirmed mis-keys among the 112. All 13 C-bucket 'identity-absent' flags are Thread-N blind-read artifacts (case IS in the correctly-resolved lead). All 11 B-bucket suspect-captions resolve benign; the 3 register items (Davis pair, Flippo, Anchondo) all CONFIRM (not assumed). 1 genuine coverage-gap (INS v. Delgado) already escalated. 1 supplementary MIS-KEY (Chapman) confirmed per task directive, outside the 112.

---

## A — benign-caption (74) → COSMETIC-caption-variance

≥50% expected-party-token coverage in the blind parties_in_text (correct case, caption/styling variance — state-court caption for a SCOTUS grant, in-rem caption, consolidated caption, or body-only 'petitioner/respondent'). Sampled 10 across the bucket by reading the cached lead head — **all 10 confirmed the correct case**; no spot-check failed, so no individual CL follow-up needed. R5: cosmetic → reconcile freely.

- **A Quantity of Copies of Books v. Kansas** — SPOT-VERIFIED (lead 9422858): Brennan; obscene-book seizure, Kansas — correct → COSMETIC-caption-variance
- **Berkemer v. McCarty** — SPOT-VERIFIED (lead 9429728): Marshall; Miranda + traffic misdemeanor — correct → COSMETIC-caption-variance
- **Frazier v. Cupp** — SPOT-VERIFIED (lead 107913): Marshall; Oregon confession/co-defendant ruse — correct (lead==cluster, genuine) → COSMETIC-caption-variance
- **Illinois v. Andreas** — SPOT-VERIFIED (lead 9429344): Burger; reopening sealed contraband container — correct → COSMETIC-caption-variance
- **Kolender v. Lawson** — SPOT-VERIFIED (lead 9429183): O'Connor; vagueness loitering-ID statute — correct → COSMETIC-caption-variance
- **Kuhlmann v. Wilson** — SPOT-VERIFIED (lead 9430620): Powell; passive jailhouse informant — correct → COSMETIC-caption-variance
- **Massachusetts v. Sheppard** — SPOT-VERIFIED (lead 111263): White; warrant (Leon companion) — correct (lead==cluster, genuine) → COSMETIC-caption-variance
- **Michigan v. Tucker** — SPOT-VERIFIED (lead 9425753): Rehnquist; Miranda-derived witness testimony — correct → COSMETIC-caption-variance
- **Peters v. New York** — SPOT-VERIFIED (lead 9423756): Warren; Terry companion, frisk — correct → COSMETIC-caption-variance
- **Thompson v. Louisiana** — SPOT-VERIFIED (lead 111282): Per Curiam; murder-scene search, La. — correct (lead==cluster, genuine) → COSMETIC-caption-variance

Remaining 64 A rows: bucket-level cosmetic (blind parties_in_text already carries the expected caption tokens); not individually spot-checked.

## B — suspect-caption (11) → resolved from cached text + FP register (0 CL)

- **Camara v. Municipal Court** (lead 107473) → **COSMETIC-no-printed-caption**. White; municipal housing-inspection administrative-warrant substance matches Camara 387 U.S. 523; body uses appellant/appellee (no printed caption). cluster==lead 107473 but cached text is genuinely Camara.
- **Davis v. United States (2011)** (lead 9441776) → **CORRECTLY-KEYED**. Alito; 'passenger Willie Davis'; 'binding appellate precedent...not subject to exclusionary rule' = Davis good-faith (564 U.S. 229). Register-CONFIRMED (218926/9441776). Blind 'no party names' + holding-overlap-zero were read artifacts. NOTE: triage citation '565 U.S. 1100' looks like a cert/misc page vs reporter 564 U.S. 229 — citation-string metadata nuance only, identity is correct.
- **Davis v. United States** (lead 9433017) → **CORRECTLY-KEYED**. O'Connor; 'Maybe I should talk to a lawyer' = Davis 1994 ambiguous-invocation (512 U.S. 452). Register-CONFIRMED (117863/9433017). NOTE: triage citation '513 U.S. 1008' vs reporter 512 U.S. 452 — citation-string metadata nuance only, identity correct.
- **Flippo v. West Virginia** (lead 1854815) → **COSMETIC-no-printed-caption**. Per Curiam; 'homicide crime scene' warrantless search = Flippo 528 U.S. 11 (no murder-scene exception). Register FP-suspicion CONFIRMED as false positive: record is correctly keyed. cluster==lead 1854815, genuine.
- **Go-Bart Importing Co. v. United States** (lead 101643) → **COSMETIC-caption-variance**. Butler; 'Gowen, Bartels and others are defendants' — the company Go-Bart = Gowen+Bartels; printed parties are the individuals. Genuine Go-Bart 282 U.S. 344. cluster==lead 101643.
- **Marcus v. Search Warrant** (lead 9422285) → **COSMETIC-caption-variance**. Brennan; Missouri obscene-publication seizure; appellants printed as Kansas City News Distributors et al. In-rem style caption ('v. Search Warrant'). Genuine Marcus 367 U.S. 717.
- **Mathis v. United States (1968)** (lead 9423682) → **COSMETIC-no-printed-caption**. Black; false-claims/IRS custodial interrogation, Miranda applies = Mathis 391 U.S. 1. Petitioner unnamed in body; substance matches. 9.5KB genuine short opinion.
- **Patterson v. Illinois** (lead 9431404) → **COSMETIC-no-printed-caption**. White; post-indictment interrogation, 6th Am right to counsel, 'Vice Lords' = Patterson 487 U.S. 285. Body uses petitioner/respondent; substance matches.
- **State v. Demesme** (lead 4848796) → **CORRECTLY-KEYED**. La. writ denial ('Writ denied.', writ of cert to 4th Cir, Parish of Orleans) = State v. Demesme 228 So.3d 1206. Lead IS the correct disposition. CONTENT-GAP: the famous 'lawyer dog' is Crichton, J. concurring, ABSENT from the 197B lead — already filed to P2 via stub triage; teaching-support gap, not a mis-key.
- **State v. Larson** (lead 1187724) → **COSMETIC-no-printed-caption**. Deits, C.J. (Or. App.); state seeks reversal of suppression of warrant-seized evidence = State v. Larson 159 Or.App. 34. Oregon 'state v. defendant' caption; defendant name not in body. cluster==lead 1187724.
- **United States v. Anchondo** (lead 758111) → **COSMETIC-no-printed-caption**. Tacha, C.J. (10th Cir); cocaine possession, I-25 checkpoint, passenger Garcia = United States v. (Erick) Anchondo 156 F.3d 1043. Register-CONFIRMED (not a fabrication/misspelling risk). Defendant unnamed in body. cluster==lead 758111.

## C — identity-absent (13) → all CORRECTLY-KEYED (0 CL; cached lead text carries the named party)

For each: cluster→lead was already the correctly-resolved sub-opinion id in the triage; the named case appears in the cached lead text (party-hit counts below). The 'identity-absent' + 'presence-absence' flags are Thread-N blind-read artifacts — three (Bryan County, Fernandez, Jacobson) even had EMPTY blind parties_in_text, i.e. the blind extractor returned nothing while the caption is plainly present. Cluster-collision watch cases (Lange 4894407→4698186, Hay 9485331→9951944, Robinson 4340460→9871494) confirmed to resolve to the RIGHT opinion (cluster≠lead, correct). No live L3 resolution required.

- **Arizona v. Gant** (lead 9435359, party x51) → **CORRECTLY-KEYED**. Stevens; 'Rodney Gant' — SIA-vehicle. Blind identity-absent = read artifact.
- **Berghuis v. Thompkins** (lead 6680916, party x92) → **CORRECTLY-KEYED**. Kennedy; 'Van Chester Thompkins...respondent; Berghuis...petitioner' printed verbatim.
- **Board of County Commissioners of Bryan County v. Brown** (lead 9842136, party x23) → **CORRECTLY-KEYED**. O'Connor; 'Respondent Jill Brown...petitioner Bryan County' printed. Blind parties_in_text was EMPTY = extractor miss.
- **California v. Carney** (lead 9430011, party x19) → **CORRECTLY-KEYED**. Burger; 'respondent, Charles Carney'...motor home — correct.
- **Colorado v. Spring** (lead 9430793, party x84) → **CORRECTLY-KEYED**. Powell; 'respondent John Leroy Spring' — correct.
- **Corley v. United States** (lead 145888, party x49) → **CORRECTLY-KEYED**. SCOTUS slip op; 'JOHNNIE CORLEY, PETITIONER v. UNITED STATES' in syllabus. cluster==lead 145888 but text genuine.
- **Fernandez v. California** (lead 9798884, party x16) → **CORRECTLY-KEYED**. Alito; 'petitioner Walter Fernandez' — correct. Blind parties_in_text was EMPTY = extractor miss.
- **Florence v. County of Burlington** (lead 626454, party x30) → **CORRECTLY-KEYED**. SCOTUS slip op; 'Albert W. Florence...v. Board of Chosen Freeholders...Burlington' in syllabus. cluster==lead 626454, genuine.
- **Florida v. Harris** (lead 820744, party x57) → **CORRECTLY-KEYED**. SCOTUS slip op; 'FLORIDA...v. CLAYTON HARRIS' in syllabus. cluster==lead 820744, genuine.
- **Jacobson v. United States** (lead 9432514, party x8) → **CORRECTLY-KEYED**. White; 'petitioner Keith Jacobson' — entrapment. Blind parties_in_text was EMPTY = extractor miss.
- **Lange v. California** (lead 4698186, party x61) → **CORRECTLY-KEYED**. SCOTUS slip op; 'Arthur Gregory Lange...v. California'. cluster 4894407 -> resolved lead 4698186 (cluster!=lead, correctly resolved).
- **United States v. Hay** (lead 9951944, party x84) → **CORRECTLY-KEYED**. 10th Cir; 'Mr. Hay' (Bruce L. Hay), geofence 2024. cluster 9485331 -> lead 9951944 (correctly resolved).
- **United States v. Robinson (4th Cir. en banc)** (lead 9871494, party x44) → **CORRECTLY-KEYED**. Niemeyer (4th Cir en banc); 'Shaquille Robinson' frisked. cluster 4340460 -> lead 9871494 (correctly resolved).

## D — doctrine (14) → 10 N-BLIND-UNREAD + 4 ALREADY-RESOLVED (0 CL)

Coverage/split discordances (blind doctrine read vs build case-set). Cross-refs: `reconciliation.jsonl` discordance_detail, `_run/s6-coverage-ledger.json`, and the prior P2 doctrine arc (JOURNAL: 16 items ruled, queue CLEARED — commits 1c4ba2d, a319410, 6be84df). **All 13 over-inclusion-candidate case pages EXIST** (Kalkines, Hanapel, Perez-Rodriguez, Reddick, Wilson, Carter, Amos, Lopez-Mendoza, Calandra, Leary, Mathis, Evans + others) — so every 'oi' is benign N-blindness, not a coverage gap. **Only genuine coverage gap: INS v. Delgado** (no lake file, no content) — already escalated. No live split-currency check performed: the split calls here were adjudicated in the prior arc; splits are re-derivations of closed items.

- **Public-Employee Compelled Statements (Garrity)** → **N-BLIND-UNREAD**. N-only-split (Kalkines 'subjective-belief-of-termination + objectively-reasonable?' refinement); no named circuit positions = not a live circuit split. oi Kalkines page EXISTS, homed Key-Progeny. Benign N framing divergence.
- **Entrapment** → **ALREADY-RESOLVED**. N-only-split: (1) subjective vs objective test [taught], (2) outrageous-government-conduct defense viability. Outrageous-conduct prong ESCALATED to R7 absence sweep in prior P2 doctrine arc (commit 1c4ba2d). oi Hanapel + Perez-Rodriguez pages EXIST, homed Key. Do not re-litigate.
- **Aerial & Enhanced Surveillance** → **N-BLIND-UNREAD**. N-only-split (prolonged pole-camera / persistent aerial = search post-Carpenter). Real live divergence (Moore-Bush 1st-Cir en-banc 3-3 / Tuggle 7th) but page teaches it; no coverage gap. Prior-arc 'divergences taught' DISMISS class. If page exposition thin, orchestrator may want SPLIT-CURRENCY — flag.
- **Private & Foreign Searches** → **N-BLIND-UNREAD**. P-only-split (page HAS hash-match split signal Reddick 5th / Wilson 9th; N did not derive one). Pure N-blindness. oi Reddick + Wilson pages EXIST, homed Key. Page is the correct/richer read.
- **Cell-Site Simulators** → **N-BLIND-UNREAD**. N-only-split ('is CSS deployment a search requiring warrant?'); p_homed=0, no named circuit positions. Emerging-tech question the page frames as open; no live named circuit split to currency-check. Benign.
- **Real-Time Tracking** → **N-BLIND-UNREAD**. N-only-split (short-term real-time CSLI post-Carpenter; pole-camera mosaic). Overlaps Aerial page. Benign framing divergence; page teaches the open questions. No coverage gap.
- **Reverse-Keyword & Geofence Warrants** → **ALREADY-RESOLVED**. N-only-split (geofence acquisition = search? / geofence = general warrant?). Geofence-threshold refusal DISMISSED with pool evidence (Chatrie 2026 SCOTUS: acquisition IS a search; 11349205.txt) and callout restored; page is CHATRIE/Smith(2024) EXPOSITION HOME (prior arc, commits per JOURNAL). Do not re-litigate.
- **When a Seizure Occurs** → **ALREADY-RESOLVED**. unknown_gap = INS v. Delgado (cluster 111148) genuinely ABSENT from corpus (no lake file, no content) = a real COVERAGE-GAP, but ALREADY escalated in prior arc to P4 inbox batch / INGEST recommended (commits 1c4ba2d, 6be84df). oi Carter + Amos pages EXIST (benign). Do not re-litigate; INGEST already dispatched.
- **Arrest & Arrest Warrants** → **N-BLIND-UNREAD**. P-only-split (page HAS split signal; N derived none). Pure N-blindness — page is the correct/richer read. No coverage gap.
- **Prompt Probable-Cause Determination** → **N-BLIND-UNREAD**. P-only-split (page HAS split signal; N derived none). Pure N-blindness. No coverage gap.
- **The Good-Faith Exception** → **ALREADY-RESOLVED**. N-only-split (geofence-novelty: does novelty itself support Leon/Davis good-faith reliance?). UPHELD in prior arc — Cano counter-pole fix LANDED (commit a319410: 9th-Cir Cano, novelty cuts AGAINST reliance, added to page). oi Calandra/Lopez-Mendoza/Leary/Mathis/Carpenter-remand pages EXIST (all homed). Do not re-litigate — closed.
- **Community Caretaking** → **N-BLIND-UNREAD**. N-only-split (standard for noninvestigative caretaking seizure of a person in public post-Caniglia); no named circuit positions. Benign framing divergence; page teaches open question. No coverage gap.
- **SIA — Cell Phones** → **N-BLIND-UNREAD**. N-only-split (adjacent border-device forensic-search suspicion post-Riley); p_homed=1, no named circuit positions. Adjacent/border question, not the SIA-cell-phone holding; benign N over-reach.
- **Inventory Searches** → **N-BLIND-UNREAD**. N-only-split (impound predicate + investigatory-motive taint). oi Evans page EXISTS (recent-development role). Named positions Evans/Braxton are 10th-Cir intra-circuit, not a cross-circuit split. Benign framing divergence.

## SUPPLEMENTARY — Chapman v. California (task-directed confirm; NOT among the 112)

**CONFIRMED MIS-KEY.** Lake record `_overhaul2/lake/cases/chapman-v-california--8428427.json` carries `cluster_id=8428427`, `lead_opinion_id=8398783`, `status=verified_identity`. Cached text `8398783.txt` (154B) reads in full: *"Petition for writ of certiorari to the Court of Appeal of California, Second Appellate District denied."* — a **cert-denial order**, not the merits harmless-error opinion. The real **Chapman v. California, 386 U.S. 18 (1967)** (Carl Chapman; Black, J.; constitutional-error harmless-beyond-reasonable-doubt) is a different opinion. `case_name_full` is already 'Carl CHAPMAN v. CALIFORNIA', so the metadata expects the merits case while the lead points at a procedural order.

**Recommendation (evidence only):** re-key to the real Chapman merits opinion — orchestrator/S2-builder to resolve the correct cluster/lead (a fresh CL job) and to check whether `--8428427` is an alias/folded record vs the primary Chapman record before cure. I did not resolve the correct id (would require a live CL call outside the cached-first budget).

---

*Machine-readable rows: `_run/s9/p2-evidence-2.jsonl` (113 rows = 112 + chapman).*