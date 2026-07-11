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

## GROUP: content/cases/Alvarez v. City of Brownsville.md  (`case`, 5 assertions)

### content_page

```
---
title: Alvarez v. City of Brownsville
type: case
citation: "904 F.3d 382 (2018)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 5th Cir."
court_level: coa
circuit: ca5
year: 2018
date_decided: 2018-09-18
docket: 16-40772
authority_weight: "Binding in-circuit — 5th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4536189/george-alvarez-v-city-of-brownsville/"
  cluster_id: 4536189
  opinion_id: null
  identity_checked: true
lake:
  record_id: Alvarez v. City of Brownsville
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Key
related:
  - "[[Brady and Giglio]]"
  - "[[Brady v. Maryland]]"
  - "[[Giglio v. United States]]"
tags:
  - case
  - fourth-amendment
  - brady
  - due-process
  - guilty-plea
  - section-1983
  - municipal-liability
holding: "Brady is a trial right: a defendant who pleads guilty has no clearly established constitutional right to pre-plea disclosure of exculpatory evidence, so the en banc Fifth Circuit declined to recognize such a right and reversed a § 1983 municipal-liability judgment premised on it."
---

# Alvarez v. City of Brownsville

*904 F.3d 382 (5th Cir. 2018)* (en banc) (No. 16-40772) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4536189 → lead opinion 4313442 (904 F.3d 382, en banc, decided 2018-09-18); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
George Alvarez pleaded guilty to assaulting a public servant based on a booking-area altercation. Years later, after surveillance video of the incident surfaced, Texas courts declared him "actually innocent" and [[Reading and Citing Cases#vacated|vacated]] the conviction. Alvarez sued the City of Brownsville under § 1983, alleging that the police department's practice of not disclosing [[Brady and Giglio|exculpatory]] video violated *[[Brady v. Maryland|Brady]]*. A jury awarded him $2.3 million; a panel reversed, and the Fifth Circuit reheard the case [[Reading and Citing Cases#en-banc|en banc]].

## Issue
Whether a criminal defendant has a constitutional right, enforceable under § 1983, to the disclosure of material [[Brady and Giglio|exculpatory]] evidence before entering a guilty plea.

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court held that Alvarez's *[[Brady v. Maryland|Brady]]* claim failed and reaffirmed circuit precedent (*United States v. Conroy*) that there is no such pre-plea right: "This court also declines the invitation to disturb its precedent concerning a defendant's constitutional right to *Brady* material prior to entering a guilty plea." — 904 F.3d at 389. Because *[[Brady v. Maryland|Brady]]* is grounded in the right to a fair *trial*, its disclosure obligation does not attach to the plea-bargaining process.

## Application
Without an underlying constitutional violation, there could be no municipal liability: a city cannot be deliberately indifferent to a right the circuit has held does not exist. The court declined the invitation to extend *[[Brady v. Maryland|Brady]]* to the guilty-plea context, noting a split among the circuits but adhering to its own rule, and therefore reversed the judgment against the City.

## Conclusion
The Fifth Circuit **reversed** and rendered judgment of dismissal for the City of Brownsville.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Alvarez* anchors the Fifth Circuit's position that *[[Brady v. Maryland|Brady]]* is a trial right that does not guarantee [[Brady and Giglio|exculpatory]] disclosure before a guilty plea — a question on which the Supreme Court (in *[[United States v. Ruiz]]*, on impeachment evidence) and the circuits remain divided.

## Appears on
- [[Brady and Giglio]] — *Key*

## Sources
- [*Alvarez v. City of Brownsville*, 904 F.3d 382 (5th Cir. 2018) (en banc)](https://www.courtlistener.com/opinion/4536189/george-alvarez-v-city-of-brownsville/) — pinpoint: 389 (majority; en banc); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "80f0fa47bc9851c0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "904 F.3d 382 (2018)", "court": "U.S. Court of Appeals, 5th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Alvarez v. City of Brownsville", "year": "2018"}}
{"assertion_id": "91d8ffac63160461", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Brady is a trial right: a defendant who pleads guilty has no clearly established constitutional right to pre-plea disclosure of exculpatory evidence, so the en banc Fifth Circuit declined to recognize such a right and reversed a § 1983 municipal-liability judgment premised on it.", "title": "Alvarez v. City of Brownsville"}}
{"assertion_id": "b87dc73729ac34d1", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key", "title": "Alvarez v. City of Brownsville"}}
{"assertion_id": "00f4bb83a29d42f7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "Alvarez v. City of Brownsville"}}
{"assertion_id": "0b068b103148529c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Alvarez v. City of Brownsville", "varies_by_point": "false"}}
```

### lake record — Alvarez v. City of Brownsville

```json
{
  "schema_version": "s2.v1",
  "record_id": "Alvarez v. City of Brownsville",
  "status": "under_review",
  "identity": {
    "case_name": "George Alvarez v. City of Brownsville",
    "case_name_short": "",
    "case_name_full": "George ALVAREZ, Plaintiff-Appellee, v. the CITY OF BROWNSVILLE, Defendant-Appellant.",
    "input_case_name": "Alvarez v. City of Brownsville",
    "court": "U.S. Court of Appeals, 5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2018-09-18",
    "year": 2018,
    "docket": "16-40772",
    "cluster_id": 4536189,
    "lead_opinion_id": 4313442,
    "sibling_ids": [],
    "absolute_url": "/opinion/4536189/george-alvarez-v-city-of-brownsville/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "904 F.3d 382",
      "volume": "904",
      "reporter": "F.3d",
      "page": "382",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "904 F.3d 382",
        "volume": "904",
        "reporter": "F.3d",
        "page": "382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "904 F.3d 382",
    "official_selection": {
      "court_class": "coa",
      "selected": "904 F.3d 382",
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
    "date_created": "2026-07-07T13:26:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:26:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:26:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "alvarez-v-city-of-brownsville--4536189",
      "to_record_id": "Alvarez v. City of Brownsville",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Alvarez v. City of Brownsville (truncated)

```
     Case: 16-40772       Document: 00514646077         Page: 1     Date Filed: 09/18/2018




           IN THE UNITED STATES COURT OF APPEALS
                    FOR THE FIFTH CIRCUIT

                                                                   United States Court of Appeals

                                       No. 16-40772
                                                                            Fifth Circuit

                                                                          FILED
                                                                  September 18, 2018

GEORGE ALVAREZ,                                                      Lyle W. Cayce
                                                                          Clerk
              Plaintiff-Appellee,
v.

THE CITY OF BROWNSVILLE,

              Defendant-Appellant.




                   Appeal from the United States District Court
                        for the Southern District of Texas


Before STEWART, Chief Judge, and JOLLY, JONES, SMITH, WIENER,
DENNIS, CLEMENT, OWEN, ELROD, SOUTHWICK, HAYNES, GRAVES,
HIGGINSON, COSTA, WILLETT, and HO, Circuit Judges. *

CARL E. STEWART, Chief Judge, joined by JOLLY, JONES, SMITH,
WIENER, CLEMENT, OWEN, ELROD, SOUTHWICK, HAYNES,
HIGGINSON, WILLETT, and HO, Circuit Judges: ∗∗




       * Judge Prado was on the court at the time that this en banc case was submitted and
argued but did not participate in the consideration of the decision. Judge Duncan, Judge
Engelhardt and Judge Oldham joined the court after this case was submitted and did not
participate in the decision.
       ∗∗
          Judge Haynes and Judge Willett concur in Sections I, II.A., and III., and they would
not reach the issue in Section II.B.
    Case: 16-40772     Document: 00514646077      Page: 2   Date Filed: 09/18/2018



                                  No. 16-40772
      This case was reheard en banc after the Appellee, George Alvarez, had
his $2.3 million judgment reversed and his claims against the City of
Brownsville dismissed by a panel of this court. The en banc court has carefully
considered two important questions as to the merits of this case: (1) whether
the City of Brownsville should have been subjected to municipal liability for
Alvarez’s claim under Brady v. Maryland, 373 U.S. 83 (1963); and (2) whether
Alvarez was precluded from asserting his constitutional Brady claim for his 42
U.S.C. § 1983 action against the City of Brownsville because he pled guilty.
For the reasons set forth below, we REVERSE the district court’s judgment,
and RENDER judgment in favor of the City of Brownsville. Alvarez’s action
against the City of Brownsville is DISMISSED with prejudice.
      I.     FACTUAL BACKGROUND AND PROCEDURAL HISTORY
   A. Factual Background
      1.   The Incident Between Alvarez and Officer Arias at the Jail
      On November 27, 2005, Alvarez, a then-seventeen year old ninth grade
special education student, was arrested by the Brownsville Police Department
and taken to a detention center in Brownsville, Texas on suspicion of public
intoxication and burglary of a motor vehicle. After being placed in one of the
holding cells, Alvarez attempted to use a telephone located in the cell. Initially,
Alvarez was able to place a call but the phone eventually stopped working.
Alvarez then banged the phone’s handset against the phone’s switch hook
mounted on the wall, and made an obscene gesture towards a camera. Because
Alvarez became somewhat disruptive, officers removed Alvarez from his cell
and attempted to transfer him to a padded cell to calm down. To move Alvarez
to the padded cell, the officers had to walk him across the jail’s central lobby
booking area.


                                        2
    Case: 16-40772      Document: 00514646077     Page: 3   Date Filed: 09/18/2018



                                   No. 16-40772
         After reaching the booking area, Alvarez engaged in a conversation with
a group of officers. Alvarez primarily spoke to Officer Jesus Arias who took the
lead in trying to direct Alvarez to the padded cell. As the conversation
continued, Alvarez was reluctant to move towards the padded cell and obey
Officer Arias’s instructions to walk towards the cell. When recalling the
conversation with Officer Arias, Alvarez indicated, “I understand I wasn’t
compliant.”
         A scuffle between Alvarez and Officer Arias soon ensued. The altercation
began when Officer Arias grabbed Alvarez’s left arm and maneuvered Alvarez
to the ground. Officer Arias then placed Alvarez in a choke hold and eventually
a head lock. Officers assisting Officer Arias subdued Alvarez by shackling
Alvarez’s legs and handcuffing him. Throughout the struggle, Alvarez
squirmed and flailed his arms. Alvarez, handcuffed and legs shackled, was
then carried and placed in the padded holding cell. All of the events that took
place at the jail before, during, and after Alvarez’s incident with Officer Arias
were captured on video.
         2.  Investigations Conducted by the Brownsville Police Department
         The Brownsville Police Department utilizes separate investigative
tracks for internal disciplinary investigations of its officers and alleged crimes
committed by detainees at the jail. An internal administrative investigation
was conducted to determine if Officer Arias violated the Brownsville Police
Department’s use of force policy during the altercation with Alvarez.
Additionally, a criminal investigation was conducted by the Brownsville Police
Department to determine if there was probable cause for recommending that
the district attorney’s office criminally charge Alvarez for assaulting Officer
Arias.


                                         3
    Case: 16-40772     Document: 00514646077       Page: 4   Date Filed: 09/18/2018



                                   No. 16-40772
      Generally, the Brownsville Police Department’s internal administrative
affairs division does not share information with the criminal investigation
division. If information is to be shared between the internal administrative
affairs division and the criminal investigation division, Police Chief Carlos
Garcia is usually the individual who authorizes the exchange. However,
Sergeant David Infante, the jail supervisor who downloaded the videos of the
incident for the internal administrative investigation of Officer Arias, stated
that “if something would have been asked of me by the criminal investigation,
I would have submitted it.” Police Chief Garcia further added that Sergeant
Infante should have provided the videos of the incident to the criminal
investigation division if he knew criminal charges were being brought against
Alvarez. Commander Roberto Avitia, also a supervisor of Sergeant Infante,
similarly stated that Sergeant Infante should have disclosed the videos to the
criminal investigation division.
      For the internal investigation, Sergeant Infante evaluated the videos
and Officer Arias’s report of the incident. Four different videos were reviewed:
(1) a video of Alvarez in the initial holding cell that he was placed in; (2) a video
of the officers at the central command post in the detention center before,
during, and after the incident; (3) a video of the altercation between Alvarez
and Officer Arias that occurred in the lobby booking area; and (4) a video of
Alvarez in the padded cell after he was transported. After conducting the
investigation, Sergeant Infante came to the conclusion that Officer Arias used
proper force and that no further action should be taken.
      Two days after the incident between Alvarez and Officer Arias, on
November 29, 2005, Sergeant Infante sent a memorandum to Police Chief
Garcia reiterating his recommendation that proper force was used. On
December 8, 2005, another supervisor of Sergeant Infante, Commander
                                         4
     Case: 16-40772      Document: 00514646077         Page: 5    Date Filed: 09/18/2018



                                      No. 16-40772
Ramiro Rodriguez, reviewed Sergeant Infante’s report and the video
recordings, and submitted a report to Police Chief Garcia recommending
closure of the internal administrative investigation since Officer Arias’s
actions were in compliance with Brownsville Police Department regulations.
       Even though the reports and recommendations were stamped as
received on December 8, 2005 by Police Chief Garcia’s office, Police Chief
Garcia did not review the reports. The materials for the internal investigation,
including the videos, were never passed on to an internal affairs unit for a
formal disciplinary investigation of Officer Arias or to the criminal
investigation division of the Brownsville Police Department.
       The criminal investigation division reviewed the incident after the
internal administrative review was conducted. The criminal investigation
began on November 27, 2005, with Sergeant Jim Brown preparing and filing
an offense report of the incident that occurred between Alvarez and Officer
Arias. Sergeant Brown was the patrol supervisor responsible for addressing
issues that arose at the jail when the incident occurred. 1 Sergeant Brown’s
report stated Alvarez allegedly assaulted Officer Arias but did not mention
that there were any video recordings of the incident. Criminal investigator
Officer Rene Carrejo was subsequently assigned to review Officer Arias’s
complaint that Alvarez assaulted him by grabbing his throat and his right
inner thigh. Officer Carrejo never requested or inquired about the possible
existence of a video recording of the incident. Lieutenant Henry Etheridge, the
head of the internal affairs division of the Brownsville Police Department at


       1  Although Sergeant Infante was officially the jail supervisor, the supervision
responsibilities of the jail passed to Sergeant Brown as one of the patrol supervisors after
5:00 p.m. Because the incident between Alvarez and Officer Arias occurred around 9:00 p.m.,
when Sergeant Infante was off duty, Sergeant Brown was responsible for supervising the jail
at this time.
                                             5
    Case: 16-40772      Document: 00514646077     Page: 6   Date Filed: 09/18/2018



                                   No. 16-40772
the time of the administrative review, opined that the criminal investigation
division did not conduct a proper investigation because it failed to collect all
evidence. Lieutenant Etheridge further noted that, “[i]f I knew that [the
criminal investigation division] wasn’t conducting proper investigations in
regards to collecting that video, by all means, I would have taken corrective
action to . . . get that video in their hands.”
      3.   Alvarez’s Guilty Plea and Imprisonment
      The criminal investigation division subsequently alerted the district
attorney’s office of the incident and Alvarez was charged with assault on a
public servant, a felony offense in Texas. In January 2006, a grand jury
returned an indictment charging Alvarez with the assault. During discovery,
Alvarez’s attorney reviewed the prosecution’s case file that did not contain the
videos of the incident. In March 2006, Alvarez pled guilty to assault on a public
servant. In May 2006, Alvarez was given a suspended sentence of eight years
of imprisonment and ten years of community supervision. As a condition of the
community supervision, the court imposed “a term of confinement and
treatment in a substance abuse felony punishment facility . . . for not less than
90 days or more than 12 months as a condition of probation.” In November
2006, after Alvarez failed to complete the treatment program, the state
revoked the suspension of Alvarez’s sentence and remanded Alvarez to prison
for the remainder of his eight-year sentence.
      4.   The Uncovering of the Video Recordings of the Incident
      Approximately four years after Alvarez began to serve his prison
sentence, the videos of Alvarez’s incident with Officer Arias surfaced during
discovery for an unrelated § 1983 case. After the discovery of the videos,
Alvarez filed an application for a writ of habeas corpus in Texas state court,
claiming that the Brownsville Police Department had withheld the videos in

                                          6
    Case: 16-40772    Document: 00514646077      Page: 7    Date Filed: 09/18/2018



                                 No. 16-40772
violation of Brady. In October 2010, after the state district court recommended
that the writ of habeas corpus be granted and that Alvarez be given a new trial,
the Texas Court of Criminal Appeals concluded that Alvarez was “actually
innocent” of committing the assault. Alvarez’s assault conviction was then set
aside and all charges against Alvarez were later dismissed.
   B. Procedural History
      Several months after being declared “actually innocent,” in April 2011,
Alvarez sued the City of Brownsville, Officer Arias, and other individuals from
the Brownsville Police Department, asserting various claims under § 1983,
which included nondisclosure of exculpatory evidence in violation of Brady. In
August 2012, the City of Brownsville, Officer Arias, and the other defendants
filed a motion for summary judgment arguing that Alvarez’s claims should be
dismissed. Adopting the magistrate judge’s report and recommendation, the
district court denied the defendants’ motion for summary judgment as to: (1)
the Brady claim against the City of Brownsville for nondisclosure of
exculpatory evidence; and (2) a fabrication of evidence claim brought against
Officer Arias in his individual capacity. The district court granted the
defendants’ motion for summary judgment as to all other claims. The
fabrication claim against Officer Arias was later dismissed after Alvarez and
Officer Arias filed a voluntary stipulation of dismissal.
      In January 2014, Alvarez and the City of Brownsville, as the only
remaining parties, filed cross motions for summary judgment addressing
whether: (1) a Brownsville Police Department policy of nondisclosure existed;
(2) the Brownsville Police Department’s failure to disclose the videos
constituted a Brady violation; and (3) a Brownsville Police Department policy
caused the Brady violation. The district court subsequently granted Alvarez’s
motion for summary judgment concluding that there was a Brady violation as
                                        7
    Case: 16-40772     Document: 00514646077    Page: 8   Date Filed: 09/18/2018



                                 No. 16-40772
a matter of law, and Alvarez established “all substantive elements of a § 1983
municipal liability claim against the City of Brownsville.”
      The district court held a jury trial to determine whether Alvarez was
entitled to monetary damages for the Brady violation. Following a two-day jury
trial, the jury awarded Alvarez $2,000,000 in compensatory damages. The
parties agreed to attorneys’ fees of $300,000 and the court entered final
judgment in favor of Alvarez for $2,300,000. The City of Brownsville filed post-
trial motions, which were denied by the district court. The City of Brownsville
timely appealed.
      A panel of this court reversed the $2,300,000 judgment awarded to
Alvarez and dismissed Alvarez’s action against the City of Brownsville. Alvarez
v. City of Brownsville, 860 F.3d 799, 803 (5th Cir. 2017), reh’g en banc granted,
874 F.3d 898 (5th Cir. 2017). The panel opinion held that by entering a guilty
plea Alvarez waived the right to assert the Brady claim foundational to his §
1983 action. The panel opinion was withdrawn in light of en banc rehearing of
this case. After supplemental briefing and oral argument to the en banc court,
we reverse the district court and render judgment of dismissal in favor of the
City of Brownsville.
                                II.   DISCUSSION
      Alvarez’s Brady claim should have been dismissed as a matter of law on
summary judgment because the City of Brownsville should not have been
subjected to municipal liability for Alvarez’s § 1983 claim. This court also
declines the invitation to disturb its precedent concerning a defendant’s
constitutional right to Brady material prior to entering a guilty plea.
   A. Municipal Liability
      Alvarez argues that the City of Brownsville, through its police
department, had an unwritten, customary policy of not disclosing exculpatory
                                       8
    Case: 16-40772     Document: 00514646077      Page: 9   Date Filed: 09/18/2018



                                  No. 16-40772
evidence obtained in the course of internal administrative investigations—a
policy that caused Alvarez’s constitutional violation. Alternatively, Alvarez
asserts that making Police Chief Garcia the sole decision-maker related to the
sharing of information from internal administrative matters created the high
possibility of a constitutional violation. Because of Police Chief Garcia’s
oversight, Alvarez asserts that the City of Brownsville should be held liable as
a municipality. This court is not persuaded by Alvarez’s arguments.
      Summary judgment rulings are subject to de novo review. Aldous v.
Darwin Nat’l Assurance Co., 851 F.3d 473, 477 (5th Cir. 2017), vacated in part
by 889 F.3d 798 (5th Cir. 2018). Summary judgment is appropriate “if the
movant shows that there is no genuine dispute as to any material fact and the
movant is entitled to judgment as a matter of law.” Fed. R. Civ. P. 56(a). “‘A
complete failure of proof concerning an essential element of the nonmoving
party’s case necessarily renders all other facts immaterial’ and ‘mandates the
entry of summary judgment’ for the moving party.” United States ex rel.
Farmer v. City of Houston, 523 F.3d 333, 337 (5th Cir. 2008) (quoting Celotex
Corp. v. Catrett, 477 U.S. 317, 322–23 (1986)). “We resolve factual
controversies in favor of the nonmoving party, but only when there is an actual
controversy, that is, when both parties have submitted evidence of
contradictory facts.” State Farm Fire & Casualty Co. v. Flowers, 854 F.3d 842,
844 (5th Cir. 2017) (quoting Little v. Liquid Air Corp., 37 F.3d 1068, 1075 (5th
Cir. 1994)).
      Three essential elements must be established for a municipality to face
§ 1983 liability. There must be: (1) a policymaker; (2) an official policy; and (3)
a violation of a constitutional right whose “moving force” is the policy or
custom. Piotrowski v. City of Houston, 237 F.3d 567, 578 (5th Cir. 2001) (citing
Monell v. Dep’t of Soc. Servs., 436 U.S. 658, 694 (1978)). An official policy
                                        9
    Case: 16-40772     Document: 00514646077      Page: 10    Date Filed: 09/18/2018



                                   No. 16-40772
“usually exists in the form of written policy statements, ordinances, or
regulations, but may also arise in the form of a widespread practice that is so
common and well-settled as to constitute a custom that fairly represents
municipal policy.” James v. Harris County, 577 F.3d 612, 617 (5th Cir. 2009)
(quoting Piotrowski, 237 F.3d at 579) (quotation marks omitted).
      To establish that the City of Brownsville is liable as a municipality, a
policy must have been the “moving force” behind Alvarez’s constitutional
violation. See Piotrowski, 237 F.3d at 580 (quoting Monell, 436 U.S. at 694).
Stated differently, Alvarez “must show direct causation, i.e., that there was ‘a
direct causal link’ between the policy and the violation.” See James, 577 F.3d
at 617 (quoting Piotrowski, 237 F.3d at 580). Additionally, Alvarez must
demonstrate that the policy was implemented with “deliberate indifference” to
the “known or obvious consequences” that constitutional violations would
result. See Bd. of Cty. Comm’rs of Bryan Cty. v. Brown, 520 U.S. 397, 407
(1997). To base deliberate indifference on a single incident, “it should have
been apparent to the policymaker that a constitutional violation was the highly
predictable consequence of a particular policy.” Burge v. St. Tammany Par.,
336 F.3d 363, 373 (5th Cir. 2003). The causal link “moving force” requirement
and the degree of culpability “deliberate indifference” requirement must not be
diluted, for “where a court fails to adhere to rigorous requirements of
culpability and causation, municipal liability collapses into respondeat
superior liability.” Snyder v. Trepagnier, 142 F.3d 791, 796 (5th Cir. 1998)
(quoting Brown, 520 U.S. at 415).
      Assuming that Police Chief Garcia is a policymaker and that the practice
of not freely sharing information from the internal administrative
investigations with the criminal investigation division constitutes a policy,
Alvarez’s theory of liability falls short in two respects: (1) there is not a “direct
                                         10
    Case: 16-40772    Document: 00514646077       Page: 11   Date Filed: 09/18/2018



                                  No. 16-40772
causal link between the policy and the violation,” and (2) there was no
“deliberate indifference” shown. See Valle v. City of Hous., 613 F.3d 536, 542
(5th Cir. 2010); James, 577 F.3d at 617 (quoting Piotrowski, 237 F.3d at 580).
      First, there is not “a direct causal link between the policy and the
violation.” See James, 577 F.3d at 617 (quoting Piotrowski, 237 F.3d at 580).
When questioned about whether he could turn materials over to the criminal
investigation division, Sergeant Infante stated that “if something would have
been asked of me by the criminal investigation, I would have submitted it.”
Moreover, Police Chief Garcia and Commander Avitia both stated that
Sergeant Infante should have disclosed the videos of the incident if he was
aware of the criminal investigation against Alvarez. Commander Avitia
further stated that “[v]ideos are videos. They should be able to be available to
either one of the investigations. . . . They’re available for both investigations.”
The criminal investigator, Officer Carrejo, also neglected to request or inquire
about any video recordings of the incident despite knowing about the presence
of cameras in the jail. Lieutenant Etheridge stated that the criminal
investigation division did not conduct a proper investigation because of its
failure to collect all of the evidence. Lieutenant Etheridge further noted that,
“[i]f I knew that [the criminal investigation division] wasn’t conducting proper
investigations in regards to collecting that video, by all means, I would have
taken corrective action to . . . get that video in their hands.”
      This series of interconnected errors within the Brownsville Police
Department that involved individual officers was separate from the general
policy of non-disclosure of information from the internal administrative
investigations. The general policy of non-disclosure was not a direct cause of
Alvarez’s injury. See Fraire v. City of Arlington, 957 F.2d 1268, 1281 (5th Cir.
1992) (“To form the basis of liability under § 1983, a municipal policy must be
                                        11
    Case: 16-40772    Document: 00514646077     Page: 12   Date Filed: 09/18/2018



                                 No. 16-40772
affirmatively linked to the constitutional violation and be the moving force
behind it.”).
      Second, this general policy of non-disclosure was not implemented with
“deliberate indifference.” To show deliberate indifference based on a single
incident, there must be evidence that shows that it should have been apparent
or obvious to the policymaker that a constitutional violation was the “highly
predictable consequence” of the particular policy. See Burge, 336 F.3d at 373;
Brown v. Bryan County, 219 F.3d 450, 461 (5th Cir. 2000). While it was
established that information from internal administrative investigations is
generally not shared, Sergeant Infante, Commander Avitia, Lieutenant
Etheridge, and Police Chief Garcia still understood that this policy did not
prohibit them from disclosing video recordings. Moreover, if Officer Carrejo
requested or inquired about the existence of any videos of the incident, the
videos would have been turned over. Because of the understanding throughout
the police department that even with the policy that possibly exculpatory
evidence such as the videos could be disclosed, it was by no means “apparent”
that a constitutional violation was a “highly predictable consequence” of the
general policy of non-disclosure. See Burge, 336 F.3d at 373. Put another way,
it can not be “apparent” that a constitutional violation is a “highly predictable
consequence” if no impression is created from the policy that the evidence
central to the alleged violation has to be withheld. Accordingly, there was no
“deliberate indifference” shown in implementing this policy. See id. (citing
Brown, 219 F.3d at 461).
      Even if this court adopts Alvarez’s alternative theory that the “policy”
was Police Chief Garcia being vested with the sole authority to review the
internal administrative investigation reports, there is no showing that this
policy was adopted or implemented with deliberate indifference. When
                                       12
   Case: 16-40772       Document: 00514646077    Page: 13     Date Filed: 09/18/2018



                                  No. 16-40772
advancing this theory, Alvarez lodges two different concepts for how deliberate
indifference was shown. First, Alvarez asserts that the policy of allowing Police
Chief Garcia to be the sole decision maker relating to the internal
investigations was deliberately indifferent because there was no safety net to
catch Police Chief Garcia’s mistakes. Second, Alvarez avers that Police Chief
Garcia implemented this policy with deliberate indifference because he
overlooked internal administrative reports, knowing that his error would
probably result in the violation of an individual’s constitutional rights.
      Both of Alvarez’s arguments are unavailing. Placing the final decision
making authority in the hands of one individual, even if it makes an error more
likely, does not by itself establish deliberate indifference. “Deliberate
indifference is a degree of culpability beyond mere negligence or even gross
negligence; it must amount to an intentional choice, not merely an
unintentionally negligent oversight.” James, 577 F.3d at 617–18 (quoting
Rhyne v. Henderson County, 973 F.2d 386, 392 (5th Cir. 1992) (quotation marks
omitted). No evidence from the record indicates that Police Chief Garcia’s
actions should be characterized as anything more than negligent oversight.
Moreover, Alvarez points to no case from any circuit that premises § 1983
municipal   liability   on   a   policymaker’s   deliberate    indifference   to   a
constitutional right that a circuit court has expressly held does not exist—e.g.,
the defendant’s right to be presented with Brady material before entering a
guilty plea. No deliberate indifference was shown to establish municipal
liability under this alternative theory proposed by Alvarez.
      In conclusion, the City of Brownsville should not have been liable as a
matter of law for Alvarez’s § 1983 action.




                                        13
   Case: 16-40772     Document: 00514646077     Page: 14   Date Filed: 09/18/2018



                                 No. 16-40772
   B. Extension of the Brady right to the Plea Bargaining Process
      Alvarez additionally argued to the en banc court that his guilty plea did
not preclude him from asserting a viable Brady claim for his § 1983 action.
Prior to this court granting Alvarez’s petition for rehearing en banc, settled
precedent in this circuit held that there was no constitutional right to Brady
material prior to a guilty plea. See United States v. Conroy, 567 F.3d 174, 178–
79 (5th Cir. 2009) (citing Matthew v. Johnson, 201 F.3d 353, 361–62 (5th Cir.
2000)). Alvarez argues that under Brady the videos of the incident between
him and Officer Arias constituted exculpatory evidence that he was
constitutionally entitled to before the entry of his guilty plea. See 373 U.S. at
87. This court declines the invitation to uproot its precedent.
      In United States v. Ruiz, the Supreme Court held that “the Constitution
does not require the Government to disclose material impeachment evidence
prior to entering a plea agreement with a criminal defendant.” 536 U.S. 622,
633 (2002). The Supreme Court stated that impeachment information was not
“critical information of which the defendant must always be aware prior to
pleading guilty.” Id. at 630. The Supreme Court, however, did not explicitly
address whether the withholding of exculpatory evidence during the pretrial
plea bargaining process would violate a defendant’s constitutional rights. See
id. at 630–33.
      In Conroy, this court addressed the scope of a defendant’s constitutional
entitlement to Brady material before he enters a guilty plea. 567 F.3d at 179.
Unequivocally, the court rejected the defendant’s argument that Ruiz states
that impeachment and exculpatory evidence should be treated differently, and
that exculpatory evidence must be turned over before the entry of a guilty plea.
Id. This court stated, “Ruiz never makes such a distinction nor can this
proposition be implied from its discussion. Accordingly, we conclude that [the
                                       14
    Case: 16-40772     Document: 00514646077      Page: 15    Date Filed: 09/18/2018



                                   No. 16-40772
defendant’s] guilty plea precludes her from claiming that the government’s
failure to disclose . . . was a Brady violation.” Id.
      The First, Second, and Fourth Circuits also seem to have doubts about a
defendant’s constitutional entitlement to exculpatory Brady material before
entering a guilty plea. In United States v. Mathur, the First Circuit explained
that, “[t]he animating principle of Brady is the avoidance of an unfair trial. It
is, therefore, universally acknowledged that the right memorialized in Brady
is a trial right.” 624 F.3d 498, 506–07 (1st Cir. 2010) (internal citation omitted).
Extending Brady to pretrial plea negotiations was characterized as “new
ground,” a “novel approach,” and an “unprecedented expansion of Brady.” Id.
at 507. The First Circuit noted that “Ruiz teaches that Brady does not protect
against the possible prejudice that may ensue from the loss of an opportunity
to plea-bargain with complete knowledge of all relevant facts.” Id. “[W]hen a
defendant chooses to admit his guilt, Brady concerns subside.” Id. (“The Brady
rule’s focus on protecting the integrity of trials suggests that where no trial is
to occur, there may be no constitutional violation.” (quoting Matthew, 201 F.3d
at 361)).
      Additionally, the Second Circuit in Friedman v. Rehal stated the
“Supreme Court has consistently treated exculpatory and impeachment
evidence in the same way for the purpose of defining the obligation of a
prosecutor to provide Brady material prior to trial, and the reasoning
underlying Ruiz could support a similar ruling for a prosecutor’s obligations
prior to a guilty plea.” 618 F.3d 142, 154 (2d Cir. 2010) (internal citation
omitted).
      Likewise, the Fourth Circuit in United States v. Moussaoui emphasized
that “[t]he Brady right . . . is a trial right” that “exists to preserve the fairness
of a trial verdict and to minimize the chance that an innocent person would be
                                         15
   Case: 16-40772     Document: 00514646077      Page: 16   Date Filed: 09/18/2018



                                  No. 16-40772
found guilty.” 591 F.3d 263, 285 (4th Cir. 2010) (emphasis in original). The
Fourth Circuit went on citing the Fifth Circuit’s Matthew and Orman opinions,
stating “[w]hen a defendant pleads guilty, those concerns are almost
completely eliminated because his guilt is admitted.” Id. (citing Orman v. Cain,
228 F.3d 616, 617 (5th Cir. 2000); Matthew, 201 F.3d at 361). After
acknowledging the circuit split for whether the Brady right extended to the
guilty plea context, the Fourth Circuit did not decide the issue. Id. at 286.
      The Seventh, Ninth, and Tenth Circuits, however, recognized the
possible distinction noted by the Supreme Court in Ruiz between impeachment
and exculpatory evidence in the guilty plea context. In McCann v.
Mangialardi, the Seventh Circuit stated that “Ruiz indicates a significant
distinction between impeachment information and exculpatory evidence of
actual innocence.” 337 F.3d 782, 788 (7th Cir. 2003). The Seventh Circuit went
on to say, “[g]iven this distinction, it is highly likely that the Supreme Court
would find a violation of the Due Process Clause if prosecutors or other
relevant government actors have knowledge of a criminal defendant’s factual
innocence but fail to disclose such information to a defendant before he enters
into a guilty plea.” Id. In the next line, the court explained that “[w]e need not
resolve this question” because the plaintiff did not present evidence that the
defendant was aware of the potential exculpatory evidence. Id.
      In United States v. Ohiri, the defendant contended that the government
committed Brady violations by failing to disclose exculpatory evidence prior to
his decision to plead guilty. 133 F. App’x 555, 556 (10th Cir. 2005)
(unpublished). The Tenth Circuit explained that the “government should have
disclosed all known exculpatory information at least by that point in the
proceedings” prior to the defendant’s guilty plea entered on the first day of jury
selection. Id. at 562. Notably, “the unusual circumstances presented” by the
                                       16
   Case: 16-40772     Document: 00514646077     Page: 17   Date Filed: 09/18/2018



                                 No. 16-40772
defendant’s acceptance of an “eleventh-hour plea agreement” on the day the
defendant was set to go to trial was highlighted in the court’s reasoning. See
Ohiri, 133 F. App’x at 562. The Tenth Circuit emphasized that, unlike Ruiz,
the evidence the prosecution withheld from the defendant was alleged to be
exculpatory and not just impeachment evidence. Id. The court concluded by
stating that “the Supreme Court [in Ruiz] did not imply that the government
may avoid the consequence of a Brady violation if the defendant accepts an
eleventh-hour plea agreement while ignorant of withheld exculpatory evidence
in the government’s possession.” Id.
      Similarly, the Ninth Circuit alluded to possibly allowing a defendant to
assert a Brady violation after pleading guilty. See Smith v. Baldwin, 510 F.3d
1127, 1148 (9th Cir. 2007) (en banc). When the Ninth Circuit referred to the
defendant’s ability to assert a Brady violation after pleading guilty, the court
cited to a case predating Ruiz for the proposition that the defendant could still
assert a viable Brady claim even though he pled guilty. See id. (citing Sanchez
v. United States, 50 F.3d 1148, 1454 (9th Cir. 1995)).
      In sum, case law from the Supreme Court, this circuit, and other circuits
does not affirmatively establish that a constitutional violation occurs when
Brady material is not shared during the plea bargaining process. The en banc
court will not disturb this circuit’s settled precedent and abstains from
expanding the Brady right to the pretrial plea bargaining context for Alvarez.


                             III. CONCLUSION
      For the foregoing reasons, we REVERSE the district court’s judgment,
and RENDER judgment in favor of the City of Brownsville. Alvarez’s action
against the City of Brownsville is DISMISSED with prejudice.


                                       17
    Case: 16-40772     Document: 00514646077      Page: 18    Date Filed: 09/18/2018



                                   No. 16-40772
EDITH H. JONES, Circuit Judge, joined by SMITH and HO, Circuit Judges,
concurring:

      I am pleased to join Chief Judge Stewart’s opinion for the court, with
which I fully agree. The genesis of this case is, however, troubling, and worth
noting. It is an unsavory vehicle in which to be discussing significant theories
of law.
      How Alvarez 1 obtained his habeas relief in the state appellate court,
using his then-attorney Lucio, who later became a co-defendant in a federal
RICO and bribery prosecution against then-Cameron County DA Villalobos, is
more than suspicious. The state courts were presented a redacted video of the
encounter between Alvarez and Officer Arias, which omitted a crucial 30+
seconds leading up to their tussle. In that period of time, it was evident that
Alvarez was arguing with and resisting the officers’ instructions to move from
one cell into another. Unredacted, the video portrays a much more complex
picture of events than the “self defense” theory propounded by attorney Lucio.
Lucio also offered the supporting testimony of Alvarez’s former attorney, de la
Fuente, an unindicted co-conspirator in the bribery case. In the state habeas
court, the DA’s office, oddly, never questioned the video, immediately agreed
to a new trial, and apparently offered an agreed set of findings and conclusions.
That court granted only a new trial.          When Lucio appealed to the state
appellate court on his “actual innocence” theory—which is supportable only if
one sees no more than the redacted video—the DA filed no response. After the
appellate court remanded, the DA quickly dismissed charges.               One may




      1  I have no knowledge whether Alvarez had any information about the attorneys’
deeds in his case.
                                         18
   Case: 16-40772     Document: 00514646077     Page: 19    Date Filed: 09/18/2018



                                 No. 16-40772
surmise, as Gilbert & Sullivan wrote in Trial by Jury, Alvarez’s release “was
managed by a job, and a good job too.”
      For present purposes, the point is that without having been “exonerated”
by the state courts, Alvarez could not pursue his very novel Section 1983 claim
against the City. See Heck v. Humphrey, 512 U.S. 477, 486-87, 114 S. Ct. 2364,
2372 (1994). Alvarez’s damage suit proceeded contemporaneously in federal
court with the RICO/bribery charges against the former DA and his attorney
cohorts. Indeed, the judge originally assigned to Alvarez’s case had to recuse
when he became responsible for the criminal case. In the bribery prosecution,
Alvarez’s habeas case was mentioned indirectly.            The City’s attorneys
attempted repeatedly to challenge the redacted video in Alvarez’s civil suit, but
the federal court ignored their efforts. Why? I do not understand the district
court’s unwillingness to explore whether Alvarez’s case was founded on
doctored evidence. If doctored evidence tainted Alvarez’s habeas case, the
federal court would have had to consider ethical action against certain
attorneys. On the other hand, it would not have had to opine on unusual issues
concerning municipal liability and the ramifications of the Brady doctrine.
      Allegations of doctored evidence here may have been misplaced, but
surely they were not frivolous. Because factual integrity is the gateway to
litigating a claim in court, Fed. R. Civ. P. 11, integrity in the fact-finding
process must be maintained vigilantly. No defendant, including the City,
should be persecuted by means of litigation with a false foundation.           It’s
unfortunate if that is what happened here.
      I urge our colleagues at the district court level to be more attuned to non-
frivolous complaints of potentially unethical behavior.




                                       19
    Case: 16-40772       Document: 00514646077          Page: 20     Date Filed: 09/18/2018



                                       No. 16-40772
STEPHEN HIGGINSON, Circuit Judge, joined by JOLLY, JONES, WIENER
and OWEN, Circuit Judges, concurring:

       Criminal discovery rules and practices vary. In federal criminal cases,
discovery practices are responsive to local court and professionalism
requirements, notably the United States Attorney’s Manual; 1 the rulemaking
process—itself dynamic and receptive to change urged by criminal justice
participants—notably Fed. R. Crim. P. 16 (Discovery and Inspection);
legislative initiatives, notably the Jencks Act, 18 U.S.C. 3500; and, judicial
decisions elaborating the due process imperative for fundamental fairness,
notably Brady v. Maryland, 373 U.S. 83 (1963).
       I write in agreement with the majority that we should not stretch the
last by constitutionalizing Brady forward in time from a fair trial right
(“existing Brady”) to a pre-plea right (“new Brady”), as well as to observe that
the Who, What and When components of any new disclosure obligation be
described with clarity to prosecutors, defense counsel and trial judges.
       Who owes new Brady disclosure (after what, if any, search)? Existing
Brady law imposes constructive knowledge on the government, see, e.g., Kyles
v. Whitley, 514 U.S. 419, 437 (1995) (“[T]he individual prosecutor has a duty to
learn of any favorable evidence known to the others acting on the government's
behalf in the case, including the police.”). If an earlier-in-time, new Brady right
is recognized, the orbit of government responsibility must be drawn. Guilty
plea agreements which offer benefits to defendants are vitally important to



       1 See e.g. U.S.A.M. 9-5.001(D) (Timing of disclosure); id. 9-5.001(D)(1) (“Exculpatory
information must be disclosed reasonably promptly after it is discovered.”); id. 9-11.233 (“It
is the policy of the Department of Justice, however, that when a prosecutor conducting a
grand jury inquiry is personally aware of substantial evidence that directly negates the guilt
of a subject of the investigation, the prosecutor must present or otherwise disclose such
evidence to the grand jury before seeking an indictment against such a person.”).
                                             20
   Case: 16-40772    Document: 00514646077      Page: 21   Date Filed: 09/18/2018



                                 No. 16-40772
accused persons yet remain a matter of executive discretion.         Those plea
agreement offers may well be withheld if a Brady imputation rule applies to
prosecutors when a matter is still being investigated with disparate law
enforcement involvement, especially when law enforcement is responding to
reactive crimes and arrests. Or plea agreement offers may come only with a
waiver of any such new Brady right. Cf. United States v. Sylvester, 583 F.3d
285, 293-294 (5th Cir. 2009) (allowing case-in-chief plea statement waivers). Or
they may come slowly, after coordinated due diligence review of investigative
materials, regardless of whether a defendant seeks to avoid pretrial detention
and the possibility of superseding charges by accepting responsibility and
pleading guilty quickly.
      What must be disclosed? The answer seems to be Brady minus Ruiz, yet
that would revive difficult distinctions between exculpatory and impeachment
evidence which bedeviled earlier due process caselaw. See United States v.
Bagley, 473 U.S. 667, 676 (1985).
      When must disclosure occur? The constitution does not prevent accused
persons from acknowledging responsibility and guilt, yet any new Brady rule
likely would require prosecutors to collect and review existing evidence first,
perhaps, as noted, seeking pretrial detention during that time, as well as,
thereafter, superseding with additional charges if more, not less, incriminating
evidence is found. Depending on the timing of any new Brady rule, especially
one triggered by a defendant’s stated intention to plead guilty, courts may need
to anticipate pretrial detention requests against defendants who seek to plead
guilty as well as requests for in camera submissions or protective orders to
safeguard victims and witnesses.
      Fairness and truth-finding are imperatives. Berger v. United States, 295
U.S. 78, 88 (1935). For that reason, it is worthwhile to emphasize that the
                                      21
    Case: 16-40772       Document: 00514646077          Page: 22     Date Filed: 09/18/2018



                                       No. 16-40772
constitution already protects against prosecutors who use false evidence to
obtain a conviction. Napue v. Illinois, 360 U.S. 264, 269 (1959); Giglio v. United
States, 405 U.S. 150 (1972); cf. Ferrara v. United States, 456 F.3d 278, 291-297
(1st Cir. 2006) (nondisclosure “so outrageous that it constituted impermissible
prosecutorial misconduct sufficient to ground the petitioner's claim that his
guilty plea was involuntary”). 2
       And the constitution already protects against ineffective assistance of
counsel, which occurs regardless of the attractiveness of a plea offer if counsel,
in the best position to have ascertained innocence, fails to “investigate[] the
law and circumstances” relating to a defendant’s guilty plea. See United States
v. Juarez, 672 F.3d 381, 390 (5th Cir. 2012); Hill v. Lockhart, 474 U.S. 52, 59
(1985).
       Finally, the constitution already assures further protection against the
miscarriage of justice of an innocent pleading guilty by requiring that judges
engage in extended, direct colloquy with defendants who seek to confirm their
guilt under oath. Boykin v. Alabama, 395 U.S. 238 (1969); Fed. R. Crim. P.
11(b)(1). Judges must confirm that a factual basis supports every guilty plea.
See Fed. R. Crim. P. 11(b)(3); cf. United States v. Gobert, 139 F.3d 436, 439-441




       2 Furthermore, existing Brady is a continuing duty, United States v. Cessa, 861 F.3d
121, 134 n.8 (5th Cir. 2017) (“Brady obligations are continuing throughout trial, and are
neither dependent on a request from the defendant nor the form of the Brady material.”), and
extends to sentencing, Brady v. Maryland, 373 U.S. 83, 87-88 (1963), thus may be violated if
a prosecutor withholds evidence which contradicts a presentence report offense narrative the
government relies on. As with a proffer of a factual basis at rearraignment, endorsement of
a presentence report will occur during the period when defendants may seek to withdraw
their guilty pleas and any existing Brady obligation and disclosure triggered by use of a
factual basis or presentence report may well qualify as a “fair and just reason for requesting
withdrawal.” Fed. R. Crim. P. 11(d).
                                             22
    Case: 16-40772      Document: 00514646077         Page: 23    Date Filed: 09/18/2018



                                     No. 16-40772
(5th Cir. 1998) (finding clear error in acceptance of guilty plea without adequate
factual basis). 3




      3Indeed, judges frequently ask defendants to confirm their guilt in their own words.
This may be particularly advisable when defendants and the government submit plea
agreements with especially favorable terms for court acceptance. Fed. R. Crim. P. 11(c)(2)-
(5).
                                            23
    Case: 16-40772    Document: 00514646077      Page: 24    Date Filed: 09/18/2018



                                  No. 16-40772
JAMES C. HO, Circuit Judge, joined by E. GRADY JOLLY, EDITH H. JONES,
JERRY E. SMITH, EDITH BROWN CLEMENT, and PRISCILLA R. OWEN,
Circuit Judges, concurring:

      A number of circuits are openly flirting with, if not embracing outright,
a novel alteration of the constitutional doctrine first announced in Brady v.
Maryland, 373 U.S. 83 (1963). See, e.g., Smith v. Baldwin, 510 F.3d 1127, 1148
(9th Cir. 2007) (en banc) (citing Sanchez v. United States, 50 F.3d 1448, 1454
(9th Cir. 1995)); United States v. Ohiri, 133 F. App’x 555, 562 (10th Cir. 2005)
(unpublished); McCann v. Mangialardi, 337 F.3d 782, 788 (7th Cir. 2003).
      Under Brady, the defendant has the right to review exculpatory material
from the prosecution team in order to prepare for trial. Under the proposed
new rule, the prosecution team is now required to disclose such material, even
if the accused does not want it, and instead seeks to plead guilty—and if the
accused does not receive the material, he can later nullify the plea agreement.
      The proposed rule is foreclosed by circuit precedent. And Chief Judge
Stewart’s en banc majority opinion expressly declines any invitation to
overrule our precedent. I am pleased to join his excellent opinion.
      I write separately to make two points about precedent. First, there was
no justification for the district court to ignore our circuit precedent. Second,
our circuit precedent was correctly decided.        Indeed, it is compelled by
established principles of constitutional law:      Brady announced a right to
exculpatory evidence as part of the right to a fair trial. Pleading guilty waives
the right to a trial, and inherent in that waiver is the waiver of subsidiary trial
rights such as Brady.      The district court contradicted these established
principles when it extended Brady to the plea bargaining stage and treated it
not as a right of the accused, but as a requirement defendants cannot waive.
      I concur in the reversal of the district court.

                                        24
   Case: 16-40772     Document: 00514646077     Page: 25   Date Filed: 09/18/2018



                                 No. 16-40772
                                       I.
      If the constitutional theory urged by George Alvarez and his amici had
been an open question in this circuit, the district court could have attempted
to justify its judgment on either the text or original understanding of the
Constitution or on a faithful application of analogous Supreme Court or circuit
precedent.
      But that is not this case. To the contrary, the district court awarded a
$2.3 million judgment based on a constitutional theory that our previous
rulings expressly foreclose. See United States v. Conroy, 567 F.3d 174, 178–79
(5th Cir. 2009) (per curiam) (citing Matthew v. Johnson, 201 F.3d 353, 361–62
(5th Cir. 2000)). What’s more, the district court did not even cite—let alone
distinguish—our prior precedents.
      In describing the judicial power established in Article III of the
Constitution, Federalist 78 observes that, “[t]o avoid an arbitrary discretion in
the courts, it is indispensable that they should be bound down by strict rules
and precedents, which serve to define and point out their duty in every
particular case that comes before them.” THE FEDERALIST NO. 78 (Alexander
Hamilton).
      Consistent with these foundational constitutional principles, it is long
established that district courts are bound to follow circuit precedent unless it
directly conflicts with Supreme Court precedent. See, e.g., Campbell v. Sonat
Offshore Drilling, Inc., 979 F.2d 1115, 1121 n.8 (5th Cir. 1992) (“It has been
long established that a legally indistinguishable decision of this court must be
followed by other panels of this court and district courts unless overruled en
banc or by the United States Supreme Court.”).




                                       25
   Case: 16-40772     Document: 00514646077     Page: 26   Date Filed: 09/18/2018



                                 No. 16-40772
      In the event of such a conflict, Supreme Court precedent of course plainly
controls. But there is no such conflict here: The Supreme Court has never held
that Brady establishes an unwaivable right at the plea bargaining phase.
      To the contrary, the Supreme Court has held precisely the opposite in
the context of two different categories of Brady material. See United States v.
Ruiz, 536 U.S. 622 (2002). First, prosecutors need not disclose exculpatory
impeachment evidence at the plea bargaining stage, as Chief Judge Stewart
explains. See Op. at 14–17 (citing Ruiz, 536 U.S. at 630–33). Moreover,
prosecutors need not disclose exculpatory evidence concerning any potential
affirmative defense at the plea bargaining stage. See Ruiz, 536 U.S. at 633
(“We do not believe the Constitution here requires provision” of “information
the Government has regarding any ‘affirmative defense’” “prior to plea
bargaining”); see also id. (Thomas, J., concurring) (“I agree with the Court that
the Constitution does not require the Government to disclose either affirmative
defense information or impeachment information relating to informants or
other witnesses before entering into a binding plea agreement with a criminal
defendant.”).
      Neither Alvarez nor his amici have explained why one rule should apply
to exculpatory evidence concerning the prima facie elements of a criminal case,
and a different rule should apply to exculpatory evidence concerning
affirmative defenses. Certainly nothing in the text or original understanding
of the Constitution supports such a distinction. And most importantly, no
Supreme Court decision has ever so held (tellingly, the district court does not




                                       26
    Case: 16-40772       Document: 00514646077          Page: 27     Date Filed: 09/18/2018



                                      No. 16-40772
even cite, let alone rely on, Ruiz). So there was no basis for the district court
to ignore binding circuit precedent. 1
                                             II.
       What’s more, our circuit precedent is correct: Brady is a trial right—and
it is a right that the accused waives if he agrees to a plea bargain.
       For his part, Alvarez argues that we should extend Brady from the trial
stage to the plea bargaining stage—and that we should treat Brady as a
requirement that a defendant cannot waive. As his brief contends, courts
should not only extend Brady to the plea bargaining phase, but also refuse to
credit any waiver of Brady rights, on the ground that any such “waiver cannot
be deemed ‘intelligent and voluntary’ [because it was] ‘entered without
knowledge      of   material      information      withheld     by    the    prosecution.’”
Supplemental Brief for Appellee at 36 (quoting Sanchez v. United States, 50
F.3d 1448, 1453 (9th Cir. 1995)).
       He errs on both counts. What’s more, converting Brady from a right to
a requirement would diminish, rather than enhance, its value to the accused.
                                             A.
       First, it is well established that Brady is a trial right. It is a right to
exculpatory evidence that is part and parcel of the constitutional right to a fair
trial under the Due Process Clause.




       1 Alvarez relies heavily on Supreme Court decisions that extend the requirement of
effective assistance of counsel to the plea bargaining stage. See, e.g., Lafler v. Cooper, 566
U.S. 156, 162–63 (2012); Missouri v. Frye, 566 U.S. 134, 140 (2012); Padilla v. Kentucky, 559
U.S. 356, 364–66 (2010). But none of those cases purport to question or undermine the
Court’s earlier decision in Ruiz declining to extend Brady to the plea bargaining phase. If
there is conceptual tension in extending the effective assistance of counsel requirement to
the plea bargaining stage, but not Brady, it has not troubled the Supreme Court.
                                             27
    Case: 16-40772    Document: 00514646077       Page: 28   Date Filed: 09/18/2018



                                  No. 16-40772
      The Supreme Court has repeatedly characterized the Brady right as
necessary to ensure a fair trial—characterizations that contradict the
suggestion    that   disclosure   is   additionally   required    to   ensure   the
constitutionality of pre-trial proceedings. In United States v. Agurs, 427 U.S.
97 (1976), for example, the Court observed that “the prosecutor will not have
violated his constitutional duty of disclosure unless his omission is of sufficient
significance to result in the denial of the defendant’s right to a fair trial.” Id.
at 108. See also, e.g., Ruiz, 536 U.S. at 628 (describing Brady as “a right that
the Constitution provides as part of its basic ‘fair trial’ guarantee”) (citing U.S.
CONST. amend. V, VI; Brady, 373 U.S. at 87); United States v. Bagley, 473 U.S.
667, 675 (1985) (“The Brady rule is based on the requirement of due process.
. . . [A prosecutor must] disclose evidence favorable to the accused that, if
suppressed, would deprive the defendant of a fair trial.”); Weatherford v.
Bursey, 429 U.S. 545, 559 (1977) (“[U]nder Brady . . . the prosecution has the
‘duty under the due process clause to insure that “criminal trials are fair” by
disclosing evidence favorable to the defendant upon request.’”) (citation
omitted).
      The entire purpose of plea bargains, of course, is to avoid the need for
trial altogether.    Extending Brady to the plea bargaining phase thus
contradicts the established understanding of Brady as a trial right. As Justice
Thomas observed in Ruiz: “The principle supporting Brady was ‘avoidance of
an unfair trial to the accused.’ That concern is not implicated at the plea
stage.” Ruiz, 536 U.S. at 634 (Thomas, J., concurring) (citation omitted).
                                        B.
      The proposed new rule also misunderstands the basic nature of plea
bargains. Plea bargains, by their very definition, involve the waiver of a
number of fundamental rights.
                                        28
    Case: 16-40772    Document: 00514646077      Page: 29    Date Filed: 09/18/2018



                                  No. 16-40772
      First and foremost, plea bargains waive the right to trial itself. What’s
more, inherent in the waiver of trial is a waiver of all rights attendant to a fair
trial—such as the Fifth Amendment right against self-incrimination, the Sixth
Amendment rights to a trial before a jury, to confront one’s accusers, and to
obtain compulsory process, and the right to disclosure of exculpatory evidence
under Brady. See, e.g., Florida v. Nixon, 543 U.S. 175, 187 (2004) (“By entering
a guilty plea, a defendant waives constitutional rights that inhere in a criminal
trial, including the right to trial by jury, the protection against self-
incrimination, and the right to confront one’s accusers.”) (citing Boykin v.
Alabama, 395 U.S. 238, 243 (1969)); Godinez v. Moran, 509 U.S. 389, 397 n.7
(1993) (same); Winters v. Cook, 489 F.2d 174, 179 (5th Cir. 1973) (en banc)
(“[P]ersonal fundamental rights include the right to plead guilty (which of
course encompasses the waiver of numerous rights), the right to waive trial by
jury, the right to waive appellate review and the right to testify personally.”)
(citing Developments in the Law—Federal Habeas Corpus, 83 HARV. L. REV.
1038, 1011 n. 102 (1970)).
      The point is simply this: The Constitution enumerates a series of rights
of the accused—but the defendant may waive those rights, for example, in
exchange for leniency in a plea agreement. There is no reason to treat Brady
any differently. To the contrary, to regard Brady, not as a right that the
accused can waive, but as a requirement that prosecutors must obey, would be
incongruous with our approach to other similar constitutional doctrines.
      No one would claim, for example, that plea bargaining itself is
unconstitutional—even though it inherently involves the right to trial under
the Sixth Amendment. See, e.g., Brady v. United States, 397 U.S. 742, 748
(1970) (“[T]he plea is more than an admission of past conduct; it is the
defendant’s consent that judgment of conviction may be entered without a
                                        29
    Case: 16-40772    Document: 00514646077      Page: 30   Date Filed: 09/18/2018



                                  No. 16-40772
trial—a waiver of his right to trial before a jury or a judge.”); Adams v. United
States ex rel. McCann, 317 U.S. 269, 276 (1942) (“It hardly occurred to the
framers of the original Constitution and of the Bill of Rights that an accused,
acting in obedience to the dictates of self-interest or the promptings of
conscience, should be prevented from surrendering his liberty by admitting his
guilt.”).
       It is likewise well established that the accused has the right to waive the
right to jury trial in favor of a bench trial. See, e.g., Adams, 317 U.S. at 278
(“[S]ince trial by jury confers burdens as well as benefits, an accused should be
permitted to forego its privileges when his competent judgment counsels him
that his interests are safer in the keeping of the judge than of the jury.”). See
also generally Erwin N. Griswold, The Historical Development of Waiver of
Jury Trial in Criminal Cases, 20 VA. L. REV. 655 (1934) (collecting materials).
       Similarly, no one here argues that the accused has an unwaivable Sixth
Amendment right to confront one’s accusers or to have compulsory process to
secure favorable witnesses, prior to agreeing to a plea bargain. Indeed, such
an argument would effectively invalidate numerous codes of criminal
procedure that generally do not permit pre-trial depositions absent special
circumstances. See, e.g., Tex. Code Crim. Proc. § 39.02; La. Code Crim. Proc.
art. 716; Miss. R. Crim. Proc. 17.5. Otherwise, in every rape or sexual abuse
case, for example, the victim would be required to endure a deposition by the
accused, even where the accused is willing to plead guilty and forgo trial.
       Neither Alvarez nor his amici offer any principled distinction as to why—
among these various trial rights, all waivable upon a plea bargain—Brady
should be treated any differently.




                                        30
    Case: 16-40772    Document: 00514646077      Page: 31   Date Filed: 09/18/2018



                                  No. 16-40772
                                        C.
      To convert Brady from a right to a requirement would not only defy
established principles of constitutional law. It would also diminish the value
of those fundamental rights to the accused.
      Rights are most valuable when individuals have the choice not to invoke
them, depending on the circumstances. An old legend tells how the King of
Siam would bestow sacred white elephants upon his political rivals. As gifts
from the king, the elephants could not be rejected. Yet the sacred pachyderms,
which could not be sold or used for work, would inevitably eat their owners out
of house and home—driving them into bankruptcy, and leaving them far worse
off than before they received the “gift.”
      Forcing unwaivable “rights” upon the accused can have a similar effect.
We empower the accused when we allow them to waive their rights. From the
defendant’s perspective, the way to maximize the value of a right is to give him
the option to waive it, just in case (as is often the case) he can exchange it for
something else that is even more valuable to him. As the Supreme Court once
put it: “When the administration of the criminal law in the federal courts is
hedged about as it is by the Constitutional safeguards for the protection of an
accused, to deny him in the exercise of his free choice the right to dispense with
some of these safeguards . . . is to imprison a man in his privileges and call it
the Constitution.” Adams, 317 U.S. at 280 (emphasis added).
      The power to waive trial rights provides the accused with a significant
bargaining chip in plea negotiations. Prosecutors lack the resources to take
every case to trial. So prosecutors have a natural incentive to offer plea deals
with lower penalties than what the accused might receive from a trial. “Plea
bargaining flows from ‘the mutuality of advantage’ to defendants and
prosecutors, each with his own reasons for wanting to avoid trial.”
                                        31
   Case: 16-40772     Document: 00514646077      Page: 32   Date Filed: 09/18/2018



                                  No. 16-40772
Bordenkircher v. Hayes, 434 U.S. 357, 363 (1978). And the flip side is also true:
giving prosecutors “a reduced incentive to bargain” will accrue “to the
detriment of the many defendants for whom plea bargaining offers the only
hope for ameliorating the consequences to them of a serious criminal charge.”
Blackledge v. Perry, 417 U.S. 21, 37 (1974) (Rehnquist, J., dissenting).
      These principles apply to Brady. A defendant who agrees to waive his
Brady right relieves the prosecution team of the substantial burdens
associated with identifying, assembling, and disclosing the range of
exculpatory materials required under Brady—as explained further in Judge
Higginson’s thoughtful concurrence.         Converting the Brady right into a
prosecutorial requirement would substantially upset this balance, by giving
defendants less to offer the prosecution during the negotiations. Prosecutors
may be less likely to offer deals at all, if they are forced to expend significant
resources regardless of whether the case is pled or proceeds to trial. Or they
might offer inferior plea deals, in the form of longer sentences. Either result
is a materially worse outcome for the accused.
                                         ***
      There are times when it is necessary to upset circuit precedent—for
example, in direct response to squarely conflicting Supreme Court precedent,
or (where the Supreme Court has not yet ruled) to better align our precedents
with the text and original understanding of the Constitution or the plain
language of United States statutes. But that is not this case.
      To the contrary, the alteration of our circuit’s Brady precedents urged by
Alvarez and his amici would violate established legal principles and even
diminish the value of Brady to the accused. If there is a case to be made for
such reform, it must be accomplished through one of the mechanisms
established by our Founders, such as Article V of the Constitution, or through
                                       32
    Case: 16-40772      Document: 00514646077        Page: 33     Date Filed: 09/18/2018



                                     No. 16-40772
the proper exercise of legislative powers vested in Congress and in the several
states. Cf. Brady, 373 U.S. at 92 (separate opinion of White, J.) (“I would leave
this task, at least for now, to the rulemaking or legislative process after full
consideration by legislators, bench, and bar.”).
      I concur in the reversal of the district court. 2




      2  I also agree with the majority’s reliance on Monell. And I recognize that Monell
alone is enough to reverse the judgment of the district court—we did not have to undertake
the additional effort of addressing Brady in order to decide this appeal. But our Court
granted rehearing en banc to reach the Brady question—and it is a question our dissenting
colleagues address as well—so accordingly, I examine the Brady issue presented here.
                                           33
   Case: 16-40772    Document: 00514646077      Page: 34   Date Filed: 09/18/2018



                                 No. 16-40772
JAMES L. DENNIS, Circuit Judge, dissenting:
      I respectfully dissent from the majority opinion because, in my view, the
en banc court should have recognized the federal constitutional right of a
defendant to exculpatory evidence at the plea-bargaining stage, essentially for
the reasons described in Judge Costa’s dissent. I also join Part 1 of Judge
Graves’s dissent, in which he explains how the City’s policy of nondisclosure of
exculpatory evidence caused a violation of Alvarez’s right to the exculpatory
video that ultimately exonerated him, prior to entering his guilty plea.




                                      34
   Case: 16-40772         Document: 00514646077       Page: 35   Date Filed: 09/18/2018



                                       No. 16-40772
JAMES E. GRAVES, JR., Circuit Judge, joined by COSTA, Circuit Judge,
dissenting 1:

      I write separately to: (1) dissent from the majority’s moving force
analysis; (2) dissent from the majority’s deliberate indifference analysis; and
(3) address Brownsville’s egregiously inadequate training policies.
      1.       Non-disclosure policy was moving force for non-disclosure.
      The majority states that the Brownsville Police Department’s (“BPD”)
failure to disclose the video evidence was the result of a “series of
interconnected errors” by individual officers that was “separate from” official
BPD policy. I respectfully disagree.
      “[T]here can be no municipal liability unless [an official policy] is the
moving force behind the constitutional violation.” James v. Harris Cty., 577
F.3d 612, 617 (5th Cir. 2009). “In other words, a plaintiff must show direct
causation, i.e., that there was ‘a direct causal link’ between the policy and the
violation.” Id. (quoting Piotrowski v. Hous., 237 F.3d 567, 578 (5th Cir. 2001)).
Whether a sufficient causal link exists is a question of fact. See Jett v. Dall.
Indp. Sch. Dist., 491 U.S. 701, 737 (1989); Kirkpatrick v. Washoe, 843 F.3d 784,
797 (9th Cir. 2016); James, 577 F.3d at 618; Bielevicz v. Dubinon, 915 F.2d 845,
851 (3d Cir. 1990).
      Here, as part of the internal affairs division (“IAD”) investigation, Officer
Arias created a use of force report and submitted it up his chain of command
to Sgt. Infante and Commander Rodriguez. Infante and Rodriguez then
reviewed the report, and the video evidence, and submitted their own
individual reports to Chief Garcia. Garcia never reviewed the file, and none of
the officers disclosed the videos outside of the IAD.


      1   Judge Dennis joins part 1.
                                           35
   Case: 16-40772     Document: 00514646077       Page: 36   Date Filed: 09/18/2018



                                   No. 16-40772
      Meanwhile, Officer Carrejo, the criminal investigations division (“CID”)
officer assigned to submit the case file to the District Attorney, obtained the
IAD incident reports from the jail. Carrejo then submitted those reports to the
District Attorney without conducting additional evidentiary investigation
because there was no “evidence form” in the records alerting him that relevant
evidence existed.
      According to the majority, these actions were a “series of interconnected”
errors by the officers involved. With respect, record evidence shows that the
officers committed no errors at all under BPD policies.
      CID investigators are responsible for providing criminal case files to the
District Attorney’s office. To start that process, they collect documents, such as
incident reports, from a “cubbyhole” at the jail designated for the CID case prep
team. They then conduct evidentiary follow-up as needed, based largely on
“evidence forms” that fellow officers attach to the files provided to CID.
Without an evidence form in the file, CID investigators would be unaware that
follow-up is necessary.
      BPD has a policy, however, that IAD officers do not proactively disclose
evidence, including Brady evidence, to CID investigators. Instead, IAD officers
pass all Brady evidence up their chain of command to Chief Garcia, who has
sole responsibility to ensure that any Brady evidence is properly disclosed.
Because these officers do not disclose evidence, there is no “evidence form”
generated for the CID case file.
      Thus, contrary to the majority’s view, the officers committed no
“interconnected errors” in conducting their investigation. The IAD officers
faithfully passed the evidence up the chain of command to Chief Garcia
without disclosing the evidence to CID. In turn, the CID officer, unaware that
relevant evidence existed, conducted no evidentiary follow-up and simply
                                       36
   Case: 16-40772     Document: 00514646077     Page: 37   Date Filed: 09/18/2018



                                 No. 16-40772
passed the file to the District Attorney’s office. This was not error, it was how
the system was designed to work.
      Moreover, while the majority characterizes Garcia’s failure to review the
file as nothing “more than negligent oversight,” the record paints a different
picture. Indeed, Garcia did not review nine out of thirteen known use of force
cases. Even when Garcia did review such files, it may be “several weeks, even
up to a month or more . . . after the criminal case had been submitted to the
[D]istrict [A]ttorney’s office.” Garcia’s failure to review the instant case was
entirely in line with BPD practice.
      I therefore respectfully dissent from the majority’s conclusion that
Alvarez has not established that the non-disclosure policy was the moving force
behind the alleged violation. BPD’s policy of not disclosing exculpatory
evidence to CID investigators was the direct cause of BPD’s failure to disclose
the video evidence to the District Attorney and the defense.
      2.    Non-disclosure      policy      implemented     with     deliberate
      indifference.
      The majority next concludes that BPD could not have implemented the
non-disclosure policy with deliberate indifference because there was an
“understanding throughout the police department” that IAD officers could
disclose exculpatory evidence. With respect, that conclusion is not supported
by the record evidence.
      Though BPD officers did claim that they “should,” “could,” and “would”
have disclosed the video evidence to the CID if asked to do so, the
overwhelming weight of the evidence is that officers understood that IAD
evidence was simply not shared with CID as a matter of policy.
      For instance, officers were trained to consider IAD and CID as separate
investigative tracts that operate independently. As a result, there was a
                                       37
    Case: 16-40772      Document: 00514646077        Page: 38     Date Filed: 09/18/2018



                                     No. 16-40772
widespread belief among IAD officers that they had no duty to confirm that
CID had exculpatory evidence. Instead, IAD officers simply passed evidence up
their chain of command without disclosure to, or even consideration of, any
parallel CID investigation. That understanding was based on “in-service
training.”
      In contrast, there is no evidence to support the officers’ claims that IAD
officers would, could, or should freely disclose evidence to the CID. Quite the
opposite is true, as no BPD policy, commanding officer, or training, informed
IAD officers that they could, or even should, do so.
      Compounding this problem, BPD provided CID investigators with no
training on how to conduct their investigations. Instead, CID officers act purely
pursuant to on-the-job experience. For Carrejo, that “mostly consists of getting
ahold of victims or witnesses and get[ting] whatever information is needed for
the file.” Carrejo expects fellow officers to “book” relevant evidence in order to
generate an “evidence report,” 2 so that Carrejo can then “follow up with that
evidence.” There is no indication in the record that Carrejo received any
training, or even instruction, to pursue the robust evidentiary investigation
that Brownsville, and the majority, claims he should have done. There is
likewise no evidence at all that CID investigators ever asked IAD for evidence.
      I respectfully dissent from the majority’s conclusion that there was an
“understanding throughout the police department” that IAD officers could
disclose exculpatory evidence. The weight of the evidence states otherwise.
      I also disagree with the majority opinion’s conclusion that a deliberate
indifference theory of municipal liability was not viable because at the time we



      2 These evidence reports were among the many topics on which BPD failed to train its
CID officers.
                                           38
    Case: 16-40772     Document: 00514646077     Page: 39   Date Filed: 09/18/2018



                                  No. 16-40772
had not recognized a pre-plea right to Brady material. The City never made
this “clearly established” argument in the district court or in our court. By
adopting it sua sponte, the court repeats the mistake we recently made in
Hernandez v. Mesa, 785 F.3d 117 (5th Cir. 2015) (en banc). We held that a
border patrol agent was entitled to qualified immunity for shooting a Mexican
national because the law was not clearly established that the Fifth
Amendment applied to a foreign citizen injured outside the United States. Id.
at 121. The Supreme Court reversed, explaining that the agent did not know
at the time of the shooting whether the victim was a U.S. citizen. 137 S. Ct.
2003, 2007 (2017). The same is true for the similar deliberate indifference
inquiry here. When he failed to disclose the exculpatory video, Police Chief
Garcia did not know that Alvarez was pleading guilty. Even more than in
Mesa, he could not have known as that fact did not yet exist (that is, the plea
decision had not yet been made). But Garcia knew that the way to comply with
the Brady obligation that has long existed for cases that go to trial is to notify
the criminal investigations division of exculpatory material in the IA file so it
becomes part of the prosecutor’s file later disclosed to the defense. There was
not one procedure for transferring exculpatory evidence from the IAD side to
the investigations side for “trial” cases and a separate procedure for “plea”
cases. Because that transfer of the video to the investigations division did not
happen, Garcia was deliberately indifferent to the long recognized Brady right
for cases that get tried.
      It is true that some caselaw suggests that deliberate indifference liability
applies only when the indifference is to a clearly established right. The idea,
the same rationale for qualified immunity, is that liability should attach based
on an individual’s conduct only if there is a knowing violation of constitutional
law. That culpability exists here because Garcia was deliberately indifferent
                                       39
   Case: 16-40772     Document: 00514646077      Page: 40   Date Filed: 09/18/2018



                                  No. 16-40772
to his constitutional obligation to turn over exculpatory evidence for a case
that, like any other, could have resulted in a trial with the long recognized
Brady right. Once that deliberate indifference to a clear constitutional right is
established, it is just a matter of causation to show that the deliberate
indifference to ensuring the criminal file contained exculpatory material led to
Alvarez’s constitutional injury that Judge Costa’s opinion recognizes.
      The defect in the majority opinion on this point can be seen by imagining
this same case but with Alvarez having gone to trial on the criminal charge.
Under the majority opinion’s analysis, Garcia could avoid liability by saying
“well, when I failed to give the video to the criminal investigators, I thought he
was probably going to plead. And it is not clearly established that I have to
turn over exculpatory evidence when defendants plead.” That defense should
not immunize the City from liability because Garcia did not know how the
criminal case would be resolved when he failed to disclose the video to the
investigative side. Thus, (1) Garcia was deliberately indifferent to the clear-
as-can-be Brady rights that defendants going to trial have, and (2) Garcia’s
deliberate indifference caused the violation of Alvarez’s right to pre-plea Brady
materials.
      3.     BPD training policy was constitutionally deficient.
      Though the majority does not address Alvarez’s claim that Brownsville
failed to adequately train its officers on Brady rights, I do so because BPD’s
training policy, or rather complete lack thereof, is so deficient that it clearly
exhibits deliberate indifference to the constitutional rights of those that come
into contact with BPD officers.
      “[T]he inadequacy of police training may serve as the basis for § 1983
liability only where the failure to train amounts to deliberate indifference to
the rights of persons with whom the police come into contact.” Canton v.
                                       40
   Case: 16-40772     Document: 00514646077      Page: 41   Date Filed: 09/18/2018



                                  No. 16-40772
Harris, 489 U.S. 378, 388 (1989). “[I]t may happen that in light of the duties
assigned to specific officers or employees the need for more or different training
is so obvious, and the inadequacy so likely to result in the violation of
constitutional rights, that the policymakers of the city can reasonably be said
to have been deliberately indifferent to the need.” Id. at 390.
      As Chief Garcia acknowledged, it is foreseeable that BPD officers will
encounter use of force incidents and, as a result, have to decide what evidence
to disclose in their reports. Garcia further acknowledged that officers will
choose what evidence to disclose “based on the type of training they receive.”
Despite this foreseeability, BPD had “no policy” of providing training on Brady.
Indeed, Chief Garcia could not even state whether any of his officers had ever
touched on Brady at any time. At best, Garcia claimed only that BPD officers
had “[m]aybe” covered Brady in non-BPD trainings - in some cases up to 30
years in the past.
      Unsurprisingly, BPD officers suffer from widespread ignorance on Brady
rights. Chief Garcia candidly admitted that “it would not surprise” him to learn
that his officers did not know what Brady obligations are. Nor should it. Officer
Arias did not know what “exculpatory” meant, and Officer Carrejo, the CID
officer assigned to provide evidence to the District Attorney, was likewise “not
familiar.”
      That such a complete failure to train on Brady rights is “likely to result
in the violation of constitutional rights” is “obvious,” see Canton, 489 U.S. at
390, because “in the absence of training, there is no way for novice officers to
obtain the legal knowledge they require.” Connick v. Thompson, 563 U.S. 51,
64 (2011). Naturally, the resulting “[w]idespread officer ignorance on the
proper handling of exculpatory materials would have the ‘highly predictable


                                       41
    Case: 16-40772     Document: 00514646077        Page: 42   Date Filed: 09/18/2018



                                     No. 16-40772
consequence’ of due process violations.” See Gregory v. Louisville, 444 F.3d 725,
753 (6th Cir. 2006).
      Brownsville’s complete lack of training on Brady rights evidences
“deliberate indifference to the [constitutional] rights of persons with whom the
police come into contact.” See Canton, 489 U.S. at 388; see also Gregory, 444
F.3d at 753-54.
                                 CONCLUSION
      The district court thought the evidence showing municipal liability was
so strong that it granted summary judgment on that issue in favor of the
plaintiff. The majority opinion does a 180-degree turn and holds there is no
municipal liability as a matter of law. For the reasons I have discussed, at a
minimum, there are factual disputes that a jury should resolve on municipal
liability. I respectfully dissent.




                                         42
    Case: 16-40772       Document: 00514646077          Page: 43     Date Filed: 09/18/2018



                                       No. 16-40772
GREGG COSTA, Circuit Judge, joined by GRAVES, Circuit Judge, dissenting:
       Let this sink in: If George Alvarez had been convicted of a federal crime
in this circuit, he would have served his full 10-year sentence despite
eventually discovering that the government failed to disclose an exculpatory
video. That is because we are the only federal court of appeals that has held
that a defendant who pleads guilty is not entitled to evidence that might
exonerate him. Fortunately for Alvarez, and for those who believe that “justice
suffers when any accused is treated unfairly,” Brady v. Maryland, 373 U.S. 83,
87 (1963), he was convicted of a state offense. 1 For almost forty years, Texas
has interpreted the federal Brady right to require the government to provide
exculpatory information “to defendants who plead guilty as well as to those
who plead not guilty.” Ex parte Lewis, 587 S.W. 2d 697, 701 (Tex. Crim. App.
1979); see also Ex parte Johnson, 2009 WL 1396807, at *1 (Tex. Crim. App.
May 20, 2009) (vacating a guilty plea because of a Brady violation). Texas is
not alone. The highest courts of other states that have considered this question
agree that defendants have a federal due process right to exculpatory evidence
before they plead guilty. See Buffey v. Ballard, 782 S.E.2d 204, 218 (W. Va.
2015); State v. Huebler, 275 P.3d 91, 96–97 (Nev. 2012); Hyman v. State, 723
S.E.2d 375, 380 (S.C. 2012); Medel v. State, 184 P.3d 1226, 1235 (Utah 2008).
Because we now have “for the most part a system of pleas, not a system of
trials,” Lafler v. Cooper, 566 U.S. 156, 170 (2012), today’s opinion reaffirming
our outlier position means that the vast majority of defendants in this circuit



       1 In its amicus brief, the Department of Justice points to the grant of habeas relief in
Alvarez’s case as an example of the “existing remedies . . . typically available to defendants
who admit their guilt but later claim actual innocence” that makes a Brady right unnecessary
for such defendants. U.S. Br. 13. This ignores that federal habeas law, whether reviewing
state or federal convictions, would not provide that relief because it does not recognize a
freestanding innocence claim. Herrera v. Collins, 506 U.S. 390, 400 (199).
                                             43
    Case: 16-40772    Document: 00514646077       Page: 44   Date Filed: 09/18/2018



                                  No. 16-40772
will not have a right to relief if it comes to light after their conviction that the
government suppressed exculpatory evidence.
      The origins of the Brady right support Texas courts’ longstanding view
that it requires pre-plea disclosure of exculpatory evidence.         The seminal
Supreme Court case describes the right as a due process requirement for a
prosecutor, upon request, to disclose information favorable to the accused that
“is material either to guilt or to punishment.” Brady, 373 U.S. at 87. Although
the more common framing of the right is the first characterization that relates
to “innocence or guilt,” Brady itself was a case about punishment as the
suppressed confession only resulted in a new sentencing trial. Id. at 90–91. It
is notable that the right has from its inception applied to the sentencing phase
of a proceeding that is vitally important but “does not concern the defendant’s
guilt or innocence.” Lafler, 566 U.S. at 165. Because a plea hearing is all about
a defendant’s guilt or innocence, it more strongly implicates Brady’s
“overriding concern with the justice of the finding of guilt.” United States v.
Bagley, 473 U.S. 667, 678 (1985) (quoting United States v. Agurs, 427 U.S. 97,
112 (1976). It certainly does so more directly than does a suppression hearing
where the focus is on whether the government unlawfully obtained evidence,
see United States v. Bowie, 198 F.3d 905, 912 (D.C. Cir. 1999), yet we have
recognized the Brady right extends to suppression motions. Smith v. Black,
904 F.2d 950, 965–66 (1990), vacated on other grounds, 503 U.S. 930 (1992).
And the Brady rule seeks “to ensure that a miscarriage of justice does not
occur,” Bagley, 473 U.S. at 675, a risk that we know exists not just for trial
convictions but also for guilty pleas, see Brady v. United States, 397 U.S. 742,
758 (1970) (recognizing that plea agreements are “no more foolproof than full
trials”); Stephanos Bibas, Plea Bargaining’s Role in Wrongful Convictions, in
EXAMINING WRONGFUL CONVICTIONS 157–62 (2014) (discussing the incentives,
                                        44
    Case: 16-40772      Document: 00514646077       Page: 45    Date Filed: 09/18/2018



                                    No. 16-40772
structural constraints, and psychological influences that can lead to innocent
defendants pleading guilty); infra p. 16.
      Digging deeper into the roots of Brady further supports its application to
requests for exculpatory evidence before pleading. The 1963 decision relied on
earlier Supreme Court cases recognizing a due process violation when the
government knowingly used false testimony to secure a conviction. See 373
U.S. at 86–87 (citing Mooney v. Holohan, 294 U.S. 103, 112 (1935) (per curiam);
Napue v. Illinois, 360 U.S. 264, 269 (1959)). At a plea hearing, the government
must provide a factual basis for the defendant’s guilt to support the conviction.
See FED. R. CRIM. P. 11(b)(3); cf. Brady v. United States, 397 U.S. at 758
(explaining that a court’s ability to determine “that there is nothing to question
the accuracy and reliability of the defendants’ admissions” provides an
important safeguard against problems with plea agreements). Just as failure
to provide exculpatory information at a trial subverts the jury’s ability to
determine guilt, so too does failure to provide that information in connection
with a plea prevent the judge from properly assessing whether there is a
factual basis to support a conviction. Failing to disclose exculpatory evidence
in reciting the essential facts of the case thus is at odds with the government’s
constitutional duty to tell the truth in court.
      Indeed, as a general matter due process rights are usually not limited to
trials, but may apply in various types of proceedings at which the government
seeks to deprive someone of life, liberty, or property. Other due process rights
apply at plea hearings, most fundamentally the requirement that a plea be
knowing and voluntary. 2 McCarthy v. United States, 394 U.S. 459, 466 (1969).


      2  Some courts have taken the view that a failure to disclose exculpatory evidence
renders the plea unknowing and involuntary. Sanchez v. United States, 50 F.3d 1448, 1453
(9th Cir. 1995); cf. United States v. Fisher, 711 F.3d 460 (4th Cir. 2013).
                                          45
    Case: 16-40772      Document: 00514646077        Page: 46     Date Filed: 09/18/2018



                                     No. 16-40772
But also others like the government’s obligation to fulfill its promises in a plea
agreement. Santobello v. New York, 404 U.S. 257, 262 (1971). Looking even
more broadly to the Fifth Amendment as a whole, none of its rights apply solely
in trials. Protections against self-incrimination, takings, double jeopardy, and
being charged without a grand jury indictment guard against arbitrary
government action that can occur in a variety of contexts outside of trial.
Although Fifth Amendment rights may appear to lack the unifying theme that
is evident for the conscience and expression-protecting First Amendment, the
trial-focused Sixth and Seventh Amendments (first criminal then civil); or the
punishment-focused Eighth, one scholar has noted that most rights in the Fifth
Amendment cover the period between the investigative phase addressed in the
Fourth Amendment and the trial phase addressed in the Sixth.                       BURT
NEUBORNE, MADISON’S MUSIC: ON READING THE FIRST AMENDMENT 26–27
(2015). The Amendment’s focus on pretrial criminal proceedings rather than
trials thus further supports requiring the disclosure of exculpatory evidence in
the plea hearing.
      So what is the basis for limiting a due process right like Brady to the
context of a full-blown trial even though a plea hearing involves its core
concern about whether the courts are fulfilling their truth-finding function?
The most basic argument against applying Brady to pleas is that by pleading
guilty the defendant implicitly waives a right to obtain evidence that might
undermine his admission of guilt. 3 Put more bluntly, if a defendant is saying
he is guilty, isn’t that the end of the issue? But the same argument could be



      3  This is different than the question whether a defendant could affirmatively waive
his Brady rights in pleading guilty. This case does not present that question as Alvarez
requested full discovery from the defendant and never waived the Brady right that Texas
courts afford all defendants.
                                           46
    Case: 16-40772     Document: 00514646077       Page: 47    Date Filed: 09/18/2018



                                    No. 16-40772
made and was for ineffective assistance of counsel claims asserted by those
who pleaded guilty. If a defendant admitted guilt, how could he later complain
that with better lawyering he might have been acquitted? Indeed, the right to
effective assistance of counsel was sometimes framed, as Brady has sometimes
been, only as a fair trial right. Strickland v. Washington, 466 U.S. 668, 686
(1984) (explaining that “in giving meaning to the requirement” of effective
assistance, “we must take its purpose—to ensure a fair trial—as the guide”);
see also United States v. Cronic, 466 U.S. 648, 658 (1984) (“[T]he right to the
effective assistance of counsel is recognized not for its own sake, but because
of the effect it has on the ability of the accused to receive a fair trial.”); see also
Michael Nasser Petegorsky, Plea Bargaining in the Dark, 81 FORDHAM L. REV.
3599, 3631 (2013) (“[L]ike Brady, the right to effective assistance was
traditionally considered purely a trial right.”). Yet the Supreme Court has long
recognized that a defendant can undo a guilty plea by showing that ineffective
assistance caused him to make that decision rather than proceed to trial. Hill
v. Lockhart, 474 U.S. 52, 56–57 (1985). The Court’s rejection of the view “that
a knowing and voluntary plea supersedes error by defense counsel,” Missouri
v. Frye, 566 U.S. 134, 141 (2012), reflects a realistic view of modern plea
bargaining, which is influenced by a variety of structural and psychological
forces in addition to traditional notions of risk assessment. See Stephanos
Bibas, Plea Bargaining Outside the Shadow of Trial, 117 HARV. L. REV. 2463,
2507–10 (2004). A defendant may even plead guilty while maintaining his
innocence. North Carolina v. Alford, 400 U.S. 25 (1970). As the Supreme Court
has rejected the plea=waiver argument in the context of ineffective assistance




                                          47
    Case: 16-40772       Document: 00514646077          Page: 48     Date Filed: 09/18/2018



                                       No. 16-40772
claims, it is hard to see how it has much force in the Brady context. 4 Lafler,
566 U.S. at 164.
       Another argument against applying Brady to pleas is that its materiality
inquiry is often framed in terms of the impact the exculpatory information
would have had on the trial. See Matthew v. Johnson, 201 F.3d 353, 361–62
(5th Cir. 2000). 5 But the materiality standard sometimes refers more broadly
to the effect on a “proceeding.” Bagley, 473 U.S. at 682 (“[E]vidence is material
only if there is a reasonable probability that, had the evidence been disclosed
to the defense, the result of the proceeding would have been different.”). That
makes sense as Brady itself was a case about undisclosed evidence that
required a new sentencing hearing but not a new trial. 373 U.S. at 90–91. And
looking to ineffective assistance case law is again instructive. Strickland’s
prejudice requirement developed in tandem with the Brady materiality
standard. In Bagley, the Court recognized it had “relied on and reformulated”
the test for materiality from Brady cases (the Augers test) in Strickland. 473
U.S. at 681–82. It then decided the same refined standard should apply in
Brady cases, concluding “the Strickland formulation” was “sufficiently flexible
to cover [all] cases of prosecutorial failure to disclose evidence favorable to the
accused: [t]he evidence is material only if there is a reasonable probability that,
had the evidence been disclosed to the defense, the result of the proceeding
would have been different.” Id. at 682. And as I have already noted, the
Supreme Court recently rejected the argument that attorney errors “before



       4  Indeed, United States v. Ruiz, 536 U.S. 622 (2002), which will be discussed in more
depth later, did not use a waiver rationale in rejecting a right to impeachment evidence before
a plea.
        5 It is worth noting that Matthew did not review de novo the question of Brady’s

application to pleas. It was a habeas case so the holding was only that Teague v. Lane, 489
U.S. 288 (1989), barred recognizing the right on collateral review. 201 F.3d at 369-70.
                                              48
    Case: 16-40772       Document: 00514646077          Page: 49     Date Filed: 09/18/2018



                                       No. 16-40772
trial . . . are not cognizable under the Sixth Amendment unless they affect the
fairness of the trial itself.” Lafler, 566 U.S. at 164–65. It concluded “the right
to adequate assistance of counsel cannot be defined or enforced without taking
account of the central role plea bargaining plays in securing convictions.” Id.
at 170. The materiality standard thus does not pose a problem because it is
already applied in ineffective assistance cases to assess whether the absence
of attorney error would have changed the plea decision. Armstrong v. Scott, 37
F.3d 202, 206 (5th Cir. 1994); see also Huebler, 275 P.3d at 203 (applying to a
defendant who pleaded a Brady materiality standard asking “whether there is
a reasonable probability that but for the failure to disclose the Brady material,
the defendant would have refused to plead and would have gone to trial”). It
would be anomalous if the Strickland right that is found in the trial-focused
Sixth Amendment applied to pleas but the due process Brady right did not.
       The Department of Justice opposes a pre-plea Brady right in part
because of its belief that such a rule “would impose serious costs on the
criminal justice system” by making pleas less efficient. DOJ Amicus Brief 15.
That concern is puzzling because, as it acknowledges, its own policy requires
federal prosecutors to turn over exculpatory evidence “reasonably promptly
after it is discovered.” UNITED STATES ATTORNEY’S MANUAL (USAM) § 9-
5.001(D)(1). 6    Court rules in 20 federal judicial districts, including Local



       6  The U.S. Attorneys’ Manual distinguishes between exculpatory and impeachment
evidence. As mentioned above, the former must be disclosed “promptly after it is discovered.”
USAM § 9-5.001(D)(1). The latter must be disclosed “at a reasonable time before trial to
allow the trial to proceed efficiently.” Id. § 9-5.001(D)(2). That later in time disclosure of
impeachment evidence may be further delayed if the benefits of pretrial disclosure are
outweighed by “other significant interests—such as witness security or national security.”
Id. The exception for early disclosure of exculpatory information is narrower, limited to
“classified or otherwise sensitive national security material.” Id. § 9-5.001(D)(1). This
confirms that the costs of disclosing impeachment evidence pre-plea are greater than the
                                             49
    Case: 16-40772       Document: 00514646077        Page: 50     Date Filed: 09/18/2018



                                      No. 16-40772
Criminal Rule 16 in the Western District of Texas which usually vies with the
Southern District of Texas for the largest number of federal prosecutions each
year, impose a more definite early disclosure requirement: Brady material
must be disclosed within two weeks of arraignment, which in almost every case
will be before a plea is entered.            FEDERAL JUDICIAL CENTER, BRADY V.
MARYLAND IN THE UNITED STATES DISTRICT COURTS: RULES, ORDERS, AND
POLICIES 16 (2007) (table listing 20 districts that require Brady disclosures
within two weeks of arraignment or when the defendant enters a “not guilty
plea”). And ethical rules in a number of states, including all three that make
up this circuit, require the same of prosecutors. TEX. DISCIPLINARY R. PROF’L
CONDUCT § 3.09(d) (1989); LA. R. PROF’L CONDUCT § 3.08(d) (2004); MISS. R.
PROF’L CONDUCT § 3.08(d) (all based on Rule 3.8 of the American Bar
Association’s Rules of Professional Conduct). 7 Indeed, DOJ cites its policy and
the ethical rules as reasons why applying Brady to pleas is unnecessary. But
if these policies and rules of professional responsibility are resulting in early
disclosure of exculpatory evidence, wouldn’t that impose the same costs that a
corresponding Brady right would? The source of the disclosure obligation
shouldn’t change the cost of compliance.                What is different is that a
constitutional obligation provides the defendant with a remedy when a
prosecutor fails to comply due to either negligence or malice. A violation of
DOJ, court, or ethical rules would not have helped Alvarez when he learned



costs of disclosing exculpatory information, a factor that distinguishes the Supreme Court’s
Ruiz decision from the question we confront. See infra p. 10–11.
        7 MODEL RULES OF PROF’L CONDUCT R. 3.8(D) (2012) (requiring prosecutors to “make
timely disclosure to the defense of all evidence or information known to the prosecutor that
tends to negate the guilt of the accused or mitigates the offense”); ABA COMM. ON ETHICS
AND PROF’L RESPONSIBILITY, Formal Op. 09-454 (2009) (clarifying that disclosure must be
made pre-plea to satisfy “significant purpose” of assisting defendants in making intelligent
plea-bargaining decisions).
                                            50
   Case: 16-40772     Document: 00514646077     Page: 51   Date Filed: 09/18/2018



                                 No. 16-40772
about the undisclosed video. See USAM § 1-1.100 (explaining that the U.S.
Attorney’s Manual does not create any rights enforceable in court).
      But we do not have to guess whether requiring pre-plea disclosure of
exculpatory evidence as a constitutional matter would inhibit plea bargaining.
We can look to experience, as a number of jurisdictions have such a rule. See
Lafler, 566 U.S. at 164, 172 (discounting administrability and “floodgate”
concerns about applying ineffective-assistance-of-counsel claims to the
rejection of plea agreements because a number of circuits had already done so
“without demonstrated difficulties or systemic disruptions”); cf. Jeffrey S.
Sutton, 51 IMPERFECT SOLUTIONS: STATES AND THE MAKING OF AMERICAN
CONSTITUTIONAL LAW 2 (observing that when state courts have recognized a
right under state constitutions, their experience can influence administrability
concerns with recognizing a corresponding right under federal law). Since
1979, Texas state courts have read the Due Process Clause to require
disclosure of exculpatory evidence to defendants who plead guilty. A number
of other states read Brady the same way. See Buffey v. Ballard, 782 S.E.2d
204, 216 (W. Va. 2015); State v. Huebler, 275 P.3d 91, 96–97 (Nev. 2012);
Hyman v. State, 723 S.E.2d 375, 380 (S.C. 2012); Medel v. State, 184 P.3d 1226,
1235 (Utah 2008); State v. Gardner, 885 P.2d 1144, 1149 (Idaho Ct. App. 1994).
Some federal circuits have also applied Brady to plea cases either before or
after the Supreme Court’s decision in Ruiz. See Campbell v. Marshall, 769
F.2d 314, 324 (6th Cir. 1985); White v. United States, 858 F.2d 416, 422 (8th
Cir. 1988); Sanchez v. United States, 50 F.3d 1448, 1453 (9th Cir. 1995); United
States v. Avellino, 136 F.3d 249, 255 (2d Cir. 1998); United States v. Ohiri, 133
F. App’x 555, 560–61 (10th Cir. 2005). Yet these decisions have not impeded
ever-rising rates of pleas. In recent years, roughly 97% of federal convictions
were the result of a plea. Lafler, 566 U.S. at 170. 94.6% of Texas cases were
                                       51
   Case: 16-40772     Document: 00514646077        Page: 52   Date Filed: 09/18/2018



                                 No. 16-40772
resolved via plea in 2016. OFFICE OF COURT ADMIN., ANNUAL STATISTICAL
REPORT OF THE TEXAS JUDICIARY: FY 2016 at Detail-10 (2016); available at
http://bit.ly/2mcF9vp. In terms of the trend, recent decades have seen a 10-
25% increase in the percentage of convictions obtained through pleas.
Compare Lafler, 566 U.S. at 170 (reporting that “ninety-four percent of state
convictions are the result of guilty pleas”), with Brady v. United States, 397
U.S. 742, 752 n.10 (1970) (estimating that between 75 and 85% of all felony
convictions were pleas). The rise of the plea is seemingly inexorable and there
is no reason to believe that a pre-plea Brady rise gets in its way.
      There is one other problem with DOJ’s concerns about the workability of
a pre-plea Brady requirement.      From the beginning, the Brady right has
covered information that might be favorable to a defendant at sentencing. So
as the government conceded at oral argument, a plea does not excuse its
obligation to disclose any evidence in the prosecution’s file that might mitigate
the defendant’s sentence. This means it is not a matter of whether exculpatory
information is produced but when—either before the plea or after the plea but
before sentencing. See USAM § 9-5.001(D)(3) (requiring the production of
“[e]xculpatory and impeachment information that casts doubt upon proof of an
aggravating factor at sentencing” when the presentence investigation begins).
Because at some point in a federal prosecution “the government would have to
search the files of all members of the prosecution team for potentially
exculpatory material,” DOJ Br. 16, there is little added burden of requiring
that production at an earlier point in the case.
      For all these reasons, there is little evidence suggesting that our court’s
following the Brady rule that many other jurisdictions already apply would




                                       52
    Case: 16-40772       Document: 00514646077          Page: 53     Date Filed: 09/18/2018



                                       No. 16-40772
create any meaningful obstacle to plea bargaining. 8 But even if it did, query
whether a system in which 97% of defendants plead guilty is already placing
to great a premium on the need for speedy pleas at the expense of the truth-
finding function of the courts. See BIBAS, Plea Bargaining’s Role in Wrongful
Convictions, at 157 (critiquing modern plea bargaining because it “put[s]
efficiency ahead of accuracy”).
       That leaves United States v. Ruiz, 536 U.S. 622 (2002). It held the
government is not required to disclose “impeachment information relating to
any informants or other witnesses” prior to entering a plea agreement. Id. at
625. Ruiz did not present the question of exculpatory evidence because the
government agreed in the plea agreement to turn over “any [known]
information establishing the factual innocence of the defendant.” 9 Id. at 625;
see also id. at 629 (“We must decide whether the Constitution requires that
preguilty plea disclosure of impeachment information.”). Indeed, in conducting
a due process balancing test to determine whether there was a right to pre-
plea impeachment evidence, the Court explained that the agreement to give
Ruiz exculpatory evidence “diminish[ed]” the risk that “in the absence of
impeachment information, innocent individuals, accused of crimes, w[ould]
plead guilty.” Id. at 631. If Brady does not apply as a categorical matter to
defendants who plead guilty, saying just that in Ruiz would have resulted in a
much simpler and shorter opinion. That was the approach of Justice Thomas’s



       8 A pre-plea Brady right might also apply on when the defendant requests discovery,
which would further mitigate any costs on the system. Alvarez made that request.
       9 Notably, the federal government asked the Court to decide the broader question of

whether defendants who plead have a right to exculpatory information. Brief for the United
States, United State v. Ruiz, at I (“Questions Presented: 1. Whether before pleading guilty, a
criminal defendant has a constitutional right to obtain material exculpatory information,
including impeachment information, from the prosecution.”). But the Court did not accept
that invitation.
                                             53
   Case: 16-40772     Document: 00514646077      Page: 54   Date Filed: 09/18/2018



                                  No. 16-40772
one-paragraph concurring opinion that no other justice joined. See id. at 633–
34 (Thomas, J., concurring).
      Instead the Court applied the balancing test. On the benefit side of that
equation, it explained that impeachment evidence has value in terms of the
“fairness of a trial” but not to whether a plea was knowing and intelligent. Id.
at 629.    Impeachment evidence is not “critical information,” it further
explained, as its relevance may become clear only in the context of a trial. Id.
at 630. Until trial, for example, a defendant may not know if the government
will call the witness who has the credibility problems.          The less direct
connection of impeachment evidence to the ultimate “guilt or innocence”
question is reflected in the fact that it took nearly a decade for the Supreme
Court to confirm that Brady included an obligation to disclose even at trial
“evidence affecting [witness] credibility.” Giglio v. United States, 405 U.S. 150,
154 (1972). Exculpatory evidence—that which goes directly to the “factual
innocence of the defendant,” Ruiz, 536 U.S. at 631, and is valuable on its face
without requiring independent knowledge of the prosecutor’s trial strategy—
has much greater value as Ruiz recognizes when it observes that its disclosure
meant there was not much additional benefit to be gained from also disclosing
impeachment evidence before a plea. Id. at 631. Production of exculpatory
evidence provides a greater safeguard against innocent defendants pleading
guilty, both because it informs innocent defendants they have a substantial
chance of showing their innocence at trial as opposed to just casting doubt on
government witnesses and because prosecutors required to provide such
evidence lose the incentive to push for guilty pleas to obscure weak cases. See
Huebler, 275 P.3d at 97–98 (“While the value of impeachment information may
depend on innumerable variables that primarily come into play at trial and
therefore arguably make it less than critical information in entering a guilty
                                       54
    Case: 16-40772    Document: 00514646077       Page: 55   Date Filed: 09/18/2018



                                  No. 16-40772
plea, the same cannot be said of exculpatory information, which is special not
just in relation to the fairness of a trial but also in relation to whether a guilty
plea is valid and accurate.”).
      That latter point recognizes a serious risk of requiring Brady disclosures
only when a case is tried: it incentivizes prosecutors to offer favorable pleas in
cases with exculpatory evidence. That is already the type of case in which a
prosecutor’s desire for a plea agreement is strongest. Bibas, Plea Bargaining
in the Shadow of Trial, supra, at 2473 (explaining that self-interest leads
prosecutors to “make irresistible offers in weak cases”). Without a Brady
requirement, there is an additional benefit from pleading out a weak case: the
plea prevents the defendant from being able to undo the conviction if he later
discovers that the government possessed exculpatory evidence. Sanchez, 50
F.3d at 1435 (“[I]f a defendant may not raise a Brady claim after a guilty plea,
prosecutors may be tempted to deliberately withhold exculpatory information
as part of an attempt to elicit guilty pleas.”); see also United States v. Fisher,
711 F.3d 460, 469 (4th Cir. 2013); United States v. Nelson, 979 F. Supp. 2d 123,
130 (D.D.C. 2013). This is on top of the interest prosecutors already have to
resolve their weakest cases with a plea agreement.
      The cost side of the Ruiz balancing inquiry is also less favorable to the
government when it comes to exculpatory evidence. The primary problem the
Court saw with pre-plea disclosure of Giglio evidence was requiring the
government to identify the witnesses it would call at a trial that would never
happen because of the plea. This interfered with the rules governing disclosure
of witnesses, posed risks of revealing the identities of informants and
undercover agents, and eliminated some of the time savings that pleas
typically bring by avoiding trial prep.        Ruiz, 536 at 631–32.        Indeed,
prosecutors often do not even learn about credibility problems with
                                        55
   Case: 16-40772    Document: 00514646077      Page: 56   Date Filed: 09/18/2018



                                 No. 16-40772
witnesses—by running criminal background checks for example—until they
have come up with their witness list. In contrast, prosecutors generally are
aware of any evidence they possess that suggests a defendant’s innocence by
the time they enter into plea negotiations if not earlier when they bring
charges.
      The final proof that Ruiz did not decide the question of pre-plea
disclosure of exculpatory evidence—and that the result might be different for
this category—are the cases that have come after it. Soon after Ruiz, the
Seventh Circuit predicted that “it is highly likely that the Supreme Court
would find a violation of the Due Process Clause if prosecutors or other
relevant government actors have knowledge of a criminal defendant’s factual
innocence but fail to disclose such information to a defendant before he enters
into a guilty plea.” McCann v. Mangialardi, 337 F.3d 782, 788 (7th Cir. 2003).
It recognized that “Ruiz indicates a significant distinction between
impeachment information and exculpatory evidence of actual innocence,”
though the Seventh Circuit did not ultimately decide the question because
there was insufficient evidence that the government suppressed the evidence
in that case. Id. at 787. The Tenth Circuit, again noting a critical distinction
between exculpatory evidence and the impeachment evidence in Ruiz, did
decide the question in favor of a right of pleading defendants to exculpatory
evidence. See United States v. Ohiri, 133 F. App’x 555, 562 (10th Cir. 2005).
So have a number of federal district courts. Nelson, 979 F. Supp. 2d at 130
(“[I]n light of the balance of circuit court precedent and the purpose of Brady,
Nelson can assert his Brady claim to argue that his guilty plea was not
knowing and voluntary”); United States v. Danzi, 726 F. Supp. 2d 120, 128 (D.
Conn. 2010) (declining “the Government’s invitation to hold that Ruiz applies
to exculpatory as well as impeachment material”); Ollins v. O’Brien, 2005 WL
                                      56
    Case: 16-40772       Document: 00514646077          Page: 57     Date Filed: 09/18/2018



                                       No. 16-40772
730987, *11 (N.D. Ill. 2005) (“[T]he Court finds the Ruiz distinction . . .
persuasive and holds that due process requires the disclosure of information of
factual innocence during the plea bargaining process.”). To be sure, other
courts of appeals, while recognizing that Ruiz did not decide the question, have
read it as casting doubt on the existence of a pre-plea right even to exculpatory
evidence though none has done as we have and actually rejected that right.
Friedman v. Rehal, 618 F.3d 142, 154 (2d Cir. 2010) (explaining that “Ruiz did
not expressly abrogate [its prior caselaw] as applied to all Brady material” but
noting it creates uncertainty about whether exculpatory material needed to be
produced pre-plea); United States v. Moussaoui, 591 F.3d 263, 285 (4th Cir.
2010), as amended (Feb. 9, 2010) 10; cf. United States v. Mathur, 624 F.3d 498,
507 (1st Cir. 2010) (emphasizing Brady is a trial right and observing “[t]he
Ruiz Court evinced a reluctance to extend a Brady-like right to the realm of
pretrial plea negotiations” in a case when a defendant went to trial but argued
that if he had been provided exculpatory material before trial he would have
pleaded guilty).
       And we should not make the common mistake of treating federal
decisions as the universe of caselaw on this issue. Our state court peers also
interpret the federal Constitution. Four state supreme courts have held since
Ruiz that the federal Brady right applies to exculpatory evidence at the plea
phase, and the Texas Court of Criminal Appeals has reaffirmed its long ago
adoption of that view.        Buffey, 782 S.E.2d at 216 (“[T]he better-reasoned
authority supports the conclusion that a defendant is constitutionally entitled



       10 In a more recent decision the Fourth Circuit allowed a defendant to vacate a guilty
plea when he later learned that law enforcement had lied in applying for a search warrant
that led to evidence of guilt. Fisher, 711 F.3d at 460. It did so not on Brady grounds, but on
the ground that the suppression of that information made the plea unknowing. Id. at 471.
                                             57
   Case: 16-40772     Document: 00514646077      Page: 58   Date Filed: 09/18/2018



                                  No. 16-40772
to exculpatory evidence during the plea negotiation stage.”); Hyman, 723
S.E.2d at 380 (noting that an applicant can challenge the “voluntary nature of
a guilty plea” by asserting a Brady violation); Huebler, 275 P.3d at 96–97
(concluding that “the due-process calculus also weighs in favor of the added
safeguard of requiring the State to disclose material exculpatory information
before the defendant enters a guilty plea”); Medel, 184 P.3d at 1235 (providing
the requirements for a guilty plea to be rendered involuntary based on a Brady
violation); Johnson, 2009 WL 1396807, at *1; (vacating a guilty plea because
of a Brady violation); id. at *1–*2 (Cochran, J. concurring) (explaining that
“Ruiz, by its terms, applies only to material impeachment evidence”); see also
State v. Kenner, 900 So. 2d 948, 952–53 (La. App. 4 Cir. 2005), reversed on other
grounds, 917 So. 2d 1081 (La. 2005). No state high court has ruled the other
way. See WAYNE LAFAVE, ET AL. 5 CRIM. PROC. § 21.3(c) (4th ed. 2015) (noting
that “certainly the better view” is of those courts that require Brady disclosure
of exculpatory evidence to defendants who plead).
        The facts from one of those state court cases highlights the stakes of
this issue and the dynamics that can lead an innocent person to plead guilty.
Joseph Buffey was 19 when he was arrested for three breaking-and-entering
offenses of businesses. Buffey, 782 S.E.2d at 207. The week before his arrest,
an intruder had robbed and brutally raped an 83-year-old woman in the same
town. Id. at 206. During an interrogation that lasted nine hours, Buffey at
first repeatedly denied that he committed the robbery and sexual assault. Id.
at 207. Hours into the questioning, and past 3:00 in the morning, he told the
officers he had broken into “[t]his old lady’s house” but said he could not recall
any assault. Id. When the officers later told him he should be able to recall
more details, Buffey recanted saying “You really want to know the truth? . . . I
didn’t do it.” Id. He explained that he had only confessed to breaking into the
                                       58
   Case: 16-40772     Document: 00514646077     Page: 59   Date Filed: 09/18/2018



                                 No. 16-40772
house because an officer was “breathing down my neck” and “I couldn’t tell you
what went on in there.” Id.
      After Buffey was charged with the rape, the state forensic lab tested
DNA from the victim’s rape kit. Id. at 208. It issued a report stating that
“assuming there are onl

[...TRUNCATED 4856 of 124856 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Anderson v. Creighton.md  (`case`, 5 assertions)

### content_page

```
---
title: Anderson v. Creighton
type: case
citation: "483 U.S. 635 (1987)"
parallel_cite: "107 S. Ct. 3034; 97 L. Ed. 2d 523; 55 U.S.L.W. 5092"
neutral_cite: 1987 U.S. LEXIS 2894
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-06-25
docket: 85-1520
authority_weight: "Binding — SCOTUS"
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
  opinion_url: "https://www.courtlistener.com/opinion/111953/anderson-v-creighton/"
  cluster_id: 111953
  opinion_id: null
  identity_checked: true
lake:
  record_id: Anderson v. Creighton
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Foundational (clearly-established at the appropriate level of particularity)"
related:
  - "[[White v. Pauly]]"
  - "[[Harlow v. Fitzgerald]]"
  - "[[Malley v. Briggs]]"
  - "[[Ashcroft v. al-Kidd]]"
  - "[[Pearson v. Callahan]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - fourth-amendment
  - qualified-immunity
  - section-1983
  - clearly-established-law
  - warrantless-search
  - bivens
holding: "A government official sued for a constitutional violation keeps qualified immunity unless the right was clearly established in a particularized sense — its contours sufficiently clear that a reasonable official would understand his conduct violates it; for a warrantless search the dispositive inquiry is the objective, fact-specific question whether a reasonable officer could have believed the search lawful in light of clearly established law and the information the officers possessed."
---

# Anderson v. Creighton

*483 U.S. 635 (1987)* (No. 85-1520) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 111953 → 483 U.S. 635, No. 85-1520, decided 1987-06-25 (Scalia, J.); Rule/Application quotes string-matched to the CL opinion text 2026-07-07. -->

## Background
On November 11, 1983, FBI agent Russell Anderson led a warrantless search of the Creighton family's home, looking for Vadaain Dixon, a bank-robbery suspect who was not there. The Creightons sued Anderson for money damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging a Fourth Amendment violation. Anderson sought summary judgment on [[Qualified Immunity|qualified immunity]]. The District Court granted it (finding probable cause and [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]), but the Eighth Circuit reversed, holding that the right to be free of a warrantless home search absent probable cause and [[Exigent Circumstances and Hot Pursuit|exigency]] was "clearly established," so Anderson could claim no immunity. The Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
At what level of generality must a right be "clearly established" before an officer loses [[Qualified Immunity|qualified immunity]] — and, for a warrantless search, whether the officer may still prevail by showing that a reasonable officer could have believed the search lawful.

## Rule
[[Qualified Immunity|Qualified immunity]] turns on whether the right was clearly established at a **particularized** level, not an abstract one. Writing for the Court, Justice Scalia held that "the right the official is alleged to have violated must have been 'clearly established' in a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right." — 483 U.S. at 640. It is not necessary that "the very action in question ha[ve] previously been held unlawful," "but it is to say that in the light of pre-existing law the unlawfulness must be apparent." — *Id.* ^pin-640

## Application
The Eighth Circuit erred by pitching the right at too high a level of generality — a general right against warrantless home searches lacking probable cause and [[Exigent Circumstances and Hot Pursuit|exigency]]. Framed correctly, the inquiry is fact-specific: "The relevant question in this case, for example, is the objective (albeit fact-specific) question whether a reasonable officer could have believed Anderson's warrantless search to be lawful, in light of clearly established law and the information the searching officers possessed. Anderson's subjective beliefs about the search are irrelevant." — 483 U.S. at 641. [[Reading and Citing Cases#on-remand|On remand]] Anderson was entitled to argue that, as a matter of law, a reasonable officer could have thought the search lawful. ^pin-641

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]].** Scalia, J., wrote for the Court; Stevens, J., dissented (joined by Brennan and Marshall, JJ.). Anderson could press his qualified-immunity defense on the objective-reasonableness standard.

## Treatment & subsequent history
**Good law — foundational.** *Anderson* is the decision that fixed [[Qualified Immunity|qualified immunity]]'s "clearly established" inquiry at a particularized level of generality, and it is the direct antecedent the corpus reaches through *[[White v. Pauly]]* — where the Court again warned that clearly established law must not be defined "at a high level of generality." The particularization principle runs through *[[Ashcroft v. al-Kidd]]* and *[[Mullenix v. Luna]]* and remains the governing frame today.

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 111953 + 483 U.S. 635); renders under the ⚪ banner until S9 promotion. *Mitchell v. Forsyth*, cited in the opinion, is not yet in the corpus and is named in plain text to avoid a dangling link.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Foundational (clearly-established at the appropriate level of [[Particularity|particularity]])*

## Sources
- [*Anderson v. Creighton*, 483 U.S. 635 (1987)](https://www.courtlistener.com/opinion/111953/anderson-v-creighton/) — pinpoints: 640 (particularized "clearly established" standard; Scalia, J.), 641 (objective reasonable-officer question); quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "199a4c6e4827d9a0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "483 U.S. 635 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 2894", "official_citation_present": true, "parallel_cite": "107 S. Ct. 3034; 97 L. Ed. 2d 523; 55 U.S.L.W. 5092", "title": "Anderson v. Creighton", "year": "1987"}}
{"assertion_id": "604241a4a1011ad6", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Foundational (clearly-established at the appropriate level of particularity)", "title": "Anderson v. Creighton"}}
{"assertion_id": "7d82dec406b45e2c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A government official sued for a constitutional violation keeps qualified immunity unless the right was clearly established in a particularized sense — its contours sufficiently clear that a reasonable official would understand his conduct violates it; for a warrantless search the dispositive inquiry is the objective, fact-specific question whether a reasonable officer could have believed the search lawful in light of clearly established law and the information the officers possessed.", "title": "Anderson v. Creighton"}}
{"assertion_id": "39a10a4052720d76", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Anderson v. Creighton", "varies_by_point": "false"}}
{"assertion_id": "b9c7484ea7e5038c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Anderson v. Creighton"}}
```

### lake record — Anderson v. Creighton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Anderson v. Creighton",
  "status": "under_review",
  "identity": {
    "case_name": "Anderson v. Creighton",
    "case_name_short": "Anderson",
    "case_name_full": "ANDERSON v. CREIGHTON Et Al.",
    "input_case_name": "Anderson v. Creighton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-06-25",
    "year": 1987,
    "docket": "85-1520",
    "cluster_id": 111953,
    "lead_opinion_id": 9431119,
    "sibling_ids": [],
    "absolute_url": "/opinion/111953/anderson-v-creighton/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "483 U.S. 635",
      "volume": "483",
      "reporter": "U.S.",
      "page": "635",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 3034",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 523",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5092",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5092",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 2894",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2894",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "483 U.S. 635",
        "volume": "483",
        "reporter": "U.S.",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 3034",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "3034",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 L. Ed. 2d 523",
        "volume": "97",
        "reporter": "L. Ed. 2d",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 2894",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "2894",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 5092",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "5092",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "483 U.S. 635",
    "official_selection": {
      "court_class": "scotus",
      "selected": "483 U.S. 635",
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
    "date_created": "2026-07-08T00:38:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "W10 on-read identity re-verification 2026-07-07: docket 85-1520 confirmed verbatim from CL lead-opinion caption (html_with_citations)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T00:38:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "anderson-v-creighton--111953",
      "to_record_id": "Anderson v. Creighton",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Anderson v. Creighton

```
<opinion type="majority">
<author id="b686-10">Justice Scalia</author>
<p id="Av4Q">delivered the opinion of the Court.</p>
<p id="b686-11">The question presented is whether a federal law enforcement officer who participates in a search that violates the Fourth Amendment may be held personally liable for money <page-number citation-index="1" label="637">*637</page-number>damages if a reasonable officer could have believed that the search comported with the Fourth Amendment.</p>
<p id="b687-5">I</p>
<p id="b687-6">Petitioner Russell Anderson is an agent of the Federal Bureau of Investigation. On November 11, 1983, Anderson and other state and federal law enforcement officers conducted a warrantless search of the home of respondents, the Creighton family. The search was conducted because Anderson believed that Vadaain Dixon, a man suspected of a bank robbery committed earlier that day, might be found there. He was not.</p>
<p id="b687-7">The Creightons later filed suit against Anderson in a Minnesota state court, asserting among other things a claim for money damages under the Fourth Amendment, see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).<footnotemark>1</footnotemark> After removing the suit to Federal District Court, Anderson filed a motion to dismiss or for summary judgment, arguing that the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>claim was barred by Anderson’s qualified immunity from civil damages liability. See <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982). Before any discovery took place, the District Court granted summary judgment on the ground that the search was lawful, holding that the undisputed facts revealed that Anderson had had probable cause to search the Creighton’s home and that his failure to obtain a warrant was justified by the presence of exigent circumstances. App. to Pet. for Cert. 23a-25a.</p>
<p id="b687-8">The Creightons appealed to the Court of Appeals for the Eighth Circuit, which reversed. <em>Creighton </em>v. <em>St. Paul, </em><span class="citation multiple-matches"><a href="/c/F.%202d/766/1269/">766 F. 2d 1269</a></span> (1985). The Court of Appeals held that the issue of the lawfulness of the search could not properly be decided on summary judgment, because unresolved factual disputes <page-number citation-index="1" label="638">*638</page-number>made it impossible to determine as a matter of law that the warrantless search had been supported by probable cause and exigent circumstances. <em>Id., </em>at 1272-1276. The Court of Appeals also held that Anderson was not entitled to summary judgment on qualified immunity grounds, since the right Anderson was alleged to have violated — the right of persons to be protected from warrantless searches of their home unless the searching officers have probable cause and there are exigent circumstances — was clearly established. <em>Ibid.</em></p>
<p id="b688-5">Anderson filed a petition for certiorari, arguing that the Court of Appeals erred by refusing to consider his argument that he was entitled to summary judgment on qualified immunity grounds if he could establish as a matter of law that a reasonable officer could have believed the search to be lawful. We granted the petition, <span class="citation multiple-matches"><a href="/c/U.%20S./478/1003/">478 U. S. 1003</a></span> (1986), to consider that important question.</p>
<p id="b688-6">II</p>
<p id="b688-7">When government officials abuse their offices, “action[s] for damages may offer the only realistic avenue for vindication of constitutional guarantees.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 814</a></span>. On the other hand, permitting damages suits against government officials can entail substantial social costs, including the risk that fear of personal monetary liability and harassing litigation will unduly inhibit officials in the discharge of their duties. <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Ibid.</a></span> </em>Our cases have accommodated these conflicting concerns by generally providing government officials performing discretionary functions with a qualified immunity, shielding them from civil damages liability as long as their actions could reasonably have been thought consistent with the rights they are alleged to have violated. See, <em>e. g., Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 341</a></span> (1986) (qualified immunity protects “all but the plainly incompetent or those who knowingly violate the law”); <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>id., </em>at 344-345</a></span> (police officers applying for warrants are immune if a <page-number citation-index="1" label="639">*639</page-number>reasonable officer could have believed that there was probable cause to support the application); <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#528" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511, 528</a></span> (1985) (officials are immune unless “the law clearly proscribed the actions” they took); <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#191" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183, 191</a></span> (1984); <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#198" aria-description="Citation for case: Davis v. Scherer"><em>id., </em>at 198</a></span> (Brennan, J., concurring in part and dissenting in part); <em>Harlow </em>v. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Fitzgerald, supra, </em>at 819</a></span>. Cf., <em>e. g., Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 562</a></span> (1978). Somewhat more concretely, whether an official protected by qualified immunity may be held personally liable for an allegedly unlawful official action generally turns on the “objective legal reasonableness” of the action, <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 819</a></span>, assessed in light of the legal rules that were “clearly established” at the time it was taken, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald"><em>id., </em>at 818</a></span>.</p>
<p id="b689-5">The operation of this standard, however, depends substantially upon the level of generality at which the relevant “legal rule” is to be identified. For example, the right to due process of law is quite clearly established by the Due Process Clause, and thus there is a sense in which any action that violates that Clause (no matter how unclear it may be that the particular action is a violation) violates a clearly established right. Much the same could be said of any other constitutional or statutory violation. But if the test of “clearly established law” were to be applied at this level of generality, it would bear no relationship to the “objective legal reasonableness” that is the touchstone of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>. </em>Plaintiffs would be able to convert the rule of qualified immunity that our cases plainly establish into a rule of virtually unqualified liability simply by alleging violation of extremely abstract rights. <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>would be transformed from a guarantee of immunity into a rule of pleading. Such an approach, in sum, would destroy “the balance that our cases strike between the interests in vindication of citizens’ constitutional rights and in public officials’ effective performance of their.duties,” by making it impossible for officials “reasonably [to] anticipate when their conduct may give rise to liability for damages.” <em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/" aria-description="Citation for case: Davis v. Scherer">Davis</a></span>, </em><page-number citation-index="1" label="640">*640</page-number><em>swpra </em>at 195.<footnotemark>2</footnotemark> It should not be surprising, therefore, that our cases establish that the right the official is alleged to have violated must have been “clearly established” in a more particularized, and hence more relevant, sense: The contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, see <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#535" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 535, n. 12</a></span>; but it is to say that in the light of pre-existing law the unlawfulness must be apparent. See, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>e. g., Malley, supra, </em>at 344-345</a></span>; <span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#528" aria-description="Citation for case: Mitchell v. Forsyth"><em>Mitchell, supra, </em>at 528</a></span>; <span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#191" aria-description="Citation for case: Davis v. Scherer"><em>Davis, supra, </em>at 191, 195</a></span>.</p>
<p id="b690-5">Anderson contends that the Court of Appeals misapplied these principles. We agree. The Court of Appeals’ brief discussion of qualified immunity consisted of little more than an assertion that a general right Anderson was alleged to have violated — the right to be free from warrantless searches of one’s home unless the searching officers have probable cause and there are exigent circumstances — was clearly established. The Court of Appeals specifically refused to consider the argument that it was <em>not </em>clearly established that the circumstances with which Anderson was confronted did <page-number citation-index="1" label="641">*641</page-number>not constitute probable cause and exigent circumstances. The previous discussion should make clear that this refusal was erroneous. It simply does not follow immediately from the conclusion that it was firmly established that warrantless searches not supported by probable cause and exigent circumstances violate the Fourth Amendment that Anderson’s search was objectively legally unreasonable. We have recognized that it is inevitable that law enforcement officials will in some cases reasonably but mistakenly conclude that probable cause is present, and we have indicated that in such cases those officials — like other officials who act in ways they reasonably believe to be lawful — should not be held personally liable. See <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#344" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 344-345</a></span>. The same is true of their conclusions regarding exigent circumstances.</p>
<p id="b691-5">It follows from what we have said that the determination whether it was objectively legally reasonable to conclude that a given search was supported by probable cause or exigent circumstances will often require examination of the information possessed by the searching officials. But contrary to the Creightons’ assertion, this does not reintroduce into qualified immunity analysis the inquiry into officials’ subjective intent that <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>sought to minimize. See <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 815-820</a></span>. The relevant question in this case, for example, is the objective (albeit fact-specific) question whether a reasonable officer could have believed Anderson’s warrantless search to be lawful, in light of clearly established law and the information the searching officers possessed. Anderson’s subjective beliefs about the search are irrelevant.</p>
<p id="b691-6">The principles of qualified immunity that we reaffirm today require that Anderson be permitted to argue that he is entitled to summary judgment on the ground that, in light of the clearly established principles governing warrantless searches, he could, as a matter of law, reasonably have believed that the search of the Creightons’ home was lawful.<footnotemark>3</footnotemark></p>
<p id="b692-4"><page-number citation-index="1" label="642">*642</page-number>Ill</p>
<p id="b692-5">In addition to relying on the reasoning of the Court of Appeals, the Creightons advance three alternative grounds for affirmance. All of these take the same form, <em>i. e., </em>that even if Anderson is entitled to qualified immunity under the usual principles of qualified immunity law we have just described, an exception should be made to those principles in the circumstances of this case. We note at the outset the heavy burden this argument must sustain to be successful. We have emphasized that the doctrine of qualified immunity reflects a balance that has been struck “across the board,” <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#821" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 821</a></span> (Brennan, J., concurring). See also <em>Malley, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S., at 340</a></span> (“ ‘For executive officers in general, . . . qualified immunity represents the norm’ ” (quoting <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 807</a></span>)).<footnotemark>4</footnotemark> Although we have in narrow circumstances provided officials with an absolute immunity, see, <page-number citation-index="1" label="643">*643</page-number><em>e. g., Nixon </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428860"><a href="/opinion/110762/nixon-v-fitzgerald/" aria-description="Citation for case: Nixon v. Fitzgerald">457 U. S. 731</a></span> (1982), we have been unwilling to complicate qualified immunity analysis by making the scope or extent of immunity turn on the precise nature of various officials’ duties or the precise character of the particular rights alleged to have been violated. An immunity that has as many variants as there are modes of official action and types of rights would not give conscientious officials that assurance of protection that it is the object of the doctrine to provide. With that observation in mind, we turn to the particular arguments advanced by the Creightons.</p>
<p id="b693-5">First, and most broadly, the Creightons argue that it is inappropriate to give officials alleged to have violated the Fourth Amendment — and thus necessarily to have <em>unreasonably </em>searched or seized — the protection of a qualified immunity intended only to protect reasonable official action. It is not possible, that is, to say that one “reasonably” acted unreasonably. The short answer to this argument is that it is foreclosed by the fact that we have previously extended qualified immunity to officials who were alleged to have violated the Fourth Amendment. See <em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">Malley, supra</a></span> </em>(police officers alleged to have caused an unconstitutional arrest); <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511</a></span> (1985) (officials alleged to have conducted warrantless wiretaps). Even if that were not so, however, we would still find the argument unpersuasive. Its surface appeal is attributable to the circumstance that the Fourth Amendment’s guarantees have been expressed in terms of “unreasonable” searches and seizures. Had an equally serviceable term, such as “undue” searches and seizures been employed, what might be termed the “reasonably unreasonable” argument against application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>to the Fourth Amendment would not be available — just as it <em>would </em>be available against application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>to the Fifth Amendment if the term “reasonable process of law” had been employed there. The fact is that, regardless of the terminology used, the precise content of most of the Constitution’s <page-number citation-index="1" label="644">*644</page-number>civil-liberties guarantees rests upon an assessment of what accommodation between governmental need and individual freedom is reasonable, so that the Creightons’ objection, if it has any substance, applies to the application of <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>generally. We have frequently observed, and our many cases on the point amply demonstrate, the difficulty of determining whether particular searches or seizures comport with the Fourth Amendment. See, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs"><em>e. g., Malley, supra, </em>at 341</a></span>. Law enforcement officers whose judgments in making these difficult determinations are objectively legally reasonable should no more be held personally liable in damages than should officials making analogous determinations in other areas of law.</p>
<p id="b694-5">For the same reasons, we also reject the Creightons’ narrower suggestion that we overrule <em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">Mitchell, supra</a></span> </em>(extending qualified immunity to officials who conducted warrantless wiretaps), by holding that qualified immunity may never be extended to officials who conduct unlawful warrant-less searches.</p>
<p id="b694-6">Finally, we reject the Creightons’ narrowest and most Procrustean proposal: that no immunity should be provided to police officers who conduct unlawful warrantless searches of innocent third parties’ homes in search of fugitives. They rest this proposal on the assertion that officers conducting such searches were strictly liable at English common law if the fugitive was not present. See, <em>e. g., Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765). Although it is true that we have observed that our determinations as to the scope of official immunity are made in the light of the “common-law tradition,”<footnotemark>5</footnotemark> <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#342" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 342</a></span>, <page-number citation-index="1" label="645">*645</page-number>we have never suggested that the precise contours of official immunity can and should be slavishly derived from the often arcane rules of the common law. That notion is plainly contradicted by <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span>, </em>where the Court completely reformulated qualified immunity along principles not at all embodied in the common law, replacing the inquiry into subjective malice so frequently required at common law with an objective inquiry into the legal reasonableness of the official action. See <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 815-820</a></span>. As we noted before, <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>clearly expressed the understanding that the general principle of qualified immunity it established would be applied “across the board.”</p>
<p id="b695-5">The approach suggested by the Creightons would introduce into qualified immunity analysis a complexity rivaling that which we found sufficiently daunting to deter us from tailoring the doctrine to the nature of officials’ duties or of the rights allegedly violated. See <em>supra, </em>at 642-643. Just in the field of unlawful arrests, for example, a cursory examination of the Restatement (Second) of Torts (1965) suggests that special exceptions from the general rule of qualified immunity would have to be made for arrests pursuant to a warrant but outside the jurisdiction of the issuing authority, §§ 122, 129(a), arrests after the warrant had lapsed, §§ 122, 130(a), and arrests without a warrant, § 121. Both the complexity and the unsuitability of this approach are betrayed by the fact that the Creightons’ proposal itself does not actually apply the musty rule that is purportedly its justification but instead suggests an exception to qualified immunity for all fugitive searches of third parties’ dwellings, and not merely (as the English rule appears to have provided) for all <em>unsuccessful </em>fugitive searches of third parties’ dwellings. Moreover, from the sources cited by the Creightons it appears to have been a corollary of the English rule that where the search <em>was </em>successful, no civil action would lie, whether or not probable cause for the search existed. That also is (quite pru<page-number citation-index="1" label="646">*646</page-number>dently but quite illogically) not urged upon us in the Creightons’ selective use of the common law.</p>
<p id="b696-5">The general rule of qualified immunity is intended to provide government officials with the ability “reasonably [to] anticipate when their conduct may give rise to liability for damages.” <em>Davis, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/#195" aria-description="Citation for case: Davis v. Scherer">468 U. S., at 195</a></span>. Where that rule is applicable, officials can know that they will not be held personally liable as long as their actions are reasonable in light of current American law. That security would be utterly defeated if officials were unable to determine whether they were protected by the rule without entangling themselves in the vagaries of the English and American common law. We are unwilling to Balkanize the rule of qualified immunity by carving exceptions at the level of detail the Creightons propose. We therefore decline to make an exception to the general rule of qualified immunity for cases involving allegedly unlawful warrantless searches of innocent third parties’ homes in search of fugitives.</p>
<p id="b696-6">For the reasons stated, we vacate the judgment of the Court of Appeals and remand the case for further proceedings consistent with this opinion.<footnotemark>6</footnotemark></p>
<p id="b696-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b687-9"> The Creightons also named other defendants and advanced various other claims against both Anderson and the other defendants. Only the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>claim against Anderson remains at issue in this case, however.</p>
</footnote>
<footnote label="2">
<p id="b690-6"> The dissent, which seemingly would adopt this approach, seeks to avoid the unqualified liability that would follow by advancing the suggestion that officials generally (though not law enforcement officials, see <em>post, </em>at 654, 661-662, and officials accused of violating the Fourth Amendment, see <em>post, </em>at 659-667) be permitted to raise a defense of reasonable good faith, which apparently could be asserted and proved only at trial. See <em>post, </em>at 653. But even when so modified (and even for the fortunate officials to whom the modification applies) the approach would totally abandon the concern — which was the driving force behind Harlow’s substantial reformulation of qualified-immunity principles — that “insubstantial claims” against government officials be resolved prior to discovery and on summary judgment if possible. <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818-819</a></span>. A passably clever plaintiff would always be able to identify an abstract clearly established right that the defendant could be alleged to have violated, and the good-faith defense envisioned by the dissent would be available only at trial.</p>
</footnote>
<footnote label="3">
<p id="b691-7"> The Creightons argue that the qualified immunity doctrine need not be expanded to apply to the circumstances of this case, because the Federal <page-number citation-index="1" label="642">*642</page-number>Government and various state governments have established programs through which they reimburse officials for expenses and liability incurred in suits challenging actions they have taken in their official capacities. Because our holding today does not extend official qualified immunity beyond the bounds articulated in <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>and our subsequent cases, an argument as to why we should not do so is beside the point. Moreover, even assuming that conscientious officials care only about their personal liability and not the liability of the government they serve, the Creightons do not and could not reasonably contend that the programs to which they refer make reimbursement sufficiently certain and generally available to justify reconsideration of the balance struck in <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>and subsequent cases. See <span class="citation no-link">28 CFR § 50.15</span>(c) (1987) <em>(permitting </em>reimbursement of Department of Justice employees when the Attorney General finds reimbursement appropriate); 5 F. Harper, F. James, &amp; O. Gray, Law of Torts § 29.9, n. 20 (2d ed. 1986) (listing various state programs).</p>
</footnote>
<footnote label="4">
<p id="b692-10"> These decisions demonstrate the emptiness of the dissent’s assertion that “[tjoday this Court makes the fundamental error of simply assuming that <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>immunity is just as appropriate for federal law enforcement officers ... as it is <em>for </em>high <em>government </em>officials.” <em>Post, at 654 (footnote </em>omitted). Just last Term the Court unanimously held that state and federal law enforcement officers were protected by the qualified immunity described in <em>Harlow. Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335</a></span> (1986). We see no reason to overrule that holding.</p>
</footnote>
<footnote label="5">
<p id="b694-7"> Of course, it is the American rather than the English common-law tradition that is relevant, cf. <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 340-342</a></span>; and the American rule appears to have been considerably less draconian than the English. See Restatement (Second) of Torts §§ 204, 206 (1965) (officers with an arrest warrant are privileged to enter a third party’s house to effect arrest if they reasonably believe the fugitive to be there).</p>
</footnote>
<footnote label="6">
<p id="b696-8"> Noting that no discovery has yet taken place, the Creightons renew their argument that, whatever the appropriate qualified immunity standard, some discovery would be required before Anderson’s summary judgment motion could be granted. We think the matter somewhat more complicated. One of the purposes of the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>qualified immunity standard is to protect public officials from the “broad-ranging discovery” that can be “peculiarly disruptive of effective government.” 457 U. S., at 817 (footnote omitted). For this reason, we have emphasized that qualified immunity questions should be resolved at the earliest possible stage of a litigation. <em>Id., </em>at 818. See also <em>Mitchell </em>v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/#526" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511, 526</a></span> (1986). Thus, on remand, it should first be determined whether the actions the Creightons allege Anderson to have taken are actions that a reasonable officer could have believed lawful. If they are, then Anderson is entitled to dismissal prior to discovery. Cf. <em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">ibid.</a></span> </em>If they are not, and if the actions Anderson claims he took are different from those the Creightons allege (and are actions that a reasonable officer could have believed lawful), <page-number citation-index="1" label="647">*647</page-number>then discovery may be necessary before Anderson’s motion for summary judgment on qualified immunity grounds can be resolved. Of course, any such discovery should be tailored specifically to the question of Anderson’s qualified immunity.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Andresen v. Maryland.md  (`case`, 5 assertions)

### content_page

```
---
title: "Andresen v. Maryland"
type: case
citation: "427 U.S. 463 (1976)"
parallel_cite: "96 S. Ct. 2737; 49 L. Ed. 2d 627"
neutral_cite: 1976 U.S. LEXIS 78
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-29
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-06-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Andresen v. Maryland
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109522/andresen-v-maryland/"
  cluster_id: 109522
  opinion_id: 109522
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Groh v. Ramirez]]", "[[Coolidge v. New Hampshire]]", "[[Warden v. Hayden]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "particularity", "fifth-amendment", "business-records"]
holding: "A particularized warrant to search for and seize a person's business records, and their introduction in evidence, does not violate the…"
lake:
  record_id: Andresen v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Andresen v. Maryland

*427 U.S. 463 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Maryland investigators probing a real-estate false-pretenses scheme involving the sale of "Lot 13T" obtained warrants and searched the offices of Andresen, an attorney, seizing his business records — some of which contained statements he had written. The records were introduced at trial and he was convicted of false pretenses and fraudulent misappropriation.

## Issue
(1) Whether seizing an individual's own business records under a search warrant, and introducing them at his trial, violates the Fifth Amendment privilege against self-incrimination; and (2) whether a warrant's catch-all phrase — "together with other fruits, instrumentalities and evidence of crime at this [time] unknown" — rendered it an impermissibly general warrant.

## Rule
No Fifth Amendment violation: records voluntarily created before the search are not compelled testimony. "[P]etitioner was not asked to say or to do anything. The records seized contained statements that petitioner had voluntarily committed to writing." — 427 U.S. at 473. ^pin-473

The Court therefore held: "we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that '[n]o person . . . shall be compelled in any criminal case to be a witness against himself.'" — *Id.* at 477. ^pin-477

The warrant was sufficiently particular when its catch-all phrase is read in context: "the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to 'the crime of false pretenses with respect to Lot 13T.'" — *Id.* at 480. ^pin-480

## Application
On these facts the seized records had been voluntarily committed to paper before officers arrived, Andresen was never required to say or do anything, and the documents were authenticated at trial by a handwriting expert rather than by him — so there was no compulsion and no Fifth Amendment violation. And the contested "other fruits" clause appeared at the end of a long sentence listing particular Lot-13T documents; read in that context it reached only evidence of the false-pretenses crime concerning Lot 13T, so the warrant was not a forbidden general warrant.

## Conclusion
Neither the Fifth Amendment nor the [[Particularity|particularity]] requirement was violated; the judgment of the Maryland Court of Special Appeals was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Andresen* remains the leading authority that pre-existing, voluntarily prepared business records seized under a valid warrant are not "compelled" testimony, and that a particular list of items is not made "general" by a contextually limited catch-all phrase. Compare [[Groh v. Ramirez]] (a warrant that fails altogether to describe the things to be seized is facially invalid).

## Appears on
- [[Particularity]] — *Key — Progeny / Refinement*

## Sources
- *Andresen v. Maryland*, 427 U.S. 463 (1976) — https://www.courtlistener.com/opinion/109522/andresen-v-maryland/ — pinpoints: 473, 477, 480.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "52d5b66983324d7d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "427 U.S. 463 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 78", "official_citation_present": true, "parallel_cite": "96 S. Ct. 2737; 49 L. Ed. 2d 627", "title": "Andresen v. Maryland", "year": "1976"}}
{"assertion_id": "349ee891891d7c41", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Key — Progeny / Refinement", "title": "Andresen v. Maryland"}}
{"assertion_id": "e691755f4be2edde", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A particularized warrant to search for and seize a person's business records, and their introduction in evidence, does not violate the…", "title": "Andresen v. Maryland"}}
{"assertion_id": "3a336166f565ffa6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-06-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Andresen v. Maryland", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Andresen v. Maryland", "varies_by_point": "false"}}
{"assertion_id": "6a8a2e80c2243016", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Andresen v. Maryland"}}
```

### lake record — Andresen v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Andresen v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Andresen v. Maryland",
    "case_name_short": "Andresen",
    "case_name_full": "Andresen v. Maryland",
    "input_case_name": "Andresen v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-29",
    "year": 1976,
    "docket": null,
    "cluster_id": 109522,
    "lead_opinion_id": 109522,
    "sibling_ids": [
      109522,
      9426530,
      9426531,
      9426532
    ],
    "absolute_url": "/opinion/109522/andresen-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9006080,
        "score": 10,
        "case_name": "Andresen v. Maryland"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 463",
      "volume": "427",
      "reporter": "U.S.",
      "page": "463",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2737",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 627",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 78",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "78",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 463",
        "volume": "427",
        "reporter": "U.S.",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2737",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 627",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 78",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "78",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 463",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 463",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-473",
      "page": null,
      "quote": "\u2014 rendered it an impermissibly general warrant. ## Rule No Fifth Amendment violation: records voluntarily created before the search are not compelled testimony.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-477",
      "page": null,
      "quote": "we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that '[n]o person . . . shall be compelled in any criminal case to be a witness against himself.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-480",
      "page": null,
      "quote": "the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to 'the crime of false pretenses with respect to Lot 13T.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-06-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Andresen v. Maryland",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Porath v. State",
          "cluster_id": 1770795,
          "cite": [
            "148 S.W.3d 402",
            "2004 WL 1660763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Triumph Capital Group, Inc.",
          "cluster_id": 8751433,
          "cite": [
            "211 F.R.D. 31",
            "2002 U.S. Dist. LEXIS 21615",
            "2002 WL 31487754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leon",
          "cluster_id": 111262,
          "cite": [
            "82 L. Ed. 2d 677",
            "104 S. Ct. 3405",
            "468 U.S. 897",
            "1984 U.S. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waller v. Georgia",
          "cluster_id": 111186,
          "cite": [
            "81 L. Ed. 2d 31",
            "104 S. Ct. 2210",
            "467 U.S. 39",
            "1984 U.S. LEXIS 86",
            "52 U.S.L.W. 4618",
            "10 Media L. Rep. (BNA) 1714"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orange Jell Beechum",
          "cluster_id": 358983,
          "cite": [
            "582 F.2d 898",
            "1978 U.S. App. LEXIS 8198",
            "3 Fed. R. Serv. 1185"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stenson",
          "cluster_id": 1172684,
          "cite": [
            "940 P.2d 1239"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Doe",
          "cluster_id": 111110,
          "cite": [
            "79 L. Ed. 2d 552",
            "104 S. Ct. 1237",
            "465 U.S. 605",
            "1984 U.S. LEXIS 169",
            "15 Fed. R. Serv. 1",
            "52 U.S.L.W. 4296",
            "57 A.F.T.R.2d (RIA) 1270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. City of Stockton",
          "cluster_id": 1310475,
          "cite": [
            "588 F.3d 1218",
            "2009 U.S. App. LEXIS 26799",
            "2009 WL 4641736"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Melson",
          "cluster_id": 2442934,
          "cite": [
            "638 S.W.2d 342",
            "1982 Tenn. LEXIS 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. United States",
          "cluster_id": 112123,
          "cite": [
            "101 L. Ed. 2d 184",
            "108 S. Ct. 2341",
            "487 U.S. 201",
            "1988 U.S. LEXIS 2869",
            "56 U.S.L.W. 4708",
            "25 Fed. R. Serv. 632",
            "62 A.F.T.R.2d (RIA) 5744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Willie H. Dennis",
          "cluster_id": 380192,
          "cite": [
            "625 F.2d 782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hubbell",
          "cluster_id": 1087666,
          "cite": [
            "147 L. Ed. 2d 24",
            "120 S. Ct. 2037",
            "530 U.S. 27",
            "2000 U.S. LEXIS 3768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 8934968,
          "cite": [
            "745 F.2d 733"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 8923386,
          "cite": [
            "636 F.2d 1028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matter of Vanderbilt (Rosner-Hickey)",
          "cluster_id": 2592656,
          "cite": [
            "57 N.Y.2d 66",
            "439 N.E.2d 378",
            "453 N.Y.S.2d 662",
            "1982 N.Y. LEXIS 3577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John F. Gardiner (05-1247) Ronald Lupo (05-1248)",
          "cluster_id": 795717,
          "cite": [
            "463 F.3d 445",
            "2006 U.S. App. LEXIS 23176",
            "2006 WL 2597365"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sell",
          "cluster_id": 1462347,
          "cite": [
            "470 A.2d 457",
            "504 Pa. 46",
            "1983 Pa. LEXIS 792"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Andresen v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjgzNjgwMDAwMDAmcz03NjQ3MzcmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTMmcz0xMTk2MTc0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 0,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109522 OR 9426530 OR 9426531 OR 9426532)",
    "indexed_citing_opinions": 849,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109522,
        "count": 752,
        "count_source": "search"
      },
      {
        "opinion_id": 9426530,
        "count": 109,
        "count_source": "search"
      },
      {
        "opinion_id": 9426531,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426532,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1306,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/andresen-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMTA2MTcmcz0xMDYyODQyOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109522+OR+9426530+OR+9426531+OR+9426532%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109522,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 97758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 97862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 107980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 108830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109046,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 284440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 297692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 299281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 303166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 305642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 317124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 330234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 1480134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109522,
        "cited_id": 1895902,
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
    "date_created": "2026-07-04T18:01:08Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:07:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:01:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Andresen v. Maryland

```
<div>
<center><b><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463</a></span> (1976)</b></center>
<center><h1>ANDRESEN<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 74-1646.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1976.</center>
<center>Decided June 29, 1976.</center>
CERTIORARI TO THE COURT OF SPECIAL APPEALS OF MARYLAND.
<p><span class="star-pagination">*464</span> <i>Peter C. Andresen,</i> petitioner, <i>pro se,</i> argued the cause and filed a brief.</p>
<p><i>Jon F. Oster,</i> Deputy Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>Francis B. Burch,</i> Attorney General, and <i>Clarence W. Sharp</i> and <i>Gilbert Rosenthal,</i> Assistant Attorneys General.</p>
<p><i>Deputy Solicitor General Randolph</i> argued the cause for the United States as <i>amicus curiae</i> urging affirmance. On the brief were <i>Solicitor General Bork, Deputy Solicitor</i> <span class="star-pagination">*465</span> <i>General Frey, Stuart A. Smith,</i> and <i>Edward R. Korman.</i></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the issue whether the introduction into evidence of a person's business records, seized during a search of his offices, violates the Fifth Amendment's command that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." We also must determine whether the particular searches and seizures here were "unreasonable" and thus violated the prohibition of the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>In early 1972, a Bi-County Fraud Unit, acting under the joint auspices of the State's Attorneys' Offices of Montgomery and Prince George's Counties, Md., began an investigation of real estate settlement activities in the Washington, D. C., area. At the time, petitioner Andresen was an attorney who, as a sole practitioner, specialized in real estate settlements in Montgomery County. During the Fraud Unit's investigation, his activities came under scrutiny, particularly in connection with a transaction involving Lot 13T in the Potomac Woods subdivision of Montgomery County. The investigation, which included interviews with the purchaser, the mortgage holder, and other lienholders of Lot 13T, as well as an examination of county land records, disclosed that petitioner, acting as settlement attorney, had defrauded Standard-Young Associates, the purchaser of Lot 13T. Petitioner had represented that the property was free of liens and that, accordingly, no title insurance was necessary, when in fact, he knew that there were two outstanding liens on the property. In addition, investigators <span class="star-pagination">*466</span> learned that the lienholders, by threatening to foreclose their liens, had forced a halt to the purchaser's construction on the property. When Standard-Young had confronted petitioner with this information, he responded by issuing, as an agent of a title insurance company, a title policy guaranteeing clear title to the property. By this action, petitioner also defrauded that insurance company by requiring it to pay the outstanding liens.</p>
<p>The investigators, concluding that there was probable cause to believe that petitioner had committed the state crime of false pretenses, see Md. Ann. Code, Art. 27, § 140 (1976), against Standard-Young, applied for warrants to search petitioner's law office and the separate office of Mount Vernon Development Corporation, of which petitioner was incorporator, sole shareholder, resident agent, and director. The application sought permission to search for specified documents pertaining to the sale and conveyance of Lot 13T. A judge of the Sixth Judicial Circuit of Montgomery County concluded that there was probable cause and issued the warrants.</p>
<p>The searches of the two offices were conducted simultaneously during daylight hours on October 31, 1972.<sup>[1]</sup> Petitioner was present during the search of his law office and was free to move about. Counsel for him was present during the latter half of the search. Between 2% and 3% of the files in the office were seized. A single investigator, in the presence of a police officer, conducted <span class="star-pagination">*467</span> the search of Mount Vernon Development Corporation. This search, taking about four hours, resulted in the seizure of less than 5% of the corporation's files.</p>
<p>Petitioner eventually was charged, partly by information and partly by indictment, with the crime of false pretenses, based on his misrepresentation to Standard-Young concerning Lot 13T, and with fraudulent misappropriation by a fiduciary, based on similar false claims made to three home purchasers. Before trial began, petitioner moved to suppress the seized documents. The trial court held a full suppression hearing. At the hearing, the State returned to petitioner 45 of the 52 items taken from the offices of the corporation. The trial court suppressed six other corporation items on the ground that there was no connection between them and the crimes charged. The net result was that the only item seized from the corporation's offices that was not returned by the State or suppressed was a single file labeled "Potomac Woods General." In addition, the State returned to petitioner seven of the 28 items seized from his law office, and the trial court suppressed four other law office items based on its determination that there was no connection between them and the crime charged.</p>
<p>With respect to all the items not suppressed or returned, the trial court ruled that admitting them into evidence would not violate the Fifth and Fourth Amendments. It reasoned that the searches and seizures did not force petitioner to be a witness against himself because he had not been required to produce the seized documents, nor would he be compelled to authenticate them. Moreover, the search warrants were based on probable cause, and the documents not returned or suppressed were either directly related to Lot 13T, and therefore within the express language of the warrants, or properly seized and otherwise admissible to show a pattern of <span class="star-pagination">*468</span> criminal conduct relevant to the charge concerning Lot 13T.</p>
<p>At trial, the State proved its case primarily by public land records and by records provided by the complaining purchasers, lienholders, and the title insurance company. It did introduce into evidence, however, a number of the seized items. Three documents from the "Potomac Woods General" file, seized during the search of petitioner's corporation, were admitted. These were notes in the handwriting of an employee who used them to prepare abstracts in the course of his duties as a title searcher and law clerk. The notes concerned deeds of trust affecting the Potomac Woods subdivision and related to the transaction involving Lot 13T.<sup>[2]</sup> Five items seized from petitioner's law office were also admitted. One contained information relating to the transactions with one of the defrauded home buyers. The second was a file partially devoted to the Lot 13T transaction; among the documents were settlement statements, the deed conveying the property to Standard-Young Associates, and the original and a copy of a notice to the buyer about releases of liens. The third item was a file devoted exclusively to Lot 13T. The fourth item consisted of a copy of a deed of trust, dated March 27, 1972, from the seller of certain lots in the Potomac Woods subdivision to a lienholder.<sup>[3]</sup> The fifth item contained drafts of <span class="star-pagination">*469</span> documents and memoranda written in petitioner's handwriting.</p>
<p>After a trial by jury, petitioner was found guilty upon five counts of false pretenses and three counts of fraudulent misappropriation by a fiduciary. He was sentenced to eight concurrent two-year prison terms.</p>
<p>On appeal to the Court of Special Appeals of Maryland, four of the five false-pretenses counts were reversed because the indictment had failed to allege intent to defraud, a necessary element of the state offense. Only the count pertaining to Standard-Young's purchase of Lot 13T remained. With respect to this count of false pretenses and the three counts of misappropriation by a fiduciary, the Court of Special Appeals rejected petitioner's Fourth and Fifth Amendment Claims.<sup>[4]</sup> Specifically, it held that the warrants were supported by probable cause, that they did not authorize a general search in violation of the Fourth Amendment, and that the items admitted into evidence against petitioner at trial were within the scope of the warrants or were otherwise properly seized. It agreed with the trial court that the search had not violated petitioner's Fifth Amendment rights because petitioner had not been compelled to do anything. <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/" aria-description="Citation for case: Andresen v. State">24 Md. App. 128</a></span>, <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/" aria-description="Citation for case: Andresen v. State">331 A. 2d 78</a></span> (1975).</p>
<p><span class="star-pagination">*470</span> We granted certiorari limited to the Fourth and Fifth Amendment issues. <span class="citation multiple-matches"><a href="/c/U.%20S./423/822/">423 U. S. 822</a></span> (1975).<sup>[5]</sup></p>
<p></p>
<h2>II</h2>
<p>The Fifth Amendment, made applicable to the States by the Fourteenth Amendment, <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964), provides that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." As the Court often has noted, the development of this protection was in part a response to certain historical practices, such as ecclesiastical inquisitions and the proceedings of the Star Chamber, "which placed a premium on compelling subjects of the investigation to admit guilt from their own lips." <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 440</a></span> (1974). See generally L. Levy, Origins of the Fifth Amendment (1968). The "historic function" of the privilege has been to protect a " `natural individual from compulsory incrimination through his <span class="star-pagination">*471</span> own testimony or personal records.' " <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#89" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 89-90</a></span> (1974), quoting from <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/#701" aria-description="Citation for case: United States v. White">322 U. S. 694, 701</a></span> (1944).</p>
<p>There is no question that the records seized from petitioner's offices and introduced against him were incriminating. Moreover, it is undisputed that some of these business records contain statements made by petitioner. Cf. <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#21" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 21-22</a></span> (1973); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span> (1973); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); and <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966). The question, therefore, is whether the seizure of these business records, and their admission into evidence at his trial, compelled petitioner to testify against himself in violation of the Fifth Amendment. This question may be said to have been reserved in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967), and it was adverted to in <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span>, 441 n. 3 (1976).</p>
<p>Petitioner contends that "the Fifth Amendment prohibition against compulsory self-incrimination applies as well to personal business papers seized from his offices as it does to the same papers being required to be produced under a subpoena." Brief for Petitioner 9. He bases his argument, naturally, on dicta in a number of cases which imply, or state, that the search for and seizure of a person's private papers violate the privilege against self-incrimination. Thus, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the Court said: "[W]e have been unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself." And in <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906), it was observed that "the substance of the offense is the compulsory production of private <span class="star-pagination">*472</span> papers, whether under a search warrant or a <i>subpoena duces tecum,</i> against which the person . . . is entitled to protection."</p>
<p>We do not agree, however, that these broad statements compel suppression of this petitioner's business records as a violation of the Fifth Amendment. In the very recent case of <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976), the Court held that an attorney's production, pursuant to a lawful summons, of his client's tax records in his hands did not violate the Fifth Amendment privilege of the taxpayer "because enforcement against a taxpayer's lawyer would not `compel' the taxpayer to do anythingand certainly would not compel him to be a `witness' against himself." <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#397" aria-description="Citation for case: Fisher v. United States"><i>Id.,</i> at 397</a></span>. We recognized that the continued validity of the broad statements contained in some of the Court's earlier cases had been discredited by later opinions. <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#407" aria-description="Citation for case: Fisher v. United States"><i>Id.,</i> at 407-409</a></span>. In those earlier cases, the legal predicate for the inadmissibility of the evidence seized was a violation of the Fourth Amendment; the unlawfulness of the search and seizure was thought to supply the compulsion of the accused necessary to invoke the Fifth Amendment.<sup>[6]</sup> Compulsion of the accused was also absent in <i>Couch</i> v. <i>United States,</i> <span class="star-pagination">*473</span> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S. 322</a></span> (1973), where the Court held that a summons served on a taxpayer's accountant requiring him to produce the taxpayer's personal business records in his possession did not violate the taxpayer's Fifth Amendment rights.<sup>[7]</sup></p>
<p>Similarly, in this case, petitioner was not asked to say or to do anything. The records seized contained statements that petitioner had voluntarily committed to writing. The search for and seizure of these records were conducted by law enforcement personnel. Finally, when these records were introduced at trial, they were authenticated by a handwriting expert, not by petitioner. Any compulsion of petitioner to speak, other than the inherent psychological pressure to respond at trial to unfavorable evidence, was not present.</p>
<p>This case thus falls within the principle stated by Mr. Justice Holmes: "A party is privileged from producing the evidence but not from its production." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="97862"><a href="/opinion/97862/johnson-v-united-states/#458" aria-description="Citation for case: Johnson v. United States">228 U. S. 457, 458</a></span> (1913). This principle recognizes that the protection afforded by the Self-Incrimination Clause of the Fifth Amendment "adheres basically to the person, not to information that may incriminate him." <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#328" aria-description="Citation for case: Couch v. United States">409 U. S., at 328</a></span>. Thus, although the Fifth Amendment may protect an individual from complying with a subpoena for the <span class="star-pagination">*474</span> production of his personal records in his possession because the very act of production may constitute a compulsory authentication of incriminating information, see <i>Fisher</i> v. <i>United States, supra</i><i>,</i> a seizure of the same materials by law enforcement officers differs in a crucial respectthe individual against whom the search is directed is not required to aid in the discovery, production, or authentication of incriminating evidence.</p>
<p>A contrary determination that the seizure of a person's business records and their introduction into evidence at a criminal trial violates the Fifth Amendment, would undermine the principles announced in earlier cases. Nearly a half century ago, in <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), the Court upheld, against both Fourth and Fifth Amendment claims, the admission into evidence of business records seized during a search of the accused's illegal liquor business. And in <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), the Court again upheld, against both Fourth and Fifth Amendment claims, the introduction into evidence at an espionage trial of false identity papers and a coded message seized during a search of the accused's hotel room. These cases recognize a general rule: "There is no special sanctity in papers, as distinguished from other forms of property, to render them immune from search and seizure, if only they fall within the scope of the principles of the cases in which other property may be seized, and if they be adequately described in the affidavit and warrant." <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span> (1921).</p>
<p>Moreover, a contrary determination would prohibit the admission of evidence traditionally used in criminal cases and traditionally admissible despite the Fifth Amendment. For example, it would bar the admission of an accused's gambling records in a prosecution for <span class="star-pagination">*475</span> gambling; a note given temporarily to a bank teller during a robbery and subsequently seized in the accused's automobile or home in a prosecution for bank robbery; and incriminating notes prepared, but not sent, by an accused in a kidnaping or blackmail prosecution.</p>
<p>We find a useful analogy to the Fifth Amendment question in those cases that deal with the "seizure" of oral communications. As the Court has explained, " `[t]he constitutional privilege against self-incrimination. . . is designed to prevent the use of legal process to force from the lips of the accused individual the evidence necessary to convict him or to force him to produce and authenticate any personal documents or effects that might incriminate him.' " <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#88" aria-description="Citation for case: Bellis v. United States">417 U. S., at 88</a></span>, quoting <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/#698" aria-description="Citation for case: United States v. White">322 U. S., at 698</a></span>. The significant aspect of this principle was apparent and applied in <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966), where the Court rejected the contention that an informant's "seizure" of the accused's conversation with him, and his subsequent testimony at trial concerning that conversation, violated the Fifth Amendment. The rationale was that, although the accused's statements may have been elicited by the informant for the purpose of gathering evidence against him, they were made voluntarily. We see no reasoned distinction to be made between the compulsion upon the accused in that case and the compulsion in this one. In each, the communication, whether oral or written, was made voluntarily. The fact that seizure was contemporaneous with the communication in <i><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span></i> but subsequent to the communication here does not affect the question whether the accused was compelled to speak.</p>
<p>Finally, we do not believe that permitting the introduction into evidence of a person's business records seized during an otherwise lawful search would offend or undermine <span class="star-pagination">*476</span> any of the policies undergirding the privilege. <i>Murphy</i> v. <i>Waterfront Comm'n,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964).<sup>[8]</sup></p>
<p>In this case, petitioner, at the time he recorded his communication, at the time of the search, and at the time the records were admitted at trial, was not subjected to "the cruel trilemma of self-accusation, perjury or contempt." <i><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">Ibid.</a></span></i> Indeed, he was never required to say or to do anything under penalty of sanction. Similarly, permitting the admission of the records in question does not convert our accusatorial system of justice into an inquisitorial system. "The requirement of specific charges, their proof beyond a reasonable doubt, the protection of the accused from confessions extorted through whatever form of police pressures, the right to a prompt hearing before a magistrate, the right to assistance of counsel, to be supplied by government when circumstances make it necessary, the duty to advise an accused of his constitutional rightsthese are all characteristics of the accusatorial system and manifestations of its demands." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span> (1949). None of these <span class="star-pagination">*477</span> attributes is endangered by the introduction of business records "independently secured through skillful investigation." <i><span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/" aria-description="Citation for case: Watts v. Indiana">Ibid.</a></span></i> Further, the search for and seizure of business records pose no danger greater than that inherent in every search that evidence will be "elicited by inhumane treatment and abuses." 378 U. S., at 55. In this case, the statements seized were voluntarily committed to paper before the police arrived to search for them, and petitioner was not treated discourteously during the search. Also, the "good cause" to "disturb," <i>ibid.,</i> petitioner was independently determined by the judge who issued the warrants; and the State bore the burden of executing them. Finally, there is no chance, in this case, of petitioner's statements being self-deprecatory and untrustworthy because they were extracted from himthey were already in existence and had been made voluntarily.</p>
<p>We recognize, of course, that the Fifth Amendment protects privacy to some extent. However, "the Court has never suggested that every invasion of privacy violates the privilege." <i>Fisher</i> v. <i>United States,</i> 425 U. S., at 399. Indeed, we recently held that unless incriminating testimony is "compelled," any invasion of privacy is outside the scope of the Fifth Amendment's protection, saying that "the Fifth Amendment protects against `compelled self-incrimination, not [the disclosure of] private information.' " <i>Id.,</i> at 401. Here, as we have already noted, petitioner was not compelled to testify in any manner.</p>
<p>Accordingly, we hold that the search of an individual's office for business records, their seizure, and subsequent introduction into evidence do not offend the Fifth Amendment's proscription that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself."</p>
<p></p>
<h2>
<span class="star-pagination">*478</span> III</h2>
<p>We turn next to petitioner's contention that rights guaranteed him by the Fourth Amendment were violated because the descriptive terms of the search warrants were so broad as to make them impermissible "general" warrants, and because certain items were seized in violation of the principles of <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967).<sup>[9]</sup></p>
<p><span class="star-pagination">*479</span> <i>The specificity of the search warrants.</i> Although petitioner concedes that the warrants for the most part were models of particularity, Brief for Petitioner 28, he contends that they were rendered fatally "general" by the addition, in each warrant, to the exhaustive list of particularly described documents, of the phrase "together with other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 95-A. 96, A. 115. The quoted language, it is argued, must be read in isolation and without reference to the rest of the long sentence at the end of which it appears. When <span class="star-pagination">*480</span> read "properly," petitioner contends, it permits the search for and seizure of any evidence of any crime.</p>
<p>General warrants, of course, are prohibited by the Fourth Amendment. "[T]he problem [posed by the general warrant] is not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings. . . . [The Fourth Amendment addresses the problem] by requiring a `particular description' of the things to be seized." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). This requirement " `makes general searches . . . impossible and prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.' " <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965), quoting <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S., at 196</a></span>.</p>
<p>In this case we agree with the determination of the Court of Special Appeals of Maryland that the challenged phrase must be read as authorizing only the search for and seizure of evidence relating to "the crime of false pretenses with respect to Lot 13T." <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/#167" aria-description="Citation for case: Andresen v. State">24 Md. App., at 167</a></span>, <span class="citation" data-id="1480134"><a href="/opinion/1480134/andresen-v-state/#103" aria-description="Citation for case: Andresen v. State">331 A. 2d, at 103</a></span>. The challenged phrase is not a separate sentence. Instead, it appears in each warrant at the end of a sentence containing a lengthy list of specified and particular items to be seized, all pertaining to Lot 13T.<sup>[10]</sup> We think it clear from the context <span class="star-pagination">*481</span> that the term "crime" in the warrants refers only to the crime of false pretenses with respect to the sale of Lot 13T. The "other fruits" clause is one of a series that follows the colon after the word "Maryland." All clauses in the series are limited by what precedes that colon, namely, "items pertaining to . . . lot 13, block T." The warrants, accordingly, did not authorize the executing officers to conduct a search for evidence of <span class="star-pagination">*482</span> other crimes but only to search for and seize evidence relevant to the crime of false pretenses and Lot 13T.<sup>[11]</sup></p>
<p><i>The admissibility of certain items of evidence in light of </i><i>Warden v. Hayden</i><i>.</i> Petitioner charges that the seizure of documents pertaining to a lot other than Lot 13T violated the principles of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> and therefore should have been suppressed. His objection appears to be that these papers were not relevant to the Lot 13T charge and were admissible only to prove another crime with which he was charged after the search. The fact that these documents were used to help form the evidentiary basis for another charge, it is argued, shows that the documents were seized solely for that purpose.</p>
<p>The State replies that <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> was not violated and that this is so because the challenged evidence is relevant to the question whether petitioner committed the crime of false pretenses with respect to Lot 13T. In Maryland, the crime is committed when a person <span class="star-pagination">*483</span> makes a false representation of a past or existing fact, with intent to defraud and knowledge of its falsity, and obtains any chattel, money, or valuable security from another, who relies on the false representation to his detriment. <i>Polisher</i> v. <i>State,</i> <span class="citation" data-id="1895902"><a href="/opinion/1895902/polisher-v-state/#560" aria-description="Citation for case: Polisher v. State">11 Md. App. 555, 560</a></span>, <span class="citation" data-id="1895902"><a href="/opinion/1895902/polisher-v-state/#104" aria-description="Citation for case: Polisher v. State">276 A. 2d 102, 104</a></span> (1971). Thus, the State is required to prove intent to defraud beyond a reasonable doubt. The State consequently argues that the documents pertaining to another lot in the Potomac Woods subdivision demonstrate that the misrepresentation with respect to Lot 13T was not the result of mistake on the part of petitioner.</p>
<p>In <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#307" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 307</a></span>, the Court stated that when the police seize " `mere evidence,' probable cause must be examined in terms of cause to believe that the evidence sought will aid in a particular apprehension or conviction. In so doing, consideration of police purposes will be required." In this case, we conclude that the trained special investigators reasonably could have believed that the evidence specifically dealing with another lot in the Potomac Woods subdivision could be used to show petitioner's intent with respect to the Lot 13T transaction.</p>
<p>The Court has often recognized that proof of similar acts is admissible to show intent or the absence of mistake. In <i>Nye &amp; Nissen</i> v. <i>United States,</i> <span class="citation" data-id="9420303"><a href="/opinion/104655/nye-nissen-v-united-states/" aria-description="Citation for case: Nye &amp; Nissen v. United States">336 U. S. 613</a></span> (1949), for example, a case involving a scheme of fraudulent conduct, it was said:</p>
<blockquote>"The evidence showed the presentation of eleven other false invoices. . . . The trial court also admitted it at the conclusion of the case `for the sole purpose of proving guilty intent, motive, or guilty knowledge' of the defendants. Evidence that similar and related offenses were committed in this period tended to show a consistent pattern of conduct highly relevant to the issue of intent." <span class="citation" data-id="9420303"><a href="/opinion/104655/nye-nissen-v-united-states/#618" aria-description="Citation for case: Nye &amp; Nissen v. United States"><i>Id.,</i> at 618</a></span>.</blockquote>
<p><span class="star-pagination">*484</span> In the present case, when the special investigators secured the search warrants, they had been informed of a number of similar charges against petitioner arising out of Potomac Woods transactions. And, by reading numerous documents and records supplied by the Lot 13T and other complainants, and by interviewing witnesses, they had become familiar with petitioner's method of operation. Accordingly, the relevance of documents pertaining specifically to a lot other than Lot 13T, and their admissibility to show the Lot 13T offense, would have been apparent. Lot 13T and the other lot had numerous features in common. Both were in the same section of the Potomac Woods subdivision; both had been owned by the same person; and transactions concerning both had been handled extensively by petitioner. Most important was the fact that there were two deeds of trust in which both lots were listed as collateral. Unreleased liens respecting both lots were evidenced by these deeds of trusts. Petitioner's transactions relating to the other lot, subject to the same liens as Lot 13T, therefore, were highly relevant to the question whether his failure to deliver title to Lot 13T free of all encumbrances was mere inadvertence. Although these records subsequently were used to secure additional charges against petitioner, suppression of this evidence in this case was not required. The fact that the records could be used to show intent to defraud with respect to Lot 13T permitted the seizure and satisfied the requirements of <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i><i>.</i></p>
<p>The judgment of the Court of Special Appeals of Maryland is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BRENNAN, dissenting.</p>
<p>In a concurring opinion earlier this Term in <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#414" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 414</a></span> (1976), I stated my view <span class="star-pagination">*485</span> that the Fifth Amendment protects an individual citizen against the compelled production of testimonial matter that might tend to incriminate him, provided it is matter that comes within the zone of privacy recognized by the Amendment to secure to the individual "a private inner sanctum of individual feeling and thought." <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#327" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 327</a></span> (1973). Accordingly, the production of testimonial material falling within this zone of privacy may not be compelled by subpoena. The Court holds today that the search and seizure, pursuant to a valid warrant, of business records in petitioner's possession and containing statements made by the petitioner does not violate the Fifth Amendment. I can perceive no distinction of meaningful substance between compelling the production of such records through subpoena and seizing such records against the will of the petitioner. Moreover, I believe that the warrants under which petitioner's papers were seized were impermissibly general. I therefore dissent.<sup>[1]</sup></p>
<p></p>
<h2>I</h2>
<p>"There is no question that the records seized from petitioner's offices and introduced against him were incriminating. Moreover, it is undisputed that some of these business records contain statements made by petitioner." <i>Ante,</i> at 471. It also cannot be questioned that these records fall within the zone of privacy protected by the Fifth Amendment. <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#87" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 87-88</a></span> (1974), squarely recognized that "[t]he privilege applies to the business records of the sole proprietor or sole practitioner <span class="star-pagination">*486</span> as well as to personal documents containing more intimate information about the individual's private life." The Court today retreats from this view. Though recognizing the value of privacy protected by the Fifth Amendment, see <i>ante,</i> at 477, and the " `right of each individual "to a private enclave where he may lead a private life," ' " <i>ante,</i> at 476 n. 8, the Court declines, without adequate explanation, to include business records within that private zone comprising the mere physical extensions of an individual's thoughts and knowledge. As I noted in <i><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">Fisher</a></span>,</i> the failure to give effect to such a zone ignores the essential spirit of the Fifth Amendment: "[Business] records are at least an extension of an aspect of a person's activities, though concededly not the more intimate aspects of one's life. Where the privilege would have protected one's mental notes of his business affairs in a less complicated day and age, it would seem that that protection should not fall away because the complexities of another time compel one to keep business records. Cf. <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#474" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 474</a></span> (1928) (Brandeis, J., dissenting)." 425 U. S., at 426-427 (BRENNAN, J., concurring in judgment).</p>
<p>As indicated at the outset, today's assault on the Fifth Amendment is not limited to narrowing this view of the scope of privacy respected by it. The Court also sanctions circumvention of the Amendment by indulging an unjustified distinction between production compelled by subpoena and production secured against the will of the petitioner through warrant. But a privilege protecting against the compelled production of testimonial material is a hollow guarantee where production of that material may be secured through the expedient of search and seizure.</p>
<p>The matter cannot be resolved on any simplistic notion of compulsion. Search and seizure is as rife with <span class="star-pagination">*487</span> elements of compulsion as subpoena. The intrusion occurs under the lawful process of the State. The individual is not free to resist that authority. To be sure, as the Court observes, "[p]etitioner was present during the search of his law office and was free to move about," <i>ante,</i> at 466, but I do not believe the Court means to suggest that petitioner was free to obstruct the investigators' search through his files.<sup>[2]</sup></p>
<p>And compulsion does not disappear merely because the individual is absent at the time of search and seizure. The door to one's house, for example, is as much the individual's resistance to the intrusion of outsiders as his personal physical efforts to prevent the same. To refuse recognition to the sanctity of that door and, more generally, to confine the dominion of privacy to the mind, compels an unconstitutional disclosure by denying to the individual a zone of physical freedom necessary for conducting one's affairs. True to this principle, a value enshrined by the Fifth Amendment, the Court carefully observed in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> that "actual possession of documents bears the most significant relationship to Fifth Amendment protections against governmental compulsions upon the individual accused of crime," <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#333" aria-description="Citation for case: Couch v. United States">409 U. S., at 333</a></span>, and that "[w]e do indeed attach constitutional importance to possession, but only because of its close relationship to those personal compulsions and intrusions which the Fifth Amendment forbids." <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Id.,</a></span></i> at 336 n. 20. <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> also plainly indicated that it is not necessary that <span class="star-pagination">*488</span> there be actual possession in order to invoke Fifth Amendment limitations, for "situations may well arise where constructive possession is so clear or the relinquishment of possession is so temporary and insignificant as to leave the personal compulsions upon the accused substantially intact." <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#333" aria-description="Citation for case: Couch v. United States"><i>Id.,</i> at 333</a></span>.<sup>[3]</sup></p>
<p>Though the records involved in this case were clearly within petitioner's possession or at least constructive possession, the Court avoids application of these principles and the values they protect by what I submit is a mischaracterization of <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> as concerned with the "possibility of compulsory self-incrimination by the principal's implicit or explicit `testimony' that the documents were those identified in the summons." <i>Ante,</i> at 473 n. 7. Whether or not <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> was concerned with this possibility and I believe that even under the most strained reading it was not<span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States"><i>Couch</i></a></span> was clearly concerned with whether production of documents in the possession of the accused's accountant pursuant to a summons directed to the accountant operated personally to compel the accused. It was in this regard that <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> recognized that "possession bears the closest relationship to the personal compulsion forbidden by the Fifth Amendment," <span class="star-pagination">*489</span> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#331" aria-description="Citation for case: Couch v. United States">409 U. S., at 331</a></span>, a matter with which the Court refuses to deal in its treatment of <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>.</i></p>
<p><i>Couch</i> only reflects the view of a long line of decisions explicitly recognizing that the seizure of private papers may violate the Fifth Amendment. As early as <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the Court was "unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself." Though the Court in <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> held that compelling a person to be a witness against himself was tantamount to an unreasonable search and seizure, it never required a search and seizure to be independently unreasonable in order that it violate the Fifth Amendment. And though the several decisions which have found a Fifth Amendment violation stemming from a search and seizure all involved unreasonable search and seizures, it has never been established, contrary to the Court's assertion, <i>ante,</i> at 472, that the unlawfulness of the search and seizure is necessary to invoke the Fifth Amendment. <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921), though also involving a Fourth Amendment violation, makes it clear that the illegality of the search and seizure is not a prerequisite for a Fifth Amendment violation. Under <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>,</i> a Fifth Amendment violation exists because the "[accused] is the unwilling source of the evidence," <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#306" aria-description="Citation for case: Gouled v. United States"><i>id.,</i> at 306</a></span>, a matter which does not depend on the illegality <i>vel non</i> of the search and seizure.<sup>[4]</sup></p>
<p>Until today, no decision by this Court had held that the seizure of testimonial evidence by legal process did <span class="star-pagination">*490</span> not violate the Fifth Amendment. Indeed, with few exceptions,<sup>[5]</sup> the indications were strongly to the contrary. See, <i>e. g., </i><i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465-467</a></span> (1932); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#397" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 397</a></span> (1914); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906).<sup>[6]</sup> More <span class="star-pagination">*491</span> recently, <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 767</a></span> (1966), noted that the "values protected by the Fourth Amendment . . . substantially overlap those the Fifth Amendment helps to protect," and clearly indicated that in considering whether to suppress seized evidence, a first inquiry is whether its testimonial nature, if any, precludes its introduction in evidence. See <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#760" aria-description="Citation for case: Schmerber v. California"><i>id.,</i> at 760-765</a></span>. Subsequent to <i>Schmerber, Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967), carefully observed that the items of clothing seized in that case were "not `testimonial' or `communicative' in nature, and their introduction therefore did not compel respondent to become a witness against himself in violation of the Fifth Amendment."<sup>[7]</sup> These cases all reflect the root understanding of <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S., at 630</a></span>: "It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence [to the Fifth Amendment]; but it is the invasion of his indefeasible right of personal security, personal liberty <span class="star-pagination">*492</span> and private property . . . . [A]ny forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime . . . , is within the condemnation of [the Amendment]. In this regard the Fourth and Fifth Amendments run almost into each other."</p>
<p></p>
<h2>II</h2>
<p>Even if a Fifth Amendment violation is not to be recognized in the seizure of petitioner's papers, a violation of Fourth Amendment protections clearly should be, for the warrants under which those papers were seized were impermissibly general. General warrants are especially prohibited by the Fourth Amendment. The problem to be avoided is "not that of intrusion <i>per se,</i> but of a general, exploratory rummaging in a person's belongings." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#467" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 467</a></span> (1971). Thus the requirement plainly appearing on the face of the Fourth Amendment that a warrant specify with particularity the place to be searched and the things to be seized is imposed to the end that "unauthorized invasions of `the sanctity of a man's home and the privacies of life' " be prevented. <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 58</a></span> (1967). " `As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.' " <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485</a></span> (1965) (quoting <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927)).</p>
<p>The Court recites these requirements, but their application in this case renders their limitation on unlawful governmental conduct an empty promise. After a lengthy and admittedly detailed listing of items to be seized, the warrants in this case further authorized the seizure of "other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 96, A. 115. The Court construes this sweeping authorization to be <span class="star-pagination">*493</span> limited to evidence pertaining to the crime of false pretenses with respect to the sale of Lot 13T. However, neither this Court's construction of the warrants nor the similar construction by the Court of Special Appeals of Maryland was available to the investigators at the time they executed the warrants. The question is not how those warrants are to be viewed in hindsight, but how they were in fact viewed by those executing them. The overwhelming quantity of seized material that was either suppressed or returned to petitioner is irrefutable testimony to the unlawful generality of the warrants.<sup>[8]</sup> The Court's attempt to cure this defect by <i>post hoc</i> judicial construction evades principles settled in this Court's Fourth Amendment decisions. "The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge . . . ." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968). See <i>Berger</i> v. <i>New York, supra,</i> at 54; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948). It is not the function of a detached and neutral review to give effect to warrants whose terms unassailably authorize the far-reaching search and seizure of a person's papers, especially where that has in fact been the result of executing those warrants.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>I agree with MR. JUSTICE BRENNAN that the business records introduced at petitioner's trial should have been suppressed because they were seized pursuant to a general warrant. Accordingly, I need not consider <span class="star-pagination">*494</span> whether petitioner's alternative contentionthat the Fifth Amendment precludes the seizure of private papers, even pursuant to a warrantcan survive <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976), and, if so, whether this Fifth Amendment argument would protect the business records seized in this case.</p>
<h2>NOTES</h2>
<p>[1]  Before these search warrants were executed, the Bi-County Fraud Unit had also received complaints concerning other Potomac Woods real estate transactions conducted by petitioner. The gist of the complaints was that petitioner, as settlement attorney, took money from three sets of home purchasers upon assurances that he would use it to procure titles to their properties free and clear of all encumbrances. It was charged that he had misappropriated the money so that they had not received clear title to the properties as promised.</p>
<p>[2]  It is established that the privilege against self-incrimination may not be invoked with respect to corporate records. <i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#88" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 88-89</a></span> (1974); <i>Grant</i> v. <i>United States,</i> <span class="citation" data-id="97758"><a href="/opinion/97758/grant-v-united-states/" aria-description="Citation for case: Grant v. United States">227 U. S. 74</a></span> (1913); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#70" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 70</a></span> (1906). It appears, however, that the records seized at the corporation's office were really not corporate records, but were records generated by petitioner's practice as a real estate lawyer. United States Appendix of Exhibits 1-3.</p>
<p>[3]  This item was introduced as proof that petitioner failed to pay recording taxes, a charge that was abandoned before the case was submitted to the jury.</p>
<p>[4]  The Solicitor General, in an <i>amicus</i> brief filed with this Court, has suggested that the evidence forming the basis of two of the counts of misappropriation by a fiduciary, which were upheld on appeal, was obtained entirely from sources other than petitioner's offices. Brief for United States as <i>Amicus Curiae</i> 12-14, 24-25, n. 17. This fact, if true, does not, of course, affect our jurisdiction but it would permit us to apply the discretionary concurrent-sentence doctrine, <i>Benton</i> v. <i>Maryland,</i> <span class="citation" data-id="9424099"><a href="/opinion/107980/benton-v-maryland/#791" aria-description="Citation for case: Benton v. Maryland">395 U. S. 784, 791</a></span> (1969), and thereby decline to consider petitioner's constitutional claims. <i>Barnes</i> v. <i>United States,</i> <span class="citation" data-id="9425368"><a href="/opinion/108830/barnes-v-united-states/" aria-description="Citation for case: Barnes v. United States">412 U. S. 837</a></span>, 848 n. 16 (1973).</p>
<p>[5]  Both the trial and appellate courts in this case recognized the conflict among the Federal Courts of Appeals over whether documentary evidence not obtainable by means of a subpoena or a summons may be obtained by means of a search warrant. Thus, in <i>Hill</i> v. <i>Philpott,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/445/144/">445 F. 2d 144</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/991/">404 U. S. 991</a></span> (1971), the Court of Appeals held that evidence not obtainable by means of a subpoena could not be seized by means of a search warrant. The substantial majority position is of the opposite view. <i>Shaffer</i> v. <i>Wilson,</i> <span class="citation" data-id="9462146"><a href="/opinion/330234/wendell-l-shaffer-and-marjorie-m-shaffer-v-robert-c-wilson-special/" aria-description="Citation for case: Wendell L. Shaffer and Marjorie M. Shaffer v. Robert C....">523 F. 2d 175</a></span> (CA10 1975), cert. pending, No. 75-601; <i>United States</i> v. <i>Murray,</i> <span class="citation" data-id="8892672"><a href="/opinion/8905447/united-states-v-murray/#191" aria-description="Citation for case: United States v. Murray">492 F. 2d 178, 191</a></span> (CA9 1973); <i>Taylor</i> v. <i>Minnesota,</i> <span class="citation" data-id="305642"><a href="/opinion/305642/robert-muller-taylor-v-state-of-minnesota/" aria-description="Citation for case: Robert Muller Taylor v. State of Minnesota">466 F. 2d 1119</a></span> (CA8 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/956/">410 U. S. 956</a></span> (1973); <i>United States</i> v. <i>Blank,</i> <span class="citation" data-id="303166"><a href="/opinion/303166/united-states-v-john-blank/" aria-description="Citation for case: United States v. John Blank">459 F. 2d 383</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/887/">409 U. S. 887</a></span> (1972); <i>United States</i> v. <i>Scharfman,</i> <span class="citation" data-id="299281"><a href="/opinion/299281/united-states-v-max-scharfman/" aria-description="Citation for case: United States v. Max Scharfman">448 F. 2d 1352</a></span> (CA2 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/919/">405 U. S. 919</a></span> (1972); <i>United States</i> v. <i>Bennett,</i> <span class="citation" data-id="284440"><a href="/opinion/284440/united-states-v-charles-t-bennett-wilbert-haywood-elmer-jessup-henry/#896" aria-description="Citation for case: United States v. Charles T. Bennett, Wilbert Haywood,...">409 F. 2d 888, 896</a></span> (CA2), cert. denied <i>sub nom. </i><i>Jessup</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./396/852/">396 U. S. 852</a></span> (1969). The majority position accords with the views of Wigmore. 8 J. Wigmore, Evidence § 2264, p. 380 (McNaughton Rev. 1961).
</p>
<p>The Court of Special Appeals adopted the majority position and, therefore, upheld the admission of the records into evidence.</p>
<p>[6]  In <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), for example, it was held that the Government could not, consistently with the Fourth Amendment, obtain "mere evidence" from the accused; accordingly, a subpoena seeking "mere evidence" constituted compulsion of the accused against which he could invoke the Fifth Amendment. The "mere evidence" rule was overturned in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#301" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 301-302</a></span> (1967).
</p>
<p>The "convergence theory" of the Fourth and Fifth Amendments is also illustrated by <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925), where the seizure of contraband pursuant to a search not incident to arrest and otherwise unlawful in violation of the Fourth Amendment was held to permit the accused to invoke the Fifth Amendment when the Government sought to introduce this evidence in a criminal proceeding against him.</p>
<p>[7]  Petitioner relies on the statement in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span></i> that "possession bears the closest relationship to the personal compulsion forbidden by the Fifth Amendment," <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#331" aria-description="Citation for case: Couch v. United States">409 U. S., at 331</a></span>, in support of his argument that possession of incriminating evidence itself supplies the predicate for invocation of the privilege. <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>,</i> of course, was concerned with the production of documents pursuant to a summons directed to the accountant where there might have been a possibility of compulsory self-incrimination by the principal's implicit or explicit "testimony" that the documents were those identified in the summons. The risk of authentication is not present where the documents are seized pursuant to a search warrant.</p>
<p>[8]  "The privilege against self-incrimination . . . reflects many of our fundamental values and most noble aspirations: our unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt; our preference for an accusatorial rather than an inquisitorial system of criminal justice; our fear that self-incriminating statements will be elicited by inhumane treatment and abuses; our sense of fair play which dictates `a fair state-individual balance by requiring the government to leave the individual alone until good cause is shown for disturbing him and by requiring the government in its contest with the individual to shoulder the entire load' . . . ; our respect for the inviolability of the human personality and of the right of each individual `to a private enclave where he may lead a private life' . . . ; our distrust of self-deprecatory statements; and our realization that the privilege, while sometimes `a shelter to the guilty,' is often `a protection to the innocent.' "</p>
<p>[9]  Petitioner also contends that the affidavits do not establish probable cause and that the failure of the State formally to introduce the warrants into evidence violated his constitutional rights. These contentions may be disposed of summarily.
</p>
<p>The bases of petitioner's argument that the affidavits failed to establish probable cause are two: The affidavits, in violation of <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), did not establish the reliability of the information or the credibility of the informants; and the information on which they were based was so stale that there was no reason to believe that the documents sought were still in petitioner's possession.</p>
<p>The affidavits clearly establish the reliability of the information related and the credibility of its sources. The complainants are named, their positions are described, and their transactions with petitioner are related in a comprehensive fashion. In addition, the special-agent affiants aver that they have verified, at least in part, the complainants' charges by examining their correspondence with petitioner, numerous documents reflecting the transactions, and public land records. Copies of many of these records and documents are attached to the affidavits; others are described in detail. Finally, the agents aver that they have interviewed, with positive results, other persons involved in the real estate transactions that were the object of the investigation. Rarely have we seen warrant-supporting affidavits so complete and so thorough. Petitioner's probable-cause argument is without merit. See <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965).</p>
<p>It is also argued that there was a three-month delay between the completion of the transactions on which the warrants were based, and the ensuing searches, and that this time lapse precluded a determination that there was probable cause to believe that petitioner's offices contained evidence of the crime. This contention is belied by the particular facts of the case. The business records sought were prepared in the ordinary course of petitioner's business in his law office or that of his real estate corporation. It is eminently reasonable to expect that such records would be maintained in those offices for a period of time and surely as long as the three months required for the investigation of a complex real estate scheme. In addition, special investigators knew that petitioner had secured a release on Lot 13T with respect to one lienholder only three weeks before the searches and that another lien remained to be released. All this, when considered with other information demonstrating that Potomac Woods was still a current concern of petitioner, amply supports the belief that petitioner retained the sought-for records.</p>
<p>The final contention is that under <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span>, 550 n. 15 (1968), the failure of the prosecution formally to introduce the warrants into evidence precludes the State from relying upon them to justify the searches. We reject the argument for two reasons. First, it appears that petitioner based this claim of error solely on state grounds in the Court of Special Appeals. Second, even if the claim is properly before us, it fails. Both the State and the petitioner referred to and extensively discussed the language and terms of the warrants during the suppression hearing, and the trial judge, in deciding the motion to suppress, made numerous references to the warrants. The present case, therefore, is a far cry from <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> where the prosecution's assertion that it had a search warrant was made for the first time during oral argument before this Court. There is nothing in the Fourth Amendment that requires us so to exalt formalism over substance.</p>
<p>[10]  "[T]he following items pertaining to sale, purchase, settlement and conveyance of lot 13, block T, Potomac Woods subdivision, Montgomery County, Maryland:
</p>
<p>"title notes, title abstracts, title rundowns; contracts of sale and/or assignments from Raffaele Antonelli and Rocco Caniglia to Mount Vernon Development Corporation and/or others; lien payoff correspondence and lien pay-off memoranda to and from lienholders and noteholders; correspondence and memoranda to and from trustees of deeds of trust; lenders instructions for a construction loan or construction and permanent loan; disbursement sheets and disbursement memoranda; checks, check stubs and ledger sheets indicating disbursement upon settlement; correspondence and memoranda concerning disbursements upon settlement; settlement statements and settlement memoranda; fully or partially prepared deed of trust releases, whether or not executed and whether or not recorded; books, records, documents, papers, memoranda and correspondence, showing or tending to show a fraudulent intent, and/or knowledge as elements of the crime of false pretenses, in violation of Article 27, Section 140, of the Annotated Code of Maryland, 1957 Edition, as amended and revised, together with other fruits, instrumentalities and evidence of crime at this [time] unknown." App. A. 95-A. 96, A. 115.</p>
<p>Petitioner also suggests that the specific list of the documents to be seized constitutes a "general" warrant. We disagree. Under investigation was a complex real estate scheme whose existence could be proved only by piecing together many bits of evidence. Like a jigsaw puzzle, the whole "picture" of petitioner's false-pretense scheme with respect to Lot 13T could be shown only by placing in the proper place the many pieces of evidence that, taken singly, would show comparatively little. The complexity of an illegal scheme may not be used as a shield to avoid detection when the State has demonstrated probable cause to believe that a crime has been committed and probable cause to believe that evidence of this crime is in the suspect's possession. The specificity with which the documents are named here contrasts sharply with the absence of particularity in <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 58-59</a></span> (1967), where a state eavesdropping statute which authorized eavesdropping "without requiring belief that any particular offense has been or is being committed; nor that the `property' sought, the conversations, be particularly described," was invalidated.</p>
<p>[11]  The record discloses that the officials executing the warrants seized numerous papers that were not introduced into evidence. Although we are not informed of their content, we observe that to the extent such papers were not within the scope of the warrants or were otherwise improperly seized, the State was correct in returning them voluntarily and the trial judge was correct in suppressing others.
</p>
<p>We recognize that there are grave dangers inherent in executing a warrant authorizing a search and seizure of a person's papers that are not necessarily present in executing a warrant to search for physical objects whose relevance is more easily ascertainable. In searches for papers, it is certain that some innocuous documents will be examined, at least cursorily, in order to determine whether they are, in fact, among those papers authorized to be seized. Similar dangers, of course, are present in executing a warrant for the "seizure" of telephone conversations. In both kinds of searches, responsible officials, including judicial officials, must take care to assure that they are conducted in a manner that minimizes unwarranted intrusions upon privacy.</p>
<p>[1]  Today's decision is doubtless consistent with the recent trend of decisions to eviscerate Fourth Amendment protections. See, <i>e. g., </i><i>Texas</i> v. <i>White,</i> <span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U. S. 435</a></span> (1976); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976); <i>United States</i> v. <i>Santana, ante,</i> p. 38.</p>
<p>[2]  There is no meaningful distinction between requiring petitioner in this case to stand idly by while papers are extracted from his files and requiring the petitioner in <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), similarly to submit to the extraction of blood from his body. In either case, seizure is obtained by compulsion, yet in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> unlike here, Fifth Amendment limitations were recognized as applicable.</p>
<p>[3]  Similarly, I recognized writing separately in <i><span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">Couch</a></span>:</i>
</p>
<p>"[S]urely the availability of the Fifth Amendment privilege cannot depend on whether or not the owner of the documents is compelled personally to turn the documents over to the Government. If private, testimonial documents held in the owner's own possession are privileged under the Fifth Amendment, then the Government cannot nullify that privilege by finding a way to obtain the documents without requiring the owner to take them in hand and personally present them to the Government agents. Where the Government takes private records from, for example, a safety deposit box against the will of the owner of the documents, the owner has been compelled, in my view, to incriminate himself within the meaning of the Fifth Amendment." <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S., at 337</a></span> n. (concurring).</p>
<p>[4]  As the Court notes, <i>ante,</i> at 474, <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> also observed that there is no special sanctity in papers rendering them immune from search and seizure. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>. The observation, however, was hedged with qualifications, see <i>ibid.,</i> and <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> itself makes clear that this was only a general proposition inapplicable in the case of private papers. See <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#306" aria-description="Citation for case: Gouled v. United States"><i>id.,</i> at 306</a></span>.</p>
<p>[5]  The Court cites <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), as one exception, that decision having permitted the seizure of business records during the search of an illegal liquor business. <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span>,</i> however, provides little, if any, foundation for the Court's view. Though erring in the light of subsequent cases, the Court there did not view the business records as private papers or testimonial evidence. Rather, the records were viewed merely as "a part of the outfit or equipment actually used to commit the offense." <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#199" aria-description="Citation for case: Marron v. United States"><i>Id.,</i> at 199</a></span>. Moreover, the aspect of <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span></i> upon which the Court relies was clearly overruled in <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932)the ostensible effort in <i><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span></i> to distinguish it from <i><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">Marron</a></span></i> notwithstanding.
</p>
<p>The Court also cites <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), as supporting its position that private testimonial papers may be seized without violating the Fifth Amendment. The papers seized in that case, however, even if fairly characterizable as private and testimoniala matter about which I have doubtwere not admitted for the purpose of utilizing their testimonial contents as evidence.</p>
<p>Finally, this Court's wiretapping cases also lend little support to the Court's position. Two of those cases expressly recognized the danger to Fifth Amendment rights posed by wiretapping. See <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#56" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 56, 62</a></span> (1967); <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>, 329 n. 7 (1966). All cases permitting seizure have involved conversations between two or more parties under other than what could be considered confidential circumstances. Grave questions would be raised, however, where conversations are seized from the privacy of the home or where the conversations are between parties who speak at other than arm's length. In such circumstances there is danger that the zone of privacy recognized by the Fifth Amendment will have been invaded. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#471" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 471-479</a></span> (1928) (Brandeis, J., dissenting).</p>
<p>[6]  Though one component of the rationale in these cases precluding the seizure of papers appears to be the "mere evidence" rule, which was repudiated in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), they also view such seizures as tantamount to the compulsion of testimony, an unlawful act conceptually distinct from the once unlawful act of seizing mere evidence. <i>United States</i> v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#466" aria-description="Citation for case: United States v. Lefkowitz"><i>Lefkowitz, supra,</i> at 466-467</a></span>, for example, reiterates <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i>'s condemnation of the <i>compulsory</i> extraction of a man's private papers. Similarly, <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#397" aria-description="Citation for case: Weeks v. United States">232 U. S., at 397</a></span>, recognized that the seizure of a man's papers was an offense because it constituted the <i>compulsory</i> production of private papers. Accordingly, the doctrinal demise of the "mere evidence" rule left untouched the principles of these cases respecting the Fifth Amendment. See <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#420" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 420-422, n. 5</a></span> (1976) (BRENNAN, J., concurring in judgment).</p>
<p>[7]  By further observing that "[t]his case thus does not require that we consider whether there are items of evidential value whose very nature precludes them from being the object of a reasonable search and seizure," <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#303" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 303</a></span>, <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span>,</i> at the very least, clearly left open the question whether lawful seizure of testimonial evidence violated the Fifth Amendment.</p>
<p>[8]  Testimony by investigators at the suppression hearing requested by the petitioner indicates that seizure of many of his papers occurred indiscriminately. See App. A. 155, A. 156.</p>

</div>
```

---

## GROUP: content/cases/Arizona v. Evans.md  (`case`, 5 assertions)

### content_page

```
---
title: "Arizona v. Evans"
type: case
citation: "514 U.S. 1 (1995)"
parallel_cite: "115 S. Ct. 1185; 131 L. Ed. 2d 34"
neutral_cite: 1995 U.S. LEXIS 1806
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-03-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-03-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Evans
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117905/arizona-v-evans/"
  cluster_id: 117905
  opinion_id: 9433091
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Leon]]", "[[Herring v. United States]]", "[[Illinois v. Krull]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith"]
holding: "The good-faith exception extends to evidence seized on a mistaken arrest record caused by clerical errors of court employees (here, a…"
lake:
  record_id: Arizona v. Evans
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Evans

*514 U.S. 1 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Phoenix police stopped Evans for a traffic violation; the patrol-car computer showed an outstanding misdemeanor arrest warrant. Officers arrested him and, in a [[Search Incident to Arrest|search incident to arrest]], found marijuana. In fact the warrant had been quashed weeks earlier, but a court clerk's error left it in the computer system. Evans moved to suppress the marijuana as the fruit of an unlawful arrest.

## Issue
Whether the exclusionary rule requires suppression of evidence seized incident to an arrest that resulted from inaccurate computer records attributable to the clerical error of a *court* employee rather than the police.

## Rule
No. Under the *[[United States v. Leon|Leon]]* cost-benefit framework, suppression is unwarranted because it would not deter the kind of error at issue: "the exclusionary rule was historically designed as a means of deterring police misconduct, not mistakes by court employees." — 514 U.S. at 14. ^pin-14

Court clerks "are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime," so excluding evidence would not deter their recordkeeping errors. Accordingly, "[a]pplication of the *Leon* framework supports a categorical exception to the exclusionary rule for clerical errors of court employees." — [*Id.* at 16](https://www.courtlistener.com/opinion/117905/arizona-v-evans/#:~:text=are%20not%20adjuncts%20to%20the). ^pin-16

## Application
On these facts the inaccurate warrant record resulted from a court clerk's failure to remove a quashed warrant, and the arresting officer reasonably relied on the police computer. Because the error was the court's, not the arresting officer's, and exclusion could not be expected to deter such court-clerk mistakes, the deterrence purpose of the exclusionary rule did not justify suppressing the evidence here.

## Conclusion
The exclusionary rule did not require suppression; the judgment of the Arizona Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Evans* applies the [[United States v. Leon]] good-faith / deterrence analysis to court-clerk recordkeeping errors. The same cost-benefit reasoning was later extended to isolated **negligent police** recordkeeping errors in [[Herring v. United States]] (2009).

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Evans*, 514 U.S. 1 (1995) — https://www.courtlistener.com/opinion/117905/arizona-v-evans/ — pinpoints: 14, 16.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "692fafcadf55de0d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "514 U.S. 1 (1995)", "court": "U.S. Supreme Court", "neutral_cite": "1995 U.S. LEXIS 1806", "official_citation_present": true, "parallel_cite": "115 S. Ct. 1185; 131 L. Ed. 2d 34", "title": "Arizona v. Evans", "year": "1995"}}
{"assertion_id": "a386527123a73d81", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The good-faith exception extends to evidence seized on a mistaken arrest record caused by clerical errors of court employees (here, a…", "title": "Arizona v. Evans"}}
{"assertion_id": "ef03581c1fb2f75d", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "Arizona v. Evans"}}
{"assertion_id": "5bfbbf39fe77289f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1995-03-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Evans", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Arizona v. Evans", "varies_by_point": "false"}}
{"assertion_id": "f8858c82f9cf7ccd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Evans"}}
```

### lake record — Arizona v. Evans

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Evans",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Evans",
    "case_name_short": "Evans",
    "case_name_full": "Arizona v. Evans",
    "input_case_name": "Arizona v. Evans",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-03-01",
    "year": 1995,
    "docket": null,
    "cluster_id": 117905,
    "lead_opinion_id": 9433091,
    "sibling_ids": [
      117905,
      9433091,
      9433092,
      9433093,
      9433094,
      9433095
    ],
    "absolute_url": "/opinion/117905/arizona-v-evans/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "514 U.S. 1",
      "volume": "514",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 1185",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1185",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 34",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "34",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 1806",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "514 U.S. 1",
        "volume": "514",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 1185",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1185",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 34",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "34",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 1806",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "514 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "514 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-14",
      "page": null,
      "quote": "--- # Arizona v. Evans *514 U.S. 1 (1995)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Phoenix police stopped Evans for a traffic violation; the patrol-car computer showed an outstanding misdemeanor arrest warrant. Officers arrested him and, in a search incident to arrest, found marijuana. In fact the warrant had been quashed weeks earlier, but a court clerk's error left it in the computer system. Evans moved to suppress the marijuana as the fruit of an unlawful arrest. ## Issue Whether the exclusionary rule requires suppression of evidence seized incident to an arrest that resulted from inaccurate computer records attributable to the clerical error of a *court* employee rather than the police. ## Rule No. Under the *Leon* cost-benefit framework, suppression is unwarranted because it would not deter the kind of error at issue:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-16",
      "page": null,
      "quote": "are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime,",
      "star_marker": "15",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 41308,
      "fragment": "#:~:text=are%20not%20adjuncts%20to%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-03-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Evans",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kruse",
          "cluster_id": 4643214,
          "cite": [
            "303 Neb. 799",
            "931 N.W.2d 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "1A Auto, Inc. v. Director of the Office of Campaign and Political Finance",
          "cluster_id": 4533242,
          "cite": [
            "105 N.E.3d 1175",
            "480 Mass. 423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Arredondo",
          "cluster_id": 6238731,
          "cite": [
            "199 Cal. Rptr. 3d 563",
            "245 Cal. App. 4th 186",
            "2016 Cal. App. LEXIS 153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shondolyn Blevins",
          "cluster_id": 2678617,
          "cite": [
            "755 F.3d 312",
            "2014 WL 2711159",
            "2014 U.S. App. LEXIS 11138"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Isaac John Russell v. State",
          "cluster_id": 3076235,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Robbins",
          "cluster_id": 118332,
          "cite": [
            "145 L. Ed. 2d 756",
            "120 S. Ct. 746",
            "528 U.S. 259",
            "2000 U.S. LEXIS 825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Morrison",
          "cluster_id": 118363,
          "cite": [
            "146 L. Ed. 2d 658",
            "120 S. Ct. 1740",
            "529 U.S. 598",
            "2000 U.S. LEXIS 3422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bennis v. Michigan",
          "cluster_id": 118005,
          "cite": [
            "134 L. Ed. 2d 68",
            "116 S. Ct. 994",
            "516 U.S. 442",
            "1996 U.S. LEXIS 1565"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Maria Lanza v. John Ashcroft, Attorney General",
          "cluster_id": 788423,
          "cite": [
            "389 F.3d 917",
            "2004 U.S. App. LEXIS 24281",
            "2004 WL 2650828"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shareef",
          "cluster_id": 154170,
          "cite": [
            "100 F.3d 1491",
            "1996 U.S. App. LEXIS 29483",
            "1996 WL 657885"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond A. Berg, Jr. v. County of Allegheny Allegheny County Adult Probation Services Debbie Benton Richard R. Gardner Glenn Allen Wolfgang Ginny Demko",
          "cluster_id": 769512,
          "cite": [
            "219 F.3d 261",
            "2000 U.S. App. LEXIS 16681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of California v. the Little Sisters of the Poor",
          "cluster_id": 4573161,
          "cite": [
            "911 F.3d 558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Frazier",
          "cluster_id": 791897,
          "cite": [
            "423 F.3d 526",
            "2005 U.S. App. LEXIS 19190",
            "2005 WL 2123792"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McCane",
          "cluster_id": 172450,
          "cite": [
            "573 F.3d 1037",
            "2009 U.S. App. LEXIS 16557",
            "2009 WL 2231658"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Travis Kinte Echols",
          "cluster_id": 1043929,
          "cite": [
            "382 S.W.3d 266",
            "2012 Tenn. LEXIS 738"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Handy",
          "cluster_id": 2559301,
          "cite": [
            "18 A.3d 179",
            "206 N.J. 39",
            "2011 N.J. LEXIS 566"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodridge v. Department of Public Health",
          "cluster_id": 6578806,
          "cite": [
            "440 Mass. 309"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Duguay",
          "cluster_id": 724910,
          "cite": [
            "93 F.3d 346",
            "1996 WL 467316"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Evans:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgyNzgwODAwMDAwJnM9MjYzMjExMiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcmcz00NDkzODM4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 2,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117905 OR 9433091 OR 9433092 OR 9433093 OR 9433094 OR 9433095)",
    "indexed_citing_opinions": 536,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117905,
        "count": 456,
        "count_source": "search"
      },
      {
        "opinion_id": 9433091,
        "count": 99,
        "count_source": "search"
      },
      {
        "opinion_id": 9433092,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433093,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433094,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433095,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 886,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-evans.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NTU5MTUmcz05NDQ3NTM5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117905+OR+9433091+OR+9433092+OR+9433093+OR+9433094+OR+9433095%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117905,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 91840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 101688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 101887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 112640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 312873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1142841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1403994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 1445040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 2144680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117905,
        "cited_id": 2609885,
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
    "date_created": "2026-07-04T18:08:00Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:14:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:08:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Evans

```
<opinion type="majority">
<author id="b77-11">Chief Justice Rehnquist</author>
<p id="Ar">delivered the opinion of the Court.</p>
<p id="b77-12">This case presents the question whether evidence seized in violation of the Fourth Amendment by an officer who <page-number citation-index="1" label="4">*4</page-number>acted in reliance on a police record indicating the existence of an outstanding arrest <em>warrant </em>— a record that is later determined to be erroneous — must be suppressed by virtue of the exclusionary rule regardless of the source of the error. The Supreme Court of Arizona held that the exclusionary rule required suppression of evidence even if the erroneous information resulted from an error committed by an employee of the office of the Clerk of Court. We disagree.</p>
<p id="b78-5">In January 1991, Phoenix police officer Bryan Sargent observed respondent Isaac Evans driving the wrong way on a one-way street in front of the police station. The officer stopped respondent and asked to see his driver’s license. After respondent told him that his license had been suspended, the officer entered respondent’s name into a computer data terminal located in his patrol car. The computer inquiry confirmed that respondent’s license had been suspended and also indicated that there was an outstanding misdemeanor warrant for his arrest. Based upon the outstanding warrant, Officer Sargent placed respondent under arrest. While being handcuffed, respondent dropped a hand-rolled cigarette that the officers determined smelled of marijuana. Officers proceeded to search his car and discovered a bag of marijuana under the passenger’s seat.</p>
<p id="b78-6">The State charged respondent with possession of marijuana. When the police notified the Justice Court that they had arrested him, the Justice Court discovered that the arrest warrant previously had been quashed and so advised the police. Respondent argued that because his arrest was based on a warrant that had been quashed 17 days prior to his arrest, the marijuana seized incident to the arrest should be suppressed as the fruit of an unlawful arrest. Respondent also argued that “[t]he ‘good faith’ exception to the exclusionary rule [was] inapplicable ... because it was police error, not judicial error, which caused the invalid arrest.” App. 5.</p>
<p id="b78-7">At the suppression hearing, the Chief Clerk of the Justice Court testified that a Justice of the Peace had issued the <page-number citation-index="1" label="5">*5</page-number>arrest warrant on December 13, 1990, because respondent had failed to appear to answer for several, traffic violations. On December 19,1990, respondent appeared before a <em>pro tem </em>Justice of the Peace who entered a notation in respondent’s file to “quash warrant.” <em>Id., </em>at 13.</p>
<p id="b79-5">The Chief Clerk also testified regarding the standard court procedure for quashing a warrant. Under that procedure a justice court clerk calls and informs the warrant section of the Sheriff’s Office when a warrant has been quashed. The Sheriff’s Office then removes the warrant from its computer records. After calling the Sheriff’s Office, the clerk makes a note in the individual’s file indicating the clerk who made the phone call and the person at the Sheriff’s Office to whom the clerk spoke. The Chief Clerk testified that there was no indication in respondent’s file that a clerk had called and notified the Sheriff’s Office that his arrest warrant had been quashed. A records clerk from the Sheriff’s Office also testified that the Sheriff’s Office had no record of a telephone call informing it that respondent’s arrest warrant had been quashed. <em>Id., </em>at 42-43.</p>
<p id="b79-6">At the close of testimony, respondent argued that the evidence obtained as a result of the arrest should be suppressed because “the purposes of the exclusionary rule would be served here by making the clerks for the court, or the clerk for the Sheriff’s office, whoever is responsible for this mistake, to be more careful about making sure that warrants are removed from the records.” <em>Id., </em>at 47. The trial court granted the motion to suppress because it concluded that the State had been at fault for failing to quash the warrant. Presumably because it could find no “distinction between State action, whether it happens to be the police department or not,” <em>id., </em>at 52, the trial court made no factual finding as to whether the Justice Court or Sheriff’s Office was responsible for the continued presence of the quashed warrant in the police records.</p>
<p id="b80-4"><page-number citation-index="1" label="6">*6</page-number>A divided panel of the Arizona Court of Appeals reversed because it “believe[d] that the exclusionary rule [was] not intended to deter justice court employees or Sheriff’s Office employees who are not directly associated with the arresting officers or the arresting officers’ police department.” <span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/#317" aria-description="Citation for case: State v. Evans">172 Ariz. 314, 317</a></span>, <span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/#1027" aria-description="Citation for case: State v. Evans">836 P. 2d 1024, 1027</a></span> (1992). Therefore, it concluded, “the purpose of the exclusionary rule would not be served by excluding the evidence obtained in this case.” <em><span class="citation" data-id="9631692"><a href="/opinion/1445040/state-v-evans/" aria-description="Citation for case: State v. Evans">Ibid.</a></span></em></p>
<p id="b80-5">The Arizona Supreme Court reversed. <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">177 Ariz. 201</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">866 P. 2d 869</a></span> (1994). The court rejected the “distinction drawn by the court of appeals ... between clerical errors committed by law enforcement personnel and similar mistakes by court employees.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#203" aria-description="Citation for case: State v. Evans"><em>Id., </em>at 203</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#871" aria-description="Citation for case: State v. Evans">866 P. 2d, at 871</a></span>. The court predicted that application of the exclusionary rule would “hopefully serve to improve the efficiency of those who keep records in our criminal justice system.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#204" aria-description="Citation for case: State v. Evans"><em>Id., </em>at 204</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#872" aria-description="Citation for case: State v. Evans">866 P. 2d, at 872</a></span>. Finally, the court concluded that “[e]ven assuming that deterrence is the principal reason for application of the exclusionary rule, we disagree with the court of appeals that such a purpose would not be served where carelessness by a court clerk results in an unlawful arrest.” <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">Ibid.</a></span></em></p>
<p id="b80-6">We granted certiorari to determine whether the exclusionary rule requires suppression of evidence seized incident to an arrest resulting from an inaccurate computer record, regardless of whether police personnel or court personnel were responsible for the record’s continued presence in the police computer. <span class="citation multiple-matches"><a href="/c/U.%20S./511/1126/">511 U. S. 1126</a></span> (1994).<footnotemark>1</footnotemark> We now reverse.</p>
<p id="b80-7">We first must consider whether we have jurisdiction to review the Arizona Supreme Court’s decision. Respondent argues that we lack jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span> because the Arizona Supreme Court never passed upon the <page-number citation-index="1" label="7">*7</page-number>Fourth Amendment issue and instead based its decision on the Arizona good-faith statute, <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-3925</span> (1993), an adequate and independent state ground. In the alternative, respondent asks that we remand to the Arizona Supreme Court for clarification.</p>
<p id="b81-5">In <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), we adopted a standard for determining whether a state-court decision rested upon an adequate and independent state ground. When “a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long"><em>Id., </em>at 1040-1041</a></span>. We adopted this practice, in part, to obviate the “unsatisfactory and intrusive practice of requiring state courts to clarify their decisions to the satisfaction of this Court.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long"><em>Id., </em>at 1041</a></span>. We also concluded that this approach would “provide state judges with a clearer opportunity to develop state jurisprudence unimpeded by federal interference, and yet will preserve the integrity of federal law.” <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></em></p>
<p id="b81-6">Justice Ginsburg would overrule <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long, supra,</a></span> </em>because she believes that the rule of that case “impedes the States’ ability to serve as laboratories for testing solutions to novel legal problems.” <em>Post, </em>at 24.<footnotemark>2</footnotemark> The opin<page-number citation-index="1" label="8">*8</page-number>ion in <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>describes the 60-year history of the Court’s differing approaches to the determination whether the judgment of the highest court of a State rested on federal or nonfederal grounds. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1038" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1038-1040</a></span>. When we were in doubt, on some occasions we dismissed the writ of certiorari; on other occasions we vacated the judgment of the state court and remanded so that it might clarify the basis for its decision. See <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">ibid.</a></span> </em>The latter approach did not always achieve the desired result and burdened the state courts with additional work. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Ibid.</a></span></em></p>
<p id="b82-5">We believe that <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>properly serves its purpose and should not be disturbed. Under it, state courts are absolutely free to interpret state constitutional provisions to accord greater protection to individual rights than do similar provisions of the United States Constitution. They also are free to serve as experimental laboratories, in the sense that Justice Brandéis used that term in his dissenting opinion in <em>New State Ice Co. </em>v. <em>Liebmann, </em><span class="citation" data-id="9418740"><a href="/opinion/101887/new-state-ice-co-v-liebmann/#311" aria-description="Citation for case: New State Ice Co. v. Liebmann">285 U. S. 262, 311</a></span> (1932) (urging that the Court not impose federal constitutional restraints on the efforts of a State to “serve as a laboratory”). Under our decision today, the State of Arizona remains free to seek whatever solutions it chooses to problems of law enforcement posed by the advent of computerization.<footnotemark>3</footnotemark> Indeed, it is freer to do so because it is disabused of its erroneous view of what the United States Constitution requires.</p>
<p id="b82-6">State courts, in appropriate cases, are not merely free to— they are bound to — interpret the United States Constitution. In doing so, they are <em>not </em>free from the final authority of this <page-number citation-index="1" label="9">*9</page-number>Court. This principle was enunciated in <em>Cohens </em>v. <em>Virginia, </em><span class="citation" data-id="85330"><a href="/opinion/85330/cohens-v-virginia/" aria-description="Citation for case: Cohens v. Virginia">6 Wheat. 264</a></span> (1821), and presumably Justice Ginsburg does not quarrel with it.<footnotemark>4</footnotemark> In <em>Minnesota </em>v. <em>National Tea Co., </em><span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span> (1940), we recognized that our authority as final arbiter of the United States Constitution could be eroded by a lack of clarity in state-court decisions.</p>
<blockquote id="b83-5">“It is fundamental that state courts be left free and unfettered by us in interpreting their state constitutions. But it is equally important that ambiguous or obscure adjudications by state courts do not stand as barriers to a determination by this Court of the validity under the federal constitution of state action. Intelligent exercise of our appellate powers compels us to ask for the elimination of the obscurities and ambiguities from the opinions in such cases. ... For no other course assures that important federal issues, such as have been argued here, will reach this Court for adjudication; that state courts will not be the final arbiters of important issues under the federal constitution; and that we will not encroach on the constitutional jurisdiction of the states.” <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/#557" aria-description="Citation for case: Minnesota v. National Tea Co."><em>Id., </em>at 557</a></span>.</blockquote>
<p id="b83-6">We therefore adhere to the standard adopted in <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long, supra.</a></span></em></p>
<p id="b83-7">Applying that standard here, we conclude that we have jurisdiction. In reversing the Court of Appeals, the Arizona Supreme Court stated that “[w]hile it may be inappropriate to invoke the exclusionary rule where a magistrate has issued a facially valid warrant (a discretionary judicial function) based on an erroneous evaluation of the facts, the law, or both, <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> ... (1984), it is useful and proper <page-number citation-index="1" label="10">*10</page-number>to do so where negligent record keeping (a purely clerical function) results in an unlawful arrest.” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#204" aria-description="Citation for case: State v. Evans">177 Ariz., at 204</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#872" aria-description="Citation for case: State v. Evans">866 P. 2d, at 872</a></span>. Thus, the Arizona Supreme Court’s decision to suppress the evidence was based squarely upon its interpretation of federal law. See <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">ibid.</a></span> </em>Nor did it offer a plain statement that its references to federal law were “being used only for the purpose of guidance, and d[id] not themselves compel the result that [it] reached.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long"><em>Long, supra, </em>at 1041</a></span>.</p>
<p id="b84-5">The Fourth Amendment states that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” We have recognized, however, that the Fourth Amendment contains no provision expressly precluding the use of evidence obtained in violation of its commands. See <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906</a></span> (1984). “The wrong condemned by the [Fourth] Amendment is ‘fully accomplished’ by the unlawful search or seizure itself,” <em>ibid, </em>(quoting <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974)), and the use of the fruits of a past unlawful search or seizure “ ‘work[s] no new Fourth Amendment wrong,’ ” <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>at 906 (quoting <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 354</a></span>).</p>
<p id="b84-6">“The question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regarded as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 223</a></span> (1983); see also <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627-628</a></span> (1980); <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486-487</a></span> (1976); <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. The exclusionary rule operates as a judicially created remedy designed to safeguard against future violations of Fourth Amendment rights through the rule’s general deterrent effect. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at <page-number citation-index="1" label="11">*11</page-number>906</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. As with any remedial device, the rule’s application has been restricted to those instances where its remedial objectives are thought most efficaciously served. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#908" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 908</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. Where “the exclusionary rule does not result in appreciable deterrence, then, clearly, its use ... is unwarranted.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454</a></span> (1976).</p>
<p id="b85-5">In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>we applied these principles to the context of a police search in which the officers had acted in objectively reasonable reliance on a search warrant, issued by a neutral and detached Magistrate, that later was determined to be invalid. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#905" aria-description="Citation for case: United States v. Leon">468 U. S., at 905</a></span>. On the basis of three factors, we determined that there was no sound reason to apply the exclusionary rule as a means of deterring misconduct on the part of judicial officers who are responsible for issuing warrants. See <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#348" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 348</a></span> (1987) (analyzing <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra).</a></span> </em>First, we noted that the exclusionary rule was historically designed “‘to deter police misconduct rather than to punish the errors of judges and magistrates.’ ” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra,</a></span> </em>at 348 (quoting <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>). Second, there was “ ‘no evidence suggesting that judges and magistrates are inclined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires the application of the extreme sanction of exclusion.’” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra,</a></span> </em>at 348 (quoting <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>). Third, and of greatest importance, there was no basis for believing that exclusion of evidence seized pursuant to a warrant would have a significant deterrent effect on the issuing judge or magistrate. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#348" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 348</a></span>.</p>
<p id="b85-6">The <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>Court then examined whether application of the exclusionary rule could be expected to alter the behavior of the law enforcement officers. We concluded:</p>
<blockquote id="b85-7">“[W]here the officer’s conduct is objectively reasonable, ‘excluding the evidence will not further the ends of the exclusionary rule in any appreciable way; for it is painfully apparent that... the officer is acting as a reason<page-number citation-index="1" label="12">*12</page-number>able officer would and should act in similar circumstances. Excluding the evidence can in no way affect his future conduct unless it is to make him less willing to do his duty.’” <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>at 919-920 (quoting <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 539-540</a></span> (White, J., dissenting)).</blockquote>
<p id="AH">See also <em>Massachusetts </em>v. <em>Sheppard, </em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981, 990-991</a></span> (1984) (“[Suppressing evidence because the judge failed to make all the necessary clerical corrections despite his assurances that such changes would be made will not serve the deterrent function that the exclusionary rule was designed to achieve”). Thus, we held that the “marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the substantial costs of exclusion.” <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 922</a></span>.</p>
<p id="b86-6">Respondent relies on <em>United States </em>v. <em>Hensley, </em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">469 U. S. 221</a></span> (1985), and argues that the evidence seized incident to his arrest should be suppressed because he was the victim of a Fourth Amendment violation. Brief for Respondent 10-12, 21-22. In <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span>, </em>the Court determined that evidence uncovered as a result of a stop pursuant to <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), was admissible because the officers who made the stop acted in objectively reasonable reliance on a flyer that had been issued by officers of another police department who possessed a reasonable suspicion to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#231" aria-description="Citation for case: United States v. Hensley">469 U. S., at 231</a></span>. Because the <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span> </em>Court determined that there had been no Fourth Amendment violation, <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#236" aria-description="Citation for case: United States v. Hensley"><em>id., </em>at 236</a></span>, the Court never considered whether the seized evidence should have been excluded. <em><span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/" aria-description="Citation for case: United States v. Hensley">Hensley</a></span> </em>does not contradict our earlier pronouncements that “[t]he question whether the exclusionary rule’s remedy is appropriate in a particular context has long been regarded as an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#223" aria-description="Citation for case: Illinois v. Gates"><em>Gates, supra, </em>at 223</a></span>; see also <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 486-487</a></span>; <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b87-4"><page-number citation-index="1" label="13">*13</page-number>Respondent also argues that <em>Whiteley </em>v. <em>Warden, Wyo. State Penitentiary, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971), compels exclusion of the evidence. In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>the Court determined that the Fourth Amendment had been violated when police officers arrested Whiteley and recovered inculpatory evidence based upon a radio report that two suspects had been involved in two robberies. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568-569</a></span>. Although the “police were entitled to act on the strength of the radio bulletin,” the Court determined that there had been a Fourth Amendment violation because the initial complaint, upon which the arrest warrant and subsequent radio bulletin were based, was insufficient to support an independent judicial assessment of probable cause. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568</a></span>. The Court concluded that “an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.” <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Ibid.</a></span> </em>Because the “arrest violated [Whiteley’s] constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).” <em>Id., </em>at 568-569.</p>
<p id="b87-5">Although <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>clearly retains relevance in determining whether police officers have violated the Fourth Amendment, see <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#230" aria-description="Citation for case: United States v. Hensley"><em>Hensley, supra, </em>at 230-231</a></span>, its precedential value regarding application of the exclusionary rule is dubious. In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>the Court treated identification of a Fourth Amendment violation as synonymous with application of the exclusionary rule to evidence secured incident to that violation. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S., at 568-569</a></span>. Subsequent case law has rejected this reflexive application of the exclusionary rule. Cf. <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987); <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard, supra;</a></span> United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). These later cases have emphasized that the issue of exclusion is separate from whether the Fourth Amendment has been violated, see, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>e. g., Leon, supra, </em>at 906</a></span>, and exclusion is appropriate only if the <page-number citation-index="1" label="14">*14</page-number>remedial objectives of the rule are thought most efficaciously served, see <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</p>
<p id="b88-5">Our approach is consistent with the dissenting Justices’ position in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>our only major case since <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>and <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard</a></span> </em>involving the good-faith exception to the exclusionary rule. In that case, the Court found that the good-faith exception applies when an officer conducts a search in objectively reasonable reliance on the constitutionality of a statute that subsequently is declared unconstitutional. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#346" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 346</a></span>. Even the dissenting Justices in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>agreed that <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>provided the proper framework for analyzing whether the exclusionary rule applied; they simply thought that “application of <em>Leon’s </em>stated rationales le[d] to a contrary result.” <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#362" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 362</a></span> (O’Connor, J., dissenting). In sum, respondent does not persuade us to abandon the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>framework.</p>
<p id="b88-6">Applying the reasoning of <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>to the facts of this ease, we conclude that the decision of the Arizona Supreme Court must be reversed. The Arizona Supreme Court determined that it could not “support the distinction drawn ... between clerical errors committed by law enforcement personnel and similar mistakes by court employees,” <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#203" aria-description="Citation for case: State v. Evans">177 Ariz., at 203</a></span>, <span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/#871" aria-description="Citation for case: State v. Evans">866 P. 2d, at 871</a></span>, and that “even assuming... that responsibility for the error rested with the justice court, it does not follow that the exclusionary rule should be inapplicable to these facts,” <em><span class="citation" data-id="9791642"><a href="/opinion/2609885/state-v-evans/" aria-description="Citation for case: State v. Evans">ibid.</a></span></em></p>
<p id="b88-7">This holding is contrary to the reasoning of <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra;</a></span> Massachusetts </em>v. <em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/" aria-description="Citation for case: Massachusetts v. Sheppard">Sheppard, supra;</a></span> </em>and, <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull, supra.</a></span> </em>If court employees were responsible for the erroneous computer record, the exclusion of evidence at trial would not sufficiently deter fiiture errors so as to warrant such a severe sanction. First, as we noted in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the exclusionary rule was historically designed as a means of deterring police misconduct, not mistakes by court employees. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>; see also <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 350</a></span>. Second, respondent offers no evidence that court employees are in-<page-number citation-index="1" label="15">*15</page-number>dined to ignore or subvert the Fourth Amendment or that lawlessness among these actors requires application of the extreme sanction of exclusion. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916</a></span>, and n. 14; see also <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 350-351</a></span>. To the contrary, the Chief Clerk of the Justice Court testified at the suppression hearing that this type of error occurred once every three or four years. App. 37.</p>
<p id="b89-5">Finally, and most important, there is no basis for believing that application of the exclusionary rule in these circumstances will have a significant effect on court employees responsible for informing the police that a warrant has been quashed. Because court clerks are not adjuncts to the law enforcement team engaged in the often competitive enterprise of ferreting out crime, see <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), they have no stake in the outcome of particular criminal prosecutions. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 917</a></span>; <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#352" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 352</a></span>. The threat of exclusion of evidence could not be expected to deter such individuals from failing to inform police officials that a warrant had been quashed. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#917" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 917</a></span>; <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#352" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 352</a></span>.</p>
<p id="b89-6">If it were indeed a court clerk who was responsible for the erroneous entry on the police computer, application of the exclusionary rule also could not be expected to alter the behavior of the arresting officer. As the trial court in this case stated: “I think the police officer [was] bound to arrest. I think he would [have been] derelict in his duty if he failed to arrest.” App. 51. Cf. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#920" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 920</a></span> (“ ‘Excluding the evidence can in no way affect [the officer’s] future conduct unless it is to make him less willing to do his duty.’ ” quoting <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#540" aria-description="Citation for case: Stone v. Powell">428 U. S., at 540</a></span> (White, J., dissenting)). The Chief Clerk of the Justice Court testified that this type of error occurred “on[c]e every three or four years.” App. 37. In fact, once the court clerks discovered the error, they immediately corrected it, <em>id., </em>at 30, and then proceeded to search their files to make sure that no similar mistakes had occurred, <em>id., </em>at 37. There is no indication that the arresting <page-number citation-index="1" label="16">*16</page-number>officer was not acting objectively reasonably when he relied upon the police computer record. Application of the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>framework supports a categorical exception to the exclusionary rule for clerical errors of court employees. See <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#916" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 916-922</a></span>; <span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard"><em>Sheppard, supra, </em>at 990-991</a></span>.<footnotemark>5</footnotemark></p>
<p id="b90-5">The judgment of the Supreme Court of Arizona is therefore reversed, and the case is remanded to that court for proceedings not inconsistent with this opinion.</p>
<p id="b90-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b80-8"> Petitioner has conceded that respondent's arrest violated the Fourth Amendment. Brief for Petitioner 10. We decline to review that determination. Cf. <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#905" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 905</a></span> (1984); <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#357" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340, 357, n. 13</a></span> (1987).</p>
</footnote>
<footnote label="2">
<p id="b81-7"> Justice Ginsburg certainly is correct when she notes that “‘[s]ince <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>, </em>we repeatedly have followed [its] “plain statement” requirement.’” <em>Post, </em>at 33 (quoting <em>Harris </em>v. <em>Reed, </em><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/#261" aria-description="Citation for case: Harris v. Reed">489 U. S. 255, 261, n. 7</a></span> (1989) (opinion of Blackmun, J.)); see also <em>Illinois </em>v. <em>Rodriguez, </em><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#182" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 182</a></span> (1990) (opinion of Scalia, J.); <em>Pennsylvania </em>v. <em>Muniz, </em><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#588" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 588, n. 4</a></span> (1990) (opinion of Brennan, J.); <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#83" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 83-84</a></span> (1987) (opinion of Stevens, J.); <em>Caldwell </em>v. <em>Mississippi, </em><span class="citation" data-id="111471"><a href="/opinion/111471/caldwell-v-mississippi/#327" aria-description="Citation for case: Caldwell v. Mississippi">472 U. S. 320, 327-328</a></span> (1985) (opinion of Marshall, J.); <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#389" aria-description="Citation for case: California v. Carney">471 U. S. 386, 389, n. 1</a></span> (1985) (opinion of Burger, C. J.); <em>Ohio </em>v. <em>Johnson, </em><span class="citation" data-id="9429653"><a href="/opinion/111207/ohio-v-johnson/#497" aria-description="Citation for case: Ohio v. Johnson">467 U. S. 493, 497-498, n. 7</a></span> (1984) (opinion of Rehnquist, J.); <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#175" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 175-176, n. 5</a></span> (1984) (opinion of Powell, J.); cf. <em>Coleman </em><page-number citation-index="1" label="8">*8</page-number>v. <em>Thompson, </em><span class="citation" data-id="9842121"><a href="/opinion/112640/coleman-v-thompson/#740" aria-description="Citation for case: Coleman v. Thompson">501 U. S. 722, 740</a></span> (1991) (opinion of O’Connor, J.) (declining to expand the <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>and <em><span class="citation" data-id="9431577"><a href="/opinion/112205/harris-v-reed/" aria-description="Citation for case: Harris v. Reed">Harris</a></span> </em>presumption to instances “where the relevant state court decision does not fairly appear to rest primarily on federal law or to be interwoven with such law”).</p>
</footnote>
<footnote label="3">
<p id="b82-9"> Justice Ginsburg acknowledges as much when she states that since <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>, </em>“state courts, on remand, have reinstated their prior judgments after clarifying their reliance on state grounds.” <em>Post, </em>at 32 (citing statistics).</p>
</footnote>
<footnote label="4">
<p id="b83-8"> Surely if we have jurisdiction to vacate and remand a state-court judgment for clarification, <em>post, </em>at 34, n. 7, we also must have jurisdiction to determine whether a state-court judgment is based upon an adequate and independent state ground. See <em>Abie State Bank </em>v. <em>Bryan, </em><span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#773" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S. 765, 773</a></span> (1931).</p>
</footnote>
<footnote label="5">
<p id="b90-10"> The Solicitor General, as <em>amicus curiae, </em>argues that an analysis similar to that we apply here to court personnel also would apply in order to determine whether the evidence should be suppressed if police personnel were responsible for the error. As the State has not made any such argument here, we agree that “[t]he record in this case ... does not adequately present that issue for the Court’s consideration.” Brief for United States as <em>Amicus Curiae </em>13. Accordingly, we decline to address that question.</p>
</footnote>
</opinion>
```

---
