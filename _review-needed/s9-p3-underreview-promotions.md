# S9 P3 escalation — fixes blocked on `under_review` / frontier-stub lake records

**Filed:** 2026-07-19 (P3.3, loop-cap protocol). **Adjudicator:** claude-fable-5-orchestrator.

22 UPHELD/MODIFIED findings whose adjudicated fixes cannot be applied from cache because a
load-bearing cited case sits at lake `status: under_review` (never S2-promoted) or is a frontier
stub with no treatment/pinpoint derivation. The fix in every case is **S2-style two-key promotion
(or pin/treatment harvest) of the blocking lake records via the serial CL lane**, then a mechanical
loop-3 re-run of the already-written fix directives. Partial substantiation for each finding is
recorded in its loop-1 NOT-FIXED fix row (fixes.jsonl). This is S2 lake work beyond P3's sanctioned
scope — escalated rather than improvised.

## Registry nodes (15) — substantiate-from-lake blocked

| Finding | Node | Blocking case(s) (under_review) |
|---|---|---|
| F-S9-PR-9129a38f84 | search.plain-view | Horton v. California (good_law, matched pins — promotion only) |
| F-S9-PR-1898039916 | seizure.person.noninvestigative-caretaking | United States v. Rideau |
| F-S9-PR-63618573a5 | (retaliatory-arrest) | Nieves v. Bartlett + Gonzalez v. Trevino |
| F-S9-PR-d03bcf3511 | (stop-and-identify) | Kolender v. Lawson |
| F-S9-PR-7cd9e1653f | (civil-forfeiture) | Timbs, Bajakajian, Culley |
| F-S9-PR-b9b0faf4d2 | (entrapment) | Sorrells v. United States |
| F-S9-PR-401600d8a9 | (title-III) | Keith (U.S. v. U.S. Dist. Court) |
| F-S9-PR-23503e4d56 | (geofence-warrant) | Chatrie v. United States (2026; official cite null) |
| F-S9-PR-6dc90d8200 | (absolute-immunity) | Imbler, Rehberg, Buckley |
| F-S9-PR-5c8c9e31a0 | search.private-foreign | Burdeau + Verdugo-Urquidez |
| F-S9-PR-ad302e0c26 | liability.federal-officer-suits | Egbert v. Boule |
| F-S9-PR-3eb697a51d | remedy.exclusionary | Weeks v. United States (good_law — promotion only) |
| F-S9-PR-8a201a17d3 | seizure.person.constructive-entry | Nora, Al-Azzawy, Vaneaton |
| F-S9-PR-3102a1efd9 | search.person.sia-cellphone | Riley v. California (good_law, sole authority) |
| F-S9-PR-ccd4c2ea4f | liability.malicious-prosecution | Thompson v. Clark + Chiaverini |

## Page-side callouts / treatment items (7)

| Finding | Page | Blocker |
|---|---|---|
| F-S9-PR-f51839133d | Reasonable Suspicion.md | Heien official cite 574 U.S. 54 absent from lake (needs_cl) |
| F-S9-PR-7936bdbc34 | Absolute Immunity.md | Imbler/Briscoe/Rehberg/Buckley under_review, pinpoints=[] |
| F-S9-PR-624aa3a6c6 | Civil Asset Forfeiture.md | Austin/Bajakajian/Timbs under_review, pinpoints=[] |
| F-S9-PR-71148ef394 | Malicious Prosecution (§1983).md | Thompson/Chiaverini under_review, pinpoints=[] |
| F-S9-PR-e265b5a655 | Retaliatory Arrest.md | Nieves/Gonzalez frontier-stub verification breadth (page itself accurate + hedged) |
| F-S9-PR-95ee95c8da | Brady and Giglio page (Youngblood) | frontier-stub currency; needs CL/S6 derivation |
| F-S9-PR-1c2af33b30 | Curtilage.md (G.M. Leasing) | frontier-stub currency; needs CL/S6 derivation |

## Workorder (post-P3, sanction required)

1. Serial-CL two-key promotion of the ~25 distinct blocking cases (several are good_law with
   matched pins already — promotion is verification bookkeeping, not re-research; text cache
   already holds many leads).
2. Pin/treatment harvest for the pinpoints=[] stubs named above.
3. Loop-3 mechanical re-run of the 22 stored fix directives; every one is expected to flip FIXED
   with no new judgment.
