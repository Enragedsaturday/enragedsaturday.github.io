# P3 residue notes (orchestrator running log — reconcile in P3.3)

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
