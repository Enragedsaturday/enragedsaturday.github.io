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

## GROUP: _overhaul2/lake/cases/United States v. Carpenter (6th Cir. 2019 remand).json  (`lake-record`, 2 assertions)

### content_page

```
---
title: "United States v. Carpenter (6th Cir. 2019 remand)"
type: case
citation: "926 F.3d 313 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir.
court_level: coa
circuit: ca6
year: 2019
date_decided: ""
docket: ""
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4628336/united-states-v-timothy-carpenter/"
  cluster_id: 4628336
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. Carpenter (6th Cir. 2019 remand)"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Good-Faith Exception]]"
    role: Key
related:
  - "[[The Exclusionary Rule]]"
  - "[[Carpenter v. United States]]"
  - "[[United States v. Leon]]"
  - "[[Illinois v. Krull]]"
  - "[[United States v. Warshak]]"
tags:
  - case
  - exclusionary-rule
  - good-faith-exception
  - cell-site-location-information
  - stored-communications-act
holding: "On remand from Carpenter v. United States, the Sixth Circuit held that although the warrantless acquisition of the defendant's historical cell-site location information violated the Fourth Amendment, suppression was not required because the FBI agents obtained the records in objectively reasonable, good-faith reliance on the Stored Communications Act."
---

# United States v. Carpenter (6th Cir. 2019 remand)

*926 F.3d 313 (6th Cir. 2019)* · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4628336 → opinion 4405589; quote string-matched to the CL opinion text 2026-07-07. CAPTION TRAP: this is the Sixth Circuit's 2019 good-faith remand (926 F.3d 313), distinct from the Supreme Court's *Carpenter v. United States*, 585 U.S. 296 (2018). S9 promotes. -->

## Background
FBI agents obtained Timothy Carpenter's historical cell-site location information (CSLI) without a warrant, using court orders issued under the Stored Communications Act (SCA), 18 U.S.C. § 2703(d). The Sixth Circuit initially held that acquiring CSLI was not a Fourth Amendment search. In *[[Carpenter v. United States]]* (2018), the Supreme Court reversed, holding that the warrantless acquisition of the records was a search, and [[Reading and Citing Cases#on-remand|remanded]]. [[Reading and Citing Cases#on-remand|On remand]], the question was whether the CSLI evidence had to be suppressed.

## Issue
Whether the [[The Good-Faith Exception|good-faith exception]] to the exclusionary rule permits admission of CSLI obtained without a warrant in reliance on the Stored Communications Act, after *[[Carpenter v. United States|Carpenter]]* held such acquisition unconstitutional.

## Rule
Evidence obtained in objectively reasonable, good-faith reliance on a statute later held not to authorize the search is not subject to exclusion, because suppression would not deter police who simply followed a duly enacted law (*[[United States v. Leon|Leon]]*; *[[Illinois v. Krull]]*). Applying that rule, the panel held: "Because these agents reasonably relied on the Stored Communications Act (SCA), we AFFIRM the judgment of the district court." — 926 F.3d at 313. ^pin-313

## Application
The unconstitutionality of the CSLI acquisition was not clear until after the Supreme Court reversed the panel's own prior decision; the agents had followed the SCA's § 2703(d) procedure, and nothing in the record suggested intentional misconduct. Because suppression would serve no deterrent purpose where officers relied in good faith on the statute then governing CSLI acquisition, the exclusionary rule did not apply, and the panel affirmed the denial of suppression.

## Conclusion
The judgment of the district court denying suppression was **affirmed**. The Sixth Circuit panel affirmed.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. The remand is a leading application of the *[[United States v. Leon|Leon]]*/*[[Illinois v. Krull|Krull]]* [[The Good-Faith Exception|good-faith exception]] at the digital-surveillance frontier: even after *[[Carpenter v. United States|Carpenter]]* made the CSLI acquisition a search, statute-reliance good faith defeated suppression. **Caption note:** distinct from the Supreme Court's *[[Carpenter v. United States]]*, 585 U.S. 296 (2018) — both pages exist deliberately.

## Appears on
- [[The Exclusionary Rule]] — *Key*

## Sources
- [*United States v. Carpenter*, 926 F.3d 313 (6th Cir. 2019)](https://www.courtlistener.com/opinion/4628336/united-states-v-timothy-carpenter/) — pinpoint: 313 (opening holding, good-faith SCA reliance; the CL text carries paragraph markers rather than internal reporter star pagination, so the opening holding sits on the reporter's first page, 926 F.3d 313); cluster 4628336 → opinion 4405589; quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "13cd2758549e90d6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Carpenter (6th Cir. 2019 remand)"}, "payload": {"all": [{"cite": "926 F.3d 313", "page": "313", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "926"}], "display": "926 F.3d 313", "official": {"cite": "926 F.3d 313", "page": "313", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "926"}, "official_selection_present": true, "record_id": "United States v. Carpenter (6th Cir. 2019 remand)"}}
{"assertion_id": "50ff29bdc08ceeb9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Carpenter (6th Cir. 2019 remand)"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Carpenter (6th Cir. 2019 remand)", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Carpenter (6th Cir. 2019 remand)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Carpenter (6th Cir. 2019 remand)",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Timothy Carpenter",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Timothy Ivory CARPENTER, Defendant-Appellant.",
    "input_case_name": "United States v. Carpenter",
    "court": "6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": null,
    "year": 2019,
    "docket": null,
    "cluster_id": 4628336,
    "lead_opinion_id": 4405589,
    "sibling_ids": [],
    "absolute_url": "/opinion/4628336/united-states-v-timothy-carpenter/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "926 F.3d 313",
      "volume": "926",
      "reporter": "F.3d",
      "page": "313",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "926 F.3d 313",
        "volume": "926",
        "reporter": "F.3d",
        "page": "313",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "926 F.3d 313",
    "official_selection": {
      "court_class": "coa",
      "selected": "926 F.3d 313",
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
    "date_created": "2026-07-07T01:59:41Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:59:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:59:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:59:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:59:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-carpenter--4628336",
      "to_record_id": "United States v. Carpenter (6th Cir. 2019 remand)",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Carpenter (6th Cir. 2019 remand)

```
                             RECOMMENDED FOR FULL-TEXT PUBLICATION
                                 Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                        File Name: 19a0126p.06

                      UNITED STATES COURT OF APPEALS
                                     FOR THE SIXTH CIRCUIT



 UNITED STATES OF AMERICA,                                  ┐
                                      Plaintiff-Appellee,   │
                                                            │
                                                            >      No. 14-1572
        v.                                                  │
                                                            │
                                                            │
 TIMOTHY IVORY CARPENTER,                                   │
                                   Defendant-Appellant.     │
                                                            ┘

                        On Remand from the United States Supreme Court.
             United States District Court for the Eastern District of Michigan at Detroit.
                        No. 2:12-cr-20218-4—Sean F. Cox, District Judge.

                                  Decided and Filed: June 11, 2019

                  Before: GUY, KETHLEDGE, and STRANCH, Circuit Judges.
                                        _________________

                                             OPINION
                                        _________________

       JANE B. STRANCH, Circuit Judge. This case returns on remand from the Supreme
Court. In our prior opinion, the majority held that the Government’s warrantless collection of
Timothy Ivory Carpenter’s cell-site location information (CSLI) did not violate the Fourth
Amendment. The Supreme Court disagreed.              The unconstitutionality of the Government’s
search was not clear until after the Supreme Court reversed our decision, which leads us to the
question of whether the FBI agents who obtained Carpenter’s CSLI acted in good faith. Because
these agents reasonably relied on the Stored Communications Act (SCA), we AFFIRM the
judgment of the district court.
 No. 14-1572                         United States v. Carpenter                            Page 2


                                       I. BACKGROUND

       A. CSLI and the SCA

       We begin with the basics of CSLI and the related legal framework. CSLI refers to the
time-stamped location records generated each time a wireless device communicates with a
carrier’s network by connecting to the nearest antenna, known as a “cell site.” Carpenter v.
United States (Carpenter II), 138 S. Ct. 2206, 2211 (2018). As cell phone usage has become
ubiquitous, cell sites have proliferated. Id. Each new cell site, in turn, enhances the precision of
cell phone owners’ CSLI. Even in the time elapsed between Carpenter’s trial and the Supreme
Court’s decision in Carpenter II, CSLI had “rapidly approach[ed] GPS-level precision.” Id. at
2219; see also id. (“[W]ith new technology measuring the time and angle of signals hitting their
towers, wireless carriers already have the capability to pinpoint a phone’s location within 50
meters.”).

       The imminent launch of fifth-generation wireless technology, known as 5G, promises to
multiply the number of cell sites in this country. Wireless networks once designed to carry cell
phone traffic will soon support an unprecedented number of devices connected across industries,
including autonomous vehicles, smart homes, wearable devices, industrial machinery, and
drones. See Jill C. Gallagher & Michael E. DeVine, Cong. Research Serv., R45485, Fifth-
Generation (5G) Telecommunications Technologies: Issues for Congress 2–6 (2019). To handle
all the wireless data transmitted by these new technologies, carriers must greatly increase the
number of cell sites nationwide. Verizon, for example, recently estimated that upgrading the
nation’s wireless infrastructure to prepare for 5G will require “100 times more antenna locations
than currently exist,” and AT&T projected “that providers will deploy hundreds of thousands of
wireless facilities in the next few years alone—equal to or more than the number providers have
deployed in total over the last few decades.” In the Matter of Accelerating Wireless Broadband
Deployment by Removing Barriers to Infrastructure Inv., F.C.C. No. 18-133, 2018 WL 4678555,
at *17 (Sept. 27, 2018).

       Against the backdrop of this new era of connected devices, § 2703(d) of the SCA—a
provision first drafted 25 years ago—permits law enforcement to obtain certain records of a
 No. 14-1572                          United States v. Carpenter                            Page 3


person’s wireless communications whenever the government “offers specific and articulable
facts showing that there are reasonable grounds to believe” the records sought “are relevant and
material to an ongoing criminal investigation.”        See Communications Assistance for Law
Enforcement Act, Pub. L. No. 103-414, 108 Stat. 4279, 4292 (1994). Unlike other provisions of
the SCA, the court-ordered production mechanism in § 2703(d) does not require law
enforcement to get a warrant before acquiring these records. Compare 18 U.S.C. § 2703(d) with
id. § 2703(a), (c)(1)(A).    In this case, the Government collected Carpenter’s CSLI under
§ 2703(d); it did not obtain a warrant.

       B. Factual and Procedural History

       Because we and the Supreme Court summarized the facts of this case in prior decisions,
see Carpenter II, 138 S. Ct. at 2211–13; United States v. Carpenter (Carpenter I), 819 F.3d 880,
884–85 (6th Cir. 2016), we focus on the information most relevant to the analysis on remand.
First, a housekeeping matter: Carpenter I addressed the consolidated appeals of both Carpenter
and a codefendant, Timothy Michael Sanders, see 819 F.3d at 884, but only Carpenter sought
Supreme Court review. Carpenter limited his petition for certiorari to the question of whether
the Fourth Amendment permits the warrantless acquisition of CSLI, see Petition for Writ of
Certiorari, Carpenter II, 138 S. Ct. 2206 (No. 16-402), and did not include the other grounds for
appeal that he raised (and we rejected) in Carpenter I, see 819 F.3d at 890–93. We adopt
Carpenter I’s treatment of those issues not considered in Carpenter II. Our task here is only to
apply the Supreme Court’s Fourth Amendment analysis to Carpenter’s case.

       A federal jury convicted Carpenter of robbery and gun charges after he and others
committed a string of robberies in Michigan and Ohio between 2010 and 2012. During its
investigation, the Government sought court orders under § 2703(d) for Carpenter’s CSLI. In
response to the Government’s applications, two magistrate judges ordered Carpenter’s wireless
carriers to provide “the locations of cell/site sector (physical addresses) for the target telephones
at call origination and at call termination for incoming and outgoing calls.”          Carpenter II
described the scope of the CSLI turned over by Carpenter’s carriers:
 No. 14-1572                          United States v. Carpenter                         Page 4


       The first order sought 152 days of cell-site records from MetroPCS, which
       produced records spanning 127 days. The second order requested seven days of
       CSLI from Sprint, which produced two days of records covering the period when
       Carpenter’s phone was “roaming” in northeastern Ohio. Altogether the
       Government obtained 12,898 location points cataloging Carpenter’s
       movements—an average of 101 data points per day.

138 S. Ct. at 2212. Carpenter joined Sanders’s motion in limine to suppress the cell phone data,
which the district court denied.

       At trial, the Government used Carpenter’s CSLI to create a record of his physical
proximity to many of the alleged robberies:

       With the cell-site data provided by Carpenter’s and Sanders’s wireless carriers,
       [FBI agent Christopher] Hess created maps showing that Carpenter’s and
       Sanders’s phones were within a half-mile to two miles of the location of each of
       the robberies around the time the robberies happened. Hess used MetroPCS call-
       detail records, for example, to show that Carpenter was within that proximity of a
       Detroit Radio Shack that was robbed around 10:35 a.m. on December 13, 2010.
       Specifically, MetroPCS records showed that at 10:24 a.m. Carpenter’s phone
       received a call that lasted about four minutes. At the start and end of the call,
       Carpenter’s phone drew its signal from MetroPCS tower 173, sectors 1 and 2,
       located southwest of the store and whose signals point north-northeast. After the
       robbery, Carpenter placed an eight-minute call originating at tower 145, sector 3,
       located northeast of the store, its signal pointing southwest; when the call ended,
       Carpenter’s phone was receiving its signal from tower 164, sector 1, alongside
       Interstate 94, north of the Radio Shack. Hess provided similar analysis
       concerning the locations of Carpenter’s and Sanders’s phones at the time of a
       December 18, 2010 robbery in Detroit; a March 4, 2011 robbery in Warren, Ohio;
       and an April 5, 2011 robbery in Detroit.

Carpenter I, 819 F.3d at 885. The Government emphasized the importance of Carpenter’s CSLI
during its closing argument, saying: “Then there’s another overlay of corroboration and that is
the phone data tracking. Little Tim[othy Carpenter]’s phone just happened to be right where the
first robbery was at the exact time of the robbery, the exact sector.”

       A jury convicted Carpenter of Hobbs Act robbery and related gun charges in violation of
18 U.S.C. §§ 924(c) and 1951(a). The district court sentenced him to more than 100 years in
prison, and he appealed.      We affirmed in a divided opinion, with the majority rejecting
Carpenter’s claim that the Government’s collection of his CSLI was a warrantless search in
 No. 14-1572                          United States v. Carpenter                            Page 5


violation of the Fourth Amendment. Carpenter filed a petition for certiorari, which the Supreme
Court granted.

       C. Carpenter II

       Carpenter II begins by situating the Government’s acquisition of Carpenter’s CSLI at
“the intersection of two lines” of Fourth Amendment precedent. 138 S. Ct. at 2214–15. The first
line “addresses a person’s expectation of privacy in his physical location and movements,” while
the second holds that “a person has no legitimate expectation of privacy in information he
voluntarily turns over to third parties.” See id. at 2215–16 (citation omitted); see also Carpenter
I, 819 F.3d at 895 (Stranch, J., concurring in the judgment).

       As for the first line of precedent, Carpenter II explained that “when the Government
tracks the location of a cell phone it achieves near perfect surveillance, as if it had attached an
ankle monitor to the phone’s user.” 138 S. Ct. at 2218. Key to the Court’s reasoning was the
inability of CSLI to distinguish between public and private life: because a cell phone “faithfully
follows its owner beyond public thoroughfares and into private residences, doctor’s offices,
political headquarters, and other potentially revealing locales,” any collection of CSLI risks
opening “an intimate window into a person’s life, revealing not only his particular movements,
but through them his ‘familial, political, professional, religious, and sexual associations.’” Id. at
2217 (quoting United States v. Jones, 565 U.S. 400, 415 (2012) (Sotomayor, J., concurring)).
The Court found that Carpenter had a “reasonable expectation of privacy in the whole of his
physical movements” as recorded by his CSLI. Id. at 2219.

       Under the second line of cases, the Court held that the third-party doctrine did not shield
the Government’s collection of CSLI from Fourth Amendment safeguards.                 That doctrine
originated decades ago, when “few could have imagined a society in which a phone goes
wherever its owner goes[.]” Id. at 2217. Nor could prior courts have anticipated the “depth,
breadth, and comprehensive reach” of the CSLI used by law enforcement today. Id. at 2223.
Because cell phone owners do not, in any “meaningful sense,” choose to turn over such a
thorough record of their public and private lives, the Court found that the acquisition of
 No. 14-1572                          United States v. Carpenter                             Page 6


Carpenter’s CSLI was a Fourth Amendment search regardless of whether the Government
obtained the data from a third party. Id. at 2220.

       With the Supreme Court’s guidance in mind, we reevaluate whether the district court
properly permitted the Government to introduce Carpenter’s CSLI at trial.

                                          II. ANALYSIS

       “When reviewing the denial of a motion to suppress, we will set aside the district court’s
factual findings only if they are clearly erroneous, but will review de novo the court’s
conclusions of law.” United States v. Lee, 793 F.3d 680, 684 (6th Cir. 2015). The Supreme
Court’s decision in Carpenter II leaves no doubt that the Government’s collection of Carpenter’s
CSLI was a search under the Fourth Amendment. The Government needed a warrant to obtain
that information, and the district court erred in concluding otherwise. As Carpenter II explained:
“Before compelling a wireless carrier to turn over a subscriber’s CSLI, the Government’s
obligation is a familiar one—get a warrant.” 138 S. Ct. at 2221.

       Although the Government should have obtained a warrant in this case, we may
nevertheless affirm the district court’s decision if the Government acquired Carpenter’s CSLI in
good faith reliance on the SCA.         “Though evidence obtained in violation of the Fourth
Amendment is generally excluded, the Supreme Court has held that the exclusionary rule ‘should
be modified so as not to bar the admission of evidence seized in reasonable, good faith reliance
on a search warrant that is subsequently held to be defective.’” United States v. Frazier, 423
F.3d 526, 533 (6th Cir. 2005) (quoting United States v. Leon, 468 U.S. 897, 905 (1984)). In
Illinois v. Krull, the Court extended Leon’s good faith exception to evidence obtained in
reasonable reliance on a statute that is later declared unconstitutional, reasoning “that the greatest
deterrent to the enactment of unconstitutional statutes by a legislature is the power of the courts
to invalidate such statutes.” 480 U.S. 340, 352 (1987); see also id. at 349 (“The application of
the exclusionary rule to suppress evidence obtained by an officer acting in objectively reasonable
reliance on a statute would have as little deterrent effect on the officer’s actions as would the
exclusion of evidence when an officer acts in objectively reasonable reliance on a warrant.”).
 No. 14-1572                          United States v. Carpenter                              Page 7


       That Carpenter II did not invalidate § 2703(d) whole cloth does not meaningfully
distinguish this case from Krull. What matters is whether it was objectively reasonable for the
officers to rely on the statute at the time of the search. See id. Here, it was not unreasonable for
the FBI agents who acquired Carpenter’s CSLI to rely on § 2703(d). The SCA contemplates the
Fourth Amendment’s protections by specifying some instances where warrants are necessary,
see 18 U.S.C. § 2703(a), (c)(1)(A), so one can understand why the agents might have believed—
wrongly, it turns out—that a warrant was not required to obtain CSLI under § 2703(d). And it
was not just these officers who believed that § 2703(d) empowered the Government to acquire
CSLI without a warrant. Two magistrate judges issued court orders granting the Government’s
request to compel the production of Carpenter’s CSLI. At the time these requests were granted,
this circuit had already considered reliance on § 2703(d) to be reasonable. See United States v.
Warshak, 631 F.3d 266, 288–89 (6th Cir. 2010) (finding that government agents relied on
§ 2703(d) in good faith when compelling a defendant’s internet service provider to produce the
defendant’s emails).1 And despite Carpenter’s arguments to the contrary, nothing in the record
suggests that the FBI agents who obtained his CSLI engaged in intentional misconduct.

       Carpenter II confirmed that the SCA does not immunize a government officer’s
collection of CSLI from the safeguards of the Fourth Amendment. Moving forward, traditional
Fourth Amendment principles will replace reflexive or mechanical use of § 2703(d).                The
government must either get a warrant or rely on a recognized exception to the warrant
requirement.

                                        III. CONCLUSION

       Carpenter II teaches that, to avoid “embarrass[ing] the future,” courts must carefully and
incrementally adapt their Fourth Amendment jurisprudence to advancements in the digital era.
138 S. Ct. at 2220 (citation omitted). The Government’s acquisition of Carpenter’s CSLI
violated the Fourth Amendment. The district court nevertheless properly denied suppression


       1
         Although Warshak announced a prospective rule barring the warrantless search of a suspect’s
private emails under § 2703(d), the court did not address any other circumstances where reliance on
§ 2703(d) might be unreasonable. The decision in Warshak therefore would not have alerted the agents in
Carpenter’s case to the unconstitutionality of seeking the CSLI at issue here.
No. 14-1572                     United States v. Carpenter                     Page 8


because the FBI agents relied in good faith on the SCA when they obtained the data. We
therefore AFFIRM.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Castillo.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Castillo
type: case
citation: "70 F.4th 894 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir.
court_level: coa
circuit: ca5
year: 2023
date_decided: 2023-06-19
docket: 22-50060
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
  opinion_url: "https://www.courtlistener.com/opinion/9407477/united-states-v-castillo/"
  cluster_id: 9407477
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Castillo
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - border-searches
  - cell-phone
  - manual-search
  - no-suspicion-required
  - fifth-circuit
holding: "Joining every circuit to have addressed the question, the Fifth Circuit held that no individualized suspicion is required for the government to conduct a manual border search of a cell phone; because agents at a port of entry manually scrolled through Castillo's phone and found child pornography, the search was reasonable by virtue of occurring at the border, and suppression was properly denied."
aliases:
  - United States v. Castillo
  - "United States v. Castillo (5th Cir. 2023)"
---

# United States v. Castillo

*70 F.4th 894 (5th Cir. 2023)* (No. 21-50406) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9407477 → majority opinion 9402953 (Ho, J.; 70 F.4th 894, decided June 19, 2023). Re-keyed in the pre-W5 identity audit from a wrong-case namesake (sentencing/plea-breach Castillo) to the intended border-search Castillo; identity re-verified on read 2026-07-07. Rule quote string-matched to the CL opinion text; slip-style pin (the CL text carries only the 5th Cir. slip pagination, not the 70 F.4th star pages) — S9 verifies the reporter pincite. -->

## Background
Alvaro Castillo crossed the international bridge into Presidio, Texas, near midnight in an RV towing a car and was sent to secondary inspection. Border agents found a revolver hidden between frying pans in the oven, ammunition in a taped pressure cooker, and marijuana in luggage. Castillo admitted owning the contraband and gave agents the passcode to his phone; a Homeland Security agent manually scrolled through the phone's apps and found suspected child pornography, prompting a broader forensic search of his devices. Castillo moved to suppress; the district court refused, and he was convicted on six child-pornography counts.

## Issue
Whether a manual border search of a cell phone requires individualized (reasonable) suspicion under the Fourth Amendment.

## Rule
Searches at the border "are reasonable simply by virtue of the fact that they occur at the border," pursuant to the sovereign's right to protect itself. Although cell phones can be "unusually intrusive" (*[[Riley v. California|Riley]]*), the court did not decide the forensic-search question but adopted the circuits' consensus on manual searches, holding: "every circuit to have addressed the issue has agreed that no individualized suspicion is required for the government to undertake a manual border search of a cell phone. We see no reason to depart from the consensus of the circuits." — slip op. at 1. ^pin-slip1

## Application
The agent's search was a manual one — scrolling by hand through apps on the unlocked phone — not a forensic extraction, and it occurred at a port of entry during a routine secondary inspection. Because a manual border search of a cell phone requires no individualized suspicion, the initial search was reasonable; the images it revealed then supported the further forensic examination. The court expressly reserved the harder, circuit-splitting question whether a forensic border search of a phone requires reasonable suspicion, because deciding the manual-search issue resolved the appeal.

## Conclusion
**Affirmed.** Judge Ho wrote for the panel (Jones, Southwick, Ho, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Castillo* places the Fifth Circuit with the consensus that manual cell-phone searches at the border need no suspicion, while deliberately leaving open the *forensic*-search question that divides the circuits after *[[Riley v. California|Riley]]* and *[[Carpenter v. United States|Carpenter]]* — a live frontier of the *[[Border Searches]]* doctrine.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Castillo*, 70 F.4th 894 (5th Cir. 2023)](https://www.courtlistener.com/opinion/9407477/united-states-v-castillo/) — pinpoint: slip op. at 1 (no individualized suspicion for a manual border search of a cell phone; forensic-search question reserved). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is slip-paginated, so the 70 F.4th star page is not asserted here.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "30d5dff0816ac6b6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Castillo"}, "payload": {"all": [{"cite": "70 F.4th 894", "page": "894", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "70"}], "display": "70 F.4th 894", "official": {"cite": "70 F.4th 894", "page": "894", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "70"}, "official_selection_present": true, "record_id": "United States v. Castillo"}}
{"assertion_id": "b7f47d5f51217b45", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Castillo"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Castillo", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Castillo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Castillo",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Castillo",
    "case_name_short": "Castillo",
    "case_name_full": "",
    "input_case_name": "United States v. Castillo",
    "court": "5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2023-06-19",
    "year": 2023,
    "docket": "22-50060",
    "cluster_id": 9407477,
    "lead_opinion_id": 9402953,
    "sibling_ids": [],
    "absolute_url": "/opinion/9407477/united-states-v-castillo/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "70 F.4th 894",
      "volume": "70",
      "reporter": "F.4th",
      "page": "894",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "70 F.4th 894",
        "volume": "70",
        "reporter": "F.4th",
        "page": "894",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "70 F.4th 894",
    "official_selection": {
      "court_class": "coa",
      "selected": "70 F.4th 894",
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
    "date_created": "2026-07-07T18:15:32Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-castillo--9407477",
      "to_record_id": "United States v. Castillo",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Castillo

```
Case: 21-50406     Document: 00516791307         Page: 1     Date Filed: 06/19/2023




           United States Court of Appeals
                for the Fifth Circuit                                 United States Court of Appeals
                                                                               Fifth Circuit

                                                                             FILED
                                                                         June 19, 2023
                                  No. 21-50406
                                                                        Lyle W. Cayce
                                                                             Clerk

   United States of America,

                                                             Plaintiff—Appellee,

                                       versus

   Alvaro Castillo, Jr.,

                                                         Defendant—Appellant.


                  Appeal from the United States District Court
                       for the Western District of Texas
                           USDC No. 4:19-CR-780-1


   Before Jones, Southwick, and Ho, Circuit Judges.
   James C. Ho, Circuit Judge:
          The Fourth Amendment protects the right of the American people
   “to be secure in their persons, houses, papers, and effects, against
   unreasonable searches and seizures.” U.S. Const. amend. IV. Today we
   address what searches are reasonable and unreasonable at the intersection of
   two established lines of Fourth Amendment precedent—when the
   government searches a cell phone at the border.
          On the one hand, the Supreme Court has long held that “searches
   made at the border . . . are reasonable simply by virtue of the fact that they
Case: 21-50406        Document: 00516791307        Page: 2   Date Filed: 06/19/2023




                                    No. 21-50406


   occur at the border,” “pursuant to the long-standing right of the sovereign
   to protect itself by stopping and examining persons and property crossing
   into this country.” United States v. Ramsey, 431 U.S. 606, 616 (1977).
          But on the other hand, the Court has also made clear that searches of
   modern devices like cell phones can be unusually intrusive. After all, “[c]ell
   phones differ in both a quantitative and a qualitative sense from other objects
   that might be kept on an arrestee’s person.” Riley v. California, 573 U.S. 373,
   393 (2014). Depending on the extent of the search, the government could
   theoretically access virtually every aspect about one’s life based on a single
   handheld device.
          Our circuit has not yet articulated the standard that governs cell phone
   searches at the border. In some circuits, the governing standard depends on
   the extent of the search—whether the government is conducting merely a
   manual search of what is immediately available on the device, or a more
   intrusive forensic search. The circuits are divided over whether reasonable
   suspicion is required for a forensic search of a cell phone at the border. But
   every circuit to have addressed the issue has agreed that no individualized
   suspicion is required for the government to undertake a manual border search
   of a cell phone.
          We see no reason to depart from the consensus of the circuits. And
   adopting that consensus is all we need to do to decide this appeal. We
   accordingly affirm.
                                         I.
          The parties jointly stipulated to the facts that govern this appeal.
   Defendant Alvaro Castillo and two others crossed the international bridge to
   Presidio, Texas, in a recreational vehicle (RV) that was towing a passenger
   car behind it, at around midnight. Upon reaching the port of entry into the
   United States, the RV was sent to secondary inspection—as is standard




                                         2
Case: 21-50406      Document: 00516791307          Page: 3   Date Filed: 06/19/2023




                                    No. 21-50406


   operating procedure when it comes to vehicles of that size entering the
   country at that time of night. Defendant and his companions told border
   agents that they had nothing to declare.
          During the search of the RV, an officer found a .357 revolver taped
   between two frying pans that had been wrapped in packing foam and taped
   inside the oven. The officer also found ammunition for a .357 inside a
   pressure cooker that had been taped shut, as well as evidence of marijuana
   inside of luggage.
          Defendant was placed in a holding cell. He admitted to owning the
   contraband. He also provided the passcode to unlock his cell phone to a
   Homeland Security Investigations special agent.
          The agent manually scrolled through various apps. As a result, he
   found what he believed to be child pornography in the photo section of
   Defendant’s phone.
          Based on those initial findings, various agents conducted a more
   intrusive forensic search of the phone. They also conducted both manual and
   forensic searches of other electronic devices in Defendant’s possession.
   Those efforts produced additional child pornography images.
          Defendant was subsequently indicted on six charges involving child
   pornography. He subsequently moved to suppress the evidence obtained
   from the search of his devices. After a hearing, the district court refused to
   suppress the child pornography. Defendant was found guilty on all six counts
   and sentenced to 720 months imprisonment and a life term of supervised
   release. He filed a timely notice of appeal.
          A district court’s factual findings on a motion to suppress are
   reviewed for clear error, and the court’s ultimate conclusions on whether the
   Fourth Amendment was violated are reviewed de novo. United States v.




                                          3
Case: 21-50406      Document: 00516791307          Page: 4    Date Filed: 06/19/2023




                                    No. 21-50406


   Scroggins, 599 F.3d 433, 440 (5th Cir. 2010). The evidence is reviewed in the
   light most favorable to the prevailing party unless that view is inconsistent
   with the court’s findings or is clearly erroneous in light of the evidence as a
   whole. Id.
                                         II.
          The Fourth Amendment provides that “[t]he right of the people to be
   secure in their persons, houses, papers and effects, against unreasonable
   searches and seizures, shall not be violated.” U.S. Const. amend. IV.
   “[W]arrantless searches are typically unreasonable where a search is
   undertaken by law enforcement officials to discover evidence of criminal
   wrongdoing.” Carpenter v. United States, 138 S. Ct. 2206, 2221 (2018)
   (quotation omitted). “In the absence of a warrant, a search is reasonable only
   if it falls within a specific exception to the warrant requirement.” Riley, 573
   U.S. at 382.
          The border search exception is a “longstanding, historically
   recognized exception to the Fourth Amendment’s general principle that a
   warrant be obtained” for a search. Ramsey, 431 U.S. at 621. “[T]he border-
   search exception allows officers to conduct ‘routine inspections and searches
   of individuals or conveyances seeking to cross . . . borders’ without any
   particularized suspicion of wrongdoing.” United States v. Aguilar, 973 F.3d 445,
   449 (5th Cir. 2020) (quoting Ramsey, 431 U.S. at 619) (emphasis added).
   Moreover, even “[s]o-called ‘nonroutine’ searches need only reasonable
   suspicion, not the higher threshold of probable cause.” United States v.
   Molina-Isidoro, 884 F.3d 287, 291 (5th Cir. 2018). “For border searches both
   routine and not, no case has required a warrant.” Id.
          The “scope of a search conducted under an exception to the warrant
   requirement must be commensurate with its purposes.” Arizona v. Gant, 556
   U.S. 332, 339 (2009). The border search exception reflects “the long-




                                          4
Case: 21-50406     Document: 00516791307           Page: 5   Date Filed: 06/19/2023




                                    No. 21-50406


   standing right of the sovereign to protect itself by stopping and examining
   persons and property crossing into this country.” Ramsey, 431 U.S. at 616.
   “The Government’s interest in preventing the entry of unwanted persons
   and effects is at its zenith at the international border” and has been
   recognized “since the beginning of our Government.” United States v.
   Flores-Montano, 541 U.S. 149, 152–53 (2004). “Historically such broad
   powers have been necessary to prevent smuggling and to prevent prohibited
   articles from entry.” Ramsey, 431 U.S. at 619.
          Accordingly, courts have allowed a variety of border searches without
   requiring either a warrant or reasonable suspicion. See, e.g., Flores–Montano,
   541 U.S. at 155 (“the Government’s authority to conduct suspicionless
   inspections at the border includes the authority to remove, disassemble, and
   reassemble a vehicle’s fuel tank”); Ramsey, 431 U.S. at 620 (“custom
   officials could search, without probable cause and without a warrant,
   envelopes carried by an entering traveler, whether in his luggage or on his
   person,” and “no different constitutional standard should apply simply
   because the envelopes were mailed, not carried”); United States v.
   Chaplinski, 579 F.2d 373, 374 (5th Cir. 1978) (“At the border, customs agents
   need not have a reasonable or articulable suspicion that criminal activity is
   involved to stop one who has traveled from a foreign point, examine his or
   her visa, and search luggage and personal effects for contraband.”).
          To be sure, modern cell phones are fundamentally distinct from other
   personal items. As the Supreme Court observed in Riley, “many of these
   devices are in fact minicomputers that also happen to have the capacity to be
   used as telephones.”      573 U.S. at 393.       “One of the most notable
   distinguishing features of modern cell phones is their immense storage
   capacity.” Id. “Before cell phones, a search of a person was limited by
   physical realities and tended as a general matter to constitute only a narrow
   intrusion on privacy.” Id. But today, “the possible intrusion on privacy is



                                         5
Case: 21-50406      Document: 00516791307          Page: 6   Date Filed: 06/19/2023




                                    No. 21-50406


   not physically limited in the same way when it comes to cell phones.” Id. at
   394. Accordingly, government searches of such devices have the potential to
   be uniquely intrusive.
          The extent of the privacy intrusion, however, will depend on the
   methodology employed by the government agent. “Basic border searches . . .
   require an officer to manually traverse the contents of the traveler’s
   electronic device, limiting in practice the quantity of information available
   during a basic search.” Alasaad v. Mayorkas, 988 F.3d 8, 18 (1st Cir. 2021).
   “And a basic border search does not allow government officials to view
   deleted or encrypted files.” Id. at 19. See also id. at 18–19 (“The CBP Policy
   only allows searches of data resident on the device.”).
          Accordingly, when it comes to manual cell phone searches at the
   border, our sister circuits have uniformly held that Riley does not require
   either a warrant or reasonable suspicion. See, e.g., United States v. Xiang, 67
   F.4th 895, 900 (8th Cir. 2023) (“No Circuit has held that the government
   must obtain a warrant to conduct a routine border search of electronic
   devices.”); Alasaad v. Mayorkas, 988 F.3d 8, 18–19 (1st Cir. 2021) (“We . . .
   agree with the holdings of the Ninth and Eleventh circuits that basic border
   searches are routine searches and need not be supported by reasonable
   suspicion.”); United States v. Cano, 934 F.3d 1002, 1016 (9th Cir. 2019)
   (“manual searches of cell phones at the border are reasonable without
   individualized suspicion”).
          Our sister circuits have differed only as to whether reasonable
   suspicion is required for a more intrusive forensic search of a cell phone at
   the border. Compare, e.g., United States v. Touset, 890 F.3d 1227, 1231 (11th
   Cir. 2018) (“the Fourth Amendment does not require any suspicion [even]
   for forensic searches of electronic devices at the border”), with Cano, 934
   F.3d at 1016 (“we hold that manual searches of cell phones at the border are




                                         6
Case: 21-50406        Document: 00516791307          Page: 7   Date Filed: 06/19/2023




                                      No. 21-50406


   reasonable without individualized suspicion, whereas the forensic
   examination of a cell phone requires a showing of reasonable suspicion”).
             All we need to decide this case, however, is to adopt the consensus
   view of our sister circuits and hold that the government can conduct manual
   cell phone searches at the border without individualized suspicion. After all,
   the manual cell phone search here produced evidence of child pornography.
   So if that search was valid, then it’s hard to see how that would not justify the
   subsequent forensic searches for additional evidence of child pornography.
   And Castillo does not appear to claim otherwise. He argues that the
   government violated the Fourth Amendment by conducting the manual as
   well as forensic searches. But he does not claim that the forensic search was
   invalid even if we find the manual search valid.
             We see no reason to disagree with our sister circuits. Accordingly, we
   hold that no reasonable suspicion is necessary to conduct the sort of routine
   manual cell phone search at the border that occurred here. We therefore
   affirm.




                                            7

```

---

## GROUP: _overhaul2/lake/cases/United States v. Ceccolini.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Ceccolini"
type: case
citation: "435 U.S. 268 (1978)"
parallel_cite: "98 S. Ct. 1054; 55 L. Ed. 2d 268"
neutral_cite: 1978 U.S. LEXIS 70
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-12-05
docket: 76-1151
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ceccolini
  varies_by_point: false
  scope_note: "The witness-attenuation factors remain the governing framework for suppressing live-witness testimony as a fruit; reaffirmed in the modern attenuation line."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109816/united-states-v-ceccolini/"
  cluster_id: 109816
  opinion_id: 109816
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny (attenuation)"
related: ["[[Wong Sun v. United States]]", "[[Brown v. Illinois]]", "[[Nardone v. United States]]", "[[United States v. Crews]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation", "live-witness"]
holding: "Live-witness testimony is far less readily suppressed as a fruit of an illegal search than inanimate evidence; the exclusionary rule applies with much greater reluctance to the discovery of a willing witness."
lake:
  record_id: United States v. Ceccolini
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ceccolini

*435 U.S. 268 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While lawfully in Ceccolini's flower shop on an unrelated matter, a police officer (Biro) idly picked up an envelope and found gambling policy slips inside; he then learned from the shop employee, Lois Hennessey, that the slips belonged to Ceccolini. Months later, FBI agents — without mentioning the slips — interviewed Hennessey, who later testified against Ceccolini at his perjury trial. He moved to suppress her testimony as the fruit of the illegal search of the envelope.

## Issue
Whether the testimony of a live witness whose identity or willingness to testify is discovered through an illegal search must be suppressed as a [[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]] under the same standard applied to inanimate evidence.

## Rule
No — exclusion of live-witness testimony demands a closer connection to the illegality than suppression of an object. "[T]he exclusionary rule should be invoked with much greater reluctance where the claim is based on a causal relationship between a constitutional violation and the discovery of a live witness than when a similar claim is advanced to support suppression of an inanimate object." — 435 U.S. at 280. ^pin-280

Because a witness's willingness to come forward of her own volition attenuates the taint, and because permanently disabling a witness exacts a far higher cost than excluding an object, courts weigh the witness's free will, whether the illegally obtained evidence was used in the questioning, the time elapsed, and the officer's purpose.

## Application
On these facts the connection was sufficiently attenuated. "The evidence indicates overwhelmingly that the testimony given by the witness was an act of her own free will in no way coerced or even induced by official authority as a result of Biro's discovery of the policy slips." — [*Id.* at 279–280](https://www.courtlistener.com/opinion/109816/united-states-v-ceccolini/#:~:text=The%20evidence%20indicates%20overwhelmingly%20that). ^pin-279

The slips themselves were not used in questioning Hennessey; substantial time elapsed between the search, the first contact, and the trial testimony; her identity and relationship to Ceccolini were already well known to investigators; and Biro had no intent to find evidence or a witness when he picked up the envelope. "The cost of permanently silencing Hennessey is too great for an evenhanded system of law enforcement to bear in order to secure such a speculative and very likely negligible deterrent effect." — [*Id.* at 280](https://www.courtlistener.com/opinion/109816/united-states-v-ceccolini/#:~:text=The%20cost%20of%20permanently%20silencing). ^pin-280b

## Conclusion
The degree of [[Fruits and Attenuation|attenuation]] was sufficient to dissipate the connection between the illegal search and Hennessey's testimony; the Court of Appeals erred, and its suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ceccolini* builds on the [[Fruits and Attenuation|attenuation]] principle of [[Nardone v. United States]] and [[Wong Sun v. United States]], holding that live-witness testimony is suppressed as a fruit only with "much greater reluctance"; the [[Brown v. Illinois]] [[Fruits and Attenuation|attenuation]] factors govern the closely related confession context.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny ([[Fruits and Attenuation|attenuation]])*

## Sources
- *United States v. Ceccolini*, 435 U.S. 268 (1978) — https://www.courtlistener.com/opinion/109816/united-states-v-ceccolini/ — pinpoints: 279–280, 280.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f84dc65d9c9f9d5d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ceccolini"}, "payload": {"all": [{"cite": "435 U.S. 268", "page": "268", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "435"}, {"cite": "98 S. Ct. 1054", "page": "1054", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "55 L. Ed. 2d 268", "page": "268", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "55"}, {"cite": "1978 U.S. LEXIS 70", "page": "70", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "435 U.S. 268", "official": {"cite": "435 U.S. 268", "page": "268", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "435"}, "official_selection_present": true, "record_id": "United States v. Ceccolini"}}
{"assertion_id": "2ed695a4b365276b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-279", "record_id": "United States v. Ceccolini"}, "payload": {"fragment": "#:~:text=The%20evidence%20indicates%20overwhelmingly%20that", "page": null, "pin_id": "pin-279", "pinpoint_status": "star-verified", "quote": "The evidence indicates overwhelmingly that the testimony given by the witness was an act of her own free will in no way coerced or even induced by official authority as a result of Biro's discovery of the policy slips.", "quote_fidelity": "matched", "record_id": "United States v. Ceccolini", "star_marker": "279"}}
{"assertion_id": "de967a0daf797c93", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-280b", "record_id": "United States v. Ceccolini"}, "payload": {"fragment": "#:~:text=The%20cost%20of%20permanently%20silencing", "page": null, "pin_id": "pin-280b", "pinpoint_status": "star-verified", "quote": "The cost of permanently silencing Hennessey is too great for an evenhanded system of law enforcement to bear in order to secure such a speculative and very likely negligible deterrent effect.", "quote_fidelity": "matched", "record_id": "United States v. Ceccolini", "star_marker": "280"}}
{"assertion_id": "e010112b1208d439", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-280", "record_id": "United States v. Ceccolini"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-280", "pinpoint_status": "slip-only", "quote": "--- # United States v. Ceccolini *435 U.S. 268 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While lawfully in Ceccolini's flower shop on an unrelated matter, a police officer (Biro) idly picked up an envelope and found gambling policy slips inside; he then learned from the shop employee, Lois Hennessey, that the slips belonged to Ceccolini. Months later, FBI agents — without mentioning the slips — interviewed Hennessey, who later testified against Ceccolini at his perjury trial. He moved to suppress her testimony as the fruit of the illegal search of the envelope. ## Issue Whether the testimony of a live witness whose identity or willingness to testify is discovered through an illegal search must be suppressed as a fruit of the poisonous tree under the same standard applied to inanimate evidence. ## Rule No — exclusion of live-witness testimony demands a closer connection to the illegality than suppression of an object.", "quote_fidelity": "mismatch", "record_id": "United States v. Ceccolini", "star_marker": null}}
{"assertion_id": "9a12643c93bed5ea", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ceccolini"}, "payload": {"as_of_content": "1978-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Ceccolini", "scope_note": "The witness-attenuation factors remain the governing framework for suppressing live-witness testimony as a fruit; reaffirmed in the modern attenuation line.", "varies_by_point": false}}
```

### lake record — United States v. Ceccolini

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ceccolini",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ceccolini",
    "case_name_short": "Ceccolini",
    "case_name_full": "United States v. Ceccolini",
    "input_case_name": "United States v. Ceccolini",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-12-05",
    "year": 1978,
    "docket": "76-1151",
    "cluster_id": 109816,
    "lead_opinion_id": 109816,
    "sibling_ids": [
      109816,
      9427104,
      9427105
    ],
    "absolute_url": "/opinion/109816/united-states-v-ceccolini/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "435 U.S. 268",
      "volume": "435",
      "reporter": "U.S.",
      "page": "268",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 1054",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1054",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 L. Ed. 2d 268",
        "volume": "55",
        "reporter": "L. Ed. 2d",
        "page": "268",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 70",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "70",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "435 U.S. 268",
        "volume": "435",
        "reporter": "U.S.",
        "page": "268",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 1054",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1054",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 L. Ed. 2d 268",
        "volume": "55",
        "reporter": "L. Ed. 2d",
        "page": "268",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 70",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "70",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "435 U.S. 268",
    "official_selection": {
      "court_class": "scotus",
      "selected": "435 U.S. 268",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-280",
      "page": null,
      "quote": "--- # United States v. Ceccolini *435 U.S. 268 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While lawfully in Ceccolini's flower shop on an unrelated matter, a police officer (Biro) idly picked up an envelope and found gambling policy slips inside; he then learned from the shop employee, Lois Hennessey, that the slips belonged to Ceccolini. Months later, FBI agents \u2014 without mentioning the slips \u2014 interviewed Hennessey, who later testified against Ceccolini at his perjury trial. He moved to suppress her testimony as the fruit of the illegal search of the envelope. ## Issue Whether the testimony of a live witness whose identity or willingness to testify is discovered through an illegal search must be suppressed as a fruit of the poisonous tree under the same standard applied to inanimate evidence. ## Rule No \u2014 exclusion of live-witness testimony demands a closer connection to the illegality than suppression of an object.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-279",
      "page": null,
      "quote": "The evidence indicates overwhelmingly that the testimony given by the witness was an act of her own free will in no way coerced or even induced by official authority as a result of Biro's discovery of the policy slips.",
      "star_marker": "279",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 25384,
      "fragment": "#:~:text=The%20evidence%20indicates%20overwhelmingly%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-280b",
      "page": null,
      "quote": "The cost of permanently silencing Hennessey is too great for an evenhanded system of law enforcement to bear in order to secure such a speculative and very likely negligible deterrent effect.",
      "star_marker": "280",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26667,
      "fragment": "#:~:text=The%20cost%20of%20permanently%20silencing",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ceccolini",
    "varies_by_point": false,
    "scope_note": "The witness-attenuation factors remain the governing framework for suppressing live-witness testimony as a fruit; reaffirmed in the modern attenuation line.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4371038,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ghim",
          "cluster_id": 4312059,
          "cite": [
            "360 Or. 425",
            "381 P.3d 789",
            "2016 Ore. LEXIS 680"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gary Lee Wipf",
          "cluster_id": 789199,
          "cite": [
            "397 F.3d 677",
            "66 Fed. R. Serv. 605",
            "2005 U.S. App. LEXIS 2635",
            "2005 WL 356505"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Osama Awadallah",
          "cluster_id": 784129,
          "cite": [
            "349 F.3d 42",
            "2 A.L.R. Fed. 2d 705",
            "2003 U.S. App. LEXIS 22879",
            "2003 WL 22519622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez-Moran",
          "cluster_id": 7170059,
          "cite": [
            "17 F. App'x 539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cantu",
          "cluster_id": 22035,
          "cite": [
            "230 F.3d 148",
            "2000 WL 1481157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez-Gonzalez",
          "cluster_id": 9449,
          "cite": [
            "87 F.3d 712",
            "1996 WL 361327"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Finger",
          "cluster_id": 6115945,
          "cite": [
            "208 A.D.2d 645",
            "617 N.Y.S.2d 358",
            "1994 N.Y. App. Div. LEXIS 9537"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Finger",
          "cluster_id": 6066072,
          "cite": [
            "166 A.D.2d 714",
            "561 N.Y.S.2d 471",
            "1990 N.Y. App. Div. LEXIS 13221"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jesus Ramirez-Sandoval",
          "cluster_id": 521934,
          "cite": [
            "872 F.2d 1392",
            "1989 U.S. App. LEXIS 5020",
            "1989 WL 35626"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
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
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
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
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Elstad",
          "cluster_id": 111364,
          "cite": [
            "84 L. Ed. 2d 222",
            "105 S. Ct. 1285",
            "470 U.S. 298",
            "1985 U.S. LEXIS 60",
            "53 U.S.L.W. 4244"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Branti v. Finkel",
          "cluster_id": 110232,
          "cite": [
            "63 L. Ed. 2d 574",
            "100 S. Ct. 1287",
            "445 U.S. 507",
            "1980 U.S. LEXIS 4",
            "1 I.E.R. Cas. (BNA) 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 109895,
          "cite": [
            "57 L. Ed. 2d 65",
            "98 S. Ct. 2187",
            "437 U.S. 82",
            "1978 U.S. LEXIS 109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
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
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lyng v. Northwest Indian Cemetery Protective Assn.",
          "cluster_id": 112037,
          "cite": [
            "99 L. Ed. 2d 534",
            "108 S. Ct. 1319",
            "485 U.S. 439",
            "1988 U.S. LEXIS 1871",
            "18 Envtl. L. Rep. (Envtl. Law Inst.) 21043",
            "56 U.S.L.W. 4292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Russell",
          "cluster_id": 1296847,
          "cite": [
            "882 P.2d 747",
            "125 Wash. 2d 24",
            "63 U.S.L.W. 2291",
            "1994 Wash. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodman v. Lukens Steel Co.",
          "cluster_id": 111926,
          "cite": [
            "96 L. Ed. 2d 572",
            "107 S. Ct. 2617",
            "482 U.S. 656",
            "1987 U.S. LEXIS 2730",
            "55 U.S.L.W. 4881",
            "44 Fair Empl. Prac. Cas. (BNA) 1",
            "43 Empl. Prac. Dec. (CCH) 37,099"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyer",
          "cluster_id": 2515839,
          "cite": [
            "133 P.3d 581",
            "42 Cal. Rptr. 3d 677",
            "38 Cal. 4th 412",
            "2006 Daily Journal DAR 5671",
            "2006 Cal. Daily Op. Serv. 3863",
            "2006 Cal. LEXIS 5397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 1247657,
          "cite": [
            "767 P.2d 1047",
            "47 Cal. 3d 1194",
            "255 Cal. Rptr. 569",
            "1989 Cal. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaetano Modica",
          "cluster_id": 396890,
          "cite": [
            "663 F.2d 1173",
            "1981 U.S. App. LEXIS 16444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Alston",
          "cluster_id": 2283490,
          "cite": [
            "440 A.2d 1311",
            "88 N.J. 211",
            "1981 N.J. LEXIS 1677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Thomas Cherry",
          "cluster_id": 450747,
          "cite": [
            "759 F.2d 1196",
            "81 A.L.R. Fed. 303",
            "1985 U.S. App. LEXIS 29511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McCurdy",
          "cluster_id": 2718099,
          "cite": [
            "59 Cal. 4th 1063",
            "331 P.3d 265",
            "176 Cal. Rptr. 3d 103",
            "2014 WL 3953468",
            "2014 Cal. LEXIS 5467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thurman",
          "cluster_id": 1367765,
          "cite": [
            "846 P.2d 1256",
            "203 Utah Adv. Rep. 18",
            "1993 Utah LEXIS 40",
            "1993 WL 4794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny L. Marshall v. Secretary, Florida Department of Corrections",
          "cluster_id": 4237860,
          "cite": [
            "828 F.3d 1277",
            "2016 U.S. App. LEXIS 12812",
            "2016 WL 3742164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ceccolini:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109816 OR 9427104 OR 9427105) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDg3NzQ0MDAwMDAmcz01MjE5MzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109816+OR+9427104+OR+9427105%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(109816 OR 9427104 OR 9427105)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDAmcz0xMjkzMjE5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109816+OR+9427104+OR+9427105%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109816 OR 9427104 OR 9427105)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109816 OR 9427104 OR 9427105)",
    "indexed_citing_opinions": 463,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109816,
        "count": 431,
        "count_source": "search"
      },
      {
        "opinion_id": 9427104,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9427105,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 702,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ceccolini.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1NzI2Mjcmcz00NDMwNDIyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109816+OR+9427104+OR+9427105%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109816,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 100989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 102843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 103657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 108949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 109546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 253629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 262430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109816,
        "cited_id": 339153,
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
    "date_created": "2026-07-05T23:02:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:02:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:02:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:02:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ceccolini

```
<div>
<center><b><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/" aria-description="Citation for case: United States v. Ceccolini">435 U.S. 268</a></span> (1978)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
CECCOLINI.</h1></center>
<center>No. 76-1151.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 5, 1977.</center>
<center>Decided March 21, 1978.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*269</span> <i>Richard A. Allen</i> argued the cause for the United States. With him on the brief were <i>Solicitor General McCree, Assistant Attorney General Civiletti, Deputy Solicitor General Frey,</i> and <i>Sidney M. Glazer.</i></p>
<p><i>Leon J. Greenspan</i> argued the cause and filed a brief for respondent.</p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>In December 1974, Ronald Biro, a uniformed police officer on assignment to patrol school crossings, entered respondent's place of business, the Sleepy Hollow Flower Shop, in North Tarrytown, N. Y. He went behind the customer counter and, in the words of Ichabod Crane, one of Tarrytown's more <span class="star-pagination">*270</span> illustrious inhabitants of days gone past, "tarried," spending his short break engaged in conversation with his friend Lois Hennessey, an employee of the shop. During the course of the conversation he noticed an envelope with money sticking out of it lying on the drawer of the cash register behind the counter. Biro picked up the envelope and, upon examining its contents, discovered that it contained not only money but policy slips. He placed the envelope back on the register and, without telling Hennessey what he had seen, asked her to whom the envelope belonged. She replied that the envelope belonged to respondent Ceccolini, and that he had instructed her to give it to someone.</p>
<p>The next day, Officer Biro mentioned his discovery to North Tarrytown detectives who in turn told Lance Emory, an FBI agent. This very ordinary incident in the lives of Biro and Hennessey requires us, over three years later, to decide whether Hennessey's testimony against respondent Ceccolini should have been suppressed in his trial for perjury. Respondent was charged with that offense because he denied that he knew anything of, or was in any way involved with, gambling operations. Respondent was found guilty after a bench trial in the United States District Court for the Southern District of New York, but immediately after the finding of guilt the District Court granted respondent's motion to "suppress" the testimony of Hennessey because the court concluded that the testimony was a "fruit of the poisonous tree"; assuming respondent's motion for a directed verdict included a motion to set aside the verdict of guilty, the District Court granted the motion because it concluded that without Hennessey's testimony there was insufficient evidence of respondent's guilt. The Government appealed these rulings to the Court of Appeals for the Second Circuit.</p>
<p>That court rightly concluded that the Government was entitled to appeal both the order granting the motion to suppress and the order setting aside the verdict of guilty, since <span class="star-pagination">*271</span> further proceedings if the Government were successful on the appeal would not be barred by the Double Jeopardy Clause.<sup>[1]</sup> <span class="citation" data-id="9463108"><a href="/opinion/339153/united-states-v-ralph-ceccolini/#139" aria-description="Citation for case: United States v. Ralph Ceccolini">542 F. 2d 136, 139-140</a></span> (1976). The District Court had sensibly first made its finding on the factual question of guilt or innocence, and then ruled on the motion to suppress; a reversal of these rulings would require no further proceedings in the District Court, but merely a reinstatement of the finding of guilt. <i>United States</i> v. <i>Morrison,</i> <span class="citation" data-id="109546"><a href="/opinion/109546/united-states-v-morrison/" aria-description="Citation for case: United States v. Morrison">429 U. S. 1</a></span> (1976); <i>United States</i> v. <i>Wilson,</i> <span class="citation" data-id="9426008"><a href="/opinion/109200/united-states-v-wilson/#352" aria-description="Citation for case: United States v. Wilson">420 U. S. 332, 352-353</a></span> (1975).</p>
<p>The Government, however, was not successful on the merits of its appeal; the Court of Appeals by a divided vote affirmed the District Court's suppression ruling. <span class="citation" data-id="9463108"><a href="/opinion/339153/united-states-v-ralph-ceccolini/#140" aria-description="Citation for case: United States v. Ralph Ceccolini">542 F. 2d, at 140-142</a></span>. We granted certiorari to consider the correctness of this ruling of the Court of Appeals. <span class="citation" data-id="9005810"><a href="/opinion/9012845/rose-v-city-of-los-angeles/" aria-description="Citation for case: Rose v. City of Los Angeles">431 U. S. 903</a></span> (1977).</p>
<p></p>
<h2>I</h2>
<p>During the latter part of 1973, the Federal Bureau of Investigation was exploring suspected gambling operations in North Tarrytown. Among the establishments under surveillance was respondent's place of business, which was a frequent and regular stop of one Francis Millow, himself a suspect in the investigation. While the investigation continued on a reduced scale after December 1973,<sup>[2]</sup> surveillance of the flower <span class="star-pagination">*272</span> shop was curtailed at that time. It was thus a full year after this discontinuance of FBI surveillance that Biro spent his patrol break behind the counter with Hennessey. When Biro's discovery of the policy slips was reported the following day to Emory, Emory was not fully informed of the manner in which Biro had obtained the information. Four months later, Emory interviewed Hennessey at her home for about half an hour in the presence of her mother and two sisters. He identified himself, indicated that he had learned through the local police department that she worked for respondent, and told her that the Government would appreciate any information regarding respondent's activities that she had acquired in the shop. Emory did not specifically refer to the incident involving Officer Biro. Hennessey told Emory that she was studying police science in college and would be willing to help. She then related the events which had occurred during her visit with Officer Biro.</p>
<p>In May 1975, respondent was summoned before a federal grand jury where he testified that he had never taken policy bets for Francis Millow at the flower shop. The next week Hennessey testified to the contrary, and shortly thereafter respondent was indicted for perjury.<sup>[3]</sup> Respondent waived a jury, and with the consent of all parties the District Court considered simultaneously with the trial on the merits respondent's motion to suppress both the policy slips and the testimony of Hennessey. At the conclusion of the evidence, the District Court excluded from its consideration "the envelope and the contents of the envelope," but nonetheless found respondent guilty of the offense charged. The court then, as previously <span class="star-pagination">*273</span> described, granted respondent's motion to suppress the testimony of Hennessey, because she "first came directly to the attention of the government as a result of an illegal search" and the Government had not "sustained its burden of showing that Lois Henness[e]y's testimony definitely would have been obtained without the illegal search." App. to Pet. for Cert. 28a-29a.</p>
<p>The Court of Appeals affirmed this ruling on the Government's appeal, reasoning that "the road to Miss Henness[e]y's testimony from Officer Biro's concededly unconstitutional search is both straight and uninterrupted." <span class="citation" data-id="9463108"><a href="/opinion/339153/united-states-v-ralph-ceccolini/#142" aria-description="Citation for case: United States v. Ralph Ceccolini">542 F. 2d, at 142</a></span>. The Court of Appeals also concluded that there was support in the record for the District Court's finding that the ongoing investigation would not have inevitably led to the evidence in question without Biro's discovery of the two policy slips. <span class="citation" data-id="9463108"><a href="/opinion/339153/united-states-v-ralph-ceccolini/#141" aria-description="Citation for case: United States v. Ralph Ceccolini"><i>Id.,</i> at 141</a></span>. Because of our traditional deference to the "two court rule," <i>Graver Mfg. Co.</i> v. <i>Linde Co.,</i> <span class="citation" data-id="104637"><a href="/opinion/104637/graver-tank-mfg-co-v-linde-air-products-co/#275" aria-description="Citation for case: Graver Tank &amp; Mfg. Co. v. Linde Air Products Co.">336 U. S. 271, 275</a></span> (1949), and the fact that the Government has not sought review of this latter ruling, we leave undisturbed this part of the Court of Appeals' decision. Because we decide that the Court of Appeals was wrong in concluding that there was insufficient attenuation between Officer Biro's search and Hennessey's testimony at the trial, we also do not reach the Government's contention that the exclusionary rule should not be applied when the evidence derived from the search is being used to prove a subsequent crime such as perjury.</p>
<p></p>
<h2>II</h2>
<p>The "road" to which the Court of Appeals analogized the train of events from Biro's discovery of the policy slips to Hennessey's testimony at respondent's trial for perjury is one of literally thousands of such roads traveled periodically between an original investigative discovery and the ultimate trial of the accused. The constitutional question under the Fourth Amendment was phrased in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), as whether "the connection <span class="star-pagination">*274</span> between the lawless conduct of the police and the discovery of the challenged evidence has `become so attenuated as to dissipate the taint.'" <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 487, 491</a></span>. The question was in turn derived from the Court's earlier decision in <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939), where Mr. Justice Frankfurter stated for the Court:</p>
<blockquote>"Here, as in the <i>Silverthorne</i> case [<i>Silverthorne Lumber Co.</i> v. <i>United States</i>], the facts improperly obtained do not `become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it' simply because it is used derivatively. <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>.</blockquote>
<blockquote>"In practice this generalized statement may conceal concrete complexities. Sophisticated argument may prove a causal connection between information obtained through illicit wire-tapping and the Government's proof. As a matter of good sense, however, such connection may have become so attenuated as to dissipate the taint."</blockquote>
<p>This, of course, makes it perfectly clear, if indeed ever there was any doubt about the matter, that the question of causal connection in this setting, as in so many other questions with which the law concerns itself, is not to be determined solely through the sort of analysis which would be applicable in the physical sciences. The issue cannot be decided on the basis of causation in the logical sense alone, but necessarily includes other elements as well. And our cases subsequent to <i><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">Nardone, supra,</a></span></i> have laid out the fundamental tenets of the exclusionary rule, from which the elements that are relevant to the causal inquiry can be divined.</p>
<p>An examination of these cases leads us to reject the Government's suggestion that we adopt what would in practice amount to a <i>per se</i> rule that the testimony of a live witness should not be excluded at trial no matter how close and proximate <span class="star-pagination">*275</span> the connection between it and a violation of the Fourth Amendment. We also reaffirm the holding of <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States"><i>Wong Sun, supra,</i> at 485</a></span>, that "verbal evidence which derives so immediately from an unlawful entry and an unauthorized arrest as the officers' action in the present case is no less the `fruit' of official illegality than the more common tangible fruits of the unwarranted intrusion." We are of the view, however, that cases decided since <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> significantly qualify its further observation that "the policies underlying the exclusionary rule [do not] invite any logical distinction between physical and verbal evidence." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>. Rather, at least in a case such as this, where not only was the alleged "fruit of the poisonous tree" the testimony of a live witness, but unlike <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> the witness was not a putative defendant, an examination of our cases persuades us that the Court of Appeals was simply wrong in concluding that if the road were uninterrupted, its length was immaterial. Its length, we hold, <i>is</i> material, as are certain other factors enumerated below to which the court gave insufficient weight.</p>
<p>In <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976), we observed that "despite the broad deterrent purpose of the exclusionary rule, it has never been interpreted to proscribe the introduction of illegally seized evidence in all proceedings or against all persons." Recognizing not only the benefits but the costs, which are often substantial, of the exclusionary rule, we have said that "application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served," <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). In that case, we refused to require that illegally seized evidence be excluded from presentation to a grand jury. We have likewise declined to prohibit the use of such evidence for the purpose of impeaching a defendant who testifies in his own behalf. <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954).</p>
<p>We have limited the standing requirement in the exclusionary rule context because the "additional benefits of extending <span class="star-pagination">*276</span> the . . . rule" to persons other than the ones subject to the illegal search are outweighed by the "further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth." <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174-175</a></span> (1969). Even in situations where the exclusionary rule is plainly applicable, we have declined to adopt a "<i>per se</i> or `but for' rule" that would make inadmissible any evidence, whether tangible or live-witness testimony, which somehow came to light through a chain of causation that began with an illegal arrest. <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 603</a></span> (1975).</p>
<p>Evaluating the standards for application of the exclusionary rule to live-witness testimony in light of this balance, we are first impelled to conclude that the degree of free will exercised by the witness is not irrelevant in determining the extent to which the basic purpose of the exclusionary rule will be advanced by its application. This is certainly true when the challenged statements are made by a putative defendant after arrest, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States"><i>Wong Sun, supra,</i> at 491</a></span>; <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra</a></span></i><i>,</i> and <i>a fortiori</i> is true of testimony given by nondefendants.</p>
<p>The greater the willingness of the witness to freely testify, the greater the likelihood that he or she will be discovered by legal means and, concomitantly, the smaller the incentive to conduct an illegal search to discover the witness.<sup>[4]</sup> Witnesses are not like guns or documents which remain hidden from view until one turns over a sofa or opens a filing cabinet. Witnesses can, and often do, come forward and offer evidence entirely of their own volition. And evaluated properly, the degree of free will necessary to dissipate the taint will very likely be found more often in the case of live-witness testimony <span class="star-pagination">*277</span> than other kinds of evidence. The time, place and manner of the initial questioning of the witness may be such that any statements are truly the product of detached reflection and a desire to be cooperative on the part of the witness. And the illegality which led to the discovery of the witness very often will not play any meaningful part in the witness' willingness to testify.</p>
<blockquote>"The proffer of a living witness is not to be mechanically equated with the proffer of inanimate evidentiary objects illegally seized. The fact that the name of a potential witness is disclosed to police is of no evidentiary significance, per se, since the living witness is an individual human personality whose attributes of will, perception, memory and volition interact to determine what testimony he will give. The uniqueness of this human process distinguishes the evidentiary character of a witness from the relative immutability of inanimate evidence." <i>Smith</i> v. <i>United States,</i> 117 U. S. App. D. C. 1, 3-4, <span class="citation" data-id="9449714"><a href="/opinion/262430/wilson-m-smith-jr-v-united-states-of-america-raymond-bowden-v-united/#881" aria-description="Citation for case: Wilson M. Smith, Jr. v. United States of America, Raymond...">324 F. 2d 879, 881-882</a></span> (1963) (Burger, J.) (footnotes omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/954/">377 U. S. 954</a></span> (1964).</blockquote>
<p>Another factor which not only is relevant in determining the usefulness of the exclusionary rule in a particular context, but also seems to us to differentiate the testimony of all live witnesseseven putative defendantsfrom the exclusion of the typical documentary evidence, is that such exclusion would perpetually disable a witness from testifying about relevant and material facts, regardless of how unrelated such testimony might be to the purpose of the originally illegal search or the evidence discovered thereby. Rules which disqualify knowledgeable witnesses from testifying at trial are, in the words of Professor McCormick, "serious obstructions to the ascertainment of truth"; accordingly, "[f]or a century the course of legal evolution has been in the direction of sweeping away these obstructions." C. McCormick, Law of Evidence § 71 (1954). Alluding to the enormous cost engendered by <span class="star-pagination">*278</span> such a permanent disability in an analogous context, we have specifically refused to hold that "making a confession under circumstances which preclude its use, perpetually disables the confessor from making a usable one after those conditions have been removed." <i>United States</i> v. <i>Bayer,</i> <span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/#541" aria-description="Citation for case: United States v. Bayer">331 U. S. 532, 541</a></span> (1947). For many of these same reasons, the Court has also held admissible at trial testimony of a witness whose identity was disclosed by the defendant's statement given after inadequate <i>Miranda</i> warnings. <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#450" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 450-451</a></span> (1974).</p>
<blockquote>"For, when balancing the interests involved, we must weigh the strong interest under any system of justice of making available to the trier of fact all concededly relevant and trustworthy evidence which either party seeks to adduce. . . . Here respondent's own statement, which might have helped the prosecution show respondent's guilty conscience at trial, had already been excised from the prosecution's case pursuant to this Court's <i>Johnson</i> [v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966)] decision. To extend the excision further under the circumstances of this case and exclude relevant testimony of a third-party witness would require far more persuasive arguments than those advanced by respondent."</blockquote>
<p>In short, since the cost of excluding live-witness testimony often will be greater, a closer, more direct link between the illegality and that kind of testimony is required.</p>
<p>This is not to say, of course, that live-witness testimony is always or even usually more reliable or dependable than inanimate evidence. Indeed, just the opposite may be true. But a determination that the discovery of certain evidence is sufficiently unrelated to or independent of the constitutional violation to permit its introduction at trial is not a determination which rests on the comparative reliability of that evidence. Attenuation analysis, appropriately concerned with the differences between live-witness testimony and inanimate evidence, <span class="star-pagination">*279</span> can consistently focus on the factors enumerated above with respect to the former, but on different factors with respect to the latter.</p>
<p>In holding that considerations relating to the exclusionary rule and the constitutional principles which it is designed to protect must play a factor in the attenuation analysis, we do no more than reaffirm an observation made by this Court half a century ago:</p>
<blockquote>"A criminal prosecution is more than a game in which the Government may be checkmated and the game lost merely because its officers have not played according to rule." <i>McGuire</i> v. <i>United States,</i> <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/#99" aria-description="Citation for case: McGuire v. United States">273 U. S. 95, 99</a></span> (1927).</blockquote>
<p>The penalties visited upon the Government, and in turn upon the public, because its officers have violated the law must bear some relation to the purposes which the law is to serve.</p>
<p></p>
<h2>III</h2>
<p>Viewing this case in the light of the principles just discussed, we hold that the Court of Appeals erred in holding that the degree of attenuation was not sufficient to dissipate the connection between the illegality and the testimony. The evidence indicates overwhelmingly that the testimony given by the witness was an act of her own free will in no way coerced or even induced by official authority as a result of Biro's discovery of the policy slips. Nor were the slips themselves used in questioning Hennessey. Substantial periods of time elapsed between the time of the illegal search and the initial contact with the witness, on the one hand, and between the latter and the testimony at trial on the other. While the particular knowledge to which Hennessey testified at trial can be logically traced back to Biro's discovery of the policy slips, both the identity of Hennessey and her relationship with the respondent were well known to those investigating the case. There is, in addition, not the slightest evidence to suggest <span class="star-pagination">*280</span> that Biro entered the shop or picked up the envelope with the intent of finding tangible evidence bearing on an illicit gambling operation, much less any suggestion that he entered the shop and searched with the intent of finding a willing and knowledgeable witness to testify against respondent. Application of the exclusionary rule in this situation could not have the slightest deterrent effect on the behavior of an officer such as Biro. The cost of permanently silencing Hennessey is too great for an evenhanded system of law enforcement to bear in order to secure such a speculative and very likely negligible deterrent effect.</p>
<p>Obviously no mathematical weight can be assigned to any of the factors which we have discussed, but just as obviously they all point to the conclusion that the exclusionary rule should be invoked with much greater reluctance where the claim is based on a causal relationship between a constitutional violation and the discovery of a live witness than when a similar claim is advanced to support suppression of an inanimate object. The judgment of the Court of Appeals is accordingly</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE BLACKMUN took no part in the consideration or decision of this case.</p>
<p>MR. CHIEF JUSTICE BURGER, concurring in the judgment.</p>
<p>I agree with the Court's ultimate conclusion that there is a fundamental difference, for purposes of the exclusionary rule, between live-witness testimony and other types of evidence. I perceive this distinction to be so fundamental, however, that I would not prevent a factfinder from hearing and considering the relevant statements of any witness, except perhaps under the most remarkable of circumstancesalthough none such have ever been postulated that would lead me to exclude the testimony of a live witness.</p>
<p><span class="star-pagination">*281</span> To appreciate this position, it is essential to bear in mind the purported justification for employing the exclusionary rule in a Fourth Amendment context: deterrence of official misconduct. See <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976); <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 458-459, n. 35</a></span> (1976). As an abstract intellectual proposition this can be buttressed by a plausible rationale since there is at least some comprehensible connectionalbeit largely and dubiously speculativebetween the exclusion of evidence and the deterrence of intentional illegality on the part of a police officer.<sup>[1]</sup> But if that is the purpose of the rule, it seems to me that the appropriate inquiry in every case in which a defendant seeks the exclusion of otherwise admissible and reliable evidence is whether official conduct in reality will be measurably altered by taking such a course.</p>
<p>On the facts of this case the Court is, of course, correct in holding that the "[a]pplication of the exclusionary rule in this situation could not have the slightest deterrent effect on the behavior of an officer such as Biro." <i>Ante,</i> at 280. Reaching this result, however, requires no judicial excursion into an area about which "philosophers have been able to argue endlessly,"<sup>[2]</sup> namely, the degree of "free will" exercised by a person when engaging in an act such as speaking.</p>
<p>In the history of ideas many thinkers have maintained with persuasion that there is no such thing as "free will," in the sense that the term implies the independent ability of an actor to regulate his or her conduct. Others have steadfastly maintained the opposite, arguing that the human personality is one innately free to choose among alternatives. Still a third group <span class="star-pagination">*282</span> would deny that the very term "free will" has coherent meaning. These are only a few of the many perspectives on a subject which lies at the core of our intellectual and religious heritage. While this ancient debate will undoubtedly continue, "society and the law have no choice in the matter. We must proceed . . . on the scientifically unprovable assumption that human beings make choices in the regulation of their conduct and that they are influenced by society's standards as well as by personal standards." <i>Blocker</i> v. <i>United States,</i> 110 U. S. App. D. C. 41, 53, <span class="citation" data-id="9447847"><a href="/opinion/253629/comer-blocker-v-united-states/#865" aria-description="Citation for case: Comer Blocker v. United States">288 F. 2d 853, 865</a></span> (1961) (Burger, J., concurring in result). Mr. Justice Jackson expressed this in <i>Gregg Cartage &amp; Storage Co.</i> v. <i>United States,</i> <span class="citation" data-id="9419241"><a href="/opinion/103657/gregg-cartage-storage-co-v-united-states/#80" aria-description="Citation for case: Gregg Cartage &amp; Storage Co. v. United States">316 U. S. 74, 80</a></span> (1942): "[T]he practical business of government and administration of the law is obliged to proceed on more or less rough and ready judgments based on the assumption that mature and rational persons are in control of their own conduct." And in <i>Steward Machine Co.</i> v. <i>Davis,</i> <span class="citation" data-id="9418925"><a href="/opinion/102843/steward-machine-co-v-davis/#590" aria-description="Citation for case: Steward MacHine Co. v. Davis">301 U. S. 548, 590</a></span> (1937), Mr. Justice Cardozo put it thus: "Till now the law has been guided by a robust common sense which assumes the freedom of the will as a working hypothesis in the solution of its problems."</p>
<p>We are nonetheless cognizant of the fact that this assumption must continually confront the inherent practical obstacle of one person's being unable to know with certainty the content of another's mind. We cross this barrier daily, of course, in the process of determining criminal culpability.<sup>[3]</sup> Yet in criminal trials we are willing to bear the risk of errorsubstantially diminished by the requirement of proof beyond a reasonable doubtin order to effectuate the common-law tradition of <span class="star-pagination">*283</span> imposing punishment only upon those who can be said to be morally responsible for their acts. There is no analogue to this concern, however, in the area of Fourth Amendment exclusion, which has an admitted pragmatic purposebased as I suggested on speculative hypotheses which ought to lead us to apply it with reasoned discrimination, not as an automatic response. In short, the results achieved from current exclusionary rule standards are bizarre enough without steering the analysis in the direction of areas which offer no reasonable hope of a comprehensible framework for inquiry.</p>
<p>It would be obvious nonsense to postulate that during his brief encounter in the florist shop Officer Biro was making a painstaking analysis of the extent to which Lois Hennessey's "free will" would affect her disposition to testify against respondent at some future point. It is one thing to engage in scholastic hindsight, particularly as the dissent has done here, in which speculation proceeds from unfounded hypotheses as to the <i>probable</i> explanations for the decision of a live witness to come forward and testify. But it is quite another to suppose that the police officer, assuming he is contemplating illegal action, will, or would be able to, engage in a similar inquiry.</p>
<p>There are several reasons which support this analysis, which, I might add, is found acceptable in every other legal system in the world. Initially, I would point out that the concept of effective deterrence assumes that the police officer consciously realizes the probable consequences of a presumably impermissible course of conduct. The officer must be cognizant of at least the possibility that his actionsbecause of possible suppressionwill undermine the chances of convicting a known criminal. I strongly suspect that in the vast majority of instances in this setting the officer accused of a Fourth Amendment violation will not be even remotely aware of the existence of a witness, as for example, where seizure of an item of evidence guides official inquiry to an eyewitness. <span class="star-pagination">*284</span> Of course, an officer conducting a search later held illegal may have some hope that his inquiry will lead to persons who can come forward with testimony. It is not plausible, however, that a police officer would consciously engage in illegal action simply to gain access to a witness, knowing full well that under prevailing legal doctrine the result will be the certain exclusion of whatever tangible evidence might be found.<sup>[4]</sup></p>
<p>Even if we suppose that the officer suspects that his illegal actions will produce a lead to a witness, he faces the intractable problem of understanding how valuable that person will be to his investigation. As one philosopher has aptly stated the matter, "[t]he freedom of the will consists in the impossibility of knowing actions that still lie in the future." L. Wittgenstein, Tractatus Logico-Philosophicus ¶ 5.1362 (Pears &amp; McGuinness trans. 1961). In <i>Smith</i> v. <i>United States,</i> 117 U. S. App. D. C. 1, 3-4, <span class="citation" data-id="9449714"><a href="/opinion/262430/wilson-m-smith-jr-v-united-states-of-america-raymond-bowden-v-united/#881" aria-description="Citation for case: Wilson M. Smith, Jr. v. United States of America, Raymond...">324 F. 2d 879, 881-882</a></span> (1963), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/954/">377 U. S. 954</a></span> (1964), this point was applied to the case of a live witness testifying under oath:</p>
<blockquote>"The proffer of a living witness is not to be mechanically equated with the proffer of inanimate evidentiary objects illegally seized. The fact that the name of a potential witness is disclosed to police is of no evidentiary significance, per se, since the living witness is an individual human personality whose attributes of will, perception, memory and volition interact to determine what <span class="star-pagination">*285</span> testimony he will give. The uniqueness of this human process distinguishes the evidentiary character of a [living] <i>witness</i> from the relative immutability of inanimate evidence." (Emphasis added.) (Footnotes omitted.)</blockquote>
<p>It can, of course, be argued, that the prospect of finding a helpful witness may play <i>some</i> role in a policeman's decision to be indifferent about Fourth Amendment procedures. The answer to this point, however, is that we have never insisted on employing the exclusionary rule whenever there is some possibility, no matter how remote, of deterring police misconduct. Rather, we balance the cost to society of losing perfectly competent evidence against the prospect of incrementally enhancing Fourth Amendment values. See, <i>e. g., </i><i>Stone,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S., at 486</a></span>; <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#350" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 350-351</a></span> (1974); <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174-175</a></span> (1969).</p>
<p>Using this approach it strikes me as evident that the permanent silencing of a witnesswho, after all, is appearing under oathis not worth the high price the exclusionary rule exacts. Any rule of law which operates to keep an eyewitness to a crimea murder, for examplefrom telling the jury what that person saw has a rational basis roughly comparable to the primitive rituals of human sacrifice.</p>
<p>I would, therefore, resolve the case of a living witness on a <i>per se</i> basis, holding that such testimony is always admissible, provided it meets all other traditional evidentiary requirements. At very least this solution would alleviate the burden now squarely thrust upon courtsof determining in each instance whether the witness possessed that elusive quality characterized by the term "free will."</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>While "reaffirm[ing]" the holding of <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 485</a></span> (1963), that verbal evidence, like <span class="star-pagination">*286</span> physical evidence, may be "fruit of the poisonous tree," the Court today "significantly qualif[ies]" <i>Wong Sun'</i>s further conclusion, <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States"><i>id.,</i> at 486</a></span>, that no "`logical distinction'" can be drawn between verbal and physical evidence for purposes of the exclusionary rule. <i>Ante,</i> at 275. In my view, the distinction that the Court attempts to draw cannot withstand close analysis. To extend "a time-worn metaphor," <i>Harrison</i> v. <i>United States,</i> <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/#222" aria-description="Citation for case: Harrison v. United States">392 U. S. 219, 222</a></span> (1968), I do not believe that the same tree, having its roots in an unconstitutional search or seizure, can bear two different kinds of fruit, with one kind less susceptible than the other of exclusion on Fourth Amendment grounds. I therefore dissent.</p>
<p>The Court correctly states the question before us: whether the connection between the police officer's concededly unconstitutional search and Hennessey's disputed testimony was "so attenuated as to dissipate the taint," <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939). See <i>ante,</i> at 274. In resolving questions of attenuation, courts typically scrutinize the facts of the individual case, with particular attention to such matters as the "temporal proximity" of the official illegality and the discovery of the evidence, "the presence of intervening circumstances," and "the purpose and flagrancy of the official misconduct." <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 603-604</a></span> (1975). The Court retains this general framework, but states that "[a]ttenuation analysis" should be "concerned with the differences between live-witness testimony and inanimate evidence." <i>Ante,</i> at 278-279. The differences noted by the Court, however, have to a large extent already been accommodated by current doctrine. Where they have not been so accommodated, it is because the differences asserted are either illusory or of no relevance to the issue of attenuation.</p>
<p>One difference mentioned by the Court is that witnesses, unlike inanimate objects, "can, and often do, come forward and offer evidence entirely of their own volition." <i>Ante,</i> at 276. Recognition of this obvious fact does nothing to advance <span class="star-pagination">*287</span> the attenuation inquiry. We long ago held that, if knowledge of evidence is gained from a source independent of police illegality, the evidence should be admitted. <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920) (Holmes, J.). This "independent source" rule would plainly apply to a witness whose identity is discovered in an illegal search but who later comes to the police for reasons unrelated to the official misconduct. In the instant case, however, as the Court recognizes, <i>ante,</i> at 273, there is a "`straight and uninterrupted'" road between the illegal search and the disputed testimony.</p>
<p>Even where the road is uninterrupted, in some cases the Government may be able to show that the illegally discovered evidence would inevitably have come to light in the normal course of a legal police investigation. Assuming such evidence is admissiblea proposition that has been questioned, <i>Fitzpatrick</i> v. <i>New York,</i> <span class="citation" data-id="9425580"><a href="/opinion/108949/fitzpatrick-v-new-york/" aria-description="Citation for case: Fitzpatrick v. New York">414 U. S. 1050</a></span> (1973) (WHITE, J., dissenting from denial of certiorari)this "inevitable discovery" rule would apply to admit the testimony of a witness who, in the absence of police misconduct, would have come forward "entirely of [his or her] own volition." Again, however, no such situation is presented by this case, since the Court accepts the findings of the two lower courts that Hennessey's testimony would not inevitably have been discovered. <i>Ante,</i> at 273.</p>
<p>Both the independent-source and inevitable-discovery rules, moreover, can apply to physical evidence as well as to verbal evidence. The police may show, for example, that they learned from an independent source, or would inevitably have discovered through legal means, the location of an object that they also knew about as a result of illegal police activity. It may be that verbal evidence is more likely to have an independent source, because live witnesses can indeed come forward of their own volition, but this simply underscores the degree to which the Court's approach involves a form of judicial "double counting." The Court would apparently first <span class="star-pagination">*288</span> determine whether the evidence stemmed from an independent source or would inevitably have been discovered; if neither of these rules was found to apply, as here, the Court would still somehow take into account the fact that, as a general proposition (but not in the particular case), witnesses sometimes do come forward of their own volition.</p>
<p>The Court makes a related point that "[t]he greater the willingness of the witness to freely testify, . . . the smaller the incentive to conduct an illegal search to discover the witness." <i>Ante,</i> at 276. The somewhat incredible premise of this statement is that the police in fact refrain from illegal behavior in which they would otherwise engage because they know in advance both that a witness will be willing to testify and that he or she "will be discovered by legal means." <i><span class="citation" data-id="9425580"><a href="/opinion/108949/fitzpatrick-v-new-york/" aria-description="Citation for case: Fitzpatrick v. New York">Ibid.</a></span></i> This reasoning surely reverses the normal sequence of events; the instances must be very few in which a witness' willingness to testify is known before he or she is discovered. In this case, for example, the police did not even know that Hennessey was a potentially valuable witness, much less whether she would be willing to testify, prior to conducting the illegal search. See <i>ante,</i> at 279-280. When the police are certain that a witness "will be discovered by legal means," <i>ante,</i> at 276if they ever can be certain about such a factthey of course have no incentive to find him or her by illegal means, but the same can be said about physical objects that the police know will be discovered legally.</p>
<p>The only other point made by the Court is that exclusion of testimony "perpetually disable[s] a witness from testifying about relevant and material facts." <i>Ante,</i> at 277. The "perpetual. . . disable[ment]" of which the Court speaks, however, applies as much to physical as to verbal evidence. When excluded, both types of evidence are lost for the duration of the particular trial, despite their being "relevant and material. . . [and] unrelated . . . to the purpose of the originally <span class="star-pagination">*289</span> illegal search." <i><span class="citation" data-id="9425580"><a href="/opinion/108949/fitzpatrick-v-new-york/" aria-description="Citation for case: Fitzpatrick v. New York">Ibid.</a></span></i> Moreover, while it is true that "often" the exclusion of testimony will be very costly to society, <i>ante,</i> at 278, at least as often the exclusion of physical evidence such as heroin in a narcotics possession case or business records in a tax casewill be as costly to the same societal interests. But other, more important societal interests, see <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#599" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 599-600</a></span>; <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>, have led to the rule, which the Court today reaffirms, that "fruits of the poisonous tree" must be excluded despite their probative value, unless the facts of the case justify a finding of sufficient attenuation.</p>
<p>The facts of this case do not justify such a finding. Although, as the Court notes, <i>ante,</i> at 272; see <i>ante,</i> at 279, four months elapsed between the illegal search and the FBI's first contact with Hennessey, the critical evidence was provided at the time and place of the search, when the police officer questioned Hennessey and she identified respondent, <i>ante,</i> at 270. The time that elapsed thereafter is of no more relevance than would be a similar time period between the discovery of an object during an illegal search and its later introduction into evidence at trial. In this case, moreover, there were no intervening circumstances between Hennessey's statement at the time of the search and her later testimony. She did not come to the authorities and ask to testify, despite being a student of police science; an FBI agent had to go to her home and interrogate her. <i>Ante,</i> at 272.</p>
<p>Finally, whatever the police officer's purpose in the flower shop on the day of the search, the search itself was not even of arguable legality, as was conceded by the Government below. <span class="citation" data-id="9463108"><a href="/opinion/339153/united-states-v-ralph-ceccolini/" aria-description="Citation for case: United States v. Ralph Ceccolini">542 F. 2d 136</a></span>, 140 n. 5 (CA2 1976). It is also undisputed that the shop had been under surveillance as part of an ongoing gambling investigation in which the local police force had actively participated; its participation included interception of at least one of respondent's telephone conversations <span class="star-pagination">*290</span> in the very month of the search. <i>Ante,</i> at 271-272, and n. 2. Under all of the circumstances, the connection here between the official illegality and the disputed testimony cannot be deemed "so attenuated as to dissipate the taint." The District Court therefore properly excluded the testimony.</p>
<p>I would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[1]  Appeal from the suppression order is, of course, authorized by the clear language of <span class="citation no-link">18 U. S. C. § 3731</span> (1976 ed.). That section permits "[a]n appeal by the United States . . . from a decision or order of a district courts [<i>sic</i>] suppressing or excluding evidence . . . , not made after the defendant has been put in jeopardy and before the verdict or finding on an indictment or information . . . ." If Congress had intended only pretrial suppression orders to be appealable, it would not have added the phrase "and before the verdict or finding on an indictment or information."</p>
<p>[2]  The extent of the continued investigation is not made clear on the record but we do know at least that on December 3, 1974, a telephone conversation between Millow and Ceccolini, which implicated the latter in a policy betting operation, was intercepted by local police participating in a combined federal-state gambling investigation.</p>
<p>[3]  Respondent was also indicted on a second count which charged that he had knowingly made a false statement when he testified that he did not know Hank Bucci was involved in gambling operations. The judge found respondent not guilty on this count, however, because "although there is evidence to support this charge the government has not met its burden of proof beyond a reasonable doubt." App. to Pet. for Cert. 28a.</p>
<p>[4]  Of course, the analysis might be different where the search was conducted by the police for the specific purpose of discovering potential witnesses.</p>
<p>[1]  Empirically speaking, though, I have the gravest doubts as to whether the exclusion of evidence, in and of itself, has any direct appreciable effect on a policeman's behavior in most situationsemergency actions in particular. See <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#416" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 416-417, 426-427</a></span> (1971) (BURGER, C. J., dissenting).</p>
<p>[2]  J. Sartre, Being and Nothingness 433 (Barnes trans. 1956).</p>
<p>[3]  A somewhat similar hurdle is presented in civil cases, which may rest decision on the standard of a "reasonable man's" actions. In those circumstances we assume that a person is ordinarily capable of conforming conduct to an objective standard of reasonableness. Consequently, while the <i>assumption</i> is indulged that the person possesses control over his actions, there is generally no need to inquire into mental processes as such.</p>
<p>[4]  Perhaps a case might arise in which the police conducted a search only for the purpose of obtaining the names of witnesses. In such a circumstance it is possibly arguable that the exclusion of any testimony gained as a result of the search would have an effect on official behavior. This clearly did not occur here, nor can I conceive of many instances in which it would. In any event, the decision to exclude such testimony should depend on the <i>officers'</i> motivation and not on the "free will" of the witnesses. I would not want to speculate, however, as to whether such an unlikely case would justify modifying a <i>per se</i> approach to this general problem.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Chadwick.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Chadwick"
type: case
citation: "433 U.S. 1 (1977)"
parallel_cite: "97 S. Ct. 2476; 53 L. Ed. 2d 538"
neutral_cite: 1977 U.S. LEXIS 133
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-21
docket: 75-1721
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1977-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Chadwick
  varies_by_point: true
  scope_note: "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
  point_overrides:
    - point: legacy-limited-united-states-v-chadwick
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: California v. Acevedo
          cluster_id: 112608
          cite: 500 U.S. 565
          field_ii: limited
      scope_note: "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/"
  cluster_id: 109714
  opinion_id: 9426913
  identity_checked: true
homes:
  - page: "[[Searching Effects and Containers]]"
    role: "Key — Anchor"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
  - page: "[[Automobile Exception]]"
    role: "Related (limited by Acevedo for a container in a car)"
related: ["[[California v. Acevedo]]", "[[United States v. Ross]]", "[[Chambers v. Maroney]]", "[[Chimel v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "containers", "luggage", "search-incident-to-arrest", "warrant-requirement"]
holding: "Luggage/containers carry a high expectation of privacy; once seized and reduced to exclusive police control with no exigency, a footlocker may not be searched without a warrant, and the search is not incident to arrest."
lake:
  record_id: United States v. Chadwick
  status: verified
  projected_at: 2026-07-09
---

# United States v. Chadwick

*433 U.S. 1 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents had probable cause to believe a 200-pound double-locked footlocker shipped by train contained marijuana. After Chadwick and his confederates picked it up and loaded it into the trunk of a waiting car, agents arrested them and seized the footlocker. More than an hour later, at the federal building and with the footlocker under the agents' exclusive control, they opened and searched it without a warrant and found the marijuana.

## Issue
Whether federal agents who have lawfully seized a footlocker incident to arrest, and reduced it to their exclusive control, may search it without a warrant when no [[Exigent Circumstances and Hot Pursuit|exigency]] exists.

## Rule
No. Personal luggage carries a high expectation of privacy that the warrant requirement protects: "By placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination. . . . There being no exigency, it was unreasonable for the Government to conduct this search without the safeguards a judicial warrant provides." — 433 U.S. at 11. ^pin-11

The vehicle's diminished privacy does not extend to luggage: "a person's expectations of privacy in personal luggage are substantially greater than in an automobile." — *Id.* at 13. ^pin-13

Nor is the [[Search Incident to Arrest|search incident to arrest]] once the property is secured: "Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest." — [*Id.* at 15](https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/#:~:text=Once%20law%20enforcement%20officers%20have). ^pin-15

## Application
The footlocker's brief contact with Chadwick's car did not make this an automobile search, and its diminished-privacy rationale did not apply to luggage. Once agents seized the footlocker and moved it to the federal building under their exclusive control, there was no danger of removal or destruction of evidence, so no [[Exigent Circumstances and Hot Pursuit|exigency]] justified bypassing a magistrate; and because the search came more than an hour after the agents gained exclusive control and the arrestees were securely in custody, it could not be justified as incident to the arrest.

## Conclusion
The warrantless search was unreasonable; suppression was affirmed. The Warrant Clause draws the line at the point where seized property comes under the exclusive dominion of police authority and no [[Exigent Circumstances and Hot Pursuit|exigency]] is shown.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by** [[California v. Acevedo]] — Acevedo collapsed the *Chadwick*/*[[Arkansas v. Sanders]]* container distinction **in the automobile context**, holding that police with probable cause may search a container located in a vehicle without a warrant. *Chadwick*'s core teaching — that luggage and other personal effects reduced to exclusive police control with no [[Exigent Circumstances and Hot Pursuit|exigency]] require a warrant — remains the rule outside that auto-container setting.

## Appears on
- [[Automobile Exception]] — *Key — Limiting / Historical*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *United States v. Chadwick*, 433 U.S. 1 (1977) — https://www.courtlistener.com/opinion/109714/united-states-v-chadwick/ — pinpoints: 11, 13, 15.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0c38d862e92b4a7b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Chadwick"}, "payload": {"all": [{"cite": "433 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "433"}, {"cite": "97 S. Ct. 2476", "page": "2476", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "53 L. Ed. 2d 538", "page": "538", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "53"}, {"cite": "1977 U.S. LEXIS 133", "page": "133", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "433 U.S. 1", "official": {"cite": "433 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "433"}, "official_selection_present": true, "record_id": "United States v. Chadwick"}}
{"assertion_id": "0c3a77bbab0119ba", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-15", "record_id": "United States v. Chadwick"}, "payload": {"fragment": "#:~:text=Once%20law%20enforcement%20officers%20have", "page": null, "pin_id": "pin-15", "pinpoint_status": "star-verified", "quote": "Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest.", "quote_fidelity": "matched", "record_id": "United States v. Chadwick", "star_marker": "15"}}
{"assertion_id": "c08bc0e180bb8c80", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-13", "record_id": "United States v. Chadwick"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-13", "pinpoint_status": "slip-only", "quote": "a person's expectations of privacy in personal luggage are substantially greater than in an automobile.", "quote_fidelity": "mismatch", "record_id": "United States v. Chadwick", "star_marker": null}}
{"assertion_id": "f8ea14631c8c5d2d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-11", "record_id": "United States v. Chadwick"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-11", "pinpoint_status": "slip-only", "quote": "--- # United States v. Chadwick *433 U.S. 1 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents had probable cause to believe a 200-pound double-locked footlocker shipped by train contained marijuana. After Chadwick and his confederates picked it up and loaded it into the trunk of a waiting car, agents arrested them and seized the footlocker. More than an hour later, at the federal building and with the footlocker under the agents' exclusive control, they opened and searched it without a warrant and found the marijuana. ## Issue Whether federal agents who have lawfully seized a footlocker incident to arrest, and reduced it to their exclusive control, may search it without a warrant when no exigency exists. ## Rule No. Personal luggage carries a high expectation of privacy that the warrant requirement protects:", "quote_fidelity": "mismatch", "record_id": "United States v. Chadwick", "star_marker": null}}
{"assertion_id": "f14e5df1ec12f75e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Chadwick"}, "payload": {"as_of_content": "1977-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "United States v. Chadwick", "scope_note": "The Chadwick-Sanders distinction — that luggage/containers carry a high REP demanding a warrant even when connected to a car — was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting.", "varies_by_point": true}}
```

### lake record — United States v. Chadwick

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Chadwick",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Chadwick",
    "case_name_short": "Chadwick",
    "case_name_full": "UNITED STATES v. CHADWICK Et Al.",
    "input_case_name": "United States v. Chadwick",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-21",
    "year": 1977,
    "docket": "75-1721",
    "cluster_id": 109714,
    "lead_opinion_id": 9426913,
    "sibling_ids": [
      109714,
      9426913,
      9426914,
      9426915
    ],
    "absolute_url": "/opinion/109714/united-states-v-chadwick/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "433 U.S. 1",
      "volume": "433",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 2476",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 538",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 133",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "433 U.S. 1",
        "volume": "433",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2476",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 538",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 133",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "433 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "433 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-11",
      "page": null,
      "quote": "--- # United States v. Chadwick *433 U.S. 1 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents had probable cause to believe a 200-pound double-locked footlocker shipped by train contained marijuana. After Chadwick and his confederates picked it up and loaded it into the trunk of a waiting car, agents arrested them and seized the footlocker. More than an hour later, at the federal building and with the footlocker under the agents' exclusive control, they opened and searched it without a warrant and found the marijuana. ## Issue Whether federal agents who have lawfully seized a footlocker incident to arrest, and reduced it to their exclusive control, may search it without a warrant when no exigency exists. ## Rule No. Personal luggage carries a high expectation of privacy that the warrant requirement protects:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-13",
      "page": null,
      "quote": "a person's expectations of privacy in personal luggage are substantially greater than in an automobile.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-15",
      "page": null,
      "quote": "Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest.",
      "star_marker": "15",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28915,
      "fragment": "#:~:text=Once%20law%20enforcement%20officers%20have",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1977-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Chadwick",
    "varies_by_point": true,
    "scope_note": "The Chadwick-Sanders distinction \u2014 that luggage/containers carry a high REP demanding a warrant even when connected to a car \u2014 was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting.",
    "point_overrides": [
      {
        "point": "legacy-limited-united-states-v-chadwick",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "California v. Acevedo",
            "cluster_id": 112608,
            "cite": "500 U.S. 565",
            "field_ii": "limited"
          }
        ],
        "scope_note": "The Chadwick-Sanders distinction \u2014 that luggage/containers carry a high REP demanding a warrant even when connected to a car \u2014 was collapsed in the automobile context by California v. Acevedo, which lets police search a container in a vehicle on PC alone. Chadwick's core (property reduced to exclusive police control, no exigency, needs a warrant) survives outside the auto-container setting."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": "500 U.S. 565",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
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
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
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
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": [
            "58 L. Ed. 2d 387",
            "99 S. Ct. 421",
            "439 U.S. 128",
            "1978 U.S. LEXIS 2452"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Chadwick:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTk5ODM2ODAwMDAwJnM9MTM4NTc2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDImcz0xMTAxMDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
        "reviewed": 19,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 19,
        "triage_read": 0,
        "triage_snippet_classified": 19
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109714 OR 9426913 OR 9426914 OR 9426915)",
    "indexed_citing_opinions": 1642,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109714,
        "count": 1488,
        "count_source": "search"
      },
      {
        "opinion_id": 9426913,
        "count": 202,
        "count_source": "search"
      },
      {
        "opinion_id": 9426914,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426915,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2561,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-chadwick.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNTc4NjImcz05Mzk3NDYwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109714+OR+9426913+OR+9426914+OR+9426915%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109714,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 292608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 294420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 305845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 312363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 317229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 319326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 325005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 326798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 328838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 334451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 335388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 339773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109714,
        "cited_id": 340781,
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
    "date_created": "2026-07-05T23:06:52Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:07:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Chadwick

```
<opinion type="majority">
<author id="b31-5">MR. Chief Justice Burger</author>
<p id="Azh">delivered the opinion of the Court.</p>
<p id="b31-6">We granted certiorari in this case to decide whether a search warrant is required before federal agents may open a locked footlocker which they have lawfully seized at the time of the arrest of its owners, when there is probable cause to believe the footlocker contains contraband.</p>
<p id="b31-7">(1)</p>
<p id="b31-8">On May 8, 1973, Amtrak railroad officials in San Diego observed respondents Gregory Machado and Bridget Leary load a brown footlocker onto a train bound for Boston. Their suspicions were aroused when they noticed that the trunk was unusually heavy for its size, and that it was leaking talcum powder, a substance often used to mask the odor of marihuana or hashish. Because Machado matched a profile used to spot drug traffickers, the railroad officials reported these circumstances to federal agents in San Diego, who in turn relayed the information, together with detailed descriptions of Machado and the footlocker, to their counterparts in Boston.</p>
<p id="b31-9">When the train arrived in Boston two days later, federal narcotics agents were on hand. Though the officers had not obtained an arrest or search warrant, they had with them a police dog trained to detect marihuana. The agents identified Machado and Leary and kept them under surveillance as they claimed their suitcases and the footlocker, which had been <page-number citation-index="1" label="4">*4</page-number>transported by baggage cart from the train to the departure area. Machado and Leary lifted the footlocker from the baggage cart, placed it on the floor and sat down on it.</p>
<p id="b32-5">The agents then released the dog near the footlocker. Without alerting respondents, the dog signaled the presence of a controlled substance inside. Respondent Chadwick then joined Machado and Leary, and they engaged an attendant to move the footlocker outside to Chadwick’s waiting automobile. Machado, Chadwick, and the attendant together lifted the 200-pound footlocker into the trunk of the car, while Leary waited in'the front seat. At that point, while the trunk of the car was still open and before the car engine had been started, the officers arrested all three. A search disclosed no weapons, but the keys to the footlocker were apparently taken from Machado.</p>
<p id="b32-6">Respondents were taken to the Federal Building in Boston; the agents followed with Chadwick’s car and the footlocker. As the Government concedes, from the moment of respondents’ arrests at about 9 p. m., the footlocker remained under the exclusive control of law enforcement officers at all times. The footlocker and luggage were placed in the Federal Building, where, as one of the agents later testified, “there was no risk that whatever was contained in the footlocker trunk would be removed by the defendants or their associates.” App. 44. The agents had no reason to believe that the footlocker contained explosives or other inherently dangerous items, or that it contained evidence which would lose its value unless the footlocker were opened at once. Facilities were readily available in which the footlocker could have been stored securely; it is not contended that there was any exigency calling for an immediate search.</p>
<p id="b32-7">At the Federal Building an hour and a half after the arrests, the agents opened the footlocker and luggage. They did not obtain respondents’ consent; they did not secure a search warrant. The footlocker was locked with a padlock and a <page-number citation-index="1" label="5">*5</page-number>regular trunk lock. It is unclear whether it was opened with the keys taken from respondent Machado, or by other means. Large amounts of marihuana were found in the footlocker.<footnotemark>1</footnotemark></p>
<p id="b33-5">Respondents were indicted for possession of marihuana with intent to distribute it, in violation of <span class="citation no-link">21 U. S. C. § 841</span> (a) (1), and for conspiracy, in violation of <span class="citation no-link">21 U. S. C. § 846</span>. Before trial, they moved to suppress the marihuana obtained from the footlocker. In the District Court, the Government sought to justify its failure to secure a search warrant under the “automobile exception” of <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), and as a search incident to the arrests. Holding that “ [warrantless searches are <em>per se </em>unreasonable, subject to a few carefully delineated and limited exceptions,” the District Court rejected both justifications. <span class="citation" data-id="1452588"><a href="/opinion/1452588/united-states-v-chadwick/#771" aria-description="Citation for case: United States v. Chadwick">393 F. Supp. 763, 771</a></span> (Mass. 1975). The court saw the relationship between the footlocker and Chadwick’s automobile as merely coincidental, and held that the double-locked, 200-pound footlocker was not part of “the area from within which [respondents] might gain possession of a weapon or destructible evidence.” <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763</a></span> (1969).</p>
<p id="b33-6">A divided Court of Appeals for the First Circuit affirmed the suppression of the seized marihuana. The court held that the footlocker had been properly taken into federal custody after respondents’ lawful arrest; it also agreed that the agents had probable cause to believe that the footlocker contained a controlled substance when they opened it. But probable cause alone was held not enough to sustain the warrantless search. <page-number citation-index="1" label="6">*6</page-number>On the premise that warrantless searches are <em>per se </em>unreasonable unless they fall within some established exception to the warrant requirement, the Court of Appeals agreed with the District Court that the footlocker search was not justified either under the “automobile exception” or as a search incident to a lawful arrest.</p>
<p id="b34-5">The Court of Appeals then responded to an argument, suggested by the Government for the first time on appeal, that movable personalty lawfully seized in a public place should be subject to search without a warrant if there exists probable cause to believe it contains evidence of a crime. Conceding that such personalty shares some characteristics of mobility which support warrantless automobile searches, the court nevertheless concluded that a rule permitting a search of personalty on probable cause alone had not yet “received sufficient recognition by the Supreme Court outside the automobile area, or generally, for us to recognize it as a valid exception to the fourth amendment warrant requirement.” <span class="citation" data-id="9462594"><a href="/opinion/334451/united-states-v-joseph-a-chadwick/#781" aria-description="Citation for case: United States v. Joseph A. Chadwick">532 F. 2d 773, 781</a></span> (1976). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./429/814/">429 U. S. 814</a></span> (1976). We affirm.</p>
<p id="b34-6">(2)</p>
<p id="b34-7">In this Court the Government again contends that the Fourth Amendment Warrant Clause protects only interests traditionally identified with the home.<footnotemark>2</footnotemark> Recalling the colonial writs of assistance, which were often executed in searches of private dwellings, the Government claims that the Warrant Clause was adopted primarily, if not exclusively, in response to unjustified intrusions into private homes on the authority of general warrants. The Government argues there is no evidence that the Framers of the Fourth Amendment intended <page-number citation-index="1" label="7">*7</page-number>to disturb the established practice of permitting warrantless searches outside the home, or to modify the initial clause of the Fourth Amendment by making warrantless searches supported by probable cause <em>per se </em>unreasonable.</p>
<p id="b35-5">Drawing on its reading of history, the Government argues that only homes, offices, and private communications implicate interests which lie at the core of the Fourth Amendment. Accordingly, it is only in these contexts that the determination whether a search or seizure is reasonable should turn on whether a warrant has been obtained. In all other situations, the Government contends, less significant privacy values are at stake, and the reasonableness of a government intrusion should depend solely on whether there is probable cause to believe evidence of criminal conduct is present. Where personal effects are lawfully seized outside the home on probable cause, the Government would thus regard searches without a warranty not “unreasonable.”</p>
<p id="b35-6">We do not agree that the Warrant Clause protects only dwellings and other specifically designated locales. As we have noted before, the Fourth Amendment “protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967); more particularly, it protects people from unreasonable government intrusions into their legitimate expectations of privacy. In this case, the Warrant Clause makes a significant contribution to that protection. The question, then, is whether a warrantless search in these circumstances was unreasonable.<footnotemark>3</footnotemark></p>
<p id="b35-7">(3)</p>
<p id="b35-8">It cannot be doubted that the Fourth Amendment’s commands grew in large measure out of the colonists’ experience <page-number citation-index="1" label="8">*8</page-number>with the writs of assistance and their memories of the general warrants formerly in use in England. These writs, which were issued on executive rather than judicial authority, granted sweeping power to customs officials and other agents of the King to search at large for smuggled goods. Though the authority to search granted by the writs was not limited to the home, searches conducted pursuant to them often were carried out in private residences. See generally <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span> (1965); <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724-729</a></span> (1961); <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span> (1959).</p>
<p id="b36-5">Although the searches and seizures which deeply concerned the colonists, and which were foremost in the minds of the Framers, were those involving invasions of the home, it would be a mistake to conclude, as the Government contends, that the Warrant Clause was therefore intended to guard only against intrusions into the home. First, the Warrant Clause does not in terms distinguish between searches conducted in private homes and other searches. There is also a strong historical connection between the Warrant Clause and the initial clause of the Fourth Amendment, which draws no distinctions among “persons, houses, papers, and effects” in safeguarding against unreasonable searches and seizures. See <em>United States </em>v. <em>Rabinowits, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 68</a></span> (1950) (Frankfurter, J., dissenting).</p>
<p id="b36-6">Moreover, if there is little evidence that the Framers intended the Warrant Clause to operate outside the home, there is no evidence at all that they intended to exclude from protection of the Clause all searches occurring outside the home. The absence of a contemporary outcry against war-rantless searches in public places was because, aside from searches incident to arrest, such warrantless searches were not a large issue in colonial America. Thus, silence in the historical record tells us little about the Framers' attitude toward application of the Warrant Clause to the search of respond<page-number citation-index="1" label="9">*9</page-number>ents’ footlocker.<footnotemark>4</footnotemark> What we do know is that the Framers were men who focused on the wrongs of that day but who intended the Fourth Amendment to safeguard fundamental values which would far outlast the specific abuses which gave it birth.</p>
<p id="b37-5">Moreover, in this area we do not write on a clean slate. Our fundamental inquiry in considering Fourth Amendment issues is whether or not a search or seizure is reasonable under all the circumstances. <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967). The judicial warrant has a significant role to play in that it provides the detached scrutiny of a neutral magistrate, which is a more reliable safeguard against improper searches than the hurried judgment of a law enforcement officer “engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Once a lawful search has begun, it is also far more likely that it will not exceed proper bounds when it is done pursuant to a judicial authorization “particularly describing the place to be searched and the persons or things to be seized.” Further, a warrant assures the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search. <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span> (1967).</p>
<p id="b37-6">Just as the Fourth Amendment “protects people, not places,” the protections a judicial warrant offers against erro<page-number citation-index="1" label="10">*10</page-number>neous governmental intrusions are effective whether applied in or out of the home. Accordingly, we have held warrantless searches unreasonable, and therefore unconstitutional, in a variety of settings.<footnotemark>5</footnotemark> A century ago, Mr. Justice Field, speaking for the Court, included within the reach of the Warrant Clause printed matter traveling through the mails within the United States:</p>
<blockquote id="b38-5">“Letters and sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household.” <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878).</blockquote>
<p id="b38-6">We reaffirmed <em>Jackson </em>in <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970), where a search warrant was obtained to open two packages which, on mailing, the sender had declared contained only coins. Judicial warrants have been required for other searches conducted outside the home. <em>E. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967) (electronic interception of conversation in public telephone booth); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971) (automobile on private <page-number citation-index="1" label="11">*11</page-number>premises); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964) (automobile in custody); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1961) (hotel room); <em>G. M. Leasing Corp, </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338</a></span> (1977) (office); <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968) (office). These cases illustrate the applicability of the Warrant Clause beyond the narrow limits suggested by the Government. They also reflect the settled constitutional principle, discussed earlier, that a fundamental purpose of the Fourth Amendment is to safeguard individuals from unreasonable government invasions of legitimate privacy interests,<footnotemark>6</footnotemark> and not simply those interests found inside the four walls of the home. <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949).</p>
<p id="b39-5">In this case, important Fourth Amendment privacy interests were at stake. By placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination. No less than one who locks the doors of his home against intruders, one who safeguards his personal possessions in this manner is due the protection of the Fourth Amendment Warrant Clause. There being no exigency, it was unreasonable for the Government to conduct this search without the safeguards a judicial warrant provides.</p>
<p id="b39-6">(4)</p>
<p id="b39-7">The Government does not contend that the footlocker’s brief contact with Chadwick’s car makes this an automobile search, but it is argued that the rationale of our automobile <page-number citation-index="1" label="12">*12</page-number>search cases demonstrates the reasonableness of permitting warrantless searches of luggage; the Government views such luggage as analogous to motor vehicles for Fourth Amendment purposes. It is true that, like the footlocker in issue here, automobiles are “effects” under the Fourth Amendment, and searches and seizures of automobiles are therefore subject to the constitutional standard of reasonableness. But this Court has recognized significant differences between motor vehicles and other property which permit warrantless searches of automobiles in circumstances in which warrantless searches would not be reasonable in other contexts. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Preston </em>v. <em>United States, supra, </em>at 366-367; <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970). See also <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span> (1976).</p>
<p id="b40-5">Our treatment of automobiles has been based in part on their inherent mobility, which often makes obtaining a judicial warrant impracticable. Nevertheless, we have also sustained “warrantless searches of vehicles ... in cases in which the possibilities of the vehicle’s being removed or evidence in it destroyed were remote, if not nonexistent.” . <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); accord, <em>South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 367</a></span>; see <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/" aria-description="Citation for case: Texas v. White">423 U. S. 67</a></span> (1975); <em>Chambers </em>v. <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra;</a></span> Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967).</p>
<p id="b40-6">The answer lies in the diminished expectation of privacy which surrounds the automobile:</p>
<blockquote id="b40-7">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one’s residence or as the repository of personal effects. ... It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b40-8">Other factors reduce automobile privacy. “All States require <page-number citation-index="1" label="13">*13</page-number>vehicles to be registered and operators to be licensed. States and localities have enacted extensive and detailed codes regulating the condition and manner in which motor vehicles may be operated on public streets and highways.” <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 441</a></span>. Automobiles periodically undergo official inspection, and they are often taken into police custody in the interests of public safety. <em>South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 368</a></span>.</p>
<p id="b41-5">The factors which diminish the privacy aspects of an automobile do not apply to respondents’ footlocker. Luggage contents are not open to public view, except as a condition to a border entry or common carrier travel; nor is luggage subject to regular inspections and official • scrutiny on a continuing basis. Unlike an automobile, whose primary function is transportation, luggage is intended as a repository of personal effects. In sum, a person’s expectations of privacy in personal luggage are substantially greater than in an automobile.</p>
<p id="b41-6">Nor does the footlocker’s mobility justify dispensing with the added protections of the Warrant Clause. Once the federal agents had seized it at the railroad station and had safely transferred it to the Boston Federal Building under their exclusive control, there was not the slightest danger that the footlocker or its contents could have been removed before a valid search warrant could be obtained.<footnotemark>7</footnotemark> The initial seizure and detention of the footlocker, the validity of which respondents do not contest, were sufficient to guard against any risk that evidence might be lost. With the footlocker safely immobilized, it was unreasonable to undertake the additional and greater intrusion of a search without a warrant.<footnotemark>8</footnotemark></p>
<p id="b42-4"><page-number citation-index="1" label="14">*14</page-number>Finally, the Government urges that the Constitution permits the warrantless search- of any property in the possession of a person arrested in public, so long as there is probable cause to believe that the property contains contraband or evidence of crime. Although recognizing that the footlocker was not within respondents’ immediate control, the Government insists that the search was reasonable because the footlocker was seized contemporaneously with respondents' arrests and was searched as soon thereafter as was practicable. The reasons justifying search in a custodial arrest are quite different. When a custodial arrest is made, there is always some danger that the person arrested may seek to use a weapon, or that evidence may be concealed or destroyed. To safeguard himself and others, and to prevent the loss of evidence, it has been held reasonable for the arresting officer to conduct a prompt, warrantless “search of the arrestee’s person and the area ‘within his immediate control’ — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.” <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. See also <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968).</p>
<p id="b42-5">Such searches may be conducted without a warrant, and they may also be made whether or not there is probable cause to believe that the person arrested may have a weapon or is about to destroy evidence. The potential dangers lurking in <page-number citation-index="1" label="15">*15</page-number>all custodial arrests make warrantless searches of items within the “immediate control” area reasonable without requiring the arresting officer to calculate the probability that weapons or destructible evidence may be involved. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra.</a></span> </em>However, warrantless searches of luggage or other property seized at the time of an arrest cannot be justified as incident to that arrest either if the “search is remote in time or place from the arrest,” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S., at 367</a></span>, or no exigency exists. Once law enforcement officers have reduced luggage or other personal property not immediately associated with the person of the arrestee to their exclusive control, and there is no longer any danger that the arrestee might gain access to the property to seize a weapon or destroy evidence, a search of that property is no longer an incident of the arrest.<footnotemark>9</footnotemark></p>
<p id="b43-5">Here the search was conducted more than an hour after federal agents had gained exclusive control of the footlocker and long after respondents were securely in custody; the search therefore cannot be viewed as incidental to the arrest or as justified by any other exigency. Even though on this record the issuance of a warrant by a judicial officer was reasonably predictable, a line must be drawn. In our view, when no exigency is shown to support the need for an immediate search, the Warrant Clause places the line at the point where the property to be searched comes under the exclusive dominion of police authority. Respondents were therefore entitled to the protection of the Warrant Clause with the <page-number citation-index="1" label="16">*16</page-number>evaluation of a neutral magistrate, before their privacy-interests in the contents of the footlocker were invaded.<footnotemark>10</footnotemark></p>
<p id="AzR">Accordingly, the judgment is</p>
<p id="b44-5">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b33-7"> Marihuana was also found in the suitcases. The Court of Appeals found no adequate justification for the warrantless suitcase search, and suppressed this evidence. Incriminating statements made by respondent Chadwick during the arrest procedure were also suppressed, on the theory that there had not been probable cause to arrest him and that his statements were therefore tainted as the product of an illegal arrest. However, the petition for certiorari draws into question only the footlocker search; consequently, we need not pass on the legality of Chadwick’s arrest or the search of the suitcases.</p>
</footnote>
<footnote label="2">
<p id="b34-8"> The Fourth Amendment provides:</p>
<blockquote id="b34-9">“The right of the people to be secure in their persons, houses, papersj and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="3">
<p id="b35-9"> In this Court the Government has limited the question presented to “[w]hether a search warrant is required before federal agents may open a locked footlocker that is properly in their possession and that they have probable cause to believe contains contraband.” Accordingly, this case presents no issue of the application of the exclusionary rule.</p>
</footnote>
<footnote label="4">
<p id="b37-7"> The Government’s historical analysis is further undercut by its own arguments. The Government acknowledges that the core values the Fourth Amendment protects are privacy interests. In its view, those privacy interests which should receive the “maximum protection from governmental search or seizure” provided by the Warrant Clause include private oral and electronic communication, “[i]n addition to the home and other structures such as an office or hotel room . . . .” Brief for United States 30. It is not readily apparent how the Government’s contention that the Warrant Clause applies to high privacy areas, both within and without the home, can be reconciled with its earlier contention that judicial warrants are appropriate only for searches conducted within private dwellings.</p>
</footnote>
<footnote label="5">
<p id="b38-7"><em> </em>In circumstances involving noncriminal inventory searches, where probable cause to search is irrelevant, we have recognized "that search warrants are not required, linked as the warrant requirement textually is to the probable-cause concept.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>, 370 n. 5 (1976). This is so because the salutary functions of a warrant simply have no application in that context; the constitutional reasonableness of inventory searches must be determined on other bases.</p>
</footnote>
<footnote label="6">
<p id="b39-8"> This has been settled law in this Court for over 90 years. At least since <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), we have known that “[i]t is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property . . . .” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 630</a></span>.</p>
<p id="b39-9">This is not to say that the Fourth Amendment translates precisely into a constitutional privacy right. See <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350-351</a></span> (1967).</p>
</footnote>
<footnote label="7">
<p id="b41-7"> This may often not be the case when automobiles are seized, Absolutely secure storage facilities may not be available, see <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973), and the size and inherent mobility of a vehicle malee it susceptible to theft or intrusion by vandals.</p>
</footnote>
<footnote label="8">
<p id="b41-8"> Respondents’ principal privacy interest in the footlocker was, of <page-number citation-index="1" label="14">*14</page-number>course, not in the container itself, which was exposed to public view, but in its contents. A search of the interior was therefore a far greater intrusion into Fourth Amendment values than the impoundment of the footlocker. Though surely a substantial infringement of’respondents’ use and possession, the seizure did not diminish respondents’ legitimate expectation that the footlocker’s contents would remain private.</p>
<p id="b42-7">It was the greatly reduced expectation of privacy in the automobile, coupled with the transportation function of the vehicle, which made the Court in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>unwilling to decide whether an immediate search of an automobile, or its seizure and indefinite immobilization, constituted a greater interference with the rights of the owner. This is clearly not the case with locked luggage.</p>
</footnote>
<footnote label="9">
<p id="b43-6"> Of course, there may be other justifications for a warrantless search of luggage taken from a suspect at the time of his arrest; for example, if officers have reason to believe that luggage contains some immediately dangerous instrumentality, such as explosives, it would be foolhardy to transport it to the station house without opening the luggage and dis&gt;arming the weapon. See, <em>e. g., United States </em>v. <em>Johnson, </em><span class="citation" data-id="9458727"><a href="/opinion/305845/united-states-v-alphonse-johnson/#639" aria-description="Citation for case: United States v. Alphonse Johnson">467 F. 2d 630, 639</a></span> (CA2 1972).</p>
</footnote>
<footnote label="10">
<p id="b44-10"> TMike searches of the person, <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973); <em>United States </em>v. <em>Edwards, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U. S. 800</a></span> </em>(1974), searches of possessions within an arrestee’s immediate control cannot be justified by any reduced expectations of privacy caused by the arrest. Respondents’ privacy interest in the contents of the footlocker was not eliminated simply because they were under arrest.</p>
</footnote>
</opinion>
```

---
