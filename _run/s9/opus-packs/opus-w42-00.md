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

## GROUP: content/cases/United States v. United States District Court (Keith).md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. United States District Court (Keith)"
type: case
citation: "407 U.S. 297 (1972)"
parallel_cite: "92 S. Ct. 2125; 32 L. Ed. 2d 752"
neutral_cite: 1972 U.S. LEXIS 38
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-06-19
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/"
  cluster_id: 108581
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. United States District Court (Keith)"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: Anchor
related:
  - "[[Electronic Surveillance and Title III]]"
  - "[[Katz v. United States]]"
  - "[[Berger v. New York]]"
tags:
  - case
  - fourth-amendment
  - electronic-surveillance
  - national-security
  - warrant-requirement
  - domestic-security
  - title-iii
holding: "The Fourth Amendment requires prior judicial approval before the Government may conduct electronic surveillance of domestic organizations for internal-security purposes; the President's asserted power to protect national security does not exempt warrantless domestic security surveillance from the warrant requirement, and 18 U.S.C. § 2511(3) merely disclaims any intent to define the President's power rather than conferring authority. The holding is limited to domestic threats and does not reach surveillance of foreign powers or their agents."
aliases:
  - "United States v. United States District Court (Keith)"
  - United States v. United States District Court
  - Keith case
  - United States v. U.S. District Court
---

# United States v. United States District Court (Keith)

*407 U.S. 297 (1972)* (No. 70-153) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 108581 → combined opinion 108581 (Powell, J.; 407 U.S. 297, argued Feb. 24, 1972, decided June 19, 1972). Caption disambiguated (worklist): the "Keith" case (after District Judge Damon Keith), a mandamus proceeding styled United States v. United States District Court for the Eastern District of Michigan (Plamondon et al., real parties in interest). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*324`). S9 promotes. -->

## Background
In a federal criminal case charging conspiracy to destroy government property — one defendant, Plamondon, was charged with dynamite-bombing a CIA office in Ann Arbor, Michigan — the defendants moved to compel disclosure of electronic surveillance. The Government produced an affidavit of the Attorney General acknowledging warrantless wiretaps he had approved to gather intelligence to protect the nation from domestic organizations seeking to attack and subvert the structure of the Government, and defended them as a lawful exercise of the President's power to protect national security, conducted without prior judicial approval. District Judge Damon Keith held the surveillance violated the Fourth Amendment and ordered disclosure of Plamondon's overheard conversations. The Government sought a writ of mandamus; the Sixth Circuit held the surveillance unlawful and upheld the disclosure order.

## Issue
Whether the President, acting through the Attorney General, may authorize warrantless electronic surveillance of domestic organizations in the name of internal security, or whether the Fourth Amendment requires prior judicial approval for such surveillance.

## Rule
The Court first read 18 U.S.C. § 2511(3) as a neutral disclaimer — Congress meant only not to legislate on the President's constitutional powers, not to grant any warrantless-surveillance authority. Turning to the Fourth Amendment, it held that the important governmental interest in internal security does not justify departing from the warrant requirement when the target is a domestic threat: "We do hold, however, that prior judicial approval is required for the type of domestic security surveillance involved in this case and that such approval may be made in accordance with such reasonable standards as the Congress may prescribe." — 407 U.S. at 324. ^pin-324

## Application
Even if this particular surveillance might readily have gained judicial approval, the Fourth Amendment does not sustain a search merely because officers acted in good faith and confined themselves to the least intrusive means. Unreviewed executive discretion in domestic security matters risks yielding to pressures to gather evidence and to intrude on privacy and protected First Amendment expression, precisely where the danger of abuse is greatest. Prior judicial approval would neither cripple intelligence gathering nor fracture necessary secrecy, and Congress remained free to fashion standards for domestic security warrants different from Title III's ordinary-crime requirements. The Court pointedly confined its decision to *domestic* organizations, expressing no opinion on surveillance of foreign powers or their agents.

## Conclusion
The judgment of the Court of Appeals for the Sixth Circuit was **affirmed**. Powell, J., delivered the opinion of the Court. Douglas, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; White, J., filed an opinion concurring in the judgment; Burger, C.J., concurred in the result; Rehnquist, J., took no part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. The *Keith* case is the anchor establishing that domestic national-security surveillance requires a warrant, while expressly reserving the foreign-intelligence question — the reservation Congress answered six years later with the Foreign Intelligence Surveillance Act (1978). Teach it against Title III's ordinary-crime scheme (*[[Berger v. New York]]*, *[[Katz v. United States]]*) as the case that closed the "internal security" loophole for domestic threats and set the stage for the foreign-intelligence framework.

## Appears on
- [[Electronic Surveillance and Title III]] — *Anchor*

## Sources
- [*United States v. United States District Court*, 407 U.S. 297 (1972)](https://www.courtlistener.com/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/) — pinpoint: 324 (Powell, J., for the Court; the CL opinion text carries the reporter star `*324` immediately before the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a9c876a6793fe34a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "407 U.S. 297 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 38", "official_citation_present": true, "parallel_cite": "92 S. Ct. 2125; 32 L. Ed. 2d 752", "title": "United States v. United States District Court (Keith)", "year": "1972"}}
{"assertion_id": "4453de9301d0e0dd", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Anchor", "title": "United States v. United States District Court (Keith)"}}
{"assertion_id": "abf8236e114a2bb6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment requires prior judicial approval before the Government may conduct electronic surveillance of domestic organizations for internal-security purposes; the President's asserted power to protect national security does not exempt warrantless domestic security surveillance from the warrant requirement, and 18 U.S.C. § 2511(3) merely disclaims any intent to define the President's power rather than conferring authority. The holding is limited to domestic threats and does not reach surveillance of foreign powers or their agents.", "title": "United States v. United States District Court (Keith)"}}
{"assertion_id": "c51e93cf49f237f5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. United States District Court (Keith)", "varies_by_point": "false"}}
{"assertion_id": "f7c22ec4475a064d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. United States District Court (Keith)"}}
```

### lake record — United States v. United States District Court (Keith)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. United States District Court (Keith)",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. United States District Court for the Eastern District of Michigan",
    "case_name_short": "",
    "case_name_full": "UNITED STATES v. UNITED STATES DISTRICT COURT FOR THE EASTERN DISTRICT OF MICHIGAN Et Al. (PLAMONDON Et Al., REAL PARTIES IN INTEREST)",
    "input_case_name": "United States v. United States District Court (Keith)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-06-19",
    "year": 1972,
    "docket": null,
    "cluster_id": 108581,
    "lead_opinion_id": 9424952,
    "sibling_ids": [],
    "absolute_url": "/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": "caption_mismatch_accepted_by_citation"
  },
  "citations": {
    "official": {
      "cite": "407 U.S. 297",
      "volume": "407",
      "reporter": "U.S.",
      "page": "297",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 2125",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "2125",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 752",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 38",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "407 U.S. 297",
        "volume": "407",
        "reporter": "U.S.",
        "page": "297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 2125",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "2125",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 752",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "752",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 38",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "407 U.S. 297",
    "official_selection": {
      "court_class": "scotus",
      "selected": "407 U.S. 297",
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
    "date_created": "2026-07-06T13:40:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "frontier identity accepted by citation rung despite caption mismatch"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-united-states-district-court-keith--108581",
      "to_record_id": "United States v. United States District Court (Keith)",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. United States District Court (Keith)

```
<opinion type="majority">
<author id="b337-3">Mr. Justice Powell</author>
<p id="AXD">delivered the opinion of the Court.</p>
<p id="b337-4">The issue before us is ah important one for the people of our country and their Government. It involves the delicate question of the President’s power, acting through the Attorney General, to authorize electronic surveillance in internal security matters without prior judicial approval. Successive.Presidents for more, than one-quarter of a century have authorized such surveillance in varying degrees,<footnotemark>1</footnotemark> without guidance from the Congress or a definitive decision of this Court.. This case brings the issue here for the first time. Its resolution is a matter of national concern, requiring sensitivity both to the Government’s right to protect itself from unlawful subversion and attack and to the citizen’s right to be secure in his privacy against unreasonable Government intrusion.</p>
<p id="b337-5">This case arises from a criminal proceeding in the United States District Court for the Eastern District of Michigan, in which the United States charged three defendants with conspiracy to destroy Government property in violation of <span class="citation no-link">18 U. S. C. § 371</span>. One of the defendants, Plamondon, was charged with the dynamite bombing of an office of the Central Intelligence Agency in Ann Arbor, Michigan.</p>
<p id="b337-6">During pretrial proceedings, the defendants moved to compel the United States to disclose certain electronic <page-number citation-index="1" label="300">*300</page-number>surveillance information and to conduct a hearing to determine whether this information “tainted” the evidence on which the indictment was based or which theGovernment intended to offer at trial. In response, the- Government filed an affidavit of the Attorney General, acknowledging that its agents had overheard conversations in which Plamondon had participated. The affidavit also stated that the Attorney General approved the wiretaps “to gather intelligence information deemed necessary to protect the nation from attempts of domestic organizations to attack and subvert the existing structure of the Government.” <footnotemark>2</footnotemark> The logs of the surveillance <page-number citation-index="1" label="301">*301</page-number>were filed in a sealed exhibit for <em>in camera, </em>inspection by the District Court. •</p>
<p id="b339-4">On the basis of the Attorney General’s affidavit and the sealed exhibit, the' Government' asserted that the surveillance was lawful, though conducted without prior judicial approval, as a reasonable exercise of- the President’s power (exercised through the Attorney General) to protect the national security. The District Court held that the surveillance violated the Fourth . Amendment, and ordered the Government to 'make full, disclosure to Plamondon of his overheard conversations. <span class="citation" data-id="2597112"><a href="/opinion/2597112/united-states-v-sinclair/" aria-description="Citation for case: United States v. Sinclair">321 F. Supp. 1074</a></span> (ED Mich. 1971).</p>
<p id="b339-5">The Government then filed in the Court of Appeals for the Sixth Circuit a petition for-a writ of mandamus to set aside the District Court order, which was stayed pending final disposition of the case. ..After- concluding that it had jurisdiction,<footnotemark>3</footnotemark> that ‘court held that the surveillance was unlawful and that the District Court had properly .required disclosure of the overheard conversations, <span class="citation" data-id="9457025"><a href="/opinion/297517/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">444 F. 2d 651</a></span> (1971). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./403/930/">403 U. S. 930</a></span>.</p>
<p id="b339-6">I</p>
<p id="b339-7">Title III of the Omnibus Crime Control and Safe Streets Act, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>, authorizes the use of electronic surveillance for classes of crimes care<page-number citation-index="1" label="302">*302</page-number>fully specified in <span class="citation no-link">18 U. S. C. § 2516</span>. Such surveillance is subject to prior court order. Section 2518 sets forth the detailed and particularized application necessary to obtain such an order as well as carefully circumscribed conditions for its use. The Act represents a comprehensive attempt by Congress to promote more effective control of crime while protecting the privacy of individual thought and expression. Much of Title III was drawn to meet the constitutional requirements for electronic surveillance enunciated by this Court in <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967).</p>
<p id="b340-5">Together with the elaborate surveillance requirements in Title III, there is the following proviso; <span class="citation no-link">18 U. S. C. §2511</span>(3):</p>
<blockquote id="b340-6">“Nothing contained in this chapter or in section 605 of the Communications Act of 1934 (<span class="citation no-link">48 Stat. 1143</span>; 47 U. S. C. 605) shall limit the constitutional power of the President to take such measures as he deems necessary to protect the Nation against actual or potential attack or other hostile acts of a foreign power, to obtain foreign' intelligence information deemed essential to the security of the United States, or to protect national security information against foreign intelligence activities. <em>Nor shall anything contained in this chapter he deemed to limit the constitutional power, of the President to take such measures as he deems necessary to protect the United States against the overthrow of the Government by force or other unlawful means, or against any other clear and present danger to the structure or existence of the Government. </em>The contents of any wire or oral communication intercepted by authority of the President in the exercise of the foregoing powers may be received in evidence in any trial hearing, <page-number citation-index="1" label="303">*303</page-number>or other proceeding only where such interception was reasonable, and shall not be otherwise used or disclosed except as is necessary to implement that power.” (Emphasis supplied.)</blockquote>
<p id="b341-4">The Government relies on § 2511 (3). It argues that “in excepting national security surveillances from the Act’s warrant requirement. Congress recognized the President’s authority to conduct such, surveillances without prior, judicial approval.” Brief for United States 7, 28. The section thus is viewed as a recognition or affirmance of a constitutional authority in the President to conduct warrantless domestic security surveillance such as that involved in this case.</p>
<p id="b341-5">We think the language of § 2511 (3), as well as the legislative history of the statute, refutes this-interpretation. . The relevant language is that:</p>
<blockquote id="b341-6">“Nothing contained in this chapter . . . shall limit the constitutional power of the President to take such measures ás he deems necessary to protect.. .”</blockquote>
<p id="b341-7">against the dangers specified. At most, this is an implicit recognition that the President does have certain powers in the specified areas. Few would doubt this, as the section refers — among other things — to protection “against actual or potential attack or other hostile acts of a foreign power.” But so far as the use of the President’s electronic surveillance power is concerned, the language is essentially neutral.</p>
<p id="b341-8">Section 2511 (3) certainly confers no power, as the language is wholly inappropriate for such a purpose. It merely provides that the Act shall not be interpreted to limit or disturb such power as the President may have under the Constitution. In short, Congress simply left presidential powers where it found thém. This view is reinforced by the general context of Title III. Section 2511 (1) broadly prohibits the use of electronic <page-number citation-index="1" label="304">*304</page-number>surveillance “{ejxcept as otherwise specifically provided in this chapter.” Subsection (2) thereof contains four specific exceptions. In each of the specified exceptions, the statutory language is as follows:</p>
<blockquote id="b342-4">“It shall not be unlawful ... to intercept” the particular type of communication described.<footnotemark>4</footnotemark></blockquote>
<p id="b342-5">The language of subsection (3), here involved, is to be contrasted with the language of the exceptions set forth in the preceding subsection. Rather than stating that warrantless presidential uses of electronic surveillance “shall not be unlawful” and thus employing the standard language of exception, subsection (3) merely disclaims any intention to “limit the constitutional power of the President.”</p>
<p id="b342-6">The express grant of authority to conduct surveil-lances is found in § 2516, which authorizes the Attorney General to make application to a federal judge when surveillance may provide evidence of certain offenses. These offenses are described with meticulous care and specificity.</p>
<p id="b342-7">Where the Act authorizes surveillance, the procedure to be followed is specified in §2518. Subsection (1) thereof requires application to a judge of competent jurisdiction for a prior order of approval, and states in detail the information réquired in such application.<footnotemark>5</footnotemark> <page-number citation-index="1" label="305">*305</page-number>Subsection (3) prescribes the necessary eleménts of probable cause which the .judge must find before issuing an order authorizing an interception. Subsection (4) sets forth the required contents of such an order.. <page-number citation-index="1" label="306">*306</page-number>Subsection (5) sets strict time limits on an order. Provision is made in subsection (7) for “an emergency-situation” found to exist by the Attorney General (or by the principal prosecuting attorney of a State) “with respect to conspiratorial activities threatening the national security interest.” In such a situation, emergency surveillance may be conducted “if an application for an order approving the interception is made . . . within forty-eight hours.” If such an order is not obtained, or the application therefor is denied, the interception is deemed to be a violation of the Act.</p>
<p id="b344-5">In view of these and other interrelated provisions delineating permissible interceptions of particular criminal activity upon carefully specified conditions, it would have been incongruous for Congress to have legislated with respect to the important and complex area of national security in a single brief and nebulous paragraph. This would not comport with the sensitivity of the problem involved or with the extraordinary care Congress exercised in drafting other sections of the Act. We therefore think the conclusion inescapable that Congress only intended to make clear that the Act simply did not legislate with respect to national security surveillances.<footnotemark>6</footnotemark></p>
<p id="b344-6">The legislative history of §2511(3) supports this interpretation. Most relevant is the colloquy between Senators Hart, Holland, and McClellan on the Senate floor:</p>
<blockquote id="b344-7">“Mr.'HOLLAND. . .. The section [2511(3)] from which the Senator [Hart] has read does not affirma<page-number citation-index="1" label="307">*307</page-number>tively give any power. ... <em>We are not affirmatively conferring any power upon the President. </em>We are simply saying that nothing herein shall limit such power as the President has under the Constitution. . . . We certainly do not grant him a thing.</blockquote>
<blockquote id="b345-4">“There is nothing affirmative in this statement.</blockquote>
<blockquote id="b345-5">“Mr. McCLELLAN. Mr. President, <em>we make it understood that we are not trying to take anything away from-him.</em></blockquote>
<blockquote id="b345-6">“Mr. HOLLAND. The Senator is correct.</blockquote>
<blockquote id="b345-7">“Mr. HART. Mr. President, there is no intention • here to expand by this language a constitutional power. Clearly we could not do so.</blockquote>
<blockquote id="b345-8">“Mr. McCLELLAN. Even though intended, we could not do so.</blockquote>
<blockquote id="b345-9">“Mr. HART. . . . However, we are agreed that this language should not be regarded as intending to grant any authority, including authority to put a bug on, that the President does not have now.</blockquote>
<blockquote id="b345-10">“In addition, Mr. President, <em>as I think our exchange makes clear, nothing in section 2511 (3) even attempts to define the limits of the. President’s national security power under present law, which I have always found extremely vague </em>.... <em>.Section </em>2511(8) <em>'merely says that if the President has such a power, then its exercise is in no way affected by title III.” </em><footnotemark><em>7</em></footnotemark><em> </em>(Emphasis supplied.)</blockquote>
<p id="b346-4"><page-number citation-index="1" label="308">*308</page-number>One could hardly expect a clearer expression of congressional neutrality. The debate above explicitly indicates that nothing in § 2511 (3) was intended to <em>expand </em>or to <em>contract </em>or to <em>define </em>whatever presidential surveillance powers existed in matters affecting the national security. If we could accept the Government's characterization of § 2511 (3) as a congressionally prescribed exception to the general requirement of a warrant, it would be necessary to consider the question of whether the surveillance in this casé came within the exception and, if so, whether the statutory exception was itself constitutionally valid. But viewing § 2511 (3) as a congressional' disclaimer and expression of neutrality, we hold that the statute is not the measure of the executive authority asserted in this case. Rather, we must look to the constitutional powers of the President.</p>
<p id="b346-5">II</p>
<p id="b346-6">It is important at the outset to emphasize the limited nature of the question before the Court. This case raises- no constitutional challenge to electronic surveillance as specifically authorized by Title III of the Omnibus Crime Control and Safe Streets Act of 1968. Nor. is there any question or doubt as to the necessity of obtaining a warrant in the surveillance of crimes unrelated to the national security interest. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). Further, the instant case requires no judgment on the scope of the President's surveillance power with respect to the activities of foreign powers, within or without this country. The Attorney General’s affidavit in this case states that, the surveillances were <page-number citation-index="1" label="309">*309</page-number>“deemed, necessary to protect the nation from attempts of <em>domestic organizations </em>to attack and subvert the existing structure of Government” (emphasis supplied). There -is no evidence of any involvement, directly or indirectly, of a foreign power.<footnotemark>8</footnotemark></p>
<p id="b347-4">Our present inquiry, though important, is therefore a narrow one. It addresses a question left open by. <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz, supra,</a></span> </em>at 358 n. 23:</p>
<blockquote id="b347-5">“Whether safeguards othér than prior authorization by- a magistrate would satisfy the Fourth Amendment in a situation involving the national-security . . 7 .”</blockquote>
<p id="b347-6">The determination of this question requires the essential Fourth .Amendment inquiry into .the “reasonableness” of the search and seizure in question, and the way in which that “reasonableness” derives content and mean<page-number citation-index="1" label="310">*310</page-number>ing through reference to the warrant ulause. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#473" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 473-84</a></span> (1971).</p>
<p id="b348-5">We begin the inquiry by noting that the President of the United States has the fundamental duty, under Art. II, § 1, of the Constitution, to “preserve, protect and defend the Constitution of the United States.” Implicit in that duty is the power to protect our Government against those who. would subvert or overthrow it by unlawful means. In the discharge of this duty, the President — through the Attorney General— may find it necessary to employ electronic surveillance to obtain intelligence information on the plans of those who plot unlawful acts against the Government.<footnotemark>9</footnotemark> The use of such surveillance in internal security cases has been sanctioned more or less continuously by various Presidents and Attorneys General since July 1946.<footnotemark>10</footnotemark> <page-number citation-index="1" label="311">*311</page-number>Herbert Brownell, Attorney General under President Eisenhower, urged the use of electronic surveillance both in internal and international security matters on the grounds that those acting against the Government</p>
<blockquote id="b349-4">“turn to the telephone to carry on their intrigue. The success of their plans frequently rests upon piecing together shreds of information received from many sources and many- nests. The participants in the conspiracy are often dispersed and stationed in various strategic positions in government and industry throughout the country.”<footnotemark>11</footnotemark></blockquote>
<p id="b349-5">Though the Government and respondents debate their seriousness and magnitude, threats and acts of sabotage against the Government exist in sufficent number to justify investigative powers with respect to them.<footnotemark>12</footnotemark> The covertness and complexity of potential unlawful con<page-number citation-index="1" label="312">*312</page-number>duct against the Government and the necessary dependency of many conspirators upon the telephone make electronic surveillance an effective investigatory instrument in certain circumstances. The marked acceleration in technological developments and sophistication in their use have resulted in new techniques for the planning, commission, and concealment of criminal activities. It would be contrary to the public interest for Government to deny to itself the prudent and lawful employment of those very techniques which are employed against the Government and its law-abiding citizens.</p>
<p id="b350-5">It has been said that “[t]he most basic' function of any government is to provide for the security of the individual and of his property.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#539" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 539</a></span> (1966) (White, J., dissenting). And unless Government safeguards its own capacity to function and to preserve the security of its people, society itself could become so disordered that all rights' and liberties would be endangered. As Chief Justice Hughes reminded us in <em>Cox </em>v. <em>New Hampshire, </em><span class="citation" data-id="103490"><a href="/opinion/103490/cox-v-new-hampshire/#574" aria-description="Citation for case: Cox v. New Hampshire">312 U. S. 569, 574</a></span> (1941):</p>
<blockquote id="b350-6">“Civil liberties, as guaranteed by the Constitution, imply the existence of an organized society maintaining public order without which liberty itself would be lost in the excesses of unrestrained' abuses.”</blockquote>
<p id="b350-7">But a recognition of these elementary truths does not make the employment by Government of electronic surveillance a welcome development — even when employed with restraint' and under judicial supervision. There is, understandably, a deep-seated uneasiness and apprehension that this capability will be used to intrude upon cherished privacy of law-abiding citizens.<footnotemark>13</footnotemark> We <page-number citation-index="1" label="313">*313</page-number>look to the Bill of Rights to safeguard this privacy. Though physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed, its broader spirit, now shields private speech from unreasonable surveillance. <em>Katz </em>v. <em>United States, supra; Berger </em>v. <em>New <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">York, supra;</a></span> Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961). Our decision in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>refused to lock the Fourth Amendment into • instances of actual physical trespass. Rather, the Amendment governs “not only the seizure of tangible items, but extends'as well to the recording of oral statements . . . without any ‘technical trespass under . . . local property law.’ ” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 353</a></span>. That decision implicitly recognized that the broad and unsuspected governmental incursions into conversational privacy which electronic surveillance entails<footnotemark>14</footnotemark> necessitate the application of Fourth Amendment safeguards.</p>
<p id="b351-4">National security cases, moreover, often reflect a convergence of First and Fourth Amendment values not present in cases of “ordinary” crime. Though the investigative duty of the executive may be stronger in such cases, so also is there greater jeopardy to constitutionally protected speech. “Historically the struggle for freedom of speech and press in England was bound up with the issue of the scope of the search and seizure <page-number citation-index="1" label="314">*314</page-number>power,” <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724</a></span> (1961). History abundantly documents the tendency of Government — however benevolent and benign its motives — to view with suspicion those who most fervently dispute its policies. Fourth Amendment protections become the more necessary when the targets of official surveillance may be those suspected of unorthodoxy in their political beliefs. The danger to political dissent is acute where the Government attempts to act under so vague a concept as the power to protect “domestic security.” Given the difficulty of defining the domestic security, interest, the danger of abuse in acting to protect that interest becomes apparent. Senator Hart addressed this dilemma in the floor debate on § 2511 (3):</p>
<blockquote id="b352-4">“As I read it — and this is my fear — we are saying that the President, on his motion, could declare— name your favorite poison — draft dodgers, Black Muslims, the Ku Klux Klan, or civil rights activists to be a clear and present danger to. the structure or existence of the Government.” <footnotemark>15</footnotemark></blockquote>
<p id="b352-5">The price of lawful public dissent must not be a dread of subjection to an unchecked surveillance power. Nor must the fear of unauthorized official eavesdropping deter vigorous citizen.dissent and discussion of Government action in private conversation. For private dissent, no less than open public discourse, is essential to our free society.</p>
<p id="b352-6">Ill</p>
<p id="b352-7">As the Fourth Amendment is not absolute in its terms, our task is to examine and balance the basic values at stake in this case: the duty of Government <page-number citation-index="1" label="315">*315</page-number>to protect the domestic security, and the potential danger posed by unreasonable surveillance to individual privacy and free expression. If the legitimate need of Government to. safeguard domestic security requires the use of electronic surveillance, the question is whether the needs of citizens for privacy and free expression may not be better protected by requiring a warrant before such surveillance, is undertaken; We must also ask whether a warrant requirement would unduly frustrate; the. efforts of Government to protect itself from acts of subversion and overthrow, directed against it.</p>
<p id="b353-4">Though the Fourth Amendment speaks broadly of ‘unreasonable searches and seizures,” the definition of “reasonableness”' turns, at least in part, on the more specific commands of the warrant clarise. Some have argued that “[t]he relevant'.test is hot whether it is reasonable to procure á search warrant, but whethér the search was reasonable,”. <em>United States </em>v. <em>Rabinowitz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./330/56/">330 U. S. 56</a></span>, 66 (1950).<footnotemark>16</footnotemark> This view, however, overlooks the second clause of the Amendment. The warrant clause of the Fourth Amendment is not dead language. Rather, it has been.</p>
<blockquote id="AJB">“a valued part of our constitutional law for decades, and it has determined the result in scores and scores' of cases in courts all over this country. It is riot an inconvenience to be somehow ‘weighed’ against the claims of, police efficiency. It is, or should <page-number citation-index="1" label="316">*316</page-number>-be,- an- important working part of our machinery of government, operating as a matter of course to check the - ‘well-intentioned but mistakenly overzealous executive officers’. who are a part of any system of law enforcement.” <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#481" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 481</a></span>.</blockquote>
<p id="b354-4">See also <em>United States </em>v. <em>Rabinowitz, supra, </em>at 68 (Frankfurter, J.,, <em>dissenting); Davis </em>y. <em>United States, </em><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#604" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 604</a></span> (1946) (Frankfurter, J., dissenting):</p>
<p id="b354-5">Over two centuries ago, Lord Mansfield held that common-law principles prohibited warrants that ordered the' arrest of unnamed individuals who the. <em>officer </em>might conclude were guilty, of seditious libel. “It is not fit,” . said Mansfield, “that the receiving. oi- judging of the. information should be left to the discretion of . the. officer. The magistrate ought to . judge;’ and should . give certain directions to the officer.” <em>Leach </em>v. <em>Three of the King’s Messengers, </em>19 How. St. Tr. 1001, 1027 (1765).</p>
<p id="b354-6">• Lord Mansfield’s formulation touches' the very heart of the Fourth Amendment directive: that, where practical, a governmental search,and seizure should repre- ' sent both the efforts of the officer to gather evidence of .wrongful acts and the judgment of the magistrate that the collected evidence is sufficient to justify invasion of a citizen’s private premises or conversation.' Inherent in the concept of a warrant is its issúance by a “neutral and detached, magistrate.” <em>Coolidge </em>v. <em>New Hampshire, supra, </em>at 453; <em>Katz </em>v. <em>United States, supra, </em>at 356. The further requirement of “probable cause” instructs the magistrate that baseless searches shall not proceed.</p>
<p id="b354-7">These Fourth Amendment freedoms cannot properly be guaranteed if domestic security surveillances may be' conducted solely .within the discretion of the Execu<page-number citation-index="1" label="317">*317</page-number>tive Branch. The Fourth Amendment does not contemplate the executive officers of .Government as neutral and disinterested magistrates. . Their duty and responsibility are to enforce the- laws, to investigate, and to prosecute. <em>Katz </em>v. <em>United States, supra, </em>at 359-360 (Douglas, J., concurring). But those charged with this investigative and prosecutorial duty should not be the sole judges of when to utilize constitutionally sensitive means in pursuing their tasks. The historical judgment, which the Fourth Amendment accepts, is that unreviewed executive discretion may yield too. readily to pressures to-obtain incriminating evidence and overlook potential invasions of privacy and protected speech.<footnotemark>17</footnotemark></p>
<p id="b355-4">It may well be that, in the instant case, the Government’s surveillance of Plamondon’s conversations was a reasonable one which readily would have gained prior judicial approval. But this Court “has never sustained a search upon the sole ground that officers reasonably expected to .find evidence of a particular crime and voluntarily confined their activities, to the least intru-. sive means consistent with that end.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 356-35</a></span>.7. The Fourth Amendment contemplates a prior judicial judgment,<footnotemark>18</footnotemark> not the risk that executive discretion may be reasonably exercised. This judicial role accords with our basic constitutional doctrine that individual freedoms will best be preserved through . a separation of powers and division of functions among the different branches and levels of Government. Harlan, Thoughts at a Dedication: Keeping the Judicial Function in Balance, 49 A. B. A. J. 943-944 (1963). The independent check upon executive discretion.is not <page-number citation-index="1" label="318">*318</page-number>satisfied, as the Government' argues, by “extremely limited” post-surveillance judicial review.<footnotemark>19</footnotemark> Indeed, post-surveillance review would never reach the- surveillances which failed to result in prosecutions. Prior review by a neutral and detached' magistrate is the time-tested means of effectuating Fourth Amendment rights. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964).</p>
<p id="b356-5">It is true that there have been some exceptions to the warrant requirement. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). But those exceptions are few in number and carefully delineated, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States"><em>Katz, supra, </em>at 357</a></span>; in general, they serve the legitimate needs of law enforcement officers to protect their own well-being and preserve evidence from destruction. Even while carving out those exceptions, the Court has reaffirmed the principle that the “police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure,” <em>Terry </em>v. <em>Ohio, supra, </em>at 20; <em>Chimel </em>v. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California"><em>California, supra, </em>at 762</a></span>.</p>
<p id="b356-6">The Government argues that the special circumstances applicable to domestic, security, surveillances necessitate a further exception to the warrant requirement. It is urged that the requirement of prior judicial review would obstruct the President in the discharge of his constitutional duty to protect domestic, security. We are told further that these surveillances • are. directed- primarily to the collecting and maintaining of intelligence with <page-number citation-index="1" label="319">*319</page-number>respect to subversive forces/ and are not an attempt to gather evidence for specific criminal prosecutions. It is said that this type of surveillance should not be subject to traditional warrant requirements which were established to govern investigation' of criminal activity, not ongoing intelligence gathering. Brief for United States 15-16, 23-24; Reply Brief for United States 2-3.</p>
<p id="b357-4">The Government further insists that courts “as a practical matter would have neither-the knowledge nor the techniques necessary to determine whether there was probable cause to believe that surveillance was necessary to protect national security.”. These security problems, the Government contends, involve “a large number of complex and subtle factors” beyond the competence of courts to evaluate. Reply Brief for United States 4.</p>
<p id="b357-5">As a final reason for exemption from a warrant requirement, the Government believes that disclosure to a magistrate of all or even a significant portion of the information' involved in domestic security surveillances “would create serious potential dangers to -the national security and to the lives of informants and agents., . . .' Secrecy is the essential ingredient in intelligence gathering; requiring prior judicial authorization would create a greater 'danger of leaks . . . , because in addition to the judge, you have the clerk,-.the stenographer and some other officer like a law assistant or bailiff who may be apprised of the nature’ of the surveillance-.” Brief for United States 24-25:</p>
<p id="b357-6">These contentions in behalf .of a complete exemption from the warrant requirement, when urged on behalf of the President and the national security in -its domestic implications', merit the most careful consideration. We •certainly do not reject them lightly, especially at a time of worldwide ferment and when civil disorders in this country are more prevalent than iñ the less turbulent <page-number citation-index="1" label="320">*320</page-number>periods of our history.' There is, no doubt, pragmatic force to the Government’s position.</p>
<p id="b358-4">But we do not think a case has been made for the requested departure from Fourth Amendment standards. The circumstances, described do not justify complete exemption of domestic security surveillance from prior judicial scrutiny. Official surveillance, whether its purpose be criminal investigation or ongoing intelligence gathering, risks infringement of constitutionally protected privacy of speech. Security surveillances are especially sensitive because of the inherent vagueness of the domestic security concept, the necessarily broad and continuing nature of intelligence gathering, and the temptation to utilize such surveillances to oversee political dissent. <em>We </em>recognize, as we have before, the constitutional basis, of the President’s domestic security role, but we think it must be exercised in a manner compatible with the Fourth Amendment. In this case w;e hold that this requires an appropriate prior warrant procedure.</p>
<p id="b358-5">We cannot accept the Government’s argument that internal security matters are too. subtle and complex for judicial evaluation. Courts regularly deal with the most difficult issues of our society. There is no reason to believe that federal judges will be insensitive to or uncomprehending of the issues involved in domestic security cases. Certainly courts can recognize, that domestic security surveillance involves-different considerations from the surveillance of “ordinary crime.” If the threat is too subtle or complex for our senior law enforcement officers to convey its significance to a court, one may question whether there is probable cause for surveillance.</p>
<p id="Aso">Nor do we believe prior judicial approval will fracture the secrecy essential to official intelligence gathering. The- investigation 'of criminal activity has long <page-number citation-index="1" label="321">*321</page-number>involved imparting , sensitive information to judicial officers who have respected the confidentialities involved. Judges may be counted upon to. be especially conscious of security requirements in national security cases. Titie III of the Omnibus Crime Control and Safe Streets Act already has imposed this responsibility on the judiciary in connection with such crimes as espionage, sabotage, and treason, .§§ 2516 (l.)(a) and (c), each of which may involve domestic as well as foreign security threats. Moreover, a warrant application involves no public or adversary proceedings: it is an <em>ex parte </em>request before a. magistrate or judge; Whatever security dangers clerical and secretarial personnel may pose can be minimized by proper administrative measures, possibly to the point of allowing the Government itself to provide the necessary clerical assistance.</p>
<p id="b359-2">Thus, we conclude that the Government’s concerns do not justify departure in this case from the customary Fourth Amendment requirement of judicial approval prior to initiation of a search or surveillance. Although some added burden will be imposed upon the Attorney General, this inconvenience is justified in a free society to protect constitutional values. Nor do we think the Government’s domestic surveillance powers will be impaired to any significant degree. A prior warrant establishes presumptive validity of the surveillance and will minimize the burden of justification in post-surveillance judicial review. By no means of least importance will be the reassurance of the public generally that indiscriminate wiretapping and bugging of law-abiding citizens cannot occur.</p>
<p id="b359-3">IV</p>
<p id="b359-4">We emphasize, before concluding this opinion, the scope of our decision. As stated at the outset, this case involves only the domestic aspects of national security. We have not addressed, and express no opinion <page-number citation-index="1" label="322">*322</page-number>as to, the issues which may be involved with respect to activities of foreign powers or their agents.<footnotemark>20</footnotemark> Nor does our decision rest on thé langi^age of § 2511 (3) or any other section of Title III of the Omnibus Crime Control and Safe Streets Act of 1968. That Act does not attempt to define or delineate the powers of the President to meet domestic threats to the national security.</p>
<p id="b360-4">Moreover, we do not hold that the same type of standards and procedures prescribed by Title III are necessarily applicable to this case. , We recognize that domestic security surveillance may involve different policy and practical considerations from the surveillance of “ordinary crime.” The gathering of security intelligence is often long range and involves the interrelation of various sources and types of information. The exact targets of such surveillance may be more difficult to identify than in surveillance operations against many types of crime specified in Title III. Often, too, the emphasis of domestic intelligence gathering is on the prevention of unlawful activity or the enhancement of the Government’s preparedness for some possible future crisis or emergency. Thus, the focus of domestic surveillance may be less precise than that directed against more conventional types of crime.</p>
<p id="b360-5">Given these potential distinctions between Title III criminal surveillances and those involving the domestic security, Congress may wish to. consider protective standards for the latter , which differ from those already prescribed for specified crimes in Title III. Different standards may be compatible with the Fourth Amend<page-number citation-index="1" label="323">*323</page-number>ment if they are reasonable both in relation to the legitimate need of Government for intelligence information and the protected rights of our citizens. For the warrant application may vary according to the governmental interest to be enforced and the nature of citizen rights deserving protection. As the 'Court said in <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535</a></span> (1967):</p>
<blockquote id="b361-4">“In cases in which the Fourth Amendment requires that a warrant to search be. obtained, ‘probable cause’ is the standard by which a particular decision -to search is tested against the constitutional mandate of reasonableness. . . . In determining whether a particular inspection is reasonable — -and thus in determining whether there is probable cause to issue a warrant for that inspection — the need for. the inspection must be weighed in terms of these reasonable goals of code enforcement.”</blockquote>
<p id="AL7">It may be that’ Congress, for example, would judge that the application and affidavit showing probable cause need. not follow the exact requirements of § 2518 but should allege other circumstances more appropriate to domestic security cases; that the request for prior court •authorization could, in sensitive cases, be made to. any member of a specially designated court (e. <em>g., </em>the District Court for the District of Columbia or the Court of Appeals for the District of Columbia Circuit); and that the time and reporting requirements need not be so strict as those in § 2518. ■</p>
<p id="b361-6">The above paragraph does not, -of course, attempt to guide the congressional judgment but rather to delineate the present scope of our own opinion. We do not attempt to detail the precise standards for domestic secu-. rity warrants any more than our decision in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>sought to set the refined requirements for the specified criminal surveillances which now constitute Title III. We do <page-number citation-index="1" label="324">*324</page-number>hold, however, that prior judicial approval is required for the type .of domestic security surveillance involved in this case and that such approval may be made in accordance with such reasonable standards as the Congress may prescribe.</p>
<p id="b362-4">V</p>
<p id="b362-5">As the surveillance of Plamondon’s conversations was unlawful, because conducted without prior judicial approval, the courts below correctly held that <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969), is controlling and that it requires disclosure to the accused of his own im-permissibly intercepted conversations. As stated in <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span>, </em>“the trial court .can and should, where appropriate, place a defendant and his counsel under enforceable orders against unwarranted disclosure of thé materials which they may be entitled to inspect.” <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#185" aria-description="Citation for case: Alderman v. United States">394 U. S., at 185</a></span>.<footnotemark>21</footnotemark></p>
<p id="b362-6">The judgment of the Court of Appeals is hereby</p>
<p id="b362-7">
<em>Affirmed.</em>
</p>
<judges id="b362-8">The Chief Justice concurs in the result.</judges>
<judges id="b362-9">Mr, Justice Rehnquist took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b337-7"> See n. 10, <em>infra.</em></p>
</footnote>
<footnote label="2">
<p id="b338-5"> The Attorney General’s affidavit reads as follows:</p>
<blockquote id="b338-6">“JohN N. Mitchell being duly sworn deposes and says:</blockquote>
<blockquote id="b338-7">“1. I ani the Attorney General of the United States.</blockquote>
<blockquote id="b338-8">“2. This affidavit is submitted in connection with the Government’s opposition to the disclosure to the defendant Plamondon of information concerning the overhearing of his conversations which occurred during the course of eléctronic surveillances which the Government contends were legal.</blockquote>
<blockquote id="b338-9">“3. The defendant Plamondon has participated in conversations which were overheard by Government agents who were monitoring wiretaps' which were being employed to gather intelligence information deemed necessary to protect the nation from attempts of domestic organizations to attack and subvert the existing structure of the Government. The records of the Department of Justice. reflect the installation of these' wiretaps had been expressly approved by the Attorney General. '</blockquote>
<blockquote id="b338-10">“4. Submitted with this affidavit is a sealed exhibit containing the records of the intercepted conversations, a description of the premises that were the subjects of surveillances, and copies of the memoranda reflecting the Attorney General’s express approval of the installation of the surveillances.</blockquote>
<blockquote id="b338-11"><em>“5. </em>I certify that it would prejudice the national interest to disclose the particular facts concerning these surveillances other than to the court <em>in camera. </em>Accordingly, the sealed exhibit referred to herein is being submitted solely for the court’s <em>in camera </em>inspection and a copy of the sealed exhibit is not being furnished to the defendants. I would request, the court, at the conclusion of its <page-number citation-index="1" label="301">*301</page-number>hearing on this matter,- to place the sealed exhibit in a sealed envelope and return it to the Department of Justice where it will be retained under seal so that it may be submitted to any appellate court that may review this matter.”</blockquote>
</footnote>
<footnote label="3">
<p id="b339-10"> Jurisdiction was challenged before the Court of Appeals on the ground that the District Court’s order was interlocutory and not appealable under <span class="citation no-link">28 U. S. C. § 1291</span>. On this issue, the court correctly held that it did have jurisdiction, relying upon the All Writs Act, <span class="citation no-link">28 U. S. C. § 1651</span>, and cases cited in its opinion, <span class="citation" data-id="9457025"><a href="/opinion/297517/united-states-v-united-states-district-court-for-the-eastern-district-of/#655" aria-description="Citation for case: United States v. United States District Court for the...">444 F. 2d, at 655-656</a></span>. No attack was made in this Court as to the appropriateness of the writ of mandamus procedure.</p>
</footnote>
<footnote label="4">
<p id="b342-8"> These exceptions relate to certain activities of communication common carriers and the Federal Communications Commission, and to specified situations where a party to the communication has consented to the interception.</p>
</footnote>
<footnote label="5">
<p id="b342-9"> Title <span class="citation no-link">18 U. S. C. §2518</span>, subsection (1), reads as follows:</p>
<blockquote id="b342-10">“§ 2518. Procedure for interception of wire or oral communications “(1) Each application for an order authorizing or approving the interception of a wire or oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction <page-number citation-index="1" label="305">*305</page-number>and shall state the applicant’s authority to' make such application. Each application shall include the following information:</blockquote>
<blockquote id="AIzg">“(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</blockquote>
<blockquote id="AK2">“(b) a full and complete statement of the facts and circumstances relied upon by the applicant, to jústify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about to be committed,' (ii) a particular description of the nature and location of the facilities from which or the place where the communication is to be intercepted, (in) a particular description of the type of communications sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications áre to be intercepted;</blockquote>
<blockquote id="Asl">“(c) a full and complete statement as to whether or not other investigative procedures have been tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be too dangerous;</blockquote>
<blockquote id="AY4">“(d) a statement of the period of time for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause' to believe that additional communications of the same type will occur thereafter;.</blockquote>
<blockquote id="AnP">“(e) a full .and complete statement of the .facts concerning all previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of the same persons, facilities or places specified in the application, and the action taken by the judge, on each such application; and</blockquote>
<blockquote id="AUl">“(f) where the application .is for the extension- of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results.”</blockquote>
</footnote>
<footnote label="6">
<p id="b344-8"> The final sentence of § 2511 (3) states that the contents of an interception “by authority of the; President in the exercise of the foregoing powers may be received in evidence . . . only where such interception was reasonable . . . This sentence seems intended to assure that when the President conducts lawful surveillance— pursuant to whatever power he may possess — the evidence is admissible.</p>
</footnote>
<footnote label="7">
<p id="b345-12"> 114 Cong. Rec. 14751. Senator McClellan was the sponsor of the bill.. The above exchange constitutes the only time that § 2511 (3) was expressly debated on the Senate or House floor. The Report of the Senate Judiciary Committee is not so explicit as the exchange •on the floor, but it appears to recognize that under. § 2511 (3) the • national security power of the President — whatever it may be — “is not to be deemed disturbed.” S. Rep. No. 109.7, 90th Cong., 2d Sess., 94 (1968). See also The “National Security Wiretap”: Presidential Prerogative or Judicial Responsibility, where the author concludes that in § 2511 (3) “Congress took what amounted to a position of <page-number citation-index="1" label="308">*308</page-number>neutral noninterference on the question of the constitutionality of warrantless national security wiretaps authorized by the President.” <span class="citation no-link">45 S. Cal. L. Rev. 888</span>, 889 (1972).</p>
</footnote>
<footnote label="8">
<p id="b347-7"> Section 2511 (3) refers to “the constitutional power of the President” in two types of situations: (i) where necessary to protect against attack, other hostile acts or intelligence activities of a “foreign power”; or (ii) where necessary to protect against the overthrow of the' Government or other clear and present danger to the structure or existence of the Government. Although both of the specified situations are sometimes referred to as “national security” threats, the term “national security”- is used only in the first sentence of § 2511 (3) with respect to the activities of foreign powers. This case involves only the second sentence of §2511 (3), with' the threat emanating — according to the Attorney General’s affidavit — from “domestic organizations.” Although we attempt no precise definition, we use the term “domestic organization” in this opinion to mean a group or organization (whether formally or informally constituted) composed of citizens of the United States and which has no significant connection with a foreign power, its agents or agencies. No doubt there are cases where it will be difficult to distinguish between “domestic” and “foreign” unlawful activities directed against the Government of the United States where there is collaboration in varying degrees between domestic groups or organizations and agents or agencies of foreign powers. But this is not such a case.</p>
</footnote>
<footnote label="9">
<p id="b348-6"> Enactment of Title III reflects congressional recognition of the importance of such surveillance in combatting various types of crime. Frank S. Hogan, District Attorney for New York County for over 25 years, described telephonic interception, pursuant to court order, as “the single , most valuable weapon in law enforcement’s fight against organized crime.” 117 Cong. Rec. 14051. The “Crime Commission” appointed by President Johnson noted that “[t]he .great majority of law enforcement officials .believe that the evidence necessary to bring criminal sanctions to bear consistently on the higher echelons of organized crime will not be obtained without the aid of electronic surveillance techniques. They maintain these techniques are indispensable to develop adequate strategic intelligence concerning organized crime, to set up specific investigations, to.develop witnesses, to corroborate their testimony, and to serve as substitutes for them — each a necessary step in the evidence-gathering process'in organized crime investigations and prosecutions.” Report by the President’s Commission on Law Enforcement and Administration of Justice, The Challenge of Crime in a Free Society 201 (1967).</p>
</footnote>
<footnote label="10">
<p id="b348-7"> In that month Attorney General Tom Clark advised President Truman of the necessity of using wiretaps “in cases vitally affecting the domestic security.” In May 1940 President Roosevelt had au<page-number citation-index="1" label="311">*311</page-number>thorized Attorney General Jackson to utilize wiretapping in matters “involving the defense of the nation,” but it is questionable whether this language was meant to apply to solely domestic subversion. The nature and extent of wiretapping apparently varied under different administrations and Attorneys General, but, except for the sharp curtailment under Attorney General Ramsey Clark in the latter years of the Johnson administration, electronic surveillance has been used both against organized crime and in domestic security cases at least since .the 1946 memorandum from Clark to Truman. Brief for United States 16-18; Brief for Respondents 51-56; 117 Cong. Rec. 14056.</p>
</footnote>
<footnote label="11">
<p id="b349-7"> Brownell, The Public Security and Wire Tapping, 39 Cornell L. Q. 195, 202 (1954). See also Rogers, The Case For Wire Tapping, 63 Yale L. J. 792 (1954). •</p>
</footnote>
<footnote label="12">
<p id="b349-9"> The Government asserts that there , were 1,562 bombing incidents in the United States from January 1, 1971,’ to July 1, 1971, most of-which involved Government related facilities. Respondents dispute these statistics as incorporating many frivolous incidents as well as bombings against nongovernmental facilities. The precise level of this activity, however, is not relevant to the disposition of this case. Brief for United States 18; Brief for Respondents 26-29; Reply Brief for United States 13.</p>
</footnote>
<footnote label="13">
<p id="AV6"> Professor Alan Westin has written on. the likely course of future conflict between the value of privacy and the “new technology” of law enforcement. Much of the book details techniques <page-number citation-index="1" label="313">*313</page-number>of physical and electronic surveillance and such possible- threats to personal privacy as psychological and personality testing and electronic information storage and retrieval. Not all of the contemporary threats to privacy emanate directly from the pressures of crime control. Privacy and Freedom (1967).</p>
</footnote>
<footnote label="14">
<p id="Axn"> Though the total number of intercepts authorized by. state and federal judges pursuant to Tit. Ill of the. 1968 Omnibus Crime Control and Safe Streets Act was 597 in 1970, éaeh surveillance may involve interception of hundreds of different conversations. The average intercept in 1970 involved 44 people and 655 conversations, of which 295 or 45% were incriminating. 117 Cong. Rec. 14052.</p>
</footnote>
<footnote label="15">
<p id="b352-8"> 114 Cong. Rec. 14750. The subsequent, assurances, quoted in part I of the opinion, that §2511 (3) implied no statutory grant, contraction, or definition of presidential power eased the Senator’s misgivings.</p>
</footnote>
<footnote label="16">
<p id="b353-7"> This view has not been accepted.' ’ In <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), the Court considered the Government’s contention that the search be judged on a general “reasonableness” standard without reference to the warrant clause. .The Court concluded that argument was “founded on little more than a subjective view regarding the acceptability of certain, sorts of police conduct, and not on considerations relevant to Fourth Amendment interests. Under such, an unconfined analysis, Fourth Amendment protection in this area would approach the evaporation point.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#764" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 764-765</a></span>.</p>
</footnote>
<footnote label="17">
<p id="b355-5"> N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 79-105 (1937).</p>
</footnote>
<footnote label="18">
<p id="b355-6"> We use the word “judicial” to connote the traditional Fourth Amendment requirement of a neutral and detached magistrate.</p>
</footnote>
<footnote label="19">
<p id="b356-7"> The Government.argues that domestic security wiretaps should be upheld by courts in post-surveillance review “[u]nless it appears that the Attorney General’s determination that the proposed surveillance relates to a national security'matter is arbitrary and capricious, <em>i. e., </em>that it constitutes a clear abuse of the broad discretion that the Attorney General has to obtain all information that will be helpful to the President in protecting the-Government .,. .” against the various unlawful acts in §2511(3). Brief for United States 22.</p>
</footnote>
<footnote label="20">
<p id="A4t"> See n. 8, <em>swgra.. </em>For the view that warrantless surveillance, though impermissible in domestic security cases, may be constitutional where foreign powers are involved, see <em>United States v. Smith, </em><span class="citation" data-id="2597100"><a href="/opinion/2597100/united-states-v-smith/#425" aria-description="Citation for case: United States v. Smith">321 F. Supp. 424, 425-426</a></span> (CD Cal. 1971); and American Bar Association Project on Standards for Criminal Justice, Electronic Surveillance 120, 121 (Approved. Draft 1971, and Feb. 1971 Supp. 11). See also <em>United States </em>v. <em>Clay, </em><span class="citation" data-id="9455905"><a href="/opinion/291561/united-states-v-cassius-marsellus-clay-jr/" aria-description="Citation for case: United States v. Cassius Marsellus Clay, Jr.">430 F. 2d 165</a></span> (CA5 1970).</p>
</footnote>
<footnote label="21">
<p id="b362-13"> We think it unnecessary at this time and on the facts , of this case to consider the arguments advanced by the Government for a re-examination of the basis and scope of the Court’s decision in <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Verdugo-Urquidez.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Verdugo-Urquidez
type: case
citation: "494 U.S. 259 (1990)"
parallel_cite: "110 S. Ct. 1056; 108 L. Ed. 2d 222"
neutral_cite: "1990 U.S. LEXIS 1175; 1990 WL 16772"
court: U.S.
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-02-28
docket: 88-1353
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
  opinion_url: "https://www.courtlistener.com/opinion/112382/united-states-v-verdugo-urquidez/"
  cluster_id: 112382
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Verdugo-Urquidez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — Anchor (foreign search)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[Fourth Amendment Recalibration]]"
tags:
  - case
  - fourth-amendment
  - the-people
  - extraterritoriality
  - nonresident-alien
holding: "The Fourth Amendment does not apply to the search and seizure by United States agents of property owned by a nonresident alien and located in a foreign country, because 'the people' the Amendment protects are those who are part of the national community or have otherwise developed a sufficient voluntary connection with the United States."
---

# United States v. Verdugo-Urquidez

*494 U.S. 259 (1990)* (No. 88-1353) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112382 → lead opinion 112382; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
René Martín Verdugo-Urquidez, a citizen and resident of Mexico, was apprehended by Mexican authorities and transferred to United States custody on drug-trafficking charges. Working with Mexican police, DEA agents then searched his residences in Mexicali and San Felipe, Mexico, without a United States warrant, and seized documents. Verdugo-Urquidez moved to suppress the seized evidence, arguing that the warrantless searches of his Mexican property violated the Fourth Amendment.

## Issue
Whether the Fourth Amendment applies to the search and seizure by United States agents of property that is owned by a nonresident alien and located in a foreign country.

## Rule
The Court construed the Amendment's reference to "the people." It held: "'the people' protected by the Fourth Amendment, and by the First and Second Amendments, and to whom rights and powers are reserved in the Ninth and Tenth Amendments, refers to a class of persons who are part of a national community or who have otherwise developed sufficient connection with this country to be considered part of that community." — 494 U.S. at 265. ^pin-265

A nonresident alien whose property abroad is searched by U.S. agents is not among "the people," so the Fourth Amendment does not reach the search.

## Application
Verdugo-Urquidez was a citizen and resident of Mexico with no voluntary attachment to the United States, and the property searched was located in Mexico. The Court grounded its reading in the Amendment's text and history and in the impracticability of imposing its warrant and reasonableness requirements on U.S. operations abroad. His involuntary presence in the United States for prosecution did not supply the substantial connection the text requires; the Fourth Amendment therefore did not apply to the foreign searches.

## Conclusion
The judgment of the Ninth Circuit was **reversed**. Rehnquist, C.J., delivered the opinion of the Court; Kennedy, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Stevens, J., concurred in the judgment; Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Marshall, J.; Blackmun, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Verdugo-Urquidez* fixes the personal scope of the Fourth Amendment — defining who counts as "the people" — and remains the framework anchor for questions about the Amendment's reach over nonresident aliens and conduct abroad.

## Appears on
- [[Private and Foreign Searches]] — *Key — Anchor (foreign search)*

## Sources
- [*United States v. Verdugo-Urquidez*, 494 U.S. 259 (1990)](https://www.courtlistener.com/opinion/112382/united-states-v-verdugo-urquidez/) — pinpoint: 265 (Opinion of the Court, "the people" holding; Rehnquist, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b130c167a8ce2e8f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "494 U.S. 259 (1990)", "court": "U.S.", "neutral_cite": "1990 U.S. LEXIS 1175; 1990 WL 16772", "official_citation_present": true, "parallel_cite": "110 S. Ct. 1056; 108 L. Ed. 2d 222", "title": "United States v. Verdugo-Urquidez", "year": "1990"}}
{"assertion_id": "1962510569c2ae04", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Key — Anchor (foreign search)", "title": "United States v. Verdugo-Urquidez"}}
{"assertion_id": "b17f972e78b180bd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fourth Amendment does not apply to the search and seizure by United States agents of property owned by a nonresident alien and located in a foreign country, because 'the people' the Amendment protects are those who are part of the national community or have otherwise developed a sufficient voluntary connection with the United States.", "title": "United States v. Verdugo-Urquidez"}}
{"assertion_id": "008b6124370f86b1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Verdugo-Urquidez", "varies_by_point": "false"}}
{"assertion_id": "2b25bc0ef723420b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Verdugo-Urquidez"}}
```

### lake record — United States v. Verdugo-Urquidez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Verdugo-Urquidez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Verdugo-Urquidez",
    "case_name_short": "Verdugo-Urquidez",
    "case_name_full": "United States v. Verdugo-Urquidez",
    "input_case_name": "United States v. Verdugo-Urquidez",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-02-28",
    "year": 1990,
    "docket": "88-1353",
    "cluster_id": 112382,
    "lead_opinion_id": 9431925,
    "sibling_ids": [],
    "absolute_url": "/opinion/112382/united-states-v-verdugo-urquidez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "494 U.S. 259",
      "volume": "494",
      "reporter": "U.S.",
      "page": "259",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1056",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 222",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 1175",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1175",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 WL 16772",
        "volume": "1990",
        "reporter": "WL",
        "page": "16772",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "494 U.S. 259",
        "volume": "494",
        "reporter": "U.S.",
        "page": "259",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1056",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 222",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 1175",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1175",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 WL 16772",
        "volume": "1990",
        "reporter": "WL",
        "page": "16772",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "494 U.S. 259",
    "official_selection": {
      "court_class": "scotus",
      "selected": "494 U.S. 259",
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
    "date_created": "2026-07-07T01:40:48Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-verdugo-urquidez--112382",
      "to_record_id": "United States v. Verdugo-Urquidez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Verdugo-Urquidez

```
<opinion type="majority">
<author id="b327-9">Chief Justice Rehnquist</author>
<p id="AQg">delivered the opinion of the Court.</p>
<p id="b327-10">The question presented by this case is whether the Fourth Amendment applies to the search and seizure by United States agents of property that is owned by a nonresident alien and located in a foreign country. We hold that it does not.</p>
<p id="b328-4"><page-number citation-index="1" label="262">*262</page-number>Respondent Rene Martin Verdugo-Urquidez is a citizen and resident of Mexico. He is believed by the United States Drug Enforcement Agency (DEA) to be one of the leaders of a large and violent organization in Mexico that smuggles narcotics into the United States. Based on a complaint charging respondent with various narcotics-related offenses, the Government obtained a warrant for his arrest on August 3, 1985. In January 1986, Mexican police officers, after discussions with United States marshals, apprehended Verdugo-Urquidez in Mexico and transported him to the United States Border Patrol station in Calexico, California. There, United States marshals arrested respondent and eventually moved him to a correctional center in San Diego, California, where he remains incarcerated pending trial.</p>
<p id="b328-5">Following respondent’s arrest, Terry Bowen, a DEA agent assigned to the Calexico DEA office, decided to arrange for searches of Verdugo-Urquidez’s Mexican residences located in Mexicali and San Felipe. Bowen believed that the searches would reveal evidence related to respondent’s alleged narcotics trafficking activities and his involvement in the kidnaping and torture-murder of DEA Special Agent Enrique Camarena Salazar (for which respondent subsequently has been convicted in a separate prosecution. See <em>United States </em>v. <em>Verdugo-Urquidez, </em>No. CR-87-422-ER (CD Cal., Nov. 22, 1988)). Bowen telephoned Walter White, the Assistant Special Agent in charge of the DEA office in Mexico City, and asked him to seek authorization for the search from the Director General of the Mexican Federal Judicial Police (MFJP). After several attempts to reach high ranking Mexican officials, White eventually contacted the Director General, who authorized the searches and promised the cooperation of Mexican authorities. Thereafter, DEA agents working in concert with officers of the MFJP searched respondent’s properties in Mexicali and San Felipe and seized certain documents. In particular, the search of the Mexicali residence uncovered a tally sheet, which the Government <page-number citation-index="1" label="263">*263</page-number>believes reflects the quantities of marijuana smuggled by Verdugo-Urquidez into the United States.</p>
<p id="b329-5">The District Court granted respondent’s motion to suppress evidence seized during the searches, concluding that the Fourth Amendment applied to the searches and that the DEA agents had failed to justify searching respondent’s premises without a warrant. A divided panel of the Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d 1214</a></span> (1988). It cited this Court’s decision in <em>Reid </em>v. <em>Covert, </em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">354 U. S. 1</a></span> (1957), which held that American citizens tried by United States military authorities in a foreign country were entitled to the protections of the Fifth and Sixth Amendments, and concluded that “[t]he Constitution imposes substantive constraints on the federal government, even when it operates abroad.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1218" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d, at 1218</a></span>. Relying on our decision in <em>INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S. 1032</a></span> (1984), where a majority of Justices assumed that illegal aliens in the United States have Fourth Amendment rights, the Ninth Circuit majority found it “difficult to conclude that Verdugo-Urquidez lacks these same protections.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1223" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d, at 1223</a></span>. It also observed that persons in respondent’s position enjoy certain trial-related rights, and reasoned that “[i]t would be odd indeed to acknowledge that Verdugo-Urquidez is entitled to due process under the fifth amendment, and to a fair trial under the sixth amendment, . . . and deny him the protection from unreasonable searches and seizures afforded under the fourth amendment.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1224" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez"><em>Id., </em>at 1224</a></span>. Having concluded that the Fourth Amendment applied to the searches of respondent’s properties, the court went on to decide that the searches violated the Constitution because the DEA agents failed to procure a search warrant. Although recognizing that “an American search warrant would be of no legal validity in Mexico,” the majority deemed it sufficient that a warrant would have “substantial constitutional value in this country,” because it would reflect a magistrate’s determination <page-number citation-index="1" label="264">*264</page-number>that there existed probable cause to search and would define the scope of the search. <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1230" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez"><em>Id., </em>at 1230</a></span>.</p>
<p id="b330-5">The dissenting judge argued that this Court’s statement in <em>United States </em>v. <em>Curtiss-Wright Export Corp., </em><span class="citation" data-id="102726"><a href="/opinion/102726/united-states-v-curtiss-wright-export-corp/#318" aria-description="Citation for case: United States v. Curtiss-Wright Export Corp.">299 U. S. 304, 318</a></span> (1936), that “[n]either the Constitution nor the laws passed in pursuance of it have any force in foreign territory unless in respect of our own citizens,” foreclosed any claim by respondent to Fourth Amendment rights. More broadly, he viewed the Constitution as a “compact” among the people of the United States, and the protections of the Fourth Amendment were expressly limited to “the people.” We granted certiorari, 490 U. S; 1019 (1989).</p>
<p id="b330-6">Before analyzing the scope of the Fourth Amendment, we think it significant to note that it operates in a different manner than the Fifth Amendment, which is not at issue in this case. The privilege against self-incrimination guaranteed by the Fifth Amendment is a fundamental trial right of criminal defendants. See <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). Although conduct by law enforcement officials prior to trial may ultimately impair that right, a constitutional violation occurs only at trial. <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 453</a></span> (1972). The Fourth Amendment functions differently. It prohibits “unreasonable searches and seizures” whether or not the evidence is sought to be used in a criminal trial, and a violation of the Amendment is “fully accomplished” at the time of an unreasonable governmental intrusion. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974); <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906</a></span> (1984). For purposes of this case, therefore, if there were a constitutional violation, it occurred solely in Mexico. Whether evidence obtained from respondent’s Mexican residences should be excluded at trial in the United States is a remedial question separate from the existence <em>vel non </em>of the constitutional violation. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 354</a></span>; <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 906</a></span>.</p>
<p id="b330-7">The Fourth Amendment provides:</p>
<blockquote id="b331-4"><page-number citation-index="1" label="265">*265</page-number>“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b331-5">That text, by contrast with the Fifth and Sixth Amendments, extends its reach only to “the people.” Contrary to the suggestion of <em>amici curiae </em>that the Framers used this phrase “simply to avoid [an] awkward rhetorical redundancy,” Brief for American Civil Liberties Union et al. as <em>Amici Curiae </em>12, n. 4, “the people” seems to have been a term of art employed in select parts of the Constitution. The Preamble declares that the Constitution is ordained and established by “the People of the United States.” The Second Amendment protects “the right of the people to keep and bear Arms,” and the Ninth and Tenth Amendments provide that certain rights and powers are retained by and reserved to “the people.” See also U. S. Const., Arndt. 1 (“Congress shall make no law . . . abridging <em>... the right of the people </em>peaceably to assemble”) (emphasis added); Art. I, § 2, cl. 1 (“The House of Representatives shall be composed of Members chosen every second Year <em>by the People of the several States”) </em>(emphasis added). While this textual exegesis is by no means conclusive, it suggests that “the, people” protected by the Fourth Amendment, and by the First and Second Amendments, and to whom rights and powers are reserved in the Ninth and Tenth Amendments, refers to a class of persons who are part of a national community or who have otherwise developed sufficient connection with this country to be considered part of that community. See <em>United States ex rel. Turner </em>v. <em>Williams, </em><span class="citation" data-id="9417945"><a href="/opinion/96089/united-states-ex-rel-turner-v-williams/#292" aria-description="Citation for case: United States Ex Rel. Turner v. Williams">194 U. S. 279, 292</a></span> (1904) (Excludable alien is not entitled to First Amendment rights, because “[h]e does not become one of the people to whom these things are secured by our Constitution by an attempt to enter forbidden by law”). The language of these Amendments contrasts with the words <page-number citation-index="1" label="266">*266</page-number>“person” and “accused” used in the Fifth and Sixth Amendments regulating procedure in criminal cases.</p>
<p id="b332-5">What we know of the history of the drafting of the Fourth Amendment also suggests that its purpose was to restrict searches and seizures which might be conducted by the United States in domestic matters. The Framers originally decided not to include a provision like the Fourth Amendment, because they believed the National Government lacked power to conduct searches and seizures. See C. Warren, The Making of the Constitution 508-509 (1928); The Federalist No. 84, p. 513 (C. Rossiter ed. 1961) (A. Hamilton); 1 Annals of Cong. 437 (1789) (statement of J. Madison). Many disputed the original view that the Federal Government possessed only narrow delegated powers over domestic affairs, however, and ultimately felt an Amendment prohibiting unreasonable searches and seizures was necessary. Madison, for example, argued that “there is a clause granting to Congress the power to make all laws which shall be necessary and proper for carrying into execution all of the powers vested in the Government of the United States,” and that general warrants might be considered “necessary” for the purpose of collecting revenue. <em>Id., </em>at 438. The driving force behind the adoption of the Amendment, as suggested by Madison’s advocacy, was widespread hostility among the former colonists to the issuance of writs of assistance empowering revenue officers to search suspected places for smuggled goods, and general search warrants permitting the search of private houses, often to uncover papers that might be used to' convict persons of libel. See <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625-626</a></span> (1886). The available historical data show, therefore, that the purpose of the Fourth Amendment was to protect the people of the United States against arbitrary action by their own Government; it was never suggested that the provision was intended to restrain the actions of the Federal Government against aliens outside of the United States territory.</p>
<p id="b333-4"><page-number citation-index="1" label="267">*267</page-number>There is likewise no indication that the Fourth Amendment was understood by contemporaries of the Framers to apply to activities of the United States directed against aliens in foreign territory or in international waters. Only seven years after the ratification of the Amendment, French interference with American commercial vessels engaged in neutral trade triggered what came to be known as the “undeclared war” with France. In an Act to “protect the Commerce of the United States” in 1798, Congress authorized President Adams to “instruct the commanders of the public armed vessels which are, or which shall be employed in the service of the United States, to subdue, seize and take any armed French vessel, which shall be found within the jurisdictional limits of the United States, or elsewhere, on the high seas.” § 1 of An Act Further to Protect the Commerce of the United States, ch. 68, <span class="citation no-link">1 Stat. 578</span>. This public naval force consisted of only 45 vessels, so Congress also gave the President power to grant to the owners of private armed ships and vessels of the United States “special commissions,” which would allow them “the same license and authority for the subduing, seizing and capturing any armed French vessel, and for the recapture of the vessels, goods and effects of the people of the United States, as the public armed vessels of the United States may by law have.” § 2, <span class="citation no-link">1 Stat. 579</span>; see U. S. Const., Art. I, §8, cl. 11 (Congress has power to grant letters of marque and reprisal). Under the latter provision, 365 private armed vessels were commissioned before March 1, 1799, see G. Allen, Our Naval War with France 59 (1967); together, these enactments resulted in scores of seizures of foreign vessels under congressional authority. See M. Palmer, Stoddert’s War: Naval Operations During the Quasi-War with France, 1798-1801, p. 235 (1987). See also An Act Further to Suspend the Commercial Intercourse Between the United States and France, ch. 2, <span class="citation no-link">1 Stat. 613</span>. Some commanders were held liable by this Court for unlawful seizures because their actions were beyond the scope of the congres<page-number citation-index="1" label="268">*268</page-number>sional grant of authority, see, <em>e. g., Little </em>v. <em>Barreme, </em><span class="citation" data-id="84781"><a href="/opinion/84781/little-v-barreme/#177" aria-description="Citation for case: Little v. Barreme">2 Cranch 170, 177-178</a></span> (1804); cf. <em>Talbot </em>v. <em>Seeman, </em><span class="citation" data-id="84754"><a href="/opinion/84754/talbot-v-seeman/#81" aria-description="Citation for case: Talbot v. Seeman">1 Cranch 1, 81</a></span> (1801) (seizure of neutral ship lawful where American captain had probable cause to believe vessel was French), but it was never suggested that the Fourth Amendment restrained the authority of Congress or of United States agents to conduct operations such as this.</p>
<p id="b334-5">The global view taken by the Court of Appeals of the application of the Constitution is also contrary to this Court’s decisions in the <em>Insular Cases, </em>which held that not every constitutional provision applies to governmental activity even where the United States has sovereign power. See, <em>e. g., Balzac </em>v. <em>Porto Rico, </em><span class="citation" data-id="99954"><a href="/opinion/99954/balzac-v-porto-rico/" aria-description="Citation for case: Balzac v. Porto Rico">258 U. S. 298</a></span> (1922) (Sixth Amendment right to jury trial inapplicable in Puerto Rico); <em>Ocampo </em>v. <em>United States, </em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">234 U. S. 91</a></span> (1914) (Fifth Amendment grand jury provision inapplicable in Philippines); <em>Dorr </em>v. <em>United States, </em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/" aria-description="Citation for case: Dorr v. United States">195 U. S. 138</a></span> (1904) (jury trial provision inapplicable in Philippines); <em>Hawaii </em>v. <em>Mankichi, </em><span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197</a></span> (1903) (provisions on indictment by grand jury and jury trial inapplicable in Hawaii); <em>Downes </em>v. <em>Bidwell, </em><span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span> (1901) (Revenue Clauses of Constitution inapplicable to Puerto Rico). In <em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/" aria-description="Citation for case: Dorr v. United States">Dorr</a></span>, </em>we declared the general rule that in an unincorporated territory — one not clearly destined for statehood — Congress was not required to adopt “a system of laws which shall include the right of trial by jury, and that <em>the Constitution does not, without legislation and of its own force, carry such right to territory so situated.” </em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/#149" aria-description="Citation for case: Dorr v. United States">195 U. S., at 149</a></span> (emphasis added). Only “fundamental” constitutional rights are guaranteed to inhabitants of those territories. <span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/#148" aria-description="Citation for case: Dorr v. United States"><em>Id., </em>at 148</a></span>; <span class="citation" data-id="99954"><a href="/opinion/99954/balzac-v-porto-rico/#312" aria-description="Citation for case: Balzac v. Porto Rico"><em>Balzac, supra, </em>at 312-313</a></span>; see <em>Examining Board of Engineers, Architects and Surveyors </em>v. <em>Flores de Otero, </em><span class="citation" data-id="9426457"><a href="/opinion/109490/examining-bd-of-engineers-architects-and-surveyors-v-flores-de-otero/#599" aria-description="Citation for case: Examining Bd. of Engineers, Architects and Surveyors v....">426 U. S. 572, 599, n. 30</a></span> (1976). If that is true with respect to territories ultimately governed by Congress, respondent’s claim that the protections of the Fourth Amendment extend to aliens in foreign nations is even weaker. And certainly, it is not open to us in light of the <em>Insular Cases </em>to endorse the <page-number citation-index="1" label="269">*269</page-number>view that every constitutional provision applies wherever the United States Government exercises its power.</p>
<p id="b335-5">Indeed, we have rejected the claim that aliens are entitled to Fifth Amendment rights outside the sovereign territory of the United States. In <em>Johnson </em>v. <em>Eisentrager, </em><span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">339 U. S. 763</a></span> (1950), the Court held that enemy aliens arrested in China and imprisoned in Germany after World War II could not obtain writs of habeas corpus in our federal courts on the ground that their convictions for war crimes had violated the Fifth Amendment and other constitutional provisions. The <em><span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">Eisentrager</a></span> </em>opinion acknowledged that in some cases constitutional provisions extend beyond the citizenry; “[t]he alien . . . has been accorded a generous and ascending scale of rights as he increases his identity with our society.” <span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/#770" aria-description="Citation for case: Johnson v. Eisentrager"><em>Id., </em>at 770</a></span>. But our rejection of extraterritorial application of the Fifth Amendment was emphatic:</p>
<blockquote id="b335-6">“Such extraterritorial application of organic law would have been so significant an innovation in the practice of governments that, if intended or apprehended, it could scarcely have failed to excite contemporary comment. Not one word can be cited. No decision of this Court supports such a view. <em>Cf. Downes </em>v. <em>Bidwell, </em><span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span> [(1901)]. None of the learned commentators on our Constitution has even hinted at it. The practice of every modern government is opposed to it.” <em>Id., </em>at 784.</blockquote>
<p id="b335-7">If such is true of the Fifth Amendment, which speaks in the relatively universal term of “person,” it would seem even more true with respect to the Fourth Amendment, which applies only to “the people.”</p>
<p id="b335-8">To support his all-encompassing view of the Fourth Amendment, respondent points to language from the plurality opinion in <em>Reid </em>v. <em>Covert, </em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">354 U. S. 1</a></span> (1957). <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>involved an attempt by Congress to subject the wives of American servicemen to trial by military tribunals without the protection of the Fifth and Sixth Amendments. The Court held that it was unconstitutional to apply the Uniform Code of Military <page-number citation-index="1" label="270">*270</page-number>Justice to the trials of the American women for capital crimes. Four Justices “rejected] the idea that when the United States acts <em>against citizens </em>abroad it can do so free of the Bill of Rights.” <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#5" aria-description="Citation for case: Reid v. Covert"><em>Id., </em>at 5</a></span> (emphasis added). The plurality went on to say:</p>
<blockquote id="b336-5">“The United States is entirely a creature of the Constitution. Its power and authority have no other source. It can only act in accordance with all the limitations imposed by the Constitution. When the Government reaches out to punish <em>a citizen </em>who is abroad, the shield which the Bill of Rights and other parts of the Constitution provide to protect his life and liberty should not be stripped away just because he happens to be in another land.” <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#5" aria-description="Citation for case: Reid v. Covert"><em>Id., </em>at 5-6</a></span> (emphasis added; footnote omitted).</blockquote>
<p id="b336-6">Respondent urges that we interpret this discussion to mean that federal officials are constrained by the Fourth Amendment wherever and against whomever they act. But the holding of <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>stands for no such sweeping proposition: it decided that United States citizens stationed abroad could invoke the protection of the Fifth and Sixth Amendments. The concurrences by Justices Frankfurter and Harlan in <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>resolved the case on much narrower grounds than the plurality and declined even to hold that United States citizens were entitled to the full range of constitutional protections in all overseas criminal prosecutions. See <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#75" aria-description="Citation for case: Reid v. Covert"><em>id., </em>at 75</a></span> (Harlan, J., concurring in result) (“I agree with my brother Frankfurter that... we have before us a question analogous, ultimately, to issues of due process; one can say, in fact, that the question of which specific safeguards of the Constitution are appropriately to be applied in a particular context overseas can be reduced to the issue of what process is ‘due’ a defendant in the particular circumstances of a particular case”). Since respondent is not a United States citizen, he can derive no comfort from the <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>holding.</p>
<p id="b336-7">Verdugo-Urquidez also relies on a series of cases in which we have held that aliens enjoy certain constitutional rights. <page-number citation-index="1" label="271">*271</page-number>See, <em>e. g., Plyler </em>v. <em>Doe, </em><span class="citation" data-id="9428818"><a href="/opinion/110742/plyler-v-doe/#211" aria-description="Citation for case: Plyler v. Doe">457 U. S. 202, 211-212</a></span> (1982) (illegal aliens protected by Equal Protection Clause); <em>Kwong Hai Chew </em>v. <em>Colding, </em><span class="citation" data-id="105078"><a href="/opinion/105078/kwong-hai-chew-v-colding/#596" aria-description="Citation for case: Kwong Hai Chew v. Colding">344 U. S. 590, 596</a></span> (1953) (resident alien is a “person” within the meaning of the Fifth Amendment); <em>Bridges </em>v. <em>Wixon, </em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#148" aria-description="Citation for case: Bridges v. Wixon">326 U. S. 135, 148</a></span> (1945) (resident aliens have First Amendment rights); <em>Russian Volunteer Fleet </em>v. <em>United States, </em><span class="citation" data-id="101660"><a href="/opinion/101660/russian-volunteer-fleet-v-united-states/" aria-description="Citation for case: Russian Volunteer Fleet v. United States">282 U. S. 481</a></span> (1931) (Just Compensation Clause of Fifth Amendment); <em>Wong Wing </em>v. <em>United States, </em><span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#238" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 238</a></span> (1896) (resident aliens entitled to Fifth and Sixth Amendment rights); <em>Yick Wo </em>v. <em>Hopkins, </em><span class="citation" data-id="91704"><a href="/opinion/91704/yick-wo-v-hopkins/#369" aria-description="Citation for case: Yick Wo v. Hopkins">118 U. S. 356, 369</a></span> (1886) (Fourteenth Amendment protects resident aliens). These cases, however, establish only that aliens receive constitutional protections when they have come within the territory of the United States and developed substantial connections with this country. See, <span class="citation" data-id="9428818"><a href="/opinion/110742/plyler-v-doe/#212" aria-description="Citation for case: Plyler v. Doe"><em>e. g., Plyler, supra, </em>at 212</a></span> (The provisions of the Fourteenth Amendment “ ‘are universal in their application, <em>to all persons within the territorial jurisdiction . </em>. .’”) (quoting <em>Yick Wo, supra, </em>at 369); <span class="citation" data-id="105078"><a href="/opinion/105078/kwong-hai-chew-v-colding/#596" aria-description="Citation for case: Kwong Hai Chew v. Colding"><em>Kwong Hai Chew, supra, </em>at 596, n. 5</a></span> (“The Bill of Rights is a futile authority for the alien seeking admission for the first time to these shores. But <em>once an alien lawfully enters and resides in this country </em>he becomes invested with the rights guaranteed by the Constitution to all people within our borders”) (quoting <span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#161" aria-description="Citation for case: Bridges v. Wixon"><em>Bridges, supra, </em>at 161</a></span> (concurring opinion) (emphasis added)). Respondent is an alien who has had no previous significant voluntary connection with the United States, so these cases avail him not.</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Von Neumann.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Von Neumann
type: case
citation: "474 U.S. 242 (1986)"
parallel_cite: "106 S. Ct. 610; 88 L. Ed. 2d 587; 54 U.S.L.W. 4065"
neutral_cite: 1986 U.S. LEXIS 39
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-01-14
docket: No. 84-1144
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
  opinion_url: "https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/"
  cluster_id: 111551
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Von Neumann
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. $8,850 in Currency]]"
tags:
  - case
  - civil-forfeiture
  - due-process
  - remission
  - customs
  - delay
holding: "A 36-day delay by the Customs Service in ruling on a petition for remission or mitigation after seizing an undeclared car did not deny the claimant due process: because the judicial forfeiture proceeding itself supplies the post-seizure hearing due process requires (its timeliness measured by the Barker v. Wingo factors), the discretionary remission procedure is not constitutionally necessary and creates no separate right to a speedy answer to a remission petition."
aliases:
  - United States v. Von Neumann
  - "United States v. Von Neumann (1986)"
---

# United States v. Von Neumann

*474 U.S. 242 (1986)* (No. 84-1144) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 111551 → combined opinion 111551 (Brennan, J.; 474 U.S. 242, argued Nov. 4, 1985, decided Jan. 14, 1986). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*250` and `*251`, i.e., on page 250). S9 promotes. -->

## Background
In January 1975, John Von Neumann drove a Jaguar Panther he had bought in Switzerland across the Canadian border into Washington State and failed to declare it to U.S. customs; a customs officer seized the car under 19 U.S.C. § 1497. The same day, Von Neumann filed a petition for remission or mitigation under 19 U.S.C. § 1618, and about two weeks later posted a $24,500 bond to get the car back. Thirty-six days after the petition was filed, the Customs Service acted on it, reducing the penalty to $3,600. After exhausting administrative review, Von Neumann sued, and the Ninth Circuit held that the 36-day delay in ruling on the remission petition denied him due process — going so far as to require Customs to act on such petitions within 24 hours.

## Issue
Whether a claimant whose property has been seized has a due process right to a speedy disposition of his § 1618 petition for remission or mitigation, such that a 36-day delay in ruling on the petition violates the Fifth Amendment.

## Rule
The Court located the claimant's constitutional protection in the forfeiture proceeding itself, not in the remission procedure. Under *[[United States v. $8,850 in Currency|$8,850]]*, the judicial forfeiture action — whose own timeliness is measured by the *Barker v. Wingo* factors — provides the post-seizure hearing due process requires. Remission is a discretionary act of grace that lets the parties resolve the matter informally, but it is not a step the Constitution mandates. The Court therefore held: "Thus there is no constitutional basis for a claim that respondent's interest in the car, or in the money put up to secure the bond, entitles him to a speedy answer to his remission petition." — 474 U.S. at 250. ^pin-250

## Application
Because remission proceedings are not necessary to a forfeiture determination, the claimant's property interest in the car and the bond money gave him no constitutional entitlement to a prompt ruling on his remission petition; his protection was the right to a timely forfeiture proceeding, which he had. The Court added that, even assuming § 1618 created some protectable interest, any timeliness requirement was amply satisfied here: the delay was brief, part of it may not even count (Von Neumann supplemented his petition and got a final decision 13 days later), and he showed no prejudice to either his forfeiture defense or his remission "case," which was complete when filed.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed**. Brennan, J., delivered the opinion of the Court; Stevens, J., filed an opinion concurring in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Von Neumann* fixes the constitutional locus of forfeiture process: the due process a claimant is owed attaches to the *forfeiture proceeding* (timed under *[[United States v. $8,850 in Currency|$8,850]]*'s *Barker* factors), not to the discretionary administrative *remission* petition. Teach it with *[[United States v. $8,850 in Currency]]* (the timeliness framework it applies) as the pair that maps where — and where not — due process constrains the pace of civil forfeiture.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. Von Neumann*, 474 U.S. 242 (1986)](https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/) — pinpoint: 250 (Brennan, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*250` and `*251`, i.e., on page 250). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c31ebf6df1806777", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "474 U.S. 242 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 39", "official_citation_present": true, "parallel_cite": "106 S. Ct. 610; 88 L. Ed. 2d 587; 54 U.S.L.W. 4065", "title": "United States v. Von Neumann", "year": "1986"}}
{"assertion_id": "a7bbb6714a08b26a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 36-day delay by the Customs Service in ruling on a petition for remission or mitigation after seizing an undeclared car did not deny the claimant due process: because the judicial forfeiture proceeding itself supplies the post-seizure hearing due process requires (its timeliness measured by the Barker v. Wingo factors), the discretionary remission procedure is not constitutionally necessary and creates no separate right to a speedy answer to a remission petition.", "title": "United States v. Von Neumann"}}
{"assertion_id": "ba3624fcb770b784", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "United States v. Von Neumann"}}
{"assertion_id": "142b0ad1f47caac9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Von Neumann"}}
{"assertion_id": "73a35b293c926606", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Von Neumann", "varies_by_point": "false"}}
```

### lake record — United States v. Von Neumann

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Von Neumann",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Von Neumann",
    "case_name_short": "Von Neumann",
    "case_name_full": "United States v. Von Neumann",
    "input_case_name": "United States v. Von Neumann",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-01-14",
    "year": 1986,
    "docket": "No. 84-1144",
    "cluster_id": 111551,
    "lead_opinion_id": 9430249,
    "sibling_ids": [],
    "absolute_url": "/opinion/111551/united-states-v-von-neumann/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "474 U.S. 242",
      "volume": "474",
      "reporter": "U.S.",
      "page": "242",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "474 U.S. 242",
        "volume": "474",
        "reporter": "U.S.",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "474 U.S. 242",
    "official_selection": {
      "court_class": "scotus",
      "selected": "474 U.S. 242",
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
    "date_created": "2026-07-06T13:41:55Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-von-neumann--111551",
      "to_record_id": "United States v. Von Neumann",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Von Neumann

```
<opinion type="majority">
<author id="b381-10">Justice Brennan</author>
<p id="AMB">delivered the opinion of the Court.</p>
<p id="b381-11">We must decide in this case whether a 36-day delay by the United States Customs Service in responding to a remission petition filed by respondent in response to the seizure of his car by customs agents deprived respondent of property without due process of law.</p>
<p id="b381-12">I</p>
<p id="b381-13">Title <span class="citation no-link">19 U. S. C. § 1497</span><footnotemark>1</footnotemark> provides that any article not declared upon entry into the United States which by law <page-number citation-index="1" label="244">*244</page-number>must be declared is subject to forfeiture or to a penalty equaling the value of the article. After seizure of an article by the United States Customs Service, a claimant to it has essentially two options. He may pursue an administrative remedy under <span class="citation no-link">19 U. S. C. §1618</span> (1982 ed., Supp. Ill),<footnotemark>2</footnotemark> which vests in the Secretary of the Treasury the discretionary authority to mitigate or remit the penalty or forfeiture, or he may challenge the seizure in a judicial forfeiture action initiated by the Government.<footnotemark>3</footnotemark> <span class="citation no-link">19 U. S. C. §§ 1602-1604</span>.<footnotemark>4</footnotemark></p>
<p id="b383-4"><page-number citation-index="1" label="245">*245</page-number>In 1974, respondent John Von Neumann shipped to Vancouver, Canada, a 1974 Jaguar Panther automobile he purchased in Switzerland. On January 20, 1975, he and a friend picked up the car in Vancouver, obtained a release from Canadian Customs to take possession of the vehicle and also obtained a form that Von Neumann was to deliver to the Canadian Customs station at the border. Von Neumann failed to deliver the form to Canadian Customs officials. He claimed that he inadvertently drove past the Canadian Customs station because of poor visibility and inadequate directions. Instead, Von Neumann and his friend arrived at the United States border checkpoint at Blaine, Washington, where they were questioned by United States Immigration Officer Harry Perkins, a designated customs officer. Canadian Customs officials had earlier alerted United States Customs that Von Neumann’s car would be crossing the border, and Perkins specifically asked Von Neumann whether he had anything to declare. When Von Neumann failed to declare the automobile, Perkins asked him into the checkpoint station and referred the matter to Customs Inspector Donald E. Morrison. Upon being asked why he had not declared the car, Von Neumann explained that he did not think a declaration was required. Morrison then seized the car pursuant to <span class="citation no-link">19 U. S. C. § 1497</span>.</p>
<p id="b383-5">That same day, January 20, Von Neumann prepared a “Petition for Remission or Mitigation of Forfeitures and Penalties Incurred,” pursuant to <span class="citation no-link">19 U. S. C. § 1618</span>, explaining that he had not intended to violate United States Customs laws when he failed to declare the car. Two weeks later, on February 3, Von Neumann posted a bond for $24,500, the <page-number citation-index="1" label="246">*246</page-number>value of his car, and Customs released the vehicle pursuant to its authority under <span class="citation no-link">19 U. S. C. § 1614</span>. On February 12, counsel for Von Neumann filed a supplement to the original remission petition. On February 25 — 36 days after the petition was filed — the Seattle District Director of the Customs Service, pursuant to delegation of authority from the Secretary of the Treasury,<footnotemark>5</footnotemark> acted on Von Neumann’s remission petition, and informed Von Neumann that the penalty for failure to declare the car was being reduced to $3,600. On administrative review of this determination, the Regional Commissioner of Customs in San Francisco, on April 14, 1975, upheld the $3,600 penalty.</p>
<p id="b384-5">Having exhausted his administrative remedies, Von Neu-mann filed a complaint in the United States District Court for the Central District of California. He sought cancellation of the $3,600 penalty on the ground that he had not violated § 1497. He also requested an injunction prohibiting Customs from placing his name on a computer list of violators, and a declaration that this seizure and penalty were unlawful. The District Court found that Von Neumann had violated <span class="citation no-link">19 U. S. C. § 1497</span>, and that seizure of the car therefore was proper. The court also upheld the validity of the remission and mitigation procedures. Accordingly, it entered judgment for the Government.<footnotemark>6</footnotemark> Von Neumann appealed this de-<page-number citation-index="1" label="247">*247</page-number>cisión, challenging both the procedures followed by Customs in imposing the penalty and also the penalty itself.</p>
<p id="b385-5">The Court of Appeals for the Ninth. Circuit agreed with the District Court that Von Neumann had violated § 1497. <span class="citation multiple-matches"><a href="/c/F.%202d/660/1319/">660 F. 2d 1319</a></span>, 1323 (1981). The court, however, also considered and sustained Von Neumann’s claim that the 36-day delay in acting on his remission petition denied Von Neu-mann due process of law in violation of the Fifth Amendment. The court reasoned that speed in the handling of the remission petition, particularly where the seizure is of an automobile, is constitutionally required — that strict guidelines in responding to remission petitions are necessary “to ensure the due process rights of administrative claimants,” <em>id., </em>at 1326-1327, and concluded that Customs must “act on a petition for remission or mitigation within 24 hours of receipt,” <em>id., </em>at 1327. In addition, the court ruled, a claimant has a right to a personal appearance to present his or her claim. <em>Ibid.</em></p>
<p id="b385-6">The Government petitioned for certiorari. We granted the petition, vacated, and remanded for reconsideration in light of <em>United States </em>v. <em>$8,850, </em><span class="citation multiple-matches"><a href="/c/U.%20S./461/665/">461 U. S. 665</a></span> (1983). <span class="citation" data-id="9039097"><a href="/opinion/9045725/united-states-v-von-neumann/" aria-description="Citation for case: United States v. Von Neumann">462 U. S. 1101</a></span> (1983). In <em>$8,850, </em>however, the issue presented did not involve the remission procedure; rather the question was whether the Government’s 18-month delay in bringing a <em>forfeiture </em>proceeding violated the claimant’s right to due process of law. The Court held that due process requires a postseizure determination within a reasonable time of the seizure. We concluded that the four-factor balancing test of <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), provides the relevant framework for determining whether a delay was reasonable. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test involves a weighing of four factors: the length of any delay, the reason for the delay, the defendant’s assertion of his right, and prejudice suffered by the defendant. Applying this test to the 18-month delay before it, the <page-number citation-index="1" label="248">*248</page-number>Court in <em>$8,850 </em>found no unreasonable delay, in part because a substantial portion of the delay in question was attributable to pending administrative and criminal proceedings.</p>
<p id="b386-5">On remand in this case, the Court of Appeals recognized that <em>$8,850 </em>“presented a somewhat different issue from that arising in the instant case,” <span class="citation multiple-matches"><a href="/c/F.%202d/729/657/">729 F. 2d 657</a></span>, 659 (1984), because <em>$8,850 </em>dealt with forfeiture rather than the remission procedure. Nevertheless, it concluded that this Court’s holding in <em>$8,850 </em>“reinforces our earlier view that due process rights attach to the processing of the petition for remission,” 729 F. 2d, at 660, and therefore reaffirmed its holding that “due process requires Customs to act promptly in ruling on petitions for remission or mitigation under <span class="citation no-link">19 U. S. C. §1618</span>.” <em><span class="citation no-link">Ibid.</span> </em>The court recognized that its earlier attempt to set specific time limits for the processing of remission petitions was “ill-advised,” <em>ibid., </em>and held instead that the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>factors should also be applied to determine whether Customs has violated due process in delaying a response to a remission petition. The court accordingly remanded the case to the District Court to consider whether the 36-day delay violated due process. In addition, however, the court made clear its view that the circumstances of this case support a finding of a due process violation. Thus, the court noted that the propriety of the length of the delay may turn on the nature of the item that has been seized, and reemphasized the point made in its earlier opinion that “special hardships [are] imposed on persons deprived of the use of their automobiles . . . .” 729 F. 2d, at 661. With respect to the reason for the delay, the Court of Appeals observed that the “record here provides no obvious reason for the Government’s one-month delay in processing von Neumann’s petition, although we note that Customs processes a great number of petitions each year.” <em>Ibid. </em>In addition, the court pointed to the filing of the remission petition itself as the necessary assertion of the right to a speedy determination under <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>. </em>Finally, the court <page-number citation-index="1" label="249">*249</page-number>noted that prejudice could be established by the inconvenience of being without a vehicle for any length of time.</p>
<p id="b387-7">Arguing that due process considerations do not govern the Secretary’s disposition of remission petitions, the Government petitioned for certiorari. We granted the Government’s petition. <span class="citation multiple-matches"><a href="/c/U.%20S./471/1064/">471 U. S. 1064</a></span> (1984). We now reverse.</p>
<p id="b387-8">I — ! b — I</p>
<p id="b387-1">We understand respondent to argue that his property interest in his car gives him a constitutional right to a speedy disposition of his remission petition without awaiting a forfeiture proceeding. We disagree. Implicit in this Court’s discussion of timeliness in <em>$8,850 </em>was the view that the forfeiture proceeding, without more, provides the postseizure hearing required by due process to protect Von Neumann’s property interest in the car.<footnotemark>7</footnotemark> Respondent argues, however, that “[t]he petition for remission procedure is just one step in which it is determined whether that property interest will be extinguished via a judicial foreclosure proceeding.” Brief for Respondent 8-9. We think respondent misunderstands the remission procedure’s role. It is true that, as a practical matter, most forfeitures are disposed of through the administrative remission procedures,<footnotemark>8</footnotemark> but that is constitutionally <page-number citation-index="1" label="250">*250</page-number>irrelevant. We noted in <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#234" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 234</a></span> (1972), that in the event an item is not declared at the border under § 1497 “[t]he Government need only prove that the property was brought into the United States without the required declaration; the Government bears no burden with respect to intent.” The remission statute simply grants the Secretary the discretion not to pursue a complete forfeiture despite the Government’s entitlement to one. Remission proceedings supply both the Government and the claimant a way to resolve a dispute informally rather than in judicial forfeiture proceedings. But remission proceedings are not <em>necessary </em>to a forfeiture determination, and therefore are not constitutionally required. Thus there is no constitutional basis for a claim that respondent’s interest in the car, or in the money put up to secure the bond, entitles him to a speedy answer to his remission petition.</p>
<p id="b388-5">Ill</p>
<p id="b388-6">While his interest in the car is the only basis on which respondent relies in his support of the Court of Appeals’ decision, the Government asks that the Court adjudge the case of a claimant who relies on the argument that § 1618 itself creates a property right which cannot be taken away without due process that includes a speedy answer to a remission petition. The Government argues that the statute creates no such right. We need not address the hypothetical, however. It is abundantly clear on, the record in this case that, even if respondent had such a property right, any due process requirement of timely disposition was more than adequately provided here. It is difficult, indeed impossible, to see what prejudice respondent suffered from the 36-day delay in the response. True, he was without his car for 14 days, and then, for another 22 days, without the money he <page-number citation-index="1" label="251">*251</page-number>had to put up to secure a bond, and Von Neumann urges the importance of automobiles to citizens in this society. But we have already noted that his right to a forfeiture proceeding meeting the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test satisfies any due process right with respect to the car and the money. In fact, it is not altogether certain that the delay dated from the filing on January 20 of the original remission petition. Respondent supplemented his remission petition and was given a final decision just 13 days later. Moreover, respondent gives no hint as to how or why even a 36-day delay in the disposition of his remission petition deprived him of the process he claims was his due in connection with that petition. He does not argue that the delay prejudiced his defense against the forfeiture, see <em>$8,850, </em>461 U. S., at 569, and with respect to preparing his “case” for remission, that case was made at the time of filing and could not have been affected by the subsequent delay. On the record before us, the 36-day delay cannot be said to deprive respondent of due process of law.</p>
<p id="b389-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b381-14"> Section 497, <span class="citation no-link">46 Stat. 728</span>, <span class="citation no-link">19 U. S. C. § 1497</span>, provides:</p>
<p id="b381-15">“Any article not included in the declaration and entry as made, and, before examination of the baggage was begun, not mentioned in writing by such person, if written declaration and entry was required, or orally if written <page-number citation-index="1" label="244">*244</page-number>declaration and entry was not required, shall be subject to forfeiture and such person shall be liable to a penalty equal to the value of such article.”</p>
</footnote>
<footnote label="2">
<p id="b382-6"> Section 618, <span class="citation no-link">46 Stat. 757</span>, as amended and set forth in <span class="citation no-link">19 U. S. C. § 1618</span> (1982 ed., Supp. Ill), provides in pertinent part:</p>
<p id="b382-7">“Whenever any person interested in any vessel, vehicle, aircraft, merchandise, or baggage seized under the provisions of this chapter, or who has incurred, or is alleged to have incurred, any fine or penalty thereunder, files with the Secretary of the Treasury if under the customs laws ... before the sale of such vessel, vehicle, aircraft, merchandise, or baggage a petition for the remission or mitigation of such fine, penalty, or forfeiture, the Secretary of the Treasury ... if he finds that such fine, penalty, or forfeiture was incurred without willful negligence or without any intention on the part of the petitioner to defraud the revenue or to violate the law, or finds the existence of such mitigating circumstances as to justify the remission or mitigation of such fine, penalty, or forfeiture, may remit or mitigate the same upon such terms and conditions as he deems reasonable and just, or order discontinuance of any prosecution relating thereto.”</p>
</footnote>
<footnote label="3">
<p id="b382-8"> The claimant may trigger the Government’s initiation of forfeiture proceedings. In <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#569" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S. 555, 569</a></span> (1983), we noted:</p>
<p id="AKp"><em>“A </em>claimant is able to trigger rapid filing of a forfeiture action if he desires it. First, the claimant can file an equitable action seeking an order compelling the filing of the forfeiture action or return of the seized property. See <em>Slocum </em>v. <em>Mayberry, </em><span class="citation" data-id="85171"><a href="/opinion/85171/slocum-v-mayberry/#10" aria-description="Citation for case: Slocum v. Mayberry">2 Wheat. 1, 10</a></span> (1817) (Marshall, C. J.). Less formally, the claimant could simply request that the Customs Service refer the matter to the United States Attorney. If the claimant believes the initial seizure was improper, he could file a motion under Federal Rule of Criminal Procedure 41(e) for a return of the seized property.”</p>
</footnote>
<footnote label="4">
<p id="b382-9"> When the Jaguar was seized in this case, a customs officer could have instituted nonjudicial, summary forfeiture proceedings if the value of the car had been not more than $10,000. See <span class="citation no-link">19 U. S. C. §§ 1607-1609</span>. Congress has since raised this limit to $100,000. <span class="citation no-link">19 U. S. C. § 1607</span> (1982 ed., <page-number citation-index="1" label="245">*245</page-number>Supp. III). Even for a seizure of property appraised at less than $100,000, the claimant has a right to a judicial determination upon posting a bond to cover costs in the sum of $2,500 or 10% of the value of the claimed property, whichever is smaller, but not less than $250. <span class="citation no-link">19 U. S. C. § 1608</span> (1982 ed., Supp. III).</p>
</footnote>
<footnote label="5">
<p id="b384-6"> The Secretary of the Treasury is authorized by statute to act on petitions for remission. <span class="citation no-link">19 U. S. C. § 1618</span>. This authority has been delegated to District Directors of the Customs Service in some cases where the total value of the merchandise forfeited does not exceed $100,000, <span class="citation no-link">19 CFR § 171.21</span> (1985). At the time of this seizure, the limit was $25,000. See <span class="citation no-link">19 CFR § 171.21</span> (1974).</p>
</footnote>
<footnote label="6">
<p id="b384-7"> The Government filed a contingent counterclaim seeking recovery of the full $24,500 in accordance with <span class="citation no-link">19 U. S. C. § 1497</span>, in the event the District Court found the mitigation invalid. Because the District Court entered judgment in favor of the Government on the merits of Von Neumann’s complaint, it denied the contingent counterclaim. In its answer in the District Court the Government had also contended that the remission and mitigation sought and received by respondent was a settle<page-number citation-index="1" label="247">*247</page-number>ment, accord, and satisfaction binding on Von Neumann. The District Court did not reach this issue; nor do we.</p>
</footnote>
<footnote label="7">
<p id="b387-2"> In <em>$8,850 </em>the claimant conceded that no preseizure hearing is required when Customs makes a seizure at the border. Respondent does not dispute that here, and we doubt that he could. In <em>$8,850 </em>we noted that while the general rule is that “absent an ‘extraordinary situation’ a party cannot invoke the power of the state to seize a person’s property without a <em>prior </em>judicial determination that the seizure is justified. . . . [D]ue process does not require federal customs officials to conduct a hearing before seizing items subject to forfeiture.” <span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 562, n. 12</a></span>. We reasoned that such a requirement would make customs processing entirely unworkable and also found that because “the seizure serves important governmental purposes[,] a preseizure notice might frustrate the statutory purpose ....” <em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">Ibid.</a></span></em></p>
</footnote>
<footnote label="8">
<p id="b387-3"> We noted in <em>$8,850 </em>that Customs processes over 50,000 noncontraband forfeitures per year, and that in 90% of all seizures, the claimant files a petition for remission or mitigation. We further noted that the Secretary <page-number citation-index="1" label="250">*250</page-number>in turn grants at least partial relief for an estimated 75% of the petitions. Typically, this mitigation process terminates the dispute without the necessity of filing a forfeiture action.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Wade.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Wade"
type: case
citation: "388 U.S. 218 (1967)"
parallel_cite: "87 S. Ct. 1926; 18 L. Ed. 2d 1149"
neutral_cite: 1967 U.S. LEXIS 1085
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Wade
  varies_by_point: false
  scope_note: "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107486/united-states-v-wade/"
  cluster_id: 107486
  opinion_id: 9423472
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Gilbert v. California]]", "[[Kirby v. Illinois]]", "[[United States v. Ash]]", "[[Stovall v. Denno]]"]
aliases: []
tags: ["case", "sixth-amendment", "eyewitness-identification", "lineup", "right-to-counsel", "critical-stage"]
holding: "A post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel; counsel's…"
lake:
  record_id: United States v. Wade
  status: verified
  projected_at: 2026-07-06
---

# United States v. Wade

*388 U.S. 218 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Wade was indicted for bank robbery and counsel was appointed. Without notifying counsel, an FBI agent had Wade and other prisoners stand in a lineup — wearing strips of tape on their faces and repeating words used by the robber — so two bank employees could identify him. At trial, the two employees identified Wade in the courtroom, and on cross-examination it emerged that they had also identified him at the lineup. Wade argued that the uncounseled lineup violated his Fifth and Sixth Amendment rights.

## Issue
Whether a post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel, and what remedy applies to an in-court identification that followed an uncounseled lineup.

## Rule
A post-indictment lineup is a critical stage at which the accused is entitled to counsel: "there can be little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was 'as much entitled to such aid [of counsel] . . . as at the trial itself.'" — 388 U.S. at 237. ^pin-237

The remedy is not automatic exclusion of the in-court identification; the in-court identification is admissible only if it has a source independent of the tainted lineup. The Court [[Reading and Citing Cases#vacated|vacated]] the conviction "pending a hearing to determine whether the in-court identifications had an independent source." — 388 U.S. at 242. ^pin-242

## Application
Wade had been indicted and had counsel when the FBI conducted the lineup without notifying his lawyer; the lineup was therefore an uncounseled critical stage, violating Wade's Sixth Amendment right. Because the two bank employees' in-court identifications might have been tainted by that lineup, the proper course was to vacate the conviction and remand so the District Court could determine whether those identifications rested on an [[Inevitable Discovery and Independent Source|independent source]] (or whether their admission was harmless).

## Conclusion
The post-indictment lineup was a critical stage requiring counsel; the judgment of the Court of Appeals was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to determine whether the in-court identifications had an [[Inevitable Discovery and Independent Source|independent source]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The right recognized in *Wade* was later **limited** by [[Kirby v. Illinois]] (the right to counsel attaches only after the initiation of adversary judicial proceedings — no counsel at pre-charge lineups) and by [[United States v. Ash]] (no right to counsel at a photographic array). Within its domain — post-charge corporeal lineups — *Wade* remains good law, alongside its companion [[Gilbert v. California]].

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *United States v. Wade*, 388 U.S. 218 (1967) — https://www.courtlistener.com/opinion/107486/united-states-v-wade/ — pinpoints: 237, 242 (parallel 87 S. Ct. 1926).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ffa92dd5e16ff62d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "388 U.S. 218 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 1085", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1926; 18 L. Ed. 2d 1149", "title": "United States v. Wade", "year": "1967"}}
{"assertion_id": "4fae79b835317ae8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel; counsel's…", "title": "United States v. Wade"}}
{"assertion_id": "7e896d9b4d21b500", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Anchor", "title": "United States v. Wade"}}
{"assertion_id": "083cad41e1cff401", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Wade", "field_i_validity": "good_law", "scope_note": "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays).", "title": "United States v. Wade", "varies_by_point": "false"}}
{"assertion_id": "b32096a3bc839bf7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Wade"}}
```

### lake record — United States v. Wade

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Wade",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Wade",
    "case_name_short": "Wade",
    "case_name_full": "United States v. Wade",
    "input_case_name": "United States v. Wade",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": null,
    "cluster_id": 107486,
    "lead_opinion_id": 9423472,
    "sibling_ids": [
      107486,
      9423472,
      9423473,
      9423474,
      9423475,
      9423476
    ],
    "absolute_url": "/opinion/107486/united-states-v-wade/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 218",
      "volume": "388",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1926",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1926",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1149",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1085",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 218",
        "volume": "388",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1926",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1926",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1149",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1085",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1085",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-237",
      "page": null,
      "quote": "--- # United States v. Wade *388 U.S. 218 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Wade was indicted for bank robbery and counsel was appointed. Without notifying counsel, an FBI agent had Wade and other prisoners stand in a lineup \u2014 wearing strips of tape on their faces and repeating words used by the robber \u2014 so two bank employees could identify him. At trial, the two employees identified Wade in the courtroom, and on cross-examination it emerged that they had also identified him at the lineup. Wade argued that the uncounseled lineup violated his Fifth and Sixth Amendment rights. ## Issue Whether a post-indictment lineup is a critical stage of the prosecution at which the accused has a Sixth Amendment right to counsel, and what remedy applies to an in-court identification that followed an uncounseled lineup. ## Rule A post-indictment lineup is a critical stage at which the accused is entitled to counsel:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-242",
      "page": null,
      "quote": "pending a hearing to determine whether the in-court identifications had an independent source.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Wade",
    "varies_by_point": false,
    "scope_note": "Right-to-counsel reach later limited by Kirby v. Illinois (post-charge only) and United States v. Ash (no counsel at photo arrays).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Red Kettle",
          "cluster_id": 4536563,
          "cite": [
            "2018 SD 66",
            "918 N.W.2d 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane1_negative"
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
        "journal_ref": "United States v. Wade:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dwight Smith",
          "cluster_id": 4452817,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane1_negative"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Rose",
          "cluster_id": 1769614,
          "cite": [
            "523 S.W.2d 930",
            "1975 Tenn. LEXIS 605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lafler v. Cooper",
          "cluster_id": 625833,
          "cite": [
            "182 L. Ed. 2d 398",
            "132 S. Ct. 1376",
            "566 U.S. 156",
            "2012 U.S. LEXIS 2322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harrington v. California",
          "cluster_id": 107952,
          "cite": [
            "23 L. Ed. 2d 284",
            "89 S. Ct. 1726",
            "395 U.S. 250",
            "1969 U.S. LEXIS 1435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
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
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Wade:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEwODc2ODAwMDAwJnM9NjIzOTE4NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU1JnM9MTEwMjMwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
        "reviewed": 68,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 68,
        "triage_read": 0,
        "triage_snippet_classified": 68
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107486 OR 9423472 OR 9423473 OR 9423474 OR 9423475 OR 9423476)",
    "indexed_citing_opinions": 5655,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107486,
        "count": 5272,
        "count_source": "search"
      },
      {
        "opinion_id": 9423472,
        "count": 545,
        "count_source": "search"
      },
      {
        "opinion_id": 9423473,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423474,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423475,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423476,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8444,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-wade.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNjQzNiZzPTEwMjcwNjI1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107486+OR+9423472+OR+9423473+OR+9423474+OR+9423475+OR+9423476%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107486,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107342,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 247981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 270482,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 271227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 273233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1143352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1176636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1192333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1512648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1550414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1748367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 1780007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2023100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2023137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2063045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2122471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2144553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2241740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2340930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2609203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 2619179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3416298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3484258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107486,
        "cited_id": 3609080,
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
    "date_created": "2026-07-06T03:26:40Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:30:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:27:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Wade

```
<opinion type="majority">
<author id="b255-11">Mr. Justice Brennan</author>
<p id="ARz">delivered the opinion of the Court.</p>
<p id="b255-12">The question here is whether courtroom identifications of an accused at trial are to be excluded from evidence because the accused was exhibited to the witnesses before trial at a post-indictment lineup conducted for <page-number citation-index="1" label="220">*220</page-number>identification purposes without notice to and in the absence of the accused’s appointed counsel.</p>
<p id="b256-5">The federally insured bank in Eustace, Texas, was robbed on September 21, 1964. A man with a small strip of tape on each side of his face entered the bank, pointed a pistol at the female cashier and the vice president, the only persons in the bank at the time, and forced them to fill a pillowcase with the bank’s money. The man then drove away with an accomplice who had been waiting in a stolen car outside the bank. On March 23, 1965, an indictment was returned against respondent, Wade, and two others for conspiring to rob the bank, and against Wade and the accomplice for the robbery itself. Wade was arrested on April 2, and counsel was appointed to represent him on April 26. Fifteen days later an FBI agent, without notice to Wade’s lawyer, arranged to have the two bank employees observe a lineup made up of Wade and five or six other prisoners and conducted in a courtroom of the local county courthouse. Each person in the line wore strips of tape such as allegedly worn by the robber and upon direction each said something like "put the money in the bag,” the words allegedly uttered by the robber. Both bank employees identified Wade in the lineup as the bank robber.</p>
<p id="b256-6">At trial, the two employees, when asked on direct examination if the robber was in the courtroom, pointed to Wade. The prior lineup identification was then elicited from both employees on cross-examination. At the close of testimony, Wade’s counsel moved for a judgment of acquittal or, alternatively, to strike the bank officials’ courtroom identifications on the ground that conduct of the lineup, without notice to and in the absence of his appointed counsel, violated his Fifth Amendment privilege against self-incrimination and his Sixth Amendment right to the assistance of counsel. The motion was denied, and Wade was convicted. The <page-number citation-index="1" label="221">*221</page-number>Court of Appeals for the Fifth Circuit reversed the conviction and ordered a new trial at which the in-court identification evidence was to be excluded, holding that, though the lineup did not violate Wade’s Fifth Amendment rights, “the lineup, held as it was, in the absence of counsel, already chosen to represent appellant, was a violation of his Sixth Amendment rights . . . .” <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#560" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d 557, 560</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./385/811/">385 U. S. 811</a></span>, and set the case for oral argument with No. 223, <em>Gilbert </em>v. <em>California, post, </em>p. 263, and No. 254, <em>Stovall </em>v. <em>Denno, post, </em>p. 293, which present similar questions. We reverse the judgment of the Court of Appeals and remand to that court with direction to enter a new judgment vacating the conviction and remanding the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b257-6">I.</p>
<p id="b257-7">Neither the lineup itself nor anything shown by this record that'Wade was required to do in the lineup violated his privilege against self-incrimination. We have only recently reaffirmed that the privilege “protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature ....” <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761</a></span>. We there held that compelling a suspect to submit to a withdrawal of a sample of his blood for analysis for alcohol content and the admission in evidence of the analysis report were not compulsion to those ends. That holding was supported by the opinion in <em>Holt </em>v. <em>United States, </em><span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>, in which case a question arose as to whether a blouse belonged to the defendant. A witness testified at trial that the defendant put on the blouse and it had fit him. The defendant argued that the admission of the testimony was error because compelling him to put on the blouse was a violation of his privilege. The Court <page-number citation-index="1" label="222">*222</page-number>rejected the claim as “an extravagant extension of the Fifth Amendment,” Mr. Justice Holmes saying for the Court:</p>
<blockquote id="b258-6">“[T]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S., at 252-253</a></span>.</blockquote>
<p id="b258-7">The Court in <em><span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">Holt</a></span>, </em>however, put aside any constitutional questions which might be involved in compelling an accused, as here, to exhibit himself before victims of or witnesses to an alleged crime; the Court stated, “we need not consider how far a court would go in compelling a man to exhibit himself.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#253" aria-description="Citation for case: Holt v. United States"><em>Id., </em>at 253</a></span>.<footnotemark>1</footnotemark></p>
<p id="b258-8">We have no doubt that compelling the accused merely to exhibit his person for observation by a prosecution witness prior to trial involves no compulsion of the accused to give evidence having testimonial significance. It is compulsion of the accused to exhibit his physical characteristics, not compulsion to disclose any knowledge he might have. It is no different from compelling Schmerber to provide a blood sample or Holt to wear the blouse, and, as in those instances, is not within the cover of the privilege. Similarly, compelling Wade to speak within hearing distance of the witnesses, even to utter words purportedly uttered by the robber, was not compulsion to utter statements of a “testimonial” nature; he was required to use his voice as an identifying <page-number citation-index="1" label="223">*223</page-number>physical characteristic, not to speak his guilt. We held in <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 761</a></span>, that the distinction to be drawn under the Fifth Amendment privilege against self-incrimination is one between an accused’s “communications” in whatever form, vocal or physical, and “compulsion which makes a suspect or accused the source of ‘real or physical evidence,’ ” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 764</a></span>. We recognized that “both federal and state courts have usually held that . . . [the privilege] offers no protection against compulsion to submit to' fingerprinting, photography, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><em>Id., </em>at 764</a></span>. None of these activities becomes testimonial within the scope of the privilege because required of the accused in a pretrial lineup.</p>
<p id="b259-5">Moreover, it deserves emphasis that this case presents no question of the admissibility in evidence of anything Wade said or did at the lineup which implicates his privilege. The Government offered no such evidence as part of its case, and what came out about the lineup proceedings on Wade’s cross-examination of the bank employees involved no violation of Wade’s privilege.</p>
<p id="b259-6">II.</p>
<p id="b259-7">The fact that the lineup involved no violation of Wade’s privilege against self-incrimination does not, however, dispose of his contention that the courtroom identifications should have been excluded because the lineup was conducted without notice to and in the absence of his counsel. Our rejection of the right to counsel claim in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>rested on our conclusion in that case that “[n]o issue of counsel’s ability to assist petitioner in respect of any rights he did possess is presented.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S., at 766</a></span>. In contrast, in this case it is urged that the assistance of counsel at the lineup was indispensable <page-number citation-index="1" label="224">*224</page-number>to protect Wade’s most basic right as a criminal defendant — his right- to a fair trial at which the witnesses against him might be meaningfully cross-examined.</p>
<p id="b260-4">The Framers of the Bill of Rights envisaged a broader role for counsel than under the practice then prevailing in England of merely advising his client in “matters of law,” and eschewing any responsibility for “matters of fact.” <footnotemark>2</footnotemark> The constitutions in at least 11 of the 13 States expressly or impliedly abolished this distinction. <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-65</a></span>; Note, 73 Yale L. J. 1000, 1030-1033 (1964). “Though the colonial provisions about counsel were in accord on few things, they agreed on the necessity of abolishing the facts-law distinction; the colonists appreciated that if a defendant were forced to stand alone against the state, his case was foredoomed.” 73 Yale L. <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#1033" aria-description="Citation for case: Billy Joe Wade v. United States">J., <em>supra, </em>at 1033-1034</a></span>. This background is reflected in the scope given by our decisions to the Sixth Amendment’s guarantee to an accused of the assistance of counsel for his defense. When the Bill of Rights was adopted, there were no organized police forces as we know them today.<footnotemark>3</footnotemark> The accused confronted the prosecutor and the witnesses against him, and the evidence was marshalled, largely at the trial itself. In contrast, today’s law enforcement machinery involves critical confrontations of the accused by the prosecution at pretrial proceedings where the results might well settle the accused’s fate and reduce the trial itself to a mere formality. In recognition of these realities of modern criminal prosecution, our cases have construed the Sixth Amendment guarantee to apply to “critical” stages of the proceedings. The guarantee reads: “In all criminal <page-number citation-index="1" label="225">*225</page-number>prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel <em>for his defence.” </em>(Emphasis supplied.) The plain wording of this guarantee thus encompasses counsel’s assistance whenever necessary to assure a meaningful “defence.”</p>
<p id="b261-5">As early as <em>Powell </em>v. <em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama, supra,</a></span> </em>we recognized that the period from arraignment to trial was “perhaps the most critical period of the proceedings . . . ,” <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama"><em>id., </em>at 57</a></span>, during which the accused “requires the guiding hand of counsel. . .,” <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama"><em>id., </em>at 69</a></span>, if the guarantee is not to prove an empty right. That principle has since been applied to require the assistance of counsel at the type of arraignment — for example, that provided by Alabama — where certain rights might be sacrificed or lost: “What happens there may affect the whole trial. Available defenses may be irretrievably lost, if not then and there asserted . . . .” <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/#54" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52, 54</a></span>. See <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>. The principle was also applied in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>, where we held that incriminating statements of the defendant should have been excluded from evidence when it appeared that they were overheard by federal agents who, without notice to the defendant’s lawyer, arranged a meeting between the defendant and an accomplice turned informant. We said, quoting a concurring opinion in <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 326</a></span>, that “[a]nything less . . . might deny a defendant ‘effective representation by counsel at the only stage when legal aid and advice would help him.’ ” <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#204" aria-description="Citation for case: Massiah v. United States">377 U. S., at 204</a></span>.</p>
<p id="b261-6">In <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, we drew upon the rationale of <em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">Hamilton</a></span> </em>and <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>in holding that the right to counsel was guaranteed at the point where the accused, prior to arraignment, was subjected to secret interrogation despite repeated requests to see his lawyer. We again noted the necessity of counsel’s pres<page-number citation-index="1" label="226">*226</page-number>ence if the accused was to have a fair opportunity to present a defense at the trial itself:</p>
<blockquote id="b262-6">“The rule sought by the State here, however, would make the trial no more than an appeal from the interrogation; and the ‘right to use counsel at the formal trial [would be] a very hollow thing [if], for all practical purposes, the conviction is already assured by pretrial examination’.... ‘One can imagine a cynical prosecutor saying: “Let them have the most illustrious counsel, now. They can’t escape the noose. There is nothing that counsel can do for them at the trial.” ’ ” <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#487" aria-description="Citation for case: Escobedo v. Illinois">378 U. S., at 487-488</a></span>.</blockquote>
<p id="b262-7">Finally in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the rules established for custodial interrogation included the right to the presence of counsel. The result was rested on our finding that this and the other rules were necessary to safeguard the privilege against self-incrimination from being jeopardized by such interrogation.</p>
<p id="b262-8">Of course, nothing decided or said in the opinions in the cited cases links the right to counsel only to protection of Fifth Amendment rights. Rather those decisions “no more than reflect a constitutional principle established as long ago as <em>Powell </em>v. <em>Alabama </em>. . . .” <em>Massiah </em>v. <em>United States, supra, </em>at 205. It is central to that principle that in addition to counsel’s presence at trial,<footnotemark>4</footnotemark> the accused is guaranteed that he need not stand alone against the State at any stage of the prosecution, formal or informal, in court or out, where counsel’s absence might derogate from the accused’s right to a fair trial.<footnotemark>5</footnotemark> The security of that right is as much the aim of the right to counsel as it is of the other guarantees of the <page-number citation-index="1" label="227">*227</page-number>Sixth Amendment — the right of the accused to a speedy and public trial by an impartial jury, his right to be informed of the nature and cause of the accusation, and his right to be confronted with the witnesses against him and to have compulsory process for obtaining witnesses in his favor. The presence of counsel at such critical confrontations, as at the trial itself, operates to assure that the accused’s interests will be protected consistently with our adversary theory of criminal prosecution. Cf. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>.</p>
<p id="b263-6">In sum, the principle of <em>Powell </em>v. <em>Alabama </em>and succeeding cases requires that we scrutinize <em>any </em>pretrial confrontation of the accused to determine whether the presence of his counsel is necessary to preserve the defendant’s basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself. It calls upon us to analyze whether potential substantial prejudice to defendant’s rights inheres in the particular confrontation and the ability of counsel to help avoid that prejudice.</p>
<p id="b263-7">III.</p>
<p id="b263-8">The Government characterizes the lineup as a mere preparatory step in the gathering of the prosecution’s evidence, not different — for Sixth Amendment purposes — from various other preparatory steps, such as systematized or scientific analyzing of the accused’s fingerprints, blood sample, clothing, hair, and the like. We think there are differences which preclude such stages being characterized as critical stages at which the accused has the right to the presence of his counsel. Knowledge of the techniques of science and technology is sufficiently available, and the variables in techniques few enough, that the accused has the opportunity for a meaningful confrontation of the Government’s case at <page-number citation-index="1" label="228">*228</page-number>trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts. The denial of a right to have his counsel present at such analyses does not therefore violate the Sixth Amendment; they are not critical stages since there is minimal risk that his counsel's absence at such stages might derogate from his right to a fair trial.</p>
<p id="b264-5">IV.</p>
<p id="b264-6">But the confrontation compelled by the State between the accused and the victim or witnesses to a crime to elicit identification evidence is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial. The vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification.<footnotemark>6</footnotemark> Mr. Justice Frankfurter once said: “What is the worth of identification testimony even when uncontradicted? The identification of strangers is proverbially untrustworthy. The hazards of such testimony are established by a formidable number of instances in the records of English and American trials. These instances are recent — not due to the brutalities of ancient criminal procedure.” The Case of Sacco and Vanzetti 30 (1927). A major factor contributing to the high incidence of miscarriage of justice from mistaken identification has been the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification. A commenta<page-number citation-index="1" label="229">*229</page-number>tor has observed that “[t]he influence of improper suggestion upon identifying witnesses probably accounts for more miscarriages of justice than any other single factor — ■ perhaps it is responsible for more such errors than all other factors combined.” Wall, Eye-Witness Identification in Criminal Cases 26. Suggestion can be created intentionally or unintentionally in many subtle ways.<footnotemark>7</footnotemark> And the dangers for the suspect are particularly grave when the witness’ opportunity for observation was insubstantial, and thus his susceptibility to suggestion the greatest.</p>
<p id="b265-5">Moreover, “[i]t is a matter of common experience that, once a witness has picked out the accused at the line-up, he is not likely to go back on his word later on, so that in practice the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial.” <footnotemark>8</footnotemark></p>
<p id="b265-6">The pretrial confrontation for purpose of identification may take the form of a lineup, also known as an “identification parade” or “showup,” as in the present case, or presentation of the suspect alone to the witness, as in <em>Stovall </em>v. <em>Denno, supra. </em>It is obvious that risks of suggestion attend either form of confrontation and increase the dangers inhering in eyewitness identification.<footnotemark>9</footnotemark> But <page-number citation-index="1" label="230">*230</page-number>as is the case with secret interrogations, there is serious difficulty in depicting what transpires at lineups and other forms of identification confrontations. “Privacy results in secrecy and this in turn results in a gap in our knowledge as to what in fact goes on . . . .” <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#448" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 448</a></span>. For the same reasons, the defense can seldom reconstruct the manner and mode of lineup identification for judge or jury at trial. Those participating in a lineup with the accused may often be police officers;<footnotemark>10</footnotemark> in any event, the participants’ names are rarely recorded or divulged at trial.<footnotemark>11</footnotemark> The impediments to an objective observation are increased when the victim is the witness. Lineups are prevalent in rape and robbery prosecutions and present a particular hazard that a victim’s understandable outrage may excite vengeful or spiteful motives.<footnotemark>12</footnotemark> In any event, neither witnesses nor lineup participants are apt to be alert for conditions prejudicial to the suspect. And if they were, it would likely be of scant benefit to the suspect since neither witnesses nor lineup participants are likely to be schooled in the detection of suggestive influences.<footnotemark>13</footnotemark> Improper in<page-number citation-index="1" label="231">*231</page-number>fluences may go undetected by a suspect, guilty or not, who experiences the emotional tension which we might expect in one being confronted with potential accusers.<footnotemark>14</footnotemark> Even when he does observe abuse, if he has a criminal record he may be reluctant to take the stand and open up the admission of prior convictions. Moreover, any protestations by the suspect of the fairness of the lineup made at trial are likely to be in vain;<footnotemark>15</footnotemark> the jury’s choice is between the accused’s unsupported version and that of the police officers present.<footnotemark>16</footnotemark> In short, the accused’s <page-number citation-index="1" label="232">*232</page-number>inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness’ courtroom identification.</p>
<p id="b268-6">What facts have been disclosed in specific cases about the conduct of pretrial confrontations for identification illustrate both the potential for substantial prejudice to the accused at that stage and the need for its revelation at trial. A commentator provides some striking examples:</p>
<blockquote id="b268-7">“In a Canadian case . . . the defendant had been picked out of a line-up of six men, of which he was the only Oriental. In other cases, a black-haired suspect was placed among a group of light-haired persons, tall suspects have been made to stand with short non-suspects, and, in a case where the perpetrator of the crime was known to be a youth, a suspect under twenty was placed in a line-up with five other persons, all of whom were forty or over.” <footnotemark>17</footnotemark></blockquote>
<p id="b268-8">Similarly state reports, in the course of describing prior identifications admitted as evidence of guilt, reveal <page-number citation-index="1" label="233">*233</page-number>numerous instances of suggestive procedures, for example, that all in the lineup but the suspect were known to the identifying witness,<footnotemark>18</footnotemark> that the other participants in a lineup were grossly dissimilar in appearance to the suspect,<footnotemark>19</footnotemark> that only the suspect was required to wear distinctive clothing which the culprit allegedly wore,<footnotemark>20</footnotemark> that the witness is told by the police that they have caught the culprit after which the defendant is brought before the witness alone or is viewed in jail,<footnotemark>21</footnotemark> that the suspect is pointed out before or during a lineup,<footnotemark>22</footnotemark> and that the participants in the lineup are asked to try on an article of clothing which fits only the suspect.<footnotemark>23</footnotemark></p>
<p id="b269-5">The potential for improper influence is illustrated by the circumstances, insofar as they appear, surrounding the prior identifications in the three cases we decide today. In the present case, the testimony of the identi<page-number citation-index="1" label="234">*234</page-number>fying witnesses elicited on cross-examination revealed that those witnesses were taken to the courthouse and seated in the courtroom to await assembly of the lineup. The courtroom faced on a hallway observable to the witnesses through an open door. The cashier testified that she saw Wade “standing in the hall” within sight of an FBI agent. Five or six other prisoners later appeared in the hall. The vice president testified that he saw a person in the hall in the custody of the agent who “resembled the person that we identified as the one that had entered the bank.” <footnotemark>24</footnotemark></p>
<p id="b270-6">The lineup in <em>Gilbert, supra, </em>was conducted in an auditorium in which some 100 witnesses to several alleged state and federal robberies charged to Gilbert made wholesale identifications of Gilbert as the robber in each other’s presence, a procedure said to be fraught with dangers of suggestion.<footnotemark>25</footnotemark> And the vice of suggestion created by the identification in <em>Stovall, supra, </em>was the presentation to the witness of the suspect alone handcuffed to police officers. It is hard to imagine a situation more clearly conveying the suggestion to the witness that the one presented is believed guilty by the police. See Frankfurter, The Case of Sacco and Vanzetti 31-32.</p>
<p id="b270-7">The few cases that have surfaced therefore reveal the existence of a process attended with hazards of serious unfairness to the criminal accused and strongly suggest the plight of the more numerous defendants who are unable to ferret out suggestive influences in the <page-number citation-index="1" label="235">*235</page-number>secrecy of the confrontation. We do not assume that these risks are the result of police procedures intentionally designed to prejudice an accused. Rather we assume they derive from the dangers inherent in eyewitness identification and the suggestibility inherent in the context of the pretrial identification. Williams &amp; Hammelmann, in one of the most comprehensive studies of such forms of identification, said, “[T]he fact that the police themselves have, in a given case, little or no doubt that the man put up for identification has committed the offense, and that their chief pre-occupation is with the problem of getting sufficient proof, because he has not 'come clean,’ involves a danger that this persuasion may communicate itself even in a doubtful case to the witness in some way . . . .” Identification Parades, Part I, [1963] Crim. L. Rev. 479, 483.</p>
<p id="b271-5">Insofar as the accused’s conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him. <em>Pointer </em>v. <em>Texas, </em><span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. And even though cross-examination is a precious safeguard to a fair trial, it cannot be viewed as an absolute assurance of accuracy and reliability. Thus in the present context, where so many variables and pitfalls exist, the first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused’s fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no <page-number citation-index="1" label="236">*236</page-number>effective appeal from the judgment there rendered by the witness — “that’s the man.”</p>
<p id="b272-6">Since it appears that there is grave potential for prejudice, intentional or not, in the pretrial lineup, which may not be capable of reconstruction at trial, and since presence of counsel itself can often avert prejudice and assure a meaningful confrontation at trial,<footnotemark>26</footnotemark> there can be <page-number citation-index="1" label="237">*237</page-number>little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was “as much entitled to such aid [of counsel] ... as at the trial itself.” <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span>. Thus both Wade and his counsel should have been notified of the impending lineup, and counsel’s presence should have been a requisite to conduct of the lineup, absent an “intelligent waiver.” See <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span>. No substantial countervailing policy considerations have been advanced against the requirement of the presence of counsel. Concern is expressed that the requirement will forestall prompt identifications and result in obstruction of the confrontations. As for the first, we note that in the two cases in which the right to counsel is today held to apply, counsel had already been appointed and no argument is made in either case that notice to counsel would have prejudicially delayed the confrontations. Moreover, we leave open the question whether the presence of substitute counsel might not suffice where notification and presence of the suspect’s own counsel would result in prejudicial delay.<footnotemark>27</footnotemark> And to refuse to recognize the right to counsel for fear that counsel will obstruct the course of justice is contrary to the <page-number citation-index="1" label="238">*238</page-number>basic assumptions upon which this Court has operated in Sixth Amendment cases. We rejected similar logic in <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span> </em>concerning presence of counsel during custodial interrogation, 384 U. S., at 480-481:</p>
<blockquote id="b274-4">“[A]n attorney is merely exercising the good professional judgment he has been taught. This is not cause for considering the attorney a menace to law enforcement. He is merely carrying out what he is sworn to do under his oath — to protect to the extent of his ability the rights of his client. In fulfilling this responsibility the attorney plays a vital role in the administration of criminal justice under our Constitution.”</blockquote>
<p id="b274-5">In our view counsel can hardly impede legitimate law enforcement; on the contrary, for the reasons expressed, law enforcement may be assisted by preventing the infiltration, of taint in the prosecution’s identification evidence.<footnotemark>28</footnotemark> That result cannot help the guilty avoid conviction but can only help assure that the right man has been brought to justice.<footnotemark>29</footnotemark></p>
<p id="b275-3"><page-number citation-index="1" label="239">*239</page-number>Legislative or other regulations, such as those of local police departments, which eliminate the risks of abuse and unintentional suggestion at lineup proceedings and the impediments to meaningful confrontation at trial may also remove the basis for regarding the stage as “critical.”<footnotemark>30</footnotemark> But neither Congress nor the federal authorities have seen fit to provide a solution. What we hold today “in no way creates a constitutional straitjacket which will handicap sound efforts at reform, nor is it intended to have this effect.” <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 467</a></span>.</p>
<p id="b275-4">V.</p>
<p id="b275-5">We come now to the question whether the denial of Wade’s motion to strike the courtroom identification by the bank witnesses at trial because of the absence of his counsel at the lineup required, as the Court of Appeals held, the grant of a new trial at which such evidence is <page-number citation-index="1" label="240">*240</page-number>to be excluded. We do not think this disposition can be justified without first giving the Government the opportunity to establish by clear and convincing evidence that the in-court identifications were based upon observations of the suspect other than the lineup identification. See <em>Murphy </em>v. <em>Waterfront Commission, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#79" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 79, n. 18</a></span>.<footnotemark>31</footnotemark> Where, as here, the admissibility of evidence of the lineup identification itself is not involved, a <em>per se </em>rule of exclusion of courtroom identification would be unjustified.<footnotemark>32</footnotemark> See <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>. A rule limited solely to the exclusion of testimony concerning identification at the lineup itself, without regard to admissibility of the courtroom identification, would render the right to counsel an empty one. The lineup is most often used, as in the present case, to crystallize the witnesses’ identification of the defendant for future reference. We have already noted that the lineup identification will have that effect. The State may then rest upon the witnesses’ unequivocal courtroom identification, and not mention the pretrial identification as part of the State’s case at trial. Counsel is then in the predicament in which Wade’s counsel found himself — realizing that possible unfairness at the lineup may be the sole means of attack upon the unequivocal courtroom identification, and having to probe in the dark <page-number citation-index="1" label="241">*241</page-number>in an attempt to discover and reveal unfairness, whde bolstering the government witness’ courtroom identification by bringing out and dwelling upon his prior identification. Since counsel’s presence at the lineup would equip him to attack not only the lineup identification but the courtroom identification as well, limiting the impact of violation of the right to counsel to exclusion of evidence only of identification at the lineup itself disregards a critical element of that right.</p>
<p id="b277-3">We think it follows that the proper test to be applied in these situations is that quoted in <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>, “ ‘[W]hether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint." Maguire, Evidence of Guilt 221 (1959).” See also <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#309" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 309</a></span>. Application of this test in the present context requires consideration of various factors; for example, the prior opportunity to observe the alleged criminal act, the existence of any discrepancy between any pre-lineup description and the defendant’s actual description, any identification prior to lineup of another person, the identification by picture of the defendant prior to the lineup, failure to identify the defendant on a prior occasion, and the lapse of time between the alleged act and the lineup identification. It is also relevant to consider those facts which, despite the absence of counsel, are disclosed concerning the conduct of the lineup.<footnotemark>33</footnotemark></p>
<p id="b278-4"><page-number citation-index="1" label="242">*242</page-number>We doubt that the Court of Appeals applied the prop'er test for exclusion of the in-court identification of the two witnesses. The court stated that “it cannot be said with any certainty that they would have recognized appellant at the time of trial if this intervening lineup had not occurred,” and that the testimony of the two witnesses “may well have been colored by the illegal procedure [and] was prejudicial.” <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/#560" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d, at 560</a></span>. Moreover, the court was persuaded, in part, by the “compulsory verbal responses made by Wade at the instance of the Special Agent.” <em><span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/" aria-description="Citation for case: Billy Joe Wade v. United States">Ibid.</a></span> </em>This implies the erroneous holding that Wade’s privilege against self-incrimination was violated so that the denial of counsel required exclusion.</p>
<p id="b278-5">On the record now before us we cannot make the determination whether the in-court identifications had an independent origin. This was not an issue at trial, although there is some evidence relevant to a determination. That inquiry is most properly made in the District Court. We therefore think the appropriate procedure to be followed is to vacate the conviction pending a hearing to determine whether the in-court identifications had an independent source, or whether, in any event, the introduction of the evidence was harmless error, <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, and for the District Court to reinstate the conviction or order a new trial, as may be proper. See <em>United States </em>v. <em>Shotwell Mfg. Co., </em><span class="citation" data-id="9421525"><a href="/opinion/105597/united-states-v-shotwell-manufacturing-co/#245" aria-description="Citation for case: United States v. Shotwell Manufacturing Co.">355 U. S. 233, 245-246</a></span>.</p>
<p id="b279-4"><page-number citation-index="1" label="243">*243</page-number>The judgment of the Court of Appeals is vacated and the case is remanded to that court with direction to enter a new judgment vacating the conviction and remanding the case to the District Court for further proceedings consistent with this opinion.</p>
<p id="b279-5">
<em>It is so ordered.</em>
</p>
<judges id="b279-6">The Chief Justice joins the opinion of the Court except for Part I, from which he dissents for the reasons expressed in the opinion of Mr. Justice Foutas.</judges>
<judges id="b279-7">Mr. Justice Douglas joins the opinion of the Court except for Part I. On that phase of the case he adheres to the dissenting views in <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#772" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 772-779</a></span>, since he believes that compulsory lineup violates the privilege against self-incrimination contained in the Fifth Amendment.</judges>
<footnote label="1">
<p id="b258-9"><em> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">Holt</a></span> </em>was decided before <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, fashioned the rule excluding illegally obtained evidence in a federal prosecution. The Court therefore followed <em>Adams </em>v. <em>New York, </em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. <em>585, </em></a></span>in holding that, in any event, “when he is exhibited, whether voluntarily or by order, and even if the order goes too far, the evidence, if material,'is competent.” <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#253" aria-description="Citation for case: Holt v. United States">218 U. S., at 253</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b260-5"> See <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#60" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 60-65</a></span>; Beaney, Right to Counsel in American Courts 8-26.</p>
</footnote>
<footnote label="3">
<p id="b260-6"> See Note, 73 Yale L. J. 1000, 1040-1042 (1964); Comment, <span class="citation no-link">53 Calif. L. Rev. 337</span>, 347-348 (1965).</p>
</footnote>
<footnote label="4">
<p id="b262-9"> See, <em>e. g., Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>; <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <em>White </em>v. <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland"><em>Maryland, 373 </em>U. S. 59</a></span>; <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>; <em>Massiah </em>v. <em>United States, 377 </em>U. S. 201.</p>
</footnote>
<footnote label="5">
<p id="b262-10"> See cases cited n. 4, <em>supra; Avery </em>v. <em>Alabama, </em><span class="citation" data-id="103272"><a href="/opinion/103272/avery-v-alabama/#446" aria-description="Citation for case: Avery v. Alabama">308 U. S. 444, 446</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b264-7"> Borchard, Convicting the Innocent; Frank &amp; Frank, Not Guilty; Wall, Eye-Witness Identification in Criminal Cases; 3 Wigmore, Evidence § 786a (3d ed. 1940); Rolph, Personal Identity; Gross, Criminal Investigation 47-54 (Jackson ed. 1962); Williams, Proof of Guilt 83-98 (1955); Wills, Circumstantial Evidence 192-205 (7th ed. 1937); Wigmore, The Science of Judicial Proof §§ 250-253 (3d ed. 1937).</p>
</footnote>
<footnote label="7">
<p id="b265-7"> See Wall, <em>supra, </em>n. 6, at 26-65; Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>; Napley, Problems of Effecting the Presentation of the Case for a Defendant, 66 Col. L. Rev. 94, 98-99 (1966); Williams, Identification Parades, [1955] Crim. L. Rev. (Eng.) 525; Paul, Identification of Accused Persons, 12 Austl. L. J. 42 (1938); Houts, From Evidence to Proof 25; Williams &amp; Hammelmann, Identification Parades, Parts I &amp; II, [1963] Crim. L. Rev. 479-490, 545-555; Gorphe, Showing Prisoners to Witnesses for Identification, 1 Am. J. Police Sci. 79 (1930); Wigmore, The Science of Judicial Proof, <em>supra, </em>n. 6, at §253; Devlin, The Criminal Prosecution in England 70; Williams, Proof of Guilt 95-97.</p>
</footnote>
<footnote label="8">
<p id="b265-8"> Williams &amp; Hammelmann, Identification Parades, Part I, [1963] Crim. L. Rev. 479, 482.</p>
</footnote>
<footnote label="9">
<p id="b265-9"> Williams &amp; Hammelmann, Identification Parades, Part <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#7" aria-description="Citation for case: Escobedo v. Illinois">I, <em>supra, </em>n. 7</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b266-6"> See Wall, <em>supra, </em>n. 6, at 57-59; see, <em>e. g., People </em>v. <em>Boney, </em><span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">28 Ill. 2d 505</a></span>, <span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">192 N. E. 2d 920</a></span> (1963); <em>People </em>v. <em>James, </em><span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/" aria-description="Citation for case: People v. James">218 Cal. App. 2d 166</a></span>, <span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/" aria-description="Citation for case: People v. James">32 Cal. Rptr. 283</a></span> (1963).</p>
</footnote>
<footnote label="11">
<p id="b266-7"> See Rolph, Personal Identity 50: “The bright burden of identity, at these parades, is lifted from the innocent participants to hover about the suspect, leaving the rest featureless and unknown and without interest.”</p>
</footnote>
<footnote label="12">
<p id="b266-8"> See Williams &amp; Hammelmann, Identification Parades, Part II, [1963] Crim. L. Rev. 545, 546; Borchard, Convicting the Innocent 367.</p>
</footnote>
<footnote label="13">
<p id="b266-9"> An additional impediment to the detection of such influences by participants, including the suspect, is the physical conditions often surrounding the conduct of the lineup. In many, lights shine on the stage in such a way that the suspect cannot see the witness. See <em>Gilbert </em>v. <em>United States, </em><span class="citation" data-id="9452205"><a href="/opinion/273233/jesse-james-gilbert-v-united-states/" aria-description="Citation for case: Jesse James Gilbert v. United States">366 F. 2d 923</a></span> (C. A. 9th Cir. 1966). In some a one-way mirror is used and what is said on the witness’ <page-number citation-index="1" label="231">*231</page-number>side cannot be heard. See <em>Rigney </em>v. <em>Hendrick, </em><span class="citation" data-id="8874911"><a href="/opinion/8888781/rigney-v-hendrick/#711" aria-description="Citation for case: Rigney v. Hendrick">355 F. 2d 710, 711, n. 2</a></span> (C. A. 3d Cir. 1965); <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">273 Ala. 337</a></span>, <span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">139 So. 2d 309</a></span> (1961).</p>
</footnote>
<footnote label="14">
<p id="b267-6"> Williams &amp; Hammelmann, Part <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#7" aria-description="Citation for case: Escobedo v. Illinois">I, <em>supra, </em>n. 7</a></span>, at 489; Napley, <em>supra, </em>n. 7, at 99.</p>
</footnote>
<footnote label="15">
<p id="b267-7"> See <em>In re Groban, </em><span class="citation" data-id="9421372"><a href="/opinion/105449/in-re-groban/#340" aria-description="Citation for case: In Re Groban">352 U. S. 330, 340</a></span> (Black, J., dissenting). The difficult position of defendants in attempting to protest the manner of pretrial identification is illustrated by the many state court eases in which contentions of blatant abuse rested on their unsupportable allegations, usually controverted by the police officers present. See, e. <em>g., People </em>v. <em>Shields, </em><span class="citation" data-id="1170096"><a href="/opinion/1170096/people-v-shields/#634" aria-description="Citation for case: People v. Shields">70 Cal. App. 2d 628, 634-635</a></span>, <span class="citation" data-id="1170096"><a href="/opinion/1170096/people-v-shields/#478" aria-description="Citation for case: People v. Shields">161 P. 2d 475, 478-479</a></span> (1945); <em>People </em>v. <em>Hicks, </em><span class="citation" data-id="2122471"><a href="/opinion/2122471/the-people-v-hicks/" aria-description="Citation for case: The People v. Hicks">22 Ill. 2d 364</a></span>, <span class="citation" data-id="2122471"><a href="/opinion/2122471/the-people-v-hicks/" aria-description="Citation for case: The People v. Hicks">176 N. E. 2d 810</a></span> (1961); <em>State </em>v. <em>Hill, </em><span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">193 Kan. 512</a></span>, <span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">394 P. 2d 106</a></span> (1964); <em>Redmon </em>v. <em>Commonwealth, </em><span class="citation" data-id="2371331"><a href="/opinion/2371331/redmon-v-commonwealth/" aria-description="Citation for case: Redmon v. Commonwealth">321 S. W. 2d 397</a></span> (Ky. Ct. App. 1959); <em>Lubinski </em>v. <em>State, </em><span class="citation" data-id="3484258"><a href="/opinion/3486372/lubinski-v-state/#8" aria-description="Citation for case: Lubinski v. State">180 Md. 1, 8</a></span>, <span class="citation" data-id="3484258"><a href="/opinion/3486372/lubinski-v-state/#459" aria-description="Citation for case: Lubinski v. State">22 A. 2d 455, 459</a></span> (1941). For a striking case in which hardly anyone agreed upon what occurred at the lineup, including who identified whom, see <em>Johnson </em>v. <em>State, </em><span class="citation" data-id="1512648"><a href="/opinion/1512648/johnson-v-state/" aria-description="Citation for case: Johnson v. State">237 Md. 283</a></span>, <span class="citation" data-id="1512648"><a href="/opinion/1512648/johnson-v-state/" aria-description="Citation for case: Johnson v. State">206 A. 2d 138</a></span> (1965).</p>
</footnote>
<footnote label="16">
<p id="b267-8"> An instructive example of the defendant’s predicament may be found in <em>Proctor </em>v. <em>State, </em><span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/" aria-description="Citation for case: Proctor v. State">223 Md. 394</a></span>, <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/" aria-description="Citation for case: Proctor v. State">164 A. 2d 708</a></span> (1960). A prior identification is admissible in Maryland only under the salutary rule that it cannot have been made “under conditions of unfairness or unreliability.” <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/#401" aria-description="Citation for case: Proctor v. State"><em>Id., </em>at 401</a></span>, <span class="citation" data-id="1550414"><a href="/opinion/1550414/proctor-v-state/#712" aria-description="Citation for case: Proctor v. State">164 A. 2d, at 712</a></span>. Against the defendant’s contention that these conditions had not been met, the Court stated:</p>
<blockquote id="b267-9">“In the instant case, there are no such facts as, in our judgment, would call for a finding that the identification . . . was made under conditions of unfairness or unreliability. The relatively large number of persons put into the room together for [the victim] to look at <page-number citation-index="1" label="232">*232</page-number>is one circumstance indicating fairness, and the fact that the police officer was unable to remember the appearances of the others and could not recall if they had physical characteristics similar to [the defendant’s] or not is at least suggestive that they were not of any one type or that they all differed markedly in looks from the defendant. There is no evidence that the Police Sergeant gave the complaining witness any indication as to which of the thirteen men was the defendant; the Sergeant’s testimony is simply that he asked [the victim] if he could identify [the defendant] after having put the thirteen men in the courtroom.”</blockquote>
</footnote>
<footnote label="17">
<p id="b268-10"> Wall, Eye-Witness Identification in Criminal Cases 53. For other such examples see Houts, From Evidence to Proof 25; Frankfurter, The Case of Sacco and Vanzetti 12-14, 30-32; 3 Wigmore, Evidence § 786a, at 164, n. 2 (3d ed. 1940); Paul, Identification of Accused Persons, 12 Austl. L. J. 42, 44 (1938); Rolph, Personal Identity 34-43.</p>
</footnote>
<footnote label="18">
<p id="b269-6"> See <em>People </em>v. <em>James, </em><span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/#170" aria-description="Citation for case: People v. James">218 Cal. App. 2d 166, 170-171</a></span>, <span class="citation" data-id="2215593"><a href="/opinion/2215593/people-v-james/#286" aria-description="Citation for case: People v. James">32 Cal. Rptr. 283, 286</a></span> (1963); <em>People </em>v. <em>Boney, </em><span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">28 Ill. 2d 505</a></span>, <span class="citation" data-id="2023100"><a href="/opinion/2023100/the-people-v-boney/" aria-description="Citation for case: The People v. Boney">192 N. E. 2d 920</a></span> (1963).</p>
</footnote>
<footnote label="19">
<p id="b269-9"> See <em>Fredericksen </em>v. <em>United States, </em>105 U. S. App. D. C. 262, <span class="citation" data-id="247981"><a href="/opinion/247981/charles-d-fredericksen-v-united-states/" aria-description="Citation for case: Charles D. Fredericksen v. United States">266 F. 2d 463</a></span> (1959); <em>People </em>v. <em>Adell, </em><span class="citation" data-id="2144553"><a href="/opinion/2144553/people-v-adell/" aria-description="Citation for case: People v. Adell">75 Ill. App. 2d 385</a></span>, <span class="citation" data-id="2144553"><a href="/opinion/2144553/people-v-adell/" aria-description="Citation for case: People v. Adell">221 N. E. 2d 72</a></span> (1966); <em>State </em>v. <em>Hill, </em><span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">193 Kan. 512</a></span>, <span class="citation" data-id="9794721"><a href="/opinion/2619179/state-v-hill/" aria-description="Citation for case: State v. Hill">394 P. 2d 106</a></span> (1964); <em>People </em>v. <em>Seppi, </em><span class="citation" data-id="3609080"><a href="/opinion/3626126/people-v-seppi/" aria-description="Citation for case: People v. . Seppi">221 N. Y. 62</a></span>, <span class="citation" data-id="3609080"><a href="/opinion/3626126/people-v-seppi/" aria-description="Citation for case: People v. . Seppi">116 N. E. 793</a></span> (1917); <em>State </em>v. <em>Duggan, </em><span class="citation" data-id="1299385"><a href="/opinion/1299385/state-v-duggan/#162" aria-description="Citation for case: State v. Duggan">215 Ore. 151, 162</a></span>, <span class="citation" data-id="1299385"><a href="/opinion/1299385/state-v-duggan/#912" aria-description="Citation for case: State v. Duggan">333 P. 2d 907, 912</a></span> (1958).</p>
</footnote>
<footnote label="20">
<p id="b269-10"> See <em>People </em>v. <em>Crenshaw, </em><span class="citation" data-id="2063045"><a href="/opinion/2063045/the-people-v-crenshaw/#460" aria-description="Citation for case: The PEOPLE v. Crenshaw">15 Ill. 2d 458, 460</a></span>, <span class="citation" data-id="2063045"><a href="/opinion/2063045/the-people-v-crenshaw/#602" aria-description="Citation for case: The PEOPLE v. Crenshaw">155 N. E. 2d 599, 602</a></span> (1959); <em>Presley </em>v. <em>State, </em><span class="citation" data-id="2340930"><a href="/opinion/2340930/presley-v-state/" aria-description="Citation for case: Presley v. State">224 Md. 550</a></span>, <span class="citation" data-id="2340930"><a href="/opinion/2340930/presley-v-state/" aria-description="Citation for case: Presley v. State">168 A. 2d 510</a></span> (1961); <em>State </em>v. <em>Ramirez, </em>76 N. M. 72, <span class="citation" data-id="1176636"><a href="/opinion/1176636/state-v-ramirez/" aria-description="Citation for case: State v. Ramirez">412 P. 2d 246</a></span> (1966); <em>State </em>v. <em>Bazemore, </em><span class="citation" data-id="3674765"><a href="/opinion/3928137/state-v-bazemore/" aria-description="Citation for case: State v. . Bazemore">193 N. C. 336</a></span>, <span class="citation no-link">137 S. E. 172</span> (1927); <em>Barrett </em>v. <em>State, </em><span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">190 Tenn. 366</a></span>, <span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">229 S. W. 2d 516</a></span> (1950).</p>
</footnote>
<footnote label="21">
<p id="b269-14"> See <em>Aaron </em>v. <em>State, </em><span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">273 Ala. 337</a></span>, <span class="citation" data-id="1143352"><a href="/opinion/1143352/aaron-v-state/" aria-description="Citation for case: Aaron v. State">139 So. 2d 309</a></span> (1961); <em>Bishop </em>v. <em>State, </em><span class="citation" data-id="1748367"><a href="/opinion/1748367/bishop-v-state/" aria-description="Citation for case: Bishop v. State">236 Ark. 12</a></span>, <span class="citation" data-id="1748367"><a href="/opinion/1748367/bishop-v-state/" aria-description="Citation for case: Bishop v. State">364 S. W. 2d 676</a></span> (1963); <em>People </em>v. <em>Thompson, </em><span class="citation" data-id="2241740"><a href="/opinion/2241740/people-v-thompson/" aria-description="Citation for case: People v. Thompson">406 Ill. 555</a></span>, <span class="citation" data-id="2241740"><a href="/opinion/2241740/people-v-thompson/" aria-description="Citation for case: People v. Thompson">94 N. E. 2d 349</a></span> (1950); <em>People </em>v. <em>Berne, </em><span class="citation" data-id="3416298"><a href="/opinion/3419836/the-people-v-berne/" aria-description="Citation for case: The People v. Berne">384 Ill. 334</a></span>, <span class="citation" data-id="3416298"><a href="/opinion/3419836/the-people-v-berne/" aria-description="Citation for case: The People v. Berne">51 N. E. 2d 578</a></span> (1943); <em>People </em>v. <em>Martin, </em><span class="citation" data-id="6980660"><a href="/opinion/7075921/people-v-martin/" aria-description="Citation for case: People v. Martin">304 Ill. 494</a></span>, <span class="citation" data-id="6980660"><a href="/opinion/7075921/people-v-martin/" aria-description="Citation for case: People v. Martin">136 N. E. 711</a></span> (1922); <em>Barrett </em>v. <em>State, </em><span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">190 Tenn. 366</a></span>, <span class="citation" data-id="1780007"><a href="/opinion/1780007/barrett-v-state/" aria-description="Citation for case: Barrett v. State">229 S. W. 2d 516</a></span> (1950).</p>
</footnote>
<footnote label="22">
<p id="b269-15"> See <em>People </em>v. <em>Clark, </em><span class="citation" data-id="2023137"><a href="/opinion/2023137/the-people-v-clark/" aria-description="Citation for case: The PEOPLE v. Clark">28 Ill. 2d 423</a></span>, <span class="citation" data-id="2023137"><a href="/opinion/2023137/the-people-v-clark/" aria-description="Citation for case: The PEOPLE v. Clark">192 N. E. 2d 851</a></span> (1963); <em>Gillespie </em>v. <em>State, </em><span class="citation" data-id="1192333"><a href="/opinion/1192333/gillespie-v-state/#454" aria-description="Citation for case: Gillespie v. State">355 P. 2d 451, 454</a></span> (Okla. Cr. 1960).</p>
</footnote>
<footnote label="23">
<p id="b269-16"> See <em>People </em>v. <em>Parham, </em><span class="citation" data-id="2609203"><a href="/opinion/2609203/people-v-parham/" aria-description="Citation for case: People v. Parham">60 Cal. 2d 378</a></span>, <span class="citation" data-id="2609203"><a href="/opinion/2609203/people-v-parham/" aria-description="Citation for case: People v. Parham">384 P. 2d 1001</a></span> (1963).</p>
</footnote>
<footnote label="24">
<p id="b270-8"> See Wall, <em>supra, </em>n. 6, at 48; Napley, <em>supra, </em>n. 7, at 99: “[W]hile many identification parades are conducted by the police with scrupulous regard for fairness, it is not unknown for the identifying witness to be placed in a position where he can see the suspect before the parade forms . . . .”</p>
</footnote>
<footnote label="25">
<p id="b270-9"> Williams &amp; Hammelmann, Part I, <em>supra, </em>n. 7, at 486; Burtt, Applied Psychology 254-255.</p>
</footnote>
<footnote label="26">
<p id="b272-7"> One commentator proposes a model statute providing not only for counsel, but other safeguards as well:</p>
<blockquote id="b272-8">“Most, if not all, of the attacks on the lineup process could be averted by a uniform statute modeled upon the best features of the civilian codes. Any proposed statute should provide for the right to counsel during any lineup or during any confrontation. Provision should be made that any person, whether a victim or a witness, must give a description of the suspect before he views any arrested person. A written record of this description should be required, and the witness should be made to sign it. This written record would be available for inspection by defense counsel for copying before the trial and for use at the trial in testing the accuracy of the identification made during the lineup and during the trial.</blockquote>
<blockquote id="b272-9">“This ideal statute would require at least six persons in addition to the accused in a lineup, and these persons would have to be of approximately the same height, weight, coloration of hair and skin, and bodily types as the suspect. In addition, all of these men should, as nearly as possible, be dressed alike. If distinctive garb was used during the crime, the suspect should not be forced to wear similar clothing in the lineup unless all of the other persons are similarly garbed. A complete written report of the names, addresses, descriptive details of the other persons in the lineup, and of everything which transpired during the identification would be mandatory. This report would include everything stated by the identifying witness during this step, including any reasons given by him as to what features, etc., have sparked his recognition.</blockquote>
<blockquote id="b272-10">“This statute should permit voice identification tests by having each person in the lineup repeat identical innocuous phrases, and it would be impermissible to force the use of words allegedly used during a criminal act.</blockquote>
<blockquote id="b272-11">“The statute would enjoin the police from suggesting to any viewer that one or more persons in the lineup had been arrested as a suspect. If more than one witness is to make an identification, each <page-number citation-index="1" label="237">*237</page-number>witness should be required to do so separately and should be forbidden to speak to another witness until all of them have completed the process.</blockquote>
<blockquote id="b273-6">“The statute could require the use of movie cameras and tape recorders to record the lineup process in those states which are financially able to afford these devices. Finally, the statute should provide that any evidence obtained as the result of a violation of this statute would be inadmissible.” Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>, 627-628.</blockquote>
</footnote>
<footnote label="27">
<p id="b273-7"><em> </em>Although the right to counsel usually means a right to the suspect’s own counsel, provision for substitute counsel may be justified on the ground that the substitute counsel’s presence may eliminate the hazards which render the lineup a critical stage for the presence of the suspect’s <em>own </em>counsel.</p>
</footnote>
<footnote label="28">
<p id="b274-6"> Concern is also expressed that the presence of counsel will force divulgence of the identity of government witnesses whose identity the Government may want to conceal. To the extent that this is a valid or significant state interest there are police practices commonly used to effect concealment, for example, masking the face.</p>
</footnote>
<footnote label="29">
<p id="b274-7"> Many other nations surround the lineup with safeguards against prejudice to the suspect. In England the suspect must be allowed the presence of his solicitor or a friend, Napley, <em>supra, </em>n. 7, at 98-99; Germany requires the presence of retained counsel; France forbids the confrontation of the suspect in the absence of his counsel; Spain, Mexico, and Italy provide detailed procedures prescribing the conditions under which confrontation must occur under the supervision of a judicial officer who sees to it that the proceedings are officially recorded to assure adequate scrutiny at trial. Murray, The Criminal Lineup at Home and Abroad, <span class="citation no-link">1966 Utah L. Rev. 610</span>, 621-627.</p>
</footnote>
<footnote label="30">
<p id="b275-6"> Thirty years ago Wigmore suggested a “scientific method” of pretrial identification “to reduce the risk of error hitherto inherent in such proceedings.” Wigmore, The Science of Judicial Proof 541 (3d ed. 1937). Under this approach, at least 100 talking films would be prepared of men from various occupations, races, etc. Each would be photographed in a number of stock movements, with and without hat and coat, and would read aloud a standard passage. The suspect would be filmed in the same manner. Some 25 of the films would be shown in succession in a special projection room in which each witness would be provided an electric button which would activate a board backstage when pressed to indicate that the witness had identified a given person. Provision would be made for the degree of hesitancy in the identification to be indicated by the number of presses. <em>Id., </em>at 540-541. Of course, the more systematic and scientific a process or proceeding, including one for purposes of identification, the less the impediment to reconstruction of the conditions bearing upon the reliability of that process or proceeding at trial. See discussion of fingerprint and like tests, Part III, <em>supra, </em>and of handwriting exemplars in <em>Gilbert </em>v. <em>California, supra.</em></p>
</footnote>
<footnote label="31">
<p id="b276-5"> See <em>Goldstein </em>v. <em>United States, </em><span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/#124" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114, 124, n. 1</a></span> (Murphy, J., dissenting). “[A]fter an accused sustains the initial burden, imposed by <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>, of proving to the satisfaction of the trial judge in the preliminary hearing that wire-tapping was unlawfully employed, as petitioners did here, it is only fair that the burden should then shift to the Government to convince the trial judge that its proof had an independent origin.”</p>
</footnote>
<footnote label="32">
<p id="b276-6"> We reach a contrary conclusion in <em>Gilbert </em>v. <em>California, supra, </em>as to the admissibility of the witness’ testimony that he also identified the accused at the lineup.</p>
</footnote>
<footnote label="33">
<p id="b277-4"> Thus it is not the case that “[i]t matters not how well the witness knows the suspect, whether the witness is the suspect’s mother, brother, or long-time associate, and no matter how long or well the witness observed the perpetrator at the scene of the crime.” Such factors will have an important bearing upon the true basis of <page-number citation-index="1" label="242">*242</page-number>the witness’ in-court identification. Moreover, the State’s inability to bolster the witness’ courtroom identification by introduction of the lineup identification.itself, see <em>Gilbert </em>v. <em>California, supra, </em>will become less significant the more the evidence of other opportunities of the witness to observe the defendant. Thus where the witness is a “kidnap victim who has lived for days with his abductor” the value to the State of admission of the lineup identification is indeed marginal, and such identification would be a mere formality.</p>
</footnote>
</opinion>
```

---
