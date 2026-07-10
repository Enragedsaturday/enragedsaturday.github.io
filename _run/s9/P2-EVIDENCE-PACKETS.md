# S9 P2 — Evidence Packets (split-presence diffs + Delgado gap + Good-Faith over-inclusions)

> Lane `s9-p2-evidence-prep` · model `claude-opus-4-8` · read-only, zero CL. Prepares evidence for the **orchestrator** to adjudicate; this lane does NOT rule. Inputs: `_run/s9/P2-DISCORDANCE-QUEUE.md` (13 split-diff rows lines ~375-420 + INS v. Delgado coverage-gap line 395 + Lopez-Mendoza/Calandra over-inclusion lines 387-388); `_run/s9/thread-N-doctrine.jsonl` (`derived.splits` / `derived.negative_notes` / `derived.case_set`); `_run/s9/thread-P.json` (`split.signal_lines`).
>
> **Classification vocabulary** (per item): `TEACHES-THE-DIVERGENCE` (page presents the competing positions, whether or not it says "split") · `TEACHES-ONE-SIDE-ONLY` · `SILENT` · `RESOLVED-BY-LATER-AUTHORITY` (page correctly treats it as settled — settling case named). Quotes ≤6 lines; every quote carries a `content/…:line` locator.

---

## 1. Real-Time Tracking `P-d-0e214dcd8a56` (N-only-split; P-homed 3 / N-derived 8)

**N claim (queue verbatim).** `N-questions=['Post-Carpenter, is short-term real-time location tracking (real-time CSLI / phone pings) a Fourth Amendment search?', "Does prolonged fixed-point video surveillance of a home's exterior (pole cameras) become a search by aggregation (mosaic theory)?"]`

**N fuller (thread-N-doctrine.jsonl · derived.splits).**
- Q1 positions: SCOTUS *Carpenter* — "expressly reserved — 'we do not address' real-time CSLI or tower dumps (text-grounded)"; 6th Cir. *Skinner* (2012) — not a search on public highways (uncached); Mass. *Almonor* (2019) — pinging a phone is a search under the state constitution (uncached). **Confidence: low-medium** ("the reservation itself is text-grounded in Carpenter; the circuit/state positions are uncached").
- Q2 positions: 7th Cir. *Tuggle* (2021) — no search / 18 months of pole cameras (text-grounded); 1st Cir. en banc *Moore-Bush* (2022) — equally divided, no majority (uncached). **Confidence: medium.**

**What P teaches.** Page `content/searches/the-third-party-doctrine-and-digital-surveillance/Real-Time Tracking.md`.
- Q1 — the page presents the exact reserved/unsettled question and the competing frames:
  > "*[[Carpenter]]* pointedly **did not decide** real-time CSLI or 'tower dumps'… Lower courts are working out whether pinging a phone's real-time location, or short-term real-time CSLI, is governed by *[[Knotts]]* or *[[Carpenter]]*; the answer is unsettled and jurisdiction-dependent. Do not state a national rule for real-time CSLI." (`Real-Time Tracking.md:38`; echoed `:44`, `:48`, mermaid `:73` "RESERVED / unsettled").
- Q2 — the pole-camera / mosaic-aggregation question is **not on this page**; it is developed on the Aerial page (item 2). No pole-camera, video-surveillance, or *Tuggle* text appears in `Real-Time Tracking.md`.

**Classification.** Q1 = **TEACHES-THE-DIVERGENCE** (page frames it as reserved, *Knotts* vs *Carpenter*, jurisdiction-dependent — the same open question N derived, though it names no circuit cases). Q2 = **SILENT** on this page — N's pole-camera sub-question is mis-homed here; its natural home is Aerial & Enhanced Surveillance, where N *also* derived it (item 2). Reading: no P defect; Q1 is taught, Q2 belongs to a sibling page.

---

## 2. Aerial & Enhanced Surveillance `P-d-2732f927a8cc` (N-only-split; P-homed 5 / N-derived 9)

**N claim (queue verbatim).** `N-questions=["Is prolonged, warrantless pole-camera (or persistent aerial) surveillance of a home's exterior a Fourth Amendment search after Carpenter?"]`

**N fuller (derived.splits).** Positions: CA7 *Tuggle* — no search (text-verified); CA6 *Houston* (per Tuggle's text) — no search; CA10 *Jackson* (per Tuggle's text) — no search; CA1 en banc *Moore-Bush* + state courts — contrary/divided ("Federal circuit, federal district, and state courts have splintered"; positions not independently text-verified). **Confidence: high that the disagreement exists** (Tuggle's own text says the answer "is the subject of disagreement among our sister circuits and counterparts in state courts"); medium on precise alignment.

**What P teaches.** Page `content/searches/Aerial and Enhanced Surveillance.md`, "Lower-court developments":
  > "In *[[Tuggle]]*, 4 F.4th 505 (7th Cir. 2021), the Seventh Circuit held that months of continuous pole-camera recording of a home's exterior 'did not constitute a search under the current understanding of the Fourth Amendment,' while expressing unease that aggregated long-term surveillance may eventually warrant *[[Carpenter]]*-style treatment. … **The pole-camera question divides the lower courts and no controlling rule has emerged.**" (`Aerial and Enhanced Surveillance.md:58`).

**Classification.** **TEACHES-THE-DIVERGENCE.** The page states the *Tuggle* pole and expressly says the question "divides the lower courts and no controlling rule has emerged" — presenting the divergence N derived (it does not enumerate CA6/CA10/CA1, but N's own contrary-pole cases were uncached too). P non-signal is a `split.has_split_signal=False` mechanical miss; the prose teaches the divergence.

---

## 3. The Good-Faith Exception `P-d-2d77b33c5c60` — geofence good-faith split (N-only-split; P-homed 17 / N-derived 16)

**N claim (queue verbatim).** `N-questions=['For novel surveillance techniques (geofence warrants), how settled must authority be before Leon/Davis good faith saves the search -- does novelty itself support objectively reasonable reliance?']`

**N fuller (derived.splits).** Positions: 5th Cir. *Smith* (2024) — "Good faith applies because of the very novelty and dearth of authority, even while holding the geofence warrant unconstitutional"; 9th Cir. *Cano* (quoting *Lara*) — "Davis good faith only where binding appellate precedent SPECIFICALLY authorizes the search — novelty cuts against reliance"; 4th Cir. en banc *Chatrie* — "not text-verifiable from the lake cache (candidate_unverified)." **Confidence: medium.**

**What P teaches.** Page `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md`.
- Presents the *Smith* "novelty supports good faith" pole:
  > "*Smith* held geofence acquisition a search yet upheld admission under *[[Leon]]* given the novelty of the technology, 110 F.4th 817, 838…" (`:78`).
  > "courts reach for good faith exactly when the officer's reliance was reasonable and the illegality was someone else's mistake **or an unsettled question of law**, because there is no culpable conduct for suppression to deter." (`:80`; see also `:54`).
- The page does **not** present the 9th Cir. *Cano*/*Lara* counter-pole (that *Davis* good faith requires binding precedent *specifically authorizing* the search, so novelty cuts *against* reliance). No *Cano* / *Lara* / "specifically authorizes" text on the page.

**Classification.** **TEACHES-ONE-SIDE-ONLY.** The page teaches the *Smith*/"unsettled-law ⇒ good-faith" pole as its through-line and omits the competing 9th-Circuit "novelty defeats *Davis* reliance" position that makes N's question a genuine divergence. Load-bearing: `The Good-Faith Exception.md:78-80`.

---

## 4. SIA — Cell Phones `P-d-59506c88a4b0` (N-only-split; P-homed 1 / N-derived 7)

**N claim (queue verbatim).** `N-questions=['Adjacent (border-search, intersecting phone privacy post-Riley): what suspicion is required for forensic searches of electronic devices at the border?']`

**N fuller (derived.splits).** Positions: 9th Cir. *Cano* (2019) — manual = routine, forensic requires reasonable suspicion; 11th Cir. *Touset* (2018) — "no suspicion is necessary." **Confidence: medium**, with N's own caveat: "the split belongs to the **border-search topic**; noted here because both courts route around Riley's SIA holding."

**What P teaches.** Page `content/warrant-exceptions/searching-a-person/SIA Cell Phones.md`, "Lower-court developments":
  > "*[[Riley]]* is a bright line and has held; the frontier work is at the phone's edges (**border-search device inspections**, forced decryption, and the scope of a phone warrant) and is **treated on the digital-surveillance pages rather than here**. No lower-court development narrows the core rule that a warrant is required to search a phone's data incident to arrest." (`SIA Cell Phones.md:46`).

**Classification.** **SILENT** (deliberate cross-reference). The page expressly assigns the border-forensic-suspicion question to another page and teaches none of it. N itself concedes the split belongs to the border-search topic, not SIA. Reading: N over-derived a topically-adjacent split onto the wrong page; the P page's non-signal is correct.

---

## 5. Public-Employee Compelled Statements (Garrity) `P-d-7ef550636751` (N-only-split; P-homed 6 / N-derived 8)

**N claim (queue verbatim).** `N-questions=["When no statute or employer order expressly threatens discharge, does Garrity immunity attach on the employee's subjective belief that refusal means termination, and must that belief be objectively reasonable?"]`

**N fuller (derived.splits).** Positions: SCOTUS *Garrity* — grounded anchor only (coercion flowed from an express statutory forfeiture; the implicit-threat question is unresolved); courts of appeals (Friedrick/Camacho/Vangates line, uncached) — "circuits divide between requiring both a subjective belief and objective reasonableness, and broader implied-coercion readings." **Confidence: low** ("the split is asserted from lane knowledge; only the Garrity anchor is text-grounded").

**What P teaches.** Page `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md`, "Lower-court developments":
  > "The live line-drawing … tracks a few recurring frontiers: (a) whether *[[Garrity]]* immunity is **self-executing**, attaching from the objective compulsion of a job-loss threat even where **no formal warning** was read, **versus requiring a subjective belief that silence would cost the job that was objectively reasonable**… *Specific circuit and state authority … deferred to … R13 … and S9; no new case holding is asserted here.*" (`Garrity.md:62`).

**Classification.** **TEACHES-THE-DIVERGENCE.** Frontier (a) states exactly N's two competing poles (self-executing/objective compulsion vs. subjective-belief-that-was-objectively-reasonable). Names no circuit cases — matching N's own low-confidence, uncached posture. P `split.has_split_signal=False` is a mechanical miss; the prose teaches the divergence. Load-bearing: `Garrity.md:62` (frontier (a)).

---

## 6. Reverse-Keyword & Geofence Warrants `P-d-9b281351afcb` (N-only-split; P-homed 2 / N-derived 8)

**N claim (queue verbatim).** `N-questions=['Is government acquisition of geofence (bulk device-location) data a Fourth Amendment search?', 'Are geofence warrants categorically unconstitutional general warrants?']`

**N fuller (derived.splits).**
- Q1 positions: 5th Cir. *Smith* — yes, a search (text-grounded); 4th Cir. panel *Chatrie* — no, not a search for a limited window (uncached); SCOTUS *Chatrie* (2026) — "resolved: acquisition is a search." **Confidence: medium.**
- Q2 positions: 5th Cir. *Smith* — "categorically prohibited" general warrants (text-grounded); SCOTUS *Chatrie* — "declined to adopt the categorical rule; particularity/probable-cause left live." **Confidence: medium-low.**

**What P teaches.** Page `content/searches/the-third-party-doctrine-and-digital-surveillance/Reverse-Keyword and Geofence Warrants.md`.
- Q1 — treated as **settled by later authority**:
  > "**The threshold is settled: acquisition is a search.** After years of division in the lower courts, the Supreme Court resolved the geofence search-threshold question in *[[Chatrie]]*: compelling Google to produce a user's Location History **is** a search under *[[Carpenter]]*…" (`:36`; en banc 4th-Cir. 7-7 split recounted `:59`).
- Q2 — presented as **open, with the competing poles**:
  > "Whether a geofence **warrant** can ever satisfy probable cause and particularity is **unsettled**: the Fifth Circuit held such warrants are 'modern-day general warrants' and categorically unconstitutional…, but *[[Chatrie]]* **expressly declined** to adopt that categorical rule, leaving probable-cause/particularity the live question on remand." (`:29`; "*Smith*'s general-warrant holding is now the **persuasive minority position** binding only in the Fifth Circuit," `:38`).

**Classification.** Q1 = **RESOLVED-BY-LATER-AUTHORITY** (settling case named: *Chatrie v. United States*, 609 U.S. ___ (2026); page also recounts the prior lower-court division). Q2 = **TEACHES-THE-DIVERGENCE** (*Smith* categorical pole vs. *Chatrie* reservation; expressly "unsettled"). Load-bearing: `:36` (Q1), `:29` and `:38` (Q2).

---

## 7. Community Caretaking `P-d-baad20928a25` (N-only-split; P-homed 4 / N-derived 7)

**N claim (queue verbatim).** `N-questions=['What standard governs a noninvestigative caretaking/welfare seizure of a person in public after Caniglia?']`

**N fuller (derived.splits).** Positions: 10th Cir. *Garner* — Terry-style "specific and articulable facts" of caretaking need, balanced; 5th Cir. en banc *Rideau* — general reasonableness / public-welfare removal of hazardous intoxicated persons; 8th Cir. *Graham v. Barnette* — a mental-health seizure requires probable cause of dangerousness. **Confidence: medium-high** (all three grounded in cached circuit texts; "framed as divergent standards rather than a crisp yes/no split").

**What P teaches.** Page `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md`.
  > "State the scope honestly: this strand is circuit law. There is **no Supreme Court holding** squarely governing a caretaking **seizure of a person** in public. The doctrine is developed by the circuits…" (`:44`).
  > "So a *brief* welfare detention of an impaired person (*[[Garner]]* / *[[Rideau]]*) and a *serious psychiatric seizure* (*[[Graham]]*) are different objects: the former rides the *[[Garner]]* test; the latter climbs to **PC of dangerousness**." (`:56`; three-part *Garner* test `:46-52`; *Rideau* `:54`; contours "worked out fact-by-fact" `:87`).

**Classification.** **TEACHES-THE-DIVERGENCE.** The page presents all three circuit standards N derived and flags the strand as circuit law with no SCOTUS holding. Caveat for the adjudicator: the page partly **reconciles** them by seizure-type (brief welfare detention → *Garner*/*Rideau*; serious psychiatric → *Graham*'s PC-of-dangerousness) rather than staging a head-to-head conflict on one question — consistent with N's own "divergent standards rather than a crisp yes/no split." Load-bearing: `Community Caretaking.md:44` + `:56`.

---

## 8. Cell-Site Simulators `P-d-c1df624b8e8c` (N-only-split; P-homed 0 / N-derived 9)

**N claim (queue verbatim).** `N-questions=['Is deploying a cell-site simulator to force a phone to reveal its location a Fourth Amendment search requiring a warrant?']`

**N fuller (derived.splits).** Positions: state appellate / D.C. / S.D.N.Y. (*Andrews* Md. 2016; *Jones* D.C. 2017; *Lambis* S.D.N.Y. 2016) — yes, a search, warrant required (all uncached); 7th Cir. *Patrick* (2016) — declined to decide, affirmed on other grounds (uncached). **Confidence: low** ("no position is groundable in cached text; the verified anchors (Karo/Kyllo) strongly imply the home-location scenario is a search but no controlling holding exists").

**What P teaches.** Page `content/searches/the-third-party-doctrine-and-digital-surveillance/Cell-Site Simulators.md`.
  > "There is **no controlling Supreme Court decision**, but the governing analogies point one way: using the device to locate a phone **inside a home** … is a search (*[[Karo]]*…), as is aiming sense-enhancing technology 'not in general public use' at a home (*[[Kyllo]]*…). … Treat cell-site-simulator deployment as **warrant-requiring**, and the precise constitutional rule as **unsettled**." (`:27`).
  > "*State v. Andrews* (Md. … 2016) held … a Fourth Amendment search requiring a warrant… It remains the most-cited judicial statement that cell-site-simulator deployment needs a warrant." (`:52`).

**Classification.** **TEACHES-ONE-SIDE-ONLY** (warrant-required, by *Karo*/*Kyllo*/*Carpenter* analogy + *Andrews* + DOJ/DHS policy), while expressly flagging "no controlling SCOTUS" and the rule as "unsettled." Note for the adjudicator: N's "split" is not a genuine two-pole doctrinal conflict — its contrary case (*Patrick*) merely *declined to decide*, and N concedes "no controlling holding exists" and no position is text-groundable. P and N agree the area is open; the page teaches the operative warrant-required analogy. Load-bearing: `Cell-Site Simulators.md:27`.

---

## 9. Entrapment `P-d-d2d0ff10db5d` (N-only-split; P-homed 8 / N-derived 8)

**N claim (queue verbatim).** `N-questions=['Subjective (predisposition) versus objective (police-conduct) test for entrapment', 'Viability and scope of the freestanding outrageous-government-conduct due-process defense after Russell and Hampton']`

**N fuller (derived.splits).**
- Q1 positions: *Sorrells*/*Sherman*/*Russell* majorities — subjective (predisposition controls); Roberts, J. in *Sorrells* — objective; Frankfurter, J. concurring in *Sherman* — objective. **Confidence: high**, noting "this is an intra-Court methodological split **resolved for federal law in favor of the subjective test**."
- Q2 positions: SCOTUS (*Russell* dictum; *Hampton* plurality narrowing) — "reserved but never applied"; courts of appeals — "divide between recognizing the defense in principle and repudiating it" (uncached). **Confidence: medium** ("the SCOTUS reservation is text-grounded; the circuit disagreement rests on lane knowledge").

**What P teaches.** Page `content/fair-trial-and-reliability-doctrines/Entrapment.md`.
- Q1 — presents both tests and states the federal resolution:
  > "The objective-test minority (a non-federal alternative). A minority of states apply an **objective** test that asks whether the **police conduct** would induce a hypothetical law-abiding person… It is illustrative only and **does not govern in federal court**, which applies the subjective/predisposition test; *[[Russell]]* reaffirmed the subjective test and rejected the objective approach." (`:38`).
- Q2 — presents the SCOTUS-reservation status:
  > "The Court reserved the possibility that 'some day … [police conduct may be] so outrageous that due process principles would absolutely bar' … but held *[[Russell]]* 'distinctly not of that breed.' In *[[Hampton]]*, three Justices would have foreclosed the due-process route entirely, but Justices Powell and Blackmun … expressly **reserved** it… The defense exists on paper and almost never succeeds." (`:40`; Key-cases *Hampton* `:66`).

**Classification.** Q1 = **TEACHES-THE-DIVERGENCE + RESOLVED-BY-LATER-AUTHORITY** (subjective vs. objective competing tests presented; federal law resolved subjective by *United States v. Russell* — the page frames objective as minority-state/non-governing). Q2 = **TEACHES-ONE-SIDE-ONLY / SILENT on the circuit split** (page fully teaches the SCOTUS "reserved, rarely successful" status but does **not** map N's courts-of-appeals recognize-vs-repudiate divergence — which N itself could only assert from uncached lane knowledge). Load-bearing: `Entrapment.md:38` (Q1), `:40` (Q2).

---

## 10. Inventory Searches `P-d-e5fc7db3f3c7` (N-only-split; P-homed 9 / N-derived 11)

**N claim (queue verbatim).** `N-questions=["Must the impoundment predicate itself be justified by a reasonable, non-pretextual community-caretaking rationale (and by standardized criteria) before an inventory can stand — and how far does an officer's investigatory motive taint an otherwise policy-compliant inventory?"]`

**N fuller (derived.splits).** Positions: 10th Cir. *Braxton* (2023, following Venezia/Sanders) — impoundment must be a reasonable, non-pretextual exercise of community caretaking; inventory falls with the impoundment (text-grounded); SCOTUS baseline *Bertine*/*Wells* — standardized criteria + no "ruse for general rummaging," but "mixed-motive and impoundment-justification details left open" (text-grounded). **Confidence: low as a circuit SPLIT** — "only the 10th Circuit's position is text-verifiable in the lake … recorded as **doctrinal openness with one grounded pole**."

**What P teaches.** Page `content/warrant-exceptions/searching-a-vehicle/Inventory Searches.md`.
  > "The Supreme Court framework (*[[Opperman]]* / *[[Bertine]]* / *[[Wells]]* / *[[Lafayette]]*) is settled; the live circuit work is over **how much the impoundment decision itself must be policy-governed**, and how courts police the line between a genuine inventory and an investigatory search." (`:52`).
  > "*[[Braxton]]* (10th Cir. 2023) — *the impoundment/inventory must be proved, not assumed.*" (`:55`); "Circuits that scrutinize the impoundment decision (was there a caretaking reason to tow at all?) apply the same anti-pretext logic one step earlier…" (`:57`; requirement stated at `:26`, `:47`).

**Classification.** **TEACHES-THE-DIVERGENCE** (of the openness kind). The page presents the impoundment-predicate + anti-pretext frontier as "live circuit work," grounds the 10th-Circuit *Braxton* pole, and treats the SCOTUS baseline as settled-but-silent on impoundment justification — the same "doctrinal openness with one grounded pole" N recorded. Convergent substance; the split-signal difference is only that P's detector did not tag it and N labeled it a low-confidence split. Load-bearing: `Inventory Searches.md:52` + `:57`.

---

## 11. Private & Foreign Searches `P-d-176e2487d9cb` — **P-only-split** (P-homed 6 / N-derived 8)

**Queue.** `split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]`

**P split-signal lines (thread-P.json `split.signal_lines`).**
- `line 59`: "*The digital private-search frontier is automated hash-matching, and the circuits are split.* Providers scan uploaded files against databases of hash values … whether an officer's later opening of a flagged file is a fresh search or merely re-does the private 'search.'"
- `line 64`: "The split is squarely about *[[Jacobsen]]*'s 'virtual certainty' test applied to an algorithm: **the Ninth Circuit demands that a human actually have viewed the specific file, while the Fifth and Sixth treat a reliable hash match as the functional equivalent. The Supreme Court has not resolved it.**"
- `line 109`: "*United States v. Miller*, 982 F.3d 412 (6th Cir. 2020) (pinpoint: 416) — hash-match circuit split; brief-mention terminal…"

**What P teaches (page `content/searches/Private and Foreign Searches.md`).** A grounded, named two-pole split in "Lower-court developments":
  > 9th Cir. *[[Wilson]]*, 13 F.4th 961 (2021) — where "**no human had ever viewed**" the hash-flagged images, the officer's viewing "exceeded the scope of any antecedent private search and was itself a government search." (`:61`).
  > 5th/6th Cir. *[[Reddick]]* (2018) and *United States v. Miller* (2020) — a hash match "created a 'virtual certainty' … meeting '*Jacobsen*'s required level of certainty'" so opening is **not** a search. (`:62`); synthesis at `:64`.

**Does N address it?** N `derived.splits = []`. But N `derived.negative_notes[0]` **corroborates the disagreement exists** and explains the non-derivation:
  > "The known circuit disagreement over applying the *Jacobsen* private-search scope rule to electronic devices (container-by-container vs whole-device unit of search) has **NO lake coverage** — no Runyan/Lichtenberger/Sparks/Ackerman records — so no split row can be honestly derived."

**Which reading the texts support.** **N under-derivation (fail-closed), not P overclaim.** P teaches a genuine, text-anchored circuit split (*Wilson* vs *Reddick*/*Miller*, pincite 416 verified via the FA-Framework LCD). N recognized a digital private-search circuit disagreement but framed it around a *different, uncached* case line (Runyan/Lichtenberger/Sparks/Ackerman) and declined to emit a split row for lack of lake grounding. The P-only diff is a coverage/grounding artifact of N's honesty, not a P defect. **P classification: TEACHES-THE-DIVERGENCE** (real, grounded). Load-bearing: `Private and Foreign Searches.md:64` (P); `thread-N-doctrine.jsonl` Private-&-Foreign `negative_notes[0]` (N corroboration).

---

## 12. Arrest & Arrest Warrants `P-d-aa5b3e10c79c` — **P-only-split** (P-homed 4 / N-derived 18)

**Queue.** `split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]`

**P split-signal line (thread-P.json).**
- `line 51`: "The arrest-standard core is settled at the Supreme Court, so the live questions are refinements **rather than a circuit split on the basic rule**."

**What P teaches (page `content/seizures/arrests/Arrest and Arrest Warrants.md`).** The page teaches the core as **settled**, not split. The lone "signal" sentence *denies* a split:
  > "The arrest-standard core is settled at the Supreme Court, so the live questions are refinements **rather than a circuit split on the basic rule**." (`:51`).
  The two LCD bullets that follow are SCOTUS refinements (*Nieves* retaliatory overlay `:53`; *Wesby* totality `:54`), not a circuit divergence.

**Does N address it?** N `derived.splits = []`, and N `derived.negative_notes` affirmatively **agree there is no split**:
  > "Worklist split_signal not corroborated by cached texts for this topic's core rule: the lake carries no circuit opinions mapping the in-presence question; the home-entry/constructive-entry splits belong to **Arrest in the Home**."
  (plus the *Atwater* n.11 in-presence question is an expressly-reserved SCOTUS question, not a circuit split.)

**Which reading the texts support.** **P's split-signal is a keyword false-positive** — the mechanical detector fired on the token "split" inside a sentence that negates a split. There is **no divergence to adjudicate**: the page teaches the core as settled and N independently derived no split, with negative_notes attributing the only true frontiers (in-presence; constructive/home entry) to *Atwater* n.11 (reserved) and to the **Arrest in the Home** page. **P classification: RESOLVED/SETTLED — no split taught** (false-positive signal). Load-bearing: `Arrest and Arrest Warrants.md:51` (the negating sentence) + N `negative_notes`.

---

## 13. Prompt Probable-Cause Determination `P-d-c4fefc8243df` — **P-only-split** (P-homed 2 / N-derived 6)

**Queue.** `split diff [P-only-split]: P_signal=True N_split=False; N-questions=[]`

**P split-signal line (thread-P.json).**
- `line 49`: "The 48-hour framework is settled at the Supreme Court; the recurring questions below the Court are application questions … **rather than a split on the rule itself**. No controlling circuit split is mapped in this build…"

**What P teaches (page `content/seizures/arrests/Prompt Probable-Cause Determination.md`).** Settled 48-hour framework (*Gerstein*/*McLaughlin*); the "signal" sentence again *denies* a split:
  > "The 48-hour framework is settled at the Supreme Court; the recurring questions below the Court are application questions (what delay is 'unreasonable' within the window, and what remedy a *[[Gerstein]]* violation carries) **rather than a split on the rule itself. No controlling circuit split is mapped in this build**…" (`:49`).

**Does N address it?** N `derived.splits = []`; N `derived.negative_notes` treat the open points as **remedy/application questions, not a split**:
  > "Neither Gerstein nor McLaughlin (cached texts) specifies the **remedy** for a violation … no cached text resolves suppression for McLaughlin delay." (and "Powell v. Nevada … is not in the lake corpus").

**Which reading the texts support.** Same as item 12: **P's split-signal is a keyword false-positive** on a sentence that negates a split; P and N **agree** the 48-hour framework is settled and the residue is remedy/application questions, not a circuit split. No divergence to adjudicate. **P classification: RESOLVED/SETTLED — no split taught** (false-positive signal). Load-bearing: `Prompt Probable-Cause Determination.md:49` + N `negative_notes`.

---

## 14. INS v. Delgado — coverage-gap on When a Seizure Occurs `P-d-72c3cb092c3f` (P-homed 20 / N-derived 16)

**Queue (verbatim).** `UNKNOWN coverage-gap: **INS v. Delgado** (cluster 111148, N-role limiting, cand_unverified=False)`. N `derived.case_set` includes: `INS v. Delgado (cluster 111148) role=limiting`. N `derived.negative_notes` note only that *Summers/Bailey/Mena* were screened out as "authority-to-detain doctrine rather than threshold" — Delgado was **retained** as a threshold *limiting* case.

**Ledger status (verified).** Delgado / cluster 111148 appears in **zero** `thread-P.json` items; no `cases/INS v. Delgado.md` exists on disk; `reconciliation.jsonl` marks it `gap_class:"UNKNOWN-gap"`, `resolved_p_path:null`. So it is **in neither P ledger** — not homed to this page (P-homed 20 excludes it) and not homed-elsewhere in the P corpus.

**Page treatment of workplace / factory encounters.** Page `content/seizures/Seizure of the Person.md` has **no** treatment of workplace, factory-survey, or workforce encounters (token scan for `factory`/`workforce`/`workplace`/`Delgado` = 0 hits). The nearest doctrinal neighborhood on the page is the confined-setting / "free to terminate the encounter" line, taught through *Bostick* and *Drayton*:
  > "***[[Florida v. Bostick]]*** … *Confined setting.* Where the person is already confined (a bus seat), the test is reframed: a seizure occurs only if a reasonable person would not feel free to decline the officers' requests or otherwise terminate the encounter." (`Seizure of the Person.md:106`).
  > "***[[United States v. Drayton]]*** … *Bus sweep.* No seizure where officers do not block exits, brandish weapons, or use a commanding tone…" (`:107`).

**Where Delgado would slot.** INS v. Delgado (the INS "factory survey" case; N-role *limiting* — questioning of workers, with agents posted near exits, held not a seizure of the workforce) is the factory-workplace sibling of *Bostick*/*Drayton*: it is the origin of the "free to decline/terminate the encounter" formulation *Bostick* adopts, on the show-of-authority (*Mendenhall*) branch. It would slot either in the "Road one, show of authority — *Mendenhall* 'free to leave'" strand / consensual-encounter continuum (`:37`, `:47`), or in the "Related cases across doctrines" table beside *Bostick*/*Drayton* (`:106-107`), as the workplace/questioning-alone limiting case. (Citation commonly *INS v. Delgado*, 466 U.S. 210 (1984); N-derived, **not** lake-quote-verified in this evidence-prep lane — flagged for the orchestrator.)

**Summary for adjudication.** P coverage gap (not P overclaim): N's blind derivation found a legitimate threshold *limiting* case that the page teaches *around* (via *Bostick*/*Drayton*) but never cites, and that is absent from the entire P corpus. The page is **SILENT** on the workplace/factory scenario specifically.

---

## 15. INS v. Lopez-Mendoza — over-inclusion candidate on The Good-Faith Exception `P-d-2d77b33c5c60`

**Queue.** `over-inclusion candidate: cases/Immigration & Naturalization Service v. Lopez-Mendoza.md (P-role: Key — Progeny / Refinement)` (also advisory line 431). N `derived.case_set` for Good-Faith does **not** contain Lopez-Mendoza (N's blind set = the reliance family + four-floors + geofence progeny: Leon, Sheppard, Krull, Evans, Herring, Davis, Groh, Franks, Malley, Messerschmidt, DeFillippo, Smith-5th, Morton-5th, Cano-9th, Jackson-8th, Chatrie-4th).

**What P says about it.** Page `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md` treats Lopez-Mendoza as a **forum/proceedings-scope boundary** of the deterrence engine, not a reliance-family good-faith holding:
  > "The same cost-benefit calculus keeps the rule out of proceedings where its deterrent value is too slight… It does not apply to … **civil removal/deportation** hearings (*[[Lopez-Mendoza]]*, 468 U.S. 1032, 1050 (1984))… **These are not 'good faith' holdings, but they run on the identical engine**: no net deterrence, no suppression." (`:52`; Key-cases row "**Boundary.** The rule generally does not apply in civil removal/deportation proceedings," `:95`).

**Is the P-role supported? N-blindness or mis-homing?** The **home is supported** — the page genuinely and expressly discusses Lopez-Mendoza (as a deterrence-engine forum boundary). The P-role label "**Key — Progeny / Refinement**" is **loosely applied**: the page itself files it as a "**Boundary**" case, not a good-faith progeny. This is **N-blindness, not mis-homing**: Lopez-Mendoza is a *proceedings-scope* case (where the exclusionary rule applies), a sub-doctrine N did not derive because N scoped its Good-Faith set to *reliance-family* cases — confirmed by N's `negative_notes[2]`: "every SCOTUS extension involves reliance on a third-party source (warrant, statute, court record, police database, binding precedent)." Load-bearing: `The Good-Faith Exception.md:52` + `:95`.

---

## 16. United States v. Calandra — over-inclusion candidate on The Good-Faith Exception `P-d-2d77b33c5c60`

**Queue.** `over-inclusion candidate: cases/United States v. Calandra.md (P-role: Key — Progeny / Refinement)` (also advisory line 431). N `derived.case_set` for Good-Faith does **not** contain Calandra (same blind set as item 15).

**What P says about it.** Calandra is used **prominently and foundationally** — as the deterrent-remedy-not-a-right rationale that opens the doctrine, and as the grand-jury forum boundary:
  > "Suppression 'is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved.' *[[Calandra]]*, 414 U.S. 338, 348 (1974)." (`:33`).
  > "It does not apply to **grand-jury** questioning (*[[Calandra]]*, 414 U.S. at 348)…" (`:52`; Key-cases row "**Deterrent remedy, not a right.** … it does not apply to grand-jury questioning," `:93`).

**Is the P-role supported? N-blindness or mis-homing?** The **home is strongly supported** — the page's opening rationale rests on Calandra and it recurs as a forum boundary. The P-role label "**Key — Progeny / Refinement**" is **chronologically inapt** (Calandra, 1974, *predates* the *Leon* anchor, 1984, so it is not a "progeny" of the good-faith exception; it is better described as the **foundational deterrence-rationale / forum-boundary anchor**). But the mis-label does **not** make it mis-homed. This is **N-blindness**: like Lopez-Mendoza, Calandra is a rationale/proceedings-scope case outside N's reliance-family scope, which N's `negative_notes[2]` explains. Load-bearing: `The Good-Faith Exception.md:33` + `:52`/`:93`.

---

## Disposition table (item | classification | load-bearing quote location)

| # | Item (doctrine · question) | Classification | Load-bearing quote location |
|---|---|---|---|
| 1 | Real-Time Tracking · Q1 real-time CSLI / Q2 pole cameras | Q1 **TEACHES-THE-DIVERGENCE**; Q2 **SILENT** (mis-homed → Aerial) | `content/searches/the-third-party-doctrine-and-digital-surveillance/Real-Time Tracking.md:38` |
| 2 | Aerial & Enhanced Surveillance · pole-camera search | **TEACHES-THE-DIVERGENCE** | `content/searches/Aerial and Enhanced Surveillance.md:58` |
| 3 | Good-Faith · geofence novelty ⇒ good faith? | **TEACHES-ONE-SIDE-ONLY** (Smith pole; Cano counter-pole absent) | `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:78-80` |
| 4 | SIA — Cell Phones · border forensic-search suspicion | **SILENT** (page cross-refs to Border Searches; N concedes off-topic) | `content/warrant-exceptions/searching-a-person/SIA Cell Phones.md:46` |
| 5 | Garrity · self-executing vs subjective-belief immunity | **TEACHES-THE-DIVERGENCE** | `content/confessions-interrogation-and-the-fifth-amendment/Public-Employee Compelled Statements (Garrity).md:62` |
| 6 | Geofence · Q1 acquisition-a-search / Q2 categorical general warrant | Q1 **RESOLVED-BY-LATER-AUTHORITY** (*Chatrie* 2026); Q2 **TEACHES-THE-DIVERGENCE** | `content/searches/the-third-party-doctrine-and-digital-surveillance/Reverse-Keyword and Geofence Warrants.md:36` (Q1); `:29`/`:38` (Q2) |
| 7 | Community Caretaking · person-in-public standard post-Caniglia | **TEACHES-THE-DIVERGENCE** (partly reconciled by seizure-type) | `content/warrant-exceptions/home-entry-and-search/Community Caretaking.md:44` + `:56` |
| 8 | Cell-Site Simulators · warrant required? | **TEACHES-ONE-SIDE-ONLY** (warrant-required analogy; flags no-SCOTUS/unsettled; N "split" = openness) | `content/searches/the-third-party-doctrine-and-digital-surveillance/Cell-Site Simulators.md:27` |
| 9 | Entrapment · Q1 subjective vs objective / Q2 outrageous-conduct DP | Q1 **TEACHES-THE-DIVERGENCE + RESOLVED** (*Russell*, subjective); Q2 **TEACHES-ONE-SIDE-ONLY / SILENT on circuit split** | `content/fair-trial-and-reliability-doctrines/Entrapment.md:38` (Q1); `:40` (Q2) |
| 10 | Inventory Searches · impoundment-predicate + mixed-motive | **TEACHES-THE-DIVERGENCE** (openness; 10th-Cir. *Braxton* pole grounded) | `content/warrant-exceptions/searching-a-vehicle/Inventory Searches.md:52` + `:57` |
| 11 | Private & Foreign (P-only) · hash-match private-search split | **TEACHES-THE-DIVERGENCE** (genuine, grounded) — diff = **N under-derivation** (fail-closed, uncached), N negative_notes corroborate | `content/searches/Private and Foreign Searches.md:64`; N `negative_notes[0]` |
| 12 | Arrest & Arrest Warrants (P-only) | **SETTLED — no split** (P signal is keyword false-positive; sentence negates a split; N agrees) | `content/seizures/arrests/Arrest and Arrest Warrants.md:51` |
| 13 | Prompt Probable-Cause Determination (P-only) | **SETTLED — no split** (P signal is keyword false-positive; N agrees, residue = remedy/application) | `content/seizures/arrests/Prompt Probable-Cause Determination.md:49` |
| 14 | INS v. Delgado (When a Seizure Occurs gap) | **SILENT** on workplace/factory; slots with *Bostick*/*Drayton* free-to-terminate line; in neither P ledger (UNKNOWN-gap) | `content/seizures/Seizure of the Person.md:106-107` (slot); token-scan absence |
| 15 | Lopez-Mendoza (Good-Faith over-inclusion) | **Home supported** (forum boundary); role label loose ("Boundary" not "progeny") — **N-blindness** (proceedings-scope), not mis-homing | `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:52` + `:95` |
| 16 | Calandra (Good-Faith over-inclusion) | **Home supported** (foundational rationale + grand-jury boundary); role label chronologically inapt ("progeny" pre-dates *Leon*) — **N-blindness**, not mis-homing | `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:33` + `:52`/`:93` |
