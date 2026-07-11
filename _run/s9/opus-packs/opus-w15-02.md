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

## GROUP: _overhaul2/lake/cases/United States v. Chavez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Chavez
type: case
citation: "534 F.3d 1338 (2008)"
parallel_cite: ""
neutral_cite: "2008 U.S. App. LEXIS 16558; 2008 WL 2893057"
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2008
date_decided: 2008-07-29
docket: 07-3389
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/171034/united-states-v-chavez/"
  cluster_id: 171034
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Chavez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: Key
related:
  - "[[Collective Knowledge and the Fellow-Officer Rule]]"
  - "[[Whren v. United States]]"
  - "[[Terry v. Ohio]]"
tags:
  - case
  - fourth-amendment
  - collective-knowledge
  - fellow-officer-rule
  - imputed-probable-cause
  - traffic-stop
  - tenth-circuit
holding: "Under the collective-knowledge doctrine, probable cause held by the DEA task force that investigated and arranged a controlled cocaine buy could be imputed to the patrolman the task force directed to stop the suspect's vehicle, even though the patrolman himself was not privy to the investigation's details; the stop and search were therefore justified and suppression was properly denied."
aliases:
  - United States v. Chavez
  - "United States v. Chavez (10th Cir. 2008)"
---

# United States v. Chavez

*534 F.3d 1338 (10th Cir. 2008)* · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 171034 → majority opinion 171034 (Ebel, J.; 534 F.3d 1338, decided July 29, 2008). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (illegal-reentry sentencing Chavez) to the intended fellow-officer/collective-knowledge Chavez; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text (near reporter star `*1342`) — S9 verifies the exact star page. -->

## Background
A DEA task force spent months investigating Servando Moreno and, through a confidential source, arranged to buy a kilogram of cocaine from him. On the day of the deal, agents surveilled Moreno leaving with a driver — Victor Chavez — in a white pickup, then directed New Mexico State Police Patrolman Chavez to stop the truck, giving him the plate, description, and occupant count but telling him to develop his own basis and that the truck was carrying "coke." The patrolman stopped and searched the truck, finding a kilogram of cocaine hidden in a bucket of nails. Chavez argued the patrolman lacked probable cause because he was not privy to the DEA investigation; the district court denied suppression.

## Issue
Whether the stop and search were justified under the collective-knowledge doctrine when the probable cause was developed by the investigating DEA task force rather than the officer who executed the stop.

## Rule
The central question was "whether the patrolman's stop and search of Mr. Chavez's vehicle was justified under the 'collective knowledge' doctrine," and the court concluded that it was. The investigating team's probable cause is imputed to the officer it directs to act, whose own subjective knowledge need not independently satisfy the standard. Analyzing the issue in two steps, the court held: "asking first whether the DEA task force agents had probable cause to believe Mr. Chavez's vehicle contained narcotics. They did. Second, we query whether the DEA task force's probable cause could be imputed to Patrolman Chavez. It could, in light of *Zamudio-Carrillo*." — 534 F.3d at 1342. ^pin-1342

## Application
The DEA had probable cause built from a controlled buy, monitored calls, and continuous surveillance tracking the cocaine from Moreno's supplier to the white pickup Chavez drove. That probable cause was imputed to Patrolman Chavez when the task force directed him to stop the identified vehicle; his lack of personal knowledge of the investigation's particulars did not defeat the stop. The search that followed was therefore lawful.

## Conclusion
**Affirmed.** Judge Ebel wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Chavez* is a leading circuit statement of the *[[Collective Knowledge and the Fellow-Officer Rule]]*: an investigating team's probable cause is imputed to the officer it instructs to make the stop, so the acting officer need not personally possess the facts — the vertical-imputation branch of the doctrine.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key*

## Sources
- [*United States v. Chavez*, 534 F.3d 1338 (10th Cir. 2008)](https://www.courtlistener.com/opinion/171034/united-states-v-chavez/) — pinpoint: 534 F.3d at 1342 (collective-knowledge doctrine; the investigating task force's probable cause imputed to the directed stopping officer). Rule quote string-matched to the CL opinion text 2026-07-07 (near reporter star `*1342`).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "606624120a6672b8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Chavez"}, "payload": {"all": [{"cite": "534 F.3d 1338", "page": "1338", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "534"}, {"cite": "2008 U.S. App. LEXIS 16558", "page": "16558", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2008"}, {"cite": "2008 WL 2893057", "page": "2893057", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2008"}], "display": "534 F.3d 1338", "official": {"cite": "534 F.3d 1338", "page": "1338", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "534"}, "official_selection_present": true, "record_id": "United States v. Chavez"}}
{"assertion_id": "144950aba7e27044", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Chavez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Chavez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Chavez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Chavez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Chavez",
    "case_name_short": "Chavez",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Victor CHAVEZ, Defendant-Appellant",
    "input_case_name": "United States v. Chavez",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2008-07-29",
    "year": 2008,
    "docket": "07-3389",
    "cluster_id": 171034,
    "lead_opinion_id": 171034,
    "sibling_ids": [],
    "absolute_url": "/opinion/171034/united-states-v-chavez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "534 F.3d 1338",
      "volume": "534",
      "reporter": "F.3d",
      "page": "1338",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. App. LEXIS 16558",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "16558",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 2893057",
        "volume": "2008",
        "reporter": "WL",
        "page": "2893057",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "534 F.3d 1338",
        "volume": "534",
        "reporter": "F.3d",
        "page": "1338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. App. LEXIS 16558",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "16558",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 2893057",
        "volume": "2008",
        "reporter": "WL",
        "page": "2893057",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "534 F.3d 1338",
    "official_selection": {
      "court_class": "coa",
      "selected": "534 F.3d 1338",
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
    "date_created": "2026-07-07T18:16:12Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-chavez--171034",
      "to_record_id": "United States v. Chavez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Chavez

```
                                                                     FILED
                                                          United States Court of Appeals
                                                                  Tenth Circuit

                                                                 July 29, 2008
                                                             Elisabeth A. Shumaker
                                                                 Clerk of Court
                                    PUBLISH

                   UNITED STATES COURT OF APPEALS

                                TENTH CIRCUIT


 UNITED STATES OF AMERICA,

       Plaintiff – Appellee,
 v.
                                                       No. 07-2008
 VICTOR CHAVEZ,

       Defendant – Appellant.


                 Appeal from the United States District Court
                        for the District of New Mexico
                      (D.C. No. 1:06-CR-00264-MCA)


Arturo B. Nieto, Albuquerque, NM, for Defendant-Appellant Victor Chavez.

Gregory J. Fouratt, Assistant United States Attorney (Larry Gomez, Acting
United States Attorney, with him on the brief) for Plaintiff-Appellee United
States of America.


Before HARTZ, EBEL and TYMKOVICH, Circuit Judges.


EBEL, Circuit Judge.


      During a search of Defendant-Appellant Victor Chavez’s pick-up truck, a

New Mexico State Police patrolman discovered approximately 1 kilogram of

cocaine in a bucket covered with nails. Mr. Chavez eventually entered a
conditional guilty plea to one count of conspiracy to commit possession with

intent to distribute more than 500 grams of cocaine, in violation of 21 U.S.C. §§

841(a)(1) & 841(b)(1)(B) and 846, and one count of possession with intent to

distribute more than 500 grams of cocaine, in violation of 21 U.S.C. § 841(a)(1)

& (b)(1)(B). He conditioned his plea on the right to challenge on appeal the

district court’s decision not to suppress the narcotics evidence as fruits of an

illegal stop and search.

      The patrolman who pulled Mr. Chavez over was instructed to do so by a

Drug Enforcement Agency (“DEA”) task force officer. Prior to the traffic stop, a

DEA task force had investigated and conducted surveillance of Servando Moreno,

the passenger in Mr. Chavez’s pick-up at the time of the stop. More to the point,

the DEA had, through a confidential source, arranged to purchase 1 kilo of

cocaine from Mr. Moreno on the day of the stop. Based on its investigation, the

DEA directed the patrolman to stop and search Mr. Chavez’s vehicle. Mr. Chavez

contends that the patrolman lacked probable cause because he was not privy to

the details of the DEA investigation. The central question presented here is

whether the patrolman’s stop and search of Mr. Chavez’s vehicle was justified

under the “collective knowledge” doctrine. We conclude that it was. Exercising

jurisdiction under 28 U.S.C. § 1291, we affirm.




                                         -2-
I.    BACKGROUND

      A. The Sting

      After a months-long investigation, the DEA set in motion a sting operation

targeting Mr. Moreno on January 18, 2006. Serving as an intermediary, a

confidential source (“CS”) who had previously proven to be reliable, 1 made a

series of monitored telephone calls 2 to Mr. Moreno and indicated that a buyer

from Amarillo, Texas, was interested in purchasing 1 kilo of cocaine. As

negotiated by Mr. Moreno and the CS, the transaction was to occur at a truck stop

in Santa Rosa, New Mexico (a location between Amarillo and Albuquerque).

When Agent Maudlin spoke with the CS on the evening of January 18, the CS

confirmed the location, price, and other logistical details of the drug deal, and

also noted that Mr. Moreno had indicated that “he was going to get a driver to

take him” from Albuquerque to Santa Rosa. 3




      1
       During the suppression hearing, Agent Jeff Maudlin and DEA Task Force
Officer (“TFO”) Jeramy Melton averred that the CS had proven himself reliable
during past investigations. The district court found this testimony credible.
      2
       On January 19, the CS spent the day with TFO Melton in a secure location.
Melton monitored each communication between the CS and Mr. Moreno during
the course of the day, and reported the content of those communications to his
fellow task force officers.
      3
       While Mr. Moreno refused to tell the CS the driver’s name, he did give the
CS the driver’s telephone number. Agent Maudlin cross-checked the number and
learned it was assigned to Victor Chavez.

                                        -3-
         B. The Surveillance

         The next morning, January 19, Agent Maudlin and Task Force Officer

(“TFO”) James Mowduk staked out Mr. Moreno’s trailer home in Albuquerque.

Around 9:20 a.m., the CS called Mr. Moreno to check on the status of the deal,

and Mr. Moreno indicated that the deal was on, but that he was still at home. Just

a few minutes later, a man matching Mr. Moreno’s description left the trailer

carrying a small duffel bag, got in a burnt orange truck customarily driven by

Moreno, and drove to 319 Riverside, a home located in the South Valley area of

Albuquerque. The DEA agents followed the burnt orange pick-up to the

Riverside residence. After arriving at 319 Riverside, the orange truck

disappeared behind a stucco fence paralleling a driveway that led behind the

house.

         Approximately fifteen minutes later, a white pick-up truck left 319

Riverside. The DEA agents followed the truck to a gas station, where they

ascertained that two individuals were in the truck. One matched Mr. Moreno’s

description and the other, as it turned out, was Mr. Chavez. While the white truck

was at the gas station, the DEA team instructed the CS to telephone Mr. Moreno

again. Mr. Moreno told the CS that he was just leaving Albuquerque en route to

Santa Rosa. A few minutes later, the two individuals left the gas station, headed

north on I-25, and then took eastbound I-40 towards Santa Rosa. The DEA




                                          -4-
agents, including Agent Maudlin and TFO Mowduk, continued their surreptitious

pursuit.

      C. The Stop

      As members of the DEA task force followed the white pick-up onto I-40,

TFO Mowduk called Patrolman Arcenio Chavez, 4 a canine officer with the New

Mexico State Police. The day before, in preparation for the sting operation, TFO

Mowduk had confirmed with Patrolman Chavez that Chavez would be on duty the

following day with his canine partner, Chica. TFO Mowduk then informed him

that the DEA task force wanted him to perform a traffic stop the next day.

      During their conversation on the morning of January 19, TFO Mowduk

provided Patrolman Chavez with the “plate number, the vehicle description, the

number of occupants,” and a description of the white pick-up truck that the DEA

wanted him to stop. TFO Mowduk also advised the patrolman that he would have

to develop his own probable cause for stopping the vehicle because the occupants

were wearing seat-belts and appeared to be observing traffic laws. Lastly, in

response to Patrolman Chavez’s queries, TFO Mowduk stated that the white pick-

up was carrying “coke” and that he didn’t know whether the occupants were

armed.




      4
      There is no indication in the record that Patrolman Chavez is related to the
Defendant-Appellant.

                                       -5-
      When TFO Mowduk called, Patrolman Chavez was waiting on the median

of I-40 east of Albuquerque. He eventually located the white pick-up, and

engaged his emergency equipment. 5 After the white pick-up truck pulled over, a

charade of sorts took place. Patrolman Chavez pretended that he had stopped Mr.

Chavez for failing to turn on his headlights in a safety corridor – a failure that the

patrolman in fact believed at the time of the stop was an infraction of New

Mexico’s regulations. 6 As such, he followed his routine traffic stop procedure,

asking first for Mr. Chavez’s license, registration, and proof of insurance.

Patrolman Chavez filled out a citation for the headlight infraction and for Mr.

Chavez’s failure to provide proof of insurance. After asking Mr. Chavez and Mr.

Moreno routine questions about their travel plans, Patrolman Chavez returned Mr.

Chavez’s license and registration and stated that Mr. Chavez and Mr. Moreno

were free to leave.




      5
        The patrolman’s police car was equipped with a recording camera, and a
video was made of the traffic stop. Neither party adduced either the videotape or
the transcript of that tape as part of the Record on Appeal.
      6
       Patrolman Chavez testified that, throughout the course of the traffic stop,
he believed he had probable cause to search the pick-up based on the DEA’s
statement that there was cocaine in the truck. He pursued the pretense – asking
for Mr. Chavez’s documents, asking where Mr. Chavez and Mr. Moreno were
going, writing the citation, asking for consent to search the vehicle – to comply
with the DEA’s request that he not reveal information about their investigation.
At no point during the stop did Patrolman Chavez inform Mr. Chavez and Mr.
Moreno that they were under investigation for drug trafficking.

                                         -6-
      D. The Search

      Before Mr. Chavez could drive off, however, Patrolman Chavez asked Mr.

Chavez if he would answer some more questions. During this colloquy, the

patrolman asked for permission to search the truck. Mr. Chavez queried what

would happen if he did not consent; Patrolman Chavez responded that he would

have Chica sniff the truck before letting them go. Eventually, Mr. Chavez

consented to the search, and both Mr. Chavez and Mr. Moreno signed

standardized consent forms that were written in both English and Spanish.

During the subsequent search, Patrolman Chavez discovered a packet of a

substance that was later confirmed to be cocaine in a bucket of nails on the

truck’s bed. He then arrested both Mr. Chavez and Mr. Moreno. All told, the

traffic stop and search lasted about 30 minutes.

      E. The Secrecy

      The DEA task force opted to involve Patrolman Chavez – and to request

that he develop his own rationale for stopping the truck – to maintain the secrecy

of its investigation. Agent Maudlin testified that Patrolman Chavez was given

minimal information to protect the integrity of the DEA investigation and the

identity of the CS. By having a New Mexico State Police officer pull Mr. Moreno

over, the DEA task force hoped to convince the traffickers that the stop was a

random occurrence.




                                        -7-
      F. The Suppression Decision

      On February 7, 2006, Mr. Chavez was indicted on one count of conspiracy

to commit possession with intent to distribute more than 500 grams of cocaine, in

violation of 21 U.S.C. §§ 841(a)(1) & (b)(1)(B) and 846, one count of possession

with intent to distribute more than 500 grams of cocaine, in violation of 21 U.S.C.

§ 841(a)(1) & (b)(1)(B), and one count of aiding and abetting, in violation of 18

U.S.C. § 2. Mr. Chavez and Mr. Moreno submitted a joint motion to suppress

evidence, and the district court held a suppression hearing on August 29 and

August 31, 2006. After Judge Armijo rejected the motion to suppress in a

Memorandum Opinion and Order dated September 8, 2006, Mr. Chavez entered a

conditional guilty plea to the first and second counts (conspiracy and possession).

On appeal, Mr. Chavez renews his Fourth Amendment objections to the traffic

stop and the search.

II.   DISCUSSION

      A. Standard of Review

      In assessing a denial of a motion to suppress, this court “accept[s] the

factual findings of the district court, and its determination of witness credibility,

unless they are clearly erroneous.” United States v. Herrera, 444 F.3d 1238, 1242

(10th Cir. 2006) (quotation omitted); United States v. Cervine, 347 F.3d 865, 868

(10th Cir. 2003). Moreover, this court “review[s] the evidence in the light most

favorable to the government.” United States v. Patterson, 472 F.3d 767, 775

                                         -8-
(10th Cir. 2006). Ultimately, however, this court must review de novo the

reasonableness of the government’s action under the Fourth Amendment.

Herrera, 444 F.3d at 1242. The government bears the burden of proving the

reasonableness of the search or seizure. Id.

      B. Merits

      Mr. Chavez asserts that Patrolman Chavez unlawfully stopped and searched

his pick-up because (1) the DEA had evidence of Mr. Moreno’s criminal conduct

but no individualized evidence regarding Mr. Chavez, and (2) TFO Mowduk

never communicated the information constituting probable cause to Patrolman

Chavez, rendering Patrolman Chavez’s reliance on the instructions to stop and

search the truck unreasonable. 7 As such, Mr. Chavez argues that the district court

should have excluded all evidence derived from the traffic stop.

      The Fourth Amendment protects the “right of the people to be secure in

their persons, houses, papers, and effects, against unreasonable searches and

seizures.” U.S. Const. amend. IV. 8 Although a traffic stop is typically brief, it is

a “seizure” within the meaning of the Fourth Amendment. Delaware v. Prouse,

      7
       Mr. Chavez has standing to challenge the search and seizure because he
has a reasonable expectation of privacy in the area that Patrolman Chavez
searched, the bed of the pick-up he owned. See United States v. Eylicio-
Montoya, 70 F.3d 1158, 1162 (10th Cir. 1995); cf. United States v. DeLuca, 269
F.3d 1128, 1131-32 (10th Cir. 2001) (noting that passengers “without a
possessory or property interest in the vehicle searched” lack standing).
      8
       Mapp v. Ohio, 367 U.S. 643 (1961), incorporated this protection against
actions by state governments.

                                         -9-
440 U.S. 648, 653 (1979). Because routine traffic stops are “more analogous to

an investigative detention than a custodial arrest,” the principles set forth in Terry

v. Ohio, 392 U.S. 1 (1968), guide this court’s analysis of the reasonableness of

the traffic stop. See United States v. Hunnicutt, 135 F.3d 1345, 1348 (10th Cir.

1998). Thus, we examine whether the traffic stop was (1) “justified at its

inception” and (2) “reasonably related in scope to the circumstances which

justified the interference in the first place.” United States v. Botero-Ospina, 71

F.3d 783, 786 (10th Cir. 1995) (en banc) (quoting Terry, 392 U.S. at 20).

      The police may stop a car if they have probable cause or a reasonable,

articulable suspicion to believe the car is carrying contraband. See United States

v. Cortez-Galaviz, 495 F.3d 1203, 1205-06 (10th Cir. 2007) (“[A] traffic stop will

be held reasonable when, under the totality of the circumstances, the officer bears

a ‘reasonable suspicion’ that criminal activity ‘may be afoot.’” (quoting United

States v. Arvizu, 534 U.S. 266, 273 (2002)); United States v. Stone, 866 F.2d 359,

362 (10th Cir. 1989) (citing United States v. Sharpe, 470 U.S. 675, 682 (1985)).

This court looks only at whether the stop was “objectively justified”; the officer’s

subjective motives are irrelevant. United States v. DeGasso, 369 F.3d 1139, 1143

(10th Cir. 2004).




                                         - 10 -
      Because Mr. Chavez’s first argument stands or falls on the result of his

second, we turn at the outset to the latter argument. 9 In Cervine, this court left

open the question whether, “absent any traffic violation,” a reasonable, articulable

suspicion (or probable cause) of illegal activity communicated to the stopping

officer by other law enforcement officers would suffice to permit a traffic stop.

Cervine, 347 F.3d at 870 n.6. 10 This question is squarely before the court now. 11

A natural extension of United States v. Zamudio-Carrillo, 499 F.3d 1206 (10th

Cir. 2007), answers the question and forecloses Mr. Chavez’s arguments about the

unlawfulness of the traffic stop and subsequent search.

      We will analyze this initial issue in two steps, asking first whether the DEA

task force agents had probable cause to believe Mr. Chavez’s vehicle contained


      9
        Mr. Chavez’s first argument– that the DEA’s investigation targeted only
Mr. Moreno and that the DEA agents thus lacked individualized information
regarding Mr. Chavez – is foreclosed by Stone so long as (1) the DEA task force
had probable cause and (2) that probable cause could be imputed to Patrolman
Chavez. See Stone, 866 F.2d at 362 (“Police may stop and detain an automobile
and its occupants if they have an articulable and reasonable suspicion that the car
is carrying contraband.” (emphasis added)). At the time he was stopped, Mr.
Chavez was driving a truck the DEA task force believed – because of the
investigation of Mr. Moreno – had a kilo of cocaine in it. For the reasons
discussed below, we conclude that Mr. Chavez’s first argument falters.
      10
        The Cervine court left the question open because the government did not
“argue that the troopers stopped Mr. Cervine based on the objective, reasonable,
and articulable suspicion of drug trafficking as communicated to them by the
DEA.” 347 F.3d at 870 n.6.
      11
         In fact, the government never advanced the argument that Patrolman
Chavez was actually stopping Mr. Chavez in an attempt to enforce New Mexico’s
traffic laws.

                                         - 11 -
narcotics. They did. Second, we query whether the DEA task force’s probable

cause could be imputed to Patrolman Chavez. It could, in light of Zamudio-

Carrillo and precedent from our sister circuits. Accordingly, we agree with the

district court’s conclusion that Patrolman Chavez, acting on the strength of the

DEA task force’s information, was objectively justified in initiating the stop and

in searching the truck.

      1. Probable Cause

      Here, the government relies on the information derived from the DEA’s

investigation to justify both the stop of Mr. Chavez and the search of his truck.

As noted above, an officer may stop a car if he has either a reasonable, articulable

suspicion or probable cause to believe that the car is carrying contraband. See

Cortez-Galaviz, 495 F.3d at 1205-06. “Probable cause to search a vehicle is

established if, under the totality of the circumstances, there is a fair probability

that the car contains contraband or evidence.” United States v. Vasquez-Castillo,

258 F.3d 1207, 1212 (10th Cir. 2001) (quoting United States v. Downs, 151 F.3d

1301, 1303 (10th Cir. 1998)); cf. Ornelas v. United States, 517 U.S. 690, 696

(1996).

      Based on a credible confidential source’s communication with Mr. Moreno

and the task force’s ongoing surveillance of Mr. Moreno, the DEA task force –

specifically Agent Maudlin and TFO Mowduk – knew that: (1) Mr. Moreno had

agreed to sell 1 kilo of cocaine to a buyer at a truck stop in Santa Rosa on January

                                         - 12 -
19; (2) Mr. Moreno planned to have someone drive him to Santa Rosa; (3) a man

matching Mr. Moreno’s description and driving an orange truck customarily

driven by Mr. Moreno left Mr. Moreno’s trailer home and drove to 319 Riverside;

(4) a white pick-up left that address with two occupants, one of whom appeared to

be the man who left Mr. Moreno’s trailer in the orange truck; (5) Mr. Moreno

then told the confidential source that he was en route to Santa Rosa with a driver

to complete the drug deal; and (6) the white pick-up took the interstate that

connects Albuquerque with Santa Rosa. As the district court held, this evidence

suffices to support the conclusion that the DEA task force had probable cause to

believe that Mr. Chavez’s pick-up contained the kilo of cocaine.

      The “automobile exception” to the warrant requirement permits law

enforcement officers who have “probable cause to believe a car contains

contraband [to] search the car without first obtaining a search warrant.” United

States v. Beckstead, 500 F.3d 1154, 1165 (10th Cir. 2007); see also California v.

Carney, 471 U.S. 386, 392 (1985). Once the officer’s suspicions rise to the level

of probable cause, they are empowered to search “the entire vehicle, including the

trunk and all containers therein that might contain contraband.” United States v.

Bradford, 423 F.3d 1149, 1160 (10th Cir. 2005).

      Therefore, the DEA task force officers with knowledge of the above-listed

facts would have been within the Fourth Amendment’s reasonableness bounds had

they searched Mr. Chavez’s pick-up.

                                       - 13 -
      2. Collective Knowledge

      The next issue is whether the information known to TFO Mowduk and

other members of the DEA task force can be imputed to Patrolman Chavez. That

is, this court must decide whether a police officer may rely on the instructions of

another law enforcement agency or officer to initiate a traffic stop and then

conduct a search pursuant to the “automobile exception.”

      This question implicates the “fellow officer” rule, also known as the

“collective knowledge” doctrine. This doctrine can be conceptualized using two

categories: “horizontal” collective knowledge and “vertical” collective

knowledge. The first category subsumes situations where a number of individual

law enforcement officers have pieces of the probable cause puzzle, but no single

officer possesses information sufficient for probable cause. See United States v.

Shareef, 100 F.3d 1491, 1503-05 (10th Cir. 1996). In such situations, the court

must consider whether the individual officers have communicated the information

they possess individually, thereby pooling their collective knowledge to meet the

probable cause threshold. See id. at 1504-05; see also United States v. Maestas, 2

F.3d 1485, 1493 (10th Cir. 1993). This case, on the other hand, implicates the

second category; it is a situation where one officer has probable cause and

instructs another officer to act, but does not communicate the corpus of




                                       - 14 -
information known to the first officer that would justify the action. 12 We review

now the precedents applying this “vertical” variety of collective knowledge.

      In United States v. Hensley, 469 U.S. 221, 231 (1985), the Supreme Court

noted that “when evidence is uncovered during a search incident to an arrest in

reliance on a flyer or bulletin, its admissibility turns on whether the officers who

issued the flyer possessed probable cause to make the arrest.” There, police

officers had initiated a Terry stop of the defendant in reliance on a “wanted

flyer.” Id. at 223-24. On the facts before it, the Court concluded that, so long as

the officers that issued the flyer had a reasonable suspicion about the person it

targeted, “then reliance on that flyer or bulletin justifies a stop to check

identification, to pose questions to the person, or to detain the person briefly . . .

.” Id. at 232 (internal citations omitted).

      Logically, the Hensley holding approaches a rule that would allow us to

impute the DEA’s knowledge to Patrolman Chavez. However, Hensley addressed

a Terry stop situation (and not a full-on search pursuant to the automobile

exception). Dicta in Whiteley v. Warden, 401 U.S. 560 (1971), similarly supports

this conclusion. There, the Supreme Court suggested in dicta that an arresting

officer could rely on an arrest warrant obtained by another law enforcement


      12
       Of course, the officer who has probable cause may possess that
information as a result of communication from other officers. Thus, the
“horizontal” and “vertical” collective knowledge categories are by no means
mutually exclusive.

                                         - 15 -
agency. Id. at 568. However, that statement was not dispositive to the issues

here because it dealt with an arrest warrant issued by a magistrate and the holding

of Whiteley was that the underlying warrant itself was defective, thereby

mandating the suppression of the evidence obtained by the second, arresting

officer. Id. at 568-69. The missing link then is whether an officer, like

Patrolman Chavez, who was not intimately involved in an investigation can rely

on the collective knowledge of the investigators to stop and search a vehicle when

justifiable conclusions of the collective investigation are conveyed to him.

Zamudio-Carrillo substantially supplied that link.

      In Zamudio-Carrillo, this court addressed a situation where one state

trooper, Trooper Rule, observed two Ford SUVs with sequentially numbered

Arizona specialty plates driving along I-70 in Kansas. 499 F.3d at 1207-08.

Trooper Rule also noticed that one of the vehicles, a Ford Explorer, appeared to

have a false floor compartment under its rear wheel well. Id. at 1208. After

pulling the Explorer over, Trooper Rule “confirmed the presence of a false

compartment.” Id. He then “contacted dispatch and asked them to send an

officer to locate” the other Ford SUV. Id. A second state trooper, Trooper

Harvey, “pulled up to Rule’s location and Rule gave him a brief description” of

the other Ford SUV. Id. Trooper Harvey then tracked down the vehicle, stopped

it, and arrested the driver. Id.




                                        - 16 -
      The driver of the second vehicle, Zamudio-Carrillo, argued that Trooper

Harvey’s action – taken in reliance on Trooper Rule’s “brief description” –

violated the Fourth Amendment. Id. at 1209-10. This court disagreed. Id. at

1210. We concluded that “the discovery of a false compartment in the Ford

Explorer coupled with objective information indicating [the Explorer’s driver]

was traveling in tandem with Zamudio-Carrillo gave Trooper Harvey probable

cause to stop and seize Zamudio-Carrillo.” Id. at 1209. It is not clear from the

discussion in Zamudio-Carrillo whether Trooper Rule communicated to Trooper

Harvey the basis for his suspicions about the Ford Explorer or just Trooper Rule’s

conclusion that he believed the Ford Explorer was involved in drug trafficking.

Because the Zamudio-Carrillo court did not explicitly discuss the details of the

communication between Rule and Harvey, we will delve a bit deeper.

      Extrapolating from Hensley, those circuits that have addressed squarely the

issue presented here have held that a police officer may rely on the instructions of

the DEA (or other law enforcement agencies) in stopping a car, even if that

officer himself or herself is not privy to all the facts amounting to probable cause.

See United States v. Ramirez, 473 F.3d 1026, 1037 (9th Cir. 2007) (“Where one

officer knows facts constituting reasonable suspicion or probable cause (sufficient

to justify action under an exception to the warrant requirement), and he

communicates an appropriate order or request, another officer may conduct a

warrantless stop, search, or arrest without violating the Fourth Amendment.”);

                                        - 17 -
United States v. Williams, 429 F.3d 767, 771-72 (8th Cir. 2005) (“[W]e also hold

that the collective knowledge of the DEA team was sufficient to provide

reasonable suspicion to stop [the co-defendant’s] vehicle, and such knowledge

was imputed to the officer at the scene when he received [another officer’s]

radioed request.”); United States v. Burton, 288 F.3d 91, 99 (3d Cir. 2002)

(“[T]he arresting officer need not possess an encyclopedic knowledge of the facts

supporting probable cause, but can instead rely on an instruction to arrest

delivered by other officers possessing probable cause.”); United States v. Ibarra-

Sanchez, 199 F.3d 753, 758-59 (5th Cir. 1999); United States v. Celio, 945 F.2d

180, 183 (7th Cir. 1991). 13

      Ignoring these precedential obstacles, Mr. Chavez cites Shareef for the

proposition that Patrolman Chavez could not act on TFO Mowduk’s instructions

unless Mowduk communicated the substance of the DEA’s suspicions. His

reliance on Shareef is misplaced. In Shareef, one police officer had stopped a car

and communicated with the driver, meanwhile another officer had conversed with

the dispatcher, who provided a physical description (the weight and height) of a



      13
        Of course, these cases note that there must be some communication
between the officer or officers with probable cause and the officer who executes
the stop or search. This communication confirms that the officers are functioning
as a team. See Ramirez, 473 F.3d at 1036; United States v. Rodriguez, 831 F.2d
162, 166 (7th Cir. 1987) (noting that where a DEA agent points out specifically
what car another officer should stop that officer acts merely “as an ‘extension’ or
agent of the DEA agent”).

                                        - 18 -
man wanted by authorities elsewhere. Id. at 1503-04. Because those two officers

never shared their respective quanta of information, this court held that the fact

that the driver’s physique matched the wanted man’s physical description could

not be considered as a factor in reviewing the objective reasonableness of either

officers’ actions. Id. at 1504-05. The Shareef court thereby rejected a rule that

information known, individually, to officers is pooled (as if they were one

sentient law-enforcing organism) even absent any evidence of communication.

      Here, however, the aspects of the DEA investigation that are pertinent to

the probable cause inquiry were known to TFO Mowduk, the officer who asked

Patrolman Chavez to stop Mr. Chavez’s vehicle. Rather than a horizontal pooling

of discrete pieces of information, one officer here (Mowduk) had all the requisite

probable cause components; the question then is whether that information can be

imputed vertically to another officer (Patrolman Chavez). As explained above,

our sister circuits have extrapolated from Hensley and upheld this latter

application of the collective knowledge doctrine. Moreover, Zamudio-Carrillo

counsels the identical result.

      Accordingly, we conclude, as did the district court, that Patrolman Chavez

acted on the strength of the DEA’s probable cause when he stopped and searched

Mr. Chavez’s truck. He merely supplied a cover story (the putative headlight

infraction) that would mask the basis for his alternative probable cause (the drug

trafficking). “[D]isguising the stop as a ‘traffic stop’ was a valid law

                                        - 19 -
enforcement tactic calculated to ensure an officer’s safety,” Ramirez, 473 F.3d at

1038 (Kozinski, J., concurring), and safeguard the CS’s identity and the integrity

of the DEA investigation.

      As Mr. Chavez concedes in his brief, our conclusion that the DEA task

force’s knowledge can be imputed to Patrolman Chavez forecloses Mr. Chavez’s

ancillary arguments. Each of Mr. Chavez’s remaining arguments regarding the

scope of the initial detention, the consent to search, and the applicability of the

automobile exception to the warrant requirement turn on the initial issue of the

propriety of Patrolman Chavez’s stop of Mr. Chavez. Accordingly, we address

them only perfunctorily.

      3. The Reasonableness of the Stop and Search

      During his interaction with Mr. Chavez and Mr. Moreno, Patrolman Chavez

followed each step of his routine traffic stop sequence. He asked Mr. Chavez for

his documents, and chatted with both Mr. Chavez and Mr. Moreno about their

travel plans. He wrote up two citations for Mr. Chavez (although one turned out

to be a misstatement of New Mexico’s traffic regulations). He then returned Mr.

Chavez’s papers and informed the pair they could leave. Before letting them do

so, however, he re-initiated contact to request permission to search the truck. He

did not need to do so, given the fact that he had probable cause all along. See,

e.g., Vasquez-Castillo, 258 F.3d at 1212. However, by requesting consent,




                                         - 20 -
Patrolman Chavez followed the directions of the DEA. 14 Patrolman Chavez had

probable cause to believe the truck contained contraband; thus, the stop and

search were lawful under the Fourth Amendment.

III.   CONCLUSION

       At the time of the traffic stop, “the facts and circumstances within [the

DEA task force’s] knowledge and of which they had reasonably trustworthy

information were sufficient to warrant a prudent man in believing that the

[defendant] . . . was committing an offense.” Beck v. Ohio, 379 U.S. 89, 91

(1964). Because TFO Mowduk – and the DEA task force collectively – had

probable cause to search the truck, so too did Patrolman Chavez. And this, of

course, permitted his warrantless search of those locations in the truck that might

contain the narcotics (such as the bucket of nails). As such, we AFFIRM the

denial of Mr. Chavez’s motion to suppress.

       14
         The district court concluded that Patrolman Chavez did not coerce Mr.
Chavez’s consent. Although we need not decide the issue – because Patrolman
Chavez had probable cause to search the truck regardless – we would be inclined
to agree. “A consensual encounter is the voluntary cooperation of a private
citizen in response to non-coercive questioning by a law enforcement officer.”
United States v. Wallace, 429 F.3d 969, 974 (10th Cir. 2005) (quoting United
States v. West, 219 F.3d 1171, 1176 (10th Cir. 2000)). An officer’s questioning
is non-coercive if a “reasonable person under the circumstances would believe he
was free to leave or disregard the officer’s request for information.” Id. at 974-75
(quoting United States v. Elliott, 107 F.3d 810, 814 (10th Cir. 1997)). Although
Patrolman Chavez did caution that he would run Chica around the truck
regardless of whether the pair consented, Illinois v. Caballes, 543 U.S. 405, 409
(2005), confirms that the officer had the authority to do so. More importantly,
there was little evidence put before the district court that would cast as coercive
Patrolman Chavez’s request for consent.

                                        - 21 -

```

---

## GROUP: _overhaul2/lake/cases/United States v. Classic.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Classic"
type: case
citation: "313 U.S. 299 (1941)"
parallel_cite: "61 S. Ct. 1031; 85 L. Ed. 1368"
neutral_cite: 1941 U.S. LEXIS 601
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1941
date_decided: 1941-10-13
docket: 618
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1941-05-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Classic
  varies_by_point: false
  scope_note: "The 'under color of' state law definition remains the governing test; adopted for § 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103531/united-states-v-classic/"
  cluster_id: 103531
  opinion_id: 103531
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Monroe v. Pape]]", "[[Screws v. United States]]"]
aliases: []
tags: ["case", "section-1983", "color-of-law", "section-242", "civil-rights", "state-action"]
holding: "Misuse of power possessed by virtue of state law and made possible only because the wrongdoer is clothed with state authority is action taken 'under color of' state law — the anchor color-of-law definition later applied to § 1983."
lake:
  record_id: United States v. Classic
  status: verified
  projected_at: 2026-07-06
---

# United States v. Classic

*313 U.S. 299 (1941)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Louisiana election commissioners were indicted under the federal criminal civil-rights statutes (then §§ 19 and 20 of the Criminal Code, now 18 U.S.C. §§ 241–242) for willfully altering and falsely counting ballots cast in a Democratic primary election for a seat in the U.S. House of Representatives. They moved to dismiss, arguing both that the right to vote in a primary was not constitutionally protected and that, as election officials, they had not acted "under color of" state law.

## Issue
Whether officials who misuse authority conferred on them by state law act "under color of" state law for purposes of the federal civil-rights statutes (and whether the right to vote in a primary is constitutionally protected).

## Rule
Officials who abuse power held by virtue of their state office act under [[Section 1983 Liability and Qualified Immunity|color of state law]]. "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law." — 313 U.S. at 326. ^pin-326

The Court also held that the constitutionally protected right to choose a Representative includes the right to vote in a primary that is an integral part of the election machinery, so the commissioners' fraud deprived voters of a federally secured right.

## Application
The commissioners' acts — altering and falsely certifying the ballot count — were done "in the course of their performance of duties under the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election." Because they could commit the fraud only because they were clothed with the authority of state election law, their misuse of that authority was action "under color of" state law, and it deprived the voters of a right secured by the Constitution.

## Conclusion
Reversed in relevant part. Misuse of state-conferred power is action under [[Section 1983 Liability and Qualified Immunity|color of state law]], and the indictment stated an offense; the color-of-law definition announced here became the foundational test for state action under the civil-rights statutes.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Classic*'s "under color of" definition is the anchor later carried into criminal civil-rights enforcement in [[Screws v. United States]] and expressly adopted for civil § 1983 liability in [[Monroe v. Pape]]; it remains the governing color-of-law formulation. (*Classic* also overruled *Grovey v. Townsend* on the primary-voting question.) No negative treatment of the color-of-law holding.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *United States v. Classic*, 313 U.S. 299 (1941) — https://www.courtlistener.com/opinion/103531/united-states-v-classic/ — pinpoint: 326 (CL stores a paragraph-numbered format without star pages; page per official U.S. Reports citation).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "16f60372750fc3ed", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Classic"}, "payload": {"all": [{"cite": "313 U.S. 299", "page": "299", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "313"}, {"cite": "61 S. Ct. 1031", "page": "1031", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "85 L. Ed. 1368", "page": "1368", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "85"}, {"cite": "1941 U.S. LEXIS 601", "page": "601", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1941"}], "display": "313 U.S. 299", "official": {"cite": "313 U.S. 299", "page": "299", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "313"}, "official_selection_present": true, "record_id": "United States v. Classic"}}
{"assertion_id": "26c71e20eb7ce2f4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-326", "record_id": "United States v. Classic"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-326", "pinpoint_status": "slip-only", "quote": "state law for purposes of the federal civil-rights statutes (and whether the right to vote in a primary is constitutionally protected). ## Rule Officials who abuse power held by virtue of their state office act under color of state law.", "quote_fidelity": "mismatch", "record_id": "United States v. Classic", "star_marker": null}}
{"assertion_id": "39faf92c2c7ed9e5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Classic"}, "payload": {"as_of_content": "1941-05-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Classic", "scope_note": "The 'under color of' state law definition remains the governing test; adopted for § 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)", "varies_by_point": false}}
```

### lake record — United States v. Classic

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Classic",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Classic",
    "case_name_short": "Classic",
    "case_name_full": "UNITED STATES v. CLASSIC Et Al.",
    "input_case_name": "United States v. Classic",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1941-10-13",
    "year": 1941,
    "docket": "618",
    "cluster_id": 103531,
    "lead_opinion_id": 103531,
    "sibling_ids": [
      103531,
      9419158,
      9419159
    ],
    "absolute_url": "/opinion/103531/united-states-v-classic/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "313 U.S. 299",
      "volume": "313",
      "reporter": "U.S.",
      "page": "299",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "61 S. Ct. 1031",
        "volume": "61",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 1368",
        "volume": "85",
        "reporter": "L. Ed.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1941 U.S. LEXIS 601",
        "volume": "1941",
        "reporter": "U.S. LEXIS",
        "page": "601",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "313 U.S. 299",
        "volume": "313",
        "reporter": "U.S.",
        "page": "299",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 S. Ct. 1031",
        "volume": "61",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 1368",
        "volume": "85",
        "reporter": "L. Ed.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1941 U.S. LEXIS 601",
        "volume": "1941",
        "reporter": "U.S. LEXIS",
        "page": "601",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "313 U.S. 299",
    "official_selection": {
      "court_class": "scotus",
      "selected": "313 U.S. 299",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "state law for purposes of the federal civil-rights statutes (and whether the right to vote in a primary is constitutionally protected). ## Rule Officials who abuse power held by virtue of their state office act under color of state law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1941-05-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Classic",
    "varies_by_point": false,
    "scope_note": "The 'under color of' state law definition remains the governing test; adopted for \u00a7 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Dustin Myers v. Murry Bowman",
          "cluster_id": 857864,
          "cite": [
            "713 F.3d 1319",
            "2013 WL 1442055",
            "2013 U.S. App. LEXIS 7216",
            "24 Fla. L. Weekly Fed. C 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Constitutionality of the D.C. House Voting Rights Act of 2009",
          "cluster_id": 6236943,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellee-Cross-Appellant v. Eva C. Temple, Appellant-Cross-Appellee",
          "cluster_id": 794242,
          "cite": [
            "447 F.3d 130",
            "97 A.F.T.R.2d (RIA) 2265",
            "2006 U.S. App. LEXIS 10885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tobin",
          "cluster_id": 10699401,
          "cite": [
            "2005 DNH 161"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roberto Hernandez Miranda v. Clark County, Nevada Morgan Harris Thomas Rigsby",
          "cluster_id": 776499,
          "cite": [
            "279 F.3d 1102",
            "2002 Cal. Daily Op. Serv. 1289",
            "2002 Daily Journal DAR 1628",
            "2002 U.S. App. LEXIS 2004",
            "2002 WL 193029"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mentavlos v. Anderson",
          "cluster_id": 2967409,
          "cite": [
            "249 F.3d 301",
            "2001 WL 475936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "West v. Atkins",
          "cluster_id": 112116,
          "cite": [
            "101 L. Ed. 2d 40",
            "108 S. Ct. 2250",
            "487 U.S. 42",
            "1988 U.S. LEXIS 2744",
            "56 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adickes v. S. H. Kress & Co.",
          "cluster_id": 108153,
          "cite": [
            "26 L. Ed. 2d 142",
            "90 S. Ct. 1598",
            "398 U.S. 144",
            "1970 U.S. LEXIS 31"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scheuer v. Rhodes",
          "cluster_id": 109009,
          "cite": [
            "40 L. Ed. 2d 90",
            "94 S. Ct. 1683",
            "416 U.S. 232",
            "1974 U.S. LEXIS 126",
            "71 Ohio Op. 2d 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. Carr",
          "cluster_id": 106366,
          "cite": [
            "7 L. Ed. 2d 663",
            "82 S. Ct. 691",
            "369 U.S. 186",
            "1962 U.S. LEXIS 1567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buckley v. Valeo",
          "cluster_id": 109380,
          "cite": [
            "46 L. Ed. 2d 659",
            "96 S. Ct. 612",
            "424 U.S. 1",
            "1976 U.S. LEXIS 16"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lugar v. Edmondson Oil Co.",
          "cluster_id": 110766,
          "cite": [
            "73 L. Ed. 2d 482",
            "102 S. Ct. 2744",
            "457 U.S. 922",
            "1982 U.S. LEXIS 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reynolds v. Sims",
          "cluster_id": 106850,
          "cite": [
            "12 L. Ed. 2d 506",
            "84 S. Ct. 1362",
            "377 U.S. 533",
            "1964 U.S. LEXIS 1002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Shea v. Littleton",
          "cluster_id": 108906,
          "cite": [
            "38 L. Ed. 2d 674",
            "94 S. Ct. 669",
            "414 U.S. 488",
            "1974 U.S. LEXIS 41"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Breckenridge",
          "cluster_id": 108362,
          "cite": [
            "29 L. Ed. 2d 338",
            "91 S. Ct. 1790",
            "403 U.S. 88",
            "1971 U.S. LEXIS 3774",
            "3 Empl. Prac. Dec. (CCH) 8284",
            "9 Fair Empl. Prac. Cas. (BNA) 1196"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owen v. City of Independence",
          "cluster_id": 110236,
          "cite": [
            "63 L. Ed. 2d 673",
            "100 S. Ct. 1398",
            "445 U.S. 622",
            "1980 U.S. LEXIS 14"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rendell-Baker v. Kohn",
          "cluster_id": 110764,
          "cite": [
            "73 L. Ed. 2d 418",
            "102 S. Ct. 2764",
            "457 U.S. 830",
            "1982 U.S. LEXIS 43"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davidson v. Cannon",
          "cluster_id": 111556,
          "cite": [
            "88 L. Ed. 2d 677",
            "106 S. Ct. 668",
            "474 U.S. 344",
            "1986 U.S. LEXIS 44",
            "54 U.S.L.W. 4095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Sparks",
          "cluster_id": 110353,
          "cite": [
            "66 L. Ed. 2d 185",
            "101 S. Ct. 183",
            "449 U.S. 24",
            "1980 U.S. LEXIS 9",
            "49 U.S.L.W. 4001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Youngstown Sheet & Tube Co. v. Sawyer",
          "cluster_id": 105018,
          "cite": [
            "96 L. Ed. 2d 1153",
            "72 S. Ct. 863",
            "343 U.S. 579",
            "1952 U.S. LEXIS 2625",
            "62 Ohio Law. Abs. 417",
            "96 L. Ed. 1153",
            "26 A.L.R. 2d 1378",
            "47 Ohio Op. 430",
            "30 L.R.R.M. (BNA) 2172",
            "1952 Trade Cas. (CCH) 67,293"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103531 OR 9419158 OR 9419159) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NDExNTUyMDAwMDAmcz0yMzM2MzE4JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103531+OR+9419158+OR+9419159%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(103531 OR 9419158 OR 9419159)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDYmcz0xMTIyMDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103531+OR+9419158+OR+9419159%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103531 OR 9419158 OR 9419159)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103531 OR 9419158 OR 9419159)",
    "indexed_citing_opinions": 1016,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103531,
        "count": 930,
        "count_source": "search"
      },
      {
        "opinion_id": 9419158,
        "count": 116,
        "count_source": "search"
      },
      {
        "opinion_id": 9419159,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2093,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-classic.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NTcxNTQmcz05NDkzNTU4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103531+OR+9419158+OR+9419159%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103531,
        "cited_id": 84968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 88998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 89266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 90042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 92299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 92761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 93413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 102874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 1087873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 2620807,
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
    "date_created": "2026-07-05T23:09:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:13:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Classic (truncated)

```
<p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">61 S.Ct. 1031</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">85 L.Ed. 1368</a></span></p>
    <p class="parties">UNITED STATES<br>v.<br>CLASSIC et al.</p>
    <p class="docket">No. 618.</p>
    <p class="date">Argued April 7, 1941.</p>
    <p class="date">Decided May 26, 1941.</p>
    <p class="date">Rehearing Denied Oct. 13, 1941.</p>
    <div class="prelims">
      <p class="indent">[Syllabus from pages 299-301 intentionally omitted]</p>
      <p class="indent">Messrs. Robert H. Jackson, Atty. Gen., and Herbert Wechsler, of Washington, D.C., for appellant.</p>
      <p class="indent">[Argument of Counsel from pages 301-303 intentionally omitted]</p>
      <p class="indent">Mr. Warren O. Coleman, of New Orleans, La., for appellees.</p>
      <p class="indent">[Argument of Counsel from Pages 304-306 intentionally omitted]</p>
      <p class="indent">Mr. Justice STONE, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">Two counts of an indictment found in a federal district court charged that appellees, Commissioners of Elections, conducting a primary election under Louisiana law, to nominate a candidate of the Democratic Party for representative in Congress, willfully altered and falsely counted and certified the ballots of voters cast in the primary election. The questions for decision are whether the right of qualified voters to vote in the Louisiana primary and to have their ballots counted is a right 'secured * * * by the Constitution' within the meaning of &#167;&#167; 19 and 20 of the Criminal Code, and whether the acts of appellees charged in the indictment violate those sections.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">On September 25, 1940, appellees were indicted in the District Court for Eastern Louisiana for violations of &#167;&#167; 19 and 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. &#167;&#167; 51</span>, 52, <span class="citation no-link">18 U.S.C.A. &#167; 51</span>, 52. The first count of the indictment alleged that a primary election was held on September 10, 1940, for the purpose of nominating a candidate of the Democratic Party for the office of Representative in Congress for the Second Congressional District of Louisiana, to be chosen at an election to be held on November 10th; that in that district nomination as a candidate of the Democratic Party is and always has been equivalent to an election; that appellees were Commissioners of Election, selected in accordance with the Louisiana law to conduct the primary in the Second Precinct of the Tenth Ward of New Orleans, in which there were five hundred and thirty-seven citizens and qualified voters.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The charge based on these allegations, was that the appellees conspired with each other and with others unknown, to injure and oppress citizens in the free exercise and enjoyment of rights and privileges secured to them by the Constitution and Laws of the United States, namely, (1) the right of qualified voters who cast their ballots in the primary election to have their ballots counted as cast for the candidate of their choice, and (2) the right of the candidates to run for the office of Congressman and to have the votes in favor of their nomination counted as cast. The overt acts alleged were that the appellees altered eighty-three ballots cast for one candidate and fourteen cast for another, marking and counting them as votes for a third candidate, and that they falsely certified the number of votes cast for the respective candidates to the chairman of the Second Congressional District Committee.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">The second count, repeating the allegations of fact already detailed, charged that the appellees, as Commissioners of Election willfully and under color of law subjected registered voters at the pr mary who were inhabitants of Louisiana to the deprivation of rights, privileges and immunities secured and protected by the Constitution and Laws of the United States, namely their right to cast their votes for the candidates of their choice and to have their votes counted as cast. It further charged that this deprivation was effected by the willful failure and refusal of defendants to count the votes as cast, by their alteration of the ballots, and by their false certification of the number of votes cast for the respective candidates in the manner already indicated.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">The District Court sustained a demurrer to counts 1 and 2 on the ground that &#167;&#167; 19 and 20 of the Criminal Code under which the indictment was drawn do not apply to the state of facts disclosed by the indictment and that, if applied to those facts, &#167;&#167; 19 and 20 are without constitutional sanction, citing United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#488" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476, 488, 489</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#411" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407, 411, 412</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>; Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>. The case comes here on direct appeal from the District Court under the provisions of the Criminal Appeals Act, Judicial Code, &#167; 238, <span class="citation no-link">18 U.S.C. &#167; 682</span>, <span class="citation no-link">18 U.S.C.A. &#167; 682</span>, <span class="citation no-link">28 U.S.C. &#167; 345</span>, <span class="citation no-link">28 U.S.C.A. &#167; 345</span>, which authorize an appeal by the United States from a decision or judgment sustaining a demurrer to an indictment where the decision or judgment is 'based upon the invalidity, or construction of the statute upon which the indictment is founded'.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Upon such an appeal our review is confined to the questions of statutory construction and validity decided by the District Court. United States v. Patten, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">226 U.S. 525</a></span>, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">33 S.Ct. 141</a></span>, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">57 L.Ed. 333</a></span>, 44 L.R.A.,N.S., 325; United States v. Birdsall, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/#230" aria-description="Citation for case: United States v. Birdsall">233 U.S. 223, 230</a></span>, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/#514" aria-description="Citation for case: United States v. Birdsall">34 S.Ct. 512, 514</a></span>, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/" aria-description="Citation for case: United States v. Birdsall">58 L.Ed. 930</a></span>; United States v. Borden Co., <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/#192" aria-description="Citation for case: United States v. Borden Co.">308 U.S. 188, 192, 193</a></span>, <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/#185" aria-description="Citation for case: United States v. Borden Co.">60 S.Ct. 182, 185</a></span>, <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/" aria-description="Citation for case: United States v. Borden Co.">84 L.Ed. 181</a></span>. Hence, we do not pass upon various arguments advanced by appellees as to the sufficiency and construction of the indictment.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">Section 19 of the Criminal Code condemns as a criminal offense any conspiracy to injure a citizen in the exercise 'of any right or privilege secured to him by the Constitution or laws of the United States'. Section 20 makes it a penal offense for anyone who, 'acting under color of any law' 'willfully subjects, or causes to be subjected, any inhabitant of any State * * * to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States'. The Government argues that the right of a qualified voter in a Louisiana congressional primary election to have his vote counted as cast is a right secured by Article I, &#167;&#167; 2 and 4 of the Constitution, and that a conspiracy to deprive the citizen of that right is a violation of &#167; 19, and also that the willful action of appellees as state officials, in falsely counting the ballots at the primary election and in falsely certifying the count, deprived qualified voters of that right and of the equal protection of the laws guaranteed by the Fourteenth Amendment, all in violation of &#167; 20 of the Criminal Code.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Article I, &#167; 2 of the Constitution, commands that 'The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the qualifications requisite for Electors of the most numerous Branch of the State Legislature'. By &#167; 4 of the same article 'The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators'. Such right as is secured by the Constitution to qualified voters to choose members of the House of Representatives is thus to be exercised in conformity to the requirements of state law subject to the restrictions prescribed by &#167; 2 and to the authority conferred on Congress by &#167; 4, to regulate  he times, places and manner of holding elections for representatives.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">We look then to the statutes of Louisiana here involved to ascertain the nature of the right which under the constitutional mandate they define and confer on the voter and the effect upon its exercise of the acts with which appellees are charged, all with the view to determining, first, whether the right or privilege is one secured by the Constitution of the United States, second, whether the effect under the state statute of appellee's alleged acts is such that they operate to injure or oppress citizens in the exercise of that right within the meaning of &#167; 19 and to deprive inhabitants of the state of that right within the meaning of &#167; 20, and finally, whether &#167;&#167; 19 and 20 respectively are in other respects applicable to the alleged acts of appellees.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">Pursuant to the authority given by &#167; 2 of Article I of the Constitution, and subject to the legislative power of Congress under &#167; 4 of Article I, and other pertinent provisions of the Constitution, the states are given, and in fact exercise a wide discretion in the formulation of a system for the choice by the people of representatives in Congress. In common with many other states Louisiana has exercised that discretion by setting up machinery for the effective choice of party candidates for representative in Congress by primary elections and by its laws it eliminates or seriously restricts the candidacy at the general election of all those who are defeated at the primary. All political parties, which are defined as those that have cast at least 5 per cent of the total vote at specified preceding elections, are required to nominate their candidates for representative by direct primary elections. Louisiana Act No. 46, Regular Session, 1940, &#167;&#167; 1 and 3.</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The primary is conducted by the state at public expense. Act No. 46, supra, &#167; 35. The primary, as is the general election, is subject to numerous statutory regulations as to the time, place and manner of conducting the election, including provisions to insure that the ballots cast at the primary are correctly counted, and the results of the count correctly recorded and certified to the Secretary of State, whose duty it is to place the names of the successful candidates of each party on the official ballot.<a class="footnote" href="#fn1" id="fn1_ref">1</a> The Secretary of State is prohibited from placing on the official ballot the name of any person as a candidate for any political party not nominated in accordance with the provisions of the Act. Act 46, &#167; 1.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">One whose name does not appear on the primary ballot, if otherwise eligible to become a candidate at the general election, may do so in either of two ways, by filing nomination papers with the requisite number of signatures or by having his name 'written in' on the ballot on the final election. Louisiana Act No. 224, Regular Session 1940, &#167;&#167; 50, 73. Section 87 of Act No. 46 provides 'No one who participates in the primary election of any political party shall have the right to participate in any primary election of any other political party, with a view of nominating opposing candidates, nor shall he be permitted to sign any nomination papers for  ny opposing candidate or candidates; nor shall he be permitted to be himself a candidate in opposition to any one nominated at or through a primary election in which he took part'.</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">Section 15 of Article VIII of the Constitution of Louisiana as amended by Act 80 of 1934, provides that 'no person whose name is not authorized to be printed on the official ballot, as the nominee of a political party or as an independent candidate, shall be considered a candidate,' unless he shall file in the appropriate office at least ten days before the general election a statement containing the correct name under which he is to be voted for and containing the further statement that he is willing and consents to be voted for for that office. The article also provides that 'no commissioners of election shall count a ballot as cast for any person whose name is not printed on the ballot or who does not become a candidate in the foregoing manner'. Applying these provisions the Louisiana Court of Appeals for the Parish of Orleans has held in Serpas v. Trebucq, <span class="citation" data-id="3473908"><a href="/opinion/3474685/serpas-v-trebucq/" aria-description="Citation for case: Serpas v. Trebucq">1 So.2d 346</a></span>, decided April 7, 1941, rehearing denied with opinion April 21, 1941, <span class="citation" data-id="3473283"><a href="/opinion/3474110/serpas-v-trebucq/" aria-description="Citation for case: Serpas v. Trebucq">1 So.2d 705</a></span>, that an unsuccessful candidate at the primary may not offer himself as a candidate at a general election, and that votes for him may not lawfully be written into the ballot or counted at such an election.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">The right to vote for a representative in Congress at the general election is, as a matter of law, thus restricted to the successful party candidate at the primary, to those not candidates at the primary who file nomination papers, and those whose names may be lawfully written into the ballot by the electors. Even if, as appellees argue, contrary to the decision in Serpas v. Trebucq, supra, voters may lawfully write into their ballots, cast at the general election, the name of a candidate rejected at the primary and have their ballots counted, the practical operation of the primary law in otherwise excluding from the ballot on the general election the names of candidates rejected at the primary is such as to impose serious restrictions upon the choice of candidates by the voters save by voting at the primary election. In fact, as alleged in the indictment, the practical operation of the primary in Louisiana, is and has been since the primary election was established in 1900 to secure the election of the Democratic primary nominee for the Second Congressional District of Louisiana.<a class="footnote" href="#fn2" id="fn2_ref">2</a></p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Interference with the right to vote in the Congressional primary in the Second Congressional District for the choice of Democratic candidate for Congress is thus as a matter of law and in fact an interference with the effective choice of the voters at the only stage of the election procedure when their choice is of significance, since it is at the only stage when such interference could have any practical effect on the ultimate result, the choice of the Congressman to represent the district. The primary in Louisiana is an integral part of the procedure for the popular choice of Congressman. The right of qualified voters to vote at the Congressional primary in Louisiana and to have their ballots counted is thus the right to participate in that choice.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">We come then to the question whether that right is one secured by the Constitution. Section 2 of Article I commands that Congressmen shall be chosen by the people of the several states by electors, the qualifications of which it prescribes. The right of the people to choose, whatever its appropriate constitutional limitations, where in other respects it is defined, and the mode of its exercise is prescribed by state action in conformity to the Cons itution, is a right established and guaranteed by the Constitution and hence is one secured by it to those citizens and inhabitants of the state entitled to exercise the right. Ex parte Yarbrough (The Ku-Klux Cases), <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 651</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">4 S.Ct. 152</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">238 U.S. 383</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>. And see Hague v. C.I.O., <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#508" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496, 508, 513, 526, 527, 529</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#960" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954, 960, 963, 969, 970</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span>, giving the same interpretation to the like phrase 'rights' 'secured by the Constitution' appearing in &#167; 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, <span class="citation no-link">8 U.S.C.A. &#167; 43</span>. While, in a loose sense, the right to vote for representatives in Congress is sometimes spoken of as a right derived from the states, see, Minor v. Happersett, <span class="citation" data-id="88998"><a href="/opinion/88998/minor-v-happersett/#170" aria-description="Citation for case: Minor v. Happersett">21 Wall. 162, 170</a></span>, <span class="citation" data-id="88998"><a href="/opinion/88998/minor-v-happersett/" aria-description="Citation for case: Minor v. Happersett">22 L.Ed. 627</a></span>; United States v. Reese, <span class="citation" data-id="9417037"><a href="/opinion/89266/united-states-v-reese/#217" aria-description="Citation for case: United States v. REESE">92 U.S. 214, 217, 218</a></span>, <span class="citation no-link">23 L.Ed. 563</span>; McPherson v. Blacker, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/#38" aria-description="Citation for case: McPherson v. Blacker">146 U.S. 1, 38, 39</a></span>, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/#11" aria-description="Citation for case: McPherson v. Blacker">13 S.Ct. 3, 11, 12</a></span>, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/" aria-description="Citation for case: McPherson v. Blacker">36 L.Ed. 869</a></span>; Breedlove v. Suttles, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/#283" aria-description="Citation for case: Breedlove v. Suttles">302 U.S. 277, 283</a></span>, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/#207" aria-description="Citation for case: Breedlove v. Suttles">58 S.Ct. 205, 207</a></span>, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/" aria-description="Citation for case: Breedlove v. Suttles">82 L.Ed. 252</a></span>, this statement is true only in the sense that the states are authorized by the Constitution, to legislate on the subject as provided by &#167; 2 of Art. I, to the extent that Congress has not restricted state action by the exercise of its powers to regulate elections under &#167; 4 and its more general power under Article I, &#167; 8, clause 18 of the Constitution 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers'. See Ex parte Siebold, <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">100 U.S. 371</a></span>, <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">25 L.Ed. 717</a></span>; Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#664" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 663, 664</a></span>, <span class="citation no-link">4 S.Ct. 158</span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; Swafford v. Templeton, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">185 U.S. 487</a></span>, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">22 S.Ct. 783</a></span>, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">46 L.Ed. 1005</a></span>; Wiley v. Sinkler, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/#64" aria-description="Citation for case: Wiley v. Sinkler">179 U.S. 58, 64</a></span>, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/#20" aria-description="Citation for case: Wiley v. Sinkler">21 S.Ct. 17, 20</a></span>, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/" aria-description="Citation for case: Wiley v. Sinkler">45 L.Ed. 84</a></span>.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">Obviously included within the right to choose, secured by the Constitution, is the right of qualified voters within a state to cast their ballots and have them counted at Congressional elections. This Court has consistently held that this is a right secured by the Constitution. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> Wiley v. <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/" aria-description="Citation for case: Wiley v. Sinkler">Sinkler, supra;</a></span> Swafford v. <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">Templeton, supra;</a></span> United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra;</a></span> see Ex parte <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">Siebold, supra;</a></span> In re Coy, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">127 U.S. 731</a></span>, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">8 S.Ct. 1263</a></span>, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">32 L.Ed. 274</a></span>; Logan v. United States, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">12 S.Ct. 617</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">36 L.Ed. 429</a></span>. And since the constitutional command is without restriction or limitation, the right unlike those guaranteed by the Fourteenth and Fifteenth Amendments, is secured against the action of individuals as well as of states. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> Logan v. United States, supra.</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">But we are now concerned with the question whether the right to choose at a primary election, a candidate for election as representative, is embraced in the right to choose representatives secured by Article I, &#167; 2. We may assume that the framers of the Constitution in adopting that section, did not have specifically in mind the selection and elimination of candidates for Congress by the direct primary any more than they contemplated the application of the commerce clause to interstate telephone, telegraph and wireless communication which are concededly within it. But in determining whether a provision of the Constitution applies to a new subject matter, it is of little significance that it is one with which the framers were not familiar. For in setting up an enduring framework of government they undertook to carry out for the indefinite future and in all the vicissitudes of the changing affairs of men, those fundamental purposes which the instrument itself discloses. Hence we read its words, not as we read legislative codes which are subject to continuous revision with the changing course of events, but as the revelation of the great purposes which were intended to be achieved by the Constitution as a continuing instrument of government. Cf. Davidson v. New Orleans, <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">96 U.S. 97</a></span>, <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">24 L.Ed. 616</a></span>; Brown v. Walker, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#595" aria-description="Citation for case: Brown v. Walker">161 U.S. 591, 595</a></span>, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#646" aria-description="Citation for case: Brown v. Walker">16 S.Ct. 644, 646</a></span>, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">40 L.Ed. 819</a></span>; Robertson v. Baldwin, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/#281" aria-description="Citation for case: Robertson v. Baldwin">165 U.S. 275, 281, 282</a></span>, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/#328" aria-description="Citation for case: Robertson v. Baldwin">17 S.Ct. 326, 328, 329</a></span>, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/" aria-description="Citation for case: Robertson v. Baldwin">41 L.Ed. 715</a></span>. If we r member that 'it is a Constitution we are expounding', we cannot rightly prefer, of the possible meanings of its words, that which will defeat rather than effectuate the Constitutional purpose.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">That the free choice by the people of representatives in Congress, subject only to the restrictions to be found in &#167;&#167; 2 and 4 of Article I and elsewhere in the Constitution, was one of the great purposes of our Constitutional scheme of government cannot be doubted. We cannot regard it as any the less the constitutional purpose or its words as any the less guarantying the integrity of that choice when a state, exercising its privilege in the absence of Congressional action, changes the mode of choice from a single step, a general election, to two, of which the first is the choice at a primary of those candidates from whom, as a second step, the representative in Congress is to be chosen at the election.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">Nor can we say that that choice which the Constitution protects is restricted to the second step because &#167; 4 of Article I, as a means of securing a free choice of representatives by the people, has authorized Congress to regulate the manner of elections, without making any mention of primary elections. For we think that the authority of Congress, given by &#167; 4, includes the authority to regulate primary elections when, as in this case, they are a step in the exercise by the people of their choice of representatives in Congress. The point whether the power conferred by &#167; 4 includes in any circumstances the power to regulate primary elections was reserved in United States v. <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra,</a></span> <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 487</a></span>, <span class="citation no-link">37 S.Ct. 411</span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>. In Newberry v. United States, supra, four Justices of this Court were of opinion that the term 'elections' in &#167; 4 of Article I did not embrace a primary election since that procedure was unknown to the framers. A fifth Justice who with them pronounced the judgment of the Court, was of opinion that a primary, held under a law enacted before the adoption of the Seventeenth Amendment, for the nomination of candidates for Senator, was not an election within the meaning of &#167; 4 of Article I of the Constitution, presumably because the choice of the primary imposed no legal restrictions on the election of Senators by the state legislatures to which their election had been committed by Article I, &#167; 3. The remaining four Justices were of the opinion that a primary election for the choice of candidates for Senator or Representative were elections subject to regulation by Congress within the meaning of &#167; 4 of Article I. The question then has not been prejudged by any decision of this Court.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">To decide it we turn to the words of the Constitution read in their historical setting as revealing the purpose of its framers, and in search for admissible meanings of its words which, in the circumstances of their application, will effectuate those purposes. As we have said, a dominant purpose of &#167; 2, so far as the selection of representatives in Congress is concerned, was to secure to the people the right to choose representatives by the designated electors, that is to say, by some form of election. Cf. the Seventeenth Amendment as to popular 'election' of Senators. From time immemorial an election to public office has been in point of substance no more and no less than the expression by qualified electors of their choice of candidates.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">Long before the adoption of the Constitution the form and mode of that expression had changed from time to time. There is no historical warrant for supposing that the framers were under the illusion that the method of effecting the choice of the electors would never change or that if it did, the change was for that reason to be permitted to defeat the right of the people to choose representatives for Congress which the Constitution had guaranteed. The right to participate in the choice of representatives for Congress includes, as we have said, the right to cast a ballot and to have it counted at the general el ction whether for the successful candidate or not. Where the state law has made the primary an integral part of the procedure of choice, or where in fact the primary effectively controls the choice, the right of the elector to have his ballot counted at the primary, is likewise included in the right protected by Article I, &#167; 2. And this right of participation is protected just as is the right to vote at the election, where the primary is by law made an integral part of the election machinery, whether the voter exercises his right in a party primary which invariably, sometimes or never determines the ultimate choice of the representative. Here, even apart from the circumstance that the Louisiana primary is made by law an integral part of the procedure of choice, the right to choose a representative is in fact controlled by the primary because, as is alleged in the indictment, the choice of candidates at the Democratic primary determines the choice of the elected representative. Moreover, we cannot close our eyes to the fact already mentioned that the practical influence of the choice of candidates at the primary may be so great as to affect profoundly the choice at the general election even though there is no effective legal prohibition upon the rejection at the election of the choice made at the primary and may thus operate to deprive the voter of his constitutional right of choice. This was noted and extensively commented upon by the concurring Justices in Newberry v. United States, supra, 256 U.S. 263&#8212;269, 285, 287, <span class="citation no-link">41 S.Ct. 476</span> 478, 484, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Unless the constitutional protection of the integrity of 'elections' extends to primary elections, Congress is left powerless to effect the constitutional purpose, and the popular choice of representatives is stripped of its constitutional protection save only as Congress, by taking over the control of state elections, may exclude from them the influence of the state primaries.<a class="footnote" href="#fn3" id="fn3_ref">3</a> Such an expedient would end that state autonomy with respect to elections which the Constitution contemplated that Congress should be free to leave undisturbed, subject only to such minimum regulation as it should find necessary to insure the freedom and integrity of the choice. Words, especially those of a constitution, are not to be read with such stultifying narrowness. The words of &#167;&#167; 2 and 4 of Article I, read in the sense which is plainly permissible and in the light of the constitutional purpose, require us to hold that a primary election which involves a necessary step in the choice of candidates for election as representatives in Congress, and which in the circumstances of this case controls that choice, is an election within the meaning of the constitutional provision and is subject to congressional regulation as to the manner of holding it.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Not only does &#167; 4 of Article I authorize Congress to regulate the manner of holding elections, but by Article I, &#167; 8, Clause 18, Congress is given authority 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.' This provision leaves to the Congress the choice of means by which its constitutional powers are to be carried into execution. 'L t the end be legitimate, let it be within the scope of the constitution, and all means which are appropriate, which are plainly adapted to that end, which are not prohibited, but consist with the letter and spirit of the constitution, are constitutional'. McCulloch v. Maryland, <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#421" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 421</a></span>, <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 L.Ed. 579</a></span>. That principle has been consistently adhered to and liberally applied, and extends to the congressional power by appropriate legislation to safeguard the right of choice by the people of representatives in Congress secured by &#167; 2 of Article I. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#658" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 657, 658</a></span>, <span class="citation no-link">4 S.Ct. 154</span>, 155, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; cf. Second Employers' Liability Cases, (Mondou v. New York, N.H. &amp; H.R. Co.), <span class="citation" data-id="98132"><a href="/opinion/98132/miller-v-united-states/#49" aria-description="Citation for case: Miller v. United States">233 U.S. 1, 49</a></span>, <span class="citation" data-id="8142543"><a href="/opinion/8180624/mondou-v-new-york-new-haven-hartford-railroad/#174" aria-description="Citation for case: Mondou v. New York, New Haven &amp; Hartford Railroad">32 S.Ct. 169, 174</a></span>, <span class="citation" data-id="2620807"><a href="/opinion/2620807/second-employersliability-cases/" aria-description="Citation for case: Second Employers&#x27;liability Cases">56 L.Ed. 327</a></span>, 38 L.R.A.,N.S., 44; Houston &amp; Texas Ry. Co. v. United States, <span class="citation" data-id="98232"><a href="/opinion/98232/houston-east-west-texas-railway-co-v-united-states/#350" aria-description="Citation for case: Houston, East &amp; West Texas Railway Co. v. United States">234 U.S. 342, 350, 355</a></span>, <span class="citation" data-id="98232"><a href="/opinion/98232/houston-east-west-texas-railway-co-v-united-states/#835" aria-description="Citation for case: Houston, East &amp; West Texas Railway Co. v. United States">34 S.Ct. 833, 835, 838</a></span>, <span class="citation no-link">58 L.Ed. 341</span>; Wilson v. New et al., <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/#346" aria-description="Citation for case: Wilson v. New">243 U.S. 332, 346, 347</a></span>, <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/#301" aria-description="Citation for case: Wilson v. New">37 S.Ct. 298, 301</a></span>, <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/" aria-description="Citation for case: Wilson v. New">61 L.Ed. 755</a></span>, L.R.A.1917E, 938, Ann.Cas.1918A, 1024; First National Bank v. Union Trust Company, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/#419" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">244 U.S. 416, 419</a></span>, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/#735" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">37 S.Ct. 734, 735</a></span>, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">61 L.Ed. 1233</a></span>, L.R.A.1918C, 283, Ann.Cas.1918D, 1169; Selective Draft Cases, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/#381" aria-description="Citation for case: Selective Draft Law Cases">245 U.S. 366, 381</a></span>, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/#162" aria-description="Citation for case: Selective Draft Law Cases">38 S.Ct. 159, 162</a></span>, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/" aria-description="Citation for case: Selective Draft Law Cases">62 L.Ed. 349</a></span>, L.R.A.1918C, 361, Ann.Cas.1918B, 856; United States v. Ferger et al., <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/#205" aria-description="Citation for case: United States v. Ferger">250 U.S. 199, 205</a></span>, <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/#446" aria-description="Citation for case: United States v. Ferger">39 S.Ct. 445, 446</a></span>, <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/" aria-description="Citation for case: United States v. Ferger">63 L.Ed. 936</a></span>; Hamilton v. Kentucky Distilleries Co., <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/#155" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">251 U.S. 146, 155, 163</a></span>, <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/#107" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">40 S.Ct. 106, 107, 110</a></span>, <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">64 L.Ed. 194</a></span>; Jacob Ruppert v. Caffey, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">251 U.S. 264</a></span>, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">40 S.Ct. 141</a></span>, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">64 L.Ed. 260</a></span>; Smith v. Kansas City Title &amp; Trust Co., <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">255 U.S. 180</a></span>, <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">41 S.Ct. 243</a></span>, <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">65 L.Ed. 577</a></span>; United States v. Darby, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">312 U.S. 100</a></span>, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">61 S.Ct. 451</a></span>, 85 L.Ed. &#8212;-, <span class="citation no-link">132 A.L.R. 1430</span>, decided February 3, 1941, and cases cited.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">There remains the question whether &#167;&#167; 19 and 20 are an exercise of the congressional authority applicable to the acts with which appellees are charged in the indictment. Section 19 makes it a crime to conspire to 'injure' or 'oppress' any citizen 'in the free exercise * * * of any right or privilege secured to him by the Constitution'.<a class="footnote" href="#fn4" id="fn4_ref">4</a> In Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> and in United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra,</a></span> as we have seen, it was held that the right to vote in a congressional election is a right secured by the Constitution, and that a conspiracy to prevent the citizen from voting or to prevent the official count of his ballot when cast, is a conspiracy to injure and oppress the citizen in the free exercise of a right secured by the Constitution within the meaning of &#167; 19. In reaching this conclusion the Court found no uncertainty or ambiguity in the statutory language, obviously devised to protect the citizen 'in the free exercise * * * of any right or privilege secured to him by the Constitution', and concerned itself with the question whether the right to participate in choosing a representative is so secured.<a class="footnote" href="#fn5" id="fn5_ref">5</a> Such is our function here. Conspiracy to prevent the official count of a citizen's ballot, held in United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra,</a></span> to be a violation of &#167; 19 in the case of a congressional election, is equally a conspiracy to injure and oppress the citizen when the ballots are cast in a primary election prerequisite to the choice of party candidates for a congressional election. In both cases the right infringed is one secured by the Constitution. The injury suffered by the citizen in the exercise of the right is an injury which the statute describes and to which it applies in the one case as in the other.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">The suggestion that &#167; 19, concededly applicable to conspiracies to deprive electors of their votes at congressional elections, is not sufficiently specific to be deemed applicable to primary elections, will hardly bear examination. Section 19 speaks neither of elections nor of primaries. In unambiguous language it protects 'any right or privilege secured * * * by the Constitution', a phrase which as we have seen extends to the right of the voter to have his vote counted in both the general election and in the primary election, where the latter is a part of the election machinery, as well as to numerous other constitutional rights which are wholly unrelated to the choice of a representative in Congress. United States v. Waddell, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">112 U.S. 76</a></span>, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">5 S.Ct. 35</a></span>, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">28 L.Ed. 673</a></span>; Logan v. United States, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">12 S.Ct. 617</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">36 L.Ed. 429</a></span>; In re Quarles, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">158 U.S. 532</a></span>, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">15 S.Ct. 959</a></span>, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">39 L.Ed. 1080</a></span>; Motes v. United States, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">178 U.S. 458</a></span>, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">20 S.Ct. 993</a></span>, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">44 L.Ed. 1150</a></span>; Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124.</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">In the face of the broad language of the statute, we are pointed to no principle of statutory construction and to no significant legislative history which could be thought to sanction our saying that the statute applies any the less to primaries than to elections, where in one as in the other it is the same constitutional right which is infringed. It does not avail to attempt to distinguish the protection afforded by &#167; 1 of the Civil Rights Act of 1871,<a class="footnote" href="#fn6" id="fn6_ref">6</a> to the right to participate in primary as well as general elections, secured to all citizens by the Constitution, see Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124; Nixon v. Herndon, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">273 U.S. 536</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">47 S.Ct. 446</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">71 L.Ed. 759</a></span>; Nixon v. Condon, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">286 U.S. 73</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">52 S.Ct. 484</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">76 L.Ed. 984</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">88 A.L.R. 458</a></span>; Lane v. Wilson, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">307 U.S. 268</a></span>, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">59 S.Ct. 872</a></span>, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">83 L.Ed. 1281</a></span>, on the ground that in those cases the injured citizens were Negroes whose rights were clearly protected by the Fourteenth Amendment. At least since Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> and no member of the Court seems ever to have questioned it, the right to participate in the choice of representatives in Congress has been recognized as a right protected by Art. I, &#167;&#167; 2 and 4 of the Constitution.<a class="footnote" href="#fn7" id="fn7_ref">7</a> Differences of opinion have arisen as to the effect of the primary in particular cases on the choice of representatives. But we are troubled by no such doubt here. Hence, the right to participate through the primary in the choice of representatives in Congress&#8212;a right clearly secured by the Constitution&#8212;is within the words and purpose of &#167; 19 in the same manner and to the same extent as the right to vote at the general election. United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra.</a></span> It is no extension of the criminal statute, as it was not of the civil statute in Nixon v. <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">Herndon, supra,</a></span> to find a violation of it in a new method of interference with the right which its words protect. For it is the constitutional right, regardless of the method of interference, which is the subject of the statute and which in precise terms it protects from injury and oppression.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">It is hardly the performance of the judicial function to construe a statute, which in terms protects a right secured by the Constitution, here the right to choose a representative in Congress, as applying to an election whose only function is to ratify a choice already made at the primary but as having no application to the primary which is the only effective means of choice. To withdraw from the scope of the statute, an effective interference with the constitutional right of choice, because other wholly different situations not now before us may not be found to involve such an interference, cf. United States v. Bathgate, <span class="citation" data-id="1087873"><a href="/opinion/1087873/united-states-v-bathgate/" aria-description="Citation for case: United States v. Bathgate">246 U.S. 220</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">38 S.Ct. 269</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>; United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, is to say that acts plainly within the statute should be deemed to be without it because other hypothetical cases may later be found not to infringe the constitutional right with which alone the statute is concerned.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">If a right secured by the Constitution may be infringed by the corrupt failure to include the vote at a primary in the official count, it is not significant that the primary, like the voting machine, was unknown when &#167; 19 was adopted.<a class="footnote" href="#fn8" id="fn8_ref">8</a> Abuse of either may infringe the right and therefore violate &#167; 19. See United States v. Pleva, 2 Cir., <span class="citation" data-id="9639102"><a href="/opinion/1488148/united-states-v-pleva/#530" aria-description="Citation for case: United States v. Pleva">66 F.2d 529, 530</a></span>; cf. Browder v. United States, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/" aria-description="Citation for case: Browder v. United States">312 U.S. 335</a></span>, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/" aria-description="Citation for case: Browder v. United States">61 S.Ct. 599</a></span>, 85 L.Ed. &#8212;-. Nor does the fact that in circumstances not here present there may be difficulty in determining whether the primary so affects the right of the choice as to bring it within the constitutional protection, afford any ground for doubting the construction and application of the statute once the constitutional question is resolved. That difficulty is inherent in the judicial administration of every federal criminal statute, for none, whatever its terms, can be applied beyond the reach of the congressional power which the Constitution confers. Standard Sanitary Mfg. Co. v. United States, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">226 U.S. 20</a></span>, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">33 S.Ct. 9</a></span>, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">57 L.Ed. 107</a></span>; Hoke v. United States, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">227 U.S. 308</a></span>, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">33 S.Ct. 281</a></span>, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">57 L.Ed. 523</a></span>, 43 L.R.A.,N.S., 906, Ann.Cas.1913E, 905; Nash v. United States, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">229 U.S. 373</a></span>, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">33 S.Ct. 780</a></span>, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">57 L.Ed. 1232</a></span>; United States v. Freeman, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">239 U.S. 117</a></span>, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">36 S.Ct. 32</a></span>, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">60 L.Ed. 172</a></span>; United States v. F. W. Darby, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">312 U.S. 100</a></span>, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">61 S.Ct. 451</a></span>, 85 L.Ed. &#8212;-, <span class="citation no-link">132 A.L.R. 1430</span>, decided February 3, 1941.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">The right of the voters at the primary to have their votes counted is, as we have stated, a right or privilege secured by the Constitution, and to this &#167; 20 also gives protection.<a class="footnote" href="#fn9" id="fn9_ref">9</a> The alleged acts of appellees were committed in the course of their performance of duties unde  the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election. Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law. Ex parte Virginia, <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339, 346</a></span>, <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">25 L.Ed. 676</a></span>; Home Telephone &amp; Telegraph Co. v. Los Angeles, <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#287" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U.S. 278, 287</a></span>, et seq., <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#314" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">33 S.Ct. 312, 314</a></span>, <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">57 L.Ed. 510</a></span>; Hague v. C.I.O., <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#507" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496, 507, 519</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#960" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954, 960, 965</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span>; cf. <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">Id.,</a></span> 3 Cir., <span class="citation" data-id="9640063"><a href="/opinion/1494037/hague-v-committee-for-industrial-organization/#790" aria-description="Citation for case: Hague v. Committee for Industrial Organization">101 F.2d 774, 790</a></span>. Here the acts of appellees infringed the constitutional right and deprived the voters of the benefit of it within the meaning of &#167; 20, unless by its terms its application is restricted to deprivations 'on account of (an) inhabitant being an alien, or by reason of his color, or race'.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">The last clause of &#167; 20 protects inhabitants of a state from being subjected to different punishments, pains or penalties by reason of alienage, color or race, than are prescribed for the punishment of citizens. That the qualification with respect to alienage, color and race, refers only to differences in punishment and not to deprivations of any rights or privileges secured by the Constitution, is evidenced by the structure of the section and the necessities of the practical application of its provisions. The qualification as to alienage, color and race, is a parenthetical phrase in the clause penalizing different punishments 'than are prescribed for * * * citizens' and in the common use of language could refer only to the subject matter of the clause and not to that of the earlier one relating to the deprivation of rights to which it makes no reference in terms.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">Moreover the prohibited differences of punishment on account of alienage, color or race, are those referable to prescribed punishments which are to be compared with those prescribed for citizens. A standard is thus set up applicable to differences in prescribed punishments on account of alienage, color or race, which it would be difficult if not impossible to apply to the willful deprivations of constitutional rights or privileges, in order to determine whether they are on account of alienage, color or race. We think that &#167; 20 authorizes the punishment of two different offenses. The one is willfully subjecting any inhabitant to the deprivation of rights secured by the Constitution; the other is willfully subjecting any inhabitant to different punishments on account of his color or race, than are prescribed for the punishment of citizens. The meager legislative history of the section supports this conclusion.<a class="footnote" href="#fn10" id="fn10_ref">10</a></p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">So interpreted &#167; 20 applies to deprivation of the constitutional rights of qualified voters to choose representatives in Congress. The generality of the section made applicable as it is to deprivations of any constitutional right, does not obscure its meaning or impair its force within the scope of its application, which is restricted by its terms to deprivations which are willfully inflicted by those acting under color of any law, statute and the like.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">We do not discuss the application of &#167; 20 to deprivations of the right to equal protection of the laws guaranteed by the Fourteenth Amendment, a point apparently raised and discussed for the first time in the Government's brief in this Court. The point was not specially considered or decided by the court below, and has not been assigned as error by the Government. Since the indictment on its face does not purport to charge a deprivation of equal protection to voters or candidates, we are not called upon to construe the indictment in order to raise a question of statutory validity or construction which we are alone authorized to review upon this appeal.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">Reversed.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">The Chief Justice took no part in the consideration or decision of this case.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">Mr. Justice DOUGLAS, dissenting.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">Free and honest elections are the very foundation of our republican form of government. Hence any attempt to defile the sanctity of the ballot cannot be viewed with equanimity. As stated by Mr. Justice Miller in Ex parte Yarbrough (The Ku-Klux Cases), <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#666" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 651, 666</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#159" aria-description="Citation for case: Ex Parte Yarbrough">4 S.Ct. 152, 159</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>, 'the temptations to control these elections by violence and by corruption' have been a constant source of danger in the history of all republics. The acts here charged, if proven, are of a kind which carries that threat and are highly offensive. Since they corrupt the process of Congressional elections, they transcend mere local concern and extend a contaminating influence into the national domain.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">I think Congress has ample power to deal with them. That is to say I disagree with Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>, to the extent that it holds that Congress has no power to control primary elections. Art. I, &#167; 2 of the Constitution provides that 'The House of Representatives shall be composed of Members chosen every second Year by the People of the several States.' Art. I, &#167; 4 provides that 'The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators.' And Art. I, &#167; 8, clause 18 gives Congress the power 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.' Those sections are an arsenal of power ample to protect Congressional elections from any and all forms of pollution. The fact that a particular form of pollution has only an indirect effect on the final election is immaterial. The fact that it occurs in a primary election or nominating convention is likewise irrelevant. The important consideration is that the Constitution should be interpreted broadly so as to give to the representatives of a free people abundant power to deal with all the exigencies of the electoral process. It means that the Constitution should be read so as to give Congress an expansive implied power to place beyond the pale acts which, in their direct or indirect effect, impair the integrity of Congressional elections. For when corruption enters, the election is no longer free, the choice of the people is affected. To hold that Congress is powerless to control these primaries would indeed be a narrow construction of the Constitution inconsistent with the view that that instrument of government was designed not only for contemporary needs but for the vicissitudes of time.</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">So I agree with most of the views expressed in the opinion of the Court. And it is with diffidence that I dissent from the result there reached.</p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">The disagreement centers on the meaning of &#167; 19 of the Criminal Code which protects every right secured by the Constitution. The right to vote at a final Congressional election and the right to have one's vote counted in such an election have been held to be protected by &#167; 19. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">238 U.S. 383</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>. Yet I do not think that the principles of those cases should be, or properly can be, extended to primary elections. To sustain this indictment we must so extend them. But when we do, we enter perilous territory.</p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">We enter perilous territory because, as stated in United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#485" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476, 485</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#410" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407, 410</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, there is no common law offense against the United States; 'the legislative authority of the Union must first make an act a crime, affix a punishment to it, and declare the Court that shall have jurisdiction of the offence.' United States v. Hudson, <span class="citation" data-id="84968"><a href="/opinion/84968/the-united-states-v-hudson-and-goodwin/#34" aria-description="Citation for case: The United States v. Hudson and Goodwin">7 Cranch 32, 34</a></span>, <span class="citation" data-id="84968"><a href="/opinion/84968/the-united-states-v-hudson-and-goodwin/" aria-description="Citation for case: The United States v. Hudson and Goodwin">3 L.Ed. 259</a></span>. If a person is to be convicted of a crime, the offense must be clearly and plainly embraced within the statute. As stated by Chief Justice Marshall in United States v. Wiltberger, <span class="citation" data-id="6607979"><a href="/opinion/6726712/united-states-v-wiltberger/#105" aria-description="Citation for case: United States v. Wiltberger">5 Wheat. 76, 105</a></span>, <span class="citation" data-id="6607979"><a href="/opinion/6726712/united-states-v-wiltberger/" aria-description="Citation for case: United States v. Wiltberger">5 L.Ed. 37</a></span>, 'probability is not a guide which a court, in construing a penal statute, can safely take.' It is one thing to allow wide and generous scope to the express and implied powers of Congress; it is distinctly another to read into the vague and general language of an act of Congress specifications of crimes. We should ever be mindful that 'before a man can be punished, his case must be plainly and unmistakably within the statute.' United States v. Lacher, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/#628" aria-description="Citation for case: United States v. Lacher">134 U.S. 624, 628</a></span>, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/#626" aria-description="Citation for case: United States v. Lacher">10 S.Ct. 625, 626</a></span>, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/" aria-description="Citation for case: United States v. Lacher">33 L.Ed. 1080</a></span>. That admonition is reemphasized here by the fact that &#167; 19 imposes not only a fine of $5,000 and ten years in prison but also makes him who is convicted 'ineligible to any office, or place of honor, profit, or trust created by the Constitution or laws of the United States.' It is not enough for us to find in the vague penumbra of a statute some offense about which Congress could have legislated and then to particularize it as a crime because it is highly offensive. Cf. James v. Bowman, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">190 U.S. 127</a></span>, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">23 S.Ct. 678</a></span>, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">47 L.Ed. 979</a></span>. Civil liberties are too dear to permit conviction for crimes which are only implied and which can be spelled out only by adding inference to inference.</p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">Sec. 19 does not purport to be an exercise by Congress of its power to regulate primaries. It merely penalizes conspiracies 'to injure, oppress, threaten, or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States'. Thus, it does no more than refer us to the Constitution<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> for the purpose of determining whether or not the right to vote in a primary is there secured. Hence we must do more than find in the Constitution the power of Congress to afford that protection. We must find that protection on the face of the Constitution itself. That is to say, we must in view of the wording of &#167; 19 read the relevant provisions of the Constitution for the purposes of this case through the window of a criminal statute.</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p class="indent">There can be put to one side cases where state election officials deprive negro citizens of their right to vote at a general election (Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124), or at a primary. Nixon v. Herndon, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">273 U.S. 536</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">47 S.Ct. 446</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">71 L.Ed. 759</a></span>; Nixon v. Condon, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">286 U.S. 73</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">52 S.Ct. 484</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">76 L.Ed. 984</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">88 A.L.R. 458</a></span>. Discrimination on the basis of race or color is plainly outlawed by the Fourteenth Amendment. Since the constitutional mandate is plain, there is no reason why &#167; 19 or &#167; 20 should not be applicable. But the situation here is quite different. When we turn to the constitutional provisions relevant to this case we find no such unambiguous mandate.</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent">Art. I, &#167; 4 specifies the machinery whereby the times, places and manner of holding elections shall be established and controlled. Art. I, &#167; 2 provides that representatives shall be 'chosen' by the people. But for purposes of the criminal law as contrasted to the interpretation of the Constitution as the source of the implied power of Congress, I do not  hink that those provisions in absence of specific legislation by Congress protect the primary election or the nominating convention. While they protect the right to vote and the right to have one's vote counted at the final election as held in the Yarbrough and Mosley cases, they certainly do not per se extend to all acts which is their indirect or incidental effect restrain, restrict, or interfere with that choice. Bribery of voters at a general election certainly is an interference with that freedom of choice. It is a corruptive influence which for its impact on the election process is as intimate and direct as the acts charged in this indictment. And Congress has ample power to deal with it. But this Court in United States v. Bathgate, <span class="citation" data-id="1087873"><a href="/opinion/1087873/united-states-v-bathgate/" aria-description="Citation for case: United States v. Bathgate">246 U.S. 220</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">38 S.Ct. 269</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>, by a unanimous vote, held that conspiracies to bribe voters at a general election were not covered by &#167; 19. While the conclusion in that case may be reconciled with the results in the Yarbrough and Mosley cases on the ground that the right to vote at a general election is personal while the bribery of voters only indirectly affects that personal right, that distinction is not of aid here. For the failure to count votes cast at a primary has by the same token only an indirect effect on the voting at the general election. In terms of causal effect tampering with the primary vote may be as important on the outcome of the general election as bribery of voters at the general election itself. Certainly from the viewpoint of the individual voter there is as much a dilution of his vote in the one case as in the other. So, in light of the Mosley and Bathgate cases, the test under &#167; 19 is not whether the acts in question constitute an interference with the effective choice of the voters. It is whether the voters are deprived of their votes in the general election. Such a test comports with the standards for construction of a criminal law, since it restricts &#167; 19 to protection of the rights plainly and directly guaranteed by the Constitution. Any other test entails an inquiry into the indirect or incidental effect on the general election of the acts done. But in view of the generality of the words employed such a test would be incompatible with the criteria appropriate for a criminal case.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The Mosley case, in my view, went to the verge when it held that &#167; 19 and the relevant constitutional provisions made it a crime to fail to count votes cast at a general election. That Congress intended &#167; 19 to have that effect was none too clear. The dissenting opinion of Mr. Justice Lamar in that case points out that &#167; 19 was originally part of the Enforcement Act of May 31, 1870, c. 114, &#167; 6, <span class="citation no-link">16 Stat. 140</span>. Under another section of that act (&#167; 4), which was repealed by the Act of February 8, 1894 (<span class="citation no-link">28 Stat. 36</span>) the crime charged in the Mosley case would have been punishable by a fine of not less than $500 and imprisonment for 12 months.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> Under &#167; 19 it carried, as it still does, a penalty of $5000 and ten years in prison. The Committee Report (H.Rep. No. 18, 53d Cong., 1st Sess.) which recommended the repeal of other sections clearly indicated an intent to remove the hand of the Federal Government from such elections and to restore their conduct and policing to the states. As the Report stated (p. 7): 'Let every trace of the reconstruction measures be wiped from the statute books; let the States of this great Union understand that the elections are in their own hands, and if there be fraud, coercion, or force used they will be the first to feel it. Responding to a universal sentiment throughout the country for greater purity in elections many of our States have enacted laws to protect the voter and to purify the ballot. These, under the guidance of State officers, have worked efficiently, satisfactorily, and beneficently; and if these Federal statutes are repealed that sentiment will receive an impetus which, if the cause still exists, will carry such enactments in every State in the Union.' I  view of this broad, comprehensive program of repeal it is not easy to conclude that the general language of &#167; 19 which was not repealed not only continued in effect much which had been repealed but also upped the penalties for certain offenses which had been explicitly covered by one of the repealed sections. Mr. Justice Holmes, writing for the majority in the Mosley case, found in the legislative and historical setting of &#167; 19 and in its revised form a Congressional interpretation which, if &#167; 19 were taken at its face value, was thought to afford voters in final Congressional elections general protection. And that view is a tenable one since &#167; 19 originally was part of an Act regulating general elections and since the acts charged had a direct rather than an indirect effect on the right to vote at a general election.</p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">But as stated by a unanimous court in United States v. <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra,</a></span> 243 U.S. page 486, 37 S.Ct. page 411, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, the Mosley case 'falls far short' of making &#167; 19 'applicable to the conduct of a state nominating primary'. Indeed, Mr. Justice Holmes, the author of the Mosley opinion, joined with Mr. Justice McReynolds in the Newberry case in his view that Congress had no authority under Art. I, &#167; 4 of the Constitution of legislate on primaries. When &#167; 19 was part of the Act of May 31, 1870, it certainly would never have been contended that it embraced primaries, for they were hardly known at that time.<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a> It is true that 'even a criminal statute embraces everything which subsequently falls within its scope.' Browder v. United States, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/#340" aria-description="Citation for case: Browder v. United States">312 U.S. 335, 340</a></span>, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/#602" aria-description="Citation for case: Browder v. United States">61 S.Ct. 599, 602</a></span>, 85 L.Ed. &#8212;-. Yet the attempt to bring under &#167; 19 offenses 'committed in the conduct of primary elections or nominating caucuses or conventions' was rejected in the Gradwell case, where this Court said that in absence of legislation by Congress on the subject of primaries it is not for the courts 'to attempt to supply it by stretching old statutes to new uses, to which they are not adapted and for which they were not intended. * * * the section of the Criminal Code relied upon, originally enacted for the protection of the civil rights of the then lately enfranchised negro, cannot be extended so as to make it an agency for enforcing a state primary law.' 243 U.S. pages 488, 489, 37 S.Ct. page 411, 412, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>. The fact that primaries were hardly known when &#167; 19 was enacted, the fact that it was part of a legislative program governing general elections not primary elections, the fact that it has been in nowise implemented by legislation directed at primaries give credence to the unanimous view in the Gradwell case that &#167; 19 has not by the mere passage of time taken on a new and broadened meaning. At least it seems plain that the difficulties of applying the historical reason adduced by Mr. Justice Holmes in the Mosley case to bring general elections within &#167; 19 are so great in case of primaries that we have left the safety zone of interpretation of criminal statutes when we sustain this indictment. It is one thing to say, as in the Mosley case, that Congress was legislating as respects general elections when it passed &#167; 19. That was the fact. It is qu te another thing to say that Congress by leaving &#167; 19 unmolested for some seventy years has legislated unwittingly on primaries. Sec. 19 was never part of an act of Congress directed towards primaries. That was not its original frame of reference. Therefore, unlike the Mosley case, it cannot be said here that &#167; 19 still covers primaries because it was once an integral part of primary legislation.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">Furthermore, the fact that Congress has legislated only sparingly and at infrequent intervals even on the subject of general elections (United States v <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra)</a></span> should make us hesitate to conclude that by mere inaction Congress has taken the greater step, entered the field of primaries, and gone further than any announced legislative program has indicated. The acts here charged constitute crimes under the Louisiana statute. La.Act No. 46, Reg.Sess.1940, &#167; 89. In absence of specific Congressional action we should assume that Congress has left the control of primaries and nominating conventions to the states&#8212;an assumption plainly in line with the Committee Report, quoted above, recommending the repeal of portions of the Enforcement Act of May 31, 1870 so as to place the details of elections in state hands. There is no ground for inference in subsequent legislative history that Congress has departed from that policy by superimposing its own primary penal law on the primary penal laws of the states. Rather, Congress has been fairly consistent in recognizing state autonomy in the field of elections. To be sure, it has occasionally legislated on primaries.<a class="footnote" href="#fn4-1" id="fn4-1_ref">4</a> But even when dealing specifically with the nominating process, it has never made acts of the kind here in question a crime. In this connection it should be noted that the bill which became the Hatch Act, <span class="citation no-link">53 Stat. 1147</span>, <span class="citation no-link">18 U.S.C. &#167; 61</span> et seq., <span class="citation no-link">18 U.S.C.A. &#167; 61</span> et seq., contained a section which made it unlawful 'for any person to intimidate, threaten, or coerce, or to attempt to intimidate, threaten, or coerce, any other person for the purpose of interfering with the right of such other person to vote or to vote as he may choose, or of causing such other person to vote for or not to vote for any candidate for the nomination of any party as its candidate' for various federal offices including representatives 'at any primary or nominating convention held solely or in part' for that purpose. This was stricken in the Senate. 84 Cong.Rec., pt. 4, 76th Cong., 1st Sess., p. 4191. That section would have extended the same protection to the primary and nominating convention as &#167; 1 of the Hatch Act<a class="footnote" href="#fn5-1" id="fn5-1_ref">5</a> extends to the general election. The Senate, however, refused to do so. Yet this Court now holds that &#167; 19 has protected the primary vote all along and that it covers conspiracies to do the precise thing on which Congress refused to legislate in 1939. The hesitation on the part of Congress through the years to enter the primary field, its refusal to do so<a class="footnote" href="#fn6-1" id="fn6-1_ref">6</a> in 1939, and the restricted scope of such primary laws as it has passed should be ample evidence that this Court is legislating when it takes the initiative in extending &#167; 19 to primaries.</p>
    </div>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">We should adhere to the strict construction given to &#167; 19 by a unanimous court in United States v. Bathgate, supra, 246 U.S. page 226, 38 S.Ct. page 271, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>, where it was said: 'Section 19, Criminal Code * * *, of course, now has the same meaning as when first enacted * * * and considering the policy of Congress not to interfere with elections within a state except by clear and specific provisions, together with the rule respecting construction of criminal statutes, we cannot think it was intended to apply to conspiracies to bribe voters.' That leads to the conclusion that &#167; 19 and the relevant constitutional provisions should be read so as to exclude all acts which do not have the direct effect of depriving voters of their right to vote at general elections. That view has received tacit recognition by Congress. For the history of legislation governing Federal elections shows that the occasional Acts of Congress<a class="footnote" href="#fn7-1" id="fn7-1_ref">7</a> on the subject have been primarily directed towards supplying detailed regulations designed to protect the individual's constitutional right to vote against pollution and corruption. Those laws, the latest of which is &#167; 1 of the Hatch Act, are ample recognition by Congress itself that specific legislation is necessary in order to protect the electoral process against the wide variety of acts which in their indirect or incidental effect interfere with the voter's freedom of choice and corrupt the electoral process. They are evidence that detailed regulations are essential in order to reach acts which do not directly interfere with the voting privilege. They are inconsistent with the notions in the opinion of the Court that the Constitution unaided by definite supplementary legislation protects the methods by which party candidates are nominated.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">That &#167; 19 lacks the requisite specificity necessary for inclusion of acts which interfere with the nomination of party candidates is reemphasized by the test here employed. The opinion of the Court stresses, as does the indictment, that the winner of the Democratic primary in Louisiana invariably carries the general election. It is also emphasized that a candidate defeated in the Louisiana primaries cannot be a candidate at the general election. Hence, it is argued that interference with the right to vote in such a primary is 'as a matter of law and in fact an interference with the effective choice of the voters at the only stage of the election procedure when their choice is of significance,' and that the 'primary in Louisiana is an integral part of the procedure for the popular choice' of representatives. By that means the Gradwell case is apparently distinguished. But I do not think it is a valid distinction for the purposes of this case.</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">One of the indictments in the Gradwell case charged that the defendants conspired to procure one thousand unqualified persons to vote in a West Virginia primary for the nomination of a United States Senator.  his Court, by a unanimous vote, affirmed the judgment which sustained a demurrer to that indictment. The Court specifically reserved the question as to whether a 'primary shall be treated as an election within the meaning of the Constitution'. But it went on to say that even assuming it were, certain 'strikingly unusual features' of the particular primary precluded such a holding in that case. It noted that candidates of certain parties were excluded from the primary and that even candidates who were defeated at the primary could on certain conditions be nominated for the general election. It therefore concluded that whatever power Congress might have to control such primaries, it had not done so by &#167; 19.</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p class="indent">If the Gradwell case is to survive, as I think it should, we have therefore this rather curious situation. Primaries in states where the winner invariably carries the general election are protected by &#167; 19 and the Constitution, even though such primaries are not by law an integral part of the election process. Primaries in states where the successful candidate never wins, seldom wins, or may not win in the general election are not so protected, unless perchance state law makes such primaries an integral part of the election process. Congress having a broad control over primaries might conceivably draw such distinctions in a penal code. But for us to draw them under &#167; 19 is quite another matter. For we must go outside the statute, examine local law and local customs, and then on the basis of the legal or practical importance of a particular primary interpret the vague language of &#167; 19 in the light of the significance of the acts done. The result is to make refined and nice distinctions which Congress certainly has not made, to create unevenness in the application of &#167; 19 among the various states, and to make the existence of a crime depend, not on the plain meaning of words employed interpreted in light of the legislative history of the statute, but on the result of research into local law or local practices. Unless Congress has explicitly made a crime dependent on such facts, we should not undertake to do so. Such procedure does not comport with the strict standards essential for the interpretation of a criminal law. The necessity of resorting to such a circuitous route is sufficient evidence to me that we are performing a legislative function in finding here a definition of a crime which will sustain this indictment. A crime, no matter how offensive, should not be spelled out from such vague inferences.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">Mr. Justice BLACK and Mr. Justice MURPHY join in this dissent.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> The ballots are printed at public expense, &#167; 35 of Act No. 46, Regular Session, 1940, are furnished by the Secretary of State, &#167; 36 in a form prescribed by statute, &#167; 37. Close supervision of the delivery of the ballots to the election commissioners is prescribed, &#167;&#167; 43&#8212;46. The polling places are required to be equipped to secure secrecy, &#167;&#167; 48&#8212;50; &#167;&#167; 54&#8212;57. The selection of election commissioners is prescribed, &#167; 61 and their duties detailed. The commissioners must swear to conduct the election impartially, &#167; 64 and are subject to punishment for deliberately falsifying the returns or destroying the lists and ballots, &#167;&#167; 98, 99. They must identify by certificate the ballot boxes used, &#167; 67, keep a triplicate list of voters, &#167; 68, publicly canvass the return, &#167; 74 and certify the same to the Secretary of State, &#167; 75.</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> For a discussion of the practical effect of the primary in controlling or restricting election of candidates at general elections, see, Hasbrouck, Party Government in the House of Representatives (1927) 172, 176, 177; Merriam and Overacker, Primary Elections (1928) 267&#8212;269; Stoney, Suffrage in the South; 29 Survey Graphic, 163, 164.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> Congress has recognized the effect of primaries on the free exercise of the right to choose the representatives, for it has inquired into frauds at primaries as well as at the general elections in judging the 'Elections, Returns, and Qualifications of its own Members', Art. I, &#167; 5. See Grace v. Whaley, H. Rept. No. 158, 63d Cong., 2d Sess.; Peddy v. Mayfield, S.Rept. No. 973, 68th Cong., 2d Sess.; Wilson v. Vare, S.Rept. No. 1858, 70th Cong., 2d Sess., S.Rept. No. 47, 71st Cong. 2d Sess., and S.Res. 111, 71st Cong., 2d Sess.</p>
        <p>See also Investigation of Campaign Expenditures in the 1940 Campaign, S.Rept. No. 47, 77th Cong., 1st Sess., p. 48 et seq.</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> Section 19 of the Criminal Code, U.S.C., Title 18, Sec. 51, <span class="citation no-link">18 U.S.C.A. &#167; 51</span>:</p>
        <p>'If two or more persons conspire to injure, oppress, threaten, or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States, or because of his having so exercised the same, or if two or more persons go in disguise on the highway, or on the premises of another, with intent to prevent or hinder his free exercise or enjoyment of any right or privilege so secured, they shall be fined n t more than $5,000 and imprisoned not more than ten years, and shall, moreover, be thereafter ineligible to any office, or place of honor, profit, or trust created by the Constitution or laws of the United States.' (R.S. &#167; 5508; Mar. 4, 1909, c. 321, &#167; 19, <span class="citation no-link">35 Stat. 1092</span>).</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> In United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#386" aria-description="Citation for case: United States v. Mosley">238 U.S. 383, 386</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#905" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904, 905</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>, the Court thought that 'Manifestly the words are broad enough to cover the case', it canvassed at length the objections that &#167; 19 was never intended to apply to crimes against the franchise, and the other contention, which it also rejected, that &#167; 19 had been repealed or so restricted as not to apply to offenses of that class. It is unnecessary to repeat that discussion here.</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> Section 1 now reads, <span class="citation no-link">8 U.S.C. &#167; 43</span>, <span class="citation no-link">8 U.S.C.A. &#167; 43</span>: 'Every person who, under color of any statute, ordinance, re ulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.'</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> See e.g. Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124; United States v. O'Toole, D.C., <span class="citation" data-id="8800997"><a href="/opinion/8816481/united-states-v-otoole/" aria-description="Citation for case: United States v. O&#x27;Toole">236 F. 993</a></span>, affirmed, United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>; Aczel v. United States, 7 Cir., <span class="citation" data-id="8799368"><a href="/opinion/8814892/aczel-v-united-states/" aria-description="Citation for case: Aczel v. United States">232 F. 652</a></span>; Felix v. United States, 5 Cir., <span class="citation" data-id="8778884"><a href="/opinion/8794848/felix-v-united-states/" aria-description="Citation for case: Felix v. United States">186 F. 685</a></span>; Karem v. United States, 6 Cir., <span class="citation" data-id="8750159"><a href="/opinion/8766689/karem-v-united-states/" aria-description="Citation for case: Karem v. United States">121 F. 250</a></span>, <span class="citation" data-id="8750159"><a href="/opinion/8766689/karem-v-united-states/" aria-description="Citation for case: Karem v. United States">61 L.R.A. 437</a></span>; Walker v. United States, 8 Cir., <span class="citation" data-id="1542868"><a href="/opinion/1542868/walker-v-united-states/" aria-description="Citation for case: Walker v. United States">93 F.2d 383</a></span>; Luteran v. United States, 8 Cir., <span class="citation" data-id="1542708"><a href="/opinion/1542708/luteran-v-united-states/" aria-description="Citation for case: Luteran v. United States">93 F.2d 395</a></span>.</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> No conclusion is to be drawn from the failure of the Hatch Act, <span class="citation no-link">53 Stat. 1147</span>, <span class="citation no-link">18 U.S.C. &#167; 61</span> et seq., <span class="citation no-link">18 U.S.C.A. &#167; 61</span> et seq., to enlarge &#167; 19 by provisions specifically applicable to primaries. Its failure to deal with the subject seems to be attributable to constitutional doubts, stimulated by Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>, which are here resolved. See 84 Cong.Rec., 76th Cong., 1st Sess., p. 4191; cf. Investigation of Campaign Expenditures in the 1940 Campaign, S.Rept. No. 47, 77th Cong., 1st Sess., p. 48.</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> Section 20 of the Criminal Code, U.S.C., Title 18, Sec. 52, <span class="citation no-link">18 U.S.C.A. &#167; 52</span>:</p>
        <p>'Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects, or causes to be subjected, any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be find not more than $1,000, or imprisoned not more than one year, or both.' (R.S. &#167; 5510; Mar. 4, 1909, c. 321, &#167; 20, <span class="citation no-link">35 Stat. 1092</span>).</p>
      </div>
      <div class="footnote" id="fn10">
        <a class="footnote" href="#fn10_ref">10</a>
        <p> The precursor of &#167; 20 was &#167; 2 of the Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, which reads:</p>
        <p>'That any person who, under color of any law, statute, ordinance, regulation, or custom, shall subject, or cause to be subjected, any inhabitant of any State or Territory to the deprivation of any right secured or protected by this act, or to different punishment, pains, or penalties on account of such person having at any time been held in a condition of slavery or involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, or by reason of his color or race, than is prescribed for the punishment of white persons, shall be deemed guilty of a misdemeanor, and, on conviction, shall be punished by fine * * *.'</p>
        <p>This section, so far as now material, was in substance the same as &#167; 20 except that the qualifying reference to differences in punishment made no mention of alienage, the reference being to 'different punishment * * * on account of such person having at any time been held in a condition of slavery or involuntary servitude'.</p>
        <p>Senator Trumbull, the putative author of S. 61, 39th Cong., 1st Sess., the Civil Rights Bill of 1866, and Chairman of the Senate Judiciary Committee which reported the bill, in explaining it stated that the bill was 'to protect all persons in the United States in their civil rights and furnishes the means of their vindication. * * *' Cong.Globe, 39th Cong., 1st Sess., p. 211. He also declared, 'The bill applies to white men as well as black men'. Cong.Globe, 39th Cong., 1st Sess., p. 599. Opponents of the bill agreed with this construction of the first clause of the section, declaring that it referred to the deprivation of constitutional rights of all inhabitants of the states of every race and color. Pp. 598, 601.</p>
        <p>On February 24, 1870, Senator Stewart of Nevada, introduced S. 365, 41st Cong., 2d Sess., &#167; 2 of which read:</p>
        <p>'That any person who under color of any law, statute, ordinance, regulation or custom shall subject, or cause to be subjected any inhabitant or any State or Territory to the deprivation of any rights secured or protected by this act, or to different punishment, pains, or penalties on account of such person being an alien, or by reason of his color or race, than is prescribed for the punishment of white persons, shall be deemed guilty of a misdemeanor. * * *'</p>
        <p>In explaining the bill he declared, Cong. Globe, 41st Cong., 2d Sess., p. 1536, that the purpose of the bill was to extend its benefits to aliens, saying, 'It extends the operation of the Civil Rights Bill, which is well known in the Senate and to the country, to all persons within the jurisdiction of the United States.' The Committee reported out a substitute bill to H.R. 1293, to which S. 365 was added as an amendment. As so amended the bill when adopted became the present &#167; 20 of the Criminal Code which read exactly as did &#167; 2 of the Civil Rights Act, except that the word 'aliens' was added and the word 'citizens' was substituted for the phrase 'white persons'.</p>
        <p>While the legislative history indicates that the immediate occasion for the adoption of &#167; 20, like the Fourteenth Amendment itself, was the more adequate 

[...TRUNCATED 5773 of 125773 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/United States v. Cole.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Cole
type: case
citation: "21 F.4th 421 (2021)"
parallel_cite: ""
neutral_cite: ""
court: 7th Cir.
court_level: coa
circuit: ca7
year: 2021
date_decided: 2021-12-17
docket: 20-2105
authority_weight: "Binding in-circuit — 7th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/5307612/united-states-v-janhoi-cole/"
  cluster_id: 5307612
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Cole
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Traffic Stops]]"
    role: Key
related:
  - "[[Traffic Stops]]"
  - "[[Rodriguez v. United States]]"
  - "[[Whren v. United States]]"
  - "[[Illinois v. Caballes]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - traffic-stop
  - reasonable-suspicion
  - rodriguez-mission
  - seventh-circuit
  - en-banc
holding: "Travel-plan questions ordinarily fall within the mission of a traffic stop and so do not, by themselves, measurably prolong it; like any inquiry during a stop, however, they must be reasonable under the circumstances — and here the trooper's follow-up questions were justified by the driver's evasive answers, and reasonable suspicion of drug trafficking developed before the stop was extended for a dog sniff, so suppression was properly denied."
aliases:
  - United States v. Cole
  - "United States v. Cole (7th Cir. 2021)"
---

# United States v. Cole

*21 F.4th 421 (7th Cir. 2021)* (No. 20-2105, [[Reading and Citing Cases#en-banc|en banc]]) · U.S. Court of Appeals for the Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 5307612 → majority opinion 5136163 (St. Eve, J., en banc; 21 F.4th 421, decided Dec. 17, 2021). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (the CL text carries only the slip-opinion pagination, not the 21 F.4th star pages) — S9 verifies the reporter pincite. -->

## Background
An Illinois state trooper stopped Janhoi Cole for following too closely on an interstate. Cole was driving with an Arizona license and a California registration on a recently purchased, recently insured car; the trooper's questions about his license, registration, and travel plans drew answers he found evasive, inconsistent, and improbable. Combined with other indicators, this led the trooper to suspect drug trafficking; he called a K-9 unit to a nearby gas station, the dog alerted, and officers found methamphetamine and heroin. A divided panel had reversed the denial of suppression, holding that the trooper's roadside travel-plan questioning unreasonably prolonged the stop; the Seventh Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether travel-plan questions are part of the "mission" of a traffic stop under *[[Rodriguez v. United States]]*, such that asking them does not unlawfully prolong the stop.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, a stop may last no longer than needed to complete its mission, and off-mission inquiries that add time require independent reasonable suspicion. Resolving an intra-circuit conflict, the [[Reading and Citing Cases#en-banc|en banc]] court held: "we hold that travel-plan questions ordinarily fall within the mission of a traffic stop. Travel-plan questions, however, like other police inquiries during a traffic stop, must be reasonable under the circumstances." — slip op. at 2. ^pin-slip2

## Application
Because travel-plan questions ordinarily belong to the stop's mission, the trooper's initial inquiries did not prolong the detention at all. His follow-up questions were reasonable responses to Cole's "less-than-forthright answers," and by the time the stop moved to the gas station for the dog sniff, the trooper had developed reasonable suspicion of drug trafficking to support the brief extension. The stop was lawfully initiated and never unreasonably prolonged.

## Conclusion
**Affirmed.** The [[Reading and Citing Cases#en-banc|en banc]] court affirmed the denial of Cole's motion to suppress. Judge St. Eve wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Cole* is a leading [[Reading and Citing Cases#en-banc|en banc]] statement placing routine travel-plan questioning inside the *[[Rodriguez v. United States|Rodriguez]]* mission, consistent with *[[Illinois v. Caballes|Caballes]]* on dog sniffs that do not add time — while cautioning that such questions must still be reasonable in the circumstances.

## Appears on
- [[Traffic Stops]] — *Key*

## Sources
- [*United States v. Cole*, 21 F.4th 421 (7th Cir. 2021)](https://www.courtlistener.com/opinion/5307612/united-states-v-janhoi-cole/) — pinpoint: slip op. at 2 (travel-plan questions within the stop's mission). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is slip-paginated, so the 21 F.4th star page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a830817d0b78c47b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Cole"}, "payload": {"all": [{"cite": "21 F.4th 421", "page": "421", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "21"}], "display": "21 F.4th 421", "official": {"cite": "21 F.4th 421", "page": "421", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "21"}, "official_selection_present": true, "record_id": "United States v. Cole"}}
{"assertion_id": "10bae1835390a257", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Cole"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Cole", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Cole

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cole",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Janhoi Cole",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Cole",
    "court": "7th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca7",
    "state": null,
    "date_decided": "2021-12-17",
    "year": 2021,
    "docket": "20-2105",
    "cluster_id": 5307612,
    "lead_opinion_id": 5136163,
    "sibling_ids": [],
    "absolute_url": "/opinion/5307612/united-states-v-janhoi-cole/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "21 F.4th 421",
      "volume": "21",
      "reporter": "F.4th",
      "page": "421",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "21 F.4th 421",
        "volume": "21",
        "reporter": "F.4th",
        "page": "421",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "21 F.4th 421",
    "official_selection": {
      "court_class": "coa",
      "selected": "21 F.4th 421",
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
    "date_created": "2026-07-07T18:18:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-cole--5307612",
      "to_record_id": "United States v. Cole",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Cole

```
                                 In the

     United States Court of Appeals
                      For the Seventh Circuit
                        ____________________
No. 20-2105
UNITED STATES OF AMERICA,
                                                     Plaintiﬀ-Appellee,
                                   v.

JANHOI COLE,
                                                 Defendant-Appellant.
                        ____________________

          Appeal from the United States District Court for the
                      Central District of Illinois.
              No. 3:18-cr-30038 — Richard Mills, Judge.
                        ____________________

 ARGUED SEPTEMBER 30, 2021 — DECIDED DECEMBER 17, 2021
                ____________________

   Before SYKES, Chief Judge, and EASTERBROOK, KANNE,
ROVNER, WOOD, HAMILTON, BRENNAN, SCUDDER, ST. EVE, and
KIRSCH, Circuit Judges. *




    * Circuit Judge  Jackson-Akiwumi did not participate in the considera-
tion or decision of this case.
2                                                  No. 20-2105

    ST. EVE, Circuit Judge. An Illinois state trooper stopped
Janhoi Cole for following too closely behind another car. At
the time, Cole was traveling on an Illinois interstate with an
Arizona driver’s license and a California registration. During
the brief roadside detention that followed, the trooper ques-
tioned Cole about his license, registration, and travel plans.
Cole’s answers struck the trooper as evasive, inconsistent, and
improbable. Many of the trooper’s questions were follow-up
questions to Cole’s answers and volunteered information.
Combined with other factors, they led the trooper to suspect
that Cole was traﬃcking drugs. To investigate his suspicions,
the trooper called for a K-9 unit to meet him and Cole at a
nearby gas station. The dog alerted, and oﬃcers found large
quantities of methamphetamine and heroin in Cole’s car.
    Facing federal charges, Cole moved to suppress the drugs
as well as his statements during the stop. He argued that the
trooper unlawfully initiated the stop and unreasonably pro-
longed it without reasonable suspicion of other criminal ac-
tivity. The district court denied the motion, but a divided
panel of this Court reversed on the basis that the trooper’s in-
itial roadside questioning unreasonably prolonged the traﬃc
stop. We reheard the case en banc to resolve an apparent con-
ﬂict between the panel’s decision and United States v. Lewis,
920 F.3d 483 (7th Cir. 2019), as to whether travel-plan ques-
tions are part of the “mission” of a traﬃc stop under Rodriguez
v. United States, 575 U.S. 348 (2015).
   In keeping with Lewis and the consensus of other circuits,
we hold that travel-plan questions ordinarily fall within the
mission of a traﬃc stop. Travel-plan questions, however, like
other police inquiries during a traﬃc stop, must be reasonable
under the circumstances. And here they were. The trooper
No. 20-2105                                                    3

inquired about the basic details of Cole’s travel, and his fol-
low-up questions were justiﬁed given Cole’s less-than-forth-
right answers. The stop itself was lawfully initiated, and the
trooper developed reasonable suspicion of other criminal ac-
tivity before moving the initial stop to the gas station for the
dog sniﬀ. We therefore aﬃrm the district court’s denial of
Cole’s motion to suppress.
                               I.
    A magistrate judge held a hearing on Cole’s motion to
suppress. Evidence at the hearing included the trooper’s po-
lice report and dash camera video as well as testimony from
Cole, the trooper, and another oﬃcer involved in the stop. Af-
ter the hearing, the magistrate judge entered a report and rec-
ommendation with extensive factual ﬁndings, which the dis-
trict court adopted. Absent clear error, we defer to the district
court’s factual ﬁndings. United States v. Bacon, 991 F.3d 835,
840 (7th Cir. 2021).
                               A.
    Sheriﬀ’s Deputy Derek Suttles was on criminal interdic-
tion patrol in central Illinois when he spotted a silver
Volkswagen hatchback traveling east on the interstate. The
car caught his attention because it was travelling 10 to 15 miles
below the posted speed limit. Deputy Suttles also noticed a
covering over the car’s rear cargo area. He messaged Illinois
State Police Trooper Clayton Chapman, who was doing crim-
inal interdiction patrol further east on the interstate, and told
him to look out for the Volkswagen. Trooper Chapman had
about 250 hours of training, mostly related to drug interdic-
tion and other crime interdiction on roadways.
4                                                 No. 20-2105

   Deputy Suttles relayed the information that he considered
to be suspicious, along with the results of a license plate
check. The check revealed that the Volkswagen had been sold
and registered three weeks earlier to Janhoi Cole, with an ad-
dress in Los Angeles, California. It had been insured only four
days earlier.
    Trooper Chapman spotted the Volkswagen, whose driver
was leaned far back in the seat with his arms fully extended,
obscuring his face, and began following the vehicle. Shortly
thereafter, Trooper Chapman saw another car merge in front
of the Volkswagen from the far-left lane. When the other car
merged, the Volkswagen did not move into the right lane, but
instead followed closely behind the merged car. From his van-
tage point—about a football ﬁeld behind the Volkswagen—
Trooper Chapman determined that the Volkswagen was two
car lengths or less behind the merged car.
   Trooper Chapman stopped the Volkswagen for following
too closely, in violation of Illinois law. See 625 ILCS 5/11-
710(a). After calling in the license plate and conﬁrming that
the plate matched the car, Trooper Chapman approached the
Volkswagen and asked the driver (Cole) for his license and
registration. Cole produced his Arizona driver’s license and
California registration. In response to Trooper Chapman’s
questions, Cole conﬁrmed that his license showed his current
address and that he owned the Volkswagen. Trooper Chap-
man then asked Cole to sit in his squad car so he could explain
the purpose of the stop in a quieter and safer setting. While
standing by Cole’s car, Trooper Chapman saw numerous
drinks and snacks in the car, which led him to believe that
Cole had been traveling long distances. He observed, though,
that the only luggage in the car was a small backpack.
No. 20-2105                                                  5

   In the squad car, Trooper Chapman spent about a minute
explaining the details of how Cole had followed the other car
too closely. He then asked Cole about his Arizona driver’s li-
cense and California license plate. Cole oﬀered, “I’m a chef. I
spend most of my time between Los Angeles and Maryland
and New York at work. But I genuinely had a job in Arizona.
And I genuinely keep this driver’s license because of the ex-
piration date.”
    About four minutes into the stop, Trooper Chapman be-
gan inquiring into Cole’s travel plans. He ﬁrst asked where
Cole was headed. Cole answered, Maryland, because his boss
resided in Maryland. Following up, the trooper asked where
Cole worked and for whom. Cole responded that he was a
personal chef for two former professional football players
and, in between, an ordinary chef. After conﬁrming Cole’s
destination (Maryland), the trooper asked Cole where his trip
began. Cole did not answer the question initially. Instead, he
oﬀered that he had met up with some friends and family in
Colorado Springs. The trooper asked again where the trip be-
gan. Cole clariﬁed that his trip started in Maryland. From
there, he went to Cincinnati, before heading to Colorado
Springs, then Boulder, and was going back home to Maryland
when the trooper stopped him. The trooper asked Cole when
he left on the trip. Cole said about four to ﬁve days earlier.
    The trooper then moved on to the vehicle’s information.
He questioned Cole as to how long he had owned the
Volkswagen. Cole said six months, adding that he just had the
paperwork transferred. He explained that the car was a recent
purchase. He had been driving with his friend’s paperwork
and had only recently acquired the insurance and registra-
tion. Looking at Cole’s paperwork, the trooper noted that the
6                                                    No. 20-2105

car had been registered on June 4, 2018. Cole veriﬁed that was
correct; his girlfriend had registered the car then.
    Trooper Chapman next inquired where Cole was living.
Cole said he spent most of his time in Los Angeles, adding
that he had a child in both Los Angeles and Florida and was
planning to move to Florida. The trooper wondered, “So,
you’ve got an Arizona driver’s license that says Tucson … I’m
just trying to … And you said you’ve been traveling from
Maryland, so have you been staying recently in Maryland?”
Cole replied, “Yes. I have family in Maryland. My boss is in
Maryland. When I work in Maryland, I stay by my uncle. But
this driver’s license, I genuinely keep it just because of the ex-
piration. I haven’t been in Arizona in a long time.” The
trooper followed up, “So your primary address, or your cur-
rent address, is in California. But recently you’ve been staying
in ….” Before he could ﬁnish, Cole interjected, “Yeah, cause
I’m a chef. I travel.” The trooper asked, “Back and forth?”
Cole said yes, explaining that he went wherever he got jobs.
The trooper concluded by asking Cole why he did not ﬂy.
Cole responded, “Fly? I have a car. And I travel with pots
sometimes. I’m a chef. Occasionally I travel with a bicycle.”
   Trooper Chapman thought that Cole’s travel details
sounded vague and made up. Cole appeared extremely nerv-
ous during the stop. Among other physical symptoms, he was
breathing heavily, and his neck was sweaty.
    Less than nine minutes into the stop, Trooper Chapman
told Cole that he was going to issue him a warning. He ex-
plained, though, that they would have to relocate to a nearby
gas station for safety reasons. Cole returned to his own car,
and they drove separately to the gas station. At the gas station,
Trooper Chapman called for a K-9 unit. While waiting,
No. 20-2105                                                    7

Trooper Chapman continued questioning Cole about his
travel plans. He regarded Cole’s answers as increasingly sus-
picious. He also learned from dispatch that Cole had been ar-
rested three times on drug traﬃcking charges. About 45
minutes after the stop began, the K-9 unit alerted on Cole’s
car. Oﬃcers searched the car and found large quantities of
methamphetamine and heroin.
                               B.
    A federal grand jury charged Cole with possession with
intent to distribute 500 grams or more of methamphetamine
(Count 1) and heroin (Count 2). Cole moved to suppress the
drugs found in his car and his statements during the stop. The
magistrate judge recommended denying the motion. The dis-
trict court accepted the recommendation and denied the mo-
tion. Cole conditionally pleaded guilty to both counts, while
reserving his right to appeal the denial of his motion to sup-
press. A divided panel of this Court reversed, but we vacated
that opinion and voted to rehear the case en banc.
                               II.
    Cole maintains that Trooper Chapman violated his Fourth
Amendment rights by stopping him without reasonable sus-
picion of a traﬃc violation and by unreasonably prolonging
the stop to inquire into his travel plans. We review the district
court’s legal conclusions de novo, Bacon, 991 F.3d at 840, and
its factual ﬁndings for clear error, United States v. Gholston,
1 F.4th 492, 496 (7th Cir. 2021).
    The Fourth Amendment provides that “[t]he right of the
people to be secure in their persons, houses, papers, and ef-
fects, against unreasonable searches and seizures, shall not be
violated.” U.S. Const. amend. IV. Time and again, the
8                                                        No. 20-2105

Supreme Court has held that “the ultimate touchstone of the
Fourth Amendment is reasonableness.” Lange v. California,
141 S. Ct. 2011, 2017 (2021) (quoting Brigham City v. Stuart, 547
U.S. 398, 403 (2006)). “Reasonableness, in turn, is measured in
objective terms by examining the totality of the circum-
stances.” Ohio v. Robinette, 519 U.S. 33, 39 (1996).
    Traﬃc stops are seizures, so they must be reasonable un-
der the circumstances. Whren v. United States, 517 U.S. 806, 809
(1996). To be reasonable, a traﬃc stop must be “justiﬁed at its
inception, and reasonably related in scope to the circum-
stances which justiﬁed the interference in the ﬁrst place.”
Hiibel v. Sixth Jud. Dist. Ct. of Nevada, Humboldt Cnty., 542 U.S.
177, 185 (2004). Because traﬃc stops are typically brief deten-
tions, more akin to Terry stops than formal arrests, they re-
quire only reasonable suspicion of a traﬃc violation—not
probable cause. Rodriguez, 575 U.S. at 354; Navarette v. Califor-
nia, 572 U.S. 393, 396–97 (2014); see also Terry v. Ohio, 392 U.S.
1 (1968). By the same token, though, traﬃc stops must remain
limited in scope: “A seizure for a traﬃc violation justiﬁes a
police investigation of that violation.” Rodriguez, 575 U.S. at
354. Police may not “detour[]” from that “mission” to investi-
gate other criminal activity. Id. at 356–57. A detour that “pro-
longs the stop” violates the Fourth Amendment unless the of-
ﬁcer has reasonable suspicion of other criminal activity to in-
dependently justify prolonging the stop. Id. at 355.
                                  A.
   The ﬁrst issue we address is whether Trooper Chapman
had a lawful basis to initiate the stop.1 We have little trouble


    1 We, of course, do not consider Trooper Chapman’s subjective moti-
vations for deciding to conduct a traﬃc stop. As the Supreme Court has
No. 20-2105                                                               9

concluding that he did. Under Illinois law, “[t]he driver of a
motor vehicle shall not follow another vehicle more closely
than is reasonable and prudent, having due regard for the
speed of such vehicles and the traﬃc upon and the condition
of the highway.” 625 ILCS 5/11-710(a). Trooper Chapman tes-
tiﬁed that Cole was less than two car lengths behind the car in
front of him. The magistrate judge credited that testimony
and made an express factual ﬁnding that Cole was following
too closely behind the other car. Cole does not challenge that
factual ﬁnding on appeal. Instead, he argues that the district
court failed to consider the statutory factors (speed of other
cars, traﬃc, and road conditions) when determining that
there was reasonable suspicion of a traﬃc violation. The ques-
tion, however, is whether Trooper Chapman reasonably be-
lieved that he saw a traﬃc violation, not whether Cole actu-
ally violated the statute. United States v. Muriel, 418 F.3d 720,
724 (7th Cir. 2005); see also United States v. Simon, 937 F.3d 820,
829 (7th Cir. 2019) (“If an oﬃcer reasonably thinks he sees a
driver commit a traﬃc infraction, that is a suﬃcient basis to
pull him over without violating the Constitution.”). As in
Muriel, the trooper’s “estimation” of a short following dis-
tance justiﬁed the stop. Muriel, 418 F.3d at 724; accord Lewis,
920 F.3d at 490.




unequivocally held, “[s]ubjective intentions play no role in ordinary,
probable-cause Fourth Amendment analysis.” Whren, 517 U.S. at 813. To
the extent that the dissent opposes the objective test established by Whren,
or suggests that police discretion informs how courts should approach
Fourth Amendment law more generally, that is an issue for the Supreme
Court, not us.
10                                                   No. 20-2105

                               B.
   The more substantial issue is whether Trooper Chapman
unlawfully prolonged the traﬃc stop by inquiring about
Cole’s itinerary.
                                1.
    To answer this question, we start with Rodriguez. There,
the Supreme Court held that “the tolerable duration of police
inquiries in the traﬃc-stop context is determined by the sei-
zure’s ‘mission.’” Rodriguez, 575 U.S. at 354 (quoting Illinois v.
Caballes, 543 U.S. 405, 407 (2005)). The mission of a traﬃc stop,
in turn, is “to address the traﬃc violation that warranted the
stop and attend to related safety concerns.” Id. (citations omit-
ted). Tasks within that mission include “determining whether
to issue a traﬃc ticket” and pursuing “‘ordinary inquiries in-
cident to [the traﬃc] stop.’” Id. at 355 (quoting Caballes, 543
U.S. at 408). Typically, the ordinary inquiries incident to a
traﬃc stop “involve checking the driver’s license, determin-
ing whether there are outstanding warrants against the
driver, and inspecting the automobile’s registration and proof
of insurance.” Id. Such inquiries fall within the mission of a
stop because they “serve the same objective as enforcement of
the traﬃc code: ensuring that vehicles on the road are oper-
ated safely and responsibly.” Id. Rodriguez distinguished
those ordinary inquiries from measures aimed at investigat-
ing other criminal activity, such as a dog sniﬀ for drugs. Id.
   As part of making these ordinary inquiries, no one dis-
putes that an oﬃcer may ask questions unrelated to the stop,
and even conduct a dog sniﬀ, if doing so does not prolong the
traﬃc stop. As the Supreme Court explained in Arizona v.
Johnson, 555 U.S. 323 (2009), “[a]n oﬃcer’s inquiries into
No. 20-2105                                                     11

matters unrelated to the justiﬁcation for the traﬃc stop … do
not convert the encounter into something other than a lawful
seizure, so long as those inquiries do not measurably extend
the duration of the stop.” Id. at 333; see Rodriguez, 575 U.S. at
354–55; Caballes, 543 U.S. at 408 (dog sniﬀ). This recognition
does not resolve this appeal because the record is undevel-
oped as to whether Trooper Chapman’s travel-plan questions
prolonged the stop. If they did not, then they would have
been permissible even if they exceeded the mission of the
stop. See Lewis, 920 F.3d at 492; United States v. Walton, 827 F.3d
682, 687 (7th Cir. 2016). But because the district court never
made such a factual ﬁnding, we put this issue aside and ask
whether Trooper Chapman’s travel-plan questions fell within
the mission of the stop, such that they could not have pro-
longed it in the ﬁrst place.
    Rodriguez did not list travel-plan questions among the or-
dinary inquiries of a traﬃc stop. See Rodriguez, 575 U.S. at 351.
From this, Cole infers that the Supreme Court must have
meant to exclude them. Judicial opinions are not statutes,
however, and we decline to extrapolate a holding about
travel-plan questions from the Supreme Court’s silence on
them in a case where they were not at issue. See United States
v. Skoien, 614 F.3d 638, 640 (7th Cir. 2010) (en banc). The ques-
tion presented in Rodriguez was “whether the Fourth Amend-
ment tolerates a dog sniﬀ conducted after completion of a
traﬃc stop.” Rodriguez, 575 U.S. at 350. The Court had no oc-
casion to reach—and did not reach—the propriety and per-
missible scope of travel-plan questions. We decline to read Ro-
driguez as creating an exhaustive list of mission-related in-
quiries. See United States v. Gholston, 1 F.4th 492, 496 (7th Cir.
2021) (noting that “[a] stop may call for a variety of measures
beyond” the ordinary inquiries listed in Rodriguez).
12                                                    No. 20-2105

    Though Rodriguez did not address whether travel-plan
questions fall within the mission of a traﬃc stop, it supplied
an analytical framework for answering that question.
Namely, we must ask whether, in the totality of circum-
stances, reasonable travel-plan questions, like the other ordi-
nary inquiries of a stop, are justiﬁed by the traﬃc violation
itself or by the “related” concerns of “[h]ighway and oﬃcer
safety.” Rodriguez, 575 U.S. at 354, 356–57. Our sister circuits
have followed this approach in deciding whether other un-
listed inquiries fall within the mission of a traﬃc stop. See, e.g.,
United States v. Buzzard, 1 F.4th 198, 203–04 (4th Cir. 2021);
United States v. Clark, 902 F.3d 404, 410–11 (3d Cir. 2018);
United States v. Evans, 786 F.3d 779, 786–87 (9th Cir. 2015).
    Applying the Rodriguez framework, we hold that travel-
plan questions ordinarily fall within the mission of a traﬃc
stop. To begin, travel-plan questions supply important con-
text for the violation at hand. If, for example, “a given driver
was speeding in order to get his pregnant wife to the hospi-
tal,” then perhaps this “extenuating circumstance” might per-
suade the oﬃcer to issue a warning or simply release the
driver. United States v. Brigham, 382 F.3d 500, 508 & n.6 (5th
Cir. 2004) (en banc); accord United States v. Cortez, 965 F.3d 827,
839 (10th Cir. 2020) (reasoning that oﬃcer’s travel-plan ques-
tions “could cast light on why Cortez had been speeding, ty-
ing them to the initial justiﬁcation for the stop”). In other cir-
cumstances, the context of a stop might counsel in favor of a
ticket or arrest. See Brigham, 382 F.3d at 508 & n.6.
    A driver’s travel plans may also inform an oﬃcer’s assess-
ment of roadway safety concerns beyond the immediate vio-
lation. An oﬃcer investigating a broken taillight, for example,
has a legitimate interest in knowing whether the driver is two
No. 20-2105                                                      13

miles from home or halfway through a cross-country trip. Cf.
United States v. Ellis, 497 F.3d 606, 613–14 (6th Cir. 2007) (hold-
ing that oﬃcer who stopped car for weaving “was justiﬁed in
asking the occupants general questions of who, what, where,
and why regarding their 3:23 a.m. travel,” as such questions
could help “determine the driver’s ability to safely operate the
vehicle”).
    At a more general level, “[t]ravel plans typically are re-
lated to the purpose of a traﬃc stop because the motorist is
traveling at the time of the stop.” United States v. Holt, 264 F.3d
1215, 1221 (10th Cir. 2001) (en banc), abrogated on other grounds
as recognized in Cortez, 965 F.3d at 839; see also United States v.
Collazo, 818 F.3d 247, 258 (6th Cir. 2016) (describing travel-
plan questions as “classic context-framing questions directed
at the driver’s conduct at the time of the stop” (quoting United
States v. Lyons, 687 F.3d 754, 770 (6th Cir. 2012))). In that sense,
travel-plan questions comport with the “public’s expectations
regarding ordinary inquiries incidental to traﬃc stops.” Cor-
tez, 965 F.3d at 839.
    In short, travel-plan questions are routine inquiries that
reasonably relate to the underlying traﬃc violation and road-
way safety. As a result, we hold that such questions ordinarily
fall within the mission of a traﬃc stop. This does not mean,
however, that oﬃcers have a free pass to ask travel-plan ques-
tions until they are subjectively satisﬁed with the answers. An
oﬃcer’s travel-plan questions, like the oﬃcer’s other actions
during the stop, must remain reasonable, and reasonableness
is an objective standard based on all the circumstances. Robi-
nette, 519 U.S. at 39.
   We are not alone in holding that travel-plan questions or-
dinarily fall within the mission of a traﬃc stop. In fact, every
14                                                    No. 20-2105

circuit to address the issue post-Rodriguez has reached the
same conclusion. Most recently, the Eleventh Circuit rejected
a defendant’s argument that an oﬃcer’s travel-plan questions
went beyond the mission of a stop, holding that “[g]enerally,
questions related to an individual’s traﬃc plans or itinerary
are ordinary inquires related to a traﬃc stop.” United States v.
Braddy, 11 F.4th 1298, 1311 (11th Cir. 2021). Five other circuits
agree. Cortez, 965 F.3d at 838 (“An oﬃcer may … inquire about
the driver’s travel plans.”); United States v. Garner, 961 F.3d
264, 271 (3d Cir. 2020) (“[S]ome questions relating to a driver’s
travel plans ordinarily fall within the scope of the traﬃc
stop.”); United States v. Smith, 952 F.3d 642, 647 (5th Cir. 2020)
(observing that an oﬃcer “may … ask about the purpose and
itinerary of the occupants’ trip” (quoting Brigham, 382 F.3d at
508)); United States v. Dion, 859 F.3d 114, 125 (1st Cir. 2017)
(“[O]ur case law allows an oﬃcer carrying out a routine traﬃc
stop to … inquire into the driver’s itinerary.”); Collazo, 818
F.3d at 258 (“Questions relating to travel plans … rarely of-
fend our Fourth Amendment jurisprudence.” (quoting Lyons,
687 F.3d at 770)); see also United States v. Callison, 2 F.4th 1128,
1131 n.2 (8th Cir. 2021) (noting that “[i]n some post-Rodriguez
cases we have at least suggested that travel-related questions
remain a ‘permissible’ part of routine traﬃc stops in the
Eighth Circuit.” (citing United States v. Murillo-Salgado, 854
F.3d 407, 415 (8th Cir. 2017))).
    The dissent claims that the Tenth Circuit has taken a more
nuanced approach to travel-related questions in United States
v. Gomez-Arzate. 981 F.3d 832 (10th Cir. 2020). In Gomez-Arzate,
however, the oﬃcers’ travel-plan questions came after the traf-
ﬁc stop was completed, in contrast to the questions from
Trooper Chapman that occurred during the traﬃc stop. Id. at
840 n.3 (“Here, though, the traﬃc stop had eﬀectively been
No. 20-2105                                                            15

completed before the VIN search and questioning about
travel plans.”).
    We, too, have approved of travel-plan questions post-Ro-
driguez. In Lewis, the defendant complained that an oﬃcer
spent several minutes “asking about irrelevant travel matters”
during a traﬃc stop, thereby prolonging the stop in violation
of the rule announced in Rodriguez. 920 F.3d at 492. We re-
jected the argument. To begin, we dismissed the idea that the
oﬃcer’s ﬁrst question—“Where are we headed to today,
sir?”—was unrelated to the stop, remarking that “[o]ﬃcers
across the country would be surprised if we countenanced the
characterization of this basic, routine question as irrelevant to
a traﬃc stop.” Id. Lewis’s response to the oﬃcer’s ﬁrst ques-
tion was “not entirely forthcoming,” and prompted the oﬃcer
to ask several follow-up questions. Lewis answered these
questions in a similarly evasive manner. Again, adhering to
the rule announced in Rodriguez, we squarely rejected Lewis’s
argument that the oﬃcer’s travel-plan questions were imper-
missible: “The Constitution allows an oﬃcer to ask these
questions during a traﬃc stop, especially when the answers
objectively seem suspicious.” 2 Id.
    Lewis reinforces an important corollary of our holding: Of-
ﬁcers asking travel-plan questions may also ask reasonable
follow-up questions based on a driver’s responses. Travel-
plan questions are not mere formalities; they serve important


    2 The dissent attempts to recast Lewis, asserting that “the most im-
portant reason [we] had for aﬃrming denial of the motion to suppress
there was that the defendant had simply failed as a matter of fact to show
that the questioning had actually prolonged the stop.” But that reading
contradicts the opinion’s unambiguous language. Lewis, 920 F.3d at 492.
16                                                 No. 20-2105

law-enforcement purposes, and therefore an oﬃcer has an in-
terest not only in asking such questions but also in receiving
truthful answers to them. If a driver’s responses are evasive,
inconsistent, or improbable, the oﬃcer need not accept them
at face value and move on. To the contrary, the oﬃcer may
ask reasonable follow-up questions to clarify the answers.
This was our point in Lewis, when we said the Fourth Amend-
ment permits travel-plan questions during traﬃc stops “espe-
cially when the answers objectively seem suspicious.” Id.; see
also Murillo-Salgado, 854 F.3d at 415 (holding that an oﬃcer
may take the time to respond to “legitimate complications”
that arise during the “routine tasks” of a traﬃc stop); Dion,
859 F.3d at 124–25 (explaining that a Terry stop is not a “snap-
shot of events frozen in time and place” and that an oﬃcer’s
“actions must be fairly responsive to the emerging tableau”
(internal quotation and citation omitted)). It is only when an
oﬃcer’s follow-up questions go too far and become unreason-
able that a stop risks becoming prolonged.
                               2.
   Applying these principles here, we hold that Trooper
Chapman’s travel-plan questions during the initial roadside
detention fell within the mission of the traﬃc stop and did not
unlawfully prolong the traﬃc stop.
    At the outset, it is important to recall the sequence of
events here. Trooper Chapman asked his travel-plan ques-
tions following Cole’s elusive and confusing account. These
travel-plan questions related closely to his questions about
Cole’s Arizona license and California registration. See Braddy,
11 F.4th at 1311 (holding that the oﬃcer’s questions about li-
cense, registration, and travel plans were within the mission
of stop). Before inquiring into Cole’s travel, Trooper
No. 20-2105                                                    17

Chapman asked Cole about the discrepancy between his Ari-
zona license and California registration. Cole’s response ref-
erenced three other states beyond Arizona and California. He
explained that he was a chef who split his time between Los
Angeles, Maryland, and New York, adding that he kept his
Arizona license because of the expiration date and that he
might be moving to Florida soon. When Trooper Chapman
began generally inquiring about Cole’s travel details, Cole
added two more states into the mix: He said he had stopped
in Cincinnati on his way from Maryland to Colorado. By this
point, Cole had mentioned seven diﬀerent states—none of
which was Illinois—in response to Trooper Chapman’s ques-
tions about his license, registration, and basic trip details. See
id. (holding that the oﬃcer’s travel-plan questions were “or-
dinary inquiries related to the traﬃc stop, especially given the
fact that Braddy was driving a vehicle on Alabama roads with
an obstructed Florida license plate that was not registered to
him”).
    Understandably, Trooper Chapman had follow-up ques-
tions. Cole evaded some of these follow-up questions. After
Cole volunteered that he worked as a chef, for example,
Trooper Chapman asked where he worked. Cole replied with
his occupation, saying he was a personal chef. Trooper Chap-
man tried asking the same question another way: “Who do
you work for?” This time, Cole responded that he worked for
two former professional football players and that “in be-
tween” he was a chef. Cole similarly evaded Trooper Chap-
man’s question about where he began his trip, prompting
Trooper Chapman to repeat the question. Cole’s explanation
for where he was currently living was also hard to pin down.
Initially, he said he spent most of his time in Los Angeles,
while noting that he might be moving to Florida. When
18                                                    No. 20-2105

Trooper Chapman followed up, however, Cole seemed to
agree that he was currently living in Maryland. In addition to
evading questions, Cole gave confusing and improbable an-
swers that prompted other reasonable follow-up questions.
See Dion, 859 F.3d at 125–26 (where driver with Colorado
plates produced an Arizona license and “described his travel
itinerary as a return trip from a cross-country road trip to visit
a CPA in Pennsylvania,” an oﬃcer’s follow-up questions on
the same subject were “both prompted and warranted” by
that “odd answer to a concededly appropriate question about
travel itinerary”).
    Under these circumstances, Trooper Chapman’s travel-
plan questions were reasonable. Trooper Chapman ques-
tioned Cole about the basic details of his travel—which were
relevant to the traﬃc violation and roadway safety—and
asked reasonable follow-up questions based on Cole’s elusive
answers. See Lewis, 920 F.3d at 492. As Trooper Chapman tes-
tiﬁed, his questions were aimed at “piec[ing] together” Cole’s
“inconsistent” answers to basic travel-plan questions. He was
not, as Cole suggests, conducting a “ﬁshing expedition” for
information that might generate reasonable suspicion to pro-
long the stop. Dion, 859 F.3d at 128 n.12 (citing United States v.
Pruitt, 174 F.3d 1215, 1221 (11th Cir. 1999)); cf. Cortez, 965 F.3d
at 840 (holding that “repetitive” and “in depth” questions
about travel details were unrelated to traﬃc stop because
such questions “neither helped investigate the original infrac-
tion—speeding—nor could they reasonably be characterized
as relating to oﬃcer safety”); United States v. Macias, 658 F.3d
509, 519 (5th Cir. 2011) (holding that oﬃcer’s detailed ques-
tions about driver’s mother, children, and past encounters
with law enforcement went beyond mission of stop because
they bore no relation to driver’s failure to wear a seatbelt).
No. 20-2105                                                   19

    Cole complains that Trooper Chapman’s questions went
beyond the details of his travel and into unrelated matters,
such as his occupation. But Cole initially volunteered his oc-
cupation almost three minutes into the stop in response to a
question about his license and registration and repeatedly re-
turned to it when explaining his travel and living situation, so
it was reasonable for Trooper Chapman to ask a few follow-
up questions about it. Cole also complains about the length of
Trooper Chapman’s travel-plan questions (just under ﬁve
minutes). But “we repeatedly have declined to adopt even a
rule of thumb that relies on the number of minutes any given
stop lasts.” Gholston, 1 F.4th at 496 n.4. Reasonableness is the
touchstone, and what is reasonable depends on the circum-
stances of a case. Lange, 141 S. Ct. at 2017. Here, Trooper Chap-
man’s questioning stayed within reasonable limits given
Cole’s responses.
   Because Trooper Chapman’s questioning was reasonable,
we need not speculate about scenarios in which travel-plan
questions might go too far. For now, it is enough to say that
travel-plan questions go too far when they are no longer rea-
sonably related to the stop itself (and related safety concerns)
but rather reﬂect an independent investigation of other crim-
inal activity. See Rodriguez, 575 U.S. at 356–57.
                               3.
    We do not address whether Trooper Chapman’s addi-
tional questions at the gas station stayed within the mission
of the stop because he developed reasonable suspicion of
other criminal activity less than nine minutes into the stop,
before he told Cole he would issue him a warning and before
they drove to the gas station.
20                                                  No. 20-2105

    Reasonable suspicion exists when, considering the totality
of the circumstances, an oﬃcer has “a particularized and ob-
jective basis for suspecting the particular person stopped of
criminal activity.” Navarette, 572 U.S. at 396–97 (quoting
United States v. Cortez, 449 U.S. 411, 417–18 (1981)). A hunch is
not enough, but “the likelihood of criminal activity need not
rise to the level required for probable cause, and it falls con-
siderably short of satisfying a preponderance of the evidence
standard.” United States v. Arvizu, 534 U.S. 266, 274 (2002). The
standard “allows oﬃcers to draw on their own experience
and specialized training to make inferences from and deduc-
tions about the cumulative information available to them that
‘might well elude an untrained person.’” Id. at 273 (quoting
Cortez, 449 U.S. at 418).
     This standard was met here. Cole was driving on an Illi-
nois interstate with an Arizona driver’s license and a Califor-
nia registration, and his explanation for this discrepancy was
confusing at best. According to Cole, he was a traveling per-
sonal chef who split his time between California, Maryland,
and New York, traveling to each destination by car so that he
could bring his pots and bicycle with him. He claimed to have
had a job at one point in Arizona, and he added that he might
be moving to Florida soon, again for job-related reasons. Even
if this story was not inconceivable, Trooper Chapman reason-
ably suspected that it was false. See Walton, 827 F.3d at 688–89
(ﬁnding reasonable suspicion based in part on defendant’s
“implausible” answers).
   The details of Cole’s current trip were equally dubious and
seemed to evolve throughout the conversation. In Cole’s tell-
ing, he had driven from Maryland to Cincinnati to multiple
locations in Colorado and then to Illinois on his way back to
No. 20-2105                                                  21

Maryland—all in just four or ﬁve days. He originally said he
spent two of the four days in Cincinnati for work, but he
quickly changed his answer and said he just passed through
Cincinnati. His story about Colorado also seemed to evolve.
Initially, he said he met friends and family in “the springs.”
Then, he said he met some friends at the Springs and went to
Boulder to visit a buddy. After that, he said he met some
friends in Colorado because one of them was getting a di-
vorce. Cole’s improbable and inconsistent answers about his
trip details reasonably increased Trooper Chapman’s suspi-
cions. See Lewis, 920 F.3d at 493 (ﬁnding reasonable suspicion
based in part on defendant’s “suspiciously inconsistent” an-
swers).
    Cole’s extreme nervousness reinforced the suspicion. See
United States v. Rodriguez-Escalera, 884 F.3d 661, 669 (7th Cir.
2018) (“[N]ervousness is certainly a factor that can support
reasonable suspicion.”). Trooper Chapman testiﬁed that Cole
was “extremely nervous” throughout the stop, adding that
his neck was sweaty and that he was breathing heavily. Cole
suggests that the dash camera video refutes this testimony,
but the dash camera was not pointed at Cole during the con-
versation. Moreover, the dash camera records Cole himself
commenting on how nervous he was, so if anything, it sup-
ports Trooper Chapman’s testimony. Cole cannot show that
the district court’s ﬁnding of extreme nervousness was clearly
erroneous. See id. (holding that the district court did not have
to credit oﬃcer’s testimony that defendant was nervous
“when the court’s own review of the traﬃc stop footage led it
to the opposite conclusion”).
    Additional factors further supported Trooper Chapman’s
belief that Cole was engaged in criminal activity. Cole’s car
22                                                     No. 20-2105

was newly registered and insured. Trooper Chapman found
this suspicious because he knew that drug traﬃckers often
traded and reregistered cars and purchased insurance for spe-
ciﬁc trips rather than maintaining permanent insurance. Cole
disputes the district court’s ﬁnding that Trooper Chapman
possessed this knowledge. But Deputy Suttles’s message to
Trooper Chapman provided the car’s most recent registration
date, and Cole, himself, told Trooper Chapman that he re-
cently acquired the “insurance, registration, and all that
stuﬀ.” So here too, Cole has not shown clear error. In addition
to the recent registration and insurance purchase, Trooper
Chapman knew from Deputy Suttles that Cole had a covering
over his rear cargo area, which was common among persons
engaged in criminal activity. Finally, Trooper Chapman no-
ticed that Cole had limited luggage in his car—one small
backpack—which was hard to square with Cole’s cross-coun-
try road trip.
    Taken together and assessing the totality of the circum-
stances known to Trooper Chapman, these factors created
reasonable suspicion that Cole was engaged in criminal activ-
ity. We need not consider the other factors that the govern-
ment relies on—e.g., the make of Cole’s car (a Volkswagen),
Cole’s origin in Los Angeles (a supposed drug source loca-
tion), his travel on Interstate-55 (a supposed drug corridor),
and his slow speed and rigid driving posture—though we re-
mind the government to refrain from using criteria so broad
as to subject “a very large category of presumably innocent
travelers” to “virtually random seizures.” Reid v. Georgia, 448
U.S. 438, 441 (1980); see also United States v. Street, 917 F.3d 586,
594 (7th Cir. 2019) (“Without more, a description that applies
to large numbers of people will not justify the seizure of a par-
ticular individual.”).
No. 20-2105                                               23

   Because Trooper Chapman developed reasonable suspi-
cion less than nine minutes into the stop, during the initial
roadside detention, he had a lawful basis for prolonging the
stop to conduct a dog sniﬀ at the gas station, where Cole’s
increasingly incoherent answers and criminal history further
increased his suspicions. See Rodriguez, 575 U.S. at 355.
                            III.
  The trooper’s actions in this case complied with the Fourth
Amendment, so we AFFIRM the district court’s denial of Cole’s
motion to suppress.
24                                                     No. 20-2105

    HAMILTON, Circuit Judge, joined by ROVNER and WOOD,
Circuit Judges, dissenting. A broken taillight, a too-sudden
lane change, or tailgating for a few seconds allows a police
officer to carry out a traffic stop even if the officer’s real pur-
pose is to investigate other possible crimes. In such stops, no
one sees a problem with an officer’s question or two about
where the driver is coming from or going. Answers to those
questions may help the officer understand the situation and
assess the driver’s attitude and potential threats. The major-
ity’s decision today errs, however, by going much further.
Under the majority opinion, the officer may also subject a
driver and passengers to repetitive and detailed questioning
about where they are coming from and where they are going
until the officer is satisfied that the answers are truthful. Ante at
15–16. Given the low “hit rate” of police searches of vehicles
for drugs, this decision will enable police officers to harass
and humiliate civilians far more often than they actually turn
up significant quantities of drugs.
     The scope of permissible police activity in pretextual traf-
fic stops is important. By adopting a general presumption al-
lowing such detailed interrogation as occurred in this case,
the majority enables police officers to subject almost any mo-
torist to similar interrogation, delay, and even humiliation, for
little gain in terms of law enforcement. See Jeannine Bell, The
Violence of Nosy Questions, 100 B.U. L. Rev. 935 (2020) (criticiz-
ing wide discretion for officers to ask “nosy” questions on
fishing expeditions that humiliate and anger drivers stopped
for minor traffic infractions).
    This case presents a pretextual traffic stop based on a po-
lice officer’s hunch that the car was carrying drugs. The video
recording and the officer’s later testimony show that, almost
No. 20-2105                                                    25

from the very outset, the officer prolonged the stop by ques-
tioning the driver at length and in detail on subjects beyond
the legal justification for the stop. Under Rodriguez v. United
States, 575 U.S. 348 (2015), the officer’s prolonging of this stop
violated the Fourth Amendment. We should order suppres-
sion of evidence found later in the stop.
   To be sure, in some traffic stops, some questions about
travel plans will be relevant. For example, an officer who has
reason to believe the driver is impaired by fatigue will want
to know how long the driver has been on the road. In such
cases, an officer should have little difficulty explaining his
questioning in terms of the lawful purpose of the stop. This
stop for tailgating was not such a stop, and the officer offered
no such lawful explanation. I respectfully dissent.
    To explain my conclusion, Part I of this opinion outlines
the legal doctrines allowing pretextual stops and their well-
known consequences. Part II lays out important limits the Su-
preme Court has imposed on such pretextual traffic stops, in
terms of both time and the activities an officer may engage in
unless and until he develops at least reasonable suspicion of
some criminal activity. Part III explains why the traffic stop of
defendant Janhoi Cole was prolonged in violation of the
Fourth Amendment. Part IV identifies further problems in the
majority’s decision. Part V concludes with some suggestions
for going forward in similar cases.
I. Pretextual Traffic Stops and Their Effects
   In Whren v. United States, 517 U.S. 806 (1996), the Supreme
Court held that the reasonableness of a traffic stop under the
Fourth Amendment must be decided using an objective
standard, not the officer’s actual purposes. Whren thus gave
26                                                    No. 20-2105

police officers wide latitude to stop vehicles for reasons hav-
ing nothing to do with the traffic laws that provide lawful pre-
texts for the stops.
    Many of those traffic laws also give an officer considerable
room for judgment and discretion in applying them. In this
case, for example, the stop was justified based on a perceived
violation of this law: “The driver of a motor vehicle shall not
follow another vehicle more closely than is reasonable and pru-
dent, having due regard for the speed of such vehicles and the
traffic upon and the condition of the highway.” 625 ILCS 5/11-
710(a) (emphasis added). Extending that discretion even fur-
ther, courts will uphold a traffic stop based on not only the
actual facts and law but even an officer’s reasonable mistake
of fact or law. Heien v. North Carolina, 574 U.S. 54, 61 (2014).
     The combination of the objective test under Whren, the
number and detail of traffic laws, and the discretion inherent
in applying those laws gives police officers the power to stop
nearly any vehicle if they watch it for more than a few
minutes. See David A. Harris, “Driving While Black” and All
Other Traffic Offenses: The Supreme Court and Pretextual Traffic
Stops, 87 J. Crim. L. & Criminology 544, 545, 558–59 (1997) (“In
the most literal sense, no driver can avoid violating some traf-
fic law during a short drive, even with the most careful atten-
tion;” “with the traffic code in hand, any officer can stop any
driver any time”); Barbara C. Salken, The General Warrant of
the Twentieth Century? A Fourth Amendment Solution to Un-
checked Discretion to Arrest for Traffic Offenses, 62 Temp. L. Rev.
221, 223 (1989) (“The innumerable rules and regulations gov-
erning vehicular travel make it difficult not to violate one of
them at one time or another.”). As then-Attorney General
Robert Jackson said long ago, “We know that no local police
No. 20-2105                                                     27

force can strictly enforce the traffic laws, or it would arrest
half the driving population on any given morning.” Robert
Jackson, The Federal Prosecutor, Address Delivered at the Second
Annual Conference of United States Attorneys (April 1, 1940),
quoted in Morrison v. Olson, 487 U.S. 654, 727–28 (1988)
(Scalia, J., dissenting).
    The phrase “Driving While Black” reflects long recogni-
tion of how Whren enables racially discriminatory stops and
searches. See, e.g., Tracey Maclin, Cops and Cars: How the Au-
tomobile Drove Fourth Amendment Law, 99 B.U. L. Rev. 2317,
2347–49 (2019); David A. Harris, Profiles in Injustice: Why Ra-
cial Profiling Cannot Work 30 (2002); David A. Sklansky, Traffic
Stops, Minority Motorists, and the Future of the Fourth Amend-
ment, 1997 Sup. Ct. Rev. 271, 308–16.
    These police tactics subject large numbers of innocent
drivers to this sort of harassment and humiliation for minimal
gains in drug interdiction. For judges who see these tactics
primarily in criminal prosecutions in the rare cases where
dealer quantities of drugs were found, it’s easy to lose sight of
this reality. Empirical studies based on millions of traffic stops
show: (1) that police departments have exploited Whren to
carry out pretextual stops on a massive scale; (2) that Black
and Hispanic drivers are subjected to such stops and ensuing
searches at substantially higher rates than white drivers; and
(3) that pretextual stops rarely find drugs, let alone dealer
quantities of drugs. The empirical studies have used statistical
methods to control for variables other than racial profiling,
and the disparities remain dramatic. E.g., Emma Pierson et al.,
A Large-Scale Analysis of Racial Disparities in Police Stops Across
the United States, 4 Nature Human Behavior 736 (2020) (based
on data from nearly 100 million stops nationwide); Stephen
28                                                    No. 20-2105

Rushin & Griffin Edwards, An Empirical Assessment of Pre-
textual Stops and Racial Profiling, 73 Stan. L. Rev. 637 (2021)
(based on data from over 8 million stops in Washington state);
Frank R. Baumgartner, Derek A. Epp & Kelsey Shoub, Suspect
Citizens 215 (2018) (based on 18 years of data in North Caro-
lina); Samuel R. Gross & Katherine Y. Barnes, Road Work: Ra-
cial Profiling and Drug Interdiction on the Highway, 101 Mich. L.
Rev. 651, 666–67 (2002) (based on three years of data from
Maryland State Police). The Department of Justice’s own data
has long supported the conclusion that Black and Hispanic
drivers are significantly more likely than white drivers to be
searched during a traffic stop. Patrick A. Langan et al., Bureau
of Justice Statistics, Contacts Between Police and the Public, at
18 (2001).
    For example, the North Carolina study found that, on av-
erage, Black drivers were twice as likely to be searched as
white drivers, with some police forces having much higher
rates of racial disparity. The empirical work also shows that
when police use traffic stops to search for drugs, a small frac-
tion of searches turn up any drugs, and the proportion finding
dealer quantities of drugs is much lower still. The North Car-
olina study looked at data from more than 20 million traffic
stops. Searches were carried out in a small fraction, about
690,000, or 3.36%. Baumgartner et al., Suspect Citizens 59.
Drugs were found—in any quantity—in 96,841 of those stops,
or 14% of all searches. Id. at 62. Typically, dealer quantities are
found in a small fraction of those. See Gross & Barnes, 101
Mich. L. Rev. at 695–97 (88.8% of Maryland State Police vehi-
cle searches in drug corridor did not locate dealer quantities
of drugs). In other words, these intrusive and humiliating po-
lice tactics are used disproportionately on Black and Hispanic
drivers, the vast majority of whom are not trafficking drugs,
No. 20-2105                                                              29

and thus whose cases do not wind up in criminal courts to
shape Fourth Amendment jurisprudence. 1
II. Limits on Pretextual Stops
    While pretextual traffic stops are easy to initiate, the Su-
preme Court has tried to impose some legal limits on them.
Most important, such a stop is limited by time and the pur-
pose that makes the stop lawful in the first place. A seizure
that is “lawful at its inception” can violate the Fourth Amend-
ment if it is “prolonged beyond the time reasonably required
to complete” the initial mission of the stop. Illinois v. Caballes,
543 U.S. 405, 407 (2005).
    The Supreme Court took an important step to make this
limit effective in Rodriguez v. United States, 575 U.S. 348 (2015),
which established the governing law for this appeal. In Rodri-
guez, a police officer had carried out a traffic stop for a car that
had driven onto the shoulder of the highway. After the officer
had issued and explained a written warning to the driver, he
insisted that the driver could not leave until another officer
arrived some minutes later with a drug-sniffing dog, which
led to a search that found drugs in the car.
    The district court in Rodriguez denied a motion to sup-
press, applying circuit precedent holding that dog sniffs that
occur shortly after completion of the traffic stop did not vio-
late the Fourth Amendment if the intrusion on the driver’s lib-
erty was “de minimis.” 575 U.S. at 353. Rodriguez rejected that




    1For interested readers, the articles cited in the text cite in turn nu-
merous other sources on the doctrinal questions and empirical effects of
Whren’s pretextual stops.
30                                                 No. 20-2105

“de minimis” exception. The Court vacated the denial of the
motion to suppress and remanded.
    Establishing guidance that applies here, Rodriguez ex-
plained that “a police stop exceeding the time needed to han-
dle the matter for which the stop was made violates the Con-
stitution’s shield against unreasonable seizures.” 575 U.S. at
350. During a traffic stop, the police officer must stick to the
“mission” of the seizure: ensuring road safety and determin-
ing whether to issue a traffic ticket. “Typically such inquiries
involve checking the driver’s license, determining whether
there are outstanding warrants against the driver, and in-
specting the automobile’s registration and proof of insur-
ance.” Id. at 355. An officer may not prolong the stop, “absent
the reasonable suspicion ordinarily demanded to justify de-
taining an individual.” Id. The latter qualification creates an
opportunity for exploiting pretextual stops. The question for
the officer is whether he can see, hear, or smell anything that
provides reasonable suspicion for expanding the scope of the
pretextual traffic stop.
III. Prolonging the Stop in This Case
   One way to prolong a pretextual stop is to question drivers
and passengers about topics beyond the mission authorized
by the supposed ground for the stop. That’s what happened
here, for all to see in Trooper Chapman’s video recording of
the stop.
   The trooper’s tailgating rationale for stopping Janhoi Cole
was obviously pretextual. The trooper had received the tip
from Deputy Suttles, who suspected the car was transporting
No. 20-2105                                                                  31

drugs. 2 The trooper began following Cole’s car, looking for a
reason to stop him. Cole was driving so carefully that it took
a while. (The most startling fact in this case is that Cole was
driving so carefully that Deputy Suttles never managed to
identify even a pretext for stopping him.) Trooper Chapman
also found no basis for a stop until, finally, Cole entered a con-
struction zone where interstate highway lanes had to merge.
The trooper saw another vehicle cut off Cole’s car. The trooper
did not stop the other vehicle for its dangerous maneuver. In-
stead, he stopped Cole on the ground that he had followed
that other car too closely for a few seconds.
    Following too closely was enough, based on the district
court’s factual findings, to permit the stop under Whren. But
the supposed infraction of following too closely also set limits
on the trooper’s powers over Cole and his vehicle, unless and




    2 The tip from Deputy Suttles fell well short of reasonable suspicion.
He observed that Cole was driving below the speed limit on an interstate
highway in a car with California plates. He sat with an erect posture that
Suttles thought was unusual, and he had empty fast-food wrappers in the
car. Suttles also apparently thought that two contradictory observations
added to the suspicion: that the only luggage he could see was a small
backpack and that the cargo area of the car was covered. See generally
Kansas v. Glover, 589 U.S. ––, ––, 140 S. Ct. 1183, 1190 (2020) (traffic stops
do not “allow officers to stop drivers whose conduct is no different from
any other driver’s”); United States v. Flores, 798 F.3d 645, 649 (7th Cir. 2015)
(“A suspicion so broad that would permit the police to stop a substantial
portion of the lawfully driving public ... is not reasonable.”); United States
v. Ingrao, 897 F.2d 860, 865 (7th Cir. 1990) (reversing denial of motion to
suppress where arrest was based in part on defendant’s cautious driving:
“The mere lawful operation of a motor vehicle should not be considered
suspicious activity absent extraordinary contemporaneous events.”).
32                                                    No. 20-2105

until the trooper developed reasonable suspicion for further
investigation.
    Under Rodriguez and Caballes, the trooper’s authority to
pull Cole over did not give him license to detain Cole for a
speculative search or interrogation for “evidence of ordinary
criminal wrongdoing.” Rodriguez, 575 U.S. at 355, quoting City
of Indianapolis v. Edmond, 531 U.S. 32, 41 (2000). Police deten-
tion, however brief, is not a “minor inconvenience and petty
indignity.” Terry v. Ohio, 392 U.S. 1, 10, 16–17 (1968) (citation
omitted). The Supreme Court has “emphatically reject[ed]”
the notion that the Constitution does not regulate an officer’s
actions when he “accosts an individual and restrains his free-
dom to walk away.” Id. at 16.
    In pretextual traffic stops, courts should expect just the
sort of “mission creep” that we see in this case. See State v.
Jimenez, 420 P.3d 464, 476, 308 Kan. 315, 329–30 (2018) (follow-
ing Rodriguez to affirm suppression of evidence from stop pro-
longed by questions about travel plans unrelated to grounds
for stop). After all, if a stop is actually motivated by a different
purpose, we should expect officers to behave consistently
with their actual purposes, not with the legal fiction that
Whren tolerates.
    That’s what happened here, as the record makes obvious.
Even before stopping Cole, the trooper had already obtained
most of the information that Rodriguez treats as routinely
within the scope of a traffic stop: “determining whether to is-
sue a traffic ticket, … checking the driver’s license, determin-
ing whether there are outstanding warrants against the
driver, and inspecting the automobile’s registration and proof
of insurance.” 575 U.S. at 355. The trooper already had ob-
tained the registration information for the car showing Cole
No. 20-2105                                                                33

as the owner. He also had Cole’s license information. (As for
the last Rodriguez item, insurance, the trooper already knew
that insurance information was on file, though he did not yet
have details. He did nothing more about insurance infor-
mation until nearly twenty minutes into the stop, well after he
had improperly prolonged the stop by interrogating Cole on
other topics.)
    Instead of focusing on the tailgating and the routine topics
of license, registration, and insurance, the trooper almost im-
mediately focused on a different topic: detailed, repetitive,
and intrusive questioning about Cole’s travel itinerary. The
questioning went far beyond a quick and routine “where are
you headed?” or “where are you coming from?” In the ten
minutes of the stop while the trooper kept Cole in the police
car at the side of the highway, about six minutes consisted of
questioning about Cole’s itinerary and the related topic of his
work.3
    We now know that Cole’s confusing answers on those top-
ics were not true. And as a person who was transporting a
substantial quantity of illegal drugs, Cole elicits little sympa-
thy. Yet the stakes here are more important than this one drug

    3 The majority suggests that its essay on travel plan questions results
from the record being “undeveloped” on whether the trooper’s question-
ing actually prolonged the stop. Ante at 11. The record is more than suffi-
cient to say that it did. We have the video recording of the stop. We also
know that the trooper already had license and registration information at
the outset, and that he did not seek more insurance information until
much later in the stop. The government has not tried to show that the
trooper was actually making any progress on the subject of the traffic stop
while he interrogated Cole about his travel plans. Cf. United States v. Lewis,
920 F.3d 483, 492 (7th Cir. 2019) (video and testimony showed that officer
worked on warning while questioning driver about itinerary).
34                                                           No. 20-2105

courier. The evidence is clear that police use these tactics to
stop, search, and even humiliate large numbers of innocent
drivers, and that these tactics are used disproportionately on
Blacks and Hispanics.
    Rodriguez makes clear that a traffic stop’s mission is “to
address the traffic violation that warranted the stop and at-
tend to related safety concerns.” 575 U.S. at 354 (internal cita-
tion omitted); United States v. Clark, 902 F.3d 404, 411 (3d Cir.
2018) (affirming suppression of evidence obtained by pro-
longing traffic stop by questioning driver about his criminal
history). Hence the Rodriguez endorsement of the usual litany:
license, registration, and insurance, and an opportunity to
check for outstanding warrants. 575 U.S. at 355.
    Courts need to guard against unjustified expansion and
prolonging of pretextual stops by questioning on other topics.
As the Third Circuit explained in Clark: “Not all inquiries dur-
ing a traffic stop qualify as ordinarily incident to the stop’s
mission. In particular, those ‘measure[s] aimed at detect[ing]
evidence of ordinary criminal wrongdoing’ do not pass mus-
ter.” 902 F.3d at 410 (alterations in original), quoting Rodri-
guez, 575 U.S. at 355. Since detecting evidence of ordinary
criminal wrongdoing is often the officer’s real purpose, we
should not be surprised when an officer devotes his time to
pursuing his real aims rather than the pretext.4


     4 Whren established that whether a stop is constitutionally permissible

depends on objective grounds, not the officer’s subjective purpose,
whether pretextual or not. Contrary to the majority’s footnote, however,
that rule about the legality of the initial stop does not mean that courts
must or may close their eyes to what was really going on. Cf. ante at 8 n.1.
When considering factual issues that govern whether the officer has gone
No. 20-2105                                                                 35

    Where should we draw the lines on how an officer may
spend his time in such a stop? We start with the Rodriguez list
of the activities typically part of the mission of the traffic stop:
checking license, registration, and insurance information, and
the opportunity to check for outstanding warrants. 575 U.S. at
355. Those actions are designed to protect highway safety by
determining whether the vehicle and driver are authorized to
be on the road at all, and whether they might pose a particular
danger to others on the road. Rodriguez also recognized that
traffic stops can be dangerous for police officers, id. at 356, so
that measures to protect an officer’s safety can also be author-
ized. Beyond the listed topics, however, which activities are
permissible quickly becomes a very case-specific problem. It
defies general rules like the majority’s presumption here.
    Courts applying Rodriguez must consider whether an of-
ficer spent time on matters apart from those safety-based mat-
ters authorized by the lawful but pretextual basis for the stop,
at least unless and until the officer developed reasonable sus-
picion to pursue other matters. See, e.g., United States v. Cortez,
965 F.3d 827, 839–40 (10th Cir. 2020) (assuming without de-
ciding that thirteen minutes of repetitive questioning about
how long driver and passenger had been in town where jour-
ney started was not justified by traffic stop, but officer already

beyond the boundaries permitted by the traffic stop, courts should pay
attention to reality rather than legal fiction. Rodriguez itself makes that
much clear. It directs lower federal courts to consider actual facts in eval-
uating whether a stop has been extended impermissibly. 575 U.S. at 357
(“The reasonableness of a seizure, however, depends on what the police
in fact do. See Knowles [v. Iowa, 525 U.S. 113, 115–17 (1998).] In this regard,
the Government acknowledges that ‘an officer always has to be reasona-
bly diligent.’ Tr. of Oral Arg. 49. How could diligence be gauged other
than by noting what the officer actually did and how he did it?”).
36                                                    No. 20-2105

had independent reasonable suspicion of human smuggling
before beginning those questions); Clark, 902 F.3d at 410–11
(stop improperly prolonged to question driver about his crim-
inal history); United States v. Evans, 786 F.3d 779, 787 (9th Cir.
2015) (stop improperly prolonged to see if driver had
properly registered in Nevada registry of ex-felons).
    Turning to questions about travel plans, courts must “in-
quire whether, on the facts of the particular case, [itinerary]
questioning is within the traffic stop’s mission” and if not,
must determine whether the questioning impermissibly
lengthened the stop. 4 Wayne R. LaFave, Search & Seizure
§ 9.3(d) (6th ed. 2020). There has never been a problem with a
brief question or two about travel like, “Where are you
headed today?” or “Where are you coming from?” As the ar-
resting officer in Cortez testified, innocuous background ques-
tions can help an officer assess a driver’s stress and possible
evasion, and they may help an officer gauge how cautious he
needs to be in the stop. 965 F.3d at 839.
    Similarly, if an officer has reason to suspect that a driver
may be impaired by fatigue, alcohol, or drugs, questioning
about how long the driver has been on the road and where he
is headed might help the officer assess the driver’s condition
and any dangers that might be posed. Jimenez, 420 P.3d at 475–
76, 308 Kan. at 329; see also Navarette v. California, 572 U.S. 393,
402–03 (2014) (report that truck had forced another vehicle off
road gave officer reasonable suspicion that driver was im-
paired, permitting stop to investigate). In other cases, infor-
mation about travel plans might help an officer decide
whether to issue a ticket or a warning, or perhaps even to hop
back in the police car and lead a speeding car to a hospital so
No. 20-2105                                                  37

the passenger can safely give birth. See United States v.
Brigham, 382 F.3d 500, 508 & n.6 (5th Cir. 2004) (en banc).
    This case, however, is not about such brief, routine, and
easily justifiable questions. This case is about whether an of-
ficer may start with those questions and then prolong the stop
while continuing to probe the answers, looking for evasion
and contradiction by asking more questions, by repeating the
questions, by asking others the same questions, and by check-
ing answers against other information that might be available
with in-car computers. As Professor LaFave has explained in
his treatise, the controversy is over
      multi-question extended inquiries of vehicle oc-
      cupants into the most minute details regarding
      the parts of the journey completed and lying
      ahead. The officers are “trained to subtly ask
      questions about * * * their destination, their itin-
      erary, the purpose of their visit, the names and
      addresses of whomever they are going to see,
      etc.,” “to make this conversation appear as nat-
      ural and routine a part of the collection of infor-
      mation incident to a citation or warning,” and
      “to interrogate the passengers separately, so
      their stories can be compared.” The objective is
      not to gain some insight into the traffic infrac-
      tion providing the legal basis for the stop, but to
      uncover inconsistent, evasive or false assertions
      that can contribute to reasonable suspicion or
      probable cause regarding drugs.
38                                                             No. 20-2105

4 LaFave, Search & Seizure § 9.3(d) (footnotes omitted), quot-
ing Gross & Barnes, 101 Mich. L. Rev. at 685. 5
    Cases after Rodriguez from around the country illustrate
the wide, almost kaleidoscopic variations in the ways these
questions can arise and play out. Several circuits have taken
the route the majority does here, which I believe is contrary to
Rodriguez, writing that questions about a driver’s travel plans
are ordinarily within the scope of a traffic stop, and that an
officer may prolong a stop to ask follow-up questions to con-
firm or check those answers. United States v. Braddy, 11 F.4th
1298, 1311 (11th Cir. 2021) (following pre-Rodriguez case law
on itinerary questions, at least where driver’s license had in-
correct address and ownership of vehicle was not clear);
United States v. Dion, 859 F.3d 114, 125–26 & n.7 (1st Cir. 2017)
(defendant conceded that pre-Rodriguez case law allowed itin-
erary questions); United States v. Collazo, 818 F.3d 247, 258 (6th
Cir. 2016) (allowing questions to follow up on conflicting an-
swers from driver and passenger). But see United States v.
Callison, 2 F.4th 1128, 1131–32 & n.2 (8th Cir. 2021) (holding
that itinerary questions were permissible because the officer,
as a matter of fact, was still “handl[ing] the matter for which
the stop was made,” but declining to reach the question of
“the extent to which officers may ask travel-related questions


     5 The majority asserts that this stop was not a “fishing expedition,” see

ante at 18, and implies that it was Cole’s answers to the travel plan ques-
tions that led the trooper to suspect that he was transporting drugs. Ante
at 2. The record contradicts both the assertion and the implication. The
trooper was always acting on Deputy Suttles’ hunch that Cole was trans-
porting drugs. He was looking for a way to justify a longer stop that would
lead to a search. And as the trooper later testified, he simply was not going
to let Cole go, no matter what, until a dog could sniff the car for drugs.
No. 20-2105                                                   39

during a routine traffic stop after Rodriguez.”) (alteration in
original), quoting Rodriguez, 575 U.S. at 350.
    The majority’s summary of other courts’ decisions, how-
ever, glosses over substantial variety among the approaches.
Other courts have wisely taken more nuanced and fact-spe-
cific approaches to the problem, recognizing that not all traffic
stops justify prolonged and close interrogation about travel
plans. See, e.g., United States v. Gomez-Arzate, 981 F.3d 832,
836, 840–44 (10th Cir. 2020) (finding that a few minutes of itin-
erary questioning that prolonged an already completed stop
violated Constitution, but noting extended inquiry into car
ownership may be permissible where driver is not listed on
registration and cannot say who owns vehicle); United States
v. Garner, 961 F.3d 264, 271–72 (3d Cir. 2020) (some itinerary
questions were permissible; some follow-up on employment,
family, criminal history, and unrelated conduct was not, but
officer’s reasonable suspicion of criminal activity permitted
the additional questioning); Jimenez, 420 P.3d at 469, 475–77,
308 Kan. at 318, 328–30 (affirming suppression where itiner-
ary questions prolonged stop for following too closely, and
noting that courts must guard against “mission creep” in pre-
textual traffic stops); see also Cortez, 965 F.3d at 839–40 (some
itinerary questions were permissible, but later follow-up
questioning fell outside bounds permitted by original reason
for stop).
    Disagreeing with the majority’s rule in this case, Professor
LaFave’s treatise has this to say about travel-plan questioning
as it is actually carried out by officers who are looking for
drugs:
       The objective is not to gain some insight into the
       traffic infraction providing the legal basis for
40                                                   No. 20-2105

       the stop, but to uncover inconsistent, evasive or
       false assertions that can contribute to reasonable
       suspicion or probable cause regarding drugs.
       Thus, “[n]ot only are questions about travel
       plans investigatory rather than merely conver-
       sational, the ordinary traveler cannot reasona-
       bly be expected to decline to answer such ques-
       tions, particularly if they are posed while an of-
       ficer is holding the driver’s license and other es-
       sential documents.”
4 LaFave, Search & Seizure § 9.3(d) (alteration in original)
(footnote and citation omitted).
    In this case, the trooper’s questions did nothing to advance
the limited road- and driver-safety missions that he was le-
gally authorized to pursue. Cole’s claim to be a California-
based traveling personal chef employed part-time in Mary-
land had nothing to do with whether he was safe to continue
driving. And Trooper Chapman knew that Cole was author-
ized to drive the Volkswagen when he saw that his name
matched the registration mere seconds into the initial ten-mi-
nute stop at the roadside.
    It should not matter here whether, at some later point,
Cole’s answers became suspicious. The critical point under
Rodriguez is that it was unconstitutional to prolong the stop,
the restraint on liberty, to ask those questions to begin with.
United States v. Lopez, 907 F.3d 472, 486–87 (7th Cir. 2018) (sup-
pressing evidence gathered following questioning that pro-
longed seizure); see also Garner, 961 F.3d at 270–71 (looking
for “Rodriguez moment” when officer began pursuing off-mis-
sion tasks); United States v. Childs, 277 F.3d 947, 952 (7th Cir.
2002) (en banc) (“Questioning that prolongs the detention, yet
No. 20-2105                                                   41

cannot be justified by the purpose of such an investigatory
stop, is unreasonable under the fourth amendment.”), citing
United States v. Sharpe, 470 U.S. 675, 685 (1985).
   When asked to explain his actions, Trooper Chapman ad-
mitted that he delayed collecting the last of the authorized in-
formation (for investigating the tailgating and Cole’s driving)
because he “was trying to piece together Mr. Cole’s story,
which was—as we all heard, was kind of inconsistent.
Changed each time.” Tr. 35.
    With respect, that is not how this is supposed to work. Un-
der the Constitution, people do not need “stories” to travel on
interstate highways—even if they have a broken taillight,
don’t signal a lane change, or briefly tailgate another vehicle.
Unless an officer efficiently processing the legitimate purpose
of the stop sees, hears, or smells something new that gives him
reasonable suspicion of other criminal activity, he needs to let
the driver go with a ticket or warning when the legitimate
tasks are done. This rule applies even if the officer still has a
hunch the driver is up to no good.
    We have explained that during a Terry stop, one of three
things must happen:
       (1) the police gather enough information to de-
       velop probable cause and allow for continued
       detention; (2) the suspicions of the police are
       dispelled and they release the suspect; or (3) the
       suspicions of the police are not dispelled, yet the
       officers have not developed probable cause but
       must release the suspect because the length of
       the stop is about to become unreasonable.
42                                                  No. 20-2105

United States v. Leo, 792 F.3d 742, 751 (7th Cir. 2015) (internal
citations omitted). An officer who reasonably believes a
driver is suspicious based on some ambiguous or conflicting
statements may not detain the suspect indefinitely, lest the
stop turn into “a de facto arrest that must be based on proba-
ble cause.” See id., quoting United States v. Bullock, 632 F.3d
1004, 1015 (7th Cir. 2011).
IV. Other Problems with the Majority Holding
    The majority here adopts a different rule, at least “ordinar-
ily.” Ante at 12 (“[W]e hold that travel-plan questions ordi-
narily fall within the mission of a traffic stop.”). The majority
does not hint at what might not be ordinary. It offers instead
what is supposed to be a reassuring limit: “This does not
mean, however, that officers have a free pass to ask travel-
plan questions until they are subjectively satisfied with the
answers. [Such questions] must remain reasonable, and rea-
sonableness is an objective standard based on all the circum-
stances.” Ante at 13. If the officer’s questions “go too far and
become unreasonable,” the stop may no longer be permissi-
ble. Ante at 16.
    Despite that assurance, the majority’s approach invites un-
reasonable restraints on liberty. The majority adds that an of-
ficer asking travel-plan questions may ask “reasonable fol-
low-up questions,” especially if the answers are “evasive, in-
consistent, or improbable.” Ante at 16. That’s the critical door
that enables further abuse of pretextual traffic stops, prolong-
ing those stops as the officer uses the coercive power of the
state and the authority to use force to subject drivers and their
passengers to close questioning in search of other criminal ac-
tivity. That is exactly what Rodriguez rejected. 575 U.S. at 355–
56. All the other questions that Rodriguez treats as part of the
No. 20-2105                                                   43

mission of every stop should quickly produce a clear answer
rather than inviting discretionary interrogation. A driver’s li-
cense can be valid or not, but it is unlikely to call for follow-
up questions.
    In Rodriguez, the Supreme Court pointedly declined to cat-
egorically permit questioning about travel plans as central—
even “ordinarily” central—to traffic stops’ missions. The of-
ficer in Rodriguez had asked the driver and passenger about
their itinerary, 575 U.S. at 351, but the Court left travel plans
out of the topics typically permissible because they help en-
sure that vehicles are “operated safely and responsibly,” id. at
355. The majority responds to this omission by noting that ju-
dicial opinions are not statutes and that the travel-plan ques-
tions were not directly at issue in Rodriguez, so we should in-
fer nothing from the omission of travel-plan questions from
the Rodriguez list. Ante at 11.
    That is an unduly narrow understanding of the opinion.
The Court knew it was providing important and practical
guidance for police officers and motorists all over the nation,
especially with that key passage about what is “typically”
within the scope of a traffic stop. No one suggests that the list
is universal and complete for all cases. As noted above, for
some traffic stops travel plans will be relevant. But those cases
should be evaluated based on their specific facts, not using a
general rule that allows such persistent, repetitive, and close
questioning in a stop legally justified as merely a routine traf-
fic stop. At a minimum, courts should expect an officer who
engages in such questioning to be able to explain how, specif-
ically, the questioning was based on the legal justification for
the stop. As Professor LaFave has explained:
44                                                  No. 20-2105

       [G]iven the Supreme Court’s Rodriguez decision,
       … the contention ”that unrestrained travel plan
       questioning is routine and always within a traffic
       stop’s mission” must be rejected out of hand, and …
       instead courts must inquire whether, on the
       facts of the particular case, such questioning is
       within the traffic stop’s mission.
4 LaFave, Search & Seizure § 9.3(d) (emphasis added) (foot-
note and citation omitted).
    The extraordinary nature of this en banc rehearing also
should not be passed by in silence. After the panel issued its
decision, the government chose not to seek en banc review. It
also informed this court that it did not oppose Cole’s motion
for immediate release from prison. No litigant is better able to
protect its interests in the federal courts than the federal gov-
ernment. This court chose, however, to act sua sponte to re-
hear the case en banc. That is an extraordinary step that this
court has taken very rarely.
    The majority suggests that en banc review was needed to
resolve an apparent conflict between the panel decision here
and another post-Rodriguez decision, United States v. Lewis,
920 F.3d 483 (7th Cir. 2019). The supposed conflict was illu-
sory. Lewis did not hold that an officer may prolong a stop
indefinitely to ask increasingly invasive and repetitive ques-
tions about a driver’s travels and employer—nor could it
have, given Rodriguez. As Lewis explained, the most important
reason it had for affirming denial of the motion to suppress
there was that the defendant had simply failed as a matter of
fact to show that the questioning had actually prolonged the
stop. Id. at 492. Careful analysis of Lewis shows that the case
is distinguishable on that fact, which is decisive under
No. 20-2105                                                   45

Rodriguez. See United States v. Cole, 994 F.3d 844, 855–57 (7th
Cir. 2021) (panel decision here).
V. Moving Forward
    Having explained why I view the majority’s general pre-
sumption in favor of allowing questions about travel plans in
pretextual traffic stops as unwise and contrary to Rodriguez, it
is still necessary to look toward future cases.
    District courts should be alert for unconstitutional “mis-
sion creep” where the stop is justified constitutionally by one
limited purpose but is actually motivated by a different pur-
pose. See Jimenez, 420 P.3d at 476, 308 Kan. at 329–30. In such
cases, district courts must make the joint legal and factual de-
termination of how long was reasonably necessary to execute
the stop’s permissible mission, and must then decide whether
the stop’s duration exceeded that limit or the officer otherwise
unreasonably prolonged the stop. Extensive itinerary ques-
tions posed to a motorist stopped for a broken taillight or tail-
gating, for example, should not pass muster.
    Courts deciding motions to suppress often give officers
substantial leeway in evaluating their actions and credibility.
An obviously pretextual stop, however, calls for more skepti-
cism. We should expect officers to behave in ways that serve
their real purpose, without necessarily working from the pre-
textual basis for the stop. When officers do so, district courts
should make the appropriate factual findings, and our review
of their fact-finding should be deferential. E.g., United States
v. Simon, 937 F.3d 820, 832–33 (7th Cir. 2019) (deferring to dis-
trict court’s credibility determinations as to whether the offic-
ers prolonged a stop); Lewis, 920 F.3d at 492 (similar); see also
United States v. Rodriguez-Escalera, 884 F.3d 661, 672 (7th Cir.
46                                               No. 20-2105

2018) (affirming grant of motion to suppress based on factual
findings, including those on credibility).
   We should reverse this judgment, suppress the evidence
obtained by improperly prolonging this traffic stop, and re-
mand to allow Cole to withdraw his guilty plea.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Conner.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Conner"
type: case
citation: "127 F.3d 663 (1997)"
parallel_cite: ""
neutral_cite: "1997 U.S. App. LEXIS 27680; 1997 WL 615947"
court: "U.S. Court of Appeals, 8th Circuit"
court_level: coa
circuit: 8th
year: 1997
date_decided: 1997-10-08
docket: ""
authority_weight: "Binding in-circuit — 8th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Conner
  varies_by_point: false
  scope_note: "Good law in-circuit; a door opened in submission to a police demand under color of authority is not consensual."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/747208/united-states-v-larry-duane-conner-united-states-of-america-v-john/"
  cluster_id: 747208
  opinion_id: 9490703
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Recent development (role-based)"
related: ["[[Payton v. New York]]", "[[Schneckloth v. Bustamonte]]", "[[United States v. Drayton]]"]
aliases: ["United States v. Larry Duane Conner"]
tags: ["case", "fourth-amendment", "consent", "securing-the-scene"]
holding: "Where police, under color of authority, demand that occupants of a motel room open the door, and an occupant opens the door not…"
lake:
  record_id: United States v. Conner
  status: verified
  projected_at: 2026-07-06
---

# United States v. Conner

*127 F.3d 663 (8th Cir. 1997)* · U.S. Court of Appeals, 8th Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Four police officers positioned themselves at the door of a motel room and knocked longer and more vigorously than an ordinary visitor — loudly enough to wake guests in neighboring rooms. When an occupant opened the door, the officers gained visual and physical access to the room. The district court found the officers had entered "under color of authority" and that the occupant opened the door not voluntarily but in response to their show of authority.

## Issue
Whether police obtain lawful, consensual access to a motel room when an occupant opens the door in submission to a police demand made under color of authority, rather than voluntarily.

## Rule
A door opened in submission to authority is not consent: "an unconstitutional search occurs when officers gain visual or physical access to a motel room after an occupant opens the door not voluntarily, but in response to a demand under color of authority." — 127 F.3d at 666. ^pin-666

Whether the door-opening was voluntary or coerced is judged by how the encounter would appear to a reasonable person; a coercive, badge-backed demand to open the door is a Fourth Amendment intrusion, not a consensual entry.

## Application
On these facts the record amply supported that the officers acted under color of authority: four of them massed at the door and knocked far more forcefully and persistently than a private citizen would, in a manner calculated to compel a response. The occupant's opening of the door was therefore submission to that authority, not voluntary consent. Because the officers gained access by coercion rather than consent, their entry was an unconstitutional search.

## Conclusion
The motel-room entry was an unconstitutional search because the door was opened in response to a demand under color of authority, not voluntarily. Police cannot manufacture consensual access by compelling an occupant to open the door through a coercive show of authority.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 8th Cir.**
- *Conner* applies the warrant-protection of the dwelling recognized in [[Payton v. New York]] (a motel room is a temporary home) and the voluntariness requirement of [[Schneckloth v. Bustamonte]]; contrast [[United States v. Drayton]], where officers merely requested cooperation without a coercive show of authority.

## Appears on
- [[Securing the Scene]] — *Recent development (role-based)*

## Sources
- *United States v. Conner*, 127 F.3d 663 (8th Cir. 1997) — https://www.courtlistener.com/opinion/747208/united-states-v-larry-duane-conner-united-states-of-america-v-john/ — pinpoint: 666 (CL carries the opinion without star pagination; pinpoint per the published reporter).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2df61cc37d46b573", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Conner"}, "payload": {"all": [{"cite": "127 F.3d 663", "page": "663", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "1997 U.S. App. LEXIS 27680", "page": "27680", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}, {"cite": "1997 WL 615947", "page": "615947", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1997"}], "display": "127 F.3d 663", "official": {"cite": "127 F.3d 663", "page": "663", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "127"}, "official_selection_present": true, "record_id": "United States v. Conner"}}
{"assertion_id": "33a308332580f377", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-666", "record_id": "United States v. Conner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-666", "pinpoint_status": "slip-only", "quote": "and that the occupant opened the door not voluntarily but in response to their show of authority. ## Issue Whether police obtain lawful, consensual access to a motel room when an occupant opens the door in submission to a police demand made under color of authority, rather than voluntarily. ## Rule A door opened in submission to authority is not consent:", "quote_fidelity": "mismatch", "record_id": "United States v. Conner", "star_marker": null}}
{"assertion_id": "b025057ae0d2d2e1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Conner"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Conner", "scope_note": "Good law in-circuit; a door opened in submission to a police demand under color of authority is not consensual.", "varies_by_point": false}}
```

### lake record — United States v. Conner

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Conner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Larry Duane Conner, United States of America v. John Charles Tilton",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Appellant, v. Larry Duane CONNER, Appellee; UNITED STATES of America, Appellant, v. John Charles TILTON, Appellee",
    "input_case_name": "United States v. Conner",
    "court": "U.S. Court of Appeals, 8th Circuit",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "8th",
    "state": null,
    "date_decided": "1997-10-08",
    "year": 1997,
    "docket": null,
    "cluster_id": 747208,
    "lead_opinion_id": 9490703,
    "sibling_ids": [
      747208,
      9490703,
      9490704
    ],
    "absolute_url": "/opinion/747208/united-states-v-larry-duane-conner-united-states-of-america-v-john/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "127 F.3d 663",
      "volume": "127",
      "reporter": "F.3d",
      "page": "663",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. App. LEXIS 27680",
        "volume": "1997",
        "reporter": "U.S. App. LEXIS",
        "page": "27680",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 WL 615947",
        "volume": "1997",
        "reporter": "WL",
        "page": "615947",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "127 F.3d 663",
        "volume": "127",
        "reporter": "F.3d",
        "page": "663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. App. LEXIS 27680",
        "volume": "1997",
        "reporter": "U.S. App. LEXIS",
        "page": "27680",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 WL 615947",
        "volume": "1997",
        "reporter": "WL",
        "page": "615947",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "127 F.3d 663",
    "official_selection": {
      "court_class": "coa",
      "selected": "127 F.3d 663",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-666",
      "page": null,
      "quote": "and that the occupant opened the door not voluntarily but in response to their show of authority. ## Issue Whether police obtain lawful, consensual access to a motel room when an occupant opens the door in submission to a police demand made under color of authority, rather than voluntarily. ## Rule A door opened in submission to authority is not consent:",
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
    "composite_basis_ref": "United States v. Conner",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; a door opened in submission to a police demand under color of authority is not consensual.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Randy Lee Vanhorn",
          "cluster_id": 778362,
          "cite": [
            "296 F.3d 713",
            "2002 WL 1540153"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rene Madrid",
          "cluster_id": 757241,
          "cite": [
            "152 F.3d 1034",
            "1998 U.S. App. LEXIS 20785",
            "1998 WL 538150"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 98-3583",
          "cluster_id": 764869,
          "cite": [
            "180 F.3d 967"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spotted Elk",
          "cluster_id": 1285159,
          "cite": [
            "548 F.3d 641",
            "2008 U.S. App. LEXIS 24202",
            "2008 WL 4999125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Berry Washington",
          "cluster_id": 788213,
          "cite": [
            "387 F.3d 1060",
            "2004 U.S. App. LEXIS 22710",
            "2004 WL 2435487"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Are",
          "cluster_id": 1434458,
          "cite": [
            "590 F.3d 499",
            "2009 U.S. App. LEXIS 28701",
            "2009 WL 5125820"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mar James, Also Known as James Beine",
          "cluster_id": 784577,
          "cite": [
            "353 F.3d 606",
            "2003 U.S. App. LEXIS 26148",
            "2003 WL 22998108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reeves",
          "cluster_id": 170685,
          "cite": [
            "524 F.3d 1161",
            "2008 U.S. App. LEXIS 9808",
            "2008 WL 1961246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tonnie Franklin Williams",
          "cluster_id": 764955,
          "cite": [
            "181 F.3d 945",
            "1999 U.S. App. LEXIS 13704",
            "1999 WL 410110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawyer v. City of Council Bluffs",
          "cluster_id": 785513,
          "cite": [
            "361 F.3d 1099",
            "2004 U.S. App. LEXIS 5689"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruth Lee, United States of America v. Michael Sandmeyer",
          "cluster_id": 784928,
          "cite": [
            "356 F.3d 831",
            "2003 U.S. App. LEXIS 26456"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. State",
          "cluster_id": 2275446,
          "cite": [
            "813 A.2d 231",
            "372 Md. 386",
            "2002 Md. LEXIS 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tejada",
          "cluster_id": 1195099,
          "cite": [
            "524 F.3d 809",
            "2008 U.S. App. LEXIS 7658",
            "2008 WL 962837"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marrocco",
          "cluster_id": 1456522,
          "cite": [
            "578 F.3d 627",
            "2009 U.S. App. LEXIS 18980",
            "2009 WL 2581339"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cox v. State",
          "cluster_id": 854101,
          "cite": [
            "696 N.E.2d 853",
            "1998 Ind. LEXIS 84",
            "1998 WL 340696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Vincent Kelly",
          "cluster_id": 782013,
          "cite": [
            "329 F.3d 624",
            "2003 U.S. App. LEXIS 10415",
            "2003 WL 21212088"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rutter",
          "cluster_id": 1891781,
          "cite": [
            "93 S.W.3d 714",
            "2002 Mo. LEXIS 146",
            "2002 WL 31863839"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Deandra Sue Warford, United States of America v. Phillip Whatley",
          "cluster_id": 793505,
          "cite": [
            "439 F.3d 836",
            "2006 U.S. App. LEXIS 5554",
            "2006 WL 522210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Deshawne Glenn, Also Known as George Loper",
          "cluster_id": 757243,
          "cite": [
            "152 F.3d 1047",
            "1998 U.S. App. LEXIS 20858",
            "1998 WL 541579"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Marion",
          "cluster_id": 771898,
          "cite": [
            "238 F.3d 965",
            "2001 U.S. App. LEXIS 1719",
            "2001 WL 96090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mowatt",
          "cluster_id": 1024793,
          "cite": [
            "513 F.3d 395",
            "2008 U.S. App. LEXIS 1438",
            "2008 WL 203581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillip W. Hammons",
          "cluster_id": 757239,
          "cite": [
            "152 F.3d 1025",
            "1998 U.S. App. LEXIS 20786",
            "1998 WL 538141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mastella L. Jackson",
          "cluster_id": 3219456,
          "cite": [
            "369 Wis. 2d 673",
            "2016 WI 56",
            "882 N.W.2d 422",
            "2016 Wisc. LEXIS 161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Conner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(747208 OR 9490703 OR 9490704) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca8)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 2,
        "triage_snippet_classified": 28
      },
      "lane2_top_cited": {
        "query": "cites:(747208 OR 9490703 OR 9490704)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02JnM9MTQ1NDE3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28747208+OR+9490703+OR+9490704%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(747208 OR 9490703 OR 9490704)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(747208 OR 9490703 OR 9490704)",
    "indexed_citing_opinions": 84,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 747208,
        "count": 78,
        "count_source": "search"
      },
      {
        "opinion_id": 9490703,
        "count": 6,
        "count_source": "search"
      },
      {
        "opinion_id": 9490704,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 109,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-conner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjMzNTI5MDQmcz02MjUzMDcmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28747208+OR+9490703+OR+9490704%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 747208,
        "cited_id": 6756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 154170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 610652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 629188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 663762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 677812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 701300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 703196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 710920,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 722457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 722623,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 737426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 747208,
        "cited_id": 2098652,
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
    "date_created": "2026-07-05T23:13:14Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:13:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Conner

```
<opinion type="majority">
<author id="b732-18">HEANEY, Circuit Judge.</author>
<p id="b732-19">The government appeals the district court’s suppression of evidence obtained after police demanded entry into a motel room rented by appellants. We affirm.</p>
<p id="b732-20">I.</p>
<p id="b732-21">On February 22,1996, a federal grand jury in the Northern District of Iowa returned separate two-count indictments against Larry Duane Conner and John Charles Tilton charging each with being a convicted felon in possession of a firearm, <span class="citation no-link">18 U.S.C. § 922</span>(g)(1), and with possession of a stolen firearm, <span class="citation no-link">18 U.S.C. § 922</span>(j). Both defendants moved to suppress evidence seized pursuant to a search warrant authorizing the search of Room 31 at the Elmdale Motel in Sioux City, Iowa. Conner also moved to suppress evidence seized from his home pursuant to a warrant. Conner and Tilton argued that the court should suppress the evidence obtained pursuant to the warrants because police used illegal methods to obtain the information relied on to establish the probable cause to issue the search warrant. After an evidentiary hearing, the district court granted the motions to suppress. The court agreed that essential information in the search warrant affidavits was obtained in violation of the Fourth Amendment. The court rejected the government’s contention that the evidence <page-number citation-index="1" label="665">*665</page-number>was admissible under either the good-faith exception or the independent-source exception.</p>
<p id="b733-4">We find no clear error in the district court’s detailed factual findings. <em>See United States v. McMurray, </em><span class="citation" data-id="6932131"><a href="/opinion/7030110/united-states-v-mcmurray/#1409" aria-description="Citation for case: United States v. McMurray">34 F.3d 1405, 1409</a></span> (8th Cir.1994) (standard of review) (citations omitted). Police in Sioux City, Iowa were investigating a burglary that occurred in late December 1995. The victim had given police a detailed description of the stolen items, which included a large coin collection, jewelry, silver place settings, and three handguns. Several days after the burglary, police received an anonymous telephone call reporting that Larry Conner and John Tilton had committed the burglary and that they were staying at an unknown hotel or motel in Sioux City. According to the caller, Conner and Tilton had the coins with them and they were preparing to leave the city later that day to dispose of the stolen property. They reportedly had been driving a red Pontiac Fiero with Iowa license plate WEH624.</p>
<p id="b733-5">Based on the anonymous tip, police cheeked area motels and hotels for the red Fiero. Because three handguns had been taken in the burglary, the investigators believed that Conner and Tilton might be armed. Two Sioux City police detectives located the Fiero in front of Room 31 at the Elmdale Motel and called for backup. In all, six police officers were on the scene; only one was in uniform. Sergeant Young, the officer in charge, testified that he planned to knock on the front door of the room and attempt to speak to individuals inside about the burglary. He incorrectly assumed that one of the other officers had checked with the motel office to ascertain who had rented Room 31. In fact, at the time the officers approached Room 31, they did not know that Conner had rented the room. The officers approached Room 31 solely because they observed the red Fiero parked in front of it.</p>
<p id="b733-6">Two officers, including Sergeant Young, went to the door of Room 31; two others positioned themselves by the room’s picture window; and two officers took up positions behind the motel. One of the officers, who knew nothing about the burglary except what he had been told when he arrived at the motel, noticed packages of coins on the windowsill between the room’s curtains and window. He attempted to draw the coins to the attention of the officer in charge, but no other officer noticed the gesture or the coins on the windowsill.</p>
<p id="b733-8">An officer knocked on the door and identified himself as a police officer. No one in the room responded. The officer knocked again, and announced a second time that he was a police officer. One of the officers stationed by the window saw someone move aside the drawn curtains and look out of the window. In response, the police repositioned themselves for better protection, and at least one officer drew his pistol and held it behind his back. The officer at the door knocked again and announced the police presence. In addition, Sergeant Young shouted, “Open up,” in a voice loud enough to be heard by a motel resident two rooms away. The officers were loud enough to awaken another guest and cause her to step out of her room under the mistaken belief that the police were knocking at her door.</p>
<p id="b733-9">Shortly after the officers’ third attempt, Tilton opened the door to the room. The district court explicitly found that Tilton opened the door in response to Sergeant Young’s command. When Tilton opened the door, officers observed what appeared to be foreign currency, coins, and envelopes the size of currency on the bed and blue, gold, and maroon boxes matching the victim’s description scattered throughout the room. Believing that the currency and other materials were related to the burglary, Sergeant Young drew his weapon on Tilton, ordered him to back away from the door, and placed him under arrest. Another officer found Conner in the bathroom and arrested him as well.</p>
<p id="b733-10">The officers stayed in the motel room to secure the evidence but did not conduct a search of the room until they obtained a warrant. The search warrant application included the following information: “Officers knocked on the [motel] door and .identified themselves and Mr. Tilton opened the door. At that time, in plain view were coin rolls and coin sets throughout the room.” The police obtained a search warrant for the motel room <page-number citation-index="1" label="666">*666</page-number>and seized a Smith &amp; Wesson .38 caliber revolver, a Colt pistol, coins, three large briefcases, and other items believed to have been taken during the burglary. After searching the room, police obtained a warrant for Conner’s residence in Sloan, Iowa based on the same facts used to support the first warrant and a list of the items seized from the motel room. During the search of Conner’s house, law enforcement officers seized items they believed had also been taken during the burglary.</p>
<p id="b734-4">II.</p>
<p id="b734-5">Based on these facts, we agree with the district court that the officers’ entry into the motel room and arrest of the occupants violated Conner’s and Tilton’s Fourth Amendment rights. It is a well-established constitutional principle that law enforcement officers may not enter a person’s home without a warrant unless the entry is justified by exigent circumstances or the consent of the occupant. <em>Steagald v. United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U.S. 204, 211</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#1647" aria-description="Citation for case: Steagald v. United States">101 S.Ct. 1642, 1647</a></span>, <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">68 L.Ed.2d 38</a></span> (1981); <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1380</a></span>, 63 L.Ed,2d 639 (1980). In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the Supreme Court explained that no zone of privacy is more clearly defined than a person’s home: “[T]he Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1382</a></span>. The same protection against unreasonable searches and seizures extends to a person’s privacy in temporary dwelling-places such as hotel or motel rooms. <em>Hoffa v. United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U.S. 293, 301</a></span>, <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#413" aria-description="Citation for case: Hoffa v. United States">87 S.Ct. 408, 413</a></span>, <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">17 L.Ed.2d 374</a></span> (1966); <em>Stoner v. California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#490" aria-description="Citation for case: Stoner v. California">376 U.S. 483, 490</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#893" aria-description="Citation for case: Stoner v. California">84 S.Ct. 889, 893-94</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">11 L.Ed.2d 856</a></span> (1964); <em>United States v. Rambo, </em><span class="citation" data-id="469416"><a href="/opinion/469416/united-states-v-douglas-edward-rambo/#1295" aria-description="Citation for case: United States v. Douglas Edward Rambo">789 F.2d 1289, 1295</a></span> (8th Cir.1986).</p>
<p id="b734-9">The government contends that <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>does not apply because the police did not “enter” the motel room; they merely observed contraband in plain view when Til-ton opened the door. In other words, the government asserts that Conner and Tilton voluntarily engaged with the police at the motel. <em>See United States v. Deanda, </em><span class="citation" data-id="710920"><a href="/opinion/710920/united-states-v-ben-nouglas-deanda-edward-contrell-sample-edmond-clyde/#825" aria-description="Citation for case: United States v. Ben Nouglas Deanda, Edward Contrell...">73 F.3d 825, 825-26</a></span> (8th Cir.1996) (person who opens door voluntarily or in response to a simple knock by police knowingly exposes to the public anything that can be seen through the door thereby defeating any possible Fourth Amendment arguments because it involves no “search.”); <em>United States v. Peters, </em><span class="citation" data-id="547018"><a href="/opinion/547018/united-states-v-ronald-e-peters/#210" aria-description="Citation for case: United States v. Ronald E. Peters">912 F.2d 208, 210</a></span> (8th Cir.1990) (same). The district court, however, correctly determined that an unconstitutional search occurs when officers gain visual or physical access to a motel room after an occupant opens the door not voluntarily, but in response to a demand under color of authority. <em>See United States v. Jerez, </em><span class="citation" data-id="9490090"><a href="/opinion/737426/united-states-v-lenin-m-jerez-and-carlos-m-solis/#692" aria-description="Citation for case: United States v. Lenin M. Jerez and Carlos M. Solis">108 F.3d 684, 692</a></span> (7th Cir.1997); <em>United States v. Tovar-Rico, </em><span class="citation" data-id="6935649"><a href="/opinion/7033317/united-states-v-tovar-rico/#1535" aria-description="Citation for case: United States v. Tovar-Rico">61 F.3d 1529, 1535-36</a></span> (11th Cir.1995); <em>United States v. Winsor, </em><span class="citation" data-id="9477657"><a href="/opinion/506186/united-states-v-steven-dale-winsor/#1572" aria-description="Citation for case: United States v. Steven Dale Winsor">846 F.2d 1569, 1572</a></span> (9th Cir.1988) (en banc). Further, we find no error in the district court’s determination that, under the totality of circumstances, Tilton did not voluntarily consent to the officers’ entry into the motel room.<footnotemark>2</footnotemark> Thus, the police officers’ action constituted an unconstitutional intrusion into that zone of privacy.<footnotemark>3</footnotemark></p>
<p id="b735-3"><page-number citation-index="1" label="667">*667</page-number>As an alternative basis for reversal, the government argues that either the good-faith or the inevitable-discovery exception to the exclusionary rule renders the evidence admissible despite the Fourth Amendment violation in gaining access to the motel room. The government contends that the evidence obtained in the searches of the motel room and Conner’s home should be admissible even if we find the warrant invalid because law enforcement officers reasonably relied on warrants issued by a neutral magistrate. <em>See United States v. Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. 897, 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3420" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405, 3420</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984). The rule in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>is based on the theory that where there has been no police illegality, there is no conduct the courts need to deter and therefore no basis to enforce the exclusionary rule. As the Supreme Court stated: “Penalizing the officer for the magistrate’s error, rather than his .own, cannot logically contribute to the deterrence of Fourth Amendment violations.” <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#921" aria-description="Citation for case: United States v. Leon">468 U.S. at 921</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#3419" aria-description="Citation for case: United States v. Leon">104 S.Ct. at 3419</a></span>. The ultimate question under Leon is whether the officers “had an objectively reasonable basis to believe they were complying with [applicable law] and the Fourth Amendment.” <em>United States v. Moore, </em><span class="citation" data-id="9482613"><a href="/opinion/577749/united-states-v-phillip-moore/#848" aria-description="Citation for case: United States v. Phillip Moore">956 F.2d 843, 848</a></span> (8th Cir.1992). In the context of investigatory stops, we have stated that suppression is unwarranted where pre-warrant police conduct was “close enough to the line of validity to make the officers’ belief in the validity of the warrant objectively reasonable.” <em>United States v. White, </em><span class="citation" data-id="9479752"><a href="/opinion/532988/united-states-v-bennie-ree-white/#1419" aria-description="Citation for case: United States v. Bennie Ree White">890 F.2d 1413, 1419</a></span> (8th Cir.1989); <em>United States v. Fletcher, </em><span class="citation" data-id="722623"><a href="/opinion/722623/united-states-v-michael-dale-fletcher/#51" aria-description="Citation for case: United States v. Michael Dale Fletcher">91 F.3d 48, 51</a></span> (8th Cir.1996). If, on the other hand, the officers’ pre-warrant conduct is “clearly illegal,” the good-faith exception does not apply. <em>United States v. O’Neal, </em><span class="citation" data-id="9486466"><a href="/opinion/663762/united-states-v-john-derek-oneal/" aria-description="Citation for case: United States v. John Derek O&#x27;Neal">17 F.3d 239</a></span>, 242-43 n. 6 (8th Cir.1994).</p>
<p id="b735-4">The district court concluded that the government could not invoke <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>in this case because “[n]o officer could in good faith believe, under the facts as they existed at the time, that the defendants consented to the officers’ visual or physical access to the motel room.” <em>United States v. Conner, </em><span class="citation" data-id="2098652"><a href="/opinion/2098652/united-states-v-conner/#853" aria-description="Citation for case: United States v. Conner">948 F.Supp. 821, 853</a></span> (N.D.Iowa 1996). Nor could the police reasonably believe that exigent circumstances justified the intrusion on Conner and Tilton’s reasonable expectation of privacy. <span class="citation" data-id="2098652"><a href="/opinion/2098652/united-states-v-conner/#854" aria-description="Citation for case: United States v. Conner"><em>Id. </em>at 854</a></span>. Sergeant Young stated that he planned only to talk to the occupants of Room 31 and that he lacked probable cause to arrest prior to viewing the contents of the room. In fact, none of the officers involved even knew to whom the room was rented. We agree with the district court that the exception in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>does not salvage the warrantless entry by police.</p>
<p id="b735-7">Finally, for the first time on appeal, the government advances the argument that even if the police had not commanded the defendants to open the door to the motel room, they inevitably would have discovered the evidence through independent search warrants. <em>See Nix v. Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#433" aria-description="Citation for case: Nix v. Williams">467 U.S. 431, 433</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#2504" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501, 2504</a></span>, <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span> (1984). Although we need not address an issue that was not raised below, <em>see United States v. Johnson, </em><span class="citation" data-id="9488478"><a href="/opinion/703196/united-states-v-anthony-philip-johnson-united-states-of-america-v-chico/#1126" aria-description="Citation for case: United States v. Anthony Philip Johnson, United States of...">64 F.3d 1120, 1126</a></span> (8th Cir.1995); <em>United States v. Chalmers, </em><span class="citation multiple-matches"><a href="/c/F.2d/800/737/">800 F.2d 737</a></span>, 738 (8th Cir.1986), the district court made factual findings that dispose of this claim and those factual findings are not clearly erroneous. To succeed under the inevitable-discovery exception to the exclusionary rule, the government must prove by a preponderance of the evidence: (1) that there was a reasonable probability that the evidence would have been discovered by lawful means in the absence of police misconduct, and (2) that the government was actively pursuing a substantial, alternative line of investigation at the time of the constitutional violation. <em>United States v. Wilson, </em><span class="citation" data-id="9413527"><a href="/opinion/6756/united-states-v-wilson/#1304" aria-description="Citation for case: United States v. Wilson">36 F.3d 1298, 1304</a></span> (5th Cir.1994). The district court concluded that there was no independent basis for admission of the evidence. Specifical<page-number citation-index="1" label="668">*668</page-number>ly, the court found that the officers would not have sought either search warrant but for their observation of what they believed to be the proceeds of the Uhlir burglary following their illegal entry into the motel room. <em>Conner, </em><span class="citation" data-id="2098652"><a href="/opinion/2098652/united-states-v-conner/#859" aria-description="Citation for case: United States v. Conner">948 F.Supp. at 859</a></span>. Given that finding and the fact that the government offers no concrete evidence that police explored any alternative investigatory approach, we find no basis to apply the inevitable-discovery exception to this case.</p>
<p id="b736-4">III.</p>
<p id="b736-5">Police officers entered appellees’ motel room in violation of the Fourth Amendment. The evidence obtained following that entry, including that which police seized pursuant to search warrants, was tainted by the illegal entry and the evidence was properly excluded over the government’s assertions of good faith and inevitable discovery. Therefore, we affirm the district court’s suppression order.</p>
<footnote label="2">
<p id="b734-7">. In fact, the district court's determination that the police entered Room 31 under color of authority is well supported by the record. Four police officers were positioned at or near the door. They knocked on the door longer and more vigorously than would an ordinary member of the public. The knocking was loud enough to awaken a guest in a nearby room and to cause another to open her door. Several minutes passed before Conner or Tilton responded to the knocks. ' Before Tilton opened the door, he looked out the window to assess the forces outside. Only after two of the officers had identified themselves as police and demanded him to "open up” did he concede to that demand.</p>
</footnote>
<footnote label="3">
<p id="b734-10">. Our analysis of the entry of the motel room under <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>necessarily rejects the government's argument that we should assess the police officers' command to open the door under a reasonableness standard. <em>See Terry v. Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span> (1968). The government asserts that the demand was part of a brief, investigatory questioning consistent with the Fourth Amendment and that the occupants of the room "control” the situation— they decide how far to open the door and what objects to leave in plain view during the questioning. This argument is as detached from real life as it is from established constitutional principles. Despite the four police officers outside the room and the two other officers in the general <page-number citation-index="1" label="667">*667</page-number>area, Conner and Tilton attempted without success to "control the nature of the encounter" by refusing to answer the door. Also, once inside the room, the officers would be entitled to make a sweep of the motel room to ensure their safety during questioning. Thus, it is disingenuous to assert that the defendants could have limited the officers' exposure to the room by opening the door just a crack. Finally, if the police could demand entry into a person's home or hotel room to investigate suspected criminal activity in situations where they lack a warrant or even probable cause to search or arrest, the Fourth Amendment rule would be swallowed by the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>exception.</p>
</footnote>
</opinion>
```

---
