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

## GROUP: content/cases/G. M. Leasing Corp. v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: G. M. Leasing Corp. v. United States
type: case
citation: "429 U.S. 338 (1977)"
parallel_cite: "97 S. Ct. 619; 50 L. Ed. 2d 530; 39 A.F.T.R.2d (RIA) 475"
neutral_cite: 1977 U.S. LEXIS 33
court: U.S.
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-12
docket: 75-235
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
  opinion_url: "https://www.courtlistener.com/opinion/109579/g-m-leasing-corp-v-united-states/"
  cluster_id: 109579
  opinion_id: null
  identity_checked: true
lake:
  record_id: G. M. Leasing Corp. v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Curtilage]]"
    role: Key
related:
  - "[[Curtilage]]"
  - "[[The Warrant Requirement]]"
  - "[[Florida v. White]]"
  - "[[Camara v. Municipal Court]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - commercial-premises
  - tax-levy
holding: "Warrantless seizure of a taxpayer's automobiles from public streets and lots to satisfy a tax levy involves no Fourth Amendment search and needs no warrant, but a warrantless entry into the taxpayer's private business offices to seize books and records is an unreasonable intrusion the Fourth Amendment forbids absent a warrant."
---

# G. M. Leasing Corp. v. United States

*429 U.S. 338 (1977)* (No. 75-235) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109579 → lead opinion 109579; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
After assessing jeopardy income-tax deficiencies against Norman Chreske, IRS agents — acting without a warrant — seized several automobiles held in the name of G. M. Leasing Corp. (found to be Chreske's alter ego) from public streets and parking lots to satisfy the levy, and separately entered the corporation's business offices and seized books and records. G. M. Leasing sued, contending that both the seizure of the cars and the entry into and search of its offices violated the Fourth Amendment.

## Issue
Whether the Fourth Amendment required a warrant (1) to seize the taxpayer's automobiles from public places to enforce a tax levy, and (2) to enter the corporation's private business offices to seize its books and records.

## Rule
The Court analyzed the two intrusions separately. As to the vehicles, a levy on property located in public places is not a search and needs no warrant: "The seizures of the automobiles in this case took place on public streets, parking lots, or other open places, and did not involve any invasion of privacy." — 429 U.S. at 351. ^pin-351

As to the offices, the result was different: "The seizure of the books and records, however, involved intrusion into the privacy of petitioner's offices." — 429 U.S. at 352. ^pin-352

Private commercial premises fall within the Fourth Amendment's protection, and the settled rule is that "except in certain carefully defined classes of cases, a search of private property without proper consent is 'unreasonable' unless it has been authorized by a valid search warrant" — a requirement the Government's tax-collection purpose did not dispense with.

## Application
Because the automobiles were seized from public streets and lots, the levy invaded no privacy interest and required no warrant. But the agents' forced, warrantless entry into the corporation's offices to search for and seize its records intruded on a constitutionally protected private space. Nothing about the tax assessment or the summary-levy power justified that entry without a warrant, so the office intrusion violated the Fourth Amendment even though the underlying levy was lawful.

## Conclusion
The judgment was **affirmed in part and reversed in part**, and the case **[[Reading and Citing Cases#on-remand|remanded]]**: the warrantless seizure of the automobiles was upheld, while the warrantless entry into the offices and seizure of the books and records was held unconstitutional. Blackmun, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *G. M. Leasing* remains a foundational statement that business premises enjoy Fourth Amendment protection and that an administrative or tax-collection objective does not relax the warrant requirement for entering them — while property seized from public places to satisfy a levy implicates no privacy interest at all.

## Appears on
- [[Curtilage]] — *Key*

## Sources
- [*G. M. Leasing Corp. v. United States*, 429 U.S. 338 (1977)](https://www.courtlistener.com/opinion/109579/g-m-leasing-corp-v-united-states/) — pinpoint: 351 (public-place seizure, no invasion of privacy), 352 (intrusion into the privacy of the offices); Opinion of the Court, Blackmun, J.; quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "40fe42c1d488581f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "429 U.S. 338 (1977)", "court": "U.S.", "neutral_cite": "1977 U.S. LEXIS 33", "official_citation_present": true, "parallel_cite": "97 S. Ct. 619; 50 L. Ed. 2d 530; 39 A.F.T.R.2d (RIA) 475", "title": "G. M. Leasing Corp. v. United States", "year": "1977"}}
{"assertion_id": "25493f8ce5c3c35a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Warrantless seizure of a taxpayer's automobiles from public streets and lots to satisfy a tax levy involves no Fourth Amendment search and needs no warrant, but a warrantless entry into the taxpayer's private business offices to seize books and records is an unreasonable intrusion the Fourth Amendment forbids absent a warrant.", "title": "G. M. Leasing Corp. v. United States"}}
{"assertion_id": "64df3aad46ab71df", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Key", "title": "G. M. Leasing Corp. v. United States"}}
{"assertion_id": "06befd5db4b8e5b6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "G. M. Leasing Corp. v. United States", "varies_by_point": "false"}}
{"assertion_id": "9df32788fcf3f706", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "G. M. Leasing Corp. v. United States"}}
```

### lake record — G. M. Leasing Corp. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "G. M. Leasing Corp. v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "G. M. Leasing Corp. v. United States",
    "case_name_short": "GM Leasing",
    "case_name_full": "G. M. LEASING CORP. Et Al. v. UNITED STATES Et Al.",
    "input_case_name": "G. M. Leasing Corp. v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-12",
    "year": 1977,
    "docket": "75-235",
    "cluster_id": 109579,
    "lead_opinion_id": 9426638,
    "sibling_ids": [],
    "absolute_url": "/opinion/109579/g-m-leasing-corp-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 338",
      "volume": "429",
      "reporter": "U.S.",
      "page": "338",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 619",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 530",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 A.F.T.R.2d (RIA) 475",
        "volume": "39",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "475",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 33",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 338",
        "volume": "429",
        "reporter": "U.S.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 619",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 530",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 33",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "33",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "39 A.F.T.R.2d (RIA) 475",
        "volume": "39",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "475",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 338",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 338",
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
    "date_created": "2026-07-07T13:25:41Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:25:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "g-m-leasing-corp-v-united-states--109579",
      "to_record_id": "G. M. Leasing Corp. v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — G. M. Leasing Corp. v. United States

```
<opinion type="majority">
<author id="b490-7">Mr. Justice Blackmun</author>
<p id="AUy3">delivered the opinion of the Court.</p>
<p id="b490-8">We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1031/">423 U. S. 1031</a></span> (1975), limited to the Fourth Amendment issue arising in the context of seizures of property in partial satisfaction of income tax assessments.<footnotemark>1</footnotemark></p>
<p id="b490-9">I</p>
<p id="b490-10">Petitioner G. M. Leasing Corp. is a Utah corporation organized in April 1972; among its stated business purposes is the leasing of automobiles. George I. Norman, Jr., although apparently not an incorporator, officer, or director of petitioner, was its general manager.</p>
<p id="b490-11">In 1971 Norman was tried and convicted in the United States District Court for the District of Colorado on two counts of aiding and abetting a misapplication of funds from a federally insured bank, in violation of 18 U. S. C. § § 2 and 656. He was sentenced to two concurrent two-year terms of imprisonment. On appeal, his conviction was affirmed. <em>United States </em>v. <em>Cooper, </em><span class="citation" data-id="304880"><a href="/opinion/304880/united-states-v-donald-s-cooper/#651" aria-description="Citation for case: United States v. Donald S. Cooper">464 F. 2d 648, 651-652</a></span> (CA10 1972). This Court denied certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./409/1107/">409 U. S. 1107</a></span> (1973).</p>
<p id="b491-4"><page-number citation-index="1" label="341">*341</page-number>Norman and his wife, on November 15, 1971,<footnotemark>2</footnotemark> filed a joint income tax Form 1040 for the calendar year 1970 on which, apart from their names, address, social security numbers, occupations, and dependents, they indicated only that their tax for that year, “ [estimated,” was $280,000. The sum of $289,800 was transmitted when the form was filed and was placed by the Internal Revenue Service in a suspense account for future credit. Apart from the naked figure of estimated tax, the return contained no information as to income or deductions. App. 94.</p>
<p id="b491-5">The Normans also sought and were granted an extension of time within which to file their return for the calendar year 1971. A check for $405,125 was given to the Service on April 15, 1972, for application on their 1971 tax. This check evidently was dishonored. Although further extensions of time were granted, neither of the Normans ever filed a 1971 return.</p>
<p id="b491-6">In October 1972, after Norman’s conviction was affirmed by the Tenth Circuit, the Service assigned the Norman account for 1970 and 1971 to Agent P. J. Clayton for investigation. Mr. Clayton, however, took no immediate action. <em>Id., </em>at 66; Tr. of Oral Arg. 24 — 25.</p>
<p id="b491-7">In March 1973, after Norman’s petition for a writ of certiorari had been denied, and after his petition for rehearing had also been denied, <span class="citation multiple-matches"><a href="/c/U.%20S./410/959/">410 U. S. 959</a></span> (1973), he surrendered to the United States Marshal for the serving of his sentence. By a ruse, however, he immediately disappeared. Tr. of Oral Arg. 6. Norman thereupon became a fugitive from justice; he was still one at the time of the oral argument. App. 15; Brief for Petitioners 5; Tr. of Oral Arg. 5-6.</p>
<p id="b491-8">Upon Norman’s becoming a fugitive, the Service activated its investigation. On March 19, it determined deficiencies in Norman’s income tax liability for 1970 and 1971 in the <page-number citation-index="1" label="342">*342</page-number>amounts of $406,099.34 and $545,310.59, respectively.<footnotemark>3</footnotemark> App. 95. These were based solely on information from third parties concerning the amount of stock sales Norman made through various brokerage houses. <em>Id., </em>at 30, 67.<footnotemark>4</footnotemark> Because of Norman’s failure to file appropriate returns and because of his fugitive status, collection of the taxes as so determined was regarded by the Service as in jeopardy; the deficiencies, therefore, were assessed forthwith pursuant to the authority granted by § 6861 (a) of the Internal Revenue Code of 1954, <span class="citation no-link">26 U. S. C. § 6861</span> (a).<footnotemark>5</footnotemark></p>
<p id="b492-5">The following day revenue agents called at the Norman residence in Salt Lake City to endeavor to collect the taxes. <page-number citation-index="1" label="343">*343</page-number>Mrs. Norman answered the door. The agents informed her of the jeopardy assessments and demanded payment. No payment was forthcoming, and Mrs. Norman suggested that the agents get in touch with her attorney. App. 56. Thereafter, pursuant to their authority under § 6331 of the Code, the agents filed notice of tax liens with the Salt Lake County Recorder’s Office and levied on a bank account of Norman. App. 95, 58.</p>
<p id="b493-5">While the agents were at the Norman residence, they observed automobiles parked in the driveway. Later, upon checking with the Utah Motor Vehicle Division, they learned that these vehicles were registered in the name of petitioner or in the name of another corporation owned by Norman, and that no automobile was registered in Norman’s name or in that of his wife. <em>Id., </em>at' 73-74. They also learned that petitioner had no license to conduct business within Salt Lake County and had no telephone listing. <em>Id., </em>at 74. It was further ascertained that, pursuant to the request of the Utah Department of Employment Security, petitioner had filed a Status Report. That report described the corporation’s principal business activity as “Leasing Luxury Automobiles, Boats, etc.” It recited that the corporation’s “average number of employees” was zero and that it had paid no wages while it was in existence during the last three quarters of 1972 or thus far in 1973. <em>Id., </em>at 91-92. On its Utah Sales and Use Tax Return for the second quarter of 1972, the corporation reported no sales. <em>Id., </em>at 93. The agents regarded the automobiles seen at the Norman residence as “show” or “collector” cars and not the type “that would normally be used in a leasing business.” <em>Id., </em>at 74.</p>
<p id="b493-6">All these facts suggested to the agents that petitioner corporation was not engaged in any business activity but, instead, was Norman’s alter ego and a repository of at least some of his personal assets. The agents consulted with the Service’s Regional Counsel. With his concurrence, <page-number citation-index="1" label="344">*344</page-number>the conclusion was drawn that the assets of the corporation actually belonged to Norman. Accordingly, the decision was made to levy upon and seize automobiles titled in petitioner’s name in partial satisfaction of the assessments against Norman. <em>Id., </em>at 75-76.</p>
<p id="b494-5">On or about March 21, two days after the jeopardy assessments, revenue officers, without a warrant, seized several automobiles. Among them were a 1972 Stutz, a Rolls Royce Phantom V, a 1930 Rolls Royce Phantom I, two 1971 Stutzes, and a Jaguar. Three were taken at two different locations in Salt Lake City; two at the Century Plaza parking lot in Los Angeles, Cal.; and one near Norman’s residence in Salt Lake City. <em>Id., </em>at 121, 129; Tr. of Oral Arg. 13-14. None of the ears was on property in which petitioner had an interest. All were registered in petitioner’s name. App. 75-76. The officers left a Chevrolet and 'a station wagon for the personal use of Mrs. Norman and her family.<footnotemark>6</footnotemark> <em>Id., a.t 58.</em></p>
<p id="b494-6">Also on March 21, revenue officers went to petitioner’s office'in Salt Lake County to levy on property subject to seizure, including the building itself. <em>Id., </em>at 19. They had information that one, and possibly two, luxury automobiles might be there. Upon learning that a car was in the garage on the premises, they telephoned their superior, Bert Apple-gate, and asked him to come out to assist. <em>Id., </em>at 77-79. The premises consisted of a cottage-type building and the garage. When Applegate arrived, a locksmith was there. He already had removed the lock from the garage door <page-number citation-index="1" label="345">*345</page-number>at the direction of the officers. A Stutz automobile was inside. The locksmith also had removed the lock on the cottage’s rear door. <em>Id., </em>at 80-81.</p>
<p id="b495-5">Applegate entered the cottage. He observed that its outward appearance was such that it could be a residence. He noticed a kitchen. He instructed the officers not to proceed with the seizure of any property there until the status of the cottage could be confirmed.<footnotemark>7</footnotemark> <em>Id., </em>at 81, 23-24. The officers then left the cottage without taking anything, and its lock was replaced. <em>Id., </em>at 82.</p>
<p id="b495-6">While the officers were in the cottage, Norman’s son, George I. Norman III, age 19, and listed as a dependent on the 1970 Form 1040, appeared. He told the officers that the Stutz belonged to the petitioner corporation, and not to Norman. <em>Id., </em>at 80, 34. He testified that he was living at the cottage “as security.” <em>Id., </em>at 34. He was asked to provide evidence as to the car’s ownership. A decision was made not to seize the automobile at that 'time.</p>
<p id="b495-7">Information then came to Applegate, primarily from a Mr. Redd who was a contractor for Norman, that the cottage was a place of business and not a residence. <em>Id., </em>at 79. In addition, there was activity at the cottage that night; the lights were on and boxes were being moved. The next morning the Stutz was not in the garage.<footnotemark>8</footnotemark> <em>Id., </em>at 83. Sometime during the next two days, a decision was made to seize the cottage, its furnishings and any other assets there.<footnotemark>9</footnotemark> On <page-number citation-index="1" label="346">*346</page-number>March 23,<footnotemark>10</footnotemark> agents, acting without a warrant, and with the assistance of locksmiths and the equipment of a private van and storage firm, entered the cottage and removed its remaining contents, including furnishings and books and records. An inventory was made of the property so seized. The agents hoped to examine the books and records to see if they contained’stock certificates or information concerning the location of other assets. The Regional Counsel, however, instructed them to pack the books and records, seal the boxes, and remove them to a safe storage place. <em>Id., </em>at 83-88.</p>
<p id="b496-5">In May, petitioner corporation instituted this suit. JBy its amended complaint it asserted a claim for wrongful levy, with a request for the return of the automobiles; a claim for suppression of all evidence obtained from the seized documents; and a claim against the agents for damages. <em>Id., </em>at 105-112. It alleged that the assessments were arbitrary and capricious, that petitioner was not an alter ego of Norman, and that the levy upon its premises and the contents violated the Fourth Amendment. <em>Ibid.</em></p>
<p id="b496-6">Shortly thereafter, the Service returned to the cottage the originals of the records and documents that had been seized. In the meantime, however, they had been photocopied.<footnotemark>11</footnotemark> By a second amendment to petitioner’s complaint, <em>id., </em>at 124, punitive damages, among other relief, were requested.</p>
<p id="b496-7">Norman’s son filed a complaint in intervention, <em>id., </em>at 112-117, alleging essentially the same facts and requesting <page-number citation-index="1" label="347">*347</page-number>similar relief. The District Court allowed his intervention. The Government then filed a counterclaim seeking foreclosure of the tax liens against the property held in petitioner’s name. <em>Id., </em>at 127-134.</p>
<p id="b497-5">At the ensuing trial before the court without a jury there was testimony that Norman himself originally held title to some of the automobiles registered in petitioner’s name, <em>id., </em>at 37; that petitioner had no employees and did not lease any cars, <em>id., </em>at 37, 39; that petitioner’s only assets were luxury or vintage model automobiles; that the cars had not been transferred to it until at or near the end of 1972; and that petitioner never issued any stock, held any director’s meetings, or engaged in any business.<footnotemark>12</footnotemark> <em>Id., </em>at 43-45.</p>
<p id="b497-6">The District Court entered judgment for petitioner and for the intervenor. It found that the premises in question were the offices of petitioner and the residence of the intervenor; that the revenue-officer defendants had no&gt; search warrant; that they forcibly entered the premises on March 23 and again on March 25;<footnotemark>13</footnotemark> that they made the entry, search, and seizure “knowing full well that they were violating the rights” of petitioner, the intervenor, “and others”; that Agent Clayton committed the entry “maliciously”; that the defendants returned the books and records that had been seized but photocopied them and retained the photocopies; that the defendants levied upon and seized all the assets of petitioner, including seven automobiles and a bank account; that they disposed of two of the automobiles and stored the others in Salt Lake City; that the assessments of taxes, penalties, and interest against Norman and his wife for 1970 and 1971 were erroneous; that Norman and his wife had no liability for federal income tax, penalties, <page-number citation-index="1" label="348">*348</page-number>or interest for those years; that petitioner had “engaged in substantial business activity in preparation for its business purpose of leasing automobiles”; that it was not controlled solely by Norman or his wife; that it was not an alter ego of Norman or his wife; and that it was not their nominee. The court concluded that the revenue-officer defendants committed an illegal search and seizure of petitioner’s offices and the intervenor’s residence, in violation of the Fourth Amendment; that the photocopies of the seized books and records in the possession of the Service should be destroyed because am&amp;.use of them would be illegal; that petitioner and the intervenor were entitled to general and punitive damages in amounts to be determined; that the Government’s counterclaim should be dismissed with prejudice; that the Service should return all the seized assets of petitioner and of the intervenor; and that judgment should be awarded against the United States in favor of petitioner for the value of the two automobiles that had been sold. <em>Id., </em>at 136-142. Judgment, including injunctive relief for the return of the automobiles and the books and records, and for the destruction of the photocopies, was entered accordingly. <em>Id., </em>at 142-144.</p>
<p id="b498-5">The Court of Appeals, for the most part, reversed. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">514 F. 2d 935</a></span> (CA10 1975). It ruled that the evidence conclusively established that petitioner was Norman’s alter ego so that its assets could be seized to satisfy Norman’s income tax liability; that the District Court’s finding to the contrary was clearly erroneous; that petitioner had not sustained its burden of proving the assessments to be erroneous; and that the trial court erred in invalidating, the assessments and in dismissing the Government’s counterclaim. In regard to the claim of illegal search and seizures, the Court of Appeals held:</p>
<blockquote id="b498-6">“The refusal to pay authorized appellants to collect the tax by levy, and this included the power of 'seizure by any means.’ Thus appellants were acting pursuant to <page-number citation-index="1" label="349">*349</page-number>statute and did not commit an illegal search. The trial court’s order returning the assets and suppressing the documents is improper.” (Footnote omitted.) <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#941" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,..."><em>Id., </em>at 941</a></span>.</blockquote>
<p id="b499-5">The c(3urt also ruled that there was no evidence to support the trial court’s finding that Clayton’s participation “was of a malicious character.” <em><span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">Ibid.</a></span> </em>In accord with a concession by the Government, the Court of Appeals affirmed the trial court’s judgment insofar as it ordered the return of certain shares of stock to the intervenor.<footnotemark>14</footnotemark></p>
<p id="b499-6">II</p>
<p id="b499-7">A. Section 6331 (a) of the 1954 Code authorizes the Secretary or his delegate to collect taxes “by levy upon all property and rights to property” belonging to a person who “neglects or refuses to pay” any tax “or on which there is a lien ... for the payment of such tax.”<footnotemark>15</footnotemark> Section 6331 (b), <page-number citation-index="1" label="350">*350</page-number>and §7701 (a) (21) as well, define “levy” as including “the power of distraint and seizure by any means.” Both real estate and personal property, tangible and intangible, are subject to levy. Levy upon tangible property normally is effected by service of forms of levy or notice of levy and physical seizure of the property. Where that is not feasible, the property is posted or tagged. Because intangible property is not susceptible of physical seizure, posting, or tagging, levy upon it is effected by serving the appropriate form upon the party holding the property or rights to property. See <span class="citation no-link">Treas. Reg. § 301.6331-1</span> (a)(1), <span class="citation no-link">26 CFR § 301.6331-1</span> (a)(1) (1976). See also <em>Phelps </em>v. <em>United States, </em><span class="citation" data-id="109249"><a href="/opinion/109249/phelps-v-united-states/#335" aria-description="Citation for case: Phelps v. United States">421 U. S. 330, 335-337</a></span> (1975). And the Court has recognized that compulsion on the part of the Service occasionally is required in the enforcement of the revenue laws. See <em>United States </em>v. <em>Bisceglia, </em><span class="citation" data-id="9425992"><a href="/opinion/109190/united-states-v-bisceglia/#145" aria-description="Citation for case: United States v. Bisceglia">420 U. S. 141, 145</a></span> (1975). Indeed, one may readily acknowledge that the existence of the levy power is an essential part of our self-assessment tax system and that it enhances voluntary compliance in the collection of taxes that this Court has described as “the life-blood of government, and their prompt and certain availability an imperious need.” <em>Bull </em>v. <em>United States, </em><span class="citation" data-id="102455"><a href="/opinion/102455/bull-v-united-states/#259" aria-description="Citation for case: Bull v. United States">295 U. S. 247, 259</a></span> (1935).</p>
<p id="b500-4">Under § 6321 of the Code,<footnotemark>16</footnotemark> the assessments against Norman were a lien in favor of the United States upon all property <page-number citation-index="1" label="351">*351</page-number>belonging to Norman. If petitioner was Norman’s alter ego, it had no countervailing effect for purposes of his federal income tax. <em>Griffiths </em>v. <em>Commissioner, </em><span class="citation" data-id="103261"><a href="/opinion/103261/griffiths-v-commissioner/" aria-description="Citation for case: Griffiths v. Commissioner">308 U. S. 355</a></span> (1939); <em>Higgins </em>v. <em>Smith, </em><span class="citation" data-id="9419068"><a href="/opinion/103275/higgins-v-smith/#476" aria-description="Citation for case: Higgins v. Smith">308 U. S. 473, 476</a></span> (1940). It would then follow that the Service could properly regard petitioner’s assets as Norman’s property subject to the lien under § 6321, and the Service would be empowered, under § 6331, to levy upon assets held in petitioner’s name in satisfaction of Norman’s income tax liability. See <em>United States </em>v. <em>Plastic Electro-Finishing Corp., </em><span class="citation" data-id="1969224"><a href="/opinion/1969224/united-states-v-plastic-electro-finishing-corporation/#333" aria-description="Citation for case: United States v. Plastic Electro-Finishing Corporation">313 F. Supp. 330, 333-334</a></span> (EDNY 1970), aff’d, <span class="citation no-link">71-1 USTC ¶9421</span> (CA2 1971).</p>
<p id="b501-5">B. Our grant of certiorari was limited to the Fourth Amendment issue, and we declined to review petitioner’s and Norman’s son’s claims that the assessments and levies should have been voided and that petitioner was not Norman’s alter ego. Pet. for Cert. 2, 3.<footnotemark>17</footnotemark> We therefore approach this case accepting the Court of Appeals’ determinations that the assessments and levies were valid and that petitioner was Norman’s alter ego. Those facts necessarily establish probable cause to believe that assets held by petitioner were properly subject to seizure in satisfaction of the assessments. Petitioner does not claim that' there was no probable cause to believe that the automobiles were held by petitioner, nor does it claim that there was no probable cause to believe that its offices would contain other seizable goods. There being probable cause for the search and seizures, the only questions before the Court are whether warrants were required to malee “reasonable” either the seizures of the cars or the entry into and seizure of goods in the cottage.</p>
<p id="b501-6">C. The seizures of the automobiles in this case took place on public streets, parking lots, or other open places, and did not involve any invasion of privacy. In <em>Murray’s Lessee </em>v. <page-number citation-index="1" label="352">*352</page-number><em>Hoboken Land &amp; Improv. Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856), this Court held that a judicial warrant is not required for the seizure of a debtor’s land in satisfaction of a claim of the United States. The seizure in <em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">Murray’s Lessee</a></span> </em>was made through a transfer of title which did not involve an invasion of privacy. The warrantless seizures of the automobiles in this case are governed by the same principles and therefore were not unconstitutional. See also <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924) (liquor seized in open field).<footnotemark>18</footnotemark></p>
<p id="b502-5">D. The seizure of the books and records, however, involved intrusion into the privacy of petitioner’s offices. Significantly, the Court has said:</p>
<blockquote id="b502-6">“[0]ne governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search <page-number citation-index="1" label="353">*353</page-number>of private property without proper consent is 'unreasonable’ unless it has been authorized by a valid search warrant.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967).</blockquote>
<p id="b503-5">See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>, 45A-455 (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#512" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 512</a></span> (White, J., concurring and dissenting) ; <em>Stoner </em>v. <em>California, </em><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964); <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925).</p>
<p id="b503-6">The respondents do not contend that business premises are not protected by the Fourth Amendment. Such a proposition could not be defended in light of this Court’s clear holdings to the contrary. <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967); <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920). Nor can it be claimed that corporations are without some Fourth Amendment rights. <em>Go-Bart Co. </em>v. <em>United States, supra; Silverthorne Lumber Co. </em>v. <em>United States, supra; Oklahoma Press Pub. Co. </em>v. <em>Walling, </em><span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/#205" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186, 205-206</a></span> (1946); <em>Hale </em>v. <em>Henkel, </em><span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#75" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 75-76</a></span> (1906). Cf. <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21</a></span> (1974); <em>Federal Trade Comm’n </em>v. <em>American Tobacco Co., </em><span class="citation" data-id="100375"><a href="/opinion/100375/federal-trade-commission-v-american-tobacco-co/#305" aria-description="Citation for case: Federal Trade Commission v. American Tobacco Co.">264 U. S. 298, 305-306</a></span> (1924); <em>Wilson </em>v. <em>United States, </em><span class="citation" data-id="1293085"><a href="/opinion/1293085/wilson-v-united-states/#375" aria-description="Citation for case: Wilson v. United States">221 U. S. 361, 375-376</a></span> (1911); <em>Consolidated Rendering Co. </em>v. <em>Vermont, </em><span class="citation" data-id="96746"><a href="/opinion/96746/consolidated-rendering-co-v-vermont/#553" aria-description="Citation for case: Consolidated Rendering Co. v. Vermont">207 U. S. 541, 553-554</a></span> (1908).</p>
<p id="b503-7">The Court, of course, has recognized that a business, by its special nature and voluntary existence, may open itself to intrusions that would not be permissible in a purely private context. Thus, in <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), a warrantless search of a locked storeroom during business hours, pursuant to the inspection procedure authorized by the Gun Control Act of 1968, <span class="citation no-link">18 U. S. C. § 923</span> (g), was upheld:</p>
<blockquote id="b503-8">“When a dealer chooses to engage in this pervasively <page-number citation-index="1" label="354">*354</page-number>regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection.” <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p id="b504-5">See also <em>Colonnade Catering Corp. </em>v. <em>United </em>States, <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (Congress has broad authority to fashion standards of reasonableness for searches and seizures to regulate the liquor industry but failed in that case to authorize a warrantless search).</p>
<p id="b504-6">In the present case, however, the intrusion into petitioner’s privacy was not based on the nature of its business, its license, or any regulation of its activities. Rather, the intrusion is claimed to be justified on the ground that petitioner’s assets were seizable to satisfy tax assessments. This involves nothing more than the normal enforcement of the tax laws, and we find no justification for treating petitioner differently in these circumstances simply because it is a corporation.</p>
<p id="b504-7">The respondents argue that there is a broad exception to the Fourth Amendment that allows warrantless intrusions into privacy in the furtherance of enforcement of the tax laws. We recognize that the “Power to lay and collect Taxes” is a specifically enunciated power of the Federal Government, Const., Art. I, § 8, cl. 1, and that the First Congress, which proposed the adoption of the Bill of Rights, also provided that certain taxes could be “levied by distress and sale of goods of the person or persons refusing or neglecting to pay.” Act of Mar. 3, 1791, c. 15, § 23, <span class="citation no-link">1 Stat. 204</span>. This, however, relates to warrantless seizures rather than to warrantless searches. It is one thing to seize without a warrant property resting in an open area or seizable by levy without an intrusion into privacy, and it is quite another thing to effect a warrantless seizure of property, even that owned by a corporation, situated on private premises to which access is not otherwise available for the seizing officer.</p>
<p id="b505-4"><page-number citation-index="1" label="355">*355</page-number>Indeed, one of the primary evils intended to be eliminated by the Fourth Amendment was the massive intrusion on privacy undertaken in the collection of taxes pursuant to general warrants and writs of assistance.<footnotemark>19</footnotemark> As Madison argued, urging the adoption of a Bill of Rights to restrain the Federal Government:</p>
<blockquote id="b505-5">“The General Government has a right to pass all laws which shall be necessary to collect its revenue; the means for enforcing the collection are within the direction of the Legislature: may not general warrants be considered necessary for this purpose, as well as for some purposes which it was supposed at the framing of their constitutions the State Governments had in view? If there was reason for restraining the State Governments from exercising this power, there is like reason for restraining the Federal Government.” 1 Annals of Cong. 438 (1834 ed.).</blockquote>
<p id="b505-6">The respondents urge that the history of the common law in England and the laws in several States prior to the adoption of the Bill of Rights support the view that the Fourth Amendment was not intended to cover intrusions into privacy in the enforcement of the tax laws. We do not find in the cited materials anything approaching the clear evidence that would be required to create so great an exception to the Fourth Amendment’s protections against warrantless intrusions into privacy.</p>
<p id="b505-7">The respondents also rely upon certain dicta in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886) <footnotemark>20</footnotemark> (subpoena of private <page-number citation-index="1" label="356">*356</page-number>papers impermissible). But see <em>Fisher </em>v. <em>United States, 425 </em>U. S. 391, 408-411 (1976), and <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#471" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 471-472</a></span> (1976). We do not find in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>any direct holding that the warrant protections of the Fourth Amendment do not apply to invasions of privacy in furtherance of tax collection. Insofar as language in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>might be read so to state, we decline to follow those dicta into rejection of the basic governing principle that has shaped Fourth Amendment law.</p>
<p id="b506-5">Finally, the respondents argue that warrantless searches are justified by congressional enactment, as were the searches in <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Colonnade. </em>The statute, § 6331 (b) of the Code, <span class="citation no-link">26 U. S. C. § 6331</span> (b), authorizes “distraint and seizure by any means.” See n. 15, <em>supra. </em>Read narrowly, it au<page-number citation-index="1" label="357">*357</page-number>thorizes the use of every means to deprive the taxpayer of use, enjoyment, or title to property (e. <em>g., </em>transferring title, asportation, immobilization). It does not refer to warrant-less intrusions into privacy. The respondents, however, would have us read the statute to authorize such warrant-less intrusions. They assert that a statute of that kind is permissible in light of the considerations discussed in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>and <em>See. </em>Examination of the statute shows that quite the opposite is true.</p>
<p id="b507-5">The respondents recognize that one of the Court’s critical concerns in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span> </em>and <em>See </em>was the discretion of the seizing officers. Brief for Respondents 66. Yet § 6331 clearly gives the Secretary or his delegate discretion as to what property to seize. If more than one location is involved, the Secretary will choose which dwelling will be invaded. If property is to be found both in public places and in private areas, the Secretary may choose which to seize. This hardly can be called a restraint on discretion. The respondents also recognize the concern with the existence of questions of disputed fact. They argue that in the seizure situation there are no such questions; yet in the present case the agents’ confusion over whether the premises were an office or a residence demonstrates the contrary.</p>
<p id="b507-6">The respondents assert that the burden on the Government of obtaining a warrant is a relevant factor. Brief for Respondents 67-68. They suggest that the burden is great here because the Government is dealing with persons who may attempt to put their property beyond reach. Yet the statute authorizes distraint and seizure whenever a taxpayer <em>neglects </em>or refuses to pay his tax, and regardless of any indication of risk of concealment. The statute simply does not focus on situations involving a need for rapid action.</p>
<p id="b507-7">The respondents argue that the interest in the collection of taxes is such as to bring this case within the reasoning of <em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span> </em>and <em>Colonnade. </em>Those cases involved voluntary <page-number citation-index="1" label="358">*358</page-number>participation in a highly regulated activity. Section 6331, however, covers all defaults on all taxes, and we are unwilling to hold that the mere interest in the collection of taxes is sufficient to justify a statute declaring <em>per se </em>exempt from the warrant requirement every intrusion into privacy made in furtherance of any tax seizure.</p>
<p id="b508-5">The respondents suggest that the privacy interest in business premises is less than that in a private home., Even if correct, the assertion is irrelevant with respect to the intent of the statute, for the statute makes no distinction between business properties and dwelling areas. If it authorizes entries at all, it authorizes entries into both business premises and private homes.</p>
<p id="b508-6">The respondents offer no legislative history in support of their reading of § 6331, and to give the statute that reading would call its constitutionality into serious question. We therefore decline to read it as giving <em>carte blanche </em>for warrantless invasions of privacy. Rather, we give it its natural reading, namely, as an authorization for all forms of <em>seizure, </em>but as silent on the subject of intrusions into privacy.</p>
<p id="b508-7">The intrusion into petitioner’s office is therefore governed by the normal Fourth Amendment rule that “except in certain carefully defined classes of cases, a search of private property without proper consent is 'unreasonable’ unless it has been authorized by a valid search warrant.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528-529</a></span>.</p>
<p id="b508-8">As an alternative to their argument that a new exception to the warrant requirement should be recognized, the respondents assert that the facts of this case bring it within the “exigent circumstances” exception to the warrant requirement.<footnotemark>21</footnotemark> The agents’ own actions, however, in their <page-number citation-index="1" label="359">*359</page-number>delay for two days following their first entry, and for more than one day following the observation of materials being moved from the office, before they made the entry during which they seized the records, are sufficient to support the District Court’s implicit finding that there were no exigent circumstances in this case.</p>
<p id="b509-5">We therefore conclude that the warrantless entry into petitioner’s office was in violation of the commands of the Fourth Amendment.</p>
<p id="b509-6">Ill</p>
<p id="b509-7">This takes us to the issue of remedy. Specifically, petitioner, by its second amended complaint, prayed for (a) the return of the photocopies of the books and records; (b) the return of the automobiles; (c) a declaration that petitioner is not the alter ego of Norman or of Mrs. Norman; (d) the suppression of all evidence obtained from the books And records; (e) the suppression of the automobiles as evidence; (f) the release of all levies; and (g) general and punitive damages against the individual defendant-agents. App, 123-124.</p>
<p id="b509-8">The alter ego issue, as has been noted, was denied review. The books and' records were returned, and the photocopies concededly have been destroyed; that claim, thus, is moot. We have decided the issue of the legality of the seizure of the automobiles adversely to petitioner. The suppression issue, as to the books and records, obviously is premature and may be considered if and when proceedings arise in which the Government seeks to use the documents or information obtained from them. See <em>Meister </em>v. <em>United </em>States, <span class="citation" data-id="8879056"><a href="/opinion/8892725/meister-v-united-states/#269" aria-description="Citation for case: Meister v. United States">397 F. 2d 268, 269</a></span> (CA3 1968); <em>Hill </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/F.%202d/346/175/">346 F. 2d 175</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./382/956/">382 U. S. 956</a></span> (1965). And the irreparable injury required to support a motion to suppress, under Fed. Rule Crim. Proc. 41 (e), on equitable grounds in advance of any proceedings, has not been dem<page-number citation-index="1" label="360">*360</page-number>onstrated. <em>Hunsucker </em>v. <em>Phinney, </em><span class="citation" data-id="9460619"><a href="/opinion/319298/louis-sager-hunsucker-jr-v-robert-l-phinney-district-director-of/#34" aria-description="Citation for case: Louis Sager Hunsucker, Jr. v. Robert L. Phinney, District...">497 F. 2d 29, 34</a></span> (CA5 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/927/">420 U. S. 927</a></span> (1975).</p>
<p id="b510-5">This leaves only the issue of damages against the individual agents. The District Court found that Agent Clayton “maliciously committed said forced entry, and search and seizure,” App. 138, and concluded that he and other individual defendants acted “knowing full well that they were violating the rights of” petitioner. <em>Ibid. </em>It concluded that petitioner was entitled to judgment for those actions. The Court of Appeals, in the context of its holding that the entry and search were not illegal, ruled that the finding of maliciousness on the part of Clayton was unsupported by any evidence in the record and was clearly erroneous. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#940" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,...">514 F. 2d, at 940-941</a></span>. It also reversed the judgment awarding petitioner damages. <span class="citation" data-id="327017"><a href="/opinion/327017/g-m-leasing-corp-v-the-united-states-of-america-george-i-norman-iii/#942" aria-description="Citation for case: G. M. Leasing Corp. v. The United States of America,..."><em>Id., </em>at 942</a></span>.</p>
<p id="b510-6">We have held above, however, that a warrant should have been obtained, under the circumstances of this case, before the forcible entry was effected. This brings into focus and for consideration this Court’s decision in <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971), and the reservation there of the immunity question. The Government suggests that, assuming a violation of the Fourth Amendment by the agents, petitioner is not entitled to money damages if the agents acted in good faith; that good faith was supported by the “apparent fact” that the agents’ conduct was in conformity with standard Service procedures based upon <em>Murray’s Lessee, supra; </em>and that the record justifies the conclusion that the agents acted in good faith. That may well be, but we conclude that this aspect of the facts, the existence of proof of any injury to petitioner resulting from the entry and the temporary seizure of the books and records, and the immunity issue all should be addressed in the first instance by the Court of Appeals and, if it so directs, by the District Court.</p>
<p id="b511-4"><page-number citation-index="1" label="361">*361</page-number>The judgment of the Court of Appeals is therefore affirmed in part and reversed in part, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b511-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b490-12"> The Fourth Amendment reads:</p>
<blockquote id="b490-13">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="2">
<p id="b491-9"> Four extensions of time for filing had been granted. App. 99.</p>
</footnote>
<footnote label="3">
<p id="b492-6"> At the same time, the Service determined deficiencies in Mrs. Norman’s income tax liability for 1970 and 1971 in the amounts of $69,265.04 and $84,873.50, respectively. <em>Id., </em>at 96. Those deficiencies are not at issue in this case.</p>
</footnote>
<footnote label="4">
<p id="b492-7"> Agent Clayton, called as a witness for the petitioner in the present case, on cross-examination answered “No” to the question whether he was “able to get any cooperation at all” from Mr. Norman. <em>Id., </em>at 30. When later called as a witness on behalf of the respondents, Clayton also gave a negative answer to the question whether he had received “any information from the taxpayer or his accountant or representative.” <em>Id., </em>at 66.</p>
<p id="b492-8">Petitioner protests any adverse inference that might flow from this testimony and asserts that there is no evidence that Clayton requested assistance from Norman or his representatives who had filed powers of attorney with the Service. Reply Brief for Petitioners 3-4. Counsel for respondents at oral argument stated: “I want to correct any wrong implication if there is one, that they received no cooperation from Mr. Norman. . . . [N]obody had asked him prior to that time [his becoming a fugitive] for cooperation.” Tr. of Oral Arg. 25.</p>
</footnote>
<footnote label="5">
<p id="b492-9"> Jeopardy assessments of the determined deficiencies in Mrs. Norman’s taxes were also made on March 19. App. 97.</p>
<p id="b492-10">The notice which is required after jeopardy assessment by § 6861 (b) of the Code enables the taxpayer to file a petition with the United States Tax Court for a redetermination of the deficiency. See <em>Laing </em>v. <em>United States, </em><span class="citation" data-id="9426233"><a href="/opinion/109340/laing-v-united-states/" aria-description="Citation for case: Laing v. United States">423 U. S. 161</a></span> (1976). A timely notice was sent to Norman, and a petition was filed on his behalf with the Tax Court. His case awaits trial there (Docket No. 6000-73).</p>
</footnote>
<footnote label="6">
<p id="b494-7"> The two automobiles seized in Los Angeles were a two-door tan Stutz, valued at $30,000, and a four-door burgundy Stutz, valued at $100,000. They were financed by loans from Murray First Thrift. Following the levy, Murray foreclosed its own liens and arranged with Norman’s attorney for the sale of the automobiles. App. 33, 122. It appears that the Government did not participate in those transactions and received no portion of the proceeds of the sales.</p>
</footnote>
<footnote label="7">
<p id="b495-8"> The Internal Revenue Service Manual, ¶ 5341.1, instructs that if an occupant of a private residence denies a revenue officer permission to enter, the officer should not attempt entry by force.</p>
</footnote>
<footnote label="8">
<p id="b495-9"> The Service later found this particular automobile at another location. App. 83. It had been moved by Norman’s son after the revenue agents had left on March 21. <em>Id., </em>at 34.</p>
</footnote>
<footnote label="9">
<p id="b495-10"> Title to the cottage was in the name of Real Estate, Inc., a corporation the Service determined to be the alter ego of Mrs. Norman. <em>Id., </em>at 97. That corporation is not a party to the present suit and the relief petitioner requests does not include the return of the cottage.</p>
</footnote>
<footnote label="10">
<p id="b496-8"> There is some evidence in the record that this took place on March 22 rather than March 23. <em>Id., </em>at 34, 59, 77.</p>
</footnote>
<footnote label="11">
<p id="b496-9"> The respondents in their brief state that while the case was pending on appeal to the Tenth Circuit the Service voluntarily destroyed all existing photocopies of the seized books and records. Brief for Respondents 16 n. 9, 76-77, and n. 43. Petitioner concedes that the seized documents have been returned and the photocopies destroyed. Tr. of Oral Arg. <em>14r-15.</em></p>
</footnote>
<footnote label="12">
<p id="b497-7"> There was conflicting testimony as to whether stock was issued. 1 Tr. 52-53.</p>
</footnote>
<footnote label="13">
<p id="b497-8"> This date appears to be an error. See also n. 10, <em>supra.</em></p>
</footnote>
<footnote label="14">
<p id="b499-8"> This portion of the judgment of the Court of Appeals affirming the trial court is not before us. Neither is any right of the intervenor at issue here. Tr. of Oral Arg. 13.</p>
</footnote>
<footnote label="15">
<p id="b499-9"> Section 6331 reads in part:</p>
<blockquote id="b499-10">“(a) Authority of Secretary or delegate.</blockquote>
<blockquote id="b499-11">“If any person liable to pay any tax neglects or refuses to pay the same within 10 days after notice and demand, it shall be lawful for the Secretary or his delegate to collect such tax (and such further sum as shall be sufficient to cover the expenses of the levy) by levy upon all property and rights to property (except such property as is exempt under section 6334) belonging to such person or on which there is a lien provided in this chapter for the payment of such tax. ... If the Secretary or his delegate makes a finding that the collection of such tax is in jeopardy, notice and demand for immediate payment of such tax may be made by the Secretary or his delegate and, upon failure or refusal to pay such tax, collection thereof by levy shall be lawful without regard to the 10-day period provided in this section.</blockquote>
<blockquote id="b499-12">“(b) Seizure and sale of property.</blockquote>
<blockquote id="b499-13">“The term ‘levy’ as used in this title includes the power of distraint and seizure by any means. A levy shall extend only to property pos<page-number citation-index="1" label="350">*350</page-number>sessed and obligations existing at the time thereof. In any case in which the Secretary or his delegate may levy upon property or rights to property, he may seize and sell such property or rights to property (whether real or personal, tangible or intangible).”</blockquote>
</footnote>
<footnote label="16">
<p id="b500-6"> Section 6321 reads:</p>
<blockquote id="b500-7">“If any person liable to pay any tax neglects or refuses to pay the same after demand, the amount (including any interest, additional amount, addition to tax, or assessable penalty, together with any costs that may accrue in addition thereto) shall be a lien in favor of the United States upon all property and rights to property, whether real or personal, belonging to such person.”</blockquote>
</footnote>
<footnote label="17">
<p id="b501-7"> This effectuated a denial of the son’s petition for certiorari.</p>
</footnote>
<footnote label="18">
<p id="b502-7"> If additional support were needed for this result, it is found in the Court’s decisions sustaining the right of the Government to collect taxes by summary administrative proceedings. Thus, in <em>Bull </em>v. <em>United States, </em><span class="citation" data-id="102455"><a href="/opinion/102455/bull-v-united-states/#260" aria-description="Citation for case: Bull v. United States">295 U. S. 247, 260</a></span> (1935), it was stated that a tax assessment “is given the force of a judgment, and if the amount assessed is not paid when due, administrative officials may seize the debtor’s property to satisfy the debt.” See also <em>Cheatham </em>v. <em>United States, </em><span class="citation" data-id="89244"><a href="/opinion/89244/cheatham-v-united-states/#87" aria-description="Citation for case: Cheatham v. United States">92 U. S. 85, 87-90</a></span> (1876); <em>State Railroad Tax Cases, </em><span class="citation" data-id="89311"><a href="/opinion/89311/taylor-v-secor/#612" aria-description="Citation for case: Taylor v. Secor">92 U. S. 575, 612-615</a></span> (1876); <em>Graham </em>v. <em>Du Pont, </em><span class="citation" data-id="100215"><a href="/opinion/100215/graham-v-du-pont/#255" aria-description="Citation for case: Graham v. Du Pont">262 U. S. 234, 255</a></span> (1923). The rationale underlying these decisions, of course, is that the very existence of government depends upon the prompt collection of the revenues. In <em>Phillips </em>v. <em>Commissioner, </em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#596" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589, 596-597</a></span> (1931), the Court rejected a constitutional challenge to the statutory system under which taxes may be collected summarily without a pre-seizure judicial hearing. It was held that as long as there was an adequate opportunity for a post-seizure determination of the taxpayer’s rights, the statute met the requirements of due process. See <em>Commissioner </em>v. <em>Shapiro, </em><span class="citation" data-id="9426305"><a href="/opinion/109396/commissioner-v-shapiro/#630" aria-description="Citation for case: Commissioner v. Shapiro">424 U. S. 614, 630-633</a></span> (1976); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 91-92</a></span> (1972). These cases, of course, center upon the Due Process Clause rather than the Fourth Amendment, but the constitutional analysis is similar and yields a like result. It is to be noted that the Court in <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#596" aria-description="Citation for case: Phillips v. Commissioner"><em>Phillips, 283 </em>U. S., at 596</a></span>, cited <em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">Murray’s Lessee</a></span> </em>with approval as a case which sustained proceedings “more summary in character” and “involving less directly the obligation of the taxpayer.”</p>
</footnote>
<footnote label="19">
<p id="b505-8"> See T. Taylor, Two Studies in Constitutional Interpretation 41 (1969); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937); J. Landynski, Search and Seizure and the Supreme Court 30-42 (1966).</p>
</footnote>
<footnote label="20">
<p id="b505-9"> In <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>the Court stated:</p>
<p id="b505-10">“The search for and seizure of stolen or forfeited goods, or goods liable to duties and concealed to avoid the payment thereof, are totally different <page-number citation-index="1" label="356">*356</page-number>things from a search for and seizure of a man’s private books and papers for the purpose of obtaining information therein contained, or of using them as evidence against him.” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S., at 623</a></span>.</p>
<p id="b506-7">The Court's concern in <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>was with establishing the impermissibility of the subpoena of papers. It was not concerned with the warrant requirement for entry into- private places. The'Court, however, did say:</p>
<p id="b506-8">“The entry upon premises, made by a sheriff or other officer of the law, for the purpose of seizing goods and chattels <em>by virtue of a judicial writ, </em>such as an attachment, a sequestration, or an execution, is not within the prohibition of the Fourth or Fifth Amendment, or any other clause of the Constitution.” <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 624</a></span> (emphasis added).</p>
<p id="b506-9">The Court was not concerned with, and therefore did not explain, whether the “judicial writ” referred to above was necessary in order to meet the warrant requirements. The opinion does describe the “obnoxious writs of assistance” against which the Fourth Amendment was designed to protect. This description gives an indication of the types of tax-enforcement actions that the Amendment’s protections were intended to reach:</p>
<p id="b506-10">“Even the act under which the obnoxious writs of assistance were issued did not go as far as this, but' only authorized the examination of ships and vessels, and persons found therein, for the purpose of finding goods prohibited to be imported or exported, or on which the duties were not paid, and to enter into and search any suspected vaults, cellars, or warehouses for such goods." (Footnote omitted.) <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States"><em>Id., </em>at 623</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b508-9"> There is no claim that any"'other exception to the warrant requirement, such as “hot pursuit,” “plain view,” or “pursuant to an arrest,” is applicable here.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Gardner v. Broderick.md  (`case`, 5 assertions)

### content_page

```
---
title: "Gardner v. Broderick"
type: case
citation: "392 U.S. 273 (1968)"
parallel_cite: "88 S. Ct. 1913; 20 L. Ed. 2d 1082"
neutral_cite: 1968 U.S. LEXIS 1351
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-10
docket: 635
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gardner v. Broderick
  varies_by_point: false
  scope_note: "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107738/gardner-v-broderick/"
  cluster_id: 107738
  opinion_id: 107738
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Lefkowitz v. Turley]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "immunity-waiver"]
holding: "A public employee (here a police officer) may not be dismissed solely for refusing to waive his Fifth Amendment immunity; but he may be required to answer questions specifically, directly, and narrowly related to his official duties under a grant of use immunity, and discharged if he refuses to answer those."
lake:
  record_id: Gardner v. Broderick
  status: verified
  projected_at: 2026-07-06
---

# Gardner v. Broderick

*392 U.S. 273 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gardner, a New York City police officer, was called before a grand jury investigating police corruption. He was advised of his privilege against self-incrimination but was asked to sign a "waiver of immunity" that would have allowed his compelled testimony to be used to prosecute him. He refused to sign and was discharged from the force under a City Charter provision mandating dismissal of any officer who refuses to waive immunity. He challenged the dismissal as a penalty for exercising his Fifth Amendment privilege.

## Issue
Whether a police officer may be dismissed solely because he refused to waive his constitutional privilege against self-incrimination — that is, refused to sign a waiver of immunity — before a grand jury investigating his conduct.

## Rule
An employee may not be fired merely for asserting the privilege: "the mandate of the great privilege against self-incrimination does not tolerate the attempt, regardless of its ultimate effectiveness, to coerce a waiver of the immunity it confers on penalty of the loss of employment." — 392 U.S. at 279. ^pin-279

But the employer may compel job-related answers under immunity: "If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties, without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself, . . . the privilege against self-incrimination would not have been a bar to his dismissal." — *Id.* at 278. ^pin-278

## Application
Gardner was not discharged for refusing to give an account of his official conduct under a grant of immunity; he was discharged for refusing to sign a blanket waiver that would have stripped the immunity protecting his compelled testimony from use in a criminal prosecution. Because the City conditioned his continued employment on surrendering the privilege itself — rather than on answering duty-related questions while keeping the immunity — his dismissal penalized the exercise of a constitutional right and could not stand.

## Conclusion
The dismissal was unconstitutional and was reversed. *Gardner* refines [[Garrity v. New Jersey]]: a public employer may require an officer to answer questions narrowly related to his official duties under a grant of use immunity (and discharge him for refusing), but may not fire him simply for refusing to waive that immunity.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Gardner* is good law and, with [[Lefkowitz v. Turley]], fixes the rule that the State may compel duty-related answers only under immunity, never by forcing a waiver. The federal counterpart warning is articulated in [[Kalkines v. United States]].

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Gardner v. Broderick*, 392 U.S. 273 (1968) — https://www.courtlistener.com/opinion/107738/gardner-v-broderick/ — pinpoints: 278, 279.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "97e7ffadeb6fcd92", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "392 U.S. 273 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1351", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1913; 20 L. Ed. 2d 1082", "title": "Gardner v. Broderick", "year": "1968"}}
{"assertion_id": "5625ea905555d809", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Key — Progeny / Refinement", "title": "Gardner v. Broderick"}}
{"assertion_id": "74335810a4b27ecc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A public employee (here a police officer) may not be dismissed solely for refusing to waive his Fifth Amendment immunity; but he may be required to answer questions specifically, directly, and narrowly related to his official duties under a grant of use immunity, and discharged if he refuses to answer those.", "title": "Gardner v. Broderick"}}
{"assertion_id": "3db3d78f6e5b638d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gardner v. Broderick"}}
{"assertion_id": "ca08f4aae963beca", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Gardner v. Broderick", "field_i_validity": "good_law", "scope_note": "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted).", "title": "Gardner v. Broderick", "varies_by_point": "false"}}
```

### lake record — Gardner v. Broderick

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gardner v. Broderick",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gardner v. Broderick",
    "case_name_short": "Gardner",
    "case_name_full": "GARDNER v. BRODERICK, POLICE COMMISSIONER OF THE CITY OF NEW YORK, Et Al.",
    "input_case_name": "Gardner v. Broderick",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": "635",
    "cluster_id": 107738,
    "lead_opinion_id": 107738,
    "sibling_ids": [
      107738
    ],
    "absolute_url": "/opinion/107738/gardner-v-broderick/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8970907,
        "score": 20,
        "case_name": "Gardner v. Broderick"
      },
      {
        "cluster_id": 8970362,
        "score": 20,
        "case_name": "Gardner v. Broderick"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 273",
      "volume": "392",
      "reporter": "U.S.",
      "page": "273",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1913",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1913",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1082",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1082",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1351",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1351",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 273",
        "volume": "392",
        "reporter": "U.S.",
        "page": "273",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1913",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1913",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1082",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1082",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1351",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1351",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 273",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 273",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-279",
      "page": null,
      "quote": "that would have allowed his compelled testimony to be used to prosecute him. He refused to sign and was discharged from the force under a City Charter provision mandating dismissal of any officer who refuses to waive immunity. He challenged the dismissal as a penalty for exercising his Fifth Amendment privilege. ## Issue Whether a police officer may be dismissed solely because he refused to waive his constitutional privilege against self-incrimination \u2014 that is, refused to sign a waiver of immunity \u2014 before a grand jury investigating his conduct. ## Rule An employee may not be fired merely for asserting the privilege:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-278",
      "page": null,
      "quote": "If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties, without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself, . . . the privilege against self-incrimination would not have been a bar to his dismissal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gardner v. Broderick",
    "varies_by_point": false,
    "scope_note": "Good law; the Garrity companion drawing the line between firing an employee for asserting the privilege (barred) and compelling job-related answers under use immunity (permitted).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spielbauer v. County of Santa Clara",
          "cluster_id": 5608087,
          "cite": [
            "45 Cal. 4th 704",
            "199 P.3d 1125",
            "88 Cal. Rptr. 3d 590",
            "28 I.E.R. Cas. (BNA) 1254",
            "2009 Cal. LEXIS 1010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sher v. U.S. Department of Veterans Affairs",
          "cluster_id": 202763,
          "cite": [
            "488 F.3d 489",
            "26 I.E.R. Cas. (BNA) 243",
            "2007 U.S. App. LEXIS 12365",
            "90 Empl. Prac. Dec. (CCH) 43,067",
            "100 Fair Empl. Prac. Cas. (BNA) 1495",
            "2007 WL 1532655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Verbois",
          "cluster_id": 1451583,
          "cite": [
            "10 S.W.3d 825",
            "2000 Tex. App. LEXIS 1263",
            "2000 WL 216934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Burlington Police Officers' Ass'n v. City of Burlington",
          "cluster_id": 8209509,
          "cite": [
            "166 Vt. 581",
            "689 A.2d 1071",
            "1996 Vt. LEXIS 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Serafino v. Hasbro, Inc.",
          "cluster_id": 196719,
          "cite": [
            "82 F.3d 515",
            "1996 U.S. App. LEXIS 8849",
            "70 Fair Empl. Prac. Cas. (BNA) 917",
            "1996 WL 187381"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. U.S. Department of the Treasury",
          "cluster_id": 6491,
          "cite": [
            "25 F.3d 237"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Moses",
          "cluster_id": 1882575,
          "cite": [
            "792 F. Supp. 529",
            "1992 U.S. Dist. LEXIS 8685",
            "23 Bankr. Ct. Dec. (CRR) 137",
            "1992 WL 132012"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steven M. Asherman v. Larry Meachum, Commissioner, Connecticut Department of Correction",
          "cluster_id": 578610,
          "cite": [
            "957 F.2d 978",
            "1992 U.S. App. LEXIS 2101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Matt v. Larocca",
          "cluster_id": 5689113,
          "cite": [
            "71 N.Y.2d 154",
            "524 N.Y.S.2d 180",
            "518 N.E.2d 1172",
            "1987 N.Y. LEXIS 19884"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lonnie Benjamin and Harold Hicken v. The City of Montgomery",
          "cluster_id": 466179,
          "cite": [
            "785 F.2d 959",
            "1986 U.S. App. LEXIS 23631"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lybarger v. City of Los Angeles",
          "cluster_id": 1206957,
          "cite": [
            "710 P.2d 329",
            "40 Cal. 3d 822",
            "221 Cal. Rptr. 529",
            "1985 Cal. LEXIS 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clarence Leon Taylor, Jr. v. E. Parry Best, Lt. D.W. Smith, Paul Mills L.T. Lester",
          "cluster_id": 442995,
          "cite": [
            "746 F.2d 220",
            "1984 U.S. App. LEXIS 18178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Acceptance Company of America v. Joseph S. Bathalter, Jr.",
          "cluster_id": 417757,
          "cite": [
            "705 F.2d 924",
            "36 Fed. R. Serv. 2d 447",
            "1983 U.S. App. LEXIS 28695"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re the Claim of Altieri",
          "cluster_id": 5999349,
          "cite": [
            "92 A.D.2d 1028",
            "461 N.Y.S.2d 436",
            "1983 N.Y. App. Div. LEXIS 17429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE DEPT. OF HIGHWAY SAF., ETC. v. Zimmer",
          "cluster_id": 1729887,
          "cite": [
            "398 So. 2d 463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kastigar v. United States",
          "cluster_id": 108541,
          "cite": [
            "32 L. Ed. 2d 212",
            "92 S. Ct. 1653",
            "406 U.S. 441",
            "1972 U.S. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Turley",
          "cluster_id": 108882,
          "cite": [
            "38 L. Ed. 2d 274",
            "94 S. Ct. 316",
            "414 U.S. 70",
            "1973 U.S. LEXIS 132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
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
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maness v. Meyers",
          "cluster_id": 109130,
          "cite": [
            "42 L. Ed. 2d 574",
            "95 S. Ct. 584",
            "419 U.S. 449",
            "1975 U.S. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Couch v. United States",
          "cluster_id": 108650,
          "cite": [
            "34 L. Ed. 2d 548",
            "93 S. Ct. 611",
            "409 U.S. 322",
            "1973 U.S. LEXIS 23",
            "31 A.F.T.R.2d (RIA) 477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kordel",
          "cluster_id": 108066,
          "cite": [
            "25 L. Ed. 2d 1",
            "90 S. Ct. 763",
            "397 U.S. 1",
            "1970 U.S. LEXIS 71",
            "13 Fed. R. Serv. 2d 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Filarsky v. Delia",
          "cluster_id": 798512,
          "cite": [
            "182 L. Ed. 2d 662",
            "132 S. Ct. 1657",
            "566 U.S. 377",
            "2012 U.S. LEXIS 3105"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Tennessee",
          "cluster_id": 108551,
          "cite": [
            "32 L. Ed. 2d 358",
            "92 S. Ct. 1891",
            "406 U.S. 605",
            "1972 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Cunningham",
          "cluster_id": 109683,
          "cite": [
            "53 L. Ed. 2d 1",
            "97 S. Ct. 2132",
            "431 U.S. 801",
            "1977 U.S. LEXIS 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garner v. United States",
          "cluster_id": 109400,
          "cite": [
            "47 L. Ed. 2d 370",
            "96 S. Ct. 1178",
            "424 U.S. 648",
            "1976 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Selective Service System v. Minnesota Public Interest Research Group",
          "cluster_id": 111260,
          "cite": [
            "82 L. Ed. 2d 632",
            "104 S. Ct. 3348",
            "468 U.S. 841",
            "1984 U.S. LEXIS 151",
            "52 U.S.L.W. 5140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. Oregon",
          "cluster_id": 109043,
          "cite": [
            "40 L. Ed. 2d 642",
            "94 S. Ct. 2116",
            "417 U.S. 40",
            "1974 U.S. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Apfelbaum",
          "cluster_id": 110216,
          "cite": [
            "63 L. Ed. 2d 250",
            "100 S. Ct. 948",
            "445 U.S. 115",
            "1980 U.S. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bennie Lenard, Cross-Appellant v. Robert Argento & Joseph Sansone v. Village of Melrose Park",
          "cluster_id": 414191,
          "cite": [
            "699 F.2d 874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pillsbury Co. v. Conboy",
          "cluster_id": 110821,
          "cite": [
            "74 L. Ed. 2d 430",
            "103 S. Ct. 608",
            "459 U.S. 248",
            "1983 U.S. LEXIS 124",
            "35 Fed. R. Serv. 2d 669",
            "51 U.S.L.W. 4061",
            "12 Fed. R. Serv. 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Aichele",
          "cluster_id": 566407,
          "cite": [
            "941 F.2d 761",
            "91 Cal. Daily Op. Serv. 6180",
            "91 Daily Journal DAR 9211",
            "1991 U.S. App. LEXIS 16620",
            "1991 WL 138118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edith Libutti, Doing Business as Lion Crest Stable, a Sole Proprietorship v. United States",
          "cluster_id": 736205,
          "cite": [
            "107 F.3d 110",
            "79 A.F.T.R.2d (RIA) 1240",
            "1997 U.S. App. LEXIS 3060"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William L. O'Brien v. Robert J. Digrazia",
          "cluster_id": 340425,
          "cite": [
            "544 F.2d 543",
            "1976 U.S. App. LEXIS 6330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Carroll",
          "cluster_id": 2285969,
          "cite": [
            "772 A.2d 45",
            "339 N.J. Super. 429"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73222,
          "cite": [
            "153 F.3d 1233",
            "1998 U.S. App. LEXIS 38861",
            "1998 WL 564374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vincent E. Scott v. United States",
          "cluster_id": 287590,
          "cite": [
            "419 F.2d 264",
            "135 U.S. App. D.C. 377",
            "1969 U.S. App. LEXIS 8942"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gardner v. Broderick:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107738) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTg0NzM2MDAwMDAmcz01OTg1NDM3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107738%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 18,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 19,
        "triage_snippet_classified": 181
      },
      "lane2_top_cited": {
        "query": "cites:(107738)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OCZzPTY1NzM0MSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107738%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107738)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107738)",
    "indexed_citing_opinions": 488,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107738,
        "count": 488,
        "count_source": "search"
      }
    ],
    "citation_count": 696,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gardner-v-broderick.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ4MDA2NzYmcz0zMTYwMDQwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107738%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107738,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 107337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107738,
        "cited_id": 2591177,
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
    "date_created": "2026-07-05T05:04:47Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:12:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:06:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gardner v. Broderick

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b316-6">
  Me. Justice Fortas
 </author>
<p id="A0r">
  delivered the opinion of the Court.
 </p>
<p id="b316-7">
  Appellant brought this action in the Supreme Court of the State of New York seeking reinstatement as a New York City patrolman and back pay. He claimed he was unlawfully dismissed because he refused to waive his privilege against self-incrimination. In August 1965, pursuant to subpoena, appellant appeared before a New York County grand jury which was investigating alleged bribery and corruption of police officers in connection with unlawful gambling operations. He was advised that the grand jury proposed to examine him concerning the performance of his official duties. He was advised of his privilege against self-incrimination,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  but he was asked to sign a “waiver of immunity” after being told that he would be fired if he did not sign.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Following
  <span citation-index="1" class="star-pagination" label="275"> 
   *275
   </span>
  his refusal, he was given an administrative hearing and was discharged solely for this refusal, pursuant to § 1123 of the New York City Charter.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b318-5">
<span citation-index="1" class="star-pagination" label="276"> 
   *276
   </span>
  The New York Supreme Court dismissed his petition for reinstatement, 27 App. Div. 2d 800, 279 N. Y. S. 2d 150 (1967), and the New York Court of Appeals affirmed. 20 N. Y. 2d 227, <span class="citation" data-id="5523781"><a href="/opinion/5676083/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">229 N. E. 2d 184</a></span> (1967). We noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./390/918/">390 U. S. 918</a></span> (1968).
 </p>
<p id="b318-6">
  Our decisions establish beyond dispute the breadth of the privilege to refuse to respond to questions when the result may be self-incriminatory, and the need fully to implement its guaranty. See
  <em>
   Spevack
  </em>
  v.
  <em>
   Klein,
  </em>
  <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">385 U. S. 511</a></span> (1967);
  <em>
   Counselman
  </em>
  v.
  <em>
   Hitchcock,
  </em>
  <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 585-586</a></span> (1892);
  <em>
   Albertson
  </em>
  v.
  <em>
   SACB,
  </em>
  <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#80" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 80</a></span> (1965). The privilege is applicable to state as well as federal proceedings.
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964);
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Commission,
  </em>
  <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52</a></span> (1964). The privilege may be waived in appropriate circumstances if the waiver is knowingly and voluntarily made. Answers may be compelled regardless of the privilege if there is immunity from federal and state use of the compelled testimony or its fruits in connection with a criminal prosecution against the person testifying.
  <em>
   Counselman
  </em>
  v.
  <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#585" aria-description="Citation for case: Counselman v. Hitchcock"><em>
   Hitchcock, supra,
  </em>
  at 585-586</a></span>;
  <em>
   Murphy
  </em>
  v.
  <em>
   Waterfront Commission, supra,
  </em>
  at 79.
 </p>
<p id="b318-7">
  The question presented in the present case is whether a policeman who refuses to waive the protections which the privilege gives him may be dismissed from office because of that refusal.
 </p>
<p id="b318-8">
  About a year and a half after New York City discharged petitioner for his refusal to waive this immunity, we decided
  <em>
   Garrity
  </em>
  v.
  <em>
   New Jersey, 385
  </em>
  U. S. 493 (1967). In that case, we held that when a policeman had been compelled to testify by the threat that otherwise he would be removed from office, the testimony that he gave could not be used against him in a subsequent prosecution. Garrity had not signed a waiver of immunity and no immunity statute was applicable in the circumstances.
  <span citation-index="1" class="star-pagination" label="277"> 
   *277
   </span>
  Our holding was summarized in the following statement (at 500):
 </p>
<blockquote id="b319-5">
  “We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.”
 </blockquote>
<p id="b319-6">
  The New York Court of Appeals considered that
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  did not control the present case. It is true that
  <em>
   <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Garrity</a></span>
  </em>
  related to the attempted use of compelled testimony. It did not involve the precise question which is presented here: namely, whether a State may discharge an officer for refusing to waive a right which the Constitution guarantees to him. The New York Court of Appeals also distinguished our post
  <em>
   -Garrity
  </em>
  decision in
  <em>
   Spevack
  </em>
  v.
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Klein, supra.</a></span>
  </em>
  In
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Spevack</a></span>,
  </em>
  we ruled that a lawyer could not be disbarred solely because he refused to testify at a disciplinary proceeding on the ground that his testimony would tend to incriminate him. The Court of Appeals concluded that
  <em>
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/" aria-description="Citation for case: Spevack v. Klein">Spevack</a></span>
  </em>
  does not control the present case because different considerations apply in the case of a public official such as a policeman. A lawyer, it stated, although licensed by the state is not an employee. This distinction is now urged upon us. It is argued that although a lawyer could not constitutionally be confronted with Hobson’s choice between self-incrimination and forfeiting his means of livelihood, the same principle should not protect a policeman. Unlike the lawyer, he is directly, immediately, and entirely responsible to the city or State which is his employer. He owes his entire loyalty to it. He has no other “client” or principal. He is a trustee of the public interest, bearing
  <span citation-index="1" class="star-pagination" label="278"> 
   *278
   </span>
  the burden of great and total responsibility to his public employer. Unlike the lawyer who is directly responsible to his client, the policeman is either responsible to the State or to no one.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b320-5">
  We agree that these factors differentiate the situations. If appellant, a policeman, had refused to answer questions specifically, directly, and narrowly relating to the performance of his official duties,
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  without being required to waive his immunity with respect to the use of his answers or the fruits thereof in a criminal prosecution of himself,
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra,</a></span>
  </em>
  the privilege against self-incrimination would not have been a bar to his dismissal.
 </p>
<p id="b320-6">
  The facts of this case, however, do not present this issue. Here, petitioner was summoned to testify before a grand jury in an investigation of alleged criminal conduct. He was discharged from office, not for failure to answer relevant questions about his official duties, but for refusal to waive a constitutional right. He was dismissed for failure to relinquish the protections of the privilege against self-incrimination. The Constitution of New York State and the City Charter both expressly provided that his failure to do so, as well as his failure to testify, would result in dismissal from his job. He was dismissed solely for his refusal to waive the immunity to which he is entitled if he is required to testify despite his constitutional privilege;
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra.</a></span>
  </em>
</p>
<p id="b320-7">
  We need not speculate whether, if appellant had executed the waiver of immunity in the circumstances, the effect of our subsequent decision in
  <em>
   Garrity
  </em>
  v.
  <em>
   New <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, supra,</a></span>
  </em>
  would have been to nullify the effect of
  <span citation-index="1" class="star-pagination" label="279"> 
   *279
   </span>
  the waiver. New York City discharged him for refusal to execute a document purporting to waive his constitutional rights and to permit prosecution of himself on the basis of his compelled testimony. Petitioner could not have assumed — and certainly he was not required to assume — that he was being asked to- do an idle act of no legal effect. In any event, the mandate of the great privilege against self-incrimination does not tolerate the attempt, regardless of its ultimate effectiveness, to coerce a waiver of the immunity it confers on penalty of the loss of employment. It is clear that petitioner’s testimony was demanded before the grand jury in part so that it might be used to prosecute him, and not solely for the purpose of securing an accounting of his performance of his public trust. If the latter had been the only purpose, there would have been no reason to seek to compel petitioner to waive his immunity.
 </p>
<p id="b321-5">
  Proper regard for the history and meaning of the privilege against self-incrimination,
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  applicable to the States under our decision in
  <em>
   Malloy
  </em>
  v.
  <em>
   Hogan,
  </em>
  <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), and for the decisions of this Court,
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  dictate the conclusion that the provision of the New York City Charter pursuant to which petitioner was dismissed cannot stand. Accordingly, the judgment is
 </p>
<p id="b321-6">
<em>
   Reversed.
  </em>
</p>
<judges id="b321-7">
  Mr. Justice Black concurs in the result.
 </judges>
<p id="b321-8">
  [For opinion of Mr. Justice Harlan, concurring in the result, see
  <em>
   post,
  </em>
  p. 285.]
 </p>







<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b316-8">
   The Assistant District Attorney said to appellant:
  </p>
<blockquote id="b316-9">
   “You understand . . . that under the Constitution of the United States, as well as the Constitution of New York, no one can be compelled to testify against himself, and that he has a right, the absolute right to refuse to answer any questions that would tend to incriminate him?”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b316-10">
   Appellant was told:
  </p>
<blockquote id="b316-11">
   “You understand . . . that under the Constitution of New York, as well as the Charter of the City of New York, ... a public officer, which includes a police officer, when called before a Grand Jury to answer questions concerning the conduct of his public office and the performance of his duties is required to sign a waiver of immunity if he wishes to retain that public office?”
  </blockquote>
<p id="b316-12">
   The document appellant was asked to sign was phrased as follows:
  </p>
<blockquote id="b316-13">
   “I . . . do hereby waive all benefits, privileges, rights and immunity which I would otherwise obtain from indictment, prosecution, and punishment for or on account of, regarding or relating to any matter, transaction or things, concerning the conduct of my office or the
   <span citation-index="1" class="star-pagination" label="275"> 
    *275
    </span>
   performance of my official duties, or the property, government or affairs of the State of New York or of any county included within its territorial limits, or the nomination, election, appointment or official conduct of any officer of the city or of any such county, concerning any of which matters, transactions or things I may testify or produce evidence documentary or otherwise, before the [blank] Grand Jury in the County of New York, in the investigation being conducted by said Grand Jury.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b317-12">
   That section provides:
  </p>
<blockquote id="b317-13">
   “If any councilman or other officer or employee of the city shall, after lawful notice or process, wilfully refuse or fail to appear before any court or judge, any legislative committee, or any officer, board or body authorized to conduct any hearing or inquiry, or having appeared shall refuse to testify or to answer any question regarding the property, government or affairs of the city or of any county included within its territorial limits, or regarding the nomination, election, appointment or official conduct of any officer or employee of the city or of any such county, on the ground that his answer would tend to incriminate him, or shall refuse to waive immunity from prosecution on account of any such matter in relation to which he may be asked to testify upon .any such hearing or inquiry, his term or tenure of office or employment shall terminate and such office or employment shall be vacant, and he shall not be eligible to election or appointment to any office or employment under the city or any agency.”
  </blockquote>
<p id="b317-14">
   Section 6 of Article I of the New York Constitution provides:
  </p>
<blockquote id="b317-15">
   “No person shall be . . . compelled in any criminal case to be a witness against himself, providing, that any public officer who, upon being called before a grand jury to testify concerning the conduct of his present office ... or the performance of his official duties . . . refuses to sign a waiver of immunity against subsequent criminal prosecution, or to answer any relevant question concerning such matters before such grand jury, shall by virtue of such refusal, be disqualified from holding any other public office or public employment for a period of five years . . . and shall be removed from his present office by the appropriate authority or shall forfeit his present office at the suit of the attorney-general.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b320-8">
   Cf.
   <em>
    Spevack
   </em>
   v.
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/#519" aria-description="Citation for case: Spevack v. Klein"><em>
    Klein, supra,
   </em>
   at 519-520</a></span> (concurring in judgment).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b320-9">
   The statements in my separate opinion in
   <em>
    Spevack
   </em>
   v.
   <span class="citation" data-id="9423320"><a href="/opinion/107337/spevack-v-klein/#519" aria-description="Citation for case: Spevack v. Klein"><em>
    Klein, supra,
   </em>
   at 519-520</a></span>, to which the New York Court of Appeals referred, are expressly limited to situations of this kind.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b321-9">
   See
   <em>
    Miranda
   </em>
   v.
   <em>
    Arizona,
   </em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 458-466</a></span> (1966), and authorities cited therein.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b321-10">
   See,
   <em>
    e. g., Griffin
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965);
   <em>
    Malloy
   </em>
   v.
   <em>
    <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan, supra.</a></span>
   </em>
</p>
</div></div></opinion>
```

---

## GROUP: content/cases/Go-Bart Importing Co. v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Go-Bart Importing Co. v. United States"
type: case
citation: "282 U.S. 344 (1931)"
parallel_cite: "51 S. Ct. 153; 75 L. Ed. 374"
neutral_cite: 1931 U.S. LEXIS 842
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1931
date_decided: 1931-01-05
docket: 111
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1931-01-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Go-Bart Importing Co. v. United States
  varies_by_point: false
  scope_note: "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101643/go-bart-importing-co-v-united-states/"
  cluster_id: 101643
  opinion_id: 101643
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Historical / Foundational"
related: ["[[Chimel v. California]]", "[[Agnello v. United States]]", "[[United States v. Robinson]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "general-search", "historical", "reasonableness"]
holding: "A search incident to arrest may not become a general exploratory search of the premises; a warrantless arrest used to justify ransacking an office for evidence is an unreasonable general search, judged on each case's own facts."
lake:
  record_id: Go-Bart Importing Co. v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Go-Bart Importing Co. v. United States

*282 U.S. 344 (1931)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Prohibition agents, acting on an invalid warrant issued by a commissioner who lacked authority, entered the petitioners' import-company office, arrested Gowen and Bartels, and — under a false claim of having a warrant and by threat of force — compelled Gowen to open his desk and safe. The agents then ransacked the desk, safe, filing cabinets, and other parts of the office, seizing papers, even though they had ample information and time to obtain a valid warrant.

## Issue
Whether a warrantless general search and seizure of papers throughout an office, conducted incident to an arrest, is a reasonable [[Search Incident to Arrest|search incident to arrest]] or an unconstitutional general search.

## Rule
Reasonableness is fact-specific: "There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances." — 282 U.S. at 357. ^pin-357

A [[Search Incident to Arrest|search incident to arrest]] may not become a general rummaging of the premises: by "pretension of right and threat of force he compelled Gowen to open the desk and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found." — *Id.* at 358. ^pin-358

## Application
Unlike *Marron v. United States* — where officers executing a valid warrant seized a ledger and bills that were "visible and accessible and in the offender's immediate custody," with "no threat of force or general search or rummaging" — the agents here arrested the men without seeing any crime, then forced open the desk and safe and ransacked the entire office for evidence under a false claim of authority. That was a general exploratory search, not a permissible incident of the arrest, and was unreasonable.

## Conclusion
Reversed. The general search of the office was unreasonable; the papers had to be suppressed and returned. *Go-Bart* fixes an early outer limit on [[Search Incident to Arrest|search incident to arrest]] — it cannot be converted into a general exploratory search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The general-exploratory-search limit survives and was given its modern structure in [[Chimel v. California]] (SITA confined to the arrestee's person and the area within immediate control); it is companion to [[Agnello v. United States]]. (The Court's contemporaneous "mere evidence" assumptions, drawn from *[[Gouled v. United States|Gouled]]*, were later changed by *[[Warden v. Hayden]]* — but that does not disturb *Go-Bart*'s search-incident-to-arrest holding.)

## Appears on
- [[SIA Persons]] — *Key — Historical / Foundational*

## Sources
- *Go-Bart Importing Co. v. United States*, 282 U.S. 344 (1931) — https://www.courtlistener.com/opinion/101643/go-bart-importing-co-v-united-states/ — pinpoints: 357, 358.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "96f670362bfd7e77", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "282 U.S. 344 (1931)", "court": "U.S. Supreme Court", "neutral_cite": "1931 U.S. LEXIS 842", "official_citation_present": true, "parallel_cite": "51 S. Ct. 153; 75 L. Ed. 374", "title": "Go-Bart Importing Co. v. United States", "year": "1931"}}
{"assertion_id": "0ac9555139740708", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Key — Historical / Foundational", "title": "Go-Bart Importing Co. v. United States"}}
{"assertion_id": "2fee46444b0737e7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search incident to arrest may not become a general exploratory search of the premises; a warrantless arrest used to justify ransacking an office for evidence is an unreasonable general search, judged on each case's own facts.", "title": "Go-Bart Importing Co. v. United States"}}
{"assertion_id": "4dc503517a3574a0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1931-01-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Go-Bart Importing Co. v. United States", "field_i_validity": "good_law", "scope_note": "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California.", "title": "Go-Bart Importing Co. v. United States", "varies_by_point": "false"}}
{"assertion_id": "a505c8f700e21a67", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Go-Bart Importing Co. v. United States"}}
```

### lake record — Go-Bart Importing Co. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Go-Bart Importing Co. v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Go-Bart Importing Co. v. United States",
    "case_name_short": "",
    "case_name_full": "GO-BART IMPORTING COMPANY Et Al. v. UNITED STATES",
    "input_case_name": "Go-Bart Importing Co. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1931-01-05",
    "year": 1931,
    "docket": "111",
    "cluster_id": 101643,
    "lead_opinion_id": 101643,
    "sibling_ids": [
      101643
    ],
    "absolute_url": "/opinion/101643/go-bart-importing-co-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "282 U.S. 344",
      "volume": "282",
      "reporter": "U.S.",
      "page": "344",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "51 S. Ct. 153",
        "volume": "51",
        "reporter": "S. Ct.",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 374",
        "volume": "75",
        "reporter": "L. Ed.",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1931 U.S. LEXIS 842",
        "volume": "1931",
        "reporter": "U.S. LEXIS",
        "page": "842",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "282 U.S. 344",
        "volume": "282",
        "reporter": "U.S.",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 S. Ct. 153",
        "volume": "51",
        "reporter": "S. Ct.",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 374",
        "volume": "75",
        "reporter": "L. Ed.",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1931 U.S. LEXIS 842",
        "volume": "1931",
        "reporter": "U.S. LEXIS",
        "page": "842",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "282 U.S. 344",
    "official_selection": {
      "court_class": "scotus",
      "selected": "282 U.S. 344",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-357",
      "page": null,
      "quote": "--- # Go-Bart Importing Co. v. United States *282 U.S. 344 (1931)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Prohibition agents, acting on an invalid warrant issued by a commissioner who lacked authority, entered the petitioners' import-company office, arrested Gowen and Bartels, and \u2014 under a false claim of having a warrant and by threat of force \u2014 compelled Gowen to open his desk and safe. The agents then ransacked the desk, safe, filing cabinets, and other parts of the office, seizing papers, even though they had ample information and time to obtain a valid warrant. ## Issue Whether a warrantless general search and seizure of papers throughout an office, conducted incident to an arrest, is a reasonable search incident to arrest or an unconstitutional general search. ## Rule Reasonableness is fact-specific:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-358",
      "page": null,
      "quote": "pretension of right and threat of force he compelled Gowen to open the desk and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1931-01-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Go-Bart Importing Co. v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational early limit on search incident to arrest; the principle that a SITA may not become a general exploratory search of the premises survives and was reaffirmed/structured in Chimel v. California.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pacemaker Diagnostic Clinic of America, Inc., a Corporation, Plaintiff- Cross-Appellee v. Instromedix, Inc., a Corporation, Cross-Appellant",
          "cluster_id": 429819,
          "cite": [
            "725 F.2d 537",
            "1984 U.S. App. LEXIS 25408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gill v. State",
          "cluster_id": 1770662,
          "cite": [
            "625 S.W.2d 307",
            "1981 Tex. Crim. App. LEXIS 1283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Superior Court",
          "cluster_id": 5806373,
          "cite": [
            "102 Cal. App. 3d 342",
            "162 Cal. Rptr. 295",
            "1980 Cal. App. LEXIS 1491"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Super Spuds, Inc. v. New York Mercantile Exchange",
          "cluster_id": 9343908,
          "cite": [
            "591 F.2d 174",
            "26 Fed. R. Serv. 2d 1010"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dolan",
          "cluster_id": 6330597,
          "cite": [
            "95 Misc. 2d 470",
            "1978 N.Y. Misc. LEXIS 2449",
            "408 N.Y.S.2d 249"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bianco",
          "cluster_id": 7427525,
          "cite": [
            "55 Cal. App. Supp. 3d 8",
            "127 Cal. Rptr. 92",
            "1975 Cal. App. LEXIS 1842"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. Estelle",
          "cluster_id": 8905678,
          "cite": [
            "493 F.2d 532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Baird",
          "cluster_id": 2118432,
          "cite": [
            "18 Cal. App. 3d 450",
            "95 Cal. Rptr. 700",
            "1971 Cal. App. LEXIS 1399"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coolidge v. New Hampshire",
          "cluster_id": 108377,
          "cite": [
            "29 L. Ed. 2d 564",
            "91 S. Ct. 2022",
            "403 U.S. 443",
            "1971 U.S. LEXIS 25"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. United States",
          "cluster_id": 104605,
          "cite": [
            "93 L. Ed. 2d 153",
            "69 S. Ct. 191",
            "335 U.S. 451",
            "1948 U.S. LEXIS 1456"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freytag v. Commissioner",
          "cluster_id": 112644,
          "cite": [
            "115 L. Ed. 2d 764",
            "111 S. Ct. 2631",
            "501 U.S. 868",
            "1991 U.S. LEXIS 3818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 104422,
          "cite": [
            "67 S. Ct. 1098",
            "331 U.S. 145",
            "91 L. Ed. 1399",
            "1947 U.S. LEXIS 2936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "See v. City of Seattle",
          "cluster_id": 107474,
          "cite": [
            "18 L. Ed. 2d 943",
            "87 S. Ct. 1737",
            "387 U.S. 541",
            "1967 U.S. LEXIS 1255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cobbledick v. United States",
          "cluster_id": 103311,
          "cite": [
            "309 U.S. 323",
            "60 S. Ct. 540",
            "84 L. Ed. 783",
            "1940 U.S. LEXIS 1091",
            "1940 Trade Cas. (CCH) 56,011"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Go-Bart Importing Co. v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101643) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0tMjM1ODcyMDAwMDAmcz0yODQyNzEmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101643%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(101643)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzEmcz0xMTIyMDQzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28101643%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101643)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(101643)",
    "indexed_citing_opinions": 589,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101643,
        "count": 589,
        "count_source": "search"
      }
    ],
    "citation_count": 885,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/go-bart-importing-co-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUxOTcyODUmcz00MzIwNzMxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101643%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101643,
        "cited_id": 84827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 90713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 92143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 94408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 95422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 95722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 97412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99525,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 101354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101643,
        "cited_id": 2425305,
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
    "date_created": "2026-07-05T05:36:41Z",
    "date_modified": "2026-07-06T07:51:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:40:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:36:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Go-Bart Importing Co. v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b412-5">
<span citation-index="1" class="star-pagination" label="348"> 
   *348
   </span>
  Mr. Justice Butler
 </author>
<p id="A9G">
  delivered the opinion of the Court.
 </p>
<p id="b412-6">
  In a criminal proceeding before a United States commissioner in the Southern District of New York in which Gowen, Bartels and others are defendants, the petitioners applied to the district court for an order enjoining the use as evidence of books and papers alleged to have been seized and taken from petitioners in violation' of the Fourth and Fifth Amendments and directing their return. The court made an order that the United States show' cause why the relief prayed should not be granted. The United States attorney appeared and opposed the motion, and affidavits of W. J. Calhoun, special agent in charge of special agents of the Bureau of Prohibition, and certain of his subordinates were filed in opposition. The district court denied the applications. The Circuit Court of Appeals affirmed as to the United States attorney and held that as to the special agent in charge the order to show cause should have been discharged. 40 F. (2d) 593.
 </p>
<p id="b412-7">
  Petitioners’ applications to the district court, which are in form affidavits, set forth the following:
 </p>
<p id="b413-2">
<span citation-index="1" class="star-pagination" label="349"> 
   *349
   </span>
  June 5, 1929, Calhoun went before the United States commissioner and, in order to have a warrant issued for the arrest of Gowen, Bartels and others, yerified and filed a complaint. He alleged, upon information and belief, that beginning January 1, 1929, and continuing down to the filing of the complaint Gowen, Bartels and other defendants conspired in that district to commit/ a nuisance against the United States, that is to say, to possess, transport, sell and solicit and receive orders for intoxicating liquor in violation of the National. Prohibition Act, and that, in pursuance of the conspiracy .and to effqct its objects, one Heath purchased an automobile on May 23, 1929. See <span class="citation no-link">27 U. S. C., §§ 33</span>, 35. The complaint did not specify any building, structure, location or place or set forth any particulars or other overt act or show any connection between the purchase of the automobile and any offense referred to in the complaint. On the same day the commissioner issued a warrant in the usual form commanding the marshal of the district and his deputies to apprehend the persons so accused and to bring them before the commissioner or some judge or justice of the United States to be dealt with according to law.
 </p>
<p id="b413-3">
  On the next day Calhoun's subordinates, prohibition agents O’Brien, Collins and Sipe, went to the petitioning company’s office at No. 200 Fifth Avenue. Bartels, the secretary-treasurer of the company, was there when they entered. O’Brien said he had a warrant to search the premises and exhibited a paper which he falsely claimed was such a warrant. The agents arrested Bartels, searched his person and took papers therefrom. While they were there Gowen, the president of the company, came to the office. O’Brien told him that he had a warrant for his arrest and a warrant to search the premises. The agents, arrested and searched Gowen and took papers from him. They took his keys and by threat of force compelled him to open a desk and safe, searched and took papers from
  <span citation-index="1" class="star-pagination" label="350"> 
   *350
   </span>
  them, searched other parts of the office and took therefrom other papers, journals, account books, letter files, insurance policies, cancelled checks, index cards and other things belonging respectively to.Gowen, Bartels and the company. For brevity these will be referred to herein as “ papers.”
 </p>
<p id="b414-4">
  Gowen and Bartels were on the same day arraigned before the commissioner and held on bail further to answer the complaint. A date was set for the examination, hearing has been postponed from time to time and no examination has been had. The paper's so seized were taken to the office of Calhoun in the Sub-Treasury Building where they were examined by him and the United States at-' torney and their subordinates, and such papers have since been kept and held there, as is later herein shown, under the control of the United States attorney in the care and custody of the special agent in charge, for use as evidence against Gowen and Bartels.
 </p>
<p id="b414-5">
  Soon after the seizures were made each of the petitioners brought a suit in equity in the federal court for that district against the special agent in charge and the United States attorney, to enjoin them from using such papers as evidence and to have them returned. The court dismissed these suits' on the ground that the proper remedy was by motion in the criminal proceedings.
 </p>
<p id="b414-6">
  Then Gowen and Bartels, each in his own behalf, and the company, acting through Bartels, made these applications. The court made its order that the United States show cause why an injunction should not issue restraining it and its officers from using as evidence the papers so seized and why an order should not issue directing their return.
 </p>
<p id="b414-7">
  ■ • In opposition, the affidavit of one Braidwood was submitted. It tends to show that in 1927. and 1928 petitioners and others acting together engaged in the unlawful sale of intoxicating liquor, that at the company’s office
  <span citation-index="1" class="star-pagination" label="351"> 
   *351
   </span>
  they exhibited and took orders for intoxicating- liquor some of which was delivered there and some elsewhere, and that in April,. 1929, he reported these facts to Calhoun. Calhoun’s affidavit states that Braidwood had so reported and that by independent investigations he had corroborated such statements and thus knew that a conspiracy unlawfully to sell intoxicating liquors in 1928 and 1929 had been entered into and overt acts in furtherance thereof had been performed within- the district and that he believed the petitioners had been parties to such conspiracy, that prior to the day of the arrests he communicated such statements and belief to O’Brien and assigned him to further investigate the case.
 </p>
<p id="b415-3">
  O’Brien’s affidavit states: From the information given him by Calhoun he believed petitioners and others had so conspired. Calhoun described to him the company’s office in detail and the personal appearance of Gowen and Bartels. On June 6, 1929, he took a certified copy of the complaint and warrant “ for the purpose of reference, as to the names of the various defendants ” and went to petitioners’ office. It-consisted of a suite of three rooms fitted up with office ..furniture including desks, filing cabinets and a safe. He told Bartels and Gowen that he was an officer of the United States and placed them under arrest, for such conspiracy. No warrant was “ served ” upon either of them. The office was searched and there were found and taken therefrom approximately a dozen-bottles of assorted intoxicating liquor, a large number of memo-randa, books of account, records, filing cases, and other papers all of which, pertained to unlawful dealings by Gowen and Bartels in intoxicating liquors.
 </p>
<p id="b415-4">
  O’Brien’s affidavit also states that the papers so seized are of such quantity and bulk that it is impracticable to attach copies to-the affidavit, that such papers are “ specifically incorporated herein by reference and made a part hereof and are further made ayailable for inspection at
  <span citation-index="1" class="star-pagination" label="352"> 
   *352
   </span>
  any time, if desired by the Court, in connection with the consideration of this order to show cause.”
 </p>
<p id="b416-5">
  In reply to O’Brien’s affidavit petitioners submitted affidavits of,. Gowen, Bartels and other defendants who were arrested at the company’s office on that occasion and affidavits of. other persons who were present during some part of the time that the prohibition agents were there. These affidavits show that O’Brien said he had a warrant of arrest and produced a paper which several of these affiants say they read and believe to be the warrant issued by the commissioner, a copy bf which was filed with the moving papers. As to these details there is no conflict in the evidence.
 </p>
<p id="AYZ9">
  The district court refused to sustain the contention that no use was made of thé warrant and accepted the state- ■ ments that O’Brien claimed to have warrants for the arrests and searches. The Circuit Court of Appeals did not definitely express opinion as to that matter. We have examined the evidence. It requires a finding that O’Brien did so claim, that he had the warrant issued by the commissioner or a copy of it and that when he arrested Gowen and Bartels he claimed and purported to act under the warrant. No warrant for the search of the premises was issued.
 </p>
<p id="b416-7">
  The orders dismissing petitioners’ suits in equity are not before us. The question whether the district court had jurisdiction summarily-to deal with petitioners’ applications, while not brought forward by the parties, arises upon the record, was considered by the Circuit Court of Appeals and suggested during the argument here.
 </p>
<p id="b416-8">
  United States, commissioners are inferior officers.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
<em>
   United States
  </em>
  v.
  <em>
   Allred,
  </em>
  <span class="citation" data-id="94069"><a href="/opinion/94069/united-states-v-allred/#594" aria-description="Citation for case: United States v. Allred">155 U. S. 591, 594</a></span>.
  <em>
   Rice
  </em>
  v.
  <em>
   Ames,
  </em>
<span citation-index="1" class="star-pagination" label="353"> 
   *353
   </span>
  <span class="citation" data-id="95422"><a href="/opinion/95422/rice-v-ames/#377" aria-description="Citation for case: Rice v. Ames">180 U. S. 371, 377, 378</a></span>. Cf.
  <em>
   Ex parte Hennen,
  </em>
  <span class="citation" data-id="2518125"><a href="/opinion/2518125/ex-parte-duncan-n-hennen/#257" aria-description="Citation for case: Ex Parte Duncan N. Hennen">13 Pet. 230, 257</a></span>,
  <em>
   et seg.
  </em>
  The Act of May 28, 1896, <span class="citation no-link">29 Stat. 184</span>, abolished commissioners of the circuit courts, authorized each district court to appoint United States commissioners, gave to them the same powers and duties that commissioners of the circuit courts had, required such appointments to be entered of record in the district courts, provided that the commissioners should hold their office subject to removal by the court appointing them (<span class="citation no-link">28 U. S. C., § 526</span>) and required them to keep records of proceedings before them in criminal cases and deliver the same to the clerks of the courts on the commissioners’ ceasing to hold office.
  <em>
   <span class="citation no-link">Id.,</span>
  </em>
  § 529. They are authorized by statute in respect of numerous matters
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and the relations between them and the district courts vary as do their official acts. Cf.
  <em>
   United States
  </em>
  v.
  <em>
   Allred, ubi supra. Grin
  </em>
  v.
  <em>
   Shine,
  </em>
  <span class="citation" data-id="95722"><a href="/opinion/95722/grin-v-shine/#187" aria-description="Citation for case: Grin v. Shine">187 U. S. 181, 187</a></span>.
  <em>
   Todd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94212"><a href="/opinion/94212/todd-v-united-states/#282" aria-description="Citation for case: Todd v. United States">158 U. S. 278, 282</a></span>.
  <em>
   Collins
  </em>
  v.
  <em>
   Miller,
  </em>
  <span class="citation" data-id="99554"><a href="/opinion/99554/collins-v-miller/#369" aria-description="Citation for case: Collins v. Miller">252 U. S. 364, 369</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Berry,
  </em>
  <span class="citation" data-id="8121751"><a href="/opinion/8160102/united-states-v-berry/" aria-description="Citation for case: United States v. Berry">4 Fed. 779</a></span>.
  <em>
   Ex parte
  </em>
  Perkins, <span class="citation" data-id="8310779"><a href="/opinion/8342362/ex-parte-perkins/" aria-description="Citation for case: Ex parte Perkins">29 Fed. 900</a></span>.
  <em>
   The Mary,
  </em>
  <span class="citation" data-id="8799626"><a href="/opinion/8815150/the-mary/" aria-description="Citation for case: The Mary">233 Fed. 121</a></span>.
 </p>
<p id="b417-3">
  We need not consider what power the district court may exert over the commissioners dealing with matters unlike
  <span citation-index="1" class="star-pagination" label="354"> 
   *354
   </span>
  that now before us. Here the commissioner acted under R.'S., § 1014, which provides that for any crime or offense against the'United. States, the offender may by any justice or judge of the United States or by any commissioner of the circuit court to take bail (now United States commissioner) be arrested and imprisoned, or bailed, as the "case may be, for trial before such court of the United States as by law has cognizance of the offense. <span class="citation no-link">18 U. S. C., § 591</span>. All the commissioner’s acts and the things doné by the prohibition officers in respect of this matter were preparatory and preliminary to a consideration of the charge by a grand jury and, if an indictment should be found, the final disposition of the case in the district court. The commissioner acted not as a court, or as a judge of any court, but as a mere officer of the district court in proceedings of which that court had authority to take control at any time.
  <em>
   Todd
  </em>
  v.
  <em>
   United States, ubi supra. Collins
  </em>
  v.
  <em>
   Miller, ubi supra. United States
  </em>
  v.
  <em>
   <span class="citation" data-id="8121751"><a href="/opinion/8160102/united-states-v-berry/" aria-description="Citation for case: United States v. Berry">Berry, supra.</a></span> United States
  </em>
  v.
  <em>
   Casino,
  </em>
  <span class="citation" data-id="8829038"><a href="/opinion/8843817/united-states-v-casino/#979" aria-description="Citation for case: United States v. Casino">286 Fed. 976, 979</a></span>.
 </p>
<p id="Aba1">
  Notwithstanding the order to show cause was addressed to the United States alone, this is in substance and effect a proceeding against the United States attorney and the special agent in charge. The special agent in charge was the prosecuting witness. It was his duty under the statute to report violations to the United States attorney.
  <em>
   Donnelley
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101264"><a href="/opinion/101264/donnelley-v-united-states/" aria-description="Citation for case: Donnelley v. United States">276 U. S. 505</a></span>. And he was authorized, subject to. the control of the United States attorney, to “ conduct the prosecution at the committing trial for the purpose of having the offenders held for the action of a grand jury,” <span class="citation no-link">27 U. S. C., § 11</span>. It is immaterial whether he intended or was personally to conduct the prosecution before the commissioner. As the United States attorney had control of the prosecution‘before the commissioner, whether conducted by his assistants or prohibition agents, the papers were held subject to his control and direction although in the immediate care and custody
  <span citation-index="1" class="star-pagination" label="355"> 
   *355
   </span>
  of the prohibition officers. He and they voluntarily came before the court to defend the seizure, the retention and proposed use of the papers and so in effect became parties to the proceeding. By making the papers a part of O’Brien’s affidavit they brought the papers within the power of the court and constructively into its possession, if indeed the papers had not already come within its reach. In so far as it purports to run .against the United States, the form of the order may be treated as a mere irregularity.
 </p>
<p id="b419-3">
  The United States attorney and the special agent in charge, as officers authorized to conduct such prosecution and having .control and custody of the papers for that purpose, are, in respect of the acts relating to such prosecution, alike subject to the proper exertion of the disciplinary powers of the court. And on the facts here shown it is plain that the district court had jurisdiction summarily to determine whether the evidence should be suppressed and the papers returned to the petitioners.
  <em>
   Weeks
  </em>
  v.
  <em>
   United
  </em>
  States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span>.
  <em>
   Wise
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="97412"><a href="/opinion/97412/wise-v-henkel/#558" aria-description="Citation for case: Wise v. Henkel">220 U. S. 556, 558</a></span>.
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#390" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 390</a></span>.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States
  </em>
  <span class="citation" data-id="101354"><a href="/opinion/101354/cogen-v-united-states/#225" aria-description="Citation for case: Cogen v. United States">278 U. S. 221, 225</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Mills,
  </em>
  <span class="citation" data-id="8778272"><a href="/opinion/8794247/united-states-v-mills/" aria-description="Citation for case: United States v. Mills">185 Fed. 318</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   McHie,
  </em>
  <span class="citation" data-id="8782452"><a href="/opinion/8798345/united-states-v-mchie/#898" aria-description="Citation for case: United States v. McHie">194 Fed. 894, 898</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Lydecker,
  </em>
  <span class="citation" data-id="8822257"><a href="/opinion/8837179/united-states-v-lydecker/#980" aria-description="Citation for case: United States v. Lydecker">275 Fed. 976, 980</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Kraus,
  </em>
  <span class="citation" data-id="8819275"><a href="/opinion/8834265/united-states-v-kraus/#580" aria-description="Citation for case: United States v. Kraus">270 Fed. 578, 580</a></span>. Cf.
  <em>
   Applybe
  </em>
  v.
  <em>
   United States,
  </em>
  32 F. (2d) 873, 874.
 </p>
<p id="b419-4">
  The Government concedes that the warrant did not authorize O’Brien or other prohibition agents to make the arrests. The complaint, which in substance is recited in the warrant, was verified,merely on information and belief and does not state facts sufficient to constitute an offense.
  <em>
   Ex parte Burford,
  </em>
  <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/#453" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448,453</a></span>.
  <em>
   Rice
  </em>
  v.
  <span class="citation" data-id="95422"><a href="/opinion/95422/rice-v-ames/#374" aria-description="Citation for case: Rice v. Ames"><em>
   Ames, supra,
  </em>
  374</a></span>.
  <em>
   Byars
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Cruikshank,
  </em>
  <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#558" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542, 558</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Hess,
  </em>
  <span class="citation" data-id="92143"><a href="/opinion/92143/united-states-v-hess/" aria-description="Citation for case: United States v. Hess">124 U. S. 483</a></span>.
  <em>
   United States
  </em>
  v.
  <em>
   Ruroede,
  </em>
  <span class="citation" data-id="8794535"><a href="/opinion/8810183/united-states-v-ruroede/" aria-description="Citation for case: United States v. Ruroede">220 Fed. 210</a></span>,
  <span citation-index="1" class="star-pagination" label="356"> 
   *356
   </span>
  212, 213. The warrant was improvidently issued and invalid on its face. It does not purport to authorize anyone other than the marshal and his deputies.
 </p>
<p id="b420-5">
  The company is not mentioned in the complaint or warrant and is a stranger to the proceeding before the commissioner. Unquestionably the order of the district court as to it was final and appealable.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States, ubi supra. Ex parte Tiffany,
  </em>
  252 U., S. 32.
  <em>
   Savannah
  </em>
  v.
  <em>
   Jesup,
  </em>
  <span class="citation" data-id="9417350"><a href="/opinion/90713/savannah-v-jesup/" aria-description="Citation for case: Savannah v. Jesup">106 U. S. 563</a></span>.
  <em>
   Gumbel
  </em>
  v.
  <em>
   Pitkin,
  </em>
  <span class="citation" data-id="2425305"><a href="/opinion/2425305/gumbel-v-pitkin/" aria-description="Citation for case: Gumbel v. Pitkin">113 U. S. 545</a></span>: When the application was made, no information or indictment had been found'or returned against Gowen or Bartels. There was nothing to show that any criminal proceeding would ever be instituted in that court against them.
  <em>
   Post
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94408"><a href="/opinion/94408/post-v-united-states/#587" aria-description="Citation for case: Post v. United States">161 U. S. 583, 587</a></span>. And, as above shown, the complaint does not state an offense. It follows that the order of the district court was not made in. or dependent upon any case or proceeding there pending and therefore the order as to them was appealable.
  <em>
   Cogen
  </em>
  v.
  <em>
   United States, ubi supra. Perlman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99162"><a href="/opinion/99162/perlman-v-united-states/#13" aria-description="Citation for case: Perlman v. United States">247 U. S. 7, 13</a></span>.
  <em>
   Burdeau
  </em>
  v.
  <em>
   McDowell,
  </em>
  <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>.
 </p>
<p id="b420-6">
  Without pausing to consider the matter, we assume, as held by the lower courts, that the facts of which Calhoun and O’Brien, had been informed prior to the arrests are sufficient to justify the apprehension without a warrant of Gowen and Bartels for the conspiracy referred to in Braidwood’s affidavit and on that basis we treat the arrests as lawful and valid.
 </p>
<p id="b420-7">
  No question is here raised as to the search of the persons. There remains for consideration the question whether the search of the premises, the seizure of the papers therefrom and their retention for use as evidence may. be sustained. The first, clause of the Fourth Amendment declares: “ The right of the people to be se
  <span citation-index="1" class="star-pagination" label="357"> 
   *357
   </span>
  cure in their persons, houses, papers, and effects, against unreasonable searches and seizures sh^ll not be violated.” It is general and forbids every search that is unreasonable; it protects all, those suspected or known to be offenders as well as the innocent, and unquestionably extends to the premises where the search was made and the papers taken.
  <em>
   Gouled
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#307" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 307</a></span>. The second clause declares: “ and no Warrants shall issue, but upon probable cause, supported by’ Oath or affirmation, ,and particularly describing the place to be searched, and the persons or things to be seized.” This prevents the issue of warrants on loose, vague or doubtful bases of. fact. It emphasizes the purpose to protect against all general searches. Since before the creation of our government, such searches have been deemed obnoxious to fundamental principles of liberty. They are denounced in the constitutions or statutes of every State in the Union.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. The need of protection against them is attested alike by history and present conditions. The Amendment is to be liberally construed and all owe the duty of vigilance for its effective enforcement lest there shall be impairment of the rights for the protection of which it was adopted.
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623</a></span>.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  389-92.
 </p>
<p id="b421-4">
  There is no formula for the determination of reasonableness. Each case is to be decided on its own facts and circumstances. It is not, and could not be, claimed that the officers saw conspiracy being committed. And there is no suggestion that Gowen or Bartels was committing crime when arrested. In April, 1929, Braidwood reported to Calhoun the existence of a conspiracy and that in pursuance of it sales and deliveries of intoxicating liquor had been made in 1927 and 1928. The record does not show
  <span citation-index="1" class="star-pagination" label="358"> 
   *358
   </span>
  any criminal overt act in 1929. Calhoun's description to O'Brien of the company’s office in detail and of Gowen and Bartels shows that he knew the place and offenders. Notwithstanding he had. an abundance of information and time to swear out a valid warrant, he failed to do so. O'Brien falsely claimed to have a warrant ’or the search of the premises and he made the arrests under color of the invalid warrant.. By pretension of right and threat of force he compelled Gowen to open the desk ,and the safe and with the others made a general and apparently unlimited search, ransacking the desk, safe, filing cases and other parts of the office. It was a lawless invasion of the premises and a general exploratory search in the hope that evidence of crime might be found.
  <em>
   Federal Trade Commission
  </em>
  v.
  <em>
   American Tobacco Co.,
  </em>
  <span class="citation" data-id="100375"><a href="/opinion/100375/federal-trade-commission-v-american-tobacco-co/#306" aria-description="Citation for case: Federal Trade Commission v. American Tobacco Co.">264 U. S. 298, 306</a></span>.
 </p>
<p id="A28">
  Plainly the case before us is essentially different from
  <em>
   Marrón
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span>.. There, officers executing a valid search warrant for intoxicating liquors found and arrested one Birdsall who in pursuance of a conspiracy was actually engaged in running a saloon. As an incident to the arrest they seized a ledger in a closet where the. liquor or some of it was kept and some bills beside the cash register. These things were visible and accessible and in the offender’s immediate custody. There was no threat of force or general search or rummaging of the place.
 </p>
<p id="b422-5">
  The .uncontradicted evidence requires a finding that here the search of the premises was unreasonable.
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra. Marron
  </em>
  v.
  <em>
   United States, supra,
  </em>
  199.
  <em>
   United States
  </em>
  v.
  <em>
   Kirschenblatt,
  </em>
  16 F. (2d) 202. The judgments below must be reversed and the case remanded to the district court with directions to enjoin the United States attorney and the special agent in charge from using the papers as evidence id to order the same returned to petitioners.
 </p>
<p id="b422-6">
<em>
   Reversed.
  </em>
</p>

<div class="footnotes"><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b417-4">
   The powers and duties of United States commissioners include: To arrest and imprison, or bail, for trial (18 U. S. C., ■§ 591; see also §§ 593-597) and in certain cases to take recognizances from witnesses on preliminary hearings • (<span class="citation no-link">28 U. S. C., § 657</span>); to issue warrants for and examine persons charged with being fugitives from justice (18 U. S. C., § .651); to hold to security of the peace and for good behavior (28 U. ,S. C., § 392); to issue search warrants (<span class="citation no-link">18 U. S. C., §§ 611-627</span>; <span class="citation no-link">26 U. S. C., § 1195</span>); to take bail and affidavits in civil causes (<span class="citation no-link">28 U. S. C., § 758</span>); to discharge poor uonvicts imprisoned for non-payment of fines (<span class="citation no-link">18 U. S. C., § 641</span>); to institute prosecutions under laws relating to the elective franchise and civil rights and to appoint persons to execute warrants thereunder (<span class="citation no-link">8 U. S. C., §§ 49</span>, 50); to enforce arbitration awards of foreign consuls in disputes between captains and crews of foreign vessels (<span class="citation no-link">28 U. S. C., § 393</span>); to summon master of ship to show cause why process should not issue against it for seaman’s wages (46 U. S. C., § '603); to take oaths and acknowledgments. <span class="citation no-link">5 U. S. C., § 92</span>,' 28 U. Sv C., § 525.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Gooding v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Gooding v. United States"
type: case
citation: "416 U.S. 430 (1974)"
parallel_cite: "94 S. Ct. 1780; 40 L. Ed. 2d 250"
neutral_cite: 1974 U.S. LEXIS 133
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-04-29
docket: 72-6902
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-04-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gooding v. United States
  varies_by_point: false
  scope_note: "Statutory holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction stands. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109017/gooding-v-united-states/"
  cluster_id: 109017
  opinion_id: 109017
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Related (nighttime execution)"
related: []
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "warrant-execution", "nighttime-search", "narcotics"]
holding: "Under 21 U.S.C. § 879(a), a narcotics search warrant may be executed at night with no special showing of need beyond probable cause that the contraband is likely to be on the premises at that time."
lake:
  record_id: Gooding v. United States
  status: verified
  projected_at: 2026-07-09
---

# Gooding v. United States

*416 U.S. 430 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
District of Columbia Metropolitan Police, armed with a warrant to search Gooding's apartment for narcotics, executed it at roughly 9:30 p.m. and seized a substantial quantity of contraband. The supporting affidavit stated that the officer was "positive" Gooding was secreting narcotics in the apartment and described continuing drug traffic plus a prior controlled purchase. Gooding moved to suppress, arguing the nighttime seizure violated the governing statutory restrictions on after-dark search-warrant execution.

## Issue
Which statute governs nighttime execution of a federal narcotics search warrant, and what showing it requires — specifically, whether 21 U.S.C. § 879(a) demands a special justification for searching at night beyond probable cause that the contraband is present.

## Rule
The narcotics-specific statute, 21 U.S.C. § 879(a), controls rather than Federal Rule of Criminal Procedure 41 or the D.C. Code daytime-service provisions. Section 879(a) permits service "at any time of the day or night" so long as the issuing authority "is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." — 416 U.S. at 439. ^pin-439

"We therefore conclude that 21 U.S.C. § 879(a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time." — *Id.* at 458. ^pin-458

## Application
The affidavit supporting Gooding's warrant "suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available." That was "sufficient to satisfy 21 U.S.C. § 879(a)," so the 9:30 p.m. execution was lawful and the seized contraband was admissible. — [416 U.S. at 458](https://www.courtlistener.com/opinion/109017/gooding-v-united-states/#:~:text=suggested%20that%20there%20was%20a). ^pin-458b

## Conclusion
The nighttime narcotics search was authorized under § 879(a) on the showing made; the Court of Appeals' judgment upholding the search was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Gooding* is a statutory-construction holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction governs nighttime execution of federal narcotics warrants.

## Appears on
- [[Scope Manner and Related Issues]] — *Related (nighttime execution)*

## Sources
- *Gooding v. United States*, 416 U.S. 430 (1974) — https://www.courtlistener.com/opinion/109017/gooding-v-united-states/ — pinpoints: 439, 458.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e714d7a87b95f305", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "416 U.S. 430 (1974)", "court": "U.S. Supreme Court", "neutral_cite": "1974 U.S. LEXIS 133", "official_citation_present": true, "parallel_cite": "94 S. Ct. 1780; 40 L. Ed. 2d 250", "title": "Gooding v. United States", "year": "1974"}}
{"assertion_id": "1acddf8951b7246e", "dimension": "support", "kind": "home_role", "locator": {"home": "Scope Manner and Related Issues"}, "payload": {"home": "Scope Manner and Related Issues", "role": "Related (nighttime execution)", "title": "Gooding v. United States"}}
{"assertion_id": "2ea64381e3ded161", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under 21 U.S.C. § 879(a), a narcotics search warrant may be executed at night with no special showing of need beyond probable cause that the contraband is likely to be on the premises at that time.", "title": "Gooding v. United States"}}
{"assertion_id": "5a7bf1bc9ca1da7b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1974-04-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Gooding v. United States", "field_i_validity": "good_law", "scope_note": "Statutory holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction stands. Good law.", "title": "Gooding v. United States", "varies_by_point": "false"}}
{"assertion_id": "b0102ecafa2b14e2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gooding v. United States"}}
```

### lake record — Gooding v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gooding v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gooding v. United States",
    "case_name_short": "Gooding",
    "case_name_full": "Gooding v. United States",
    "input_case_name": "Gooding v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-04-29",
    "year": 1974,
    "docket": "72-6902",
    "cluster_id": 109017,
    "lead_opinion_id": 109017,
    "sibling_ids": [
      109017,
      9425696,
      9425697,
      9425698
    ],
    "absolute_url": "/opinion/109017/gooding-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "416 U.S. 430",
      "volume": "416",
      "reporter": "U.S.",
      "page": "430",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 1780",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1780",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 250",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 133",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 U.S. 430",
        "volume": "416",
        "reporter": "U.S.",
        "page": "430",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 1780",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1780",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 250",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 133",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "416 U.S. 430",
    "official_selection": {
      "court_class": "scotus",
      "selected": "416 U.S. 430",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-439",
      "page": null,
      "quote": "Gooding was secreting narcotics in the apartment and described continuing drug traffic plus a prior controlled purchase. Gooding moved to suppress, arguing the nighttime seizure violated the governing statutory restrictions on after-dark search-warrant execution. ## Issue Which statute governs nighttime execution of a federal narcotics search warrant, and what showing it requires \u2014 specifically, whether 21 U.S.C. \u00a7 879(a) demands a special justification for searching at night beyond probable cause that the contraband is present. ## Rule The narcotics-specific statute, 21 U.S.C. \u00a7 879(a), controls rather than Federal Rule of Criminal Procedure 41 or the D.C. Code daytime-service provisions. Section 879(a) permits service",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-458",
      "page": null,
      "quote": "We therefore conclude that 21 U.S.C. \u00a7 879(a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-458b",
      "page": null,
      "quote": "suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available.",
      "star_marker": "458",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 29625,
      "fragment": "#:~:text=suggested%20that%20there%20was%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-04-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gooding v. United States",
    "varies_by_point": false,
    "scope_note": "Statutory holding interpreting 21 U.S.C. \u00a7 879(a); the statute remains in force and the construction stands. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Richard J. Rizzi",
          "cluster_id": 792946,
          "cite": [
            "434 F.3d 669",
            "2006 U.S. App. LEXIS 450",
            "2006 WL 39266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Rome v. United States",
          "cluster_id": 110248,
          "cite": [
            "64 L. Ed. 2d 119",
            "100 S. Ct. 1548",
            "446 U.S. 156",
            "1980 U.S. LEXIS 123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alejandrina Torres",
          "cluster_id": 446389,
          "cite": [
            "751 F.2d 875"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antoine Jones v. Steve Kirchner",
          "cluster_id": 4251490,
          "cite": [
            "835 F.3d 74",
            "2016 U.S. App. LEXIS 15759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Wayne Searp",
          "cluster_id": 360886,
          "cite": [
            "586 F.2d 1117",
            "58 A.L.R. Fed. 743",
            "1978 U.S. App. LEXIS 7945"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. State",
          "cluster_id": 2386467,
          "cite": [
            "782 A.2d 862",
            "366 Md. 121",
            "2001 Md. LEXIS 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burch, Larry D.",
          "cluster_id": 184680,
          "cite": [
            "156 F.3d 1315",
            "332 U.S. App. D.C. 287",
            "50 Fed. R. Serv. 3d 1",
            "1998 U.S. App. LEXIS 24913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1995209,
          "cite": [
            "742 N.W.2d 163",
            "2007 Minn. LEXIS 756",
            "2007 WL 4261169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lien",
          "cluster_id": 1719873,
          "cite": [
            "265 N.W.2d 833",
            "1978 Minn. LEXIS 1353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawson",
          "cluster_id": 1512232,
          "cite": [
            "502 F. Supp. 158",
            "1980 U.S. Dist. LEXIS 14227"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patrick Harm Keene",
          "cluster_id": 548987,
          "cite": [
            "915 F.2d 1164",
            "31 Fed. R. Serv. 64",
            "1990 U.S. App. LEXIS 16882",
            "1990 WL 138148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Richard Tedford",
          "cluster_id": 523577,
          "cite": [
            "875 F.2d 446",
            "1989 U.S. App. LEXIS 7870",
            "1989 WL 56819"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Yanez-Marquez v. Loretta Lynch",
          "cluster_id": 2808824,
          "cite": [
            "789 F.3d 434",
            "2015 U.S. App. LEXIS 10107",
            "2015 WL 3719105"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 1757509,
          "cite": [
            "665 So. 2d 1237",
            "1995 WL 713755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1149871,
          "cite": [
            "617 P.2d 1117",
            "1980 Alas. LEXIS 721"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roth v. State",
          "cluster_id": 898092,
          "cite": [
            "2007 ND 112",
            "735 N.W.2d 882",
            "2007 N.D. LEXIS 125",
            "2007 WL 2120566"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brock",
          "cluster_id": 1188105,
          "cite": [
            "653 P.2d 543",
            "294 Or. 15",
            "1982 Ore. LEXIS 1281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. Superior Court",
          "cluster_id": 2180261,
          "cite": [
            "199 Cal. App. 3d 1453",
            "245 Cal. Rptr. 617",
            "1988 Cal. App. LEXIS 309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 1995384,
          "cite": [
            "742 N.W.2d 149",
            "2007 Minn. LEXIS 752",
            "2007 WL 4259511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seth Mason and Carl Peterson v. United States",
          "cluster_id": 426314,
          "cite": [
            "719 F.2d 1485",
            "14 Fed. R. Serv. 817",
            "1983 U.S. App. LEXIS 15900"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Grimshaw",
          "cluster_id": 2219758,
          "cite": [
            "595 N.E.2d 302",
            "413 Mass. 73",
            "1992 Mass. LEXIS 388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Porco",
          "cluster_id": 1461438,
          "cite": [
            "842 F. Supp. 1393",
            "1994 U.S. Dist. LEXIS 869",
            "1994 WL 22574"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rowe",
          "cluster_id": 1379495,
          "cite": [
            "806 P.2d 730",
            "154 Utah Adv. Rep. 12",
            "1991 Utah App. LEXIS 15",
            "1991 WL 17377"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 2,
        "triage_snippet_classified": 46
      },
      "lane2_top_cited": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02JnM9MTgxMTkxNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109017+OR+9425696+OR+9425697+OR+9425698%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
    "indexed_citing_opinions": 65,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109017,
        "count": 61,
        "count_source": "search"
      },
      {
        "opinion_id": 9425696,
        "count": 5,
        "count_source": "search"
      },
      {
        "opinion_id": 9425697,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425698,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 98,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gooding-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjEzMDU1Mjkmcz0yOTY4MjQ3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109017+OR+9425696+OR+9425697+OR+9425698%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109017,
        "cited_id": 101357,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 102494,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 104671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 106253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 260559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 270626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 285611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 310420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 2293098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 2307321,
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
    "date_created": "2026-07-05T05:40:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:45:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gooding v. United States

```
<div>
<center><b><span class="citation" data-id="9425696"><a href="/opinion/109017/gooding-v-united-states/" aria-description="Citation for case: Gooding v. United States">416 U.S. 430</a></span> (1974)</b></center>
<center><h1>GOODING<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 72-6902.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1974.</center>
<center>Decided April 29, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*431</span> <i>Herbert A. Rosenthal,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./414/998/">414 U. S. 998</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen, Edward R. Korman,</i> and <i>Jerome M. Feit.</i></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Petitioner in this case presents a claim that evidence offered against him at his trial should have been suppressed because it was seized at nighttime in violation of governing statutory provisions. The search which led to the seizure was conducted by officers of the District of Columbia Metropolitan Police Department at approximately 9:30 p. m. within the District of Columbia. <span class="star-pagination">*432</span> Armed with a search warrant, the officers entered petitioner's apartment for the purpose of discovering violations of a federal narcotics statute, and seized a substantial amount of contraband narcotics. The parties urge upon us differing theories concerning which federal or District of Columbia statute bears on the legality of this search, and we must therefore interpret and reconcile several recent congressional enactments dealing with nighttime searches which seem to embody somewhat inconsistent views.<sup>[1]</sup></p>
<p>The Court of Appeals agreed with the District Court's description of this congeries of statutes as a " `bramble-bush of uncertainties and contradictions,' "<sup>[2]</sup> and a mere summary of the statutes attests to the accuracy of that observation:</p>
<p><i>District of Columbia Statutes:</i> The older of the two conceivably relevant District of Columbia statutes, D. C. Code § 33-414 (1973),<sup>[3]</sup> was enacted in 1956 and authorizes <span class="star-pagination">*433</span> search warrants for violations of the District of Columbia narcotics laws. This section does not limit the time during which searches may be made, stating plainly that "[t]he judge or commissioner shall insert a direction in the warrant that it may be served at any time in the day or night." This liberal time provision is in direct contrast to the more restrictive provisions of the second <span class="star-pagination">*434</span> District of Columbia statute to be considered, D. C. Code § 23-521 (f) (5),<sup>[4]</sup> which specifically requires that search warrants be served in the daytime unless certain conditions <span class="star-pagination">*435</span> set forth in § 23-522 (c) (1) are met. These conditions essentially require a showing of special need to search at night, and concededly have not been satisfied in this case.</p>
<p><span class="star-pagination">*436</span> <i>Federal Statutes and Rules:</i> The general provision governing federal search warrants is found in Fed. Rule Crim. Proc. 41.<sup>[5]</sup> At the time the search in this case <span class="star-pagination">*437</span> took place, Rule 41 (c) provided that warrants must be served in the daytime except where "the affidavits are positive that the property is on the person or in the place to be searched."<sup>[6]</sup> In such event the warrant <span class="star-pagination">*438</span> could direct "that it be served at any time." This provision was incorporated in the Rules in 1948 as a replacement for language previously contained in the Espionage Act of 1917.<sup>[7]</sup> A second federal statute relating only to searches for "controlled substances" is found in <span class="citation no-link">21 U. S. C. § 879</span> (a),<sup>[8]</sup> which was enacted in <span class="star-pagination">*439</span> 1970. That section provides that a warrant may be served "at any time of the day or night" so long as the issuing authority "is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." This provision in turn is the successor to a provision in <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.),<sup>[9]</sup> enacted in 1956 to relax the "positivity" test of Rule 41 in cases involving certain narcotic drugs.<sup>[10]</sup> Congress had passed this statute in response to the complaints of law enforcement officers that the positivity requirement gave commercial narcotics dealers a definite advantage over federal agents. Rule 41 is therefore not applicable to searches governed by the more specific narcotic search statutes.<sup>[11]</sup></p>
<p><span class="star-pagination">*440</span> The facts of this case must be understood in the context of these statutes. On February 11, 1971, an Assistant United States Attorney applied to a United States Magistrate sitting in the District of Columbia for a warrant authorizing a search of petitioner's apartment for evidence of illegal narcotics. The application included the brief notation: "Violation: U. S. C.; Title 26. Sections: 4704a." In connection with the application, an officer of the Metropolitan Police Department vice squad appeared before the Magistrate and swore that he had reason to believe petitioner was concealing property held in violation of that same code provision.<sup>[12]</sup><span class="star-pagination">*441</span> The officer supplemented his personal testimony with a written affidavit, outlining the basis for the application in more detail and alleging specifically that "illegal drugs are sold and possessed in violation of the United States Code, Title 26, Section 4704a."<sup>[13]</sup> The affidavit concluded with the language: "I am positive that Lonnie Gooding is secreting narcotics inside his apartment at 1419 Chapin Street NW in violation of the US Code."</p>
<p>The Magistrate then issued a warrant directing the Chief of Police or "any member of MPDC" to search petitioner's apartment.<sup>[14]</sup> The warrant specifically noted <span class="star-pagination">*442</span> that facts had been set forth in an affidavit alleging a violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.) and that those facts established probable cause to make the search. The warrant also stated that the search could be made "at any time in the day or night." This phrase was accompanied by a footnote reference to Fed. Rule Crim. Proc. 41 (c), presumably because the police officer had asserted he was "positive" the drugs were in petitioner's apartment. One of the briefs filed in this case suggests that the warrant form was preprinted and contemplated application of Rule 41 standards.<sup>[15]</sup></p>
<p>The search warrant was executed on February 12, 1971, at 9:30 p. m.<sup>[16]</sup> The officers engaged in the search were <span class="star-pagination">*443</span> all members of the District of Columbia Metropolitan Police Department, and the search uncovered a substantial quantity of contraband narcotic materials. They were seized and formed the basis for charging petitioner with violations of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.)<sup>[17]</sup> and <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.).<sup>[18]</sup> Following his indictment in the United States District Court for the District of Columbia on April 6, 1971, petitioner filed a motion to suppress the evidence discovered in the February 12 search.</p>
<p>Several grounds were asserted in support of the motion, particularly that "[t]he search warrant was executed at night but the application for the warrant did not comply with the D. C. Code provisions for nighttime search <span class="star-pagination">*444</span> warrants . . . ."<sup>[19]</sup> Although no provisions of the D. C. Code were explicitly referred to, petitioner's argument apparently was that Title 23 of the D. C. Code, requiring that a special showing of need be made to justify a search at night, governed this search, and that its requirements had not been met. The District Court found this reasoning persuasive and granted the motion to suppress. Rejecting the Government's argument that the warrant was not issued under Title 23 but rather under <span class="citation no-link">21 U. S. C. § 879</span> (a), the court stated:</p>
<blockquote>"Whatever be the standards generally for issuance of a nighttime search warrant in federal narcotics cases in other parts of the country, however, the Court finds that the existence of <span class="citation no-link">21 U. S. C. § 879</span> (a) does not remove such cases from the explicit requirements for search warrants in the District of Columbia under the newly enacted Title 23, D. C. Code."<sup>[20]</sup></blockquote>
<p>Having decided that District of Columbia law applied, the District Court admitted to some uncertainty about the status of D. C. Code § 33-414, the provision dealing specifically with violations of local drug laws. The court noted with some puzzlement that no mention of this provision was found in the legislative history of Title 23, and that some language in the legislative history suggested that the provision had simply been overlooked.<sup>[21]</sup> Nevertheless, the court determined that</p>
<blockquote>"[p]ending prompt review of this determination <span class="star-pagination">*445</span> or congressional action, and pending interpretation of 33 D. C. Code § 414 (h) in light of the new Title 23 provisions, search warrants which are to be executed in the nighttime should comply in all respects with 23 D. C. Code § 523 (b)."<sup>[22]</sup></blockquote>
<p>Concededly the warrant issued in this case did not comply with the requirements of Title 23.</p>
<p>The Court of Appeals for the District of Columbia Circuit reversed the District Court,<sup>[23]</sup> although none of the three judges who composed the panel completely agreed with any other on the proper rationale. All three agreed, however, that <span class="citation no-link">21 U. S. C. § 879</span> (a), rather than any provision of the District of Columbia Code, was the provision which determined the legality of this search. All three likewise agreed that the affidavit submitted by the District of Columbia police officer satisfied the requirements of that section. Judge Wilkey and Judge Fahy found that no greater showing for a nighttime search was required by § 879 (a) than was required by its predecessor statute governing federal narcotics searches, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), and that the affidavit need establish only probable cause to believe that the property would be on the premises at the time of the search.<sup>[24]</sup> Judge Robinson believed that § 879 (a) <span class="star-pagination">*446</span> did require an additional showing for a nighttime search, but concluded that such a showing had been made in this case.<sup>[25]</sup></p>
<p>Petitioner urges that we reverse the Court of Appeals on either or both of two alternative grounds. First, petitioner repeats his assertion, sustained by the District Court, that Title 23 of the D. C. Code is the statute applicable to the search in this case and that, as the Government has conceded, the requirements of that title have not been satisfied. Second, petitioner argues that, if <span class="citation no-link">21 U. S. C. § 879</span> (a) is considered to be the applicable provision, a special showing for nighttime searches must be made. We agree with the Court of Appeals that <span class="citation no-link">21 U. S. C. § 879</span> (a) is the statute applicable to this case, and that its provisions have been satisfied here.<sup>[26]</sup></p>
<p></p>
<h2>I</h2>
<p>The unique situation of the District of Columbia, for which Congress legislates both specially and as a part <span class="star-pagination">*447</span> of the Nation, gives rise to the principal difficulties in this case. For we deal here not with statutory schemes enacted by independent legislative bodies, but with possibly overlapping schemes enacted by a single body. Despite the potential overlap, however, we think that the operative facts surrounding this search strongly indicate that the standards for issuance of a warrant should be governed by the nationwide federal legislation enacted by Congressthat is, <span class="citation no-link">21 U. S. C. § 879</span> (a)<sup>[27]</sup> rather than by the local D. C. laws. To begin with, an Assistant United States Attorney, who had discretion to proceed either under federal or under local law, filed the application for the search warrant alleging a violation of the United States Code. Application was made to a United States Magistrate, located in the United States District Court building, and neither the application nor the supporting affidavits contained any mention of the local narcotics laws. After the materials were seized, petitioner was indicted for violations of federal law.</p>
<p>Petitioner contends, however, that Title 23 of the D. C. Code should apply to this case because the executing officers, as well as the officer swearing to the affidavit presented to the Magistrate, were not federal officers but officers of the District of Columbia Metropolitan Police Department. He argues that the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) were intended to apply solely to agents of the Bureau of Narcotics and Dangerous Drugs, none of whom were involved here, whereas Title 23 of the D. C. Code was intended to provide comprehensive regulation of District of Columbia police officers investigating both local and federal offenses. Petitioner reinforces his argument by nothing that the former federal statute <span class="star-pagination">*448</span> regulating drug searches specifically provided that "a search warrant may be directed to any officer of the Metropolitan Police of the District of Columbia authorized to enforce or assist in enforcing a violation of any of such provisions,"<sup>[28]</sup> while no such section appears in <span class="citation no-link">21 U. S. C. § 879</span>. Therefore, says petitioner, the District of Columbia police were no longer to be considered federal agents for the purpose of enforcing federal drug laws.</p>
<p>Although petitioner's arguments cannot be dismissed lightly, we find them ultimately unpersuasive. Concededly there are hints in the statutory framework and legislative history of the Controlled Substances Act, <span class="citation no-link">84 Stat. 1242</span>, that indicate the policing function under those provisions would be the primary responsibility of the Bureau of Narcotics and Dangerous Drugs.<sup>[29]</sup> But this focus on the Bureau's role seems entirely natural in view of one of the Act's stated purposes to "collect the diverse drug <span class="star-pagination">*449</span> control and enforcement laws under one piece of legislation to facilitate law enforcement, drug research, educational and related control facilities."<sup>[30]</sup> In providing a comprehensive federal scheme for the control of drug abuse, Congress could be expected to pay special attention to the federal agency set up to enforce the laws. But this attention does not mean that Congress at the same time wished to dispense with the aid of other enforcement personnel who had previously given assistance.</p>
<p>The failure of Congress to include a special provision authorizing District of Columbia police officers to obtain search warrants for investigating federal offenses cannot be taken as a deliberate exclusion in view of the overall statutory framework. The provision included in the previous federal statute may well have seemed unnecessary, both in light of the history of cooperation between the District of Columbia police and federal officers and in view of the provisions of D. C. Code § 4-138 providing that "[a]ny warrant for search or arrest, issued by any magistrate of the District, may be executed in any part of the District by any member of the police force . . . ."<sup>[31]</sup> Thus, both custom and statute already assured the availability of District of Columbia police. Furthermore, the legislative history relating to § 879 (a) stresses the need for stronger enforcement of the federal narcotics laws, a goal hardly advanced by reducing the forces available to execute those laws. In fact, the provision <span class="star-pagination">*450</span> which is now § 879 (b), permitting "no-knock" searches under certain conditions, was one of the most controversial sections of the entire bill, and was defended primarily by the pressing need for added enforcement weapons to combat the increased drug traffic.<sup>[32]</sup></p>
<p>Finally, the interpretation urged by petitioner would leave District of Columbia officers able to execute general federal search warrants under amended Fed. Rule Crim. Proc. 41, but would deny them that authority under the federal drug search statute. Rule 41 now provides that "a federal law enforcement officer"defined in the Rule to include "any category of officers authorized by the Attorney General to request the issuance of a search warrant"may make applications under the Rule. The Attorney General has since listed the Metropolitan Police Department among those agencies <span class="star-pagination">*451</span> which are so authorized.<sup>[33]</sup> If petitioner's contention were accepted, it would seemingly mean that the general search warrant statute applicable to the District of Columbia would govern District of Columbia police officers investigating federal drug cases, but would not govern them when investigating other federal crimes. This result would obtain despite the fact that District of Columbia police officers historically played a prominent role in the enforcement of federal drug laws under <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.).</p>
<p>There is little indication that Title 23 of the D. C. Code was intended to serve the sweeping purpose which petitioner attributes to it.<sup>[34]</sup> The search warrant provisions upon which petitioner relies were part of the Court Reform and Criminal Procedure Act, which substantially reorganized the District of Columbia court system, providing for a new local court of general jurisdiction and relieving the United States District Court for the District of Columbia of much of its local burden.<sup>[35]</sup> Prior to that time all local felonies had been tried in the United States District Court, and the Federal Rules of Criminal Procedure by their terms had applied. The creation of the new Superior Court created the need for a new set of procedural <span class="star-pagination">*452</span> rules, and, though some important changes were made, the new rules quite closely tracked the Federal Rules. It does not seem unreasonable, therefore, to suggest that the general provision relating to search warrants, found in D. C. Code § 23-521 <i>et seq.</i> and then incorporated in similar form into the rules<sup>[36]</sup> promulgated <span class="star-pagination">*453</span> Feb. 1, 1971, for the new Superior Court, was intended to be a counterpart to Fed. Rule Crim. Proc. 41. The Federal Rule, as discussed <i>infra,</i> did not apply to narcotics cases in the federal courts since more specific provisions, first those of <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.) and then those of <span class="citation no-link">21 U. S. C. § 879</span> (a), controlled.<sup>[37]</sup></p>
<p>This conclusion is reinforced by the fact that Federal Rule 41 has been subsequently modified to more closely resemble the District of Columbia statute and rule. The new Federal Rule, though less specific than the local rule, provides that a search warrant must be served in the daytime, "unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime," and abandons the old, cumbersome positivity standard. The concern for individual privacy revealed in the provisions of the District of Columbia search statute may thus be found in the new Federal Rule as well, but Congress, as it had in the earlier version of the Rule, <span class="star-pagination">*454</span> nevertheless showed its clear intention to leave intact other special search warrant provisions, including, of course, the provisions relating to searches for controlled substances.<sup>[38]</sup> In those limited cases Congress has considered the need for privacy to be counterbalanced by the public need for more effective law enforcement. We do not believe that Congress, by enacting a general search warrant provision for the District of Columbia, has struck a different balance in federal drug cases simply because District of Columbia police officers are involved.</p>
<p>We therefore conclude, as did all the judges of the Court of Appeals, that the statute applicable to this case is <span class="citation no-link">21 U. S. C. § 879</span> (a). Our remaining task is to determine whether the requirements of that section have been met.</p>
<p></p>
<h2>II</h2>
<blockquote>"A search warrant relating to offenses involving controlled substances may be served at any time of the day or night if the judge or United States magistrate issuing the warrant is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." <span class="citation no-link">21 U. S. C. § 879</span> (a).</blockquote>
<p>Only the last seven words of the statute are really in controversy here. Petitioner contends that this language, not found in the predecessor statute, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), was intended to require some special showing of need for searches conducted at night rather than during the day. His contention was adopted, at least in part, by Judge Robinson in the Court of Appeals. The Government, on the other hand, contends that it must show only probable cause to believe that the <span class="star-pagination">*455</span> sought-after property will be on the premises at the time of the search, and that if there is probable cause to believe the property will be on the premises at night, such a showing sufficiently meets the requirement imposed by the last seven words of § 879 (a).</p>
<p>The language of the statute by itself is not crystal clear on this issue. Petitioner insists that the last phrase requires with unmistakable clarity a separate finding of probable cause to justify a nighttime search. Thus, according to petitioner, the issuing magistrate would have to satisfy himself that there was not only probable cause for the search, but also probable cause for believing that the search should be conducted at nighttime rather than during the daytime. While this is <i>a</i> possible meaning, it is by no means the only possible meaning attributable to the words.</p>
<p>Petitioner's interpretation really assumes that the statute reads: "There is probable cause to believe that grounds exist for the warrant and, <i>if served at night,</i> for its service at such time." But the statute does not include the italicized four words; it makes no distinction whatever between day and night, and literally read would apparently require that a special showing be made for a daytime search as well. The idea that a particularized showing must be made for searches in the daytime is completely novel and lacks even a single counterpart in other search statutes enacted by Congress.</p>
<p>Petitioner suggests that since Congress was concerned about the greater intrusion resulting from nighttime searches, it would be logical to apply the language, "probable cause . . . for its service at such time," only to nighttime searches. But even this interpretation, which is by no means a literal reading of the language, is not wholly convincing. The traditional limitation placed on nighttime searches, as evident from the earlier <span class="star-pagination">*456</span> language of Rule 41, is to require, not that there be probable cause for searching at night, but that the affiant be <i>positive</i> that the property is in fact located on the property to be searched. Thus Congress' very choice of the words "probable cause" would indicate that the earlier limitation of "positivity" was not to apply, while offering no other immediately ascertainable standard for what should constitute "probable cause" for executing a search warrant during the night.</p>
<p>This roundabout way of limiting nighttime searches, if that were in fact the statute's intent, would sharply contrast with the manner in which Congress has required special showings for nighttime searches in other statutes. For example, Title 23 of the D. C. Code, discussed <i>supra,</i> specifies that the warrant "be executed <i>during the hours of daylight</i>" (emphasis added) unless certain itemized conditions are met. Federal Rule Crim. Proc. 41, as amended in 1972, states: "The warrant <i>shall be served in the daytime</i> unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime." (Emphasis added.) The fact that Congress, when it has intended to require such special showings for nighttime searches, has done so in language largely free from ambiguity militates against petitioner's assertion that the language of § 879 (a) on its face supports his position.</p>
<p>The legislative history lends no support to petitioner's interpretation, but in fact cuts the other way. Both the House and the Senate Committee Reports on the bill incorporated a summary prepared by the Department of Justice, where much of the bill's drafting had taken place, which stated:</p>
<blockquote>"Section 702 (a) [now § 879 (a)] incorporates 18 U. S. C. [§] 1405 and authorizes service of a search <span class="star-pagination">*457</span> warrant at any time of the day or night if probable cause has been established to the satisfaction of the judge or U. S. magistrate issuing the warrant."<sup>[39]</sup></blockquote>
<p>As previously noted, § 1405 provided that a search warrant could be served at any time of the day or night so long as the issuing officer was "satisfied that there is probable cause to believe that the grounds for the application exist . . . ." Case law had uniformly interpreted the language to mean that probable cause for the warrant itself was all that was necessary for a nighttime search.<sup>[40]</sup> The officers or agents simply had to establish probable cause for believing that the sought-after property would be found in the place to be searched.</p>
<p>There is no suggestion in any of the hearings or debates before Congress that a change from the prior law in this area was intended. The provision itself went unmentioned in the debates and hearings on the bill, a surprising omission if the bill effected the cutback petitioner says it did. Of like import is the fact that in the long and heated discussions over § 702 (b), the so-called "no-knock" provision of the bill, no defender of the bill saw fit to argue that any greater intrusion caused by the no-knock provision would be partially offset by the greater difficulty in obtaining warrants executable at night.<sup>[41]</sup> While congressional silence as to a particular provision of a bill during debates which give extensive consideration to neighboring provisions is not easy to interpret, it would be unusual for such a significant <span class="star-pagination">*458</span> change as that proposed by petitioner to have entirely escaped notice.</p>
<p>Finally, it is important to note that the Department of Justice itself submitted this bill to Congress for enactment, including § 879 (a) in its present form. Since the hearings and debates stress that a major purpose of the bill was to supply more effective enforcement tools to combat the increasing use of narcotic drugs, it seems totally illogical to suggest that the Department of Justice would submit a bill making it substantially more difficult to control the traffic in hard drugs. Petitioner suggests that this surrender was necessary to convince Congress to bring additional drugs within the Controlled Substances Act, but that theory rests entirely on speculation. There is absolutely no indication in the legislative history that any price had to be paid for what was thought to be a much-desired reorganization and expansion of the drug laws, much less the substantial price that petitioner argues had to be paid here.</p>
<p>We therefore conclude that <span class="citation no-link">21 U. S. C. § 879</span> (a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time.<sup>[42]</sup> We believe that the showing was met in this case. The affidavit submitted by the District of Columbia police officer suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available. This was sufficient to satisfy <span class="citation no-link">21 U. S. C. § 879</span> (a). The judgment of the Court of Appeals for the District of Columbia Circuit is</p>
<p><i>Affirmed.</i></p>
<p><span class="star-pagination">*459</span> MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL concur, dissenting.</p>
<p>The petitioner is charged with possession of heroin and narcotics paraphernalia in violation of <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.) and <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.). He moved the District Court to suppress certain evidence seized from his home pursuant to a search warrant secured by and directed to the Metropolitan Police Department of the District of Columbia. The District Court granted the suppression motion on the ground that the search was conducted at night in violation of D. C. Code §§ 23-521-523 (1973) which limit search warrant execution to daylight hours absent specific contrary authorization founded upon the judicial officer's determination</p>
<blockquote>"that (A) it cannot be executed during the hours of daylight, (B) the property sought is likely to be removed or destroyed if not seized forthwith, or (C) the property sought is not likely to be found except at certain times or in certain circumstances. . . ." D. C. Code § 23-522 (c) (1).<sup>[1]</sup></blockquote>
<p>Though the warrant here directed a search "at any time in the day or night," none of the grounds set forth in § 23-522 (c) (1) were contained in either the application or the warrant itself. The police obtained the warrant on February 11, 1971, but they failed to execute it during the day of February 12, waiting instead until 9:30 p. m. on that date. Since they delayed execution until well after the daylight hours had ended, <span class="star-pagination">*460</span> the seizure was invalid if governed by D. C. Code §§ 23-521 to 23-523.</p>
<p>The Court holds, however, that the D. C. Code provisions are inapplicable and that the search is governed by <span class="citation no-link">21 U. S. C. § 879</span> (a). That section became effective October 27, 1970, as part of the Controlled Substances Act, <span class="citation no-link">84 Stat. 1242</span>, <span class="citation no-link">21 U. S. C. § 801</span> <i>et seq.;</i> it relates to search warrants issued in connection with offenses involving controlled substances. The D. C. Code provisions, however, became effective February 11, 1971, as part of the District of Columbia Court Reform and Criminal Procedure Act. The latter Act did not distinguish between local and federal prosecutions in its procedural innovations.<sup>[2]</sup> The purpose of the restriction upon nighttime searches was to limit such intrusions to those instances where there is "some justification for it,"<sup>[3]</sup> thus implementing the "policy generally disfavoring nighttime executions, nighttime intrusions, more characteristic of a `police state' lacking in the respect for due process and the right of privacy dictated by the U. S. Constitution and history . . . ."<sup>[4]</sup></p>
<p>Approximately 60% of the search warrants issued in the District of Columbia relate to narcotics violations. Congress was aware of this, and, if it had intended to except federal narcotics search warrants from the protections against unnecessary nighttime "police state" searches, one would expect an expression of such intent. I agree with Judge Gesell that no such intent is indicated. <span class="star-pagination">*461</span> Thus, "[w]hatever be the standards generally for issuance of a nighttime search warrant in federal narcotics cases in other parts of the country . . . the existence of <span class="citation no-link">21 U. S. C. § 879</span> (a) does not remove such cases from the explicit requirements for search warrants in the District of Columbia under the newly enacted Title 23, D. C. Code." <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1007" aria-description="Citation for case: United States v. Gooding">328 F. Supp. 1005, 1007</a></span>. I would reverse the Court of Appeals and sustain the District Court's suppression order.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE BRENNAN join, dissenting.</p>
<p>I agree with my Brother DOUGLAS that the provisions of the District of Columbia Code requiring a showing of need for execution of a search warrant at night govern the search involved in this case, and, accordingly, I join in his dissenting opinion. A majority of the Court, however, rejects this argument and goes on to discuss the standards imposed by <span class="citation no-link">21 U. S. C. § 879</span> (a) upon issuance of search warrants for nighttime execution in federal narcotics cases. Obviously, the Court's interpretation of § 879 (a) is of far greater significance, of national rather than purely local concern. I cannot let the Court's construction of § 879 (a) pass without registering my dissent on this issue as well.</p>
<p>The opinion of the Court, it seems to me, analyzes the § 879 (a) issue in a vacuum, without any discussion of some of the important policy considerations which underlie this question of statutory interpretation. Perhaps a partial vacuum would be a more appropriate description, since the Court is obviously fully cognizant of the substantial governmental interest in enforcement of the narcotics laws, an interest which its interpretation of § 879 (a) so well serves. But plainly there are other concerns implicated in our interpretation of this congressional <span class="star-pagination">*462</span> enactment restricting the issuance of search warrantsthe protection of individual privacy which is the very purpose of the statute's search warrant requirement and which of course is given constitutional recognition in the Fourth Amendment. The Court seems totally oblivious to these constitutional considerations. Taking them into account, I find that the only acceptable interpretation of the statute is one which requires some additional justification for authorizing a nighttime search over and above the ordinary showing of probable cause to believe that a crime has been committed and that evidence of the crime will be found upon the search.</p>
<p>Fundamentally at issue in this case is the extent of the protection which we will all enjoy from police intrusion into the privacy of our homes during the middle of the night. The Fourth Amendment was intended to protect our reasonable expectations of privacy from unjustified governmental intrusion. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360-362</a></span> (1967) (Harlan, J., concurring). In my view, there is no expectation of privacy more reasonable and more demanding of constitutional protection than our right to expect that we will be let alone in the privacy of our homes during the night. The idea of the police unnecessarily forcing their way into the home in the middle of the nightfrequently, in narcotics cases, without knocking and announcing their purposerousing the residents out of their beds, and forcing them to stand by in indignity in their night clothes while the police rummage through their belongings does indeed smack of a " `police state' lacking in the respect for . . . the right of privacy dictated by the U. S. Constitution." S. Rep. No. 91-538, p. 12 (1969). The public outrage at the series of mistaken nighttime raids by narcotics agents in Collinsville, Illinois, last <span class="star-pagination">*463</span> April, see N. Y. Times, Apr. 29, 1973, p. 1, col. 5; N. Y. Times, Apr. 30, 1973, p. 30, col. 1, serves to emphasize just how inconsistent with our constitutional guarantees such nighttime searches are.</p>
<p>This Court has consistently recognized that the intrusion upon privacy engendered by a search of a residence at night is of an order of magnitude greater than that produced by an ordinary search. Mr. Justice Harlan observed in holding a nighttime search unconstitutional in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#498" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 498</a></span> (1958): "[I]t is difficult to imagine a more severe invasion of privacy than the nighttime intrusion into a private home." In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#477" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 477</a></span> (1971), the Court again recognized that a midnight entry into a home was an "extremely serious intrusion." And our decision in <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965), was in large part based upon our revulsion at the thought of nighttime searches of the marital bedroom to discover evidence of illegal contraceptive use. See <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#485" aria-description="Citation for case: Griswold v. Connecticut"><i>id.,</i> at 485-486</a></span>.</p>
<p>It is small wonder, then, that Congress has consistently required more stringent justification for nighttime searches than that needed to authorize a search during the day. The first congressional enactment setting out comprehensive search warrant procedures, § 10 of Tit. XI of the Espionage Act of 1917, <span class="citation no-link">40 Stat. 217</span>, 229, <span class="citation no-link">18 U. S. C. § 620</span> (1940 ed.), required that the affiant must be "positive" that the property to be seized was on the premises to justify a nighttime search. When the provisions of the Espionage Act were replaced by the Federal Rules of Criminal Procedure in 1946, this requirement of positivity was carried forward in Rule 41. Despite the stringency of this requirement, it remained with us until very recently, until the 1972 amendments to Rule 41. And although the Rule was then modified to require <span class="star-pagination">*464</span> "reasonable cause" for nighttime execution of a warrant, significantly the amended Rule retained the principle that nighttime searches require an additional showing of justification over and above probable cause. Congress has also manifested its concern for protection of individual privacy against nighttime searches in its legislation for the District of Columbia, as MR. JUSTICE DOUGLAS' opinion amply demonstrates with respect to enactment of the D. C. Court Reform and Criminal Procedure Act in 1970. <i>Ante,</i> at 460.<sup>[1]</sup></p>
<p>The strong policy underlying these congressional enactments is clear. As even the Government in this case concedes, "searches conducted in the middle of the night . . . involve a greater intrusion than ordinary searches and therefore require a greater justification." Brief for United States 14. In my view, this principle may well be a constitutional imperative. It is by now established Fourth Amendment doctrine that increasingly severe standards of probable cause are necessary to justify increasingly intrusive searches. In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), after holding that search warrants were required to authorize administrative inspections, we held that the quantum of probable cause required for issuance of an inspection warrant must be determined in part by the reasonableness of the proposed search. As MR. JUSTICE WHITE stated, "there can be no ready test for determining reasonableness other than by balancing the need to search against the invasion which the search entails." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 536-537</a></span>. The Court in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> thus approved the issuance <span class="star-pagination">*465</span> of area inspection warrants in part because such searches "involve a relatively limited invasion of the urban citizen's privacy." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 537</a></span>. See also <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S. 322</a></span>, 349 n. 6 (1973) (MARSHALL, J., dissenting). I do not regard this principle as a one-way street, to be used only to water down the requirement of probable cause when necessary to authorize governmental intrusions. In some situationsand the search of a private home during nighttime would seem to be a paradigm this principle requires a showing of additional justification for a search over and above, the ordinary showing of probable cause. Cf. <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485-486</a></span> (1965).</p>
<p>Of course, this constitutional question is not presented in this case and need not be resolved here. But the long history of congressional authorization of nighttime searches only upon a showing of additional justification, the strong constitutionally based policy which these statutes implement, and the substantial constitutional question posed by the majority's interpretation of § 879 (a) are surely relevant to the question of statutory interpretation with which we are faced. Viewed against this background, I think it is plain that the majority's interpretation of the statute should be rejected.</p>
<p>Section 879 (a) provides that search warrants may be executed at night only if "there is probable cause to believe that grounds exist for the warrant and for its service at such time." It seems to me quite clear that the statute, on its face, imposes two distinct requirements: that there be probable cause for the issuance of the warrant, and that there be cause "for its service at such time." While the Court relies on legislative history which suggests that § 879 (a) merely "incorporates" the provisions of its predecessor, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), the plain <span class="star-pagination">*466</span> fact is that § 879 (a) does far more than this: it also adds to the language of § 1405 the final clause"and for its service at such time"which is at the heart of the dispute in this case. I can see no plausible interpretation of this final clause other than that it imposes an additional requirement of justification for a search at night over and above a showing of probable cause.</p>
<p>The Court, while conceding this to be a "possible" meaning of the statute's final clause, argues that "it is by no means the only possible meaning attributable to the words." <i>Ante,</i> at 455. Unfortunately, the Court then fails to come forward with any alternative interpretation of these final words of § 879 (a). Instead, the Court simply reads the disputed language out of the statute entirely, and decrees that the statute shall be interpreted as if it were not there. The Court holds that the statute requires only "a showing that the contraband is likely to be on the property or person to be searched at that time" to justify nighttime execution of a search warrant. <i>Ante,</i> at 458. But the showing of probable cause required for issuance of any warrant necessarily includes a showing that the objects to be seized will probably be found on the premises at the time of the search. See <i>Sgro</i> v. <i>United States,</i> <span class="citation" data-id="9418758"><a href="/opinion/101970/sgro-v-united-states/#210" aria-description="Citation for case: Sgro v. United States">287 U. S. 206, 210-211</a></span> (1932); <i>Schoeneman</i> v. <i>United States,</i> 115 U. S. App. D. C. 110, 113, <span class="citation" data-id="260559"><a href="/opinion/260559/harry-carl-schoeneman-v-united-states-of-america-garlan-euel-markham-jr/#176" aria-description="Citation for case: Harry Carl Schoeneman v. United States of America, Garlan...">317 F. 2d 173, 176-177</a></span> (1963); <i>Rosencranz</i> v. <i>United States,</i> <span class="citation" data-id="270626"><a href="/opinion/270626/samuel-rosencranz-v-united-states-of-america-anthony-dipietro-v-united/#315" aria-description="Citation for case: Samuel Rosencranz v. United States of America, Anthony...">356 F. 2d 310, 315-318</a></span> (CA1 1966). This requirement is clearly imposed by the Fourth Amendment itself. It is also clearly mandated by the first part of the statutory language, which merely incorporates the constitutional requirement of probable cause for issuance of the warrant. The majority's interpretation of the statute thus leaves the final clause of § 879 (a)the language in controversy heretotally without meaning. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="9751925"><a href="/opinion/2307321/united-states-v-thomas/#170" aria-description="Citation for case: United States v. Thomas">294 A. 2d 164, 170</a></span> (DC Ct. App.) <span class="star-pagination">*467</span> (Kelly, J., dissenting), cert. denied, <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/" aria-description="Citation for case: Thomas v. United States">409 U. S. 992</a></span> (1972); <i>United States</i> v. <i>Gooding,</i> 155 U. S. App. D. C. 259, 273, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#442" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428, 442</a></span> (1973) (Robinson, J., concurring in result). I cannot subscribe to such an evisceration of the statute.<sup>[2]</sup></p>
<p><span class="star-pagination">*468</span> The Court bases its holding upon the meager recorded legislative history of § 879 (a). But when the language of a statute is as clear and unambiguous as it is here, it is neither helpful nor appropriate to look to its legislative history. <i>Ex parte Collett,</i> <span class="citation" data-id="9420318"><a href="/opinion/104671/ex-parte-collett/#61" aria-description="Citation for case: Ex Parte Collett">337 U. S. 55, 61</a></span> (1949); <i>United States</i> v. <i>Oregon,</i> <span class="citation" data-id="9422227"><a href="/opinion/106253/united-states-v-oregon/#648" aria-description="Citation for case: United States v. Oregon">366 U. S. 643, 648</a></span> (1961). While committee reports in particular are often a helpful guide to the meaning of ambiguous statutory language, even they must be disregarded if inconsistent with the plain language of the statute. <i>Helvering</i> v. <i>City Bank Farmers Trust Co.,</i> <span class="citation" data-id="102494"><a href="/opinion/102494/helvering-v-city-bank-farmers-trust-co/#89" aria-description="Citation for case: Helvering v. City Bank Farmers Trust Co.">296 U. S. 85, 89</a></span> (1935); <i>George Van Camp &amp; Sons Co.</i> v. <i>American Can Co.,</i> <span class="citation" data-id="101357"><a href="/opinion/101357/george-van-camp-sons-co-v-american-can-co/#253" aria-description="Citation for case: George Van Camp &amp; Sons Co. v. American Can Co.">278 U. S. 245, 253-254</a></span> (1929). It is the language of the statute, as enacted by the Congress, that is the law of the land, not the language of a committee report which may or may not represent accurately the views of the hundreds of other legislators who voted for the bill.</p>
<p>In any event, even if resort to examination of the legislative history were appropriate here, I do not find it nearly so conclusive as does the majority of the Court. The Court relies on a single brief statement on § 879 (a) in the committee report stating that the statute merely incorporated the provisions of § 1405, which had been construed not to impose any requirement for a nighttime search warrant over and above probable cause. Yet this statement fails to provide any explanation for the language which Congress added to § 1405, the language <span class="star-pagination">*469</span> in controversy here. As to the meaningor, as the Court would have it, the lack of meaningof this language, the Court relies basically upon the law enforcement goals of the Department of Justice and the silence of Congress. But, as we have frequently warned, "[i]t is at best treacherous to find in congressional silence alone the adoption of a controlling rule of law." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#69" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 69</a></span> (1946); see H. M. Hart &amp; A. Sacks, The Legal Process:Basic Problems in the Making and Application of Law 1395-1398 (tent. ed. 1958), and cases there cited. The Court in effect presumes from Congress' failure to explain the meaning of the final clause of § 879 (a) its acquiescence in the Justice Department's apparent view that this language in fact serves no purpose.</p>
<p>I would presume the contrary. Congress' consistent protection of nighttime privacy by imposing restrictions upon the availability of warrants for nighttime searches reinforces the unambiguous statutory language. Both lead me to the conclusion that the final clause of § 879 (a) must be viewed as another congressional manifestation of its strong policy against nighttime intrusions into the home. I do not think that this interpretation is at all inconsistent with the narcotics law-enforcement objectives which were the principal focus of this legislation. The requirement that cause be shown for the necessity of a nighttime search is still a substantial easing of the requirement of positivity which was then embodied in Rule 41, and which would otherwise have applied to many of the searches now covered by § 879 (a). I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  The Government contends that even though we were to determine that the applicable statutory provision was violated in this case, the evidence should nonetheless not be suppressed. Since we conclude that the seizure was consistent with the governing statute, we have no occasion to reach this alternative argument.</p>
<p>[2]  See 155 U. S. App. D. C. 259, 261, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#430" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428, 430</a></span> (1973), quoting from <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1008" aria-description="Citation for case: United States v. Gooding">328 F. Supp. 1005, 1008</a></span> (DC 1971).</p>
<p>[3]  "§ 33-414. Search warrantsRequirementsFormContents ReturnPenalty for interfering with service.
</p>
<p>"(a) A search warrant may be issued by any judge of the Superior Court of the District of Columbia or by a United States commissioner for the District of Columbia when any narcotic drugs are manufactured, possessed, controlled, sold, prescribed, administered, dispensed, or compounded, in violation of the provisions of this chapter, and any such narcotic drugs and any other property designed for use in connection with such unlawful manufacturing, possession, controlling, selling, prescribing, administering, dispensing, or compounding, may be seized thereunder, and shall be subject to such disposition as the court may make thereof and such narcotic drugs may be taken on the warrant from any house or other place in which they are concealed.</p>
<p>"(b) A search warrant cannot be issued but upon probable cause supported by affidavit particularly describing the property and the place to be searched.</p>
<p>"(c) The judge or commissioner must, before issuing the warrant, examine on oath the complainant and any witnesses he may produce, and require their affidavits or take their depositions in writing and cause them to be subscribed by the parties making them.</p>
<p>"(d) The affidavits or depositions must set forth the facts tending to establish the grounds of the application or probable cause for believing that they exist.</p>
<p>"(e) If the judge or commissioner is thereupon satisfied of the existence of the grounds of the application or that there is probable cause to believe their existence, he must issue a search warrant, signed by him, to the major and superintendent of police of the District of Columbia or any member of the Metropolitan police department, stating the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof, and commanding him forthwith to search the place named for the property specified and to bring it before the judge or commissioner.</p>
<p>"(f) A search warrant may in all cases be served by any of the officers mentioned in its direction, but by no other person, except in aid of the officer on his requiring it, he being present and acting in its execution.</p>
<p>"(g) The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute the warrant, if, after notice of his authority and purpose, he is refused admittance.</p>
<p>"(h) The judge or commissioner shall insert a direction in the warrant that it may be served at any time in the day or night."</p>
<p>[4]  "§ 23-521. Nature and issuance of search warrants
</p>
<p>"(a) Under circumstances described in this subchapter, a judicial officer may issue a search warrant upon application of a law enforcement officer or prosecutor. A warrant may authorize a search to be conducted anywhere in the District of Columbia and may be executed pursuant to its terms.</p>
<p>"(b) A search warrant may direct a search of any or all of the following:</p>
<p>"(1) one or more designated or described places or premises;</p>
<p>"(2) one or more designated or described vehicles;</p>
<p>"(3) one or more designated or described physical objects; or</p>
<p>"(4) designated persons.</p>
<p>"(c) A search warrant may direct the seizure of designated property or kinds of property, and the seizure may include, to such extent as is reasonable under all the circumstances, taking physical or other impressions, or performing chemical, scientific, or other tests or experiments of, from, or upon designated premises, vehicles, or objects.</p>
<p>"(d) Property is subject to seizure pursuant to a search warrant if there is probable cause to believe that it</p>
<p>"(1) is stolen or embezzled;</p>
<p>"(2) is contraband or otherwise illegally possessed;</p>
<p>"(3) has been used or is possessed for the purpose of being used, or is designed or intended to be used, to commit or conceal the commission of a criminal offense; or</p>
<p>"(4) constitutes evidence of or tends to demonstrate the commission of an offense or the identity of a person participating in the commission of an offense.</p>
<p>"(e) A search warrant may be addressed to a specific law enforcement officer or to any classification of officers of the Metropolitan Police Department of the District of Columbia or other agency authorized to make arrests or execute process in the District of Columbia.</p>
<p>"(f) A search warrant shall contain</p>
<p>"(1) the name of the issuing court, the name and signature of the issuing judicial officer, and the date of issuance;</p>
<p>"(2) if the warrant is addressed to a specific officer, the name of that officer, otherwise, the classifications of officers to whom the warrant is addressed;</p>
<p>"(3) a designation of the premises, vehicles, objects, or persons to be searched, sufficient for certainty of identification;</p>
<p>"(4) a description of the property whose seizure is the object of the warrant;</p>
<p>"(5) a direction that the warrant be executed during the hours of daylight or, where the judicial officer has found cause therefor, including one of the grounds set forth in section 23-522 (c) (1), an authorization for execution at any time of day or night;</p>
<p>"(6) where the judicial officer has found cause therefor, including one of the grounds set forth in subparagraph (A), (B), or (D) of section 23-591 (c) (2), an authorization that the executing officer may break and enter the dwelling house or other building or vehicles to be searched without giving notice of his identity and purpose; and</p>
<p>"(7) a direction that the warrant and an inventory of any property seized pursuant thereto be returned to the court on the next court day after its execution.</p>
<p>"§ 23-522. Applications for search warrants</p>
<p>"(a) Each application for a search warrant shall be made in writing upon oath or affirmation to a judicial officer.</p>
<p>"(b) Each application shall include</p>
<p>"(1) the name and title of the applicant;</p>
<p>"(2) a statement that there is probable cause to believe that property of a kind or character described in section 23-521 (d) is likely to be found in a designated premise, in a designated vehicle or subject, or upon designated persons;</p>
<p>"(3) allegations of fact supporting such statement; and</p>
<p>"(4) a request that the judicial officer issue a search warrant directing a search for and seizure of the property in question.</p>
<p>"The applicant may also submit depositions or affidavits of other persons containing allegations of fact supporting or tending to support those contained in the application.</p>
<p>"(c) The application may also contain</p>
<p>"(1) a request that the search warrant be made executable at any hour of the day or night, upon the ground that there is probable cause to believe that (A) it cannot be executed during the hours of daylight, (B) the property sought is likely to be removed or destroyed if not seized forthwith, or (C) the property sought is not likely to be found except at certain times or in certain circumstances; and</p>
<p>"(2) a request that the search warrant authorize the executing officer to break and enter dwelling houses or other buildings or vehicles to be searched without giving notice of his identity and purpose, upon probable cause to believe that one of the conditions set forth in subparagraph (A), (B), or (D) of section 23-591 (c) (2) is likely to exist at the time and place at which such warrant is to be executed.</p>
<p>"Any request made pursuant to this subsection must be accompanied and supported by allegations of fact supporting such request."</p>
<p>[5]  At the time of the search in this case Rule 41 read, in part, as follows:
</p>
<p>"Search and Seizure</p>
<p>"(a) Authority to Issue Warrant. A search warrant authorized by this rule may be issued by a judge of the United States or of a state, commonwealth or territorial court of record or by a United States commissioner within the district wherein the property sought is located.</p>
<p>"(b) Grounds for Issuance. A warrant may be issued under this rule to search for and seize any property</p>
<p>"(1) Stolen or embezzled in violation of the laws of the United States; or</p>
<p>"(2) Designed or intended for use or which is or has been used as the means of committing a criminal offense; or</p>
<p>"(3) Possessed, controlled, or designed or intended for use or which is or has been used in violation of Title <span class="citation no-link">18, U. S. C., § 957</span>.</p>
<p>"(c) Issuance and contents. A warrant shall issue only on affidavit sworn to before the judge or commissioner and establishing the grounds for issuing the warrant. If the judge or commissioner is satisfied that grounds for the application exist or that there is probable cause to believe that they exist, he shall issue a warrant identifying the property and naming or describing the person or place to be searched. The warrant shall be directed to a civil officer of the United States authorized to enforce or assist in enforcing any law thereof or to a person so authorized by the President of the United States. It shall state the grounds or probable cause for its issuance and the names of the persons whose affidavits have been taken in support thereof. It shall command the officer to search forthwith the person or place named for the property specified. The warrant shall direct that it be served in the daytime, but if the affidavits are positive that the property is on the person or in the place to be searched, the warrant may direct that it be served at any time. It shall designate the district judge or the commissioner to whom it shall be returned.</p>
<p>.....</p>
<p>"(g) Scope and Definition. This rule does not modify any act, inconsistent with it, regulating search, seizure and the issuance and execution of search warrants in circumstances for which special provision is made. The term `property' is used in this rule to include documents, books, papers and any other tangible objects."</p>
<p>[6]  Rule 41 has since been amended to read, in part:
</p>
<p>"(a) Authority to issue warrant. A search warrant authorized by this rule may be issued by a federal magistrate or a judge of a state within the district wherein the property sought is located, upon request of a federal law enforcement officer or an attorney for the government.</p>
<p>"(b) Property which may be seized with a warrant. A warrant may be issued under this rule to search for and seize any (1) property that constitutes evidence of the commission of a criminal offense; or (2) contraband, the fruits of crime, or things otherwise criminally possessed; or (3) property designed or intended for use or which is or has been used as the means of committing a criminal offense.</p>
<p>"(c) Issuance and contents. A warrant shall issue only on an affidavit or affidavits sworn to before the federal magistrate or state judge and establishing the grounds for issuing the warrant. If the federal magistrate or state judge is satisfied that grounds for the application exist or that there is probable cause to believe that they exist, he shall issue a warrant identifying the property and naming or describing the person or place to be searched. The finding of probable cause may be based upon hearsay evidence in whole or in part. Before ruling on a request for a warrant the federal magistrate or state judge may require the affiant to appear personally and may examine under oath the affiant and any witnesses he may produce, provided that such proceeding shall be taken down by a court reporter or recording equipment and made part of the affidavit. The warrant shall be directed to a civil officer of the United States authorized to enforce or assist in enforcing any law thereof or to a person so authorized by the President of the United States. It shall command the officer to search, within a specified period of time not to exceed 10 days, the person or place named for the property specified. The warrant shall be served in the daytime, unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime. It shall designate a federal magistrate to whom it shall be returned.</p>
<p>.....</p>
<p>"(h) Scope and definition. This rule does not modify any act, inconsistent with it, regulating search, seizure and the issuance and execution of search warrants in circumstances for which special provision is made. The term `property' is used in this rule to include documents, books, papers and any other tangible objects. The term `daytime' is used in this rule to mean the hours from 6:00 a. m. to 10:00 p. m. according to local time. The phrase `federal law enforcement officer' is used in this rule to mean any government agent, other than an attorney for the government as defined in Rule 54 (c), who is engaged in the enforcement of the criminal laws and is within any category of officers authorized by the Attorney General to request the issuance of a search warrant."</p>
<p>[7]  § 10, <span class="citation no-link">40 Stat. 229</span>.</p>
<p>[8]  "<span class="citation no-link">21 U. S. C. § 879</span>. Search warrants.
</p>
<p>"(a) A search warrant relating to offenses involving controlled substances may be served at any time of the day or night if the judge or United States magistrate issuing the warrant is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time."</p>
<p>[9]  "§ 1405. Issuance of search warrantsprocedure.
</p>
<p>"In any case involving a violation of any provision of part I or part II of subchapter A of chapter 39 of the Internal Revenue Code of 1954 the penalty for which is provided is subsection (a) or (b) of section 7237 of such code, a violation of subsection (c), (h), or (i) of section 2 of the Narcotic Drugs Import and Export Act, as amended (<span class="citation no-link">21 U. S. C., sec. 174</span>), or a violation of the Act of July 11, 1941, as amended (21 U. S. C., sec 184a)</p>
<p>"(1) a search warrant may be served at any time of the day or night if the judge or the United States Commissioner issuing the warrant is satisfied that there is probable cause to believe that the grounds for the application exist, and</p>
<p>"(2) a search warrant may be directed to any officer of the Metropolitan Police of the District of Columbia authorized to enforce or assist in enforcing a violation of any of such provisions."</p>
<p>[10]  See, <i>e. g.,</i> H. R. Rep. No. 2546, 84th Cong., 2d Sess., 16 (1956).</p>
<p>[11]  See, <i>e. g., </i><i>United States</i> v. <i>Stallings,</i> <span class="citation" data-id="9454706"><a href="/opinion/285611/united-states-v-eulice-stallings-william-earl-wilson/" aria-description="Citation for case: United States v. Eulice Stallings, William Earl Wilson">413 F. 2d 200</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/972/">396 U. S. 972</a></span> (1969); <i>United States</i> v. <i>Castle,</i> <span class="citation" data-id="2293098"><a href="/opinion/2293098/united-states-v-castle/" aria-description="Citation for case: United States v. Castle">213 F. Supp. 52</a></span> (DC 1962).
</p>
<p>Our Brother MARSHALL in his dissenting opinion stresses Congress' continuing concern for individual privacy, as demonstrated by the limitations on nighttime searches contained in the Espionage Act, <i>supra,</i> and later, Fed. Rule Crim. Proc 41. The implication seems to be that this concern must be read into the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) to reach the interpretation for which he argues. But this argument totally ignores the fact that Congress, in 1956, enacted a statute governing searches for dangerous drugs which deliberately removed the stricter limitations on night searches found in Rule 41. Our construction of the principal statute considered in this case, <span class="citation no-link">21 U. S. C. § 879</span> (a), therefore, represents no novel departure from previous congressional policy in this area, but is, on the contrary, consistent with the conceded meaning of the statute which governed federal drug searches for almost 15 years.</p>
<p>[12]  The affidavit read in full:
</p>
<p>"BEFORE Lawrence S. Margolis, Wash., D. C. The undersigned being duly sworn deposes and says:</p>
<p>"That he (has reason to believe) that (on the premises known as) 1419 Chapin Street, N. W., as you enter the building last apartment on the right next to the elevator on the first floor Washington in the District of Columbia there is now being concealed certain property, namely heroin, syringes, tourniquets, cookers and paraphernalia used in the preparation of heroin for retail and any other paraphernalia used in the preparation and dispensation of heroin and any other narcotic drugs illegally held, which are in violation of Title 26 U. S. Code Section 4704 (a).</p>
<p>"And that the facts tending to establish the foregoing grounds for issuance of a Search Warrant are as follows: See the facts set forth in the affidavit attached hereto and made a part hereof.</p>
                                   /s/  Marion L. Green
                                        MARION L. GREEN
                                        MPD"

<p>[13]  The affidavit states specifically:
</p>
<p>"I, the undersigned officer who is assigned to the Third District Vice Squad, Metropolitan Police Department, and working in the City of Washington, D. C. in an undercover capacity where illegal drugs are sold and possessed in violation of the United States Code, Title 26, Section 4704a. Had the occasion to investigate the following offense."</p>
<p>[14]  The warrant read in its entirety:
</p>
<p>"To Chief of Police or any Member of MPDC</p>
<p>"Affidavit having been made before me by Plc. Marrion [<i>sic</i>] L. Green, Jr. Third District Vice Squad that he (has reason to believe) that (on the premises known as) 1419 Chapin Street, N. W., as you enter the building last apartment on the right next to the elevator on the first floor, Washington in the District of Columbia, there is now being concealed certain property, namely heroin, capsules, envelopes, syringes, tourniquets, cookers and paraphernalia used in the preparation of heroin for distribution or use and any other instrumentalities or evidence of illegal possession or dispensation of heroin or of any other narcotic drugs illegally held. See the facts set forth in the affidavit attached hereto and made a part hereof which are in violation of Title 26 Section 4704 (a) of the U. S. Code, and as I am satisfied that there is probable cause to believe that the property so described is being concealed on the (premises) above described and that the foregoing grounds for application for issuance of the search warrant exist.</p>
<p>"<i>You are hereby commanded</i> to search forthwith the (place) named for the property specified, serving this warrant and making the search (at any time in the day or night[*]) and if the property be found there to seize it, leaving a copy of this warrant and a receipt for the property taken, and prepare a written inventory of the property seized and return this warrant and bring the property before me within ten days of this date, as required by law.</p>
  "Dated this day of Feb. 11, 1971
                               /s/   Lawrence S. Margolis
                                     U. S. Commissioner"
<p>"[*] The Federal Rules of Criminal Procedure provide: `The warrant shall direct that it be served in the daytime, but if the affidavits are positive that the property is on the person or in the place to be searched, the warrant may direct that it be served at any time.' (Rule 41C)."</p>
<p>[15]  Reply Brief for Petitioner 8.</p>
<p>[16]  The Government contends in its brief, apparently for the first time in the course of this litigation, that the search was not in fact a nighttime search. The primary basis for this argument is revised Fed. Rule Crim. Proc. 41 which states that "[t]he term `daytime' is used in this rule to mean the hours from 6:00 a. m. to 10:00 p. m. according to local time." See n. 6, <i>supra.</i> In view of our conclusion that the standards for a nighttime as well as a daytime search under <span class="citation no-link">21 U. S. C. § 879</span> (a) were met in this case, we do not need to resolve this issue.</p>
<p>[17]  "§ 4704. Packages.
</p>
<p>"(a) General requirement.</p>
<p>"It shall be unlawful for any person to purchase, sell, dispense, or distribute narcotic drugs except in the original stamped package or from the original stamped package; and the absence of appropriate taxpaid stamps from narcotic drugs shall be prima facie evidence of a violation of this subsection by the person in whose possession the same may be found."</p>
<p>[18]  "§ 174. Same; penalty; evidence.
</p>
<p>"Whoever fraudulently or knowingly imports or brings any narcotic drug into the United States or any territory under its control or jurisdiction, contrary to law, or receives, conceals, buys, sells, or in any manner facilitates the transportation, concealment, or sale of any such narcotic drug after being imported or brought in, knowing the same to have been imported or brought into the United States contrary to law, or conspires to commit any of such acts in violation of the laws of the United States, shall be imprisoned not less than five or more than twenty years and, in addition, may be fined not more than $20,000. For a second or subsequent offense (as determined under section 7237 (c) of the Internal Revenue Code of 1954), the offender shall be imprisoned not less than ten or more than forty years and, in addition, may be fined not more than $20,000."</p>
<p>[19]  Petitioner also contended that the officers entered the apartment without knocking and without having a "no-knock" warrant and that the police had no probable cause to search him. Neither court below passed upon the sufficiency of these contentions, and they are not before us here.</p>
<p>[20]  <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1007" aria-description="Citation for case: United States v. Gooding">328 F. Supp., at 1007</a></span>.</p>
<p>[21]  <i><span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/" aria-description="Citation for case: United States v. Gooding">Id.,</a></span></i> at 1008 n. 1.</p>
<p>[22]  <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1008" aria-description="Citation for case: United States v. Gooding"><i>Id.,</i> at 1008</a></span>.</p>
<p>[23]  155 U. S. App. D. C. 259, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428</a></span> (1973).</p>
<p>[24]  Judge Wilkey stated in his opinion: "We hold that the applicable statute, <span class="citation no-link">21 U. S. C. § 879</span> (a), requires only a showing of probable cause to believe that the narcotics will be found on the premises at any time of the day or night." <span class="citation no-link"><i>Id.,</i> at 266</span>, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#435" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 435</a></span>. Judge Fahy in his opinion stated: "Thus, in the case of narcotics, previously under Section 1405 (1) and later under Section 879 (a), if the judge was satisfied `that there is probable cause to believe' rather than `if the affidavits are positive' that the `property is on the person or in the place to be searched,' the warrant could permit execution at any time." <i>Id.,</i> at 268, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#437" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 437</a></span>.</p>
<p>[25]  Judge Robinson concluded: "The test of reasonable cause for nighttime execution does not demand a demonstration that drugs are positively on the premises at night, or that they could be found on the premises only at night, or that for some reason a search would be impossible in the daytime. It does summon some factual basis for a prudent conclusion that the greater intrusiveness of nighttime execution of the warrant is justified by the exigencies of the situation." <i>Id.,</i> at 274, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#443" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 443</a></span>. Judge Robinson then went on to find that a proper showing had been made in this case. He stated: "Where, as here, it appears that a search is calculated not only to garner evidence of past crime but also to terminate a serious species of ongoing criminality, reasonable cause for a nocturnal intrusion is demonstrated." <i>Id.,</i> at 275, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#444" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 444</a></span>.</p>
<p>[26]  We are therefore not required to reach the Government's argument that, despite the fact that the application for the search warrant alleged a violation of the United States Code, the search could be justified under D. C. Code § 33-414 as a search for violations of local drug laws.</p>
<p>[27]  The provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) prevail over the provisions of Fed. Rule Crim. Proc. 41 when controlled substances are involved. See nn. 10 and 11, <i>supra.</i></p>
<p>[28]  See n. 9, <i>supra.</i></p>
<p>[29]  For example, John Ingersoll, Director of the Bureau of Narcotics and Dangerous Drugs, stated at the Hearings on Drug Abuse Control Amendments1970 before the Subcommittee on Public Health and Welfare of the House Committee on Interstate and Foreign Commerce, 91st Cong., 2d Sess., ser. 91-45, pt. 1, p. 86 (1970), that the no-knock provision, incorporated in § 702 (b) of the proposed bill, see n. 32, <i>infra,</i> would grant authority "restricted to special agents of the Bureau of Narcotics and Dangerous Drugs." In addition, the preceding provision of the bill set forth expanded powers for the agents of the BNDD. However, although these excerpts would argue for petitioner's position here, we believe that the Government's position ultimately proves to be stronger. We believe for the reasons stated in the text that the emphasis on the powers of the BNDD agents was not intended to remove powers from other federal agents who had previously assisted in the enforcement of federal drug laws. See also <span class="citation no-link">18 U. S. C. §§ 3052</span>, 3053, and 3056, setting forth arrest powers for agents of the Federal Bureau of Investigation, United States marshals, and Secret Service agents.</p>
<p>[30]  S. Rep. No. 91-613, p. 3 (1969).</p>
<p>[31]  D. C. Code § 4-138 provides:
</p>
<p>"Any warrant for search or arrest, issued by any magistrate of the District, may be executed in any part of the District by any member of the police force, without any backing or indorsement of the warrant, and according to the terms thereof; and all provisions of law in relation to bail in the District shall apply to this chapter." See <i>Thomas</i> v. <i>United States,</i> <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/#993" aria-description="Citation for case: Thomas v. United States">409 U. S. 992, 993</a></span> (1973) (DOUGLAS, J., dissenting).</p>
<p>[32]  "§ 879. Search warrants.
</p>
<p>.....</p>
<p>"(b) Any officer authorized to execute a search warrant relating to offenses involving controlled substances the penalty for which is imprisonment for more than one year may, without notice of his authority and purpose, break open an outer or inner door or window of a building, or any part of the building, or anything therein, if the judge or United States magistrate issuing the warrant (1) is satisfied that there is probable cause to believe that (A) the property sought may and, if such notice is given, will be easily and quickly destroyed or disposed of, or (B) the giving of such notice will immediately endanger the life or safety of the executing officer or another person, and (2) has included in the warrant a direction that the officer executing it shall not be required to give such notice. Any officer acting under such warrant, shall, as soon as practicable after entering the premises, identify himself and give the reasons and authority for his entrance upon the premises."</p>
<p>See H. R. Rep. No. 91-1444, p. 25 (1970), which stated:</p>
<p>"The purpose of this provision [the no-knock provision], as explained in the hearings, is to provide law enforcement officials with a tool to aid in combatting the illicit traffic in drugs which has proved helpful in all of the 29 States where this authority exists either by statute or common law."</p>
<p>[33]  See Atty. Gen. Order 510-73, <span class="citation no-link">38 Fed. Reg. 7244</span>-7245.</p>
<p>[34]  The effect of Title 23 on other statutes was debated in some detail below. Judge Wilkey in his opinion noted that the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) were not only enacted after the provisions of Title 23 (although they took effect sooner), but also are more specific in terms of subject matter, <i>i. e.,</i> drug control. 155 U. S. App. D. C., at 262, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#431" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 431</a></span>. Thus, as a matter of statutory construction, it is somewhat difficult to see how Title 23 was intended to modify any later, more specific statute. Petitioner no longer suggests that Title 23 must be read into the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a). He contends either that Title 23 is applicable in its entirety or that § 879 (a) by its own terms requires a special showing for searches at night.</p>
<p>[35]  D. C. Code § 11-901.</p>
<p>[36]  "Rule 41. Search and Seizure.
</p>
<p>"(a) Authority to Issue Warrant. A search warrant authorized by this rule may be issued by a judge of the Superior Court.</p>
<p>"(b) Grounds for Issuance. A warrant may be issued under this rule to search for and seize property. Property is subject to seizure pursuant to a search warrant if there is probable cause to believe that it (1) is stolen or embezzled; or (2) is contraband or otherwise illegally possessed; or (3) has been used or is possessed for the purpose of being used, or is designed or intended to be used, to commit or conceal the commission of an offense; or (4) constitutes evidence of or tends to demonstrate the commission of an offense or the identify of a person participating in the commission of an offense.</p>
<p>"(c) Application for Search Warrants. Each application for a search warrant shall be made in writing upon oath to a judge of the Superior Court. Each application shall include the name and title of the applicant; a statement that there is probable cause to believe that property described in paragraph (b) as subject to seizure is likely to be found in a designated premise, in a designated vehicle or object, or upon designated persons; allegations of fact supporting such statement; and a request that the judge issue a search warrant directing a search for and seizure of the property in question. The applicant may also submit depositions or affidavits of other persons containing allegations of fact supporting or tending to support those contained in the application.</p>
<p>"The application may also contain (1) a request that the search warrant be made executable at any hour of the day or night, upon the ground that (i) there is probable cause to believe that it cannot be executed during the hours of daylight, or (ii) the property sought is likely to be removed or destroyed if not seized forthwith, or (iii) the property sought is not likely to be found except at certain times or in certain circumstances; and (2) a request approved by an appropriate prosecutor that the search warrant authorize the executing officer to break and enter dwelling houses or other buildings or vehicles to be searched without giving notice of his identity and purpose, upon probable cause to believe that one of the conditions listed in subparagraphs (a), (b), or (d) of D. C. Code § 23-591 (c) (2) is likely to exist at the time and place at which such warrant is to be executed whereby the applicant may dispense with such requirement. Any request that a search warrant be executable at any time of the day or night or that a search warrant authorize the executing officer to break and enter without a prior announcement of his identity and purpose must be accompanied and supported by allegations of fact supporting such request." Effective Oct. 25, 1973, paragraph (b) of this rule was amended. Paragraphs (a) and (c) were unchanged.</p>
<p>[37]  We note that the District of Columbia Court of Appeals has indicated that the specific provisions of Title 33 are not qualified by the more general provisions of Title 23 in searches for violations of the local drug laws in the District of Columbia. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="9751925"><a href="/opinion/2307321/united-states-v-thomas/#167" aria-description="Citation for case: United States v. Thomas">294 A. 2d 164, 167-168</a></span>, cert. denied, <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/" aria-description="Citation for case: Thomas v. United States">409 U. S. 992</a></span> (1973).</p>
<p>[38]  See Fed. Rule Crim. Proc. 41 (h), <i>supra,</i> n. 6. See also subsection (g) of prior Rule 41, n. 5, <i>supra.</i></p>
<p>[39]  S. Rep. No. 91-613, pp. 30-31 (1969). See also H. R. Rep. No. 91-1444, pt. 1, p. 54 (1970).</p>
<p>[40]  See n. 11, <i>supra.</i></p>
<p>[41]  The debates on this controversial proposal may be found generally in volume 116 of the Congressional Record. See, <i>e. g.,</i> 116 Cong. Rec. 1159-1162, 1164-1177, 33639-33645.</p>
<p>[42]  We note that the Court of Appeals for the Fifth Circuit has recently reached the same conclusion. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="315831"><a href="/opinion/315831/united-states-v-titus-thomas-aka-tee/" aria-description="Citation for case: United States v. Titus Thomas, AKA Tee">489 F. 2d 664</a></span> (1973).</p>
<p>[1]  D. C. Code § 23-523 (b) directs that all search warrants are to be executed only during daylight hours, absent express authorization pursuant to D. C. Code § 23-521 (f). Section 23-521 (f) (5) allows authorization for nighttime execution where the "judicial officer has found cause therefore, including one of the grounds set forth in section 23-522 (c) (1) . . . ."</p>
<p>[2]  Thus various rules are applicable in the United States District Court for the District of Columbia which are not applicable in district courts elsewhere in the country. See, <i>e. g.,</i> D. C. Code § 23-1322, dealing with detention prior to trial.</p>
<p>[3]  Hearings on Crime in the National Capital before the Senate Committee on the District of Columbia, 91st cong., 1st Sess., pt. 4, p. 1404 (1969).</p>
<p>[4]  S. Rep. No. 91-538, p. 12 (1969).</p>
<p>[1]  Similarly, most of the States' laws provide that search warrants may only be served during the day unless express authorization for a nighttime search is obtained, and such authorization can generally be obtained only by meeting special requirements for a nighttime search. See L. Hall, Y. Kamisar, W. LaFave &amp; J. Israel, Modern Criminal Procedure 259 (3d ed. 1969).</p>
<p>[2]  In an effort to conjure up ambiguity in the statutory language, the Court argues that the statute could have been drawn with more precision, and specifically points out that read literally, the statutory requirement of cause "for its service at such time" would seem to apply to daytime searches as well as those conducted at night. <i>Ante,</i> at 455-456. I readily agree that the statute could have been more artfully drafted, but the fact that it could have been stated in different words hardly justifies disregarding the plain meaning of the statutory language with which we must deal. It ill suits the Court to suggest that this language is ambiguous when the Court is unable to come forward with any plausible alternative construction.
</p>
<p>The Court's suggestion that the statute is ambiguous because it could be literally applied to daytime searches as well as those during the night is wholly insubstantial. As the Court well knows, no one has ever proposed that an additional burden of justification for daytime searches is necessary or appropriate; in sharp contrast, the Congress has consistently acted to protect nighttime privacy through such an additional burden on nighttime searches. The Court's confusion arises only because the words "at such time" in the statute logically refer back to its authorization of service "at any time of the day or night." But this latter phrase has consistently been used in congressional enactments as a shorthand expression for a warrant whose service at night is authorized, see, <i>e. g.,</i> D. C. Code § 33-414 (h), <i>ante,</i> at 433 n. 3; §§ 23-521 (f) (5), 23-522 (c) (1), <i>ante,</i> at 435-436, n. 4; cf. former Fed. Rule Crim. Proc. 41 (c), <i>ante,</i> at 436-437, n. 5, to distinguish such a warrant from any other warrant, which may be served only in the day. Plainly the statute's requirement of cause "for its service at such time" was intended to apply only to nighttime execution of search warrants.</p>
<p>As for the Court's complaint that a requirement of cause for nighttime service of a warrant is not the "traditional limitation" imposed upon nighttime searches, it should suffice to point out that Congress became aware in its consideration of the D. C. Court Reform and Criminal Procedure Act in 1969 that a requirement of cause would provide <i>greater</i> protection for nighttime privacy than the old positivity test, by eliminating unnecessary nighttime searches regardless of how sure police were of their basis for the search. See Hearings on Crime in the National Capital before the Senate Committee on the District of Columbia, 91st Cong., 1st Sess., pt. 4, p. 1404 (1969); Brief for United States 49-50. This change was therefore incorporated into the D. C. Code, see D. C. Code §§ 23-521 to 23-523. It was also adopted in the 1972 amendment to Rule 41. It would hardly be surprising for the Congress to introduce a modification along the same lines into § 879 (a).</p>

</div>
```

---
