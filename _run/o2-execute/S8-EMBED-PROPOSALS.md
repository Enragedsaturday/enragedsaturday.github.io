# S8 EMBED PROPOSALS — R9 transclusion conversions (ADJUDICATION INPUT)

**Lane:** o2-opus-xhigh (`claude-opus-4-8`) · S8 embeds · **read-only vs content** · COMMIT NOTHING · zero CL.
**Detector:** `scripts/s8/shingles.py` (self-test PASS) · **Machine report:** `_run/o2-execute/s8-shingle-report.jsonl` · **threshold:** >=25 contiguous tokens.
**Embed grammar (authoritative exhibit `51e1f4b`, `content/.../Curtilage.md`):** rule shell `> [!rule] Black-letter rule — stated on [[Home]]` + `> ![[<full-slug>#^rule-tail]]`; pin `![[cases/<Case>#^pin-N]]`. **Full-slug targets only** (R9 alias-stub trap).

> **STOP line.** This file is the orchestrator's adjudication input. Every hit below is a *mechanical* >=25-token overlap; whether it converts is a judgment surface (an embed changes rendered content). The detector does not decide — it flags. No content was written.

## Zone / matching policy (documented decision)

- Block segmentation = `zones.iter_blocks` (frozen). **Prose blocks** = para / listitem / blockquote that are neither a rule-callout nor a pin block and not inside a `## Sources` section.
- Offset-preserving normalization blanks **embeds `![[…]]`** (embed-excluded by construction — an already-embedded block yields no tokens), keeps only rendered wikilink/markdown-link display text, and blanks callout titles + bare block anchors.
- Masked R2 zones: `sources, comment, frontmatter, code`. **`quote` and `citation` zones are NOT masked** — flavor (b) is defined by re-typed direct quotations (which live inside `"…"`) and shared rule prose runs through inline citations; masking them would make the pinned-quote flavor undetectable. (Every other S8 pass still honors those zones; this detector is the one place quoted text must participate.)
- **Same-page overlap is never a hit** (a page may restate its own rule); only FOREIGN source blocks match.

## Summary

| metric | value |
|---|---|
| files scanned | 724 |
| rule sources (`^rule-*` callouts) | 73 |
| pin sources (`^pin-N`, cases only) | 1070 |
| prose blocks swept | 4372 |
| **total hits** | **128** |
| — rule restatements (flavor a) | 3 |
| — pinned-quote overlaps (flavor b) | 125 |
| read errors (torn/concurrent) | 0 |
| distinct targets / unresolved full-slugs / missing anchors | 124 / 0 / 0 |

Pin-hit shape: **1** re-typed block-quote · **8** list items · **116** inline-woven paragraphs (the last group is where the spec's *"short inline quote snippets woven into a sentence stay ordinary quoted text + R4 links"* carve-out lives — those crossing >=25 tokens are flagged for per-hit adjudication, not auto-conversion).

---

## Tier A — rule-node restatements (flavor a, rule shell embed)

3 hits. Each is a page's prose restating another page's canonical black-letter rule >=25 tokens. Proposed conversion = the `[!rule]` shell embedding the foreign `^rule-*` block.

### A1. `content/seizures/arrests/Arrest in the Home.md:26` → `warrant-exceptions/home-entry-and-search/Entry to Arrest#^rule-entry-to-arrest`  (32t, 28% of block; resolves ✓)

Offending block:
```text
**The suspect's own home: an arrest warrant plus reason to believe he is within.** For the suspect's **own** dwelling *[[Payton v. New York|Payton]]* supplies the operative rule: "[a]n arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within." 445 U.S. at 603. Two predicates ride on that one sentence: the suspect **lives** there and there is **reason to believe** he is **present now**. So the field answer for the suspect's own home is an **arrest warrant plus reason to believe the suspect is within** (or consent, or a true exigency).
```
Overlapping run:
> arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within

Proposed embed:
```markdown
> [!rule] Black-letter rule — stated on [[Entry to Arrest]]
> ![[warrant-exceptions/home-entry-and-search/Entry to Arrest#^rule-entry-to-arrest]]
```
Prose that remains: the block's framing/analysis sentences stay in the page's own voice; the restated black-letter sentence is replaced by the shell. If the whole paragraph is the restatement, the shell replaces it wholesale.

### A2. `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:52` → `warrant-exceptions/home-entry-and-search/Emergency Aid#^rule-emergency-aid`  (26t, 23% of block; resolves ✓)

Offending block:
```text
**The other exigencies, in brief.** The **evidence-destruction** branch (the dissipating-alcohol line and the no-police-created-exigency rule) is developed on [[Destruction of Evidence]]. The **life-safety / emergency-aid** branch is governed by an objective standard: police "may enter a home without a warrant when they have an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened," and "[t]he officer's subjective motivation is irrelevant." *[[Brigham City v. Stuart#^pin-400|Brigham City v. Stuart]]*, 547 U.S. 398, 400, 404 (2006). Develop these on [[Emergency Aid]]; note there is **no** freestanding "community caretaking" power to cross a ...
```
Overlapping run:
> police may enter a home without a warrant when they have an objectively reasonable basis for believing that an occupant is seriously injured or imminently threatened

Proposed embed:
```markdown
> [!rule] Black-letter rule — stated on [[Emergency Aid]]
> ![[warrant-exceptions/home-entry-and-search/Emergency Aid#^rule-emergency-aid]]
```
Prose that remains: the block's framing/analysis sentences stay in the page's own voice; the restated black-letter sentence is replaced by the shell. If the whole paragraph is the restatement, the shell replaces it wholesale.

### A3. `content/warrant-exceptions/home-entry-and-search/Securing the Scene.md:40` → `the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene#^rule-detention-scene`  (31t, 22% of block; resolves ✓)

Offending block:
```text
**Detaining the people present is a separate power, developed elsewhere.** Securing a scene usually means holding the people in it, and a premises search warrant "founded on probable cause implicitly carries with it the limited authority to detain the occupants of the premises while a proper search is conducted." *[[Michigan v. Summers|Michigan v. Summers]]*, 452 U.S. 692 (1981). That detention authority is categorical, enforceable with reasonable force, but spatially confined to the immediate vicinity, and it is **not** authority to search the people present. The full treatment (*[[Michigan v. Summers|Summers]]* / *[[Muehler v. Mena|Muehler]]* / *[[Bailey v. United States|Bailey]]* / *[[Los ...
```
Overlapping run:
> founded on probable cause implicitly carries with it the limited authority to detain the occupants of the premises while a proper search is conducted Michigan v Summers 452 U S 692

Proposed embed:
```markdown
> [!rule] Black-letter rule — stated on [[Detention and Search of Persons at the Scene]]
> ![[the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene#^rule-detention-scene]]
```
Prose that remains: the block's framing/analysis sentences stay in the page's own voice; the restated black-letter sentence is replaced by the shell. If the whole paragraph is the restatement, the shell replaces it wholesale.

---

## Tier B — re-typed pinned block-quote (flavor b, cleanest)

1 hit(s). Offending block is a true markdown block-quote that re-types a passage a case page pins — the exact Curtilage `![[cases/…#^pin-N]]` exhibit pattern.

### B1. `content/warrant-exceptions/searching-a-vehicle/Automobile Exception.md:34` → `cases/California v. Carney#^pin-393`  (47t, 87% of block; resolves ✓)

Offending block:
```text
> "First, the vehicle is obviously readily mobile by the turn of an ignition key, if not actually moving. Second, there is a reduced expectation of privacy stemming from its use as a licensed motor vehicle subject to a range of police regulation inapplicable to a fixed dwelling." — *[[California v. Carney|Carney]]*, 471 U.S. 386, 393 (1985).
```
Proposed embed (replaces the block-quote wholesale):
```markdown
![[cases/California v. Carney#^pin-393]]
```
Prose that remains: none inside the quote; the lead-in sentence above the block-quote stays.

---

## Tier C — pinned quote inside a list item

8 hits. A list item carries a >=25-token verbatim pin passage. Adjudicate whether the list structure survives an embed (block embeds break list flow) or the item stays quoted text + R4 link.

| # | offending `file:line` | overlap | target | resolves | run |
|---|---|---|---|:--:|---|
| C1 | `content/confessions-interrogation-and-the-fifth-amendment/Miranda and Custodial Interrogation.md:70` | 56t (34%) | `![[cases/United States v. Liddell#^pin-1009]]` | ✓ | the risk of police officers being injured by the mishandling of unknown firearms or drug p ... |
| C2 | `content/instructor-craft-and-study/Three Golden Rules.md:44` | 38t (18%) | `![[cases/Maryland v. Buie#^pin-335]]` | ✓ | articulable facts which taken together with the rational inferences from those facts would ... |
| C3 | `content/searches/Curtilage.md:77` | 33t (35%) | `![[cases/United States v. Lundin#^pin-1159]]` | ✓ | officers knocked on Lundin s door around 4 00 a m without evidence that Lundin generally a ... |
| C4 | `content/seizures/Terry Stops and Reasonable Suspicion.md:71` | 26t (20%) | `![[cases/United States v. Robinson (4th Cir. en banc)#^pin-696]]` | ✓ | officer who makes a lawful traffic stop and who has a reasonable suspicion that one of the ... |
| C5 | `content/seizures/arrests/Arrest in the Home.md:59` | 27t (32%) | `![[cases/United States v. Vasquez-Algarin#^pin-477]]` | ✓ | the Fifth Sixth Seventh and Ninth Circuits in holding that Payton s reason to believe lang ... |
| C6 | `content/use-of-force-and-liability/Qualified Immunity.md:66` | 29t (38%) | `![[cases/Wright v. City of Euclid#^pin-op17]]` | ✓ | that drawing a weapon on a suspect who was not fleeing or posing a safety risk and taserin ... |
| C7 | `content/warrant-exceptions/home-entry-and-search/Securing the Scene.md:67` | 33t (31%) | `![[cases/United States v. Conner#^pin-666]]` | ✓ | an unconstitutional search occurs when officers gain visual or physical access to a motel ... |
| C8 | `content/warrant-exceptions/searching-a-vehicle/Checkpoints and Roadblocks.md:28` | 29t (64%) | `![[cases/Brown v. Texas#^pin-51]]` | ✓ | the gravity of the public concerns served by the seizure the degree to which the seizure a ... |

---

## Tier D — inline-woven pinned quotes (paragraphs)

116 hits, sorted by block-coverage (overlap ÷ block tokens) descending. **High coverage = the paragraph is mostly the quote (strong embed candidate); low coverage = a long quote woven into original analysis (spec carve-out likely: keep as quoted text + R4 name→`#^pin` / pincite→fragment links).** Every target is a full-slug that resolves with a live anchor.

Proposed conversion for a Tier-D *embed* decision: replace the quoted span with `![[<target>#^<anchor>]]`, keeping the paragraph's framing sentences around it. Proposed *non-embed* decision (R4): leave the quote inline, wire the case-name to `#^<anchor>` and the pincite to its external fragment.

| # | offending `file:line` | cover | overlap | target | resolves | run |
|---|---|:--:|---|---|:--:|---|
| D1 | `content/cases/Beckwith v. United States.md:57` | 66% | 27t | `![[cases/Miranda v. Arizona#^pin-444a]]` | ✓ | questioning initiated by law enforcement officers after a person has been taken into custody or ... |
| D2 | `content/fair-trial-and-reliability-doctrines/Brady and Giglio.md:36` | 58% | 39t | `![[cases/Banks v. Dretke#^pin-691]]` | ✓ | components The evidence at issue must be favorable to the accused either because it is exculpat ... |
| D3 | `content/fair-trial-and-reliability-doctrines/Brady and Giglio.md:36` | 57% | 38t | `![[cases/Strickler v. Greene#^pin-281]]` | ✓ | The evidence at issue must be favorable to the accused either because it is exculpatory or beca ... |
| D4 | `content/seizures/arrests/Prompt Probable-Cause Determination.md:31` | 56% | 65t | `![[cases/Gerstein v. Pugh#^pin-113]]` | ✓ | the arrest and a brief booking detention but not prolonged custody a policeman s on the scene a ... |
| D5 | `content/confessions-interrogation-and-the-fifth-amendment/Miranda and Custodial Interrogation.md:38` | 53% | 32t | `![[cases/Rhode Island v. Innis#^pin-301]]` | ✓ | any words or actions on the part of the police other than those normally attendant to arrest an ... |
| D6 | `content/warrant-exceptions/searching-a-person/SIA Persons.md:33` | 53% | 54t | `![[cases/United States v. Robinson#^pin-235]]` | ✓ | It is the fact of the lawful arrest which establishes the authority to search and we hold that ... |
| D7 | `content/warrant-exceptions/searching-a-vehicle/Automobile Exception.md:30` | 47% | 33t | `![[cases/Carroll v. United States#^pin-p37]]` | ✓ | where it is not practicable to secure a warrant because the vehicle can be quickly moved out of ... |
| D8 | `content/fair-trial-and-reliability-doctrines/Entrapment.md:36` | 47% | 32t | `![[cases/Mathews v. United States#^pin-62]]` | ✓ | even if the defendant denies one or more elements of the crime he is entitled to an entrapment ... |
| D9 | `content/cases/Florida v. Powell.md:55` | 46% | 31t | `![[cases/Duckworth v. Eagan#^pin-203]]` | ✓ | as if construing a will or defining the terms of an easement The inquiry is simply whether the ... |
| D10 | `content/seizures/arrests/Prompt Probable-Cause Determination.md:37` | 44% | 37t | `![[cases/County of Riverside v. McLaughlin#^pin-57]]` | ✓ | Where an arrested individual does not receive a probable cause determination within 48 hours th ... |
| D11 | `content/cases/New York v. Belton.md:87` | 43% | 33t | `![[cases/Arizona v. Gant#^pin-351]]` | ✓ | only if the arrestee is within reaching distance of the passenger compartment at the time of th ... |
| D12 | `content/the-warrant/getting-a-warrant/Probable Cause in the Affidavit.md:30` | 43% | 58t | `![[cases/Illinois v. Gates#^pin-238a]]` | ✓ | The task of the issuing magistrate is simply to make a practical common sense decision whether ... |
| D13 | `content/the-warrant/getting-a-warrant/Particularity.md:33` | 42% | 25t | `![[cases/Steele v. United States#^pin-503]]` | ✓ | It is enough if the description is such that the officer with a search warrant can with reasona ... |
| D14 | `content/warrant-exceptions/searching-a-vehicle/SIA Vehicles.md:27` | 42% | 45t | `![[cases/Arizona v. Gant#^pin-351]]` | ✓ | Police may search a vehicle incident to a recent occupant s arrest only if the arrestee is with ... |
| D15 | `content/warrant-exceptions/searching-a-person/SIA Persons.md:35` | 40% | 34t | `![[cases/Chimel v. California#^pin-763]]` | ✓ | a search of the arrestee s person and the area within his immediate control construing that phr ... |
| D16 | `content/the-warrant/executing-a-warrant/Scope Manner and Related Issues.md:38` | 40% | 50t | `![[cases/Zurcher v. Stanford Daily#^pin-556]]` | ✓ | evidence is there The critical element in a reasonable search is not that the owner of the prop ... |
| D17 | `content/searches/Plain View Doctrine.md:40` | 40% | 34t | `![[cases/Horton v. California#^pin-137]]` | ✓ | only must the officer be lawfully located in a place from which the object can be plainly seen ... |
| D18 | `content/warrant-exceptions/Consent Searches.md:38` | 39% | 62t | `![[cases/United States v. Matlock#^pin-171a]]` | ✓ | on mutual use of the property by persons generally having joint access or control for most purp ... |
| D19 | `content/the-warrant/executing-a-warrant/Knock-and-Announce.md:34` | 38% | 41t | `![[cases/Richards v. Wisconsin#^pin-394a]]` | ✓ | the police must have a reasonable suspicion that knocking and announcing their presence under t ... |
| D20 | `content/seizures/arrests/Prompt Probable-Cause Determination.md:35` | 36% | 31t | `![[cases/County of Riverside v. McLaughlin#^pin-56]]` | ✓ | a jurisdiction that provides judicial determinations of probable cause within 48 hours of arres ... |
| D21 | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:52` | 36% | 35t | `![[cases/United States v. Garner#^pin-1213c]]` | ✓ | the officer has completed the inquiry necessary to satisfy the purpose of the initial detention ... |
| D22 | `content/seizures/arrests/Prompt Probable-Cause Determination.md:33` | 36% | 37t | `![[cases/Gerstein v. Pugh#^pin-125]]` | ✓ | it must provide a fair and reliable determination of probable cause as a condition for any sign ... |
| D23 | `content/searches/Abandonment.md:31` | 35% | 29t | `![[cases/Hester v. United States#^pin-58]]` | ✓ | any Fourth Amendment interest in them there was no seizure in the sense of the law when the off ... |
| D24 | `content/use-of-force-and-liability/Use of Force.md:37` | 34% | 40t | `![[cases/Scott v. Harris#^pin-1779]]` | ✓ | A police officer s attempt to terminate a dangerous high speed car chase that threatens the liv ... |
| D25 | `content/warrant-exceptions/Consent Searches.md:42` | 34% | 33t | `![[cases/Illinois v. Rodriguez#^pin-188]]` | ✓ | judged against an objective standard would the facts available to the officer at the moment war ... |
| D26 | `content/warrant-exceptions/searching-a-vehicle/Inventory Searches.md:32` | 33% | 34t | `![[cases/Illinois v. Lafayette#^pin-648]]` | ✓ | not unreasonable for police as part of the routine procedure incident to incarcerating an arres ... |
| D27 | `content/warrant-exceptions/home-entry-and-search/Entry to Arrest.md:45` | 33% | 38t | `![[cases/New York v. Harris#^pin-21]]` | ✓ | the exclusionary rule does not bar the State s use of a statement made by the defendant outside ... |
| D28 | `content/warrant-exceptions/Consent Searches.md:48` | 33% | 37t | `![[cases/Florida v. Jimeno#^pin-251]]` | ✓ | The standard for measuring the scope of a suspect s consent under the Fourth Amendment is that ... |
| D29 | `content/searches/Plain View Doctrine.md:80` | 32% | 25t | `![[cases/Minnesota v. Dickerson#^pin-375]]` | ✓ | If a police officer lawfully pats down a suspect s outer clothing and feels an object whose con ... |
| D30 | `content/seizures/arrests/Arrest in the Home.md:36` | 32% | 38t | `![[cases/New York v. Harris#^pin-21]]` | ✓ | the exclusionary rule does not bar the State s use of a statement made by the defendant outside ... |
| D31 | `content/fair-trial-and-reliability-doctrines/Brady and Giglio.md:34` | 31% | 37t | `![[cases/Brady v. Maryland#^pin-87]]` | ✓ | suppression by the prosecution of evidence favorable to an accused upon request violates due pr ... |
| D32 | `content/use-of-force-and-liability/Use of Force.md:33` | 31% | 38t | `![[cases/Graham v. Connor#^pin-396a]]` | ✓ | case including the severity of the crime at issue whether the suspect poses an immediate threat ... |
| D33 | `content/searches/Aerial and Enhanced Surveillance.md:40` | 30% | 46t | `![[cases/Kyllo v. United States#^pin-34]]` | ✓ | obtaining by sense enhancing technology any information regarding the interior of the home that ... |
| D34 | `content/the-warrant/executing-a-warrant/Scope Manner and Related Issues.md:44` | 30% | 35t | `![[cases/Winston v. Lee#^pin-759]]` | ✓ | A compelled surgical intrusion into an individual s body for evidence implicates expectations o ... |
| D35 | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:38` | 30% | 48t | `![[cases/Cady v. Dombrowski#^pin-441]]` | ✓ | frequently investigate vehicle accidents in which there is no claim of criminal liability and e ... |
| D36 | `content/seizures/arrests/Arrest and Arrest Warrants.md:34` | 30% | 32t | `![[cases/Atwater v. City of Lago Vista#^pin-354]]` | ✓ | If an officer has probable cause to believe that an individual has committed even a very minor ... |
| D37 | `content/seizures/Seizure of the Person.md:37` | 30% | 44t | `![[cases/United States v. Mendenhall#^pin-554a]]` | ✓ | the threatening presence of several officers the display of a weapon by an officer some physica ... |
| D38 | `content/the-warrant/getting-a-warrant/Particularity.md:37` | 30% | 37t | `![[cases/Groh v. Ramirez#^pin-557]]` | ✓ | The fact that the application adequately described the things to be seized does not save the wa ... |
| D39 | `content/use-of-force-and-liability/Qualified Immunity.md:31` | 29% | 28t | `![[cases/Harlow v. Fitzgerald#^pin-818]]` | ✓ | are shielded from liability for civil damages insofar as their conduct does not violate clearly ... |
| D40 | `content/the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene.md:34` | 29% | 35t | `![[cases/Muehler v. Mena#^pin-98]]` | ✓ | An officer s authority to detain incident to a search is categorical it does not depend on the ... |
| D41 | `content/searches/Plain View Doctrine.md:38` | 29% | 32t | `![[cases/Harris v. United States (1968)#^pin-236a]]` | ✓ | objects falling in the plain view of an officer who has a right to be in the position to have t ... |
| D42 | `content/searches/Abandonment.md:27` | 28% | 33t | `![[cases/California v. Greenwood#^pin-40b]]` | ✓ | It is common knowledge that plastic garbage bags left on or at the side of a public street are ... |
| D43 | `content/warrant-exceptions/programmatic-and-special-needs-searches/Border Searches.md:31` | 28% | 30t | `![[cases/United States v. Flores-Montano#^pin-152a]]` | ✓ | balancing tests to determine what is a routine search of a vehicle as opposed to a more intrusi ... |
| D44 | `content/the-warrant/getting-a-warrant/Probable Cause in the Affidavit.md:38` | 28% | 41t | `![[cases/United States v. Grubbs#^pin-96]]` | ✓ | no different in principle from ordinary warrants They require the magistrate to determine 1 tha ... |
| D45 | `content/fair-trial-and-reliability-doctrines/Entrapment.md:34` | 28% | 27t | `![[cases/United States v. Russell#^pin-436]]` | ✓ | It is only when the Government s deception actually implants the criminal design in the mind of ... |
| D46 | `content/the-right-to-counsel/Lineups and the Right to Counsel.md:34` | 27% | 38t | `![[cases/Gilbert v. California#^pin-273]]` | ✓ | Only a per se exclusionary rule as to such testimony can be an effective sanction to assure tha ... |
| D47 | `content/warrant-exceptions/Consent Searches.md:46` | 27% | 40t | `![[cases/Georgia v. Randolph#^pin-120]]` | ✓ | a warrantless search of a shared dwelling for evidence over the express refusal of consent by a ... |
| D48 | `content/seizures/Seizure of the Person.md:43` | 27% | 29t | `![[cases/Brower v. County of Inyo#^pin-599]]` | ✓ | enough for a seizure that a person be stopped by the very instrumentality set in motion or put ... |
| D49 | `content/use-of-force-and-liability/Use of Force.md:37` | 27% | 31t | `![[cases/Plumhoff v. Rickard#^pin-777b]]` | ✓ | if police officers are justified in firing at a suspect in order to end a severe threat to publ ... |
| D50 | `content/the-right-to-counsel/Sixth Amendment Right to Counsel.md:34` | 26% | 43t | `![[cases/Massiah v. United States#^pin-206]]` | ✓ | was denied the basic protections of that guarantee when there was used against him at his trial ... |
| D51 | `content/seizures/Collective Knowledge and the Fellow-Officer Rule.md:39` | 26% | 31t | `![[cases/Herring v. United States#^pin-144]]` | ✓ | trigger the exclusionary rule police conduct must be sufficiently deliberate that exclusion can ... |
| D52 | `content/warrant-exceptions/home-entry-and-search/Entry to Arrest.md:43` | 26% | 37t | `![[cases/United States v. Nora#^pin-1055]]` | ✓ | the officers had no reason to believe Nora might pose a danger to the public by attempting to f ... |
| D53 | `content/searches/two-definitions-of-search/Reasonable Expectation of Privacy.md:35` | 26% | 30t | `![[cases/Katz v. United States#^pin-361]]` | ✓ | a twofold requirement first that a person have exhibited an actual subjective expectation of pr ... |
| D54 | `content/fair-trial-and-reliability-doctrines/Entrapment.md:32` | 25% | 33t | `![[cases/Jacobson v. United States#^pin-548]]` | ✓ | may not originate a criminal design implant in an innocent person s mind the disposition to com ... |
| D55 | `content/use-of-force-and-liability/Use of Force.md:35` | 25% | 38t | `![[cases/Tennessee v. Garner#^pin-3]]` | ✓ | may not be used unless it is necessary to prevent the escape and the officer has probable cause ... |
| D56 | `content/warrant-exceptions/home-entry-and-search/Securing the Scene.md:36` | 24% | 42t | `![[cases/Maryland v. Buie#^pin-335]]` | ✓ | there must be articulable facts which taken together with the rational inferences from those fa ... |
| D57 | `content/the-warrant/getting-a-warrant/The Neutral and Detached Magistrate.md:30` | 24% | 32t | `![[cases/Johnson v. United States#^pin-13]]` | ✓ | protection consists in requiring that those inferences be drawn by a neutral and detached magis ... |
| D58 | `content/the-right-to-counsel/Lineups and the Right to Counsel.md:32` | 24% | 28t | `![[cases/United States v. Wade#^pin-237]]` | ✓ | the post indictment lineup was a critical stage of the prosecution at which he was as much enti ... |
| D59 | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:42` | 24% | 56t | `![[cases/Kalkines v. United States#^pin-1393]]` | ✓ | warning a governmental employer is not wholly barred from insisting that relevant information b ... |
| D60 | `content/searches/Private and Foreign Searches.md:39` | 24% | 25t | `![[cases/Walter v. United States#^pin-654]]` | ✓ | was a significant expansion of the search that had been conducted previously by a private party ... |
| D61 | `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:52` | 23% | 26t | `![[cases/Brigham City v. Stuart#^pin-400]]` | ✓ | police may enter a home without a warrant when they have an objectively reasonable basis for be ... |
| D62 | `content/warrant-exceptions/home-entry-and-search/Fire-Scene Entries.md:31` | 23% | 25t | `![[cases/Michigan v. Tyler#^pin-510]]` | ✓ | officials need no warrant to remain in a building for a reasonable time to investigate the caus ... |
| D63 | `content/searches/Aerial and Enhanced Surveillance.md:34` | 23% | 41t | `![[cases/California v. Ciraolo#^pin-215]]` | ✓ | an age where private and commercial flight in the public airways is routine it is unreasonable ... |
| D64 | `content/the-warrant/executing-a-warrant/Scope Manner and Related Issues.md:42` | 23% | 25t | `![[cases/Coolidge v. New Hampshire#^pin-466a]]` | ✓ | the plain view doctrine may not be used to extend a general exploratory search from one object ... |
| D65 | `content/the-warrant/executing-a-warrant/Knock-and-Announce.md:34` | 23% | 25t | `![[cases/Richards v. Wisconsin#^pin-394]]` | ✓ | cannot remove from the neutral scrutiny of a reviewing court the reasonableness of the police d ... |
| D66 | `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:33` | 22% | 32t | `![[cases/Herring v. United States#^pin-144]]` | ✓ | To trigger the exclusionary rule police conduct must be sufficiently deliberate that exclusion ... |
| D67 | `content/searches/Private and Foreign Searches.md:43` | 22% | 28t | `![[cases/United States v. Verdugo-Urquidez#^pin-265]]` | ✓ | a class of persons who are part of a national community or who have otherwise developed suffici ... |
| D68 | `content/fair-trial-and-reliability-doctrines/Brady and Giglio.md:42` | 22% | 41t | `![[cases/United States v. Bagley#^pin-682]]` | ✓ | Evidence is material only if there is a reasonable probability that had the evidence been discl ... |
| D69 | `content/the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene.md:38` | 22% | 27t | `![[cases/Bailey v. United States#^pin-201]]` | ✓ | A spatial constraint defined by the immediate vicinity of the premises to be searched is theref ... |
| D70 | `content/searches/Private and Foreign Searches.md:35` | 22% | 25t | `![[cases/United States v. Jacobsen#^pin-113a]]` | ✓ | is wholly inapplicable to a search or seizure even an unreasonable one effected by a private in ... |
| D71 | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:32` | 22% | 47t | `![[cases/Garrity v. New Jersey#^pin-500]]` | ✓ | the protection of the individual under the Fourteenth Amendment against coerced statements proh ... |
| D72 | `content/the-warrant/getting-a-warrant/Probable Cause in the Affidavit.md:34` | 22% | 25t | `![[cases/United States v. Harris (1971)#^pin-583]]` | ✓ | of crime like admissions against proprietary interests carry their own indicia of credibility s ... |
| D73 | `content/fair-trial-and-reliability-doctrines/Entrapment.md:30` | 21% | 34t | `![[cases/Sorrells v. United States#^pin-454]]` | ✓ | the conception and planning of an offense by an officer and his procurement of its commission b ... |
| D74 | `content/searches/Plain View Doctrine.md:44` | 21% | 26t | `![[cases/Arizona v. Hicks#^pin-326]]` | ✓ | We now hold that probable cause is required To say otherwise would be to cut the plain view doc ... |
| D75 | `content/the-warrant/getting-a-warrant/Probable Cause in the Affidavit.md:36` | 21% | 26t | `![[cases/United States v. Ventresca#^pin-109b]]` | ✓ | and the resolution of doubtful or marginal cases in this area should be largely determined by t ... |
| D76 | `content/the-warrant/getting-a-warrant/Franks Challenges.md:41` | 20% | 27t | `![[cases/United States v. Leon#^pin-923]]` | ✓ | was misled by information in an affidavit that the affiant knew was false or would have known w ... |
| D77 | `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:38` | 20% | 36t | `![[cases/Newman v. Underhill#^pin-op10]]` | ✓ | a suspect may not defeat an arrest which has been set in motion in a public place by the expedi ... |
| D78 | `content/the-warrant/executing-a-warrant/Detention and Search of Persons at the Scene.md:40` | 19% | 25t | `![[cases/Ybarra v. Illinois#^pin-91]]` | ✓ | a person s mere propinquity to others independently suspected of criminal activity does not wit ... |
| D79 | `content/searches/Tents.md:29` | 19% | 28t | `![[cases/United States v. Sandoval#^pin-661]]` | ✓ | a camper who overstayed his permit in a public campground would lose his Fourth Amendment right ... |
| D80 | `content/warrant-exceptions/home-entry-and-search/Emergency Aid.md:39` | 19% | 26t | `![[cases/Ryburn v. Huff#^pin-476]]` | ✓ | Fourth Amendment permits an officer to enter a residence if the officer has a reasonable basis ... |
| D81 | `content/confessions-interrogation-and-the-fifth-amendment/Miranda Waiver and Invocation.md:31` | 19% | 31t | `![[cases/Berghuis v. Thompkins#^pin-388]]` | ✓ | a suspect who has received and understood the Miranda warnings and has not invoked his Miranda ... |
| D82 | `content/fair-trial-and-reliability-doctrines/Entrapment.md:32` | 19% | 25t | `![[cases/Jacobson v. United States#^pin-548a]]` | ✓ | the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit th ... |
| D83 | `content/warrant-exceptions/Consent Searches.md:44` | 18% | 27t | `![[cases/Stoner v. California#^pin-488]]` | ✓ | the rights protected by the Fourth Amendment are not to be eroded by strained applications of t ... |
| D84 | `content/warrant-exceptions/Consent Searches.md:46` | 18% | 27t | `![[cases/Fernandez v. California#^pin-303]]` | ✓ | an occupant who is absent due to a lawful detention or arrest stands in the same shoes as an oc ... |
| D85 | `content/searches/Open Fields.md:33` | 18% | 25t | `![[cases/Hester v. United States#^pin-59]]` | ✓ | the special protection accorded by the Fourth Amendment to the people in their persons houses p ... |
| D86 | `content/confessions-interrogation-and-the-fifth-amendment/Due-Process Voluntariness of Confessions.md:38` | 18% | 32t | `![[cases/Colorado v. Connelly#^pin-167]]` | ✓ | that coercive police activity is a necessary predicate to the finding that a confession is not ... |
| D87 | `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:33` | 18% | 26t | `![[cases/United States v. Calandra#^pin-348]]` | ✓ | is a judicially created remedy designed to safeguard Fourth Amendment rights generally through ... |
| D88 | `content/warrant-exceptions/home-entry-and-search/Securing the Scene.md:36` | 18% | 31t | `![[cases/Maryland v. Buie#^pin-334]]` | ✓ | as a precautionary matter and without probable cause or reasonable suspicion look in closets an ... |
| D89 | `content/warrant-exceptions/Consent Searches.md:50` | 18% | 39t | `![[cases/United States v. Osage#^pin-522]]` | ✓ | before an officer may actually destroy or render completely useless a container which would oth ... |
| D90 | `content/the-right-to-counsel/Sixth Amendment Right to Counsel.md:30` | 18% | 34t | `![[cases/Kirby v. Illinois#^pin-689]]` | ✓ | the Court s right to counsel decisions have involved points of time at or after the initiation ... |
| D91 | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:54` | 17% | 25t | `![[cases/United States v. Rideau#^pin-1574]]` | ✓ | function Police have long served the public welfare by removing intoxicated people from the pub ... |
| D92 | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:44` | 17% | 27t | `![[cases/LaChance v. Erickson#^pin-268]]` | ✓ | a Government agency may take adverse action against an employee because the employee made false ... |
| D93 | `content/warrant-exceptions/home-entry-and-search/Emergency Aid.md:41` | 17% | 32t | `![[cases/Case v. Montana#^pin-slip9]]` | ✓ | The entry is also scope limited an emergency aid entry provides no basis to search the premises ... |
| D94 | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:40` | 17% | 25t | `![[cases/Colorado v. Bertine#^pin-375]]` | ✓ | so long as that discretion is exercised according to standard criteria and on the basis of some ... |
| D95 | `content/use-of-force-and-liability/Section 1983 Liability and Qualified Immunity.md:35` | 17% | 32t | `![[cases/Monroe v. Pape#^pin-184]]` | ✓ | Misuse of power possessed by virtue of state law and made possible only because the wrongdoer i ... |
| D96 | `content/use-of-force-and-liability/Section 1983 Liability and Qualified Immunity.md:35` | 17% | 32t | `![[cases/United States v. Classic#^pin-326]]` | ✓ | Misuse of power possessed by virtue of state law and made possible only because the wrongdoer i ... |
| D97 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:38` | 17% | 37t | `![[cases/Alderman v. United States#^pin-171]]` | ✓ | can be successfully urged only by those whose rights were violated by the search itself not by ... |
| D98 | `content/warrant-exceptions/home-entry-and-search/Emergency Aid.md:43` | 16% | 28t | `![[cases/Mincey v. Arizona#^pin-392]]` | ✓ | the Fourth Amendment does not bar police officers from making warrantless entries and searches ... |
| D99 | `content/warrant-exceptions/Consent Searches.md:38` | 16% | 25t | `![[cases/United States v. Matlock#^pin-170]]` | ✓ | consent of one who possesses common authority over premises or effects is valid as against the ... |
| D100 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:40` | 16% | 35t | `![[cases/United States v. Salvucci#^pin-85]]` | ✓ | defendants charged with crimes of possession may only claim the benefits of the exclusionary ru ... |
| D101 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:44` | 16% | 28t | `![[cases/Minnesota v. Carter#^pin-90]]` | ✓ | an overnight guest in a home may claim the protection of the Fourth Amendment but one who is me ... |
| D102 | `content/searches/Aerial and Enhanced Surveillance.md:36` | 15% | 28t | `![[cases/Florida v. Riley#^pin-452]]` | ✓ | no intimate details connected with the use of the home or curtilage were observed and there was ... |
| D103 | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:56` | 15% | 26t | `![[cases/Graham v. Barnette#^pin-op10a]]` | ✓ | that probable cause of dangerousness is the standard that must be met for a warrantless mental ... |
| D104 | `content/searches/Private and Foreign Searches.md:37` | 14% | 25t | `![[cases/United States v. Jacobsen#^pin-115]]` | ✓ | additional invasions of respondents privacy by the Government agent must be tested by the degre ... |
| D105 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:38` | 14% | 32t | `![[cases/Rakas v. Illinois#^pin-143]]` | ✓ | depends not upon a property right in the invaded place but upon whether the person who claims t ... |
| D106 | `content/warrant-exceptions/Consent Searches.md:32` | 14% | 27t | `![[cases/United States v. Drayton#^pin-206]]` | ✓ | rejected in specific terms the suggestion that police officers must always inform citizens of t ... |
| D107 | `content/warrant-exceptions/home-entry-and-search/Emergency Aid.md:41` | 14% | 27t | `![[cases/Case v. Montana#^pin-slip7]]` | ✓ | reasonable suspicion Brigham City did not adopt Terry s reasonable suspicion standard for home ... |
| D108 | `content/searches/Aerial and Enhanced Surveillance.md:36` | 14% | 26t | `![[cases/Florida v. Riley#^pin-451]]` | ✓ | member of the public could legally have been flying over Riley s property in a helicopter at th ... |
| D109 | `content/the-right-to-counsel/Sixth Amendment Right to Counsel.md:30` | 14% | 27t | `![[cases/United States v. Gouveia#^pin-188]]` | ✓ | have involved points of time at or after the initiation of adversary judicial criminal proceedi ... |
| D110 | `content/warrant-exceptions/searching-a-vehicle/Automobile Exception.md:38` | 13% | 32t | `![[cases/United States v. Ross#^pin-825]]` | ✓ | If probable cause justifies the search of a lawfully stopped vehicle it justifies the search of ... |
| D111 | `content/warrant-exceptions/home-entry-and-search/Emergency Aid.md:41` | 13% | 25t | `![[cases/Case v. Montana#^pin-slip8]]` | ✓ | asked simply whether an officer had an objectively reasonable basis for believing that his entr ... |
| D112 | `content/use-of-force-and-liability/Use of Force.md:31` | 13% | 26t | `![[cases/Graham v. Connor#^pin-395]]` | ✓ | in the course of an arrest investigatory stop or other seizure of a free citizen should be anal ... |
| D113 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:40` | 13% | 29t | `![[cases/United States v. Payner#^pin-735]]` | ✓ | the interest in deterring illegal searches does not justify the exclusion of tainted evidence a ... |
| D114 | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:32` | 13% | 28t | `![[cases/Garrity v. New Jersey#^pin-497]]` | ✓ | option to lose their means of livelihood or to pay the penalty of self incrimination is the ant ... |
| D115 | `content/the-exclusionary-rule-remedies-and-standing/Standing to Challenge a Search.md:38` | 13% | 28t | `![[cases/United States v. Padilla#^pin-82]]` | ✓ | can be successfully urged only by those whose rights were violated by the search itself not by ... |
| D116 | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:34` | 9% | 26t | `![[cases/Lefkowitz v. Turley#^pin-84]]` | ✓ | adequate immunity the State may plainly insist that employees either answer questions under oat ... |

---

## Cross-page target frequency (canonical-source concentration)

Targets pinned/stated once but quoted on multiple pages (the canonical blocks embeds should point at). Top by inbound hits:

| target | kind | inbound hits |
|---|:--:|:--:|
| `cases/Arizona v. Gant#^pin-351` | pin | 2 |
| `cases/Maryland v. Buie#^pin-335` | pin | 2 |
| `cases/Herring v. United States#^pin-144` | pin | 2 |
| `cases/New York v. Harris#^pin-21` | pin | 2 |
| `cases/Miranda v. Arizona#^pin-444a` | pin | 1 |
| `cases/Duckworth v. Eagan#^pin-203` | pin | 1 |
| `cases/Colorado v. Connelly#^pin-167` | pin | 1 |
| `cases/Berghuis v. Thompkins#^pin-388` | pin | 1 |
| `cases/Rhode Island v. Innis#^pin-301` | pin | 1 |
| `cases/United States v. Liddell#^pin-1009` | pin | 1 |
| `cases/Garrity v. New Jersey#^pin-497` | pin | 1 |
| `cases/Garrity v. New Jersey#^pin-500` | pin | 1 |
| `cases/Lefkowitz v. Turley#^pin-84` | pin | 1 |
| `cases/Kalkines v. United States#^pin-1393` | pin | 1 |
| `cases/LaChance v. Erickson#^pin-268` | pin | 1 |

_Generated by `scripts/s8/shingles.py` sweep; 128 hits; adjudication pending (STOP after report per work order)._
