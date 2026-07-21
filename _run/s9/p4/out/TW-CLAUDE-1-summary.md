# TW-CLAUDE-1 summary (tripwire 13-cat frontier re-run, Claude lane, units 1-5)

Packet: TW-CLAUDE-1 (Claude lane). Method: BLIND discovery, WebSearch only. No corpus / lake /
`out/codex/*` read. Window: 2024-01-01 -> 2026-07-21 (+ pre-2024 cases 2024-25 commentary treats as
doctrine-shaping). Bound: ~15 searches/unit, stop a thread after two successive null searches.
Governing rulings read: P4-03 (I5 units), P4-07 (tripwire FIRED, Lowers predicate), P4-08 (paced re-run).

Model id: claude-opus-4-8. Candidates: `_run/s9/p4/out/TW-CLAUDE-1-candidates.jsonl` (20 rows).

## Coverage: assigned / examined / candidates per unit
- Unit 1 standards (PC/RS, Franks, informants, Gates, dog alerts, Heien): examined; 3 candidates.
- Unit 2 searches non-digital (REP, curtilage/open fields, aerial, canine, abandonment, tents, plain view/feel): examined; 9 candidates.
- Unit 3 seizures of persons (Terry, arrests, Hodari, Rodriguez stops, checkpoints, Torres force): examined; 3 candidates.
- Unit 4 the warrant (issuance, neutral magistrate, particularity, staleness, anticipatory, execution, knock-and-announce): examined; 3 candidates.
- Unit 5 warrant exceptions (SITA, automobile, exigency/Lange, emergency aid/Case v. Montana, consent, inventory, special needs, border non-device, community caretaking): examined; 2 candidates.
- Skipped/deferred: none silently. Threads that returned null (no new in-window controlling case) are logged below as stop conditions.

## Searches per unit (approx; some queries cross-served two units)
- Unit 1: ~8 (SCOTUS PC/RS; Franks materiality/omissions; dog-sniff reliability; Heien; informant reliability; anonymous tip/Navarette; Chiaverini; Felton).
- Unit 2: ~8 (open fields/IJ; Collins/curtilage; drone/Maxon aerial; abandonment; tents/encampment; plain view/feel; canine apartment door; curtilage knock-and-talk/Banks).
- Unit 3: ~5 (Barnes v. Felix; Rodriguez progeny; Torres/Hodari progeny; Terry-gun/high-crime post-Bruen; checkpoints).
- Unit 4: ~4 (geofence particularity/Chatrie/Smith; knock-and-announce; anticipatory/staleness; term-review roundup).
- Unit 5: ~8 (Lange progeny; Caniglia progeny; border non-device; SITA/automobile/Davis; consent/special-needs; special-needs DUI/school; Mendez holding-check; term-review roundup).
- Cross-cutting: ~3 (circuit-split roundup; OT2025 SCOTUS term review; Mumford dog-sniff split).
Total ~36 searches.

## Stop conditions (two-successive-null threads / single nulls)
- Unit 3, "precedent-progeny" thread: Rodriguez progeny (null) + Torres/Hodari progeny (null) = two successive nulls -> stopped generic progeny probing. Live hits came from other threads (Barnes; Wilson) + the Rodriguez prolonged-seizure split node (commentary).
- Unit 3, checkpoints: null (no new in-window published circuit checkpoint case; only Martinez-Fuerte/Sitz/Edmond/Lidster background). Stopped.
- Unit 4, anticipatory + staleness: null (no new in-window controlling circuit case). Single null; moved on.
- Unit 5, special-needs thread: consent/apparent-authority (null) + special-needs DUI/school/parolee (null, only STATE cases surfaced: State v. German (SC), PA ER blood-draw) = two successive nulls -> stopped.
- Unit 5, Lange progeny (null) + Caniglia progeny (null): the emergency-aid capstone is Case v. Montana (SCOTUS 2026), captured; no new published circuit Lange/Caniglia hot-pursuit or community-caretaking case surfaced in-window.
- Unit 5, border NON-device: null. The one concrete in-window published circuit border case, United States v. Mendez, 103 F.4th 1303 (7th Cir. 2024) (No. 23-1460, cert. denied 24-302), is a border ELECTRONIC-DEVICE (cellphone) search -> DIGITAL umbrella, OUT OF non-device scope; excluded from candidates (see cross-lane note).

## High-confidence MUST-cover SCOTUS holdings in window (all filed)
- Chiaverini v. City of Napoleon, 602 U.S. 556 (2024) [standards].
- Barnes v. Felix, 145 S. Ct. 1353 (2025) -- moment-of-threat rejected [seizures].
- Case v. Montana, No. 24-624 (2026-01-14) -- emergency-aid, objectively-reasonable-basis, no PC [warrantexc].
- United States v. Chatrie, 609 U.S. ___ (2026), No. 25-112 -- geofence access = search; particularity remand [warrant; digital-overlap].

## Cross-lane observations (NOT filed as unit 1-5 rows -- for the diff lane / digital lane / orchestrator)
- HASH-MATCH PRIVATE-SEARCH (tripwire's own domain): a divided 4th Cir. panel held a defendant has a REP in files in a private Google Drive and that warrantless law-enforcement access in the hash-matching context is unreasonable (aligning 2d/9th Cir.; against 5th/6th Cir.); reheard EN BANC; SCOTUS GRANTED CERT 2026-01-20 (CA4 opinion 224489.p.pdf). This is the same private-search/hash split that produced the Lowers tripwire (P4-07). It is DIGITAL/private-search, not units 1-5 -- flagged so the digital lane / S6 split-map is refreshed and the diff lane can confirm it is (or is not) accounted. Docket differs from Lowers (22-4489 vs 24-4546); likely companion.
- CONTINUED-RETENTION-OF-SEIZED-PROPERTY split (9th/DC Cir. apply Fourth Amendment reasonableness to ongoing retention; 1st/2d/6th/7th/11th limit it to the initial seizure) -- property/civil-remedies grain, not seizures-of-persons; belongs to the civil-remedies I5 unit (already ran). Flagged, not filed here.
- United States v. Sultanov (E.D.N.Y. 2025) -- district court requiring a warrant for border device searches; DIGITAL/device + non-appellate; out of scope, noted.

## Confidence / verification notes for the orchestrator serial-CL lane
- Exact reporter cites flagged "pending verification" (no F.4th pin from open-web results): Parkerson (5th Cir. 2025), Rahmings (11th Cir. 2024-07-31), Burnett (7th Cir. 2025-01-13), Wilson (5th Cir. 2025), Smith (5th Cir. 2024). All have a corroborating secondary source in `discovery_path`; captions + court + approximate date are firm.
- Node/split markers (no single controlling caption): Franks-omissions (standards), open-fields reexamination (searches), Long Lake/Maxon drone (searches; STATE), Mumford dog-interior split (searches; cert-denied state case), prolonged-seizure/Rodriguez split (seizures). Filed at low/medium confidence as doctrine-ferment the wiki should carry; not asserted as new binding federal holdings.
- Two-key gate reminder: rows here are the CLAUDE key only. Orchestrator diff vs S6 saturation logs + codex lane, then serial-CL verification of any not-accounted two-key find, per P4-08.
