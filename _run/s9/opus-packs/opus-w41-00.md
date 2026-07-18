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

## GROUP: content/cases/United States v. Giordano.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Giordano
type: case
citation: "416 U.S. 505 (1974)"
parallel_cite: "94 S. Ct. 1820; 40 L. Ed. 2d 341"
neutral_cite: 1974 U.S. LEXIS 36
court: U.S.
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-05-13
docket: 72-1057
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
  opinion_url: "https://www.courtlistener.com/opinion/109020/united-states-v-giordano/"
  cluster_id: 109020
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Giordano
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: Anchor
related:
  - "[[Electronic Surveillance and Title III]]"
  - "[[United States v. Donovan]]"
  - "[[Scott v. United States]]"
tags:
  - case
  - fourth-amendment
  - electronic-surveillance
  - title-iii
  - wiretap
  - suppression
  - attorney-general-authorization
holding: "Under 18 U.S.C. § 2516(1), only the Attorney General or an Assistant Attorney General specially designated by him may authorize a Title III wiretap application; where an application was in fact approved by the Attorney General's Executive Assistant rather than a statutorily designated official, the interception was 'unlawfully intercepted' and the evidence — including evidence derived under a later extension order — must be suppressed, because the senior-approval requirement directly and substantially implements Congress's purpose of confining wiretaps to situations that clearly warrant them."
aliases:
  - United States v. Giordano
  - "United States v. Giordano (1974)"
---

# United States v. Giordano

*416 U.S. 505 (1974)* (No. 72-1057) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109020 → combined opinion 109020 (White, J.; 416 U.S. 505, argued Jan. 8, 1974, decided May 13, 1974). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*527`). S9 promotes. -->

## Background
In a narcotics investigation, an Assistant United States Attorney applied for a Title III wiretap on Giordano's Maryland telephone. The application recited that Assistant Attorney General Will Wilson — a specially designated official under § 2516(1) — had authorized it. In fact, the initial October 16, 1970 application had been reviewed and approved not by Wilson or the Attorney General, but by the Attorney General's *Executive Assistant*, who signed off believing the Attorney General would approve and caused the Attorney General's initials to be placed on the authorization. A November 6 extension application was approved by the Attorney General himself. The District Court suppressed the evidence for misidentification of the authorizing official, and the Fourth Circuit affirmed, holding the interceptions "unlawfully intercepted."

## Issue
Whether § 2516(1) permits someone other than the Attorney General or a specially designated Assistant Attorney General (here, the Executive Assistant) to authorize a wiretap application, and whether, if not, the resulting evidence — and evidence derived from a later extension — must be suppressed under §§ 2515 and 2518(10)(a).

## Rule
The Court held that only the named officials may authorize a wiretap application and that this requirement is one whose violation compels suppression. Rejecting the Government's argument that § 2518(10)(a)(i) reaches only constitutional violations, the Court set the test for statutory suppression: "The words 'unlawfully intercepted' are themselves not limited to constitutional violations, and we think Congress intended to require suppression where there is failure to satisfy any of those statutory requirements that directly and substantially implement the congressional intention to limit the use of intercept procedures to those situations clearly calling for the employment of this extraordinary investigative device." — 416 U.S. at 527. ^pin-527

## Application
The pre-application approval requirement — conditioning any wiretap on the judgment of a senior Justice Department official — was exactly such a requirement — one the Court found central to the statutory scheme — so suppression had to follow when it was ignored. The Executive Assistant's approval, however confident he was of the Attorney General's likely views, did not satisfy § 2516(1). And the November 6 extension evidence, though the extension itself was approved by the Attorney General, was "derived" from the unlawfully intercepted October communications and so was likewise suppressed.

## Conclusion
The judgment of the Court of Appeals for the Fourth Circuit was **affirmed**. White, J., delivered the opinion of the Court, with separate opinions concurring and concurring in part and dissenting in part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Giordano* supplies Title III's suppression test — evidence is suppressed for violating a statutory requirement only when that requirement "directly and substantially" implements Congress's intent to limit wiretapping — and holds the senior-approval requirement to be one of them. Teach it as the anchor of that test, paired with its companion *[[United States v. Donovan]]* (identification and inventory-notice violations, by contrast, do *not* require suppression) and *[[Scott v. United States]]* on minimization.

## Appears on
- [[Electronic Surveillance and Title III]] — *Anchor*

## Sources
- [*United States v. Giordano*, 416 U.S. 505 (1974)](https://www.courtlistener.com/opinion/109020/united-states-v-giordano/) — pinpoint: 527 (White, J., for the Court; the CL opinion text carries the reporter star `*527` immediately before the quoted suppression-standard sentence). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f1e20d7721679e2e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "416 U.S. 505 (1974)", "court": "U.S.", "neutral_cite": "1974 U.S. LEXIS 36", "official_citation_present": true, "parallel_cite": "94 S. Ct. 1820; 40 L. Ed. 2d 341", "title": "United States v. Giordano", "year": "1974"}}
{"assertion_id": "74c2c30775609614", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under 18 U.S.C. § 2516(1), only the Attorney General or an Assistant Attorney General specially designated by him may authorize a Title III wiretap application; where an application was in fact approved by the Attorney General's Executive Assistant rather than a statutorily designated official, the interception was 'unlawfully intercepted' and the evidence — including evidence derived under a later extension order — must be suppressed, because the senior-approval requirement directly and substantially implements Congress's purpose of confining wiretaps to situations that clearly warrant them.", "title": "United States v. Giordano"}}
{"assertion_id": "d734a4bac72ee3d3", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Anchor", "title": "United States v. Giordano"}}
{"assertion_id": "63296ac60aa2a0e0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Giordano"}}
{"assertion_id": "d548e867d2ae6c93", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Giordano", "varies_by_point": "false"}}
```

### lake record — United States v. Giordano

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Giordano",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Giordano",
    "case_name_short": "Giordano",
    "case_name_full": "UNITED STATES v. GIORDANO Et Al.",
    "input_case_name": "United States v. Giordano",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-05-13",
    "year": 1974,
    "docket": "72-1057",
    "cluster_id": 109020,
    "lead_opinion_id": 9425702,
    "sibling_ids": [],
    "absolute_url": "/opinion/109020/united-states-v-giordano/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "416 U.S. 505",
      "volume": "416",
      "reporter": "U.S.",
      "page": "505",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 1820",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 341",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 36",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 U.S. 505",
        "volume": "416",
        "reporter": "U.S.",
        "page": "505",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 1820",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1820",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 341",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 36",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "36",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "416 U.S. 505",
    "official_selection": {
      "court_class": "scotus",
      "selected": "416 U.S. 505",
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
    "date_created": "2026-07-07T13:25:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:25:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:25:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-giordano--109020",
      "to_record_id": "United States v. Giordano",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Giordano

```
<opinion type="majority">
<author id="b575-12">Mr. Justice White</author>
<p id="AnO">delivered the opinion of the Court.</p>
<p id="b575-13">Title III-of the Omnibus Crime Control and Safe Streets Act UU1968, <span class="citation no-link">82 Stat. 211</span>-225, 18 U. S. C.' §§ 2510-2520, prescribes the procedure for securing judicial authority to intercept wire communications in the investigation of specified serious offenses. The Court must here determine whether the Government sufficiently complied with the required application procedures in this case and whether, if not, evidence obtained as a result of such surveillance, under a court order based on the applications, is admissible at the criminal trial of those whose conversations were overheard. In particular, we must decide whether the provision of <span class="citation no-link">18 U. S. C. <page-number citation-index="1" label="508">*508</page-number>§ 2516</span> (1)<footnotemark>1</footnotemark> conferring power , on the “Attorney General, or any .Assistant Attorney General specially designated by the Attorney General” to “authorize an application to a Federal judge ... for ... an order authorizing or approving the interception of wire or oral communications” by federal investigative agencies seeking evidence of certain designated offenses permits the Attorney General’s Executive Assistant to validly authorize a wiretap application to be made. We conclude, that Congress did not intend the power to authorize wiretap applications to be exercised by any individuals other than the Attorney General or an Assistant Attorney General specially designated by him and that primary or derivative evidence secured by wire interceptions pursuant to a court order issued in response to an application which was, in fact, not authorized by one of the statutorily designated officials must be suppressed under <span class="citation no-link">18 U. S. C. § 2515</span> upon a motion properly made under <span class="citation no-link">18 U. S. C. § 2518</span> (10)(a). Accordingly, we affirm the judgment of the Court of Appeals.</p>
<p id="b576-5">I</p>
<p id="b576-6">In the'course of an initial investigation of suspected narcotics dealings on the part of respondent Giordano, it developed that Giordano himself sold narcotics to an undercover agent on October 5, 1970, and also told an informant to call a specified number when interested in transacting narcotics business. Based on this and other information, Francis Brocato, an Assistant United States Attorney, on October 16, 1970, submitted an application to the Chief Judge of the District of Maryland for an order permitting interception of the communications of Giordano, and of others as yet unknown, to or from Giordano’s telephone. The application recited that <page-number citation-index="1" label="509">*509</page-number>Assistant Attorney General Will Wilson had been'specially designated by the Attorney General to authorize the application. Attached to the application was a letter -from Will Wilson to Brocato which stated that Wilson had reviewed Brocato’s request for authorization and had made the necessary probable-cause determinations and which then purported tb authorize Brocato to proceed with the application to the court. Also attached were various affidavits'of law enforcement officers stating the reasons and justification for the proposed ^interception.. Upon reviewing the application, the Chief Judge, issued an order on the same day authorizing the interception “pursuant to application authorized by the Assistant Attorney General . . . Will Wilson, who has been specially designated in this proceeding by the Attorney General ... to exercise the powers conferred on him by [<span class="citation no-link">18 U. S. C. §2516</span>].” On November 6, the same judge extended the intercept authority based on an application similar in form to the original, but also including information obtained from the interception already authorized and carried out and extending the authority to conversations óf additional named individuals calling from or to Giordano’s telephoné. The interception was terminated on November' 18 when Giordano and the other respondents were- arrested and charged with viola- ' tions of the narcotics laws..</p>
<p id="b577-5">Suppression hearings'followed pretrial notification by the Government, see § 2518 (9), that it intended tó use in evidence the results of the court-authorized interceptions of communications on Giordano’s telephone. It developed at the hearings'that the applications for interception authority presented to the District Court had inaccurately described the official who had' authorized the applications and that neither the initial application for the October 16 order nor the application for the <page-number citation-index="1" label="510">*510</page-number>November 6 extension order had been approved and authorized by Assistant Attorney General Will Wilson, as the applications had indicated. An affidavit of the Executive Assistant to the Attorney General divulged that he, the Executive Assistant, had reviewed the request for authorization to apply for the initial order, had concluded, from his “knowledge of the Attorney General’s actions on previous cases, that he would approve the request if submitted to him,” and, because the Attorney General was then on a trip- away from Washington,. D. C., and pursuant to authorization by the Attorney General for him to do so in such circumstances, had approved the request and caused the Attorney General’s initials to be placed on a memorandum to Wilson instructing him to authorize Brocato to proceed. The affidavit also stated that the Attorney General himself had approved the November 6 request for extension and had initialed the memorandum to Wilson designating him to authorize Brocato to make application for an .extension' order. It was also revealed that although the applications recited that they had been authorized by Will Wilson, he had not himself reviewed Brocato’s applications, and that his action was at best only formal authorization to Brocato. Furthermore, it became apparent that Wilson did not himself sign either of the letters bearing his name‘and accompanying the applications io the District Court. Instead, it appeared that someone in Wilson’s office had affixed his signature after the signing of the letters had been authorized by a Deputy Assistant Attorney General in the Criminal .Division who had, in turn, acted after the approval of the request for authorization had occurred in and had -been received from the Office of the Attorney General.</p>
<p id="b578-4">. The District Court sustained the motions to suppress on the ground that the officer in the Justice Department <page-number citation-index="1" label="511">*511</page-number>approving each application had been misidentified in the applications and intercept orders, in • violation of <span class="citation no-link">18 U. S. C. §§ 2518</span> (l)(a). and (4)(d), <em>United States </em>v. <em>Focarile, </em><span class="citation" data-id="1445598"><a href="/opinion/1445598/united-states-v-focarile/#1060" aria-description="Citation for case: United States v. Focarile">340 F. Supp. 1033, 1060</a></span> (Md. 1972). On the Government’s pretrial appeal under <span class="citation no-link">18 U. S. C. § 3731</span>, the Court of Appeals affirmed on the different ground that the authorization of the October 16 wiretap application by the Attorney General’s Executive Assistant violated § 2516 (1) .of the statute and struck at “the very heart” of Title III, thereby requiring suppression of the wiretap and derivative evidence under §§ 2515 and 2518 (10)(a)(i) and (ii).<footnotemark>2</footnotemark> <span class="citation multiple-matches"><a href="/c/F.%202d/469/522/">469 F. 2d 522</a></span>, 531 (CA4 1972). We granted certiorari to resolve- the' conflict with decisions of the Court of Appeals for the Second Circuit<footnotemark>3</footnotemark> <page-number citation-index="1" label="512">*512</page-number>with, respect to the administration of the circumscribed authority Congress has granted in Title III for the use of wiretapping and wiretap evidence by law enforcement officers. <span class="citation multiple-matches"><a href="/c/U.%20S./411/905/">411 U. S. 905</a></span>.</p>
<p id="b580-5">II</p>
<p id="b580-6">The United States contends that the authorization of intercept applications by the Attorney General’s Executive Assistant was not-inconsistent with the statute and that even if it were, there being no constitutional violation, the wiretap and derivative evidence should not have been ordered suppressed. We disagree with both contentions.<footnotemark>4</footnotemark></p>
<p id="b580-7">Turning first to whether the statute permits the authorization of wiretap applications by. the Attorney General’s Executive Assistant, we begin with the lan<page-number citation-index="1" label="513">*513</page-number>guage of § 2516 (1), which provides that “[t]he Attorney-General, or any Assistant Attorney General specially designated by the Attorney General, may authorize” an application for intercept authority. Plainly enough, the Executive Assistant is neither the Attorney General nor a specially designated Assistant Attorney General; but the United States argues that <span class="citation no-link">28 U. S. C. § 509</span>,<footnotemark>5</footnotemark> deriving from the Reorganization Acts of 1949 and 1950, vests all functions of the. Department of Justice, with some exceptions, in the Attorney General, and that Congress characteristically assigns newly created duties to the Attorney General rather than to the Department of Justice, thus making essential the provision for delegation appearing in <span class="citation no-link">28 U. S. C. §510</span>:</p>
<blockquote id="b581-5">“The Attorney General may from time to time make such provisions as he considers appropriate authorizing the performance by any other officer, employee, or agency of the Department of Justice of any function of the Attorney General.”</blockquote>
<p id="b581-6">It is therefore argued that merely vesting a duty in the Attorney General, as it is said Congress did in § 2516 (1), evinces no intention whatsoever to preclude delegation to other officers in the Department of Justice, including those on the Attorney General's own staff.</p>
<p id="b582-3"><page-number citation-index="1" label="514">*514</page-number>As a general proposition, the argument is unexceptionable. But here the matter of delegation is expressly addressed by § 2516, and the power of the Attorney General in this respect is specifically limited to delegating his authority to ‘ any Assistant Attorney General specially designated by the Attorney General.” Despite § 510, Congress does not always contemplate that the duties assigned to ,the Attorney»-General may be freely delegated. Under the Civil Rights Act of 1968, for instance, certain prosecutions are authorized only on the certification of the Attorney General or the Deputy Attorney General, “which function of certification may not be delegated.” <span class="citation no-link">18 U. S. C. § 245</span> (a)(1). Equally precise language forbidding delegation wás not employed in the legislation-before us; but we think § 2516 (1), fairly read, was intended to limit the power to ’authorize wiretap applications to the Attorney General himself and to any Assistant Attorney General he might designate. This interpretation of the statute is. also strongly supported by its purpose and legislative history.</p>
<p id="b582-4">The purpose of the legislation, which was passed in 1968, was effectively to prohibit, on the pain of criminal and civil penalties,<footnotemark>6</footnotemark> all interceptions of oral and wire communications, except those specifically provided for in the Act, most notably those interceptions permitted to law enforcement officers when authorized by court order in connection with the investigation of the serious crimes listed’ in § 2516. Judicial wiretap orders must be preceded by applications containing prescribed information, § 2518 (1). The judge must make certain findings before authorizing interceptions, including/the existence of probable cg¡use, § 2518 (3). The orders themselves <page-number citation-index="1" label="515">*515</page-number>must particularize the extent and nature of the interceptions that they authorize, § 2518 (4), and they expire within a specified time unless expressly extended by a judge based on further application by enforcement, officials, § 2518 (5). Judicial supervision of the progress of the interception is provided for, § 2518 (6), as is official control of the custody of any recordings or tapes produced by the interceptions carried out pursuant to the order, § 2518 (8). The Act also contains provisions specifying the circumstances and procedures under and by which aggrieved persons may seek and obtain orders for the suppression of intercepted wire or oral communications sought to. be used in evidence by the Government. § 2518 (10) (a).</p>
<p id="b583-5">The Act is not as. clear in some respects as it mignt be, but it is at once apparent that it not only limits the crimes for which intercept authority may be obtained but also imposes important preconditions to obtaining any intercept authority at all. Congress legislated in considerable detail in providing for applications and orders authorizing wiretapping and evinced the clear intent to make doubly sure that the statutory authority be used with restraint and only where the circumstances warrant the surreptitious interception of wire and oral communications. These procedures were not to be routinely employed as the initial step in criminal investigation. Rather, the applicant must state and the court must find that normal investigative procedures have been tried, and failed or reasonably appear to be unlikely to succeed if tried or to be too dangerous. §§2518 (l)(c) and (3) (c). The Act plainly calls for the prior, informed judgment of enforcement officers desiring court approval for intercept authority, and investigative personnel may not themselves ask a judge for authority to wiretap or eavesdrop. The mature judgment of a particular, <page-number citation-index="1" label="516">*516</page-number>responsible Department of Justice official is interposed as a critical precondition to any judicial order.</p>
<p id="b584-5">The legislative history of the Act supports this view. As we have indicated, the Act was passed in 1968, but the provision of § 2516 requiring approval of applications by the Attorney General or a designated Assistant Attorney General dates from 1961, when a predecessor bill was being, considered in the 87th Congress. Section 4 (b) of that bill, S.' 1495, which was also aimed at prohibiting all but designated official interception, initially provided that the “Attorney General, or any officer of the Department of Justice or any United States Attorney specially designated by the Attorney General, may authorize any investigative or law enforcement officer of the United States or any Federal agency to apply to a judge” for a wire interception order. Hearings oh Wiretapping and Eavesdropping Legislation before the Subcommittee on Constitutional Rights of the Senate Committee on the Judiciary, 87th Cong., 1st Sess.,'5 (1961). Under ..that phraseology, the authority was centered in the Attorney General, but he could empower any officer of the Department of Justice, including United States Attorneys and the Executive Assistant, to authorize applications for intercept orders. At hearings on the bill, the Assistant Attorney General in charge of the Criminal Division stated the views of. the Department of Justice, and the Department later officially proposed, that the authority tq approve applications be substantially narrowed so that the Attorney General could delegate his authority only to an Assistant Attorney General. The testimony was:</p>
<blockquote id="b584-6">“This is the approach of S. 1495, with which the Department of Justice is in general agreement. The bill makes wiretapping a crime unless specifically authorized by a Federal judge in situations involving <page-number citation-index="1" label="517">*517</page-number>specified crimes.' As I understand the bill, the application for a court order- could be made only by the authority of the Attorney General or . an officer of the Department of Justice or ■ U. S. Attorney authorized by him. I suggest that the bill should confine the power to authorize an application for a court order to the Attorney General and any assistant Attorney General whom he may designate. This would give greater assurance of a responsible executive determination of the need and justifiability of each interception.” <em>Id., </em>at 356.</blockquote>
<p id="b585-5">The official proposal was that § 4 (b) be changed tc provide .that the “Attorney General, or any Assistant Attorney General of the Department of Justice specially designated by the Attorney General, may authorise” <em>e, </em>wiretap application. <em>Id., </em>at 372.</p>
<p id="b585-6">■ S. 1495 was not enacted, but its provision limiting those who could approve applications-for. court orders survived and was included in almost identical form in later legislative proposals, including the bill that became Title III of the Act now before us.<footnotemark>7</footnotemark> In the course of <page-number citation-index="1" label="518">*518</page-number>testimony before a House Committee in 1967, the draftsman of the bill containing the basic outline of Title III engaged in the following colloquy:</p>
<blockquote id="b586-5">“The Chairman. . . . About the origin of the application, as I understand it, your bill provides it must be originated by the Attorney General or an Assistant Attorney General.' Am I correct in that regard? &gt;</blockquote>
<blockquote id="b586-6">“Professor Blakey. Yes, you are, Mr. Chairman. ,</blockquote>
<blockquote id="b586-7">“The Chairman. The application must be made by the Attorney General or an Assistant Attorney General.</blockquote>
<blockquote id="b586-8">“Professor Blakey. If I am not mistaken, the present procedure is before any wiretapping or electronic equipment is used now it is generally approved at that level anyway,- Mr. Chairman, and- I would not want this equipment’ used without high level responsible officials passing on it. It may very well be that in some number of cases there will not be time to get the Attorney General to approve it. I think we are going to have just [sic] to let those cases go, and that if this equipment is to be used it ought to be approved by the highest level in the <page-number citation-index="1" label="519">*519</page-number>Department of Justice.. If we cannot make certain cases, that is going to have to be the price we will have to pay.” Hearings on Anti-Crime Program before Subcommittee No. 5 of the House Committee on the Judiciary, 90th Cong., 1st Sess., 1379 (1967).<footnotemark>8</footnotemark></blockquote>
<p id="b588-4"><page-number citation-index="1" label="520">*520</page-number>As it turned out, the House Judiciary Committee' did not report out a wiretap bill, but the House did pass H. R. 5037, entitled the “Law Enforcement and Criminal Justice. Assistance Act of 1967,” 113 Cong. Rec. 21861 (Aug. 8, 1967). The Senate amended that bill by adding to it Title III, which in turn essentially reflected the provisions of S. 917, which had been favorably reported by the Senate Judiciary Committee and which contained the Committee’s own proposals with respect tó the interception of oral and wire communications. The report on the bill stated:</p>
<blockquote id="b588-5">“Section 2516 of the new chapter authorizes the interception of particular wire or oral communication under court order pursuant to the authorization of the appropriate Federal, State, or local prosecuting officer.</blockquote>
<blockquote id="b588-6">“Paragraph (1) . . . centralizes in a .publicly responsible official subject to the political process the formulation of. law enforcement policy on the use of electronic surveillance techniques. Centralization will avoid the possibility that divergent practices might develop. Should abuses occur, the lines of responsibility lead to • an identifiable person. This provision in itself should go a long way toward guaranteeing that no abuses will happen.” S. Rep. No. 1097, 90th Cong., 2d Sess., 96-97 (1968).</blockquote>
<p id="b588-7">This report is particularly significant in that it not only recognizes that the authority to apply for court orders is to be narrowly confined but also declares that it is to be limited to those responsive to the political process, a category to which the Executive Assistant to the Attorney General- obviously does not belong.<footnotemark>9</footnotemark></p>
<p id="b589-3"><page-number citation-index="1" label="521">*521</page-number>The Senate passed H. It. 5037, with the amendments tracking the provisions of S. 917, on May 23, 1968, as the Omnibus Crime Control and Safe Streets Act of 1968, 114 Cong, Rec. 14798 and 14889. During the proceedings leading to the passage of the bill, emphasis was again placed on § 2516. That the Attorney General had the exclusive authority to approve or provide for the approval of wiretap applications was reiterated, and it was made clear that as the bill was drafted no United States Attorney would have or could be given the authority to apply for an intercept order without the advance approval of a senior officer in the Department.<footnotemark>10</footnotemark> <page-number citation-index="1" label="522">*522</page-number>There was no congressional attempt, however, to extend that authority beyond the Attorney General or his Assistant Attorney General designate.</p>
<p id="b590-5">The Government insists that because § 2516 (2) provides for a wider dispersal of authority among state officers to approve wiretap applications and leaves the matter of delegation up to state law,<footnotemark>11</footnotemark> it is inappropriate <page-number citation-index="1" label="523">*523</page-number>to confine the authority so narrowly on the federal level. But it is apparent that Congress desired to centralize and limit this authority where it was feasible to do so, a desire easily implemented in the federal establishment by confining the authority to approve wiretap applications to the Attorney General or a designated Assistant Attorney General. To us, it appears wholly at odds with the scheme and history of the Act to construe § 2516 (1) to permit the Attorney General to delegate his authority at will, whether it be to his Executive Assistant or to any jfiicer'in the Department other than an Assistant Attorney General.<footnotemark>12</footnotemark></p>
<p id="b592-3"><page-number citation-index="1" label="524">*524</page-number>nr</p>
<p id="b592-4">We also reject the Government's contention that even if the approval by "the Attorney General's Executive Assistant of the October 16 application did not comply with the statutory requirements, the evidence obtained from the interceptions should not have been suppressed. The issue does not turn on the judicially fashioned exclusionary rule aimed at deterring violations of Fourth Amendment rights, but upon the provisions of Title <em>III; </em>and, .in our view, the Court of Appeals correctly suppressed the challenged wiretap evidence.</p>
<p id="b592-5">Section 2515 provides that no part of the contents of any wire or oral communication, and no evidence derived therefrom, may be received at certain proceedings, including trials, “if the disclosure of that information would be in violation of this chapter.” What disclosures are forbidden, and are subject to motions to suppress, is in turn governed by § 2518 (10) (a), which provides for suppression of evidence on the following grounds:</p>
<blockquote id="b592-6">“(i) the communication was unlawfully intercepted <em>; .</em></blockquote>
<blockquote id="b593-4"><page-number citation-index="1" label="525">*525</page-number>“(ii) the order of authorization or approval under which it was intercepted is insufficient on its face; or</blockquote>
<blockquote id="Ax1">“(iii) the interception was not'made in conformity with the order of authorization or approval.”<footnotemark>13</footnotemark></blockquote>
<p id="b593-5">The Court of Appeals held that the communications the Government desired to offer in evidence had been “unlawfully intercepted” within the meaning of paragraph (i), because the October application had been approved by the Executive Assistant to the Attorney General rather than by the Attorney General himself or •a designated Assistant Attorney General.<footnotemark>14</footnotemark> We have already determined that delegation to the Executive Assistant was indeed contrary to the statute; but the Government contends that approval by the wrong official is a statutory violation only and that paragraph- (i) must be construed to reach constitutional, but not statutory, Violations.<footnotemark>15</footnotemark> The argument ■ is a straightforward one based on the structure of §2518 (10) (a). On the one hand, the unlawful interceptions referred to in para<page-number citation-index="1" label="526">*526</page-number>graph (i) must include some constitutional violations. Suppression for lack of probable cause, for example, is not provided for in so many words and must fall within paragraph (i) unless, as is most unlikely; the statutory suppression procedures were not intended to reach constitutional violations at all. On the other hand paragraphs (ii) and (iii) plainly reach some purely statutory defaults without constitutional overtones, and these omissions cannot be deemed unlawful interceptions under paragraph (i), else there would have been no necessity for paragraphs (ii). and (iii) — or to pujb the matter another way, if unlawful interceptions under paragraph (i) include purely statutory issues, paragraphs (ii) and (iii) are drained of all meaning and are surplusage. The conclusion of the argument is that if nonconstitutional omissions reached by paragraphs (ii) and (iii) are not unlawful interceptions under paragraph (i), then there is no basis for holding that “unlawful interceptions” include <em>any </em>such statutory matters; the <em>only </em>purely statutory transgressions warranting suppression are those falling within paragraphs (ii) and (iii).</p>
<p id="b594-4">The position gains some support from the fact that predecessor bills specified a fourth ground for suppression — the lack of probable cause — which was omitted in subsequent bills, apparently on the ground that it was not needed because official interceptions without probable cause would be unlawful within the meaning of paragraph (i).<footnotemark>16</footnotemark> k Arguably, the inference is that since <page-number citation-index="1" label="527">*527</page-number>paragraphs (ii) and (iii) were retained, they must have been considered “necessary,” that is, not covered by paragraph (i).</p>
<p id="b595-5">The argument of the United States has substance, and it does appear that paragraphs (ii) and (iii) must be deemed to provide suppression for failure to observe some statutory requirements that would not render interceptions unlawful under paragraph (i). But it does not necessarily follow, and we cannot believe, that no statutory infringements whatsoever are also unlawful interceptions within the meaning of paragraph (i). The words “unlawfully intercepted” are themselves not limited to constitutional violations, and we think Congress intended^ to require suppression where there is failure to satisfy any of those statutory requirements that directly and substantially implement the congressional intention to limit the use of intercept procedures to thosé situations clearly calling for the employment of this extraordinary investigative device. We have already determined that Congress intended not only to limit resort to wiretapping to certain crimes and situations where probable cause is present but also to condition the. usé ,of intercept procedures upon the judgment of a senior .‘official in the Department of Justice that the situation is one of those warranting their use. It is <page-number citation-index="1" label="528">*528</page-number>reasonable to believe that such a precondition would inevitably foreclose resort to wiretapping in various situations where investigative personnel would otherwise seek intercept authority from the court and the court would very likely authorize its use. We are confident that the provision for pre-application approval was intended to play a central role in the statutory scheme and that suppression must follow when it is shown that this statutory requirement has been ignored.</p>
<p id="AiZ">The principal' piece of legislative history relative to this question is S. Rep. No. 1097, 90th Cong., 2d Sess. (1968). The Government emphasizes that the report expressly states that §2518 (10) (a) “largely reflects existing law” and that there was no intention to “press the scope of the suppression role beyond present search and seizure law.” <em>Id., </em>at 96. But the report also states that the section provides for suppression of evidence directly or indirectly obtained “in violation of the chapter” and that the provision “should serve to guarantee that the standards of the new chapter will sharply curtail •the unlawful interception of wire and oral communications.” <footnotemark>17</footnotemark> Moreover, it would not extend existing search- <page-number citation-index="1" label="529">*529</page-number>and-seizure law for Congress to provide for the suppression of evidence obtained in violation of explicit statutory-prohibitions. <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span> (1937); <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939).<footnotemark>18</footnotemark></p>
<p id="b597-4">IV</p>
<p id="b597-5">■Even though suppression of the wire communications intercepted under the October 16, 1970, order is required, the Government nevertheless contends that com<page-number citation-index="1" label="530">*530</page-number>munications intercepted under the Novémber 6 extension order are admissible because they are not “evidence derived” from the contents of communications intercepted under the October 16 order within the meaning of §§ 2515 and 2518 (10)(a). This position is untenable.</p>
<p id="AOzF">Under § 2518, extension orders do not stand on the same footing as original authorizations but are provided for separately. “Extensions of an order may be granted, but only upon application for an extension made in accordance with subsection (1) of this section and the court making the findings required by subsection (3) of this section.” § 2518 (5). Under subsection (1) (e), applications for extensions must reveal previous applications and orders, and under (1) (f) must contain “a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results.” Based on the application, the court is required, to make the same findings that are required in connection with the original order; that is, it must be found not only that there is probable cause in the traditional sense and that normal investigative procedures are unlikely to succeed but also that there is probable cause for believing that particular communications concerning the offense will be obtained through the interception and for believing that the facilities or place from which the wire or oral communications are to be intercepted are used or will be used in connection with the commission of such offense or are under lease to the suspect or commonly used by him. § 2518 (3).</p>
<p id="b598-6">In its November 6 application, the Government sought authority to intercept the conversations of not only Giordano, who alone was expressly named in the initial application and order, but of nine other named persons who were alleged to be involved with Giordano in narcotics violations. Based on the attached affidavit, it was alleged that there was probable cause to believe that <page-number citation-index="1" label="531">*531</page-number>communications concerning the offense involved would be intercepted, particularly those between Giordano and the other named individuals, as well as those with others as yet unnamed, and that the telephone listed in the ñame of Giordano and whose monitoring was sought to be continued “has been used, and is being used and will be used, in connection with the commission' of the offenses described.” App. 62.</p>
<p id="b599-5">In the affidavit supporting the application, the United States set out the previous applications and orders, incorporated by reference and reasserted the “facts, details and conclusions contained in [the] affidavits” supporting the prior wiretap application, and set down in detail the relevant communications overheard under the existing order, as well as the physical movements of Giordano observed as the result of an around-the-clock surveillance that had been conducted by the authorities. App. 65-•81. The Government concluded “[a]fter analyzing the intercepted conversations to and from [Giordano’s telephone] and the results of BNDD surveillance” that nine listed individuals, some identified only by aliases, were associated with Giordano as suppliers or buyers in illegal narcotics trafficking and that certain other persons were perhaps connected with the operation in an as yet undisclosed fashion. <em>Id., </em>at 79-80. It was also said that the full scope of Giordano’s organization was not yet known. <em>Id., </em>at 80. Assertedly, Giordano was extremely guarded in his telephone conversations, “any specific narcotics conversations he makes are from pay phones” and “[conventional surveillance would be completely ineffective except as an adjunct to electronic interception.” <em>Id., </em>at 81. The United States accordingly requested an extension of the interception order for no longer than a 15-day period.</p>
<p id="b599-6">It is apparent from the foregoing that the communications intercepted pursuant to the extension order were <page-number citation-index="1" label="532">*532</page-number>evidence derived from the communications invalidly intercepted pursuant to the' initial order. In the' first place, the application sought and the order granted authority to intercept the communications of various named individuals not mentioned in the initial order. It is plain from the affidavit submitted that information about most of these persons was obtained through the-initial illegal interceptions. It is equally plain that the telephone monitoring and accompanying surveillance were coordinated operations, necessarily intertwined. As the Government' asserted, the surveillance and conventional investigative techniques “would, be completely ineffective except as an adjunct to electronic interception.” That the extension order and the interceptions under it were not in fact the product of the earlier electronic surveillance is incredible.</p>
<p id="b600-4">Second, an extension order could validly be granted <em>only </em>upon an application complying with subsection (1) of §2518. Subsection (1) (e) requires that the fact of prior applications and orders be rev.ealed, and (1) (f) directs that the application set out either the results obtained under the prior order or an explanation for the absence of such results. Plainly the function of § 2518 (1) (f) is to permit the court realistically to appraise the probability that relevant conversations will be overheard in the future. If during the initial period, no communications of the kind, that had been anticipated had been overheard, the Act. requires an adequate explanation for the failure before the necessary findings can be made as a predicate to an extension order. But here there were results, and they were set out in great detail. Had they been omitted no extension order at all could have been granted; but with them, there were sufficient facts to warrant the trial court's finding, in accordance with §2518 (3) (b), of probable cause to believe that wire communications concerning the offenses involved “will <page-number citation-index="1" label="533">*533</page-number>be obtained through the interception,” App. 83, as well as.the finding complying with §2518 (3) (d) that there was probable cause to believe that Giordano’s telephone “has been used, is being used, and will be used, in connection with the commission of the offenses described above and is commonly used by Nicholas Giordano . . .” and nine other named persons. <em>Ibid.</em></p>
<p id="b601-5">It is urged in dissent that the information obtained from the illegal October 16 interception order may be ignored and that the remaining evidence submitted in the extension application was sufficient to support the extensión order. But whether or not the application, without the facts obtained from monitoring Giordano’s telephone, would independently support original wiretap authority, the Act itself forbids extensions of prior authorizations without consideration of the results meanwhile obtained. Obviously, those results were presented, considered, and relied on in this case. Moreover, as previously noted, the Government itself had stated that the wire interception was an indispensable factor in its investigation and that ordinary surveillance alone would have been insufficient: In our view, the results of the conversations overheard under the initial order were essential, both in fact and in law, to any extension of the intercept authority. Accordingly, communications intercepted under the extension order are derivative evidence and must be suppressed.<footnotemark>19</footnotemark> The judgment of the Court of Appeals is</p>
<p id="b601-7">
<em>Affirmed.</em>
</p>
<p id="b601-8">[For concurring* opinion of Mr. Justice Douglas, see <em>post, </em>p. 580.]</p>
<p id="b602-3"><page-number citation-index="1" label="534">*534</page-number>APPENDIX TO OPINION. OF THE COURT</p>
<p id="b602-4">Relevant Provisions of Title III, Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span></p>
<p id="b602-5">§ 2511. interception and disclosure of wire or oral communications prohibited.</p>
<p id="b602-6">(1) Except as otherwise specifically provided in this chapter any person who—</p>
<blockquote id="b602-7">(a) willfully intercepts, endeavors to intercept, or procures any other person to intercept or endeavor to intercept, any wire or oral communication;</blockquote>
<blockquote id="b602-8">(b) willfully uses, endeavors to use, or procures any other person to use or endeavor to use- any electronic, mechanical, or other device to intercept any oral communication when—</blockquote>
<blockquote id="b602-9">(i) such device is affixed to, or otherwise transmits a signal through, a wire, cable, or other like connection used in wire communication; or</blockquote>
<blockquote id="b602-10">(ii) such device transmits communications by radio, or interferes with the transmission of such communication; or</blockquote>
<blockquote id="b602-11">(iii) such person knows,, or has reason to know, <page-number citation-index="1" label="535">*535</page-number>that such device or any component thereof has been sent through the mail or transported in interstate or foreign commerce; or</blockquote>
<blockquote id="b603-4">(iv) such use or endeavor to use (A) takes place on the premises of any business pr other commercial establishment the operations of which affect interstate or foreign commerce; or (B) obtains or is for the purpose of obtaining information relating to the operations of any business or other commercial establishment the operations of which affect interstate or foreign commerce; or</blockquote>
<blockquote id="b603-5">(v) such person acts in the District of Columbia, the Commonwealth of'Puerto Rico, or any territory or possession of the United States;</blockquote>
<blockquote id="b603-6">(c) willfully discloses, or. endeavors to disclose, to any other person the contents of any wire or oral communication, knowing or having reason to know that the information was obtained through the interception of a wire or oral communication in violation of this subsection; or .</blockquote>
<blockquote id="b603-7">,(d) willfully uses, or endeavors to use, the contents of any wire or oral communication, knowing or having reason to know that the information was obtained through the interception of a wire or oral communication in violation of this subsection;</blockquote>
<p id="b603-8">shall be fined not more than $10,000 or imprisoned not more than five years, or both.</p>
<p id="b603-9">(2) (a) (i) It shall not be unlawful under this chapter for an operator of a switchboard, or an officer, employee, or agent of any communication common carrier, whose facilities are used in the transmission of a wire communication, to intercept, disclose, or use that communication in the normal course of his employment while engaged in any activity which is a necessary incident to the rendition <page-number citation-index="1" label="536">*536</page-number>of his service or to the protection of the rights or property of the carrier of such communication: <em>Provided, </em>That said communication common carriers shall not utilize service observing or random monitoring except for mechanical or service quality control checks.</p>
<p id="b604-4">(ii) It shall not be unlawful undér this chapter for an officer, employee, or agent of any communication common carrier to provide information, facilities, or technical assistance to an investigative or law enforcement officer who, pursuant to this chapter, is authorized to intercept a wire or oral communication.</p>
<p id="Ahd">(b) It shall not be unlawful under this chapter for an officer, employee, or agent of the Federal Communications Commission,, in the normal course of his employment and in discharge of the monitoring responsibilities exercised .by the Commission in the enforcement of chapter .5 of title 47. of the United States Code, to intercept a wire communication, or oral communication transmitted by radio, or to disclose or use the information thereby obtained.</p>
<p id="b604-6">(e) It shall not be unlawful under this, chapter for a person acting under color of law to intercept a wire or oral communication, where such person is a party to the communication of one of the parties to the communication has given prior consent to such interception.</p>
<p id="b604-7">(d) It shall not be unlawful under this chapter for a person not acting under color of law to intercept a wire or oral communication where such person is a party to the communication or where one of the partiés to the communication has given priqr consent to such interception unless such communication is intercepted for the purpose of committing any criminal or tortious act in violation of the Constitution or laws of the United States or of any State or for the purpose of committing any other injurious act.</p>
<p id="b605-3"><page-number citation-index="1" label="537">*537</page-number>(3) Nothing contained in this chapter or in section 605 of the Communications Act of 1934 (<span class="citation no-link">48 Stat. 1143</span>; 47 U. S. C. 605) shall limit the constitutional power of the President to take such measures as he deems necessary to protect the . Nation against actual or potential attack or other hostile acts of a foreign power, to obtain foreign intelligence information deemed, essential to the security of the United States, or to protect national security information against foreign intelligence activities. Nor shall anything contained in this chapter be deemed to limit the constitutional power of the President to take such measures as he deems necessary to protect the United States against the overthrow of the Government by force or other unlawful means, or against any other ciear and present danger to the structure or existence of the Government. The contents of any wire or oral communication intercepted by authority of the President in the exercise of the foregoing powers may be received in evidence in any trial hearing, or other proceeding only where such interception was reasonable, and shall not be otherwise used or disclosed except as is necessary to implement that power.</p>
<p id="b605-4">§ 2515. Prohibition of use as evidence of intercepted wire or oral communications.</p>
<p id="b605-5">Whenever any wire or oral communication has been intercepted, no part' of the contents of such communication and no evidence derived therefrom may be received in evidence in any trial, hearing, or other proceeding, in or before any court, grand jury, department, officer, agency, regulatory body, legislative committee, or other authority of the United States, a State, or a political subdivision thereof if the disclosure of that information would be in violation, of this chapter.</p>
<p id="b606-3"><page-number citation-index="1" label="538">*538</page-number>§ 2516. Authorization for interception of wire or oral communications.</p>
<p id="b606-5">.(1) The Attorney General, or any Assistant Attorney General specially designated by the Attorney General, may authorize an application to a Federal judge of competent jurisdiction for, and such judge may grant in conformity with section 2518 of this chapter an order authorizing or approving the interception of wire or oral communications by the Federal Bureau of Investigation, or a Federal agency having responsibility for the investigation of the offense as to which the application is made, when such interception may provide or has provided evidence of—</p>
<blockquote id="b606-6">(a) any offense punishable by death or by imprisonment for more than one year under sections 2274 through 2277 of title 42 of the United States Code (relating to the enforcement of the Atomic Energy Act of 1954), or under the following chapters of this title: chapter 37 (relating to espionage)-, chapter 105 (relating to sabotage), .chapter 115 (relating to treason), or chapter 102 (relating to riots);</blockquote>
<blockquote id="b606-7">(b) a violation of section 186 or section 501 (c) of title 29, United States Code (dealing with restrictions on payments and loans to labor organizations), or any offense which involves murder, kidnapping, robbery, or extortion, and which is punishable under this title;</blockquote>
<blockquote id="b606-8">(c) any offense which is punishable under the following sections of this title: section 201 (bribery, of public officials and witnesses), section 224 (bribery in sporting contests), subsection (d), (e), (f), (g), (h), or (i) of section 844 (unlawful use of explosives), section 1084 (transmission of wagering information), section 1503 (influencing or injuring an officer, juror, or witness generally), section 1510 (obstruction of criminal investigations), section 1511 (obstruction of <page-number citation-index="1" label="539">*539</page-number>State or local law enforcement), section 1751 (Presidential assassinations, kidnapping, and assault), section 1951 (interference with commerce by threats or violence), section 1952 (interstate and foreign travel or transportation in aid of racketeering enterprises), section 1954 (offer, acceptance, or solicitation to influence operations of employee benefit plan), section 1955 (prohibition of business enterprises of gambling), section 659 (theft from interstate shipment), section 664 (embezzlement from pension and welfare funds), sections 2314 and 2315 (interstate transportation' of stolen property), section 1963 (violations with respect to racketeer influenced and corrupt organizations) or section 351 (violations with respect to congressional assassination, kidnapping, and assault);</blockquote>
<blockquote id="b607-5">(d) any offense involving counterfeiting punishable under section 471, 472, or 473 of this title;</blockquote>
<blockquote id="b607-6">(e) any offense involving bankruptcy fraud or the manufacture, importation, receiving, concealment, buying, selling, or otherwise - dealing in narcotic drugs, marihuana, or other dangerous drugs, punishable under any ]#w of the United States;</blockquote>
<blockquote id="b607-7">(f) any offense including extortionate credit transactions under sections 892, 893, or 894 of this title; or</blockquote>
<blockquote id="b607-8">(g) any conspiracy to commit any of the foregoing offenses.</blockquote>
<p id="b607-9">(2) The principal prosecuting attorney of any State, or the principal prosecuting attorney of any political subdivision thereof, if such attorney is authorized by a statute of that State to make application to a State court judge of competent jurisdiction for an order authorizing or approving the interception of wire or oral communications, may apply to such judge for, and such judge may grant in conformity with section 2518 of this chap<page-number citation-index="1" label="540">*540</page-number>ter and with the, applicable State statute an order authorizing, or approving the interception of wire or oral communications by investigative or law enforcement officers having responsibility for the investigation of the offense as to which the application is made, when such interception may provide or has provided evidence of the commission of the offense of murder, kidnapping, gambling, robbery, bribery, extortion, or dealing in narcotic drugs, marihuana or other dangerous drugs, or other crime dangerous to life, limb, or property, and punishable by imprisonment for more than one year, designated in any applicable State statute authorizing such interception, or any conspiracy to commit any of the foregoing offenses.</p>
<p id="b608-5">§ 2518. Procedure for interception of wire or oral communications.</p>
<p id="b608-6">(1) Each application, for an order authorizing or approving the interception of a wire- o'r oral communication shall be made in writing upon oath or affirmation to a judge of competent jurisdiction and shall state the applicant’s authority to make such application. , Each application shall-include the following information:</p>
<blockquote id="b608-7">(a) the identity of the investigative or law enforcement officer making the application, and the officer authorizing the application;</blockquote>
<blockquote id="b608-8">(b) a full and complete statement of the facts and circumstances relied upon by the applicant, to justify his belief that an order should be issued, including (i) details as to the particular offense that has been, is being, or is about tó be committed, (ii) a particular description of the. nature and location of the facilities from which or the place where the communication is to be intercepted, (iii) a particular description -of the type of communications <page-number citation-index="1" label="541">*541</page-number>sought to be intercepted, (iv) the identity of the person, if known, committing the offense and whose communications are to be intercepted;</blockquote>
<blockquote id="b609-5">(c) a full and complete statement as to whether or not other investigative procedures have been ■tried and failed or why they reasonably appear to be unlikely to succeed if tried or to be too dangerous;</blockquote>
<blockquote id="b609-6">(d) a statement of the period of time-for which the interception is required to be maintained. If the nature of the investigation is such that the authorization for interception should not automatically terminate when the described type of communication has been first obtained, a particular description of facts establishing probable cause to believe that additional communications of the same type will occur thereafter;</blockquote>
<blockquote id="b609-7">(e) a full and complete statement of the facts concerning ¿11 previous applications known to the individual authorizing and making the application, made to any judge for authorization to intercept, or for approval of interceptions of, wire or oral communications involving any of 'the same persons, facilities or places specified in the application, and the action taken by the'judge on each such application; and</blockquote>
<blockquote id="b609-8">(f) where the application is for the extension of an order, a statement setting forth the results thus far obtained from the interception, or a reasonable explanation of the failure to obtain such results.</blockquote>
<p id="b609-10">. (2) The judge may require the applicant -to furnish additional testimony or documentary evidence in support of the application.</p>
<p id="b609-11">(3) Upon such application the judge may enter an ex parte order, as requested or as modified, authorizing or approving interception of wire or oral communications <page-number citation-index="1" label="542">*542</page-number>within the territorial jurisdiction of the'court in which tfyp judge is sitting, if the judge determines on the basis, of the facts submitted by the applicant that—</p>
<blockquote id="b610-4">(a) there is probable cause for belief that am individual is committing, has committed, or is about' to commit a particular offense eftumerated in section 2516 of this chapter;</blockquote>
<blockquote id="Aul">(b) there is probable cause for belief that particular communications ¡concerning that offense will be obtained through -such interception;</blockquote>
<blockquote id="ARdO">(c)- normal investigative procedures have been triéd and. have failed or reasonably appear to be. unlikely to succeed if tried, or to be too dangerous;-</blockquote>
<blockquote id="ArWz">(d) there is probable cause for belief that the facilities from ^which, or the1 place where, the wire or oral; communications, are to be intercepted are being used, or are about to be used; in connection with the commission of- such offense, or are leased to, listed in the name of, or commonly Used by such person.</blockquote>
<p id="b610-10">(á) Each order authorizing or approving the interception of any wire or oral communication shall specify—</p>
<blockquote id="ABE">.(a) the idéntity of the person, if known, whose communications are to be intercepted;</blockquote>
<blockquote id="Ane">-• (b) the nature and location of the communications facilities as. to which, or the place where, authority to intercept is granted;</blockquote>
<blockquote id="b610-14">(c) a particular description of the type of communication sought to be intercepted, and a statement of the particular offense to which it relates;</blockquote>
<blockquote id="b610-15">(d) the-identity pf the agency authorized to intereept the communications, and of thé person authorizing the application; and ,</blockquote>
<blockquote id="b610-16">(e) the period of time during which such interception is authorized, including a statement as to whether <page-number citation-index="1" label="543">*543</page-number>or not the interception shall automatically terminate when the described communication has been first obtained.</blockquote>
<p id="b611-6">An' order authorizing the interception of a wire or oral communication shall, upon request of the applicant, direct that a communication common carrier, landlord, custodian or other person shall furnish the applicant forthwith all information, facilities, and technical assistance .necéssary to accomplish the interception unobtrusively and with a minimum of interference with the services that such carrier, landlord, custodian, or person is according the person whose communications are to be intercepted. Any communication common carrier, landlord, custodian or other person furnishing such facilities or technical assistance shall be compensated therefor by the applicant at the prevailing rates.</p>
<p id="b611-7">(5) No order entered under this section may authorize or approve the interception of any wire or oral communication for any period longer than is necessary to achieve the objective of the authorization, nor in any event longer than thirty days. Extensions of an order may be granted, but only upon application for an extension made in accordance with subsection (1) of this section and the court making the findings required by subsection (3) of this section. The period of extension shall be- no longer than the authorizing judge deems necessary to achieve the purposes for which it was granted and in no event for longer than thirty days. Every order and extension thereof shall contain a provision that the authorization to intercept shall be executed as soon as practicable, shall be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under this chapter, and must terminate upon attainment of the authorized objective, or in any event in thirty days.</p>
<p id="b612-3"><page-number citation-index="1" label="544">*544</page-number>(6) Whenever an order authorizing interception is entered pursuant to this chapter, the order may require reports to be made to the judge who issued the order showing what progress has been made toward achievement of the. authorized objective and the need for continued interception. Such reports shall be made at such intervals as the judge may require.</p>
<p id="b612-4">(7) Notwithstanding any other provision of this chapter, any investigative or law enforcement officer, specially designated by the Attorney General or by the principal prosecuting attorney of any State or subdivision thereof acting pursuant to a statute of that State, who reasonably determines that—</p>
<blockquote id="b612-5">(á) an emergency situation exists with respect to conspiratorial activities threatening the national security interest or. to conspiratorial activities characteristic of organized crime that requires a wire or oral communication to be intercepted before an order authorizing such 'interception can with due diligence be obtained, and</blockquote>
<blockquote id="b612-6">(b) there are grounds upon which an order could be entered under this chapter to authorize such interception,</blockquote>
<p id="b612-7">may intercept such wire or oral communication if an application for an order approving the interception is made in accordance with this section within forty-eight hours after the interception has occurred, or begins to occur. In the absence of an order, such interception shall immediately terminate when the communication sought is obtained or when the application for the order is denied, whichever is earlier.. In the event such application for approval is denied, or in any other case where the interception is terminated without an order having been issued, the contents of any wire or oral communication intercepted shall be treated as having been obtained <page-number citation-index="1" label="545">*545</page-number>in violation of this chapter, and an inventory shall be served as provided for in subsection (d) of this section on the person named in the application.</p>
<p id="b613-4">(8) (a) The contents of any wire or oral communicatibn intercepted by any means authorized by this chapter shall, if possible, be recorded on tape or wire or other comparable device. The recording of the contents of any wire or oral communication under this subsection shall be done in such a way as will protect the recording from editing or. other alterations. Immediately upon the expiration of the period of the order, or extensions thereof, such recordings shall be made available to the judge issuing such order and sealed under his directions. Custody of the recordings shall be wherever the judge orders. They shall not be destroyed except upon an order of the issuing or denying judge and in any event shall be kept for ten years. Duplicate recordings may be made for use or disclosure pursuant to the provisions of subsections (1) and (2) of section 2517 of this chapter for investigations. The presence of the seal provided for by this subsection, or a satisfactory explanation for the absence thereof, shall be a prerequisite for the use or disclosure of the contents of any wire or oral communication or evidence derived therefrom under subsection (3) of section 2517.</p>
<p id="b613-5">,(b) Applications made and orders granted under this chapter shall be sealed by the judge. Custody of the applications and orders shall be wherever the judge directs. Such applications and orders shall be disclosed only upon a showing of good cause before a judge of competent jurisdiction and shall not be destroyed except on order of the issuing or denying judge, and in . any event shall be kept for ten years.</p>
<p id="b613-6">(c) Any violation of the provisions of this subsection may be punished as contempt' of the issuing or' denying judge.</p>
<p id="b614-3"><page-number citation-index="1" label="546">*546</page-number>(d) Within a reasonable time but not later than ninety days after the filing of an application for an order of approval under section 2518 (7) (b) which is denied or the termination of the period of an order or extensions thereof, the issuing or denying judge shall cause to be served, on the persons named in the order or the application, and such other parties to intercepted communications as the judge may determine in his discretion that is in the. interest of justice, an inventory which shall include notice of—</p>
<blockquote id="b614-4">(1) the fact of the entry of the order or the application;</blockquote>
<blockquote id="AHt">(2) the date of the entry and the period of author-is;ed, approved or disapproved interception-, or the denial.of the application; and</blockquote>
<blockquote id="b614-7">(3) the fact that during the period wire or oral communications were or were not intercepted.</blockquote>
<p id="b614-8">The judge, upon the filing of a motion, may in his discretion make available to such person or. his counsel for inspection such portions of the intercepted communications, applications and orders as the judge determines to be in the interest of justice. On an ex parte showing of good -cause to a judge of competent jurisdiction the serving of the inventory required by this subsection may be postponed.</p>
<p id="b614-9">(9)' The contents of any intercepted wire or oral communication or evidence derived therefrom shall not be received in evidence or otherwise disclosed in any trial, hearing, or other proceeding in a Federal or State court unless.each party, not less than ten days before the trial, hearing, or proceeding, has been furnished with a copy of the court order, and accompanying application, under which the interception was authorized or approved. This ten-day period may be waived by the judge if he finds that it was riot possible to furnish the party with <page-number citation-index="1" label="547">*547</page-number>the above information ten days before the trial, hearing, or proceeding and that the party will not be prejudiced by the delay in receiving such information.</p>
<p id="b615-5">(10) (a) Any aggrieved person, in any trial, hearing, or proceeding in or before any court, department, officer, agency, regulatory body, or other authority of the United States, a State, or a political subdivision thereof, may move to suppress the contents, of any intercepted wire or oral communication, or evidence derived therefrom, on the grounds that—</p>
<blockquote id="b615-6">(i) the communication was unlawfully intercepted;</blockquote>
<blockquote id="b615-7">(ii) the order of authorization or approval under which- it was intercepted is insufficient on' its face; or</blockquote>
<blockquote id="b615-8">(iii) the interception was not made in conformity with the order of authorization or- approval.</blockquote>
<p id="b615-9">Such motion shall be made before the trial, hearing, or proceeding unless there was no opportunity to make such motion or the person was not aware of the grounds, of the motion. If the motion is granted, the contents of the intercepted wire or oral communication, or evidence derived therefrom, shall be treated as having been obtained in violation of this chapter. The judge, upon the filing of such motion by the aggrieved person, may in his discretion make available to the aggrieved person or his counsel for inspection such portions of the intercepted communication or evidence derived therefrom ¿s the judge determines to be in the interests of justice;</p>
<p id="b615-10">(b) In addition to any other right to appeal, the United States shall have the right, to appeal from an order granting a motion to suppress made under paragraph. (a) of this subsection, or the denial .of an application for an order of approval, if the United States attorney shall certify to the judge or other official granting such motion or denying such application that the appeal <page-number citation-index="1" label="548">*548</page-number>is not taken for purposes of delay. Such appeal shall be taken within thirty days after the date the order was entered and shall be diligently prosecuted.</p>
<p id="b616-4">§ 2520. Recovery of civil damages authorized.</p>
<p id="b616-5">Any person whose wire or oral communication is intercepté!, disclosed, pr used in violation of this chapter shall (1) have a civil cause of action against any,person who intercepts, discloses, ór uses, or procures any other person to intercept, disclose, or use such communications, and (2) be entitled to recover from any such person—</p>
<blockquote id="b616-6">(a) actual damages but not less than 'liquidated damages computed at the rate of $100 a day for each day of. violation or $1,000, whichever is higher;</blockquote>
<blockquote id="b616-7">(b) punitive damages; and</blockquote>
<blockquote id="b616-8">(c) a reasonable attorney’s fee and other litigation costs reasonably incurred.</blockquote>
<p id="b616-9">A good faith reliance on a-court order, or legislative authorization, shall constitute a complete defense to any civil or criminal action brought under this chapter or under any" other law.</p>
<footnote label="1">
<p id="b576-7"> This and other relevant provisions of the statute are contained in the Appendix to this opinion, <em>post, </em>p. 534.</p>
</footnote>
<footnote label="2">
<p id="b579-5"> Evidence derived from the unlawful interceptions conducted pursuant to the October 16 wiretap order was held to include the evidence obtained under the November 6 wiretap extension order and also the evidence secured under court orders of October 22 and November 6 extending investigative authority to use a “pen register,” <em>i. e., </em>a device that records telephone numbers dialed from a particular phone, which had previously been used to monitor the numbers dialed from Giordano’s phone pursuant to a court order of October 8. The applications presented to the District Court to extend wiretap and pen register authority each detailed at considerable length the contents of conversations intercepted, pursuant to the October 16 order in support of the requests. We therefore agree with the Court of Appeals, for the reasons discussed in Part IV, <em>infra, </em>that evidence gathered under the wiretap and pen. register extension orders is tainted by the use of unlawfully intercepted communications under the. October 16 order to secure judicial approval for. the extensions, and must be suppressed.</p>
</footnote>
<footnote label="3">
<p id="b579-6"> The Second Circuit has held that approval of wiretap applications by the Attorney General’s Executive Assistant complies with the dictates of §2516 (1). In <em>United States </em>v. <em>Pisacano, </em><span class="citation" data-id="303139"><a href="/opinion/303139/united-states-v-vincent-peter-pisacano/" aria-description="Citation for case: United States v. Vincent Peter Pisacano">459 F. 2d 259</a></span> (1972), the court refused to permit withdrawal of guilty pleas on the basis of subsequent discovery that the Executive Assistant had authorized the first of three wiretap applications, declaring that it was “not at all convinced that if this case had gone <page-number citation-index="1" label="512">*512</page-number>to trial and the court had refused to suppress evidence obtained by the wiretaps, we would have reversed,” and that “the- Justice Department’s procedures were very likely consistent with the mandate of §2516(1).” <em>Id., </em>at 264 and n. 5. Shortly thereafter a different panel of that Circuit affirmed judgments of convictions in a case raising the same issue, out of “adherence to the 1'aw of the circuit” so recently decided and with the admonition that its decision should “not... be construed as an approval of the procedure followed by the Attorney General and his staff.”" <em>United States </em>v. <em>Becker, </em><span class="citation" data-id="303774"><a href="/opinion/303774/united-states-v-richard-becker-and-jack-eisen/#236" aria-description="Citation for case: United States v. Richard Becker and Jack Eisen">461 F. 2d 230, 236</a></span> (1972). In every other circuit which has considered the issue, suppression of evidence derived from court-approved wire .interceptions based on an application authorized by the Attorney Generalas TExecutive Assistant has been held to be required by Title III. <em>United States </em>v. <em>Mantello, </em>156 U. S. App. D. C. 2, <span class="citation" data-id="310952"><a href="/opinion/310952/united-states-v-louis-mantello-united-states-of-america-v-john/" aria-description="Citation for case: United States v. Louis Mantello United States of America...">478 F. 2d 671</a></span> (1973); <em>United States </em>v. <em>Roberts, </em><span class="citation" data-id="8889965"><a href="/opinion/8902969/united-states-v-roberts/" aria-description="Citation for case: United States v. Roberts">477 F. 2d 57</a></span> (CA7 1973); <em>United States v. King, </em><span class="citation" data-id="9459489"><a href="/opinion/310930/united-states-v-richard-michael-king-aka-richard-hansen/" aria-description="Citation for case: United States v. Richard Michael King, AKA Richard Hansen">478 F. 2d 494</a></span> (CA9 1973). See also <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="306054"><a href="/opinion/306054/united-states-v-j-w-robinson/" aria-description="Citation for case: United States v. J. W. Robinson">468 F. 2d 189</a></span> (CA5 1972), remanded for an evidentiary hearing to determiné whether the applications were properly authorized under § 2516 (1), <span class="citation" data-id="9459111"><a href="/opinion/307978/united-states-v-j-w-robinson/" aria-description="Citation for case: United States v. J. W. Robinson">472 F. 2d 973</a></span> (en banc 1973).</p>
</footnote>
<footnote label="4">
<p id="b580-9"><em> </em>Because of our -disposition of this^case, we do not reach the grounds relied upon by the District Gqürt. ‘ The issue resolved in the District Court, however, is the subject of the companion case, <em>United States </em>v. <em>Chavez, post, </em>p. 562.</p>
</footnote>
<footnote label="5">
<p id="b581-7"> In full, <span class="citation no-link">28 U. S. C. § 509</span> provides:</p>
<blockquote id="b581-8">“§ 5Ó9. Functions of- the Attorney General.</blockquote>
<blockquote id="b581-9">■ “All functions of other officers of the Department of Justice and all. functions of agencies and employees of the Department of Justice are-vested in the Attorney General except the functions—</blockquote>
<blockquote id="b581-10">“(1) vested by subchapt-er II of chapter 5 of title 5 in hearing examiners employed by the Department of Justice;</blockquote>
<blockquote id="b581-11">“(2) of the Federal Prison Industries, Inc.;</blockquote>
<blockquote id="b581-12">“(3) of the Board of Directors and officers of the Federal Prison Industries,.Inc.; and</blockquote>
<blockquote id="Ap_">“(4) of the Board of Parole.”</blockquote>
</footnote>
<footnote label="6">
<p id="b582-5"> Criminal sanctions were, provided in <span class="citation no-link">18 U. S. C. § 2511</span>, and a civil damages remedy was created by § 2520. See Appendix to this opinion, <em>post, </em>p. 534.</p>
</footnote>
<footnote label="7">
<p id="b585-7"> In 1967, a draft statute prepared by Professor G. Robert Blakey of the University of Notre Dame Law School to regulate the interception of wire and oral communications was published in The President’s Commission on Law Enforcement and Administration of Justice, Task Force Report: Organized Crime, Appendix C, at 106-113. In part, it would have added a provision to Title 18, United States Code,.which empowered the “Attorney General, or any Assistant Attorney General of the Department of Justice specially designated by the Attorney General” to authorize an application to a federal judge for an order to' intercept wire or oral communications. <em>Id., </em>at 108. Senator McClellan introduced a proposed “Federal Wire Interception Act,” S. 675, on January 25, 1967, 113 Cong. Rec. 1491, containing, in § 5 (a), the same designations of which federal prosecutiig officials could authorize a wiretap application. Hearings on Controlling Crime Through More Effective Law Enforcement before the Subcommittee on Criminal Laws and Procedures of the Senate Com<page-number citation-index="1" label="518">*518</page-number>mittee on the Judiciary, 90th Cong., 1st Sess., 76 (1967). Senator Hruska later introduced S. 2050 on June 29, 1967, 113 Cong. Rec. 18007, which would have provided for regulated use of' electronic surveillance, as well as wiretapping, and which again made provision, in a new § 2516 to be added to Title 18, United States Code, for the same system of approval of applications for the interception of wire or oral communications as was present in the Blakey bill. Hearings, <em>supra, </em>at 1005. In the House of Representatives, the Blakey bill was introduced on October 3, 1967, in the form of H. R. 13275, 113 Cong. Rec. 27718. Ultimately, the same operative language was enacted in Title III.</p>
</footnote>
<footnote label="8">
<p id="b587-5"> In the hearings on the McClellan bill, S. 675, see n. 7, <em>supra, </em>the limitation on the application authorization power was frequently brought to the fore. Thus, Chief Judge Lumbard of the United States Court of Appeals for the Second Circuit, who had earlier been United States Attorney for the Southern District of New York¿; noted in testimony on March 8, 1967, that the “application would" require approval of the Attorney General or a designated assistant . . . ,” and he urged, in support of his recommendation that it was-unnecessary to limit the use of wiretapping to the investigation of a narrow group of serious crimes, the fact that there were other factors which would greatly limit the use of wiretapping, beginning with the observation that “the proposed statute, section 5a, provides that only the Attorney General, or any Assistant Attorney General specifically designated by him, may authorize the necessary application to a Federal judge for ápproval tojwiretap. Thus the. application will be carefully screened.” Hearings on Controlling Crime Through More Effective Law Enforcement, <em>supra, </em>n. 7, at 171— 172. A letter urging adoption of legislation to govern the area of wiretapping and electronic eavesdropping was sent to the subcommittee on March 7 by all living former United States Attorneys of the Southern District of New York, who recommended that interception be prohibited “unless authorized by a'Federal judge on application of the Attorney General, or any Assistant Attorney General of the Department of Justice specially designated by the Attorney General, when such authorized interception or recording may provide evidence of an offense against the laws of the United States.” <em>Id., </em>at 511-512. And Senator McClellan- himself commented to a judge testifying before the subcommittee:</p>
<blockquote id="b587-6">“This legislation, as you know, requires rather thorough court supervision through the application for a court order made by the Attorney General or officials designated in the bill. A court, of course, would have to weigh the probable cause or the reasonable cause in support of such an application. I do not know how to tighten it up any more than we have in the bill. . . . Can you tell us how to tighten it up any inore?” <em>Id., </em>at 894-895.</blockquote>
</footnote>
<footnote label="9">
<p id="b588-8"> The Attorney General is appointed by the President, by and with the advice and consent of the Senate, <span class="citation no-link">28 U. S. C. § 503</span>, as <page-number citation-index="1" label="521">*521</page-number>are the nine Assistant Attorneys General provided for in <span class="citation no-link">28 U. S. C. § 506</span>. The position of Executive Assistant, on the other hand, is established by regulation, to assist the Attorney General, <em>inter alia, </em>in the review of “matters submitted for the Attorney General’s ae+ion” and to “[p]erform such other duties and functions as may be specially assigned from time to time by the Attorney General.” <span class="citation no-link">28 CFR § 0.6</span>. It would appear from the Government’s brief that the Executive Assistant involved in this case served as Executive Assistant to at least four Attorneys General.</p>
</footnote>
<footnote label="10">
<p id="b589-5"> In debate on the Senate floor the day before Title III was adopted, Senator McClellan responded to an inquiry of Senator Lausche in the following matter:</p>
<blockquote id="b589-6">“Mr. LAUSCHE. Does the bill as now written give absolute, unconditional power to stop searches or tapping, or to'authorize tapping?</blockquote>
<blockquote id="b589-7">“Mr. McCLELLAN. No. We have to go first to the Attorney General in. the case of the Federal Government, and to the chief law enforcement officers of a State ....</blockquote>
<blockquote id="b589-8">“Mr. LAUSCHE. There is, then, a. prohibition against tapping unless the application is filed with the chief law enforcement official He approves it and then the application is filed with the court, is that not correct?</blockquote>
<blockquote id="b589-9">“Mr. McCLELLAN. The chief law enforcement officer, like the Attorney General of the United States, must authorize the application .... A prosecuting attorney or a U. S. district attorney cannot, on his. own motion, do it. He has to get the authority from the <page-number citation-index="1" label="522">*522</page-number>Attorney General of'the United States first to submit the application to the court.” 114 Cong. Rec. 14469.</blockquote>
<p id="b590-7">During the same debate, Senator Long read from a report of the Association of the Bar of the City of. New York, Committee on Federal Legislation, Committee on Civil Rights, “Proposed Legislation on Wiretapping and Eavesdropping after <em>Berger </em>v. <em>New York </em>and <em>Katz </em>v. <em>United States,” </em>which commented on the application provisions of Title III in the following manner:</p>
<blockquote id="b590-8">“Who May Apply</blockquote>
<blockquote id="ADnW">“The Blakey .Bill provides that applications for wiretapping or eavesdropping orders may be made by only a limited number of persons. At the Federal level these are the Attorney General of the United States or an Assistant. Attorney General and at the State level they are the State Attorney General or the principal prosecuting attorney of a political subdivision (such as a county or city District Attorney);</blockquote>
<blockquote id="AX4">“We agree that responsibility should be focused on those public officials who will be principally accountable to the courts and the public for their actions. Police and investigative agencies should not have the power to make such applications on their own. On the other hand, it seems anomalous to permit only very high Federal officials to apply, excluding such officials as United States Attorneys for entire States or Districts like the Southern District of New York, .while permitting county district attorneys with substantially less responsibility to make applications....</blockquote>
<blockquote id="b590-11">“We also would seek to reduce the anomaly referred to above-by providing that the Attorney General may delegate to United States Attorneys the power to initiate applications.” 114 Cong. Rec. 14473-14474.</blockquote>
</footnote>
<footnote label="11">
<p id="AZj"> The following comments concerning § 2516 (2) are found in S. Rep. No. 1097, 90th Cong., 2d Sess., 98 (1968):</p>
<blockquote id="b590-13">“Paragraph (2) -provides that the principal prosecuting attorney of any State or the principal prosecuting-attorney of any political <page-number citation-index="1" label="523">*523</page-number>subdivision of a State may authorize an application tó a State judge of competent jurisdiction ... for an order authorizing the interception of wire or oral communications. The issue of delegation by that officer would be a question of State law. In most States, the principal prosecuting attorney of the State would be the attorney general. The important question, however, is not name but function. The intent of the proposed provision is to provide for the centralization of policy relating to statewide law enforcement in the area of the use of electronic surveillance in the chief prosecuting officer of the State. . . . Where no such office exists, policymaking would not be possible on a statewide basis; it would have to move down to the next level of government. In most States, the principal prosecuting attorney at the next political level of a State,- usually the county, would be the district attorney, State’s attorney, or county solicitor. The'intent ... is to centralize areawide law enforcement policy in him. . . . Where there are both an attorney general and a district attorney, either could authorize applications, the attorney general anywhere in the State and the district attorney anywhere in his county. The proposed provision does not envision a further breakdown. Although city attorneys may have in some places limited criminal prosecuting jurisdiction, the proposed provision is not intended to include them.”</blockquote>
</footnote>
<footnote label="12">
<p id="b591-6"> We also deem it clear that the authority must be exercised <em>before </em>the application is presented to a federal judge. The suggestion that it is acceptable, practice .under §2516(1) for the Attorney General’s Executive Assistant to approve wiretap applications in the Attorney General’s absence if the Attorney General <page-number citation-index="1" label="524">*524</page-number>subsequently, after a court order has issued, ratifies the giving of approval in the particular instance, either direbtly or by personally approving the submission of a further .application for an extension order, as in this case, is wide of the mark. ’ As the Court of Appeals for the Fifth Circuit noted in the panel decision in <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="306054"><a href="/opinion/306054/united-states-v-j-w-robinson/#193" aria-description="Citation for case: United States v. J. W. Robinson">468 F. 2d, at 193</a></span>, the Attorney General’s “authority from Congress was to initiate wiretap applications, not to seek to have those terminated he found should never have been-requested in the first place.” It would ill serve the congressional policy of having the Attorney General or one of his Assistants screen the applications prior to their submission to court to have the screening process occur after the application is made- and after investigative officials have already begun to intercept wire or oral communications under a court order predicated on the assumption that proper authorization to apply for intercept authority had been given.</p>
</footnote>
<footnote label="13">
<p id="b593-6"> No question is raised in this case concerning the manner of conducting the court-approved interceptions of Giordano’s telephone and. thus § 2518 (10) (a) (iii) is inapplicable to the present situation.</p>
</footnote>
<footnote label="14">
<p id="b593-7"> The Court of Appeals also held that suppression w.'is required under.subdivision (ii) on the theory that the absence of any valid authorization of the wiretap application was the equivalent of failing to identify at all in the interception order the person who authorized the application, rendering the order “insufficient on its face.” Manifestly, however, the order, on its face, clearly, though erroneously, identified Assistant Attorney General Wilson as :he Justice Department officer authorizing the application, pursuant to special designation by the Attorney General. As it stood, th3 intercept order was facially sufficient under §2516 (1), and despite what was subsequently discovered, the Court of Appeals was in erro;- in justifying suppression under § 2518 (10) (at (ii).</p>
</footnote>
<footnote label="15">
<p id="b593-9"> The Government suggested at oral argument that, tn addition to constitutional violations, willful statutory violations might also fit. within the terms of §2518 (10) (a) (i), Tr. of Oral Arg. 33.</p>
</footnote>
<footnote label="16">
<p id="b594-5"> The draft statute prepared by Professor Blakey provided this fourth ground warranting suppression in cases where there was no probable cause for believing the existence of the grounds on which the interception order was issued. Task Force Report: Organized Crime, <em>supra, </em>n. 7, at 111, § 3803 (k) (1) (C). So did the McClellan bill, S. 675, which was introduced prior to <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). Hearings on Controlling Crime Through More Effective Law Enforcement, <em>supra, </em>n. 7, at 78, § 8 (g) (3). But the <page-number citation-index="1" label="527">*527</page-number>bill proposed by Senator Hruska after <em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">Berger</a></span> </em>(S. 2050) omitted th s •ground in a provision the language of which is substantially identical to § 2518 (10) (a) as finally enacted. <em>Id., </em>at 1008, § 2518 (k) (1). An explanation for the omission is provided in an appendix comparir g S. 675 with S. 2050, which was published by Senator Scott, a cosponsor of the latter bill, in an article in the Howard Law Journal, Wiretapping and Organized Crime, .14 How. L. J. 1 (1968), and which was reprinted in Senator Scott’s remarks on the Senate floor concerning the Omnibus Crime Control and Safe Streets Act of 1968. 114 Cong. Rec. 13205-13211. It is there simply stated that “Senator Hruska’s man says that the probable cause test is implied in (1).” <em>Id., </em>at 13211.</p>
</footnote>
<footnote label="17">
<p id="b596-5"> In relevant part S. Rep. No. 1097, <em>supra, </em>n. 11, at 96, 106, provides:</p>
<blockquote id="A7y">. “Section 2515 of the new chapter imposes an evidentiary sanction to compel compfiance with the other prohibitions of the chapter. . . . The provision must, of course, be read in light of section 2518 (10) (a) discussed below, which defines the class entitled to make a motion to suppress. It largely reflects existing law. It applies to suppress evidence directly <em>(Nardone </em>v. <em>United States, </em><span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span> (1937)) or indirectly obtained in violation of the chapter. <em>(Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939).) There is, however, no intention to change the attenuation rule. . . . Nor generally to press the scope of the suppression role beyond present search and seizure law. . . . But it does apply across the board in both Federal and State proceeding[s]. . . . And it is not limited to criminal proceedings. Such a suppression rule is necessary and proper to protect privacy. . . . The provision thus forms an -integral part of the system of limitar <page-number citation-index="1" label="529">*529</page-number>tions designed to protect privacy. Along with the criminal and civil remedies, it should serve to guarantee that the standards of the new chapter will sharply curtail the unlawful interception of wire and oral communications.</blockquote>
<blockquote id="b597-7">“[Section 2518 (10) (a)] must be read in connection with sections 2515 and 2517, discussed above, which it limits. It provides the remedy for the right created by section ■ 2515. - [Except for its inapplicability to grand jury proceedings and an absénce of intent to grant jurisdiction to federal courts over Congress,] [otherwise, the scope of the provision is intended to be comprehensive.”</blockquote>
</footnote>
<footnote label="18">
<p id="b597-8"> We find without substance the Government’s suggestion that since <span class="citation no-link">18 U. S. C. §2511</span> (1) (c) makes criminal the “willful” disclosure of the contents of an intercepted, communication, “knowing or having reason to know that the information was obtained through the interception of a wire or oral communication in Violation of this subsection,” and § 2515 ties the propriety of suppression of evidence to the impropriety of its “disclosure,” to hold that statutory violations committed in the Justice Department’s internal approval and submission procedures with respect to wiretap applications preclude disclosure in court would be to attribute to Congress an intent to impose substantial criminal penalties for “every defect in processing applications.” Brief for'United States 38. Apart from the fact that a majority of the Court in <em>United States </em>v. <em>Chavez, post, </em>p. 562, has concluded that not every defect-will warrant suppression, it is evident that §2511 does not impose criminal liability unless disclosure is “willful” and unless the information was known to have been obtained in violation of §2511 (l): Clearly, the circumstances under which suppression of evidence would be required are not necessarily the same as those under which a criminal violation of Title III would .be found.</p>
</footnote>
<footnote label="19">
<p id="b601-9"> We are also of the view that the evidence obtained from the extended authorizations of October 22 and November 6 for the installation and use of the pen register device on Giordano’s <page-number citation-index="1" label="534">*534</page-number>telephone was inadmissible because derived from the invalid wire interception that began on October 16. See n. 2, <em>supra. </em>The application for the October 22 extension attached the logs of telephone conversations monitored under the October 16 order and asserted that these logs revealed the “continued use of the telephone . . . for conversations regarding illegal trafficking in narcotics.” .App. 55. In these, circumstances, it appears to us that the illegally monitored conversations should be considered a critical element in extending the pen register authority. We have been furnished with nothing to indicate that the pen register extension of November 6 should be accorded any different treatment.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Gooch.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Gooch"
type: case
citation: "6 F.3d 673 (1993)"
parallel_cite: 93 Daily Journal DAR 12716
neutral_cite: "93 Cal. Daily Op. Serv. 7462; 1993 U.S. App. LEXIS 25518; 1993 WL 390206"
court: "U.S. Court of Appeals, Ninth Circuit"
court_level: coa
circuit: 9th
year: 1993
date_decided: 1993-10-06
docket: 92-30358
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1993-09-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gooch
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/"
  cluster_id: 654273
  opinion_id: 654273
  identity_checked: true
homes:
  - page: "[[Tents]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[California v. Carney]]", "[[United States v. Basher]]"]
aliases: ["United States v. Gooch (9th Cir. 1993)", "United States v. Kenneth D. Gooch"]
tags: ["case", "fourth-amendment", "tent", "reasonable-expectation-of-privacy", "campground", "ninth-circuit"]
holding: "(Persuasive (outside circuit) — 9th Cir.) An occupant has a reasonable expectation of privacy in a tent in a public campground; 'a tent is more like a house than a car,' so its warrantless search violated the 4A."
lake:
  record_id: United States v. Gooch
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gooch

*6 F.3d 673 (9th Cir. 1993)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Responding to a 3:50 a.m. report that a man had fired a shot at a state campground, Stevens County officers located Kenneth Gooch — who had been living in a closed tent there for several days with no other residence — asleep in his tent. Without an arrest warrant, they ordered him out, arrested and handcuffed him, locked him in a patrol car 20 yards away, removed the other occupant, and then, still without a warrant, searched the tent and found a loaded handgun under his air mattress. A post-trial [[Common Legal Terms#suppression-hearing|suppression hearing]] held the firearm should have been suppressed; the government appealed.

## Issue
Whether a person has a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent pitched on a public campground, such that a warrantless search of the tent violates the Fourth Amendment.

## Rule
Yes. A tent is treated as a dwelling for Fourth Amendment purposes, not as a vehicle. Occupancy of a tent requires "both a subjective and an objectively reasonable expectation of privacy in the tent." — 6 F.3d at 677 (citing [[Katz v. United States]]). ^pin-677

That expectation survives pitching the tent on public ground: "This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp." — [*Id.*](https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/#:~:text=This%20reasonable%20expectation%20is%20not) ^pin-677a

The court rejected any vehicle analogy and held: "The district court did not err in concluding a tent is more like a house than a car. We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/#:~:text=The%20district%20court%20did%20not%20err%20in%20concluding%20a) ^pin-677b

## Application
On these facts the warrantless tent search was unlawful. Gooch had lived in the closed tent for days with no other residence, establishing a subjective expectation of privacy that the district court's finding (not [[Common Legal Terms#clear-error|clearly erroneous]]) supported; the government's argument that a lawbreaker expecting police response can have no such expectation would, the court noted, deny privacy to anyone because "the expectation of arrest is always imminent." The expectation was also objectively reasonable: although a tent is movable, "[t]he fact that a tent may be moved, alone, is not enough to remove the Fourth Amendment protections," and a tent is more analogous to a movable closed container — or a house — than to a car to which the automobile exception of [[California v. Carney]] would apply. With Gooch secured in the patrol car and no [[Exigent Circumstances and Hot Pursuit|exigency]], the warrantless search of the tent violated the Fourth Amendment.

## Conclusion
Gooch had a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his tent; the warrantless search violated the Fourth Amendment, and the suppression of the firearm was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- No negative subsequent treatment identified. *Gooch* remains the Ninth Circuit's leading statement that a tent occupied as a dwelling carries a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] ("more like a house than a car"), distinguishing the vehicle rule of [[California v. Carney]].

## Appears on
- [[Tents]] — *Key — Anchor*

## Sources
- *United States v. Gooch*, 6 F.3d 673 (9th Cir. 1993) — https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/ — pinpoint: 677. (CL's copy carries no internal star-pagination; the 677 pinpoint is the standard reporter pinpoint for the reasonable-expectation holding — quotes verbatim-verified against the opinion text.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "80ef776be50ccd6c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "6 F.3d 673 (1993)", "court": "U.S. Court of Appeals, Ninth Circuit", "neutral_cite": "93 Cal. Daily Op. Serv. 7462; 1993 U.S. App. LEXIS 25518; 1993 WL 390206", "official_citation_present": true, "parallel_cite": "93 Daily Journal DAR 12716", "title": "United States v. Gooch", "year": "1993"}}
{"assertion_id": "41ad971b7de6a759", "dimension": "support", "kind": "home_role", "locator": {"home": "Tents"}, "payload": {"home": "Tents", "role": "Key — Anchor", "title": "United States v. Gooch"}}
{"assertion_id": "b40d7da6e213f5ab", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "(Persuasive (outside circuit) — 9th Cir.) An occupant has a reasonable expectation of privacy in a tent in a public campground; 'a tent is more like a house than a car,' so its warrantless search violated the 4A.", "title": "United States v. Gooch"}}
{"assertion_id": "43ce53ffea423b74", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Gooch"}}
{"assertion_id": "c6390624462ca548", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1993-09-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Gooch", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Gooch", "varies_by_point": "false"}}
```

### lake record — United States v. Gooch

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gooch",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Kenneth D. Gooch",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Kenneth D. GOOCH, Defendant-Appellee",
    "input_case_name": "United States v. Gooch",
    "court": "U.S. Court of Appeals, Ninth Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "1993-10-06",
    "year": 1993,
    "docket": "92-30358",
    "cluster_id": 654273,
    "lead_opinion_id": 654273,
    "sibling_ids": [
      654273,
      9485948,
      9485949
    ],
    "absolute_url": "/opinion/654273/united-states-v-kenneth-d-gooch/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "6 F.3d 673",
      "volume": "6",
      "reporter": "F.3d",
      "page": "673",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 Daily Journal DAR 12716",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "12716",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "93 Cal. Daily Op. Serv. 7462",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "7462",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. App. LEXIS 25518",
        "volume": "1993",
        "reporter": "U.S. App. LEXIS",
        "page": "25518",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 390206",
        "volume": "1993",
        "reporter": "WL",
        "page": "390206",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "6 F.3d 673",
        "volume": "6",
        "reporter": "F.3d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 12716",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "12716",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 7462",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "7462",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. App. LEXIS 25518",
        "volume": "1993",
        "reporter": "U.S. App. LEXIS",
        "page": "25518",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 390206",
        "volume": "1993",
        "reporter": "WL",
        "page": "390206",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "6 F.3d 673",
    "official_selection": {
      "court_class": "coa",
      "selected": "6 F.3d 673",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-677",
      "page": null,
      "quote": "--- # United States v. Gooch *6 F.3d 673 (9th Cir. 1993)* \u00b7 U.S. Court of Appeals, Ninth Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Responding to a 3:50 a.m. report that a man had fired a shot at a state campground, Stevens County officers located Kenneth Gooch \u2014 who had been living in a closed tent there for several days with no other residence \u2014 asleep in his tent. Without an arrest warrant, they ordered him out, arrested and handcuffed him, locked him in a patrol car 20 yards away, removed the other occupant, and then, still without a warrant, searched the tent and found a loaded handgun under his air mattress. A post-trial suppression hearing held the firearm should have been suppressed; the government appealed. ## Issue Whether a person has a Fourth Amendment reasonable expectation of privacy in a closed tent pitched on a public campground, such that a warrantless search of the tent violates the Fourth Amendment. ## Rule Yes. A tent is treated as a dwelling for Fourth Amendment purposes, not as a vehicle. Occupancy of a tent requires",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-677a",
      "page": null,
      "quote": "This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 7730,
      "fragment": "#:~:text=This%20reasonable%20expectation%20is%20not",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-677b",
      "page": null,
      "quote": "The district court did not err in concluding a tent is more like a house than a car. We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 16441,
      "fragment": "#:~:text=The%20district%20court%20did%20not%20err%20in%20concluding%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1993-09-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gooch",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rodrigo Sandoval",
          "cluster_id": 767260,
          "cite": [
            "200 F.3d 659",
            "2000 Cal. Daily Op. Serv. 581",
            "2000 Daily Journal DAR 907",
            "2000 U.S. App. LEXIS 805",
            "2000 WL 48991"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Yong Hyon Kim",
          "cluster_id": 672873,
          "cite": [
            "27 F.3d 947",
            "1994 U.S. App. LEXIS 16298",
            "1994 WL 287235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basher",
          "cluster_id": 183144,
          "cite": [
            "629 F.3d 1161",
            "2011 U.S. App. LEXIS 1064",
            "2011 WL 167045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tibolt",
          "cluster_id": 196502,
          "cite": [
            "72 F.3d 965",
            "1995 U.S. App. LEXIS 37154",
            "1995 WL 757848"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. Loomis Armored Inc.",
          "cluster_id": 1179712,
          "cite": [
            "913 P.2d 377"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher McIver United States of America v. Brian Eberle",
          "cluster_id": 765594,
          "cite": [
            "186 F.3d 1119",
            "99 Cal. Daily Op. Serv. 6304",
            "99 Daily Journal DAR 8052",
            "1999 U.S. App. LEXIS 18290",
            "1999 WL 587573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robin Lynn Bailey v. Anthony Newland, Warden",
          "cluster_id": 774778,
          "cite": [
            "263 F.3d 1022",
            "2001 Cal. Daily Op. Serv. 7675",
            "2001 Daily Journal DAR 9513",
            "2001 U.S. App. LEXIS 19398",
            "2001 WL 994913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence Ezekiel Reid, United States of America v. Wayne Blake",
          "cluster_id": 770456,
          "cite": [
            "226 F.3d 1020",
            "2000 Cal. Daily Op. Serv. 7702",
            "2000 Daily Journal DAR 10217",
            "2000 U.S. App. LEXIS 23203",
            "2000 WL 1290375"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ray Lewis Bowman, A.K.A. Charles Clark",
          "cluster_id": 769118,
          "cite": [
            "215 F.3d 951",
            "55 Fed. R. Serv. 105",
            "2000 Cal. Daily Op. Serv. 4635",
            "2000 U.S. App. LEXIS 13013",
            "2000 WL 744083"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harold McRae",
          "cluster_id": 758065,
          "cite": [
            "156 F.3d 708",
            "1998 U.S. App. LEXIS 24526",
            "1998 WL 673216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salemme",
          "cluster_id": 2510809,
          "cite": [
            "91 F. Supp. 2d 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. City of San Jose",
          "cluster_id": 1355654,
          "cite": [
            "558 F.3d 1069",
            "2009 U.S. App. LEXIS 5567",
            "2009 WL 606132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Collazo-Aponte",
          "cluster_id": 8619338,
          "cite": [
            "216 F.3d 163",
            "54 Fed. R. Serv. 3d 1311",
            "2000 U.S. App. LEXIS 14658"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jose Ortiz-Sandoval v. Linda Clarke, Warden",
          "cluster_id": 781363,
          "cite": [
            "323 F.3d 1165",
            "2003 Cal. Daily Op. Serv. 2602",
            "2003 U.S. App. LEXIS 5697",
            "2003 WL 1480565"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brett W. Dumstrey",
          "cluster_id": 3169926,
          "cite": [
            "366 Wis. 2d 64",
            "2016 WI 3",
            "873 N.W.2d 502",
            "2016 Wisc. LEXIS 2"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Piedad Barajas-Avaslos",
          "cluster_id": 787179,
          "cite": [
            "377 F.3d 1040",
            "2004 U.S. App. LEXIS 15362",
            "2004 WL 1656517"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiting v. State",
          "cluster_id": 1479286,
          "cite": [
            "885 A.2d 785",
            "389 Md. 334",
            "2005 Md. LEXIS 643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Casel Nora",
          "cluster_id": 2722177,
          "cite": [
            "765 F.3d 1049",
            "2014 U.S. App. LEXIS 16677",
            "2014 WL 4235955"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughston",
          "cluster_id": 2285590,
          "cite": [
            "168 Cal. App. 4th 1062",
            "85 Cal. Rptr. 3d 890",
            "2008 Cal. App. LEXIS 2361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rivera-Melendez",
          "cluster_id": 198984,
          "cite": [
            "216 F.3d 163"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nishi",
          "cluster_id": 5811207,
          "cite": [
            "207 Cal. App. 4th 954",
            "143 Cal. Rptr. 3d 882",
            "2012 WL 2870591",
            "2012 Cal. App. LEXIS 806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wakeford",
          "cluster_id": 884811,
          "cite": [
            "1998 MT 16",
            "953 P.2d 1065",
            "287 Mont. 220",
            "55 State Rptr. 56",
            "1998 Mont. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Arellano-Ochoa, United States of America v. Jose Luis Arellano-Ochoa",
          "cluster_id": 795590,
          "cite": [
            "461 F.3d 1142",
            "2006 U.S. App. LEXIS 22466",
            "2006 WL 2506395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alward v. State",
          "cluster_id": 1119018,
          "cite": [
            "912 P.2d 243",
            "112 Nev. 141",
            "66 A.L.R. 5th 763",
            "1996 Nev. LEXIS 24"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(654273 OR 9485948 OR 9485949) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 2,
        "triage_snippet_classified": 11
      },
      "lane2_top_cited": {
        "query": "cites:(654273 OR 9485948 OR 9485949)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yJnM9MjQwMDYzOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28654273+OR+9485948+OR+9485949%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(654273 OR 9485948 OR 9485949)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(654273 OR 9485948 OR 9485949)",
    "indexed_citing_opinions": 61,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 654273,
        "count": 54,
        "count_source": "search"
      },
      {
        "opinion_id": 9485948,
        "count": 7,
        "count_source": "search"
      },
      {
        "opinion_id": 9485949,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 119,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gooch.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjE1NzYwOTYmcz0yMzE5MzE2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28654273+OR+9485948+OR+9485949%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 654273,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 603575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 1245135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 1500109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 546167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 566881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 251769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 431931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 441786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 452994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 460378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 465254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 475484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 480405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 506240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 522259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 566881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 567665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 603575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1245135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1420587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1500109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 7841712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 8693761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 8947287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9049052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9108589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9426247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9427384,
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
    "date_created": "2026-07-06T00:07:12Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:11:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gooch

```
<p class="case_cite"><span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d 673</a></span></p>
    <p class="case_cite"><span class="citation no-link">62 USLW 2295</span></p>
    <p class="parties">UNITED STATES of America, Plaintiff-Appellant,<br>v.<br>Kenneth D. GOOCH, Defendant-Appellee.</p>
    <p class="docket">No. 92-35428.</p>
    <p class="court">United States Court of Appeals,<br>Ninth Circuit.</p>
    <p class="date">Argued and Submitted May 4, 1993.<br>Decided Oct. 6, 1993.</p>
    <div class="prelims">
      <p class="indent">Timothy J. Ohms, Asst. U.S. Atty., Spokane, WA, for plaintiff-appellant.</p>
      <p class="indent">Daniel J. Keane and Brian L. Meck, Keane &amp; Rasmussen, Spokane, WA, for defendant-appellee.</p>
      <p class="indent">Appeal from the United States District Court for the Eastern District of Washington.</p>
      <p class="indent">Before:  WRIGHT, ALARCON, and BEEZER, Circuit Judges.</p>
      <p class="indent">BEEZER, Circuit Judge:</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The United States appeals the district court's judgment of acquittal and the subsequent order of dismissal with prejudice of defendant Kenneth D. Gooch's conviction for being a felon in possession of a firearm.  The government contends that a warrantless arrest of Gooch and a warrantless search of Gooch's tent did not violate the Fourth Amendment.  We affirm.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">* At about 3:50 a.m., a woman called the Stevens County Sheriff's office on behalf of Marc Cole, who claimed a man had shot at him at the state campground.  Two officers responded.  As they neared the campsite, they observed a vehicle leaving the campsite.  The occupants told the officers that Gooch was "hurting people" at the campground and that shots had been fired.  Closer to the campground, the officers encountered Marc Cole.  Cole said Gooch had fired a shot in his direction after a fight in which Gooch tried to "stick [Cole's] head into the fire."   These incidents occurred between midnight and 2:00 a.m.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The officers arrived at the entrance to the campground at approximately 5:00 a.m. and then waited some time for the arrival of another deputy and a reserve officer.  It was daylight by this time.  Three officers then headed down the entrance road to the campsite itself, a distance of approximately one mile.  On the way, they encountered a young man, who told them Gooch was in his tent with a woman.  The district court found that when the officers arrived at the campsite, they observed that the campsite was quiet and they determined that Gooch was asleep in his closed tent.<a class="footnote" href="#fn1" id="fn1_ref">1</a>  Gooch had been living in the tent for several days;  he had no other residence.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">The officers, without seeking an arrest warrant, ordered Gooch out of the tent, patted him down, and arrested him.  He was handcuffed and locked in the patrol car 20 yards from the tent.  The officers then ordered the other occupant of the tent, Mary Baker, out of the tent.  The district court found that the officers then talked to other campers for about 15 minutes.  The other campers were not obstructive or threatening, nor was there any indication that they had been involved in the criminal activity.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Still lacking a warrant, the officers searched the tent for the firearm.  One of them found a loaded handgun under Gooch's air mattress in the tent.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">After dismissal of state charges, a federal indictment for being a felon in possession of a firearm was then returned.  A jury convicted Gooch of the federal charge.  Gooch timely moved for judgment of acquittal and for a new trial.  Gooch also filed a Sec. 2255 petition for habeas corpus in which he claimed ineffective assistance of counsel in that his counsel had failed to move to suppress the firearm.  The district court held a post-trial suppression hearing and determined that the firearm, along with the holster and ammunition, should have been suppressed and that the warrantless arrest was invalid.  The district court determined that Gooch had a reasonable expectation of privacy in the tent which was protected under the Fourth Amendment, that there were no "exigent circumstances," and that even if the arrest was lawful, the search was not a valid search incident to arrest.</p>
    </div>
    <p>II</p>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">The threshold issue is whether the Fourth Amendment protects a person's privacy interests in a tent located on a public campground.  The lawfulness of a search or arrest is reviewed de novo.  United States v. Tarazon, <span class="citation" data-id="9484087"><a href="/opinion/603575/united-states-v-ramon-p-tarazon/#1048" aria-description="Citation for case: United States v. Ramon P. Tarazon">989 F.2d 1045, 1048</a></span> (9th Cir.1993), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./114/155/">114 S.Ct. 155</a></span>, <span class="citation no-link">126 L.Ed.2d 116</span> (1993).  The district court's factual findings are reviewed for clear error.  United States v. Echegoyen, <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">799 F.2d 1271, 1277</a></span> (9th Cir.1986).</p>
    </div>
    <p>III</p>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Gooch must have had both a subjective and an objectively reasonable expectation of privacy in the tent.  Katz v. United States, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#516" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507, 516</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967).  The government contends that Gooch could not have had a subjective expectation of privacy in the tent since he could have expected the police to respond to the disturbance he caused and to intrude on his privacy.  According to this view, no lawbreaker would have a subjective expectation of privacy in any place because the expectation of arrest is always imminent.  The court's finding that Gooch established a subjective expectation of privacy is not clearly erroneous.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">We have already established that a person can have an objectively reasonable expectation of privacy in a tent on private property.  LaDuke v. Nelson, <span class="citation" data-id="452994"><a href="/opinion/452994/charles-laduke-v-alan-c-nelson-etc/" aria-description="Citation for case: Charles Laduke v. Alan C. Nelson, Etc.">762 F.2d 1318</a></span>, 1326 n. 11, 1332 n. 19 (9th Cir.1985).  Accord LaDuke v. Castillo, <span class="citation" data-id="1415838"><a href="/opinion/1415838/laduke-v-castillo/" aria-description="Citation for case: LaDuke v. Castillo">455 F.Supp. 209</a></span> (E.D.Wash.1978).  This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp.  The Fourth Amendment "protects people, not places."  Katz, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. at 351</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#511" aria-description="Citation for case: Katz v. United States">88 S.Ct. at 511</a></span>;  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">id. at 351-52</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#511" aria-description="Citation for case: Katz v. United States">88 S.Ct. at 511</a></span> (What a citizen "seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected.");  United States v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U.S. 1, 7</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#2481" aria-description="Citation for case: United States v. Chadwick">97 S.Ct. 2476, 2481</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">53 L.Ed.2d 538</a></span> (1977).  In Rakas v. Illinois, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span> (1978), the Court interpreted Katz to hold that "capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place."  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">Id. at 143</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#430" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 430</a></span>;  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">id.</a></span> at 144 n. 12, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 430</a></span> n. 12.  ("Expectations of privacy protected by the Fourth Amendment ... need not be based on a common-law interest in real or personal property, or on the invasion of such an interest.").</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">The government would have us compare Gooch's case to those involving mobile motor homes, in which a person has a reduced expectation of privacy.  See California v. Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U.S. 386</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">105 S.Ct. 2066</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">85 L.Ed.2d 406</a></span> (1985) (warrantless search of mobile home in which defendant resided did not violate Fourth Amendment because automobile exception applied).  The fact that a tent may be moved, alone, is not enough to remove the Fourth Amendment protections.  As noted above, tents are protected under the Fourth Amendment like a more permanent structure.  Also, a tent is more analogous to a (large) movable container than to a vehicle;  the Fourth Amendment protects expectations of privacy in movable, closed containers.  United States v. Ross, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#811" aria-description="Citation for case: United States v. Ross">456 U.S. 798, 811</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2165" aria-description="Citation for case: United States v. Ross">102 S.Ct. 2157, 2165</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">72 L.Ed.2d 572</a></span> (1982);  United States v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U.S. 1, 13</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#2484" aria-description="Citation for case: United States v. Chadwick">97 S.Ct. 2476, 2484</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">53 L.Ed.2d 538</a></span> (1977).  See also Pottinger v. City of Miami, <span class="citation" data-id="1500109"><a href="/opinion/1500109/pottinger-v-city-of-miami/" aria-description="Citation for case: Pottinger v. City of Miami">810 F.Supp. 1551</a></span> (S.D.Fla.1992) (person has reasonable expectation of privacy in belongings and personal effects in public area);  State v. Mooney, <span class="citation" data-id="7841712"><a href="/opinion/7894385/state-v-mooney/" aria-description="Citation for case: State v. Mooney">218 Conn. 85</a></span>, <span class="citation" data-id="7841712"><a href="/opinion/7894385/state-v-mooney/" aria-description="Citation for case: State v. Mooney">588 A.2d 145</a></span> (same), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./112/330/">112 S.Ct. 330</a></span>, <span class="citation" data-id="9108589"><a href="/opinion/9114090/grumman-aerospace-corp-v-united-states/" aria-description="Citation for case: Grumman Aerospace Corp. v. United States">116 L.Ed.2d 270</a></span> (1991).  Besides, the reduced expectation of privacy in a vehicle is due in large part to the fact that there is "pervasive" government regulation of vehicles.  Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U.S. at 392</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#2069" aria-description="Citation for case: California v. Carney">105 S.Ct. at 2069</a></span> ("These reduced expectations of privacy derive not from the fact that the area to be searched is in plain view, but from the pervasive regulation of vehicles capable of traveling on the public highways.");  South Dakota v. Opperman, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364, 368</a></span>, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#3096" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092, 3096</a></span>, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">49 L.Ed.2d 1000</a></span> (1976).  Finally, even the automobile exception applies only when a vehicle is on the open road or is capable of movement and is "in a place not regularly used for residential purposes--temporary or otherwise."  Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U.S. at 392</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#2070" aria-description="Citation for case: California v. Carney">105 S.Ct. at 2070</a></span>.   The district court did not err in concluding a tent is more like a house than a car.  We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment.</p>
    </div>
    <p>IV</p>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The district court held the police were required to obtain an arrest warrant, so the warrantless arrest was unconstitutional.  No warrant is required to arrest a suspected felon in a public place.  United States v. Watson, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U.S. 411</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976).  Absent exigent circumstances, a warrantless arrest is unconstitutional in a "non-public" place, even when that place is not one's residence.<a class="footnote" href="#fn2" id="fn2_ref">2</a>  United States v. Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#881" aria-description="Citation for case: United States v. Alvarez">810 F.2d 879, 881</a></span> (9th Cir.1987);  Minnesota v. Olson, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U.S. 91</a></span>, 96 n. 5, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">110 S.Ct. 1684</a></span>, 1688 n. 5, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">109 L.Ed.2d 85</a></span> (1990).  See United States v. Ruckman, <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1475" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d 1471, 1475-76</a></span> (10th Cir.1986) (McKay, J., dissenting) (suggesting that inhabitant of cave on public property has an objectively reasonable expectation of privacy therein even if the cave is not considered a house).</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">We have not yet settled whether a tent is a "non-public" place for arrest warrant purposes.  In United States v. Rigsby, <span class="citation" data-id="567665"><a href="/opinion/567665/united-states-v-wendell-b-rigsby/" aria-description="Citation for case: United States v. Wendell B. Rigsby">943 F.2d 631</a></span> (6th Cir.1991), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./112/1269/">112 S.Ct. 1269</a></span>, <span class="citation no-link">117 L.Ed.2d 496</span> (1992), the Sixth Circuit addressed whether an officer who pulled back the unzipped flap of an unoccupied tent and saw a shotgun inside was required to obtain a search warrant.  The court concluded that no search warrant was necessary.  In that case, "there was no indication that the tent was like a 'home' or even a temporary habitation."  Id. at 636.   The court explicitly reserved judgment on the defendant's privacy interest in the tent.  Id. at 636-37 ("This is not to say that defendant had no privacy interest in the tent itself, but merely that the presence of the tent, in which no one was apparently residing, did not create a privacy interest in the otherwise non-private area surrounding it.").</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">The court in People v. Livermore, <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">9 Mich.App. 47</a></span>, <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/#714" aria-description="Citation for case: People v. Livermore">155 N.W.2d 711, 714</a></span> (1967), addressed whether police could enter a tent in a public campground and arrest the occupants.  The court analyzed the case as one involving a "dwelling house" but upheld the arrest because under Michigan law the officers were justified in making a warrantless arrest in a dwelling house.  The court relied on a case involving police entry into a house to support its conclusion that the police entry was justified.  <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">Id.</a></span></p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">The defendant in Livermore also raised the issue whether the tent was a "public" or "private" place, arguing that the information required proof that the crime occurred in a public place.  The state trial court assumed "[f]or the purposes of argument" that the tent was "the equivalent of a private residence notwithstanding its location in a public park," but, like the appellate court, decided the case on other grounds.  <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">Id.</a></span> <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/#715" aria-description="Citation for case: People v. Livermore">155 N.W.2d at 715</a></span>.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Though Gooch's tent was pitched on public property, we hold that the closed tent was a "non-public" place for purposes of Fourth Amendment analysis.  We have recognized that, despite the special status afforded a residence under the Fourth Amendment, "an individual's privacy interests may be implicated in a variety of other settings."  United States v. Driver, <span class="citation" data-id="460378"><a href="/opinion/460378/united-states-v-samuel-clinton-driver-and-panom-driver/#809" aria-description="Citation for case: United States v. Samuel Clinton Driver and Panom Driver">776 F.2d 807, 809</a></span> (9th Cir.1985).  By establishing a campground, the state created a situation where campers were invited to come to set up a tent.  The campers could reasonably assert a legitimate, though temporary, interest in their privacy even in this short-term "dwelling."   A guest in Yellowstone Lodge, a hotel on government park land, would have no less reasonable an expectation of privacy in his hotel room than a guest in a private hotel, and the same logic would extend to a campsite where the opportunity is extended to spend the night.  See Stoner v. California, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#490" aria-description="Citation for case: Stoner v. California">376 U.S. 483, 490</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#893" aria-description="Citation for case: Stoner v. California">84 S.Ct. 889, 893</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">11 L.Ed.2d 856</a></span> (1964) (hotel guest has Fourth Amendment protections).  See also Eng Fung Jem v. United States, <span class="citation" data-id="251769"><a href="/opinion/251769/eng-fung-jem-v-united-states/#805" aria-description="Citation for case: Eng Fung Jem v. United States">281 F.2d 803, 805</a></span> (9th Cir.1960) ("The transience of appellant's stay in the [hotel] room searched by the officers does not dilute the force of constitutional protection.  The hotel room in question was appellant's dwelling.  That he lived there for but several days is of no consequence....  The right to privacy must be accorded with equal vigor both to transient hotel guests and to occupants of private, permanent dwellings.").</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">For the first time on appeal, the government argues that Gooch's use of the campground was wrongful because state law prohibited using the campground primarily for residence purposes.  We do not address that argument, as "[i]ssues not presented to the trial court cannot generally be raised for the first time on appeal."  United States v. Flores-Payon, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/#558" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">942 F.2d 556, 558</a></span> (9th Cir.1991).  Though we can review pure issues of law which were not raised before the district court, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">id.,</a></span> it is not clear from the record, as a matter of law, that Gooch was wrongfully camping at the campground despite the fact that Gooch had no other legal residence.  See Ruckman, <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1476" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d at 1476</a></span> (McKay, J., dissenting).</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">We hold that Gooch's warrantless arrest in his tent violated the proscription of the Fourth Amendment, absent exigent circumstances.</p>
    </div>
    <p>V</p>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">We review de novo whether exigent circumstances justify a warrantless arrest or seizure.  Echegoyen, <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">799 F.2d at 1277-78</a></span>.   The district court's factual findings are reviewed for clear error.  <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">Id. at 1277</a></span>.   The government has the "heavy burden," Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#881" aria-description="Citation for case: United States v. Alvarez">810 F.2d at 881</a></span>, of showing that exigent circumstances "made the warrantless arrest imperative."  United States v. Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#894" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890, 894</a></span> (9th Cir.1985), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986).</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">Exigent circumstances are " 'those in which a substantial risk of harm to the persons involved or to the law enforcement process would arise if the police were to delay a search [or arrest] until a warrant could be obtained.' "  Id. (citation omitted) (brackets in original).  Exigent circumstances are present when "a reasonable person [would] believe that entry ... was necessary to prevent physical harm to the officers or other persons, the destruction of relevant evidence, the escape of the suspect, or some other consequence improperly frustrating legitimate law enforcement efforts."  United States v. McConney, <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1199" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195, 1199</a></span> (9th Cir.)  (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./469/824/">469 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984).</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">* The exigencies cited by the government in justifying the arrest in this case were the risk that evidence would be destroyed and the potential danger to the officers and other campers.<a class="footnote" href="#fn3" id="fn3_ref">3</a>  As the district court observed, there was "no independent indication" that the firearm would be destroyed, nor could it even be removed from the tent with the officers present.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">The district court found the risk of harm to the officers and others to present a closer issue.  The facts that Gooch was intoxicated, that a firearm had been discharged recently, and that people were leaving the campground in fear supported the officers' conclusion that there was an immediate threat to public safety.  However, there was no actual ongoing threat.  The district court found that the campground appeared quiet when the officers arrived in the daylight hours.  The alleged fight and discharge of the firearm took place several hours before the arrest.  The district court did not err in concluding that the deputies could not have reasonably believed that there was a present danger to other occupants of the tent or to other campers.  Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#883" aria-description="Citation for case: United States v. Alvarez">810 F.2d at 883-84</a></span>.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The government compares the circumstances here to those in Al-Azzawy.   In that case, we determined exigent circumstances existed on the sole basis that the police had been informed by a reliable person that the defendant possessed explosives.  Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#894" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 894</a></span>.   However, we expressly contrasted Al-Azzawy's circumstances with those addressed in United States v. Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1161-1163</a></span> (6th Cir.1984), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985).  In Morgan, the court held that defendants' possession of automatic weapons did not give rise to exigent circumstances.</p>
    </div>
    <p>B</p>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">The search was also not justified by exigent circumstances, as the district court found:  "At the time of the search, the defendant was in custody, handcuffed, and locked in the back of a patrol car.  He was not a danger to anyone, and he was the only one that the deputies had any reasonable grounds to believe had violated the law, or who could possibly have been a threat to them."</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">The government argues the officers needed to search the tent immediately because the firearm presented a potential danger to the children at the campsite.  The presence of a firearm alone is not an exigent circumstance.  Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1167" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1167</a></span>;  United States v. Gooch, <span class="citation" data-id="8693761"><a href="/opinion/8710575/united-states-v-gooch/#732" aria-description="Citation for case: United States v. Gooch">780 F.Supp. 725, 732</a></span> (E.D.Wash.1991).  The cases cited by the government involved circumstances where unsupervised children would be left inside the house with the weapon or explosives if the officer did not secure it.  Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#895" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 895</a></span>;  United States v. Antwine, <span class="citation" data-id="522259"><a href="/opinion/522259/united-states-v-james-edward-antwine/#1147" aria-description="Citation for case: United States v. James Edward Antwine">873 F.2d 1144, 1147</a></span> (8th Cir.1989);  United States v. Queen, <span class="citation" data-id="506240"><a href="/opinion/506240/united-states-v-ellery-queen/#353" aria-description="Citation for case: United States v. Ellery Queen">847 F.2d 346, 353</a></span> (7th Cir.1988).  In the instant case, no one remained in the tent at the time of the search.  It would not have been difficult to prevent children or anyone else from entering the tent until a warrant was obtained.  The government's argument logically would authorize any warrantless search where officers had reason to believe a firearm was involved.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">This was not a case in which one or two police officers were forced to react quickly in an inaccessible locale that could only be reached on foot for some distance.  The officers drove directly to the campground, only one mile off the main road, in two vehicles.  They parked just 20 yards from the tent.  Three officers were present to arrest Gooch, with another as backup.  There was no ongoing threat.  We hold that no exigent circumstances existed.</p>
    </div>
    <p>VI</p>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">The government finally contends the search falls into the "search incident to a lawful arrest" exception to the warrant requirement.  Chimel v. California, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U.S. 752</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969).  As the arrest was not lawful, we need not decide whether the warrantless search was a valid search incident to a lawful arrest.</p>
    </div>
    <p class="indent">The district court's judgment is</p>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">AFFIRMED.</p>
    </div>
    <p class="indent">ALARCON, Circuit Judge, dissenting:</p>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">The majority has decided that the district court did not err in concluding that the totality of the circumstances did not justify a warrantless entry and search of Gooch's tent based upon exigent circumstances requiring immediate action to protect the officers from harm.  I cannot join in their opinion because the district court erroneously found that the officers were told prior to the entry that Gooch was asleep.  The majority, while conceding that this finding was clearly erroneous, has failed to discuss the impact of this error regarding an essential fact on the district court's conclusion that there were no exigent circumstances.  Without a remand, this court cannot determine whether, when informed of its error, the district court would reverse its determination that there were no exigent circumstances, especially in light of the fact that it stated that the issue of exigent circumstances created a "difficult question" for the court.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">To appreciate the gravity of the district court's factual error, it is necessary to consider the totality of circumstances known to the officers.  At approximately 4:00 a.m. on July 29, 1990, Stevens County Sheriff's Deputies Ted Campbell and Ed Burns responded to a call from a man claiming to have been shot at the State of Washington Department of Natural Resources ("DNR") campground on Long Lake.  While proceeding to the campground, the deputies encountered an automobile.  The occupants of the car informed the deputies that Ken Gooch was "hurting people" at the DNR campground on Long Lake.  The occupants also indicated that shots had been fired, but did not inform the deputies that Gooch fired the shots.  While proceeding to the campground, the deputies encountered Marc Cole walking alongside the road.  Mr. Cole stated that Gooch fired shots in his direction after they engaged in a family dispute.  These events occurred between midnight and 2:00 a.m.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">Deputies Campbell and Burns arrived at the campground at around 5:00 a.m., where they were subsequently joined by Deputy Steve Bruchman and a reserve deputy.  Without a warrant, the deputies ordered Gooch from his tent.  Gooch was searched and placed under arrest.  After placing Gooch in a patrol car, the deputies ordered Mary Baker, Gooch's companion, from the tent.  Approximately fifteen minutes later, the deputies conducted a warrantless search of the tent and located a loaded handgun under a mattress.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">The district court found that upon arriving at the campground the deputies determined that Gooch was sleeping in his tent.  During oral argument, we requested that counsel for Gooch file a supplemental brief indicating the portion of the record that supported this finding.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">In his supplemental brief, Gooch asserts that the record shows that Sergeant Burns spoke with a pedestrian along the roadside on his way to the campground.  According to Gooch, the pedestrian informed Sergeant Burns that Gooch was sleeping in the tent he shared with his girlfriend.  Gooch acknowledges that Sergeant Burns did not testify, but explains that Deputies Campbell and Bruchman testified that Sergeant Burns had been informed that Gooch was asleep.  Counsel for Gooch has misrepresented the evidence produced in the trial court.  The record does not support the district court's finding that any of the officers were informed prior to the search that Gooch was asleep.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">I agree with the majority that the district court's finding was clearly erroneous.  After acknowledging the district court's error in footnote 1, the majority proceeds to make its own findings regarding whether exigent circumstances justified the search for the handgun without discussing whether the district court's clearly erroneous understanding of the facts caused it to grant the motion.  Therefore, I assume that the majority has made a finding that it didn't matter what the officers were told regarding whether Gooch was asleep.  This determination invades the province of the district court, which has the responsibility to determine factual matters.</p>
    </div>
    <p>III.</p>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">Rule 12(e) of the Federal Rules of Criminal Procedure, which governs motions to suppress, requires that "[w]here factual issues are involved in determining a motion, the [district] court shall state its essential findings on the record."   While Rule 12(e) does not address the precise issue presented here, i.e., what remedy is available to the Government when the district court has made a clearly erroneous finding on a material issue, clearly the drafters of Rule 12(e) assumed that the district court would make accurate factual determinations.  A contrary conclusion would impute to Congress an intent to enact an absurd rule.  We would be required to hold that Rule 12(e) is satisfied if findings are made by the trial court, regardless of the fact that there is no evidence in the record to support them.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">I would hold that if a reviewing court determines that the district court has made a clearly erroneous factual determination on a material issue, a remand is required for further factual findings that reflect on the true state of the record.  The district court must determine, in the first instance, whether the fact that the officers did not know whether Gooch was asleep before they ordered him out of the tent was a factor in persuading them that it was necessary to locate his firearm immediately to protect themselves and others at the campground from lethal force.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">My conclusion that this court cannot substitute itself for the trial court in weighing the effect of the true circumstances relied upon by the officers in believing that exigent circumstances required a warrantless search is supported by the Supreme Court's analysis in Murray v. United States, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">487 U.S. 533</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">101 L.Ed.2d 472</a></span> (1988).  In Murray, federal law enforcement agents conducted a warrantless entry into a Boston warehouse where they observed bales of marijuana.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#535" aria-description="Citation for case: Murray v. United States">Id. at 535</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2532" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2532</a></span>.   The agents placed the warehouse under surveillance and applied for a search warrant, without informing the magistrate of the initial entry or the marijuana they observed.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#535" aria-description="Citation for case: Murray v. United States">Id. at 535-36</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2532" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2532</a></span>.   At issue was whether the second search was truly independent from the initial warrantless search.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#542" aria-description="Citation for case: Murray v. United States">Id. at 542</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2535" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2535</a></span>.   The district court denied the motion and the appellate court affirmed, concluding that it was "absolutely certain that the warrantless entry in no way contributed in the slightest either to the issuance of a warrant or to the discovery of the evidence during the lawful search that occurred pursuant to the warrant."  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#542" aria-description="Citation for case: Murray v. United States">Id. at 542-43</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">The Supreme Court determined that the record did not support the Court of Appeals' findings on the application of the independent source doctrine and remanded for further factual findings on the contested issue.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#543" aria-description="Citation for case: Murray v. United States">Id. at 543-44</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.   The Court concluded that "it is the function of the District Court rather than the Court of Appeals to determine the facts."  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#543" aria-description="Citation for case: Murray v. United States">Id. at 543</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.   In a case such as this, where the district court has made erroneous factual findings, we may not substitute our judgment for that of the district court and make a factual finding that the totality of the circumstances did not establish exigent circumstances justifying the warrantless search of Gooch's tent and the seizure of his firearm.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">We have previously relied on Murray in determining that Rule 12(e) requires the district court to make essential findings of fact when ruling upon a motion to suppress.  See United States v. Prieto-Villa, <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/" aria-description="Citation for case: United States v. Pedro Prieto-Villa">910 F.2d 601</a></span> (9th Cir.1990).  In Prieto-Villa, the defendant was arrested while the police searched a co-defendant's apartment in the process of investigating a drug conspiracy.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#602" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 602</a></span>.   Prieto filed a pre-trial motion to suppress the introduction of cocaine and post-arrest statements made to the police.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#603" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 603</a></span>.   The district court denied his motion but failed to make sufficient factual findings to permit appellate review.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#605" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 605-06</a></span>.   We held that Rule 12(e) required the district court to make appropriate factual findings and remanded for the development of an adequate record.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#607" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 607</a></span>.   In determining that Rule 12(e) imposed a mandatory requirement on the district court, we cited Murray for the proposition that the district court, and not the appellate court, is responsible for making factual findings.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#608" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 608-610</a></span>.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">I believe it is particularly important that we remand this matter to the district court to rectify its unsupportive finding, because of the consequences of the district court's clear error.  We have previously noted that a suppression hearing is "often as important as the trial itself."  Prieto-Villa, <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/" aria-description="Citation for case: United States v. Pedro Prieto-Villa">910 F.2d at 609</a></span> (quoting Waller v. Georgia, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#46" aria-description="Citation for case: Waller v. Georgia">467 U.S. 39, 46</a></span>, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#2215" aria-description="Citation for case: Waller v. Georgia">104 S.Ct. 2210, 2215</a></span>, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/" aria-description="Citation for case: Waller v. Georgia">81 L.Ed.2d 31</a></span> (1984)).  This observation is particularly important in this case, as the Government has conceded that it would be unable to sustain its burden of proof in the absence of the physical evidence seized from Gooch's tent.  In light of the fact that the district court stated that whether the facts in this case demonstrated a "difficult question," the district court resolved that question against the Government based on an erroneous factual finding.  A remand is mandatory under the Supreme Court's decision in Murray, and the law of this circuit as explained in Prieto-Villa.</p>
    </div>
    <p>IV.</p>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">The Government has also raised serious questions concerning Gooch's alleged violations of numerous Washington state regulations prohibiting the use of campground property primarily for residential purposes.  The Government cites California v. Ciraolo, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1985) for the proposition that a person must have a legitimate expectation of privacy to invoke the protection of the Fourth Amendment.  <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">Id. at 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#1811" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. at 1811</a></span>.   If these regulations were indeed violated, Gooch may not be able to demonstrate that he had a legitimate expectation of privacy in his tent.  The Government, however, failed to raise this argument before the district court.  Under the law of this circuit, "[i]ssues not presented to the trial court cannot generally be raised for the first time on appeal."  United States v. Flores-Payon, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/#558" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">942 F.2d 556, 558</a></span> (8th Cir.1991).  Because I believe the Supreme Court's decision in Murray requires that we remand this case to the district court, the question whether Gooch had a legitimate expectation of privacy in a tent used as a residence in violation of Washington law should be resolved in the district court.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Although Gooch had either fallen asleep or passed out due to alcohol consumption, there is no evidence in the record that the officers knew that fact.  This finding of the district court is clearly erroneous</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> As it happens, Gooch's tent was his residence.  However, the police officers could not reasonably have been expected to realize that fact.  This opinion does not rely in any way on the fact that Gooch actually had no other residence</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> The government also noted that problems with radio communication in the southwest corner of the county would have made obtaining a warrant inconvenient.  "Police officers may not, in their zeal to arrest an individual, ignore the [F]ourth [A]mendment's warrant requirement merely because it is inconvenient."  United States v. Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1164</a></span> (6th Cir.1984), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985)</p>
      </div>
    </div>
    
```

---

## GROUP: content/cases/United States v. Hensley.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Hensley"
type: case
citation: "469 U.S. 221 (1985)"
parallel_cite: "105 S. Ct. 675; 83 L. Ed. 2d 604; 53 U.S.L.W. 4053"
neutral_cite: 1985 U.S. LEXIS 34
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-08
docket: 83-1330
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Hensley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111294/united-states-v-hensley/"
  cluster_id: 111294
  opinion_id: 9429804
  identity_checked: true
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[Delaware v. Prouse]]", "[[United States v. Cortez]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "collective-knowledge", "fellow-officer-rule", "wanted-flyer", "completed-crime"]
holding: "Police may conduct a Terry investigatory stop in objective reliance on a wanted flyer or bulletin issued by another police department if…"
lake:
  record_id: United States v. Hensley
  status: verified
  projected_at: 2026-07-06
---

# United States v. Hensley

*469 U.S. 221 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an armed tavern robbery in St. Bernard, Ohio, an informant told Officer Davis that Thomas Hensley had driven the getaway car. Davis took a written statement and issued a "wanted flyer" to other Cincinnati-area departments, describing Hensley and the robbery and asking them to pick him up. Covington, Kentucky officers, who had read the flyer at shift changes, recognized Hensley days later, stopped his car, and — after one officer approached and saw a handgun — arrested him. Hensley, a felon, was convicted of being a felon in possession.

## Issue
(1) Whether the Fourth Amendment permits a *[[Terry v. Ohio|Terry]]* investigatory stop on reasonable suspicion that a person was involved in a *completed* crime; and (2) whether officers may make such a stop in objective reliance on a "wanted flyer" issued by another department.

## Rule
Yes to both. First, *[[Terry v. Ohio|Terry]]* stops are not confined to ongoing or imminent crimes: "if police have a reasonable suspicion, grounded in specific and articulable facts, that a person they encounter was involved in or is wanted in connection with a completed felony, then a *Terry* stop may be made to investigate that suspicion." — 469 U.S. at 229. ^pin-229

Second, the validity of a stop made in reliance on a bulletin turns on the issuing department's knowledge, judged objectively: "It is the objective reading of the flyer or bulletin that determines whether other police officers can defensibly act in reliance on it." — *Id.* at 232. ^pin-232

"Assuming the police make a *Terry* stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who *issued* the flyer or bulletin possessed a reasonable suspicion justifying a stop, and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department." — *Id.* at 233. ^pin-233

## Application
On these facts the Covington stop was lawful. Although the robbery was already completed, the St. Bernard police had a reasonable suspicion — grounded in the informant's specific account that Hensley drove the getaway car, reduced to a written statement — sufficient to justify a stop, and that suspicion "underlies and supports their issuance of the flyer." The Covington officers acted in objective reliance on the flyer, and the stop they made "was not significantly more intrusive than would have been permitted the St. Bernard police." Because the issuing department had the requisite reasonable suspicion and the actual stop stayed within those bounds, "the investigatory stop was reasonable under the Fourth Amendment, and the evidence discovered during the stop was admissible." The Court did not need to decide whether the issuing department had probable cause, nor whether *[[Terry v. Ohio|Terry]]* reaches all completed crimes — reasonable suspicion of a completed felony was enough.

## Conclusion
A *[[Terry v. Ohio|Terry]]* stop may rest on reasonable suspicion of a completed felony, and officers may make it in objective reliance on another department's flyer where the issuing department had reasonable suspicion; the Sixth Circuit's judgment reversing the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Hensley* is the foundational SCOTUS statement of the collective-knowledge / fellow-officer rule for investigatory stops, extending the [[Terry v. Ohio]] framework to completed crimes and to inter-department bulletin reliance.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key — Anchor*

## Sources
- *United States v. Hensley*, 469 U.S. 221 (1985) — https://www.courtlistener.com/opinion/111294/united-states-v-hensley/ — pinpoints: 229, 232, 233.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "eb19bdb8cbb459b4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "469 U.S. 221 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 34", "official_citation_present": true, "parallel_cite": "105 S. Ct. 675; 83 L. Ed. 2d 604; 53 U.S.L.W. 4053", "title": "United States v. Hensley", "year": "1985"}}
{"assertion_id": "3085aac571a69aa3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police may conduct a Terry investigatory stop in objective reliance on a wanted flyer or bulletin issued by another police department if…", "title": "United States v. Hensley"}}
{"assertion_id": "fdc9d1a15990ed7b", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key — Anchor", "title": "United States v. Hensley"}}
{"assertion_id": "5d2f0977373aaebd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-01-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Hensley", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Hensley", "varies_by_point": "false"}}
{"assertion_id": "fdd2ef677986d631", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Hensley"}}
```

### lake record — United States v. Hensley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hensley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Hensley",
    "case_name_short": "Hensley",
    "case_name_full": "United States v. Hensley",
    "input_case_name": "United States v. Hensley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-08",
    "year": 1985,
    "docket": "83-1330",
    "cluster_id": 111294,
    "lead_opinion_id": 9429804,
    "sibling_ids": [
      111294,
      9429804,
      9429805
    ],
    "absolute_url": "/opinion/111294/united-states-v-hensley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 221",
      "volume": "469",
      "reporter": "U.S.",
      "page": "221",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 675",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 604",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4053",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4053",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 34",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 221",
        "volume": "469",
        "reporter": "U.S.",
        "page": "221",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 675",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "675",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 604",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 34",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4053",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4053",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 221",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 221",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-229",
      "page": null,
      "quote": "issued by another department. ## Rule Yes to both. First, *Terry* stops are not confined to ongoing or imminent crimes:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-232",
      "page": null,
      "quote": "It is the objective reading of the flyer or bulletin that determines whether other police officers can defensibly act in reliance on it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-233",
      "page": null,
      "quote": "Assuming the police make a *Terry* stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who *issued* the flyer or bulletin possessed a reasonable suspicion justifying a stop, and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Hensley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Connor William Clar Steffens",
          "cluster_id": 4332280,
          "cite": [
            "889 N.W.2d 691",
            "2016 Iowa App. LEXIS 1316",
            "2016 WL 7393893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Keene",
          "cluster_id": 3189183,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Emerson",
          "cluster_id": 2830814,
          "cite": [
            "2015 MT 254",
            "380 Mont. 487",
            "2015 Mont. LEXIS 441",
            "355 P.3d 763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. State",
          "cluster_id": 2449770,
          "cite": [
            "955 S.W.2d 85",
            "1997 Tex. Crim. App. LEXIS 72",
            "1997 WL 587024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Winston v. Lee",
          "cluster_id": 111380,
          "cite": [
            "84 L. Ed. 2d 662",
            "105 S. Ct. 1611",
            "470 U.S. 753",
            "1985 U.S. LEXIS 76",
            "53 U.S.L.W. 4367"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hayes v. Florida",
          "cluster_id": 111382,
          "cite": [
            "84 L. Ed. 2d 705",
            "105 S. Ct. 1643",
            "470 U.S. 811",
            "1985 U.S. LEXIS 1523",
            "53 U.S.L.W. 4382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Maumee v. Weisner",
          "cluster_id": 2689810,
          "cite": [
            "1999 Ohio 68",
            "87 Ohio St. 3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zellner v. Summerlin",
          "cluster_id": 2707,
          "cite": [
            "494 F.3d 344",
            "2007 U.S. App. LEXIS 17272",
            "2007 WL 2067932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Anthony Perdue",
          "cluster_id": 656633,
          "cite": [
            "8 F.3d 1455",
            "1993 U.S. App. LEXIS 28321",
            "1993 WL 437983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McKnight",
          "cluster_id": 6894158,
          "cite": [
            "107 Ohio St. 3d 101",
            "837 N.E.2d 315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delk v. State",
          "cluster_id": 1669263,
          "cite": [
            "855 S.W.2d 700",
            "1993 Tex. Crim. App. LEXIS 88",
            "1993 WL 120353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
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
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kennedy",
          "cluster_id": 1374527,
          "cite": [
            "726 P.2d 445",
            "107 Wash. 2d 1",
            "1986 Wash. LEXIS 1273"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Hensley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111294 OR 9429804 OR 9429805) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk4MTI0ODAwMDAwJnM9MjY3MDc5NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111294+OR+9429804+OR+9429805%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111294 OR 9429804 OR 9429805)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDEmcz0yNDI5NjQ2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111294+OR+9429804+OR+9429805%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111294 OR 9429804 OR 9429805)",
        "reviewed": 54,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 54,
        "triage_read": 2,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111294 OR 9429804 OR 9429805)",
    "indexed_citing_opinions": 1345,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111294,
        "count": 1147,
        "count_source": "search"
      },
      {
        "opinion_id": 9429804,
        "count": 216,
        "count_source": "search"
      },
      {
        "opinion_id": 9429805,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2344,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-hensley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDQ4MDgmcz0xMDE2MTI2OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111294+OR+9429804+OR+9429805%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111294,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 311449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 324941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 336263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 372580,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111294,
        "cited_id": 422083,
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
    "date_created": "2026-07-06T00:38:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:41:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Hensley

```
<opinion type="majority">
<author id="b365-4"><page-number citation-index="1" label="223">*223</page-number>Justice O’Connor</author>
<p id="AXO">delivered the opinion of the Court.</p>
<p id="b365-5">We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1203/">467 U. S. 1203</a></span> (1984), to determine whether police officers may stop and briefly detain a person who is the subject of a “wanted flyer” while they attempt to find out whether an arrest warrant has been issued. We conclude that such stops are consistent with the Fourth Amendment under appropriate circumstances.</p>
<p id="b365-6">I</p>
<p id="b365-7">On December 4, 1981, two armed men robbed a tavern in the Cincinnati suburb of St. Bernard, Ohio. Six days later, a St. Bernard police officer, Kenneth Davis, interviewed an informant who passed along information that respondent Thomas Hensley had driven the getaway car during the armed robbery. Officer Davis obtained a written statement from the informant and immediately issued a “wanted flyer” to other police departments in the Cincinnati metropolitan area.</p>
<p id="b365-8">The flyer twice stated that Hensley was wanted for investigation of an aggravated robbery. It described both Hensley and the date and location of the alleged robbery, and asked other departments to pick up and hold Hensley for the St. Bernard police in the event he were located. The flyer also warned other departments to use caution and to consider Hensley armed and dangerous.</p>
<p id="b365-9">The St. Bernard Police Department’s “wanted flyer” was received by teletype in the headquarters of the Covington Police Department on December 10,' 1981. Covington is a Kentucky suburb of Cincinnati that is approximately five miles from St. Bernard. The flyer was read aloud at each change of shift in the Covington Police Department between December 10 and December 16, 1981. Some of the Coving-ton officers were acquainted with Hensley, and after December 10 they periodically looked for him at places in Covington he was known to frequent.</p>
<p id="b365-10">On December 16, 1981, Covington Officer Terence Eger saw a white Cadillac convertible stopped in the middle of a <page-number citation-index="1" label="224">*224</page-number>Covington street. Officer Eger saw Hensley in the driver’s seat and asked him to move on. As Hensley drove away, Eger inquired by radio whether there was a warrant outstanding for Hensley’s arrest. Before the dispatcher could answer, two other Covington officers who were in separate cars on patrol interrupted to say that there might be an Ohio robbery warrant outstanding on Hensley. The officers, Daniel Cope and David Rassache, subsequently testified that they had heard or read the St. Bernard flyer on several occasions, that they recalled that the flyer sought a stop for investigation only, and that in their experience the issuance of such a flyer was usually followed by the issuance of an arrest warrant. While the dispatcher checked to see whether a warrant had been issued, Officer Cope drove to a Holman Street address where Hensley occasionally stayed, and Officer Rassache went to check a second location.</p>
<p id="b366-5">The dispatcher had difficulty in confirming whether a warrant had been issued. Unable to locate the flyer, she called the Cincinnati Police Department on the mistaken belief that the flyer had originated in Cincinnati. The Cincinnati Police Department transferred the call to its records department, which placed the dispatcher on hold. In the meantime, Officer Cope reported that he had sighted a white Cadillac approaching him on Holman Street. Cope turned on his flashing lights and Hensley pulled over to the curb. Before Cope left his patrol car, the dispatcher advised him that she had “Cincinnati hunting for the warrant,” App. 49, but that she had not yet confirmed it. Cope approached Hensley’s car with his service revolver drawn and pointed into the air. He had Hensley and a passenger seated next to him step out of the car.</p>
<p id="b366-6">Moments later, Officer Rassache arrived in his separate car. He recognized the passenger, Albert Green, a convicted felon. Rassache stepped up to the open passenger door of Hensley’s car and observed the butt of a revolver protruding from underneath the passenger’s seat. Green <page-number citation-index="1" label="225">*225</page-number>was then arrested. A search of the car uncovered a second handgun wrapped in a jacket in the middle of the front seat and a third handgun in a bag in the back seat. After the discovery of these weapons, Hensley was also arrested.</p>
<p id="b367-5">After state handgun possession charges against Hensley were dismissed, Hensley was indicted by a federal grand jury in the Eastern District of Kentucky for being a convicted felon in possession of firearms in violation of 18 U. S. C. App. § 1202(a)(1). Hensley moved to suppress the handguns from evidence on the grounds that the Covington police had imper-missibly stopped him in violation of the Fourth Amendment and the principles announced in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). The District Judge held the stop to be proper and denied the motion. Respondent was convicted after a bench/ trial and sentenced to two years in federal prison.</p>
<p id="b367-7">The United States Court of Appeals for the Sixth Circuit reversed the conviction. <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d 220</a></span> (1983). The panel noted that the Covington police could not justifiably conclude from the St. Bernard flyer that a warrant had been issued for Hensley’s arrest; nor could the Covington police stop the respondent while they attempted to find out whether a warrant had in fact been issued. Reviewing this Court’s decisions applying <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the Sixth Circuit concluded that investigative stops remain a narrow exception to the probable-cause requirement, and that this Court has manifested a “clear intention to restrict investigative stops to settings involving the investigation of ongoing crimes.” <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#225" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 225</a></span>. Since Covington police encountered Hensley almost two weeks after the armed robbery in St. Bernard, they had no reason to believe they were investigating an ongoing crime. Because the Covington police were familiar only with the St. Bernard flyer, and not with the specific information which led the St. Bernard police to issue the flyer, the Court of Appeals held they lacked a reasonable suspicion sufficient-to justify an investigative stop. The Court of Appeals concluded that Hensley’s conviction rested on evidence obtained <page-number citation-index="1" label="226">*226</page-number>through an illegal arrest, and therefore had to be reversed. We disagree, and now reverse.</p>
<p id="b368-5">II</p>
<p id="b368-6">The Fourth Amendment protects the right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures. In <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry, supra,</a></span> </em>and subsequent cases, this Court has held that, consistent with the Fourth Amendment, police may stop persons in the absence of probable cause under limited circumstances. See <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 207-211</a></span> (1979). In particular, the Court has noted that law enforcement agents may briefly stop a moving automobile to investigate a reasonable suspicion that its occupants are involved in criminal activity. See <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975) (within United States borders, Government interest in preventing illegal entry of aliens permits a <em>Terry </em>stop on reasonable suspicion that particular vehicle contains aliens). Although stopping a car and detaining its occupants constitute a seizure within the meaning of the Fourth Amendment, the governmental interest in investigating an officer’s reasonable suspicion, based on specific and articulable facts, may outweigh the Fourth Amendment interest of the driver and passengers in remaining secure from the intrusion. See <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-655</a></span> (1979).</p>
<p id="b368-7">In this case, the Sixth Circuit announced two prerequisites to such an investigatory stop and held that they were lacking: first, the crime being investigated was not imminent or ongoing, but rather was already completed; second, the “wanted flyer” was insufficient to create a reasonable suspicion that respondent had engaged in criminal activity. If either part of this analysis is correct, then it was indeed improper to stop respondent, and his conviction cannot stand. We accordingly turn to the separate but related issues of <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops to investigate completed crimes and <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops in reliance on another police department’s “wanted flyer.”</p>
<p id="b369-4"><page-number citation-index="1" label="227">*227</page-number>A</p>
<p id="b369-5">This is the first case we have addressed in which police stopped a person because they suspected he was involved in a completed crime. In our previous decisions involving investigatory stops on less than probable cause, police stopped or seized a person because they suspected he was about to commit a crime, <em>e. g., <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry, supra,</a></span> </em>or was committing a crime at the moment of the stop, <em>e. g., Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972). Noting that <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), struck down a particularly intrusive detention of a person suspected of committing an ongoing crime, the Court of Appeals in this case concluded that we clearly intended to restrict investigative stops to the context of ongoing crimes.</p>
<p id="b369-6">We do not agree with the Court of Appeals that our prior opinions contemplate an inflexible rule that precludes police from stopping persons they suspect of past criminal activity unless they have probable cause for arrest. To the extent previous opinions have addressed the issue at all, they have suggested that some investigative stops based on a reasonable suspicion of past criminal activity could withstand Fourth Amendment scrutiny. Thus <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417, n. 2</a></span> (1981), indicates in a footnote that “[o]f course, an officer may stop and question a person if there are reasonable grounds to believe that person is wanted for past criminal conduct.” And in <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), decided barely a month before the Sixth Circuit’s opinion, this Court stated that its prior opinions acknowledged police authority to stop a person “when the officer has reasonable, articulable suspicion that the person <em>has been, </em>is, or is about to be engaged in criminal activity.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#702" aria-description="Citation for case: United States v. Place"><em>Id., </em>at 702</a></span> (emphasis added). See also <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#699" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 699</a></span>, and n. 7 (1981). Indeed, <em>Florida </em>v. <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Royer</a></span> </em>itself suggests that certain seizures are justifiable under the Fourth Amendment even in the absence of probable cause “if there is articulable suspicion that a person <em>has committed </em>or is about to commit a crime.” <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S., at 498</a></span> (plurality opinion) (emphasis added).</p>
<p id="b370-4"><page-number citation-index="1" label="228">*228</page-number>At the least, these dicta suggest that the police are not automatically shorn of authority to stop a suspect in the absence of probable cause merely because the criminal has completed his crime and escaped from the scene. The precise limits on investigatory stops to investigate past criminal activity are more difficult to define. The proper way to identify the limits is to apply the same test already used to identify the proper bounds of intrusions that further investigations of imminent or ongoing crimes. That test, which is grounded in the standard of reasonableness embodied in the Fourth Amendment, balances the nature and quality of the intrusion on personal security against the importance of the governmental interests alleged to justify the intrusion. <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 703</a></span>; <em>Michigan </em>v. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#698" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 698-701</a></span>. When this balancing test is applied to stops to investigate past crimes, we think that probable cause to arrest need not always be required.</p>
<p id="b370-5">The factors in the balance may be somewhat different when a stop to investigate past criminal activity is involved rather than a stop to investigate ongoing criminal conduct. This is because the governmental interests and the nature of the intrusions involved in the two situations may differ. As we noted in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>one general interest present in the context of ongoing or imminent criminal activity is “that of effective crime prevention and detection.” <em>Terry, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. A stop to investigate an already completed crime does not necessarily promote the interest of crime prevention as directly as a stop to investigate suspected ongoing criminal activity. Similarly, the exigent circumstances which require a police officer to step in before a crime is committed or completed are not necessarily as pressing long afterwards. Public safety may be less threatened by a suspect in a past crime who now appears to be going about his lawful business than it is by a suspect who is currently in the process of violating the law. Finally, officers making a stop to investigate past crimes may have a wider range of opportunity to <page-number citation-index="1" label="229">*229</page-number>choose the time and circumstances of the stop. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979); ALI Model Code of Pre-Arraignment Procedure 12 (Prop. Off. Draft No. 1, 1972).</p>
<p id="b371-5">Despite these differences, where police have been unable to locate a person suspected of involvement in a past crime, the ability to briefly stop that person, ask questions, or check identification in the absence of probable cause promotes the strong government interest in solving crimes and bringing offenders to justice. Restraining police action until after probable cause is obtained would not only hinder the investigation, but might also enable the suspect to flee in the interim and to remain at large. Particularly in the context of felonies or crimes involving a threat to public safety, it is in the public interest that the crime be solved and the suspect detained as promptly as possible. The law enforcement interests at stake in these circumstances outweigh the individual’s interest to be free of a stop and detention that is no more extensive than permissible in the investigation of imminent or ongoing crimes.</p>
<p id="b371-6">We need not and do not decide today whether <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops to investigate all past crimes, however serious, are permitted. It is enough to say that, if police have a reasonable suspicion, grounded in specific and articulable facts, that a person they encounter was involved in or is wanted in connection with a completed felony, then a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop may be made to investigate that suspicion. The automatic barrier to such stops erected by the Court of Appeals accordingly cannot stand.</p>
<p id="b371-7">B</p>
<p id="b371-8">At issue in this case is a stop of a person by officers of one police department in reliance on a flyer issued by another department indicating that the person is wanted for investigation of a felony. The Court of Appeals concluded that “the Fourth Amendment does not permit police officers in one department to seize a person simply because a neighboring <page-number citation-index="1" label="230">*230</page-number>police department has circulated a flyer reflecting the desire to question that individual about some criminal investigation that does not involve the arresting officers or their department.” <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#225" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 225</a></span>. This holding apparently rests on the omission from the flyer of the specific and articulable facts which led the first department to suspect respondent’s involvement in a completed crime. <em><span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/" aria-description="Citation for case: United States v. Thomas J. Hensley">Ibid.</a></span></em></p>
<p id="b372-5">This Court discussed a related issue in <em>Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971). In <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span>, </em>a county sheriff in Wyoming obtained an arrest warrant for a person suspected of burglary. The sheriff then issued a message through a statewide law enforcement radio network describing the suspect, his car, and the property taken. At least one version of the message also indicated that a warrant had been issued. <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#564" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 564</a></span>, and n. 5. The message did not specify the evidence that gave the sheriff probable cause to believe the suspect had committed the breaking and entering. In reliance on the radio message, police in Laramie stopped the suspect and searched his car. The Supreme Court, in an opinion by Justice Harlan, ultimately concluded that the sheriff had lacked probable cause to obtain the warrant and that the evidence obtained during the search by the police in Laramie had to be excluded. In so ruling, however, the Court noted:</p>
<blockquote id="b372-6">“We do not, of course, question that the Laramie police were entitled to act on the strength of the radio bulletin. Certainly police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.” <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary"><em>Id., </em>at 568</a></span>.</blockquote>
<p id="b372-7">This language in <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>suggests that, had the sheriff who issued the radio bulletin possessed probable cause for <page-number citation-index="1" label="231">*231</page-number>arrest, then the Laramie police could have properly arrested the defendant even though they were unaware of the specific facts that established probable cause. See <em>United States </em>v. <em>Maryland, </em><span class="citation" data-id="311449"><a href="/opinion/311449/united-states-v-napoleon-maryland-jr/#569" aria-description="Citation for case: United States v. Napoleon Maryland, Jr.">479 F. 2d 566, 569</a></span> (CA5 1973). Thus <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>supports the proposition that, when evidence is uncovered during a search incident to an arrest in reliance merely on a flyer or bulletin, its admissibility turns on whether the officers who <em>issued </em>the flyer possessed probable cause to make the arrest. It does not turn on whether those relying on the flyer were themselves aware of the specific facts which led their colleagues to seek their assistance. In an era when criminal suspects are increasingly mobile and increasingly likely to flee across jurisdictional boundaries, this rule is a matter of common sense: it minimizes the volume of information concerning suspects that must be transmitted to other jurisdictions and enables police in one jurisdiction to act promptly in reliance on information from another jurisdiction.</p>
<p id="b373-5">Neither respondent nor the Court of Appeals suggests any reason why a police department should be able to act on the basis of a flyer indicating that another department has a warrant, but should not be able to act on the basis of a flyer indicating that another department has a reasonable suspicion of involvement with a crime. Faced with this precise issue, the Court of Appeals for the Ninth Circuit applied <em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span> </em>and concluded that, although the officer who issues a wanted bulletin must have a reasonable suspicion sufficient to justify a stop, the officer who acts in reliance on the bulletin is not required to have personal knowledge of the evidence creating a reasonable suspicion. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/#1300" aria-description="Citation for case: United States v. Steven Linwood Robinson">536 F. 2d 1298, 1300</a></span> (1976). The Ninth Circuit there noted “that effective law enforcement cannot be conducted unless police officers can act on directions and information transmitted by one officer to another and that officers, who must often act swiftly, cannot be expected to cross-examine their fellow officers about the foundation for the transmitted information.” <span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/#1299" aria-description="Citation for case: United States v. Steven Linwood Robinson"><em>Id., </em>at 1299</a></span>.</p>
<p id="b374-4"><page-number citation-index="1" label="232">*232</page-number>It could be argued that police can more justifiably rely on a report that a magistrate has issued a warrant than on a report that another law enforcement agency has simply concluded that it has a reasonable suspicion sufficient to authorize an investigatory stop. We do not find this distinction significant. The law enforcement interests promoted by allowing one department to make investigatory stops based upon another department’s bulletins or flyers are considerable, while the intrusion on personal security is minimal. The same interests that weigh in favor of permitting police to make a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop to investigate a past crime, <em>swpra, </em>at 229, support permitting police in other jurisdictions to rely on flyers or bulletins in making stops to investigate past crimes.</p>
<p id="b374-5">We conclude that, if a flyer or bulletin has been issued on the basis of articulable facts supporting a reasonable suspicion that the wanted person has committed an offense, then reliance on that flyer or bulletin justifies a stop to check identification, see <em>United States ex rel. Kirby </em>v. <em>Sturges, </em><span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#400" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 400-401</a></span> (CA7) (Stevens, J.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/1016/">421 U. S. 1016</a></span> (1975), to pose questions to the person, or to detain the person briefly while attempting to obtain further information. See <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972) (“A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be the most reasonable in light of the facts known to the officer at the time”). If the flyer has been issued in the absence of a reasonable suspicion, then a stop in the objective reliance upon it violates the Fourth Amendment. In such a situation, of course, the officers making the stop may have a good-faith defense to any civil suit. See <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974); <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547</a></span> (1967); <em>Turner </em>v. <em>Raynes, </em><span class="citation" data-id="372580"><a href="/opinion/372580/jack-e-turner-v-e-t-raynes-and-bill-edd-jones/#93" aria-description="Citation for case: Jack E. Turner v. E. T. Raynes and Bill Edd Jones">611 F. 2d 92, 93</a></span> (CA5) (officer relying in good faith on an invalid arrest warrant has defense to civil suit), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/900/">449 U. S. 900</a></span> (1980). It is the objective reading of the flyer or bulletin that determines whether other <page-number citation-index="1" label="233">*233</page-number>police officers can defensibly act in reliance on it. Cf. Terry, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21-22</a></span> (“it is imperative that the facts be judged against an objective standard: would the facts available to the officer at the moment of the seizure or the search ‘warrant a man of reasonable caution in the belief’ that the action taken was appropriate?”). Assuming the police make a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop in objective reliance on a flyer or bulletin, we hold that the evidence uncovered in the course of the stop is admissible if the police who <em>issued </em>the flyer or bulletin possessed a reasonable suspicion justifying a stop, <em>United States </em>v. <em><span class="citation" data-id="9462804"><a href="/opinion/336263/united-states-v-steven-linwood-robinson/" aria-description="Citation for case: United States v. Steven Linwood Robinson">Robinson, supra,</a></span> </em>and if the stop that in fact occurred was not significantly more intrusive than would have been permitted the issuing department.</p>
<p id="b375-8">H-I ► — i I — f</p>
<p id="b375-3">It remains to apply the two sets of principles described above to the stop and subsequent arrest of respondent Hensley.</p>
<p id="b375-4">At the outset, we assume, <em>arguendo, </em>that the St. Bernard police who issued the “wanted flyer” on Hensley lacked probable cause for his arrest. The District Court implied that the St. Bernard police had probable cause for arrest, but held only that the St. Bernard officers had reasonable suspicion sufficient to justify a stop. App. to Pet. for Cert. 14a. The Court of Appeals implied that probable cause might be lacking, <span class="citation" data-id="422083"><a href="/opinion/422083/united-states-v-thomas-j-hensley/#223" aria-description="Citation for case: United States v. Thomas J. Hensley">713 F. 2d, at 223</a></span>, but ultimately concluded that the question was irrelevant because the Covington police would not be entitled to make an arrest or a stop regardless of whether the St. Bernard police possessed probable cause or a reasonable suspicion. In this Court, no party contends that the St. Bernard police had probable cause to arrest Hensley.</p>
<p id="b375-5">We agree with the District Court that the St. Bernard police possessed a reasonable suspicion, based on specific and articulable facts, that Hensley was involved in an armed robbery. The District Judge heard testimony from the St. Bernard officer who interviewed the informant. On the strength of the evidence, the District Court concluded <page-number citation-index="1" label="234">*234</page-number>that the wealth of detail concerning the robbery revealed by the informant, coupled with her admission of tangential participation in the robbery, established that the informant was sufficiently reliable and credible “to arouse a reasonable suspicion of criminal activity by [Hensley] and to constitute the specific and articulable facts needed to underly a stop.” App. to Pet. for Cert. 14a. Under the circumstances, “the information carried enough indicia of reliability,” <em>Adams </em>v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams"><em>Williams, supra, </em>at 147</a></span>, to justify an investigatory stop of Hensley.</p>
<p id="b376-5">The justification for a stop did not evaporate when the armed robbery was completed. Hensley was reasonably suspected of involvement in a felony and was at large from the time the suspicion arose until the stop by the Covington police. A brief stop and detention at the earliest opportunity after the suspicion arose is fully consistent with the principles of the Fourth Amendment.</p>
<p id="b376-6">Turning to the flyer issued by the St. Bernard police, we believe it satisfies the objective test announced today. An objective reading of the entire flyer would lead an experienced officer to conclude that Thomas Hensley was at least wanted for questioning and investigation in St. Bernard. Since the flyer was issued on the basis of articulable facts supporting a reasonable suspicion, this objective reading would justify a brief stop to check Hensley’s identification, pose questions, and inform the suspect that the St. Bernard police wished to question him. As an experienced officer could well assume that a warrant might have been obtained in the period after the flyer was issued, we think the flyer would further justify a brief detention at the scene of the stop while officers checked whether a warrant had in fact been issued. It is irrelevant whether the Covington officers intended to detain Hensley only long enough to confirm the existence of a warrant, or for some longer period; what matters is that the stop and detention that occurred were <page-number citation-index="1" label="235">*235</page-number>in fact no more intrusive than would have been permitted an experienced officer on an objective reading of the flyer.</p>
<p id="b377-5">To be sure, the St. Bernard flyer at issue did not request that other police departments briefly detain Hensley merely to check his identification or confirm the existence of a warrant. Instead, it asked other departments to pick up and hold Hensley for St. Bernard. Our decision today does not suggest that such a detention, whether at the scene or at the Covington police headquarters, would have been justified. Given the distance involved and the time required to identify and communicate with the department that issued the flyer, such a detention might well be so lengthy or intrusive as to exceed the permissible limits of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. See <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S., at 709</a></span>. Nor do we mean to endorse St. Bernard’s request in its flyer for actions that could forseeably violate the Fourth Amendment. We hold only that this flyer, objectively read and supported by a reasonable suspicion on the part of the issuing department, justified the length and intrusiveness of the stop and detention that actually occurred.</p>
<p id="b377-6">When the Covington officers stopped Hensley, they were authorized to take such steps as were reasonably necessary to protect their personal safety and to maintain the status quo during the course of the stop. The Covington officers’ conduct was well within the permissible range in the context of suspects who are reported to be armed and dangerous. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049-1050</a></span> (1983); <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 110-111</a></span> (1977) <em>(per curiam). </em>Having stopped Hensley, the Covington police were entitled to seize evidence revealed in plain view in the course of the lawful stop, to arrest Hensley’s passenger when evidence discovered in plain view gave probable cause to believe the passenger had committed a crime, <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983) (plurality opinion), and subsequently to search the passenger compartment of the car because it was within the passenger’s immediate control. <em>New York </em><page-number citation-index="1" label="236">*236</page-number>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981). Finally, having discovered additional weapons in Hensley’s car during the course of a lawful search, the Covington officers had probable cause to arrest Hensley himself for possession of firearms.</p>
<p id="b378-5">The length of Hensley’s detention from his stop to his arrest on probable cause was brief. A reasonable suspicion on the part of the St. Bernard police underlies and supports their issuance of the flyer. Finally, the stop that occurred was reasonable in objective reliance on the flyer and was not significantly more intrusive than would have been permitted the St. Bernard police. Under these circumstances, the investigatory stop was reasonable under the Fourth Amendment, and the evidence discovered during the stop was admissible.</p>
<p id="b378-6">The judgment of the Court of Appeals is reversed, and the case is remanded for proceedings consistent with this opinion.</p>
<p id="b378-7">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Jacobsen.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Jacobsen"
type: case
citation: "466 U.S. 109 (1984)"
parallel_cite: "104 S. Ct. 1652; 80 L. Ed. 2d 85; 52 U.S.L.W. 4414"
neutral_cite: 1984 U.S. LEXIS 53
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-04-02
docket: 82-1167
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Jacobsen
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/"
  cluster_id: 111143
  opinion_id: 111143
  identity_checked: true
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[Carpenter v. United States]]", "[[United States v. Jones]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-definition", "seizure-definition", "private-search-doctrine", "field-test", "government-action"]
holding: "Defines a property seizure; the Amendment reaches only government action — once a private party exposes contents, a government inspection within that scope invades no remaining privacy (private-search doctrine)."
lake:
  record_id: United States v. Jacobsen
  status: verified
  projected_at: 2026-07-09
---

# United States v. Jacobsen

*466 U.S. 109 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Express employees, following company policy after a forklift damaged a package, opened it and found a tube containing plastic bags of white powder. They notified the DEA and put the items back in the box. A DEA agent arrived, removed the bags from the tube, saw the powder, and conducted a field chemical test that identified it as cocaine. The agent had not obtained a warrant. The Eighth Circuit held the testing was an unlawful search.

## Issue
Whether a government agent's reexamination of a package — and a field chemical test of its contents — after a private party had already opened it and exposed the contents, constitutes a "search" or "seizure" within the meaning of the Fourth Amendment.

## Rule
The Fourth Amendment "protects two types of expectations, one involving 'searches,' the other 'seizures.'" — 466 U.S. at 113. "A 'search' occurs when an expectation of privacy that society is prepared to consider reasonable is infringed. A 'seizure' of property occurs when there is some meaningful interference with an individual's possessory interests in that property." — *Id.* ^pin-113

The Amendment reaches only government action; it is "wholly inapplicable 'to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government.'" — *Id.* ^pin-113a

Where a private search has already occurred, the government's later conduct is measured against it: "The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search." — [*Id.* at 115](https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/#:~:text=The%20additional%20invasions%20of%20respondents%27). ^pin-115

A test that reveals only the presence or absence of contraband is not a search: "A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy." — [*Id.* at 123](https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/#:~:text=A%20chemical%20test%20that%20merely). ^pin-123

## Application
On these facts there was no Fourth Amendment violation. The FedEx employees' opening of the package was private action, so it implicated no constitutional limit "because of their private character." The DEA agent's reexamination did not exceed the scope of that private search — he viewed and handled what the employees had already exposed — so it infringed no remaining expectation of privacy and was not a "search." The field test exceeded the private search but revealed only whether the powder was cocaine, compromising no legitimate privacy interest, and so was not a "search" either. The agent's destruction of a trace of the powder to run the test was a "seizure," but a reasonable one, because it is constitutionally reasonable to seize effects on probable cause to believe they contain contraband. Each step was therefore permissible.

## Conclusion
Neither the reinspection of the package nor the field test was an unreasonable search or seizure; the Eighth Circuit's judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Jacobsen* supplies the canonical Fourth Amendment definitions of "search" and "seizure," the government-action requirement, and the private-search doctrine; it remains good law and is read alongside the trespass/privacy framework of [[Katz v. United States]], [[United States v. Jones]], and [[Carpenter v. United States]].

## Appears on
- [[Private and Foreign Searches]] — *Key — Anchor*

## Sources
- *United States v. Jacobsen*, 466 U.S. 109 (1984) — https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/ — pinpoints: 113, 115, 123.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2ecfd32cdad2e93d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "466 U.S. 109 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 53", "official_citation_present": true, "parallel_cite": "104 S. Ct. 1652; 80 L. Ed. 2d 85; 52 U.S.L.W. 4414", "title": "United States v. Jacobsen", "year": "1984"}}
{"assertion_id": "353f9d2afe624cd4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Defines a property seizure; the Amendment reaches only government action — once a private party exposes contents, a government inspection within that scope invades no remaining privacy (private-search doctrine).", "title": "United States v. Jacobsen"}}
{"assertion_id": "cf3e5ef83b240d93", "dimension": "support", "kind": "home_role", "locator": {"home": "Private and Foreign Searches"}, "payload": {"home": "Private and Foreign Searches", "role": "Key — Anchor", "title": "United States v. Jacobsen"}}
{"assertion_id": "3ba4e24c86c9ad89", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-04-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Jacobsen", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Jacobsen", "varies_by_point": "false"}}
{"assertion_id": "98d22f19f323eeb5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Jacobsen"}}
```

### lake record — United States v. Jacobsen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Jacobsen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Jacobsen",
    "case_name_short": "Jacobsen",
    "case_name_full": "UNITED STATES v. JACOBSEN Et Al.",
    "input_case_name": "United States v. Jacobsen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-04-02",
    "year": 1984,
    "docket": "82-1167",
    "cluster_id": 111143,
    "lead_opinion_id": 111143,
    "sibling_ids": [
      111143,
      9429558,
      9429559,
      9429560
    ],
    "absolute_url": "/opinion/111143/united-states-v-jacobsen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 109",
      "volume": "466",
      "reporter": "U.S.",
      "page": "109",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 1652",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 85",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4414",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4414",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 53",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "53",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 109",
        "volume": "466",
        "reporter": "U.S.",
        "page": "109",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 1652",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 85",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 53",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "53",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4414",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4414",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 109",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 109",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule The Fourth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-113a",
      "page": null,
      "quote": "wholly inapplicable 'to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-115",
      "page": null,
      "quote": "The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search.",
      "star_marker": "115",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8004,
      "fragment": "#:~:text=The%20additional%20invasions%20of%20respondents%27",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-123",
      "page": null,
      "quote": "A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy.",
      "star_marker": "123",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19669,
      "fragment": "#:~:text=A%20chemical%20test%20that%20merely",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Jacobsen",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane1_negative"
      },
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
        "journal_ref": "United States v. Jacobsen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Caballes",
          "cluster_id": 137742,
          "cite": [
            "160 L. Ed. 2d 842",
            "125 S. Ct. 834",
            "543 U.S. 405",
            "2005 U.S. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amores v. State",
          "cluster_id": 1670855,
          "cite": [
            "816 S.W.2d 407",
            "1991 Tex. Crim. App. LEXIS 183",
            "1991 WL 183121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI5MDIwODAwMDAwJnM9NDUwNzU5MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTkmcz0xMDYwNTkzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
        "reviewed": 80,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 80,
        "triage_read": 2,
        "triage_snippet_classified": 78
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
    "indexed_citing_opinions": 1716,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111143,
        "count": 1456,
        "count_source": "search"
      },
      {
        "opinion_id": 9429558,
        "count": 288,
        "count_source": "search"
      },
      {
        "opinion_id": 9429559,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429560,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3226,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-jacobsen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzODAyNjMmcz0xMDU5NzM3MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111143,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 376747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 401057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 406270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 2114544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 2443377,
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
    "date_created": "2026-07-06T00:44:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Jacobsen

```
<div>
<center><b><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U.S. 109</a></span> (1984)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
JACOBSEN ET AL.</h1></center>
<center>No. 82-1167.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 7, 1983</center>
<center>Decided April 2, 1984</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
<p><span class="star-pagination">*110</span> <i>David A. Strauss</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Lee, Assistant Attorney General Jensen, Deputy Solicitor General Frey,</i> and <i>Joel M. Gershowitz.</i></p>
<p><i>Mark W. Peterson</i> argued the cause and filed a brief for respondents.<sup>[*]</sup></p>
<p><i>John Kenneth Zwerling</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p><span class="star-pagination">*111</span> JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>During their examination of a damaged package, the employees of a private freight carrier observed a white powdery substance, originally concealed within eight layers of wrappings. They summoned a federal agent, who removed a trace of the powder, subjected it to a chemical test and determined that it was cocaine. The question presented is whether the Fourth Amendment required the agent to obtain a warrant before he did so.</p>
<p>The relevant facts are not in dispute. Early in the morning of May 1, 1981, a supervisor at the Minneapolis-St. Paul Airport Federal Express office asked the office manager to look at a package that had been damaged and torn by a fork-lift. They then opened the package in order to examine its contents pursuant to a written company policy regarding insurance claims.</p>
<p>The container was an ordinary cardboard box wrapped in brown paper. Inside the box five or six pieces of crumpled newspaper covered a tube about 10 inches long; the tube was made of the silver tape used on basement ducts. The supervisor and office manager cut open the tube, and found a series of four zip-lock plastic bags, the outermost enclosing the other three and the innermost containing about six and a half ounces of white powder. When they observed the white powder in the innermost bag, they notified the Drug Enforcement Administration. Before the first DEA agent arrived, they replaced the plastic bags in the tube and put the tube and the newspapers back into the box.</p>
<p>When the first federal agent arrived, the box, still wrapped in brown paper, but with a hole punched in its side and the top open, was placed on a desk. The agent saw that one end of the tube had been slit open; he removed the four plastic bags from the tube and saw the white powder. He then opened each of the four bags and removed a trace of the <span class="star-pagination">*112</span> white substance with a knife blade. A field test made on the spot identified the substance as cocaine.<sup>[1]</sup></p>
<p>In due course, other agents arrived, made a second field test, rewrapped the package, obtained a warrant to search the place to which it was addressed, executed the warrant, and arrested respondents. After they were indicted for the crime of possessing an illegal substance with intent to distribute, their motion to suppress the evidence on the ground that the warrant was the product of an illegal search and seizure was denied; they were tried and convicted, and appealed. The Court of Appeals reversed. <span class="citation" data-id="9469462"><a href="/opinion/406270/united-states-v-bradley-thomas-jacobsen-and-donna-marie-jacobsen/" aria-description="Citation for case: United States v. Bradley Thomas Jacobsen and Donna Marie...">683 F. 2d 296</a></span> (CA8 1982). It held that the validity of the search warrant depended on the validity of the agents' warrantless test of the white powder,<sup>[2]</sup> that the testing constituted a significant expansion of the earlier private search, and that a warrant was required.</p>
<p>As the Court of Appeals recognized, its decision conflicted with a decision of another Court of Appeals on comparable facts, <i>United States</i> v. <i>Barry,</i> <span class="citation" data-id="9469019"><a href="/opinion/401057/united-states-v-richard-john-barry/" aria-description="Citation for case: United States v. Richard John Barry">673 F. 2d 912</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./459/927/">459 U. S. 927</a></span> (1982).<sup>[3]</sup> For that reason, and because <span class="star-pagination">*113</span> field tests play an important role in the enforcement of the narcotics laws, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./460/1021/">460 U. S. 1021</a></span>.</p>
<p></p>
<h2>I</h2>
<p>The first Clause of the Fourth Amendment provides that the "right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." This text protects two types of expectations, one involving "searches," the other "seizures." A "search" occurs when an expectation of privacy that society is prepared to consider reasonable is infringed.<sup>[4]</sup> A "seizure" of property occurs when there is some meaningful interference with an individual's possessory interests in that property.<sup>[5]</sup> This Court has also consistently construed this protection as proscribing only governmental action; it is wholly inapplicable "to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government or with the participation or knowledge of any governmental official." <i>Walter</i> v. <span class="star-pagination">*114</span> <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 662</a></span> (1980) (BLACKMUN, J., dissenting).<sup>[6]</sup></p>
<p>When the wrapped parcel involved in this case was delivered to the private freight carrier, it was unquestionably an "effect" within the meaning of the Fourth Amendment. Letters and other sealed packages are in the general class of effects in which the public at large has a legitimate expectation of privacy; warrantless searches of such effects are presumptively unreasonable.<sup>[7]</sup> Even when government agents may lawfully seize such a package to prevent loss or destruction of suspected contraband, the Fourth Amendment requires that they obtain a warrant before examining the contents of such a package.<sup>[8]</sup> Such a warrantless search could not be characterized as reasonable simply because, after the official invasion of privacy occurred, contraband is discovered.<sup>[9]</sup> Conversely, in this case the fact that agents of the private carrier independently opened the package and made an examination that might have been impermissible for a government agent <span class="star-pagination">*115</span> cannot render otherwise reasonable official conduct unreasonable. The reasonableness of an official invasion of the citizen's privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred.</p>
<p>The initial invasions of respondents' package were occasioned by private action. Those invasions revealed that the package contained only one significant item, a suspicious looking tape tube. Cutting the end of the tube and extracting its contents revealed a suspicious looking plastic bag of white powder. Whether those invasions were accidental or deliberate,<sup>[10]</sup> and whether they were reasonable or unreasonable, they did not violate the Fourth Amendment because of their private character.</p>
<p>The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search. That standard was adopted by a majority of the Court in <i>Walter</i> v. <i>United States, supra</i><i>.</i> In <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> a private party had opened a misdirected carton, found rolls of motion picture films that appeared to be contraband, and turned the carton over to the Federal Bureau of Investigation. Later, without obtaining a warrant, FBI agents obtained a projector and viewed the films. While there was no single opinion of the Court, a majority did agree on the appropriate analysis of a governmental search which follows on the heels of a private one. Two Justices took the position:</p>
<blockquote>"If a properly authorized official search is limited by the particular terms of its authorization, at least the same kind of strict limitation must be applied to any official <span class="star-pagination">*116</span> use of a private party's invasion of another person's privacy. Even though some circumstances  for example, if the results of the private search are in plain view when materials are turned over to the Government  may justify the Government's reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search. In these cases, the private party had not actually viewed the films. Prior to the Government screening, one could only draw inferences about what was on the films. The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search." <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 657</a></span> (opinion of STEVENS, J., joined by Stewart, J.) (footnote omitted).<sup>[11]</sup></blockquote>
<p>Four additional Justices, while disagreeing with this characterization of the scope of the private search, were also of the view that the legality of the governmental search must be tested by the scope of the antecedent private search.</p>
<blockquote>"`Under these circumstances, since the L'Eggs employees so fully ascertained the nature of the films before contacting the authorities, we find that the FBI's subsequent viewing of the movies on a projector did not "change the nature of the search" and was not an additional search subject to the warrant requirement.' " <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#663" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 663-664</a></span> (BLACKMUN, J., dissenting, joined by BURGER, C. J., and POWELL and REHNQUIST, JJ.) (footnote omitted) (quoting <i>United States</i> v. <i>Sanders,</i> 592 <span class="star-pagination">*117</span> F. 2d 788, 793-794 (CA5 1979) (case below in <i>Walter</i>).<sup>[12]</sup></blockquote>
<p>This standard follows from the analysis applicable when private parties reveal other kinds of private information to the authorities. It is well settled that when an individual reveals private information to another, he assumes the risk that his confidant will reveal that information to the authorities, and if that occurs the Fourth Amendment does not prohibit governmental use of that information. Once frustration of the original expectation of privacy occurs, the Fourth Amendment does not prohibit governmental use of the now nonprivate information: "This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in a third party will not be betrayed." <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 443</a></span> (1976).<sup>[13]</sup> The Fourth Amendment is implicated only if the authorities use information with respect to which the expectation of privacy has not already been frustrated. In such a case the authorities have not relied on what is in effect a private <span class="star-pagination">*118</span> search, and therefore presumptively violate the Fourth Amendment if they act without a warrant.<sup>[14]</sup></p>
<p>In this case, the federal agents' invasions of respondents' privacy involved two steps: first, they removed the tube from the box, the plastic bags from the tube, and a trace of powder from the innermost bag; second, they made a chemical test of the powder. Although we ultimately conclude that both actions were reasonable for essentially the same reason, it is useful to discuss them separately.</p>
<p></p>
<h2>II</h2>
<p>When the first federal agent on the scene initially saw the package, he knew it contained nothing of significance except a tube containing plastic bags and, ultimately, white powder. It is not entirely clear that the powder was visible to him before he removed the tube from the box.<sup>[15]</sup> Even if the white <span class="star-pagination">*119</span> powder was not itself in "plain view" because it was still enclosed in so many containers and covered with papers, there was a virtual certainty that nothing else of significance was in the package and that a manual inspection of the tube and its contents would not tell him anything more than he already had been told. Respondents do not dispute that the Government could utilize the Federal Express employees' testimony concerning the contents of the package. If that is the case, it hardly infringed respondents' privacy for the agents to re-examine the contents of the open package by brushing aside a crumpled newspaper and picking up the tube. The advantage the Government gained thereby was merely avoiding the risk of a flaw in the employees' recollection, rather than in further infringing respondents' privacy. Protecting the risk of misdescription hardly enhances any legitimate privacy interest, and is not protected by the Fourth Amendment.<sup>[16]</sup> Respondents could have no privacy interest in the contents of the package, since it remained unsealed and since the Federal Express employees had just examined the package and had, of their own accord, invited the federal agent to their offices for the express purpose of viewing its contents. The agent's viewing of what a private party had freely made available for his inspection did not violate the Fourth Amendment. <span class="star-pagination">*120</span> See <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971); <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475-476</a></span> (1921).</p>
<p>Similarly, the removal of the plastic bags from the tube and the agent's visual inspection of their contents enabled the agent to learn nothing that had not previously been learned during the private search.<sup>[17]</sup> It infringed no legitimate expectation of privacy and hence was not a "search" within the meaning of the Fourth Amendment.</p>
<p>While the agents' assertion of dominion and control over the package and its contents did constitute a "seizure,"<sup>[18]</sup> that <span class="star-pagination">*121</span> seizure was not unreasonable. The fact that, prior to the field test, respondents' privacy interest in the contents of the package had been largely compromised is highly relevant to the reasonableness of the agents' conduct in this respect. The agents had already learned a great deal about the contents of the package from the Federal Express employees, all of which was consistent with what they could see. The package itself, which had previously been opened, remained unsealed, and the Federal Express employees had invited the agents to examine its contents. Under these circumstances, the package could no longer support any expectation of privacy; it was just like a balloon "the distinctive character [of which] spoke volumes as to its contents  particularly to the trained eye of the officer," <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#743" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 743</a></span> (1983) (plurality opinion); see also <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><i>id.,</i> at 746</a></span> (POWELL, J., concurring in judgment); or the hypothetical gun case in <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span> (1979). Such containers may be seized, at least temporarily, without a warrant.<sup>[19]</sup> Accordingly, since it was apparent that the tube and plastic bags contained contraband and little else, this warrantless seizure was reasonable,<sup>[20]</sup> for it is well settled that it is constitutionally reasonable for law enforcement officials to seize "effects" that cannot support a justifiable expectation <span class="star-pagination">*122</span> of privacy without a warrant, based on probable cause to believe they contain contraband.<sup>[21]</sup></p>
<p></p>
<h2>III</h2>
<p>The question remains whether the additional intrusion occasioned by the field test, which had not been conducted by the Federal Express employees and therefore exceeded the scope of the private search, was an unlawful "search" or "seizure" within the meaning of the Fourth Amendment.</p>
<p>The field test at issue could disclose only one fact previously unknown to the agent  whether or not a suspicious white powder was cocaine. It could tell him nothing more, not even whether the substance was sugar or talcum powder. We must first determine whether this can be considered a "search" subject to the Fourth Amendment  did it infringe an expectation of privacy that society is prepared to consider reasonable?</p>
<p>The concept of an interest in privacy that society is prepared to recognize as reasonable is, by its very nature, critically different from the mere expectation, however well justified, that certain facts will not come to the attention of the authorities.<sup>[22]</sup> Indeed, this distinction underlies the rule that <span class="star-pagination">*123</span> government may utilize information voluntarily disclosed to a governmental informant, despite the criminal's reasonable expectation that his associates would not disclose confidential information to the authorities. See <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White">401 U. S. 745, 751-752</a></span> (1971) (plurality opinion).</p>
<p>A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy. This conclusion is not dependent on the result of any particular test. It is probably safe to assume that virtually all of the tests conducted under circumstances comparable to those disclosed by this record would result in a positive finding; in such cases, no legitimate interest has been compromised. But even if the results are negative  merely disclosing that the substance is something other than cocaine  such a result reveals nothing of special interest. Congress has decided  and there is no question about its power to do so  to treat the interest in "privately" possessing cocaine as illegitimate; thus governmental conduct that can reveal whether a substance is cocaine, and no other arguably "private" fact, compromises no legitimate privacy interest.<sup>[23]</sup></p>
<p>This conclusion is dictated by <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), in which the Court held that subjecting luggage to a "sniff test" by a trained narcotics detection dog was not a "search" within the meaning of the Fourth Amendment:</p>
<blockquote>
<span class="star-pagination">*124</span> "A `canine sniff' by a well-trained narcotics detection dog, however, does not require opening the luggage. It does not expose noncontraband items that otherwise would remain hidden from public view, as does, for example, an officer's rummaging through the contents of the luggage. Thus, the manner in which information is obtained through this investigative technique is much less intrusive than a typical search. Moreover, the sniff discloses only the presence or absence of narcotics, a contraband item. Thus, despite the fact that the sniff tells the authorities something about the contents of the luggage, the information obtained is limited." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>.<sup>[24]</sup></blockquote>
<p>Here, as in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the likelihood that official conduct of the kind disclosed by the record will actually compromise any legitimate interest in privacy seems much too remote to characterize the testing as a search subject to the Fourth Amendment.</p>
<p>We have concluded, in Part II, <i>supra,</i> that the initial "seizure" of the package and its contents was reasonable. Nevertheless, as <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> also holds, a seizure lawful at its inception can nevertheless violate the Fourth Amendment because its manner of execution unreasonably infringes possessory interests protected by the Fourth Amendment's prohibition on "unreasonable seizures."<sup>[25]</sup> Here, the field test did affect respondents' possessory interests protected by the Amendment, since by destroying a quantity of the powder it converted <span class="star-pagination">*125</span> what had been only a temporary deprivation of possessory interests into a permanent one. To assess the reasonableness of this conduct, "[w]e must balance the nature and quality of the intrusion on the individual's Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S., at 703</a></span>.<sup>[26]</sup></p>
<p>Applying this test, we conclude that the destruction of the powder during the course of the field test was reasonable. The law enforcement interests justifying the procedure were substantial; the suspicious nature of the material made it virtually certain that the substance tested was in fact contraband. Conversely, because only a trace amount of material was involved, the loss of which appears to have gone unnoticed by respondents, and since the property had already been lawfully detained, the "seizure" could, at most, have only a <i>de minimis</i> impact on any protected property interest. Cf. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 591-592</a></span> (1974) (plurality opinion) (examination of automobile's tires and taking of paint scrapings was a <i>de minimis</i> invasion of constitutional interests).<sup>[27]</sup> Under these circumstances, the safeguards of a warrant would only minimally advance Fourth Amendment interests. This warrantless "seizure" was reasonable.<sup>[28]</sup></p>
<p><span class="star-pagination">*126</span> In sum, the federal agents did not infringe any constitutionally protected privacy interest that had not already been frustrated as the result of private conduct. To the extent that a protected possessory interest was infringed, the infringement was <i>de minimis</i> and constitutionally reasonable. The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>JUSTICE WHITE, concurring in part and concurring in the judgment.</p>
<p>It is relatively easy for me to concur in the judgment in this case, since in my view the case should be judged on the basis of the Magistrate's finding that, when the first DEA agent arrived, the "tube was in plain view in the box and the bags with the white powder were visible from the end of the tube." App. to Pet. for Cert. 18a. Although this finding was challenged before the District Court, that court found it unnecessary to pass on the issue. <i><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Id.,</a></span></i> at 12a-13a. As I understand its opinion, however, the Court of Appeals accepted the Magistrate's finding: the Federal Express manager "placed the bags back in the tube, leaving them visible from the tube's end, and placed the tube back in the box"; he later gave the box to the DEA agent, who "removed the tube from the open box, took the bags out of the tube, and extracted a sample of the powder." <span class="citation" data-id="9469462"><a href="/opinion/406270/united-states-v-bradley-thomas-jacobsen-and-donna-marie-jacobsen/#297" aria-description="Citation for case: United States v. Bradley Thomas Jacobsen and Donna Marie...">683 F. 2d 296, 297</a></span> (CA8 1982). At the very least, the Court of Appeals assumed that <span class="star-pagination">*127</span> the contraband was in plain view. The Court of Appeals then proceeded to consider whether the federal agent's field test was an illegal extension of the private search, and it invalidated the field test solely for that reason.</p>
<p>Particularly since respondents argue here that whether or not the contraband was in plain view when the federal agent arrived is irrelevant and that the only issue is the validity of the field test, see, <i>e. g.,</i> Brief for Respondents 25, n. 11; Tr. of Oral Arg. 28, I would proceed on the basis that the clear plastic bags were in plain view when the agent arrived and that the agent thus properly observed the suspected contraband. On that basis, I agree with the Court's conclusion in Part III that the Court of Appeals erred in holding that the type of chemical test conducted here violated the Fourth Amendment.</p>
<p>The Court, however, would not read the Court of Appeals' opinion as having accepted the Magistrate's finding. It refuses to assume that the suspected contraband was visible when the first DEA agent arrived on the scene, conducts its own examination of the record, and devotes a major portion of its opinion to a discussion that would be unnecessary if the facts were as found by the Magistrate. The Court holds that even if the bags were not visible when the agent arrived, his removal of the tube from the box and the plastic bags from the tube and his subsequent visual examination of the bags' contents "infringed no legitimate expectation of privacy and hence was not a `search' within the meaning of the Fourth Amendment" because these actions "enabled the agent to learn nothing that had not previously been learned during the private search." <i>Ante,</i> at 120 (footnote omitted). I disagree with the Court's approach for several reasons.</p>
<p>First, as I have already said, respondents have abandoned any attack on the Magistrate's findings; they assert that it is irrelevant whether the suspected contraband was in plain view when the first DEA agent arrived and argue only that the plastic bags could not be opened and their contents tested <span class="star-pagination">*128</span> without a warrant. In short, they challenge only the expansion of the private search, place no reliance on the fact that the plastic bags containing the suspected contraband might not have been left in plain view by the private searchers, and do not contend that their Fourth Amendment rights were violated by the duplication of the private search they alleged in the District Court was necessitated by the condition to which the private searchers returned the package. In these circumstances, it would be the better course for the Court to decide the case on the basis of the facts found by the Magistrate and not rejected by the Court of Appeals, to consider only whether the alleged expansion of the private search by the field test violated the Fourth Amendment, and to leave for another day the question whether federal agents could have duplicated the prior private search had that search not left the contraband in plain view.</p>
<p>Second, if the Court feels that the Magistrate may have erred in concluding that the white powder was in plain view when the first agent arrived and believes that respondents have not abandoned their challenge to the agent's duplication of the prior private search, it nevertheless errs in responding to that challenge. The task of reviewing the Magistrate's findings belongs to the District Court and the Court of Appeals in the first instance. We should request that they perform that function, particularly since if the Magistrate's finding that the contraband was in plain view when the federal agent arrived were to be sustained, there would be no need to address the difficult constitutional question decided today. The better course, therefore, would be to remand the case after rejecting the Court of Appeals' decision invalidating the field test as an illegal expansion of the private search.</p>
<p>Third, if this case must be judged on the basis that the plastic bags and their contents were concealed when the first agent arrived, I disagree with the Court's conclusion that the agent could, without a warrant, uncover or unwrap the tube <span class="star-pagination">*129</span> and remove its contents simply because a private party had previously done so. The remainder of this opinion will address this issue.</p>
<p>The governing principles with respect to the constitutional protection afforded closed containers and packages may be readily discerned from our cases. The Court has consistently rejected proposed distinctions between worthy and unworthy containers and packages, <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#815" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 815, 822-823</a></span> (1982); <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#425" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 425-426</a></span> (1981) (plurality opinion), and has made clear that "the Fourth Amendment provides protection to the owner of every container that conceals its contents from plain view" and does not otherwise unmistakably reveal its contents. <i>United States</i> v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross"><i>Ross, supra,</i> at 822-823</a></span>; see <i>Robbins</i> v. <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#427" aria-description="Citation for case: Robbins v. California"><i>California, supra,</i> at 427-428</a></span> (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764, n. 13</a></span> (1979). Although law enforcement officers may sometimes seize such containers and packages pending issuance of warrants to examine their contents, <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#749" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 749-750</a></span> (1983) (STEVENS, J., concurring in judgment), the mere existence of probable cause to believe that a container or package contains contraband plainly cannot justify a warrantless examination of its contents. <i>Ante,</i> at 114; <i>United States</i> v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross"><i>Ross, supra,</i> at 809-812</a></span>; <i>Arkansas</i> v. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders"><i>Sanders, supra,</i> at 762</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13</a></span>, and n. 8 (1977).</p>
<p>This well-established prohibition of warrantless searches has applied notwithstanding the manner in which the police obtained probable cause. The Court now for the first time sanctions warrantless searches of closed or covered containers or packages whenever probable cause exists as a result of a prior private search. It declares, in fact, that governmental inspections following on the heels of private searches are not searches at all as long as the police do no more than the private parties have already done. In reaching this conclusion, the Court excessively expands our prior decisions recognizing <span class="star-pagination">*130</span> that the Fourth Amendment proscribes only governmental action. <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971).</p>
<p>As the Court observes, the Fourth Amendment "is wholly inapplicable `to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government or with the participation or knowledge of any governmental official.' " <i>Ante,</i> at 113 (quoting <i>Walter</i> v. <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 662</a></span> (1980) (BLACKMUN, J., dissenting)). Where a private party has revealed to the police information he has obtained during a private search or exposed the results of his search to plain view, no Fourth Amendment interest is implicated because the police have done no more than fail to avert their eyes. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#489" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 489</a></span>.</p>
<p>The private-search doctrine thus has much in common with the plain-view doctrine, which is "grounded on the proposition that once police are lawfully in a position <i>to observe an item firsthand,</i> its owner's privacy interest in that item is lost . . . ." <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983) (emphasis added). It also shares many of the doctrinal underpinnings of cases establishing that "the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities," <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 443</a></span> (1976), although the analogy is imperfect since the risks assumed by a person whose belongings are subjected to a private search are not comparable to those assumed by one who voluntarily chooses to reveal his secrets to a companion.</p>
<p>Undoubtedly, the fact that a private party has conducted a search "that might have been impermissible for a government agent cannot render otherwise reasonable official conduct unreasonable." <i>Ante,</i> at 114-115. But the fact that a repository of personal property previously was searched by a private party has never been used to legitimize <i>governmental conduct</i> that otherwise would be subject to challenge under <span class="star-pagination">*131</span> the Fourth Amendment. If government agents are unwilling or unable to rely on information or testimony provided by a private party concerning the results of a private search and that search has not left incriminating evidence in plain view, the agents may wish to duplicate the private search to observe firsthand what the private party has related to them or to examine and seize the suspected contraband the existence of which has been reported. The information provided by the private party clearly would give the agents probable cause to secure a warrant authorizing such actions. Nothing in our previous cases suggests, however, that the agents may proceed to conduct their own search of the same or lesser scope as the private search without first obtaining a warrant. <i>Walter</i> v. <i>United States, supra,</i> at 660-662 (WHITE, J., concurring in part and concurring in judgment).</p>
<p><i>Walter</i> v. <i>United States</i><i>,</i> on which the majority heavily relies in opining that "[t]he additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search," <i>ante,</i> at 115, does not require that conclusion. JUSTICE STEVENS' opinion in <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> does contain language suggesting that the government is free to do all of what was done earlier by the private searchers. But this language was unnecessary to the decision, as JUSTICE STEVENS himself recognized in leaving open the question whether "the Government would have been required to obtain a warrant had the private party been the first to view [the films]," <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States">447 U. S., at 657, n. 9</a></span>, and in emphasizing that "[e]ven though some circumstances  for example, <i>if the results of the private search are in plain view when materials are turned over to the Government</i>  may justify the Government's reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search." <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 657</a></span> (emphasis added). Nor does JUSTICE BLACKMUN's dissent in <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> necessarily support today's holding, for it emphasized that the opened containers <span class="star-pagination">*132</span> turned over to the Government agents "clearly revealed the nature of their contents," <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#663" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 663</a></span>; see <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#665" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 665</a></span>, and the facts of this case, at least as viewed by the Court, do not support such a conclusion.</p>
<p>Today's decision also is not supported by the majority's reference to cases involving the transmission of previously private information to the police by a third party who has been made privy to that information. <i>Ante,</i> at 117-118. The police may, to be sure, use confidences revealed to them by a third party to establish probable cause or for other purposes, and the third party may testify about those confidences at trial without violating the Fourth Amendment. But we have never intimated until now that an individual who reveals that he stores contraband in a particular container or location to an acquaintance who later betrays his confidence has no expectation of privacy in that container or location and that the police may thus search it without a warrant.</p>
<p>That, I believe, is the effect of the Court's opinion. If a private party breaks into a locked suitcase, a locked car, or even a locked house, observes incriminating information, returns the object of his search to its prior locked condition, and then reports his findings to the police, the majority apparently would allow the police to duplicate the prior search on the ground that the private search vitiated the owner's expectation of privacy. As JUSTICE STEVENS has previously observed, this conclusion cannot rest on the proposition that the owner no longer has a subjective expectation of privacy since a person's expectation of privacy cannot be altered by subsequent events of which he was unaware. <i>Walter</i> v. <i>United States, supra,</i> at 659, n. 12.</p>
<p>The majority now ignores an individual's subjective expectations and suggests that "[t]he reasonableness of an official invasion of a citizen's privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred." <i>Ante,</i> at 115. On that view, however, the reasonableness of a particular individual's remaining expectation of privacy should turn entirely on whether the private <span class="star-pagination">*133</span> search left incriminating evidence or contraband in plain view. Cf. <i>Walter</i> v. <i>United States, supra,</i> at 663, 665 (BLACKMUN, J., dissenting). If the evidence or contraband is not in plain view and not in a container that clearly announces its contents at the end of a private search, the government's subsequent examination of the previously searched object necessarily constitutes an independent, governmental search that infringes Fourth Amendment privacy interests. <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S., at 662</a></span> (WHITE, J., concurring in part and concurring in judgment).</p>
<p>The majority opinion is particularly troubling when one considers its logical implications. I would be hard-pressed to distinguish this case, which involves a private search, from (1) one in which the private party's knowledge, later communicated to the government, that a particular container concealed contraband and nothing else arose from his presence at the time the container was sealed; (2) one in which the private party learned that a container concealed contraband and nothing else when it was previously opened in his presence; or (3) one in which the private party knew to a certainty that a container concealed contraband and nothing else as a result of conversations with its owner. In each of these cases, the approach adopted by the Court today would seem to suggest that the owner of the container has no legitimate expectation of privacy in its contents and that government agents opening that container without a warrant on the strength of information provided by the private party would not violate the Fourth Amendment.</p>
<p>Because I cannot accept the majority's novel extension of the private-search doctrine and its implications for the entire concept of legitimate expectations of privacy, I concur only in Part III of its opinion and in the judgment.</p>
<p>JUSTICE BRENNAN, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>This case presents two questions: first whether law enforcement officers may conduct a warrantless search of the <span class="star-pagination">*134</span> contents of a container merely because a private party has previously examined the container's contents and informed the officers of its suspicious nature; and second, whether law enforcement officers may conduct a chemical field test of a substance once the officers have legitimately located the substance. Because I disagree with the Court's treatment of each of these issues, I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>I agree entirely with JUSTICE WHITE that the Court has expanded the reach of the private-search doctrine far beyond its logical bounds. <i>Ante,</i> at 127-133 (WHITE, J., concurring in judgment). It is difficult to understand how respondents can be said to have no expectation of privacy in a closed container simply because a private party has previously opened the container and viewed its contents. I also agree with JUSTICE WHITE, however, that if the private party presents the contents of a container to a law enforcement officer in such a manner that the contents are plainly visible, the officer's visual inspection of the contents does not constitute a "search" within the meaning of the Fourth Amendment. Because the record in this case is unclear on the question whether the contents of respondents' package were plainly visible when the Federal Express employee showed the package to the DEA officer, I would remand the case for further factfinding on this central issue.</p>
<p></p>
<h2>II</h2>
<p>As noted, I am not persuaded that the DEA officer actually came upon respondents' cocaine without violating the Fourth Amendment and, accordingly, I need not address the legality of the chemical field test. Since the Court has done so, however, I too will address the question, assuming, <i>arguendo,</i> that the officer committed neither an unconstitutional search nor an unconstitutional seizure prior to the point at which he took the sample of cocaine out of the plastic bags to conduct the test.</p>
<p></p>
<h2>
<span class="star-pagination">*135</span> A</h2>
<p>I agree that, under the hypothesized circumstances, the field test in this case was not a search within the meaning of the Fourth Amendment for the following reasons: <i>First,</i> the officer came upon the white powder innocently; <i>second,</i> under the hypothesized circumstances, respondents could not have had a reasonable expectation of privacy in the chemical identity of the powder because the DEA agents were already able to identify it as contraband with virtual certainty, <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#750" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 750-751</a></span> (1983) (STEVENS, J., concurring in judgment); and <i>third,</i> the test required the destruction of only a minute quantity of the powder. The Court, however, has reached this conclusion on a much broader ground, relying on two factors alone to support the proposition that the field test was not a search: <i>First,</i> the fact that the test revealed only whether or not the substance was cocaine, without providing any further information; and <i>second,</i> the assumption that an individual does not have a reasonable expectation of privacy in such a fact.</p>
<p>The Court asserts that its "conclusion is dictated by <i>United States</i> v. <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i>" <i>ante,</i> at 123, in which the Court stated that a "canine sniff" of a piece of luggage did not constitute a search because it "is much less intrusive than a typical search," and because it "discloses only the presence or absence of narcotics, a contraband item." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Presumably, the premise of <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was that an individual could not have a reasonable expectation of privacy in the presence or absence of narcotics in his luggage. The validity of the canine sniff in that case, however, was neither briefed by the parties nor addressed by the courts below. Indeed, since the Court ultimately held that the defendant's luggage had been impermissibly seized, its discussion of the question was wholly unnecessary to its judgment. In short, as JUSTICE BLACKMUN pointed out at the time, "[t]he Court [was] certainly in no position to consider all the ramifications of this important issue." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#723" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 723-724</a></span>.</p>
<p><span class="star-pagination">*136</span> Nonetheless, the Court concluded:</p>
<blockquote>"[T]he canine sniff is <i>sui generis.</i> We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here  exposure of respondent's luggage, which was located in a public place, to a trained canine  did not constitute a `search' within the meaning of the Fourth Amendment." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>.</blockquote>
<p>As it turns out, neither the Court's knowledge nor its imagination regarding criminal investigative techniques proved very sophisticated, for within one year we have learned of another investigative procedure that shares with the dog sniff the same defining characteristics that led the Court to suggest that the dog sniff was not a search.</p>
<p>Before continuing along the course that the Court so hastily charted in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> it is only prudent to take this opportunity  in my view, the first real opportunity  to consider the implications of the Court's new Fourth Amendment jurisprudence. Indeed, in light of what these two cases have taught us about contemporary law enforcement methods, it is particularly important that we analyze the basis upon which the Court has redefined the term "search" to exclude a broad class of surveillance techniques. In my view, such an analysis demonstrates that, although the Court's conclusion is correct in this case, its dictum in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was dangerously incorrect. More important, however, the Court's reasoning in both cases is fundamentally misguided and could potentially lead to the development of a doctrine wholly at odds with the principles embodied in the Fourth Amendment.</p>
<p>Because the requirements of the Fourth Amendment apply only to "searches" and "seizures," an investigative technique <span class="star-pagination">*137</span> that falls within neither category need not be reasonable and may be employed without a warrant and without probable cause, regardless of the circumstances surrounding its use. The prohibitions of the Fourth Amendment are not, however, limited to any preconceived conceptions of what constitutes a search or a seizure; instead we must apply the constitutional language to modern developments according to the fundamental principles that the Fourth Amendment embodies. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 356 (1974). Before excluding a class of surveillance techniques from the reach of the Fourth Amendment, therefore, we must be certain that none of the techniques so excluded threatens the areas of personal security and privacy that the Amendment is intended to protect.</p>
<p>What is most startling about the Court's interpretation of the term "search," both in this case and in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> is its exclusive focus on the nature of the information or item sought and revealed through the use of a surveillance technique, rather than on the context in which the information or item is concealed. Combining this approach with the blanket assumption, implicit in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and explicit in this case, that individuals in our society have no reasonable expectation of privacy in the fact that they have contraband in their possession, the Court adopts a general rule that a surveillance technique does not constitute a search if it reveals only whether or not an individual possesses contraband.</p>
<p>It is certainly true that a surveillance technique that identifies only the presence or absence of contraband is less intrusive than a technique that reveals the precise nature of an item regardless of whether it is contraband. But by seizing upon this distinction alone to conclude that the first type of technique, as a general matter, is not a search, the Court has foreclosed any consideration of the circumstances under which the technique is used, and may very well have paved <span class="star-pagination">*138</span> the way for technology to override the limits of law in the area of criminal investigation.</p>
<p>For example, under the Court's analysis in these cases, law enforcement officers could release a trained cocaine-sensitive dog  to paraphrase the California Court of Appeal, a "canine cocaine connoisseur"  to roam the streets at random, alerting the officers to people carrying cocaine. Cf. <i>People</i> v. <i>Evans,</i> <span class="citation" data-id="2114544"><a href="/opinion/2114544/people-v-evans/#932" aria-description="Citation for case: People v. Evans">65 Cal. App. 3d 924, 932</a></span>, <span class="citation" data-id="2114544"><a href="/opinion/2114544/people-v-evans/#440" aria-description="Citation for case: People v. Evans">134 Cal. Rptr. 436, 440</a></span> (1977). Or, if a device were developed that, when aimed at a person, would detect instantaneously whether the person is carrying cocaine, there would be no Fourth Amendment bar, under the Court's approach, to the police setting up such a device on a street corner and scanning all passersby. In fact, the Court's analysis is so unbounded that if a device were developed that could detect, from the outside of a building, the presence of cocaine inside, there would be no constitutional obstacle to the police cruising through a residential neighborhood and using the device to identify all homes in which the drug is present. In short, under the interpretation of the Fourth Amendment first suggested in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and first applied in this case, these surveillance techniques would not constitute searches and therefore could be freely pursued whenever and wherever law enforcement officers desire. Hence, at some point in the future, if the Court stands by the theory it has adopted today, search warrants, probable cause, and even "reasonable suspicion" may very well become notions of the past. Fortunately, we know from precedents such as <i>Katz</i> v. <i>United States, supra</i><i>,</i> overruling the "trespass" doctrine of <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span> (1942), and <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), that this Court ultimately stands ready to prevent this Orwellian world from coming to pass.</p>
<p>Although the Court accepts, as it must, the fundamental proposition that an investigative technique is a search within the meaning of the Fourth Amendment if it intrudes upon a privacy expectation that society considers to be reasonable, <span class="star-pagination">*139</span> <i>ante,</i> at 113, the Court has entirely omitted from its discussion the considerations that have always guided our decisions in this area. In determining whether a reasonable expectation of privacy has been violated, we have always looked to the context in which an item is concealed, not to the identity of the concealed item. Thus in cases involving searches for physical items, the Court has framed its analysis first in terms of the expectation of privacy that normally attends the location of the item and ultimately in terms of the legitimacy of that expectation. In <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), for example, we held that "[n]o less than one who locks the doors of his home against intruders, one who safeguards his possessions [by locking them in a footlocker] is due the protection of the Fourth Amendment . . . ." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 11</a></span>. Our holding was based largely on the observation that, "[b]y placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination." <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></i> The Court made the same point in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 822-823</a></span> (1982), where it held that the "Fourth Amendment provides protection to the owner of every container that conceals its contents from plain view." The fact that a container contains contraband, which indeed it usually does in such cases, has never altered our analysis.</p>
<p>Similarly, in <i>Katz</i> v. <i>United States</i><i>,</i> we held that electronic eavesdropping constituted a search under the Fourth Amendment because it violated a reasonable expectation of privacy. In reaching that conclusion, we focused upon the private context in which the conversation in question took place, stating: "What a person knowingly exposes to the public . . . is not a subject of Fourth Amendment protection. . . . But what he seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351-352</a></span>. Again, the fact that the conversations involved in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> were incriminating did not alter our consideration of the <span class="star-pagination">*140</span> privacy issue. Nor did such a consideration affect our analysis in <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), in which we reaffirmed the principle that the home is private even though it may be used to harbor a fugitive.</p>
<p>In sum, until today this Court has always looked to the manner in which an individual has attempted to preserve the private nature of a particular fact before determining whether there is a reasonable expectation of privacy upon which the government may not intrude without substantial justification. And it has always upheld the general conclusion that searches constitute at least "those more extensive intrusions that significantly jeopardize the sense of security which is the paramount concern of Fourth Amendment liberties." <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S. 745, 786</a></span> (1971) (Harlan, J., dissenting).</p>
<p>Nonetheless, adopting the suggestion in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the Court has veered away from this sound and well-settled approach and has focused instead solely on the product of the would-be search. In so doing, the Court has ignored the fundamental principle that "[a] search prosecuted in violation of the Constitution is not made lawful by what it brings to light." <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927). The unfortunate product of this departure from precedent is an undifferentiated rule allowing law enforcement officers free rein in utilizing a potentially broad range of surveillance techniques that reveal only whether or not contraband is present in a particular location. The Court's new rule has rendered irrelevant the circumstances surrounding the use of the technique, the accuracy of the technique, and the privacy interest upon which it intrudes. Furthermore, the Court's rule leaves no room to consider whether the surveillance technique is employed randomly or selectively, a consideration that surely implicates Fourth Amendment concerns. See 2 W. LaFave, Search and Seizure § 2.2(f) (1978). Although a technique that reveals only the presence or absence of illegal <span class="star-pagination">*141</span> activity intrudes less into the private life of an individual under investigation than more conventional techniques, the fact remains that such a technique does intrude. In my view, when the investigation intrudes upon a domain over which the individual has a reasonable expectation of privacy, such as his home or a private container, it is plainly a search within the meaning of the Fourth Amendment. Surely it cannot be that the individual's reasonable expectation of privacy dissipates simply because a sophisticated surveillance technique is employed.</p>
<p>This is not to say that the limited nature of the intrusion has no bearing on the general Fourth Amendment inquiry. Although there are very few exceptions to the general rule that warrantless searches are presumptively unreasonable, the isolated exceptions that do exist are based on a "balancing [of] the need to search against the invasion which the search entails." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967). Hence it may be, for example, that the limited intrusion effected by a given surveillance technique renders the employment of the technique, under particular circumstances, a "reasonable" search under the Fourth Amendment. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#723" aria-description="Citation for case: United States v. Place">462 U. S., at 723</a></span> (BLACKMUN, J., concurring in judgment) ("a dog sniff may be a search, but a minimally intrusive one that could be justified in this situation under <i>Terry</i>"). At least under this wellsettled approach, the Fourth Amendment inquiry would be broad enough to allow consideration of the method by which a surveillance technique is employed as well as the circumstances attending its use. More important, however, it is only under this approach that law enforcement procedures, like those involved in this case and in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> may continue to be governed by the safeguards of the Fourth Amendment.</p>
<p></p>
<h2>B</h2>
<p>In sum, the question whether the employment of a particular surveillance technique constitutes a search depends on <span class="star-pagination">*142</span> whether the technique intrudes upon a reasonable expectation of privacy. This inquiry, in turn, depends primarily on the private nature of the area or item subjected to the intrusion. In cases involving techniques used to locate or identify a physical item, the manner in which a person has attempted to shield the item's existence or identity from public scrutiny will usually be the key to determining whether a reasonable expectation of privacy has been violated. Accordingly, the use of techniques like the dog sniff at issue in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> constitutes a search whenever the police employ such techniques to secure any information about an item that is concealed in a container that we are prepared to view as supporting a reasonable expectation of privacy. The same would be true if a more technologically sophisticated method were developed to take the place of the dog.</p>
<p>In this case, the chemical field test was used to determine whether certain white powder was cocaine. Upon visual inspection of the powder in isolation, one could not identify it as cocaine. In the abstract, therefore, it is possible that an individual could keep the powder in such a way as to preserve a reasonable expectation of privacy in its identity. For instance, it might be kept in a transparent pharmaceutical vial and disguised as legitimate medicine. Under those circumstances, the use of a chemical field test would constitute a search. However, in this case, as hypothesized above, see <i>supra,</i> at 134, the context in which the powder was found could not support a reasonable expectation of privacy. In particular, the substance was found in four plastic bags, which had been inside a tube wrapped with tape and sent to respondents via Federal Express. It was essentially inconceivable that a legal substance would be packaged in this manner for transport by a common carrier. Thus, viewing the powder as they did at the offices of Federal Express, the DEA agent could identify it with "virtual certainty"; it was essentially as though the chemical identity of the powder was <span class="star-pagination">*143</span> plainly visible. See <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#751" aria-description="Citation for case: Texas v. Brown">460 U. S., at 751</a></span> (STEVENS, J., concurring in judgment). Under these circumstances, therefore, respondents had no reasonable expectation of privacy in the identity of the powder, and the use of the chemical field test did not constitute a "search" violative of the Fourth Amendment.</p>
<h2>NOTES</h2>
<p>[*]  <i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak, Howard G. Berringer, David Crump, Daniel B. Hales, William B. Randall,</i> and <i>Evelle J. Younger</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  As the test is described in the evidence, it involved the use of three test tubes. When a substance containing cocaine is placed in one test tube after another, it will cause liquids to take on a certain sequence of colors. Such a test discloses whether or not the substance is cocaine, but there is no evidence that it would identify any other substances.</p>
<p>[2]  The Court of Appeals did not hold that the facts would not have justified the issuance of a warrant without reference to the test results; the court merely held that the facts recited in the warrant application, which relied almost entirely on the results of the field tests, would not support the issuance of the warrant if the field test was itself unlawful. " `It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention.' " <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#413" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 413, n. 3</a></span> (1969) (emphasis in original) (quoting <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 109, n. 1</a></span> (1964)). See <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 238-239</a></span> (1983).</p>
<p>[3]  See also <i>People</i> v. <i>Adler,</i> 50 N. Y. 2d 730, <span class="citation" data-id="5533133"><a href="/opinion/5684320/people-v-adler/" aria-description="Citation for case: People v. Adler">409 N. E. 2d 888</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1014/">449 U. S. 1014</a></span> (1980); cf. <i>United States</i> v. <i>Andrews,</i> <span class="citation" data-id="9466632"><a href="/opinion/376747/united-states-v-john-allen-andrews/" aria-description="Citation for case: United States v. John Allen Andrews">618 F. 2d 646</a></span> (CA10) (upholding warrantless field test without discussion), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/824/">449 U. S. 824</a></span> (1980).</p>
<p>[4]  See <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983); <i>United States</i> v. <i>Knotts,</i> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#280" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 280-281</a></span> (1983); <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-741</a></span> (1979); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968).</p>
<p>[5]  See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#716" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 716</a></span> (BRENNAN, J., concurring in result); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (STEVENS, J., concurring in judgment); see also <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13-14, n. 8</a></span> (1977); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906). While the concept of a "seizure" of property is not much discussed in our cases, this definition follows from our oft-repeated definition of the "seizure" of a person within the meaning of the Fourth Amendment  meaningful interference, however brief, with an individual's freedom of movement. See <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#696" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 696</a></span> (1981); <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span>, n. (1980) <i>(per curiam); </i><i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#551" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 551-554</a></span> (1980) (opinion of Stewart, J.); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50</a></span> (1979); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16, 19, n. 16</a></span>.</p>
<p>[6]  See <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#656" aria-description="Citation for case: Walter v. United States">447 U. S., at 656</a></span> (opinion of STEVENS, J.); <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#660" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 660-661</a></span> (WHITE, J., concurring in part and concurring in judgment); <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#455" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 455-456, n. 31</a></span> (1976); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971); <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921).</p>
<p>[7]  <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 10</a></span> (1977); <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#251" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249, 251</a></span> (1970); <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878); see also <i>Walter,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#654" aria-description="Citation for case: Walter v. United States">447 U. S., at 654-655</a></span> (opinion of STEVENS, J.).</p>
<p>[8]  See, <i>e. g., </i><i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S., at 701</a></span>; <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 809-812</a></span> (1982); <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 426</a></span> (1981) (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 762</a></span> (1979); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>, and n. 8; <i>United States</i> v. <i>Van <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">Leeuwen, supra</a></span></i><i>.</i> There is, of course, a well-recognized exception for customs searches; but that exception is not involved in this case.</p>
<p>[9]  See <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#567" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 567, n. 11</a></span> (1971); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 484</a></span> (1963); <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960); <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span> (1959); <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#312" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 312</a></span> (1958); <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span> (1948); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927).</p>
<p>[10]  A post-trial affidavit indicates that an agent of Federal Express may have opened the package because he was suspicious about its contents, and not because of damage from a forklift. However, the lower courts found no governmental involvement in the private search, a finding not challenged by respondents. The affidavit thus is of no relevance to the issue we decide.</p>
<p>[11]  See also <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#658" aria-description="Citation for case: Walter v. United States">447 U. S., at 658-659</a></span> (footnotes omitted) ("The fact that the cartons were unexpectedly opened by a third party before the shipment was delivered to its intended consignee does not alter the consignor's legitimate expectation of privacy. The private search merely frustrated that expectation in part. It did not simply strip the remaining unfrustrated portion of that expectation of all Fourth Amendment protection").</p>
<p>[12]  In <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span>,</i> a majority of the Court found a violation of the Fourth Amendment. For present purposes, the disagreement between the majority and the dissenters in that case with respect to the comparison between the private search and the official search is less significant than the agreement on the standard to be applied in evaluating the relationship between the two searches.</p>
<p>[13]  See <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#743" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 743-744</a></span> (1979); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#749" aria-description="Citation for case: United States v. White">401 U. S. 745, 749-753</a></span> (1971) (plurality opinion); <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#326" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 326-331</a></span> (1966); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#300" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 300-303</a></span> (1966); <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> (1966); <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#437" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 437-439</a></span> (1963); <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#753" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 753-754</a></span> (1952). See also <i>United States</i> v. <i>Henry,</i> <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#272" aria-description="Citation for case: United States v. Henry">447 U. S. 264, 272</a></span> (1980); <i>United States</i> v. <i>Caceres,</i> <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#744" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 744, 750-751</a></span> (1979).</p>
<p>[14]  See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967); <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961).</p>
<p>[15]  Daniel Stegemoller, the Federal Express office manager, testified at the suppression hearing that the white substance was not visible without reentering the package at the time the first agent arrived. App. 42-43, 58. As JUSTICE WHITE points out, the Magistrate found that the "tube was in plain view in the box and the bags with the white powder were visible from the end of the tube." App. to Pet. for Cert. 18a. The bags were, however, only visible if one picked up the tube and peered inside through a small aperture; even then, what was visible was only the translucent bag that contained the white powder. The powder itself was barely visible, and surely was not so plainly in view that the agents did "no more than fail to avert their eyes," <i>post,</i> at 130. In any event, respondents filed objections to the Magistrate's report with the District Court. The District Court declined to resolve respondents' objections, ruling that fact immaterial and assuming for purposes of its decision "that the newspaper in the box covered the gray tube and that neither the gray tube nor the contraband could be seen when the box was turned over to the . . . DEA agents." App. to Pet. for Cert. 12a-13a. At trial, the federal agent first on the scene testified that the powder was not visible until after he pulled the plastic bags out of the tube. App. 71-72. Respondents continue to argue this case on the assumption that the Magistrate's report is incorrect. Brief for Respondents 2-3. As our discussion will make clear, we agree with the District Court that it does not matter whether the loose pieces of newspaper covered the tube at the time the agent first saw the box.</p>
<p>[16]  See <i>United States</i> v. <i>Caceres,</i> <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#750" aria-description="Citation for case: United States v. Caceres">440 U. S., at 750-751</a></span>; <i>United States</i> v. <i>White,</i> 401 U. S., at 749-753 (plurality opinion); <i>Osborn</i> v. <i>United States,</i> 385 U. S., at 326-331; <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#753" aria-description="Citation for case: On Lee v. United States">343 U. S., at 753-754</a></span>. For example, in <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963), the Court wrote: "Stripped to its essentials, petitioner's argument amounts to saying that he has a constitutional right to rely on possible flaws in the agent's memory, or to challenge the agent's credibility without being beset by corroborating evidence . . . . For no other argument can justify excluding an accurate version of a conversation that the agent could testify to from memory. We think the risk that petitioner took in offering a bribe to Davis fairly included the risk that the offer would be accurately reproduced in court . . . ." <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States"><i>Id.,</i> at 439</a></span> (footnote omitted).</p>
<p>[17]  We reject JUSTICE WHITE's suggestion that this case is indistinguishable from one in which the police simply learn from a private party that a container contains contraband, seize it from its owner, and conduct a warrantless search which, as JUSTICE WHITE properly observes, would be unconstitutional. Here, the Federal Express employees who were lawfully in possession of the package invited the agent to examine its contents; the governmental conduct was made possible only because private parties had compromised the integrity of this container. JUSTICE WHITE would have this case turn on the fortuity of whether the Federal Express employees placed the tube back into the box. But in the context of their previous examination of the package, their communication of what they had learned to the agent, and their offer to have the agent inspect it, that act surely could not create any privacy interest with respect to the package that would not otherwise exist. See <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S., at 771-772</a></span>. Thus the precise character of the white powder's visibility to the naked eye is far less significant than the facts that the container could no longer support any expectation of privacy, and that it was virtually certain that it contained nothing but contraband. Contrary to JUSTICE WHITE's suggestion, we do not "sanctio[n] warrantless searches of closed or covered containers or packages whenever probable cause exists as a result of a prior private search." <i>Post,</i> at 129. A container which can support a reasonable expectation of privacy may not be searched, even on probable cause, without a warrant. See <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S., at 809-812</a></span>; <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S., at 426-427</a></span> (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764-765</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977).</p>
<p>[18]  Both the Magistrate and the District Court found that the agents took custody of the package from Federal Express after they arrived. Although respondents had entrusted possession of the items to Federal Express, the decision by governmental authorities to exert dominion and control over the package for their own purposes clearly constituted a "seizure," though not necessarily an unreasonable one. See <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970). Indeed, this is one thing on which the entire Court appeared to agree in <i>Walter</i> v. <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">447 U. S. 649</a></span> (1980).</p>
<p>[19]  See also <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S., at 822-823</a></span>; <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#428" aria-description="Citation for case: Robbins v. California">453 U. S., at 428</a></span> (plurality opinion).</p>
<p>[20]  Respondents concede that the agents had probable cause to believe the package contained contraband. Therefore we need not decide whether the agents could have seized the package based on something less than probable cause. Some seizures can be justified by an articulable suspicion of criminal activity. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983).</p>
<p>[21]  See <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S., at 701-702</a></span>; <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#741" aria-description="Citation for case: Texas v. Brown">460 U. S., at 741-742</a></span> (plurality opinion); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#748" aria-description="Citation for case: Texas v. Brown"><i>id.,</i> at 748</a></span> (STEVENS, J., concurring in judgment); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980); <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977); <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968) <i>(per curiam)</i><i>.</i></p>
<p>[22]  "Obviously, however, a `legitimate' expectation of privacy by definition means more than a subjective expectation of not being discovered. A burglar plying his trade in a summer cabin during the off season may have a thoroughly justified subjective expectation of privacy, but it is not one which the law recognizes as `legitimate.' His presence, in the words of <i>Jones</i> [v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960)], is `wrongful'; his expectation [of privacy] is not `one that society is prepared to recognize as "reasonable." ' <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring). And it would, of course, be merely tautological to fall back on the notion that those expectations of privacy which are legitimate depend primarily on cases deciding exclusionary-rule issues in criminal cases. Legitimation of expectations of privacy by law must have a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society." <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143-144, n. 12</a></span> (1978). See also <i>United States</i> v. <i>Knotts,</i> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983) (use of a beeper to track car's movements infringed no reasonable expectation of privacy); <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979) (use of a pen register to record phone numbers dialed infringed no reasonable expectation of privacy).</p>
<p>[23]  See Loewy, The Fourth Amendment as a Device for Protecting the Innocent, <span class="citation no-link">81 Mich. L. Rev. 1229</span> (1983). Our discussion, of course, is confined to possession of contraband. It is not necessarily the case that the purely "private" possession of an article that cannot be distributed in commerce is itself illegitimate. See <i>Stanley</i> v. <i>Georgia,</i> <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557</a></span> (1969).</p>
<p>[24]  Respondents attempt to distinguish <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> arguing that it involved no physical invasion of Place's effects, unlike the conduct at issue here. However, as the quotation makes clear, the <i>reason</i> this did not intrude upon any legitimate privacy interest was that the governmental conduct could reveal nothing about noncontraband items. That rationale is fully applicable here.</p>
<p>[25]  In <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the Court held that while the initial seizure of luggage for the purpose of subjecting it to a "dog sniff" test was reasonable, the seizure became unreasonable because its length unduly intruded upon constitutionally protected interests. See <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 707-710</a></span>.</p>
<p>[26]  See, <i>e. g., </i><i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1046" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1046-1047</a></span> (1983); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20-21</a></span>; <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967).</p>
<p>[27]  In fact, respondents do not contend that the amount of material tested was large enough to make it possible for them to have detected its loss. The only description in the record of the amount of cocaine seized is that "[i]t was a trace amount." App. 75.</p>
<p>[28]  See <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#296" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 296</a></span> (1973) (warrantless search and seizure limited to scraping suspect's fingernails justified even when full search may not be). Cf. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S., at 703-706</a></span> (approving brief warrantless seizure of luggage for purposes of "sniff test" based on its minimal intrusiveness and reasonable belief that the luggage contained contraband); <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#252" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S., at 252-253</a></span> (detention of package on reasonable suspicion was justified since detention infringed no "significant Fourth Amendment interest"). Of course, where more substantial invasions of constitutionally protected interests are involved, a warrantless search or seizure is unreasonable in the absence of exigent circumstances. See, <i>e. g., </i><i>Steagald</i> v. <i>United States,</i> <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). We do not suggest, however, that any seizure of a small amount of material is necessarily reasonable. An agent's arbitrary decision to take the "white powder" he finds in a neighbor's sugar bowl, or his medicine cabinet, and subject it to a field test for cocaine, might well work an unreasonable seizure.</p>

</div>
```

---
