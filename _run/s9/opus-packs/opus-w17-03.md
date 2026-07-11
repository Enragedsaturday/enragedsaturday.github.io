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

## GROUP: _overhaul2/lake/cases/United States v. Lewis.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: United States v. Lewis
type: case
citation: "No. 22-5593, slip op. (6th Cir. 2023)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 6th Cir."
court_level: coa
circuit: ca6
year: 2023
date_decided: 2023-09-01
docket: 22-5593
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
  opinion_url: "https://www.courtlistener.com/opinion/9424185/united-states-v-edward-leonidas-lewis/"
  cluster_id: 9424185
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Lewis
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Consent Searches]]"
    role: Key
related:
  - "[[Consent Searches]]"
  - "[[United States v. Leon]]"
  - "[[Riley v. California]]"
tags:
  - case
  - fourth-amendment
  - consent-search
  - scope-of-consent
  - electronic-devices
  - bare-bones-affidavit
  - good-faith-exception
  - sixth-circuit
holding: "A homeowner's consent to an on-site 'preview' of his laptop and cell phone authorized only that limited search; the later seizure and full forensic examination of the devices required a warrant, and because the supporting affidavit was a bare-bones, conclusory statement that recited only that a consented search had 'become apparent' incriminating — without any facts a magistrate could independently weigh — it failed to establish probable cause, and the good-faith exception could not save so deficient a warrant."
aliases:
  - United States v. Lewis
  - "United States v. Lewis (6th Cir. 2023)"
  - United States v. Edward Leonidas Lewis
---

# United States v. Lewis

*No. 22-5593, slip op. (6th Cir. 2023)* · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9424185 → published opinion 9829122 (Moore, J.; Nos. 22-5593/5800, RECOMMENDED FOR PUBLICATION 23a0206p.06, decided Sept. 1, 2023). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published opinion; no F.4th reporter page locatable from any independent source — S2 A3, S9 verifies). -->

## Background
Acting on a foreign-agency tip, Kentucky State Police Detective Gatson and federal agents went to Edward Lewis's home; Lewis let them in and signed a form consenting to a complete search of the premises and his named laptop and cell phone. A forensic examiner "previewed" the devices on-site, surfacing file names indicative of child pornography and thumbnail images. Officers stopped, arrested Lewis, and seized the devices; a Commonwealth prosecutor advised obtaining a warrant, and a later forensic examination under that warrant produced the charged evidence. The district court found the warrant lacked probable cause but denied suppression under the [[The Good-Faith Exception|good-faith exception]]; Lewis pleaded guilty reserving his appeal.

## Issue
Whether the warrant authorizing the full forensic search of Lewis's seized devices was supported by probable cause and, if not, whether the [[The Good-Faith Exception|good-faith exception]] nonetheless barred suppression.

## Rule
Probable cause is judged within the "four corners of the affidavit," which must state facts showing a fair probability that evidence will be found — not a mere conclusion — and on so bare-bones an affidavit the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] is unavailable. The court held Detective Gatson's affidavit fell short: "That conclusory statement was too vague and insubstantial to establish probable cause to search Lewis's electronic devices. ... The search warrant that was issued based on Detective Gatson's affidavit therefore violated the Fourth Amendment's probable-cause requirement." — slip op. at 7. ^pin-slip7

## Application
Lewis's consent authorized only the initial on-scene preview; the officers' subsequent seizure and full forensic examination of the devices required a warrant. But the affidavit supplied only Gatson's say-so — that during a consented search "it became apparent" Lewis had viewed illegal images — with no description of the evidence or investigative steps a magistrate could evaluate. Like the affidavits condemned in *Nathanson* and *[[Aguilar v. Texas|Aguilar]]*, it was "wholly inadequate," so "[n]o reasonable officer" could have relied on it in good faith. The [[The Good-Faith Exception|good-faith exception]] did not apply.

## Conclusion
**Reversed, [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]].** The Sixth Circuit reversed the denial of suppression, [[Reading and Citing Cases#vacated|vacated]] Lewis's conviction, and [[Reading and Citing Cases#on-remand|remanded]] for further proceedings. Judge Moore wrote for the panel (Moore, Clay, Gibbons, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lewis* teaches two connected limits: consent to a narrow on-site device "preview" does not authorize a later full forensic search — for which the heightened privacy interest in digital data (*[[Riley v. California|Riley]]*) demands a warrant — and a bare-bones affidavit forfeits *[[United States v. Leon|Leon]]* good faith. Published Sixth Circuit opinion (23a0206p.06); rendered slip-style here because no Federal [[Reading and Citing Cases#reporter|Reporter]] page could be independently confirmed.

## Appears on
- [[Consent Searches]] — *Key*

## Sources
- [*United States v. Edward Leonidas Lewis*, No. 22-5593, slip op. (6th Cir. 2023)](https://www.courtlistener.com/opinion/9424185/united-states-v-edward-leonidas-lewis/) — pinpoint: slip op. at 7 (bare-bones affidavit fails probable cause; good faith unavailable). Rule quote string-matched to the CL opinion text 2026-07-07. Published as 6th Cir. op. 23a0206p.06; the CL cluster carries no citations[] and no F.4th page was independently locatable (S2 A3 slip render).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2830866229828303", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Lewis"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Lewis", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lewis",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Edward Leonidas Lewis",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Lewis",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2023-09-01",
    "year": 2023,
    "docket": "22-5593",
    "cluster_id": 9424185,
    "lead_opinion_id": 9829122,
    "sibling_ids": [],
    "absolute_url": "/opinion/9424185/united-states-v-edward-leonidas-lewis/",
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
      "court_class": "coa",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 slip disposition (previously R3-escalated; pre-W5 re-key landed correct identity United States v. Edward Leonidas Lewis, 6th Cir. No. 22-5593, decided 2023-09-01, consent-scope reversal). CL cluster 9424185 Published but citations[] empty (live-verified 2026-07-07). Published as 6th Cir. op. 23a0206p; no F.4th reporter page locatable from any independent source (Justia/FindLaw/vLex index by docket only) \u2014 no-fabrication slip render pending reporter pagination.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.opn.ca6.uscourts.gov/opinions.pdf/23a0206p-06.pdf",
          "cite": "6th Cir. op. 23a0206p, No. 22-5593, RECOMMENDED FOR PUBLICATION, 2023-09-01"
        },
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/federal/appellate-courts/ca6/22-5593/22-5593-2023-09-01.html",
          "cite": "No. 22-5593 (6th Cir. 2023), no F.4th cite listed"
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
    "date_created": "2026-07-07T13:49:58Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:50:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lewis--9424185",
      "to_record_id": "United States v. Lewis",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lewis

```
                                 RECOMMENDED FOR PUBLICATION
                                 Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                        File Name: 23a0206p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



                                                              ┐
 UNITED STATES OF AMERICA,
                                                              │
                                     Plaintiff-Appellee,      │
                                                               >        Nos. 22-5593/5800
                                                              │
        v.                                                    │
                                                              │
 EDWARD LEONIDAS LEWIS,                                       │
                                  Defendant-Appellant.        │
                                                              ┘

 Appeal from the United States District Court for the Eastern District of Kentucky at Frankfort.
               No. 3:21-cr-00021—Gregory F. Van Tatenhove, District Judge.

                             Decided and Filed: September 1, 2023

                   Before: MOORE, CLAY, and GIBBONS, Circuit Judges.

                                       _________________

                                             COUNSEL

ON BRIEF: David J. Guarnieri, MCBRAYER PLLC, Lexington, Kentucky, for Appellant.
Lauren Tanner Bradley, Charles P. Wisdom, Jr., UNITED STATES ATTORNEY’S OFFICE,
Lexington, Kentucky, for Appellee.
                                       _________________

                                              OPINION
                                       _________________

       KAREN NELSON MOORE, Circuit Judge. Kentucky State Police officers searched
Edward Lewis’s laptop, cell phone, and thumb drive and found evidence of child pornography.
Lewis moved to suppress the evidence, arguing that it was obtained through an unlawful search
and seizure of his electronic devices. The district court found that the good-faith exception to the
exclusionary rule applied and denied Lewis’s motion, and Lewis pleaded guilty while reserving
 Nos. 22-5593/5800                    United States v. Lewis                               Page 2


his right to bring this appeal. We REVERSE the district court’s order denying Lewis’s motion
to suppress, VACATE Lewis’s conviction, and REMAND for further proceedings.

                                      I. BACKGROUND

       In 2019, federal Homeland Security agents received a tip from a foreign law-enforcement
agency that an internet-protocol address later connected to Lewis was “viewing child sexual
exploitation online[.]” R. 35 (Hr’g Tr. at 11, 78–79) (Page ID #207, 274–75). The agents
notified the Kentucky State Police, who opened an investigation. Id. at 10–12 (Page ID #206–
08).

       Two years later, in February 2021, Detective Anthony Gatson of the Kentucky State
Police and Homeland Security Special Agents Brian Minnick and Brandon Even traveled to
Lewis’s home as part of their ongoing investigation. Id. at 13, 56–57 (Page ID #209, 252–53).
Detective Gatson knocked on Lewis’s door, which Lewis answered. Id. at 13 (Page ID #209).
Detective Gatson identified himself and the Homeland Security agents to Lewis, and “asked if
[they] could speak to [Lewis] about a federal complaint of some alleged crimes over the internet
from the federal government.” Id. Lewis invited Detective Gatson and the agents inside. Id.

       Inside Lewis’s home, Detective Gatson explained that he had “been told there was child
sexual exploitation activity at the house.” Id. Detective Gatson asked Lewis “if he would mind
if someone came over and looked at . . . his devices.” Id. Lewis responded that he had no
objection, id., and agreed to sign a consent form stating that he “consent[ed] to a complete search
of the premises, property or vehicle located” at his residence “and more particularly described as
Samsung Galaxy Note 9 [and] HP Pavilion Laptop[,]” R. 26-2 (Consent Form at 1) (Page ID
#141). Detective Gatson then called for a forensic examiner to come to Lewis’s home and
“preview the items” described in the signed consent form. R. 35 (Hr’g Tr. at 13–14) (Page ID
#209–10).

       Approximately twenty minutes later, Jason Rollins, a forensic examiner with the
Kentucky State Police, arrived at Lewis’s home. Id. at 20 (Page ID #216). Rollins generated a
preview of Lewis’s laptop, which revealed several file names indicative of child pornography,
including “2yo_boy,” “Tara,” and “pedomom.” Id. at 21–22 (Page ID #217–18). Rollins also
 Nos. 22-5593/5800                    United States v. Lewis                               Page 3


reviewed Lewis’s cell phone, where he found thumbnail images, which were determined on an
unspecified later date to be taken from videos of Lewis’s cousin’s children bathing naked in a
bathroom. Id. at 23–24 (Page ID #219–20). As Rollins was searching Lewis’s laptop and cell
phone, Lewis reportedly stated that he knew it was illegal to save child pornography but that he
did not know that it was illegal merely to look at it. Id. at 39 (Page ID #235). Rollins shared the
results of his initial searches with Detective Gatson, but neither Rollins nor Detective Gatson
opened any of the files or thumbnail images on Lewis’s laptop or cell phone. Id. at 23 (Page ID
#219).

         Detective Gatson called a Commonwealth prosecutor to ask for advice. Id. at 25 (Page
ID #221). The prosecutor told Detective Gatson to arrest Lewis and obtain a search warrant for
his residence. Id. Following that advice, Detective Gatson asked Lewis to step outside and read
him his Miranda rights. Id. at 26 (Page ID #222); see also Miranda v. Arizona, 384 U.S. 436
(1966). Lewis invoked his rights, but he did not say that he was revoking his consent to the
search of his electronic devices or his home. R. 35 (Hr’g Tr. at 28) (Page ID #224). Another
Kentucky State Police officer then arrived and drove Lewis to jail. Id. at 18, 52 (Page ID #214,
248).

         After Lewis was arrested, Detective Gatson returned to his office while Special Agents
Minnick and Even “sat on the front porch to secure the house[.]” Id. at 29 (Page ID #225).
Detective Gatson prepared a search warrant for Lewis’s house and any electronic devices stored
inside the home that could contain evidence of child pornography, including the laptop and cell
phone that Detective Gatson and Rollins had reviewed at Lewis’s home. Id. Detective Gatson
did not share the proposed search warrant or his affidavit in support of the warrant with a
prosecutor, but instead took the documents directly to a Franklin County judge. Id. at 57 (Page
ID #253). Detective Gatson did not provide the state judge with any additional information
beyond what he included in the proposed search warrant and his affidavit. Id. at 29 (Page ID
#225). The state judge signed the search warrant. Id.; R. 24-3 (Search Warrant at 6) (Page ID
#107).
 Nos. 22-5593/5800                   United States v. Lewis                               Page 4


       Law-enforcement officers subsequently executed the search warrant, searching Lewis’s
home and seizing his laptop, cell phone, and other electronic devices. R. 35 (Hr’g Tr. at 31)
(Page ID #227). The officers took the devices to a state laboratory, where the devices were
forensically searched. Id. The forensic search revealed evidence of child pornography on
Lewis’s laptop, cell phone, and USB thumb drive. Id.; R. 24-3 (Search Warrant Return at 1)
(Page ID #111).

       Lewis was indicted in October 2021 and charged with seven counts of producing,
receiving, and possessing child pornography, in violation of 18 U.S.C. §§ 2251(a) and
(e), 2252(a)(2), and 2251(a)(4)(B). R. 1 (Indictment at 1–4) (Page ID #1–4). Lewis pleaded not
guilty and later moved under the Fourth Amendment to suppress the evidence obtained from his
laptop, cell phone, and thumb drive as the fruits of an unlawful search and seizure. R. 11
(Minute Entry at 1) (Page ID #28); R. 24 (Mot. to Suppress at 1) (Page ID #82). He argued that
the search warrant authorizing the search and seizure of his electronic devices was not supported
by probable cause and, among other things, that the affidavit Detective Gatson submitted in
support of the search warrant was a bare-bones affidavit. R. 24-1 (Mem. at 3–4) (Page ID #86–
87).

       A magistrate judge held a hearing on Lewis’s motion to suppress and later issued a report
and recommendation to the district court recommending that Lewis’s motion be denied. United
States v. Lewis, No. 3:21-CR-00021-GFVT-EBA, 2022 WL 1284061, at *1 (E.D. Ky. Jan. 11,
2022) (Lewis I), report and recommendation rejected, 591 F. Supp. 3d 177 (E.D. Ky. 2022)
(Lewis II). The magistrate judge declined to address Lewis’s challenges to the search warrant.
Lewis I, 2022 WL 1284061, at *7. The magistrate judge instead found that Lewis had knowingly
and voluntarily consented to the search of his electronic devices, that Lewis’s consent authorized
not only the initial preview of his devices but also the subsequent seizure and forensic
examination of the devices, and that Lewis had not withdrawn his consent at any time. Id. at *4–
6. Lewis objected to the report and recommendation. R. 36 (Objs. to R&R at 1–19) (Page ID
#284–302).

       The district court declined to adopt the report and recommendation but agreed that
Lewis’s motion should be denied on other grounds. Lewis II, 591 F. Supp. 3d at 181. The
 Nos. 22-5593/5800                     United States v. Lewis                               Page 5


district court disagreed with the magistrate judge’s analysis of the scope of Lewis’s consent,
finding that Lewis had consented to the preview of his electronic devices but not to the
subsequent seizure or search of those devices. Id. at 185. The district court further agreed with
Lewis that the search warrant failed to establish probable cause to believe that his electronic
devices contained evidence of a crime. Id. at 186–87. But the district court ultimately found that
suppression was inappropriate because law-enforcement officers had relied on the search warrant
in good faith. Id. at 187–88. The district court therefore denied Lewis’s motion to suppress. Id.
at 190–91.

         Following the denial of his motion to suppress, Lewis signed a conditional plea
agreement pursuant to which he pleaded guilty to one count of producing child pornography, in
violation of 18 U.S.C. § 2251(a), but retained his right to appeal the district court’s suppression
order and to withdraw his plea if he prevailed on that appeal. R. 46 (Plea Agreement at 1–2)
(Page ID #359–60). The district court sentenced Lewis to 300 months’ imprisonment and a life
term of supervised release. R. 57 (Am. Judgment at 2–3) (Page ID #409–10). Lewis filed this
timely appeal.

                                          II. ANALYSIS

         Lewis appeals the denial of his motion to suppress, challenging the district court’s finding
that the good-faith exception to the exclusionary rule precludes suppression of evidence
recovered from his electronic devices. We review the district court’s conclusions of law de novo
and its factual findings for clear error. United States v. Master, 614 F.3d 236, 238 (6th Cir.
2010).

A. The Search Warrant

         The district court found that the search warrant was not supported by probable cause but
that the good-faith exception applied. Lewis II, 591 F. Supp. 3d at 187. We accord “great
deference” to the state magistrate’s probable-cause determination, but we give no particular
weight to the district court’s review of that determination. United States v. Lapsins, 570 F.3d
758, 763 (6th Cir. 2009) (quotation omitted) (quoting United States v. Terry, 522 F.3d 645, 647
 Nos. 22-5593/5800                   United States v. Lewis                               Page 6


(6th Cir. 2008)). The district court’s finding that the “good faith exception applies is a legal
conclusion that we review de novo.” United States v. Frazier, 423 F.3d 526, 533 (6th Cir. 2005).

       1. Probable Cause

       The Fourth Amendment provides that a search warrant may issue only “upon probable
cause, supported by Oath or affirmation[.]” U.S. Const. amend IV. When determining whether
a search warrant was supported by probable cause, we limit our review to the “four corners of the
affidavit.” United States v. Brooks, 594 F.3d 488, 492 (6th Cir. 2010). To establish probable
cause for a search warrant, “an affidavit must contain facts that indicate a fair probability that
evidence of a crime will be located on the premises of the proposed search.” United States v.
Abboud, 438 F.3d 554, 572 (6th Cir. 2006) (quoting Frazier, 423 F.3d at 531).

       Here, the state-court judge issued a search warrant based on Detective Gatson’s affidavit.
In the government’s words, Detective Gatson’s affidavit “detailed his considerable experience
investigating child sexual exploitation crimes and included boilerplate language concerning such
investigations.” Appellee Br. at 4–5. The affidavit then “set forth only the facts that” Detective
Gatson “believe[d] [were] necessary to establish probable cause to believe that evidence, fruits
and instrumentalities of violations of” Kentucky’s child sexual-exploitation laws were “present
at” Lewis’s home. R. 24-3 (Gatson Aff. at 4) (Page ID #105). Those facts were:

       An HSI investigation identified Edward L Lewis . . . as a person of interest. HSI
       SA Minnick requested assistance with interviewing Mr. Lewis. Mr. Lewis was
       located at his residence at [address.] Mr. Lewis gave consent to search his laptop
       and cell phone. During [the] search it became apparent that Mr. Lewis had used
       his laptop to view images of child sexual exploitation. The search based on
       consent was stopped and Mr. Lewis was arrested.
       Based on the affiant’s knowledge, experience and training, Edward L Lewis has
       demonstrated a pattern of criminal activity related to child pornography, and there
       is a reasonable likelihood that the user treats child pornography as a valuable
       commodity to be retained and collected, a characteristic common to many people
       interested in child pornography. It is, therefore, likely that evidence of the
       contraband remains in the user’s possession[.]

Id.
 Nos. 22-5593/5800                    United States v. Lewis                                   Page 7


       The government does not dispute that Detective Gatson’s affidavit failed to establish
probable cause. “Detective Gatson provided the state judge only one fact in support of the
existence of probable cause: that a search of Mr. Lewis’s laptop and cell phone had occurred.”
Lewis II, 591 F. Supp. 3d at 186. Absent additional information, such as a description of the
evidence uncovered during that search, Detective Gatson’s affidavit merely stated his belief that
Lewis had viewed child pornography.           That conclusory statement was too vague and
insubstantial to establish probable cause to search Lewis’s electronic devices. See United States
v. Carpenter, 360 F.3d 591, 595 (6th Cir. 2004) (en banc). The search warrant that was issued
based on Detective Gatson’s affidavit therefore violated the Fourth Amendment’s probable-cause
requirement.

       2. Good Faith

       Generally, evidence obtained in violation of the Fourth Amendment must be excluded.
See United States v. Rice, 478 F.3d 704, 711 (6th Cir. 2007). In United States v. Leon, however,
the Supreme Court recognized a good-faith exception to the exclusionary rule that applies when
“reliable physical evidence [is] seized by officers reasonably relying on a warrant issued by a
detached and neutral magistrate[.]” 468 U.S. 897, 913 (1984). The good-faith exception, the
Court explained, is premised on the conclusion “that the marginal or nonexistent benefits
produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently
invalidated search warrant cannot justify the substantial costs of exclusion.” Id. at 922.

       Leon declined to go so far as to hold “that exclusion is always inappropriate in cases
where an officer has obtained a warrant and abided by its terms.”           Id. Rather, the Court
recognized that exclusion’s benefits outweigh its costs—and “[s]uppression therefore remains an
appropriate remedy”—when a law-enforcement officer lacks “reasonable grounds for believing
that the warrant was properly issued.” Id. at 922–23. A law-enforcement officer lacks such
reasonable grounds, and the good-faith exception is inapposite, in at least four situations:

       (1) where the issuing magistrate was misled by information in an affidavit that the
       affiant knew was false or would have known was false except for his reckless
       disregard for the truth; (2) where the issuing magistrate wholly abandoned his
       judicial role and failed to act in a neutral and detached fashion, serving merely as
       a rubber stamp for the police; (3) where the affidavit was nothing more than a
 Nos. 22-5593/5800                          United States v. Lewis                                          Page 8


        “bare bones” affidavit that did not provide the magistrate with a substantial basis
        for determining the existence of probable cause, or where the affidavit was so
        lacking in indicia of probable cause as to render official belief in its existence
        entirely unreasonable; and (4) where the officer’s reliance on the warrant was not
        in good faith or objectively reasonable, such as where the warrant is facially
        deficient.

Rice, 478 F.3d at 712 (quoting United States v. Hython, 443 F.3d 480, 484 (6th Cir. 2006)).

        In this case, the issue is whether law-enforcement officers reasonably relied on the search
warrant. Lewis argues that the application of the good-faith exception is inapposite because
Detective Gatson’s affidavit was a “bare bones” affidavit.1                     “Suppression . . . remains an
appropriate remedy” when “a warrant [is] based on an affidavit so lacking in indicia of probable
cause as to render official belief in its existence entirely unreasonable.” Leon, 468 U.S. at 923
(internal quotations omitted). “Affidavits that are ‘so lacking in indicia of probable cause’ have
come to be known as ‘bare bones’ affidavits.” United States v. Laughton, 409 F.3d 744, 748 (6th
Cir. 2005). A bare-bones affidavit is an affidavit “that states suspicions, beliefs, or conclusions,
without providing some underlying factual circumstances regarding veracity, reliability, and
basis of knowledge[.]” United States v. Weaver, 99 F.3d 1372, 1378 (6th Cir. 1996). Put
differently, a bare-bones affidavit is “a conclusory affidavit” that “states only the affiant’s belief
that probable cause existed.” United States v. Williams, 224 F.3d 530, 533 (6th Cir. 2000)
(quotation omitted).

        We agree with Lewis that the law-enforcement officers did not reasonably rely on
Detective Gatson’s affidavit because the affidavit was a bare-bones affidavit.                            Although
Detective Gatson’s affidavit fell well short of establishing probable cause, “[a]n affidavit cannot
be labeled ‘bare bones’ simply because it lacks the requisite facts and inferences to sustain the
magistrate’s probable-cause finding[.]” United States v. White, 874 F.3d 490, 497 (6th Cir.
2017). Rather, the affidavit “must be so lacking in indicia of probable cause that, despite a
judicial officer having issued a warrant, no reasonable officer would rely on it.” Id. Considering
the complete lack of factual information included in Detective Gatson’s affidavit, we hold that

        1Lewis also argues that the other three situations in which the good-faith exception is inapposite are present
here. Because we agree that Detective Gatson’s affidavit was a bare-bones affidavit, we decline to reach Lewis’s
other arguments.
 Nos. 22-5593/5800                    United States v. Lewis                               Page 9


no reasonable officer would rely on the affidavit to establish probable cause to believe that
Lewis’s electronic devices would contain evidence of a child sexual-exploitation offense or any
other crime.

       As discussed above, the non-boilerplate portion of Detective Gatson’s affidavit begins by
stating that “[a]n HSI investigation identified Edward L Lewis . . . as a person of interest.”
R. 24-3 (Gatson Aff. at 4) (Page ID #105). The affidavit does not explain what “HSI” stands for,
why HSI considered Lewis to be a person of interest, or the significance of HSI’s person-of-
interest designation. Reading that initial portion of Detective Gatson’s affidavit, a judge would
have no factual basis upon which to conclude that Lewis may have committed any crime, let
alone the specific crime of child sexual exploitation as defined by Kentucky law.

       Next, the affidavit states that Lewis “consent[ed] to [a] search [of] his laptop and cell
phone” and that “[d]uring [the] search it became apparent that Mr. Lewis had used his laptop to
view images of child sexual exploitation.” Id. This section clearly expresses Detective Gatson’s
belief that Lewis had committed a crime, but it does not provide a factual basis upon which a
magistrate could independently reach that conclusion. Indeed, Detective Gatson’s conclusion
that “it became apparent that” Lewis had “view[ed] images of child sexual exploitation” was “a
mere conclusory statement that [gave] the magistrate virtually no basis at all for making a
judgment regarding probable cause.” Illinois v. Gates, 462 U.S. 213, 239 (1983). A magistrate
could conclude that there was probable cause to search Lewis’s electronic devices only by
substituting Detective Gatson’s evaluation of the evidence for the magistrate’s own evaluation.

       Lastly, the affidavit states that “[b]ased on [Detective Gatson’s] knowledge, experience
and training, Edward L Lewis has demonstrated a pattern of criminal activity related to child
pornography, and there is a reasonable likelihood that the user treats child pornography as a
valuable commodity to be retained and collected, a characteristic common to many people
interested in child pornography.” R. 24-3 (Gatson Aff. at 4) (Page ID #105). This final
statement likewise fails to set forth any factual information. It is tantamount to a statement that
“probable cause existed”—the very definition of a conclusory statement. Williams, 224 F.3d at
533.
 Nos. 22-5593/5800                      United States v. Lewis                             Page 10


          Taking a step back and considering Detective Gatson’s affidavit under the totality of the
circumstances, “the combined boilerplate language and minimal . . . information provide few, if
any, particularized facts of an incriminating nature and little more than conclusory statements of
affiant’s belief that probable cause existed regarding criminal activity.” Weaver, 99 F.3d at
1379. By omitting the essential facts of his investigation and communicating only his bottom-
line conclusion, Detective Gatson asked the magistrate to find probable cause based solely on his
say-so.     “No reasonable officer could have believed” under those circumstances “that the
affidavit was not so lacking in indicia of probable cause as to be reliable.” Laughton, 409 F.3d at
751.

          Our conclusion is consistent with United States v. White. 874 F.3d 490. White addressed
a search-warrant affidavit stating that an investigator had received information that White was
selling marijuana from a residence and that the investigator had used a confidential source to
purchase marijuana directly from White in the driveway outside that same residence. Id. at 494.
Rejecting White’s argument that the affidavit was a bare-bones affidavit, we contrasted the
affidavit with those held to be insufficiently detailed in Nathanson v. United States, 290 U.S. 41
(1933), and Aguilar v. Texas, 378 U.S. 108 (1964). White, 874 F.3d at 498–99.

          “In Nathanson, the affiant stated under oath that ‘he has cause to suspect and does believe
that’ liquor illegally brought into the United States ‘is now deposited and contained within the
premises’ belonging to the defendant.” Id. at 498 (quoting Nathanson, 290 U.S. at 44). And
“[i]n Aguilar, the affiants stated that they ‘received reliable information from a credible person
and do believe that heroin, marijuana, barbiturates and other narcotics and narcotic paraphernalia
are being kept at the above described premises for the purpose of sale and use contrary to the
provisions of the law.’” Id. (quoting Aguilar, 378 U.S. at 109). White explained that “[t]hese
affidavits were wholly inadequate—what we would call ‘bare bones’ nowadays—because they
presented ‘a mere affirmation of suspicion and belief without any statement of adequate
supporting facts.’” Id. (quoting Nathanson, 290 U.S. at 46; Aguilar, 378 U.S. at 113–14). By
contrast, the investigator in White “showed his work, explaining that White engaged in a
recorded drug deal on the premises, that White had a history of drug offenses, and that White had
dogs inside the residence.” Id. at 499.
 Nos. 22-5593/5800                     United States v. Lewis                               Page 11


       The affidavit here much more closely resembles the bare-bones affidavits in Nathanson
and Aguilar than the affidavit in White. The White investigator “showed his work[.]” Id. He
stated in his affidavit that he had “received information that marijuana was being sold . . . by . . .
White” at a particular address and that the investigator “initiated a controlled purchase of
marijuana with the use of a confidential source” from White outside that same residence. Id. at
494. This information would allow a magistrate to make an independent finding that White had
sold marijuana, and to infer that it was possible that additional marijuana could be found inside
the home. Detective Gatson, by contrast, skipped over his work. He stated in his affidavit that
he searched Lewis’s laptop and cell phone and that “it became apparent that Mr. Lewis had used
his laptop to view images of child sexual exploitation.” R. 24-3 (Gatson Aff. at 4) (Page ID
#105). Nowhere did he explain the evidence that compelled him to reach that conclusion; the
investigative process that was explained in White went left unsaid here. Like the Nathanson and
Aguilar affidavits, then, Detective Gatson’s affidavit was “wholly inadequate . . . because [it]
presented ‘a mere affirmation of suspicion and belief without any statement of adequate
supporting facts.’” White, 874 F.3d at 498 (quoting Nathanson, 290 U.S. at 46; Aguilar, 378
U.S. at 113–14). No reasonable officer would rely on Detective Gatson’s affidavit to establish
probable cause to believe that Lewis’s electronic devices contained evidence of child sexual
exploitation.

       The government suggests that “reasonable inferences” can rescue Detective Gatson’s
affidavit. “[R]easonable inferences that are not sufficient to sustain probable cause in the first
place may suffice to save the ensuing search as objectively reasonable.”           Id. at 500. For
example, United States v. Paull held that the good-faith exception applied where a search
warrant for evidence of child pornography “relied on events that were at least thirteen months
[after] the last time the accused subscribed to the suspect website.” 551 F.3d 516, 522 (6th Cir.
2009) (internal quotation omitted). Paull reasoned that “[t]o the extent that one is persuaded that
there are gaps in the evidence caused by the delay between the investigation and the search, they
were filled in by [the affiant’s] experience, whose familiarity with consumers of child
pornographers gave her adequate reason to suspect that Paull continued to possess illegal
images.” Id. at 523.
 Nos. 22-5593/5800                    United States v. Lewis                             Page 12


       No comparable inference can be drawn here. The flaw in Detective Gatson’s affidavit is
not that it does not explicitly draw connections between information included in the affidavit or
explain the inferences needed to support probable cause. Rather, the inescapable flaw is that the
affidavit does not identify a sufficient factual basis for believing that Lewis’s devices contained
evidence of child pornography. Paull and White hold that a court may draw certain reasonable
inferences from the information presented in a search warrant affidavit. But neither decision
suggests that a court can “infer” facts that are entirely missing from the affidavit. Yet that is
what a magistrate would have to do to save Detective Gatson’s warrant: the magistrate would
have to “infer” that Detective Gatson possessed sufficient—yet undisclosed—evidence to
support his conclusion that it was “apparent that Mr. Lewis had used his laptop to view images of
child sexual exploitation.” R. 24-3 (Gatson Aff. at 4) (Page ID #105). If a court could simply
presume that sufficient evidence supported a law-enforcement affiant’s “suspicions, beliefs, or
conclusions,” no affidavit would ever be held to be bare bones. Weaver, 99 F.3d at 1378.

       Under these circumstances, application of the good-faith exception would be
inappropriate. The purpose of the exclusionary rule “is to deter future Fourth Amendment
violations.” Davis v. United States, 564 U.S. 229, 236–37 (2011). The good-faith exception
promotes that purpose by precluding suppression where the remedy would “[p]enaliz[e] the
officer for the magistrate’s error, rather than his own[.]” Leon, 468 U.S. at 921. Where “the
officer’s reliance on the magistrate’s probable-cause determination” is “entirely unreasonable[,]”
however, suppression promotes deterrence and the good-faith exception is inapposite Id. at 922–
23. That is the case here.

       Neither the laws nor the facts are complex. A law-enforcement officer with as much
training and experience as Detective Gatson—and indeed any reasonable law-enforcement
officer—should know that a warrant affidavit must provide enough non-conclusory information
to allow a neutral magistrate to determine whether there is probable cause. See Nathanson, 290
U.S. 41; Aguilar, 378 U.S. 108. And here, providing the magistrate with those facts would have
been straightforward: officers found incriminating evidence on Lewis’s computer and Lewis
made incriminating statements during their conversation. Yet Detective Gatson chose not to
provide that information in his affidavit. See R. 24-3 (Gatson Aff. at 4) (Page ID #105); R. 35
 Nos. 22-5593/5800                    United States v. Lewis                              Page 13


(Hr’g Tr. at 49) (Page ID #245).       As a result, law-enforcement officers searched Lewis’s
electronic devices based on an affidavit that any reasonable officer would have known lacked
sufficient information to establish probable cause. Rejecting the application of the good-faith
exception is necessary to demonstrate that Detective Gatson and the other officers had a duty to
ensure that the affidavit was free of obvious constitutional defects and to underscore the costs of
not discharging that duty.

       For all these reasons, we conclude that the good-faith exception is inapplicable here. A
search-warrant affidavit that states only the affiant’s conclusory belief that a suspect committed a
crime is a bare-bones affidavit that cannot establish probable cause to search and that precludes
application of the good-faith exception to the exclusionary rule. Because the search warrant here
was supported by only Detective Gatson’s bare-bones affidavit, the warrant did not authorize
law-enforcement officers to search or seize Lewis’s electronic devices and the fruits of those
searches must be excluded unless an exception to the Fourth Amendment’s warrant requirement
applies.

B. Exceptions to the Warrant Requirement

       Warrantless searches and seizures “are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and well-delineated exceptions.”
Mincey v. Arizona, 437 U.S. 385, 390 (1978) (quoting Katz v. United States, 389 U.S. 347, 357
(1967)). Thus, the evidence recovered from Lewis’s electronic devices must be suppressed
unless an exception to the warrant requirement permitted the search and seizure of the devices.
The government invokes two exceptions: consent and the plain-view doctrine.

       1. Consent

       The government first contends that Lewis consented to the search and seizure of his
electronic devices. Consent is an exception to the Fourth Amendment’s warrant requirement.
Schneckloth v. Bustamonte, 412 U.S. 218, 219 (1973). Lewis concedes that he consented to an
initial search of his laptop and cell phone and that Detective Gatson and forensic examiner
Rollins were entitled to perform that search without first securing a warrant. Lewis argues,
 Nos. 22-5593/5800                   United States v. Lewis                              Page 14


however, that he did not consent to the seizure or subsequent forensic examination of his
electronic devices.

       The district court found that Lewis consented to the initial search of his laptop and cell
phone performed by Rollins at Lewis’s home, but that the law-enforcement officers exceeded the
scope of Lewis’s consent when they seized his electronic devices and later forensically examined
them. Lewis II, 591 F. Supp. 3d at 183–85. “The district court’s determination of whether a
search” or seizure “exceeded the scope of consent is a question of fact that we review for clear
error.” United States v. Garrido-Santana, 360 F.3d 565, 570 (6th Cir. 2004). “A factual finding
will only be clearly erroneous when, although there may be evidence to support it, the reviewing
court on the entire evidence is left with the definite and firm conviction that a mistake has been
committed.” United States v. Henry, 429 F.3d 603, 608 (6th Cir. 2005) (quoting United States v.
Oliver, 397 F.3d 369, 374 (6th Cir. 2005)).

       “The standard for measuring the scope of a suspect’s consent under the Fourth
Amendment is that of ‘objective’ reasonableness—what would the typical reasonable person
have understood by the exchange between the officer and the suspect?” Florida v. Jimeno, 500
U.S. 248, 251 (1991). To determine what a reasonable person would have understood the scope
of their consent to be, we look to the “expressed object” of the search or seizure. Id. A
reasonable person who consents to the search of his car for narcotics, for example, would
understand that the law-enforcement officer could “search containers within that car which might
bear drugs.” Id.

       The parties agree that Lewis consented to the initial search of his laptop and cell phone at
his home. Detective Gatson specifically told Lewis that he was looking for evidence of child
pornography and asked Lewis “if he would mind if someone came over and looked at . . . his
devices” for that evidence. R. 35 (Hr’g Tr. at 13) (Page ID #209). Lewis did not object to
Detective Gatson’s request, and he then signed a consent-to-search form that authorized “a
complete search of the premises, property or vehicle located at [his address] and more
particularly described as Samsung Galaxy Note 9 [and] HP Pavilion Laptop[.]”              R. 26-2
(Consent Form at 1) (Page ID #141). Lewis was then present as Rollins searched and generated
the preview of his laptop and looked through his phone. R. 35 (Hr’g Tr. at 20–26) (Page ID
 Nos. 22-5593/5800                     United States v. Lewis                                Page 15


#216–22).      Lewis never attempted to withdraw his consent while Rollins performed these
searches or generated the preview of his laptop. Id. at 28 (Page ID #224). A reasonable person
would have understood these events to authorize Detective Gatson and Rollins to search Lewis’s
laptop and cell phone for evidence of child pornography and to generate the preview of Lewis’s
laptop.

          The government argues that Lewis also consented to the seizure and forensic examination
of his electronic devices. The district court rejected the government’s argument, finding that
nothing in Lewis’s exchange with Detective Gatson or the other law-enforcement officers would
suggest to a reasonable person that Lewis had consented to anything more than the initial search
of his devices. The district court’s findings are consistent with Lewis’s exchange with the law-
enforcement officers and those officers’ actions, and therefore are not clearly erroneous.

          At the suppression hearing, Detective Gatson, Special Agent Minnick, and Special Agent
Even testified that Detective Gatson asked Lewis something to the effect of whether he
“mind[ed] if [they] look[ed]” at his devices. Id. at 78 (Page ID #274); see also id. at 15 (Page ID
#211) (Detective Gatson recounting that he asked Lewis “if he would mind . . . if we could look
at his devices”); id. at 64 (Page ID #260) (Special Agent Minnick testifying that Detective
Gatson asked Lewis “for consent to search some media”). None of the law-enforcement officers
testified that Lewis was asked for his consent to seize his devices or to a perform a second, more
invasive search of the devices at a state forensic laboratory, or that he voluntarily consented to
those actions.

          Although Lewis signed a consent form that authorized “a complete search” (but not a
seizure) of his “premises, property or vehicle[,]” R. 26-2 (Consent Form at 1) (Page ID #141),
Detective Gatson said that he understood Lewis to be “giving consent for a forensic examiner to
come out and preview devices” and not “to come out and look around” more broadly, see R. 35
(Hr’g Tr. at 43) (Page ID #239). Detective Gatson’s stated understanding of the limited scope of
Lewis’s consent is consistent with the actions that he and other officers took before, during, and
after the initial search of Lewis’s laptop and cell phone. As just noted above, Detective Gatson
asked Lewis for his consent to have Rollins come to Lewis’s home and look through his laptop
and cell phone, not to engage in an exhaustive examination of all of Lewis’s devices or to
 Nos. 22-5593/5800                   United States v. Lewis                             Page 16


conduct a forensic examination of them. R. 35 (Hr’g Tr. at 43) (Page ID #239). After Rollins
searched Lewis’s laptop and cell phone, Detective Gatson told Lewis that he was placing him
under arrest, that the consent search was complete, and that he would seek a search warrant for
Lewis’s devices.     Id. at 25–28 (Page ID #221–24); see also Appellant Reply Br. at 6
(transcribing recorded conversation). Lewis was then transported to jail, and Detective Gatson
left Lewis’s home while the agents stood guard outside of it. Id. at 26–29, 51–52 (Page ID
#222–25, 247–48).

       The district court did not clearly err in finding that Detective Gatson and the other law-
enforcement officers exceeded the scope of Lewis’s consent when they seized his electronic
devices and forensically examined them. As the district court observed, searches and seizures
implicate different Fourth Amendment interests. See Horton v. California, 496 U.S. 128, 133
(1990); see also Soldal v. Cook County, 506 U.S. 56, 66 (1992). Nothing in Lewis’s exchange
with Detective Gatson or in the law-enforcement officers’ actions would suggest to a reasonable
person that Lewis had consented to the seizure of all the electronic devices in his home. The
officers did not ask for his consent to seize, and the consent form Lewis signed did not authorize
a seizure. Further, all agree that Lewis allowed Rollins to search his devices while Rollins,
Lewis, and the law-enforcement officers were present in Lewis’s home.             But the events
recounted above demonstrate that Detective Gatson and the other officers reached the limit of
Lewis’s consent once they terminated the consent search, arrested Lewis, and left his home to
obtain a search warrant. Thus, Lewis’s consent did not authorize the seizure and forensic
examination of his devices.

       2. Plain View

       The government invokes one other exception to the Fourth Amendment’s warrant
requirement: the plain-view doctrine. “Under [the plain-view] doctrine, if police are lawfully in
a position from which they view an object, if its incriminating character is immediately apparent,
and if the officers have a lawful right of access to the object, they may seize it without a
warrant.” Minnesota v. Dickerson, 508 U.S. 366, 375 (1993). The government argues that
Detective Gatson and Rollins were entitled to seize Lewis’s electronic devices and later
 Nos. 22-5593/5800                    United States v. Lewis                             Page 17


forensically search them after they saw incriminating file names on the laptop during the initial
consent search.

       The government’s plain-view argument falls flat. To start, the argument is forfeited. The
government did not invoke the plain-view doctrine in the district court proceedings below. See
generally R. 26-1 (Gov’t Suppression Mem.) (Page ID #131–40); R. 35 (Suppression Hr’g Tr.)
(Page ID #197–281). It was not until the government filed its brief with this court that it cited
the doctrine for the first time.   We have made clear under similar circumstances that the
government is subject to the same forfeiture rules as any other litigant. See United States v.
Russell, 26 F.4th 371, 376 (6th Cir. 2022); United States v. Noble, 762 F.3d 509, 526–28 (6th
Cir. 2014). Given its forfeiture, “the government must show that the forfeited error was clear
and affected its substantial rights.” Russell, 26 F.4th at 376. The government cannot do so here.

       The plain-view doctrine permits certain warrantless seizures, not searches. See Hopkins
v. Nichols, 37 F.4th 1110, 1118 (6th Cir. 2022). Here, the government did not uncover the
evidence Lewis seeks to suppress until after it seized his devices and then forensically examined
them at the state laboratory. See R. 35 (Hr’g Tr. at 23, 31, 47–48) (Page ID #219, 227, 243–44).
During the suppression hearing, Detective Gatson confirmed that the evidence that formed the
basis of the charges brought against Lewis were the files recovered after the electronic devices
were seized and forensically examined at the state laboratory, and not the results of the preview
search conducted at Lewis’s home. Id. Thus, even if we agreed with the government that the
plain-view doctrine permitted the law-enforcement officers to seize Lewis’s laptop and cell
phone, cf. United States v. Herndon, 501 F.3d 683, 686, 692–94 (6th Cir. 2007) (plain-view
doctrine permitted warrantless seizure of laptop and hard drives that were later searched in
greater detail pursuant to a search warrant), the officers still would need some other Fourth
Amendment justification to conduct the complete forensic examination of the devices. See
Horton, 496 U.S. at 141 & n.11 (noting that “the seizure of an object in plain view does not
involve an intrusion on privacy” and that when the “item is a container . . . it may only be opened
pursuant to either a search warrant . . . or one of the well-delineated exceptions to the warrant
requirement.”). The plain-view doctrine cannot provide that justification, and therefore the
government has not shown plain error.
 Nos. 22-5593/5800                  United States v. Lewis                             Page 18


                                     III. CONCLUSION

       Lewis consented to the initial search of his laptop and cell phone performed at his home,
and the law-enforcement officers’ account of that search and the preview generated during the
search were validly obtained and are admissible under the Fourth Amendment.           All other
evidence taken from Lewis’s electronic devices, by contrast, was obtained through searches and
seizures that were not supported by a valid warrant or a valid claim to an exception to the
warrant requirement. Accordingly, we REVERSE the district court’s order denying Lewis’s
motion to suppress, VACATE Lewis’s conviction, and REMAND for further proceedings.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Liddell.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Liddell
type: case
citation: "517 F.3d 1007 (2008)"
parallel_cite: ""
neutral_cite: "2008 U.S. App. LEXIS 4012; 2008 WL 482410"
court: 8th Cir.
court_level: coa
circuit: ca8
year: 2008
date_decided: ""
docket: 07-1337
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
  opinion_url: "https://www.courtlistener.com/opinion/1461978/united-states-v-liddell/"
  cluster_id: 1461978
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Liddell
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: Key
related:
  - "[[Miranda and Custodial Interrogation]]"
  - "[[New York v. Quarles]]"
  - "[[Miranda v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - custodial-interrogation
  - public-safety-exception
  - quarles
  - eighth-circuit
holding: "The Eighth Circuit held that an un-Mirandized, in-custody question to a secured arrestee — 'Is there anything else in there we need to know about?' after officers found a concealed revolver in his car — fell within New York v. Quarles's public-safety exception to Miranda, because the risk that officers might mishandle other unknown weapons while searching a vehicle incident to a late-night arrest is an objectively reasonable public-safety concern; the incriminating statement was admissible and the felon-in-possession conviction affirmed."
---

# United States v. Liddell

*517 F.3d 1007 (8th Cir. 2008)* (No. 07-1337) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 1461978 → majority opinion 1461978 (517 F.3d 1007, decided 2008-02-25, Loken, C.J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
At about 12:45 a.m., Officer Adney stopped Antonio Liddell's car for a loud-music violation and arrested him after learning he was barred from driving in Iowa. A pat-down turned up marijuana, cash, and two cell phones, and Adney handcuffed Liddell in the patrol car. Officer Melvin, searching the car incident to the arrest, found an unloaded .38 revolver under the front seat and asked whether Liddell had been thoroughly searched. Adney then removed Liddell and asked whether there was anything else in the car they needed to know about; Melvin added, "That's gonna hurt us?" Liddell laughed and answered that he knew it was there but it was not his, before saying there were no other weapons. Charged as a felon in possession, Liddell entered a conditional guilty plea after the district court denied suppression of that statement. The government conceded he was in custody and had not received *[[Miranda v. Arizona|Miranda]]* warnings.

## Issue
Whether Liddell's un-Mirandized, in-custody statement was admissible under the public-safety exception to *[[Miranda v. Arizona|Miranda]]* recognized in *[[New York v. Quarles]]* — even though the revolver had already been found and Liddell was handcuffed and under the officers' control when the question was asked.

## Rule
The public-safety exception applies, under an **objective** standard that does not turn on the officers' subjective motivation, when "police officers ask questions reasonably prompted by a concern for the public safety." Applying that standard, the Eighth Circuit held that the danger posed by other, unlocated weapons during a search justifies a limited question to a secured arrestee: "Our prior cases recognized that the risk of police officers being injured by the mishandling of unknown firearms or drug paraphernalia provides a sufficient public safety basis to ask a suspect who has been arrested and secured whether there are weapons or contraband in a car or apartment that the police are about to search." — 517 F.3d at 1009–10. ^pin-1009

## Application
Liddell argued the exception could not apply because the revolver had been found, he was handcuffed and controlled by two officers, and no bystanders could have accessed the car. The court rejected that: discovering one concealed firearm gave the officers an objectively reasonable concern that other, possibly loaded weapons were in the vehicle they were about to search incident to a late-night arrest, which could cause harm to an officer who happened upon them unexpectedly or mishandled them. Because the officers had no way to know the .38 was the only weapon, the question about anything else in the car was reasonably prompted by public-safety concern rather than designed solely to elicit testimony, so Liddell's incriminating answer was admissible despite the absence of *[[Miranda v. Arizona|Miranda]]* warnings.

## Conclusion
**Affirmed.** Chief Judge Loken wrote for the court (Loken, C.J.; Gruender and Benton, JJ.). Judge Gruender concurred separately, questioning whether the circuit's public-safety cases had drifted from *[[New York v. Quarles|Quarles]]*'s tethering of the exception to genuine [[Exigent Circumstances and Hot Pursuit|exigent circumstances]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Liddell* is a workhorse Eighth Circuit application of the *[[New York v. Quarles|Quarles]]* **public-safety exception** to *[[Miranda v. Arizona|Miranda]]*: after finding one weapon, officers may ask a secured suspect about other weapons or contraband in a space they are about to search, because mishandling an unknown firearm is an objectively reasonable safety risk. Note the internal tension flagged by Judge Gruender's [[Common Legal Terms#concurring-opinion|concurrence]] — whether that application still requires the [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] *[[New York v. Quarles|Quarles]]* demanded.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key*

## Sources
- [*United States v. Liddell*, 517 F.3d 1007 (8th Cir. 2008)](https://www.courtlistener.com/opinion/1461978/united-states-v-liddell/) — pinpoint: 1009–10 (public-safety-exception applied holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "78a3c670d7157fe5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Liddell"}, "payload": {"all": [{"cite": "517 F.3d 1007", "page": "1007", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "517"}, {"cite": "2008 U.S. App. LEXIS 4012", "page": "4012", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2008"}, {"cite": "2008 WL 482410", "page": "482410", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2008"}], "display": "517 F.3d 1007", "official": {"cite": "517 F.3d 1007", "page": "1007", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "517"}, "official_selection_present": true, "record_id": "United States v. Liddell"}}
{"assertion_id": "3e65c64baea80678", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Liddell"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Liddell", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Liddell

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Liddell",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Liddell",
    "case_name_short": "Liddell",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Antonio Ray LIDDELL, Defendant-Appellant",
    "input_case_name": "United States v. Liddell",
    "court": "8th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": null,
    "year": 2008,
    "docket": "07-1337",
    "cluster_id": 1461978,
    "lead_opinion_id": 9634236,
    "sibling_ids": [],
    "absolute_url": "/opinion/1461978/united-states-v-liddell/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 F.3d 1007",
      "volume": "517",
      "reporter": "F.3d",
      "page": "1007",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. App. LEXIS 4012",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "4012",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 482410",
        "volume": "2008",
        "reporter": "WL",
        "page": "482410",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 F.3d 1007",
        "volume": "517",
        "reporter": "F.3d",
        "page": "1007",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. App. LEXIS 4012",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "4012",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 482410",
        "volume": "2008",
        "reporter": "WL",
        "page": "482410",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 F.3d 1007",
    "official_selection": {
      "court_class": "coa",
      "selected": "517 F.3d 1007",
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
    "date_created": "2026-07-07T01:39:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-liddell--1461978",
      "to_record_id": "United States v. Liddell",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Liddell

```
<opinion type="majority">
<author id="b1026-7">LOKEN, Chief Judge.</author>
<p id="b1026-8">Antonio Ray Liddell pleaded guilty to being a felon in possession of a firearm in violation of <span class="citation no-link">18 U.S.C. §§ 922</span>(g)(1) and 924(a)(2). As permitted by a condition in his plea agreement, Liddell now appeals the denial of his motion to suppress a post-arrest statement made without the warnings required by <em>Miranda v. Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966). We agree with the district court<footnotemark>1</footnotemark> that the arresting officers’ in-custody questioning fell within the public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>established in <em>New York v. Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U.S. 649</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">81 L.Ed.2d 550</a></span> (1984). Accordingly, we affirm.</p>
<p id="b1026-11">The following facts are undisputed. At approximately 12:45 a.m., Police Officer Michael Adney stopped a car driven by Liddell for a loud music violation. Adney arrested Liddell when a check revealed that he was barred from driving in Iowa. After the arrest, a pat-down search uncovered a bag of marijuana, $183 in cash, and two cell phones. Adney handcuffed Lid-dell and placed him in the patrol car. Meanwhile, Police Officer Jon Melvin arrived to assist and began to search Lid-dell’s car incident to the arrest. When Melvin discovered an unloaded .38 caliber revolver under the front seat, he showed the gun to Adney and asked whether Lid-dell’s person had been thoroughly searched after the arrest.</p>
<p id="b1026-12">Adney removed Liddell from the patrol car and asked, referring to Liddell’s ear, “Is there anything else in there we need to know about?” Melvin added, “That’s gonna hurt us?” Adney repeated, “That’s gonna hurt us? Since we found the pistol already.” Liddell laughed and said, “I knew it was there but ... it’s not mine,” before telling the officers there were no other weapons in his car. Melvin completed the search of the car, finding .38 caliber ammunition and rolling papers used to make marijuana cigarettes.</p>
<p id="b1026-13">Charged with unlawful possession of the firearm and with unrelated drug offenses, Liddell entered a conditional plea of guilty to the felon-in-possession charge after the district court denied a motion to suppress his highly incriminating statement that he knew the .38 revolver was under the front seat of his car. In the district court and on appeal, the government conceded that Liddell was in custody and had not been given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings at the time the officers asked the question <page-number citation-index="1" label="1009">*1009</page-number>that elicited this incriminating statement. Thus, the issue is whether the statement is admissible under the public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>as articulated by the Supreme Court in <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span> </em>and applied by this court in <em>United States v. Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d 945</a></span> (8th Cir.1999), and <em>United States v. Luker, </em><span class="citation" data-id="9497692"><a href="/opinion/788993/united-states-v-tony-john-luker/" aria-description="Citation for case: United States v. Tony John Luker">395 F.3d 830</a></span> (8th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./546/831/">546 U.S. 831</a></span>,<span class="citation multiple-matches"><a href="/c/S.Ct./126/52/">126 S.Ct. 52</a></span>,<span class="citation" data-id="9247905"><a href="/opinion/9253089/ramirez-v-dretke/" aria-description="Citation for case: Ramirez v. Dretke">163 L.Ed.2d 82</a></span> (2005). “Whether facts support an exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirement is a question of law” that we review <em>de novo. United States v. Lackey, 384 </em>F.3d 1224, 1226 (10th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./540/997/">540 U.S. 997</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./124/502/">124 S.Ct. 502</a></span>, <span class="citation no-link">157 L.Ed.2d 399</span> (2003); <em>accord United States v. Talley, </em><span class="citation" data-id="775984"><a href="/opinion/775984/united-states-v-curtis-talley/#561" aria-description="Citation for case: United States v. Curtis Talley">275 F.3d 560, 561</a></span> (6th Cir.2001).</p>
<p id="b1027-11">In <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span>, </em>the Supreme Court held that “there is a ‘public safety’ exception to the requirement that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be given before a suspect’s answers may be admitted into evidence.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#655" aria-description="Citation for case: New York v. Quarles">467 U.S. at 655</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>. In this context, protection of the public safety includes protection of the police officers themselves. <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Id.</a></span> </em>at 658 n. 7, 659, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>. The exception does not depend upon the subjective motivation of the questioning officers. Instead, the Court adopted an objective standard: the exception applies when “police officers ask questions reasonably prompted by a concern for the public safety.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#656" aria-description="Citation for case: New York v. Quarles"><em>Id. </em>at 656</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, quoted in <em>Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/#953" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953</a></span>. It does not apply to “questions designed solely to elicit testimonial evidence from a suspect.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#659" aria-description="Citation for case: New York v. Quarles">467 U.S. at 659</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>.<footnotemark>2</footnotemark></p>
<p id="b1027-13">Liddell argues that the public safety exception does not apply because, at the time the officers asked the question that prompted his incriminating admission, “there was no longer an objective reasonable need to protect the police or the public from any immediate danger” because the revolver had been found, Liddell was handcuffed and under the control of the two officers, and there were no passengers or nearby members of the public who could have accessed or been harmed by the contents of Liddell’s car. The district court rejected this contention, explaining:</p>
<blockquote id="Aj">The discovery of a firearm hidden in a vehicle would lead an officer to have an objectively reasonable concern that other, possibly loaded, firearms may also be in the vehicle which could cause harm to an officer if they were to happen upon them unexpectedly or mishandle them in some way. The accidental discovery of additional weapons poses a threat to officer safety and at the time the officers conducted their limited questioning of [Liddell], given the information then known to them, it was reasonable for the officers to believe this threat existed. There was no way for Officer Melvin or Officer Adney to know that the firearm found under the driver’s seat was ultimately the only weapon or dangerous device located inside of the vehicle.</blockquote>
<p id="b1027-7">The district court’s analysis is consistent with this court’s controlling precedents. Our prior cases recognized that the risk of police officers being injured by the mishandling of unknown firearms or drug par<page-number citation-index="1" label="1010">*1010</page-number>aphernalia provides a sufficient public safety basis to ask a suspect who has been arrested and secured whether there are weapons or contraband in a car or apartment that the police are about to search. <em>See Luker, </em><span class="citation" data-id="9497692"><a href="/opinion/788993/united-states-v-tony-john-luker/#832" aria-description="Citation for case: United States v. Tony John Luker">395 F.3d at 832</a></span> (public safety exception applied to post-arrest question whether there was anything in intoxicated driver’s car the police should know about); <em>Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/#953" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953-54</a></span> (public safety exception applied to post-arrest question, “is there anything we need to be aware of’ in the suspect’s apartment, because the police “could not have known whether other hazardous weapons were present ... that could cause them harm if they happened upon them unexpectedly or mishandled them in some way”). Accord <em>Lackey, </em>334 F.3d at 1227-28; <em>contra United States v. Williams, </em><span class="citation" data-id="797465"><a href="/opinion/797465/united-states-v-patrick-williams/#428" aria-description="Citation for case: United States v. Patrick Williams">483 F.3d 425, 428</a></span> (6th Cir.2007). Here, when the officers found Liddell’s concealed .38 caliber revolver, they had good reason to be concerned that additional weapons might pose a threat to their safety when they searched Liddell’s car incident to a late-night arrest.</p>
<p id="b1028-4">The judgment of the district court is affirmed.</p>
<footnote label="1">
<p id="b1026-9">. The HONORABLE JAMES E. GRITZNER, United Slates District Judge for the Southern District of Iowa.</p>
</footnote>
<footnote label="2">
<p id="b1027-2">. Because this is an objective standard, and because police officers must react spontaneously to situations posing a threat to public safety, the public safety exception does not turn on the specific form of questions asked. <em>See </em>Williams, <span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953</a></span> n. 13; <em>United States v. Newton, </em><span class="citation" data-id="786350"><a href="/opinion/786350/united-states-v-sewn-newton/" aria-description="Citation for case: United States v. Sewn Newton">369 F.3d 659</a></span>, 678-79 &amp; n. 8 (2d Cir.2004). There can be no doubt that tVu» nmactinn nncpH hv flip nffirprQ in this rncp was sufficiently focused on public safety to trigger the public safety exception. By contrast, the Court explained in <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U.S. at 659</a></span> n. 8, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, the post-arrest questioning without <em>Miranda </em>warnings in <em>Or-ozco v. Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#325" aria-description="Citation for case: Orozco v. Texas">394 U.S. 324, 325-26</a></span>, <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">89 S.Ct. 1095</a></span>, <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">22 L.Ed.2d 311</a></span> (1969), was "clearly investigatory."</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Loera.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Loera
type: case
citation: "923 F.3d 907 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2019
date_decided: 2019-05-13
docket: 17-2087
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
  opinion_url: "https://www.courtlistener.com/opinion/4619076/united-states-v-loera/"
  cluster_id: 4619076
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Loera
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[Horton v. California]]"
  - "[[Riley v. California]]"
  - "[[United States v. Ganias]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - computer-search
  - particularity
  - plain-view
  - scope-of-search
  - tenth-circuit
holding: "The Tenth Circuit held that the Fourth Amendment does not require officers executing an electronic-search warrant to stop when they discover evidence of a different, out-of-scope crime, so long as their search remains directed at uncovering the evidence the warrant specifies; agents who found child pornography while searching Loera's devices for computer-fraud evidence could continue the authorized search, and — having obtained a second, pornography-specific warrant to search for that evidence — the denial of suppression was affirmed."
---

# United States v. Loera

*923 F.3d 907 (10th Cir. 2019)* (No. 17-2087) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4619076 → opinion 4396329 (923 F.3d 907, decided 2019-05-13, Ebel, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In 2012 the FBI investigated Jason Loera for illegally intercepting e-mails meant for New Mexico Governor Susana Martinez and her staff — computer fraud under 18 U.S.C. §§ 2511 and 1030. Agents obtained a warrant to search Loera's home for evidence of that offense, including on electronic storage media. Executing it, agents previewing his CDs discovered child pornography on four discs; they continued their authorized search for computer-fraud evidence (Search 1), then seized a number of devices along with the four CDs. A week later, one agent reopened the CDs he knew contained pornography to describe several images in an affidavit for a **second** warrant to search all the seized devices for child pornography (Search 2); a magistrate issued it and the agents found more. Charged with receipt of child pornography, Loera moved to suppress the evidence from each search; the district court denied the motion, and he entered a conditional guilty plea preserving the appeal.

## Issue
Whether the Fourth Amendment required the agents to stop their authorized computer-fraud search of Loera's electronic devices once they discovered child pornography that lay outside the first warrant's scope — and whether the evidence had to be suppressed.

## Rule
When officers execute a particular warrant to search an electronic device for evidence of one crime and come across evidence of a different, ongoing crime, they need not abandon the authorized search, provided it stays trained on the warrant's specified evidence: "We hold, among other things, that the Fourth Amendment does not require police officers to stop executing an electronic search warrant when they discover evidence of an ongoing crime outside the scope of the warrant, so long as their search remains directed at uncovering evidence specified in that warrant." — 923 F.3d at 911. ^pin-911

## Application
Because the agents' continued examination of Loera's CDs and devices remained directed at uncovering the computer-fraud evidence the first warrant specified — rather than becoming a roving, exploratory hunt for the pornography they had glimpsed — they were not required to stop when they encountered the out-of-scope child pornography. To actually search the seized devices *for* that pornography, the agents did the constitutionally required thing: they obtained a **second**, pornography-specific warrant before conducting that search. On those facts the court affirmed the denial of Loera's motion to suppress the evidence seized in each search.

## Conclusion
**Affirmed** — the denial of suppression stands. Judge Ebel wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Loera* is an important digital-search-scope authority for the **plain-view / anti-exploratory-search** frontier: an officer who lawfully searches a device for one crime's evidence may keep going when other-crime evidence surfaces, so long as the search stays tethered to the warrant's targets — but to search *for* the newly discovered offense, a fresh warrant is required. Pair it with *[[United States v. Ganias|Ganias]]* on digital over-seizure and *[[Coolidge v. New Hampshire|Coolidge]]*'s bar on using plain view to run a general exploratory search from one object to another.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Loera*, 923 F.3d 907 (10th Cir. 2019)](https://www.courtlistener.com/opinion/4619076/united-states-v-loera/) — pinpoint: 911 (the electronic-search-need-not-stop holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "974fb651db4bc980", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Loera"}, "payload": {"all": [{"cite": "923 F.3d 907", "page": "907", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "923"}], "display": "923 F.3d 907", "official": {"cite": "923 F.3d 907", "page": "907", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "923"}, "official_selection_present": true, "record_id": "United States v. Loera"}}
{"assertion_id": "efe1aad3cec9e1fe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Loera"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Loera", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Loera

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Loera",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Loera",
    "case_name_short": "Loera",
    "case_name_full": "UNITED STATES of America Plaintiff - Appellee, v. Jason LOERA, Defendant - Appellant.",
    "input_case_name": "United States v. Loera",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2019-05-13",
    "year": 2019,
    "docket": "17-2087",
    "cluster_id": 4619076,
    "lead_opinion_id": 4396329,
    "sibling_ids": [],
    "absolute_url": "/opinion/4619076/united-states-v-loera/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "923 F.3d 907",
      "volume": "923",
      "reporter": "F.3d",
      "page": "907",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "923 F.3d 907",
        "volume": "923",
        "reporter": "F.3d",
        "page": "907",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "923 F.3d 907",
    "official_selection": {
      "court_class": "coa",
      "selected": "923 F.3d 907",
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
    "date_created": "2026-07-07T18:18:30Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-loera--4619076",
      "to_record_id": "United States v. Loera",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Loera

```
                                                                                FILED
                                                                    United States Court of Appeals
                                      PUBLISH                               Tenth Circuit

                       UNITED STATES COURT OF APPEALS                       May 13, 2019

                                                                        Elisabeth A. Shumaker
                            FOR THE TENTH CIRCUIT                           Clerk of Court
                        _________________________________

 UNITED STATES OF AMERICA

       Plaintiff - Appellee,

 v.                                                         No. 17-2180

 JASON LOERA,

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                            for the District of New Mexico
                           (D.C. No. 1:13-CR-01876-JB-1)
                       _________________________________

Jerry A. Walz, Walz and Associates, P.C., Albuquerque, New Mexico for Defendant-
Appellant.

Kristopher N. Houghton, Assistant United States Attorney (John C. Anderson, United
States Attorney, with him on the brief), Albuquerque, New Mexico for Plaintiff-
Appellee.
                        _________________________________

Before LUCERO, EBEL, and PHILLIPS, Circuit Judges.
                  _________________________________

EBEL, Circuit Judge.
                        _________________________________

      This appeal requires us to apply Fourth Amendment principles to a situation

where a police officer executing a warrant to search an electronic storage device for

evidence of one crime discovers evidence of other criminal activity. Here, while
executing a warrant to search Jason Loera’s home for evidence of computer fraud,

FBI agents discovered child pornography on four of Loera’s CDs. Despite

discovering the pornography, the agents continued their search for evidence of

computer fraud—one agent continued to search the CDs that were found to contain

some child pornography and a second agent searched other electronic devices

belonging to Loera, not including those particular CDs (Search 1). After the agents

finished their on-site search, they seized a number of electronic devices that appeared

to contain evidence of computer fraud, plus the four CDs that were found to contain

child pornography, and then brought the seized items back to their office. One week

later, one of the agents reopened the CDs that he knew contained some child

pornography so that he could describe a few pornographic images in an affidavit

requesting a (second) warrant to search all of the seized electronic devices for child

pornography (Search 2). A magistrate judge issued the warrant, and, upon executing

it through two searches, the agents found more child pornography.

      In the subsequent prosecution against him for possessing child pornography,

Loera filed a motion to suppress the evidence seized pursuant to each search, arguing

that the searches violated the Fourth Amendment. On denial of his motion, Loera

pled guilty to receipt of child pornography but preserved his right to appeal that

denial. Exercising jurisdiction under 28 U.S.C. § 1291, we affirm the denial of

Loera’s motion to suppress. We hold, among other things, that the Fourth

Amendment does not require police officers to stop executing an electronic search

warrant when they discover evidence of an ongoing crime outside the scope of the

                                           2
warrant, so long as their search remains directed at uncovering evidence specified in

that warrant.

                                  I.   BACKGROUND

       This case involves several police searches governed by the Fourth

Amendment. The Fourth Amendment protects “the right of the people to be secure in

their persons, houses, papers, and effects, against unreasonable searches and

seizures.” U.S. Const. amend. IV. Generally, for a search to be reasonable, it must

be authorized by a warrant that “particularly” describes “the place to be searched, and

the persons or things to be seized.” U.S. Const. amend. IV. Once officers obtain a

sufficiently particular warrant, they must execute it according to the warrant’s terms.

Horton v. California, 496 U.S. 128, 140 (1990). The following undisputed facts

explain how the warrant-based searches in this case arose.

       In 2012, the FBI began investigating Jason Loera for illegally intercepting e-

mails intended for then-sitting New Mexico Governor Susana Martinez and her staff

in violation of 18 U.S.C. § 2511 (illegal interception) and 18 U.S.C. § 1030

(computer fraud) [collectively, “computer fraud”]. As part of that investigation

(more details of which can be found in the district court’s opinion United States v.

Loera, 59 F. Supp. 3d 1089, 1095–1108 (D.N.M. 2014)), FBI agents applied for and

received a warrant to search Loera’s residence for computer fraud, including any

such evidence residing on electronic devices or storage media (“the first warrant”).

       The first warrant authorized FBI agents to search and seize, in relevant part,

“All records, in any form, relating to violations of [computer fraud], involving Jason

                                             3
Loera.” ROA Vol. I at 37. The warrant defined the terms “records” and “information”

as including: “all of the foregoing items of evidence in whatever forms and by whatever

means they may have been created or stored, including any form of computer or

electronic storage (such as hard disks or other media that can store data).” Id. at 39. In a

separate provision, the warrant sought “Any computers, cell phones, and/or electronic

media that could have been used as a means to commit the offenses described on the

warrant.” Id. at 87. Finally, for any electronic device, whether it was used to commit the

offenses or simply had relevant records stored on it, the warrant permitted the agents to

search and seize evidence of who used, owned, or controlled the device, such as

“configuration files . . . documents, browsing history . . . photographs, and

correspondence . . . .” Id. at 38.

   A. The First Search

       On November 20, 2012, FBI agents including Agent Aaron Cravens and

Special Agent Brian Nishida executed the first search warrant. They discovered a

large volume of electronic media in Loera’s residence, including CDs, DVDs, laptop

computers, external hard drives, a USB flash drive, an iPhone, and an iPad. Cravens

and Nishida were responsible for “previewing” the CDs at Loera’s residence to

ensure that the FBI seized only those CDs that contained information relevant to the

authorized investigation. ROA Vol. II at 53, 58. The two agents split up the CDs

between themselves and searched them separately.

       Cravens tried to view the files of the first CD using a program called FTK

Imager, which would have allowed Cravens to limit his search to a particular type of

                                             4
file, for example, only image, text, or audio files. However, the program did not

work. Consequently, Cravens opened the CD on a computer and used the “thumbnail

view” to preview the files stored on it, meaning, he saw small images of the files, the

file names, and the file types in a vertical list that he had to scroll through to see in

its entirety. Although Cravens believed he had authority under the first warrant to view

the entire contents of the CD, Cravens used the thumbnail-image view to fast-track his

search. He would scroll past irrelevant files but “click[] on anything that didn’t appear

correct, or any documents” to open them. Id. at 92. While Cravens was “scrolling

down through the images or files . . . on the CDs, [he] found what looked like a nude

child.” Id. at 60. He opened the file to confirm that it was an image of child

pornography. After determining that it was, Cravens ejected the CD from his

computer, set it aside, and alerted Agent Nishida and the FBI agent in charge of

Loera’s case. Then, Cravens searched the rest of the CDs assigned to him for

evidence of computer fraud. Cravens later found a child pornography image on a

second CD. Just as he did with the first, Cravens set the CD aside after discovering the

illegal images and did not open any other files on that CD.

       Agent Nishida took a different approach to his search. He previewed the files

on his assigned CDs using the “details view” of Windows Explorer, meaning that he

saw a list of files, file names, and last-modified dates of those files, but not pictures

associated with the files. Id. at 157. For his search of the CDs, or “triage,” as he called

it, Nishida would open two or three files on each CD and then determine from that

sample whether the CD should be seized pursuant to the warrant. Id. at 160. If Nishida

                                             5
found something he believed might be responsive to the warrant in the files that he

sampled, he would set the CD aside to be reviewed off-site. As he was sampling files,

Nishida found child pornography on two CDs. Unlike Cravens, Nishida did not cease his

search of those CDs after discovering child pornography; he continued sampling files on

the CDs to determine if they contained information that was responsive to the warrant.

       The FBI seized thirteen CDs in total from Loera’s residence: four contained child

pornography images and nine contained evidence of computer fraud.1 In addition to the

thirteen CDs, the FBI seized computers, external hard drives, an iPhone, and an iPad.

    B. The Second Search

       One week later, on November 27, 2012, Cravens decided to apply for a search

warrant to search the items seized from Loera’s residence for child pornography.

Cravens wanted to include in his warrant affidavit a detailed description of one child

pornography image from each of the four CDs on which he and Nishida had found child

pornography during their on-site preview. Consequently, Cravens opened each of the

four CDs, viewing several images on each, to find child pornography images that he

could accurately describe. Viewing the photos and drafting the affidavit took a total of

two-and-a-half hours. However, Cravens testified before the district court that he did not

spend “anywhere near the two-and-a-half hours” actually looking at photos on the CDs.

Id. at 74-75.



1
 There is no indication in the record whether the four CDs that contained child
pornography also contained evidence responsive to the warrant. However, Loera does
not challenge the FBI’s seizure of those CDs pursuant to the first warrant.
                                             6
       Cravens’ affidavit included two sections. In Section I, Cravens described his

training and experience with computers and child pornography. In Section II, Cravens

explained the details of the FBI’s investigation of Loera that led to the agent’s discovery

of child pornography on the CDs in Loera’s residence. In particular, paragraph 21

described in general terms how Cravens discovered the child pornography:

       21. In the process of executing this warrant, an FBI certified computer
       forensic examiner and a computer analysis response team (CART)
       technician previewed the loose media located during the search (e.g.,
       thumb drives, CD-Rs, DVD-Rs, memory cards, etc.) for evidence
       relevant to the original unrelated investigation. During the preview, the
       examiners identified four writable CDs which appeared to contain
       images of child pornography. The CDs were seized and placed in the
       evidence control room at the local FBI office.

ROA Vol. I at 120. In paragraph 23, Cravens explained that on November 27, 2012,

he “reviewed the four CDs . . . that were believed to contain child pornography,” id.

at 121, and that “[d]uring the review of the CDs, [he] observed multiple pictures of

children many of which are in various states of dress,” id. Then, in paragraphs

24-27, Cravens provided a detailed description of one image from each CD that

depicted a minor engaged in sexually explicit conduct. Cravens’ descriptions

included the apparent age of the minor and the conduct depicted. On November 29,

2012, based on Cravens’ affidavit, a federal magistrate judge approved a warrant to

search the thirteen CDs and six other electronic devices that were seized from Loera’s

residence for child pornography (“the second warrant”).




                                             7
   C. Searches Pursuant to the Second Warrant

      Agent Nishida executed the second warrant on two separate dates. In December

2012, Nishida searched Loera’s laptop pursuant to both the first and second warrants,

looking for evidence of computer fraud and child pornography. He discovered more than

730 child pornography images on Loera’s laptop. In April 2013, Nishida searched the

four CDs seized from Loera’s residence for child pornography pursuant to the second

warrant. He discovered approximately 330 images and two movies of child pornography

on those CDs.

   D. Proceedings Below

      A federal grand jury indicted Loera on several counts of possessing child

pornography that implicated the images found on both his laptop and his CDs. Loera

filed a motion to suppress that child pornography evidence, and the district court

denied the motion. Loera filed a motion for reconsideration, which the district court

also denied. Following that denial, Loera pled guilty to one count of knowingly

receiving child pornography in violation of 18 U.S.C. §§ 2252(a)(2), 2252(b)(1), and

2256, pursuant to a plea agreement, but he reserved the right to appeal the denial of

his motions.

      On appeal, Loera argues that the district court should have suppressed the

child pornography evidence discovered during the first search, the second search, and

the searches conducted pursuant to the second warrant because, according to Loera,

each search was unlawful. Loera argues that the first search exceeded the scope of

the first warrant, the second search exceeded the scope of the first warrant, and the

                                            8
last two searches, while authorized by the second warrant, were unlawful because

that warrant was invalid. Additionally, Loera maintains that none of the exceptions

to the warrant requirement apply to the searches in this case. We conclude that the

first search was lawful, but we agree with Loera that the remaining searches were

unlawful. Nevertheless, we AFFIRM the district court’s denial of Loera’s motion to

suppress and motion to reconsider under the inevitable discovery doctrine.

                                  II.   DISCUSSION

   A. Standard of Review

       “When reviewing the district court’s denial of a motion to suppress, we view

the evidence in the light most favorable to the government and accept the district

court’s factual findings unless they are clearly erroneous,” United States v. Grimmett,

439 F.3d 1263, 1268 (10th Cir. 2006), but “[t]he ultimate question of reasonableness

under the Fourth Amendment is a legal conclusion that we review de novo.” Id.

Accordingly, de novo review applies to the issues we address in this opinion,

including, the scope of a search warrant, United States v. Angelos, 433 F.3d 738, 745

(10th Cir. 2006), the sufficiency of a search warrant, United States v. Danhauer, 229

F.3d 1002, 1005 (10th Cir. 2000), the applicability of the good-faith exception, id.,

and the applicability of the inevitable discovery doctrine, United States v. Christy, 739

F.3d 534, 540 (10th Cir. 2014).

   B. Validity of the Government’s Application for the First Warrant

       First, Loera argues that the FBI agents obtained the initial warrant to search

his residence for evidence of computer fraud as a pretext to search instead for

                                            9
evidence of child pornography. The district court disagreed, finding that the sole

purpose of the first search was to uncover evidence of computer fraud. We affirm

that conclusion.

      Loera’s pretext argument is based on a statement that Agent Nishida made in a

report dated February 28, 2013, three months after the first and second searches were

conducted. In that report, Nishida wrote:

      On November 14, 2012, SA Michael Boady requested that the above
      listed specimen or specimens be examined for evidence of intercepting a
      communication. For example, e-mail messages to or from the domain
      Susanna2010.com. In addition, SA Boady requested that the evidence
      also be examined for evidence of child pornography possession and
      receipt.

ROA Vol. II at 191–92. Loera argues that this report proves that on November 14,

2012, six days before the first search, Agent Nishida received instructions to search

Loera’s home and effects for evidence of child pornography.

      The district court made explicit factual findings to the contrary, which are

supported by the record. First, the district court found that, had the FBI agents had

suspicions that Loera possessed child pornography, agents would have included that

information in their application for the first warrant. Second, Agent Nishida testified

at the suppression hearing that the February 2013 report summarized two separate

instructions from SA Boady: on November 14, 2012, Boady instructed Nishida to

search for evidence of interception, and, later, Boady instructed Nishida to search for

evidence of child pornography. Finally, both Cravens and Nishida testified at the

suppression hearing that the purpose of the November 20 search was only to uncover


                                            10
evidence of computer fraud, and the district court credited that testimony. Each of

these facts supports the district court’s determination that the agents conducted the

first search solely to look for evidence of computer fraud. And we are unpersuaded

by Loera’s only evidence of pretext, the report written three months after the

allegedly pretextual search.2

       Thus, we conclude the FBI agents had no pretextual motivations for obtaining

the first warrant, and we affirm the district on this issue.

    C. Reasonableness of the First and Second Searches

       Next, we determine that the first search of Loera’s residence was reasonable

because it was directed solely at uncovering the items specified in the first warrant

both before and after the officers discovered the child pornography evidence.

However, we conclude that the second search was unreasonable because it was

directed at uncovering evidence of child pornography.

    1. Relevant legal principles

       The Fourth Amendment provides:

       The right of the people to be secure in their persons, houses, papers, and
       effects, against unreasonable searches and seizures, shall not be
       violated, and no Warrants shall issue, but upon probable cause,
       supported by Oath or affirmation, and particularly describing the place
       to be searched, and the persons or things to be seized.




2
 Alternatively, even if the agents had an additional motive for conducting the first
search, that argument would fail as a matter of law under Whren v. United States,
517 U.S. 806, 813 (1996).
                                            11
U.S. Const. amend. IV. It is now well-recognized that “the ultimate touchstone of

the Fourth Amendment is ‘reasonableness.’” Brigham City v. Stuart, 547 U.S. 398,

403 (2006). “[R]easonableness generally requires the obtaining of a judicial

warrant,” Riley v. California, 134 S.Ct. 2473, 2482 (2014), subject to only a few

exceptions. The warrant must “particularly” describe “the place to be searched, and

the persons or things to be seized,” U.S. Const. amend. IV.

      However, obtaining a sufficiently particular warrant is just the first step to

conducting a reasonable search. The officers tasked with executing a sufficiently

particular warrant must conduct their search “strictly within the bounds set by the

warrant.” Bivens v. Six Unknown Named Agents of Fed. Bureau of Narcotics, 403

U.S. 388, 395 n.7 (1971) (quoting Marron, 275 U.S. at 196). The Supreme Court has

held that, “[i]f the scope of [a] search exceeds that permitted by the terms of a validly

issued warrant . . . the subsequent seizure [of evidence] is unconstitutional without

more.” Horton v. California, 496 U.S. 128, 140 (1990).

      Determining whether a search exceeds the scope of its authorizing warrant is,

like most inquiries under the Fourth Amendment, an exercise in reasonableness

assessed on a case-by-case basis. Dalia v. United States, 441 U.S. 238, 258 (1979)

(holding that the manner of a search is subject to “later judicial review as to its

reasonableness”). The general Fourth Amendment rule is that investigators executing

a warrant can look anywhere where evidence described in the warrant might

conceivably be located. United States v. Ross, 456 U.S. 798, 824 (1982). For

example:

                                           12
       Just as probable cause to believe that a stolen lawnmower may be found in
       a garage will not support a warrant to search an upstairs bedroom, probable
       cause to believe that undocumented aliens are being transported in a van
       will not justify a warrantless search of a suitcase. Probable cause to believe
       that a container placed in the trunk of a taxi contains contraband or
       evidence does not justify a search of the entire cab.

Id. This limitation works well in the physical-search context to ensure that searches

pursuant to warrants remain narrowly tailored, but it is less effective in the electronic-

search context where searches confront what one commentator has called the “needle-in-

a-haystack” problem. Orin S. Kerr, Digital Evidence and the New Criminal

Procedure, 105 Colum. L. Rev. 279, 301 (2005). Given the enormous amount of data

that computers can store and the infinite places within a computer that electronic

evidence might conceivably be located, the traditional rule risks allowing unlimited

electronic searches.

       To deal with this problem, rather than focusing our analysis of the

reasonableness of an electronic search on “what” a particular warrant permitted the

government agents to search (i.e., “a computer” or “a hard drive”), we have focused

on “how” the agents carried out the search, that is, the reasonableness of the search

method the government employed. See United States v. Burgess, 576 F.3d 1078

(10th Cir. 2009); United States v. Walser, 275 F.3d 981 (10th Cir. 2001); United

States v. Carey, 172 F.3d 1268 (10th Cir. 1999). Our electronic search precedents

demonstrate a shift away from considering what digital location was searched and

toward considering whether the forensic steps of the search process were reasonably

directed at uncovering the evidence specified in the search warrant. Shifting our


                                             13
focus in this way is necessary in the electronic search context because search

warrants typically contain few—if any—restrictions on where within a computer or

other electronic storage device the government is permitted to search. See United

States v. Christie, 717 F.3d 1156, 1165 (10th Cir. 2013) (holding that, so long as an

electronic search warrant requires the government to “direct all of its search efforts”

toward evidence relating to a specific crime, the warrant is sufficiently particular,

even where it permits the government to search a “computer” for “all records”

relating to the crimes of “murder, neglect, and abuse”). Because it is “unrealistic to

expect a warrant prospectively [to] restrict the scope of a search by directory,

filename or extension or to attempt to structure search methods,” Burgess, 576 F.3d

at 1093 (alteration added), our ex post assessment of the propriety of a government

search is essential to ensuring that the Fourth Amendment’s protections are realized

in this context. Our precedent of Carey, Burgess, and Walser, to which we turn next,

are instructive as to what constitutes a reasonable electronic search pursuant to a

valid warrant.

      Carey is the only case in which we invalidated an electronic search for

exceeding the scope of its authorizing warrant. See 172 F.3d at 1276. There, a

police officer obtained a warrant to search files on the defendant’s computer for

evidence “pertaining to the sale and distribution of controlled substances.” Id. at

1270. Prior to searching the computer, the officer first viewed the computer’s file

directory, which showed numerous “JPG” files with sexually suggestive titles. Id.

During his search, the officer came across a number of files that he did not recognize

                                           14
and that he was unable to view on the computer that he was using. Id. at 1271. To

view the files, the officer downloaded them onto a separate disk, inserted that disk

into another computer, and then was immediately able to view a “JPG file” that

depicted child pornography. Id. Rather than navigating away from the

nonresponsive material, the officer “downloaded approximately two hundred forty-

four” more JPG files and then transferred them to nineteen disks, viewing five to

seven images on each disk to determine that they all contained child pornography.

Id. The whole process took about five hours. Id. at 1273. After he had catalogued

the child pornography images in this manner, he then “returned” to his “original task

of looking for evidence of drug transactions.” Id. at 1271.

      The Carey court held that this was an unlawful, general exploratory search

because, although it was permissible for the officer to open the first JPG file to see if

it was responsive to the warrant, id. at 1273 n.4, his opening of the remaining files

exceeded the bounds of the authorizing warrant, id. at 1276. The Carey court’s

holding turned on four facts: (1) the officer spent five hours, a significant amount of

time, specifically perusing the trove of nonresponsive material, id. at 1273; (2) the

nonresponsive files were characteristically distinct and set apart from the other files

on the computer (such that they could have been avoided) because each file was

labeled “JPG,” many had sexually suggestive titles, and the officer had to download

them to open them, id. at 1274; (3) the officer did not discover the files inadvertently

(at least after his first look), id. at 1273; and (4) a more narrowly tailored search was

possible—the officer could have gone back to searching for drug-related documents

                                           15
much sooner than he did, id. at 1273. Importantly, we did not condemn the officer’s

decision to return to searching for drug-related documents after discovering the child

pornography, but, instead, we condemned his “temporar[y] abandon[ment]” of the

original search to conduct a “five hour search of the child pornography files.” Id. at

1273.

        Next, we turn to Walser and Burgess, both of which upheld electronic searches

in which the investigator discovered incriminating, nonresponsive material while

executing a search warrant but then navigated away from it. In United States v.

Walser, the police obtained a warrant to search the defendant’s hotel room for

electronically stored records of “evidence of the possession of controlled

substances.” 275 F.3d 981, 983–84 (10th Cir. 2001). A police officer searched the

room pursuant to the warrant and found a laptop and a digital camera. Id. at 984.

The agent seized the laptop, removed it from the hotel room, and then conducted a

drug-specific search of the laptop, looking for “ledgers of drug transactions or images

of drug use.” Id. In order to find those things, the agent employed a particularized

search method that “selectively proceeded to the ‘Microsoft Works’ sub-folder on the

premise that[,] because Works is a spreadsheet program, that folder would be most

likely to contain records relating to the business of drug trafficking.” Id. at 986. It

was while searching the contents of the Works folder that the officer came across a

file labeled “bstfit.avi” and opened it. Id. at 984. When he viewed the contents, he

discovered that the file contained child pornography images. Id. at 986–87. He then

immediately ceased his search. Id.

                                           16
       We upheld the officer’s search as reasonable because we determined that, by

using a particularized search method, the officer avoided conducting the kind of

“sweeping, comprehensive search of a computer’s hard drive” that Carey prohibited.

Id. at 986. The defendant in Walser argued that the agent exceeded the scope of the

warrant by opening the “AVI file,” a video file, because “it could not possibly have

contained the type of evidence the [a]gent was authorized to search for, namely,

records of drug transactions or still images of drug use.” Id. at 987. We rejected that

argument by interpreting Carey to excuse an officer’s discovery of child pornography

during a search for “relevant records in places where such records might logically be

found” so long as the officer does not conduct a supervening search specifically

directed at finding pornography evidence. Id. at 986. Applying that rule, we held in

Walser that the officer’s opening the “bstfit.avi” file was permissible because (1) he

was looking in a folder that was “most likely to contain records relating to the

business of drug trafficking” when he opened it, and (2) he did not conduct an

intervening search directly focused on child pornography like the agent in Carey. Id.

Based on those facts, we concluded that the “search was reasonable and within the

parameters of the search warrant” and that the evidence found as a result of it did not

need to be suppressed. Id. at 987.

       Finally, in United States v. Burgess, 576 F.3d 1078 (10th Cir. 2009), we again

upheld an electronic search that uncovered evidence of child pornography as

reasonable and within the scope of its authorizing warrant. There, police obtained a

warrant to search a motorhome for, among other things, “computer records” that

                                            17
would tend to show “conspiracy to sell drugs.” Id. at 1083. The warrant

incorporated the affidavit on which it was based, which stated that the affiant “knows

that persons involved in trafficking or the use of narcotics often keep photographs of

coconspirators or photographs of illegal narcotics in their vehicle.” Id.

      Based on the warrant, officers searched two hard drives and a laptop found in

the motorhome. Id. An agent searched one of the hard drives by using a program

called EnCase, which copies the contents of a hard drive over to a computer to

prevent file corruption. Id. at 1083–84. EnCase allows an investigator to “preview”

reduced-sized photos of each image file as they are being copied. Id. at 1084, 1094.

The agent took advantage of this feature and viewed each image file on the hard drive

as it was being copied. Id. at 1084. After viewing 200-300 digital images, mostly

personal photos, the agent saw an image that looked like child sexual exploitation.

Id. He then closed the preview program and sought a warrant to search all of the

defendant’s electronic storage devices for evidence of child pornography. Id. Upon

conducting that search, the agent found more than one hundred thousand illegal

images. Id.

      The defendant asked the district court to suppress the child pornography

evidence because, he argued, the agent’s use of the “preview” program exceeded the

scope of the warrant because he did not employ a particularized search method like

the agent in Walser but instead looked through each image file contained on the hard

drive. We determined that the agent’s use of the “preview” program was reasonable

and did not exceed the scope of the warrant for two reasons. First, we noted that,

                                          18
because the warrant did not expressly limit the file types that the agent was allowed

to search, for example, by limiting the search to text files (.doc, .wpd, .txt, etc.), the

agent was well within the scope of the warrant when he decided to view all of the

image files on the hard drive using the preview program. Id. at 1092. Second, we

determined that there was no reasonable way for the agent to conduct a more

narrowly tailored search because, when the object of a search is likely to be an image

file, as it was in Burgess, “there may be no practical substitute for actually looking in

many (perhaps all) folders and sometimes at the documents contained within those

folders.” Id. at 1094.

       Reading these cases together, we determine that four features of the

unconstitutional search in Carey demonstrate that it was unreasonably directed at

uncovering evidence of child pornography, rather than directed at the evidence

specified in the warrant, and distinguish it from the reasonable searches in Walser

and Burgess: (1) the length of time the searching officer spent looking at the

incriminating, nonresponsive evidence (five hours in Carey versus less than one

minute in Walser and Burgess); (2) the fact that the nonresponsive files were set apart

from the responsive files saved on the storage device (JPG files downloaded onto

separate disks in Carey versus generic files intermingled all in one place in Burgess);

(3) the manner in which the evidence was discovered (purposefully in Carey versus

inadvertently in Walser and Burgess);3 and (4) the breadth of the search method


3
 We acknowledge that in Horton v. California, 496 U.S. 128, 130 (1990), the
Supreme Court held that, in physical searches, “even though inadvertence is a
                                            19
employed (the wide detour in Carey versus the narrowly tailored search in Walser).

Contrary to Loera’s assertion, these cases do not require that officers stop searching

upon discovering evidence of a crime outside the scope of the warrant. Such a rule

would prohibit what the Fourth Amendment expressly permits—reasonable searches

based upon a warrant supported by probable cause. We have never required that.

      This conclusion brings us in line with every circuit that has confronted this

issue. See United States v. Stabile, 633 F.3d 219, 240 (3d Cir. 2011) (upholding

denial of motion to suppress where officers continued warrant-authorized search of

the defendant’s computer for financial crimes after discovering child pornography);

United States v. Williams, 592 F.3d 511, 521–24 (4th Cir. 2010) (upholding search

where the officer continued his warrant-authorized search of the defendant’s

computer for evidence of “making threats and computer harassment” after

discovering child pornography); United States v. Miranda, 325 F.App’x 858, 859–60

(11th Cir. 2009) (per curiam) (unpublished) (upholding search where officer

continued his warrant-authorized search for evidence of counterfeit software after

discovering child pornography); United States v. Wong, 334 F.3d 831, 834 (9th Cir.


characteristic of most legitimate ‘plain view’ seizures, it is not a necessary
condition.” However, because Carey, Walser, and Burgess, each of which succeeded
Horton in time, considered the subjective intentions of the searching officers where
that information was available, we continue to include inadvertence as a factor to
consider when deciding whether an electronic search fell within the scope of its
authorizing warrant or outside of it. The fundamental differences between electronic
searches and physical searches, including the fact that electronic search warrants are
less likely prospectively to restrict the scope of the search, justify our inclusion of
that factor. See Horton, 496 U.S. at 139 (abandoning inadvertence as a necessary
condition for a legitimate plain view seizure).
                                          20
2003) (upholding denial of motion to suppress where the officer continued his

warrant-authorized search of the defendant’s computer for, among other things,

“[a]ny maps, receipts, or writings, depicting Churchill County Nevada” after

discovering child pornography).

       Although officers do not have to stop executing a search warrant when they

run across evidence outside the warrant’s scope, they must nevertheless reasonably

direct their search toward evidence specified in the warrant. What that looks like

depends on the particular facts of a given case. Narrowly tailored search methods

that begin looking “in the most obvious places and [then] progressively move from the

obvious to the obscure,” Burgess, 576 F.3d at 1094, should be used where possible but

are not necessary in every case. In cases like this one, where the electronic storage

device is not well-organized and the most practical way to search it is through an item-

by-item review, “there may be no practical substitute for actually looking in many

(perhaps all) folders and sometimes at the documents contained within those folders.”

Id. In such a case, however, the searching officer must respond appropriately to what

he or she sees. The reasonableness of a search evolves as the search progresses and

as the searching officer learns more about the files on the device that he or she is

searching.

       An analogy to the physical realm is helpful here. Imagine a warrant authorizes

police officers to search a “residence” for evidence of “firearms and ammunition.”

Under that warrant, it would be reasonable for a police officer to search the medicine

cabinet in the bathroom for a minute or two to see if a small gun or ammunition is

                                            21
hidden there, however, it would be unreasonable for the officer to spend two hours

reading the labels on each bottle of medicine in the cabinet. On the other hand, if the

warrant had authorized the officer to search the residence for evidence of “illegal

drug trafficking and manufacture,” an intensive search of the medicine cabinet would

be reasonable. In both cases, the medicine cabinet is fair game to search, but the

intensity level of the permitted search differs depending on the evidence to be seized.

The same is true for electronic searches. While in some cases many (perhaps all)

electronic areas of a computer will be fair game to search, the level of intensity that

officers are permitted to spend searching those areas will differ depending on

whether the area appears to contain responsive material. This is true even when

officers come across evidence of incriminating, nonresponsive material. In all cases,

the ultimate test is the one mandated by the Fourth Amendment: whether the search

was “reasonable” under the circumstances. In the case of a computer search,

“reasonableness” requires officers to take into account the flexibility of computers

and the multiple configurations to which they may be adapted. As the computer

search continues and as the executing officer obtains more information about how a

suspect used his computer, that too may inform the reasonableness of the continuing

search.

       We now apply these principles to the November 20 and 27 searches conducted

in this case.




                                           22
   2. November 20 search was reasonable

      Loera argues that, although the first warrant permitted the FBI agents to search his

CDs for evidence of computer fraud, the officers’ search exceeded the scope of the first

warrant when they continued searching after discovering evidence of child pornography.

We disagree. The searches that Agent Cravens and Agent Nishida each conducted of

Loera’s CDs on November 20 were reasonable and conducted within the scope of the

first warrant because at all times each was reasonably directed at discovering evidence of

computer fraud. Therefore, the first search did not violate the Fourth Amendment and

thus did not warrant suppression of the evidence discovered during that search.

      The agents’ searches on November 20 resemble the searches in Walser and

Burgess more than they resemble the search in Carey, both before and after they

discovered the child pornography evidence. First, both agents here spent very little

time looking at the child pornography images they discovered. They noticed them,

alerted a supervisor, and then moved on to the rest of the images on the same CD (in

Nishida’s case), or the other CDs (in Cravens’ case), looking for evidence of

computer fraud. Both responses were reasonable because, as mentioned above, the

agents were not required to stop searching altogether. And both responses

demonstrate an effort to navigate away from the nonresponsive material and toward

files that they believed were more likely to contain material responsive to the

warrant. Second, the files on the CDs that the agents previewed were not

characteristically distinct or set apart from the other files, in contrast to Carey. Agent

Cravens testified that, when he put a CD into his computer to see the files that it

                                            23
contained, the computer pulled up a generic list of those files. The record does not

indicate that there were any folders or distinctive titles setting clearly apart the

nonresponsive child pornography files from the other files on the disk. Loera bears

the burden of proof on his suppression motion, and he has offered no evidence on this

point. Third, the agents discovered the child pornography files inadvertently on

November 20. Fourth, both agents’ search methods were reasonably narrow under

the circumstances, considering the fact that the CDs did not seem particularly

organized. Given that the warrant permitted the agents to search the CDs for

“photographs,” “documents,” and “configuration files,” it was reasonable for Nishida and

Cravens to search all file types on the CDs (image, video, and text) for evidence of

computer fraud rather than to narrow that search to one particular file type. The agents’

searches on November 20 were reasonable because they fell within the scope of the

first warrant both before and after they discovered the child pornography evidence. We

reverse the district court’s ruling to the contrary.

   3. November 27 search was unreasonable

       Loera also argues that Agent Cravens’ subsequent search on November 27,

2012, of the four seized CDs that contained child pornography violated the Fourth

Amendment because Cravens was “[i]ntentionally searching for evidence of a crime

outside the scope of the [f]irst [w]arrant prior to obtaining a new warrant.” Aplt. Br. 29.

In making this argument, Loera accepts that the first warrant permitted the government to

seize the four CDs that were found to contain some child pornography and to search them

for evidence of computer fraud. Therefore, Loera challenges Cravens’ November 27

                                              24
search only for exceeding that permission. Accordingly, we confine our analysis to

whether the second search exceeded the scope of the first warrant. The district court

concluded that it did and that neither exigent circumstances nor any other exception to

the warrant requirement justified that search. We agree and conclude that the district

court correctly excised the evidence obtained during the November 27th search from

Cravens’ affidavit for the second warrant. Several of the district court’s factual findings

support that result.

       The district court found that “Cravens was not searching for evidence of

electronic fraud” on November 27 but instead was searching for child pornography.

Dist. Ct. Op. at 144. The district court based this finding on Cravens’ testimony at the

suppression hearing that he reopened Loera’s CDs on November 27 specifically “[t]o

write a description of an image on the disc” so that he could “obtain a second warrant

for child pornography.” ROA Vol. II at 72. That admission is the most probative

fact in the record that Cravens’ search was directed at finding child pornography.

The district court also found that Cravens had the four CDs for a total of two-and-a-

half hours that day, during which time he searched the CDs and drafted the second

affidavit. Although the record does not indicate how long Cravens searched the CDs,

he testified at the suppression hearing that he looked at several images on each CD—

“more than just a couple” but “[m]ost likely less than a dozen.” ROA Vol. II at 143.

Whatever the amount of time, Cravens’ devoted it exclusively to nonresponsive

material. Rather than navigate away from the child pornography images when he found

them, Cravens explicitly navigated toward such images. Based on these findings, we

                                             25
agree with the district court that, in contrast with the agents’ searches on November

20, Agent Cravens’ search on November 27 was unreasonable because it was directed

at uncovering evidence of child pornography.

       The government argues that two exceptions save Cravens’ search from

violating the Fourth Amendment: the plain view doctrine and the foregone-

conclusion exception. We disagree. For its plain view argument, the government

asserts that the law permitted Agent Cravens to take a “second look” at the child

pornography images on Loera’s CDs because members of the FBI had already seen

the images in plain view during a lawful search, and, therefore, his “second look”

was no further invasion of Loera’s privacy than the initial, lawful viewing. The

government points to a Fourth Circuit case, United States v. Jackson, 131 F.3d 1105

(4th Cir. 1997), where a law enforcement officer had consent to search a residence for a

fugitive. Id. at 1107. While looking for the fugitive in the basement, the officer observed

some suspicious metal items on the floor. Id. He did not pause to examine those items at

that time, but he instead proceeded to finish his sweep for the fugitive. Id. Once

finished, he went back to take a closer look at the objects on the floor, this time

recognizing them as drug paraphernalia. Id. More officers arrived and took a look at the

paraphernalia, eventually using the presence of those items to obtain a search warrant for

the house, which uncovered a gun and large quantities of drugs. Id. at 1108. That further

search was held to have been constitutional under the plain-view doctrine. Id.

       There are too many factual distinctions between Jackson and this case to permit

Cravens’ second look under the plain view doctrine. First, as government counsel

                                             26
admitted at oral argument, there is no evidence in the record that Cravens looked at the

same photos on November 27 that the officers viewed on November 20. Second, seven

days elapsed between the first and second searches in this case, not a matter of minutes.

Third, Cravens’ “second look” led him to peruse more than just the child pornography

images, so we cannot say that the November 27 search did not cause a further invasion

of Loera’s privacy. The plain view doctrine permits the warrantless seizure of

evidence of criminal activity when police officers observe the evidence during a

lawful search. United States v. Naugle, 997 F.2d 819, 822 (10th Cir. 1993). That

doctrine cannot be used to justify Cravens’ November 27 search.

       The government also argues that Cravens’ “second look” was justified under

what it has termed the “foregone-conclusion exception” to the warrant requirement.

This doctrine comes from several of our plain view cases where we have permitted

the warrantless search of containers in plain view whose contents “are a foregone

conclusion” because the container is “not closed,” “transparent,” or, if it is closed,

“its ‘distinctive configuration . . . proclaims its contents’” nonetheless. United States

v. Corral, 970 F.2d 719, 725 (10th Cir. 1992). We have also held that the doctrine

applies “where the police have already seen the contents of a seized container prior to

conducting the search, [because] there is no significant additional invasion of privacy

involved in searching the container.” Id. at 725. We reject this argument for the

same reasons as the government’s plain view argument. Here, Cravens knew to a

near certainty that the seized and re-searched CDs contained some child pornography,

but he had no idea what else they contained. And, again, there is no evidence that

                                            27
Cravens had previously seen the child pornography images that he viewed on

November 27.

       Thus, Cravens’ November 27 search was unlawful because it exceeded the scope

of the first warrant and none of the exceptions to the warrant requirement apply.

   D. Reasonableness of the Searches Conducted Under the Second Warrant

       Additionally, Loera argues that the child pornography evidence that Agent

Nishida discovered when he executed the second warrant should have been

suppressed because the second warrant was not supported by probable cause and no

exceptions to the warrant requirement apply. We agree that the second warrant was

not supported by probable cause and that the good faith exception is inapplicable

here. However, the inevitable discovery doctrine supports the district court’s denial

of Loera’s motion to suppress, and we affirm on that basis.

   1. Second warrant was not supported by probable cause

       We review whether a magistrate properly issued a search warrant by determining

whether there was a “substantial basis” for probable cause in the affidavit submitted in

support of the warrant. Illinois v. Gates, 462 U.S. 213, 236 (1983). Because we find

that the November 27 search was unlawful, we must excise from the affidavit that

Cravens filed in support of the second warrant all of the descriptions of child

pornography that he unlawfully obtained during the second search and then

determine whether “there was probable cause absent that information.” United States

v. Sims, 428 F.3d 945, 954 (10th Cir. 2005). The district court determined that the



                                            28
second warrant remained supported by probable cause without the tainted

descriptions. We disagree.

       While “probable cause does not demand the certainty we associate with formal

trials,” Gates, 462 U.S. at 246, “[s]ufficient information must be presented to the

magistrate to allow that official to determine probable cause; his action cannot be a mere

ratification of the bare conclusions of others,” id. at 239 (emphasis added). For example,

“[a] sworn statement of an affiant that ‘he has cause to suspect and does believe that’

liquor illegally brought into the United States is located on certain premises” is not

sufficient to support a finding that probable cause exists to search the premises. Id.

       The child pornography descriptions that Agent Cravens obtained during the

unlawful second search appear in paragraphs 24-27 of Cravens’ affidavit. Once we

excise those descriptions, all that remains substantively is Cravens statement that,

“During the preview, the examiners identified four writable CDs which appeared to

contain images of child pornography.” ROA Vol. I at 120. This sentence does not

support a finding of probable cause.

       In United States v. Pavulak, the Third Circuit reviewed an affidavit to support

a warrant to search for child pornography that contained language very similar to the

bare-bones description left in the affidavit in our case, 700 F.3d 651, 661 (3d Cir.

2012). The warrant affidavit in Pavulak stated that an informant had seen the

defendant “viewing child pornography” of females “between 16 and 18 years old,”

without providing any further details about what the images depicted. Id. at 657.

The Third Circuit held that the affidavit lacked probable cause because it did not

                                             29
allow the magistrate judge “to independently evaluate whether the contents of the

alleged images [met] the legal definition of child pornography.” Id. at 661. We find

that analysis persuasive here. Agent Cravens’ remaining statement that the CDs

“appeared to contain images of child pornography” provides no detailed description

of what the images depicted such that a magistrate could independently assess

whether the images meet the legal definition of child pornography. ROA Vol. I at

120.

       Therefore, the affidavit supporting the second warrant lacked probable cause

absent the tainted information. We reverse the district court’s contrary conclusion.

   2. Good-faith exception inapplicable to these facts

       Next, we consider whether the good faith exception to the exclusionary rule

from United States v. Leon, 468 U.S. 897, 918 (1984), applies when police execute a

search warrant that is based on information obtained through an unlawful predicate

search. Disagreeing with the district court, we conclude that it does not. The

Supreme Court’s opinion in Leon and our opinion in United States v. Scales, 903

F.2d 765, 768 (10th Cir. 1990), dictate that the good faith exception does not apply in

a case like the one before us because the illegality at issue stems from unlawful

police conduct, rather than magistrate error, and therefore the deterrence purposes of

the Fourth Amendment are best served by applying the exclusionary rule.

       In United States v. Leon, the Supreme Court modified the exclusionary rule

“so as not to bar the use in the prosecution’s case in chief of evidence obtained by

officers acting in reasonable reliance on a search warrant issued by a detached and

                                          30
neutral magistrate but ultimately found to be unsupported by probable cause,” 468

U.S. at 900. The Court reasoned that the purpose of the exclusionary rule is to deter

police misconduct and in such a case “there is no police illegality and thus nothing to

deter.” Id. at 920. In this circuit, “Leon’s good faith exception applies only narrowly,

and ordinarily only when an officer relies, in an objectively reasonable manner, on a

mistake made by someone other than the officer.” United States v. Cos, 498 F.3d 1115,

1132 (10th Cir. 2007) (declining to apply good faith exception to warrantless search of

apartment where officers mistakenly believed the person that consented to the search had

the authority to do so); United States v. Herrera, 444 F.3d 1238, 1251 (10th Cir. 2006)

(declining to apply good faith exception to state trooper who conducted a warrantless

inspection of a truck based on the officer’s mistaken belief the truck was a commercial

vehicle subject to such inspection). Thus, Leon is inapplicable here where the

mistake—the unconstitutional second search—was the fault of the officer, not the

magistrate.

      We considered whether Leon applied to a warrant affidavit based on tainted

evidence in Scales, 903 F.2d at 768. There, we held that Leon did not apply to

excuse a law enforcement officer’s reliance on a search warrant where the facts in the

warrant affidavit were obtained through an unlawful predicate seizure. In that case,

DEA agents seized a suitcase that they believed contained drugs. Id. at 767. Then,

they took the suitcase to a drug-sniffing canine team that signaled the suitcase did

contain drugs. Id. Finally, after having had the suitcase in their possession for

twenty-four hours, the agents applied for and obtained a warrant to search the

                                            31
suitcase based on the probable cause provided by the canine alert. Id. Upon

conducting the search, the agents discovered more than 2,000 grams of cocaine in the

suitcase. Id. The defendant moved to suppress the cocaine evidence, arguing that the

agents’ initial seizure of the suitcase was unlawful because it was unsupported by

probable cause. Id. at 767.

      The district court in Scales denied the motion, finding that, even if the seizure

of the suitcase was unlawful, the good faith exception ratified the agents’ behavior.

Id. We reversed, holding that Leon was inapplicable “[b]ecause the DEA agents

were not acting in reliance on a search warrant when they seized the luggage and held

it for more than twenty-four hours.” Id. at 768. Our holding was informed by the

reasoning in Leon that “Penalizing the officer for the magistrate’s error, rather than

his [or her] own, cannot logically contribute to the deterrence of Fourth Amendment

violations.” Id. at 768 (quoting Leon, 468 U.S. at 921) (alteration in original).

Because the contraposition is also true—that penalizing an officer for his or her own

error does contribute to deterrence—we determined that the exclusionary rule must

apply to the agents’ unlawful pre-warrant seizure of the suitcase. Id.

      Scales and Leon control our outcome here. Cravens conducted an unlawful

search of Loera’s CDs on November 27 in the absence of a warrant. He included the

tainted fruit that he uncovered during that search in the affidavit that he submitted in

support of the second warrant. Cravens’ warrant affidavit was facially valid, and

therefore the magistrate did not error by issuing a warrant based upon it. Instead, the

constitutional error came from Agent Cravens.

                                           32
      The government argues that Cravens acted in good faith because he

“transparently informed the magistrate judge of the steps he had taken to obtain the

descriptions he included in his affidavit.” Aple. Br. at 40. Cravens’ affidavit

provided some information about the first search. It explained that, while executing

the first search warrant, the FBI agents identified four CDs that contained child

pornography and seized them. Then, Cravens wrote:

      On November 27, 2012, the writer, an FBI certified CART Technician,
      reviewed the four CDs, each of which are designated in attachment A,
      that were believed to contain child pornography. During the review of
      the CDs, the writer observed multiple pictures of children many of
      which are in various state of dress including the following images . . . .

ROA Vol. I at 50. However, that information was not sufficient to allow the

magistrate to determine the constitutionality of the second search such that the

magistrate can be said to have endorsed Cravens’ pre-warrant conduct. Furthermore,

even if it was, that would not affect our outcome. Tenth Circuit precedent dictates

that the good faith exception does not apply at all when a warrant affidavit is based

on tainted evidence from a prior, unlawful search.

      Four other circuits have likewise concluded that Leon is inapplicable when an

officer executes in good faith a search warrant that is based on unlawfully-obtained

evidence. United States v. Scott, 731 F.3d 659, 664 (7th Cir. 2013) (holding that

evidence discovered pursuant to a warrant based on illegally-obtained evidence will

be inadmissible unless other, untainted information in the affidavit establishes

probable cause); United States v. Mowatt, 513 F.3d 395, 405 (4th Cir. 2008) (holding

that “Leon only prohibits penalizing officers for their good-faith reliance on

                                          33
magistrates’ probable cause determinations” and that the exclusionary rule operates

to penalize officers for any unconstitutional conduct preceding a magistrate’s

involvement); United States v. McGough, 412 F.3d 1232 (11th Cir. 2005) (refusing

to apply good faith exception where an unlawful entry into the defendant’s apartment

led to the officer’s request for a search warrant); United States v. Vasey, 834 F.2d

782, 789 (9th Cir. 1987) (holding that good faith exception did not apply to a warrant

that was based on information obtained in an illegal warrantless search because “[t]he

constitutional error was made by the officer . . ., not by the magistrate”). At least two

commentators support this analysis as well. See Wayne R. LaFave, Search &

Seizure: A Treatise on the Fourth Amendment § 1.3(f) (5th ed. 2016) (explaining

that, because courts rarely require affiants to prove that they obtained the evidence

listed in an affidavit lawfully, “there is no reason why that process should, via Leon,

shield that activity from full scrutiny at the suppression hearing”); Craig M.

Bradley, The “Good Faith Exception” Cases: Reasonable Exercise in Futility, 60 Ind.

L.J. 287, 302 (1985) (quoting Leon, 468 U.S. at 914) (“When the magistrate issued

the warrant, he did not endorse past activity; he only authorized future activity. . . .

[T]he function of the magistrate is to determine ‘whether a particular affidavit

establishes probable cause,’ not whether the methods used to obtain the information

in that affidavit were legal.”).

       However, five other circuits have concluded that the good faith exception can

apply where an affidavit supporting a search warrant is tainted by illegally-obtained

evidence in at least some limited circumstances. Three of those circuits apply the

                                            34
good faith exception if the predicate search, although ultimately determined to be

unlawful, was arguably lawful under the binding precedent in effect at the time of the

search. United States v Bain, 874 F.3d 1, 22–23 (1st Cir. 2017) (applying good faith

exception because binding precedent did not “clearly classify” as unlawful the

conduct that invalidated the predicate search); United States v. Hopkins, 824 F.3d

726 (8th Cir. 2016) (applying good faith exception because the reasonableness of the

illegal predicate search was “close enough to the line of validity” to make an

officer’s belief in the validity of the warrant objectively reasonable); United States v.

Holley, 831 F.3d 322, 326–27 (5th Cir. 2016) (also applying “close enough to the

line of validity” test). Two other circuits apply the good faith exception in these

types of cases when (1) the predicate search was arguably reasonable and (2) the

warrant affidavit truthfully conveyed the circumstances of the illegal predicate search

to the magistrate judge. United States v. McClain, 444 F.3d 556, 566 (6th Cir. 2005)

(applying Leon because the reasonableness of the predicate search was a close call

and the warrant affidavit “fully disclosed” the circumstances surrounding the initial

warrantless search); United States v. Thomas, 757 F.2d 1359 (2d Cir. 1985) (applying

good faith exception because officer’s affidavit fully described the unlawful, pre-

warrant canine sniff that supplied probable cause for the warrant and there was

“nothing more the officer could have or should have done” to be sure his search was

legal). We cannot read Leon or Scales to support the rules adopted by these courts.

When a magistrate issues a warrant based on illegally obtained evidence, typically the

manner in which the affidavit evidence is obtained is not before the magistrate, and the

                                            35
magistrate is not asked explicitly to endorse the evidence-gathering procedure. Even

though some disclosure of the evidence-gathering technique may have occurred, that is

not ordinarily the focus of an application for a warrant. Thus, we are unwilling to read a

warrant as ratifying the information-gathering process of a search that preceded it. In any

event, we are bound by Scales, which appears to us to have been correctly decided.

       Therefore, the district court erred by finding that the good faith doctrine applied to

the searches Agent Nishida conducted in execution of the second warrant.

   3. Inevitable discovery doctrine supports denial of Loera’s motion

       Finally, we consider whether the government would have inevitably discovered

the child pornography evidence on Loera’s electronic devices. Loera argues that, because

there was no probable cause to support the second warrant, all evidence discovered as a

result of the execution of the second warrant should have been suppressed. The issue

before us, then, is whether the FBI agents would have inevitably discovered the roughly

330 child pornography images on Loera’s CDs and 730 child pornography images on

Loera’s laptop that Nishida found when he executed the second warrant. We conclude

that they would have. Accordingly, we affirm the district court’s denial of Loera’s

motion to suppress.

       When evidence is obtained in violation of the Fourth Amendment, that

evidence need not be suppressed if agents inevitably would have discovered it

through lawful means independent from the unconstitutional search. United States v.

Christy, 739 F.3d 534, 540 (10th Cir. 2014). The government is required to prove by a

preponderance of the evidence that the unlawfully-obtained evidence would have been

                                             36
discovered through lawful means. Id. The “lawful means” need not be a second,

independent investigation. Id. Rather, the inevitable discovery doctrine will apply if

there was “one line of investigation that would have led inevitably to the obtaining of a

search warrant by independent lawful means but was halted prematurely by a search

subsequently contended to be illegal.” Id. (citations omitted). The key to applying this

doctrine is to place the government officers in the “same positions they would have

been in had the impermissible conduct not taken place,” and, from that vantage point,

to ask whether the government would have inevitably discovered the evidence

lawfully. Nix v. Williams, 467 U.S. 431, 447 (1984).

       Here, the district court’s supportable findings demonstrate by a preponderance of

the evidence that the FBI would have inevitably discovered the child pornography

evidence on Loera’s electronic devices through lawful means independent from Agent

Cravens’ unlawful second search. On November 26 (the day before the second search),

the government lawfully had in its possession Loera’s computers, external hard drives,

iPhone, iPad, and thirteen CDs (nine without child pornography and four with child

pornography).4 The government had the authority under the first warrant to search

Loera’s electronic devices—most importantly his laptop and CDs—for evidence of

computer fraud. The district court issued an explicit factual finding that, had the

second warrant never been obtained, Agent Nishida would “have searched [Loera’s



4
  As mentioned above, although Loera challenges the first search of these four CDs,
he does not separately challenge their seizure were we to determine, as we have, that
the first search was constitutional.
                                            37
laptop] for evidence of electronic mail hijacking and computer fraud pursuant to the

[f]irst [w]arrant.” Dist. Ct. Op. at 24. The district court further found that, as part of

that search, lawfully conducted pursuant to the parameters of the first warrant, Agent

Nishida would have searched the electronic folders where he discovered child

pornography when he executed the second warrant, including, the “My Documents”

folder, the “Bookmarks” tab of Loera’s internet browser, and a folder saved on the

Desktop titled “Allmyfiles.txt.” Id. at 24–25. The district court also accepted

Nishida’s statement that, had he found child pornography images on the laptop

during a search conducted solely pursuant to the first warrant, he would have “alerted

the case agent so that [he] could get a search warrant for child pornography.” Id. at

25.

      The laptop, including the specific files referenced above, contained over 730

images and 40 movies involving child pornography. Id. at 24. To take one specific

example, the “Allmyfiles.txt” file, which the district court found Nishida would have

lawfully opened pursuant to the first warrant, contained files called “Spycam 9yr

Undress.” Id. Such information would have been sufficient to establish probable

cause to support a warrant to search all of the electronic devices belonging to Loera

that the government had in its possession, including the four CDs that Agent Cravens

searched unlawfully on November 27. That fact, combined with Agent Nishida’s

indication that he would have sought a warrant, allows us to conclude that the

inevitable discovery doctrine applies in this case such that the evidence discovered

pursuant to the second warrant did not need to be suppressed.

                                            38
                             III.   CONCLUSION

      For the foregoing reasons, we AFFIRM the orders of the district court denying

the defendant’s motion to suppress and motion for reconsideration.




                                         39

```

---

## GROUP: _overhaul2/lake/cases/United States v. Loines.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Loines
type: case
citation: "56 F.4th 1099 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir.
court_level: coa
circuit: ca6
year: 2023
date_decided: 2023-01-06
docket: 21-1516
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
  opinion_url: "https://www.courtlistener.com/opinion/9357039/united-states-v-aaron-loines/"
  cluster_id: 9357039
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Loines
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[Arizona v. Hicks]]"
  - "[[Texas v. Brown]]"
  - "[[Horton v. California]]"
tags:
  - case
  - fourth-amendment
  - search
  - plain-view
  - probable-cause
  - immediately-apparent
  - automobile-exception
  - sixth-circuit
holding: "The Sixth Circuit reversed the denial of suppression and vacated the conviction, holding that the plain-view doctrine did not supply probable cause to search Loines's car: a detective's claim to have seen a 'bag of dope' through a tinted window was not plausible on the record, and in any event the objects — a plastic bag near a cigar wrapper and a lottery ticket — were not immediately and apparently incriminating from outside the car, their criminal character emerging only after officers entered and closely inspected the console, itself a further search unsupported by probable cause."
---

# United States v. Loines

*56 F.4th 1099 (6th Cir. 2023)* (No. 22-3073) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9357039 → opinion 9352511 (56 F.4th 1099, decided 2023-01-06, Clay, J.). NOTE: appeal docket is No. 22-3073 (per the opinion caption); the lake stub's docket field reads 21-1516 (stale — flag for S2). Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In April 2020, Cleveland detective Donald Kopchak was investigating Mekhel Rivers for drug trafficking; after surveillance, police obtained and executed a search warrant for Rivers's Euclid, Ohio house. During the search, Kopchak walked to a red Nissan parked on the street, cupped a hand to the tinted window, leaned in, and claimed to see a "bag of dope" — a small plastic bag near a Black & Mild cigar wrapper and a folded lottery ticket — in the center console; a lieutenant said he saw it too. Officers found Aaron Loines inside the house; Loines said the car keys were his (confirmed by sounding the alarm). The Nissan was towed and searched without a warrant, yielding a firearm, suspected narcotics, a press, and a scale. Loines moved to suppress; the government justified the warrantless search solely on the "plain view" of the "bag of dope," with Kopchak the only witness. The district court denied the motion, and Loines pled guilty to controlled-substance and § 924(c) firearm offenses, preserving the appeal.

## Issue
Whether the [[Plain View Doctrine|plain-view doctrine]] gave the officers probable cause to search Loines's vehicle without a warrant — in particular, whether the objects the detective claimed to see through the tinted window were actually in plain view and whether their incriminating character was "immediately apparent."

## Rule
The plain-view exception requires that the item be in plain view, that its incriminating character be **immediately apparent**, that the officer be lawfully positioned to see it, and that he have a lawful right of access. "Immediately apparent" means the object's criminal character is apparent at the time of discovery without further inspection; lawful, innocuous items cannot be seized under the doctrine absent an immediately apparent association with criminal activity. Applying that standard, the court held the predicate failed: "The objects purportedly seen by Kopchak were not immediately and apparently incriminating. Accordingly, the officers lacked probable cause to search the vehicle." — 56 F.4th 1099, slip op. at 13. ^pin-op13

## Application
The court found the detective's account — that he saw a "bag of dope" through the tinted window from outside the car — not plausible on the record: Kopchak never claimed to see narcotics or residue on the lottery ticket, did not claim the cigar wrapper was contraband, and gave no description of the plastic bag as seen from outside. The bag's incriminating character emerged only after the officers entered the vehicle and closely inspected the center console — and that close inspection constituted a further search unsupported by probable cause. Because the innocuous items were not immediately and apparently incriminating, there was no probable cause, so the plain-view rationale failed — and with it the automobile exception, which the government had tied to the same predicate. Having found the objects were not in plain view, the court did not reach whether Kopchak's cupping his hands against the window was itself an unlawful trespass.

## Conclusion
**Reversed, conviction [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]].** Judge Clay wrote for the panel (Cole, Clay, and Mathis, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Loines* is a clean cautionary application of the **plain-view / "immediately apparent"** prong: an officer's bare say-so that he saw contraband through a tinted window does not establish plain view where the item's criminal character becomes apparent only after a closer intrusion — echoing *[[Arizona v. Hicks|Hicks]]* (developing probable cause by closer inspection is itself a search) and the rule that innocuous items are not seizable without an immediately apparent criminal association.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Loines*, 56 F.4th 1099 (6th Cir. 2023)](https://www.courtlistener.com/opinion/9357039/united-states-v-aaron-loines/) — pinpoint: slip op. at 13 (not-immediately-apparent / no-probable-cause holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0707fcfba3c211fc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Loines"}, "payload": {"all": [{"cite": "56 F.4th 1099", "page": "1099", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}], "display": "56 F.4th 1099", "official": {"cite": "56 F.4th 1099", "page": "1099", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "56"}, "official_selection_present": true, "record_id": "United States v. Loines"}}
{"assertion_id": "146293cb6757c710", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Loines"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Loines", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Loines

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Loines",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Aaron Loines",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Loines",
    "court": "6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2023-01-06",
    "year": 2023,
    "docket": "21-1516",
    "cluster_id": 9357039,
    "lead_opinion_id": 9352511,
    "sibling_ids": [],
    "absolute_url": "/opinion/9357039/united-states-v-aaron-loines/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "56 F.4th 1099",
      "volume": "56",
      "reporter": "F.4th",
      "page": "1099",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "56 F.4th 1099",
        "volume": "56",
        "reporter": "F.4th",
        "page": "1099",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "56 F.4th 1099",
    "official_selection": {
      "court_class": "coa",
      "selected": "56 F.4th 1099",
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
    "date_created": "2026-07-07T18:19:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-loines--9357039",
      "to_record_id": "United States v. Loines",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Loines

```
                                RECOMMENDED FOR PUBLICATION
                                Pursuant to Sixth Circuit I.O.P. 32.1(b)
                                       File Name: 23a0004p.06

                    UNITED STATES COURT OF APPEALS
                                   FOR THE SIXTH CIRCUIT



                                                             ┐
 UNITED STATES OF AMERICA,
                                                             │
                                    Plaintiff-Appellee,      │
                                                              >        No. 22-3073
                                                             │
        v.                                                   │
                                                             │
 AARON LOINES,                                               │
                                 Defendant-Appellant.        │
                                                             ┘

  Appeal from the United States District Court for the Northern District of Ohio at Cleveland.
                  No. 1:20-cr-00293-2—Donald C. Nugent, District Judge.

                                   Argued: October 27, 2022

                               Decided and Filed: January 6, 2023

                     Before: COLE, CLAY, and MATHIS, Circuit Judges.

                                      _________________

                                            COUNSEL

ARGUED: John J. Spellacy, JOHN J. SPELLACY & ASSOCIATES, CO., Cleveland, Ohio,
for Appellant. Matthew B. Kall, UNITED STATES ATTORNEY’S OFFICE, Cleveland, Ohio,
for Appellee. ON BRIEF: John J. Spellacy, JOHN J. SPELLACY & ASSOCIATES, CO.,
Cleveland, Ohio, for Appellant. Matthew B. Kall, UNITED STATES ATTORNEY’S OFFICE,
Cleveland, Ohio, for Appellee.
                                      _________________

                                             OPINION
                                      _________________

       CLAY, Circuit Judge. Defendant Aaron Loines appeals the district court’s denial of his
pretrial motion to suppress preceding his guilty plea to controlled substance offenses in violation
of 21 U.S.C. §§ 846, 841(a)(1), 841(b)(1)(C); and a firearm offense in violation of 18 U.S.C.
 No. 22-3073                              United States v. Loines                                      Page 2


§ 924(c)(1)(A). For the reasons set forth below, the Court REVERSES the district court’s
denial of Loines’ motion to suppress, VACATES his conviction, and REMANDS the case for
further proceedings consistent with this opinion.

                                            I. BACKGROUND

                                         A. Factual Background

        In 2020, Detective Donald Kopchak of the Cleveland Police Department was aiding in an
investigation into potential drug trafficking activities by Mekhel Rivers, who was subsequently
charged as a co-defendant. Police investigators suspected Rivers of distributing heroin and
fentanyl. During the investigation, on April 21, 2020, Kopchak observed Rivers leaving a house
on East 221st Street, in Euclid, Ohio, driving a red Nissan Ultima to a meeting place to sell drugs
to an informant, and then returning to the same Euclid house.                      After numerous days of
surveillance, investigators determined that Rivers lived at the East 221st Street house, obtained a
search warrant for the house, and executed the warrant on April 30, 2020.

        After arrving at the house, while executing the search warrant, Kopchak again observed
the red Nissan Ultima parked on the street near the residence, bearing the same license plate
number he previously observed. Kopchak walked up to the passenger side of the car, cupped a
hand to the tinted window,1 and leaned in to attempt to see into the vehicle. While leaning
against the vehicle and looking through the window, Kopchak allegedly observed a Black and
Mild cigar wrapper and “a folded piece of paper” in the center console of the car. (Tr. of Mot. to
Suppress Hr’g, R. 142, Page ID #729). From this vantage point, Kopchak claims he was also
able to view a small plastic bag that he immediately identified as “a bag of dope.” (Id. at Page
ID ##726, 729). Lieutenant Charles DiPenti approached the car’s passenger side, looked through
the window, and verbally indicated that he also saw the “bag of dope.” (Id. at Page ID #728).

        After Kopchak purportedly saw the “bag of dope” in the vehicle, he went into the East
221st Street residence. Officers found Loines in Rivers’ residence, along with other individuals


        1InOhio, side windows may be tinted, but they must permit fifty percent of the light through. Ohio Admin.
Code § 4501-41-03(A)(3). The government does not argue that Loines’ tinted windows were in violation of Ohio
law.
 No. 22-3073                               United States v. Loines                                        Page 3


implicated in this case. Kopchak read the individuals their Miranda rights and inquired about car
keys found in the home. In response, Loines volunteered that the keys were his. Kopchak then
confirmed that the car keys belonged to the Nissan by using the key to sound the car alarm.

        The car was then towed for an inventory search. During the inventory search of the
inside of the car, the officers took a picture of the car’s center console from the driver’s seat.
That picture showed a small plastic bag underneath a cigar wrapper, with a lottery ticket placed
beside it. Law enforcement searched the vehicle after it was towed and found a firearm, the bag
of suspected narcotics, a larger bag of purported narcotics,2 a press,3 and a scale. Police did not
obtain a warrant to search the automobile before or during the investigation.

        Loines moved to suppress the evidence seized from his vehicle, and during the motion to
suppress hearing, Kopchak sought to justify the warrantless search by averring that he had
probable cause to search the vehicle based on the “plain view” of the “bag of dope.” Kopchak
was the only witness called to testify at the hearing. To support Kopchak’s testimony that he
saw the “bag of dope” in plain view and thus had probable cause to search the vehicle, the
government relied upon: (1) videos of Kopchak and other officers walking around and peering
into the car; and (2) a photo taken while inside the car from the vantage point of one sitting in the
driver’s seat.

        Based on Kopchak’s testimony, the videos provided evidence of where the car was in
proximity to the East 221st Street residence, Kopchak’s position looking into the passenger side
window of the car, and Kopchak’s claim that he saw a “bag of dope.” (Tr. of Mot. to Suppress
Hr’g, R. 142, Page ID # 721–26). The videos also provide Lieutenant DiPenti’s perspective


        2The    government has not provided information as to whether the bags found in the vehicle contained
controlled substances. The only information found on the record as to whether a controlled substance was found in
the vehicle is by the government in its response to the Defendant’s motion to suppress in the court below. The
government contends that approximately “70+ of heroin” appeared in the bags and includes a footnote stating that
“[t]he lab tests on this substance showed no scheduled controlled substance.” (Resp. to Mot. to Suppress, R. 61,
Page ID # 338). There is no additional information offered as to what “70 + of heroin” means, or if any lab test was
performed to confirm that the bags found in the car contained controlled substances. However, this issue is not on
appeal. Because the Court finds that the vehicle was not lawfully searched, we need not address whether officers
actually found narcotics in the vehicle.
          3Kopchak defines a press as an object used by drug traffickers to combine, by means of compacting,
different substances together, to prepare the finished product for sale.
 No. 22-3073                         United States v. Loines                               Page 4


when looking through the passenger side window, without pressing his hands against the
window, confirming Kopchak’s observation. The photograph taken from the inside of the
vehicle illustrates a lottery ticket, cigar wrapper, and beneath the cigar wrapper, a small plastic
bag. At issue, however, is whether Kopchak and DiPenti could actually see the small plastic bag
from outside of the car.

       The government claims that the officers’ body camera footage and associated screenshots
“show[] that a person standing next to the car could see through the window, even though it was
partially tinted.” (Resp’t’s Br., ECF No. 15, 14). Furthermore, the government contends that
while no cameras were “positioned at the proper angle to show the suspected drugs,” the videos
establish that an officer could see inside the car. (Id. at 15). Neither proposition is convincing.
The videos themselves do not establish that Kopchak, from his vantage point outside the vehicle,
had a sufficiently clear view to identify the presence of drugs inside the car. Instead, the videos
show only the position of the officers when peering into the vehicle. In an attempt to provide a
better illustration of what was seen from outside the car, screenshots of the video were provided
by the government in their appellate briefing; however, those screenshots are dark to the point of
being indecipherable. Besides conclusory statements as to what officers saw, the government
has furnished no evidence to establish that the photo taken from inside the car was an accurate
depiction of what was seen from outside the vehicle.

                                     B. Procedural History

       A grand jury indicted Loines in the underlying matter on June 11, 2020. The grand jury
charged Loines with the following: one count of Conspiracy to Distribute and Possess with
Intent to Distribute Controlled Substances in violation of 21 U.S.C. § 846; one count of
Possession with Intent to Distribute Controlled Substances in violation of 21 U.S.C. §§ 841(a)(1)
and (b)(1)(C); and one count of Possession of a Firearm in Furtherance of a Drug Trafficking
Crime in violation of 18 U.S.C. § 924(c)(1)(A)(i).

       Loines filed a motion to suppress on December 22, 2020, contending that the
investigating officers conducted an unlawful warrantless search of his vehicle and any inventory
search of the vehicle in question was done improperly. After the government filed its response,
 No. 22-3073                           United States v. Loines                               Page 5


and Loines filed his reply, the district court conducted a suppression hearing on May 17, 2021.
Kopchak was the only witness in the hearing; and the government introduced, without objection,
three videos and one picture. After listening to the testimony and considering the evidence, the
court orally denied Loines’ suppression motion.

          On September 13, 2021, Loines pleaded guilty to all three counts pursuant to a plea
agreement, and reserved the right to appeal the district court’s denial of his motion to suppress.
The district court sentenced Loines to 93 months’ imprisonment, after which Loines filed this
timely appeal.

                                          II. DISCUSSION

                                       A. Standard of Review

          The Court reviews a district court’s decision on a suppression motion for clear error as to
factual findings and de novo as to conclusions of law. United States v. Jenkins, 396 F.3d 751,
757 (6th Cir. 2005). Because the appeal of the district court’s denial of Loines’ suppression
motion is based on factual findings, this Court reviews the decision for clear error. See id.
“Clear error will be found only when the reviewing court is left with the definite and firm
conviction that a mistake has been committed.” Max Trucking, LLC v. Liberty Mut. Ins. Corp.,
802 F.3d 793, 808 (6th Cir. 2015) (citing Anderson v. City of Bessemer City, 470 U.S. 564, 573
(1985)).

          “Whether a search was reasonable under the Fourth Amendment is a question of law
which is reviewed de novo.” United States v. Pearce, 531 F.3d 374, 379 (6th Cir. 2008) (citing
United States v. Blair, 524 F.3d 740, 747 (6th Cir. 2008)). “When a district court has denied the
motion to suppress, we must ‘consider the evidence in the light most favorable to the
government.’” Id. (quoting United States v. Carter, 378 F.3d 584, 587 (6th Cir. 2004) (en
banc)).

                                             B. Analysis

          The Fourth Amendment provides that “[t]he right of the people to be secure in their
persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be
 No. 22-3073                               United States v. Loines                                        Page 6


violated[.]” U.S. Const. amend. IV. “The basic purpose of this Amendment, as recognized in
countless decisions of [the Supreme] Court, is to safeguard the privacy and security of
individuals against arbitrary invasions by governmental officials.” Camara v. Mun. Ct. of City &
Cnty. of S.F., 387 U.S. 523, 528 (1967). “[S]earches conducted outside the judicial process,
without prior approval by judge or magistrate, are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and well-delineated exceptions.”
Katz v. United States, 389 U.S. 347, 357 (1967) (internal citations omitted). The government
bears the burden of demonstrating that an exception to the warrant requirement applies. United
States v. Jeffers, 342 U.S. 48, 51 (1951).

        Kopchak’s entrance into the car to obtain evidence necessary to indict Loines was subject
to the Fourth Amendment protections. The interior of a vehicle is a constitutionally protected
area, into which a government official is not permitted to intrude without probable cause. See
New York v. Class, 475 U.S. 106, 114–15 (1986) (“[A] car’s interior as a whole is [ ] subject to
Fourth Amendment protection from unreasonable intrusions by the police.”); United States v.
Jones, 565 U.S. 400, 404 (2012) (“It is beyond dispute that a vehicle is an ‘effect’ as that term is
used in the [Fourth] Amendment.”) (quoting United States v. Chadwick, 433 U.S. 1, 12 (1977)).
Officers found the evidence used to indict Loines inside of Loines’ vehicle and without a
warrant. Accordingly, for the search to be reasonable, an exception to the warrant requirement
must apply. See Katz, 389 U.S. at 357. The government asserts that Kopchak’s conduct was
permissible under two exceptions: the “plain view doctrine” and the “automobile exception.”
See Maryland v. Dyson, 527 U.S. 465, 466–67 (1999) (per curiam); Minnesota v. Dickerson, 508
U.S. 366, 374–75 (1993). Neither asserted exception applies in this case.4




        4Loines   argues that the inventory search exception does not apply in this case. However, the inventory
search exception is not properly before this Court. The government explicitly waived the inventory search exception
argument, stating “the government . . . is not relying on [the inventory search exception] directly in this appeal.”
(Resp’t.’s Br., ECF No. 15, 18). To preserve an issue for appellate review, a party must develop its argument in its
appellate briefing; a requirement that the government does not meet on this issue. Puckett v. Lexington-Fayette Urb.
Cnty. Gov’t, 833 F.3d 590, 610–11 (6th Cir. 2016); see also Bolden v. City of Euclid, 595 F. App’x 464, 468 (6th
Cir. 2014).
 No. 22-3073                          United States v. Loines                              Page 7


1. Plain View Doctrine

       The government argues that the bag with the narcotics was in plain view. This claim has
not been substantiated.

       “Warrantless seizures presumptively violate the Fourth Amendment, but under certain
circumstances an officer may seize evidence in plain view without a warrant.” United States v.
Mathis, 738 F.3d 719, 732 (6th Cir. 2013) (citing Arizona v. Hicks, 480 U.S. 321, 326–27
(1987)). “[O]bjects falling in the plain view of an officer who has a right to be in the position to
have that view are subject to seizure and may be introduced in evidence.” Harris v. United
States, 390 U.S. 234, 236 (1968) (citations omitted). Under the plain view doctrine, four factors
must be satisfied: “(1) the item seized must be in plain view, (2) the item’s incriminating
character must be immediately apparent, (3) the officer must lawfully be in the place from where
the item can be plainly seen, and (4) the officer must have a lawful right of access to the item.”
Mathis, 738 F.3d at 732 (citing Horton v. California, 496 U.S. 128, 136–37 (1990)). Loines
argues that the first three elements of the standard are not met; because the Court finds that the
plain view doctrine does not apply in this case, it does not need to reach a determination as to the
fourth factor, which is not argued by either party.

       a. Plain View

       Officer Kopchak testified that he looked through the red Nissan’s passenger side window
and saw a “bag of dope” in plain view in the car’s center console. To support Kopchak’s
testimony, the government points to the photograph taken from inside the vehicle, body camera
footage, and screenshots taken from the body camera footage. However, Kopchak provides no
testimony or evidence as to what was seen of the small, partially obstructed bag from outside the
vehicle. Instead, he simply asserts that he saw a “bag of dope.” (Tr. of Mot. to Suppress Hr’g,
R. 142, Page ID #731–32).

       For the object to be in plain view, Kopchak’s view of the bag must have been from his
vantage point outside the passenger side window. Moreover, he “must discover incriminating
evidence ‘inadvertently’. . . he may not ‘know in advance the location of [certain] evidence and
 No. 22-3073                          United States v. Loines                                Page 8


intend to seize it,’ relying on the plain view doctrine only as a pretext.” Texas v. Brown, 460
U.S. 730, 737 (1983) (quoting Coolidge v. New Hampshire, 403 U.S. 443, 470 (1971)).

         The government’s evidence purported to establish that the plastic bag was plainly visible
from outside the vehicle is deficient, and instead, leads to the opposite conclusion. First, a
photograph taken inside the vehicle from the vantage point of the driver, is insufficient to
demonstrate the bag was visible from outside the car. The only objective evidence provided by
the government illustrating the view from outside the vehicle are three videos from body camera
footage, and two screenshots from those videos. The body camera videos simply provide the
position of the car and each officer, but do not provide the Court with what Kopchak saw when
observing the inside of the vehicle. The screenshots of the footage are dark, the center console is
barely visible, and there is no clear view into the interior of car through the passenger side
window. The screenshots display no small plastic bag, no lottery ticket, and no cigar wrapper.

         Kopchak’s testimony provides support for the Court’s observation: he states that the
twisted plastic was not apparent in the “still frame . . . but there’s another picture that was taken
of the center console with the bag of dope . . . . packaged . . . in those small plastic bags with the
tie off.” (Tr. of Mot. to Suppress Hr’g, R. 142, Page ID #729, 731). This other picture
referenced in Kopchak’s testimony is the photograph taken during the inventory search from
inside the car. Kopchak did not provide testimony as to what he saw from outside the vehicle,
except for the simple statement that he saw a “bag of dope.” (Tr. of Mot. to Suppress Hr’g, R.
142, Page ID #731–32).

         Accordingly, the only evidence supporting the government’s position is Kopchak’s own
unsupported testimony that he saw a bag of narcotics. Simple statements from the officers
contending that they saw “a bag of narcotics” in the car are not enough to establish that an object
was in plain view when the screenshots that the government presented contradict the officers’
statements. This Circuit recognizes that when evaluating an application of the plain view
doctrine, an officer’s testimony can be “sufficient to establish that the [incriminating evidence]
was visible from outside the car.” United States v. Galaviz, 645 F.3d 347, 356–57 (6th Cir.
2011).    In Galaviz the government provided photographic evidence that the incriminating
evidence was visible from outside the car; however, the photo was taken from inside the car at a
 No. 22-3073                          United States v. Loines                               Page 9


position below the window. Id. The court acknowledged that the photo provided by the
government was insufficient to show that the incriminating evidence was visible from outside the
car, but ultimately found that the testimony provided by the officer was enough to prove the
object was in plain view. Id. However, in Galaviz, no evidence contradicted the officer’s
statement. This case is distinguishable in that the photos provided by the government illustrate
that it was implausible for an individual to view the “bag of dope” from outside the car, thereby
directly contradicting the officer’s testimony. The government offers no plausible explanation as
to how the officers could see the “bag of dope” through the tinted window, but the cameras could
not capture any view into the interior of the car.        Had the photo corroborated Kopchak’s
testimony, Galaviz would apply.

       Kopchak, based on his prior observations of the vehicle at issue, may have had a strong
suspicion about the contents of the car, but without any incriminating evidence being in plain
view from outside of the car, Kopchak did not have lawful access to the contents of the car. See
Brown, 460 U.S. at 737. In sum, from the vantage point of an individual looking through the
passenger side window from outside the vehicle, the plastic bag was not in plain view. We
acknowledge that under the clear error standard, if “the district court’s account of the evidence is
plausible in light of the record viewed in its entirety, the court of appeals may not reverse it even
though [the court may be] convinced that had it been sitting as the trier of fact, it would have
weighed the evidence differently.” Anderson, 470 U.S. at 573–74. But even given the great
deference afforded to the district court under the clear error standard, the photographic evidence
provided by the government does not establish that the “bag of dope” was in plain view. In fact,
the photographs plainly and directly contradict the officer’s testimony.

       We find that the district court’s account of the evidence is not plausible in light of the
record viewed in its entirety. Accordingly, the Court reverses the district court’s holding as to
the denial of Defendant’s motion to suppress.
 No. 22-3073                          United States v. Loines                            Page 10


       b. Incriminating Nature is Immediately Apparent

       The government argues that “the way that the powder was packaged and its proximity to
a folded lottery ticket—commonly used to deliver drugs—made the powder’s incriminating
character obvious.” (Resp’t’s Br., ECF No. 15, 20). We disagree.

       To determine whether an object’s incriminating nature is “immediately apparent,” the
Court looks to four instructive factors:

       (1) a nexus between the seized object and the items particularized in the search
       warrant; (2) whether the ‘intrinsic nature’ or appearance of the seized object gives
       probable cause to believe that it is associated with criminal activity; (3) whether
       the executing officers can at the time of discovery of the object on the facts then
       available to them determine probable cause of the object’s incriminating
       nature; . . . . [and (4) whether the officer can] recognize the incriminating nature
       of an object as a result of his immediate or instantaneous sensory perception.

United States v. Garcia, 496 F.3d 495, 510–11 (6th Cir. 2007) (emphasis in original) (quotations
and citations omitted). “Requiring that evidence be ‘immediate’ and ‘apparent’ constrains the
expansion of the limited search authorized by the warrant into a generalized search, and it
prevents officers from having an opportunity to create a reason to expand the search.” United
States v. McLevain, 310 F.3d 434, 440 (6th Cir. 2002) (quoting United States v. McLernon, 746
F.2d 1098, 1125 (6th Cir. 1984)). In considering whether evidence was “apparent” to the
executing officers, courts “should be duly mindful of the executing officers’ particular,
subjective training and experiences.” United States v. Szymkowiak, 727 F.2d 95, 98 (6th Cir.
1984) (first citing Brown, 460 U.S. at 745–46 (Powell, J., concurring); and then citing United
States v. Cortez, 449 U.S. 411, 418 (1981)); see also United States v. Pacheco, 841 F.3d 384,
395–96 (6th Cir. 2016). Probable cause “merely requires that the facts available to the officer
would ‘warrant a man of reasonable caution in the belief’ . . . that certain items may be
contraband or stolen property or useful as evidence of a crime . . . .” Brown, 460 U.S. at 742
(first quoting Carroll v. United States, 267 U.S. 132, 162 (1925); and then citing Brinegar v.
United States, 338 U.S. 160, 176 (1949)).

       Applying the first factor articulated in Garcia, neither Loines nor the vehicle were subject
to the search warrant in this case.        See Garcia, 496 F.3d at 510 (“Requiring particular
 No. 22-3073                         United States v. Loines                             Page 11


descriptions in search warrants prevents police officers from engaging in general exploratory
searches[.]” (citing Coolidge, 403 U.S. at 465)). Therefore, there is no nexus between Loines’
vehicle, parked away from the house, and the items particularized in the search warrant. Even
though the intention of the warrant was to locate controlled substances, the warrant did not
permit law enforcement to search beyond the geographical location described within. This is
especially true considering the officers had ample opportunity to obtain a valid warrant for the
vehicle. See Garcia, 496 F.3d at 510; Coolidge, 403 U.S. at 465. “An overbroad reading of the
immediately apparent requirement subverts and jeopardizes fundamental Fourth Amendment
principles.” Garcia, 496 F.3d at 510.

       As to the remaining Garcia factors, the government relies on two cases to support its
claim that the bag containing the alleged heroin was “immediately apparent.”             First the
government analogizes to Brown, where an officer conducting a routine driver’s license
checkpoint saw narcotics in plain view after the defendant removed his hand from his pocket to
retrieve his license, and dropped on the floor an “opaque, green party balloon, knotted about one
half inch from the tip.” Brown, 460 U.S. at 733. The officer alleged that his previous experience
making arrests for drug offenses informed him that the dropped substance was a narcotic. Id. at
734. The officer’s knowledge of how narcotics are packaged, and the appearance of the balloon,
without knowledge of the contents, were enough to establish that the officer properly seized the
narcotics under the plain view exception. Id. at 743–44. Second, the government references
Pacheco, where an officer conducting a protective frisk of an individual during a traffic stop felt
a solid “brick-like object protruding approximately one inch out of [the defendant’s] cargo
pocket” and determined that the object was “around six-to-eight inches long.” Pacheco, 841
F.3d at 395. The court found that because the object’s incriminating nature was readily apparent,
the seizure was appropriate under the plain view exception. Id. at 396.

       The government argues that that Kopchak was able to identify the “bag of dope”
immediately as the twisted end of the bag resembled items from earlier in the investigation, and
the lottery ticket’s presence corroborated his belief that the plastic he could see was a bag of
narcotics. Further, the government asserts that given Kopchak’s extensive experience in the
field, and that Kopchak had participated in a controlled buy on April 21, 2020, during which
 No. 22-3073                          United States v. Loines                            Page 12


time Rivers used the vehicle to sell drugs to an informant in a package almost identical to the one
seen in this search, the incriminating nature of the plastic bag was readily apparent.

       However, as discussed above, from the vantage point of the street, or through the
Nissan’s tinted windows, the purported bag of narcotics is not visible. What Kopchak saw of the
plastic bag from outside the vehicle, besides a simple statement that he saw a “bag of dope,” has
not been established on the record. However, assuming Kopchak could see inside the car, he
testifies that he could see a Black and Mild cigar wrapper and a lottery ticket from outside the
vehicle. Neither are “intrinsically incriminating.” McLevain, 310 F.3d at 442–43. Officers are
not authorized to seize items “merely because [they are] in ‘plain view.’” Id. at 441 (emphasis in
original) (quoting McLernon, 746 F.2d at 1125). “[L]awful and innocuous items” cannot be
seized under the plain view exception without an immediately apparent association between the
items and the purported criminal activity. Garcia, 496 F.3d at 511; see also McLernon, 746 F.2d
at 1125 (The officer’s immediate perceptions must produce more than “visual images of . . .
‘intrinsically innocent’ items.” (citations omitted)). Innocuous items that could be used for
criminal activity are not enough to establish probable cause. See United States v. Beal, 810 F.2d
574, 577 (6th Cir. 1987).

       Kopchak does not claim to have seen narcotics or any residue on the lottery ticket, makes
no claim that the cigar wrappers could be contraband, and provides no description of the plastic
bag from outside the vehicle. It was not until the officers entered the vehicle and closely
inspected the center console, that the “bag of dope” was observed to be apparently incriminating.
This close inspection of the inside of the car constituted a further search unsupported by probable
cause. See United States v. Tatman, 397 F. App’x 152, 175 (6th Cir. 2010) (“[W]hen an item
appears suspicious to an officer but further investigation is required to establish probable cause
as to its association with criminal activity, the item is not immediately incriminating.”(quoting
McLevain, 310 F.3d at 443)); see also Beal, 810 F.2d at 577. In Pacheco, the officer felt a solid,
brick-like object that was six to eight inches long, whereas in this case, the purported bag of
narcotics is not seen, or descriptively identified, except for the photograph taken inside the
vehicle. See Pacheco, 841 F.3d at 395–96. Similarly, in Brown, the officer, with the aid of a
flashlight, clearly saw an opaque, green party balloon drop from the defendant’s hand. See
 No. 22-3073                        United States v. Loines                             Page 13


Brown, 460 U.S. at 733–34. In this case, by contrast, the purported bag of narcotics was not
apparent when officers looked into the car from the tinted windows.

       The objects purportedly seen by Kopchak were not immediately and apparently
incriminating. Accordingly, the officers lacked probable cause to search the vehicle. See Beal,
810 F.2d at 578 (“[T]his circuit has vigorously adhered to the requirement that probable cause
must be both immediate and apparent.”).

       c. Legally Present

       Loines argues that Kopchak committed trespass when he cupped his hand or hands
against the Nissan’s tinted windows to see inside Loines’ vehicle, and therefore, Kopchak’s
touching of the car is per se unreasonable under the Fourth Amendment. Because we find that
the objects claimed to be seen by Kopchak were not in plain view, the Court need not determine
whether he was legally permitted to place his hand on the car window to facilitate or enhance his
view of the inside of the car.

2. Automobile Exception

       Under the automobile exception, officers may search a vehicle without a warrant if they
have “probable cause to believe that the vehicle contains evidence of a crime.” United States v.
Smith, 510 F.3d 641, 647 (6th Cir. 2007) (first quoting United States v. Lumpkin, 159 F.3d 983,
986 (6th Cir. 1998); and then citing Smith v. Thornburg, 136 F.3d 1070, 1074 (6th Cir.1998)).
Traditionally, this exception was based on the “ready mobility” of the automobile, which created
“an exigency sufficient to excuse failure to obtain a search warrant once probable cause to
conduct the search [was] clear.” Pennsylvania v. Labron, 518 U.S. 938, 940 (1996) (quoting
California v. Carney, 471 U.S. 386, 390–91 (1985)). More recent cases no longer require that
the automobile exception rest on an independent showing of exigency, because “[e]ven in cases
where an automobile was not immediately mobile, the lesser expectation of privacy resulting
from its use as a readily mobile vehicle justified application of the vehicular exception.” Smith,
510 F.3d at 647 (quoting Carney, 471 U.S. at 391).
 No. 22-3073                         United States v. Loines                          Page 14


       The government argues that Kopchak’s belief that the vehicle contained evidence of a
crime was based on the “bag of dope” seen in plain view.           Therefore, according to the
government’s argument, Kopchak was only legally permitted to search the inside of the vehicle
under the automobile exception if the plain view exception applied. As indicated above, because
the “bag of dope” was not in plain view, there was no probable cause to search the vehicle, and
thus, the government does not properly satisfy the automobile exception.

                                      III. CONCLUSION

       For the reasons set forth above, this Court REVERSES the district court’s denial of
Defendant’s motion to suppress, VACATES his conviction, and REMANDS the case for further
proceedings consistent with this decision.

```

---
