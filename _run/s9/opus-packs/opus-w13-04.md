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

## GROUP: _overhaul2/lake/cases/United States v. $8,850 in Currency.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: "United States v. $8,850 in Currency"
type: case
citation: "461 U.S. 555 (1983)"
parallel_cite: "103 S. Ct. 2005; 76 L. Ed. 2d 143; 51 U.S.L.W. 4587"
neutral_cite: 1983 U.S. LEXIS 34
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-05-23
docket: No. 81-1062
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
  opinion_url: "https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/"
  cluster_id: 110936
  opinion_id: null
  identity_checked: true
lake:
  record_id: "United States v. $8,850 in Currency"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. James Daniel Good Real Property]]"
tags:
  - case
  - civil-forfeiture
  - due-process
  - delay
  - customs
  - currency-reporting
holding: "An 18-month delay between the customs seizure of currency and the Government's filing of a civil forfeiture action did not deny the claimant due process; whether a delay in instituting a forfeiture proceeding is reasonable is measured by the four-factor balancing test of Barker v. Wingo — the length of the delay, the reason for it, the claimant's assertion of the right to a hearing, and prejudice to the claimant."
aliases:
  - "United States v. $8,850 in Currency"
  - "United States v. $8,850"
  - United States v. Eight Thousand Eight Hundred and Fifty Dollars
---

# United States v. $8,850 in Currency

*461 U.S. 555 (1983)* (No. 81-1062) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110936 → combined opinion 110936 (O'Connor, J.; 461 U.S. 555, argued Jan. 18, 1983, decided May 23, 1983). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted opening holding sits between `*556` and `*557`, i.e., on page 556; internal citation to *Barker* elided). S9 promotes. -->

## Background
On September 10, 1975, Mary Josephine Vasquez arrived at Los Angeles International Airport after a short trip to Canada and declared to customs that she was not carrying more than $5,000; an inspector nonetheless found and seized $8,850 in currency she had failed to report under the Bank Secrecy Act. Vasquez petitioned the Customs Service for remission or mitigation, and a parallel criminal prosecution followed. The Government did not file a civil action to forfeit the currency until roughly 18 months after the seizure. The District Court found the delay reasonable and declared the currency forfeited, but a divided panel of the Ninth Circuit reversed, holding the delay violated due process.

## Issue
Whether the Government's 18-month delay between seizing the currency and filing a civil forfeiture proceeding deprived the claimant of property without due process of law.

## Rule
The Court held that the question is not answered by a fixed limitations period but by a contextual balancing borrowed from the speedy-trial setting, because a claimant's core complaint about forfeiture delay — being kept from a hearing at a meaningful time — mirrors the concern behind the right to a speedy trial. It therefore held: "We conclude that the four-factor balancing test of *Barker* v. *Wingo* ... provides the relevant framework for determining whether the delay in filing a forfeiture action was reasonable." — 461 U.S. at 556. The four *Barker* factors are the length of the delay, the reason for the delay, the claimant's assertion of the right to a hearing, and prejudice to the claimant. ^pin-556

## Application
Weighing those factors, the Court found no unreasonable delay. Much of the elapsed time was attributable to the claimant's own pending administrative petition for remission and to a parallel criminal proceeding whose outcome the Government could reasonably await; the reasons for the delay were legitimate rather than a tactic to gain advantage. Critically, Vasquez had not asserted a right to an earlier judicial hearing — she could have forced the issue but did not — and she neither claimed nor showed that the delay prejudiced her ability to defend the forfeiture. On balance, the delay did not deny due process.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. O'Connor, J., delivered the opinion of the Court. Stevens, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *$8,850* is the timing anchor for civil forfeiture: the Government's delay in commencing a forfeiture action is tested under the *Barker v. Wingo* balancing factors rather than a rigid deadline, with the claimant's failure to demand a prompt hearing and the absence of prejudice weighing heavily. Teach it with *[[United States v. James Daniel Good Real Property]]* (1993), which governs the distinct question of *pre*-deprivation notice and hearing before the Government seizes real property.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. $8,850 in Currency*, 461 U.S. 555 (1983)](https://www.courtlistener.com/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/) — pinpoint: 556 (O'Connor, J., for the Court; the CL opinion text places the quoted opening holding between the reporter stars `*556` and `*557`, i.e., on page 556). Rule quote string-matched to the CL opinion text 2026-07-07 (the internal citation to *Barker v. Wingo* is elided).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "70362db4c085e93a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. $8,850 in Currency"}, "payload": {"all": [{"cite": "461 U.S. 555", "page": "555", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "461"}, {"cite": "103 S. Ct. 2005", "page": "2005", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "76 L. Ed. 2d 143", "page": "143", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "76"}, {"cite": "1983 U.S. LEXIS 34", "page": "34", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4587", "page": "4587", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "461 U.S. 555", "official": {"cite": "461 U.S. 555", "page": "555", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "461"}, "official_selection_present": true, "record_id": "United States v. $8,850 in Currency"}}
{"assertion_id": "c02d4d25f9723b81", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. $8,850 in Currency"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. $8,850 in Currency", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. $8,850 in Currency

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. $8,850 in Currency",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Eight Thousand Eight Hundred & Fifty Dollars",
    "case_name_short": "$8,850",
    "case_name_full": "United States v. Eight Thousand Eight Hundred and Fifty Dollars ($8,850) in United States Currency",
    "input_case_name": "United States v. $8,850 in Currency",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-05-23",
    "year": 1983,
    "docket": "No. 81-1062",
    "cluster_id": 110936,
    "lead_opinion_id": 9429199,
    "sibling_ids": [],
    "absolute_url": "/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "461 U.S. 555",
      "volume": "461",
      "reporter": "U.S.",
      "page": "555",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "461 U.S. 555",
        "volume": "461",
        "reporter": "U.S.",
        "page": "555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2005",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2005",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 L. Ed. 2d 143",
        "volume": "76",
        "reporter": "L. Ed. 2d",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 34",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "34",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4587",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4587",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "461 U.S. 555",
    "official_selection": {
      "court_class": "scotus",
      "selected": "461 U.S. 555",
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
    "date_created": "2026-07-06T13:41:57Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-8-850-in-currency--110936",
      "to_record_id": "United States v. $8,850 in Currency",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. $8,850 in Currency

```
<opinion type="majority">
<author id="b614-10">Justice O’Connor</author>
<p id="A8h">delivered the opinion of the Court.</p>
<p id="Aeo">United States Customs officials seized $8,850 in currency from the claimant as she passed through customs at Los Angeles International Airport. The question in this case is whether the Government’s 18-month delay in filing a civil proceeding for forfeiture of the currency violates the claimant’s right to due process of law. We conclude that the four-factor balancing test of <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), provides the relevant framework for determining whether the delay in filing a forfeiture action was reasonable. Applying the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test to the circumstances of this case, we find no unreasonable delay.</p>
<p id="AkG"><page-number citation-index="1" label="557">*557</page-number>I</p>
<p id="A2q">A</p>
<p id="Avp">Section 231 of the Bank Secrecy Act of 1970, <span class="citation no-link">84 Stat. 1122</span>, <span class="citation no-link">31 U. S. C. § 1101</span>, requires persons knowingly transporting monetary instruments exceeding $5,000 into the United States to file a report with the Customs Service declaring the amount being transported. Congress has authorized the Government to seize and forfeit any monetary instruments for which a required report was not filed. <span class="citation no-link">31 U. S. C. § 1102</span>(a). Since the Bank Secrecy Act does not specify the procedures to be followed in seizing monetary instruments, the Customs Service generally follows the procedures governing forfeitures for violations of the customs laws, as set forth in <span class="citation no-link">19 U. S. C. § 1602</span> <em>et seq. </em>(1976 ed. and Supp. V), and the implementing regulations. Under these procedures, the Customs Service notifies any person who appears to have an interest in the seized property of the property’s liability to forfeiture and of the claimant’s right to petition the Secretary of the Treasury for remission or mitigation of the forfeiture.<footnotemark>1</footnotemark> See <span class="citation no-link">19 CFR § 162.31</span>(a) (1982). The regulations require a claimant to file the petition within 60 days. <span class="citation no-link">19 CFR § 171.12</span>(b) (1982).</p>
<p id="Asa">If the claimant does not file a petition, or if the decision on a petition makes legal proceedings appear necessary,<footnotemark>2</footnotemark> the appropriate customs officer must prepare a full report of the <page-number citation-index="1" label="558">*558</page-number>seizure for the United States Attorney. <span class="citation no-link">19 U. S. C. § 1603</span> (1976 ed., Supp. V).<footnotemark>3</footnotemark> Upon receipt of a report, the United States Attorney is required “immediately to inquire into the facts” and, if it appears probable that a forfeiture has been incurred, “forthwith to cause the proper proceedings to be commenced and prosecuted, without delay.” <span class="citation no-link">19 U. S. C. § 1604</span> (1976 ed., Supp. V). After a case is reported to the United States Attorney for institution of legal proceedings, no administrative action may be taken on any petition for remission or mitigation. <span class="citation no-link">19 CFR § 171.2</span>(a) (1982).</p>
<p id="b616-5">The Customs Service processes over 50,000 noncontra-band forfeitures per year. U. S. Customs Service, Customs U. S. A. 36 (1982). In 90% of all seizures, the claimant files an administrative petition for remission or mitigation. Brief for United States 7. The Secretary in turn grants at least partial relief for an estimated 75% of the petitions. <em><span class="citation no-link">Ibid.</span> </em>Typically, this relief terminates the dispute without the filing of a forfeiture action in district court.</p>
<p id="b616-6">B</p>
<p id="b616-7">On September 10, 1975, claimant Mary Josephine Vasquez and a companion arrived at Los Angeles International Airport after a short visit to Canada. During customs processing, Vasquez declared that she was not carrying more than $5,000 in currency. Nevertheless, a customs inspector discovered and seized $8,850 in United States currency from her. On September 18, 1975, the Customs Service officially informed Vasquez by letter that the seized currency was subject to forfeiture and that she had the right to petition for re<page-number citation-index="1" label="559">*559</page-number>mission or mitigation. A week later, Vasquez filed a petition for remission or mitigation,<footnotemark>4</footnotemark> asserting that the violation was unintentional because she had mistakenly believed she was required to declare only funds that had been obtained in another country and that she had brought the seized funds with her from the United States.</p>
<p id="b617-5">On October 20, 1975, the Customs Office of Investigation assigned Special Agent Pompeo to investigate the petition. Within a few days, Agent Pompeo had interviewed the customs inspectors at the airport who were involved in the seizure. After several unsuccessful attempts to contact him, in mid-November Agent Pompeo contacted Vasquez’ attorney to arrange an interview with Vasquez. The attorney was unable to meet at that time, and he desired to be present during the interview with his client. Around this time, Agent Pompeo also opened a criminal file because she suspected Vasquez of smuggling drugs. From November 1975 until April 1976, Agent Pompeo contacted various state, federal, and Canadian law enforcement officials to determine whether the seized currency was part of a narcotics transaction.<footnotemark>5</footnotemark></p>
<p id="b617-6">In January 1976, Vasquez’ attorney inquired about the status of the petition, and was informed it was still under investigation. On March 2, 1976, Agent Pompeo again contacted the attorney regarding an interview with Vasquez, and an interview took place three days later. On April 26, 1976, the attorney again inquired about the status of the petition and requested that it be acted on as soon as possible. Also in April 1976, Agent Pompeo received final reports from the law enforcement agencies. From these reports, Agent <page-number citation-index="1" label="560">*560</page-number>Pompeo concluded there was no evidence to support a charge of narcotics violations.</p>
<p id="b618-5">In May 1976, Agent Pompeo submitted a report to the United States Attorney, recommending prosecution of Vasquez for the reporting violation. After Agent Pompeo re-interviewed the customs agents and reported her findings, the United States Attorney submitted the case to the grand jury. On June 15, 1976, a grand jury returned an indictment charging Vasquez with the felony of knowingly and willfully making false statements to a United States Customs officer, in violation of <span class="citation no-link">18 U. S. C. § 1001</span>; and with the misdemeanor of knowingly and willfully transporting $8,850 into the United States without filing a report, in violation of <span class="citation no-link">31 U. S. C. §§ 1058</span> and 1101. The indictment sought forfeiture of the currency as part of the misdemeanor count.</p>
<p id="b618-6">In August 1976, Agent Pompeo recommended that disposition of the remission petition be withheld until the currency was no longer needed as evidence at the criminal trial. On December 24, 1976, Vasquez was convicted on the felony count but acquitted on the misdemeanor charge of willfully failing to file a currency report.<footnotemark>6</footnotemark> Four days after the criminal trial was completed, Vasquez' attorney again inquired whether there would be any further delay in acting on the petition.</p>
<p id="b618-7">On March 10,1977, the Customs Service informed Vasquez that the claim of forfeiture had been referred to the United States Attorney. Within two weeks, a complaint seeking forfeiture under <span class="citation no-link">31 U. S. C. § 1102</span> was filed in Federal District Court.<footnotemark>7</footnotemark> In answer to the complaint, Vasquez admitted the factual allegations but asserted as one of several affirma<page-number citation-index="1" label="561">*561</page-number>tive defenses that the Government’s “dilatory processing” of her petition for remission or mitigation and “dilatory” commencement of the civil forfeiture action violated her right to due process. The District Court, after a 2-day bench trial held in January 1978, determined that the time which had elapsed was reasonable under the circumstances and therefore declared the currency forfeited under <span class="citation no-link">31 U. S. C. § 1102</span>.</p>
<p id="b619-4">A divided panel of the Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="9467783"><a href="/opinion/389222/united-states-v-eight-thousand-eight-hundred-fifty-dollars-885000-in/" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred Fifty...">645 F. 2d 836</a></span> (1981). Proceeding from the premise that the Government must bring forfeiture actions promptly because seizures infringe upon property rights, the Court of Appeals concluded that the Government’s 18-month delay in filing its forfeiture action was unjustified. The Court of Appeals specifically held that pending administrative or criminal investigations cannot justify the delay when the necessary elements for a forfeiture were established at the time of the seizure and when the claimant seeks a speedy resolution of the claim. The Court of Appeals likewise rejected the Government’s argument that the claimant should be required to show that the delay prejudiced her ability to present a defense to the forfeiture action. As a remedy for the due process violation, the Court of Appeals ordered dismissal of the Government’s forfeiture action.<footnotemark>8</footnotemark></p>
<p id="b619-5">Since other Circuits have determined that pending criminal<footnotemark>9</footnotemark> or administrative<footnotemark>10</footnotemark> investigations and prejudice to the claimant<footnotemark>11</footnotemark> are relevant considerations in determining <page-number citation-index="1" label="562">*562</page-number>whether a delay in instituting forfeiture proceedings violates due process, we granted certiorari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./455/1015/">455 U. S. 1015</a></span> (1982). We reverse.</p>
<p id="b620-3">II</p>
<p id="A8V">The due process issue presented here is a narrow one. Vasquez concedes that the Government could constitutionally seize her property without a prior hearing.<footnotemark>12</footnotemark> Nor does Vasquez challenge the sufficiency of the judicial hearing that was eventually held. She argues only that the Government’s delay in filing a civil forfeiture proceeding violated her due process right to a hearing “‘at a meaningful time,”’ <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#80" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 80</a></span> (1972), quoting <em>Armstrong </em>v. <em>Manzo, </em><span class="citation" data-id="107034"><a href="/opinion/107034/armstrong-v-manzo/#552" aria-description="Citation for case: Armstrong v. Manzo">380 U. S. 545, 552</a></span> (1965). Unlike the situation where due process requires a prior hearing, there is no obvious bright line dictating when a postseizure hearing must occur. Because our prior cases in this area have wrestled with whether due process requires a preseizure hearing, we have not previously determined when a postseizure delay may be<page-number citation-index="1" label="563">*563</page-number>come so prolonged that the dispossessed property owner has been deprived of a meaningful hearing at a meaningful time.<footnotemark>13</footnotemark></p>
<p id="b621-5">The Government argues that there is no general due process requirement of prompt postseizure filing of a judicial forfeiture action. Rather, the Government urges that the standard for assessing the timeliness of the suit be the same as that employed for due process challenges to delay in instituting criminal prosecutions. As articulated in <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783</a></span> (1977), such claims can prevail only upon a showing that the Government delayed seeking an indictment in a deliberate attempt to gain an unfair tactical advantage over the defendant or in reckless disregard of its probable prejudicial impact upon the defendant’s ability to defend against the charges. The Government argues that in the absence of unfair conduct of this sort, the timeliness of the suit is controlled only by the applicable statute of limitations. Here, Congress has required the Government to institute forfeiture proceedings within five years. <span class="citation no-link">19 U. S. C. §1621</span> (1976 ed., Supp. V).</p>
<p id="b621-6">We reject the Government’s suggestion that <em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">Lovasco</a></span> </em>provides the appropriate test for determining whether the delay violates the due process command. <em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/" aria-description="Citation for case: United States v. Lovasco">Lovasco</a></span> </em>recognized that the interests of the suspect and society are better served if, absent bad faith or extreme prejudice to the defendant, the prosecutor is allowed sufficient time to weigh and sift evidence to ensure that an indictment is well founded. While the <page-number citation-index="1" label="564">*564</page-number>value of allowing the Government time to pursue its investigation applies to the civil forfeiture situation as well as the criminal proceeding, a major distinction exists. A suspect who has not been indicted retains his liberty; a claimant whose property has been seized, however, has been entirely deprived of the use of the property.</p>
<p id="b622-5">A more apt analogy is to a defendant’s right to a speedy trial once an indictment or other formal process has issued. In that situation, the defendant no longer retains his complete liberty. Even if he is allowed to post bail, his liberty is subject to the conditions required by his bail agreement. In <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), we developed a test to determine when Government delay has abridged the right to a speedy trial. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test involves a weighing of four factors: length of delay, the reason for the delay, the defendant’s assertion of his right, and prejudice to the defendant. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#530" aria-description="Citation for case: Barker v. Wingo"><em>Id., </em>at 530</a></span>.</p>
<p id="b622-6">Of course, <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>dealt with the Sixth Amendment right to a speedy trial rather than the Fifth Amendment right against deprivation of property without due process of law. Nevertheless, the Fifth Amendment claim here — which challenges only the length of time between the seizure and the initiation of the forfeiture trial — mirrors the concern of undue delay encompassed in the right to a speedy trial. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>balancing inquiry provides an appropriate framework for determining whether the delay here violated the due process right to be heard at a meaningful time. We have often repeated the seminal statement from <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#481" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471, 481</a></span> (1972), that “due process is flexible and calls for such procedural protections as the particular situation demands.” <em>E. g., Schweiker </em>v. <em>McClure, </em><span class="citation" data-id="110694"><a href="/opinion/110694/schweiker-v-mcclure/#200" aria-description="Citation for case: Schweiker v. McClure">456 U. S. 188, 200</a></span> (1982); <em>Memphis Light, Gas &amp; Water Division </em>v. <em>Craft, </em><span class="citation" data-id="9427172"><a href="/opinion/109855/memphis-light-gas-water-division-v-craft/#14" aria-description="Citation for case: Memphis Light, Gas &amp; Water Division v. Craft">436 U. S. 1, 14-15, n. 15</a></span> (1978). The flexible approach of <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>which “necessarily compels courts to approach speedy trial cases on an <em>ad hoc </em>basis,” 407 U. S., at 530, is thus an appropriate inquiry for determining whether <page-number citation-index="1" label="565">*565</page-number>the flexible requirements of due process have been met. As we stressed in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>none of these factors is a necessary or sufficient condition for finding unreasonable delay. Rather, these elements are guides in balancing the interests of the claimant and the Government to assess whether the basic due process requirement of fairness has been satisfied in a particular case.<footnotemark>14</footnotemark></p>
<p id="b623-5">III</p>
<p id="b623-6">In applying the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>balancing test to this situation, the overarching factor is the length of the delay. As we said in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>, </em>the length of the delay “is to some extent a triggering mechanism.” <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Ibid.</a></span> </em>Little can be said on when a delay becomes presumptively improper, for the determination necessarily depends on the facts of the particular case. Our inquiry is the constitutional one of due process; we are not establishing a statute of limitations. Obviously, short delays — of perhaps a month or so — need less justification than longer delays. We regard the delay here — some 18 months— as quite significant. Being deprived of this substantial sum of money for a year and a half is undoubtedly a significant burden.</p>
<p id="b623-7">Closely related to the length of the delay is the reason the Government assigns to justify the delay. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#531" aria-description="Citation for case: Barker v. Wingo"><em>Id., </em>at 531</a></span>. The Government must be allowed some time to decide whether to institute forfeiture proceedings. The customs official’s decision to seize property is of necessity a hasty one. Both the Government and the claimant have an interest in a rule that allows the Government some time to investigate the situation in order to determine whether the facts entitle the Government to forfeiture so that, if not, the Government may return the money without formal proceedings. Cf. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#791" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em><page-number citation-index="1" label="566">*566</page-number>at 791</a></span>. Normally, investigating officials can make such a determination fairly quickly, so that this reason alone could only rarely justify a lengthy delay.</p>
<p id="b624-5">An important justification for delaying the initiation of forfeiture proceedings is to see whether the Secretary’s decision on the petition for remission will obviate the need for judicial proceedings. This delay can favor both the claimant and the Government. Cf. <span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#521" aria-description="Citation for case: Barker v. Wingo"><em>Barker, supra, </em>at 521</a></span>; <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#794" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 794-795</a></span>. In many cases, the Government’s entitlement to the property is clear, and the claimant’s only prospect for reacquiring the property is that the Secretary will favorably exercise his discretion and allow remission or mitigation. If the Government were forced to initiate judicial proceedings without regard to administrative proceedings, the claimant would lose this benefit. Further, administrative proceedings are less formal and expensive than judicial forfeiture proceedings. Given the great percentage of successful petitions, allowing the Government to wait for action on administrative petitions eliminates unnecessary and burdensome court proceedings. Finally, a system whereby the judicial proceeding occurs after administrative action spares litigants and the Government from the burden of simultaneously participating in two forums.<footnotemark>15</footnotemark></p>
<p id="b624-6">The Government takes the extreme position, however, that a pending administrative petition should completely toll the requirement of filing a judicial proceeding. Nothing in the statutory scheme or in our cases supports this argument. A claimant need not waive his right to a prompt judicial hearing simply because he seeks the additional remedy of an administrative petition for mitigation.<footnotemark>16</footnotemark> Unreasonable delay <page-number citation-index="1" label="567">*567</page-number>in processing the administrative petition cannot justify prolonged seizure of his property without a judicial hearing. Rather, the pendency of an administrative petition is simply a weighty factor in the flexible balancing inquiry.</p>
<p id="b625-5">Pending criminal proceedings present similar justifications for delay in instituting civil forfeiture proceedings. A prior or contemporaneous civil proceeding could substantially hamper the criminal proceeding, which — as here — may often include forfeiture as part of the sentence. A prior civil suit might serve to estop later criminal proceedings and may provide improper opportunities for the claimant to discover the details of a contemplated or pending criminal prosecution. Compare Federal Rule of Civil Procedure 26(b) with Federal Rule of Criminal Procedure 16. In some circumstances, a civil forfeiture proceeding would prejudice the claimant’s ability to raise an inconsistent defense in a contemporaneous criminal proceeding. See, <em>e. g., United States </em>v. <em>U. S. Currency, </em><span class="citation" data-id="9466912"><a href="/opinion/380368/united-states-v-u-s-currency/" aria-description="Citation for case: United States v. U. S. Currency">626 F. 2d 11</a></span> (CA6 1980). Again, however, the pendency of criminal proceedings is only an element to be considered in determining whether delay is unreasonable. Although federal criminal proceedings are generally fairly rapid since the advent of the Speedy Trial Act of 1974, <span class="citation no-link">18 U. S. C. § 3161</span> <em>et seq. </em>(1976 ed. and Supp. V), the pendency of a trial does not automatically toll the time for instituting a forfeiture proceeding.</p>
<p id="b625-6">In this case the Government relies on both a pending petition for mitigation or remission and a pending criminal proceeding to justify the delay in filing civil forfeiture proceedings. During the initial seven months after the seizure the Customs Service was determining whether to grant the petition. This investigation required responses to inquiries to state, federal, and Canadian law enforcement officers. Such an investigation inherently is time consuming, and there is no <page-number citation-index="1" label="568">*568</page-number>indication that it was not pursued with diligence. The Customs Service then referred the matter to the United States Attorney, who obtained criminal indictments within two months. Importantly, one count of the indictment sought forfeiture as part of the sentence. If the Government had prevailed, a civil forfeiture would have been rendered unnecessary. There is no evidence in the record that the Government was responsible for the slow pace of the criminal proceedings, which reached a verdict five months later. After the criminal trial ended, the Secretary of the Treasury made a final decision within three months to deny the petition, and the United States Attorney promptly filed a civil forfeiture proceeding.</p>
<p id="b626-5">We are impressed by the assessment made by the District Court that the Goverment had acted with all due speed. Indeed, in an oral colloquy during trial the District Judge commented:</p>
<blockquote id="b626-6">“I have been anxious to see in this case whether there has been a lot of dilitory <em>[sic] </em>conduct that the government has really not done what it should do in order to push this thing with all reasonable speed, and, frankly, I don’t see any point in which the government has been lax.</blockquote>
<blockquote id="b626-7"><em>“If </em>I had found such, and I found it an unreasonable length of time, I would have been happy to so hold ....</blockquote>
<blockquote id="b626-8">“But, in view of the evidence here, I just cannot see any way in which this Court can say that the government has not pursued their claim in all reasonable diligence.” App. 77.</blockquote>
<p id="b626-9">In sum, the Government’s diligent pursuit of pending administrative and criminal proceedings indicates strongly that the reasons for its delay in filing a civil forfeiture proceeding were substantial.</p>
<p id="b626-10">The third element to be considered in the due process balance is the claimant’s assertion of the right to a judicial hear<page-number citation-index="1" label="569">*569</page-number>ing. A claimant is able to trigger rapid filing of a forfeiture action if he desires it. First, the claimant can file an equitable action seeking an order compelling the filing of the forfeiture action or return of the seized property. See <em>Slocum, </em>v. <em>Mayberry, </em><span class="citation" data-id="85171"><a href="/opinion/85171/slocum-v-mayberry/#10" aria-description="Citation for case: Slocum v. Mayberry">2 Wheat. 1, 10</a></span> (1817) (Marshall, C. J.). Less formally, the claimant could simply request that the Customs Service refer the matter to the United States Attorney. If the claimant believes the initial seizure was improper, he could file a motion under Federal Rule of Criminal Procedure 41(e) for a return of the seized property. Yasquez did none of these things and only occasionally inquired about the result of the petition for mitigation or remission and asked that the Secretary reach a decision promptly. The failure to use these remedies can be taken as some indication that Yasquez did not desire an early judicial hearing.</p>
<p id="b627-5">The final element is whether the claimant has been prejudiced by the delay. The primary inquiry here is whether the delay has hampered the claimant in presenting a defense on the merits, through, for example, the loss of witnesses or other important evidence. Such prejudice could be a weighty factor indicating that the delay was unreasonable. Here, Vasquez has never alleged or shown that the delay affected her ability to defend against the impropriety of the forfeiture on the merits. On the contrary, Vasquez conceded that the elements necessary for a forfeiture under § 1102(a) were present in her case.</p>
<p id="b627-6">IV</p>
<p id="b627-7">In this case, the balance of factors indicates that the Government’s delay in instituting civil forfeiture proceedings was reasonable. Although the 18-month delay was a substantial period of time, it was justified by the Government’s diligent efforts in processing the petition for mitigation or remission and in pursuing related criminal proceedings. Vasquez never indicated that she desired early commencement of a civil forfeiture proceeding, and she has not asserted or shown <page-number citation-index="1" label="570">*570</page-number>that the delay prejudiced her ability to defend against the forfeiture. Therefore, the claimant was not denied due process of law. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b628-5">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="AK4"> In addition to the general remission provisions of Title IV, Title II of the Bank Secrecy Act contains its own remission provision, <span class="citation no-link">31 U. S. C. § 1104</span>: “The Secretary may in his discretion remit any forfeiture or penalty under this subchapter in whole or in part upon such terms and conditions as he deems reasonable and just.”</p>
</footnote>
<footnote label="2">
<p id="AGqz"> At the time of the seizure in this case, a customs officer could institute nonjudicial, summary forfeiture proceedings if the value of the seized merchandise was not more than $2,500. See <span class="citation no-link">19 U. S. C. §§ 1607-1609</span>. Congress has since raised this limit to $10,000. <span class="citation no-link">19 U. S. C. § 1607</span> (1976 ed., Supp. V). Even for a seizure of property appraised at less than $10,000, the claimant has a right to a judicial determination upon posting a $250 bond to cover costs. <span class="citation no-link">19 U. S. C. § 1608</span>.</p>
</footnote>
<footnote label="3">
<p id="b616-8"> At the time of the seizure of the currency from Vasquez, <span class="citation no-link">19 U. S. C. § 1603</span> contained no requirement of a prompt report of a seizure by the Customs Service to the United States Attorney for purposes of instituting forfeiture proceedings. As amended in 1978, § 1603 now requires the appropriate customs officer “to report promptly” to the United States Attorney whenever legal proceedings “in connection with such seizure or discovery are required.” <span class="citation no-link">19 U. S. C. § 1603</span> (1976 ed., Supp. V).</p>
</footnote>
<footnote label="4">
<p id="b617-7"> On September 11, 1975, the day after the seizure, Vasquez’ counsel had written an informal letter to the District Director of Customs, explaining why she had not declared the money.</p>
</footnote>
<footnote label="5">
<p id="b617-9"> This inquiry was relevant to the reporting violation. A currency reporting violation is normally a misdemeanor, but a reporting violation committed in furtherance of any other federal offense is a felony. Compare <span class="citation no-link">31 U. S. C. § 1058</span> with <span class="citation no-link">31 U. S. C. § 1059</span>.</p>
</footnote>
<footnote label="6">
<p id="b618-8"> The conviction on the felony count was subsequently reversed because court files were left in the jury room during deliberations. <em>United States </em>v. <em>Vasquez, </em><span class="citation" data-id="365698"><a href="/opinion/365698/united-states-v-mary-josephine-vasquez/" aria-description="Citation for case: United States v. Mary Josephine Vasquez">597 F. 2d 192</a></span> (CA9 1979).</p>
</footnote>
<footnote label="7">
<p id="b618-9"> On March 28, 1977, the Customs Service officially notified Vasquez that her petition had been denied.</p>
</footnote>
<footnote label="8">
<p id="b619-6"> Because we find no violation of due process, we do not decide whether dismissal of the forfeiture action with prejudice would be an appropriate remedy for undue delay.</p>
</footnote>
<footnote label="9">
<p id="b619-7"><em> E. g., White </em>v. <em>Acree, </em><span class="citation" data-id="364740"><a href="/opinion/364740/lincoln-c-white-john-b-ford-intervenor-appellee-v-vernon-d-acree/" aria-description="Citation for case: Lincoln C. White, John B. Ford, Intervenor-Appellee v....">594 F. 2d 1385</a></span> (CA10 1979).</p>
</footnote>
<footnote label="10">
<p id="b619-8"> <em>E. g., United States </em>v. <em>Thirty-Six Thousand One Hundred &amp; Twenty-Five Dollars in U. S. Currency, </em><span class="citation multiple-matches"><a href="/c/F.%202d/642/1211/">642 F. 2d 1211</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/835/">454 U. S. 835</a></span> (1981) (aff’g <span class="citation" data-id="1980791"><a href="/opinion/1980791/united-states-v-thirty-six-thousand-one-hundred-twenty-five-dollars/" aria-description="Citation for case: United States v. Thirty-Six Thousand, One Hundred &amp;...">510 F. Supp. 303</a></span> (ED La. 1980)).</p>
</footnote>
<footnote label="11">
<p id="b619-9"><em> E. g., United States </em>v. <em>Various Pieces of Semiconductor Manufacturing Equipment, </em><span class="citation" data-id="390531"><a href="/opinion/390531/united-states-v-various-pieces-of-semiconductor-manufacturing-equipment/" aria-description="Citation for case: United States v. Various Pieces of Semiconductor...">649 F. 2d 606</a></span> (CA8 1981); <em>United States </em>v. <em>One 1976 Mercedes 450 SLC, </em><span class="citation" data-id="8914520"><a href="/opinion/8925059/united-states-v-one-1976-mercedes-450-slc/" aria-description="Citation for case: United States v. One 1976 Mercedes 450 SLC">667 F. 2d 1171</a></span> (CA5 1982).</p>
</footnote>
<footnote label="12">
<p id="b620-4"> The general rule, of course, is that absent an “extraordinary situation” a party cannot invoke the power of the state to seize a person’s property without a <em>prior </em>judicial determination that the seizure is justified. <em>Boddie </em>v. <em>Connecticut, </em><span class="citation" data-id="9424471"><a href="/opinion/108281/boddie-v-connecticut/#378" aria-description="Citation for case: Boddie v. Connecticut">401 U. S. 371, 378-379</a></span> (1971). See also <em>North Georgia Finishing, Inc. </em>v. <em>Di-Chem, Inc., </em><span class="citation" data-id="9425911"><a href="/opinion/109137/north-georgia-finishing-inc-v-di-chem-inc/" aria-description="Citation for case: North Georgia Finishing, Inc. v. Di-Chem, Inc.">419 U. S. 601</a></span> (1975); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <em>Sniadach </em>v. <em>Family Finance Corp., </em><span class="citation" data-id="9424067"><a href="/opinion/107960/sniadach-v-family-finance-corp-of-bay-view/" aria-description="Citation for case: Sniadach v. Family Finance Corp. of Bay View">395 U. S. 337</a></span> (1969); cf. <em>Mitchell </em>v. <em>W. T. Grant Co., </em><span class="citation" data-id="9425706"><a href="/opinion/109023/mitchell-v-w-t-grant-co/" aria-description="Citation for case: Mitchell v. W. T. Grant Co.">416 U. S. 600</a></span> (1974). But we have previously held that such an extraordinary situation exists when the government seizes items subject to forfeiture. In <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), the Court upheld a Puerto Rico statute modeled after a federal forfeiture statute, <span class="citation no-link">21 U. S. C. § 881</span>(a), which allowed Puerto Rican authorities to seize, without prior notice or hearing, a yacht suspected of importing marihuana. <em>Pearson Yacht </em>clearly indicates that due process does not require federal customs officials to conduct a hearing before seizing items subject to forfeiture. Such a requirement would make customs processing entirely unworkable. The government interests found decisive in <em>Pearson Yacht </em>are equally present in this situation: the seizure serves important governmental purposes; a pre-seizure notice might frustrate the statutory purpose; and the seizure was made by government officials rather than self-motivated private parties.</p>
</footnote>
<footnote label="13">
<p id="b621-7"> In <em>United States </em>v. <em>Thirty-seven </em>Photographs, <span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363</a></span> (1971), we construed a statute allowing customs officials to seize obscene material as requiring a postseizure filing within 14 days and completion of the hearing in an additional 60 days. That case interpreted the statute so as to avoid possible First Amendment problems of prior restraint. The case did not involve, and thus we had no occasion to address, the time restraints imposed by the Due Process Clause. Even if we'were inclined to interpret the statutes here in such a way as to avoid any due process question, it would be impossible to read into the statutory scheme, as we did in <em>Thirty-seven Photographs, </em>a short statute of limitations, since <span class="citation no-link">19 U. S. C. § 1621</span> (1976 ed., Supp. V) expressly allows the Government to bring a civil forfeiture proceeding within five years.</p>
</footnote>
<footnote label="14">
<p id="b623-8"> The deprivation in <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>— loss of liberty — may well be more grievous than the deprivation of one’s use of property at issue here. Thus, the balance of the interests, which depends so heavily on the context of the particular situation, may differ from a situation involving the right to a speedy trial.</p>
</footnote>
<footnote label="15">
<p id="b624-7"> By regulation, the Secretary is not allowed to process any petition for remission or mitigation while a civil forfeiture proceeding is pending. <span class="citation no-link">19 CFR § 171.2</span>(a) (1982).</p>
</footnote>
<footnote label="16">
<p id="b624-8"> Under the 1978 revisions to <span class="citation no-link">19 CFR § 162.31</span>(a), the Customs Service is now required to warn claimants that unless they agree to defer judicial forfeiture proceedings until completion of the administrative process, the case <page-number citation-index="1" label="567">*567</page-number>will be referred promptly to the United States Attorney for institution of judicial proceedings, or summary forfeiture proceedings will be begun.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Agurs.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Agurs"
type: case
citation: "427 U.S. 97 (1976)"
parallel_cite: "96 S. Ct. 2392; 49 L. Ed. 2d 342"
neutral_cite: 1976 U.S. LEXIS 72
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-06-24
docket: 75-491
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1976-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Agurs
  varies_by_point: true
  scope_note: "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
  point_overrides:
    - point: legacy-limited-united-states-v-agurs
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: United States v. Bagley
          cluster_id: 111514
          cite: 473 U.S. 667
          field_ii: limited
      scope_note: "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109506/united-states-v-agurs/"
  cluster_id: 109506
  opinion_id: 109506
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]", "[[Giglio v. United States]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "brady", "giglio", "materiality", "disclosure", "no-request", "due-process"]
holding: "The prosecution's duty to disclose exculpatory evidence exists even when the defense makes no request, but a nondisclosure is a constitutional violation only when the omission is material — defined (in the no-request situation) as evidence that creates a reasonable doubt that did not otherwise exist. (Materiality standard later unified under Bagley's 'reasonable probability' test.)"
lake:
  record_id: United States v. Agurs
  status: verified
  projected_at: 2026-07-09
---

# United States v. Agurs

*427 U.S. 97 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Linda Agurs was convicted of second-degree murder for stabbing James Sewell during an altercation in a hotel room; her defense was self-defense. After trial, defense counsel learned that Sewell had a prior criminal record — including convictions for assault and carrying a deadly weapon — which the prosecutor had not disclosed and which counsel argued would have supported the self-defense theory. The defense had made no specific pretrial request for the victim's record. The Court of Appeals ordered a new trial; the Government sought review.

## Issue
Whether, and under what standard of materiality, the prosecution's failure to disclose [[Brady and Giglio|exculpatory]] evidence violates due process when the defense made no request (or only a general request) for it.

## Rule
The duty to disclose can arise without a request, but only material omissions are constitutional error — **a standard later limited by** [[United States v. Bagley]]. The Court rejected any rule that the prosecutor must disclose anything that "might" affect the verdict: "the prosecutor will not have violated his constitutional duty of disclosure unless his omission is of sufficient significance to result in the denial of the defendant's right to a fair trial." — 427 U.S. at 108. ^pin-108

For the no-request situation, the Court fixed materiality to the justice of the verdict: "if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record." — [427 U.S. at 112](https://www.courtlistener.com/opinion/109506/united-states-v-agurs/#:~:text=if%20the%20omitted%20evidence%20creates%20a%20reasonable%20doubt%20that%20did%20not%20otherwise%20exist%2C). ^pin-112

## Application
Measured against that standard, the prosecutor's failure to disclose Sewell's prior assault-and-weapons record was not a constitutional violation. The record of the victim's violent character, viewed against the entire trial record — Agurs had inflicted multiple stab wounds while suffering none herself, undercutting self-defense — did not create a reasonable doubt about guilt that did not otherwise exist. Because the undisclosed evidence was not material in that sense, the prosecutor's nondisclosure (absent any request) did not deny Agurs a fair trial, and a new trial was not warranted.

## Conclusion
Reversed. The undisclosed evidence did not create a reasonable doubt that did not otherwise exist, so the nondisclosure was not a due-process violation; the prosecutor's duty to volunteer obviously [[Brady and Giglio|exculpatory]] evidence is bounded by materiality.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS** (Stevens, J.; Marshall, J., joined by Brennan, J., dissenting).
- **Materiality standard superseded by** [[United States v. Bagley]] (1985): Agurs had set different materiality tests for its three situations (knowing use of perjury; specific request; no/general request); *[[United States v. Bagley|Bagley]]* adopted a single "reasonable probability" standard for all undisclosed *[[Brady v. Maryland|Brady]]*/*[[Giglio v. United States|Giglio]]* evidence, absorbing Agurs's no-request "reasonable doubt that did not otherwise exist" formula. The **surviving** holding — that the disclosure duty attaches to obviously [[Brady and Giglio|exculpatory]] evidence even without a request — remains good law and is built into [[Brady v. Maryland]]/[[Kyles v. Whitley]] doctrine. Agurs's situation 1 traces to the knowing-perjury line of [[Mooney v. Holohan]] and [[Giglio v. United States]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Agurs*, 427 U.S. 97 (1976) — https://www.courtlistener.com/opinion/109506/united-states-v-agurs/ — pinpoints: 108, 112.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "84bab3d156b9e980", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Agurs"}, "payload": {"all": [{"cite": "427 U.S. 97", "page": "97", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "427"}, {"cite": "96 S. Ct. 2392", "page": "2392", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 342", "page": "342", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 72", "page": "72", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "427 U.S. 97", "official": {"cite": "427 U.S. 97", "page": "97", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "427"}, "official_selection_present": true, "record_id": "United States v. Agurs"}}
{"assertion_id": "98e168317d8f568f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-112", "record_id": "United States v. Agurs"}, "payload": {"fragment": "#:~:text=if%20the%20omitted%20evidence%20creates%20a%20reasonable%20doubt%20that%20did%20not%20otherwise%20exist%2C", "page": null, "pin_id": "pin-112", "pinpoint_status": "star-verified", "quote": "if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record.", "quote_fidelity": "matched", "record_id": "United States v. Agurs", "star_marker": "112"}}
{"assertion_id": "fabaedc07c8f6314", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-108", "record_id": "United States v. Agurs"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-108", "pinpoint_status": "slip-only", "quote": "--- # United States v. Agurs *427 U.S. 97 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Linda Agurs was convicted of second-degree murder for stabbing James Sewell during an altercation in a hotel room; her defense was self-defense. After trial, defense counsel learned that Sewell had a prior criminal record — including convictions for assault and carrying a deadly weapon — which the prosecutor had not disclosed and which counsel argued would have supported the self-defense theory. The defense had made no specific pretrial request for the victim's record. The Court of Appeals ordered a new trial; the Government sought review. ## Issue Whether, and under what standard of materiality, the prosecution's failure to disclose exculpatory evidence violates due process when the defense made no request (or only a general request) for it. ## Rule The duty to disclose can arise without a request, but only material omissions are constitutional error — **a standard later limited by** [[United States v. Bagley]]. The Court rejected any rule that the prosecutor must disclose anything that", "quote_fidelity": "mismatch", "record_id": "United States v. Agurs", "star_marker": null}}
{"assertion_id": "3aab2c1c48a76740", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Agurs"}, "payload": {"as_of_content": "1976-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "United States v. Agurs", "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework.", "varies_by_point": true}}
```

### lake record — United States v. Agurs

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Agurs",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Agurs",
    "case_name_short": "Agurs",
    "case_name_full": "United States v. Agurs",
    "input_case_name": "United States v. Agurs",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-06-24",
    "year": 1976,
    "docket": "75-491",
    "cluster_id": 109506,
    "lead_opinion_id": 109506,
    "sibling_ids": [
      109506,
      9426498,
      9426499
    ],
    "absolute_url": "/opinion/109506/united-states-v-agurs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "427 U.S. 97",
      "volume": "427",
      "reporter": "U.S.",
      "page": "97",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 2392",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2392",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 342",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 72",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "72",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "427 U.S. 97",
        "volume": "427",
        "reporter": "U.S.",
        "page": "97",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 2392",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "2392",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 342",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 72",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "72",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "427 U.S. 97",
    "official_selection": {
      "court_class": "scotus",
      "selected": "427 U.S. 97",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-108",
      "page": null,
      "quote": "--- # United States v. Agurs *427 U.S. 97 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Linda Agurs was convicted of second-degree murder for stabbing James Sewell during an altercation in a hotel room; her defense was self-defense. After trial, defense counsel learned that Sewell had a prior criminal record \u2014 including convictions for assault and carrying a deadly weapon \u2014 which the prosecutor had not disclosed and which counsel argued would have supported the self-defense theory. The defense had made no specific pretrial request for the victim's record. The Court of Appeals ordered a new trial; the Government sought review. ## Issue Whether, and under what standard of materiality, the prosecution's failure to disclose exculpatory evidence violates due process when the defense made no request (or only a general request) for it. ## Rule The duty to disclose can arise without a request, but only material omissions are constitutional error \u2014 **a standard later limited by** [[United States v. Bagley]]. The Court rejected any rule that the prosecutor must disclose anything that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-112",
      "page": null,
      "quote": "if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record.",
      "star_marker": "112",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23248,
      "fragment": "#:~:text=if%20the%20omitted%20evidence%20creates%20a%20reasonable%20doubt%20that%20did%20not%20otherwise%20exist%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1976-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Agurs",
    "varies_by_point": true,
    "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework.",
    "point_overrides": [
      {
        "point": "legacy-limited-united-states-v-agurs",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "United States v. Bagley",
            "cluster_id": 111514,
            "cite": "473 U.S. 667",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Core duty survives: obviously exculpatory evidence must be disclosed even absent a defense request. But Agurs's distinct 'reasonable doubt that did not otherwise exist' materiality formula for the no-request situation was superseded by the single 'reasonable probability' standard of United States v. Bagley (1985), which collapsed Agurs's three-situation framework."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": "473 U.S. 667",
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
          "name": "State of Louisiana v. Brhian Thomas",
          "cluster_id": 10618702,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bateman",
          "cluster_id": 9413757,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Caldwell",
          "cluster_id": 4881045,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Strickland v. Washington",
          "cluster_id": 111170,
          "cite": [
            "80 L. Ed. 2d 674",
            "104 S. Ct. 2052",
            "466 U.S. 668",
            "1984 U.S. LEXIS 79"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cronic",
          "cluster_id": 111169,
          "cite": [
            "80 L. Ed. 2d 657",
            "104 S. Ct. 2039",
            "466 U.S. 648",
            "1984 U.S. LEXIS 78",
            "52 U.S.L.W. 4560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
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
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Briscoe v. LaHue",
          "cluster_id": 110885,
          "cite": [
            "75 L. Ed. 2d 96",
            "103 S. Ct. 1108",
            "460 U.S. 325",
            "1983 U.S. LEXIS 146",
            "51 U.S.L.W. 4247"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Valenzuela-Bernal",
          "cluster_id": 110797,
          "cite": [
            "73 L. Ed. 2d 1193",
            "102 S. Ct. 3440",
            "458 U.S. 858",
            "1982 U.S. LEXIS 159",
            "50 U.S.L.W. 5108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Greer v. Miller",
          "cluster_id": 111956,
          "cite": [
            "97 L. Ed. 2d 618",
            "107 S. Ct. 3102",
            "483 U.S. 756",
            "1987 U.S. LEXIS 2930"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruiz",
          "cluster_id": 121166,
          "cite": [
            "153 L. Ed. 2d 586",
            "122 S. Ct. 2450",
            "536 U.S. 622",
            "2002 U.S. LEXIS 4650"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cole",
          "cluster_id": 2590164,
          "cite": [
            "95 P.3d 811",
            "17 Cal. Rptr. 3d 532",
            "33 Cal. 4th 1158",
            "2004 Cal. Daily Op. Serv. 7469",
            "2004 Daily Journal DAR 10101",
            "2004 Cal. LEXIS 7573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mabry v. Johnson",
          "cluster_id": 111208,
          "cite": [
            "81 L. Ed. 2d 437",
            "104 S. Ct. 2543",
            "467 U.S. 504",
            "1984 U.S. LEXIS 105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Whiteside",
          "cluster_id": 111603,
          "cite": [
            "89 L. Ed. 2d 123",
            "106 S. Ct. 988",
            "475 U.S. 157",
            "1986 U.S. LEXIS 8",
            "54 U.S.L.W. 4194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Agurs:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109506 OR 9426498 OR 9426499) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjEwMDY0MDAwMDAwJnM9NDg0NjM4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109506+OR+9426498+OR+9426499%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109506 OR 9426498 OR 9426499)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDQmcz0xNjk5OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109506+OR+9426498+OR+9426499%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109506 OR 9426498 OR 9426499)",
        "reviewed": 119,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 119,
        "triage_read": 2,
        "triage_snippet_classified": 117
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109506 OR 9426498 OR 9426499)",
    "indexed_citing_opinions": 4292,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109506,
        "count": 3847,
        "count_source": "search"
      },
      {
        "opinion_id": 9426498,
        "count": 518,
        "count_source": "search"
      },
      {
        "opinion_id": 9426499,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6542,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-agurs.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTA5NDUmcz0xMDYxNTM4MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109506+OR+9426498+OR+9426499%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109506,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 104321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 104681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 107354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 107361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 109024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 253599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 276039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 277986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 279213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 279966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 285114,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 285177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 290286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 295841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 305106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 307051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 307845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 313335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 316285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 316953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 317641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 320391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 325310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 325594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 330049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 330694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 1361490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109506,
        "cited_id": 1474384,
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
    "date_created": "2026-07-05T22:00:04Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:00:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Agurs

```
<div>
<center><b><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U.S. 97</a></span> (1976)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
AGURS.</h1></center>
<center>No. 75-491.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 28, 1976.</center>
<center>Decided June 24, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*98</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Bork, Assistant Attorney General Thornburgh, John F. Cooney, Jerome M. Feit,</i> and <i>Robert H. Plaxico.</i></p>
<p><i>Edwin J. Bradley</i> argued the cause for respondent. With him on the brief were <i>Michael E. Geltner, William Greenhalgh,</i> and <i>Sherman L. Cohn.</i></p>
<p>MR. JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>After a brief interlude in an inexpensive motel room, respondent repeatedly stabbed James Sewell, causing his death. She was convicted of second-degree murder. The question before us is whether the prosecutor's failure <span class="star-pagination">*99</span> to provide defense counsel with certain background information about Sewell, which would have tended to support the argument that respondent acted in self-defense, deprived her of a fair trial under the rule of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span>.</p>
<p>The answer to the question depends on (1) a review of the facts, (2) the significance of the failure of defense counsel to request the material, and (3) the standard by which the prosecution's failure to volunteer exculpatory material should be judged.</p>
<p></p>
<h2>I</h2>
<p>At about 4:30 p. m. on September 24, 1971, respondent, who had been there before, and Sewell, registered in a motel as man and wife. They were assigned a room without a bath. Sewell was wearing a bowie knife in a sheath, and carried another knife in his pocket. Less than two hours earlier, according to the testimony of his estranged wife, he had had $360 in cash on his person.</p>
<p>About 15 minutes later three motel employees heard respondent screaming for help. A forced entry into their room disclosed Sewell on top of respondent struggling for possession of the bowie knife. She was holding the knife; his bleeding hand grasped the blade; according to one witness he was trying to jam the blade into her chest. The employees separated the two and summoned the authorities. Respondent departed without comment before they arrived. Sewell was dead on arrival at the hospital.</p>
<p>Circumstantial evidence indicated that the parties had completed an act of intercourse, that Sewell had then gone to the bathroom down the hall, and that the struggle occurred upon his return. The contents of his pockets were in disarray on the dresser and no money was found; the jury may have inferred that respondent took Sewell's money and that the fight started when Sewell re-entered the room and saw what she was doing.</p>
<p><span class="star-pagination">*100</span> On the following morning respondent surrendered to the police. She was given a physical examination which revealed no cuts or bruises of any kind, except needle marks on her upper arm. An autopsy of Sewell disclosed that he had several deep stab wounds in his chest and abdomen, and a number of slashes on his arms and hands, characterized by the pathologist as "defensive wounds."<sup>[1]</sup></p>
<p>Respondent offered no evidence. Her sole defense was the argument made by her attorney that Sewell had initially attacked her with the knife, and that her actions had all been directed toward saving her own life. The support for this self-defense theory was based on the fact that she had screamed for help. Sewell was on top of her when help arrived, and his possession of two knives indicated that he was a violence-prone person.<sup>[2]</sup> It took the jury about 25 minutes to elect a foreman and return a verdict.</p>
<p>Three months later defense counsel filed a motion for a new trial asserting that he had discovered (1) that Sewell had a prior criminal record that would have further evidenced his violent character; (2) that the prosecutor had failed to disclose this information to the defense; and (3) that a recent opinion of the United States Court of Appeals for the District of Columbia Circuit made it clear that such evidence was admissible even if not known to the defendant.<sup>[3]</sup> Sewell's prior record included a plea of guilty to a charge of assault and carrying <span class="star-pagination">*101</span> a deadly weapon in 1963, and another guilty plea to a charge of carrying a deadly weapon in 1971. Apparently both weapons were knives.</p>
<p>The Government opposed the motion, arguing that there was no duty to tender Sewell's prior record to the defense in the absence of an appropriate request; that the evidence was readily discoverable in advance of trial and hence was not the kind of "newly discovered" evidence justifying a new trial; and that, in all events, it was not material.</p>
<p>The District Court denied the motion. It rejected the Government's argument that there was no duty to disclose material evidence unless requested to do so,<sup>[4]</sup><span class="star-pagination">*102</span> assumed that the evidence was admissible, but held that it was not sufficiently material. The District Court expressed the opinion that the prior conviction shed no light on Sewell's character that was not already apparent from the uncontradicted evidence, particularly the fact that he carried two knives; the court stressed the inconsistency between the claim of self-defense and the fact that Sewell had been stabbed repeatedly while respondent was unscathed.</p>
<p>The Court of Appeals reversed.<sup>[5]</sup> The court found no lack of diligence on the part of the defense and no misconduct by the prosecutor in this case. It held, however, that the evidence was material, and that its nondisclosure required a new trial because the jury might have returned a different verdict if the evidence had been received.<sup>[6]</sup></p>
<p>The decision of the Court of Appeals represents a significant departure from this Court's prior holding; because we believe that that court has incorrectly interpreted the constitutional requirement of due process, we reverse.</p>
<p></p>
<h2>
<span class="star-pagination">*103</span> II</h2>
<p>The rule of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span>, arguably applies in three quite different situations. Each involves the discovery, after trial, of information which had been known to the prosecution but unknown to the defense.</p>
<p>In the first situation, typified by <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>, the undisclosed evidence demonstrates that the prosecution's case includes perjured testimony and that the prosecution knew, or should have known, of the perjury.<sup>[7]</sup> In a series of subsequent cases, the Court has consistently held that a conviction obtained by the knowing use of perjured testimony is fundamentally unfair,<sup>[8]</sup> and must be set aside if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury.<sup>[9]</sup> It is this line of cases on which the <span class="star-pagination">*104</span> Court of Appeals placed primary reliance. In those cases the Court has applied a strict standard of materiality, not just because they involve prosecutorial misconduct, but more importantly because they involve a corruption of the truth-seeking function of the trial process. Since this case involves no misconduct, and since there is no reason to question the veracity of any of the prosecution witnesses, the test of materiality followed in the <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> line of cases is not necessarily applicable to this case.</p>
<p>The second situation, illustrated by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> case itself, is characterized by a pretrial request for specific evidence. In that case defense counsel had requested the extrajudicial statements made by Brady's accomplice, one Boblit. This Court held that the suppression of one of Boblit's statements deprived Brady of due process, noting specifically that the statement had been requested and that it was "material."<sup>[10]</sup> A fair analysis of the holding in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> indicates that implicit in the requirement of materiality is a concern that the suppressed evidence might have affected the outcome of the trial.</p>
<p>Brady was found guilty of murder in the first degree. Since the jury did not add the words "without capital punishment" to the verdict, he was sentenced to death. At his trial Brady did not deny his involvement in the deliberate killing, but testified that it was his accomplice, <span class="star-pagination">*105</span> Boblit, rather than he, who had actually strangled the decedent. This version of the event was corroborated by one of several confessions made by Boblit but not given to Brady's counsel despite an admittedly adequate request.</p>
<p>After his conviction and sentence had been affirmed on appeal,<sup>[11]</sup> Brady filed a motion to set aside the judgment, and later a post-conviction proceeding, in which he alleged that the State had violated his constitutional rights by suppressing the Boblit confession. The trial judge denied relief largely because he felt that Boblit's confession would have been inadmissible at Brady's trial. The Maryland Court of Appeals disagreed;<sup>[12]</sup> it ordered a new trial on the issue of punishment. It held that the withholding of material evidence, even "without guile," was a denial of due process and that there were valid theories on which the confession might have been admissible in Brady's defense.</p>
<p>This Court granted certiorari to consider Brady's contention that the violation of his constitutional right to a fair trial vitiated the entire proceeding.<sup>[13]</sup> The holding that the suppression of exculpatory evidence violated Brady's right to due process was affirmed, as was the separate holding that he should receive a new trial on the issue of punishment but not on the issue of guilt or innocence. The Court interpreted the Maryland Court <span class="star-pagination">*106</span> of Appeals opinion as ruling that the confession was inadmissible on that issue. For that reason, the confession could not have affected the outcome on the issue of guilt but could have affected Brady's punishment. It was material on the latter issue but not the former. And since it was not material on the issue of guilt, the entire trial was not lacking in due process.</p>
<p>The test of materiality in a case like <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> in which specific information has been requested by the defense is not necessarily the same as in a case in which no such request has been made.<sup>[14]</sup> Indeed, this Court has not yet decided whether the prosecutor has any obligation to provide defense counsel with exculpatory information when no request has been made. Before addressing that question, a brief comment on the function of the request is appropriate.</p>
<p>In <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> the request was specific. It gave the prosecutor notice of exactly what the defense desired. Although there is, of course, no duty to provide defense counsel with unlimited discovery of everything known by the prosecutor, if the subject matter of such a request is material, or indeed if a substantial basis for claiming materiality exists, it is reasonable to require the prosecutor to respond either by furnishing the information or by submitting the problem to the trial judge. When the prosecutor receives a specific and relevant request, the failure to make any response is seldom, if ever, excusable.</p>
<p>In many cases, however, exculpatory information in the possession of the prosecutor may be unknown to defense counsel. In such a situation he may make no request at all, or possibly ask for "all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material" or for "anything exculpatory." Such a request really gives the prosecutor no better notice than if no request is <span class="star-pagination">*107</span> made. If there is a duty to respond to a general request of that kind, it must derive from the obviously exculpatory character of certain evidence in the hands of the prosecutor. But if the evidence is so clearly supportive of a claim of innocence that it gives the prosecution notice of a duty to produce, that duty should equally arise even if no request is made. Whether we focus on the desirability of a precise definition of the prosecutor's duty or on the potential harm to the defendant, we conclude that there is no significant difference between cases in which there has been merely a general request for exculpatory matter and cases, like the one we must now decide, in which there has been no request at all. The third situation in which the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule arguably applies, typified by this case, therefore embraces the case in which only a general request for "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> material" has been made.</p>
<p>We now consider whether the prosecutor has any constitutional duty to volunteer exculpatory matter to the defense, and if so, what standard of materiality gives rise to that duty.</p>
<p></p>
<h2>III</h2>
<p>We are not considering the scope of discovery authorized by the Federal Rules of Criminal Procedure, or the wisdom of amending those Rules to enlarge the defendant's discovery rights. We are dealing with the defendant's right to a fair trial mandated by the Due Process Clause of the Fifth Amendment to the Constitution. Our construction of that Clause will apply equally to the comparable clause in the Fourteenth Amendment applicable to trials in state courts.</p>
<p>The problem arises in two principal contexts. First, in advance of trial, and perhaps during the course of a trial as well, the prosecutor must decide what, if anything, he should voluntarily submit to defense counsel. <span class="star-pagination">*108</span> Second, after trial a judge may be required to decide whether a nondisclosure deprived the defendant of his right to due process. Logically the same standard must apply at both times. For unless the omission deprived the defendant of a fair trial, there was no constitutional violation requiring that the verdict be set aside; and absent a constitutional violation, there was no breach of the prosecutor's constitutional duty to disclose.</p>
<p>Nevertheless, there is a significant practical difference between the pretrial decision of the prosecutor and the post-trial decision of the judge. Because we are dealing with an inevitably imprecise standard, and because the significance of an item of evidence can seldom be predicted accurately until the entire record is complete, the prudent prosecutor will resolve doubtful questions in favor of disclosure. But to reiterate a critical point, the prosecutor will not have violated his constitutional duty of disclosure unless his omission is of sufficient significance to result in the denial of the defendant's right to a fair trial.</p>
<p>The Court of Appeals appears to have assumed that the prosecutor has a constitutional obligation to disclose any information that might affect the jury's verdict. That statement of a constitutional standard of materiality approaches the "sporting theory of justice" which the Court expressly rejected in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[15]</sup> For a jury's <span class="star-pagination">*109</span> appraisal of a case "might" be affected by an improper or trivial consideration as well as by evidence giving rise to a legitimate doubt on the issue of guilt. If everything that might influence a jury must be disclosed, the only way a prosecutor could discharge his constitutional duty would be to allow complete discovery of his files as a matter of routine practice.</p>
<p>Whether or not procedural rules authorizing such broad discovery might be desirable, the Constitution surely does not demand that much. While expressing the opinion that representatives of the State may not "suppress substantial material evidence," former Chief Justice Traynor of the California Supreme Court has pointed out that "they are under no duty to report sua sponte to the defendant all that they learn about the case and about their witnesses." <i>In re Imbler,</i> <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#569" aria-description="Citation for case: In Re Imbler">60 Cal. 2d 554, 569</a></span>, <span class="citation" data-id="1361490"><a href="/opinion/1361490/in-re-imbler/#14" aria-description="Citation for case: In Re Imbler">387 P. 2d 6, 14</a></span> (1963). And this Court recently noted that there is "no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case." <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span>.<sup>[16]</sup> The mere possibility that an item of undisclosed information <span class="star-pagination">*110</span> might have helped the defense, or might have affected the outcome of the trial, does not establish "materiality" in the constitutional sense.</p>
<p>Nor do we believe the constitutional obligation is measured by the moral culpability, or the willfulness, of the prosecutor.<sup>[17]</sup> If evidence highly probative of innocence is in his file, he should be presumed to recognize its significance even if he has actually overlooked it. Cf. <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span>. Conversely, if evidence actually has no probative significance at all, no purpose would be served by requiring a new trial simply because an inept prosecutor incorrectly believed he was suppressing a fact that would be vital to the defense. If the suppression of evidence results in constitutional error, it is because of the character of the evidence, not the character of the prosecutor.</p>
<p>As the District Court recognized in this case, there are situations in which evidence is obviously of such substantial value to the defense that elementary fairness requires it to be disclosed even without a specific request.<sup>[18]</sup> For though the attorney for the sovereign must prosecute the accused with earnestness and vigor, he <span class="star-pagination">*111</span> must always be faithful to his client's overriding interest that "justice shall be done." He is the "servant of the law, the twofold aim of which is that guilt shall not escape or innocence suffer." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span>. This description of the prosecutor's duty illuminates the standard of materiality that governs his obligation to disclose exculpatory evidence.</p>
<p>On the one hand, the fact that such evidence was available to the prosecutor and not submitted to the defense places it in a different category than if it had simply been discovered from a neutral source after trial. For that reason the defendant should not have to satisfy the severe burden of demonstrating that newly discovered evidence probably would have resulted in acquittal.<sup>[19]</sup> If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State's possession as when it was found in a neutral source, there would be no special significance to the prosecutor's obligation to serve the cause of justice.</p>
<p>On the other hand, since we have rejected the suggestion that the prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel, we cannot consistently treat every nondisclosure as though it were error. It necessarily follows that the judge should not order a new trial every time he is unable to <span class="star-pagination">*112</span> characterize a nondisclosure as harmless under the customary harmless-error standard. Under that standard when error is present in the record, the reviewing judge must set aside the verdict and judgment unless his "conviction is sure that the error did not influence the jury, or had but very slight effect." <i>Kotteakos</i> v. <i>United States,</i> <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#764" aria-description="Citation for case: Kotteakos v. United States">328 U. S. 750, 764</a></span>. Unless every nondisclosure is regarded as automatic error, the constitutional standard of materiality must impose a higher burden on the defendant.</p>
<p>The proper standard of materiality must reflect our overriding concern with the justice of the finding of guilt.<sup>[20]</sup> Such a finding is permissible only if supported by evidence establishing guilt beyond a reasonable doubt. It necessarily follows that if the omitted evidence creates a reasonable doubt that did not otherwise exist, constitutional error has been committed. This means that the omission must be evaluated in the context of the entire record.<sup>[21]</sup> If there is no reasonable doubt about <span class="star-pagination">*113</span> guilt whether or not the additional evidence is considered, there is no justification for a new trial. On the other hand, if the verdict is already of questionable validity, additional evidence of relatively minor importance might be sufficient to create a reasonable doubt.</p>
<p>This statement of the standard of materiality describes the test which courts appear to have applied in actual cases although the standard has been phrased in different language.<sup>[22]</sup> It is also the standard which the trial judge applied in this case. He evaluated the significance of Sewell's prior criminal record in the context of the full trial which he recalled in detail. Stressing in particular the incongruity of a claim that Sewell was the aggressor with the evidence of his multiple wounds and respondent's unscathed condition, the trial judge indicated his unqualified opinion that respondent was guilty. He <span class="star-pagination">*114</span> noted that Sewell's prior record did not contradict any evidence offered by the prosecutor, and was largely cumulative of the evidence that Sewell was wearing a bowie knife in a sheath and carrying a second knife in his pocket when he registered at the motel.</p>
<p>Since the arrest record was not requested and did not even arguably give rise to any inference of perjury, since after considering it in the context of the entire record the trial judge remained convinced of respondent's guilt beyond a reasonable doubt, and since we are satisfied that his firsthand appraisal of the record was thorough and entirely reasonable, we hold that the prosecutor's failure to tender Sewell's record to the defense did not deprive respondent of a fair trial as guaranteed by the Due Process Clause of the Fifth Amendment. Accordingly, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>The Court today holds that the prosecutor's constitutional duty to provide exculpatory evidence to the defense is not limited to cases in which the defense makes a request for such evidence. But once having recognized the existence of a duty to volunteer exculpatory evidence, the Court so narrowly defines the category of "material" evidence embraced by the duty as to deprive it of all meaningful content.</p>
<p>In considering the appropriate standard of materiality governing the prosecutor's obligation to volunteer exculpatory evidence, the Court observes:</p>
<blockquote>"[T]he fact that such evidence was available to the prosecutor and not submitted to the defense places it in a different category than if it had simply been <span class="star-pagination">*115</span> discovered from a neutral source after trial. For that reason the defendant should not have to satisfy the severe burden of demonstrating that newly discovered evidence probably would have resulted in acquittal [the standard generally applied to a motion under Fed. Rule Crim. Proc. 33 based on newly discovered evidence.<sup>[1]</sup>]. If the standard applied to the usual motion for a new trial based on newly discovered evidence were the same when the evidence was in the State's possession as when it was found in a neutral source, there would be no special significance to the prosecutor's obligation to serve the cause of justice." <i>Ante,</i> at 111 (footnote omitted).</blockquote>
<p>I agree completely.</p>
<p>The Court, however, seemingly forgets these precautionary words when it comes time to state the proper standard of materiality to be applied in cases involving neither the knowing use of perjury nor a specific defense request for an item of information. In such cases, the prosecutor commits constitutional error, the Court holds, "if the omitted evidence creates a reasonable doubt that did not otherwise exist." <i>Ante,</i> at 112. As the Court's subsequent discussion makes clear, the defendant challenging the prosecutor's failure to disclose evidence is entitled to relief, in the Court's view, only if the withheld evidence actually creates a reasonable doubt as to guilt in the judge's mind. The burden thus imposed on the defendant is at least as "severe" as, if not more <span class="star-pagination">*116</span> "severe" than,<sup>[2]</sup> the burden he generally faces on a Rule 33 motion. Surely if a judge is able to say that evidence actually creates a reasonable doubt as to guilt in his mind (the Court's standard), he would also conclude that the evidence "probably would have resulted in acquittal" (the general Rule 33 standard). In short, in spite of its own salutary precaution, the Court treats the case in which the prosecutor withholds evidence no differently from the case in which evidence is newly discovered from a neutral source. The "prosecutor's obligation to serve the cause of justice" is reduced to a status, to borrow the Court's words, of "no special significance." <i>Ante,</i> at 111.</p>
<p>Our overriding concern in cases such as the one before us is the defendant's right to a fair trial. One of the most basic elements of fairness in a criminal trial is that available evidence tending to show innocence, as well as that tending to show guilt, be fully aired before the jury; more particularly, it is that the State in its zeal to convict a defendant not suppress evidence that might exonerate him. See <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#810" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 810</a></span> (1972) (opinion of MARSHALL, J.). This fundamental notion of fairness does not pose any irreconcilable conflict for the prosecutor, for as the Court reminds us, the prosecutor "must always be faithful to his client's overriding interest that `justice shall be done.' " <i>Ante,</i> at 111. No interest of the State is served, and no duty of the prosecutor advanced, by the suppression of evidence favorable to the defendant. On the contrary, the prosecutor fulfills his most basic responsibility when he fully airs all the relevant evidence at his command.</p>
<p>I recognize, of course, that the exculpatory value to the defense of an item of information will often not be apparent to the prosecutor in advance of trial. And <span class="star-pagination">*117</span> while the general obligation to disclose exculpatory information no doubt continues during the trial, giving rise to a duty to disclose information whose significance becomes apparent as the case progresses, even a conscientious prosecutor will fail to appreciate the significance of some items of information. See <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#147" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 147</a></span> (CA2 1968). I agree with the Court that these consideration, as well as the general interest in finality of judgments, preclude the granting of a new trial in every case in which the prosecutor has failed to disclose evidence of some value to the defense. But surely these considerations do not require the rigid rule the Court intends to be applied to all but a relatively small number of such cases.</p>
<p>Under today's ruling, if the prosecution has not made knowing use of perjury, and if the defense has not made a specific request for an item of information, the defendant is entitled to a new trial only if the withheld evidence actually creates a reasonable doubt as to guilt in the judge's mind. With all respect, this rule is completely at odds with the overriding interest in assuring that evidence tending to show innocence is brought to the jury's attention. The rule creates little, if any, incentive for the prosecutor conscientiously to determine whether his files contain evidence helpful to the defense. Indeed, the rule reinforces the natural tendency of the prosecutor to overlook evidence favorable to the defense, and creates an incentive for the prosecutor to resolve close questions of disclosure in favor of concealment.</p>
<p>More fundamentally, the Court's rule usurps the function of the jury as the trier of fact in a criminal case. The Court's rule explicitly establishes the judge as the trier of fact with respect to evidence withheld by the prosecution. The defendant's fate is sealed so long as the evidence does not create a reasonable doubt as to guilt in the judge's mind, regardless of whether the <span class="star-pagination">*118</span> evidence is such that reasonable men could disagree as to its importregardless, in other words, of how "close" the case may be.<sup>[3]</sup></p>
<p>The Court asserts that this harsh standard of materiality is the standard that "courts appear to have applied in actual cases although the standard has been phrased in different language." <i>Ante,</i> at 113 (footnote omitted). There is no basis for this assertion. None of the cases cited by the Court in support of its statement suggests that a judgment of conviction should be sustained so long as the judge remains convinced beyond a reasonable doubt of the defendant's guilt.<sup>[4]</sup> The prevailing <span class="star-pagination">*119</span> view in the federal courts of the standard of materiality for cases involving neither a specific request for information nor other indications of deliberate misconducta standard with which the cases cited by the Court are fully consistentis quite different. It is essentially the following: If there is a significant chance that the withheld evidence, developed by skilled counsel, would have induced a reasonable doubt in the minds of enough jurors to avoid a conviction, then the judgment of conviction must be set aside.<sup>[5]</sup> This standard, unlike the Court's reflects a recognition that the determination must be in terms of the impact of an item of evidence on the jury, and that this determination cannot always be made with certainty.<sup>[6]</sup></p>
<p><span class="star-pagination">*120</span> The Court approvesbut only for a limited category of casesa standard virtually identical to the one I have described as reflecting the prevailing view. In cases in which "the undisclosed evidence demonstrates that the prosecution's case includes perjured testimony and that the prosecution knew, or should have known, of the perjury," <i>ante,</i> at 103, the judgment of conviction must be set aside "if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury." <i><span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/" aria-description="Citation for case: United States v. James Vincent Keogh">Ibid.</a></span></i> This lesser burden on the defendant is appropriate, the Court states, primarily because the withholding of evidence contradicting testimony offered by witnesses called by the prosecution "involve[s] a corruption of the truth-seeking function of the trial process." <i>Ante,</i> at 104. But surely the truth-seeking process is corrupted by the withholding of evidence favorable to the defense, regardless of whether the evidence is directly contradictory to evidence offered by the prosecution. An example offered by Mr. Justice Fortas serves to illustrate the point. "[L]et us assume that the State possesses information that blood was found on the victim, and that this blood is of a type which does not match that of the accused or of the victim. Let us assume that no related testimony was offered by the State." <i>Giles</i> v. <i>Maryland,</i> <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#100" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 100</a></span> (1967) (concurring in judgment). The suppression of the information unquestionably corrupts the truth-seeking process, and the burden on the defendant in establishing his entitlement to a new trial ought be no different from the burden he would face if related testimony had been elicited by the prosecution. See <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#99" aria-description="Citation for case: Giles v. Maryland"><i>id.,</i> at 99-101</a></span>.</p>
<p>The Court derives its "reasonable likelihood" standard for cases involving perjury from cases such as <i>Napue</i> v. <span class="star-pagination">*121</span> <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972). But surely the results in those cases, and the standards applied, would have been no different if perjury had not been involved. In <i><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span></i> and <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span>,</i> co-conspirators testifying against the defendants testified falsely, in response to questioning by defense counsel, that they had not received promises from the prosecution. The prosecution failed to disclose that promises had in fact been made. The corruption of the truth-seeking process stemmed from the suppression of evidence affecting the overall credibility of the witnesses, see <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><i>Napue, supra,</i> at 269</a></span>; <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States"><i>Giglio, supra,</i> at 154</a></span>, and that corruption would have been present whether or not defense counsel had elicited statements from the witnesses denying that promises had been made.</p>
<p>It may be that contrary to the Court's insistence, its treatment of perjury cases reflects simply a desire to deter deliberate prosecutorial misconduct. But if that were the case, we might reasonably expect a rule imposing a lower threshold of materiality than the Court imposes perhaps a harmless-error standard. And we would certainly expect the rule to apply to a broader category of misconduct than the failure to disclose evidence that contradicts testimony offered by witnesses called by the prosecution. For the prosecutor is guilty of misconduct when he deliberately suppresses evidence that is clearly relevant and favorable to the defense, regardless, once again, of whether the evidence relates directly to testimony given in the course of the Government's case.</p>
<p>This case, however, does not involve deliberate prosecutorial misconduct. Leaving open the question whether a different rule might appropriately be applied in cases involving deliberate misconduct,<sup>[7]</sup> I would hold that the <span class="star-pagination">*122</span> defendant in this case had the burden of demonstrating that there is a significant chance that the withheld evidence, developed by skilled counsel, would have induced a reasonable doubt in the minds of enough jurors to avoid a conviction. This is essentially the standard applied by the Court of Appeals, and I would affirm its judgment.</p>
<h2>NOTES</h2>
<p>[1]  The alcohol level in Sewell's blood was slightly below the legal definition of intoxication.</p>
<p>[2]  Moreover, the motel clerk testified that Sewell's wife had said he "would use a knife"; however, Mrs. Sewell denied making this statement. There was no dispute about the fact that Sewell carried the bowie knife when he registered.</p>
<p>[3]  See <i>United States</i> v. <i>Burks,</i> 152 U. S. App. D. C. 284, 286, <span class="citation" data-id="9458954"><a href="/opinion/307051/united-states-v-james-h-burks/#434" aria-description="Citation for case: United States v. James H. Burks">470 F. 2d 432, 434</a></span> (1972).</p>
<p>[4]  "THE COURT: What are you saying? How can you request that which you don't know exists. That is the very essence of Brady.
</p>
<p>.....</p>
<p>"THE COURT: Are you arguing to the Court that the status of the law is that if you have a report indicating that fingerprints were taken and that the fingerprints on the item . . . which the defendant is alleged to have assaulted somebody turn out not to be the defendant's, that absent a specific request for that information, you do not have any obligation to defense counsel?</p>
<p>"MR. CLARKE: No, Your Honor. There is another aspect which comes to this, and that is whether or not the Government knowingly puts on perjured testimony. It has an obligation to correct that perjured testimony.</p>
<p>"THE COURT: I am not talking about perjured testimony. You don't do anything about it. You say nothing about it. You have got the report there. You know that possibly it could be exculpatory. Defense counsel doesn't know about it. He has been misinformed about it. Suppose he doesn't know about it. And because he has made no specific request for that information, you say that the status of the law under Brady is that you have no obligation as a prosecutor to open your mouth?</p>
<p>"MR. CLARKE: No. Your Honor . . . .</p>
<p>"But as the materiality of the items becomes less to the point where it is not material, there has to be a request, or else the Government, just like the defense, is not on notice." App. 147-149.</p>
<p>[5]  167 U. S. App. D. C. 28, <span class="citation" data-id="325310"><a href="/opinion/325310/united-states-v-linds-agurs-united-states-of-america-v-linda-v-agurs/" aria-description="Citation for case: United States v. Linds Agurs, United States of America v....">510 F. 2d 1249</a></span> (1975). The opinion of the Court of Appeals disposed of the direct appeal filed after respondent was sentenced as well as the two additional appeals taken from the two orders denying motions for new trial. After the denial of the first motion, respondent's counsel requested leave to withdraw in order to enable substitute counsel to file a new motion for a new trial on the ground that trial counsel's representation had been ineffective because he did not request Sewell's criminal record for the reason that he incorrectly believed that it was inadmissible. The District Court denied that motion. Although that action was challenged on appeal, the Court of Appeals did not find it necessary to pass on the validity of that ground. We think it clear, however, that counsel's failure to obtain Sewell's prior criminal record does not demonstrate ineffectiveness.</p>
<p>[6]  Although a majority of the active judges of the Circuit, as well as one of the members of the panel, expressed doubt about the validity of the panel's decision, the court refused to rehear the case en banc.</p>
<p>[7]  In <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> it was alleged that the petitioner's conviction was based on perjured testimony "which was knowingly used by the prosecuting authorities in order to obtain that conviction, and also that these authorities deliberately suppressed evidence which would have impeached and refuted the testimony thus given against him." <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#110" aria-description="Citation for case: Mooney v. Holohan">294 U. S., at 110</a></span>.
</p>
<p>The Court held that such allegations, if true, would establish such fundamental unfairness as to justify a collateral attack on petitioner's conviction.</p>
<p>"It is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation." <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan"><i>Id.,</i> at 112</a></span>.</p>
<p>[8]  <i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span>; <i>Alcorta</i> v. <i>Texas,</i> <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>; <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span>; <i>Miller</i> v. <i>Pate,</i> <span class="citation" data-id="107354"><a href="/opinion/107354/miller-v-pate/" aria-description="Citation for case: Miller v. Pate">386 U. S. 1</a></span>; <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span>; <i>Donnelly</i> v. <i>DeChristoforo,</i> <span class="citation" data-id="9425708"><a href="/opinion/109024/donnelly-v-dechristoforo/" aria-description="Citation for case: Donnelly v. DeChristoforo">416 U. S. 637</a></span>.</p>
<p>[9]  See <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States"><i>Giglio, supra,</i> at 154</a></span>, quoting from <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><i>Napue, supra,</i> at 271</a></span>.</p>
<p>[10]  "We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. Although in <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Mooney</a></span></i> the Court had been primarily concerned with the willful misbehavior of the prosecutor, in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> the Court focused on the harm to the defendant resulting from nondisclosure. See discussions of this development in Note, The Prosecutor's Constitutional Duty to Reveal Evidence to the Defendant, 74 Yale L. J. 136 (1964); and Comment, <i>Brady</i> v. <i>Maryland</i> and The Prosecutor's Duty to Disclose, <span class="citation no-link">40 U. Chi. L. Rev. 112</span> (1972).</p>
<p>[11]  <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">220 Md. 454</a></span>, <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">154 A. 2d 434</a></span> (1959).</p>
<p>[12]  <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/" aria-description="Citation for case: Brady v. State">226 Md. 422</a></span>, 174 A. 2d. 167 (1961).</p>
<p>[13]  "The petitioner was denied due process of law by the State's suppression of evidence before his trial began. The proceeding must commence again from the stage at which the petitioner was overreached. The denial of due process of law vitiated the verdict and the sentence. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#545" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 545</a></span>. The verdict is not saved because other competent evidence would support it. <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#621" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 621</a></span>." Brief for Petitioner in <i>Brady</i> v. <i>Maryland</i><i>,</i> No. 490, O. T. 1962, p. 6.</p>
<p>[14]  See Comment, 40 U. Chi. L. Rev., <i>supra,</i> n. 10, at 115-117.</p>
<p>[15]  "In the present case a unanimous Court of Appeals has said that nothing in the suppressed confession `could have reduced the appellant Brady's offense below murder in the first degree.' We read that statement as a ruling on the admissibility of the confession on the issue of innocence or guilt. A sporting theory of justice might assume that if the suppressed confession had been used at the first trial, the judge's ruling that it was not admissible on the issue of innocence or guilt might have been flouted by the jury just as might have been done if the court had first admitted a confession and then stricken it from the record. But we cannot raise that trial strategy to the dignity of a constitutional right and say that the deprival of this defendant of that sporting chance through the use of a bifurcated trial (cf. <i>Williams</i> v. <i>New York,</i> <span class="citation" data-id="9420330"><a href="/opinion/104681/williams-v-new-york/" aria-description="Citation for case: Williams v. New York">337 U. S. 241</a></span>) denies him due process or violates the Equal Protection Clause of the Fourteenth Amendment." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#90" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 90-91</a></span> (footnote omitted).</p>
<p>[16]  In his opinion concurring in the judgment in <i>Giles</i> v. <i>Maryland,</i> <span class="citation" data-id="9423353"><a href="/opinion/107361/giles-v-maryland/#98" aria-description="Citation for case: Giles v. Maryland">386 U. S. 66, 98</a></span>, Mr. Justice Fortas stated:
</p>
<p>"This is not to say that convictions ought to be reversed on the ground that information merely repetitious, cumulative, or embellishing of facts otherwise known to the defense or presented to the court, or without importance to the defense for purposes of the preparation of the case or for trial was not disclosed to defense counsel. It is not to say that the State has an obligation to communicate preliminary, challenged, or speculative information."</p>
<p>[17]  In <i>Brady</i> this Court, as had the Maryland Court of Appeals, expressly rejected the good faith or the bad faith of the prosecutor as the controlling consideration: "We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, <i>irrespective of the good faith or bad faith of the prosecution.</i> The principle of <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> is not punishment of society for misdeeds of a prosecutor but avoidance of an unfair trial to the accused." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. (Emphasis added.) If the nature of the prosecutor's conduct is not controlling in a case like <i>Brady,</i> surely it should not be controlling when the prosecutor has not received a specific request for information.</p>
<p>[18]  The hypothetical example given by the District Judge in this case was fingerprint evidence demonstrating that the defendant could not have fired the fatal shot.</p>
<p>[19]  This is the standard generally applied by lower courts in evaluating motions for new trial under Fed. Rule Crim. Proc. 33 based on newly discovered evidence. See, <i>e. g., </i><i>Ashe</i> v. <i>United States,</i> <span class="citation" data-id="253599"><a href="/opinion/253599/neil-w-ashe-v-united-states-of-america-two-cases/#733" aria-description="Citation for case: Neil W. Ashe v. United States of America, (Two Cases)">288 F. 2d 725, 733</a></span> (CA6 1961); <i>United States</i> v. <i>Thompson,</i> <span class="citation" data-id="317641"><a href="/opinion/317641/united-states-v-carl-thompson-united-states-of-america-v-steven-teresi/#310" aria-description="Citation for case: United States v. Carl Thompson, United States of America...">493 F. 2d 305, 310</a></span> (CA9 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/834/">419 U. S. 834</a></span>; <i>United States</i> v. <i>Houle,</i> <span class="citation" data-id="9460174"><a href="/opinion/316285/united-states-v-joseph-g-houle-and-victor-diodato/#171" aria-description="Citation for case: United States v. Joseph G. Houle and Victor Diodato">490 F. 2d 167, 171</a></span> (CA2 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./417/970/">417 U. S. 970</a></span>; <i>United States</i> v. <i>Meyers,</i> <span class="citation" data-id="313335"><a href="/opinion/313335/united-states-v-irving-h-meyers-two-cases/#116" aria-description="Citation for case: United States v. Irving H. Meyers (Two Cases)">484 F. 2d 113, 116</a></span> (CA3 1973); <i>Heald</i> v. <i>United States,</i> <span class="citation" data-id="1474384"><a href="/opinion/1474384/heald-v-united-states/#883" aria-description="Citation for case: Heald v. United States">175 F. 2d 878, 883</a></span> (CA10 1949). See also 2 C. Wright, Federal Practice and Procedure § 557 (1969).</p>
<p>[20]  It has been argued that the standard should focus on the impact of the undisclosed evidence on the defendant's ability to prepare for trial, rather than the materiality of the evidence to the issue of guilt or innocence. See Note, The Prosecutor's Constitutional Duty to Reveal Evidence to the Defense, 74 Yale L. J. 136 (1964). Such a standard would be unacceptable for determining the materiality of what has been generally recognized as "<i>Brady</i> material" for two reasons. First, that standard would necessarily encompass incriminating evidence as well as exculpatory evidence, since knowledge of the prosecutor's entire case would always be useful in planning the defense. Second, such an approach would primarily involve an analysis of the adequacy of the notice given to the defendant by the State, and it has always been the Court's view that the notice component of due process refers to the charge rather than the evidentiary support for the charge.</p>
<p>[21]  "If, for example, one of only two eyewitnesses to a crime had told the prosecutor that the defendant was definitely not its perpetrator and if this statement was not disclosed to the defense, no court would hesitate to reverse a conviction resting on the testimony of the other eyewitness. But if there were fifty eyewitnesses, fortynine of whom identified the defendant, and the prosecutor neglected to reveal that the other, who was without his badly needed glasses on the misty evening of the crime, had said that the criminal looked something like the defendant but he could not be sure as he had only had a brief glimpse, the result might well be different." Comment, 40 U. Chi. L. Rev., <i>supra,</i> n. 10, at 125.</p>
<p>[22]  See, <i>e. g., </i><i>Stout</i> v. <i>Cupp,</i> <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/#882" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden">426 F. 2d 881, 882-883</a></span> (CA9 1970); <i>Peterson</i> v. <i>United States,</i> <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/#1079" aria-description="Citation for case: Gerald D. Peterson v. United States">411 F. 2d 1074, 1079</a></span> (CA8 1969); <i>Lessard</i> v. <i>Dickson,</i> <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#90" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California...">394 F. 2d 88, 90-92</a></span> (CA9 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./393/1004/">393 U. S. 1004</a></span>; <i>United States</i> v. <i>Tomaiolo,</i> <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/#28" aria-description="Citation for case: United States v. Charles Tomaiolo">378 F. 2d 26, 28</a></span> (CA2 1967). One commentator has identified three different standards this way:
</p>
<p>"As discussed previously, in earlier cases the following standards for determining materiality for disclosure purposes were enunciated: (1) evidence which may be merely helpful to the defense; (2) evidence which raised a reasonable doubt as to defendant's guilt; (3) evidence which is of such a character as to create a substantial likelihood of reversal." Comment, Materiality and Defense Requests: Aids in Defining the Prosecutor's Duty of Disclosure, <span class="citation no-link">59 Iowa L. Rev. 433</span>, 445 (1973).</p>
<p>See also Note, The Duty of the Prosecutor to Disclose Exculpatory Evidence, 60 Col. L. Rev. 858 (1960).</p>
<p>[1]  The burden generally imposed upon such a motion has also been described as a burden of demonstrating that the newly discovered evidence would probably produce a different verdict in the event of a retrial. See, <i>e. g., </i><i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d 272, 287</a></span> (CA2 1973); <i>United States</i> v. <i>Rodriguez,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/437/940/">437 F. 2d 940</a></span>, 942 (CA5 1971); <i>United States</i> v. <i>Curran,</i> <span class="citation" data-id="305106"><a href="/opinion/305106/united-states-v-m-prial-curran/#264" aria-description="Citation for case: United States v. M. Prial Curran">465 F. 2d 260, 264</a></span> (CA7 1972).</p>
<p>[2]  See <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#148" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 148</a></span> (CA2 1968), in which Judge Friendly implies that the standard the Court adopts is more severe than the standard the Court rejects.</p>
<p>[3]  To emphasize the harshness of the Court's rule, the defendant's fate is determined finally by the judge only if the judge does not entertain a reasonable doubt as to guilt. If evidence withheld by the prosecution does create a reasonable doubt as to guilt in the judge's mind, that does not end the caserather, the defendant (one might more accurately say the prosecution) is "entitled" to have the case decided by a jury.</p>
<p>[4]  In <i>Stout</i> v. <i>Cupp,</i> <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden">426 F. 2d 881</a></span> (CA9 1970), a habeas proceeding, the court simply quoted the District Court's finding that if the suppressed evidence had been introduced, "the jury would not have reached a different result." <span class="citation" data-id="290286"><a href="/opinion/290286/wayne-l-stout-v-hoyt-c-cupp-warden/#883" aria-description="Citation for case: Wayne L. Stout v. Hoyt C. Cupp, Warden"><i>Id.,</i> at 883</a></span>. There is no indication that the quoted language was intended as anything more than a finding of fact, which would, quite obviously, dispose of the defendant's claim under any standard that might be suggested. In <i>Peterson</i> v. <i>United States,</i> <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/" aria-description="Citation for case: Gerald D. Peterson v. United States">411 F. 2d 1074</a></span> (CA8 1969), the court appeared to require a showing that the withheld evidence "was `material' and would have aided the defense." <span class="citation" data-id="285177"><a href="/opinion/285177/gerald-d-peterson-v-united-states/#1079" aria-description="Citation for case: Gerald D. Peterson v. United States"><i>Id.,</i> at 1079</a></span>. The court in <i>Lessard</i> v. <i>Dickson,</i> <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California...">394 F. 2d 88</a></span> (CA9 1968), found it determinative that the withheld evidence "could hardly be regarded as being able to have much force against the inexorable array of incriminating circumstances with which [the defendant] was surrounded." <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#91" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California..."><i>Id.,</i> at 91</a></span>. The jury, the court noted, would not have been "likely to have had any [difficulty]" with the argument defense counsel would have made with the withheld evidence. <span class="citation" data-id="9453575"><a href="/opinion/279966/albert-lessard-v-fred-r-dickson-warden-california-state-prison-san/#92" aria-description="Citation for case: Albert Lessard v. Fred R. Dickson, Warden California..."><i>Id.,</i> at 92</a></span>. Finally, <i>United States</i> v. <i>Tomaiolo,</i> <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/" aria-description="Citation for case: United States v. Charles Tomaiolo">378 F. 2d 26</a></span> (CA2 1967), required the defendant to show that the evidence was "material and of some substantial use to the defendant." <span class="citation" data-id="276039"><a href="/opinion/276039/united-states-v-charles-tomaiolo/#28" aria-description="Citation for case: United States v. Charles Tomaiolo"><i>Id.,</i> at 28</a></span>.</p>
<p>[5]  See, <i>e. g., </i><i>United States</i> v. <i>Morell,</i> <span class="citation" data-id="9462216"><a href="/opinion/330694/united-states-v-pedro-morell-and-ramon-bruzon/#553" aria-description="Citation for case: United States v. Pedro Morell and Ramon Bruzon">524 F. 2d 550, 553</a></span> (CA2 1975); <i>Ogden</i> v. <i>Wolff,</i> <span class="citation" data-id="8897326"><a href="/opinion/8909699/ogden-v-wolff/#822" aria-description="Citation for case: Ogden v. Wolff">522 F. 2d 816, 822</a></span> (CA8 1975); <i>Woodcock</i> v. <i>Amaral,</i> <span class="citation" data-id="325594"><a href="/opinion/325594/lyle-s-woodcock-v-r-w-amaral/#991" aria-description="Citation for case: Lyle S. Woodcock v. R. W. Amaral">511 F. 2d 985, 991</a></span> (CA1 1974); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="320391"><a href="/opinion/320391/united-states-of-america-charles-l-miller/#744" aria-description="Citation for case: United States of America, Charles L. Miller">499 F. 2d 736, 744</a></span> (CA10 1974); <i>Shuler</i> v. <i>Wainwright,</i> <span class="citation" data-id="316953"><a href="/opinion/316953/robert-shuler-and-jerry-chatman-v-louie-l-wainwright-direcotor-division/#1223" aria-description="Citation for case: Robert Shuler and Jerry Chatman v. Louie L. Wainwright,...">491 F. 2d 1213, 1223</a></span> (CA5 1974); <i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d, at 287</a></span>; <i>Clarke</i> v. <i>Burke,</i> <span class="citation" data-id="295841"><a href="/opinion/295841/charles-robert-clarke-v-john-c-burke/#855" aria-description="Citation for case: Charles Robert Clarke v. John C. Burke">440 F. 2d 853, 855</a></span> (CA7 1971); <i>Hamric</i> v. <i>Bailey,</i> <span class="citation" data-id="277986"><a href="/opinion/277986/bonnie-june-hamric-v-june-r-bailey-superintendent-of-the-west-virginia/#393" aria-description="Citation for case: Bonnie June Hamric v. June R. Bailey, Superintendent of...">386 F. 2d 390, 393</a></span> (CA4 1967).</p>
<p>[6]  That there is a significant difference between the Court's standards and what has been described as the prevailing view is made clear by Judge Friendly, writing for the court in <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9454610"><a href="/opinion/285114/united-states-v-james-miller/" aria-description="Citation for case: United States v. James Miller">411 F. 2d 825</a></span> (CA2 1969). After stating the court's conclusion that a new trial was required because of the Government's failure to disclose to the defense the pretrial hypnosis of its principal witness, Judge Friendly observed:
</p>
<p>"We have reached this conclusion with some reluctance, particularly in light of the considered belief of the able and conscientious district judge, who has lived with this case for years, that review of the record in light of all the defense new trial motions left him `convinced of the correctness of the jury's verdict.' We, who also have had no small exposure to the facts, are by no means convinced otherwise. The test, however, is not how the newly discovered evidence concerning the hypnosis would affect the trial judge or ourselves but whether, with the Government's case against [the defendant] already subject to serious attack, there was a significant chance that this added item, developed by skilled counsel as it would have been, could have induced a reasonable doubt in the minds of enough jurors to avoid a conviction. We cannot conscientiously say there was not." <span class="citation" data-id="9454610"><a href="/opinion/285114/united-states-v-james-miller/#832" aria-description="Citation for case: United States v. James Miller"><i>Id.,</i> at 832</a></span> (footnote omitted).</p>
<p>[7]  It is the presence of deliberate prosecutorial misconduct and a desire to deter such misconduct, presumably, that leads the Court to recognize a rule more readily permitting new trials in cases involving a specific defense request for information. The significance of the defense request, the Court states, is simply that it gives the prosecutor notice of what is important to the defense; once such notice is received, the failure to disclose is "seldom, if ever, excusable." <i>Ante,</i> at 106. It would seem to follow that if an item of information is of such obvious importance to the defense that it could not have escaped the prosecutor's attention, its suppression should be treated in the same manner as if there had been a specific request. This is precisely the approach taken by some courts. See, <i>e. g., </i><i>United States</i> v. <i>Morell,</i> <span class="citation" data-id="9462216"><a href="/opinion/330694/united-states-v-pedro-morell-and-ramon-bruzon/#553" aria-description="Citation for case: United States v. Pedro Morell and Ramon Bruzon">524 F. 2d, at 553</a></span>; <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="320391"><a href="/opinion/320391/united-states-of-america-charles-l-miller/#744" aria-description="Citation for case: United States of America, Charles L. Miller">499 F. 2d, at 744</a></span>; <i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="307845"><a href="/opinion/307845/united-states-v-irving-b-kahn-and-teleprompter-corporation/#287" aria-description="Citation for case: United States v. Irving B. Kahn and Teleprompter Corporation">472 F. 2d, at 287</a></span>; <i>United States</i> v. <i>Keogh,</i> <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#146" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d, at 146-147</a></span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Aigbekaen.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Aigbekaen
type: case
citation: "943 F.3d 713 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2019
court_level: coa
circuit: ca4
year: 2019
date_decided: 2019-11-21
docket: 17-4109
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4680725/united-states-v-raymond-aigbekaen/"
  cluster_id: 4680725
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Aigbekaen
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Border Searches]]"
    role: Key
related:
  - "[[Border Searches]]"
  - "[[Riley v. California]]"
  - "[[United States v. Cotterman]]"
tags:
  - case
  - fourth-amendment
  - search
  - border-search
  - digital-privacy
  - good-faith-exception
holding: "The border-search exception does not authorize a warrantless, nonroutine forensic search of a returning traveler's electronic devices unless the government's individualized suspicion bears some nexus to the exception's historic purposes — protecting national security, collecting duties, blocking unwanted entrants, or intercepting contraband; suspicion of purely domestic crimes is not enough, so the forensic searches of Aigbekaen's devices violated the Fourth Amendment, though the good-faith exception barred suppression."
---

# United States v. Aigbekaen

*943 F.3d 713 (4th Cir. 2019)* (No. 17-4109) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4680725 → opinion 4457978 (943 F.3d 713, decided 2019-11-21); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
A sixteen-year-old runaway told police that Raymond Aigbekaen and another man had trafficked her for sex across Maryland, Virginia, and New York. Homeland Security Investigations built a case tying Aigbekaen to the trafficking. When Aigbekaen returned to the United States from abroad in May 2015, agents seized his MacBook Pro, iPhone, and iPod at the airport and conducted warrantless forensic searches of all three devices under the border-search exception. He was charged with sex trafficking and related crimes and convicted after a nine-day trial; he appealed the denial of his motion to suppress the device evidence.

## Issue
Whether the border-search exception permits warrantless, nonroutine forensic searches of a returning traveler's electronic devices when the government's individualized suspicion concerns purely domestic crimes with no nexus to the historic rationales of the border-search doctrine.

## Rule
Building on *[[United States v. Kolsuz]]*, the Fourth Circuit held that to conduct an intrusive, nonroutine border search without a warrant, the government must have individualized suspicion of an offense bearing some nexus to the exception's purposes — protecting national security, collecting duties, blocking the entry of unwanted persons, or disrupting the import or export of contraband: "where a search at the border is so intrusive as to require some level of individualized suspicion, the object of that suspicion must bear some nexus to the purposes of the border search exception in order for the exception to apply. Because no such nexus existed here, the warrantless, nonroutine forensic searches violated the Fourth Amendment." — slip op. at 14.

## Application
HSI had probable cause to suspect Aigbekaen of grave domestic crimes, but that suspicion was "entirely unmoored" from the sovereign interests underlying the border-search exception. The Government's fallback theories failed: no affidavit ever alleged the devices held child pornography, and treating any "criminal" who carries the "instrumentalities" of a domestic offense across the border as supplying a nexus would erase the exception's distinction from a "generalized interest in law enforcement." Because no border nexus existed, the forensic searches were unconstitutional. The court nonetheless affirmed under the [[The Good-Faith Exception|good-faith exception]], since the agents had reasonably relied on then-unsettled law.

## Conclusion
Convictions **affirmed**: the warrantless forensic device searches violated the Fourth Amendment, but suppression was barred by the [[The Good-Faith Exception|good-faith exception]]. Motz, J., wrote for the majority (Motz, Wynn, JJ.); Richardson, J., concurred in the judgment, disagreeing with the nexus holding.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Aigbekaen* sharpens the digital border-search doctrine within the Fourth Circuit: even a highly intrusive forensic device search must be tethered to the border-search exception's own purposes, so probable cause to suspect a domestic crime — without any transnational or contraband nexus — does not bring the search within the exception.

## Appears on
- [[Border Searches]] — *Key*

## Sources
- [*United States v. Aigbekaen*, 943 F.3d 713 (4th Cir. 2019)](https://www.courtlistener.com/opinion/4680725/united-states-v-raymond-aigbekaen/) — pinpoint: slip op. at 14 (nexus requirement / Fourth Amendment holding); the CL opinion text carries the slip-opinion page numbers rather than 943 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b3a182aedb57101b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Aigbekaen"}, "payload": {"all": [{"cite": "943 F.3d 713", "page": "713", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "943"}], "display": "943 F.3d 713", "official": {"cite": "943 F.3d 713", "page": "713", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "943"}, "official_selection_present": true, "record_id": "United States v. Aigbekaen"}}
{"assertion_id": "763a8d95002ab7b9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Aigbekaen"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Aigbekaen", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Aigbekaen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Aigbekaen",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Raymond Aigbekaen",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Aigbekaen",
    "court": "4th Cir. 2019",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2019-11-21",
    "year": 2019,
    "docket": "17-4109",
    "cluster_id": 4680725,
    "lead_opinion_id": 4457978,
    "sibling_ids": [],
    "absolute_url": "/opinion/4680725/united-states-v-raymond-aigbekaen/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "943 F.3d 713",
      "volume": "943",
      "reporter": "F.3d",
      "page": "713",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "943 F.3d 713",
        "volume": "943",
        "reporter": "F.3d",
        "page": "713",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "943 F.3d 713",
    "official_selection": {
      "court_class": "state",
      "selected": "943 F.3d 713",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:49:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:49:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-aigbekaen--4680725",
      "to_record_id": "United States v. Aigbekaen",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Aigbekaen

```
                                     PUBLISHED

                      UNITED STATES COURT OF APPEALS
                          FOR THE FOURTH CIRCUIT


                                      No. 17-4109


UNITED STATES OF AMERICA,

                    Plaintiff – Appellee,

             v.

RAYMOND IDEMUDIA AIGBEKAEN,

                    Defendant – Appellant.



Appeal from the United States District Court for the District of Maryland, at Baltimore.
James K. Bredar, Chief District Judge. (1:15-cr-00462-JKB-2)


Argued: May 8, 2019                                       Decided: November 21, 2019


Before MOTZ, WYNN, and RICHARDSON, Circuit Judges.


Affirmed by published opinion. Judge Motz wrote the majority opinion, in which Judge
Wynn joined. Judge Richardson wrote an opinion concurring in the judgment.


ARGUED: Michael Lawlor, BRENNAN, MCKENNA & LAWLOR, CHTD., Greenbelt,
Maryland, for Appellant. Matthew James Maddox, OFFICE OF THE UNITED STATES
ATTORNEY, Baltimore, Maryland, for Appellee. ON BRIEF: Robert K. Hur, United
States Attorney, Ayn B. Ducao, Assistant United States Attorney, OFFICE OF THE
UNITED STATES ATTORNEY, Baltimore, Maryland, for Appellee.
DIANA GRIBBON MOTZ, Circuit Judge:

       In April of 2015, a minor alerted law enforcement officers that Raymond Idemudia

Aigbekaen and another man had trafficked her for sex in three mid-Atlantic states. As part

of the investigation that followed, when Aigbekaen returned to the United States from

traveling abroad, the Government seized his MacBook Pro laptop, iPhone, and iPod at the

airport and conducted warrantless forensic searches of the data on all three devices. The

Government subsequently charged Aigbekaen with sex trafficking and related crimes, and

at the conclusion of a nine-day trial, the jury convicted him of these crimes.

       Aigbekaen appeals, arguing primarily that the warrantless forensic searches of his

digital devices violated the Fourth Amendment.         The Government counters that the

searches fell within the “border search” exception to the warrant requirement and that, in

any event, suppression is not appropriate. We agree with Aigbekaen that the border search

exception does not extend to the challenged searches, rendering them unconstitutional. But

we agree with the Government that the good-faith exception to the exclusionary rule bars

suppression. Accordingly, we affirm.



                                             I.

       On April 12, 2015, a sixteen-year-old girl (to whom we, like the parties, refer

pseudonymously as “L.”) called 911 from a Homewood Suites hotel in Bel Air, Maryland.

L. reported that she had run away from home and was looking for help. When an officer

arrived on the scene and spoke with L., she claimed not to remember with whom she had

traveled or where she had been. But after some equivocation, L. disclosed that two men,

                                             2
one named Marcell Greene and another of Nigerian ethnicity named “Raymond,” had

transported her around Maryland, Virginia, and Long Island, New York; had posted ads of

her on Backpage.com; and had trafficked her for sex. L. provided phone numbers for these

men and identified Greene and Raymond Aigbekaen in hotel surveillance footage. She

also recognized images of herself from online prostitution ads on Backpage.com.

Homewood Suites records showed that Aigbekaen had rented L.’s hotel room. Officers

searched the room and found used condoms. 1

       Local law enforcement officers then sent their complete case file to Homeland

Security Investigations (HSI), an investigative arm of the U.S. Department of Homeland

Security.   After receiving the case file, HSI subpoenaed Verizon Wireless and

Backpage.com; the companies’ responses confirmed that the phone number L. had

provided indeed belonged to Aigbekaen, and that this number was listed as a contact on

the Backpage.com prostitution ads. The Backpage.com ads were also linked to two Yahoo!

email addresses, each of which contained portions of Aigbekaen’s name. HSI further

uncovered rental car and hotel records that showed Aigbekaen had traveled to hotels in

Maryland, Virginia, and Long Island.




       1
          By the time of Aigbekaen’s trial, L. was able to testify more fully that she and two
other girls had fled a group home in Dix Hills, New York in January 2015 to live with a
man named Y.P., who trafficked them for sex. L. was able to escape Y.P. with Greene’s
sister, Jasmine. But Jasmine relocated L. to Greene’s home, where Greene and Jasmine
decided to continue trafficking her. Greene then contacted Aigbekaen, who joined the
scheme. Greene and Aigbekaen proceeded to transport L. around Maryland, Virginia, and
Long Island, where she had sex for pay with as many as five men each day. Greene and
Aigbekaen kept all of the proceeds.
                                              3
        HSI agents learned that Aigbekaen had left the country and was set to return through

John F. Kennedy International Airport. The agents asked U.S. Customs and Border

Protection officers to seize any electronic media devices in Aigbekaen’s possession at the

airport upon his return. On May 19, 2015, the officers honored this request and, without

warrants, seized Aigbekaen’s MacBook Pro laptop computer, iPhone, and iPod. The

officers transported the devices to Baltimore, where an HSI agent created and reviewed a

forensic image of each device. HSI did not return the devices to Aigbekaen until June 2,

2015.       The forensic search 2 of the laptop revealed temporary backups of Facebook

Messenger conversations between Aigbekaen and another user that apparently related to

sex trafficking.

        A few months after the warrantless forensic searches, the Government secured and

executed search warrants for the same MacBook Pro and iPhone, Aigbekaen’s Facebook

and Yahoo! accounts, his vehicle, five additional cell phones, his DNA, and Greene’s

residence. A magistrate judge also granted the Government’s application to procure cell

site location information (“CSLI”) under the Stored Communications Act (“SCA”) without

obtaining a warrant.




        2
          A “forensic search” is “a powerful tool” capable of not only viewing data that a
user has intentionally saved on a digital device, but also “unlocking password-protected
files, restoring deleted material, and retrieving images viewed on websites.” United States
v. Cotterman, 709 F.3d 952, 957 (9th Cir. 2013). Unlike a “manual” search of a digital
device, a forensic search generally entails the connection of external equipment and/or the
use of specialized software. United States v. Kolsuz, 890 F.3d 133, 146 & n.6 (4th Cir.
2018).
                                             4
       In the midst of these warrant and SCA applications, a grand jury indicted Greene

and Aigbekaen on six counts, all of which related to interstate sex trafficking of L. and

transportation of her for the purpose of prostitution. Prior to trial, Aigbekaen moved to

suppress various pieces of evidence, including (as relevant here) any evidence recovered

from the May 2015 warrantless forensic searches.

       Aigbekaen argued that the May 2015 forensic searches were unconstitutional

because they were conducted without warrants and did not fall within the border search

exception to the warrant requirement. Aigbekaen maintained that “there has to be a point

at which the nature of the government investigation is so separated and so divorced from

anything related to the border” that the exception becomes inapplicable. He explained that

the Government’s “general interest in enforcing [domestic] criminal laws” does not

constitute an interest justifying “border searches.” The Government responded that, at the

time of the forensic searches, it had reasonable suspicion both that Aigbekaen had

trafficked L. for sex domestically and that he “might be bringing contraband in the form of

child pornography into the country,” citing for the latter argument only an “allegation from

the manager of the hotel where the victim was recovered.”

       At the close of the suppression hearing, the district court dismissed the

Government’s child pornography argument as “a lot weaker” but held that under “the

traditional border search analysis,” “the circumstances of where the property was and

where the person was when the search occurred” “trump[ed]” any need to justify the

specific search. As a result, the court found that no warrants were required for the May

2015 searches. The court further reasoned that if any individualized suspicion was needed

                                             5
to justify the “intrusive” forensic searches of Aigbekaen’s devices, the Government met

this standard because HSI had “at least” reasonable suspicion, if not probable cause, that

the warrantless searches would reveal evidence of domestic sex trafficking. 3

       The court thus denied the suppression motion, and Aigbekaen proceeded to trial.

After considering testimony from over twenty witnesses, a jury found Aigbekaen guilty on

all six counts. Aigbekaen timely noted this appeal.



                                             II.

       Aigbekaen’s principal argument on appeal is that the May 2015 warrantless forensic

searches of his laptop, iPhone, and iPod violated the Fourth Amendment. Although the

Government contends (and we ultimately agree) that the good-faith exception to the

exclusionary rule requires affirmance in any event, “when a Fourth Amendment case

presents a novel question of law whose resolution is necessary to guide future action by

law enforcement officers and magistrates, there is sufficient reason for [a court] to decide

the violation issue before turning to the good-faith question.” United States v. Bosyk, 933




       3
        Prior to trial, Aigbekaen also moved to suppress the CSLI on the ground that the
Government’s procurement of it constituted a search and so required a warrant. He later
conceded, and the district court held, that then-controlling circuit precedent foreclosed his
claim. See United States v. Graham, 824 F.3d 421, 424–25 (4th Cir. 2016) (en banc),
abrogated by Carpenter v. United States, 138 S. Ct. 2206, 2223 (2018). During the
pendency of this appeal, the Supreme Court vindicated Aigbekaen’s position. See
Carpenter, 138 S. Ct. at 2223. But as Aigbekaen acknowledges, binding circuit precedent
nevertheless precludes suppression of the CSLI because the Government obtained it in
good-faith reliance on a federal statutory scheme — namely, the SCA. United States v.
Chavez, 894 F.3d 593, 608 (4th Cir. 2018).
                                             6
F.3d 319, 332 n.10 (4th Cir. 2019) (alterations in original) (quoting Illinois v. Gates, 462

U.S. 213, 264 (1983) (White, J., concurring)).

       We review the district court’s legal conclusions de novo and its factual findings for

clear error, considering the record evidence in the light most favorable to the Government.

Kolsuz, 890 F.3d at 141–42. Because the Government conducted the challenged searches

without warrants, it bears the burden of proving, by a preponderance of the evidence, that

an exception to the warrant requirement applies. United States v. Davis, 690 F.3d 226, 262

(4th Cir. 2012).

                                             A.

       The Fourth Amendment requires that governmental searches and seizures be

reasonable. In most cases, this requires a warrant based on probable cause. See, e.g., Riley

v. California, 573 U.S. 373, 382 (2014). 4 “In the absence of a warrant, a search is

reasonable only if it falls within a specific exception to the warrant requirement.” Riley,

573 U.S. at 382.

       One such exception applies at our nation’s borders, where the Supreme Court has

long recognized the federal Government’s substantial sovereign interests in “protect[ing]

. . . territorial integrity” and national security, United States v. Flores-Montano, 541 U.S.



       4
         Aigbekaen maintains that Riley, which held the search incident to arrest exception
inapplicable to modern cell phones, similarly renders the border search exception
categorically inapplicable to modern cell phones and analogous digital devices. See id. at
403. However, we have held after Riley that law enforcement officers may conduct a
warrantless forensic search of a cell phone under the border search exception where the
officers possess sufficient individualized suspicion of transnational criminal activity. See
Kolsuz, 890 F.3d at 148. Accordingly, we must reject Aigbekaen’s interpretation of Riley.
                                             7
149, 153 (2004); blocking “the entry of unwanted persons and effects,” id. at 152;

“regulat[ing] the collection of duties,” United States v. Montoya de Hernandez, 473 U.S.

531, 537 (1985); and “prevent[ing] the introduction of contraband,” id. These Government

concerns are “at [their] zenith” at the border, whereas an individual’s “expectation of

privacy is less at the border than it is in the interior.” Flores-Montano, 541 U.S. at 152,

154. Thus, “[a]t a border” or its “functional equivalent, like [an] international airport . . .

government agents may conduct routine searches and seizures of persons and property

without a warrant or any individualized suspicion.” Kolsuz, 890 F.3d at 137 (internal

quotation marks omitted).

       Although this “border search” exception to the warrant requirement is broad, it is

not boundless. Even when the exception applies, the Supreme Court has explained that

certain “highly intrusive searches” may qualify as “‘nonroutine’” and so require some level

of individualized suspicion. Flores-Montano, 541 U.S. at 152 (quoting Montoya de

Hernandez, 473 U.S. at 541 n.4). Just last year, we applied this principle in the context of

an intrusive forensic search of a cell phone at the border. Given the “unparalleled breadth

of private information” that such a search could reveal, we held that “a forensic search of

a digital phone must be treated as a nonroutine border search, requiring some form of

individualized suspicion” even if not a warrant. Kolsuz, 890 F.3d at 145–46. 5 If the border

exception applies to the May 2015 forensic searches of Aigbekaen’s devices, these searches




       5
        We declined to decide whether reasonable suspicion was sufficient to justify such
a search or whether, instead, probable cause was required. Id. at 148.
                                              8
(like the forensic searches in Kolsuz) were sufficiently intrusive to be “nonroutine” and so

required some level of individualized suspicion. Id. at 137.

       But this raises another question: Does the border exception even apply to the May

2015 forensic searches?      Phrased differently, of what must the Government have

individualized suspicion for the border search exception to apply? Again, precedent offers

a clear answer. As the Supreme Court and this court have repeatedly explained, “the scope

of a warrant exception should be defined by its justifications.” Id. at 143 (citing Riley, 573

U.S. at 385–91); accord, e.g., Arizona v. Gant, 556 U.S. 332, 351 (2009) (“When the[]

justifications” underlying an exception to the warrant requirement “are absent, a

[warrantless] search . . . will be unreasonable . . . .”). That is to say, a warrant exception

will not excuse a warrantless search where applying the exception “would untether the rule

from the justifications underlying [it].” Riley, 573 U.S. at 386 (internal quotation marks

omitted).

       The same limitation applies to the border search exception. Indeed, neither the

Supreme Court nor this court has ever authorized a warrantless border search unrelated to

the sovereign interests underpinning the exception, let alone nonroutine, intrusive searches

like those at issue here. Rather, our decision in Kolsuz teaches that the Government may

not “invoke[] the border exception on behalf of its generalized interest in law enforcement

and combatting crime.” 890 F.3d at 143. This restriction makes particularly good sense

as applied to intrusive, nonroutine forensic searches of modern digital devices, which store

vast quantities of uniquely sensitive and intimate personal information, id. at 145 (citing

Riley, 573 U.S. at 393–97), yet cannot contain many forms of contraband, like drugs or

                                              9
firearms, the detection of which constitutes “the strongest historic rationale for the border-

search exception,” United States v. Molina-Isidoro, 884 F.3d 287, 295 (5th Cir. 2018)

(Costa, J., concurring).

       Accordingly, as we explained in Kolsuz, 890 F.3d at 143, to conduct such an

intrusive and nonroutine search under the border search exception (that is, without a

warrant), the Government must have individualized suspicion of an offense that bears some

nexus to the border search exception’s purposes of protecting national security, collecting

duties, blocking the entry of unwanted persons, or disrupting efforts to export or import

contraband. See also United States v. Ramsey, 431 U.S. 606, 620 (1977) (“The border-

search exception is grounded in the recognized right of the sovereign to control, subject to

substantive limitations imposed by the Constitution, who and what may enter the

country.”). If a nonroutine search becomes too “attenuated” from these historic rationales,

it “no longer [will] fall under” the exception.       Kolsuz, 890 F.3d at 143.       In such

circumstances, the search will be unconstitutional unless accompanied by a warrant or

justified under a different exception to the warrant requirement.

       Applying these principles to the facts at hand, we can only conclude that the

warrantless forensic searches of Aigbekaen’s devices in May of 2015 lacked the requisite

nexus to the recognized historic rationales justifying the border search exception. Of

course, when Aigbekaen landed at the airport with his MacBook Pro, iPhone, and iPod in

tow, HSI agents had not only reasonable suspicion but probable cause to suspect that he

had previously committed grave domestic crimes. But these suspicions were entirely

unmoored from the Government’s sovereign interests in protecting national security,

                                             10
collecting or regulating duties, blocking Aigbekaen’s own entry, or excluding contraband.

Thus, holding the border search exception applicable here, based simply on the

Government’s knowledge of domestic crimes, would “untether” that exception from its

well-established justifications. Riley, 573 U.S. at 386.

       Resisting this result, the Government asserts that Aigbekaen’s crime “clearly was

one that is the proper subject of a border search, because [sex trafficking] is a crime

‘commonly involving cross-border movements.’” Supp. Response Br. at 13 (quoting

United States v. Caballero, 178 F. Supp. 3d 1008, 1017 n.7 (S.D. Cal. 2016)). Of course,

the general character of a crime may be relevant to an officer’s reasonable suspicion that it

involves a transnational component. But inherent in the notion of individualized suspicion

is some evidentiary basis for what a specific crime does involve in the individual case at

hand, not just what it “commonly involves” as a general matter. Here, the Government has

offered no reasonable basis to suspect that Aigbekaen’s domestic crimes had any such

transnational component.

       We also must reject the district court’s conclusion that a nonroutine, intrusive

search’s physical and temporal proximity to an international border “trumps everything”

under the Fourth Amendment. To be sure, the Supreme Court has stated that routine border

searches “are reasonable simply by virtue of the fact that they occur at the border.” Ramsey,

431 U.S. at 616. But in the context of “highly intrusive” nonroutine border searches,

Flores-Montano, 541 U.S. at 152, the Court has explicitly struck a “balance between the

interests of the Government and the privacy right of the individual,” Montoya de

Hernandez, 473 U.S. at 540; see also Riley, 573 U.S. at 385 (instructing courts to evaluate

                                             11
any exception to the warrant requirement by weighing individual privacy interests against

“legitimate governmental interests” (quoting Wyoming v. Houghton, 526 U.S. 295, 300

(1999))). Consistent with this balancing, we clarified in Kolsuz that a nonroutine search’s

location is not dispositive of whether the border search exception applies; rather, it is the

search’s relation to the Government’s sovereign interests that is paramount. 890 F.3d at

142–43.

       Moreover, “the ultimate touchstone of the Fourth Amendment is reasonableness.”

Riley, 573 U.S. at 381 (internal quotation marks omitted). And on the facts of this case,

the reasonableness of requiring law enforcement to secure a warrant before conducting an

intrusive forensic search of a traveler’s digital device, solely to seek evidence of crimes

with no transnational component, is readily apparent. By the time Aigbekaen arrived at

the airport with his devices, and prior to any searches of those devices, HSI agents had

probable cause to believe that Aigbekaen’s laptop, at least, contained evidence of domestic

sex trafficking. Indeed, in August of 2015, HSI secured warrants to search both the

MacBook Pro and the iPhone, relying almost exclusively on evidence that was in agents’

possession before Aigbekaen arrived at the airport in May. Given the information in its

possession at the time, it is only reasonable to expect the Government to have procured

these warrants prior to the May searches. 6


       6
        Of course, if HSI agents were unable to timely secure such warrants and reasonably
feared that Aigbekaen would destroy the evidence in the meantime, the exigent
circumstances exception might apply. See Riley, 573 U.S. at 402 (noting that Fourth
Amendment “exigencies could include the need to prevent the imminent destruction of
evidence in individual cases”). But the Government does not even suggest that exigency
played any role here.
                                              12
       In contrast, it would be patently unreasonable to permit highly intrusive forensic

Government searches of travelers’ digital devices, without warrants, on bases unrelated to

the United States’s sovereign authority over its borders. To be clear, we do not question

the import of the Government’s general interest in combatting crime. But we cannot agree

that this interest categorically eclipses individuals’ privacy interests in the vast troves of

data contained on their digital devices when the suspected offenses have little or nothing

to do with the border.

       As the Supreme Court explained in Riley, “[m]odern cell phones, as a category,

implicate privacy concerns far beyond those implicated” by physical searches. Id. at 393.

This is so because cell phones and other modern digital devices feature “an element of

pervasiveness” that distinguishes them from physical records; these days, “it is the person

who is not carrying a cell phone, with all that it contains, who is the exception.” Id. at 395.

At the same time, these devices have “immense storage capacity,” as well as cloud storage

capabilities, which they use to collect “in one place many distinct types of information . . .

that reveal much more in combination than any isolated record.” Id. at 393–94, 397. These

include unusually sensitive data regarding one’s relationships, personal interests and

preferences, prior internet searches, location history, and much more. Id. at 395–96. To

adopt the Government’s position, we would need to hold that it could conduct a warrantless

forensic search of any traveler’s cell phone — uncovering all of this data, including

“password-protected” and “deleted material[s],” Cotterman, 709 F.3d at 957 — on

suspicion that the phone may contain evidence of any prior domestic crime.



                                              13
       Because Aigbekaen does not challenge any routine border searches, we need not

decide whether or how the interests that underpin the border search exception constrain, in

practice, the Government’s broad and historic authority to conduct suspicionless searches

of individuals and their effects at the border. Ramsey, 431 U.S. at 616. Similarly, we need

not determine what quantum of individualized suspicion, if any, beyond the familiar

reasonable-suspicion standard is needed to justify a warrantless forensic search of a device

at the border.

       We simply apply the teaching of Kolsuz: where a search at the border is so intrusive

as to require some level of individualized suspicion, the object of that suspicion must bear

some nexus to the purposes of the border search exception in order for the exception to

apply. Because no such nexus existed here, the warrantless, nonroutine forensic searches

violated the Fourth Amendment.

                                            B.

       The Government briefly presses two secondary arguments in an attempt to establish

that the May 2015 searches were constitutional. Neither is persuasive.

       First, the Government devotes four sentences of briefing to a claim that at the time

of the warrantless searches, it “had a concern” that Aigbekaen’s devices “might” contain

not only evidence of past crimes, but also child pornography. Because of this “concern,”

the Government maintains, the warrantless forensic searches featured both individualized

suspicion and the requisite nexus to a dominant interest underpinning the border search

exception: preventing contraband from entering the country.



                                            14
       Like the district court, we do not find this claim persuasive. Even assuming that a

warrantless forensic search of a digital device at the border could be justified by reasonable

suspicion, 7 we can discern no “particularized and objective basis” in the record for agents

to reasonably suspect that Aigbekaen possessed child pornography on his devices.

Montoya de Hernandez, 473 U.S. at 541 (internal quotation marks omitted).                The

Government’s stated “concern” is based on a local police officer’s brief testimony, during

the suppression hearing, that a hotel manager received a tip from an unnamed employee

that the employee had “overheard one of the gentlem[e]n staying in the room [saying], you

know, let’s hurry up and get this video done.” Suppr. Hr’g Tr., ECF No. 193, at 217–19.

During cross-examination, the officer was asked if the hotel manager “ever g[a]ve [him]

any other indication as to why that [unnamed] employee thought that there was some type

of movie making or video making going on,” to which he replied, “No.” Id. at 217. At

trial, although the hotel manager recounted in detail the events surrounding L.’s 911 call,

he could no longer recall hearing any such statement from an employee or relating it to law

enforcement. 9/23/16 Trial Tr., ECF No. 259, at 69–70, 76. This isolated, vague, and

third-hand allegation does not rise to the level of reasonable suspicion. 8




       7
         See Kolsuz, 890 F.3d at 148 (declining to determine “whether more than reasonable
suspicion is required for a search of this nature”).
       8
         Notably, although the Government asserted at oral argument before us that it had
probable cause (not just reasonable suspicion) to suspect Aigbekaen’s devices contained
child pornography, not one of HSI’s numerous warrant affidavits and CSLI applications
included any such allegations. Nor did the HSI agent who testified at the suppression
hearing mention any suspicion that Aigbekaen’s devices contained child pornography.
                                             15
       Second, the Government suggests that the requisite nexus to the purposes of the

border search exception was present because Aigbekaen was a “criminal[]” seeking to enter

the United States and carried the “instrumentalities” of his domestic crime (that is, his

digital devices) into the country with him. Again, we must disagree. If the border search

exception is to retain any distinction from the Government’s “generalized interest in law

enforcement and combatting crime,” Kolsuz, 890 F.3d at 143, it cannot be invoked to

sanction invasive and nonroutine warrantless searches of all suspected domestic

“criminals,” nor the suspected “instrumentalities” of their domestic crimes. Importantly,

the Government does not contend (save for its unavailing child pornography claim) that

these “instrumentalities” were contraband.

       Because the Government lacked sufficient individualized suspicion of criminal

activity with any nexus to the sovereign interests underlying the border search exception,

its warrantless forensic searches of Aigbekaen’s devices violated the Fourth Amendment.



                                             III.

       In the alternative, the Government argues that any constitutional infirmity in the

May 2015 searches does not justify reversal for several independent reasons. We turn now

to these contentions.

                                             A.

       In its brief, the Government maintains that any dispute over these searches is moot

because no tainted evidence was admitted at trial. However, the record belies this assertion.

At the very least, HSI’s affidavit in support of the warrant to search Aigbekaen’s Facebook

                                             16
account relied on conversations and screen shots uncovered during the May 2015

searches. 9 And the Government introduced the Facebook warrant returns at trial.

       At oral argument before us, the Government did not dispute these facts. Instead, it

sought to refashion its mootness claim, asserting in its place that the August 2015 warrant-

backed searches of Aigbekaen’s devices constituted an “independent source” that cured

any taint from the prior warrantless searches. The record evidence, however, does not

support application of the independent-source doctrine. Under that doctrine, evidence

“initially discovered during, or as a consequence of, an unlawful search, but later obtained

independently from activities untainted by the initial illegality” may be admitted at trial.

Murray v. United States, 487 U.S. 533, 537 (1988). But later activities, like the August

2015 searches, do not qualify as independent sources if “the agents’ decision to seek the

warrant[s] was prompted by what they had seen during the initial [searches].” Id. at 542.

As the Government conceded at oral argument, the district court did not make any factual

findings on this point. Mindful of the Supreme Court’s admonition that “it is the function

of the District Court rather than the Court of Appeals to determine the facts,” id. at 543, we

cannot assume in the first instance that the August 2015 warrants were not prompted by

the May 2015 warrantless searches.

                                             B.

       The Government next contends that the good-faith exception to the exclusionary

rule bars suppression of any evidence tainted by any constitutional defect in the May 2015


       9
        The district court later opined that the probable cause underlying this warrant, even
with these allegations, was “a little thin.”
                                             17
searches. Aigbekaen counters that the lack of a nexus renders the good-faith exception

inapplicable. On this point, we must agree with the Government.

       The evidentiary fruits of Fourth Amendment violations are generally inadmissible

at trial. See Wong Sun v. United States, 371 U.S. 471, 484–85 (1963). But the fruits of “a

search conducted in reasonable reliance on binding precedent [are] not subject to the

exclusionary rule,” as that rule is designed “to deter future Fourth Amendment violations.”

Davis v. United States, 564 U.S. 229, 236–37, 241 (2011) (emphasis added).

       In this case, the HSI agents who searched Aigbekaen’s devices in May of 2015

reasonably relied on an “established and uniform body of precedent allowing warrantless

border searches of digital devices.” Kolsuz, 890 F.3d at 148. Although it has long been

understood that the scope of a warrant exception should be tailored to the purposes

underlying that exception, no court had yet applied that principle to require a warrant “for

any border search, no matter how nonroutine or invasive.” Id. at 147; see also Molina-

Isidoro, 884 F.3d at 294 (Costa, J., concurring) (noting that “no reported federal decision

has required a warrant for any border search”). Only in 2018 did this court recognize that

“a search initiated at the border could become so attenuated from the rationale for the

border search exception that it no longer would fall under that exception” and so require a

warrant. Kolsuz, 890 F.3d at 143. And only today have we applied that principle to hold

unconstitutional such an attenuated, warrantless, nonroutine forensic search at the border.

       Tellingly, Aigbekaen offers almost no argument against application of the good-

faith exception, save for a question-begging allegation that the Government “attempt[ed]

to exploit an exception to the Fourth Amendment warrant requirement.” He may well be

                                            18
correct that even prior to Kolsuz, “the better practice” would have been for the Government

to get a warrant in the first place. But good faith does not mandate best practices. Given

the uniform body of precedent that permitted warrantless searches at the border in May of

2015, we cannot help but conclude that the good-faith exception applies here. 10



                                              IV.

       For the foregoing reasons, the judgment of the district court is

                                                                                  AFFIRMED.




       10
          Aigbekaen also argues, in supplemental briefing, that the multi-week seizures of
his digital devices constituted an unreasonable interference with his possessory interests.
See United States v. Pratt, 915 F.3d 266, 271–73 (4th Cir. 2019). However, Aigbekaen
opted neither to press this claim before the district court nor to raise it in his opening brief
to this court. In fact, when the district court asked Aigbekaen’s counsel whether he
intended to develop a factual record regarding the reasonableness of the seizures, his
counsel chose not to “request[] any further information” on the issue. We decline to
address this forfeited claim. In his pro se brief and supplemental briefs, Aigbekaen also
raises a host of additional challenges to his conviction and sentence. Although “an
appellant who is represented by counsel has no right to file pro se briefs or raise additional
substantive issues in an appeal,” United States v. Cohen, 888 F.3d 667, 682 (4th Cir. 2018),
we have examined Aigbekaen’s contentions and find no reversible error.
                                              19
RICHARDSON, Circuit Judge, concurring in the judgment:

       For the first time in this Circuit, the Majority holds a border search unlawful by

applying a “nexus” requirement tethered to narrowly defined purposes that supposedly

underlie the border-search doctrine: national security, blocking the entry of persons, and

disrupting the trafficking of contraband. And, although my good colleagues agree that law

enforcement reasonably suspected a foreign national of interstate sex trafficking, this

reasonable suspicion is not enough for them. Because interstate sex trafficking—as

“distinguished” from international sex trafficking—lacks the Majority’s requisite nexus to

the perceived purposes of the border-search doctrine, the Majority holds the search of a sex

trafficker’s cell phone at the border violates the Fourth Amendment.

       In my view, the Majority errs in adopting a “nexus” test that is in deep tension with

Supreme Court precedent. And even assuming the “nexus” test were proper, I would find

it satisfied here.

       In the end, the Majority affirms Aigbekaen’s conviction based on the good-faith

exception to the exclusionary rule. And I agree with that judgment. But I respectfully

disagree with the decision to declare this border search unlawful.

                                             I.

       The Fourth Amendment prohibits “unreasonable searches and seizures.” U.S.

CONST. amend. IV. And as the Supreme Court has explained, “reasonableness” is the

“ultimate touchstone of the Fourth Amendment.” Riley v. California, 573 U.S. 373, 381

(2014) (quoting Brigham City v. Stuart, 547 U.S. 398, 403 (2006)). In determining what

is reasonable, courts look to longstanding traditions with an eye towards determining “that


                                            20
degree of privacy against government that existed when the Fourth Amendment was

adopted.” United States v. Jones, 565 U.S. 400, 406 (2012) (quoting Kyllo v. United States,

533 U.S. 27, 34 (2001)); see also Riley, 573 U.S. at 382 (looking to the historical bases for

a search incident to arrest).

       One such tradition, the “border-search doctrine,” gives government agents at

international borders broad discretion to search people and their effects. United States v.

Ramsey, 431 U.S. 606, 616–17 (1977). The border-search doctrine has “a history as old as

the Fourth Amendment itself,” id. at 619, and rests on the principle “that the United States,

as sovereign, has the inherent authority to protect, and a paramount interest in protecting,

its territorial integrity,” United States v. Flores-Montano, 541 U.S. 149, 153 (2004); cf.

United States v. Curtiss-Wright Exp. Corp., 299 U.S. 304, 318 (1936) (describing territorial

integrity as inherent to sovereignty). Thus, the government’s “interest in preventing the

entry of unwanted persons and effects is at its zenith at the international border.” Flores-

Montano, 541 U.S. at 152. And travelers understand that they subject themselves and their

property to some form of search by crossing international boundaries. As a result, “the

expectation of privacy is less at the border than it is in the interior.” Id. at 154.

       Supreme Court jurisprudence purports to reflect the border-search doctrine’s

historical scope. See Ramsey, 431 U.S. at 616–19; see also Boyd v. United States, 116 U.S.

616, 623–24 (1886). But in the three decades since Ramsey, more historical work has been

done to understand the Fourth Amendment. See, e.g., WILLIAM J. CUDDIHY, The Fourth

Amendment: Origins and Original Meaning 602–1791 (2009). And in recent years, some

work has begun to better understand the border-search doctrine itself—analyzing the


                                               21
backdrop English common-law doctrine, the historical understanding of sovereign

prerogatives under international law, the drafting and ratification history of the Fourth

Amendment (and relevant state analogues), and statutes enacted around the time the Bill

of Rights was ratified (such as the Collection Acts of 1789 and 1790). See, e.g., Note, The

Border Search Muddle, 132 HARV. L. REV. 2278, 2287–97 (2019).

       Based on this more recent historical work, one might ask whether Ramsey’s

historical analysis would change (or perhaps be confirmed) if we were to revisit the

relevant historical sources (including those left aside by Ramsey). But this case is neither

the time nor the place to do so. We are an inferior court (to say nothing of the lack of

briefing focused on this historical inquiry and a somewhat limited academic literature

focused on the border-search doctrine). As an inferior court, we take the Supreme Court’s

precedents as we find them.

       And the Supreme Court has repeatedly upheld border agents’ broad discretion to

conduct searches in sweeping terms, requiring particularized suspicion only for especially

intrusive searches.   The distinction between “routine” searches and highly intrusive

“nonroutine” searches provides the analytical linchpin for determining whether

particularized suspicion is required at the border. An agent may undertake routinely

intrusive border searches of international travelers—such as patting them down for

weapons and rummaging through their luggage—with no articulable suspicion. Flores-

Montano, 541 U.S. at 152.

       Highly intrusive searches at the border that are deemed nonroutine are different. For

this limited category, the government must articulate reasonable suspicion. United States


                                            22
v. Montoya de Hernandez, 473 U.S. 531, 542 (1985). 1 In Montoya de Hernandez, border

agents suspected a woman, who had arrived on an international flight, of swallowing

balloons containing illegal drugs. Id. at 534−35. Agents strip searched the woman and

detained her for over sixteen hours so that they could inspect the results of a bowel

movement. Id. at 535. Eventually, a federal magistrate authorized a rectal examination,

which uncovered a balloon filled with cocaine (the first of eighty-eight ultimately

revealed). Id. Even on these facts, the Supreme Court held that only reasonable suspicion

was needed to detain the woman. Id. at 541.

       The Supreme Court has suggested that only three highly intrusive situations may

qualify as nonroutine: (1) “highly intrusive searches of the person,” (2) searches of

property that are “destructive,” and (3) searches carried out in a “particularly offensive”

manner.    Flores-Montano, 541 U.S. at 152–56, 154 n.2; see also United States v.

Cotterman, 709 F.3d 952, 973 (9th Cir. 2013) (en banc) (Callahan, J., concurring in part,

dissenting in part, and concurring in the judgment).

       In making this distinction based on the intrusiveness of a search, the Court considers

whether the subject of a search is a person or property. Despite hinting at the possibility

that a “destructive” search of property might amount to a nonroutine search, see Flores-

Montano, 541 U.S. at 152–56, 154 n.2, the Supreme Court has never actually held that any

search of property—as opposed to persons—was “nonroutine.” See, e.g., United States v.


       1
        The potential that particularized suspicion might be required for more intrusive
searches had been left open by older precedents. See Ramsey, 431 U.S. at 618 n.13 (not
“decid[ing] whether, and under what circumstances, a border search might be deemed
‘unreasonable’ because of the particularly offensive manner in which it is carried out”).

                                             23
Touset, 890 F.3d 1227, 1234 (11th Cir. 2018) (“Property and persons are different.”). And

the Court has set a high bar for when a property search might ever rise to that level. In

Flores-Montano, the Court held that customs officers conducted only a “routine” search

when they stopped and dissembled a vehicle to remove and inspect its gas tank. 541 U.S.

at 155–56. In so holding, the Court instructed that, where border searches of property were

involved, only “destructive” or otherwise “particularly offensive” searches of that property

would be so intrusive as to require any particularized suspicion. See id. at 154 n.2. The

Supreme Court also chastised lower courts for being too quick to undermine the simplicity

of the border-search doctrine for property with “[c]omplex balancing tests to determine

what is a ‘routine’ search,” explaining that such tests “have no place in border searches of

vehicles.” Id. at 152.

       Despite that guidance on searches of property at the border, in United States v.

Kolsuz, 890 F.3d 133 (4th Cir. 2018), we held that a detailed “forensic” search—as opposed

to a “manual” search—of an international traveler’s electronic devices at the border was

“nonroutine” and thus required particularized suspicion. See id. at 144 (relying, in part, on

Riley v. California, 573 U.S. 373 (2014)). That holding may be controversial. See, e.g.,

Touset, 890 F.3d at 1233–36. But whatever one thinks of creating a constitutional

distinction between “forensic” and “manual” searches of property, it is the law of our

circuit. And so I assume that some degree of suspicion was required for the forensic search

of Aigbekaen’s electronic devices.

       Kolsuz also addressed, and rejected, an argument that the search in that case had an

inadequate “nexus” to the purposes of the border-search doctrine. We first observed that,


                                             24
“[a]s a general rule, the scope of a warrant exception should be defined by its

justifications.” Kolsuz, 890 F.3d at 143 (citing Riley, 573 U.S. at 384–92). We then noted,

in general terms, the possibility that a search “could become so attenuated from the

rationale for the border search exception that it would no longer fall under that exception.”

Kolsuz, 890 F.3d at 143 (emphasis added). We held that the search before us in that case

did not fail “on any account of a ‘nexus’ requirement” because the crime being investigated

had a “transnational” nature. Id. That is, Kolsuz held that suspicion of transnational crime

was sufficient to satisfy any potential “nexus” requirement.

       Kolsuz did not hold that such suspicion was necessary for a border search. Nor did

Kolsuz explain the rationale for the border-search doctrine or otherwise explore the bounds

of what constitutes an adequate transnational “nexus.” And so the Majority overstates the

case when it claims that Kolsuz held that “where a search at the border is so intrusive as to

require some level of individualized suspicion, the object of that suspicion must bear some

nexus to the purposes of the border search exception in order for the exception to apply.”

Majority Op. at 14. Kolsuz merely noted the possible existence of a “nexus” requirement

and, assuming it existed, concluded that it was satisfied.

                                             II.

       In this case, the Majority goes beyond Kolsuz by imposing this transnational

“nexus” requirement to hold a border search unlawful for the first time in our circuit.

                                             A.

       Before evaluating the Majority’s “nexus” requirement, I briefly note what I

understand it to be, and not to be. The Majority opinion does not cast doubt on non-


                                             25
invasive searches (like going through someone’s luggage) that happen every day at the

border. If such “routine” searches could be challenged as having an inadequate “nexus” to

the border, the border-search doctrine would be eviscerated. Thankfully, the Majority does

not go there (although it does not rule out the possibility of going there in the future, and it

may be challenging to maintain a principled reason for not doing so). 2

       Instead, the Majority’s “nexus” requirement comes into play (for now) only for the

more intrusive “nonroutine” searches that already require objective, particularized

suspicion. It seeks to regulate what kind of particularized suspicion is required. In the

Majority’s view, the grounds for suspicion must dovetail with the ultimate purposes of the




       2
         The Ninth Circuit has gone there. United States v. Cano, 934 F.3d 1002, 1016 (9th
Cir. 2019) (holding that “border searches are limited in scope to searches for contraband
and do not encompass searches for evidence of past or future border-related crimes”). In
that case, the court held that agents could conduct a “manual” search of a phone without
any suspicion but that the search exceeded the permissible scope of a border search when
agents recorded phone numbers and messages. Id. at 1019. The Ninth Circuit reasoned
that recording numbers and messages went beyond what was reasonably necessary to
search for contraband. Id. I find the Ninth Circuit’s reasoning on that point hard to accept,
both for the reasons I explain below and under the plain-view doctrine: surely, if officers
have discovered information during a lawful search, recording that information does not
render the search unlawful.

                                              26
border-search doctrine. 3       Having reason to believe that the search will uncover

contraband—for example, that the person’s cell phone contains child pornography—

necessarily corresponds to the Majority’s purposes of the border-search doctrine. The

Majority is also willing to permit searches for evidence of “transnational” criminal activity.

But when agents seek evidence of domestic crimes, my colleagues decide they need

probable cause and a warrant.

                                                      B.

         This “nexus” requirement is inconsistent with the Supreme Court’s border-search

cases.       Those cases consistently describe the government’s powers at the border in

sweeping terms:

                 Time and again, we have stated that “searches made at the
                 border, pursuant to the longstanding right of the sovereign to
                 protect itself by stopping and examining persons and property
                 crossing into this country, are reasonable simply by virtue of
                 the fact that they occur at the border.” . . . It is axiomatic that
                 the United States, as sovereign, has the inherent authority to
                 protect, and a paramount interest in protecting, its territorial
                 integrity.

Flores-Montano, 541 U.S. at 152–53 (quoting Ramsey, 531 U.S. at 616). The Supreme

Court has limited the border-search doctrine only when the intrusiveness of the search

makes it unreasonable without particularized suspicion—not based on the government’s


         3
         The precise type of “reasonable suspicion” required to establish a nexus has
divided courts. Compare United States v. Cano, 934 F.3d at 1020 (narrower: reasonable
suspicion that searched item contains contraband), with Majority Op. at 9–11 (broader:
reasonable suspicion of prohibited transnational activity). Of course, in the context of
border searches involving child pornography stored in cell phones, the suspicion of
contraband (child pornography) and of ongoing prohibited transnational activity
(smuggling of child pornography) will overlap.

                                                 27
interests or a “nexus” between these interests and the specific search conducted. See id.

The Court has authorized no further exceptions to the near-absolute description of the

doctrine in Flores-Montano and Ramsey. In fact, it has cautioned lower courts against

creating them. Id.

       The Majority’s innovation is to limit the border-search doctrine based not on the

intrusiveness of the search, but on the nature of the government’s interests at stake. Not

only is there no support for this innovation in the Supreme Court’s border-search cases, but

this also ignores the Court’s admonitions to interpret the doctrine broadly and avoid

creating new limitations.

       Now there is an argument that the border-search doctrine should be limited in this

way—or perhaps even more narrowly. Some jurists have taken the view that the border-

search doctrine is concerned solely with detection of contraband. See, e.g., Cano, 934 F.3d

at 1016−19; United States v. Vergara, 884 F.3d 1309, 1317 (11th Cir. 2018) (Pryor, J.,

dissenting). And this narrow reading has some historical support. After all, the Supreme

Court has mainly grounded the border-search doctrine in founding-era statutes that

authorized warrantless customs inspections. Ramsey, 431 U.S. at 616–17 (citing Act of

July 31, 1789, ch. 5, § 24, 1 Stat. 29, 43); see also Act of Aug. 4, 1790, ch. 35, § 31, 1 Stat.

145, 164–65 (permitting revenue collectors to board and search vessels in coastal waters

without suspicion); id. at §§ 47–48, 1 Stat. at 169–70 (permitting revenue collectors to open

containers on vessels “on suspicion of fraud” without a warrant).

       On the other hand, there are reasons to conclude that this “contraband-only” view

might be too narrow given the interests of the United States, as sovereign, at its territorial


                                              28
borders. As we observed in Kolsuz, the government has a broader national-security interest

at the border that goes beyond the immediate search for contraband. 890 F.3d at 143. So

we noted that the doctrine should encompass searches for evidence of “ongoing efforts to

export contraband illegally, through searches initiated at the border,” id. at 143−44, not just

“direct interception of contraband,” id. at 143. Thus construed, the purposes of the border-

search doctrine overlap to some degree with general law enforcement.

       And the Supreme Court has described the border-search doctrine as being concerned

with regulating the movement not only of goods, but also of people. Carroll v. United

States, 267 U.S. 132, 154 (1925). It is “‘without doubt’ that the power to exclude aliens

‘can be effectuated by routine inspections and searches of individuals or conveyances

seeking to cross our borders.’” Ramsey, 431 U.S. at 619 (quoting Almeida-Sanchez v.

United States, 413 U.S. 266, 272 (1973)); see also United States v. Oriakhi, 57 F.3d 1290,

1296 (4th Cir. 1995) (“From the sovereign’s power to protect itself is derived its power to

exclude harmful influences, including undesirable aliens, from the sovereign’s territory.”).

And the Supreme Court has articulated the federal government’s control over migration—

and the nation’s borders—as near-plenary. See, e.g., Ramsey, 431 U.S. at 619; see also

U.S. ex rel. Knauff v. Shaughnessy, 338 U.S. 537, 542 (1950).

       But no matter how we, as lower-court judges, might wish to shape the doctrine, we

are not free to rewrite the Supreme Court’s case law based on our own ideas. And that law

is sweeping in its deference to the authority of the government to conduct searches at the

border.




                                              29
       Without support in the Court’s border-search cases, the Majority bases its “nexus”

requirement on the Court’s analysis of the search-incident-to-arrest exception in Riley v.

California, 573 U.S. 373 (2014). Like the Kolsuz panel, my colleagues read Riley to say

that, “[a]s a general rule, the scope of a warrant exception should be defined by its

justifications.” Kolsuz, 890 F.3d at 143. But transplanting Riley’s “general rule” into the

specific context of border searches to support the “nexus” requirement raises at least two

problems.

       First, Riley said nothing about border searches; it concerned the far different context

of searches incident to arrest. We cannot, as lower-court judges, strain to insert the

Supreme Court’s reasoning from one line of cases into another where it does not fit.

Particularly where two areas of case law point in different directions, we must follow the

cases that are most on point. 4 And as I have explained, the Court has never held that the

border-search doctrine should be “defined by its justifications.” Id. at 143. To the contrary,

it has articulated the doctrine in sweeping terms and told us to apply it accordingly.




       4
         There are, moreover, important differences between a search incident to arrest and
a border search. These differences undermine any reliance on Riley’s search-incident-to-
arrest analysis to support the “nexus” requirement in the border-search context. For one,
the two doctrines have different justifications. The border-search doctrine, unlike the
search-incident-to-arrest doctrine, implicates the sovereign’s paramount interest in
protecting its territorial integrity—suggesting a far broader scope than the narrower
rationales justifying the search-incident-to-arrest doctrine. And unlike searches incident to
arrest, border searches are based in part on implied consent. Just as airline passengers
understand that having their bodies scanned and their bags x-rayed is part of the price of
admission to modern airports, so travelers at international crossings have long understood
that they are subjecting themselves to search at the border.

                                             30
       And second, Riley itself does not support the Majority’s approach. Riley made clear

that we should be looking categorically at the type of search—not the suspicion motivating

the search. Riley considered whether the search-incident-to-arrest doctrine, which permits

warrantless and suspicionless searches of an arrestee’s person and immediate surroundings,

should apply to cell-phone searches. In addressing that issue, the Court noted that it had

limited the scope of searches falling within this doctrine. For example, the “extensive

warrantless search of [an arrestee’s] home” cannot be justified as an incident to arrest. 573

U.S. at 383 (citing Chimel v. California, 395 U.S. 752, 763, 768 (1969)). This doctrine

also does not justify the search of a car once the arrestee has been secured or otherwise

brought beyond reach of the vehicle’s passenger compartment. Id. at 374 (citing Arizona

v. Gant, 556 U.S. 332 (2009)). The Riley Court determined that, for similar reasons, the

“particular category of effects” before it (i.e., cell phones) fell outside the search-incident-

to-arrest doctrine. Id. at 386. In doing so, the Court insisted that the availability of the

exception must turn categorically on the type of search. It expressly rejected the prospect

of “case-by-case adjudication” resting on “the probability in a particular arrest situation

that weapons or evidence would in fact be found.” Id. at 384 (quoting United States v.

Robinson, 414 U.S. 218, 235 (1973)).

       The Majority takes the very approach that Riley rejected, making the scope of the

border-search doctrine turn not just on the type of the search as a categorical matter but

also on a case-by-case analysis of the probability of finding contraband or evidence of a

“transnational” crime in the context of a specific search. If the Majority wants to rely on

Riley’s search-incident-to-arrest analysis, it should take the bitter with the sweet.


                                              31
       Thus, even if Riley has relevance for border searches, it teaches us to adopt a simpler

test, one unconcerned with the type of misconduct under investigation. Rather than look

at the type of governmental interest, the Supreme Court has already instructed us to look

at the type of search to determine what, if any, requirements should apply. Montoya de

Hernandez has given us a two-step analysis based on the type of border search: if the

search is routinely intrusive, then no suspicion is required; if the search is highly intrusive

and thus nonroutine, then some particularized suspicion is required. See United States v.

Oriakhi, 57 F.3d 1290, 1297 (4th Cir. 1995) (citing Montoya de Hernandez, 473 U.S. 531,

541 (1985)). 5 Instead of looking to the degree of intrusion, the Majority’s “nexus”

approach focuses on the purpose of the search. This approach fails to faithfully follow

either the Supreme Court’s border-search cases or Riley. I, therefore, respectfully disagree

with the Majority’s decision to hold the search unlawful on that basis.

                                              C.

       Despite my reservations, the Majority has made its “nexus” requirement the law of

this circuit. Having created it, how should it be applied? While apparently leaving the

details to another day, the Majority does require that officers have some basis to believe

that the border search will uncover (1) contraband or (2) evidence of a “transnational”



       5
         Perhaps there should be a third category for the most intrusive searches, like body-
cavity searches, where more than reasonable suspicion is required. But the Supreme Court
has not yet adopted one in its border-search cases (admittedly without ruling one out, see
Montoya de Hernandez, 473 U.S. at 541 n.4). And in evaluating its intrusiveness, a cell-
phone search surely cannot require more than the reasonable suspicion needed to justify
the “long, uncomfortable, indeed, humiliating” detention in Montoya de Hernandez. Id. at
544.

                                              32
crime. Applying that test here, the Majority concludes that the agents’ suspicion at the

time of the search failed to meet this requirement because, while Aigbekaen was suspected

of being an interstate sex trafficker, he was not suspected of being an international sex

trafficker. In my view, the Majority’s application of its “nexus” requirement is too narrow.

       Consider the evidence that the agents had against Aigbekaen when they conducted

the search. On April 12, 2015, a sixteen-year-old girl called 911 from a hotel in Bel Air,

Maryland. J.A. 53. She told police that “Raymond” and another man had taken her from

New York to Maryland and Virginia, where they had sold her to over one hundred men for

sex over the course of a few weeks.          She also explained that the men had used

Backpage.com to advertise her services.           Based on her statement and additional

information (a review of Backpage.com postings and hotel records), police identified both

men. J.A. 67. They learned that “Raymond” meant Aigbekaen, a Nigerian national, who

had paid for the room. J.A. 66. A search of the hotel room revealed used condoms. J.A.

272. Police also spoke to a manager at the hotel, who overheard the two men referring to

a “movie” they were making. J.A. 270. Officers learned that Aigbekaen had left the

country but would be returning to the United States at JFK International Airport. J.A. 107.

They alerted border agents, who stopped Aigbekaen at customs on May 19, 2015, and

searched his electronic devices. J.A. 108.

       As the Majority agrees, officers had probable cause to believe that Aigbekaen was

engaged in interstate sex trafficking of underage girls. Police had the underage victim’s

statement. They also found evidence that Aigbekaen rented a hotel room used for sex with

the girl. And there was evidence that Aigbekaen had used the internet to commit his crimes


                                             33
by posting advertisements on Backpage.com. This meant, of course, that there was

probable cause to believe that searching Aigbekaen’s electronic devices would turn up

relevant evidence. And it would beggar belief to claim that Aigbekaen’s crimes were

purely historical. Police knew that Aigbekaen had recently sold one underage victim to

over one hundred men over a short time. The reasonable inference was that his criminal

activity was professional and ongoing.

       These facts also supported reasonable suspicion that Aigbekaen’s interstate crimes

had an international component. Police knew he was a foreign national who trafficked

underage girls across state lines for profit and that, while engaged in that business, he

traveled abroad. There was at least some reason to suspect that Aigbekaen’s foreign travels

were not purely personal, but professional as well.

       Police also reasonably suspected that Aigbekaen was a foreign national traveling

from abroad into the United States with the intent to continue his criminal activity. Cf.

United States v. Oriakhi, 57 F.3d 1290, 1296 (4th Cir. 1995) (“From the sovereign’s power

to protect itself is derived its power to exclude harmful influences, including undesirable

aliens, from the sovereign’s territory.”).

       And despite the Majority’s suggestion, we may view the facts particular to

Aigbekaen against the background understanding that many sex crimes have a

transnational component. The trafficking of women across international lines is well

documented. So is the phenomenon of international “sex tourism.” These suspicions about

international misconduct may not have risen to the level of probable cause. But they did




                                             34
rise to the level of reasonable suspicion, which is all we should require to find an adequate

“nexus.” 6

       There were also reasonable grounds to suspect that Aigbekaen’s electronic devices

contained child pornography—a type of contraband. Aigbekaen had posted suggestive

photos of the underage victim on Backpage.com. While these photos apparently did not

constitute child pornography, there was reason to suspect that Aigbekaen might also have

more explicit pictures of his victims. (Indeed, given how widely used cell-phone cameras

are, one might reasonably guess that very few sex traffickers of underage girls do not have

child pornography on their phones.) But there was even more direct evidence: the hotel

manager had overheard Aigbekaen and his co-conspirator referring to a “movie” they were

making. Child pornography is contraband, and reasonable suspicion at the border that

someone’s electronic devices possess child pornography should be enough for a forensic

search under any theory.

       The Majority strains to conclude that there was no such reasonable suspicion. But

the Majority simply misapplies the law, in effect applying a standard tantamount to

probable cause (or perhaps something even more demanding). Reasonable suspicion

merely means, under “the totality of the circumstances,” there is “a particularized and

objective basis for suspecting legal wrongdoing.” United States v. Bernard, 927 F.3d 799,

805 (4th Cir. 2019) (quoting United States v. Vaughan, 700 F.3d 705, 710 (4th Cir. 2012)).


       6
        The Majority holds that the government lacked reasonable suspicion, leaving open
what level of suspicion is generally necessary for this type of search. I would require no
more than reasonable suspicion—assuming, of course, that some type of suspicion of a
nexus-related activity should be required in the first place.

                                             35
For example, if police see someone “driving erratically,” they have reasonable suspicion

that he might be “impaired or fatigued”—despite having no direct evidence. Id. In the

classic case, officers had “reasonable suspicion” that a group of men were planning to rob

a convenience store based on a combination of otherwise “innocent” acts, such as standing

around, walking back and forth, talking to each other, and looking at the store repeatedly.

Terry v. Ohio, 392 U.S. 1, 22–23 (1968). Here, there was a particularized and objective

basis for suspecting that Aigbekaen—a foreign national who trafficked underage girls for

sex across state lines, took photos of them, and was overheard discussing a “movie” with

his accomplice—was engaged in illegal conduct during his foreign travels, was entering

the country to keep engaging in ongoing and future criminal schemes, and had explicit

photos of underage girls on his phone.

       In sum, there was reasonable suspicion that Aigbekaen had contraband and that his

interstate crimes also had the “transnational” component the Majority would require. That

should be more than enough.

                                            ***

       The scope of the border-search doctrine raises difficult questions. But in my view,

the Majority’s “nexus” requirement does not faithfully follow the Supreme Court’s case

law. In any event, this requirement is satisfied here, making it a particularly troubling case

to reach beyond good faith to find the search unlawful.




                                             36

```

---

## GROUP: _overhaul2/lake/cases/United States v. Al-Azzawy.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Al-Azzawy
type: case
citation: "784 F.2d 890 (1986)"
parallel_cite: ""
neutral_cite: ""
court: 9th Cir.
court_level: coa
circuit: ca9
year: 1986
date_decided: 1986-03-11
docket: 85-5004
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
  opinion_url: "https://www.courtlistener.com/opinion/465254/united-states-v-riad-abed-al-azzawy/"
  cluster_id: 465254
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Al-Azzawy
  status: under_review
  projected_at: 2026-07-08
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — coerced-emergence pole (arrest location = suspect's position; exit at gunpoint = in-home arrest, 784 F.2d at 893-95)"
  - page: "[[Arrest in the Home]]"
    role: "Related — cross-doctrine (Payton reach)"
---

# United States v. Al-Azzawy

*784 F.2d 890 (9th Cir. 1986)* (No. 85-5004) · U.S. Court of Appeals, 9th Cir. · **Binding in-circuit — 9th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 465254 → 784 F.2d 890, No. 85-5004, decided 1986-03-11 (Beezer, J.). Rule/Application quotes string-matched to the CL opinion text 2026-07-08. Distinct from the earlier 768 F.2d 1141 (1985, No. 84-5367). -->

## Background
Police were summoned to a trailer park after a neighbor reported that Riad Al-Azzawy had threatened to shoot him, to blow up the trailer park, and to burn his trailer, and that Al-Azzawy possessed hand grenades and automatic weapons. Officers "then surrounded appellee's trailer with their guns drawn, and ordered appellee to come outside." When Al-Azzawy appeared he was ordered to his knees, frisked, and questioned; he admitted having firearms inside. The district court suppressed the resulting evidence as the fruit of a warrantless in-home arrest and search; the government appealed.

## Issue
Where officers surround a suspect's dwelling with weapons drawn and order him out over a bullhorn, whether the ensuing arrest occurs "inside" the home for *[[Payton v. New York|Payton]]* purposes even though the suspect physically emerges before being seized.

## Rule
The location of the arrest is fixed by the suspect's position at the moment his freedom is overborne, not by where he happens to be standing when handcuffed. "In the case at bar, the police had completely surrounded appellee's trailer with their weapons drawn and ordered him through a bullhorn to leave the trailer and drop to his knees. Appellee was not free to leave, his freedom of movement was totally restricted, and the officers' show of force and authority was overwhelming." 784 F.2d at 894. ^pin-894

"Moreover, since appellee was in his trailer at the time he was surrounded by armed officers, and since he did not voluntarily expose himself to their view or control outside his trailer but only emerged under circumstances of extreme coercion, the arrest occurred while he was still inside his trailer." *Id.* at 894–95. ^pin-895

## Application
Applying that rule, the court held that "appellee was arrested inside his residence" without a warrant. But the inquiry did not end there: because the reported threats (grenades, automatic weapons, and a threat to blow up the trailer park) established genuine [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], the warrantless in-home arrest was justified, and the district court's suppression order was error. The court therefore **reversed**. ^pin-895b

Al-Azzawy thus establishes *both* poles of the analysis: coerced emergence from a surrounded home is an in-home arrest (the containment/exit-command rule), yet a real, present danger can supply the [[Exigent Circumstances and Hot Pursuit|exigency]] that excuses the warrant.

## Conclusion
Reversed. A suspect who emerges from his surrounded home only under overwhelming coercion is arrested inside it; here, [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] arising from the armed threats justified the warrantless in-home arrest.

## Treatment & subsequent history
- **Status:** ⚪ unverified (frontier stub) — **Binding in-circuit — 9th Cir.** Treatment/progeny not machine-certified until S9 promotion.
- *Al-Azzawy* is the coerced-emergence pole of the Ninth-Circuit surround-and-call-out line. It is the anchor *[[United States v. Nora]]* distinguishes at 894 (Nora had no comparable "agitated and violent state," and the perimeter defeated any flight [[Exigent Circumstances and Hot Pursuit|exigency]]), and the coercion counterpoint to the voluntary-exposure holding of *[[United States v. Vaneaton]]*, 49 F.3d 1423 (9th Cir. 1995).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 465254 + 784 F.2d 890); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Al-Azzawy*, 784 F.2d 890 (9th Cir. 1986)](https://www.courtlistener.com/opinion/465254/united-states-v-riad-abed-al-azzawy/) — pinpoints: 894 (surround/bullhorn = total restraint), 894–95 (coerced emergence = arrest inside the home; exigency justified the warrantless in-home arrest); quotes string-matched to the CL opinion text 2026-07-08.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1f18909e5c314731", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Al-Azzawy"}, "payload": {"all": [{"cite": "784 F.2d 890", "page": "890", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "784"}], "display": "784 F.2d 890", "official": {"cite": "784 F.2d 890", "page": "890", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "784"}, "official_selection_present": true, "record_id": "United States v. Al-Azzawy"}}
{"assertion_id": "d225aecac59ee1eb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Al-Azzawy"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Al-Azzawy", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Al-Azzawy

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Al-Azzawy",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Riad Abed Al-Azzawy",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Riad Abed AL-AZZAWY, Defendant-Appellee",
    "input_case_name": "United States v. Al-Azzawy",
    "court": "9th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca9",
    "state": null,
    "date_decided": "1986-03-11",
    "year": 1986,
    "docket": "85-5004",
    "cluster_id": 465254,
    "lead_opinion_id": 465254,
    "sibling_ids": [],
    "absolute_url": "/opinion/465254/united-states-v-riad-abed-al-azzawy/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "784 F.2d 890",
      "volume": "784",
      "reporter": "F.2d",
      "page": "890",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "784 F.2d 890",
        "volume": "784",
        "reporter": "F.2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "784 F.2d 890",
    "official_selection": {
      "court_class": "coa",
      "selected": "784 F.2d 890",
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
    "date_created": "2026-07-08T16:52:38Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T16:52:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-al-azzawy--465254",
      "to_record_id": "United States v. Al-Azzawy",
      "as_of": "2026-07-08T22:30:00Z",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Al-Azzawy

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b983-15">
  BEEZER, Circuit Judge:
 </author>
<p id="b983-16">
  The government appeals a district court ruling excluding certain evidence on the ground that it resulted from an unlawful warrantless arrest of appellee in his residence and an unlawful warrantless search. We reverse.
 </p>
<p id="b983-17">
  At approximately 9 a.m. on November 19, 1984, Los Angeles police were summoned to investigate a disturbance at a trailer park. Steven Williams told the officers that Riad Abed Al-Azzawy, a neighbor, had threatened to shoot Williams, to blow up the trailer park and to burn Williams’ trailer. Williams also told the officers that Al-Azzawy had threatened him with a pistol the day before, and that a third party had told Williams that he had seen Al-Azzawy in possession of hand grenades and automatic weapons some days earlier.
 </p>
<p id="b983-19">
  Police officers then surrounded appellee’s trailer with their guns drawn, and ordered appellee to come outside. When Al-Azzawy appeared, he was ordered to get on his knees and place his hands on or above his head, which he did. He was then frisked and questioned about the disturbance. Appellee admitted having firearms in his trailer.
 </p>
<p id="b983-20">
  According to the police, appellee and his wife were asked if their trailer could be searched, and both consented. Both denied ever being asked for their consent.
 </p>
<p id="b983-21">
  During the search the police seized sawed-off weapons, an automatic pistol, three hand grenades, gunpowder, a gallon jug full of gasoline with matches glued to it, and other items. Appellee was charged with possession of unregistered firearms and being an illegal alien in possession of a firearm.
 </p>
<p id="b983-22">
  The district court granted appellee’s motion to exclude the unregistered firearms from evidence, holding that appellee was arrested in his home without a warrant or an exception to the warrant requirement. The court also held that appellee verbally consented to the search of his trailer, but that the consent was invalid, both because of the coercive circumstances and because it was tainted by appellee’s prior illegal arrest. The court also ruled that the search was not justified by exigent circumstances. The government appeals.
 </p>
<p id="b983-23">
  On appeal, the government argues that appellee was initially only subjected to a
  <em>
   Terry
  </em>
  stop when he was ordered out of his trailer, and that the later warrantless arrest occurred outside the trailer.
  <em>
   See Terry v. Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span>, 20
  <span citation-index="1" class="star-pagination" label="892"> 
   *892
   </span>
  L.Ed.2d 889 (1968). The district court’s decisions to the contrary are questions of law subject to de novo review.
  <em>
   See United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195</a></span> (9th Cir.) (en banc),
  <em>
   cert. denied,
  </em>
  — U.S.-, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984).
 </p>
<p id="b984-6">
  In
  <em>
   United States v. Morgan,
  </em>
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158</a></span> (6th Cir.1984),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985), the Sixth Circuit decided a case almost identical to the one at bar. While investigating a complaint of target shooting in a public park, a Sheriff was told by an unidentified observer that the suspects had numerous machine guns and other weapons, and that they had threatened to “kill any law that tries to arrest them.” <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1160" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1160</a></span>. The Sheriff broadcast an alert describing the suspects’ car, which was found at the home of defendant Morgan’s mother.
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Id.</a></span>
  </em>
  Nine officers converged on the home, surrounded it, flooded it with spotlights, and summoned Morgan from the house with a bullhorn. <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1161</a></span>. After the suspects left the house, they were arrested, handcuffed and frisked, and the house was searched.
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Id.</a></span>
  </em>
</p>
<p id="b984-9">
  The court held that the suspects had been arrested, saying:
 </p>
<blockquote id="b984-10">
  “These circumstances surely amount to a show of official authority such that ‘a reasonable person would have believed he was not free to leave.’ ”
  <em>
   Florida v. Royer,
  </em>
  460 U.S. [491, 501-03, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1326" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1326-27</a></span>, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span> (1983) ]____ Viewed objectively, Morgan was placed under arrest, without the issuance of a warrant, at the moment the police encircled the Morgan residence.
 </blockquote>
<p id="A-c">
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1164</a></span>.
 </p>
<p id="b984-13">
  Similarly, the court rejected the argument that the actual arrest occurred outside the home because the agents did not cross the threshold:
 </p>
<blockquote id="b984-14">
  We agree with the Ninth Circuit that the important consideration in this type of case “is the location of the arrested person, and not the arresting agent, that determines whether an arrest occurs within a home.”
 </blockquote>
<blockquote id="b984-15">
  Applying this rule here, it is undisputed that Morgan was peacefully residing in his mother’s home until he was aroused by the police activities occurring outside. Morgan was then compelled to leave the house. Thus, as in
  <em>
   Johnson, supra,
  </em>
  “it cannot be said that [Morgan] voluntarily exposed himself to a warrant-less arrest” by appearing at the door. On the contrary, Morgan appeared at the door
  <em>
   only because
  </em>
  o/the coercive police behavior taking place outside of the house____ Viewed in these terms, the arrest of Morgan occurred while he was present inside a private home. Although there was no direct police entry into the Morgan home prior to Morgan’s arrest, the constructive entry accomplished the same thing, namely, the arrest of Morgan. Thus, the warrantless arrest of Morgan, as he stood within the door of a private home, after emerging in response to coercive police conduct, violated Morgan’s fourth amendment rights.
 </blockquote>
<p id="b984-18">
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span> (citations omitted).
 </p>
<p id="b984-19">
  The principles set forth in
  <em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
  </em>
  are consistent with the law of this circuit. In
  <em>
   United States v. Johnson,
  </em>
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d 753</a></span> (9th Cir.1980),
  <em>
   aff'd on other grounds,
  </em>
  <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span>, <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span> (1982), for example, two Secret Service agents approached the door of a suspect’s home, drew their weapons, pointed them downward and knocked, at first identifying themselves by fictitious names. When the suspect opened the door, the agents identified themselves as special agents and asked to talk with the suspect. He told them to come in. This court began its analysis by stating that
 </p>
<blockquote id="AqE">
  whether an arrest has occurred depends upon an objective, not subjective, evaluation of what a person innocent of a crime would have thought of the situation, given all of the factors involved. When an arrest has occurred depends in each case upon an evaluation of all the surrounding circumstances. Primary among these is a determination of whether or not the defendant was free to choose between terminating or continuing the encounter with the law enforcement officers____
  <span citation-index="1" class="star-pagination" label="893"> 
   *893
   </span>
  From a review of all of the circumstances surrounding the encounter between Johnson and the special agents, we find that appellant’s arrest occurred as he stood within his home at the doorway of his home and was first confronted by the agents with their guns drawn____ It is extremely doubtful that Johnson would have believed that he was free to leave at any time or to request the officers to leave after the initial encounter. A reasonable person, under those circumstances, would have thought he was under arrest.
 </blockquote>
<p id="b985-6">
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#755" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 755-56</a></span>.
  <em>
   See also United States v. Patterson,
  </em>
  <span class="citation" data-id="9467917"><a href="/opinion/390276/united-states-v-edward-d-patterson-richard-l-flintoff-jimmie-r/#632" aria-description="Citation for case: United States v. Edward D. Patterson, Richard L....">648 F.2d 625, 632</a></span> (9th Cir.1981) (“Whether an arrest has occurred ‘depends on all of the surrounding circumstances, including the extent that freedom of movement is curtailed and the degree and type of force or authority used to effectuate the stop.’ ... The question is whether, under all of the circumstances, ‘a reasonable person would conclude he was under arrest.’ ”). Regarding the exact location of the arrest, the court stated:
 </p>
<blockquote id="b985-7">
  In this case, we are confronted with the situation where the suspect was arrested as he stood inside his home and the officers stood outside his home with drawn weapons. In these circumstances, it is the location of the arrested person, and not the arresting agents, that determines whether an arrest occurs within a home. Otherwise, arresting officers could avoid illegal “entry” into a home simply by remaining outside the doorway and controlling the movements of suspects within through the use of weapons that greatly extend the “reach” of the arresting officers.
 </blockquote>
<p id="b985-10">
  <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/#757" aria-description="Citation for case: United States v. Raymond Eugene Johnson">626 F.2d at 757</a></span>. The court distinguished cases upholding arrests at open doorways by noting that Johnson had opened his door only after the agents misrepresented their identities and that he invited them inside only after the door was opened and he was subjected to the coercive effect of their brandished weapons.
  <em>
   <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
  </em>
  Since “Johnson’s initial exposure to the view and physical control of the agents [and therefore to warrantless arrest] was not consensual on his part,” this court held that the arrest occurred within a residence.
  <em>
   <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
  </em>
<a class="footnote" href="#fn1" id="fn1_ref">
<em>
    1
   </em>
</a>
</p>
<p id="b985-11">
  In the case at bar, the police had completely surrounded appellee’s trailer with their weapons drawn and ordered him through a bullhorn to leave the trailer and drop to his knees. Appellee was not free to leave, his freedom of movement was totally restricted, and the officers’ show of force and authority was overwhelming. Any reasonable person would have believed he was under arrest in these circumstances. Moreover, since appellee was in his trailer at the time he was surrounded by armed officers, and since he did not voluntarily expose himself to their view or control outside his trailer but only emerged under circumstances of extreme coercion, the arrest occurred while he was still inside his trailer.
  <em>
   United States v. Johnson, supra.
  </em>
</p>
<p id="b985-12">
  We affirm the district court’s ruling that appellee was arrested inside his residence without a warrant.
 </p>
<p id="b985-13">
  Appellee next contends that the arrest was not supported by probable cause
  <span citation-index="1" class="star-pagination" label="894"> 
   *894
   </span>
  because the police acted on the information of only one witness who was not previously known to be reliable, they did not attempt to corroborate the information, and the information about the hand grenades and automatic weapons was hearsay.
 </p>
<blockquote id="b986-4">
  There is probable cause for a warrant-less arrest and a search incident to that arrest if, under the totality of the facts and circumstances known to the arresting officer, a prudent person would have concluded that there was a fair probability that the suspect had committed a crime____
 </blockquote>
<p id="b986-5">
<em>
   United States v. Gonzales,
  </em>
  <span class="citation" data-id="445284"><a href="/opinion/445284/united-states-v-esteban-leon-gonzales/#1337" aria-description="Citation for case: United States v. Esteban Leon Gonzales">749 F.2d 1329, 1337</a></span> (9th Cir.1984).
 </p>
<p id="b986-6">
  In the case at bar, Williams told the police that Al-Azzawy had threatened serious violence both aimed at persons and property and that Al-Azzawy possessed the means to carry out the threats. Regardless of whether the police had probable cause to suspect appellee of possessing illegal explosives or automatic weapons, we hold that they had probable cause to arrest him for assault.
 </p>
<p id="b986-7">
  Probable cause alone will not support a warrantless search or arrest in a residence, however, unless some exception to the warrant requirement is also present.
  <em>
   See Payton,
  </em>
  445 U.S. at 590, 100 S.Ct. at 1382;
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/#758" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d 752, 758</a></span> (9th Cir.1984),
  <em>
   cert. denied,
  </em>
  — U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./105/978/">105 S.Ct. 978</a></span>, <span class="citation" data-id="9045702"><a href="/opinion/9052236/hersom-v-united-states-army/" aria-description="Citation for case: Hersom v. United States Army">83 L.Ed.2d 980</a></span> (1985). The government argues that appellee’s warrantless arrest was justified by the exception of exigent circumstances.
 </p>
<p id="b986-10">
  The Ninth Circuit has defined exigent circumstances as “ ‘those in which a substantial risk of harm to the persons involved or to the law enforcement process would arise if the police were to delay a search [or arrest] until a warrant could be obtained.’ ”
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d at 758</a></span> (quoting
  <em>
   United States v. Robertson,
  </em>
  <span class="citation" data-id="370365"><a href="/opinion/370365/united-states-v-johnny-bob-robertson/#859" aria-description="Citation for case: United States v. Johnny Bob Robertson">606 F.2d 853, 859</a></span> (9th Cir. 1979)). The burden is on the government to show that exigent circumstances existed and made the warrantless arrest imperative.
  <em>
   Vale v. Louisiana,
  </em>
  <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30, 34</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#1972" aria-description="Citation for case: Vale v. Louisiana">90 S.Ct. 1969, 1972</a></span>, <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">26 L.Ed.2d 409</a></span> (1970);
  <em>
   United States v. Salvador,
  </em>
  <span class="citation" data-id="439305"><a href="/opinion/439305/united-states-v-elias-que-salvador-united-states-of-america-v-katrina/#758" aria-description="Citation for case: United States v. Elias Que Salvador, United States of...">740 F.2d at 758</a></span>. We review the district court’s ruling that exigent circumstances did not exist in this case de novo.
  <em>
   Id.; United States v. Hicks,
  </em>
  <span class="citation" data-id="446612"><a href="/opinion/446612/united-states-v-victoria-hicks/#383" aria-description="Citation for case: United States v. Victoria Hicks">752 F.2d 379, 383</a></span> (9th Cir.1985);
  <em>
   United States v. McConney,
  </em>
  <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1204" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d at 1204-05</a></span>; E.R. 220.
 </p>
<p id="b986-12">
  Whether the facts known to the officers in this case were sufficient to give rise to exigent circumstances is a close question. On the one hand, Williams had told the police that appellee’s threat of violence had been expressly conditioned on Williams somehow bothering his family again, all appeared calm around the Al-Azzawy trailer when the police arrived, there was no indication from appellee that he might be presently violent or try to flee, and the information concerning automatic weapons and explosives was entirely hearsay.
 </p>
<p id="b986-13">
  On the other hand, if the officers reasonably believed that appellee possessed illegal explosives and was in an agitated and violent state, there was a sufficiently substantial risk to human life to justify a warrant-less arrest.
  <em>
   But cf. United States v. Morgan,
  </em>
  <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1161-63</a></span> (no exigent circumstances in case involving possible automatic weapons in similar circumstances). The district court concluded that there was no indication that Williams was unreliable and that the officers were therefore entitled to rely on his hearsay statements regarding the grenades without obtaining independent confirmation. Since such reliance seems both reasonable and necessary under the facts of this ease, we hold that exigent circumstances justified appellee’s warrantless arrest.
  <em>
   See, e.g., United States v. Doe,
  </em>
  <span class="citation" data-id="9473606"><a href="/opinion/453431/united-states-v-john-doe-minor-phx/" aria-description="Citation for case: United States v. John Doe (Minor, Phx)">764 F.2d 695</a></span> (9th Cir.1985);
  <em>
   United States v. Alfonso,
  </em>
  <span class="citation" data-id="450644"><a href="/opinion/450644/united-states-v-serafin-alfonso-humberto-rayo-fabian-mora-primo-antonio/" aria-description="Citation for case: United States v. Serafin Alfonso, Humberto Rayo, Fabian...">759 F.2d 728</a></span> (9th Cir.1985).
 </p>
<p id="b986-14">
  The district court also ruled that although the Al-Azzawys had verbally consented to the search, the consent was invalid because it was not voluntary and because it was tainted by the illegal arrest.
  <em>
   See Florida v. Royer,
  </em>
  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U.S. 491</a></span>, 507-OS, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#1329" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319, 1329-30</a></span>, 75 L.Ed.2d
  <span citation-index="1" class="star-pagination" label="895"> 
   *895
   </span>
  229 (1983) (illegal detention taints and invalidates consent search). Since we hold that exigent circumstances made the warrantless arrest legal, we need not discuss the latter issue.
 </p>
<p id="b987-4">
  The government has the burden of demonstrating that consent to a warrant-less search was voluntary.
  <em>
   United States v. Ritter,
  </em>
  <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/#439" aria-description="Citation for case: United States v. Alberto Ritter">752 F.2d 435, 439</a></span> (9th Cir.1985). Voluntariness is a question of fact to be determined from all the surrounding circumstances.
  <em>
   <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/" aria-description="Citation for case: United States v. Alberto Ritter">Id.</a></span>
  </em>
  A trial court’s finding on voluntariness should not be overturned unless it is clearly erroneous.
  <em>
   United States v. Faherty,
  </em>
  <span class="citation" data-id="9469933"><a href="/opinion/410980/united-states-v-caron-faherty/#1260" aria-description="Citation for case: United States v. Caron Faherty">692 F.2d 1258, 1260-61</a></span> (9th Cir.1982).
 </p>
<p id="b987-5">
  Although the Al-Azzawys did not argue that their consent was coerced, there were sufficient facts to support such a conclusion by the district court. The AlAzzawys had been approached by numerous police officers with their guns drawn while Mr. Al-Azzawy remained on his knees with his hands on his head.
  <em>
   See United States v. Mendenhall,
  </em>
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#559" aria-description="Citation for case: United States v. Mendenhall">446 U.S. 544, 559</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. 1870</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">64 L.Ed.2d 497</a></span> (1980) (whether suspect entered the coercive surroundings voluntarily found relevant to the validity of consent);
  <em>
   United States v. Perez,
  </em>
  <span class="citation" data-id="388822"><a href="/opinion/388822/united-states-v-jesus-perez-benjamin-ascencion-marquez-and-salomon-de-la/#1303" aria-description="Citation for case: United States v. Jesus Perez, Benjamin Ascencion Marquez...">644 F.2d 1299, 1303</a></span> (9th Cir.1981) (fact that suspects were approached by customs agents with drawn weapons one factor in finding consent involuntary). The Al-Azzawys were never informed of either their
  <em>
   Miranda
  </em>
  rights or their right to refuse consent to the search.
  <em>
   United States v. Mendenhall,
  </em>
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#558" aria-description="Citation for case: United States v. Mendenhall">446 U.S. at 558-59</a></span>, <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#1879" aria-description="Citation for case: United States v. Mendenhall">100 S.Ct. at 1879-80</a></span> (knowledge of right to refuse consent “highly relevant” to determination that there was consent);
  <em>
   United States v. Ritter,
  </em>
  <span class="citation" data-id="446623"><a href="/opinion/446623/united-states-v-alberto-ritter/#439" aria-description="Citation for case: United States v. Alberto Ritter">752 F.2d 435, 439</a></span> (9th Cir.1985) (absence of
  <em>
   Miranda
  </em>
  warnings is one factor in determining voluntariness of consent). Under these circumstances, we cannot say that the district court was clearly erroneous in finding that the consent was not voluntary.
 </p>
<p id="b987-8">
  The same factors and analysis apply to the presence of exigent circumstances for the warrantless trailer search that apply to the warrantless arrest. Since the police reasonably believed that the trailer contained explosives and that they were not able to arrest all of the persons entitled to enter the trailer (such as appellee’s two small children), we hold that the warrant-less search of the trailer was justified by exigent circumstances.
  <em>
   See United States v. Williams,
  </em>
  <span class="citation" data-id="380508"><a href="/opinion/380508/united-states-v-webster-williams/#703" aria-description="Citation for case: United States v. Webster Williams">626 F.2d 697, 703</a></span> (9th Cir.) (possibility of bomb in car “is an exigent circumstance sufficient to justify an immediate [warrantless] search”),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./449/1020/">449 U.S. 1020</a></span>,<span class="citation multiple-matches"><a href="/c/S.Ct./101/586/">101 S.Ct. 586</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/66/482/">66 L.Ed.2d 482</a></span> (1980).
 </p>
<p id="b987-9">
  We reverse the district court’s decision to exclude evidence on the grounds that the warrantless arrest and search were justified by exigent circumstances.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The case is remanded for further proceedings consistent with this opinion.
 </p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b985-8">
<em>
    .
   </em>
   Appellant argues that
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   (and, by implication,
   <em>
    Johnson)
   </em>
   are both based on erroneous interpretations of
   <em>
    Payton v. New York,
   </em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980). It is true that
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   condemned actual physical police intrusion into the home in order to make an arrest. The
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   court found
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   applicable, however, because it considered surrounding the house and ordering the suspect out to be a "constructive entry,” and because the suspect emerged from the house only because of police coercion. <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1166</a></span>. Similarly, this court in
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   noted the factual difference with
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   but explained that "[w]e doubt the Supreme Court would have reached a different result had the police stood [just outside] the doorway and immediately placed [the suspect] under arrest with weapons drawn” rather than crossing the threshhold to make the arrest. 626 F.2d at 757. Moreover, the court noted that neither the
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   nor the
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   suspects
   <em>
    voluntarily
   </em>
   exposed themselves to the possibility of warrantless arrest.
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Id.</a></span>
   </em>
   Since this court construes
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   in much the same way the Sixth Circuit does, and since the
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   court relied heavily on our
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>
   </em>
   decision, we cannot reject
   <em>
    <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/" aria-description="Citation for case: United States v. John Henry Morgan">Morgan</a></span>
   </em>
   without at least implicitly overruling
   <em>
    <span class="citation" data-id="380517"><a href="/opinion/380517/united-states-v-raymond-eugene-johnson/" aria-description="Citation for case: United States v. Raymond Eugene Johnson">Johnson</a></span>.
   </em>
   We decline to do so.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b987-6">
   . Our decision makes it unnecessary to address the government’s argument that we should create a good-faith exception to the exclusionary rule for police conduct.
  </p>
</div></div></opinion>
```

---
