# S9 P2 — Discordance Adjudication Queue

> Lane `s9-p2-reconcile` · model `claude-opus-4-8` · spec S9 R5. Mechanical reconciliation of Thread-P (built corpus) vs Thread-N (blind re-derivation). Every candidate below is for the **orchestrator** to adjudicate (what diverged / which stands). The script fails toward candidate and never buries a conflict.

## Summary

- Case classes: {"CONCORDANT-STRONG": 298, "CONCORDANT-WEAK": 41, "DISCORDANT-candidate": 69, "UNREADABLE": 200, "JOIN-MISS": 1}
- Case discordance kinds: {"identity-absent": 10, "presence-absence": 10, "identity-caption": 60, "holding-overlap-zero": 2}
- Doctrine classes: {"N-SKIP-DISPOSITION": 36, "CONCORDANT-WEAK": 65, "DISCORDANT-candidate": 14}
- Doctrine coverage-gap classes: {"homed-elsewhere": 372, "N-unverified": 50, "known-ledger:brief-mention": 22, "UNKNOWN-gap": 1, "known-ledger:unverifiable": 1}
- Doctrine over-inclusion classes: {"over-inclusion-candidate": 43, "n-blind-unread": 122, "expected-role": 78}
- No-regression floor satisfied: **True** (724/724 P items dispositioned; JOIN-MISS=1)
- Residual (reads sweeping): UNREADABLE=200 cases; parse status {"parsed": 804, "no_cached_text": 312, "no_read": 95, "repaired": 2}

## JOIN-MISS (P items with no N disposition — no-regression floor)

- `P-c-0f8ce8cf0f1c` **Silverman v. United States** (case) — cases/Silverman v. United States.md

## Case discordance candidates (judgment grain)

### presence-absence  (10)

- **Florence v. County of Burlington** (566 U.S. 318 (2012)) `P-c-1850eaa2144b` — kinds: **identity-absent,identity-caption,presence-absence**
    - P holding: Jail officials may conduct a close visual strip search of every arrestee admitted to the general population without reasonable suspicion, regardless of the minor nature of the offense; the Fourth and Fourteenth Amendment
    - N: lens A: match=False present=True disp='affirmed' oc=0.625 | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Florence v. County of Burlington.md, N-A:codex-A-read-p1-prod-77cb05a8::parsed::/Users/johngalt/cssi-lake/cache/text/626454.txt, N-B:codex-B-read-p1-prod-77cb05a8::parsed::/Users/johngalt/cssi-lake/cache/text/626454.txt

- **Berghuis v. Thompkins** () `P-c-358c5ce11e7c` — kinds: **identity-absent,presence-absence**
    - P holding: The right to remain silent must be invoked UNAMBIGUOUSLY; merely staying silent does not invoke it, and a suspect who answers questions…
    - N: lens A: match=None present=False disp=None oc=None | lens B: match=True present=True disp='reversed and remanded with instructions to deny the petition' oc=0.545
    - refs: P:cases/Berghuis v. Thompkins.md, N-A:codex-A-read-p1-prod-c9440923::parsed::/Users/johngalt/cssi-lake/cache/text/6680916.txt, N-B:codex-B-read-p1-prod-c9440923::parsed::/Users/johngalt/cssi-lake/cache/text/6680916.txt

- **Florida v. Harris** (568 U.S. 237 (2013)) `P-c-4b4c7c0d6334` — kinds: **identity-absent,presence-absence**
    - P holding: Whether a dog's alert furnishes probable cause is a totality-of-the-circumstances question; evidence of a dog's satisfactory performance…
    - N: lens A: match=None present=False disp=None oc=None | lens B: match=True present=True disp='Reversed.' oc=0.727
    - refs: P:cases/Florida v. Harris.md, N-A:codex-A-read-p1-prod-a72a9e5c::parsed::/Users/johngalt/cssi-lake/cache/text/820744.txt, N-B:codex-B-read-p1-prod-a72a9e5c::parsed::/Users/johngalt/cssi-lake/cache/text/820744.txt

- **Corley v. United States** (556 U.S. 303 (2009)) `P-c-6ce3b2f6d858` — kinds: **identity-absent,presence-absence**
    - P holding: 18 U.S.C. §3501 modified but did not supplant the McNabb-Mallory rule: a federal confession made before presentment and more than six hours after arrest must be suppressed if the presentment delay was unreasonable or unn
    - N: lens A: match=True present=True disp='vacated and remanded' oc=0.75 | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Corley v. United States.md, N-A:codex-A-read-p1-prod-a0136c04::parsed::/Users/johngalt/cssi-lake/cache/text/145888.txt, N-B:codex-B-read-p1-prod-a0136c04::parsed::/Users/johngalt/cssi-lake/cache/text/145888.txt

- **Lange v. California** (594 U.S. 295 (2021)) `P-c-705f05b72e63` — kinds: **identity-absent,presence-absence**
    - P holding: Pursuit of a fleeing MISDEMEANOR suspect does not categorically justify warrantless home entry; courts apply a case-by-case exigency…
    - N: lens A: match=None present=False disp=None oc=None | lens B: match=True present=True disp='Vacated and remanded.' oc=0.5
    - refs: P:cases/Lange v. California.md, N-A:codex-A-read-p1-prod-b7fee323::parsed::/Users/johngalt/cssi-lake/cache/text/4698186.txt, N-B:codex-B-read-p1-prod-b7fee323::parsed::/Users/johngalt/cssi-lake/cache/text/4698186.txt

- **California v. Carney** (471 U.S. 386 (1985)) `P-c-810d6ced6f45` — kinds: **identity-absent,presence-absence**
    - P holding: The automobile exception applies to a motor home being used as a vehicle, and articulates the exception's TWO justifications: (1) ready…
    - N: lens A: match=True present=True disp='reversed and remanded' oc=0.545 | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/California v. Carney.md, N-A:codex-A-read-p1-prod-5ec485ca::parsed::/Users/johngalt/cssi-lake/cache/text/9430011.txt, N-B:codex-B-read-p1-prod-5ec485ca::parsed::/Users/johngalt/cssi-lake/cache/text/9430011.txt

- **Jacobson v. United States** (503 U.S. 540 (1992)) `P-c-84171765a808` — kinds: **identity-absent,presence-absence**
    - P holding: Where the government induces the crime, it must prove the defendant was predisposed to commit it INDEPENDENT of, and PRIOR TO, the…
    - N: lens A: match=None present=False disp=None oc=None | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Jacobson v. United States.md, N-A:codex-A-read-p1-prod-195fe7e7::parsed::/Users/johngalt/cssi-lake/cache/text/9432514.txt, N-B:codex-B-read-p1-prod-195fe7e7::parsed::/Users/johngalt/cssi-lake/cache/text/9432514.txt

- **Colorado v. Spring** (479 U.S. 564 (1987)) `P-c-c2a80d5f9788` — kinds: **identity-absent,presence-absence**
    - P holding: A Miranda waiver is knowing and intelligent even though police did not tell the suspect all of the crimes or subjects the interrogation would cover; awareness of every possible subject of questioning is not a prerequisit
    - N: lens A: match=True present=True disp='reversed and remanded' oc=0.304 | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Colorado v. Spring.md, N-A:codex-A-read-p1-prod-744b5c4c::parsed::/Users/johngalt/cssi-lake/cache/text/9430793.txt, N-B:codex-B-read-p1-prod-744b5c4c::parsed::/Users/johngalt/cssi-lake/cache/text/9430793.txt

- **Fernandez v. California** () `P-c-d1e2ef75a534` — kinds: **identity-absent,presence-absence**
    - P holding: Randolph is limited to a PHYSICALLY PRESENT objector. Once the objecting occupant is lawfully removed (e.g., by arrest), the remaining…
    - N: lens A: match=None present=False disp=None oc=None | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Fernandez v. California.md, N-A:codex-A-read-p1-prod-c3e9cc5d::parsed::/Users/johngalt/cssi-lake/cache/text/9798884.txt, N-B:codex-B-read-p1-prod-c3e9cc5d::parsed::/Users/johngalt/cssi-lake/cache/text/9798884.txt

- **Arizona v. Gant** (556 U.S. 332 (2009)) `P-c-e7047b17d444` — kinds: **identity-absent,presence-absence**
    - P holding: Cabins Belton. A vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within…
    - N: lens A: match=True present=True disp='affirmed' oc=0.636 | lens B: match=None present=False disp=None oc=None
    - refs: P:cases/Arizona v. Gant.md, N-A:codex-A-read-p1-prod-e3eda52d::parsed::/Users/johngalt/cssi-lake/cache/text/9435359.txt, N-B:codex-B-read-p1-prod-e3eda52d::parsed::/Users/johngalt/cssi-lake/cache/text/9435359.txt


### holding-overlap-zero  (2)

- **Davis v. United States (2011)** (565 U.S. 1100 (2011)) `P-c-8591ccdde720` — kinds: **identity-caption,holding-overlap-zero**
    - P holding: The exclusionary rule does not apply to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is only later overruled, because there is no culpable police misc
    - N: lens A: match=False present=True disp='certiorari denied' oc=0.0 | lens B: match=False present=True disp='Petition for writ of certiorari denied.' oc=0.0
    - refs: P:cases/Davis v. United States (2011).md, N-A:codex-A-read-p1-prod-4c4c5d70::parsed::/Users/johngalt/cssi-lake/cache/text/7268220.txt, N-B:codex-B-read-p1-prod-4c4c5d70::parsed::/Users/johngalt/cssi-lake/cache/text/7268220.txt

- **Davis v. United States** (513 U.S. 1008 (1994)) `P-c-e9b28c3e1bd6` — kinds: **identity-caption,holding-overlap-zero**
    - P holding: A suspect must invoke the right to counsel UNAMBIGUOUSLY; an equivocal or ambiguous reference ("maybe I should talk to a lawyer") does…
    - N: lens A: match=False present=True disp='Certiorari denied.' oc=0.0 | lens B: match=False present=True disp='Certiorari denied.' oc=0.0
    - refs: P:cases/Davis v. United States.md, N-A:codex-A-read-p1-prod-aa20c106::parsed::/Users/johngalt/cssi-lake/cache/text/9143409.txt, N-B:codex-B-read-p1-prod-aa20c106::parsed::/Users/johngalt/cssi-lake/cache/text/9143409.txt


### identity-caption  (57)

- **Weeks v. United States** (232 U.S. 383 (1914)) `P-c-0105ecdd26bb` — kinds: **identity-caption**
    - P holding: Origin of the federal exclusionary rule: evidence obtained in violation of the Fourth Amendment is inadmissible against a defendant in…
    - N: lens A: match=False present=True disp='Reversed and remanded for further proceedings.' oc=0.4 | lens B: match=False present=True disp='reversed and remanded' oc=0.3
    - refs: P:cases/Weeks v. United States.md, N-A:codex-A-read-p1-prod-6b9b1e17::parsed::/Users/johngalt/cssi-lake/cache/text/98094.txt, N-B:codex-B-read-p1-prod-6b9b1e17::parsed::/Users/johngalt/cssi-lake/cache/text/98094.txt

- **Camara v. Municipal Court** (387 U.S. 523 (1967)) `P-c-089fe95b62a6` — kinds: **identity-caption**
    - P holding: Administrative inspections of private property generally require a warrant, but it may be an "area warrant" issued on reasonable…
    - N: lens A: match=False present=True disp='vacated and remanded for further proceedings not inconsistent with the opinion' oc=0.8 | lens B: match=False present=True disp='judgment vacated and case remanded' oc=0.5
    - refs: P:cases/Camara v. Municipal Court.md, N-A:codex-A-read-p1-prod-65584209::parsed::/Users/johngalt/cssi-lake/cache/text/107473.txt, N-B:codex-B-read-p1-prod-65584209::parsed::/Users/johngalt/cssi-lake/cache/text/107473.txt

- **Kuhlmann v. Wilson** (477 U.S. 436 (1986)) `P-c-093a99438fca` — kinds: **identity-caption**
    - P holding: A defendant does not make out a Sixth Amendment violation merely by showing an informant reported his statements; he must show the…
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.5 | lens B: match=False present=True disp='reversed and remanded' oc=0.5
    - refs: P:cases/Kuhlmann v. Wilson.md, N-A:codex-A-read-p1-prod-e81bb257::parsed::/Users/johngalt/cssi-lake/cache/text/9430620.txt, N-B:codex-B-read-p1-prod-e81bb257::parsed::/Users/johngalt/cssi-lake/cache/text/9430620.txt

- **Illinois v. Andreas** (463 U.S. 765 (1983)) `P-c-0d7c37da8058` — kinds: **identity-caption**
    - P holding: Reopening a container after a lawful controlled delivery is not a new search where no substantial likelihood exists that the contents changed during a gap in surveillance — the earlier lawful inspection already extinguis
    - N: lens A: match=False present=True disp='Reversed and remanded.' oc=0.571 | lens B: match=True present=True disp='reversed and remanded' oc=0.524
    - refs: P:cases/Illinois v. Andreas.md, N-A:codex-A-read-p1-prod-d295fae2::parsed::/Users/johngalt/cssi-lake/cache/text/9429344.txt, N-B:codex-B-read-p1-prod-d295fae2::parsed::/Users/johngalt/cssi-lake/cache/text/9429344.txt

- **Illinois v. Lafayette** (462 U.S. 640 (1983)) `P-c-10d6e98cbe5c` — kinds: **identity-caption**
    - P holding: As part of the routine booking/incarceration process (a stationhouse inventory), police may search any container or article in an…
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.545 | lens B: match=True present=True disp='Reversed and remanded.' oc=0.545
    - refs: P:cases/Illinois v. Lafayette.md, N-A:codex-A-read-p1-prod-5e07abce::parsed::/Users/johngalt/cssi-lake/cache/text/9429258.txt, N-B:codex-B-read-p1-prod-5e07abce::parsed::/Users/johngalt/cssi-lake/cache/text/9429258.txt

- **Michigan v. Thomas** (458 U.S. 259 (1982)) `P-c-177deef1b971` — kinds: **identity-caption**
    - P holding: The automobile exception permits a warrantless search of an impounded car at the station on probable cause; the justification does not vanish once the car is immobilized and no separate showing of exigency is required.
    - N: lens A: match=False present=True disp='Reversed and remanded' oc=0.389 | lens B: match=True present=True disp='Certiorari and leave to proceed in forma pauperis granted; judgment of the Michigan Court of Appeals reversed; case remanded.' oc=0.556
    - refs: P:cases/Michigan v. Thomas.md, N-A:codex-A-read-p1-prod-fff39f3c::parsed::/Users/johngalt/cssi-lake/cache/text/110776.txt, N-B:codex-B-read-p1-prod-fff39f3c::parsed::/Users/johngalt/cssi-lake/cache/text/110776.txt

- **Bivens v. Six Unknown Named Agents** (403 U.S. 388 (1971)) `P-c-181e7b00a896` — kinds: **identity-caption**
    - P holding: A victim of a Fourth Amendment violation by federal officers acting under color of federal authority may recover money damages directly under the Constitution — the implied federal-officer analog to § 1983.
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.444 | lens B: match=True present=True disp='reversed and remanded' oc=0.556
    - refs: P:cases/Bivens v. Six Unknown Named Agents.md, N-A:codex-A-read-p1-prod-1fb31236::parsed::/Users/johngalt/cssi-lake/cache/text/108375.txt, N-B:codex-B-read-p1-prod-1fb31236::parsed::/Users/johngalt/cssi-lake/cache/text/108375.txt

- **Michigan Dept. of State Police v. Sitz** (496 U.S. 444 (1990)) `P-c-1a40a25b320d` — kinds: **identity-caption**
    - P holding: Suspicionless sobriety (DUI) checkpoints are constitutional; the state's interest in combating drunk driving and the checkpoint's…
    - N: lens A: match=False present=True disp='Reversed and remanded for further proceedings not inconsistent with the opinion.' oc=0.455 | lens B: match=True present=True disp='reversed and remanded' oc=0.545
    - refs: P:cases/Michigan Dept. of State Police v. Sitz.md, N-A:codex-A-read-p1-prod-33afbb85::parsed::/Users/johngalt/cssi-lake/cache/text/9432063.txt, N-B:codex-B-read-p1-prod-33afbb85::parsed::/Users/johngalt/cssi-lake/cache/text/9432063.txt

- **Michigan v. Summers** (452 U.S. 692 (1981)) `P-c-22da1b6b0273` — kinds: **identity-caption**
    - P holding: A warrant to search premises for contraband, founded on probable cause, implicitly carries the limited authority to detain the occupants…
    - N: lens A: match=False present=True disp='Reversed the judgment of the Supreme Court of Michigan.' oc=0.462 | lens B: match=True present=True disp='Reversed' oc=0.692
    - refs: P:cases/Michigan v. Summers.md, N-A:codex-A-read-p1-prod-51e23485::parsed::/Users/johngalt/cssi-lake/cache/text/9428436.txt, N-B:codex-B-read-p1-prod-51e23485::parsed::/Users/johngalt/cssi-lake/cache/text/9428436.txt

- **Minnesota v. Dickerson** (508 U.S. 366 (1993)) `P-c-2bb931ce2beb` — kinds: **identity-caption**
    - P holding: Plain-feel corollary: contraband whose identity is immediately apparent by touch during a lawful *Terry* frisk may be seized — but not where the officer squeezed/manipulated it to ID it.
    - N: lens A: match=False present=True disp='affirmed' oc=0.625 | lens B: match=True present=True disp='affirmed' oc=0.562
    - refs: P:cases/Minnesota v. Dickerson.md, N-A:codex-A-read-p1-prod-1205b67e::parsed::/Users/johngalt/cssi-lake/cache/text/9432823.txt, N-B:codex-B-read-p1-prod-1205b67e::parsed::/Users/johngalt/cssi-lake/cache/text/9432823.txt

- **Beecher v. Alabama** (389 U.S. 35 (1967)) `P-c-3009489be342` — kinds: **identity-caption**
    - P holding: A confession obtained at gunpoint from a wounded suspect threatened with death, and a second statement signed five days later while drugged on morphine and in intense pain with no break in the stream of events, are the p
    - N: lens A: match=False present=True disp='Motion for leave to proceed in forma pauperis and petition for certiorari granted; judgment reversed.' oc=0.269 | lens B: match=False present=True disp='in forma pauperis and certiorari granted; judgment reversed' oc=0.4
    - refs: P:cases/Beecher v. Alabama.md, N-A:codex-A-read-p1-prod-778b99b3::parsed::/Users/johngalt/cssi-lake/cache/text/9423505.txt, N-B:codex-B-read-p1-prod-778b99b3::parsed::/Users/johngalt/cssi-lake/cache/text/9423505.txt

- **Mathis v. United States (1968)** (391 U.S. 1 (1968)) `P-c-3582d3b5d89f` — kinds: **identity-caption**
    - P holding: Miranda warnings are required when a person already in custody (here, serving a prison sentence) is interrogated by officers, even though the questioning concerns an entirely separate matter and even though it is a routi
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.5 | lens B: match=False present=True disp='reversed and remanded' oc=0.429
    - refs: P:cases/Mathis v. United States (1968).md, N-A:codex-A-read-p1-prod-89435ef6::parsed::/Users/johngalt/cssi-lake/cache/text/9423682.txt, N-B:codex-B-read-p1-prod-89435ef6::parsed::/Users/johngalt/cssi-lake/cache/text/9423682.txt

- **Miranda v. Arizona** (384 U.S. 436 (1966)) `P-c-4003da473d51` — kinds: **identity-caption**
    - P holding: Statements from custodial interrogation are inadmissible unless police first gave the warnings and the suspect knowingly, voluntarily…
    - N: lens A: match=False present=True disp='Reversed in Nos. 759, 760, and 761; affirmed in No. 584.' oc=0.417 | lens B: match=True present=True disp='Reversed as to Nos. 759, 760, and 761; affirmed as to No. 584.' oc=0.583
    - refs: P:cases/Miranda v. Arizona.md, N-A:codex-A-read-p1-prod-35d87ee3::parsed::/Users/johngalt/cssi-lake/cache/text/9423233.txt, N-B:codex-B-read-p1-prod-35d87ee3::parsed::/Users/johngalt/cssi-lake/cache/text/9423233.txt

- **Wilson v. Arkansas** (514 U.S. 927 (1995)) `P-c-407775502f86` — kinds: **identity-caption**
    - P holding: The common-law **knock-and-announce** principle — that officers must announce their presence and authority before forcibly entering a…
    - N: lens A: match=False present=True disp='Reversed and remanded.' oc=0.5 | lens B: match=True present=True disp='Reversed and remanded.' oc=0.5
    - refs: P:cases/Wilson v. Arkansas.md, N-A:codex-A-read-p1-prod-e6899457::parsed::/Users/johngalt/cssi-lake/cache/text/117936.txt, N-B:codex-B-read-p1-prod-e6899457::parsed::/Users/johngalt/cssi-lake/cache/text/117936.txt

- **Marbury v. Madison** (5 U.S. 137 (1803)) `P-c-45b88cf5126c` — kinds: **identity-caption**
    - P holding: Establishes judicial review: it is the province and duty of the judiciary to say what the law is, and a law repugnant to the…
    - N: lens A: match=False present=True disp='Rule discharged; mandamus not issued.' oc=0.0 | lens B: match=False present=True disp='rule discharged; mandamus denied' oc=0.2
    - refs: P:cases/Marbury v. Madison.md, N-A:codex-A-read-p1-prod-e7c53de0::parsed::/Users/johngalt/cssi-lake/cache/text/84759.txt, N-B:codex-B-read-p1-prod-e7c53de0::parsed::/Users/johngalt/cssi-lake/cache/text/84759.txt

- **Illinois v. Perkins** (496 U.S. 292 (1990)) `P-c-46b27bfdca48` — kinds: **identity-caption**
    - P holding: Miranda warnings are not required when an undercover officer (or agent) posing as an inmate elicits statements from a suspect — because…
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.727 | lens B: match=True present=True disp='reversed and remanded' oc=0.818
    - refs: P:cases/Illinois v. Perkins.md, N-A:codex-A-read-p1-prod-33a94e78::parsed::/Users/johngalt/cssi-lake/cache/text/9432050.txt, N-B:codex-B-read-p1-prod-33a94e78::parsed::/Users/johngalt/cssi-lake/cache/text/9432050.txt

- **Rhode Island v. Innis** (446 U.S. 291 (1980)) `P-c-4890ad8bd485` — kinds: **identity-caption**
    - P holding: 'Interrogation' under Miranda is not limited to express questioning. It also includes the 'functional equivalent' of express…
    - N: lens A: match=False present=True disp='Judgment of the Supreme Court of Rhode Island vacated; case remanded for further proceedings not inconsistent with the opinion.' oc=0.875 | lens B: match=True present=True disp='vacated and remanded' oc=0.875
    - refs: P:cases/Rhode Island v. Innis.md, N-A:codex-A-read-p1-prod-2a086788::parsed::/Users/johngalt/cssi-lake/cache/text/9427901.txt, N-B:codex-B-read-p1-prod-2a086788::parsed::/Users/johngalt/cssi-lake/cache/text/9427901.txt

- **Turner v. United States** () `P-c-4fab2afeb7b5` — kinds: **identity-caption**
    - P holding: Counterweight: *Brady* materiality is demanding and judged on the whole record; the suppression here was immaterial — no *Brady* violation.
    - N: lens A: match=False present=True disp='affirmed' oc=0.273 | lens B: match=True present=True disp='affirmed' oc=0.273
    - refs: P:cases/Turner v. United States.md, N-A:codex-A-read-p1-prod-8cb2305d::parsed::/Users/johngalt/cssi-lake/cache/text/4181055.txt, N-B:codex-B-read-p1-prod-8cb2305d::parsed::/Users/johngalt/cssi-lake/cache/text/4181055.txt

- **Benn v. Lambert** (283 F.3d 1040 (2002)) `P-c-502f01ba43f4` — kinds: **identity-caption**
    - P holding: Granted habeas relief: the prosecution suppressed BOTH material exculpatory evidence (expert evidence on the cause of the fire) AND…
    - N: lens A: match=False present=True disp="AFFIRMED; the district court's grant of habeas corpus and order for a new trial were affirmed." oc=0.583 | lens B: match=False present=True disp='affirmed' oc=0.667
    - refs: P:cases/Benn v. Lambert.md, N-A:codex-A-read-p1-prod-98bba5db::parsed::/Users/johngalt/cssi-lake/cache/text/9494850.txt, N-B:codex-B-read-p1-prod-98bba5db::parsed::/Users/johngalt/cssi-lake/cache/text/9494850.txt

- **Murray v. United States** (487 U.S. 533 (1988)) `P-c-50d1be85abee` — kinds: **identity-caption**
    - P holding: Independent source: evidence first observed during an unlawful entry is admissible if later acquired through a genuinely independent…
    - N: lens A: match=False present=True disp='vacated and remanded' oc=0.769 | lens B: match=True present=True disp='Vacated and remanded with instructions for the Court of Appeals to remand to the District Court for an independent-source determination.' oc=0.692
    - refs: P:cases/Murray v. United States.md, N-A:codex-A-read-p1-prod-d8001fd5::parsed::/Users/johngalt/cssi-lake/cache/text/9431434.txt, N-B:codex-B-read-p1-prod-d8001fd5::parsed::/Users/johngalt/cssi-lake/cache/text/9431434.txt

- **Olmstead v. United States** (277 U.S. 438 (1928)) `P-c-518245dfdebf` — kinds: **identity-caption**
    - P holding: Wiretapping with no physical entry was not a search — pure property/trespass framing; overruled on the privacy point by *Katz* (property instinct later revived by *Jones*).
    - N: lens A: match=False present=True disp='affirmed' oc=0.125 | lens B: match=False present=True disp='affirmed' oc=0.188
    - refs: P:cases/Olmstead v. United States.md, N-A:codex-A-read-p1-prod-d4ad4606::parsed::/Users/johngalt/cssi-lake/cache/text/101320.txt, N-B:codex-B-read-p1-prod-d4ad4606::parsed::/Users/johngalt/cssi-lake/cache/text/101320.txt

- **Berkemer v. McCarty** (468 U.S. 420 (1984)) `P-c-52c52de12d13` — kinds: **identity-caption**
    - P holding: (1) Miranda applies to ALL custodial interrogation regardless of the offense's severity — misdemeanors included; (2) the temporary,…
    - N: lens A: match=False present=True disp='Affirmed.' oc=0.5 | lens B: match=False present=True disp='Affirmed' oc=0.5
    - refs: P:cases/Berkemer v. McCarty.md, N-A:codex-A-read-p1-prod-674a91a7::parsed::/Users/johngalt/cssi-lake/cache/text/9429728.txt, N-B:codex-B-read-p1-prod-674a91a7::parsed::/Users/johngalt/cssi-lake/cache/text/9429728.txt

- **United States v. Smith (2024)** (110 F.4th 817 (2024)) `P-c-5f4962e7d0be` — kinds: **identity-caption**
    - P holding: Acquiring Google Location History through a geofence warrant is a Fourth Amendment search under Carpenter, and geofence warrants — which identify everyone in an area rather than a particularized suspect — are modern-day 
    - N: lens A: match=False present=True disp='AFFIRMED' oc=0.469 | lens B: match=True present=True disp='affirmed' oc=0.5
    - refs: P:cases/United States v. Smith (2024).md, N-A:codex-A-read-p1-prod-274c4b5f::parsed::/Users/johngalt/cssi-lake/cache/text/10502720.txt, N-B:codex-B-read-p1-prod-274c4b5f::parsed::/Users/johngalt/cssi-lake/cache/text/10502720.txt

- **Pennsylvania v. Mimms** (434 U.S. 106 (1977)) `P-c-64cb408fe994` — kinds: **identity-caption**
    - P holding: Once a vehicle is lawfully stopped for a traffic violation, an officer may order the driver out of the vehicle as a matter of course;…
    - N: lens A: match=False present=True disp='in forma pauperis granted; certiorari granted; judgment reversed and remanded' oc=0.417 | lens B: match=True present=True disp='Certiorari granted; judgment of the Supreme Court of Pennsylvania reversed; remanded for further proceedings not inconsistent with the opinion.' oc=0.417
    - refs: P:cases/Pennsylvania v. Mimms.md, N-A:codex-A-read-p1-prod-ee61fad9::parsed::/Users/johngalt/cssi-lake/cache/text/9427002.txt, N-B:codex-B-read-p1-prod-ee61fad9::parsed::/Users/johngalt/cssi-lake/cache/text/9427002.txt

- **Preston v. United States** (376 U.S. 364 (1964)) `P-c-666f755e4536` — kinds: **identity-caption**
    - P holding: A warrantless search of a vehicle is not a valid search incident to arrest once the arrestee is in custody and the car has been removed; a search remote in time or place from the arrest cannot be justified as incident to
    - N: lens A: match=False present=True disp='Reversed and remanded.' oc=0.625 | lens B: match=True present=True disp='Reversed and remanded.' oc=0.625
    - refs: P:cases/Preston v. United States.md, N-A:codex-A-read-p1-prod-e3d0482a::parsed::/Users/johngalt/cssi-lake/cache/text/106771.txt, N-B:codex-B-read-p1-prod-e3d0482a::parsed::/Users/johngalt/cssi-lake/cache/text/106771.txt

- **Hester v. United States** (265 U.S. 57 (1924)) `P-c-6a78d4144604` — kinds: **identity-caption**
    - P holding: Origin of the open-fields doctrine — 4A protection of 'persons, houses, papers, and effects' does not extend to open fields; and a fleeing suspect who drops containers abandons any 4A interest in them.
    - N: lens A: match=False present=True disp='affirmed' oc=0.312 | lens B: match=False present=True disp='affirmed' oc=0.312
    - refs: P:cases/Hester v. United States.md, N-A:codex-A-read-p1-prod-7bdddc0f::parsed::/Users/johngalt/cssi-lake/cache/text/100413.txt, N-B:codex-B-read-p1-prod-7bdddc0f::parsed::/Users/johngalt/cssi-lake/cache/text/100413.txt

- **Donovan v. Dewey** (452 U.S. 594 (1981)) `P-c-6b001d9f647b` — kinds: **identity-caption**
    - P holding: Warrantless inspections of a pervasively regulated industry (mines) are reasonable where a comprehensive statutory scheme — defining the certainty, regularity, frequency, and scope of inspection — provides a constitution
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.381 | lens B: match=False present=True disp='Reversed and remanded.' oc=0.381
    - refs: P:cases/Donovan v. Dewey.md, N-A:codex-A-read-p1-prod-89923788::parsed::/Users/johngalt/cssi-lake/cache/text/9428427.txt, N-B:codex-B-read-p1-prod-89923788::parsed::/Users/johngalt/cssi-lake/cache/text/9428427.txt

- **United States v. Santana** (427 U.S. 38 (1976)) `P-c-6b2c12922789` — kinds: **identity-caption**
    - P holding: A suspect standing in her own doorway/threshold is in a 'public' place for Fourth Amendment purposes; she cannot defeat a lawful arrest…
    - N: lens A: match=False present=True disp='reversed' oc=0.429 | lens B: match=True present=True disp='Reversed' oc=0.5
    - refs: P:cases/United States v. Santana.md, N-A:codex-A-read-p1-prod-086e185a::parsed::/Users/johngalt/cssi-lake/cache/text/109504.txt, N-B:codex-B-read-p1-prod-086e185a::parsed::/Users/johngalt/cssi-lake/cache/text/109504.txt

- **Illinois v. Wardlow** (528 U.S. 119 (2000)) `P-c-7c03eb3e6ec1` — kinds: **identity-caption**
    - P holding: Unprovoked headlong flight upon noticing police, combined with presence in a high-crime area, can furnish reasonable suspicion for a…
    - N: lens A: match=True present=True disp='Reversed and remanded.' oc=0.462 | lens B: match=False present=True disp='Reversed and remanded' oc=0.615
    - refs: P:cases/Illinois v. Wardlow.md, N-A:codex-A-read-p1-prod-d362a1cc::parsed::/Users/johngalt/cssi-lake/cache/text/9433881.txt, N-B:codex-B-read-p1-prod-d362a1cc::parsed::/Users/johngalt/cssi-lake/cache/text/9433881.txt

- **Go-Bart Importing Co. v. United States** (282 U.S. 344 (1931)) `P-c-81da3e8dc94e` — kinds: **identity-caption**
    - P holding: A search incident to arrest may not become a general exploratory search of the premises; a warrantless arrest used to justify ransacking an office for evidence is an unreasonable general search, judged on each case's own
    - N: lens A: match=False present=True disp='Reversed and remanded with directions to enjoin use of the papers as evidence and order their return to petitioners.' oc=0.412 | lens B: match=False present=True disp='Reversed and remanded with directions to enjoin use of the papers as evidence and order their return to petitioners.' oc=0.412
    - refs: P:cases/Go-Bart Importing Co. v. United States.md, N-A:codex-A-read-p1-prod-16cb61d5::parsed::/Users/johngalt/cssi-lake/cache/text/101643.txt, N-B:codex-B-read-p1-prod-16cb61d5::parsed::/Users/johngalt/cssi-lake/cache/text/101643.txt

- **Sorrells v. United States** (287 U.S. 435 (1932)) `P-c-91dd80ddd9ff` — kinds: **identity-caption**
    - P holding: Entrapment is a valid defense; it arises when government officials implant the criminal design in the mind of a person who had no…
    - N: lens A: match=False present=True disp='Reversed and remanded for further proceedings.' oc=0.364 | lens B: match=False present=True disp='Reversed and remanded for further proceedings in conformity with the opinion.' oc=0.455
    - refs: P:cases/Sorrells v. United States.md, N-A:codex-A-read-p1-prod-5477268d::parsed::/Users/johngalt/cssi-lake/cache/text/101997.txt, N-B:codex-B-read-p1-prod-5477268d::parsed::/Users/johngalt/cssi-lake/cache/text/101997.txt

- **Lefkowitz v. Turley** (414 U.S. 70 (1973)) `P-c-93000c94817c` — kinds: **identity-caption**
    - P holding: A State may not compel a person (employee or contractor) to choose between waiving Fifth Amendment immunity and losing state employment or contracts; it may compel testimony about official functions only by granting use-
    - N: lens A: match=False present=True disp='affirmed' oc=0.364 | lens B: match=True present=True disp='affirmed' oc=0.364
    - refs: P:cases/Lefkowitz v. Turley.md, N-A:codex-A-read-p1-prod-217cec83::parsed::/Users/johngalt/cssi-lake/cache/text/108882.txt, N-B:codex-B-read-p1-prod-217cec83::parsed::/Users/johngalt/cssi-lake/cache/text/108882.txt

- **Florida v. Wells** (495 U.S. 1 (1990)) `P-c-961d843346f0` — kinds: **identity-caption**
    - P holding: An inventory search must not be a ruse for general rummaging to discover incriminating evidence; standardized criteria or established…
    - N: lens A: match=False present=True disp='affirmed' oc=0.455 | lens B: match=True present=True disp='affirmed' oc=0.455
    - refs: P:cases/Florida v. Wells.md, N-A:codex-A-read-p1-prod-7bbb6b70::parsed::/Users/johngalt/cssi-lake/cache/text/9431971.txt, N-B:codex-B-read-p1-prod-7bbb6b70::parsed::/Users/johngalt/cssi-lake/cache/text/9431971.txt

- **Hampton v. United States** (425 U.S. 484 (1976)) `P-c-9bbc384b4adb` — kinds: **identity-caption**
    - P holding: Neither the entrapment defense nor the Due Process Clause bars conviction of a PREDISPOSED defendant even where a government agent…
    - N: lens A: match=False present=True disp='Affirmed' oc=0.462 | lens B: match=True present=True disp='Affirmed.' oc=0.615
    - refs: P:cases/Hampton v. United States.md, N-A:codex-A-read-p1-prod-89ae6387::parsed::/Users/johngalt/cssi-lake/cache/text/9426380.txt, N-B:codex-B-read-p1-prod-89ae6387::parsed::/Users/johngalt/cssi-lake/cache/text/9426380.txt

- **United States v. Sandoval** (200 F.3d 659 (2000)) `P-c-a6704648359b` — kinds: **identity-caption**
    - P holding: (Persuasive (outside circuit) — 9th Cir.) A reasonable expectation of privacy in a tent on public (BLM) land does not turn on whether the camper had permission to be there; denial of suppression reversed.
    - N: lens A: match=False present=True disp='reversed and remanded for a new trial' oc=0.368 | lens B: match=True present=True disp='reversed and remanded for a new trial' oc=0.474
    - refs: P:cases/United States v. Sandoval.md, N-A:codex-A-read-p1-prod-ca68dd30::parsed::/Users/johngalt/cssi-lake/cache/text/767260.txt, N-B:codex-B-read-p1-prod-ca68dd30::parsed::/Users/johngalt/cssi-lake/cache/text/767260.txt

- **Mooney v. Holohan** (294 U.S. 103 (1935)) `P-c-a8ac55ae4faa` — kinds: **identity-caption**
    - P holding: The knowing use of perjured testimony by the prosecution to obtain a conviction violates Fourteenth Amendment due process — a 'deliberate deception of court and jury' is as inconsistent with justice as obtaining a convic
    - N: lens A: match=False present=True disp='leave to file petition denied without prejudice' oc=0.379 | lens B: match=False present=True disp='leave to file petition for original writ of habeas corpus denied without prejudice' oc=0.414
    - refs: P:cases/Mooney v. Holohan.md, N-A:codex-A-read-p1-prod-99beb8d6::parsed::/Users/johngalt/cssi-lake/cache/text/102372.txt, N-B:codex-B-read-p1-prod-99beb8d6::parsed::/Users/johngalt/cssi-lake/cache/text/102372.txt

- **New York v. Belton** (453 U.S. 454 (1981)) `P-c-ac946df6e406` — kinds: **identity-caption**
    - P holding: Defines the SCOPE of a vehicle search incident to arrest: on a lawful custodial arrest of a vehicle occupant, police may search the…
    - N: lens A: match=False present=True disp='reversed' oc=0.7 | lens B: match=True present=True disp='reversed' oc=0.6
    - refs: P:cases/New York v. Belton.md, N-A:codex-A-read-p1-prod-6401ca3c::parsed::/Users/johngalt/cssi-lake/cache/text/9428488.txt, N-B:codex-B-read-p1-prod-6401ca3c::parsed::/Users/johngalt/cssi-lake/cache/text/9428488.txt

- **Lo-Ji Sales, Inc. v. New York** (442 U.S. 319 (1979)) `P-c-adf90e71a26e` — kinds: **identity-caption**
    - P holding: A magistrate who abandons the neutral-and-detached role — here the Town Justice joined and effectively led the search party, conducting…
    - N: lens A: match=False present=True disp='reversed and remanded' oc=0.429 | lens B: match=True present=True disp='Reversed and remanded.' oc=0.357
    - refs: P:cases/Lo-Ji Sales, Inc. v. New York.md, N-A:codex-A-read-p1-prod-04138d99::parsed::/Users/johngalt/cssi-lake/cache/text/110100.txt, N-B:codex-B-read-p1-prod-04138d99::parsed::/Users/johngalt/cssi-lake/cache/text/110100.txt

- **Michigan v. Chesternut** (486 U.S. 567 (1988)) `P-c-b0a889a19e56` — kinds: **identity-caption**
    - P holding: Police pursuit, standing alone, is not a Fourth Amendment seizure; whether police conduct is a seizure is determined by the Mendenhall objective test — whether, in all the circumstances, a reasonable person would have be
    - N: lens A: match=False present=True disp='Reversed and remanded.' oc=0.667 | lens B: match=True present=True disp='reversed and remanded' oc=0.444
    - refs: P:cases/Michigan v. Chesternut.md, N-A:codex-A-read-p1-prod-9065f420::parsed::/Users/johngalt/cssi-lake/cache/text/9431339.txt, N-B:codex-B-read-p1-prod-9065f420::parsed::/Users/johngalt/cssi-lake/cache/text/9431339.txt

- **Michigan v. Tucker** (417 U.S. 433 (1974)) `P-c-b91d350e5d27` — kinds: **identity-caption**
    - P holding: The 'fruits' of a mere prophylactic Miranda violation — here, a witness whose identity was learned from a statement taken with incomplete warnings — need not be suppressed where the statement was voluntary and not actual
    - N: lens A: match=False present=True disp='Reversed' oc=0.304 | lens B: match=False present=True disp='reversed' oc=0.304
    - refs: P:cases/Michigan v. Tucker.md, N-A:codex-A-read-p1-prod-a4fdd5ea::parsed::/Users/johngalt/cssi-lake/cache/text/9425753.txt, N-B:codex-B-read-p1-prod-a4fdd5ea::parsed::/Users/johngalt/cssi-lake/cache/text/9425753.txt

- **Oliver v. United States** (466 U.S. 170 (1984)) `P-c-c345c798edb4` — kinds: **identity-caption**
    - P holding: Reaffirms that open fields get no Fourth Amendment protection — even fenced, posted 'No Trespassing' land; only curtilage carries the home's protection.
    - N: lens A: match=False present=True disp='Oliver v. United States affirmed; Maine v. Thornton reversed and remanded.' oc=0.4 | lens B: match=True present=True disp='Oliver v. United States affirmed; Maine v. Thornton reversed and remanded.' oc=0.467
    - refs: P:cases/Oliver v. United States.md, N-A:codex-A-read-p1-prod-0ebfc5b3::parsed::/Users/johngalt/cssi-lake/cache/text/9429563.txt, N-B:codex-B-read-p1-prod-0ebfc5b3::parsed::/Users/johngalt/cssi-lake/cache/text/9429563.txt

- **Wong Sun v. United States** (371 U.S. 471 (1963)) `P-c-c348c635778b` — kinds: **identity-caption**
    - P holding: 'Fruit of the poisonous tree': derivative evidence is suppressed if come at by exploitation of the primary illegality, not merely 'but…
    - N: lens A: match=False present=True disp='Reversed and remanded to the District Court for further proceedings.' oc=0.091 | lens B: match=True present=True disp="Reversed and remanded to the District Court for further proceedings; Wong Sun entitled to a new trial and Toy's conviction set aside for lack of competent evidence." oc=0.0
    - refs: P:cases/Wong Sun v. United States.md, N-A:codex-A-read-p1-prod-d60c6223::parsed::/Users/johngalt/cssi-lake/cache/text/106515.txt, N-B:codex-B-read-p1-prod-d60c6223::parsed::/Users/johngalt/cssi-lake/cache/text/106515.txt

- **Frazier v. Cupp** (394 U.S. 731 (1969)) `P-c-c7d4e1426bc2` — kinds: **identity-caption**
    - P holding: Police misrepresentation (falsely telling a suspect his codefendant had confessed) did not render the confession involuntary; deception…
    - N: lens A: match=False present=True disp='affirmed' oc=0.091 | lens B: match=False present=True disp='affirmed' oc=0.091
    - refs: P:cases/Frazier v. Cupp.md, N-A:codex-A-read-p1-prod-f64ae93d::parsed::/Users/johngalt/cssi-lake/cache/text/107913.txt, N-B:codex-B-read-p1-prod-f64ae93d::parsed::/Users/johngalt/cssi-lake/cache/text/107913.txt

- **Peters v. New York** (392 U.S. 40 (1968)) `P-c-c7e1045e15af` — kinds: **identity-caption**
    - P holding: Where probable cause to arrest existed (furtive conduct and flight indicating attempted burglary), the search of the suspect was valid as incident to a lawful arrest, even though the formal arrest followed the seizure.
    - N: lens A: match=False present=True disp="Peters' conviction affirmed; Sibron's conviction reversed." oc=0.3 | lens B: match=False present=True disp='Affirmed as to Peters (No. 74); reversed as to Sibron (No. 63).' oc=0.35
    - refs: P:cases/Peters v. New York.md, N-A:codex-A-read-p1-prod-268994ca::parsed::/Users/johngalt/cssi-lake/cache/text/9423756.txt, N-B:codex-B-read-p1-prod-268994ca::parsed::/Users/johngalt/cssi-lake/cache/text/9423756.txt

- **LaChance v. Erickson** (522 U.S. 262 (1998)) `P-c-cce8f609cbe9` — kinds: **identity-caption**
    - P holding: Neither due process nor the civil-service statutes bar a federal agency from disciplining an employee for making false statements to investigators in response to an underlying misconduct charge; the right to be heard doe
    - N: lens A: match=False present=True disp='reversed' oc=0.536 | lens B: match=False present=True disp='reversed' oc=0.5
    - refs: P:cases/LaChance v. Erickson.md, N-A:codex-A-read-p1-prod-4f034674::parsed::/Users/johngalt/cssi-lake/cache/text/118163.txt, N-B:codex-B-read-p1-prod-4f034674::parsed::/Users/johngalt/cssi-lake/cache/text/118163.txt

- **Michigan v. Jackson** (475 U.S. 625 (1986)) `P-c-cdaa6d1b1878` — kinds: **identity-caption**
    - P holding: Held a post-appointment, police-initiated waiver of the Sixth Amendment right to counsel presumptively invalid — **overruled by *Montejo v. Louisiana* (2009)**; survives only as history.
    - N: lens A: match=False present=True disp='affirmed' oc=0.176 | lens B: match=True present=True disp='Affirmed.' oc=0.471
    - refs: P:cases/Michigan v. Jackson.md, N-A:codex-A-read-p1-prod-588b0da0::parsed::/Users/johngalt/cssi-lake/cache/text/9430407.txt, N-B:codex-B-read-p1-prod-588b0da0::parsed::/Users/johngalt/cssi-lake/cache/text/9430407.txt

- **Brown v. Mississippi** (297 U.S. 278 (1936)) `P-c-d3d2dbf9555d` — kinds: **identity-caption**
    - P holding: A confession extracted by physical torture is involuntary and its use to convict violates Fourteenth Amendment due process.
    - N: lens A: match=False present=True disp='Reversed' oc=0.333 | lens B: match=False present=True disp='reversed' oc=0.333
    - refs: P:cases/Brown v. Mississippi.md, N-A:codex-A-read-p1-prod-3a916683::parsed::/Users/johngalt/cssi-lake/cache/text/102604.txt, N-B:codex-B-read-p1-prod-3a916683::parsed::/Users/johngalt/cssi-lake/cache/text/102604.txt

- **Massachusetts v. Sheppard** (468 U.S. 981 (1984)) `P-c-d47225fa464d` — kinds: **identity-caption**
    - P holding: Companion to Leon: where a warrant was technically/clerically defective in form (wrong pre-printed form) but officers reasonably relied…
    - N: lens A: match=False present=True disp='Reversed and remanded for further proceedings not inconsistent with the opinion.' oc=0.462 | lens B: match=False present=True disp='reversed and remanded' oc=0.385
    - refs: P:cases/Massachusetts v. Sheppard.md, N-A:codex-A-read-p1-prod-564a1743::parsed::/Users/johngalt/cssi-lake/cache/text/111263.txt, N-B:codex-B-read-p1-prod-564a1743::parsed::/Users/johngalt/cssi-lake/cache/text/111263.txt

- **Wright v. City of Euclid** (962 F.3d 852 (2020)) `P-c-d72dc4329dbb` — kinds: **identity-caption**
    - P holding: The Sixth Circuit REVERSED summary judgment / denial of qualified immunity on multiple Fourth Amendment § 1983 claims: excessive force…
    - N: lens A: match=False present=True disp='affirmed in part, reversed in part, and remanded' oc=0.467 | lens B: match=True present=True disp='Affirmed in part, reversed in part, and remanded for further proceedings.' oc=0.6
    - refs: P:cases/Wright v. City of Euclid.md, N-A:codex-A-read-p1-prod-79bd487e::parsed::/Users/johngalt/cssi-lake/cache/text/4542480.txt, N-B:codex-B-read-p1-prod-79bd487e::parsed::/Users/johngalt/cssi-lake/cache/text/4542480.txt

- **Thompson v. Louisiana** (469 U.S. 17 (1984)) `P-c-d9189cb65e3e` — kinds: **identity-caption**
    - P holding: There is no 'murder-scene exception' to the warrant requirement; a warrantless two-hour general search of a homicide scene in a private home is unreasonable, even though shorter than the four-day search in Mincey, and th
    - N: lens A: match=False present=True disp='Reversed and remanded; leave to proceed in forma pauperis and certiorari granted.' oc=0.63 | lens B: match=False present=True disp='reversed and remanded' oc=0.593
    - refs: P:cases/Thompson v. Louisiana.md, N-A:codex-A-read-p1-prod-a7b500e3::parsed::/Users/johngalt/cssi-lake/cache/text/111282.txt, N-B:codex-B-read-p1-prod-a7b500e3::parsed::/Users/johngalt/cssi-lake/cache/text/111282.txt

- **United States v. Anchondo** (156 F.3d 1043 (1998)) `P-c-dac063437b79` — kinds: **identity-caption**
    - P holding: ACTUAL holding: cocaine found on the defendant's body was the product of a lawful SEARCH INCIDENT TO ARREST, not the automobile…
    - N: lens A: match=False present=True disp='affirmed' oc=0.636 | lens B: match=False present=True disp='affirmed' oc=0.545
    - refs: P:cases/United States v. Anchondo.md, N-A:codex-A-read-p1-prod-eb3dbe84::parsed::/Users/johngalt/cssi-lake/cache/text/758111.txt, N-B:codex-B-read-p1-prod-eb3dbe84::parsed::/Users/johngalt/cssi-lake/cache/text/758111.txt

- **Horton v. California** (496 U.S. 128 (1990)) `P-c-e0c383183059` — kinds: **identity-caption**
    - P holding: Sets the modern plain-view SEIZURE test and DROPS the inadvertence requirement: a warrantless seizure of an item in plain view is lawful…
    - N: lens A: match=False present=True disp='affirmed' oc=0.333 | lens B: match=False present=True disp='affirmed' oc=0.417
    - refs: P:cases/Horton v. California.md, N-A:codex-A-read-p1-prod-2a82e334::parsed::/Users/johngalt/cssi-lake/cache/text/9432041.txt, N-B:codex-B-read-p1-prod-2a82e334::parsed::/Users/johngalt/cssi-lake/cache/text/9432041.txt

- **Kalkines v. United States** () `P-c-e10e3a47a1f4` — kinds: **identity-caption**
    - P holding: A federal employee may be discharged for refusing to answer narrowly job-related questions only if first adequately advised both that refusal subjects him to discharge and that his answers (and their fruits) cannot be us
    - N: lens A: match=False present=True disp="Plaintiff's motion for summary judgment granted; defendant's motion denied; lost-pay recovery to be determined under Rule 131(c)." oc=0.542 | lens B: match=True present=True disp="Plaintiff's motion for summary judgment granted; defendant's motion denied; discharge held invalid; recovery of lost pay to be determined under Rule 131(c)." oc=0.583
    - refs: P:cases/Kalkines v. United States.md, N-A:codex-A-read-p1-prod-b0f151ab::parsed::/Users/johngalt/cssi-lake/cache/text/8594616.txt, N-B:codex-B-read-p1-prod-b0f151ab::parsed::/Users/johngalt/cssi-lake/cache/text/8594616.txt

- **Brown v. Texas** (443 U.S. 47 (1979)) `P-c-e344647fa8aa` — kinds: **identity-caption**
    - P holding: Police may not stop a person and demand identification without reasonable suspicion of criminal activity; the constitutionality of suspicionless seizures is judged by balancing public concern, advancement of the public i
    - N: lens A: match=False present=True disp='Reversed.' oc=0.19 | lens B: match=False present=True disp='reversed' oc=0.333
    - refs: P:cases/Brown v. Texas.md, N-A:codex-A-read-p1-prod-345aafab::parsed::/Users/johngalt/cssi-lake/cache/text/110128.txt, N-B:codex-B-read-p1-prod-345aafab::parsed::/Users/johngalt/cssi-lake/cache/text/110128.txt

- **United States v. Conner** (127 F.3d 663 (1997)) `P-c-e7a4141a490f` — kinds: **identity-caption**
    - P holding: Where police, under color of authority, demand that occupants of a motel room open the door, and an occupant opens the door not…
    - N: lens A: match=False present=True disp='affirmed' oc=0.545 | lens B: match=False present=True disp='affirmed' oc=0.455
    - refs: P:cases/United States v. Conner.md, N-A:codex-A-read-p1-prod-4f24cf48::parsed::/Users/johngalt/cssi-lake/cache/text/9490703.txt, N-B:codex-B-read-p1-prod-4f24cf48::parsed::/Users/johngalt/cssi-lake/cache/text/9490703.txt

- **Kolender v. Lawson** (461 U.S. 352 (1983)) `P-c-eb69a845fb3c` — kinds: **identity-caption**
    - P holding: A stop-and-identify statute that requires a detained suspect to provide 'credible and reliable' identification is unconstitutionally vague, because it vests police with standardless discretion to decide what satisfies it
    - N: lens A: match=False present=True disp='affirmed and remanded' oc=0.368 | lens B: match=False present=True disp='Affirmed and remanded for further proceedings consistent with the opinion.' oc=0.421
    - refs: P:cases/Kolender v. Lawson.md, N-A:codex-A-read-p1-prod-347981b7::parsed::/Users/johngalt/cssi-lake/cache/text/9429183.txt, N-B:codex-B-read-p1-prod-347981b7::parsed::/Users/johngalt/cssi-lake/cache/text/9429183.txt

- **Flippo v. West Virginia** (528 U.S. 11 (1999)) `P-c-fd4241ee242d` — kinds: **identity-caption**
    - P holding: There is no general 'crime-scene exception' to the warrant requirement; a warrantless search of a secured homicide scene (including opening a closed briefcase) is invalid unless a recognized exception applies.
    - N: lens A: match=False present=True disp='certiorari granted; judgment reversed; remanded' oc=0.579 | lens B: match=False present=True disp='In forma pauperis and certiorari granted; judgment reversed and remanded.' oc=0.684
    - refs: P:cases/Flippo v. West Virginia.md, N-A:codex-A-read-p1-prod-d330e8c7::parsed::/Users/johngalt/cssi-lake/cache/text/1854815.txt, N-B:codex-B-read-p1-prod-d330e8c7::parsed::/Users/johngalt/cssi-lake/cache/text/1854815.txt


## Doctrine discordance candidates (coverage + split grain)

### Real-Time Tracking `P-d-0e214dcd8a56`  (P-homed 3 / N-derived 8)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['Post-Carpenter, is short-term real-time location tracking (real-time CSLI / phone pings) a Fourth Amendment search?', "Does prolonged fixed-point video surveillance of a home's exterior (pole cameras) become a search by aggregation (mosaic theory)?"]

### Private & Foreign Searches `P-d-176e2487d9cb`  (P-homed 6 / N-derived 8)
  - split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]

### Aerial & Enhanced Surveillance `P-d-2732f927a8cc`  (P-homed 5 / N-derived 9)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=["Is prolonged, warrantless pole-camera (or persistent aerial) surveillance of a home's exterior a Fourth Amendment search after Carpenter?"]

### The Good-Faith Exception `P-d-2d77b33c5c60`  (P-homed 17 / N-derived 16)
  - over-inclusion candidate: cases/Immigration & Naturalization Service v. Lopez-Mendoza.md (P-role: Key — Progeny / Refinement)
  - over-inclusion candidate: cases/United States v. Calandra.md (P-role: Key — Progeny / Refinement)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['For novel surveillance techniques (geofence warrants), how settled must authority be before Leon/Davis good faith saves the search -- does novelty itself support objectively reasonable reliance?']

### SIA — Cell Phones `P-d-59506c88a4b0`  (P-homed 1 / N-derived 7)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['Adjacent (border-search, intersecting phone privacy post-Riley): what suspicion is required for forensic searches of electronic devices at the border?']

### When a Seizure Occurs `P-d-72c3cb092c3f`  (P-homed 20 / N-derived 16)
  - UNKNOWN coverage-gap: **INS v. Delgado** (cluster 111148, N-role limiting, cand_unverified=False)

### Public-Employee Compelled Statements (Garrity) `P-d-7ef550636751`  (P-homed 6 / N-derived 8)
  - over-inclusion candidate: cases/Kalkines v. United States.md (P-role: Key — Progeny / Refinement)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=["When no statute or employer order expressly threatens discharge, does Garrity immunity attach on the employee's subjective belief that refusal means termination, and must that belief be objectively reasonable?"]

### Reverse-Keyword & Geofence Warrants `P-d-9b281351afcb`  (P-homed 2 / N-derived 8)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['Is government acquisition of geofence (bulk device-location) data a Fourth Amendment search?', 'Are geofence warrants categorically unconstitutional general warrants?']

### Arrest & Arrest Warrants `P-d-aa5b3e10c79c`  (P-homed 4 / N-derived 18)
  - split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]

### Community Caretaking `P-d-baad20928a25`  (P-homed 4 / N-derived 7)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['What standard governs a noninvestigative caretaking/welfare seizure of a person in public after Caniglia?']

### Cell-Site Simulators `P-d-c1df624b8e8c`  (P-homed 0 / N-derived 9)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['Is deploying a cell-site simulator to force a phone to reveal its location a Fourth Amendment search requiring a warrant?']

### Prompt Probable-Cause Determination `P-d-c4fefc8243df`  (P-homed 2 / N-derived 6)
  - split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]

### Entrapment `P-d-d2d0ff10db5d`  (P-homed 8 / N-derived 8)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=['Subjective (predisposition) versus objective (police-conduct) test for entrapment', 'Viability and scope of the freestanding outrageous-government-conduct due-process defense after Russell and Hampton']

### Inventory Searches `P-d-e5fc7db3f3c7`  (P-homed 9 / N-derived 11)
  - split diff [N-only-split]: P_signal=False N_split=True; N-questions=["Must the impoundment predicate itself be justified by a reasonable, non-pretextual community-caretaking rationale (and by standardized criteria) before an inventory can stand — and how far does an officer's investigatory motive taint an otherwise policy-compliant inventory?"]

## Over-inclusion advisory (WEAK; P homes, N lacks — expected N-blindness)

> Not counted as DISCORDANT-candidate. Only core-role misses (non foil/history/progeny-role, N could read the case) are listed; n-blind-unread and expected-role are omitted here.

- **Plain View & Plain Feel** `P-d-0bc586a754b8` (5): People v. Hughes [Key — Progeny / Refinement]; State v. Mansor [Recent development (role-based)]; State v. Volle [Recent development (role-based)]; United States v. Morton [Recent development (role-based)]; United States v. Tuggle [Recent development (role-based)]
- **Inevitable Discovery & Independent Source** `P-d-14a6b3ba356c` (1): State v. Mitcham [Recent development (role-based)]
- **Miranda: Waiver and Invocation** `P-d-1e5d553d49aa` (1): Salinas v. Texas [Key — Progeny]
- **Probable Cause** `P-d-2a5c8e3fa21f` (1): Hill v. California [Progeny]
- **Protective Sweeps & Securing the Scene** `P-d-2a5f587bde2a` (2): United States v. August [Recent development (role-based)]; United States v. Conner [Recent development (role-based)]
- **The Good-Faith Exception** `P-d-2d77b33c5c60` (2): Immigration & Naturalization Service v. Lopez-Mendoza [Key — Progeny / Refinement]; United States v. Calandra [Key — Progeny / Refinement]
- **Section 1983 & Municipal Liability** `P-d-33cdad292347` (3): Chavez v. Martinez [Key — Progeny]; United States v. Classic [Key — Anchor]; Vega v. Tekoh [Key — Progeny]
- **Sixth Amendment Right to Counsel** `P-d-6ce1eb316325` (1): Hoffa v. United States [Key — Progeny / Refinement]
- **Public-Employee Compelled Statements (Garrity)** `P-d-7ef550636751` (1): Kalkines v. United States [Key — Progeny / Refinement]
- **Special Needs & Administrative** `P-d-87eb1bc143aa` (1): Florence v. County of Burlington [Key — Progeny / Refinement]
- **Brady and Giglio** `P-d-b75a3bfea3dc` (1): Glossip v. Oklahoma [Key — Progeny / Refinement]
- **Fruits & Attenuation** `P-d-b7adf6aee9fe` (4): Elkins v. United States [Anchor (silver-platter abolition; deterrence rationale)]; Mapp v. Ohio [Key — Anchor]; Walder v. United States [Key — Anchor (impeachment exception)]; Weeks v. United States [Key — Anchor]
- **Qualified Immunity** `P-d-c2d3ababe456` (2): Hanlon v. Berger [Key — Progeny / Refinement]; Wright v. City of Euclid [Recent development (role-based)]
- **The Automobile Exception** `P-d-ca996dedf7f9` (1): United States v. Morley [Recent development (role-based)]
- **Due-Process Voluntariness of Confessions** `P-d-d826f6fae7ac` (6): Beecher v. Alabama [Key — Progeny / Refinement]; Corley v. United States [Key — Progeny / Refinement]; Frazier v. Cupp [Key — Progeny / Refinement]; Mallory v. United States [Key — Anchor]; Malloy v. Hogan [Key — Anchor]; McNabb v. United States [Key — Anchor]
- **Exigent Circumstances — Hot Pursuit** `P-d-db79db9b164f` (1): Newman v. Underhill [Recent development (role-based)]
- **Traffic Stops** `P-d-dfe4a5bfd76c` (3): Arkansas v. Sullivan [Progeny]; Michigan v. Long [Key — Progeny / Refinement]; United States v. Vinton [Key — Progeny / Refinement]
- **Exigent Circumstances — Emergency Aid** `P-d-ee7913e4e885` (2): Case v. Montana [Key — Progeny / Refinement]; Michigan v. Tyler [Key — Progeny / Refinement]
- **Terry Stops and Reasonable Suspicion** `P-d-f46fb52a2207` (2): Brown v. Texas [Anchor]; Hiibel v. Sixth Judicial Dist. Court [Key-on (during a valid Terry stop)]
- **Collective Knowledge and the Fellow-Officer Rule** `P-d-f73828a90790` (1): Herring v. United States [Key (non-exclusive; imputation limit)]
- **Knock and Talk** `P-d-f8cf1244658a` (2): Florida v. Bostick [Key — Progeny / Refinement]; United States v. Drayton [Key — Progeny / Refinement]

## Treatment-currency advisory (low-confidence; NOT auto-adjudicated)

> N reads are as-of-decision (manifest-blind to later treatment); self-negative string matches are dominated by false positives. Surfaced (never buried) for the R7 currency sweep / agent read, but not counted as DISCORDANT-candidate.

- **Kuhlmann v. Wilson** `P-c-093a99438fca` — P.validity=good_law; N excerpt: …As of this opinion, no named Supreme Court precedent is overruled. The Massiah/Henry/Moulton line remains good but is confined to deliberate elici…
- **Elkins v. United States** `P-c-206cea20d87b` — P.validity=good_law; N excerpt: …As of this decision, the silver platter doctrine is no longer good law in federal criminal trials. The controlling rule is exclusion over timely o…
- **Berghuis v. Thompkins** `P-c-358c5ce11e7c` — P.validity=good_law; N excerpt: …s remain operative; this opinion clarifies and extends them rather than overruling them. The controlling rule in this case is good law as of the decision date:…
- **California v. Acevedo** `P-c-613b4b1832e6` — P.validity=good_law; N excerpt: …s in automobiles is no longer good law in that context. Ross, Carroll, and Chambers remain good law as the governing automobile-exception framework, and Ross' l…
- **Donovan v. Dewey** `P-c-6b001d9f647b` — P.validity=good_law; N excerpt: …ict-court ruling is no longer good law after reversal.…
- **Glossip v. Oklahoma** `P-c-7319bb79e86a` — P.validity=good_law; N excerpt: …indication that it has been overruled, vacated, withdrawn, or limited; only publication-form revision signals appear.…
- **Berger v. New York** `P-c-8b8d3172e8fc` — P.validity=good_law; N excerpt: …overed reasoning is no longer good law in the form described by this opinion.…
- **United States v. Cotterman** `P-c-97f88ad215dc` — P.validity=good_law; N excerpt: …ion itself shows no later overruling, while separate opinions flag asserted tension with Supreme Court precedent and an asserted circuit split.…
- **O'Connor v. Ortega** `P-c-9bfa1422d991` — P.validity=good_law; N excerpt: …nal signal suggests this opinion was overruled; several adjacent issues were expressly left undecided.…
- **Monell v. Department of Social Services** `P-c-a2d977ccb1f5` — P.validity=good_law; N excerpt: …6, 1978, Monroe is no longer good law on absolute local-government immunity under § 1983. Monell is the operative rule: local governments are § 1983 persons fo…
- **Montejo v. Louisiana** `P-c-a5d7121ada61` — P.validity=good_law; N excerpt: …higan v. Jackson is no longer good law. Miranda, Edwards, Minnick, and Patterson remain operative; Montejo may still seek suppression on remand under Edwards or…
- **Delaware v. Prouse** `P-c-adec6c16c2bc` — P.validity=good_law; N excerpt: …nion indicates that this holding was overruled or limited as of the decision date.…
- **United States v. Matlock** `P-c-bde0e9322636` — P.validity=good_law; N excerpt: ….txt indicates that this decision had been overruled, limited, or superseded as of that time.…
- **Florida v. Meyers** `P-c-c1b8cd321c91` — P.validity=good_law; N excerpt: …ded or immobilized. This opinion reinforces, rather than limits or overrules, that rule.…
- **Doyle v. Ohio** `P-c-cac656c6a7f7` — P.validity=good_law; N excerpt: …in footnote 11. No later overruling or negative treatment appears within the opinion text.…
- **Hill v. California** `P-c-d082360c60c1` — P.validity=good_law; N excerpt: …ty opinion controls this case: the California Supreme Court judgment is affirmed, no named prior case is overruled, Chimel remains good law but is not applied r…
- **United States v. Morley** `P-c-d265e227c567` — P.validity=good_law; N excerpt: …ains no signal that this opinion itself had been overruled, limited, or superseded as of its decision date.…
- **Skinner v. Railway Labor Executives' Ass'n** `P-c-d4fceda6e184` — P.validity=good_law; N excerpt: …allenge. Burnley is no longer good law to the extent it required individualized suspicion for these regulations; the cited Supreme Court precedents remain good…
- **Thompson v. Louisiana** `P-c-d9189cb65e3e` — P.validity=good_law; N excerpt: …law and controlled this case; no prior Supreme Court precedent is overruled, limited, or undermined. The Louisiana Supreme Court's contrary murder-scene-search…
- **United States v. Conner** `P-c-e7a4141a490f` — P.validity=good_law; N excerpt: …e is no signal that this opinion or the rules it applies were overruled, limited, or questioned as of that time.…
- **Harlow v. Fitzgerald** `P-c-eba400a421b0` — P.validity=good_law; N excerpt: …nternal signal that this holding was overruled or negatively treated as of the decision.…
- **Pembaur v. City of Cincinnati** `P-c-ec99cf0b48b7` — P.validity=good_law; N excerpt: …ains no signal that this opinion was overruled or limited as of issuance, but it flags Part II-B as outside the opinion of the Court and decides the Fourth Amen…
- **City of Canton v. Harris** `P-c-f4e84da82f04` — P.validity=good_law; N excerpt: …sness standards are no longer good law to that extent.…
- **Chandler v. Miller** `P-c-f63d0219eaf7` — P.validity=good_law; N excerpt: …ains no signal that this opinion itself is overruled or limited.…
