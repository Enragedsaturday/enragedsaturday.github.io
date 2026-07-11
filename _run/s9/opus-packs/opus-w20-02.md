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

## GROUP: _overhaul2/lake/cases/United States v. United States District Court (Keith).json  (`lake-record`, 2 assertions)

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
{"assertion_id": "9872375a26ca03f4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. United States District Court (Keith)"}, "payload": {"all": [{"cite": "407 U.S. 297", "page": "297", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "407"}, {"cite": "92 S. Ct. 2125", "page": "2125", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "32 L. Ed. 2d 752", "page": "752", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "32"}, {"cite": "1972 U.S. LEXIS 38", "page": "38", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "407 U.S. 297", "official": {"cite": "407 U.S. 297", "page": "297", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "407"}, "official_selection_present": true, "record_id": "United States v. United States District Court (Keith)"}}
{"assertion_id": "6ad9bb7ae0a6080e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. United States District Court (Keith)"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. United States District Court (Keith)", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Van Leeuwen.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Van Leeuwen"
type: case
citation: "397 U.S. 249 (1970)"
parallel_cite: "90 S. Ct. 1029; 25 L. Ed. 2d 282"
neutral_cite: 1970 U.S. LEXIS 57
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-04-27
docket: 403
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-04-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Van Leeuwen
  varies_by_point: false
  scope_note: "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/"
  cluster_id: 108099
  opinion_id: 108099
  identity_checked: true
homes:
  - page: "[[Seizure of Property]]"
    role: "Key — package / mail detention"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Place]]", "[[Terry v. Ohio]]", "[[Illinois v. McArthur]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure-of-property", "reasonable-suspicion", "mail", "warrant-requirement"]
holding: "First-class mail may be detained without a warrant on reasonable suspicion while officers diligently pursue a search warrant; the brief detention invades no Fourth Amendment privacy interest, which is implicated only when the package is opened under a warrant."
lake:
  record_id: United States v. Van Leeuwen
  status: verified
  projected_at: 2026-07-09
---

# United States v. Van Leeuwen

*397 U.S. 249 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Van Leeuwen mailed two 12-pound insured first-class packages — declared to contain coins — at a Washington post office near the Canadian border, addressed to post-office boxes in California and Tennessee. A suspicious postal clerk alerted an officer, who noticed the return address was a vacant area of a nearby junior college and that Van Leeuwen's car bore British Columbia plates. Investigation revealed that both addressees were under investigation for trafficking in illegal coins. The packages were detained while a warrant was sought; because of a time difference in reaching Tennessee, the warrant did not issue and reach the post office until about 29 hours after mailing. The packages were then opened (revealing illegally imported gold coins), resealed, and promptly sent on. The Ninth Circuit reversed Van Leeuwen's conviction for want of a timely warrant.

## Issue
Did the warrantless detention of first-class mail packages — on reasonable suspicion, while officers diligently pursued a search warrant — violate the Fourth Amendment?

## Rule
No. While first-class mail may be opened only under a warrant, the suspicious circumstances "certainly justified detention, without a warrant, while an investigation was made." — 397 U.S. at 252. ^pin-252

Mere detention invaded no protected interest: "No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained." — [*Id.* at 253](https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/#:~:text=No%20interest%20protected%20by%20the). ^pin-253

The Court cautioned that the rule "is not that first-class mail can be detained 29 hours . . . to obtain the search warrant"; rather, "on the facts of this case — the nature of the mailings, their suspicious character, the fact that there were two packages going to separate destinations, the unavoidable delay in contacting the more distant of the two destinations . . . — a 29-hour delay between the mailings and the service of the warrant cannot be said to be 'unreasonable.'" — *Id.* ^pin-253b

## Application
The packages' weight, the fictitious return address, and the British Columbia plates of a mailer in a border town supplied reasonable suspicion justifying detention while officers investigated. The only thing done on suspicion was to detain the packages — no search occurred and no privacy interest was invaded until the magistrate approved the warrant. The 29-hour interval reflected diligent, unavoidable investigation of two distant destinations across a time difference, not delay or indifference, and was therefore reasonable on these particular facts.

## Conclusion
The detention of the packages pending the warrant was reasonable; the evidence was properly admitted, and the judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Van Leeuwen* remains the controlling authority that property (here, mail) may be briefly detained on reasonable suspicion while a warrant is diligently sought, reasoning by analogy to [[Terry v. Ohio]]. It is the direct predecessor of [[United States v. Place]] (luggage-detention duration limit) and runs alongside [[Illinois v. McArthur]] (temporary seizure of premises pending a warrant). No negative treatment.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Van Leeuwen*, 397 U.S. 249 (1970) — https://www.courtlistener.com/opinion/108099/united-states-v-van-leeuwen/ — pinpoints: 252, 253.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2c0d6be7ebf4038e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Van Leeuwen"}, "payload": {"all": [{"cite": "397 U.S. 249", "page": "249", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "397"}, {"cite": "90 S. Ct. 1029", "page": "1029", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "25 L. Ed. 2d 282", "page": "282", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}, {"cite": "1970 U.S. LEXIS 57", "page": "57", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": "397 U.S. 249", "official": {"cite": "397 U.S. 249", "page": "249", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "397"}, "official_selection_present": true, "record_id": "United States v. Van Leeuwen"}}
{"assertion_id": "1abaccb0633aa740", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-252", "record_id": "United States v. Van Leeuwen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-252", "pinpoint_status": "slip-only", "quote": "--- # United States v. Van Leeuwen *397 U.S. 249 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Van Leeuwen mailed two 12-pound insured first-class packages — declared to contain coins — at a Washington post office near the Canadian border, addressed to post-office boxes in California and Tennessee. A suspicious postal clerk alerted an officer, who noticed the return address was a vacant area of a nearby junior college and that Van Leeuwen's car bore British Columbia plates. Investigation revealed that both addressees were under investigation for trafficking in illegal coins. The packages were detained while a warrant was sought; because of a time difference in reaching Tennessee, the warrant did not issue and reach the post office until about 29 hours after mailing. The packages were then opened (revealing illegally imported gold coins), resealed, and promptly sent on. The Ninth Circuit reversed Van Leeuwen's conviction for want of a timely warrant. ## Issue Did the warrantless detention of first-class mail packages — on reasonable suspicion, while officers diligently pursued a search warrant — violate the Fourth Amendment? ## Rule No. While first-class mail may be opened only under a warrant, the suspicious circumstances", "quote_fidelity": "mismatch", "record_id": "United States v. Van Leeuwen", "star_marker": null}}
{"assertion_id": "85aa8d25041c1983", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-253", "record_id": "United States v. Van Leeuwen"}, "payload": {"fragment": "#:~:text=No%20interest%20protected%20by%20the", "page": null, "pin_id": "pin-253", "pinpoint_status": "star-verified", "quote": "No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained.", "quote_fidelity": "matched", "record_id": "United States v. Van Leeuwen", "star_marker": "253"}}
{"assertion_id": "928c00a68ddd064f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-253b", "record_id": "United States v. Van Leeuwen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-253b", "pinpoint_status": "slip-only", "quote": "is not that first-class mail can be detained 29 hours . . . to obtain the search warrant", "quote_fidelity": "mismatch", "record_id": "United States v. Van Leeuwen", "star_marker": null}}
{"assertion_id": "f7915ce3b63e2fe0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Van Leeuwen"}, "payload": {"as_of_content": "1970-04-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Van Leeuwen", "scope_note": "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place.", "varies_by_point": false}}
```

### lake record — United States v. Van Leeuwen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Van Leeuwen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Van Leeuwen",
    "case_name_short": "",
    "case_name_full": "United States v. Van Leeuwen",
    "input_case_name": "United States v. Van Leeuwen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-04-27",
    "year": 1970,
    "docket": "403",
    "cluster_id": 108099,
    "lead_opinion_id": 108099,
    "sibling_ids": [
      108099
    ],
    "absolute_url": "/opinion/108099/united-states-v-van-leeuwen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "397 U.S. 249",
      "volume": "397",
      "reporter": "U.S.",
      "page": "249",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1029",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1029",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 282",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "282",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 57",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "57",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "397 U.S. 249",
        "volume": "397",
        "reporter": "U.S.",
        "page": "249",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1029",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1029",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 282",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "282",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 57",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "57",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "397 U.S. 249",
    "official_selection": {
      "court_class": "scotus",
      "selected": "397 U.S. 249",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-252",
      "page": null,
      "quote": "--- # United States v. Van Leeuwen *397 U.S. 249 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Van Leeuwen mailed two 12-pound insured first-class packages \u2014 declared to contain coins \u2014 at a Washington post office near the Canadian border, addressed to post-office boxes in California and Tennessee. A suspicious postal clerk alerted an officer, who noticed the return address was a vacant area of a nearby junior college and that Van Leeuwen's car bore British Columbia plates. Investigation revealed that both addressees were under investigation for trafficking in illegal coins. The packages were detained while a warrant was sought; because of a time difference in reaching Tennessee, the warrant did not issue and reach the post office until about 29 hours after mailing. The packages were then opened (revealing illegally imported gold coins), resealed, and promptly sent on. The Ninth Circuit reversed Van Leeuwen's conviction for want of a timely warrant. ## Issue Did the warrantless detention of first-class mail packages \u2014 on reasonable suspicion, while officers diligently pursued a search warrant \u2014 violate the Fourth Amendment? ## Rule No. While first-class mail may be opened only under a warrant, the suspicious circumstances",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-253",
      "page": null,
      "quote": "No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained.",
      "star_marker": "253",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8102,
      "fragment": "#:~:text=No%20interest%20protected%20by%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-253b",
      "page": null,
      "quote": "is not that first-class mail can be detained 29 hours . . . to obtain the search warrant",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1970-04-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Van Leeuwen",
    "varies_by_point": false,
    "scope_note": "Controlling: a brief detention of mailed packages on reasonable suspicion, while a warrant is diligently sought, is reasonable; mere detention invades no privacy interest until the package is opened under a warrant. A precursor to the property-detention analysis of United States v. Place.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Corey Joel Eichers",
          "cluster_id": 2731770,
          "cite": [
            "853 N.W.2d 114",
            "2014 Minn. LEXIS 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Noel Lee Decker, Barbara K. Decker",
          "cluster_id": 577733,
          "cite": [
            "956 F.2d 773",
            "1992 U.S. App. LEXIS 1519",
            "1992 WL 19476"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Neem Shiva Dass and Ma Surina Dasi, Marvin Neer, Gerald Terpak",
          "cluster_id": 507432,
          "cite": [
            "849 F.2d 414",
            "1988 U.S. App. LEXIS 8007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John Christopher Beale",
          "cluster_id": 437319,
          "cite": [
            "736 F.2d 1289"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reedo Eric Corbitt",
          "cluster_id": 402364,
          "cite": [
            "675 F.2d 626",
            "1982 U.S. App. LEXIS 20065"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond J. Place",
          "cluster_id": 394856,
          "cite": [
            "660 F.2d 44"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vito Giacalone",
          "cluster_id": 361931,
          "cite": [
            "588 F.2d 1158",
            "1978 U.S. App. LEXIS 6938"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane1_negative"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
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
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Bolton",
          "cluster_id": 108714,
          "cite": [
            "35 L. Ed. 2d 201",
            "93 S. Ct. 739",
            "410 U.S. 179",
            "1973 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 2316658,
          "cite": [
            "586 A.2d 85",
            "123 N.J. 1",
            "1991 N.J. LEXIS 17"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hempele",
          "cluster_id": 1435469,
          "cite": [
            "576 A.2d 793",
            "120 N.J. 182",
            "1990 N.J. LEXIS 92"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Athan",
          "cluster_id": 2622136,
          "cite": [
            "158 P.3d 27"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mooney",
          "cluster_id": 7894385,
          "cite": [
            "218 Conn. 85",
            "588 A.2d 145",
            "1991 Conn. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Francis Lafrance",
          "cluster_id": 526045,
          "cite": [
            "879 F.2d 1",
            "1989 U.S. App. LEXIS 10185",
            "1989 WL 77159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government, Wabun-Inini, AKA Vernon Bellecourt v. William Sessions, Director, Federal Bureau of Investigation, Washington, D.C. Jeffrey J. Jamar, Agent-In-Charge, Minneapolis Office of the Fbi, Minneapolis, Minnesota Peter Cunningham, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota William Clifford, Special Agent, Minneapolis Office of the Fbi, Minneapolis, Minnesota John Doe Jane Doe, and Other Presently Unknown Officials of the United States Government",
          "cluster_id": 539907,
          "cite": [
            "900 F.2d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKinnon",
          "cluster_id": 2616887,
          "cite": [
            "500 P.2d 1097",
            "7 Cal. 3d 899",
            "103 Cal. Rptr. 897",
            "1972 Cal. LEXIS 233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1192493,
          "cite": [
            "918 P.2d 945",
            "82 Wash. App. 594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas J. Licata",
          "cluster_id": 451773,
          "cite": [
            "761 F.2d 537"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Irving Hillison, United States of America v. Murray David Jacobson, United States of America v. Jeffrey Ketchum Mansfield",
          "cluster_id": 435104,
          "cite": [
            "733 F.2d 692"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Richards",
          "cluster_id": 386047,
          "cite": [
            "638 F.2d 765"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darrell Jay Glover, United States of America v. Susan Noreen Kozak",
          "cluster_id": 733387,
          "cite": [
            "104 F.3d 1570",
            "1997 U.S. App. LEXIS 1060",
            "1997 WL 25529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Van Leeuwen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108099) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 172,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 172,
        "triage_read": 11,
        "triage_snippet_classified": 161
      },
      "lane2_top_cited": {
        "query": "cites:(108099)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NSZzPTU5NzE1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108099%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108099)",
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
    "complete_query": "cites:(108099)",
    "indexed_citing_opinions": 259,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108099,
        "count": 259,
        "count_source": "search"
      }
    ],
    "citation_count": 399,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-van-leeuwen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUyMjA1ODImcz00MzM3MzA4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108099%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108099,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 99756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 104235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 107064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108099,
        "cited_id": 286052,
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
    "date_created": "2026-07-06T03:15:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:19:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:16:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Van Leeuwen

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b351-9">
  Mr. Justice Douglas
 </author>
<p id="Aj0">
  delivered the opinion of the Court.
 </p>
<p id="b351-10">
  Respondent, at about 1:30 p. m. on Thursday, March 28, 1968, mailed two 12-pound packages at the post office in Mt. Vernon, Washington, a town some 60 miles from the Canadian border. One package was addressed to a post office box in Van Nuys, California, and the other to a post office box in Nashville, Tennessee. Respondent declared they contained coins. Each pack
  <span citation-index="1" class="star-pagination" label="250"> 
   *250
   </span>
  age was to be sent airmail registered and each was insured for $10,000, a type of mailing that the parties agree was first class, making them not subject to discretionary inspection.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b352-5">
  When the postal clerk told a policeman who happened to be present that he was suspicious of the packages, the policeman at once noticed that the return address on the packages was a vacant housing area of a nearby junior college, and that the license plates of respondent’s car were British Columbia. The policeman called the Canadian police, who called customs in Seattle. At 3 o’clock that afternoon customs called Van Nuys and learned that the addressee of one package was under investigation in Van Nuys for trafficking in illegal coins. Due to the time differential, Seattle customs was unable to reach Nashville until the following morning, March 29, when Seattle was advised that the second addressee was also being investigated for the same crime. A customs official in Seattle thereupon filed an affidavit for a search warrant for both packages with a United States commissioner, who issued the search warrant at 4 p. m., and it was executed in Mt. Vernon at 6:30 p. m., 2% hours later. Thereupon the packages were opened, inspected, resealed, and promptly sent on their way.
 </p>
<p id="b352-6">
  Other evidence showed that respondent had brought the two packages in from Canada without declaring them. He was tried for illegally importing gold coins in violation of <span class="citation no-link">18 U. S. C. § 545</span> and found guilty and sentenced and fined. On appeal, the Court of Appeals reversed, holding that the coins were improperly admitted in evidence because a timely warrant had not been obtained. <span class="citation" data-id="9454782"><a href="/opinion/286052/united-states-v-gerritt-johannes-van-leeuwen/" aria-description="Citation for case: United States v. Gerritt Johannes Van Leeuwen">414 F. 2d 758</a></span>. The case is here on a petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/885/">396 U. S. 885</a></span>. We reverse.
 </p>
<p id="b353-2">
<span citation-index="1" class="star-pagination" label="251"> 
   *251
   </span>
  It has long been held that first-class mail such as letters and sealed packages subject to letter postage— as distinguished from newspapers, magazines, pamphlets, and other printed matter — is free from inspection by-postal authorities, except in the manner provided by the Fourth Amendment. As stated in
  <em>
   Ex parte Jackson,
  </em>
  <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span>, decided in 1878:
 </p>
<blockquote id="b353-3">
  “Letters and sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household. No law of Congress can place in the hands of officials connected with the postal service any authority to invade the secrecy of letters and such sealed packages in the
  <em>
   mail;
  </em>
  and all regulations adopted as to mail matter of this kind must be in subordination to the great principle embodied in the fourth amendment of the Constitution.”
 </blockquote>
<p id="b353-4">
  The course of events since 1878 has underlined the relevance and importance of the Post Office to our constitutional rights. Mr. Justice Holmes in
  <em>
   Milwaukee Pub. Co.
  </em>
  v.
  <em>
   Burleson, 255
  </em>
  U. S. 407, 437 (dissenting opinion), said that “the use of the mails is almost as much a part of free speech as the right to use our tongues.” We have emphasized over and over again that while Congress may classify the mail and fix the charges
  <span citation-index="1" class="star-pagination" label="252"> 
   *252
   </span>
  for its carriage, it may not set up regimes of censorship over it,
  <em>
   Hannegan
  </em>
  v.
  <em>
   Esquire, Inc.,
  </em>
  <span class="citation" data-id="9419751"><a href="/opinion/104235/hannegan-v-esquire-inc/" aria-description="Citation for case: Hannegan v. Esquire, Inc.">327 U. S. 146</a></span>, or encumber its flow by setting “administrative officials astride the flow of mail to inspect it, appraise it, write the addressee about it, and await a response before dispatching the mail” to him.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
<em>
   Lamont
  </em>
  v.
  <em>
   Postmaster General,
  </em>
  <span class="citation" data-id="9423040"><a href="/opinion/107064/lamont-v-postmaster-general/#306" aria-description="Citation for case: Lamont v. Postmaster General">381 U. S. 301, 306</a></span>. Yet even first-class mail is not beyond the reach of all
  <em>
   inspection;
  </em>
  and the sole question here is whether the conditions for its detention and inspection had been satisfied. We think they had been.
 </p>
<p id="b354-6">
  The nature and weight of the packages, the fictitious return address, and the British Columbia license plates of respondent who made the mailings in this border town certainly justified detention, without a warrant, while an investigation was made. The “protective search for weapons” of a suspect which the Court approved in
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-27</a></span>, even when probable cause for an arrest did not exist, went further than we need go here. The only thing done here on the basis of suspicion was detention of the packages. There was at that point no possible invasion of the right “to be secure” in the “persons, houses, papers, and effects” protected by the Fourth Amendment against “unreasonable searches and seizures.” Theoretically — and it is theory only that respondent has on his side — detention of mail could at some point become an unreasonable seizure of “papers” or “effects” within the meaning of the Fourth Amendment. Detention for 1% hours — from 1:30 p. m. to 3 p. m. — for an investigation certainly was not excessive; and at the end of that time probable cause existed for believing that the California package was part of an illicit project. A warrant could have been obtained that
  <span citation-index="1" class="star-pagination" label="253"> 
   *253
   </span>
  day for the one package; yet the mystery of the other package remained unsolved and federal officials in Tennessee could not be reached because of the time differential. The next morning they were reached and it was learned that the second package was also probably part of an illicit project. By 4 p. m. — or 26% hours after the mailing in Mt. Vernon — a search warrant was obtained in Seattle and at 6:30 p. m., or 29 hours after the mailing, the search warrant reached Mt. Vernon, a speedy transmission considering the rush-hour time of day and the congested highway.
 </p>
<p id="b355-4">
  No interest protected by the Fourth Amendment was invaded by forwarding the packages the following day rather than the day when they were deposited. The significant Fourth Amendment interest was in the privacy of this first-class mail; and that privacy was not disturbed or invaded until the approval of the magistrate was obtained.
 </p>
<p id="b355-5">
  The rule of our decisions certainly is not that first-class mail can be detained 29 hours after mailing in order to obtain the search warrant needed for its inspection. We only hold that on the facts of this case— the nature of the mailings, their suspicious character, the fact that there were two packages going to separate destinations, the unavoidable delay in contacting the more distant of the two destinations, the distance between Mt. Vernon and Seattle — a 29-hour delay between the mailings and the service of the warrant cannot be said to be “unreasonable” within the meaning of the Fourth Amendment. Detention for this limited time was, indeed, the prudent act rather than letting the packages enter the mails and then, in case the initial suspicions were confirmed, trying to locate them en route and enlisting the help of distant federal officials in serving the warrant.
 </p>
<p id="b355-6">
<em>
   Reversed.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b352-7">
   <span class="citation no-link">39 CFR §131.2</span> describes “first class” mail as “matter closed against postal inspection,” which follows the definition in <span class="citation no-link">39 U. S. C. §4251</span> (a).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b354-7">
   The question as to the right of the addressee to stop deliveries is a separate and distinct one. See No. 399,
   <em>
    Rowan
   </em>
   v.
   <em>
    Post Office, post,
   </em>
   p. 728.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Vaneaton.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Vaneaton
type: case
citation: "49 F.3d 1423 (1995)"
parallel_cite: 95 Daily Journal DAR 3223
neutral_cite: "95 Cal. Daily Op. Serv. 1884; 1995 U.S. App. LEXIS 4793; 1995 WL 101835"
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1995
date_decided: 1995-03-13
docket: 93-30387
authority_weight: "Binding in-circuit — 9th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/691388/united-states-v-jack-palmer-vaneaton/"
  cluster_id: 691388
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Vaneaton
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — voluntary-exposure pole (voluntary doorway exposure = no Payton violation, 49 F.3d at 1426-27)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (doorway arrests)"
---

# United States v. Vaneaton

*49 F.3d 1423 (9th Cir. 1995)* (No. 93-30387) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 691388 / lead opinion 9487908 → 49 F.3d 1423, No. 93-30387, decided 1995-03-13 (Trott, J.; Tashima, J., dissenting). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. ENRICH-CONFIRM: exact star-pages (1426/1427) inferred from block ids; finalize at mint enrich via read_document offsets. -->

## Background
Bend, Oregon officers with probable cause to arrest John Vaneaton for receiving stolen property went to his motel room without a warrant and knocked. Vaneaton saw the uniformed officers through the window and opened the door; he was arrested while "standing just inside the open door of his motel room." The police did not cross the threshold until after they announced the arrest. Vaneaton moved to suppress, arguing the warrantless arrest violated *[[Payton v. New York]]*; the magistrate found he had opened the door voluntarily and without coercion, and the district court denied suppression.

## Issue
Whether a suspect who opens his door in response to a noncoercive police knock and is arrested at the open doorway is protected by *[[Payton v. New York|Payton]]*'s bar on warrantless in-home arrests, or whether he has voluntarily exposed himself to a warrantless arrest.

## Rule
The dispositive question is voluntary exposure, not the suspect's exact position at the threshold. "As we read the controlling authority, the question presented in this case is not decided only on the basis of whether Vaneaton was standing inside or outside the threshold of his room, but whether he 'voluntarily exposed himself to warrantless arrest' by freely opening the door of his motel room to the police." 49 F.3d at 1426 (quoting *United States v. Johnson*, 626 F.2d 753, 757 (9th Cir. 1980)). ^pin-1426

If he so exposed himself, the *[[Payton v. New York|Payton]]* presumption is overcome: "implicit in *Johnson* is approval of the warrantless arrest of a suspect who voluntarily opens the door of his dwelling in response to a noncoercive knock by the police." *Id.* at 1427. ^pin-1427

## Application
The record showed voluntary exposure. "When Vaneaton saw them through the window, he voluntarily opened the door and exposed both himself and the immediate area to them. No threats or force were used by the police to get him to open the door, and his actions were not taken in response to a claim of lawful authority. The police did not enter the house until they formally placed Vaneaton under arrest." 49 F.3d at 1427. ^pin-1427b

Because voluntariness is a factual finding reviewed only for [[Common Legal Terms#clear-error|clear error]] (*[[United States v. Al-Azzawy]]*, 784 F.2d 890, 895 (9th Cir. 1986)), and the magistrate's findings were supported, no *[[Payton v. New York|Payton]]* violation occurred.

## Conclusion
Affirmed. A suspect who voluntarily opens his door to a noncoercive knock and is arrested at the doorway has exposed himself to a lawful warrantless arrest; *[[Payton v. New York|Payton]]* is not offended. (Tashima, J., dissented, reading the result as contrary to *[[Payton v. New York|Payton]]*.)

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Vaneaton* is the voluntary-exposure pole of the Ninth-Circuit surround-and-call-out line — the containment-vs-exit-command contrast to *[[United States v. Al-Azzawy]]* (coerced emergence) and *[[United States v. Nora]]* (surround-and-summon under overwhelming force). The line turns on voluntariness: a free response to a noncoercive knock forfeits *[[Payton v. New York|Payton]]*'s protection; a coerced emergence under a show of force does not.

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 691388 + 49 F.3d 1423); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Limiting*

## Sources
- [*United States v. Vaneaton*, 49 F.3d 1423 (9th Cir. 1995)](https://www.courtlistener.com/opinion/691388/united-states-v-vaneaton/) — pinpoints: 1426 (voluntary-exposure question presented), 1427 (voluntary opening to a noncoercive knock overcomes *Payton*; distinguishing *Al-Azzawy* at 895); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6fc84c7a910012d5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Vaneaton"}, "payload": {"all": [{"cite": "49 F.3d 1423", "page": "1423", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "95 Daily Journal DAR 3223", "page": "3223", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "95"}, {"cite": "95 Cal. Daily Op. Serv. 1884", "page": "1884", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "95"}, {"cite": "1995 U.S. App. LEXIS 4793", "page": "4793", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1995"}, {"cite": "1995 WL 101835", "page": "101835", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1995"}], "display": "49 F.3d 1423", "official": {"cite": "49 F.3d 1423", "page": "1423", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "49"}, "official_selection_present": true, "record_id": "United States v. Vaneaton"}}
{"assertion_id": "6a68aecbe3a557d0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Vaneaton"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Vaneaton", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Vaneaton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Vaneaton",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Jack Palmer Vaneaton",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Jack Palmer VANEATON, Defendant-Appellant",
    "input_case_name": "United States v. Vaneaton",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1995-03-13",
    "year": 1995,
    "docket": "93-30387",
    "cluster_id": 691388,
    "lead_opinion_id": 9487908,
    "sibling_ids": [],
    "absolute_url": "/opinion/691388/united-states-v-jack-palmer-vaneaton/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "49 F.3d 1423",
      "volume": "49",
      "reporter": "F.3d",
      "page": "1423",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 Daily Journal DAR 3223",
        "volume": "95",
        "reporter": "Daily Journal DAR",
        "page": "3223",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "95 Cal. Daily Op. Serv. 1884",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. App. LEXIS 4793",
        "volume": "1995",
        "reporter": "U.S. App. LEXIS",
        "page": "4793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 WL 101835",
        "volume": "1995",
        "reporter": "WL",
        "page": "101835",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "49 F.3d 1423",
        "volume": "49",
        "reporter": "F.3d",
        "page": "1423",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Daily Journal DAR 3223",
        "volume": "95",
        "reporter": "Daily Journal DAR",
        "page": "3223",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Cal. Daily Op. Serv. 1884",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. App. LEXIS 4793",
        "volume": "1995",
        "reporter": "U.S. App. LEXIS",
        "page": "4793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 WL 101835",
        "volume": "1995",
        "reporter": "WL",
        "page": "101835",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "49 F.3d 1423",
    "official_selection": {
      "court_class": "coa",
      "selected": "49 F.3d 1423",
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
    "date_created": "2026-07-08T16:52:45Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:56:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-vaneaton--691388",
      "to_record_id": "United States v. Vaneaton",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Vaneaton

```
<opinion type="majority">
<p id="b1468-14">Opinion by Judge TROTT. Dissent by Judge TASHIMA.</p>
<author id="b1468-15">TROTT, Circuit Judge:</author>
<p id="b1468-16">John Vaneaton<footnotemark>1</footnotemark> was arrested on September 9, 1992, while standing just inside the open door of his motel room in Bend, Oregon. He was arrested without a warrant by officers of the Bend Police Department. He concedes that the police who arrested him for receiving stolen property had probable cause to do so, but he contends that the warrant-less arrest violated the rule of <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), a rule ordinarily requiring police to obtain a warrant before arresting a suspect inside his home, or in this case, inside his motel room.</p>
<p id="b1468-20">We have jurisdiction over this timely appeal pursuant to <span class="citation no-link">28 U.S.C. § 1291</span> and Fed. R.Crim.P. 11(e)(2). We affirm the district court’s denial of Vaneaton’s motion to suppress a revolver found in his motel room in connection with his arrest. This revolver was used to secure his conditional plea of guilty to a charge of felon in possession of a firearm.</p>
<p id="b1468-21">I</p>
<p id="b1468-22">On August 25, 1992, officers of the Portland Police Bureau arrested Vaneaton in Portland, Oregon on outstanding no-bail warrants charging him with a parole violation and contempt of court. He had failed to report as required to his parole officer. Va-neaton, a notorious, thrice-convicted burglar known by the police to operate primarily in the Willamette Valley and along the coast of Oregon, lived in Independence, Oregon, some 60 miles from Portland. He was known to have committed crimes in at least four counties: Polk, Lincoln, Jackson, and Multnomah.</p>
<p id="b1468-23">Around the time Vaneaton was arrested, he had been repeatedly selling goods to various pawn shops in the Portland area, an activity that attracted the attention of the police. Among the items he sold were pieces of jewelry that turned out to have been stolen during recent unsolved residential burglaries in the Bend, Oregon area. Bend is located in the middle of the state, approximately 150 miles from Portland, and 100 miles from Independence. When arrested, he had documents on his person indicating he had previously been in Bend. Vaneaton was <page-number citation-index="1" label="1425">*1425</page-number>released shortly after his arrest. The police were unaware of his release.</p>
<p id="b1469-4">As part of an investigation instigated as a result of Vaneaton’s possession of stolen property, and in order to determine if proof could be developed that Vaneaton had been in Bend precisely at the time of the crimes during which the jewelry was stolen, uniformed officers of the Bend Police Department were detailed on September 9, 1992, to tour motels in that area to look for such evidence. They found it at their first stop, the Rainbow Motel. Not only did they discover that Vaneaton had been in Bend at the time of the burglaries, but they also discovered to their surprise that he was back, and staying again in the Rainbow Motel for at least another night. This discovery was unexpected for two reasons. First, the Bend police believed he was still in custody for a parole violation. Second, it was counter intuitive to find him back at the scene of the crime.-</p>
<p id="b1469-5">Armed with this unexpected information, and now with ample probable cause to arrest him for receiving stolen property with respect to the recovered loot he possessed in Portland, the officers called for backup. When it arrived, they went directly to his motel room to see if he was there and to arrest him if he was. .</p>
<p id="b1469-6">Wearing their uniforms and with their guns in their holsters, the officers knocked on the door to Vaneaton’s room. They made no demands; in fact, they said nothing. According to the stipulated facts, Vaneaton opened the curtains of a window, saw the officers, and opened the door. Detective Carpenter asked him if he was Jack Vanea-ton, and when he said he was, he was arrested. At the moment of his arrest, Vaneaton was standing at the doorway but just inside the threshold.- The arresting officer was immediately outside the threshold of the' room and did not enter before advising Vaneaton he was under arrest. Vaneaton was then handcuffed, advised of his <em>Miranda </em>rights, and asked for permission to search the room. He gave verbal permission for such a search and signed a written consent form. Officer Reeves also asked him if he had a gun. Vaneaton said he did and directed them to a closet. The police then found a revolver where Vaneaton had told them it was located.</p>
<p id="b1469-8">II</p>
<p id="b1469-9">The issue Vaneaton raises is whether the police, acting with probable cause but without a warrant and while standing outside his motel room, could lawfully arrest him while he was standing immediately inside the open doorway. Relying on <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), and denying the existence of exigent circumstances, Vaneaton claims, the answer is clear: The arresting officers were required to have had a warrant.</p>
<p id="b1469-10">In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the Court drew a bright fine at the identifiable threshold of a protected dwelling and said such a line cannot be crossed !to arrest a suspect inside, absent consent or exigent circumstances:</p>
<blockquote id="b1469-11">The Fourth Amendment protects the individual’s privacy in a variety of settings. In none is the zone of privacy <em>more clearly defined </em>than when bounded by the <em>unambiguous physical dimensions </em>of an individual’s home — a zone that finds its roots in clear and specific constitutional terms: “The right of the people to be secure in their ... houses ... shall not be violated.” ... In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has <em>drawn a firm line </em>at the entrance to the house. Absent exigent circumstances, that <em>threshold </em>may not reasonably be crossed without a warrant.</blockquote>
<p id="b1469-12"><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U.S. at 589-90</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1381" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1381-82</a></span> (citations omitted) (emphasis added). The purpose of this rule is manifest from the rule itself: to protect an individual’s “zone of privacy.” Thus, the result of <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is that “seizures inside a home without a warrant are presumptively unreasonable.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>Id. </em>at 586</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1380" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1380</a></span>.</p>
<p id="b1469-13">The government’s response to Vaneaton’s claim is that a warrantless arrest at the doorway of a suspect’s dwelling is constitutionally proper, provided that law enforcement has not misidentified itself, has not used coercion, and the suspect acquiesces to the encounter. In support of this argument, the government invokes this Court’s discus<page-number citation-index="1" label="1426">*1426</page-number>sion in <em>United States v. Whitten, </em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d 1000, 1015-17</a></span> <em>(9th Cir,1983), cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./465/1100/">465 U.S. 1100</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./104/1593/">104 S.Ct. 1593</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/80/125/">80 L.Ed.2d 125</a></span> (1984), of the arrest of Whitten’s codefendant, John Gaiefsky, and <em>United States v. Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980), <em>aff'd, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span> (1982). In <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>, </em>we held that Gaiefsky’s arrest while standing in the doorway of his hotel room did not violate <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>because “[a] doorway ..., unlike the interior of a hotel room, is a public place.” <span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d at 1015</a></span>. As authority for this proposition, we relied on <em>United States v. Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U.S. 38</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">96 S.Ct. 2406</a></span>, <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">49 L.Ed.2d 300</a></span> (1976).</p>
<p id="b1470-4">As we read the controlling authority, the question presented in this cáse is not decided only on the basis of whether Vaneaton was standing inside or outside the threshold of his room, but whether he “voluntarily exposed himself to warrantless arrest” by freely opening thé door of his motel room to the police. <em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. If he so exposed himself, the presumption created by <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>is overcome. <em>See <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">id.</a></span></em><footnotemark><em>2</em></footnotemark></p>
<p id="b1470-5">A</p>
<p id="b1470-6">In resolving whether Vaneaton voluntarily exposed himself to warrantless arrest, we find considerable guidance in <em>United States v. Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980). In <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>, </em>the question before us was whether Johnson’s warrantless arrest as he stood at an open doorway within his home satisfied <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>. </em>We held that it did not because of the deceitful manner in which the door was caused by the arresting officers to.be opened. The agents had used a subterfuge to get Johnson to open the door, and because of their use of that subterfuge — they misrepresented. their identities — we held that “Johnson’s initial exposure to the view and the physical control of the agents was not consensual on his part.” <em>Id. </em>at 757.</p>
<p id="b1470-7">On the basis of factual differences, <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>explicitly distinguished <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>and a <em>pre-Payton </em>case from our circuit, <em>United States v. Botero, </em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d 430</a></span> (9th Cir.1978), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./441/944/">441 U.S. 944</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./99/2162/">99 S.Ct. 2162</a></span>, <span class="citation" data-id="9015516"><a href="/opinion/9022296/botero-v-united-states/" aria-description="Citation for case: Botero v. United States">60 L.Ed.2d 1045</a></span> (1979). <em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. In <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>the United States Supreme Court</p>
<blockquote id="A_FZ">upheld the warrantless arrest of a defendant who was standing within the frame of her doorway as the officers - approached and who then retreated into the vestibule of her home where the officers followed and effected the arrest. The Court held that once the defendant was exposed to public view in her doorway, her act of retreating into her house could not thwart an otherwise proper arrest by officers who pursued her inside.</blockquote>
<p id="b1470-12"><em>Johnson, </em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#756" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 756</a></span>.</p>
<p id="b1470-13">In <em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">Botero</a></span>, </em>officers without a warrant knocked on Botero’s door, and when he opened it, he was placed under arrest. We held in <em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/" aria-description="Citation for case: United States v. Diego Botero, United States of America...">Botero</a></span>, </em>citing <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana</a></span>, </em>that under the circumstances the doorway in which he was standing was a public place. <em>Botero, </em><span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/#432" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d at 432</a></span>. Thus, implicit in <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>is approval of the warrantless arrest of a suspect who voluntarily opens the door of his dwelling in response to a noncoercive knock by the police. This holding is consistent with our holding in <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>.</em></p>
<p id="b1470-14">As in <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span> </em>and <em><span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">Whitten</a></span>, </em>the arrest in the instant case involves factors that distinguish it from the arrests made in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and its consolidated companion case, <em>Riddick v. New York. </em>In <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>the police who entered Payton’s apartment broke through a closed door with crowbars. No one was home, but incriminating evidence seen in plain view was seized and used to convict him. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York">445 U.S. at 576-77</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1374" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1374-75</a></span>. In <em>Riddick, </em>the closed door of Riddick’s house on which, the police knocked was opened by Riddick’s young son. Riddick could be seen sitting inside the apartment on a bed. He was covered by a sheet. Without any behavior on Riddick’s part that could be construed as consent, the police entered and arrested him on the spot. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#578" aria-description="Citation for case: Payton v. New York">445 U.S. at 578</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1376" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1376</a></span>. In both cases, the entries preceded the arrests.</p>
<p id="b1471-3"><page-number citation-index="1" label="1427">*1427</page-number>By contrast, in Vaneaton’s case the uniformed police used no force or threats, and unlike <em><span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>, </em>they did not resort to a subterfuge or a ruse, or draw weapons-. When Vaneaton saw them through the window, he voluntarily opened the door and exposed both himself and the immediate area to them. No threats or force were used by the police to get him to open the door, and his actions were not taken in response to-a claim of lawful authority. The police did not enter the house until they formally placed Vaneaton under arrest. The magistrate’s findings of fact that (1) Vaneaton opened the door voluntarily, and (2) no coercion was used by the police, are fully supported by the record. “A trial court’s finding on voluntariness should not be overturned unless it is clearly erroneous.” <em>United States v. Al-Azzawy, </em><span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#895" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890, 895</a></span> (9th Cir.1985) (citation omitted), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986). Accordingly, by opening the door as he did, Vaneaton exposed himself in a public place. His warrantless arrest, therefore, does riot offerid the Fourth Amendment. <em>United States v. Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson">423 U.S. 411, 421-24</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#826" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820, 826-28</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976) (The Fourth Amendment is not violated by a warrantless felony arrest in a public place).<footnotemark>3</footnotemark></p>
<p id="b1471-4">In summary, this episode does not materially resemble the kinds of “invasions” or “intrusions” against which <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>seeks to guard. Knocking on a door to attempt to contact a person inside is a common event and hardly a hallmark of a police state, and indeed, <em>under these facts </em>the zone of privacy sought by <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>to be protected is not implicated. Accordingly, we hold that <em>Pay-ton </em>was not violated, and that Vaneaton’s arrest was proper.<footnotemark>4</footnotemark></p>
<p id="b1471-8">CONCLUSION</p>
<p id="b1471-9">We conclude that the seizure in this case did not offend the Fourth Amendment. Thus we affirm the district court’s denial of Vaneaton’s motion to suppress.</p>
<p id="b1471-10">AFFIRMED.</p>
<footnote label="1">
<p id="b1468-24">. The defendant-appellant’s name is spelled many different ways' in the record. We hope our choice is correct.</p>
</footnote>
<footnote label="2">
<p id="b1470-8">. -Because we conclude that Vaneaton’s exposure to the police was voluntary, we need not discuss exigent circumstances.</p>
</footnote>
<footnote label="3">
<p id="b1471-5">. Our analysis is consistent with our holding in <em>United States v. Winsor, </em><span class="citation" data-id="9477657"><a href="/opinion/506186/united-states-v-steven-dale-winsor/" aria-description="Citation for case: United States v. Steven Dale Winsor">846 F.2d 1569</a></span> (9th Cir.1988) (en banc),-which dealt with the validity of a search rather than a seizure. To quote the en banc panel,</p>
<blockquote id="b1471-6">In <em>United States v. Hersh, </em><span class="citation" data-id="304759"><a href="/opinion/304759/united-states-v-clifford-hersh/#229" aria-description="Citation for case: United States v. Clifford Hersh">464 F.2d 228, 229-30</a></span> (9th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./409/1008/">409 U.S. 1008</a></span>, [<span class="citation multiple-matches"><a href="/c/S.Ct./93/442/">93 S.Ct. 442</a></span>, <span class="citation" data-id="8982969"><a href="/opinion/8990796/basyap-inc-v-district-of-columbia-redevelopment-land-agency/" aria-description="Citation for case: Basyap, Inc. v. District of Columbia Redevelopment Land...">34 L.Ed.2d 301</a></span>] ... (1972), the police, while standing on the front porch, looked through a window and saw incriminating evidence inside the residence. We held no search was effected because police merely did what any member of the public was free to do — walk onto the front porch and observe whatever was in plain view through an unobstructed window. Similarly, in <em>Davis v. United States, </em><span class="citation" data-id="263083"><a href="/opinion/263083/albert-douglas-davis-v-united-states/#303" aria-description="Citation for case: Albert Douglas Davis v. United States">327 F.2d 301, 303</a></span> (9th Cir.1964), the police did what any person could do — they knocked on the front door of a residence, hut did not use their authority as police officers to command the occupants to open the door. When the occupant opened the door, he did so voluntarily, not, as Dennis Winsor did, in response to a claim of lawful authority.</blockquote>
<p id="b1471-16"><em>Winsor, </em><span class="citation" data-id="9477657"><a href="/opinion/506186/united-states-v-steven-dale-winsor/#1573" aria-description="Citation for case: United States v. Steven Dale Winsor">846 F.2d at 1573</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b1471-17">. <em>Accord United States v. Carrion, </em><span class="citation" data-id="482020"><a href="/opinion/482020/united-states-v-anthony-nicholas-carrion-and-fred-solmor/#1128" aria-description="Citation for case: United States v. Anthony Nicholas Carrion and Fred Solmor">809 F.2d 1120, 1128</a></span> (5th Cir.1987) (a suspect standing in an open doorway stands in a public place). <em>But cf. United States v. Morgan, </em><span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158</a></span>, 1166 n. 2 (6th Cir.1984) (P<em>ayton </em>requires exigent circumstances before a warrantless arrest can be made of an individual standing in the doorway of a private residence.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Vasquez-Algarin.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Vasquez-Algarin
type: case
citation: "821 F.3d 467 (2016)"
parallel_cite: ""
neutral_cite: "2016 U.S. App. LEXIS 7889; 2016 WL 1730540"
court: 3d Cir. 2016
court_level: coa
circuit: ca3
year: 2016
date_decided: 2016-05-02
docket: 15-1941
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
  opinion_url: "https://www.courtlistener.com/opinion/3199633/united-states-v-johnny-vasquez-algarin/"
  cluster_id: 3199633
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Vasquez-Algarin
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Arrest in the Home]]"
    role: Key
related:
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[Steagald v. United States]]"
  - "[[Maryland v. Buie]]"
tags:
  - case
  - fourth-amendment
  - arrest-warrant
  - home-entry
  - probable-cause
  - reason-to-believe
  - third-circuit
holding: "To force entry into a dwelling to execute an arrest warrant, officers must have probable cause — not a lesser 'reasonable belief' — that the suspect both resides at and is present within the home; joining the Fifth, Sixth, Seventh, and Ninth Circuits, the Third Circuit held that Payton's 'reason to believe' language means probable cause, and because the officers here forced entry into a residence that was not shown to be the arrestee's home on that standard, the denial of suppression was reversed."
aliases:
  - United States v. Vasquez-Algarin
  - "United States v. Vasquez-Algarin (3d Cir. 2016)"
---

# United States v. Vasquez-Algarin

*821 F.3d 467 (3d Cir. 2016)* (No. 15-1941) · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 3199633 → lead opinion 3199527 (Krause, J.; 821 F.3d 467, decided 2016-05-02); Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star-pagination *477). S9 promotes. -->

## Background
Officers holding an arrest warrant for one individual forced entry into a residence to execute it. Johnny Vasquez-Algarin — who, the record showed, was neither the person named in the warrant nor connected to that arrestee — was found and arrested inside, and evidence recovered there was used against him. He moved to suppress, arguing the officers lacked a sufficient basis to believe that the residence they entered was the named suspect's home. The district court denied suppression, appearing to assume that a probable-cause standard was satisfied, and Vasquez-Algarin appealed, presenting the open question of how certain officers must be before forcing entry into a dwelling to make an arrest.

## Issue
Whether the "reason to believe" that officers must have under *[[Payton v. New York]]* before forcing entry into a residence to execute an arrest warrant — that the suspect resides there and is present — requires probable cause or something less.

## Rule
An arrest warrant carries limited authority to enter the suspect's own dwelling to make the arrest, but only when officers have adequate grounds to believe the suspect lives there and is then present; the Third Circuit held those grounds must rise to probable cause. As the court put it: "we join the Fifth, Sixth, Seventh and Ninth Circuits in holding that Payton's 'reason to believe' language amounts to a probable-cause standard." — 821 F.3d at 477. ^pin-477

## Application
Reading *[[Payton v. New York|Payton]]* in the context of the Supreme Court's Fourth Amendment jurisprudence, the court concluded that the "reason to believe" phrase was used interchangeably with "probable cause" within the bounded factual setting *[[Payton v. New York|Payton]]* addressed, and that the profound protection the Constitution affords the home compels the more demanding standard. Requiring probable cause that the suspect both resides at and is present within the dwelling is the only conclusion commensurate with those protections — particularly where, as here, the person found inside was a third party unconnected to the arrest warrant, implicating the *[[Steagald v. United States|Steagald]]* concern for the privacy of those not named in the warrant. The court cabined its holding to the *[[Payton v. New York|Payton]]* context, disclaiming any effect on the separate reasonable-suspicion line. Because the entry was not justified on the probable-cause standard the court adopted, the suppression ruling could not stand.

## Conclusion
The Third Circuit **reversed** the denial of the suppression motion and [[Reading and Citing Cases#on-remand|remanded]], declining to reach Vasquez-Algarin's separate sentencing challenge. Judge Krause wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Vasquez-Algarin* is a leading circuit statement that *[[Payton v. New York|Payton]]*'s "reason to believe" is a **probable-cause** standard — that officers need probable cause the suspect both **resides at** and **is present in** a home before forcing entry on an arrest warrant. Teach it with *[[Steagald v. United States|Steagald]]* (a search warrant is required to enter a **third party's** home) and note the acknowledged circuit split, with some courts treating "reason to believe" as a lesser standard than probable cause.

## Appears on
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Vasquez-Algarin*, 821 F.3d 467 (3d Cir. 2016)](https://www.courtlistener.com/opinion/3199633/united-states-v-johnny-vasquez-algarin/) — pinpoint: 477 (*Payton*'s "reason to believe" requires probable cause; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b5444ecdc7224fe", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Vasquez-Algarin"}, "payload": {"all": [{"cite": "821 F.3d 467", "page": "467", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "821"}, {"cite": "2016 U.S. App. LEXIS 7889", "page": "7889", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}, {"cite": "2016 WL 1730540", "page": "1730540", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}], "display": "821 F.3d 467", "official": {"cite": "821 F.3d 467", "page": "467", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "821"}, "official_selection_present": true, "record_id": "United States v. Vasquez-Algarin"}}
{"assertion_id": "c01b420b304f6964", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Vasquez-Algarin"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Vasquez-Algarin", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Vasquez-Algarin

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Vasquez-Algarin",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Johnny Vasquez-Algarin",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America v. Johnny VASQUEZ-ALGARIN, Appellant",
    "input_case_name": "United States v. Vasquez-Algarin",
    "court": "3d Cir. 2016",
    "court_id": "ca3",
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2016-05-02",
    "year": 2016,
    "docket": "15-1941",
    "cluster_id": 3199633,
    "lead_opinion_id": 3199527,
    "sibling_ids": [],
    "absolute_url": "/opinion/3199633/united-states-v-johnny-vasquez-algarin/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "821 F.3d 467",
      "volume": "821",
      "reporter": "F.3d",
      "page": "467",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. App. LEXIS 7889",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "7889",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1730540",
        "volume": "2016",
        "reporter": "WL",
        "page": "1730540",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "821 F.3d 467",
        "volume": "821",
        "reporter": "F.3d",
        "page": "467",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 7889",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "7889",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1730540",
        "volume": "2016",
        "reporter": "WL",
        "page": "1730540",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "821 F.3d 467",
    "official_selection": {
      "court_class": "coa",
      "selected": "821 F.3d 467",
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
    "date_created": "2026-07-06T05:59:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-vasquez-algarin--3199633",
      "to_record_id": "United States v. Vasquez-Algarin",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Vasquez-Algarin

```
                                        PRECEDENTIAL

      UNITED STATES COURT OF APPEALS
           FOR THE THIRD CIRCUIT
                _____________

                    No. 15-1941
                   _____________

          UNITED STATES OF AMERICA


                          v.

          JOHNNY VASQUEZ-ALGARIN,
                               Appellant
               _______________

    On Appeal from the United States District Court
        for the Middle District of Pennsylvania
             (D.C. No. 1-11-cr-00200-001)
       District Judge: Honorable Sylvia Rambo
                   _______________

              Argued: February 11, 2016

Before: FUENTES, KRAUSE, and ROTH Circuit Judges.

                 (Filed: May 2, 2016)
                  _______________
Ronald A. Krauss, Esq.
Frederick W. Ulrich, Esq. (Argued)
Office of Federal Public Defender
100 Chestnut Street
Suite 306
Harrisburg, PA 17101

               (Counsel for Appellant)

Daryl F. Bloom, Esq. (Argued)
Stephen R. Cerutti, II, Esq.
Office of United States Attorney
228 Walnut Street, P.O. Box 11754
220 Federal Building and Courthouse
Harrisburg, PA 17108

               (Counsel for Appellee)

                      _______________

                 OPINION OF THE COURT
                     _______________

KRAUSE, Circuit Judge.

        Law enforcement officers need both an arrest warrant
and a search warrant to apprehend a suspect at what they
know to be a third party’s home. If the suspect resides at the
address in question, however, officers need only an arrest
warrant and a “reason to believe” that the individual is
present at the time of their entry. This case sits between these
two rules and calls on us to decide their critical point of
inflection: how certain must officers be that a suspect resides




                               2
at and is present at a particular address before forcing entry
into a private dwelling?

       A careful examination of the Supreme Court’s Fourth
Amendment jurisprudence reveals that the standard cannot be
anything less than probable cause. Because here, law
enforcement acted on information that fell short of the
standard, we will vacate the conviction and remand to the
District Court.

I.     Background

       A.     Facts

       In 2010, an arrest warrant was issued for Edguardo
Rivera,1 a suspect in a homicide case. Deputy U.S. Marshal
Gary Duncan, a member of the Dauphin County Fugitive
Task Force, received information from another law
enforcement officer and from street informants that Rivera
was “staying” or “residing” at an address on North 13th Street
in Harrisburg, Pennsylvania. App. 25–26, 35–36. With the
arrest warrant for Rivera in hand, Deputy Marshal Duncan
and officers from the Harrisburg Bureau of Police and the
Dauphin County Drug Task Force arrived at the apartment
and knocked on the door. They received no response but
“heard a lot of movement inside,” as well as a phone ring
once or twice and stop ringing and a dog bark and cease
barking, giving the officers the impression that a person had


       1
         The District Court uses a different spelling than the
party briefs and the court transcripts, referring to the suspect
as “Edwardo Rivera.”




                               3
manually silenced the phone and muzzled the dog. App. 29–
30. The officers then forcibly entered the home.

        As it turned out, however, the sought fugitive, Rivera,
did not live in the apartment and was not present.2 Instead,
upon entering, the officers saw Appellant Johnny Vasquez-
Algarin, and, during a protective sweep, they identified in
plain view sandwich baggies, a razor blade, and what
appeared to be powder cocaine. After Vasquez-Algarin
declined to grant consent for a search, one officer obtained a
search warrant while the other officers waited at the
apartment. During the subsequent search conducted pursuant
to the warrant, the officers discovered ammunition, unused
plastic bags, and hundreds of small black bands, as well as a
cell phone in the master bedroom that was later searched
pursuant to another search warrant. At some point during the
search, the officers identified a set of car keys, which they
used to open a stolen Mazda located across from the
apartment.      Vasquez-Algarin, who had no outstanding
warrants, was then arrested.

       B.     Proceedings

       Vasquez-Algarin and the two brothers with whom he
shared the apartment were each charged with distribution and
possession with intent to distribute cocaine in violation of 21
U.S.C. § 841(a)(1) and (b)(1)(A)(ii) and conspiracy to do the
same in violation of 21 U.S.C. § 846. In October 2013,
Vasquez-Algarin pleaded not guilty to the charges.


       2
        The record contains no evidence of any connection
between the two men.




                              4
       The month before trial, Vasquez-Algarin moved to
suppress the evidence seized from the North 13th Street
residence, arguing that law enforcement’s forced entry into
the apartment was unconstitutional. At his suppression
hearing, the Government presented three witnesses, all
officers involved in various stages of Vasquez-Algarin’s
apprehension and arrest. Two witnesses, Deputy Marshal
Duncan and Middletown Borough Police Detective Dennis
Morris, testified about the sounds that officers heard coming
from inside the residence on their arrival, but only Deputy
Marshal Duncan could speak to the circumstances that led
law enforcement to Vasquez-Algarin’s residence.

        Deputy Marshal Duncan testified that he had an arrest
warrant for Edguardo Rivera and was given “reliable”
information from a detective from the Harrisburg Bureau of
Police and informants that Rivera lived at the North 13th
Street address. App. 25, 26. During cross-examination, when
defense counsel pressed Deputy Marshal Duncan to elaborate
on “the exact factors” that led him to believe that Rivera lived
at the address, Deputy Marshal Duncan reiterated that he had
relied on “[i]nformation being provided to me by another law
enforcement officer, information that we had from informants
on the street that that address was being used by Mr. Rivera.”
App. 36. When counsel asked if, prior to going to the
residence, Deputy Marshal Duncan had checked records for
the resident of the apartment, he confirmed that he had but
was unable to recall whether he had identified the renter of
the apartment.

       The District Court denied Vasquez-Algarin’s motion
to suppress, concluding from Deputy Marshal Duncan and
Detective Morris’s testimony that the officers had a
“reasonable belief” and “probable cause to believe” that the




                               5
fugitive, Rivera, resided at the apartment and was present at
the time of the officers’ entry and that their entry was
therefore constitutional.3 United States v. Vasquez-Algarin,
No. 1:11-CR-0200-01, 2014 WL 1672008, at *1–2 (M.D. Pa.
Apr. 28, 2014). At trial the next month, Deputy Marshal
Duncan provided substantially the same information about
what had led him to the North 13th Street address to
apprehend Rivera.4 However, he offered a different answer to

       3
          At the suppression hearing, there was some question
as to Vasquez-Algarin’s standing to challenge the search
because he testified that the apartment was merely rented in
his name and that he had moved out two months before the
search, leaving only his dog in the apartment with his
brothers. He further represented he was in the apartment at
the time of the search only because he had received a call
from the landlord about problems with the rent and
electricity. The District Court determined that the master
bedroom belonged to Vasquez-Algarin, “as he could not
identify key details related to his alleged other residence, and
was the individual on the lease of the 142 North 13th Street
residence and kept possessions therein,” and expressly
rejected as “not credible” Vasquez-Algarin’s claim that he no
longer resided at the apartment at the time of the search.
Vasquez-Algarin, 2014 WL 1672008, at *2 n.2. In addition,
Vasquez-Algarin maintained at the suppression hearing that
he had standing to assert a Fourth Amendment claim, and the
Government does not now challenge his standing.
       4
         Specifically, at trial Deputy Marshal Duncan testified
that the U.S. Marshals Service “received information that Mr.
Rivera could possibly be residing at an address on North 13th
Street,” App. 136, and that “the information . . . was provided




                               6
a question he also had been asked at the suppression hearing
about why he spent significant time knocking and yelling at
the door. At the suppression hearing, Deputy Marshal
Duncan had testified that often residents will not come to the
door for law enforcement but “if we stay there for a while,
and you continue to knock and continue to not leave, typically
you’ll gain some response from somebody inside.” App. 29.
In his trial testimony, however, he identified a second reason
he knocked for so long at the door in this case: “The address
was not the address of record for Mr. Rivera, so we wanted to
knock and attempt to gain contact with somebody inside and
gain their consent to search the address.” App. 138.

       After a two-day trial, a jury convicted Vasquez-
Algarin on both drug counts. He now appeals the District
Court’s denial of his suppression motion.5 We review the
District Court’s legal conclusions de novo and the underlying
factual findings for clear error. United States v. Torres, 534
F.3d 207, 209 (3d Cir. 2008). In the present context, where
we are reviewing the denial of a motion to suppress to

to [him] by a detective from the City of Harrisburg who
received the information that Mr. Rivera may be staying
there,” App. 137.
      5
          The District Court had jurisdiction pursuant to 18
U.S.C. § 3231, and we have jurisdiction pursuant to 28 U.S.C.
§ 1291. Because we vacate the conviction, we do not reach
the second issue Vasquez-Algarin raises on appeal, whether
the District Court committed clear error in applying a two-
level sentencing enhancement for Vasquez-Algarin’s role as
an organizer, leader, manager or supervisor in the criminal
activity under § 3B1.1(c) of the U.S. Sentencing Guidelines.




                              7
determine whether police officers had probable cause to
believe the subject of their arrest warrant lived in the
apartment they entered, we may look to the entire record and
are “not restricted to the evidence presented at the
suppression hearing where the motion was denied.” United
States v. Silveus, 542 F.3d 993, 1001 (3d Cir. 2008) (quoting
Gov’t of the V.I. v. Williams, 739 F.2d 936, 939 (3d Cir.
1984)).

II.   Discussion

       Vasquez-Algarin argues that law enforcement officers
needed a search warrant to enter the North 13th Street
apartment because the subject of their arrest warrant (the
“arrestee”6) did not in fact reside there. As we will explain
below, however, their entry was constitutional if they had
sufficient information to support a reasonable belief that the
arrestee resided at and was present within the targeted home.
To determine what reasonable belief requires, we will look to
the principles set forth in the Supreme Court’s key
precedents, the views expressed by our sister Circuits and,
most importantly, the fundamental tenets of Fourth

      6
         The term “arrestee” is usually used to describe an
individual who was been arrested, see Black’s Law
Dictionary (10th ed. 2014) (defining “arrestee” as “[s]omeone
who has been taken into custody by legal authority; a person
who has been arrested”), but in the Payton context, the courts
regularly use the term to refer to the intended target of the
arrest warrant. For ease of reference, we use the term in this
sense throughout the opinion, although the person eventually
arrested in this case differed from the person named on the
warrant.




                              8
Amendment jurisprudence governing the home. We conclude
that to satisfy the reasonable belief standard law enforcement
required, but lacked, probable cause. The officers’ entry was
therefore unconstitutional and, because the good-faith
exception to the exclusionary rule is inapplicable here, the
evidence seized from Vasquez-Algarin’s apartment should
have been suppressed.




                              9
       A.     Payton and Steagald

        The Supreme Court has issued two major decisions
regarding the constitutionality of in-home arrests. Because
here law enforcement officers believed, albeit mistakenly,
that the home they were entering was the residence of the
subject of their arrest warrant, the controlling authority is the
first of these decisions, Payton v. New York, 445 U.S. 573
(1980).      There, the Supreme Court considered two
consolidated cases in which police officers entered private
residences without any kind of warrant to make routine felony
arrests and held that the state statutes that had authorized
these warrantless entries were unconstitutional; the officers
were required to have an arrest warrant to arrest a suspect in
his home. Id. at 602–03. In a dictum that has since evolved
into a tenet of Fourth Amendment jurisprudence, the Court
also observed that a search warrant would not be required in
that circumstance because “an arrest warrant founded on
probable cause implicitly carries with it the limited authority
to enter a dwelling in which the suspect lives when there is
reason to believe the suspect is within.” Id. at 603 (emphasis
added).

       In the wake of Payton, to assess the constitutionality of
an officer’s entry into a home to execute an arrest warrant, the
Courts of Appeals have drawn upon the Supreme Court’s
language to develop a two-prong test that extends to
residency: the officer must have a “reasonable belief”7 that


       7
         Close examination reveals the Courts of Appeals
have uniformly cast Payton’s “reason to believe” language as
a reasonable belief standard. See, e.g., United States v.
Gorman, 314 F.3d 1105, 1114–15 (9th Cir. 2002). However,




                               10
(1) the arrestee resides at the dwelling, and (2) the arrestee is
present at the time of the entry. See, e.g., United States v.
Veal, 453 F.3d 164, 167 (3d Cir. 2006) (quoting United States
v. Gay, 240 F.3d 1222, 1226 (10th Cir. 2001)).

        A different framework applies, however, where
officers believe an individual for whom they have an arrest
warrant is a guest in a third-party home. A year after handing
down Payton, the Supreme Court held in Steagald v. United
States, 451 U.S. 204 (1981), that officers may not enter a
third party’s residence to execute an arrest warrant without
first obtaining a search warrant “based on their belief that [the
suspect] might be a guest there,” unless the search is
consensual or justified by exigent circumstances. Id. at 213,
216. In so reasoning, the Court rejected the Government’s
argument as to the “practical problems [that] might arise if
law enforcement officers are required to obtain a search
warrant before entering the home of a third party to make an
arrest,” and concluded that “the inconvenience incurred by
the police is simply not that significant” and in any event
“cannot outweigh the constitutional interests at stake.” Id. at
220–22.

       Before us is a case of mistaken belief that underscores
the tension between the residency test that the Courts of
Appeals have derived from Payton and the relatively robust
Fourth Amendment protections guaranteed to third-party
homes under Steagald.8 Because officers may force entry

as discussed infra in Section II.B, they diverge on what that
standard requires.
       8
         Vasquez-Algarin was not the arrestee sought nor, as
far as the record shows, connected to the arrestee in any way.




                               11
into a home as long as they have a reasonable belief the
suspect resides and is present there, but must have nothing
short of a search warrant where the suspect is a guest in a
third party’s home, law enforcement’s assessment of a
suspect’s residency is, in effect, a determination of the level
of protection to which a dwelling is entitled. Our choice
about how much and what kind of information must form the
basis for that critical determination thus affects not only the
homes of arrestees but also any home that could be mistaken
for one. For that reason, we must draw not only from the
principles laid out in Payton but also from those set forth in
Steagald when determining just how stringent the reasonable
belief standard must be. With these principles in mind, we
next consider our own precedent relevant to this issue and the
case law of our sister Circuits that have addressed the issue
squarely, but with divergent results.

      B.     The reasonable belief standard

      Vasquez-Algarin contends that this Court has already
equated “reason to believe” or “reasonable belief” with a
probable cause standard, and the District Court appears to
have assumed probable cause applied as well. Vasquez-
Algarin, 2014 WL 1672008, at *1. The issue, however,
remains an open question in our Circuit.


This distinguishes this case from any of our relevant
precedents and from many of the cases in which other Courts
of Appeals have had occasion to interpret and apply the
Payton reasonable belief standard. See, e.g., Veal, 453 F.3d
164 (defendant was the intended arrestee); United States v.
Agnew, 407 F.3d 193 (3d Cir. 2005) (same).




                              12
       Vazquez-Algarin is correct that we treated reasonable
belief and probable cause as equivalent in United States v.
Agnew, 407 F.3d 193 (3d Cir. 2005). There, in applying the
Payton reasonable belief test, we observed that “police may
enter a suspect’s residence to make an arrest armed only with
an arrest warrant if they have probable cause to believe that
the suspect is in the home.” Id. at 196. Yet in that case the
government possessed sufficient information to meet the
standard irrespective of its precise definition, so we had no
occasion to analyze the point and it had no effect on our
holding. Recognizing as much, we observed the following
year in Veal that although “[o]ur Court . . . has described the
test using the language of ‘probable cause,’” the courts had
taken different approaches to the question, and we decided,
under these circumstances, that we would “determine whether
a possibly lower standard of reasonable belief should be
applied” another day. 453 F.3d at 167 n.3.

       That day has arrived. Because a number of our sister
Circuits have opined on this issue, we review their
approaches for their persuasive value before staking out our
own. As described below, these approaches vary widely:
Although the Courts of Appeals once overwhelmingly
interpreted reasonable belief as less stringent than probable
cause, they are now nearly evenly divided on this point.9


      9
        In the last decade, a number of Courts of Appeals
have expressed agreement with the Ninth Circuit’s
longstanding view that reasonable belief amounts to probable
cause. See United States v. Harper, 928 F.2d 894, 897 (9th
Cir. 1991), overruled on other grounds by United States v.
King, 687 F.3d 1189, 1189 (9th Cir. 2012) (en banc) (per
curiam); accord United States v. Jackson, 576 F.3d 465, 469




                              13
       The D.C., First, Second and Tenth Circuits have
determined that reasonable belief requires less than probable
cause.10 See United States v. Thomas, 429 F.3d 282, 286
(D.C. Cir. 2005); United States v. Werra, 638 F.3d 326, 337
(1st Cir. 2011); United States v. Lauter, 57 F.3d 212, 215 (2d
Cir. 1995); Valdez v. McPheters, 172 F.3d 1220, 1224–25
(10th Cir. 1999). But those courts have offered little by way
of explanation for this interpretation. In Thomas, the D.C.
Circuit observed that, to date, most of the appellate courts had
determined that reasonable belief is a less stringent standard
than probable cause and that it was “more likely . . . that the
Supreme Court in Payton used a phrase other than ‘probable
cause’ because it meant something other than ‘probable
cause.’” 429 F.3d at 286. In Valdez, the Tenth Circuit
offered a more detailed explanation for its adoption of a
standard less stringent than probable cause, but rather than
explaining why probable cause would be inappropriate, the
court focused entirely on the impracticability of imposing on

(7th Cir. 2009); United States v. Hardin, 539 F.3d 404, 416 &
n.6 (6th Cir. 2008); see also United States v. Barrera, 464
F.3d 496, 501 & n.5 (5th Cir. 2006) (equating the two terms
and describing the disagreement among the appellate courts
as “semantic”); United States v. Route, 104 F.3d 59, 62 (5th
Cir. 1997) (analogizing reasonable belief to probable cause
but ultimately rejecting the latter standard).
       10
          Even those courts that agree that reasonable belief is
a lower standard than probable cause disagree on its precise
definition. Compare, e.g., Gay, 240 F.3d at 1227 (describing
reasonable belief and reasonable suspicion as “two different
legal standards”); with Werra, 638 F.3d at 337 (equating
reasonable belief to reasonable suspicion).




                              14
officers an “actual knowledge” requirement, which none of
the Courts of Appeals has imposed in applying Payton. See
Valdez, 172 F.3d at 1224–25 (10th Cir. 1999) (criticizing the
Ninth Circuit’s adoption of the probable cause standard in
part because “requiring actual knowledge of the suspect’s true
residence would effectively make Payton a dead letter”). But
see United States v. Hill, 649 F.3d 258, 274 (4th Cir. 2011)
(Agee, J., dissenting) (“[N]o court applying [Payton] has ever
held[] that the police must have seen the defendant nearby or
have actual knowledge that he is inside a residence before
they can enter.”); United States v. Magluta, 44 F.3d 1530,
1535 (11th Cir. 1995) (“[P]robable cause itself is a doctrine of
reasonable probability and not certainty.”).

       The Fifth, Sixth, Seventh and Ninth Circuits have
endorsed—or, in the case of the Seventh Circuit, “inclined”
toward—interpreting reasonable belief as the equivalent, or
functional equivalent, of probable cause. See United States v.
Barrera, 464 F.3d 496, 500-01 & n.5 (5th Cir. 2006); United
States v. Hardin, 539 F.3d 404, 415–16 & n.6 (6th Cir. 2008);
United States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009);
United States v. Gorman, 314 F.3d 1105, 1114–15 (9th Cir.
2002). 11 To reach this conclusion, some of these Courts of
Appeals have looked to the Supreme Court’s own post-

       11
          The Sixth Circuit has reconsidered its position on
the issue. In Hardin, the Sixth Circuit rejected as dictum its
previous determination in United States v. Pruitt that
reasonable belief is a less stringent standard than probable
cause, and, in new dictum, endorsed Judge Clay’s concurring
opinion in Pruitt that equated the two standards. Hardin, 539
F.3d at 415 & n.6 (citing United States v. Pruitt, 458 F.3d
477, 490 (6th Cir. 2006) (Clay, J., concurring)).




                              15
Payton characterization of its “reason to believe” language, as
well as the terms with which the Court has generally defined
the probable cause standard.

        Most notably, in Maryland v. Buie, 494 U.S. 325
(1990), when considering whether officers executing a home
arrest pursuant to Payton could also perform a protective
sweep of the residence, the Supreme Court concluded that
“[p]ossessing an arrest warrant and probable cause to believe
Buie was in his home, the officers were entitled to enter and
to search anywhere in the house in which Buie might be
found.” Id. at 332–33 (emphasis added). According to the
Sixth and Ninth Circuits, this passage is most naturally read
to mean that the Supreme Court intended the Payton “reason
to believe” language to serve as a reference to probable cause.
See Hardin, 539 F.3d at 416 n.6 (“Had the Court truly
intended the ‘reason to believe’ language in Payton to set
forth a new, lesser standard, surely the Court in Buie would
have explained that the officers were entitled to be inside
Buie’s residence on the basis of an arrest warrant and a
‘reasonable belief’ as to Buie’s presence, but the Court used
the term ‘probable cause’ instead.”); accord Gorman, 314
F.3d at 1114.12


       12
          As these courts have pointed out, Justice White’s
description of the majority opinion in his dissent in Payton
provides additional support for interpreting Payton’s “reason
to believe” language as a reference to probable cause.
Hardin, 539 F.3d at 410; Gorman, 314 F.3d at 1114 & n.10.
His disagreement with the majority was predicated in part on
his understanding that “under [the majority’s] decision, the
officers apparently need an extra increment of probable cause
when executing the arrest warrant, namely, grounds to believe




                              16
        As further evidence that reasonable belief amounts to
probable cause, some of these Courts of Appeals have also
considered the Supreme Court’s tendency to explain and
define the term “probable cause” using “grammatical
analogues” of “reason to believe.” Hardin, 539 F.3d at 416
n.6 (citing Pruitt, 458 F.3d at 490 (Clay, J., concurring)). For
example, the Court has described probable cause as requiring
a “reasonable ground for belief.” Pruitt, 458 F.3d at 490
(Clay, J., concurring) (quoting Maryland v. Pringle, 540 U.S.
366, 370–71 (2003); Ybarra v. Illinois, 444 U.S. 85, 91
(1979)); see also Illinois v. Gates, 462 U.S. 213, 243 (1983)
(suggesting that “probable cause” is synonymous with
“‘reasonable grounds’ to believe”).

        Among the Courts of Appeals that have equated
reasonable belief with probable cause, the Fifth Circuit is
notable in that it has also concluded that “the courts that
distinguish the terms have done so because ‘probable cause’
is a term of art.” See Barrera, 464 F.3d at 501 & n.5 (citing
United States v. Woods, 560 F.2d 660 (5th Cir. 1977); United
States v. Route, 104 F.3d 59, 62 (5th Cir. 1997)). We do not
necessarily agree with the suggestion in Barrera that the
disagreement among the Circuits as to whether reasonable
belief equates to probable cause is “more about semantics
than substance.” Id. The D.C. Circuit, for instance, appears
to require significantly less evidence to support a belief of
residency than the other Courts of Appeals, presumably in
part as a result of its choice to depart from the probable cause
standard and the protections it affords. See, e.g., Thomas, 429
F.3d at 286 (holding that officers had requisite reasonable

that the suspect is within the dwelling.” Payton, 445 U.S. at
616 n.13 (White, J., dissenting) (emphasis added).




                              17
belief to enter residence where arresting marshals provided no
testimony about where they had obtained the parolee’s
address except to say that an “investigation was done” and the
address “turned up”).

        We do agree with the Fifth Circuit, however, that
probable cause has specialized usage and is not a standard
typically applied by police to settle a question of the kind
before us about where an individual lives.13 Although the
Supreme Court has long insisted on a “practical,
nontechnical” definition of probable cause, Gates, 462 U.S. at
231 (quoting Brinegar v. United States, 338 U.S. 160, 176
(1949)), describing it as a “fluid concept” that defies
“reduc[tion] to a neat set of legal rules,” id. at 232, the
fluidity of the concept has not translated into diverse
application. A close reading of the case law shows that the
Supreme Court uses the “probable cause” standard almost
exclusively to assess the basis and strength of an officer or

       13
           The awkwardness that the Fifth Circuit has
identified, of applying the probable cause standard in the
Payton context, see Route, 104 F.3d at 62, may be a function
of the appellate courts’ recasting of the Payton “reason to
believe” standard—which the Supreme Court used to describe
only whether the arrestee was present within the residence—
as a two-part test in which that same standard governs both
whether the dwelling is the arrestee’s residence and whether
the arrestee is inside. Applying the probable cause standard
to determine only whether the arrestee is present within the
home presents no such difficulties. Cf. Steagald, 451 U.S. at
213–14 n.7 (“[T]he plain wording of the Fourth Amendment
admits of no exemption from the warrant requirement when
the search of a home is for a person rather than for a thing.”).




                              18
magistrate’s belief that a particular person has committed a
particular crime or that an article subject to seizure can be
found at a particular location—in short, whether criminal
activity is afoot. See, e.g., Brinegar, 338 U.S. at 175 (“The
substance of all the definitions of probable cause is a
reasonable ground for belief of guilt.” (internal quotation
marks omitted)).

        The Supreme Court’s general practice of reserving
probable cause language to these circumstances perhaps helps
account for the Eighth and Eleventh Circuits’ decision to
simply treat reasonable belief as its own standard for purposes
of applying the Payton test. The Eleventh Circuit in Magluta,
observing that “it is difficult to define the Payton ‘reason to
believe’ standard, or to compare the quantum of proof the
standard requires with the proof that probable cause requires,”
side-stepped the comparison altogether and treated the inquiry
as, in essence, its own reasonableness determination. 44 F.3d
at 1535–36 (citing Woods, 560 F.2d at 665); accord United
States v. Risse, 83 F.3d 212, 216–17 (8th Cir. 1996)
(employing a similar test and citing Magluta).14 Relying on
the same case law as the Fifth Circuit in Barrera, the
Eleventh Circuit thus opted for a “practical interpretation of
Payton” that resembles probable cause in that “in order for
law enforcement officials to enter a residence to execute an
arrest warrant for a resident of the premises, the facts and
      14
          Although Woods predated Payton, the Eleventh
Circuit has deemed the cases consistent. Magluta, 44 F.3d at
1536. Decisions of the former Fifth Circuit rendered prior to
October 1, 1981, are precedent in the Eleventh Circuit.
Bonner v. City of Prichard, 661 F.2d 1206, 1209 (11th Cir.
1981) (en banc).




                              19
circumstances within the knowledge of the law enforcement
agents, when viewed in the totality, must warrant a reasonable
belief that the location to be searched is the suspect’s
dwelling, and that the suspect is within the residence at the
time of entry.” Magluta, 44 F.3d at 1535; cf. Gates, 462 U.S.
at 238 (explaining that, for purposes of a probable cause
determination, a “totality of the circumstances” analysis
requires the magistrate issuing a warrant “simply to make a
practical, common-sense decision whether . . . there is a fair
probability that contraband or evidence of a crime will be
found in a particular place.”).

       C.     Reasonable belief as probable cause

        Having considered the different approaches of our
sister Circuits and their reasoning where provided, we join the
Fifth, Sixth, Seventh and Ninth Circuits in holding that
Payton’s “reason to believe” language amounts to a probable
cause standard.15 As explained more fully below, we do so
for two reasons. First, the Supreme Court’s use of the phrase
“reason to believe,” when considered in the context of Payton
and more generally the Court’s Fourth Amendment
jurisprudence, supports a probable cause standard. Second,
and more fundamentally, requiring that law enforcement

       15
          The Seventh Circuit has stated its “inclin[ation] to
adopt the view . . . that ‘reasonable belief’ is synonymous
with probable cause,” Jackson, 576 F.3d at 469, and the Sixth
Circuit has endorsed the view that the two standards are
synonymous in what it conceded was dictum, Hardin, 539
F.3d at 415–16 & n.6.




                              20
officers have probable cause to believe their suspect resides at
and is present within the dwelling before making a forced
entry is the only conclusion commensurate with the
constitutional protections the Supreme Court has accorded to
the home.

       We consider first the Court’s use of the term “reason
to believe” in Payton and other criminal cases. On careful
reading, Payton appears to be a case in which the Court used
the terms “probable cause” and “reason to believe” in close
proximity and interchangeably. This is readily apparent when
we examine how the Payton Court couched its analysis.
Expressly “put[ting] to one side related problems that are not
presented today,” the Court noted that neither of the
consolidated cases before it in Payton involved exigent
circumstances or consent, the home of a third party, or
allegations “that the police lacked probable cause to believe
that the suspect was at home when they entered.” Payton,
445 U.S. at 582–84. It is within this carefully bounded
factual framework—the search of an arrestee’s home without
exigent circumstances or consent but with probable cause to
believe he was present—that the Court concluded its decision
with the observation that “an arrest warrant founded on
probable cause implicitly carries with it the limited authority
to enter a dwelling in which the suspect lives when there is
reason to believe the suspect is within.” Id. at 603.

       Payton is not an anomaly. On several occasions, the
Supreme Court has used the very same “reason to believe”
language that appears in Payton as a stand-in for “probable
cause.” For example, in the landmark case Berger v. New
York, 388 U.S. 41 (1967), where the Court held that the
wiretapping statute in question violated the Fourth
Amendment       because    it   authorized     suspicionless




                              21
eavesdropping, the Court explained that “[t]he purpose of the
probable cause requirement of the Fourth Amendment [is] to
keep the state out of constitutionally protected areas until it
has reason to believe that a specific crime has been or is
being committed.” Id. at 59 (emphases added). In Gerstein v.
Pugh, 420 U.S. 103 (1975), the Court likewise observed that
at common law the justice of the peace would “determine
whether there was reason to believe the prisoner had
committed a crime” and that this “initial determination of
probable cause” could be reviewed on a writ of habeas
corpus. Id. at 114–15. And in Cardwell v. Lewis, 417 U.S.
583 (1974) (plurality opinion), after recounting all of the
evidence that established that police had “probable cause to
search [the suspect’s] car,” the Court concluded that the
resulting composite “provided reason to believe that the car
was used in the commission of the crime.” Id. at 592.
Examples of this kind serve to undercut the D.C. Circuit’s
conclusion that Payton’s “reason to believe” should be
construed loosely simply because the Court elected to use a
phrase other than “probable cause” to describe the requisite
belief law enforcement must have that an arrestee is present
in his dwelling at the time of the search. Thomas, 429 F.3d at
286.

        Although the language of Payton and the Supreme
Court’s other Fourth Amendment decisions provides strong
support for interpreting reasonable belief as a probable cause
standard, it is the nature of the privacy interests at stake that
solidifies our conclusion.16 Without question, the home takes


       16
         We recognize that there are limits to parsing
language alone to determine what the Supreme Court
intended by its use of the phrase “reason to believe” in




                               22
pride of place in our constitutional jurisprudence. As the
Supreme Court has reiterated on numerous occasions, “when
it comes to the Fourth Amendment, the home is first among
equals. At the Amendment’s ‘very core’ stands ‘the right of a
man to retreat into his own home and there be free from


Payton, because the Court has not adhered to hard and fast
rules when using “reasonableness” language. For example,
the Court has sometimes referred to “reasonable belief” when
discussing “reasonable suspicion,” see, e.g., Buie, 494 U.S. at
336–37; United States v. Place, 462 U.S. 696, 703–04 (1983),
a practice that has been cited by at least one Court of Appeals
to suggest Payton may require less than probable cause, see,
e.g., Pruitt, 458 F.3d at 484. The Court’s references to
“reasonable belief” outside the Payton context, however, have
little relevance to our inquiry, particularly as the phrase
“reasonable belief” does not actually appear in Payton and
using it as shorthand for “reason to believe” is an adaptation
of the Courts of Appeals. Conversely, our holding today that
the “reason to believe” or short-hand “reasonable belief”
standard equates to probable cause is limited to the Payton
context and should not be construed to mean that “reasonable
belief,” “reasonable grounds to believe,” or a substantially
similar iteration means probable cause in other circumstances.
While the Supreme Court has occasionally discussed
reasonable suspicion in terms of “reasonable belief,” for
example, reasonable suspicion is “obviously less demanding”
than probable cause, United States v. Sokolow, 490 U.S. 1, 7
(1989), and nothing we have said today bears on that line of
cases, see, e.g., United States v. Arvizu, 534 U.S. 266 (2002);
Alabama v. White, 496 U.S. 325 (1990); Terry v. Ohio, 392
U.S. 1 (1968).




                              23
unreasonable governmental intrusion.’” Florida v. Jardines,
133 S. Ct. 1409, 1414 (2013) (quoting Silverman v. United
States, 365 U.S. 505, 511 (1961)). Indeed, such intrusion is
“the chief evil against which the wording of the Fourth
Amendment is directed.” Payton, 445 U.S. at 585.

       The vaunted place of the home in our constitutional
privacy jurisprudence was central to the Supreme Court’s
analysis in Payton and Steagald. See, e.g., Payton, 445 U.S.
at 585–90; Steagald, 451 U.S. at 220, 222. These cases
together provide insight that neither case provides alone—
insight that leads inexorably to the conclusion that the
Circuit-created two-prong test is workable only if governed
by a robust reasonableness standard akin to probable cause,
and that anything less would defeat the “stringent . . .
protection” the home is due. United States v. Martinez-
Fuerte, 428 U.S. 543, 561 (1976) (private homes are
“ordinarily afforded the most stringent Fourth Amendment
protection”).

       On one hand, adopting a too-rigorous interpretation of
“reason to believe” seems at odds with the portion of Payton
leading up to the Court’s articulation of the “reason to
believe” rule:

      It is true that an arrest warrant requirement may
      afford less protection than a search warrant
      requirement, but it will suffice to interpose the
      magistrate's determination of probable cause
      between the zealous officer and the citizen. If
      there is sufficient evidence of a citizen’s
      participation in a felony to persuade a judicial
      officer that his arrest is justified, it is
      constitutionally reasonable to require him to




                             24
       open his doors to the officers of the law. Thus,
       for Fourth Amendment purposes, an arrest
       warrant founded on probable cause implicitly
       carries with it the limited authority to enter a
       dwelling in which the suspect lives when there
       is reason to believe the suspect is within.

Payton, 445 U.S. at 602–03 (emphasis added). This language
seems to cut against interpreting the “reason to believe”
standard too stringently insofar as the Court clearly indicates
that the probable cause determination required for an arrest
warrant already offers much of the requisite protection.
Payton, by its terms, however, applies only with respect to an
individual for whom an arrest warrant has been issued and
with respect to the place where he resides. See id. at 583.

       On the other hand, where there is uncertainty about
where the arrestee resides—a situation not presented in
Payton but encompassed within the Circuit-created two-prong
test—we must take care not to adopt an interpretation of
“reason to believe” that requires of law enforcement so little
evidence that an arrestee resides at a dwelling as to expose all
dwellings to an unacceptable risk of police error and
warrantless entry. Here, Steagald comes into play, for to
adopt such an interpretation would be to disregard the
explanation the Court provides there for why it chose to
distinguish Payton and to conclude, in effect, that the homes
of fugitives and non-fugitives are entitled to different degrees
of Fourth Amendment protection:

       Because an arrest warrant authorizes the police
       to deprive a person of his liberty, it necessarily
       also authorizes a limited invasion of that
       person’s privacy interest when it is necessary to




                              25
      arrest him in his home. This analysis, however,
      is plainly inapplicable when the police seek to
      use an arrest warrant as legal authority to enter
      the home of a third party to conduct a search.
      Such a warrant embodies no judicial
      determination whatsoever regarding the person
      whose home is to be searched. Because it does
      not authorize the police to deprive the third
      person of his liberty, it cannot embody any
      derivative authority to deprive this person of his
      interest in the privacy of his home. Such a
      deprivation must instead be based on an
      independent showing that a legitimate object of
      a search is located in the third party’s home.
      We have consistently held, however, that such a
      determination is the province of the magistrate,
      and not that of the police officer.

Steagald, 451 U.S. at 214 n.7 (emphasis added). Like
Payton, Steagald does not contemplate the possibility of
uncertain residency, nor does it address the proper means of
resolving that uncertainty. But read alongside Payton, the
Court’s reasoning in Steagald makes clear that its
determination of the legality of a forced home entry in this
context turns on whether the officer has the benefit of some
type of probable cause determination by a neutral arbiter, be
that by way of an arrest warrant or search warrant.

       Given this precedent and the constitutional principles
at stake, law enforcement armed with only an arrest warrant
may not force entry into a home based on anything less than
probable cause to believe an arrestee resides at and is then
present within the residence. A laxer standard would effect
an end-run around the stringent baseline protection




                             26
established in Steagald and render all private homes—the
most sacred of Fourth Amendment spaces—susceptible to
search by dint of mere suspicion or uncorroborated
information and without the benefit of any judicial
determination. Such intrusions are “the chief evil against
which the wording of the Fourth Amendment is directed.”
Payton, 445 U.S. at 585. We therefore join those Courts of
Appeals that have held that reasonable belief in the Payton
context “embodies the same standard of reasonableness
inherent in probable cause.” Gorman, 314 F.3d at 1111;
accord Barrera, 464 F.3d at 501.

      D.      Application

       Having defined the reasonable belief standard as
equivalent to probable cause, we have no trouble concluding
that law enforcement did not meet that standard as to either
prong of the Payton test here, and the District Court erred in
concluding otherwise.

       To make a probable cause determination, we must
consider the “totality of the circumstances,” Silveus, 542 F.3d
at 1000 (citing Gates, 462 U.S. at 238), which, in the context
of second-hand information, encompasses considerations
such as the basis and reliability of the information and the
receiving officer’s ability to corroborate its content, United
States v. Ritter, 416 F.3d 256, 262–64 (3d Cir. 2005) (citing
Alabama v. White, 496 U.S. 325 (1990)).

       Here, to meet Payton’s first prong, Deputy Marshal
Duncan relied entirely on informant tips and the word of
another detective but provided little information by which the
District Court could assess the information he obtained. At
the suppression hearing, Deputy Marshal Duncan explained




                              27
only that he had based his belief that the intended arrestee,
Rivera, lived at the North 13th Street address on information
conveyed to him by another officer and by informants. He
did not identify the number of informants, their reliability
based on any prior interactions he may have had with them,
the specific information they related, or even whether he
obtained information from “informants on the street” first-
hand or through the other officer. App. 36. Nor did he
describe with any specificity the information provided by that
other officer or the basis for that officer’s statement. See
Whiteley v. Warden, 401 U.S. 560, 568 (1971) (“[A]n
otherwise illegal arrest cannot be insulated from challenge by
the decision of the instigating officer to rely on fellow
officers to make the arrest.”); Rogers v. Powell, 120 F.3d 446,
453 (3d Cir. 1997) (“[S]tatements by fellow officers
conveying that there is probable cause for a person’s arrest,
by themselves, cannot provide the “facts and circumstances”
necessary to support a finding of probable cause . . . . The
legality of a seizure based solely on statements issued by
fellow officers depends on whether the officers who issued
the statements possessed the requisite basis to seize the
suspect.”).

       In his trial testimony, moreover, Deputy Marshal
Duncan cast further doubt on the reasonableness of his belief
that the dwelling was Rivera’s residence when he explained
that the officers knocked vigorously and waited at the door
for a prolonged period in part because “[t]he address was not
the address of record for Mr. Rivera, so we wanted to knock
and attempt to gain contact with somebody inside and gain
their consent to search the address.” App. 138. This
explanation suggests that, at the time of entry, Deputy
Marshal Duncan not only had limited basis to believe Rivera




                              28
resided at the apartment but also possessed evidence that gave
him significant doubt. Cf. Hill, 649 F.3d at 263–64 (officers
did not have reason to believe arrestee was present, because,
among other things, police had documented another residence
for arrestee based on a recent traffic citation, and the lead
officer on the scene testified that he did not believe the
arrestee would be present).

        Nor are we persuaded that the Government met its
burden as to Payton’s second prong, i.e., that it established
probable cause to believe Rivera was present in the apartment
by way of the suspicious sounds the officers heard coming
from inside. True, the Government's burden at this stage is
not onerous, for the threshold determination that there is
probable cause to believe the home is the arrestee’s residence
not only entitles that home to lesser protections under Payton
but also, as a logical matter, increases the likelihood the
arrestee can be found within it. See Payton 445 U.S. at 602
(recognizing “that an arrest warrant requirement may afford
less protection than a search warrant requirement”). Thus,
once the predicate of residency is established, that alone
carries significant weight in establishing probable cause to
believe the arrestee is present, necessarily reducing the
quantum of proof needed to meet Payton’s second prong in
the totality of the circumstances analysis.

       Ultimately, however, that analysis must be made on a
case-by-case basis, accounting not only for the fact that there
is an increased likelihood the arrestee will be found in his
own home but also for other indicia supporting law
enforcement’s belief that the suspect is then inside. See, e.g.,
United States v. Diaz, 491 F.3d 1074, 1078 (9th Cir. 2007)
(officers reasonably believed that arrestee was home because
he himself told government agents that he was usually home




                              29
during the day, they knew he worked at home as a mechanic,
and when they had previously visited he was absent only
once); Pruitt, 458 F.3d at 483 (officers had reasonable belief
parolee was inside the residence where, among other things,
an individual exiting the residence matched the parolee’s
picture to the person selling drugs inside); United States v.
Beck, 729 F.2d 1329, 1331–32 (11th Cir. 1984) (per curiam)
(“Beck’s car, identified by the agents, was parked nearby; and
it was reasonable to believe that one would be at home at 7:30
a.m. and be sound asleep . . . .” (footnote omitted)).

        Here, because the officers lacked probable cause to
believe Rivera lived in the home, mere signs of life inside,
even if suspicious, could not establish probable cause to
believe he was present and could not justify their warrantless
entry into Vasquez-Algarin’s apartment.          Indeed, such
bootstrapping would be clearly untenable as a logical matter,
for law enforcement cannot compensate for the deficiency of
the information underlying its belief that a suspect even lives
at a particular residence by way of generic evidence
indicating merely that someone is inside the home. Cf. Shea
v. Smith, 966 F.2d 127, 131 (3d Cir. 1992) (observing that
“[i]f the police lack probable cause to believe the suspect is
an actual resident, but have probable cause to believe he’s
present, they must get a search warrant.” (quoting Harper,
928 F.2d at 896)).

       In sum, we note that on both prongs of the Payton test,
the information that law enforcement relied upon to justify
breaking into Vasquez-Algarin’s apartment contrasts sharply
in kind and quantity from the information deemed sufficient
by this Court and other Courts of Appeals applying the
probable cause standard. See, e.g., Veal, 453 F.3d at 168
(officers lawfully entered the home of the arrestee’s wife




                              30
where the parole violation warrant indicated he was no longer
living at his last known address and listed his wife as a
possible lead, his former landlord reported that the couple had
lived together in the apartment they rented from him, and the
car the arrestee allegedly drove was registered to his wife and
parked near her home); Route, 104 F.3d at 62–63 (officer
confirmed that the arrestee’s credit card applications, utility
bills and vehicle registration matched the address of the
residence, and at the residence observed a known associate
backing out of the driveway, another vehicle in the driveway,
and noise coming from a television inside the home);
Jackson, 576 F.3d at 469 (concluding “the police had enough
evidence to easily satisfy a probable cause standard” where
they received a tip that the arrestee was residing at a friend’s
apartment and, on their arrival, the arrestee’s girlfriend
confirmed he was inside).

       Just as private citizens are provided protection from
mistaken arrest by the requirement that law enforcement have
probable cause to believe they committed the crime in
question, private homes must be protected from mistaken
entry by, at minimum, a probable cause determination as to
whether the suspect sought even lives there. Because the
officers lacked information sufficient to meet that threshold in
this case, their entry into Vasquez-Algarin’s home and the
subsequent searches were unconstitutional, and, absent some
exception to the exclusionary rule, the evidence they seized
should have been suppressed. We turn, then, to the
Government’s argument that one such exception is
applicable.




                              31
      E. The good-faith exception

       The Government argues that even if officers
unlawfully entered Vasquez-Algarin’s home, his conviction
should stand because the exclusionary rule has no application
and the evidence is admissible under the good-faith exception
where law enforcement’s conduct was not “deliberate,
reckless, or grossly negligent.” Gov’t Br. at 24–25 (citing
Herring v. United States, 555 U.S. 135 (2009)). We are not
persuaded on these facts by the Government’s invocation of
the good-faith exception.

       The Supreme Court has “over time applied [the] good-
faith exception across a range of cases” where applying the
exclusionary rule would not “yield ‘appreciable deterrence.’”
Davis v. United States, 131 S. Ct. 2419, 2426, 2428 (2011)
(quoting United States v. Janis, 428 U.S. 433, 454 (1976)).
For example, the Court has held that, under the good-faith
exception, evidence need not be suppressed where police
conduct a search in “objectively reasonable reliance” on a
search warrant subsequently deemed invalid, United States v.
Leon, 468 U.S. 897, 922 (1984), or on a statute subsequently
held unconstitutional, Illinois v. Krull, 480 U.S. 340, 360
(1987).

       Drawing on this line of cases, in Davis, the Supreme
Court held that “[e]vidence obtained during a search
conducted in reasonable reliance on binding precedent is not
subject to the exclusionary rule.” 131 S. Ct. at 2429. And in
our en banc decision in United States v. Katzin, 769 F.3d 163
(3d Cir. 2014), this Court, in turn, relied on Davis and the
Supreme Court’s prior good-faith decisions to conclude that
the exception applies not only where law enforcement agents
act on binding appellate precedent but also, and more




                             32
fundamentally, where the officers act “upon an objectively
reasonable good faith belief in the legality of their conduct.”
Id. at 182.

       In neither respect is the exception warranted in this
case. First, the Government does not purport to rely on
binding appellate precedent for its assertion that the officers
had sufficient information to forcibly enter Vasquez-
Algarin’s home, nor could it in view of the binding Supreme
Court authority in Payton and Steagald that points the other
way. Even Herring—which the Government cites not as
binding appellate precedent on these facts but for the general
proposition that a finding of a Fourth Amendment violation
does not compel automatic reversal—weighs in favor of
suppression. Herring involved a county’s inadvertent failure
to update its database concerning a recalled arrest warrant—
“isolated negligence attenuated from the arrest” that the Court
determined was not “sufficiently deliberate that exclusion can
meaningfully deter it” or “sufficiently culpable that such
deterrence is worth the price paid by the justice system.” 555
U.S. at 137–38, 144. In contrast, here we are confronted not
with an inadvertent recordkeeping error but with a deliberate
decision to force entry into a home based on only vague and
uncorroborated information as to whether the subject of the
arrest warrant even lived there. The gulf between this case
and Herring is only reinforced by Deputy Marshal Duncan’s
trial testimony acknowledging documentation in his
possession that caused him concern that this was a third-party
residence for which he needed consent to search.

       We thus turn to the second and more fundamental
inquiry we undertook in Katzin, the “objectively ascertainable
question whether a reasonably well trained officer would
have known that the search was illegal under all of the




                              33
circumstances.” 769 F.3d at 179 (quoting Leon, 468 U.S. at
922 n.23). In making this determination, we consider the
decisions set forth by the Supreme Court, our Court and our
sister Circuits. See id. at 182–84. As is apparent from our
survey of the case law, however, those decisions also favor
suppression.

        Read together, Payton and Steagald make clear that,
because of the sanctity of the home, nothing less than
probable cause is appropriate when it comes to determining
whether a home belongs to an arrestee and to undertaking a
forced entry on the basis of an arrest warrant alone. See
supra Section II.A. As for our own precedent, although we
have clarified today that “reasonable belief” in the Payton
context does indeed amount to probable cause, our decisions
to date have assumed as much and used probable cause as the
applicable standard. See Veal, 453 F.3d at 167 n.3; Agnew,
407 F.3d at 196. Lastly, where this Court and our sister
Circuits have upheld the validity of police entries into homes
under Payton, it has been on the basis of far more specific and
reliable information than what the officers relied upon here to
enter Vasquez-Algarin’s apartment, see Section II.D, and
conversely, where the only evidence available has been of
such meager quantity and quality, the Courts of Appeals have
held that suppression is appropriate, see, e.g., Werra, 638
F.3d at 341; Hardin, 539 F.3d at 427. Thus, in contrast with
Katzin, where “[t]he constellation of circumstances that
appeared to authorize [the officers’] conduct included well
settled principles of Fourth Amendment law as articulated by
the Supreme Court [and] a near-unanimity of circuit courts
applying these principles to the same conduct,” 769 F.3d at
182, the very opposite is true here.




                              34
       We do not take lightly the “significant social costs of
suppressing reliable, probative evidence.” Id. However, we
are compelled to enforce the exclusionary rule where law
enforcement officers, “at the time they acted, would have or
should have known their [conduct] w[as] unconstitutional.”
Id. at 179. The Government’s argument in this case boils
down to the proposition that law enforcement officers may
forcibly enter a home based on nothing more than the general
representation of another law enforcement officer and the
vague and uncorroborated assertions of unidentified
informants that the intended arrestee lives there. We reject
this position as inconsistent with fundamental Fourth
Amendment principles and the language and logic of
Supreme Court precedent governing in-home arrests. Given
the dictates of Payton and Steagald, our prior applications of
Payton in Veal and Agnew, and the out-of-Circuit precedent
consistently holding law enforcement to a higher bar than
what was proffered here to justify a forced home entry, we
conclude the officers’ conduct was, at a minimum, “grossly
negligent,” and thus was “sufficiently deliberate that
exclusion can meaningfully deter it, and sufficiently culpable
that such deterrence is worth the price paid by the justice
system.” Herring, 555 U.S. at 144.

III.   Conclusion

       For the foregoing reasons, we will reverse the District
Court’s denial of Vasquez-Algarin’s motion to suppress,
vacate the conviction, and remand for proceedings consistent
with this opinion.




                             35

```

---
