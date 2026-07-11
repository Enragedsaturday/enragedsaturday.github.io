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

## GROUP: _overhaul2/lake/cases/United States v. Crumble.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Crumble
type: case
citation: "878 F.3d 656 (2018)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir.
court_level: coa
circuit: ca8
year: 2018
date_decided: 2018-01-02
docket: 16-4114
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4456532/united-states-v-prentiss-anthony-crumble/"
  cluster_id: 4456532
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Crumble
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Abandonment]]"
    role: Key
related:
  - "[[Abandonment]]"
  - "[[Riley v. California]]"
  - "[[Minnesota v. Carter]]"
tags:
  - case
  - fourth-amendment
  - abandonment
  - reasonable-expectation-of-privacy
  - cell-phone
  - standing
  - eighth-circuit
holding: "A person who flees a wrecked car and leaves his cell phone behind, then denies any knowledge of the vehicle, abandons the phone and forfeits any reasonable expectation of privacy in it — judged by the objective facts available to officers, not the owner's subjective intent — and the abandonment doctrine applies to cell phones notwithstanding Riley v. California, so the warrantless seizure and later search of the phone did not violate the Fourth Amendment."
aliases:
  - United States v. Crumble
  - "United States v. Crumble (8th Cir. 2018)"
  - United States v. Prentiss Anthony Crumble
---

# United States v. Crumble

*878 F.3d 656 (8th Cir. 2018)* · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4456532 → majority opinion 4233785 (Shepherd, J.; 878 F.3d 656, decided Jan. 2, 2018). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (Rehaif felon-in-possession Crumble) to the intended abandonment Crumble; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text; slip-style pin (the CL text carries a page-image map, not 878 F.3d reporter star-pagination) — S9 verifies the reporter pincite. -->

## Background
After a shooting between two cars in St. Paul, one vehicle — a tan Buick — crashed into a house, and its two occupants fled on foot. Officers found the wrecked Buick with the key in the ignition, a shot-out rear window, a handgun on the floorboard, and a cell phone on the driver's seat. A witness's description led officers to Prentiss Crumble, hiding nearby; taken to the scene, he denied any knowledge of the shooting or the Buick. An officer later seized the phone and, under a warrant, found a video of Crumble with a similar handgun shortly before the shooting. The district court held Crumble had abandoned the phone and denied suppression.

## Issue
Whether Crumble abandoned his cell phone — forfeiting any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it — when he fled the wrecked car and disclaimed knowledge of the vehicle, and whether the abandonment doctrine applies to cell phones after *[[Riley v. California]]*.

## Rule
A defendant "does not have a reasonable expectation of privacy in abandoned property"; the question is whether, "in leaving the property," he "relinquished [his] reasonable expectation of privacy," judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] by "the objective facts available to the investigating officers, not ... the owner's subjective intent," with "two important factors [being] denial of ownership and physical relinquishment of the property." Rejecting a categorical carve-out, the court held: "Crumble urges this Court to categorically deny application of the abandonment doctrine to cell phones. We decline to do so." — slip op. at 3. ^pin-slip3

## Application
Objectively, Crumble fled the crash, left the phone on the seat of a wrecked car with the key in the ignition and the rear window shot out (open to anyone), and then affirmatively denied knowing anything about the Buick — conduct demonstrating both physical relinquishment and denial of ownership. His later admission, made after the phone was seized, did not reassert a privacy interest already forfeited. *[[Riley v. California|Riley]]* did not help him: its holding is limited to [[Search Incident to Arrest|searches incident to arrest]] and expressly leaves other case-specific exceptions — including abandonment — intact.

## Conclusion
**Affirmed.** Judge Shepherd wrote for the panel; the district court's abandonment finding was not [[Common Legal Terms#clear-error|clearly erroneous]], and the phone evidence was admissible.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Crumble* is a clean circuit application of the *[[Abandonment]]* doctrine to a modern device: fleeing and disclaiming ownership objectively forfeits the [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and *[[Riley v. California|Riley]]*'s special solicitude for phones does not exempt them from abandonment. Read it against the standing threshold of *[[Minnesota v. Carter]]*.

## Appears on
- [[Abandonment]] — *Key*

## Sources
- [*United States v. Crumble*, 878 F.3d 656 (8th Cir. 2018)](https://www.courtlistener.com/opinion/4456532/united-states-v-prentiss-anthony-crumble/) — pinpoint: slip op. at 3 (abandonment forfeits the reasonable expectation of privacy; the doctrine applies to cell phones despite *Riley*). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries a page-image map, not 878 F.3d reporter star-pagination, so the reporter page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ebca964e3162537", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Crumble"}, "payload": {"all": [{"cite": "878 F.3d 656", "page": "656", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "878"}], "display": "878 F.3d 656", "official": {"cite": "878 F.3d 656", "page": "656", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "878"}, "official_selection_present": true, "record_id": "United States v. Crumble"}}
{"assertion_id": "f0624b4a20d7883b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Crumble"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Crumble", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Crumble

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Crumble",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Prentiss Anthony Crumble",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee v. Prentiss Anthony CRUMBLE, Defendant-Appellant",
    "input_case_name": "United States v. Crumble",
    "court": "8th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2018-01-02",
    "year": 2018,
    "docket": "16-4114",
    "cluster_id": 4456532,
    "lead_opinion_id": 4233785,
    "sibling_ids": [],
    "absolute_url": "/opinion/4456532/united-states-v-prentiss-anthony-crumble/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "878 F.3d 656",
      "volume": "878",
      "reporter": "F.3d",
      "page": "656",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "878 F.3d 656",
        "volume": "878",
        "reporter": "F.3d",
        "page": "656",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "878 F.3d 656",
    "official_selection": {
      "court_class": "coa",
      "selected": "878 F.3d 656",
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
    "date_created": "2026-07-07T18:16:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-crumble--4456532",
      "to_record_id": "United States v. Crumble",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Crumble

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 16-4308
                        ___________________________

                             United States of America

                        lllllllllllllllllllPlaintiff - Appellee

                                          v.

                            Prentiss Anthony Crumble

                      lllllllllllllllllllll Defendant - Appellant
                                      ____________

                    Appeal from United States District Court
                     for the District of Minnesota - St. Paul
                                 ____________

                           Submitted: October 20, 2017
                              Filed: January 2, 2018
                                 ____________

Before WOLLMAN and SHEPHERD, Circuit Judges, and GOLDBERG,1 Judge.
                         ____________

SHEPHERD, Circuit Judge.

      On October 21, 2014, at approximately 1:28 p.m., police received reports of
shots being fired between two vehicles in St. Paul, Minnesota. Dispatch informed
responding officers that one of the vehicles—a tan Buick—had crashed into a house


      1
       The Honorable Richard W. Goldberg, Judge for the United States Court of
International Trade, sitting by designation.
and its two male occupants had fled on foot. Officers arrived at the scene to find the
wrecked Buick with bullet holes along its passenger side and a shot-out rear window.
They noticed the Buick’s key in its ignition and a handgun on the driver’s side
floorboard. A witness informed the officers that after the crash the other vehicle’s
shooter continued to fire at the Buick. The witness stated that the Buick’s two
occupants fled the scene on foot heading west, describing one as a black male, in his
early 20s, wearing a white t-shirt. Another witness also reported seeing an
approximately 25-year-old black male in a white t-shirt running westward from the
Buick. Officers found a man matching this description hiding behind a shed a block
and a half away. That man was appellant Prentiss Crumble.

       Officers took Crumble into custody and drove him to the scene of the wrecked
Buick—where he denied any knowledge of the shooting or the Buick. When an
officer searched the Buick later that day, he found a cell phone on the driver’s seat,
which he secured into evidence. The following day, the officer applied for a search
warrant to search the cell phone for “information as to the second occupant in the
Buick or further information related to the crime.” A county judge issued a warrant
to search “[a]ll electronic data (including but not limited to contacts, calenders, call
records, voice messages, text messages, photo and video files) stored in” the phone.
In the subsequent search, the officer found a video of Crumble inside a vehicle
wearing a white t-shirt and brandishing a handgun similar to that recovered from the
Buick. The video was recorded shortly before the shooting on October 21, 2014 at
1:15 p.m.

      Crumble was charged with being a felon in possession of a firearm in violation
of 18 U.S.C. §§ 922(g)(1) and 924(e). Crumble moved to suppress the evidence
recovered from the cell phone. The magistrate judge recommended granting
Crumble’s motion to suppress, finding Crumble had not abandoned his Fourth
Amendment rights in the phone. The district court rejected the magistrate judge’s
recommendation, concluding that the evidence from the cell phone was admissible

                                          -2-
because Crumble abandoned the Buick and the phone left in it when he fled and
subsequently denied any knowledge of the vehicle. The district court alternatively
held that the search warrant was supported by probable cause and did not lack
particularity or amount to a general warrant. Finally, even if there were no probable
cause or a lack of particularity, the good-faith exception applied because it was
objectively reasonable for the police to rely on the warrant.

       Crumble entered a conditional guilty plea, reserving his right to appeal the
district court’s denial of his motion to suppress the evidence obtained in the search
of his cell phone. At sentencing, the government sought application of the Armed
Career Criminal Act (“ACCA”) based on Crumble’s prior felony convictions under
Minnesota law, which included a conviction for second-degree assault, a conviction
for second-degree burglary, and two convictions for third-degree burglary. Crumble
argued the burglary convictions were not violent felonies under the ACCA. The
district court disagreed and imposed the ACCA mandatory minimum sentence of 15
years in prison. Crumble now appeals his conviction and sentence.

                                           I.

       We first take up Crumble’s Fourth Amendment challenge to the search of the
cell phone. The Fourth Amendment protects “against unreasonable searches and
seizures.” U.S. Const. amend. IV. “[I]n order to claim the protection of the Fourth
Amendment, a defendant must demonstrate that he personally has [a reasonable]
expectation of privacy in the place searched . . . . ” Minnesota v. Carter, 525 U.S. 83,
88 (1998). Therefore, we must initially consider whether Crumble had a reasonable
expectation of privacy in the cell phone he left behind in the Buick.

       It is well-established that a defendant does not have a reasonable expectation
of privacy in abandoned property. See United States v. Tugwell, 125 F.3d 600, 602
(8th Cir. 1997). Thus, if Crumble abandoned the cell phone, he forfeited his

                                          -3-
expectation of privacy and cannot raise a Fourth Amendment challenge to the
subsequent search. See id. (“A warrantless search of abandoned property does not
implicate the Fourth Amendment, for any expectation of privacy in the item searched
is forfeited upon its abandonment.”). “The issue is not abandonment in the strict
property right sense, but rather, whether the defendant in leaving the property has
relinquished [his] reasonable expectation of privacy . . . . ” Id. (internal quotation
marks omitted). A finding of abandonment depends on the totality of the
circumstances, with “two important factors [being] denial of ownership and physical
relinquishment of the property.” Id. (internal quotation marks omitted). Courts
consider only “the objective facts available to the investigating officers, not . . . the
owner’s subjective intent.” United States v. Nowak, 825 F.3d 946, 948 (8th Cir.
2016) (per curiam) (internal quotation marks omitted).

      Here, the district court found that Crumble abandoned the cell phone. We
review this factual finding for clear error, “affirm[ing] the district court’s
abandonment finding unless its decision is ‘unsupported by substantial evidence,
based on an erroneous interpretation of applicable law, or, in light of the entire
record, we are left with a firm and definite conviction that a mistake has been made.’”
United States v. Ruiz, 935 F.2d 982, 984 (8th Cir. 1991) (quoting United States v.
Meirovitz, 918 F.2d 1376, 1379 (8th Cir. 1990)).

       Based on the totality of the circumstances, we cannot say that the district court
clearly erred in finding Crumble abandoned the cell phone in the Buick. After the
crash, Crumble fled the scene, leaving the Buick wrecked on a stranger’s lawn. The
Buick’s key was in the ignition and its back window was shot out—allowing for easy
access to the vehicle and its contents—which included a gun on the floorboard and
the cell phone on the driver’s seat. Crumble claims he was not fleeing from police,
but rather attempting to get away from the shooter in the other vehicle.
Abandonment, however, does not turn on Crumble’s subjective intent, but rather “the
objective facts available to the investigating officers.” Nowak, 825 F.3d at 948

                                          -4-
(internal quotation marks omitted). Based on these objective facts, the district court
did not clearly err in concluding Crumble had abandoned the vehicle and its contents,
including the cell phone. See United States v. Taylor, 462 F.3d 1023, 1025-26 (8th
Cir. 2006) (finding defendant abandoned cell phone when he dropped it on street
while fleeing vehicle); see also United States v. Smith, 648 F.3d 654, 660 (8th Cir.
2011) (finding defendant abandoned vehicle and contents when he fled, leaving door
open, key in ignition, and motor running); United States v. Tate, 821 F.2d 1328, 1330
(8th Cir. 1987) (finding defendant abandoned vehicle and contents when he fled,
leaving vehicle unoccupied and unlocked).

       Moreover, Crumble initially denied any knowledge of the wrecked Buick,
evincing his intent to abandon the vehicle and its contents. See United States v.
Nordling, 804 F.2d 1466, 1470 (8th Cir. 1986) (finding defendant’s “denials
objectively demonstrate an intent to abandon the property”). Only the following
day—after police had already seized the cell phone—did Crumble admit to having
been in the Buick. This admission did not constitute a reassertion of a privacy
interest in the abandoned cell phone. See id.

       Crumble urges this Court to categorically deny application of the abandonment
doctrine to cell phones. We decline to do so. Crumble points to Riley v. California,
where the Supreme Court held that the search incident to arrest exception does not
apply to cell phone searches, in part because cell phones hold “the privacies of life.”
134 S. Ct. 2473, 2494-95 (2014) (internal quotation marks omitted). However,
Riley’s holding is limited to cell phones seized incident to arrest. Id. at 2495. Riley
was explicit that “other case-specific exceptions may still justify a warrantless search
of a particular phone.” Id. at 2494. Other courts have found abandonment to be one
such exception. See, e.g., United States v. Quashie, 162 F. Supp. 3d 135, 141-42
(E.D.N.Y. 2016) (finding Riley does not eliminate abandonment exception for cell
phones).



                                          -5-
      We conclude the district court did not clearly err in finding abandonment and
denying Crumble’s motion to suppress. Because we affirm the district court’s
holding based on abandonment, we need not consider whether the warrant was valid.
Cf. Tugwell, 125 F.3d at 602 (“warrantless search of abandoned property does not
implicate the Fourth Amendment”).

                                          II.

       We next turn to Crumble’s sentencing challenge. The district court sentenced
Crumble to the ACCA mandatory minimum of 15 years imprisonment. The ACCA
applies when a defendant convicted under 18 U.S.C. § 922(g) has three prior
convictions “for a violent felony or a serious drug offense.” 18 U.S.C. § 924(e)(1).
As noted earlier, Crumble’s prior felony convictions include a Minnesota conviction
for second-degree assault, a Minnesota conviction for second-degree burglary, and
two Minnesota convictions for third-degree burglary. Crumble argues his burglary
convictions do not qualify as violent felonies under the ACCA, and the government
agrees. We review whether a prior conviction qualifies as a violent felony de novo.
United States v. Shockley, 816 F.3d 1058, 1062 (8th Cir. 2016).

       The ACCA’s definition of “violent felony” includes burglary. 18 U.S.C.
§ 924(e)(2)(B)(ii). To determine whether a state burglary conviction qualifies as
burglary under the ACCA, we must first determine whether to apply the categorical
approach (used when an indivisible statute lists alternative means of committing a
single crime) or the modified categorical approach (used when a divisible statute lists
alternative elements to define multiple crimes). See Mathis v. United States, 136 S.
Ct. 2243, 2248-49 (2016). Under the categorical approach, a state burglary
conviction qualifies only if its statute’s elements are the same as, or narrower than,
those of generic burglary, which is an “‘unlawful or unprivileged entry into, or
remaining in, a building or structure, with intent to commit a crime.’” Descamps v.



                                         -6-
United States, 133 S. Ct. 2276, 2283 (2013) (quoting Taylor v. United States, 495
U.S. 575, 599 (1990)).

      Minnesota’s third-degree burglary statute provides that:

      Whoever enters a building without consent and with intent to steal or
      commit any felony or gross misdemeanor while in the building, or enters
      a building without consent and steals or commits a felony or gross
      misdemeanor while in the building . . . commits burglary in the third
      degree . . . .

Minn. Stat. § 609.582, subdiv. 3. In determining whether Minnesota third-degree
burglary qualifies as a violent felony under the ACCA, this Court’s decision in
United States v. McArthur, 850 F.3d 925 (8th Cir. 2017) is controlling. There, this
Court found Minnesota’s third-degree burglary statute to be indivisible and applied
the categorical approach. Id. at 938. While the first alternative means in the
Minnesota statute (entering with intent to commit a crime) qualifies as generic
burglary, the second alternative means (unlawful entry followed by the commission
of a crime) does not. Id. at 938-40. That is because the second alternative means
“does not require that the defendant have formed the ‘intent to commit a crime’ at the
time of the nonconsensual entry or remaining in,” as is required by the definition of
generic burglary in Taylor. Id. at 940. Thus, Minnesota third-degree burglary “is
broader than generic burglary” and does not qualify as a predicate conviction under
the ACCA. Id.

      Minnesota’s second-degree burglary statute provides that:

      Whoever enters a building without consent and with intent to commit a
      crime, or enters a building without consent and commits a crime while
      in the building . . . commits burglary in the second degree . . . .



                                         -7-
Minn. Stat. § 609.582, subdiv. 2(a). Both parties agree that because this statute
includes the same overbroad second alternative means as Minnesota’s third-degree
burglary statute (unlawful entry followed by the commission of a crime), Minnesota
second-degree burglary does not qualify as a violent felony under the ACCA. Indeed,
this Court’s analysis of Minnesota’s third-degree burglary statute in McArthur applies
with equal force to Minnesota’s second-degree burglary statute. The statute is
indivisible, so we apply the categorical approach. See McArthur, 850 F.3d at 938
(citing State v. Gonzales, No. A15-0975, 2016 WL 3222795, at *2-3 (Minn. Ct. App.
June 13, 2016)). Because a conviction under the second alternative means of the
statute “does not require that the defendant have formed the ‘intent to commit a
crime’ at the time of the nonconsensual entry or remaining in,” Minnesota second-
degree burglary “is broader than generic burglary” and does not qualify as a predicate
conviction under the ACCA. See id. at 940.

       Because Crumble’s Minnesota burglary convictions do not qualify as violent
felonies, Crumble has no more than one predicate conviction. The ACCA mandatory
minimum, therefore, does not apply. We vacate his sentence and remand to the
district court for resentencing.

                                         III.

     For the foregoing reasons, we affirm the district court’s denial of Crumble’s
motion to suppress and remand for resentencing in accordance with this opinion.
                      ______________________________




                                         -8-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Daniels.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Daniels
type: case
citation: "101 F.4th 770 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2024
date_decided: 2024-05-08
docket: 22-1378
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
  opinion_url: "https://www.courtlistener.com/opinion/9500360/united-states-v-daniels/"
  cluster_id: 9500360
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Daniels
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Key
  - page: "[[Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Terry v. Ohio]]"
  - "[[United States v. Black]]"
  - "[[Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - terry-stop
  - reasonable-suspicion
  - anonymous-tip
holding: "The totality of the circumstances did not establish reasonable suspicion to detain Daniels: a near-anonymous, non-emergency tip that alleged no illegality and described men in dark clothing — which Daniels, in a bright orange jumpsuit, did not match — plus his mere proximity to the described SUV in a high-crime area late at night amounted only to an arbitrary hunch, so suppressing his name as the fruit of the unlawful detention was proper."
---

# United States v. Daniels

*101 F.4th 770 (10th Cir. 2024)* (No. 22-1378) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9500360 → opinion 9966973 (101 F.4th 770, decided 2024-05-08); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Just before midnight, the Aurora Police Department received a near-anonymous, non-emergency call reporting that three Black men in dark hoodies and jeans were taking guns in and out of their pockets and getting in and out of a dark SUV in an apartment parking lot; the caller thought they were "getting ready to do something" but conceded it was not an emergency and reported no illegality. Officer Idler arrived at the high-crime complex, spotted a dark SUV, and saw Lyndell Daniels standing five to ten feet away — wearing a bright orange jumpsuit with a reflective strip. Daniels appeared to say something to the SUV, which then drove off at a normal speed. Idler ordered Daniels to raise his hands, detained him, obtained his name, and learned he was a felon. The SUV was later stopped and found to contain a stolen Glock, and Daniels's name led to a DNA warrant tying him to that gun. Charged as a felon in possession, Daniels moved to suppress his name as the fruit of an unlawful detention; the district court granted the motion, and the government appealed.

## Issue
Whether Officer Idler had reasonable suspicion to detain Daniels, where a near-anonymous, non-emergency tip described men in dark clothing handling guns, Daniels wore bright orange and merely stood near the described SUV in a high-crime area late at night, and the tip alleged no illegality.

## Rule
An investigatory detention is justified at its inception only if specific and articulable facts, and the rational inferences from them, give rise to a reasonable suspicion that a person has committed, is committing, or is about to commit a crime, assessed under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. Applying that standard [[Common Legal Terms#de-novo|de novo]], the Tenth Circuit affirmed suppression: "the totality of the circumstances known by Officer Idler when he detained Daniels did not amount to reasonable suspicion. As such, Daniels' detention was unreasonable under the Fourth Amendment, and the district court's grant of Daniels' motion to suppress was proper." — slip op. at 6.

## Application
Each factor fell short. The non-emergency "area watch" tip alleged no illegality and described men in dark hoodies — a description Daniels, in a bright orange jumpsuit, plainly did not match, so the tip could supply suspicion only as to the individuals and things it described. The dark SUV's presence and its unhurried departure were not inherently suspicious, and Daniels's mere proximity and apparently saying something to it did not make him suspicious by association. The late hour and high-crime location added little, and the reported handling of firearms carried limited weight where public carry may be lawful. Taken together, the circumstances left Officer Idler acting on "an arbitrary hunch," not reasonable suspicion particularized to Daniels.

## Conclusion
**Affirmed**: the district court properly suppressed Daniels's name as the fruit of an unlawful detention. Seymour, J., wrote for the court (Eid, Seymour, Kelly, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Daniels* reinforces that reasonable suspicion must be particularized to the person seized: a suspect who does not match a tip's description, and whose only connection is proximity to a described vehicle in a high-crime area at night, cannot be detained on the tip or by association — echoing *[[United States v. Black]]* on lawful firearm activity and suspicion by association.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key*
- [[Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Daniels*, 101 F.4th 770 (10th Cir. 2024)](https://www.courtlistener.com/opinion/9500360/united-states-v-daniels/) — pinpoint: slip op. at 6 (totality / no-reasonable-suspicion holding); the CL opinion text carries the slip-opinion page numbers rather than 101 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "744a54be945efaa0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Daniels"}, "payload": {"all": [{"cite": "101 F.4th 770", "page": "770", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}], "display": "101 F.4th 770", "official": {"cite": "101 F.4th 770", "page": "770", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "101"}, "official_selection_present": true, "record_id": "United States v. Daniels"}}
{"assertion_id": "56dd8573f54abf8d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Daniels"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Daniels", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Daniels

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Daniels",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Daniels",
    "case_name_short": "Daniels",
    "case_name_full": "",
    "input_case_name": "United States v. Daniels",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2024-05-08",
    "year": 2024,
    "docket": "22-1378",
    "cluster_id": 9500360,
    "lead_opinion_id": 9966973,
    "sibling_ids": [],
    "absolute_url": "/opinion/9500360/united-states-v-daniels/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "101 F.4th 770",
      "volume": "101",
      "reporter": "F.4th",
      "page": "770",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "101 F.4th 770",
        "volume": "101",
        "reporter": "F.4th",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "101 F.4th 770",
    "official_selection": {
      "court_class": "coa",
      "selected": "101 F.4th 770",
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
    "date_created": "2026-07-07T01:39:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-daniels--9500360",
      "to_record_id": "United States v. Daniels",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Daniels

```
Appellate Case: 22-1378    Document: 010111045898         Date Filed: 05/08/2024 Page: 1
                                                                                 FILED
                                                                     United States Court of Appeals
                                         PUBLISH                             Tenth Circuit

                        UNITED STATES COURT OF APPEALS                       May 8, 2024

                                                                        Christopher M. Wolpert
                              FOR THE TENTH CIRCUIT                         Clerk of Court


   UNITED STATES OF AMERICA,

         Plaintiff - Appellant,

   v.                                                              No. 22-1378

   LYNDELL DANIELS,

         Defendant - Appellee.



                      Appeal from the United States District Court
                              for the District of Colorado
                          (D.C. No. 21-CR-00332-RMR)
                        _________________________________

 Elizabeth S. Ford Milani, Assistant United States Attorney (Cole Finegan, United States
 Attorney, with her on the brief), Office of the United States Attorney, Denver, Colorado,
 for Plaintiff-Appellant.

 John C. Arceci, Assistant Federal Public Defender (Virginia L. Grady, Federal Public
 Defender, with him on the briefs), Office of the Federal Public Defender, Denver,
 Colorado, for Defendant-Appellee.
                          _________________________________

 Before EID, SEYMOUR, and KELLY, Circuit Judges.
                   _________________________________

 SEYMOUR, Circuit Judge.
                     _________________________________

        Mr. Lyndell Daniels was detained by law enforcement who, by using his name,

 connected Daniels to a stolen Glock and charged him with being a felon in possession of a
Appellate Case: 22-1378     Document: 010111045898         Date Filed: 05/08/2024       Page: 2


 firearm in violation of 18 U.S.C. § 922(g)(1). Daniels moved to suppress his name as the

 fruit of an unlawful investigative detention, arguing the officers had no reasonable

 suspicion to detain him. The district court agreed and granted his motion. On appeal, the

 government argues the district court erred because there was reasonable suspicion to detain

 Daniels. We affirm.

                                         Background

        Just before midnight on February 7, 2021, the Aurora Police Department received a

 near-anonymous call. The caller expressed concern over something happening in her

 apartment complex’s parking lot: Three Black men, wearing dark hoodies and jeans, were

 intermittently taking guns in and out of their pockets and getting in and out of a dark SUV.

 The caller believed they were “getting ready to do something,” but conceded that it was not

 an emergency and reported no illegality. Rec., vol. I at 55. The call was logged as a non-

 emergency “area watch.” Id.

        Aurora Police Officers William Idler and Glenn Snow were dispatched to the

 caller’s apartment, located in a high-crime neighborhood of Aurora, Colorado. The

 complex was densely populated, and the parking lot was well-lit. Officer Idler arrived first

 and identified what he assumed to be the reported dark SUV. Standing five to ten feet away

 from the SUV was Daniels. Daniels was wearing a bright orange jumpsuit with a reflective

 strip and an orange hood under a black jacket. Officer Idler testified that as he approached,

 Daniels appeared to say something (which he could not hear) to the SUV. At that point, the

 SUV left the parking lot at a normal rate of speed. Officer Idler identified himself and




                                               2
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024      Page: 3


 ordered Daniels to put his hands up. Daniels immediately complied and was detained.

 Officer Idler acquired Daniels’ name, ran a criminal background check, and discovered he

 was a convicted felon.

        Police separately followed the dark SUV. The car drove lawfully, but eventually ran

 a red light and was stopped. Within the vehicle, officers found four firearms, one of which

 was a stolen 9mm Glock 17. Using Daniels’ name, law enforcement obtained a warrant for

 his DNA. Subsequent forensic testing of the DNA tied Daniels to the stolen Glock. A grand

 jury indicted Daniels on the sole count of being a felon in possession of a firearm in

 violation of 18 U.S.C. § 922(g)(1). In response, Daniels moved to suppress his name as the

 fruit of Officer Idler’s unlawful detention. The district court held an evidentiary hearing

 and then granted his motion. This appeal followed.

                                              Discussion

        The government argues that the district court erred in granting Daniels’ motion to

 suppress because Officer Idler had reasonable suspicion to detain Daniels. When reviewing

 a district court’s grant of a motion to suppress, we review factual findings for clear error

 and legal determinations de novo. United States v. Morales, 961 F.3d 1086, 1090 (10th Cir.

 2020). “[We] view[] the evidence in the light most favorable to the district court’s

 decision.” Id. The ultimate question of reasonableness under the Fourth Amendment we

 review de novo. Id.

        The Fourth Amendment establishes a right to be free from “unreasonable searches

 and seizures.” U.S. Const. amend. IV. Even so, in Terry v. Ohio, 392 U.S. 1 (1968), the




                                                3
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 4


 Supreme Court clarified that “a police officer may in appropriate circumstances and in an

 appropriate manner approach a person for purposes of investigating possibly criminal

 behavior even though there is no probable cause to make an arrest.” 392 U.S. at 22. In

 other words, the Fourth Amendment permits temporary detentions of individuals—so long

 as “the facts available to the officer at the moment of the seizure or the search ‘warrant a

 man of reasonable caution in the belief’ that the action taken was appropriate.” Id. at 21–

 22. See also United States v. McHugh, 639 F.3d 1250, 1255 (10th Cir. 2011) (observing

 that the Fourth Amendment protects individuals from unreasonable “investigatory stops”

 and detentions). To be “reasonable” a police officer’s investigatory stop must be “justified

 at its inception,” and the “officer’s actions must be reasonably related in scope to the

 circumstances which justified the interference in the first place.” United States v. Madrid,

 713 F.3d 1251, 1256 (10th Cir. 2013) (quoting Terry, 392 U.S. at 20) (internal quotations

 omitted). This appeal concerns only the first prong, i.e., whether Daniels’ detention by

 Officer Idler was justified at its inception.

        “An investigatory detention is justified at its inception if the specific and articulable

 facts and rational inferences drawn from those facts give rise to a reasonable suspicion a

 person has or is committing a crime,” id. (quoting McHugh, 639 F.3d at 1255), or “that

 criminal activity ‘may be afoot.’” United States v. Sokolow, 490 U.S. 1, 7 (1989). Police

 officers must have “reasonable suspicion that criminal activity ‘is, has, or is about to

 occur.’” United States v. Copening, 506 F.3d 1241, 1246 (10th Cir. 2007); see also United

 States v. Cortez, 449 U.S. 411, 417 (1981) (“An investigatory stop must be justified by




                                                 4
Appellate Case: 22-1378        Document: 010111045898         Date Filed: 05/08/2024       Page: 5


 some objective manifestation that the person stopped is, or is about to be, engaged in

 criminal activity.”). It is true that “the likelihood of criminal activity need not rise to the

 level required for probable cause,” United States v. Arvizu, 534 U.S. 266, 274 (2002), but it

 is equally true that officers cannot rely on “inchoate and unparticularized suspicion[s] or

 ‘hunch[es].’” Sokolow, 490 U.S. at 7. The Fourth Amendment requires “some minimal

 level of objective justification.” Id. The objective nature of this standard is key. See Terry,

 392 U.S. at 21–22 (“[I]t is imperative that the facts be judged against an objective standard

 . . . .”) (emphasis added).

        To determine whether a detaining officer had the required “particularized and

 objective basis for suspecting [a] particular person stopped of criminal activity,” we

 consider the “totality of the circumstances—the whole picture.” Cortez, 449 U.S. at 417–

 18. When making that determination, “a court may not evaluate and reject each factor in

 isolation.” Madrid, 713 F.3d at 1256 (quoting United States v. Gandara-Salinas, 327 F.3d

 1127, 1130 (10th Cir. 2003)). Indeed, “[c]onduct that may be wholly innocent may

 nonetheless support a finding of reasonable suspicion in certain circumstances.” United

 States v. Johnson, 364 F.3d 1185, 1192 (10th Cir. 2004). All factors, “mitigating and

 aggravating,” must be considered in the totality of the circumstances. Id. at 1193.

        The parties agree Officer Idler detained Daniels for the purposes of the Fourth

 Amendment and so was subject to its strictures. The parties and the district court further

 agree that there were four relevant factors and circumstances known to Officer Idler when

 he detained Daniels: (1) the 911 phone call and Computer Aided Dispatch (“CAD”) notes,




                                                 5
Appellate Case: 22-1378       Document: 010111045898          Date Filed: 05/08/2024       Page: 6


 (2) the presence and actions of the dark SUV, (3) the time of Officer Idler’s encounter with

 Daniels, and (4) the location of their encounter. The question before us is whether the

 district court properly analyzed and weighed these factors when determining Officer Idler

 did not have reasonable suspicion to detain Daniels. Our de novo review convinces us that

 the totality of the circumstances known by Officer Idler when he detained Daniels did not

 amount to reasonable suspicion. As such, Daniels’ detention was unreasonable under the

 Fourth Amendment, and the district court’s grant of Daniels’ motion to suppress was

 proper. We address each factor before analyzing all together to determine whether the

 totality of the circumstances established reasonable suspicion. United States v. Leon, 80

 F.4th 1160, 1166 (10th Cir. 2023).

        1. The 911 Call

        The district court began by analyzing the import of the near-anonymous 911 call. A

 tip to the police, like a 911 call, can “justify an investigatory stop if under the totality of the

 circumstances the tip furnishes both sufficient indicia of reliability and sufficient

 information to provide reasonable suspicion that criminal conduct is, has, or is about to

 occur.” Madrid, 713 F.3d at 1258. Our analysis to determine a tip’s reliability is “case-

 specific” and factor-based. United States v. Chavez, 660 F.3d 1215, 1222 (10th Cir. 2011).

 We consider:

        (1) [W]hether the informant lacked “true anonymity” (i.e., whether the police knew
        some details about the informant or had means to discover them); (2) whether the
        informant reported contemporaneous, firsthand knowledge; (3) whether the
        informant provided detailed information about the events observed; (4) the
        informant’s stated motivation for reporting the information; and (5) whether the
        police were able to corroborate information provided by the informant.


                                                 6
Appellate Case: 22-1378      Document: 010111045898           Date Filed: 05/08/2024        Page: 7



 Id. “[N]o single factor is dispositive.” Id.

        The district court eschewed this factor-based inquiry for a comparison between the

 instant case and Florida v. J.L., 529 U.S. 266 (2000), in which the Supreme Court found

 that “the bare report of an unknown, unaccountable informant,” unaccompanied by

 “specific indicia of reliability” was insufficient to establish reasonable suspicion. 529 U.S.

 at 269, 271. While the district court’s comparative analysis was not per se improper, see

 Chavez, 660 F.3d at 1222 (comparing the factual circumstances between J.L. and the case

 before it), it was insufficient. Since J.L., our circuit has articulated the nature of those

 “specific indicia of reliability,” and the district court should have evaluated the presence

 (or lack thereof) of those indicia in its analysis. See, e.g., Chavez, 660 F.3d at 1222;

 Copening, 506 F.3d at 1247; United States v. Brown, 496 F.3d 1070 (10th Cir. 2007);

 Madrid, 713 F.3d at 1258. United States v. Johnson is illustrative: There, when considering

 the reliability of an anonymous tip, we were “mindful of the concerns expressed in J.L.,”

 but ultimately evaluated those concerns alongside the specific facts of Johnson’s case. See

 364 F.3d at 1191.

        As we review the facts of this case under the proper analysis, the call is close. All

 the indicia we traditionally consider appear to be present, but to varying degrees of

 potency. The 911 call alone was certainly insufficient to establish reasonable suspicion—

 indeed, the government itself does not contend that it was sufficient—and the call’s

 reliability, even when placed alongside the other facts of this case, is not determinative.




                                                 7
Appellate Case: 22-1378       Document: 010111045898          Date Filed: 05/08/2024       Page: 8


          Nonetheless, even assuming its reliability, we afford the 911 call little weight. In

 Navarette v. California, 572 U.S. 393 (2014), the Supreme Court observed that even a

 reliable tip must create “reasonable suspicion that ‘criminal activity may be afoot.’” 572

 U.S. at 401 (citing Terry, 392 U.S. at 30). As an example, it noted that “a reliable tip

 alleging the dangerous behaviors [consistent with drunk driving] would justify a traffic

 stop on suspicion of drunk driving.” Id. at 402. Here, we have assumed arguendo the 911

 call’s reliability, but that inquiry is separate from its utility in establishing reasonable

 suspicion. Id. The tip alleged no criminal activity or dangerous behaviors; the caller only

 reported that guns were being intermittently taken in and out of pockets, and that the three

 Black men “look like they are getting ready to do something.” Rec., vol. I at 57. This may

 be odd, but it is not obviously illegal. Moreover, if we are to take seriously the normative

 thrust of the Supreme Court’s recent decision in New York State Rifle & Pistol Association,

 Inc., v. Bruen, 597 U.S. 1 (2022), then we cannot look with suspicion on citizens

 presumably exercising their Second Amendment rights in a lawful way. 597 U.S. at 70

 (“The constitutional right to bear arms in public for self-defense is not a ‘second-class right

 . . . .”).

          Granted, “reasonable suspicion may exist even where a 911 call fails to allege

 criminal activity,” see United States v. Conner, 699 F.3d 1225, 1231 (10th Cir. 2012), but

 the described activity here, i.e., three Black men looking like they were about to “do

 something,” getting in and out of an SUV, is simply too generic. The men were not yelling

 or hollering or running or disturbing anyone or, frankly, doing much of anything. Another




                                                 8
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 9


 caller reporting that she was nervous because three armed Black men were relaxing

 alongside an SUV would have been just as descriptive and (un)helpful in establishing

 reasonable suspicion.

        The tip is even less useful in establishing reasonable suspicion for Daniels. Recall,

 the 911 call could have only helped establish reasonable suspicion for the individuals or

 things described. United States v. Fisher, 597 F.3d 1156, 1158–59 (10th Cir. 2010) (“The

 particular person that is stopped must be suspected of criminal activity.”). The district court

 found that it would have been “objectively unreasonable” for Officer Idler to believe that

 Daniels was one of the men described, because he “so obviously did not match the

 description of the individuals identified by the caller.” Rec., vol. I at 115. When asked

 during testimony, Officer Snow, who accompanied Officer Idler to the scene, agreed that

 Daniels “did not match the description . . . that the caller had given.” Rec., vol. IV at 76.

 “Other than the fact that he was black, there was nothing about the Defendant to suggest

 that he was one of the individuals described by the 911 caller.” Rec., vol. I at 115. We

 agree. That criminal activity might be afoot does not give police carte blanche to arrest

 everyone who happens to be nearby. See Fisher, 597 F.3d at 1158–59.

        We consider the 911 call in our totality analysis, but we appropriately “discount” the

 weight we afford it because of the call’s supergeneric, innocuous nature and because

 Daniels himself was not described in it. Johnson, 364 F.3d at 1192.




                                                9
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 10


         2. The Presence and Actions of the SUV

         The district court next considered the weight that should be given to the presence

  and actions of the dark SUV that was idling in the parking lot and that then drove away

  (ostensibly at the direction of Daniels) as Officer Idler approached. We hold that the SUV

  and its actions were insufficient alone to establish reasonable suspicion.

         The government argued below and to us that Officer Idler had reasonable suspicion

  to stop Daniels because of Daniels’ association with the SUV. We interpret this argument

  as raising two important inquiries: (1) whether the SUV itself was reasonably suspicious

  because of its presence and actions, and (2) the nature of Daniels’ association with the

  SUV.

         We address first whether the dark SUV itself was reasonably suspicious. The SUV

  at issue was idling in front of Daniels’ apartment complex as Officer Idler approached. But

  it was far from the only vehicle present. Officer Idler’s bodycam shows at least three other

  cars idling in front of the complex; at least three cars leaving or driving through the lot; one

  car parked in the no-parking loading zone; and no open parking spots to be seen. In other

  words, the parking lot was packed and busy, especially given the late hour. In that context,

  we do not find the dark SUV’s mere presence in the lot to be odd, much less suspicious.

  We do not ignore that the 911 call reported that there was a “dark color SUV” in the

  parking lot. And, indeed, so there was. But the tip’s support is ultimately superficial, and

  its practical utility limited. The bodycam footage shows two “dark color” SUVs, one black,

  the other burgundy, idling in the complex’s lot, one right behind the other. The SUV at




                                                10
Appellate Case: 22-1378       Document: 010111045898           Date Filed: 05/08/2024       Page: 11


  issue in this case turned out to be the black SUV, but the caller gave no hint which one she

  was referring to. The CAD notes are absent of any make, model, color, or license plate

  number.1 It was a coin flip then, as equally likely to be wrong as right, by Officer Idler

  when deciding which SUV’s presence in the lot was “suspicious.” In that sense, even

  assuming the tip’s “reliabil[ity] in its assertion of illegality,”2 it was certainly not reliable

  “in its tendency to identify a determinate person [or thing].” J.L., 529 U.S. at 272. We are

  generally skeptical of anonymous or near-anonymous tips, and even more skeptical when

  they are supergeneric, as here. See Johnson, 364 F.3d at 1191 (“Overly generic tips, even if

  made in good faith, could give police excessive discretion to stop and search large numbers

  of citizens.”). The situation faced by Officer Idler as he approached the complex and was

  forced to proceed on an arbitrary hunch is a good illustration why.

           Moreover, although reasonable suspicion does not demand witnessing illegal

  conduct, Conner, 699 F.3d at 1231 (“Reasonable suspicion may exist even where . . . the

  responding officers do not observe any illegal conduct.”), Officer Idler did not observe any

  criminal activity or even the guns reported by the 911 tipster, weakening the claim that the

  SUV was inherently suspicious.3 Indeed, our review of the record indicates that Officer


  1
   The CAD notes did provide slightly more description for a nearby sedan, which the caller
  described as either “sil[ver] or white.” Rec., vol. I at 58.
  2
      Which, we again emphasize, the tip did not allege.
  3
    The district court made a factual finding that “Further, there is no evidence here that the
  officers observed anything to suggest that the SUV or its occupants were carrying guns or
  otherwise engaged in illegal activity.” Rec., vol. I at 117. Our independent review of the
  record confirms this assessment. Morales, 961 F.3d at 1090.


                                                  11
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024     Page: 12


  Idler did not witness any activity whatsoever by anyone in or near the SUV before the SUV

  drove away. We are ever “mindful of the concerns expressed in J.L.,” Johnson, 364 F.3d at

  1191, and we find the facts of this case uncomfortably reminiscent of the facts there. In

  J.L., aside from an anonymous tip, the “officers had no reason to suspect” J.L. and his

  friends of any illegal conduct, the officers “did not see a firearm,” J.L. and his friends made

  no threatening or otherwise unusual movements, and when the officers approached, J.L.

  was “just hanging out.” J.L., 529 U.S. at 268. Here, there was a near-anonymous tip that

  did not allege illegal conduct, no illegal conduct or firearms were seen, neither the SUV

  nor Daniels made any threatening or unusual movements, and the SUV appeared to be

  innocuously idling as Officer Idler approached.

         Of course, the SUV did drive away as Officer Idler approached (ostensibly at

  Daniels’ direction in Officer Idler’s recount). This action by the SUV offers more, but

  ultimately insufficient, support to establish reasonable suspicion. Certainly, we can and do

  consider a suspect’s evasive movements in determining reasonable suspicion, see, e.g.,

  United States v. Briggs, 720 F.3d 1281, 1286 (10th Cir. 2013), and “headlong flight” is far

  from the only behavior that is fair game, see id. at 1287.4 The facts here make it difficult to


  4
   Our caselaw requires something more than just walking away when the police arrive.
  After all, “not all attempts to avoid police contact raise suspicion[].” Briggs, 720 F.3d at
  1287. The government cites several cases, but none are persuasively analogous. In United
  States v. Briggs, the defendants “changed direction” and “picked up their pace”; Briggs
  “repeatedly looked over his shoulder” and “grabbed at the waistline of his pants”; and one
  defendant was “nearly running.” 720 F.3d at 1283,1287. In United States v. Ballance, we
  admitted that Ballance’s “walking away from [a] gas station on foot” supported reasonable
  suspicion, but there was a tip alleging illegality and identifying Ballance’s specific car. No.



                                                12
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024     Page: 13


  determine whether the SUV was attempting to evade the police as it drove away. The

  district court did not think it was, finding that the “SUV here simply left the parking lot.”

  Rec., vol. I at 117. The government does not allege that finding was clearly erroneous, and

  upon our review of the record, we agree. See Morales, 961 F.3d at 1090. The bodycam

  shows the SUV driving away at a normal rate of speed, a speed similar to that of a white

  car that can be seen leaving as Officer Idler arrived. According to Officer Snow, who had a

  better vantage point, the black SUV did not appear to drive away “at a high rate of speed”

  or “jump a curb or anything like that,” and otherwise simply, and safely, departed. Rec.,

  vol. IV at 74. Further, the burgundy SUV left during the encounter, and another vehicle

  drove several yards away when Officer Idler approached. This confirms that the parking lot

  was busy with activity. We cannot say that simply leaving the lot, as the bodycam footage

  shows several other cars similarly doing, indicated that criminal activity was afoot. In

  United States v. Davis, 94 F.3d 1465 (10th Cir. 1996), we found that a defendant’s “actions

  in exiting [a] car, making and then breaking eye contact with the officers, and then walking

  away from the officers” was not sufficient alone to establish reasonable suspicion. The

  facts in this case offer even less support. 94 F.3d at 1468. The SUV driving away at a

  normal rate of speed as Officer Idler approached is not enough to establish the


  20-3141, 2022 WL 108330, at *6 (10th Cir. Jan. 12, 2022) (unpublished). United States v.
  Madrid stands for the proposition that the defendant’s “attempted exit from [a] parking lot
  just after a police car drove by” could be considered in the reasonable suspicion analysis,
  713 F.3d at 1257, which the district court here did not dispute. United States v. Robinson is
  the only case cited that has held that a simple “about-face” could contribute, but it is
  unpublished and its analysis is conclusory. 304 F.App’x 746, 751 (10th Cir. 2008)
  (unpublished).


                                                13
Appellate Case: 22-1378        Document: 010111045898        Date Filed: 05/08/2024     Page: 14


  “particularized and objective basis for suspecting” it of criminal activity. Cortez, 449 U.S.

  at 417.

            That leads to our second inquiry, Daniels’ association with the SUV. We interpret

  the government as arguing that Daniels’ interaction with the SUV (ostensibly warning the

  SUV to leave as Officer Idler approached) both contributed to the reasonable suspicion of

  the SUV and linked Daniels to it. We are unpersuaded, because Daniels’ connection to the

  SUV appears tenuous. The government alleges that the SUV left at the direction of

  Daniels. But Officer Idler did not hear what Daniels may have said to the SUV’s

  occupants. True, we do “accord deference to an officer’s ability to distinguish between

  innocent and suspicious actions,” see Madrid, 713 F.3d at 1256, but we are not required to

  take on blind faith an officer’s speculation on the contents of a conversation he admits he

  could not hear.5 A fair inference for Officer Idler to have made was that there was some

  relationship between the occupants of the SUV and Daniels. But the nature of that

  relationship was unknown. This inference may have been sufficient if the SUV had done

  something else to be reasonably suspicious, but the other facts do not substantially indicate

  that Officer Idler had a “particular and objective basis” to suspect either Daniels (or the



  5
    Indeed, we are especially reticent to accord much deference to Officer Idler’s instincts
  given his contradictory narratives. In his summary of the stop, related the following day,
  Officer Idler reported a mundane, if ambiguous, scene: “I heard [Daniels] saying
  something when the Dark SUV pulled out of the parking lot and fled the scene.” Rec., vol.
  I at 28. However, at his testimony, Officer Idler’s story recast Daniels into the role of
  scout, warning the SUV to flee as he approached: “[T]he person in the orange jumpsuit
  with the black jacket on [Daniels] I heard say something to the people inside the black
  SUV, and then the black SUV took off.” Rec., vol. IV at 29.


                                                 14
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024        Page: 15


  SUV) had been or was committing a crime. See id. That is, after all, our reasonable

  suspicion lodestar: whether the facts tended to show that Daniels committed or was about

  to commit a crime. See Johnson, 364 F.3d at 1189. His proximity to an innocuous SUV and

  an unknown conversation with its occupants who then simply left when Officer Idler

  approached do not tend to show that.

         All of this can and must be considered in our final totality of the circumstances

  analysis, but we agree with the district court that neither the SUV’s nor Daniels’ presence

  or actions are sufficient alone to establish reasonable suspicion.

         3. The Time and Location

         The district court finally considered the location and time of Officer Idler’s

  encounter with Daniels. It observed that the stop occurred in a “high crime area” of Aurora,

  Colorado “in the middle of the night,” and concluded that those facts, although insufficient

  alone, could be considered in the totality of the circumstances analysis. We agree.6

         Of course, these factors do not operate as a “check-the-box” exercise or foreclose

  analysis of “relevant contextual considerations.” Wardlow, 528 U.S. at 124. Here, Officer

  Idler detained Daniels near midnight. But the evening in question was February 7, 2021,



  6
    Caselaw has extensively established that such facts can be considered. See, e.g., Illinois v.
  Wardlow, 528 U.S. 119, 124 (2000); McHugh, 639 F.3d at 1257; United States v. DeJear,
  552 F.3d 1196, 1201 (10th Cir. 2009) (noting that “the fact that conduct occurs in an area
  known for criminal activity” should be considered when determining reasonable
  suspicion); United States v. Clarkson, 551 F.3d 1196, 1202 (10th Cir. 2009) (“This court
  has also considered the time of night as a factor in determining the existence of reasonable
  suspicion.”); Gallegos v. City of Colo. Springs, 114 F.3d 1024, 1029 (10th Cir. 1997)
  (considering the time of night, 1:15 AM, in the reasonable suspicion analysis).


                                                15
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024      Page: 16


  the night of the Super Bowl LV. An officer should have expected football fans celebrating

  (or commiserating about) the game’s outcome late into the night. The time of day Officer

  Idler encountered Daniels is militated by the events of that day. Moreover, the district court

  found the parking lot was “well-lit,” “densely populated,” and “heavily trafficked,” and we

  agree. Rec., vol. I at 119. This further militates against finding reasonable suspicion,

  because any actions taken by the SUV’s occupants (or Daniels) would be easily seen and

  quickly reported, which Officer Idler would have known.

         That the neighborhood was a “high-crime area” with police often getting calls for

  “domestic violence or people with weapons or other such various felonies or intense

  crimes,” Rec., vol. IV at 20–21, did offer some objective and particularized reason for

  suspicion. But caselaw has been skeptical that such a factor can carry the day. See, e.g.,

  United States v. Dennison, 410 F.3d 1203, 1208 (10th Cir. 2005) (“[Defendant]’s presence

  in a high-crime area is not, ‘standing alone,’ enough to provide reasonable suspicion, but it

  may be a ‘relevant contextual consideration’ in a Terry analysis.”).

         Both the time and location factors are relevant, and so we consider them in our

  totality of the circumstances analysis below. But neither one was sufficient by itself to

  establish reasonable suspicion.

         4. Totality of the Circumstances

         Having concluded that none of those factors alone establish reasonable suspicion,

  our task is now to consider the “totality of the circumstances—the whole picture,” faced by

  Officer Idler as he approached and detained Daniels. Cortez, 449 U.S. at 417–18.




                                                16
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024     Page: 17


         Our review of the records shows the following circumstances were known to Officer

  Idler as he approached and detained Daniels on that fateful February 7th night: (1) the

  police received an arguably reliable tip describing three Black men in dark clothing,

  holding guns, and getting in and out of a dark SUV; (2) the tipster believed the men were

  about to “do something” but reported no illegality; (3) based on the call, Officers Snow and

  Idler were dispatched on a “non-emergency area watch request”; (4) the officers did not see

  any of the men identified by the caller, but possibly identified the “dark color SUV”

  reported as a black SUV idling in front of the complex; (5) the officers did not see any

  guns or illegal activity when they arrived; (6) Officer Idler saw Daniels who was wearing a

  bright orange jumpsuit, orange jeans, and a black jacket; (7) Daniels was standing five to

  ten feet away from the black SUV; (8) Officer Idler thought he heard Daniels say

  something to the SUV, after which the SUV left the lot at a “normal rate of speed”; (9)

  Daniels did not have any guns, did not attempt to leave the scene, and initially complied

  with all of Officer Idler’s orders; (10) the encounter took place near midnight; (11) the stop

  was in a high-crime area; and (12) the parking lot was busy, packed, and well-lit. Like the

  district court, we are not persuaded that these circumstances provided Officer Idler with

  reasonable suspicion to detain Daniels.

         We again emphasize the principle that anchors our analysis: Officer Idler had to

  have a “particularized and objective basis” to believe Daniels had been or was committing,

  or was about to commit a crime or engage in criminal activity. Cortez, 449 U.S. at 417–18.

  That minimal objective basis was not met here. The supergeneric and vague 911 tip did not




                                               17
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 18


  allege illegal, or even particularly unusual, activity by the men the caller identified, and

  nowhere at all did it describe anyone akin to Daniels. As Officer Idler arrived, he was

  confronted by an unremarkable, frankly banal, scene: a packed and busy apartment parking

  lot with several cars leaving, idling in, and driving through it. It was perhaps a bit more

  puzzling given the late time of night, but that could have been plausibly explained by the

  trouncing the Buccaneers had shown the Chiefs only a few hours prior.7 As the caller had

  described, there was a “dark colored SUV” outside, two in fact, but no hint as to which one

  the caller had been referring. Despite the area’s reputation as a “high-crime area,” the

  bodycam footage shows nothing was amiss, much less dangerous, as Officer Idler

  approached the scene. Officer Idler admitted that he did not see any weapons when he

  arrived. As he approached, he heard Daniels say something (ostensibly to the SUV) and

  saw the black SUV, which had been idling, leave at a normal, lawful speed. Neither before

  nor after being stopped did Daniels make any threatening or evasive movements, and he

  complied with all Officer Idler’s orders. Daniels had no firearms on him, and he was

  dressed in a bright, eye-catching orange jumpsuit—which seems to be a somewhat

  counterintuitive fashion choice for someone committing, or about to commit, a crime and

  hoping to get away with it.

         The most glaring thing about these circumstances viewed together is what there is

  not: any hint of any kind of illegality whatsoever. True, “[c]onduct that may be wholly



  7
    For those keeping score, the Buccaneers ended the night with a final victory of 31–9 over
  the Chiefs.


                                                18
Appellate Case: 22-1378      Document: 010111045898           Date Filed: 05/08/2024      Page: 19


  innocent may nonetheless support a finding of reasonable suspicion in certain

  circumstances,” but here we have trouble identifying anything but innocent conduct.

  Johnson, 364 F.3d at 1192. Even analyzing everything together, we are not persuaded the

  circumstances known to Officer Idler “tend to show that [Daniels had] committed or [was]

  about to commit a crime,” as reasonable suspicion demands. Id. at 1189. There are precious

  few facts to suggest that criminal activity was “afoot”—and fewer still that Daniels had any

  role in it, if it was. Whatever is needed to establish reasonable suspicion, this case falls

  short of that minimal particularized and objective basis we have always required. Because

  there was no reasonable suspicion to stop Daniels, Officer Idler’s investigatory detention of

  him was unreasonable under the Fourth Amendment, and the district court’s order to

  suppress was proper.

         Before concluding, we address two of the government’s arguments that the district

  court’s process when conducting its totality of the circumstances analysis was improper.

  First, the government appears to suggest that the district court should not have been

  allowed to consider and weigh the innocent and unsuspicious facts in the record when

  determining whether Officer Idler had reasonable suspicion. See Aplt. Br. at 27; Aplt.

  Reply at 11. To the extent that is their argument, it is certainly wrong. The district court

  was not only empowered, but required, to evaluate all the factors in the record when

  analyzing reasonable suspicion, including facts militating against reasonable suspicion. See

  Johnson, 364 F.3d at 1193 (“All of the[] factors, mitigating and aggravating, should have




                                                 19
Appellate Case: 22-1378       Document: 010111045898           Date Filed: 05/08/2024          Page: 20


  been analyzed as part of the totality of the circumstances faced by Officer Middleton at the

  inception of the detention.”).

         Second, the government contends that the district court analyzed each factor (the

  911 call, the SUV, the time and location) in isolation, rather than weighing them together.

  To illustrate the kind of analysis we have found impermissible, it points us to Johnson.

  There, too, the district court granted a motion to suppress based on four factors. See id. at

  1189–90. The court conducted its totality analysis by “proceed[ing] through the factors . . .

  evaluat[ing] and reject]ing] each before moving on to the next.” Id. at 1190. The court

  mentioned the “appropriate ‘totality of the circumstances’ standard only once, in passing,

  and only after having analyzed each factor . . . in isolation.” Id. This, we found, was

  improper. Id. at 1189.

         Here, the district court avoided the improper process in Johnson. It analyzed each

  factor individually, but it was clear that it would consider all the facts in its totality

  analysis: “This Court will analyze each fact, and it will then consider all the facts together

  to determine whether the totality of the circumstances supports a finding of reasonable

  suspicion sufficient to support the Defendant’s detention.” Rec., vol. I at 111 (emphasis

  added). The court did not say that it would consider “all the facts that support reasonable

  suspicion”; it said “all the facts”—even those it found would not support reasonable

  suspicion alone. It lived up to its promise. It dedicated an entire section to its totality

  analysis, separate from the factors, as we have here. In that analysis, the court included




                                                  20
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024     Page: 21


  discussion of the 911 call and the SUV along with all the other facts, despite finding the

  former two insufficient to support reasonable suspicion alone.

         The court engaged in the exact process we have approved. It analyzed the relevant

  factors to determine whether, standing alone, they supported reasonable suspicion;

  discounted those factors that were weak based on the record; and finally considered all the

  factors together to analyze as required. That the government was unhappy with the result is

  not enough to transform its substantive distaste into procedural error.

                                              Conclusion

         Because the circumstances confronting Officer Idler did not amount to reasonable

  suspicion, his detention of Daniels was unreasonable under the Fourth Amendment. As

  such, the district court properly granted Daniels’ motion to suppress. We affirm.




                                               21
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 22



  22-1378, United States v. Daniels
  EID, J., concurring in the judgment.

         I generally agree with the majority’s opinion, but write separately to express my

  view regarding the degree of suspicion to be assigned to the 911 call. The majority

  thinks that the 911 caller described nothing but innocuous conduct. Maj. Op. at 10

  (reasoning that the caller described three men armed with guns who only acted

  “innocuous[ly]”). I disagree. At the same time, however, I agree with the majority that

  any reasonable suspicion from the call did not attach to Daniels for a simple reason: He

  did not match the caller’s description of the men engaged in suspicious activity.

         To begin, unlike the majority, I would find that the 911 caller described three men

  acting suspiciously. Late at night, at about 11:35 PM, someone called the police

  reporting that three Black men in dark clothing visibly held “guns in their hands” and

  “intermittently t[ook] out [the] guns and then put[] them back into their pockets.” App’x

  Vol. I at 107, 112. The caller stated that the men appeared as if “they [we]re getting

  ready to do something.” Id. at 112. And the caller went on to say that these three men

  repeatedly got “in and out” of a “dark color SUV.” Id. at 107.

         If a police officer were to observe that situation, I would think that the three men’s

  “unusual conduct” would lead the officer “reasonably to conclude in light of his

  experience that criminal activity may be afoot and that the persons with whom he is

  dealing [are] armed and presently dangerous.” Terry v. Ohio, 392 U.S. 1, 30 (1968).

         The majority thinks differently. First, as part of its reasoning, the majority states

  that the 911 call did not establish reasonable suspicion because the officers took the call
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024       Page: 23



  as a “non-emergency area watch request.” Maj. Op. at 17. It is true that the 911 caller

  also stated that the situation described was “currently not an emerg[ency].” App’x Vol. I

  at 112. But surely reasonable suspicion may arise outside of an emergency. What makes

  that clear is that an officer may confirm or dispel suspicion of a crime before it occurs.

  See, e.g., Terry, 392 U.S. at 30 (involving officers who suspected that two men appeared

  to be “casing a job” by walking in front of and peering into a store several times).

  Indeed, crime can still be afoot without an emergency, such as while suspects prepare for

  a crime, whether it be casing a store for a future robbery or putting guns and equipment in

  a car like the 911 caller described. Compare id., with App’x Vol. I at 107, 112

  (describing men in dark clothing getting in and out of an SUV while armed with guns in-

  hand and appearing as if “they [we]re getting ready to do something” close to midnight).

         As the primary reason for finding no suspicious activity from the call, the majority

  places great weight on an assumption that the call “alleged no criminal activity or

  dangerous behaviors.” Maj. Op. at 8 (“[T]he caller only reported that guns were being

  intermittently taken in and out of pockets, and that the three men ‘look like they are

  getting ready to do something.’” (citation omitted)). In reaching its holding, the majority

  relies on the “normative thrust of the Supreme Court’s recent decision in” New York State

  Rifle & Pistol Association, Inc. v. Bruen, 597 U.S. 1 (2022), to reason that the three men

  here were “presumably exercising their Second Amendment rights in a lawful way.”

  Maj. Op. at 8 (emphasis added).

         The problem with the majority’s reasoning is that we do not know for certain,

  under the relevant law or the record, whether the open carry of firearms here was

                                                   2
Appellate Case: 22-1378     Document: 010111045898         Date Filed: 05/08/2024        Page: 24



  “lawful” or not. Id. Colorado leaves the regulation over the open carry of firearms to its

  local and municipal authorities. See Colo. Rev. Stat. Ann. § 29-11.7-104. Looking to the

  relevant locality here, the City of Aurora leaves the lawfulness of open carried firearms

  up to public and private property owners.1 With that in mind, the law here does not

  necessarily clarify whether the three men described in the 911 call could carry openly

  because we do not know if the apartment parking lot had any restrictions on open carry of

  a firearm. And the record does not help us out either in that regard.

         This is not a case where we know that individuals merely “exercise[ed] their

  Second Amendment rights in a lawful way.” Contra Maj. Op. at 8. Or at least, nothing

  from the law or record indicates that is the case. Even so, based on nothing more than

  speculation, the majority holds that the men “presumably” open carried guns lawfully.

  Id. (emphasis added).

         I would not presume so. I acknowledge that the Supreme Court has said that

  “bare-boned tips about guns” do not create “an automatic firearm exception” to the

  Fourth Amendment. Florida v. J.L., 529 U.S. 266, 273 (2000). But the caller here did

  not just report that the men had guns. There was more: Again, three men dressed in dark

  clothing, actively moved in and out of cars in a parking lot close to midnight, were



         1
           See Aurora Stat. art. IV, div. 2, § 94-152(a) (providing that “[i]t shall be
  unlawful for any person, carrying a firearm, to enter or remain upon any private
  property of another or any building or property of a commercial establishment when
  such property, building, or establishment is posted with notification that the carrying
  of firearms is prohibited”); id. § 94-154(a) (providing that “[t]he carrying of firearms
  in or upon public facilities is unlawful when said facilities are posted with
  notification that the carrying of firearms is prohibited”).
                                                  3
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024       Page: 25



  visibly armed with weapons, and appeared as if “they [we]re getting ready to do

  something.” App’x Vol. I at 107, 112. That I would find amounts to a tip “that criminal

  activity may be afoot.” Terry, 392 U.S. at 30.

         In any case, however, the suspicious activity described on the call does not end

  this matter. The officers here did not view the situation described on the 911 call with

  their own eyes. Instead, the officers received a tip that needed to be corroborated.

  Importantly, “[a] police officer cannot legally detain a person simply because criminal

  activity is afoot.” United States v. Fisher, 597 F.3d 1156, 1158 (10th Cir. 2010). Instead,

  an officer must “suspect[]” that “the particular person stopped” has committed or was

  committing “criminal activity.” Id. at 1158–59.

         With that in mind, something needed to connect Daniels as one of the men

  described in the 911 call. Nothing did. Critically, the government concedes that “Officer

  Idler didn’t notice anyone in the area matching the clothing descriptions provided by the

  911 caller.” Aplt. Br. at 3. And indeed, the record reflects that no officer could

  reasonably expect Daniels to be one of the men in dark clothing described on the call.

  Daniels was not wearing a black hoodie. He instead wore a bright orange jumpsuit with a

  reflective strip across the front. The 911 call also mentioned that the three men went in

  and out of a dark colored SUV. Daniels did no such thing. Instead, he stood

  “approximately five to ten feet away” from an SUV, “outside his own home.” App’x

  Vol. I at 107, 121. And lastly, the 911 caller described that the men visibly held “guns in

  their hands and pockets.” Id. at 112. Yet again, Daniels did no such thing. At no time



                                                   4
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024        Page: 26



  did Officer Idler see Daniels with a firearm in hand or on his person, even after the

  seizure.

  As such, I agree with the majority that Daniels did not match the caller’s description. See

  Maj. Op. at 9–10.

         In sum, unlike the majority, I believe that the 911 call reported suspicious activity.

  That disagreement aside, I agree with the majority that Daniels did not match the caller’s

  description of the three men acting suspiciously. Any suspicion stemming from the call

  was dispelled when Officer Idler found no one on the scene that matched the caller’s

  description. For these reasons, I concur in the judgment.




                                                   5

```

---

## GROUP: _overhaul2/lake/cases/United States v. Donovan.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Donovan
type: case
citation: "429 U.S. 413 (1977)"
parallel_cite: "97 S. Ct. 658; 50 L. Ed. 2d 652"
neutral_cite: 1977 U.S. LEXIS 36
court: U.S.
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-18
docket: 75-212
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
  opinion_url: "https://www.courtlistener.com/opinion/109584/united-states-v-donovan/"
  cluster_id: 109584
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Donovan
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: Anchor
related:
  - "[[Electronic Surveillance and Title III]]"
  - "[[United States v. Giordano]]"
  - "[[Scott v. United States]]"
tags:
  - case
  - fourth-amendment
  - electronic-surveillance
  - title-iii
  - wiretap
  - suppression
  - inventory-notice
holding: "Title III's identification requirement, § 2518(1)(b)(iv), obliges the Government to name in a wiretap application every person it has probable cause to believe is committing the offense and whose communications will be intercepted, and § 2518(8)(d) requires it to give the issuing judge a complete list of identifiable persons overheard so the judge can decide who receives inventory notice; but the failure to comply fully with either provision does not render the interception 'unlawful' and does not require suppression, because those requirements do not directly and substantially implement Congress's purpose of confining wiretaps to situations that clearly call for them."
aliases:
  - United States v. Donovan
  - "United States v. Donovan (1977)"
---

# United States v. Donovan

*429 U.S. 413 (1977)* (No. 75-212) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109584 → combined opinion 109584 (Powell, J.; 429 U.S. 413, argued Oct. 13, 1976, decided Jan. 18, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*434` and `*435`, i.e., on page 434). S9 promotes. -->

## Background
A Title III wiretap on gambling-related telephones in Ohio named certain principal targets and "others as yet unknown." During the tap the Government learned that respondents Donovan, Robbins, and Buzzacco were discussing gambling with the named subjects, but when it sought an extension it did not add their names to the application. Later, when the Government proposed a list of persons to receive post-interception inventory notice, two other participants — Merlo and Lauer — were left off through what the Government called "administrative oversight" and never received notice. On the defendants' motions, the District Court suppressed the wiretap evidence: as to Donovan, Robbins, and Buzzacco for the failure to name them, and as to Merlo and Lauer for the failure to serve inventory notice. The Sixth Circuit affirmed, holding both requirements played a "central role" in the statute.

## Issue
Whether § 2518(1)(b)(iv) requires naming every person the Government has probable cause to believe will be overheard committing the offense; whether the Government must give the issuing judge a complete list of identifiable persons overheard under § 2518(8)(d); and whether failure to comply with those provisions requires suppression under § 2518(10)(a).

## Rule
The Court agreed the Government must identify all persons it has probable cause to believe are engaged in the offense and will be intercepted, and must supply the judge a complete list of identifiable persons overheard — but held that violating those requirements does not trigger suppression. Drawing on *[[United States v. Giordano|Giordano]]*, it explained that suppression is required only for a failure to satisfy statutory requirements that "directly and substantially implement the congressional intention to limit the use of intercept procedures"; the identification and notice provisions, though important, are not of that character: "Although both statutory requirements are undoubtedly important, we do not think that the failure to comply fully with those provisions renders unlawful an intercept order that in all other respects satisfies the statutory requirements." — 429 U.S. at 434. ^pin-434

## Application
The failure to name additional targets could not invalidate an order the issuing judge was authorized to enter, because the judge's decision to approve the wiretap turned on probable cause, necessity, and the target facilities — not on a complete roster of everyone who might later be overheard. Likewise, the post-interception notice provisions serve to inform surveilled persons after the fact; their breach did not affect the lawfulness of the interceptions themselves. Because the orders were facially sufficient and the interceptions conformed to them, the communications were not "unlawfully intercepted," and suppression was unwarranted.

## Conclusion
The judgment of the Court of Appeals for the Sixth Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Powell, J., delivered the opinion of the Court. Burger, C.J., filed an opinion concurring in part and concurring in the judgment, and there were separate opinions concurring and dissenting in part (including Marshall, J., dissenting in part).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Donovan* anchors Title III's suppression calculus: not every statutory violation makes an interception "unlawful," so suppression follows only where the breached requirement "directly and substantially" implements Congress's core limits on wiretapping. Teach it against *[[United States v. Giordano]]* (violation of the senior-approval requirement *does* require suppression) as the two poles of the *Giordano/Chavez* suppression test, and with *[[Scott v. United States]]* on minimization.

## Appears on
- [[Electronic Surveillance and Title III]] — *Anchor*

## Sources
- [*United States v. Donovan*, 429 U.S. 413 (1977)](https://www.courtlistener.com/opinion/109584/united-states-v-donovan/) — pinpoint: 434 (Powell, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*434` and `*435`, i.e., on page 434). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "574418d550dac17c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Donovan"}, "payload": {"all": [{"cite": "429 U.S. 413", "page": "413", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "429"}, {"cite": "97 S. Ct. 658", "page": "658", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "50 L. Ed. 2d 652", "page": "652", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "50"}, {"cite": "1977 U.S. LEXIS 36", "page": "36", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "429 U.S. 413", "official": {"cite": "429 U.S. 413", "page": "413", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "429"}, "official_selection_present": true, "record_id": "United States v. Donovan"}}
{"assertion_id": "141a9e499e62f5c4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Donovan"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Donovan", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Donovan

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Donovan",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Donovan",
    "case_name_short": "Donovan",
    "case_name_full": "UNITED STATES v. DONOVAN Et Al.",
    "input_case_name": "United States v. Donovan",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-18",
    "year": 1977,
    "docket": "75-212",
    "cluster_id": 109584,
    "lead_opinion_id": 9426645,
    "sibling_ids": [],
    "absolute_url": "/opinion/109584/united-states-v-donovan/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 413",
      "volume": "429",
      "reporter": "U.S.",
      "page": "413",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 658",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 652",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 36",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 413",
        "volume": "429",
        "reporter": "U.S.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 658",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "658",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 652",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 36",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 413",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 413",
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
    "date_created": "2026-07-07T13:27:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-donovan--109584",
      "to_record_id": "United States v. Donovan",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Donovan

```
<opinion type="majority">
<author id="b566-5">Me. Justice Powell</author>
<p id="AV">delivered the opinion of the Court.</p>
<p id="b566-6">This case presents issues concerning the construction of Title III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>. Specifically, we must decide whether <span class="citation no-link">18 U. S. C. §2518</span> (l)(b)(iv), which requires the Government to include in its wiretap applications “the identity of the person, if known, committing the offense and whose communications are to be intercepted,” is satisfied when the Government identifies only the “principal targets” of the intercept. Second, we must decide whether the Government has a statutory responsibility to inform the issuing judge of the identities of persons whose conversations were overheard in the course of the interception, thus enabling him to decide whether they should be served with notice of the interception pursuant to <span class="citation no-link">18 U. S. C. §2518</span>(8)(d). And finally, we must determine whether failure to comply fully with these statutory provisions requires suppression of evidence under <span class="citation no-link">18 U. S. C. §2518</span> (10)(a).</p>
<p id="b566-7">I</p>
<p id="b566-8">On November 28, 1972, a special agent of the Federal Bureau of Investigation applied to the United States District Court for the Northern District of Ohio for an order authorizing a wiretap interception in accordance with Title III.<footnotemark>1</footnotemark> The application requested authorization to intercept <page-number citation-index="1" label="417">*417</page-number>gambling-related communications over two telephones at one address in North Olmstead, Ohio, and two other telephones at a home in Canton, Ohio. The accompanying affidavit recited that the telephones were being used by Albert Kotoch, Joseph Spaganlo, and George Florea' to conduct an illegal gambling business, and that in conducting that business they <page-number citation-index="1" label="418">*418</page-number>would place calls to and receive calls from various persons, three of whom were also named in the wiretap application.<footnotemark>2</footnotemark> The affiant also stated that the Government’s informants would refuse to testify against the persons named ha the application, that telephone records alone would be insufficient to support a gambling conviction, and that normal investigative techniques were unlikely to be fruitful. Pursuant to the Government’s request, the District Court authorized for a period of 15 days the interception of gambling-related wire communications of Kotoch, Spaganlo, Florea, three named individuals other than the respondents, and “others, as yet unknown,” to and from the four listed telephones.<footnotemark>3</footnotemark></p>
<p id="b569-4"><page-number citation-index="1" label="419">*419</page-number>During the course of the wiretap, the Government learned that respondents Donovan, Robbins, and Buzzacco were discussing illegal gambling activities with the named subjects. On December 26, 1972, the Government applied for an extension of the initial intercept order.<footnotemark>4</footnotemark> This time it sought authorization to intercept gambling-related conversations of Kotoch, Spaganlo, Florea, two other named individuals, and “others as yet unknown,” but it did not identify respondents Donovan, Buzzacco, and Robbins in this second application.<footnotemark>5</footnotemark> <page-number citation-index="1" label="420">*420</page-number>The District Court again authorized interception of gambling-related conversations for a maximum of 15 days.</p>
<p id="b570-5">On February 21, 1973, the Government submitted to the District Court a proposed order giving notice of the interceptions to 37 persons, a group which the Government apparently thought included all individuals who could be identified as having discussed gambling over the monitored telephones.<footnotemark>6</footnotemark> The District Court signed the proposed order, and an inventory notice was served on the listed persons, including respondents Donovan, Buzzacco, and Robbins. On September 11, 1973, after the Government submitted the names of two additional persons whose identities allegedly had been omitted inadvertently from the initial list, the District Court entered an amended order giving notice to those individuals. As a result of what the Government labels “administrative oversight,” respondents Merlo and Lauer were not included in either list of names and were never served with inventory notice.<footnotemark>7</footnotemark></p>
<p id="b571-4"><page-number citation-index="1" label="421">*421</page-number>On November 1, 1973, an indictment was returned in the United States District Court for the Northern District of Ohio charging Kotoch, Spaganlo, the five respondents, and 10 other individuals with conspiracy to conduct and conducting a gambling business in violation of <span class="citation no-link">18 U. S. C. §§ 371</span> and 1955. The five respondents filed motions to suppress evidence derived from the wire interception. After an evidentiary hearing on the motions, the District Court suppressed as to respondents Donovan, Robbins, and Buzzacco all evidence derived from the December 26 intercept order on the ground that failure to identify them by name in the application and order of that date violated <span class="citation no-link">18 U. S. C. §§ 2518</span> (l)(b)(iv) and 2518 (4)(a). With respect to Merlo and Lauer, who were not known to the Government until after the December 26 application, the District Court suppressed all evidence derived from both intercept orders on the ground that they had not been served with inventory notice.</p>
<p id="b571-5">The Court of Appeals for the Sixth Circuit affirmed. <span class="citation" data-id="9461598"><a href="/opinion/326404/united-states-v-thomas-w-donovan/" aria-description="Citation for case: United States v. Thomas W. Donovan">513 F. 2d 337</a></span> (1975).<footnotemark>8</footnotemark> On the identification issue, the court held that the wiretap application must identify every person whose conversations relating to the subject criminal activity the Government has probable cause to believe it will intercept. Agreeing with the District Court that at the time of the December 26 application the Government had probable cause to believe that it would overhear Donovan, Robbins, and Buzzacco “committing the offense,” the Court of Appeals affirmed the suppression of evidence derived from <page-number citation-index="1" label="422">*422</page-number>the December 26 order. On the notice question, it held that the Government has an implied statutory duty to inform the issuing judge of the identities of the parties whose conversations were overheard so that he can determine whether discretionary inventory notice should be required.<footnotemark>9</footnotemark> Because the Government had failed to perform this duty with respect to Merlo and Lauer, the Court of Appeals affirmed the District Court’s order suppressing evidence derived from both intercept orders. The court found it unnecessary to determine whether the failure to identify respondents Donovan, Robbins, and Buzzacco in the December 26 application and to name respondents Merlo and Lauer in the proposed inventory notice orders was inadvertent or purposeful, since the mere fact of omission was sufficient to require suppression under <span class="citation no-link">18 U. S. C. §2518</span> (10)(a).<footnotemark>10</footnotemark></p>
<p id="b572-5">We granted certiorari to resolve these issues, which concern the construction of a major federal statute, <span class="citation multiple-matches"><a href="/c/U.%20S./424/907/">424 U. S. 907</a></span>, and now reverse.</p>
<p id="b572-6">II</p>
<p id="b572-7">The United States contends that § 2518 (1) (b) (iv) requires that a wiretap application identify only the principal target of the interception, and that § 2518 (8) (d) does not require the Government to provide the issuing judge with a list of all identifiable persons who were overheard in the <page-number citation-index="1" label="423">*423</page-number>course of an authorized interception. We think neither contention is sound.</p>
<p id="b573-5">A</p>
<p id="b573-6">We turn first to the identification requirements of § 2518 (l)(b)(iv). That provision requires a wiretap application to specify “the identity of the person, if known, committing the offense and whose communications are to be intercepted.” In construing that language, this Court already has ruled that the Government is not required to identify an individual in the application unless it has probable cause to believe (i) that the individual is engaged in the criminal activity under investigation and (ii) that the individual’s conversations will be intercepted over the target telephone. <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974). The question at issue here is whether the Government is required to name <em>all </em>such individuals.<footnotemark>11</footnotemark></p>
<p id="b574-4"><page-number citation-index="1" label="424">*424</page-number>The United States argues that the most reasonable interpretation of the plain language of the statute is that the application must identify only the principal target of the investigation, who “will almost always be the individual whose phone is to be monitored.” <footnotemark>12</footnotemark> Brief for United States 18. Under this interpretation, if the Government has reason to believe that an individual will use the target telephone to place or receive calls, and the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation, the individual qualifies as a principal target and must be named in the wiretap application. On the other hand, an individual who uses a different telephone to place calls to or receive calls from the target telephone is not a principal target even if the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation. In other words, whether one is a principal target of the investigation depends on whether one operates the target telephone to place or receive calls.<footnotemark>13</footnotemark></p>
<p id="b574-5">Whatever the merits of such a statutory scheme, we find little support for it in the language and structure of Title III or in the legislative history. The statutory language itself refers only to “the person, if known, committing the <page-number citation-index="1" label="425">*425</page-number>offense and whose communications are to be intercepted.” That description is as applicable to a suspect placing calls to the target telephone as it is to a suspect placing calls from that telephone. It is true, as the United States suggests, that when read in the context of the other subdivisions of §2518 (1) (b), an argument can be made that Congress focused in subdivision (iv) on the primary user of the target telephone. But it is also clear from other sections of the statute that Congress expected that wiretap applications would name more than one individual. For example, Title III requires that inventory notice be served upon “the <em>persons </em>named in the order or the application.” <span class="citation no-link">18 U. S. C. §2518</span> (8)(d) (emphasis added). And §2518 (1) (e) requires that an intercept application disclose all previous intercept applications “involving <em>any of the same persons . </em>. . specified in the application” (emphasis added). It may well be that Congress anticipated that a given application would cover more than one telephone or that several suspects would use one telephone, and that an application for those reasons alone would require identification of more than one individual. But nothing on the face of the statute suggests that Congress intended to remove from the identification requirement those suspects whose intercepted communications originated on a telephone other than that listed in the wiretap application.<footnotemark>14</footnotemark></p>
<p id="b576-4"><page-number citation-index="1" label="426">*426</page-number>Nor can we find support in the legislative history for the “principal target” interpretation. Title III originated as a combination of S. 675, the Federal Wire Interception Act, which was introduced by Senator McClellan several months prior to this Court’s decision in <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and S. 2050, the Electronic Surveillance Control Act of 1967, introduced by Senator Hruska a few days after the <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>decision. S. Rep. No. 1097, 90th Cong., 2d Sess., 66 (1968). Both bills required that wiretap applications include a full and complete statement of the facts and circumstances relied upon by the applicant and specification of the nature and location of the communication facilities involved. Although neither bill contained an express identification requirement such as that at issue-here, both bills required the application to include a “full and complete statement of the facts concerning all previous applications . . . <em>involving any person named in the application </em>as committing, having committed, or being about to commit an offense.” Hearings Before the Subcommittee on Criminal Laws and Procedures of the Senate Committee on the Judiciary on Controlling'Crime Through More Effective Law Enforcement, 90th Cong.'; 1st Sess., 77, §8 (a)(3), and 1006, §2518 (4)(a) (1967) (emphasis added). Thus, even at this early stage, it was recognized that an application could identify several individuals, and there is no indication that the identification would be limited to principal targets.</p>
<p id="b576-5">S. 917 combined the major provisions of S. 675 and S. 2050 and eventually was enacted. While it was pending before the Senate Judiciary Committee, this Court decided <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). S. 917 was then redrafted to conform to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>as well as <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span>, </em>and the identification provision was added at that time. The Senate Report states that the requirements set forth in the vari<page-number citation-index="1" label="427">*427</page-number>ous subdivisions of § 2518 (l)(b), including the identification requirement at issue here, were intended to “reflect . . . the constitutional command of particularization.” S. Rep. No. 1097, <em>supra, </em>at 101, citing <em>Berger </em>v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#58" aria-description="Citation for case: Berger v. New York"><em>New York, supra, </em>at 58-60</a></span>, and <em>Katz </em>v. <em>United States, supra, </em>at 354-356. The United States now contends that although it may be that Congress read <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>to require, as a constitutional matter, that the subject of the surveillance be named if known, Congress would hardly have read those cases as requiring the naming of all ^parties likely to be overheard.<footnotemark>15</footnotemark> Brief for United States 25-26. But to the extent that Congress thought it was meeting the constitutional commands of particularization established in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>Congress may have read those cases as mandating a broad identification requirement. The statute that we confronted in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>required identification of “the person or persons” whose communications were to be overheard. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S., at 59</a></span>. And we expressly noted that that provision “[did] no more than identify the person whose constitutionally protected area is to be invaded . . . .” <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Ibid.</a></span> </em>Given the statute at issue in <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and our comment upon it, Congress may have concluded that the Constitution required the naming, in a wiretap application, of all suspects rather than just the primary user.<footnotemark>16</footnotemark></p>
<p id="b578-4"><page-number citation-index="1" label="428">*428</page-number>In any event, for our present purposes it is unnecessary to speculate as to exactly how Congress interpreted <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>and <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>with respect to the identification issue. It is sufficient to note that in response to those decisions Congress included an identification requirement which on its face draws no distinction based on the telephone one uses, and the United States points to no evidence in the legislative history that supports such a distinction. Indeed, the legislative materials apparently contain no use of the term “principal target” or any discussion of a different treatment based on the telephone from which a suspect speaks.<footnotemark>17</footnotemark> We therefore conclude that a wiretap application must name an individual if the Government has probable cause to believe that the individual is engaged in the criminal activity under investigation and expects to intercept the individual’s conversations over the target telephone.</p>
<p id="b578-5">B</p>
<p id="b578-6">The other statutory provision at issue in this case is <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d), which provides that the judge shall cause to be served on the persons named in the order or application an inventory, which must give notice of the entry of the order or application, state the disposition of <page-number citation-index="1" label="429">*429</page-number>the application, and indicate whether communications were intercepted.<footnotemark>18</footnotemark> Although the statute mandates inventory notice only for persons named in the application or the order, the statute also provides that the judge may order similar notice to other parties to intercepted communications if he concludes that such action is in the interest of justice.<footnotemark>19</footnotemark> Observing that this notice provision does not expressly require law enforcement authorities routinely to supply the judge with specific information upon which to exercise his discretion, the .United States contends that it would be inappropriate to read such a requirement into the statute since the judge has the option of asking the law enforcement authorities for whatever information he requires.</p>
<p id="b579-5">Our reading of the legislative history of the discretionary notice provision in light of the purposes of Title III leads us to reject the Government’s interpretation.. As reported from the Judiciary Committee, § 2518 (8) (d) contained only a provision mandating notice to the persons named in the application or the order; the discretionary notice provision was added by amendment on the floor of the Senate. In introducing that amendment, Senator Hart explained its purpose:</p>
<blockquote id="b579-6">“The amendment would give the judge who issued the order discretion to require notice to be served on other parties to intercepted communications, even though such <page-number citation-index="1" label="430">*430</page-number>parties are not specifically named in the court order. The Berger and Katz decisions established that notice of surveillance is a constitutional requirement of any surveillance statute. It may be that the required notice must be served on all parties to intercepted communications. Since legitimate interests of privacy may make such notice to all parties undesirable, the amendment leaves the final determination to the judge.” 114 Cong. Rec. 14485-14486 (1968).<footnotemark>20</footnotemark></blockquote>
<p id="b580-5">In deciding whether legitimate privacy interests justify withholding inventory notice from parties to intercepted conversations, a judge is likely to require information and assistance beyond that contained in the application papers and the recordings of intercepted conversations made available by law enforcement authorities. No purpose is served by holding that those authorities have no routine duty to supply the judge with relevant information. The Court of Appeals for the Ninth Circuit recently confronted this problem of dual responsibility, and we adopt the balanced construction that court placed on § 2518 (8) (d):</p>
<blockquote id="b580-6">“To discharge this obligation the judicial officer must have, at a minimum, knowledge of the particular categories into which fall all the individuals whose conver<page-number citation-index="1" label="431">*431</page-number>sations have been intercepted. Thus, while precise identification of each party to an intercepted communication is not required, a description of the general class, or classes, which they comprise is essential to enable the judge to determine whether additional information is necessary for a proper evaluation of the interests of the various parties. Furthermore, although the judicial officer has the duty to cause the filing of the inventory [notice], it is abundantly clear that the prosecution has greater access to and familiarity with the intercepted communications. Therefore we feel justified in imposing upon the latter the duty to classify all those whose conversations have been intercepted, and to transmit this information to the judge. Should the judge desire more information regarding these classes in order to exercise his [statutory] § 2518 (8) (d) discretion, . . . the government is [also] required to furnish such information as is available to it.” <em>United States </em>v. <em>Chun, </em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/#540" aria-description="Citation for case: United States v. David Chun">503 F. 2d 533, 540</a></span> (1974). (Footnote omitted.)</blockquote>
<p id="b581-5">We agree with the Ninth Circuit that this allocation of responsibility best serves the purposes of Title III.<footnotemark>21</footnotemark></p>
<p id="b581-6">Currently, the policy of the Justice Department is to provide the issuing judge with the name of every person who has been overheard as to whom there is any reasonable possibility of indictment. Brief for United States 39. Because it fails to assure that the necessary range of infor<page-number citation-index="1" label="432">*432</page-number>relation will be before the issuing judge, this policy does not meet the test set out in <em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/" aria-description="Citation for case: United States v. David Chun">Chun</a></span>. </em>Moreover, where, as here, the Government chooses to supply the issuing judge with a list of all identifiable persons rather than a description of the classes into which those persons fall, the list must be complete. Applying these principles, we find that the Government did not comply adequately with §2518 (8)(d), since the names of respondents Merlo and Lauer were not included on the purportedly complete list of identifiable persons submitted to the issuing judge.</p>
<p id="b582-5">Ill</p>
<p id="b582-6">We turn now to the question whether the District Court properly suppressed evidence derived from the wiretaps at issue solely because of the failure of the law enforcement authorities to comply fully with the provisions of §§2518 (1) (b)(iv) and 2518 (8) (d). Section 2515 expressly prohibits the use at trial, and at certain other proceedings, of the contents of any intercepted wire communication or any evidence derived therefrom “if the disclosure of that information would be in violation of this chapter.” The circumstances that trigger suppression under § 2515 are in turn enumerated in § 2518 (10) (a) :</p>
<blockquote id="b582-7">“(i) the communication was unlawfully intercepted;</blockquote>
<blockquote id="A4az">“(ii) the order of authorization or approval under which it was intercepted is insufficient on its face; or</blockquote>
<blockquote id="A-c">“(iii) the interception was not made in conformity with the order of authorization or approval.”</blockquote>
<p id="b582-8">There is no basis on the facts of this case to suggest that the authorization orders are facially insufficient, or that the interception was not conducted in conformity with the orders. Thus, only § 2518 (10) (a) (i) is relevant: Were the communications “unlawfully intercepted” given the violations of §§ 2518 (1) (b) (iv) and 2518 (8) (d) ? <footnotemark>22</footnotemark></p>
<p id="b583-4"><page-number citation-index="1" label="433">*433</page-number>Resolution of that question must begin with <em>United States </em>v. <em>Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span> (1974), and <em>United States </em>v. <em>Chavez, </em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">416 U. S. 562</a></span> (1974). Those cases hold that “[not] every failure to comply fully with any requirement provided in Title III would render the interception of wire or oral communications 'unlawful.5 55 <span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/#574" aria-description="Citation for case: United States v. Chavez"><em>Id., </em>at 574-575</a></span>. To the contrary, suppression is required only for a “failure to satisfy any of those statutory requirements that directly and substan<page-number citation-index="1" label="434">*434</page-number>tially implement the congressional intention to limit the use of intercept procedures to those, situations clearly calling for the employment of this extraordinary investigative device.” <em>United States </em>v. <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/#527" aria-description="Citation for case: United States v. Giordano"><em>Giordano, supra, </em>at 527</a></span>.</p>
<p id="b584-5"><em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">Giordano</a></span> </em>concerned the provision in Title III requiring that an application for an intercept order be approved by the Attorney General or an Assistant Attorney General specially designated by the Attorney General. Concluding that Congress intended to condition the use of wiretap procedures on the judgment of senior officials in the Department of Justice, the Court required suppression for failure to comply with the approval provision. <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>concerned the statutory requirement that the application for an intercept order specify the identity of the official authorizing the application. The problem in <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>was one of <em>misidentification; </em>although the application had in fact been authorized by the Attorney General, the application erroneously identified an Assistant Attorney General as the official authorizing the application. The Court concluded that mere misidentification of the official authorizing the application did not make the application unlawful within the meaning of § 2518 (10) (a) (i) since that identification requirement did not play a “substantive role” in the regulatory system. 416 U. S., at 578.</p>
<p id="b584-6">In the instant case, the Court of Appeals concluded that both the identification requirement of § 2518 (l)(b)(iv) and the notice requirement of § 2518 (8) (d) played a “central role” in the statutory framework, and for that reason affirmed the District Court's order suppressing relevant evidence. Although both statutory requirements are undoubtedly important, we do not think that the failure to comply fully with those provisions renders unlawful an intercept order that in all other respects satisfies the statutory requirements.</p>
<p id="b585-4"><page-number citation-index="1" label="435">*435</page-number>A</p>
<p id="b585-5">.As to § 2518 (l)(b)(iv), the issue is whether the identification in an intercept application of all those likely to be overheard in incriminating conversations plays a “substantive role” with respect to judicial authorization of intercept orders and consequently imposes a limitation on the use of intercept procedures. The statute provides that the issuing judge may approve an intercept application if he determines that normal investigative techniques have failed or are unlikely to succeed and there is probable cause to believe that: (i) an individual is engaged in criminal activity; (ii) particular communications concerning the offense will be .obtained through interception; and (iii) the target facilities are being used in connection with the specified criminal activity. §§ 2518 (3)(a-d). That determination is based on the “full and complete statement” of relevant facts supplied by law enforcement authorities. If, after evaluating the statutorily enumerated factors in light of the information contained in the application, the judge concludes that the wiretap order should issue, the failure to identify additional persons who are likely to be overheard engaging in incriminating conversations could hardly invalidate an otherwise lawful judicial authorization. The intercept order may issue only if the issuing judge determines that the statutory factors are present, and the failure to name additional targets in no way detracts from the sufficiency of those factors.</p>
<p id="b585-6">This case is unlike <em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">Giordano</a></span>, </em>where failure to satisfy the statutory requirement of prior approval by specified Justice Department officials bypassed a congressionally imposed limitation on the use of the intercept procedure. The Court there noted that it was reasonable to believe that requiring prior approval from senior officials in the Justice Department “would inevitably foreclose resort to wiretapping in various situations where investigative personnel would otherwise seek intercept authority from the court <page-number citation-index="1" label="436">*436</page-number>and the court would very likely authorize its use.” 416 U. S., at 528. Here, however, the statutorily imposed preconditions to judicial authorization were satisfied, and the issuing judge was simply unaware that additional persons might be overheard engaging in incriminating conversations. In no meaningful sense can it be said that the presence of that information as to additional targets would have precluded judicial authorization of the intercept <footnotemark>23</footnotemark> Rather, this case resembles <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span>, </em>where we held that a wiretap was not unlawful simply because the issuing judge was incorrectly informed as to which designated official had authorized the application. The <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span> </em>intercept was lawful because the Justice Department had performed its task of prior approval, and the instant intercept is lawful because the application provided sufficient information to enable the issuing judge to determine that the statutory preconditions were satisfied.<footnotemark>24</footnotemark></p>
<p id="b587-4"><page-number citation-index="1" label="437">*437</page-number>Finally, we note that nothing in the legislative history suggests that Congress intended this broad identification requirement to play “a central, or even functional, role in guarding against unwarranted use of wiretapping or electronic surveillance.” <em>United States </em>v. <em>Chavez, </em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/#578" aria-description="Citation for case: United States v. Chavez">416 U. S., at 578</a></span>. Neither S. 675 nor S. 2050, the predecessor bills of S. 917, contained an identification provision. See <em>supra, </em>at 426. The only explanation given in the Senate Report for the inclusion of the broad identification provision was that it was intended to reflect what Congress perceived to be the constitutional command of particularization. This explanation was offered with respect to all the information required by § 2518 (l)(b) to be set out in an intercept application. No additional guidance can be. gleaned from the floor debates, since they contain no substantive discussion of the identification provision.<footnotemark>25</footnotemark></p>
<p id="b588-4"><page-number citation-index="1" label="438">*438</page-number>B</p>
<p id="b588-5">We reach the same conclusion with respect to the Government's duty to inform the judge of all identifiable persons whose conversations were intercepted. As noted earlier, the version of Title III that emerged from the Senate Judiciary Committee provided only for mandatory notice to the “persons named in the order or the application.'' The Senate Report detailed the purpose of that provision:</p>
<blockquote id="b588-6">“[T]he intent of the provision is that the principle of postuse notice will be retained. This provision alone should insure the community that the techniques are reasonably employed. Through its operation all authorized interceptions must eventually become known at least to the subject. He can then seek appropriate civil redress, for example, under section 2520 ... if he feels that his privacy has been unlawfully invaded.” S. Rep. No. 1097, 90th Cong., 2d Sess., 105 (1968).</blockquote>
<p id="b588-7">The floor discussion concerning the amendment adding the provision for discretionary notice merely indicates an intent to provide notice to such additional persons as may be constitutionally required.</p>
<p id="b588-8">Nothing in the structure of the Act or this legislative history suggests that incriminating conversations are “unlawfully intercepted” whenever parties to those conversations do not receive discretionary inventory notice as a result of the Government’s failure to inform the District Court of their identities. At the time inventory notice was served on the other identifiable persons, the intercept had been completed and the conversations had been “seized” under a valid intercept order. The fact that discretionary notice reached <page-number citation-index="1" label="439">*439</page-number>39 rather than 41 identifiable persons does not in itself mean that the conversations were unlawfully intercepted.<footnotemark>26</footnotemark></p>
<p id="b589-5">The legislative history indicates that postintercept notice was designed instead to assure the community that the wiretap technique is reasonably employed. But even recognizing that Congress placed considerable emphasis on that aspect of the overall statutory scheme, we do not think that postintercept notice was intended to serve as an independent restraint on resort to the wiretap procedure.</p>
<p id="b589-6">IV</p>
<p id="b589-7">Although the Government was required to identify respondents Donovan, Robbins, and Buzzacco in the December 26 application for an extension of the initial intercept, failure to do so in the circumstances here presented did not warrant suppression under § 2518 (10) (a) (i). Nor was suppression justified with respect to respondents Merlo and Lauer simply because the Government inadvertently omitted their names from the comprehensive list of all identifiable persons whose conversations had been overheard. We hold that this is the correct result under the provisions of Title III, but we re<page-number citation-index="1" label="440">*440</page-number>emphasize the suggestion we made in <em>United States </em>v. <em><span class="citation" data-id="9425704"><a href="/opinion/109021/united-states-v-chavez/" aria-description="Citation for case: United States v. Chavez">Chavez</a></span>, </em>that “strict adherence by the Government to the provisions of Title III would nonetheless be more in keeping with the responsibilities Congress has imposed upon it when authority to engage in wiretapping or electronic surveillance is sought.” 416 U. S., at 580.</p>
<p id="b590-5">The judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b590-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b566-9"> The wiretap application procedure is set forth at <span class="citation no-link">18 U. S. C. § 2518</span> (1), which provides:</p>
<p id="b566-10">“(1) Each application for an order authorizing or approving the interception of a wire or oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction and shall state <page-number citation-index="1" label="417">*417</page-number>the applicant’s authority to make such application. Each application shall include the following information:</p>
<p id="AWp">“(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</p>
<p id="AJ0_">“ (b) a full and complete statement of the facts and circumstances relied upon by the applicant, to justify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about to be committed, (ii) a particular description of the nature and location of the facilities from which or the place where the communication is to be intercepted, (iii) a particular description of the type of communications sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications are to be intercepted;</p>
<p id="Au9">“(c) a full and complete statement as to whether or not other investigative procedures have been tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be-too dangerous;</p>
<p id="A7Y">“(d) a statement of the period of time for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause to believe that additional communications of the same type will occur thereafter;</p>
<p id="AJx">“(e) a full and complete statement of the facts concerning all previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of the same persons, facilities or places specified in the application, and the action taken by the judge on each such application; and</p>
<p id="A3K">“(f) where the application is for the extension of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results.”</p>
<p id="ABI">The issuing judge is free to require the applicant to furnish additional information. <span class="citation no-link">18 U. S. C. § 2518</span> (2).</p>
</footnote>
<footnote label="2">
<p id="b568-5"> The affidavit set forth extensive information indicating that the named individuals were conducting a gambling operation. This information was derived from physical surveillance by agents of the FBI, an examination of telephone company toll records, and the personal observations of six informants, whose past reliability also was detailed in the affidavit.</p>
</footnote>
<footnote label="3">
<p id="b568-6"> The District Court’s order was issued pursuant to <span class="citation no-link">18 U. S. C. §§ 2518</span> (3), (4), which provide in pertinent part:</p>
<p id="b568-7">“(3) Upon such application the judge may enter an ex parte order, as requested or as modified, authorizing or approving interception of wire or oral communications within the territorial jurisdiction of the court in which the judge is sitting, if the judge determines on the basis of the facts submitted by the applicant that—</p>
<p id="b568-8">“(a) there is probable cause for belief that an individual is committing, has committed, or is about to commit a particular offense enumerated in section 2516 of this chapter;</p>
<p id="b568-9">"(b) there is probable cause for belief that particular communications concerning that offense will be obtained through such interception;</p>
<p id="b568-10">"(c) normal investigative procedures have been tried and have failed or reasonably appear to be unlikely to succeed if tried or to be too dangerous;</p>
<p id="b568-11">“(d) there is probable cause for belief that the facilities from which, or the place where, the wire or oral communications are to be intercepted are being used, or are about to be used, in connection with the commission of such offense, or are leased to, listed in the name of, or commonly used by such person.</p>
<p id="b569-5"><page-number citation-index="1" label="419">*419</page-number>“(4) Each order authorizing or approving the interception of any wire or oral communication shall specify—</p>
<p id="Apq">“(a) the identity of the person, if known, whose communications are to be intercepted;</p>
<p id="A1k">“(b) the nature and location of the communications facilities as to which, or the place where, authority to intercept is granted;</p>
<p id="AWM">“(c) a particular description of the type of communication sought to be intercepted, and a statement of the particular offense to which it relates;</p>
<p id="AH2">“(d) the identity of the agency authorized to intercept the communications, and of the person authorizing the application; and</p>
<p id="Azs">“(e) the period of time during which such interception is authorized, including a statement as to whether or not the interception shall automatically terminate when the described communication has been first obtained.”</p>
</footnote>
<footnote label="4">
<p id="b569-10"> In addition to the December 26 application requesting an extension of the initial intercept order, the Government also filed on that date a separate application seeking authorization to monitor a third telephone discovered at the same North Olmstead address. Both applications were accompanied by another affidavit setting forth the results of the initial monitoring, the manner in which the third telephone was discovered, the facts, indicating that the newly discovered telephone was being used, to conduct a gambling business, and reasons why continued interception was necessary. A copy of the affidavit filed on November 28 was also attached to the December 26 applications. For the sake of clarity, the two applications filed on December 26 will be treated as a single application.</p>
</footnote>
<footnote label="5">
<p id="b569-11"> The United States conceded in the Court of Appeals that respondents Donovan and Robbins were “known” within the meaning of the statute at the time of the December 26 application, but challenged as <page-number citation-index="1" label="420">*420</page-number>clearly erroneous the District Court’s finding that respondent Buzzacco was “known” at that time. The Court of Appeals upheld the District Court’s finding, and the United States has not sought review of that disposition. Thus, for our purposes, all three respondents were “known” on December 26.</p>
</footnote>
<footnote label="6">
<p id="b570-11"> An inventory notice <em>must </em>be served within a designated period of time upon “the persons named in the order or the application.” <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). The inventory must give notice of the entry of the intercept order or application, state the disposition of the application, and indicate whether communications were or were not intercepted. <em><span class="citation no-link">Ibid.</span> </em>Upon the filing of a motion, the judge has discretion to make available the intercepted communications, the applications, and the orders. <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b570-12">Title III also authorizes the District Court to cause an inventory notice to be served on “other parties to intercepted communications” if the judge determines that such notice is in the interest of justice. <em><span class="citation no-link">Ibid.</span> </em>Those other parties may also be given access to the intercepted communications, the applications, and the orders. <em><span class="citation no-link">Ibid.</span></em></p>
</footnote>
<footnote label="7">
<p id="b570-13"> Although respondents Merlo and Lauer were not served with inventory notice pursuant to §2518 (8) (d), the intercept orders, applications, <page-number citation-index="1" label="421">*421</page-number>and related papers were made available to all the defendants, including Merlo and Lauer, on November 26, 1973. Thus, the introduction into evidence at trial of the contents of the intercepted conversations and evidence derived therefrom would not be prohibited by <span class="citation no-link">18 U. S. C. §2518</span> (9).</p>
</footnote>
<footnote label="8">
<p id="b571-11"> The Government filed its appeal from the District Court’s order suppressing evidence under <span class="citation no-link">18 U. S. C. § 3731</span>, and there has been no trial on the charges with respect to the respondents.</p>
</footnote>
<footnote label="9">
<p id="b572-8"> See n. 6, <em>supra.</em></p>
</footnote>
<footnote label="10">
<p id="b572-9"><em> </em>Title <span class="citation no-link">18 U. S. C. § 2518</span> (10) (a) provides in pertinent part:</p>
<p id="b572-10">“(10) (a) Any aggrieved person in any trial, hearing, or proceeding in or before any court, department, officer, agency, regulatory body, or other authority of the United States, a State, or a political subdivision thereof, may move to suppress the. contents of any intercepted wire or oral communication, or evidence derived therefrom, on the grounds that—</p>
<p id="Ahz">“(i) the communication was unlawfully intercepted;</p>
<p id="b572-11">“(ii) the order of authorization or approval under which it was intercepted is insufficient on its face; or</p>
<p id="b572-12">“(iii) the interception was not made in conformity with the order of authorization or approval.”</p>
</footnote>
<footnote label="11">
<p id="b573-7"> Every Court of Appeals that has considered the issue has concluded that an individual whose conversations probably will be intercepted by a wiretap must be identified in the wiretap application if the law enforcement authorities have probable cause to believe the individual is committing the offense for which the wiretap is sought. <em>United States </em>v. <em>Chiarizio, </em><span class="citation" data-id="331054"><a href="/opinion/331054/united-states-v-michael-chiarizio/#292" aria-description="Citation for case: United States v. Michael Chiarizio">525 F. 2d 289, 292</a></span> (CA2 1975); <em>United States </em>v. <em>Bernstein, </em><span class="citation" data-id="324740"><a href="/opinion/324740/united-states-v-calman-bernstein/" aria-description="Citation for case: United States v. Calman Bernstein">509 F. 2d 996</a></span> (CA4 1975), cert. pending, No. 74-1486; <em>United States </em>v. <em>Doolittle, </em><span class="citation multiple-matches"><a href="/c/F.%202d/507/1368/">507 F. 2d 1368</a></span> (CA5), aff’d en banc, <span class="citation multiple-matches"><a href="/c/F.%202d/518/500/">518 F. 2d 500</a></span> (1975), cert. pending, Nos. 75-500, 75-509, 75-513; <em>United States </em>v. <em>Civella, </em><span class="citation" data-id="8898935"><a href="/opinion/8911188/united-states-v-civella/" aria-description="Citation for case: United States v. Civella">533 F. 2d 1395</a></span> (CA8 1976), cert. pending, Nos. 75-1813, 76-169; <em>United States </em>v. <em>Russo, </em><span class="citation" data-id="331942"><a href="/opinion/331942/united-states-v-anthony-r-russo/#1056" aria-description="Citation for case: United States v. Anthony R. Russo">527 F. 2d 1051, 1056</a></span> (CA10 1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/906/">426 U. S. 906</a></span> (1976). See also <em>United States </em>v. <em>Moore, </em>168 U. S. App. D. C. 227, 235-236, <span class="citation" data-id="326419"><a href="/opinion/326419/united-states-v-aaron-r-moore-jr-united-states-of-america-v-robert/#493" aria-description="Citation for case: United States v. Aaron R. Moore, Jr., United States of...">513 F. 2d 485, 493-494</a></span> (1975) (interpreting D. C. Code § 23-547 (a) (2) (D), which is almost identical to the provision at issue here).</p>
<p id="b573-8">A number of these courts have concluded, and respondents Donovan, Robbins, and Buzzacco argue, that our decision in <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974), resolved this identification issue. See <em>United States </em>v. <em><span class="citation" data-id="331054"><a href="/opinion/331054/united-states-v-michael-chiarizio/" aria-description="Citation for case: United States v. Michael Chiarizio">Chiarizio, supra;</a></span> United States </em>v. <em><span class="citation" data-id="326419"><a href="/opinion/326419/united-states-v-aaron-r-moore-jr-united-states-of-america-v-robert/" aria-description="Citation for case: United States v. Aaron R. Moore, Jr., United States of...">Moore, supra.</a></span> </em>Although there is language in <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span> </em>suggesting that wiretap applications must identify all such individuals, the identification question presented here was not before us in <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span>. </em>The question in that case was whether a wiretap application had to identify a known user of the target telephone whose com<page-number citation-index="1" label="424">*424</page-number>plicity in the criminal activity under investigation was not known at the time of the application. <em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">Kahn</a></span> </em>is a relevant, though not controlling, precedent.</p>
</footnote>
<footnote label="12">
<p id="b574-7"> The United States does not suggest that regardless of the factual circumstances a wiretap application must identify only a single individual. To the contrary, it concedes that if two or more persons are using the target telephone “equally” to commit the offense, and thus are “equally” targets of the investigation, “all must be named.” Brief for United States 18 n. 13.</p>
</footnote>
<footnote label="13">
<p id="b574-8"> Counsel for the United States explained this position succinctly at oral argument: “The critical distinction ... is [one] between the users of the telephone that is being monitored on the one hand, and all other persons throughout the world who may converse from unmonitored phones on the other hand.” Tr. of Oral Arg. 13.</p>
</footnote>
<footnote label="14">
<p id="b575-5"> Indeed, the contrary conclusion is suggested by the fact that identification of an individual in an application for an intercept order triggers other statutory provisions. First, § 2518 (1) (e) requires an intercept application to disclose all previous applications “involving any of the same persons . . . specified in the application.” To the extent that Congress thought it necessary to provide the issuing judge with such information, there is no indication of congressional intent to require provision of such information only if a suspect operated from one end of a telephone line. Second, § 2518 (8) (d) mandates that an inventory notice be served upon “the persons named in the order or the application.” As with §2518 (1) (e), the congressional purpose would <page-number citation-index="1" label="426">*426</page-number>not be <em>served by </em>limiting that notice on the basis of the telephone from which one speaks.</p>
</footnote>
<footnote label="15">
<p id="b577-5"> At the time of the enactment of Title III, Congress did not have before it the view we expressed on this issue in <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S., at 155</a></span> n. 15. The Fourth Amendment requires specification of “the place to be searched, and the persons or things to be seized.” In the wiretap context, those requirements are satisfied by identification of the telephone line to be tapped and the particular conversations to be seized. It is not a constitutional requirement that all those likely to be overheard engaging in incriminating conversations be named. Specification of this sort “identifies] the person whose constitutionally protected area is to be invaded rather than ‘particularly describing’ the communications, conversations, or discussions to be seized.” <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#59" aria-description="Citation for case: Berger v. New York">388 U. S., at 59</a></span>.</p>
</footnote>
<footnote label="16">
<p id="b577-6"> That Congress may have so understood the constitutional require<page-number citation-index="1" label="428">*428</page-number>ment is also suggested by <em>the </em>portion of <em>the </em>Senate Report dealing with that provision of S. 917 that required the intercept <em>order </em>to “specify the identity, if known, of the individual whose communications are to be intercepted.” The Senate Report merely cites <em>West </em>v. <em>Cabell, </em><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">153 U. S. 78</a></span> (1894), which concerns the need for proper identification of the subject of an arrest warrant. S. Rep. No. 1097, 90th Cong., 2d Sess., 102 (1968). To the extent that Congress may have considered <em><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">West</a></span> </em>to apply to wiretap orders, we have no reason to believe that Congress considered its applicability to extend only to those suspects using the target telephone.</p>
</footnote>
<footnote label="17">
<p id="b578-8"> At least one Senator read the identification requirement in S. 917 to parallel the identification requirement contained in the statute at issue in <em>Berger </em>v. <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">New York</a></span>: </em>“Specificity is required as to the person or persons whose communications will be intercepted.” 114 Cong. Rec. 14763 (1968) (remarles of Sen. Percy).</p>
</footnote>
<footnote label="18">
<p id="b579-7"> The inventory notice must be served within a reasonable time but not later than 90 days after the date the application for an intercept order was filed. On an <em>ex parte </em>showing of good cause, service of the inventory may be postponed.</p>
</footnote>
<footnote label="19">
<p id="b579-8"> In addition to these provisions for mandatory and discretionary inventory notice, the Government is required to supply the issuing judge with recordings of the intercepted conversations, which are to be sealed according to his directions. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (a). These notice and return provisions satisfy constitutional requirements. See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#355" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 355-356</a></span>, and n. 16 (1967); <em>Berger </em>v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#60" aria-description="Citation for case: Berger v. New York"><em>New York, supra, </em>at 60</a></span>.</p>
</footnote>
<footnote label="20">
<p id="b580-7"> It is worth noting that shortly before Senator Hart proposed this amendment to S. 917, Senator Long had read to the Senate portions of a report prepared by the Association of the Bar of the City of New York on federal wiretap legislation. That report commented that parties to intercepted conversations other than those named in the application or order probably should be served with inventory notice, but it also recognized that under some circumstances the provision of such notice could be harmful and gave the following example:</p>
<p id="b580-8"><em>“A, </em>a businessman, talks with his customers, and the latter are served with papers showing that A is being bugged .... [T]he damage to confidence in A and to A's reputation in general may damage A unjustly. In this case it would seem that the customers should not be served with the inventory..” 114 Cong. Rec. 14476 (1968).</p>
</footnote>
<footnote label="21">
<p id="b581-7"> At oral argument, counsel for the United States recognized the merit of the approach specified in <em>United States </em>v. <em><span class="citation" data-id="321775"><a href="/opinion/321775/united-states-v-david-chun/" aria-description="Citation for case: United States v. David Chun">Chun</a></span>:</em></p>
<p id="b581-8">“Perhaps the approach of the Court of Appeals for the Ninth Circuit, which suggested that rather than submitting specific names we should submit categories of persons who had been overheard, is a better policy, would be more helpful to the district court in exercising its discretion, and we would have no objection to following any reasonable policy that the district courts determine would be useful to them in this area.” Tr. of Oral Arg. 6-7.</p>
</footnote>
<footnote label="22">
<p id="b582-9"> The availability of the suppression remedy for these statutory, <page-number citation-index="1" label="433">*433</page-number>as opposed to constitutional, violations, see nn. 15 and 19, <em>supra, </em>turns on the provisions of Title III rather than the judicially fashioned exclusionary rule aimed at deterring violations of Fourth Amendment rights. <em>United States v. Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/#524" aria-description="Citation for case: United States v. Giordano">416 U. S. 505, 524</a></span> (1974).</p>
<p id="b583-6">The concurring opinion of The Cheep Justice contends that respondents Donovan, Robbins, and Buzzacco lack standing even to seek suppression. <em>Post, </em>at 440-441. This contention rests on the ground that Congress rejected an amendment proposed by Senators Long and Hart that would have added a fourth ground justifying suppression — namely, that the person against whom the Government sought to introduce the evidence was not named in the court order. Since these three respondents would have been entitled to suppression under the rejected amendment, the concurring opinion concludes they .cannot seek suppr&amp;sion here.</p>
<p id="b583-7">This view fails to recognize that § 2518 (10) (a) establishing the suppression remedy provides <em>alternative </em>grounds on which one can seek suppression of evidence derived from a wiretap. Thus, the mere fact that Congress chose not to add a fourth alternative could not mean that it intended to prevent persons who would have been covered by that alternative from seeking suppression on one of the other grounds. As the Justice Department commented, in the same statement cited in the concurring opinion: “The [Long and Hart] amendment is designed to limit the scope of electronic surveillance, but it accomplishes this purpose in an artificial manner. <em>So long as a court order is validly obtained, </em>evidence obtained under the order should be admissible against any person not merely against the person named in the order.” 114 Cong. Rec. 14718 (1968) (emphasis added). Here, respondents Donovan, Robbins, and Buzzacco challenge the validity of the court order, and nothing in either Congress’ rejection of the proposed amendment or the Justice Department’s comment thereon suggests that § 2518 (10) (a) (i) is unavailable to persons who might have had a remedy under a provision not enacted by Congress.</p>
</footnote>
<footnote label="23">
<p id="b586-5"> There is no suggestion in this case that the Government agents knowingly failed to identify respondents Donovan, Robbins, and Buzzacco for the purpose of keeping relevant information from the District Court that might have prompted the court to conclude that probable cause was lacking. If such a showing had been made, we would have a different case. Nor is there any suggestion that as a result of the failure to name these three respondents they were denied the mandatory inventory notice supplied to persons named in the application. <span class="citation no-link">18 U. S. C. § 2518</span> (8) (d). Respondents Donovan, Robbins, and Buzzacco were <em>among the </em>37 persons served with the initial inventory.</p>
</footnote>
<footnote label="24">
<p id="b586-6"><em> </em>No one suggests that the failure to identify in a wiretap application individuals who are “unknown” within the meaning of the statute, see <em>United States </em>v. <em>Kahn, </em><span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span> (1974), requires suppression of intercepted conversations to which those individuals were parties. Though recognizing that the failure to identify such an “unknown” individual does not make unlawful an otherwise valid intercept order, respondents Donovan, Robbins, and Buzzacco suggest that the opposite is true with respect to the failure to identify in a wiretap application individuals who are “known” within the meaning of the statute. Counsel for these respondents suggested at oral argument that this difference in result is justified by analogy to warrantless searches or arrests. Tr. of Oral Arg. 40. Although law enforcement officials can often take action without a warrant when they have <page-number citation-index="1" label="437">*437</page-number>been unable to foresee the circumstances that eventually confronted them, they still must obtain a search or arrest warrant when their prior knowledge is sufficient to establish probable cause, and it is suggested that the same principle applies here. The major flaw' in that reasoning is that this case does not concern warrantless action. Here, the omission on the part of law enforcement authorities was not a failure to seek prior judicial authorization, but a failure to identify every individual who could be expected to be overheard engaging in incriminating conversations. That the complete absence of prior judicial authorization would make an intercept unlawful has no bearing on the lawfulness of an intercept order that fails to identify every target.</p>
</footnote>
<footnote label="25">
<p id="b587-6"> Even if we assume that Congress thought that a broad identification requirement was constitutionally mandated, it does not follow that Congress imposed <em>statutory </em>suppression under §§ 2515 and 2518 (10) (a) (i) as a sanction for noncompliance. In limiting use of the intercept procedure to “the most precise and discriminate circumstances,” S. Rep. No. 1097, 90th Cong., 2d Sess., 102 (1968), Congress required law enforcement authorities to convince a district court that probable cause existed to believe that a specific person was committing a specific offense using a specific telephone. This requirement was satisfied here when the application set forth sufficient information to indicate that the primary targets were conducting a gambling business over four particular telephones. Nothing <page-number citation-index="1" label="438">*438</page-number>in the legislative history indicates that Congress intended to declare an otherwise constitutional intercept order “unlawful” under § 2518 (10) (a) (i) — resulting in suppression under § 2515 — for failure to name additional targets.</p>
</footnote>
<footnote label="26">
<p id="b589-8"> Counsel for respondents Merlo and Lauer conceded at oral argument that the failure to name those respondents in the proposed inventory order was not intentional, Tr. of Oral Arg. 32, and we axe therefore not called upon to decide whether suppression would be an available remedy if the Government knowingly sought to prevent the District Court from serving inventory notice on particular parties. Nor does this case present an opportunity to comment upon the suggestion, recognized by the United States, Brief 49 n. 40, that suppression might be required if the agents knew before the interception that no inventory would be served.</p>
<p id="b589-9">Moreover, respondents Merlo and Lauer were not prejudiced by their failure to receive postintercept notice under either of the District Court's inventory orders. As noted earlier, the Government made available to all defendants the intercept orders, applications, and related papers. See n. 7, <em>supra. </em>And in response to pretrial discovery motions, the Government produced transcripts of the intercepted conversations.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Drayton.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Drayton"
type: case
citation: "536 U.S. 194 (2002)"
parallel_cite: "122 S. Ct. 2105; 153 L. Ed. 2d 242"
neutral_cite: 2002 U.S. LEXIS 4420
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Drayton
  varies_by_point: false
  scope_note: "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121153/united-states-v-drayton/"
  cluster_id: 121153
  opinion_id: 121153
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Key — Progeny / Refinement"
related: ["[[Florida v. Bostick]]", "[[Schneckloth v. Bustamonte]]", "[[Ohio v. Robinette]]", "[[California v. Hodari D.]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "seizure"]
holding: "A bus sweep with consent-to-search requests is not a seizure, and consent can be voluntary even though officers do not advise passengers…"
lake:
  record_id: United States v. Drayton
  status: verified
  projected_at: 2026-07-09
---

# United States v. Drayton

*536 U.S. 194 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Three officers boarded a stopped interstate bus as part of a drug interdiction sweep. One stationed himself at the front, another at the rear, and a third worked his way down the aisle, leaning toward passengers and asking about their travel and luggage. He asked Drayton and Brown for permission to search their persons; both consented, and officers found drugs taped to their legs. The officer did not tell passengers they were free to refuse to cooperate.

## Issue
Whether the bus passengers were seized when officers questioned them and requested consent to search, and whether their consent was involuntary because officers did not advise them of their right to refuse.

## Rule
Bus-sweep questioning is not a [[Common Legal Terms#per-se|per se]] seizure; the test is objective: "Applying the *Bostick* framework to the facts of this particular case, we conclude that the police did not seize respondents when they boarded the bus and began questioning passengers." — 536 U.S. at 203. ^pin-203

The inquiry is "whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter." — [*Id.* at 202](https://www.courtlistener.com/opinion/121153/united-states-v-drayton/#:~:text=whether%20a%20reasonable%20person%20would) (quoting *Florida v. Bostick*). ^pin-202

And officers need not warn of the right to refuse: "The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search." — [*Id.* at 206](https://www.courtlistener.com/opinion/121153/united-states-v-drayton/#:~:text=The%20Court%20has%20rejected%20in). ^pin-206

## Application
On these facts the officers gave passengers no reason to believe they were required to cooperate: they did not brandish weapons, block the aisle, or use a commanding tone, and Drayton was free to refuse. The encounter was therefore not a seizure. And although the officer never told Drayton he could refuse the search, he did request permission to search rather than demand it, and under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] Drayton's consent was voluntary. The failure to advise of the right to refuse was one factor, not a disqualifier, so the searches were reasonable.

## Conclusion
The bus passengers were not seized, and their consent to search was voluntary despite the absence of any advice of the right to refuse; the suppression below was reversed. Officers may work a bus and request consent without effecting a seizure, and need not warn passengers that they may decline.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Drayton* applies the free-to-decline test of [[Florida v. Bostick]] and the totality-of-circumstances voluntariness rule of [[Schneckloth v. Bustamonte]] and [[Ohio v. Robinette]] (no warning of the right to refuse required); on when a show of authority becomes a seizure, compare [[California v. Hodari D.]].

## Appears on
- [[Knock and Talk]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Drayton*, 536 U.S. 194 (2002) — https://www.courtlistener.com/opinion/121153/united-states-v-drayton/ — pinpoints: 202, 203, 206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "60e1c89d1348359e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Drayton"}, "payload": {"all": [{"cite": "536 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "536"}, {"cite": "122 S. Ct. 2105", "page": "2105", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "153 L. Ed. 2d 242", "page": "242", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "153"}, {"cite": "2002 U.S. LEXIS 4420", "page": "4420", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}], "display": "536 U.S. 194", "official": {"cite": "536 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "536"}, "official_selection_present": true, "record_id": "United States v. Drayton"}}
{"assertion_id": "32093e8e1150bd4c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-206", "record_id": "United States v. Drayton"}, "payload": {"fragment": "#:~:text=The%20Court%20has%20rejected%20in", "page": null, "pin_id": "pin-206", "pinpoint_status": "star-verified", "quote": "The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search.", "quote_fidelity": "matched", "record_id": "United States v. Drayton", "star_marker": "206"}}
{"assertion_id": "6d2d1645ce340422", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-202", "record_id": "United States v. Drayton"}, "payload": {"fragment": "#:~:text=whether%20a%20reasonable%20person%20would", "page": null, "pin_id": "pin-202", "pinpoint_status": "star-verified", "quote": "whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter.", "quote_fidelity": "matched", "record_id": "United States v. Drayton", "star_marker": "202"}}
{"assertion_id": "9f8028332dc55bb6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-203", "record_id": "United States v. Drayton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-203", "pinpoint_status": "slip-only", "quote": "--- # United States v. Drayton *536 U.S. 194 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three officers boarded a stopped interstate bus as part of a drug interdiction sweep. One stationed himself at the front, another at the rear, and a third worked his way down the aisle, leaning toward passengers and asking about their travel and luggage. He asked Drayton and Brown for permission to search their persons; both consented, and officers found drugs taped to their legs. The officer did not tell passengers they were free to refuse to cooperate. ## Issue Whether the bus passengers were seized when officers questioned them and requested consent to search, and whether their consent was involuntary because officers did not advise them of their right to refuse. ## Rule Bus-sweep questioning is not a per se seizure; the test is objective:", "quote_fidelity": "mismatch", "record_id": "United States v. Drayton", "star_marker": null}}
{"assertion_id": "b9e5c739e28b1504", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Drayton"}, "payload": {"as_of_content": "2002-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Drayton", "scope_note": "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse.", "varies_by_point": false}}
```

### lake record — United States v. Drayton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Drayton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Drayton",
    "case_name_short": "Drayton",
    "case_name_full": "UNITED STATES v. DRAYTON Et Al.",
    "input_case_name": "United States v. Drayton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-17",
    "year": 2002,
    "docket": null,
    "cluster_id": 121153,
    "lead_opinion_id": 121153,
    "sibling_ids": [
      121153,
      9434276,
      9434277
    ],
    "absolute_url": "/opinion/121153/united-states-v-drayton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 194",
      "volume": "536",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2105",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2105",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 242",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4420",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4420",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 194",
        "volume": "536",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2105",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2105",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 242",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4420",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4420",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-203",
      "page": null,
      "quote": "--- # United States v. Drayton *536 U.S. 194 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three officers boarded a stopped interstate bus as part of a drug interdiction sweep. One stationed himself at the front, another at the rear, and a third worked his way down the aisle, leaning toward passengers and asking about their travel and luggage. He asked Drayton and Brown for permission to search their persons; both consented, and officers found drugs taped to their legs. The officer did not tell passengers they were free to refuse to cooperate. ## Issue Whether the bus passengers were seized when officers questioned them and requested consent to search, and whether their consent was involuntary because officers did not advise them of their right to refuse. ## Rule Bus-sweep questioning is not a per se seizure; the test is objective:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-202",
      "page": null,
      "quote": "whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter.",
      "star_marker": "202",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13873,
      "fragment": "#:~:text=whether%20a%20reasonable%20person%20would",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-206",
      "page": null,
      "quote": "The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search.",
      "star_marker": "206",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28368,
      "fragment": "#:~:text=The%20Court%20has%20rejected%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Drayton",
    "varies_by_point": false,
    "scope_note": "Good law; bus-sweep questioning and consent requests are not a per se seizure, and officers need not advise of the right to refuse.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Gutierrez",
          "cluster_id": 6240355,
          "cite": [
            "245 Cal. Rptr. 3d 143",
            "33 Cal. App. Supp. 5th 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morris Wise",
          "cluster_id": 4448990,
          "cite": [
            "877 F.3d 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parker",
          "cluster_id": 4440893,
          "cite": [
            "807 S.E.2d 617",
            "256 N.C. App. 319"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Daniel White",
          "cluster_id": 4322612,
          "cite": [
            "887 N.W.2d 172",
            "2016 Iowa Sup. LEXIS 105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 3203547,
          "cite": [
            "823 F.3d 20",
            "2016 U.S. App. LEXIS 8834",
            "2016 WL 2821485"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moises Donjuan v. State",
          "cluster_id": 2980860,
          "cite": [
            "461 S.W.3d 611",
            "2015 Tex. App. LEXIS 1618",
            "2015 WL 732640"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camp",
          "cluster_id": 2774669,
          "cite": [
            "2015 Ohio 329"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Branham v. Commonwealth",
          "cluster_id": 1057965,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zamudio",
          "cluster_id": 2634388,
          "cite": [
            "181 P.3d 105",
            "75 Cal. Rptr. 3d 289",
            "43 Cal. 4th 327",
            "2008 Cal. LEXIS 4431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl James v. Wilkes Barre City",
          "cluster_id": 812864,
          "cite": [
            "700 F.3d 675",
            "2012 U.S. App. LEXIS 24592",
            "2012 WL 5954632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tully",
          "cluster_id": 844166,
          "cite": [
            "54 Cal. 4th 952",
            "282 P.3d 173",
            "145 Cal. Rptr. 3d 146",
            "2012 WL 3064338",
            "2012 Cal. LEXIS 7247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gherna",
          "cluster_id": 2252587,
          "cite": [
            "784 N.E.2d 799",
            "203 Ill. 2d 165",
            "271 Ill. Dec. 245",
            "2003 Ill. LEXIS 2"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caraballo",
          "cluster_id": 78534,
          "cite": [
            "595 F.3d 1214",
            "2010 WL 297146"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 2623710,
          "cite": [
            "166 P.3d 1015",
            "284 Kan. 763",
            "2007 Kan. LEXIS 487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Monterroso",
          "cluster_id": 2507854,
          "cite": [
            "101 P.3d 956",
            "22 Cal. Rptr. 3d 1",
            "34 Cal. 4th 743",
            "2004 Daily Journal DAR 14707",
            "2004 Cal. Daily Op. Serv. 10899",
            "2004 Cal. LEXIS 11763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625130,
          "cite": [
            "208 A.3d 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennings v. Jones",
          "cluster_id": 8440132,
          "cite": [
            "499 F.3d 2",
            "2007 U.S. App. LEXIS 19583",
            "2007 WL 2339195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jordan",
          "cluster_id": 212479,
          "cite": [
            "635 F.3d 1181",
            "2011 U.S. App. LEXIS 5235",
            "2011 WL 891075"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trafton v. City of Woodbury",
          "cluster_id": 2150404,
          "cite": [
            "799 F. Supp. 2d 417",
            "2011 U.S. Dist. LEXIS 70682",
            "2011 WL 2610747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cox",
          "cluster_id": 1058221,
          "cite": [
            "171 S.W.3d 174",
            "2005 Tenn. LEXIS 683",
            "2005 WL 2051278"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2200827,
          "cite": [
            "789 N.E.2d 260",
            "204 Ill. 2d 220",
            "273 Ill. Dec. 360",
            "2003 Ill. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Romain",
          "cluster_id": 201394,
          "cite": [
            "393 F.3d 63",
            "2004 WL 2997954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Drayton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121153 OR 9434276 OR 9434277) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEyNDE2MDAwMDAwJnM9MzEyMjU1NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121153+OR+9434276+OR+9434277%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(121153 OR 9434276 OR 9434277)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTc3OTI3MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121153+OR+9434276+OR+9434277%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121153 OR 9434276 OR 9434277)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121153 OR 9434276 OR 9434277)",
    "indexed_citing_opinions": 594,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121153,
        "count": 502,
        "count_source": "search"
      },
      {
        "opinion_id": 9434276,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9434277,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1085,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-drayton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NDA5NzMmcz05NDI1NzQ5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121153+OR+9434276+OR+9434277%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121153,
        "cited_id": 72919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 73082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121153,
        "cited_id": 771014,
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
    "date_created": "2026-07-05T23:36:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:42:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:36:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Drayton

```
<div>
<center><b><span class="citation" data-id="9434276"><a href="/opinion/121153/united-states-v-drayton/" aria-description="Citation for case: United States v. Drayton">536 U.S. 194</a></span> (2002)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
DRAYTON et al.</h1></center>
<center>No. 01-631.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued April 16, 2002.</center>
<center>Decided June 17, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE ELEVENTH CIRCUIT
<p><span class="star-pagination">*196</span> <span class="star-pagination">*196</span> Kennedy, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Thomas, and Breyer, JJ., joined. Souter, J., filed a dissenting opinion, in which Stevens and Ginsburg, JJ., joined, <i>post,</i> p. 208.</p>
<p><i>Larry D. Thompson</i> argued the cause for the United States. On the briefs were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Deputy Solicitor General Dreeben, Jeffrey A. Lamken,</i> and <i>Kathleen A. Felton.</i> </p>
<p><i>Gwendolyn Spivey,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./535/903/">535 U. S. 903</a></span>, argued the cause for respondents. With her on the brief were <i>Randolph P. Murrell, Steven L. Seliger,</i> by appointment <span class="star-pagination">*197</span> of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./535/903/">535 U. S. 903</a></span>, <i>Jeffrey T. Green,</i> and <i>Jacqueline G. Cooper.</i><sup>[*]</sup></p>
<p>Justice Kennedy, delivered the opinion of the Court.</p>
<p>The Fourth Amendment permits police officers to approach bus passengers at random to ask questions and to request their consent to searches, provided a reasonable person would understand that he or she is free to refuse. <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991). This case requires us to determine whether officers must advise bus passengers during these encounters of their right not to cooperate.</p>
<p></p>
<h2>I</h2>
<p>On February 4, 1999, respondents Christopher Drayton and Clifton Brown, Jr., were traveling on a Greyhound bus en route from Ft. Lauderdale, Florida, to Detroit, Michigan. The bus made a scheduled stop in Tallahassee, Florida. The passengers were required to disembark so the bus could be refueled and cleaned. As the passengers reboarded, the driver checked their tickets and then left to complete paperwork inside the terminal. As he left, the driver allowed three members of the Tallahassee Police Department to board the bus as part of a routine drug and weapons interdiction effort. The officers were dressed in plain clothes and carried concealed weapons and visible badges.</p>
<p>Once on board Officer Hoover knelt on the driver's seat and faced the rear of the bus. He could observe the passengers <span class="star-pagination">*198</span> and ensure the safety of the two other officers without blocking the aisle or otherwise obstructing the bus exit. Officers Lang and Blackburn went to the rear of the bus. Blackburn remained stationed there, facing forward. Lang worked his way toward the front of the bus, speaking with individual passengers as he went. He asked the passengers about their travel plans and sought to match passengers with luggage in the overhead racks. To avoid blocking the aisle, Lang stood next to or just behind each passenger with whom he spoke.</p>
<p>According to Lang's testimony, passengers who declined to cooperate with him or who chose to exit the bus at any time would have been allowed to do so without argument. In Lang's experience, however, most people are willing to cooperate. Some passengers go so far as to commend the police for their efforts to ensure the safety of their travel. Lang could recall five to six instances in the previous year in which passengers had declined to have their luggage searched. It also was common for passengers to leave the bus for a cigarette or a snack while the officers were on board. Lang sometimes informed passengers of their right to refuse to cooperate. On the day in question, however, he did not.</p>
<p>Respondents were seated next to each other on the bus. Drayton was in the aisle seat, Brown in the seat next to the window. Lang approached respondents from the rear and leaned over Drayton's shoulder. He held up his badge long enough for respondents to identify him as a police officer. With his face 12-to-18 inches away from Drayton's, Lang spoke in a voice just loud enough for respondents to hear:</p>
<blockquote>"I'm Investigator Lang with the Tallahassee Police Department. We're conducting bus interdiction <i>[sic],</i>  attempting to deter drugs and illegal weapons being transported on the bus. Do you have any bags on the bus?" App. 55.</blockquote>
<p><span class="star-pagination">*199</span> Both respondents pointed to a single green bag in the overhead luggage rack. Lang asked, "Do you mind if I check it?," and Brown responded, "Go ahead." <i>Id.,</i> at 56. Lang handed the bag to Officer Blackburn to check. The bag contained no contraband.</p>
<p>Officer Lang noticed that both respondents were wearing heavy jackets and baggy pants despite the warm weather. In Lang's experience drug traffickers often use baggy clothing to conceal weapons or narcotics. The officer thus asked Brown if he had any weapons or drugs in his possession. And he asked Brown: "Do you mind if I check your person?" Brown answered, "Sure," and cooperated by leaning up in his seat, pulling a cell phone out of his pocket, and opening up his jacket. <i>Id.,</i> at 61. Lang reached across Drayton and patted down Brown's jacket and pockets, including his waist area, sides, and upper thighs. In both thigh areas, Lang detected hard objects similar to drug packages detected on other occasions. Lang arrested and handcuffed Brown. Officer Hoover escorted Brown from the bus.</p>
<p>Lang then asked Drayton, "Mind if I check you?" <i>Id.,</i>  at 65. Drayton responded by lifting his hands about eight inches from his legs. Lang conducted a patdown of Drayton's thighs and detected hard objects similar to those found on Brown. He arrested Drayton and escorted him from the bus. A further search revealed that respondents had ducttaped plastic bundles of powder cocaine between several pairs of their boxer shorts. Brown possessed three bundles containing 483 grams of cocaine. Drayton possessed two bundles containing 295 grams of cocaine.</p>
<p>Respondents were charged with conspiring to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846, and with possessing cocaine with intent to distribute it, in violation of § 841(a)(1). They moved to suppress the cocaine, arguing that the consent to the patdown search was invalid. Following a hearing at which only Officer Lang testified, the <span class="star-pagination">*200</span> United States District Court for the Northern District of Florida denied their motions to suppress. The District Court determined that the police conduct was not coercive and respondents' consent to the search was voluntary. The District Court pointed to the fact that the officers were dressed in plain clothes, did not brandish their badges in an authoritative manner, did not make a general announcement to the entire bus, and did not address anyone in a menacing tone of voice. It noted that the officers did not block the aisle or the exit, and stated that it was "obvious that [respondents] can get up and leave, as can the people ahead of them." App. 132. The District Court concluded: "[E]verything that took place between Officer Lang and Mr. Drayton and Mr. Brown suggests that it was cooperative. There was nothing coercive, there was nothing confrontational about it." <i>Ibid.</i> </p>
<p>The Court of Appeals for the Eleventh Circuit reversed and remanded with instructions to grant respondents' motions to suppress. <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d 787</a></span> (2000). The court held that this disposition was compelled by its previous decisions in <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">151 F. 3d 1354</a></span> (1998), and <i>United States</i> v. <i>Guapi,</i> <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">144 F. 3d 1393</a></span> (1998). Those cases had held that bus passengers do not feel free to disregard police officers' requests to search absent "some positive indication that consent could have been refused." <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/#1357" aria-description="Citation for case: United States v. Washington"><i>Washington, supra,</i> at 1357</a></span>.</p>
<p>We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./534/1074/">534 U. S. 1074</a></span> (2002). The respondents, we conclude, were not seized and their consent to the search was voluntary; and we reverse.</p>
<p></p>
<h2>II</h2>
<p>Law enforcement officers do not violate the Fourth Amendment's prohibition of unreasonable seizures merely by approaching individuals on the street or in other public places and putting questions to them if they are willing to listen. See, <i>e. g., </i><i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 497</a></span> (1983) <span class="star-pagination">*201</span> (plurality opinion); see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523, n. 3</a></span> (Rehnquist, J., dissenting); <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 5-6</a></span> (1984) <i>(per curiam)</i> (holding that such interactions in airports are "the sort of consensual encounter[s] that implicat[e] no Fourth Amendment interest"). Even when law enforcement officers have no basis for suspecting a particular individual, they may pose questions, ask for identification, and request consent to search luggageprovided they do not induce cooperation by coercive means. See <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 434-435</a></span> (citations omitted). If a reasonable person would feel free to terminate the encounter, then he or she has not been seized.</p>
<p>The Court has addressed on a previous occasion the specific question of drug interdiction efforts on buses. In <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span>,</i> two police officers requested a bus passenger's consent to a search of his luggage. The passenger agreed, and the resulting search revealed cocaine in his suitcase. The Florida Supreme Court suppressed the cocaine. In doing so it adopted a <i>per se</i> rule that due to the cramped confines onboard a bus the act of questioning would deprive a person of his or her freedom of movement and so constitute a seizure under the Fourth Amendment.</p>
<p>This Court reversed. <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> first made it clear that for the most part <i>per se</i> rules are inappropriate in the Fourth Amendment context. The proper inquiry necessitates a consideration of "all the circumstances surrounding the encounter." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 439</a></span>. The Court noted next that the traditional rule, which states that a seizure does not occur so long as a reasonable person would feel free "to disregard the police and go about his business," <i>California</i> v. <i>Hodari D.,</i>  <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#628" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 628</a></span> (1991), is not an accurate measure of the coercive effect of a bus encounter. A passenger may not want to get off a bus if there is a risk it will depart before the opportunity to reboard. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#434" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 434-436</a></span>. A bus rider's movements are confined in this sense, but this is the natural result of choosing to take the bus; it says nothing <span class="star-pagination">*202</span> about whether the police conduct is coercive. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#436" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 436</a></span>. The proper inquiry "is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter." <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Ibid.</a></span></i> Finally, the Court rejected Bostick's argument that he must have been seized because no reasonable person would consent to a search of luggage containing drugs. The reasonable person test, the Court explained, is objective and "presupposes an <i>innocent</i> person." <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 437-438</a></span>.</p>
<p>In light of the limited record, <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> refrained from deciding whether a seizure occurred. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 437</a></span>. The Court, however, identified two factors "particularly worth noting" on remand. <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#432" aria-description="Citation for case: Florida v. Bostick"><i>Id.,</i> at 432</a></span>. First, although it was obvious that an officer was armed, he did not remove the gun from its pouch or use it in a threatening way. Second, the officer advised the passenger that he could refuse consent to the search. <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Ibid.</a></span></i> </p>
<p>Relying upon this latter factor, the Eleventh Circuit has adopted what is in effect a <i>per se</i> rule that evidence obtained during suspicionless drug interdiction efforts aboard buses must be suppressed unless the officers have advised passengers of their right not to cooperate and to refuse consent to a search. In <i>United States</i> v. <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi, supra</a></span></i><i>,</i> the Court of Appeals described "[t]he most glaring difference" between the encounters in <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> and in <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> as "the complete lack of any notification to the passengers that they were in fact free to decline the search request. . . . Providing [this] simple notification . . . is perhaps the most efficient and effective method to ensure compliance with the Constitution." <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/#1395" aria-description="Citation for case: United States v. Guapi">144 F. 3d, at 1395</a></span>. The Court of Appeals then listed other factors that contributed to the coerciveness of the encounter: (1) the officer conducted the interdiction before the passengers disembarked from the bus at a scheduled stop; (2) the officer explained his presence in the form of a general announcement to the entire bus; (3) the officer wore a police uniform; and (4) the officer questioned passengers as he <span class="star-pagination">*203</span> moved from the front to the rear of the bus, thus obstructing the path to the exit. <span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/#1396" aria-description="Citation for case: United States v. Guapi"><i>Id.,</i> at 1396</a></span>.</p>
<p>After its decision in <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> the Court of Appeals decided <i>United States</i> v. <i><span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Washington</a></span></i> and the instant case. The court suppressed evidence obtained during similar drug interdiction efforts despite the following facts: (1) the officers in both cases conducted the interdiction after the passengers had reboarded the bus; (2) the officer in the present case did not make a general announcement to the entire bus but instead spoke with individual passengers; (3) the officers in both cases were not in uniform; and (4) the officers in both cases questioned passengers as they moved from the rear to the front of the bus and were careful not to obstruct passengers' means of egress from the bus.</p>
<p>Although the Court of Appeals has disavowed a <i>per se</i> requirement, the lack of an explicit warning to passengers is the only element common to all its cases. See <i>Washington,</i>  <span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/#1357" aria-description="Citation for case: United States v. Washington">151 F. 3d, at 1357</a></span> ("It seems obvious to us that if police officers genuinely want to ensure that their encounters with bus passengers remain absolutely voluntary, they can simply say so. Without such notice in this case, we do not feel a reasonable person would have felt able to decline the agents' requests"); <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#790" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d, at 790</a></span> (noting that "[t]his case is controlled by" <i><span class="citation" data-id="72919"><a href="/opinion/72919/united-states-v-guapi/" aria-description="Citation for case: United States v. Guapi">Guapi</a></span></i> and <i><span class="citation" data-id="8598546"><a href="/opinion/8619326/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Washington</a></span>,</i> and dismissing any factual differences between the three cases as irrelevant). Under these cases, it appears that the Court of Appeals would suppress any evidence obtained during suspicionless drug interdiction efforts aboard buses in the absence of a warning that passengers may refuse to cooperate. The Court of Appeals erred in adopting this approach.</p>
<p>Applying the <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> framework to the facts of this particular case, we conclude that the police did not seize respondents when they boarded the bus and began questioning passengers. The officers gave the passengers no reason to believe that they were required to answer the officers' questions. When Officer Lang approached respondents, he <span class="star-pagination">*204</span> did not brandish a weapon or make any intimidating movements. He left the aisle free so that respondents could exit. He spoke to passengers one by one and in a polite, quiet voice. Nothing he said would suggest to a reasonable person that he or she was barred from leaving the bus or otherwise terminating the encounter.</p>
<p>There were ample grounds for the District Court to conclude that "everything that took place between Officer Lang and [respondents] suggests that it was cooperative" and that there "was nothing coercive [or] confrontational" about the encounter. App. 132. There was no application of force, no intimidating movement, no overwhelming show of force, no brandishing of weapons, no blocking of exits, no threat, no command, not even an authoritative tone of voice. It is beyond question that had this encounter occurred on the street, it would be constitutional. The fact that an encounter takes place on a bus does not on its own transform standard police questioning of citizens into an illegal seizure. See <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#439" aria-description="Citation for case: Florida v. Bostick">501 U. S., at 439-440</a></span>. Indeed, because many fellow passengers are present to witness officers' conduct, a reasonable person may feel even more secure in his or her decision not to cooperate with police on a bus than in other circumstances.</p>
<p>Respondents make much of the fact that Officer Lang displayed his badge. In <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez">469 U. S., at 5-6</a></span>, however, the Court rejected the claim that the defendant was seized when an officer approached him in an airport, showed him his badge, and asked him to answer some questions. Likewise, in <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#212" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 212-213</a></span> (1984), the Court held that Immigration and Naturalization Service (INS) agents' wearing badges and questioning workers in a factory did not constitute a seizure. And while neither Lang nor his colleagues were in uniform or visibly armed, those factors should have little weight in the analysis. Officers are often required to wear uniforms and in many circumstances this is cause for assurance, not discomfort. <span class="star-pagination">*205</span> Much the same can be said for wearing sidearms. That most law enforcement officers are armed is a fact well known to the public. The presence of a holstered firearm thus is unlikely to contribute to the coerciveness of the encounter absent active brandishing of the weapon.</p>
<p>Officer Hoover's position at the front of the bus also does not tip the scale in respondents' favor. Hoover did nothing to intimidate passengers, and he said nothing to suggest that people could not exit and indeed he left the aisle clear. In <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,</i> the Court determined there was no seizure even though several uniformed INS officers were stationed near the exits of the factory. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#219" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 219</a></span>. The Court noted: "The presence of agents by the exits posed no reasonable threat of detention to these workers, . . . the mere possibility that they would be questioned if they sought to leave the buildings should not have resulted in any reasonable apprehension by any of them that they would be seized or detained in any meaningful way." <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Ibid.</a></span></i> </p>
<p>Finally, the fact that in Officer Lang's experience only a few passengers have refused to cooperate does not suggest that a reasonable person would not feel free to terminate the bus encounter. In Lang's experience it was common for passengers to leave the bus for a cigarette or a snack while the officers were questioning passengers. App. 70, 81. And of more importance, bus passengers answer officers' questions and otherwise cooperate not because of coercion but because the passengers know that their participation enhances their own safety and the safety of those around them. "While most citizens will respond to a police request, the fact that people do so, and do so without being told they are free not to respond, hardly eliminates the consensual nature of the response." <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216</a></span>.</p>
<p>Drayton contends that even if Brown's cooperation with the officers was consensual, Drayton was seized because no reasonable person would feel free to terminate the encounter with the officers after Brown had been arrested. The Court <span class="star-pagination">*206</span> of Appeals did not address this claim; and in any event the argument fails. The arrest of one person does not mean that everyone around him has been seized by police. If anything, Brown's arrest should have put Drayton on notice of the consequences of continuing the encounter by answering the officers' questions. Even after arresting Brown, Lang addressed Drayton in a polite manner and provided him with no indication that he was required to answer Lang's questions.</p>
<p>We turn now from the question whether respondents were seized to whether they were subjected to an unreasonable search, <i>i. e.,</i> whether their consent to the suspicionless search was involuntary. In circumstances such as these, where the question of voluntariness pervades both the search and seizure inquiries, the respective analyses turn on very similar facts. And, as the facts above suggest, respondents' consent to the search of their luggage and their persons was voluntary. Nothing Officer Lang said indicated a command to consent to the search. Rather, when respondents informed Lang that they had a bag on the bus, he asked for their permission to check it. And when Lang requested to search Brown and Drayton's persons, he asked first if they objected, thus indicating to a reasonable person that he or she was free to refuse. Even after arresting Brown, Lang provided Drayton with no indication that he was required to consent to a search. To the contrary, Lang asked for Drayton's permission to search him ("Mind if I check you?"), and Drayton agreed.</p>
<p>The Court has rejected in specific terms the suggestion that police officers must always inform citizens of their right to refuse when seeking permission to conduct a warrantless consent search. See, <i>e. g., </i><i>Ohio</i> v. <i>Robinette,</i> <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39-40</a></span> (1996); <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#227" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 227</a></span> (1973). "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective <span class="star-pagination">*207</span> consent." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span></i> Nor do this Court's decisions suggest that even though there are no <i>per se</i> rules, a presumption of invalidity attaches if a citizen consented without explicit notification that he or she was free to refuse to cooperate. Instead, the Court has repeated that the totality of the circumstances must control, without giving extra weight to the absence of this type of warning. See, <i>e. g., </i><i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth, supra</a></span></i><i>; </i><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette"><i>Robinette, supra,</i> at 39-40</a></span>. Although Officer Lang did not inform respondents of their right to refuse the search, he did request permission to search, and the totality of the circumstances indicates that their consent was voluntary, so the searches were reasonable.</p>
<p>In a society based on law, the concept of agreement and consent should be given a weight and dignity of its own. Police officers act in full accord with the law when they ask citizens for consent. It reinforces the rule of law for the citizen to advise the police of his or her wishes and for the police to act in reliance on that understanding. When this exchange takes place, it dispels inferences of coercion.</p>
<p>We need not ask the alternative question whether, after the arrest of Brown, there were grounds for a <i>Terry</i> stop and frisk of Drayton, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), though this may have been the case. It was evident that Drayton and Brown were traveling togetherOfficer Lang observed the pair reboarding the bus together; they were each dressed in heavy, baggy clothes that were ill-suited for the day's warm temperatures; they were seated together on the bus; and they each claimed responsibility for the single piece of green carry-on luggage. Once Lang had identified Brown as carrying what he believed to be narcotics, he may have had reasonable suspicion to conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop and frisk on Drayton as well. That question, however, has not been presented to us. The fact the officers may have had reasonable suspicion does not prevent them from relying on a citizen's consent to the search. It would be a paradox, and one most puzzling to law enforcement officials and courts alike, were <span class="star-pagination">*208</span> we to say, after holding that Brown's consent was voluntary, that Drayton's consent was ineffectual simply because the police at that point had more compelling grounds to detain him. After taking Brown into custody, the officers were entitled to continue to proceed on the basis of consent and to ask for Drayton's cooperation.</p>
<p>The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Souter, with whom Justice Stevens and Justice Ginsburg join, dissenting.</p>
<p>Anyone who travels by air today submits to searches of the person and luggage as a condition of boarding the aircraft. It is universally accepted that such intrusions are necessary to hedge against risks that, nowadays, even small children understand. The commonplace precautions of air travel have not, thus far, been justified for ground transportation, however, and no such conditions have been placed on passengers getting on trains or buses. There is therefore an air of unreality about the Court's explanation that bus passengers consent to searches of their luggage to "enhanc[e] their own safety and the safety of those around them." <i>Ante,</i> at 205. Nor are the other factual assessments underlying the Court's conclusion in favor of the Government more convincing.</p>
<p>The issue we took to review is whether the police's examination of the bus passengers, including respondents, amounted to a suspicionless seizure under the Fourth Amendment.<sup>[1]</sup> If it did, any consent to search was plainly <span class="star-pagination">*209</span> invalid as a product of the illegal seizure. See <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#507" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 507-508</a></span> (1983) (plurality opinion) ("[T]he consent was tainted by the illegality and . . . ineffective to justify the search"); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span> (Powell, J., concurring); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#509" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 509</a></span> (Brennan, J., concurring in result).</p>
<p><i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), established the framework for determining whether the bus passengers were seized in the constitutional sense. In that case, we rejected the position that police questioning of bus passengers was a <i>per se</i> seizure, and held instead that the issue of seizure was to be resolved under an objective test considering all circumstances: whether a reasonable passenger would have felt "free to decline the officers' requests or otherwise terminate the encounter," <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#436" aria-description="Citation for case: Florida v. Bostick"><i>id.,</i> at 436</a></span>. We thus applied to a bus passenger the more general criterion, whether the person questioned was free "to ignore the police presence and go about his business," <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">id.,</a></span></i> at 437 (quoting <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#569" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 569</a></span> (1988)).</p>
<p>Before applying the standard in this case, it may be worth getting some perspective from different sets of facts. A perfect example of police conduct that supports no colorable claim of seizure is the act of an officer who simply goes up to a pedestrian on the street and asks him a question. See <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S., at 497</a></span>; see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523, n. 3</a></span> (Rehnquist, J., dissenting). A pair of officers questioning a pedestrian, <span class="star-pagination">*210</span> without more, would presumably support the same conclusion. Now consider three officers, one of whom stands behind the pedestrian, another at his side toward the open sidewalk, with the third addressing questions to the pedestrian a foot or two from his face. Finally, consider the same scene in a narrow alley. On such bare bones facts, one may not be able to say a seizure occurred, even in the last case, but one can say without qualification that the atmosphere of the encounters differed significantly from the first to the last examples. In the final instance there is every reason to believe that the pedestrian would have understood, to his considerable discomfort, what Justice Stewart described as the "threatening presence of several officers," <i>United States</i>  v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980) (opinion of Stewart, J.). The police not only carry legitimate authority but also exercise power free from immediate check, and when the attention of several officers is brought to bear on one civilian the imbalance of immediate power is unmistakable. We all understand this, as well as we understand that a display of power rising to Justice Stewart's "threatening" level may overbear a normal person's ability to act freely, even in the absence of explicit commands or the formalities of detention. As common as this understanding is, however, there is little sign of it in the Court's opinion. My own understanding of the relevant facts and their significance follows.</p>
<p>When the bus in question made its scheduled stop in Tallahassee, the passengers were required to disembark while the vehicle was cleaned and refueled. App. 104. When the passengers returned, they gave their tickets to the driver, who kept them and then left himself, after giving three police officers permission to board the bus in his absence. <i>Id.,</i> at 77-78. Although they were not in uniform, the officers displayed badges and identified themselves as police. One stationed himself in the driver's seat by the door at the front, facing back to observe the passengers. The two others went to the rear, from which they worked their way forward, <span class="star-pagination">*211</span> with one of them speaking to passengers, the other backing him up. <i>Id.,</i> at 47-48. They necessarily addressed the passengers at very close range; the aisle was only 15 inches wide, and each seat only 18.<sup>[2]</sup> The quarters were cramped further by the overhead rack, 19 inches above the top of the passenger seats. The passenger by the window could not have stood up straight, <i>id.,</i> at 55, and the face of the nearest officer was only a foot or 18 inches from the face of the nearest passenger being addressed, <i>id.,</i> at 57. During the exchanges, the officers looked down, and the passengers had to look up if they were to face the police. The officer asking the questions spoke quietly. He prefaced his requests for permission to search luggage and do a body patdown by identifying himself by name as a police investigator "conducting bus interdiction" and saying, "`We would like for your cooperation. Do you have any luggage on the bus?'" <i>Id.,</i> at 82.</p>
<p>Thus, for reasons unexplained, the driver with the tickets entitling the passengers to travel had yielded his custody of the bus and its seated travelers to three police officers, whose authority apparently superseded the driver's own. The officers took control of the entire passenger compartment, one stationed at the door keeping surveillance of all the occupants, the others working forward from the back. With one officer right behind him and the other one forward, a third officer accosted each passenger at quarters extremely close and so cramped that as many as half the passengers could not even have stood to face the speaker. None was asked whether he was willing to converse with the police or to take part in the enquiry. Instead the officer said the police were "conducting bus interdiction," in the course of which they "would like . . . cooperation." <i>Ibid.</i> The reasonable inference was that the "interdiction" was not a consensual exercise, but one the police would carry out whatever <span class="star-pagination">*212</span> the circumstances; that they would prefer "cooperation" but would not let the lack of it stand in their way. There was no contrary indication that day, since no passenger had refused the cooperation requested, and there was no reason for any passenger to believe that the driver would return and the trip resume until the police were satisfied. The scene was set and an atmosphere of obligatory participation was established by this introduction. Later requests to search prefaced with "Do you mind . . ." would naturally have been understood in the terms with which the encounter began.</p>
<p>It is very hard to imagine that either Brown or Drayton would have believed that he stood to lose nothing if he refused to cooperate with the police, or that he had any free choice to ignore the police altogether. No reasonable passenger could have believed that, only an uncomprehending one. It is neither here nor there that the interdiction was conducted by three officers, not one, as a safety precaution. See <i>id.,</i> at 47. The fact was that there were three, and when Brown and Drayton were called upon to respond, each one was presumably conscious of an officer in front watching, one at his side questioning him, and one behind for cover, in case he became unruly, perhaps, or "cooperation" was not forthcoming. The situation is much like the one in the alley, with civilians in close quarters, unable to move effectively, being told their cooperation is expected. While I am not prepared to say that no bus interrogation and search can pass the <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i> test without a warning that passengers are free to say no, the facts here surely required more from the officers than a quiet tone of voice. A police officer who is certain to get his way has no need to shout.</p>
<p>It is true of course that the police testified that a bus passenger sometimes says no, App. 81, but that evidence does nothing to cast the facts here in a different light. We have no way of knowing the circumstances in which a passenger elsewhere refused a request; maybe that has happened only <span class="star-pagination">*213</span> when the police have told passengers they had a right to refuse (as the officers sometimes advised them), <i>id.,</i> at 81-82. Nor is it fairly possible to see the facts of this case differently by recalling <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984), as precedent. In that case, a majority of this Court found no seizure when a factory force was questioned by immigration officers, with an officer posted at every door leading from the workplace. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#219" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 219</a></span>. Whether that opinion was well reasoned or not, the facts as the Court viewed them differed from the case here. <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> considered an order granting summary judgment in favor of respondents, with the consequence that the Court was required to construe the record and all issues of fact favorably to the Immigration and Naturalization Service. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#214" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 214</a></span>; <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#221" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 221</a></span> (Stevens, J., concurring). The Court therefore emphasized that even after "th[e] surveys were initiated, the employees were about their ordinary business, operating machinery and performing other job assignments." <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 218</a></span>. In this case, however, Brown and Drayton were seemingly pinned-in by the officers and the customary course of events was stopped flat. The bus was going nowhere, and with one officer in the driver's seat, it was reasonable to suppose no passenger would tend to his own business until the officers were ready to let him.</p>
<p>In any event, I am less concerned to parse this case against <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> than to apply <i><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">Bostick</a></span></i>'s totality of circumstances test, and to ask whether a passenger would reasonably have felt free to end his encounter with the three officers by saying no and ignoring them thereafter. In my view the answer is clear. The Court's contrary conclusion tells me that the majority cannot see what Justice Stewart saw, and I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Daniel J. Popeo</i> and <i>Richard A. Samp</i> filed a brief for the Washington Legal Foundation et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>Leon Friedman</i> and <i>Joshua L. Dratel</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p><i>James P. Manak, Wayne W. Schmidt, Richard Weintraub, Bernard J. Farber,</i> and <i>Carl Milazzo</i> filed a brief for Americans For Effective Law Enforcement, Inc., et al. as <i>amici curiae.</i> </p>
<p>[1]  The Court proceeds to resolve the voluntariness issue on the heels of its seizure enquiry, but the voluntariness of respondents' consent was not within the question the Court accepted for review. Accord, Reply Brief for United States 20, n. 7 (stating that the consent issue "is not presented by this case; the question here is whether there was an illegal seizure in the first place"). While it is true that the Eleventh Circuit purported to address the question "whether the consent given by each defendant for the search was `uncoerced and legally voluntary,' " <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#788" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d 787, 788</a></span> (2000), elsewhere the court made it clear that it was applying the test in <i>Florida</i> v. <i>Bostick,</i> <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429</a></span> (1991), which is relevant to the issue of seizure, <span class="citation" data-id="771014"><a href="/opinion/771014/united-states-of-amercia-v-christopher-drayton-clifton-brown-jr/#791" aria-description="Citation for case: United States of Amercia v. Christopher Drayton &amp; Clifton...">231 F. 3d, at 791, n. 6</a></span>. There is thus no occasion here to reach any issue of consent untainted by seizure. If there were, the consent would have to satisfy the voluntariness test of <i>Schneckloth</i> v. <i>Bustamonte,</i>  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973), which focuses on "the nature of a person's subjective understanding," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#230" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i> at 230</a></span>, and requires consideration of "the characteristics of the accused [in addition to] the details of the interrogation," <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>id.,</i>  at 226</a></span>.</p>
<p>[2]  The figures are from a Lodging filed by respondents (available in Clerk of Court's case file). The Government does not dispute their accuracy.</p>

</div>
```

---
