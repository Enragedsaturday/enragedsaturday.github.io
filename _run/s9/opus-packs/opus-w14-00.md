# S9 R1 panel-review — Opus model-diversity lane (prompt pack)

You are the **Claude/Opus** leg of the S9 three-lane adversarial panel (1 Claude + 2 Codex, R1). The two Codex lanes carry the A (support/quote-fidelity) and B (currency/treatment) attack lenses; **you carry model diversity and MUST vote on every paneled assertion across BOTH lenses' concerns.** You are refute-framed: try hard to break each assertion; **default to REFUTED on uncertainty**; never fabricate a cite, quote, or holding; use ONLY the evidence inlined below (no search, no outside knowledge). You are a SIGHTED reviewer — the FULL lake record (judgment fields included) is inlined.

You are a WRITER lane, not an adjudicator: you FIND and VOTE. You do not tally, adjudicate, or close any row — the orchestrator does.

For EACH group below, return one JSON object with the exact `reviewed[]` shape from the output contract (identical framing to the Codex lenses). Emit a finding object ONLY for a real defect (verdict refuted / stands-modified); a group you find wholly clean returns all-`stands` verdicts (the harness records a clean attestation). Concatenate the per-group JSON objects into a top-level `{"packs": [ ... ]}` array, one entry per group, each carrying its `group_id`.


OUTPUT CONTRACT — return ONE JSON object, nothing else:
{
  "lens": "A" | "B",
  "group_id": "<echo the group id>",
  "reviewed": [
    {
      "assertion_id": "<from group_inventory.jsonl>",
      "dimension": "existence|support|quote_fidelity|pincite|treatment|black_letter",
      "verdict": "stands" | "refuted" | "stands-modified",
      "verifiable_from_disclosed": true | false,
      "defect": null,   // null when verdict=="stands"; else an object:
      //  {"problem": "...", "severity": "high|medium|low", "proposed_fix": "...", "evidence_quote": "verbatim from disclosed evidence or null", "needs_cl": true|false, "locator_note": "..."}
      "reasons": ["short evidence-grounded reason", "..."],
      "breaks_true_positives": true | false,
      "residual_risks": ["..."],
      "suggested_tightening": "... or null"
    }
  ],
  "notes": ""
}
Rules: verdict=='stands' <=> defect==null (assertion survives your attack). verdict=='refuted' <=> a real defect (the assertion as framed is wrong). verdict=='stands-modified' <=> survives but needs a stated modification (a minor defect). Review EVERY assertion_id in group_inventory.jsonl exactly once. Output ONLY the JSON object.
---

## GROUP: _overhaul2/lake/cases/United States v. Amos.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Amos
type: case
citation: "88 F.4th 446 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 3d Cir.
court_level: coa
circuit: ca3
year: 2023
date_decided: 2023-12-14
docket: 20-3298
authority_weight: "Binding in-circuit — 3d Cir."
treatment:
  field_i_validity: unverified
  as_of_content: null
  as_of_treatment: null
  composite_basis: unverified
  composite_basis_ref: null
  varies_by_point: false
  scope_note: "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9452158/united-states-v-shiheem-amos/"
  cluster_id: 9452158
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Amos
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Seizure of the Person]]"
    role: Key
related:
  - "[[Seizure of the Person]]"
  - "[[California v. Hodari D.]]"
  - "[[Brendlin v. California]]"
  - "[[United States v. Mendenhall]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - show-of-authority
  - terry-stop
holding: "A show of authority does not effect a Fourth Amendment seizure unless the suspect actually submits to it; a suspect already in motion who raises his hands only partway and pauses momentarily before fleeing has not submitted, so no seizure occurs until he is physically restrained — meaning a handgun that falls at that point is not the fruit of any earlier, unsupported seizure."
---

# United States v. Amos

*88 F.4th 446 (3d Cir. 2023)* (No. 20-3298) · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9452158 → opinion 9909983 (88 F.4th 446, decided 2023-12-14); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
At about 2:00 a.m., two uniformed Philadelphia officers responded to a radio call about a person screaming and a man assaulting a woman near Eddie's Café. Finding no one there, they saw Shiheem Amos walking alone in an alleyway, "stomping [his] feet" and "throwing his arms around." The officers drove the wrong way down a one-way street with their lights on to cut him off and parked in the mouth of the alley, in Amos's path. Officer Lemos commanded Amos to stop and put his hands up; Amos raised his hands to a "halfway point," stopped for "[m]aybe a second," and then ran. Officer Mastroianni caught and handcuffed him about three car lengths away, and a handgun fell from Amos's pocket. Charged as a felon in possession, Amos moved to suppress the gun, arguing he had been seized pre-flight without reasonable suspicion. The district court found no pre-flight seizure and denied the motion.

## Issue
Whether Amos was "seized" before he fled — which requires both a show of authority and actual submission to it — so that the handgun recovered after his flight was the fruit of a seizure unsupported by reasonable suspicion.

## Rule
A seizure by show of authority is not complete without submission. The Third Circuit held the officers did show authority: "When a uniformed officer approaches an individual in the middle of the night in a marked police car and commands that person to stop and raise his or her hands, that is a show of authority." — slip op. at 10. But a show of authority alone does not seize a person; quoting *[[Brendlin v. California]]*, the court reaffirmed that "there is no seizure without actual submission; otherwise, there is at most an attempted seizure, so far as the Fourth Amendment is concerned."

## Application
Amos raised his hands only partway and paused for "maybe a second" before fleeing — the conduct of a suspect "already in motion" who refuses to stop, not the submission of the stationary, "frozen" suspect in *United States v. Lowe* who was seized precisely because he remained still. Momentary compliance is not submission. Because Amos never submitted, no seizure occurred until Officer Mastroianni physically overpowered him after the flight; the pre-flight encounter therefore required no reasonable suspicion, and the handgun that fell during the arrest was not the fruit of an unlawful seizure.

## Conclusion
The denial of the motion to suppress was **affirmed**; the court [[Reading and Citing Cases#on-remand|remanded]] for resentencing because Amos's prior Pennsylvania aggravated-assault conviction did not qualify as a "crime of violence." Nygaard, J., wrote for the court (Bibas, Nygaard, Fuentes, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Amos* illustrates the submission requirement of *[[California v. Hodari D.|Hodari D.]]* and *[[Brendlin v. California|Brendlin]]*: a moving suspect who only momentarily pauses before running has not submitted to a show of authority, so the Fourth Amendment clock does not start until physical restraint — the point at which reasonable suspicion is measured.

## Appears on
- [[Seizure of the Person]] — *Key*

## Sources
- [*United States v. Amos*, 88 F.4th 446 (3d Cir. 2023)](https://www.courtlistener.com/opinion/9452158/united-states-v-shiheem-amos/) — pinpoint: slip op. at 10 (show-of-authority holding); the CL opinion text carries the slip-opinion page numbers rather than 88 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4390887f1c059898", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Amos"}, "payload": {"all": [{"cite": "88 F.4th 446", "page": "446", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}], "display": "88 F.4th 446", "official": {"cite": "88 F.4th 446", "page": "446", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "88"}, "official_selection_present": true, "record_id": "United States v. Amos"}}
{"assertion_id": "906e2f3db102df70", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Amos"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Amos", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Amos

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Amos",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Shiheem Amos",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Amos",
    "court": "3d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2023-12-14",
    "year": 2023,
    "docket": "20-3298",
    "cluster_id": 9452158,
    "lead_opinion_id": 9909983,
    "sibling_ids": [],
    "absolute_url": "/opinion/9452158/united-states-v-shiheem-amos/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "88 F.4th 446",
      "volume": "88",
      "reporter": "F.4th",
      "page": "446",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "88 F.4th 446",
        "volume": "88",
        "reporter": "F.4th",
        "page": "446",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "88 F.4th 446",
    "official_selection": {
      "court_class": "coa",
      "selected": "88 F.4th 446",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "unverified",
    "as_of_content": null,
    "as_of_treatment": null,
    "composite_basis": "unverified",
    "composite_basis_ref": null,
    "varies_by_point": false,
    "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": null,
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-07T01:38:56Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-amos--9452158",
      "to_record_id": "United States v. Amos",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Amos

```
                                 PRECEDENTIAL


  UNITED STATES COURT OF APPEALS
       FOR THE THIRD CIRCUIT

                 __________

                 No. 20-3298
                 __________

      UNITED STATES OF AMERICA

                      v.

              SHIHEEM AMOS,
                         Appellant
                __________

On Appeal from the United States District Court
   for the Eastern District of Pennsylvania

(District Court Criminal No. 2-18-cr-00571-001)
  District Judge: Honorable Gerald J. Pappert

           Argued: January 23, 2023

BEFORE: BIBAS, NYGAARD, and FUENTES,
            Circuit Judges


          (Filed: December 14, 2023)
Anthony J. Carissimi
Timothy M. Stengel
Robert A. Zauzmer [Argued]
Office of United States Attorney
615 Chestnut Street
Suite 1250
Philadelphia, PA 19106
       Counsel for Appellee

Abigail E. Horn [Argued]
Federal Community Defender Office
for the Eastern District of Pennsylvania
601 Walnut Street
The Curtis Center, Suite 540 West
Philadelphia, PA 19106
        Counsel for Appellant
                          __________

                 OPINION OF THE COURT
                       __________

NYGAARD, Circuit Judge.
       Shiheem Amos appeals the District Court’s denial of his
motion to suppress and his criminal sentence. He first argues
that the court erred when it denied his motion to suppress a
firearm because he was seized without reasonable suspicion.
Second, he argues that the court erred when it included a
United States Sentencing Guidelines’ crime of violence en-
hancement for a previous state court conviction and sentenced
him to 62 months’ imprisonment. We will affirm the denial of
the motion to suppress, but because Amos’s prior conviction is
not a crime of violence, we will remand for resentencing.




                              2
            I.    Background
       On September 26, 2018, police officers Hugo Lemos
and Nicholas Mastroianni were working the overnight shift as
patrol officers in southwest Philadelphia. At about 2:00 a.m.,
they received a radio call for a person screaming at the inter-
section of 65th Street and Dicks Avenue outside Eddie’s Café
and a man assaulting a woman on the highway. The officers
were nearby and arrived at Eddie’s Café within two minutes.
No one was outside Eddie’s Café.
        The officers continued driving past the café on 65th
Street and Officer Lemos saw one pedestrian, later discovered
to be Shiheem Amos, walking alone in an alleyway across the
street. Amos was walking toward 64th Street and was “stomp-
ing [his] feet, and kind of throwing his arms around,” accord-
ing to Officer Lemos. App’x 85. The officers drove around the
block to cut Amos off, driving the wrong way down a one-way
street with the overhead lights on. The officers parked midway
in the entrance to the alleyway and Amos continued to walk
toward them. Officer Lemos got out of the vehicle and told
Amos to stop and put his hands up. 1 Officer Lemos testified
that Amos placed his hands at a “halfway point” and stopped

1
  There is some discrepancy about where Officer Lemos was
when he asked Amos to stop. At the preliminary hearing, he
testified that he was out of the car. At the suppression hearing,
he testified that he was still in the car and yelled out the win-
dow. He testified that the earlier testimony was probably accu-
rate. The District Court explained that any discrepancy did not
impact its assessment of Officer Lemos’s credibility or alter its
legal analysis.




                               3
for “[m]aybe a second.” App’x 89, 91. Amos then ran diago-
nally and reached about three car lengths away from the offic-
ers. Officer Mastroianni quickly caught up with Amos and
handcuffed him. At that time, a handgun fell from Amos’s
pocket, a firearm he was not permitted to carry due to his pre-
vious conviction of a felony punishable by a term of imprison-
ment exceeding one year.
        Amos was charged with one count of possession of a
firearm by a felon under 18 U.S.C. § 922(g). He filed a motion
to suppress the gun and argued that he was seized pre-flight
without reasonable suspicion. After an evidentiary hearing, the
District Court denied the motion, finding no pre-flight seizure
occurred. Amos then pleaded guilty pursuant to a plea agree-
ment. 2
       At sentencing, the parties disputed the applicability of a
sentencing enhancement under Sentencing Guidelines
§ 2K2.1(a)(4)(A) which applies to defendants previously con-
victed of a felony “crime of violence.” The Government argued
that Amos’s 2008 Pennsylvania state conviction for aggravated

2
  Amos’s plea agreement waived appellate and collateral chal-
lenges with only a few exceptions, including that he could chal-
lenge the denial of his motion to suppress and he could raise
ineffective assistance of counsel. As such, Amos originally
couched his crime of violence argument in ineffective assis-
tance of counsel. However, the Government agreed to waive
the appellate waiver so we can exercise ordinary review of the
guideline challenge. Amos confirms this, explaining that the
ineffective assistance claim is no longer necessary, and the
Court can review the issue squarely.




                               4
assault, a second-degree felony, qualified as a predicate crime
of violence.
       The state court records did not identify the specific
second-degree subsection of the aggravated assault statute, 18
Pa. Cons. Stat. § 2702(a)(3)–(7), under which Amos was con-
victed. Accordingly, the Government had to prove that all five
subsections qualified as a crime of violence. The District Court
found that the Government met its burden and applied the en-
hancement. This resulted in a base offense level of twenty,
from which the court deducted two levels for acceptance of re-
sponsibility, making it eighteen. Combined with Amos’s crim-
inal history category of six, he was subject to an advisory
Guidelines’ range of 57 to 71 months’ imprisonment. Without
the enhancement, Amos’s range would have been 30 to 37
months’ imprisonment. The court imposed a sentence of 62
months’ imprisonment followed by three years of supervised
release. Amos timely appealed. 3
           II.   Motion to Suppress
       We review the District Court’s denial of a motion to
suppress for clear error as to the underlying factual findings
and exercise plenary review over questions of law. United
States v. Coward, 296 F.3d 176, 179 (3d Cir. 2002).




3
 The District Court had jurisdiction under 18 U.S.C. § 3231
and we have jurisdiction pursuant to 28 U.S.C. § 1291 and 18
U.S.C. § 3742.




                               5
                  A. The Fourth Amendment Suppression
                     Analysis
        The Fourth Amendment prohibits “unreasonable
searches and seizures….” U.S. Const. amend. IV. Unless an
exception applies, a seizure “must be effectuated with a war-
rant based on probable cause” in order to be reasonable under
the Fourth Amendment. United States v. Robertson, 305 F.3d
164, 167 (3d Cir. 2002). One such exception to the warrant re-
quirement was established in Terry v. Ohio, 392 U.S. 1 (1968).
When a police officer has a “reasonable, articulable suspicion
that criminal activity is afoot,” he may conduct a brief, inves-
tigatory stop without a warrant, i.e., a “Terry stop.” Illinois v.
Wardlow, 528 U.S. 119, 123 (2000). “[R]easonable suspicion
is a less demanding standard than probable cause and requires
a showing considerably less than preponderance of the evi-
dence.” Id. However, an officer must “articulate more than an
‘inchoate and unparticularized suspicion or “hunch”’ of crimi-
nal activity” to establish reasonable suspicion. Id. at 124 (quot-
ing Terry, 392 U.S. at 27). If a Terry stop is conducted without
reasonable suspicion of criminal activity, any evidence ob-
tained must be suppressed as “fruit of the poisonous tree.”
Wong Sun v. United States, 371 U.S. 471, 487–88 (1963) (in-
ternal quotation marks omitted).
       Reasonable suspicion is evaluated at the moment of a
seizure, so the first step in a suppression analysis is to deter-
mine when the seizure occurred. United States v. Smith, 575
F.3d 308, 312 (3d Cir. 2009). When determining whether a sei-
zure occurred, we must consider “all the circumstances sur-
rounding the encounter.” Id. (quoting Florida v. Bostick, 501
U.S. 429, 439 (1991)). If a seizure occurred pre-flight, then the




                                6
flight “plays no role in the reasonable suspicion analysis.”
United States v. Brown, 448 F.3d 239, 245 (3d Cir. 2006).
        A seizure can occur in two ways: 1) “a laying on of
hands or application of physical force to restrain movement,
even when it is ultimately unsuccessful,” or 2) “submission to
a ‘show of authority.’” Id. (quoting California v. Hodari D.,
499 U.S. 621, 626 (1991)). There is no dispute that the police
officers did not touch Amos before he tried to flee, so a seizure
could only have occurred pre-flight if Amos 1) submitted 2) to
a show of authority. The absence of either element is fatal to
his appeal.
                  B. The Police Officers Showed Authority
                     Because No Reasonable Person in
                     Amos’s Position Would Have Felt Free to
                     Leave
        We first address whether the police officers showed au-
thority when they encountered Amos in the alleyway. The Dis-
trict Court found no show of authority by the officers because
they did not communicate to Amos that he was not free to
leave. The court relied on the facts that the officers did not ac-
tivate the police car’s lights or sirens, brandish their weapons,
block Amos’s path, come into contact with Amos, or make any
threats or intimidating movements.
        An objective test determines whether there has been a
show of authority; we must ask whether a reasonable person
would have believed he was not free to leave based on the of-
ficer’s words and actions. Hodari D, 499 U.S. at 628. Factors
such as “the threatening presence of several officers, the dis-
play of a weapon by an officer, some physical touching of the




                                7
person of the citizen, or the use of language or tone of voice
indicating that compliance with the officer’s request might be
compelled” may indicate a show of authority occurred. United
States v. Mendenhall, 446 U.S. 544, 554 (1980) (plurality opin-
ion).
       The Government hardly protests that the officers did not
show authority. See Appellee Br. 12 (“In this matter, whether
or not there was a show of authority in the officer’s command
to stop, there is no question that Amos did not comply before
running on foot.”); see also id. at 15 (“Assuming Officer
Lemos’ single request that the defendant stop and raise hands
was a show of authority, the defendant never submitted to it.”).
In a footnote, the Government notes that the District Court did
not find a show of authority and says, “that conclusion alone
resolves this case.” Id. at 16 n.3.
       Amos argues that the police officers’ show of authority
was strong. He asserts that late at night, he was pursued by two
uniformed officers in a marked patrol car. The officers
emerged the wrong way out of a one-way street and parked in
the mouth of the alleyway from where Amos was emerging.
He argues that based on our caselaw, the officers showed au-
thority because no reasonable person would have felt free to
leave.
       We agree with Amos that the officers displayed a show
of authority. Under the circumstances of the encounter between
Amos and the officers, a reasonable person would have be-
lieved he was not free to leave. While the District Court is right
that the officers did not brandish their weapons or make any
threats, the record shows that at 2:00 a.m. a marked police car




                                8
parked against the flow of traffic midway in the entrance to the
alleyway from where Amos was walking. The car was parked
in Amos’s direct forward path and inside were two uniformed
officers. One officer immediately got out and approached
Amos, commanding him to stop and show his hands.
        Additionally, the record indicates the officers arrived in
a hurried manner as they drove the wrong way against traffic
with their lights on initially to get in Amos’s path. Similar facts
were presented in United States v. Lowe, 791 F.3d 424 (3d Cir.
2015). In Lowe, multiple marked police cars, which used their
lights and sirens en route to their destination, arrived at a resi-
dence in the middle of the night. Id. at 428. Multiple uniformed
officers approached the defendant and commanded that he
show his hands. Id. at 431–32. Based on the record, we found
that “the officers’ approach constituted a show of authority, as
a reasonable person in Lowe’s position would not have felt free
to decline the interaction or leave.” Id. at 432.
       We think that under the circumstances presented to
Amos, a reasonable individual would have understood that the
officers were exercising control and showing authority. No rea-
sonable person who is commanded to stop and show their
hands in the middle of the night by uniformed officers with a
marked police car would feel free to ignore the command and
walk away. We have previously found a “clear show of author-
ity” when an officer informed two robbery suspects that the
“victim was being brought over to identify them as possible
suspects and, if they were not identified, they would be free to
go—necessarily implying that they were not free to leave.”
Brown, 448 F.3d at 245. We went on to say that the officer’s
demand that the suspects submit to a pat-down “would have




                                9
conveyed … to a reasonable person” that “he was being or-
dered to restrict his movement.” Id. (quoting Hodari D., 499
U.S. at 628). And we have assumed a show of authority when
officers instruct a defendant to place his hands on their vehicle.
See Smith, 575 F.3d at 314. Today, we confirm that assump-
tion. When a uniformed officer approaches an individual in the
middle of the night in a marked police car and commands that
person to stop and raise his or her hands, that is a show of au-
thority.
                  C. Amos Did Not Submit to the Officer’s
                     Show of Authority
       We next consider submission to authority. Although
Amos is correct that the officers displayed a show of authority,
he must have also submitted to that display in order to have
been seized. “A police officer may make a seizure by a show
of authority and without the use of physical force, but there is
no seizure without actual submission; otherwise, there is at
most an attempted seizure, so far as the Fourth Amendment is
concerned.” Brendlin v. California, 551 U.S. 249, 254 (2007).
       When Officer Lemos told Amos to stop and put his
hands up, Amos placed his hands at a “halfway point” and
stopped for “[m]aybe a second” before he ran. App’x 89, 91.
The District Court found that Amos did not submit to the of-
ficers when he fled before his hands were all the way up.
       When determining whether an individual has submitted
to a show of authority, we consider both the nature of the show
of authority and the individual’s conduct at that moment. See
Lowe, 791 F.3d at 430. “Thus, while ‘a fleeing man is not
seized until he is physically overpowered, … one sitting in a




                               10
chair may submit to authority by not getting up to run away.’”
Id. at 431 (quoting Brendlin, 551 U.S. at 262).
        Amos focuses on three cases to argue that he submitted
to the officers’ authority, but his reliance on those cases is mis-
placed. Amos asserts that in Lowe, the defendant “submitted
even though he took several steps backward into a fence, and
even though he failed to comply with the officers’ commands
to show his hands.” Appellant Br. 19. But we explained that
Lowe stayed put where he was when the officers converged
and was described by officers as “frozen” and “shocked.”
Lowe, 791 F.3d at 433. We explicitly held that “when a station-
ary suspect reacts to a show of authority by not fleeing, making
no threatening movement or gesture, and remaining stationary,
he has submitted under the Fourth Amendment and a seizure
has been effectuated.” Id. at 434 (emphasis added). Amos was
not a stationary suspect and did not remain stationary. In fact,
we distinguished such a circumstance in Lowe when we
pointed out that “[o]ther courts have found no submission
when a suspect already in motion refuses to stop when ap-
proached by an officer.” Id. at 433 (collecting cases).
       Amos also relies on Brown, which bears closer resem-
blance to the situation at hand but just misses the mark. As de-
scribed above, the officer in Brown demanded that robbery sus-
pects submit to a pat-down. 448 F.3d at 245. We explained that
one suspect “clearly submitted” when he “turned to face the
police car and placed his hands on the vehicle in response to
[the officer’s] demand.” Id. at 246. Amos points out that we
said that “conclusion is not meaningfully contradicted by [the
officer’s] testimony that Brown had begun to move his hands
to the vehicle, but did not complete the action.” Id. True




                                11
enough, but we also explained that “Brown demonstrated more
than ‘momentary compliance’” with the officer’s demands and
distinguished a situation where a defendant did not. Id. (distin-
guishing United States v. Valentine, 232 F.3d 350, 359 (3d Cir.
2000)).
        For its seizure analysis, we found Brown similar to
United States v. Coggins, 986 F.2d 651 (3d Cir. 1993), which
Amos also relies on. Coggins, who was sitting down, attempted
to terminate an encounter with a Drug Enforcement Admin-
istration agent at an airport. Id. at 652. When he stood up and
said he had to use the bathroom, the agent told him to wait. Id.
Coggins then sat back down. Id. We explained that Coggins
submitted to the agent’s authority by sitting down. Id. at 654.
He made a clear request to leave, the agent ordered him to stay,
and Coggins complied with the order by sitting down. Id. Such
a clear affirmative submission is missing from Amos’s encoun-
ter with the officers.
        Instead, Amos’s actions were like those in Valentine
and Smith, where we found no submission and thus no seizure.
In Valentine, police officers approached a man who matched
the description of a tip for a gunman and told him to place his
hands on their police car. 232 F.3d at 352–53. The man re-
sponded, “Who, me?” and then ran toward the officers before
being grabbed and wrestled to the ground. Id. at 353. Although
we found that, under the totality of the circumstances, the of-
ficers had reasonable suspicion to stop and frisk Valentine, we
went on to address whether a seizure occurred prior to his at-
tempt to flee. Id. at 357–59. Valentine argued that when the
officer ordered him to place his hands on the car, he momen-
tarily complied with the order when he stopped and gave his




                               12
name, which in turn triggered a seizure. Id. at 359. But we ex-
plained that Valentine’s momentary “compliance” was not a
submission to authority. Id. “Even if Valentine paused for a
few moments and gave his name, he did not submit in any re-
alistic sense to the officers’ show of authority, and therefore
there was no seizure until [the officer] grabbed him.” Id.
        In Smith, officers were patrolling during the night when
they encountered Smith on the street and asked him to talk. 575
F.3d at 311. He briefly complied, walking toward the officers’
car and answering questions about his identification and desti-
nation. Id. He then provided nonresponsive answers to contin-
ued questioning, so one of the officers asked him to place his
hands on the hood of the car. Id. Smith took two steps toward
the vehicle, at which point the officers opened their car doors
and Smith ran. Id. We relied on Valentine for the finding that
“momentary compliance was not enough to trigger a seizure”
and found that Smith’s two steps towards the officers’ vehicle
did not indicate submission to the show of authority. Id. at 315–
16. “[S]ubmission to authority under Hodari D., ‘requires at
minimum, that a suspect manifest compliance with police or-
ders.’” Id. at 316 (quoting United States v. Waterman, 569 F.3d
144, 146 n.3 (3d Cir. 2009)). Smith’s two steps and non-
responsive answers did not represent manifest compliance. Id.
We distinguished Brown by explaining that the defendant there
submitted to the officer’s orders to stay put prior to turning to
face the car, and thus his submission was manifested at that
point. Id. at 315.
       Amos’s situation is most analogous to Smith. Id. at 311.
Like the officer in Smith who directed the suspect to put his
hands on the vehicle, the officer here told Amos to stop and put




                               13
his hands up. Just as Smith did not comply by taking two steps
forward before running, Amos’s brief hesitation and raising of
his hands halfway before running was not “manifest compli-
ance.” Id. at 316. Similarly, even though Valentine paused for
a few moments and gave his name, he did not submit in a real-
istic sense to the officers’ show of authority. Valentine, 232
F.3d at 359. The same can be said for Amos.
       We conclude that as in Valentine and Smith, Amos’s ac-
tions were not a submission to authority. In the cases where we
found such a submission, the compliance was more definite
than Amos’s display. Amos’s one- or two-second pause and
halfway hand raise is clearly different than affirmatively sitting
down after being told to or complying with an officer’s order
for more than a moment. Instead, it was more akin to the “ex-
traordinarily brief” compliance we have recognized as insuffi-
cient submission to authority. See United States v. Hester, 910
F.3d 78, 86 (3d Cir. 2018) (referring to Valentine and Smith).
        Accordingly, because submission “would seem to re-
quire something more than a momentary pause,” Amos’s brief
pause and halfway hand raise was not a submission to the of-
ficers’ show of authority. Waterman, 569 F.3d at 146. As
Amos did not submit to the show of authority, no seizure oc-
curred at that time. Thus, reasonable suspicion is not evaluated
at that point. See Smith, 575 F.3d at 312.
       When Amos ran and attempted to flee, the officers
caught him and put him into handcuffs—a classic seizure. See
Hodari D., 499 U.S. at 624. Amos concedes that if he was not
seized until after he fled, then there was reasonable suspicion




                               14
at that point to seize him based on his headlong flight. 4 See
Wardlow, 528 U.S. at 124; Appellant Br. 6.
       In sum, Amos’s one- or two-second pause and halfway
hand raise did not manifest submission to the officer’s show of
authority. Because Amos did not submit to the show of author-
ity and was not seized until the officers put him in handcuffs
based on reasonable suspicion, the District Court did not err in
denying his motion to suppress.
           III.   Crime of Violence Sentencing Enhancement
       We next consider Amos’s challenge to his sentence. He
has challenged only one aspect of his sentencing: the crime of
violence enhancement. Whether an offense qualifies as a crime
of violence is a question of law subject to plenary review. See
United States v. Wilson, 880 F.3d 80, 83 (3d Cir. 2018).
                  A. The Elements of Force Clause
        The “crime of violence” enhancement to the firearm
guideline applies where “the defendant committed any part of
the instant offense subsequent to sustaining one felony convic-
tion of either a crime of violence or a controlled substance of-
fense.” U.S.S.G. § 2K2.1(a)(4)(A). A crime of violence is any
federal or state offense, punishable by imprisonment for more
than a year, that “(1) has as an element the use, attempted use,
or threatened use of physical force against the person of

4
 Because Amos was not seized until he was grabbed and hand-
cuffed by the officers, we need not decide whether the officers
had reasonable suspicion at an earlier time based on the anon-
ymous tip.




                              15
another, or (2) is murder, voluntary manslaughter, kidnapping,
aggravated assault, a forcible sex offense, robbery, arson, ex-
tortion, or the use or unlawful possession of a firearm described
in 26 U.S.C. § 5845(a) or explosive material as defined in 18
U.S.C. § 841(c).” U.S.S.G. § 4B1.2(a). There is no assertion
by the parties that subsection two applies to Amos, so our in-
quiry is confined to subsection one, the so-called elements of
force clause. “Physical force” in the elements of force clause
“means violent force—that is, force capable of causing physi-
cal pain or injury to another person.” Johnson v. United States,
559 U.S. 133, 138–40 (2010). 5
                  B. The Modified Categorical Approach
       When determining whether a conviction is a crime of
violence, we must use the categorical approach. This requires
us to “compare the elements of the statute under which the de-
fendant was convicted to the [G]uidelines’ definition of crime
of violence.” United States v. Wilson, 880 F.3d 80, 83 (3d Cir.
2018) (citing United States v. Chapman, 866 F.3d 129, 133 (3d
Cir. 2017)). When conducting the categorical approach analy-
sis under the elements of force clause, we ask whether “the use,
attempted use, or threatened use of physical force against an-
other person is categorically an element of the offense of

5
  Johnson addressed whether an offense constituted a “violent
felony” under the Armed Career Criminal Act, 18 U.S.C.
§ 924(e). Because the definition of crime of violence bears
“substantial similarity” to the definition of violent felony in the
ACCA, we apply authority interpreting one definition to the
other. See United States v. Marrero, 743 F.3d 389, 394 n.2 (3d
Cir. 2014) (citation omitted).




                                16
conviction.” United States v. Ramos, 892 F.3d 599, 606 (3d
Cir. 2018). As stated above, physical force “means vio-
lent force—that is, force capable of causing physical pain or
injury to another person.” Johnson, 559 U.S. at 140. “Accord-
ingly, a crime is a violent one under the elements clause so long
as it has an element that can be satisfied only through the use,
threatened use, or attempted use of force against another per-
son that is capable of causing that person physical pain or in-
jury.” Ramos, 892 F.3d at 611. That is true regardless of
whether an offender could be convicted under the statute for
applying force directly or indirectly. Chapman, 866 F.3d at
132–33.
        Thus, if the state statute Amos was convicted under has
an element of violent force capable of causing physical pain or
injury, “then the statute proscribes a predicate crime of vio-
lence within the meaning of the Guidelines.” Ramos, 892 F.3d
at 606. But if the statute does not have such an element, it
“sweeps more broadly” and the state conviction is not a predi-
cate offense for the crime of violence sentencing enhancement.
See United States v. Brown, 765 F.3d 185, 189 (3d Cir. 2014)
(citation omitted).
         A court “may ‘look only to the statutory definitions’—
i.e., the elements—of a defendant’s prior offenses, and not ‘to
the particular facts underlying those convictions.’” Id. (quoting
Descamps v. United States, 570 U.S. 254, 261 (2013) (empha-
sis in original)). This approach requires that a court both “ig-
nore the actual manner in which the defendant committed the
prior offense” and “presume that the defendant did so by en-
gaging in no more than ‘the minimum conduct criminalized by




                               17
the state statute.’” Ramos, 892 F.3d at 606 (quoting Moncrieffe
v. Holder, 569 U.S. 184, 191 (2013)).
       However, when a defendant was convicted under a “di-
visible” statute that defines multiple crimes, we apply the
“modified categorical approach.” United States v. Abdullah,
905 F.3d 739, 744 (3d Cir. 2018) (citation omitted). This ap-
proach allows us to look beyond the statute of conviction and
identify the specific statutory provision under which the de-
fendant was previously convicted. Id. We may look to so-
called Shepard documents, including the charging document,
written plea agreement, and plea colloquy transcript. Id.; see
Shepard v. United States, 544 U.S. 13, 16 (2005). If a specific
provision is identified, the categorical approach is applied to
that one provision. Abdullah, 905 F.3d at 744. If the records
are unclear, the Government must “show that all of the stat-
ute’s offenses [meet] the federal definition” of crime of vio-
lence. Pereida v. Wilkinson, 141 S. Ct. 754, 766 (2021) (em-
phasis in original).
                 C. The Pennsylvania Second-Degree Aggra-
                    vated Assault Statute
        The state court records show that Amos was charged
with and entered a guilty plea to aggravated assault as a felony
in the second-degree generally. In 2008, when Amos commit-
ted the crime, the Pennsylvania aggravated assault statute in-
cluded seven subsections enumerating an aggravated assault.
Subsections one and two are felonies in the first-degree,
whereas subsections three through seven are felonies in the
second-degree. See 18 Pa. Cons. Stat. § 2702(b).
       A person is guilty of aggravated assault if he:




                              18
(3) attempts to cause or intentionally or know-
ingly causes bodily injury to any of the officers,
agents, employees or other persons enumerated
in subsection (c), in the performance of duty;
(4) attempts to cause or intentionally or know-
ingly causes bodily injury to another with a
deadly weapon;
(5) attempts to cause or intentionally or know-
ingly causes bodily injury to a teaching staff
member, school board member or other em-
ployee, including a student employee, of any el-
ementary or secondary publicly-funded educa-
tional institution, any elementary or secondary
private school licensed by the Department of Ed-
ucation or any elementary or secondary paro-
chial school while acting in the scope of his or
her employment or because of his or her employ-
ment relationship to the school;
(6) attempts by physical menace to put any of the
officers, agents, employees or other persons enu-
merated in subsection (c), while in the perfor-
mance of duty, in fear of imminent serious bodily
injury; or
(7) uses tear or noxious gas as defined in section
2708(b) (relating to use of tear or noxious gas in
labor disputes) or uses an electric or electronic
incapacitation device against any officer, em-
ployee or other person enumerated in subsection
(c) while acting in the scope of his employment.




                       19
Id. § 2702(a)(3)–(7).
        At sentencing, the Government argued that Amos’s
2008 Pennsylvania state aggravated assault conviction quali-
fied as a predicate crime of violence. Under Ramos, the modi-
fied categorial approach applies because the Pennsylvania ag-
gravated assault statute is divisible. See 892 F.3d at 607–10.
Accordingly, the Government provided the District Court with
the state court Certified Records of Conviction. The Govern-
ment conceded that the Shepard documents do not indicate
what subsection of Section 2702(a) Amos was convicted un-
der, except to say it was a felony in the second-degree as listed
on the written guilty plea colloquy. The Government argued
the crime of violence enhancement applied because each of the
possible five subsections is a crime of violence. Amos’s trial
counsel confined his argument in opposition to subsection six.
See App’x 240 (“Your Honor, my argument is limited to § 6.”).
The court agreed with the Government and applied the sentenc-
ing enhancement, which resulted in a sentence of 62 months’
imprisonment followed by three years of supervised release.
                  D. 18 Pa. Con. Stat. § 2702(a)(3) Is Not a
                     Crime of Violence 6
       As previously stated, the Government must show that
all subsections of Pennsylvania’s aggravated assault statute



6
  Because Amos succeeds under subsection three, we need not
address whether the other subsections of aggravated assault in
the second-degree are crimes of violence. Likewise, we need
not address whether the Government waived its right to argue




                               20
meet the federal definition of crime of violence. See Pereida,
141 S. Ct. at 766. If the Government is unable to do so on even
one subsection, then Amos prevails in his argument that his
conviction under the statute is not a crime of violence, and he
is thus not subject to the sentencing enhancement.
        We start and end our analysis by applying our recent
decision in United States v. Jenkins, 68 F.4th 148 (3d Cir.
2023). In Jenkins, we addressed whether 18 Pa. Cons. Stat.
§ 2702(a)(3)—one of the exact subsections at issue here—is a
violent felony under the ACCA. We relied on the Pennsylvania
Supreme Court’s decision United States v. Harris, 289 A.3d
1060 (Pa. 2023), to find “that Section 2702(a)(3) can at least
be violated by a failure to act, so it is not a violent felony.”
Jenkins, 68 F.4th at 152. Like the subsection addressed in Har-
ris, the statutory language in Section 2702(a)(3) makes no
mention of force and there is no reference “to the manner by
which an injury must be inflicted.” Id. at 153 (quoting Harris,
289 A.3d at 1070).
       That affirmative holding controls here because of the
“substantial similarity” between the definitions of violent fel-
ony in the ACCA and crime of violence in the Guidelines. See
Marrero, 743 F.3d at 394 n.2 (citation omitted). The Shepard
documents do not rule out that Amos was convicted under sub-
section three of the Pennsylvania aggravated assault statute,
and under Jenkins, subsection three is not a crime a violence.
Accordingly, Amos must be resentenced.


that Amos was not convicted under subsection seven and
whether a closed record on remand is necessary.




                              21
          IV.    Conclusion
        For the foregoing reasons, we will affirm the District
Court’s order denying Amos’s motion to suppress. Addition-
ally, because Section 2702(a)(3) is not a crime of violence, we
vacate Amos’s sentence and remand for resentencing con-
sistent with this opinion.




                              22

```

---

## GROUP: _overhaul2/lake/cases/United States v. Anchondo.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Anchondo"
type: case
citation: "156 F.3d 1043 (1998)"
parallel_cite: ""
neutral_cite: "1998 U.S. App. LEXIS 21392; 1998 WL 559355"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 1998
date_decided: 1998-09-01
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Anchondo
  varies_by_point: false
  scope_note: "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/758111/united-states-v-erick-anchondo/"
  cluster_id: 758111
  opinion_id: 758111
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Chimel v. California]]", "[[Rawlings v. Kentucky]]", "[[Arizona v. Gant]]"]
aliases: ["United States v. Erick Anchondo"]
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile"]
holding: "ACTUAL holding: cocaine found on the defendant's body was the product of a lawful SEARCH INCIDENT TO ARREST, not the automobile…"
lake:
  record_id: United States v. Anchondo
  status: under_review
  projected_at: 2026-07-06
---

# United States v. Anchondo

*156 F.3d 1043 (10th Cir. 1998)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had probable cause to arrest Anchondo in connection with a drug transaction. They searched his person and found cocaine on his body, and the arrest followed shortly after the search. He moved to suppress the cocaine, and the search's validity turned on the search-incident-to-arrest exception rather than on any search of an automobile.

## Issue
Whether cocaine found on the defendant's person was lawfully obtained as a [[Search Incident to Arrest|search incident to arrest]] where the search preceded, rather than followed, the formal arrest.

## Rule
A search may validly precede the arrest it is incident to: "A warrantless search preceding an arrest is a legitimate 'search incident to arrest' as long as (1) a legitimate basis for the arrest existed before the search, and (2) the arrest followed shortly after the search." — 156 F.3d at 1045. ^pin-1045

Applying that rule, the court held that "the discovery of cocaine on the defendant's person was the result of a lawful search incident to arrest." — *Id.* at 1046. ^pin-1046

## Application
Because the officers had a legitimate basis to arrest Anchondo before they searched him, and the arrest followed shortly after, the search of his person was a lawful [[Search Incident to Arrest|search incident to arrest]] even though it came first; the cocaine found on his body was admissible. The court resolved the case on the search-incident-to-arrest exception — not the automobile exception — making *Anchondo* a frequently miscategorized authority.

## Conclusion
The search of Anchondo's person was a lawful [[Search Incident to Arrest|search incident to arrest]] and the cocaine was admissible; the conviction was affirmed. A [[Search Incident to Arrest|search incident to arrest]] may precede the arrest when probable cause already exists and the arrest follows promptly.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Anchondo* applies the search-incident-to-arrest doctrine of [[Chimel v. California]] and the search-may-precede-arrest principle of [[Rawlings v. Kentucky]]. It is listed here on the **Automobile Exception** page as a cautionary cross-reference: despite frequent miscitation, its holding rests on [[Search Incident to Arrest|search incident to arrest]], not the automobile exception (compare [[Arizona v. Gant]] on vehicle [[Search Incident to Arrest|searches incident to arrest]]).

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *United States v. Anchondo*, 156 F.3d 1043 (10th Cir. 1998) — https://www.courtlistener.com/opinion/758111/united-states-v-erick-anchondo/ — pinpoints: 1045, 1046.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "32878e701b5a987c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Anchondo"}, "payload": {"all": [{"cite": "156 F.3d 1043", "page": "1043", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "156"}, {"cite": "1998 U.S. App. LEXIS 21392", "page": "21392", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}, {"cite": "1998 WL 559355", "page": "559355", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1998"}], "display": "156 F.3d 1043", "official": {"cite": "156 F.3d 1043", "page": "1043", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "156"}, "official_selection_present": true, "record_id": "United States v. Anchondo"}}
{"assertion_id": "4a3d47f9fead8c04", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1045", "record_id": "United States v. Anchondo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1045", "pinpoint_status": "slip-only", "quote": "--- # United States v. Anchondo *156 F.3d 1043 (10th Cir. 1998)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had probable cause to arrest Anchondo in connection with a drug transaction. They searched his person and found cocaine on his body, and the arrest followed shortly after the search. He moved to suppress the cocaine, and the search's validity turned on the search-incident-to-arrest exception rather than on any search of an automobile. ## Issue Whether cocaine found on the defendant's person was lawfully obtained as a search incident to arrest where the search preceded, rather than followed, the formal arrest. ## Rule A search may validly precede the arrest it is incident to:", "quote_fidelity": "mismatch", "record_id": "United States v. Anchondo", "star_marker": null}}
{"assertion_id": "fae1ea5c39bbb874", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1046", "record_id": "United States v. Anchondo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1046", "pinpoint_status": "slip-only", "quote": "the discovery of cocaine on the defendant's person was the result of a lawful search incident to arrest.", "quote_fidelity": "mismatch", "record_id": "United States v. Anchondo", "star_marker": null}}
{"assertion_id": "c0caad6b5be80414", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Anchondo"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Anchondo", "scope_note": "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest.", "varies_by_point": false}}
```

### lake record — United States v. Anchondo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Anchondo",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Erick Anchondo",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Erick ANCHONDO, Defendant-Appellant",
    "input_case_name": "United States v. Anchondo",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "1998-09-01",
    "year": 1998,
    "docket": null,
    "cluster_id": 758111,
    "lead_opinion_id": 758111,
    "sibling_ids": [
      758111
    ],
    "absolute_url": "/opinion/758111/united-states-v-erick-anchondo/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "156 F.3d 1043",
      "volume": "156",
      "reporter": "F.3d",
      "page": "1043",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. App. LEXIS 21392",
        "volume": "1998",
        "reporter": "U.S. App. LEXIS",
        "page": "21392",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 WL 559355",
        "volume": "1998",
        "reporter": "WL",
        "page": "559355",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "156 F.3d 1043",
        "volume": "156",
        "reporter": "F.3d",
        "page": "1043",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. App. LEXIS 21392",
        "volume": "1998",
        "reporter": "U.S. App. LEXIS",
        "page": "21392",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 WL 559355",
        "volume": "1998",
        "reporter": "WL",
        "page": "559355",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "156 F.3d 1043",
    "official_selection": {
      "court_class": "coa",
      "selected": "156 F.3d 1043",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1045",
      "page": null,
      "quote": "--- # United States v. Anchondo *156 F.3d 1043 (10th Cir. 1998)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had probable cause to arrest Anchondo in connection with a drug transaction. They searched his person and found cocaine on his body, and the arrest followed shortly after the search. He moved to suppress the cocaine, and the search's validity turned on the search-incident-to-arrest exception rather than on any search of an automobile. ## Issue Whether cocaine found on the defendant's person was lawfully obtained as a search incident to arrest where the search preceded, rather than followed, the formal arrest. ## Rule A search may validly precede the arrest it is incident to:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1046",
      "page": null,
      "quote": "the discovery of cocaine on the defendant's person was the result of a lawful search incident to arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Anchondo",
    "varies_by_point": false,
    "scope_note": "Good law. Often miscited as an automobile-exception case; its actual holding is search incident to arrest.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. McKissick",
          "cluster_id": 159263,
          "cite": [
            "204 F.3d 1282",
            "2000 Colo. J. C.A.R. 1203",
            "2000 U.S. App. LEXIS 2719",
            "2000 WL 216949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rosborough",
          "cluster_id": 164599,
          "cite": [
            "366 F.3d 1145",
            "2004 U.S. App. LEXIS 8651",
            "2004 WL 938459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Claudio Lugo, AKA Lugo Mano, Joel Logue-Lugo, Joel Lugo Luke",
          "cluster_id": 762490,
          "cite": [
            "170 F.3d 996",
            "51 Fed. R. Serv. 918",
            "1999 Colo. J. C.A.R. 1420",
            "1999 U.S. App. LEXIS 3948",
            "1999 WL 128901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Victor Manuel Torres-Castro",
          "cluster_id": 796200,
          "cite": [
            "470 F.3d 992",
            "2006 U.S. App. LEXIS 30420",
            "2006 WL 3598365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Anderson",
          "cluster_id": 2575795,
          "cite": [
            "281 Kan. 896",
            "136 P.3d 406",
            "2006 Kan. LEXIS 355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 2626323,
          "cite": [
            "108 P.3d 424",
            "141 Idaho 277",
            "2005 Ida. App. LEXIS 21"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sanchez",
          "cluster_id": 171758,
          "cite": [
            "555 F.3d 910",
            "2009 U.S. App. LEXIS 2474",
            "2009 WL 311267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cash",
          "cluster_id": 4870403,
          "cite": [
            "483 P.3d 1047"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitehead v. Com.",
          "cluster_id": 1058299,
          "cite": [
            "683 S.E.2d 299",
            "278 Va. 300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howards v. McLaughlin",
          "cluster_id": 212271,
          "cite": [
            "634 F.3d 1131",
            "2011 WL 856275"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conn",
          "cluster_id": 2582083,
          "cite": [
            "99 P.3d 1108",
            "278 Kan. 387",
            "2004 Kan. LEXIS 651"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Adam Chartier",
          "cluster_id": 2755606,
          "cite": [
            "772 F.3d 539",
            "2014 U.S. App. LEXIS 22323",
            "2014 WL 6678412"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. DAVID D. LEWIS",
          "cluster_id": 4281856,
          "cite": [
            "147 A.3d 236",
            "2016 D.C. App. LEXIS 369",
            "2016 WL 5539892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ojeda-Ramos",
          "cluster_id": 167867,
          "cite": [
            "455 F.3d 1178",
            "2006 U.S. App. LEXIS 19175",
            "2006 WL 2106801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mercado-Nava",
          "cluster_id": 2522106,
          "cite": [
            "486 F. Supp. 2d 1271",
            "2007 U.S. Dist. LEXIS 27486",
            "2007 WL 1098203"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 9484380,
          "cite": [
            "544 P.3d 820"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoskins v. Withers",
          "cluster_id": 9476608,
          "cite": [
            "92 F.4th 1279"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Chapman",
          "cluster_id": 4649632,
          "cite": [
            "2019 Ohio 3339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Romero",
          "cluster_id": 2471071,
          "cite": [
            "743 F. Supp. 2d 1281",
            "2010 U.S. Dist. LEXIS 91598",
            "2010 WL 3829636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Urdiales",
          "cluster_id": 2898078,
          "cite": [
            "2015 Ohio 3632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Torres-Castro",
          "cluster_id": 2397679,
          "cite": [
            "374 F. Supp. 2d 994",
            "2005 U.S. Dist. LEXIS 13810",
            "2005 WL 1554701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE v. COUSAN",
          "cluster_id": 4688823,
          "cite": [
            "447 P.3d 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whitehead v. Commonwealth",
          "cluster_id": 1062623,
          "cite": [
            "668 S.E.2d 435",
            "53 Va. App. 1",
            "2008 Va. App. LEXIS 503",
            "2008 WL 4862460"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dudsak",
          "cluster_id": 5289164,
          "cite": [
            "2021 Ohio 3632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE v. COUSAN",
          "cluster_id": 4689527,
          "cite": [
            "2019 OK CR 16",
            "447 P.3d 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Anchondo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(758111) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      },
      "lane2_top_cited": {
        "query": "cites:(758111)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9Mjg5ODA3OCZ0PW8mZD0yMDI2LTA3LTA2JnA9Mg%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28758111%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(758111)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(758111)",
    "indexed_citing_opinions": 33,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 758111,
        "count": 33,
        "count_source": "search"
      }
    ],
    "citation_count": 54,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-anchondo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIxOTY2NTkmcz0xMDYyNjIzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28758111%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 758111,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 349459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 518495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 563786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 658364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 758111,
        "cited_id": 736301,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:04:14Z",
    "date_modified": "2026-07-06T08:58:18Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:11:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:04:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Anchondo

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1122-15">
  TACHA, Circuit Judge.
 </author>
<p id="b1122-16">
  The defendant was indicted on one of count of possession with intent to distribute more than 500 grams of cocaine, in violation of <span class="citation no-link">21 U.S.C. § 841</span>(a)(1) and 841(b)(1)(B), and for aiding and abetting, in violation of <span class="citation no-link">18 U.S.C. § 2</span>. After the district court denied his motion to suppress evidence, the defendant entered a conditional guilty plea. He now appeals the denial of his motion to suppress. We take jurisdiction pursuant to <span class="citation no-link">28 U.S.C. § 1291</span> and affirm.
 </p>
<p id="b1122-17">
  1.
 </p>
<p id="b1122-18">
  On the evening of January 9, 1997, the defendant and his passenger, Felipe Garcia, stopped at a fixed checkpoint on Highway I-25, about 26 miles north of Las Cruces, New Mexico. While one border patrol agent asked the men routine questions, another agent walked a drug-sniffing canine around the exterior of the defendant’s sedan. During this canine inspection, the dog “alerted,” indicating the presence of illegal narcotics.
 </p>
<p id="b1122-19">
  Based on the canine alert, the agents asked the defendant to move his car to a secondary inspection area in order to confirm the canine’s alert. The defendant consented, moved the ear, and voluntarily exited the vehicle to allow a more thorough search of the car. The dog again alerted to the inside of the ear and the defendant and Garcia were moved to a nearby trailer.
 </p>
<p id="b1122-20">
  The border patrol agents were unable to locate the presence of any contraband in the vehicle. Agent Alvarado went to the trailer and asked the defendant and Garcia if they had any personal amounts of contraband in the vehicle. Defendant responded by stating: “[yjou’re not going to find anything in that vehicle.” Applt. App. at 11. At the suppression hearing, the defendant denied making this statement. In reviewing a motion to suppress, however, we consider the evidence in the light most favorable to the district court’s ruling,
  <em>
   see United States v. Elliott,
  </em>
  <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/#813" aria-description="Citation for case: United States v. Asta M. Elliott">107 F.3d 810, 813</a></span> (10th Cir.1997), md therefore must assume the statement was made.
 </p>
<p id="b1122-21">
  Agent Jose Alvarado then conducted a ‘pat and frisk” of the defendant’s outer cloth
  <span citation-index="1" class="star-pagination" label="1045"> 
   *1045
   </span>
  ing, which he described as “loose.” Applt. App. at 12. During the search, Agent Alvarado felt a hard object in the defendant’s waistline. The agent testified that he believed the object to be the butt of a semiautomatic handgun. The agent removed the object and found that it was a package of cocaine strapped to the defendant’s stomach. Four such packages were recovered from the defendant. Marijuana was found on the body of Garcia.
 </p>
<p id="b1123-5">
  II.
 </p>
<p id="b1123-6">
  When reviewing a district court’s grant or denial of a motion to suppress, we accept the district court’s factual findings unless they are clearly erroneous.
  <em>
   See Elliott,
  </em>
  <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/#813" aria-description="Citation for case: United States v. Asta M. Elliott">107 F.3d at 813</a></span>. The ultimate conclusion of whether the Fourth Amendment allowed a particular stop, however, is a legal determination that we review de novo.
  <em>
   See <span class="citation" data-id="736301"><a href="/opinion/736301/united-states-v-asta-m-elliott/" aria-description="Citation for case: United States v. Asta M. Elliott">id.</a></span>
  </em>
</p>
<p id="b1123-7">
  The defendant admits that the officers had probable cause to search the vehicle. He argues, however, that under the totality of the circumstances, the agents had no authority to search the defendant’s person for illegal narcotics. Furthermore, the defendant argues that the agents cannot even make the less onerous showing under
  <em>
   Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968), to justify a pat-down search of the defendant for weaponry. According to the defendant, if the agents had truly thought that the defendant posed a threat to their safety, they would have patted him down immediately after moving him to the secondary inspection area.
 </p>
<p id="b1123-8">
  We find it unnecessary to address the parties arguments on the application of
  <em>
   Terry v. Ohio
  </em>
  to this case because the agents were justified in conducting a full, warrant-less search of the defendant under these circumstances. The Fourth Amendment normally requires that law enforcement officers obtain a warrant, based on probable cause, before conducting a search.
  <em>
   See, e.g., New York v. Belton,
  </em>
  <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#457" aria-description="Citation for case: New York v. Belton">453 U.S. 454, 457</a></span>, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">101 S.Ct. 2860</a></span>, <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">69 L.Ed.2d 768</a></span> (1981). There are limited exceptions to that rule, however, one of which is that officers may conduct a war-rantless search of a person when it is incident to a lawful arrest of that person.
  <em>
   See Chimel v. California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U.S. 752, 762-63</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969). In order to be a legitimate “search incident to arrest,” the search need not take place after the arrest. A warrantless search preceding an arrest is a legitimate “search incident to arrest” as long as (1) a legitimate basis for the arrest existed before the search, and (2) the arrest followed shortly after the search.
  <em>
   See United States v. Rivera,
  </em>
  <span class="citation" data-id="518495"><a href="/opinion/518495/united-states-v-jesus-antonio-rivera/#1264" aria-description="Citation for case: United States v. Jesus Antonio Rivera">867 F.2d 1261, 1264</a></span> (10th Cir.1989);
  <em>
   cf. Rawlings v. Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#111" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98, 111</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">100 S.Ct. 2556</a></span>, <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">65 L.Ed.2d 633</a></span> (1980) (stating that where the arrest was justified before the search and the arrest “followed quickly on the heels of the challenged search of petitioner’s person, we do not believe it particularly important that the search preceded the arrest rather than vice versa.”). Whether or not the officer intended to actually arrest the defendant at the time of the search is immaterial to this two-part inquiry.
  <em>
   See United States v. Ricard,
  </em>
  <span class="citation" data-id="349459"><a href="/opinion/349459/united-states-v-raymond-ernest-ricard/#49" aria-description="Citation for case: United States v. Raymond Ernest Ricard">563 F.2d 45, 49</a></span> (2d Cir.1977).
 </p>
<p id="b1123-10">
  First, we inquire as to whether the agent had a legitimate basis to arrest the defendant at the time of the search. Arrests must be based on probable cause. Probable cause to arrest exists when an officer has learned of facts and circumstances through reasonably trustworthy information that would lead a reasonable person to believe that an offense has been or is being committed by the person arrested.
  <em>
   See United States v. Morgan,
  </em>
  <span class="citation" data-id="9481753"><a href="/opinion/563786/united-states-v-rodney-lee-morgan/#1568" aria-description="Citation for case: United States v. Rodney Lee Morgan">936 F.2d 1561, 1568</a></span> (10th Cir.1991). A canine alert provides the probable cause necessary for searches and seizures.
  <em>
   See United States v. Ludwig,
  </em>
  <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/#1527" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">10 F.3d 1523, 1527</a></span> (10th Cir.1993). Here, the canine alerted twice to the inside of the defendant’s car. Under
  <em>
   <span class="citation" data-id="658364"><a href="/opinion/658364/united-states-v-keith-rudolph-ludwig-national-association-of-criminal/" aria-description="Citation for case: United States v. Keith Rudolph Ludwig, National...">Ludwig</a></span>,
  </em>
  that provided the probable cause necessary to arrest the defendant. Even if the subsequent fruitless search of the car diminished the probability of contraband being in the car, it increased the chances that whatever the dog had alerted to was on the defendants’ bodies.
 </p>
<p id="b1123-11">
  Second, we determine whether the actual arrest was too remote from the search. Here, the arrest occurred immediately after
  <span citation-index="1" class="star-pagination" label="1046"> 
   *1046
   </span>
  the drugs were found on the defendant’s body.
 </p>
<p id="b1124-4">
  III.
 </p>
<p id="b1124-5">
  Given the above analysis, the discovery of cocaine on the defendant’s person was the result of a lawful search incident to arrest. We AFFIRM.
 </p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Arvizu.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Arvizu"
type: case
citation: "534 U.S. 266 (2002)"
parallel_cite: "122 S. Ct. 744; 151 L. Ed. 2d 740"
neutral_cite: 2002 U.S. LEXIS 490
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-01-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-01-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Arvizu
  varies_by_point: false
  scope_note: "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118474/united-states-v-arvizu/"
  cluster_id: 118474
  opinion_id: 118474
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[United States v. Cortez]]", "[[Illinois v. Wardlow]]", "[[Ornelas v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion"]
holding: "Reasonable suspicion is judged on the totality of the circumstances — the \"whole picture\" — and reviewing courts may NOT use a…"
lake:
  record_id: United States v. Arvizu
  status: verified
  projected_at: 2026-07-06
---

# United States v. Arvizu

*534 U.S. 266 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Border Patrol agent on a remote Arizona back road stopped a minivan after a sensor alert and a series of observations: the route avoided a checkpoint, the timing coincided with a shift change, the driver was rigid and avoided eye contact, and the children in the back waved in an oddly mechanical way as if instructed, with their knees raised over what turned out to be packages. The agent found over 100 pounds of marijuana. The Ninth Circuit had rejected several of the factors as individually innocent and reversed.

## Issue
Whether reasonable suspicion is assessed by examining each factor in isolation and discarding those susceptible to innocent explanation, or by evaluating the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
Reasonable suspicion is judged on the whole picture, not factor-by-factor: reviewing courts "must look at the 'totality of the circumstances' of each case to see whether the detaining officer has a 'particularized and objective basis' for suspecting legal wrongdoing." — 534 U.S. at 273. ^pin-273

The Court rejected the appellate court's approach of evaluating each factor in isolation: "*Terry*, however, precludes this sort of divide-and-conquer analysis." — *Id.* at 274. ^pin-274

## Application
Viewing the agent's observations together — and giving due weight to his specialized training and experience with the area's smuggling patterns — the combination of the avoided checkpoint, the suspicious timing, the driver's stiff demeanor, and the children's choreographed waving with their feet propped on the cargo supplied a particularized and objective basis to suspect criminal activity. The Ninth Circuit erred by dismissing factors individually; assessed as a whole, the stop was supported by reasonable suspicion.

## Conclusion
The stop was supported by reasonable suspicion; the Ninth Circuit's reversal was itself reversed. Courts must assess reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], not by isolating and discounting individual factors.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Arvizu* applies the reasonable-suspicion standard of [[Terry v. Ohio]] and the "whole picture"/"particularized and objective basis" formulation of [[United States v. Cortez]]; it parallels the totality approach approved in [[Illinois v. Wardlow]] and the deference to officer inferences in [[Ornelas v. United States]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Arvizu*, 534 U.S. 266 (2002) — https://www.courtlistener.com/opinion/118474/united-states-v-arvizu/ — pinpoints: 273, 274.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4a1b73e258ed254d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Arvizu"}, "payload": {"all": [{"cite": "534 U.S. 266", "page": "266", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "534"}, {"cite": "122 S. Ct. 744", "page": "744", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "151 L. Ed. 2d 740", "page": "740", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "151"}, {"cite": "2002 U.S. LEXIS 490", "page": "490", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}], "display": "534 U.S. 266", "official": {"cite": "534 U.S. 266", "page": "266", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "534"}, "official_selection_present": true, "record_id": "United States v. Arvizu"}}
{"assertion_id": "74e7174ebbe24c70", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-274", "record_id": "United States v. Arvizu"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-274", "pinpoint_status": "slip-only", "quote": "*Terry*, however, precludes this sort of divide-and-conquer analysis.", "quote_fidelity": "mismatch", "record_id": "United States v. Arvizu", "star_marker": null}}
{"assertion_id": "a45212117b83a79f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-273", "record_id": "United States v. Arvizu"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-273", "pinpoint_status": "slip-only", "quote": "--- # United States v. Arvizu *534 U.S. 266 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Border Patrol agent on a remote Arizona back road stopped a minivan after a sensor alert and a series of observations: the route avoided a checkpoint, the timing coincided with a shift change, the driver was rigid and avoided eye contact, and the children in the back waved in an oddly mechanical way as if instructed, with their knees raised over what turned out to be packages. The agent found over 100 pounds of marijuana. The Ninth Circuit had rejected several of the factors as individually innocent and reversed. ## Issue Whether reasonable suspicion is assessed by examining each factor in isolation and discarding those susceptible to innocent explanation, or by evaluating the totality of the circumstances. ## Rule Reasonable suspicion is judged on the whole picture, not factor-by-factor: reviewing courts", "quote_fidelity": "mismatch", "record_id": "United States v. Arvizu", "star_marker": null}}
{"assertion_id": "ed33aea56a1dea13", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Arvizu"}, "payload": {"as_of_content": "2002-01-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Arvizu", "scope_note": "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard.", "varies_by_point": false}}
```

### lake record — United States v. Arvizu

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Arvizu",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Arvizu",
    "case_name_short": "Arvizu",
    "case_name_full": "United States v. Arvizu",
    "input_case_name": "United States v. Arvizu",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-01-15",
    "year": 2002,
    "docket": null,
    "cluster_id": 118474,
    "lead_opinion_id": 118474,
    "sibling_ids": [
      118474,
      9434181,
      9434182
    ],
    "absolute_url": "/opinion/118474/united-states-v-arvizu/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "534 U.S. 266",
      "volume": "534",
      "reporter": "U.S.",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 744",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 740",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 490",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "490",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "534 U.S. 266",
        "volume": "534",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 744",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "151 L. Ed. 2d 740",
        "volume": "151",
        "reporter": "L. Ed. 2d",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 490",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "490",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "534 U.S. 266",
    "official_selection": {
      "court_class": "scotus",
      "selected": "534 U.S. 266",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-273",
      "page": null,
      "quote": "--- # United States v. Arvizu *534 U.S. 266 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Border Patrol agent on a remote Arizona back road stopped a minivan after a sensor alert and a series of observations: the route avoided a checkpoint, the timing coincided with a shift change, the driver was rigid and avoided eye contact, and the children in the back waved in an oddly mechanical way as if instructed, with their knees raised over what turned out to be packages. The agent found over 100 pounds of marijuana. The Ninth Circuit had rejected several of the factors as individually innocent and reversed. ## Issue Whether reasonable suspicion is assessed by examining each factor in isolation and discarding those susceptible to innocent explanation, or by evaluating the totality of the circumstances. ## Rule Reasonable suspicion is judged on the whole picture, not factor-by-factor: reviewing courts",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-274",
      "page": null,
      "quote": "*Terry*, however, precludes this sort of divide-and-conquer analysis.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-01-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Arvizu",
    "varies_by_point": false,
    "scope_note": "Good law; reaffirms the totality-of-the-circumstances reasonable-suspicion standard.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane1_negative"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shrestha v. Holder",
          "cluster_id": 1434187,
          "cite": [
            "590 F.3d 1034",
            "2010 U.S. App. LEXIS 138",
            "2010 WL 10982"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Madden v. State",
          "cluster_id": 1404569,
          "cite": [
            "242 S.W.3d 504",
            "2007 Tex. Crim. App. LEXIS 1802",
            "2007 WL 4404270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas L. Feathers Kathleen Feathers v. William Aey J.P. Donohue, City of Akron",
          "cluster_id": 780866,
          "cite": [
            "319 F.3d 843",
            "2003 U.S. App. LEXIS 2642",
            "2003 WL 296924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Branch",
          "cluster_id": 1026476,
          "cite": [
            "537 F.3d 328",
            "2008 U.S. App. LEXIS 17710",
            "2008 WL 3854500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eleuterio Lopez-Moreno, Also Known as Eleuterio Lopez",
          "cluster_id": 791593,
          "cite": [
            "420 F.3d 420",
            "2005 U.S. App. LEXIS 16564",
            "2005 WL 1864257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yul Darnell Givan, United States of America v. Wayne Torrence",
          "cluster_id": 780959,
          "cite": [
            "320 F.3d 452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pedro Luis Christopher Tinoco",
          "cluster_id": 75998,
          "cite": [
            "304 F.3d 1088",
            "59 Fed. R. Serv. 3d 1146",
            "2002 U.S. App. LEXIS 18479",
            "2002 WL 2013777"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brigham",
          "cluster_id": 35972,
          "cite": [
            "382 F.3d 500",
            "2004 WL 1854552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ricky A. Caruthers",
          "cluster_id": 795277,
          "cite": [
            "458 F.3d 459",
            "2006 U.S. App. LEXIS 20569",
            "2006 WL 2320942"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shepherd v. State",
          "cluster_id": 2190342,
          "cite": [
            "273 S.W.3d 681",
            "2008 Tex. Crim. App. LEXIS 855",
            "2008 WL 4149707"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pack",
          "cluster_id": 150729,
          "cite": [
            "612 F.3d 341",
            "2010 U.S. App. LEXIS 14562",
            "2010 WL 2777061"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Chase",
          "cluster_id": 1563033,
          "cite": [
            "960 A.2d 108",
            "599 Pa. 80",
            "2008 Pa. LEXIS 2180",
            "2008 WL 5002958"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James W. Smoak v. Eric Hall, David Bush Jeff Phann Tim McHood Brian Brock Jerry Andrews, Lieutenant",
          "cluster_id": 795446,
          "cite": [
            "460 F.3d 768",
            "2006 U.S. App. LEXIS 21661",
            "2006 WL 2455321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Arvizu:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118474 OR 9434181 OR 9434182) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcwMzcxMjAwMDAwJnM9OTMyODM0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118474+OR+9434181+OR+9434182%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(118474 OR 9434181 OR 9434182)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTQmcz03Nzk1NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118474+OR+9434181+OR+9434182%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118474 OR 9434181 OR 9434182)",
        "reviewed": 192,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 192,
        "triage_read": 1,
        "triage_snippet_classified": 191
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118474 OR 9434181 OR 9434182)",
    "indexed_citing_opinions": 2098,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118474,
        "count": 1638,
        "count_source": "search"
      },
      {
        "opinion_id": 9434181,
        "count": 489,
        "count_source": "search"
      },
      {
        "opinion_id": 9434182,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3942,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-arvizu.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTcwODgmcz0xMDYxODc3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118474+OR+9434181+OR+9434182%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118474,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118474,
        "cited_id": 771188,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:11:48Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:17:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:12:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Arvizu

```
<div>
<center><b><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U.S. 266</a></span> (2002)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
ARVIZU</h1></center>
<center>No. 00-1519.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued November 27, 2001.</center>
<center>Decided January 15, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*268</span> Rehnquist, C. J., delivered the opinion for a unanimous Court. Scalia, J., filed a concurring opinion, <i>post,</i> p. 278.</p>
<p><i>Austin C. Schlick</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Deputy Solicitor General Dreeben,</i> and <i>Deborah Watson.</i> </p>
<p><i>Victoria A. Brambl</i> argued the cause for respondent. With her on the brief was <i>Fredric F. Kay.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*268</span> Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>Respondent Ralph Arvizu was stopped by a border patrol agent while driving on an unpaved road in a remote area of southeastern Arizona. A search of his vehicle turned up more than 100 pounds of marijuana. The District Court for the District of Arizona denied respondent's motion to suppress, but the Court of Appeals for the Ninth Circuit reversed. In the course of its opinion, it categorized certain factors relied upon by the District Court as simply out of bounds in deciding whether there was "reasonable suspicion" for the stop. We hold that the Court of Appeals' methodology was contrary to our prior decisions and that it reached the wrong result in this case.</p>
<p>On an afternoon in January 1998, Agent Clinton Stoddard was working at a border patrol checkpoint along U. S. Highway 191 approximately 30 miles north of Douglas, Arizona. App. 22, 24. See Appendix, <i>infra</i> (containing a map of the area noting the location of the checkpoint and other points important to this case). Douglas has a population of about 13,000 and is situated on the United States-Mexico border in the southeastern part of the State. Only two highways lead north from Douglas. See App. 157. Highway 191 leads north to Interstate 10, which passes through Tucson and Phoenix. State Highway 80 heads northeast through less populated areas toward New Mexico, skirting south and east of the portion of the Coronado National Forest that lies approximately 20 miles northeast of Douglas.<sup>[1]</sup></p>
<p>The checkpoint is located at the intersection of 191 and Rucker Canyon Road, an unpaved east-west road that connects 191 and the Coronado National Forest. When the checkpoint is operational, border patrol agents stop the traffic <span class="star-pagination">*269</span> on 191 as part of a coordinated effort to stem the flow of illegal immigration and smuggling across the international border. See <i>id.,</i> at 20-21. Agents use roving patrols to apprehend smugglers trying to circumvent the checkpoint by taking the backroads, including those roads through the sparsely populated area between Douglas and the national forest. <i>Id.,</i> at 21-22, 26, 80. Magnetic sensors, or "intrusion devices," facilitate agents' efforts in patrolling these areas. See <i>id.,</i> at 25. Directionally sensitive, the sensors signal the passage of traffic that would be consistent with smuggling activities. <i>Ibid.;</i> Tr. of Oral Arg. 23-24.</p>
<p>Sensors are located along the only other northbound road from Douglas besides Highways 191 and 80: Leslie Canyon Road. Leslie Canyon Road runs roughly parallel to 191, about halfway between 191 and the border of the Coronado National Forest, and ends when it intersects Rucker Canyon Road. It is unpaved beyond the 10-mile stretch leading out of Douglas and is very rarely traveled except for use by local ranchers and forest service personnel. App. 26. Smugglers commonly try to avoid the 191 checkpoint by heading west on Rucker Canyon Road from Leslie Canyon Road and thence to Kuykendall Cutoff Road, a primitive dirt road that leads north approximately 12 miles east of 191. <i>Id.,</i> at 29-30. From there, they can gain access to Tucson and Phoenix. <i>Id.,</i> at 30.</p>
<p>Around 2:15 p.m., Stoddard received a report via Douglas radio that a Leslie Canyon Road sensor had been triggered. <i>Id.,</i> at 24. This was significant to Stoddard for two reasons. First, it suggested to him that a vehicle might be trying to circumvent the checkpoint. <i>Id.,</i> at 27. Second, the timing coincided with the point when agents begin heading back to the checkpoint for a shift change, which leaves the area unpatrolled. <i>Id.,</i> at 26, 47. Stoddard knew that alien smugglers did extensive scouting and seemed to be most active when agents were en route back to the checkpoint. Another border patrol agent told Stoddard that the same <span class="star-pagination">*270</span> sensor had gone off several weeks before and that he had apprehended a minivan using the same route and witnessed the occupants throwing bundles of marijuana out the door. <i>Id.,</i> at 27.</p>
<p>Stoddard drove eastbound on Rucker Canyon Road to investigate. As he did so, he received another radio report of sensor activity. <i>Id.,</i> at 29. It indicated that the vehicle that had triggered the first sensor was heading westbound on Rucker Canyon Road. He continued east, passing Kuykendall Cutoff Road. He saw the dust trail of an approaching vehicle about a half mile away. <i>Id.,</i> at 31. Stoddard had not seen any other vehicles and, based on the timing, believed that this was the one that had tripped the sensors. <i>Id.,</i> at 31-32. He pulled off to the side of the road at a slight slant so he could get a good look at the oncoming vehicle as it passed by. <i>Id.,</i> at 32.</p>
<p>It was a minivan, a type of automobile that Stoddard knew smugglers used. <i>Id.,</i> at 33. As it approached, it slowed dramatically, from about 50-55 to 25-30 miles per hour. <i>Id.,</i>  at 32, 57. He saw five occupants inside. An adult man was driving, an adult woman sat in the front passenger seat, and three children were in the back. <i>Id.,</i> at 33-34. The driver appeared stiff and his posture very rigid. He did not look at Stoddard and seemed to be trying to pretend that Stoddard was not there. <i>Id.,</i> at 33. Stoddard thought this suspicious because in his experience on patrol most persons look over and see what is going on, and in that area most drivers give border patrol agents a friendly wave. <i>Id.,</i> at 59. Stoddard noticed that the knees of the two children sitting in the very back seat were unusually high, as if their feet were propped up on some cargo on the floor. <i>Id.,</i> at 34.</p>
<p>At that point, Stoddard decided to get a closer look, so he began to follow the vehicle as it continued westbound on Rucker Canyon Road toward Kuykendall Cutoff Road. <i>Id.,</i>  at 34-35. Shortly thereafter, all of the children, though <span class="star-pagination">*271</span> still facing forward, put their hands up at the same time and began to wave at Stoddard in an abnormal pattern. <i>Id.,</i> at 35, 61. It looked to Stoddard as if the children were being instructed. Their odd waving continued on and off for about four to five minutes. <i>Id.,</i> at 35, 73.</p>
<p>Several hundred feet before the Kuykendall Cutoff Road intersection, the driver signaled that he would turn. <i>Id.,</i>  at 36. At one point, the driver turned the signal off, but just as he approached the intersection he put it back on and abruptly turned north onto Kuykendall. The turn was significant to Stoddard because it was made at the last place that would have allowed the minivan to avoid the checkpoint. <i>Id.,</i> at 37. Also, Kuykendall, though passable by a sedan or van, is rougher than either Rucker Canyon or Leslie Canyon Roads, and the normal traffic is four-wheel-drive vehicles. <i>Id.,</i> at 36, 63-64. Stoddard did not recognize the minivan as part of the local traffic agents encounter on patrol, <i>id.,</i>  at 37, and he did not think it likely that the minivan was going to or coming from a picnic outing. He was not aware of any picnic grounds on Turkey Creek, which could be reached by following Kuykendall Cutoff all the way up. <i>Id.,</i>  at 54. He knew of picnic grounds and a Boy Scout camp east of the intersection of Rucker Canyon and Leslie Canyon Roads, <i>id.,</i> at 31, 53, 54, but the minivan had turned west at that intersection. And he had never seen anyone picnicking or sightseeing near where the first sensor went off. <i>Id.,</i> at 53, 75.</p>
<p>Stoddard radioed for a registration check and learned that the minivan was registered to an address in Douglas that was four blocks north of the border in an area notorious for alien and narcotics smuggling. <i>Id.,</i> at 37-38, 66-67. After receiving the information, Stoddard decided to make a vehicle stop. <i>Id.,</i> at 38. He approached the driver and learned that his name was Ralph Arvizu. Stoddard asked if respondent would mind if he looked inside and searched <span class="star-pagination">*272</span> the vehicle. <i>Id.,</i> at 43. Respondent agreed, and Stoddard discovered marijuana in a black duffel bag under the feet of the two children in the back seat. <i>Id.,</i> at 45-46. Another bag containing marijuana was behind the rear seat. <i>Id.,</i>  at 46. In all, the van contained 128.85 pounds of marijuana, worth an estimated $99,080. Brief for United States 8.</p>
<p>Respondent was charged with possession with intent to distribute marijuana in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1) (1994 ed.). He moved to suppress the marijuana, arguing among other things that Stoddard did not have reasonable suspicion to stop the vehicle as required by the Fourth Amendment. After holding a hearing where Stoddard and respondent testified, the District Court for the District of Arizona ruled otherwise. App. to Pet. for Cert. 21a. It pointed to a number of the facts described above and noted particularly that any recreational areas north of Rucker Canyon would have been accessible from Douglas via 191 and another paved road, making it unnecessary to take a 40-to50-mile trip on dirt roads. <i><span class="citation no-link">Id.,</span></i> at 22a.</p>
<p>The Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d 1241</a></span> (2000). In its view, fact-specific weighing of circumstances or other multifactor tests introduced "a troubling degree of uncertainty and unpredictability" into the Fourth Amendment analysis. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu"><i>Id.,</i> at 1248</a></span> (internal quotation marks omitted). It therefore "attempt[ed] . . . to describe and clearly delimit the extent to which certain factors may be considered by law enforcement officers in making stops such as the stop involv[ing]" respondent. <i><span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/" aria-description="Citation for case: United States v. Ralph Arvizu">Ibid.</a></span></i>  After characterizing the District Court's analysis as relying on a list of 10 factors, the Court of Appeals proceeded to examine each in turn. It held that seven of the factors, including respondent's slowing down, his failure to acknowledge Stoddard, the raised position of the children's knees, and their odd waving carried little or no weight in the reasonable-suspicion calculus. The remaining factorsthe <span class="star-pagination">*273</span> road's use by smugglers, the temporal proximity between respondent's trip and the agents' shift change, and the use of minivans by smugglerswere not enough to render the stop permissible. <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1251" aria-description="Citation for case: United States v. Ralph Arvizu"><i>Id.,</i> at 1251</a></span>. We granted certiorari to review the decision of the Court of Appeals because of its importance to the enforcement of federal drug and immigration laws. <span class="citation multiple-matches"><a href="/c/U.%20S./532/1065/">532 U. S. 1065</a></span> (2001).</p>
<p>The Fourth Amendment prohibits "unreasonable searches and seizures" by the Government, and its protections extend to brief investigatory stops of persons or vehicles that fall short of traditional arrest. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968); <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981). Because the "balance between the public interest and the individual's right to personal security," <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975), tilts in favor of a standard less than probable cause in such cases, the Fourth Amendment is satisfied if the officer's action is supported by reasonable suspicion to believe that criminal activity "`may be afoot,' " <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 30</a></span>). See also <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S., at 417</a></span> ("An investigatory stop must be justified by some objective manifestation that the person stopped is, or is about to be, engaged in criminal activity").</p>
<p>When discussing how reviewing courts should make reasonable-suspicion determinations, we have said repeatedly that they must look at the "totality of the circumstances" of each case to see whether the detaining officer has a "particularized and objective basis" for suspecting legal wrongdoing. See, <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>e. g., id.,</i> at 417-418</a></span>. This process allows officers to draw on their own experience and specialized training to make inferences from and deductions about the cumulative information available to them that "might well elude an untrained person." <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez"><i>Id.,</i> at 418</a></span>. See also <i>Ornelas</i>  v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 699</a></span> (1996) (reviewing court must give "due weight" to factual inferences drawn by resident <span class="star-pagination">*274</span> judges and local law enforcement officers). Although an officer's reliance on a mere "`hunch' " is insufficient to justify a stop, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 27</a></span>, the likelihood of criminal activity need not rise to the level required for probable cause, and it falls considerably short of satisfying a preponderance of the evidence standard, <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow"><i>Sokolow, supra,</i> at 7</a></span>.</p>
<p>Our cases have recognized that the concept of reasonable suspicion is somewhat abstract. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#696" aria-description="Citation for case: Ornelas v. United States"><i>Ornelas, supra,</i> at 696</a></span> (principle of reasonable suspicion is not a "`finely-tuned standar[d]' "); <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez"><i>Cortez, supra,</i> at 417</a></span> (the cause "sufficient to authorize police to stop a person" is an "elusive concept"). But we have deliberately avoided reducing it to "`a neat set of legal rules,' " <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas, supra,</a></span></i> at 695-696 (quoting <i>Illinois</i>  v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 232</a></span> (1983)). In <i><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">Sokolow</a></span>,</i> for example, we rejected a holding by the Court of Appeals that distinguished between evidence of ongoing criminal behavior and probabilistic evidence because it "create[d] unnecessary difficulty in dealing with one of the relatively simple concepts embodied in the Fourth Amendment." <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S., at 7-8</a></span>.</p>
<p>We think that the approach taken by the Court of Appeals here departs sharply from the teachings of these cases. The court's evaluation and rejection of seven of the listed factors in isolation from each other does not take into account the "totality of the circumstances," as our cases have understood that phrase. The court appeared to believe that each observation by Stoddard that was by itself readily susceptible to an innocent explanation was entitled to "no weight." See <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1249" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1249-1251</a></span>. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> however, precludes this sort of divide-and-conquer analysis. The officer in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> observed the petitioner and his companions repeatedly walk back and forth, look into a store window, and confer with one another. Although each of the series of acts was "perhaps innocent in itself," we held that, taken together, they "warranted further investigation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. See also <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#9" aria-description="Citation for case: United States v. Sokolow"><i>Sokolow, supra,</i> at 9</a></span> (holding that factors which by themselves <span class="star-pagination">*275</span> were "quite consistent with innocent travel" collectively amounted to reasonable suspicion).</p>
<p>The Court of Appeals' view that it was necessary to "clearly delimit" an officer's consideration of certain factors to reduce "troubling . . . uncertainty," <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1248</a></span>, also runs counter to our cases and underestimates the usefulness of the reasonable-suspicion standard in guiding officers in the field. In <i>Ornelas</i> v. <i>United States</i><i>,</i> we held that the standard for appellate review of reasonablesuspicion determinations should be <i>de novo,</i> rather than for "abuse of discretion." <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#691" aria-description="Citation for case: Ornelas v. United States">517 U. S., at 691</a></span>. There, we reasoned that <i>de novo</i> review would prevent the affirmance of opposite decisions on identical facts from different judicial districts in the same circuit, which would have been possible under the latter standard, and would allow appellate courts to clarify the legal principles. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 697</a></span>. Other benefits of the approach, we said, were its tendency to unify precedent and greater capacity to provide law enforcement officers with the tools to reach correct determinations beforehand: Even if in many instances the factual "mosaic" analyzed for a reasonable-suspicion determination would preclude one case from squarely controlling another, "two decisions when viewed together may usefully add to the body of law on the subject." <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 697-698</a></span>.</p>
<p>But the Court of Appeals' approach would go considerably beyond the reasoning of <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas</a></span></i> and seriously undercut the "totality of the circumstances" principle which governs the existence <i>vel non</i> of "reasonable suspicion." Take, for example, the court's positions that respondent's deceleration could not be considered because "slowing down after spotting a law enforcement vehicle is an entirely normal response that is in no way indicative of criminal activity" and that his failure to acknowledge Stoddard's presence provided no support because there were "no `special circumstances' rendering `innocent avoidance . . . improbable.' " <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1248" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1248-1249</a></span>. We think it quite reasonable that a driver's <span class="star-pagination">*276</span> slowing down, stiffening of posture, and failure to acknowledge a sighted law enforcement officer might well be unremarkable in one instance (such as a busy San Francisco highway) while quite unusual in another (such as a remote portion of rural southeastern Arizona). Stoddard was entitled to make an assessment of the situation in light of his specialized training and familiarity with the customs of the area's inhabitants. See <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States"><i>Ornelas, supra,</i> at 699</a></span>. To the extent that a totality of the circumstances approach may render appellate review less circumscribed by precedent than otherwise, it is the nature of the totality rule.</p>
<p>In another instance, the Court of Appeals chose to dismiss entirely the children's waving on grounds that odd conduct by children was all too common to be probative in a particular case. See <span class="citation" data-id="771188"><a href="/opinion/771188/united-states-v-ralph-arvizu/#1249" aria-description="Citation for case: United States v. Ralph Arvizu">232 F. 3d, at 1249</a></span> ("If every odd act engaged in by one's children . . . could contribute to a finding of reasonable suspicion, the vast majority of American parents might be stopped regularly within a block of their homes"). Yet this case did not involve simply any odd act by children. At the suppression hearing, Stoddard testified about the children's waving several times, and the record suggests that he physically demonstrated it as well.<sup>[2]</sup> The District Court Judge, who saw and heard Stoddard, then characterized the waving as "methodical," "mechanical," "abnormal," and "certainly . . . a fact that is odd and would lead a reasonable officer to wonder why they are doing this." App. to Pet. for Cert. 25a. Though the issue of this case does not turn on the children's idiosyncratic actions, the Court of Appeals should not have casually rejected this factor in light of the District Court's superior access to the evidence and the well-recognized inability of reviewing courts to reconstruct what happened in the courtroom.</p>
<p><span class="star-pagination">*277</span> Having considered the totality of the circumstances and given due weight to the factual inferences drawn by the law enforcement officer and District Court Judge, we hold that Stoddard had reasonable suspicion to believe that respondent was engaged in illegal activity. It was reasonable for Stoddard to infer from his observations, his registration check, and his experience as a border patrol agent that respondent had set out from Douglas along a little-traveled route used by smugglers to avoid the 191 checkpoint. Stoddard's knowledge further supported a commonsense inference that respondent intended to pass through the area at a time when officers would be leaving their backroads patrols to change shifts. The likelihood that respondent and his family were on a picnic outing was diminished by the fact that the minivan had turned away from the known recreational areas accessible to the east on Rucker Canyon Road. Corroborating this inference was the fact that recreational areas farther to the north would have been easier to reach by taking 191, as opposed to the 40-to-50-mile trip on unpaved and primitive roads. The children's elevated knees suggested the existence of concealed cargo in the passenger compartment. Finally, for the reasons we have given, Stoddard's assessment of respondent's reactions upon seeing him and the children's mechanical-like waving, which continued for a full four to five minutes, were entitled to some weight.</p>
<p>Respondent argues that we must rule in his favor because the facts suggested a family in a minivan on a holiday outing. A determination that reasonable suspicion exists, however, need not rule out the possibility of innocent conduct. See <i>Illinois</i> v. <i>Wardlow,</i> <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/#125" aria-description="Citation for case: Illinois v. Wardlow">528 U. S. 119, 125</a></span> (2000) (that flight from police is not necessarily indicative of ongoing criminal activity does not establish Fourth Amendment violation). Undoubtedly, each of these factors alone is susceptible of innocent explanation, and some factors are more probative than others. Taken together, we believe they sufficed to form a particularized and objective basis for Stoddard's <span class="star-pagination">*278</span> stopping the vehicle, making the stop reasonable within the meaning of the Fourth Amendment.</p>
<p>The judgment of the Court of Appeals is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>[Appendix to opinion of the Court follows this page.]</p>
<p>Justice Scalia, concurring.</p>
<p>I join the opinion of the Court, because I believe it accords with our opinion in <i>Ornelas</i> v. <i>United States,</i> <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#699" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 699</a></span> (1996), requiring <i>de novo</i> review which nonetheless gives "due weight to inferences drawn from [the] facts by resident judges . . . ." As I said in my dissent in <i><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">Ornelas</a></span>,</i> however, I do not see how deferring to the District Court's factual inferences (as opposed to its findings of fact) is compatible with <i>de novo</i> review. <span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#705" aria-description="Citation for case: Ornelas v. United States"><i>Id.,</i> at 705</a></span>.</p>
<p>The Court today says that "due weight" should have been given to the District Court's determinations that the children's waving was "`methodical,' `mechanical,' `abnormal,' and `certainly . . . a fact that is odd and would lead a reasonable officer to wonder why they are doing this.' " <i>Ante,</i>  at 276. "Methodical," "mechanical," and perhaps even "abnormal" and "odd," are findings of fact that deserve respect. But the inference that this "would lead a reasonable officer to wonder why they are doing this," amounts to the conclusion that their action was suspicious, which I would have thought (if <i>de novo</i> review is the standard) is the prerogative of the Court of Appeals. So we have here a peculiar sort of <i>de novo</i> review.</p>
<p>I may add that, even holding the Ninth Circuit to no more than the traditional methodology of <i>de novo</i> review, its judgment here would have to be reversed.</p>
<p></p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging affirmance were filed for the DKT Liberty Project by <i>Julia M. Carpenter;</i> and for the National Association of Criminal Defense Lawyers et al. by <i>Lawrence S. Lustberg</i> and <i>Risa E. Kaufman.</i> </p>
<p>[1]  Coronado National Forest consists of 12 widely scattered sections of land covering 1,780,000 acres in southeastern Arizona and southwestern New Mexico. The section of the forest near Douglas includes the Chiricahua, Dragoon, and Peloncillo Mountain Ranges.</p>
<p>[2]  At one point during the hearing, Stoddard testified that "[the children's waving] wasn't in a normal pattern. It looked like they were instructed to do so. They kind of stuck their hands up and began waving to me like this." App. 35.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Ash.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Ash"
type: case
citation: "413 U.S. 300 (1973)"
parallel_cite: "93 S. Ct. 2568; 37 L. Ed. 2d 619"
neutral_cite: 1973 U.S. LEXIS 45
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ash
  varies_by_point: false
  scope_note: "Good law; no Sixth Amendment right to counsel at a photographic display."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108846/united-states-v-ash/"
  cluster_id: 108846
  opinion_id: 108846
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Kirby v. Illinois]]", "[[Gilbert v. California]]", "[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[Stovall v. Denno]]"]
aliases: ["United States v. Charles J. Ash, Jr."]
tags: ["case", "sixth-amendment", "eyewitness-identification", "right-to-counsel"]
holding: "The Sixth Amendment does not grant a right to counsel at a post-indictment photographic display (no trial-like confrontation, since the…"
lake:
  record_id: United States v. Ash
  status: verified
  projected_at: 2026-07-06
---

# United States v. Ash

*413 U.S. 300 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Ash was indicted for a bank robbery, the prosecutor, preparing for trial, showed witnesses a set of color photographs — including Ash's — to confirm their identifications. Defense counsel was not present at this post-indictment photographic display. Ash argued the procedure was a critical stage at which he was entitled to counsel under the Sixth Amendment.

## Issue
Whether a defendant has a Sixth Amendment right to have counsel present when the government conducts a post-indictment photographic display of the accused to witnesses for identification purposes.

## Rule
No. The Court held that "the Sixth Amendment does not grant the right to counsel at photographic displays conducted by the Government for the purpose of allowing a witness to attempt an identification of the offender." — 413 U.S. at 321. ^pin-321

A photographic display is not a trial-like confrontation: the accused is not present and need not confront witnesses or the prosecution, so the presence of counsel is not required to preserve a fair trial.

## Application
Because Ash was not present when the prosecutor showed the photo array to witnesses, the display was not a trial-like confrontation triggering the right to counsel. The risks of suggestive photographic identification could be exposed through ordinary trial tools — cross-examination of the witnesses and the officers — rather than by counsel's attendance at the display. The absence of defense counsel from the photo identification therefore did not violate the Sixth Amendment.

## Conclusion
There was no Sixth Amendment right to counsel at the post-indictment photographic display; the Court of Appeals' contrary judgment was reversed. The right to counsel attaches to trial-like confrontations at which the accused is present, not to photo arrays shown to witnesses.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ash* distinguishes the live-lineup right to counsel of [[Gilbert v. California]] and is consistent with [[Kirby v. Illinois]] (right attaches at the initiation of adversary proceedings); suggestive photo identifications are policed instead through the due-process reliability test of [[Neil v. Biggers]] and [[Manson v. Brathwaite]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Ash*, 413 U.S. 300 (1973) — https://www.courtlistener.com/opinion/108846/united-states-v-ash/ — pinpoint: 321.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "78fdcce416d0c6fa", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ash"}, "payload": {"all": [{"cite": "413 U.S. 300", "page": "300", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "413"}, {"cite": "93 S. Ct. 2568", "page": "2568", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "37 L. Ed. 2d 619", "page": "619", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "37"}, {"cite": "1973 U.S. LEXIS 45", "page": "45", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1973"}], "display": "413 U.S. 300", "official": {"cite": "413 U.S. 300", "page": "300", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "413"}, "official_selection_present": true, "record_id": "United States v. Ash"}}
{"assertion_id": "b59055b93519be46", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-321", "record_id": "United States v. Ash"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-321", "pinpoint_status": "slip-only", "quote": "--- # United States v. Ash *413 U.S. 300 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Ash was indicted for a bank robbery, the prosecutor, preparing for trial, showed witnesses a set of color photographs — including Ash's — to confirm their identifications. Defense counsel was not present at this post-indictment photographic display. Ash argued the procedure was a critical stage at which he was entitled to counsel under the Sixth Amendment. ## Issue Whether a defendant has a Sixth Amendment right to have counsel present when the government conducts a post-indictment photographic display of the accused to witnesses for identification purposes. ## Rule No. The Court held that", "quote_fidelity": "mismatch", "record_id": "United States v. Ash", "star_marker": null}}
{"assertion_id": "345422af364de3e8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ash"}, "payload": {"as_of_content": "1973-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Ash", "scope_note": "Good law; no Sixth Amendment right to counsel at a photographic display.", "varies_by_point": false}}
```

### lake record — United States v. Ash

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ash",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ash",
    "case_name_short": "Ash",
    "case_name_full": "United States v. Ash",
    "input_case_name": "United States v. Ash",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-21",
    "year": 1973,
    "docket": null,
    "cluster_id": 108846,
    "lead_opinion_id": 108846,
    "sibling_ids": [
      108846,
      9425398,
      9425399,
      9425400
    ],
    "absolute_url": "/opinion/108846/united-states-v-ash/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 300",
      "volume": "413",
      "reporter": "U.S.",
      "page": "300",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2568",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 619",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 45",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 300",
        "volume": "413",
        "reporter": "U.S.",
        "page": "300",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2568",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2568",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 619",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 45",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 300",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 300",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-321",
      "page": null,
      "quote": "--- # United States v. Ash *413 U.S. 300 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Ash was indicted for a bank robbery, the prosecutor, preparing for trial, showed witnesses a set of color photographs \u2014 including Ash's \u2014 to confirm their identifications. Defense counsel was not present at this post-indictment photographic display. Ash argued the procedure was a critical stage at which he was entitled to counsel under the Sixth Amendment. ## Issue Whether a defendant has a Sixth Amendment right to have counsel present when the government conducts a post-indictment photographic display of the accused to witnesses for identification purposes. ## Rule No. The Court held that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ash",
    "varies_by_point": false,
    "scope_note": "Good law; no Sixth Amendment right to counsel at a photographic display.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Dew",
          "cluster_id": 9406638,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Craigen",
          "cluster_id": 10160931,
          "cite": [
            "370 Or. 696",
            "524 P.3d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramirez v. United States",
          "cluster_id": 8719635,
          "cite": [
            "898 F. Supp. 2d 659",
            "2012 U.S. Dist. LEXIS 107824",
            "2012 WL 3115161"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Henry Murphy v. State",
          "cluster_id": 3127894,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph Van Patten v. Jodine Deppisch",
          "cluster_id": 792984,
          "cite": [
            "434 F.3d 1038",
            "2006 U.S. App. LEXIS 1658",
            "2006 WL 162992"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LaPointe v. State",
          "cluster_id": 1380200,
          "cite": [
            "166 S.W.3d 287",
            "2005 WL 995371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Watson v. State",
          "cluster_id": 2333044,
          "cite": [
            "95 S.W.3d 342",
            "2002 WL 1722064"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Franks v. State",
          "cluster_id": 1495257,
          "cite": [
            "90 S.W.3d 771",
            "2002 WL 1592443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darnell Hayes",
          "cluster_id": 771010,
          "cite": [
            "231 F.3d 663",
            "2000 Cal. Daily Op. Serv. 8991",
            "2000 Daily Journal DAR 11947",
            "2000 U.S. App. LEXIS 27872",
            "2000 WL 1672631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Oliver v. State",
          "cluster_id": 5269601,
          "cite": [
            "995 S.W.2d 878",
            "1999 Tex. App. LEXIS 4604",
            "1999 WL 417387"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evitts v. Lucey",
          "cluster_id": 111302,
          "cite": [
            "83 L. Ed. 2d 821",
            "105 S. Ct. 830",
            "469 U.S. 387",
            "1985 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wheat v. United States",
          "cluster_id": 112074,
          "cite": [
            "100 L. Ed. 2d 140",
            "108 S. Ct. 1692",
            "486 U.S. 153",
            "1988 U.S. LEXIS 2306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Lopez",
          "cluster_id": 145633,
          "cite": [
            "165 L. Ed. 2d 409",
            "126 S. Ct. 2557",
            "548 U.S. 140",
            "2006 U.S. LEXIS 5165",
            "19 Fla. L. Weekly Fed. S 368",
            "33 A.L.R. Fed. 2d 661",
            "74 U.S.L.W. 4453"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perry v. Leeke",
          "cluster_id": 112168,
          "cite": [
            "102 L. Ed. 2d 624",
            "109 S. Ct. 594",
            "488 U.S. 272",
            "1989 U.S. LEXIS 306",
            "57 U.S.L.W. 4075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Willie Decoster, Jr.",
          "cluster_id": 314954,
          "cite": [
            "487 F.2d 1197",
            "159 U.S. App. D.C. 326"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. State",
          "cluster_id": 1448541,
          "cite": [
            "16 S.W.3d 808",
            "2000 Tex. Crim. App. LEXIS 43",
            "2000 WL 369127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael G. Thevis, Alton Bart Hood, Global Industries, Inc., Anna Jeanette Evans",
          "cluster_id": 397401,
          "cite": [
            "665 F.2d 616",
            "9 Fed. R. Serv. 1025",
            "1982 U.S. App. LEXIS 22706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rigoberto Moya-Gomez Celestino Orlando Estevez Amado Raphael Leon Adalberto Herrera and Menelao Orlando Estevez",
          "cluster_id": 513458,
          "cite": [
            "860 F.2d 706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Atwood",
          "cluster_id": 1182224,
          "cite": [
            "832 P.2d 593",
            "171 Ariz. 576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williamson v. State",
          "cluster_id": 1111870,
          "cite": [
            "512 So. 2d 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mitcham",
          "cluster_id": 1203051,
          "cite": [
            "824 P.2d 1277",
            "1 Cal. 4th 1027",
            "5 Cal. Rptr. 2d 230",
            "92 Cal. Daily Op. Serv. 1532",
            "92 Daily Journal DAR 3034",
            "1992 Cal. LEXIS 1269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Virgil",
          "cluster_id": 844274,
          "cite": [
            "253 P.3d 553",
            "51 Cal. 4th 1210",
            "126 Cal. Rptr. 3d 465",
            "2011 Cal. LEXIS 6538"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jackson",
          "cluster_id": 1838293,
          "cite": [
            "217 N.W.2d 22",
            "391 Mich. 323",
            "1974 Mich. LEXIS 139"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lotter",
          "cluster_id": 2116540,
          "cite": [
            "586 N.W.2d 591",
            "255 Neb. 456",
            "1998 Neb. LEXIS 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ash:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTUyMjU2MDAwMDAmcz02NTc2Nzg2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzImcz0yNTQzNDU5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108846 OR 9425398 OR 9425399 OR 9425400)",
    "indexed_citing_opinions": 590,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108846,
        "count": 551,
        "count_source": "search"
      },
      {
        "opinion_id": 9425398,
        "count": 57,
        "count_source": "search"
      },
      {
        "opinion_id": 9425399,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425400,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 868,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ash.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc2NjY3MDEmcz02NDUwODQ1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108846+OR+9425398+OR+9425399+OR+9425400%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108846,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 283186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 284440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 288980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 290782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 292225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 295836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 299374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 303766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 303865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1186833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1206841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1241302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1353187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1434555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1534458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1710337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1724451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1758004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1838693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 1911421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2061648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2087977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2133215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2172829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2178575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2222943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108846,
        "cited_id": 2616794,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T22:17:08Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:24:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:17:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ash (truncated)

```
<div>
<center><b><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">413 U.S. 300</a></span> (1973)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
ASH.</h1></center>
<center>No. 71-1255.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 10, 1973.</center>
<center>Decided June 21, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT
<p><i>Edward R. Korman</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Griswold, Assistant Attorney General Petersen,</i> and <i>Jerome M. Feit.</i></p>
<p><i>Sherman L. Cohn,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./408/942/">408 U. S. 942</a></span>, argued the cause and filed a brief for respondent.</p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>In this case the Court is called upon to decide whether <span class="star-pagination">*301</span> the Sixth Amendment<sup>[1]</sup> grants an accused the right to have counsel present whenever the Government conducts a post-indictment photographic display, containing a picture of the accused, for the purpose of allowing a witness to attempt an identification of the offender. The United States Court of Appeals for the District of Columbia Circuit, sitting en banc, held, by a 5-to-4 vote, that the accused possesses this right to counsel. 149 U. S. App. D. C. 1, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span> (1972). The court's holding is inconsistent with decisions of the courts of appeals of nine other circuits.<sup>[2]</sup> We granted certiorari <span class="star-pagination">*302</span> to resolve the conflict and to decide this important constitutional question. <span class="citation multiple-matches"><a href="/c/U.%20S./407/909/">407 U. S. 909</a></span> (1972). We reverse and remand.</p>
<p></p>
<h2>I</h2>
<p>On the morning of August 26, 1965, a man with a stocking mask entered a bank in Washington, D. C., and began waving a pistol. He ordered an employee to hang up the telephone and instructed all others present not to move. Seconds later a second man, also wearing a stocking mask, entered the bank, scooped up money from tellers' drawers into a bag, and left. The gunman followed, and both men escaped through an alley. The robbery lasted three or four minutes.</p>
<p>A Government informer, Clarence McFarland, told authorities that he had discussed the robbery with Charles J. Ash, Jr., the respondent here. Acting on this information, an FBI agent, in February 1966, showed five black-and-white mug shots of Negro males of generally the same age, height, and weight, one of which was of Ash, to four witnesses. All four made uncertain identifications of Ash's picture. At this time Ash was not in custody and had not been charged. On April 1, 1966, an indictment was returned charging Ash and a codefendant, John L. Bailey, in five counts related to this <span class="star-pagination">*303</span> bank robbery, in violation of D. C. Code Ann. § 22-2901 and <span class="citation no-link">18 U. S. C. § 2113</span> (a).</p>
<p>Trial was finally set for May 1968, almost three years after the crime. In preparing for trial, the prosecutor decided to use a photographic display to determine whether the witnesses he planned to call would be able to make in-court identifications. Shortly before the trial, an FBI agent and the prosecutor showed five color photographs to the four witnesses who previously had tentatively identified the black-and-white photograph of Ash. Three of the witnesses selected the picture of Ash, but one was unable to make any selection. None of the witnesses selected the picture of Bailey which was in the group. This post-indictment<sup>[3]</sup> identification provides the basis for respondent Ash's claim that he was denied the right to counsel at a "critical stage" of the prosecution.</p>
<p>No motion for severance was made, and Ash and Bailey were tried jointly. The trial judge held a hearing on the suggestive nature of the pretrial photographic displays.<sup>[4]</sup> The judge did not make a clear ruling on suggestive nature, but held that the Government had demonstrated by "clear and convincing" evidence that in-court identifications would be "based on observation of <span class="star-pagination">*304</span> the suspect other than the intervening observation." App. 63-64.</p>
<p>At trial, the three witnesses who had been inside the bank identified Ash as the gunman, but they were unwilling to state that they were certain of their identifications. None of these made an in-court identification of Bailey. The fourth witness, who had been in a car outside the bank and who had seen the fleeing robbers after they had removed their masks, made positive in-court identifications of both Ash and Bailey. Bailey's counsel then sought to impeach this in-court identification by calling the FBI agent who had shown the color photographs to the witnesses immediately before trial. Bailey's counsel demonstrated that the witness who had identified Bailey in court had failed to identify a color photograph of Bailey. During the course of the examination, Bailey's counsel also, before the jury, brought out the fact that this witness had selected another man as one of the robbers. At this point the prosecutor became concerned that the jury might believe that the witness had selected a third person when, in fact, the witness had selected a photograph of Ash. After a conference at the bench, the trial judge ruled that all five color photographs would be admitted into evidence. The Court of Appeals held that this constituted the introduction of a post-indictment identification at the prosecutor's request and over the objection of defense counsel.<sup>[5]</sup></p>
<p><span class="star-pagination">*305</span> McFarland testified as a Government witness. He said he had discussed plans for the robbery with Ash before the event and, later, had discussed the results of the robbery with Ash in the presence of Bailey. McFarland was shown to possess an extensive criminal record and a history as an informer.</p>
<p>The jury convicted Ash on all counts. It was unable to reach a verdict on the charges against Bailey, and his motion for acquittal was granted. Ash received concurrent sentences on the several counts, the two longest being 80 months to 12 years.</p>
<p>The five-member majority of the Court of Appeals held that Ash's right to counsel, guaranteed by the Sixth Amendment, was violated when his attorney was not given the opportunity to be present at the photographic displays conducted in May 1968 before the trial. The majority relied on this Court's lineup cases, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), and on <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967).</p>
<p>The majority did not reach the issue of suggestiveness; their opinion implies, however, that they would order a remand for additional findings by the District Court. 149 U. S. App. D. C., at 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#98" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 98</a></span>. The majority refrained from deciding whether the in-court identifications could have independent bases, <i><span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">id.,</a></span></i> at 14-15 and nn. 20, 21, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 105</a></span>-106 and nn. 20, 21, but expressed doubt that the identifications at the trial had independent origins.</p>
<p>Dissenting opinions, joined by four judges, disagreed with the decision of the majority that the photographic identification was a "critical stage" requiring counsel, and criticized the majority's suggestion that the in-court identifications were tainted by defects in the photographic identifications. <i>Id.,</i> at 14-43, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#106" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 106-134</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*306</span> II</h2>
<p>The Court of Appeals relied exclusively on that portion of the Sixth Amendment providing, "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence." The right to counsel in Anglo-American law has a rich historical heritage, and this Court has regularly drawn on that history in construing the counsel guarantee of the Sixth Amendment. We re-examine that history in an effort to determine the relationship between the purposes of the Sixth Amendment guarantee and the risks of a photographic identification.</p>
<p>In <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-66</a></span> (1932), the Court discussed the English common-law rule that severely limited the right of a person accused of a felony to consult with counsel at trial. The Court examined colonial constitutions and statutes and noted that "in at least twelve of the thirteen colonies the rule of the English common law, in the respect now under consideration, had been definitely rejected and the right to counsel fully recognized in all criminal prosecutions, save that in one or two instances the right was limited to capital offenses or to the more serious crimes." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#64" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 64-65</a></span>. The Sixth Amendment counsel guarantee, thus, was derived from colonial statutes and constitutional provisions designed to reject the English common-law rule.</p>
<p>Apparently several concerns contributed to this rejection at the very time when countless other aspects of the common law were being imported. One consideration was the inherent irrationality of the English limitation. Since the rule was limited to felony proceedings, the result, absurd and illogical, was that an accused misdemeanant could rely fully on counsel, but <span class="star-pagination">*307</span> the accused felon, in theory at least,<sup>[6]</sup> could consult counsel only on legal questions that the accused proposed to the court. See <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 60</a></span>. English writers were appropriately critical of this inconsistency. See, for example, 4 W. Blackstone, Commentaries *355.</p>
<p>A concern of more lasting importance was the recognition and awareness that an unaided layman had little skill in arguing the law or in coping with an intricate procedural system. The function of counsel as a guide through complex legal technicalities long has been recognized by this Court. Mr. Justice Sutherland's well-known observations in <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span></i> bear repeating here:</p>
<blockquote>"Even the intelligent and educated layman has small and sometimes no skill in the science of law. If charged with crime, he is incapable, generally, of determining for himself whether the indictment is good or bad. He is unfamiliar with the rules of evidence. Left without the aid of counsel he may be put on trial without a proper charge, and convicted upon incompetent evidence, or evidence irrelevant to the issue or otherwise inadmissible. He lacks both the skill and knowledge adequately to prepare his defense, even though he have a perfect one. He requires the guiding hand of counsel at every step in the proceedings against him. Without it, though he be not guilty, he faces the danger of conviction because he does not know how to establish his innocence." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 69</a></span>.</blockquote>
<p>The Court frequently has interpreted the Sixth Amendment <span class="star-pagination">*308</span> to assure that the "guiding hand of counsel" is available to those in need of its assistance. See, for example, <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#344" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 344-345</a></span> (1963), and <i>Argersinger</i> v. <i>Hamlin,</i> <span class="citation" data-id="9424926"><a href="/opinion/108567/argersinger-v-hamlin/#31" aria-description="Citation for case: Argersinger v. Hamlin">407 U. S. 25, 31</a></span> (1972).</p>
<p>Another factor contributing to the colonial recognition of the accused's right to counsel was the adoption of the institution of the public prosecutor from the Continental inquisitorial system. One commentator has explained the effect of this development:</p>
<blockquote>"[E]arly in the eighteenth century the American system of judicial administration adopted an institution which was (and to some extent still is) unknown in England: while rejecting the fundamental juristic concepts upon which continental Europe's inquisitorial system of criminal procedure is predicated, the colonies borrowed one of its institutions, the public prosecutor, and grafted it upon the body of English (accusatorial) procedure embodied in the common law. Presumably, this innovation was brought about by the lack of lawyers, particularly in the newly settled regions, and by the increasing distances between the colonial capitals on the eastern seaboard and the ever-receding western frontier. Its result was that, at a time when virtually all but treason trials in England were still in the nature of suits between private parties, the accused in the colonies faced a government official whose specific function it was to prosecute, and who was incomparably more familiar than the accused with the problems of procedure, the idiosyncrasies of juries, and, last but not least, the personnel of the court." F. Heller, The Sixth Amendment 20-21 (1951) (footnote omitted).</blockquote>
<p><span class="star-pagination">*309</span> Thus, an additional motivation for the American rule was a desire to minimize the imbalance in the adversary system that otherwise resulted with the creation of a professional prosecuting official. Mr. Justice Black, writing for the Court in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938), spoke of this equalizing effect of the Sixth Amendment's counsel guarantee:</p>
<blockquote>"It embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel."</blockquote>
<p>This historical background suggests that the core purpose of the counsel guarantee was to assure "Assistance" at trial, when the accused was confronted with both the intricacies of the law and the advocacy of the public prosecutor.<sup>[7]</sup> Later developments have led this Court <span class="star-pagination">*310</span> to recognize that "Assistance" would be less than meaningful if it were limited to the formal trial itself.</p>
<p>This extension of the right to counsel to events before trial has resulted from changing patterns of criminal procedure and investigation that have tended to generate pretrial events that might appropriately be considered to be parts of the trial itself. At these newly emerging and significant events, the accused was confronted, just as at trial, by the procedural system, or by his expert adversary, or by both. In <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> the Court explained the process of expanding the counsel guarantee to these confrontations:</p>
<blockquote>"When the Bill of Rights was adopted, there were no organized police forces as we know them today. The accused confronted the prosecutor and the witnesses against him, and the evidence was marshalled, largely at the trial itself. In contrast, today's law enforcement machinery involves critical confrontations of the accused by the prosecution at pretrial proceedings where the results might well settle the accused's fate and reduce the trial itself to a mere formality. In recognition of these realities of modern criminal prosecution, our cases have construed the Sixth Amendment guarantee to apply to `critical' <span class="star-pagination">*311</span> stages of the proceedings." 388 U. S., at 224 (footnote omitted).</blockquote>
<p>The Court consistently has applied a historical interpretation of the guarantee, and has expanded the constitutional right to counsel only when new contexts appear presenting the same dangers that gave birth initially to the right itself.</p>
<p>Recent cases demonstrate the historical method of this expansion. In <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961), and in <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963), the accused was confronted with the procedural system and was required, with definite consequences, to enter a plea. In <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the accused was confronted by prosecuting authorities who obtained, by ruse and in the absence of defense counsel, incriminating statements. In <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), the accused was confronted by his adversary at a "critical stage" preliminary hearing at which the uncounseled accused could not hope to obtain so much benefit as could his skilled adversary.</p>
<p>The analogy between the unrepresented accused at the pretrial confrontation and the unrepresented defendant at trial, implicit in the cases mentioned above, was explicitly drawn in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>:</i></p>
<blockquote>"The trial which might determine the accused's fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness`that's the man.'" 388 U. S., at 235-236.</blockquote>
<p><span class="star-pagination">*312</span> Throughout this expansion of the counsel guarantee to trial-like confrontations, the function of the lawyer has remained essentially the same as his function at trial. In all cases considered by the Court, counsel has continued to act as a spokesman for, or advisor to, the accused. The accused's right to the "Assistance of Counsel" has meant just that, namely, the right of the accused to have counsel acting as his assistant. In <i><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">Hamilton</a></span></i> and <i><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">White</a></span>,</i> for example, the Court envisioned the lawyer as advising the accused on available defenses in order to allow him to plead intelligently. <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/#54" aria-description="Citation for case: Hamilton v. Alabama">368 U. S., at 54-55</a></span>; <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/#60" aria-description="Citation for case: White v. Maryland">373 U. S., at 60</a></span>. In <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> counsel could have advised his client on the benefits of the Fifth Amendment and could have sheltered him from the overreaching of the prosecution. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#205" aria-description="Citation for case: Massiah v. United States">377 U. S., at 205</a></span>. Cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 466</a></span> (1966). In <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> the skill of the lawyer in examining witnesses, probing for evidence, and making legal arguments was relied upon by the Court to demonstrate that, in the light of the purpose of the preliminary hearing under Alabama law, the accused required "Assistance" at that hearing. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#9" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 9</a></span>.</p>
<p>The function of counsel in rendering "Assistance" continued at the lineup under consideration in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and its companion cases. Although the accused was not confronted there with legal questions, the lineup offered opportunities for prosecuting authorities to take advantage of the accused. Counsel was seen by the Court as being more sensitive to, and aware of, suggestive influences than the accused himself, and as better able to reconstruct the events at trial. Counsel present at lineup would be able to remove disabilities of the accused in precisely the same fashion that counsel compensated for the disabilities of the layman at trial. Thus, the Court mentioned that the accused's memory might be dimmed by "emotional tension," that the accused's credibility at <span class="star-pagination">*313</span> trial would be diminished by his status as defendant, and that the accused might be unable to present his version effectively without giving up his privilege against compulsory self-incrimination. <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade">388 U. S., at 230-231</a></span>. It was in order to compensate for these deficiencies that the Court found the need for the assistance of counsel.</p>
<p>This review of the history and expansion of the Sixth Amendment counsel guarantee demonstrates that the test utilized by the Court has called for examination of the event in order to determine whether the accused required aid in coping with legal problems or assistance in meeting his adversary. Against the background of this traditional test, we now consider the opinion of the Court of Appeals.</p>
<p></p>
<h2>III</h2>
<p>Although the Court of Appeals' majority recognized the argument that "a major purpose behind the right to counsel is to protect the defendant from errors that he himself might make if he appeared in court alone," the court concluded that "other forms of prejudice," mentioned and recognized in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> could also give rise to a right to counsel. 149 U. S. App. D. C., at 10, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#101" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 101</a></span>. These forms of prejudice were felt by the court to flow from the possibilities for mistaken identification inherent in the photographic display.<sup>[8]</sup></p>
<p><span class="star-pagination">*314</span> We conclude that the dangers of mistaken identification, mentioned in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> were removed from context by the Court of Appeals and were incorrectly utilized as a sufficient basis for requiring counsel. Although <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> did discuss possibilities for suggestion and the difficulty for reconstructing suggestivity, this discussion occurred only after the Court had concluded that the lineup constituted a trial-like confrontation, requiring the "Assistance of Counsel" to preserve the adversary process by compensating for advantages of the prosecuting authorities.</p>
<p>The above discussion of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> has shown that the traditional Sixth Amendment test easily allowed extension of counsel to a lineup. The similarity to trial was apparent, and counsel was needed to render "Assistance" in counterbalancing any "overreaching" by the prosecution.</p>
<p>After the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> held that a lineup constituted a trial-like confrontation requiring counsel, a more difficult issue remained in the case for consideration. The same changes in law enforcement that led to lineups and pretrial hearings also generated other events at which the accused was confronted by the prosecution. The Government had argued in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that if counsel was required at a lineup, the same forceful considerations would mandate counsel at other preparatory steps in the "gathering of the prosecution's evidence," such as, for <span class="star-pagination">*315</span> particular example, the taking of fingerprints or blood samples. 388 U. S., at 227.</p>
<p>The Court concluded that there were differences. Rather than distinguishing these situations from the lineup in terms of the need for counsel to assure an equal confrontation at the time, the Court recognized that there were times when the subsequent trial would cure a one-sided confrontation between prosecuting authorities and the uncounseled defendant. In other words, such stages were not "critical." Referring to fingerprints, hair, clothing, and other blood samples, the Court explained:</p>
<blockquote>"Knowledge of the techniques of science and technology is sufficiently available, and the variables in techniques few enough, that the accused has the opportunity for a meaningful confrontation of the Government's case at trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts." 388 U. S., at 227-228.</blockquote>
<p>The structure of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> viewed in light of the careful limitation of the Court's language to "confrontations,"<sup>[9]</sup><span class="star-pagination">*316</span> makes it clear that lack of scientific precision and inability to reconstruct an event are not the tests for requiring counsel in the first instance. These are, instead, the tests to determine whether confrontation with counsel at trial can serve as a substitute for counsel at the pretrial confrontation. If accurate reconstruction is possible, the risks inherent in any confrontation still remain, but the opportunity to cure defects at trial causes the confrontation to cease to be "critical." The opinion of the Court even indicated that changes in procedure might cause a lineup to cease to be a "critical" confrontation:</p>
<blockquote>"Legislative or other regulations, such as those of local police departments, which eliminate the risks of abuse and unintentional suggestion at lineup proceedings and the impediments to meaningful confrontation at trial may also remove the basis for regarding the stage as `critical.'" 388 U. S., at 239 (footnote omitted).</blockquote>
<p>See, however, <i>id.,</i> at 262 n. (opinion of Fortas, J.).</p>
<p>The Court of Appeals considered its analysis complete after it decided that a photographic display lacks scientific precision and ease of accurate reconstruction at trial. That analysis, under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> however, merely carries one to the point where one must establish that the trial itself can provide no substitute for counsel if a pretrial confrontation is conducted in the absence of counsel. Judge Friendly, writing for the Second Circuit in <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888</a></span> (1969), recognized that the "criticality" test of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> if applied outside the confrontation context, would result in drastic expansion of the right to counsel:</p>
<blockquote>"None of the classical analyses of the assistance to be given by counsel, Justice Sutherland's in Powell v. Alabama . . . and Justice Black's in Johnson v. <span class="star-pagination">*317</span> Zerbst . . . and Gideon v. Wainwright . . . suggests that counsel must be present when the prosecution is interrogating witnesses in the defendant's absence even when, as here, the defendant is under arrest; counsel is rather to be provided to prevent the defendant himself from falling into traps devised by a lawyer on the other side and to see to it that all available defenses are proffered. Many other aspects of the prosecution's interviews with a victim or a witness to a crime afford just as much opportunity for undue suggestion as the display of photographs; so, too, do the defense's interviews, notably with alibi witnesses." <i>Id.,</i> at 899-900.</blockquote>
<p>We now undertake the threshhold analysis that must be addressed.</p>
<p></p>
<h2>IV</h2>
<p>A substantial departure from the historical test would be necessary if the Sixth Amendment were interpreted to give Ash a right to counsel at the photographic identification in this case. Since the accused himself is not present at the time of the photographic display, and asserts no right to be present, Brief for Respondent 40, no possibility arises that the accused might be misled by his lack of familiarity with the law or overpowered by his professional adversary. Similarly, the counsel guarantee would not be used to produce equality in a trial-like adversary confrontation. Rather, the guarantee was used by the Court of Appeals to produce confrontation at an event that previously was not analogous to an adversary trial.</p>
<p>Even if we were willing to view the counsel guarantee in broad terms as a generalized protection of the adversary process, we would be unwilling to go so far as to extend the right to a portion of the prosecutor's trial-preparation interviews with witnesses. Although photography <span class="star-pagination">*318</span> is relatively new, the interviewing of witnesses before trial is a procedure that predates the Sixth Amendment. In England in the 16th and 17th centuries counsel regularly interviewed witnesses before trial. 9 W. Holdsworth, History of English Law 226-228 (1926). The traditional counterbalance in the American adversary system for these interviews arises from the equal ability of defense counsel to seek and interview witnesses himself.</p>
<p>That adversary mechanism remains as effective for a photographic display as for other parts of pretrial interviews.<sup>[10]</sup> No greater limitations are placed on defense counsel in constructing displays, seeking witnesses, and conducting photographic identifications than those applicable to the prosecution.<sup>[11]</sup> Selection of the picture of a person other than the accused, or the inability of a witness to make any selection, will be useful to the defense in precisely the same manner that the selection of <span class="star-pagination">*319</span> a picture of the defendant would be useful to the prosecution.<sup>[12]</sup> In this very case, for example, the initial tender of the photographic display was by Bailey's counsel, who sought to demonstrate that the witness had failed to make a photographic identification. Although we do not suggest that equality of access to photographs removes all potential for abuse,<sup>[13]</sup> it does remove any inequality in the adversary process itself and thereby fully satisfies the historical spirit of the Sixth Amendment's counsel guarantee.</p>
<p>The argument has been advanced that requiring counsel might compel the police to observe more scientific procedures or might encourage them to utilize corporeal rather than photographic displays.<sup>[14]</sup> This Court has <span class="star-pagination">*320</span> recognized that improved procedures can minimize the dangers of suggestion. <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span>, 386 n. 6 (1968). Commentators have also proposed more accurate techniques.<sup>[15]</sup></p>
<p>Pretrial photographic identifications, however, are hardly unique in offering possibilities for the actions of the prosecutor unfairly to prejudice the accused. Evidence favorable to the accused may be withheld; testimony of witnesses may be manipulated; the results of laboratory tests may be contrived. In many ways the prosecutor, by accident or by design, may improperly subvert the trial. The primary safeguard against abuses of this kind is the ethical responsibility of the prosecutor,<sup>[16]</sup> who, as so often has been said, may "strike hard blows" but not "foul ones." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935); <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87-88</a></span> (1963). If that safeguard fails, review remains available under due process standards. See <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972); <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935); <i>Miller</i> v. <i>Pate,</i> <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span> (1967); <i>Chambers</i> v. <i>Mississippi,</i> <span class="citation" data-id="9425169"><a href="/opinion/108718/chambers-v-mississippi/" aria-description="Citation for case: Chambers v. Mississippi">410 U. S. 284</a></span> (1973). These same safeguards apply to misuse of photographs. See <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>.</p>
<p><span class="star-pagination">*321</span> We are not persuaded that the risks inherent in the use of photographic displays are so pernicious that an extraordinary system of safeguards is required.</p>
<p>We hold, then, that the Sixth Amendment does not grant the right to counsel at photographic displays conducted by the Government for the purpose of allowing a witness to attempt an identification of the offender. This holding requires reversal of the judgment of the Court of Appeals. Although respondent Ash has urged us to examine this photographic display under the due process standard enunciated in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>, the Court of Appeals, expressing the view that additional findings would be necessary, refused to decide the issue. 149 U. S. App. D. C., at 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#98" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d, at 98</a></span>. We decline to consider this question on this record in the first instance. It remains open, of course, on the Court of Appeals' remand to the District Court.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE STEWART, concurring in the judgment.</p>
<p>The issue in the present case is whether, under the Sixth Amendment, a person who has been indicted is entitled to have a lawyer present when prosecution witnesses are shown the person's photograph and asked if they can identify him.</p>
<p>The Sixth Amendment guarantees that "[i]n all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence." This Court's decisions make it clear that a defendant is entitled to the assistance of counsel not only at the trial itself, but at all "critical stages" of his "prosecution." See <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>; <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>. The requirement <span class="star-pagination">*322</span> that there be a "prosecution," means that this constitutional "right to counsel attaches only at or after the time that adversary judicial proceedings have been initiated against [an accused] . . . ." "It is this point . . . that marks the commencement of the `criminal prosecutions' to which alone the explicit guarantees of the Sixth Amendment are applicable." <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#688" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 688, 690</a></span> (plurality opinion). Since the photographic identification in the present case occurred after the accused had been indicted, and thus clearly after adversary judicial proceedings had been initiated, the only question is whether that procedure was such a "critical stage" that the Constitution required the presence of counsel.</p>
<p>In <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra</a></span></i><i>,</i> the Court determined that a pretrial proceeding is a "critical stage" if "the presence of . . . counsel is necessary to preserve the defendant's. . . right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." 388 U. S., at 227. Pretrial proceedings are "critical," then, if the presence of counsel is essential "to protect the fairness of the trial itself." <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#239" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 239</a></span>; cf. <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#27" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 27-28</a></span> (STEWART, J., dissenting).</p>
<p>The Court held in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that a post-indictment, pretrial lineup at which the accused was exhibited to identifying witnesses was such a critical stage, because of the substantial possibility that the accused's right to a fair trial would otherwise be irretrievably lost. The hazard of unfair suggestive influence at a lineup, which, because of the nature of the proceeding, could seldom be reconstructed at trial, left little doubt, the Court thought, "that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was `as much entitled to such aid [of counsel] . . . as at the trial itself.'" 388 U. S., at 237.</p>
<p><span class="star-pagination">*323</span> The Court stressed in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that the danger of mistaken identification at trial was appreciably heightened by the "degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 228</a></span>. There are numerous and subtle possibilities for such improper suggestion in the dynamic context of a lineup. Judge Wilkey, dissenting in the present case, accurately described a lineup as:</p>
<blockquote>"a little drama, stretching over an appreciable span of time. The accused is there in the flesh, three-dimensional and always full-length. Further, he isn't merely there, he acts. He walks on stage, he blinks in the glare of lights, he turns and twists, often muttering asides to those sharing the spotlight. He can be required to utter significant words, to turn a profile or back, to walk back and forth, to doff one costume and don another. All the while the potentially identifying witness is watching, a prosecuting attorney and a police detective at his elbow, ready to record the witness' every word and reaction." 149 U. S. App. D. C. 1, 17, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/#108" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92, 108</a></span>.</blockquote>
<p>With no attorney for the accused present at this "little drama," defense counsel at trial could seldom convincingly discredit a witness' courtroom identification by showing it to be based on an impermissibly suggestive lineup. In addition to the problems posed by the fluid nature of a lineup, the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> pointed out that neither the witnesses nor the lineup participants were likely to be alert for suggestive influences or schooled in their detection. "In short, the accused's inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness' court-room identification." 388 U. S., at 231-232.</p>
<p><span class="star-pagination">*324</span> The Court held, therefore, that counsel was required at a lineup, primarily as an observer, to ensure that defense counsel could effectively confront the prosecution's evidence at trial. Attuned to the possibilities of suggestive influences, a lawyer could see any unfairness at a lineup, question the witnesses about it at trial, and effectively reconstruct what had gone on for the benefit of the jury or trial judge.<sup>[*]</sup></p>
<p>A photographic identification is quite different from a lineup, for there are substantially fewer possibilities of impermissible suggestion when photographs are used, and those unfair influences can be readily reconstructed at trial. It is true that the defendant's photograph may be markedly different from the others displayed, but this unfairness can be demonstrated at trial from an actual comparison of the photographs used or from the witness' description of the display. Similarly, it is possible that the photographs could be arranged in a suggestive manner, or that by comment or gesture the prosecuting authorities might single out the defendant's picture. But these are the kinds of overt influence that a witness can easily recount and that would serve to impeach the identification testimony. In short, there are few possibilities for unfair suggestivenessand those rather blatant and easily reconstructed. Accordingly, an accused would not be foreclosed from an effective cross-examination of an identification witness simply because his counsel was <span class="star-pagination">*325</span> not present at the photographic display. For this reason, a photographic display cannot fairly be considered a "critical stage" of the prosecution. As the Court of Appeals for the Third Circuit aptly concluded:</p>
<blockquote>"If . . . the identification is not in a live lineup at which defendant may be forced to act, speak or dress in a suggestive way, where the possibilities for suggestion are multiplied, where the ability to reconstruct the events is minimized, and where the effect of a positive identification is likely to be permanent, but at a viewing of immobile photographs easily reconstructible, far less subject to subtle suggestion, and far less indelible in its effect when the witness is later brought face to face with the accused, there is even less reason to denominate the procedure a critical stage at which counsel must be present." <i>United States ex rel. Reed</i> v. <i>Anderson,</i> <span class="citation" data-id="9458303"><a href="/opinion/303865/united-states-of-america-ex-rel-cleveland-reed-v-raymond-anderson/#745" aria-description="Citation for case: United States of America Ex Rel. Cleveland Reed v....">461 F. 2d 739, 745</a></span>.</blockquote>
<p>Preparing witnesses for trial by checking their identification testimony against a photographic display is little different, in my view, from the prosecutor's other interviews with the victim or other witnesses before trial. See <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#900" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 900</a></span>. While these procedures can be improperly conducted, the possibility of irretrievable prejudice is remote, since any unfairness that does occur can usually be flushed out at trial through cross-examination of the prosecution witnesses. The presence of defense counsel at such pretrial preparatory sessions is neither appropriate nor necessary under our adversary system of justice "to preserve the defendant's basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#227" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 227</a></span>.</p>
<p><span class="star-pagination">*326</span> MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The Court holds today that a pretrial display of photographs to the witnesses of a crime for the purpose of identifying the accused, unlike a lineup, does not constitute a "critical stage" of the prosecution at which the accused is constitutionally entitled to the presence of counsel. In my view, today's decision is wholly unsupportable in terms of such considerations as logic, consistency, and, indeed, fairness. As a result, I must reluctantly conclude that today's decision marks simply another<sup>[1]</sup> step towards the complete evisceration of the fundamental constitutional principles established by this Court, only six years ago, in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); and <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). I dissent.</p>
<p></p>
<h2>I</h2>
<p>On the morning of August 26, 1965, two men wearing stocking masks robbed the American Security and Trust Co. in Washington, D. C. The robbery lasted only about three or four minutes and, on the day of the crime, none of the four witnesses was able to give the police a description of the robbers' facial characteristics. Some five months later, on February 3, 1966, an FBI agent showed each of the four witnesses a group of black and white mug shots of the faces of five black males, including respondent, all of generally the same age, height, and weight. Respondent's photograph was included because of information received from a Government informant charged with other crimes.<sup>[2]</sup> None of the witnesses <span class="star-pagination">*327</span> was able to make a "positive" identification of respondent.<sup>[3]</sup></p>
<p>On April 1, 1966, an indictment was returned charging respondent and a codefendant in five counts relating to the robbery of the American Security and Trust Co. Trial was finally set for May 8, 1968, almost three years after the crime and more than two years after the return of the indictment. During the entire two-year period between indictment and trial, although one of the witnesses expressly sought an opportunity to see respondent in person, the Government never attempted to arrange a corporeal lineup for the purposes of identification. Rather, <i>less than 24 hours before trial,</i> the FBI agent, accompanied by the prosecutor, showed five color photographs to the witnesses, three of whom identified the picture of respondent.</p>
<p>At trial, all four witnesses made in-court identifications of respondent, but only one of these witnesses was "positive" of her identification. The fact that three of the witnesses had previously identified respondent from the color photographs, and the photographs themselves, were also admitted into evidence. The only other evidence <span class="star-pagination">*328</span> implicating respondent in the crime was the testimony of the Government informant.<sup>[4]</sup> On the basis of this evidence, respondent was convicted on all counts of the indictment.</p>
<p>On appeal, the United States Court of Appeals for the District of Columbia Circuit, sitting en banc, reversed respondent's conviction. 149 U. S. App. D. C. 1, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span> (1972). Noting that "the dangers of mistaken identification from uncounseled lineup identifications . . . are applicable in large measure to photographic as well as corporeal identifications,"<sup>[5]</sup> the Court of Appeals reasoned that this Court's decisions in <i>Wade, Gilbert,</i> and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> compelled the conclusion that a pretrial photographic identification, like a lineup, is a "critical" stage of the prosecution at which the accused is constitutionally entitled to the attendance of counsel. Accordingly, the Court of Appeals held that respondent was denied his Sixth Amendment right to "the Assistance of Counsel for his defence" when his attorney was not given an opportunity to attend the display of the color photographs on the very eve of trial.<sup>[6]</sup> In my view, both the reasoning and conclusion of the Court of Appeals were unimpeachably correct, and I would therefore affirm.</p>
<p></p>
<h2>II</h2>
<p>In June 1967, this Court decided a trilogy of "lineup" cases which brought into sharp focus the problems of <span class="star-pagination">*329</span> pretrial identification. See <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra</a></span></i><i>; </i><i>Gilbert</i> v. <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">California, supra</a></span></i><i>; </i><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i> In essence, those decisions held (1) that a pretrial lineup is a "critical stage" in the criminal process at which the accused is constitutionally entitled to the presence of counsel; (2) that evidence of an identification of the accused at such an uncounseled lineup is <i>per se</i> inadmissible; and (3) that evidence of a subsequent in-court identification of the accused is likewise inadmissible unless the Government can demonstrate by clear and convincing evidence that the in-court identification was based upon observations of the accused independent of the prior uncounseled lineup identification. The considerations relied upon by the Court in reaching these conclusions are clearly applicable to photographic as well as corporeal identifications. Those considerations bear repeating here in some detail, for they touch upon the very heart of our criminal justice systemthe right of an accused to a fair trial, including the effective "Assistance of Counsel for his defence."</p>
<p>At the outset, the Court noted that "identification evidence is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 228</a></span>. Indeed, "[t]he vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> Apart from "the dangers inherent in eyewitness identification," <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 235</a></span>, such as unreliable memory or perception, the Court pointed out that "[a] major factor contributing to the high incidence of miscarriage of justice from mistaken identification has been the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 228</a></span>. The Court recognized that the dangers of suggestion are not necessarily due to "police <span class="star-pagination">*330</span> procedures intentionally designed to prejudice an accused." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. On the contrary, "[s]uggestion can be created intentionally or unintentionally in many subtle ways." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 229</a></span>. And the "`fact that the police themselves have, in a given case, little or no doubt that the man put up for identification has committed the offense . . . involves a danger that this persuasion may communicate itself even in a doubtful case to the witness in some way . . . .'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>, quoting Williams &amp; Hammelmann, Identification Parades-I, [1963] Crim. L. Rev. 479, 483.</p>
<p>The Court also expressed concern over the possibility that a mistaken identification at a pretrial lineup might itself be conclusive on the question of identity, thereby resulting in the conviction of an innocent man. The Court observed that "`once a witness has picked out the accused at the line-up, he is not likely to go back on his word later on, so that in practice the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.'" <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 229</a></span>, quoting Williams &amp; Hammelmann, <i>supra,</i> at 482.</p>
<p>Moreover, "the defense can seldom reconstruct the manner and mode of lineup identification for judge or jury at trial." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 230</a></span>. For "as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups . . . ." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> Although the accused is present at such corporeal identifications, he is hardly in a position to detect many of the more subtle "improper influences" that might infect the identification.<sup>[7]</sup> In addition, the Court emphasized <span class="star-pagination">*331</span> that "neither witnesses nor lineup participants are apt to be alert for conditions prejudicial to the suspect. And, if they were, it would likely be of scant benefit to the suspect since neither witnesses nor lineup participants are likely to be schooled in the detection of suggestive influences." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> As a result, "even though cross-examination is a precious safeguard to a fair trial, it cannot [in this context] be viewed as an absolute assurance of accuracy and reliability." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>.</p>
<p>With these considerations in mind, the Court reasoned that "the accused's inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness' courtroom identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#231" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 231-232</a></span>. And "[i]nsofar as the accused's conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. Thus, noting that "presence of counsel [at the lineup] can often avert prejudice and assure a meaningful confrontation at trial," the Court concluded that a pretrial corporeal identification is "a critical stage of the prosecution at which [the accused is] `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 236, 237</a></span>, quoting <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span> (1932).</p>
<p></p>
<h2>
<span class="star-pagination">*332</span> III</h2>
<p>As the Court of Appeals recognized, "the dangers of mistaken identification . . . set forth in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> are applicable in large measure to photographic as well as corporeal identifications." 149 U. S. App. D. C., at 9, 461 F. 2d, at 100. To the extent that misidentification may be attributable to a witness' faulty memory or perception, or inadequate opportunity for detailed observation during the crime, the risks are obviously as great at a photographic display as at a lineup.<sup>[8]</sup> But "[b]ecause of the inherent limitations of photography, which presents its subject in two dimensions rather than the three dimensions of reality, . . . a photographic identification, even when properly obtained, is clearly inferior to a properly obtained corporeal identification." P. Wall, Eye-Witness Identification in Criminal Cases 70 (1965). Indeed, noting "the hazards of initial identification by photograph," we have expressly recognized that "a corporeal identification. . . is normally more accurate" than a photographic identification. <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 384</a></span>, 386 n. 6 (1968).<sup>[9]</sup> Thus, in this sense at <span class="star-pagination">*333</span> least, the dangers of misidentification are even greater at a photographic display than at a lineup.</p>
<p>Moreover, as in the lineup situation, the possibilities for impermissible suggestion in the context of a photographic display are manifold. See <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 383</a></span>. Such suggestion, intentional or unintentional, may derive from three possible sources. First, the photographs themselves might tend to suggest which of the pictures is that of the suspect. For example, differences in age, pose, or other physical characteristics of the persons represented, and variations in the mounting, background, lighting, or markings of the photographs all might have the effect of singling out the accused.<sup>[10]</sup></p>
<p>Second, impermissible suggestion may inhere in the manner in which the photographs are displayed to the witness. The danger of misidentification is, of course, "increased if the police display to the witness . . . the pictures of several persons among which the photograph of a single such individual recurs or is in some way emphasized." <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Ibid.</a></span></i> And, if the photographs are arranged in an asymmetrical pattern, or if they are displayed in a time sequence that tends to emphasize a particular photograph, "any identification of the photograph which stands out from the rest is no more reliable than an identification of a single photograph, exhibited alone." P. Wall, <i>supra,</i> at 81.</p>
<p>Third, gestures or comments of the prosecutor at the time of the display may lead an otherwise uncertain <span class="star-pagination">*334</span> witness to select the "correct" photograph. For example, the prosecutor might "indicate to the witness that [he has] other evidence that one of the persons pictured committed the crime,"<sup>[11]</sup> and might even point to a particular photograph and ask whether the person pictured "looks familiar." More subtly, the prosecutor's inflection, facial expressions, physical motions, and myriad other almost imperceptible means of communication might tend, intentionally or unintentionally, to compromise the witness' objectivity. Thus, as is the case with lineups, "[i]mproper photographic identification procedures,. . . by exerting a suggestive influence upon the witnesses, can often lead to an erroneous identification. . . ." P. Wall, <i>supra,</i> at 89.<sup>[12]</sup> And "[r]egardless of how the initial misidentification comes about, the witness <span class="star-pagination">*335</span> thereafter is apt to retain in his memory the image of the photograph rather than of the person actually seen . . . ." <i>Simmons</i> v. <i>United States, supra,</i> at 383-384.<sup>[13]</sup> As a result, "`the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.'" <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 229</a></span>, quoting Williams &amp; Hammelmann, <i>supra,</i> at 482.</p>
<p>Moreover, as with lineups, the defense can "seldom reconstruct" at trial the mode and manner of photographic identification. It is true, of course, that the photographs used at the pretrial display might be preserved for examination at trial. But "it may also be said that a photograph can preserve the record of a lineup; yet this does not justify a lineup without counsel." 149 U. S. App. D. C., at 9-10, 461 F. 2d, at 100-101. Cf. <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span></i> at 239 and n. 30. Indeed, in reality, preservation of the photographs affords little protection to the unrepresented accused. For, although retention of the photographs may mitigate the dangers of misidentification due to the suggestiveness of the photographs themselves, it cannot in any sense reveal to defense counsel the more subtle, and therefore more dangerous, suggestiveness that might derive from the manner in which the photographs were displayed or any accompanying comments or gestures. Moreover, the accused cannot rely upon the witnesses themselves to expose these latter sources of suggestion, for the witnesses are not "apt to be alert for conditions prejudicial to the suspect. And if they were, it would likely be of scant benefit to the suspect" since the witnesses are hardly "likely to be schooled in the detection of suggestive influences." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 230</a></span>.</p>
<p><span class="star-pagination">*336</span> Finally, and <i>unlike</i> the lineup situation, the accused himself is not even present at the photographic identification, thereby reducing the likelihood that irregularities in the procedures will ever come to light. Indeed, in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> the Government itself observed:<sup>[14]</sup></p>
<blockquote>"When the defendant is presentas he is during a lineuphe may personally observe the circumstances, report them to his attorney, and (if he chooses to take the stand) testify about them at trial. . . . [I]n the absence of an accused, on the other hand, there is no one present to verify the fairness of the interview or to report any irregularities. If the prosecution were tempted to engage in `sloppy or biased or fraudulent' conduct . . ., it would be far more likely to do so when the accused is absent than when he himself is being `used.'"</blockquote>
<p>Thus, the difficulties of reconstructing at trial an uncounseled photographic display are at least equal to, and possibly greater than, those involved in reconstructing an uncounseled lineup.<sup>[15]</sup> And, as the Government argued <span class="star-pagination">*337</span> in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> in terms of the need for counsel, "[t]here is no meaningful difference between a witness' pretrial identification from photographs and a similar identification made at a lineup."<sup>[16]</sup> For, in both situations "the accused's inability effectively to reconstruct at trial any unfairness that occurred at the [pretrial identification] may deprive him of his only opportunity meaningfully to attack the credibility of the witness' courtroom identification." <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#231" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 231-232</a></span>. As <span class="star-pagination">*338</span> a result, both photographic and corporeal identifications create grave dangers that an innocent defendant might be convicted simply because of his inability to expose a tainted identification. This being so, considerations of logic, consistency, and, indeed, fairness compel the conclusion that a pretrial photographic identification, like a pretrial corporeal identification, is a "critical stage of the prosecution at which [the accused is] `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#237" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 237</a></span>, quoting <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 57</a></span>.</p>
<p></p>
<h2>IV</h2>
<p>Ironically, the Court does not seriously challenge the proposition that presence of counsel at a pretrial photographic display is essential to preserve the accused's right to a fair trial on the issue of identification. Rather, in what I can only characterize a triumph of form over substance, the Court seeks to justify its result by engrafting a wholly unprecedentedand wholly unsupportablelimitation on the Sixth Amendment right of "the accused . . . to have the Assistance of Counsel for his defence." Although apparently conceding that the right to counsel attaches, not only at the trial itself, but at all "critical stages" of the prosecution, see <i>ante,</i> at 309-311, the Court holds today that, in order to be deemed "critical," the particular "stage of the prosecution" under consideration must, at the very least, involve the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." According to the Court a pretrial photographic identification does not, of course, meet these criteria.</p>
<p>In support of this rather crabbed view of the Sixth Amendment, the Court cites our decisions in <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), <i>White</i> v. <i>Maryland,</i> 373 U. S. 59 <span class="star-pagination">*339</span> (1963), and <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961). Admittedly, each of these decisions guaranteed the assistance of counsel in pretrial proceedings at least arguably involving the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused required the "guiding hand of counsel."<sup>[17]</sup> Moreover, as the Court points out, these decisions are consistent with the view that the Sixth Amendment "embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel." <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938). But, contrary to the Court's assumption, this is merely one <i>facet</i> of the Sixth Amendment guarantee, and the decisions relied upon by the Court represent, not the boundaries of the right to counsel, but mere applications of a far broader and more reasoned understanding of the Sixth Amendment than that espoused today.</p>
<p>The fundamental premise underlying <i>all</i> of this Court's decisions holding the right to counsel applicable at "critical" pretrial proceedings, is that a "stage" of the prosecution must be deemed "critical" for the purposes of the Sixth Amendment if it is one at which the presence of counsel is necessary "to protect the fairness of <i>the trial itself." </i><i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#239" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., 218, 239</a></span> (1973) (emphasis added). Thus, in <i>Hamilton</i> v. <i>Alabama,</i> <span class="star-pagination">*340</span> <i>supra</i><i>,</i> for example, we made clear that an arraignment under Alabama law is a "critical stage" of the prosecution, not only because the accused at such an arraignment requires "the guiding hand of counsel," but, more broadly, because "[w]hat happens there may affect the whole trial." <i>Id.,</i> at 54. Indeed, to exclude counsel from a pretrial proceeding at which his presence might be necessary to assure the fairness of the subsequent trial would, in practical effect, render the Sixth Amendment guarantee virtually meaningless, for it would "deny a defendant `effective representation by counsel at the only stage when legal aid and advice would help him.'" <i>Massiah</i> v. <i>United States, supra,</i> at 204, quoting <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 326</a></span> (1959) (DOUGLAS, J., concurring); see <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#484" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 484-485</a></span> (1964).</p>
<p>This established conception of the Sixth Amendment guarantee is, of course, in no sense dependent upon the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." On the contrary, in <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932), the seminal decision in this area, we explicitly held the right to counsel applicable at a stage of the pretrial proceedings involving <i>none</i> of the three criteria set forth by the Court today. In <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span>,</i> the defendants in a state felony prosecution were not appointed counsel until the very eve of trial. This Court held, in no uncertain terms, that such an appointment could not satisfy the demands of the Sixth Amendment, for "`[i]t is vain . . . to guarantee [the accused] counsel without giving the latter any opportunity to acquaint himself with the facts or law of the case.'" <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#59" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 59</a></span>. In other words, <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span></i> made clear that, in order to preserve the accused's right to a fair trial and to "effective and substantial"<sup>[18]</sup> assistance <span class="star-pagination">*341</span> of counsel at that trial, the Sixth Amendment guarantee necessarily encompasses a reasonable period of time before trial during which counsel might prepare the defense. Yet it can hardly be said that this preparatory period of research and investigation involves the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel."</p>
<p>Moreover, despite the Court's efforts to rewrite <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> so as to suggest a precedential basis for its own analysis,<sup>[19]</sup> the rationale of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> lends no support whatever to today's decision. In <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> after concluding that compelled participation in a lineup does not violate the accused's right against self-incrimination,<sup>[20]</sup> the Court addressed the argument "that the assistance of counsel at the lineup was indispensable to protect Wade's most basic right as a criminal defendanthis right to a fair trial at which the witnesses against him might be meaningfully cross-examined." 388 U. S., at 223-224. The Court then surveyed the history of the Sixth Amendment, and specifically concluded that that Amendment guarantees "counsel's assistance <i>whenever</i> necessary to assure a meaningful `defence.'" <i>Id.,</i> at 225 (emphasis added). <span class="star-pagination">*342</span> Then, after examining this Court's prior decisions concerning the applicability of the counsel guarantee,<sup>[21]</sup> the Court stressed once again that a pretrial proceeding is a "critical stage" of the prosecution if "the presence of his counsel is necessary to preserve the defendant's basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself." <i>Id.,</i> at 227.</p>
<p>The Court next addressed the Government's contention that a lineup is "a mere preparatory step in the gathering of the prosecution's evidence, not differentfor Sixth Amendment purposesfrom various other preparatory steps, such as systematized or scientific analyzing of the accused's fingerprints, blood sample, clothing, hair, and the like." <i>Id.,</i> at 227. If the Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> had even the remotest intention of embracing the wooden interpretation of the Sixth Amendment ascribed to it today, it could have rejected the Government's contention simply by pointing out the obvious fact that such "systematized or scientific analyzing" does not in any sense involve the physical "presence of the accused," at a "trial-like confrontation" with the Government, at which the accused requires the "guiding hand of counsel." But the Court offered not even the slightest hint of such <span class="star-pagination">*343</span> an approach. Instead, the Court reasoned that, in light of the scientific nature of such analyses,</p>
<blockquote>"the accused has the opportunity for a meaningful confrontation of the Government's case at trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts. The denial of a right to have his counsel present at such analyses does not therefore violate the Sixth Amendment; <i>they are not critical stages since there is minimal risk that his counsel's absence at such stages might derogate from his right to a fair trial." Id.,</i> at 227-228 (emphasis added).</blockquote>
<p>Finally, after discussing the dangers of misidentification arising out of lineup procedures and the difficulty of reconstructing the lineup at trial, the Court noted that "[i]nsofar as the accused's conviction may rest on a court-room identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 235</a></span>. The Court therefore concluded that "[s]ince it appears that there is grave potential for prejudice, intentional or not, in the pretrial lineup, which may not be capable of reconstruction at trial, and since presence of counsel itself can often avert prejudice and assure a meaningful confrontation at trial, there can be little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was `as much entitled to such aid [of counsel] . . . as at the trial itself.'" <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 236-237</a></span>.</p>
<p>Thus, contrary to the suggestion of the Court, the conclusion in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> that a pretrial lineup is a "critical stage" of the prosecution did not in any sense turn on <span class="star-pagination">*344</span> the fact that a lineup involves the physical "presence of the accused" at a "trial-like confrontation" with the Government. And that conclusion most certainly did not turn on the notion that presence of counsel was necessary so that counsel could offer legal advice or "guidance" to the accused at the lineup. On the contrary, <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> envisioned counsel's function at the lineup to be primarily that of a trained observer, able to detect the existence of any suggestive influences and capable of understanding the legal implications of the events that transpire. Having witnessed the proceedings, counsel would then be in a position effectively to reconstruct at trial any unfairness that occurred at the lineup, thereby preserving the accused's fundamental right to a fair trial on the issue of identification.</p>
<p>There is something ironic about the Court's conclusion today that a pretrial lineup identification is a "critical stage" of the prosecution because counsel's presence can help to compensate for the accused's deficiencies as an observer, but that a pretrial photographic identification is not a "critical stage" of the prosecution because the accused is not able to observe at all. In my view, there simply is no meaningful difference, in terms of the need for attendance of counsel, between corporeal and photographic identifications. And applying established and well-reasoned Sixth Amendment principles, I can only conclude that a pretrial photographic display, like a pretrial lineup, is a "critical stage" of the prosecution at which the accused is constitutionally entitled to the presence of counsel.</p>
<h2>NOTES</h2>
<p>[1]  "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence."</p>
<p>[2]  <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#898" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 898-900</a></span> (CA2), cert. denied <i>sub nom. </i><i>Haywood</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./396/852/">396 U. S. 852</a></span> (1969); <i>United States ex rel. Reed</i> v. <i>Anderson,</i> <span class="citation" data-id="9458303"><a href="/opinion/303865/united-states-of-america-ex-rel-cleveland-reed-v-raymond-anderson/" aria-description="Citation for case: United States of America Ex Rel. Cleveland Reed v....">461 F. 2d 739</a></span> (CA3 1972) (en bane); <i>United States</i> v. <i>Collins,</i> <span class="citation" data-id="9454903"><a href="/opinion/286688/united-states-v-william-francis-collins/" aria-description="Citation for case: United States v. William Francis Collins">416 F. 2d 696</a></span> (CA4 1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1025/">396 U. S. 1025</a></span> (1970); <i>United States</i> v. <i>Ballard,</i> <span class="citation" data-id="288980"><a href="/opinion/288980/united-states-v-erwin-edward-ballard-united-states-of-america-v-richard/" aria-description="Citation for case: United States v. Erwin Edward Ballard, United States of...">423 F. 2d 127</a></span> (CA5 1970); <i>United States</i> v. <i>Serio,</i> <span class="citation" data-id="295836"><a href="/opinion/295836/united-states-v-august-serio-also-known-as-delbert-beard/#829" aria-description="Citation for case: United States v. August Serio, Also Known as Delbert Beard">440 F. 2d 827, 829-830</a></span> (CA6 1971); <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="283186"><a href="/opinion/283186/united-states-v-burnell-robinson/#67" aria-description="Citation for case: United States v. Burnell Robinson">406 F. 2d 64, 67</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./395/926/">395 U. S. 926</a></span> (1969); <i>United States</i> v. <i>Long,</i> <span class="citation" data-id="8886509"><a href="/opinion/8899737/united-states-v-long/#301" aria-description="Citation for case: United States v. Long">449 F. 2d 288, 301-302</a></span> (CA8 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/974/">405 U. S. 974</a></span> (1972); <i>Allen</i> v. <i>Rhay,</i> <span class="citation" data-id="292225"><a href="/opinion/292225/gordon-m-allen-and-v-b-j-rhay-superintendent-of-the-washington-state/#1166" aria-description="Citation for case: Gordon M. Allen, and v. B. J. Rhay, Superintendent of the...">431 F. 2d 1160, 1166-1167</a></span> (CA9 1970); <i>McGee</i> v. <i>United States,</i> <span class="citation" data-id="282032"><a href="/opinion/282032/floyd-lenox-mcgee-v-united-states/#436" aria-description="Citation for case: Floyd Lenox McGee v. United States">402 F. 2d 434, 436</a></span> (CA10 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/908/">394 U. S. 908</a></span> (1969). The en banc decision of the Third Circuit in <i>Anderson</i> overruled in part a panel decision in <i>United States</i> v. <i>Zeiler,</i> <span class="citation" data-id="290782"><a href="/opinion/290782/united-states-v-william-edward-zeiler-united-states-of-america-v-william/" aria-description="Citation for case: United States v. William Edward Zeiler, United States of...">427 F. 2d 1305</a></span> (CA3 1970).
</p>
<p>The question has also produced conflicting decisions in state courts. The majority view, as in the courts of appeals, rejects the claimed right, to counsel. See, <i>e. g., </i><i>McGhee</i> v. <i>State,</i> <span class="citation" data-id="1724451"><a href="/opinion/1724451/mcghee-v-state/" aria-description="Citation for case: McGhee v. State">48 Ala. App. 330</a></span>, <span class="citation" data-id="1724451"><a href="/opinion/1724451/mcghee-v-state/" aria-description="Citation for case: McGhee v. State">264 So. 2d 560</a></span> (Ala. Crim. App. 1972); <i>State</i> v. <i>Yehling,</i> <span class="citation" data-id="1353187"><a href="/opinion/1353187/state-v-yehling/" aria-description="Citation for case: State v. Yehling">108 Ariz. 323</a></span>, <span class="citation" data-id="1353187"><a href="/opinion/1353187/state-v-yehling/" aria-description="Citation for case: State v. Yehling">498 P. 2d 145</a></span> (1972); <i>People</i> v. <i>Lawrence,</i> <span class="citation" data-id="9552312"><a href="/opinion/1186833/people-v-lawrence/" aria-description="Citation for case: People v. Lawrence">4 Cal. 3d 273</a></span>, <span class="citation" data-id="9552312"><a href="/opinion/1186833/people-v-lawrence/" aria-description="Citation for case: People v. Lawrence">481 P. 2d 212</a></span> (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./407/909/">407 U. S. 909</a></span> (1972); <i>Reed</i> v. <i>State,</i> ___ Del. ___, <span class="citation" data-id="2061648"><a href="/opinion/2061648/reed-v-state/" aria-description="Citation for case: Reed v. State">281 A. 2d 142</a></span> (1971); <i>People</i> v. <i>Holiday,</i> <span class="citation" data-id="2087977"><a href="/opinion/2087977/the-people-v-holiday/" aria-description="Citation for case: The PEOPLE v. Holiday">47 Ill. 2d 300</a></span>, <span class="citation" data-id="2087977"><a href="/opinion/2087977/the-people-v-holiday/" aria-description="Citation for case: The PEOPLE v. Holiday">265 N. E. 2d 634</a></span> (1970); <i>Baldwin</i> v. <i>State,</i> <span class="citation" data-id="2172829"><a href="/opinion/2172829/baldwin-v-state/" aria-description="Citation for case: Baldwin v. State">5 Md. App. 22</a></span>, <span class="citation" data-id="2172829"><a href="/opinion/2172829/baldwin-v-state/" aria-description="Citation for case: Baldwin v. State">245 A. 2d 98</a></span> (1968) (dicta); <i>Commonwealth</i> v. <i>Ross,</i> ___ Mass. ___, <span class="citation" data-id="2133215"><a href="/opinion/2133215/commonwealth-v-ross/" aria-description="Citation for case: Commonwealth v. Ross">282 N. E. 2d 70</a></span> (1972), vacated on other grounds and remanded, <span class="citation multiple-matches"><a href="/c/U.%20S./410/901/">410 U. S. 901</a></span> (1973); <i>Stevenson</i> v. <i>State,</i> <span class="citation" data-id="1911421"><a href="/opinion/1911421/stevenson-v-state/" aria-description="Citation for case: Stevenson v. State">244 So. 2d 30</a></span> (Miss. 1971); <i>State</i> v. <i>Brookins,</i> <span class="citation" data-id="1534458"><a href="/opinion/1534458/state-v-brookins/" aria-description="Citation for case: State v. Brookins">468 S. W. 2d 42</a></span> (Mo. 1971) (dicta); <i>People</i> v. <i>Coles,</i> 34 App. Div. 2d 1051, 312 N. Y. S. 2d 621 (1970) (dicta); <i>State</i> v. <i>Moss,</i> <span class="citation" data-id="1710337"><a href="/opinion/1710337/state-v-moss/" aria-description="Citation for case: State v. Moss">187 Neb. 391</a></span>, <span class="citation" data-id="1710337"><a href="/opinion/1710337/state-v-moss/" aria-description="Citation for case: State v. Moss">191 N. W. 2d 543</a></span> (1971); <i>Drewry</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1241302"><a href="/opinion/1241302/dreway-v-commonwealth/" aria-description="Citation for case: DREWAY v. Commonwealth">213 Va. 186</a></span>, <span class="citation" data-id="1241302"><a href="/opinion/1241302/dreway-v-commonwealth/" aria-description="Citation for case: DREWAY v. Commonwealth">191 S. E. 2d 178</a></span> (1972); <i>State</i> v. <i>Nettles,</i> <span class="citation" data-id="9793951"><a href="/opinion/2616794/state-v-nettles/" aria-description="Citation for case: State v. Nettles">81 Wash. 2d 205</a></span>, <span class="citation" data-id="9793951"><a href="/opinion/2616794/state-v-nettles/" aria-description="Citation for case: State v. Nettles">500 P. 2d 752</a></span> (1972); <i>Kain</i> v. <i>State,</i> <span class="citation" data-id="1838693"><a href="/opinion/1838693/kain-v-state/" aria-description="Citation for case: Kain v. State">48 Wis. 2d 212</a></span>, <span class="citation multiple-matches"><a href="/c/N.%20W.%202d/179/777/">179 N. W. 2d 777</a></span> (1970). Cf. <i>State</i> v. <i>Accor,</i> <span class="citation" data-id="1206841"><a href="/opinion/1206841/state-v-accor/" aria-description="Citation for case: State v. Accor">277 N. C. 65</a></span>, <span class="citation" data-id="1206841"><a href="/opinion/1206841/state-v-accor/" aria-description="Citation for case: State v. Accor">175 S. E. 2d 583</a></span> (1970). Several state courts, however, have granted a right to counsel at photographic identifications. See, <i>e. g., </i><i>Cox</i> v. <i>State,</i> <span class="citation" data-id="1758004"><a href="/opinion/1758004/cox-v-state/" aria-description="Citation for case: Cox v. State">219 So. 2d 762</a></span> (Fla. App. 1969) (video tapes); <i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">389 Mich. 155</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">205 N. W. 2d 461</a></span> (1973); <i>Thompson</i> v. <i>State,</i> <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">85 Nev. 134</a></span>, <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">451 P. 2d 704</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/893/">396 U. S. 893</a></span> (1969); <i>Commonwealth</i> v. <i>Whiting,</i> <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">439 Pa. 205</a></span>, <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">266 A. 2d 738</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/919/">400 U. S. 919</a></span> (1970).</p>
<p>[3]  Respondent Ash does not assert a right to counsel at the black-and-white photographic display in February 1966 because he recognizes that <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), forecloses application of the Sixth Amendment to events before the initiation of adversary criminal proceedings. Tr. of Oral Arg. 21-22; Brief for Respondent 32 n. 21.</p>
<p>[4]  At this hearing both the black-and-white and color photographs were introduced as exhibits. App. 44. The FBI agents who conducted the pretrial displays were called as witnesses and were cross-examined fully. App. 10, 28. Two of the four witnesses who were expected to make in-court identifications also testified and were cross-examined concerning the photographic identifications. App. 55, 65.</p>
<p>[5]  The majority of the Court of Appeals concluded that Ash's counsel properly had preserved his objection to introduction of the photographs. 149 U. S. App. D. C., at 6 n. 6, 461 F. 2d, at 97 n. 6. Although the contrary view of the dissenting judges has been noted here by the Government, the majority's ruling on this issue is not asserted by the Government as a basis for reversal. Pet. for Cert. 4 n. 5; Brief for United States 6 n. 6. Under these circumstances, we are not inclined to disturb the ruling of the Court of Appeals on this close procedural question. App. 104, 126-131.</p>
<p>[6]  Although the English limitation was not expressly rejected until 1836, the rule appears to have been relaxed in practice. 9 W. Holdsworth, History of English Law 235 (1926); 4 W. Blackstone, Commentaries *355-356.</p>
<p>[7]  Similar concerns eventually led to abandonment of the common-law rule in England. That rule originated at a time when counsel was said to be "hardly necessary" because expert knowledge of the law was not required at trial and systematic examination of witnesses had not yet developed. T. Plucknett, A Concise History of the Common Law 410 (4th ed. 1948).
</p>
<p>Confrontation with legal technicalities became common at English trials when complex rules developed for attacking the indictment. <i>Ibid.</i> The English response was not an unlimited right to counsel, however, but was rather a right for counsel to argue only legal questions. See <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60</a></span> (1932). A plea in abatement directed at insufficiency of the indictment, for example, allowed a prisoner to "pray counsel to be assigned to him to manage his exceptions and take more." 2 M. Hale, Pleas of the Crown 236 (1736).</p>
<p>Confrontation with a professional prosecutor arose in English treason trials before it appeared in ordinary criminal trials. See 1 J. Stephen, History of the Criminal Law of England 348-350 (1883). In 1695 this imbalance in the adversary process was corrected by a statute granting prisoners the right to counsel at treason trials. <span class="citation no-link">7 Win. 3</span>, c. 3 (1695). Hawkins explained that the professional ability of king's counsel motivated this reform because it had "been found by experience that prisoners have been often under great disadvantages from the want of counsel, in prosecutions of high treason against the king's person, which are generally managed for the crown with greater skill and zeal than ordinary prosecutions. . . ." 2 W. Hawkins, Pleas of the Crown 566 (Leach ed. 1787). The 1695 statute weakened the English rule and, after a century of narrowing practical application, see n. 6, <i>supra,</i> the rule was finally abrogated by statute in 1836. The Trials for Felony Act, 6 &amp; 7 Wm. 4, c. 114 (1836).</p>
<p>[8]  "[T]he dangers of mistaken identification from uncounseled lineup identifications set forth in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> are applicable in large measure to photographic as well as corporeal identifications. These include, notably, the possibilities of suggestive influence or mistakeparticularly where witnesses had little or no opportunity for detailed observation during the crime; the difficulty of reconstructing suggestivityeven greater when the defendant is not even present; the tendency of a witness's identification, once given under these circumstances, to be frozen. While these difficulties may be somewhat mitigated by preserving the photograph shown, it may also be said that a photograph can preserve the record of a lineup; yet this does not justify a lineup without counsel. The same may be said of the opportunity to examine the participants as to what went on in the course of the identification, whether at lineup or on photograph. Sometimes this may suffice to bring out all pertinent facts, even at a lineup, but this would not suffice under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> to offset the constitutional infringement wrought by proceeding without counsel. The presence of counsel avoids possibilities of suggestiveness in the manner of presentation that are otherwise ineradicable." 149 U. S. App. D. C., at 9-10, 461 F. 2d, at 100-101.</p>
<p>[9]  The Court rather narrowly defined the issues under consideration:
</p>
<p>"The pretrial <i>confrontation</i> for purpose of identification may take the form of a lineup, also known as an `identification parade' or `showup,' as in the present case, or presentation of the suspect alone to the witness, as in <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i> It is obvious that risks of suggestion attend either form of <i>confrontation</i> . . . . But as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups and <i>other forms of identification confrontations." </i><i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 229-230</a></span> (1967) (emphasis added).</p>
<p>The photographic identification could hardly have been overlooked by inadvertence since the Government stressed the similarity between lineups and photographic identifications. Brief for United States in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> No. 334, O. T. 1966, pp. 7, 14, 19, 24.</p>
<p>[10]  Duplication by defense counsel is a safeguard that normally is not available when a formal confrontation occurs. Defense counsel has no statutory authority to conduct a preliminary hearing, for example, and defense counsel will generally be prevented by practical considerations from conducting his own lineup. Even in some confrontations, however, the possibility of duplication may be important. The Court noted this in holding that the taking of handwriting exemplars did not constitute a "critical stage":
</p>
<p>"If, for some reason, an unrepresentative exemplar is taken, this can be brought out and corrected through the adversary process at trial since the accused can make an unlimited number of additional exemplars for analysis and comparison by government and defense handwriting experts." <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#267" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 267</a></span> (1967).</p>
<p>[11]  We do not suggest, of course, that defense counsel has any greater freedom than the prosecution to abuse the photographic identification. Evidence of photographic identifications conducted by the defense may be excluded as unreliable under the same standards that would be applied to unreliable identifications conducted by the Government.</p>
<p>[12]  The Court of Appeals deemed it significant that a photographic identification is admissible as substantive evidence, whereas other parts of interviews may be introduced only for impeachment. 149 U. S. App. D. C., at 10, 461 F. 2d, at 101. In this case defense counsel for Bailey introduced the inability to identify, and that was received into evidence. Thus defense counsel still received benefits equivalent to those available to the prosecution. Although defense counsel may be concerned that repeated photographic displays containing the accused's picture as the only common characteristic will tend to promote identification of the accused, the defense has other balancing devices available to it, such as the use of a sufficiently large number of photographs to counteract this possibility.</p>
<p>[13]  Although the reliability of in-court identifications and the effectiveness of impeachment may be improved by equality of access, we do not suggest that the prosecution's photographic identification would be more easily reconstructed at trial simply because defense counsel could conduct his own photographic display. But, as we have explained, <i>supra,</i> at 315-316, the possibility of perfect reconstruction is relevant to the evaluation of substitutes for counsel, not to the initial designation of an event as a "critical stage."</p>
<p>[14]  Sobel, Assailing the Impermissible Suggestion: Evolving Limitations on the Abuse of Pre-Trial Criminal Identification Methods, 38 Brooklyn L. Rev. 261, 299 (1971); Comment, 43 N. Y. U. L. Rev. 1019, 1022 (1968); Note, 2 Rutgers Camden L. J. 347, 359 (1970); Note, <span class="citation no-link">21 Syracuse L. Rev. 1235</span>, 1241-1242 (1970). A variant of this argument is that photographic identifications may be used to circumvent the need for counsel at lineups. Brief for Respondent 44-45.</p>
<p>[15]  <i>E. g.,</i> P. Wall, Eye-Witness Identification in Criminal Cases 77-85 (1965); Sobel, <i>supra,</i> n. 14, at 309-310; Comment, <span class="citation no-link">56 Iowa L. Rev. 408</span>, 420-421 (1970).</p>
<p>[16]  Throughout a criminal prosecution the prosecutor's ethical responsibility extends, of course, to supervision of any continuing investigation of the case. By prescribing procedures to be used by his agents and by screening the evidence before trial with a view to eliminating unreliable identifications, the prosecutor is able to minimize abuse in photographic displays even if they are conducted in his absence.</p>
<p>[*]  I do not read <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> as requiring counsel because a lineup is a "trial-type" situation, nor do I understand that the Court required the presence of an attorney because of the advice or assistance he could give to his client at the lineup itself. Rather, I had thought the reasoning of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> was that the right to counsel is essentially a protection for the defendant at trial, and that counsel is necessary at a lineup in order to ensure a meaningful confrontation and the effective assistance of counsel at trial.</p>
<p>[1]  See <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972).</p>
<p>[2]  At the time of respondent's trial, the informant, one Clarence McFarland, was serving a sentence for bank robbery. According to the Court of Appeals, "McFarland had been before the grand jury with regard to five separate offenses, in addition to his bank robbery, and had not been indicted on any of them, including one in which he had confessed guilt. The Assistant United States Attorney had arranged to have McFarland transferred from the D. C. Jail to a local jail in Rockville, Maryland, and in addition had helped McFarland's wife move from Southeast Washington to an apartment near the parochial school that McFarland's children were due to attend. 149 U. S. App. D. C. 1, 6 n. 7, <span class="citation" data-id="9458278"><a href="/opinion/303766/united-states-v-charles-j-ash-jr/" aria-description="Citation for case: United States v. Charles J. Ash, Jr.">461 F. 2d 92</a></span>, 97 n. 7 (1972). The Assistant United States Attorney also testified that he "had indicated he would testify before the parole board in McFarland's behalf." <i>Id.,</i> at 6, 461 F. 2d, at 97.</p>
<p>[3]  Respondent does not contend that he was denied his Sixth Amendment right to counsel at the pre-indictment display of the black and white photographs. Tr. of Oral Arg. 21-22; Brief for Respondent 32 n. 21.</p>
<p>[4]  As the Court of Appeals noted, this testimony was of at least questionable credibility. See n. 2, <i>supra.</i></p>
<p>[5]  149 U. S. App. D. C., at 9, 461 F. 2d, at 100.</p>
<p>[6]  The Court of Appeals also noted "that there are at the very least strong elements of suggestiveness in this color photo confrontation," and that "it is hard to see how the Government can be held to have shown, by clear and convincing evidence, that these color photographs did not affect the in-court identification made one day later." <i>Id.,</i> at 7, 14 n. 20, 461 F. 2d, at 98, 105 n. 20.</p>
<p>[7]  The Court pointed out that "[i]mproper influences may go undetected by a suspect, guilty or not, who experiences the emotional tension which we might expect in one being confronted with potential accusers. Even when he does observe abuse, if he has a criminal record he may be reluctant to take the stand and open up the admission of prior convictions. Moreover, any protestations by the suspect of the fairness of the lineup made at trial are likely to be in vain; the jury's choice is between the accused's unsupported version and that of the police officers present." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#230" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 230-231</a></span> (1967).</p>
<p>[8]  Thus, "[a] witness may have obtained only a brief glimpse of a criminal, or may have seen him under poor conditions. Even if the police subsequently follow the most correct photographic identification procedures . . . there is some danger that the witness may make an incorrect identification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 383</a></span> (1968).</p>
<p>[9]  See also Sobel, Assailing the Impermissible Suggestion: Evolving Limitations on the Abuse of Pre-Trial Criminal Identification Methods, 38 Brooklyn L. Rev. 261, 264, 296 (1971); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 531; Comment, Photographic Identification: The Hidden Persuader, <span class="citation no-link">56 Iowa L. Rev. 408</span>, 419 (1970); Note, Pretrial Photographic IdentificationA "Critical Stage" of Criminal Proceedings?, <span class="citation no-link">21 Syracuse L. Rev. 1235</span>, 1241 (1970). Indeed, recognizing the superiority of corporeal to photographic identifications, English courts have long held that once the accused is in custody, pre-lineup photographic identification is "indefensible" and grounds for quashing the conviction. <i>Rex</i> v. <i>Haslam,</i> 19 Crim. App. Rep. 59, 60 (1925); <i>Rex</i> v. <i>Goss,</i> 17 Crim. App. Rep. 196, 197 (1923). See also P. Wall, Eye-Witness Identification in Criminal Cases 71 (1965).</p>
<p>[10]  See, <i>e. g.,</i> Comment, <i>supra,</i> n. 9, at 410-411; Note, Criminal ProcedurePhoto-Identification<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> Prospectivity Rule Invoked to Avoid Extension of Right to Counsel, 43 N. Y. U. L. Rev. 1019, 1021 (1968).</p>
<p>[11]  <i>Simmons</i> v. <i>United States, supra,</i> at 383.</p>
<p>[12]  The Court maintains that "the ethical responsibility of the prosecutor" is in itself a sufficient "safeguard" against impermissible suggestion at a photographic display. See <i>ante,</i> at 320. The same argument might, of course, be made with respect to lineups. Moreover, it is clear that the "prosecutor" is not always present at such pretrial displays. Indeed, in this very case, one of the four eyewitnesses was shown the color photographs on the morning of trial by an agent of the FBI, <i>not</i> in the presence of the "prosecutor." See 149 U. S. App. D. C., at 5, 461 F. 2d, at 96. And even though "the ethical responsibility of the prosecutor" might be an adequate "safeguard" against <i>intentional</i> suggestion, it can hardly be doubted that a "prosecutor" is, after all, only human. His behavior may be fraught with wholly <i>unintentional</i> and indeed unconscious nuances that might effectively suggest the "proper" response. See P. Wall, <i>supra,</i> n. 9, at 26-65; Napley, Problems of Effecting the Presentation of the Case for a Defendant, 66 Col. L. Rev. 94, 98-99 (1966); Williams &amp; Hammelmann, Identification Parades-I, [1963] Crim. L. Rev. 479, 483. See also <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><i>Wade,</i> supra, at 229, 235, 236</a></span>. And, of course, as <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> itself makes clear, unlike other forms of unintentional prosecutorial "manipulation," even unintentional suggestiveness at an identification procedure involves serious risks of "freezing" the witness' mistaken identification and creates almost insurmountable obstacles to reconstruction at trial.</p>
<p>[13]  See also P. Wall, <i>supra,</i> n. 9, at 68; Napley, <i>supra,</i> n. 12, at 98-99; Williams &amp; Hammelmann, <i>supra,</i> n. 12, at 484; Comment, <i>supra,</i> n. 9, at 411-413; Note, <i>supra,</i> n. 10, at 1023.</p>
<p>[14]  Brief for United States 24-25 in <i>United States</i> v. <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i><i>,</i> No. 334, O. T. 1966.</p>
<p>[15]  The Court's assertion, <i>ante,</i> at 317-319 and n. 10, that these difficulties of reconstruction are somehow minimized because the defense can "duplicate" a photographic identification reflects a complete misunderstanding of the issues in this case. Aside from the fact that lineups can also be "duplicated," the Court's assertion is wholly inconsistent with the underlying premises of both <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for cas

[...TRUNCATED 8784 of 128784 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
