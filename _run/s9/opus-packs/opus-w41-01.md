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

## GROUP: content/cases/United States v. James Daniel Good Real Property.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. James Daniel Good Real Property
type: case
citation: "510 U.S. 43 (1993)"
parallel_cite: "114 S. Ct. 492; 126 L. Ed. 2d 490; 7 Fla. L. Weekly Fed. S 665; 93 Daily Journal DAR 15706; 62 U.S.L.W. 4013"
neutral_cite: "1993 U.S. LEXIS 7941; 93 Cal. Daily Op. Serv. 9143; 1993 WL 505539"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-12-13
docket: No. 92-1180
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
  opinion_url: "https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/"
  cluster_id: 112914
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. James Daniel Good Real Property
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
  - real-property
  - notice-and-hearing
  - exigent-circumstances
holding: "Absent exigent circumstances, the Due Process Clause of the Fifth Amendment requires the Government to give the owner notice and a meaningful opportunity to be heard before seizing real property in a civil forfeiture; separately, filing the forfeiture action within the five-year statute of limitations makes it timely, and non-compliance with the customs laws' internal reporting deadlines does not require dismissal."
aliases:
  - United States v. James Daniel Good Real Property
  - United States v. James Daniel Good
  - "United States v. James Daniel Good Real Property (1993)"
---

# United States v. James Daniel Good Real Property

*510 U.S. 43 (1993)* (No. 92-1180) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112914 → combined opinion 112914 (Kennedy, J.; 510 U.S. 43, argued Oct. 6, 1993, decided Dec. 13, 1993). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*62` and `*63`, i.e., on page 62). S9 promotes. -->

## Background
In January 1985, Hawaii police searched James Daniel Good's home and found about 89 pounds of marijuana and related contraband; Good later pleaded guilty to a state drug offense and was sentenced. Roughly four and a half years later, in August 1989, the United States filed an *in rem* action to forfeit Good's house and its four-acre parcel under 21 U.S.C. § 881(a)(7). A magistrate found probable cause in an *[[Common Legal Terms#ex-parte|ex parte]]* proceeding, and the Government seized the property without any prior notice to Good or an adversary hearing, redirecting the tenants' rent to the U.S. Marshal. Good challenged the seizure as a denial of due process and argued the action was untimely. The District Court granted summary judgment for the Government; the Ninth Circuit held the no-notice seizure unconstitutional but also held the action untimely for failing certain internal reporting deadlines.

## Issue
Whether, absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], the Due Process Clause permits the Government to seize real property for civil forfeiture without prior notice and a hearing; and whether a forfeiture filed within the [[Common Legal Terms#statute-of-limitations|statute of limitations]] must be dismissed for failing to meet the customs laws' internal timing directives.

## Rule
On the constitutional question, the Court applied the general due-process rule that the Government must afford notice and an opportunity to be heard before depriving a person of property, and found no extraordinary justification for dispensing with it when the property is real estate — which cannot abscond and can be secured by less drastic means (a *lis pendens*, restraining order, or bond). It held: "Unless exigent circumstances are present, the Due Process Clause requires the Government to afford notice and a meaningful opportunity to be heard before seizing real property subject to civil forfeiture." — 510 U.S. at 62. ^pin-62

## Application
Because the Government sought only to preserve the property pending forfeiture — not to seize contraband or protect the public — nothing about a house and land presented the kind of [[Exigent Circumstances and Hot Pursuit|exigency]] that could justify skipping pre-seizure process; less restrictive measures would protect the Government's interests. That Good had already been convicted did not matter, since fair procedures are not confined to the innocent and the issue was the legality of the seizure, not the strength of the Government's case. On the separate timeliness question, the Court held that filing within the five-year limitations period made the action timely: where a statute sets internal reporting deadlines but no consequence for missing them, courts will not invent dismissal as a sanction.

## Conclusion
The Court **affirmed** the Ninth Circuit's due-process ruling and **reversed** its ruling that the action was untimely. Kennedy, J., delivered the opinion of the Court. Rehnquist, C.J. (joined by Scalia, J., and in part by O'Connor, J.), and O'Connor and Thomas, JJ., each filed opinions concurring in part and dissenting in part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *James Daniel Good* is the pre-deprivation-process anchor for civil forfeiture: the Government must ordinarily give notice and a hearing *before* seizing real property, unless it proves genuine [[Exigent Circumstances and Hot Pursuit|exigency]]. Teach it against *[[United States v. $8,850 in Currency]]* (1983), which governs the different question of how long the Government may wait to *file* a forfeiture action after a seizure (the *Barker v. Wingo* factors).

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. James Daniel Good Real Property*, 510 U.S. 43 (1993)](https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/) — pinpoint: 62 (Kennedy, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*62` and `*63`, i.e., on page 62). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2239cbde6d7624f9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "510 U.S. 43 (1993)", "court": "U.S. Supreme Court", "neutral_cite": "1993 U.S. LEXIS 7941; 93 Cal. Daily Op. Serv. 9143; 1993 WL 505539", "official_citation_present": true, "parallel_cite": "114 S. Ct. 492; 126 L. Ed. 2d 490; 7 Fla. L. Weekly Fed. S 665; 93 Daily Journal DAR 15706; 62 U.S.L.W. 4013", "title": "United States v. James Daniel Good Real Property", "year": "1993"}}
{"assertion_id": "0934982d210890c9", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "United States v. James Daniel Good Real Property"}}
{"assertion_id": "cf9ef0be218d4fbb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Absent exigent circumstances, the Due Process Clause of the Fifth Amendment requires the Government to give the owner notice and a meaningful opportunity to be heard before seizing real property in a civil forfeiture; separately, filing the forfeiture action within the five-year statute of limitations makes it timely, and non-compliance with the customs laws' internal reporting deadlines does not require dismissal.", "title": "United States v. James Daniel Good Real Property"}}
{"assertion_id": "9a151c964a6d84ae", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. James Daniel Good Real Property"}}
{"assertion_id": "b9f575be06de1909", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. James Daniel Good Real Property", "varies_by_point": "false"}}
```

### lake record — United States v. James Daniel Good Real Property

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. James Daniel Good Real Property",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. James Daniel Good Real Property",
    "case_name_short": "James Daniel Good ",
    "case_name_full": "UNITED STATES v. JAMES DANIEL GOOD REAL PROPERTY Et Al.",
    "input_case_name": "United States v. James Daniel Good Real Property",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-12-13",
    "year": 1993,
    "docket": "No. 92-1180",
    "cluster_id": 112914,
    "lead_opinion_id": 9432907,
    "sibling_ids": [],
    "absolute_url": "/opinion/112914/united-states-v-james-daniel-good-real-property/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "510 U.S. 43",
      "volume": "510",
      "reporter": "U.S.",
      "page": "43",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "510 U.S. 43",
        "volume": "510",
        "reporter": "U.S.",
        "page": "43",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "510 U.S. 43",
    "official_selection": {
      "court_class": "scotus",
      "selected": "510 U.S. 43",
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
    "date_created": "2026-07-06T13:16:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-james-daniel-good-real-property--112914",
      "to_record_id": "United States v. James Daniel Good Real Property",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. James Daniel Good Real Property

```
<opinion type="majority">
<author id="Afh"><page-number citation-index="1" label="46">*46</page-number>Justice Kennedy</author>
<p id="AYL">delivered the opinion of the Court.</p>
<p id="ASH">The principal question presented is whether, in the absence of exigent circumstances, the Due Process Clause of the Fifth Amendment prohibits the Government in a civil forfeiture case from seizing real property without first affording the owner notice and an opportunity to be heard. We hold that it does.</p>
<p id="AZ2">A second issue in the case concerns the timeliness of the forfeiture action. We hold that filing suit for forfeiture within the statute of limitations suffices to make the action timely, and that the cause should not be dismissed for failure to comply with certain other statutory directives for expeditious prosecution in forfeiture cases.</p>
<p id="A9v">I.</p>
<p id="Ax">On January 31, 1985, Hawaii police officers executed a search warrant at the home of claimant James Daniel Good. The search uncovered about 89 pounds of marijuana, marijuana seeds, vials containing hashish oil, and drug paraphernalia. About six months later, Good pleaded guilty to promoting a harmful drug in the second degree, in violation of Hawaii law. <span class="citation no-link">Haw. Rev. Stat. § 712-1245</span>(l)(b) (1985). He was sentenced to one year in jail and five years’ probation, and fined $1,000. Good was also required to forfeit to the State $3,187 in cash found on the premises.</p>
<p id="Aq7">On August 8, 1989, 4V2 years after the drugs were found, the United States filed an <em>in rem </em>action in the United States District Court for the District of Hawaii, seeking to forfeit Good’s house and the 4-acre parcel on which it was situated. The United States sought forfeiture under <span class="citation no-link">21 U. S. C. § 881</span>(a)(7), on the ground that the property had been used to commit or facilitate the commission of a federal drug offense.<footnotemark>1</footnotemark></p>
<p id="b251-4"><page-number citation-index="1" label="47">*47</page-number>On August 18, 1989, in an <em>ex parte </em>proceeding, a United States Magistrate Judge found that the Government had established probable cause to believe Good’s property was subject to forfeiture under § 881(a)(7). A warrant of arrest <em>in rem </em>was issued, authorizing seizure of the property. The warrant was based on an affidavit recounting the fact of Good’s conviction and the evidence discovered during the January 1985 search of his home by Hawaii police.</p>
<p id="b251-5">The Government seized the property on August 21, 1989, without prior notice to Good or an adversary hearing. At the time of the seizure, Good was renting his home to tenants for $900 per month. The Government permitted the tenants to remain on the premises subject to an occupancy agreement, but directed the payment of future rents to the United States Marshal.</p>
<p id="b251-6">Good filed a claim for the property and an answer to the Government’s complaint. He asserted that the seizure deprived him of his property without due process of law and that the forfeiture action was invalid because it had not been timely commenced under the statute. The District Court granted the Government’s motion for summary judgment and entered an order forfeiting the property.</p>
<p id="b251-7">The Court of Appeals for the Ninth Circuit affirmed in part, reversed in part, and remanded for further proceedings. <span class="citation multiple-matches"><a href="/c/F.%202d/971/1376/">971 F. 2d 1376</a></span> (1992). The court was unanimous in holding that the seizure of Good’s property, without prior notice and a hearing, violated the Due Process Clause.</p>
<p id="b252-3"><page-number citation-index="1" label="48">*48</page-number>In a divided decision, the Court of Appeals further held that the District Court erred in finding the action timely. The Court of Appeals ruled that the 5-year statute of limitations in <span class="citation no-link">19 U. S. C. § 1621</span> is only an “outer limit” for filing a forfeiture action, and that further limits are imposed by <span class="citation no-link">19 U. S. C. §§ 1602-1604</span>. 971 F. 2d, at 1378-1382. Those provisions, the court reasoned, impose a “series of internal notification and reporting requirements,” under which “customs agents must report to customs officers, customs officers must report to the United States attorney, and the Attorney General must ‘immediately’ and ‘forthwith’ bring a forfeiture action if he believes that one is warranted.” <em>Id., </em>at 1379 (citations omitted). The Court of Appeals ruled that failure to comply with these internal reporting rules could require dismissal of the forfeiture action as untimely. The court remanded the case for a determination whether the Government had satisfied its obligation to make prompt reports. <em>Id., </em>at 1382.</p>
<p id="b252-4">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./507/983/">507 U. S. 983</a></span> (1993), to resolve a conflict among the Courts of Appeals on the constitutional question presented. Compare <em>United States </em>v. <em>Premises and Real Property at 4492 South Livonia Road, </em><span class="citation" data-id="8975191"><a href="/opinion/8983256/united-states-v-4492-south-livonia-road/" aria-description="Citation for case: United States v. 4492 South Livonia Road">889 F. 2d 1258</a></span> (CA2 1989), with <em>United States </em>v. <em>A Single Family Residence and Real Property, </em><span class="citation" data-id="478062"><a href="/opinion/478062/united-states-v-a-single-family-residence-and-real-property-located-at-900/" aria-description="Citation for case: United States v. A Single Family Residence and Real...">803 F. 2d 625</a></span> (CA11 1986). We now affirm the due process ruling and reverse the ruling on the timeliness question.</p>
<p id="b252-5">II</p>
<p id="b252-6">The Due Process Clause of the Fifth Amendment guarantees that “[n]o person shall ... be deprived of life, liberty, or property, without due process of law.” Our precedents establish the general rule that individuals must receive notice and an opportunity to be heard before the Government deprives them of property. See <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S. 555, 562, n. 12</a></span> (1983); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#82" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 82</a></span> (1972); <em>Sniadach </em>v. <em>Family Finance Corp. of Bay View, </em><page-number citation-index="1" label="49">*49</page-number><span class="citation" data-id="9424067"><a href="/opinion/107960/sniadach-v-family-finance-corp-of-bay-view/#342" aria-description="Citation for case: Sniadach v. Family Finance Corp. of Bay View">395 U. S. 337, 342</a></span> (1969) (Harlan, J., concurring); <em>Mullane </em>v. <em>Central Hanover Bank &amp; Trust Co., </em><span class="citation" data-id="9420472"><a href="/opinion/104786/mullane-v-central-hanover-bank-trust-co/#313" aria-description="Citation for case: Mullane v. Central Hanover Bank &amp; Trust Co.">339 U. S. 306, 313</a></span> (1950).</p>
<p id="b253-5">The Government does not, and could not, dispute that the seizure of Good’s home and 4-acre parcel deprived him of property interests protected by the Due Process Clause. By the Government’s own submission, the seizure gave it the right to charge rent, to condition occupancy, and even to evict the occupants. Instead, the Government argues that it afforded Good all the process the Constitution requires. The Government makes two separate points in this regard. First, it contends that compliance with the Fourth Amendment suffices when the Government seizes property for purposes of forfeiture. In the alternative, it argues that the seizure of real property under the drug forfeiture laws justifies an exception to the usual due process requirement of preseizure notice and hearing. We turn to these issues.</p>
<p id="b253-6">A</p>
<p id="b253-7">The Government argues that because civil forfeiture serves a “law enforcement purpos[e],” Brief for United States 13, the Government need comply only with the Fourth Amendment when seizing forfeitable property. We disagree. The Fourth Amendment does place restrictions on seizures conducted for purposes of civil forfeiture, <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#696" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 696</a></span> (1965) (holding that the exclusionary rule applies to civil forfeiture), but it does not follow that the Fourth Amendment is the sole constitutional provision in question when the Government seizes property subject to forfeiture.</p>
<p id="b253-8">We have rejected the view that the applicability of one constitutional amendment pre-empts the guarantees of another. As explained in <em>Soldal </em>v. <em>Cook County, </em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#70" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 70</a></span> (1992):</p>
<blockquote id="b253-9">“Certain wrongs affect more than a single right and, accordingly, can implicate more than one of the Constitution’s commands. Where such multiple violations <page-number citation-index="1" label="50">*50</page-number>are alleged, we are not in the habit of identifying as a preliminary matter the claim’s ‘dominant’ character. Rather, we examine each constitutional provision in turn.”</blockquote>
<p id="b254-4">Here, as in <em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Soldal</a></span>, </em>the seizure of property implicates two “ ‘explicit textual source[s] of constitutional protection,’ ” the Fourth Amendment and the Fifth. <em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Ibid.</a></span> </em>The proper question is not which Amendment controls but whether either Amendment is violated.</p>
<p id="b254-5">Nevertheless, the Government asserts that when property is seized for forfeiture, the Fourth Amendment provides the full measure of process due under the Fifth. The Government relies on <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), and <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), in support of this proposition. That reliance is misplaced. <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>and <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span> </em>concerned not the seizure of property but the arrest or detention of criminal suspects, subjects we have considered to be governed by the provisions of the Fourth Amendment without reference to other constitutional guarantees. In addition, also unlike the seizure presented by this case, the arrest or detention of a suspect occurs as part of the regular criminal process, where other safeguards ordinarily ensure compliance with due process.</p>
<p id="b254-6"><em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>held that the Fourth Amendment, rather than the Due Process Clause, determines the requisite postarrest proceedings when individuals are detained on criminal charges. Exclusive reliance on the Fourth Amendment is appropriate in the arrest context, we explained, because the Amendment was “tailored explicitly for the criminal justice system,” and its “balance between individual and public interests always has been thought to define the ‘process that is due’ for seizures of person or property in criminal cases.” <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 125, n. 27</a></span>. Furthermore, we noted that the protections afforded during an arrest and initial detention are “only the <em>first </em>stage of an elaborate system, unique in jurisprudence, <page-number citation-index="1" label="51">*51</page-number>designed to safeguard the rights of those accused of criminal conduct.” <em>Ibid, </em>(emphasis in original).</p>
<p id="b255-5">So too, in <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span> </em>we held that claims of excessive force in the course of an arrest or investigatory stop should be evaluated under the Fourth Amendment reasonableness standard, not under the “more generalized notion of ‘substantive due process.’” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor">490 U.S., at 395</a></span>. Because the degree of force used to effect a seizure is one determinant of its reasonableness, and because the Fourth Amendment guarantees citizens the right “to be secure in their persons . . . against unreasonable . . . seizures,” we held that a claim of excessive force in the course of such a seizure is “most properly characterized as one invoking the protections of the Fourth Amendment.” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor"><em>Id., </em>at 394</a></span>.</p>
<p id="b255-6">Neither <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>nor <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>, </em>however, provides support for the proposition that the Fourth Amendment is the beginning and end of the constitutional inquiry whenever a seizure occurs. That proposition is inconsistent with the approach we took in <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), which examined the constitutionality of <em>ex parte </em>seizures of forfeitable property under general principles of due process, rather than the Fourth Amendment. And it is at odds with our reliance on the Due Process Clause to analyze prejudgment seizure and sequestration of personal property. See, <em>e. g., Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <em>Mitchell </em>v. <em>W. T. Grant Co., </em><span class="citation" data-id="9425706"><a href="/opinion/109023/mitchell-v-w-t-grant-co/" aria-description="Citation for case: Mitchell v. W. T. Grant Co.">416 U. S. 600</a></span> (1974).</p>
<p id="b255-7">It is true, of course, that the Fourth Amendment applies to searches and seizures in the civil context and may serve to resolve the legality of these governmental actions without reference to other constitutional provisions. See <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (holding that a warrant based on probable cause is required for administrative search of residences for safety inspections); <em>Skinner </em>v. <em>Railway Labor Executives' Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (holding that federal regulations authorizing railroads to conduct blood and urine tests of cer<page-number citation-index="1" label="52">*52</page-number>tain employees, without a warrant and without reasonable suspicion, do not violate the Fourth Amendment prohibition against unreasonable searches and seizures). But the purpose and effect of the Government’s action in the present case go beyond the traditional meaning of search or seizure. Here the Government seized property not to preserve evidence of wrongdoing, but to assert ownership and control over the property itself. Our cases establish that government action of this consequence must comply with the Due Process Clauses of the Fifth and Fourteenth Amendments.</p>
<p id="b256-4">Though the Fourth Amendment places limits on the Government’s power to seize property for purposes of forfeiture, it does not provide the sole measure of constitutional protection that must be afforded property owners in forfeiture proceedings. So even assuming that the Fourth Amendment were satisfied in this case, it remains for us to determine whether the seizure complied with our well-settled jurisprudence under the Due Process Clause.</p>
<p id="b256-5">B</p>
<p id="b256-6">Whether <em>ex parte </em>seizures of forfeitable property satisfy the Due Process Clause is a question we last confronted in <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., supra, </em>which held that the Government could seize a yacht subject to civil forfeiture without affording prior notice or hearing. Central to our analysis in <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>was the fact that a yacht was the “sort [of property] that could be removed to another jurisdiction, destroyed, or concealed, if advance warning of confiscation were given.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#679" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Id., </em>at 679</a></span>. The ease with which an owner could frustrate the Government’s interests in the forfeitable property created a “ ‘special need for very prompt action’ ” that justified the postponement of notice and hearing until after the seizure. <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Id.,</a></span> </em>at 678 (quoting <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin"><em>Fuentes, supra, </em>at 91</a></span>).</p>
<p id="b256-7">We had no occasion in <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>to decide whether the same considerations apply to the forfeiture of real property, <page-number citation-index="1" label="53">*53</page-number>which, by its very nature, can be neither moved nor concealed. In fact, when <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>was decided, both the Puerto Rican statute, P. R. Laws Ann., Tit. 24, §2512 (Supp. 1973), and the federal forfeiture statute upon which it was modeled, <span class="citation no-link">21 U. S. C. § 881</span> (1970 ed.), authorized the forfeiture of personal property only. It was not until 1984, 10 years later, that Congress amended § 881 to authorize the forfeiture of real property. See <span class="citation no-link">21 U. S. C. § 881</span>(a)(7); <span class="citation no-link">Pub. L. 98-473, §306</span>, <span class="citation no-link">98 Stat. 2050</span>.</p>
<p id="b257-5">The right to prior notice and a hearing is central to the Constitution’s command of due process. “The purpose of this requirement is not only to ensure abstract fair play to the individual. Its purpose, more particularly, is to protect his use and possession of property from arbitrary encroachment — to minimize substantively unfair or mistaken deprivations of property . . . .” <em>Fuentes, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#80" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 80-81</a></span>.</p>
<p id="b257-6">We tolerate some exceptions to the general rule requiring predeprivation notice and hearing, but only in “‘extraordinary situations where some valid governmental interest is at stake that justifies postponing the hearing until after the event.’” <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Id.,</a></span> </em>at 82 (quoting <em>Boddie </em>v. <em>Connecticut, </em><span class="citation" data-id="9424471"><a href="/opinion/108281/boddie-v-connecticut/#379" aria-description="Citation for case: Boddie v. Connecticut">401 U. S. 371, 379</a></span> (1971)); <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 562, n. 12</a></span>. Whether the seizure of real property for purposes of civil forfeiture justifies such an exception requires an examination of the competing interests at stake, along with the promptness and adequacy of later proceedings. The three-part inquiry set forth in <em>Mathews </em>v. <em>Eldridge, </em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">424 U. S. 319</a></span> (1976), provides guidance in this regard. The <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span> </em>analysis requires us to consider the private interest affected by the official action; the risk of an erroneous deprivation of that interest through the procedures used, as well as the probable value of additional safeguards; and the Government’s interest, including the administrative burden that additional procedural requirements would impose. <span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/#335" aria-description="Citation for case: Mathews v. Eldridge"><em>Id., </em>at 335</a></span>.</p>
<p id="b257-7">Good’s right to maintain control over his home, and to be free from governmental interference, is a private interest of <page-number citation-index="1" label="54">*54</page-number>historic and continuing importance. Cf. <em>United States </em>v. <em>Karo, </em><span class="citation no-link">468 U. S. 706</span>, 714-716 (1984); <em>Payton </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./446/673/">446 U. S. 673</a></span>, 690 (1980). The seizure deprived Good of valuable rights of ownership, including the right of sale, the right of occupancy, the right to unrestricted use and enjoyment, and the right to receive rents. All that the seizure left him, by the Government’s own submission, was the right to bring a claim for the return of title at some unscheduled future hearing.</p>
<p id="b258-4">In <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Fuentes</a></span>, </em>we held that the loss of kitchen appliances and household furniture was significant enough to warrant a predeprivation hearing. <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#70" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 70-71</a></span>. And in <em>Connecticut </em>v. <em>Doehr, </em><span class="citation" data-id="9432319"><a href="/opinion/112615/connecticut-v-doehr/" aria-description="Citation for case: Connecticut v. Doehr">501 U. S. 1</a></span> (1991), we held that a state statute authorizing prejudgment attachment of real estate without prior notice or hearing was unconstitutional, in the absence of extraordinary circumstances, even though the attachment did not interfere with the owner’s use or possession and did not affect, as a general matter, rentals from existing leaseholds.</p>
<p id="b258-5">The seizure of a home produces a far greater deprivation than the loss of furniture, or even attachment. It gives the Government not only the right to prohibit sale, but also the right to evict occupants, to modify the property, to condition occupancy, to receive rents, and to supersede the owner in all rights pertaining to the use, possession, and enjoyment of the property.</p>
<p id="b258-6">The Government makes much of the fact that Good was renting his home to tenants, and contends that the tangible effect of the seizure was limited to taking the $900 a month he was due in rent. But even if this were the only deprivation at issue, it'would not render the loss insignificant or unworthy of due process protection. The rent represents a significant portion of the exploitable economic value of Good’s home. It cannot be classified as <em>de minimis </em>for purposes of procedural due process. In sum, the private <page-number citation-index="1" label="55">*55</page-number>interests at stake in the seizure of real property weigh heavily in the <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span> </em>balance.</p>
<p id="b259-5">The practice of <em>ex parte </em>seizure, moreover, creates an unacceptable risk of error. Although Congress designed the drug forfeiture statute to be a powerful instrument in enforcement of the drug laws, it did not intend to deprive innocent owners of their property. The affirmative defense of innocent ownership is allowed by statute. See <span class="citation no-link">21 U. S. C. § 881</span>(a)(7) (“[N]o property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner”).</p>
<p id="b259-6">The <em>ex parte </em>preseizure proceeding affords little or no protection to the innocent owner. In issuing a warrant of seizure, the magistrate judge need determine only that there is probable cause to believe that the real property was “used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of,” a felony narcotics offense. <em><span class="citation no-link">Ibid.</span> </em>The Government is not required to offer any evidence on the question of innocent ownership or other potential defenses a claimant might have. See, <em>e. g., Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U. S. 602</a></span> (1993) (holding that forfeitures under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7) are subject to the limitations of the Excessive Fines Clause). Nor would that inquiry, in the <em>ex parte </em>stage, suffice to protect the innocent owner’s interests. “[Fjairness cán rarely be obtained by secret, one-sided determination of facts decisive of rights. ... No better instrument has been devised for arriving at truth than to give a person in jeopardy of serious loss notice of the case against him and opportunity to meet it.” <em>Joint Anti-Fascist Refugee Comm. </em>v. <em>McGrath, </em><span class="citation" data-id="9420571"><a href="/opinion/104894/joint-anti-fascist-refugee-committee-v-mcgrath/#170" aria-description="Citation for case: Joint Anti-Fascist Refugee Committee v. McGrath">341 U. S. 123, 170-172</a></span> (1951) (Frankfurter, J., concurring) (footnotes omitted).</p>
<p id="b259-7">The purpose of an adversary hearing is to ensure the requisite neutrality that must inform all governmental decision-making. That protection is of particular importance here, <page-number citation-index="1" label="56">*56</page-number>where the Government has a direct pecuniary interest in the outcome of the proceeding.<footnotemark>2</footnotemark> See <em>Harmelin </em>v. <em>Michigan, </em><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/#979" aria-description="Citation for case: Harmelin v. Michigan">501 U. S. 957, 979, n. 9</a></span> (1991) (opinion of Scalia, J.) (“[I]t makes sense to scrutinize governmental action more closely when the State stands to benefit”). Moreover, the availability of a postseizure hearing may be no recompense for losses caused by erroneous seizure. Given the congested civil dockets in federal courts, a claimant may not receive an adversary hearing until many months after the seizure. And even if the ultimate judicial decision is that the claimant was an innocent owner, or that the Government lacked' probable cause, this determination, coming months after the seizure, “would not cure the temporary deprivation that an earlier hearing might have prevented.” <em>Doehr, </em><span class="citation" data-id="9432319"><a href="/opinion/112615/connecticut-v-doehr/#15" aria-description="Citation for case: Connecticut v. Doehr">501 U. S., at 15</a></span>.</p>
<p id="b260-4">This brings us to the third consideration under <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span>, </em>“the Government’s interest, including the function involved and the fiscal and administrative burdens that the additional or substitute procedural requirement would entail.” <span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/#335" aria-description="Citation for case: Mathews v. Eldridge">424 U. S., at 335</a></span>. The governmental interest we consider here is not some general interest in forfeiting property but the specific interest in seizing real property before the forfeiture hearing. The question in the civil forfeiture context is whether <em>ex parte </em>seizure is justified by a pressing need for prompt action. See <em>Fuentes, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 91</a></span>. We find no pressing need here.</p>
<p id="b261-4"><page-number citation-index="1" label="57">*57</page-number>This is apparent by comparison to <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span>, </em>where the Government’s interest in immediate, seizure of a yacht subject to civil forfeiture justified dispensing with the usual requirement of prior notice and hearing. Two essential considerations informed our ruling in that case: First, immediate seizure was necessary to establish the court’s jurisdiction over the property, 416 U. S., at 679, and second, the yacht might have disappeared had the Government given advance warning of the forfeiture action, <em>ibid. </em>See also <em>United States </em>v. <em>Von Neumann, </em><span class="citation" data-id="9430249"><a href="/opinion/111551/united-states-v-von-neumann/#251" aria-description="Citation for case: United States v. Von Neumann">474 U. S. 242, 251</a></span> (1986) (no preseizure hearing is required when customs officials seize an automobile at the border). Neither of these factors is present when the target of forfeiture is real property.</p>
<p id="b261-5">Because real property cannot abscond, the court’s jurisdiction can be preserved without prior seizure. It is true that seizure of the res has long been considered a prerequisite to the initiation of <em>in rem </em>forfeiture proceedings. See <em>Republic Nat. Bank of Miami </em>v. <em>United States, </em><span class="citation" data-id="9432701"><a href="/opinion/112797/republic-national-bank-of-miami-v-united-states/#84" aria-description="Citation for case: Republic National Bank of Miami v. United States">506 U. S. 80, 84</a></span> (1992); <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#363" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 363</a></span> (1984). This rule had its origins in the Court’s early admiralty cases, which involved the forfeiture of vessels and other movable personal property. See <em>Taylor </em>v. <em>Carryl, </em><span class="citation" data-id="9416646"><a href="/opinion/87188/james-l-v-carryl/#599" aria-description="Citation for case: James L. v. Carryl">20 How. 583, 599</a></span> (1858); <em>The Brig Ann, </em><span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/" aria-description="Citation for case: The Brig Ann, McLain, Master">9 Cranch 289</a></span> (1815); <em>Keene </em>v. <em>United States, </em><span class="citation" data-id="84912"><a href="/opinion/84912/keene-v-the-united-states/#310" aria-description="Citation for case: Keene v. The United States">5 Cranch 304, 310</a></span> (1809). Justice Story, writing for the Court in <em>The Brig Ann, </em>explained the justification for the rule as one of fixing and preserving jurisdiction: “[Bjefore judicial cognizance can attach upon a forfeiture <em>in rem, . . . </em>there must be a seizure; for until seizure it is impossible to ascertain what is the competent forum.” <span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/#291" aria-description="Citation for case: The Brig Ann, McLain, Master">9 Cranch, at 291</a></span>. But when the res is real property, rather than personal goods, the appropriate judicial forum may be determined without actual seizure.</p>
<p id="b261-6">As <em>The Brig Ann </em>held, all that is necessary “[i]n order to institute and perfect proceedings <em>in rem, </em>[is] that the thing should be actually or constructively within the reach of the Court.” <em><span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/" aria-description="Citation for case: The Brig Ann, McLain, Master">Ibid.</a></span> </em>And as we noted last Term, “[f]airly read, <page-number citation-index="1" label="58">*58</page-number><em>The Brig Ann </em>simply restates the rule that the court must have actual or constructive control of the res when an <em>in rem </em>forfeiture suit is initiated.” <em>Republic Nat </em>Bank, <em>supra, </em>at 87. In the case of real property, the res may be brought within the reach of the court simply by posting notice on the property and leaving a copy of the process with the occupant. In fact, the rules which govern forfeiture proceedings under § 881 already permit process to be executed on real property without physical seizure:</p>
<blockquote id="b262-4">“If the character or situation of the property is such that the taking of actual possession is impracticable, the marshal or other person executing the process shall affix a copy thereof to the property in a conspicuous place and leave a copy of the complaint and process with the person having possession or the person’s agent.” Rule E(4)(b), Supplemental Rules for Certain Admiralty and Maritime Claims.</blockquote>
<p id="APc">See also <em>United States </em>v. <em>TWP 17 R 4, Certain Real Property in Maine, </em><span class="citation" data-id="587573"><a href="/opinion/587573/united-states-v-twp-17-r-4-certain-real-property-in-maine-united-states/#986" aria-description="Citation for case: United States v. Twp 17 R 4, Certain Real Property in...">970 F. 2d 984, 986</a></span>, and n. 4 (CA1 1992).</p>
<p id="b262-6">Nor is the <em>ex parte </em>seizure of real property necessary to accomplish the statutory purpose of § 881(a)(7). The Government’s legitimate interests at the inception of forfeiture proceedings are to ensure that the property not be sold, destroyed, or used for further illegal activity prior to the forfeiture judgment. These legitimate interests can be secured without seizing the subject property.</p>
<p id="b262-7">Sale of the property can be prevented by filing a notice of <em>lis pendens </em>as authorized by state law when the forfeiture proceedings commence. <span class="citation no-link">28 U. S. C. § 1964</span>; and see <span class="citation no-link">Haw. Rev. Stat. § 684-51</span> (1985) <em>(lis pendens </em>provision). If there is evidence, in a particular case, that an owner is likely to destroy his property when advised of the pending action, the Government may obtain an <em>ex parte </em>restraining order, or other appropriate relief, upon a proper showing in district court. See Fed. Rule Civ. Proc. 65; <em>United States </em>v. <em>Prem</em><page-number citation-index="1" label="59">*59</page-number><em>ises and Real Property at 4492 South Livonia Road, </em><span class="citation" data-id="8975191"><a href="/opinion/8983256/united-states-v-4492-south-livonia-road/#1265" aria-description="Citation for case: United States v. 4492 South Livonia Road">889 F. 2d 1258, 1265</a></span> (CA2 1989). The Government’s policy of leaving occupants in possession of real property under an occupancy agreement pending the final forfeiture ruling demonstrates that there is no serious concern about destruction in the ordinary case. See Brief for United States 13, n. 6 (citing Directive No. 90-10 (Oct. 9, 1990), Executive Office for Asset Forfeiture, Office of Deputy Attorney General). Finally, the Government can forestall further illegal activity with search and arrest warrants obtained in the ordinary course.</p>
<p id="b263-5">In the usual case, the Government thus has various means, short of seizure, to protect its legitimate interests in forfeit-able real property. There is no reason to take the additional step of asserting control over the property without first affording notice and an adversary hearing.</p>
<p id="b263-6">Requiring the Government to postpone seizure until after an adversary hearing creates no significant administrative burden. A claimant is already entitled to an adversary hearing before a final judgment of forfeiture. No extra hearing would be required in the typical case, since the Government can wait until after the forfeiture judgment to seize the property. From an administrative standpoint it makes little difference whether that hearing is held before or after the seizure. And any harm that results from delay is minimal in comparison to the injury occasioned by erroneous seizure.</p>
<p id="b263-7">C</p>
<p id="b263-8">It is true that, in cases decided over a century ago, we permitted the <em>ex parte </em>seizure of real property when the Government was collecting debts or revenue. See, <em>e. g., Springer </em>v. <em>United States, </em><span class="citation" data-id="90272"><a href="/opinion/90272/springer-v-united-states/#593" aria-description="Citation for case: Springer v. United States">102 U. S. 586, 593-594</a></span> (1881); <em>Murray’s Lessee </em>v. <em>Hoboken Land &amp; Improvement Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856). Without revisiting these cases, it suffices to say that their apparent rationale — like that for allowing summary seizures during wartime, see <em>Stoehr </em>v. <em>Wallace, </em><span class="citation" data-id="99736"><a href="/opinion/99736/stoehr-v-wallace/" aria-description="Citation for case: Stoehr v. Wallace">255 <page-number citation-index="1" label="60">*60</page-number>U. S. 239</a></span> (1921); <em>Bowles </em>v. <em>Willingham, </em><span class="citation" data-id="9419466"><a href="/opinion/103952/bowles-v-willingham/" aria-description="Citation for case: Bowles v. Willingham">321 U. S. 503</a></span> (1944), and seizures of contaminated food, see <em>North American Cold Storage Co. </em>v. <em>Chicago, </em><span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (1908) — was one of executive urgency. “The prompt payment of taxes,” we noted, “may be vital to the existence of a government.” <span class="citation" data-id="90272"><a href="/opinion/90272/springer-v-united-states/#594" aria-description="Citation for case: Springer v. United States"><em>Springer, supra, </em>at 594</a></span>. See also <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352, n. 18</a></span> (1977) (“The rationale underlying [the revenue] decisions, of course, is that the very existence of government depends upon the prompt collection of the revenues”).</p>
<p id="b264-4">A like rationale justified the <em>ex parte </em>seizure of tax-delinquent distilleries in the late 19th century, see, <em>e. g., United States </em>v. <em>Stowell, </em><span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">133 U. S. 1</a></span> (1890); <em>Dobbins's Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395</a></span> (1878), since before passage of the Sixteenth Amendment, the Federal Government relied heavily on liquor, customs, and tobacco taxes to generate operating revenues. In 1902, for example, nearly 75 percent of total federal revenues — $479 million out of a total of $653 million — was raised from taxes on liquor, customs, and tobacco. See U. S. Bureau of Census, Historical Statistics of the United States, Colonial Times to the Present 1122 (1976).</p>
<p id="b264-5">The federal income tax code adopted in the first quarter of this century, however, afforded the taxpayer notice and an opportunity to be heard by the Board of Tax Appeals before the Government could seize property for nonpayment of taxes. See Revenue Act of 1921, <span class="citation no-link">42 Stat. 265</span>-266; Revenue Act of 1924, <span class="citation no-link">43 Stat. 297</span>. In <em>Phillips </em>v. <em>Commissioner, </em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589</a></span> (1931), the Court relied upon the availability, and adequacy, of these preseizure administrative procedures in holding that no judicial hearing was required prior to the seizure of property. <em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">Id.,</a></span> </em>at 597-599 (citing Act of Feb. 26, 1926, ch. 27, § 274(a), <span class="citation no-link">44 Stat. 9</span>, 55; Act of May 29, 1928, ch. 852, §§ 272(a), 601, <span class="citation no-link">45 Stat. 791</span>, 852, 872). These constraints on the Commissioner could be overridden, but only when the Commissioner made a determination that a jeopardy assessment was necessary. <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#598" aria-description="Citation for case: Phillips v. Commissioner">283 U. S., at 598</a></span>. Writing for a unani<page-number citation-index="1" label="61">*61</page-number>mous Court, Justice Brandéis explained that under the tax laws “[f]ormal notice of the tax liability is thus given; the Commissioner is required to answer; and there is a complete hearing <em>de novo </em>.... These provisions amply protect the [taxpayer] against improper administrative action.” <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#598" aria-description="Citation for case: Phillips v. Commissioner"><em>Id., </em>at 598-599</a></span>; see also <em>Commissioner </em>v. <em>Shapiro, </em><span class="citation" data-id="9426305"><a href="/opinion/109396/commissioner-v-shapiro/#631" aria-description="Citation for case: Commissioner v. Shapiro">424 U. S. 614, 631</a></span> (1976) (“[In] the <em>Phillips </em>case . .. the taxpayer’s assets could not have been taken or frozen . . . until he had either had, or waived his right to, a full and final adjudication of his tax liability before the Tax Court (then the Board of Tax Appeals)”).</p>
<p id="b265-5">Similar provisions remain in force today. The current Internal Revenue Code prohibits the Government from levying upon a deficient taxpayer’s property without first affording the taxpayer notice and an opportunity for a hearing, unless exigent circumstances indicate that delay will jeopardize the collection of taxes due. See <span class="citation no-link">26 U. S. C. §§6212</span>, 6213, 6851, 6861.</p>
<p id="b265-6">Just as the urgencies that justified summary seizure of property in the 19th century had dissipated by the time of <em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">Phillips</a></span>, </em>neither is there a plausible claim of urgency today to justify the summary seizure of real property under § 881(a)(7). Although the Government relies to some extent on forfeitures as a means of defraying law enforcement expenses, it does not, and we think could not, justify the prehearing seizure of forfeitable real property as necessary for the protection of its revenues.</p>
<p id="b265-7">D</p>
<p id="b265-8">The constitutional limitations we enforce in this case apply to real property in general, not simply to residences. That said, the case before us well illustrates an essential principle: Individual freedom finds tangible expression in property rights. At stake in this and many other forfeiture cases are the security and privacy of the home and those who take shelter within it.</p>
<p id="b266-3"><page-number citation-index="1" label="62">*62</page-number>Finally, the suggestion that this one claimant must lose because his conviction was known at the time of seizure, and because he raises an as applied challenge to the statute, founders on a bedrock proposition: Fair procedures are not confined to the innocent. The question before us is the legality of the seizure, not the strength of the Government’s case.</p>
<p id="b266-4">In sum, based upon the importance of the private interests at risk and the absence of countervailing Government needs, we hold that the seizure of real property under § 881(a)(7) is not one of those extraordinary instances that justify the postponement of notice and hearing. Unless exigent circumstances are present, the Due Process Clause requires the Government to afford notice and a meaningful opportunity to be heard before seizing real property subject to civil forfeiture.<footnotemark>3</footnotemark></p>
<p id="b266-5">To establish exigent circumstances, the Government must show that less restrictive <em>measures </em>— i. <em>e., </em>a <em>lis pendens, </em>restraining order, or bond — would not suffice to protect the Government’s interests in preventing the sale, destruction, or continued unlawful use of the real property. We agree with the Court of Appeals that no showing of exigent circumstances has been made in this case, and we affirm its ruling that the <em>ex parte </em>seizure of Good’s real property violated due process.</p>
<p id="b266-6">Ill</p>
<p id="b266-7">We turn now to the question whether a court must dismiss a forfeiture action that the Government filed within the stat<page-number citation-index="1" label="63">*63</page-number>ute of limitations, but without complying with certain other statutory timing directives.</p>
<p id="b267-5">Title <span class="citation no-link">21 U. S. C. § 881</span>(d) incorporates the “provisions of law relating to the seizure, summary and judicial forfeiture, and condemnation of property for violation of the customs laws.” The customs laws in turn set forth various timing requirements. Title <span class="citation no-link">19 U. S. C. § 1621</span> contains the statute of limitations: “No suit or action to recover any pecuniary penalty or forfeiture of property accruing under the customs laws shall be instituted unless such suit or action is commenced within five years after the time when the alleged offense was discovered.” All agree that the Government filed its action within the statutory period.</p>
<p id="b267-6">The customs laws also contain a series of internal requirements relating to the timing of forfeitures. Title <span class="citation no-link">19 U. S. C. § 1602</span> requires that a customs agent “report immediately” to a customs officer every seizure for violation of the customs laws, and every violation of the customs laws. Section 1603 requires that the customs officer “report promptly” such seizures or violations to the United States attorney. And § 1604 requires the Attorney General “forthwith to cause the proper proceedings to be commenced” if it appears probable that any fine, penalty, or forfeiture has been incurred. The Court of Appeals held, over a dissent, that failure to comply with these internal timing requirements mandates dismissal of the forfeiture action. We disagree.</p>
<p id="b267-7">We have long recognized that “many statutory requisitions intended for the guide of officers in the conduct of business devolved upon them ... do not limit their power or render its exercise in disregard of the requisitions ineffectual.” <em>French </em>v. <em>Edwards, </em><span class="citation" data-id="9416845"><a href="/opinion/88488/french-v-edwards/#511" aria-description="Citation for case: French v. Edwards">13 Wall. 506, 511</a></span> (1872). We have held that if a statute does not specify a consequence for noncompliance with statutory timing provisions, the federal courts will not in the ordinary course impose their own coercive sanction. See <em>United States </em>v. <em>Montalvo-Murillo, </em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#717" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S. 711, 717-721</a></span> (1990); <em>Brock </em>v. <em>Pierce County, </em><span class="citation" data-id="111668"><a href="/opinion/111668/brock-v-pierce-county/#259" aria-description="Citation for case: Brock v. Pierce County">476 U. S. 253, <page-number citation-index="1" label="64">*64</page-number>259-262</a></span> (1986); see also <em>St. Regis Mohawk Tribe </em>v. <em>Brock, </em><span class="citation" data-id="456178"><a href="/opinion/456178/st-regis-mohawk-tribe-new-york-v-william-e-brock-secretary-of-labor/#41" aria-description="Citation for case: St. Regis Mohawk Tribe, New York v. William E. Brock,...">769 F. 2d 37, 41</a></span> (CA2 1985) (Friendly, J.).</p>
<p id="b268-4">In <em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/" aria-description="Citation for case: United States v. Montalvo-Murillo">Montalvo-Murillo</a></span>, </em>for example, we considered the Bail Reform Act of 1984, which requires an “immediate]” hearing upon a pretrial detainee’s “first appearance before the judicial officer.” <span class="citation no-link">18 U. S. C. § 3142</span>(f). Because “[n]either the timing requirements nor any other part of the Act [could] be read to require, or even suggest, that a timing error must result in release of a person who should otherwise be detained,” we held that the federal courts could not release a person pending trial solely because the hearing had not been held “immediately.” <span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#716" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S., at 716-717</a></span>. We stated that “[t]here is no presumption or general rule that for every duty imposed upon the court or the Government and its prosecutors there must exist some corollary punitive sanction for departures or omissions, even if negligent.” <em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/" aria-description="Citation for case: United States v. Montalvo-Murillo">Id.,</a></span> </em>at 717 (citing <span class="citation" data-id="9416845"><a href="/opinion/88488/french-v-edwards/#511" aria-description="Citation for case: French v. Edwards"><em>French, supra, </em>at 511</a></span>). To the contrary, we stated that “[w]e dp not agree that we should, or can, invent a remedy to satisfy some perceived need to coerce the courts and the Government into complying with the statutory time limits.” <span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#721" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S., at 721</a></span>.</p>
<p id="b268-5">Similarly, in <em>Brock, supra, </em>we considered a statute requiring that the Secretary of Labor begin an investigation within 120 days of receiving information about the misuse of federal funds. The respondent there argued that failure to act within the specified time period divested the Secretary of authority to investigate a claim after the time limit had passed. We rejected that contention, relying on the fact that the statute did not specify a consequence for a failure to comply with the timing provision. <em>Id., </em>at 258-262.</p>
<p id="b268-6">Under our precedents, the failure of Congress to specify a consequence for noncompliance with the timing requirements of <span class="citation no-link">19 U. S. C. §§ 1602-1604</span> implies that Congress intended the responsible officials administering the Act to have discretion to determine what disciplinary measures are appropriate when their subordinates fail to discharge their statu<page-number citation-index="1" label="65">*65</page-number>tory duties. Examination of the structure and history of the internal timing provisions at issue in this case supports the conclusion that the courts should not dismiss a forfeiture action for noncompliance. Because § 1621 contains a statute of limitations — the usual legal protection against stale claims— we doubt Congress intended to require dismissal of a forfeiture action for noncompliance with the internal timing requirements of §§ 1602-1604. Cf. <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#563" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 563, n. 13</a></span>.</p>
<p id="b269-5">Statutes requiring customs officials to proceed with dispatch have existed at least since 1799. See Act of Mar. 2, 1799, § 89, <span class="citation no-link">1 Stat. 695</span>-696. These directives help to ensure that the Government is prompt in obtaining revenue from forfeited property. It would make little sense to interpret directives designed to ensure the expeditious collection of revenues in a way that renders the Government unable, in certain circumstances, to obtain its revenues at all.</p>
<p id="b269-6">We hold that courts may not dismiss a forfeiture action filed within the 5-year statute of limitations for noncompliance with the internal timing requirements of §§ 1602-1604. The Government filed the action in this case within the 5-year statute of limitations, and that sufficed to make it timely. We reverse the contrary holding of the Court of Appeals.</p>
<p id="b269-7">IV</p>
<p id="b269-8">The case is remanded for further proceedings consistent with this opinion.</p>
<p id="b269-9">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="AMq"> Title <span class="citation no-link">21 U. S. C. § 881</span>(a)(7) provides:</p>
<blockquote id="AOj">“(a) . . .</blockquote>
<blockquote id="AgD">“The following shall be subject to forfeiture to the United States and no property right shall exist in them:</blockquote>
<blockquote id="ATo"><page-number citation-index="1" label="47">*47</page-number>“(7) All real property, including any right, title, and interest (including any leasehold interest) in the whole of any lot or tract of land and any appurtenances or improvements, which is used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of, a violation of this subchapter punishable by more than one year’s imprisonment, except that no property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner.”</blockquote>
</footnote>
<footnote label="2">
<p id="b260-5"> The extent of the Government’s financial stake in drug forfeiture is apparent from a 1990 memo, in which the Attorney General urged United States Attorneys to increase the volume of forfeitures in order to meet the Department of Justice’s annual budget target:</p>
<p id="b260-6">“We must significantly increase production to reach our budget target.</p>
<p id="b260-7">“. . . Failure to achieve the $470 million projection would expose the Department’s forfeiture program to criticism and undermine confidence in our budget projections. Every effort must be made to increase forfeiture income during the remaining three months of [fiscal year] 1990.” Executive Office for United States Attorneys, U. S. Dept, of Justice, 38 United States Attorney’s Bulletin 180 (1990).</p>
</footnote>
<footnote label="3">
<p id="b266-8"> We do not address what sort of procedures are required for preforfeiture seizures of real property in the context of criminal forfeiture. See, <em>e. g., </em><span class="citation no-link">21 U. S. C. § 863</span>; <span class="citation no-link">18 U. S. C. § 1963</span> (1988 ed. and Supp. IV). We note, however, that the federal drug laws now permit seizure before entry of a criminal forfeiture judgment only where the Government persuades a district court that there is probable cause to believe that a protective order “may not be sufficient to assure the availability of the property for forfeiture.” <span class="citation no-link">21 U.S.C. § 863</span>(f).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Jones.md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Jones"
type: case
citation: "565 U.S. 400 (2012)"
parallel_cite: "132 S. Ct. 945; 181 L. Ed. 2d 911"
neutral_cite: 2012 U.S. LEXIS 1063
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-23
docket: 10-1259
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Jones
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/622304/united-states-v-jones/"
  cluster_id: 622304
  opinion_id: 9485324
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Key — Anchor"
  - page: "[[Real-Time Tracking]]"
    role: "Key — cross-ref (GPS trespass; mosaic concurrences)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — mosaic seed for Carpenter)"
related: ["[[Katz v. United States]]", "[[Carpenter v. United States]]", "[[Florida v. Jardines]]", "[[Olmstead v. United States]]", "[[United States v. Jacobsen]]"]
aliases: ["United States v. Jones (2012)", "United States v. Antoine Jones"]
tags: ["case", "fourth-amendment", "search-definition", "trespass-theory", "gps-tracking", "physical-intrusion"]
holding: "Installing a GPS tracker on a vehicle and monitoring it was a search under the revived trespass theory — physical intrusion on an 'effect' to obtain information; the controlling modern trespass-search case."
lake:
  record_id: United States v. Jones
  status: verified
  projected_at: 2026-07-06
---

# United States v. Jones

*565 U.S. 400 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating Antoine Jones for drug trafficking, agents installed a GPS tracking device on the undercarriage of a Jeep Jones used while it was parked in a public lot, then tracked the vehicle's movements for 28 days. The installation occurred outside the scope of the warrant they had obtained (wrong jurisdiction and after it expired), so it was treated as warrantless. The data tied Jones to a stash house, and he was convicted; the D.C. Circuit reversed, holding the tracking was an unconstitutional search.

## Issue
Whether the government's attachment of a GPS tracking device to a vehicle, and its use of that device to monitor the vehicle's movements on public roads, constitutes a "search" within the meaning of the Fourth Amendment.

## Rule
Yes — under a trespass-based theory of the Fourth Amendment. "We hold that the Government's installation of a GPS device on a target's vehicle, and its use of that device to monitor the vehicle's movements, constitutes a 'search.'" — 565 U.S. at 404. ^pin-404

The basis is physical intrusion on a constitutionally protected "effect": "The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a 'search' within the meaning of the Fourth Amendment when it was adopted." — *Id.* at 404–05. ^pin-404a

The trespass test survives alongside *[[Katz v. United States|Katz]]*: "the *Katz* reasonable-expectation-of-privacy test has been *added to*, not *substituted for*, the common-law trespassory test." — *Id.* at 409. ^pin-409

## Application
On these facts the GPS surveillance was a search. The agents physically attached the device to the Jeep — an "effect" — and did so "for the purpose of obtaining information" about its movements; that trespassory intrusion onto a protected area to gather information was itself a search, without regard to whether Jones had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his movements on public roads. The Court did not need to reach the *[[Katz v. United States|Katz]]* expectation-of-privacy question (or the *[[United States v. Knotts|Knotts]]* beeper line, which involved no trespass), because the common-law trespass theory independently resolved the case: installing and monitoring the device on Jones's vehicle was a Fourth Amendment search.

## Conclusion
Attaching and using the GPS device was a search; the D.C. Circuit's judgment reversing the conviction was affirmed. The Court left the reasonableness (warrant/exception) question for remand.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Jones* revives the common-law trespass test as one of the "two definitions of search" alongside the [[Katz v. United States]] privacy test; it anchors the property-based line later applied to the [[Curtilage|curtilage]] in [[Florida v. Jardines]] and informs the digital-privacy analysis of [[Carpenter v. United States]].

## Appears on
- [[Trespass]] — *Key — Anchor*
- [[Real-Time Tracking]] — *Key — cross-ref (GPS trespass; mosaic [[Common Legal Terms#concurring-opinion|concurrences]])*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — mosaic seed for Carpenter)*

## Sources
- *United States v. Jones*, 565 U.S. 400 (2012) — https://www.courtlistener.com/opinion/7350871/united-states-v-jones/ — pinpoints: 404, 409. (Lead majority opinion id 7268856.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ce0bfc36448f60ed", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 400 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 1063", "official_citation_present": true, "parallel_cite": "132 S. Ct. 945; 181 L. Ed. 2d 911", "title": "United States v. Jones", "year": "2012"}}
{"assertion_id": "3842e7757cf82a53", "dimension": "support", "kind": "home_role", "locator": {"home": "Real-Time Tracking"}, "payload": {"home": "Real-Time Tracking", "role": "Key — cross-ref (GPS trespass; mosaic concurrences)", "title": "United States v. Jones"}}
{"assertion_id": "c6623d8c14949f5e", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Key — Anchor", "title": "United States v. Jones"}}
{"assertion_id": "ee5e95fe0cb2c24a", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-ref — mosaic seed for Carpenter)", "title": "United States v. Jones"}}
{"assertion_id": "f1e427d2cc9eba8b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Installing a GPS tracker on a vehicle and monitoring it was a search under the revived trespass theory — physical intrusion on an 'effect' to obtain information; the controlling modern trespass-search case.", "title": "United States v. Jones"}}
{"assertion_id": "88b6b4925ed52e7b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-01-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Jones", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Jones", "varies_by_point": "false"}}
{"assertion_id": "b45a7c4087b20a4c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Jones"}}
```

### lake record — United States v. Jones

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Jones",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Jones",
    "case_name_short": "Jones",
    "case_name_full": "United States v. Jones",
    "input_case_name": "United States v. Jones",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-23",
    "year": 2012,
    "docket": "10-1259",
    "cluster_id": 622304,
    "lead_opinion_id": 9485324,
    "sibling_ids": [
      622304,
      9485324,
      9485325,
      9485326
    ],
    "absolute_url": "/opinion/622304/united-states-v-jones/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 7350871,
        "score": 120,
        "case_name": "United States v. Jones"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 400",
      "volume": "565",
      "reporter": "U.S.",
      "page": "400",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 945",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 911",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1063",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1063",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 945",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 911",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 400",
        "volume": "565",
        "reporter": "U.S.",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1063",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1063",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 400",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 400",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-404",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes \u2014 under a trespass-based theory of the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-404a",
      "page": null,
      "quote": "The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a 'search' within the meaning of the Fourth Amendment when it was adopted.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-409",
      "page": null,
      "quote": "the *Katz* reasonable-expectation-of-privacy test has been *added to*, not *substituted for*, the common-law trespassory test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Jones",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
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
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
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
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Atkinson v. City of Mountain View",
          "cluster_id": 819982,
          "cite": [
            "709 F.3d 1201",
            "2013 WL 462381",
            "2013 U.S. App. LEXIS 2703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union of Ill. v. Alvarez",
          "cluster_id": 799453,
          "cite": [
            "679 F.3d 583",
            "40 Media L. Rep. (BNA) 1721",
            "2012 WL 1592618",
            "2012 U.S. App. LEXIS 9303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthews, Cornelious L.",
          "cluster_id": 2949477,
          "cite": [
            "431 S.W.3d 596",
            "2014 WL 3029070",
            "2014 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 3152697,
          "cite": [
            "303 Kan. 11",
            "363 P.3d 875",
            "2015 Kan. LEXIS 929"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition, Inc. v. Attorney General of the United States",
          "cluster_id": 676451,
          "cite": [
            "677 F.3d 519",
            "2012 WL 1255056",
            "2012 U.S. App. LEXIS 7543"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Drake v. Filko",
          "cluster_id": 1035893,
          "cite": [
            "724 F.3d 426",
            "2013 WL 3927735",
            "2013 U.S. App. LEXIS 15635"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 4395694,
          "cite": [
            "858 F.3d 71",
            "2017 WL 2346566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Graham",
          "cluster_id": 3208153,
          "cite": [
            "824 F.3d 421",
            "2016 WL 3068018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
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
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fulton, I., Aplt.",
          "cluster_id": 4469590,
          "cite": [
            "179 A.3d 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil Morgan v. Fairfield Cty., Ohio",
          "cluster_id": 4532978,
          "cite": [
            "903 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Electronic Privacy Information Center v. United States Department of Homeland Security",
          "cluster_id": 2778134,
          "cite": [
            "414 U.S. App. D.C. 151",
            "777 F.3d 518",
            "2015 U.S. App. LEXIS 2043",
            "2015 WL 525183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union v. Clapper",
          "cluster_id": 8442192,
          "cite": [
            "785 F.3d 787",
            "43 Media L. Rep. (BNA) 1649",
            "62 Communications Reg. (P&F) 945",
            "2015 U.S. App. LEXIS 7531",
            "2015 WL 2097814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nathaniel Holt, Jr.",
          "cluster_id": 2775033,
          "cite": [
            "777 F.3d 1234",
            "96 Fed. R. Serv. 747",
            "2015 WL 399128",
            "2015 U.S. App. LEXIS 1473"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nimesh Patel v. Facebook, Inc.",
          "cluster_id": 4646691,
          "cite": [
            "932 F.3d 1264"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jones:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDgwMzc3NjAwMDAwJnM9NDMyNTQ5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NSZzPTQ0MDUyODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
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
    "complete_query": "cites:(622304 OR 9485324 OR 9485325 OR 9485326)",
    "indexed_citing_opinions": 584,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 622304,
        "count": 584,
        "count_source": "search"
      },
      {
        "opinion_id": 9485324,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485325,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485326,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 8,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-jones.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1MzE4ODYmcz01MzAzNDYyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28622304+OR+9485324+OR+9485325+OR+9485326%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 622304,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 118354,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 122246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 131154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 152441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 152929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 179601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 215613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 328036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 608150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2311429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2443377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 622304,
        "cited_id": 2574690,
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
    "date_created": "2026-07-06T00:55:27Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:01:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:56:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Jones

```
<opinion type="majority">
<author id="Ay9"><page-number citation-index="1" label="402">*402</page-number>Justice Scalia</author>
<p id="A-A">delivered the opinion of the Court.</p>
<p id="AJOK">We decide whether the attachment of a Global-Positioning-­System (GPS) tracking device to an individual’s vehicle, and subsequent use of that device to monitor the vehicle’s move­ments on public streets, constitutes a search or seizure within the meaning of the Fourth Amendment.</p>
<p id="Aem">HH</p>
<p id="Arl">In 2004 respondent Antoine Jones, owner and operator of a nightclub in the District of Columbia, came under suspicion of trafficking in narcotics and was made the target of an in­vestigation by a joint Federal Bureau of Investigation and Metropolitan Police Department task force. Officers em­ployed various investigative techniques, including visual sur­veillance of the nightclub, installation of a camera focused on the front door of the club, and a pen register and wiretap covering Jones’s cellular phone.</p>
<p id="AQN">Based in part on information gathered from these sources, in 2005 the Government applied to the United States District Court for the District of Columbia for a warrant authorizing the use of an electronic tracking device on the Jeep Grand Cherokee registered to Jones’s wife. A warrant issued, au­<page-number citation-index="1" label="403">*403</page-number>thorizing installation of the device in the District of Colum­bia and within 10 days.</p>
<p id="b617-5">On the 11th day, and not in the District of Columbia but in Maryland,<footnotemark>1</footnotemark> agents installed a GPS tracking device on the undercarriage of the Jeep while it was parked in a public parking lot. Over the next 28 days, the Government used the device to track the vehicle’s movements, and once had to replace the device’s battery when the vehicle was parked in a different public lot in Maryland. By means of signals from multiple satellites, the device established the vehicle’s loca­tion within 50 to 100 feet, and communicated that location by cellular phone to a Government computer. It relayed more than 2,000 pages of data over the 4-week period.</p>
<p id="b617-6">The Government ultimately obtained a multiple-count in­dictment charging Jones and several alleged co-conspirators with, as relevant here, conspiracy to distribute and possess with intent to distribute five kilograms or more of cocaine and 50 grams or more of cocaine base, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span> and 846. Before trial, Jones filed a motion to suppress evidence obtained through the GPS device. The District Court granted the motion only in part, suppressing the data obtained while the vehicle was parked in the garage adjoining Jones’s residence. <span class="citation" data-id="2574690"><a href="/opinion/2574690/united-states-v-jones/#88" aria-description="Citation for case: United States v. Jones">451 F. Supp. 2d 71, 88</a></span> (2006). It held the remaining data admissible, because “ ‘[a] person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another.’ ” <em>Ibid, </em>(quoting <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 281</a></span> (1983)). Jones’s trial in October 2006 produced a hung jury on the conspiracy count.</p>
<p id="b617-7">In March 2007, a grand jury returned another indictment, charging Jones and others with the same conspiracy. The Government introduced at trial the same GPS-derived loca­tional data admitted in the first trial, which connected Jones <page-number citation-index="1" label="404">*404</page-number>to the alleged conspirators’ stash house that contained $850,000 in cash, 97 kilograms of cocaine, and 1 kilogram of cocaine base. The jury returned a guilty verdict, and the District Court sentenced Jones to life imprisonment. The United States Court of Appeals for the District of Columbia Circuit reversed the conviction because of admis­sion of the evidence obtained by warrantless use of the GPS device which, it said, violated the Fourth Amendment. <em>United States </em>v. <em>Maynard, </em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/" aria-description="Citation for case: United States v. Maynard">615 F. 3d 544</a></span> (2010). The D. C. Circuit denied the Government’s petition for rehearing en banc, with four judges dissenting. <span class="citation" data-id="9438641"><a href="/opinion/179601/united-states-v-jones/" aria-description="Citation for case: United States v. Jones">625 F. 3d 766</a></span> (2010). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./564/1036/">564 U. S. 1036</a></span> (2011).</p>
<p id="AHl">1 — 1 1 — I</p>
<p id="ALr">A</p>
<p id="AR0">The Fourth Amendment provides in relevant part that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated.” It is beyond dispute that a vehicle is an “effect” as that term is used in the Amendment. <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 12</a></span> (1977). We hold that the Government’s installation of a GPS device on a target’s vehicle,<footnotemark>2</footnotemark> and its use of that device to monitor the vehicle’s movements, constitutes a “search.”</p>
<p id="AKbo">It is important to be clear about what occurred in this case: The Government physically occupied private property for the purpose of obtaining information. We have no doubt that such a physical intrusion would have been considered a <page-number citation-index="1" label="405">*405</page-number>“search” within the meaning of the Fourth Amendment when it was adopted. <em>Entick </em>v. <em>Carrington, </em>95 Eng. Rep. 807 (C. P. 1765), is a “case we have described as a ‘monument of English freedom’ ‘undoubtedly familiar’ to ‘every American statesman’ at the time the Constitution was adopted, and considered to be ‘the true and ultimate expression of consti­tutional law’ ” with regard to search and seizure. <em>Brower </em>v. <em>County of Inyo, </em><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989) (quoting <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626</a></span> (1886)). In that case, Lord Camden expressed in plain terms the significance of prop­erty rights in search-and-seizure analysis:</p>
<blockquote id="b619-5">“[O]ur law holds the property of every man so sacred, that no man can set his foot upon his neighbour’s close without his leave; if he does he is a trespasser, though he does no damage at all; if he will tread upon his neigh-­bour’s ground, he must justify it by law.” <em>Entick, swpra, </em>at 817.</blockquote>
<p id="b619-6">The text of the Fourth Amendment reflects its close connec­tion to property, since otherwise it would have referred simply to “the right of the people to be secure against unrea­sonable searches and seizures”; the phrase “in their persons, houses, papers, and effects” would have been superfluous.</p>
<p id="b619-7">Consistent with this understanding, our Fourth Amend­ment jurisprudence was tied to common-law trespass, at least until the latter half of the 20th century. <em>Kyllo </em>v. <em>United States, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#31" aria-description="Citation for case: Kyllo v. United States">533 U. S. 27, 31</a></span> (2001); Kerr, The Fourth Amendment and New Technologies: Constitutional Myths and the Case for Caution, <span class="citation no-link">102 Mich. L. Rev. 801</span>, 816 (2004). Thus, in <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), we held that wiretaps attached to telephone wires on the public streets did not constitute a Fourth Amendment search be­cause “ft]here was no entry of the houses or offices of the defendants,” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States"><em>id., </em>at 464</a></span>.</p>
<p id="b619-8">Our later cases, of course, have deviated from that exclu­sively property-based approach. In <em>Katz </em>v. <em>United States, </em><page-number citation-index="1" label="406">*406</page-number><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), we said that “the Fourth Amend­ment protects people, not places,” and found a violation in attachment of an eavesdropping device to a public telephone booth. Our later cases have applied the analysis of Justice Harlan’s concurrence in that case, which said that a violation occurs when government officers violate a person’s “reason­able expectation of privacy,” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 360</a></span>. See, <em>e. g., Bond </em>v. <em>United States, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">529 U. S. 334</a></span> (2000); <em>California </em>v. <em>Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986); <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979).</p>
<p id="b620-5">The Government contends that the Harlan standard shows that no search occurred here, since Jones had no “reasonable expectation of privacy” in the area of the Jeep accessed by Government agents (its underbody) and in the locations of the Jeep on the public roads, which were visible to all. But we need not address the Government’s contentions, because Jones’s Fourth Amendment rights do not rise or fall with the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>formulation. At bottom, we must “assur[e] preserva­tion of that degree of privacy against government that ex­isted when the Fourth Amendment was adopted.” <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#34" aria-description="Citation for case: Kyllo v. United States"><em>Kyllo, supra, </em>at 34</a></span>. As explained, for most of our history the Fourth Amendment was understood to embody a particular concern for government trespass upon the areas (“persons, houses, papers, and effects”) it enumerates.<footnotemark>3</footnotemark> <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>did not <page-number citation-index="1" label="407">*407</page-number>repudiate that understanding. Less than two years later the Court upheld defendants’ contention that the Govern­ment could not introduce against them conversations be­tween <em>other </em>people obtained by warrantless placement of electronic surveillance devices in their homes. The opinion rejected the dissent’s contention that there was no Fourth Amendment violation “unless the conversational privacy of the homeowner himself is invaded.”<footnotemark>4</footnotemark> <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#176" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 176</a></span> (1969). “[W]e [do not] believe that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>by holding that the Fourth Amendment protects per­sons and their private conversations, was intended to with­draw any of the protection which the Amendment extends to the home .. . .” <em>Id., </em>at 180.</p>
<p id="b621-5">More recently, in <em>Soldal </em>v. <em>Cook County, </em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56</a></span> (1992), the Court unanimously rejected the argument that although a “seizure” had occurred “in a ‘technical’ sense” when a trailer home was forcibly removed, <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County"><em>id., </em>at 62</a></span>, no Fourth Amendment violation occurred because law enforce­ment had not “invade[d] the [individuals’] privacy,” <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#60" aria-description="Citation for case: Soldal v. Cook County"><em>id., </em>at 60</a></span>. <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Court explained, established that “property rights are not the sole measure of Fourth Amendment violations,” but did not “snuf[f] out the previously recognized protection for property.” <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#64" aria-description="Citation for case: Soldal v. Cook County">506 U. S., at 64</a></span>. As Justice Brennan ex­plained in his concurrence in <em>Knotts, Katz </em>did not erode the principle “that, when the Government <em>does </em>engage in physi­cal intrusion of a constitutionally protected area in order to obtain information, that intrusion may constitute a violation of the Fourth Amendment.” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#286" aria-description="Citation for case: United States v. Knotts">460 U. S., at 286</a></span> (opinion con­curring in judgment). We have embodied that preservation <page-number citation-index="1" label="408">*408</page-number>of past rights in our very definition of “reasonable expecta­tion of privacy” which we have said to be an expectation “that has a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society.” <em>Minnesota </em>v. <em>Carter, </em><span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#88" aria-description="Citation for case: Minnesota v. Carter">525 U. S. 83, 88</a></span> (1998) (inter­nal quotation marks omitted). <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>did not narrow the Fourth Amendment’s scope.<footnotemark>5</footnotemark></p>
<p id="b622-5">The Government contends that several of our post-Aate cases foreclose the conclusion that what occurred here consti­tuted a search. It relies principally on two cases in which we rejected Fourth Amendment challenges to “beepers,” electronic tracking devices that represent another form of electronic monitoring. The first ease, <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>upheld against Fourth Amendment challenge the use of a “beeper” that had been placed in a container of chloroform, allowing law enforcement to monitor the location of the container. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#278" aria-description="Citation for case: United States v. Knotts">460 U. S., at 278</a></span>. We said that there had been no infringe­ment of Knotts’ reasonable expectation of privacy since the information obtained — the location of the automobile carry­<page-number citation-index="1" label="409">*409</page-number>ing the container on public roads, and the location of the off­loaded container in open fields near Knotts’ cabin — had been voluntarily conveyed to the public.<footnotemark>6</footnotemark> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts"><em>Id., </em>at 281-282</a></span>. But as we have discussed, the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>reasonable-expeetation-of-­privacy test has been <em>added to, </em>not <em>substituted for, </em>the common-law trespassory test. The holding in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>ad­dressed only the former, since the latter was not at issue. The beeper had been placed in the container before it came into Knotts’ possession, with the consent of the then-owner. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#278" aria-description="Citation for case: United States v. Knotts">460 U. S., at 278</a></span>. Knotts did not challenge that installation, and we specifically declined to consider its effect on the Fourth Amendment analysis. <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#279" aria-description="Citation for case: United States v. Knotts"><em>Id., </em>at 279</a></span>, n. <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>would be relevant, perhaps, if the Government were making the argument that what would otherwise be an unconstitutional search is not such where it produces only public information. The Government does not make that argument, and we know of no case that would support it.</p>
<p id="b623-5">The second “beeper” case, <em>United States </em>v. <em>Karo, </em>468 U. S.-­705 (1984), does not suggest a different conclusion. There we addressed the question left open by <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>whether the installation of a beeper in a container amounted to a search or seizure. 468 U. S., at 713. As in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>at the time the beeper was installed the container belonged to a third party, and it did not come into possession of the defendant until later. 468 U. S., at 708. Thus, the specific question we con­sidered was whether the installation <em>“with the consent of the original owner </em>constitute^] a search or seizure . . . when the container is delivered to a buyer having no knowledge of the presence of the beeper.” <em>Id., </em>at 707 (emphasis added). We held not. The Government, we said, came into physical contact with the container only before it belonged to the de­<page-number citation-index="1" label="410">*410</page-number>fendant Karo; and the transfer of the container with the un­monitored beeper inside did not convey any information and thus did not invade Karo’s privacy. See <em>id., </em>at 712. That conclusion is perfectly consistent with the one we reach here. Karo accepted the container as it came to him, beeper and all, and was therefore not entitled to object to the beeper’s presence, even though it was used to monitor the container’s location. Cf. <em>On Lee </em>v. <em>United States, </em><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#751" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 751-752</a></span> (1952) (no search or seizure where an informant, who was wearing a concealed microphone, was invited into the defend­ant’s business). Jones, who possessed the Jeep at the time the Government trespassorily inserted the information-­gathering device, is on much different footing.</p>
<p id="b624-5">The Government also points to our exposition in <em>New York </em>v. <em>Class, </em><span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">475 U. S. 106</a></span> (1986), that “[t]he exterior of a car . .. is thrust into the public eye, and thus to examine it does not constitute a ‘search.’ ” <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#114" aria-description="Citation for case: New York v. Class"><em>Id., </em>at 114</a></span>. That statement is of marginal relevance here since, as the Government acknowl­edges, “the officers in this ease did <em>more </em>than conduct a visual inspection of respondent’s vehicle,” Brief for United States 41 (emphasis added). By attaching the device to the Jeep, officers encroached on a protected area. In <em><span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">Class</a></span> </em>it­self we suggested that this would make a difference, for we concluded that an officer’s momentary reaching into the interior of a vehicle did constitute a search.<footnotemark>7</footnotemark> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#114" aria-description="Citation for case: New York v. Class">475 U. S., at 114-115</a></span>.</p>
<p id="b624-6">Finally, the Government’s position gains little support from our conclusion in <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> <page-number citation-index="1" label="411">*411</page-number>(1984), that officers’ information-gathering intrusion on an “open field” did not constitute a Fourth Amendment search even though it was a trespass at common law, <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#183" aria-description="Citation for case: Oliver v. United States"><em>id., </em>at 183</a></span>. Quite simply, an open field, unlike the curtilage of a home, see <em>United States </em>v. <em>Dunn, </em><span class="citation" data-id="9430862"><a href="/opinion/111833/united-states-v-dunn/#300" aria-description="Citation for case: United States v. Dunn">480 U. S. 294, 300</a></span> (1987), is not one of those protected areas enumerated in the Fourth Amendment. <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#176" aria-description="Citation for case: Oliver v. United States"><em>Oliver, supra, </em>at 176-177</a></span>. See also <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924). The Government’s physical intrusion on such an area — unlike its intrusion on the “effect” at issue here — is of no Fourth Amendment significance.<footnotemark>8</footnotemark></p>
<p id="b625-5">B</p>
<p id="b625-6">The concurrence begins by accusing us of applying “18th-­century tort law.” <em>Post, </em>at 418. That is a distortion. What we apply is an 18th-century guarantee against unreasonable searches, which we believe must provide <em>at a minimum </em>the degree of protection it afforded when it was adopted. The concurrence does not share that belief. It would apply <em>ex­clusively Katz’s </em>reasonable-expectation-of-privacy test, even when that eliminates rights that previously existed.</p>
<p id="b625-7">The concurrence faults our approach for “presenting] par­ticularly vexing problems” in cases that do not involve physi­cal contact, such as those that involve the transmission of electronic signals. <em>Post, </em>at 426. We entirely fail to under­stand that point. For unlike the concurrence, which would make <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>the <em>exclusive </em>test, we do not make trespass the exclusive test. Situations involving merely the transmission of electronic signals without trespass would <em>remain </em>subject to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>analysis.</p>
<p id="b626-4"><page-number citation-index="1" label="412">*412</page-number>In fact, it is the concurrence’s insistence on the exclusivity of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>test that needlessly leads us into “particularly vexing problems” in the present case. This Court has to date not deviated from the understanding that mere visual observation does not constitute a search. See <em>Kyllo, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#31" aria-description="Citation for case: Kyllo v. United States">533 U. S., at 31-32</a></span>. We accordingly held in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>that “[a] per­son traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another.” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S., at 281</a></span>. Thus, even assum­ing that the concurrence is correct to say that “[tjraditional surveillance” of Jones for a 4-week period “would have re­quired a large team of agents, multiple vehicles, and perhaps aerial assistance,” <em>post, </em>at 429, our cases suggest that such visual observation is constitutionally permissible. It may be that achieving the same result through electronic means, without an accompanying trespass, is an unconstitutional in­vasion of privacy, but the present case does not require us to answer that question.</p>
<p id="b626-5">And answering it affirmatively leads us needlessly into ad­ditional thorny problems. The concurrence posits that “rel­atively short-term monitoring of a person’s movements on public streets” is okay, but that “the use of longer term GPS monitoring in investigations <em>of most offenses” </em>is no good. <em>Post, </em>at 430 (emphasis added). That introduces yet another novelty into our jurisprudence. There is no precedent for the proposition that whether a search has occurred depends on the nature of the crime being investigated. And even accepting that novelty, it remains unexplained why a 4-week investigation is “surely” too long and why a drug-trafficking conspiracy involving substantial amounts of cash and narcot­ics is not an “extraordinary offens[e]” which may permit longer observation. See <em>post, </em>at 430-431. What of a 2-day monitoring of a suspected purveyor of stolen electronics? Or of a 6-month monitoring of a suspected terrorist? We may have to grapple with these “vexing problems” in some future case where a classic trespassory search is not involved <page-number citation-index="1" label="413">*413</page-number>and resort must be had to <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>analysis; but there is no reason for rushing forward to resolve them here.</p>
<p id="AnBW">III</p>
<p id="A3H">The Government argues in the alternative that even if the attachment and use of the device was a search, it was reasonable — and thus lawful — under the Fourth Amend­ment because “officers had reasonable suspicion, and indeed probable cause, to believe that [Jones] was a leader in a large-scale cocaine distribution conspiracy.” Brief for United States 50-51. We have no occasion to consider this argument. The Government did not raise it below, and the D. C. Circuit therefore did not address it. See <span class="citation" data-id="9438641"><a href="/opinion/179601/united-states-v-jones/#767" aria-description="Citation for case: United States v. Jones">625 F. 3d, at 767</a></span> (Ginsburg, Tatel, and Griffith, JJ., concurring in de­nial of rehearing en banc). We consider the argument for­feited. See <em>Sprietsma </em>v. <em>Mercury Marine, </em><span class="citation" data-id="122246"><a href="/opinion/122246/sprietsma-v-mercury-marine/#56" aria-description="Citation for case: Sprietsma v. Mercury Marine">537 U. S. 51, 56, n. 4</a></span> (2002).</p>
<p id="AYc">* * *</p>
<p id="AjG">The judgment of the Court of Appeals for the D. C. Circuit is affirmed.</p>
<p id="AJT-">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b617-8"> In this litigation, the Government has conceded noncompliance with the warrant and has argued only that a warrant was not required. <em>United States </em>v. <em>Maynard, </em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/#566" aria-description="Citation for case: United States v. Maynard">615 F. 3d 544, 566</a></span>, n. (CADC 2010).</p>
</footnote>
<footnote label="2">
<p id="AAu4"> As we have noted, the Jeep was registered to Jones’s wife. The Gov­ernment acknowledged, however, that Jones was “the exclusive driver.” <span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/#555" aria-description="Citation for case: United States v. Maynard"><em>Id., </em>at 555</a></span>, n. (internal quotation marks omitted). If Jones was not the owner he had at least the property rights of a bailee. The Court of Ap­peals concluded that the vehicle’s registration did not affect his ability to make a Fourth Amendment objection, <em>ibid., </em>and the Government has not challenged that determination here. We therefore do not consider the Fourth Amendment significance of Jones’s status.</p>
</footnote>
<footnote label="3">
<p id="b620-6"> Justice Alito’s concurrence (hereinafter concurrence) doubts the wis­dom of our approach because “it is almost impossible to think of late-18th­century situations that are analogous to what took place in this case.” <em>Post, </em>at 420 (opinion concurring in judgment). But in fact it posits a sit­uation that is not far afield — a constable’s concealing himself in the target’s coach in order to track its movements. <em><span class="citation" data-id="152441"><a href="/opinion/152441/united-states-v-maynard/" aria-description="Citation for case: United States v. Maynard">Ibid.</a></span> </em>There is no doubt that the information gained by that trespassory activity would be the product of an unlawful search — whether that information consisted of the conversations occurring in the coach, or of the destinations to which the coach traveled.</p>
<p id="b620-7">In any case, it is quite irrelevant whether there was an 18th-century analog. Whatever new methods of investigation may be devised, our task, <em>at a minimum, </em>is to decide whether the action in question would have constituted a “search” within the original meaning of the Fourth Amendment. Where, as here, the Government obtains information by <page-number citation-index="1" label="407">*407</page-number>physically intruding on a constitutionally protected area, such a search has undoubtedly occurred.</p>
</footnote>
<footnote label="4">
<p id="b621-8"><em> </em>Thus, the concurrence’s attempt to recast <em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span> </em>as meaning that individuals have a “legitimate expectation of privacy in all conversations that [take] place under their roof,” <em>'post, </em>at 423-424, is foreclosed by the Court’s opinion. The Court took as a given that the homeowner’s “con­versational privacy” had not been violated.</p>
</footnote>
<footnote label="5">
<p id="b622-6"> The concurrence notes that post-Aate we have explained that <em>“ </em>‘an ac­tual trespass is neither necessary <em>nor sufficient </em>to establish a constitu­tional violation.’” <em>Post, </em>at 423 (quoting <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#713" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 713</a></span> (1984)). That is undoubtedly true, and undoubtedly irrelevant. <em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">Karo</a></span> </em>was considering whether a seizure occurred, and as the concurrence explains, a seizure of property occurs, not when there is a trespass, but “when there is some meaningful interference with an individual’s posses-­sory interests in that property.” <em>Post, </em>at 419 (internal quotation marks omitted). Likewise with a search. Trespass alone does not qualify, but there must be conjoined with that what was present here: an attempt .to find something or to obtain information.</p>
<p id="b622-7">Related to this, and similarly irrelevant, is the concurrence’s point that, if analyzed separately, neither the installation of the device nor its use would constitute a Fourth Amendment search. See <em>post, </em>at 420. Of course not. A trespass on “houses” or “effects,” or a <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>invasion of privacy, is not alone a search unless it is done to obtain information; and the obtaining of information is not alone a search unless it is achieved by such a trespass or invasion of privacy.</p>
</footnote>
<footnote label="6">
<p id="b623-6"> <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>noted the “limited use which the government made of the sig­nals from this particular beeper,” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#284" aria-description="Citation for case: United States v. Knotts">460 U. S., at 284</a></span>, and reserved the ques­tion whether “different constitutional principles may be applicable” to “dragnet-type law enforcement practices” of the type that GPS tracking made possible here, <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">ibid.</a></span></em></p>
</footnote>
<footnote label="7">
<p id="b624-7"> The Government also points to <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974), in which the Court rejected the claim that the inspection of an impounded vehicle’s tire tread and the collection of paint scrapings from its exterior violated the Fourth Amendment. Whether the plurality said so because no search occurred or because the search was reasonable is unclear. Com­pare <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis"><em>id., </em>at 591</a></span> (opinion of Blackmun, J.) (“[W]e fail to comprehend what expectation of privacy was infringed”), with <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#592" aria-description="Citation for case: Cardwell v. Lewis"><em>id., </em>at 592</a></span> (“Under circum­stances such as these, where probable cause exists, a warrantless examina­tion of the exterior of a car is not unreasonable ... ”).</p>
</footnote>
<footnote label="8">
<p id="b625-8"> Thus, our theory is <em>not </em>that the Fourth Amendment is concerned with <em>“any </em>technical trespass that led to the gathering of evidence.” <em>Post, </em>at 420 (Alito, J., concurring in judgment) (emphasis added). The Fourth Amendment protects against trespassory searches only with regard to those items (“persons, houses, papers, and effects”) that it enumerates. The trespass that occurred in <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>may properly be understood as a “search,” but not one “in the constitutional sense.” <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#170" aria-description="Citation for case: Oliver v. United States">466 U. S., at 170,183</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Karo.md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Karo"
type: case
citation: "468 U.S. 705 (1984)"
parallel_cite: "104 S. Ct. 3296; 82 L. Ed. 2d 530"
neutral_cite: 1984 U.S. LEXIS 148
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-09-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Karo
  varies_by_point: false
  scope_note: "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111257/united-states-v-karo/"
  cluster_id: 111257
  opinion_id: 9429751
  identity_checked: true
homes:
  - page: "[[Real-Time Tracking]]"
    role: "Key — Anchor (interior context-flip)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Knotts]]", "[[Kyllo v. United States]]", "[[United States v. Jones]]", "[[Carpenter v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "beeper", "tracking", "surveillance", "home"]
holding: "Monitoring a beeper inside a private residence — a location not open to visual surveillance — is a Fourth Amendment search requiring a warrant, because it reveals a critical fact about the interior of the home."
lake:
  record_id: United States v. Karo
  status: verified
  projected_at: 2026-07-06
---

# United States v. Karo

*468 U.S. 705 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With the informant-seller's consent, agents placed a beeper in a can of ether that Karo and others bought to extract cocaine. Agents monitored the beeper as the ether moved among vehicles and houses, including while it was inside a private residence, and used the in-house signal to confirm the ether's location and obtain a search warrant. Karo challenged the warrantless monitoring of the beeper while it was inside the home.

## Issue
Whether the warrantless monitoring of a beeper inside a private residence — a location not open to visual surveillance — violates the Fourth Amendment rights of those with a justifiable privacy interest in the residence.

## Rule
Yes. "This case . . . presents the question whether the monitoring of a beeper in a private residence, a location not open to visual surveillance, violates the Fourth Amendment rights of those who have a justifiable interest in the privacy of the residence. Contrary to the submission of the United States, we think that it does." — 468 U.S. at 714. ^pin-714

The decisive point is that the device reveals interior facts unobtainable from outside: the monitoring "does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like *Knotts*, for there the beeper told the authorities nothing about the interior of Knotts' cabin." — *Id.* at 715. ^pin-715

## Application
Agents used the beeper to establish that the ether was *inside* a particular residence — a fact they could not have verified by lawful outside observation. Because warrantless searches of a home are presumptively unreasonable, electronically determining that a specific article is within the home, without a warrant, was an unreasonable search. The Court contrasted this with public-road tracking ([[United States v. Knotts]]), where the beeper revealed only movements exposed to public view.

## Conclusion
Warrantless monitoring of the beeper inside the residence violated the Fourth Amendment. Paired with [[United States v. Knotts]], *Karo* draws the home/public line for location-tracking technology: tracking inside the home is a search; tracking public movements is not.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[United States v. Knotts]]. Its interior-of-the-home reasoning anticipates [[Kyllo v. United States]] (sense-enhancing technology and the home) and the modern location-tracking cases [[United States v. Jones]] (trespassory GPS installation) and [[Carpenter v. United States]] (long-term cell-site aggregation).

## Appears on
- [[Real-Time Tracking]] — *Key — Anchor (interior context-flip)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Karo*, 468 U.S. 705 (1984) — https://www.courtlistener.com/opinion/111257/united-states-v-karo/ — pinpoints: 714, 715.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c2699989a86914c1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "468 U.S. 705 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 148", "official_citation_present": true, "parallel_cite": "104 S. Ct. 3296; 82 L. Ed. 2d 530", "title": "United States v. Karo", "year": "1984"}}
{"assertion_id": "5c383224ca5007d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-ref — umbrella)", "title": "United States v. Karo"}}
{"assertion_id": "6095c4d6f80a3e13", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "United States v. Karo"}}
{"assertion_id": "b2e714590a238094", "dimension": "support", "kind": "home_role", "locator": {"home": "Real-Time Tracking"}, "payload": {"home": "Real-Time Tracking", "role": "Key — Anchor (interior context-flip)", "title": "United States v. Karo"}}
{"assertion_id": "c301b58daeab02a8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Monitoring a beeper inside a private residence — a location not open to visual surveillance — is a Fourth Amendment search requiring a warrant, because it reveals a critical fact about the interior of the home.", "title": "United States v. Karo"}}
{"assertion_id": "7cc78343bb1f5c39", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Karo"}}
{"assertion_id": "fe1c504d28a71841", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Karo", "field_i_validity": "good_law", "scope_note": "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter.", "title": "United States v. Karo", "varies_by_point": "false"}}
```

### lake record — United States v. Karo

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Karo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Karo",
    "case_name_short": "Karo",
    "case_name_full": "UNITED STATES v. KARO Et Al.",
    "input_case_name": "United States v. Karo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-09-18",
    "year": 1984,
    "docket": null,
    "cluster_id": 111257,
    "lead_opinion_id": 9429751,
    "sibling_ids": [
      111257,
      9429751,
      9429752,
      9429753
    ],
    "absolute_url": "/opinion/111257/united-states-v-karo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 705",
      "volume": "468",
      "reporter": "U.S.",
      "page": "705",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3296",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 530",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 148",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 705",
        "volume": "468",
        "reporter": "U.S.",
        "page": "705",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3296",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 530",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "530",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 148",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "148",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 705",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 705",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-714",
      "page": null,
      "quote": "--- # United States v. Karo *468 U.S. 705 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the informant-seller's consent, agents placed a beeper in a can of ether that Karo and others bought to extract cocaine. Agents monitored the beeper as the ether moved among vehicles and houses, including while it was inside a private residence, and used the in-house signal to confirm the ether's location and obtain a search warrant. Karo challenged the warrantless monitoring of the beeper while it was inside the home. ## Issue Whether the warrantless monitoring of a beeper inside a private residence \u2014 a location not open to visual surveillance \u2014 violates the Fourth Amendment rights of those with a justifiable privacy interest in the residence. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-715",
      "page": null,
      "quote": "does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like *Knotts*, for there the beeper told the authorities nothing about the interior of Knotts' cabin.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Karo",
    "varies_by_point": false,
    "scope_note": "Good law; the rule that monitoring a tracking device inside a private residence is a search requiring a warrant remains controlling and was reinforced by the trespass/aggregation analyses of United States v. Jones and Carpenter.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
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
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Hill",
          "cluster_id": 2769569,
          "cite": [
            "776 F.3d 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane1_negative"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
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
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowers v. Hardwick",
          "cluster_id": 111738,
          "cite": [
            "92 L. Ed. 2d 140",
            "106 S. Ct. 2841",
            "478 U.S. 186",
            "1986 U.S. LEXIS 123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tenenbaum v. Williams",
          "cluster_id": 7079141,
          "cite": [
            "193 F.3d 581",
            "1999 WL 822538"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bull",
          "cluster_id": 1998703,
          "cite": [
            "705 N.E.2d 824",
            "185 Ill. 2d 179",
            "235 Ill. Dec. 641",
            "1998 Ill. LEXIS 1578"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
          "cluster_id": 111667,
          "cite": [
            "90 L. Ed. 2d 226",
            "106 S. Ct. 1819",
            "476 U.S. 227",
            "1986 U.S. LEXIS 155",
            "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
            "54 U.S.L.W. 4464",
            "24 ERC (BNA) 1385"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. 4492 South Livonia Road",
          "cluster_id": 8983256,
          "cite": [
            "889 F.2d 1258",
            "1989 U.S. App. LEXIS 17524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Henry Morgan",
          "cluster_id": 441786,
          "cite": [
            "743 F.2d 1158",
            "1984 U.S. App. LEXIS 18632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Karo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEwODA5NjAwMDAwJnM9MjkyNTU3MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEmcz01ODAwMjgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111257 OR 9429751 OR 9429752 OR 9429753)",
    "indexed_citing_opinions": 567,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111257,
        "count": 497,
        "count_source": "search"
      },
      {
        "opinion_id": 9429751,
        "count": 82,
        "count_source": "search"
      },
      {
        "opinion_id": 9429752,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429753,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 895,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-karo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1ODM2Nzkmcz0xMDYzMTUxNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111257+OR+9429751+OR+9429752+OR+9429753%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111257,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111257,
        "cited_id": 420988,
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
    "date_created": "2026-07-06T01:01:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:06:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:01:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Karo

```
<opinion type="majority">
<author id="b749-6">Justice White</author>
<p id="Ark">delivered the opinion of the Court.</p>
<p id="b749-7">In <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983), we held that the warrantless monitoring of an electronic tracking device (“beeper”)<footnotemark>1</footnotemark> inside a container of chemicals did not violate the Fourth Amendment when it revealed no information that could not have been obtained through visual surveillance. In this case, we are called upon to address two questions left unresolved in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>: </em>(1) whether installation of a beeper in a container of chemicals with the consent of the original owner constitutes a search or seizure within the meaning of the Fourth Amendment when the container is delivered to a buyer having no knowledge of the presence of the beeper, and (2) whether monitoring of a beeper falls within the ambit of the Fourth Amendment when it reveals information that could not have been obtained through visual surveillance.</p>
<p id="b750-3"><page-number citation-index="1" label="708">*708</page-number>I</p>
<p id="b750-4">In August 1980 Agent Rottinger of the Drug Enforcement Administration (DEA) learned that respondents James Karo, Richard Horton, and William Harley had ordered 50 gallons of ether from Government informant Carl Muehlenweg of Graphic Photo Design in Albuquerque, N. M. Muehlenweg told Rottinger that the ether was to be used to extract cocaine from clothing that had been imported into the United States. The Government obtained a court order authorizing the installation and monitoring of a beeper in one of the cans of ether. With Muehlenweg’s consent, agents substituted their own can containing a beeper for one of the cans in the shipment and then had all 10 cans painted to give them a uniform appearance.</p>
<p id="b750-5">On September 20, 1980, agents saw Karo pick up the ether from Muehlenweg. They then followed Karo to his house using visual and beeper surveillance. At one point later that day, agents determined by using the beeper that the ether was still inside the house, but they later determined that it had been moved undetected to Horton’s house, where they located it using the beeper. Agent Rottinger could smell the ether from the public sidewalk near Horton’s residence. Two days later, agents discovered that the ether had once again been moved, and, using the beeper, they located it at the residence of Horton’s father. The next day, the beeper was no longer transmitting from Horton’s father’s house, and agents traced the beeper to a commercial storage facility.</p>
<p id="b750-6">Because the beeper equipment was not sensitive enough to allow agents to learn precisely which locker the ether was in, agents obtained a subpoena for the records of the storage company and learned that locker 143 had been rented by Horton. Using the beeper, agents confirmed that the ether was indeed in one of the lockers in the row containing locker 143, and using their noses they detected the odor of ether emanating from locker 143. On October 8 agents obtained an order authorizing installation of an entry tone alarm into the door <page-number citation-index="1" label="709">*709</page-number>jamb of the locker so they would be able to tell when the door was opened. While installing the alarm, agents observed that the cans containing ether were still inside. Agents ceased visual and beeper surveillance, relying instead on the entry tone alarm. However, on October 16 Horton retrieved the contents from the locker without sounding the alarm. Agents did not learn of the entry until the manager of the storage facility notified them that Horton had been there.</p>
<p id="b751-5">Using the beeper, agents traced the beeper can to another self-storage facility three days later. Agents detected the smell of ether coming from locker 15 and learned from the manager that Horton and Harley had rented that locker using an alias the same day that the ether had been removed from the first storage facility. The agents obtained an order authorizing the installation of an entry tone alarm in locker 15, but instead of installing that alarm, they obtained consent from the manager of the facility to install a closed-circuit video camera in a locker that had a view of locker 15. On February 6, 1981, agents observed, by means of the video camera, Gene Rhodes and an unidentified woman removing the cans from the locker and loading them onto the rear bed of Horton’s pickup truck. Using both visual and beeper surveillance agents tracked the truck to Rhodes’ residence where it was parked in the driveway. Agents then observed Rhodes and a woman bringing boxes and other items from inside the house and loading the items into the trunk of an automobile. Agents did not see any cans being transferred from the pickup.</p>
<p id="b751-6">At about 6 p. m. on February 6, the car and the pickup left the driveway and traveled along public highways to Taos. During the trip, the two vehicles were under both physical and electronic surveillance. When the vehicles arrived at a house in Taos rented by Horton, Harley, and Michael Steele, the agents did not maintain tight surveillance for fear of detection. When the vehicles left the Taos residence, agents <page-number citation-index="1" label="710">*710</page-number>determined, using the beeper monitor, that the beeper can was still inside the house. Again on February 7, the beeper revealed that the ether can was still on the premises. At one point, agents noticed that the windows of the house were wide open on a cold windy day, leading them to suspect that the ether was being used. On February 8, the agents applied for and obtained a warrant to search the Taos residence based in part on information derived through use of the beeper. The warrant was executed on February 10, 1981, and Horton, Harley, Steele, and Evan Roth were arrested, and cocaine and laboratory equipment were seized.</p>
<p id="b752-5">Respondents Karo, Horton, Harley, Steele, and Roth were indicted for conspiring to possess cocaine with intent to distribute it and with the underlying offense. <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846. Respondent Rhodes was indicted only for conspiracy to possess. The District Court granted respondents’ pretrial motion to suppress the evidence seized from the Taos residence on the grounds that the initial warrant to install the beeper was invalid and that the Taos seizure was the tainted fruit of an unauthorized installation and monitoring of that beeper. The United States appealed but did not challenge the invalidation of the initial warrant. The Court of Appeals affirmed, except with respect to Rhodes, holding that a warrant was required to install the beeper in one of the 10 cans of ether and to monitor it in private dwellings and storage lockers. <span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">710 F. 2d 1433</a></span> (CA10 1983). The warrant for the search in Taos and the resulting seizure were tainted by the prior illegal conduct of the Government. The evidence was therefore properly suppressed with respect to respondents Horton, Harley, Steele, and Roth, who were held to have protectible interests in the privacy of the Taos dwelling, and with respect to respondent Karo because the beeper had been installed without a warrant and had been monitored while its ether-can host was in his house.<footnotemark>2</footnotemark> We <page-number citation-index="1" label="711">*711</page-number>granted the Government’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1068/">464 U. S. 1068</a></span> (1984), which raised the question whether a warrant was required to authorize either the installation of the beeper or its subsequent monitoring. We deal with each contention in turn.</p>
<p id="b753-5">II</p>
<p id="b753-6">Because the judgment below in favor of Karo rested in major part on the conclusion that the installation violated his Fourth Amendment rights and that any information obtained from monitoring the beeper was tainted by the initial illegality, we must deal with the legality of the warrantless installation. It is clear that the actual placement of the beeper into the can violated no one’s Fourth Amendment rights. The can into which the beeper was placed belonged at the time to the DEA, and by no stretch of the imagination could it be said that respondents then had any legitimate expectation of privacy in it. The ether and the original 10 cans, on the other hand, belonged to, and were in the possession of, Muehlenweg, who had given his consent to any invasion of those items that occurred. Thus, even if there had been no substitution of cans and the agents had placed the beeper into one of the original 10 cans, Muehlenweg’s consent was sufficient to validate the placement of the beeper in the can. See <em>United States </em>v. <em>Matlock, </em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U. S. 164</a></span> (1974); <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731</a></span> (1969).</p>
<p id="b753-7">The Court of Appeals acknowledged that before Karo took control of the ether “the DEA and Muehlenweg presumably could do with the can and ether whatever they liked without violating Karo’s rights.” <span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/#1438" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">710 F. 2d, at 1438</a></span>. It did not hold that the actual placement of the beeper into the ether can violated the Fourth Amendment. Instead, it held that the violation occurred at the time the beeper-laden can was transferred to Karo. The court stated:</p>
<blockquote id="b754-4"><page-number citation-index="1" label="712">*712</page-number>“All individuals have a legitimate expectation of privacy that objects coming into their rightful ownership do not have electronic devices attached to them, devices that would give law enforcement agents the opportunity to monitor the location of the objects at all times and in every place that the objects are taken, including inside private residences and other areas where the right to be free from warrantless governmental intrusion is unquestioned.” <em><span class="citation" data-id="420988"><a href="/opinion/420988/united-states-v-james-connors-karo-richard-miles-horton-william/" aria-description="Citation for case: United States v. James Connors Karo, Richard Miles...">Ibid.</a></span></em></blockquote>
<p id="b754-5">Not surprisingly, the Court of Appeals did not describe the transfer as either a “search” or a “seizure,” for plainly it is neither. A “search” occurs “when an expectation of privacy that society is prepared to consider reasonable is infringed.” <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). The mere transfer to Karo of a can containing an unmonitored beeper infringed no privacy interest. It conveyed no information that Karo wished to keep private, for it conveyed no information at all. To be sure, it created a <em>potential </em>for an invasion of privacy, but we have never held that potential, as opposed to actual, invasions of privacy constitute searches for purposes of the Fourth Amendment. A holding to that effect would mean that a policeman walking down the street carrying a parabolic microphone capable of picking up conversations in nearby homes would be engaging in a search even if the microphone were not turned on. It is the exploitation of technological advances that implicates the Fourth Amendment, not their mere existence.</p>
<p id="b754-6">We likewise do not believe that the transfer of the container constituted a seizure. A “seizure” of property occurs when “there is some meaningful interference with an individual's possessory interests in that property.” <em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span> </em>Although the can may have contained an unknown and unwanted foreign object, it cannot be said that anyone’s possessory interest was interfered with in a meaningful way. At most, there was a technical trespass on the space occupied by the beeper. The existence of a physical trespass is only <page-number citation-index="1" label="713">*713</page-number>marginally relevant to the question of whether the Fourth Amendment has been violated, however, for an actual trespass is neither necessary nor sufficient to establish a constitutional violation. Compare <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967) (no trespass, but Fourth Amendment violation), with <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984) (trespass, but no Fourth Amendment violation). Of course, if the presence of a beeper in the can constituted a seizure merely because of its occupation of space, it would follow that the presence of any object, regardless of its nature, would violate the Fourth Amendment.</p>
<p id="AG0">We conclude that no Fourth Amendment interest of Karo or of any other respondent was infringed by the installation of the beeper. Rather, any impairment of their privacy interests that may have occurred was occasioned by the monitoring of the beeper.<footnotemark>3</footnotemark></p>
<p id="A1q">rH f-H Y — (</p>
<p id="AatS">In <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983), law enforcement officials, with the consent of the seller, installed a beeper in a 5-gallon can of chloroform and monitored the beeper after delivery of the can to the buyer in Minneapolis, Minn. Although there was partial visual surveillance as the automobile containing the can moved along the public highways, the beeper enabled the officers to locate the can in the area of a cabin near Shell Lake, Wis., and it was this information that provided the basis for the issuance of a search warrant. As the case came to us, the installation of the beeper was not challenged; only the monitoring was at issue. The Court held that since the movements of the automobile and the arrival of the can containing the beeper in the area of the <page-number citation-index="1" label="714">*714</page-number>cabin could have been observed by the naked eye, no Fourth Amendment violation was committed by monitoring the beeper during the trip to the cabin. In <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>the record did not show that the beeper was monitored while the can containing it was inside the cabin, and we therefore had no occasion to consider whether a constitutional violation would have occurred had the fact been otherwise.</p>
<p id="b756-5">Here, there is no gainsaying that the beeper was used to locate the ether in a specific house in Taos, N. M., and that that information was in turn used to secure a warrant for the search of the house. The affidavit supporting the application for a search warrant recited that the ether arrived at the residence in a motor vehicle that later departed and that:</p>
<blockquote id="AcC">“For fear of detection, we did not maintain tight surveillance of the residence. . . . Using the ‘beeper’ locator, I positively determined that the ‘beeper’ can (5-gallon can of ether, described earlier in this affidavit) was now inside the above-described premises to be searched because the ‘beeper’ locator (direction finder) pinpointed the beeper signal as emanating from the above-described premises. . . . Again, later on Saturday (now in the daytime), 7 February 1981, my ‘beeper’ locator still shows a strong ‘beeper’ signal emanating from inside the above-described residence.” App. 57-58.</blockquote>
<p id="b756-6">This case thus presents the question whether the monitoring of a beeper in a private residence, a location not open to visual surveillance, violates the Fourth Amendment rights of those who have a justifiable interest in the privacy of the residence. Contrary to the submission of the United States, we think that it does.</p>
<p id="b756-7">At the risk of belaboring the obvious, private residences are places in which the individual normally expects privacy free of governmental intrusion not authorized by a warrant, and that expectation is plainly one that society is prepared to recognize as justifiable. Our cases have not deviated from this basic Fourth Amendment principle. Searches and <page-number citation-index="1" label="715">*715</page-number>seizures inside a home without a warrant are presumptively unreasonable absent exigent circumstances. <em>Welsh </em>v. <em>Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#748" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 748-749</a></span> (1984); <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981); <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980). In this case, had a DEA agent thought it useful to enter the Taos residence to verify that the ether was actually in the house and had he done so surreptitiously and without a warrant, there is little doubt that he would have engaged in an unreasonable search within the meaning of the Fourth Amendment. For purposes of the Amendment, the result is the same where, without a warrant, the Government surreptitiously employs an electronic device to obtain information that it could not have obtained by observation from outside the curtilage of the house. The beeper tells the agent that' a particular article is actually located at a particular time in the private residence and is in the possession of the person or persons whose residence is being watched. Even if visual surveillance has revealed that the article to which the beeper is attached has entered the house, the later monitoring not only verifies the officers’ observations but also establishes that the article remains on the premises. Here, for example, the beeper was monitored for a significant period after the arrival of the ether in Taos and before the application for a warrant to search.</p>
<p id="b757-5">The monitoring of an electronic device such as a beeper is, of course, less intrusive than a full-scale search, but it does reveal a critical fact about the interior of the premises that the Government is extremely interested in knowing and that it could not have otherwise obtained without a warrant. The case is thus not like <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>, </em>for there the beeper told the authorities nothing about the interior of Knotts’ cabin. The information obtained in <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>was “voluntarily conveyed to anyone who wanted to look . . . ,” <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#281" aria-description="Citation for case: United States v. Knotts">460 U. S., at 281</a></span>; here, as we have said, the monitoring indicated that the beeper was inside the house, a fact that could not have been visually verified.</p>
<p id="b758-4"><page-number citation-index="1" label="716">*716</page-number>We cannot accept the Government’s contention that it should be completely free from the constraints of the Fourth Amendment to determine by means of an electronic device, without a warrant and without probable cause or reasonable suspicion, whether a particular article — or a person, for that matter — is in an individual’s home at a particular time. Indiscriminate monitoring of property that has been withdrawn from public view would present far too serious a threat to privacy interests in the home to escape entirely some sort of Fourth Amendment oversight.<footnotemark>4</footnotemark></p>
<p id="b759-4"><page-number citation-index="1" label="717">*717</page-number>We also reject the Government’s contention that it should be able to monitor beepers in private residences without a warrant if there is the requisite justification in the facts for believing that a crime is being or will be committed and that monitoring the beeper wherever it goes is likely to produce evidence of criminal activity. Warrantless searches are presumptively unreasonable, though the Court has recognized a few limited exceptions to this general rule. See, <em>e. g., United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982) (automobiles); <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973) (consent); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (exigent circumstances). The Government’s contention that warrantless beeper searches should be deemed reasonable is based upon its deprecation of the benefits and exaggeration of the difficulties associated with procurement of a warrant. The Government argues that the traditional justifications for the warrant requirement are inapplicable in beeper cases, but to a large extent that argument is based upon the contention, rejected above, that the beeper constitutes only a minuscule intrusion on protected privacy interests. The primary reason for the warrant requirement is to interpose a “neutral and detached magistrate” between the citizen and “the officer engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Those suspected of drug offenses are no less entitled to that protection than those suspected of nondrug offenses. Requiring a warrant will have the salutary effect of ensuring that use of beepers is not abused, by imposing upon agents the requirement that they demonstrate in advance their justification for the desired search. This is not to say that there <page-number citation-index="1" label="718">*718</page-number>are no exceptions to the warrant rule, because if truly exigent circumstances exist no warrant is required under general Fourth Amendment principles.</p>
<p id="b760-5">If agents are required to obtain warrants prior to monitoring a beeper when it has been withdrawn from public view, the Government argues, for all practical purposes they will be forced to obtain warrants in every case in which they seek to use a beeper, because they have no way of knowing in advance whether the beeper will be transmitting its signals from inside private premises. The argument that a warrant requirement would oblige the Government to obtain warrants in a large number of cases is hardly a compelling argument against the requirement. It is worthy of note that, in any event, this is not a particularly attractive case in which to argue that it is impractical to obtain a warrant, since a warrant was in fact obtained in this case, seemingly on probable cause.</p>
<p id="b760-6">We are also unpersuaded by the argument that a warrant should not be required because of the difficulty in satisfying the particularity requirement of the Fourth Amendment. The Government contends that it would be impossible to describe the “place” to be searched, because the location of the place is precisely what is sought to be discovered through the search. Brief for United States 42. However true that may be, it will still be possible to describe the object into which the beeper is to be placed, the circumstances that led agents to wish to install the beeper, and the length of time for which beeper surveillance is requested. In our view, this information will suffice to permit issuance of a warrant authorizing beeper installation and surveillance.</p>
<p id="b760-7">In sum, we discern no reason for deviating from the general rule that a search of a house should be conducted pursuant to a warrant.<footnotemark>5</footnotemark></p>
<p id="b761-9"><page-number citation-index="1" label="719">*719</page-number>t — I &lt;1</p>
<p id="b761-3">As we have said, by maintaining the beeper the agents verified that the ether was actually located in the Taos house and that it remained there while the warrant was sought. This information was obtained without a warrant and would therefore be inadmissible at trial against those with privacy interests in the house — Horton, Harley, Steele, and Roth. That information, which was included in the warrant affidavit, would also invalidate the warrant for the search of the house if it proved to be critical to establishing probable cause for the issuance of the warrant. However, if sufficient untainted evidence was presented in the warrant affidavit to establish probable cause, the warrant was nevertheless valid. <em>Franks </em>v. <em>Delaware, </em><span class="citation" data-id="9427321"><a href="/opinion/109925/franks-v-delaware/#172" aria-description="Citation for case: Franks v. Delaware">438 U. S. 154, 172</a></span> (1978).</p>
<p id="b761-4">It requires only a casual examination of the warrant affidavit, which in relevant respects consists of undisputed factual assertions, to conclude that the officers could have secured the warrant without relying on the beeper to locate the ether in the house sought to be searched. The affidavit recounted the months-long tracking of the evidence, including the visual and beeper surveillance of Horton’s pickup on its trip from Albuquerque to the immediate vicinity of the Taos residence; its departure a short time later without the ether; its later return to the residence; and the visual observation of the residence with its windows open on a cold night.</p>
<p id="b761-5">That leaves the question whether any part of this additional information contained in the warrant affidavit was itself the fruit of a Fourth Amendment violation to which any of the occupants of the house could object. As far as the <page-number citation-index="1" label="720">*720</page-number>present record reveals, two of the four respondents who had standing to object to the search of the residence — Steele and Roth — had no interest in any of the arguably private places in which the beeper was monitored prior to its arrival in Taos. The evidence seized in the house would be admissible against them.</p>
<p id="b762-5">The question as to Horton and Harley is somewhat more complicated. On the initial leg of its journey, the ether came to rest in Karo’s house where it was monitored; it then moved in succession to two other houses, including Horton’s, before it was moved first to a locker in one public warehouse and then to a locker in another. Both lockers were rented jointly by Horton and Harley. On September 6, the ether was removed from the second storage facility and transported to Taos.</p>
<p id="b762-6">Assuming for present purposes that prior to its arrival at the second warehouse the beeper was illegally used to locate the ether in a house or other place in which Horton or Harley had a justifiable claim to privacy, we are confident that such use of the beeper does not taint its later use in locating the ether and tracking it to Taos. The movement of the ether from the first warehouse was undetected, but by monitoring the beeper the agents discovered that it had been moved to the second storage facility. No prior monitoring of the beeper contributed to this discovery; using the beeper for this purpose was thus untainted by any possible prior illegality. Furthermore, the beeper informed the agents only that the ether was somewhere in the warehouse; it did not identify the specific locker in which the ether was located. Monitoring the beeper revealed nothing about the contents of the locker that Horton and Harley had rented and hence was not a search of that locker.<footnotemark>6</footnotemark> The locker was identified only <page-number citation-index="1" label="721">*721</page-number>when agents traversing the public parts of the facility found that the smell of ether was coming from a specific locker.</p>
<p id="b763-5">The agents set up visual surveillance of that locker, and on September 6, they observed Rhodes and a female remove the ether and load it into Horton’s pickup truck. The truck moved over the public streets and was tracked by beeper to Rhodes’ house, where it was temporarily parked. At about 6 p. m. the truck was observed departing and was tracked visually and by beeper to the vicinity of the house in Taos. Because locating the ether in the warehouse was not an illegal search — and because the ether was seen being loaded into Horton’s truck, which then traveled the public highways — it is evident that under <em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span> </em>there was no violation of the Fourth Amendment as to anyone with or without standing to complain about monitoring the beeper while it was located in Horton’s truck. Under these circumstances, it is clear that the warrant affidavit, after striking the facts about monitoring the beeper while it was in the Taos residence, contained sufficient untainted information to furnish probable cause for the issuance of the search warrant. The evidence seized in the house should not have been suppressed with respect to any of the respondents.<footnotemark>7</footnotemark></p>
<p id="b763-6">The judgment of the Court of Appeals is accordingly</p>
<p id="b763-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b749-9"> “A beeper is a radio transmitter, usually battery operated, which emits periodic signals that can be picked up by a radio receiver.” <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#277" aria-description="Citation for case: United States v. Knotts">460 U. S., at 277</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b752-6"> The Court of Appeals reversed as to Rhodes since he had not shown that the beeper had been located in any place in which he had a reasonable <page-number citation-index="1" label="711">*711</page-number>expectation of privacy, nor had he shown any possessory interest in the ether itself that would have been invaded by the installation of the beeper.</p>
</footnote>
<footnote label="3">
<p id="AKb"> Despite this holding, warrants for the installation and monitoring of a beeper will obviously be desirable since it may be useful, even critical, to monitor the beeper to determine that it is actually located in a place not open to visual surveillance. As will be evident below, such monitoring without a warrant may violate the Fourth Amendment.</p>
</footnote>
<footnote label="4">
<p id="b758-5"> Justice O’Connor observes that a homeowner has no reasonable expectation that a person invited into his home will not be wired with a microphone that transmits conversations in which he engages, see <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White"><em>White, 401 U. </em>S. 746</a></span> (1971), and <em>from </em>this proposition she concludes that a homeowner has no reasonable expectation that an invitee will not bring an object containing a beeper into his home. <em>Post, </em>at 722-724. While that observation would be relevant if one of the conspirators in this case had consented to the placement of the beeper in the can, it has no relevance to the case at hand. Surely if the Government surreptitiously plants a listening device on an unsuspecting household guest or family member and then monitors conversations with the homeowner, the homeowner could challenge the monitoring of the conversations regardless of the fact that he did not have power “to give effective consent to the search” of the visitor. <em>Post, </em>at 724. As the plurality recognized in <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#749" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 749</a></span>, there is a substantial distinction between “revela-tionfs] to the Government by a party to conversations with the defendant” and eavesdropping on conversations without the knowledge or consent of either party to it. A homeowner takes the risk that his guest will cooperate with the Government but not the risk that a trustworthy friend has been bugged by the Government without his knowledge or consent. Under Justice O’Connor’s view it could easily be said that in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), Katz had no reasonable expectation of privacy in his conversation because the person to whom he was speaking might have divulged the contents of the conversation. There would be nothing left of the Fourth Amendment right to privacy if anything that a <em>hypothetical </em>government informant <em>might </em>reveal is stripped of constitutional protection.</p>
<p id="b758-6"><em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980), is simply inapposite, since it was not Rawlings’ home in which the challenged search occurred. Cf. <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969) (homeowner has standing to <page-number citation-index="1" label="717">*717</page-number>challenge illegal search of house even if he has no interest in the property seized). Justice O’Connor seems to recognize as much, noting in the discussion of <em>Katz, post, </em>at 725, that “a third person, <em>who never used a particular telephone line” </em>would have no standing to challenge illegal eavesdropping. If the phone line is that of the third person, however, a different analysis is involved.</p>
</footnote>
<footnote label="5">
<p id="b760-8"> The United States insists that if beeper monitoring is deemed a search, a showing of reasonable suspicion rather than probable cause <page-number citation-index="1" label="719">*719</page-number>should suffice for its execution. That issue, however, is not before us. The initial warrant was not invalidated for want of probable cause, which plainly existed, but for misleading statements in the affidavit. The Government did not appeal the invalidation of the warrant and as the case has turned out, the Government prevails without a warrant authorizing installation. It will be time enough to resolve the probable cause-reasonable suspicion issue in a case that requires it.</p>
</footnote>
<footnote label="6">
<p id="b762-7"> Had the monitoring disclosed the presence of the container within a particular locker the result would be otherwise, for surely Horton and Harley had a reasonable expectation of privacy in their own storage locker.</p>
</footnote>
<footnote label="7">
<p id="b763-11"> Although the unwarranted monitoring of the beeper in Karo’s house would foreclose using that evidence against him, it did not taint the discovery of the ether in the second warehouse and the ensuing surveillance of the trip to Taos.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Knotts.md  (`case`, 7 assertions)

### content_page

```
---
title: "United States v. Knotts"
type: case
citation: "460 U.S. 276 (1983)"
parallel_cite: "103 S. Ct. 1081; 75 L. Ed. 2d 55; 51 U.S.L.W. 4232"
neutral_cite: 1983 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-03-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-03-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Knotts
  varies_by_point: false
  scope_note: "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110882/united-states-v-knotts/"
  cluster_id: 110882
  opinion_id: 9429102
  identity_checked: true
homes:
  - page: "[[Real-Time Tracking]]"
    role: "Key — Anchor (baseline)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — umbrella)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Karo]]", "[[United States v. Jones]]", "[[Carpenter v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "beeper", "tracking", "surveillance", "public-movements"]
holding: "Beeper-aided tracking of a vehicle over public roads is not a search; a person has no reasonable expectation of privacy in his movements over public thoroughfares."
lake:
  record_id: United States v. Knotts
  status: verified
  projected_at: 2026-07-09
---

# United States v. Knotts

*460 U.S. 276 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
With the seller's consent, officers placed a beeper in a drum of chloroform purchased by a co-conspirator. Using visual surveillance aided by the beeper, agents tracked the drum as it was driven over public roads to a secluded cabin. The tracking, combined with other facts, supported a search warrant for the cabin. Knotts argued the beeper-aided tracking was a warrantless search.

## Issue
Whether monitoring a beeper's signals to track a vehicle's movements over public roads invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and thus constitutes a Fourth Amendment search.

## Rule
No. "A person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another." — 460 U.S. at 281. ^pin-281

The beeper added nothing the Fourth Amendment protects against: "Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case." — [*Id.* at 282](https://www.courtlistener.com/opinion/110882/united-states-v-knotts/#:~:text=Nothing%20in%20the%20Fourth%20Amendment). ^pin-282

## Application
As the chloroform drum traveled the public roads, the driver voluntarily exposed his route, stops, and destination to anyone who cared to look. The beeper merely supplemented the agents' visual surveillance of those publicly observable movements; it revealed nothing about the interior of the cabin or any other constitutionally protected space. Because no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] was invaded, the tracking was not a search and required no warrant.

## Conclusion
The beeper-aided tracking of public movements was not a Fourth Amendment search. Paired with [[United States v. Karo]] (monitoring inside a residence is a search), *Knotts* anchors the public-movements / interior-of-the-home line for location-tracking technology.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Companion to [[United States v. Karo]]. [[United States v. Jones]] (2012) reached GPS *installation* on a trespass theory while preserving *Knotts*; [[Carpenter v. United States]] (2018) distinguished short-term public tracking (Knotts) from the long-term, comprehensive aggregation of cell-site records. *Knotts*' core holding for short-term public tracking stands.

## Appears on
- [[Real-Time Tracking]] — *Key — Anchor (baseline)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — umbrella)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *United States v. Knotts*, 460 U.S. 276 (1983) — https://www.courtlistener.com/opinion/110882/united-states-v-knotts/ — pinpoints: 281, 282.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f0dbe0cbb915e5a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "460 U.S. 276 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 135", "official_citation_present": true, "parallel_cite": "103 S. Ct. 1081; 75 L. Ed. 2d 55; 51 U.S.L.W. 4232", "title": "United States v. Knotts", "year": "1983"}}
{"assertion_id": "2758473e85e01c84", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Beeper-aided tracking of a vehicle over public roads is not a search; a person has no reasonable expectation of privacy in his movements over public thoroughfares.", "title": "United States v. Knotts"}}
{"assertion_id": "3b5adadb9e597f49", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-ref — umbrella)", "title": "United States v. Knotts"}}
{"assertion_id": "53421727ecc173b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "United States v. Knotts"}}
{"assertion_id": "b7777ce247d43ba9", "dimension": "support", "kind": "home_role", "locator": {"home": "Real-Time Tracking"}, "payload": {"home": "Real-Time Tracking", "role": "Key — Anchor (baseline)", "title": "United States v. Knotts"}}
{"assertion_id": "0590c6c8a01e519c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Knotts"}}
{"assertion_id": "41fc014810bcc003", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-03-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Knotts", "field_i_validity": "good_law", "scope_note": "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts.", "title": "United States v. Knotts", "varies_by_point": "false"}}
```

### lake record — United States v. Knotts

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Knotts",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Knotts",
    "case_name_short": "Knotts",
    "case_name_full": "United States v. Knotts",
    "input_case_name": "United States v. Knotts",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-03-02",
    "year": 1983,
    "docket": null,
    "cluster_id": 110882,
    "lead_opinion_id": 9429102,
    "sibling_ids": [
      110882,
      9429102,
      9429103,
      9429104
    ],
    "absolute_url": "/opinion/110882/united-states-v-knotts/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 276",
      "volume": "460",
      "reporter": "U.S.",
      "page": "276",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1081",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 55",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "55",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4232",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 135",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 276",
        "volume": "460",
        "reporter": "U.S.",
        "page": "276",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1081",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 55",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "55",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 135",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4232",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 276",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 276",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-281",
      "page": null,
      "quote": "--- # United States v. Knotts *460 U.S. 276 (1983)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background With the seller's consent, officers placed a beeper in a drum of chloroform purchased by a co-conspirator. Using visual surveillance aided by the beeper, agents tracked the drum as it was driven over public roads to a secluded cabin. The tracking, combined with other facts, supported a search warrant for the cabin. Knotts argued the beeper-aided tracking was a warrantless search. ## Issue Whether monitoring a beeper's signals to track a vehicle's movements over public roads invades a reasonable expectation of privacy and thus constitutes a Fourth Amendment search. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-282",
      "page": null,
      "quote": "Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case.",
      "star_marker": "282",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15056,
      "fragment": "#:~:text=Nothing%20in%20the%20Fourth%20Amendment",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-03-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Knotts",
    "varies_by_point": false,
    "scope_note": "Good law for short-term tracking of public movements. United States v. Jones (2012) decided GPS installation on trespass grounds without disturbing Knotts, and Carpenter (2018) distinguished short-term public tracking from long-term aggregation; neither overruled Knotts.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
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
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Augustine",
          "cluster_id": 6580805,
          "cite": [
            "467 Mass. 230",
            "4 N.E.3d 846",
            "2014 WL 901649",
            "2014 Mass. LEXIS 30"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane1_negative"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carpenter v. United States",
          "cluster_id": 4510032,
          "cite": [
            "585 U.S. 296",
            "138 S. Ct. 2206",
            "201 L. Ed. 2d 507",
            "2018 U.S. LEXIS 3844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas Emmons v. Robert McLaughlin Donald Ratliff, Gary Dewalt, City of Norwalk, Reese Wineman",
          "cluster_id": 522917,
          "cite": [
            "874 F.2d 351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Riley",
          "cluster_id": 112175,
          "cite": [
            "102 L. Ed. 2d 835",
            "109 S. Ct. 693",
            "488 U.S. 445",
            "1989 U.S. LEXIS 580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anita Christensen and Robert Alty v. County of Boone, Illinois, and Edward Krieger",
          "cluster_id": 797469,
          "cite": [
            "483 F.3d 454"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 8939436,
          "cite": [
            "757 F.2d 1359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
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
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 449643,
          "cite": [
            "757 F.2d 1359",
            "1985 U.S. App. LEXIS 29735"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Campbell",
          "cluster_id": 1215380,
          "cite": [
            "759 P.2d 1040",
            "306 Or. 157",
            "1988 Ore. LEXIS 400"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Wesley Taylor, United States of America v. Steven Wayne Pressler, and Donald Wesley Taylor",
          "cluster_id": 424125,
          "cite": [
            "716 F.2d 701",
            "14 Fed. R. Serv. 218",
            "1983 U.S. App. LEXIS 16622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Knotts:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjY0OTgyNDAwMDAwJnM9MTMyNDYzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDMmcz00Mzg2NzcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 0,
        "triage_snippet_classified": 27
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110882 OR 9429102 OR 9429103 OR 9429104)",
    "indexed_citing_opinions": 454,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110882,
        "count": 368,
        "count_source": "search"
      },
      {
        "opinion_id": 9429102,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9429103,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429104,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 751,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-knotts.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjY4Njgmcz05OTg2MTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110882+OR+9429102+OR+9429103+OR+9429104%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110882,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 337810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 342454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 349387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 352591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 356186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 364698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 378215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 380205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 396251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 402220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110882,
        "cited_id": 1092690,
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
    "date_created": "2026-07-06T01:11:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:16:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:12:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Knotts

```
<opinion type="majority">
<author id="b339-11">Justice Rehnquist</author>
<p id="A4t">delivered the opinion of the Court.</p>
<p id="b339-12">A beeper is a radio transmitter, usually battery operated, which emits periodic signals that can be picked up by a radio receiver. In this case, a beeper was placed in a five-gallon drum containing chloroform purchased by one of respondent’s codefendants. By monitoring the progress of a car carrying the chloroform Minnesota law enforcement agents were able to trace the can of chloroform from its place of purchase in Minneapolis, Minn., to respondent’s secluded cabin near Shell Lake, Wis. The issue presented by the case is whether such use of a beeper violated respondent’s rights secured by the Fourth Amendment to the United States Constitution.</p>
<p id="b339-13">I — &lt;</p>
<p id="b339-3">Respondent and two codefendants were charged in the United States District Court for the District of Minnesota with conspiracy to manufacture controlled substances, including but not limited to methamphetamine, in violation of <span class="citation no-link">21 U. S. C. §846</span>. One of the codefendants, Darryl Petschen, <page-number citation-index="1" label="278">*278</page-number>was tried jointly with respondent; the other codefendant, Tristan Armstrong, pleaded guilty and testified for the Government at trial.</p>
<p id="b340-5">Suspicion attached to this trio when the 3M Co., which manufactures chemicals in St. Paul, notified a narcotics investigator for the Minnesota Bureau of Criminal Apprehension that Armstrong, a former 3M employee, had been stealing chemicals which could be used in manufacturing illicit drugs. Visual surveillance of Armstrong revealed that after leaving the employ of 3M Co., he had been purchasing similar chemicals from the Hawkins Chemical Co. in Minneapolis. The Minnesota narcotics officers observed that after Armstrong had made a purchase, he would deliver the chemicals to codefendant Petschen.</p>
<p id="b340-6">With the consent of the Hawkins Chemical Co., officers installed a beeper inside a five-gallon container of chloroform, one of the so-called “precursor” chemicals used to manufacture illicit drugs. Hawkins agreed that when Armstrong next purchased chloroform, the chloroform would be placed in this particular container. When Armstrong made the purchase, officers followed the car in which the chloroform had been placed, maintaining contact by using both visual surveillance and a monitor which received the signals sent from the beeper.</p>
<p id="b340-7">Armstrong proceeded to Petschen’s house, where the container was transferred to Petschen’s automobile. Officers then followed that vehicle eastward towards the state line, across the St. Croix River, and into Wisconsin. During the latter part of this journey, Petschen began making evasive maneuvers, and the pursuing agents ended their visual surveillance. At about the same time officers lost the signal from the beeper, but with the assistance of a monitoring device located in a helicopter the approximate location of the signal was picked up again about one hour later. The signal now was stationary and the location identified was a cabin occupied by respondent near Shell Lake, Wis. The record before us does not reveal that the beeper was used after the <page-number citation-index="1" label="279">*279</page-number>location in the area of the cabin had been initially determined.</p>
<p id="b341-5">Relying on the location of the chloroform derived through the use of the beeper and additional information obtained during three days of intermittent visual surveillance of respondent’s cabin, officers secured a search warrant. During execution of the warrant, officers discovered a fully operable, clandestine drug laboratory in the cabin. In the laboratory area officers found formulas for amphetamine and methamphetamine, over $10,000 worth of laboratory equipment, and chemicals in quantities sufficient to produce 14 pounds of pure amphetamine. Under a barrel outside the cabin, officers located the five-gallon container of chloroform.</p>
<p id="b341-6">After his motion to suppress evidence based on the war-rantless monitoring of the beeper was denied, respondent was convicted for conspiring to manufacture controlled substances in violation of 21 U. S. C. .§ 846. He was sentenced to five years’ imprisonment. A divided panel of the United States Court of Appeals for the Eighth Circuit reversed the conviction, finding that.the monitoring of the beeper was prohibited by the Fourth Amendment because its use had violated respondent’s reasonable expectation of privacy, and that all information derived after the location of the cabin was a fruit of the illegal beeper monitoring.<footnotemark>*</footnotemark> <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d 515</a></span> <page-number citation-index="1" label="280">*280</page-number>(1981). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1131/">457 U. S. 1131</a></span> (1982), and we now reverse the judgment of the Court of Appeals.</p>
<p id="b342-3">In <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), this Court held that the wiretapping of a defendant’s private telephone line did not violate the Fourth Amendment because the wiretapping had been effectuated without a physical trespass by the Government. Justice Brandéis, joined by Justice Stone, dissented from that decision, believing that the actions of the Government in that case constituted an “unjustifiable intrusion . . . upon the privacy of the individual,” and therefore a violation of the Fourth Amendment. <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States"><em>Id., </em>at 478</a></span>. Nearly 40 years later, in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the Court overruled <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span> </em>saying that the Fourth Amendment’s reach “cannot turn upon the presence or absence of a physical intrusion into any given enclosure.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>. The Court said:</p>
<blockquote id="b342-4">“The Government’s activities in electronically listening to and recording the petitioner’s words violated the privacy upon which he justifiably relied while using the telephone booth and thus constituted a ‘search and seizure’ within the meaning of the Fourth Amendment. The fact that the electronic device employed to achieve that end did not happen to penetrate the wall of the booth can have no constitutional significance.” <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Ibid.</a></span></em></blockquote>
<p id="b342-5">In <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979), we elaborated on the principles stated in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>:</em></p>
<blockquote id="b342-6">“Consistently with <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>this Court uniformly has held that the application of the Fourth Amendment depends on whether the person invoking its protection can claim a ‘justifiable,’ a ‘reasonable,’ or a ‘legitimate expectation of privacy’ that has been invaded by government action. [Citations omitted.] This inquiry, as Mr. Justice Harlan aptly noted in his <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>concurrence, normally embraces <page-number citation-index="1" label="281">*281</page-number>two discrete questions. The first is whether the individual, by his conduct, has ‘exhibited an actual (subjective) expectation of privacy,’ <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> — whether, in the words of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>majority, the individual has shown that ‘he seeks to preserve [something] as private.’ <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><em>Id., </em>at 351</a></span>. The second question is whether the individual’s subjective expectation of privacy is ‘one that society is prepared to recognize as “reasonable,”’ <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">id.,</a></span> </em>at 361— whether, in the words of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>majority, the individual’s expectation, viewed objectively, is ‘justifiable’ under the circumstances. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><em>Id., at </em>353</a></span>. <em>See Rakas </em>v. <em>Illinois, </em>439 U. S., at 143-144, n. 12; <em>id., </em>at 151 (concurring opinion); <em>United States </em>v. <em>White, </em>401 U. S., at 752 (plurality opinion).” <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 740-741</a></span> (footnote omitted).</blockquote>
<p id="b343-5">The governmental surveillance conducted by means of the beeper in this case amounted principally to the following of an automobile on public streets and highways. We have commented more than once on the diminished expectation of privacy in an automobile:</p>
<blockquote id="b343-6">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one’s residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b343-7">See also <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#153" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 153-154</a></span>, and n. 2 (1978) (Powell, J., concurring); <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976).</p>
<p id="b343-8">A person traveling in an automobile on public thoroughfares has no reasonable expectation of privacy in his movements from one place to another. When Petschen traveled over the public streets he voluntarily conveyed to anyone who wanted to look the fact that he was traveling over par<page-number citation-index="1" label="282">*282</page-number>ticular roads in a particular direction, the fact of whatever stops he made, and the fact of his final destination when he exited from public roads onto private property.</p>
<p id="b344-5">Respondent Knotts, as the owner of the cabin and surrounding premises to which Petschen drove, undoubtedly had the traditional expectation of privacy within a dwelling place insofar as the cabin was concerned:</p>
<blockquote id="b344-6">“Crime, even in the privacy of one’s own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also of grave concern, not only to the individual, but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), quoted with approval in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980).</blockquote>
<p id="b344-7">But no such expectation of privacy extended to the visual observation of Petschen’s automobile arriving on his premises after leaving a public highway, nor to movements of objects such as the drum of chloroform outside the cabin in the “open fields.” <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p id="b344-8">Visual surveillance from public places along Petschen’s route or adjoining Knotts’ premises would have sufficed to reveal all of these facts to the police. The fact that the officers in this case relied not only on visual surveillance, but also on the use of the beeper to signal the presence of Petschen’s automobile to the police receiver, does not alter the situation. Nothing in the Fourth Amendment prohibited the police from augmenting the sensory faculties bestowed upon them at birth with such enhancement as science and technology afforded them in this case. In <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/" aria-description="Citation for case: United States v. Lee">274 U. S. 559</a></span> (1927), the Court said:</p>
<blockquote id="b345-4"><page-number citation-index="1" label="283">*283</page-number>“But no search on the high seas is shown. The testimony of the boatswain shows that he used a searchlight. It is not shown that there was any exploration below decks or under hatches. For aught that appears, the cases of liquor were on deck and, like the defendants, were discovered before the motor boat was boarded. Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution.” <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee"><em>Id., </em>at 563</a></span>.</blockquote>
<p id="b345-5">We have recently had occasion to deal with another claim which was to some extent a factual counterpart of respondent’s assertions here. In <em>Smith </em>v. <em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">Maryland</a></span>, </em>we said:</p>
<blockquote id="b345-6">“This analysis dictates that [Smith] can claim no legitimate expectation of privacy here. When he used his phone, [Smith] voluntarily conveyed numerical information to the telephone company and ‘exposed’ that information to its equipment in the ordinary course of business. In so doing, [Smith] assumed the risk that the company would reveal to police the numbers he dialed. The switching equipment that processed those numbers is merely the modern counterpart of the operator who, in ' an earlier day, personally completed calls for the subscriber. [Smith] concedes that if he had placed his calls through an operator, he could claim no legitimate expectation of privacy. [Citation omitted.] We are not inclined to hold that a different constitutional result is required because the telephone company has decided to automate.” <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#744" aria-description="Citation for case: Smith v. Maryland">442 U. S., at 744-745</a></span>.</blockquote>
<p id="b345-7">Respondent does not actually quarrel with this analysis, though he expresses the generalized view that the result of the holding sought by the Government would be that “twenty-four hour surveillance of any citizen of this country will be possible, without judicial knowledge or supervision.” Brief for Respondent 9 (footnote omitted). But the fact is that the “reality hardly suggests abuse,” <em>Zurcher </em>v. <em>Stanford </em><page-number citation-index="1" label="284">*284</page-number><em>Daily, </em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#566" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 566</a></span> (1978); if such dragnet-type law enforcement practices as respondent envisions should eventually occur, there will be time enough then to determine whether different constitutional principles may be applicable. <em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/" aria-description="Citation for case: Zurcher v. Stanford Daily">Ibid.</a></span> </em>Insofar as respondent’s complaint appears to be simply that scientific devices such as the beeper enabled the police to be more effective in detecting crime, it simply has no constitutional foundation. We have never equated police efficiency with unconstitutionality, and we decline to do so now.</p>
<p id="b346-5">Respondent specifically attacks the use of the beeper insofar as it was used to determine that the can of chloroform had come to rest on his property at Shell Lake, Wis. He repeatedly challenges the “use of the beeper to determine the location of the chemical drum at Respondent’s premises,” Brief for Respondent 26; he states that “[t]he government thus overlooks the fact that this case involves the sanctity of Respondent’s residence, which is accorded the greatest protection available under the Fourth Amendment.” <em><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/" aria-description="Citation for case: Zurcher v. Stanford Daily">Ibid.</a></span> </em>The Court of Appeals appears to have rested its decision on this ground:</p>
<blockquote id="b346-6">“As noted above, a principal rationale for allowing war-rantless tracking of beepers, particularly beepers in or on an auto, is that beepers are merely a more effective means of observing what is already public. But people pass daily from public to private spheres. When police agents track bugged personal property without first obtaining a warrant, they must do so at the risk that this enhanced surveillance, intrusive at best, might push fortuitously and unreasonably into the private sphere protected by the Fourth Amendment.” <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/#518" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d, at 518</a></span>.</blockquote>
<p id="b346-7">We think that respondent’s contentions, and the above-quoted language from the opinion of the Court of Appeals, to some extent lose sight of the limited use which the government made of the signals from this particular beeper. As we have noted, nothing in this record indicates that the beeper <page-number citation-index="1" label="285">*285</page-number>signal was received or relied upon after it had indicated that the drum containing the chloroform had ended its automotive journey at rest on respondent’s premises in rural Wisconsin. Admittedly, because of the failure of the visual surveillance, the beeper enabled the law enforcement officials in this case to ascertain the ultimate resting place of the chloroform when they would not have been able to do so had they relied solely on their naked eyes. But scientific enhancement of this sort raises no constitutional issues which visual surveillance would not also raise. A police car following Petschen at a distance throughout his journey could have observed him leaving the public highway and arriving at the cabin owned by respondent, with the drum of chloroform still in the car. This fact, along with others, was used by the government in obtaining a search warrant which led to the discovery of the clandestine drug laboratory. But there is no indication that the beeper was used in any way to reveal information as to the movement of the drum within the cabin, or in any way that would not have been visible to the naked eye from outside the cabin. Just as notions of physical trespass based on the law of real property were not dispositive in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), neither were they dis-positive in <em>Hester </em>v. <em>United States, </em><span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924).</p>
<p id="b347-5">We thus return to the question posed at the beginning of our inquiry in discussing <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz, supra;</a></span> </em>did monitoring the beeper signals complained of by respondent invade any legitimate expectation of privacy on his part? For the reasons previously stated, we hold it did not. Since it did not, there was neither a “search” nor a “seizure” within the contemplation of the Fourth Amendment. The judgment of the Court of Appeals is therefore</p>
<p id="b347-6">
<em>Reversed.</em>
</p>
<p id="b347-7">Justice Brennan, with whom Justice Marshall joins, concurring in the judgment.</p>
<p id="b347-8">I join Justice Blackmun’s and Justice Stevens’ opinions concurring in the judgment. I should add, however, <page-number citation-index="1" label="286">*286</page-number>that I think this would have been a much more difficult case if respondent had challenged, not merely certain aspects of the monitoring of the beeper installed in the chloroform container purchased by respondent’s compatriot, but also its original installation. See <em>ante, </em>at 279, n. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), made quite clear that the Fourth Amendment protects against governmental invasions of a person’s reasonable “expectation[s] of privacy,” even when those invasions are not accompanied by physical intrusions. Cases such as <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#509" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 509-512</a></span> (1961), however, hold that, when the Government <em>does </em>engage in physical intrusion of a constitutionally protected area in order to obtain information, that intrusion may constitute a violation of the Fourth Amendment even if the same information could have been obtained by other means. I do not believe that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>or its progeny, have eroded that principle. Cf. The Supreme Court, 1979 Term, <span class="citation no-link">94 Harv. L. Rev. 75</span>, 203-204 (1980).</p>
<p id="b348-4">I am also entirely unconvinced by the Court of Appeals’ footnote disposing of the installation issue with the statement: “we hold that the consent of the owner [of the chloroform drum] at the time of installation meets the requirements of the Fourth Amendment, even if the consenting owner intends to soon sell the ‘bugged’ property to an unsuspecting buyer. <em>Caveat </em>emptor.” <span class="citation" data-id="9468533"><a href="/opinion/396251/united-states-v-leroy-carlton-knotts-and-darryl-petschen/#517" aria-description="Citation for case: United States v. Leroy Carlton Knotts and Darryl Petschen">662 F. 2d 515, 517, n. 2</a></span> (1981) (citation omitted). The Government is not here defending against a claim for damages in an action for breach of a warranty; it is attempting to justify the legality of a search conducted in the course of a criminal investigation. I am not at all sure that, for purposes of the Fourth Amendment, there is a constitutionally significant difference between planting a beeper in an object in the possession of a criminal suspect and purposefully arranging that he be sold an object that, unknown to him, already has a beeper installed inside it. Cf. <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#305" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 305-306</a></span> (1921); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#211" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 211</a></span> (1966).</p>
<p id="b349-4"><page-number citation-index="1" label="287">*287</page-number>Respondent claimed at oral argument that, under this Court’s cases, he would not have standing to challenge the original installation of the beeper in the chloroform drum because the drum was sold, not to him, but to one of his compatriots. See <em>ante, </em>at 279, n. If respondent is correct, that would only confirm for me the formalism and confusion in this Court’s recent attempts to redefine Fourth Amendment standing. See <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#114" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 114</a></span> (1980) (Marshall, J., dissenting); <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#156" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 156</a></span> (1978) (White, J., dissenting).</p>
<footnote label="*">
<p id="b341-7">Respondent does not challenge the warrantless installation of the beeper in the chloroform container, suggesting in oral argument that he did not believe he had standing to make such a challenge. We note that while several Courts of Appeals have approved warrantless installations, see <em>United States </em>v. <em>Bernard, </em><span class="citation" data-id="9466894"><a href="/opinion/380205/united-states-v-howard-dale-bernard-united-states-of-america-v-ralph/" aria-description="Citation for case: United States v. Howard Dale Bernard, United States of...">625 F. 2d 854</a></span> (CA9 1980); <em>United States </em>v. <em>Lewis, </em><span class="citation" data-id="378215"><a href="/opinion/378215/united-states-v-john-bradley-lewis-jr-kenneth-brooks-aka-james-earl/" aria-description="Citation for case: United States v. John Bradley Lewis, Jr., Kenneth Brooks,...">621 F. 2d 1382</a></span> (CA5 1980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./450/935/">450 U. S. 935</a></span> (1981); <em>United States </em>v. <em>Bruneau, </em><span class="citation" data-id="364698"><a href="/opinion/364698/united-states-v-dale-david-bruneau-united-states-of-america-v-jeffrey/" aria-description="Citation for case: United States v. Dale David Bruneau, United States of...">594 F. 2d 1190</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./444/847/">444 U. S. 847</a></span> (1979); <em>United States </em>v. <em>Miroyan, </em><span class="citation multiple-matches"><a href="/c/F.%202d/577/489/">577 F. 2d 489</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/896/">439 U. S. 896</a></span> (1978); <em>United States </em>v. <em>Cheshire, </em><span class="citation" data-id="352591"><a href="/opinion/352591/united-states-v-alan-kent-cheshire/" aria-description="Citation for case: United States v. Alan Kent Cheshire">569 F. 2d 887</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./437/907/">437 U. S. 907</a></span> (1978); <em>United States </em>v. <em>Curtis, </em><span class="citation" data-id="8903472"><a href="/opinion/8915345/united-states-v-curtis/" aria-description="Citation for case: United States v. Curtis">562 F. 2d 1153</a></span> (CA9 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./439/910/">439 U. S. 910</a></span> (1978); <em>United States </em>v. <em>Abel, </em><span class="citation" data-id="342454"><a href="/opinion/342454/united-states-v-joseph-e-abel-sr-larry-neal-whittington-james-glenn/" aria-description="Citation for case: United States v. Joseph E. Abel, Sr., Larry Neal...">548 F. 2d 591</a></span> (CA5), cert. denied, 431U. S. 956 (1977); <em>United States </em>v. <em>Hufford, </em>539 F. 2d.32 (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1002/">429 U. S. 1002</a></span> (1976), we have not before and do not now pass on the issue.</p>
</footnote>
</opinion>
```

---
