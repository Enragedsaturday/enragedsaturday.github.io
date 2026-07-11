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

## GROUP: _overhaul2/lake/cases/United States v. Ganias.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Ganias
type: case
citation: "824 F.3d 199 (2016)"
parallel_cite: "117 A.F.T.R.2d (RIA) 1841"
neutral_cite: "2016 U.S. App. LEXIS 9706; 2016 WL 3031285"
court: 2d Cir. en banc
court_level: coa
circuit: ca2
year: 2016
date_decided: 2016-05-27
docket: 12-240-cr
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/3207604/united-states-v-ganias/"
  cluster_id: 3207604
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Ganias
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[United States v. Leon]]"
  - "[[Riley v. California]]"
  - "[[The Exclusionary Rule]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - computer-search
  - over-retention
  - particularity
  - good-faith-exception
  - second-circuit
holding: "Sitting en banc, the Second Circuit affirmed Ganias's tax-evasion conviction on good-faith grounds — the agents' reliance on the 2006 warrant to search forensic mirror images retained from a 2003 search was objectively reasonable under Leon — and therefore expressly declined to decide whether the Government's years-long retention of non-responsive mirrored computer data beyond the 2003 warrant's scope violated the Fourth Amendment, displacing the panel's contrary holding."
---

# United States v. Ganias

*824 F.3d 199 (2d Cir. 2016) (en banc)* (No. 12-240-cr) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 3207604 → en banc majority opinion 3207498 (824 F.3d 199, decided 2016-05-27); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In 2003, Army criminal investigators obtained a warrant to search the office of accountant Stavros Ganias for records of two companies (IPM and American Boiler) suspected of defrauding the Army. Rather than sift the computers on site, agents made complete forensic **mirror images** of three hard drives for off-site review. Those mirrors contained both data responsive to the 2003 warrant and a great deal of **non-responsive** data — including Ganias's own personal and client files. The Government retained the full mirrors as its investigation continued. In 2006, after suspicion turned to Ganias himself, agents obtained a **second warrant** and searched the retained non-responsive data, finding evidence that convicted Ganias of two counts of tax evasion. Ganias argued that once the responsive data had been segregated (by early 2005), continued retention of the non-responsive mirror data violated the Fourth Amendment and tainted the 2006 search.

## Issue
Whether the Government's retention of forensically mirrored computer data that was non-responsive to the 2003 warrant, and its later search of that data under a 2006 warrant, required suppression — or whether the agents' reliance on the 2006 warrant was protected by the [[The Good-Faith Exception|good-faith exception]], making it unnecessary to decide the Fourth Amendment retention question.

## Rule
The [[Reading and Citing Cases#en-banc|en banc]] court resolved the case on the [[The Good-Faith Exception|good-faith exception]] without reaching the constitutional retention question. Because the agents obtained and relied on a 2006 warrant, and that reliance was objectively reasonable, the *[[United States v. Leon|Leon]]* [[The Good-Faith Exception|good-faith exception]] foreclosed suppression regardless of whether the underlying retention was lawful: "We conclude that the Government relied in good faith on the 2006 warrant, and that this reliance was objectively reasonable. Accordingly, we need not decide whether retention of the forensic mirrors violated the Fourth Amendment, and we AFFIRM the judgment of the district court." — 824 F.3d 199, slip op. at 3. ^pin-op3

## Application
The court assumed without deciding that the prolonged retention of non-responsive mirror data might raise a serious Fourth Amendment concern, but held that even if it did, the deterrence rationale of the exclusionary rule had no purchase here: the agents did not act deliberately, recklessly, or with gross negligence. They preserved the mirrors in the good-faith belief that doing so was lawful, sought a fresh judicial warrant in 2006 before searching the retained data, and reasonably relied on that warrant. On that record, suppression was unwarranted under *[[United States v. Leon|Leon]]*, and the constitutional question about digital over-seizure and over-retention could be left for another day.

## Conclusion
**Affirmed.** Judges Livingston and Lynch wrote for the [[Reading and Citing Cases#en-banc|en banc]] majority; Judge Lohier (joined by Judge Pooler) concurred, and Judge Chin dissented. The [[Reading and Citing Cases#en-banc|en banc]] court's good-faith disposition displaced the 2014 panel decision, which had held that the retention of the non-responsive mirror data violated the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Ganias* is the Second Circuit's marquee statement on the **digital over-seizure / over-retention** problem, but it decides the issue only through the *[[United States v. Leon|Leon]]* good-faith exit — the [[Reading and Citing Cases#en-banc|en banc]] court expressly declined to hold whether keeping non-responsive computer-mirror data beyond a warrant's scope is itself a Fourth Amendment violation, leaving the [[Particularity|particularity]]/retention question open in the circuit. Frame it as an unresolved-scope authority, paired with the plain-view anti-exploratory-search principle.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Ganias*, 824 F.3d 199 (2d Cir. 2016) (en banc)](https://www.courtlistener.com/opinion/3207604/united-states-v-ganias/) — pinpoint: slip op. at 3 (good-faith holding + express reservation of the retention question; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fc70671b3cd9b6f9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ganias"}, "payload": {"all": [{"cite": "824 F.3d 199", "page": "199", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "824"}, {"cite": "117 A.F.T.R.2d (RIA) 1841", "page": "1841", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "117"}, {"cite": "2016 U.S. App. LEXIS 9706", "page": "9706", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}, {"cite": "2016 WL 3031285", "page": "3031285", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}], "display": "824 F.3d 199", "official": {"cite": "824 F.3d 199", "page": "199", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "824"}, "official_selection_present": true, "record_id": "United States v. Ganias"}}
{"assertion_id": "7c169273461bdb89", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ganias"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Ganias", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Ganias

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ganias",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Ganias",
    "case_name_short": "Ganias",
    "case_name_full": "UNITED STATES of America, Appellee, v. Stavros M. GANIAS, Defendant-Appellant",
    "input_case_name": "United States v. Ganias",
    "court": "2d Cir. en banc",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2016-05-27",
    "year": 2016,
    "docket": "12-240-cr",
    "cluster_id": 3207604,
    "lead_opinion_id": 9823643,
    "sibling_ids": [],
    "absolute_url": "/opinion/3207604/united-states-v-ganias/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "824 F.3d 199",
      "volume": "824",
      "reporter": "F.3d",
      "page": "199",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 A.F.T.R.2d (RIA) 1841",
        "volume": "117",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1841",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. App. LEXIS 9706",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "9706",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 3031285",
        "volume": "2016",
        "reporter": "WL",
        "page": "3031285",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "824 F.3d 199",
        "volume": "824",
        "reporter": "F.3d",
        "page": "199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 A.F.T.R.2d (RIA) 1841",
        "volume": "117",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1841",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 9706",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "9706",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 3031285",
        "volume": "2016",
        "reporter": "WL",
        "page": "3031285",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "824 F.3d 199",
    "official_selection": {
      "court_class": "coa",
      "selected": "824 F.3d 199",
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
    "date_created": "2026-07-07T01:39:29Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-ganias--3207604",
      "to_record_id": "United States v. Ganias",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Ganias (truncated)

```
<opinion type="majority">
<p id="b224-10">LIVINGSTON and LYNCH, JJ., filed the majority opinion in which KATZMANN, C.J., JACOBS, CABRANES, RAGGI, WESLEY, HALL, CARNEY, and DRONEY, JJ., joined in full, and POOLER and LOHIER, JJ., joined in full as to Parts I and III and in part as to Part II.</p>
<judges id="b224-12">LOHIER, J., filed a concurring opinion in which POOLER, J., joined.</judges>
<judges id="b224-13">CHIN, J., filed a dissenting opinion.</judges>
<author id="b224-14">DEBRA ANN LIVINGSTON and GERARD E. LYNCH, Circuit Judges:</author>
<p id="b224-15">Defendant-Appellant Stavros Ganias appeals from a judgment of the United States District Court for the District of Connecticut (Thompson, <em>J.) </em>convicting him, after a jury trial, of two counts of tax evasion in violation of <span class="citation no-link">26 U.S.C. § 7201</span>. He challenges his conviction on the ground that the Government violated his Fourth Amendment rights when, after lawfully copying three of his hard drives for off-site review pursuant to a 2003 search warrant, it retained these full forensic copies (or “mirrors”), which included data both responsive and non-responsive to the 2003 warrant, while its investigation continued, and ultimately searched the non-responsive data pursuant to a second warrant in 2006. Ganias contends that the Government had successfully sorted the data on the mirrors responsive to the 2003 warrant from the non-responsive data by January 2005, and that the retention of the mirrors thereafter (and, by extension, the 2006 search, which would not have been possible but for that retention) violated the Fourth Amendment. He argues that evidence obtained in executing the 2006 search warrant should therefore have been suppressed.</p>
<p id="b224-16">We conclude that the Government relied in good faith on the 2006 warrant, and that this reliance was objectively reasonable. Accordingly, we need not decide whether retention of the forensic mirrors violated the Fourth Amendment, and we AFFIRM the judgment of the district court.</p>
<p id="b224-17">I</p>
<p id="b224-18">A. Background<footnotemark>1</footnotemark></p>
<p id="b224-19">In August 2003, agents of the U.S. Army Criminal Investigation Division (“Army <page-number citation-index="1" label="201">*201</page-number>CID”) received an anonymous tip that Industrial Property Management (“IPM”), a company providing security for and otherwise maintaining a government-owned property in Stratford, Connecticut, pursuant to an Army contract, had engaged in misconduct in connection with that work. In particular, the informant alleged that IPM, owned by James McCarthy, had billed the Army for work that IPM employees had done for one of McCarthy’s other businesses, American Boiler, Inc. (“AB”), and for construction work performed for IPM’s operations manager at his home residence. The informant told the agents, including Special Agent Michael Conner, that IPM and AB’s financial books were maintained by Stavros Ganias, a former Internal Revenue Service (“IRS”) agent, who conducted business as Taxes International. On the basis of the informant’s information, as well as extensive additional corroboration, Agent Conner prepared an affidavit seeking three warrants to search the offices of IPM, AB, and Taxes International for evidence of criminal activity.<footnotemark>2</footnotemark> Nothing in the record suggests that Ganias himself was suspected of any crimes at that time.</p>
<p id="b225-11">In a warrant dated November 17, 2003, U.S. Magistrate Judge William I. Garfink-el authorized the search of Taxes International. The warrant authorized agents to seize, <em>inter alia, </em>“[a]ll books, records, documents, materials, computer hardware and software and computer associated data relating to the business, financial and accounting operations of [IPM] and [AB].” J.A. 438. It further authorized seizure of “[a]ny of the items described [in the warrant] ... which are stored in the form of magnetic or electronic coding on computer media or on media capable of being read by a computer with the aid of computer-related equipment, including ... fixed hard disks, or removable hard disk cartridges, software or memory in any form.” <em><span class="citation no-link">Id.</span> </em>The warrant also specifically authorized a number of digital search protocols, though it did not state that <em>only </em>these protocols were permitted.<footnotemark>3</footnotemark> The warrant authorized seizure of all hardware relevant to the alleged crimes.<footnotemark>4</footnotemark></p>
<p id="b226-3"><page-number citation-index="1" label="202">*202</page-number>On November 19, 2003, Army CID agents executed the search warrants. Because the warrants authorized the seizure of computer hardware and software, in addition to paper documents, Agent Conner sought the help, in executing the warrants, of agents from the Army CID’s Computer Crimes Investigation Unit (“CCIU”), a unit with specialized expertise in digital forensics and imaging. At Gani-as’s office, the CCIU agents — and in particular Special Agent David Shaver — located three computers. Rather than take the physical hard drives, which would have significantly impaired Ganias’s ability to conduct his business, Agent Shaver created mirror images: exact copies of all of the data stored thereon, down to the bit.<footnotemark>5</footnotemark> Ga-nias was present at his office during the creation of the mirrors, spoke with the agents, and was aware that mirrored copies of his three hard drives had been created and taken off-site.<footnotemark>6</footnotemark> There is no dispute that the forensic mirrors taken from Gani-as’s office contained all of the computerized data maintained by Ganias’s business, including not only material related to IPM or AB, but also Ganias’s own personal <page-number citation-index="1" label="203">*203</page-number>financial records, and the records of “many other” accounting clients of Ganias: businesses of various sorts having no connection to the Government’s criminal investigation.<footnotemark>7</footnotemark> J.A. 464, ¶ 14.</p>
<p id="b227-5">The next day, Agent Shaver consolidated the eleven mirrored hard drives from all three searches (including the three from Ganias’s office) onto a single external hard drive which he provided to Agent Conner. Agent Conner, in turn, provided this hard drive to the evidence custodian of the Army CID, who stored it at Fort Devens, Massachusetts. There the consolidated drive remained, unaltered and untouched, throughout the events relevant to this case. Around the same time, Agent Shaver created two additional copies of the mirrored drives on two sets of nineteen DVDs. After providing these DVD sets to Agent Conner, Agent Shaver then purged the external hard drives onto which he had originally written the mirrors. At this point, a week after the search, three complete copies of the mirrors of Ganias’s hard drives existed: an untouched copy stowe.d away in an evidence locker and two copies available for forensic analysis.<footnotemark>8</footnotemark></p>
<p id="b227-6">Though internal protocols required that specialized digital forensic analysts search the mirrored hard drives, the paper files were not subject to such limitations. Thus, shortly after the November 19 seizure, the Army CID agents began to analyze the non-digital files seized pursuant to' the warrant. These files suggested that IPM had made payments to a third company whose owner, according to the Connecticut Department of Labor, was a full-time employee of an insurance company who received no wages from any source other than that insurance company. This and other red flags spurred Agent Conner to contact the Criminal Investigation Division of the IRS, which subsequently joined the investigation.</p>
<p id="b227-9">In early February 2004, as he and his fellow agents continued to follow leads from the paper files, Agent Conner sent one of the two DVD sets containing the forensic mirrors to the Army Criminal Investigation Laboratory (“ACIL”) in Forest Park, Georgia, accompanied by a copy of one of the three search warrants..In early June, the ACIL assigned Gregory Norman, a digital evidence examiner, to perform a forensic analysis. Around the same time, Special Agent Michelle Chowaniec, who replaced Agent Conner as the primary case agent for the Army CID in late March, provided the second set of DVDs to the IRS agent assigned to the case, Special Agent Paul Holowczyk. Agent Ho-Iowczyk in turn, passed it on, by way of intermediaries, to Special Agent Vita Paukstelis, a computer investigative spe<page-number citation-index="1" label="204">*204</page-number>cialist. By the end of June 2004, computer experts for the Army CID and the IRS— Norman and Agent Paukstelis, respectively — had received copies of the digital evidence (which, as the district court found, were “encoded so that only agents with forensic software not directly available to the case agents could view [them],” <em>Gañí-as, </em><span class="citation no-link">2011 WL 2532396</span>, at *7), and forensic examination began.</p>
<p id="b228-4">Norman commenced his analysis in late June by loading the eleven mirrored drives into EnCase — the same software with which Agent Shaver initially created the mirrors — so that he could search the data thereon. After looking at the search warrants, he created a number of keywords, with which he searched for potentially relevant data. Initially, the search returned far too many results for practicable review (more than 17,000 hits); thus, Norman requested new keywords from Agent Cho-waniec. On the basis of these new keywords, he was able to narrow his search and ultimately identify several files he thought might be of interest to the investigation, all of which he put on a single CD.<footnotemark>9</footnotemark> Some of these files he was able personally to examine, to determine whether they were responsive to the warrant; a few (including the QuickBooks file labeled “Steve_ga.qbw,” which was ultimately searched pursuant to the 2006 warrant, J.A. 467) Norman could not open without a specific software edition of QuickBooks to which he did not have immediate access. However, as these files (like the others) contained keywords that were taken from the narrower list and generated on the basis of the warrant, Norman included the QuickBooks files in the CD he ultimately sent to Agent Chowaniec along with a report.<footnotemark>10</footnotemark> On July 23, 2004, Chowaniec received this CD. Norman, in turn, returned the nineteen DVDs to Army CID’s evidence custodian in Boston for safekeeping.</p>
<p id="b228-7">Norman’s counterpart in the IRS, Agent Paukstelis — who, in addition to receiving the search warrant with her set of DVDs, also received a list of companies, addresses, and key individuals relating to the investigation, along with “a handwritten notation next to the name ‘Taxes International’ that stated ‘(return preparer) do not search,’ ” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *3 — conducted her analysis over a period of about four months. Because she worked for the IRS, she limited her search to the three mirrored drives from Taxes International. Though Agent Paukstelis used ILook, a different software program, to review the mirrored hard drives, she too could not open Quick-Books files without the relevant proprietary software. Still, though she could not open these files, she believed, based on the information to which she had access, that they were within the scope of the warrant; thus, in October 2004, she copied this data, in concert with other responsive data, onto a CD, three copies of which she sent to Agent Holowczyk and Special Agent Amy Hosney, also with the IRS. In light of the note she had received with her DVD set as well as the list of relevant entities, Agent Paukstelis avoided, to the degree she could, searching any files of Taxes International that did not appear to be directly relevant to that list. On November 30, 2004, Paukstelis also provided a “restoration” of the mirrors of the Taxes International hard drives to Special Agent <page-number citation-index="1" label="205">*205</page-number>George Francischelli, an IRS computer specialist assigned to the case.<footnotemark>11</footnotemark></p>
<p id="b229-5">Agents Chowaniec and Conner, after receiving Norman’s CD and report in late July, conducted initial reviews of the data. Like Norman and Agent Paukstelis, however, they could not open the QuickBooks files. At the same time, the agents were busy, in the words of Agent Chowaniec, “tracking down other leads[,] ... [issuing] grand jury subpoenas, ... doing interviews of subcontractors and identifying subcontractors from the papers that [the agents had] received from the search warrants.” J.A. 294-95. In October, Agents Hosney and Chowaniec attempted, together, to review the QuickBooks files, but again lacked the relevant software to do so. Finally, in November 2004, Agent Cho-waniec, having acquired the appropriate software, opened two IPM QuickBooks files on her office computer, and then in December, Agents Hosney and Chowaniec, using the restoration provided by Agent Paukstelis, looked at additional IPM QuickBooks files. Though they had the entirety of the mirrored data before them (the only time throughout the investigation that the case agents had direct access to a software interface permitting them to view essentially all of the data stored on the mirrors), they carefully limited their search: Agent Hosney testified that they “only looked at the QuickBooks files for Industrial Property Management and American Boiler ... [b]eeause those were the only two companies named in the search warrant attachment.” J.A. 340. They did, however, observe that other files existed — both on the CD Norman had provided and on the restoration — in particular, the files Agent Hosney ultimately searched in 2006.</p>
<p id="b229-9">Ganias contends that there is no dispute that by this point, the agents had finished “identifying and segregating the files within the November 2003 warrant’s scope.” Appellant Reply Br. at 5. In actuality, the record is unclear as to whether the forensic examination of the mirrored computers pursuant to the initial search warrant had indeed concluded as a forward-looking matter, rather than from the perspective of hindsight.<footnotemark>12</footnotemark> The district court did not find any facts decisive to this question. It is, further, undisputed that the investigation into McCarthy, IPM, and AB was ongoing at this time, and that this investigation would culminate in an indictment of McCarthy in 2008 secured in large part <page-number citation-index="1" label="206">*206</page-number>through reliance on evidence responsive to the 2003 warrant and located on the mirrored copies of Ganias’s hard drives. <em>See </em>Indictment, <em>United States v. McCarthy, </em>No. 3:08cr224 (EBB) (D. Conn. Oct. 31, 2008), EOF No. 1. When asked why, at this time or any time later, Agent Conner did not return or destroy the data stored on the mirrors that did not appear directly to relate to the crimes alleged in the warrant, Agent Conner explained that “[the] investigation was still ... open” and that, generally, items would be “released back to the owner” once an investigation was closed. J.A. 123. He further noted that the Army CID “would not routinely go into DVDs to delete data, as we’re altering the original data that was seized.” J.A. 122.<footnotemark>13</footnotemark></p>
<p id="b230-7">Over the next year, the agents continued to investigate IPM and AB. Analysis of the paper files taken pursuant to the November 2003 search warrant revealed potential errors in AB’s tax returns that seemed to omit income reflected in checks deposited into IPM’s account. Aware that Ganias had prepared these tax returns and deposited the majority of these checks, Agent Hos-ney came to suspect that Ganias was engaged in tax-related crimes.<footnotemark>14</footnotemark> She did not, however, return to the restoration or otherwise open any of Ganias’s digital financial documents or files associated with <page-number citation-index="1" label="207">*207</page-number>Taxes International.<footnotemark>15</footnotemark> Instead, Agent Hos-ney subpoenaed Ganias’s bank records from 1999 to 2003 and accessed his income tax returns for the same period. On July 28, 2005, the IRS — believing Ganias to be involved both personally and as an accomplice or co-conspirator in tax evasion— officially expanded the investigation to include him.</p>
<p id="b231-5">On February 14, 2006, Ganias, accompanied by his lawyer, met in a proffer session with Agent Hosney and others involved in the investigation.<footnotemark>16</footnotemark> That' day or shortly thereafter, Agent Hosney asked Ganias for consent to access his personal QuickBooks files and those of his business, Taxes International — data Agent Hosney knew to be present on the forensic mirrors but which she had not accessed. When, by April 24, 2006 (two and a half months later), Ganias had failed to respond (either by consenting, objecting, or filing a motion under Federal Rule of Criminal Procedure 41(g) for return of seized property), Agent Hosney sought a search warrant to search the mirrored drives again.<footnotemark>17</footnotemark> In her search warrant affidavit, Agent Hosney pointed to bank records, income tax forms, and additional evidence to demonstrate that she had probable cause to believe that Ganias had violated <span class="citation no-link">26 U.S.C. § 7201</span> (by committing tax evasion) and § 7206(1) (by making false declarations).<footnotemark>18</footnotemark> She further noted that the items to be searched were “mirror images of computers seized on November 19, 2003 from the offices of Taxes International,” J.A. 461, ¶ 7; that information material to the initial investigation had been located on these mirrors and that, “[djuring th[at] investigation,” such information had been “analyzed in detail,” J.A. 464, ¶ 15; that Ganias was not, at the time of the initial seizure, under investigation, J.A. 461, ¶ 3 (“On July 28, 2005, the Government’s investigation was expanded to include an examination of whether Ganias, McCarthy’s accountant and former IRS Revenue ‘Agent, violated the federal tax laws.”); and thus that, though Agent Hos-ney believed that the second mirrored drive, called Taxlnt_2, was “the primary computer for Taxes International,” J.A. 463, ¶ 13, she could not search Ganias’s personal or business files as “[p]ursuant to the 2003 search warrant, only files for [AB] and IPM could be viewed,” J.A. 464, ¶ 14. The magistrate judge issued the warrant, Agent Hosney searched the referenced data, and ultimately the Government indicted Ganias for tax evasion.</p>
<p id="b231-9">B. Procedural History</p>
<p id="b231-10">In February 2010, Ganias moved to suppress the evidence Agent Hosney acquired pursuant to the 2006 warrant. After a two-<page-number citation-index="1" label="208">*208</page-number>day hearing, the district court denied the motion on April 14, 2010, and issued a written decision on June 24, 2011. In that decision, the district court found, <em>inter alia, </em>that the forensic examination of the mirrored drives “was conducted within the limitations imposed by the [2003] warrant” and that “[a] copy of the evidence was preserved in the form in which it was taken.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. Judge Thompson observed that Ganias “never moved for destruction or return of the data, which could have led to the seized pertinent data being preserved by other means.” <em><span class="citation no-link">Id.</span> </em>The district court concluded that the Government’s retention of the mirrored drives' — and thus its subsequent search of those drives pursuant to a warrant — did not violate the Fourth Amendment. Having found no Fourth Amendment violation, the district court did not reach the question of good faith. <span class="citation no-link"><em>Id. </em>at *9</span>.</p>
<p id="b232-4">At trial, the Government introduced information in Ganias’s QuickBooks files as evidence against him, in particular highlighting the fact that payments made to him by clients such as IPM were characterized as “owner’s contributions,” which prevented QuickBooks from recognizing them as income.<footnotemark>19</footnotemark> On the basis of this and other evidence, the jury convicted Ganias of two counts of tax evasion, and the district court sentenced him to two terms of 24 months’ incarceration, to be served concurrently.</p>
<p id="b232-8">Ganias appealed. On review of his conviction, a panel of this Court concluded, unanimously, that the Government had violated the Fourth Amendment; in a divided decision, the panel then ordered suppression of the evidence obtained in executing the 2006 warrant and vacated the jury verdict. We subsequently ordered this rehearing <em>en banc </em>in regards to, first, the existence of a Fourth Amendment violation and, second, the appropriateness of suppression.<footnotemark>20</footnotemark></p>
<p id="b232-9">II</p>
<p id="b232-10">“On appeal from a district court’s ruling on a motion to suppress evidence, ‘we review legal conclusions de novo and findings of fact for clear error.’ ” <em>United States v. Bershchansky, </em><span class="citation" data-id="8413470"><a href="/opinion/8442239/united-states-v-bershchansky/#108" aria-description="Citation for case: United States v. Bershchansky">788 F.3d 102, 108</a></span> (2d Cir. 2015) (quoting <em>United States v. Freeman, 735 </em>F.3d 92, 95 (2d Cir. 2013)). We may uphold the validity of a judgment “on any ground that finds support in the record.” <em>Headley v. Tilghman, </em><span class="citation" data-id="695149"><a href="/opinion/695149/andrew-headley-v-lawrence-tilghman-warden-connecticut-correction/#476" aria-description="Citation for case: Andrew Headley v. Lawrence Tilghman, Warden, Connecticut...">53 F.3d 472, 476</a></span> (2d Cir. 1995).</p>
<p id="b232-11">The district court concluded that the conduct of the agents in this case comported fully with the Fourth Amendment, and <page-number citation-index="1" label="209">*209</page-number>thus did not reach the question whether they also acted in good faith. Because we conclude that the agents acted in good faith, we need not decide whether a Fourth Amendment violation occurred. We thus affirm the district court on an alternate ground. Nevertheless, though we offer no opinion on the existence of a Fourth Amendment violation in this case, we make some observations bearing on the reasonableness of the agents’ actions, both to illustrate the complexity of the questions in this significant Fourth Amendment context and to highlight the importance of careful consideration of the technological contours of digital search and seizure for future cases.</p>
<p id="b233-6">“The touchstone of the Fourth Amendment is reasonableness.... ” <em>United States v. Miller, </em><span class="citation" data-id="792539"><a href="/opinion/792539/united-states-v-alfred-g-miller/#97" aria-description="Citation for case: United States v. Alfred G. Miller">430 F.3d 93, 97</a></span> (2d Cir. 2005) (alteration omitted) (quoting <em>United States v. Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#118" aria-description="Citation for case: United States v. Knights">534 U.S. 112, 118</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S.Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L.Ed.2d 497</a></span> (2001)). As relevant here, “searches pursuant to a warrant will rarely require any deep inquiry into reasonableness.” <em>United States v. Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. 897, 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span> (1984) (alteration omitted) (quoting <em>Illinois v. Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#267" aria-description="Citation for case: Illinois v. Gates">462 U.S. 213, 267</a></span>, <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">103 S.Ct. 2317</a></span>, <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">76 L.Ed.2d 527</a></span> (1983) (White, J., concurring in judgment)). Nevertheless, both the scope of a seizure permitted by a warrant,<footnotemark>21</footnotemark> and the reasonableness of government conduct in executing a valid warrant,<footnotemark>22</footnotemark> can present Fourth <page-number citation-index="1" label="210">*210</page-number>Amendment issues. Ganias thus argues that the Government violated the Fourth Amendment in this case, notwithstanding the two warrants that issued, by retaining complete forensic copies of his three hard drives during the pendency of its investigation.</p>
<p id="b234-4">According to Ganias, when law enforcement officers execute a warrant for a hard drive or forensic mirror that contains data that, as here, cannot feasibly be sorted into responsive and non-responsive categories on-site, “the Fourth Amendment demands, at the very least, that the officers expeditiously complete their off-site search and then promptly return (or destroy) files outside the warrant’s scope.”<footnotemark>23</footnotemark> Appellant Br. at 18. Arguing that a culling process took place here and that it had concluded by, at the latest, January 2005, Ganias faults the Government for retaining the mirrored drives — including storing one forensic copy in an evidence locker for safekeeping.<footnotemark>24</footnotemark> It was this retention, he argues, that constituted the Fourth Amendment violation — a violation that, in turn, made the 2006 search of the data itself unconstitutional as, but for this retention, the search could never have occurred.</p>
<p id="b234-10">To support this argument, Ganias relies principally on <em>United States v. Tamura, </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d 591</a></span> (9th Cir. 1982), a Ninth Circuit case involving the search and seizure of physical records. In <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(unlike the present case, in which a warrant specifically authorized the agents to seize hard drives and to search them off-site) officers armed only with a warrant authorizing them to seize specific “records” instead seized numerous boxes of printouts, file <page-number citation-index="1" label="211">*211</page-number>drawers, and cancelled checks for off-site search and sorting. <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#594" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 594-95</a></span>. After the officers had clearly sorted the responsive paper documents from the non-responsive ones, they refused — despite request — to return the non-responsive paper files. <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#596" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 596-97</a></span>. The Ninth Circuit concluded that both the unauthorized seizure of voluminous material not specified in the warrant and the retention of the seized documents violated the Fourth Amendment.<footnotemark>25</footnotemark> <span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#595" aria-description="Citation for case: United States v. Leigh Raymond Tamura"><em>Id. </em>at 595, 597</a></span>; <em>see also Andresen v. Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">427 U.S. 463</a></span>, 482 n. 11, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">96 S.Ct. 2737</a></span>, <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/" aria-description="Citation for case: Andresen v. Maryland">49 L.Ed.2d 627</a></span> (1976) (“[W]e observe that to the extent [seized] papers were not within the scope of the warrants or were otherwise improperly seized, the State was correct in returning them voluntarily and the trial judge was correct in suppressing others.... In searches for papers, it is certain that some innocuous documents will be examined, at least cursorily, in order to determine whether they are, in fact, among those papers authorized to be seized.... [Responsible officials [conducting such searches], including judicial officials, must take care to assure that they are conducted in a manner that minimizes unwarranted intrusions upon privacy.”); <em>cf. United States v. Matias, </em><span class="citation" data-id="499737"><a href="/opinion/499737/united-states-v-miguel-matias-sr-jose-caraballo-miguel-matias-jr/#747" aria-description="Citation for case: United States v. Miguel Matias, Sr., Jose Caraballo,...">836 F.2d 744, 747</a></span> (2d Cir. 1988) (“[W]hen items outside the scope of a valid warrant are seized, the normal remedy is suppression and return of those items.... ”).</p>
<p id="b235-5">Because we resolve this case on good faith grounds, we need not decide the relevance, if any, of <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(or, more broadly, the validity of Ganias’s Fourth Amendment claim). We note, however, that there are reasons to doubt whether <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>(to the extent we would indeed follow it) answers the questions before us. First, on its facts, <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>is distinguishable from this case, insofar as the officers there seized for off-site review records that the warrant did not authorize them to seize,<footnotemark>26</footnotemark> and retained those records even after their return was requested. Here, in contrast, the warrant authorized the seizure of the hard drives, not merely particular records, and Ganias did not request return or destruction of the mirrors (even after he was indisputably alerted to the Government’s continued retention of them) by, for instance, filing a motion for such return pursuant to Federal Rule of Criminal Procedure 41(g). Second, and more broadly, even if the facts of <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>were otherwise on point, Ganias’s invocation of <em>Ta-mura’s </em>reasoning rests on an analogy between paper files intermingled in a file cabinet and digital data on a hard drive. Though we do not take any position on the ultimate disposition of the constitutional questions herein, we nevertheless pause to address the appropriateness of this analogy, which is often invoked '(including by the dissent) and bears examination.</p>
<p id="b235-9">The central premise of Ganias’s reliance on <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>is that the search of a digital storage medium is analogous to the search of a file cabinet. The analogy has some force, particularly as seen from the perspective of the affected computer user. Computer users — or at least, average users (in contrast to, say, digital forensics experts) — typically experience computers as filing cabinets, as that is precisely how <page-number citation-index="1" label="212">*212</page-number>user interfaces are designed to be perceived by such users.<footnotemark>27</footnotemark> Given that the file cabinet analogy (at least largely) thus captures an average person’s subjective experience with a computer interface, the analogy may shed light on a user’s subjective expectations of privacy regarding data maintained on a digital storage device. Because we experience' digital files as discrete items, and because we navigate through a computer as through a virtual storage space, we may expect the law similarly to treat data on a storage device as comprised of distinct, severable files, even if, in fact, “[sjtorage media do not naturally divide into parts.” Josh Goldfoot, <em>The Physical Computer and the Fourth Amendment, </em>16 Berkeley J. Crim. L. 112, 131 (2011). In this case, for example, a person in Ganias’s situation could well understand the “files” on his hard drives containing information relating to IPM and AB as separate from the “files” containing his personal financial information and that of other clients. Indeed, the very fact that the Government sought additional search authorization via the 2006 warrant when it established probable cause to search Gani-as’s personal files indicates that the Government too understood — and credited— this distinction.</p>
<p id="b236-7">That said, though it may have some relevance to our inquiry, the file cabinet analogy is only that — an analogy, and an imperfect one. <em>Cf. </em>James Boyle, <em>The Public Domain </em>107 (2008) (“Analogies are only bad when they ignore the key difference between the two things being analyzed.”). Though to a user a hard drive may seem like a file cabinet, a digital forensics expert reasonably perceives the hard drive simply as a coherent physical storage medium for digital data^ — data that is interspersed <em>throughout </em>the medium, which itself must be maintained and accessed with care, lest this data be altered or destroyed.<footnotemark>28</footnotemark> <em>See </em><page-number citation-index="1" label="213">*213</page-number>Goldfoot, <em>supra, </em>at 114 (arguing digital storage media are physical objects like “drugs, blood, or clothing”); Wayne Jekot, <em>Computer Forensics, Search Strategies, and the Particularity Requirement, </em>7 U. Pitt. J. Tech. L. &amp; Pol'y, art. 5, at 1, 30 (2007) (“[A] computer does not simply hold data, it is <em>composed </em>of data.”). Even the most conventional “files” — word documents and spreadsheets such as those the Government searched in this case — are not maintained, like files in a file cabinet, in discrete physical locations separate and distinct from other files. They are in fact “fragmented” on a storage device, potentially across physical locations. Jekot, <em>supra, </em>at 13. “Because of the manner in which data is written to the hard drive, rarely will one file be stored intact in one place on a hard drive,” <em>id.; </em>so-called “files” are stored in multiple locations and in multiple forms, <em>see </em>Goldfoot, <em>supra, </em>at 127-28.<footnotemark>29</footnotemark> And as a corollary to this fragmentation, the computer stores unseen information about any given “file”' — not only meta-data about when the file was created or who created it, <em>see </em>Michael W. Graves, <em>Digital Archaeology: The Art and Science of Digital Forensics </em>94-95 (2014), but also prior versions or edits that may still exist “in the document or associated temporary files on [the] disk” — further interspersing the data corresponding to that “file” across the physical storage medium, Eoghan Casey, <em>Digital Evidence and Computer Crime </em>507 (3d ed. 2011).</p>
<p id="b237-7">“Files,” in short, are not as discrete as they may appear to a user. Their interspersion throughout a digital storage medium, moreover, may affect the degree to which it is feasible, in a case involving search pursuant to a warrant, to fully extract and segregate responsive data from non-responsive data. To be clear, we do not suggest that it is impossible to do so in any particular or in every case; we emphasize only that in assessing the reasonableness, for Fourth Amendment purposes, of the search and seizure of digital evidence, we must be. attuned to the technological features unique to digital media as a whole and to those relevant in a particular case— features that simply do not exist in the context of paper files.</p>
<p id="b237-8">These features include an additional complication affecting the validity of the file cabinet analogy: namely, that a good deal of the information that a forensic examiner may seek on a digital storage device (again, because it is a coherent and complex forensic object and not a file cabinet) does not even remotely fit into the typical user’s conception of a “file.” <em>See </em>Daniel B. Garrie <em>&amp; </em>Francis M. Allegra, Fed. Judicial Ctr., <em>Understanding Software, the Internet, Mobile Computing, and the Cloud: A Guide for Judges </em>39 (2015) (“Forensic software gives a forensic examiner access to electronically stored information (ESI) that is otherwise unavailable to a typical computer user.”). Forensic investigators may, <em>inter alia, </em>search for and discover evidence that a file was <page-number citation-index="1" label="214">*214</page-number>deleted as well as evidence sufficient to reconstruct a deleted file — evidence that can exist in so-called “unallocated” space on a hard drive. <em>See </em>Casey, <em>supra, </em>at 496; Orin S. Kerr, <em>Searches and Seizures in a Digital World, </em><span class="citation no-link">119 Harv. L. Rev. 531</span>, 542, 545 (2005); Fed. Judicial Ctr., <em>supra, </em>at 40 (“A host of information can lie in the interstices between the allocated spaces.”). They may seek responsive metadata about a user’s activities, or the manner in which information has been stored, to show such things as knowledge or intent, or to create timelines as to when information was created or accessed.<footnotemark>30</footnotemark> Forensic examiners will sometimes seek evidence on a storage medium that something <em>did not happen: </em>“If a defendant claims he is innocent because a computer virus committed the crime, the absence of a virus on his hard drive is ‘dog that did not bark’ negative evidence that disproves his story.... To prove something is not on a hard drive, it is necessary to look at every place on the drive where it might be found and confirm it is not there.”<footnotemark>31</footnotemark> Goldfoot, <em>supra, </em>at 141; <em>see also United States v. O’Keefe, </em><span class="citation" data-id="77425"><a href="/opinion/77425/united-states-v-michael-aaron-okeefe/#1341" aria-description="Citation for case: United States v. Michael Aaron O&#x27;Keefe">461 F.3d 1338, 1341</a></span> (11th Cir. 2006) (“[The government’s expert] testified that the two viruses he found on [the defendant’s] computer were not capable of ‘downloading and uploading child pornography and sending out advertisements.’ ”).<footnotemark>32</footnotemark></p>
<p id="b239-4"><page-number citation-index="1" label="215">*215</page-number>Finally, because of the complexity of the data thereon and the manner in which it is stored, the nature of digital storage presents potential challenges to parties seeking to preserve digital evidence, authenticate it at trial, and establish its integrity for a fact-finder — challenges that materially differ from those in the paper file context. First, the extraction of specific data files to some other medium can alter, omit, or even destroy portions of the information contained in the original storage medium. Preservation of the original medium or a complete mirror may therefore be necessary in order to safeguard the integrity of evidence that has been lawfully obtained or to authenticate it at trial. Graves, <em>supra, </em>at 95-96 (“[The investigator] must be able to prove that the information presented came from where he or she claims and was not altered in any way during examination, and that there was no opportunity for it to have been replaced or altered in the interim.”); <em>see also </em>Casey, <em>supra, </em>at 480 (“Even after copying data from a computer or piece of storage media, digital investigators generally retain the original evidential item in a secure location for future reference.”).<footnotemark>33</footnotemark> The preservation of data, moreover, is not simply a concern for law enforcement. Retention of the original storage medium or its mirror may also be necessary to afford criminal defendants access to that medium or its forensic copy so that, relying on forensic experts of their own, they may challenge the authenticity or reliability of evidence allegedly retrieved. <em>See, e.g., United States v. Kimoto, </em><span class="citation" data-id="1311543"><a href="/opinion/1311543/united-states-v-kimoto/#480" aria-description="Citation for case: United States v. Kimoto">588 F.3d 464, 480</a></span> (7th Cir. 2009) (quoting the defendant’s motion as stating: “Upon beginning their work, [digital analysis experts] advised [the defendant’s] Counsel that the discovery provided to the defense did not appear to be a complete forensic copy, and that such was necessary to verify the data as accurate and unaltered.”).<footnotemark>34</footnotemark> Defendants may also require access to a forensic copy to conduct an independent analysis of precisely what the government’s forensic expert did — potentially altering evidence in a manner material to the case — or to locate exculpatory evidence that the government missed.<footnotemark>35</footnotemark></p>
<p id="b240-3"><page-number citation-index="1" label="216">*216</page-number>Notwithstanding any other distinctions between this ease and <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span>, </em>then, the Government plausibly argues that, because digital storage media constitute coherent forensic objects with contours more complex than — and materially distinct from— file cabinets containing interspersed paper documents, a digital storage medium or its forensic copy may need to be retained, during the course of an investigation and prosecution, to permit the accurate extraction of the primary evidentiary material sought pursuant to the warrant; to secure metadata and other probative evidence stored in the interstices of the storage medium; and to preserve, authenticate, and effectively present at trial the evidence thus lawfully obtained. To be clear, we do not decide the ultimate merit of this argument as applied to the circumstances of this case.<footnotemark>36</footnotemark> Nor do we gainsay the <page-number citation-index="1" label="217">*217</page-number>privacy concerns implicated when the government retains a hard drive or forensic mirror containing personal information irrelevant to the ongoing investigation, even if such information is never viewed. We discuss the aptness and limitations of Gani-as’s analogy and the Government’s response simply to highlight the complexity of the relevant questions for future cases and to underscore the importance, in answering such questions, of engaging with the technological specifics.<footnotemark>37</footnotemark></p>
<p id="b241-5">In emphasizing such specifics, we reiterate that we do not mean to thereby minimize or ignore the privacy concerns implicated when a hard drive or forensic mirror is retained, even pursuant to a warrant. The seizure of a computer hard drive, and its subsequent retention by the government, can give the government possession of a vast trove of personal information about the person to whom the drive belongs, much of which may be entirely irrelevant to the criminal investigation that led to the seizure. Indeed, another weakness of the file cabinet analogy is that no file cabinet has the capacity to contain as much information as the typical computer hard drive. In 2005, Professor Orin Kerr noted that the typical personal computer hard drive had a storage capacity of about eighty gigabytes, which he estimated could hold text files equivalent to the “information contained in the books on one floor of a typical academic library.” Kerr, <em>Searches and Seizures in a Digital World, supra, </em>at <page-number citation-index="1" label="218">*218</page-number>542. By 2011, computers were being sold with one terabyte of capacity — about twelve times the size of Professor Kerr’s library floor. Paul Ohm, Response, <em>Massive Hard Drives, General Warrants, and the Power of Magistrate Judges, </em>97 Va. L. Rev. In Brief 1, 6 (2011). The <em>New York Times </em>recently reported that commercially available storage devices can hold “16 pe-tabytes of data, roughly equal to 16 billion thick’books.” Quentin Hardy, As <em>a Data Deluge Grows, Companies Rethink Storage, </em>N.Y. Times, Mar. 15, 2016, at B3.</p>
<p id="b242-4">Moreover, quantitative measures fail to capture the significance of the data kept by many individuals on their computers. Tax records, diaries, personal photographs, electronic books, electronic media, medical data, records of internet searches, banking and shopping information — all may be kept in the same device, interspersed among the evidentiary material that justifies the seizure or search. <em>Cf. Riley v. California, </em>— U.S. -, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/#2489" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473, 2489-90</a></span>, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span> (2014) (explaining that even microcomputers, such as cellphones, have “immense storage capacity” that may contain “every piece of mail [people] have received for the past several months, every picture they have taken, or every book or article they have read,” which can allow the “sum of an individual’s private life [to] be reconstructed”); <em>United States v. Galpin, </em><span class="citation" data-id="931473"><a href="/opinion/931473/united-states-v-galpin/#446" aria-description="Citation for case: United States v. Galpin">720 F.3d 436, 446</a></span> (2d Cir. 2013) (“[Advances in technology and the centrality of computers in the lives of average people have rendered the computer hard drive akin to a residence in terms of the scope and quantity of private information it may contain.”). While physical searches for paper records or other evidence may require agents to rummage at least cursorily through much private material, the reasonableness of seizure and subsequent retention by the government of such vast quantities of irrelevant private material was rarely if ever presented in cases prior to the age of digital storage, and has never before been considered justified, or even practicable, in such cases. Even as we recognize that search and seizure of digital media is, in some ways, distinct from what has come before, we must remain mindful of the privacy interests that necessarily inform our analysis.<footnotemark>38</footnotemark></p>
<p id="b242-9">We note, however, that parties with an interest in retained storage media are not without recourse. As noted above, Ganias never sought the return of any seized material, either by negotiating 'with the Government or by motion to the court. Though negotiated stipulations regarding the admissibility or integrity of evidence may not always suffice to satisfy reasonable interests of the government in retention during the pendency of an investigation,<footnotemark>39</footnotemark> such <page-number citation-index="1" label="219">*219</page-number>stipulations may make return feasible in a proper case, and can be explored.</p>
<p id="b243-5">A person from whom property is seized by law enforcement may move for its return under Federal Rule of Criminal Procedure 41(g).<footnotemark>40</footnotemark> Rule 41(g) permits a defendant or any “person aggrieved” by either an unlawful or <em>lawful </em>deprivation of property, <em>see United States v. Comprehensive Drug Testing, Inc., </em><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/#1173" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">621 F.3d 1162, 1173</a></span> (9th Cir. 2010) (en banc) (per curiam), to move for its return, Fed. R. Crim. P. 41(g). Evaluating such a motion, a district court “must receive evidence on any factual issue necessary to decide the motion,” and, in the event that the motion is granted, may “impose reasonable conditions to protect access to the property and its use in later proceedings.” <em><span class="citation" data-id="9438359"><a href="/opinion/175207/united-states-v-comprehensive-drug-testing-inc/" aria-description="Citation for case: United States v. Comprehensive Drug Testing, Inc.">Id.</a></span> </em>Since we resolve this case on other grounds, we need not address whether Ganias’s failure to make such a motion forfeited any Fourth Amendment objection he might otherwise have had to the Government’s retention of the mirrors. But we agree with the district court that, as a pragmatic matter, such a motion “would have given a court the opportunity to consider ‘whether the government’s interest could be served by an alternative to retaining the property,’ and perhaps to order the [mirrors] returned to Ganias, all while enabling the court to ‘impose reasonable conditions to protect access to the property and its use in later proceedings.’ ” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8 (citation omitted) (first quoting <em>In re Smith, 888 </em>F.2d 167, 168 (D.C. Cir. 1989) (per curiam); then quoting Fed. R. Crim. P. 41(g)).</p>
<p id="b243-11">Rule 41(g) thus provides a potential mechanism, in at least some contexts, for dealing with the question of retention at a time when the government may be expected to have greater information about the data it seeks and the best process through which to search and present that data in court. It is worth observing, then, that Rule 41(g) constitutes a statutory solution (as opposed to a purely judicially constructed one) to at least one facet of the retention problem.<footnotemark>41</footnotemark> Statutory approaches, of course, do not relieve courts from their obligation to interpret the Constitution; nevertheless, such approaches have, historically, provided one mechanism for safeguarding privacy interests while, at the same time, addressing the needs of law enforcement in the face of technological change. Indeed, when Congress addressed wiretapping in the Omnibus Crime Control <page-number citation-index="1" label="220">*220</page-number>and Safe Streets Act of 1968, the Senate Judiciary Committee issued a report reflecting precisely this ambition — to provide a framework through which law enforcement might comport with the demands of the Constitution and meet important law enforcement interests. <em>See </em>S. Rep. No. 90-1097, at 66-76 (1968) (describing the construction of the then-Omnibus Crime Control and Safe Streets of Act of 1967, which laid out comprehensive rules for when and how law enforcement could intercept wire and oral communications through electronic surveillance, as a Congressional attempt to respond to and synthesize, first, technological change, <em>id. </em>at 67, second, ineffective or unclear state statutory regimes, <em>id. </em>at 69, third, evolving Supreme Court precedent, <em>id. </em>at 74-75, and fourth, law enforcement concerns, <em>id. </em>at 70); <em>see also id. </em>at 66 (“Title III has as its dual purpose (1) protecting the privacy of wire and oral communications, and (2) delineating on a uniform basis the circumstances and conditions under which the interception of wire and oral communications may be author-izecl.”). The Act did not seek to supplant the role of the courts, nor could it have done so, but it did demonstrate the intuitive proposition that Congress can and should be a partner in the process of fleshing out the contours of law-enforcement policy in a shifting technological landscape. In acknowledging the role of Rule 41(g), then, we seek also to suggest that search and seizure of electronic media may, no less than wiretapping, merit not only judicial review but also legislative analysis; courts need not act alone.</p>
<p id="b244-6">As we have said, we need not resolve the ultimate question whether the Government’s retention of forensic copies of Gani-as’s hard drives during the pendency of its investigation violated the Fourth Amendment. We conclude, moreover, that we should not decide this question on the present record, which does not permit a full assessment of the complex and rapidly evolving technological issues, and the significant privacy concerns, relevant to its consideration.<footnotemark>42</footnotemark> Having noted Ganias’s ar<page-number citation-index="1" label="221">*221</page-number>gument, we do not decide its merits. We instead turn to the question of good faith.</p>
<p id="b245-4">Ill</p>
<p id="b245-5">The Government argues that, because it acted in good faith throughout the pen-dency of this case, any potential violation of the Fourth Amendment does not justify the extraordinary remedy of suppression. <em>See Davis v. United States, </em><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/#237" aria-description="Citation for case: Davis v. United States">564 U.S. 229, 237</a></span>, <span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span>, <span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span> (2011) (noting the “heavy toll” exacted by suppression, which “requires courts to ignore reliable, trustworthy evidence,” and characterizing suppression as a “bitter pill,” to be taken “only as a ‘last resort’ ” (quoting <em>Hudson v. Michigan, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan">547 U.S. 586, 591</a></span>, <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span>, <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">165 L.Ed.2d 56</a></span> (2006))); <em>accord United States v. Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#99" aria-description="Citation for case: United States v. Clark">638 F.3d 89, 99</a></span> (2d Cir. 2011). In particular, the Government urges that its “reliance on the 2006 warrant,” which it obtained after disclosing to the magistrate judge all relevant facts regarding its retention of the mirrored files, “fits squarely within the traditional <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>exception for conduct taken in reliance on a search warrant issued by a neutral and detached magistrate judge.”<footnotemark>43</footnotemark> Government Br. at 59; <em>see Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>. For the following reasons, we agree.</p>
<p id="b245-8">In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Supreme Court determined that the exclusion of evidence is inappropriate when the government acts “in objectively reasonable reliance” on a search warrant, even when the warrant is subsequently invalidated. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>; <em>see also Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#100" aria-description="Citation for case: United States v. Clark">638 F.3d at 100</a></span> (“[I]n <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Supreme Court strongly signaled that most searches conducted pursuant to a warrant would likely fall within its protection.”). Such reliance, however, must be <em>objectively reasonable. See Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922-23</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span> (“[I]t is clear that in some circumstances the officer will have no reasonable grounds for believing that the warrant was properly issued.” (footnote omitted)). Thus, to assert good faith reliance successfully, officers must, <em>inter alia, </em>disclose all potentially adverse information to the issuing judge. <em>See United States v. Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d 1271, 1280</a></span> (2d Cir.) (“The good faith exception to the exclusionary rule does not protect searches by officers who fail to provide all potentially adverse information to the issuing judge.... ”), <em>aff'd and amended, </em><span class="citation multiple-matches"><a href="/c/F.3d/91/331/">91 F.3d 331</a></span> (2d Cir. 1996) (per curiam); <em>see also United States v. Thomas, </em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas">757 F.2d 1359, 1368</a></span> (2d Cir. 1985) (finding good faith reliance on a warrant, under <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>where officers, first, committed a constitutional violation they did not <page-number citation-index="1" label="222">*222</page-number>reasonably know, at the time, was unconstitutional — a warrantless canine sniff— and second, in relying on evidence from this sniff in a warrant application, fully revealed the fact of the canine sniff to a magistrate judge), <em>cert. denied by Fisher v. United States, </em><span class="citation" data-id="9049107"><a href="/opinion/9055582/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">474 U.S. 819</a></span>, <span class="citation" data-id="9049105"><a href="/opinion/9055580/coronel-quintana-v-united-states/" aria-description="Citation for case: Coronel-Quintana v. United States">106 S.Ct. 66</a></span>, <span class="citation" data-id="9049110"><a href="/opinion/9055585/mcmahon-v-green/" aria-description="Citation for case: McMahon v. Green">88 L.Ed.2d 54</a></span> (1985) <em>and Rice v. United States, </em><span class="citation" data-id="9057476"><a href="/opinion/9063854/rice-v-united-states/" aria-description="Citation for case: Rice v. United States">479 U.S. 818</a></span>, <span class="citation" data-id="9057476"><a href="/opinion/9063854/rice-v-united-states/" aria-description="Citation for case: Rice v. United States">107 S.Ct. 78</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/93/34/">93 L.Ed.2d 34</a></span> (1986).</p>
<p id="b246-4">Ganias argues that reliance on the 2006 warrant is misplaced for two reasons. First, he urges that the alleged constitutional violation here (unlawful retention of the mirrored drives) had “long since” ripened into a violation by April 2006, when the second warrant was obtained, Appellant Br. at 55-56, and attests that “[n]oth-ing [in Leon] suggests that the police, <em>after </em>they engage in misconduct, can then ‘launder their prior unconstitutional behavior by presenting the fruits of it to a magistrate,’ ” <em>id. </em>at 56 (quoting <em>State v. Hicks, </em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/" aria-description="Citation for case: State v. Hicks">146 Ariz. 533</a></span>, <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#333" aria-description="Citation for case: State v. Hicks">707 P.2d 331, 333</a></span> (Ariz. Ct. App. 1985)). Second, Ganias argues that, even if “a subsequent warrant can ever appropriately purge the taint of an earlier violation, the agent must, at the very least, ‘provide all potentially adverse information’ regarding the earlier illegality ‘to the issuing [magistrate] judge,’” a requirement that he argues was not satisfied here. <em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/" aria-description="Citation for case: State v. Hicks">Id.</a></span> </em>at 58 (quoting <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span>). Ganias’s arguments are unavailing.</p>
<p id="b246-5">First, Ganias relies on this Court’s decision in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>to argue categorically that agents who have engaged in a predicate Fourth Amendment violation may not rely on a subsequently issued warrant to establish good faith. <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>however, stands for no such thing. In <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>officers unlawfully intruded on the defendant’s curtilage, discovering about twenty marijuana plants, before they departed and obtained a search warrant based on a “bare-bones” description of their intrusion and resulting observations which this Court found “almost calculated to mislead.” <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span>; <em>see also <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">id.</a></span> </em>(“[The affidavit] simply ... stated that [the officers] walked along Reilly’s property until they found an area where marijuana plants were grown. It did not describe this area to the Judge[,] ... [and it] gave no description of the cottage, pond, gazebo, or other characteristics of the area.... [The omitted information] was crucial. Without it, the issuing judge could not possibly make a valid assessment of the legality of the warrant that he was asked to issue.”). We rejected the government’s argument that the officers were entitled to rely on the warrant, noting that the officers had “undert[aken] a search that caused them to invade what they could not fail to have known was potentially ... curtilage,” and that they thereafter “failed to provide [the magistrate issuing the warrant] with an account of what they did,” so that the magistrate was unable to ascertain whether the evidence on which the officers relied in seeking the warrant was “itself obtained illegally and in bad faith.” <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly"><em>Id. </em>at 1281</a></span>. In such circumstances, <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>did not — and does not — permit good faith reliance on a warrant. <em>See Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#923" aria-description="Citation for case: United States v. Leon">468 U.S. at 923</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span> (observing that an officer’s reliance on a warrant is not <em>objectively reasonable </em>if he “misled [the magistrate with] information in an affidavit that [he] knew was false or would have known was false except for his reckless disregard of the truth”).</p>
<p id="b246-8">The present case, however, is akin not to <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>but to this Court’s decision in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>which the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel carefully distinguished, while reaffirming. <em>See Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281-82</a></span>. In <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>an agent, acting without a warrant, used a dog trained to detect narcotics to conduct a “canine sniff’ at a dwelling. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1367" aria-description="Citation for case: United States v. Thomas">757 F.2d at 1367</a></span>. The agent presented evidence acquired as a result of the sniff to a “neutral <page-number citation-index="1" label="223">*223</page-number>and detached magistrate” who, on the basis of this and other evidence, determined that the officer had probable cause to conduct a subsequent search of the dwelling in question. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas"><em>Id. </em>at 1368</a></span>. The defendant moved to suppress the evidence found in executing the search warrant, arguing that the antecedent canine sniff constituted a war-rantless, unconstitutional search and that the evidence acquired from that sniff was dispositive to the magistrate judge’s finding of probable cause. <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1366" aria-description="Citation for case: United States v. Thomas"><em>See id. </em>at 1366</a></span>. This Court agreed on both counts: first deciding, as a matter of first impression in our Circuit, that the canine sniff at issue constituted a search, <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1367" aria-description="Citation for case: United States v. Thomas"><em>id. </em>at 1367</a></span>, and second determining that, absent the evidence acquired from this search, the warrant was not supported by probable cause, <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas"><em>id. </em>at 1368</a></span>. The <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>panel nevertheless concluded that suppression was inappropriate because the agent’s reliance on the warrant was objectively reasonable: “The ... agent brought his evidence, including [a factual description of the canine sniff], to a neutral and detached magistrate. That magistrate determined that probable cause to search existed, and issued a search warrant. There is nothing more the officer could have or should have done under these circumstances to be sure his search would be legal.” <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Id.</a></span></em></p>
<p id="b247-4"><em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>carefully distinguished <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>and in a manner that makes apparent that it is <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>that is dispositive here. First, the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel noted that <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>was unlike <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>in that the agent in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>disclosed all crucial facts for the legal determination in question to the magistrate judge. <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281</a></span>. Then, the <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>panel articulated another difference: while in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>“the officers undertook a search that caused them to invade what they could not fail to have known was potentially Reilly’s curtilage,” in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>the agent “did not have any significant reason to believe that what he had done [conducting the canine sniff] was unconstitutional.” <em>Id:, see also <span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">id.</a></span> </em>(“[U]ntil <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>was decided, no court in this Circuit had held that canine sniffs violated the Fourth Amendment.”). Thus, the predicate act in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span> </em>tainted the subsequent search warrant, whereas the predicate act in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>did not. The distinction did not turn on whether the violation found was <em>predicate, </em>or prior to, the subsequent search warrant on which the officers eventually relied, but on whether the officers’ reliance on the warrant was reasonable.</p>
<p id="b247-8">Contrary to Ganias’s argument, then, it is not the case that good faith reliance on a warrant is never possible in circumstances in which a predicate constitutional violation has occurred. The agents in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>committed such a violation, but they had no “significant reason to believe” that their predicate act was indeed unconstitutional, <em>Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1281" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1281</a></span>, and the issuing magistrate was apprised of the relevant conduct, so that the magistrate was able to determine whether any predicate illegality precluded issuance of the warrant. In such circumstances, invoking the good faith doctrine does not “launder [the agents’] prior unconstitutional behavior by presenting the fruits of it to a magistrate,” as Ganias suggests. Appellant Br. at 56 (quoting <em>Hicks, </em><span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#333" aria-description="Citation for case: State v. Hicks">707 P.2d at 333</a></span>). In such cases, the good faith doctrine simply reaffirms <em>Leon's, </em>basic lesson: that suppression is inappropriate where reliance on a warrant was “objectively reasonable.” <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U.S. at 922</a></span>, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span>.<footnotemark>44</footnotemark></p>
<p id="b248-3"><page-number citation-index="1" label="224">*224</page-number>Such is the case here. First, Agent Hosney provided sufficient information in her affidavit to apprise the magistrate judge of the pertinent facts regarding the retention of the mirrored copies of Gani-as’s hard drives — the alleged constitutional violation on which he relies. Agent Hosney explained that the mirror images in question had been “seized on November 19, 2003 from the offices of Taxes International,” J.A. 461, ¶ 7; that information material to the initial investigation of a third party had been located on the mirrors and “analyzed in detail,” J.A. 464, ¶ 15; that Ganias was not, at the time of the original seizure, under investigation, J.A. 461, ¶ 3; that, “[pjursuant to [that initial warrant],” Agent Hosney could not search Ganias’s personal or business files as the warrant authorized search only of “files for [AB] and IPM,” J.A. 464, ¶ 14; and that Gani-as’s personal data — which Agent Hosney was not authorized to search — was <em>on those mirrored drives, </em>J.A. 467, ¶ 27, and thus, <em>a fortiori, </em>had been there for the past two and a half years. The magistrate judge was thus informed of the fact that mirrors containing data non-responsive to the 2003 warrant had been retained for several years past the initial execution of that warrant and, to the degree it was necessary, that data responsive to the 2003 warrant had been analyzed in detail. The magistrate therefore had sufficient information on which to determine whether such retention precluded issuance of the 2006 warrant. <em>Cf. Thomas, </em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/#1368" aria-description="Citation for case: United States v. Thomas">757 F.2d at 1368</a></span> (“The magistrate, whose duty it is to interpret the law, determined that the canine sniff could form the basis for probable cause.... ”).</p>
<p id="b248-6">Ganias disagrees, arguing, in particular, that, though Agent Hosney alerted the magistrate that the mirrors had been retained for several years; that data responsive to the original warrant had been both located and extensively analyzed; and that those of Ganias’s QuickBooks files that Agent Hosney wanted to search were non-responsive to the original warrant, the Hosney affidavit did not go far enough in. that it failed to disclose that the agents “had been retaining the non-responsive records for a full 16 months <em>after </em>the files within the November 2003 warrant’s scope had been identified.” Appellant Br. at 60. As an initial matter, the Government <em>did </em>alert the magistrate that it had located responsive data on the mirrors <em>and </em>conducted extensive analysis of that responsive material, and it is not clear what else the Government should have said: the district court did not determine — nor does the record show — that by January 2005, as Ganias contends, the Government had determined, as a forward-looking matter, that it had performed all forensic searches of data responsive to the 2003 warrant that might prove necessary over the course of its investigation. <em>Compare </em>J.A. 322 (Q: “So it’s fair to say that as of mid-December [2004], your forensic analysis was completed at that time?” Agent Chowaniec: “That’s correct, of the computers.”), <em>with </em>J.A. 324 (Q: “Did you know you wouldn’t require further analysis by Greg Norman or any other examiner at the Army lab in Georgia after December of 2004?” Agent <page-number citation-index="1" label="225">*225</page-number>Chowaniec: “No.”); see <em>supra </em>note 12. Nor would it be reasonable to expect additional detail in the affidavit on this point, even assuming Ganias’s contention to be correct that the Government had both finished its segregation <em>and </em>provided insufficient facts to alert the magistrate judge to that reality, given the dearth of precedent suggesting its relevance. <em>Cf. Clark, </em><span class="citation" data-id="206195"><a href="/opinion/206195/united-states-v-clark/#105" aria-description="Citation for case: United States v. Clark">638 F.3d at 105</a></span> (“[Wjhere the need for specificity in a warrant or warrant affidavit on a particular point was not yet settled or was otherwise ambiguous, we have declined to find that a well-trained officer could not reasonably rely on a warrant issued in the absence of such specificity.”); <em>cf. Reilly, </em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/#1280" aria-description="Citation for case: United States v. Kevin C. Reilly">76 F.3d at 1280</a></span> (noting that the affidavit in that case, in clear contrast to the affidavit in this one, was “almost calculated to mislead”).</p>
<p id="b249-5">Second, here, as in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span>, </em>it is also clear that the agents, as the panel put it in <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>“did not have any significant reason to believe that what [they] had done was unconstitutional,” <em><span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">Reilly</a></span>, </em>76 F.3d at 1281— that their retention of the mirrored hard drives, while the investigation was ongoing, was anything but routine. At the time of the retention, no court in this Circuit had held that retention of a mirrored hard drive during the pendency of an investigation could violate the Fourth Amendment, much less that such retention would do so in the circumstances presented here. <em>See <span class="citation" data-id="713016"><a href="/opinion/713016/united-states-v-kevin-c-reilly/" aria-description="Citation for case: United States v. Kevin C. Reilly">id.</a></span> </em>(noting that suppression was inappropriate in <em><span class="citation" data-id="8929842"><a href="/opinion/8939436/united-states-v-thomas/" aria-description="Citation for case: United States v. Thomas">Thomas</a></span> </em>in part because no relevant precedent established that canine sniffs of a dwelling “violated the Fourth Amendment”).<footnotemark>45</footnotemark> Moreover, as noted above, the 2003 warrant authorized the lawful seizure not merely of particular records or data, but of the hard drives themselves, or in the alternative the creation of mirror images of the drives to be removed from the premises for later forensic evaluation, . and set no greater limit on the Government’s retention of those materials than on any other evidence whose seizure it authorized.</p>
<p id="b249-9">Finally, the record here is clear that the agents acted reasonably throughout the investigation. They sought authorization in 2003 to seize the hard drives and search them off-site; they minimized the disruption to Ganias’s business by taking full forensic mirrors; they searched the mirrors only to the extent authorized by, first, the 2003 warrant, and then the warrant issued in 2006; they were never alerted that Ganias sought the return of the mirrors; and they alerted the magistrate judge to these pertinent facts in applying for the second warrant. In short, the agents acted reasonably in relying on the 2006 warrant to search for evidence of Ganias’s tax evasion. This case fits squarely within <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>so that, assuming, <em>arguen-do, </em>that a Fourth Amendment violation occurred, suppression was not warranted.</p>
<p id="b249-10">We conclude that the Government relied in good faith on the 2006 search warrant and thus AFFIRM the judgment of the <page-number citation-index="1" label="226">*226</page-number>district court. Given this determination, we do not reach the specific Fourth Amendment question posed to us today.</p>
<footnote label="1">
<p id="b225-5">. These facts are drawn from the district court decision denying Ganias s motion to suppress and from testimony at the suppression hearing and at Ganias’s jury trial. With few exceptions noted herein, the facts in this case are not in dispute.</p>
</footnote>
<footnote label="2">
<p id="b225-6">. Specifically, Agent Conner sought evidence relating to violations of <span class="citation no-link">18 U.S.C. § 287</span> (making false claims) and § 641 (stealing government property).</p>
</footnote>
<footnote label="3">
<p id="b225-7">. The warrant specified as follows:</p>
<blockquote id="b225-8">The search procedure of the electronic data contained in computer operating software or memory devices may include the following techniques:</blockquote>
<blockquote id="b225-9">(a)surveying various file ''directories” and the individual files they contain (analogous to looking at the outside of a file cabinet for the markings it contains and opening a drawer believed to contain pertinent files);</blockquote>
<blockquote id="b225-13">(b) "opening” or cursorily reading the first few "pages” of such files in order to determine their precise contents;</blockquote>
<blockquote id="b225-14">(c) "scanning” storage areas to discover and possibly recover recently deleted files;</blockquote>
<blockquote id="b225-15">(d) "scanning” storage areas for deliberately hidden files; or</blockquote>
<blockquote id="b225-16">(e) performing key word searches through all electronic storage areas to determine whether occurrences of language contained in such storage areas exist that are intimately related to the subject matter of the investigation.</blockquote>
<p id="b225-17">J.A. 433-34.</p>
</footnote>
<footnote label="4">
<p id="b225-18">.In his attached affidavit, Agent Conner offered three reasons why it was necessary for the agents to take entire hard drives off-site for subsequent search rather than search the <page-number citation-index="1" label="202">*202</page-number>hard drives on-site: First, he stated that computer searches had to be conducted by computer forensics experts, who "us[ed] ... investigative techniques” to both “protect the integrity of the evidence ... [and] detect hidden, disguised, erased, compressed, password protected, or encrypted files.” J.A. 448-49. Because of "[t]he vast array” of software and hardware available, it would not always be possible "to know before a search which expert is qualified to analyze the [particular] system and its data.” J.A. 450. Thus, the appropriate experts could not be expected, in all cases, to accompany agents to the relevant site to be searched. Second, Agent Conner affirmed that such searches often must occur in "a laboratory or other controlled environment” given the sensitivity of the digital storage media. J.A. 449-50. And third, he stated that "[t]he search process can take weeks or months, depending on the particulars of the hard drive to be searched.” J.A. 449. The district court found, in denying Ganias's motion to suppress, that, as a result of technological limitations in 2003 and the complexities of searching digital data,. "[a] full [on-site] search would have taken months to complete.” <em>United States </em>v. <em>Ganias, </em>No. 3:08CR00224, <span class="citation no-link">2011 WL 2532396</span>, at *2 D. Conn. June 24, 2011.</p>
</footnote>
<footnote label="5">
<p id="b226-5">. Hard drives are storage media comprising numerous bits — units of data that may be expressed as ones or zeros. Mirroring involves using a commercially available digital software (in the present case, though not always, EnCase) to obtain a perfect, forensic replica of the sequence of ones and zeros written onto the original hard drive. During the mirroring, EnCase acquires metadata about the mirroring process, writing an unalterable record of who creates the copy and when the copy is created. It also assigns the mirror a "hash value” — a unique code that can be used to verify whether, upon subsequent examination of the mirror at any later date, even a single one or zero has been altered from the original reproduction.</p>
</footnote>
<footnote label="6">
<p id="b226-8">. Testifying at the suppression hearing, Agent Conner explained that the decision to take mirrors, rather than the hard drives themselves, reflected a desire to mitigate the burden on Ganias and his business. <em>See </em>J.A. 140-41. The district court credited this testimony, concluding that the agents "used a means less intrusive to the individual whose possessions were seized than other means they were authorized to use.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. The district court, further, explicitly found that the 2003 warrant authorized the Government to take these mirrors, <span class="citation no-link"><em>id. </em>at *10</span>, a position Ganias has not challenged on appeal, and that runs directly counter to the dissent's seeming suggestions that the Government somehow acted improperly when it mirrored Ganias's hard drives or that this initial seizure went beyond the scope of the 2003 warrant, <em>see, e.g., </em>Dissent at 227 (noting that “although the Government had a warrant for documents relating to only two of defendant-appellant Stavros Ganias's accounting clients, it seized <em>all </em>the data from three of his computers”); <em>id. </em>at <em>111 </em>(stating that "the Government ... entered Ganias’s premises with a warrant to seize certain papers and indiscriminately seized — and <em>retained </em>— all papers instead”).</p>
</footnote>
<footnote label="7">
<p id="b227-7">. Ganias claimed before the district court that when he expressed some concern about the scope of the data being seized, an agent assured him that the agents were only looking for files related to AB and IPM, and that irrelevant files "would be purged once they completed their search” for such files. J.A. 428. The district court made no finding to this effect, however. It is undisputed, moreover, that Ganias became aware in February 2006 that the Government retained the mirrors and sought to search them in connection with Ganias’s own tax reporting. At no time thereafter did Ganias seek return of the mirrors pursuant to Federal Rule of Criminal Procedure 41(g) or otherwise contact a case agent to seek their return or destruction.</p>
</footnote>
<footnote label="8">
<p id="b227-11">. These copies were identical digital replicas of Ganias's hard drives as mirrored on November 19, 2003. Notably, the original hard drives in Ganias’s computers had, already been significantly altered since the Government mirrored them. Ganias explains in his brief before this Court that ”[t]wo days after the execution of the November 2003 warrant, [he] reviewed his personal QuickBooks file and.... <em>corrected over 90 errors in earlier journal entries.” </em>Appellant Br. at 15 n.7 (emphasis added).</p>
</footnote>
<footnote label="9">
<p id="b228-5">. The rest of the data remained on the DVDs, where agents would not be able to access it without specific forensic software. <em>See Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *7.</p>
</footnote>
<footnote label="10">
<p id="b228-8">. Norman describes the storage device he sent to Chowaniec as a "DVD,” J.A. 218; the district court described it as a "CD,” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *4. The distinction is immaterial.</p>
</footnote>
<footnote label="11">
<p id="b229-6">. A “restoration” is a software interface that enables a user (potentially a jury) to view data on a mirror as such data would have appeared to a person accessing the data on the original storage device at the time the mirror was created. <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *4.</p>
</footnote>
<footnote label="12">
<p id="b229-7">. At the suppression hearing, Agent Chowan-iec testified, in response to the question whether "as of mid-December, [her] forensic analysis was completed": "That's correct, of the computers.” J.A. 322. But when asked later, "[D]id you know [in December 2004] you wouldn't need to look at any information that had been provided by Greg Norman on that CD anymore in the course of this investigation,” Agent Chowaniec responded, "No,” and when further asked, "Did you know you wouldn’t require further analysis by Greg Norman or any other examiner at the Army lab in Georgia after December of 2004," Agent Chowaniec again responded, "No.” J.A. 324. Agent Conner similarly answered with uncertainty when asked a related question. <em>See </em>J.A. 145 (“I didn’t know the entire universe of information that was contained within the DVDs that were sent to [Norman] for analysis. I knew only what he sent back to me saying this is what I found off your keyword search.”). The dissent disputes our conclusion that the record was unclear on this point, arguing, through citation to Agent Chowan-iec’s testimony, that "the record ... shows otherwise.” Dissent at 233. The district court found no facts on this issue, and the record, as demonstrated above, is indeed unclear.</p>
</footnote>
<footnote label="13">
<p id="b230-4">. Agent Conner’s explanation for why the Government did not, as a matter of policy in this or other cases, delete mirrored drives or otherwise require segregation or deletion of non-responsive data, is not a model of clarity: in addition to citing concerns of evidentiary integrity and suggesting a policy of non-deletion or return prior to the end of an investigation, he noted that "you never know what data you may need in the future," J.A. 122, and at one point referred to the DVDs as "the government’s property, not Mr. Ganias'[s] property," J.A. 146. The dissent seizes on this single sentence during Agent Conner's cross-examination as the smoking gun of the Government’s bad faith, citing it on no fewer than four occasions. <em>See </em>Dissent at 227, 229, 238, 240. The district court, however, did not find facts explicating Agent Conner’s testimony or placing it within the context of the explanations that he and other agents offered for retention of the mirrors. The court did note in its legal analysis that "[a] copy of the evidence was preserved in the form in which it was taken.” <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *8. Further, the Government on appeal provides numerous rationales — many echoing those articulated by Agent Conner <em>throughout </em>his testimony — for why retention of a forensic mirror may be necessary during the pendency of an investigation, none of which amounts to the argument that the mirror is simply "government[] property."</p>
</footnote>
<footnote label="14">
<p id="b230-5">. The dissent suggests that "[w]hat began nearly thirteen years ago as an investigation by the Army into two of Ganias’s business clients <em>somehow </em>evolved into an unrelated investigation by the IRS into Ganias’s personal affairs, largely because” the Government retained the mirrored copies of Ganias's hard drives. Dissent at 241 (emphasis added). In fact, Agent Hosney's affidavit in support of the 2006 warrant explains that the Government suspected Ganias of underreporting his income because of evidence that Ganias had assisted McCarthy in underreporting income from <em>McCarthy’s </em>companies — evidence which led to an indictment of <em>both </em>McCarthy and Ganias for conspiracy to commit tax fraud. Further, when Agent Hosney developed this suspicion — which was hardly "unrelated” to the initial investigation — she did not turn to the mirrors, but instead engaged in old-fashioned investigatory work, "examining Gani-as’s tax returns] more closely to determine if his own income was underreported.” J.A. 465, ¶ 18. She then reviewed deposits in his bank account, cross-referenced bank records and tax returns, and finally presented this evidence in a proffer session to Ganias — all without once looking at any non-responsive information on the mirrors. Only after she had acquired independent probable cause— and only after extensive evidence suggested Ganias may have committed a crime — did Agent Hosney seek a second warrant to search the mirrors. It is, in short, no mystery how the investigation of McCarthy, IPM, and AB came to include Ganias, and, further, an inaccurate statement of the record to suggest that this "evolution” had anything to do with the retention of the mirrors.</p>
</footnote>
<footnote label="15">
<p id="b231-6">. Agent Hosney explained in her testimony: "[W]e couldn't look at that file because it wasn’t — Steve Ganias and Taxes International were not listed on the original Attachment B, items to be seized.” J.A. 348.</p>
</footnote>
<footnote label="16">
<p id="b231-7">. According to Agent Hosney, in that proffer session Ganias claimed "that he failed to record income from his own business [to his QuickBook files] as a result of a computer flaw in the QuickBooks software ... [but that,] ... although he attempted to duplicate the software error, he was unable to do so.” J.A. 467, ¶ 28. Agent Hosney contacted Intuit, Inc., which released QuickBooks, to determine whether such an error might have affected, generally, the pertinent version of the software, and was told that the company was aware of no such "widespread malfunction.” J.A. 469, ¶ 35.</p>
</footnote>
<footnote label="17">
<p id="b231-12">. U.S. Magistrate Judge William I. Garfink-el, who had authorized the 2003 warrant, authorized this 2006 warrant as well. J.A. 430, 454.</p>
</footnote>
<footnote label="18">
<p id="b231-13">. Ganias did not contest before the district court, and does not contest on appeal, that this evidence — none of which was acquired through search of non-responsive data on the mirrors — created sufficient probable cause for the 2006 warrant.</p>
</footnote>
<footnote label="19">
<p id="b232-5">. Many of these entries existed <em>only </em>on the QuickBooks files that the Government had accessed on the mirrors, as a result of Gani-as’s amendments to the entries on his hard drives days after the execution of the 2003 warrant. At trial, Ganias testified that his characterization of the payments as "owner's contributions" was simply a good faith mistake, and not evidence of intent to commit tax evasion, a claim that the Government labeled implausible in light of Ganias’s extensive experience as an IRS agent and accountant.</p>
</footnote>
<footnote label="20">
<p id="b232-6">. Specifically, we asked the parties to brief the following two issues:</p>
<blockquote id="b232-12">(1) Whether the Fourth Amendment was violated when, pursuant to a warrant, the government seized and cloned three computer hard drives containing both responsive and non-responsive files, retained the cloned hard drives for some two-and-a-half years, and then searched the nonresponsive files pursuant to a subsequently issued warrant; and</blockquote>
<blockquote id="b232-13">(2) Considering all relevant factors, whether the government agents in this case acted reasonably and in good faith such that the files obtained from the cloned hard drives should not be suppressed.</blockquote>
<p id="b232-14"><em>United States v. Ganias, 791 </em>F.3d 290 (2d Cir. 2015) (mem.).</p>
</footnote>
<footnote label="21">
<p id="b233-4">. Specifically, courts have long recognized that a prohibition on "general warrants”— warrants completely lacking in particularity— was a central impetus for the ratification of the Fourth Amendment. <em>See, e.g., Riley v. California, - </em>U.S. -, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/#2494" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473, 2494</a></span>, <span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span> (2014) (noting, in the context of evaluating the reasonableness of a warrant-less search of a cell phone, that "[o]ur cases have recognized that the Fourth Amendment was the founding generation's response to the reviled ‘general warrants’ and ‘writs of assistance’ of the colonial era, which allowed British officers to rummage through homes in an unrestrained search for evidence of criminal activity” and that "opposition to such searches was in fact one of the driving forces behind the Revolution itself”); <em>Marshall v. Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#311" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307, 311</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">98 S.Ct. 1816</a></span>, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">56 L.Ed.2d 305</a></span> (1978) (noting, in the context of evaluating the reasonableness of warrantless inspections of business premises, that “[t]he particular offensiveness” of general warrants "was acutely felt by the merchants and businessmen whose premises and products were inspected” under them); <em>Stanford v. Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#486" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 486</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S.Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L.Ed.2d 431</a></span> (1965) (”[T]he Fourth ... Amendment ] guarantee^] ... that no official ... shall ransack [a person’s] home and seize his books and papers under the unbridled authority of a general warrant....”); <em>United States v. Galpin, </em><span class="citation" data-id="931473"><a href="/opinion/931473/united-states-v-galpin/#445" aria-description="Citation for case: United States v. Galpin">720 F.3d 436, 445</a></span> (2d Cir. 2013) ("The chief evil that prompted the framing and adoption of the Fourth Amendment was the 'indiscriminate searches and seizures’ conducted by the British ‘under the authority of "general warrants.” ’ ” (quoting <em>Payton v. New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 583</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980))).</p>
<p id="b233-8">We agree with the dissent that "the precedents are absolutely clear that general warrants are unconstitutional.” Dissent at 237. To the degree that the dissent would go further, however, and find it "absolutely clear” to a reasonable- government agent in 2005 that the retention of a lawfully acquired mirror during the pendency of an investigation and the subsequent search of data on that mirror pursuant to a second warrant would implicate the ban on general warrants, we respectfully disagree.</p>
</footnote>
<footnote label="22">
<p id="b233-9">. <em>See, e.g., L.A. Cty. v. Rettele, </em><span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/#614" aria-description="Citation for case: Los Angeles County, California v. Rettele">550 U.S. 609, 614-16</a></span>, <span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/" aria-description="Citation for case: Los Angeles County, California v. Rettele">127 S.Ct. 1989</a></span>, <span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/" aria-description="Citation for case: Los Angeles County, California v. Rettele">167 L.Ed.2d 974</a></span> (2007) (applying the reasonableness standard to evaluate whether police officers' manner of executing a valid warrant violated the Fourth Amendment); <em>Wilson v. Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#611" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 611</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S.Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L.Ed.2d 818</a></span> (1999) ("[T]he Fourth Amendment does require that police actions in execution of a warrant be related to the objectives of the authorized intrusion....”); <em>Dalia </em>v. <em>United States, </em><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/#258" aria-description="Citation for case: Dalia v. United States">441 U.S. 238, 258</a></span>, <span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">99 S.Ct. 1682</a></span>, <span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/" aria-description="Citation for case: Dalia v. United States">60 L.Ed.2d 177</a></span> (1979) ("[T]he manner in which a warrant is executed is subject to later judicial review as to its reasonableness.”); <em>Terebesi v. Torreso, </em><span class="citation" data-id="8413121"><a href="/opinion/8441937/terebesi-v-torreso/#235" aria-description="Citation for case: Terebesi v. Torreso">764 F.3d 217, 235</a></span> (2d Cir. 2014) ("[T]he method used to execute a search warrant ... <page-number citation-index="1" label="210">*210</page-number>[is] as a matter of clearly established constitutional law,.subject to Fourth Amendment protections. ..c<em>ert. denied sub nom. Torresso v. </em>Terebesi, - U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./135/1842/">135 S.Ct. 1842</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/191/723/">191 L.Ed.2d 723</a></span> (2015) (mem.); <em>Lauro v. Charles, </em><span class="citation" data-id="769506"><a href="/opinion/769506/john-lauro-jr-v-michael-charles-the-city-of-new-york-and-the-police/#209" aria-description="Citation for case: John Lauro, Jr. v. Michael Charles, the City of New York...">219 F.3d 202, 209</a></span> (2d Cir. 2000) ("[T]he Fourth Amendment’s proscription of unreasonable searches and seizures 'not only ... prevents] searches and seizures that would be unreasonable if conducted at all, but also ... ensure[s] reasonableness in the manner and scope of searches and seizures that are carried out.' ” (all but first alteration in original) (quoting <em>Ayeni v. Mottola, </em><span class="citation" data-id="678500"><a href="/opinion/678500/tawa-ayeni-v-james-mottola/#684" aria-description="Citation for case: Tawa Ayeni v. James Mottola">35 F.3d 680, 684</a></span> (2d Cir. 1994))).</p>
</footnote>
<footnote label="23">
<p id="b234-8">. On appeal, Ganias does not question the scope or validity of the 2003 warrant. The district court found that the 2003 warrant authorized the Government to mirror Gani-as's hard drives for off-site review, <em>Ganias, </em><span class="citation no-link">2011 WL 2532396</span>, at *10; that the warrant, though authorizing such seizure, was sufficiently particularized and not a "general warrant," <em>id.; </em>that, absent mirroring for off-site review, on-site review would have taken months, <span class="citation no-link"><em>id. </em>at *2</span>; and that mirroring thus minimized any intrusion on Ganias's business, <span class="citation no-link"><em>id. </em>at *8</span>; <em>cf. </em>Fed. R. Crim. P. 41(e)(2)(B) (which, as amended in 2009, permits a warrant to "authorize the seizure of electronic storage media or the seizure or copying of electronically stored information,” and notes that "[ujnless otherwise specified, the warrant authorizes a later review of the media or information consistent with the warrant”); Fed. R. Crim. P. 41(e)(2)(B) advisory committee's note to 2009 amendments (explaining that, because "[c]omputers and other electronic storage media commonly contain such large amounts of information that it is often impractical for law enforcement to review all of the information during execution of the warrant at the search location[, t]his rule acknowledges the need for a two-step process: officers may seize or copy the entire storage medium and review it later to determine what electronically stored information falls within the scope of the warrant”). Ganias does not contest these conclusions on appeal but contends, instead, that considerations <em>underlying </em>the prohibition on general warrants may require that, if the government lawfully mirrors an entire hard drive containing non-responsive as well as responsive information for off-site review, it may not then retain the mirror throughout the pendency of its investigation.</p>
</footnote>
<footnote label="24">
<p id="b234-12">. As already noted, the district court made no finding as to when or whether forensic examination of the mirrors pursuant to the 2003 warrant was completed.</p>
</footnote>
<footnote label="25">
<p id="b235-6">. The Ninth Circuit declined to reverse the defendant’s conviction, as no improperly seized document was admitted at trial, and as blanket suppression was not warranted. <em>See Tamura, </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#597" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d at 597</a></span>.</p>
</footnote>
<footnote label="26">
<p id="b235-7">. The fact that the officers in <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>lacked a warrant for the initial seizure was not incidental to the decision: the <em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/" aria-description="Citation for case: United States v. Leigh Raymond Tamura">Tamura</a></span> </em>court explicitly found that it was the lack of a warrant that made the initial seizure — even if otherwise understandable in light of the voluminous material to be reviewed — a violation of the Fourth Amendment. <em>See </em><span class="citation" data-id="411427"><a href="/opinion/411427/united-states-v-leigh-raymond-tamura/#596" aria-description="Citation for case: United States v. Leigh Raymond Tamura">694 F.2d at 596</a></span>.</p>
</footnote>
<footnote label="27">
<p id="b236-4">. <em>See </em>Daniel B. Garrie &amp; Francis M. Allegra, Fed. Judicial Ctr., <em>Understanding Software, the Internet, Mobile Computing, and the Cloud: A Guide forjudges </em>8-14 (2015) (contrasting "operating systems ... [which] hide the hardware resources behind abstractions to provide an environment that is more user-friendly,” <em>id. </em>at 13, with machine language, assembly language, high-level languages, data structures, and algorithms); Josh Goldfoot, <em>The Physical Computer and the Fourth Amendment, </em>16 Berkeley J. Crim. L. 112, 117 (2011) (contrasting two perspectives on digital storage media — the "internal perspective,” or how “the user experiences [such media,] as parcels of information, grouped into files, or even into smaller units such as spreadsheet rows” and the "external perspective,” or how the actual computer functions, in which "files are not ... ‘things’ at all,” but "groupings of data ... inseparably tied to the storage medium,” created by the computer by manipulating "chunks of physical matter [such as regions on a hard drive] whose state is altered to record information”).</p>
</footnote>
<footnote label="28">
<p id="b236-5">. <em>See </em>Eoghan Casey, <em>Digital Evidence and Computer Crime </em>472, 474-96 (3d ed. 2011) (highlighting the fact that forensic examination of storage media can create tiny alterations, which necessitates care on the part of examiners in acquiring, searching, and preserving that data); <em>id. </em>at 477-78 (describing the importance of protecting digital storage media from "dirt, fluids, humidity, impact, excessive heat and cold, strong magnetic fields, and static electricity”); Michael W. Graves, <em>Digital Archaeology: The Art and Science of Digital Forensics </em>95 (2014) ("Computer data is extremely volatile and easily deleted, and can be destroyed, either intentionally or accidentally, with a few mouse clicks.”); Bill Nelson et al., <em>Guide to Computer Forensics and Investigations </em>160 (5th ed. 2015) (emphasizing the importance of “maintaining] the integrity of digital evidence in the lab” by creating a read-only copy prior to analysis); Jonathan L. Moore, <em>Time for an Upgrade: Amending the Federal Rules of Evidence to Address the Challenges of Electronically Stored Information in Civil Litigation, </em><span class="citation no-link">50 Jurimetrics J. 147</span>, 153 (2010) ("[All electronically stored information is] prone to manipulation[;] ... [such] alteration can occur intentionally or inadvertently.”); Int’l Org. for Standardization &amp; Int’l Electrotechnical Comm’n, <em>Guidelines for Identification, Collec</em><page-number citation-index="1" label="213">*213</page-number><em>tion, Acquisition, and Preservation of Digital Evidence </em>17 (2012) [hereinafter ISO/IEC, Guidelines] (emphasizing the importance of careful storage and transport techniques and noting that "[s]poliation can result from magnetic degradation, electrical degradation, heat, high or low humidity exposure, as well as shock and vibration”).</p>
</footnote>
<footnote label="29">
<p id="b237-6">. <em>See </em>Goldfoot, <em>supra </em>("Storage media do not naturally divide into parts,” <em>id. </em>at 131; "it is difficult to agree ... on where the subcon-tamers begin and end,” <em>id. </em>at 113.); Orin S. Kerr, <em>Searches and Seizures in a Digital World, </em><span class="citation no-link">119 Harv. L. Rev. 531</span>, 557 (2005) ("[V]irtual files are not robust concepts. Files are contingent creations assembled by operating systems and software.”); <em>see also </em>Orin S. Kerr, <em>Executing Warrants for Digital Evidence: The Case for Use Restrictions on Nonresponsive Data, </em><span class="citation no-link">48 Tex. Tech L. Rev. 1</span>, 32 (2015) ("What does it mean to 'delete' data?”).</p>
</footnote>
<footnote label="30">
<p id="b238-4">. <em>See Fharmacy Records v. Nassar, </em><span class="citation" data-id="2979016"><a href="/opinion/2979016/fharmacy-records-v-salaam-nassar/#525" aria-description="Citation for case: Fharmacy Records v. Salaam Nassar">379 Fed. Appx. 522, 525</a></span> (6th Cir. 2010) (describing testimony of a digital forensics expert in a copyright case that the number and physical location of a file on an Apple Macintosh— which saves files sequentially on its storage medium — demonstrated that the file had been back-dated).</p>
</footnote>
<footnote label="31">
<p id="b238-5">. Indeed, in this very case, as already noted, <em>see supra </em>note 16, Ganias at one point claimed that a “software error” or “computer flaw” prevented him from recording certain income in his QuickBooks files. J.A. 467, ¶ 28. Data confirming the existence, or non-existence, of an error affecting the particular installation of a program on a given digital storage device could be, in a hypothetical case, relevant to the probity of information otherwise located thereupon.</p>
</footnote>
<footnote label="32">
<p id="b238-6">. We note that some of these inferences may be limited to — or at least of more relevance to — traditional magnetic disk drives, which have long been the primary digital storage technology. "Generally when data is deleted from a [traditional hard disk drive], the data is retained until new data is written onto the same location. If no new data is written over the deleted data, then the forensic investigator can recover the deleted data, albeit in fragments.” Alastair Nisbet et al., <em>A Forensic Analysis and Comparison of Solid State Drive Data Retention with TRIM Enabled File Systems, </em>Proceedings of the 11th Australian Digital Forensics Conference 103 (2013). In contrast, the technology used in solid state drives “requires a cell to be completely erased or zeroed-out before a further write can be committed,” <em>id. </em>at 104, and in part because such erasure can be time consuming, solid state drives incorporate protocols which “zero-delete data locations ... as a matter of course,” thereby "reducing] the data that can be retrieved from the drive by [a] forensic investigator,” <em>id. </em>at 103. <em>See also </em>Graeme B. Bell &amp; Richard Boddington, <em>Solid State Drives: The Beginning of the End for Current Practice in Digital Forensic Recovery?, </em>5 J. Digital Forensics, Sec. &amp; L., no. 3, 2010, at 1, 12 (staling that, in connection with such storage devices, "evidence indicating 'no data’ does not authoritatively prove that data did not exist at the time of capture”). That is not to say that studies indicate that deleted information is <em>never </em>recoverable from any model of solid state drive. <em>See, e.g., </em>Christopher King &amp; Timothy Vidas, <em>Empirical Analysis of Solid State Disk Data Retention When Used with Contemporary Operating Systems, </em>8 Digital Investigation 111, 113 (2011) (citing a study suggesting that data deleted from a particular solid state drive was recoverable in certain contexts); Gabriele Bonetti et al., <em>A Comprehensive Black-Box Methodolo

[...TRUNCATED 21519 of 141519 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/United States v. Garner.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Garner"
type: case
citation: "416 F.3d 1208 (2005)"
parallel_cite: ""
neutral_cite: "2005 U.S. App. LEXIS 15369; 2005 WL 1766377"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2005
date_decided: 2005-07-27
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2005-07-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Garner
  varies_by_point: false
  scope_note: "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/166206/united-states-v-garner/"
  cluster_id: 166206
  opinion_id: 166206
  identity_checked: true
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Anchor"
related: ["[[Cady v. Dombrowski]]", "[[United States v. Rideau]]", "[[Graham v. Barnette]]", "[[Caniglia v. Strom]]", "[[Terry v. Ohio]]"]
aliases: ["United States v. Garner (10th Cir. 2005)", "United States v. Mark James Garner"]
tags: ["case", "fourth-amendment", "community-caretaking", "investigative-detention", "persons-in-public", "tenth-circuit"]
holding: "A community-caretaking detention of a person is valid under a three-part test — (1) specific and articulable facts warranting the intrusion, (2) the government's caretaking interest outweighing the individual's liberty interest, and (3) scope and duration tailored to the caretaking purpose; once that purpose is satisfied, continued detention requires independent reasonable suspicion."
lake:
  record_id: United States v. Garner
  status: verified
  projected_at: 2026-07-09
---

# United States v. Garner

*416 F.3d 1208 (10th Cir. 2005)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 5:00 p.m., South Salt Lake City police received a report that a man had been seen in a field near an apartment complex for several hours, unconscious in a half-sitting, half-slumped-over position. Officer Boyd and the municipal fire department responded and found Garner lying in the field. As Officer Boyd approached, Garner walked away but was stopped by a stone wall; Boyd told him to come back and sit so the fire department could examine him. Garner appeared nervous and repeatedly moved his hands in and out of his pockets. After the fire department's examination, the officers continued the encounter, ran a warrant check, and Garner admitted recent drug use and outstanding warrants; he then fled, was tackled, and a search of his pockets revealed a handgun and burglary tools. He was charged as a felon in possession (18 U.S.C. § 922(g)(1)) and moved to suppress.

## Issue
Whether an officer exercising a community-caretaking function may detain a person without reasonable suspicion of a crime, and what standards govern such a caretaking detention of a person.

## Rule
A police officer exercising community-caretaking functions "may ... properly detain a person," subject to a three-part test. **First (articulable need):** "such a community caretaking detention must be based upon 'specific and articulable facts which ... reasonably warrant [an] intrusion' into the individual's liberty." — 416 F.3d at 1213. ^pin-1213

**Second (interest-balancing):** "the government's interest must outweigh the individual's interest in being free from arbitrary governmental interference." — *Id.* ^pin-1213a

**Third (tailoring):** "the detention must last no longer than is necessary to effectuate its purpose, and its scope must be carefully tailored to its underlying justification." — [*Id.*](https://www.courtlistener.com/opinion/166206/united-states-v-garner/#:~:text=the%20detention%20must%20last%20no) ^pin-1213b

Once the caretaking purpose is satisfied, any further detention needs an independent justification: "Once the officer has completed the inquiry necessary to satisfy the purpose of the initial detention, he or she must allow the person to proceed unless the officer has a reasonable suspicion of criminal conduct." — *Id.* ^pin-1213c

## Application
On these facts, Officer Boyd was acting in a community-caretaking role when he directed Garner — reported unconscious in a field for hours — to return so the fire department could examine him; that supplied the articulable facts of need, and the government's interest in protecting a man who "might well have needed medical assistance" outweighed Garner's liberty interest. When the medical examination ended, the detention did not become unlawful: Garner's continuing nervous, evasive behavior and hand movements furnished reasonable suspicion to extend the stop, and the limited questions (name, date of birth) and warrant check were reasonably tailored to the encounter's purpose. The caretaking detention and its continuation were therefore reasonable.

## Conclusion
The detention did not violate the Fourth Amendment; the Tenth Circuit affirmed the denial of Garner's motion to suppress the handgun and burglary tools.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Garner* is the Tenth Circuit anchor for the **persons-in-public** community-caretaking strand, applying [[Cady v. Dombrowski]]'s "community caretaking functions" to the detention of a person and citing [[United States v. Rideau]] (5th Cir.) for extending a caretaking detention based on an apparently impaired person's behavior.
- [[Caniglia v. Strom]] (2021) held there is no *freestanding* community-caretaking exception authorizing a warrantless entry into a **home**; that holding is confined to the home and does **not** disturb *Garner*'s rule for caretaking detentions of persons in public.

## Appears on
- [[Community Caretaking]] — *Key — Anchor*

## Sources
- *United States v. Garner*, 416 F.3d 1208 (10th Cir. 2005) — https://www.courtlistener.com/opinion/166206/united-states-v-garner/ — pinpoints: 1213.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b27773d05741bd36", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Garner"}, "payload": {"all": [{"cite": "416 F.3d 1208", "page": "1208", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "416"}, {"cite": "2005 U.S. App. LEXIS 15369", "page": "15369", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2005"}, {"cite": "2005 WL 1766377", "page": "1766377", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2005"}], "display": "416 F.3d 1208", "official": {"cite": "416 F.3d 1208", "page": "1208", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "416"}, "official_selection_present": true, "record_id": "United States v. Garner"}}
{"assertion_id": "0698ddd5be57cd8b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1213a", "record_id": "United States v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1213a", "pinpoint_status": "slip-only", "quote": "the government's interest must outweigh the individual's interest in being free from arbitrary governmental interference.", "quote_fidelity": "mismatch", "record_id": "United States v. Garner", "star_marker": null}}
{"assertion_id": "851a9fbf80af0eda", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1213", "record_id": "United States v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1213", "pinpoint_status": "slip-only", "quote": "--- # United States v. Garner *416 F.3d 1208 (10th Cir. 2005)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 5:00 p.m., South Salt Lake City police received a report that a man had been seen in a field near an apartment complex for several hours, unconscious in a half-sitting, half-slumped-over position. Officer Boyd and the municipal fire department responded and found Garner lying in the field. As Officer Boyd approached, Garner walked away but was stopped by a stone wall; Boyd told him to come back and sit so the fire department could examine him. Garner appeared nervous and repeatedly moved his hands in and out of his pockets. After the fire department's examination, the officers continued the encounter, ran a warrant check, and Garner admitted recent drug use and outstanding warrants; he then fled, was tackled, and a search of his pockets revealed a handgun and burglary tools. He was charged as a felon in possession (18 U.S.C. § 922(g)(1)) and moved to suppress. ## Issue Whether an officer exercising a community-caretaking function may detain a person without reasonable suspicion of a crime, and what standards govern such a caretaking detention of a person. ## Rule A police officer exercising community-caretaking functions", "quote_fidelity": "mismatch", "record_id": "United States v. Garner", "star_marker": null}}
{"assertion_id": "b80f2cf6e960de27", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1213c", "record_id": "United States v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1213c", "pinpoint_status": "slip-only", "quote": "Once the officer has completed the inquiry necessary to satisfy the purpose of the initial detention, he or she must allow the person to proceed unless the officer has a reasonable suspicion of criminal conduct.", "quote_fidelity": "mismatch", "record_id": "United States v. Garner", "star_marker": null}}
{"assertion_id": "f76251f44af21119", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1213b", "record_id": "United States v. Garner"}, "payload": {"fragment": "#:~:text=the%20detention%20must%20last%20no", "page": null, "pin_id": "pin-1213b", "pinpoint_status": "slip-only", "quote": "the detention must last no longer than is necessary to effectuate its purpose, and its scope must be carefully tailored to its underlying justification.", "quote_fidelity": "matched", "record_id": "United States v. Garner", "star_marker": null}}
{"assertion_id": "55be6957b76aca97", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Garner"}, "payload": {"as_of_content": "2005-07-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Garner", "scope_note": "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public.", "varies_by_point": false}}
```

### lake record — United States v. Garner

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Garner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Garner",
    "case_name_short": "Garner",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Mark James GARNER, Defendant-Appellant",
    "input_case_name": "United States v. Garner",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2005-07-27",
    "year": 2005,
    "docket": null,
    "cluster_id": 166206,
    "lead_opinion_id": 166206,
    "sibling_ids": [
      166206
    ],
    "absolute_url": "/opinion/166206/united-states-v-garner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "416 F.3d 1208",
      "volume": "416",
      "reporter": "F.3d",
      "page": "1208",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2005 U.S. App. LEXIS 15369",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "15369",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1766377",
        "volume": "2005",
        "reporter": "WL",
        "page": "1766377",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 F.3d 1208",
        "volume": "416",
        "reporter": "F.3d",
        "page": "1208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 U.S. App. LEXIS 15369",
        "volume": "2005",
        "reporter": "U.S. App. LEXIS",
        "page": "15369",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2005 WL 1766377",
        "volume": "2005",
        "reporter": "WL",
        "page": "1766377",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "416 F.3d 1208",
    "official_selection": {
      "court_class": "coa",
      "selected": "416 F.3d 1208",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1213",
      "page": null,
      "quote": "--- # United States v. Garner *416 F.3d 1208 (10th Cir. 2005)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 5:00 p.m., South Salt Lake City police received a report that a man had been seen in a field near an apartment complex for several hours, unconscious in a half-sitting, half-slumped-over position. Officer Boyd and the municipal fire department responded and found Garner lying in the field. As Officer Boyd approached, Garner walked away but was stopped by a stone wall; Boyd told him to come back and sit so the fire department could examine him. Garner appeared nervous and repeatedly moved his hands in and out of his pockets. After the fire department's examination, the officers continued the encounter, ran a warrant check, and Garner admitted recent drug use and outstanding warrants; he then fled, was tackled, and a search of his pockets revealed a handgun and burglary tools. He was charged as a felon in possession (18 U.S.C. \u00a7 922(g)(1)) and moved to suppress. ## Issue Whether an officer exercising a community-caretaking function may detain a person without reasonable suspicion of a crime, and what standards govern such a caretaking detention of a person. ## Rule A police officer exercising community-caretaking functions",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1213a",
      "page": null,
      "quote": "the government's interest must outweigh the individual's interest in being free from arbitrary governmental interference.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1213b",
      "page": null,
      "quote": "the detention must last no longer than is necessary to effectuate its purpose, and its scope must be carefully tailored to its underlying justification.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 8961,
      "fragment": "#:~:text=the%20detention%20must%20last%20no",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1213c",
      "page": null,
      "quote": "Once the officer has completed the inquiry necessary to satisfy the purpose of the initial detention, he or she must allow the person to proceed unless the officer has a reasonable suspicion of criminal conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2005-07-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Garner",
    "varies_by_point": false,
    "scope_note": "Good law; anchor for the persons-in-public caretaking strand. Caniglia v. Strom (2021) confined its no-freestanding-caretaking holding to the home and does not disturb a community-caretaking detention of a person in public.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Storey v. Garcia",
          "cluster_id": 3062104,
          "cite": [
            "696 F.3d 987",
            "2012 WL 4478784",
            "2012 U.S. App. LEXIS 20471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lundstrom v. Romero",
          "cluster_id": 173471,
          "cite": [
            "616 F.3d 1108",
            "2010 U.S. App. LEXIS 17136",
            "2010 WL 3222048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Novitsky v. City of Aurora",
          "cluster_id": 169434,
          "cite": [
            "491 F.3d 1244",
            "2007 U.S. App. LEXIS 15959",
            "2007 WL 1935142"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Kenneth McCormick",
          "cluster_id": 3202373,
          "cite": [
            "494 S.W.3d 673",
            "2016 WL 2742841",
            "2016 Tenn. LEXIS 318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Terry Lee Coffman",
          "cluster_id": 4509998,
          "cite": [
            "914 N.W.2d 240"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donahue v. Wihongi",
          "cluster_id": 4707601,
          "cite": [
            "948 F.3d 1177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "STATE of Tennessee v. James David MOATS",
          "cluster_id": 1043895,
          "cite": [
            "403 S.W.3d 170",
            "2013 WL 1181967",
            "2013 Tenn. LEXIS 311"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 1886723,
          "cite": [
            "975 A.2d 877",
            "409 Md. 415",
            "2009 Md. LEXIS 277"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Samuels",
          "cluster_id": 169448,
          "cite": [
            "493 F.3d 1187",
            "2007 U.S. App. LEXIS 16194",
            "2007 WL 1969675"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maurice Trotter, A.K.A. Mo Mardell Trotter, A.K.A. Juice, A.K.A. Del",
          "cluster_id": 797493,
          "cite": [
            "483 F.3d 694",
            "2007 WL 1128851"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 166672,
          "cite": [
            "429 F.3d 952",
            "2005 U.S. App. LEXIS 25106",
            "2005 WL 3105700"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chavez",
          "cluster_id": 4848966,
          "cite": [
            "985 F.3d 1234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Neugin",
          "cluster_id": 4750564,
          "cite": [
            "958 F.3d 924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ozga v. Elliot",
          "cluster_id": 7317315,
          "cite": [
            "150 F. Supp. 3d 178",
            "2015 U.S. Dist. LEXIS 169812",
            "2015 WL 9286767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schreiber v. Moe",
          "cluster_id": 2500057,
          "cite": [
            "445 F. Supp. 2d 799",
            "2006 U.S. Dist. LEXIS 55900",
            "2006 WL 2331175"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 1477450,
          "cite": [
            "932 A.2d 739",
            "176 Md. App. 7",
            "2007 Md. App. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilmore",
          "cluster_id": 2770554,
          "cite": [
            "776 F.3d 765",
            "2015 WL 221619",
            "2015 U.S. App. LEXIS 696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America v. Philip Wetmore",
          "cluster_id": 10697026,
          "cite": [
            "560 F. Supp. 3d 591",
            "2021 DNH 091P"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 4587106,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Duffin Windham v. State",
          "cluster_id": 3109009,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villagrana-Flores",
          "cluster_id": 168356,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Garner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(166206) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 1,
        "triage_snippet_classified": 6
      },
      "lane2_top_cited": {
        "query": "cites:(166206)",
        "reviewed": 22,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 21,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(166206)",
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
    "complete_query": "cites:(166206)",
    "indexed_citing_opinions": 22,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 166206,
        "count": 22,
        "count_source": "search"
      }
    ],
    "citation_count": 40,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-garner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjE0ODExNDEmcz0yNTAwMDU3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28166206%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 166206,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 118352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 160815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 162075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 162579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 164194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 165035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 165216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 604813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 661539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 685190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 166206,
        "cited_id": 741171,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:00:03Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:05:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:01:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Garner

```
                                                                            F I L E D
                                                                      United States Court of Appeals
                                                                              Tenth Circuit
                                     PUBLISH
                                                                             July 27, 2005
                   UNITED STATES COURT OF APPEALS
                                                                        PATRICK FISHER
                                                                                  Clerk
                                TENTH CIRCUIT



    UNITED STATES OF AMERICA,

              Plaintiff-Appellee,


    v.                                                   No. 04-4111


    MARK JAMES GARNER,

              Defendant-Appellant.




         APPEAL FROM THE UNITED STATES DISTRICT COURT
                   FOR THE DISTRICT OF UTAH
                    (D.C. No. 2:03-CR-320-DKW)


Richard P. Mauro, Salt Lake City, Utah, for the Defendant-Appellant.

Paul M. Warner, United States Attorney, District of Utah, and Kevin L. Sundwall,
Assistant United States Attorney, District of Utah, for the Plaintiff-Appellee.


Before HENRY , MCCONNELL, and HARTZ , Circuit Judges.             *




HENRY, Circuit Judge.


*
  After examining the briefs and appellate record, this panel has determined
unanimously that oral argument would not materially assist the determination of
this appeal. See F ED . R. A PP . P. 34(a)(2); 10 TH C IR . R. 34.1(G). The case is
therefore ordered submitted without oral argument.
      After the district court denied his motion to suppress, Mark James Garner

entered a conditional guilty plea to possession of a firearm after conviction of a

felony, a violation of 18 U.S.C. § 922(g)(1). In this appeal, he argues that

because South Salt Lake City police officers lacked reasonable suspicion to detain

him, the district court erred in denying his motion to suppress. We are not

persuaded by Mr. Garner’s arguments and therefore affirm the district court’s

decision.



                                 I. BACKGROUND

      Around 5:00 p.m. on April 11, 2003, the South Salt Lake City Police

Department received information that a man had been seen in a field near an

apartment complex for several hours, unconscious in a half-sitting, half-slumped-

over position. Rec. vol. II, at 5 (Tr. of Oct. 23, 2003 Hr’g). Officer Tyrone

Boyd proceeded to the apartment complex, arriving at approximately the same

time as the municipal fire department. He found Mr. Garner lying in a field on

the north side of the complex.

      As Officer Boyd approached, Mr. Garner began to walk away. Mr. Garner

turned a corner around a building but was stopped by a stone wall. Officer Boyd

told Mr. Garner to come back and sit down so that the fire department personnel

                                         -2-
could examine him. Mr. Garner complied but, according to Officer Boyd, he

appeared nervous, “always looking around [and] saying everything was cool and

[that] he didn’t want any trouble” and moving his hands in and out of his pockets.

Id. at 8.

       After fire department personnel examined Mr. Garner, he began to walk

away. Officer Boyd told him to sit back down because he was not done with him

yet. He then asked Mr. Garner his name and his date of birth, and Mr. Garner

provided the information.

       About this time, Officer Robert Ransdell arrived. Officer Boyd informed

Officer Ransdell that Mr. Garner appeared nervous. Officer Ransdell instructed

Officer Boyd to ask the dispatcher to determine whether Mr. Garner had any

outstanding warrants.

       Officer Ransdell then approached Mr. Garner. Like Officer Boyd, he

noticed that Mr. Garner appeared nervous and was moving his hands in and out of

his pockets. Officer Ransdell asked Mr. Garner to keep his hands in view and

then inquired why Mr. Garner was at the apartment complex and why he was so

nervous. Mr. Garner responded that he did not know why he was there and that

he had passed out. Officer Ransdell then asked whether Mr. Garner had been

taking drugs. Mr. Garner replied that he had “smoked some dope prior that day”

and that he had “some warrants.” Id. at 44.



                                        -3-
      At that point, Officer Boyd informed Officer Ransdell of the results of his

background check: Mr. Garner did have some outstanding warrants. Officer

Ransdell told Mr. Garner, “you’ve got some warrants, no big deal,” id. at 45, but

also indicated that he would be detained until the officers could determine the

substance of those warrants. Officer Ransdell directed Mr. Garner to turn around

and put his hands behind his back.

      At that point, Mr. Garner began to comply but then ran away. The officers,

along with fire department personnel, chased and tackled him. Mr. Garner fought

with the officers, but they managed to place him in handcuffs. A search of Mr.

Garner’s pants pockets revealed a handgun and burglary tools.

      After the government charged Mr. Garner with possession of a firearm after

a felony conviction, a violation of 18 U.S.C. § 922(g)(1), Mr. Garner moved to

suppress the evidence found by the officers. In support of his motion to suppress,

Mr. Garner first argued that Officer Boyd lacked the necessary reasonable

suspicion to support the initial detention. He also argued that, once the fire

department completed its examination, the officers lacked reasonable suspicion to

continue the detention.

      After hearing testimony from Officers Boyd and Ransdell, the district court

rejected both arguments. As to the initial detention, the court reasoned that

Officer Boyd’s observation of Mr. Garner sitting in the field, combined with Mr.


                                         -4-
Garner’s nervous and evasive behavior, provided reasonable suspicion to warrant

detaining Mr. Garner to investigate a possible public intoxication offense and to

determine whether Mr. Garner was suffering from some medical problem. The

court further concluded that even after the fire department personnel completed

their examination, “Officer Boyd had a continuing and remaining need to assess

[Mr. Garner’s] condition to determine whether he was under the influence of

drugs or alcohol . . . and to assess whether [Mr. Garner] was a danger to himself

or others.” Rec. vol. I, doc. 21, at 10 (Memorandum Decision and Order Denying

Defendant’s Motion to Suppress, filed Jan. 8, 2004). Thus, according to the

district court, the officers did not violate Mr. Garner’s Fourth Amendment rights,

and suppression of the evidence discovered in his pockets was not justified.



                                 II. DISCUSSION

      Mr. Garner now argues that Officer Boyd lacked reasonable suspicion to

detain him. He notes that the Officer Boyd acted on an anonymous tip and

observes that, before allowing police officers to detain a suspect, the courts have

usually required some kind of corroboration of the information provided by the

tip. As in the district court proceedings, Mr. Garner also argues that Officers

Boyd and Ransdell lacked the reasonable suspicion required to continue the

detention once fire department personnel finished the physical examination.


                                        -5-
      When reviewing the district court’s denial of a motion to suppress, we view

the evidence in the light most favorable to the government and accept the district

court’s factual findings unless they are clearly erroneous. United States v.

Kimoana, 383 F.3d 1215, 1220 (10th Cir. 2004). The ultimate question of

reasonableness under the Fourth Amendment is a legal conclusion that we review

de novo. Id.



                              A. The Initial Detention

      We begin our inquiry with the initial contact between the police officers

and Mr. Garner—Officer Boyd’s directing Mr. Garner to come back and sit down

so that the fire department personnel could examine him. Although Mr. Garner

argues that Officer Boyd then lacked any evidence that a crime had been

committed, that argument does not fully describe the role in which Officer Boyd

was acting.

      This court has recognized that “‘[e]ncounters are initiated by the police for

a wide variety of purposes, some of which are wholly unrelated to the desire to

prosecute for crime.’” United States v. King, 990 F.2d 1552, 1560 (10th Cir.

1993) (quoting Terry v. Ohio, 392 U.S. 1, 13 (1968)); see also id. (stating that

“those aspects of police function that relate to minimizing the likelihood of

disorder . . . are equal in their importance to the police function in identifying


                                         -6-
and punishing wrongdoers”) (quoting 1 ABA S TANDARDS FOR C RIMINAL J USTICE

§ 1-1.1(c), at 18 (2d ed. 1986)). The Supreme Court has deemed these

responsibilities “community caretaking functions” and has observed that they are

“totally divorced from the detection, investigation, or acquisition of evidence

relating to the violation of a criminal statute.” Cady v. Dombrowski, 413 U.S.

433, 441 (1973).

      In some circumstances, a police officer who is exercising these functions

may properly detain a person. King, 990 F.2d at 1561. For example, in King, we

concluded that a police officer’s brief detention of a motorist to advise him of

hazardous conditions created by an accident and to direct him to stop honking his

horn constituted a proper exercise of the community caretaking function

“regardless of whether [the defendant’s] actions violated any traffic laws.” Id.

      Like an investigative detention for law enforcement purposes, such a

community caretaking detention must be based upon “‘specific and articulable

facts which . . . reasonably warrant [an] intrusion’ into the individual’s liberty.”

Id. at 1560 (quoting Terry, 392 U.S. at 21). Additionally, the government’s

interest must outweigh the individual’s interest in being free from arbitrary

governmental interference. Id. Finally, the detention must last no longer than is

necessary to effectuate its purpose, and its scope must be carefully tailored to its

underlying justification. See Florida v. Royer, 460 U.S. 491, 500 (1983). Once


                                         -7-
the officer has completed the inquiry necessary to satisfy the purpose of the initial

detention, he or she must allow the person to proceed unless the officer has a

reasonable suspicion of criminal conduct. United States v. Gonzalez-Lerma, 14

F.3d 1479, 1483 (10th Cir. 1994).

      We acknowledge that some statements in our subsequent cases appear

inconsistent with the application of the community caretaking doctrine in King.

For example, in United States v. Bute , 43 F.3d 531, 535 (10th Cir. 1994), we

stated that “the community caretaking exception to the warrant requirement is

applicable only in cases involving automobile searches.” We agreed with the

Seventh Circuit that “the plain import from the language of [   Cady ] is that the

Supreme Court did not intend to create a broad exception to the Fourth

Amendment warrant requirement to apply whenever the police are acting in an

‘investigative,’ rather than a ‘criminal’ function’” and that “[the Supreme] Court

intended to confine the holding to the automobile exception and to foreclose an

expansive construction of the decision allowing warrantless searches of private

homes or businesses.”    Id. (quoting United States v. Pichany , 687 F.2d 204, 209

(7th Cir. 1982)). Accordingly, we rejected the government’s argument that the

search of an industrial building based on an officer’s suspicion of burglary and

vandalism was justified under the community caretaking doctrine.




                                           -8-
       In several other decisions, we have cited   Bute for the proposition that “the

community caretaking exception to the warrant requirement is applicable only in

cases involving automobile searches.”      See United States v. Maddox , 388 F.3d

1356, 1366 n.5 (10th Cir. 2004) (rejecting the government’s argument that the

community caretaking doctrine supported the detention of a defendant who had

reached under the seat of a pick-up truck as he pulled up to a residence where

officers were serving a search warrant),    cert. denied , 125 S. Ct. 1689 (2005);

United States v. Thomson , 354 F.3d 1197, 1200 n.1 (10th Cir. 2003) (noting the

government’s concession that the community caretaking doctrine was inapplicable

to a case in which officers had responded to reports of the defendant’s threatening

remarks to coworkers and had opened a canvas bag after the defendant stated that

the bag contained a gun).   But see Gallegos v. City of Colorado Springs    , 114 F.3d

1024, 1029 n.4 (10th Cir. 1997) (concluding that police officers properly detained

a citizen pursuant to the community caretaking function when they observed “a

distraught [man] on a public sidewalk in the middle of the night [who] [n]ot only

smell[ed] of alcohol, but . . . was crying and walking down the street with his

hands over his face”).

       Nevertheless, for several reasons these statements do not foreclose the

officers’ exercise of the community caretaking function here. First,     Bute

involved the search of a building, not, as here, the brief detention of a citizen


                                            -9-
reasonably believed by the officers to be at risk to himself. Additionally, in

Maddox and Thomson , the police officers were acting in their investigative

capacity; there is no indication that in effecting the detentions at issue, they acted

for some purpose “ wholly unrelated to the desire to prosecute for crime.” Terry,

392 U.S. at 13. Moreover, neither Bute nor Maddox nor Thomson cites King , and

our application of the community caretaking doctrine in the earlier case thus

remains the law of the circuit.   See Rogers v. United States , 281 F.3d 1108, 1116

(10th Cir. 2002) (observing that “earlier decisions prevail in the case of an

intra-circuit conflict”).

       Here, upon review of the record, we conclude that Officer Boyd was

exercising a community caretaking function when he directed Mr. Garner to

return so that the fire department could examine him. Cf. Gallegos , 114 F.3d at

1029 n.4 (concluding that police officers properly detained a citizen pursuant to

the community caretaking function when they observed him on a public sidewalk

in the middle of the night smelling of alcohol, crying, and holding his hands over

his face); United States v. Rideau, 969 F.2d 1572, 1574 (5th Cir. 1992) (en banc)

(concluding that officers properly detained a defendant for his own safety and the

safety of others after observing him standing in the middle of the road at night,

dressed in dark clothes, and apparently intoxicated). Moreover, Officer Boyd’s

directive was based on “specific and articulable facts . . . reasonably warrant[ing]


                                          -10-
that intrusion.” Terry, 392 U.S. at 21. In particular, Officer Boyd had received a

report of “an man down, said to be unconscious in a half sitting, half slumped

over position for several hours.” Rec. vol. II, at 5. When he arrived at the scene,

Officer Boyd found Mr. Garner, and he thus had reasonable grounds to conclude

that Mr. Garner might be in need of medical assistance.

      Officer Boyd also had reasonable suspicion that Mr. Garner may have

violated the criminal law. See Gallegos, 114 F.3d at 1029 n.4 (concluding that

police officers’ “initial stop . . . was valid under both an investigatory and

noninvestigatory rationale”). A Utah statute provides that:

             A person is guilty of intoxication if he is under the
             influence of alcohol, a controlled substance, or any
             substance having the property of releasing toxic vapors, to
             a degree that the person may endanger himself or another,
             in a public place or in a private place where he
             unreasonably disturbs other persons.

U TAH C ODE A NN . § 76-9-701(1). The report of an unconscious man in the field

outside the apartment complex, combined with Officer Boyd’s discovery of Mr.

Garner, provided the officer with grounds to briefly detain him to investigate a

possible public intoxication offense.

      We are not persuaded by Mr. Garner’s argument that the anonymity of the

person who called the police invalidates the initial detention. To be sure, as a

general rule, when police officers investigate the possible commission of a crime,

“something more than an anonymous tip of illegal activity is required to provide

                                          -11-
reasonable suspicion.” United States v. Tucker, 305 F.3d 1193, 1201 (10th Cir.

2002); see also Florida v. J.L., 529 U.S. 266, 268 (2000) (holding that “an

anonymous tip that a person is carrying a gun,” “without more,” did not establish

reasonable suspicion). That “something more” may be corroboration of

information provided by the tip. See id. at 270 (stating that “there are situations

in which an anonymous tip, suitably corroborated, exhibits ‘sufficient indicia of

reliability to provide reasonable suspicion to make the investigatory stop’”)

(quoting Alabama v. White, 496 U.S. 325, 327 (1990)). However, when the only

information corroborated is readily available and does not itself indicate that a

crime has been committed, reasonable suspicion may be lacking. See United

States v. Tuter, 240 F.3d 1292, 1297 (10th Cir. 2001) (noting that “[a]lmost

anyone can describe the residents of, and vehicles at, a particular home without

having any special knowledge of what goes on inside the home”).

      Nevertheless, the decisions upon which Mr. Garner relies in challenging the

anonymous source are distinguishable. Unlike the anonymous tips in those cases,

the tip here did not assert that Mr. Garner was engaging in some hidden criminal

activity. See e.g., J.L., 529 U.S. at 272 (describing the issue as whether “the

tipster ha[d] knowledge of concealed criminal activity”) (emphasis added); cf. 4

W AYNE R. L A F AVE , S EARCH AND S EIZURE § 9.5(h), at 571 (4th ed. 2004) (stating

that “the central issue [in this line of cases] is whether the informant’s


                                         -12-
information is so reliable and complete that it makes past, present, or pending

criminal conduct sufficiently likely to justify a stopping of the designated person

for investigation”). Thus, when the officers personally observed a man in the

field near the apartment complex, they confirmed the key information that they

had received from the anonymous source. Because that source had not purported

to describe any hidden criminal activities, no further investigation was necessary

to adequately corroborate the tip so that Officer Boyd could briefly detain Mr.

Garner.

      Similarly, the fact that Officer Boyd could not confirm all the information

offered by the anonymous source (e.g., how long Mr. Garner had been in the field

and whether he had been unconscious) is not dispositive. To establish reasonable

suspicion, not every detail of an anonymous tip must be verified. See White, 496

U.S. at 331.

      We further conclude that the government’s interest in community

caretaking outweighed Mr. Garner’s interest in being free from arbitrary

interference. The anonymous source had reported that Mr. Garner had remained

in the field for several hours and appeared unconscious. In light of that

observation, Mr. Garner might well have needed medical assistance, and the

government had a substantial interest in protecting him. See Rideau, 969 F.2d at

1574 (noting that police officers “have long served the public welfare by



                                        -13-
removing intoxicated people from the public streets, where they pose a hazard to

themselves and others”). In contrast, the intrusion upon Mr. Garner’s liberty was

not extensive. Officer Boyd merely told Mr. Garner to return to the spot from

where he had come so that fire department personnel could conduct a brief

physical examination.

      Accordingly, we conclude that Officer Boyd’s initial seizure of Mr. Garner

comported with the Fourth Amendment.



                           B. The Continuing Detention

      Mr. Garner also challenges Officer Boyd’s actions after the fire department

personnel completed their medical examination. As we have noted, when Mr.

Garner attempted to walk away for a second time, Officer Boyd told him to sit

back down because the police were not done with him yet. Mr. Garner argues that

the officers had no grounds upon which to continue to detain him.

      We disagree. As the fire department examined Mr. Garner, Officer Boyd

had an opportunity to make further observations. He noted that Mr. Garner

appeared “really nervous” and that he was moving his hands in and out of his

pockets. Rec. vol. II, at 8. Moreover, even though the fire department concluded

the examination and apparently found no emergency medical problems, Officer

Boyd had reason to believe that Mr. Garner might still have been intoxicated or



                                       -14-
constituted a danger to himself or others and that Mr. Garner may have violated

the Utah public intoxication statute. Cf. Illinois v. Wardlow, 528 U.S. 119, 125

(2002) (concluding that even though “the conduct justifying [a] stop was

ambiguous and susceptible of an innocent explanation[,]” the officers could

“detain the individuals to resolve the ambiguity”); Rideau, 969 F.2d at 1574-75

(concluding that an apparently intoxicated suspect’s nervous behavior and

backing away from police officers warranted extending the detention).

      Moreover, the continuing detention of Mr. Garner was reasonable in scope.

Although Mr. Garner maintains that Officer Boyd’s request for identification was

unduly intrusive, the Supreme Court has held that “[a]n identity request has an

immediate relation to the Terry stop’s purpose, rationale, and practical demands.”

See Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt County, 124 S. Ct.

2451, 2459 (2004). Officer Boyd’s asking Mr. Garner his name was thus

reasonable. In light of the information that Mr. Garner had been sitting and lying

in the field for several hours (which suggested that he might be a risk to himself

or others and that he might have violated the Utah public intoxication statute),

Mr. Garner’s continuing nervous behavior, and his moving his hands in and out of

his pockets, the subsequent questioning by Officers Boyd and Ransdell was also

reasonably related to the purposes of the detention.




                                        -15-
                               III. CONCLUSION

      Accordingly, we AFFIRM the district court’s decision denying Mr.

Garner’s motion to suppress.




                                     -16-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Gastiaburo.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Gastiaburo"
type: case
citation: "16 F.3d 582 (1994)"
parallel_cite: ""
neutral_cite: 1994 WL 32623
court: "U.S. Court of Appeals, Fourth Circuit"
court_level: coa
circuit: 4th
year: 1994
date_decided: 1994-02-08
docket: ""
authority_weight: "Binding in-circuit — 4th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1994-02-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gastiaburo
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/"
  cluster_id: 7027957
  opinion_id: 6929715
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Acevedo]]", "[[Carroll v. United States]]", "[[United States v. Johns]]", "[[Chambers v. Maroney]]"]
aliases: ["United States v. Gastiaburo (4th Cir. 1994)"]
tags: ["case", "fourth-amendment", "automobile-exception", "impoundment", "delayed-search", "fourth-circuit"]
holding: "The automobile exception is not subject to a temporal limit; a 38-day gap between the car's seizure and the warrantless search did not…"
lake:
  record_id: United States v. Gastiaburo
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gastiaburo

*16 F.3d 582 (4th Cir. 1994)* · U.S. Court of Appeals, Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gastiaburo's car was seized on October 8, 1991. Thirty-eight days later, on November 15, 1991, after his passenger Dina Viola told the police there was a hidden compartment behind the radio containing drugs, money, and a handgun, officer Cosslett went to the impound lot and searched that compartment without a warrant, recovering a gun and a 24-gram rock of crack cocaine. Gastiaburo moved to suppress, arguing the impoundment and the 38-day delay defeated the automobile exception.

## Issue
Whether the automobile exception justifies a warrantless search of a car that has already been seized and impounded, where 38 days elapsed between the seizure and the search.

## Rule
Yes. Probable cause supporting an automobile-exception search is not dissolved by impoundment or by the passage of time. The Fourth Circuit held the government's automobile-exception argument "is clearly correct." — 16 F.3d at 585. ^pin-585

Immobilization does not matter: "the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded." — [*Id.* at 586](https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/#:~:text=the%20justification%20to%20conduct%20a). ^pin-586

Nor is there any temporal limit: "Not a single published federal case speaks of a 'temporal limit' to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car's lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search." — *Id.* at 587. ^pin-587

## Application
On these facts the November 15 search was valid. Viola's uncontroverted tip about the hidden compartment "would have more than sufficed to justify the issuance of a warrant," so it sufficed to justify a warrantless search of that same area, and the officer confined his search to it. Neither of Gastiaburo's objections defeated the exception: the car's impoundment did not convert it into a "fixed piece of property" (citing [[United States v. Johns]]), and the 38-day gap was not a *[[Common Legal Terms#per-se|per se]]* unreasonable delay — indeed the officer "conducted his search on the very same day that he first had probable cause to believe contraband could be found behind the dashboard," so the search "falls squarely within the specifically established and well-delineated 'automobile exception.'" — *Id.* at 587.

## Conclusion
The warrantless search of the impounded car was reasonable under the automobile exception; the denial of suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 4th Cir.**
- No negative subsequent treatment identified. The decision applies [[California v. Acevedo]], [[Carroll v. United States]], [[Chambers v. Maroney]], and [[United States v. Johns]] to reject any "temporal limit" on a probable-cause vehicle search.

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Gastiaburo*, 16 F.3d 582 (4th Cir. 1994) — https://www.courtlistener.com/opinion/7027957/united-states-v-gastiaburo/ — pinpoints: 585, 586, 587. (Lead opinion id 6929715; the cluster-URL integer 7027957 is, separately, an unrelated opinion id — see SR-5 note.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "348d89f6bec5f786", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Gastiaburo"}, "payload": {"all": [{"cite": "16 F.3d 582", "page": "582", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "16"}, {"cite": "1994 WL 32623", "page": "32623", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1994"}], "display": "16 F.3d 582", "official": {"cite": "16 F.3d 582", "page": "582", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "16"}, "official_selection_present": true, "record_id": "United States v. Gastiaburo"}}
{"assertion_id": "44711a28c8afe6ec", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-587", "record_id": "United States v. Gastiaburo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-587", "pinpoint_status": "slip-only", "quote": "Not a single published federal case speaks of a 'temporal limit' to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car's lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search.", "quote_fidelity": "mismatch", "record_id": "United States v. Gastiaburo", "star_marker": null}}
{"assertion_id": "674ca5d5126ac2c8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-586", "record_id": "United States v. Gastiaburo"}, "payload": {"fragment": "#:~:text=the%20justification%20to%20conduct%20a", "page": null, "pin_id": "pin-586", "pinpoint_status": "star-verified", "quote": "the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded.", "quote_fidelity": "matched", "record_id": "United States v. Gastiaburo", "star_marker": "586"}}
{"assertion_id": "b45a1ff1a1a85cde", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-585", "record_id": "United States v. Gastiaburo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-585", "pinpoint_status": "slip-only", "quote": "--- # United States v. Gastiaburo *16 F.3d 582 (4th Cir. 1994)* · U.S. Court of Appeals, Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gastiaburo's car was seized on October 8, 1991. Thirty-eight days later, on November 15, 1991, after his passenger Dina Viola told the police there was a hidden compartment behind the radio containing drugs, money, and a handgun, officer Cosslett went to the impound lot and searched that compartment without a warrant, recovering a gun and a 24-gram rock of crack cocaine. Gastiaburo moved to suppress, arguing the impoundment and the 38-day delay defeated the automobile exception. ## Issue Whether the automobile exception justifies a warrantless search of a car that has already been seized and impounded, where 38 days elapsed between the seizure and the search. ## Rule Yes. Probable cause supporting an automobile-exception search is not dissolved by impoundment or by the passage of time. The Fourth Circuit held the government's automobile-exception argument", "quote_fidelity": "mismatch", "record_id": "United States v. Gastiaburo", "star_marker": null}}
{"assertion_id": "03c8d8c7e4aa98ca", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Gastiaburo"}, "payload": {"as_of_content": "1994-02-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Gastiaburo", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Gastiaburo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gastiaburo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Gastiaburo",
    "case_name_short": "Gastiaburo",
    "case_name_full": "United States v. Joseph GASTIABURO, a/k/a Joe Gastiaburo, a/k/a Joseph Gastiburo, a/k/a Joseph Menendez, a/k/a Joseph Gastibury, a/k/a Robert Julio Gastiaburo, a/k/a Joseph Mendez, a/k/a Joseph Rodriguez",
    "input_case_name": "United States v. Gastiaburo",
    "court": "U.S. Court of Appeals, Fourth Circuit",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "4th",
    "state": null,
    "date_decided": "1994-02-08",
    "year": 1994,
    "docket": null,
    "cluster_id": 7027957,
    "lead_opinion_id": 6929715,
    "sibling_ids": [
      6929715
    ],
    "absolute_url": "/opinion/7027957/united-states-v-gastiaburo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 663093,
        "score": 120,
        "case_name": "United States v. Gastiaburo"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "16 F.3d 582",
      "volume": "16",
      "reporter": "F.3d",
      "page": "582",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "1994 WL 32623",
        "volume": "1994",
        "reporter": "WL",
        "page": "32623",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "16 F.3d 582",
        "volume": "16",
        "reporter": "F.3d",
        "page": "582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 WL 32623",
        "volume": "1994",
        "reporter": "WL",
        "page": "32623",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "16 F.3d 582",
    "official_selection": {
      "court_class": "coa",
      "selected": "16 F.3d 582",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-585",
      "page": null,
      "quote": "--- # United States v. Gastiaburo *16 F.3d 582 (4th Cir. 1994)* \u00b7 U.S. Court of Appeals, Fourth Circuit \u00b7 **Binding in-circuit \u2014 4th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gastiaburo's car was seized on October 8, 1991. Thirty-eight days later, on November 15, 1991, after his passenger Dina Viola told the police there was a hidden compartment behind the radio containing drugs, money, and a handgun, officer Cosslett went to the impound lot and searched that compartment without a warrant, recovering a gun and a 24-gram rock of crack cocaine. Gastiaburo moved to suppress, arguing the impoundment and the 38-day delay defeated the automobile exception. ## Issue Whether the automobile exception justifies a warrantless search of a car that has already been seized and impounded, where 38 days elapsed between the seizure and the search. ## Rule Yes. Probable cause supporting an automobile-exception search is not dissolved by impoundment or by the passage of time. The Fourth Circuit held the government's automobile-exception argument",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-586",
      "page": null,
      "quote": "the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded.",
      "star_marker": "586",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15463,
      "fragment": "#:~:text=the%20justification%20to%20conduct%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-587",
      "page": null,
      "quote": "Not a single published federal case speaks of a 'temporal limit' to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car's lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-02-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gastiaburo",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Lenzi v. Systemax, Inc.",
          "cluster_id": 4684832,
          "cite": [
            "944 F.3d 97"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. State",
          "cluster_id": 5281599,
          "cite": [
            "361 S.W.3d 649",
            "2011 Tex. Crim. App. LEXIS 1664",
            "2011 WL 6057840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Nicholson",
          "cluster_id": 6587522,
          "cite": [
            "58 Mass. App. Ct. 601",
            "792 N.E.2d 124",
            "2003 Mass. App. LEXIS 765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gastiaburo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6929715) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca4)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(6929715)",
        "reviewed": 3,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(6929715)",
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
    "complete_query": "cites:(6929715)",
    "indexed_citing_opinions": 3,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6929715,
        "count": 3,
        "count_source": "search"
      }
    ],
    "citation_count": 159,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gastiaburo.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 3,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:05:59Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:07:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:06:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gastiaburo

```
<opinion type="majority">
<p id="b684-6">OPINION</p>
<author id="b684-7">MURNAGHAN, Circuit Judge:</author>
<p id="b684-8">After pulling over defendant-appellant, Joseph Gastiaburo, for a routine traffic stop, a Virginia State Trooper conducted a warrant-less consent search of Gastiaburo’s car. The search produced $10,000 cash, drug paraphernalia, and several grams of cocaine base (“crack cocaine”). The state police arrested Gastiaburo and impounded his car.</p>
<p id="b684-9">Five weeks later, after receiving a tip from an acquaintance of Gastiaburo, the police conducted a warrantless search of a hidden compartment in the car’s dashboard and seized a loaded semiautomatic pistol and a much larger quantity of crack cocaine. The district court denied Gastiaburo’s motion to suppress the evidence seized during the latter search.</p>
<p id="b684-10">At trial under an indictment charging (a) possession of drugs with intent to distribute, (b) carrying a firearm during and in relation to a drug trafficking crime, and (c) possession of a firearm by a convicted felon, the government put a law enforcement officer on the stand as an expert on drug trafficking practices and techniques. Over and beyond direct and cross-examination, the district judge asked the government’s expert several questions; later, he asked the defense’s sole witness several questions, as well. The jury convicted Gastiaburo on all counts, and the district judge sentenced him to 322 months imprisonment. He has appealed.</p>
<p id="b684-11">
<em>I. The Facts</em>
</p>
<p id="b684-12">At midday on October 8,1991, Joseph Gas-tiaburo and a passenger, Dina Viola, were heading southbound on Interstate 95. Virginia State Police Trooper Mark Cosslett pulled Gastiaburo over for reckless driving. Adhering to state police procedures for a routine traffic stop, Cosslett asked Gastiabu-ro for his license and registration and also asked if he was transporting any drugs or weapons. Gastiaburo replied that he was not, and asked Cosslett whether he would like to take a look in the vehicle. Cosslett replied, “You don’t mind if I take a look through your vehicle?” Gastiaburo answered, “No, go ahead.” Cosslett reiterated his request and explicitly confirmed that Gas-tiaburo had no objections to a search of both the vehicle and any containers therein.</p>
<p id="b684-13">Following those repeated consents to a search, Cosslett placed Gastiaburo in the police cruiser, wrote out a traffic citation, and waited for a backup officer. After the backup arrived, Gastiaburo was again asked for permission to search the vehicle, including any containers, and he again consented. With Gastiaburo sitting on the interstate guardrail adjacent to the car, Cosslett commenced his search. The search produced, among other things, a set of hand scales, rolling papers, razor blades, a knife with a retractable blade, a large number of small plastic baggies, an address book with various names and financial notations, a paging device or “beeper,” $10,000 in cash (folded into $100 increments), a box of .25 caliber ammunition, and a black leather zippered pouch containing twenty-one small zip-locked plastic baggies, each containing about one-fifth of a gram of a rock-like substance that was subsequently determined to be crack cocaine.</p>
<p id="b684-14">The backup officer arrested Gastiaburo and drove him to a nearby detention center. His car was seized for forfeiture by the Commonwealth of Virginia and removed to an impoundment lot at the regional State Police headquarters, where it was secured by parking state vehicles around it. The next morning an inventory search of the impounded car produced no additional contraband.</p>
<p id="b684-15">On November 15, 1991, Cosslett and Viola, Gastiaburo’s passenger at the time of arrest, <page-number citation-index="1" label="585">*585</page-number>met at the Prince William County Courthouse. Viola inquired whether he had found the gun. When Cosslett said that he had not, Viola told him that there was a hidden compartment located behind the radio in the console of Gastiaburo’s car, and that the compartment contained drugs, money, and a handgun.</p>
<p id="b685-4">Cosslett promptly went to the impound lot and, without obtaining a warrant, searched for and located the hidden compartment. He found and seized a loaded, .25 caliber semiautomatic pistol and, wrapped in aluminum foil and then in brown paper lunch bags, a lump of rock-like substance that was subsequently determined to be a 24-gram “rock” of crack cocaine.</p>
<p id="b685-5">A grand jury of the United States District Court for the Eastern District of Virginia returned the above-mentioned three-count indictment against Gastiaburo. On April 3, 1992, a suppression hearing took place. After listening to conflicting testimony from Gastiaburo and Cosslett, the district judge resolved the credibility conflicts in Cosslett’s favor and denied all of Gastiaburo’s motions, including a motion to suppress the gun and the crack cocaine that Cosslett had seized during his warrantless search of the impounded car on November 15, 1991.</p>
<p id="b685-6">On April 22, 1992, Gastiaburo was tried before a jury in Judge Ellis’s courtroom. The government called Cosslett, who gave testimony substantially similar to his earlier testimony at the suppression hearing. The government also called Sergeant Floyd Johnston of the U.S. Park Police as an expert in the field of drug trafficking practices and techniques. Among other things, Johnston examined the various government exhibits that had been seized from Gastiaburo’s car and testified that they were generally consistent with crack cocaine distribution, rather than with mere personal use of the drug. In response to questions from the bench, Johnston also testified about the quantities of crack cocaine consumed by typical addicts.</p>
<p id="b685-7">Gastiaburo called only one witness, Charles J. Pucci, his brother-in-law. Pucci testified that Gastiaburo had visited him in New York City shortly before the arrest, and that he had given Gastiaburo $10,000 in loose cash to pay a debt to a family member in Florida. The court asked Pucci several questions about the cash, and also inquired about Pucci’s occupation. Judge Ellis then asked whether Pucci had ever been convicted of a felony. Pucci responded, “I have not.”</p>
<p id="b685-9">The jury returned guilty verdicts on all three counts. The district court imposed a sentence of 322 months imprisonment plus five years of supervised release, $10,000 forfeiture, and $150 in special assessments. Gastiaburo’s appeal followed.</p>
<p id="b685-10">
<em>II. The Gun and Cocaine Seized on November 15, 1991</em>
</p>
<p id="b685-11">Gastiaburo has contended that the gun and the 24-gram rock of crack cocaine that the police seized from his car on November 15, 1991 should have been suppressed because they were obtained without a warrant, in violation of his Fourth Amendment rights. In response the government has argued that the district court’s denial of Gastiaburo’s motion to suppress should be affirmed on- any of four grounds: (1) the evidence was seized during a valid consent search; (2) the evidence was seized during a valid inventory search; (3) the police had probable cause to believe the search would uncover contraband (i.e., the so-called “automobile exception” to the warrant requirement); or (4) the evidence was seized during a valid search of a vehicle subject to forfeiture. The third argument, based on the “automobile exception” to the warrant requirement, is clearly correct. Because we review such a mixed question of law and fact <em>de novo, see, e.g., United States v. Moore, </em><span class="citation" data-id="487763"><a href="/opinion/487763/united-states-v-norman-delano-moore/#1106" aria-description="Citation for case: United States v. Norman Delano Moore">817 F.2d 1105, 1106-08</a></span> (4th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./484/965/">484 U.S. 965</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./108/456/">108 S.Ct. 456</a></span>, <span class="citation" data-id="9067158"><a href="/opinion/9073337/smith-v-united-states-merit-systems-protection-board/" aria-description="Citation for case: Smith v. United States Merit Systems Protection Board">98 L.Ed.2d 396</a></span> (1987), the district court’s decision not to suppress the evidence seized on November 15, 1991 should be affirmed.</p>
<p id="b685-12">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects against unreasonable searches and seizures.” U.S. Const. amend. IV. Searches conducted without a warrant issued by a judge or magistrate upon probable cause “are <em>per se </em>unreasonable under the Fourth Amendment — subject only to a few specifically established and <page-number citation-index="1" label="586">*586</page-number>well-delineated exceptions.” <em>California v. Acevedo, </em><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U.S. 565</a></span>, -, -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#1991" aria-description="Citation for case: California v. Acevedo">111 S.Ct. 1982, 1991</a></span>, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">114 L.Ed.2d 619</a></span> (1991) (citations and internal quotation marks omitted); <em>see also United States v. Turner, </em><span class="citation no-link">9383 F.2d 240</span>, 244 (4th Cir.1991). At least since 1925, when the Supreme Court handed down its decision in <em>Carroll v. United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U.S. 132</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">45 S.Ct. 280</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">69 L.Ed. 543</a></span> (1925), the federal judiciary has recognized an “automobile exception” to the warrant requirement: it may be reasonable and therefore constitutional to search a movable vehicle without a warrant, even though it would be unreasonable and unconstitutional to conduct a similar search of a home, store, or other fixed piece of property. <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><em>See id. </em>at 153, 158-59</a></span>, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#285" aria-description="Citation for case: Carroll v. United States">45 S.Ct. at 285, 287</a></span>.</p>
<p id="b686-6">The Supreme Court delivered its most recent exposition on the “automobile exception” in <em>California v. <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">Acevedo, supra.</a></span> </em>The <em><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">Acevedo</a></span> </em>Court held that “[t]he police may search an automobile and the containers within it where they have probable cause to believe contraband or evidence is contained.” Ill S.Ct. at 1991. “[T]he scope of a warrant-less search of an automobile is ‘no narrower — and no broader — than the scope of a search authorized by a warrant supported by probable cause.’” <em>United States v. $29,000</em>—U.S. <em>Currency, </em><span class="citation" data-id="442875"><a href="/opinion/442875/united-states-v-29000-us-currency-in-re-2900000-us-currency/#855" aria-description="Citation for case: United States v. $29,000--u.s. Currency, in Re 29,000.00...">745 F.2d 853, 855</a></span> (4th Cir.1984) (quoting <em>United States v. Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U.S. 798, 823</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2172" aria-description="Citation for case: United States v. Ross">102 S.Ct. 2157, 2172</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">72 L.Ed.2d 572</a></span> (1982)). With or without warrant, the scope of the search of an automobile is defined by the object of the search and the places in which there is probable cause to believe that it may be found. For example, probable cause to believe that a container placed in the trunk of an automobile contains contraband does not justify a search of the entire car. <em>See Acevedo, </em>500 U.S. at -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">111 S.Ct. at 1991</a></span> (citing <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U.S. at 824</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2172" aria-description="Citation for case: United States v. Ross">102 S.Ct. at 2172</a></span>).</p>
<p id="b686-9">In the present case, as of November 15, 1991, the police had probable cause to believe that one particular area within Gastiaburo’s car contained as-yet undiscovered contraband. On that date, Dina Viola, Gastiaburo’s passenger at the time <em>of - </em>his arrest, met Cosslett at the Prince William County Courthouse and told him that there was a hidden compartment behind the radio in the console of Gastiaburo’s car and that the compartment contained additional drugs and money, as well as a handgun. Those facts are uneon-troverted, and they would have more than sufficed to justify the issuance of a warrant by a magistrate. Therefore, they also sufficed to justify a warrantless search of the area behind the radio.</p>
<p id="b686-11">Furthermore, the facts in the record indicate no overreaching by the police. As of November 15, 1991, the police apparently had probable cause to believe that contraband remained hidden only where Viola had told Cosslett to look. Appropriately, Cos-slett confined his search to that area. And Gastiaburo does not claim that the search of November 15, 1991 covered a broader scope than that contained in the tip that gave Cos-slett probable cause. Therefore, the November 15, 1991 search complied with the requirements of the Fourth Amendment.</p>
<p id="b686-12">Gastiaburo has made two responses to the government’s “automobile exception” argument. First, he has contended that im-poundment effectively transformed his car from a movable vehicle into a “fixed piece of property,” thus making the automobile exception to the warrant requirement inapplicable. However, the justification to conduct a warrantless search under the automobile exception does not disappear merely because the car has been immobilized and impounded. See <em>United States v. Johns, </em><span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#484" aria-description="Citation for case: United States v. Johns">469 U.S. 478, 484</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#885" aria-description="Citation for case: United States v. Johns">105 S.Ct. 881, 885</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">83 L.Ed.2d 890</a></span> (1985); <em>Florida v. Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#382" aria-description="Citation for case: Florida v. Meyers">466 U.S. 380, 382</a></span>, <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/#1853" aria-description="Citation for case: Florida v. Meyers">104 S.Ct. 1852, 1853</a></span>, <span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">80 L.Ed.2d 381</a></span> (1984) (per curiam); <em>Michigan v. Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. 259, 261</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. 3079</a></span>-3080-81, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">73 L.Ed.2d 750</a></span> (1982) (per curiam); <em>see also Turner, </em>933 F.2d at 244; <em>$29,000</em>—U.S. <em>Currency, </em><span class="citation" data-id="442875"><a href="/opinion/442875/united-states-v-29000-us-currency-in-re-2900000-us-currency/#855" aria-description="Citation for case: United States v. $29,000--u.s. Currency, in Re 29,000.00...">745 F.2d at 855</a></span>. Under the Supreme Court’s precedents, the fact that impoundment may have made it virtually impossible for anyone to drive the car away or to tamper with its contents is irrelevant to the constitutionality of a warrantless search under the circumstances of the present case. <em>See, e.g., Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. at 261</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#3081" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. at 3081</a></span>.</p>
<p id="b686-13">Second, Gastiaburo has noted that thirty-eight days transpired between the sei<page-number citation-index="1" label="587">*587</page-number>zure of his car on October 8, 1991 and the warrantless search in question, and has argued that the delay violated the “temporal limit on the automobile exception” and that “it was a <em>per se </em>unreasonable delay.” Gastia-buro’s “delay” argument also lacks merit. Not a single published federal case speaks of a “temporal limit” to the automobile exception. The Supreme Court has repeatedly stated that a warrantless search of a car (1) need not occur contemporaneously with the car’s lawful seizure and (2) need not be justified by the existence of exigent circumstances that might have made it impractical to secure a warrant prior to the search. <em>See Acevedo, </em>500 U.S. at -, <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#1986" aria-description="Citation for case: California v. Acevedo">111 S.Ct. at 1986</a></span> (explaining that the police can search later whenever they could have searched earlier, had they so chosen) (describing the Court’s reasoning in <em>Chambers v. Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U.S. 42, 51-52</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#1981" aria-description="Citation for case: Chambers v. Maroney">90 S.Ct. 1975, 1981-82</a></span>, <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">26 L.Ed.2d 419</a></span> (1970)); <em>Johns, </em><span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#484" aria-description="Citation for case: United States v. Johns">469 U.S. at 484-85</a></span>, <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#885" aria-description="Citation for case: United States v. Johns">105 S.Ct. at 885-86</a></span>; <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U.S. at 261-62</a></span>, <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#3080" aria-description="Citation for case: Michigan v. Thomas">102 S.Ct. at 3080-81</a></span>. Therefore, the passage of time between the seizure and the search of Gastiaburo’s car is legally irrelevant.</p>
<p id="b687-6">Moreover, Cosslett’s actual “delay” here was minimal: he conducted the search on the very same day that he first had probable cause to believe contraband could be found behind the dashboard of Gastiaburo’s car. Cosslett testified at the suppression hearing that, upon learning of the hidden compartment in Gastiaburo’s dashboard, he proceeded “to the headquarters, obtained the keys from the evidence custodian, removed the vehicles [that were blocking in Gastiaburo’s ear], and checked the hidden compartment.” Such an expeditious search cannot be deemed <em>“per se </em>unreasonable.” Rather, it falls squarely within the specifically established and well-delineated “automobile exception” to the Fourth Amendment’s warrant requirement.</p>
<p id="b687-7">
<em>III. Expert Testimony</em>
</p>
<p id="b687-8">Gastiaburo next has contended that the district court erred in admitting expert testimony from Sergeant Johnston that included (1) an opinion as to Gastiaburo’s intent, allegedly in violation of Rule 704(b) of the Federal Rules of Evidence; and (2) matters within the common understanding of the jurors, allegedly in violation of Rule 702.</p>
<p id="b687-11"><em>A Johnston’s testimony on “intent to distribute.” </em>The prosecutor had asked Johnston: “Would you have an opinion based on your training and experience what that crack cocaine [that the police had seized from the hidden compartment in Gastiaburo’s car and the twenty-one zip-locked plastic baggies, each containing a “hit” of crack cocaine], ... were possessed for, taking all the elements into consideration?” Johnston replied: “Clearly, based on my opinion, my training and experience, it was certainly possessed with the intent to distribute.” Gastiaburo’s trial attorney did not object. On appeal, Gastiaburo has claimed that Johnston’s answer provided expert opinion testimony on Gastiaburo’s intent in a specific-intent crime, a violation of Federal Rule of Evidence 704(b).</p>
<p id="b687-12">Because Gastiaburo did not object at trial, we review the admission of Johnston’s expert testimony for plain error. Rule 52(b) of the Federal Rules of Criminal Procedure provides that “[p]lain errors or defects affecting substantial rights may be noticed although they were not brought to the attention of the court.” Fed.R.Crim.P. 52(b). The Supreme Court recently interpreted Rule 52(b) to require not only the existence of an “error” <em>(i.e., </em>a “[deviation from a legal rule” that the defendant has not waived), but also that the error be “plain” <em>(i.e., </em>“clear” or, equivalently, “obvious” under the current applicable law). <em>United States v. Olano, </em>— U.S. -, -, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/#1777" aria-description="Citation for case: United States v. Olano">113 S.Ct. 1770, 1777</a></span>, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/" aria-description="Citation for case: United States v. Olano">123 L.Ed.2d 508</a></span> (1993) (citations and internal quotation marks omitted).</p>
<p id="b687-15">Rule 704(b) of the Federal Rules of Evidence provides:</p>
<blockquote id="b687-16">No expert witness testifying with respect to the mental state or condition of a defendant in a criminal case may state an opinion or inference as to whether the defendant did or did not have the mental state or condition constituting an element of the crime charged or of a defense thereto. Such ultimate issues are matters for the trier of fact alone.</blockquote>
<p id="b688-3"><page-number citation-index="1" label="588">*588</page-number>Fed.R.Evid. 704(b). Rule 704(b) was enacted in the wake of the attempted assassination of President Reagan and the murder of John Lennon, and was an attempt to constrain psychiatric testimony on behalf of defendants asserting the insanity defense. <em>See generally </em>Anne Lawson Braswell, Note, <em>Resurrection of the Ultimate Issue Rule: Federal Rule of Evidence 701(b) and the Insanity Defense, </em>72 Cornell L.Rev. 620 (1987). The application of the same rule in an entirely different context — a law enforcement officer’s expert opinion testimony on behalf of the government at the trial of an alleged drug dealer — is murky at best.</p>
<p id="b688-4">Was Johnston in fact “testifying with respect to the mental state or condition of a defendant in a criminal case”? Did he actually “state an opinion or inference as to whether the defendant did or did not have the mental state or condition constituting an element” of the crime of possession of cocaine with intent to distribute? The testimony lends itself to the interpretation that possession of the quantity of crack cocaine seized from Gastiaburo’s car — with the individual “hits” packaged in twenty-one small zip-locked baggies, and the larger “rock” in foil and paper bags — was consistent with the distribution of cocaine, rather than with mere personal use of the drug.</p>
<p id="b688-5">In any event, Gastiaburo’s failure to object at the trial made the relevant inquiry for us whether Judge Ellis committed a “plain error” under Rule 52(b). The error, if any, was not “plain” (or “clear” or “obvious”). <em>Cf. Olano, </em>— U.S. at -, <span class="citation" data-id="9432789"><a href="/opinion/112848/united-states-v-olano/#1777" aria-description="Citation for case: United States v. Olano">113 S.Ct. at 1777</a></span>. Most appellate panels have refused to find error in the admission of expert testimony on intent to distribute controlled substances. <em>See, e.g., United States v. Valentine, </em><span class="citation" data-id="599184"><a href="/opinion/599184/united-states-v-glenn-valentine/#910" aria-description="Citation for case: United States v. Glenn Valentine">984 F.2d 906, 910</a></span> (8th Cir.), <em>cert. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./114/93/">114 S.Ct. 93</a></span>, <span class="citation" data-id="113210"><a href="/opinion/113210/robinson-v-central-brass-manufacturing-co/" aria-description="Citation for case: Robinson v. Central Brass Manufacturing Co.">126 L.Ed.2d 60</a></span> (1993); <em>United States v. Chin, </em><span class="citation" data-id="597101"><a href="/opinion/597101/united-states-v-andrew-p-chin/#1279" aria-description="Citation for case: United States v. Andrew P. Chin">981 F.2d 1275, 1279</a></span> (D.C.Cir.1992), <em>cert. denied, </em>—— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./113/2377/">113 S.Ct. 2377</a></span>, <span class="citation no-link">124 L.Ed.2d 281</span> (1993); <em>United States v. Williams, </em><span class="citation" data-id="596385"><a href="/opinion/596385/united-states-v-patrick-a-williams/#1465" aria-description="Citation for case: United States v. Patrick A. Williams">980 F.2d 1463, 1465-66</a></span> (D.C.Cir.1992); <em>United States v. Wilson, </em><span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#810" aria-description="Citation for case: United States v. Terry Wilson">964 F.2d 807, 810</a></span> (8th Cir.1992); <em>United States v. Gomez-Norena, </em><span class="citation" data-id="544744"><a href="/opinion/544744/united-states-v-jaime-leon-gomez-norena/#502" aria-description="Citation for case: United States v. Jaime Leon Gomez-Norena">908 F.2d 497, 502</a></span> (9th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./498/947/">498 U.S. 947</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./111/363/">111 S.Ct. 363</a></span>, <span class="citation" data-id="9097104"><a href="/opinion/9102741/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">112 L.Ed.2d 326</a></span> (1990); <em>United States v. Alvarez, </em><span class="citation" data-id="500424"><a href="/opinion/500424/united-states-v-marcelino-efrain-alvarez-jose-delgado-ramirez-juan-ramon/#1030" aria-description="Citation for case: United States v. Marcelino Efrain Alvarez, Jose Delgado...">837 F.2d 1024, 1030-31</a></span> (11th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./486/1026/">486 U.S. 1026</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./108/2003/">108 S.Ct. 2003</a></span>, 2004, <span class="citation no-link">100 L.Ed.2d 234</span>, 235 (1988).<footnotemark>*</footnotemark> One recent D.C. Circuit decision did find that the admission of expert testimony on the defendant’s intent to distribute violated Rule 704(b), but went on to hold that the error was not “plain” under the settled law of the Supreme Court or the D.C. Circuit, as it stood at the time of the trial. <em>See United States v. Mitchell, </em><span class="citation" data-id="609728"><a href="/opinion/609728/united-states-v-keith-len-mitchell-united-states-of-america-v-richard/#421" aria-description="Citation for case: United States v. Keith Len Mitchell, United States of...">996 F.2d 419, 421-23</a></span> (D.C.Cir.1993).</p>
<p id="b688-16"><em>B. Johnston’s other testimony. </em>Gastiaburo also has contended that the district court should have rejected various parts of Johnston’s testimony as insufficiently helpful for the trier of fact under Federal Rule of Evidence 702. On direct examination, Johnston testified, over defense counsel’s objection, that it is not uncommon for people transporting controlled substances to grant consent to law enforcement officers to search their possessions or their persons. He also testified about the attributes of persons involved in the distribution of drugs and the “tools of the <em>trade” </em>— e.g., beepers, address books, the quantities of drugs possessed by dealers, and so on. During defense counsel’s cross-examination, Judge Ellis interjected, asking Johnston about half-a-dozen questions. In response, Johnston testified about addicts’ typical levels of crack consumption, typical patterns of addiction, and typical quantities of crack that a user will purchase and hold at any given moment. Although Gastiaburo did not object at trial to the colloquy between Judge Ellis and Johnston, he has complained on appeal that the judge’s questions violated Rule 614 of the Federal Rules of Evidence, <em>see infra </em>Part IV, and that the Johnston’s answers violated Rule 702.</p>
<p id="b688-17">Federal Rule of Evidence 702 provides:</p>
<blockquote id="AMb-">If scientific, technical, or other specialized knowledge-will assist the trier of fact to understand the evidence or to determine a <page-number citation-index="1" label="589">*589</page-number>fact in issue, a witness qualified as an expert by knowledge, skill, experience, training, or education, may testify thereto in the form of an opinion or otherwise.</blockquote>
<p id="Agk">The trial judge has broad discretion under Rule 702. <em>See Hamling v. United States, </em><span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/#108" aria-description="Citation for case: Hamling v. United States">418 U.S. 87, 108</a></span>, <span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/#2903" aria-description="Citation for case: Hamling v. United States">94 S.Ct. 2887, 2903</a></span>, <span class="citation" data-id="9842003"><a href="/opinion/109084/hamling-v-united-states/" aria-description="Citation for case: Hamling v. United States">41 L.Ed.2d 590</a></span> (1974) (“[T]he District Court has wide discretion in its determination to admit and exclude evidence, and this is particularly true in the case of expert testimony.”) (citations omitted); <em>cf. United States v. Ham, </em><span class="citation" data-id="9011910"><a href="/opinion/9018724/united-states-v-ham/#1252" aria-description="Citation for case: United States v. Ham">998 F.2d 1247, 1252</a></span> (4th Cir.1993).</p>
<p id="b689-4">As then-Judge Ruth Bader Ginsburg has explained: “In accord with the commodious standard of Federal Rule of Evidence 702, expert testimony on the <em>modus operandi </em>of criminals ‘is commonly admitted,’ particularly regarding the methods of drug dealers.” <em>Chin, </em><span class="citation" data-id="597101"><a href="/opinion/597101/united-states-v-andrew-p-chin/" aria-description="Citation for case: United States v. Andrew P. Chin">981 F.2d at 1279</a></span> (quoting <em>United States v. Dunn, </em><span class="citation" data-id="506047"><a href="/opinion/506047/united-states-v-richard-earl-dunn-united-states-of-america-v-angelo/#763" aria-description="Citation for case: United States v. Richard Earl Dunn, United States of...">846 F.2d 761, 763</a></span> (D.C.Cir.1988)); <em>see also Mitchell, </em><span class="citation" data-id="609728"><a href="/opinion/609728/united-states-v-keith-len-mitchell-united-states-of-america-v-richard/#423" aria-description="Citation for case: United States v. Keith Len Mitchell, United States of...">996 F.2d at 423</a></span> (“Federal courts often allow expert testimony on narcotics operations to familiarize jurors with the variety of methods by which drug dealers attempt to pursue and conceal their activities_”) (citing <em>Dunn, </em><span class="citation" data-id="506047"><a href="/opinion/506047/united-states-v-richard-earl-dunn-united-states-of-america-v-angelo/#763" aria-description="Citation for case: United States v. Richard Earl Dunn, United States of...">846 F.2d at 763</a></span>).</p>
<p id="b689-7">We have repeatedly upheld the admission of law enforcement officers’ expert opinion testimony in drug trafficking eases. <em>See, e.g., United States v. Safari, </em><span class="citation" data-id="507790"><a href="/opinion/507790/united-states-v-mahmoud-safari/#895" aria-description="Citation for case: United States v. Mahmoud Safari">849 F.2d 891, 895</a></span> (4th Cir.) (upholding the admission of expert testimony on the size of an average dose of heroin, because, “[w]hile not usurping the function of the jury, this testimony aided the jury dining its deliberations, for most laymen are not familiar with the quantity, purity, and dosage units of heroin”), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./488/945/">488 U.S. 945</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./109/374/">109 S.Ct. 374</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/102/363/">102 L.Ed.2d 363</a></span> (1988); <em>United States v. Monu, </em><span class="citation" data-id="464629"><a href="/opinion/464629/united-states-v-ifeanyi-monu/#1210" aria-description="Citation for case: United States v. Ifeanyi Monu">782 F.2d 1209, 1210-11</a></span> (4th Cir.1986) (upholding the admission of two investigative agents’ expert opinion testimony regarding the purity of heroin and heroin distributors’ use of triple-beam balance scales). Similarly, in <em>United States v. Wilson, </em><span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#809" aria-description="Citation for case: United States v. Terry Wilson">964 F.2d at 809-10</a></span>, the Eighth Circuit upheld a conviction for possession with intent to distribute and affirmed the admission of a drug enforcement agent’s testimony that, based upon his experience and training, 130 grams of methamphetamine (the amount seized from the defendant) was more than generally possessed by mere users of the drug. The Eighth Circuit found no abuse of discretion in admitting the agent’s testimony: “Such testimony aids the jury by putting the drug dealer in context with the drug world. It is a reasonable assumption that a jury is not well versed in the behavior and average consumption of drug users.” <span class="citation" data-id="583690"><a href="/opinion/583690/united-states-v-terry-wilson/#810" aria-description="Citation for case: United States v. Terry Wilson"><em>Id. </em>at 810</a></span> (citation omitted); <em>see also United States v. Foster, </em><span class="citation" data-id="565036"><a href="/opinion/565036/united-states-v-derek-foster/#452" aria-description="Citation for case: United States v. Derek Foster">939 F.2d 445, 452</a></span> (7th Cir.1991) (noting that “jurors are not well versed in the behavior of drug dealers”). Here, too, the. district court properly admitted Johnston’s expert testimony.</p>
<p id="b689-10">
<em>IV. The District Judge’s Questioning of Witnesses</em>
</p>
<p id="b689-11">Gastiaburo has further contended that he was denied a fair trial because the district judge violated Rule 614 of the Federal Rules of Evidence by improperly questioning witnesses at trial. Gastiaburo has claimed that there was error in the judge’s questioning of Charles Pucci, Gastiaburo’s brother-in-law and the only witness whom Gastiaburo called at trial. At the end of the government’s cross-examination of Pucci, the judge asked him whether he typically sent $10,000 payments in cash via his brother-in-law (Gastiaburo), where he got the cash, what his occupation was, and whether he had ever been convicted of a felony. Gastiaburo did not object to those questions at trial.</p>
<p id="b689-12">Gastiaburo’s argument appears to come too late. The plain language of Rule 614(c) of the Federal Rules of Evidence requires objections to the trial judge’s interrogation of witnesses “[to] be made at the time or at the next available opportunity when the jury is not present.” Fed.R.Evid. 614(c). We, interpreting that rule, have held that “the failure of ... counsel to object to any of [the district judge’s] questioning at trial precludes our review of this issue on appeal.” <em>Stillman v. Norfolk &amp; W. Ry. Co., </em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/#839" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">811 F.2d 834, 839</a></span> (4th Cir.1987).</p>
<p id="b689-13"><em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">Stillman</a></span> </em>recognized a “limited exception” to the general rule against appellate review “‘[w]here a trial judge’s comments were so prejudicial as to deny a party an opportunity for a fair and impartial trial.’” <page-number citation-index="1" label="590">*590</page-number><em><span class="citation" data-id="483263"><a href="/opinion/483263/carl-r-stillman-v-norfolk-western-railway-company-a-corporation/" aria-description="Citation for case: Carl R. Stillman v. Norfolk &amp; Western Railway Company, a...">Id.</a></span> </em>(quoting <em>Miley v. Delta Marine Drilling Co., </em><span class="citation" data-id="308314"><a href="/opinion/308314/burns-miley-jr-v-delta-marine-drilling-company/#857" aria-description="Citation for case: Burns Miley, Jr. v. Delta Marine Drilling Company">473 F.2d 856, 857-58</a></span> (5th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./414/871/">414 U.S. 871</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./94/93/">94 S.Ct. 93</a></span>, <span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">38 L.Ed.2d 89</a></span> (1973)). In sketching the contours of that “limited exception,” we cited a case in which the judge interrupted the witness to answer the counsel’s question himself, referred to the question as one that “any five-year-old idiot” could answer, and then instructed counsel, “Don’t waste my time and the jury’s on that.” <em><span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">Id.</a></span> </em>(internal quotation marks omitted). Even those inflammatory and insulting comments were deemed <em>not </em>“sufficiently biased or notorious” to permit appellate review absent any objection at trial. <em><span class="citation" data-id="8987391"><a href="/opinion/8995064/thomas-v-estelle/" aria-description="Citation for case: Thomas v. Estelle">Id.</a></span></em></p>
<p id="b690-4">Clearly, none of the questions that Judge Ellis asked of Johnston (a topic dealt with above) even began to approach the level of “bias” or “notoriety” found in the above-cited example. The same can be said of Judge Ellis’s questioning of Pucci, with one qualification. Judge Ellis may appear to have overstepped the bounds of proper judicial interrogation when he asked the criminal defendant’s sole witness whether he had ever been convicted of a felony. Seen in the printed record, the absence of any particularized, good-faith basis made the question inappropriate.</p>
<p id="b690-5">However, while Judge Ellis’s final question of Pucci may have been improvident, it was not so prejudicial as to deny Gastiaburo the opportunity for a fair and impartial trial. Judge Ellis was not requested to retract the question. The answer to it, promptly given, was in the negative. Thus, Gastiaburo’s failure to object to Judge Ellis’s interrogation during the trial is fatal to his argument on appeal.</p>
<p id="b690-6">
<em>V. Ineffective Assistance of Counsel at Sentencing</em>
</p>
<p id="b690-7">Finally, Gastiaburo has contended that he was denied the effective assistance of counsel at sentencing when, after he claimed on the record that his trial counsel had been ineffective, his counsel failed to alloeute on his behalf.</p>
<p id="b690-8">A claim of ineffective assistance of counsel should be raised by motion under <span class="citation no-link">28 U.S.C. § 2255</span> in the district court and not on direct appeal, unless it “conclusively appears” from the record that defense counsel did not provide effective representation. <em>United States v. Fisher, </em><span class="citation" data-id="310396"><a href="/opinion/310396/united-states-v-ronald-richard-fisher/#302" aria-description="Citation for case: United States v. Ronald Richard Fisher">477 F.2d 300, 302</a></span> (4th Cir.1973) (citing <em>United States v. Mandello, </em><span class="citation" data-id="290322"><a href="/opinion/290322/united-states-v-mauro-m-mandello/#1023" aria-description="Citation for case: United States v. Mauro M. Mandello">426 F.2d 1021, 1023</a></span> (4th Cir.1970)); <em>see also United States v. DeFusco, </em><span class="citation" data-id="572183"><a href="/opinion/572183/united-states-v-david-allen-hagen-defusco-two-cases/#120" aria-description="Citation for case: United States v. David Allen Hagen Defusco, (Two Cases)">949 F.2d 114, 120-21</a></span> (4th Cir.1991), <em>cert. denied, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./112/1703/">112 S.Ct. 1703</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/118/412/">118 L.Ed.2d 412</a></span> (1992); <em>United States v. Percy, </em><span class="citation" data-id="454500"><a href="/opinion/454500/united-states-v-james-percy/#1205" aria-description="Citation for case: United States v. James Percy">765 F.2d 1199, 1205</a></span> (4th Cir.1985).</p>
<p id="b690-12">In the present case, the record on appeal does not conclusively demonstrate ineffective assistance of counsel. Therefore, we do not now address the issue on direct appeal. Gas-tiaburo may assert the claim in a § 2255 <em>habeas </em>motion, if he so chooses.</p>
<p id="b690-13">
<em>VI. Conclusion</em>
</p>
<p id="A-y">Accordingly, the judgment is</p>
<p id="Am_">
<em>AFFIRMED.</em>
</p>
<footnote label="*">
<p id="b688-12">The question presented here has only recently been discussed. At the time of Gastiaburo’s trial, the cases cited here had not yet been decided and published, with the exceptions of <em><span class="citation" data-id="544744"><a href="/opinion/544744/united-states-v-jaime-leon-gomez-norena/" aria-description="Citation for case: United States v. Jaime Leon Gomez-Norena">Gomez-Norena</a></span> </em>and <em><span class="citation" data-id="500424"><a href="/opinion/500424/united-states-v-marcelino-efrain-alvarez-jose-delgado-ramirez-juan-ramon/" aria-description="Citation for case: United States v. Marcelino Efrain Alvarez, Jose Delgado...">Alvarez</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Giordano.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "a2bacffbc563a201", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Giordano"}, "payload": {"all": [{"cite": "416 U.S. 505", "page": "505", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "416"}, {"cite": "94 S. Ct. 1820", "page": "1820", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "40 L. Ed. 2d 341", "page": "341", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "40"}, {"cite": "1974 U.S. LEXIS 36", "page": "36", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}], "display": "416 U.S. 505", "official": {"cite": "416 U.S. 505", "page": "505", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "416"}, "official_selection_present": true, "record_id": "United States v. Giordano"}}
{"assertion_id": "66f4b6a3a0574911", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Giordano"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Giordano", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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
