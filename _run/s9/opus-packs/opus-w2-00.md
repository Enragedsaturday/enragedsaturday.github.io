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

## GROUP: _overhaul2/lake/cases/Board of County Commissioners of Bryan County v. Brown.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Board of County Commissioners of Bryan County v. Brown
type: case
citation: "520 U.S. 397 (1997)"
parallel_cite: "117 S. Ct. 1382; 137 L. Ed. 2d 626; 65 U.S.L.W. 4286; 10 Fla. L. Weekly Fed. S 405; 12 I.E.R. Cas. (BNA) 1217; 97 Daily Journal DAR 5311"
neutral_cite: "1997 U.S. LEXIS 2793; 97 Cal. Daily Op. Serv. 3033"
court: U.S.
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-28
docket: 95-1100
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
  opinion_url: "https://www.courtlistener.com/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/"
  cluster_id: 118104
  opinion_id: null
  identity_checked: true
lake:
  record_id: Board of County Commissioners of Bryan County v. Brown
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Monell v. Department of Social Services]]"
tags:
  - case
  - section-1983
  - municipal-liability
  - monell
  - deliberate-indifference
  - failure-to-screen
holding: "A single municipal hiring decision can support § 1983 liability only on a stringent showing of deliberate indifference: the plaintiff must prove that adequate scrutiny of the applicant's background would have made the plainly obvious consequence of hiring him the specific constitutional injury the plaintiff suffered."
aliases:
  - Board of County Commissioners of Bryan County v. Brown
  - Bryan County v. Brown
  - "Board of County Commissioners of Bryan County v. Brown (1997)"
---

# Board of County Commissioners of Bryan County v. Brown

*520 U.S. 397 (1997)* (No. 95-1100) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 118104 → combined opinion 118104 (O'Connor, J.; 520 U.S. 397, decided Apr. 28, 1997). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*411`). S9 promotes. -->

## Background
Sheriff B.J. Moore of Bryan County, Oklahoma, hired his great-nephew, Stacy Burns, as a reserve deputy without reviewing the specifics of Burns's record, which included guilty pleas to assault and battery, resisting arrest, and various driving offenses. During a high-speed stop, Burns used an "arm bar" technique to pull Jill Brown from a truck, severely injuring her knees. Brown sued the County under 42 U.S.C. § 1983, contending that Sheriff Moore's decision to hire Burns without adequate screening was itself the municipal "policy" that caused her injury — a single-decision theory of *[[Monell v. Department of Social Services|Monell]]* liability. A jury found the County liable, and the Fifth Circuit affirmed.

## Issue
Whether a county may be held liable under § 1983 for a single hiring decision, on the theory that an official's inadequate scrutiny of the applicant's background caused a third party's constitutional injury.

## Rule
Municipal liability may not rest on *[[Common Legal Terms#respondeat-superior|respondeat superior]]*; a single facially lawful hiring decision can be the "moving force" behind an injury only under a rigorous culpability-and-causation standard. Stating that standard, the Court held: "A plaintiff must demonstrate that a municipal decision reflects deliberate indifference to the risk that a violation of a particular constitutional or statutory right will follow the decision." — 520 U.S. at 411. ^pin-411

## Application
Even assuming Sheriff Moore's screening of Burns was inadequate, that showed at most a generalized risk that an unfit officer might someday violate someone's rights — not [[Section 1983 Liability and Qualified Immunity|deliberate indifference]] to the risk of *this* injury. Liability required proof that a full review of Burns's background would have made his use of excessive force a "plainly obvious consequence" of hiring him. Burns's record of misdemeanors did not meet that bar, so the causal link between the hiring decision and Brown's specific injury was too weak to support municipal liability.

## Conclusion
The judgment was **reversed**. O'Connor, J., delivered the opinion of the Court (5–4); Souter, J. (joined by Stevens and Breyer, JJ.), and Breyer, J. (joined by Stevens and Ginsburg, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Bryan County* extends *[[City of Canton v. Harris]]*'s deliberate-indifference standard to hiring and, together with *[[Monell v. Department of Social Services|Monell]]*, makes single-incident municipal liability exceptionally hard to prove: the plaintiff must connect the specific applicant's known background to the specific violation as a "plainly obvious" consequence. Teach it as the outer limit of *[[Monell v. Department of Social Services|Monell]]* "policy" liability.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Board of County Commissioners of Bryan County v. Brown*, 520 U.S. 397 (1997)](https://www.courtlistener.com/opinion/118104/board-of-county-commissioners-of-bryan-county-v-brown/) — pinpoint: 411 (O'Connor, J., for the Court; the CL opinion text carries the reporter star `*411` in the paragraph stating the standard). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7775f8ac8b31f12e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Board of County Commissioners of Bryan County v. Brown"}, "payload": {"all": [{"cite": "520 U.S. 397", "page": "397", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "520"}, {"cite": "117 S. Ct. 1382", "page": "1382", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "117"}, {"cite": "137 L. Ed. 2d 626", "page": "626", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "1997 U.S. LEXIS 2793", "page": "2793", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}, {"cite": "65 U.S.L.W. 4286", "page": "4286", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "65"}, {"cite": "10 Fla. L. Weekly Fed. S 405", "page": "405", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "10"}, {"cite": "12 I.E.R. Cas. (BNA) 1217", "page": "1217", "reporter": "I.E.R. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "12"}, {"cite": "97 Cal. Daily Op. Serv. 3033", "page": "3033", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "97"}, {"cite": "97 Daily Journal DAR 5311", "page": "5311", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "97"}], "display": "520 U.S. 397", "official": {"cite": "520 U.S. 397", "page": "397", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "520"}, "official_selection_present": true, "record_id": "Board of County Commissioners of Bryan County v. Brown"}}
{"assertion_id": "132ca9f3fc740940", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Board of County Commissioners of Bryan County v. Brown"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Board of County Commissioners of Bryan County v. Brown", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Board of County Commissioners of Bryan County v. Brown

```json
{
  "schema_version": "s2.v1",
  "record_id": "Board of County Commissioners of Bryan County v. Brown",
  "status": "under_review",
  "identity": {
    "case_name": "Board of the County Commissioners of Bryan County v. Brown",
    "case_name_short": "Brown",
    "case_name_full": "BOARD OF THE COUNTY COMMISSIONERS OF BRYAN COUNTY, OKLAHOMA v. BROWN Et Al.",
    "input_case_name": "Board of County Commissioners of Bryan County v. Brown",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-28",
    "year": 1997,
    "docket": "95-1100",
    "cluster_id": 118104,
    "lead_opinion_id": 9842136,
    "sibling_ids": [],
    "absolute_url": "/opinion/118104/board-of-the-county-commissioners-of-bryan-county-v-brown/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 397",
      "volume": "520",
      "reporter": "U.S.",
      "page": "397",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1382",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 626",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 U.S.L.W. 4286",
        "volume": "65",
        "reporter": "U.S.L.W.",
        "page": "4286",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Fla. L. Weekly Fed. S 405",
        "volume": "10",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 I.E.R. Cas. (BNA) 1217",
        "volume": "12",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1217",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Daily Journal DAR 5311",
        "volume": "97",
        "reporter": "Daily Journal DAR",
        "page": "5311",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2793",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Cal. Daily Op. Serv. 3033",
        "volume": "97",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 397",
        "volume": "520",
        "reporter": "U.S.",
        "page": "397",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1382",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 626",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2793",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2793",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 U.S.L.W. 4286",
        "volume": "65",
        "reporter": "U.S.L.W.",
        "page": "4286",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 Fla. L. Weekly Fed. S 405",
        "volume": "10",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 I.E.R. Cas. (BNA) 1217",
        "volume": "12",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1217",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Cal. Daily Op. Serv. 3033",
        "volume": "97",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 Daily Journal DAR 5311",
        "volume": "97",
        "reporter": "Daily Journal DAR",
        "page": "5311",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 397",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 397",
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
    "date_created": "2026-07-07T13:24:37Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "board-of-county-commissioners-of-bryan-county-v-brown--118104",
      "to_record_id": "Board of County Commissioners of Bryan County v. Brown",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Board of County Commissioners of Bryan County v. Brown

```
<opinion type="majority">
<author id="b491-9">Justice O’Connor</author>
<p id="AOj">delivered the opinion of the Court.</p>
<p id="b491-10">Respondent Jill Brown brought a claim for damages against petitioner Bryan County under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>. She alleged that a county police officer used <page-number citation-index="1" label="400">*400</page-number>excessive force in arresting her, and that the county itself was liable for her injuries based on its sheriff’s hiring and training decisions. She prevailed on her claims against the county following a jury trial, and the Court of Appeals for the Fifth Circuit affirmed the judgment against the county on the basis of the hiring claim alone. 67. F. 3d 1174 (1995). We granted certiorari. We conclude that the Court of Appeals’ decision cannot be squared with our recognition that, in enacting § 1983, Congress did not intend to impose liability on a municipality unless <em>deliberate </em>action attributable to the municipality itself is the “moving force” behind the plaintiff’s deprivation of federal rights. <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 694</a></span> (1978).</p>
<p id="b492-7">I</p>
<p id="b492-3">In the early morning hours of May 12, 1991, Jill Brown (hereinafter respondent) and her husband were driving from Grayson County, Texas, to their home in Bryan County, Oklahoma. After crossing into Oklahoma, they approached a police checkpoint. Mr. Brown, who was driving, decided to avoid the checkpoint and return to Texas. After seeing the Browns’ truck turn away from the checkpoint, Bryan County Deputy Sheriff Robert Morrison and Reserve Deputy Stacy Burns pursued the vehicle. Although the parties’ versions of events differ, at trial both deputies claimed that their patrol car reached speeds in excess of 100 miles per hour. Mr. Brown testified that he was unaware of the deputies’ attempts to overtake him. The chase finally ended four miles south of the police checkpoint.</p>
<p id="b492-4">After he got out of the squad car, Deputy Sheriff Morrison pointed his gun toward the Browns’ vehicle and ordered the Browns to raise their hands. Reserve Deputy Burns, who was unarmed, rounded the corner of the vehicle on the passenger’s side. Burns twice ordered respondent from the .vehicle. When she did not exit, he used an “arm bar” technique, grabbing respondent’s arm at the wrist and elbow, <page-number citation-index="1" label="401">*401</page-number>pulling her from the vehicle, and spinning her to the ground. Respondent’s knees were severely injured, and she later underwent corrective surgery. Ultimately, she may need knee replacements.</p>
<p id="b493-5">Respondent sought compensation for her injuries under <span class="citation no-link">42 U. S. C. § 1983</span> and state law from Burns, Bryan County Sheriff B. J. Moore, and the county itself. Respondent claimed, among other things, that Bryan County was liable for Burns’ alleged use of excessive force based on Sheriff Moore’s decision to hire Burns, the son of his nephew. Specifically, respondent claimed that Sheriff Moore had failed to adequately review Burns’ background. Burns had a record of driving infractions and had pleaded guilty to various driving-related and other misdemeanors, including assault and battery, resisting arrest, and public drunkenness. Oklahoma law does not preclude the hiring of an individual who has committed a misdemeanor to serve as a peace officer. See Okla. Stat., Tit. 70, § 3311(D)(2)(a) (1991) (requiring that the hiring agency certify that the prospective officer’s records do not reflect a felony conviction). At trial, Sheriff Moore testified that he had obtained Burns’ driving record and a report on Burns from the National Crime Information Center, but had not closely reviewed either. Sheriff Moore authorized Burns to make arrests, but not to carry a weapon or to operate a patrol car.</p>
<p id="b493-6">In a ruling not at issue here, the District Court dismissed respondent’s § 1983 claim against Sheriff Moore prior to trial. App. 28. Counsel for Bryan County stipulated that Sheriff Moore “was the policy maker for Bryan County regarding the Sheriff’s Department.” <em>Id., </em>at 30. At the close of respondent’s case and again at the close of all of the evidence, Bryan County moved for judgment as a matter of law. As to respondent’s claim that Sheriff Moore’s decision to hire Burns triggered municipal liability, the county argued that a single hiring decision by a municipal policymaker could not give rise to municipal liability under § 1983. <em>Id., </em>at 59-60. <page-number citation-index="1" label="402">*402</page-number>The District Court denied the county’s motions. The court also overruled the county’s objections to jury instructions on the § 1983 claim against the county. <em>Id., </em>at 125-126, 132.</p>
<p id="b494-5">To resolve respondent’s claims, the jury was asked to answer several interrogatories. The jury concluded that Stacy Burns had arrested respondent without probable cause and had used excessive force, and therefore found him liable for respondent’s injuries. It also found that the “hiring policy” and the “training policy” of Bryan County “in the case of Stacy Burns as instituted by its policymaker, B. J. Moore,” were each “so inadequate as to amount to deliberate indifference to the constitutional needs of the Plaintiff.” <em>Id., </em>at 135. The District Court entered judgment for respondent on the issue of Bryan County’s §1983 liability. The county appealed on several grounds, and the Court of Appeals for the Fifth Circuit affirmed. <span class="citation multiple-matches"><a href="/c/F.%203d/67/1174/">67 F. 3d 1174</a></span> (1995). The court held, among other things, that Bryan County was properly found liable under § 1983 based on Sheriff Moore’s decision to hire Burns. <em>Id., </em>at 1185. The court addressed only those points that it thought merited review; it did not address the jury’s determination of county liability based on inadequate training of Burns, <em>id., </em>at 1178, nor do we. We granted cer-tiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./517/1154/">517 U. S. 1154</a></span> (1996), to decide whether the county was properly held liable for respondent’s injuries based on Sheriff Moore’s single decision to hire Burns. We now reverse.</p>
<p id="b494-6">II</p>
<p id="b494-7">Title <span class="citation no-link">42 U. S. C. § 1983</span> provides in relevant part:</p>
<blockquote id="b494-8">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party in<page-number citation-index="1" label="403">*403</page-number>jured in an action at jaw, suit in equity, or other proper proceeding for redress.”</blockquote>
<p id="b495-6">We held in <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#689" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 689</a></span>, that municipalities and other local governmental bodies are “persons” within the meaning of § 1983. We also recognized that a municipality may not be held liable under § 1983 solely because it employs a tortfeasor. Our conclusion rested partly on the language of § 1983 itself. In' light of the statute’s imposition of liability on one who “subjects [a person], or causes [that person] to be subjected,” to a deprivation of federal rights, we concluded that it “cannot be easily read to impose liability vicariously on governing bodies solely on the basis of the existence of an employer-employee relationship with a tortfeasor.” <em>Id., </em>at 692. Our conclusion also rested upon the statute’s legislative history. As stated in <em>Pembaur </em>v. <em>Cincinnati, 475 </em>U. S. 469, 479 (1986), “while Congress never questioned its power to impose civil liability on municipalities for their <em>own </em>illegal acts, Congress did doubt its constitutional power to impose such liability in order to oblige municipalities to control the conduct of <em>others” </em>(citing <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#665" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 665-683</a></span>). We have consistently refused to hold municipalities liable under a theory of <em>respondeat superior. </em>See <em>Oklahoma City </em>v. <em>Tuttle, </em><span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#818" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 818</a></span> (1985) (plurality opinion); <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#828" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>id., </em>at 828</a></span> (opinion of Brennan, J.); <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#478" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 478-479</a></span>; <em>St. Louis </em>v. <em>Praprotnik, </em><span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#122" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112, 122</a></span> (1988) (plurality opinion); <span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/#137" aria-description="Citation for case: City of St. Louis v. Praprotnik"><em>id., </em>at 137</a></span> (opinion of Brennan, J.); <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378, 392</a></span> (1989).</p>
<p id="b495-7">Instead, in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and subsequent cases, we have required a plaintiff seeking to impose liability on a municipality under §1983 to identify a municipal “policy” or “custom” that caused the plaintiff’s injury. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>; <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#480" aria-description="Citation for case: Pembaur v. City of Cincinnati"><em>Pembaur, supra, </em>at 480-481</a></span>; <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#389" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 389</a></span>. Locating a “policy” ensures that a municipality is held liable only for those deprivations resulting from the decisions of its duly constituted legislative body or of those officials whose acts <page-number citation-index="1" label="404">*404</page-number>may fairly be said to be those of the municipality. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>Monell, supra, </em>at 694</a></span>. Similarly, an act performed pursuant to a “custom” that has not been formally approved by an appropriate decisionmaker may fairly subject a municipality to liability on the theory that the relevant practice is so widespread as to have the force of law. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 690</a></span>-691 (citing <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#167" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 167-168</a></span> (1970)).</p>
<p id="b496-5">The parties join issue on whether, under <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and subsequent cases, a single hiring decision by a county sheriff can be a “policy” that triggers municipal liability. Relying on our decision in <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>respondent claims that a single act by a decisionmaker with final authority in the relevant area constitutes a “policy” attributable to the municipality itself. So long as a § 1983 plaintiff identifies a decision properly attributable to the municipality, respondent argues, there is no risk of imposing <em>respondeat superior </em>liability. Whether that decision was intended to govern only the situation at hand or to serve as a rule to be applied over time is immaterial. Rather, under respondent’s theory, identification of an act of a proper municipal decisionmaker is all that is required to ensure that the municipality is held liable only for its own conduct. The Court of Appeals accepted respondent’s approach.</p>
<p id="b496-6">As our § 1983 municipal liability jurisprudence illustrates, however, it is not enough for a § 1983 plaintiff merely to identify conduct properly attributable to the municipality. The plaintiff must also demonstrate that, through its <em>deliberate </em>conduct, the municipality was the “moving force” behind the injury alleged. That is, a plaintiff must show that the municipal action was taken with the requisite degree of culpability and must demonstrate a direct causal link between the municipal action and the deprivation of federal rights.</p>
<p id="b496-7">Where a plaintiff claims that a particular municipal action <em>itself </em>violates federal law, or directs an employee to do so, resolving these issues of fault and causation is straightfor<page-number citation-index="1" label="405">*405</page-number>ward. Section 1983 itself “contains no state-of-mind requirement independent of that necessary to state a violation” of the underlying federal right. <em>Daniels </em>v. <em>Williams, </em><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/#330" aria-description="Citation for case: Daniels v. Williams">474 U. S. 327, 330</a></span> (1986). In any § 1983 suit, however, the plaintiff must establish the state of mind required to prove the underlying violation. Accordingly, proof that a municipality’s legislative body or authorized decisionmaker has intentionally deprived a plaintiff of a federally protected right necessarily establishes that the municipality acted culpably. Similarly, the conclusion that the action taken or directed by the municipality or its authorized decisionmaker itself violates federal law will also determine that the municipal action was the moving force behind the injury of which the plaintiff complains.</p>
<p id="b497-5">Sheriff Moore’s hiring decision was itself legal, and Sheriff Moore did not authorize Burns to use excessive force. Respondent’s claim, rather, is that a single facially lawful hiring decision can launch a series of events that ultimately cause a violation of federal rights. Where a plaintiff claims that the municipality has not directly inflicted an injury, but nonetheless has caused an employee to do so, rigorous standards of culpability and causation must be applied to ensure that the municipality is not held liable solely for the actions of its employee. See <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#391" aria-description="Citation for case: City of Canton v. Harris"><em>Canton, supra, </em>at 391-392</a></span>; <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#824" aria-description="Citation for case: City of Oklahoma v. Tuttle"><em>Tuttle, supra, </em>at 824</a></span> (plurality opinion). See also <em>Springfield </em>v. <em>Kibbe, </em><span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/#270" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257, 270-271</a></span> (1987) <em>(per curiam) </em>(dissent from dismissal of writ as improvidently granted).</p>
<p id="b497-6">In relying heavily on <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>respondent blurs the distinction between § 1983 cases that present no difficult questions of fault and causation and those that do. To the extent that we have recognized a cause of action under § 1983 based on a single decision attributable to a municipality, we have done so only where the evidence that the municipality had acted and that the plaintiff had suffered a deprivation of federal rights also proved fault and causation. For example, <em>Owen </em>v. <em>Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980), and <em>Newport </em>v. <page-number citation-index="1" label="406">*406</page-number><em>Fact Concerts, Inc., </em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S. 247</a></span> (1981), involved formal decisions of municipal legislative bodies. In <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Owen</a></span>, </em>the city council allegedly censured and discharged an employee without a hearing. <span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/#627" aria-description="Citation for case: Owen v. City of Independence">445 U. S., at 627-629, 633</a></span>, and n. 13. In <em>Fact Concerts, </em>the city council canceled a license permitting a concert following a dispute over the performance’s content. <span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/#252" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">453 U. S., at 252</a></span>. Neither decision reflected implementation of a generally applicable rule. But we did not question that each decision, duly promulgated by city lawmakers, could trigger municipal liability if the decision itself were found to be unconstitutional. Because fault and causation were obvious in each case, proof that the municipality’s decision was unconstitutional would suffice to establish that the municipality itself was liable for the plaintiff’s constitutional injury.</p>
<p id="b498-5">Similarly, <em>Pembaur </em>v. <em>Cincinnati </em>concerned a decision by a county prosecutor, acting as the county’s final decision-maker, <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#485" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S., at 485</a></span>, to direct county deputies to forcibly enter petitioner’s place of business to serve <em>capiases </em>upon third parties. Relying on <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Owen</a></span> </em>and <em><span class="citation" data-id="9428471"><a href="/opinion/110553/city-of-newport-v-fact-concerts-inc/" aria-description="Citation for case: City of Newport v. Fact Concerts, Inc.">Newport</a></span>, </em>we concluded that a final decisionmaker’s adoption of a course of action “tailored to a particular situation and not intended to control decisions in later situations” may, in some circumstances, give rise to municipal liability under § 1983. <span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/#481" aria-description="Citation for case: Pembaur v. City of Cincinnati">475 U. S., at 481</a></span>. In <em><span class="citation" data-id="9430387"><a href="/opinion/111615/pembaur-v-city-of-cincinnati/" aria-description="Citation for case: Pembaur v. City of Cincinnati">Pembaur</a></span>, </em>it was not disputed that the prosecutor had specifically directed the action resulting in the deprivation of petitioner’s rights. The conclusion that the decision was that of a final municipal decisionmaker and was therefore properly attributable to the municipality established municipal liability. No questions of fault or causation arose.</p>
<p id="b498-6">Claims not involving an allegation that the municipal action itself violated federal law, or directed or authorized the deprivation of federal rights, present much more difficult problems of proof. That a plaintiff has suffered a deprivation of federal rights at the hands of a municipal employee will not alone permit an inference of municipal culpability and causation; the plaintiff will simply have shown that the <page-number citation-index="1" label="407">*407</page-number><em>employee </em>acted culpably. We recognized these difficulties in <em>Canton </em>v. <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Harris</a></span>, </em>where we considered a claim that inadequate training of shift supervisors at a city jail led to a deprivation of a detainee’s constitutional rights. We held that, quite apart from the state of mind required to establish the underlying constitutional violation — in that case, a violation of due process, <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 388-389</a></span>, n. 8 — a plaintiff seeking to establish municipal liability on the theory that a facially lawful municipal action has led an employee to violate a plaintiff’s rights must demonstrate that the municipal action was taken with “deliberate indifference” as to its known or obvious consequences. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#388" aria-description="Citation for case: City of Canton v. Harris"><em>Id., </em>at 388</a></span>. A showing of simple or even heightened negligence will not suffice.</p>
<p id="b499-4">We concluded in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>that an “inadequate training” claim could be the basis for § 1983 liability in “limited circumstances.” <em>Id., </em>at 387. We spoke, however, of a deficient training “program,” necessarily intended to apply over time to multiple employees. <em>Id., </em>at 390. Existence of a “program” makes proof of fault and causation at least possible in an inadequate training case. If a program does not prevent constitutional violations, municipal decisionmakers may eventually be put on notice that a new program is called for. Their continued adherence to an approach that they know or should know has failed to prevent tortious conduct by employees may establish the conscious disregard for the consequences of their action — the “deliberate indifference” — necessary to trigger municipal liability. <em>Id., </em>at 390, n. 10 (“It could ... be that the police, in exercising their discretion, so often violate constitutional rights that the need for further training must have been plainly obvious to the city policymakers, who, nevertheless, are ‘deliberately indifferent’ to the need”); <em>id., </em>at 397 (O’Connor, J., concurring in part and dissenting in part) (“[Municipal liability for failure to train may be proper where it can be shown that policymakers were aware of, and acquiesced in, a pattern of constitutional violations . . .”). In addition, the existence of a pattern of <page-number citation-index="1" label="408">*408</page-number>tortious conduct by inadequately trained employees may tend to show that the lack of proper training, rather than a one-time negligent administration of the program or factors peculiar to the officer involved in a particular incident, is the “moving force” behind the plaintiff’s injury. See <em>id., </em>at 390-391.</p>
<p id="b500-5">Before trial, counsel for Bryan County stipulated that Sheriff Moore “was the policy maker for Bryan County regarding the Sheriff’s Department.” App. 30. Indeed, the county sought to avoid liability by claiming that its Board of Commissioners participated in no policy decisions regarding the conduct and operation of the office of the Bryan County Sheriff. <em>Id., </em>at 32. Accepting the county’s representations below, then, this case presents no difficult questions concerning whether Sheriff Moore has final authority to act for the municipality in hiring matters. Cf. <em>Jett </em>v. <em>Dallas Independent School Dist., </em><span class="citation" data-id="9842104"><a href="/opinion/112313/jett-v-dallas-independent-school-district/" aria-description="Citation for case: Jett v. Dallas Independent School District">491 U. S. 701</a></span> (1989); <em>St. Louis </em>v. <em>Praprotnik, </em><span class="citation" data-id="9431224"><a href="/opinion/112017/city-of-st-louis-v-praprotnik/" aria-description="Citation for case: City of St. Louis v. Praprotnik">485 U. S. 112</a></span> (1988). Respondent does not claim that she can identify any pattern of injuries linked to Sheriff Moore’s hiring practices. Indeed, respondent does not contend that Sheriff Moore’s hiring practices are generally defective. The only evidence on this point at trial suggested that Sheriff Moore had adequately screened the backgrounds of all prior deputies he hired. App. 106-110. Respondent instead seeks to trace liability to what can only be described as a deviation from Sheriff Moore’s ordinary hiring practices. Where a claim of municipal liability rests on a single decision, not itself representing a violation of federal law and not directing such a violation, the danger that a municipality will be held liable without fault is high. Because the decision necessarily governs a single case, there can be no notice to the municipal decisionmaker, based on previous violations of federally protected rights, that his approach is inadequate. Nor will it be readily apparent that the municipality’s action caused the injury in question, because the plaintiff can point to no other incident tending to make it more likely that the <page-number citation-index="1" label="409">*409</page-number>plaintiff’s own injury flows from the municipality’s action, rather than from some other intervening cause.</p>
<p id="b501-5">In <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>we did not foreclose the possibility that evidence of a single violation of federal rights, accompanied by a showing that a municipality has failed to train its employees to handle recurring situations presenting an obvious potential for such a violation, could trigger municipal liability. <span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#390" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 390</a></span>, and n. 10 (“[I]t may happen that in light of the duties assigned to specific officers or employees the need for more or different training is so obvious . . . that the policymakers of the city can reasonably be said to have been deliberately indifferent to the need”). Respondent purports to rely on <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>, </em>arguing that Burns’ use of excessive force was the plainly obvious consequence of Sheriff Moore’s failure to screen Burns’ record. In essence, respondent claims that this showing of “obviousness” would demonstrate both that Sheriff Moore acted with conscious disregard for the consequences of his action and that the Sheriff’s action directly caused her injuries, and would thus substitute for the pattern of injuries ordinarily necessary to establish municipal culpability and causation.</p>
<p id="b501-6">The proffered analogy between failure-to-train cases and inadequate screening cases is not persuasive. In leaving open in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>the possibility that a plaintiff might succeed in carrying a failure-to-train claim without showing a pattern of constitutional violations, we simply hypothesized that, in a narrow range of circumstances, a violation of federal rights may be a highly predictable consequence of a failure to equip law enforcement officers with specific tools to handle recurring situations. The likelihood that the situation will recur and the predictability that an officer lacking specific tools to handle that situation will violate citizens’ rights could justify a finding that policymakers’ decision not to train the officer reflected “deliberate indifference” to the obvious consequence of the policymakers’ choice — namely, a violation of a specific constitutional or statutory right. The high degree <page-number citation-index="1" label="410">*410</page-number>of predictability may also support an inference of causation— that the municipality’s indifference led directly to the very consequence that was so predictable.</p>
<p id="b502-5">Where a plaintiff presents a § 1983 claim premised upon the inadequacy of an official’s review of a prospective applicant’s record, however, there is a particular danger that a municipality will be held liable for an injury not directly caused by a deliberate action attributable to the municipality itself. Every injury suffered at the hands of a municipal employee can be traced to a hiring decision in a “but-for” sense: But for the municipality’s decision to hire the employee, the plaintiff would not have suffered the injury. To prevent municipal liability for a hiring decision from collapsing into <em>re-spondeat superior </em>liability, a court must carefully test the link between the policymaker’s inadequate decision and the particular injury alleged.</p>
<p id="b502-6">In attempting to import the reasoning of <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>into the hiring context, respondent ignores the fact that predicting the consequence of a single hiring decision, even one based on an inadequate assessment of a record, is far more difficult than predicting what might flow from the failure to train a single law enforcement officer as to a specific skill necessary to the discharge of his duties. As our decision in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span> </em>makes clear, “deliberate indifference” is a stringent standard of fault, requiring proof that a municipal actor disregarded a known or obvious consequence of his action. Unlike the risk from a particular glaring omission in a training regimen, the risk from a single instance of inadequate screening of an applicant’s background is not “obvious” in the abstract; rather, it depends upon the background of the applicant. A lack of scrutiny may increase the likelihood that an unfit officer will be hired, and that the unfit officer will, when placed in a particular position to affect the rights of citizens, act improperly. But that is only a generalized showing of risk. The fact that inadequate scrutiny of an applicant’s background would make a violation of rights more <em>likely </em>cannot alone <page-number citation-index="1" label="411">*411</page-number>give rise to an inference that a policymaker’s failure to scrutinize the record of a particular applicant produced a specific constitutional violation. After all, a full screening of an applicant’s background might reveal no cause for concern at all; if so, a hiring official who failed to scrutinize the applicant’s background cannot be said to have consciously disregarded an obvious risk that the officer would subsequently inflict a particular constitutional injury.</p>
<p id="b503-5">We assume that a jury could properly find in this case that Sheriff Moore’s assessment of Burns’ background was inadequate. Sheriff Moore’s own testimony indicated that he did not inquire into the underlying conduct or the disposition of any of the misdemeanor charges reflected on Burns’ record before hiring him. But this showing of an instance of inadequate screening is not enough to establish “deliberate indifference.” In layman’s terms, inadequate screening of an applicant’s record may reflect “indifference” to the applicant’s background. For purposes of a legal inquiry into municipal liability under § 1983, however, that is not the <em>relevant </em>“indifference.” A plaintiff must demonstrate that a municipal decision reflects deliberate indifference to the risk that a violation of a particular constitutional or statutory right will follow the decision. Only where adequate scrutiny of an applicant’s background would lead a reasonable policymaker to conclude that the plainly obvious consequence of the decision to hire the applicant would be the deprivation of a third party’s federally protected right can the official’s failure to adequately scrutinize the applicant’s background constitute “deliberate indifference.”</p>
<p id="b503-6">Neither the District Court nor the Court of Appeals directly tested the link between Burns’ actual background and the risk that, if hired, he would use excessive force. The District Court instructed the jury on a theory analogous to that reserved in <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Canton</a></span>. </em>The court required respondent to prove that Sheriff Moore’s inadequate screening of Burns’ background was “so likely to result in <em>violations of constitu</em><page-number citation-index="1" label="412">*412</page-number><em>tional rights” </em>that the Sheriff could “reasonably [be] said to have been deliberately indifferent to the <em>constitutional needs </em>of the Plaintiff.” App. 12B (emphasis added). The court also instructed the jury, without elaboration, that respondent was required to prove that the “inadequate hiring . . . policy directly caused the Plaintiff’s injury.” <em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">Ibid.</a></span></em></p>
<p id="b504-3">As discussed above, a finding of culpability simply cannot depend on the mere probability that any officer inadequately screened will inflict any constitutional injury. Rather, it must depend on a finding that <em>this </em>officer was highly likely to inflict the <em>particular </em>injury suffered by the plaintiff. The connection between the background of the particular applicant and the specific constitutional violation alleged must be strong. What the District Court’s instructions on culpability, and therefore the jury’s finding of municipal liability, failed to capture is whether Burns’ background made his use of excessive force in making an arrest a plainly obvious consequence of the hiring decision. The Court of Appeals’ af-firmance of the jury’s finding of municipal liability depended on its view that the jury could have found that “inadequate screening of <em>a deputy </em>could likely result in the violation of <em>citizens’ constitutional rights.” </em>67 F. 3d, at 1185 (emphasis added). Beyond relying on a risk of violations of unspecified constitutional rights, the Court of Appeals also posited that Sheriff Moore’s decision reflected indifference to “the public’s welfare.” <em>Id., at </em>1184.</p>
<p id="b504-4">Even assuming without deciding that proof of a single instance of inadequate screening could ever trigger municipal liability, the evidence in this case was insufficient to support a finding that, in hiring Burns, Sheriff Moore disregarded a known or obvious risk of injury. To test the link between Sheriff Moore’s hiring decision and respondent’s injury, we must ask whether a full review of Burns’ record reveals that Sheriff Moore should have concluded that Burns’ use of excessive force would be a plainly obvious consequence of the <page-number citation-index="1" label="413">*413</page-number>hiring decision.<footnotemark>1</footnotemark> On this point, respondent’s showing was inadequate. To be sure, Burns’ record reflected various misdemeanor infractions. Respondent claims that the record demonstrated such a strong propensity for violence that Burns’ application of excessive force was highly likely. The primary charges on which respondent relies, however, are those arising from a fight on a college campus where Burns was a student. In connection with this single incident, Burns was charged with assault and battery, resisting arrest, and public drunkenness.<footnotemark>2</footnotemark> In January 1990, when he pleaded <page-number citation-index="1" label="414">*414</page-number>guilty to those charges, Burns also pleaded guilty to various driving-related offenses, including nine moving violations and a charge of driving with a suspended license. In addition, Burns had previously pleaded guilty to being in actual physical control of a vehicle while intoxicated.</p>
<p id="b506-5">The fact that Burns had pleaded guilty to traffic offenses and other misdemeanors may well have made him an extremely poor candidate for reserve deputy. Had Sheriff Moore fully reviewed Burns’ record, he might have come to precisely that conclusion. But unless he would necessarily have reached that decision <em>because </em>Burns’ use of excessive force would have been a plainly obvious consequence of the hiring decision, Sheriff Moore’s inadequate scrutiny of Burns’ record cannot constitute “deliberate indifference” to respondent’s federally protected right to be free from a use of excessive force.</p>
<p id="b506-6">Justice Souter’s reading of the case is that the jury believed that Sheriff Moore in fact read Burns’ entire record. <em>Post, </em>at 426-427. That is plausible, but it is also irrelevant. It is not sufficient for respondent to show that Sheriff Moore read Burns’ record and therefore hired Burns with knowledge of his background. Such a decision may reflect indif<page-number citation-index="1" label="415">*415</page-number>ference to Burns’ <em>record, </em>but what is required is deliberate indifference to a plaintiff’s constitutional right. That is, whether Sheriff Moore failed to examine Burns’ record, partially examined it, or fully examined it, Sheriff Moore’s hiring decision could not have been “deliberately indifferent” unless in light of that record Burns’ use of excessive force would have been a plainly obvious consequence of the hiring decision. Because there was insufficient evidence on which a jury could base a finding that Sheriff Moore’s decision to hire Burns reflected conscious disregard of an obvious risk that a use of excessive force would follow, the District Court erred in submitting respondent’s inadequate screening claim to the jury.</p>
<p id="b507-5">III</p>
<p id="b507-6">Cases involving 'constitutional injuries allegedly traceable to an ill-considered hiring decision pose the greatest risk that a municipality will be held liable for an injury that it did not cause. In the broadest sense, every injury is traceable to a hiring decision. Where a court fails to adhere to rigorous requirements of culpability and causation, municipal liability collapses into <em>respondeat superior </em>liability. As we recognized in <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>and have repeatedly reaffirmed, Congress did not intend municipalities to be held liable unless <em>deliberate </em>action attributable to the municipality directly caused a deprivation of federal rights. A failure to apply stringent culpability and causation requirements raises serious federalism concerns, in that it risks constitutionalizing particular hiring requirements that States have themselves elected not to impose. Cf. <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/#392" aria-description="Citation for case: City of Canton v. Harris">489 U. S., at 392</a></span>. Bryan County is not liable for Sheriff Moore’s isolated decision to hire Burns without adequate screening, because respondent has not demonstrated that his decision reflected a conscious disregard for a high risk that Burns would use excessive force in violation of respondent’s federally pro<page-number citation-index="1" label="416">*416</page-number>tected right. We therefore vacate the judgment of the Court of Appeals and remand this case for further proceedings consistent with this opinion.</p>
<p id="b508-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b505-4"> In suggesting that our decision complicates this Court’s § 1983 municipal liability jurisprudence by altering the understanding of culpability, Justice Souter and Justice Breyer misunderstand our approach. <em>Post, </em>at 422; <em>post, </em>at 430, 433-434. We do not suggest that a plaintiff in an inadequate screening case must show a higher degree of culpability than the “deliberate indifference” required in <em>Canton </em>v. <em>Harris, </em><span class="citation" data-id="9431589"><a href="/opinion/112209/city-of-canton-v-harris/" aria-description="Citation for case: City of Canton v. Harris">489 U. S. 378</a></span> (1989); we need not do so, because, as discussed below, respondent has not made a showing of deliberate indifference here. See <em>infra </em>this page and 414. Furthermore, in assessing the risks of a decision to hire a particular individual, we draw no distinction between what is “so obvious” or “so likely to occur” and what is “plainly obvious.” The difficulty with the lower courts’ approach is that it fails to connect the background of the particular officer hired in this case to the particular constitutional violation the respondent suffered. <em>Supra, </em>at 412. Ensuring that lower courts link the background of the officer to the constitutional violation alleged does not complicate our municipal liability jurisprudence with degrees of “obviousness,” but seeks to ensure that a plaintiff in an inadequate screening ease establishes a policymaker’s deliberate indifference — that is, conscious disregard for the known and obvious consequences of his actions.</p>
</footnote>
<footnote label="2">
<p id="b505-5"> Justice Souter implies that Burns’ record reflected assault and battery charges arising from more than one incident. <em>Post, </em>at 428. There' has never been a serious dispute that a single misdemeanor assault and battery conviction arose out of a single campus fight. Nor did petitioner’s expert testify that the record reflected any assault charge without a disposition, see 9 Record 535-536, although Justice Souter appears to suggest otherwise, <em>post, </em>at 428-429, n. 6.</p>
<p id="b505-6">In fact, respondent’s own expert witness testified that Burns’ record reflected a single assault conviction. 7 Record 318; see also <em>id., </em>at 320. Petitioner has repeatedly so claimed. See, <em>e. g., </em>Suggestion for Rehearing En Banc in No. 93-5376 (CA5), p. 12 (“Burns had one misdemeanor assault <page-number citation-index="1" label="414">*414</page-number>convietion stemming from a campus fight”); Pet. for Rehearing of Substituted Opinion in No. 93-5376 (CA5), p. 11 (same); 3 Record 927 (Brief in Support of Defendants’ Motion for Judgment Notwithstanding the Verdict 10); Pet. for Cert. 16 (“Burns pled guilty to assault and battery” as a result of “one campus fight”).</p>
<p id="b506-8">Respondent has not once contested this characterization. See, <em>e. g., </em>3 Record 961 (Brief in Support of Plaintiff’s Response to Defendants’ Motion for Judgment Notwithstanding the Jury Verdict 4); Brief for Appellee/ Cross-Appellant Brown et al. in No. 93-5376 (CA5), pp. 3-4; Brief in Opposition 1. Indeed, since the characterization is reflected in the county’s petition for certiorari, under this Court’s Rule 15(2) respondent would have had an obligation in her brief in opposition to correct “any perceived misstatement” in the petition. She did not. Involvement in a single fraternity fracas does not demonstrate “a proclivity to violence against the person.” <em>Post, </em>at 429, n. 6.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Board of Education v. Earls.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Board of Education v. Earls"
type: case
citation: ""
parallel_cite: "536 U.S. 822; 122 S. Ct. 2559; 153 L. Ed. 2d 735; 2002 Daily Journal DAR 7275; 70 U.S.L.W. 4737; 15 Fla. L. Weekly Fed. S 483"
neutral_cite: "2002 U.S. LEXIS 4882; 2002 Cal. Daily Op. Serv. 5761"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-27
docket: 01-332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Board of Education v. Earls
  varies_by_point: false
  scope_note: "Extends Vernonia to non-athletes; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/"
  cluster_id: 121171
  opinion_id: 121171
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Vernonia School District 47J v. Acton]]", "[[New Jersey v. T.L.O.]]", "[[Skinner v. Railway Labor Executives' Assn.]]"]
aliases: ["Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls", "Earls"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "schools"]
holding: "Suspicionless drug testing of all students participating in competitive extracurricular activities is a reasonable special-needs search."
lake:
  record_id: Board of Education v. Earls
  status: verified
  projected_at: 2026-07-09
---

# Board of Education v. Earls

*536 U.S. 822 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The Tecumseh, Oklahoma school district adopted a Student Activities Drug Testing Policy requiring all middle- and high-school students to submit to urinalysis drug testing in order to participate in any competitive extracurricular activity (choir, band, academic team, athletics, and the like). Lindsay Earls and other students who participated in such activities challenged the policy as an unreasonable search.

## Issue
Whether a public school's suspicionless drug testing of all students who participate in competitive extracurricular activities is a reasonable search under the Fourth Amendment.

## Rule
In the public-school special-needs context, the search need not rest on individualized suspicion: "In this context, the Fourth Amendment does not require a finding of individualized suspicion". — 536 U.S. at 837. ^pin-837

Applying the special-needs reasonableness balance, the Court upheld the policy: "we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren." — [*Id.* at 838](https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/#:~:text=we%20hold%20only%20that%20Tecumseh%27s). ^pin-838

## Application
On these facts the testing reached students who voluntarily participated in extracurricular activities, the intrusion (a monitored but private urine sample, results kept confidential and not turned over to law enforcement) was limited, and the district faced a documented drug problem within its custodial responsibility over schoolchildren. Weighing those factors, the Court concluded the Tecumseh policy was a reasonable, effective means of addressing drug use and did not require individualized suspicion.

## Conclusion
The policy was a reasonable special-needs search; the judgment of the Tenth Circuit invalidating it was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Earls* **extends** [[Vernonia School District 47J v. Acton]] beyond student athletes to all participants in competitive extracurricular activities.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Board of Education v. Earls*, 536 U.S. 822 (2002) — https://www.courtlistener.com/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/ — pinpoints: 837, 838.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "55953a17721bf523", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Board of Education v. Earls"}, "payload": {"all": [{"cite": "536 U.S. 822", "page": "822", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "536"}, {"cite": "122 S. Ct. 2559", "page": "2559", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "153 L. Ed. 2d 735", "page": "735", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "153"}, {"cite": "2002 U.S. LEXIS 4882", "page": "4882", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}, {"cite": "2002 Cal. Daily Op. Serv. 5761", "page": "5761", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}, {"cite": "2002 Daily Journal DAR 7275", "page": "7275", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2002"}, {"cite": "70 U.S.L.W. 4737", "page": "4737", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "70"}, {"cite": "15 Fla. L. Weekly Fed. S 483", "page": "483", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "15"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Board of Education v. Earls"}}
{"assertion_id": "57872668044bbad2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-837", "record_id": "Board of Education v. Earls"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-837", "pinpoint_status": "slip-only", "quote": "--- # Board of Education v. Earls *536 U.S. 822 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The Tecumseh, Oklahoma school district adopted a Student Activities Drug Testing Policy requiring all middle- and high-school students to submit to urinalysis drug testing in order to participate in any competitive extracurricular activity (choir, band, academic team, athletics, and the like). Lindsay Earls and other students who participated in such activities challenged the policy as an unreasonable search. ## Issue Whether a public school's suspicionless drug testing of all students who participate in competitive extracurricular activities is a reasonable search under the Fourth Amendment. ## Rule In the public-school special-needs context, the search need not rest on individualized suspicion:", "quote_fidelity": "mismatch", "record_id": "Board of Education v. Earls", "star_marker": null}}
{"assertion_id": "7a433abbe830aaae", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-838", "record_id": "Board of Education v. Earls"}, "payload": {"fragment": "#:~:text=we%20hold%20only%20that%20Tecumseh%27s", "page": null, "pin_id": "pin-838", "pinpoint_status": "star-verified", "quote": "we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren.", "quote_fidelity": "matched", "record_id": "Board of Education v. Earls", "star_marker": "838"}}
{"assertion_id": "f104b55a02e12220", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Board of Education v. Earls"}, "payload": {"as_of_content": "2002-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Board of Education v. Earls", "scope_note": "Extends Vernonia to non-athletes; good law.", "varies_by_point": false}}
```

### lake record — Board of Education v. Earls

```json
{
  "schema_version": "s2.v1",
  "record_id": "Board of Education v. Earls",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
    "case_name_short": "Earls",
    "case_name_full": "BOARD OF EDUCATION OF INDEPENDENT SCHOOL DISTRICT NO. 92 OF POTTAWATOMIE COUNTY Et Al. v. EARLS Et Al.",
    "input_case_name": "Board of Education v. Earls",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-27",
    "year": 2002,
    "docket": "01-332",
    "cluster_id": 121171,
    "lead_opinion_id": 121171,
    "sibling_ids": [
      121171,
      9434325,
      9434326,
      9434327,
      9434328
    ],
    "absolute_url": "/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9271936,
        "score": 20,
        "case_name": "Board of Education of Independent School District No. 92 v. Earls"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "536 U.S. 822",
        "volume": "536",
        "reporter": "U.S.",
        "page": "822",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2559",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 735",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Daily Journal DAR 7275",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "7275",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 U.S.L.W. 4737",
        "volume": "70",
        "reporter": "U.S.L.W.",
        "page": "4737",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "15 Fla. L. Weekly Fed. S 483",
        "volume": "15",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4882",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Cal. Daily Op. Serv. 5761",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "5761",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 822",
        "volume": "536",
        "reporter": "U.S.",
        "page": "822",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2559",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 735",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4882",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Cal. Daily Op. Serv. 5761",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "5761",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Daily Journal DAR 7275",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "7275",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 U.S.L.W. 4737",
        "volume": "70",
        "reporter": "U.S.L.W.",
        "page": "4737",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "15 Fla. L. Weekly Fed. S 483",
        "volume": "15",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-837",
      "page": null,
      "quote": "--- # Board of Education v. Earls *536 U.S. 822 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The Tecumseh, Oklahoma school district adopted a Student Activities Drug Testing Policy requiring all middle- and high-school students to submit to urinalysis drug testing in order to participate in any competitive extracurricular activity (choir, band, academic team, athletics, and the like). Lindsay Earls and other students who participated in such activities challenged the policy as an unreasonable search. ## Issue Whether a public school's suspicionless drug testing of all students who participate in competitive extracurricular activities is a reasonable search under the Fourth Amendment. ## Rule In the public-school special-needs context, the search need not rest on individualized suspicion:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-838",
      "page": null,
      "quote": "we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren.",
      "star_marker": "838",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 37097,
      "fragment": "#:~:text=we%20hold%20only%20that%20Tecumseh%27s",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Board of Education v. Earls",
    "varies_by_point": false,
    "scope_note": "Extends Vernonia to non-athletes; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mangino v. Incorporated Village of Patchogue",
          "cluster_id": 3164642,
          "cite": [
            "808 F.3d 951",
            "2015 U.S. App. LEXIS 22431",
            "2015 WL 9287019"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re D.H.",
          "cluster_id": 5280981,
          "cite": [
            "306 S.W.3d 955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gillman Ex Rel. Gillman v. School Board for Holmes County",
          "cluster_id": 1454556,
          "cite": [
            "567 F. Supp. 2d 1359",
            "2008 U.S. Dist. LEXIS 56589",
            "2008 WL 2854266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Frederick",
          "cluster_id": 145707,
          "cite": [
            "168 L. Ed. 2d 290",
            "127 S. Ct. 2618",
            "551 U.S. 393",
            "2007 U.S. LEXIS 8514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Shukri Baker",
          "cluster_id": 618459,
          "cite": [
            "664 F.3d 467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christian Legal Soc. Chapter of Univ. of Cal., Hastings College of Law v. Martinez",
          "cluster_id": 150544,
          "cite": [
            "177 L. Ed. 2d 838",
            "130 S. Ct. 2971",
            "561 U.S. 661",
            "2010 U.S. LEXIS 5367"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Ontario v. Quon",
          "cluster_id": 148797,
          "cite": [
            "177 L. Ed. 2d 216",
            "130 S. Ct. 2619",
            "560 U.S. 746",
            "2010 U.S. LEXIS 4972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Woodard",
          "cluster_id": 4578612,
          "cite": [
            "912 F.3d 1278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittan Holland v. Kelly Rosen",
          "cluster_id": 4515181,
          "cite": [
            "895 F.3d 272"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brandon Michael Lifshitz",
          "cluster_id": 786321,
          "cite": [
            "369 F.3d 173",
            "2004 WL 1043468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 01-5098",
          "cluster_id": 782823,
          "cite": [
            "336 F.3d 1194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Lee Scott",
          "cluster_id": 794629,
          "cite": [
            "450 F.3d 863",
            "2006 U.S. App. LEXIS 14182"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul G. Sczubelek",
          "cluster_id": 789683,
          "cite": [
            "402 F.3d 175",
            "2005 WL 638158"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Board of Education v. Earls:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM2NTQwODAwMDAwJnM9Nzc5NzQ1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MiZzPTI1MDcxNjkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121171 OR 9434325 OR 9434326 OR 9434327 OR 9434328)",
    "indexed_citing_opinions": 274,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121171,
        "count": 243,
        "count_source": "search"
      },
      {
        "opinion_id": 9434325,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9434326,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434327,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434328,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 499,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/board-of-education-v-earls.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5MDY1Mjgmcz00Nzc4NDAyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121171+OR+9434325+OR+9434326+OR+9434327+OR+9434328%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121171,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 106395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 112779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 118432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 772423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121171,
        "cited_id": 2580272,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:09:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Board of Education v. Earls

```
<div>
<center><b><span class="citation" data-id="9434325"><a href="/opinion/121171/board-of-education-of-independent-school-district-no-92-of-pottawatomie/" aria-description="Citation for case: Board of Education of Independent School District No. 92...">536 U.S. 822</a></span> (2002)</b></center>
<center><h1>BOARD OF EDUCATION OF INDEPENDENT SCHOOL DISTRICT NO. 92 OF POTTAWATOMIE COUNTY et al.<br>
v.<br>
EARLS et al.</h1></center>
<center>No. 01-332.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 19, 2002.</center>
<center>Decided June 27, 2002.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT
<p><span class="star-pagination">*823</span> <span class="star-pagination">*824</span> Thomas, J., delivered the opinion of the Court, in which Rehnquist, C. J., and Scalia, Kennedy, and Breyer, JJ., joined. Breyer, J., filed a concurring opinion, <i>post,</i> p. 838. O'Connor, J., filed a dissenting opinion, in which Souter, J., joined, <i>post,</i> p. 842. Ginsburg, J., filed a dissenting <span class="star-pagination">*825</span> opinion, in which Stevens, O'Connor, and Souter, JJ., joined, <i>post,</i>  p. 842.</p>
<p><i>Linda Maria Meoli</i> argued the cause for petitioners. With her on the briefs were <i>Stephanie J. Mather</i> and <i>William P. Bleakley.</i> </p>
<p><i>Deputy Solicitor General Clement</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General McCallum, Gregory G. Garre, Leonard Schaitman,</i> and <i>Lowell V. Sturgill, Jr.</i> </p>
<p><i>Graham A. Boyd</i> argued the cause for respondents. With him on the brief was <i>Steven R. Shapiro.</i><sup>[*]</sup></p>
<p>Justice Thomas, delivered the opinion of the Court.</p>
<p>The Student Activities Drug Testing Policy implemented by the Board of Education of Independent School District No. 92 of Pottawatomie County (School District) requires all students who participate in competitive extracurricular activities to submit to drug testing. Because this Policy reasonably serves the School District's important interest in detecting and preventing drug use among its students, we hold that it is constitutional.</p>
<p></p>
<h2>
<span class="star-pagination">*826</span> I</h2>
<p>The city of Tecumseh, Oklahoma, is a rural community located approximately 40 miles southeast of Oklahoma City. The School District administers all Tecumseh public schools. In the fall of 1998, the School District adopted the Student Activities Drug Testing Policy (Policy), which requires all middle and high school students to consent to drug testing in order to participate in any extracurricular activity. In practice, the Policy has been applied only to competitive extracurricular activities sanctioned by the Oklahoma Secondary Schools Activities Association, such as the Academic Team, Future Farmers of America, Future Homemakers of America, band, choir, pom pon, cheerleading, and athletics. Under the Policy, students are required to take a drug test before participating in an extracurricular activity, must submit to random drug testing while participating in that activity, and must agree to be tested at any time upon reasonable suspicion. The urinalysis tests are designed to detect only the use of illegal drugs, including amphetamines, marijuana, cocaine, opiates, and barbituates, not medical conditions or the presence of authorized prescription medications.</p>
<p>At the time of their suit, both respondents attended Tecumseh High School. Respondent Lindsay Earls was a member of the show choir, the marching band, the Academic Team, and the National Honor Society. Respondent Daniel James sought to participate in the Academic Team.<sup>[1]</sup> Together with their parents, Earls and James brought a Rev. <span class="star-pagination">*827</span> Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, action against the School District, challenging the Policy both on its face and as applied to their participation in extracurricular activities.<sup>[2]</sup> They alleged that the Policy violates the Fourth Amendment as incorporated by the Fourteenth Amendment and requested injunctive and declarative relief. They also argued that the School District failed to identify a special need for testing students who participate in extracurricular activities, and that the "Drug Testing Policy neither addresses a proven problem nor promises to bring any benefit to students or the school." App. 9.</p>
<p>Applying the principles articulated in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), in which we upheld the suspicionless drug testing of school athletes, the United States District Court for the Western District of Oklahoma rejected respondents' claim that the Policy was unconstitutional and granted summary judgment to the School District. The court noted that "special needs" exist in the public school context and that, although the School District did "not show a drug problem of epidemic proportions," there was a history of drug abuse starting in 1970 that presented "legitimate cause for concern." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1287" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1287</a></span> (2000). The District Court also held that the Policy was effective because "[i]t can scarcely be disputed that the drug problem among the student body is effectively addressed by making sure that the large number of students participating in competitive, extracurricular activities do not use drugs." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1295" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh..."><i>Id.,</i>  at 1295</a></span>.</p>
<p>The United States Court of Appeals for the Tenth Circuit reversed, holding that the Policy violated the Fourth Amendment. The Court of Appeals agreed with the District Court that the Policy must be evaluated in the "unique environment of the school setting," but reached a different conclusion <span class="star-pagination">*828</span> as to the Policy's constitutionality. <span class="citation multiple-matches"><a href="/c/F.%203d/242/1264/">242 F. 3d 1264</a></span>, 1270 (2001). Before imposing a suspicionless drug testing program, the Court of Appeals concluded that a school "must demonstrate that there is some identifiable drug abuse problem among a sufficient number of those subject to the testing, such that testing that group of students will actually redress its drug problem." <i>Id.,</i> at 1278. The Court of Appeals then held that because the School District failed to demonstrate such a problem existed among Tecumseh students participating in competitive extracurricular activities, the Policy was unconstitutional. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./534/1015/">534 U. S. 1015</a></span> (2001), and now reverse.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment to the United States Constitution protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." Searches by public school officials, such as the collection of urine samples, implicate Fourth Amendment interests. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 652</a></span>; cf. <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334</a></span> (1985). We must therefore review the School District's Policy for "reasonableness," which is the touchstone of the constitutionality of a governmental search.</p>
<p>In the criminal context, reasonableness usually requires a showing of probable cause. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 619</a></span> (1989). The probable-cause standard, however, "is peculiarly related to criminal investigations" and may be unsuited to determining the reasonableness of administrative searches where the "Government seeks to <i>prevent</i> the development of hazardous conditions." <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#667" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 667-668</a></span> (1989) (internal quotation marks and citations omitted) (collecting cases). The Court has also held that a warrant and finding of probable cause are unnecessary in the public school context because such requirements "`would unduly interfere with the maintenance of the swift and informal <span class="star-pagination">*829</span> disciplinary procedures [that are] needed.' " <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Vernonia, supra,</a></span></i> at 653 (quoting <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 340-341</a></span>).</p>
<p>Given that the School District's Policy is not in any way related to the conduct of criminal investigations, see Part IIB, <i>infra,</i> respondents do not contend that the School District requires probable cause before testing students for drug use. Respondents instead argue that drug testing must be based at least on some level of individualized suspicion. See Brief for Respondents 12-14. It is true that we generally determine the reasonableness of a search by balancing the nature of the intrusion on the individual's privacy against the promotion of legitimate governmental interests. See <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979). But we have long held that "the Fourth Amendment imposes no irreducible requirement of [individualized] suspicion." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 561</a></span> (1976). "[I]n certain limited circumstances, the Government's need to discover such latent or hidden conditions, or to prevent their development, is sufficiently compelling to justify the intrusion on privacy entailed by conducting such searches without any measure of individualized suspicion." <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Von Raab, supra,</i>  at 668</a></span>; see also <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#624" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 624</a></span>. Therefore, in the context of safety and administrative regulations, a search unsupported by probable cause may be reasonable "when `special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.' " <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (quoting <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 351</a></span> (Blackmun, J., concurring in judgment)); see also <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 653</a></span>; <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 619</a></span>.</p>
<p>Significantly, this Court has previously held that "special needs" inhere in the public school context. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 653</a></span>; <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O."><i>T. L. O., supra,</i> at 339-340</a></span>. While schoolchildren do not shed their constitutional rights when they enter the schoolhouse, see <i>Tinker</i> v. <i>Des Moines Independent Community School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), "Fourth <span class="star-pagination">*830</span> Amendment rights . . . are different in public schools than elsewhere; the `reasonableness' inquiry cannot disregard the schools' custodial and tutelary responsibility for children." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 656</a></span>. In particular, a finding of individualized suspicion may not be necessary when a school conducts drug testing.</p>
<p>In <i>Vernonia,</i> this Court held that the suspicionless drug testing of athletes was constitutional. The Court, however, did not simply authorize all school drug testing, but rather conducted a fact-specific balancing of the intrusion on the children's Fourth Amendment rights against the promotion of legitimate governmental interests. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 652-653</a></span>. Applying the principles of <i>Vernonia</i> to the somewhat different facts of this case, we conclude that Tecumseh's Policy is also constitutional.</p>
<p></p>
<h2>A</h2>
<p>We first consider the nature of the privacy interest allegedly compromised by the drug testing. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 654</a></span>. As in <i>Vernonia,</i> the context of the public school environment serves as the backdrop for the analysis of the privacy interest at stake and the reasonableness of the drug testing policy in general. See <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> ("Central . . . is the fact that the subjects of the Policy are (1) children, who (2) have been committed to the temporary custody of the State as schoolmaster"); see also <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#665" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 665</a></span> ("The most significant element in this case is the first we discussed: that the Policy was undertaken in furtherance of the government's responsibilities, under a public school system, as guardian and tutor of children entrusted to its care"); <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> ("[W]hen the government acts as guardian and tutor the relevant question is whether the search is one that a reasonable guardian and tutor might undertake").</p>
<p>A student's privacy interest is limited in a public school environment where the State is responsible for maintaining discipline, health, and safety. Schoolchildren are routinely required to submit to physical examinations and vaccinations <span class="star-pagination">*831</span> against disease. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 656</a></span>. Securing order in the school environment sometimes requires that students be subjected to greater controls than those appropriate for adults. See <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#350" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 350</a></span> (Powell, J., concurring) ("Without first establishing discipline and maintaining order, teachers cannot begin to educate their students. And apart from education, the school has the obligation to protect pupils from mistreatment by other children, and also to protect teachers themselves from violence by the few students whose conduct in recent years has prompted national concern").</p>
<p>Respondents argue that because children participating in nonathletic extracurricular activities are not subject to regular physicals and communal undress, they have a stronger expectation of privacy than the athletes tested in <i>Vernonia.</i>  See Brief for Respondents 18-20. This distinction, however, was not essential to our decision in <i>Vernonia,</i> which depended primarily upon the school's custodial responsibility and authority.<sup>[3]</sup></p>
<p>In any event, students who participate in competitive extracurricular activities voluntarily subject themselves to many of the same intrusions on their privacy as do athletes.<sup>[4]</sup><span class="star-pagination">*832</span> Some of these clubs and activities require occasional offcampus travel and communal undress. All of them have their own rules and requirements for participating students that do not apply to the student body as a whole. <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1289" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d, at 1289-1290</a></span>. For example, each of the competitive extracurricular activities governed by the Policy must abide by the rules of the Oklahoma Secondary Schools Activities Association, and a faculty sponsor monitors the students for compliance with the various rules dictated by the clubs and activities. See <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1290" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh..."><i>id.,</i> at 1290</a></span>. This regulation of extracurricular activities further diminishes the expectation of privacy among schoolchildren. Cf<i>. </i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 657</a></span> ("Somewhat like adults who choose to participate in a closely regulated industry, students who voluntarily participate in school athletics have reason to expect intrusions upon normal rights and privileges, including privacy" (internal quotation marks omitted)). We therefore conclude that the students affected by this Policy have a limited expectation of privacy.</p>
<p></p>
<h2>B</h2>
<p>Next, we consider the character of the intrusion imposed by the Policy. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>. Urination is "an excretory function traditionally shielded by great privacy." <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#626" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 626</a></span>. But the "degree of intrusion" on one's privacy caused by collecting a urine sample "depends upon the manner in which production of the urine sample is monitored." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>.</p>
<p>Under the Policy, a faculty monitor waits outside the closed restroom stall for the student to produce a sample and must "listen for the normal sounds of urination in order to guard against tampered specimens and to insure an accurate chain of custody." App. 199. The monitor then pours the sample into two bottles that are sealed and placed into a mailing pouch along with a consent form signed by the student. This procedure is virtually identical to that reviewed in <i>Vernonia,</i> except that it additionally protects privacy by <span class="star-pagination">*833</span> allowing male students to produce their samples behind a closed stall. Given that we considered the method of collection in <i>Vernonia</i> a "negligible" intrusion, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>, the method here is even less problematic.</p>
<p>In addition, the Policy clearly requires that the test results be kept in confidential files separate from a student's other educational records and released to school personnel only on a "need to know" basis. Respondents nonetheless contend that the intrusion on students' privacy is significant because the Policy fails to protect effectively against the disclosure of confidential information and, specifically, that the school "has been careless in protecting that information: for example, the Choir teacher looked at students' prescription drug lists and left them where other students could see them." Brief for Respondents 24. But the choir teacher is someone with a "need to know," because during off-campus trips she needs to know what medications are taken by her students. Even before the Policy was enacted the choir teacher had access to this information. See App. 132. In any event, there is no allegation that any other student did see such information. This one example of alleged carelessness hardly increases the character of the intrusion.</p>
<p>Moreover, the test results are not turned over to any law enforcement authority. Nor do the test results here lead to the imposition of discipline or have any academic consequences. Cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 658</a></span>, and n. 2. Rather, the only consequence of a failed drug test is to limit the student's privilege of participating in extracurricular activities. Indeed, a student may test positive for drugs twice and still be allowed to participate in extracurricular activities. After the first positive test, the school contacts the student's parent or guardian for a meeting. The student may continue to participate in the activity if within five days of the meeting the student shows proof of receiving drug counseling and submits to a second drug test in two weeks. For the second positive test, the student is suspended from participation in <span class="star-pagination">*834</span> all extracurricular activities for 14 days, must complete four hours of substance abuse counseling, and must submit to monthly drug tests. Only after a third positive test will the student be suspended from participating in any extracurricular activity for the remainder of the school year, or 88 school days, whichever is longer. See App. 201-202.</p>
<p>Given the minimally intrusive nature of the sample collection and the limited uses to which the test results are put, we conclude that the invasion of students' privacy is not significant.</p>
<p></p>
<h2>C</h2>
<p>Finally, this Court must consider the nature and immediacy of the government's concerns and the efficacy of the Policy in meeting them. See <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 660</a></span>. This Court has already articulated in detail the importance of the governmental concern in preventing drug use by schoolchildren. See <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#661" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 661-662</a></span>. The drug abuse problem among our Nation's youth has hardly abated since <i>Vernonia</i> was decided in 1995. In fact, evidence suggests that it has only grown worse.<sup>[5]</sup> As in <i>Vernonia,</i> "the necessity for the State to act is magnified by the fact that this evil is being visited not just upon individuals at large, but upon children for whom it has undertaken a special responsibility of care and direction." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 662</a></span>. The health and safety risks identified in <i>Vernonia</i> apply with equal force to Tecumseh's children. Indeed, the nationwide drug epidemic makes the war against drugs a pressing concern in every school.</p>
<p>Additionally, the School District in this case has presented specific evidence of drug use at Tecumseh schools. Teachers testified that they had seen students who appeared to be <span class="star-pagination">*835</span> under the influence of drugs and that they had heard students speaking openly about using drugs. See, <i>e. g.,</i> App. 72 (deposition of Dean Rogers); <i>id.,</i> at 115 (deposition of Sheila Evans). A drug dog found marijuana cigarettes near the school parking lot. Police officers once found drugs or drug paraphernalia in a car driven by a Future Farmers of America member. And the school board president reported that people in the community were calling the board to discuss the "drug situation." See 115 F. Supp. 2d, at 1285 1286. We decline to second-guess the finding of the District Court that "[v]iewing the evidence as a whole, it cannot be reasonably disputed that the [School District] was faced with a `drug problem' when it adopted the Policy." <i>Id.,</i> at 1287.</p>
<p>Respondents consider the proffered evidence insufficient and argue that there is no "real and immediate interest" to justify a policy of drug testing nonathletes. Brief for Respondents 32. We have recognized, however, that "[a] demonstrated problem of drug abuse . . . [is] notin all cases necessary to the validity of a testing regime," but that some showing does "shore up an assertion of special need for a suspicionless general search program." <i>Chandler</i> v. <i>Miller,</i>  <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 319</a></span> (1997). The School District has provided sufficient evidence to shore up the need for its drug testing program.</p>
<p>Furthermore, this Court has not required a particularized or pervasive drug problem before allowing the government to conduct suspicionless drug testing. For instance, in <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> the Court upheld the drug testing of customs officials on a purely preventive basis, without any documented history of drug use by such officials. See 489 U. S., at 673. In response to the lack of evidence relating to drug use, the Court noted generally that "drug abuse is one of the most serious problems confronting our society today," and that programs to prevent and detect drug use among customs officials could not be deemed unreasonable. <i>Id.,</i> at 674; cf. <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 607</a></span>, and n. 1 (noting nationwide <span class="star-pagination">*836</span> studies that identified on-the-job alcohol and drug use by railroad employees). Likewise, the need to prevent and deter the substantial harm of childhood drug use provides the necessary immediacy for a school testing policy. Indeed, it would make little sense to require a school district to wait for a substantial portion of its students to begin using drugs before it was allowed to institute a drug testing program designed to deter drug use.</p>
<p>Given the nationwide epidemic of drug use, and the evidence of increased drug use in Tecumseh schools, it was entirely reasonable for the School District to enact this particular drug testing policy. We reject the Court of Appeals' novel test that "any district seeking to impose a random suspicionless drug testing policy as a condition to participation in a school activity must demonstrate that there is some identifiable drug abuse problem among a sufficient number of those subject to the testing, such that testing that group of students will actually redress its drug problem." 242 F. 3d, at 1278. Among other problems, it would be difficult to administer such a test. As we cannot articulate a threshold level of drug use that would suffice to justify a drug testing program for schoolchildren, we refuse to fashion what would in effect be a constitutional quantum of drug use necessary to show a "drug problem."</p>
<p>Respondents also argue that the testing of nonathletes does not implicate any safety concerns, and that safety is a "crucial factor" in applying the special needs framework. Brief for Respondents 25-27. They contend that there must be "surpassing safety interests," <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#634" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 634</a></span>, or "extraordinary safety and national security hazards," <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Von Raab, supra,</i> at 674</a></span>, in order to override the usual protections of the Fourth Amendment. See Brief for Respondents 25-26. Respondents are correct that safety factors into the special needs analysis, but the safety interest furthered by drug testing is undoubtedly substantial for all children, athletes and nonathletes alike. We know all too well that drug <span class="star-pagination">*837</span> use carries a variety of health risks for children, including death from overdose.</p>
<p>We also reject respondents' argument that drug testing must presumptively be based upon an individualized reasonable suspicion of wrongdoing because such a testing regime would be less intrusive. See <i>id.,</i> at 12-16. In this context, the Fourth Amendment does not require a finding of individualized suspicion, see <i>supra,</i> at 829, and we decline to impose such a requirement on schools attempting to prevent and detect drug use by students. Moreover, we question whether testing based on individualized suspicion in fact would be less intrusive. Such a regime would place an additional burden on public school teachers who are already tasked with the difficult job of maintaining order and discipline. A program of individualized suspicion might unfairly target members of unpopular groups. The fear of lawsuits resulting from such targeted searches may chill enforcement of the program, rendering it ineffective in combating drug use. See <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 663-664</a></span> (offering similar reasons for why "testing based on `suspicion' of drug use would not be better, but worse"). In any case, this Court has repeatedly stated that reasonableness under the Fourth Amendment does not require employing the least intrusive means, because "[t]he logic of such elaborate less-restrictivealternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers." <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-557, n. 12</a></span>; see also <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#624" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 624</a></span> ("[A] showing of individualized suspicion is not a constitutional floor, below which a search must be presumed unreasonable").</p>
<p>Finally, we find that testing students who participate in extracurricular activities is a reasonably effective means of addressing the School District's legitimate concerns in preventing, deterring, and detecting drug use. While in <i>Vernonia</i> there might have been a closer fit between the testing of athletes and the trial court's finding that the drug problem <span class="star-pagination">*838</span> was "fueled by the `role model' effect of athletes' drug use," such a finding was not essential to the holding. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 663</a></span>; cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#684" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>id.,</i> at 684-685</a></span> (O'Connor, J., dissenting) (questioning the extent of the drug problem, especially as applied to athletes). <i>Vernonia</i> did not require the school to test the group of students most likely to use drugs, but rather considered the constitutionality of the program in the context of the public school's custodial responsibilities. Evaluating the Policy in this context, we conclude that the drug testing of Tecumseh students who participate in extracurricular activities effectively serves the School District's interest in protecting the safety and health of its students.</p>
<p></p>
<h2>III</h2>
<p>Within the limits of the Fourth Amendment, local school boards must assess the desirability of drug testing schoolchildren. In upholding the constitutionality of the Policy, we express no opinion as to its wisdom. Rather, we hold only that Tecumseh's Policy is a reasonable means of furthering the School District's important interest in preventing and deterring drug use among its schoolchildren. Accordingly, we reverse the judgment of the Court of Appeals.</p>
<blockquote>
<i>It is so ordered.</i>  Justice Breyer, concurring. I agree with the Court that <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), governs this case and requires reversal of the Tenth Circuit's decision. The school's drug testing program addresses a serious national problem by focusing upon demand, avoiding the use of criminal or disciplinary sanctions, and relying upon professional counseling and treatment. See App. 201-202. In my view, this program does not violate the Fourth Amendment's prohibition of "unreasonable searches and seizures." I reach this conclusion primarily for the reasons given by the Court, but I would <span class="star-pagination">*839</span> emphasize several underlying considerations, which I understand to be consistent with the Court's opinion.</blockquote>
<p></p>
<h2>I</h2>
<p>In respect to the school's need for the drug testing program, I would emphasize the following: First, the drug problem in our Nation's schools is serious in terms of size, the kinds of drugs being used, and the consequences of that use both for our children and the rest of us. See, <i>e. g.,</i> White House Nat. Drug Control Strategy 25 (Feb. 2002) (drug abuse leads annually to about 20,000 deaths, $160 billion in economic costs); Department of Health and Human Services, L. Johnston et al., Monitoring the Future: National Results on Adolescent Drug Use, Overview of Key Findings 5 (2001) (Monitoring the Future) (more than one-third of all students have used illegal drugs before completing the eighth grade; more than half before completing high school); <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">ibid.</a></span></i> (about 30% of all students use drugs <i>other than marijuana</i> prior to completing high school (emphasis added)); National Center on Addiction and Substance Abuse, Malignant Neglect: Substance Abuse and America's Schools 15 (Sept. 2001) (Malignant Neglect) (early use leads to later drug dependence); Nat. Drug Control Strategy, <i>supra,</i> at 1 (same).</p>
<p>Second, the government's emphasis upon supply side interdiction apparently has not reduced teenage use in recent years. Compare R. Perl, CRS Issue Brief for Congress, Drug Control: International Policy and Options CRS-1 (Dec. 12, 2001) (supply side programs account for 66% of the federal drug control budget), with Partnership for a Drug-Free America, 2001 Partnership Attitude Tracking Study: Key Findings 1 (showing increase in teenage drug use in early 1990's, peak in 1997, holding steady thereafter); 2000-2001 PRIDE National Summary: Alcohol, Tobacco, Illicit Drugs, Violence and Related Behaviors, Grades 6 thru 12 (Jul. 16, 2002), http://www.pridesurveys.com/main/supportfiles/ natsum00.pdf, p. 15 (slight rise in high school drug use in <span class="star-pagination">*840</span> 2000-2001); Monitoring the Future, Table 1 (lifetime prevalence of drug use increasing over last 10 years).</p>
<p>Third, public school systems must find effective ways to deal with this problem. Today's public expects its schools not simply to teach the fundamentals, but "to shoulder the burden of feeding students breakfast and lunch, offering before and after school child care services, and providing medical and psychological services," all in a school environment that is safe and encourages learning. Brief for National School Boards Association et al. as <i>Amici Curiae</i> 3-4. See also <i>Bethel School Dist. No. 403</i> v. <i>Fraser,</i> <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#681" aria-description="Citation for case: Bethel School District No. 403 v. Fraser">478 U. S. 675, 681</a></span> (1986) (Schools "`prepare pupils for citizenship in the Republic [and] inculcate the habits and manners of civility as values in themselves conductive to happiness and as indispensable to the practice of self-government in the community and the nation' ") (quoting C. Beard &amp; M. Beard, New Basic History of the United States 228 (1968)). The law itself recognizes these responsibilities with the phrase <i>in loco parentis</i> a phrase that draws its legal force primarily from the needs of younger students (who here are necessarily grouped together with older high school students) and which reflects, not that a child or adolescent lacks an interest in privacy, but that a child's or adolescent's school-related privacy interest, when compared to the privacy interests of an adult, has different dimensions. Cf. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Vernonia, supra,</i> at 654-655</a></span>. A public school system that fails adequately to carry out its responsibilities may well see parents send their children to private or parochial school insteadwith help from the State. See <i>Zelman</i> v. <i>Simmons-Harris, ante,</i> p. 639.</p>
<p>Fourth, the program at issue here seeks to discourage demand for drugs by changing the school's environment in order to combat the single most important factor leading schoolchildren to take drugs, namely, peer pressure. Malignant Neglect 4 (students "whose friends use illicit drugs are more than 10 times likelier to use illicit drugs than those whose friends do not"). It offers the adolescent a nonthreatening <span class="star-pagination">*841</span> reason to decline his friend's drug-use invitations, namely, that he intends to play baseball, participate in debate, join the band, or engage in any one of half a dozen useful, interesting, and important activities.</p>
<p></p>
<h2>II</h2>
<p>In respect to the privacy-related burden that the drug testing program imposes upon students, I would emphasize the following: First, not everyone would agree with this Court's characterization of the privacy-related significance of urine sampling as "`negligible.' " <i>Ante,</i> at 833 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>). Some find the procedure no more intrusive than a routine medical examination, but others are seriously embarrassed by the need to provide a urine sample with someone listening "outside the closed restroom stall," <i>ante,</i> at 832. When trying to resolve this kind of close question involving the interpretation of constitutional values, I believe it important that the school board provided an opportunity for the airing of these differences at public meetings designed to give the entire community "the opportunity to be able to participate" in developing the drug policy. App. 87. The board used this democratic, participatory process to uncover and to resolve differences, giving weight to the fact that the process, in this instance, revealed little, if any, objection to the proposed testing program.</p>
<p>Second, the testing program avoids subjecting the entire school to testing. And it preserves an option for a conscientious objector. He can refuse testing while paying a price (nonparticipation) that is serious, but less severe than expulsion from the school.</p>
<p>Third, a contrary reading of the Constitution, as requiring "individualized suspicion" in this public school context, could well lead schools to push the boundaries of "individualized suspicion" to its outer limits, using subjective criteria that may "unfairly target members of unpopular groups," <i>ante,</i>  at 837, or leave those whose behavior is slightly abnormal <span class="star-pagination">*842</span> stigmatized in the minds of others. See Belsky, Random vs. Suspicion-Based Drug Testing in the Public SchoolsA Surprising Civil Liberties Dilemma, <span class="citation no-link">27 Okla. City U. L. Rev. 1</span>, 20-21 (forthcoming 2002) (listing court-approved factors justifying suspicion-based drug testing, including tiredness, overactivity, quietness, boisterousness, sloppiness, excessive meticulousness, and tardiness). If so, direct application of the Fourth Amendment's prohibition against "unreasonable searches and seizures" will further that Amendment's liberty-protecting objectives at least to the same extent as application of the mediating "individualized suspicion" test, where, as here, the testing program is neither criminal nor disciplinary in nature.</p>
<p></p>
<h2>* * *</h2>
<p>I cannot know whether the school's drug testing program will work. But, in my view, the Constitution does not prohibit the effort. Emphasizing the considerations I have mentioned, along with others to which the Court refers, I conclude that the school's drug testing program, constitutionally speaking, is not "unreasonable." And I join the Court's opinion.</p>
<p>Justice O'Connor, with whom Justice Souter joins, dissenting.</p>
<p>I dissented in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), and continue to believe that case was wrongly decided. Because <i>Vernonia</i> is now this Court's precedent, and because I agree that petitioners' program fails even under the balancing approach adopted in that case, I join Justice Ginsburg's dissent.</p>
<p>Justice Ginsburg, with whom Justice Stevens, Justice O'Connor, and Justice Souter join, dissenting.</p>
<p>Seven years ago, in <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), this Court determined that a school <span class="star-pagination">*843</span> district's policy of randomly testing the urine of its student athletes for illicit drugs did not violate the Fourth Amendment. In so ruling, the Court emphasized that drug use "increase[d] the risk of sports-related injury" and that Vernonia's athletes were the "leaders" of an aggressive local "drug culture" that had reached "`epidemic proportions.' " <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 649</a></span>. Today, the Court relies upon <i>Vernonia</i> to permit a school district with a drug problem its superintendent repeatedly described as "not . . . major," see App. 180, 186, 191, to test the urine of an academic team member solely by reason of her participation in a nonathletic, competitive extracurricular activityparticipation associated with neither special dangers from, nor particular predilections for, drug use.</p>
<p>"[T]he legality of a search of a student," this Court has instructed, "should depend simply on the reasonableness, under all the circumstances, of the search." <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 341</a></span> (1985). Although "`special needs' inhere in the public school context," see <i>ante,</i> at 829 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span>), those needs are not so expansive or malleable as to render reasonable any program of student drug testing a school district elects to install. The particular testing program upheld today is not reasonable; it is capricious, even perverse: Petitioners' policy targets for testing a student population least likely to be at risk from illicit drugs and their damaging effects. I therefore dissent.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>A search unsupported by probable cause nevertheless may be consistent with the Fourth Amendment "when special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable." <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987) (internal quotation marks omitted). In <i>Vernonia,</i> this Court made clear that "such `special needs' .. . exist in the public school context." <span class="star-pagination">*844</span> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span> (quoting <i>Griffin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 873</a></span>). The Court observed:</p>
<blockquote>"[W]hile children assuredly do not `shed their constitutional rights . . . at the schoolhouse gate,' <i>Tinker</i> v. <i>Des</i>  <i>Moines Independent Community School Dist.,</i> <span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), the nature of those rights is what is appropriate for children in school. . . . Fourth Amendment rights, no less than First and Fourteenth Amendment rights, are different in public schools than elsewhere; the `reasonableness' inquiry cannot disregard the schools' custodial and tutelary responsibility for children." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#655" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 655-656</a></span> (other citations omitted). The <i>Vernonia</i> Court concluded that a public school district facing a disruptive and explosive drug abuse problem sparked by members of its athletic teams had "special needs" that justified suspicionless testing of district athletes as a condition of their athletic participation.</blockquote>
<p>This case presents circumstances dispositively different from those of <i>Vernonia.</i> True, as the Court stresses, Tecumseh students participating in competitive extracurricular activities other than athletics share two relevant characteristics with the athletes of <i>Vernonia.</i> First, both groups attend public schools. "[O]ur decision in <i>Vernonia,</i> " the Court states, "depended primarily upon the school's custodial responsibility and authority." <i>Ante,</i> at 831; see also <i>ante,</i>  at 840 (Breyer, J., concurring) (school districts act <i>in loco parentis</i> ). Concern for student health and safety is basic to the school's caretaking, and it is undeniable that "drug use carries a variety of health risks for children, including death from overdose." <i>Ante,</i> at 836-837 (majority opinion).</p>
<p>Those risks, however, are present for <i>all</i> schoolchildren. <i>Vernonia</i> cannot be read to endorse invasive and suspicionless drug testing of all students upon any evidence of drug use, solely because drugs jeopardize the life and health of those who use them. Many children, like many adults, engage <span class="star-pagination">*845</span> in dangerous activities on their own time; that the children are enrolled in school scarcely allows government to monitor all such activities. If a student has a reasonable subjective expectation of privacy in the personal items she brings to school, see <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#338" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 338-339</a></span>, surely she has a similar expectation regarding the chemical composition of her urine. Had the <i>Vernonia</i> Court agreed that public school attendance, in and of itself, permitted the State to test each student's blood or urine for drugs, the opinion in <i>Vernonia</i> could have saved many words. See, <i>e. g.,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span> ("[I]t must not be lost sight of that [the Vernonia School District] program is directed . . . to drug use by school athletes, where the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high.").</p>
<p>The second commonality to which the Court points is the voluntary character of both interscholastic athletics and other competitive extracurricular activities. "By choosing to `go out for the team,' [school athletes] voluntarily subject themselves to a degree of regulation even higher than that imposed on students generally." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 657</a></span>. Comparably, the Court today observes, "students who participate in competitive extracurricular activities voluntarily subject themselves to" additional rules not applicable to other students. <i>Ante,</i> at 831.</p>
<p>The comparison is enlightening. While extracurricular activities are "voluntary" in the sense that they are not required for graduation, they are part of the school's educational program; for that reason, the petitioner (hereinafter School District) is justified in expending public resources to make them available. Participation in such activities is a key component of school life, essential in reality for students applying to college, and, for all participants, a significant contributor to the breadth and quality of the educational experience. See Brief for Respondents 6; Brief for American Academy of Pediatrics et al. as <i>Amici Curiae</i> 8-9. Students <span class="star-pagination">*846</span> "volunteer" for extracurricular pursuits in the same way they might volunteer for honors classes: They subject themselves to additional requirements, but they do so in order to take full advantage of the education offered them. Cf. <i>Lee</i>  v. <i>Weisman,</i> <span class="citation" data-id="9432656"><a href="/opinion/112779/lee-v-weisman/#595" aria-description="Citation for case: Lee v. Weisman">505 U. S. 577, 595</a></span> (1992) ("Attendance may not be required by official decree, yet it is apparent that a student is not free to absent herself from the graduation exercise in any real sense of the term `voluntary,' for absence would require forfeiture of those intangible benefits which have motivated the student through youth and all her high school years.").</p>
<p>Voluntary participation in athletics has a distinctly different dimension: Schools regulate student athletes discretely because competitive school sports by their nature require communal undress and, more important, expose students to physical risks that schools have a duty to mitigate. For the very reason that schools cannot offer a program of competitive athletics without intimately affecting the privacy of students, <i>Vernonia</i> reasonably analogized school athletes to "adults who choose to participate in a closely regulated industry." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 657</a></span> (internal quotation marks omitted). Industries fall within the closely regulated category when the nature of their activities requires substantial government oversight. See, <i>e. g., </i><i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 315-316</a></span> (1972). Interscholastic athletics similarly require close safety and health regulation; a school's choir, band, and academic team do not.</p>
<p>In short, <i>Vernonia</i> applied, it did not repudiate, the principle that "the legality of a search of a student should depend simply on the reasonableness, <i>under all the circumstances,</i>  of the search." <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341</a></span> (emphasis added). Enrollment in a public school, and election to participate in school activities beyond the bare minimum that the curriculum requires, are indeed factors relevant to reasonableness, but they do not on their own justify intrusive, suspicionless searches. <i>Vernonia,</i> accordingly, did not rest upon these <span class="star-pagination">*847</span> factors; instead, the Court performed what today's majority aptly describes as a "fact-specific balancing," <i>ante,</i> at 830. Balancing of that order, applied to the facts now before the Court, should yield a result other than the one the Court announces today.</p>
<p></p>
<h2>B</h2>
<p><i>Vernonia</i> initially considered "the nature of the privacy interest upon which the search [there] at issue intrude[d]." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 654</a></span>. The Court emphasized that student athletes' expectations of privacy are necessarily attenuated:</p>
<blockquote>"Legitimate privacy expectations are even less with regard to student athletes. School sports are not for the bashful. They require `suiting up' before each practice or event, and showering and changing afterwards. Public school locker rooms, the usual sites for these activities, are not notable for the privacy they afford. The locker rooms in Vernonia are typical: No individual dressing rooms are provided; shower heads are lined up along a wall, unseparated by any sort of partition or curtain; not even all the toilet stalls have doors. . . . [T]here is an element of communal undress inherent in athletic participation." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 657</a></span> (internal quotation marks omitted). Competitive extracurricular activities other than athletics, however, serve students of all manner: the modest and shy along with the bold and uninhibited. Activities of the kind plaintiff-respondent Lindsay Earls pursuedchoir, show choir, marching band, and academic teamafford opportunities to gain self-assurance, to "come to know faculty members in a less formal setting than the typical classroom," and to acquire "positive social supports and networks [that] play a critical role in periods of heightened stress." Brief for American Academy of Pediatrics et al. as <i>Amici Curiae</i> 13.</blockquote>
<p>On "occasional out-of-town trips," students like Lindsay Earls "must sleep together in communal settings and use <span class="star-pagination">*848</span> communal bathrooms." <span class="citation multiple-matches"><a href="/c/F.%203d/242/1264/">242 F. 3d 1264</a></span>, 1275 (CA10 2001). But those situations are hardly equivalent to the routine communal undress associated with athletics; the School District itself admits that when such trips occur, "public-like restroom facilities," which presumably include enclosed stalls, are ordinarily available for changing, and that "more modest students" find other ways to maintain their privacy. Brief for Petitioners 34.<sup>[1]</sup></p>
<p>After describing school athletes' reduced expectation of privacy, the <i>Vernonia</i> Court turned to "the character of the intrusion . . . complained of." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>. Observing that students produce urine samples in a bathroom stall with a coach or teacher outside, <i>Vernonia</i> typed the privacy interests compromised by the process of obtaining samples "negligible." <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">Ibid.</a></span></i> As to the required pretest disclosure of prescription medications taken, the Court assumed that "the School District would have permitted [a student] to provide the requested information in a confidential mannerfor example, in a sealed envelope delivered to the testing lab." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 660</a></span>. On that assumption, the Court concluded that Vernonia's athletes faced no significant invasion of privacy.</p>
<p>In this case, however, Lindsay Earls and her parents allege that the School District handled personal information collected under the policy carelessly, with little regard for its confidentiality. Information about students' prescription drug use, they assert, was routinely viewed by Lindsay's choir teacher, who left files containing the information unlocked and unsealed, where others, including students, could see them; and test results were given out to all activity sponsors whether or not they had a clear "need to know." See <span class="star-pagination">*849</span> Brief for Respondents 6, 24; App. 105-106, 131. But see <i>id.,</i>  at 199 (policy requires that "[t]he medication list shall be submitted to the lab in a sealed and confidential envelope and shall not be viewed by district employees").</p>
<p>In granting summary judgment to the School District, the District Court observed that the District's "[p]olicy expressly provides for confidentiality of test results, and the Court must assume that the confidentiality provisions will be honored." <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/#1293" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1293</a></span> (WD Okla. 2000). The assumption is unwarranted. Unlike <i>Vernonia,</i> where the District Court held a bench trial before ruling in the School District's favor, this case was decided by the District Court on summary judgment. At that stage, doubtful matters should not have been resolved in favor of the judgment seeker. See <i>United States</i> v. <i>Diebold, Inc.,</i> <span class="citation" data-id="106395"><a href="/opinion/106395/united-states-v-diebold-inc/#655" aria-description="Citation for case: United States v. Diebold, Inc.">369 U. S. 654, 655</a></span> (1962) <i>(per curiam)</i> ("On summary judgment the inferences to be drawn from the underlying facts contained in [affidavits, attached exhibits, and depositions] must be viewed in the light most favorable to the party opposing the motion."); see also 10A C. Wright, A. Miller, &amp; M. Kane, Federal Practice and Procedure § 2716, pp. 274-277 (3d ed. 1998).</p>
<p>Finally, the "nature and immediacy of the governmental concern," <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#660" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 660</a></span>, faced by the Vernonia School District dwarfed that confronting Tecumseh administrators. Vernonia initiated its drug testing policy in response to an alarming situation: "[A] large segment of the student body, particularly those involved in interscholastic athletics, was in a state of rebellion . . . fueled by alcohol and drug abuse as well as the student[s'] misperceptions about the drug culture." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 649</a></span> (internal quotation marks omitted). Tecumseh, by contrast, repeatedly reported to the Federal Government during the period leading up to the adoption of the policy that "types of drugs [other than alcohol and tobacco] including controlled dangerous substances, are present [in the schools] but have not identified themselves as major problems at this time." 1998-1999 Tecumseh <span class="star-pagination">*850</span> School's Application for Funds under the Safe and DrugFree Schools and Communities Program, reprinted at App. 191; accord, 1996-1997 Application, reprinted at App. 186; 1995-1996 Application, reprinted at App. 180.<sup>[2]</sup> As the Tenth Circuit observed, "without a demonstrated drug abuse problem among the group being tested, the efficacy of the District's solution to its perceived problem is . . . greatly diminished." 242 F. 3d, at 1277.</p>
<p>The School District cites <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 673-674</a></span> (1989), in which this Court permitted random drug testing of customs agents absent "any perceived drug problem among Customs employees," given that "drug abuse is one of the most serious problems confronting our society today." See also <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 607</a></span>, and n. 1 (1989) (upholding random drug and alcohol testing of railway employees based upon industry-wide, rather than railwayspecific, evidence of drug and alcohol problems). The tests in <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> and <i>Railway Labor Executives,</i> however, were installed to avoid enormous risks to the lives and limbs of others, not dominantly in response to the health risks to users invariably present in any case of drug use. See <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#674" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 674</a></span> (drug use by customs agents involved in drug interdiction creates "extraordinary safety and national security hazards"); <i>Railway Labor Executives,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 628</a></span> (railway operators "discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences"); see <span class="star-pagination">*851</span> also <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#321" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 321</a></span> (1997) ("<i>Von Raab</i>  must be read in its unique context").</p>
<p>Not only did the Vernonia and Tecumseh districts confront drug problems of distinctly different magnitudes, they also chose different solutions: Vernonia limited its policy to athletes; Tecumseh indiscriminately subjected to testing all participants in competitive extracurricular activities. Urging that "the safety interest furthered by drug testing is undoubtedly substantial for all children, athletes and nonathletes alike," <i>ante,</i> at 836, the Court cuts out an element essential to the <i>Vernonia</i> judgment. Citing medical literature on the effects of combining illicit drug use with physical exertion, the <i>Vernonia</i> Court emphasized that "the particular drugs screened by [Vernonia's] Policy have been demonstrated to pose substantial physical risks to athletes." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#662" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 662</a></span>; see also <i><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">id.</a></span></i> , at 666 (Ginsburg, J., concurring) (<i>Vernonia</i> limited to "those seeking to engage with others in team sports"). We have since confirmed that these special risks were necessary to our decision in <i>Vernonia.</i> See <i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#317" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 317</a></span> (<i>Vernonia</i> "emphasized the importance of deterring drug use by schoolchildren and the risk of injury a drug-using student athlete cast on himself and those engaged with him on the playing field"); see also <i>Ferguson</i> v. <i>Charleston,</i> <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/#87" aria-description="Citation for case: Ferguson v. City of Charleston">532 U. S. 67, 87</a></span> (2001) (Kennedy, J., concurring) (Vernonia's policy had goal of "`[d]eterring drug use by our Nation's schoolchildren,' and particularly by student-athletes, because `the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high' ") (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#661" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 661-662</a></span>).</p>
<p>At the margins, of course, no policy of <i>random</i> drug testing is perfectly tailored to the harms it seeks to address. The School District cites the dangers faced by members of the band, who must "perform extremely precise routines with heavy equipment and instruments in close proximity to other students," and by Future Farmers of America, who <span class="star-pagination">*852</span> "are required to individually control and restrain animals as large as 1500 pounds." Brief for Petitioners 43. For its part, the United States acknowledges that "the linebacker faces a greater risk of serious injury if he takes the field under the influence of drugs than the drummer in the halftime band," but parries that "the risk of injury to a student who is under the influence of drugs while playing golf, cross country, or volleyball (sports covered by the policy in <i>Vernonia</i> ) is scarcely any greater than the risk of injury to a student . . . handling a 1500-pound steer (as [Future Farmers of America] members do) or working with cutlery or other sharp instruments (as [Future Homemakers of America] members do)." Brief for United States as <i>Amicus Curiae</i>  18. One can demur to the Government's view of the risks drug use poses to golfers, cf. <i>PGA TOUR, Inc.</i> v. <i>Martin,</i>  <span class="citation" data-id="9434091"><a href="/opinion/118432/pga-tour-inc-v-martin/#687" aria-description="Citation for case: PGA Tour, Inc. v. Martin">532 U. S. 661, 687</a></span> (2001) ("golf is a low intensity activity"), for golfers were surely as marginal among the linebackers, sprinters, and basketball players targeted for testing in Vernonia as steer-handlers are among the choristers, musicians, and academic-team members subject to urinalysis in Tecumseh.<sup>[3]</sup> Notwithstanding nightmarish images of out-of-control flatware, livestock run amok, and colliding tubas disturbing the peace and quiet of Tecumseh, the great majority of students the School District seeks to test in truth are engaged in activities that are not safety sensitive to an unusual degree. There is a difference between imperfect tailoring and no tailoring at all.</p>
<p>The Vernonia district, in sum, had two good reasons for testing athletes: Sports team members faced special health risks and they "were the leaders of the drug culture." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#649" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 649</a></span>. No similar reason, and no other tenable justification, explains Tecumseh's decision to target <span class="star-pagination">*853</span> for testing all participants in every competitive extracurricular activity. See <i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 319</a></span> (drug testing candidates for office held incompatible with Fourth Amendment because program was "not well designed to identify candidates who violate antidrug laws").</p>
<p>Nationwide, students who participate in extracurricular activities are significantly less likely to develop substance abuse problems than are their less-involved peers. See, <i>e. g.,</i>  N. Zill, C. Nord, &amp; L. Loomis, Adolescent Time Use, Risky Behavior, and Outcomes 52 (1995) (tenth graders "who reported spending no time in school-sponsored activities were . . . 49 percent more likely to have used drugs" than those who spent 1-4 hours per week in such activities). Even if students might be deterred from drug use in order to preserve their extracurricular eligibility, it is at least as likely that other students might forgo their extracurricular involvement in order to avoid detection of their drug use. Tecumseh's policy thus falls short doubly if deterrence is its aim: It invades the privacy of students who need deterrence least, and risks steering students at greatest risk for substance abuse away from extracurricular involvement that potentially may palliate drug problems.<sup>[4]</sup></p>
<p>To summarize, this case resembles <i>Vernonia</i> only in that the School Districts in both cases conditioned engagement in activities outside the obligatory curriculum on random subjection to urinalysis. The defining characteristics of the two programs, however, are entirely dissimilar. The Vernonia district sought to test a subpopulation of students distinguished by their reduced expectation of privacy, their special <span class="star-pagination">*854</span> susceptibility to drug-related injury, and their heavy involvement with drug use. The Tecumseh district seeks to test a much larger population associated with none of these factors. It does so, moreover, without carefully safeguarding student confidentiality and without regard to the program's untoward effects. A program so sweeping is not sheltered by <i>Vernonia;</i> its unreasonable reach renders it impermissible under the Fourth Amendment.</p>
<p></p>
<h2>II</h2>
<p>In <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span>,</i> this Court inspected "Georgia's requirement that candidates for state office pass a drug test"; we held that the requirement "d[id] not fit within the closely guarded category of constitutionally permissible suspicionless searches." <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#309" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 309</a></span>. Georgia's testing prescription, the record showed, responded to no "concrete danger," <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#319" aria-description="Citation for case: Chandler v. Miller"><i>id.,</i> at 319</a></span>, was supported by no evidence of a particular problem, and targeted a group not involved in "high-risk, safety-sensitive tasks," <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#321" aria-description="Citation for case: Chandler v. Miller"><i>id.,</i> at 321-322</a></span>. We concluded:</p>
<blockquote>"What is left, after close review of Georgia's scheme, is the image the State seeks to project. By requiring candidates for public office to submit to drug testing, Georgia displays its commitment to the struggle against drug abuse. . . . The need revealed, in short, is symbolic, not `special,' as that term draws meaning from our case law." <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Ibid.</a></span></i>  Close review of Tecumseh's policy compels a similar conclusion. That policy was not shown to advance the "`special needs' [existing] in the public school context [to maintain] . . . swift and informal disciplinary procedures . . . [and] order in the schools," <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 653</a></span> (internal quotation marks omitted). See <i>supra,</i> at 846-848, 849 853. What is left is the School District's undoubted purpose to heighten awareness of its abhorrence of, and strong stand against, drug abuse. But the desire to augment communication <span class="star-pagination">*855</span> of this message does not trump the right of persons even of children within the schoolhouse gateto be "secure in their persons . . . against unreasonable searches and seizures." U. S. Const., Amdt. 4.</blockquote>
<p>In <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span>,</i> the Court referred to a pathmarking dissenting opinion in which "Justice Brandeis recognized the importance of teaching by example: `Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example.' " <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 322</a></span> (quoting <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928)). That wisdom should guide decisionmakers in the instant case: The government is nowhere more a teacher than when it runs a public school.</p>
<p>It is a sad irony that the petitioning School District seeks to justify its edict here by trumpeting "the schools' custodial and tutelary responsibility for children." <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#656" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 656</a></span>. In regulating an athletic program or endeavoring to combat an exploding drug epidemic, a school's custodial obligations may permit searches that would otherwise unacceptably abridge students' rights. When custodial duties are not ascendant, however, schools' tutelary obligations to their students require them to "teach by example" by avoiding symbolic measures that diminish constitutional protections. "That [schools] are educating the young for citizenship is reason for scrupulous protection of Constitutional freedoms of the individual, if we are not to strangle the free mind at its source and teach youth to discount important principles of our government as mere platitudes." <i>West Virginia Bd. of Ed.</i> v. <i>Barnette,</i> <span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/#637" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U. S. 624, 637</a></span> (1943).</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, I would affirm the judgment of the Tenth Circuit declaring the testing policy at issue unconstitutional.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for the Washington Legal Foundation et al. by <i>Richard Willard, Daniel J. Popeo,</i> and <i>Richard A. Samp.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Academy of Pediatrics et al. by <i>David T. Goldberg</i> and <i>Daniel N. Abrahamson;</i> for Jean Burkett et al. by <i>Craig Goldblatt;</i> for the Juvenile Law Center et al. by <i>Marsha L. Levick;</i> for the National Association of Criminal Defense Lawyers et al. by <i>John Wesley Hall, Jr., Lisa B. Kemler, Timothy Lynch,</i> and <i>Kevin B. Zeese;</i> and for the Rutherford Institute by <i>John W. Whitehead, Steven H. Aden,</i> and <i>Jamin B. Raskin.</i> </p>
<p>Briefs of <i>amici curiae</i> were filed for the Drug-Free Schools Coalition et al. by <i>David G. Evans;</i> for the National School Boards Association et al. by <i>Julie K. Underwood, Christopher B. Gilbert,</i> and <i>Thomas E. Wheeler;</i>  and for Professor Akhil Reed Amar et al. by <i>Julia M. Carpenter.</i> </p>
<p>[1]  The District Court noted that the School District's allegations concerning Daniel James called his standing to sue into question because his failing grades made him ineligible to participate in any interscholastic competition.See <span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">115 F. Supp. 2d 1281, 1282, n. 1</a></span> (WD Okla. 2000).The court noted,however, that the disputeneed not be resolved because Lindsay Earls had standing, and therefore the court was required to address the constitution a lity of the drug testing policy. See <i><span class="citation" data-id="2580272"><a href="/opinion/2580272/earls-ex-rel-earls-v-board-of-education-of-tecumseh-public-school/" aria-description="Citation for case: Earls Ex Rel. Earls v. Board of Education of Tecumseh...">ibid.</a></span></i> Because we are likewise satisfied that Earls has standing, we need not address whether James also has standing.</p>
<p>[2]  The respondents did not challenge the Policy either as it applies to athletes or as it provides for drug testing upon reasonable, individualized suspicion. See App. 28.</p>
<p>[3]  Justice Ginsburg argues that <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), depended on the fact that the drug testing program applied only to student athletes. But even the passage cited by the dissent manifests the supplemental nature of this factor, as the Court in <i>Vernonia</i> stated that "[l]egitimate privacy expectations are <i>even less</i> with regard to student athletes." See <i>post,</i> at 847 (quoting <i>Vernonia,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#657" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 657</a></span>) (emphasis added). In upholding the drug testing program in <i>Vernonia,</i> we considered the school context "[c]entral" and "[t]he most significant element." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#654" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 654, 665</a></span>. This hefty weight on the side of the school's balance applies with similar force in this case even though we undertake a separate balancing with regard to this particular program.</p>
<p>[4]  Justice Ginsburg's observations with regard to extracurricular activities apply with equal force to athletics. See <i>post,</i> at 845 ("Participation in such [extracurricular] activities is a key component of school life, essential in reality for students applying to college, and, for all participants, a significant contributor to the breadth and quality of the educational experience").</p>
<p>[5]  For instance, the number of 12th graders using any illicitdrug increased from 48.4 percent in 1995 to 53.9 percent in 2001. The number of 12th graders reporting they had used marijuana jumped from 41.7 percent to 49.0 percent during that same period. See Department of Health and Human Services, Monitoring the Future: National Results on Adolescent Drug Use, Overview of Key Findings (2001) (Table 1).</p>
<p>[1]  According to Tecumseh's choir teacher, choir participants who chose not to wear their choir uniforms to school on the days of competitions could change either in "a rest room in a building" or on the bus, where "[m]any of them have figured out how to [change] without having [anyone] . . . see anything." 2 Appellants' App. in No. 00-6128 (CA10), p. 296.</p>
<p>[2]  The Court finds it sufficient that there be evidence of <i>some</i> drug use in Tecumseh's schools: "As we cannot articulate a threshold level of drug use that would suffice to justify a drug testing program for schoolchildren, we refuse to fashion what would in effect be a constitutional quantum of drug use necessary to show a `drug problem.' " <i>Ante,</i> at 836. One need not establish a bright-line "constitutional quantum of drug use" to recognize the relevance of the superintendent's reports characterizing drug use among Tecumseh's students as "not . . . [a] major proble[m]," App. 180, 186, 191.</p>
<p>[3]  Cross-country runners and volleyball players, by contrast, engage in substantial physical exertion. See <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#663" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 663</a></span> (1995) (describing special dangers of combining drug use with athletics generally).</p>
<p>[4]  The Court notes that programs of individualized suspicion, unlike those using random testing, "might unfairly target members of unpopular groups." <i>Ante,</i> at 837; see also <i>ante,</i> at 841-842 (Breyer, J., concurring). Assuming, <i>arguendo,</i> that this is so, the School District here has not exchanged individualized suspicion for random testing. It has installed random testing in addition to, rather than in lieu of, testing "at any time when there is reasonable suspicion." App. 197.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Bobby v. Dixon.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Bobby v. Dixon"
type: case
citation: "565 U.S. 23 (2011)"
parallel_cite: "132 S. Ct. 26; 181 L. Ed. 2d 328"
neutral_cite: 2011 U.S. LEXIS 7926
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-11-07
docket: 10-1540
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-11-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bobby v. Dixon
  varies_by_point: false
  scope_note: "Per curiam AEDPA reversal; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/616807/bobby-v-dixon/"
  cluster_id: 616807
  opinion_id: 616807
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Related"
related: ["[[Oregon v. Elstad]]", "[[Missouri v. Seibert]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "elstad", "seibert", "aedpa"]
holding: "A later Mirandized confession is admissible under Elstad — and Seibert's question-first bar does not apply — where there was no deliberate two-step strategy and no nexus between the earlier unwarned statement and the later warned confession; the Sixth Circuit's contrary habeas grant unreasonably applied clearly established law."
lake:
  record_id: Bobby v. Dixon
  status: verified
  projected_at: 2026-07-06
---

# Bobby v. Dixon

*565 U.S. 23 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dixon was suspected in the disappearance and murder of Christopher Hammer. In a first, unwarned interrogation about a forgery, Dixon denied any involvement in Hammer's disappearance. Hours later, after learning an accomplice was talking, Dixon told police he wanted to tell them what happened, received [[Miranda and Custodial Interrogation|Miranda warnings]], waived, and confessed to the murder. The Ohio courts admitted the confession. The Sixth Circuit granted federal [[Common Legal Terms#habeas-corpus|habeas]] relief, holding the confession barred by a deliberate "question-first, warn-later" strategy under *[[Missouri v. Seibert]]*.

## Issue
Whether, on AEDPA review, the state court unreasonably applied clearly established federal law in admitting Dixon's warned murder confession given his earlier unwarned interrogation about a related forgery.

## Rule
No — admission was reasonable; *[[Missouri v. Seibert|Seibert]]*'s concern was absent and *[[Oregon v. Elstad|Elstad]]* governs. "[U]nlike in *Seibert*, there is no concern here that police gave Dixon *Miranda* warnings and then led him to repeat an earlier murder confession, because there was no earlier confession to repeat." — 565 U.S. at 31. ^pin-31

There was "simply 'no nexus' between Dixon's unwarned admission to forgery and his later, warned confession to murder," and a four-hour break separated the two interrogations, so the warned confession was not the tainted product of the earlier questioning. — *Id.* ^pin-31a

Under *[[Oregon v. Elstad]]*, where the earlier *[[Miranda v. Arizona|Miranda]]* lapse "involved no actual compulsion," a subsequent properly warned and voluntary confession is admissible.

## Application
Dixon's first interrogation produced only denials, not a confession to repeat, and he himself initiated the second session by declaring he wanted to tell police what happened — so police did not use the unwarned statement to soften him up. The two-step *[[Missouri v. Seibert|Seibert]]* dynamic (a single "continuum" that drained the midstream warnings of meaning) was therefore not present, and the Ohio Supreme Court reasonably found the warned murder confession admissible. The Sixth Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] was an unreasonable application of clearly established law.

## Conclusion
The state court's admission of the confession was not contrary to, or an unreasonable application of, *[[Miranda v. Arizona|Miranda]]*, *[[Oregon v. Elstad|Elstad]]*, or *[[Missouri v. Seibert|Seibert]]*. The Sixth Circuit was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Bobby v. Dixon* marks the line between [[Oregon v. Elstad]] (a good-faith *[[Miranda v. Arizona|Miranda]]* lapse does not taint a later warned confession) and [[Missouri v. Seibert]] (a deliberate question-first strategy does): absent a deliberate two-step and a nexus, *[[Oregon v. Elstad|Elstad]]* controls.

## Appears on
- [[Miranda Waiver and Invocation]] — *Related*

## Sources
- *Bobby v. Dixon*, 565 U.S. 23 (2011) (per curiam) — https://www.courtlistener.com/opinion/616807/bobby-v-dixon/ — pinpoint: 31.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c7976c29d7f85be1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Bobby v. Dixon"}, "payload": {"all": [{"cite": "132 S. Ct. 26", "page": "26", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "181 L. Ed. 2d 328", "page": "328", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "181"}, {"cite": "565 U.S. 23", "page": "23", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "2011 U.S. LEXIS 7926", "page": "7926", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}], "display": "565 U.S. 23", "official": {"cite": "565 U.S. 23", "page": "23", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "Bobby v. Dixon"}}
{"assertion_id": "5387db804e2c3514", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-31a", "record_id": "Bobby v. Dixon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-31a", "pinpoint_status": "slip-only", "quote": "simply 'no nexus' between Dixon's unwarned admission to forgery and his later, warned confession to murder,", "quote_fidelity": "mismatch", "record_id": "Bobby v. Dixon", "star_marker": null}}
{"assertion_id": "7e0968ccab0873c3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-31", "record_id": "Bobby v. Dixon"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-31", "pinpoint_status": "slip-only", "quote": "strategy under *Missouri v. Seibert*. ## Issue Whether, on AEDPA review, the state court unreasonably applied clearly established federal law in admitting Dixon's warned murder confession given his earlier unwarned interrogation about a related forgery. ## Rule No — admission was reasonable; *Seibert*'s concern was absent and *Elstad* governs.", "quote_fidelity": "mismatch", "record_id": "Bobby v. Dixon", "star_marker": null}}
{"assertion_id": "aca44c9b9580f2ed", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Bobby v. Dixon"}, "payload": {"as_of_content": "2011-11-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Bobby v. Dixon", "scope_note": "Per curiam AEDPA reversal; good law.", "varies_by_point": false}}
```

### lake record — Bobby v. Dixon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bobby v. Dixon",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bobby v. Dixon",
    "case_name_short": "Bobby",
    "case_name_full": "Bobby, Warden v. Dixon",
    "input_case_name": "Bobby v. Dixon",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-11-07",
    "year": 2011,
    "docket": "10-1540",
    "cluster_id": 616807,
    "lead_opinion_id": 616807,
    "sibling_ids": [
      616807
    ],
    "absolute_url": "/opinion/616807/bobby-v-dixon/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 23",
      "volume": "565",
      "reporter": "U.S.",
      "page": "23",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 26",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 328",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 7926",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "7926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 26",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "26",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 328",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "328",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 23",
        "volume": "565",
        "reporter": "U.S.",
        "page": "23",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 7926",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "7926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 23",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 23",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-31",
      "page": null,
      "quote": "strategy under *Missouri v. Seibert*. ## Issue Whether, on AEDPA review, the state court unreasonably applied clearly established federal law in admitting Dixon's warned murder confession given his earlier unwarned interrogation about a related forgery. ## Rule No \u2014 admission was reasonable; *Seibert*'s concern was absent and *Elstad* governs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-31a",
      "page": null,
      "quote": "simply 'no nexus' between Dixon's unwarned admission to forgery and his later, warned confession to murder,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-11-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bobby v. Dixon",
    "varies_by_point": false,
    "scope_note": "Per curiam AEDPA reversal; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jose Vasquez v. State",
          "cluster_id": 2763816,
          "cite": [
            "453 S.W.3d 555",
            "2014 Tex. App. LEXIS 13776",
            "2014 WL 7365945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul H. Evans v. Secretary, Florida Department of Corrections",
          "cluster_id": 810858,
          "cite": [
            "699 F.3d 1249",
            "2012 WL 5200326",
            "2012 U.S. App. LEXIS 22072"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Antwion Thompson v. D. Runnel",
          "cluster_id": 815924,
          "cite": [
            "705 F.3d 1089",
            "2013 WL 263909",
            "2013 U.S. App. LEXIS 1585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Krebs",
          "cluster_id": 4680693,
          "cite": [
            "452 P.3d 609",
            "255 Cal. Rptr. 3d 95",
            "8 Cal. 5th 265"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Young",
          "cluster_id": 4642880,
          "cite": [
            "250 Cal. Rptr. 3d 192",
            "445 P.3d 591",
            "7 Cal. 5th 905"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Wayne Holsey v. Warden, Georgia Diagonstic Prison",
          "cluster_id": 808587,
          "cite": [
            "694 F.3d 1230",
            "2012 WL 4017294",
            "2012 U.S. App. LEXIS 19370"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roy Blackmon v. Raymond Booker",
          "cluster_id": 809747,
          "cite": [
            "696 F.3d 536",
            "2012 WL 4774510",
            "2012 U.S. App. LEXIS 20898"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jarnagin",
          "cluster_id": 834830,
          "cite": [
            "277 P.3d 535",
            "351 Or. 703",
            "2012 WL 1437302",
            "2012 Ore. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Black v. Ricky Bell",
          "cluster_id": 618946,
          "cite": [
            "664 F.3d 81",
            "2011 U.S. App. LEXIS 24798",
            "2011 WL 6224560"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wade Robertson v. Rise Pichon",
          "cluster_id": 4372525,
          "cite": [
            "849 F.3d 1173",
            "2017 WL 816886",
            "2017 U.S. App. LEXIS 3770"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Duvall",
          "cluster_id": 1037487,
          "cite": [
            "408 U.S. App. D.C. 73",
            "740 F.3d 604",
            "2013 WL 6501162",
            "2013 U.S. App. LEXIS 16874"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Clifton",
          "cluster_id": 4400956,
          "cite": [
            "892 N.W.2d 112",
            "296 Neb. 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peak v. Webb",
          "cluster_id": 625291,
          "cite": [
            "673 F.3d 465",
            "2012 U.S. App. LEXIS 5358",
            "2012 WL 833179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin Moore v. Mary Berghuis",
          "cluster_id": 812911,
          "cite": [
            "700 F.3d 882",
            "2012 U.S. App. LEXIS 24627",
            "2012 WL 5971205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vaughn Mitchell v. Duncan MacLaren",
          "cluster_id": 4645020,
          "cite": [
            "933 F.3d 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael D. Overstree v. Bill Wilson",
          "cluster_id": 804052,
          "cite": [
            "686 F.3d 404",
            "2012 WL 2819296",
            "2012 U.S. App. LEXIS 14106"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Verigan v. People",
          "cluster_id": 4506740,
          "cite": [
            "2018 CO 53",
            "420 P.3d 247"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Beeson",
          "cluster_id": 10133881,
          "cite": [
            "307 Or. App. 808",
            "479 P.3d 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nanavati v. Adecco USA, Inc.",
          "cluster_id": 7313087,
          "cite": [
            "99 F. Supp. 3d 1072",
            "2015 U.S. Dist. LEXIS 49053",
            "2015 WL 1738152"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "MERAS v. Sisto",
          "cluster_id": 798465,
          "cite": [
            "676 F.3d 1184",
            "2012 WL 1382857",
            "2012 U.S. App. LEXIS 8104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian Reyes v. Greg Lewis",
          "cluster_id": 2827465,
          "cite": [
            "798 F.3d 815",
            "2015 U.S. App. LEXIS 14296",
            "2015 WL 4773374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sakajust Scott v. Randall Hepp",
          "cluster_id": 9382680,
          "cite": [
            "62 F.4th 343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mohamad Khweis",
          "cluster_id": 4788077,
          "cite": [
            "971 F.3d 453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Felix Ruiz",
          "cluster_id": 4463512,
          "cite": [
            "179 A.3d 333",
            "170 N.H. 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bobby v. Dixon:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(616807) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 65,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 65,
        "triage_read": 4,
        "triage_snippet_classified": 61
      },
      "lane2_top_cited": {
        "query": "cites:(616807)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9MzE2NzQ1MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28616807%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(616807)",
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
    "complete_query": "cites:(616807)",
    "indexed_citing_opinions": 67,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 616807,
        "count": 67,
        "count_source": "search"
      }
    ],
    "citation_count": 282,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bobby-v-dixon.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NzUyMTEmcz0xMDM2Njg0NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28616807%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 616807,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 112566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 137002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 145873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 616807,
        "cited_id": 180733,
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
    "date_created": "2026-07-04T20:02:45Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:07:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:04:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bobby v. Dixon

```
                 Cite as: 565 U. S. ____ (2011)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
     DAVID BOBBY, WARDEN v. ARCHIE DIXON
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT

            No. 10–1540. Decided November 7, 2011


  PER CURIAM.
  Under the Antiterrorism and Effective Death Penalty
Act, a state prisoner seeking a writ of habeas corpus from
a federal court “must show that the state court’s ruling on
the claim being presented in federal court was so lacking
in justification that there was an error well understood
and comprehended in existing law beyond any possibility
for fairminded disagreement.” Harrington v. Richter, 562
U. S. ___, ___ (2011) (slip op., at 13). The Court of Appeals
for the Sixth Circuit purported to identify three such
grievous errors in the Ohio Supreme Court’s affirmance of
respondent Archie Dixon’s murder conviction. Because it
is not clear that the Ohio Supreme Court erred at all,
much less erred so transparently that no fairminded jurist
could agree with that court’s decision, the Sixth Circuit’s
judgment must be reversed.
                         *    *    *
   Archie Dixon and Tim Hoffner murdered Chris Hammer
in order to steal his car. Dixon and Hoffner beat Hammer,
tied him up, and buried him alive, pushing the struggling
Hammer down into his grave while they shoveled dirt on
top of him. Dixon then used Hammer’s birth certificate
and social security card to obtain a state identification
card in Hammer’s name. After using that identification
card to establish ownership of Hammer’s car, Dixon sold
the vehicle for $2,800.
   Hammer’s mother reported her son missing the day
after his murder. While investigating Hammer’s disap­
2                     BOBBY v. DIXON

                         Per Curiam

pearance, police had various encounters with Dixon, three
of which are relevant here. On November 4, 1993, a police
detective spoke with Dixon at a local police station. It is
undisputed that this was a chance encounter—Dixon was
apparently visiting the police station to retrieve his own
car, which had been impounded for a traffic violation. The
detective issued Miranda warnings to Dixon and then
asked to talk to him about Hammer’s disappearance. See
Miranda v. Arizona, 384 U. S. 436 (1966). Dixon declined
to answer questions without his lawyer present and left
the station.
   As their investigation continued, police determined that
Dixon had sold Hammer’s car and forged Hammer’s signa­
ture when cashing the check he received in that sale.
Police arrested Dixon for forgery on the morning of No­
vember 9. Beginning at 11:30 a.m. detectives intermit­
tently interrogated Dixon over several hours, speaking
with him for about 45 minutes total. Prior to the interro­
gation, the detectives had decided not to provide Dixon
with Miranda warnings for fear that Dixon would again
refuse to speak with them.
   Dixon readily admitted to obtaining the identification
card in Hammer’s name and signing Hammer’s name on
the check, but said that Hammer had given him permis­
sion to sell the car. Dixon claimed not to know where
Hammer was, although he said he thought Hammer might
have left for Tennessee. The detectives challenged the
plausibility of Dixon’s tale and told Dixon that Tim
Hoffner was providing them more useful information. At
one point a detective told Dixon that “now is the time to
say” whether he had any involvement in Hammer’s disap­
pearance because “if Tim starts cutting a deal over there,
this is kinda like, a bus leaving. The first one that gets on
it is the only one that’s gonna get on.” App. to Pet. for
Cert. 183a. Dixon responded that, if Hoffner knew any­
thing about Hammer’s disappearance, Hoffner had not
                 Cite as: 565 U. S. ____ (2011)           3

                          Per Curiam

told him. Dixon insisted that he had told police everything
he knew and that he had “[n]othing whatsoever” to do
with Hammer’s disappearance. Id., at 186a. At approxi­
mately 3:30 p.m. the interrogation concluded, and the
detectives brought Dixon to a correctional facility where
he was booked on a forgery charge.
  The same afternoon, Hoffner led police to Hammer’s
grave. Hoffner claimed that Dixon had told him that
Hammer was buried there. After concluding their inter­
view with Hoffner and releasing him, the police had Dixon
transported back to the police station.
  Dixon arrived at the police station at about 7:30 p.m.
Prior to any police questioning, Dixon stated that he had
heard the police had found a body and asked whether
Hoffner was in custody. The police told Dixon that
Hoffner was not, at which point Dixon said, “I talked to
my attorney, and I want to tell you what happened.” State
v. Dixon, 101 Ohio St. 3d 328, 331, 2004–Ohio–1585, 805
N. E. 2d 1042, 1050. The police read Dixon his Miranda
rights, obtained a signed waiver of those rights, and spoke
with Dixon for about half an hour. At 8 p.m. the police,
now using a tape recorder, again advised Dixon of his
Miranda rights. In a detailed confession, Dixon admitted
to murdering Hammer but attempted to pin the lion’s
share of the blame on Hoffner.
  At Dixon’s trial, the Ohio trial court excluded both
Dixon’s initial confession to forgery and his later confes­
sion to murder. The State took an interlocutory appeal.
The State did not dispute that Dixon’s forgery confession
was properly suppressed, but argued that the murder
confession was admissible because Dixon had received
Miranda warnings prior to that confession. The Ohio
Court of Appeals agreed and allowed Dixon’s murder
confession to be admitted as evidence. Dixon was convict­
ed of murder, kidnaping, robbery, and forgery, and sen­
tenced to death.
4                      BOBBY v. DIXON

                         Per Curiam

   The Ohio Supreme Court affirmed Dixon’s convictions
and sentence. To analyze the admissibility of Dixon’s
murder confession, the court applied Oregon v. Elstad, 470
U. S. 298 (1985). The Ohio Supreme Court found that
Dixon’s confession to murder after receiving Miranda
warnings was admissible because that confession and his
prior, unwarned confession to forgery were both voluntary.
State v. Dixon, supra, at 332–334, 805 N. E. 2d, at 1050–
1052; see Elstad, supra, at 318 (“We hold today that a
suspect who has once responded to unwarned yet uncoer­
cive questioning is not thereby disabled from waiving his
rights and confessing after he has been given the requisite
Miranda warnings”).
   Dixon then filed a petition for a writ of habeas corpus
under 28 U. S. C. §2254 in the U. S. District Court for the
Northern District of Ohio. Dixon claimed, inter alia, that
the state court decisions allowing the admission of his
murder confession contravened clearly established federal
law. The District Court denied relief, but a divided panel
of the Sixth Circuit reversed. Dixon v. Houk, 627 F. 3d
553 (2010).
   The Sixth Circuit had authority to issue the writ of
habeas corpus only if the Ohio Supreme Court’s decision
“was contrary to, or involved an unreasonable application
of, clearly established Federal law,” as set forth in this
Court’s holdings, or was “based on an unreasonable de­
termination of the facts” in light of the state court record.
§2254(d); see Harrington, 562 U. S., at ___ (slip op., at 10).
The Sixth Circuit believed that the Ohio Supreme Court’s
decision contained three such egregious errors.
   First, according to the Sixth Circuit, the Miranda deci­
sion itself clearly established that police could not speak to
Dixon on November 9, because on November 4 Dixon had
refused to speak to police without his lawyer. That is
plainly wrong. It is undisputed that Dixon was not in
custody during his chance encounter with police on No­
                     Cite as: 565 U. S. ____ (2011)                   5

                              Per Curiam

vember 4. And this Court has “never held that a person
can invoke his Miranda rights anticipatorily, in a context
other than ‘custodial interrogation.’ ” McNeil v. Wisconsin,
501 U. S. 171, 182, n. 3 (1991); see also Montejo v. Louisi-
ana, 556 U. S. 778, ___ (2009) (slip. op., at 16) (“If the
defendant is not in custody then [Miranda and its proge­
ny] do not apply”).
  Second, the Sixth Circuit held that police violated the
Fifth Amendment by urging Dixon to “cut a deal” before
his accomplice Hoffner did so.1 The Sixth Circuit cited no
precedent of this Court—or any court—holding that this
common police tactic is unconstitutional. Cf., e.g., Elstad,
supra, at 317 (“[T]he Court has refused to find that a
defendant who confesses, after being falsely told that his
codefendant has turned State’s evidence, does so involun­
tarily”). Because no holding of this Court suggests, much
less clearly establishes, that police may not urge a suspect
to confess before another suspect does so, the Sixth Circuit
had no authority to issue the writ on this ground.2
——————
   1 In the Sixth Circuit’s view, the Ohio Supreme Court’s contrary con­

clusion that Dixon’s confession was voluntary “was based on an unrea­
sonable determination of the facts in light of the evidence presented in
the State court proceeding.” §2254(d)(2). The Sixth Circuit did not,
however, purport to identify any mistaken factual finding. It differed
with the Ohio Supreme Court only on the ultimate characterization of
Dixon’s confession as voluntary, and this Court’s cases make clear that
“the ultimate issue of ‘voluntariness’ is a legal question.” Miller v.
Fenton, 474 U. S. 104, 110 (1985); see also Arizona v. Fulminante, 499
U. S. 279, 287 (1991). This Court therefore addresses the question the
Sixth Circuit should have addressed: whether the Ohio Supreme
Court’s decision “was contrary to, or involved an unreasonable applica­
tion of, clearly established Federal law, as determined by the Supreme
Court of the United States.” §2254(d)(1).
   2 The only case the Sixth Circuit cited on this issue was Mincey v.

Arizona, 437 U. S. 385 (1978). Mincey involved the “virtually continu­
ous questioning of a seriously and painfully wounded man on the edge
of consciousness” who was in a hospital’s intensive care unit and who
6                          BOBBY v. DIXON

                              Per Curiam

   Third, the Sixth Circuit held that the Ohio Supreme
Court unreasonably applied this Court’s precedent in
Elstad. In that case, a suspect who had not received
Miranda warnings confessed to burglary as police took
him into custody. Approximately an hour later, after he
had received Miranda warnings, the suspect again con­
fessed to the same burglary. This Court held that the
later, warned confession was admissible because “there is
no warrant for presuming coercive effect where the sus­
pect’s initial inculpatory statement, though technically
in violation of Miranda, was voluntary. The relevant
inquiry is whether, in fact, the second [warned] statement
was also voluntarily made.” 470 U. S., at 318 (footnote
omitted).
   As the Ohio Supreme Court’s opinion explained, the
circumstances surrounding Dixon’s interrogations demon­
strate that his statements were voluntary. During Dixon’s
first interrogation, he received several breaks, was given
water and offered food, and was not abused or threatened.
He freely acknowledged that he had forged Hammer’s
name, even stating that the police were “welcome” to that
information, and he had no difficulty denying that he had
anything to do with Hammer’s disappearance. State v.
Dixon, 101 Ohio St. 3d, at 331, 805 N. E. 2d, at 1049.
Prior to his second interrogation, Dixon made an unsolic­
ited declaration that he had spoken with his attorney and
wanted to tell the police what had happened to Hammer.
Then, before giving his taped confession, Dixon twice
received Miranda warnings and signed a waiver-of-rights
form which stated that he was acting of his own free will.


——————
“clearly expressed his wish not to be interrogated” while in a “debilitat­
ed and helpless condition.” Id., at 399–401. There is simply nothing in
the facts or reasoning of Mincey suggesting that any of Dixon’s state­
ments were involuntary.
                     Cite as: 565 U. S. ____ (2011)                     7

                              Per Curiam

The Ohio Supreme Court recognized that Dixon’s first in-
terrogation involved “an intentional Miranda violation.”
The court concluded, however, that “as in Elstad, the
breach of the Miranda procedures here involved no actual
compulsion” and thus there was no reason to suppress
Dixon’s later, warned confession. 101 Ohio St. 3d, at 334,
805 N. E. 2d, at 1052 (citing Elstad, supra, at 318).
  The Sixth Circuit disagreed, believing that Dixon’s
confession was inadmissible under Elstad because it was
the product of a “deliberate question-first, warn-later
strategy.” 627 F. 3d, at 557. In so holding, the Sixth
Circuit relied heavily on this Court’s decision in Missouri
v. Seibert, 542 U. S. 600 (2004).3 In Seibert, police em­
ployed a two-step strategy to reduce the effect of Miranda
warnings: A detective exhaustively questioned Seibert
until she confessed to murder and then, after a 15- to 20­
minute break, gave Seibert Miranda warnings and led her
to repeat her prior confession. 542 U. S., at 604–606, 616
(plurality opinion). The Court held that Seibert’s second
confession was inadmissible as evidence against her even
though it was preceded by a Miranda warning. A plurali­
ty of the Court reasoned that “[u]pon hearing warnings
only in the aftermath of interrogation and just after mak­

——————
   3 Seibert was not decided until after the Ohio Supreme Court’s opin­

ion in this case, but was issued before this Court denied Dixon’s peti­
tion for certiorari seeking review of the Ohio Supreme Court’s decision.
It is thus an open question whether Seibert was “clearly established
Federal law” for purposes of §2254(d). See Smith v. Spisak¸ 558 U. S.
___, ___ (2010) (slip op., at 3). It is not necessary to decide that ques­
tion here because Seibert is entirely consistent with the Ohio Supreme
Court’s decision. Thus, if Seibert was clearly established law, the Ohio
Supreme Court’s decision was not “contrary to” or “an unreasonable
application of” Seibert. §2254(d). And if Seibert was not clearly estab­
lished law, Seibert’s explication of Elstad further demonstrates that the
Ohio Supreme Court’s decision was not contrary to or an unreasonable
application of Elstad.
8                      BOBBY v. DIXON

                          Per Curiam

ing a confession, a suspect would hardly think he had a
genuine right to remain silent, let alone persist in so
believing once the police began to lead him over the same
ground again.” 542 U. S., at 613; see also id., at 615 (de­
tailing a “series of relevant facts that bear on whether
Miranda warnings delivered midstream could be effective
enough to accomplish their object”). JUSTICE KENNEDY
concurred in the judgment, noting he “would apply a
narrower test applicable only in the infrequent case . . . in
which the two-step interrogation technique was used in a
calculated way to undermine the Miranda warning.” Id.,
at 622.
   In this case, no two-step interrogation technique of the
type that concerned the Court in Seibert undermined the
Miranda warnings Dixon received. In Seibert, the sus­
pect’s first, unwarned interrogation left “little, if anything,
of incriminating potential left unsaid,” making it “unnatu­
ral” not to “repeat at the second stage what had been said
before.” 542 U. S., at 616–617 (plurality opinion). But in
this case Dixon steadfastly maintained during his first,
unwarned interrogation that he had “[n]othing whatso­
ever” to do with Hammer’s disappearance. App. to Pet. for
Cert. 186a. Thus, unlike in Seibert, there is no concern
here that police gave Dixon Miranda warnings and then
led him to repeat an earlier murder confession, because
there was no earlier confession to repeat. Indeed, Dixon
contradicted his prior unwarned statements when he
confessed to Hammer’s murder. Nor is there any evidence
that police used Dixon’s earlier admission to forgery to
induce him to waive his right to silence later: Dixon de­
clared his desire to tell police what happened to Hammer
before the second interrogation session even began. As the
Ohio Supreme Court reasonably concluded, there was
simply “no nexus” between Dixon’s unwarned admission to
forgery and his later, warned confession to murder. 101
Ohio St. 3d, at 333, 805 N. E. 2d, at 1051.
                     Cite as: 565 U. S. ____ (2011)                    9

                              Per Curiam

   Moreover, in Seibert the Court was concerned that the
Miranda warnings did not “effectively advise the suspect
that he had a real choice about giving an admissible
statement” because the unwarned and warned interroga­
tions blended into one “continuum.” 542 U. S., at 612, 617.
Given all the circumstances of this case, that is not so
here. Four hours passed between Dixon’s unwarned inter­
rogation and his receipt of Miranda rights, during which
time he traveled from the police station to a separate jail
and back again; claimed to have spoken to his lawyer; and
learned that police were talking to his accomplice and
had found Hammer’s body. Things had changed. Under
Seibert, this significant break in time and dramatic
change in circumstances created “a new and distinct expe­
rience,” ensuring that Dixon’s prior, unwarned interroga­
tion did not undermine the effectiveness of the Miranda
warnings he received before confessing to Hammer’s mur­
der. 542 U. S., at 615; see also id., at 622 (KENNEDY, J.,
concurring in judgment) (“For example, a substantial
break in time and circumstances between the prewarning
statement and the Miranda warning may suffice in most
circumstances, as it allows the accused to distinguish the
two contexts and appreciate that the interrogation has
taken a new turn”).4
   The admission of Dixon’s murder confession was con­
sistent with this Court’s precedents: Dixon received Mi-


——————
   4 The Sixth Circuit also concluded that “the Ohio Supreme Court

erroneously placed the burden of proof on Dixon to prove that his
confession was coerced.” Dixon v. Houk, 627 F. 3d 553, 558 (2010). But
the Ohio Supreme Court clearly said that “the state carries the burden
of proving voluntariness.” State v. Dixon, 101 Ohio St. 3d 328, 332,
2004–Ohio–1585, 805 N. E. 2d 1042, 1050. That the court’s opinion
discusses the absence of evidence of coerciveness alongside the affirma­
tive evidence of voluntariness in no way indicates that the court shifted
the burden onto Dixon.
10                    BOBBY v. DIXON

                         Per Curiam

randa warnings before confessing to Hammer’s murder;
the effectiveness of those warnings was not impaired by
the sort of “two-step interrogation technique” condemned
in Seibert; and there is no evidence that any of Dixon’s
statements was the product of actual coercion. That does
not excuse the detectives’ decision not to give Dixon Mi-
randa warnings before his first interrogation. But the
Ohio courts recognized that failure and imposed the ap­
propriate remedy: exclusion of Dixon’s forgery confession
and the attendant statements given without the benefit of
Miranda warnings. Because no precedent of this Court
required Ohio to do more, the Sixth Circuit was without
authority to overturn the reasoned judgment of the State’s
highest court.
  The petition for a writ of certiorari and respondent’s
motion to proceed in forma pauperis are granted. The
judgment of the Court of Appeals for the Sixth Circuit is
reversed, and the case is remanded for further proceedings
consistent with this opinion.
                                           It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Bond v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Bond v. United States"
type: case
citation: "529 U.S. 334 (2000)"
parallel_cite: "120 S. Ct. 1462; 146 L. Ed. 2d 365"
neutral_cite: 2000 U.S. LEXIS 2520
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-04-17
docket: 98-9349
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bond v. United States
  varies_by_point: false
  scope_note: "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118354/bond-v-united-states/"
  cluster_id: 118354
  opinion_id: 9433930
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — Progeny"
  - page: "[[Abandonment]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Ciraolo]]", "[[Florida v. Riley]]", "[[United States v. Place]]", "[[Terry v. Ohio]]"]
aliases: ["Bond v. United States (2000)"]
tags: ["case", "fourth-amendment", "search", "luggage", "tactile", "reasonable-expectation-of-privacy"]
holding: "An officer's physical manipulation (squeezing) of a bus passenger's soft carry-on luggage is a Fourth Amendment search; tactile inspection is more intrusive than visual observation."
lake:
  record_id: Bond v. United States
  status: verified
  projected_at: 2026-07-06
---

# Bond v. United States

*529 U.S. 334 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Border Patrol agent boarded a stopped Greyhound bus to check immigration status. Walking back toward the front, he squeezed the soft luggage in the overhead bins, felt a "brick-like" object in Bond's green canvas bag, obtained Bond's consent to open it, and found methamphetamine. Bond moved to suppress, arguing the agent's squeezing of his bag was an unreasonable search.

## Issue
Whether a law enforcement officer's physical manipulation of a bus passenger's soft carry-on luggage is a "search" within the meaning of the Fourth Amendment.

## Rule
Yes. Tactile examination is more invasive than visual observation: distinguishing the aerial-observation cases, the Court explained that "[p]hysically invasive inspection is simply more intrusive than purely visual inspection." — 529 U.S. at 337. ^pin-337

A traveler retains a privacy interest against exploratory squeezing: "a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent's physical manipulation of petitioner's bag violated the Fourth Amendment." — *Id.* at 338–339. ^pin-338

## Application
Bond, by placing his bag in the overhead bin, expected that fellow passengers and bus personnel might move or handle it — but not that they would feel it in the deliberate, exploratory manner the agent used to detect its contents. Because that manipulation exceeded the casual handling a traveler anticipates, it invaded a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and constituted a search; the agent had no warrant or other justification for it.

## Conclusion
The agent's exploratory squeezing of the bag was a Fourth Amendment search; the judgment was reversed. Personal luggage carried by a traveler retains Fourth Amendment protection against tactile, exploratory inspection even when exposed to incidental public handling.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Distinguishes the visual-observation line ([[California v. Ciraolo]], [[Florida v. Riley]]) and confirms that a traveler's bag is an "effect" with retained privacy (cf. [[United States v. Place]]).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — Progeny*
- [[Abandonment]] — *Related (cross-doctrine)*

## Sources
- *Bond v. United States*, 529 U.S. 334 (2000) — https://www.courtlistener.com/opinion/118354/bond-v-united-states/ — pinpoints: 337, 338–339.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c72cab765b58166d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Bond v. United States"}, "payload": {"all": [{"cite": "529 U.S. 334", "page": "334", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "529"}, {"cite": "120 S. Ct. 1462", "page": "1462", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "120"}, {"cite": "146 L. Ed. 2d 365", "page": "365", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "146"}, {"cite": "2000 U.S. LEXIS 2520", "page": "2520", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}], "display": "529 U.S. 334", "official": {"cite": "529 U.S. 334", "page": "334", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "529"}, "official_selection_present": true, "record_id": "Bond v. United States"}}
{"assertion_id": "aaa6413456cdc003", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-337", "record_id": "Bond v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-337", "pinpoint_status": "slip-only", "quote": "within the meaning of the Fourth Amendment. ## Rule Yes. Tactile examination is more invasive than visual observation: distinguishing the aerial-observation cases, the Court explained that", "quote_fidelity": "mismatch", "record_id": "Bond v. United States", "star_marker": null}}
{"assertion_id": "e50eaab0f322827e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-338", "record_id": "Bond v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-338", "pinpoint_status": "slip-only", "quote": "a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent's physical manipulation of petitioner's bag violated the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "Bond v. United States", "star_marker": null}}
{"assertion_id": "85e6e9a15b84f46b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Bond v. United States"}, "payload": {"as_of_content": "2000-04-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Bond v. United States", "scope_note": "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling.", "varies_by_point": false}}
```

### lake record — Bond v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bond v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bond v. United States",
    "case_name_short": "Bond",
    "case_name_full": "Bond v. United States",
    "input_case_name": "Bond v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-04-17",
    "year": 2000,
    "docket": "98-9349",
    "cluster_id": 118354,
    "lead_opinion_id": 9433930,
    "sibling_ids": [
      118354,
      9433930,
      9433931
    ],
    "absolute_url": "/opinion/118354/bond-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "529 U.S. 334",
      "volume": "529",
      "reporter": "U.S.",
      "page": "334",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 1462",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "1462",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "146 L. Ed. 2d 365",
        "volume": "146",
        "reporter": "L. Ed. 2d",
        "page": "365",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 2520",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "2520",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "529 U.S. 334",
        "volume": "529",
        "reporter": "U.S.",
        "page": "334",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 1462",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "1462",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "146 L. Ed. 2d 365",
        "volume": "146",
        "reporter": "L. Ed. 2d",
        "page": "365",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 2520",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "2520",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "529 U.S. 334",
    "official_selection": {
      "court_class": "scotus",
      "selected": "529 U.S. 334",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-337",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes. Tactile examination is more invasive than visual observation: distinguishing the aerial-observation cases, the Court explained that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-338",
      "page": null,
      "quote": "a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent's physical manipulation of petitioner's bag violated the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bond v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the rule that exploratory tactile manipulation of a traveler's bag is a search remains controlling.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morris Wise",
          "cluster_id": 4448990,
          "cite": [
            "877 F.3d 209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Peterson",
          "cluster_id": 3961890,
          "cite": [
            "879 N.E.2d 806",
            "173 Ohio App. 3d 575",
            "2007 Ohio 5667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poteet v. Sullivan",
          "cluster_id": 2332316,
          "cite": [
            "218 S.W.3d 780",
            "2007 WL 289871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camacho",
          "cluster_id": 2546036,
          "cite": [
            "3 P.3d 878",
            "98 Cal. Rptr. 2d 232",
            "23 Cal. 4th 824",
            "2000 Cal. Daily Op. Serv. 6235",
            "2000 Daily Journal DAR 8273",
            "2000 Cal. LEXIS 5605"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
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
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turrubiate v. State",
          "cluster_id": 2948365,
          "cite": [
            "399 S.W.3d 147",
            "2013 WL 1438172",
            "2013 Tex. Crim. App. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maynard",
          "cluster_id": 152441,
          "cite": [
            "615 F.3d 544",
            "392 U.S. App. D.C. 291",
            "2010 U.S. App. LEXIS 16417",
            "2010 WL 3063788"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lisa Amaechi v. Matthew West, and Bernard R. Pfluger Town of Dumfries",
          "cluster_id": 771726,
          "cite": [
            "237 F.3d 356",
            "2001 U.S. App. LEXIS 267",
            "2001 WL 20530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 2545158,
          "cite": [
            "3 P.3d 311",
            "97 Cal. Rptr. 2d 914",
            "23 Cal. 4th 789"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darlie Kee Darin Routier v. City of Rowlett Texas Jimmy Ray Patterson Chris Frosch Greg Davis, Assistant District Attorney for Dallas County",
          "cluster_id": 772922,
          "cite": [
            "247 F.3d 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cregan",
          "cluster_id": 2681818,
          "cite": [
            "2014 IL 113600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reyes Fabian Olivera-Mendez",
          "cluster_id": 797553,
          "cite": [
            "484 F.3d 505",
            "2007 U.S. App. LEXIS 10492",
            "2007 WL 1296781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Perea-Rey",
          "cluster_id": 801335,
          "cite": [
            "680 F.3d 1179",
            "2012 U.S. App. LEXIS 10941",
            "2012 WL 1948973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Weaver",
          "cluster_id": 5639938,
          "cite": [
            "12 N.Y.3d 433",
            "909 N.E.2d 1195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Krise v. State",
          "cluster_id": 853398,
          "cite": [
            "746 N.E.2d 957",
            "2001 Ind. LEXIS 394",
            "2001 WL 493444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frederick Alonzo Waller",
          "cluster_id": 792220,
          "cite": [
            "426 F.3d 838",
            "2005 U.S. App. LEXIS 22941",
            "2005 WL 2708784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth King",
          "cluster_id": 770537,
          "cite": [
            "227 F.3d 732",
            "2000 WL 1209277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bond v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118354 OR 9433930 OR 9433931) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 177,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 177,
        "triage_read": 6,
        "triage_snippet_classified": 171
      },
      "lane2_top_cited": {
        "query": "cites:(118354 OR 9433930 OR 9433931)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OCZzPTEyNDg0NTkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118354+OR+9433930+OR+9433931%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118354 OR 9433930 OR 9433931)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118354 OR 9433930 OR 9433931)",
    "indexed_citing_opinions": 238,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118354,
        "count": 202,
        "count_source": "search"
      },
      {
        "opinion_id": 9433930,
        "count": 41,
        "count_source": "search"
      },
      {
        "opinion_id": 9433931,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 413,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bond-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NjY0OTUmcz02NDcxNTEyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118354+OR+9433930+OR+9433931%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118354,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118354,
        "cited_id": 729772,
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
    "date_created": "2026-07-04T20:07:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:12:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:08:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bond v. United States

```
<opinion type="majority">
<author id="b411-7">Chief Justice Rehnquist</author>
<p id="Ahq">delivered the opinion of the Court.</p>
<p id="b411-8">This case presents the question whether a law enforcement officer’s physical manipulation of a bus passenger’s carry-on luggage violated the Fourth Amendment’s proscription against unreasonable searches. We hold that it did.</p>
<p id="b411-9">Petitioner Steven Dewayne Bond was a passenger on a Greyhound bus that left California bound for Little Rock, Arkansas. The bus stopped, as it was required to do, at the permanent Border Patrol checkpoint in Sierra Blanca, Texas. Border Patrol Agent Cesar Cantu boarded the bus to check the immigration status of its passengers. After reaching the back of the bus, having satisfied himself that the passengers were lawfully in the United States, Agent Cantu began walking toward the front. Along the way, he squeezed the soft luggage which passengers had placed in the overhead storage space above the seats.</p>
<p id="b412-4"><page-number citation-index="1" label="336">*336</page-number>Petitioner was seated four or five rows from the back of the bus. As Agent Cantu inspected the luggage in the compartment above petitioner’s seat, he squeezed a green canvas bag and noticed that it contained a “brick-like” object. Petitioner admitted that the bag was his and agreed to allow Agent Cantu to open it.<footnotemark>1</footnotemark> Upon opening the bag, Agent Cantu discovered a “brick” of methamphetamine. The brick had been wrapped in duct tape until it was oval-shaped and then rolled in a pair of pants.</p>
<p id="b412-5">Petitioner was indicted for conspiracy to possess, and possession with intent to distribute, methamphetamine in violation of <span class="citation no-link">84 Stat. 1260</span>, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). He moved to suppress the drugs, arguing that Agent Cantu conducted an illegal search of his bag. Petitioner’s motion was denied, and the District Court found him guilty on both counts and sentenced him to 57 months in prison. On appeal, he conceded that other passengers had access to his bag, but contended that Agent Cantu manipulated the bag in a way that other passengers would not. The Court of Appeals rejected this argument, stating that the fact that Agent Cantu’s manipulation of petitioner’s bag was calculated to detect contraband is irrelevant for Fourth Amendment purposes. <span class="citation" data-id="6981740"><a href="/opinion/7076945/united-states-v-bond/#227" aria-description="Citation for case: United States v. Bond">167 F. 3d 225, 227</a></span> (CA5 1999) (citing <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986)). Thus, the Court of Appeals affirmed the denial of the motion to suppress, holding that Agent Cantu’s manipulation of the bag was not a search within the meaning of the Fourth Amendment. <span class="citation" data-id="6981740"><a href="/opinion/7076945/united-states-v-bond/#227" aria-description="Citation for case: United States v. Bond">167 F. 3d, at 227</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/927/">528 U. S. 927</a></span> (1999), and now reverse.</p>
<p id="b412-6">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated....” A traveler’s personal luggage is clearly an “effect” protected by the Amendment. See <em>United States </em>v. <page-number citation-index="1" label="337">*337</page-number><em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Indeed, it is undisputed here that petitioner possessed a privacy interest in his bag.</p>
<p id="b413-5">But the Government asserts that by exposing his bag to the public, petitioner lost a reasonable expectation that his bag would not be physically manipulated. The Government relies on our decisions in <em>California </em>v. <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra,</a></span> </em>and <em>Florida </em>v. <em>Riley, </em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">488 U. S. 445</a></span> (1989), for the proposition that matters open to public observation are not protected by the Fourth Amendment. In <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>, </em>we held that police observation of a backyard from a plane flying at an altitude of 1,000 feet did not violate a reasonable expectation of privacy. Similarly, in <em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">Riley</a></span>, </em>we relied on <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span> </em>to hold that police observation of a greenhouse in a home’s curtilage from a helicopter passing at an altitude of 400 feet did not violate the Fourth Amendment. We reasoned that the property was “not necessarily protected from inspection that involves no physical invasion,” and determined that because any member of the public could have lawfully observed the defendants’ property by flying overhead, the defendants’ expectation of privacy was “not reasonable and not one ‘that society is prepared to honor.’ ” See <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#449" aria-description="Citation for case: Florida v. Riley"><em>Riley, supra, </em>at 449</a></span> (explaining and relying on Ciraolo’s reasoning).</p>
<p id="b413-6">But <em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span> </em>and <em><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">Riley</a></span> </em>are different from this case because they involved only visual, as opposed to tactile, observation. Physically invasive inspection is simply more intrusive than purely visual inspection. For example, in <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-17</a></span> (1968), we stated that a “careful [tactile] exploration of the outer surfaces of a person’s clothing all over his or her body” is a “serious intrusion upon the sanctity of the person, which may inflict great indignity and arouse strong resentment, and it is not to be undertaken lightly.” Although Agent Cantu did not “frisk” petitioner’s person, he did conduct a probing tactile examination of petitioner’s carry-on luggage. Obviously, petitioner’s bag was not part of his person. But travelers are particularly concerned <page-number citation-index="1" label="338">*338</page-number>about their earry-on luggage; they generally use it to transport personal items that, for whatever reason, they prefer to keep close at hand.</p>
<p id="b414-4">Here, petitioner concedes that, by placing his bag in the overhead compartment, he could expect that it would be exposed to certain kinds of touching and handling. But petitioner argues that Agent Cantu’s physical manipulation of his luggage “far exceeded the casual contact [petitioner] could have expected from other passengers.” Brief for Petitioner 18-19. The Government counters that it did not.</p>
<p id="b414-5">Our Fourth Amendment analysis embraces two questions. First, we ask whether the individual, by his conduct, has exhibited an actual expectation of privacy; that is, whether he has shown that “he [sought] to preserve [something] as private.” <em>Smith </em>v. <em>Maryland, </em><span class="citation multiple-matches"><a href="/c/U.%20S./442/785/">442 U. S. 785</a></span>, 740 (1979) (internal quotation marks omitted). Here, petitioner sought to preserve privacy by using an opaque bag and placing that bag directly above his seat. Second, we inquire whether the individual’s expectation of privacy is “one that society is prepared to recognize as reasonable.” <em>Ibid, </em>(internal quotation marks omitted).<footnotemark>2</footnotemark> When a bus passenger places a bag in an overhead bin, he expects that other passengers or bus employees may move it for one reason or another. Thus, a bus passenger clearly expects that his bag may be handled. He does not expect that other passengers or bus employees will, <page-number citation-index="1" label="339">*339</page-number>as a matter of course, feel the bag in an exploratory manner. But this is exactly what the agent did here. We therefore hold that the agent’s physical manipulation of petitioner’s bag violated the Fourth Amendment.</p>
<p id="b415-5">The judgment of the Court of Appeals is</p>
<p id="b415-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b412-7"> The Government has not argued here that petitioner’s consent to Agent Cantu’s opening the bag is a basis for admitting the evidence.</p>
</footnote>
<footnote label="2">
<p id="b414-6"> The parties properly agree that the subjective intent of the law enforcement officer is irrelevant in determining whether that officer’s actions violate the Fourth Amendment. Brief for Petitioner 14; Brief for United States 33-34; see <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813</a></span> (1996) (stating that “we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers”); <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#212" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 212</a></span> (1986) (rejecting respondent’s challenge to “the authority of government to observe his activity from any vantage point or place if the viewing is motivated by a law enforcement purpose, and not the result of a casual, accidental observation”). This principle applies to the agent’s acts in this case as well; the issue is not his state of mind, but the objective effect of his actions.</p>
</footnote>
</opinion>
```

---
