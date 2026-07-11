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

## GROUP: _overhaul2/lake/cases/McDonough v. Smith.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: McDonough v. Smith
type: case
citation: "588 U.S. 109 (2019)"
parallel_cite: "139 S. Ct. 2149; 204 L. Ed. 2d 506"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2019
date_decided: 2019-06-20
docket: No. 18-485
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
  opinion_url: "https://www.courtlistener.com/opinion/9231241/mcdonough-v-smith/"
  cluster_id: 9231241
  opinion_id: null
  identity_checked: true
lake:
  record_id: McDonough v. Smith
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Illustrates a circuit split
related:
  - "[[Malicious Prosecution under the Fourth Amendment]]"
  - "[[Heck v. Humphrey]]"
tags:
  - case
  - section-1983
  - fabricated-evidence
  - statute-of-limitations
  - accrual
  - malicious-prosecution
  - circuit-split
holding: "The statute of limitations on a § 1983 claim that the plaintiff was prosecuted using fabricated evidence does not begin to run until the criminal proceedings against him terminate in his favor — for McDonough, when he was acquitted at his second trial; the Court did not decide the elements or constitutional source of a fabricated-evidence claim."
aliases:
  - McDonough v. Smith
  - "McDonough v. Smith (2019)"
---

# McDonough v. Smith

*588 U.S. 109 (2019)* (No. 18-485) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9231241 → lead opinion 9226046 (Sotomayor, J.; 588 U.S. 109, decided June 20, 2019). frontier-split row (role: illustrates a circuit split) — split framing named in Treatment (accrual settled; the claim's elements/constitutional source left open and divided). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 139 S. Ct. 2149), so the pin is to 139 S. Ct. at 2161 (the conclusion follows page-label `*2161`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Edward McDonough, a commissioner of a county board of elections, was prosecuted for forging absentee ballots. He was tried twice — the first trial ended in a mistrial, and he was acquitted at the second. McDonough then sued the special district attorney, Youel Smith, under § 1983, alleging Smith had fabricated evidence used against him. He filed suit within three years of his acquittal, but more than three years after the fabricated evidence was used against him. The Second Circuit held the claim time-barred, treating it as having accrued when McDonough learned of and was injured by the fabrication.

## Issue
When the [[Common Legal Terms#statute-of-limitations|statute of limitations]] begins to run on a § 1983 claim alleging that the plaintiff was prosecuted using fabricated evidence.

## Rule
Analogizing to the common-law tort of malicious prosecution and to the accrual logic of *[[Heck v. Humphrey]]*, the Court held: "The statute of limitations for McDonough's § 1983 claim alleging that he was prosecuted using fabricated evidence began to run when the criminal proceedings against him terminated in his favor — that is, when he was acquitted at the end of his second trial." — 139 S. Ct. at 2161. ^pin-2161

## Application
The most natural common-law analogy, malicious prosecution, requires favorable termination and does not accrue while the prosecution is pending. The same practical considerations that led the Court to defer accrual in *[[Heck v. Humphrey|Heck]]* apply: allowing a fabricated-evidence suit to proceed during an ongoing prosecution would invite parallel civil litigation collaterally attacking the criminal case and risk conflicting judgments. A defendant's proper course is to defend at trial and, if convicted, attack the conviction through appeal or collateral review — so his § 1983 claim for the fabrication does not accrue until the proceedings end in his favor. The Court reversed the limitations ruling and, importantly, declined to define the elements or the constitutional basis of a fabricated-evidence claim, deciding only accrual.

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Sotomayor, J., delivered the opinion of the Court; Thomas, J. (joined by Kagan and Gorsuch, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. This is a **circuit-split** entry, and its posture must be taught precisely. *McDonough* is **binding** on one question — accrual: a § 1983 fabricated-evidence claim accrues on favorable termination of the criminal proceedings. But the Court expressly **reserved** the harder questions, and the courts of appeals remain **divided** on them: whether a fabricated-evidence claim is grounded in the Fourth Amendment or in the Due Process Clause, and what its elements are. The [[Common Legal Terms#dissenting-opinion|dissent]] objected that the Court fixed accrual without first defining the claim. Teach *McDonough* as settling accrual while flagging the live split over the claim's constitutional source and elements — binding as to accrual, persuasive/unsettled as to the rest.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Illustrates a circuit split*

## Sources
- [*McDonough v. Smith*, 588 U.S. 109 (2019)](https://www.courtlistener.com/opinion/9231241/mcdonough-v-smith/) — pinpoint: 139 S. Ct. 2149, 2161 (Sotomayor, J., for the Court; the CL opinion text is paginated to the parallel S. Ct. reporter, with the conclusion following the page-label `*2161` — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3c6c9ffd99d61724", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "McDonough v. Smith"}, "payload": {"all": [{"cite": "588 U.S. 109", "page": "109", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "588"}, {"cite": "139 S. Ct. 2149", "page": "2149", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}, {"cite": "204 L. Ed. 2d 506", "page": "506", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "204"}], "display": "588 U.S. 109", "official": {"cite": "588 U.S. 109", "page": "109", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "588"}, "official_selection_present": true, "record_id": "McDonough v. Smith"}}
{"assertion_id": "2c08a4db56780612", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "McDonough v. Smith"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "McDonough v. Smith", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — McDonough v. Smith

```json
{
  "schema_version": "s2.v1",
  "record_id": "McDonough v. Smith",
  "status": "under_review",
  "identity": {
    "case_name": "McDonough v. Smith",
    "case_name_short": "McDonough",
    "case_name_full": "Edward G. MCDONOUGH v. Youel SMITH, Individually and as Special District Attorney for the County of Rensselaer, New York, aka Trey Smith",
    "input_case_name": "McDonough v. Smith",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-06-20",
    "year": 2019,
    "docket": "No. 18-485",
    "cluster_id": 9231241,
    "lead_opinion_id": 9226046,
    "sibling_ids": [],
    "absolute_url": "/opinion/9231241/mcdonough-v-smith/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4631414,
        "score": 110,
        "case_name": "McDonough v. Smith"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "588 U.S. 109",
      "volume": "588",
      "reporter": "U.S.",
      "page": "109",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 2149",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 506",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "506",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "588 U.S. 109",
        "volume": "588",
        "reporter": "U.S.",
        "page": "109",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 2149",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 506",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "506",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "588 U.S. 109",
    "official_selection": {
      "court_class": "scotus",
      "selected": "588 U.S. 109",
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
    "date_created": "2026-07-06T13:47:43Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "mcdonough-v-smith--9231241",
      "to_record_id": "McDonough v. Smith",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — McDonough v. Smith

```
<opinion type="majority">
<author id="p-10">Justice SOTOMAYOR delivered the opinion of the Court.</author>
<p id="p-11"><a class="page-label" data-citation-index="1" data-label="2153" href="#p2153" id="p2153">*2153</a>Petitioner Edward McDonough alleges that respondent Youel Smith fabricated evidence and used it to pursue criminal charges against him. McDonough was acquitted, then sued Smith under <extracted-citation index="0" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>. The courts below, concluding that the limitations period for McDonough's fabricated-evidence claim began to run when the evidence was used against him, determined that the claim was untimely. We hold that the limitations period did not begin to run until McDonough's acquittal, and therefore reverse.</p>
<p id="p-12">I</p>
<p id="p-13">This case arises out of an investigation into forged absentee ballots that were submitted in a primary election in Troy, New York, in 2009. McDonough, who processed the ballots in his capacity as a commissioner of the county board of elections, maintains that he was unaware that they had been forged. Smith was specially appointed to investigate and to prosecute the matter.</p>
<p id="p-14">McDonough's complaint alleges that Smith then set about scapegoating McDonough <a class="page-label" data-citation-index="1" data-label="2154" href="#p2154" id="p2154">*2154</a>(against whose family Smith harbored a political grudge), despite evidence that McDonough was innocent. Smith leaked to the press that McDonough was his primary target and pressured him to confess. When McDonough would not, Smith allegedly fabricated evidence in order to inculpate him. Specifically, McDonough alleges that Smith falsified affidavits, coached witnesses to lie, and orchestrated a suspect DNA analysis to link McDonough to relevant ballot envelopes.</p>
<p id="p-15">Relying in part on this allegedly fabricated evidence, Smith secured a grand jury indictment against McDonough. McDonough was arrested, arraigned, and released (with restrictions on his travel) pending trial. Smith brought the case to trial a year later, in January 2012. He again presented the allegedly fabricated testimony during this trial, which lasted more than a month and ended in a mistrial. Smith then reprosecuted McDonough. The second trial also lasted over a month, and again, Smith elicited allegedly fabricated testimony. The second trial ended with McDonough's acquittal on all charges on December 21, 2012.</p>
<p id="p-16">On December 18, 2015, just under three years after his acquittal, McDonough sued Smith and other defendants under § 1983 in the U. S. District Court for the Northern District of New York. Against Smith, McDonough asserted two different constitutional claims: one for fabrication of evidence, and one for malicious prosecution without probable cause. The District Court dismissed the malicious prosecution claim as barred by prosecutorial immunity, though timely. It dismissed the fabricated-evidence claim, however, as untimely.</p>
<p id="p-17">McDonough appealed to the U. S. Court of Appeals for the Second Circuit, which affirmed. <extracted-citation case-ids="12517957" index="1" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">898 F.3d 259</a></span></extracted-citation> (2018). The Court of Appeals agreed with the District Court's disposition of the malicious prosecution claim. As for the timeliness of the fabricated-evidence claim, because all agreed that the relevant limitations period is three years, <em><extracted-citation case-ids="12517957" index="2" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12517957" index="2" url="https://cite.case.law/f3d/898/259/"> at 265</extracted-citation>, the question was when that limitations period began to run: upon McDonough's acquittal, or at some point earlier. In essence, given the dates at issue, McDonough's claim was timely only if the limitations period began running at acquittal.</p>
<p id="p-18">The Court of Appeals held that McDonough's fabricated-evidence claim accrued, and thus the limitations period began to run, "when (1) McDonough learned that the evidence was false and was used against him during the criminal proceedings; and (2) he suffered a loss of liberty as a result of that evidence." <em>Ibid</em> . This rule, in the Second Circuit's view, followed from its conclusion that a plaintiff has a complete fabricated-evidence claim as soon as he can show that the defendant's knowing use of the fabricated evidence caused him some deprivation of liberty. <em><extracted-citation case-ids="12517957" index="3" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12517957" index="3" url="https://cite.case.law/f3d/898/259/"> at 266</extracted-citation>. Those events undisputedly had occurred by the time McDonough was arrested and stood trial. <em>Ibid</em> .</p>
<p id="p-19">As the Second Circuit acknowledged, <em>id</em> ., at 267, other Courts of Appeals have held that the statute of limitations for a fabricated-evidence claim does not begin to run until favorable termination of the challenged criminal proceedings.<footnotemark>1</footnotemark> We granted certiorari to resolve the conflict, 586 U. S. ----, <extracted-citation case-ids="12624625,12624626,12624627,12624628,12624629,12624630" index="4" url="https://cite.case.law/s-ct/139/915/"><span class="citation" data-id="9335135"><a href="/opinion/9339797/simply-wireless-inc-v-t-mobile-us-inc/" aria-description="Citation for case: Simply Wireless, Inc. v. T-Mobile U.S., Inc.">139 S.Ct. 915</a></span></extracted-citation>, <extracted-citation case-ids="12624620,12624621,12624627,12624628,12624629,12624630" index="5" url="https://cite.case.law/l-ed-2d/202/641/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/202/641/">202 L.Ed.2d 641</a></span></extracted-citation> (2019), and now reverse.</p>
<p id="p-20">II</p>
<p id="p-21">The statute of limitations for a fabricated-evidence claim like McDonough's <a class="page-label" data-citation-index="1" data-label="2155" href="#p2155" id="p2155">*2155</a>does not begin to run until the criminal proceedings against the defendant (<em>i.e.,</em> the § 1983 plaintiff) have terminated in his favor. This conclusion follows both from the rule for the most natural common-law analogy (the tort of malicious prosecution) and from the practical considerations that have previously led this Court to defer accrual of claims that would otherwise constitute an untenable collateral attack on a criminal judgment.</p>
<p id="p-22">A</p>
<p id="p-23">The question here is when the statute of limitations began to run. Although courts look to state law for the length of the limitations period, the time at which a § 1983 claim accrues "is a question of federal law," "conforming in general to common-law tort principles." <em>Wallace v. Kato</em> , <extracted-citation case-ids="3553763" index="6" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 388, <extracted-citation case-ids="3553763" index="7" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="8" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007). That time is presumptively "when the plaintiff has 'a complete and present cause of action,' " <em>ibid.,</em> though the answer is not always so simple. See, <em>e.g.,</em> <em><extracted-citation case-ids="3553763" index="9" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">id.</span></extracted-citation></em> , at 388-391, and n. 3, <extracted-citation case-ids="3553763" index="10" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> ; <em>Dodd v. United States</em> , <extracted-citation case-ids="8209230" index="11" url="https://cite.case.law/us/545/353/#p360"><span class="citation" data-id="9843320"><a href="/opinion/799979/dodd-v-united-states/" aria-description="Citation for case: Dodd v. United States">545 U.S. 353</a></span></extracted-citation>, 360, <extracted-citation case-ids="8209230" index="12" url="https://cite.case.law/us/545/353/#p360"><span class="citation" data-id="9843320"><a href="/opinion/799979/dodd-v-united-states/" aria-description="Citation for case: Dodd v. United States">125 S.Ct. 2478</a></span></extracted-citation>, <extracted-citation case-ids="8209230" index="13" url="https://cite.case.law/us/545/353/#p360"><span class="citation" data-id="9843320"><a href="/opinion/799979/dodd-v-united-states/" aria-description="Citation for case: Dodd v. United States">162 L.Ed.2d 343</a></span></extracted-citation> (2005). Where, for example, a particular claim may not realistically be brought while a violation is ongoing, such a claim may accrue at a later date. See <em>Wallace</em> , <extracted-citation case-ids="3553763" index="14" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 389</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="15" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>.</p>
<p id="p-24">An accrual analysis begins with identifying " 'the specific constitutional right' " alleged to have been infringed. <em>Manuel</em> v. <em>Joliet</em> , 580 U. S. ----, ----, <extracted-citation case-ids="12609962" index="16" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct. 911</a></span></extracted-citation>, 920, <extracted-citation case-ids="12609962" index="17" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">197 L.Ed.2d 312</a></span></extracted-citation> (2017) (quoting <em>Albright v. Oliver</em> , <extracted-citation case-ids="231967" index="18" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S. 266</a></span></extracted-citation>, 271, <extracted-citation case-ids="231967" index="19" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="20" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">127 L.Ed.2d 114</a></span></extracted-citation> (1994) (plurality opinion)). Though McDonough's complaint does not ground his fabricated-evidence claim in a particular constitutional provision, the Second Circuit treated his claim as arising under the Due Process Clause. <extracted-citation case-ids="12517957" index="21" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">898 F.3d at 266</a></span></extracted-citation>. McDonough's claim, this theory goes, seeks to vindicate a " 'right not to be deprived of liberty as a result of the fabrication of evidence by a government officer.' " <em><extracted-citation case-ids="12517957" index="22" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">Ibid.</a></span></extracted-citation></em> (quoting <em>Zahrey v. Coffey</em> , <extracted-citation case-ids="11244172" index="23" url="https://cite.case.law/f3d/221/342/#p349"><span class="citation" data-id="769749"><a href="/opinion/769749/zaher-zahrey-v-martin-e-coffey/" aria-description="Citation for case: Zaher Zahrey v. Martin E. Coffey">221 F.3d 342</a></span></extracted-citation>, 349 (CA2 2000) ); see also, <em>e.g.,</em> <em>Napue v. Illinois</em> , <extracted-citation case-ids="9052" index="24" url="https://cite.case.law/us/360/264/#p269"><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U.S. 264</a></span></extracted-citation>, 269, <extracted-citation case-ids="9052" index="25" url="https://cite.case.law/us/360/264/#p269"><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">79 S.Ct. 1173</a></span></extracted-citation>, <extracted-citation case-ids="9052" index="26" url="https://cite.case.law/us/360/264/#p269"><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">3 L.Ed.2d 1217</a></span></extracted-citation> (1959). We assume without deciding that the Second Circuit's articulations of the right at issue and its contours are sound, having not granted certiorari to resolve those separate questions. See <em>Heck v. Humphrey</em> , <extracted-citation case-ids="39868" index="27" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, 480, n. 2, <extracted-citation case-ids="39868" index="28" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="29" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994) (accepting the lower courts' characterization of the relevant claims).<footnotemark>2</footnotemark></p>
<p id="p-25"><a class="page-label" data-citation-index="1" data-label="2156" href="#p2156" id="p2156">*2156</a>B</p>
<p id="p-26">As noted above, this Court often decides accrual questions by referring to the common-law principles governing analogous torts. See <em>Wallace</em> , <extracted-citation case-ids="3553763" index="30" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 388</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="31" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> ; <em>Heck</em> , <extracted-citation case-ids="39868" index="32" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 483</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="33" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. These "principles are meant to guide rather than to control the definition of § 1983 claims," such that the common law serves " 'more as a source of inspired examples than of prefabricated components.' " <em><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">Manuel</a></span></em> , 580 U. S., at ----, <extracted-citation case-ids="12609962" index="34" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct., at 920</a></span></extracted-citation>.</p>
<p id="p-27">Relying on our decision in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> , McDonough analogizes his fabricated-evidence claim to the common-law tort of malicious prosecution, a type of claim that accrues only once the underlying criminal proceedings have resolved in the plaintiff's favor. <extracted-citation case-ids="39868" index="35" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 484</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="36" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ; Prosser &amp; Keeton § 119, at 871, 874-875; Restatement (Second) of Torts §§ 653, 658 (1976) ; 3 D. Dobbs, P. Hayden, &amp; E. Bublick, Law of Torts §§ 586, 590, pp. 388-389, 402-404 (2d ed. 2011) (Dobbs). McDonough is correct that malicious prosecution is the most analogous common-law tort here.</p>
<p id="p-28">Common-law malicious prosecution requires showing, in part, that a defendant instigated a criminal proceeding with improper purpose and without probable cause. Restatement (Second) of Torts § 653 ; see also Dobbs § 586, at 388-389; Prosser &amp; Keeton § 119, at 871.<footnotemark>3</footnotemark> The essentials of McDonough's claim are similar: His claim requires him to show that the criminal proceedings against him-and consequent deprivations of his liberty<footnotemark>4</footnotemark> -were caused by Smith's malfeasance in fabricating evidence. At bottom, both claims challenge the integrity of criminal prosecutions undertaken "pursuant to legal process." See <em>Heck</em> , <extracted-citation case-ids="39868" index="37" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 484</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="38" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.<footnotemark>5</footnotemark></p>
<p id="p-29">We follow the analogy where it leads: McDonough could not bring his fabricated-evidence claim under § 1983 prior to favorable termination of his prosecution. As <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> explains, malicious prosecution's <a class="page-label" data-citation-index="1" data-label="2157" href="#p2157" id="p2157">*2157</a>favorable-termination requirement is rooted in pragmatic concerns with avoiding parallel criminal and civil litigation over the same subject matter and the related possibility of conflicting civil and criminal judgments. See <em>id</em> ., at 484-485, <extracted-citation case-ids="39868" index="39" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ; see also Prosser &amp; Keeton § 119, at 874; Dobbs § 589, at 402. The requirement likewise avoids allowing collateral attacks on criminal judgments through civil litigation. <em>Heck</em> , <extracted-citation case-ids="39868" index="40" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 484</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="41" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. These concerns track "similar concerns for finality and consistency" that have motivated this Court to refrain from multiplying avenues for collateral attack on criminal judgments through civil tort vehicles such as § 1983. <em>Id</em> ., at 485, <extracted-citation case-ids="39868" index="42" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ; see also <em>Preiser v. Rodriguez</em> , <extracted-citation case-ids="9981" index="43" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. 475</a></span></extracted-citation>, 490, <extracted-citation case-ids="9981" index="44" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation>, <extracted-citation case-ids="9981" index="45" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">36 L.Ed.2d 439</a></span></extracted-citation> (1973) (noting the "strong policy requiring exhaustion of state remedies" in order "to avoid the unnecessary friction between the federal and state court systems"); <em>Younger v. Harris</em> , <extracted-citation case-ids="11711728" index="46" url="https://cite.case.law/us/401/37/#p43"><span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">401 U.S. 37</a></span></extracted-citation>, 43, <extracted-citation case-ids="11711728" index="47" url="https://cite.case.law/us/401/37/#p43"><span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">91 S.Ct. 746</a></span></extracted-citation>, <extracted-citation case-ids="11711728" index="48" url="https://cite.case.law/us/401/37/#p43"><span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">27 L.Ed.2d 669</a></span></extracted-citation> (1971) ("Since the beginning of this country's history Congress has, subject to few exceptions, manifested a desire to permit state courts to try state cases free from interference by federal courts"). Because a civil claim such as McDonough's, asserting that fabricated evidence was used to pursue a criminal judgment, implicates the same concerns, it makes sense to adopt the same rule.<footnotemark>6</footnotemark></p>
<p id="p-30"><em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> confirms the strength of this analogy. In <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> , a prisoner serving a 15-year sentence for manslaughter sought damages under § 1983 against state prosecutors and an investigator for alleged misconduct similar to that alleged here, including knowingly destroying exculpatory evidence and causing an illegal voice identification procedure to be employed at the prisoner's trial. <extracted-citation case-ids="39868" index="49" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 478</a></span>-479</extracted-citation>, <extracted-citation case-ids="39868" index="50" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. The Court took as a given the lower courts' conclusion that those claims all effectively "challeng[ed] the legality of" the plaintiff's conviction. <em><extracted-citation case-ids="39868" index="51" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Id.</a></span></extracted-citation></em> , at 480, n. 2, <extracted-citation case-ids="39868" index="52" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. Looking first to the common law, the Court observed that malicious prosecution "provide[d] the closest analogy to" such claims because, unlike other potentially analogous common-law claims, malicious prosecution "permits damages for confinement imposed pursuant to legal process." <em><extracted-citation case-ids="39868" index="53" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="39868" index="53" url="https://cite.case.law/us/512/477/#p480"> at 484</extracted-citation>, <extracted-citation case-ids="39868" index="54" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.</p>
<p id="p-31">Emphasizing the concerns with parallel litigation and conflicting judgments just discussed, see <em><extracted-citation case-ids="39868" index="55" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">id.,</a></span></extracted-citation></em><extracted-citation case-ids="39868" index="55" url="https://cite.case.law/us/512/477/#p480"> at 484-486</extracted-citation>, <extracted-citation case-ids="39868" index="56" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, the Court in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> held that "in order to recover damages for allegedly unconstitutional conviction or imprisonment, or for other harm caused by actions whose unlawfulness would render a conviction or sentence invalid," a plaintiff in a § 1983 action first had to prove that his conviction had been invalidated in some way, <em><extracted-citation case-ids="39868" index="57" url="https://cite.case.law/us/512/477/#p480">id.</extracted-citation></em> , at 486, <extracted-citation case-ids="39868" index="58" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. This favorable-termination requirement, the Court explained, applies whenever "a judgment in favor of the plaintiff would necessarily imply" that his prior conviction or sentence was invalid. <em><extracted-citation case-ids="39868" index="59" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="39868" index="59" url="https://cite.case.law/us/512/477/#p480"> at 487</extracted-citation>, <extracted-citation case-ids="39868" index="60" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.</p>
<p id="p-32">This case differs from <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> because the plaintiff in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> had been convicted, while McDonough was acquitted. Although some claims do fall outside <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> 's ambit when a conviction is merely "anticipated," <em>Wallace</em> , <extracted-citation case-ids="3553763" index="61" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 393</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="62" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, however, McDonough's claims <a class="page-label" data-citation-index="1" data-label="2158" href="#p2158" id="p2158">*2158</a>are not of that kind, see <em>infra</em> , at 2159 - 2160. As articulated by the Court of Appeals, his claims challenge the validity of the criminal proceedings against him in essentially the same manner as the plaintiff in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> challenged the validity of his conviction. And the pragmatic considerations discussed in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> apply generally to civil suits within the domain of habeas corpus, not only to those that challenge convictions. See <em>Preiser</em> , <extracted-citation case-ids="9981" index="63" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. at 490</a></span>-491</extracted-citation>, <extracted-citation case-ids="9981" index="64" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation>. The principles and reasoning of <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> thus point toward a corollary result here: There is not " 'a complete and present cause of action,' " <em>Wallace</em> , <extracted-citation case-ids="3553763" index="65" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 388</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="66" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, to bring a fabricated-evidence challenge to criminal proceedings while those criminal proceedings are ongoing. Only once the criminal proceeding has ended in the defendant's favor, or a resulting conviction has been invalidated within the meaning of <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> , see <extracted-citation case-ids="39868" index="67" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 486</a></span>-487</extracted-citation>, <extracted-citation case-ids="39868" index="68" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, will the statute of limitations begin to run.<footnotemark>7</footnotemark></p>
<p id="p-33">C</p>
<p id="p-34">The soundness of this conclusion is reinforced by the consequences that would follow from the Second Circuit's approach, which would impose a ticking limitations clock on criminal defendants as soon as they become aware that fabricated evidence has been used against them. Such a rule would create practical problems in jurisdictions where prosecutions regularly last nearly as long as-or even longer than-the relevant civil limitations period. See Brief for Petitioner 53-55; Brief for Criminal Defense Organizations et al. as <em>Amici Curiae</em> 23-24. A significant number of criminal defendants could face an untenable choice between (1) letting their claims expire and (2) filing a civil suit against the very person who is in the midst of prosecuting them. The first option is obviously undesirable, but from a criminal defendant's perspective the latter course, too, is fraught with peril: He risks tipping his hand as to his defense strategy, undermining his privilege against self-incrimination, and taking on discovery obligations not required in the criminal context. See <em>SEC v. Dresser Industries, Inc.</em> , <extracted-citation case-ids="3507292,1292654" index="69" url="https://cite.case.law/f2d/628/1368/"><span class="citation multiple-matches"><a href="/c/F.2d/628/1368/">628 F.2d 1368</a></span></extracted-citation>, 1376 (CADC 1980) (en banc). Moreover, as noted above, the parallel civil litigation that would result if plaintiffs chose the second option would run counter to core principles of federalism, comity, consistency, and judicial economy. See <em>supra,</em> at 2156 - 2157.</p>
<p id="p-35">Smith suggests that stays and ad hoc abstention are sufficient to avoid the problems of two-track litigation. Such workarounds are indeed available when claims falling outside <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> 's scope nevertheless are initiated while a state criminal proceeding is pending, see <em>Wallace</em> , <extracted-citation case-ids="3553763" index="70" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 393</a></span>-394</extracted-citation>, <extracted-citation case-ids="3553763" index="71" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> (noting the power of district courts to stay civil actions while criminal prosecutions proceed); <em>Heck</em> , <extracted-citation case-ids="39868" index="72" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#487" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 487-488</a></span>, n. 8</extracted-citation>, <extracted-citation case-ids="39868" index="73" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> (noting possibility of abstention), but Smith's solution is poorly suited to the type of claim at issue here. When, as here, a plaintiff's claim "necessarily" questions the validity of a state proceeding, <em><extracted-citation case-ids="39868" index="74" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">id.,</a></span></extracted-citation></em><extracted-citation case-ids="39868" index="74" url="https://cite.case.law/us/512/477/#p480"> at 487</extracted-citation>, <extracted-citation case-ids="39868" index="75" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, there is no reason to put the onus to safeguard comity on district courts exercising case-by-case discretion-particularly at the foreseeable expense of potentially prejudicing litigants and cluttering dockets with dormant, unripe cases. Cf. <em>Panetti v. Quarterman</em> , <extracted-citation case-ids="3573391" index="76" url="https://cite.case.law/us/551/930/#p943"><span class="citation" data-id="9434999"><a href="/opinion/145700/panetti-v-quarterman/" aria-description="Citation for case: Panetti v. Quarterman">551 U.S. 930</a></span></extracted-citation>, 943, <extracted-citation case-ids="3573391" index="77" url="https://cite.case.law/us/551/930/#p943"><span class="citation" data-id="9434999"><a href="/opinion/145700/panetti-v-quarterman/" aria-description="Citation for case: Panetti v. Quarterman">127 S.Ct. 2842</a></span></extracted-citation>, <extracted-citation case-ids="3573391" index="78" url="https://cite.case.law/us/551/930/#p943"><span class="citation" data-id="9434999"><a href="/opinion/145700/panetti-v-quarterman/" aria-description="Citation for case: Panetti v. Quarterman">168 L.Ed.2d 662</a></span></extracted-citation> (2007) (noting that a scheme requiring "conscientious defense attorneys" to file unripe suits "would add to the burden imposed on courts, applicants, and the <a class="page-label" data-citation-index="1" data-label="2159" href="#p2159" id="p2159">*2159</a>States, with no clear advantage to any"). The accrual rule we adopt today, by contrast, respects the autonomy of state courts and avoids these costs to litigants and federal courts.</p>
<p id="p-36">In deferring rather than inviting such suits, we adhere to familiar principles. The proper approach in our federal system generally is for a criminal defendant who believes that the criminal proceedings against him rest on knowingly fabricated evidence to defend himself at trial and, if necessary, then to attack any resulting conviction through collateral review proceedings. McDonough therefore had a complete and present cause of action for the loss of his liberty only once the criminal proceedings against him terminated in his favor.</p>
<p id="p-37">III</p>
<p id="p-38">Smith's counterarguments do not sway the result.</p>
<p id="p-39">First, Smith argues that <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> is irrelevant to McDonough's claim, relying on this Court's opinion in <em>Wallace</em> . <em>Wallace</em> held that the limitations period begins to run on a § 1983 claim alleging an unlawful arrest under the Fourth Amendment as soon as the arrestee "becomes detained pursuant to legal process," not when he is ultimately released. <extracted-citation case-ids="3553763" index="79" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 397</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="80" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. The Court rejected the plaintiff's reliance on <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> , stating that the <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> rule comes "into play only when there exists 'a conviction or sentence that has <em>not</em> been ... invalidated,' that is to say, an 'outstanding criminal judgment.' " <em>Wallace</em> , <extracted-citation case-ids="3553763" index="81" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 393</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="82" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. The Court thus declined to adopt the plaintiff's theory "that an action which would impugn <em>an anticipated future conviction</em> cannot be brought until that conviction occurs and is set aside," because doing so in the context of an action for false arrest would require courts and litigants "to speculate about whether a prosecution will be brought, whether it will result in conviction, and whether the pending civil action will impugn that verdict-all this at a time when it can hardly be known what evidence the prosecution has in its possession." <em><extracted-citation case-ids="3553763" index="83" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">Ibid.</a></span></extracted-citation></em> (citations omitted).<footnotemark>8</footnotemark></p>
<p id="p-40">Smith is correct that <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> concerned a plaintiff serving a sentence for a still-valid conviction and that <em>Wallace</em> distinguished <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> on that basis, but <em>Wallace</em> did not displace the principles in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> that resolve this case. A false-arrest claim, <em>Wallace</em> explained, has a life independent of an ongoing trial or putative future conviction-it attacks the arrest only to the extent it was without legal process, even if legal process later commences. See <extracted-citation case-ids="3553763" index="84" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/#389" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 389-390</a></span>, 393</extracted-citation>, <extracted-citation case-ids="3553763" index="85" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. That feature made the claim analogous to common-law false imprisonment. <em><extracted-citation case-ids="3553763" index="86" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3553763" index="86" url="https://cite.case.law/us/549/384/#p388"> at 389</extracted-citation>, <extracted-citation case-ids="3553763" index="87" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. By contrast, a claim like McDonough's centers on evidence used to secure an indictment and at a criminal trial, so it does not require "speculat[ion] about whether a prosecution will be brought." <em><extracted-citation case-ids="3553763" index="88" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3553763" index="88" url="https://cite.case.law/us/549/384/#p388"> at 393</extracted-citation>, <extracted-citation case-ids="3553763" index="89" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. It directly challenges-and thus necessarily threatens to impugn-the prosecution itself. See <em>Heck</em> , <extracted-citation case-ids="39868" index="90" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 486</a></span>-487</extracted-citation>, <extracted-citation case-ids="39868" index="91" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.</p>
<p id="p-41">Second, Smith notes (1) that a fabricated-evidence claim in the Second Circuit (unlike a malicious prosecution claim) can exist even if there is probable cause and (2) that McDonough was acquitted. In other words, McDonough theoretically could have been prosecuted without the fabricated evidence, and he was not convicted even <a class="page-label" data-citation-index="1" data-label="2160" href="#p2160" id="p2160">*2160</a>with it. Because a violation thus could exist no matter its effect on the outcome, Smith reasons, "the date on which that outcome occurred is irrelevant." Brief for Respondent 26.</p>
<p id="p-42">Smith is correct in one sense. One could imagine a fabricated-evidence claim that does not allege that the violation's consequence was a liberty deprivation occasioned by the criminal proceedings themselves. See n. 2, <em>supra</em> . To be sure, the argument for adopting a favorable-termination requirement would be weaker in that context. That is not, however, the nature of McDonough's claim.</p>
<p id="p-43">As already explained, McDonough's claim remains most analogous to a claim of common-law malicious prosecution, even if the two are not identical. See <em>supra</em> , at 2156 - 2157. <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> explains why favorable termination is both relevant and required for a claim analogous to malicious prosecution that would impugn a conviction, and that rationale extends to an ongoing prosecution as well: The alternative would impermissibly risk parallel litigation and conflicting judgments. See <em>supra,</em> at 2156 - 2157. If the date of the favorable termination was relevant in <em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> , it is relevant here.</p>
<p id="p-44">It does not change the result, meanwhile, that McDonough suffered harm prior to his acquittal. The Court has never suggested that the date on which a constitutional injury first occurs is the only date from which a limitations period may run. Cf. <em>Wallace</em> , <extracted-citation case-ids="3553763" index="92" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. at 389</a></span>-391</extracted-citation>, and n. 3, <extracted-citation case-ids="3553763" index="93" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> (explaining that the statute of limitations for false-arrest claims does not begin running when the initial arrest takes place). To the contrary, the injury caused by a classic malicious prosecution likewise first occurs as soon as legal process is brought to bear on a defendant, yet favorable termination remains the accrual date. See <em>Heck</em> , <extracted-citation case-ids="39868" index="94" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 484</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="95" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.<footnotemark>9</footnotemark></p>
<p id="p-45">Third and finally, Smith argues that the advantages of his rule outweigh its disadvantages as a matter of policy. In his view, the Second Circuit's approach would provide more predictable guidance, while the favorable-termination approach fosters perverse incentives for prosecutors (who may become reluctant to offer favorable resolutions) and risks foreclosing meritorious claims (for example, where an outcome is not clearly "favorable"). These arguments are unconvincing. We agree that clear accrual rules are valuable but fail to see how assessing when proceedings terminated favorably will be, on balance, more burdensome than assessing when a criminal defendant "learned that the evidence was false and was used against him" and deprived him of liberty as a result. <extracted-citation case-ids="12517957" index="96" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">898 F.3d at 265</a></span></extracted-citation>. And while the risk of foreclosing certain claims and the potential incentive effects that Smith identifies could be valid considerations in other contexts,<footnotemark>10</footnotemark> <a class="page-label" data-citation-index="1" data-label="2161" href="#p2161" id="p2161">*2161</a>they do not overcome the greater danger that plaintiffs will be deterred under Smith's theory from suing for redress of egregious misconduct, see <em>supra,</em> at 2158-nor do they override the guidance of the common law and precedent.</p>
<p id="p-46">IV</p>
<p id="p-47">The statute of limitations for McDonough's § 1983 claim alleging that he was prosecuted using fabricated evidence began to run when the criminal proceedings against him terminated in his favor-that is, when he was acquitted at the end of his second trial. The judgment of the United States Court of Appeals for the Second Circuit is therefore reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="p-48"><em>It is so ordered</em> .</p>
<p id="p-49">Justice THOMAS, with whom Justice KAGAN and Justice GORSUCH join, dissenting.</p>
<p id="p-50">We granted certiorari to decide when "the statute of limitations for a Section 1983 claim based on fabrication of evidence in criminal proceedings begins to run." Pet. for Cert. i. McDonough, however, declined to take a definitive position on the "threshold inquiry in a [ 42 U.S.C.] § 1983 suit": " 'identify[ing] the specific constitutional right' at issue." <em>Manuel</em> v. <em>Joliet</em> , 580 U. S. ----, ----, <extracted-citation case-ids="12609962" index="97" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct. 911</a></span></extracted-citation>, 920, <extracted-citation case-ids="12609962" index="98" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">197 L.Ed.2d 312</a></span></extracted-citation> (2017) (quoting <em>Albright v. Oliver</em> , <extracted-citation case-ids="231967" index="99" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S. 266</a></span></extracted-citation>, 271, <extracted-citation case-ids="231967" index="100" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="101" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">127 L.Ed.2d 114</a></span></extracted-citation> (1994) (plurality opinion)). Because it is only "[a]fter pinpointing that right" that courts can proceed to "determine the elements of, and rules associated with, an action seeking damages for its violation," <em><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">Manuel</a></span></em> , 580 U. S., at ----, <extracted-citation case-ids="12609962" index="102" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct., at 920</a></span></extracted-citation>, we should have dismissed this case as improvidently granted.</p>
<p id="p-51">McDonough's failure to specify which constitutional right the respondent allegedly violated profoundly complicates our inquiry. McDonough argues that malicious prosecution is the common-law tort most analogous to his fabrication-of-evidence claim. But without " 'identify[ing] the specific constitutional right' at issue," we cannot adhere to the contours of that right when "applying, selecting among, or adjusting common-law approaches." <em><extracted-citation case-ids="12609962" index="103" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">Ibid.</a></span></extracted-citation></em> McDonough also contends that his suit is timely because he suffered a continuing constitutional violation, but this argument is similarly difficult to evaluate without identifying precisely what that violation was. Moreover, because the constitutional basis for McDonough's claim is unclear, we are unable to confirm that he has a constitutional claim at all. In my view, it would be both logical and prudent to address that antecedent question before addressing the statute of limitations for that claim.</p>
<p id="p-52">McDonough also urges us to resolve the question presented by extending <em>Preiser v. Rodriguez</em> , <extracted-citation case-ids="9981" index="104" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. 475</a></span></extracted-citation>, <extracted-citation case-ids="9981" index="105" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation>, <extracted-citation case-ids="9981" index="106" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">36 L.Ed.2d 439</a></span></extracted-citation> (1973), and <em>Heck v. Humphrey</em> , <extracted-citation case-ids="39868" index="107" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="108" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="109" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994). But the analysis under both cases depends on what facts a § 1983 plaintiff would need to prove to prevail on his claim.<footnotemark>1</footnotemark> And McDonough declines to <a class="page-label" data-citation-index="1" data-label="2162" href="#p2162" id="p2162">*2162</a>take a position on that issue as well. See Brief for Petitioner 19 ("The Court thus does not need to delve into what the elements of McDonough's constitutional claim are"); see also <em><extracted-citation case-ids="39868" index="110" url="https://cite.case.law/us/512/477/#p480">id.</extracted-citation></em> , at 37-38, n. 11.</p>
<p id="p-53">Further complicating this case, McDonough raised a malicious-prosecution claim alongside his fabrication-of-evidence claim. The District Court dismissed that claim on grounds of absolute immunity. McDonough has not fully explained the difference between that claim and his fabrication claim, which he insists is both analogous to the common-law tort of malicious prosecution and distinct from his dismissed malicious-prosecution claim. See Tr. of Oral Arg. 11-12; Reply Brief 3-4. Additionally, it appears that McDonough's fabrication claim could face dismissal on absolute-immunity grounds on remand. Brief for United States as <em>Amicus Curiae</em> 29-32.</p>
<p id="p-54">The Court, while recognizing that it is critical to ascertain the basis for a § 1983 claim when deciding how to "handl[e]" it, <em>ante,</em> at 2155, n. 2, attempts to evade these issues by "assum[ing] without deciding that the Second Circuit's articulations of the right at issue and its contours are sound." <em>Ante</em> , at 2155. But because the parties have not accepted the Second Circuit's view that the claim sounds in procedural due process,<footnotemark>2</footnotemark> that claim as "articulated by the Court of Appeals" might be different from the claim McDonough actually brought. <em>Ante</em> , at 2157 - 2158. The better course would be to dismiss this case as improvidently granted and await a case in which the threshold question of the basis of a "fabrication-of-evidence" claim is cleanly presented. Moreover, even if the Second Circuit were correct that McDonough asserts a violation of the Due Process Clause, it would be preferable for the Court to determine the claim's elements before deciding its statute of limitations.</p>
<p id="p-55">* * *</p>
<p id="p-56">McDonough asks the Court to bypass the antecedent question of the nature and elements of his claim and first determine its statute of limitations. We should have declined the invitation and dismissed the writ of certiorari as improvidently granted. I therefore respectfully dissent.</p>
<footnote label="1">
<p id="p-59">See <em>Floyd v. Attorney General of Pa.</em> , <extracted-citation index="111" url="https://cite.case.law/citations/?q=722%20Fed.%20Appx.%20112"><span class="citation no-link">722 Fed.Appx. 112</span></extracted-citation>, 114 (CA3 2018) ; <em>Mills v. Barnard</em> , <extracted-citation case-ids="12265180" index="112" url="https://cite.case.law/f3d/869/473/#p484"><span class="citation" data-id="9878123"><a href="/opinion/4422191/randall-mills-v-weakley-barnard/" aria-description="Citation for case: Randall Mills v. Weakley Barnard">869 F.3d 473</a></span></extracted-citation>, 484 (CA6 2017) ; <em>Bradford v. Scherschligt</em> , <extracted-citation case-ids="4345514" index="113" url="https://cite.case.law/f3d/803/382/#p388"><span class="citation" data-id="3004797"><a href="/opinion/3004797/ted-bradford-v-joseph-scherschligt/" aria-description="Citation for case: Ted Bradford v. Joseph Scherschligt">803 F.3d 382</a></span></extracted-citation>, 388 (CA9 2015) ; <em>Castellano v. Fragozo</em> , <extracted-citation case-ids="9298683" index="114" url="https://cite.case.law/f3d/352/939/#p959"><span class="citation" data-id="8408477"><a href="/opinion/8437970/castellano-v-fragozo/" aria-description="Citation for case: Castellano v. Fragozo">352 F.3d 939</a></span></extracted-citation>, 959-960 (CA5 2003) (en banc).</p>
</footnote>
<footnote label="2">
<p id="p-60">In accepting the Court of Appeals' treatment of McDonough's claim as one sounding in denial of due process, we express no view as to what other constitutional provisions (if any) might provide safeguards against the creation or use of fabricated evidence enforceable through a <extracted-citation index="115" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> action. See <em>Soldal v. Cook County</em> , <extracted-citation case-ids="11924920" index="116" url="https://cite.case.law/us/506/56/#p70"><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">506 U.S. 56</a></span></extracted-citation>, 70, <extracted-citation case-ids="11924920,6520087" index="117" url="https://cite.case.law/s-ct/113/538/"><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">113 S.Ct. 538</a></span></extracted-citation>, <extracted-citation case-ids="11924920" index="118" url="https://cite.case.law/us/506/56/#p70"><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">121 L.Ed.2d 450</a></span></extracted-citation> (1992) ("Certain wrongs affect more than a single right and, accordingly, can implicate more than one of the Constitution's commands"). Moreover, because the Second Circuit understood McDonough's due process claim to allege a deprivation of liberty, we have no occasion to consider the proper handling of a fabricated-evidence claim founded on an allegation that the use of fabricated evidence was so egregious as to shock the conscience, see, <em>e.g.</em> , <em>County of Sacramento v. Lewis</em> , <extracted-citation case-ids="11504410" index="119" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span></extracted-citation>, 849, <extracted-citation case-ids="11504410" index="120" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="121" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">140 L.Ed.2d 1043</a></span></extracted-citation> (1998), or caused harms exclusively to "interests other than the interest in freedom from physical restraint," <em>Albright v. Oliver</em> , <extracted-citation case-ids="231967" index="122" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S. 266</a></span></extracted-citation>, 283, <extracted-citation case-ids="231967" index="123" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="124" url="https://cite.case.law/us/510/266/#p271"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">127 L.Ed.2d 114</a></span></extracted-citation> (1994) (Kennedy, J., concurring in judgment); see also, <em>e.g.</em> , W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 119, p. 870 (5th ed. 1984) (Prosser &amp; Keeton) ("[O]ne who is wrongfully prosecuted may suffer both in reputation and by confinement"). Accordingly, we do not address what the accrual rule would be for a claim rooted in other types of harm independent of a liberty deprivation, as no such claim is before us. See <extracted-citation case-ids="12517957" index="125" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">898 F.3d 259</a></span></extracted-citation>, 266 (CA2 2018).</p>
</footnote>
<footnote label="3">
<p id="p-61">The Second Circuit borrowed the common-law elements of malicious prosecution to govern McDonough's distinct constitutional malicious prosecution claim, which is not before us. See <extracted-citation case-ids="12517957" index="126" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/#268" aria-description="Citation for case: McDonough v. Smith">898 F.3d at 268</a></span>, n. 10</extracted-citation>. This Court has not defined the elements of such a § 1983 claim, see <em>Manuel</em> v. <em>Joliet</em> , 580 U. S. ----, ---- - ----, <extracted-citation case-ids="12609962" index="127" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">137 S.Ct. 911</a></span></extracted-citation>, 921-922, <extracted-citation case-ids="12609962" index="128" url="https://cite.case.law/s-ct/137/911/#p920"><span class="citation" data-id="9873459"><a href="/opinion/4376986/manuel-v-city-of-joliet/" aria-description="Citation for case: Manuel v. City of Joliet">197 L.Ed.2d 312</a></span></extracted-citation> (2017), and this case provides no occasion to opine on what the elements of a constitutional malicious prosecution action under § 1983 are or how they may or may not differ from those of a fabricated-evidence claim. Similarly, while noting that only McDonough's malicious prosecution claim was barred on absolute-immunity grounds below, we make no statement on whether or how the doctrine of absolute immunity would apply to McDonough's fabricated-evidence claim. Any further consideration of that question is properly addressed by the Second Circuit on remand, subject to ordinary principles of waiver and forfeiture.</p>
</footnote>
<footnote label="4">
<p id="p-62">Though McDonough was not incarcerated pending trial, he was subject to restrictions on his ability to travel and other " 'restraints not shared by the public generally,' " <em>Justices of Boston Municipal Court v. Lydon</em> , <extracted-citation case-ids="6198207" index="129" url="https://cite.case.law/us/466/294/#p301"><span class="citation" data-id="9429572"><a href="/opinion/111151/justices-of-boston-municipal-court-v-lydon/" aria-description="Citation for case: Justices of Boston Municipal Court v. Lydon">466 U.S. 294</a></span></extracted-citation>, 301, <extracted-citation case-ids="6198207" index="130" url="https://cite.case.law/us/466/294/#p301"><span class="citation" data-id="9429572"><a href="/opinion/111151/justices-of-boston-municipal-court-v-lydon/" aria-description="Citation for case: Justices of Boston Municipal Court v. Lydon">104 S.Ct. 1805</a></span></extracted-citation>, <extracted-citation case-ids="6198207" index="131" url="https://cite.case.law/us/466/294/#p301"><span class="citation" data-id="9429572"><a href="/opinion/111151/justices-of-boston-municipal-court-v-lydon/" aria-description="Citation for case: Justices of Boston Municipal Court v. Lydon">80 L.Ed.2d 311</a></span></extracted-citation> (1984), and as the case comes to this Court, it is undisputed that McDonough has pleaded a liberty deprivation. See <extracted-citation case-ids="12517957" index="132" url="https://cite.case.law/f3d/898/259/"><span class="citation" data-id="8410858"><a href="/opinion/8440033/mcdonough-v-smith/" aria-description="Citation for case: McDonough v. Smith">898 F.3d at 266</a></span></extracted-citation>.</p>
</footnote>
<footnote label="5">
<p id="p-63">Smith urges the Court to steer away from the comparison to malicious prosecution, noting that the Second Circuit treats malicious prosecution claims and fabricated-evidence claims as distinct. See <em>id</em> ., at 268, and n. 12. But two constitutional claims may differ yet still both resemble malicious prosecution more than any other common-law tort; comparing constitutional and common-law torts is not a one-to-one matching exercise. See, <em>e.g.</em> , <em>Heck</em> , <extracted-citation case-ids="39868" index="133" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#479" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 479</a></span>, 484</extracted-citation>, <extracted-citation case-ids="39868" index="134" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> (analogizing malicious prosecution to several distinct claims). Tellingly, Smith has not suggested an alternative common-law analogy. See Tr. of Oral Arg. 44-46.</p>
</footnote>
<footnote label="6">
<p id="p-64">Such considerations are why Congress has determined that a petition for writ of habeas corpus, not a § 1983 action, "is the appropriate remedy for state prisoners attacking the validity of the fact or length of their confinement," <em>Preiser v. Rodriguez</em> , <extracted-citation case-ids="9981" index="135" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. 475</a></span></extracted-citation>, 490, <extracted-citation case-ids="9981" index="136" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation>, <extracted-citation case-ids="9981" index="137" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">36 L.Ed.2d 439</a></span></extracted-citation> (1973), including confinement pending trial before any conviction has occurred, see <em><extracted-citation case-ids="9981" index="138" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">id.,</a></span></extracted-citation></em><extracted-citation case-ids="9981" index="138" url="https://cite.case.law/us/411/475/#p490"> at 491</extracted-citation>, <extracted-citation case-ids="9981" index="139" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation> (citing <em>Braden v. 30th Judicial Circuit Court of Ky.</em> , <extracted-citation case-ids="11957617" index="140" url="https://cite.case.law/us/410/484/"><span class="citation" data-id="9425188"><a href="/opinion/108730/braden-v-30th-judicial-circuit-court-of-kentucky/" aria-description="Citation for case: Braden v. 30th Judicial Circuit Court of Kentucky">410 U.S. 484</a></span></extracted-citation>, <extracted-citation case-ids="11957617" index="141" url="https://cite.case.law/us/410/484/"><span class="citation" data-id="9425188"><a href="/opinion/108730/braden-v-30th-judicial-circuit-court-of-kentucky/" aria-description="Citation for case: Braden v. 30th Judicial Circuit Court of Kentucky">93 S.Ct. 1123</a></span></extracted-citation>, <extracted-citation case-ids="11957617" index="142" url="https://cite.case.law/us/410/484/"><span class="citation" data-id="9425188"><a href="/opinion/108730/braden-v-30th-judicial-circuit-court-of-kentucky/" aria-description="Citation for case: Braden v. 30th Judicial Circuit Court of Kentucky">35 L.Ed.2d 443</a></span></extracted-citation> (1973) ).</p>
</footnote>
<footnote label="7">
<p id="p-65">Because McDonough was not free to sue prior to his acquittal, we need not reach his alternative argument that his claim was timely because it alleged a continuing violation.</p>
</footnote>
<footnote label="8">
<p id="p-66"><em><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">Heck</a></span></em> itself suggested that a similar rule might allow at least some Fourth Amendment unlawful-search claims to proceed without a favorable termination. See <extracted-citation case-ids="39868" index="143" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#487" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 487</a></span>, n. 7</extracted-citation>, <extracted-citation case-ids="39868" index="144" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>.</p>
</footnote>
<footnote label="9">
<p id="p-67">As for Smith's suggestion that the fabricated evidence could not have caused any liberty deprivation where, as here, there could have been probable cause and there was in fact an acquittal, it suffices to reiterate that we assume the contours of the claim as defined by the Second Circuit, see <em>supra,</em> at 2155 - 2156, 2156 - 2157, and nn. 2, 4, and thus accept its undisputed conclusion that there was a sufficient liberty deprivation here, see <extracted-citation case-ids="12517957" index="145" url="https://cite.case.law/f3d/898/259/">898 F.3d at </extracted-citation>266 ; see also <em>Garnett v. Undercover Officer C0039</em> , <extracted-citation case-ids="12172727" index="146" url="https://cite.case.law/f3d/838/265/#p277"><span class="citation" data-id="8414281"><a href="/opinion/8442960/garnett-v-undercover-officer-c0039/" aria-description="Citation for case: Garnett v. Undercover Officer C0039">838 F.3d 265</a></span></extracted-citation>, 277 (CA2 2016) (explaining that "a further deprivation of liberty can result from the fabrication of evidence even if the initial arrest is lawful").</p>
</footnote>
<footnote label="10">
<p id="p-68">Because McDonough's acquittal was unquestionably a favorable termination, we have no occasion to address the broader range of ways a criminal prosecution (as opposed to a conviction) might end favorably to the accused. Cf. <em>Heck</em> , <extracted-citation case-ids="39868" index="147" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 486</a></span>-487</extracted-citation>, <extracted-citation case-ids="39868" index="148" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. To the extent Smith argues that the law in this area should take account of prosecutors' broad discretion over such matters as the terms on which pleas will be offered or whether charges will be dropped, those arguments more properly bear on the question whether a given resolution should be understood as favorable or not. Such considerations might call for a context-specific and more capacious understanding of what constitutes "favorable" termination for purposes of a § 1983 false-evidence claim, but that is not the question before us.</p>
</footnote>
<footnote label="1">
<p id="p-69">See <em>Preiser</em> , <extracted-citation case-ids="9981" index="149" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. at 500</a></span></extracted-citation>, <extracted-citation case-ids="9981" index="150" url="https://cite.case.law/us/411/475/#p490"><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span></extracted-citation> ("[W]hen a state prisoner is challenging the very fact or duration of his physical imprisonment, and the relief he seeks is a determination that he is entitled to immediate release or a speedier release from that imprisonment," he cannot bring suit under § 1983 ); <em>Heck</em> , <extracted-citation case-ids="39868" index="151" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. at 486</a></span>-487</extracted-citation>, <extracted-citation case-ids="39868" index="152" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ("[T]o recover damages for allegedly unconstitutional conviction or imprisonment ... a § 1983 plaintiff must prove that the conviction or sentence has been" reversed, expunged, invalidated, or otherwise called into question); accord, <em><extracted-citation case-ids="39868" index="153" url="https://cite.case.law/us/512/477/#p480">id.</extracted-citation></em> , at 486, n. 6, <extracted-citation case-ids="39868" index="154" url="https://cite.case.law/us/512/477/#p480"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> (explaining that a § 1983 action will not lie where a plaintiff would have to negate an element of the offense of which he was convicted to succeed on his § 1983 claim).</p>
</footnote>
<footnote label="2">
<p id="p-70">See Tr. of Oral Arg. 7 (petitioner) (citing the Fourth and Fourteenth Amendments); <em><extracted-citation case-ids="39868" index="155" url="https://cite.case.law/us/512/477/#p480">id.</extracted-citation></em> , at 42 (respondent) (asserting that the claim is not a procedural due process claim).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/McNabb v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "McNabb v. United States"
type: case
citation: "318 U.S. 332 (1943)"
parallel_cite: "63 S. Ct. 608; 87 L. Ed. 819"
neutral_cite: 1943 U.S. LEXIS 1280
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1943
date_decided: 1943-06-07
docket: 25
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1943-06-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: McNabb v. United States
  varies_by_point: false
  scope_note: "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501, per Corley v. United States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103791/mcnabb-v-united-states/"
  cluster_id: 103791
  opinion_id: 103791
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Mallory v. United States]]", "[[Corley v. United States]]", "[[Gerstein v. Pugh]]", "[[County of Riverside v. McLaughlin]]"]
aliases: []
tags: ["case", "fifth-amendment", "confessions", "mcnabb-mallory", "prompt-presentment", "supervisory-power", "federal"]
holding: "Under the Court's supervisory power over the federal courts, confessions obtained from federal arrestees during a prolonged detention conducted in flagrant disregard of the statutory duty to bring them promptly before a committing magistrate are inadmissible — independent of the Constitution."
lake:
  record_id: McNabb v. United States
  status: verified
  projected_at: 2026-07-06
---

# McNabb v. United States

*318 U.S. 332 (1943)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The McNabbs, a Tennessee family suspected of running an illegal still, were arrested by federal officers after a revenue agent was shot and killed during a raid. Several family members were detained by the officers — held in a barren cell, subjected to days of unremitting questioning by numerous officers, without friends or counsel and before any order of commitment — until they made incriminating statements. The statements were admitted and the McNabbs were convicted of second-degree murder of the federal officer.

## Issue
Whether confessions obtained from federal arrestees during a prolonged detention conducted in disregard of the statutory duty to take them promptly before a committing magistrate are admissible in the federal courts.

## Rule
No — they are excluded under the Court's supervisory power over federal criminal justice, apart from the Constitution. "Plainly, a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in wilful disobedience of law. . . . [T]o permit such evidence to be made the basis of a conviction in the federal courts would stultify the policy which Congress has enacted into law." — 318 U.S. at 345. ^pin-345

The exclusion rests on the integrity of the federal courts, not on a constitutional command: "We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. . . . The history of liberty has largely been the history of observance of procedural safeguards." — *Id.* at 347. ^pin-347

## Application
The McNabbs were questioned while in the custody of the arresting officers and before any commitment order, held in a barren cell and interrogated continuously for days without friends or counsel. Their confessions were thus secured during a detention that flagrantly disregarded the statutes requiring prompt presentment to a committing magistrate. Allowing convictions to rest on evidence so obtained would make the courts accomplices in disobedience of those statutes, so the confessions had to be excluded — the Court resting on its supervisory authority rather than reaching the constitutional question.

## Conclusion
The confessions were inadmissible and the convictions could not stand; the judgments were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *McNabb* is the first half of the **McNabb-Mallory** federal prompt-presentment rule, completed by [[Mallory v. United States]] under Federal Rule of Criminal Procedure 5(a). It is a **federal-court** supervisory-power rule, not a constitutional rule binding the States. Congress later **modified** — but did not supplant — the rule by 18 U.S.C. §3501's six-hour safe harbor, as the Court held in [[Corley v. United States]]. The prompt-presentment duty is the confession-suppression counterpart to the prompt judicial probable-cause determination of [[Gerstein v. Pugh]] and [[County of Riverside v. McLaughlin]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *McNabb v. United States*, 318 U.S. 332 (1943) — https://www.courtlistener.com/opinion/103791/mcnabb-v-united-states/ — pinpoints: 345, 347.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9ffc90742daa8133", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "McNabb v. United States"}, "payload": {"all": [{"cite": "318 U.S. 332", "page": "332", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "318"}, {"cite": "63 S. Ct. 608", "page": "608", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "63"}, {"cite": "87 L. Ed. 819", "page": "819", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "1943 U.S. LEXIS 1280", "page": "1280", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1943"}], "display": "318 U.S. 332", "official": {"cite": "318 U.S. 332", "page": "332", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "318"}, "official_selection_present": true, "record_id": "McNabb v. United States"}}
{"assertion_id": "2746ab1bb511de48", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-347", "record_id": "McNabb v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-347", "pinpoint_status": "slip-only", "quote": "We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. . . . The history of liberty has largely been the history of observance of procedural safeguards.", "quote_fidelity": "mismatch", "record_id": "McNabb v. United States", "star_marker": null}}
{"assertion_id": "6a52f0cebeb46368", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-345", "record_id": "McNabb v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-345", "pinpoint_status": "slip-only", "quote": "--- # McNabb v. United States *318 U.S. 332 (1943)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The McNabbs, a Tennessee family suspected of running an illegal still, were arrested by federal officers after a revenue agent was shot and killed during a raid. Several family members were detained by the officers — held in a barren cell, subjected to days of unremitting questioning by numerous officers, without friends or counsel and before any order of commitment — until they made incriminating statements. The statements were admitted and the McNabbs were convicted of second-degree murder of the federal officer. ## Issue Whether confessions obtained from federal arrestees during a prolonged detention conducted in disregard of the statutory duty to take them promptly before a committing magistrate are admissible in the federal courts. ## Rule No — they are excluded under the Court's supervisory power over federal criminal justice, apart from the Constitution.", "quote_fidelity": "mismatch", "record_id": "McNabb v. United States", "star_marker": null}}
{"assertion_id": "e1d948e5afdcc999", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "McNabb v. United States"}, "payload": {"as_of_content": "1943-06-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "McNabb v. United States", "scope_note": "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501, per Corley v. United States.", "varies_by_point": false}}
```

### lake record — McNabb v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "McNabb v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "McNabb v. United States",
    "case_name_short": "McNabb",
    "case_name_full": "McNABB Et Al. v. UNITED STATES",
    "input_case_name": "McNabb v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1943-06-07",
    "year": 1943,
    "docket": "25",
    "cluster_id": 103791,
    "lead_opinion_id": 103791,
    "sibling_ids": [
      103791,
      9419320,
      9419321
    ],
    "absolute_url": "/opinion/103791/mcnabb-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8196926,
        "score": 20,
        "case_name": "McNabb v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "318 U.S. 332",
      "volume": "318",
      "reporter": "U.S.",
      "page": "332",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "63 S. Ct. 608",
        "volume": "63",
        "reporter": "S. Ct.",
        "page": "608",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 819",
        "volume": "87",
        "reporter": "L. Ed.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1943 U.S. LEXIS 1280",
        "volume": "1943",
        "reporter": "U.S. LEXIS",
        "page": "1280",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "318 U.S. 332",
        "volume": "318",
        "reporter": "U.S.",
        "page": "332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 S. Ct. 608",
        "volume": "63",
        "reporter": "S. Ct.",
        "page": "608",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 819",
        "volume": "87",
        "reporter": "L. Ed.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1943 U.S. LEXIS 1280",
        "volume": "1943",
        "reporter": "U.S. LEXIS",
        "page": "1280",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "318 U.S. 332",
    "official_selection": {
      "court_class": "scotus",
      "selected": "318 U.S. 332",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-345",
      "page": null,
      "quote": "--- # McNabb v. United States *318 U.S. 332 (1943)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The McNabbs, a Tennessee family suspected of running an illegal still, were arrested by federal officers after a revenue agent was shot and killed during a raid. Several family members were detained by the officers \u2014 held in a barren cell, subjected to days of unremitting questioning by numerous officers, without friends or counsel and before any order of commitment \u2014 until they made incriminating statements. The statements were admitted and the McNabbs were convicted of second-degree murder of the federal officer. ## Issue Whether confessions obtained from federal arrestees during a prolonged detention conducted in disregard of the statutory duty to take them promptly before a committing magistrate are admissible in the federal courts. ## Rule No \u2014 they are excluded under the Court's supervisory power over federal criminal justice, apart from the Constitution.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-347",
      "page": null,
      "quote": "We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. . . . The history of liberty has largely been the history of observance of procedural safeguards.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1943-06-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "McNabb v. United States",
    "varies_by_point": false,
    "scope_note": "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified \u2014 not supplanted \u2014 by 18 U.S.C. \u00a73501, per Corley v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Fortunato",
          "cluster_id": 6580749,
          "cite": [
            "466 Mass. 500",
            "996 N.E.2d 457",
            "2013 WL 5451772",
            "2013 Mass. LEXIS 719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 2662992,
          "cite": [
            "841 F. Supp. 2d 322",
            "2012 WL 256088",
            "2012 U.S. Dist. LEXIS 10769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re United States",
          "cluster_id": 202116,
          "cite": [
            "441 F.3d 44",
            "2006 U.S. App. LEXIS 7779",
            "2006 WL 744801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Garcia-Echaverria",
          "cluster_id": 786819,
          "cite": [
            "374 F.3d 440",
            "2004 U.S. App. LEXIS 13590",
            "2004 WL 1470466"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Dennis Johnson",
          "cluster_id": 784434,
          "cite": [
            "351 F.3d 988",
            "63 Fed. R. Serv. 69",
            "2003 U.S. App. LEXIS 25298",
            "2003 WL 22952102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pouncey",
          "cluster_id": 7897125,
          "cite": [
            "241 Conn. 802",
            "699 A.2d 901",
            "1997 Conn. LEXIS 226"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo",
          "cluster_id": 733401,
          "cite": [
            "105 F.3d 117",
            "1997 U.S. App. LEXIS 311",
            "1997 WL 6366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario",
          "cluster_id": 6576998,
          "cite": [
            "422 Mass. 48",
            "661 N.E.2d 71",
            "1996 Mass. LEXIS 29"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Juan Ramon MATTA-BALLESTEROS, Defendant-Appellant",
          "cluster_id": 709239,
          "cite": [
            "71 F.3d 754",
            "95 Daily Journal DAR 15853",
            "95 Cal. Daily Op. Serv. 9042",
            "43 Fed. R. Serv. 338",
            "1995 U.S. App. LEXIS 33475",
            "1995 WL 704693"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 7896184,
          "cite": [
            "234 Conn. 324",
            "662 A.2d 1199",
            "1995 Conn. LEXIS 254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Turner",
          "cluster_id": 1188941,
          "cite": [
            "878 P.2d 521",
            "8 Cal. 4th 137",
            "32 Cal. Rptr. 2d 762",
            "94 Daily Journal DAR 11425",
            "94 Cal. Daily Op. Serv. 6238",
            "1994 Cal. LEXIS 4151"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Horn",
          "cluster_id": 674595,
          "cite": [
            "29 F.3d 754",
            "29 Fed. R. Serv. 3d 1525",
            "1994 U.S. App. LEXIS 18687",
            "1994 WL 378486"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. United States",
          "cluster_id": 105254,
          "cite": [
            "99 L. Ed. 2d 150",
            "75 S. Ct. 127",
            "348 U.S. 121",
            "1954 U.S. LEXIS 2740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pinkerton v. United States",
          "cluster_id": 104316,
          "cite": [
            "328 U.S. 640",
            "66 S. Ct. 1180",
            "90 L. Ed. 1489",
            "1946 U.S. LEXIS 3154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massiah v. United States",
          "cluster_id": 106822,
          "cite": [
            "12 L. Ed. 2d 246",
            "84 S. Ct. 1199",
            "377 U.S. 201",
            "1964 U.S. LEXIS 1277"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cupp v. Naughten",
          "cluster_id": 108888,
          "cite": [
            "38 L. Ed. 2d 368",
            "94 S. Ct. 396",
            "414 U.S. 141",
            "1973 U.S. LEXIS 180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Costello v. United States",
          "cluster_id": 105355,
          "cite": [
            "100 L. Ed. 2d 397",
            "76 S. Ct. 406",
            "350 U.S. 359",
            "1956 U.S. LEXIS 1845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Townsend v. Burke",
          "cluster_id": 104579,
          "cite": [
            "92 L. Ed. 2d 1690",
            "68 S. Ct. 1252",
            "334 U.S. 736",
            "1948 U.S. LEXIS 1988",
            "92 L. Ed. 1690"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherman v. United States",
          "cluster_id": 105681,
          "cite": [
            "2 L. Ed. 2d 848",
            "78 S. Ct. 819",
            "356 U.S. 369",
            "1958 U.S. LEXIS 1024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolf v. Colorado",
          "cluster_id": 104709,
          "cite": [
            "93 L. Ed. 2d 1782",
            "69 S. Ct. 1359",
            "338 U.S. 25",
            "1949 U.S. LEXIS 2079",
            "93 L. Ed. 1782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103791 OR 9419320 OR 9419321) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzUwNDMyMDAwMDAmcz0yMzUwNjAwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103791+OR+9419320+OR+9419321%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(103791 OR 9419320 OR 9419321)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03ODYmcz0xMDUxNDkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103791+OR+9419320+OR+9419321%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103791 OR 9419320 OR 9419321)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103791 OR 9419320 OR 9419321)",
    "indexed_citing_opinions": 1337,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103791,
        "count": 1254,
        "count_source": "search"
      },
      {
        "opinion_id": 9419320,
        "count": 120,
        "count_source": "search"
      },
      {
        "opinion_id": 9419321,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2030,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mcnabb-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MTYyNDEmcz00NzA3NTk1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103791+OR+9419320+OR+9419321%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103791,
        "cited_id": 84842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 85535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103702,
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
    "date_created": "2026-07-05T12:57:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:00:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — McNabb v. United States

```
<p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U.S. 332</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">63 S.Ct. 608</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">87 L.Ed. 819</a></span></p>
    <p class="parties">McNABB et al.<br>v.<br>UNITED STATES.</p>
    <p class="docket">No. 25.</p>
    <p class="date">Argued Oct. 22, 1942.</p>
    <p class="date">Decided March 1, 1943.</p>
    <p class="date">Rehearing Denied June 7, 1943.</p>
    <div class="prelims">
      <p class="indent">See <span class="citation multiple-matches"><a href="/c/U.S./319/784/">319 U.S. 784</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./63/1322/">63 S.Ct. 1322</a></span>, 87 L.Ed. &#8212;-.</p>
      <p class="indent">Mr. E. B. Baker, of Chattanooga, Tenn., for petitioners.</p>
      <p class="indent">Mr. Asst. Atty. Gen. Wendell Berge, of Washington, D.C., for respondent.</p>
      <p class="indent">Mr. Justice FRANKFURTER, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The petitioners are under sentence of imprisonment for forty-five years for the murder of an officer of the Alcohol Tax Unit of the Bureau of Internal Revenue engaged in the performance of his official duties. <span class="citation no-link">18 U.S.C. &#167; 253</span>, <span class="citation no-link">18 U.S.C.A. &#167; 253</span>. They were convicted of second-degree murder in the District Court for the Eastern District of Tennessee, and on appeal to the Circuit Court of Appeals for the Sixth Circuit the convictions were sustained. <span class="citation" data-id="1486063"><a href="/opinion/1486063/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">123 F.2d 848</a></span>. We brought the case here because the petition for certiorari presented serious questions in the administration of federal criminal justice. <span class="citation multiple-matches"><a href="/c/U.S./316/658/">316 U.S. 658</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./62/1305/">62 S.Ct. 1305</a></span>, <span class="citation no-link">86 L.Ed. 1736</span>. Determination of these questions turns upon the circumstances relating to the admission in evidence of incriminating statements made by the petitioners.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">On the afternoon of Wednesday, July 31, 1940, information was received at the Chattanooga office of the Alcoholic Tax Unit that several members of the McNabb family were planning to sell that night whiskey on which federal taxes had not been paid. The McNabbs were a clan of Tennessee mountaineers living about twelve miles from Chattanooga in a section known as the McNabb Settlement. Plans were made to apprehend the McNabbs while actually engaged in their illicit enterprise. That evening four revenue agents, accompanied by the Government's informers, drove to the McNabb Settlement. When they approached the rendezvous arranged between the McNabbs and the informers, the officers got out of the car. The informers drove on and met five of the McNabbs, of whom three&#8212;the twin brothers Freeman and Raymond, and their cousin Benjamin&#8212;are the petitioners here. (The two others, Emuil and Barney McNabb, were acquitted at the direction of the trial court.) The group proceeded to a spot near the family cemetery where the liquor was hidden. While cans containing whiskey were being loaded into the car, one of the informers flashed a prearranged signal to the officers who thereupon came running. One of these called out, 'All right, boys, federal officers!', and the McNabbs took flight.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">Instead of pursuing the McNabbs, the officers began to empty the cans. They heard noises coming from the direction of the cemetery, and after a short while a large rock landed at their feet. An officer named Leeper ran into the cemetery. He looked about with his flashlight but discovered no one. Noticing a couple of whiskey cans there he began to pour out their contents. Shortly afterwards the other officers heard a shot; running into the cemetery they found Leeper on the ground, fatally wounded. A few minutes later&#8212;at about ten o'clock&#8212;he died without having identified his assailant. A second shot slightly wounded another officer. A search of the cemetery proved futile, and the officers left.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">About three or four hours later&#8212;between one and two o'clock Thursday morning&#8212;federal officers went to the home of Freeman, Raymond, and Emuil McNabb and there placed them under arrest. Freeman and Raymond were twenty-five years old. Both had lived in the Settlement all their lives; neither had gone beyond the fourth grade in school; neither had ever been farther from his home than Jasper, twenty-one miles away. Emuil was twenty-two years old. He, too, had lived in the Settlement all his life, and had not gone beyond the second grade.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Immediately upon arrest, Freeman, Raymond, and Emuil were taken directly to the Federal Building at Chattanooga. They were not brought before a United States Commissioner or a judge. Instead, they were placed in a detention room (where there was nothing they could sit or lie down on, except the floor), and kept there for about fourteen hours, from three o'clock Thursday morning until five o'clock that afternoon. They were given some sandwiches. They were not permitted to see relatives and friends who attempted to visit them. They had no lawyer. There is no evidence that they requested the assistance of counsel, or that they were told that they were entitled to such assistance.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Barney McNabb, who had been arrested early Thursday morning by the local police, was handed over to the federal authorities about nine or ten o'clock that morning. He was twenty-eight years old; like the other McNabbs he had spent his entire life in the Settlement, had never gone beyond Jasper, and his schooling stopped at the third grade. Barney was placed in a separate room in the Federal Building where he was questioned for a short period. The officers then took him to the scene of the killing, brought him back to the Federal Building, questioned him further for about an hour, and finally removed him to the county jail three blocks away.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">In the meantime, direction of the investigation had been assumed by H. B. Taylor, district supervisor of the Alcohol Tax Unit, with headquarters at Louisville, Kentucky. Taylor was the Government's chief witness on the central issue of the admissbility of the statements made by the McNabbs. Arriving in Chattanooga early Thursday morning, he spent the day in study of the case before beginning his interrogation of the prisoners. Freeman, Raymond, and Emuil, who had been taken to the county jail about five o'clock Thursday afternoon, were brought back to the Federal Building early that evening. According to Taylor, his questioning of them began at nine o'clock. Other officers set the hour earlier.<a class="footnote" href="#fn1" id="fn1_ref">1</a></p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Throughout the questioning, most of which was done by Taylor, at least six officers were present. At no time during its course was a lawyer or any relative or friend of the defendants present. Taylor began by telling 'each of them before they were questioned that we were Government officers, what we were investigating, and advised them that they did not have to make a statement, that they need not fear force, and that any statement made by them would be used against them, and that they need not answer any questions asked unless they desired to do so'.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">The men were questioned singly and together. As described by one of the officers, 'they would be brought in, be questioned possibly at various times, some of them half an hour, or maybe an hour, or maybe two hours'. Taylor testified that the questioning continued until one o'clock in the morning, when the defendants were taken back to the county jail.<a class="footnote" href="#fn2" id="fn2_ref">2</a></p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">The questioning was resumed Friday morning, probably sometime between nine and ten o'clock.<a class="footnote" href="#fn3" id="fn3_ref">3</a> 'They were brought down from the jail several times, how many I don't know. They were questioned one at a time, as we would finish one he would be sent back and we would try to reconcile the facts they told, connect up the statements they made, and they we would get two of them together. I think at one time we probably had all five together trying to reconcile their statements. * * * When I knew the truth I told the defendants what I knew. I never called them damn liars, but I did say they were lying to me. * * * It would be impossible to tell all the motions I made with my hands during the two days of questioning, however, I didn't threaten anyone. None of the officers were prejudiced towards these defendants nor bitter toward them. We were only trying to find out who killed our fellow officer.'</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">Benjamin McNabb, the third of the petitioners, came to the office of the Alcohol Tax Unit about eight or nine o'clock Friday morning and voluntarily surrendered. Benjamin was twenty years old, had never been arrested before, had lived in the McNabb Settlement all his life, and had not got beyond the fourth grade in school. He told the officers that he had heard that they were looking for him but that he was entirely innocent of any connection with the crime. The officers made him take his clothes off for a few minutes because, so he testified, 'they wanted to look at me. This scared me pretty much.'<a class="footnote" href="#fn4" id="fn4_ref">4</a> He was not taken before a United States Commissioner or a judge. Instead, the officers questioned him for about five or six hours. When finally in the afternoon he was confronted with the statement that the others accused him of having fired both shots, Benjamin said, 'If they are going to accuse me of that, I will tell the whole truth; you may get your pencil and paper and write it down.' He then confessed that he had fired the first shot, but denied that he had also fired the second.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">Because there were 'certain discrepancies in their stories, and we were anxious to straighten them out', the defendants were brought to the Federal Building from the jail between nine and ten o'clock Friday night. They were again questioned, sometimes separately, sometimes together. Taylor testified that 'We had Freeman McNabb on the night of the second (Friday) for about three and one-half hours. I don't remember the time but I remember him particularly because he certainly was hard to get anything out of. He would admit he lied before, and then tell it all over again. I knew some of the things about the whole truth and it took about three and one-half hours before he would say it was the truth, and I finally got him to tell a story which he said was true and which certainly fit better with the physical facts and circumstances than any other story he had told. It took me three and one-half hours to get a story that was satisfactory or that I believed was nearer the truth than when we started.'</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">The questioning of the defendants continued until about two o'clock Saturday morning, when the officers finally 'got all the discrepancies straightened out.' Benjamin did not change his story that he had fired only the first shot. Freeman and Raymond admitted that they were present when the shooting occurred, but denied Benjamin's charge that they had urged him to shoot. Barney and Emuil, who were acquitted at the direction of the trial court, made no incriminating admissions.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">Concededly, the admissions made by Freeman, Raymond and Benjamin constituted the crux of the Government's case against them, and the convictions cannot stand if such evidence be excluded. Accordingly, the question for our decision is whether these incriminating statements, made under the circumstances we have summarized,<a class="footnote" href="#fn5" id="fn5_ref">5</a> were properly admitted. Relying upon the guarantees of the Fifth Amendment that no person 'shall be compelled in any Criminal Case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law', the petitioners contend that the Constitution itself forbade the use of this evidence against them. The Government counters by urging that the Constitution proscribes only 'involuntary' confessions, and that judged by appropriate criteria of 'voluntariness' the petitioners' admissions were voluntary and hence admissible.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">It is true, as the petitioners assert, that a conviction in the federal courts, the foundation of which is evidence obtained in disregard of liberties deemed fundamental by the Constitution, cannot stand. Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S.Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L.Ed. 746</a></span>; Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L.Ed. 652</a></span>, L.R.A.1915B, 834, Ann.Cas.1915C, 1177; Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S.Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L.Ed. 647</a></span>; Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S.Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L.Ed. 654</a></span>; Agnello v. United States, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">46 S.Ct. 4</a></span>, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">70 L.Ed. 145</a></span>; Byars v. United States, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">47 S.Ct. 248</a></span>, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">71 L.Ed. 520</a></span>; Grau v. United States, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U.S. 124</a></span>, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">53 S.Ct. 38</a></span>, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">77 L.Ed. 212</a></span>. And this Court has, on Constitutional grounds, set aside convictions, both in the federal and state courts, which were based upon confessions 'secured by protracted and repeated questioning of ignorant and untutored persons in whose minds the power of officers was greatly magnified', Lisenba v. California, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#239" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 239, 240</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#291" aria-description="Citation for case: Lisenba v. California">62 S.Ct. 280, 291</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">86 L.Ed. 166</a></span>, or 'who have been unlawfully held incommunicado without advice of friends or counsel', Ward v. Texas, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#555" aria-description="Citation for case: Ward v. Texas">316 U.S. 547, 555</a></span>, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#1143" aria-description="Citation for case: Ward v. Texas">62 S.Ct. 1139, 1143</a></span>, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">86 L.Ed. 1663</a></span>, and see Brown v. Mississippi, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278</a></span>, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">56 S.Ct. 461</a></span>, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">80 L.Ed. 682</a></span>; Chambers v. Florida, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">60 S.Ct. 472</a></span>, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">84 L.Ed. 716</a></span>; Canty v. Alabama, <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U.S. 629</a></span>, <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">60 S.Ct. 612</a></span>, <span class="citation no-link">84 L.Ed. 988</span>; White v. Texas, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U.S. 530</a></span>, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">60 S.Ct. 1032</a></span>, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">84 L.Ed. 1342</a></span>; Lomax v. Texas, <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U.S. 544</a></span>, <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">61 S.Ct. 956</a></span>, <span class="citation no-link">85 L.Ed. 1511</span>; Vernon v. Alabama, <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U.S. 547</a></span>, <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">61 S.Ct. 1092</a></span>, <span class="citation" data-id="8156478"><a href="/opinion/8194543/bakery-pastry-drivers-helpers-local-802-v-wohl/" aria-description="Citation for case: Bakery &amp; Pastry Drivers &amp; Helpers Local 802 v. Wohl">85 L.Ed. 1513</a></span>.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">In the view we take of the case, however, it becomes unnecessary to reach the Constitutional issue pressed upon us. For, while the power of this Court to undo convictions in state courts is limited to the enforcement of those 'fundamental principles of liberty and justice', Hebert v. Louisiana, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U.S. 312, 316</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#104" aria-description="Citation for case: Hebert v. Louisiana">47 S.Ct. 103, 104</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/" aria-description="Citation for case: Hebert v. Louisiana">71 L.Ed. 270</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/" aria-description="Citation for case: Hebert v. Louisiana">48 A.L.R. 1102</a></span>, which are secured by the Fourteenth Amendment, the scope of our reviewing power over convictions brought here from the federal courts is not confined to ascertainment of Constitutional validity. Judicial supervision of the administration of criminal justice in the federal courts implies the duty of establishing and maintaining civilized standards of procedure and evidence. Such standards are not satisfied merely by observance of those minimal historic safeguards for securing trial by reason which are summarized as 'due process of law' and below which we reach what is really trial by force. Moreover, review by this Court of state action expressing its notion of what will best further its own security in the administration of criminal justice demands appropriate respect for the deliberative judgment of a state in so basic an exercise of its jurisdiction. Considerations of large policy in making the necessary accommodations in our federal system are wholly irrelevant to the formulation and application of proper standards for the enforcement of the federal criminal law in the federal courts.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">The principles governing the admissibility of evidence in federal criminal trials have not been restricted, therefore, to those derived solely from the Constitution. In the exercise of its supervisory authority over the administration of criminal justice in the federal courts, see Nardone v. United States, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U.S. 338, 341, 342</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#267" aria-description="Citation for case: Nardone v. United States">60 S.Ct. 266, 267, 268</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>, this Court has, from the very beginning of its history, formulated rules of evidence to be applied in federal criminal prosecutions. E.g., Ex parte Bollman &amp; Swartwout, <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#130" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 130, 131</a></span>, <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout">2 L.Ed. 554</a></span>; United States v. Palmer, <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/#643" aria-description="Citation for case: United States v. Palmer">3 Wheat. 610, 643, 644</a></span>, <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/" aria-description="Citation for case: United States v. Palmer">4 L.Ed. 471</a></span>; United States v. Furlong, <span class="citation" data-id="85290"><a href="/opinion/85290/united-states-v-furlong/#199" aria-description="Citation for case: United States v. Furlong">5 Wheat. 184, 199</a></span>, <span class="citation" data-id="85290"><a href="/opinion/85290/united-states-v-furlong/" aria-description="Citation for case: United States v. Furlong">5 L.Ed. 64</a></span>; United States v. Gooding, <span class="citation" data-id="85535"><a href="/opinion/85535/united-states-v-gooding/#468" aria-description="Citation for case: United States v. Gooding">12 Wheat. 460, 468, 470</a></span>, <span class="citation" data-id="85535"><a href="/opinion/85535/united-states-v-gooding/" aria-description="Citation for case: United States v. Gooding">6 L.Ed. 693</a></span>; United States v. Wood, <span class="citation" data-id="9416399"><a href="/opinion/86149/united-states-v-wood/" aria-description="Citation for case: United States v. Wood">14 Pet. 430</a></span>, <span class="citation" data-id="9416399"><a href="/opinion/86149/united-states-v-wood/" aria-description="Citation for case: United States v. Wood">10 L.Ed. 527</a></span>; United States v. Murphy, <span class="citation" data-id="86206"><a href="/opinion/86206/united-states-v-murphy/" aria-description="Citation for case: United States v. Murphy">16 Pet. 203</a></span>, <span class="citation" data-id="86206"><a href="/opinion/86206/united-states-v-murphy/" aria-description="Citation for case: United States v. Murphy">10 L.Ed. 937</a></span>; Funk v. United States, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">290 U.S. 371</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">54 S.Ct. 212</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">78 L.Ed. 369</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">93 A.L.R. 1136</a></span>; Wolfle v. United States, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">291 U.S. 7</a></span>, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">54 S.Ct. 279</a></span>, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">78 L.Ed. 617</a></span>; see 1 Wigmore on Evidence (3d ed. 1940) pp. 170-97; Note, 47 Harv.L.Rev. 853.<a class="footnote" href="#fn6" id="fn6_ref">6</a> And in formulating such rules of evidence for federal criminal trials the Court has been guided by considerations of justice not limited to the strict canons of evidentiary relevance.</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">Quite apart from the Constitution, therefore, we are constrained to hold that the evidence elicited from the petitioners in the circumstances disclosed here must be excluded. For in their treatment of the petitioners the arresting officers assumed functions which Congress has explicitly denied them. They subjected the accused to the pressures of a procedure which is wholly incompatible with the vital but very restricted duties of the investigating and arresting officers of the Government and which tends to undermine the integrity of the criminal proceeding. Congress has explicitly commanded that 'It shall be the duty of the marshal, his deputy, or other officer, who may arrest a person charged with any crime or offense, to take the defendant before the nearest United States commissioner or the nearest judicial officer having jurisdiction under existing laws for a hearing, commitment, or taking bail for trial * * *'. <span class="citation no-link">18 U.S.C. &#167; 595</span>, <span class="citation no-link">18 U.S.C.A. &#167; 595</span>. Similarly, the Act of June 18, 1934, c. 595, <span class="citation no-link">48 Stat. 1008</span>, 5 U.S.C. &#167; 300a, 5 U.S.C.A. &#167; 300a, authorizing officers of the Federal Bureau of Investigation to make arrests, requires that 'the person arrested shall be immediately taken before a committing officer.' Compare also the Act of March 1, 1879, c. 125, <span class="citation no-link">20 Stat. 327</span>, 341, <span class="citation no-link">18 U.S.C. &#167; 593</span>, <span class="citation no-link">18 U.S.C.A. &#167; 593</span>, which provides that when arrests are made of persons in the act of operating an illicit destillery, the arrested persons shall be taken forthwith before some judicial officer residing in the county where the arrests were made, or if none, in the county nearest to the place of arrest. Similar legislation, requiring that arrested persons be promptly taken before a committing authority, appears on the statute books of nearly all the states.<a class="footnote" href="#fn7" id="fn7_ref">7</a></p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">The purpose of this impressively pervasive requirement of criminal procedure is plain. A democratic society, in which respect for the dignity of all men is central, naturally guards against the misuse of the law enforcement process. Zeal in tracking down crime is not in itself an assurance of soberness of judgment. Disinterestendness in law enforcement does not alone prevent disregard of cherished liberties. Experience has therefore counseled that safeguards must be provided against the dangers of the overzealous as well as the despotic. The awful instruments of the criminal law cannot be entrusted to a single functionary. The complicated process of criminal justice is therefore divided into different parts, responsibility for which is separately vested in the various participants upon whom the criminal law relies for its vindication. Legislation such as this, requiring that the police must with reasonable promptness show legal cause for detaining arrested persons, constitutes an important safeguard&#8212;not only in assuring protection for the innocent but also in securing conviction of the guilty by methods that commend themselves to a progressive and self-confident society. For this procedural requirement checks resort to those reprehensible practices known as the 'third degree' which, though universally rejected as indefensible, still find their way into use. It aims to avoid all the evil implications of secret interrogation of persons accused of crime. It reflects not a sentimental but a sturdy view of law enforcement. It outlaws easy but self-defeating ways in which brutality is substituted for brains as an instrument of crime detection.<a class="footnote" href="#fn8" id="fn8_ref">8</a> A statute carrying such purposes is expressive of a general legislative policy to which courts should not be heedless when appropriate situations call for its application.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">The circumstances in which the statements admitted in evidence against the petitioners were secured reveal a plain disregard of the duty enjoined by Congress upon federal law officers. Freeman and Raymond McNabb were arrested in the middle of the night at their home. Instead of being brought before a United States Commissioner or a judicial officer, as the law requires, in order to determine the sufficiency of the justification for their detention, they were put in a barren cell and kept there for fourteen hours. For two days they were subjected to unremitting questioning by numerous officers. Benjamin's confession was secured by detaining him unlawfully and questioning him continuously for five or six hours. The McNabbs had to submit to all this without the aid of friends or the benefit of counsel. The record leaves no room for doubt that the questioning of the petitioners took place while they were in the custody of the arresting officers and before any order of commitment was made. Plainly, a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in wilful disobedience of law. Congress has not explicitly forbidden the use of evidence so procured. But to permit such evidence to be made the basis of a conviction in the federal courts would stultify the policy which Congress has enacted into law.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">Unlike England, where the Judges of the King's Bench have prescribed rules for the interrogation of prisoners while in the custody of police officers,<a class="footnote" href="#fn9" id="fn9_ref">9</a> we have no specific provisions of law governing federal law enforcement officers in procuring evidence from persons held in custody. But the absence of specific restraints going beyond the legislation to which we have referred does not imply that the circumstances under which evidence was secured are irrelevant in ascertaining its admissibility. The mere fact that a confession was made while in the custody of the police does not render it inadmissible. Compare Hopt v. Utah, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#583" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U.S. 574, 583</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#206" aria-description="Citation for case: Hopt v. People of Territory of Utah">4 S.Ct. 202, 206</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">28 L.Ed. 262</a></span>; Sparf v. United States, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#55" aria-description="Citation for case: Sparf v. United States">156 U.S. 51, 55, 715</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#275" aria-description="Citation for case: Sparf v. United States">15 S.Ct. 273, 275</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/" aria-description="Citation for case: Sparf v. United States">39 L.Ed. 343</a></span>; United States ex rel. Bilokumsky v. Tod, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U.S. 149, 157</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#57" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">44 S.Ct. 54, 57</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">68 L.Ed. 221</a></span>; Ziang Sun Wan v. United States, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1, 14</a></span>, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#3" aria-description="Citation for case: Ziang Sung Wan v. United States">45 S.Ct. 1, 3</a></span>, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">69 L.Ed. 131</a></span>. But where in the course of a criminal trial in the federal courts it appears that evidence has been obtained in such violation of legal rights as this case discloses, it is the duty of the trial court to entertain a motion for the exclusion of such evidence and to hold a hearing, as was done here, to determine whether such motion should be granted or denied. Cf. Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#312" aria-description="Citation for case: Gouled v. United States">255 U.S. 298, 312, 313</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#266" aria-description="Citation for case: Gouled v. United States">41 S.Ct. 261, 266</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L.Ed. 647</a></span>; Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S.Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L.Ed. 654</a></span>; Nardone v. United States, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U.S. 338, 341, 342</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#267" aria-description="Citation for case: Nardone v. United States">60 S.Ct. 266, 267, 268</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>. The interruption of the trial for this purpose should be no longer than is required for a competent determination of the substantiality of the motion. As was observed in the Nardone case, supra, 'The civilized conduct of criminal trials cannot be confined within mechanical rules. It necessarily demands the authority of limited direction entrusted to the judge presiding in federal trials, including a well-established range of judicial discretion, subject to appropriate review on appeal in ruling upon preliminary questions of fact. Such a system as ours must, within the limits here indicated, rely on the learning, good sense, fairness and courage of federal trial judges.' <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U.S. at page 342</a></span>, 60 S.Ct. at page 268, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">In holding that the petitioners' admissions were improperly received in evidence against them, and that having been based on this evidence their convictions cannot stand, we confine ourselves to our limited function as the court of ultimate review of the standards, formulated and applied by federal courts in the trial of criminal cases. We are not concerned with law enforcement practices except in so far as courts themselves become instruments of law enforcement. We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. In so doing, we respect the policy which underlies Congressional legislation. The history of liberty has largely been the history of observance of procedural safeguards. And the effective administration of criminal justice hardly requires disregard of fair procedures imposed by law.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Reversed.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Mr. Justice RUTLEDGE took no part in the consideration or decision of this case.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Mr. Justice REED, dissenting.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">I find myself unable to agree with the opinion of the Court in this case. An officer of the United States was killed while in the performance of his duties. From the circumstances detailed in the Court's opinion, there was obvious reason to suspect that the petitioners here were implicated in firing the fatal shot from the dark. The arrests followed. As the guilty parties were known only to the McNabbs who took part in the assault at the burying ground, it was natural and proper that the officers would question them as to their actions.<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a></p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">The cases just cited show that statements made while under interrogation may be used at a trial if it may fairly be said that the information was given voluntarily. A frank and free confession of crime by the culprit affords testimony of the highest credibility and of a character which may be verified easily. Equally frank responses to officers by innocent people arrested under misapprehension give the best basis for prompt discharge from custody. The realization of the convincing quality of a confession tempts officials to press suspects unduly for such statements. To guard accused persons against the danger of being forced to confess, the law admits confessions of guilt only when they are voluntarily made. While the connotation of voluntary is indefinite, it affords an understandable label under which can be readily classified the various acts of terrorism, promises, trickery and threats which have led this and other courts to refuse admission as evidence to confessions.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> The cases cited in the Court's opinion show the broad coverage of this rule of law. Through it those coerced into confession have found a ready defense from injustice.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">Were the Court today saying merely that in its judgment the confessions of the McNabbs were not voluntary, there would be no occasion for this single protest. A notation of dissent would suffice. The opinion, however, does more. Involuntary confessions are not constitutionally admissible because violative of the provision of self-incrimination in the Bill of Rights. Now the Court leaves undecided whether the present confessions are voluntary or involuntary and declares that the confessions must be excluded because in addition to questioning the petitioners, the arresting officers failed promptly to take them before a committing magistrate. The Court finds a basis for the declaration of this new rule of evidence in its supervisory authority over the administration of criminal justice. I question whether this offers to the trial courts and the peace officers a rule of admissibility as clear as the test of the voluntary character of the confession. I am opposed to broadening the possibilities of defendants escaping punishment by these more rigorous technical requirements in the administration of justice. If these confessions are otherwise voluntary, civilized standards, in my opinion, are not advanced by setting aside these judgments because of acts of omission which are not shown to have tended toward coercing the admissions.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">Our police officers occasionally overstep legal bounds. This record does not show when the petitioners were taken before a committing magistrate. No point was made of the failure to commit by defendant or counsel. No opportunity was given to the officers to explain. Objection to the introduction of the confessions was made only on the ground that they were obtained through coercion. This was determined against the accused both by the Court, when it appraised the fact as to the voluntary character of the confessions, preliminarily to determining the legal question of their admissibility, and by the jury. The Court saw and heard witnesses for the prosecution and the defense. The defendants did not take the stand before the jury. The uncontradicted evidence does not require a different conclusion. The officers of the Alcohol Tax Unit should not be disciplined by overturning this conviction.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Officer Burke testified that the questioning Thursday night began at 6 P.M., Officer Kitts, at 7 P.M., and Officer Jakes, at 'possibly 6 or 7 o'clock'.</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> Here again Taylor's testimony is at variance with that of other officers. Officer Kitts estimated that the questioning Thursday night ended at 10 P.M., Officer Burke, at 11 P.M., and Officer Jakes, at midnight. No officer testified that the questioning that night lasted less than three hours.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> Taylor testified that the McNabbs were brought back Friday morning 'probably about nine or nine-thirty'. None of the other officers could recall the exact time. Officer Burke thought 'it must have been after nine o'clock', while Officer Jakes guessed that it was 'somewhere around ten or eleven o'clock in the morning'.</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> Taylor testified that the reason for having Benjamin remove his clothes was that 'I was informed that he had gotten an injury running through the woods or that he had been hit by a stray shot. We didn't know whether or not this was true, and asked him to take his clothes off in order to examine him and find out.'</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> To determine the admissibility of the statements secured from the defendants while they were in the custody of the federal officers, the trial court conducted a preliminary examination in the absence of the jury. After hearing the evidence (consisting principally of the testimony of the defendants and the officers), the court concluded that the statements were admissible. An exception to this ruling was taken. When the jury was recalled, the witnesses for the Government repeated their testimony. The defendants rested upon their claim that the trial court erred in admitting these statements, and stood on their constitutional right not to take the witness stand before the jury. At the conclusion of the Government's case the defendants moved to exclude from the consideration of the jury the evidence relating to the admissions made by them. This motion was denied. The motion was renewed at the conclusion of the defendants' case, and again was denied. The court charged the jury that the defendants' admissions should be disregard if found to have been involuntarily made. The issue of law which was decided by the trial court in admitting the statements made by the petitioners did not become, therefore, a question of fact foreclosed by the jury's general verdict of guilty. Under these circumstances we have treated as facts only the testimony offered on behalf of the Government and so much of the petitioners' evidence as is neither contradicted by nor inconsistent with that of the Government.</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> The function of formulating rules of evidence in areas not governed by statute has always been one of the chief concerns of courts: 'The rules of evidence on which we practise today have mostly grown up at the hands of the judges; and, except as they may be really something more than rules of evidence, they may, in the main, properly enough be left to them to be modified and reshaped.' J. B. Thayer, A Preliminary Treatise on Evidence at the Common Law (1898) pp. 530, 531.</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> Alabama&#8212;Code, 1940, Tit. 15, &#167; 160; Arizona&#8212;Code, 1939, &#167;&#167; 44-107, 44-140, 44-141; Arkansas&#8212;Pope's Digest of Statutes, 1937, &#167;&#167; 3729, 3731; California&#8212;Penal Code, 1941, &#167;&#167; 821&#8212;29, 847&#8212;49; Colorado&#8212;Statutes, 1935, c. 48, &#167; 428; Connecticut&#8212;Gen.Stats.1930, &#167; 239; Delaware&#8212;Rev.Code, 1935, &#167;&#167; 4456, 5173; District of Columbia&#8212;Code, 1940, &#167;&#167; 4-140, 23-301; Florida&#8212;Statutes, 1941, &#167;&#167; 901.06, 901.23; Georgia&#8212;Code, 1933, &#167;&#167; 27-210, 27-212; Idaho&#8212;Code, 1932, &#167;&#167; 19-515, 19-518, 19-614, 19-615; Illinois&#8212;Rev.Stats., 1941, c. 38, &#167;&#167; 655, 660; Indiana&#8212;Baldwin's Stats.Ann.1934, &#167; 11484; Iowa&#8212;Code, 1939, &#167;&#167; 13478, 13481, 13486, 13488; Kansas Gen.Stats., 1935, &#167; 62-610; Kentucky&#8212;Code, 1938, &#167;&#167; 45, 46; Louisiana&#8212;Code of Criminal Procedure, 1932, arts. 66, 79, 80; Maine&#8212;Rev.Stats., 1930, c. 145, &#167; 9; Massachusetts-Gen.Laws, 1932, c. 276, &#167;&#167; 22, 29, 34; Michigan&#8212;Stats.Ann.1938, &#167;&#167; 28.863, 28.872, 28.873, 28.885; Minnesota&#8212;Mason's Stats., 1927, c. 104, &#167;&#167; 10575, 10581; Mississippi&#8212;Code, 1930, c. 21, &#167; 1230; Missouri Rev.Stats.1939, &#167;&#167; 3862, 3883, Mo.R.S.A. &#167;&#167; 3862, 3883; Montana Rev.Code, 1935, &#167;&#167; 11731, 11739, 11740; Nebraska&#8212;Comp.Stats., 1929, &#167; 29-412; Nevada&#8212;Comp.Laws, 1929, &#167;&#167; 10744&#8212;48, 10762&#8212;64; New Hampshire&#8212;Pub.Laws, 1926, c. 364, &#167; 13; New Jersey&#8212;Rev.Stats., 1937, &#167; 2:216&#8212;9, N.J.S.A. 2:216&#8212;9; New York&#8212;Code of Criminal Procedure, 1939, &#167;&#167; 158, 159, 165, 185; North Carolina&#8212;Code, 1939, &#167;&#167; 4528, 4548; North Dakota&#8212;Comp.Laws, 1913, &#167;&#167; 10543, 10548, 10576, 10578; Ohio&#8212;Throckmorton's Code, 1940, &#167;&#167; 13432-3, 13432-4; Oklahoma&#8212;Statutes, 1941, Tit. 22, &#167;&#167; 176, 177, 181, 205; Oregon Code, 1930, &#167;&#167; 13-2117, 13-2201; Pennsylvania&#8212;Purdon's Stats.Ann., Perm.ed., Tit. 19, &#167;&#167; 3, 4; Rhode Island&#8212;Gen.Laws, 1938, c. 625, &#167; 68; South Carolina&#8212;Code, 1942, &#167;&#167; 907, 920; South Dakota&#8212;Code, 1939, &#167;&#167; 34-1608, 34-1619 to 34-1624; Tennessee&#8212;Michie's Code, 1938, &#167;&#167; 11515, 11544; Texas&#8212;Vernon's Code of Criminal Procedure, 1936, Arts. 233&#8212;235; Utah&#8212;Rev.Stats., 1933, &#167;&#167; 105-4-4, 105-4-5, 103-26-51; Virginia&#8212;Code, 1942, &#167;&#167; 4826, 4827a; Washington Rev.Stats., 1932, &#167; 1949; West Virginia&#8212;Code, 1937, &#167; 6150; Wisconsin&#8212;Statutes, 1941, &#167; 361.08; Wyoming&#8212;Rev.Stats., 1931, &#167;&#167; 33-108, 33-110, 33-115.</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> 'During the discussions which took place on the Indian Code of Criminal Procedure in 1872 some observations were made on the reasons which occasionally lead native police officers to apply torture to prisoners. An experienced civil officer observed, 'There is a great deal of laziness in it. It is far pleasanter to sit comfortably in the shade rubbing red pepper into a poor devil's eyes than to go about in the sun hunting up evidence.' This was a new view to me, but I have no doubt of its truth.' Sir James Fitzjames Stephen, A History of the Criminal Law of England (1883) vol. 1, p. 442 note. Compare &#167;&#167; 25 and 26 of the Indian Evidence Act 1872).</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> In 1912 the Judges of the King's Bench, at the request of the Home Secretary, issued rules for the guidance of police officers. See Rex v. Voisin, L.R. (1918) 1 K.B 531, 539. These rules were amended in 1918, and in 1930 a circular was issued by the Home Office, with the approval of the Judges, in order to clear up difficulties in their construction. 6 Police Journal (1933) 352-56, containing the texts of the Judge's Rules and the Circular. See Report of the Royal Commission on Police Powers and Procedure (1929) Cmd. 3297. Although the Rules do not have the force of law, Rex v. Voisin, supra, the English courts insist that they be strictly observed before admitting statements made by accused persons while in the custody of the police. See 1 Taylor on Evidence (12th ed. 1931) pp. 556&#8212;562; 'Questioning an Accused Person', 92 Justice of the Peace and Local Government Review 743, 758 (1928); Keedy, Preliminary Examination of Accused Persons in England, 73 Proceedings of American Philosophical Society 103 (1934). For a dramatic illustration of the English attitude towards interrogation of arrested persons by the police, see Inquiry in regard to the Interrogation by the Police of Miss Savidge (1928) Cmd. 3147.</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> Hopt v. Utah, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#584" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U.S. 574, 584</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#207" aria-description="Citation for case: Hopt v. People of Territory of Utah">4 S.Ct. 202, 207</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">28 L.Ed. 262</a></span>; Sparf &amp; Hansen v. United States, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#55" aria-description="Citation for case: Sparf v. United States">156 U.S. 51, 55, 715</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#275" aria-description="Citation for case: Sparf v. United States">15 S.Ct. 273, 275</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/" aria-description="Citation for case: Sparf v. United States">39 L.Ed. 343</a></span>; Pierce v. United States, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">160 U.S. 355</a></span>, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">16 S.Ct. 321</a></span>, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">40 L.Ed. 454</a></span>; Wilson v. United States, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#623" aria-description="Citation for case: Wilson v. United States">162 U.S. 613, 623</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#899" aria-description="Citation for case: Wilson v. United States">16 S.Ct. 895, 899</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">40 L.Ed. 1090</a></span>; cf. State ex rel. Bilokumsky v. Tod, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U.S. 149, 157</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#57" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">44 S.Ct. 54, 57</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">68 L.Ed. 221</a></span>.</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> 'In short, the true test of admissibility is that the confession is made freely, voluntarily and without compulsion or inducement of any sort.' Wilson v. United States, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#623" aria-description="Citation for case: Wilson v. United States">162 U.S. 613, 623</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#899" aria-description="Citation for case: Wilson v. United States">16 S.Ct. 895, 899</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">40 L.Ed. 1090</a></span>; Lisenba v. California, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#239" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 239</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#291" aria-description="Citation for case: Lisenba v. California">62 S.Ct. 280, 291</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">86 L.Ed. 166</a></span>.</p>
      </div>
    </div>
    
```

---

## GROUP: _overhaul2/lake/cases/McNeil v. Wisconsin.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "McNeil v. Wisconsin"
type: case
citation: "501 U.S. 171 (1991)"
parallel_cite: "111 S. Ct. 2204; 115 L. Ed. 2d 158"
neutral_cite: 1991 U.S. LEXIS 3483
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: McNeil v. Wisconsin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112622/mcneil-v-wisconsin/"
  cluster_id: 112622
  opinion_id: 9432329
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Michigan v. Jackson]]", "[[Montejo v. Louisiana]]", "[[Massiah v. United States]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "offense-specific", "miranda"]
holding: "The Sixth Amendment right to counsel is offense-specific, and a 6A invocation is NOT an invocation of the Fifth Amendment *Miranda-Edwards* right to counsel; the two are distinct."
lake:
  record_id: McNeil v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# McNeil v. Wisconsin

*501 U.S. 171 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
McNeil appeared with a public defender at a bail hearing on a West Allis armed robbery. While he was jailed, police later gave him [[Miranda and Custodial Interrogation|Miranda warnings]] and questioned him about a separate set of crimes in Caledonia; he waived his rights and made incriminating statements. He argued that his courtroom appearance with counsel on the West Allis charge barred any police-initiated questioning on the uncharged Caledonia offenses.

## Issue
Whether an accused's invocation of the Sixth Amendment right to counsel at a proceeding on one charged offense also invokes the Fifth Amendment *[[Miranda v. Arizona|Miranda]]*-*[[Edwards v. Arizona|Edwards]]* right to counsel so as to bar police-initiated interrogation about other, uncharged offenses.

## Rule
No. "The Sixth Amendment right, however, is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced." — 501 U.S. at 175. ^pin-175

Because the Sixth Amendment right is offense-specific, invoking it as to a charged offense does not invoke the distinct Fifth Amendment *[[Miranda v. Arizona|Miranda]]*-*[[Edwards v. Arizona|Edwards]]* right to counsel, which guards against custodial interrogation generally; the two rights serve different interests and are not interchangeable.

## Application
McNeil's Sixth Amendment right had attached and been invoked only as to the West Allis armed robbery with which he had been formally charged. His appearance with counsel on that charge did not invoke the separate Fifth Amendment *[[Miranda v. Arizona|Miranda]]* right; and because the Caledonia offenses were still uncharged, no Sixth Amendment right had attached to them. His subsequent *[[Miranda v. Arizona|Miranda]]* waivers before the Caledonia questioning were therefore valid.

## Conclusion
Affirmed; the statements were admissible.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *McNeil*'s offense-specific holding remains good law. It relied in part on [[Michigan v. Jackson]] (since **overruled** by [[Montejo v. Louisiana]]), but that later development does not disturb *McNeil*'s distinct holding that the Sixth Amendment right is offense-specific and separate from the *[[Miranda v. Arizona|Miranda]]* right.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *McNeil v. Wisconsin*, 501 U.S. 171 (1991) — https://www.courtlistener.com/opinion/112622/mcneil-v-wisconsin/ — pinpoint: 175.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b3aa22c691725491", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "McNeil v. Wisconsin"}, "payload": {"all": [{"cite": "501 U.S. 171", "page": "171", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "501"}, {"cite": "111 S. Ct. 2204", "page": "2204", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "115 L. Ed. 2d 158", "page": "158", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "115"}, {"cite": "1991 U.S. LEXIS 3483", "page": "3483", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}], "display": "501 U.S. 171", "official": {"cite": "501 U.S. 171", "page": "171", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "501"}, "official_selection_present": true, "record_id": "McNeil v. Wisconsin"}}
{"assertion_id": "722a38a31a3c5954", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-175", "record_id": "McNeil v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-175", "pinpoint_status": "slip-only", "quote": "--- # McNeil v. Wisconsin *501 U.S. 171 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeil appeared with a public defender at a bail hearing on a West Allis armed robbery. While he was jailed, police later gave him Miranda warnings and questioned him about a separate set of crimes in Caledonia; he waived his rights and made incriminating statements. He argued that his courtroom appearance with counsel on the West Allis charge barred any police-initiated questioning on the uncharged Caledonia offenses. ## Issue Whether an accused's invocation of the Sixth Amendment right to counsel at a proceeding on one charged offense also invokes the Fifth Amendment *Miranda*-*Edwards* right to counsel so as to bar police-initiated interrogation about other, uncharged offenses. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "McNeil v. Wisconsin", "star_marker": null}}
{"assertion_id": "7d72d7020263cbbd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "McNeil v. Wisconsin"}, "payload": {"as_of_content": "1991-06-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "McNeil v. Wisconsin", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — McNeil v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "McNeil v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "McNeil v. Wisconsin",
    "case_name_short": "McNeil",
    "case_name_full": "McNEIL v. WISCONSIN",
    "input_case_name": "McNeil v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-06-13",
    "year": 1991,
    "docket": null,
    "cluster_id": 112622,
    "lead_opinion_id": 9432329,
    "sibling_ids": [
      112622,
      9432329,
      9432330,
      9432331
    ],
    "absolute_url": "/opinion/112622/mcneil-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9104955,
        "score": 20,
        "case_name": "McNeil v. Wisconsin"
      },
      {
        "cluster_id": 9104954,
        "score": 20,
        "case_name": "McNeil v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "501 U.S. 171",
      "volume": "501",
      "reporter": "U.S.",
      "page": "171",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 2204",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 158",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 3483",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3483",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "501 U.S. 171",
        "volume": "501",
        "reporter": "U.S.",
        "page": "171",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 2204",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 158",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 3483",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3483",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "501 U.S. 171",
    "official_selection": {
      "court_class": "scotus",
      "selected": "501 U.S. 171",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-175",
      "page": null,
      "quote": "--- # McNeil v. Wisconsin *501 U.S. 171 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeil appeared with a public defender at a bail hearing on a West Allis armed robbery. While he was jailed, police later gave him Miranda warnings and questioned him about a separate set of crimes in Caledonia; he waived his rights and made incriminating statements. He argued that his courtroom appearance with counsel on the West Allis charge barred any police-initiated questioning on the uncharged Caledonia offenses. ## Issue Whether an accused's invocation of the Sixth Amendment right to counsel at a proceeding on one charged offense also invokes the Fifth Amendment *Miranda*-*Edwards* right to counsel so as to bar police-initiated interrogation about other, uncharged offenses. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "McNeil v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guillermo Hernandez Ruiz v. State of Iowa",
          "cluster_id": 4501180,
          "cite": [
            "912 N.W.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
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
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Saldierna",
          "cluster_id": 4332369,
          "cite": [
            "369 N.C. 401",
            "794 S.E.2d 474",
            "2016 N.C. LEXIS 1117"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ward v. Lamar University",
          "cluster_id": 5446494,
          "cite": [
            "484 S.W.3d 440",
            "2016 Tex. App. LEXIS 260",
            "2016 WL 145817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vicki Ward v. Lamar University, Texas State University System and James Simmons",
          "cluster_id": 2979722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tio Sessoms v. D Runnels",
          "cluster_id": 2736109,
          "cite": [
            "768 F.3d 882",
            "2014 U.S. App. LEXIS 18237",
            "2014 WL 4668005"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doggett v. United States",
          "cluster_id": 112780,
          "cite": [
            "120 L. Ed. 2d 520",
            "112 S. Ct. 2686",
            "505 U.S. 647",
            "1992 U.S. LEXIS 4362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 1476684,
          "cite": [
            "859 A.2d 364",
            "181 N.J. 391",
            "2004 N.J. LEXIS 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lawrence",
          "cluster_id": 2501123,
          "cite": [
            "723 S.E.2d 326",
            "365 N.C. 506",
            "2012 WL 1242316",
            "2012 N.C. LEXIS 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 1743739,
          "cite": [
            "937 S.W.2d 456",
            "1996 Tex. Crim. App. LEXIS 240",
            "1996 WL 682137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sherwood",
          "cluster_id": 1995264,
          "cite": [
            "982 A.2d 483",
            "603 Pa. 92",
            "2009 Pa. LEXIS 2359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "MacK v. State",
          "cluster_id": 1751529,
          "cite": [
            "650 So. 2d 1289",
            "1994 WL 707272"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie v. State",
          "cluster_id": 1706565,
          "cite": [
            "585 So. 2d 660",
            "1991 WL 142136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Russell Clark v. Tim Murphy",
          "cluster_id": 782256,
          "cite": [
            "331 F.3d 1062",
            "2003 Cal. Daily Op. Serv. 4923",
            "2003 Daily Journal DAR 6263",
            "2003 U.S. App. LEXIS 11496",
            "2003 WL 21338911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk5NTA3MjAwMDAwJnM9MjY3MzAxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjAmcz0xNDQ3ODgxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
        "reviewed": 39,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 39,
        "triage_read": 1,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
    "indexed_citing_opinions": 1145,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112622,
        "count": 1017,
        "count_source": "search"
      },
      {
        "opinion_id": 9432329,
        "count": 152,
        "count_source": "search"
      },
      {
        "opinion_id": 9432330,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432331,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1820,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mcneil-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MjQ5Nzkmcz0xMDExMTk0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112622,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 484283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 1190975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 2207530,
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
    "date_created": "2026-07-05T13:00:42Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:05:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — McNeil v. Wisconsin

```
<opinion type="majority">
<author id="b243-4"><page-number citation-index="1" label="173">*173</page-number>Justice Scalia</author>
<p id="AhX">delivered the opinion of the Court.</p>
<p id="b243-5">This case presents the question whether an accused’s invocation of his Sixth Amendment right to counsel during a judicial proceeding constitutes an invocation of his <em>Miranda </em>right to counsel.</p>
<p id="b243-6">I</p>
<p id="b243-7">Petitioner Paul McNeil was arrested in Omaha, Nebraska, in May 1987, pursuant to a warrant charging him with an armed robbery in West Allis, Wisconsin, a suburb of Milwaukee. Shortly after his arrest, two Milwaukee County deputy sheriffs arrived in Omaha to retrieve him. After advising him of his <em>Miranda </em>rights, the deputies sought to question him. He refused to answer any questions, but did not request an attorney. The deputies promptly ended the interview.</p>
<p id="b243-8">Once back in Wisconsin, petitioner was brought before a Milwaukee County Court Commissioner on the armed robbery charge. The Commissioner set bail and scheduled a preliminary examination. An attorney from the Wisconsin Public Defender’s Office represented petitioner at this initial appearance.</p>
<p id="b243-9">Later that evening, Detective Joseph Butts of the Milwaukee County Sheriff’s Department visited petitioner in jail. Butts had been assisting the Racine County, Wisconsin, police in their investigation of a murder, attempted murder, and armed burglary in the town of Caledonia; petitioner was a suspect. Butts advised petitioner of his <em>Miranda </em>rights, and petitioner signed a form waiving them. In this <page-number citation-index="1" label="174">*174</page-number>first interview, petitioner did not deny knowledge of the Caledonia crimes, but said that he had not been involved.</p>
<p id="b244-5">Butts returned two donia. He again began the encounter by advising petitioner of his <em>Miranda </em>rights and providing a waiver form. Petitioner placed his initials next to each of the warnings and signed the form. This time, petitioner admitted that he had been involved in the Caledonia crimes, which he described in detail. He also implicated two other men, Willie Pope and Lloyd Crowley. The statement was typed up by a detective and given to petitioner to review. Petitioner placed his initials next to every reference to himself and signed every page.</p>
<p id="b244-6">Butts and the Caledonia having in the meantime found and questioned Pope, who convinced them that he had not been involved in the Caledonia crimes. They again began the interview by administering the <em>Miranda </em>warnings and obtaining petitioner’s signature and initials on the waiver form. Petitioner acknowledged that he had lied about Pope’s involvement to minimize his own role in the Caledonia crimes and provided another statement recounting the events, which was transcribed, signed, and initialed as before.</p>
<p id="b244-7">The following day, petitioner was the Caledonia crimes and transferred to that jurisdiction. His pretrial motion to suppress the three incriminating statements was denied. He was convicted of second-degree murder, attempted first-degree murder, and armed robbery, and sentenced to 60 years in prison.</p>
<p id="b244-8">On appeal, petitioner argued that the trial court’s refusal to suppress the statements was reversible error. He contended that his courtroom appearance with an attorney for the West Allis crime constituted an invocation of the <em>Miranda </em>right to counsel, and that any subsequent waiver of that right during police-initiated questioning regarding <em>any </em>offense was invalid. Observing that the State’s Supreme <page-number citation-index="1" label="175">*175</page-number>Court had never addressed this issue, the Court of Appeals certified to that court the following question:</p>
<blockquote id="b245-5">“Does an accused’s request for counsel at an initial appearance on a charged offense constitute an invocation of his fifth amendment right to counsel that precludes police-initiated interrogation on unrelated, uncharged offenses?” App. 16.</blockquote>
<p id="b245-6">The Wisconsin Supreme Court answered “no.” <span class="citation" data-id="9736821"><a href="/opinion/2207530/state-v-mcneil/" aria-description="Citation for case: State v. McNeil">155 Wis. 2d 24</a></span>, <span class="citation" data-id="9736821"><a href="/opinion/2207530/state-v-mcneil/" aria-description="Citation for case: State v. McNeil">454 N. W. 2d 742</a></span> (1990). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./498/937/">498 U. S. 937</a></span> (1990).</p>
<p id="b245-7">II</p>
<p id="b245-8">The Sixth Amendment provides that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defence.” In <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), we held that once this right to counsel has attached and has been invoked, any subsequent waiver during a police-initiated .custodial interview is ineffective. It is undisputed, and we accept for purposes of the present case, that at the time petitioner provided the incriminating statements at issue, his Sixth Amendment right had attached and had been invoked with respect to the <em>West Allis armed robbery, </em>for which he had been formally charged.</p>
<p id="b245-9">Sixth Amendment right, however, is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced, that is, “ ‘at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.’” <em>United States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 188</a></span> (1984) (quoting <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972) (plurality opinion)). And just as the right is offense specific, so also its <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>effect of invalidating subsequent waivers in police-initiated interviews is offense specific.</p>
<blockquote id="b245-10">“The police have an interest... in investigating new or additional crimes [after an individual is formally charged <page-number citation-index="1" label="176">*176</page-number>with one crime.] . . . [T]o exclude evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities. . . .” <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#179" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 179-180</a></span> (1985).</blockquote>
<blockquote id="b246-5">“Incriminating statements pertaining to other crimes, as <em>to </em>which the Sixth Amendment right has not yet attached, are, of course, admissible at a trial of those offenses.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#180" aria-description="Citation for case: Maine v. Moulton"><em>Id., </em>at 180, n. 16</a></span>.</blockquote>
<p id="b246-6">See also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#431" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 431</a></span> (1986). Because petitioner provided the statements at issue here before his Sixth Amendment right to counsel with respect to the <em>Caledonia offenses </em>had been (or even could have been) invoked, that right poses no bar to the admission of the statements in this case.</p>
<p id="b246-7">Petitioner relies, however, upon a different “right to counsel,” found not in the text of the Sixth Amendment, but in this Court’s jurisprudence relating to the Fifth Amendment guarantee that “[n]o person . . . shall be compelled in any criminal case to be a witness against himself.” In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we established a number of prophylactic rights designed to counteract the “inherently compelling pressures” of custodial interrogation, including the right to have counsel present. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>did not hold, however, that those rights could not be waived. On the contrary, the opinion recognized that statements elicited during custodial interrogation would be admissible if the prosecution could establish that the suspect “knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 475</a></span>.</p>
<p id="b246-8">In <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), we established a second layer of prophylaxis for the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel: Once a suspect asserts the right, not only must the <page-number citation-index="1" label="177">*177</page-number>current interrogation cease, but he may not be approached for further interrogation “until counsel has been made available to him,” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>-485—which means, we have most recently held, that counsel must be present, <em>Minnick </em>v. <em>Mississippi, </em><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146</a></span> (1990). If the police do subsequently initiate an encounter in the absence of counsel (assuming there has been no break in custody), the suspect’s statements are presumed involuntary and therefore inadmissible as substantive evidence at trial, even where the suspect executes a waiver and his statements would be considered voluntary under traditional standards. This is “designed to prevent police from badgering a defendant into waiving his previously asserted <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights,” <em>Michigan </em>v. <em>Harvey, </em><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, moreover, is <em>not </em>offense specific: Once a suspect invokes the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel for interrogation regarding one offense, he may not be reapproached regarding <em>any </em>offense unless counsel is present. <em>Arizona </em>v. <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988).</p>
<p id="b247-5">Having described the nature and effects of both the Sixth Amendment right to counsel and the <em>Miranda-Edwards </em>“Fifth Amendment” right to counsel, we come at last to the issue here: Petitioner seeks to prevail by combining the two of them. He contends that, although he expressly waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel on every occasion he was interrogated, those waivers were the invalid product of impermissible approaches, because his prior invocation of the offense-specific Sixth Amendment right with regard to the West Allis burglary was also an invocation of the nonoffense-specific <em>Miranda-Edwards </em>right. We think that is false as a matter of fact and inadvisable (if even permissible) as a contrary-to-fact presumption of policy.</p>
<p id="b247-6">As to the former: The purpose of the Sixth Amendment counsel guarantee — and hence the purpose of invoking it — is to “protec[t] the unaided layman at critical confrontations” with his “expert adversary,” the government, <em>after </em>“the ad<page-number citation-index="1" label="178">*178</page-number>verse positions of government and defendant have solidified” with respect to a particular alleged crime. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#189" aria-description="Citation for case: United States v. Gouveia">467 U. S., at 189</a></span>. The purpose of the <em>Miranda-Edwards </em>guarantee, on the other hand — and hence the purpose of invoking it — is to protect a quite different interest: the suspect’s “desire to deal with the police only through counsel,” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">Edwards, <em>supra, </em>at 484</a></span>. This is in one respect narrower than the interest protected by the Sixth Amendment guarantee (because it relates only to custodial interrogation) and in another respect broader (because it relates to interrogation regarding <em>any </em>suspected crime and attaches whether or not the “adversarial relationship” produced by a pending prosecution has yet arisen). To invoke the Sixth Amendment interest is, as a matter of <em>fact, not </em>to invoke the <em>Miranda-Edwards </em>interest. One might be quite willing to speak to the police without counsel present concerning many matters, but not the matter under prosecution. It can be said, perhaps, that it is <em>likely </em>that one who has asked for counsel’s assistance in defending against a prosecution would want counsel present for all custodial interrogation, even interrogation unrelated to the charge. That is not necessarily true, since suspects often believe that they can avoid the laying of charges by demonstrating an assurance of innocence through frank and unassisted answers to questions. But even if it were true, the <em>likelihood </em>that a suspect would wish counsel to be present is not the test for applicability of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>The rule of that case applies only when the suspect “ha[s] <em>expressed” </em>his wish for the particular sort of lawyerly assistance that is the subject of <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Miranda. Edwards, supra, </em>at 484</a></span> (emphasis added). It requires, at a minimum, some statement that can reasonably be construed to be an expression of a desire for the assistance of an attorney <em>in dealing with custodial interrogation by the police. </em>Requesting the assistance of an attorney at a bail hearing does not bear that construction. “[T]o find that [the defendant] invoked his Fifth Amendment right to counsel on the present charges merely by requesting <page-number citation-index="1" label="179">*179</page-number>the appointment of counsel at his arraignment on the unrelated charge is to disregard the ordinary meaning of that request.” <em>State </em>v. <em>Stewart, </em><span class="citation" data-id="1190975"><a href="/opinion/1190975/state-v-stewart/#471" aria-description="Citation for case: State v. Stewart">113 Wash. 2d 462, 471</a></span>, <span class="citation" data-id="1190975"><a href="/opinion/1190975/state-v-stewart/#849" aria-description="Citation for case: State v. Stewart">780 P. 2d 844, 849</a></span> (1989), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./494/1020/">494 U. S. 1020</a></span> (1990).</p>
<p id="b249-5">Our holding in <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), does not, as petitioner asserts, contradict the foregoing distinction; to the contrary, it <em>rests </em>upon it. That case, it will be recalled, held that after the Sixth Amendment right to counsel attaches and is invoked, any statements obtained from the accused during subsequent police-initiated custodial questioning regarding the charge at issue (even if the accused purports to waive his rights) are inadmissible. The State in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>opposed that outcome on the ground that assertion of the Sixth Amendment right to counsel did not realistically constitute the <em>expression </em>(as <em>Edivards </em>required) of a wish to have counsel present during custodial interrogation. See 475 U. S., at 632-633. Our response to that contention was not that it <em>did </em>constitute such an expression, but that it <em>did not have to, </em>since the relevant question was not whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“Fifth Amendment” right had been <em>asserted, </em>but whether the Sixth Amendment right to counsel had been <em>waived. </em>We said that since our “settled approach to questions of waiver requires us to give a broad, rather than a narrow, interpretation to a defendant’s request for counsel, ... we <em>presume </em>that the defendant requests the lawyer’s services at every critical stage of the prosecution.” 475 U. S., at 633 (emphasis added). The holding of <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>implicitly rejects any equivalence in fact between invocation of the Sixth Amendment right to counsel and the expression necessary to trigger <em>Edivards. </em>If such invocation constituted a real (as opposed to merely a legally presumed) request for the assistance of counsel in custodial interrogation, it would have been quite unnecessary for <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>to go on to establish, as it did, a new Sixth Amendment rule of no police-<page-number citation-index="1" label="180">*180</page-number>initiated interrogation; we could simply have cited and relied upon <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em><footnotemark><em>1</em></footnotemark></p>
<p id="b250-5">There remains to though the assertion of the Sixth Amendment right to counsel does not <em>in fact </em>imply an assertion of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“Fifth Amendment” right, we should declare it to be. such as a matter of sound policy. Assuming we have such an expansive power under the Constitution, it would not wisely be exercised. Petitioner’s proposed rule has only insignificant advantages. If a suspect does not wish to communicate with the police except through an attorney, he can simply tell them that when they give him the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. There is not the remotest chance that he will feel “badgered” by their asking to talk to him without counsel present, since the subject will not be the charge on which he has already requested counsel’s assistance (for in that event <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>would preclude initiation of the interview) and he will not have rejected uncounseled interrogation on <em>any </em>subject before (for in that event <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>would preclude initiation of the interview). The proposed rule would, however, seriously impede effective law enforcement. The Sixth Amendment right to <page-number citation-index="1" label="181">*181</page-number>counsel attaches at the first formal proceeding against an accused, and in most States, at least with respect to serious offenses, free counsel is made available at that time and ordinarily requested. Thus, if we were to adopt petitioner’s rule, most persons in pretrial custody for serious offenses would be <em>unapproachable </em>by police officers suspecting them of involvement in other crimes, <em>even though they have never expressed any unwillingness to be questioned. </em>Since the ready ability to obtain uncoerced confessions is not an evil but an unmitigated good, society would be the loser. Admissions of guilt resulting from valid <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waivers “are more than merely ‘desirable’; they are essential to society’s compelling interest in finding, convicting, and punishing those who violate the law.” <em>Moran, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 426</a></span> (citation omitted).<footnotemark>2</footnotemark></p>
<p id="b251-5">Petitioner urges upon us the desirability of providing a “clear and unequivocal” guideline for the police: no police-initiated questioning of any person in custody who has requested counsel to assist him in defense or in interrogation. But the police do not need our assistance to establish such a <page-number citation-index="1" label="182">*182</page-number>guideline; they are free, if they wish, to adopt it on their own. Of course it <em>is </em>our task to establish guidelines for judicial review. We like <em>them </em>to be “clear and unequivocal,” see, <em>e. </em>g., <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#681" aria-description="Citation for case: Arizona v. Roberson">486 U. S., at 681-682</a></span>, but only when they guide sensibly and in a direction we are authorized to go. Petitioner’s proposal would in our view do much more harm than good, and is not contained within, or even in furtherance of, the Sixth Amendment’s right to counsel or the Fifth Amendment’s right against compelled self-incrimination.<footnotemark>3</footnotemark></p>
<p id="b252-5">* * *</p>
<p id="b252-6">"This Court is forever adding new stories to the temples of constitutional law, and the temples have a way of collapsing when one story too many is added.” <em>Douglas </em>v. <em>Jeannette, </em><span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/#181" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157, 181</a></span> (1943) (opinion of Jackson, J.). We decline to add yet another story to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The judgment of the Wisconsin Supreme Court is</p>
<p id="A4bd">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b250-6"> A footnote in <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 633-634, n. 7</a></span>, quoted with approval statements by the Michigan Supreme Court to the effect that the average person does not ‘“understand and appreciate the subtle distinctions between the Fifth and Sixth Amendment rights to counsel,’” that it “‘makes little sense to afford relief from further interrogation to a defendant who asks a police officer for an attorney, but permit further interrogation to a defendant who makes an identical request to a judge,’ ” and that “ ‘[t]he simple fact that defendant has requested an attorney indicates that he does not believe that he is sufficiently capable of dealing with his adversaries singlehandedly.’” <em>Michigan </em>v. <em>Bladel, </em><span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#63" aria-description="Citation for case: People v. Bladel">421 Mich. 39, 63-64</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#67" aria-description="Citation for case: People v. Bladel">365 N. W. 2d 56, 67</a></span> (1984). Those observations were perhaps true in the context of deciding whether a request for the assistance of counsel in defending against a particular charge implied a desire to have that counsel serve as an “intermediary” for all further interrogation on that charge. They are assuredly not true in the quite different context of deciding whether such a request implies a desire never to undergo custodial interrogation, about anything, without counsel present.</p>
</footnote>
<footnote label="2">
<p id="b251-6"> The dissent condemns these sentiments as “revealing a preference for an inquisitorial system of justice.” <em>Post, </em>at 189. We cannot imagine what this means. What makes a system adversarial rather than inquisitorial is not the presence of counsel, much less the presence of counsel where the defendant has not requested it; but rather, the presence of a judge who does not (as an inquisitor does) conduct the factual and legal investigation himself, but instead decides on the basis of facts and arguments pro and con adduced by the parties. In the inquisitorial criminal process of the civil law, the defendant ordinarily has counsel; and in the adversarial criminal process of the common law, he sometimes does not. Our system of justice is, and has always been, an inquisitorial one at the investigatory stage (even the grand jury is an inquisitorial body), and no other disposition is conceivable. Even if detectives were to bring impartial magistrates around with them to all interrogations, there would be no decision for the impartial magistrate to umpire. If all the dissent means by a “preference for an inquisitorial system” is a preference not to require the presence of counsel during an investigatory interview where the interviewee has not requested it — that is a strange way to put it, but we are guilty.</p>
</footnote>
<footnote label="3">
<p id="b252-8"> The dissent predicts that the result in this case will routinely be circumvented when, “[i]n future preliminary hearings, competent counsel. . . make sure that they, or their clients, make a statement on the record” invoking the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel. <em>Post, </em>at 184. We have in fact never held that a person can invoke his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights anticipatorily, in a context other than “custodial interrogation” — which a preliminary hearing will not always, or even usually, involve, cf. <em>Pennsylvania </em>v. <em>Muniz, </em><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#601" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 601-602</a></span> (1990) (plurality opinion); <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 298-303</a></span> (1980). If the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel can be invoked at a preliminary hearing, it could be argued, there is no logical reason why it could not be invoked by a letter prior to arrest, or indeed even prior to identification as a suspect. Most rights must be asserted when the government seeks to take the action they protect against. The fact that we have allowed the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel, once asserted, to be effective with respect to future custodial interrogation does not necessarily mean that we will allow it to be asserted initially outside the context of custodial interrogation, with similar future effect. Assuming, however, that an assertion at arraignment would be effective, and would be routinely made, the mere fact that adherence to the principle of our decisions will not have substantial consequences is no reason to abandon that principle. It would remain intolerable that a person in custody who had expressed <em>no </em>objection to being questioned would be unapproachable.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Messerschmidt v. Millender.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Messerschmidt v. Millender"
type: case
citation: "565 U.S. 535 (2012)"
parallel_cite: "132 S. Ct. 1235; 182 L. Ed. 2d 47"
neutral_cite: 2012 U.S. LEXIS 1687
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-02-22
docket: 10-704
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-02-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Messerschmidt v. Millender
  varies_by_point: false
  scope_note: Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/"
  cluster_id: 623242
  opinion_id: 623242
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Franks Challenges]]"
    role: "Related (cross-doctrine)"
related: ["[[Malley v. Briggs]]", "[[United States v. Leon]]", "[[Harlow v. Fitzgerald]]", "[[Pearson v. Callahan]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "warrant", "overbroad-warrant", "objective-reasonableness"]
holding: "Officers retain qualified immunity for obtaining and executing a facially overbroad warrant where their reliance on the magistrate's approval was objectively reasonable; the Malley exception is a high threshold."
lake:
  record_id: Messerschmidt v. Millender
  status: verified
  projected_at: 2026-07-09
---

# Messerschmidt v. Millender

*565 U.S. 535 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Jerry Bowen assaulted his former girlfriend with "a black sawed-off shotgun with a pistol grip" and fired at her as she fled, Detective Messerschmidt prepared a warrant to search Augusta Millender's home — where Bowen was thought to live — for **all firearms** and **all gang-related material**. The warrant was reviewed and approved by a supervisor, a deputy district attorney, and a magistrate before execution. The Millenders sued the officers under § 1983, alleging the warrant was unconstitutionally overbroad.

## Issue
Whether officers are entitled to [[Qualified Immunity|qualified immunity]] from a § 1983 damages suit for obtaining and executing a warrant later alleged to be overbroad, where a neutral magistrate approved the warrant.

## Rule
Officers are immune unless the warrant was so obviously deficient that no reasonable officer could have relied on it. A magistrate's approval is strong evidence of objective reasonableness, but it does not end the inquiry: "the fact that a neutral magistrate has issued a warrant authorizing the allegedly unconstitutional search or seizure does not end the inquiry into objective reasonableness." — 565 U.S. at 547. ^pin-547

The exception, drawn from [[Malley v. Briggs]] and [[United States v. Leon]], applies only where the affidavit is "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable." — *Id.* (quoting *Leon*, 468 U.S. at 923). But "the threshold for establishing this exception is a high one, and it should be." — [*Id.*](https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/#:~:text=so%20lacking%20in%20indicia%20of) ^pin-547b

## Application
The warrant's authorization to seize all firearms and gang material was at least arguably supported: Bowen had used a firearm in the assault and was a known gang member, so an officer could reasonably believe the broad categories were tied to evidence of the crime and of Bowen's dangerousness and gang ties. Even if the warrant was in fact overbroad, the question was only whether reliance on it was objectively reasonable — and the additional review by a supervisor, a prosecutor, and the magistrate confirmed that this was not the rare case where every reasonable officer would have known the warrant should not issue.

## Conclusion
Reversed. The officers were entitled to [[Qualified Immunity|qualified immunity]]; their reliance on the approved warrant was not objectively unreasonable, so the *[[Malley v. Briggs|Malley]]* exception did not strip their immunity.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Messerschmidt* applies the [[Malley v. Briggs]] / [[United States v. Leon]] standard to the warrant-immunity question and sits within the qualified-immunity framework of [[Harlow v. Fitzgerald]] and [[Pearson v. Callahan]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Franks Challenges]] — *Related (cross-doctrine)*

## Sources
- *Messerschmidt v. Millender*, 565 U.S. 535 (2012) — https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/ — pinpoint: 547 (lead opinion id 9485385).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3427a77c06ed5bb7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Messerschmidt v. Millender"}, "payload": {"all": [{"cite": "132 S. Ct. 1235", "page": "1235", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "182 L. Ed. 2d 47", "page": "47", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "182"}, {"cite": "2012 U.S. LEXIS 1687", "page": "1687", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}, {"cite": "565 U.S. 535", "page": "535", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}], "display": "565 U.S. 535", "official": {"cite": "565 U.S. 535", "page": "535", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "Messerschmidt v. Millender"}}
{"assertion_id": "834dd05db0a40ade", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-547", "record_id": "Messerschmidt v. Millender"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-547", "pinpoint_status": "slip-only", "quote": "and fired at her as she fled, Detective Messerschmidt prepared a warrant to search Augusta Millender's home — where Bowen was thought to live — for **all firearms** and **all gang-related material**. The warrant was reviewed and approved by a supervisor, a deputy district attorney, and a magistrate before execution. The Millenders sued the officers under § 1983, alleging the warrant was unconstitutionally overbroad. ## Issue Whether officers are entitled to qualified immunity from a § 1983 damages suit for obtaining and executing a warrant later alleged to be overbroad, where a neutral magistrate approved the warrant. ## Rule Officers are immune unless the warrant was so obviously deficient that no reasonable officer could have relied on it. A magistrate's approval is strong evidence of objective reasonableness, but it does not end the inquiry:", "quote_fidelity": "mismatch", "record_id": "Messerschmidt v. Millender", "star_marker": null}}
{"assertion_id": "a4fd95e2545900f9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-547b", "record_id": "Messerschmidt v. Millender"}, "payload": {"fragment": "#:~:text=so%20lacking%20in%20indicia%20of", "page": null, "pin_id": "pin-547b", "pinpoint_status": "slip-only", "quote": "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable.", "quote_fidelity": "matched", "record_id": "Messerschmidt v. Millender", "star_marker": null}}
{"assertion_id": "8ef42894b2b66197", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Messerschmidt v. Millender"}, "payload": {"as_of_content": "2012-02-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Messerschmidt v. Millender", "scope_note": "Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.", "varies_by_point": false}}
```

### lake record — Messerschmidt v. Millender

```json
{
  "schema_version": "s2.v1",
  "record_id": "Messerschmidt v. Millender",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Messerschmidt v. Millender",
    "case_name_short": "Messerschmidt",
    "case_name_full": "MESSERSCHMIDT Et Al. v. MILLENDER, Executor of ESTATE OF MILLENDER, DECEASED, Et Al.",
    "input_case_name": "Messerschmidt v. Millender",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-02-22",
    "year": 2012,
    "docket": "10-704",
    "cluster_id": 623242,
    "lead_opinion_id": 623242,
    "sibling_ids": [
      623242,
      9485385,
      9485386,
      9485387,
      9485388
    ],
    "absolute_url": "/opinion/623242/messerschmidt-v-millender/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 535",
      "volume": "565",
      "reporter": "U.S.",
      "page": "535",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1235",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 47",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1687",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1235",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 47",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1687",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 535",
        "volume": "565",
        "reporter": "U.S.",
        "page": "535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 535",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 535",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-547",
      "page": null,
      "quote": "and fired at her as she fled, Detective Messerschmidt prepared a warrant to search Augusta Millender's home \u2014 where Bowen was thought to live \u2014 for **all firearms** and **all gang-related material**. The warrant was reviewed and approved by a supervisor, a deputy district attorney, and a magistrate before execution. The Millenders sued the officers under \u00a7 1983, alleging the warrant was unconstitutionally overbroad. ## Issue Whether officers are entitled to qualified immunity from a \u00a7 1983 damages suit for obtaining and executing a warrant later alleged to be overbroad, where a neutral magistrate approved the warrant. ## Rule Officers are immune unless the warrant was so obviously deficient that no reasonable officer could have relied on it. A magistrate's approval is strong evidence of objective reasonableness, but it does not end the inquiry:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-547b",
      "page": null,
      "quote": "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 5024,
      "fragment": "#:~:text=so%20lacking%20in%20indicia%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-02-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Messerschmidt v. Millender",
    "varies_by_point": false,
    "scope_note": "Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa Matt Reineke, Individually and in His Official Capacity as an Officer of the Estherville Police Department and Matt Hellickson, Individually and in His Official Capacity as an Officer of the Estherville Police Department",
          "cluster_id": 4512940,
          "cite": [
            "915 N.W.2d 259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lauren Graham v. C. Gagnon",
          "cluster_id": 4242146,
          "cite": [
            "831 F.3d 176",
            "2016 U.S. App. LEXIS 13672",
            "2016 WL 4011156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cion Peralta v. T. Dillard",
          "cluster_id": 814919,
          "cite": [
            "704 F.3d 1124",
            "2013 U.S. App. LEXIS 379",
            "2013 WL 57893"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DiStiso ex rel. DiStiso v. Cook",
          "cluster_id": 807074,
          "cite": [
            "691 F.3d 226",
            "2012 WL 3570755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felders v. Malcom",
          "cluster_id": 2679716,
          "cite": [
            "755 F.3d 870",
            "2014 WL 2782368",
            "2014 U.S. App. LEXIS 11627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. Does 1-40",
          "cluster_id": 8442118,
          "cite": [
            "779 F.3d 84",
            "2014 U.S. App. LEXIS 24772",
            "2015 WL 737758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andy Thayer v. Ralph Chiczewski",
          "cluster_id": 808703,
          "cite": [
            "705 F.3d 237",
            "2012 U.S. App. LEXIS 26899",
            "2012 WL 6621169"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Davidson v. City of Stafford, Texas, et a",
          "cluster_id": 4346685,
          "cite": [
            "848 F.3d 384",
            "2017 WL 507305",
            "2017 U.S. App. LEXIS 2189"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby Bland v. B. Roberts",
          "cluster_id": 1041207,
          "cite": [
            "730 F.3d 368",
            "36 I.E.R. Cas. (BNA) 1045",
            "41 Media L. Rep. (BNA) 2445",
            "2013 WL 5228033",
            "2013 U.S. App. LEXIS 19268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leona Mullins v. Oscar Cyranek",
          "cluster_id": 3153107,
          "cite": [
            "805 F.3d 760",
            "2015 FED App. 0273P",
            "2015 U.S. App. LEXIS 19485",
            "2015 WL 6859303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stonecipher v. Valles",
          "cluster_id": 2681550,
          "cite": [
            "759 F.3d 1134",
            "2014 U.S. App. LEXIS 12384",
            "2014 WL 2937038"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zalaski v. City of Hartford",
          "cluster_id": 1034747,
          "cite": [
            "723 F.3d 382",
            "2013 WL 3796448",
            "2013 U.S. App. LEXIS 14898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "April Smith v. Jason Munday",
          "cluster_id": 4345933,
          "cite": [
            "848 F.3d 248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rex Chappell v. R. Mandeville",
          "cluster_id": 818032,
          "cite": [
            "706 F.3d 1052",
            "2013 WL 364203",
            "2013 U.S. App. LEXIS 2192"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathson Fields v. Lawrence Wharrie",
          "cluster_id": 2708971,
          "cite": [
            "740 F.3d 1107",
            "2014 WL 243245",
            "2014 U.S. App. LEXIS 1333"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clint Small v. James McCrystal",
          "cluster_id": 820762,
          "cite": [
            "708 F.3d 997",
            "2013 WL 599567",
            "2013 U.S. App. LEXIS 3372"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frank Snider, III v. Matthew Peters",
          "cluster_id": 2676418,
          "cite": [
            "752 F.3d 1149"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lal v. California",
          "cluster_id": 8441683,
          "cite": [
            "746 F.3d 1112",
            "2014 WL 1272781"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul Pavulak",
          "cluster_id": 812356,
          "cite": [
            "700 F.3d 651",
            "2012 U.S. App. LEXIS 24036",
            "2012 WL 5870742"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turkmen v. Hasty",
          "cluster_id": 8442249,
          "cite": [
            "789 F.3d 218",
            "2015 U.S. App. LEXIS 10160",
            "2015 WL 3756331"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eddie Ford v. City of Yakima",
          "cluster_id": 820004,
          "cite": [
            "706 F.3d 1188",
            "2013 U.S. App. LEXIS 2716",
            "2013 WL 485233"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ganek v. Leibowitz",
          "cluster_id": 4434937,
          "cite": [
            "874 F.3d 73",
            "2017 WL 4639594",
            "2017 U.S. App. LEXIS 20226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesby v. District of Columbia",
          "cluster_id": 2722589,
          "cite": [
            "412 U.S. App. D.C. 246",
            "765 F.3d 13",
            "2014 U.S. App. LEXIS 16893",
            "2014 WL 4290316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Almighty Supreme Born Allah v. Milling",
          "cluster_id": 8443619,
          "cite": [
            "876 F.3d 48"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Avina v. United States",
          "cluster_id": 802109,
          "cite": [
            "681 F.3d 1127",
            "2012 WL 2099257",
            "2012 U.S. App. LEXIS 11876"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 137,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 137,
        "triage_read": 4,
        "triage_snippet_classified": 133
      },
      "lane2_top_cited": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNyZzPTgwNjExOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28623242+OR+9485385+OR+9485386+OR+9485387+OR+9485388%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 0,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
    "indexed_citing_opinions": 182,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 623242,
        "count": 127,
        "count_source": "search"
      },
      {
        "opinion_id": 9485385,
        "count": 59,
        "count_source": "search"
      },
      {
        "opinion_id": 9485386,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485387,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485388,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 873,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/messerschmidt-v-millender.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2MzM0Nzkmcz05NDY3ODE5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28623242+OR+9485385+OR+9485386+OR+9485387+OR+9485388%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 623242,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 173961,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 1122997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 1192791,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T13:05:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:09:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Messerschmidt v. Millender

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

MESSERSCHMIDT ET AL. v. MILLENDER, EXECUTOR OF
   ESTATE OF MILLENDER, DECEASED, ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

  No. 10–704.     Argued December 5, 2011—Decided February 22, 2012
Shelly Kelly was afraid that she would be attacked by her boyfriend,
  Jerry Ray Bowen, while she moved out of her apartment. She there-
  fore requested police protection. Two officers arrived, but they were
  called away to an emergency. As soon as the officers left, Bowen
  showed up at the apartment, yelled “I told you never to call the cops
  on me bitch!” and attacked Kelly, attempting to throw her over a se-
  cond-story landing. After Kelly escaped to her car, Bowen pointed a
  sawed-off shotgun at her and threatened to kill her if she tried to
  leave. Kelly nonetheless sped away as Bowen fired five shots at the
  car, blowing out one of its tires.
     Kelly later met with Detective Curt Messerschmidt to discuss the
  incident. She described the attack in detail, mentioned that Bowen
  had previously assaulted her, that he had ties to the Mona Park
  Crips gang, and that he might be staying at the home of his former
  foster mother, Augusta Millender. Following this conversation, Mes-
  serschmidt conducted a detailed investigation, during which he con-
  firmed Bowen’s connection to the Millenders’ home, verified his
  membership in two gangs, and learned that Bowen had been arrested
  and convicted for numerous violent and firearm-related offenses.
  Based on this investigation, Messerschmidt drafted an application
  for a warrant authorizing a search of the Millenders’ home for all
  firearms and ammunition, as well as evidence indicating gang
  membership.
     Messerschmidt included two affidavits in the warrant application.
  The first detailed his extensive law enforcement experience and his
  specialized training in gang-related crimes. The second, expressly in-
  corporated into the search warrant, described the incident and ex-
2                  MESSERSCHMIDT v. MILLENDER

                                 Syllabus

    plained why Messerschmidt believed there was probable cause for the
    search. It also requested that the warrant be endorsed for night ser-
    vice because of Bowen’s gang ties. Before submitting the application
    to a magistrate for approval, Messerschmidt had it reviewed by his
    supervisor, Sergeant Robert Lawrence, as well as a police lieutenant
    and a deputy district attorney. Messerschmidt then submitted the
    application to a magistrate, who issued the warrant. The ensuing
    search uncovered only Millender’s shotgun, a California Social Ser-
    vices letter addressed to Bowen, and a box of .45-caliber ammunition.
       The Millenders filed an action under 42 U. S. C. §1983 against pe-
    titioners Messerschmidt and Lawrence, alleging that the officers had
    subjected them to an unreasonable search in violation of the Fourth
    Amendment. The District Court granted summary judgment to the
    Millenders, concluding that the firearm and gang-material aspects of
    the search warrant were overbroad and that the officers were not en-
    titled to qualified immunity from damages. The Ninth Circuit, sit-
    ting en banc, affirmed the denial of qualified immunity. The court
    held that the warrant’s authorization was unconstitutionally over-
    broad because the affidavits and warrant failed to establish probable
    cause that the broad categories of firearms, firearm-related material,
    and gang-related material were contraband or evidence of a crime,
    and that a reasonable officer would have been aware of the warrant’s
    deficiency.
Held: The officers are entitled to qualified immunity. Pp. 8−19.
    (a) Qualified immunity “protects government officials ‘from liability
 for civil damages insofar as their conduct does not violate clearly es-
 tablished statutory or constitutional rights of which a reasonable
 person would have known.’ ” Pearson v. Callahan, 555 U. S. 223, 231.
 Where the alleged Fourth Amendment violation involves a search or
 seizure pursuant to a warrant, the fact that a neutral magistrate has
 issued a warrant is the clearest indication that the officers acted in
 an objectively reasonable manner, or in “objective good faith.” United
 States v. Leon, 468 U. S. 897, 922–923. Nonetheless, that fact does
 not end the inquiry into objective reasonableness. The Court has rec-
 ognized an exception allowing suit when “it is obvious that no rea-
 sonably competent officer would have concluded that a warrant
 should issue.” Malley v. Briggs, 475 U. S. 335, 341. The “shield of
 immunity” otherwise conferred by the warrant, id., at 345, will be
 lost, for example, where the warrant was “based on an affidavit so
 lacking in indicia of probable cause as to render official belief in its
 existence entirely unreasonable.” Leon, 468 U. S., at 923. The
 threshold for establishing this exception is high. “[I]n the ordinary
 case, an officer cannot be expected to question the magistrate’s prob-
 able-cause determination” because “[i]t is the magistrate’s responsi-
                   Cite as: 565 U. S. ____ (2012)                    3

                              Syllabus

bility to determine whether the officer’s allegations establish proba-
ble cause and, if so, to issue a warrant comporting in form with the
requirements of the Fourth Amendment.” Leon, supra, at 921. Pp.
8−10.
   (b) This case does not fall within that narrow exception. It would
not be entirely unreasonable for an officer to believe that there was
probable cause to search for all firearms and firearm-related materi-
als. Under the circumstances set forth in the warrant, an officer
could reasonably conclude that there was a “fair probability” that the
sawed-off shotgun was not the only firearm Bowen owned, Illinois v.
Gates, 462 U. S. 213, 238, and that Bowen’s sawed-off shotgun was il-
legal. Cf. 26 U. S. C. §§ 5845(a), 5861(d). Given Bowen’s possession
of one illegal gun, his gang membership, willingness to use the gun to
kill someone, and concern about the police, it would not be unreason-
able for an officer to conclude that Bowen owned other illegal guns.
An officer also could reasonably believe that seizure of firearms was
necessary to prevent further assaults on Kelly. California law allows
a magistrate to issue a search warrant for items “in the possession of
any person with the intent to use them as a means of committing a
public offense,” Cal. Penal Code Ann. §1524(a)(3), and the warrant
application submitted by the officers specifically referenced this pro-
vision as a basis for the search. Pp. 10–12.
   (c) Regarding the warrant’s authorization to search for gang-
related materials, a reasonable officer could view Bowen’s attack as
motivated not by the souring of his romantic relationship with Kelly
but by a desire to prevent her from disclosing details of his gang ac-
tivity to the police. It would therefore not be unreasonable—based on
the facts set out in the affidavit—for an officer to believe that evi-
dence of Bowen’s gang affiliation would prove helpful in prosecuting
him for the attack on Kelly, in supporting additional, related charges
against Bowen for the assault, or in impeaching Bowen or rebutting
his defenses. Moreover, even if this were merely a domestic dispute,
a reasonable officer could still conclude that gang paraphernalia
found at the Millenders’ residence could demonstrate Bowen’s control
over the premises or his connection to other evidence found there.
Pp. 12−16.
   (d) The fact that the officers sought and obtained approval of the
warrant application from a superior and a deputy district attorney
before submitting it to the magistrate provides further support for
the conclusion that an officer could reasonably have believed that the
scope of the warrant was supported by probable cause. A contrary
conclusion would mean not only that Messerschmidt and Lawrence
were “plainly incompetent” in concluding that the warrant was sup-
ported by probable cause, Malley, supra, at 341, but that their super-
4                  MESSERSCHMIDT v. MILLENDER

                                  Syllabus

    visor, the deputy district attorney, and the magistrate were as well.
    Pp. 16−18.
       (e) In holding that the warrant in this case was so obviously defec-
    tive that no reasonable officer could have believed it to be valid, the
    court below erred in relying on Groh v. Ramirez, 540 U. S. 551.
    There, officers who carried out a warrant-approved search were not
    entitled to qualified immunity because the warrant failed to describe
    any of the items to be seized and “even a cursory reading of the war-
    rant” would have revealed this defect. Id., at 557. Here, in contrast,
    any arguable defect would have become apparent only upon a close
    parsing of the warrant application, and a comparison of the support-
    ing affidavit to the terms of the warrant to determine whether the af-
    fidavit established probable cause to search for all the items listed in
    the warrant. Unlike in Groh, any error here would not be one that
    “just a simple glance” would have revealed. Id. at 564. Pp. 18−19.
620 F. 3d 1016, reversed.

  ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, THOMAS, BREYER, and ALITO, JJ., joined. BREYER, J., filed a
concurring opinion. KAGAN, J., filed an opinion concurring in part and
dissenting in part. SOTOMAYOR, J., filed a dissenting opinion, in which
GINSBURG, J., joined.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–704
                                   _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                              [February 22, 2012]


   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   Petitioner police officers conducted a search of respond-
ents’ home pursuant to a warrant issued by a neutral
magistrate. The warrant authorized a search for all guns
and gang-related material, in connection with the investi-
gation of a known gang member for shooting at his ex-
girlfriend with a pistol-gripped sawed-off shotgun, because
she had “call[ed] the cops” on him. App. 56. Respondents
brought an action seeking to hold the officers personally
liable under 42 U. S. C. §1983, alleging that the search
violated their Fourth Amendment rights because there
was not sufficient probable cause to believe the items
sought were evidence of a crime. In particular, respond-
ents argued that there was no basis to search for all
guns simply because the suspect owned and had used a
sawed-off shotgun, and no reason to search for gang mate-
rial because the shooting at the ex-girlfriend for “call[ing]
the cops” was solely a domestic dispute. The Court of
2             MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

Appeals for the Ninth Circuit held that the warrant was
invalid, and that the officers were not entitled to immu-
nity from personal liability because this invalidity was so
obvious that any reasonable officer would have recognized
it, despite the magistrate’s approval. We disagree and
reverse.
                               I

                               A

  Shelly Kelly decided to break off her romantic relation-
ship with Jerry Ray Bowen and move out of her apart-
ment, to which Bowen had a key. Kelly feared an attack
from Bowen, who had previously assaulted her and had
been convicted of multiple violent felonies. She therefore
asked officers from the Los Angeles County Sheriff’s De-
partment to accompany her while she gathered her things.
Deputies from the Sheriff ’s Department came to assist
Kelly but were called away to respond to an emergency
before the move was complete.
  As soon as the officers left, an enraged Bowen appeared
at the bottom of the stairs to the apartment, yelling “I told
you never to call the cops on me bitch!” App. 39, 56.
Bowen then ran up the stairs to Kelly, grabbed her by her
shirt, and tried to throw her over the railing of the second-
story landing. When Kelly successfully resisted, Bowen
bit her on the shoulder and attempted to drag her inside
the apartment by her hair. Kelly again managed to escape
Bowen’s grasp, and ran to her car. By that time, Bowen
had retrieved a black sawed-off shotgun with a pistol grip.
He ran in front of Kelly’s car, pointed the shotgun at her,
and told Kelly that if she tried to leave he would kill her.
Kelly leaned over, fully depressed the gas pedal, and sped
away. Bowen fired at the car a total of five times, blowing
out the car’s left front tire in the process, but Kelly man-
aged to escape.
  Kelly quickly located police officers and reported the
                 Cite as: 565 U. S. ____ (2012)          3

                     Opinion of the Court

assault. She told the police what had happened—that
Bowen had attacked her after becoming “angry because
she had called the Sheriff’s Department”—and she men-
tioned that Bowen was “an active member of the ‘Mona
Park Crips,’ ” a local street gang. Id., at 39. Kelly also
provided the officers with photographs of Bowen.
   Detective Curt Messerschmidt was assigned to investi-
gate the incident. Messerschmidt met with Kelly to obtain
details of the assault and information about Bowen. Kelly
described the attack and informed Messerschmidt that she
thought Bowen was staying at his foster mother’s home
at 2234 East 120th Street. Kelly also informed Messer-
schmidt of Bowen’s previous assaults on her and of his
gang ties.
   Messerschmidt then conducted a background check on
Bowen by consulting police records, California Depart-
ment of Motor Vehicles records, and the “cal-gang” data-
base. Based on this research, Messerschmidt confirmed
Bowen’s connection to the 2234 East 120th Street address.
He also confirmed that Bowen was an “active” member of
the Mona Park Crips and a “secondary” member of the
Dodge City Crips. Id., at 64. Finally, Messerschmidt
learned that Bowen had been arrested and convicted for
numerous violent and firearm-related offenses. Indeed, at
the time of the investigation, Bowen’s “rapsheet” spanned
over 17 printed pages, and indicated that he had been
arrested at least 31 times. Nine of these arrests were for
firearms offenses and six were for violent crimes, includ-
ing three arrests for assault with a deadly weapon (fire-
arm). Id., at 72–81.
   Messerschmidt prepared two warrants: one to authorize
Bowen’s arrest and one to authorize the search of 2234
East 120th Street. An attachment to the search warrant
described the property that would be the object of the
search:
4             MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

    “All handguns, rifles, or shotguns of any caliber, or
    any firearms capable of firing ammunition, or fire-
    arms or devices modified or designed to allow it [sic]
    to fire ammunition. All caliber of ammunition, miscel-
    laneous gun parts, gun cleaning kits, holsters which
    could hold or have held any caliber handgun being
    sought. Any receipts or paperwork, showing the pur-
    chase, ownership, or possession of the handguns being
    sought. Any firearm for which there is no proof of
    ownership. Any firearm capable of firing or cham-
    bered to fire any caliber ammunition.
    “Articles of evidence showing street gang membership
    or affiliation with any Street Gang to include but not
    limited to any reference to ‘Mona Park Crips’, includ-
    ing writings or graffiti depicting gang membership,
    activity or identity. Articles of personal property
    tending to establish the identity of person [sic] in con-
    trol of the premise or premises. Any photographs or
    photograph albums depicting persons, vehicles, weap-
    ons or locations, which may appear relevant to gang
    membership, or which may depict the item being
    sought and or believed to be evidence in the case being
    investigated on this warrant, or which may depict ev-
    idence of criminal activity. Additionally to include
    any gang indicia that would establish the persons be-
    ing sought in this warrant, affiliation or membership
    with the ‘Mona Park Crips’ street gang.” Id., at 52.

  Two affidavits accompanied Messerschmidt’s warrant ap-
plications. The first affidavit described Messerschmidt’s
extensive law enforcement experience, including that he
had served as a peace officer for 14 years, that he was
then assigned to a “specialized unit” “investigating gang
related crimes and arresting gang members for various
violations of the law,” that he had been involved in “hun-
                 Cite as: 565 U. S. ____ (2012)           5

                     Opinion of the Court

dreds of gang related incidents, contacts, and or arrests”
during his time on the force, and that he had “received
specialized training in the field of gang related crimes”
and training in “gang related shootings.” Id., at 53–54.
   The second affidavit—expressly incorporated into the
search warrant—explained why Messerschmidt believed
there was sufficient probable cause to support the war-
rant. That affidavit described the facts of the incident
involving Kelly and Bowen in great detail, including the
weapon used in the assault. The affidavit recounted that
Kelly had identified Bowen as the assailant and that she
thought Bowen might be found at 2234 East 120th Street.
It also reported that Messerschmidt had “conducted an
extensive background search on the suspect by utilizing
departmental records, state computer records, and other
police agency records,” and that from that information he
had concluded that Bowen resided at 2234 East 120th
Street. Id., at 58.
   The affidavit requested that the search warrant be
endorsed for night service because “information provided
by the victim and the cal-gang data base” indicated that
Bowen had “gang ties to the Mona Park Crip gang” and
that “night service would provide an added element of
safety to the community as well as for the deputy person-
nel serving the warrant.” Id., at 59. The affidavit con-
cluded by noting that Messerschmidt “believe[d] that the
items sought” would be in Bowen’s possession and that
“recovery of the weapon could be invaluable in the success-
ful prosecution of the suspect involved in this case, and
the curtailment of further crimes being committed.” Ibid.
   Messerschmidt submitted the warrants to his super-
visors—Sergeant Lawrence and Lieutenant Ornales—for
review. Deputy District Attorney Janet Wilson also re-
viewed the materials and initialed the search warrant,
indicating that she agreed with Messerschmidt’s assess-
ment of probable cause. Id., at 27, 47. Finally, Messer-
6             MESSERSCHMIDT v. MILLENDER

                    Opinion of the Court

schmidt submitted the warrants to a magistrate. The
magistrate approved the warrants and authorized night
service.
  The search warrant was served two days later by a team
of officers that included Messerschmidt and Lawrence.
Sheriff’s deputies forced open the front door of 2234 East
120th Street and encountered Augusta Millender—a
woman in her seventies—and Millender’s daughter and
grandson. As instructed by the police, the Millenders
went outside while the residence was secured but re-
mained in the living room while the search was conducted.
Bowen was not found in the residence. The search did,
however, result in the seizure of Augusta Millender’s
shotgun, a California Social Services letter addressed to
Bowen, and a box of .45-caliber ammunition.
  Bowen was arrested two weeks later after Messer-
schmidt found him hiding under a bed in a motel room.
                             B
   The Millenders filed suit in Federal District Court
against the County of Los Angeles, the sheriff ’s depart-
ment, the sheriff, and a number of individual officers,
including Messerschmidt and Lawrence. The complaint
alleged, as relevant here, that the search warrant was
invalid under the Fourth Amendment. It sought damages
from Messerschmidt and Lawrence, among others.
   The parties filed cross motions for summary judgment
on the validity of the search warrant. The District Court
found the warrant defective in two respects. The District
Court concluded that the warrant’s authorization to
search for firearms was unconstitutionally overbroad
because the “crime specified here was a physical assault
with a very specific weapon”—a black sawed-off shotgun
with a pistol grip—negating any need to “search for all
firearms.” Millender v. County of Los Angeles, Civ. No.
05–2298 (CD Cal., Mar. 15, 2007), App. to Pet. for Cert.
                 Cite as: 565 U. S. ____ (2012)            7

                     Opinion of the Court

106, 157, 2007 WL 7589200, *21. The court also found
the warrant overbroad with respect to the search for gang-
related materials, because there “was no evidence that the
crime at issue was gang-related.” App. to Pet. for Cert.
157. As a result, the District Court granted summary
judgment to the Millenders on their constitutional chal-
lenges to the firearm and gang material aspects of the
search warrant. Id., at 160. The District Court also re-
jected the officers’ claim that they were entitled to quali-
fied immunity from damages. Id., at 171.
   Messerschmidt and Lawrence appealed, and a divided
panel of the Court of Appeals for the Ninth Circuit re-
versed the District Court’s denial of qualified immunity.
564 F. 3d 1143 (2009). The court held that the officers
were entitled to qualified immunity because “they reason-
ably relied on the approval of the warrant by a deputy
district attorney and a judge.” Id., at 1145.
   The Court of Appeals granted rehearing en banc and
affirmed the District Court’s denial of qualified immunity.
620 F. 3d 1016 (CA9 2010). The en banc court concluded
that the warrant’s authorization was unconstitutionally
overbroad because the affidavit and the warrant failed to
“establish[ ] probable cause that the broad categories of
firearms, firearm-related material, and gang-related
material described in the warrant were contraband or
evidence of a crime.” Id., at 1033. In the en banc court’s
view, “the deputies had probable cause to search for a
single, identified weapon . . . . They had no probable cause
to search for the broad class of firearms and firearm-
related materials described in the warrant.” Id., at 1027.
In addition, “[b]ecause the deputies failed to establish any
link between gang-related materials and a crime, the
warrant authorizing the search and seizure of all gang-
related evidence [was] likewise invalid.” Id., at 1031.
Concluding that “a reasonable officer in the deputies’
position would have been well aware of this deficiency,”
8              MESSERSCHMIDT v. MILLENDER

                      Opinion of the Court

the en banc court held that the officers were not entitled to
qualified immunity. Id., at 1033–1035.
  There were two separate dissenting opinions. Judge
Callahan determined that “the officers had probable cause
to search for and seize any firearms in the home in which
Bowen, a gang member and felon, was thought to reside.”
Id., at 1036. She also concluded that “the officers reason-
ably relied on their superiors, the district attorney, and
the magistrate to correct” any overbreadth in the warrant,
and that the officers were entitled to qualified immunity
because their actions were not objectively unreasonable.
Id., at 1044, 1049. Judge Silverman also dissented, con-
cluding that the “deputies’ belief in the validity of . . . the
warrant was entirely reasonable” and that the “record
[wa]s totally devoid of any evidence that the deputies
acted other than in good faith.” Id., at 1050. Judge Tall-
man joined both dissents.
  We granted certiorari. 564 U. S. ___ (2011).
                              II
  The Millenders allege that they were subjected to an
unreasonable search in violation of the Fourth Amend-
ment because the warrant authorizing the search of their
home was not supported by probable cause. They seek
damages from Messerschmidt and Lawrence for their roles
in obtaining and executing this warrant. The validity of
the warrant is not before us. The question instead is
whether Messerschmidt and Lawrence are entitled to im-
munity from damages, even assuming that the warrant
should not have been issued.
  “The doctrine of qualified immunity protects govern-
ment officials ‘from liability for civil damages insofar as
their conduct does not violate clearly established statutory
or constitutional rights of which a reasonable person
would have known.’ ” Pearson v. Callahan, 555 U. S. 223,
231 (2009) (quoting Harlow v. Fitzgerald, 457 U. S. 800,
                     Cite as: 565 U. S. ____ (2012)                   9

                         Opinion of the Court

818 (1982)). Qualified immunity “gives government offi-
cials breathing room to make reasonable but mistaken
judgments,” and “protects ‘all but the plainly incompetent
or those who knowingly violate the law.’ ” Ashcroft v. al-
Kidd, 563 U. S. ___, ___ (2011) (slip op., at 12) (quoting
Malley v. Briggs, 475 U. S. 335, 341 (1986)). “[W]hether
an official protected by qualified immunity may be held
personally liable for an allegedly unlawful official action
generally turns on the ‘objective legal reasonableness’ of
the action, assessed in light of the legal rules that were
‘clearly established’ at the time it was taken.” Anderson v.
Creighton, 483 U. S. 635, 639 (1987) (citation omitted).
   Where the alleged Fourth Amendment violation involves
a search or seizure pursuant to a warrant, the fact that a
neutral magistrate has issued a warrant is the clearest
indication that the officers acted in an objectively reason-
able manner or, as we have sometimes put it, in “objective
good faith.” United States v. Leon, 468 U. S. 897, 922–923
(1984).1 Nonetheless, under our precedents, the fact that
a neutral magistrate has issued a warrant authorizing the
allegedly unconstitutional search or seizure does not end
the inquiry into objective reasonableness. Rather, we
have recognized an exception allowing suit when “it is
obvious that no reasonably competent officer would have
concluded that a warrant should issue.” Malley, 475 U. S.,
at 341. The “shield of immunity” otherwise conferred by
the warrant, id., at 345, will be lost, for example, where
the warrant was “based on an affidavit so lacking in indi-
cia of probable cause as to render official belief in its exist-
——————
   1 Although Leon involved the proper application of the exclusionary

rule to remedy a Fourth Amendment violation, we have held that “the
same standard of objective reasonableness that we applied in the con-
text of a suppression hearing in Leon defines the qualified immun-
ity accorded an officer” who obtained or relied on an allegedly invalid
warrant. Malley v. Briggs, 475 U. S. 335, 344 (1986) (citation omitted);
Groh v. Ramirez, 540 U. S. 551, 565, n. 8 (2004).
10               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

ence entirely unreasonable.” Leon, 468 U. S., at 923 (in-
ternal quotation marks omitted).2
   Our precedents make clear, however, that the threshold
for establishing this exception is a high one, and it should
be. As we explained in Leon, “[i]n the ordinary case, an
officer cannot be expected to question the magistrate’s
probable-cause determination” because “[i]t is the magis-
trate’s responsibility to determine whether the officer’s
allegations establish probable cause and, if so, to issue a
warrant comporting in form with the requirements of the
Fourth Amendment.” Id., at 921; see also Malley, supra,
at 346, n. 9 (“It is a sound presumption that the magis-
trate is more qualified than the police officer to make a
probable cause determination, and it goes without saying
that where a magistrate acts mistakenly in issuing a
warrant but within the range of professional competence
of a magistrate, the officer who requested the warrant
cannot be held liable” (internal quotation marks and
citation omitted)).
                              III
  The Millenders contend, and the Court of Appeals held,
that their case falls into this narrow exception. According
to the Millenders, the officers “failed to provide any facts
or circumstances from which a magistrate could properly
conclude that there was probable cause to seize the broad
classes of items being sought,” and “[n]o reasonable officer
——————
  2 The dissent relies almost entirely on facts outside the affidavit,

including Messerschmidt’s deposition testimony, post, at 4, 11 (opinion
of SOTOMAYOR, J.), crime analysis forms, post, at 5, Kelly’s interview,
post, at 5–6, and n. 5, Messerschmidt’s notes regarding Kelly’s inter-
view, post, at 5–6, n. 5, and even several briefs filed in the District
Court and the Court of Appeals, post, at 8–9, 12. In contrast, the
dissent cites the probable cause affidavit itself only twice. See post, at
12. There is no contention before us that the affidavit was misleading
in omitting any of the facts on which the dissent relies. Cf. Leon, 468
U. S., at 923.
                 Cite as: 565 U. S. ____ (2012)          11

                     Opinion of the Court

would have presumed that such a warrant was valid.”
Brief for Respondents 27. We disagree.
                              A
   With respect to the warrant’s authorization to search for
and seize all firearms, the Millenders argue that “a rea-
sonably well-trained officer would have readily perceived
that there was no probable cause to search the house for
all firearms and firearm-related items.” Id., at 32. Noting
that “the affidavit indicated exactly what item was evi-
dence of a crime—the ‘black sawed off shotgun with a
pistol grip,’ ” they argue that “[n]o facts established that
Bowen possessed any other firearms, let alone that such
firearms (if they existed) were ‘contraband or evidence of a
crime.’ ” Ibid. (quoting App. 56).
   Even if the scope of the warrant were overbroad in
authorizing a search for all guns when there was infor-
mation only about a specific one, that specific one was a
sawed-off shotgun with a pistol grip, owned by a known
gang member, who had just fired the weapon five times in
public in an attempt to murder another person, on the
asserted ground that she had “call[ed] the cops” on him.
Id., at 56. Under these circumstances—set forth in the
warrant—it would not have been unreasonable for an
officer to conclude that there was a “fair probability” that
the sawed-off shotgun was not the only firearm Bowen
owned. Illinois v. Gates, 462 U. S. 213, 238 (1983). And
it certainly would have been reasonable for an officer to
assume that Bowen’s sawed-off shotgun was illegal. Cf. 26
U. S. C. §§5845(a), 5861(d). Evidence of one crime is not
always evidence of several, but given Bowen’s possession
of one illegal gun, his gang membership, his willingness
to use the gun to kill someone, and his concern about
the police, a reasonable officer could conclude that there
would be additional illegal guns among others that Bowen
12               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

owned.3
   A reasonable officer also could believe that seizure of the
firearms was necessary to prevent further assaults on
Kelly. California law allows a magistrate to issue a search
warrant for items “in the possession of any person with
the intent to use them as a means of committing a public
offense,” Cal. Penal Code Ann. §1524(a)(3) (West 2011),
and the warrant application submitted by the officers
specifically referenced this provision as a basis for the
search. App. 48. Bowen had already attempted to murder
Kelly once with a firearm, and had yelled “I’ll kill you” as
she tried to escape from him. Id., at 56–57. A reasonable
officer could conclude that Bowen would make another
attempt on Kelly’s life and that he possessed other fire-
arms “with the intent to use them” to that end. Cal. Penal
Code Ann. §1524(a)(3).
   Given the foregoing, it would not have been “entirely
unreasonable” for an officer to believe, in the particular
circumstances of this case, that there was probable cause
to search for all firearms and firearm-related materials.
Leon, supra, at 923 (internal quotation marks omitted).
   With respect to the warrant’s authorization to search for
evidence of gang membership, the Millenders contend that
“no reasonable officer could have believed that the affida-
vit presented to the magistrate contained a sufficient basis
to conclude that the gang paraphernalia sought was con-
traband or evidence of a crime.” Brief for Respondents 28.
They argue that “the magistrate [could not] have reasona-
bly concluded, based on the affidavit, that Bowen’s gang
membership had anything to do with the crime under
investigation” because “[t]he affidavit described a ‘spousal
——————
   3 The dissent caricatures our analysis as being that “because Bowen

fired one firearm, it was reasonable for the police to conclude . . . that
[he] must have possessed others,” post, at 10 (opinion of SOTOMAYOR,
J.). This simply avoids coming to grips with the facts of the crime at
issue.
                     Cite as: 565 U. S. ____ (2012)                   13

                          Opinion of the Court

assault’ that ensued after Kelly decided to end her ‘on
going dating relationship’ with Bowen” and “[n]othing in
that description suggests that the crime was gang-
related.” Ibid. (quoting App. 55).
   This effort to characterize the case solely as a domes-
tic dispute, however, is misleading.        Cf. post, at 5
(SOTOMAYOR, J., dissenting); post, at 2 (KAGAN, J., concur-
ring in part and dissenting in part). Messerschmidt began
his affidavit in support of the warrant by explaining that
he “has been investigating an assault with a deadly weap-
on incident” and elaborated that the crime was a “spousal
assault and an assault with a deadly weapon.” App. 55
(emphasis added). The affidavit also stated that Bowen
was “a known Mona Park Crip gang member” “based on
information provided by the victim and the cal-gang data-
base,”4 and that he had attempted to murder Kelly after
becoming enraged that she had “call[ed] the cops on
[him].” Id., at 56, 58–59. A reasonable officer could cer-
tainly view Bowen’s attack as motivated not by the sour-
ing of his romantic relationship with Kelly but instead by
a desire to prevent her from disclosing details of his gang
activity to the police. She was, after all, no longer linked
with him as a girlfriend; he had assaulted her in the past;
and she had indeed called the cops on him. And, as the
affidavit supporting the warrant made clear, Kelly had in
fact given the police information about Bowen’s gang ties.
Id., at 59.5
——————
  4 Although the cal-gang database states that information contained

therein cannot be used to establish probable cause, see App. 64, the
affidavit makes clear that Kelly also provided this information to
Messerschmidt, id., at 59, as she did to the deputies who initially
responded to the attack, id., at 39 (describing Kelly’s statement that
Bowen was “an active member of the ‘Mona Park Crips’ ”). We there-
fore need not decide whether the cal-gang database’s disclaimer is
relevant to Fourth Amendment analysis.
  5 Contrary to the dissent’s suggestion, see post, at 5–6, n. 5 (opinion

of SOTOMAYOR, J.), the affidavit’s account of Bowen’s statements is
14               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

   It would therefore not have been unreasonable—based
on the facts set out in the affidavit—for an officer to be-
lieve that evidence regarding Bowen’s gang affiliation
would prove helpful in prosecuting him for the attack on
Kelly. See Warden, Md. Penitentiary v. Hayden, 387 U. S.
294, 307 (1967) (holding that the Fourth Amendment
allows a search for evidence when there is “probable cause
. . . to believe that the evidence sought will aid in a partic-
ular apprehension or conviction”). Not only would such
evidence help to establish motive, either apart from or in
addition to any domestic dispute, it would also support the
bringing of additional, related charges against Bowen for
the assault. See, e.g., Cal. Penal Code Ann. §136.1(b)(1)
(West 1999) (It is a crime to “attempt[ ] to prevent or
dissuade another person who has been the victim of a
crime or who is witness to a crime from . . . [m]aking any
report of that victimization to any . . . law enforcement
officer”).6
——————
consistent with other accounts of the confrontation, in particular the
report prepared by the officers who spoke with Kelly immediately after
the attack. See App. 39 (stating that when Bowen “appeared at the
base of the stairs and began yelling at [Kelly,] [h]e was angry because
she had called the Sheriff ’s Department”). And at no point during this
litigation has the accuracy of the affidavit’s account of the attack been
called into question.
   6 The dissent relies heavily on Messerschmidt’s deposition, in which

he stated that Bowen’s crime was not a “gang crime.” See post, at 4–7.
Messerschmidt’s belief about the nature of the crime, however, is not
information he possessed but a conclusion he reached based on infor-
mation known to him. See Anderson v. Creighton, 483 U. S. 635, 641
(1987). We have “eschew[ed] inquiries into the subjective beliefs of law
enforcement officers who seize evidence pursuant to a subsequently
invalidated warrant.” United States v. Leon, 468 U. S. 897, 922, n. 23
(1984); see also Harlow v. Fitzgerald, 457 U. S. 800, 815–819 (1982). In
any event, as the dissent recognizes, the inquiry under our precedents
is whether “a reasonably well-trained officer in petitioner’s position
would have known that his affidavit failed to establish probable cause.”
Malley, 475 U. S., at 345 (emphasis added). Messerschmidt’s own
evaluation does not answer the question whether it would have been
                      Cite as: 565 U. S. ____ (2012)                    15

                          Opinion of the Court

   In addition, a reasonable officer could believe that evi-
dence demonstrating Bowen’s membership in a gang
might prove helpful in impeaching Bowen or rebutting
various defenses he could raise at trial. For example,
evidence that Bowen had ties to a gang that uses guns
such as the one he used to assault Kelly would certainly be
relevant to establish that he had familiarity with or access
to this type of weapon.
   Moreover, even if this were merely a domestic dispute, a
reasonable officer could still conclude that gang parapher-
nalia found at the Millenders’ residence would aid in
the prosecution of Bowen by, for example, demonstrating
Bowen’s connection to other evidence found there. The
warrant authorized a search for “any gang indicia that
would establish the persons being sought in this warrant,”
and “[a]rticles of personal property tending to establish
the identity of [the] person in control of the premise or
premises.” App. 52. Before the District Court, the Millen-
ders “acknowledge[d] that evidence of who controlled the
premises would be relevant if incriminating evidence were
found and it became necessary to tie that evidence to a
person, ” and the District Court approved that aspect of
the warrant on this basis. App. to Pet. for Cert. 158–159
(internal quotation marks omitted). Given Bowen’s known
gang affiliation, a reasonable officer could conclude that
gang paraphernalia found at the residence would be an
effective means of demonstrating Bowen’s control over the
premises or his connection to evidence found there.7
——————
unreasonable for an officer to have reached a different conclusion from
the facts in the affidavit. See n. 2, supra.
  7 The Fourth Amendment does not require probable cause to believe

evidence will conclusively establish a fact before permitting a search,
but only “probable cause . . . to believe the evidence sought will aid in a
particular apprehension or conviction.” Warden, Md. Penitentiary v.
Hayden, 387 U. S. 294, 307 (1967) (emphasis added). Even if gang
evidence might have turned out not to be conclusive because other
16               MESSERSCHMIDT v. MILLENDER

                         Opinion of the Court

   Whatever the use to which evidence of Bowen’s gang
involvement might ultimately have been put, it would not
have been “entirely unreasonable” for an officer to believe
that the facts set out in the affidavit established a fair
probability that such evidence would aid the prosecution
of Bowen for the criminal acts at issue. Leon, 468 U. S., at
923 (internal quotation marks omitted).
                              B
   Whether any of these facts, standing alone or taken
together, actually establish probable cause is a question
we need not decide. Qualified immunity “gives govern-
ment officials breathing room to make reasonable but
mistaken judgments.” al-Kidd, 563 U. S., at ___ (slip op.,
at 12). The officers’ judgment that the scope of the war-
rant was supported by probable cause may have been
mistaken, but it was not “plainly incompetent.” Malley,
475 U. S., at 341.
   On top of all this, the fact that the officers sought and
obtained approval of the warrant application from a supe-
rior and a deputy district attorney before submitting it to
the magistrate provides further support for the conclusion
that an officer could reasonably have believed that the
scope of the warrant was supported by probable cause.
Ibid. Before seeking to have the warrant issued by a
magistrate, Messerschmidt conducted an extensive inves-
tigation into Bowen’s background and the facts of the
crime. Based on this investigation, Messerschmidt pre-
pared a detailed warrant application that truthfully laid
——————
members of the Millender household also had gang ties, see post, at 8
(opinion of SOTOMAYOR, J.); post, at 2–3 (opinion of KAGAN, J.), a rea-
sonable officer could still conclude that evidence of gang membership
would help show Bowen’s connection to the residence. Such evidence
could, for example, have displayed Bowen’s gang moniker (“C Jay”)
or could have been identified by Kelly as belonging to Bowen. See
App. 64.
                 Cite as: 565 U. S. ____ (2012)           17

                     Opinion of the Court

out the pertinent facts. The only facts omitted—the offi-
cers’ knowledge of Bowen’s arrest and conviction records,
see supra, at 3—would only have strengthened the war-
rant. Messerschmidt then submitted the warrant applica-
tion for review by Lawrence, another superior officer, and
a deputy district attorney, all of whom approved the appli-
cation without any apparent misgivings. Only after this
did Messerschmidt seek the approval of a neutral magis-
trate, who issued the requested warrant. The officers thus
“took every step that could reasonably be expected of
them.” Massachusetts v. Sheppard, 468 U. S. 981, 989
(1984). In light of the foregoing, it cannot be said that “no
officer of reasonable competence would have requested the
warrant.” Malley, 475 U. S., at 346, n. 9. Indeed, a con-
trary conclusion would mean not only that Messerschmidt
and Lawrence were “plainly incompetent,” id., at 341, but
that their supervisor, the deputy district attorney, and the
magistrate were as well.
   The Court of Appeals, however, gave no weight to the
fact that the warrant had been reviewed and approved
by the officers’ superiors, a deputy district attorney, and a
neutral magistrate. Relying on Malley, the court held that
the officers had an “independent responsibility to ensure
there [was] at least a colorable argument for probable
cause.” 620 F. 3d, at 1034. It explained that “[t]he depu-
ties here had a responsibility to exercise their reasonable
professional judgment,” and that “in circumstances such
as these a neutral magistrate’s approval (and, a fortiori,
a non-neutral prosecutor’s) cannot absolve an officer of
liability.” Ibid. (citation omitted).
   We rejected in Malley the contention that an officer is
automatically entitled to qualified immunity for seeking a
warrant unsupported by probable cause, simply because
a magistrate had approved the application. 475 U. S., at
345. And because the officers’ superior and the deputy
district attorney are part of the prosecution team, their
18            MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

review also cannot be regarded as dispositive. But by
holding in Malley that a magistrate’s approval does not
automatically render an officer’s conduct reasonable, we
did not suggest that approval by a magistrate or review
by others is irrelevant to the objective reasonableness of
the officers’ determination that the warrant was valid.
Indeed, we expressly noted that we were not deciding
“whether [the officer’s] conduct in [that] case was in fact
objectively reasonable.” Id., at 345, n. 8. The fact that the
officers secured these approvals is certainly pertinent in
assessing whether they could have held a reasonable belief
that the warrant was supported by probable cause.
                             C
    In holding that the warrant in this case was so obvious-
ly defective that no reasonable officer could have believed
it was valid, the court below relied heavily on our decision
in Groh v. Ramirez, 540 U. S. 551 (2004), but that prece-
dent is far afield. There, we held that officers who carried
out a warrant-approved search were not entitled to quali-
fied immunity because the warrant in question failed to
describe the items to be seized at all. Id., at 557. We
explained that “[i]n the portion of the form that called for
a description of the ‘person or property’ to be seized, [the
applicant] typed a description of [the target’s] two-story
blue house rather than the alleged stockpile of firearms.”
Id., at 554. Thus, the warrant stated nonsensically that
“ ‘there is now concealed [on the specified premises] a
certain person or property, namely [a] single dwelling
residence two story in height which is blue in color and
has two additions attached to the east.’ ” Id., at 554–555,
n. 2 (bracketed material in original). Because “even a
cursory reading of the warrant in [that] case—perhaps
just a simple glance—would have revealed a glaring de-
ficiency that any reasonable police officer would have
known was constitutionally fatal,” id., at 564, we held that
                 Cite as: 565 U. S. ____ (2012)          19

                     Opinion of the Court

the officer was not entitled to qualified immunity.
   The instant case is not remotely similar. In contrast to
Groh, any defect here would not have been obvious from
the face of the warrant. Rather, any arguable defect
would have become apparent only upon a close parsing of
the warrant application, and a comparison of the affidavit
to the terms of the warrant to determine whether the
affidavit established probable cause to search for all the
items listed in the warrant. This is not an error that
“just a simple glance” would have revealed. Ibid. Indeed,
unlike in Groh, the officers here did not merely submit
their application to a magistrate. They also presented it
for review by a superior officer, and a deputy district
attorney, before submitting it to the magistrate. The fact
that none of the officials who reviewed the application
expressed concern about its validity demonstrates that
any error was not obvious. Groh plainly does not control
the result here.
                        *    *     *
  The question in this case is not whether the magistrate
erred in believing there was sufficient probable cause to
support the scope of the warrant he issued. It is instead
whether the magistrate so obviously erred that any rea-
sonable officer would have recognized the error. The
occasions on which this standard will be met may be rare,
but so too are the circumstances in which it will be appro-
priate to impose personal liability on a lay officer in the
face of judicial approval of his actions. Even if the war-
rant in this case were invalid, it was not so obviously
lacking in probable cause that the officers can be con-
sidered “plainly incompetent” for concluding otherwise.
Malley, supra, at 341. The judgment of the Court of Ap-
peals denying the officers qualified immunity must there-
fore be reversed.
                                           It is so ordered.
                  Cite as: 565 U. S. ____ (2012)            1

                     BREYER, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 10–704
                          _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                      [February 22, 2012]


   JUSTICE BREYER, concurring.
   The Court concludes that the officers acted reasonably
in searching the house for “ ‘all firearms and firearm-
related items.’ ” Ante, at 11–12 (emphasis deleted). In
support of this conclusion, it cites two sets of circum-
stances. First, the majority points to “Bowen’s possession
of one illegal gun, his gang membership, his willingness to
use the gun to kill someone, and his concern about the
police . . . .” Ante, at 11. Second, the majority notes that
“[a] reasonable officer also could believe that seizure of the
firearms was necessary to prevent further assaults on
Kelly,” because “Bowen had already attempted to murder
Kelly once with a firearm, and had yelled ‘I’ll kill you’ as
she tried to escape from him.” Ante, at 12. In my view,
given all these circumstances together, the officers could
reasonably have believed that the scope of their search
was supported by probable cause. On that basis, I concur.
                 Cite as: 565 U. S. ____ (2012)           1

                     Opinion of KAGAN, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–704
                         _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                     [February 22, 2012]


   JUSTICE KAGAN, concurring in part and dissenting in
part.
   Both the Court and the dissent view this case as an
all-or-nothing affair: The Court awards immunity across
the board to Messerschmidt and his colleagues, while the
dissent would grant them none at all. I think the right
answer lies in between, although the Court makes the
more far-reaching error.
   I agree with the Court that a reasonably competent
police officer could have thought this warrant valid in
authorizing a search for all firearms and related items.
See ante, at 11–12. The warrant application recounted
that a known gang member had used a sawed-off shot-
gun—an illegal weapon under California law, see Cal.
Penal Code Ann. §33215 (West 2012 Cum. Supp.)—to try
to kill another person. See App. 56–57, 59. Perhaps gang
ties plus possession of an unlawful gun plus use of that
gun to commit a violent assault do not add up to what was
needed for this search: probable cause to believe that
Bowen had additional illegal firearms (or legal firearms
that he intended to use to violate the law) at the place he
was staying. But because our and the Ninth Circuit’s
decisions leave that conclusion debatable, a reasonable
2             MESSERSCHMIDT v. MILLENDER

                     Opinion of KAGAN, J.

police officer could have found the warrant adequately
supported by “indicia of probable cause.” Malley v. Briggs,
475 U. S. 335, 345 (1986). So Messerschmidt and his
fellow officers should receive qualified immunity for their
search for firearms.
   The Court, however, goes astray when it holds that a
reasonable officer could have thought the warrant valid in
approving a search for evidence of “street gang member-
ship,” App. 52. Membership in even the worst gang does
not violate California law, so the officers could not search
for gang paraphernalia just to establish Bowen’s ties to
the Crips. Instead, the police needed probable cause to
believe that such items would provide evidence of an
actual crime—and as the Court acknowledges, see ante, at
12–14, the only crime mentioned in the warrant applica-
tion was the assault on Kelly. The problem for the Court
is that nothing in the application supports a link between
Bowen’s gang membership and that shooting. Contra the
Court’s elaborate theory-spinning, see ante, at 12–16,
Messerschmidt’s affidavit in fact characterized the violent
assault only as a domestic dispute, not as a gang-related
one, see App. 55 (describing the crime as a “spousal as-
sault and an assault with a deadly weapon”). And that
description is consistent with the most natural under-
standing of the events. The warrant application thus had
a hole at its very center: It lacked any explanation of how
gang items would (or even might) provide evidence of the
domestic assault the police were investigating.
   To fill this vacuum, the Court proposes an alternative,
but similarly inadequate justification—that gang para-
phernalia could have demonstrated Bowen’s connection to
the Millender residence and to any evidence of the assault
found there. The dissent rightly notes one difficulty with
this argument: The discovery of gang items would not
have established that Bowen was staying at the house,
given that several other gang members regularly did so.
                  Cite as: 565 U. S. ____ (2012)             3

                      Opinion of KAGAN, J.

See post, at 8–9 (opinion of SOTOMAYOR, J.). And even
setting that issue aside, the Court’s reasoning proves far
too much: It would sanction equally well a search for any
of Bowen’s possessions on the premises—a result impos-
sible to square with the Fourth Amendment. See, e.g.,
Andresen v. Maryland, 427 U. S. 463, 480 (1976) (disap-
proving “ ‘a general, exploratory rummaging in a person’s
belongings’ ” (quoting Coolidge v. New Hampshire, 403
U. S. 443, 467 (1971))). In authorizing a search for all
gang-related items, the warrant far outstripped the offic-
ers’ probable cause. Because a reasonable officer would
have recognized that defect, I would not award qualified
immunity to Messerschmidt and his colleagues for this
aspect of their search.
  Still more fundamentally, the Court errs in scolding the
Court of Appeals for failing to give “weight to the fact that
the warrant had been reviewed and approved by the offic-
ers’ superiors, a deputy district attorney, and a neutral
magistrate.” Ante, at 17. As the dissent points out,
see post, at 13–15, this Court’s holding in Malley is to
the opposite effect: An officer is not “entitled to rely on the
judgment of a judicial officer in finding that probable
cause exists and hence issuing the warrant.” 475 U. S., at
345. Malley made clear that qualified immunity turned
on the officer’s own “professional judgment,” considered
separately from the mistake of the magistrate. Id., at 346;
see ibid., n. 9 (“The officer . . . cannot excuse his own
default by pointing to the greater incompetence of the
magistrate”); id., at 350 (Powell, J., concurring in part and
dissenting in part) (objecting to the Court’s decision to
“give little evidentiary weight to the finding of probable
cause by a magistrate”). And what we said in Malley
about a magistrate’s authorization applies still more
strongly to the approval of other police officers or state
attorneys. All those individuals, as the Court puts it, are
“part of the prosecution team.” Ante, at 18. To make their
4             MESSERSCHMIDT v. MILLENDER

                    Opinion of KAGAN, J.

views relevant is to enable those teammates (whether
acting in good or bad faith) to confer immunity on each
other for unreasonable conduct—like applying for a war-
rant without anything resembling probable cause.
  For these reasons, I would reverse in part and affirm in
part the judgment of the Court of Appeals, and I would
remand this case for further proceedings.
                  Cite as: 565 U. S. ____ (2012)             1

                    SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 10–704
                          _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                      [February 22, 2012]


   JUSTICE SOTOMAYOR, with whom JUSTICE GINSBURG
joins, dissenting.
   The fundamental purpose of the Fourth Amendment’s
warrant clause is “to protect against all general searches.”
Go-Bart Importing Co. v. United States, 282 U. S. 344, 357
(1931). The Fourth Amendment was adopted specifically
in response to the Crown’s practice of using general war-
rants and writs of assistance to search “suspected places”
for evidence of smuggling, libel, or other crimes. Boyd v.
United States, 116 U. S. 616, 625–626 (1886). Early patri-
ots railed against these practices as “the worst instrument
of arbitrary power” and John Adams later claimed that
“the child Independence was born” from colonists’ opposi-
tion to their use. Id., at 625 (internal quotation marks
omitted).
   To prevent the issue of general warrants on “loose,
vague or doubtful bases of fact,” Go-Bart Importing Co.,
282 U. S., at 357, the Framers established the inviolable
principle that should resolve this case: “no Warrants shall
issue, but upon probable cause . . . and particularly de-
scribing the . . . things to be seized.” U. S. Const., Amdt. 4.
That is, the police must articulate an adequate reason to
search for specific items related to specific crimes.
2              MESSERSCHMIDT v. MILLENDER

                    SOTOMAYOR, J., dissenting

    In this case, police officers investigating a specific, non-
gang-related assault committed with a specific firearm (a
sawed-off shotgun) obtained a warrant to search for all
evidence related to “any Street Gang,” “[a]ny photographs
. . . which may depict evidence of criminal activity,” and
“any firearms.” App. 52. They did so for the asserted
reason that the search might lead to evidence related to
other gang members and other criminal activity, and that
other “[v]alid warrants commonly allow police to search
for ‘firearms and ammunition.’ ” See infra, at 8–9. That
kind of general warrant is antithetical to the Fourth
Amendment.
    The Court nonetheless concludes that the officers are
entitled to qualified immunity because their conduct was
“objectively reasonable.” I could not disagree more. All
13 federal judges who previously considered this case
had little difficulty concluding that the police officers’
search for any gang-related material violated the Fourth
Amendment. See App. to Pet. for Cert. 28–29, 45, n. 7,
73, 94, 157–158. And a substantial majority agreed that
the police’s search for both gang-related material and all
firearms not only violated the Fourth Amendment, but
was objectively unreasonable. Like them, I believe that
any “reasonably well-trained officer in petitioner’s position
would have known that his affidavit failed to establish
probable cause.” Malley v. Briggs, 475 U. S. 335, 345
(1986).
    The Court also hints that a police officer’s otherwise
unreasonable conduct may be excused by the approval of
a magistrate, or more disturbingly, another police officer.
Ante, at 16–18. That is inconsistent with our focus on the
objective reasonableness of an officer’s decision to submit
a warrant application to a magistrate, and we long ago
rejected it. See Malley, 475 U. S., at 345–346.
    The Court’s analysis bears little relationship to the
record in this case, our precedents, or the purposes under-
                     Cite as: 565 U. S. ____ (2012)                    3

                       SOTOMAYOR, J., dissenting

lying qualified immunity analysis. For all these reasons,
I respectfully dissent.
                             I
   The Court holds that a well-trained officer could have
reasonably concluded that there was probable cause to
search the Millenders’ residence for any evidence of affilia-
tion with “any Street Gang,” and “all handguns, rifles, or
shotguns of any caliber, or any firearms capable of firing
ammunition.” App. 52.1 I cannot agree.
                              A
   Most troubling is the Court’s determination that peti-
tioners reasonably could have concluded that they had
probable cause to search for all evidence of any gang affili-
ation in the Millenders’ home. The Court reaches this
result only by way of an unprecedented, post hoc recon-
struction of the crime that wholly ignores the police’s own
conclusions, as well as the undisputed facts presented to
the District Court.
   The Court primarily theorizes that “[a] reasonable of-
ficer could certainly view Bowen’s attack as motivated
not by the souring of his romantic relationship with Kelly
but instead by a desire to prevent her from disclosing
details of his gang activity to the police.” Ante, at 13. The
majority therefore dismisses as “misleading” the Millen-
ders’ characterization of the case as a “domestic dispute,”
insisting that Detective Messerschmidt could have rea-
sonably thought that the crime was gang related. See
ante, at 13–14.2
——————
  1 Not even the Court defends the warrant’s authorization to search for

“[a]ny photographs . . . which may depict evidence of criminal activity.”
  2 The Court implies Detective Messerschmidt did not consider the

crime “solely . . . a domestic dispute” because he labeled it a “spousal
assault and an assault with a deadly weapon.” Ante, at 13 (internal
quotation marks omitted). Solely domestic disputes often involve gun
violence, however. See Sorenson & Weibe, Weapons in the Lives of
4                MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

  The police flatly rejected that hypothesis, however, con-
cluding that the crime was a domestic dispute that was
not in any way gang related. Detective Messerschmidt’s
deposition is illustrative.
     “Q: So as far as you knew, it was just sort of a spousal-
     abuse-type case where the perpetrator happened to be
     in a gang, right?
     “A: Correct.
     “Q: So you didn’t have any reason to believe that the
     assault on Kelly was any sort of gang crime, did you?
     “A: No.” Record in No. CV 05–2298 DDP (RZx) (CD
     Cal.) (hereinafter Record), Doc. 51, (Exh. X), p. 120
     (hereinafter Deposition).3
The “Crime Analysis” forms prepared by the police like-
——————
Battered Women, 94 Am. J. Pub. Health 1412, 1413 (2004) (noting
more than one-third of female domestic violence shelter residents in
California reported having been threatened or harmed with a firearm).
That was the case here. In any event, the Court’s reading of Detective
Messerschmidt’s affidavit is incompatible with his testimony that the
crime was “just sort of a spousal-abuse-type case,” not a “gang crime.”
See supra this page.
  3 By suggesting that courts assessing qualified immunity should ig-

nore police officers’ testimony about the information they possessed at
the time of the search, ante, at 14–15, n. 6, the Court misreads Harlow
v. Fitzgerald, 457 U. S. 800, 815–819 (1982), and Anderson v.
Creighton, 483 U. S. 635, 645 (1987). In Harlow, we adopted a qualified
immunity test focusing on an officer’s objective good faith, rather than
whether the officer searched “with the malicious intention to cause a
deprivation of constitutional rights or other injury.” 457 U. S., at 815.
As we have explained, “examination of the information possessed by the
searching officials . . . does not reintroduce into qualified immunity
analysis the inquiry into officials’ subjective intent that Harlow sought
to minimize.” Anderson, 483 U. S., at 641. It is therefore highly
relevant that Detective Messerschmidt testified that he lacked “any
reason” to consider the crime gang related, supra this page, and pos-
sessed no “information” that there were handguns in the Millenders’
home, infra, at 11. Courts cannot ignore information in crime analysis
forms, ballistic reports, or victim interviews by labeling such infor-
mation “conclusions.”
                      Cite as: 565 U. S. ____ (2012)                     5

                       SOTOMAYOR, J., dissenting

wise identified Bowen as a “Mona Park Crip” gang mem-
ber, but did not check off “gang-related” as a motive for the
attack. See App. 41, 44 (Crime Analysis Supplemental
Form–M. O. Factors). And the District Court noted it was
undisputed that Detective Messerschmidt “had no reason
to believe Bowen’s crime was a ‘gang’ crime.” App. to Pet.
for Cert. 115.4
   The police’s conclusions matched the victim’s own ac-
count of the attack. Kelly asked police officers to help her
move out because Bowen “ha[d] a domestic violence on his
record,” had “hit [her] once or twice” already, had repeat-
edly threatened her “You’ll never leave me. I’ll kill you
if you leave me,” and she was “planning on breaking up”
with him. Record, Doc. 51 (Exh. C), pp. 5–6 (hereinafter
Kelly Interview). As Kelly described the confrontation, it
was only after she fled to her car in order to leave that
Bowen reemerged from their shared apartment with the
shotgun and told her “I’m gonna kill your ass right here if
you take off,” consistent with his prior threats. Id., at 7–8.
Every piece of information, therefore, accorded with Detec-
tive Messerschmidt’s conclusion: The crime was domestic
violence that was not gang related.5
——————
   4 The Court is wrong to imply that courts should not consider “facts

outside the affidavit,” but within the officers’ possession, when as-
sessing qualified immunity. Ante, at 10, n. 2. Our precedents make
clear that the objective reasonableness of an officer’s conduct is judged
“in light of clearly established law and the information the officers
possessed.” Wilson v. Layne, 526 U. S. 603, 615 (1999). If an officer
possesses information indicating that he lacks probable cause to search,
and that information was not presented to the neutral magistrate when
he approved the search, it is particularly likely that “a reasonably well
trained officer would have known that the search was illegal despite
the magistrate’s authorization.” United States v. Leon, 468 U. S. 897,
922, n. 23 (1984).
   5 To support its theory that Bowen attacked Kelly to keep her silent

about his gang activity, the majority relies principally on its claim that
Bowen yelled, “ ‘I told you never to call the cops on me bitch!’ ” ante, at
2, citing it no less than five times. See, ante, at 11 (Bowen “attempt[ed]
6                MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

   Unlike the Members of this Court, Detective Messer-
schmidt alone had 14 years of experience as a peace of-
ficer, “hundreds of hours of instruction on the dynamics of
gangs and gang trends,” received “specialized training in
the field of gang related crimes,” and had been “involved
in hundreds of gang related incidents, contacts, and or
arrests.” App. 53–54. The Court provides no justification
for sweeping aside the conclusions he reached on the basis
of his far greater expertise, let alone the facts found by the
District Court. We have repeatedly and recently warned
appellate courts, “far removed from the scene,” against
second-guessing the judgments made by the police or
reweighing the facts as they stood before the district court.
Ryburn v. Huff, 565 U. S. —, — (2012) (per curiam) (slip
op., at 6–8). The majority’s decision today is totally incon-
sistent with those principles.
   Qualified immunity analysis does not direct courts to
play the role of crime scene investigators, second-guessing
police officers’ determinations as to whether a crime was
committed with a handgun or a shotgun, or whether vio-
——————
to murder” Kelly “on the asserted ground that she had ‘call[ed] the cops’
on him”); see also ante, at 1, 13. Bowen, however, never made that
statement. Though it appears in the warrant application, the words
are Messerschmidt’s—taken from his own inaccurate notes of Kelly’s
account of the crime. What Kelly actually said during her interview
was that as soon as the police deputies left, Bowen “came out of no-
where talking about, ‘Did you call the police on me? You called the
police on me,’ ” to which Kelly responded “no one called the police on
you . . . . [I]nstead of arguing and fighting with you I just want to get
my shit done.” Kelly Interview 7; compare ibid. with Record, Doc. 51
(Exh. B), p. 3 (Messerschmidt’s narrative of interview with Kelly). Only
after Kelly started to leave did Bowen exclaim “oh it’s like that. It’s
like that,” retrieve a gun, and threaten to shoot her if she left. Kelly
Interview 7–8. That Bowen was “ ‘angry,’ ” ante, at 14, n. 5, because she
had called the sheriff's department for assistance reflected exactly what
Kelly and the police expected at the outset—that Bowen “would give
her a hard time about moving out.” App. 38 (sheriff’s department
incident report).
                 Cite as: 565 U. S. ____ (2012)           7

                   SOTOMAYOR, J., dissenting

lence was gang related or a domestic dispute. Indeed,
we have warned courts against asking “whether another
reasonable, or more reasonable, interpretation of the
events can be constructed five years after the fact.”
Hunter v. Bryant, 502 U. S. 224, 228 (1991) (per curiam).
The inquiry our precedents demand is not whether differ-
ent conclusions might conceivably be drawn from the
crime scene. Rather, it is whether “a reasonably well-
trained officer in petitioner’s position would have known
that his affidavit failed to establish probable cause.”
Malley, 475 U. S., at 345. The operative question in this
case, therefore, is whether—given that, as petitioners
comprehended, the crime itself was not gang related—a
reasonable officer nonetheless could have believed he had
probable cause to seek a warrant to search the suspect’s
residence for all evidence of affiliation not only with the
suspect’s street gang, but “any Street Gang.” He could
not.
  The Court offers two secondary explanations for why a
search for gang-related items might have been justified,
but they are equally unpersuasive. First, the majority
suggests that such evidence hypothetically “might prove
helpful in impeaching Bowen or rebutting various de-
fenses he could raise at trial.” Ante, at 15. That is a non-
starter. The Fourth Amendment does not permit the police
to search for evidence solely because it could be admissible
for impeachment or rebuttal purposes. If it did, the police
would be equally entitled to obtain warrants to rifle
through the papers of anyone reasonably suspected of a
crime for all evidence of his bad character, Fed. Rule Evid.
404(a)(2)(B)(i), or any evidence of any “crime, wrong, or
other act” that might prove the defendant’s “motive, op-
portunity, intent, preparation, plan, knowledge, identity,
absence of mistake, or lack of accident,” Fed. Rule Evid.
404(b)(2). Indeed, the majority’s rationale presumably
would authorize the police to search the residence of every
8               MESSERSCHMIDT v. MILLENDER

                      SOTOMAYOR, J., dissenting

member of Bowen’s street gang for similar weapons—
which likewise “might [have] prove[d] helpful in impeach-
ing Bowen or rebutting various defenses he could raise at
trial.” Ante, at 15. It has long been the case, however,
that such general searches, detached from probable cause,
are impermissible. See, e.g., Go-Bart Importing Co., 282
U. S., at 357. By their own admission, however, the offic-
ers were not searching for gang-related indicia to bolster
some hypothetical impeachment theory, but for other
reasons: because “photos sought re gang membership
could be linked with other gang members, evidencing
criminal activity as gang affiliation is an enhancement to
criminal charges.” App. 181; see also id., at 145. That
kind of fishing expedition for evidence of unidentified
criminal activity committed by unspecified persons was
the very evil the Fourth Amendment was intended to
prevent.
   Finally, the Court concludes that “even if this were
merely a domestic dispute, a reasonable officer could still
conclude that gang paraphernalia found at the Millenders’
residence would aid in the prosecution of Bowen by, for
example, demonstrating Bowen’s connection to other
[unspecified] evidence found there.” Ante, at 15. That is
difficult to understand. The police were well aware before
obtaining a warrant that “other persons associated with
the home, the Millender family members, were active
Mona Park Crip gang members.” App. 28. Simply finding
gang-related paraphernalia, therefore, would have done
little to establish probable cause that particular evidence
found in the home was connected to Bowen, rather than
any of the several other active gang members who resided
full time at the Millender home.6 Moreover, it would have
——————
  6 The Court suggests that even if gang-related evidence would be

inconclusive generally, evidence bearing Bowen’s particular gang mon-
iker could have demonstrated Bowen’s connection to the residence.
                     Cite as: 565 U. S. ____ (2012)                     9

                       SOTOMAYOR, J., dissenting

done nothing to establish that Bowen had committed the
non-gang-related crime specified in the warrant.7
                              B
   The Court also errs by concluding that petitioners could
have reasonably concluded that they had probable cause
to search for all firearms. Notably absent from the Court’s
discussion is any acknowledgment of the actual basis for
petitioners’ search. The police officers searched for all
firearms not for the reasons hypothesized by the majority,
but because they determined that “[v]alid warrants com-
monly allow police to search for ‘firearms and ammuni-
tion,’ ” and that “[h]ere, any caliber of shotgun or receipts
would show possession of and/or purchase of guns.” Id., at
144, 180–181; see also Brief for Appellant in No. 07–55518
(CA9), p. 41 (hereinafter CA9 Brief). It is small wonder
that the District Court found these arguments “nonsensi-
cal and unpersuasive.” App. to Pet. for Cert. 157. It bears
repeating that the Founders adopted the Fourth Amend-
ment to protect against searches for evidence of unspeci-
fied crimes. And merely possessing other firearms is not a
crime at all. See generally District of Columbia v. Heller,
554 U. S. 570 (2008).8
——————
But the warrant did not authorize a search for items bearing Bowen’s
moniker, but rather for items related to “any Street Gang,” including
countless street gangs of which Bowen was not a member. App. 52.
Even under the Court’s interpretation, therefore, the warrant was
hopelessly overbroad and invalid.
  7 The police also could not search for gang-related evidence for its own

sake. Mere membership in a gang is not a crime under California law.
See People v. Gardeley, 14 Cal. 4th 605, 623, 927 P. 2d 713, 725 (1996).
  8 Although the Court recites additional facts about Bowen’s back-

ground and arrest record, ante, at 2–3, none of these facts were dis-
closed to the magistrate. The police cannot rationalize a search post
hoc on the basis of information they failed to set forth in their warrant
application to a neutral magistrate. Rather, “[i]t is elementary that in
passing on the validity of a warrant, the reviewing court may consider
only information brought to the magistrate’s attention.” Aguilar v.
10               MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

   By justifying the officers’ actions on reasons of its own
invention, the Court ignores the reasons the officers actu-
ally gave, as well as the facts upon which this case was
decided below. The majority’s analysis—akin to a rational-
basis test—is thus far removed from what qualified
immunity analysis demands. Even if the police had
searched for the reasons the Court proposes, however, I
still would find it inappropriate to afford them qualified
immunity.
   The Court correctly recognizes that to satisfy the Fourth
Amendment the police were required to demonstrate
probable cause that (1) other firearms could be found at
the Millenders’ residence; and (2) such weapons were
illegal or were “ ‘possess[ed] . . . with the intent to use
them as a means of committing a public offense.’ ” Ante, at
12 (quoting Cal. Penal Code Ann. §1524(a)(3) (West
2011)). The warrant failed to establish either.
   The majority has little difficulty concluding that because
Bowen fired one firearm, it was reasonable for the police
to conclude not only that Bowen must have possessed
others, but that he must be storing these other weapons
at his 73-year-old former foster mother’s home.9 Again,
however, this is not what the police actually concluded, as
Detective Messerschmidt’s deposition makes clear.
     “Q: Did you have any reason to believe there would be

——————
Texas, 378 U. S. 108, 109, n. 1 (1964); see also United States v. Jacob-
sen, 466 U. S. 109, 112 (1984). Likewise, a police officer cannot obtain
qualified immunity for searching pursuant to a warrant by relying
upon facts outside that warrant, as evinced by Malley’s focus on
“whether a reasonably well-trained officer in petitioner’s position would
have known that his affidavit failed to establish probable cause.”
Malley v. Briggs, 475 U. S. 335, 345 (1986) (emphasis added).
  9 The majority ignores that Bowen retrieved the shotgun that he fired

from the apartment he shared with Kelly, not the Millenders’ home.
Kelly provided no indication that Bowen possessed other guns or that
he stored them at his former foster mother’s home.
                    Cite as: 565 U. S. ____ (2012)                  11

                      SOTOMAYOR, J., dissenting

     any automatic weapons in the house? 

     “A: No.

     “Q: Did you have any reason to believe there would be 

     any hand guns in the house? 

     “A: I wasn’t given information that there were.” Dep-
     osition 120.

   Undaunted, the majority finds that a well-trained officer
could have concluded on this information that he had
probable cause to search for “[a]ll hand guns, . . . [a]ll
caliber of ammunition, miscellaneous gun parts, gun
cleaning kits, holsters which could hold or have held any
caliber handgun being sought,” and “[a]ny receipts or
paperwork, showing the purchase, ownership, or posses-
sion of the handguns being sought.” App. 52. That is
puzzling. If any aspect of the Fourth Amendment is clear-
ly established, it is that the police cannot reasonably
search—even pursuant to a warrant—for items that they
do not have “any reason to believe” will be present. The
Court’s conclusion to the contrary simply reads the “prob-
able cause” requirement out of the Fourth Amendment.
   Even assuming that the police reasonably could have
concluded that Bowen possessed other guns and was
storing them at the Millenders’ home, I cannot agree that
the warrant provided probable cause to believe any weap-
on possessed in a home in which 10 persons regularly
lived—none of them the suspect in this case—was either
“contraband or evidence of a crime.” Ornelas v. United
States, 517 U. S. 690, 696 (1996). The warrant set forth no
specific facts or particularized explanation establishing
probable cause to believe that other guns found in the
home were connected to the crime specified in the warrant
or were otherwise illegal.10 While the Court hypothesizes
——————
  10 Augusta Millender was a 73-year-old grandmother living in a dan-

gerous part of Los Angeles. It would not have been unreasonable to
imagine that she validly possessed a weapon for self-defense, as turned
12                MESSERSCHMIDT v. MILLENDER

                      SOTOMAYOR, J., dissenting

that the police could have searched for all firearms to
uncover evidence of yet unnamed crimes, ante, at 11–12,
the warrant specified that the police were investigating
one particular crime—“an assault with a deadly weapon.”
App. 55. And the police officers confirmed that their
search was targeted to find the gun related to “the crime
at issue.” CA9 Brief 42; see also App. 52 (obtaining au-
thorization to search for “the item being sought and or
believed to be evidence in the case being investigated on
this warrant” (emphasis added)).
   The police told the Ninth Circuit that they searched for
all firearms not because, as the majority hypothesizes,
“there would be additional illegal guns among others that
Bowen owned,” ante, at 11–12, but on the dubious theory
that “Kelly could have been mistaken in her description of
the gun.” App. to Pet. for Cert. 20–21. The Ninth Circuit
properly dismissed that argument as carrying “little
force.” Id., at 21. Its finding is unimpeachable, given that
Kelly presented the police with a photograph of Bowen
holding the specific gun used in the crime, and the police,
the victim, and a witness to the crime all identified the
gun as a sawed-off shotgun. See id., at 20, 21, 24, 28.
   Finally, the majority suggests that the officers could
have reasonably believed that seizure of all firearms at the
Millenders’ residence was justified because those weapons
might be possessed by Bowen “ ‘with the intent to use
them as a means of committing a public offense.’ ” Ante, at
12. But the warrant specified that the police sought only
the shotgun used in this crime for that purpose. See App.
59 (statement of probable cause) (“Your Affiant also be-
lieves that the items sought will be in the possession of
Jerry Ray Bowen and the recovery of the weapon could be
invaluable in the successful prosecution of the suspect
involved in this case, and the curtailment of further
——————
out to be the case.
                     Cite as: 565 U. S. ____ (2012)                    13

                       SOTOMAYOR, J., dissenting

crimes being committed” (emphasis added)).
                               II
  The Court also finds error in the Court of Appeals’
failure to find “pertinent” the fact that the officer sought
approval of his warrant from a magistrate.11 Ante, at 18.
Whether Detective Messerschmidt presented his warrant
application to a magistrate surely would be “pertinent” to
demonstrating his subjective good faith.12 But qualified
immunity does not turn on whether an officer is motivated
by good intentions or malice, but rather on the “objective
reasonableness of an official’s conduct.” Harlow v. Fitz-
gerald, 457 U. S. 800, 818 (1982).
  The majority asserts, without citation, that the magis-
trate’s approval is relevant to objective reasonableness.
That view, however, is expressly contradicted by our hold-
ing in Malley v. Briggs, 475 U. S. 335. There, we found
that a police officer is not “entitled to rely on the judgment
of a judicial officer in finding that probable cause exists
and hence issuing the warrant,” and explained that “[that]
view of objective reasonableness is at odds with our devel-
opment of that concept in Harlow and [United States v.
Leon, 468 U. S. 897 (1984)].” Id., at 345. The appropriate
qualified immunity analysis, we held, was not whether an

——————
   11 Under California law, magistrates are the officials responsible for

issuing search warrants. Cal. Penal Code Ann. §1523 (West 2011).
   12 To be clear, no one suggests petitioners acted with malice or in-

tended to be “misleading in omitting . . . facts,” ante, at 10, n. 2, that
illustrate why it would have been objectively unreasonable to search for
the reasons the Court proposes. It is hardly surprising, for instance,
that Detective Messerschmidt did not include in his affidavit further
facts affirming that the crime was not gang related, given that he did
not believe the crime was gang related and did not search for gang-
related material for that reason. See supra, at 7–8. The affidavit and
warrant were perfectly consistent with the officers’ stated reasons for
their search—just not with the Court’s own theories.
14               MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

officer reasonably relied on a magistrate’s probable cause
determination, but rather “whether a reasonably well-
trained officer in petitioner’s position would have known
that his affidavit failed to establish probable cause and
that he should not have applied for the warrant.” Ibid.
(emphasis added).13 In such a case, “the officer’s applica-
tion for a warrant [would] not [be] objectively reasonable,
because it create[s] the unnecessary danger of an unlawful
arrest.” Ibid. When “no officer of reasonable competence
would have requested the warrant,” a “magistrate [who]
issues the warrant [makes] not just a reasonable mistake,
but an unacceptable error indicating gross incompetence
or neglect of duty.” Id., at 346, n. 9. In such cases, “[t]he
officer . . . cannot excuse his own default by pointing to the
greater incompetence of the magistrate.” Ibid.
   In cases in which it would be not only wrong but un-
reasonable for any well-trained officer to seek a warrant,
allowing a magistrate’s approval to immunize the police
officer’s unreasonable action retrospectively makes little
sense. By motivating an officer “to reflect, before submit-
ting a request for a warrant, upon whether he has a rea-
sonable basis for believing that his affidavit establishes
probable cause,” we recognized that our qualified immu-
nity precedents had the “desirable” effect of “reduc[ing] the
likelihood that the officer’s request for a warrant will be
premature,” leading to “a waste of judicial resources” or
“premature arrests.” Id., at 343. To the extent it proposes
to cut back upon Malley, the majority will promote the
opposite result—encouraging sloppy police work and ex-
acerbating the risk that searches will not comport with
the requirements of the Fourth Amendment.

——————
  13 Two  Justices wrote separately, disagreeing with the majority be-
cause they believed that “substantial weight should be accorded the
judge’s finding of probable cause.” Malley, 475 U. S., at 346 (Powell, J.,
joined by Rehnquist, C. J., concurring in part and dissenting in part).
                     Cite as: 565 U. S. ____ (2012)                    15

                       SOTOMAYOR, J., dissenting

   The Court also makes much of the fact that Detective
Messerschmidt sent his proposed warrant application to
two superior police officers and a district attorney for
review. Giving weight to that fact would turn the Fourth
Amendment on its head. This Court made clear in Malley
that a police officer acting unreasonably cannot obtain
qualified immunity on the basis of a neutral magistrate’s
approval. It would be passing strange, therefore, to im-
munize an officer’s conduct instead based upon the ap-
proval of other police officers and prosecutors.14 See John-
son v. United States, 333 U. S. 10, 14 (1948) (opinion of
Jackson, J.) (“When the right of privacy must reasonably
yield to the right of search is, as a rule, to be decided by a
judicial officer, not by a policeman or government en-
forcement agent”). The effect of the Court’s rule, however,
is to hold blameless the “plainly incompetent” action of the
police officer seeking a warrant because of the “plainly
incompetent” approval of his superiors and the district
attorney. See ante, at 16–18; see also ante, at 3–4 (opinion
of KAGAN, J.). Under the majority’s test, four wrongs
apparently make a right. I cannot agree, however, that
the “objective legal reasonableness of an official’s acts,”
Harlow, 457 U. S., at 819, turns on the number of police
officers or prosecutors who improperly sanction a search
that violates the Fourth Amendment.
                             III
  Police officers perform a difficult and essential service to
society, frequently at substantial risk to their personal
——————
  14 In the famous case of Wilkes v. Wood, Lofft 1, 98 Eng. Rep. 489

(C. P. 1763), one of the seminal events informing the Framers’ development
of the Fourth Amendment, the Undersecretary of State who searched
the home of John Wilkes pursuant to a general warrant was subjected
to monetary damages notwithstanding that his superior, Lord Halifax,
issued the warrant. See Boyd v. United States, 116 U. S. 616, 626
(1886).
16             MESSERSCHMIDT v. MILLENDER

                   SOTOMAYOR, J., dissenting

safety. And criminals like Bowen are not sympathetic
figures. But the Fourth Amendment “protects all, those
suspected or known to be offenders as well as the inno-
cent.” Go-Bart Importing Co., 282 U. S., at 357. And this
Court long ago recognized that efforts “to bring the guilty
to punishment, praiseworthy as they are, are not to be
aided by the sacrifice of those great principles established
by years of endeavor and suffering which have resulted
in their embodiment in the fundamental law of the land.”
Weeks v. United States, 232 U. S. 383, 393 (1914).
   Qualified immunity properly affords police officers protec-
tion so long as their conduct is objectively reasonable.
But it is not objectively reasonable for police investi-
gating a specific, non-gang-related assault committed with
a particular firearm to search for all evidence related to
“any Street Gang,” “photographs . . . which may depict
evidence of criminal activity,” and all firearms. The Court
reaches a contrary result not because it thinks that these
police officers’ stated reasons for searching were objective-
ly reasonable, but because it thinks different conclusions
might be drawn from the crime scene that reasonably
might have led different officers to search for different
reasons. That analysis, however, is far removed from
qualified immunity’s proper focus on whether petitioners
acted in an objectively reasonable manner.
   Because petitioners did not, I would affirm the judgment
of the Court of Appeals.

```

---
