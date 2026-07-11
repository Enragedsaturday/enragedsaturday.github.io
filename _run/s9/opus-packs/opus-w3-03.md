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

## GROUP: _overhaul2/lake/cases/Colonnade Catering Corp. v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Colonnade Catering Corp. v. United States
type: case
citation: "397 U.S. 72 (1970)"
parallel_cite: "90 S. Ct. 774; 25 L. Ed. 2d 60"
neutral_cite: 1970 U.S. LEXIS 66
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-02-25
docket: 108
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
  opinion_url: "https://www.courtlistener.com/opinion/108077/colonnade-catering-corp-v-united-states/"
  cluster_id: 108077
  opinion_id: null
  identity_checked: true
lake:
  record_id: Colonnade Catering Corp. v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Foundational (closely-regulated-industry administrative search)"
related:
  - "[[United States v. Biswell]]"
  - "[[See v. City of Seattle]]"
  - "[[Camara v. Municipal Court]]"
  - "[[Donovan v. Dewey]]"
  - "[[New York v. Burger]]"
tags:
  - case
  - fourth-amendment
  - administrative-search
  - closely-regulated-industry
  - warrantless-inspection
  - special-needs
holding: "Because the liquor industry has long been subject to close federal supervision and inspection, Congress has broad authority to fashion warrantless inspection schemes for it; but where the governing statute punished a licensee's refusal to admit an inspector only with a fine and did not authorize forcible, warrantless entry, federal agents who broke the lock on a storeroom exceeded the statutory scheme, and the seized liquor had to be suppressed."
---

# Colonnade Catering Corp. v. United States

*397 U.S. 72 (1970)* (No. 108) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 108077 → 397 U.S. 72, No. 108, decided 1970-02-25 (Douglas, J.); Rule quotes string-matched to the CL opinion text 2026-07-07. -->

## Background
Colonnade, a New York catering business holding a federal retail liquor dealer's occupational tax stamp, was visited by federal agents who suspected that bottles were being refilled in violation of the excise laws. When the company president refused to unlock the liquor storeroom and asked for a warrant, an agent broke the lock, entered, and seized the liquor. Colonnade sued to recover and suppress it. The District Court ordered the liquor returned; the Second Circuit reversed.

## Issue
Whether federal agents, acting under liquor-inspection statutes that punish a dealer's refusal of entry with a fine, may forcibly enter a locked storeroom without a warrant to inspect a closely regulated liquor business.

## Rule
Writing for the Court, Justice Douglas held that the liquor industry's long regulatory pedigree gives Congress wide latitude to authorize inspections: "We agree that Congress has broad power to design such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand." — 397 U.S. at 76. ^pin-76

But that power must be exercised by statute: "Where Congress has authorized inspection but made no rules governing the procedure that inspectors must follow, the Fourth Amendment and its various restrictive rules apply." Dealing "here with the liquor industry long subject to close supervision and inspection," the Court found that "Congress selected a standard that does not include forcible entries without a warrant." — 397 U.S. at 77. ^pin-77

## Application
Because of the industry's history of close supervision, the general rule of *[[See v. City of Seattle|See]]* — that a warrant is required to compel an administrative entry on non-public commercial premises — did not automatically control. But the specific scheme Congress enacted resolved a refusal of entry by imposing a fine, not by authorizing a forcible, warrantless break-in. The agents who broke the storeroom lock therefore exceeded what Congress had authorized, and the seizure was unlawful.

## Conclusion
**Reversed.** Douglas, J., wrote for the Court; Burger, C.J. (joined by Black and Stewart, JJ.), dissented. The forcible warrantless entry was not authorized by the statutory inspection scheme.

## Treatment & subsequent history
**Good law — foundational.** *Colonnade*, together with *[[United States v. Biswell]]* (firearms dealers, 1972), is one of the two foundational closely-regulated-industry cases: it establishes that a long history of pervasive regulation can support a statutory warrantless-inspection regime. The doctrine matured through *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]* and *[[Donovan v. Dewey]]* and was organized into the three-part test of *[[New York v. Burger]]* (1987).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 108077 + 397 U.S. 72); renders under the ⚪ banner until S9 promotion. *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]* is not yet in the corpus and is named in plain text to avoid a dangling link.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Foundational (closely-regulated-industry administrative search)*

## Sources
- [*Colonnade Catering Corp. v. United States*, 397 U.S. 72 (1970)](https://www.courtlistener.com/opinion/108077/colonnade-catering-corp-v-united-states/) — pinpoints: 76 (congressional power to inspect the closely regulated liquor industry), 77 (statute authorized a fine, not forcible warrantless entry; Douglas, J.); quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d901acbfbb806d7d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Colonnade Catering Corp. v. United States"}, "payload": {"all": [{"cite": "397 U.S. 72", "page": "72", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "397"}, {"cite": "90 S. Ct. 774", "page": "774", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "25 L. Ed. 2d 60", "page": "60", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}, {"cite": "1970 U.S. LEXIS 66", "page": "66", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": "397 U.S. 72", "official": {"cite": "397 U.S. 72", "page": "72", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "397"}, "official_selection_present": true, "record_id": "Colonnade Catering Corp. v. United States"}}
{"assertion_id": "7e3c97891d2be6f2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Colonnade Catering Corp. v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Colonnade Catering Corp. v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Colonnade Catering Corp. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colonnade Catering Corp. v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Colonnade Catering Corp. v. United States",
    "case_name_short": "",
    "case_name_full": "Colonnade Catering Corp. v. United States",
    "input_case_name": "Colonnade Catering Corp. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-02-25",
    "year": 1970,
    "docket": "108",
    "cluster_id": 108077,
    "lead_opinion_id": 9424185,
    "sibling_ids": [],
    "absolute_url": "/opinion/108077/colonnade-catering-corp-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "397 U.S. 72",
      "volume": "397",
      "reporter": "U.S.",
      "page": "72",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 774",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "774",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 60",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 66",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "397 U.S. 72",
        "volume": "397",
        "reporter": "U.S.",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 774",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "774",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 60",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 66",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "397 U.S. 72",
    "official_selection": {
      "court_class": "scotus",
      "selected": "397 U.S. 72",
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
    "date_created": "2026-07-08T00:41:06Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "W10 on-read identity re-verification 2026-07-07: docket 108 confirmed verbatim from CL lead-opinion caption (html_with_citations)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "colonnade-catering-corp-v-united-states--108077",
      "to_record_id": "Colonnade Catering Corp. v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Colonnade Catering Corp. v. United States

```
<opinion type="majority">
<author id="b170-11">Mr. Justice Douglas</author>
<p id="Ag">delivered the opinion of the Court.</p>
<p id="b170-12">Petitioner, a licensee in New York authorized to serve alcoholic beverages and also the holder.of a federal retail liquor dealer’s occupational tax stamp, <span class="citation no-link">26 U. S. C. § 5121</span> (a), brought this suit to obtain the return of seized liquor and to suppress it as evidence. The District Court granted the relief. The Court of Appeals reversed. <span class="citation" data-id="284599"><a href="/opinion/284599/petition-of-the-colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Petition of the Colonnade Catering Corp. v. United States">410 F. 2d 197</a></span>. The case is here on a petition for writ of certiorari which we granted, <span class="citation multiple-matches"><a href="/c/U.%20S./396/814/">396 U. S. 814</a></span>, to review the decision in light of <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, and <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>.</p>
<p id="b170-13">Petitioner runs a catering agent, a member of the Alcohol and Tobacco Tax Divi<page-number citation-index="1" label="73">*73</page-number>sion of the Internal Revenue Service, was a guest at a party on petitioner’s premises and noted a possible violation of the federal excise tax law. When federal agents later visited the place, another party was in progress. They noticed that liquor was being served. Without the manager’s consent, they inspected the cellar. Then they asked the manager to open the locked liquor storeroom. He said that the only person authorized to open that room was one Rozzo, petitioner’s president, who was not on the premises. Later Rozzo arrived and refused to open the storeroom. He asked if the agents had a search warrant and they answered that they did not need one. When Rozzo continued to refuse to unlock the room, an agent broke the lock and entered. Then they removed the bottles of liquor now in controversy which they apparently suspected of being refilled contrary to the command of <span class="citation no-link">26 U. S. C. § 5301</span> (c).</p>
<p id="b171-4">It is provided in <span class="citation no-link">26 U. S. C. § 5146</span> (b)<footnotemark>1</footnotemark> and in <span class="citation no-link">26 U. S. C. § 7606</span> <footnotemark>2</footnotemark> that the Secretary of the Treasury or <page-number citation-index="1" label="74">*74</page-number>delegate has broad authority to enter and inspect the premises of retail dealers in liquors.<footnotemark>3</footnotemark> And in case of the refusal of a dealer to permit the inspection, it is provided <span class="citation no-link">26 U. S. C. § 7342</span>:</p>
<blockquote id="b172-5">“Any owner of any building or place, or person having the agency or superintendence of the same, who refuses to admit any officer or employee of the Treasury Department acting under the authority of section 7606 (relating to entry of premises for examination of taxable articles) or refuses to permit him examine such article or articles, shall, for every such refusal, forfeit $500.”</blockquote>
<p id="b172-6">The question is whether the imposition of a fine for refusal to permit entry — with the attendant consequences that violation of inspection laws may have in this closely regulated industry — is under this statutory scheme the exclusive sanction, absent a warrant to break and enter.</p>
<p id="b172-7">In <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#366" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 366-367</a></span>, a case involving an inspection under a municipal code, we said:</p>
<blockquote id="b172-8">“[The] inspector has no power to force entry and did not attempt it. A fine is imposed for resistance, but officials are not authorized to break past the unwilling occupant.”</blockquote>
<p id="b172-9"><em>Frank </em>v. <em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span> </em>was overruled in Camara v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>insofar as it permitted warrantless searches or inspections under municipal fire, health, and housing codes. The dictum that the provision for a fine on refusal to allow inspection made the use of force improper when there was no warrant was not disturbed ; and the question is whether that dictum contains the controlling principle<footnotemark>4</footnotemark> for this cáse.</p>
<p id="b173-3"><page-number citation-index="1" label="75">*75</page-number>The Government, emphasizing that the Fourth Amendment bans only “unreasonable searches and seizures,” <footnotemark>5</footnotemark> relies heavily on the long history of the regulation of the liquor industry during pre-Fourth Amendment days, first in England and later in the American Colonies. It is pointed out, for example, that in 1660 the precursor of modern-day liquor legislation was enacted in England<footnotemark>6</footnotemark> which allowed commissioners to enter, on demand, brewing houses at all times for inspection. Massachusetts had a similar law in 1692.<footnotemark>7</footnotemark> And in 1791, the year in which the Fourth Amendment was ratified, Congress imposed an excise tax on imported distilled spirits and on liquor distilled here,<footnotemark>8</footnotemark> under which law federal officers had broad powers to inspect distilling premises and the premises of the importer<footnotemark>9</footnotemark> without a warrant. From these and later laws and regulations governing the liquor industry, it is argued that Congress has been most solicitous in protecting the revenue against various types of fraud and to that end has repeatedly granted federal agents power to make warrantless searches and seizures of articles under the liquor laws.</p>
<p id="b174-4"><page-number citation-index="1" label="76">*76</page-number>The Court recognized the special treatment spection laws of this kind in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 624:</p>
<blockquote id="b174-5">“[I]n the case of excisable or dutiable articles, the government has an interest in them for the payment of the duties thereon, and until such duties paid has a right to keep them under observation, to pursue and drag them from concealment.”</blockquote>
<p id="b174-6">it added:</p>
<blockquote id="b174-7">“The seizure of stolen goods common law; and the seizure of goods forfeited for breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past; and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as 'unreasonable,’ and they are not embraced within the prohibition of the amendment.” <span class="citation no-link"><em>Id., </em>at 623</span>.</blockquote>
<p id="b174-8">We agree that Congress has broad power to such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand. The general rule laid down in <em>See </em>v. <em>City of <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Seattle, supra,</a></span> </em>at 545— “that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure” — is therefore not applicable here. In <em>See, </em><page-number citation-index="1" label="77">*77</page-number>we reserved decision on the problems of “licensing programs” requiring inspection, saying they can be resolved “on a case-by-case basis under the general Fourth Amendment standard of reasonableness.” <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#546" aria-description="Citation for case: See v. City of Seattle"><em>Id., </em>at 546</a></span>.</p>
<p id="b175-4">Where Congress has authorized inspection but made no rules governing the procedure that inspectors must follow, the Fourth Amendment and its various restrictive rules apply. We said in the <em>See </em>case:</p>
<blockquote id="b175-5">“The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property. The businessman, too, has that right placed in jeopardy if the decision to enter and inspect for violation of regulatory laws can be made and enforced by the inspector in the field without official authority evidenced by a warrant.” <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle"><em>Id., </em>at 543</a></span>.</blockquote>
<p id="b175-6">What was said in <em>See </em>reflects this Nation’s traditions that are strongly opposed to using force without definite authority to break down doors. We deal here with the liquor industry long subject to close supervision and inspection. As respects that industry, and its various branches including retailers, Congress has broad authority to fashion standards of reasonableness for searches and seizures. Under the existing statutes, Congress selected a standard that does not include forcible entries without a warrant. It resolved the issue, not by authorizing forcible, warrantless entries, but by making it an offense for a licensee to refuse admission to the inspector.</p>
<p id="b175-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b171-5"> <span class="citation no-link">26 U. S. C. § 5146</span> (b) provides:</p>
<p id="b171-6">or his delegate may enter during business hours premises (including places of storage) of any dealer for the purpose of inspecting or examining any records or other documents required to be kept by such dealer under this chapter or regulations issued pursuant thereto and any distilled spirits, wines, or beer or stored by such dealer on such premises.”</p>
</footnote>
<footnote label="2">
<p id="b171-7"> <span class="citation no-link">26 U. S. C. § 7606</span> provides:</p>
<p id="b171-8">“(a) Entry during day.</p>
<p id="b171-9">“The Secretary or his delegate may enter, in the daytime, any building or place where any articles or objects subject to tax are made, produced, or kept, so far as it may be necessary for the purpose of examining said articles or objects.</p>
<p id="b171-10">“(b) Entry at night.</p>
<p id="b171-11">are open Secretary or his delegate may enter them while so open, in the performance of his duties.”</p>
</footnote>
<footnote label="3">
<p id="b172-10"> As defined in <span class="citation no-link">26 U. S. C. § 5122</span> (a).</p>
</footnote>
<footnote label="4">
<p id="b172-11"> And see <em>United States </em>v. <em>Frisch, </em><span class="citation" data-id="6888050"><a href="/opinion/6989657/united-states-v-frisch/#662" aria-description="Citation for case: United States v. Frisch">140 F. 2d 660, 662</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b173-4"> The Fourth Amendment reads as follows:</p>
<blockquote id="b173-5">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall be violated, and no Warrants shall issue, but upon probable supported by Oath or affirmation, and particularly describing place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="6">
<p id="b173-6">. 23, § 19.</p>
</footnote>
<footnote label="7">
<p id="b173-7"> Act of June 24, 1692, Mass. Acts and Resolves, Vol. 1, 1692-p. 33, c. 5, § 8.</p>
</footnote>
<footnote label="8">
<p id="b173-8"> Act of March 3, 1791, <span class="citation no-link">1 Stat. 199</span>.</p>
</footnote>
<footnote label="9">
<p id="b173-9"> Section 29 of the Act of March 3, 1791, <span class="citation no-link">1 Stat. 206</span>, provided:</p>
<blockquote id="b173-10">officers of inspection of each survey at all times in the daytime, upon request, to enter into all every the houses, store-houses, ware-houses, buildings and which shall have been [registered] in manner aforesaid, and tasting, gauging or otherwise, to take an account of the quantity, and proofs of the said spirits therein contained; and also to samples thereof, paying for the same the usual price.”</blockquote>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Colorado v. Bertine.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Colorado v. Bertine"
type: case
citation: "479 U.S. 367 (1987)"
parallel_cite: "107 S. Ct. 738; 93 L. Ed. 2d 739; 55 U.S.L.W. 4105"
neutral_cite: 1987 U.S. LEXIS 286
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-14
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Bertine
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111788/colorado-v-bertine/"
  cluster_id: 111788
  opinion_id: 9430773
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Lafayette]]", "[[Florida v. Wells]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory-search", "impoundment", "standardized-criteria", "closed-container"]
holding: "Inventory searches (including opening closed containers) are permissible where police discretion is exercised according to standardized…"
lake:
  record_id: Colorado v. Bertine
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Bertine

*479 U.S. 367 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After arresting Bertine for driving under the influence, and before a tow truck arrived, a Boulder officer inventoried his van pursuant to police procedures, opening a closed backpack and the containers inside it and finding drugs, cash, and paraphernalia. Bertine moved to suppress, arguing the warrantless inventory of closed containers was unconstitutional.

## Issue
Whether police may, as part of a routine inventory of an impounded vehicle conducted under standardized procedures, open closed containers without a warrant or probable cause.

## Rule
Yes, where standardized procedures govern and the inventory is not a pretext for investigation. "[R]easonable police regulations relating to inventory procedures administered in good faith satisfy the Fourth Amendment, even though courts might as a matter of hindsight be able to devise equally reasonable rules requiring a different procedure." — 479 U.S. 367, 374. ^pin-374

Police discretion is permissible if cabined: "Nothing in *Opperman* or *Lafayette* prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity." — *Id.* at 375. ^pin-375

## Application
The Boulder officer inventoried Bertine's van and its closed containers pursuant to departmental procedures, exercising the choice to impound according to standardized criteria, and there was no showing the inventory was a ruse to investigate crime. Because the inventory and the opening of the containers followed good-faith standardized procedures on these facts, the search was reasonable.

## Conclusion
The inventory search, including the closed containers, was constitutional; the Colorado Supreme Court's suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Bertine* applies the inventory doctrine of [[South Dakota v. Opperman]] and [[Illinois v. Lafayette]]; [[Florida v. Wells]] later confirmed that standardized criteria must in fact govern the opening of containers, lest the inventory become a pretext for general rummaging.

## Appears on
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Colorado v. Bertine*, 479 U.S. 367 (1987) — https://www.courtlistener.com/opinion/111788/colorado-v-bertine/ — pinpoints: 374, 375.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "388788f288145e73", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Colorado v. Bertine"}, "payload": {"all": [{"cite": "479 U.S. 367", "page": "367", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "479"}, {"cite": "107 S. Ct. 738", "page": "738", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "93 L. Ed. 2d 739", "page": "739", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1987 U.S. LEXIS 286", "page": "286", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4105", "page": "4105", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "479 U.S. 367", "official": {"cite": "479 U.S. 367", "page": "367", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "479"}, "official_selection_present": true, "record_id": "Colorado v. Bertine"}}
{"assertion_id": "bd26fba682535c3f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-375", "record_id": "Colorado v. Bertine"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-375", "pinpoint_status": "slip-only", "quote": "Nothing in *Opperman* or *Lafayette* prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity.", "quote_fidelity": "mismatch", "record_id": "Colorado v. Bertine", "star_marker": null}}
{"assertion_id": "d1cde7f9568dd853", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-374", "record_id": "Colorado v. Bertine"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-374", "pinpoint_status": "slip-only", "quote": "--- # Colorado v. Bertine *479 U.S. 367 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After arresting Bertine for driving under the influence, and before a tow truck arrived, a Boulder officer inventoried his van pursuant to police procedures, opening a closed backpack and the containers inside it and finding drugs, cash, and paraphernalia. Bertine moved to suppress, arguing the warrantless inventory of closed containers was unconstitutional. ## Issue Whether police may, as part of a routine inventory of an impounded vehicle conducted under standardized procedures, open closed containers without a warrant or probable cause. ## Rule Yes, where standardized procedures govern and the inventory is not a pretext for investigation.", "quote_fidelity": "mismatch", "record_id": "Colorado v. Bertine", "star_marker": null}}
{"assertion_id": "efb073216c7da891", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Colorado v. Bertine"}, "payload": {"as_of_content": "1987-01-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Colorado v. Bertine", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Colorado v. Bertine

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Bertine",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Bertine",
    "case_name_short": "Bertine",
    "case_name_full": "Colorado v. Bertine",
    "input_case_name": "Colorado v. Bertine",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-14",
    "year": 1987,
    "docket": null,
    "cluster_id": 111788,
    "lead_opinion_id": 9430773,
    "sibling_ids": [
      111788,
      9430773,
      9430774,
      9430775
    ],
    "absolute_url": "/opinion/111788/colorado-v-bertine/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 367",
      "volume": "479",
      "reporter": "U.S.",
      "page": "367",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 738",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "738",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 739",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "739",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4105",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4105",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 286",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "286",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 367",
        "volume": "479",
        "reporter": "U.S.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 738",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "738",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 739",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "739",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 286",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "286",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4105",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4105",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 367",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 367",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-374",
      "page": null,
      "quote": "--- # Colorado v. Bertine *479 U.S. 367 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After arresting Bertine for driving under the influence, and before a tow truck arrived, a Boulder officer inventoried his van pursuant to police procedures, opening a closed backpack and the containers inside it and finding drugs, cash, and paraphernalia. Bertine moved to suppress, arguing the warrantless inventory of closed containers was unconstitutional. ## Issue Whether police may, as part of a routine inventory of an impounded vehicle conducted under standardized procedures, open closed containers without a warrant or probable cause. ## Rule Yes, where standardized procedures govern and the inventory is not a pretext for investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-375",
      "page": null,
      "quote": "Nothing in *Opperman* or *Lafayette* prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-01-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Bertine",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Charles E. Blake v. State of Mississippi",
          "cluster_id": 4541114,
          "cite": [
            "256 So. 3d 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4486934,
          "cite": [
            "2018 CO 27",
            "415 P.3d 815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4316369,
          "cite": [
            "2016 COA 150",
            "417 P.3d 868"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Weathers v. State of Indiana",
          "cluster_id": 4248521,
          "cite": [
            "61 N.E.3d 279",
            "2016 Ind. App. LEXIS 297",
            "2016 WL 4379346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Parks",
          "cluster_id": 4247757,
          "cite": [
            "2015 COA 158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeffrey Ray Cox v. State",
          "cluster_id": 4288224,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Wells",
          "cluster_id": 112412,
          "cite": [
            "109 L. Ed. 2d 1",
            "110 S. Ct. 1632",
            "495 U.S. 1",
            "1990 U.S. LEXIS 2035",
            "58 U.S.L.W. 4454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hendrickson",
          "cluster_id": 1135960,
          "cite": [
            "917 P.2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Redd",
          "cluster_id": 2387024,
          "cite": [
            "48 Cal. 4th 691",
            "229 P.3d 101",
            "108 Cal. Rptr. 3d 192",
            "2010 Cal. LEXIS 3749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scottie Ray Hurst",
          "cluster_id": 770650,
          "cite": [
            "228 F.3d 751",
            "2000 U.S. App. LEXIS 23606",
            "2000 WL 1363206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Lynn Cummins, United States of America v. Timothy Akins, A/K/A Michael Mayfield",
          "cluster_id": 552404,
          "cite": [
            "920 F.2d 498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1302221,
          "cite": [
            "973 P.2d 52",
            "83 Cal. Rptr. 2d 275",
            "20 Cal. 4th 119"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rahman",
          "cluster_id": 7078717,
          "cite": [
            "189 F.3d 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald James Causey",
          "cluster_id": 498394,
          "cite": [
            "834 F.2d 1179",
            "1987 U.S. App. LEXIS 17041",
            "1987 WL 23392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brenton-Farley",
          "cluster_id": 147727,
          "cite": [
            "607 F.3d 1294",
            "2010 U.S. App. LEXIS 11125",
            "2010 WL 2179617"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George M. Khoury, Howard Kluver, David W. West, Louis H. Chippas",
          "cluster_id": 540141,
          "cite": [
            "901 F.2d 948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zapata",
          "cluster_id": 195255,
          "cite": [
            "18 F.3d 971",
            "1994 WL 86216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzg3MzI0ODAwMDAwJnM9MjY0NjU3NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUmcz02MDA3NDEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 0,
        "triage_snippet_classified": 49
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
    "indexed_citing_opinions": 993,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111788,
        "count": 827,
        "count_source": "search"
      },
      {
        "opinion_id": 9430773,
        "count": 186,
        "count_source": "search"
      },
      {
        "opinion_id": 9430774,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430775,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1722,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-bertine.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTM0ODYmcz05NTc2MDY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111788,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 364699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 432054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1211186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1284293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1792609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 2051832,
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
    "date_created": "2026-07-05T00:34:24Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:39:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Bertine

```
<opinion type="majority">
<author id="b522-13">Chief Justice Rehnquist</author>
<p id="AGe">delivered the opinion of the Court.</p>
<p id="b522-14">On February 10, 1984, a police officer in Boulder, Colorado, arrested respondent Steven Lee Bertine for driving while under the influence of alcohol. After Bertine was taken into custody and before the arrival of a tow truck to take Bertine’s van to an impoundment lot,<footnotemark>1</footnotemark> a backup officer <page-number citation-index="1" label="369">*369</page-number>inventoried the contents of the van. The officer opened a closed backpack in which he found controlled substances, cocaine paraphernalia, and a large amount of cash. Bertine was subsequently charged with driving while under the influence of alcohol, unlawful possession of cocaine with intent to dispense, sell, and distribute, and unlawful possession of methaqualone. We are asked to decide whether the Fourth Amendment prohibits the State from proving these charges with the evidence discovered during the inventory of Ber-tine’s van. We hold that it does not.</p>
<p id="b523-5">The backup officer inventoried the van in accordance with local police procedures, which require a detailed inspection and inventory of impounded vehicles. He found the backpack directly behind the frontseat of the van. Inside the pack, the officer observed a nylon bag containing metal canisters. Opening the canisters, the officer discovered that they contained cocaine, methaqualone tablets, cocaine paraphernalia, and $700 in cash. In an outside zippered pouch of the backpack, he also found $210 in cash in a sealed envelope. After completing the inventory of the van, the officer had the van towed to an impound lot and brought the backpack, money, and contraband to the police station.</p>
<p id="b523-6">After Bertine was charged with the offenses described above, he moved to suppress the evidence found during the inventory search on the ground, <em>inter alia, </em>that the search of the closed backpack and containers exceeded the permissible scope of such a search under the Fourth Amendment. The Colorado trial court ruled that probable causé supported Bertine’s arrest and that the police officers had made the decisions to impound the vehicle and to conduct a thorough inventory search in good faith. Although noting that the inventory of the vehicle was performed in a “somewhat slipshod” manner, the District Court concluded that “the search of the backpack was done for the purpose of protecting the <page-number citation-index="1" label="370">*370</page-number>owner’s property, protection of the police from subsequent claims of loss or stolen property, and the protection of the police from dangerous instrumentalities.” App. 81-83. The court observed that the standard procedures for impounding vehicles mandated a “detailed inventory involving the opening of containers and the listing of [their] contents.” <em>Id., </em>at 81. Based on these findings, the court determined that the inventory search did not violate Bertine’s rights under the Fourth Amendment of the United States Constitution. <em>Id., </em>at 83. The court, nevertheless, granted Bertine’s motion to suppress, holding that the inventory search violated the Colorado Constitution.</p>
<p id="b524-5">On the State’s interlocutory appeal, the Supreme Court of Colorado affirmed. <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/" aria-description="Citation for case: People v. Bertine">706 P. 2d 411</a></span> (1985). In contrast to the District Court, however, the Colorado Supreme Court premised its ruling on the United States Constitution. The court recognized that in <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), we had held inventory searches of automobiles to be consistent with the Fourth Amendment, and that in <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983), we had held that the inventory search of personal effects of an arrestee at a police station was also permissible under that Amendment. The Supreme Court of Colorado felt, however, that our decisions in <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), and <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), holding searches of closed trunks and suitcases to violate the Fourth Amendment, meant that <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>did not govern this case.<footnotemark>2</footnotemark></p>
<p id="b524-6">We granted certiorari to consider the important and recurring question of federal law decided by the Colorado Supreme <page-number citation-index="1" label="371">*371</page-number>Court.<footnotemark>3</footnotemark> <span class="citation" data-id="9053299"><a href="/opinion/9059729/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">475 U. S. 1081</a></span> (1986). As that court recognized, inventory searches are now a well-defined exception to the warrant requirement of the Fourth Amendment. See <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#643" aria-description="Citation for case: Illinois v. Lafayette"><em>Lafayette, supra, </em>at 643</a></span>; <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 367-376</a></span>. The policies behind the warrant requirement are not implicated in an inventory search, <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 370, n. 5</a></span>, nor is the related concept of probable cause:</p>
<blockquote id="b525-5">“The standard of probable cause is peculiarly related to criminal investigations, not routine, noncriminal procedures. . . . The probable-cause approach is unhelpful when analysis centers upon the reasonableness of routine administrative caretaking functions, particularly when no claim is made that the protective procedures are a subterfuge for criminal investigations.” <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Ibid.</a></span></em></blockquote>
<p id="b525-6">See also <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 10, n. 5</a></span>. For these reasons, the Colorado Supreme Court’s reliance on <em>Arkansas </em>v. <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders, supra,</a></span> </em>and <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra,</a></span> </em>was incorrect. Both of these cases concerned searches solely for the purpose of investigating criminal conduct, with the validity of the searches therefore dependent on the application of the probable-cause and warrant requirements of the Fourth Amendment.</p>
<p id="b525-7">By contrast, an inventory search may be “reasonable” under the Fourth Amendment even though it is not conducted pursuant to a warrant based upon probable cause. In <page-number citation-index="1" label="372">*372</page-number><em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>, </em>this Court assessed the reasonableness of an inventory search of the glove compartment in an abandoned automobile impounded by the police. We found that inventory procedures serve to protect an owner’s property while it is in the custody of the police, to insure against claims of lost, stolen, or vandalized property, and to guard the police from danger. In light of these strong governmental interests and the diminished expectation of privacy in an automobile, we upheld the search. In reaching this decision, we observed that our cases accorded deference to police caretaking procedures designed to secure and protect vehicles and their contents within police custody. See <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447-448</a></span> (1973).<footnotemark>4</footnotemark></p>
<p id="b526-5">In our more recent decision, <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>a police officer conducted an inventory search of the contents of a shoulder bag in the possession of an individual being taken into custody. In deciding whether this search was reasonable, we recognized that the search served legitimate governmental interests similar to those identified in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>. </em>We determined that those interests outweighed the individual’s Fourth Amendment interests and upheld the search.</p>
<p id="b526-6">In the present case, as in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>there was no showing that the police, who were following standardized procedures, acted in bad faith or for the sole purpose of investigation. In addition, the governmental interests justifying the inventory searches in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>are <page-number citation-index="1" label="373">*373</page-number>nearly the same as those which obtain here. In each case, the police were potentially responsible for the property taken into their custody. By securing the property, the police protected the property from unauthorized interference. Knowledge of the precise nature of the property helped guard against claims of theft, vandalism, or negligence. Such knowledge also helped to avert any danger to police or others that may have been posed by the property.<footnotemark>5</footnotemark></p>
<p id="b527-5">The Supreme Court of Colorado opined that <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>was not controlling here because there was no danger of introducing contraband or weapons into a jail facility. Our opinion in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>however, did not suggest that the station-house setting of the inventory search was critical to our holding in that case. Both in the present case and in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>the common governmental interests described above were served by the inventory searches.</p>
<p id="b527-6">The Supreme Court of Colorado also expressed the view that the search in this case was unreasonable because Bertine’s van was towed to a secure, lighted facility and because Bertine himself could have been offered the opportunity to make other arrangements for the safekeeping of his property. But the security of the storage facility does not completely eliminate the need for inventorying; the police may still wish to protect themselves or the owners of the lot against false claims of theft or dangerous instrumentalities. And while giving Bertine an opportunity to make alterna<page-number citation-index="1" label="374">*374</page-number>tive arrangements would undoubtedly have been possible, we said in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>:</em></p>
<blockquote id="b528-5">“[T]he real question is not what ‘could have been achieved,’ but whether the Fourth Amendment <em>requires </em>such steps ....</blockquote>
<blockquote id="b528-6">“The reasonableness of any particular governmental activity does not necessarily or invariably turn on the existence of alternative ‘less intrusive’ means.” <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#647" aria-description="Citation for case: Illinois v. Lafayette">462 U. S., at 647</a></span> (emphasis in original).</blockquote>
<p id="b528-7">See <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 447</a></span>; <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557, n. 12</a></span> (1976). We conclude that here, as in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>reasonable police regulations relating to inventory procedures administered in good faith satisfy the Fourth Amendment, even though courts might as a matter of hindsight be able to devise equally reasonable rules requiring a different procedure.<footnotemark>6</footnotemark></p>
<p id="b528-8">The Supreme Court of Colorado also thought it necessary to require that police, before inventorying a container, weigh the strength of the individual’s privacy interest in the container against the possibility that the container might serve as a repository for dangerous or valuable items. We think that such a requirement is contrary to our decisions in <page-number citation-index="1" label="375">*375</page-number><em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>and by analogy to our decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982):</p>
<blockquote id="b529-5">“Even if less intrusive means existed of protecting some particular types of property, it would be unreasonable to expect police officers in the everyday course of business to make fine and subtle distinctions in deciding which containers or items may be searched and which must be sealed as a unit.” <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette"><em>Lafayette, supra, </em>at 648</a></span>.</blockquote>
<blockquote id="b529-6">“When a legitimate search is under way, and when its purpose and its limits have been precisely defined, nice distinctions between closets, drawers, and containers, in the case of a home, or between glove compartments, upholstered seats, trunks, and wrapped packages, in the case of a vehicle, must give way to the interest in the prompt and efficient completion of the task at hand.” <em>United States </em>v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 821</a></span>.</blockquote>
<p id="b529-7">We reaffirm these principles here: “‘[a] single familiar standard is essential to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.’ ” <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette, supra,</a></span> </em>at 648 (quoting <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981)).</p>
<p id="b529-8">Bertine finally argues that the inventory search of his van was unconstitutional because departmental regulations gave the police officers discretion to choose between impounding his van and parking and locking it in a public parking place. The Supreme Court of Colorado did not rely on this argument in reaching its conclusion, and we reject it. Nothing in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>or <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity. Here, the discretion afforded the Boulder police was exercised in light of <page-number citation-index="1" label="376">*376</page-number>standardized criteria, related to the feasibility and appropriateness of parking and locking a vehicle rather than impounding it.<footnotemark>7</footnotemark> There was no showing that the police chose to impound Bertine’s van in order to investigate suspected criminal activity.</p>
<p id="b530-5">While both <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>are distinguishable from the present case on their facts, we think that the principles enunciated in those cases govern the present one. The judgment of the Supreme Court of Colorado is therefore</p>
<p id="b530-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b522-16"><em> </em>Section 7-7-2(a)(4) of the Boulder Revised Code authorizes police officers to impound vehicles when drivers are taken into custody. Section 7-7-2(a)(4) provides:</p>
<blockquote id="b522-17">“A peace officer is authorized to remove or cause to be removed a vehicle from any street, parking lot, or driveway when:</blockquote>
<blockquote id="pAz0">[[Image here]]</blockquote>
<blockquote id="b523-7"><page-number citation-index="1" label="369">*369</page-number>(4) The driver of a vehicle is taken into custody by the police department.” Boulder Rev. Code § 7-7-2(a)(4)(1981).</blockquote>
</footnote>
<footnote label="2">
<p id="b524-7"> Two justices dissented from the majority opinion, arguing that <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em>Illinois </em>v. <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>compel the conclusion that the inventory search of the backpack found in Bertine’s van was permissible under the Fourth Amendment.</p>
</footnote>
<footnote label="3">
<p id="b525-8"> Since our decision in <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>, </em>several courts have confronted the issue whether police may inventory the contents of containers found in vehicles taken into police custody. See, <em>e. g., United States </em>v. <em>Griffin, </em><span class="citation" data-id="9471903"><a href="/opinion/432054/united-states-v-charles-e-griffin-and-jerome-griffin/" aria-description="Citation for case: United States v. Charles E. Griffin and Jerome Griffin">729 F. 2d 475</a></span> (CA7) (upholding inventory search of package found in paper bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/830/">469 U. S. 830</a></span> (1984); <em>United States </em>v. <em>Bloomfield, </em><span class="citation" data-id="364699"><a href="/opinion/364699/united-states-v-rick-thomas-bloomfield/" aria-description="Citation for case: United States v. Rick Thomas Bloomfield">594 F. 2d 1200</a></span> (CA8 1979) (affirming suppression of evidence found in closed knapsack); <em>People </em>v. <em>Braasch, </em><span class="citation" data-id="2051832"><a href="/opinion/2051832/people-v-braasch/" aria-description="Citation for case: People v. Braasch">122 Ill. App. 3d 747</a></span>, <span class="citation" data-id="2051832"><a href="/opinion/2051832/people-v-braasch/" aria-description="Citation for case: People v. Braasch">461 N. E. 2d 651</a></span> (1984) (upholding inventory of paper bag); <em>People </em>v. <em>Gonzalez, </em>62 N. Y. 2d 386, <span class="citation" data-id="5536314"><a href="/opinion/5687200/people-v-gonzalez/" aria-description="Citation for case: People v. Gonzalez">465 N. E. 2d 823</a></span> (1984) (upholding inventory of paper bag); <em>Boggs </em>v. <em>Commonwealth, </em><span class="citation" data-id="1211186"><a href="/opinion/1211186/boggs-v-commonwealth/" aria-description="Citation for case: Boggs v. Commonwealth">229 Va. 501</a></span>, <span class="citation" data-id="1211186"><a href="/opinion/1211186/boggs-v-commonwealth/" aria-description="Citation for case: Boggs v. Commonwealth">331 S. E. 2d 407</a></span> (1985) (upholding inventory of boxes and pouch found in bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./475/1031/">475 U. S. 1031</a></span> (1986).</p>
</footnote>
<footnote label="4">
<p id="b526-7"> The Colorado Supreme Court correctly stated that <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>did not address the question whether the scope of an inventory search may extend to closed containers located in the interior of an impounded vehicle. We did note, however, that “ ‘when the police take custody of any sort of container [such as] an automobile ... it is reasonable to search the container to itemize the property to be held by the police.’ ” 428 U. S., at 371 (quoting <em>United States </em>v. <em>Gravitt, </em><span class="citation" data-id="313366"><a href="/opinion/313366/united-states-v-jerry-eugene-gravitt/#378" aria-description="Citation for case: United States v. Jerry Eugene Gravitt">484 F. 2d 375, 378</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1135/">414 U. S. 1135</a></span> (1974)).</p>
</footnote>
<footnote label="5">
<p id="b527-7"> In arguing that the latter two interests are not implicated here, the dissent overlooks the testimony of the backup officer who conducted the inventory of Bertine’s van. According to the officer, the vehicle inventory procedures of the Boulder Police Department are designed for the “[p]ro-teetion of the police department” in the event that an individual later claims that “there was something of value taken from within the vehicle.” 2 Tr. 19. The officer added that inventories are also conducted in order to cheek “[f]or any dangerous items such as explosives [or] weapons.” Id., at 20. The officer testified that he had found such items in vehicles.</p>
</footnote>
<footnote label="6">
<p id="b528-9"> We emphasize that, in this case, the trial court found that the Police Department’s procedures mandated the opening of closed containers and the listing of their contents. Our decisions have always adhered to the requirement that inventories be conducted according to standardized criteria. See <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette">462 U. S., at 648</a></span>; <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#374" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 374-376</a></span>.</p>
<p id="b528-10">By quoting a portion <em>of </em>the Colorado Supreme Court’s decision out of context, the dissent suggests that the inventory here was not authorized by the standard procedures of the Boulder Police Department. See <em>post, </em>at 380-381. Yet that court specifically stated that the procedure followed here was “officially authorized.” <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/#413" aria-description="Citation for case: People v. Bertine">706 P. 2d 411, 413, n. 2</a></span> (1985). In addition, the court did not disturb the trial court’s finding that the police procedures for impounding vehicles required a detailed inventory of Bertine’s van. See <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/#418" aria-description="Citation for case: People v. Bertine"><em>id., </em>at 418-419</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b530-9"> In arguing that the Boulder Police Department procedures set forth no standardized criteria guiding an officer’s decision to impound a vehicle, the dissent selectively quotes from the police directive concerning the care and security of vehicles taken into police custody. The dissent fails to mention that the directive establishes several conditions that must be met before an officer may pursue the park-and-loek alternative. For example, police may not park and lock the vehicle where there is reasonable risk of damage or vandalism to the vehicle or where the approval of the arrestee cannot be obtained. App. 91-92, 94-95. Not only do such conditions circumscribe the discretion of individual officers, but they also protect the vehicle and its contents and minimize claims of property loss.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Colorado v. Connelly.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Colorado v. Connelly"
type: case
citation: "479 U.S. 157 (1986)"
parallel_cite: "107 S. Ct. 515; 93 L. Ed. 2d 473; 55 U.S.L.W. 4043"
neutral_cite: 1986 U.S. LEXIS 23
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-12-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Connelly
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111779/colorado-v-connelly/"
  cluster_id: 111779
  opinion_id: 9430748
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Arizona v. Fulminante]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "confessions", "voluntariness", "police-coercion", "state-action"]
holding: "A confession is \"involuntary\" for due-process purposes only when there is COERCIVE POLICE ACTIVITY; a suspect's mental illness or…"
lake:
  record_id: Colorado v. Connelly
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Connelly

*479 U.S. 157 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Connelly approached a Denver officer and, unprompted, confessed to a murder. He was later found to have been suffering from chronic schizophrenia and to have confessed in response to "command hallucinations" that he believed were the voice of God. The Colorado courts suppressed the statements as involuntary on the ground that his mental illness had overborne his free will, without any police misconduct.

## Issue
Whether a confession can be "involuntary" under the Due Process Clause based solely on the speaker's mental illness, absent any coercive police conduct.

## Rule
No; due-process involuntariness requires state coercion. "We hold that coercive police activity is a necessary predicate to the finding that a confession is not 'voluntary' within the meaning of the Due Process Clause of the Fourteenth Amendment." — 479 U.S. 157, 167. ^pin-167

A defendant's mental condition, by itself and apart from its relation to official coercion, does not make a confession involuntary; reliability concerns are governed by state evidence law, not the Due Process Clause.

## Application
Connelly's statements were the product of his psychosis, not of any pressure by the police, who had done nothing to elicit or coerce them. Because there was no coercive police activity linked to the confession, its admission did not violate due process on these facts, however impaired Connelly's decision to speak may have been.

## Conclusion
The confession was not constitutionally involuntary; the Colorado Supreme Court's suppression was reversed. Coercive police activity is the indispensable predicate of a due-process voluntariness claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Connelly* cabins the voluntariness line of [[Brown v. Mississippi]], [[Chambers v. Florida]], and [[Ashcraft v. Tennessee]] by requiring state coercion; [[Arizona v. Fulminante]] later subjected an erroneously admitted coerced confession to harmless-error review.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Colorado v. Connelly*, 479 U.S. 157 (1986) — https://www.courtlistener.com/opinion/111779/colorado-v-connelly/ — pinpoint: 167.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0acd0ab3195fb83d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Colorado v. Connelly"}, "payload": {"all": [{"cite": "479 U.S. 157", "page": "157", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "479"}, {"cite": "107 S. Ct. 515", "page": "515", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "93 L. Ed. 2d 473", "page": "473", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1986 U.S. LEXIS 23", "page": "23", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "55 U.S.L.W. 4043", "page": "4043", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "479 U.S. 157", "official": {"cite": "479 U.S. 157", "page": "157", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "479"}, "official_selection_present": true, "record_id": "Colorado v. Connelly"}}
{"assertion_id": "9ef146ff8f49cc58", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-167", "record_id": "Colorado v. Connelly"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-167", "pinpoint_status": "slip-only", "quote": "under the Due Process Clause based solely on the speaker's mental illness, absent any coercive police conduct. ## Rule No; due-process involuntariness requires state coercion.", "quote_fidelity": "mismatch", "record_id": "Colorado v. Connelly", "star_marker": null}}
{"assertion_id": "3b23b0137243b9fd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Colorado v. Connelly"}, "payload": {"as_of_content": "1986-12-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Colorado v. Connelly", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Colorado v. Connelly

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Connelly",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Connelly",
    "case_name_short": "Connelly",
    "case_name_full": "Colorado v. Connelly",
    "input_case_name": "Colorado v. Connelly",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-12-10",
    "year": 1986,
    "docket": null,
    "cluster_id": 111779,
    "lead_opinion_id": 9430748,
    "sibling_ids": [
      111779,
      9430748,
      9430749,
      9430750,
      9430751
    ],
    "absolute_url": "/opinion/111779/colorado-v-connelly/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9060076,
        "score": 20,
        "case_name": "Colorado v. Connelly"
      },
      {
        "cluster_id": 111587,
        "score": 20,
        "case_name": "Colorado v. Connelly"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 157",
      "volume": "479",
      "reporter": "U.S.",
      "page": "157",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 515",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 473",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4043",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4043",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 23",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 157",
        "volume": "479",
        "reporter": "U.S.",
        "page": "157",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 515",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 473",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 23",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "23",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4043",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4043",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 157",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 157",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-167",
      "page": null,
      "quote": "under the Due Process Clause based solely on the speaker's mental illness, absent any coercive police conduct. ## Rule No; due-process involuntariness requires state coercion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Connelly",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Baez",
          "cluster_id": 10283156,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barrett",
          "cluster_id": 4629724,
          "cite": [
            "442 P.3d 492"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex parte Lalonde",
          "cluster_id": 6243862,
          "cite": [
            "570 S.W.3d 716"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bourjaily v. United States",
          "cluster_id": 111938,
          "cite": [
            "97 L. Ed. 2d 144",
            "107 S. Ct. 2775",
            "483 U.S. 171",
            "1987 U.S. LEXIS 2874",
            "22 Fed. R. Serv. 1105",
            "55 U.S.L.W. 4962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 6883327,
          "cite": [
            "80 Ohio St. 3d 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
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
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Medina v. California",
          "cluster_id": 112775,
          "cite": [
            "120 L. Ed. 2d 353",
            "112 S. Ct. 2572",
            "505 U.S. 437",
            "1992 U.S. LEXIS 3696"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Maury",
          "cluster_id": 2598797,
          "cite": [
            "68 P.3d 1",
            "133 Cal. Rptr. 2d 561",
            "30 Cal. 4th 342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cockrell v. State",
          "cluster_id": 1517348,
          "cite": [
            "933 S.W.2d 73",
            "1996 Tex. Crim. App. LEXIS 182",
            "1996 WL 514836"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alvarado v. State",
          "cluster_id": 1676536,
          "cite": [
            "912 S.W.2d 199",
            "1995 Tex. Crim. App. LEXIS 116",
            "1995 WL 675552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beverly A. Seymour v. Diane Walker,respondent-Appellee",
          "cluster_id": 770145,
          "cite": [
            "224 F.3d 542",
            "2000 U.S. App. LEXIS 20170",
            "2000 WL 1154017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Glen Coe, Petitioner-Appellee/cross-Appellant v. Ricky Bell, Warden, Respondent-Appellant/cross-Appellee",
          "cluster_id": 759483,
          "cite": [
            "161 F.3d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leonard",
          "cluster_id": 6893283,
          "cite": [
            "104 Ohio St. 3d 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oursbourn v. State",
          "cluster_id": 2334003,
          "cite": [
            "259 S.W.3d 159",
            "2008 Tex. Crim. App. LEXIS 686",
            "2008 WL 2261744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Montoya",
          "cluster_id": 1202376,
          "cite": [
            "753 P.2d 729",
            "12 Brief Times Rptr. 482",
            "1988 Colo. LEXIS 39",
            "1988 WL 25119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lane v. State",
          "cluster_id": 1517312,
          "cite": [
            "933 S.W.2d 504",
            "1996 Tex. Crim. App. LEXIS 225",
            "1996 WL 649142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 2633370,
          "cite": [
            "29 P.3d 103",
            "111 Cal. Rptr. 2d 2",
            "26 Cal. 4th 876",
            "2001 D.A.R. 8853",
            "2001 Daily Journal DAR 8853",
            "2001 Cal. Daily Op. Serv. 7228",
            "2001 Cal. LEXIS 5263"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Guerra",
          "cluster_id": 2633286,
          "cite": [
            "129 P.3d 321",
            "40 Cal. Rptr. 3d 118",
            "37 Cal. 4th 1067",
            "2006 Cal. Daily Op. Serv. 1802",
            "2006 Daily Journal DAR 2547",
            "2006 Cal. LEXIS 2872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antwine",
          "cluster_id": 2364064,
          "cite": [
            "743 S.W.2d 51",
            "1987 Mo. LEXIS 374",
            "1987 WL 2721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Connelly:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUyODY3MjAwMDAwJnM9NDYwMDc4MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNzYmcz0yNDE3NTEyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
        "reviewed": 99,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 99,
        "triage_read": 1,
        "triage_snippet_classified": 98
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111779 OR 9430748 OR 9430749 OR 9430750 OR 9430751)",
    "indexed_citing_opinions": 2352,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111779,
        "count": 2044,
        "count_source": "search"
      },
      {
        "opinion_id": 9430748,
        "count": 338,
        "count_source": "search"
      },
      {
        "opinion_id": 9430749,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430750,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430751,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4020,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-connelly.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMDAzMzgmcz0xMDM0MDIzOCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111779+OR+9430748+OR+9430749+OR+9430750+OR+9430751%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111779,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 1153782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111779,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T00:39:03Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:43:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:39:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Connelly

```
<opinion type="majority">
<author id="b313-4"><page-number citation-index="1" label="159">*159</page-number>Chief Justice Rehnquist</author>
<p id="Akp">delivered the opinion of the Court.</p>
<p id="b313-5">In this case, the Supreme Court of Colorado held that the United States Constitution requires a court to suppress a confession when the mental state of the defendant, at the time he made the confession, interfered with his “rational intellect” and his “free will.” Because this decision seemed to conflict with prior holdings of this Court, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./474/1050/">474 U. S. 1050</a></span> (1986). We conclude that the admissibility of this kind of statement is governed by state rules of evidence, rather than by our previous decisions regarding coerced confessions and <em>Miranda </em>waivers. We therefore reverse.</p>
<p id="b314-3"><page-number citation-index="1" label="160">*160</page-number>I</p>
<p id="Adql">On August 18, 1983, Officer Patrick Anderson of the Denver Police Department was in uniform, working in an off-duty capacity in downtown Denver. Respondent Francis Connelly approached Officer Anderson and, without any prompting, stated that he had murdered someone and wanted to talk about it. Anderson immediately advised respondent that he had the right to remain silent, that anything he said could be used against him in court, and that he had the right to an attorney prior to any police questioning. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Respondent stated that he understood these rights but he still wanted to talk about the murder. Understandably bewildered by this confession, Officer Anderson asked respondent several questions. Connelly denied that he had been drinking, denied that he had been taking any drugs, and stated that, in the past, he had been a patient in several mental hospitals. Officer Anderson again told Connelly that he was under no obligation to say anything. Connelly replied that it was “all right,” and that he would talk to Officer Anderson because his conscience had been bothering him. To Officer Anderson, respondent appeared to understand fully the nature of his acts. Tr. 19.</p>
<p id="b314-4">Shortly thereafter, Homicide Detective Stephen Antuna arrived. Respondent was again advised of his rights, and Detective Antuna asked him “what he had on his mind.” <em>Id., </em>at 24. Respondent answered that he had come all the way from Boston to confess to the murder of Mary Ann Junta, a young girl whom he had killed in Denver sometime during November 1982. Respondent was taken to police headquarters, and a search of police records revealed that the body of an unidentified female had been found in April 1983. Respondent openly detailed his story to Detective Antuna and Sergeant Thomas Haney, and readily agreed to take the officers to the scene of the killing. Under Con-nelly’s sole direction, the two officers and respondent pro-<page-number citation-index="1" label="161">*161</page-number>eeeded in a police vehicle to the location of the crime. Respondent pointed out the exact location of the murder. Throughout this episode, Detective Antuna perceived no indication whatsoever that respondent was suffering from any kind of mental illness. <em>Id., </em>at 33-34.</p>
<p id="b315-5">Respondent was held overnight. During an interview with the public defender’s office the following morning, he became visibly disoriented. He began giving confused answers to questions, and for the first time, stated that “voices” had told him to come to Denver and that he had followed the directions of these voices in confessing. <em>Id., </em>at 42. Respondent was sent to a state hospital for evaluation. He was initially found incompetent to assist in his own defense. By March 1984, however, the doctors evaluating respondent determined that he was competent to proceed to trial.</p>
<p id="b315-6">At a preliminary hearing, respondent moved to suppress all of his statements. Dr. Jeffrey Metzner, a psychiatrist employed by the state hospital, testified that respondent was suffering from chronic schizophrenia and was in a psychotic state at least as of August 17, 1983, the day before he confessed. Metzner’s interviews with respondent revealed that respondent was following the “voice of God.” This voice instructed respondent to withdraw money from the bank, to buy an airplane ticket, and to fly from Boston to Denver. When respondent arrived from Boston, God’s voice became stronger and told respondent either to confess to the killing or to commit suicide. Reluctantly following the command of the voices, respondent approached Officer Anderson and confessed.</p>
<p id="b315-7">Dr. Metzner testified that, in his expert opinion, respondent was experiencing “command hallucinations.” <em>Id., </em>at 56. This condition interfered with respondent’s “volitional abilities; that is, his ability to make free and rational choices.” <em>Ibid. </em>Dr. Metzner further testified that Connelly’s illness did not significantly impair his cognitive abilities. Thus, respondent understood the rights he had when Officer Ander<page-number citation-index="1" label="162">*162</page-number>son and Detective Antuna advised him that he need not speak. <em>Id., </em>at 56-57. Dr. Metzner admitted that the “voices” could in reality be Connelly’s interpretation of his own guilt, but explained that in his opinion, Connelly’s psychosis motivated his confession.</p>
<p id="b316-5">On the basis of this evidence the Colorado trial court decided that respondent’s statements must be suppressed because they were “involuntary.” Relying on our decisions in <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), and <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568</a></span> (1961), the court ruled that a confession is admissible only if it is a product of the defendant’s rational intellect and “free will.” Tr. 88. Although the court found that the police had done nothing wrong or coercive in securing respondent’s confession, Connelly’s illness destroyed his volition and compelled him to confess. <em>Id., </em>at 89. The trial court also found that Connelly’s mental state vitiated his attempted waiver of the right to counsel and the privilege against compulsory self-incrimination. Accordingly, respondent’s initial statements and his custodial confession were suppressed. <em>Id., </em>at 90.</p>
<p id="b316-6">The Colorado Supreme Court affirmed. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/" aria-description="Citation for case: People v. Connelly">702 P. 2d 722</a></span> (1985). In that court’s view, the proper test for admissibility is whether the statements are “the product of a rational intellect and a free will.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#728" aria-description="Citation for case: People v. Connelly"><em>Id., </em>at 728</a></span>. Indeed, “the absence of police coercion or duress does not foreclose a finding of involuntariness. One’s capacity for rational judgment and free choice may be overborne as much by certain forms of severe mental illness as by external pressure.” <em><span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/" aria-description="Citation for case: People v. Connelly">Ibid.</a></span> </em>The court found that the very admission of the evidence in a court of law was sufficient state action to implicate the Due Process Clause of the Fourteenth Amendment to the United States Constitution. The evidence fully supported the conclusion that respondent’s initial statement was not the product of a rational intellect and a free will. The court then considered respondent’s attempted waiver of his constitutional rights and found that respondent’s mental condition precluded his <page-number citation-index="1" label="163">*163</page-number>ability to make a valid waiver. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly"><em>Id., </em>at 729</a></span>. The Colorado Supreme Court thus affirmed the trial court’s decision to suppress all of Connelly’s statements.</p>
<p id="b317-5">II</p>
<p id="b317-6">The Due Process Clause of the Fourteenth Amendment provides that no State shall “deprive any person of life, liberty, or property, without due process of law.” Just last Term, in <em>Miller </em>v. <em>Fenton, </em><span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#109" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 109</a></span> (1985), we held that by virtue of the Due Process Clause “certain interrogation techniques, either in isolation or as applied to the unique characteristics of a particular suspect, are so offensive to a civilized system of justice that they must be condemned.” See also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#432" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 432-434</a></span> (1986).</p>
<p id="b317-7">Indeed, coercive government misconduct was the catalyst for this Court’s seminal confession case, <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936). In that case, police officers extracted confessions from the accused through brutal torture. The Court had little difficulty concluding that even though the Fifth Amendment did not at that time apply to the States, the actions of the police were “revolting to the sense of justice.” <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi"><em>Id., </em>at 286</a></span>. The Court has retained this due process focus, even after holding, in <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), that the Fifth Amendment privilege against compulsory self-incrimination applies to the States. See <em>Miller </em>v. <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#109" aria-description="Citation for case: Miller v. Fenton"><em>Fenton, supra, </em>at 109-110</a></span>.</p>
<p id="b317-8">Thus the cases considered by this Court over the 50 years since <em>Brown </em>v. <em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi</a></span> </em>have focused upon the crucial element of police overreaching.<footnotemark>1</footnotemark> While each confession case <page-number citation-index="1" label="164">*164</page-number>has turned on its own set of factors justifying the conclusion that police conduct was oppressive, all have contained a substantial element of coercive police conduct. Absent police conduct causally related to the confession, there is simply no basis for concluding that any state actor has deprived a criminal defendant of due process of law.<footnotemark>2</footnotemark> Respondent correctly notes that as interrogators have turned to more subtle forms of psychological persuasion, courts have found the mental condition of the defendant a more significant factor in the “voluntariness” calculus. See <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959). But this fact does not justify a conclusion that a defendant’s mental condition, by itself and apart from its relation to official coercion, should ever dispose of the inquiry into constitutional “voluntariness.”</p>
<p id="b318-5">Respondent relies on <em>Blackburn </em>v. <em>Alabama, </em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199</a></span> (1960), and <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), for the proposition that the “deficient mental condition of the defendants in those cases was sufficient to render their confessions involuntary.” Brief for Respondent 20. But respondent’s reading of <em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Blackburn</a></span> </em>and <em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span> </em>ignores the integral element of police overreaching present in both cases. In <em><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Blackburn</a></span>, </em>the Court found that the petitioner was probably insane at the time of his confession and the police learned during the interrogation that he had a history of mental prob<page-number citation-index="1" label="165">*165</page-number>lems. The police exploited this weakness with coercive tactics: “the eight- to nine-hour sustained interrogation in a tiny room which was upon occasion literally filled with police officers; the absence of Blackburn’s friends, relatives, or legal counsel; [and] the composition of the confession by the Deputy Sheriff rather than by Blackburn.” <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#207" aria-description="Citation for case: Blackburn v. Alabama">361 U. S., at 207-208</a></span>. These tactics supported a finding that the confession was involuntary. Indeed, the Court specifically condemned police activity that “wrings a confession out of an accused against his will.” <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama"><em>Id., </em>at 206-207</a></span>. <em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span> </em>presented a similar instance of police wrongdoing. In that case, a police physician had given Townsend a drug with truth-serum properties. <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#298" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 298-299</a></span>. The subsequent confession, obtained by officers who knew that Townsend had been given drugs, was held involuntary. These two cases demonstrate that while mental condition is surely relevant to an individual’s susceptibility to police coercion, mere examination of the confessant’s state of mind can never conclude the due process inquiry.</p>
<p id="b319-5">Our “involuntary confession” jurisprudence is entirely consistent with the settled law requiring some sort of “state action” to support a claim of violation of the Due Process Clause of the Fourteenth Amendment. The Colorado trial court, of course, found that the police committed no wrongful acts, and that finding has been neither challenged by respondent nor disturbed by the Supreme Court of Colorado. The latter court, however, concluded that sufficient state action was present by virtue of the admission of the confession into evidence in a court of the State. <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#728" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 728-729</a></span>.</p>
<p id="b319-6">The difficulty with the approach of the Supreme Court of Colorado is that it fails to recognize the essential link between coercive activity of the State, on the one hand, and a resulting confession by a defendant, on the other. The flaw in respondent’s constitutional argument is that it would expand our previous line of “voluntariness” cases into a far-ranging requirement that courts must divine a defendant’s <page-number citation-index="1" label="166">*166</page-number>motivation for speaking or acting as he did even though there be no claim that governmental conduct coerced his decision.</p>
<p id="b320-5">The most outrageous behavior by a private party seeking to secure evidence against a defendant does not make that evidence inadmissible under the Due Process Clause. See <em>Walter </em>v. <em>United States, </em><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#656" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 656</a></span> (1980); <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-488</a></span> (1971); <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#476" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 476</a></span> (1921). We have also observed that “[j Jurists and scholars uniformly have recognized that the exclusionary rule imposes a substantial cost on the societal interest in law enforcement by its proscription of what concededly is relevant evidence.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#448" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 448-449</a></span> (1976). See also <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#627" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 627</a></span> (1980); <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Moreover, suppressing respondent’s statements would serve absolutely no purpose in enforcing constitutional guarantees. The purpose of excluding evidence seized in violation of the Constitution is to substantially deter future violations of the Constitution. See <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906-913</a></span> (1984). Only if we were to establish a brand new constitutional right — the right of a criminal defendant to confess to his crime only when totally rational and properly motivated — could respondent’s present claim be sustained.</p>
<p id="b320-6">We have previously cautioned against expanding “currently applicable exclusionary rules by erecting additional barriers to placing truthful and probative evidence before state juries . . . .” <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 488-489</a></span> (1972). We abide by that counsel now. “[T]he central purpose of a criminal trial is to decide the factual question of the defendant’s guilt or innocence,” <em>Delaware </em>v. <em>Van Arsdall, </em><span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#681" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673, 681</a></span> (1986), and while we have previously held that exclusion of evidence may be necessary to protect constitutional guarantees, both the necessity for the collateral inquiry and the exclusion of evidence deflect a criminal trial from its basic purpose. Respondent would now have us re<page-number citation-index="1" label="167">*167</page-number>quire sweeping inquiries into the state of mind of a criminal defendant who has confessed, inquiries quite divorced from any coercion brought to bear on the defendant by the State. We think the Constitution rightly leaves this sort of inquiry to be resolved by state laws governing the admission of evidence and erects no standard of its own in this area. A statement rendered by one in the condition of respondent might be proved to be quite unreliable, but this is a matter to be governed by the evidentiary laws of the forum, see, <em>e. g., </em>Fed. Rule Evid. 601, and not by the Due Process Clause of the Fourteenth Amendment. “The aim of the requirement of due process is not to exclude presumptively false evidence, but to prevent fundamental unfairness in the use of evidence, whether true or false.” <em>Lisenba </em>v. <em>California, </em><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span> (1941).</p>
<p id="b321-5">We hold that coercive police activity is a necessary predicate to the finding that a confession is not “voluntary” within the meaning of the Due Process Clause of the Fourteenth Amendment. We also conclude that the taking of respondent’s statements, and their admission into evidence, constitute no violation of that Clause.</p>
<p id="b321-6">III</p>
<p id="b321-7">A</p>
<p id="b321-8">The Supreme Court of Colorado went on to affirm the trial court’s ruling that respondent’s later statements made while in custody should be suppressed because respondent had not waived his right to consult an attorney and his right to remain silent. That court held that the State must bear its burden of proving waiver of these <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights by “clear and convincing evidence.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 729</a></span>. Although we have stated in passing that the State bears a “heavy” burden in proving waiver, <em>Tague </em>v. <em>Louisiana, </em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">444 U. S. 469</a></span> (1980) <em>(per curiam); North Carolina </em>v. <em>Butler </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 373</a></span> (1979); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>, we have never <page-number citation-index="1" label="168">*168</page-number>held that the “clear and convincing evidence” standard is the appropriate one.</p>
<p id="b322-5">In <em>Lego </em>v. <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Twomey, supra,</a></span> </em>this Court upheld a procedure in which the State established the voluntariness of a confession by no more than a preponderance of the evidence. We upheld it for two reasons. First, the voluntariness determination has nothing to do with the reliability of jury verdicts; rather, it is designed to determine the presence of police coercion. Thus, voluntariness is irrelevant to the presence or absence of the elements of a crime, which must be proved beyond a reasonable doubt. See <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970). Second, we rejected Lego’s assertion that a high burden of proof was required to serve the values protected by the exclusionary rule. We surveyed the various reasons for excluding evidence, including a violation of the requirements of <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>and we stated that “[i]n each instance, and without regard to its probative value, evidence is kept from the trier of guilt or innocence for reasons wholly apart from enhancing the reliability of verdicts.” <em>Lego </em>v. <em>Twomey, </em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#488" aria-description="Citation for case: Lego v. Twomey">404 U. S., at 488</a></span>. Moreover, we rejected the argument that “the importance of the values served by exclusionary rules is itself sufficient demonstration that the Constitution also requires admissibility to be proved beyond a reasonable doubt.” <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Ibid.</a></span> </em>Indeed, the Court found that “no substantial evidence has accumulated that federal rights have suffered from determining admissibility by a preponderance of the evidence.” <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Ibid.</a></span></em></p>
<p id="b322-6">We now reaffirm our holding in <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Lego</a></span>: </em>Whenever the State bears the burden of proof in a motion to suppress a statement that the defendant claims was obtained in violation of our <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>doctrine, the State need prove waiver only by a preponderance of the evidence. See <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#444" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 444</a></span>, and n. 5 (1984); <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#178" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 178, n. 14</a></span> (1974) (“[T]he controlling burden of proof at suppression hearings should impose no greater burden than proof by a preponderance of the evidence . . .”). <page-number citation-index="1" label="169">*169</page-number>Cf. <em>Moore </em>v. <em>Michigan, </em><span class="citation" data-id="9841953"><a href="/opinion/105589/moore-v-michigan/#161" aria-description="Citation for case: Moore v. Michigan">355 U. S. 155, 161-162</a></span> (1957). If, as we held in <em>Lego </em>v. <em><span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/" aria-description="Citation for case: Lego v. Twomey">Twomey, supra,</a></span> </em>the voluntariness of a confession need be established only by a preponderance of the evidence, then a waiver of the auxiliary protections established in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>should require no higher burden of proof. “[Exclusionary rules are very much aimed at deterring lawless conduct by police and prosecution and it is very doubtful that escalating the prosecution’s burden of proof in . . . suppression hearings would be sufficiently productive in this respect to outweigh the public interest in placing probative evidence before juries for the purpose of arriving at truthful decisions about guilt or innocence.” <em>Lego </em>v. <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey"><em>Twomey, supra, </em>at 489</a></span>. See also <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S., at 906-913</a></span>.</p>
<p id="b323-5">B</p>
<p id="b323-6">We also think that the Supreme Court of Colorado was mistaken in its analysis of the question whether respondent had waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights in this case.<footnotemark>3</footnotemark> Of course, a waiver must at a minimum be “voluntary” to be effective against an accused. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 444, 476</a></span>; <em>North Carolina </em>v. <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 373</a></span>. The Supreme Court of Colorado in addressing this question relied on the testimony of the court-appointed psychiatrist to the effect that respondent was not capable of making a “free decision with respect to his constitutional right of silence . . . and his constitutional right to confer with a lawyer before talking to the police.” <span class="citation" data-id="9538999"><a href="/opinion/1153782/people-v-connelly/#729" aria-description="Citation for case: People v. Connelly">702 P. 2d, at 729</a></span>.</p>
<p id="b323-7">We think that the Supreme Court of Colorado erred in importing into this area of constitutional law notions of “free will” that have no place there. There is obviously no reason to require more in the way of a “voluntariness” inquiry in the <page-number citation-index="1" label="170">*170</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver context than in the Fourteenth Amendment confession context. The sole concern of the Fifth Amendment, on which <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was based, is governmental coercion. See <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 460</a></span>. Indeed, the Fifth Amendment privilege is not concerned “with moral and psychological pressures to confess emanating from sources other than official coercion.” <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#305" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 305</a></span> (1985). The voluntariness of a waiver of this privilege has always depended on the absence of police overreaching, not on “free choice” in any broader sense of the word. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 421</a></span> (“[T]he relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion or deception. . . . [T]he record is devoid of any suggestion that police resorted to physical or psychological pressure to elicit the statements”); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#726" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 726-727</a></span> (1979) (The defendant was “not worn down by improper interrogation tactics or lengthy questioning or by trickery or deceit. . . . The officers did not intimidate or threaten respondent in any way. Their questioning was restrained and free from the abuses that so concerned the Court in <em>Miranda”).</em></p>
<p id="b324-5">. Respondent urges this Court to adopt his “free will” rationale, and to find an attempted waiver invalid Whenever the defendant feels compelled to waive his rights by reason of any compulsion, even if the compulsion does not flow from the police. But such a treatment of the waiver issue would “cut this Court’s holding in <em>[Miranda] </em>completely loose from its own explicitly stated rationale.” <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protects defendants against government coercion leading them to surrender rights protected by the Fifth Amendment; it goes no further than that. Respondent’s perception of coercion flowing from the “voice of God,” however important or significant such a <page-number citation-index="1" label="171">*171</page-number>perception may be in other disciplines, is a matter to which the United States Constitution does not speak.</p>
<p id="b325-14"><em>I </em>— i &lt;1</p>
<p id="b325-3">The judgment of the Supreme Court of Colorado is accordingly reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.<footnotemark>4</footnotemark></p>
<p id="b325-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b317-9"><em> E. g., Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978) (defendant subjected to 4-hour interrogation while incapacitated and sedated in intensive-care unit); <em>Greenwald </em>v. <em>Wisconsin, </em><span class="citation" data-id="9423651"><a href="/opinion/107650/greenwald-v-wisconsin/" aria-description="Citation for case: Greenwald v. Wisconsin">390 U. S. 519</a></span> (1968) (defendant, on medication, interrogated for over 18 hours without food or sleep); <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35</a></span> (1967) (police officers held gun to the head of wounded eonfessant to extract confession); <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span> (1966) (16 days of incommunicado interrogation in closed cell without windows, limited food, and coercive tactics); <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span> (1961) <page-number citation-index="1" label="164">*164</page-number>(defendant held for four days with inadequate food and medical attention until confession obtained); <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568</a></span> (1961) (defendant held for five days of repeated questioning during which police employed coercive tactics); <em>Payne </em>v. <em>Arkansas, </em><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958) (defendant held incommunicado for three days with little food; confession obtained when officers informed defendant that Chief of Police was preparing to admit lynch mob into jail); <em>Ashcraft </em>v. <em>Tennessee, </em><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944) (defendant questioned by relays of officers for 36 hours without an opportunity for sleep).</p>
</footnote>
<footnote label="2">
<p id="b318-7"> Even where there is causal connection between police misconduct and a defendant’s confession, it does not automatically follow that there has been a violation of the Due Process Clause. See, <em>e. g., Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969).</p>
</footnote>
<footnote label="3">
<p id="b323-8"> Petitioner conceded at oral argument that when Officer Anderson handcuffed respondent, the custody requirement of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was satisfied. For purposes of our decision we accept that concession, and we similarly assume that the police officers “interrogated” respondent within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="4">
<p id="b325-10"> It is possible to read the opinion of the Supreme Court of Colorado as finding respondent’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver invalid on other grounds. Even if that is the ease, however, we nonetheless reverse the judgment in its entirety because of our belief that the Supreme Court of Colorado’s analysis was influenced by its mistaken view of “voluntariness” in the constitutional sense. Reconsideration of other issues, not inconsistent with our opinion, is of course open to the Supreme Court of Colorado on remand.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Colorado v. Spring.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Colorado v. Spring"
type: case
citation: "479 U.S. 564 (1987)"
parallel_cite: "107 S. Ct. 851; 93 L. Ed. 2d 954; 55 U.S.L.W. 4162"
neutral_cite: 1987 U.S. LEXIS 418
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-27
docket: 85-1517
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Spring
  varies_by_point: false
  scope_note: Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111798/colorado-v-spring/"
  cluster_id: 111798
  opinion_id: 9430793
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Moran v. Burbine]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver"]
holding: "A Miranda waiver is knowing and intelligent even though police did not tell the suspect all of the crimes or subjects the interrogation would cover; awareness of every possible subject of questioning is not a prerequisite to a valid waiver, and silence about the subject matter is not trickery."
lake:
  record_id: Colorado v. Spring
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Spring

*479 U.S. 564 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spring was arrested by federal agents on firearms charges. After [[Miranda and Custodial Interrogation|Miranda warnings]], he waived his rights and answered questions; the agents also asked him about an unrelated Colorado murder, which he eventually admitted. Spring argued his waiver was invalid because the agents had not told him in advance that they intended to question him about the homicide.

## Issue
Whether a suspect's waiver of his [[Miranda and Custodial Interrogation|Miranda rights]] is rendered invalid (not knowing and intelligent) because the police did not inform him beforehand of all the subjects or offenses the interrogation would cover.

## Rule
No. A valid waiver requires that it be voluntary and that it be made with full awareness of the *nature* of the right abandoned and the consequences of doing so — not awareness of every tactical detail. "[A] suspect's awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege." — 479 U.S. at 577. ^pin-577

The *[[Miranda v. Arizona|Miranda]]* warnings themselves convey the nature of the privilege and the consequences of abandoning it (anything he says may be used against him), so a suspect need not also be told *which* crimes will be discussed. Mere police silence about the subject matter of the interrogation is not the kind of trickery or deception that would invalidate an otherwise valid waiver.

## Application
Spring received and understood the *[[Miranda v. Arizona|Miranda]]* warnings and voluntarily waived his rights. The agents' failure to forewarn him that they would also ask about the Colorado murder did not affect the knowing-and-intelligent character of that waiver: he knew he could remain silent and that anything he said could be used against him. His admissions were therefore the product of a valid waiver.

## Conclusion
The waiver was knowing and intelligent despite the suspect's ignorance of all the topics to be covered. The judgment of the Colorado Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Consistent with [[Moran v. Burbine]] (a waiver is not invalidated by the police withholding information — there, that an attorney was trying to reach the suspect): the validity of a *[[Miranda v. Arizona|Miranda]]* waiver turns on the suspect's understanding of the right itself, not on full information about the investigation.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Colorado v. Spring*, 479 U.S. 564 (1987) — https://www.courtlistener.com/opinion/111798/colorado-v-spring/ — pinpoint: 577.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b9fd12fca06b2bc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Colorado v. Spring"}, "payload": {"all": [{"cite": "479 U.S. 564", "page": "564", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "479"}, {"cite": "107 S. Ct. 851", "page": "851", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "93 L. Ed. 2d 954", "page": "954", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "93"}, {"cite": "1987 U.S. LEXIS 418", "page": "418", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4162", "page": "4162", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "479 U.S. 564", "official": {"cite": "479 U.S. 564", "page": "564", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "479"}, "official_selection_present": true, "record_id": "Colorado v. Spring"}}
{"assertion_id": "c9dc4abc72ea95f9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-577", "record_id": "Colorado v. Spring"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-577", "pinpoint_status": "slip-only", "quote": "--- # Colorado v. Spring *479 U.S. 564 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spring was arrested by federal agents on firearms charges. After Miranda warnings, he waived his rights and answered questions; the agents also asked him about an unrelated Colorado murder, which he eventually admitted. Spring argued his waiver was invalid because the agents had not told him in advance that they intended to question him about the homicide. ## Issue Whether a suspect's waiver of his Miranda rights is rendered invalid (not knowing and intelligent) because the police did not inform him beforehand of all the subjects or offenses the interrogation would cover. ## Rule No. A valid waiver requires that it be voluntary and that it be made with full awareness of the *nature* of the right abandoned and the consequences of doing so — not awareness of every tactical detail.", "quote_fidelity": "mismatch", "record_id": "Colorado v. Spring", "star_marker": null}}
{"assertion_id": "6cb65302205f7f4f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Colorado v. Spring"}, "payload": {"as_of_content": "1987-01-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Colorado v. Spring", "scope_note": "Good law.", "varies_by_point": false}}
```

### lake record — Colorado v. Spring

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Spring",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Spring",
    "case_name_short": "Spring",
    "case_name_full": "Colorado v. Spring",
    "input_case_name": "Colorado v. Spring",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-27",
    "year": 1987,
    "docket": "85-1517",
    "cluster_id": 111798,
    "lead_opinion_id": 9430793,
    "sibling_ids": [
      111798,
      9430793,
      9430794
    ],
    "absolute_url": "/opinion/111798/colorado-v-spring/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 564",
      "volume": "479",
      "reporter": "U.S.",
      "page": "564",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 851",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "851",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 954",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "954",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4162",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4162",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 418",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "418",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 564",
        "volume": "479",
        "reporter": "U.S.",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 851",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "851",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 954",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "954",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 418",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "418",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4162",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4162",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 564",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 564",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-577",
      "page": null,
      "quote": "--- # Colorado v. Spring *479 U.S. 564 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spring was arrested by federal agents on firearms charges. After Miranda warnings, he waived his rights and answered questions; the agents also asked him about an unrelated Colorado murder, which he eventually admitted. Spring argued his waiver was invalid because the agents had not told him in advance that they intended to question him about the homicide. ## Issue Whether a suspect's waiver of his Miranda rights is rendered invalid (not knowing and intelligent) because the police did not inform him beforehand of all the subjects or offenses the interrogation would cover. ## Rule No. A valid waiver requires that it be voluntary and that it be made with full awareness of the *nature* of the right abandoned and the consequences of doing so \u2014 not awareness of every tactical detail.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-01-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Spring",
    "varies_by_point": false,
    "scope_note": "Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Luis Fernando Ortiz",
          "cluster_id": 4472662,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Moore, 07ca093 (11-26-2008)",
          "cluster_id": 3983329,
          "cite": [
            "2008 Ohio 6238"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane1_negative"
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
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
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
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Male Juvenile (95-Cr-1074)",
          "cluster_id": 744606,
          "cite": [
            "121 F.3d 34",
            "1997 U.S. App. LEXIS 19219",
            "1997 WL 416548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyette",
          "cluster_id": 2544386,
          "cite": [
            "58 P.3d 391",
            "127 Cal. Rptr. 2d 544",
            "29 Cal. 4th 381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 6889013,
          "cite": [
            "92 Ohio St. 3d 146",
            "749 N.E.2d 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Mauro",
          "cluster_id": 111878,
          "cite": [
            "95 L. Ed. 2d 458",
            "107 S. Ct. 1931",
            "481 U.S. 520",
            "1987 U.S. LEXIS 1933"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Koedatich",
          "cluster_id": 2159212,
          "cite": [
            "548 A.2d 939",
            "112 N.J. 225",
            "1988 N.J. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Traylor v. State",
          "cluster_id": 1765408,
          "cite": [
            "596 So. 2d 957",
            "1992 WL 4873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Musselwhite",
          "cluster_id": 1225502,
          "cite": [
            "17 Cal. 4th 1216",
            "954 P.2d 475",
            "98 Daily Journal DAR 4745",
            "98 Cal. Daily Op. Serv. 3452",
            "74 Cal. Rptr. 2d 212",
            "1998 Cal. LEXIS 2622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee Moore v. Betty Mitchell",
          "cluster_id": 2981722,
          "cite": [
            "708 F.3d 760",
            "2013 U.S. App. LEXIS 3915",
            "2013 WL 673524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Van Tran",
          "cluster_id": 2428819,
          "cite": [
            "864 S.W.2d 465",
            "1993 Tenn. LEXIS 343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ian Gordon, United States of America v. Ian Gordon",
          "cluster_id": 536184,
          "cite": [
            "895 F.2d 932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leza v. State",
          "cluster_id": 2541167,
          "cite": [
            "351 S.W.3d 344",
            "2011 Tex. Crim. App. LEXIS 1372",
            "2011 WL 4809816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. State",
          "cluster_id": 1706879,
          "cite": [
            "739 So. 2d 568",
            "1999 WL 506949"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wash",
          "cluster_id": 1158185,
          "cite": [
            "861 P.2d 1107",
            "6 Cal. 4th 215",
            "24 Cal. Rptr. 2d 421",
            "93 Cal. Daily Op. Serv. 8554",
            "93 Daily Journal DAR 14629",
            "1993 Cal. LEXIS 5807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Goodwin",
          "cluster_id": 1667339,
          "cite": [
            "774 N.W.2d 733",
            "278 Neb. 945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brenton-Farley",
          "cluster_id": 147727,
          "cite": [
            "607 F.3d 1294",
            "2010 U.S. App. LEXIS 11125",
            "2010 WL 2179617"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ripkowski v. State",
          "cluster_id": 1588890,
          "cite": [
            "61 S.W.3d 378",
            "2001 Tex. Crim. App. LEXIS 98",
            "2001 WL 1360126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 1190445,
          "cite": [
            "839 P.2d 984",
            "3 Cal. 4th 959",
            "13 Cal. Rptr. 2d 475",
            "92 Daily Journal DAR 15770",
            "92 Cal. Daily Op. Serv. 9338",
            "1992 Cal. LEXIS 5500"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Humphrey",
          "cluster_id": 2588759,
          "cite": [
            "132 P.3d 352",
            "2006 WL 988349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Spring:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111798 OR 9430793 OR 9430794) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjIzNDI0MDAwMDAwJnM9MjkzOTkzNSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111798+OR+9430793+OR+9430794%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111798 OR 9430793 OR 9430794)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTEmcz0xNzQyMDIzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111798+OR+9430793+OR+9430794%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111798 OR 9430793 OR 9430794)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111798 OR 9430793 OR 9430794)",
    "indexed_citing_opinions": 627,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111798,
        "count": 546,
        "count_source": "search"
      },
      {
        "opinion_id": 9430793,
        "count": 89,
        "count_source": "search"
      },
      {
        "opinion_id": 9430794,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1070,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-spring.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyNTA2OTUmcz05Mzk3NjI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111798+OR+9430793+OR+9430794%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111798,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 291902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 334838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 388110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 392980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 431718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111798,
        "cited_id": 2605185,
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
    "date_created": "2026-07-05T00:43:36Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:47:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:43:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Spring

```
<opinion type="majority">
<author id="b720-6">Justice Powell</author>
<p id="A9W">delivered the opinion of the Court.</p>
<p id="b720-7">In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court held that a suspect's waiver of the Fifth Amendment privilege against self-incrimination is valid only if it is made voluntarily, knowingly, and intelligently. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. This case presents the question whether the suspect’s awareness of all the crimes about which he may be questioned is relevant to determining the validity of his decision to waive the Fifth Amendment privilege.</p>
<p id="b720-8">I</p>
<p id="b720-9">In February 1979, respondent John Leroy Spring and a companion shot and killed Donald Walker during a hunting trip in Colorado. Shortly thereafter, an informant told agents of the Bureau of Alcohol, Tobacco, and Firearms (ATF) that Spring was engaged in the interstate transportation of stolen firearms. The informant also told the agents that Spring had discussed his participation in the Colorado killing. At the time the ATF agents received this information, Walker’s body had not been found and the police had received no report of his disappearance. Based on the information received from the informant relating to the firearms violations, the ATF agents set up an undercover operation to purchase firearms from Spring. On March 30, 1979, ATF agents arrested Spring in Kansas City, Missouri, during the undercover purchase.</p>
<p id="b721-4"><page-number citation-index="1" label="567">*567</page-number>An ATF agent on the scene of the arrest advised Spring of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.<footnotemark>1</footnotemark> Spring was advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights a second time after he was transported to the ATF office in Kansas City. At the ATF office, the agents also advised Spring that he had the right to stop the questioning at any time or to stop the questioning until the presence of an attorney could be secured. Spring then signed a written form stating that he understood and waived his rights, and that he was willing to make a statement and answer questions.</p>
<p id="b721-5">ATF agents first questioned Spring about the firearms transactions that led to his arrest. They then asked Spring if he had a criminal record. He admitted that he had a juvenile record for shooting his aunt when he was 10 years old. The agents asked if Spring had ever shot anyone else. Spring ducked his head and mumbled, “I shot another guy once.” The agents asked Spring if he had ever been to Colorado. Spring said no. The agents asked Spring whether he had shot a man named Walker in Colorado and thrown his body into a snowbank. Spring paused and then ducked his head again and said no. The interview ended at this point.</p>
<p id="b721-6">On May 26, 1979, Colorado law enforcement officials visited Spring while he was in jail in Kansas City pursuant to his arrest on the firearms offenses. The officers gave Spring the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, and Spring again signed a written form indicating that he understood his rights and was willing to waive them. The officers informed Spring that they wanted to question him about the Colorado homicide. Spring indicated that he “wanted to get it off his chest.” In an interview that lasted approximately IV2 hours, Spring confessed to the Colorado murder. During that time, Spring <page-number citation-index="1" label="568">*568</page-number>talked freely to the officers, did not indicate a desire to terminate the questioning, and never requested counsel. The officers prepared a written statement summarizing the interview. Spring read, edited, and signed the statement.</p>
<p id="b722-5">Spring was charged in Colorado state court with first-degree murder. Spring moved to suppress both statements on the ground that his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights was invalid. The trial court found that the ATF agents’ failure to inform Spring before the March 30 interview that they would question him about the Colorado murder did not affect his waiver of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights:</p>
<blockquote id="b722-6">“[T]he questions themselves suggested the topic of inquiry. The questions dealt with ‘shooting anyone’ and specifically killing a man named Walker and throwing his body in a snowbank in Colorado. The questions were not designed to gather information relating to a subject that was not readily evident or apparent to Spring. Spring had been advised of his right to remain silent, his right to stop answering questions, and to have an Attorney present during interrogation. He did not elect to exercise his right to remain silent or to refuse to answer questions relating to the homicide, nor did he request Counsel during interrogation.” App. to Pet. for Cert. 4-A.</blockquote>
<p id="b722-7">Accordingly, the trial court concluded that the March 30 statement should not be suppressed on Fifth Amendment grounds. The trial court, however, subsequently ruled that Spring’s statement that he “shot another guy once” was irrelevant, and that the context of the discussion did not support the inference that the statement related to the Walker homicide. For that reason, the March 30 statement was not admitted at Spring’s trial. The court concluded that the May 26 statement “was made freely, voluntarily, and intelligently, after [Spring’s] being properly and fully advised of his rights, and that the statement should not be suppressed, but should <page-number citation-index="1" label="569">*569</page-number>be admitted in evidence.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 5-A. The May 26 statement was admitted into evidence at trial, and Spring was convicted of first-degree murder.<footnotemark>2</footnotemark></p>
<p id="b723-5">Spring argued on appeal that his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights before the March 30 statement was invalid because he was not informed that he would be questioned about the Colorado murder. Although this statement was not introduced at trial, he claimed that its validity was relevant because the May 26 statement that was admitted against him was the illegal “fruit” of the March 30 statement, see <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), and therefore should have been suppressed. The Colorado Court of Appeals agreed with Spring, holding that the ATF agents “had a duty to inform Spring that he was a suspect, or to readvise him of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, before questioning him about the murder.” <span class="citation" data-id="9790096"><a href="/opinion/2605185/people-v-spring/#966" aria-description="Citation for case: People v. Spring">671 P. 2d 965, 966</a></span> (1983). Because they failed to do so before the March 30 interview, “any waiver of rights in regard to questions designed to elicit information about Walker’s death was not given knowingly or intelligently.” <span class="citation" data-id="9790096"><a href="/opinion/2605185/people-v-spring/#967" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 967</a></span>. The court held that the March 30 statement was inadmissible and that the State had failed to meet its burden of proving that the May 26 statement was not the product of the prior illegal statement. The court reversed Spring’s conviction and remanded the case for a new trial, directing that if the State sought to introduce the May 26 statement into evidence, the trial court should determine whether the “taint” of <page-number citation-index="1" label="570">*570</page-number>the March 30 statement was sufficiently attenuated to allow introduction of the May 26 statement.</p>
<p id="b724-5">The Colorado Supreme Court affirmed the judgment of the Court of Appeals, although its reasoning differed in some respects. <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/" aria-description="Citation for case: People v. Spring">713 P. 2d 865</a></span> (1985). The court found:</p>
<blockquote id="b724-6">“[T]he validity of Spring’s waiver of constitutional rights must be determined upon an examination of the totality of the circumstances surrounding the making of the statement to determine if the waiver was voluntary, knowing and intelligent. No one factor is always determinative in that analysis. Whether, and to what extent, a suspect has been informed or is aware of the subject matter of the interrogation prior to its commencement is simply one factor in the court’s evaluation of the total circumstances, although it may be a major or even a determinative factor in some situations.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#872" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 872-873</a></span> (citations omitted).</blockquote>
<p id="b724-7">The <em>court </em>concluded:</p>
<blockquote id="b724-8">“Here, the absence of an advisement to Spring that he would be questioned about the Colorado homicide, and the lack of any basis to conclude that at the time of the execution of the waiver, he reasonably could have expected that the interrogation would extend to that subject, <em>are </em>determinative factors in undermining the validity of the waiver.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#874" aria-description="Citation for case: People v. Spring"><em>Id., </em>at 874</a></span> (emphasis in original).</blockquote>
<p id="b724-9">Justice Erickson, joined by Justice Rovira, dissented as to the resolution of this issue, stating:</p>
<blockquote id="b724-10">“Law enforcement officers have no duty under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to inform a person in custody of all charges being investigated prior to questioning him. All that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires is that the suspect be advised that he has the right <em>to </em>remain silent, that anything he says can and will be used against him in court, that he has the right to consult with a lawyer and to have the lawyer present during interrogation, and that if he cannot afford a law<page-number citation-index="1" label="571">*571</page-number>yer one will be appointed to represent him.” <em>Id., </em>at 880 (citations omitted).</blockquote>
<p id="b725-5">The dissenting justices found “ample evidence to support the trial court’s conclusion that Spring waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights” and rejected “the majority’s conclusion that Spring’s waiver of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights on March 30, 1979 was invalid simply because he was not informed of all matters that would be reviewed when he was questioned by the police.” <em>Id., </em>at 881. The court remanded the case for further proceedings consistent with its opinion.</p>
<p id="b725-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./476/1104/">476 U. S. 1104</a></span> (1986), to resolve an arguable Circuit conflict<footnotemark>3</footnotemark> and to review the Colorado Supreme Court’s determination that a suspect’s awareness of the possible subjects of questioning is a relevant and sometimes determinative consideration in assessing whether a waiver of the Fifth Amendment privilege is valid. We now reverse.</p>
<p id="b725-7">II</p>
<p id="b725-8">There is no dispute that the police obtained the May 26 confession after complete <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and after informing Spring that he would be questioned about the Colorado homicide. The Colorado Supreme Court nevertheless held that the confession should have been suppressed because it was the illegal “fruit” of the March 30 statement. A confession cannot be “fruit of the poisonous tree” if the tree itself is not <page-number citation-index="1" label="572">*572</page-number>poisonous. Our inquiry, therefore, centers on the validity of the March 30 statement.<footnotemark>4</footnotemark></p>
<p id="b726-4">A</p>
<p id="b726-5">The Fifth Amendment of the United States Constitution provides that no person “shall be compelled in any criminal case to be a witness against himself.”<footnotemark>5</footnotemark> This privilege “is fully applicable during a period of custodial interrogation.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#460" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 460-461</a></span>.<footnotemark>6</footnotemark> In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the Court concluded that “without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">Id., at 467</a></span>. Accordingly, the Court formulated the now-familiar “procedural safeguards effective to secure the privilege against self-incrimination.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. The Court’s fundamental aim in designing the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings was “to assure that the individual’s right to choose between silence and speech remains unfettered throughout the interrogation process.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 469</a></span>.</p>
<p id="b726-6">Consistent with this purpose, a suspect may waive his Fifth Amendment privilege, “provided the waiver is made voluntarily, knowingly and intelligently.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>. In this case, the law enforcement officials twice informed Spring <page-number citation-index="1" label="573">*573</page-number>of his Fifth Amendment privilege in precisely the manner specified by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>As we have noted, Spring indicated that he understood the enumerated rights and signed a written form expressing his intention to waive his Fifth Amendment privilege. The trial court specifically found that “there was no element of duress or coercion used to induce Spring’s statements [on March 30, 1978].” App. to Pet. for Cert. 3-A. Despite the explicit warnings and the finding by the trial court, Spring argues that his March 30 statement was in effect compelled in violation of his Fifth Amendment privilege because he signed the waiver form without being aware that he would be questioned about the Colorado homicide. Spring’s argument strains the meaning of compulsion past the breaking point.</p>
<p id="b727-5">B</p>
<p id="b727-6">A statement is not “compelled” within the meaning of the Fifth Amendment if an individual “voluntarily, knowingly and intelligently” waives his constitutional privilege. <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 444</a></span>. The inquiry whether a waiver is coerced “has two distinct dimensions.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 421</a></span> (1986):</p>
<blockquote id="b727-7">“First the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness both of the nature of the right being abandoned and the consequences of the decision to abandon it. Only if the ‘totality of the circumstances surrounding the interrogation’ reveal both an uncoerced choice and the requisite level of comprehension may a court properly conclude that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights have been waived.” <em>Ibid, </em>(quoting <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#725" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 725</a></span> (1979)).</blockquote>
<p id="b727-8">There is no doubt that Spring’s decision to waive his Fifth Amendment privilege was voluntary. He alleges no “coer<page-number citation-index="1" label="574">*574</page-number>cion of a confession by physical violence or other deliberate means calculated to break [his] will,” <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312</a></span> (1985), and the trial court found none. His allegation that the police failed to supply him with certain information does not relate to any of the traditional indicia of coercion: “the duration and conditions of detention . . . , the manifest attitude of the police toward him, his physical and mental state, the diverse pressures which sap or sustain his powers of resistance and self-control.” <em>Culombe </em>v. <em>Connecticut, </em><span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (opinion of Frankfurter, J.). Absent evidence that Spring’s “will [was] overborne and his capacity for self-determination critically impaired” because of coercive police conduct, <em>ibid.; </em>see <em>Colorado </em>v. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#163" aria-description="Citation for case: Colorado v. Connelly">479 U. S. 157, 163-164</a></span> (1986), his waiver of his Fifth Amendment privilege was voluntary under this Court’s decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b728-5">There also is no doubt that Spring’s waiver of his Fifth Amendment privilege was knowingly and intelligently made: that is, that Spring understood that he had the right to remain silent and that anything he said could be used as evidence against him. The Constitution does not require that a criminal suspect know and understand every possible consequence of a waiver of the Fifth Amendment privilege. <em>Moran </em>v. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 422</a></span>; <em>Oregon </em>v. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad"><em>Elstad, supra, </em>at 316-317</a></span>. The Fifth Amendment’s guarantee is both simpler and more fundamental: A defendant may not be compelled to be a witness against himself in any respect. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings protect this privilege by ensuring that a suspect knows that he may choose not to talk to law enforcement officers, to talk only with counsel present, or to discontinue talking at any time. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings ensure that a waiver of these rights is knowing and intelligent by requiring that the suspect be fully advised of this constitutional privilege, including the critical advice that whatever he chooses to say may be used as evidence against him.</p>
<p id="b729-6"><page-number citation-index="1" label="575">*575</page-number>In this case there is no allegation that Spring failed to understand the basic privilege guaranteed by the Fifth Amendment. Nor is there any allegation that he misunderstood the consequences of speaking freely to the law enforcement officials. In sum, we think that the trial court was indisputably correct in finding that Spring’s waiver was made knowingly and intelligently within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b729-7">hH b-1</p>
<p id="b729-1">A</p>
<p id="Apm">Spring relies on this Court’s statement in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that “any evidence that the accused was threatened, tricked, or cajoled into a waiver will. . . show that the defendant did not voluntarily waive his privilege. ” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. He contends that the failure to inform him of the potential subjects of interrogation constitutes the police trickery and deception condemned in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>thus rendering his waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights invalid. Spring, however, reads this statement in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>out of context and without due regard to the constitutional privilege the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were designed to protect.</p>
<p id="b729-2">We note first that the Colorado courts made no finding of official trickery.<footnotemark>7</footnotemark> In fact, as noted above, the trial court expressly found that “there was no element of duress or coercion used to induce Spring’s statements.” <em>Supra, </em>at 573. <page-number citation-index="1" label="576">*576</page-number>Spring nevertheless insists that the failure of the ATF agents to inform him that he would be questioned about the murder constituted official “trickery” sufficient to invalidate his waiver of his Fifth Amendment privilege, even if the official conduct did not amount to “coercion.” Even assuming that Spring’s proposed distinction has merit, we reject his conclusion. This Court has never held that mere silence by law enforcement officials as to the subject matter of an interrogation is “trickery” sufficient to invalidate a suspect’s waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and we expressly decline so to hold today.<footnotemark>8</footnotemark></p>
<p id="b730-5">Once <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are given, it is difficult to see how official silence could cause a suspect to misunderstand the nature of his constitutional right — “his right to refuse to answer any question which might incriminate him.” <em>United States </em>v. Washington, <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). “Indeed, it seems self-evident that one who is told he is free to refuse to answer questions is in a curious posture to later complain that his answers were compelled.” <em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/" aria-description="Citation for case: United States v. Washington">Ibid.</a></span> </em>We have held that a valid waiver does not require that an individual be informed of all information “useful” in making his decision or all information that “might . . . affec[t] his decision to confess.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 422</a></span>. “[W]e have never read the Constitution to require that the police supply a suspect with a flow of information to help him calibrate his self-interest in <page-number citation-index="1" label="577">*577</page-number>deciding whether to speak or stand by his rights.” <em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Ibid.</a></span></em><footnotemark><em>9</em></footnotemark><em> </em>Here, the additional information could affect only the wisdom of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver, not its essentially voluntary and knowing nature. Accordingly, the failure of the law enforcement officials to inform Spring of the subject matter of the interrogation could not affect Spring’s decision to waive his Fifth Amendment privilege in a constitutionally significant manner.</p>
<p id="b731-10">B</p>
<p id="b731-11">This Court’s holding in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>specifically required that the police inform a criminal suspect that he has the right to remain silent and that <em>anything </em>he says may be used against him. There is no qualification of this broad and explicit warning. The warning, as formulated in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>conveys to a suspect the nature of his constitutional privilege and the consequences of.abandoning it. Accordingly, we hold that a suspect’s awareness of all the possible subjects of questioning in advance of interrogation is not relevant to determining whether the suspect voluntarily, knowingly, and intelligently waived his Fifth Amendment privilege.</p>
<p id="b731-12">f — I &lt;1</p>
<p id="b731-3">The judgment of the Colorado Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b731-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b721-7"> Under this Court’s decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), prior to a custodial interrogation a criminal suspect must “be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b723-6"> Spring also moved to suppress a third statement made on July 13, 1979, after he had pleaded guilty to the federal firearms offenses and after an information charging him with murder had been issued in Colorado. The Colorado Supreme Court unanimously concluded that the statement should be suppressed because the questioning officials made no effort “to reaffirm Spring’s decision to waive his constitutional rights after he declined to answer particular questions.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#878" aria-description="Citation for case: People v. Spring">713 P. 2d 865, 878</a></span> (1985). We granted certiorari only on the question whether the second statement should have been admitted into evidence. <span class="citation multiple-matches"><a href="/c/U.%20S./476/1104/">476 U. S. 1104</a></span> (1986). Accordingly, the admissibility of the third statement is not before us.</p>
</footnote>
<footnote label="3">
<p id="b725-9"> The Colorado Supreme Court followed the lead of several Federal Courts of Appeals in holding that a suspect’s awareness of the subject matter of the interrogation is one factor to be considered in determining whether a waiver of the Fifth Amendment privilege is valid. <em>United States </em>v. <em>Burger, </em><span class="citation" data-id="431718"><a href="/opinion/431718/united-states-v-tibor-burger-aka-tom-singer/#141" aria-description="Citation for case: United States v. Tibor Burger, A/K/A &quot;Tom Singer&quot;">728 F. 2d 140, 141</a></span> (CA2 1984); <em>Carter </em>v. <em>Garrison, </em><span class="citation" data-id="392980"><a href="/opinion/392980/andrew-thomas-carter-sr-v-sam-p-garrison-attorney-general-of-the-state/#70" aria-description="Citation for case: Andrew Thomas Carter, Sr. v. Sam P. Garrison Attorney...">656 F. 2d 68, 70</a></span> (CA4 1981) <em>(per curiam), </em>cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./455/952/">455 U. S. 952</a></span> (1982); <em>United States </em>v. <em>McCrary, </em><span class="citation" data-id="9467693"><a href="/opinion/388110/united-states-v-billy-ray-mccrary/#328" aria-description="Citation for case: United States v. Billy Ray McCrary">643 F. 2d 323, 328</a></span> (CA5 1981). Other Courts of Appeals have found that a suspect’s awareness of the subject matter of interrogation is not a relevant factor in determining the validity of a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver. <em>United States </em>v. <em>Anderson, </em>175 U. S. App. D. C. 75, 77, n. 3, <span class="citation" data-id="334838"><a href="/opinion/334838/united-states-v-willie-anderson/#1212" aria-description="Citation for case: United States v. Willie Anderson">533 F. 2d 1210, 1212, n. 3</a></span> (1976); <em>United States </em>v. <em>Campbell, </em><span class="citation" data-id="291902"><a href="/opinion/291902/united-states-v-william-scott-campbell/#99" aria-description="Citation for case: United States v. William Scott Campbell">431 F. 2d 97, 99, n. 1</a></span> (CA9 1970).</p>
</footnote>
<footnote label="4">
<p id="b726-7"> The State argued for the first time in its petition for rehearing to the Colorado Supreme Court that this Court’s decision in <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), renders the May 26 statement admissible without regard to the validity of the March 30 waiver. The Colorado Supreme Court noted that the State would be free to make this argument to the trial court on remand. <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#876" aria-description="Citation for case: People v. Spring">713 P. 2d, at 876</a></span>. The question whether our decision in <em>Oregon </em>v. <em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span> </em>provides an independent basis for admitting the May 26 statement therefore is not before us in this case.</p>
</footnote>
<footnote label="5">
<p id="b726-9"> This privilege is applicable to the States through the Due Process Clause of the Fourteenth Amendment of the Constitution. <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964).</p>
</footnote>
<footnote label="6">
<p id="b726-10"> The State does not dispute that the statement at issue was obtained during a “custodial interrogation” within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="7">
<p id="b729-3"> The trial court found: “Though it is true that [the ATF agents] did not specifically advise Spring that a part of their interrogation would include questions about the Colorado homicide, the questions themselves suggested the topic of inquiry.” App. to Pet. for Cert. 4-A. According to the Colorado Supreme Court, “It is unclear whether Spring was told by the agents that they wanted to question him specifically about the firearms violations for which he was arrested or whether the agents simply began questioning Spring without making any statement concerning the subject matter of the interrogation. What is clear is that the agents did not tell Spring that they were going to ask him questions about the killing of Walker before Spring made his original decision to waive his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.” <span class="citation" data-id="9562845"><a href="/opinion/1209392/people-v-spring/#871" aria-description="Citation for case: People v. Spring">713 P. 2d, at 871</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b730-6"> In certain circumstances, the Court has found affirmative misrepresentations by the police sufficient to invalidate a suspect’s waiver of the Fifth Amendment privilege. See, <em>e. g., Lynumn </em>v. <em>Illinois, </em><span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span> (1963) (misrepresentation by police officers that a suspect would be deprived of state financial aid for her dependent child if she failed to cooperate with authorities rendered the subsequent confession involuntary); <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959) (misrepresentation by the suspect’s friend that the friend would lose his job as a police officer if the suspect failed to cooperate rendered his statement involuntary). In this case, we are not confronted with an affirmative misrepresentation by law enforcement officials as to the scope of the interrogation and do not reach the question whether a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights would be valid in such a circumstance.</p>
</footnote>
<footnote label="9">
<p id="b731-7"> Such an extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>would spawn numerous problems of interpretation because any number of factors could affect a suspect’s decision to waive his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The requirement would also vitiate to a great extent the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule’s important “virtue of informing police and prosecutors with specificity” as to how a pretrial questioning of a suspect must be conducted. <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979).</p>
</footnote>
</opinion>
```

---
