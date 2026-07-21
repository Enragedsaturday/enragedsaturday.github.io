# I5-CLAUDE — frontier re-run summary (Claude lane, dual-model)

Packet: I5-CLAUDE (WS=I5). Per RULING P4-03, units = digital + civil-remedies + foundations
(the RANDOM pick, $RANDOM=11365 % 11). Method: blind WebSearch discovery only — no corpus
(`content/`), no lake, no `_run/s6-candidates/*`, no codex-lane output read. Independence is the
deliverable. Row schema `p4.i5.v1`. All rows carry `{lane:I5-CLAUDE, model:claude-opus-4-8}`.

## Searches per unit / stop conditions

- **Digital surveillance: 15 searches.** Threads: geofence (SCOTUS + 5th/4th), CSLI/third-party,
  reverse-keyword, pole camera/aerial, border devices, ALPR, tower dumps, drones, cell-site
  simulator, digital-warrant particularity, catch-all "most important 2025-2026." Stop condition
  hit: the last two catch-all searches re-surfaced only Chatrie + AI-surveillance CRS with no new
  decided circuit/SCOTUS case (two successive searches, nothing new).
- **Civil remedies: 12 searches.** Threads: excessive force (Barnes), malicious prosecution
  (Chiaverini/Thompson), retaliatory arrest (Gonzalez/Nieves), forfeiture (Culley/Pung/Timbs),
  Bivens (Egbert/Goldey), qualified immunity, Section 1983 procedure (Williams v. Reed), Monell,
  Vega/Miranda. Stop condition hit: QI and Monell searches returned no new 2024+ SCOTUS/landmark
  circuit merits decision (only legislation + commentary), and the OT2025-26 catch-all surfaced
  only cases already captured. Note: the term-roundup catch-all is what surfaced Case v. Montana
  (foundations) and Pung (forfeiture), both then verified.
- **Foundations: 10 searches.** Threads: private-search doctrine (Lowers/Brillhart/Ackerman +
  NCMEC), standing/REP (Parkerson/Rakas/Byrd), what-is-a-search (Katz/Jones), seizure-by-force
  (Torres line), emergency aid (Case v. Montana), traffic-stop prolongation (Rodriguez progeny),
  open fields/curtilage. Stop condition hit: the OT2025-26 4A search/seizure catch-all returned
  only Chatrie + Case v. Montana (already captured); Rodriguez-progeny and open-fields searches
  returned only fact-bound/unpublished applications and commentary — no new doctrine-shaping
  published circuit decision (two successive searches, nothing new).

Total: 37 searches (all units under the ~20/unit cap).

## Coverage statement

- Assigned: 3 units (digital, civil-remedies, foundations).
- Examined: 3/3. Candidate rows emitted: 22 (digital 6, civil 10, foundations 6).
- Skipped: 0 units. No thread silently truncated; each thread run to a two-null stop or the
  per-unit cap.

Confidence: `high` = caption + reporter/docket + holding corroborated across multiple independent
secondary sources. `medium` = holding well-attested but exact reporter cite/docket resolved from
web only (flagged in `cite_or_docket`), or a superseded/vacated posture, or a procedurally
tangential-to-search-and-seizure Section 1983 node, or (Parkerson) an unpublished disposition.
None require live CL for the *candidate* stage; the orchestrator's verify/pincite stage will.

## Highest-value frontier finds (post-date the likely S6 saturation window)

1. **Chatrie v. United States, 609 U.S. ___ (2026), No. 25-112 (Jun 29 2026)** — SCOTUS 6-3
   (Kagan): geofence Location History acquisition IS a Fourth Amendment search; REP survives
   third-party storage; remand on particularity/PC. Supersedes the 5th/4th Circuit split below.
   This is the single most likely two-key-real tripwire if the S6 logs predate cert/decision.
2. **Case v. Montana, 607 U.S. ___ (2026), No. 24-624 (Jan 14 2026)** — SCOTUS unanimous:
   emergency-aid home entry needs only an objectively reasonable basis (not PC, not RS); Caniglia
   community-caretaking distinguished.
3. **Goldey v. Fields, 606 U.S. ___ (2025), No. 24-809 (Jun 30 2025)** — SCOTUS per curiam: no
   Bivens for 8A excessive force against federal jailers; reverses a rare 4th Cir. extension.
4. **Barnes v. Felix, 605 U.S. ___ (2025), No. 23-1239 (May 15 2025)** — kills the moment-of-threat
   rule; totality-of-circumstances for 4A excessive force.
5. **Pung v. Isabella County, No. 25-95 (Jun 23 2026)** — tax-forfeiture just compensation = surplus
   proceeds; fair tax sale not an Excessive Fine (Tyler v. Hennepin follow-on).
6. **Live private-search circuit split (CSAM hash-matching):** United States v. Lowers, No. 24-4546
   (4th Cir. Mar 10 2026, published) [hash match ≠ private search; warrant required; joins 2d/9th]
   vs. United States v. Brillhart (11th Cir. Jul 9 2026) [hash-matched files openable without
   warrant; joins 5th/6th]. Brillhart is 12 days old and the freshest frontier item.

## Boundary calls / items deliberately NOT emitted as candidate rows

Task scope = "SCOTUS or published federal circuit decision" + pre-2024 items commentary treats as
newly doctrine-shaping. The following are real and active but fall outside that scope; logged here
for the orchestrator's diff-vs-saturation and the R12 maintenance handoff, NOT as candidate rows:

- **Pending / undecided (no candidate emitted):** border forensic-device warrant question before the
  2d, 3d, and 4th Circuits (EFF amici 2024-2026, no merits decision found); DOJ tower-dump appeal to
  the 5th Cir. (In re Tower Dumps, S.D. Miss. magistrate, 2025, is district-level); ALPR/Flock
  federal question (Norfolk suit is district-level, dismissed Jan 2026; no circuit decision).
- **State high-court decisions (out of scope for a federal wiki, but doctrine-adjacent):**
  Long Lake Township v. Maxon (Mich. 2024, drone surveillance / exclusionary rule); People v. Carson
  (Mich. 2025, digital-device warrant particularity); State v. Bryant (N.J. App. 2025, tower dumps);
  reverse-keyword line is currently state-only (Colorado). Flagged as coverage-context only.
- **Fact-bound / unpublished circuit applications (not doctrine-shaping "MUST-cover"):** United
  States v. Taylor (6th Cir. 2024, LEXIS-only, Rodriguez violation); United States v. Gonzalez
  (5th Cir. Jul 2024, traffic-stop scope). Parkerson (5th Cir. 2025) IS emitted but explicitly
  flagged UNPUBLISHED at `medium` for the orchestrator to filter under the "published" criterion.

## Items flagged for cite verification at the adjudication stage (no live CL used here)

- United States v. Holcomb (9th Cir. 2025) — holding (overbroad dominion-and-control clause =
  general warrant, suppressed, no good faith) well-attested; exact reporter cite/docket web-only.
- United States v. Brillhart (11th Cir. 2026) — split-creating holding corroborated by CaseMine +
  a March 2026 CRS circuit-split roundup; exact docket/reporter cite web-only (July 9 2026).
- United States v. Chatrie panel (4th Cir. 2024) cite 107 F.4th 319 and en banc 136 F.4th 100 —
  web-sourced reporter cites; en banc posture (even split / per curiam / good-faith affirm) confirmed
  across multiple sources.
