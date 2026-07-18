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

## GROUP: content/cases/Jimerson v. Lewis.md  (`case`, 5 assertions)

### content_page

```
---
title: Jimerson v. Lewis
type: case
citation: "94 F.4th 423 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 5th Cir. 2024
court_level: coa
circuit: ca5
year: 2024
date_decided: 2024-02-15
docket: 22-10441
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
  opinion_url: "https://www.courtlistener.com/opinion/9475670/jimerson-v-lewis/"
  cluster_id: 9475670
  opinion_id: null
  identity_checked: false
lake:
  record_id: Jimerson v. Lewis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Qualified Immunity]]"
    role: Key
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Maryland v. Garrison]]"
tags:
  - case
  - fourth-amendment
  - qualified-immunity
  - section-1983
  - search-warrant
  - wrong-house
  - clearly-established-law
holding: "A SWAT commander whose team executed a no-knock warrant at the wrong house was entitled to qualified immunity because, although his efforts to identify the correct residence were deficient, no clearly established law made that failure a Fourth Amendment violation."
---

# Jimerson v. Lewis

*94 F.4th 423 (5th Cir. 2024)* (No. 22-10441) · U.S. Court of Appeals for the Fifth Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9475670 → lead opinion 9941201 (94 F.4th 423, decided 2024-02-15); Rule quote string-matched to the CL opinion text 2026-07-07. CL text is slip-paginated (no 94 F.4th star pagination), so the pin is slip-style per S2 A3. S9 promotes. -->

## Background
A DEA officer asked Waxahachie SWAT commander Lieutenant Mike Lewis to help execute a nighttime search warrant on a suspected methamphetamine "stash house" at 573 8th Street. Led to the block, the team first assembled at the wrong house; when Lewis looked to a neighboring house he mistakenly identified it as the target, then, realizing that too was wrong, directed the team to yet another house — the Jimersons' home, in the opposite direction from the target. The SWAT team executed a no-knock, forced entry on the Jimersons. They sued Lewis under § 1983; the district court denied him [[Qualified Immunity|qualified immunity]], finding a fact dispute about the reasonableness of his identification efforts.

## Issue
Whether a SWAT commander whose team executed a warrant at the wrong residence is entitled to [[Qualified Immunity|qualified immunity]] where his efforts to identify the correct house were deficient but no clearly established law condemned them.

## Rule
The Fifth Circuit reversed, holding that the material facts were undisputed and the question was one of law: measured against *[[Maryland v. Garrison|Garrison]]*'s reasonable-effort standard, Lewis's conduct did not transgress a clearly established rule. "We conclude that this officer's efforts to identify the correct residence, though deficient, did not violate clearly established law." — slip op. at 1–2. Absent precedent placing the constitutional question "beyond debate," [[Qualified Immunity|qualified immunity]] shields the officer.

## Application
The court accepted that Lewis's identification of the house was objectively deficient but explained that [[Qualified Immunity|qualified immunity]] turns on notice: the plaintiffs pointed to no controlling, factually analogous precedent that would have told a reasonable commander his errors crossed a constitutional line. A nonprecedential decision could not supply clearly established law, and the circuit's cases did not clearly govern this wrong-house raid. Judge Dennis dissented, arguing the undisputed facts showed a violation of clearly established law.

## Conclusion
The denial of [[Qualified Immunity|qualified immunity]] was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]] for dismissal**. Southwick, J., wrote for the majority; Dennis, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Jimerson* is a recent, sharply divided illustration of [[Qualified Immunity|qualified immunity]]'s "clearly established law" prong operating in the wrong-house-raid context: even a deficient effort to identify the place to be searched (*[[Maryland v. Garrison|Garrison]]*) does not defeat immunity without precedent squarely on point.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key*

## Sources
- [*Jimerson v. Lewis*, 94 F.4th 423 (5th Cir. 2024)](https://www.courtlistener.com/opinion/9475670/jimerson-v-lewis/) — pinpoint: slip op. at 1–2 (holding on qualified immunity / clearly established law); the CL opinion text carries the slip-opinion page numbers rather than 94 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "afbd2860f848d13f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "94 F.4th 423 (2024)", "court": "5th Cir. 2024", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Jimerson v. Lewis", "year": "2024"}}
{"assertion_id": "330a7e1c0a1a9f0a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A SWAT commander whose team executed a no-knock warrant at the wrong house was entitled to qualified immunity because, although his efforts to identify the correct residence were deficient, no clearly established law made that failure a Fourth Amendment violation.", "title": "Jimerson v. Lewis"}}
{"assertion_id": "82e51a7c1e225ebe", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key", "title": "Jimerson v. Lewis"}}
{"assertion_id": "090d22cdf9d94d31", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "Jimerson v. Lewis"}}
{"assertion_id": "10bc9c184ec65a43", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Jimerson v. Lewis", "varies_by_point": "false"}}
```

### lake record — Jimerson v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jimerson v. Lewis",
  "status": "under_review",
  "identity": {
    "case_name": "Jimerson v. Lewis",
    "case_name_short": "Jimerson",
    "case_name_full": "",
    "input_case_name": "Jimerson v. Lewis",
    "court": "5th Cir. 2024",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": "2024-02-15",
    "year": 2024,
    "docket": "22-10441",
    "cluster_id": 9475670,
    "lead_opinion_id": 9941201,
    "sibling_ids": [],
    "absolute_url": "/opinion/9475670/jimerson-v-lewis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "94 F.4th 423",
      "volume": "94",
      "reporter": "F.4th",
      "page": "423",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "94 F.4th 423",
        "volume": "94",
        "reporter": "F.4th",
        "page": "423",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "94 F.4th 423",
    "official_selection": {
      "court_class": "coa",
      "selected": "94 F.4th 423",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Justia",
        "url": "https://law.justia.com/cases/federal/appellate-courts/ca5/22-10441/22-10441-2024-02-01.html",
        "cite": "94 F.4th 423",
        "checked_date": "2026-07-07"
      },
      {
        "source": "FindLaw",
        "url": "https://caselaw.findlaw.com/court/us-5th-circuit/115835080.html",
        "cite": "94 F.4th 423",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-06T05:45:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "jimerson-v-lewis--9475670",
      "to_record_id": "Jimerson v. Lewis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Jimerson v. Lewis

```
Case: 22-10441     Document: 00517065342       Page: 1    Date Filed: 02/15/2024




                       REVISED February 15, 2024


           United States Court of Appeals
                for the Fifth Circuit
                               ____________
                                                                  United States Court of Appeals
                                                                           Fifth Circuit
                                 No. 22-10441
                               ____________                              FILED
                                                                   February 1, 2024
   Karen Jimerson; JJ; JJ; XP; JP,                                  Lyle W. Cayce
                                                                         Clerk
                                                         Plaintiffs—Appellees,

                                     versus

   Mike Lewis, Lt,

                                           Defendant—Appellant.
                  ______________________________

                  Appeal from the United States District Court
                      for the Northern District of Texas
                           USDC No. 3:20-CV-2826
                  ______________________________

   Before Stewart, Dennis, and Southwick, Circuit Judges.
   Leslie H. Southwick, Circuit Judge:
         A search warrant showed the correct address for the target house, but
   police officers executed the warrant at an incorrect address. The homeowner
   brought suit against the officers under Section 1983. When denying summary
   judgment on the issue of qualified immunity for the officer who led the
   search, the district court held that fact questions prevented deciding the
   issue. We find no genuine disputes of material fact. The disputed issue is
   one of law. We conclude that this officer’s efforts to identify the correct
Case: 22-10441      Document: 00517065342          Page: 2   Date Filed: 02/15/2024




                                    No. 22-10441


   residence, though deficient, did not violate clearly established law.
   REVERSED and REMANDED for dismissal.
           FACTUAL AND PROCEDURAL BACKGROUND
          In March 2019, at approximately 7:15 p.m., Waxahachie Police
   Department (“WPD”) SWAT Team Commander Mike Lewis received a
   call from a Drug Enforcement Administration (“DEA”) officer. The DEA
   officer needed assistance executing a search warrant that night on a suspected
   methamphetamine “stash” house located at 573 8th Street, Lancaster, Texas
   (“target house”). The officer provided Commander Lewis with information
   about a drug deal involving the target house. Lewis requested further
   information, including pictures of the target house, whether “the location
   was fortified,” whether “it appeared to have surveillance equipment,” and
   whether “there were any exterior indicators on the property that children
   may be present.”      He also “requested identifying information on the
   [methamphetamine] seller, as well as prior law enforcement history at that
   address” involving the Lancaster Police Department (“LPD”).
          In response, Lewis received pictures showing the front of the house
   and was told there was “surveillance established at the location.” DEA
   agents told Lewis that they saw no fortification or surveillance cameras at the
   property or any evidence of children. The agents had no description of the
   people occupying the target house.
          Lewis entered the information into the WPD SWAT’s risk analysis
   assessment worksheet, which scored the incident within the range for
   “optional SWAT deployment.” Consequently, Lewis contacted the WPD
   Chief and received approval to activate the SWAT team. He also gathered
   information on the target house from the Dallas Central Appraisal District
   website, including that the house was 744 square feet, was built in 1952, and
   had a “large, deeply extending backyard.”




                                         2
Case: 22-10441        Document: 00517065342              Page: 3      Date Filed: 02/15/2024




                                         No. 22-10441


           Lewis then briefed SWAT officers at the WPD. The group decided
   to have a six-member team enter the target house and a three-member team
   enter the detached garage and backyard. Thereafter, Lewis received “real-
   time intelligence that surveillance officers at the scene reported a truck
   pulling a white box trailer [had] pulled up in front of the target location.” 1
   When Lewis received a copy of the warrant, he confirmed the address of the
   target house. The officers then finalized their preparations. LPD Officer
   Zachary Beauchamp led the SWAT team to the target house. Beauchamp
   was followed by the SWAT team vehicle, then Lewis in his marked patrol
   unit, then the Waxahachie K9, and then several unmarked DEA vehicles.
   Beauchamp was directed “to stop about a house before the target location,
   so SWAT officers could make an approach on foot.”
           When they arrived at the area, the SWAT team vehicle’s driver saw
   Beauchamp’s vehicle stop abruptly, “causing him to believe [Beauchamp]
   may have driven too far and stopped them too close to the target location.”
   As the officers exited their vehicles, Beauchamp pointed to the house with
   the truck and white trailer in front of it, and officers began their approach. As
   the SWAT team began gathering on the front porch, however, Lewis realized
   that the house did not look like the house from intelligence photos. The
   SWAT team had assembled at 583 8th Street, not at the target house at 573
   8th Street.
           When Lewis looked one house to the left, he decided the layout of the
   front of that house matched the one in the intel photos. Lewis noticed that
   “[f]rom left to right, it had one large window, followed by the front entry
   door, followed by a small window and then [four] larger windows.” He also

           _____________________
           1
             The record indicates that this intelligence was not accurate. Later investigation
   revealed that the white trailer was in front of 583 8th Street — not the target house.




                                               3
Case: 22-10441       Document: 00517065342         Page: 4    Date Filed: 02/15/2024




                                    No. 22-10441


   noticed that “[t]he driveway was . . . on the left side of the property,” and he
   believed numbers on the front of the house read “573,” though the porch
   light obscured his view. This house, it turns out, was also the wrong house.
   The house Lewis identified was 593 8th Street, two doors down from the
   target house.
          Nevertheless, Lewis told the team that they were at the wrong house
   and instructed them to “go to the house just to the left of the house where
   they were.” That house was the home of plaintiffs Karen Jimerson, James
   Parks, and their two young sons and daughter. Officers ran to the front of the
   plaintiffs’ house, deployed a flashbang, broke the front windows, and
   breached the door. The officers began a protective sweep and checked for
   occupants. They “encountered two females” whom they told to get on the
   ground. The officers then encountered an adult male, but before they could
   direct him to get down, SWAT team members yelled “Wrong House!”
          The SWAT team left the plaintiffs’ home and proceeded to the target
   house. After the target house was secured, Lewis returned to the plaintiffs’
   house, where he joined other DEA agents who were already checking on the
   plaintiffs’ welfare. Plaintiff Karen Jimerson reported some pain in her side.
   Lewis called an ambulance and she was taken to the hospital. Lewis also
   coordinated with a glass company to make repairs and remained on the scene
   until 1:30 a.m.
          A WPD internal investigation determined that “reasonable and
   normal protocol was completely overlooked” and the WPD Chief of Police
   stated that these kinds of mistakes should not happen. Lewis was suspended
   for two days without pay.
          In September 2020, the plaintiffs brought this action under 42 U.S.C.
   § 1983. They alleged violations of the Fourth Amendment and several state
   laws against 20 John Doe defendants. They later amended their complaint,




                                          4
Case: 22-10441      Document: 00517065342           Page: 5     Date Filed: 02/15/2024




                                     No. 22-10441


   naming each of the individuals in the WPD SWAT team who executed the
   warrant, including Lewis. Shortly thereafter, the plaintiffs’ state-law tort
   claims were dismissed. The defendants moved for summary judgment based
   on qualified immunity, and the matter was referred to a magistrate judge for
   pretrial management.
          The magistrate judge recommended the district court grant qualified
   immunity to all the officers, whether they entered the house or not. The
   magistrate judge also concluded the plaintiffs failed to show that Lewis did
   not make reasonable efforts to identify the target house.
          The district court agreed with the magistrate judge’s analysis on
   qualified immunity except with respect to whether Lewis made reasonable
   efforts to identify the target house. The court found “a genuine dispute of
   material fact regarding whether [Lewis] made the necessary reasonable effort
   to identify the correct residence and whether his actions were ‘[in]consistent
   with a reasonable effort to ascertain and identify the place intended to be
   searched,’” quoting Maryland v. Garrison, 480 U.S. 79, 88 (1987). The court
   denied Lewis qualified immunity. Lewis timely appealed.
                                  DISCUSSION
          Federal and state officials may be entitled to qualified immunity from
   claims for money damages for their actions. Ashcroft v. al-Kidd, 563 U.S. 731,
   735 (2011). To overcome this defense, a plaintiff needs to plead plausible
   facts “(1) that the official violated a statutory or constitutional right, and (2)
   that the right was ‘clearly established’ at the time of the challenged
   conduct.” Id. (quoting Harlow v. Fitzgerald, 457 U.S. 800, 818 (1982)).
          If the district court denies qualified immunity either on a motion to
   dismiss or on summary judgment, the defendant official may immediately
   appeal under the collateral order doctrine. Behrens v. Pelletier, 516 U.S. 299,
   307 (1996). Here, summary judgment was denied, and our review is de novo.




                                           5
Case: 22-10441      Document: 00517065342           Page: 6     Date Filed: 02/15/2024




                                     No. 22-10441


   Joseph ex rel. Joseph v. Bartlett, 981 F.3d 319, 331 (5th Cir. 2020). Review is
   limited to considering issues of law, including the legal significance of factual
   disputes identified by the district court. Id. at 331. That means “we may
   evaluate whether a factual dispute is material (i.e., legally significant), but we
   may not evaluate whether it is genuine (i.e., exists).”        Id. (emphasis in
   original). “Because the plaintiff is the non-moving party, we construe all
   facts and inferences in the light most favorable to the plaintiff.” Melton, 875
   F.3d at 261.
          As a preliminary matter, Lewis argues the plaintiffs failed to plead and
   argue that his efforts to identify the correct house were unreasonable. A
   plaintiff seeking to overcome qualified immunity “must specifically identify
   each defendant’s personal involvement in the alleged wrongdoing.” Thomas
   v. Humfield, 32 F.3d 566, 1994 WL 442484, at *5 (5th Cir. 1994). The
   plaintiffs complied with the need for specificity by alleging in the complaint
   that Lewis “was the person in charge” of the mistaken raid on their home,
   and in their summary judgment arguments that Lewis was the “overall leader
   of [the] misconduct” and that he overlooked “reasonable and normal
   protocol.”
          As to the merits, Lewis does not challenge the district court’s analysis
   of whether defendants violated the plaintiffs’ rights under federal law. The
   Fourth Amendment provides that individuals have a right “to be secure in
   their persons, houses, papers, and effects, against unreasonable searches and
   seizures.” U.S. CONST. amend. IV. The Supreme Court has held that
   officers must make “reasonable effort[s] to ascertain and identify the place
   intended to be searched” in order to comply with the Fourth Amendment.
   Garrison, 480 U.S. at 88. To be clear about an occasional irrelevant addition
   to the proper analysis, we do not consider whether the officer’s actions were
   “objectively unreasonable.” That quoted standard is a “vestige of older
   caselaw that predates the Supreme Court’s current test.” Parker v. LeBlanc,



                                           6
Case: 22-10441      Document: 00517065342          Page: 7   Date Filed: 02/15/2024




                                    No. 22-10441


   73 F.4th 400, 406 n.1 (5th Cir. 2023). In another precedential rejection of an
   “objectively unreasonable” component of qualified immunity, we held there
   is no “standalone ‘objective reasonableness’ element to the Supreme
   Court’s two-pronged test for qualified immunity.” Baker v. Coburn, 68 F.4th
   240, 251 n.10 (5th Cir. 2023).
          We evaluate the reasonableness of Lewis’s actions because the
   plaintiffs’ claims arise under the Fourth Amendment. The district court
   denied qualified immunity because the court found a “genuine dispute of
   material fact regarding whether [Lewis] made the necessary reasonable
   efforts to identify the correct residence.” As we stated earlier, we cannot
   review a district court’s determination that a factual dispute is genuine.
   Bartlett, 981 F.3d at 331. We are to decide, though, legal significance, i.e.,
   whether disputed facts are material to resolution of the case. Id.
          The district court did not find evidentiary disputes about what Lewis
   and others did before entering the incorrect house. The court stated that the
   central dispute was whether those actions constituted “necessary reasonable
   efforts.” Certainly, unlike here, exactly what an officer did may sometimes
   be factually unclear. A court’s determination of reasonableness under the
   Fourth Amendment, though, “‘is predominantly an objective inquiry.’” al-
   Kidd, 563 U.S. at 736 (quoting City of Indianapolis v. Edmond, 531 U.S. 32, 47
   (2000)).    The circumstances are to be “viewed objectively” and a
   determination made of whether they “justify” the search. Id. (quoting Scott
   v. United States, 436 U.S. 128, 138 (1978)).
          Consequently, as a legal issue for our de novo review, we consider
   whether Lewis’s conduct violated clearly established law. See id. at 325–26.
   Clearly established law is determined by reference to “controlling
   authority[,] or a robust consensus of persuasive authority.” Delaughter v.
   Woodall, 909 F.3d 130, 139 (5th Cir. 2018) (citation omitted). The keystone




                                          7
Case: 22-10441        Document: 00517065342              Page: 8       Date Filed: 02/15/2024




                                          No. 22-10441


   in this analysis is fair warning. Id. at 139–40. To overcome qualified
   immunity, plaintiffs must cite “a body of relevant case law [] in which an
   officer acting under similar circumstances . . . was held to have violated” a
   defendant’s constitutional rights. Bartlett, 981 F.3d at 330 (quotation marks and
   citations omitted). “While there need not be ‘a case directly on point,’ the
   unlawfulness of the challenged conduct must be ‘beyond debate.’” Id.
   (quoting al–Kidd, 563 U.S. at 741).
           Compliance with the Fourth Amendment requires a law enforcement
   officer’s “reasonable effort[s] to ascertain and identify the place intended to
   be searched.” Garrison, 480 U.S. at 88. In applying that general principle,
   the district court relied on two opinions. One was a nonprecedential opinion
   of this court. Rogers v. Hooper, 271 F. App’x 431 (5th Cir. 2008). The other
   was nonprecedential in the Fifth Circuit because it was issued by a different
   circuit court of appeals. Hartsfield v. Lemacks, 50 F.3d 950 (11th Cir.
   1995). 2 The plaintiffs do not cite any other authority.
           In Rogers, we affirmed a grant of qualified immunity. Rogers, 271 F.
   App’x at 436. Officers secured a warrant to search a suspected drug house.
   Id. at 432. Before executing the warrant, officers drove by the target house
   to confirm its location. Id. They saw a maroon vehicle parked in front of the

           _____________________
           2
             A nonprecedential opinion “cannot be the source of clearly established law for
   qualified immunity analysis.” Marks v. Hudson, 933 F.3d 481, 486 (5th Cir. 2019).
   Nevertheless, such opinions may be used to illustrate clearly established law. Bartlett, 981
   F.3d at 341 n.105; see also Cooper v. Brown, 844 F.3d 517, 525 n.8 (5th Cir. 2016). As for
   Hartsfield, “[w]e have not previously identified the level of out-of-circuit consensus
   necessary to put the relevant question ‘beyond debate’” and to constitute clearly
   established law. Morrow v. Meachum, 917 F.3d 870, 879 (5th Cir. 2019) (quoting al-Kidd,
   563 U.S. at 741). It is unlikely that one out-of-circuit case is sufficient.




                                                8
Case: 22-10441      Document: 00517065342            Page: 9   Date Filed: 02/15/2024




                                    No. 22-10441


   target house. Id. The officers then briefed their team on the location of the
   home and developed a plan for executing the warrant. Id. The night of the
   warrant’s execution, however, the maroon vehicle was parked in front of the
   house next door to the target house. Id. Officers broke into that house before
   ultimately realizing their mistake. Id.
          We emphasized that the officers made several efforts to identify the
   correct residence, including conducting “initial surveillance of the house
   shortly before the warrant was executed, though [the officers] increased the
   chance for mistake by approaching the house in the opposite direction than
   they would use later.” Id. at 435. There were differences in appearance
   between the mistaken house and target house, but “those differences were
   less noticeable at night.” Id. Further, we acknowledged the confusion that
   arose from the fact that “a car that earlier had been thought to be in front of
   the house to be searched was instead in front of the [p]laintiffs’ home when
   the search began.” Id. “[T]he officers made reasonable efforts, though
   obviously insufficient ones, to identify the correct house.” Id.
          In Hartsfield, the Eleventh Circuit determined that an officer was not
   entitled to qualified immunity when he executed a warrant at the wrong
   residence. 50 F.3d at 956. The officer had been to the proper residence the
   day before. Id. at 951. On the day of the raid, though, he did little to ensure
   he was leading officers to the correct address:
          As it is uncontroverted that the numbers on the houses are
          clearly marked, and that the raid took place during daylight
          hours, simply checking the warrant would have avoided the
          mistaken entry. Moreover, evidence before the court showed
          that the houses were located on different parts of the street,
          separated by at least one other residence, and that their
          appearances were distinguishable.




                                             9
Case: 22-10441     Document: 00517065342            Page: 10   Date Filed: 02/15/2024




                                     No. 22-10441


   Id. at 955. “[S]earching the wrong residence when [the officer] had done
   nothing to make sure he was searching the house described in the warrant”
   violated clearly established law. Id.
          The dissent argues Hartsfield and Rogers constitute clearly established
   law that distinguishes Lewis’s actions as objectively unreasonable under the
   fair warning analysis. Even if these two nonprecedential opinions were
   indicative of clearly established law, they would not support that Lewis
   violated that law. Lewis erred, but he made significant efforts to identify the
   correct residence. As the district court summarized, Lewis
          (1) reviewed the search warrant; (2) conducted additional
          searches on the target residence through the Dallas Central
          Appraisal District website; (3) ran a computerized criminal
          history search of the occupant of the target residence; (4)
          debriefed with DEA agents twice; (5) was provided with “real-
          time intelligence that surveillance officers at the scene reported
          a truck pulling a white box trailer just pulled up in front of the
          target location and stopped;” and (6) observed the home and
          took note of the front windows, driveway, and the numbers on
          the front of the home in an attempt to confirm the residence as
          being the target location.
   To elaborate on that final point, Lewis was careful to confirm the house had
   the proper arrangement and size of windows, but only later became aware
   that those window features were shared by the plaintiffs’ home. Moreover,
   Lewis’s confusion was compounded by misleading intelligence.                When
   officers arrived, the white trailer was not parked in front of the target house.
   Lewis correctly identified that fact, but then erred in redirecting the officers.
   Lewis was far more careful than the officers in the two opinions cited to us as
   showing he violated clearly established law.
          The “central concern” when evaluating the immunity question “is
   whether the official has fair warning that his conduct violates a constitutional




                                           10
Case: 22-10441     Document: 00517065342           Page: 11   Date Filed: 02/15/2024




                                    No. 22-10441


   right.” Delaughter, 909 F.3d at 140. That means the “dispositive question
   is whether the violative nature of particular conduct is clearly established.”
   Morrow, 917 F.3d at 875 (emphasis in original) (quotation marks and citation
   omitted). Here, the plaintiffs have not cited authority demonstrating that
   Lewis’s conduct violated clearly established law.
          We REVERSE the district court’s denial of summary judgment to
   Lewis and REMAND in order for the district court to dismiss this suit.




                                         11
Case: 22-10441        Document: 00517065342               Page: 12       Date Filed: 02/15/2024




                                          No. 22-10441


   James L. Dennis, Circuit Judge, dissenting:
           I respectfully dissent from the majority opinion. The district court
   properly denied qualified immunity to Lieutenant Mike Lewis, commander
   of the Waxahachie Police Department (WPD) SWAT team. The Jimersons’
   Fourth Amendment claim against Lewis is based on his failure to take
   sufficient steps to ensure that his team executed a no-knock warrant at the
   correct address. The district court found that factual disputes as to the
   reasonableness of Lewis’ efforts to identify the target house precluded
   granting qualified immunity to Lewis. While I agree with the majority’s
   finding that there are no factual disputes as to Lewis’ actions in leading the
   SWAT team to the wrong residence, I disagree that Lewis is entitled to
   qualified immunity 1 under clearly established law.
           Based on the undisputed facts in this case, Lewis failed to use the
   intelligence he received from the Drug Enforcement Administration (DEA)
   that would have easily allowed him to direct the SWAT team to the target
   house. The DEA alerted Lewis that the house number was painted on the
   curb and affixed to a wooden pole on the deck, and that the target house was
   the thirteenth one on the block. Despite having this information, Lewis did
   not even check the number of the house before instructing the SWAT team
   to execute the warrant on the Jimersons’ home—separated from the target

           _____________________
           1
            It’s worth noting that one of our colleagues recently suggested that “the Supreme
   Court’s original justification for qualified immunity—that Congress wouldn’t have
   abrogated common-law immunities absent explicit language—is faulty because the 1871
   Civil Rights Act expressly included such language.” Rogers v. Jarrett, 63 F.4th 971, 980 (5th
   Cir. 2023) (Willett, J., concurring); see also Alexander A. Reinert, Qualified Immunity’s
   Flawed Foundation, 111 CAL. L. REV. 201, 207–08 (2023) (arguing that “the problem with
   current qualified immunity doctrine is not just that it departs from the common law
   immunity that existed when Section 1983 was enacted,” but also that “no qualified
   immunity doctrine at all should apply in Section 1983 actions, if courts stay true to the text
   adopted by the enacting Congress and other evidence of legislative intent”).




                                                12
Case: 22-10441        Document: 00517065342                Page: 13        Date Filed: 02/15/2024




                                           No. 22-10441


   house by more than one 2 residence—by deploying a flash bang, breaking all
   their front windows using the “break and rake” technique, and forcing open
   the front door. Lewis wrote in an incident report that he “believed” the
   numbers on the Jimersons’ home to be that of the target house, despite the
   fact that he admitted his view was obscured because the Jimersons “had a
   brightly glowing porch light directly above them that was causing a reflection
   on the siding of the house.” Regardless of Lewis’ ability to see the numbers
   on the home, the search warrant alerted him that the target house number
   was written on the curb in front of the house and on a wooden pole supporting
   the house—not on the front of the house like at the Jimerson residence. Even
   more glaring are the notable physical distinctions between the two houses:
   while there is a prominent wheelchair ramp that protrudes from the Jimerson
   house with railings that appear to be waist-high, the target house had no such
   ramp and featured a chain-link fence around the perimeter of the property—
   differences evident from the photographs of the target house provided to
   Lewis before the execution of the warrant.
           Though it is undisputed that Lewis violated the Jimersons’ Fourth
   Amendment rights in executing a SWAT-style entry into their home without
   a warrant, the majority finds that the Jimersons’ claim fails because the
   unlawfulness of Lewis’ actions were not clearly established law. 3 Specifically,
           _____________________
           2
            As the majority opinion acknowledges, the SWAT team initially assembled on the
   front porch of the wrong house. After Lewis recognized that the SWAT team was at the
   wrong house, he instructed the SWAT team to execute the warrant on the Jimerson
   residence, which was in the opposite direction of the target residence.
           3
               We have sometimes described the second prong of the qualified immunity
   analysis as an inquiry into whether an official’s “actions were objectively unreasonable in
   light of clearly established law.” See, e.g., Roque v. Harvel, 993 F.3d 325, 334 (5th Cir. 2021)
   (Willett, J.). The different phrasing is of no moment because, of course, violating a clearly
   established right is objectively unreasonable. See Ziglar v. Abbasi, 582 U.S. 120, 151 (2017);
   see also Anderson v. Creighton, 483 U.S. 635, 653 (1987) (“Reliance on the objective
   reasonableness of an official’s conduct, as measured by reference to clearly established




                                                 13
Case: 22-10441        Document: 00517065342              Page: 14       Date Filed: 02/15/2024




                                          No. 22-10441


   the majority concludes that there is not enough legal authority supporting the
   Jimersons’ contention that Lewis’ efforts to locate the target residence were
   constitutionally deficient. While the majority is certainly correct that “[a]
   clearly established right is one that is sufficiently clear that every reasonable
   official would have understood that what he is doing violates that right,”
   Mullenix v. Luna, 577 U.S. 7, 11 (2015), they nonetheless unfairly limit the
   legal authority the Jimersons may rely on in rebutting Lewis’ assertion of
   qualified immunity. The “focus” of the qualified immunity analysis is
   whether the officer had “fair notice” that his conduct was unlawful, and here
   the clearly established law gave Lewis ample warning of the constitutionally
   sufficient efforts required to ensure he directed the SWAT team to the
   correct residence. Brosseau v. Haugen, 543 U.S. 194, 198 (2004) (noting that
   the “focus” of qualified immunity analysis is “whether the officer had fair
   notice that her conduct was unlawful”).
           Contrary to the majority’s assertion that there is no clearly established
   law that would have put Lewis on notice of the unlawfulness of his actions,
   the Supreme Court has stated that officers must make “a reasonable effort to
   ascertain and identify the place intended to be searched within the meaning
   of the Fourth Amendment.” Maryland v. Garrison, 480 U.S. 79, 88 (1987).
   In Garrison, officers mistakenly executed a search warrant on the wrong
   apartment because they believed that the third floor of an apartment complex
   contained only one rather than two apartments. Id. There, the Supreme
   Court found that the officers made a reasonable effort to identify the correct
   apartment because “[t]he objective facts available to the officers at the time
   suggested no distinction between McWebb’s apartment and the third-floor
   premises.” Id. Specifically, those officers made a “reasonable effort” to
           _____________________
   law[.]”); Horvath v. City of Leander, 946 F.3d 787, 800 (5th Cir. 2020) (Ho, J., concurring)
   (quoting Pearson v. Callahan, 555 U.S. 222, 232 (2009)).




                                               14
Case: 22-10441     Document: 00517065342            Page: 15   Date Filed: 02/15/2024




                                     No. 22-10441


   identify the target residence where they: (1) went to the premises to see if it
   matched the description given by an informant; (2) checked with the
   Baltimore Gas and Electric Company to ascertain in whose name the third
   floor apartment was listed; and (3) checked with the Baltimore Police
   Department to make sure that the description and address of the suspect
   matched the information provided by the informant. Id. at 81–82, 85–86 n.10.
          Moreover, Hartsfield v. Lemacks, 50 F.3d 950 (11th Cir. 1995) “aptly
   illustrates the established right” at issue in the Jimersons’ claim against
   Lewis. See id. at 955 (recognizing as “clearly established law” that “absent
   probable cause and exigent circumstances, a warrantless search of a residence
   violates the Fourth Amendment, unless the officers engage in reasonable
   efforts to avoid error”); see also Cooper v. Brown, 844 F.3d 517, 525 (5th Cir.
   2016) (explaining that where a case “does not constitute clearly established
   law for purposes of QI” it may still “aptly illustrates the established right”).
   In Hartsfield, the Eleventh Circuit denied qualified immunity where an
   officer “had the warrant in his possession” yet “did not check to make sure
   he was leading the other officers to the correct address” Hartsfield, 50 F.3d
   at 955. There, the officers’ efforts to identify the target of the search warrant
   were insufficient where: (1) the numbers were clearly marked on the houses;
   (2) the houses were separated by at least one other residence; and (3) the
   houses were physically distinguishable; (4) there were no exigent
   circumstances; and (5) the raid occurred during the daytime. Id. at 952–55.
   Here, similarly, the numbers on the houses were clearly marked (despite it
   being nighttime), the houses were separated by at least one residence and
   were physically distinguishable, and there were no exigent circumstances.
   While Lewis arguably did more to identify the correct residence than the
   officer in Hartsfield, who “did nothing to make sure he was leading the
   officers to the correct residence,” Lewis nonetheless could have easily
   avoided the mistaken entry by “simply checking” the house number or using




                                          15
Case: 22-10441        Document: 00517065342              Page: 16       Date Filed: 02/15/2024




                                          No. 22-10441


   other information at his disposal to identify the correct residence. Id. at 955.
   In light of Hartsfield’s guidance interpreting the clearly established law in
   Garrison, the Jimersons rebutted Lewis’ assertion of qualified immunity.
           Our unpublished decision in Rogers v. Hooper, 271 F. App’x 431 (5th
   Cir. 2008) also supports the denial of qualified immunity to Lewis. In Rogers,
   we affirmed a grant of qualified immunity to an officer who mistakenly led his
   team to the wrong house where: (1) the two houses were next to each other;
   (2) the officer had previously been at the correct house twice; and (3) the
   minor differences between the houses were “less noticeable at night.” Here,
   in contrast, the houses were not next to each other, and Lewis could have
   easily checked the number of the target house that was painted on the curb
   and affixed to a wooden beam supporting the home’s porch. Moreover, the
   obvious physical distinctions between the houses would have been noticeable
   even at night; while the target house had a chain-link fence around it, the
   Jimerson house did not have any fence and featured a wheelchair ramp with
   waist-high railings along it. Because Lewis did not take the same steps 4 as the
   officer in Rogers to identify the correct residence, our nonprecedential case
   law supports the denial of qualified immunity.
           In light of the efforts identified as adequate by the Supreme Court in
   Garrison and elaborated on by circuit courts, Lewis had “fair notice” of the
   minimum efforts required to comply with the Fourth Amendment when
           _____________________
           4
              Notably, the officers in Rogers and Garrison each previously visited the correct
   houses as part of their efforts to identify the target of the search warrant, whereas here
   Lewis made no such attempts. See Rogers, 271 F. App’x at 433–43 (noting that the officers
   “had been at the correct house at least twice before”); Garrison, 480 U.S. at 86 n.10 (“The
   officer went to [the target residence] and found that it matched the description given by the
   informant.”). WPD Police Chief Wade Goolsby even testified that after this incident, the
   WPD implemented additional procedures requiring officers to “get[] eyes on the location
   so that [the officer] not only sees the target, but the surrounding homes” before executing
   a search warrant.




                                                16
Case: 22-10441     Document: 00517065342           Page: 17   Date Filed: 02/15/2024




                                    No. 22-10441


   identifying a house for the purposes of executing a search warrant. Brosseau,
   543 U.S. at 198; see also Hope v. Pelzer, 536 U.S. 730, 731 (2002) (“Qualified
   immunity operates to ensure that before they are subjected to suit, officers
   are on notice that their conduct is unlawful.”). As announced in Garrison and
   elucidated in Rogers and Hartsfield, it is “beyond debate” that Lewis’ efforts
   to identify the target house were constitutionally deficient. Ashcroft v. al–
   Kidd, 563 U.S. 731, 741 (2011). The panel should affirm the district court’s
   denial of Lewis’ assertion of qualified immunity.




                                         17

```

---

## GROUP: content/cases/Kansas v. Glover.md  (`case`, 6 assertions)

### content_page

```
---
title: "Kansas v. Glover"
type: case
citation: "589 U.S. 376 (2020)"
parallel_cite: "140 S. Ct. 1183; 206 L. Ed. 2d 412"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2020
date_decided: 2020-04-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2020-04-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kansas v. Glover
  varies_by_point: false
  scope_note: "Good law; an officer who learns a vehicle's registered owner has a revoked license has reasonable suspicion to stop it absent information negating the inference that the owner is driving. The Court stressed the narrow scope of the holding: additional facts (e.g., an obvious mismatch between the owner and the observed driver) can dispel that suspicion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9231313/kansas-v-glover/"
  cluster_id: 9231313
  opinion_id: 9226123
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Progeny"
  - page: "[[Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Navarette v. California]]", "[[Delaware v. Prouse]]", "[[Heien v. North Carolina]]", "[[Terry v. Ohio]]", "[[United States v. Cortez]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "reasonable-suspicion", "vehicle-stop"]
holding: "An officer who learns that a vehicle's registered owner has a revoked license has reasonable suspicion to stop the vehicle, absent information negating the inference that the owner is the driver."
lake:
  record_id: Kansas v. Glover
  status: verified
  projected_at: 2026-07-09
---

# Kansas v. Glover

*589 U.S. 376 (2020)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Kansas deputy ran the license plate of a pickup truck and learned that the registered owner, Charles Glover, had a revoked driver's license. Without observing any traffic violation and without confirming who was actually driving, the deputy stopped the truck on the assumption that the owner was behind the wheel. Glover was in fact driving and was charged as a habitual violator. The parties stipulated that the deputy stopped the truck solely because he had learned the registered owner's license was revoked; Glover moved to suppress, arguing the stop lacked reasonable suspicion.

## Issue
Whether a police officer has reasonable suspicion to initiate an investigative traffic stop where he knows the vehicle's registered owner has a revoked license and lacks any information indicating that the owner is not the one driving.

## Rule
Yes. "We hold that when the officer lacks information negating an inference that the owner is the driver of the vehicle, the stop is reasonable." — 140 S. Ct. at 1186. ^pin-1186

Reasonable suspicion is a "less demanding" standard that lets officers make "commonsense judgments and inferences about human behavior," so the everyday inference that a vehicle's registered owner is its driver — combined with the fact that the owner's license is revoked — supplies reasonable suspicion to stop.

The Court cabined the rule. "We emphasize the narrow scope of our holding." — *Id.* at 1191. ^pin-1191

Because the stop must be "justified at its inception," "the presence of additional facts might dispel reasonable suspicion" — for example, if the officer knows the registered owner is in his mid-sixties but observes that the driver is in her mid-twenties, the inference dissolves. — *Id.* ^pin-1191b

## Application
On these stipulated facts the inference held. "From these three facts, Deputy Mehrer drew the commonsense inference that Glover was likely the driver of the vehicle, which provided more than reasonable suspicion to initiate the stop." — [*Id.* at 1188](https://www.courtlistener.com/opinion/9231313/kansas-v-glover/#:~:text=From%20these%20three%20facts%2C%20Deputy). ^pin-1188

The deputy knew the plate was linked to a truck matching the one he observed and that the registered owner's license was revoked, and he possessed no [[Brady and Giglio|exculpatory]] information rebutting the inference that the owner was driving. Because nothing in the record dispelled the inference, the stop was reasonable at its inception.

## Conclusion
The traffic stop was supported by reasonable suspicion; the Kansas Supreme Court's contrary judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. An officer may stop a vehicle on the commonsense inference that its revoked-license owner is driving — unless the officer has information dispelling that inference.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Glover* applies the reasonable-suspicion framework of [[Terry v. Ohio]], [[United States v. Cortez]], and [[Navarette v. California]] to plate-derived database information, while its express "narrow scope" caveat preserves the limit that a stop must be justified at its inception and can be defeated by facts negating the owner-is-driver inference.

## Appears on
- [[Traffic Stops]] — *Progeny*
- [[Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Kansas v. Glover*, 589 U.S. 376 (2020) — https://www.courtlistener.com/opinion/9231313/kansas-v-glover/ — pinpoints (S. Ct.): 1186, 1188, 1191.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2fd084ffa9067d28", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "589 U.S. 376 (2020)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "140 S. Ct. 1183; 206 L. Ed. 2d 412", "title": "Kansas v. Glover", "year": "2020"}}
{"assertion_id": "19976c50c8c00d66", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Progeny", "title": "Kansas v. Glover"}}
{"assertion_id": "2238769683bb2944", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Kansas v. Glover"}}
{"assertion_id": "810aef11afcfbda1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer who learns that a vehicle's registered owner has a revoked license has reasonable suspicion to stop the vehicle, absent information negating the inference that the owner is the driver.", "title": "Kansas v. Glover"}}
{"assertion_id": "24341d5a5dc6e9ca", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kansas v. Glover"}}
{"assertion_id": "5a9189166cabfc89", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-04-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kansas v. Glover", "field_i_validity": "good_law", "scope_note": "Good law; an officer who learns a vehicle's registered owner has a revoked license has reasonable suspicion to stop it absent information negating the inference that the owner is driving. The Court stressed the narrow scope of the holding: additional facts (e.g., an obvious mismatch between the owner and the observed driver) can dispel that suspicion.", "title": "Kansas v. Glover", "varies_by_point": "false"}}
```

### lake record — Kansas v. Glover

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kansas v. Glover",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kansas v. Glover",
    "case_name_short": "Glover",
    "case_name_full": "KANSAS v. Charles GLOVER",
    "input_case_name": "Kansas v. Glover",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2020-04-06",
    "year": 2020,
    "docket": null,
    "cluster_id": 9231313,
    "lead_opinion_id": 9226123,
    "sibling_ids": [
      9226123,
      9226124
    ],
    "absolute_url": "/opinion/9231313/kansas-v-glover/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4742386,
        "score": 120,
        "case_name": "Kansas v. Glover"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "589 U.S. 376",
      "volume": "589",
      "reporter": "U.S.",
      "page": "376",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "140 S. Ct. 1183",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "1183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 412",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "589 U.S. 376",
        "volume": "589",
        "reporter": "U.S.",
        "page": "376",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 S. Ct. 1183",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "1183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 412",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "589 U.S. 376",
    "official_selection": {
      "court_class": "scotus",
      "selected": "589 U.S. 376",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1186",
      "page": null,
      "quote": "--- # Kansas v. Glover *589 U.S. 376 (2020)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Kansas deputy ran the license plate of a pickup truck and learned that the registered owner, Charles Glover, had a revoked driver's license. Without observing any traffic violation and without confirming who was actually driving, the deputy stopped the truck on the assumption that the owner was behind the wheel. Glover was in fact driving and was charged as a habitual violator. The parties stipulated that the deputy stopped the truck solely because he had learned the registered owner's license was revoked; Glover moved to suppress, arguing the stop lacked reasonable suspicion. ## Issue Whether a police officer has reasonable suspicion to initiate an investigative traffic stop where he knows the vehicle's registered owner has a revoked license and lacks any information indicating that the owner is not the one driving. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1191",
      "page": null,
      "quote": "so the everyday inference that a vehicle's registered owner is its driver \u2014 combined with the fact that the owner's license is revoked \u2014 supplies reasonable suspicion to stop. The Court cabined the rule.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1191b",
      "page": null,
      "quote": "justified at its inception,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1188",
      "page": null,
      "quote": "From these three facts, Deputy Mehrer drew the commonsense inference that Glover was likely the driver of the vehicle, which provided more than reasonable suspicion to initiate the stop.",
      "star_marker": "1188",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15488,
      "fragment": "#:~:text=From%20these%20three%20facts%2C%20Deputy",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-04-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kansas v. Glover",
    "varies_by_point": false,
    "scope_note": "Good law; an officer who learns a vehicle's registered owner has a revoked license has reasonable suspicion to stop it absent information negating the inference that the owner is driving. The Court stressed the narrow scope of the holding: additional facts (e.g., an obvious mismatch between the owner and the observed driver) can dispel that suspicion.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Castillo-Martinez",
          "cluster_id": 9489871,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Silveria and Travis",
          "cluster_id": 4774990,
          "cite": [
            "267 Cal. Rptr. 3d 303",
            "471 P.3d 412",
            "10 Cal. 5th 195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Taylor v. Ricky Hughes",
          "cluster_id": 6358157,
          "cite": [
            "26 F.4th 419"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janhoi Cole",
          "cluster_id": 5307612,
          "cite": [
            "21 F.4th 421"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bass",
          "cluster_id": 4881990,
          "cite": [
            "996 F.3d 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Xzavione Taylor",
          "cluster_id": 9380817,
          "cite": [
            "60 F.4th 1233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 4883758,
          "cite": [
            "997 F.3d 603"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soukaneh v. Andrzejewski",
          "cluster_id": 10038252,
          "cite": [
            "112 F.4th 107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Degenhardt v. Bintliff",
          "cluster_id": 10124683,
          "cite": [
            "117 F.4th 747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dazhan McCallister",
          "cluster_id": 6622139,
          "cite": [
            "39 F.4th 368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patterson",
          "cluster_id": 6251538,
          "cite": [
            "25 F.4th 123"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Maloney",
          "cluster_id": 4860984,
          "cite": [
            "990 F.3d 232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kendrick Brinkley",
          "cluster_id": 4805913,
          "cite": [
            "980 F.3d 377"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mayra Reyes",
          "cluster_id": 4765369,
          "cite": [
            "963 F.3d 482"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Cloud",
          "cluster_id": 4872727,
          "cite": [
            "994 F.3d 233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nathaniel Taylor",
          "cluster_id": 10274900,
          "cite": [
            "121 F.4th 590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tremayne Drakeford",
          "cluster_id": 4868158,
          "cite": [
            "992 F.3d 255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schreiner v. Hodge",
          "cluster_id": 6406532,
          "cite": [
            "504 P.3d 410"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hunter Bishop v. State of Arkansas",
          "cluster_id": 9435394,
          "cite": [
            "675 S.W.3d 869",
            "2023 Ark. 150"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shane Nault",
          "cluster_id": 6905392,
          "cite": [
            "41 F.4th 1073"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Toddrey Willie Bruce",
          "cluster_id": 4794438,
          "cite": [
            "977 F.3d 1112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Keister",
          "cluster_id": 6452593,
          "cite": [
            "2022 Ohio 856"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alkheqani",
          "cluster_id": 9421073,
          "cite": [
            "78 F.4th 707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 10048684,
          "cite": [
            "482 Md. 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kansas v. Glover:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9226123 OR 9226124) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 98,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 98,
        "triage_read": 1,
        "triage_snippet_classified": 97
      },
      "lane2_top_cited": {
        "query": "cites:(9226123 OR 9226124)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zJnM9ODI0NDQ1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%289226123+OR+9226124%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(9226123 OR 9226124)",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 1,
        "triage_snippet_classified": 71
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9226123 OR 9226124)",
    "indexed_citing_opinions": 128,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9226123,
        "count": 128,
        "count_source": "search"
      },
      {
        "opinion_id": 9226124,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 286,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kansas-v-glover.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMjgyODEmcz0xMDE0MzEzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%289226123+OR+9226124%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T09:04:51Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:05:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:05:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:08:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:05:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kansas v. Glover

```
<opinion type="majority">
<author id="p-10">Justice THOMAS delivered the opinion of the Court.</author>
<p id="p-11"><a class="page-label" data-citation-index="1" data-label="1186" href="#p1186" id="p1186">*1186</a>This case presents the question whether a police officer violates the Fourth Amendment by initiating an investigative traffic stop after running a vehicle's license plate and learning that the registered owner has a revoked driver's license. We hold that when the officer lacks information negating an inference that the owner is the driver of the vehicle, the stop is reasonable.</p>
<p id="p-12">I</p>
<p id="p-13">Kansas charged respondent Charles Glover, Jr., with driving as a habitual violator after a traffic stop revealed that he was driving with a revoked license. See <a class="page-label" data-citation-index="1" data-label="1187" href="#p1187" id="p1187">*1187</a><extracted-citation index="0" url="https://cite.case.law/citations/?q=Kan.%20Stat.%20Ann.%20%C2%A7%208-285"><span class="citation no-link">Kan. Stat. Ann. § 8-285</span></extracted-citation>(a)(3) (2001). Glover filed a motion to suppress all evidence seized during the stop, claiming that the officer lacked reasonable suspicion. Neither Glover nor the police officer testified at the suppression hearing. Instead, the parties stipulated to the following facts:</p>
<blockquote id="p-14">"1. Deputy Mark Mehrer is a certified law enforcement officer employed by the Douglas County Kansas Sheriff 's Office.</blockquote>
<blockquote id="p-15">2. On April 28, 2016, Deputy Mehrer was on routine patrol in Douglas County when he observed a 1995 Chevrolet 1500 pickup truck with Kansas plate 295ATJ.</blockquote>
<blockquote id="p-16">3. Deputy Mehrer ran Kansas plate 295ATJ through the Kansas Department of Revenue's file service. The registration came back to a 1995 Chevrolet 1500 pickup truck.</blockquote>
<blockquote id="p-17">4. Kansas Department of Revenue files indicated the truck was registered to Charles Glover Jr. The files also indicated that Mr. Glover had a revoked driver's license in the State of Kansas.</blockquote>
<blockquote id="p-18">5. Deputy Mehrer assumed the registered owner of the truck was also the driver, Charles Glover Jr.</blockquote>
<blockquote id="p-19">6. Deputy Mehrer did not observe any traffic infractions, and did not attempt to identify the driver [of] the truck. Based solely on the information that the registered owner of the truck was revoked, Deputy Mehrer initiated a traffic stop.</blockquote>
<blockquote id="p-20">7. The driver of the truck was identified as the defendant, Charles Glover Jr." App. to Pet. for Cert. 60-61.</blockquote>
<p id="p-21">The District Court granted Glover's motion to suppress. The Court of Appeals reversed, holding that "it was reasonable for [Deputy] Mehrer to infer that the driver was the owner of the vehicle" because "there were specific and articulable facts from which the officer's common-sense inference gave rise to a reasonable suspicion." <extracted-citation index="1" url="https://cite.case.law/citations/?q=54%20Kan.%20App.%202d%20377"><span class="citation no-link">54 Kan.App.2d 377</span></extracted-citation>, 385, <extracted-citation index="2" url="https://cite.case.law/citations/?q=400%20P.3d%20182"><span class="citation no-link">400 P.3d 182</span></extracted-citation>, 188 (2017).</p>
<p id="p-22">The Kansas Supreme Court reversed. According to the court, Deputy Mehrer did not have reasonable suspicion because his inference that Glover was behind the wheel amounted to "only a hunch" that Glover was engaging in criminal activity. <extracted-citation index="3" url="https://cite.case.law/citations/?q=308%20Kan.%20590"><span class="citation no-link">308 Kan. 590</span></extracted-citation>, 591, <extracted-citation case-ids="12568912,12568911" index="4" url="https://cite.case.law/p3d/422/64/"><span class="citation multiple-matches"><a href="/c/P.3d/422/64/">422 P.3d 64</a></span></extracted-citation>, 66 (2018). The court further explained that Deputy Mehrer's "hunch" involved "applying and stacking unstated assumptions that are unreasonable without further factual basis," namely, that "the registered owner was likely the primary driver of the vehicle" and that "the owner will likely disregard the suspension or revocation order and continue to drive." <em>Id.,</em> at 595-597, <extracted-citation case-ids="12568912,12568911" index="5" url="https://cite.case.law/p3d/422/64/">422 P.3d at 68-70</extracted-citation>. We granted Kansas' petition for a writ of certiorari, 587 U. S. ----, <extracted-citation case-ids="12619031,12619032,12619033,12619034,12619035,12619036" index="6" url="https://cite.case.law/s-ct/139/1445/"><span class="citation multiple-matches"><a href="/c/S.Ct./139/1445/">139 S.Ct. 1445</a></span></extracted-citation>, <extracted-citation index="7" url="https://cite.case.law/citations/?q=203%20L.%20Ed.%202d%20680"><span class="citation no-link">203 L.Ed.2d 680</span></extracted-citation> (2019), and now reverse.</p>
<p id="p-23">II</p>
<p id="p-24">Under this Court's precedents, the Fourth Amendment permits an officer to initiate a brief investigative traffic stop when he has "a particularized and objective basis for suspecting the particular person stopped of criminal activity." <em>United States v. Cortez</em> , <extracted-citation case-ids="11716341" index="8" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U.S. 411</a></span></extracted-citation>, 417-418, <extracted-citation case-ids="11716341" index="9" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">101 S.Ct. 690</a></span></extracted-citation>, <extracted-citation case-ids="11716341" index="10" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">66 L.Ed.2d 621</a></span></extracted-citation> (1981) ; see also <em>Terry v. Ohio</em> , <extracted-citation case-ids="6167798" index="11" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span></extracted-citation>, 21-22, <extracted-citation case-ids="6167798" index="12" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="13" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span></extracted-citation> (1968). "Although a mere 'hunch' does not create reasonable suspicion, the level of suspicion the standard requires is considerably less than proof of wrongdoing by a preponderance of the evidence, and obviously less than is necessary for probable cause." <em>Prado Navarette v. California</em> , <extracted-citation case-ids="12706993" index="14" url="https://cite.case.law/us/572/393/#p397"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">572 U.S. 393</a></span></extracted-citation>, 397, <extracted-citation case-ids="12579832,12706993" index="15" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation>, <extracted-citation case-ids="12579832,12706993" index="16" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">188 L.Ed.2d 680</a></span></extracted-citation> (2014) (quotation altered); <em>United States v. Sokolow</em> , <extracted-citation case-ids="605100" index="17" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1</a></span></extracted-citation>, 7, <extracted-citation case-ids="605100" index="18" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation>, <extracted-citation case-ids="605100" index="19" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">104 L.Ed.2d 1</a></span></extracted-citation> (1989).</p>
<p id="p-25"><a class="page-label" data-citation-index="1" data-label="1188" href="#p1188" id="p1188">*1188</a>Because it is a "less demanding" standard, "reasonable suspicion can be established with information that is different in quantity or content than that required to establish probable cause." <em>Alabama v. White</em> , <extracted-citation case-ids="12122945" index="20" url="https://cite.case.law/us/496/325/#p330"><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">496 U.S. 325</a></span></extracted-citation>, 330, <extracted-citation case-ids="12122945" index="21" url="https://cite.case.law/us/496/325/#p330"><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">110 S.Ct. 2412</a></span></extracted-citation>, <extracted-citation case-ids="12122945" index="22" url="https://cite.case.law/us/496/325/#p330"><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">110 L.Ed.2d 301</a></span></extracted-citation> (1990). The standard "depends on the factual and practical considerations of everyday life on which <em>reasonable and prudent men</em> , not legal technicians, act." <em>Navarette</em> , <em>supra</em> , at 402, <extracted-citation case-ids="12579832,12706993" index="23" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation> (quoting <em>Ornelas v. United States</em> , <extracted-citation case-ids="11746351" index="24" url="https://cite.case.law/us/517/690/#p695"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690</a></span></extracted-citation>, 695, <extracted-citation case-ids="11746351" index="25" url="https://cite.case.law/us/517/690/#p695"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">116 S.Ct. 1657</a></span></extracted-citation>, <extracted-citation case-ids="11746351" index="26" url="https://cite.case.law/us/517/690/#p695"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">134 L.Ed.2d 911</a></span></extracted-citation> (1996) (emphasis added; internal quotation marks omitted)). Courts "cannot reasonably demand scientific certainty ... where none exists." <em>Illinois v. Wardlow</em> , <extracted-citation case-ids="9476180" index="27" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">528 U.S. 119</a></span></extracted-citation>, 125, <extracted-citation case-ids="9476180" index="28" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">120 S.Ct. 673</a></span></extracted-citation>, <extracted-citation case-ids="9476180" index="29" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">145 L.Ed.2d 570</a></span></extracted-citation> (2000). Rather, they must permit officers to make "commonsense judgments and inferences about human behavior." <em><extracted-citation case-ids="9476180" index="30" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">Ibid.</a></span></extracted-citation></em> ; see also <em>Navarette</em> , <em>supra</em> , at 403, <extracted-citation case-ids="12579832,12706993" index="31" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation> (noting that an officer " 'need not rule out the possibility of innocent conduct' ").</p>
<p id="p-26">III</p>
<p id="p-27">We have previously recognized that States have a "vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles [and] that licensing, registration, and vehicle inspection requirements are being observed." <em>Delaware v. Prouse</em> , <extracted-citation case-ids="6187389" index="32" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span></extracted-citation>, 658, <extracted-citation case-ids="6187389" index="33" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="6187389" index="34" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L.Ed.2d 660</a></span></extracted-citation> (1979). With this in mind, we turn to whether the facts known to Deputy Mehrer at the time of the stop gave rise to reasonable suspicion. We conclude that they did.</p>
<p id="p-28">Before initiating the stop, Deputy Mehrer observed an individual operating a 1995 Chevrolet 1500 pickup truck with Kansas plate 295ATJ. He also knew that the registered owner of the truck had a revoked license and that the model of the truck matched the observed vehicle. From these three facts, Deputy Mehrer drew the commonsense inference that Glover was likely the driver of the vehicle, which provided more than reasonable suspicion to initiate the stop.</p>
<p id="p-29">The fact that the registered owner of a vehicle is not always the driver of the vehicle does not negate the reasonableness of Deputy Mehrer's inference. Such is the case with all reasonable inferences. The reasonable suspicion inquiry "falls considerably short" of 51% accuracy, see <em>United States v. Arvizu</em> , <extracted-citation case-ids="9108176" index="35" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U.S. 266</a></span></extracted-citation>, 274, <extracted-citation case-ids="9108176" index="36" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">122 S.Ct. 744</a></span></extracted-citation>, <extracted-citation case-ids="9108176" index="37" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">151 L.Ed.2d 740</a></span></extracted-citation> (2002), for, as we have explained, "[t]o be reasonable is not to be perfect," <em>Heien v. North Carolina</em> , <extracted-citation index="38" url="https://cite.case.law/citations/?q=574%20U.S.%2054"><span class="citation no-link">574 U.S. 54</span></extracted-citation>, 60, <extracted-citation case-ids="12593411" index="39" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">135 S.Ct. 530</a></span></extracted-citation>, <extracted-citation case-ids="12593411" index="40" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">190 L.Ed.2d 475</a></span></extracted-citation> (2014).</p>
<p id="p-30">Glover's revoked license does not render Deputy Mehrer's inference unreasonable either. Empirical studies demonstrate what common experience readily reveals: Drivers with revoked licenses frequently continue to drive and therefore to pose safety risks to other motorists and pedestrians. See, <em>e.g.</em> , 2 T. Neuman et al., National Coop. Hwy. Research Program Report 500: A Guide for Addressing Collisions Involving Unlicensed Drivers and Drivers With Suspended or Revoked Licenses, p. III-1 (2003) (noting that 75% of drivers with suspended or revoked licenses continue to drive); National Hwy. and Traffic Safety Admin., Research Note: Driver License Compliance Status in Fatal Crashes 2 (Oct. 2014) (noting that approximately 19% of motor vehicle fatalities from 2008-2012 "involved drivers with invalid licenses").</p>
<p id="p-31">Although common sense suffices to justify this inference, Kansas law reinforces that it is reasonable to infer that an individual with a revoked license may continue driving. The State's license-revocation scheme covers drivers who have already <a class="page-label" data-citation-index="1" data-label="1189" href="#p1189" id="p1189">*1189</a>demonstrated a disregard for the law or are categorically unfit to drive. The Division of Vehicles of the Kansas Department of Revenue (Division) "shall" revoke a driver's license upon certain convictions for involuntary manslaughter, vehicular homicide, battery, reckless driving, fleeing or attempting to elude a police officer, or conviction of a felony in which a motor vehicle is used. <extracted-citation index="41" url="https://cite.case.law/citations/?q=Kan.%20Stat.%20Ann.%20%C2%A7%C2%A7%208-254"><span class="citation no-link">Kan. Stat. Ann. §§ 8-254</span></extracted-citation>(a), 8-252. Reckless driving is defined as "driv[ing] any vehicle in willful or wanton disregard for the safety of persons or property." § 8-1566(a). The Division also has discretion to revoke a license if a driver "[h]as been convicted with such frequency of serious offenses against traffic regulations governing the movement of vehicles as to indicate a disrespect for traffic laws and a disregard for the safety of other persons on the highways," "has been convicted of three or more moving traffic violations committed on separate occasions within a 12-month period," "is incompetent to drive a motor vehicle," or "has been convicted of a moving traffic violation, committed at a time when the person's driving privileges were restricted, suspended[,] or revoked." §§ 8-255(a)(1)-(4). Other reasons include violating license restrictions, § 8-245(c), being under house arrest, § 21-6609(c), and being a habitual violator, § 8-286, which Kansas defines as a resident or nonresident who has been convicted three or more times within the past five years of certain enumerated driving offenses, § 8-285. The concerns motivating the State's various grounds for revocation lend further credence to the inference that a registered owner with a revoked Kansas driver's license might be the one driving the vehicle.</p>
<p id="p-32">IV</p>
<p id="p-33">Glover and the dissent respond with two arguments as to why Deputy Mehrer lacked reasonable suspicion. Neither is persuasive.</p>
<p id="p-34">A</p>
<p id="p-35">First, Glover and the dissent argue that Deputy Mehrer's inference was unreasonable because it was not grounded in his law enforcement training or experience. Nothing in our Fourth Amendment precedent supports the notion that, in determining whether reasonable suspicion exists, an officer can draw inferences based on knowledge gained only through law enforcement training and experience. We have repeatedly recognized the opposite. In <em>Navarette</em> , we noted a number of behaviors-including driving in the median, crossing the center line on a highway, and swerving-that as a matter of common sense provide "sound indicia of drunk driving." <extracted-citation case-ids="12706993" index="42" url="https://cite.case.law/us/572/393/#p397"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">572 U.S. at 402</a></span></extracted-citation>, <extracted-citation case-ids="12579832,12706993" index="43" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation>. In <em><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">Wardlow</a></span></em> , we made the unremarkable observation that "[h]eadlong flight-wherever it occurs-is the consummate act of evasion" and therefore could factor into a police officer's reasonable suspicion determination. <extracted-citation case-ids="9476180" index="44" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">528 U.S. at 124</a></span></extracted-citation>, <extracted-citation case-ids="9476180" index="45" url="https://cite.case.law/us/528/119/#p125"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">120 S.Ct. 673</a></span></extracted-citation>. And in <em><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">Sokolow</a></span></em> , we recognized that the defendant's method of payment for an airplane ticket contributed to the agents' reasonable suspicion of drug trafficking because we "fe[lt] confident" that "[m]ost business travelers ... purchase airline tickets by credit card or check" rather than cash. <extracted-citation case-ids="605100" index="46" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. at 8</a></span>-9</extracted-citation>, <extracted-citation case-ids="605100" index="47" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation>. So too here. The inference that the driver of a car is its registered owner does not require any specialized training; rather, it is a reasonable inference made by ordinary people on a daily basis.</p>
<p id="p-36">The dissent reads our cases differently, contending that they permit an officer to use only the common sense derived from his "experiences in law enforcement." <em>Post</em> , at 1196 (opinion of SOTOMAYOR, J.). Such a standard defies the "common <a class="page-label" data-citation-index="1" data-label="1190" href="#p1190" id="p1190">*1190</a>sense" understanding of common sense, <em>i.e.</em> , information that is accessible to people generally, not just some specialized subset of society. More importantly, this standard appears nowhere in our precedent. In fact, we have stated that reasonable suspicion is an "abstract" concept that cannot be reduced to "a neat set of legal rules," <em>Arvizu</em> , <extracted-citation case-ids="9108176" index="48" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U.S. at 274</a></span></extracted-citation>, <extracted-citation case-ids="9108176" index="49" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">122 S.Ct. 744</a></span></extracted-citation> (internal quotation marks omitted), and we have repeatedly rejected courts' efforts to impose a rigid structure on the concept of reasonableness, <em><extracted-citation case-ids="9108176" index="50" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">ibid.</a></span></extracted-citation></em> ; <em>Sokolow</em> , <extracted-citation case-ids="605100" index="51" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. at 7</a></span>-8</extracted-citation>, <extracted-citation case-ids="605100" index="52" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation>. This is precisely what the dissent's rule would do by insisting that officers must be treated as bifurcated persons, completely precluded from drawing factual inferences based on the commonly held knowledge they have acquired in their everyday lives.</p>
<p id="p-37">The dissent's rule would also impose on police the burden of pointing to specific training materials or field experiences justifying reasonable suspicion for the myriad infractions in municipal criminal codes. And by removing common sense as a source of evidence, the dissent would considerably narrow the daylight between the showing required for probable cause and the "less stringent" showing required for reasonable suspicion. <em>Prouse</em> , <extracted-citation case-ids="6187389" index="53" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. at 654</a></span></extracted-citation>, <extracted-citation case-ids="6187389" index="54" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation> ; see <em>White</em> , <extracted-citation case-ids="12122945" index="55" url="https://cite.case.law/us/496/325/#p330"><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">496 U.S. at 330</a></span></extracted-citation>, <extracted-citation case-ids="12122945" index="56" url="https://cite.case.law/us/496/325/#p330"><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">110 S.Ct. 2412</a></span></extracted-citation>. Finally, it would impermissibly tie a traffic stop's validity to the officer's length of service. See <em>Devenpeck v. Alford</em> , <extracted-citation case-ids="5916678" index="57" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146</a></span></extracted-citation>, 154, <extracted-citation case-ids="5916678" index="58" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="59" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L.Ed.2d 537</a></span></extracted-citation> (2004). Such requirements are inconsistent with our Fourth Amendment jurisprudence, and we decline to adopt them here.</p>
<p id="p-38">In reaching this conclusion, we in no way minimize the significant role that specialized training and experience routinely play in law enforcement investigations. See, <em>e.g.</em> , <em>Arvizu</em> , <extracted-citation case-ids="9108176" index="60" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">534 U.S. at 273</a></span>-274</extracted-citation>, <extracted-citation case-ids="9108176" index="61" url="https://cite.case.law/us/534/266/#p274"><span class="citation" data-id="9434181"><a href="/opinion/118474/united-states-v-arvizu/" aria-description="Citation for case: United States v. Arvizu">122 S.Ct. 744</a></span></extracted-citation>. We simply hold that such experience is not <em>required</em> in every instance.</p>
<p id="p-39">B</p>
<p id="p-40">Glover and the dissent also contend that adopting Kansas' view would eviscerate the need for officers to base reasonable suspicion on "specific and articulable facts" particularized to the individual, see <em>Terry</em> , <extracted-citation case-ids="6167798" index="62" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. at 21</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="63" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, because police could instead rely exclusively on probabilities. Their argument carries little force.</p>
<p id="p-41">As an initial matter, we have previously stated that officers, like jurors, may rely on probabilities in the reasonable suspicion context. See <em>Sokolow</em> , <extracted-citation case-ids="605100" index="64" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. at 8</a></span>-9</extracted-citation>, <extracted-citation case-ids="605100" index="65" url="https://cite.case.law/us/490/1/#p7"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation> ; <em>Cortez</em> , <extracted-citation case-ids="11716341" index="66" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U.S. at 418</a></span></extracted-citation>, <extracted-citation case-ids="11716341" index="67" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">101 S.Ct. 690</a></span></extracted-citation>. Moreover, as explained above, Deputy Mehrer did not rely exclusively on probabilities. He knew that the license plate was linked to a truck matching the observed vehicle and that the registered owner of the vehicle had a revoked license. Based on these minimal facts, he used common sense to form a reasonable suspicion that a specific individual was potentially engaged in specific criminal activity-driving with a revoked license. Traffic stops of this nature do not delegate to officers "broad and unlimited discretion" to stop drivers at random. <em>United States v. Brignoni-Ponce</em> , <extracted-citation case-ids="9550" index="68" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span></extracted-citation>, 882, <extracted-citation case-ids="9550" index="69" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">95 S.Ct. 2574</a></span></extracted-citation>, <extracted-citation case-ids="9550" index="70" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">45 L.Ed.2d 607</a></span></extracted-citation> (1975). Nor do they allow officers to stop drivers whose conduct is no different from any other driver's. See <em>Brown v. Texas</em> , <extracted-citation case-ids="6179718" index="71" url="https://cite.case.law/us/443/47/#p52"><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U.S. 47</a></span></extracted-citation>, 52, <extracted-citation case-ids="6179718" index="72" url="https://cite.case.law/us/443/47/#p52"><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">99 S.Ct. 2637</a></span></extracted-citation>, <extracted-citation case-ids="6179718" index="73" url="https://cite.case.law/us/443/47/#p52"><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">61 L.Ed.2d 357</a></span></extracted-citation> (1979). Accordingly, combining database information and commonsense judgments in this context is fully consonant with this Court's Fourth Amendment precedents.<footnotemark>1</footnotemark></p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="1191" href="#p1191" id="p1191">*1191</a>V</p>
<p id="p-43">This Court's precedents have repeatedly affirmed that " 'the ultimate touchstone of the Fourth Amendment is "reasonableness." ' " <em>Heien</em> , <extracted-citation index="74" url="https://cite.case.law/citations/?q=574%20U.S.%2054">574 U.S. at 60</extracted-citation>, <extracted-citation case-ids="12593411" index="75" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">135 S.Ct. 530</a></span></extracted-citation> (quoting <em>Riley v. California</em> , <extracted-citation index="76" url="https://cite.case.law/citations/?q=573%20U.S.%20373"><span class="citation no-link">573 U.S. 373</span></extracted-citation>, 381, <extracted-citation case-ids="12581677" index="77" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="78" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) ). Under the totality of the circumstances of this case, Deputy Mehrer drew an entirely reasonable inference that Glover was driving while his license was revoked.</p>
<p id="p-44">We emphasize the narrow scope of our holding. Like all seizures, "[t]he officer's action must be 'justified at its inception.' " <em>Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.</em> , <extracted-citation case-ids="2528582" index="79" url="https://cite.case.law/us/542/177/#p185"><span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">542 U.S. 177</a></span></extracted-citation>, 185, <extracted-citation case-ids="2528582" index="80" url="https://cite.case.law/us/542/177/#p185"><span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">124 S.Ct. 2451</a></span></extracted-citation>, <extracted-citation case-ids="2528582" index="81" url="https://cite.case.law/us/542/177/#p185"><span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">159 L.Ed.2d 292</a></span></extracted-citation> (2004) (quoting <em>United States v. Sharpe</em> , <extracted-citation case-ids="11300009" index="82" url="https://cite.case.law/us/470/675/#p682"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">470 U.S. 675</a></span></extracted-citation>, 682, <extracted-citation case-ids="11300009" index="83" url="https://cite.case.law/us/470/675/#p682"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">105 S.Ct. 1568</a></span></extracted-citation>, <extracted-citation case-ids="11300009" index="84" url="https://cite.case.law/us/470/675/#p682"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">84 L.Ed.2d 605</a></span></extracted-citation> (1985) ). "The standard takes into account the totality of the circumstances-the whole picture." <em>Navarette</em> , <extracted-citation case-ids="12706993" index="85" url="https://cite.case.law/us/572/393/#p397"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">572 U.S. at 397</a></span></extracted-citation>, <extracted-citation case-ids="12579832,12706993" index="86" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation> (internal quotation marks omitted). As a result, the presence of additional facts might dispel reasonable suspicion. See <em>Terry</em> , <em>supra</em> , at 28, <extracted-citation case-ids="6167798" index="87" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. For example, if an officer knows that the registered owner of the vehicle is in his mid-sixties but observes that the driver is in her mid-twenties, then the totality of the circumstances would not "raise a suspicion that the particular individual being stopped is engaged in wrongdoing." <em>Cortez</em> , <extracted-citation case-ids="11716341" index="88" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U.S. at 418</a></span></extracted-citation>, <extracted-citation case-ids="11716341" index="89" url="https://cite.case.law/us/449/411/#p417"><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">101 S.Ct. 690</a></span></extracted-citation> ; <em>Ornelas</em> , <extracted-citation case-ids="11746351" index="90" url="https://cite.case.law/us/517/690/#p695"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">517 U.S. at 696</a></span></extracted-citation>, <extracted-citation case-ids="11746351" index="91" url="https://cite.case.law/us/517/690/#p695"><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">116 S.Ct. 1657</a></span></extracted-citation> (" '[e]ach case is to be decided on its own facts and circumstances' " (quoting <em>Ker v. California</em> , <extracted-citation case-ids="8495" index="92" url="https://cite.case.law/us/374/23/#p33"><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U.S. 23</a></span></extracted-citation>, 33, <extracted-citation case-ids="8495" index="93" url="https://cite.case.law/us/374/23/#p33"><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">83 S.Ct. 1623</a></span></extracted-citation>, <extracted-citation case-ids="8495" index="94" url="https://cite.case.law/us/374/23/#p33"><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">10 L.Ed.2d 726</a></span></extracted-citation> (1963) )). Here, Deputy Mehrer possessed no exculpatory information-let alone sufficient information to rebut the reasonable inference that Glover was driving his own truck-and thus the stop was justified.<footnotemark>2</footnotemark></p>
<p id="p-45">* * *</p>
<p id="p-46">For the foregoing reasons, we reverse the judgment of the Kansas Supreme Court, and we remand the case for further proceedings not inconsistent with this opinion.</p>
<p id="p-47"><em>It is so ordered.</em></p>
<p id="p-48">Justice KAGAN, with whom Justice GINSBURG joins, concurring.</p>
<p id="p-49">When you see a car coming down the street, your common sense tells you that the registered owner may well be behind the wheel. See <em>ante,</em> at 1188, 1191. Not always, of course. Families share cars; friends borrow them. Still, a person often buys a vehicle to drive it himself. So your suspicion that the owner is driving would be perfectly reasonable. See <em><extracted-citation case-ids="8495" index="95" url="https://cite.case.law/us/374/23/#p33"><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">ibid.</a></span></extracted-citation></em></p>
<p id="p-50">Now, though, consider a wrinkle: Suppose you knew that the registered owner of the vehicle no longer had a valid driver's <a class="page-label" data-citation-index="1" data-label="1192" href="#p1192" id="p1192">*1192</a>license. That added fact raises a new question. What are the odds that someone who has lost his license would continue to drive? The answer is by no means obvious. You might think that a person told not to drive on pain of criminal penalty would obey the order-so that if his car was on the road, someone else (a family member, a friend) must be doing the driving. Or you might have the opposite intuition-that a person's reasons for driving would overcome his worries about violating the law, no matter the possible punishment. But most likely (let's be honest), you just wouldn't know. Especially if you've not had your own license taken away, your everyday experience has given you little basis to assess the probabilities. Your common sense can therefore no longer guide you.</p>
<p id="p-51">Even so, Deputy Mark Mehrer had reasonable suspicion to stop the truck in this case, and I join the Court's opinion holding as much. Crucially for me, Mehrer knew yet one more thing about the vehicle's registered owner, and it related to his proclivity for breaking driving laws. As the Court recounts, Mehrer learned from a state database that Charles Glover, the truck's owner, had had his license revoked under Kansas law. See <em>ante,</em> at 1187. And Kansas almost never revokes a license except for serious or repeated driving offenses. See <extracted-citation index="96" url="https://cite.case.law/citations/?q=Kan.%20Stat.%20Ann.%20%C2%A7%C2%A7%208-254"><span class="citation no-link">Kan. Stat. Ann. § 8-254</span></extracted-citation> (2001); <em>ante,</em> at 1188 -1189. Crimes like vehicular homicide and manslaughter, or vehicular flight from a police officer, provoke a license revocation; so too do multiple convictions for moving traffic violations within a short time. See <em>ante,</em> at 1188 - 1189. In other words, a person with a revoked license has already shown a willingness to flout driving restrictions. That fact, as the Court states, provides a "reason[ ] to infer" that such a person will drive without a license-at least often enough to warrant an investigatory stop. <em><extracted-citation index="97" url="https://cite.case.law/citations/?q=Kan.%20Stat.%20Ann.%20%C2%A7%C2%A7%208-254"><span class="citation no-link">Ibid.</span></extracted-citation></em> And there is nothing else here to call that inference into question. That is because the parties' unusually austere stipulation confined the case to the facts stated above-<em>i.e.,</em> that Mehrer stopped Glover's truck because he knew that Kansas had revoked Glover's license.</p>
<p id="p-52">But as already suggested, I would find this a different case if Kansas had barred Glover from driving on a ground that provided no similar evidence of his penchant for ignoring driving laws. Consider, for example, if Kansas had suspended rather than revoked Glover's license. Along with many other States, Kansas suspends licenses for matters having nothing to do with road safety, such as failing to pay parking tickets, court fees, or child support. See <extracted-citation index="98" url="https://cite.case.law/citations/?q=Kan.%20Stat.%20Ann.%20%C2%A7%208-2110"><span class="citation no-link">Kan. Stat. Ann. § 8-2110</span></extracted-citation>(b) (2018 Cum. Supp.); see also, <em>e.g.</em> , N. J. Stat. Ann. § 39:4-139.10 (West Supp. 2019) ; <extracted-citation index="99" url="https://cite.case.law/citations/?q=Ark.%20Code%20Ann.%20%C2%A7%209-14-239"><span class="citation no-link">Ark. Code Ann. § 9-14-239</span></extracted-citation> (Supp. 2019). Indeed, several studies have found that most license suspensions do not relate to driving at all; what they most relate to is being poor. See Brief for Fines and Fees Justice Center et al. as <em>Amici Curiae</em> 7. So the good reason the Court gives for thinking that someone with a revoked license will keep driving-that he has a history of disregarding driving rules-would no longer apply. And without that, the case for assuming that an unlicensed driver is at the wheel is hardly self-evident. It would have to rest on an idea about the frequency with which even those who had previously complied with driving laws would defy a State's penalty-backed command to stay off the roads. But where would that idea come from? As discussed above, I doubt whether our collective common sense could do the necessary work. See <em>supra,</em> at 1191 - 1192. Or otherwise said, I suspect that any common sense invoked in this altered context would not much differ from a "mere 'hunch' "-and so "not create reasonable suspicion."</p>
<p id="p-53"><a class="page-label" data-citation-index="1" data-label="1193" href="#p1193" id="p1193">*1193</a><em>Prado Navarette v. California</em> , <extracted-citation case-ids="12706993" index="100" url="https://cite.case.law/us/572/393/#p397"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">572 U.S. 393</a></span></extracted-citation>, 397, <extracted-citation case-ids="12579832,12706993" index="101" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">134 S.Ct. 1683</a></span></extracted-citation>, <extracted-citation case-ids="12579832,12706993" index="102" url="https://cite.case.law/s-ct/134/1683/"><span class="citation" data-id="2670795"><a href="/opinion/2670795/prado-navarette-v-california/" aria-description="Citation for case: Prado Navarette v. California">188 L.Ed.2d 680</a></span></extracted-citation> (2014) (quoting <em>Terry v. Ohio</em> , <extracted-citation case-ids="6167798" index="103" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span></extracted-citation>, 27, <extracted-citation case-ids="6167798" index="104" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="105" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span></extracted-citation> (1968) ).</p>
<p id="p-54">And even when, as under the revocation scheme here, a starting presumption of reasonable suspicion makes sense, the defendant may show that in his case additional information dictates the opposite result. The Court is clear on this point, emphasizing that under the applicable totality-of-the-circumstances test, "the presence of additional facts might dispel reasonable suspicion" even though an officer knows that a car on the road belongs to a person with a revoked license. <em>Ante,</em> at 1186; see <em>ante,</em> at 1191 (stating that further information may "negat[e] an inference that the owner is the driver of the vehicle"). Just as the Court once said of a trained drug-detection dog's "alert," the license-revocation signal is always subject to a defendant's challenge, whether through cross-examination of the officer or introduction of his own fact or expert witnesses. <em>Florida v. Harris</em> , <extracted-citation case-ids="12407425" index="106" url="https://cite.case.law/us/568/237/#p247"><span class="citation" data-id="820744"><a href="/opinion/820744/florida-v-harris/" aria-description="Citation for case: Florida v. Harris">568 U.S. 237</a></span></extracted-citation>, 247, <extracted-citation case-ids="12407425" index="107" url="https://cite.case.law/us/568/237/#p247"><span class="citation" data-id="820744"><a href="/opinion/820744/florida-v-harris/" aria-description="Citation for case: Florida v. Harris">133 S.Ct. 1050</a></span></extracted-citation>, <extracted-citation case-ids="12407425" index="108" url="https://cite.case.law/us/568/237/#p247"><span class="citation" data-id="820744"><a href="/opinion/820744/florida-v-harris/" aria-description="Citation for case: Florida v. Harris">185 L.Ed.2d 61</a></span></extracted-citation> (2013).</p>
<p id="p-55">That challenge may take any number of forms. The Court offers a clear example of observational evidence dispelling reasonable suspicion: if the officer knows the registered owner of a vehicle is an elderly man, but can see the driver is a young woman. See <em>ante,</em> at 1191. Similarly (if not as cut-and-dry), when the officer learns a car has two or more registered owners, the balance of circumstances may tip away from reasonable suspicion that the one with the revoked license is driving. And so too, the attributes of the car may be relevant. Consider if a car bears the markings of a peer-to-peer carsharing service; or compare the likelihoods that someone other than the registered owner is driving (1) a family minivan and (2) a Ferrari. The officer himself may have a wealth of accumulated information about such matters, and the defendant may probe what that knowledge suggests about the stop at issue.</p>
<p id="p-56">Such a challenge may also use statistical evidence, which is almost daily expanding in sophistication and scope. States or municipalities often keep information about "hit rates" in stops like this one-in other words, the frequency with which those stops discover unlicensed drivers behind the wheel. See generally Brief for Andrew Manuel Crespo as <em>Amicus Curiae</em> 23-27. Somewhat less direct but also useful are state and local data (collected by governments, insurance companies, and academics alike) about the average number of drivers for each registered automobile and the extent to which unlicensed persons continue to drive. See <em>id.,</em> at 13-18. (If, to use an extreme example, every car had 10 associated drivers, and losing a license reduced driving time by 90%, an officer would not have reasonable suspicion for a stop.) Here too, defendants may question testifying officers about such information. Indeed, an officer may have his own hit rate, which if low enough could itself negate reasonable suspicion. See, <em>e.g.</em> , <em>United States v. Cortez-Galaviz</em> , <extracted-citation case-ids="3563319" index="109" url="https://cite.case.law/f3d/495/1203/#p1208"><span class="citation" data-id="169558"><a href="/opinion/169558/united-states-v-cortez-galaviz/" aria-description="Citation for case: United States v. Cortez-Galaviz">495 F.3d 1203</a></span></extracted-citation>, 1208-1209 (C.A.10 2007) (Gorsuch, J.) (considering, as part of the reasonable suspicion inquiry, the frequency of an officer's misses and the accuracy of the database on which he relied).<footnotemark>*</footnotemark></p>
<p id="p-57"><a class="page-label" data-citation-index="1" data-label="1194" href="#p1194" id="p1194">*1194</a>In this strange case, contested on a barebones stipulation, the record contains no evidence of these kinds. There is but a single, simple fact: A police officer learned from a state database that a car on the road belonged to a person with a revoked license. Given that revocations in Kansas nearly always stem from serious or repeated driving violations, I agree with the Court about the reasonableness of the officer's inference that the owner, "Glover[,] was driving while his license was revoked." <em>Ante,</em> at 1191. And because Glover offered no rebuttal, there the matter stands. But that does not mean cases with more complete records will all wind up in the same place. A defendant like Glover may still be able to show that his case is different-that the "presence of additional facts" and circumstances "dispel[s] reasonable suspicion." <em>Ibid</em> . Which is to say that in more fully litigated cases, the license-revocation alert does not (as it did here) end the inquiry. It is but the first, though no doubt an important, step in assessing the reasonableness of the officer's suspicion.</p>
<footnote label="1">
<p id="p-88">The dissent contends that this approach "pave[s] the road to finding reasonable suspicion based on nothing more than a demographic profile." <em>Post</em> , at 1197 (opinion of SOTOMAYOR, J.). To alleviate any doubt, we reiterate that the Fourth Amendment requires, and Deputy Mehrer had, an individualized suspicion that a particular citizen was engaged in a particular crime. Such a particularized suspicion would be lacking in the dissent's hypothetical scenario, which, in any event, is already prohibited by our precedents. See <em>United States v. Brignoni-Ponce</em> , <extracted-citation case-ids="9550" index="110" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span></extracted-citation>, 876, <extracted-citation case-ids="9550" index="111" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">95 S.Ct. 2574</a></span></extracted-citation>, <extracted-citation case-ids="9550" index="112" url="https://cite.case.law/us/422/873/#p882"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">45 L.Ed.2d 607</a></span></extracted-citation> (1975) (holding that it violated the Fourth Amendment to stop and "question [a vehicle's] occupants [about their immigration status] when the only ground for suspicion [was] that the occupants appear[ed] to be of Mexican ancestry").</p>
</footnote>
<footnote label="2">
<p id="p-89">The dissent argues that this approach impermissibly places the burden of proof on the individual to negate the inference of reasonable suspicion. <em>Post</em> , at 3. Not so. As the above analysis makes clear, it is the information possessed by <em>the officer</em> at the time of the stop, not any information offered by the individual after the fact, that can negate the inference.</p>
</footnote>
<footnote label="*">
<p id="p-87">The syllabus constitutes no part of the opinion of the Court but has been prepared by the Reporter of Decisions for the convenience of the reader. See <em>United States v. Detroit Timber &amp; Lumber Co.</em> , <extracted-citation case-ids="8294520" index="113" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">200 U.S. 321</a></span></extracted-citation>, 337, <extracted-citation case-ids="8294520" index="114" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">26 S.Ct. 282</a></span></extracted-citation>, <extracted-citation case-ids="8294520" index="115" url="https://cite.case.law/us/200/321/#p337"><span class="citation" data-id="96405"><a href="/opinion/96405/united-states-v-detroit-timber-lumber-co/" aria-description="Citation for case: United States v. Detroit Timber &amp; Lumber Co.">50 L.Ed. 499</a></span></extracted-citation>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Lackey v. Stinnie.md  (`case`, 5 assertions)

### content_page

```
---
title: Lackey v. Stinnie
type: case
citation: "604 U.S. 192 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 23-621
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
  opinion_url: "https://www.courtlistener.com/opinion/10776869/lackey-v-stinnie/"
  cluster_id: 10776869
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lackey v. Stinnie
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - attorneys-fees
  - section-1988
  - prevailing-party
  - preliminary-injunction
holding: "A party who obtains only a preliminary injunction — with no final judgment on the merits before the case becomes moot — is not a 'prevailing party' eligible for attorney's fees under 42 U.S.C. § 1988(b), because a preliminary injunction does not conclusively resolve the merits or create a judicially sanctioned, enduring change in the parties' legal relationship."
---

# Lackey v. Stinnie

*604 U.S. 192 (2025)* (No. 23-621) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776869 → opinion 11243456; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Virginia drivers whose licenses had been suspended for unpaid court fines and costs sued state officials under 42 U.S.C. § 1983, challenging the suspension statute. They obtained a preliminary injunction barring enforcement, and Virginia then repealed the law — mooting the case before any final judgment on the merits. The drivers sought attorney's fees under 42 U.S.C. § 1988(b), which lets a court award a reasonable fee to the "prevailing party" in certain civil-rights actions. The [[Reading and Citing Cases#en-banc|en banc]] Fourth Circuit held that a plaintiff who wins a preliminary injunction can be a "prevailing party," and awarded fees.

## Issue
Whether a party who obtains a preliminary injunction, but whose case becomes moot before the court enters a final judgment, is a "prevailing party" entitled to attorney's fees under § 1988(b).

## Rule
"Prevailing party" is a legal term of art meaning the party who successfully maintains its claim "when the matter is finally set at rest" — one who obtains a judicially sanctioned, enduring change in the legal relationship of the parties. A preliminary injunction does not qualify, because it rests only on a likelihood of success and does not conclusively resolve the merits. As the Court held: "Today, we establish that the enduring nature of that change must itself be judicially sanctioned. A plaintiff who wins a transient victory on a preliminary injunction does not become a 'prevailing party' simply because external events convert the transient victory into a lasting one." — 604 U.S. at 204. ^pin-204

## Application
The drivers' preliminary injunction gave them only temporary success at an intermediary stage of the suit; it never resolved their claims on the merits, and the subsequent repeal of the statute — an external event, not a judicial decision — was what made their relief lasting. Following *Buckhannon* and *Sole v. Wyner*, the Court held that such a transient, likelihood-based victory confers no prevailing-party status, and it favored a [[Common Legal Terms#bright-line-rule|bright-line rule]] as easy to administer and protective of judicial economy. The Court rejected the drivers' textual and historical arguments that § 1988(b) contains no finality requirement.

## Conclusion
The judgment of the Fourth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Roberts, C.J., delivered the opinion of the Court, joined by Thomas, Alito, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ.; Jackson, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Sotomayor, J.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lackey* narrows the availability of § 1988(b) fee awards in § 1983 civil-rights litigation: a preliminary-injunction winner whose case is mooted before final judgment cannot recover fees, which may affect the incentives to bring and settle such suits.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Lackey v. Stinnie*, 604 U.S. 192 (2025)](https://www.courtlistener.com/opinion/10776869/lackey-v-stinnie/) — pinpoint: 204 (holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e2842f0da48a5a0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "604 U.S. 192 (2025)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Lackey v. Stinnie", "year": "2025"}}
{"assertion_id": "20dbd55e1fe8fc5e", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Lackey v. Stinnie"}}
{"assertion_id": "e35904a27730291c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A party who obtains only a preliminary injunction — with no final judgment on the merits before the case becomes moot — is not a 'prevailing party' eligible for attorney's fees under 42 U.S.C. § 1988(b), because a preliminary injunction does not conclusively resolve the merits or create a judicially sanctioned, enduring change in the parties' legal relationship.", "title": "Lackey v. Stinnie"}}
{"assertion_id": "5b5e3ff0139cfacc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lackey v. Stinnie"}}
{"assertion_id": "f14d438508f8aa3f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Lackey v. Stinnie", "varies_by_point": "false"}}
```

### lake record — Lackey v. Stinnie

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lackey v. Stinnie",
  "status": "under_review",
  "identity": {
    "case_name": "Lackey v. Stinnie",
    "case_name_short": "Lackey",
    "case_name_full": "",
    "input_case_name": "Lackey v. Stinnie",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "23-621",
    "cluster_id": 10776869,
    "lead_opinion_id": 11243456,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776869/lackey-v-stinnie/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "604 U.S. 192",
      "volume": "604",
      "reporter": "U.S.",
      "page": "192",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "604 U.S. 192",
        "volume": "604",
        "reporter": "U.S.",
        "page": "192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "604 U.S. 192",
    "official_selection": {
      "court_class": "scotus",
      "selected": "604 U.S. 192",
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
    "date_created": "2026-07-06T12:12:30Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lackey-v-stinnie--10776869",
      "to_record_id": "Lackey v. Stinnie",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lackey v. Stinnie

```
                   PRELIMINARY PRINT

              Volume 604 U. S. Part 1
                             Pages 192–225




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                             February 25, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
192                     OCTOBER TERM, 2024

                                 Syllabus


      LACKEY, COMMISSIONER OF THE VIRGINIA
        DEPARTMENT OF MOTOR VEHICLES v.
                 STINNIE et al.
certiorari to the united states court of appeals for
                 the fourth circuit
      No. 23–621. Argued October 8, 2024—Decided February 25, 2025
Drivers whose licenses were suspended under a Virginia statute for failure
 to pay court fnes sued the Commissioner of the Virginia Department
 of Motor Vehicles under 42 U. S. C. § 1983, challenging the statute as
 unconstitutional. The District Court granted a preliminary injunction
 prohibiting the Commissioner from enforcing the statute. Before trial,
 the Virginia General Assembly repealed the statute and required re-
 instatement of licenses suspended under the law. The parties then
 agreed to dismiss the pending case as moot.
    Section 1988(b) allows an award of attorney's fees to “prevailing par-
 t[ies]” under § 1983. The District Court declined to award attorney's
 fees to the drivers under that section on the ground that parties who
Page Proof Pending Publication
 obtain a preliminary injunction do not qualify as “prevailing part[ies].”
 A Fourth Circuit panel affrmed, but the Fourth Circuit reversed en
 banc. The en banc court held that some preliminary injunctions can
 provide lasting, merits-based relief and qualify plaintiffs as prevailing
 parties, even if the case becomes moot before fnal judgment.
Held: The plaintiff drivers here—who gained only preliminary injunctive
 relief before this action became moot—do not qualify as “prevailing par-
 t[ies]” eligible for attorney's fees under § 1988(b) because no court con-
 clusively resolved their claims by granting enduring judicial relief on
 the merits that materially altered the legal relationship between the
 parties. Pp. 199–208.
    (a) Under the “American Rule,” a prevailing litigant is ordinarily not
 entitled to collect attorney's fees from the loser absent express statu-
 tory authorization. See Alyeska Pipeline Service Co. v. Wilderness So-
 ciety, 421 U. S. 240, 249. Congress has provided that in actions brought
 under certain civil rights statutes—including 42 U. S. C. § 1983—“the
 court, in its discretion, may allow the prevailing party, other than the
 United States, a reasonable attorney's fee as part of the costs.”
 § 1988(b).
    To determine whether the drivers here qualify as “prevailing par-
 t[ies]” under § 1988(b), the Court begins with the statute's text. The
 Court has recognized “prevailing party” as a legal term of art. Buck-
                      Cite as: 604 U. S. 192 (2025)                      193

                                 Syllabus

 hannon Board & Care Home, Inc. v. West Virginia Dept. of Health and
 Human Resources, 532 U. S. 598, 603. When § 1988(b) was adopted,
 contemporary dictionaries defned a prevailing party as one who suc-
 cessfully maintains its claim when the matter is fnally resolved. See
 Black's Law Dictionary 1352 (rev. 4th ed. 1968); Ballentine's Law Dic-
 tionary 985 (3d ed. 1969).
    Preliminary injunctions do not make a party “prevailing” because
 they do not conclusively decide the case on the merits. Such injunc-
 tions only determine if a plaintiff is likely to succeed, along with factors
 such as irreparable harm, the balance of equities, and the public interest.
 See Winter v. Natural Resources Defense Council, Inc., 555 U. S. 7, 20.
 The purpose of a preliminary injunction is to preserve the status quo
 until a trial can occur, see University of Tex. v. Camenisch, 451 U. S.
 390, 395, and external events that render a dispute moot do not convert
 that temporary order into a conclusive adjudication. Pp. 199–202.
    (b) The Court's precedents interpreting § 1988(b) establish that a
 plaintiff “prevails” when a court grants enduring judicial relief that ma-
 terially alters the legal relationship between the parties. Two recent
 decisions emphasize that this change must be both judicially sanctioned
 and enduring. In Buckhannon, the Court rejected the “catalyst the-
 ory”—the theory that a plaintiff may receive attorney's fees under
Page Proof Pending Publication
 § 1988(b) when he “achieves the desired result because the lawsuit
 brought about a voluntary change in the defendant's conduct.” 532
 U. S., at 601. The Court explained that the plaintiff was not a “prevail-
 ing party” because there had been “no judicially sanctioned change in
 the legal relationship of the parties.” Id., at 605. And in Sole v.
 Wyner, 551 U. S. 74, the Court decided that a plaintiff initially granted
 a preliminary injunction after an abbreviated hearing, but denied a per-
 manent injunction after a adjudication on the merits, did not qualify as
 a “prevailing party” within the meaning of § 1988(b) because the plaintiff
 gained no enduring change in the legal relationship between herself and
 the defendants. Id., at 77, 78, 86. The Court's holding in this case—
 that the enduring nature of that change must itself be judicially sanc-
 tioned—follows naturally from Sole and Buckhannon. A plaintiff who
 wins a transient victory on a preliminary injunction does not become a
 “prevailing party” simply because external events convert the transient
 victory into a lasting one. Pp. 202–204.
    (c) The rule established serves the interests of judicial economy. A
 straightforward, bright-line rule is easy to administer, reducing the risk
 of signifcant litigation over attorney's fees. Concerns that government
 defendants who have lost at the preliminary injunction stage will strate-
 gically moot litigation are speculative, and such a risk could arise in only
 a small number of contexts. The judicial role here is limited. Con-
194                      LACKEY v. STINNIE

                                 Syllabus

  gress may amend the statutory language to empower courts to award
  attorney's fees to plaintiffs who have enjoyed some success but have not
  prevailed in a judgment on the merits. Pp. 204–205.
     (d) The drivers' remaining arguments are unpersuasive. The argu-
  ment that § 1988(b) was enacted against a historical backdrop that fa-
  vored awarding interim costs at equity, including for preliminary injunc-
  tions, was rejected by the Court in Alyeska Pipeline. 421 U. S., at 241,
  247. The drivers also contend that the availability of fees in some cases
  while litigation is ongoing suggests that § 1988(b) includes no fnality
  requirement, but the Court's decisions simply indicate that attorney's
  fees may be awarded when conclusive, enduring judicial relief is meted
  out on an incremental basis. Finally, the availability of fees after a
  court-ordered consent decree is consistent with the rule announced here.
  While the decree refects the parties' own resolution of the merits, it is
  approved and given force of law by a court, and it may grant enduring
  relief that materially alters the legal relationship between the parties.
  The dissent confates preliminary judicial relief that becomes irrevers-
  ible by way of mootness with relief that is permanent by virtue of a
  judicial order. Pp. 205–207.
77 F. 4th 200, reversed and remanded.

Page       Proof Pending Publication
 Roberts, C. J., delivered the opinion of the Court, in which Thomas,
Alito, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ., joined. Jack-
son, J., fled a dissenting opinion, in which Sotomayor, J., joined, post,
p. 208.

  Erika L. Maley, Solicitor General of Virginia, argued the
cause for petitioner. With her on the briefs were Jason S.
Miyares, Attorney General of Virginia, Kevin M. Gallagher,
Principal Deputy Solicitor General, Graham K. Bryant, Dep-
uty Solicitor General, M. Jordan Minot, Assistant Solicitor
General, Maya M. Eckstein, Trevor S. Cox, and David M.
Parker.
  Anthony A. Yang argued the cause for the United States
as amicus curiae urging reversal. With him on the brief
were Solicitor General Prelogar, Principal Deputy Assist-
ant Attorney General Boynton, Deputy Solicitor General
Stewart, Charles W. Scarborough, Thomas Pulham, and
Dana Kaersvang.
  Brian D. Schmalzbach argued the cause for respondents.
With him on the brief were Matthew A. Fitzgerald, John J.
                       Cite as: 604 U. S. 192 (2025)                    195

                           Opinion of the Court

Woolard, Jonathan T. Blank, Angela A. Ciolfi, and Patrick
Levy-Lavelle.*
  Chief Justice Roberts delivered the opinion of the
Court.
  Respondents are Virginia drivers whose licenses were sus-
pended due to their failure to pay court fnes or costs. The
   *Briefs of amici curiae urging reversal were fled for the State of Geor-
gia et al. by Christopher M. Carr, Attorney General of Georgia, Stephen J.
Petrany, Solicitor General, Ross W. Bergethon, Principal Deputy Solicitor
General, and Paul R. Draper, Deputy Solicitor General, and by the Attor-
neys General for their respective States as follows: Steve Marshall of Ala-
bama, Tim Griffn of Arkansas, Ashley Moody of Florida, Raúl R. Labra-
dor of Idaho, Theodore E. Rokita of Indiana, Brenna Bird of Iowa, Kris
Kobach of Kansas, Elizabeth Murrill of Louisiana, Lynn Fitch of Missis-
sippi, Andrew Bailey of Missouri, Austin Knudsen of Montana, Michael
T. Hilgers of Nebraska, Drew Wrigley of North Dakota, Dave Yost of Ohio,
Gentner Drummond of Oklahoma, Alan Wilson of South Carolina, Marty
J. Jackley of South Dakota, Jonathan Skrmetti of Tennessee, Ken Paxton
Page Proof Pending Publication
of Texas, and Sean Reyes of Utah; for the Local Government Legal Center
et al. by Joshua A. Skinner, Benjamin J. Gibbs, and Alexander J. Lind-
vall; and for the University of Florida Board of Trustees by H. Christo-
pher Bartolomucci and Justin A. Miller.
   Briefs of amici curiae urging affrmance were fled for the Alliance De-
fending Freedom et al. by Allyson N. Ho, Elizabeth A. Kiernan, Christine
A. Budasoff, John J. Bursch, Travis C. Barham, and Cynthia Fleming
Crawford; for the American Civil Liberties Union et al. by Andrew J.
Pincus; for the Christian Legal Society et al. by Douglas Laycock, John
Greil, and Steven T. Collis; for the Constitutional Accountability Center
by Elizabeth B. Wydra, Brianne J. Gorod, and Brian R. Frazelle; for the
Firearms Policy Coalition, Inc., et al. by Cody J. Wisniewski; for the First
Liberty Institute by Kelly J. Shackelford, Jeffrey C. Mateer, David J.
Hacker, Jeremiah G. Dys, and Camille P. Varone; for the Foundation for
Individual Rights and Expression et al. by Joshua A. House and Edward
S. Rudofsky; for the Institute for Free Speech et al. by Alan Gura and
Brett R. Nolan; for the Lawyers' Committee for Civil Rights Under Law
et al. by Damon T. Hewitt, Dariely Rodriguez, Ezra D. Rosenberg,
Thomas Silverstein, Pooja Chaudhuri, Angela M. Liu, and Christopher
J. Merken; and for the New Jersey State Bar Association by Gary S. Stein,
William H. Mergner, Jr., Robert B. Hille, Peter J. Gallagher, and James
A. Lewis V.
196                  LACKEY v. STINNIE

                      Opinion of the Court

drivers sued the Commissioner of the Virginia Department
of Motor Vehicles under 42 U. S. C. § 1983, arguing that the
Virginia statute requiring suspension of their licenses was
unconstitutional. The District Court preliminarily enjoined
the Commissioner from enforcing the statute. But before
the case reached fnal judgment, the Virginia General As-
sembly repealed the challenged law, rendering the action
moot. The question presented is whether the drivers are
“prevailing part[ies]” who qualify for an award of attorney's
fees under § 1988(b).
                             I
   Until recently, a Virginia statute directed the state courts
to suspend the license of any driver who failed to pay “any
fne, costs, forfeitures, restitution, or penalty lawfully as-
sessed against him” for violation of a federal, state, or local
law. Va. Code Ann. § 46.2–395(B) (2016) (repealed 2020).
The suspension remained in force until the amount due was
Page Proof Pending Publication
paid in full or the driver entered into a court-approved pay-
ment plan. Virginia drivers—whose licenses were sus-
pended under the law and who asserted that they could not
afford to pay the fnes or costs or keep up with a payment
plan—sued the Commissioner of the Virginia Department of
Motor Vehicles on their own behalf and on behalf of a puta-
tive class. The drivers alleged that the statute facially vio-
lated the Due Process Clause by “failing to provide suffcient
notice or hearing to any driver before license suspension”
and violated both the Due Process and Equal Protection
Clauses “as applied to people who cannot afford to pay due
to their modest fnancial circumstances.” First Amended
Class Action Complaint in Stinnie v. Holcomb, No.
3:16−cv−00044 (WD Va., Sept. 11, 2018), ECF Doc. 84, pp.
2−3; see also id., at 37−43. The drivers sought declaratory
relief, preliminary and permanent injunctive relief, and at-
torney's fees under 42 U. S. C. § 1988(b).
   In December 2018, the District Court granted a prelimi-
nary injunction, prohibiting the Commissioner from enforc-
                   Cite as: 604 U. S. 192 (2025)            197

                      Opinion of the Court

ing the statute against the drivers or future class members.
See Stinnie v. Holcomb, 355 F. Supp. 3d 514, 520 (WD Va.
2018). The court explained that the drivers had made “a
clear showing that [they were] likely to succeed” on their
procedural due process claim, though it noted that they need
not “establish a certainty of success.” Id., at 527 (quoting
Di Biase v. SPX Corp., 872 F. 3d 224, 230 (CA4 2017)). The
court also determined that the remaining preliminary injunc-
tion factors—the risk of irreparable harm, the balance of eq-
uities, and the public interest—weighed in the drivers' favor.
Stinnie, 355 F. Supp. 3d, at 532; see Winter v. Natural Re-
sources Defense Council, Inc., 555 U. S. 7, 20 (2008). The
Commissioner did not appeal the grant of the preliminary
injunction.
   In April 2019, about four months before a bench trial was
scheduled to begin, the Commissioner moved to dismiss as
moot or, in the alternative, stay the case. See Stinnie v.
Page Proof Pending Publication
Holcomb, 396 F. Supp. 3d 653, 656 (WD Va.). The Virginia
General Assembly had recently adopted Budget Amendment
No. 33, which “eliminate[d] the suspension of drivers' li-
censes for failure to pay court fnes and costs through July
1, 2020, but [did] not repeal § 46.2–395.” Ibid. The Com-
missioner represented that the General Assembly was likely
to repeal the law during the next legislative session. The
District Court granted a stay, reasoning in part that doing
so served the interests of judicial economy and enabled the
court to avoid “weigh[ing] in on sensitive constitutional ques-
tions about license suspension schemes about which other
courts ha[d] disagreed.” Id., at 660.
   In April 2020, the Virginia General Assembly repealed
§ 46.2–395 and required the permanent reinstatement of li-
censes suspended under the law. See 2020 Va. Acts ch. 965.
As a result, the parties agreed that the action had become
moot and stipulated to dismissal. The drivers, however, as-
serted that they were entitled to attorney's fees under
§ 1988(b), so the parties jointly requested that the court re-
198                  LACKEY v. STINNIE

                      Opinion of the Court

tain jurisdiction to resolve that dispute. The District Court
declined to award attorney's fees, following Smyth v. Rivero,
282 F. 3d 268 (CA4 2002). See Stinnie v. Holcomb, 2021 WL
2292807 (WD Va., June 4, 2021). In Smyth the Fourth Cir-
cuit held that a plaintiff awarded a preliminary injunction is
not a “prevailing party” within the meaning of § 1988(b).
282 F. 3d, at 277. A Fourth Circuit panel affrmed, again
relying on Smyth. Stinnie v. Holcomb, 37 F. 4th 977 (2022).
Judge Harris concurred, suggesting that the Circuit may
wish to reconsider that precedent. Id., at 983.
   The Fourth Circuit did so, rehearing the case en banc and
overturning its decision in Smyth. Stinnie v. Holcomb, 77
F. 4th 200 (2023). It observed that Smyth had become the
“outlier” among the courts of appeals. 77 F. 4th, at 209. It
reasoned that some preliminary injunctions “provide endur-
ing, merits-based relief that satisfes all the requisites of the
prevailing party standard.” Id., at 203. And it explained,
Page Proof Pending Publication
in light of this Court's decision in Winter v. Natural Re-
sources Defense Council, that a plaintiff could no longer pre-
vail on a preliminary injunction for reasons that “had virtu-
ally nothing to do with the merits of her claim.” 77 F. 4th,
at 208−209; see Winter, 555 U. S., at 20 (clarifying that a
fnding of likely success on the merits is a prerequisite to
preliminary injunctive relief). Finally, it noted that Con-
gress had enacted § 1988(b) in the interest of facilitating the
redress of civil rights grievances. 77 F. 4th, at 210.
   The en banc court articulated a new standard: “When a
preliminary injunction provides the plaintiff concrete, irre-
versible relief on the merits of her claim and becomes moot
before fnal judgment because no further court-ordered as-
sistance proves necessary, the subsequent mootness of the
case does not preclude an award of attorney's fees.” Ibid.
Applying that standard, the en banc court vacated and re-
manded the case to allow the District Court to determine a
reasonable fee. Id., at 218. Judge Quattlebaum dissented,
arguing that a preliminary injunction does not constitute a
                   Cite as: 604 U. S. 192 (2025)            199

                      Opinion of the Court

judicial decision on the merits and that a fee award on the
basis of such an injunction therefore conficts with both the
text of § 1988(b) and this Court's precedents. See id., at 225,
227, 231.
  We granted certiorari to determine whether the term
“prevailing party” in § 1988(b) encompasses a party who is
awarded a preliminary injunction, if the case becomes moot
before the court reaches a fnal judgment. 601 U. S. 1161
(2024).
                               II
   Since 1796, this Court has maintained that “the Judiciary
itself would not create a general rule, independent of any
statute, allowing awards of attorneys' fees in federal courts.”
Alyeska Pipeline Service Co. v. Wilderness Society, 421 U. S.
240, 249 (1975) (citing Arcambel v. Wiseman, 3 Dall. 306
(1796)). The principle that “the prevailing litigant is ordi-
narily not entitled to collect a reasonable attorneys' fee from
Page Proof Pending Publication
the loser” became known as the “American Rule.” Alyeska
Pipeline, 421 U. S., at 247. Federal courts may depart from
this rule only when “there is express statutory authoriza-
tion” to do so. Hensley v. Eckerhart, 461 U. S. 424, 429
(1983).
   In 1976, Congress adopted the Civil Rights Attorney's
Fees Awards Act. 90 Stat. 2641. The law provides that, in
actions brought under certain civil rights statutes—includ-
ing 42 U. S. C. § 1983—“the court, in its discretion, may allow
the prevailing party, other than the United States, a reason-
able attorney's fee as part of the costs.” § 1988(b). The
question is whether the drivers in this case qualify as “pre-
vailing part[ies]” within the meaning of § 1988(b).

                                A
  When interpreting a statute, we begin with the text. As
we have previously recognized, the phrase “prevailing party”
in § 1988(b) is a “legal term of art.” Buckhannon Board &
Care Home, Inc. v. West Virginia Dept. of Health and
200                  LACKEY v. STINNIE

                      Opinion of the Court

Human Resources, 532 U. S. 598, 603 (2001). We assume
that “when Congress `borrows terms of art in which are ac-
cumulated the legal tradition and meaning of centuries of
practice, it presumably knows and adopts the cluster of ideas
that were attached to each borrowed word.' ” United States
v. Hansen, 599 U. S. 762, 774 (2023) (quoting Morissette v.
United States, 342 U. S. 246, 263 (1952)).
   At the time § 1988(b) was adopted, Black's Law Dictionary
defned “prevailing party” as the party “who successfully
prosecutes the action or successfully defends against it.”
Black's Law Dictionary 1352 (rev. 4th ed. 1968). It ex-
plained that prevailing party status “does not depend upon
the degree of success at different stages of the suit, but
whether, at the end of the suit, or other proceeding, the
party who has made a claim against the other, has success-
fully maintained it.” Ibid.; accord, Ballentine's Law Dic-
tionary 985 (3d ed. 1969). A prevailing party, in other
Page Proof Pending Publication
words, is “[t]he party ultimately prevailing when the matter
is fnally set at rest.” Black's Law Dictionary 1352.
   Preliminary injunctions, however, do not conclusively re-
solve legal disputes. In awarding preliminary injunctions,
courts determine if a plaintiff is likely to succeed on the mer-
its—along with the risk of irreparable harm, the balance of
equities, and the public interest. Winter, 555 U. S., at 20.
“The purpose of a preliminary injunction is merely to pre-
serve the relative positions of the parties until a trial on the
merits can be held,” University of Tex. v. Camenisch, 451
U. S. 390, 395 (1981), and “to balance the equities as the liti-
gation moves forward,” Trump v. International Refugee As-
sistance Project, 582 U. S. 571, 580 (2017) (per curiam).
“Crafting a preliminary injunction is an exercise of discre-
tion and judgment, often dependent as much on the equities
of a given case as the substance of the legal issues it pre-
sents.” Id., at 579. Such relief is also “customarily granted
on the basis of procedures that are less formal and evidence
that is less complete than in a trial on the merits.” Camen-
                   Cite as: 604 U. S. 192 (2025)            201

                      Opinion of the Court

isch, 451 U. S., at 395. As a result, we have previously cau-
tioned against “improperly equat[ing] `likelihood of success'
with `success' ” and treating preliminary injunctions as “tan-
tamount to decisions on the underlying merits.” Id., at 394.
   The transient nature of preliminary injunctions is most ap-
parent when a court reaches a different conclusion upon full
consideration of the merits. For example, in one of our
more recent cases interpreting § 1988, Sole v. Wyner, 551
U. S. 74, 78–79 (2007), protesters sought a preliminary in-
junction against a state regulation of beach attire in order
to assemble nude in the form of a peace sign. The day after
the complaint was fled, the District Court held a hearing
and granted the preliminary injunction. Id., at 79. The
preliminary injunction permitted the protest to occur and
thus preserved the participants' rights until a fnal determi-
nation could be made on the merits of their claim. Ulti-
mately, however, the court declined to award a permanent
Page Proof Pending Publication
injunction, ruling that the regulation was no more burden-
some than necessary to protect the public. Id., at 80−81.
   Because preliminary injunctions do not conclusively re-
solve the rights of parties on the merits, they do not confer
prevailing party status. A plaintiff who secures a prelimi-
nary injunction has achieved only temporary success at an
intermediary “stage[ ] of the suit.” Black's Law Dictionary
1352. It cannot yet be said that he will “ultimately prevail[ ]
when the matter is fnally set at rest” or that he will have
“successfully maintained” his claim “at the end.” Ibid.
And external events that render a dispute moot do not con-
vert a temporary order designed to preserve the status of
the parties into a conclusive adjudication of their rights.
   The Fourth Circuit en banc was persuaded that “Winter's
stringent merits requirement” avoided the “risk” that “a
plaintiff may prevail, and thus be entitled to fees, based on
a preliminary injunction that had virtually nothing to do
with the merits of her claim.” 77 F. 4th, at 209. But it is
not enough that Winter guarantees a preliminary injunction
202                  LACKEY v. STINNIE

                      Opinion of the Court

award has at least something to do with the merits. The
plaintiff must succeed on the merits.

                               B
   This conclusion is consistent with our precedents inter-
preting § 1988(b). We have held that, for the purposes of
§ 1988(b), a plaintiff “prevails” when a court grants enduring
judicial relief that constitutes a “material alteration of the
legal relationship of the parties.” Texas State Teachers
Assn. v. Garland Independent School Dist., 489 U. S. 782,
792−793 (1989). For example, we have ruled that a plaintiff
may qualify as a “prevailing party” based on an award of
nominal damages, Farrar v. Hobby, 506 U. S. 103, 112 (1992),
or a fnal victory on a material even if not predominant claim,
Texas State Teachers Assn., 489 U. S., at 791−793. By con-
trast, a party does not qualify as a “prevailing party” when
a court of appeals overturns directed verdicts and discovery
Page Proof Pending Publication
orders entered against him, Hanrahan v. Hampton, 446 U. S.
754, 756 (1980) (per curiam), or when a court enters a declar-
atory judgment but does not modify the defendant's behavior
toward the plaintiff, Rhodes v. Stewart, 488 U. S. 1, 3−4
(1988) (per curiam) (holding that no fees were available
under § 1988 when the judgment afforded no relief to the
plaintiff due to mootness).
   Two of our more recent decisions highlight the require-
ments that the change in legal relationship be judicially sanc-
tioned and enduring. In Buckhannon Board & Care Home,
Inc. v. West Virginia Department of Health and Human Re-
sources, we rejected the “catalyst theory”—the theory that
a plaintiff may receive attorney's fees under § 1988(b) when
he “achieves the desired result because the lawsuit brought
about a voluntary change in the defendant's conduct.” 532
U. S., at 601; see id., at 600. In that context, we explained
that the plaintiff was not a “prevailing party” because there
had been “no judicially sanctioned change in the legal rela-
tionship of the parties.” Id., at 605. The defendant's volun-
                   Cite as: 604 U. S. 192 (2025)            203

                      Opinion of the Court

tary actions “lack[ed] the necessary judicial imprimatur.”
Ibid. We were not persuaded that § 1988(b) “authorizes fed-
eral courts to award attorney's fees to a plaintiff who” fled
a “potentially meritless lawsuit” and “reached the `sought-
after destination' without obtaining any judicial relief.” Id.,
at 606 (quoting id., at 634 (Ginsburg, J., dissenting)).
   In Sole v. Wyner, we decided that “a plaintiff who gain[ed]
a preliminary injunction after an abbreviated hearing, but
[was] denied a permanent injunction after a dispositive adju-
dication on the merits,” did not qualify as a “prevailing
party” within the meaning of § 1988(b). 551 U. S., at 77; see
id., at 78. That plaintiff, we explained, “gained no enduring
change in the legal relationship” between herself and the de-
fendants. Id., at 86 (emphasis added; alterations and inter-
nal quotation marks omitted). Although we left open the
question presented in this case, see ibid., we described the
plaintiff's success at the preliminary injunction stage as
Page Proof Pending Publication
“a transient victory at the threshold of an action,” a “feeting
success” that “did not establish that [the plaintiff] prevailed
on the gravamen of her plea for injunctive relief,” one
“tentative [in] character, in view of the continuation of the
litigation to defnitively resolve the controversy,” id., at 78,
83, 84.
   We recognize that neither opinion resolves this case, but
our holding today follows naturally from these precedents.
In Sole, we established that the change in the legal rela-
tionship between the parties must be “enduring.” Id., at
86. In Buckhannon, we established that the change must
be “judicially sanctioned.” 532 U. S., at 605. Today, we
establish that the enduring nature of that change must itself
be judicially sanctioned. A plaintiff who wins a transient
victory on a preliminary injunction does not become a
“prevailing party” simply because external events convert
the transient victory into a lasting one. Rather, a plaintiff
“prevails” under the statute when a court conclusively re-
solves a claim by granting enduring judicial relief on the
204                      LACKEY v. STINNIE

                          Opinion of the Court

merits that materially alters the legal relationship between
the parties.*
                              C
   The rule we establish today also serves the interests of
judicial economy. A straightforward, bright-line rule is
easy to administer, reducing the risk of “a second major liti-
gation” over attorney's fees. Cf. Hensley, 461 U. S., at 437.
The drivers, however, suggest that our rule promotes sim-
plicity at the cost of creating perverse incentives. They fear
that government defendants who have lost at the prelimi-
nary injunction stage will strategically moot litigation rather
than risk a fee award were they to ultimately lose on the
merits. See Brief for Respondents 42−47. We found simi-
lar concerns to be “entirely speculative” when we rejected
the catalyst theory in Buckhannon, 532 U. S., at 608. We
reiterate that such risk could arise in only a small number of
contexts. After all, if a plaintiff “has a cause of action for
Page Proof Pending Publication
damages, a defendant's change in conduct will not moot the
case.” Id., at 609. And even if the plaintiff seeks only in-
junctive relief, voluntary cessation of the challenged conduct
does not moot an action “unless it is `absolutely clear that
the allegedly wrongful behavior could not reasonably be ex-
pected to recur.' ” Ibid. (quoting Friends of the Earth, Inc.
v. Laidlaw Environmental Services (TOC), Inc., 528 U. S.
167, 189 (2000)); see also FBI v. Fikre, 601 U. S. 234, 241
(2024) (characterizing this burden as “formidable” (quoting
Friends of the Earth, 528 U. S., at 190)). A survey asking
public interest organizations to self-report on the impact of

   *A different body of caselaw addresses when a defendant is a “prevail-
ing party” for the purposes of other fee-shifting statutes. Our decision
today should not be read to affect our previous holding that a defendant
need not obtain a favorable judgment on the merits to prevail, nor to
address the question we left open of whether a defendant must obtain a
preclusive judgment in order to prevail. See CRST Van Expedited, Inc.
v. EEOC, 578 U. S. 419, 431−434 (2016). As we have explained, “[p]lain-
tiffs and defendants come to court with different objectives.” Id., at 431.
                   Cite as: 604 U. S. 192 (2025)            205

                      Opinion of the Court

Buckhannon does not change our minds. See post, at 224
(Jackson, J., dissenting).
   It is Congress's job to craft policy and ours to interpret
the words that codify it. “Atextual judicial supplementation
is particularly inappropriate when . . . Congress has shown
that it knows how to adopt the omitted language or provi-
sion.” Rotkiske v. Klemm, 589 U. S. 8, 14 (2019). Congress
has shown that it knows how to empower courts to award
attorney's fees to plaintiffs who have enjoyed some success
but have not prevailed in a judgment on the merits. In the
Freedom of Information Act, for example, Congress author-
ized courts to assess attorney's fees when a complainant has
“substantially prevailed,” even if through “a voluntary or
unilateral change in position by the agency.” 5 U. S. C.
§ 552(a)(4)(E). If Congress determines that the rule we
adopt today is unwise, it may amend the statutory lan-
guage—just as it enacted § 1988(b) itself in response to our
decision in Alyeska Pipeline Service Co. v. Wilderness Soci-
Page Proof Pending Publication
ety. 421 U. S. 240; see Hensley, 461 U. S., at 429. Until
then, “it is of course our job to apply faithfully the law Con-
gress has written.” Henson v. Santander Consumer USA
Inc., 582 U. S. 79, 89 (2017).

                                D
   The drivers urge the opposite conclusion, but we fnd their
arguments unpersuasive.
   First, the drivers, joined by the dissent, argue that the
dictionary defnitions support them. But they assume that
the favorable resolution of a dispute is tantamount to success
on a claim in a legal action. A “prevailing party,” however,
is defned in the latter sense—one who “successfully prose-
cutes the action,” who has “made a claim” against another
and “has successfully maintained it.” Black's Law Diction-
ary 1352.
   Second, the drivers and dissent contend that § 1988(b) was
enacted against a historical backdrop that favored awarding
206                  LACKEY v. STINNIE

                      Opinion of the Court

interim costs at equity, including for preliminary injunctions.
See Brief for Respondents 19−21. The dissent in Alyeska
Pipeline similarly invoked “the well-established power of
federal equity courts to award attorneys' fees when the in-
terests of justice so require.” 421 U. S., at 272 (Marshall,
J., dissenting). We rejected that argument, however, and
determined that the American Rule supplied the default rule
at law and equity, subject to narrow historical exceptions not
at issue here. See id., at 241, 247 (majority opinion).
   Next, the drivers argue that the availability of fees while
litigation is ongoing suggests that § 1988(b) includes no fnal-
ity requirement. See Brief for Respondents 40−42. The
dissent likewise points to our statement in Buckhannon that
a “ `prevailing party' is not intended to be limited to the vic-
tor only after entry of a fnal judgment following a full trial
on the merits.” 532 U. S., at 607 (quoting H. R. Rep. No.
94–1558, p. 7 (1976)); see post, at 221. We have recognized
Page Proof Pending Publication
that “Congress contemplated the award of fees pendente lite
in some cases.” Hanrahan, 446 U. S., at 757. For example,
we have explained that, in school desegregation cases, “many
fnal orders may issue in the course of the litigation” because
injunctive relief “must prove its effcacy . . . over a period
of time and often with frequent modifcations.” Bradley v.
School Bd. of Richmond, 416 U. S. 696, 723 (1974). Our deci-
sions simply indicate that attorney's fees may be awarded
when conclusive, enduring judicial relief is meted out on an
incremental basis. Hanrahan, 446 U. S., at 758 (“Congress
intended to permit the interim award of counsel fees only
when a party has prevailed on the merits of at least some of
his claims.”). Key language on which the dissent relies—
our statement that a party prevails when it “succeed[s] on
any signifcant claim affording it some of the relief sought,”
including relief on the merits pendente lite—explained our
rejection of the “central issue test,” which would have re-
quired a party to prevail on its central claim in order to be
awarded attorney's fees. Texas State Teachers Assn., 489
                   Cite as: 604 U. S. 192 (2025)           207

                      Opinion of the Court

U. S., at 791; see post, at 211. It did not refer to prelimi-
nary relief.
   The availability of fees following the entry of a court-
ordered consent decree is fully consistent with the rule we
announce today. A consent decree refects the parties' own
resolution of the merits, but it is approved and given force
of law by the court. See Firefghters v. Cleveland, 478 U. S.
501, 523 (1986). Violation of a consent decree is enforceable
by a citation for contempt. Ibid. So a consent decree is
like a fnal judgment in the relevant ways: It conclusively
resolves the claim, bears a judicial imprimatur, and may
grant enduring relief that materially alters the legal re-
lationship between the parties. That is why “[w]e have only
awarded attorney's fees where the plaintiff has received
a judgment on the merits or obtained a court-ordered con-
sent decree.” Buckhannon, 532 U. S., at 605 (citation omit-
ted). For its part, the dissent confates preliminary judicial
relief that becomes irreversible by way of mootness with re-
Page Proof Pending Publication
lief that is permanent by virtue of a judicial order. See
post, at 217−218. That a preliminary order may sometimes
“function[ ] . . . like” a fnal order due to external circum-
stances, see post, at 218, is not dispositive of the nature of
the order.
                           *    *    *
   Section 1988(b) permits courts to award attorney's fees to
a “prevailing party.” A party “prevails” when a court con-
clusively resolves his claim by granting enduring relief on
the merits that alters the legal relationship between the par-
ties. Critically, both the change in relationship and its per-
manence must result from a judicial order. A preliminary
injunction, which temporarily preserves the parties' litigat-
ing positions based in part on a prediction of the likelihood
of success on the merits, does not render a plaintiff a “pre-
vailing party.” Nor do external events that moot the action
and prevent the court from conclusively adjudicating the
claim. Because the drivers in the present case gained only
208                   LACKEY v. STINNIE

                      Jackson, J., dissenting

preliminary injunctive relief before this action became moot,
they do not qualify as “prevailing part[ies]” eligible for attor-
ney's fees under § 1988(b).
  The judgment of the Court of Appeals for the Fourth Cir-
cuit is reversed, and the case is remanded for further pro-
ceedings consistent with this opinion.
                                               It is so ordered.

  Justice Jackson, with whom Justice Sotomayor joins,
dissenting.
   Congress has authorized courts to award attorney's fees
to the “prevailing party” in certain civil rights cases. 42
U. S. C. § 1988(b). Today, the Court holds that a plaintiff
who secures a preliminary injunction does not “prevail”
under this fee-shifting statute, even when the preliminary
injunction provides meaningful relief and is never reversed
on the merits. The Court maintains that this holding “fol-
Page Proof Pending Publication
lows naturally from” our precedents. Ante, at 203. But
that will come as a surprise to the 11 Courts of Appeals that
have previously considered this issue; all of them agree that
at least some preliminary injunctions trigger fee eligibility
under § 1988(b).
   Stated simply, the majority's categorical preclusion of fee
awards for any plaintiff who successfully obtains preliminary
injunctive relief is unwarranted. It lacks any basis in the
text of § 1988(b) and is plainly inconsistent with that statu-
tory provision's clear objective, which is to encourage attor-
neys to fle civil rights actions on behalf of the most vulnera-
ble people in our society. The Court has now eliminated fee
eligibility for all preliminary injunctions—even those that
effectively resolve the case. But if Congress had meant for
“prevailing party” status to hinge entirely on the “conclu-
sive” nature of a judicial order, it could easily have said so.
It is the role of Congress, not this Court, to weigh concerns
about administrative ease against the benefts of guaran-
                   Cite as: 604 U. S. 192 (2025)             209

                      Jackson, J., dissenting

teeing individuals an opportunity to vindicate their civil
rights.
  There is no persuasive reason to believe that Congress
meant to preclude fee awards for every plaintiff who secures
preliminary injunctive relief but not a fnal judgment, no
matter the context. Therefore, I respectfully dissent.

                                I
                                A
   Nothing in § 1988(b)'s text compels the conclusion that a
plaintiff who obtains preliminary injunctive relief is never
eligible for a fee award. Section 1988(b) states simply that,
in actions to enforce certain civil rights statutes, including
42 U. S. C. § 1983, “the court, in its discretion, may allow the
prevailing party, other than the United States, a reasonable
attorney's fee as part of the costs.” § 1988(b). The major-
ity recognizes that “prevailing party” is a legal term of art
Page Proof Pending Publication
and begins its analysis by asserting that this term means
what legal dictionaries said it meant at the time that
§ 1988(b) was enacted.
   According to the majority's preferred dictionary, a “pre-
vailing party” is one “ `who successfully prosecutes the action
or successfully defends against it.' ” Ante, at 200 (quoting
Black's Law Dictionary 1352 (rev. 4th ed. 1968)). Thus, pre-
vailing party status turns on “ `whether, at the end of the
suit, or other proceeding, the party who has made a claim
against the other, has successfully maintained it.' ” Ante,
at 200 (quoting Black's Law Dictionary, at 1352). Reasoning
from this defnition, the majority holds that preliminary in-
junctions, which provide interim relief by their nature, can
never confer prevailing party status because they do not
“conclusively resolve the rights of parties on the merits.”
Ante, at 201.
   But the majority's analysis inexplicably confates the re-
quirement for success when the suit ends (which is what the
dictionary defnition says) with a requirement that the suit
210                  LACKEY v. STINNIE

                      Jackson, J., dissenting

end by virtue of a “conclusive” judicial ruling on the merits
of the plaintiff's claims (which is nowhere in Black's Law
Dictionary or anywhere else). In other words, the majori-
ty's reasoning elides the fact that a suit can end in various
ways—including through acts of the defendant or others that
moot the legal action. Black's Law Dictionary and its con-
temporaries simply require a court determining eligibility
for a fee award to take stock of where things stand at the end
of the lawsuit. A prevailing party for § 1988(b) purposes is
one who has successfully maintained his claim (in the manner
I describe below, see Part II–A, infra) “when the matter is
fnally set at rest.” Black's Law Dictionary, at 1352.
   In essence, then, the majority errs by assuming that the
only kind of resolution to a suit that can precipitate a fee
award is a “conclusive” fnal judgment on the merits. See,
e. g., ante, at 200–201, 203, 206. That assumption is un-
founded. The text of the fee statute does not require a fnal
Page Proof Pending Publication
judgment in the party's favor, “conclusive” or otherwise.
Nor does any dictionary defnition of “prevailing party” to
which the majority cites. Rather, according to Black's Law
Dictionary, a “prevailing party” is simply a “part[y] to a suit
who successfully prosecutes the action or successfully de-
fends against it, prevailing on the main issue, even though
not to the extent of his original contention.” Black's Law
Dictionary, at 1352. Ballentine's Law Dictionary is substan-
tially similar; it defnes “prevailing party” as “[t]he party
who is successful or partially successful in an action, so as to
be entitled to costs.” Ballentine's Law Dictionary 985 (3d
ed. 1969).
   Signifcantly for present purposes, both dictionaries fur-
ther emphasize that “[t]o be [a prevailing party] does not de-
pend upon the degree of success at different stages of the
suit, but whether, at the end of the suit . . . the party who
has made a claim against the other, has successfully main-
tained it.” Black's Law Dictionary, at 1352; accord, Ballen-
tine's Law Dictionary, at 985. Yet, today, the majority de-
                       Cite as: 604 U. S. 192 (2025)                    211

                          Jackson, J., dissenting

mands that, in order to prevail, the party must have achieved
a certain degree of success at a certain point in the case: a
conclusive fnal judgment in his favor at the end of litigation.

                                    B
   This Court has not previously linked prevailing party
status to securing a conclusive fnal judgment. Quite to
the contrary, we have held that a prevailing party for fee-
shifting purposes is one who has “succeeded on any signif-
cant claim affording it some of the relief sought, either pen-
dente lite”—i. e., pending the suit—“or at the conclusion of
the litigation.” Texas State Teachers Assn. v. Garland In-
dependent School Dist., 489 U. S. 782, 791 (1989). That is, a
plaintiff prevails when he accomplishes his lawsuit's “objec-
tiv[e],” which is to achieve “a material alteration in the legal
relationship between the parties.” CRST Van Expedited,
Inc. v. EEOC, 578 U. S. 419, 431 (2016). This is because, for
Page Proof Pending Publication
a plaintiff, “[a]t the end of the rainbow lies not a judgment,
but some action (or cessation of action) by the defendant that
the judgment produces—the payment of damages, or some
specifc performance, or the termination of some conduct.”
Hewitt v. Helms, 482 U. S. 755, 761 (1987).
   A plaintiff who secures a preliminary injunction awarding
actual relief on the merits of his claim that is never reversed
by a fnal decision of the court has “successfully maintained”
his claim “at the end.” Black's Law Dictionary, at 1352.
Such a plaintiff has achieved what he has “come to court”
for—the desired “alteration in the legal relationship between
the parties.” CRST, 578 U. S., at 431.1
   Take this case, for example. At the point it ended—when
the District Court dismissed the litigation as moot—re-
   1
     There are, of course, other kinds of preliminary injunctive orders, in-
cluding orders that maintain the status quo. All that is necessary to re-
ject the majority's categorical rule is the recognition that at least some
preliminary injunctions afford the type of material change that confers
prevailing party status.
212                  LACKEY v. STINNIE

                      Jackson, J., dissenting

spondents had secured a preliminary injunction against the
Commissioner of the Virginia Department of Motor Vehicles.
That order enabled respondents to drive their cars on Vir-
ginia's highways for 16 months, over the Commissioner's ob-
jection. And, because the District Court's interim award
had facilitated respondents' access to the road as licensed
drivers, they had prevailed on the merits of their claim in
every meaningful sense. Put another way, “at the end of
the litigation,” respondents did not “leav[e] the courthouse
emptyhanded.” Sole v. Wyner, 551 U. S. 74, 78 (2007). In-
stead, they departed having accomplished exactly what they
had sought to achieve. The fact that respondents achieved
their goal via a preliminary court ruling, as opposed to a
fnal judgment, is irrelevant, for “[n]othing in the language
of § 1988 conditions the District Court's power to award fees
on full litigation of the issues or on a judicial determination
that the plaintiff's rights have been violated.” Maher v.
Page Proof Pending Publication
Gagne, 448 U. S. 122, 129 (1980) (emphasis added).
   Juxtapose that reality with the text of other statutes that
make “prevailing party” status expressly dependent on the
entry of a fnal order. For example, the Emergency School
Aid Act of 1972—enacted just four years before § 1988(b)—
states that, “[u]pon the entry of a fnal order,” a court hear-
ing a school desegregation case may “allow the prevailing
party, other than the United States, a reasonable attorney's
fee as part of the costs.” 20 U. S. C. § 1617 (repealed 1979)
(emphasis added). Several statutes enacted after § 1988(b)
are similarly explicit about when a fee award must be fastened
to a fnal judgment. See, e. g., 28 U. S. C. § 2412(d)(2)(H) (de-
fning “prevailing party” in eminent domain proceedings to
“mea[n] a party who obtains a fnal judgment” of a certain
amount); 15 U. S. C. § 6104(d) (authorizing courts hearing ac-
tions under the Telemarketing and Consumer Fraud and
Abuse Prevention Act to award “reasonable fees . . . to the
prevailing party” upon “issuing any fnal order”). The fact
that § 1988(b) lacks any such language confrms that a conclu-
                      Cite as: 604 U. S. 192 (2025)                  213

                         Jackson, J., dissenting

sive ruling from the court in the form of a fnal judgment is
not a prerequisite for a fee award under that statute.
                                   C
   The majority disregards these important context clues and
focuses instead on a provision of the Freedom of Information
Act (FOIA) that authorizes fee awards for a “complainant”
who “has substantially prevailed” by “obtain[ing] relief
through either—(I) a judicial order, or an enforceable written
agreement or consent decree; or (II) a voluntary or unilateral
change in position by the agency.” 5 U. S. C. § 552(a)(4)(E).
The term “prevailing party” appears nowhere in this FOIA
provision. But, no matter: The majority nevertheless sug-
gests that this is how Congress authorizes fee shifting for
“plaintiffs who have enjoyed some success but have not pre-
vailed in a judgment on the merits.” Ante, at 205.
   The problem is that Congress had a much more targeted
objective when it enacted § 552(a)(4)(E). It sought merely
Page Proof Pending Publication
to repudiate this Court's decision in Buckhannon Board &
Care Home, Inc. v. West Virginia Dept. of Health and
Human Resources, 532 U. S. 598, 606 (2001), which had held
that a plaintiff must obtain some “judicial relief ” to be eligi-
ble for a fee award in FOIA cases.2 Since the point of
§ 552(a)(4)(E) was to “abrogat[e] the rule of Buckhannon in
the FOIA context and reviv[e] the possibility of FOIA fee
awards in the absence of a court decree,” Brayton v. Offce
of U. S. Trade Rep., 641 F. 3d 521, 525 (CADC 2011), that
  2
   Congress enacted 5 U. S. C. § 552(a)(4)(E) because Buckhannon had
empowered Government agencies to “stonewall valid FOIA claims” and
then prevent an award of attorney's fees by “disclosing the documents at
the last moment before judgment,” thereby mooting the case. Brayton
v. Offce of U. S. Trade Rep., 641 F. 3d 521, 525 (CADC 2011). Under
Buckhannon, such plaintiffs were not eligible for fee awards because they
had not obtained any judicial order—preliminary, fnal, or otherwise.
This strategic behavior ensured that FOIA plaintiffs never became eligi-
ble for fee awards despite incurring signifcant costs, so Congress inter-
vened. 641 F. 3d, at 525.
214                       LACKEY v. STINNIE

                          Jackson, J., dissenting

statutory provision sheds no light whatsoever on whether
the term “prevailing party” requires a plaintiff to secure a
conclusive ruling on the merits to qualify as a prevailing
party for purposes of § 1988(b).
   In short, while the majority insists that obtaining a pre-
liminary injunction can never suffce for a fee award under
§ 1988(b) “[b]ecause preliminary injunctions do not conclu-
sively resolve the rights of parties on the merits,” ante, at
201, the text of § 1988(b), contemporary dictionary def-
nitions, and our precedents require far less. All of the
Courts of Appeals to consider the question—11 in total—
understood this and thus correctly held that, for fee-shifting
purposes, it is possible for a party to prevail based on a pre-
liminary ruling.3 The majority's reading of “prevailing
party” in § 1988(b) makes obtaining a court's conclusive fnal
judgment the hallmark of that status in a manner that is
both novel and in many ways anathema to the legal term of
art that Congress actually chose.
Page Proof Pending Publication
                                    II
                                    A
  So what does it take to qualify as a “prevailing party” for
purposes of this fee-shifting statute? In Farrar v. Hobby,
506 U. S. 103 (1992), we explained that a plaintiff “ `prevails' ”
  3
    See, e. g., Haley v. Pataki, 106 F. 3d 478, 484 (CA2 1997); Singer Mgmt.
Consultants, Inc. v. Milgram, 650 F. 3d 223, 229–230, and n. 4 (CA3 2011)
(en banc); Stinnie v. Holcomb, 77 F. 4th 200, 210 (CA4 2023) (en banc) (case
below); Dearmore v. Garland, 519 F. 3d 517, 524 (CA5 2008); Planned
Parenthood Southwest Ohio Region v. Dewine, 931 F. 3d 530, 534 (CA6
2019); Dupuy v. Samuels, 423 F. 3d 714, 723, and n. 4 (CA7 2005); Rogers
Group, Inc. v. Fayetteville, 683 F. 3d 903, 909–910 (CA8 2012); Higher
Taste, Inc. v. Tacoma, 717 F. 3d 712, 717–718 (CA9 2013); Kansas Jud.
Watch v. Stout, 653 F. 3d 1230, 1232, 1238–1239 (CA10 2011); Common
Cause Ga. v. Georgia, 17 F. 4th 102, 107 (CA11 2021); Select Milk Produc-
ers, Inc. v. Johanns, 400 F. 3d 939, 942, 948–949 (CADC 2005). The First
Circuit has not yet considered the issue. See Sinapi v. Rhode Island Bd.
of Bar Examiners, 910 F. 3d 544, 552 (2018).
                    Cite as: 604 U. S. 192 (2025)             215

                      Jackson, J., dissenting

if he receives (1) “actual relief on the merits of his claim” in
a manner that (2) “materially alters the legal relationship
between the parties by modifying the defendant's behavior
in a way that directly benefts the plaintiff.” Id., at 111–
112; see also Lefemine v. Wideman, 568 U. S. 1, 4 (2012) (per
curiam). This test is well established, and it leads inexora-
bly to the conclusion that, in some circumstances, an unre-
versed preliminary injunction can confer prevailing party
status.
   Start with the requirement of a “ `material alteration of
the legal relationship of the parties,' ” which we have repeat-
edly called the “ `touchstone' ” of the prevailing party inquiry.
Sole, 551 U. S., at 82 (quoting Texas State Teachers Assn.,
489 U. S., at 792–793). A plaintiff need not obtain all of the
relief he has requested in the lawsuit to satisfy this require-
ment. Instead, under our precedents, a plaintiff who has
achieved even “ `some of the beneft' ” he sought has secured
Page Proof Pending Publication
the change in the parties' legal relationship necessary to
“cros[s] the threshold to a fee award of some kind.” Id., at
791–792 (quoting Nadeau v. Helgemoe, 581 F. 2d 275, 278–279
(CA1 1978); emphasis added).
   A permanent injunction—just like a declaratory judgment
or a damages award—“will usually satisfy that test,” Lefe-
mine, 568 U. S., at 4, because permanent injunctive relief
generally “affects the behavior of the defendant toward the
plaintiff,” Rhodes v. Stewart, 488 U. S. 1, 4 (1988) (per cu-
riam). At least some preliminary injunctions also qualify.
The preliminary injunction in this case, for example, pro-
vided respondents with actual relief by reinstating their sus-
pended licenses, allowing them to drive without fear of sanc-
tion for failing to repay their fnes and fees. For the roughly
16 months that the preliminary injunction was in place, “that
ruling worked the requisite material alteration in the par-
ties' relationship” by permitting respondents to engage in
conduct that would have been prohibited otherwise. Lefe-
mine, 568 U. S., at 5.
216                   LACKEY v. STINNIE

                      Jackson, J., dissenting

   It is indisputable that the preliminary injunction the Dis-
trict Court issued provided a “direc[t] beneft” to respond-
ents. Farrar, 506 U. S., at 111. That relief was also
awarded “ `on the merits.' ” Lefemine, 568 U. S., at 4 (quoting
Farrar, 506 U. S., at 111–112). We have long taken a “prac-
tical” approach to the merits inquiry in this context. Han-
rahan v. Hampton, 446 U. S. 754, 758 (1980) (per curiam).
Under that approach, relief is granted “on the merits” when
it provides “a resolution of the dispute which changes the
legal relationship between [the plaintiff] and the defendant.”
Texas State Teachers Assn., 489 U. S., at 792 (internal quota-
tion marks omitted).
   Notably, for prevailing party status, we have not required
that a court actually determine whether a legal claim is meri-
torious. The majority acknowledges our holding that the
entry of a consent decree following “the parties' own resolu-
tion of the merits” counts. Ante, at 207; see Farrar, 506
Page Proof Pending Publication
U. S., at 111 (recognizing that a consent decree satisfes the
requirement that the plaintiff “obtain at least some relief on
the merits of his claim”). Indeed, in Maher, we upheld a fee
award based on a consent decree that “did not purport to
adjudicate” the plaintiff's claims at all. 448 U. S., at 126,
n. 8, 129. We have also suggested that default judgments,
which do not involve any assessment of the merits of the
plaintiff 's claims, “almost invariably give rise to fee awards.”
Kirtsaeng v. John Wiley & Sons, Inc., 579 U. S. 197, 208,
n. 3 (2016).
   A court's entry of a preliminary injunction—which does
require a judge to make a preliminary assessment of the
merits—provides a basis for prevailing party status that is
at least as strong as a consent decree or a default judgment.
Plaintiffs seeking the “extraordinary remedy” of a prelimi-
nary injunction must make a “clear showing” that they are
“likely to succeed on the merits.” Winter v. Natural Re-
sources Defense Council, Inc., 555 U. S. 7, 20, 22 (2008).
And the court's decision to order preliminary injunctive re-
                    Cite as: 604 U. S. 192 (2025)              217

                       Jackson, J., dissenting

lief often involves “searching” proceedings, Sole, 551 U. S.,
at 84, even though the “evidence . . . is less complete than in
a trial on the merits,” University of Tex. v. Camenisch, 451
U. S. 390, 395 (1981).
   In this case, the District Court thoroughly assessed the
merits of respondents' claims and granted their request for
preliminary injunctive relief after extensive briefng and an
evidentiary hearing during which multiple witnesses testi-
fed. It blinks reality to suggest that the District Court's
order requiring the Commissioner to give respondents their
licenses back now—based on the court's conclusion that re-
spondents were likely to succeed if this matter proceeded to
trial—is “not the stuff of which legal victories are made.”
Hewitt, 482 U. S., at 760.
   It is no answer to simply declare by ipse dixit that prelimi-
nary injunctions are materially different from consent de-
crees because “a consent decree is like a fnal judgment in
Page Proof Pending Publication
the relevant ways”—i. e., “[i]t conclusively resolves the
claim, bears a judicial imprimatur, and may grant enduring
relief that materially alters the legal relationship between
the parties.” Ante, at 207. The very question before us is
the relevance of this kind of fnality to the prevailing party
determination. And, luckily, that question has already been
answered: Neither the text of § 1988(b) nor any of this
Court's past cases make fee eligibility dependent on the
entry of a conclusive fnal judgment, as I explained above.
   In any event, if a plaintiff need only obtain an order that
is “like a fnal judgment” to prevail, ibid., it is not at all clear
why at least some preliminary injunctions would not count.
Consider, for example, a dispute in which the district court
reviews the evidence and the parties' arguments and enters
the type of preliminary injunction that changes the legal re-
lationship of the parties. The case proceeds but then be-
comes moot such that the litigation ends; the preliminary
injunction is not—and can never be—reversed by a subse-
quent order of the court. In this scenario, all the purport-
218                  LACKEY v. STINNIE

                      Jackson, J., dissenting

edly “relevant” characteristics of a consent decree exist, be-
cause the parties' legal relationship was materially altered
by judicial imprimatur, and that preliminary relief is conclu-
sive insofar as the case has ended and the ruling cannot be
undone by a later determination. In this circumstance, the
preliminary injunction “functions much like the grant of
an irreversible partial summary judgment on the merits,”
Northern Cheyenne Tribe v. Jackson, 433 F. 3d 1083, 1086
(CA8 2006), which all appear to agree would suffce to confer
fee eligibility under § 1988(b).

                                B
   Our decisions in Buckhannon, 532 U. S. 598, and Sole, 551
U. S. 74, are not to the contrary. The majority cites these
two decisions to support its view that obtaining a prelimi-
nary injunction is never suffcient to qualify the recipient for
a fee award under § 1988(b). Ante, at 202–204. But those
Page Proof Pending Publication
cases hold no such thing. Instead, they simply clarify that,
for a plaintiff to prevail, the requisite “change in the legal
relationship of the parties” must be both “judicially sanc-
tioned,” Buckhannon, 532 U. S., at 605, and “enduring,” Sole,
551 U. S., at 86. Neither case mandates the majority's cate-
gorical rule.
   In Buckhannon, this Court rejected the so-called “catalyst
theory,” under which a plaintiff could collect a fee award as
a “prevailing party” without securing any judicial relief so
long as the lawsuit produced “a voluntary change in the de-
fendant's conduct.” 532 U. S., at 601. We held that such a
voluntary change, “although perhaps accomplishing what the
plaintiff sought to achieve by the lawsuit, lacks the necessary
judicial imprimatur on the change” to trigger fee eligibility.
Id., at 605. In Sole, we considered whether a plaintiff who
obtains a preliminary injunction but is subsequently denied
a permanent one prevails for fee purposes under § 1988(b).
551 U. S., at 77. We explained that when a plaintiff 's “initial
victory” at the preliminary injunction stage is “superseded”
                    Cite as: 604 U. S. 192 (2025)             219

                      Jackson, J., dissenting

by a nonfavorable fnal “ruling on the merits,” he does not
qualify as a “prevailing party,” because the relief he received
was not “enduring.” Id., at 84–86.
   A preliminary injunction that mandates a judicially sanc-
tioned legal change in the parties' relationship and is never
reversed by a fnal ruling on the merits satisfes both Buck-
hannon and Sole. A court that issues interim injunctive re-
lief unquestionably gives its “judicial imprimatur” to the
change afforded, as Buckhannon requires. 532 U. S., at 605.
For its part, Sole stands merely for the proposition that a
party can be divested of “prevailing party” status if his “suc-
cess rested on a premise the District Court ultimately re-
jected.” 551 U. S., at 84–86. But Sole is inapposite when a
subsequent fnal decision does not thwart the judge-
sanctioned basis for the preliminary injunction. Indeed,
Sole expressly said so, by specifcally reserving the question
“whether, in the absence of a fnal decision on the merits of
Page Proof Pending Publication
a claim for permanent injunctive relief, success in gaining a
preliminary injunction may sometimes warrant an award of
counsel fees,” id., at 86—the precise issue that is before the
Court today.
   The majority thus overreads our precedents to support its
blanket rule that preliminary injunctions can never support
fee awards. Ante, at 202–204. With respect to Sole in par-
ticular, it is true that we characterized the preliminary injunc-
tion at issue there as “feeting” and “tentative.” 551 U. S.,
at 83–84; see also ante, at 203 (contrasting interim relief with
relief that “last[s]”). But the Sole Court did not tie the re-
quirement for “enduring” relief to the inherent permanence
of the relevant judicial order. Instead, we made crystal
clear that “[o]f controlling importance to our decision” was
the fact that “the eventual ruling on the merits for defend-
ants, after both sides considered the case ft for fnal adjudi-
cation, superseded the preliminary ruling.” 551 U. S., at 84–
85 (emphasis added); see also id., at 78 (observing that a
plaintiff does not prevail if “at the end of the litigation, her
220                  LACKEY v. STINNIE

                     Jackson, J., dissenting

initial success is undone and she leaves the courthouse
emptyhanded”).
   At the end of the day, Sole should be taken to mean only
what it expressly holds: Preliminary injunctive relief that is
subsequently superseded by a fnal judgment reversing the
ruling does not endure for fee-shifting purposes. Here, the
preliminary injunction provided actual relief to respondents
for more than 16 months, and there was no Sole-like sup-
planting of that preliminary relief by a subsequent court
order.
                             III
                               A
   In addition to misinterpreting the text of § 1988(b) and
misconstruing our precedents, the majority ignores Con-
gress's clear intent to expand access to justice. It is puz-
zling, to say the least, that the majority seems to go out of
its way to adopt a rule that categorically prohibits fee shift-
Page Proof Pending Publication
ing while interpreting a statute that expressly authorizes
fee awards.
   There is no dispute that Congress enacted § 1988(b) “for a
specifc purpose”: to respond to this Court's decision in Aly-
eska Pipeline Service Co. v. Wilderness Society, 421 U. S.
240 (1975), which had rejected the “former equitable practice
of awarding attorney's fees to the prevailing party in certain
civil rights cases.” Farrar, 506 U. S., at 118 (O'Connor, J.,
concurring). The Alyeska Court held that, absent statutory
authorization, courts should not depart from the “ `American
Rule,' ” under which litigants ordinarily bear their own at-
torney's fees. 421 U. S., at 247. Congress swiftly enacted
§ 1988(b) in Alyeska's wake to codify a civil rights exception
to the American Rule. The majority does not, and cannot,
dispute that Congress's intent was “to ensure `effective ac-
cess to the judicial process' for persons with civil rights
grievances.” Hensley v. Eckerhart, 461 U. S. 424, 429 (1983)
(quoting H. R. Rep. No. 94–1558, p. 1 (1976)).
                   Cite as: 604 U. S. 192 (2025)             221

                      Jackson, J., dissenting

    Consistent with that “clear congressional intent,” this
Court has previously recognized that fee awards should be
available to “partially prevailing civil rights plaintiffs.”
Texas State Teachers Assn., 489 U. S., at 790. This principle
is, in fact, readily apparent from the statute's enactment his-
tory. See Buckhannon, 532 U. S., at 607. The history dem-
onstrates that the question of awarding fees for success
based on interim orders was not overlooked by the legisla-
ture; to the contrary, Congress specifcally “contemplated the
award of fees pendente lite,” at least where a party “has
established his entitlement to some relief on the merits of
his claims.” Hanrahan, 446 U. S., at 757 (citing S. Rep. No.
94–1011, p. 5 (1976); H. R. Rep. No. 94–1558, at 7–8).
    The majority says that Congress merely wanted § 1988(b)
to authorize fee awards when “conclusive, enduring judicial
relief is meted out on an incremental basis.” Ante, at 206.
But that is not what the historical record establishes, and
Buckhannon fatly rejects this contention. There, we spe-
Page Proof Pending Publication
cifcally observed that, per § 1988(b)'s legislative history,
“ ` “prevailing party” is not intended to be limited to the vic-
tor only after entry of a fnal judgment following a full trial
on the merits.' ” 532 U. S., at 607 (quoting H. R. Rep. No.
94–1558, at 7); see also Hanrahan, 446 U. S., at 756–757.
The legislative history is likewise unequivocal that a prevail-
ing party for § 1988(b) purposes should “also include a liti-
gant who succeeds even if the case is concluded prior to a
full evidentiary hearing before a judge or jury.” H. R. Rep.
No. 94–1558, at 7.
                                B
  Nor could a Congress that wished to authorize fee awards
for civil rights victories have intended the absurdities that
will result from the majority's categorical preclusion of pre-
liminary injunctive relief from § 1988(b). To state the obvi-
ous, the majority's bright-line rule lacks the nuance that is
needed to account for the various circumstances in which a
preliminary injunction may be “preliminary” in name only.
222                  LACKEY v. STINNIE

                     Jackson, J., dissenting

   One example is the plaintiff who requests a preliminary
injunction to achieve an interim result, given the timeframe
at issue. “When protesters seek an injunction to exercise
their First Amendment rights at a specifc time and place—
say to demonstrate at a Saturday parade—a preliminary in-
junction will give them all the court-ordered relief they need
and the end of the parade will moot the case.” McQueary
v. Conway, 614 F. 3d 591, 599 (CA6 2010). Thus, the Courts
of Appeals regularly hold that plaintiffs who successfully ob-
tain a preliminary injunction that permits them to engage in
the otherwise prohibited conduct “prevail” for fee-shifting
purposes. See, e. g., Young v. Chicago, 202 F. 3d 1000, 1000–
1001 (CA7 2000) (per curiam) (awarding fees to plaintiffs
who obtained a preliminary injunction to protest a political
convention even though the “suit became moot before a de-
fnitive determination of its merits” could be made).
   In its rush to carve preliminary injunctions out of
Page Proof Pending Publication
§ 1988(b), the majority also overlooks situations in which
courts have, in fact, conclusively resolved the merits of a
plaintiff 's claims at the preliminary injunction stage. A
trial court might defnitively determine that a law is “ ` “fa-
cially unconstitutional” ' ” in the course of granting prelimi-
nary relief, for example. Singer Mgmt. Consultants, Inc. v.
Milgram, 650 F. 3d 223, 229–230, and n. 4 (CA3 2011) (en
banc) (quoting People Against Police Violence v. Pittsburgh,
520 F. 3d 226, 229 (CA3 2008)). But the majority nonethe-
less adopts a sweeping rule under which preliminary injunc-
tions can never be the basis for fee eligibility.
   And to what end? The majority seeks to justify its broad
holding on the grounds that it discourages fee disputes and
thereby “serves the interests of judicial economy.” Ante,
at 204. But concerns about judicial administration cannot
supplant Congress's clear intent to promote access to justice
via fee shifting in civil rights cases.
   What is more, it is actually the majority's categorical rule
that will promote wasteful litigation and incentivize litigants
                    Cite as: 604 U. S. 192 (2025)             223

                      Jackson, J., dissenting

to manipulate fee liability. Under the majority's rule, a
plaintiff who has incurred substantial attorney's fees in order
to secure a preliminary injunction that provides all the relief
he needs will face a choice: He may either concede that the
litigation has run its course and pay his own fees, or he may
seek to litigate the case to fnal judgment in order to secure
a fee award. No one would blame a plaintiff with a strong
case for choosing the latter option. But such additional liti-
gation is an ineffcient waste of judicial resources if the plain-
tiff has already achieved his objective at an earlier part of
the case.
   Worse still, the majority's rule appears to preference con-
servation of judicial resources over the maintenance of meri-
torious civil rights lawsuits, to the extent that excluding
preliminary injunctive relief from § 1988(b) facilitates the
strategic mooting of cases by defendants to avoid paying at-
torney's fees. This case illustrates precisely that problem.
Page Proof Pending Publication
After a robust evidentiary hearing, the District Court issued
a comprehensive opinion that preliminarily enjoined the
Commissioner from enforcing the challenged law against re-
spondents. Seeing the writing on the wall, the Commis-
sioner sought and obtained a stay of the case—over respond-
ents' objections—based on his representation that the
legislature was likely to repeal the challenged law. The
Commissioner then successfully lobbied the legislature to re-
peal the legislation, emphasizing that doing so would, in his
words, “result in [respondents'] pending litigation being dis-
missed, relieving the Department from continuing to incur
costly legal fees.” App. 409.
   As the Fourth Circuit observed, precluding fee shifting
in this scenario is manifestly inequitable, because it leaves
respondents “holding the bag” for considerable litigation fees
despite—and largely because of—their having succeeded in
obtaining preliminary relief. Stinnie v. Holcomb, 77 F. 4th
200, 210 (2023) (en banc). Ironically, it was the strength of
respondents' challenge as verifed by the court's preliminary
224                    LACKEY v. STINNIE

                       Jackson, J., dissenting

order that prompted both the change in law and the Commis-
sioner's robust effort to stiff the plaintiffs with respect to
attorney's fees. Moreover, it is hardly a revelation that law-
yers who would otherwise be willing to litigate meritorious
civil rights cases (i. e., matters in which interim relief is criti-
cal due to ongoing civil rights violations) will likely be dis-
couraged from taking on such representations if fee awards
can be so easily thwarted.
   The majority dismisses concerns about strategic mooting
as both “ `entirely speculative' ” and likely to “arise in only a
small number of contexts.” Ante, at 204 (quoting Buckhan-
non, 532 U. S., at 608). But, as I have shown, the facts of
this very case belie the majority's nonchalance, particularly
in light of the Buckhannon experience. Research suggests
that the Court's rejection of the catalyst theory in that case
had the predictable practical effect of discouraging public in-
terest organizations and private attorneys from taking on
Page Proof Pending Publication
civil rights actions. C. Albiston & L. Nielsen, The Proce-
dural Attack on Civil Rights: The Empirical Reality of Buck-
hannon for the Private Attorney General, 54 UCLA L. Rev.
1087, 1092 (2007); cf. n. 2, supra. Similarly, a multitude of
legal advocacy groups have fled amicus briefs in this case
to explain that losing the ability to recoup fees for securing
interim relief will jeopardize their missions. See, e. g., Brief
for Alliance Defending Freedom et al. as Amici Curiae 7–10;
Brief for American Civil Liberties Union et al. as Amici Cu-
riae 28–30; Brief for Lawyers' Committee for Civil Rights
Under Law et al. as Amici Curiae 17–18.
   There is thus every reason to believe that the net result
of today's decision will be less civil rights enforcement in the
long run. Without irony, the majority reads a statute that
was “enacted to [e]nsure that private citizens have a mean-
ingful opportunity to vindicate their [civil] rights,” Pennsyl-
vania v. Delaware Valley Citizens' Council for Clean Air,
478 U. S. 546, 559 (1986), as if Congress meant to make pri-
vate civil rights enforcement harder to achieve.
                   Cite as: 604 U. S. 192 (2025)            225

                     Jackson, J., dissenting

                         *      *      *
  The majority holds that obtaining a preliminary injunction
never entitles a plaintiff to fees under § 1988(b). In doing
so, it overrules the decisions of every Court of Appeals to
consider the issue, relies on an atextual “conclusive judg-
ment” requirement, and ignores both our precedents and
Congress's intent.
  It is quite true that Congress has demonstrated its ability
to fx our mistakes in this realm. Ante, at 205. But, in my
view, rather than relying on Congress to check our work, we
should give full effect to the plain text and remedial purpose
of § 1988(b) in the frst instance. This Court should have
held that, when a court hearing a civil rights lawsuit issues a
preliminary injunction that materially alters the relationship
between the parties and is never reversed, the requesting
party “prevails” for fee-shifting purposes and is thus eligible
for a fee award under § 1988(b).
Page Proof Pending Publication
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 217, line 13: “was” is changed to “is”

```

---

## GROUP: content/cases/Landor v. Louisiana Dept. of Corrections.md  (`case`, 5 assertions)

### content_page

```
---
title: Landor v. Louisiana Dept. of Corrections
type: case
citation: "No. 23-1197, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 23-1197
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
  opinion_url: "https://www.courtlistener.com/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/"
  cluster_id: 10878535
  opinion_id: 11346052
  identity_checked: false
lake:
  record_id: Landor v. Louisiana Dept. of Corrections
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - rluipa
  - spending-clause
  - individual-capacity
  - damages
  - supreme-court
holding: "Because RLUIPA was enacted under Congress's Spending Clause authority, an individual state official may be held personally liable under the statute only if that individual voluntarily and knowingly consented to answer such suits; the officers who allegedly shaved a Rastafarian inmate's head never entered any funding agreement with the federal government, so RLUIPA affords no damages claim against them in their personal capacities."
aliases:
  - Landor v. Louisiana Dept. of Corrections
  - Landor v. Louisiana Department of Corrections and Public Safety
  - Landor v. Louisiana
---

# Landor v. Louisiana Dept. of Corrections

*No. 23-1197, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10878535 → majority opinion 11346052 (Gorsuch, J.; No. 23-1197, decided June 23, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
Damon Landor, a Rastafarian whose faith forbids cutting his hair, alleged that Louisiana Department of Corrections officers — aware of his religious beliefs — forcibly shaved his head. He sued LDOC and several officers in their personal capacities under the Religious Land Use and Institutionalized Persons Act (RLUIPA), which Congress enacted under its Spending Clause power and which conditions federal prison funds on the recipient system's agreement to answer certain religious-exercise suits. The district court dismissed the RLUIPA claims; the Fifth Circuit declined to revive the claim against the individual officers, holding RLUIPA does not authorize personal-capacity suits.

## Issue
Whether RLUIPA, a Spending Clause statute, permits damages suits against individual state officials in their personal capacities.

## Rule
The Spending Clause lets Congress attach conditions to federal funds, but "[a]dditional sanctions are permissible only with the 'voluntar[y] and knowin[g]' consent of those who must bear them," tested through a "contract analogy" under which a person is bound only by conditions to which he actually, knowingly agreed. The Court held: "Individuals may not be held liable in their personal capacities under a Spending Clause statute unless those individuals have voluntarily and knowingly consented to answer lawsuits under the statute." — slip op. at 1. ^pin-slip1

## Application
LDOC, as the funding recipient, agreed to answer certain RLUIPA suits — but the individual officers did not. Landor never alleged that any officer personally entered an agreement with the federal government, let alone voluntarily and knowingly consented to face RLUIPA damages liability. Just as a breach-of-contract action cannot proceed against someone who never formed the contract, Landor's RLUIPA claim cannot proceed against officers who never accepted the statute's conditions. His agency-law and related arguments all failed because they sidestepped the dispositive consent requirement.

## Conclusion
**Affirmed** as to the individual-capacity claims. Justice Gorsuch wrote for the Court (6–3).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Landor* marks the ceiling of Spending Clause remedies against individuals: unlike § 1983, which reaches state officers sued in their personal capacities by force of statute, a funding-condition statute like RLUIPA binds only the consenting recipient — leaving injured plaintiffs to look elsewhere for personal-capacity damages.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Landor v. Louisiana Dept. of Corrections and Public Safety*, No. 23-1197, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/) — pinpoint: slip op. at 1 (Spending Clause individual-capacity consent rule). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9f6267942f1c2774", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 23-1197, slip op. (U.S. 2026)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Landor v. Louisiana Dept. of Corrections", "year": "2026"}}
{"assertion_id": "848a607cbd5641d9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because RLUIPA was enacted under Congress's Spending Clause authority, an individual state official may be held personally liable under the statute only if that individual voluntarily and knowingly consented to answer such suits; the officers who allegedly shaved a Rastafarian inmate's head never entered any funding agreement with the federal government, so RLUIPA affords no damages claim against them in their personal capacities.", "title": "Landor v. Louisiana Dept. of Corrections"}}
{"assertion_id": "aea9828edd0e68d8", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Landor v. Louisiana Dept. of Corrections"}}
{"assertion_id": "396a145e65c64548", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Landor v. Louisiana Dept. of Corrections", "varies_by_point": "false"}}
{"assertion_id": "bc60b2c1c3249d4f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Landor v. Louisiana Dept. of Corrections"}}
```

### lake record — Landor v. Louisiana Dept. of Corrections

```json
{
  "schema_version": "s2.v1",
  "record_id": "Landor v. Louisiana Dept. of Corrections",
  "status": "under_review",
  "identity": {
    "case_name": "Landor v. Louisiana Dept of Corrections and Public Safety",
    "case_name_short": "Landor",
    "case_name_full": "",
    "input_case_name": "Landor v. Louisiana Department of Corrections and Public Safety",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "23-1197",
    "cluster_id": 10878535,
    "lead_opinion_id": 11346052,
    "sibling_ids": [],
    "absolute_url": "/opinion/10878535/landor-v-louisiana-dept-of-corrections-and-public-safety/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 23-1197, decided 2026-06-23 (609 U.S. ___; Gorsuch, 6-3). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/23-1197",
          "cite": "No. 23-1197, decided 2026-06-23"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/609/23-1197/",
          "cite": "609 U.S. ___ (2026) placeholder"
        }
      ]
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
    "date_created": "2026-07-06T12:14:06Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:14:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "landor-v-louisiana-department-of-corrections-and-public-safety--10878535",
      "to_record_id": "Landor v. Louisiana Dept. of Corrections",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Landor v. Louisiana Dept. of Corrections

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

         LANDOR v. LOUISIANA DEPARTMENT OF
         CORRECTIONS AND PUBLIC SAFETY ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

   No. 23–1197.      Argued November 10, 2025—Decided June 23, 2026
The Religious Land Use and Institutionalized Persons Act of 2000
  (RLUIPA) was enacted pursuant to Congress’s Spending Clause au-
  thority and imposes various conditions on federal funds distributed to
  state prison systems like the Louisiana Department of Corrections
  (LDOC). One condition requires state prison systems to agree to an-
  swer federal suits by private plaintiffs alleging certain substantial bur-
  dens on their religious exercises. See 42 U. S. C. §§2000cc–1(a), (b)(1).
  Relying on that provision, inmate Damon Landor brought this
  RLUIPA lawsuit against LDOC as well as some of the prison system’s
  individual officers in their personal capacities, seeking damages from
  them. Mr. Landor is a Rastafarian whose religious convictions require
  him to leave his hair uncut. He claims that LDOC officers—despite
  being aware of his religious beliefs—forcibly shaved his head. The of-
  ficers moved to dismiss, arguing that while their employer LDOC may
  have agreed to answer certain private suits under RLUIPA, they were
  not parties to any such agreement, and therefore Mr. Landor had no
  federal cause of action against them. The district court dismissed Mr.
  Landor’s RLUIPA claims against both the officers and LDOC. On ap-
  peal, Mr. Landor challenged only the dismissal of his claim against the
  individual officers. The Fifth Circuit declined to revive that portion of
  his suit, holding that RLUIPA does not permit suits against officers in
  their individual capacities.
Held: Individuals may not be held liable in their personal capacities un-
 der a Spending Clause statute unless those individuals have voluntar-
 ily and knowingly consented to answer lawsuits under the statute; be-
 cause the individual defendants in this case did not voluntarily and
2       LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                        PUBLIC SAFETY
                           Syllabus

    knowingly consent to face RLUIPA liability in an agreement with the
    federal government, Mr. Landor’s case cannot proceed against them.
    Pp. 3–18.
       (a) While the Constitution’s “Spending Clause,” Art. I, §8, cl. 1, may
    confer on Congress the power to spend money for the general welfare,
    it does not “endow Congress with [any] power to regulate conduct.”
    Medina v. Planned Parenthood South Atlantic, 606 U. S. 357, 370.
    Congress may attach conditions to the funds it distributes, and if a
    recipient “violates those conditions,” Congress typically may “termi-
    nate” its agreement to provide funds. Id., at 365–366 (internal quota-
    tion marks omitted). But Congress cannot dictate whatever other
    sanctions it might wish for violating conditions found in its Spending
    Clause legislation. Additional sanctions are permissible only with the
    “voluntar[y] and knowin[g]” consent of those who must bear them.
    Pennhurst State School and Hospital v. Halderman, 451 U. S. 1, 17.
    To sort out whether consent exists, the Court has traditionally em-
    ployed a “contract analogy” that helps to ensure conditions attached to
    federal funds—including those prescribing exposure to potential sanc-
    tions—apply only to those who have knowingly and voluntarily agreed
    to them. Pp. 3–8.
       (b) These settled principles resolve this case. Before this Court,
    LDOC does not dispute that it is a recipient of federal funds and has
    agreed to answer certain RLUIPA suits as a condition of accepting
    those funds. But this case involves only claims against individual state
    employees in their personal capacities, and Mr. Landor does not allege
    that any of those individuals has entered any agreement with the fed-
    eral government, let alone that any of them has voluntarily and know-
    ingly consented to answer private suits under RLUIPA. Because they
    never agreed to answer suits like this one, Mr. Landor’s case cannot
    proceed against them any more than a breach of contract action might
    proceed against a defendant who never formed a contract. P. 8.
       (c) Mr. Landor’s arguments are all variations on the theme that the
    lack of voluntary and knowing consent does not matter. And they all
    fail for that reason. Under the Spending Clause and the Court’s prec-
    edents, the consent requirement is key. Pp. 9–18.
          (1) Mr. Landor invokes agency law, arguing that LDOC employees
    may be held liable because they are LDOC’s agents. But as a matter
    of blackletter law, when a principal enters a contract with a third
    party, the principal’s agents do not become liable to the third party for
    their principal’s nonperformance. LDOC might be subject to certain
    private suits under RLUIPA if it breaches its promises to the federal
    government, but it does not follow that LDOC’s employees are as well.
    Pp. 9–10.
          (2) Mr. Landor next turns to South Dakota v. Dole, 483 U. S. 203,
                      Cite as: 609 U. S. ___ (2026)                     3

                                Syllabus

  arguing that his proposed cause of action satisfies Dole’s four require-
  ments and therefore satisfies the Spending Clause too. But Dole’s re-
  quirements apply in addition to—not instead of—the rule that Con-
  gress may not use the Spending Clause to bind entities and individuals
  without their knowing and voluntary consent. Dole itself added a fifth
  rule barring compulsion and reaffirmed the clear-statement rule, both
  of which serve to ensure real consent exists. Mr. Landor also argues
  that RLUIPA’s mere existence sufficed to alert the individual defend-
  ants that they could be held personally liable. This argument fares no
  better. A Spending Clause statute assumes binding effect only
  through “voluntar[y] and knowin[g]” agreement, which is lacking here.
  Pennhurst, 451 U. S., at 17. Pp. 10–12.
       (3) Mr. Landor next turns to the fungibility of money, contending
  that the individual defendants are indirect recipients of federal funds
  because they receive paychecks from LDOC. But this argument would
  mean that so long as a penny of federal spending makes its way to an
  individual, Congress could directly regulate his conduct based on the
  fiction that he has consented to regulation. This is inconsistent with
  the requirement of knowing and voluntary consent, and it would give
  Congress an effectively unbridled police power impossible to square
  with the Spending Clause’s terms or our precedents. Pp. 12–15.
       (4) Mr. Landor’s reliance on the Necessary and Proper Clause and
  Sabri v. United States, 541 U. S. 600, is misplaced. In Sabri, the Court
  held that Congress’s criminal ban on theft, fraud, or bribery against a
  federal funding recipient is a necessary and proper incident to Con-
  gress’s authority to spend money. 541 U. S., at 605–606. Mr. Landor
  contends that his proposed cause of action is likewise incidental to
  RLUIPA’s policy protecting religious exercises. But Mr. Landor is an-
  swering the wrong question. The correct question is instead whether
  such a cause of action is a necessary and proper incident to Congress’s
  enumerated power to spend money. Suits against nonconsenting par-
  ties like the individual officers here might advance RLUIPA’s policy
  but do not safeguard federal funds from being “frittered away in graft.”
  Id., at 605. Adopting Mr. Landor’s proposed cause of action would al-
  low Congress to evade the consent requirement inherent in its Spend-
  ing Clause authority and regulate directly the conduct of countless
  nonconsenting individuals in spheres traditionally reserved to the
  States. Such a result would be inconsistent with principles of state
  sovereignty and a federal government of limited and enumerated reg-
  ulatory powers. Pp. 15–18.
82 F. 4th 337, affirmed.

  GORSUCH, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and THOMAS, ALITO, KAVANAUGH, and BARRETT, JJ., joined.
4     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                         Syllabus

JACKSON, J., filed a dissenting opinion, in which SOTOMAYOR and KAGAN,
JJ., joined.
                       Cite as: 609 U. S. ____ (2026)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    United States Reports. Readers are requested to notify the Reporter of
    Decisions, Supreme Court of the United States, Washington, D. C. 20543,
    pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 23–1197
                                  _________________


    DAMON LANDOR, PETITIONER v. LOUISIANA
      DEPARTMENT OF CORRECTIONS AND
            PUBLIC SAFETY, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                                [June 23, 2026]

   JUSTICE GORSUCH delivered the opinion of the Court.
   This case concerns whether the Religious Land Use and
Institutionalized Persons Act of 2000 permits plaintiffs to
sue nonconsenting state employees in their private capaci-
ties for damages.
                              I
  Today, Congress offers financial support to all 50 States
and many other entities. Much of that support comes with
strings attached. So, for example, Congress has conditioned
receipt of federal highway funds on a State’s agreement to
maintain laws setting a minimum drinking age of 21. See
South Dakota v. Dole, 483 U. S. 203 (1987). Likewise, Con-
gress has conditioned federal Medicaid funds on a State’s
willingness to administer its healthcare programs con-
sistent with various rules.       See Medina v. Planned
Parenthood South Atlantic, 606 U. S. 357, 362–364 (2025).
In each of these contexts and many others, the penalty for
noncompliance is straightforward: Congress may “termi-
nate funds” if a recipient fails to abide by the conditions
2    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

associated with its grants. Id., at 365–366 (internal quota-
tion marks omitted).
   The statute at issue before us, the Religious Land Use
and Institutionalized Persons Act of 2000 (RLUIPA), works
similarly. As relevant here, RLUIPA imposes various con-
ditions on federal funds distributed to state prison systems
like the Louisiana Department of Corrections (LDOC). One
condition requires prison systems to refrain from imposing
“substantial burden[s] on the religious exercise[s]” of state
prisoners outside exceptional circumstances.           See 42
U. S. C. §§2000cc–1(a), (b)(1); see also Tr. of Oral Arg. 60.
If a prison system fails to comply with that condition, Con-
gress may cut off its funding.
   But when enacting RLUIPA, Congress did something
more: It included another, distinct remedy as part of the
bargain. As a condition of funding, Congress called on state
prison systems to agree to answer suits by private plaintiffs
alleging substantial burdens on their religious exercises.
Specifically, the law asked those systems to consent to suit
by any injured party “assert[ing] a violation of ” RLUIPA
and seeking “appropriate relief.” §2000cc–2(a).
   This case concerns that provision. Damon Landor is a
Rastafarian whose religious convictions require him to
leave his hair uncut. In 2020, after a conviction in Louisi-
ana state court, Mr. Landor spent a few months in custody.
Near the end of his sentence, as officers transferred him
from one facility to another, Mr. Landor grew concerned
that the new facility’s intake officers might cut his hair pur-
suant to standard LDOC grooming policies. To avoid that
possibility, he provided the officers with a copy of Ware v.
LDOC, 866 F. 3d 263 (CA5 2017), which held that RLUIPA
generally bars prisons from cutting Rastafarians’ hair. See
id., at 266, 274. But, Mr. Landor says, the LDOC officers
in the new facility responded by throwing his copy of Ware
in the trash and proceeding to shave his head, causing him
to violate his religious beliefs.
                 Cite as: 609 U. S. ____ (2026)           3

                     Opinion of the Court

   After that transpired, Mr. Landor brought this lawsuit
under RLUIPA seeking money damages. He sued not only
LDOC, but also some of the prison system’s individual of-
ficers in their personal capacities. The officers responded
by asking the district court to dismiss Mr. Landor’s com-
plaint. As they saw it, their employer, LDOC, may have
struck a bargain with the federal government to answer
certain private suits by prisoners like Mr. Landor. But,
they argued, they were not parties to that or any other
agreement to answer private suits under RLUIPA. Accord-
ingly, they continued, Mr. Landor had no federal cause of
action against them. Ultimately, the court dismissed Mr.
Landor’s RLUIPA claims against both LDOC and the offic-
ers.
   On appeal to the Fifth Circuit, Mr. Landor did not chal-
lenge the district court’s dismissal of his RLUIPA claim
against LDOC. Instead, he focused on his claim against the
individual officers, asking the Court of Appeals to revive
only that portion of his suit. The Fifth Circuit declined to
do so. It did not question that RLUIPA may permit certain
claims against funding recipients like LDOC. But, the
court held, RLUIPA “does not permit suits against officers
in their individual capacities.” 82 F. 4th 337, 341 (2023).
We granted Mr. Landor’s petition for a writ of certiorari.
606 U. S. 916 (2025).
                            II
  Before us, the parties dispute two questions. One is
whether, by authorizing private lawsuits seeking “appro-
priate relief,” RLUIPA ever permits suits for money dam-
ages—or whether the statute instead limits plaintiffs like
Mr. Landor to other remedies, like injunctions or declara-
tory judgments. Brief for Petitioner 2–3, 18–19; Brief for
Respondents 4. The other question the parties spar over is
whether, consistent with the Constitution, a plaintiff may
bring an RLUIPA suit against individuals, like the officers
4     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

in this case, who have not formed any agreement with the
federal government. Brief for Petitioner 38–46; Brief for
Respondents 28–30, 45–46. To resolve this case, we need
answer only the second question.1
   Article I of the Constitution grants Congress certain lim-
ited and enumerated powers. Congress, for example, may
“regulate Commerce . . . among the several States.” Art. I,
§8, cl. 3. It may “establish a uniform Rule of Naturaliza-
tion, and uniform Laws on the subject of Bankruptcies.”
Cl. 4. It may “coin Money” and “provide for the Punishment
of counterfeiting.” Cls. 5–6. These provisions and others
allow Congress to regulate the behavior of the American
people in specific fields. And each allows Congress to back
up its regulations “with a sanction” enforced either “by the
COERTION of the magistracy, or by the COERTION of arms.”
The Federalist No. 15, p. 95 (J. Cooke ed. 1961) (A. Hamil-
ton). So, for example, federal statutes require airlines op-
erating in interstate commerce to hold certificates and com-
ply with federal requirements. See 49 U. S. C. §§41101,
41102, 41109. The Bankruptcy Code allows a court to alter
a creditor’s rights and a debtor’s responsibilities. See Title
11. And Title 18, Chapter 25, criminalizes counterfeiting.
See, e.g., 18 U. S. C. §473. Each of these regulations finds
its footing in a provision of Article I that empowers Con-
gress to do just that: regulate.
   The terms of RLUIPA before us rest on a different foun-
dation. As the parties agree, Congress enacted them
——————
   1 The dissent says we give “short shrift” to the principle that constitu-

tional questions are to be avoided “ ‘if there is some other ground upon
which to dispose of the case.’ ” Post, at 4 (opinion of JACKSON, J.) (quoting
Bond v. United States, 572 U. S. 844, 855 (2014)). But this is a “pruden-
tial rule,” Zobrest v. Catalina Foothills School Dist., 509 U. S. 1, 8 (1993),
not a “mechanica[l ]” one, Almendarez-Torres v. United States, 523 U. S.
224, 239 (1998). And for reasons we outline, the constitutional question
here is readily resolved by our precedents. It is also narrower than the
statutory question in an important respect: It does not require us to ad-
dress whether RLUIPA ever authorizes money damages.
                  Cite as: 609 U. S. ____ (2026)             5

                      Opinion of the Court

pursuant to what is sometimes called the Constitution’s
Spending Clause. See Sossamon v. Texas, 563 U. S. 277,
290 (2011); Brief for Petitioner 3; Brief for Respondents 2.
That provision of Article I gives Congress the “Power To lay
and collect Taxes, Duties, Imposts and Excises, to pay the
Debts and provide for the common Defence and general
Welfare of the United States.” Art. I, §8, cl. 1. At the found-
ing, some argued this language conferred on Congress the
power to regulate on nearly any topic it wishes, backed by
practically any sanction it chooses, so long as it does so in
service of the “general Welfare.” See Medina, 606 U. S., at
370. It appears that Gouverneur Morris, a leading advocate
of this reading and a member of the Committee on Style,
even tried to replace one of the draft Clause’s commas with
a semicolon with the hope of making his reading more plau-
sible. See W. Treanor, The Case of the Dishonest Scrivener:
Gouverneur Morris and the Creation of the Federalist Con-
stitution, 120 Mich. L. Rev. 1, 20–24 (2021). But a careful
proofreader—Roger Sherman—noticed the surreptitious
edit, and the Convention rejected it. See ibid.
   In the end, the founding generation rejected Morris’s
reading of the Clause just as it had his semicolon. See Me-
dina, 606 U. S., at 370–371. While the Clause may allow
Congress to raise and spend money in support of the “gen-
eral Welfare,” early authorities concluded, it did not “endow
Congress with [any] power to regulate conduct.” Ibid. (in-
ternal quotation marks omitted). Were it otherwise, they
recognized, “the ‘enumeration of specific powers’ elsewhere
in Article I would be rendered largely pointless, and the Na-
tion would trade a limited federal government for ‘an un-
limited’ one.” Id., at 371 (quoting 2 J. Story, Commentaries
on the Constitution of the United States §§904, 906, pp.
367, 369 (1833)). This Court’s precedents have long re-
spected that founding-era consensus. See Medina, 606
U. S., at 371; accord, Cummings v. Premier Rehab Keller,
596 U. S. 212, 219 (2022).
6     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

   It is an understanding that gives rise to important limi-
tations on spending legislation. Often, Congress attaches
conditions to the funds it distributes. And typically, if a re-
cipient “violates those conditions,” Congress may “termi-
nate” its agreement to provide funds. Medina, 606 U. S., at
365–366 (internal quotation marks omitted). But because
the Spending Clause confers no authority to “regulate di-
rectly,” Dole, 483 U. S., at 209, Congress cannot just dictate
whatever other sanctions it might wish for violating condi-
tions found in its Spending Clause legislation.
   Instead, additional sanctions are permissible only with
the “voluntar[y] and knowin[g]” consent of those who must
bear them. Pennhurst State School and Hospital v. Halder-
man, 451 U. S. 1, 17 (1981). Put simply, without independ-
ent regulatory authority, Congress must rely on consent. It
must ask and others must agree to face liability should they
violate a funding condition. Time and time again, from at
least 1845 to the present, our precedents have stressed the
centrality of consent in this field. Compare Searight v.
Stokes, 3 How. 151, 169 (1845) (calling spending legislation
a “compact . . . to which the state assented”), with Medina,
606 U. S., at 372 (describing spending statutes as “federal-
state agreements”).2
——————
  2 See also, e.g., Neil, Moore & Co. v. Ohio, 3 How. 720, 742 (1845) (call-

ing spending legislation “an agreement . . . between the United States
and a state”); McGee v. Mathis, 4 Wall. 143, 155 (1866) (“It is not doubted
that the grant by the United States to the State upon conditions, and the
acceptance of the grant by the State, constituted a contract” founded on
“consent of minds”); Steward Machine Co. v. Davis, 301 U. S. 548, 597–
598 (1937) (Spending legislation is an “agreemen[t] . . . with Congress”);
Pennhurst, 451 U. S., at 17 (“[L]egislation enacted pursuant to the spend-
ing power is much in the nature of a contract: in return for federal funds,
the States agree to comply with federally imposed conditions”); Gebser v.
Lago Vista Independent School Dist., 524 U. S. 274, 287 (1998) (discuss-
ing the “contractual nature” of Title IX); Barnes v. Gorman, 536 U. S.
181, 186 (2002) (“We have repeatedly characterized . . . Spending Clause
                      Cite as: 609 U. S. ____ (2026)                      7

                           Opinion of the Court

  To sort out whether consent exists—and thus whether a
condition associated with spending legislation is enforcea-
ble—we have traditionally turned to contract principles for
guidance. See Sossamon, 563 U. S., at 290 (The contract
analogy represents “a . . . limitation on” the “liability”
Spending Clause statutes may impose (emphasis deleted)).
Consider some examples. At common law, coerced assent
to a contract is invalid. See Restatement (Second) of Con-
tracts §175(1) (1979). Likewise, we have held, coerced as-
sent to a spending condition—by way of an economic “gun
to the head”—is invalid. National Federation of Independ-
ent Business v. Sebelius, 567 U. S. 519, 581–582 (2012)
(opinion of ROBERTS, C. J.); see also id., at 676–677 (joint
dissent of Scalia, Kennedy, THOMAS, and ALITO, JJ.); Dole,
483 U. S., at 211. At common law, ambiguous contractual
language is construed against its drafter. See C & L Enter-
prises, Inc. v. Citizen Band Potawatomi Tribe of Okla., 532
U. S. 411, 423 (2001). Similarly, we have concluded, Con-
gress must clearly and unambiguously alert a grant recipi-
ent to any condition on federal funds. Pennhurst, 451 U. S.,
at 17. In these ways and others, our “contract analogy”
helps safeguard against conflating Congress’s spending
power with a regulatory power. It does so by ensuring that
conditions attached to federal funds—including those pre-
scribing exposure to potential sanctions—apply only to
those who have knowingly and voluntarily agreed to them.
See Cummings, 596 U. S., at 220; cf. Medina, 606 U. S., at

——————
legislation as much in the nature of a contract” (internal quotation marks
omitted)); National Federation of Independent Business v. Sebelius, 567
U. S. 519, 577 (2012) (opinion of ROBERTS, C. J.) (“The legitimacy of Con-
gress’s exercise of the spending power . . . rests on whether the State vol-
untarily and knowingly accepts the terms of the contract” (internal quo-
tation marks omitted)); Cummings v. Premier Rehab Keller, 596 U. S.
212, 219 (2022) (“Spending Clause legislation operates based on consent:
in return for federal funds, the recipients agree to comply with federally
imposed conditions” (internal quotation marks and alteration omitted)).
8     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

371–372 (noting that an analogy to treaties, another con-
sensual instrument, may also be appropriate).3
   These settled principles resolve this case. Before us,
LDOC does not dispute that it is a recipient of federal funds.
It does not question that it has agreed to answer certain
RLUIPA suits as a condition of accepting those funds. But
as it comes to us, this case does not involve claims against
LDOC. It involves only claims against individuals in their
personal capacities. And Mr. Landor does not allege that
any of those individuals has entered any agreement with
the federal government, let alone that any of them has vol-
untarily and knowingly consented to answer private suits
under RLUIPA.
   To know that is enough to know the Court of Appeals was
correct. Mr. Landor does not have a federal RLUIPA cause
of action against the officers. Under the Spending Clause,
Congress lacks regulatory authority to impose liability on
them directly and must depend instead on consent. And
because they never agreed to answer suits like this one, Mr.
Landor’s case cannot proceed against them any more than
a breach of contract action might proceed against a defend-
ant who never formed a contract.




——————
   3 The contract analogy operates “only as a potential limitation on lia-

bility,” Cummings, 596 U. S., at 225 (internal quotation marks omitted),
meaning that consent is a necessary but not sufficient condition for con-
stitutionality. As we have explained, “the exercise of the spending power
must [also] be in pursuit of the general welfare,” spending conditions
must be “german[e] . . . to federal purposes,” and still “other constitu-
tional provisions may provide an independent bar.” Dole, 483 U. S., at
207–208 (internal quotation marks omitted). A spending agreement that
violates one of these requirements is invalid, just like “an illegal con-
tract” at common law is invalid, even if freely assented to. Kaiser Steel
Corp. v. Mullins, 455 U. S. 72, 77 (1982) (internal quotation marks omit-
ted).
                  Cite as: 609 U. S. ____ (2026)             9

                      Opinion of the Court

                            III
  Seeking to avoid this conclusion, Mr. Landor and the dis-
sent advance many arguments. But each is a variation on
the same theme. In different ways, Mr. Landor and the dis-
sent submit, the lack of voluntary and knowing consent
does not matter. And each of their arguments fails for ex-
actly that reason. Under the Spending Clause and our prec-
edents, voluntary and knowing consent is key.
                               A
   Mr. Landor begins by invoking agency and contract law.
As LDOC’s agents, he contends, the individual defendants
have a “duty to obey all reasonable directions” from their
principal. Restatement (Second) of Agency §385(1) (1957).
And, he adds, an agent’s actions can sometimes “bin[d] his
principal” to a contract when he acts “within the scope of
his authority.” United States v. Gooding, 12 Wheat. 460,
469 (1827); see also Restatement (Second) of Agency §140.
From these common law principles, Mr. Landor reasons, it
follows that the individual defendants in this case may be
held personally liable under RLUIPA. Brief for Petitioner
31–33; see also post, at 13–14, 24, n. 10 (opinion of
JACKSON, J.).
   That much does not follow even from the precepts Mr.
Landor cites. Certainly, an agent usually must obey his
principal’s directions and sometimes may bind his princi-
pal. But when a principal (here, LDOC) enters a contract
with a third party (here, the federal government), as a mat-
ter of blackletter contract law the principal’s agents do not
become “liable” to the third party for their principal’s “non-
performance.” Restatement (Second) of Agency §328 (bold-
face deleted); see also, e.g., 12 R. Lord, Williston on Con-
tracts §35:34, p. 502 (4th ed. 2012) (“The agent cannot
enforce the [principal’s] contract, nor is the agent bound by
it” (footnote omitted)); Hodgson v. Dexter, 1 Cranch 345, 363
(1803) (Marshall, C. J., for the Court) (“It is too clear to be
10    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

controverted, that . . . contracts made on account of the gov-
ernment . . . are obligatory on the government; not the [gov-
ernment’s] officer”). So, yes, LDOC might be subject to cer-
tain private suits under RLUIPA for breaching its promises
to the federal government. But under normal principles of
agency and contract law, that does not mean LDOC’s em-
ployees are as well.
   To be sure, Mr. Landor and the dissent identify ways in
which Congress could have lawfully imposed personal lia-
bility on the individual defendants. For example, Congress
could have said that, as a condition of federal funding to
LDOC, its officers had to agree to enter separate contracts
with the federal government consenting to answer suits un-
der RLUIPA. Or Congress might have conditioned its funds
on Louisiana’s agreement to exercise its own regulatory
powers to adopt a state law cause of action enforceable
against LDOC officers who violate RLUIPA. Brief for Peti-
tioner 47; cf. post, at 23–24. But these untapped possibili-
ties only underscore Mr. Landor’s bind. The first hypothet-
ical has what this case does not, namely, an agreement
between the federal government and the defendants. And
in the second hypothetical, again unlike this case, the State
would have exercised its own regulatory powers. See Ran-
dolph v. Donaldson, 9 Cranch 76, 84–85 (1815) (Story, J.,
for the Court) (describing a Virginia statute that did essen-
tially that in response to a federal request).4
                            B
   Next, Mr. Landor points to Dole. That case, he says, set
out just four requirements for Spending Clause legisla-
tion—and consent is not among them. As he reads Dole, a
——————
  4 Nor, of course, does anything prevent Louisiana from acting on its

own initiative to adopt a state law permitting damages in cases like this
one. Indeed, counsel for the individual officers before us indicated that
just such a claim may be available to Mr. Landor under state law in state
court. Tr. of Oral Arg. 113–114.
                  Cite as: 609 U. S. ____ (2026)           11

                      Opinion of the Court

condition on the grant of federal funds need only be “(1) in
pursuit of the general welfare; (2) unambiguously ex-
pressed; (3) related to the federal interest in particular na-
tional projects or programs; and (4) not in violation of other
constitutional provisions.” Brief for Petitioner 33 (citing
483 U. S., at 207–208; internal quotation marks omitted).
And because a condition requiring nonconsenting individu-
als to answer RLUIPA suits satisfies all these require-
ments, Mr. Landor concludes, his case may proceed. The
dissent appears to agree, suggesting that the voluntary and
knowing consent requirement finds no support in “any of
Dole’s prongs.” Post, at 13.
   That is incorrect. The four rules Mr. Landor extracts
from Dole apply in addition to—not instead of—the rule
that Congress may not use the Spending Clause to bind en-
tities and individuals without their knowing and voluntary
consent. That much is evident from Dole itself. As the dis-
sent admits, Dole proceeds to add a fifth rule for Spending
Clause legislation shortly after the passage Mr. Landor
cites: Funding conditions may not “pass the point at which
pressure turns into compulsion.” 483 U. S., at 211 (internal
quotation marks omitted); post, at 12–13. And that bar on
compulsion, as we have seen, serves to help ensure real con-
sent exists. See Part II, supra. The same holds true of the
clear-statement rule that Dole reaffirmed. Congress must
impose spending conditions “unambiguously,” not for no
reason, but so that participants in federally funded pro-
grams may “exercise their choice knowingly, cognizant of
the consequences of their participation.” 483 U. S., at 207
(internal quotation marks omitted). Had Dole meant to
bulldoze the consent requirement and condone consent-free
regulation under the Spending Clause, post, at 14–15, it
would have had no occasion to emphasize any of this. Nor
does Mr. Landor’s and the dissent’s consent-free gloss on
Dole merely overlook important qualifications in Dole itself.
Worse still, their misreading would pit that decision
12    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                     Opinion of the Court

against nearly two centuries’ worth of cases recognizing the
consent requirement, see n. 1, supra—hardly a sensible
way to construe our precedents.
   Responding to these problems, Mr. Landor and the dis-
sent submit that RLUIPA’s mere existence sufficed to alert
the individual defendants, or at least their employer, that
they could be held personally liable. See Brief for Petitioner
35; post, at 20. But, just like the attempt to rewrite Dole,
this argument misses the point. A Spending Clause statute
does not carry independent regulatory force. It assumes
binding effect only through “voluntar[y] and knowin[g]”
agreement. Pennhurst, 451 U. S., at 17. If someone has not
agreed to be bound, it does not matter that he may be aware
of the existence of a contract between other parties. And if
someone has not agreed to be bound, it does not matter
whether other contracting parties might wish to bind him.
Either way, he has not agreed to be bound, so he cannot be.5
                            C
  Seeking still another way around the consent require-
ment, Mr. Landor turns next to the fungibility of money.
The individual defendants, he observes, receive paychecks
from LDOC, and some of that entity’s funding comes from
the federal government. As a result, Mr. Landor submits,
the individual defendants are indirect recipients of federal
funds and, for that reason, should be deemed to have im-
plicitly consented to RLUIPA liability.

——————
  5 The dissent also attempts a factual analogy to Dole, suggesting that,

because Congress “use[d] its spending power to regulate . . . drinking
habits” there, it is free to regulate the individual officers’ conduct here.
Post, at 14. But this analogy fails for reasons we have seen. Under the
spending legislation at issue in Dole, Congress conditioned federal high-
way funds on an agreement by the States to exercise their regulatory
powers to raise their drinking ages to 21. See 483 U. S., at 205, 211.
Congress did not purport to regulate “drinking habits” directly, let alone
create a federal cause of action against underage drinkers.
                  Cite as: 609 U. S. ____ (2026)             13

                      Opinion of the Court

   This submission fails as well. Mr. Landor would have us
hold, for the first time, that so long as a penny of federal
spending makes its way to an individual, however indi-
rectly, Congress can regulate his conduct directly based on
the fiction that he has consented to regulation. None of that
is consistent with our precedents holding that funding con-
ditions in Spending Clause legislation lack independent
regulatory force but instead derive their effect from “volun-
tar[y] and knowin[g]” assent. Pennhurst, 451 U. S., at 17.
   Notice too where Mr. Landor’s theory would lead. Given
the “explo[sion]” of Spending Clause legislation in recent
decades, Medina, 606 U. S., at 373, Congress would enjoy
an effectively unbridled police power. Federal authorities
would have no need to show that their regulations repre-
sent proper exercises of Congress’s limited and enumerated
powers found in the Commerce Clause, the Bankruptcy
Clause, or any other. All they would have to show is that a
recipient who consented to a funding condition spent some
formerly federal money in transactions with a third party.
Just like that, the federal government could directly regu-
late the third party’s conduct. Take some examples. On
Mr. Landor’s theory, Congress could require coaches at uni-
versities that receive federal funds to permit transgender
athletes to play women’s sports—or face personal liability
in suits for damages. Likewise, Congress could bar doctors
at medical practices that accept federal funds from admin-
istering certain vaccines to children—again on pain of dam-
ages. See Tr. of Oral Arg. 37–43. None of that fits with our
system of limited and enumerated federal powers where all
others are reserved to the States and the people.
   The dissent criticizes us for “trot[ting] out” this “parade
of horribles.” Post, at 24. But if this is a parade, the dissent
marches right along, embracing these hypotheticals and
more. See ibid. In fact, as the dissent sees it, we should
not engage in “hairsplitting” over any “strict direct-consent-
to-liability . . . requirement” or “ill-formed” contract
14   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

analogy. Post, at 17, 25. On its view, these things are all
just “empt[y] . . . formalism[s].” Post, at 24. If Congress can
ask individuals to consent to funding conditions—or ask
States to enact laws in order to receive federal funds—Con-
gress might as well be allowed to regulate private behavior
directly. Ibid. Likely enough, that vision would have de-
lighted Gouverneur Morris. But it is one at war with the
terms of the Spending Clause, how that Clause has been
widely understood since the founding, and a long line of this
Court’s precedents. Nor is there anything “empty” about
insisting that Congress operate within the limited and enu-
merated powers the Constitution provides. This Court has
rejected views like the dissent’s many times before. See
Part II, supra. And we do so again today.
   Faced with that problem, Mr. Landor and the dissent
search for some foothold in our precedents to support their
view that the Spending Clause grants Congress direct reg-
ulatory authority. Perhaps the best they can muster is a
line snipped from Rust v. Sullivan, 500 U. S. 173 (1991),
where we said that an individual employed in a federally
funded program must “perform [his] duties in accordance
with the . . . restrictions” specified by Congress. Id., at 198;
Brief for Petitioner 32; post, at 24. But even that is of no
help. Rust did not involve an attempt to impose personal
liability on the program’s employees. The only consequence
for violating Congress’s funding conditions fell on the fed-
eral funding recipient itself and amounted to no more than
a loss of funding. See 500 U. S., at 178–179. And that is
exactly the “typical remedy” for noncompliance our cases
have long described. Medina, 606 U. S., at 373 (internal
quotation marks omitted).
   Mr. Landor and the dissent also point to Grove City Col-
lege v. Bell, 465 U. S. 555 (1984), a Title IX case. Brief for
Petitioner 32–33; post, at 15–16, n. 7. But there, too, the
only penalty was the traditional one—the “terminati[on]” of
federal funding. See Grove City College, 465 U. S., at 561.
                       Cite as: 609 U. S. ____ (2026)                        15

                            Opinion of the Court

Subsequent events illustrate as much: After losing the
case, the college decided “to exit the federal [funding] pro-
grams rather than surrender its autonomy,” a choice it was
free to make because Title IX binds only those who have
freely elected to accept federal funds. Grove City College,
Forty Years Ago, Supreme Court Case Changed GCC For-
ever (Feb. 26, 2024) (archived at https://perma.cc/2AQU-
3PME). Pretty plainly, neither Rust nor Grove City College
purported to reimagine the Spending Clause’s terms or to
rewrite our precedents construing them.6
                              D
  Finding our precedents under the Spending Clause una-
vailing, Mr. Landor and the dissent appeal to ones constru-
ing the Necessary and Proper Clause. In Sabri v. United
States, 541 U. S. 600 (2004), we held that Congress’s crimi-
nal ban on theft, fraud, or bribery against a federal funding
recipient, 18 U. S. C. §666, is a necessary and proper inci-
dent to Congress’s authority under the Spending Clause.
See 541 U. S., at 605–606; see also Salinas v. United States,
522 U. S. 52, 60–61 (1997). Mr. Landor and the dissent

——————
   6 The dissent also resorts to a supposed concession. Respondents, the

dissent says, concede “ ‘that Louisiana prison officials must comply with
RLUIPA’s substantive protections.’ ” Post, at 17 (quoting Brief for Re-
spondents 46). But the dissent omits the rest of the sentence, which clar-
ifies that respondents concede only the possibility of “injunctive relief”
against them “in their official capacities” for RLUIPA violations. Brief
for Respondents 46 (emphasis added). And, of course, an “official capac-
ity” suit is “no different from a suit against the State itself.” Printz v.
United States, 521 U. S. 898, 931 (1997) (internal quotation marks omit-
ted). Contrary to the dissent, respondents have clearly maintained all
along that they cannot “be held personally liable for an alleged RLUIPA
violation.” Brief for Respondents 46. The dissent is also wrong to sug-
gest that any LDOC official who might be sued in his official capacity can
for that reason be sued in his personal capacity. See post, at 18. The
whole point of an official-capacity suit is that it “is not a suit against the
official but rather is a suit against the official’s office.” Printz, 521 U. S.,
at 930–931 (internal quotation marks omitted).
16   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

contend this case is no different because personal liability
for nonconsenting defendants is likewise a necessary and
proper incident to RLUIPA’s policy protecting religious ex-
ercises. Brief for Petitioner 36–39; post, at 15–20.
   Much as the other arguments we have encountered mis-
conceive the Spending Clause, this one misunderstands the
Necessary and Proper Clause. The latter provision author-
izes Congress to employ “necessary and proper” means for
“carrying into Execution” its other enumerated powers.
Art. I, §8, cl. 18. Put another way, the Clause allows Con-
gress to enact laws “incidental to those powers which are
expressly given.” McCulloch v. Maryland, 4 Wheat. 316,
411 (1819). So the question is not, as Mr. Landor and the
dissent would have it, whether a personal-capacity cause of
action is incidental to RLUIPA’s policy protecting religious
exercises. The question, instead, is whether their proposed
cause of action is a necessary and proper incident to Con-
gress’s constitutionally enumerated power to spend money.
   With the question correctly framed, the distinction be-
tween this case and Sabri becomes unmistakable. Sec-
tion 666 addresses thieves, fraudsters, bribers, and others
who threaten to “fritte[r] away in graft” the funds Congress
distributes pursuant to the Spending Clause. 541 U. S., at
605. The thief steals allocated money; the fraudster ex-
tracts it under false pretenses; the briber obtains it by
greasing palms. “Congress,” Sabri held, “does not have to
sit by and accept the risk” actors of that sort pose to its con-
stitutionally enumerated spending power. Ibid. Instead,
as a necessary and proper incident to that power, Congress
may punish people who seek to sap federal funds from their
intended beneficiaries. See ibid. And Congress may do so,
Sabri concluded, even where not every misappropriated
dollar may be “ ‘traceabl[e]’ ” to “ ‘specific federal pay-
ments.’ ” United States v. Comstock, 560 U. S. 126, 147
(2010) (quoting Sabri, 541 U. S., at 605–606).
                  Cite as: 609 U. S. ____ (2026)           17

                      Opinion of the Court

   Nothing similar can be said for the cause of action Mr.
Landor and the dissent propose. Suits against nonconsent-
ing parties, like the individual officers here, might advance
RLUIPA’s laudable policy of protecting religious exercises.
But they do not safeguard from graft the federal funds Con-
gress distributes pursuant to its spending power. Recogniz-
ing as much, seemingly every Court of Appeals to address
the question has concluded that Sabri does not begin to
command the result Mr. Landor and the dissent seek. See
Tripathy v. McKoy, 103 F. 4th 106, 115 (CA2 2024) (“Sabri
is easily distinguishable”); Sharp v. Johnson, 669 F. 3d 144,
155, n. 15 (CA3 2012) (“Sabri is inapposite”); Haight v.
Thompson, 763 F. 3d 554, 570 (CA6 2014) (“RLUIPA is
nothing like the Sabri statute”); Barnett v. Short, 129 F. 4th
534, 543 (CA8 2025) (Sabri “is too dissimilar”); Wood v.
Yordy, 753 F. 3d 899, 903 (CA9 2014) (reliance on Sabri is
“not . . . sensible”).
   Nor, with Sabri out of the picture, can Mr. Landor and
the dissent explain how their proposed cause of action
would help “carr[y] into execution” Congress’s enumerated
power to spend money. McCulloch, 4 Wheat., at 434. In
truth, they don’t even try. Instead, they suggest, the Nec-
essary and Proper Clause ought to be elastic enough to al-
low the “extraction of money damages” from virtually any-
one who violates virtually any condition found in Spending
Clause legislation. Post, at 17–20, 24. But while the Nec-
essary and Proper Clause may allow Congress to enact pro-
visions actually incidental to its spending power, like those
protecting federal money against graft, it does not tolerate
outcomes that would “undermine the structure of [the fed-
eral] government established by the Constitution.” Sebe-
lius, 567 U. S., at 559 (opinion of ROBERTS, C. J.). Nor does
the Clause tolerate results that would “violat[e] the princi-
ple of state sovereignty.” Printz v. United States, 521 U. S.
898, 924 (1997). And adopting the expansive approach Mr.
18   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                    Opinion of the Court

Landor and the dissent propose would require us to violate
both rules.
   Just consider what they would have us say. On their
view, Congress may evade the consent requirement inher-
ent in its Spending Clause authority simply by invoking the
Necessary and Proper Clause. Post, at 17–20. With even a
modest federal expenditure somewhere nearby, Congress
could then proceed to regulate directly the conduct of count-
less nonconsenting individuals—not just the individual of-
ficers here, but also others like the coaches and physicians
we discussed above. See Part III–C, supra. Congress could
regulate directly, too, in innumerable spheres, including
ones traditionally reserved to the States. Really, under Mr.
Landor’s and the dissent’s logic, we would be “hard pressed
to posit any activity . . . that Congress [would be] without
power to regulate.” United States v. Lopez, 514 U. S. 549,
564 (1995). And as inconsistent as all that is with both
principles of state sovereignty and a federal government of
limited and enumerated regulatory powers, it hardly repre-
sents a “proper means for carrying into [e]xecution” Con-
gress’s spending power. Sebelius, 567 U. S., at 559 (opinion
of ROBERTS, C. J.) (internal quotation marks and some al-
terations omitted).
                             *
  Under the Spending Clause, Congress’s power to spend
money does not include the power to regulate. Spending
Clause statutes can bind only those who voluntarily and
knowingly undertake obligations by agreement with the
federal government. Because that essential element is
missing here, we affirm the judgment of the Fifth Circuit.
                                             It is so ordered.
                 Cite as: 609 U. S. ____ (2026)            1

                    JACKSON, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 23–1197
                         _________________


    DAMON LANDOR, PETITIONER v. LOUISIANA
      DEPARTMENT OF CORRECTIONS AND
            PUBLIC SAFETY, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                        [June 23, 2026]

   JUSTICE JACKSON, with whom JUSTICE SOTOMAYOR and
JUSTICE KAGAN join, dissenting.
   Congress enacted the Religious Land Use and Institu-
tionalized Persons Act of 2000 (RLUIPA) to ensure that
state and local prisons respect prisoners’ right to religious
exercise. Congress might have opted to accomplish this
through contracts with the prisons it funds. Instead, it
passed a law.
   RLUIPA requires state and local prisons that accept fed-
eral funding to accommodate prisoners’ religious exercise
more generously than the Constitution mandates. Like
many, this law comes with an enforcement mechanism: To
ensure compliance, RLUIPA authorizes an impacted pris-
oner to sue any prison employee who violates the statute.
Such suits, the statute provides, may proceed against the
employee in the employee’s individual capacity and may
yield “appropriate relief.”    42 U. S. C. §§2000cc–2(a),
2000cc–5(4)(A).
   Neither respondents nor the Court contests Congress’s
power to impose RLUIPA’s substantive directive accommo-
dating religious freedom. The majority nevertheless adopts
the peculiar position that Congress is powerless to create,
and a State is powerless to accept, the natural next step: a
damages remedy against officials who violate that directive.
2    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

   This severance of rights and remedies is a sleight of hand;
it comes by way of the majority’s full-throated endorsement
of a contract analogy even though what secures the rights
at issue is not a contract but a law. Today’s decision magi-
cally transforms a federal statute into an invitation to be
accepted or declined, deemed binding only if each particular
defendant has explicitly agreed to be penalized. No matter
that laws, as opposed to contracts, don’t ordinarily work
this way. The trick here is the majority’s effortless confla-
tion of law making and agreement making—two different
sources of binding authority.
   The majority’s analysis is spellbindingly straightforward:
Spending Clause statutes are contracts, and contracts bind
only those who consent. Ante, at 6–8. But pulling this rab-
bit out of the hat requires misconstruing the Spending
Clause and the Necessary and Proper Clause, and ignoring
decades of precedent affirming Congress’s authority to use
the power of the purse to govern. In the end, the Court re-
duces some of Congress’s greatest legislative achieve-
ments—federal laws that secure civil rights, environmental
stability, healthcare, and more—to nothing more than the
wheelings-and-dealings of an especially wealthy private
party. Because I would not so trivialize a federal statute or
the constitutional powers pursuant to which it was passed,
I respectfully dissent.
                                 I
  It is not often that a real-life incident so clearly illustrates
Congress’s reasons for adopting legislation, or the Consti-
tution’s wisdom in enabling it.
  Damon Landor’s Rastafarian faith requires him to “let
the locks of the hair of his head grow.” The Holy Bible,
Numbers 6:5 (King James Version). For a Rastafari like
Landor, locks are “the physical embodiment of . . . spiritual
identity and connection to God.” See Brief for Rastafari
Scholars as Amici Curiae 3. Landor preserved this
                  Cite as: 609 U. S. ____ (2026)            3

                     JACKSON, J., dissenting

connection—through what is known as the Nazarite Vow—
for two decades, allowing his hair to grow to his knees. And
he continued for most of a brief stint in Louisiana jails in
2020: At the two facilities that housed Landor for the bulk
of his prison time, officials accommodated his vow without
incident.
   They did so not just because it was the right thing to do
but also because federal law required it. This Court’s deci-
sion in Holt v. Hobbs, 574 U. S. 352 (2015), held that
RLUIPA mandated an accommodation for prisoners’ reli-
giously motivated beards, id., at 369–370, and thus strongly
suggested that Landor was entitled to a similar accommo-
dation. Even more on point, the Fifth Circuit—which co-
vers Louisiana—had precedent specifically requiring ac-
commodation of the Nazarite Vow. See Ware v. Louisiana
Dept. of Corrections, 866 F. 3d 263 (2017).
   Landor knew of Ware. He also knew of the threat that
jails posed to his hair (and faith) despite it. So when he was
transferred to a third jail with three weeks remaining in his
sentence, he came prepared. He carried with him a copy—
a physical, printed copy—of Ware. Upon arrival, Landor
presented the case to the intake guard. “Unmoved,” the
guard “threw Landor’s papers in the trash.” 82 F. 4th 337,
340 (CA5 2023) (case below). The guard summoned the
warden, who demanded documentation from Landor’s sen-
tencing judge corroborating his religious beliefs. “When
Landor couldn’t instantly meet that demand, two guards
carried him into another room, handcuffed him to a chair,
held him down, and shaved his head.” Ibid.
   After serving his time, Landor sued the Louisiana De-
partment of Corrections (LDOC), the jail, the warden, the
department’s secretary, and John Doe officers 1–10 in their
individual and official capacities. In addition to state-law
claims, he brought claims under RLUIPA as well as under
42 U. S. C. §1983 for violations of his First, Eighth, and
4    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

Fourteenth Amendment rights, seeking both injunctive re-
lief and damages.
   Respondents successfully moved to dismiss Landor’s com-
plaint. Landor’s release from prison, the District Court ex-
plained, mooted his bid for injunctive relief. Landor’s
RLUIPA claim thus remained only by dint of his request for
damages against the defendants in their individual capaci-
ties. But Fifth Circuit precedent held that RLUIPA does
not permit individual-capacity suits. See Sossamon v.
Texas, 560 F. 3d 316, 327–329 (2009). With Landor’s re-
maining claims failing for other reasons not relevant here,
the District Court dismissed his complaint.
   Landor had federal law on his side. And he did every-
thing he could do in real time to ensure that prison officials
knew that. We took this case to address whether Landor
can seek money damages from the officials who ignored the
law, held him down, and “uncrowned him before God.”
Brief for Rastafari Scholars as Amici Curiae 12.
                               II
   Before us, respondents offer two reasons why Landor can-
not obtain damages—one statutory and the other constitu-
tional. First, they posit that RLUIPA’s provision for “ap-
propriate relief ” against a “person acting under color of
State law,” 42 U. S. C. §§2000cc–2(a), 2000cc–5(4)(A), au-
thorizes only injunctive relief. Second, they assert that, if
RLUIPA purports to authorize individual-capacity dam-
ages lawsuits against prison officials, Congress will have
exceeded the Constitution’s limits on its spending power.
   The majority addresses only the constitutional argument,
giving short shrift to the “well-established principle . . . that
normally the Court will not decide a constitutional question
if there is some other ground upon which to dispose of the
case.” Bond v. United States, 572 U. S. 844, 855 (2014) (in-
ternal quotation marks omitted); see Ashwander v. TVA,
297 U. S. 288, 347 (1936) (Brandeis, J., concurring); Spector
                      Cite as: 609 U. S. ____ (2026)                     5

                         JACKSON, J., dissenting

Motor Service, Inc. v. McLaughlin, 323 U. S. 101, 105 (1944)
(calling this principle “more deeply rooted than any other
in the process of constitutional adjudication”). The majority
is of course correct that the practice is prudential, not inex-
orable. Ante, at 4, n. 1. But there is prudence behind a
prudential rule. The reasons for this one include “the deli-
cacy” and “comparative finality” “of [the] function” of inval-
idating a congressional enactment, and “the consideration
due to the judgment of other repositories of constitutional
power concerning the scope of their authority.” Rescue
Army v. Municipal Court of Los Angeles, 331 U. S. 549, 571
(1947).1
   So I begin by rejecting respondents’ statutory argument.
RLUIPA plainly authorizes individual-capacity lawsuits for
money damages. We have already interpreted identical
language in RLUIPA’s sister statute, the Religious Free-
dom Restoration Act of 1993 (RFRA), to allow for individ-
ual-capacity damages lawsuits. See Tanzin v. Tanvir, 592
U. S. 43 (2020). And RLUIPA’s Spending Clause underpin-
ning does not rob the statute’s text of its plain meaning.
Understanding this is necessary background for Part III,
infra, my response to the majority’s constitutional analysis.
                             A
  RLUIPA is Congress’s latest contribution to a long-run-
ning religious-liberty dialogue between Congress and this
Court. That dialogue began, for our purposes, with Employ-
ment Div., Dept. of Human Resources of Ore. v. Smith, 494
U. S. 872 (1990). Smith is a seminal case in which the
——————
  1 I have no quarrel with the premise that a court may prioritize a con-

stitutional question that is “readily resolved by our precedents” and “nar-
rower” than the statutory alternative. Ante, at 4, n. 1. But the majority’s
approach has neither virtue. As I will explain, if our precedents “readily
resolv[e]” this case, they do so in Landor’s favor. And, while the conse-
quences for RLUIPA are indeed narrower, the consequences for other
Spending Clause statutes—not to mention congressional power more
generally—are substantial.
6    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

Court held that the First Amendment does not carve out
religious exemptions from neutral and generally applicable
laws. Id., at 878–882. Smith “recognized, however, that
the political branches could shield religious exercise
through legislative accommodation.” Cutter v. Wilkinson,
544 U. S. 709, 714 (2005). Taking up the invitation, Con-
gress sought to “restore” via statute what Smith left unpro-
tected by the Constitution. Tanzin, 592 U. S., at 45. The
result was RFRA, which forbade States and the Federal
Government alike from substantially burdening religious
exercise without compelling interest and narrow tailoring.
See 42 U. S. C. §2000bb et seq.
   Importantly, RFRA was not meant to be merely advisory;
like the constitutional rights it sought to imitate, RFRA
needed bite. Thus, “RFRA made clear that it was reinstat-
ing both the pre-Smith substantive protections of the First
Amendment and the right to vindicate those protections by
a claim.” Tanzin, 592 U. S., at 50. It did so by authorizing
“appropriate relief ” for violations of its terms. §2000bb–
1(c).
   As enacted, RFRA applied to State and Federal Govern-
ments and their officials. Tanzin, 592 U. S., at 50. But
RFRA’s application to States and state officials was short
lived: This Court would soon invalidate RFRA’s application
to the States as exceeding Congress’s power under Section
5 of the Fourteenth Amendment. See City of Boerne v. Flo-
res, 521 U. S. 507 (1997).
   Partially rebuffed, Congress tried again, enacting
RLUIPA, 42 U. S. C. §2000cc et seq. In contrast to RFRA’s
“sweeping” scope, RLUIPA focused in narrowly on two dis-
crete “areas of state and local action” in which Congress
thought religious freedom faced particular threat: land-use
regulation and institutionalized persons. Sossamon v.
Texas, 563 U. S. 277, 281 (2011).
   Other than the narrower coverage, RLUIPA practically
mirrors RFRA, its “sister statute.” Ramirez v. Collier, 595
                  Cite as: 609 U. S. ____ (2026)             7

                     JACKSON, J., dissenting

U. S. 411, 424 (2022). Like RFRA, RLUIPA aims to “secure
redress” for “undue barriers” to religious exercise. Cutter,
544 U. S., at 716–717. Like RFRA, RLUIPA features “an
express private cause of action” (indeed, one “that is taken
from RFRA”). Sossamon, 563 U. S., at 282. And like
RFRA’s, RLUIPA’s express cause of action allows “[a] per-
son” who suffers a violation of the statute to “assert” the
violation “as a claim or defense in a judicial proceeding and
obtain appropriate relief against a government.” §§2000cc–
2(a), 2000bb–1(c).
  Though neither statute elaborates on what a plaintiff can
get, both specify from whom they can get it. Neither stat-
ute, that is, defines “appropriate relief.” But both define
“government” to mean, among other things, an “official” of
the relevant sovereign and any “other person acting under
color of ” the relevant sovereign’s law. §§2000cc–5(4)(A),
2000bb–2(1). Thus, like RFRA, RLUIPA creates “a claim”
for “appropriate relief against” an “official” or “other person
acting under color of ” law. §§2000cc–2(a), 2000cc–5(4)(A),
2000bb–1(c), 2000bb–2(1).
                              B
   As a matter of text, the question whether RLUIPA au-
thorizes a claim for money damages is controlled by a unan-
imous holding this Court issued just six Terms ago. In Tan-
zin, 592 U. S. 43, we held that RFRA’s materially identical
terms authorize a damages claim. Our analysis was
straightforward. First, we ascertained the who. We iden-
tified the potential defendants in a RFRA lawsuit, asking
whether “injured parties can sue Government officials in
their personal capacities.” Id., at 47. And to that question,
we said that “RFRA’s text provides a clear answer: They
can.” Ibid. RFRA authorizes lawsuits not just against a
“government” as colloquially understood, but also against
government “official[s]” and “other person[s] acting under
color of law.” §§2000bb–1(c), 2000bb–2(1). This language,
8     LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

we noted, echoes “one of the most well-known civil rights
statutes: 42 U. S. C. §1983,” which authorizes individual-
capacity lawsuits against “ ‘person[s]’ ” acting “ ‘under color
of any statute.’ ” Tanzin, 592 U. S., at 48.
   With that answer in hand, we had no trouble discerning
the what: “what ‘appropriate relief ’ entails.” Ibid. We
acknowledged that the term is “ ‘open-ended’ ” and “ ‘inher-
ently context dependent.’ ” Id., at 49 (quoting Sossamon,
563 U. S., at 286). But given the who, the term had an ob-
vious meaning: “In the context of suits against Government
officials, damages have long been awarded as appropriate
relief.” Tanzin, 592 U. S., at 49.
   So too here. Indeed, Tanzin’s reasoning applies with even
more force to RLUIPA. RLUIPA’s prison context redoubles
Tanzin’s observation that damages will often be not only an
appropriate form of relief but “the only form of relief ” avail-
able. Id., at 51. The Prison Litigation Reform Act’s exhaus-
tion requirement and strict limitations on injunctive relief
in prisons, coupled with States’ ability to transfer prisoners
and thereby moot claims for injunctive relief, mean that
withholding a damages remedy will often leave prisoners
with no remedy at all.2
   Accordingly, if RFRA’s text authorizes individual-
capacity lawsuits for money damages, RLUIPA’s must do so
as well.
                              C
   It is true, though, that while the relevant statutory text
is the same, the two statutes’ fonts of power are not. It is
on this observation that respondents rest their statutory ar-
gument. Unlike RFRA, RLUIPA relies on (as relevant here)
——————
  2 See Brief for Rights Behind Bars et al. as Amici Curiae; Brief for the

National Police Accountability Project as Amicus Curiae 17–21. Con-
gress was aware of the interaction between the Prison Litigation Reform
Act (PLRA) and RLUIPA, as it expressly preserved the PLRA in
RLUIPA. See 42 U. S. C. §2000cc–2(e).
                    Cite as: 609 U. S. ____ (2026)                  9

                       JACKSON, J., dissenting

the Spending Clause. Any divergence between the statutes’
meanings, then, would have to come not from text but from
constitutional inference—something particular to the
Spending Clause compelling us not to adopt the same read-
ing of that same statutory language. When interpreting
Spending Clause legislation, we have used a contract anal-
ogy to require that Congress express its intent to impose
conditions on the receipt of federal funds “unambiguously.”
Barnes v. Gorman, 536 U. S. 181, 186 (2002) (internal quo-
tation marks omitted). Under our precedent, this is where
contract-law principles should come into play—not as a sub-
stantive limitation on Congress’s power (as the majority
uses it today) but as a demand for statutory clarity.
   But RLUIPA’s authorization of an individual-capacity
damages remedy is unambiguous for Spending Clause pur-
poses. Our cases foreclose any argument to the contrary.
Eight years before Congress passed RLUIPA, we considered
the remedies available under Title IX, another Spending
Clause statute—but one far less clear about remedies. See
Franklin v. Gwinnett County Public Schools, 503 U. S. 60,
64–65 (1992). Where RLUIPA is strident, Title IX is coy:
That statute has no express private right of action and, ac-
cordingly, no relevant remedial language. Id., at 65–66, 71.
Yet we still concluded that it authorized damages. We ex-
plained that, even absent explicit statutory language, “we
presume the availability of all appropriate remedies unless
Congress has expressly indicated otherwise.” Id., at 66.
And we flatly rejected the notion “that the normal presump-
tion in favor of all appropriate remedies”—including dam-
ages—“should not apply because Title IX was enacted pur-
suant to Congress’ Spending Clause power.” Id., at 74; see
also id., at 69 (explaining that the available “appropriate
relief ” encompassed damages).3
——————
  3 Franklin is not alone in suggesting that monetary damages are “ap-

propriate relief ” for the violation of a spending statute. Take, for
10    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   Against Franklin, respondents point to Sossamon. But
Sossamon cannot bear anything close to the weight re-
spondents place on it. There, we held that the same
RLUIPA provision at issue today does not authorize dam-
ages in one very particular context, one with a different
who: “where the defendant is a sovereign.” Sossamon, 563
U. S., at 286. Sovereigns enjoy sovereign immunity, and
“[t]he essence of sovereign immunity . . . is that remedies
against the government differ from ‘general remedies prin-
ciples’ applicable to private litigants.” Id., at 291, n. 8. We
did not question the obvious meaning of “appropriate relief ”
in lawsuits against individuals. See ibid.4
   In short, RLUIPA leaves no need to “wonder . . . what sort
of penalties might be on the table” for a violation of its

——————
example, Barnes v. Gorman, 536 U. S. 181 (2002). There we observed
that, because of the contract analogy, “a remedy is ‘appropriate relief ’ ”
under a spending statute “only if the funding recipient is on notice that,
by accepting federal funding, it exposes itself to liability of that nature.”
Id., at 187. But we went on to explain that “[a] funding recipient is gen-
erally on notice that it is subject not only to those remedies explicitly
provided in the relevant legislation, but also to those remedies tradition-
ally available in suits for breach of contract”—including “compensatory
damages.” Ibid.
  4 Sossamon thus teaches that the term “appropriate relief ” is “ ‘inher-

ently context dependent.’ ” Tanzin, 592 U. S., at 49 (quoting Sossamon,
563 U. S., at 286). And the relevant lesson from Tanzin is that, in the
context of a suit against an individual, “appropriate relief ” plainly in-
cludes monetary damages. 592 U. S., at 49. Indeed, it can hardly mean
anything else; as damages often are not available in official-capacity law-
suits, the prospect of damages is the reason to sue officers individually.
See, e.g., Hafer v. Melo, 502 U. S. 21, 25, 27 (1991). Thus Tanzin (inter-
preting RFRA) disposed easily of Sossamon (interpreting RLUIPA), in-
voking not the different congressional powers involved but the different
defendants sued. See 592 U. S., at 51–52 (“Sossamon held that a State’s
acceptance of federal funding did not waive sovereign immunity to suits
for damages under a related statute—[RLUIPA]—which also permits
‘appropriate relief.’ The obvious difference is that this case features a
suit against individuals, who do not enjoy sovereign immunity” (citation
omitted)).
                     Cite as: 609 U. S. ____ (2026)                  11

                        JACKSON, J., dissenting

terms. Cummings v. Premier Rehab Keller, 596 U. S. 212,
220 (2022). Like RFRA, RLUIPA “reinstat[ed] both the pre-
Smith substantive protections of the First Amendment and
the right to vindicate those protections by a claim,” Tanzin,
592 U. S., at 50—with an individual damages remedy
where appropriate.5
                               III
   At long last, I arrive where today’s majority starts. On
the majority’s view, no matter how clearly Congress speaks,
all that matters is the response it elicits: Spending Clause
legislation may not make anybody liable without their ex-
press consent. And because prison officials (as opposed to
their state-prison employers) have not directly accepted
federal funds, they have not consented to being sanctioned
for their failure to follow federal law. Ante, at 6–8.
   The majority’s reasoning requires it to diminish two con-
gressional powers and contort many more precedents of this
Court. Stated simply, the Spending Clause contains no
direct-consent requirement. The power it grants Congress
“is of course not unlimited.” South Dakota v. Dole, 483 U. S.
203, 207 (1987). But neither is it so cramped as the major-
ity imagines. Most important, it is a power to legislate, not
merely to negotiate. And if the Spending Clause falls short,
the Necessary and Proper Clause supplies the additional
power Congress needs to bind prison officials—state agents
——————
   5 Because our Spending Clause precedent requires Congress to trans-

late its intent unambiguously into the statute, I do not rely heavily on
RLUIPA’s legislative history. But make no mistake: Congress indisput-
ably intended RLUIPA to authorize individual-capacity lawsuits for
money damages. See, e.g., H. R. Rep. No. 106–219, p. 29 (1999) (RLUIPA
“track[s] RFRA, creating a private cause of action for damages, injunc-
tion, and declaratory judgment”); 146 Cong. Rec. 19123 (2000) (state-
ment of Rep. Canady) (same); Religious Liberty: Hearing before the Sen-
ate Committee on the Judiciary, 106th Cong., 1st Sess., p. 91 (1999)
(statement of Douglas Laycock) (“Appropriate relief includes declaratory
judgments, injunctions, and damages”).
12   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

whose compliance is critical to RLUIPA’s effective imple-
mentation.
                               A
   The Spending Clause is embedded within Congress’s first
enumerated power. It gives Congress the “Power To lay and
collect Taxes, Duties, Imposts and Excises, to pay the Debts
and provide for the common Defence and general Welfare
of the United States.” U. S. Const., Art. I, §8, cl. 1.
   The authority to spend money for the “general Welfare”
naturally includes the power to determine the general wel-
fare and to ensure that expenditures further it. See, e.g.,
Helvering v. Davis, 301 U. S. 619, 645 (1937). Thus, “Con-
gress has broad power under the Spending Clause of the
Constitution to set the terms on which it disburses federal
funds.” Cummings, 596 U. S., at 216. To exercise that
spending power, Congress passes laws conditioning federal
funding on compliance.
   The product is, of course, federal law like any other—en-
acted via bicameralism and presentment, and constituting
“the supreme Law of the Land.” U. S. Const., Art. VI, cl. 2;
see Armstrong v. Exceptional Child Center, Inc., 575 U. S.
320, 324 (2015); Health and Hospital Corporation of Marion
Cty. v. Talevski, 599 U. S. 166, 171–172 (2023). And such
law may further not only Congress’s other enumerated pow-
ers but also ends otherwise beyond Congress’s reach. See
United States v. Butler, 297 U. S. 1, 66 (1936).
   For decades, the Court has used a consistent yardstick to
measure the constitutionality of Spending Clause legisla-
tion. We crystallized that metric in Dole, 483 U. S. 203.
Funding conditions in laws enacted pursuant to the Spend-
ing Clause must be in pursuit of the general welfare; unam-
biguously expressed; related to the federal interest; and not
in violation of other constitutional provisions. Id., at 207–
208. The “financial inducement offered by Congress” also
                  Cite as: 609 U. S. ____ (2026)           13

                     JACKSON, J., dissenting

may not be “so coercive as to pass the point at which ‘pres-
sure turns into compulsion.’ ” Id., at 211.
  When Congress “exercise[s] its Spending Power,” we have
long understood, “Dole provides the appropriate framework
for assessing . . . constitutionality.” United States v. Amer-
ican Library Assn., Inc., 539 U. S. 194, 203, n. 2 (2003)
(opinion of Rehnquist, C. J.). But neither respondents nor
the majority attempts to invalidate RLUIPA under any of
Dole’s prongs. Instead, they devise a new one: Spending
Clause legislation can make liable only those who have di-
rectly and expressly consented to be made liable. See ante,
at 8.
  This new rule starts from a kernel of truth. Spending
Clause legislation does not take effect of its own accord. It
requires a funding recipient to accept funds, and thereby to
consent to the accompanying conditions. In this way,
spending legislation differs from other federal law, which
may command without offering.
  From that kernel, though, the majority sprouts a dra-
matic innovation. The conditions prescribed in Spending
Clause legislation, the majority insists, may not bind any-
body but the funding recipient itself, no matter the recipi-
ent’s relationship to the nonrecipient (i.e., sovereign, em-
ployer, or, as here, both), and no matter how essential the
conditions are to Congress’s spending program.
                              B
  This novel consent requirement discards decades of
Spending Clause and Necessary and Proper Clause prece-
dent. This Court has upheld spending statutes that make
RLUIPA look modest in its reach.
  Recall that the individuals RLUIPA exposes to liability
are state prison officials. These are agents of the State who
voluntarily seek the State’s employ and wield its power.
The State—the funding recipient—thus exercises authority
over them in two ways. As their employer, the State can
14    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

place conditions on their employment. And as a sovereign,
the State can govern their behavior. Under our precedents,
either should have sufficed. With both, this is an easy case.
   Start with Dole itself. Dole upheld a federal law condi-
tioning highway funding on States raising the legal age for
purchasing or publicly possessing alcohol—that is, on
States forbidding a category of behavior for young adults.
483 U. S., at 205. Underage drinkers are not the Federal
Government’s contracting partners. Cf. id., at 218 (O’Con-
nor, J., dissenting) (arguing that the law was unconstitu-
tional because it was not “a condition determining how fed-
eral highway money shall be expended” but rather “a
regulation determining who shall be able to drink liquor”).
But we held that Congress could nonetheless use its spend-
ing power to regulate their drinking habits in this fashion.
   Thus, one need look no further than this Court’s most ca-
nonical Spending Clause case to cast doubt on the major-
ity’s insistence on individual consent. “If South Dakota can
agree to criminalize the behavior of its 19-year-old bourbon
enthusiasts, it’s unclear why Louisiana cannot agree to
make its prison officials liable for forcibly shaving Damon
Landor’s head.” 93 F. 4th 259, 265 (CA5 2024) (Oldham, J.,
dissenting from denial of rehearing en banc).6
   The majority maintains that this is not Dole. RLUIPA is
different, the majority says, because Congress has bound
individual prison officials directly whereas the federal law
in Dole did not act directly upon nonrecipients. Instead,
that law “influence[d] a State’s legislative choices,” causing
the State to regulate young drinkers. New York v. United
States, 505 U. S. 144, 167 (1992) (discussing Dole); ante, at
12, n. 5. But that distinction makes no relevant difference.
Either way, Congress has used its spending power to

——————
   6 See also Haight v. Thompson, 763 F. 3d 554, 570 (CA6 2014) (Sutton,

J.) (pointing out that the position the majority embraces today “is not
consistent with Dole” or multiple other precedents of this Court).
                      Cite as: 609 U. S. ____ (2026)                    15

                         JACKSON, J., dissenting

regulate individuals without their express consent. In Dole,
the State exposed the individual to liability in exchange for
federal funds. So too here.
   Regardless, in subsequent cases, we have not been
squeamish about recognizing Congress’s authority to regu-
late nonrecipients directly in service of protecting “the in-
tegrity and proper operation of the federal program.” Sa-
linas v. United States, 522 U. S. 52, 61 (1997). In Salinas,
for instance, we harbored “no serious doubt about the con-
stitutionality” of an anti-bribery statute that regulated in-
dividuals situated identically to the prison officials here—
i.e., “state and local officials employed by agencies receiving
federal funds.” See id., at 58, 60. (Salinas thus checked
both the “employer” and “sovereign” boxes.) And in Sabri
v. United States, 541 U. S. 600 (2004), we went further still,
explaining that the Spending Clause, buttressed by the
Necessary and Proper Clause, empowered Congress to
criminalize private individuals’ bribery of state and local of-
ficials employed by entities receiving federal funds, see id.,
at 605. The private individuals were complete strangers to
the funding relationship between the Federal Government
and the funded entities. No matter. Congress, we ex-
plained, can “bring federal power to bear directly on indi-
viduals” where necessary “to see to it that taxpayer dollars
appropriated under [the Spending Clause] are in fact spent
for the general welfare.” Id., at 605, 608.7
——————
  7 Our statutory-interpretation cases teach the same lesson.         Take
Grove City College v. Bell, 465 U. S. 555 (1984), where we held that Title
IX—a Spending Clause statute forbidding sex discrimination by recipi-
ents of federal funds—regulates a college that “accepts no direct [federal]
assistance but enrolls students who receive federal grants,” id., at 558.
We reasoned that the language of the statute “contain[ed] no hint that
Congress perceived a substantive difference between direct institutional
assistance and aid received by a school through its students.” Id., at 564;
see also National Collegiate Athletic Assn. v. Smith, 525 U. S. 459, 468
(1999) (“Entities that receive federal assistance, whether directly or
through an intermediary, are recipients within the meaning of Title IX”).
16    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   So it is not I but the majority that jettisons “a long line of
this Court’s precedents.” Ante, at 14. We have lived for
decades in a world in which Congress has been able to use
its spending power to reach beyond direct recipients of fed-
eral funds. And it has done so repeatedly. In the Federal
Nursing Home Reform Act, for instance, Congress author-
ized civil penalties against individual employees of feder-
ally funded nursing homes who falsify resident assess-
ments.       See 42 U. S. C. §1396r(b)(3)(B)(ii).         In the
Emergency Medical Treatment and Active Labor Act, Con-
gress authorized civil penalties against doctors in federally
funded hospitals who negligently violate the law’s require-
ments. See 42 U. S. C. §1395dd(d)(1)(B). And in Title X of
the Public Health Service Act, Congress authorized fines
and imprisonment for state officers and employees who co-
erce abortion or sterilization by threatening the loss of fed-
erally funded benefits. See 42 U. S. C. §300a–8.
   These are important measures, for obvious reasons. They
are also required if these laws’ intended ends are to be ac-
complished, for a “State can act only through its officials,”
and an institution only through its employees. Pennhurst
State School and Hospital v. Halderman, 465 U. S. 89, 114,
n. 25 (1984); cf. Printz v. United States, 521 U. S. 898, 931
(1997) (“To say that the Federal Government cannot control
the State, but can control all of its officers, is to say nothing
of significance”). Congress reasonably seeks to ensure
——————
We never suggested, much less held, that such a statutory scheme raised
constitutional concerns. In fact, the college, lacking the gumption of to-
day’s Court, argued only that Congress had not bound indirect recipients
through Title IX, not that it could not. The more extreme position (the
one the majority adopts now) occurred to nobody.
  The majority makes hay of the college’s subsequent decision to stop
welcoming students who received federal financial aid and therefore to
escape Title IX. Ante, at 14–15. Of course, this same option is available
to prison officials, who may likewise “exit the federal [funding]
progra[m]” by seeking alternative employment. Ante, at 15 (internal
quotation marks omitted).
                     Cite as: 609 U. S. ____ (2026)                   17

                        JACKSON, J., dissenting

compliance with its directives by giving individual actors
imbued with state authority a personal stake in the matter.
Nothing in the Constitution prevents Congress from de-
signing Spending Clause statutes in this fashion.
                               C
   That should spell the end of this dispute. The Spending
Clause has no strict direct-consent-to-liability requirement,
and respondents offer no reason to think RLUIPA fails the
traditional Dole test. But Congress has still more reser-
voirs of power from which to draw. The Necessary and
Proper Clause “empowers Congress to enact laws in effec-
tuation of its enumerated powers”—including the spending
power—“that are not within its authority to enact in isola-
tion.” Gonzales v. Raich, 545 U. S. 1, 39 (2005) (Scalia, J.,
concurring in judgment); see Sabri, 541 U. S., at 605.
Should RLUIPA’s individual-capacity remedy require more
power than the Spending Clause provides, the Necessary
and Proper Clause supplies it.
   This conclusion flows from a concession respondents
make without reservation: “[T]here is no dispute that Lou-
isiana prison officials must comply with RLUIPA’s substan-
tive protections.” Brief for Respondents 46. Respondents,
in other words, do not place prison officials beyond
RLUIPA’s substantive reach; accepting that RLUIPA im-
poses a duty on prison officials, they just seek to “exempt”
those officials “from any of its liability provisions.” Depart-
ment of Agriculture Rural Development Rural Housing Ser-
vice v. Kirtz, 601 U. S. 42, 62 (2024).
   There is “no proper place in our jurisprudence” for this
“wholly artificial” distinction. Ibid. (internal quotation
marks omitted).8 The Necessary and Proper Clause makes
——————
  8 What two years ago was “wholly artificial” today becomes the crux of

the majority’s decision, which depends entirely on divorcing law from li-
ability, right from remedy.      See, e.g., ante, at 14–15, and n. 6
18    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

sure of it. That Clause enables “Congress to provide, by
suitable penalties, for the enforcement of all legislation nec-
essary or proper to the execution of powers with which it is
intrusted.” United States v. Fox, 95 U. S. 670, 672 (1878).
So where an enumerated power enables Congress to pre-
scribe rules, the Necessary and Proper Clause empowers
Congress to “give those rules force by imposing conse-
quences on [those] who disobey them.” United States v. Ke-
bodeaux, 570 U. S. 387, 400 (2013) (ROBERTS, C. J., concur-
ring in judgment); McCulloch v. Maryland, 4 Wheat. 316,
416 (1819) (attributing to the Necessary and Proper Clause
the government’s ability to “punish any violation of its
laws”); Ex parte Yarbrough, 110 U. S. 651, 658–659 (1884).
That is all RLUIPA’s cause of action does. It authorizes the
extraction of money damages for behavior Congress conced-
edly may proscribe.
   Notably, the majority does not contest the premise that
Louisiana’s prison officials must abide by RLUIPA. And it
admits, as it must, that a court may order prison officials in
their official capacities to comply with RLUIPA. See ante,
at 15, n. 6. But this leaves the majority in an odd spot. In
the majority’s view, the prison official’s relationship to the
State is close enough that “the actions of ” the official are
“the actions of the [State] itself ” such that the official may
stand in for the State in litigation, Brandon v. Holt, 469
U. S. 464, 472 (1985), but distant enough that the State’s
consent to damages liability on the official’s behalf means
nothing at all. There is no rational basis for that distinc-
tion.
   Battling uphill, the majority reworks the Necessary and
Proper Clause. The majority contends that, rather than al-
low Congress to enforce statutes passed pursuant to other

——————
(distinguishing precedents of this Court and respondents’ concession on
the grounds that they “did not involve an attempt to impose personal
liability”).
                     Cite as: 609 U. S. ____ (2026)                  19

                        JACKSON, J., dissenting

enumerated powers, the Necessary and Proper Clause must
facilitate the enumerated power itself. Ante, at 16. Only if
a regulation is “a necessary and proper incident to Con-
gress’s constitutionally enumerated power,” the majority
insists, does the Necessary and Proper Clause justify it.
Ibid.
   This is a deft maneuver but not a successful one, as it
diverts our focus to the wrong relationship. “The relevant
question is simply whether the means chosen are ‘reasona-
bly adapted’ to the attainment of a legitimate end” sought
under an enumerated power, not whether the means chosen
are incidental to the power itself. Gonzales, 545 U. S., at 37
(Scalia, J., concurring in judgment) (quoting United States
v. Darby, 312 U. S. 100, 121 (1941); emphasis added); see
also Kebodeaux, 570 U. S., at 406 (Scalia, J., dissenting)
(“[W]hat is necessary and proper to enforce a statute validly
enacted pursuant to an enumerated power is . . . itself nec-
essary and proper to the execution of an enumerated
power”).
   Said otherwise, “we look to see whether the statute con-
stitutes a means that is rationally related to the implemen-
tation of a constitutionally enumerated power.” United
States v. Comstock, 560 U. S. 126, 134 (2010) (emphasis
added). This is why “the Necessary and Proper Clause . . .
authorizes Congress, in the implementation of other ex-
plicit powers, to create federal crimes, to confine offenders
to prison” and more, Kebodeaux, 570 U. S., at 394–395—not
because the power to imprison is incidental to the power to,
say, regulate commerce, but because the power to imprison
gives Congress the ability to “ ‘make [its] regulation[s] effec-
tive,’ ” Gonzales, 545 U. S., at 36 (Scalia, J., concurring in
judgment) (quoting United States v. Wrightwood Dairy Co.,
315 U. S. 110, 119 (1942)).9
——————
  9 Even viewed from a first-principles standpoint, the majority’s fram-

ing makes little sense. The majority gives the Necessary and Proper
20    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

   The majority resorts finally to abstraction, retorting that
the Necessary and Proper Clause does not permit Congress
to “undermine the structure of [the federal] government es-
tablished by the Constitution” or “violat[e] the principle of
state sovereignty.” Ante, at 17 (alterations in original; in-
ternal quotation marks omitted). I do not contest these as-
sertions. It is the Court’s application of them here that is
baffling, since exposing state officials to damages liability
does nothing so dramatic. That state officials might be vul-
nerable to federally imposed money judgments for unlawful
conduct is a common feature of our federal system. See,
e.g., 42 U. S. C. §1983. RLUIPA’s imposition of damages
liability for state officials comes as no surprise to States or
their agents and by no means offends state sovereignty.
The State chose to accept the funds with full knowledge of
RLUIPA’s command, and the officials in turn chose to ac-
cept state employment with full knowledge of federal law.
   That the Necessary and Proper Clause may extend the
reach of the Spending Clause (as we have long recognized)
does not, of course, mean that congressional power is un-
bounded. Contra, ante, at 18. But it does mean (as again
we have long recognized) that where Congress may require
compliance via law it may also secure compliance via impo-
sition of liability, including damages.
——————
Clause no independent work to do, rendering it superfluous rather than
treating it as the adjunct the Framers envisioned. See, e.g., McCulloch
v. Maryland, 4 Wheat. 316, 417 (1819) (commenting that, although “the
right to carry the mail, and to punish those who rob it, is not indispensa-
bly necessary to” the power “ ‘to establish post offices and post roads,’ ”
the Necessary and Proper Clause affords Congress the power to take
those steps); see also Letter from A. Hamilton to G. Washington, Opinion
on the Constitutionality of an Act To Establish a Bank (Feb. 23, 1791),
in 8 Papers of Alexander Hamilton 70 (H. Syrett & J. Cooke eds. 1965)
(“The clause . . . is evidently designed to place on an unequivocal footing
the power of the government to employ all the means fairly relative to
the execution of its specified powers and to the fulfilment of the objects
entrusted to its direction”).
                  Cite as: 609 U. S. ____ (2026)           21

                     JACKSON, J., dissenting

                               IV
   I do not doubt that difficult questions about the limits of
Congress’s spending power exist. But, as I have explained
thus far, this case offered no opportunity to resolve them.
Respondents seek to limit the Spending Clause in a manner
directly contrary to our precedents. And when it comes to
enforcement of a concededly proper exercise of congres-
sional power, the Necessary and Proper Clause supplies
any authority that the Spending Clause cannot.
   Let us, then, step back and examine the origin and con-
sequences of the majority’s unprecedented invocation of a
“categorical font-of-power condition” limiting Congress’s
reach under the Spending Clause. Talevski, 599 U. S., at
192 (rejecting a similar effort). This limitation is not lo-
cated in the Constitution’s text; “[i]t is hard to imagine a
broader statement of the scope of Congress’s power” than
the Spending Clause. E. Chemerinsky, Protecting the
Spending Power, 4 Chapman L. Rev. 89, 93 (2001). And it
is not in our precedents either—today’s Court cannot suc-
cessfully explain the decisions of yesterday’s. Rather, it ap-
pears that the seeds of the majority’s dramatic weakening
of the spending power were first planted some time ago, and
are rooted in a loose contract analogy the Court has repeat-
edly cautioned against taking as anything more. The ma-
jority supercharges that analogy here and now, ensuring
that it comes to full flower. This may prove to be a conse-
quential choice.
                              A
   The contract analogy derives from the insight that
Spending Clause legislation requires acceptance of federal
funds before it can take hold, making it “much in the nature
of a contract.” Pennhurst State School and Hospital v. Hal-
derman, 451 U. S. 1, 17 (1981). Until today, we have used
that insight in two relatively modest ways, both as inter-
pretive aids. First, the contract analogy gives rise to a
22   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

clear-notice requirement. See, e.g., id., at 24–25; Part II–C,
supra. Second, the analogy offers background principles to
fill in gaps where a statute falls short of the required clar-
ity. See, e.g., Cummings, 596 U. S., at 220, 221 (explaining
that a Spending Clause statute that is “silent as to availa-
ble remedies” presumptively authorizes “the usual contract
remedies” (emphasis deleted)); Barnes, 536 U. S., at 187 (“A
funding recipient is generally on notice that it is subject not
only to those remedies explicitly provided in the relevant
legislation, but also to those remedies traditionally availa-
ble in suits for breach of contract”).
   But even when using the analogy for those purposes, the
Court has always viewed it cautiously. We have consist-
ently refused to “imply . . . that suits under Spending
Clause legislation are suits in contract, or that contract-law
principles apply to all issues that they raise.” Id., at 189,
n. 2; see also Sossamon, 563 U. S., at 290 (same); Cum-
mings, 596 U. S., at 226 (declining to “incorporat[e] the law
of contract remedies wholesale”). Some Justices have war-
ily accepted the contract analogy in certain contexts while
cautioning that it “may fail” elsewhere. Barnes, 536 U. S.,
at 191 (Souter, J., concurring). Others have protested its
use as “novel.” Id., at 192 (Stevens, J., concurring in judg-
ment); Talevski, 599 U. S., at 193 (BARRETT, J., joined by
ROBERTS, C. J., concurring). Still others have cast doubt on
it as “an imperfect way” to interpret Spending Clause legis-
lation. Cummings, 596 U. S., at 230 (KAVANAUGH, J.,
joined by GORSUCH, J., concurring). In all events, the Court
has always rejected the idea—though pressed with vigor in
dissent—that Spending Clause legislation “is nothing more
than a contractual offer.” Talevski, 599 U. S., at 196
(THOMAS, J., dissenting); see also id., at 229 (criticizing the
Court for “holding that spending conditions are not merely
contractual”).
   At most, the Court has accepted that Spending Clause
legislation has “a contractual aspect” while steadfastly
                    Cite as: 609 U. S. ____ (2026)               23

                       JACKSON, J., dissenting

insisting that such laws nonetheless “cannot be viewed in
the same manner as a bilateral contract governing a con-
crete transaction.” Bennett v. Kentucky Dept. of Ed., 470
U. S. 656, 669 (1985); accord, B. Fahey, Federalism by Con-
tract, 129 Yale L. J. 2326, 2330 (2020) (noting spending
statutes’ “dual character” as “both contract-like instru-
ments and public lawmaking instruments”). After all,
“[u]nlike normal contractual undertakings,” Spending
Clause laws are “statut[es] . . . expressing the judgment of
Congress concerning desirable public policy.” Bennett, 470
U. S., at 669. Having undergone bicameralism and present-
ment, Spending Clause legislation “is legislation, in the
end, not a buy-sell transaction.” T. Seligmann, Muddy Wa-
ters: The Supreme Court and the Clear Statement Rule for
Spending Clause Legislation, 84 Tulane L. Rev. 1067, 1120
(2010).
   Today the Court abandons its warranted caution. An in-
terpretive guide becomes a substantive limitation on Con-
gress’s authority, as the Court takes a step toward embrac-
ing what one scholar has criticized as the “strong contract
theory”: the radical notion that Spending Clause legislation
is not just “ ‘in the nature of ’ a contract,” but is in fact “noth-
ing but a contract.” S. Bagenstos, Spending Clause Litiga-
tion in the Roberts Court, 58 Duke L. J. 345, 385 (2008)
(quoting Pennhurst, 451 U. S., at 17).
   Strange as it seems, today’s majority appears to mean it.
One indication is the majority’s concession that “Congress
could have lawfully imposed personal liability on the indi-
vidual defendants” if it had tweaked RLUIPA to better con-
form to the Court’s understanding of the limits of contract
law. Ante, at 10. “For example,” the majority allows, “Con-
gress could have said that, as a condition of federal funding
to LDOC, its officers had to agree to enter separate con-
tracts with the federal government consenting to answer
suits under RLUIPA.” Ibid. “Or,” the majority posits, “Con-
gress might have conditioned its funds on Louisiana’s
24    LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                      PUBLIC SAFETY
                    JACKSON, J., dissenting

agreement to exercise its own regulatory powers to adopt a
state law cause of action enforceable against LDOC officers
who violate RLUIPA.” Ibid. Those arrangements, the ma-
jority assures us, would have sufficed for Spending Clause
purposes. But the one Congress chose fails because it hews
insufficiently to the tenets of binding contractual relation-
ships.
   Of course, the arrangement Congress chose is not far off
from the “untapped possibilities” the Court prefers. Ibid.
RLUIPA is no secret. Prison officials know when they sign
up to work at a state prison that they must obey the law or
face the consequences the law prescribes; this is simply “a
consequence of their decision to accept employment.” Rust
v. Sullivan, 500 U. S. 173, 199 (1991); Brief for Former Cor-
rectional Officials as Amici Curiae 13–16. What meaning-
ful difference would it make to have them sign a contract
attesting to that knowledge?10 Similarly, it makes no mean-
ingful difference for Congress to require a State to flex its
own legislative power to bind state officials rather than al-
low the Federal Government to make state officials liable
directly, as federal law so often does. The majority, in other
words, deals in form, not substance.
   The emptiness of the majority’s formalism is further il-
lustrated by the parade of horribles it trots out. The
——————
   10 Such attestation would likely be unnecessary even if this were a true

contract case. Under the doctrine of implied consent, courts may recog-
nize an agreement “which, although not embodied in an express contract,
is inferred . . . from conduct of the parties showing, in the light of the
surrounding circumstances, their tacit understanding.” Baltimore &
Ohio R. Co. v. United States, 261 U. S. 592, 597 (1923). “[A] reasonably
competent public official should know the law governing his conduct.”
Harlow v. Fitzgerald, 457 U. S. 800, 819 (1982); see also Heckler v. Com-
munity Health Services of Crawford Cty., Inc., 467 U. S. 51, 63 (1984)
(noting “the general rule that those who deal with the Government,” and
especially “those who seek public funds,” “are expected to know the law”).
And prison officials manifest their assent to RLUIPA by showing up to
work each day.
                     Cite as: 609 U. S. ____ (2026)                   25

                        JACKSON, J., dissenting

majority warns that, if RLUIPA’s individual-capacity dam-
ages provision is constitutional, Congress could subject col-
lege coaches to liability if they refuse “to permit
transgender athletes to play women’s sports,” or make doc-
tors personally liable if they “administe[r] certain vaccines
to children.” Ante, at 13. What the majority intends by
these examples is not clear. Congress could of course im-
pose these conditions on the colleges and medical practices
themselves, assuming they receive federal funds and the
laws are otherwise constitutional and not coercive.11 Con-
gress’s reach thus remains the same either way; all that
changes is whether noncompliant coaches and doctors lose
their jobs (in the majority’s world) or become liable in dam-
ages (in Congress’s, and therefore mine).
   So the Court’s ruling apparently boils down to dissatis-
faction with the precise way Congress structured RLUIPA.
Such hairsplitting undervalues Congress’s lawmaking pre-
rogative; we ought not substitute our rigid contract-based
preferences for Congress’s considered statutory design.
“Some play must be allowed for the joints of the machine,
and it must be remembered that legislatures are ultimate
guardians of the liberties and welfare of the people in quite
as great a degree as the courts.” Missouri, K. & T. R. Co. v.
May, 194 U. S. 267, 270 (1904). Taking this wisdom to
heart, the Court usually exhibits a well-founded “reticence
to invalidate the acts of the Nation’s elected leaders.” Na-
tional Federation of Independent Business v. Sebelius, 567
U. S. 519, 537–538 (2012) (opinion of ROBERTS, C. J.). In
my view, an ill-formed analogy to contract law is a regret-
table basis on which to turn reticence into enthusiasm.



——————
  11 A Title IX case currently pending before us asks whether Congress

imposed the majority’s first “hypothetical” condition on federally funded
educational institutions. See West Virginia v. B. P. J., No. 24–43.
26   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

                               B
  Ultimately, I fear that the majority has now conjured an
apparition to replace a once-efficacious vision of Congress’s
spending power—a constitutional grant of authority that is
central to the design and functioning of our federal system.
History demonstrates that power’s significance.
  Under the Articles of Confederation, the power to tax re-
mained with the States. See Art. VIII; see also Art. II. This
arrangement left the Federal Government largely depend-
ent upon the States, eager for their cooperation but strug-
gling to secure it. D. Spencer, Sanctuary Cities and the
Power of the Purse: An Executive Dole Test, 106 Iowa
L. Rev. 1209, 1218 (2021). Thus, one major motivation for
the new Constitution was to give the Federal Government
the tools “to better incentivize states to work collectively for
the good of the entire Union.” Ibid. Granting Congress the
power to tax allowed the Federal Government to amass the
resources it needed to dangle those incentives. And grant-
ing Congress the power to spend allowed the Federal Gov-
ernment to follow through.
  Follow through it has. We owe to the Spending Clause,
for example, Title VI of the Civil Rights Act of 1964—a law
with which “few pieces of federal legislation rank in signif-
icance.” Bostock v. Clayton County, 590 U. S. 644, 649
(2020); see Students for Fair Admissions, Inc. v. President
and Fellows of Harvard College, 600 U. S. 181, 308 (2023)
(GORSUCH, J., concurring). We owe to the Spending Clause,
too, the relative cleanliness of our Nation’s air, see 42
U. S. C. §7401 et seq. (Clean Air Act), and the relative
health of our Nation’s populace, 42 U. S. C. §1395 et seq.;
§1396 et seq. (Medicare and Medicaid Acts). “Other exam-
ples, spanning virtually every domain of national and state
policy, abound.” Talevski, 599 U. S., at 198 (THOMAS, J.,
dissenting).
  While today’s decision does not endanger those laws di-
rectly, the majority’s reasoning casts a shadow that will not
                 Cite as: 609 U. S. ____ (2026)           27

                    JACKSON, J., dissenting

easily be escaped. No one knows what changes lie at the
end of a strict contract-law construction of the spending
power. But, as Members of this Court have long recognized,
importing contract principles wholesale could have “poten-
tially far-reaching consequences.” Barnes, 536 U. S., at 192
(Stevens, J., concurring in judgment).
   Indeed, it is our rejection of the strict contract analogy
that renders Spending Clause rights enforceable under
§1983. See Talevski, 599 U. S., at 229 (THOMAS, J., dissent-
ing); accord, D. Engdahl, The Contract Thesis of the Federal
Spending Power, 52 S. D. L. Rev. 496, 510 (2007). Simi-
larly, contracts presumably may not preempt state law, yet
Spending Clause legislation can do so. See, e.g., Dalton v.
Little Rock Family Planning Services, 516 U. S. 474, 476
(1996) (per curiam); Bennett v. Arkansas, 485 U. S. 395, 396
(1988) (per curiam); Philpott v. Essex County Welfare Bd.,
409 U. S. 413, 417 (1973); Townsend v. Swank, 404 U. S.
282, 286 (1971). And Congress likely could not hitch its
Necessary and Proper power to a mere contract, either, see
Engdahl, 52 S. D. L. Rev., at 532, but we have blessed just
this cocktail of enumerated powers, see Sabri, 541 U. S., at
605.
   This means that today’s decision might well land a seri-
ous blow to Congress’s effectiveness. Or it could end up
merely a bothersome statutory drafting guide: If Congress
adapts its Spending Clause legislation to fit the Court’s
newly prescribed formulas—and if the Court lets it do so—
then the majority’s robotic importation of contract princi-
ples will have little real-world effect. Either way, though,
“[t]he suggestion that [Spending Clause] statutes are not
‘law’ on the same level as other pieces of legislation makes
little sense.” See A. Gluck, Our [National] Federalism, 123
Yale L. J. 1996, 2031 (2014). And it makes even less sense
of the jurisprudence that has developed for decades around
those laws, to the great benefit of the American people.
28   LANDOR v. LOUISIANA DEPT. OF CORRECTIONS AND
                     PUBLIC SAFETY
                   JACKSON, J., dissenting

  As for RLUIPA itself, the consequences are more predict-
able. Prisoners like Landor who suffer violations of their
religious freedom in state prisons—no matter how bla-
tant—will often be left remediless. And encroachments on
prisoners’ statutory rights are likely to happen with fair fre-
quency, as state-empowered prison officials will have little
incentive to abide by federal law, even if it is handed to
them on a piece of paper.
                         *    *    *
  When Sossamon concluded that RLUIPA did not expose
States and their institutions to damages liability, JUSTICE
SOTOMAYOR lamented that the Court’s holding left RLUIPA
plaintiffs “to seek enforcement of [their] rights with one
hand tied behind their backs.” 563 U. S., at 303 (dissenting
opinion). Today the Court ties the other hand.
  To be clear, the Court’s decision does not eliminate all
damages liability from RLUIPA. See ante, at 4, n. 1. A pris-
oner who happens to be housed in a local rather than state
jail may recover damages from the municipality, which nei-
ther enjoys sovereign immunity, see Jinks v. Richland
County, 538 U. S. 456, 466 (2003), nor suffers from the
indirect-recipient defect the Court identifies, see Barnett v.
Short, 129 F. 4th 534, 542 (CA8 2025). Furthermore,
RLUIPA channels the commerce power, rather than the
spending power, in some of its applications. See 42 U. S. C.
§2000cc–1(b)(2). So the rare RLUIPA plaintiff who finds a
Commerce Clause hook may recover damages, too. See
Tripathy v. McKoy, 103 F. 4th 106, 115, n. 6 (CA2 2024).
But Congress did not enact such a patchwork scheme, and
the Constitution does not demand it.
  Yet the Court imposes such a scheme today. The Court
does so by concluding that, even where Congress can legis-
late under the Spending Clause, it may be left powerless to
enforce that legislation in the way it chooses. This
                  Cite as: 609 U. S. ____ (2026)           29

                     JACKSON, J., dissenting

development is as new as it is peculiar, and it devalues prec-
edent and congressional authority alike.

```

---
