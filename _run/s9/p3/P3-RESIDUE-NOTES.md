# P3 residue notes (orchestrator running log — reconcile in P3.3)

## P5-tidy advisories (out of P3 scope, no open finding)
- Inventory lake-mirror link_target items still carry pre-rekey identity: Chapman cluster 8428427 (canonical 107359), Fisher cluster 5141053 + case_name "In re Mirsky" (canonical 131160). Orchestrator re-key lane if inventory identity sync wanted (INV worker advisory).
- Fisher lake record filename suffix still encodes pre-rekey cluster (illinois-v-fisher--5141053.json).
- 2 orphan adjudication refs (F-S9-PR-d1d2d45449, F-S9-PR-6ffdcb45b8) + inv5 count row (2329 vs 2331) — pre-existing, documented P5 tidy.

## NOT-FIXED (loop-2 queue)
- F-S9-PR-f11d96f96f — Katz pin-361 (Harlan concurrence text not cached; needs serial CL lane or concurrence cache).
- F-S9-PR-f6aa78bbe3 — Kentucky v. King pin-op8 (rendered anchor itself an adjudicated paraphrase). RESOLVABLE loop-2 cache-only: lead 9441559 IS at ~/cssi-lake/cache/text/ (L09 didn't know the path; brief amended).
- F-S9-PR-9129a38f84 — registry search.plain-view (blocked on Horton v. California lake status under_review; needs S2 promotion, then FIXED with no registry edit).
- F-S9-PR-1898039916 — registry seizure.person.noninvestigative-caretaking (blocked on United States v. Rideau under_review; same shape).
- Shard-2 under_review blockers (7 more, same shape; partial substantiation recorded in-row): F-S9-PR-63618573a5 (Nieves + Gonzalez), F-S9-PR-d03bcf3511 (Kolender), F-S9-PR-7cd9e1653f (Timbs/Bajakajian/Culley), F-S9-PR-b9b0faf4d2 (Sorrells), F-S9-PR-401600d8a9 (Keith), F-S9-PR-23503e4d56 (Chatrie 2026, official cite null), F-S9-PR-6dc90d8200 (Imbler/Rehberg/Buckley). - Shard-3 under_review blockers (6 more, same shape): F-S9-PR-5c8c9e31a0 (Burdeau + Verdugo-Urquidez), F-S9-PR-ad302e0c26 (Egbert), F-S9-PR-3eb697a51d (Weeks, field_i=good_law), F-S9-PR-8a201a17d3 (Nora/Al-Azzawy/Vaneaton), F-S9-PR-3102a1efd9 (Riley, good_law, sole authority), F-S9-PR-ccd4c2ea4f (Thompson + Chiaverini).
P3.3 decision owed: registry NOT-FIXED total 15 findings blocked on ~25 under_review lake cases. Serial-lane S2-style promotion vs _review-needed escalation (promotion is S2 lake work; check text-cache coverage first).

- F-S9-PR-7031763b18 — al-Kidd pin-743: lake already compliant; the defect is content/cases/Ashcroft v. al-Kidd.md:57 "Id. at 743" → "563 U.S. at 744" (or L.Ed.2d pin). Page NOT in any content packet — assign to residue fixer directly (loop 2).

- F-S9-PR-221787ed46 + F-S9-PR-a92730deca — Davis 2011 / Davis 1994 cite-selector: lake already canonical; the stale cites live only in _run build artifacts (s8-link-ledger, assertion-inventory). Fix = inventory rebuild (scripts/s9/build_inventory.py), orchestrator lane, P3.3.
- F-S9-PR-4a60de1d2c (Chapman) + F-S9-PR-8233ea44e1 (Fisher) — same stale-inventory class (pre-rekey cites only in _run/s9/assertion-inventory.json); same inventory-rebuild fix. Fisher record_id suffix still encodes pre-rekey cluster (rename decision = orchestrator, P5-adjacent).
- F-S9-PR-a596cf2c08 (Carter) — 5th stale-inventory item (official_citation_present flag lives only in assertion-inventory; page + lake already correct). Same inventory-rebuild fix.
- F-S9-PR-82877c804a + F-S9-PR-83f328f205 (Davis 2011/1994 page-side dupes) + F-S9-PR-a6ee1850ad (D.C. v. R.W.) — 3 more stale-inventory/seed items (pages already canonical). Inventory-rebuild class now 8 findings.
- F-S9-PR-4e77f991c3 (GEO Group) — 9th stale-inventory item (official_citation_present in assertion-inventory item 477280eb1de56771; page + lake already slip-only-consistent).
- F-S9-PR-3cdccf1a78 (Landor) — 10th stale-inventory item (same official_citation_present shape).
- F-S9-PR-3d0d17e0c0 (Mendoza) + F-S9-PR-ab2d347d66 (Porter) — stale-inventory items 11-12 (official_citation_present derivation; pages + lake already slip-only-correct). NOTE from C06: the derivation computes official_citation_present as citation != "" — the rebuild fix may need a derivation correction, not just a re-run.
- Touset lake pin-IIIa.quote is harvested content-page markdown (new qf-harvest-artifact instance, NOT an adjudicated finding) — flag for P4 sweeps, not P3.
- F-S9-PR-b881e64bdc (Trent) — stale-inventory item 13 (C07 confirms derivation: build_inventory.py:569 official_citation_present = bool(fm.citation); fix the derivation then rebuild).
- F-S9-PR-54d45be839 (Verdugo-Urquidez) — page verbatim-confirmed accurate; remedy = lake pinpoint/holding backfill (S2-style). Joins promotion class.
- F-S9-PR-95ee95c8da (Youngblood) + F-S9-PR-1c2af33b30 (G.M. Leasing) — frontier-stub currency; needs CL/S6; no page phrase to tighten. Joins promotion/escalation class.
- F-S9-PR-620c7122bb (Private & Foreign Searches) — Walter anchor sub-fix APPLIED by C08; the Burdeau *475 / Verdugo *265 quote-verification remainder IS cache-resolvable: both leads cached (99820.txt, 112382.txt) — C08 didn't find them. Loop-2 with explicit cache ids.
- Buie lake record identity.date_decided still 1990-03-05, page corrected to 1990-02-28 by C03 (cache-verified) — residue fixer flips the lake side (mechanical).
- James roster: verify Fruits and Attenuation.md no longer lists James after HM lands (C03 fixed the case-page home; roster is HM scope).
- Sanders role relabel (F-S9-PR-b604d87ede): RESOLVED no-mirror-owed — Automobile Exception page has no role cell for Sanders (prose + case-list already say overruled-by-Acevedo).
- F-S9-PR-e265b5a655 (Retaliatory Arrest page, Nieves/Gonzalez) — page accurate + hedged; defect is frontier-stub verification breadth in the Nieves/Gonzalez lake records. Joins the under_review/frontier promotion decision (P3.3).
- C09 under_review blockers (4 more, page-side callouts, same shape as registry class): F-S9-PR-f51839133d (Heien official cite, needs_cl), F-S9-PR-7936bdbc34 (Imbler/Briscoe/Rehberg/Buckley), F-S9-PR-624aa3a6c6 (Austin/Bajakajian/Timbs), F-S9-PR-71148ef394 (Thompson/Chiaverini).
- F-S9-PR-395bcb5628 — Fare pin-724 split: needs content/cases/Fare v. Michael C.md edit (add ^pin-722 anchor, attribution "442 U.S. at 722, 724") + lake pin split; both passages cache-verified. Page NOT in content packets — assign to residue fixer (loop 2) with combined lake+page write scope.

## Star-marker normalization (mechanical pass at wave-A end; ruling branch: reporter-attribution pins = star-verified + star_marker; slip pins slip-only)
- L02's 13 re-harvested pins conservatively left (matched, slip-only, star=null): Beckwith 346, Beecher 38, Benn p1, Boyd 626, Brady 87, Brendlin 251, Brewer 398, Brower 596, Brown v. Ill. 603, Brown v. Miss. 286, Brown v. Tex. 53+51, Bumper 548. Flip reporter pins to star-verified + star_marker per attribution.

## Cross-surface mirror flags (verify covered by Wave B, else fix in residue pass)
- content/cases/Jacobson v. United States.md L65 "No negative treatment." overstates vs qualified lake scope_note (page has C03 items — check after Wave B).
- content/cases/Brendlin v. California.md L65 same shape (flagged by L02).
- content/cases/City of Ontario v. Quon.md L53 attribution reads "560 U.S. at 761", should be 764 (lake pin retargeted by L04; page has C-packet items — verify after Wave B).
- content/cases/Connally v. Georgia.md L53 renders altered "[that] might lead" vs opinion "or which might lead" (flagged by L04).
- content/cases/Cupp v. Murphy.md L53 co-anchors the *295 fragment under the single "412 U.S. at 296" pincite; needs a *295 split/new anchor (flagged by L04).
- content/cases/California v. Prysock.md cites 451 U.S. (3 occurrences incl. an *Id.* volume) — should be 453 U.S. 355 (flagged by L03; page has C01 items — verify after Wave B).
- content/cases/Oliver v. United States.md:57 ^pin-179b still truncates the "in rural areas" qualifier (lake side restored by L12 per the adjudicated Oliver directive). Page NOT in content packets — assign to residue fixer (loop 2).
- content/cases/Taylor v. Riojas.md:65 overstated no-negative-treatment prose (lake scope_note qualified by L15). Page NOT in content packets — residue fixer (loop 2), same mirror class as Jacobson/Brendlin.
- content/cases/United States v. Johns.md attribution "469 U.S. at 482" + Sources "pinpoints: 482, 487" → 483 (lake retargeted by L17). Page NOT in content packets — residue fixer (loop 2).
- content/cases/Pennsylvania v. Muniz.md Sources "590–591" → 592 (lake pin retargeted by L13; page has C04 items — verify after Wave B).
- F-S9-PR-6d1aaf0e17 — content/cases/United States v. Castillo.md:55 wrong docket "(No. 21-50406)" → 22-50060 (lake already canonical; flagged by L16). Page NOT in content packets — residue fixer (loop 2).
- content/cases/Smith v. Cain.md pincite "(slip op., at 2)" → 3 (lake corrected by L14). Page NOT in content packets — residue fixer (loop 2).
- content/cases/United States v. Van Leeuwen.md:71 unqualified "No negative treatment" bullet (lake tightened by L19) — residue fixer (loop 2), mirror class.
- content/cases/United States v. Vinton.md Background/Application prose "Officer Aton" → "Officer Alton" (lake pin corrected by L19) — residue fixer (loop 2).
