# S6 SEED — Named-but-no-page case roster (named-in-prose lane)

**Provenance.** Regenerated **2026-07-02** to close audit finding **COH-02 [CRITICAL]** — S6's scope
and S2's manifest seed (`specs/S2-authority-database.spec.md` Method step 1 / R11) pointed at a
"§S6 seed / `audit_cases.py`" that existed nowhere in the repo (see `_overhaul2/AUDIT-2026-07-02.md`
COH-02a/COH-02b, NUM-05). The original 2026-07-01 audit output was never committed; this file and
`_overhaul2/scripts/audit_cases.py` regenerate it reproducibly. Method lineage: the 2026-07-02
claims-audit measurement (claim #5: 127 raw captions → ~80–84 cleaned, 61/84 government captions,
residual noise ±4), reimplemented and hardened — see Divergence below.

**Method (one paragraph).** `audit_cases.py` scans `content/**/*.md` prose (excluding
`content/cases/`) for case captions (`X v. Y`, plus `In re X` / `Ex parte X`), ignores wikilinked
mentions (already linked) and anything that resolves to an existing `content/cases/` page —
matching against filename ∪ `title:` ∪ `aliases:`, normalized with year-parenthetical stripping
("Harris v. United States (1968)"), apostrophe/abbreviation folding (Dep't/Dept., Dist./District),
party token-sets ("Brower v. Inyo County" = "Brower v. County of Inyo"), and truncation/extension
matching with hyphen-preserving surnames ("Canton v. Harris" ⊂ "City of Canton v. Harris", but
"Perez" ≠ "Perez-Rodriguez"). Citation-format teaching placeholders are shunted to §c. Rows are
annotated with fabrication flags (`docs/FINAL-QA-SPEC.md` §0.3), O1 omissions-register dispositions
(`_overhaul/coverage/omissions.md`), and probable-variant page matches. Court/era is a cheap
same-line parenthetical heuristic — read it as "as asserted in prose," not verified fact.
Deterministic, Python stdlib only, no network.

**Re-run:**

```sh
python3 _overhaul2/scripts/audit_cases.py                    # roster markdown → stdout
python3 _overhaul2/scripts/audit_cases.py --format json      # machine-readable (S2 manifest seed)
python3 _overhaul2/scripts/audit_cases.py --show-dropped     # audit the 897 page-matched exclusions
```

**Scope note (GAP-05).** This is the **named-in-prose lane only**. The S6 officer-field-relevance
gate and the OT2019→present term-by-term **SCOTUS sweep** (audit GAP-05) are separate seed sources
that will **EXTEND** this roster — never-named doctrine (*Nieves*, *Thompson*, *Chiaverini*,
*Gonzalez*, *Culley*, *Cooley*, *Lombardo*) cannot appear here by construction. The full S6 diff is
book roster ∪ **this file** ∪ prior-research ∪ bounded frontier.

**Status column.** Every row is `unverified`. S6 verifies existence via the **two-key protocol**
(CL identity + web), compares the input name against the CL **canonical caption**, and applies
**"not found ≠ fabricated"** before any author/remove decision.

**Counts.** **89 roster rows** (63 US-/State-/Commonwealth-/People-captions — mostly circuit/state)
· 5 citation-format placeholders (§c, ignored) · 4 fabrication-flagged (§a) · 3 UNVERIFIABLE
carry-forwards (§a) · 9 alias/variant-annotated rows (§b) · O1 185-list residual: 4 (§d).
Sanity assertion (in-script, every run): **no roster row matches an existing `content/cases/`
page** (case-insensitive, normalized) — PASS.

## Roster — named in prose, no case page (all `unverified`)

| # | Caption (as found) | Court / era (heuristic) | Source file:line(s) | Mentions | Flags / variant notes | Status |
|---|---|---|---|---|---|---|
| 1 | Alasaad v. Mayorkas | 1st Cir. 2021 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:79; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:117 | 2 | caption variant of Alasaad v. Wolf (same 1st Cir. case, successor DHS secretary) | unverified |
| 2 | Alasaad v. Wolf | unknown | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:79; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:117 | 2 | caption variant of Alasaad v. Mayorkas (same 1st Cir. case, successor DHS secretary) | unverified |
| 3 | Alvarez v. City of Brownsville | 5th Cir. 2018 | 10-use-of-force-liability/Brady and Giglio.md:83; 10-use-of-force-liability/Brady and Giglio.md:117 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 4 | Arkansas v. Sanders | 1979 | 2-legal-system-research/Case Index.md:33; 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:24; 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:46; +1 more | 4 | — | unverified |
| 5 | Beautiful Struggle v. Baltimore Police Dep't | 4th Cir. 2021 | 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:57; 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:90 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 6 | Carter v. United States | D.C. Court of Appeals 2025 | 4-what-is-a-seizure/Seizure of the Person.md:101 | 1 | — | unverified |
| 7 | Chapman v. California | unknown | 9-confessions-interrogation/Due-Process Voluntariness of Confessions.md:25 | 1 | possible variant of `Chapman v. United States (1961).md` | unverified |
| 8 | Commonwealth v. Serge | 2006 | 2-legal-system-research/Reading and Citing Cases.md:146 | 1 | — | unverified |
| 9 | District of Columbia v. Heller | 2008 | 3-what-is-a-search/Fourth Amendment Framework.md:50; 3-what-is-a-search/Fourth Amendment Framework.md:95 | 2 | O1 omissions: out-of-remit (2A) → logged-only | unverified |
| 10 | Egbert v. Boule | 2022 | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:27; 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:164 | 2 | O1 omissions: OPTIONAL-tier (S2) → brief-mention | unverified |
| 11 | Frank v. Maryland | 1959 | 2-legal-system-research/Case Index.md:144; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:47; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:170 | 3 | — | unverified |
| 12 | G. M. Leasing Corp. v. United States | 1977 | 2-legal-system-research/Case Index.md:148; 3-what-is-a-search/Curtilage.md:41; 3-what-is-a-search/Curtilage.md:116; +1 more | 4 | O1 omissions: borderline (R2) — thin field relevance → brief-mention | unverified |
| 13 | Gaetjens v. Winnebago County | 7th Cir. 2021 | 12-instructor-craft-study/Three Golden Rules.md:30; 12-instructor-craft-study/Three Golden Rules.md:70 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 14 | Jimerson v. Lewis | 5th Cir. 2024 | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:115; 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:186 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 15 | Johnson v. Glick | unknown | 10-use-of-force-liability/Use of Force.md:42 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 16 | Knight v. Jacobson | 11th Cir. 2002 | 4-what-is-a-seizure/Arrest in the Home.md:84; 4-what-is-a-seizure/Arrest in the Home.md:128 | 3 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 17 | LaDuke v. Nelson | 9th Cir. 1985 | 3-what-is-a-search/Tents.md:25; 3-what-is-a-search/Tents.md:85 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 18 | LLC v. John Doe | unknown | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:188 | 1 | incidental non-4A mention (Strike 3 Holdings BitTorrent docket, corrupted-CL-object warning for Zorn) — ignore | unverified |
| 19 | Martin v. United States | 2025 | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:41; 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:187 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 20 | Milam v. United States | 4th Cir. 1924 | 3-what-is-a-search/Fourth Amendment Recalibration.md:20; 3-what-is-a-search/Fourth Amendment Recalibration.md:67 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 21 | Quantity of Copies of Books v. Kansas | 1964 | 2-legal-system-research/Case Index.md:17; 6-warrant-requirement/The Warrant Requirement.md:178 | 2 | — | unverified |
| 22 | Robbins v. California | 1981 | 2-legal-system-research/Case Index.md:318; 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:24; 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:137 | 3 | — | unverified |
| 23 | Robinson v. Commonwealth | Va. Ct. App. Apr. 7, 2026 | 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:56; 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:89 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 24 | State v. Demesme | La. 2017 | 9-confessions-interrogation/Miranda Waiver and Invocation.md:58; 9-confessions-interrogation/Miranda Waiver and Invocation.md:157 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 25 | State v. Karston | La. Ct. App. 1991 | 3-what-is-a-search/Curtilage.md:41; 3-what-is-a-search/Curtilage.md:125 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 26 | State v. Larson | 1999 | 3-what-is-a-search/Curtilage.md:41; 3-what-is-a-search/Curtilage.md:127 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 27 | State v. Weaver | Tex. Crim. App. 2011 | 3-what-is-a-search/Curtilage.md:41; 3-what-is-a-search/Curtilage.md:126 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 28 | State v. Wint | 2018 | 9-confessions-interrogation/Miranda Waiver and Invocation.md:108; 9-confessions-interrogation/Miranda Waiver and Invocation.md:156 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 29 | Trupiano v. United States | 1948 | 2-legal-system-research/Case Index.md:373; 7-exceptions-warrant/7b-pc-not-needed/Search Incident to Arrest.md:25 | 2 | — | unverified |
| 30 | United States v. Aigbekaen | 4th Cir. 2019 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:71; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:116 | 2 | — | unverified |
| 31 | United States v. Amos | 3d Cir. 2023 | 4-what-is-a-seizure/Seizure of the Person.md:100 | 1 | — | unverified |
| 32 | United States v. Berkowitz | 7th Cir. 1991 | 4-what-is-a-seizure/Arrest in the Home.md:84; 4-what-is-a-seizure/Arrest in the Home.md:127 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 33 | United States v. Black | 4th Cir. 2013 | 4-what-is-a-seizure/Terry Stops and Reasonable Suspicion.md:96; 4-what-is-a-seizure/Terry Stops and Reasonable Suspicion.md:145 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 34 | United States v. Brinkley | 4th Cir. 2020 | 4-what-is-a-seizure/Arrest in the Home.md:85; 4-what-is-a-seizure/Arrest in the Home.md:129 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 35 | United States v. Burgess | 10th Cir. 2009 | 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:86; 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:133; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:36 | 3 | — | unverified |
| 36 | United States v. Camou | 9th Cir. 2014 | 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:85; 7-exceptions-warrant/7a-pc-needed/Automobile Exception.md:134 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 37 | United States v. Capers | 2d Cir. 2010 | 9-confessions-interrogation/Miranda Waiver and Invocation.md:107; 9-confessions-interrogation/Miranda Waiver and Invocation.md:154 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 38 | United States v. Carlton Williams | 3d Cir. 2018 | 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:42; 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:85; 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:124 | 3 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 39 | United States v. Carpenter | 6th Cir. 2019 | 8-exclusionary-rule-remedies/The Exclusionary Rule.md:199 | 1 | swapped-caption match: `Carpenter v. United States.md` | unverified |
| 40 | United States v. Castillo | 5th Cir. 2023 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:84; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:118 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 41 | United States v. Chatrie | 4th Cir. en banc, 136 F.4th 100 | 3-what-is-a-search/Fourth Amendment Framework.md:80; 3-what-is-a-search/Two Definitions of Search.md:78; 3-what-is-a-search/Two Definitions of Search.md:127; +5 more | 8 | swapped-caption match: `Chatrie v. United States.md` | unverified |
| 42 | United States v. Chavez | 10th Cir. 2008 | 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:66; 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:93 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 43 | United States v. Cole | 7th Cir. 2021 | 4-what-is-a-seizure/Traffic Stops.md:95; 4-what-is-a-seizure/Traffic Stops.md:146 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 44 | United States v. Crumble | 8th Cir. 2018 | 3-what-is-a-search/Abandonment.md:76 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 45 | United States v. Cruz | unknown | 2-legal-system-research/Case Index.md:396 | 1 | UNVERIFIABLE carry-forward (O1 S5 R9) | unverified |
| 46 | United States v. Daniels | 10th Cir. 2024 | 4-what-is-a-seizure/Terry Stops and Reasonable Suspicion.md:94; 4-what-is-a-seizure/Terry Stops and Reasonable Suspicion.md:143; 5-levels-of-suspicion/Probable Cause and Reasonable Suspicion.md:113; +1 more | 4 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 47 | United States v. Davis | 4th Cir. 2021 | 7-exceptions-warrant/7b-pc-not-needed/Search Incident to Arrest.md:139 | 1 | swapped-caption match: `Davis v. United States (2011).md`; swapped-caption match: `Davis v. United States.md` | unverified |
| 48 | United States v. Ganias | 2d Cir. 2016 | 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:89; 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:134; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:36 | 3 | — | unverified |
| 49 | United States v. Hanapel | 8th Cir. 2024 | 11-adjacent-doctrines/Entrapment.md:64; 11-adjacent-doctrines/Entrapment.md:90 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 50 | United States v. Hay | 10th Cir. 2024 | 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:54; 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:87 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 51 | United States v. Holcomb | 9th Cir. 2025 | 6-warrant-requirement/The Warrant Requirement.md:115 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 52 | United States v. Hunt | 9th Cir. 2025 | 3-what-is-a-search/Abandonment.md:74 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 53 | United States v. Kolsuz | 4th Cir. 2018 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:70; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:115 | 2 | — | unverified |
| 54 | United States v. Lee | 1927 | 3-what-is-a-search/Fourth Amendment Recalibration.md:22; 3-what-is-a-search/Fourth Amendment Recalibration.md:34; 3-what-is-a-search/Fourth Amendment Recalibration.md:69 | 3 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 55 | United States v. Lewis | 6th Cir. 2023 | 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:42; 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:84; 7-exceptions-warrant/7b-pc-not-needed/Consent Searches.md:123 | 3 | swapped-caption match: `Lewis v. United States (1966).md` | unverified |
| 56 | United States v. Liddell | 8th Cir. 2008 | 9-confessions-interrogation/Miranda and Custodial Interrogation.md:100 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 57 | United States v. Loera | 10th Cir. 2019 | 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:90; 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:135 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 58 | United States v. Loines | 6th Cir. 2023 | 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:82; 7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md:136 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 59 | United States v. Lyle | Binding in-circuit — 2d Cir.; narrows Byrd lawful-possession | 8-exclusionary-rule-remedies/Standing to Challenge a Search.md:79; 8-exclusionary-rule-remedies/Standing to Challenge a Search.md:117 | 2 | fabrication-flagged (FINAL-QA §0.3); O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 60 | United States v. Maez | 10th Cir. 1989 | 4-what-is-a-seizure/Arrest in the Home.md:84; 4-what-is-a-seizure/Arrest in the Home.md:126 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 61 | United States v. Massenburg | 4th Cir. 2011 | 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:65; 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:92 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 62 | United States v. May-Shaw | 6th Cir. 2020 | 3-what-is-a-search/Curtilage.md:83; 3-what-is-a-search/Curtilage.md:123 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 63 | United States v. Mayville | 10th Cir. 2020 | 4-what-is-a-seizure/Traffic Stops.md:96; 4-what-is-a-seizure/Traffic Stops.md:147 | 2 | fabrication-flagged (FINAL-QA §0.3); O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 64 | United States v. Mendez | 7th Cir. 2024 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:83; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:120 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 65 | United States v. Mendoza | Binding in-circuit — 3d Cir.; hotel-checkout REP | 8-exclusionary-rule-remedies/Standing to Challenge a Search.md:78; 8-exclusionary-rule-remedies/Standing to Challenge a Search.md:116 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 66 | United States v. Meyer | 8th Cir. 2021 | 7-exceptions-warrant/7a-pc-needed/Exigent Circumstances and Hot Pursuit.md:73; 7-exceptions-warrant/7a-pc-needed/Exigent Circumstances and Hot Pursuit.md:116; 7-exceptions-warrant/7b-pc-not-needed/Knock and Talk.md:38; +1 more | 4 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 67 | United States v. Moore-Bush | 1st Cir. 2022, en banc | 3-what-is-a-search/Curtilage.md:82; 3-what-is-a-search/Curtilage.md:122; 3-what-is-a-search/Fourth Amendment Framework.md:82; +3 more | 6 | fabrication-flagged (FINAL-QA §0.3) | unverified |
| 68 | United States v. Oliveras | 2d Cir. 2024 | 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:115; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:169 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 69 | United States v. Payne | 9th Cir. 2024 | 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:114; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:168 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 70 | United States v. Perez | 1st Cir. 2023 | 7-exceptions-warrant/7b-pc-not-needed/Search Incident to Arrest.md:86; 7-exceptions-warrant/7b-pc-not-needed/Search Incident to Arrest.md:143 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 71 | United States v. Perez-Rodriguez | 1st Cir. 2021 | 11-adjacent-doctrines/Entrapment.md:65; 11-adjacent-doctrines/Entrapment.md:91 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 72 | United States v. Porter | 5th Cir. Mar. 17, 2026 | 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:55; 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:88 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 73 | United States v. Reddick | 5th Cir. 2018 / 6th Cir. 2020 | 3-what-is-a-search/Fourth Amendment Framework.md:84 | 1 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 74 | United States v. Ruckman | 10th Cir. 1986 | 3-what-is-a-search/Tents.md:31; 3-what-is-a-search/Tents.md:45; 3-what-is-a-search/Tents.md:80 | 3 | — | unverified |
| 75 | United States v. Ruiz | 2002 | 10-use-of-force-liability/Brady and Giglio.md:83; 10-use-of-force-liability/Brady and Giglio.md:118 | 2 | O1 omissions: out-of-remit (plea/trial) → logged-only | unverified |
| 76 | United States v. Small | 4th Cir. 2019 | 3-what-is-a-search/Abandonment.md:75 | 1 | fabrication-flagged (FINAL-QA §0.3); O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 77 | United States v. Smith | 5th Cir. 2024 | 3-what-is-a-search/Fourth Amendment Framework.md:81; 3-what-is-a-search/The Third-Party Doctrine and Digital Surveillance.md:59; 3-what-is-a-search/Two Definitions of Search.md:79; +8 more | 11 | — | unverified |
| 78 | United States v. Trent | 6th Cir. 2026 | 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:64; 4-what-is-a-seizure/Collective Knowledge and the Fellow-Officer Rule.md:91 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 79 | United States v. Vasquez-Algarin | 3d Cir. 2016 | 4-what-is-a-seizure/Arrest in the Home.md:86; 4-what-is-a-seizure/Arrest in the Home.md:130 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 80 | United States v. Verdugo-Urquidez | unknown | 2-legal-system-research/Case Index.md:453 | 1 | O1 omissions: borderline (R2) — thin field relevance → brief-mention | unverified |
| 81 | United States v. West | unknown | 2-legal-system-research/Case Index.md:396 | 1 | UNVERIFIABLE carry-forward (O1 S5 R9) | unverified |
| 82 | United States v. White | unknown | 2-legal-system-research/Case Index.md:458 | 2 | UNVERIFIABLE carry-forward (O1 S5 R9); possible variant of `Alabama v. White.md`; possible variant of `Florida v. White.md` | unverified |
| 83 | United States v. Williams | 9th Cir. 2006 | 9-confessions-interrogation/Miranda Waiver and Invocation.md:107; 9-confessions-interrogation/Miranda Waiver and Invocation.md:155 | 2 | — | unverified |
| 84 | United States v. Wilson | 9th Cir. 2021 | 3-what-is-a-search/Fourth Amendment Framework.md:83; 3-what-is-a-search/Two Definitions of Search.md:81; 3-what-is-a-search/Two Definitions of Search.md:130 | 3 | possible variant of `Maryland v. Wilson.md` | unverified |
| 85 | United States v. Xiang | 8th Cir. 2023 | 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:85; 7-exceptions-warrant/7b-pc-not-needed/Border Searches.md:119 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 86 | United States v. Young | 10th Cir. 2020 | 9-confessions-interrogation/Due-Process Voluntariness of Confessions.md:77; 9-confessions-interrogation/Due-Process Voluntariness of Confessions.md:112 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |
| 87 | Wyman v. James | 1971 | 2-legal-system-research/Case Index.md:480; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:47; 7-exceptions-warrant/7b-pc-not-needed/Special Needs and Administrative Searches.md:171 | 3 | O1 omissions: borderline (R2) — thin field relevance → brief-mention | unverified |
| 88 | Ziglar v. Abbasi | 2017 | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:27; 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:165 | 2 | — | unverified |
| 89 | Zorn v. Linton | 2026 | 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:31; 10-use-of-force-liability/Section 1983 Liability and Qualified Immunity.md:188 | 2 | O1 omissions: out-of-remit (persuasive-only, R6) → brief-mention | unverified |

## (a) Fabrication-flagged names — verify first, then author or remove

Flagged in `docs/FINAL-QA-SPEC.md:25` (§0.3 prior-build watch-list: web-discovery scouts produced a
**backwards holding** (*Moore-Bush*) and **invented frameworks** (*Mayville/Lyle/Small*)); carried
into `RUNBOOK.md` §4-S6. All four are roster rows above, flagged in the table:

| Caption | Court/era asserted | Where named | Watch-list reason |
|---|---|---|---|
| United States v. Mayville | 10th Cir. 2020 | 4-what-is-a-seizure/Traffic Stops.md:96,147 | invented-framework risk (Triple-I check "within the mission") |
| United States v. Small | 4th Cir. 2019 | 3-what-is-a-search/Abandonment.md:75 | invented-framework risk (phone-abandonment REP) |
| United States v. Lyle | 2d Cir. 2019 | 8-exclusionary-rule-remedies/Standing to Challenge a Search.md:79,117 | invented-framework risk (narrows *Byrd*) |
| United States v. Moore-Bush | 1st Cir. 2022 (en banc) | 3-what-is-a-search/{Curtilage, Fourth Amendment Framework, Two Definitions of Search, Third-Party Doctrine}.md — 6 mentions | backwards-holding scar (later corrected to unanimous reversal, 3–3 rationale) |

*Context, not clearance:* O1's serial-CL adjudication (`_run/s9-adjudications.md:34`) later confirmed
*Mayville* (10th Cir. 2020) and *Small* (4th Cir. 2019) as real and correctly stated, and the current
*Moore-Bush* text reflects the corrected holding. They remain `unverified` here because S6 re-runs
the two-key check under O2's protocol; **"not found ≠ fabricated"** cuts both ways.

**Also carried forward — UNVERIFIABLE bare names (O1 S5 R9, `_overhaul/specs/S5-case-ingest.spec.md:246-249`;
Case Index rows 396/458):** *United States v. Cruz*, *United States v. West*, *United States v. White*
(stolen-vehicle standing) — flagged exception rows by design, never resurrected without verification.
A **second bare "United States v. Jackson"** was flagged there too; it is not a roster row because a
different, real *United States v. Jackson* page exists and absorbs the name — S6 must adjudicate the
good-faith/bad-faith-warrant trio in the Exclusionary Rule context, not just the caption.

## (b) Alias / caption-variant candidates — fix the mismatch, don't blind-ingest

Rows the scanner flagged as probably related to an existing page (`swapped-caption` = both parties
match with order inverted; `possible variant` = distinctive party matches, other party is a
government litigant in both). RUNBOOK §4-S6 estimated "~6 alias/variant mismatches"; the regenerated
scan annotates 9 rows. **Warning from the prose itself:** several "swapped" pairs are genuinely
*distinct decisions in the same litigation* — adjudicate, don't merge.

| Caption found (roster row) | Probably related page | Adjudication note |
|---|---|---|
| United States v. Chatrie | `Chatrie v. United States.md` | 4th Cir. en banc (pre-cert) vs the SCOTUS 2026 merits page — distinct decisions; prose cites both |
| United States v. Carpenter | `Carpenter v. United States.md` | 6th Cir. 2019 good-faith **remand**, expressly "distinct from the SCOTUS merits decision" (Exclusionary Rule.md:131) |
| United States v. Davis | `Davis v. United States (2011).md`, `Davis v. United States.md` | 4th Cir. 2021 SITA-backpack case — likely distinct from both SCOTUS Davises |
| United States v. Lewis | `Lewis v. United States (1966).md` | 6th Cir. 2023 consent case — likely distinct |
| United States v. Wilson | `Maryland v. Wilson.md` | 9th Cir. 2021 (private-search/CSAM) — distinct |
| Chapman v. California | `Chapman v. United States (1961).md` | Real, different SCOTUS case (harmless error, 1967) — needs its own verify/ingest decision |
| United States v. White | `Alabama v. White.md`, `Florida v. White.md` | UNVERIFIABLE carry-forward; surname coincidence likely |
| Alasaad v. Mayorkas ↔ Alasaad v. Wolf | (each other; no page) | Same 1st Cir. border-device case under successor-DHS-secretary captions — one case, one page, two aliases |

## (c) Citation-format placeholders — ignore (teaching templates, not cases)

All five live in `content/2-legal-system-research/Reading and Citing Cases.md:106,113` (Bluebook
short-form and civil-caption teaching examples): *State v. Smith*, *Stern v. Florida*, *Stern v.
State*, *State v. Randolph* (short-form example of the existing *Georgia v. Randolph* page),
*Smith v. Jones*. The scanner classifies them out of the roster automatically. One adjacent
incidental stays **in** the roster but flagged ignore: *LLC v. John Doe* = *Strike 3 Holdings, LLC
v. John Doe*, the D.D.C. BitTorrent docket named only as the corrupted-CL-object warning on the
*Zorn v. Linton* entry (Section 1983 …md:188).

## (d) O1 missed-cases residual (from `_overhaul/coverage/missed-cases.md`, 185 rows)

Only **4** of O1's 185 confirmed misses are still page-less today, and all four also appear in the
prose roster above: **Trupiano v. United States** (1948), **Frank v. Maryland** (1959), **Arkansas
v. Sanders** (1979), **Robbins v. California** (1981) — a coherent pre-*Ross*/administrative-search
historical cluster O1 deliberately left as index/brief mentions. The claims audit's "12 residual"
(NUM-05) was **8 parts measurement artifact**: six year-disambiguated filenames the prior
normalization failed to match (*Chapman/Harris/Henry/Lewis/Mathis v. United States* + *United States
v. Harris (1971)* — all have pages), plus *Brower v. Inyo County* (page `Brower v. County of
Inyo.md`, alias present) and *Florida v. Myers* (page `Florida v. Meyers.md`, spelling alias).

## Divergence from the claims-audit's ~80–84

This roster lands at **89** vs the prior estimate of ~80–84 (itself ±4). Reconciled row-by-row
against the prior method's 127 raw captions: **43** of the prior entries resolved as artifacts
(truncations of existing pages like "Canton v. Harris"/"Florence v. County", possessives
"Gant's"/"Belton's", year-parenthetical false-misses, normalization misses like "INS v.
Lopez-Mendoza"), **9** reappear here under corrected full captions ("District of Columbia v.
Heller", "United States v. Moore-Bush", …), and the surplus over 84 comes from rows the prior
cleaning wrongly discarded or conflated — e.g. *United States v. Perez* (1st Cir. 2023), a real
split case distinct from *Perez-Rodriguez*. Government-caption share matches: **63/89** here vs
61/84 prior. Net: same population, cleaner boundaries; the +5 over the prior top end is explained
noise from corrected false-drops, within the prior method's own error bar.

---
*Generated by `_overhaul2/scripts/audit_cases.py` (re-run commands in the header). The table above
is the script's verbatim markdown output; regenerate rather than hand-edit.*
