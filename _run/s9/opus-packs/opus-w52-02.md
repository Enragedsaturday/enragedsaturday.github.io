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

## GROUP: content/cases/United States v. Carpenter (6th Cir. 2019 remand).md  (`case`, 5 assertions)

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
{"assertion_id": "f42006aae3b182aa", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "926 F.3d 313 (2019)", "court": "6th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Carpenter (6th Cir. 2019 remand)", "year": "2019"}}
{"assertion_id": "25452b1ff2ab8572", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key", "title": "United States v. Carpenter (6th Cir. 2019 remand)"}}
{"assertion_id": "5bcf0ba7bd8233dd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "On remand from Carpenter v. United States, the Sixth Circuit held that although the warrantless acquisition of the defendant's historical cell-site location information violated the Fourth Amendment, suppression was not required because the FBI agents obtained the records in objectively reasonable, good-faith reliance on the Stored Communications Act.", "title": "United States v. Carpenter (6th Cir. 2019 remand)"}}
{"assertion_id": "1cf5138ae8141f40", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. Carpenter (6th Cir. 2019 remand)"}}
{"assertion_id": "3f20838ef05e05cb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Carpenter (6th Cir. 2019 remand)", "varies_by_point": "false"}}
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

## GROUP: content/cases/United States v. Ceccolini.md  (`case`, 5 assertions)

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
{"assertion_id": "c2e9671fb4423768", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "435 U.S. 268 (1978)", "court": "U.S. Supreme Court", "neutral_cite": "1978 U.S. LEXIS 70", "official_citation_present": true, "parallel_cite": "98 S. Ct. 1054; 55 L. Ed. 2d 268", "title": "United States v. Ceccolini", "year": "1978"}}
{"assertion_id": "3998ebf19b8d4f5a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Live-witness testimony is far less readily suppressed as a fruit of an illegal search than inanimate evidence; the exclusionary rule applies with much greater reluctance to the discovery of a willing witness.", "title": "United States v. Ceccolini"}}
{"assertion_id": "b8f77770a50af363", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Progeny (attenuation)", "title": "United States v. Ceccolini"}}
{"assertion_id": "383317cb846d3b8c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ceccolini"}}
{"assertion_id": "8e021fd75b9e1ee4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1978-03-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ceccolini", "field_i_validity": "good_law", "scope_note": "The witness-attenuation factors remain the governing framework for suppressing live-witness testimony as a fruit; reaffirmed in the modern attenuation line.", "title": "United States v. Ceccolini", "varies_by_point": "false"}}
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

## GROUP: content/cases/United States v. Chavez.md  (`case`, 5 assertions)

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
{"assertion_id": "18774c6dfc5138e4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "534 F.3d 1338 (2008)", "court": "10th Cir.", "neutral_cite": "2008 U.S. App. LEXIS 16558; 2008 WL 2893057", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Chavez", "year": "2008"}}
{"assertion_id": "75f7e9d0bc31e280", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key", "title": "United States v. Chavez"}}
{"assertion_id": "f7d8dbd050519b3a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the collective-knowledge doctrine, probable cause held by the DEA task force that investigated and arranged a controlled cocaine buy could be imputed to the patrolman the task force directed to stop the suspect's vehicle, even though the patrolman himself was not privy to the investigation's details; the stop and search were therefore justified and suppression was properly denied.", "title": "United States v. Chavez"}}
{"assertion_id": "701401682f25b168", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Chavez"}}
{"assertion_id": "784b01609845ec7a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Chavez", "varies_by_point": "false"}}
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

## GROUP: content/cases/United States v. Conner.md  (`case`, 5 assertions)

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
{"assertion_id": "9e72bc34ba5ef398", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "127 F.3d 663 (1997)", "court": "U.S. Court of Appeals, 8th Circuit", "neutral_cite": "1997 U.S. App. LEXIS 27680; 1997 WL 615947", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Conner", "year": "1997"}}
{"assertion_id": "b5a4acbb608b7a30", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Recent development (role-based)", "title": "United States v. Conner"}}
{"assertion_id": "f744a4b607463c26", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where police, under color of authority, demand that occupants of a motel room open the door, and an occupant opens the door not…", "title": "United States v. Conner"}}
{"assertion_id": "3fc8dd096f7b5fb2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Conner"}}
{"assertion_id": "6127f0ff7e91dfb4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Conner", "field_i_validity": "good_law", "scope_note": "Good law in-circuit; a door opened in submission to a police demand under color of authority is not consensual.", "title": "United States v. Conner", "varies_by_point": "false"}}
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
