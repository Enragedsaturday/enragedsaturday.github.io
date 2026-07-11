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

## GROUP: content/cases/Austin v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Austin v. United States
type: case
citation: "509 U.S. 602 (1993)"
parallel_cite: "113 S. Ct. 2801; 125 L. Ed. 2d 488"
neutral_cite: "1993 U.S. LEXIS 4407; 1993 WL 224465"
court: U.S.
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-06-28
docket: 92-6073
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
  opinion_url: "https://www.courtlistener.com/opinion/112904/austin-v-united-states/"
  cluster_id: 112904
  opinion_id: 9432892
  identity_checked: true
lake:
  record_id: Austin v. United States
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. Bajakajian]]"
  - "[[Timbs v. Indiana]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - in-rem
  - punishment
holding: "Because in rem civil forfeiture of property used to facilitate drug offenses under 21 U.S.C. §§ 881(a)(4) and (a)(7) serves at least in part to punish, it constitutes 'payment to a sovereign as punishment for some offense' and is therefore subject to the Eighth Amendment's Excessive Fines Clause."
aliases:
  - Austin v. United States
  - "Austin v. United States (1993)"
---

# Austin v. United States

*509 U.S. 602 (1993)* (No. 92-6073) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112904 → combined opinion 112904 (Blackmun, J.; 509 U.S. 602, decided June 28, 1993). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*622`). S9 promotes. -->

## Background
Richard Lyle Austin pleaded guilty in South Dakota state court to one count of possessing cocaine with intent to distribute, arising out of a small drug sale he made from his auto body shop. After his state conviction, the federal government brought an *in rem* civil forfeiture action under 21 U.S.C. §§ 881(a)(4) and (a)(7) against Austin's mobile home and auto body shop, on the theory that the properties had been used to facilitate the drug offense. The District Court and the Eighth Circuit ordered forfeiture, rejecting Austin's argument that taking his home and business was so disproportionate to his offense that it violated the Eighth Amendment's Excessive Fines Clause — reasoning that the Clause did not reach civil, *in rem* forfeitures at all.

## Issue
Whether the Excessive Fines Clause of the Eighth Amendment applies to *in rem* civil forfeitures of property used to facilitate a drug offense.

## Rule
The Court rejected the premise that a forfeiture escapes the Eighth Amendment merely because it is labeled "civil" and proceeds against the property rather than the owner. What matters is whether the sanction serves, even in part, to punish. Because the historical understanding of forfeiture, the statute's focus on the owner's culpability, and Congress's stated deterrent aims all showed these forfeitures to be at least partly punitive, the Court held: "We therefore conclude that forfeiture under these provisions constitutes 'payment to a sovereign as punishment for some offense,' ... and, as such, is subject to the limitations of the Eighth Amendment's Excessive Fines Clause." — 509 U.S. at 622. ^pin-622

## Application
Sections 881(a)(4) and (a)(7) tie forfeiture to the property's role in a crime and exempt "innocent owners" — features that make sense only if the statute aims to punish culpable owners, not merely to remove dangerous items from circulation. The Government's "remedial" characterizations (removing instrumentalities, recouping enforcement costs) could not explain a sanction whose value bears no fixed relation to any harm or cost. Having established that the Clause applies, the Court declined Austin's invitation to announce a test for when a forfeiture is constitutionally "excessive," leaving that question for the lower courts [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] for consideration of excessiveness. Blackmun, J., delivered the opinion of the Court; Scalia, J., and Kennedy, J. (joined by Rehnquist, C.J., and Thomas, J.), concurred in part and in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Austin* is the anchor for subjecting civil forfeiture to the Excessive Fines Clause. It left the excessiveness *standard* open; the Court supplied it five years later in *[[United States v. Bajakajian]]* (1998) (a fine is unconstitutional if grossly disproportional to the offense), and it applied the Clause against the States through the Fourteenth Amendment in *[[Timbs v. Indiana]]* (2019). Teach *Austin* as step one — the Clause *applies* — and *[[United States v. Bajakajian|Bajakajian]]*/*[[Timbs v. Indiana|Timbs]]* as the standard and its reach.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*Austin v. United States*, 509 U.S. 602 (1993)](https://www.courtlistener.com/opinion/112904/austin-v-united-states/) — pinpoint: 622 (Blackmun, J., for the Court; the CL opinion text carries the reporter star `*622` immediately before the holding). Rule quote string-matched to the CL opinion text 2026-07-07 (internal citation to *Browning-Ferris* elided).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ea44519a13ceec3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "509 U.S. 602 (1993)", "court": "U.S.", "neutral_cite": "1993 U.S. LEXIS 4407; 1993 WL 224465", "official_citation_present": true, "parallel_cite": "113 S. Ct. 2801; 125 L. Ed. 2d 488", "title": "Austin v. United States", "year": "1993"}}
{"assertion_id": "158d78a912d23e5c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because in rem civil forfeiture of property used to facilitate drug offenses under 21 U.S.C. §§ 881(a)(4) and (a)(7) serves at least in part to punish, it constitutes 'payment to a sovereign as punishment for some offense' and is therefore subject to the Eighth Amendment's Excessive Fines Clause.", "title": "Austin v. United States"}}
{"assertion_id": "869c4b35ca0de73c", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "Austin v. United States"}}
{"assertion_id": "75a0c8c6a7f979ea", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Austin v. United States", "varies_by_point": "false"}}
{"assertion_id": "f43676583dcb1431", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Austin v. United States"}}
```

### lake record — Austin v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Austin v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Austin v. United States",
    "case_name_short": "Austin",
    "case_name_full": "Austin v. United States",
    "input_case_name": "Austin v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-06-28",
    "year": 1993,
    "docket": "92-6073",
    "cluster_id": 112904,
    "lead_opinion_id": 9432892,
    "sibling_ids": [],
    "absolute_url": "/opinion/112904/austin-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "509 U.S. 602",
      "volume": "509",
      "reporter": "U.S.",
      "page": "602",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "509 U.S. 602",
        "volume": "509",
        "reporter": "U.S.",
        "page": "602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 2801",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "2801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "125 L. Ed. 2d 488",
        "volume": "125",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 4407",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "4407",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 224465",
        "volume": "1993",
        "reporter": "WL",
        "page": "224465",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "509 U.S. 602",
    "official_selection": {
      "court_class": "scotus",
      "selected": "509 U.S. 602",
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
    "date_created": "2026-07-07T13:22:16Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:22:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "austin-v-united-states--112904",
      "to_record_id": "Austin v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Austin v. United States

```
<opinion type="majority">
<author id="b646-4"><page-number citation-index="1" label="604">*604</page-number>Justice Blackmun</author>
<p id="AVJ">delivered the opinion of the Court.</p>
<p id="b646-5">In this case, we are asked to decide whether the Excessive Fines Clause of the Eighth Amendment applies to forfeitures of property under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7). We hold that it does and therefore remand the case for consideration of the question whether the forfeiture at issue here was excessive.</p>
<p id="b646-6">I</p>
<p id="b646-7">On August 2,1990, petitioner Richard Lyle Austin was indicted on four counts of violating South Dakota’s drug laws. Austin ultimately pleaded guilty to one count of possessing cocaine with intent to distribute and was sentenced by the state court to seven years’ imprisonment. On September 7, the United States filed an <em>in rem </em>action in the United States District Court for the District of South Dakota seeking forfeiture of Austin’s mobile home and auto body shop under <span class="citation no-link">21 <page-number citation-index="1" label="605">*605</page-number>U. S. C. §§ 881</span>(a)(4) and (a)(7).<footnotemark>1</footnotemark> Austin filed a claim and an answer to the complaint.</p>
<p id="b647-5">On February 4, 1991, the United States made a motion, supported by an affidavit from Sioux Falls Police Officer Donald Satterlee, for summary judgment. According to Satterlee’s affidavit, Austin met Keith Engebretson at Austin’s body shop on June 13, 1990, and agreed to sell cocaine to Engebretson. Austin left the shop, went to his mobile home, and returned to the shop with two grams of cocaine which he sold to Engebretson. State authorities executed a search warrant on the body shop and mobile home the following day. They discovered small amounts of marijuana and cocaine, a .22 caliber revolver, drug paraphernalia, and approximately $4,700 in cash. App. 13. In opposing summary judgment, Austin argued that forfeiture of the properties would violate the Eighth Amendment.<footnotemark>2</footnotemark> The District Court rejected this argument and entered summary judgment for the United States. <span class="citation no-link"><em>Id., </em>at 19</span>.</p>
<p id="b647-6">The United States Court of Appeals for the Eighth Circuit “reluctantly agree[d] with the government” and affirmed. <page-number citation-index="1" label="606">*606</page-number><em>United States </em>v. <em>One Parcel of Property, </em><span class="citation multiple-matches"><a href="/c/F.%202d/964/814/">964 F. 2d 814</a></span>, 817 (1992). Although it thought that “the principle of proportionality should be applied in civil actions that result in harsh penalties,” <em>ibid., </em>and that the Government was “exacting too high a penalty in relation to the offense committed,” <em>id., </em>at 818, the court felt constrained from holding the forfeiture unconstitutional. It cited this Court’s decision in <em>CaleroToledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), for the proposition that, when the Government is proceeding against property <em>in rem, </em>the guilt or innocence of the property’s owner “is constitutionally irrelevant.” 964 F. 2d, at 817. It then reasoned: “We are constrained to agree with the Ninth Circuit that ‘[i]f the constitution allows <em>in rem </em>forfeiture to be visited upon innocent owners . . . the constitution hardly requires proportionality review of forfeitures.’” <em>Ibid., </em>quoting <em>United States </em>v. <em>Tax Lot 1500, </em><span class="citation" data-id="8965274"><a href="/opinion/8973657/united-states-v-tax-lot-1500/#234" aria-description="Citation for case: United States v. Tax Lot 1500">861 F. 2d 232, 234</a></span> (CA9 1988), cert. denied <em>sub nom. Jaffee </em>v. <em>United States, </em><span class="citation" data-id="9086527"><a href="/opinion/9092333/jaffee-v-united-states/" aria-description="Citation for case: Jaffee v. United States">493 U. S. 954</a></span> (1989).</p>
<p id="b648-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./506/1074/">506 U. S. 1074</a></span> (1993), to resolve an apparent conflict with the Court of Appeals for the Second Circuit over the applicability of the Eighth Amendment to <em>in rem </em>civil forfeitures. See <em>United States </em>v. <em>Certain Real Property, </em><span class="citation" data-id="576216"><a href="/opinion/576216/united-states-v-certain-real-property-and-premises-known-as-38-whalers/#35" aria-description="Citation for case: United States v. Certain Real Property and Premises Known...">954 F. 2d 29, 35, 38-39</a></span>, cert. denied <em>sub nom. Levin </em>v. <em>United States, </em><span class="citation" data-id="9118128"><a href="/opinion/9123561/levin-v-united-states/" aria-description="Citation for case: Levin v. United States">506 U. S. 815</a></span> (1992).</p>
<p id="b648-6">II</p>
<p id="b648-7">Austin contends that the Eighth Amendment’s Excessive Fines Clause applies to <em>in rem </em>civil forfeiture proceedings. See Brief for Petitioner 10,19, 23. We have had occasion to consider this Clause only once before. In <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S. 257</a></span> (1989), we held that the Excessive Fines Clause does not limit the award of punitive damages to a private party in a civil suit when the government neither has prosecuted the action nor has any right to receive a share of the damages. <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#264" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>Id., </em>at 264</a></span>. The Court’s opinion and Justice O’Connor’s <page-number citation-index="1" label="607">*607</page-number>opinion, concurring in part and dissenting in part, reviewed in some detail the history of the Excessive Fines Clause. See <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#264" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>id., </em>at 264-268,286-297</a></span>. The Court concluded that both the Eighth Amendment and § 10 of the English Bill of Rights of 1689, from which it derives, were intended to prevent <em>the government </em>from abusing its power to punish, see <em>id., </em>at 266-267, and therefore that “the Excessive Fines Clause was intended to limit only those fines directly imposed by, and payable to, the government,” <em>id., </em>at 268.<footnotemark>3</footnotemark></p>
<p id="b649-5">We found it unnecessary to decide in <em>Browning-Ferris </em>whether the Excessive Fines Clause applies only to criminal cases. <em>Id., </em>at 263. The United States now argues that</p>
<blockquote id="b649-6">“any claim that the government’s conduct in a civil proceeding is limited by the Eighth Amendment generally, or by the Excessive Fines Clause in particular, must fail unless the challenged governmental action, despite its label, would have been recognized as a <em>criminal </em>punishment at the time the Eighth Amendment was adopted.” Brief for United States 16 (emphasis added).</blockquote>
<p id="b649-7">It further suggests that the Eighth Amendment cannot apply to a civil proceeding unless that proceeding is so punitive that it must be considered criminal under <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144</a></span> (1963), and <em>United States </em>v. <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">448 U. S. 242</a></span> (1980). Brief for United States 26-27. We disagree.</p>
<p id="b649-8">Some provisions of the Bill of Rights are expressly limited to criminal cases. The Fifth Amendment’s Self-Incrimination Clause, for example, provides: “No person ... shall be compelled in any criminal case to be a witness <page-number citation-index="1" label="608">*608</page-number>against himself.” The protections provided by the Sixth Amendment are explicitly confined to “criminal prosecutions.” See generally <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S., at 248</a></span>.<footnotemark>4</footnotemark> The text of the Eighth Amendment includes no similar limitation. See n. <em>2, supra.</em></p>
<p id="b650-5">Nor does the history of the Eighth Amendment require such a limitation. Justice O’Connor noted in <em>Browning-Ferris: </em>“Consideration of the Eighth Amendment immediately followed consideration of the Fifth Amendment. <page-number citation-index="1" label="609">*609</page-number>After deciding to confine the benefits of the Self-Inerimination Clause of the Fifth Amendment to criminal proceedings, the Framers turned their attention to the Eighth Amendment. There were no proposals to limit that Amendment to criminal proceedings ....” <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#294" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 294</a></span>. Section 10 of the English Bill of Rights of 1689 is not expressly limited to criminal cases either. The original draft of § 10 as introduced in the House of Commons did contain such a restriction, but only with respect to the bail clause: “The requiring excessive Bail of Persons committed in criminal Cases, and imposing excessive Fines, and illegal Punishments, to be prevented.” 10 H. C. Jour. 17 (1688). The absence of any similar restriction in the other two clauses suggests that they were not limited to criminal cases. In the final version, even the reference to criminal cases in the bail clause was omitted. See 1 W. &amp; M., 2d Sess., ch. 2, 3 Stat. at Large 441 (1689) (“That excessive Bail ought not to be required, nor excessive Fines imposed; nor cruel and unusual Punishments inflicted”); see also L. Schwoerer, The Declaration of Rights, 1689, p. 88 (1981) (“But article 10 contains no reference to ‘criminal cases’ and, thus, would seem to apply ... to all cases”).<footnotemark>5</footnotemark></p>
<p id="b651-5">The purpose of the Eighth Amendment, putting the Bail Clause to one side, was to limit the government’s power to punish. See <em>Browning-Ferris, </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#266" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 266-267, 275</a></span>. The Cruel and Unusual Punishments Clause is self-evidently concerned with punishment. The Excessive Fines Clause limits the government’s power to extract payments, whether <page-number citation-index="1" label="610">*610</page-number>in cash or in kind, “as <em>punishment </em>for some offense.” <em>Id.¡ </em>at 265 (emphasis added). “The notion of punishment, as we commonly understand it, cuts across the division between the civil and the criminal law.” <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 447-448</a></span> (1989). “It is commonly understood that civil proceedings may advance punitive as well as remedial goals, and, conversely, that both punitive and remedial goals may be served by criminal penalties.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper"><em>Id., </em>at 447</a></span>. See also <em>United States ex rel. Marcus </em>v. <em>Hess, </em><span class="citation" data-id="9419289"><a href="/opinion/103757/united-states-ex-rel-marcus-v-hess/#554" aria-description="Citation for case: United States Ex Rel. Marcus v. Hess">317 U. S. 537, 554</a></span> (1943) (Frankfurter, J., concurring). Thus, the question is not, as the United States would have it, whether forfeiture under §§ 881(a)(4) and (a)(7) is civil or criminal, but rather whether it is punishment.<footnotemark>6</footnotemark></p>
<p id="b652-5">In considering this question, we are mindful of the fact that sanctions frequently serve more than one purpose. We need not exclude the possibility that a forfeiture serves remedial purposes to conclude that it is subject to the limitations of the Excessive Fines Clause. We, however, must determine that it can only be explained as serving in part to punish. We said in <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span> </em>that “a civil sanction that cannot fairly be said solely to serve a remedial purpose, but rather can only be explained as also serving either retributive or deterrent purposes, is punishment, as we have come to understand the term.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span>. We turn, then, to consider whether, at the time the Eighth Amendment was ratified, forfeiture was understood at least in part as punish<page-number citation-index="1" label="611">*611</page-number>ment and whether forfeiture under §§ 881(a)(4) and (a)(7) should be so understood today.</p>
<p id="b653-5">Ill</p>
<p id="b653-6">A</p>
<p id="b653-7">Three kinds of forfeiture were established in England at the time the Eighth Amendment was ratified in the United States: deodand, forfeiture upon conviction for a felony or treason, and statutory forfeiture. See <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#680" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 680-683</a></span>. Each was understood, at least in part, as imposing punishment.</p>
<blockquote id="b653-8">“At common law the value of an inanimate object directly or indirectly causing the accidental death of a King’s subject was forfeited to the Crown as a deodand. The origins of the deodand are traceable to Biblical and pre-Judeo-Christian practices, which reflected the view that the instrument of death was accused and that religious expiation was required. See O. Holmes, The Common Law, c. 1 (1881). The value of the instrument was forfeited to the King, in the belief that the King would provide the money for Masses to be said for the good of the dead man’s soul, or insure that the deodand was put to charitable uses. 1 W. Blackstone, Commentaries *300. When application of the deodand to religious or eleemosynary purposes ceased, and the deodand became a source of Crown revenue, the institution was justified as a penalty for carelessness.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#680" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Id., </em>at 680-681</a></span> (footnotes omitted).</blockquote>
<p id="b653-9">As Blackstone put it, “such misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture.” 1 W. Blackstone, Commentaries *301.</p>
<p id="b653-10">The second kind of common-law forfeiture fell only upon those convicted of a felony or of treason. “The convicted felon forfeited his chattels to the Crown and his lands es-<page-number citation-index="1" label="612">*612</page-number>cheated to his lord; the convicted traitor forfeited all of his property, real and personal, to the Crown.” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. Such forfeitures were known as forfeitures of estate. See 4 W. Blackstone, at *381. These forfeitures obviously served to punish felons and traitors, see <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat. 1, 14</a></span> (1827), and were justified on the ground that property was a right derived from society which one lost by violating society’s laws, see 1 W. Blackstone, at *299; 4 <em>id., </em>at *382.</p>
<p id="b654-5">Third, “English Law provided for statutory forfeitures of offending objects used in violation of the customs and revenue laws.” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. The most notable of these were the Navigation Acts of 1660 that required the shipping of most commodities in English vessels. Violations of the Acts resulted in the forfeiture of the illegally carried goods as well as the ship that transported them. See generally L. Harper, English Navigation Laws (1939). The statute was construed so that the act of an individual seaman, undertaken without the knowledge of the master or owner, could result in forfeiture of the entire ship. See <em>Mitchell </em>v. <em>Torup, </em>Park. 227, 145 Eng. Rep. 764 (Ex. 1766). Yet Blackstone considered such forfeiture statutes “penal.” 3 W. Blackstone, at *261.</p>
<p id="b654-6">In <em>Calero-Toledo, </em>we observed that statutory forfeitures were “likely a product of the confluence and merger of the deodand tradition and the belief that the right to own property could be denied the wrongdoer.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. Since each of these traditions had a punitive aspect, it is not surprising that forfeiture under the Navigation Acts was justified as a penalty for negligence: “But the Owners of Ships are to take Care what Master they employ, and the Master what Mariners; and here Negligence is plainly imputable to the Master; for he is to report the Cargo of the Ship, and if he had searched and examined the Ship with proper care, according to his Duty, he would have found the Tea . . . and <page-number citation-index="1" label="613">*613</page-number>so might have prevented the Forfeiture.” <em>Mitchell, </em>Park., at 238, 145 Eng. Rep., at 768.</p>
<p id="b655-5">B</p>
<p id="b655-6">Of England’s three kinds of forfeiture, only the third took hold in the United States. “Deodands did not become part of the common-law tradition of this country.” <em>CaleroToledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#682" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 682</a></span>. The Constitution forbids forfeiture of estate as a punishment for treason “except during the Life of the Person attainted,” U. S. Const., Art. III, § 3, cl. 2, and the First Congress also abolished forfeiture of estate as a punishment for felons. Act of Apr. 30, 1790, ch. 9, §24, <span class="citation no-link">1 Stat. 117</span>. “But ‘[l]ong before the adoption of the Constitution the common law courts in the Colonies — and later in the states during the period of Confederation — were exercising jurisdiction <em>in rem </em>in the enforcement of [English and local] forfeiture statutes.’ ” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 683</a></span>, quoting C. <em>J. Hendry Co. </em>v. <em>Moore, </em><span class="citation" data-id="9419300"><a href="/opinion/103775/c-j-hendry-co-v-moore/#139" aria-description="Citation for case: C. J. Hendry Co. v. Moore">318 U. S. 133, 139</a></span> (1943).</p>
<p id="b655-7">The First Congress passed laws subjecting ships and car-gos involved in customs offenses to forfeiture. It does not follow from that fact, however, that the First Congress thought such forfeitures to be beyond the purview of the Eighth Amendment. Indeed, examination of those laws suggests that the First Congress viewed forfeiture as punishment. For example, by the Act of July 31, 1789, ch. 5, § 12, <span class="citation no-link">1 Stat. 39</span>, Congress provided that goods could not be unloaded except during the day and with a permit.</p>
<blockquote id="b655-8">“[A]nd if the master or commander of any ship or vessel shall suffer or permit the same, such master and commander, and every other person who shall be aiding or assisting in landing, removing, housing, or otherwise securing the same, shall forfeit and pay the sum of four hundred dollars for every offence; shall moreover be disabled from holding any office of trust or profit under the United States, for a term not exceeding seven years; and it shall be the duty of the collector of the district, to <page-number citation-index="1" label="614">*614</page-number>advertise the names of all such persons in the public gazette of the State in which he resides, within twenty-days after each respective conviction. And all goods, wares and merchandise, so landed or discharged, shall become forfeited, and may be seized by any officer of the customs; and where the value thereof shall amount to four hundred dollars, the vessel, tackle, apparel and furniture, shall be subject to like forfeiture and seizure.”</blockquote>
<p id="b656-5">Forfeiture of the goods and vessel is listed alongside the other provisions for punishment. It is also of some interest that “forfeit” is the word Congress used for fine. See <em><span class="citation no-link">ibid.</span> </em>(“shall forfeit and pay the sum of four hundred dollars for every offence”).<footnotemark>7</footnotemark> Other early forfeiture statutes follow the same pattern. See, <em>e. g., </em>Act of Aug. 4, 1790, ch. 34, §§ 13, 22, 27, 28, <span class="citation no-link">1 Stat. 157</span>, 161, 163.</p>
<p id="b656-6">C</p>
<p id="b656-7">Our cases also have recognized that statutory <em>in rem </em>forfeiture imposes punishment. In <em>Peisch </em>v. <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Ware, 4 </em>Cranch 347</a></span> (1808), for example, the Court held that goods removed from the custody of a revenue officer without the payment of duties should not be forfeitable for that reason unless they were removed with the consent of the owner or his agent. Chief Justice Marshall delivered the opinion for a unanimous Court:</p>
<blockquote id="b656-8">“The court is also of opinion that the removal for which the act punishes the owner with a forfeiture of <page-number citation-index="1" label="615">*615</page-number>the goods must be made with his consent or connivance, or with that of some person employed or trusted by him. If, by private theft, or open robbery, without any fault on his part, his property should be invaded, while in the custody of the officer of the revenue, the law cannot be understood to punish him with the forfeiture of that property.” <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Id., </em>at 364</a></span>.<footnotemark>8</footnotemark></blockquote>
<p id="b657-5">The same understanding of forfeiture as punishment runs through our cases rejecting the “innocence” of the owner as a common-law defense to forfeiture. See, <em>e. g., Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 683</a></span>; <em>J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505</a></span> (1921); <em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395</a></span> (1878); <em>Harmony </em>v. <em>United States, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210</a></span> (1844); <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">12 Wheat. 1</a></span> (1827). In these cases, forfeiture has been justified on two theories — that the property itself is “guilty” of the offense, and that the owner may_ be held accountable for the wrongs of others to whom he entrusts his property. Both theories rest, at bottom, on the notion that the owner has been negligent in allowing his property to be misused and that he is properly punished for that negligence.</p>
<p id="b657-6">The fiction that “the thing is primarily considered the offender,” <em>Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#511" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 511</a></span>, has a venerable history in our case law.<footnotemark>9</footnotemark> See <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat., <page-number citation-index="1" label="616">*616</page-number>at 14</a></span> (“The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing”); <em>Harmony, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#233" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 233</a></span> (“The vessel which commits the aggression is treated as the offender, as the guilty instrument or thing to which the forfeiture attaches, without any reference whatsoever to the character or conduct of the owner”); <em>Dobbins’s Distillery, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 401</a></span> (“[T]he offence ... is attached primarily to the distillery, and the real and personal property used in connection with the same, without any regard whatsoever to the personal misconduct or responsibility of the owner”). Yet the Court has understood this fiction to rest on the notion that the owner who allows his property to become involved in an offense has been negligent. Thus, in <em>Goldsmith-Grant Co., </em>the Court said that “ascribing to the property a certain personality, a power of complicity and guilt in the wrong,” had “some analogy to the law of <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>deodand.” 254 </em>U. S., at 510</a></span>. It then quoted Blackstone’s explanation of the reason for deodand: that “‘such misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture.’” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>Id., </em>at 510-511</a></span>, quoting 1 W. Blackstone, at *301.</p>
<p id="b658-5">In none of these cases did the Court apply the guilty-property fiction to justify forfeiture when the owner had done all that reasonably could be expected to prevent the unlawful use of his property. In <em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">The Palmyra</a></span>, </em>it did no more than reject the argument that the criminal conviction of the owner was a prerequisite to the forfeiture of his property. See <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#15" aria-description="Citation for case: The Palmyra">12 Wheat., at 15</a></span> (“[N]o personal conviction of the offender is necessary to enforce a forfeiture <em>in rem </em>in cases of this nature”). In <em>Harmony, </em>the owners’ claim of “innocence” was limited to the fact that they “never contemplated <page-number citation-index="1" label="617">*617</page-number>or authorized the acts complained of.” <span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#230" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 230</a></span>. And in <em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">Dobbins’s Distillery</a></span>, </em>the Court noted that some responsibility on the part of the owner arose “from the fact that he leased the property to the distiller, and suffered it to be occupied and used by the lessee as a distillery.” <span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 401</a></span>. The more recent cases have expressly reserved the question whether the fiction could be employed to forfeit the property of a truly innocent owner. See, <em>e. g., Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#512" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 512</a></span>; <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#689" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 689-690</a></span> (noting that forfeiture of a truly innocent owner’s property would raise “serious constitutional questions”).<footnotemark>10</footnotemark> If forfeiture had been understood not to punish the owner, there would have been no reason to reserve the case of a truly innocent owner. Indeed, it is only on the assumption that forfeiture serves in part to punish that the Court’s past reservation of that question makes sense.</p>
<p id="b659-5">The second theory on which the Court has justified the forfeiture of an “innocent” owner’s property is that the owner may be held accountable for the wrongs of others to whom he entrusts his property. In <em>Harmony, </em>it reasoned that “the acts of the master and crew, in cases of this sort, bind the interest of the owner of the ship, whether he be innocent or guilty; and he impliedly submits to whatever the law denounces as a forfeiture attached to the ship by reason of their unlawful or wanton wrongs.” <span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#234" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How., at 234</a></span>. It repeated this reasoning in <em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">Dobbins’s Distillery</a></span>:</em></p>
<blockquote id="b659-6">“[T]he unlawful acts of the distiller bind the owner of the property, in respect to the management of the same, as much as if they were committed by the owner himself. Power to that effect the law vests in him by virtue of his lease; and, if he abuses his trust, it is a matter to be settled between him and his lessor; but the acts of viola<page-number citation-index="1" label="618">*618</page-number>tion as to the penal consequences to the property are to be considered just the same as if they were the acts of the owner.” <span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#404" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 404</a></span>.</blockquote>
<p id="b660-5">Like the guilty-property fiction, this theory of vicarious liability is premised on the idea that the owner has been negligent. Thus, in <em>Calero-Toledo, </em>we noted that application of forfeiture provisions “to lessors, bailors, or secured creditors who are innocent of any wrongdoing ... may have the desirable effect of inducing them to exercise greater care in transferring possession of their property.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#688" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 688</a></span>.<footnotemark>11</footnotemark></p>
<p id="b660-6">In sum, even though this Court has rejected the “innocence” of the owner as a common-law defense to forfeiture, it consistently has recognized that forfeiture serves, at least in part, to punish the owner. See <em>Peisch </em>v. <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Ware, 4 </em>Cranch, at 364</a></span> (“[T]he act punishes the owner with a forfeiture of the goods”); <em>Dobbins’s Distillery, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#404" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S., at 404</a></span> (“[T]he acts of violation as to the penal consequences to the property are to be considered just the same as if they were the acts of the owner”); <em>Goldsmith-Grant Co., </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#511" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 511</a></span> (“'[S]uch misfortunes are in part owing to the negligence of the owner, and therefore he is properly punished by such forfeiture’ ”). More recently, we have noted that forfeiture serves “punitive and deterrent purposes,” <em>Calero-Toledo, </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#686" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 686</a></span>, and “impos[es] an economic penalty,” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#687" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>id., </em>at 687</a></span>. We conclude, therefore, that forfeiture generally and statutory <em>in rem </em>forfeiture in particular historically have been understood, at least in part, as punishment.<footnotemark>12</footnotemark></p>
<p id="b661-4"><page-number citation-index="1" label="619">*619</page-number>IV</p>
<p id="b661-5">We turn next to consider whether forfeitures under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7) are properly considered punishment today. We find nothing in these provisions or their legislative history to contradict the historical understanding of forfeiture as punishment. Unlike traditional forfeiture statutes, §§ 881(a)(4) and (a)(7) expressly provide an “innocent owner” defense. See § 881(a)(4)(C) (“[N]o conveyance shall be forfeited under this paragraph to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge, consent, or willful blindness of the owner”); § 881(a)(7) (“[N]o property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner”); see also <em>United States </em>v. <em>Parcel of Rumson, N. J., Land, </em><span class="citation" data-id="9432740"><a href="/opinion/112823/united-states-v-parcel-of-rumson-nj-land/#122" aria-description="Citation for case: United States v. Parcel of Rumson, NJ, Land">507 U. S. 111, 122-123</a></span> (1993) (plurality opinion) (noting difference from traditional forfeiture statutes). These exemptions serve to focus the provisions on the culpability of the owner in a way that makes them look more like punishment, not less. In <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715</a></span> (1971), we reasoned that <span class="citation no-link">19 U. S. C. § 1618</span>, which provides that the Secretary of the Treasury is to return the property of those who do not intend to violate the law, demonstrated Congress’ intent “to impose a penalty only upon those who are significantly involved in a criminal enterprise.” <span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/#721" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S., at 721-722</a></span>. The inclusion of innocent-owner defenses in §§ 881(a)(4) and (a)(7) reveals a similar congressional intent to punish only those involved in drug trafficking.</p>
<p id="b662-4"><page-number citation-index="1" label="620">*620</page-number>Furthermore, Congress has chosen to tie forfeiture directly to the commission of drug offenses. Thus, under § 881(a)(4), a conveyance is forfeitable if it is used or intended for use to facilitate the transportation of controlled substances, their raw materials, or the equipment used to manufacture or distribute them. Under § 881(a)(7), real property is forfeitable if it is used or intended for use to facilitate the commission of a drug-related crime punishable by more than one year’s imprisonment. See n. <span class="citation" data-id="8965274"><a href="/opinion/8973657/united-states-v-tax-lot-1500/" aria-description="Citation for case: United States v. Tax Lot 1500">1, <em>supra.</em></a></span></p>
<p id="b662-5">The legislative history of §881 confirms the punitive nature of these provisions. When it added subsection (a)(7) to §881 in 1984, Congress recognized “that the traditional criminal sanctions of fine and imprisonment are inadequate to deter or punish the enormously profitable trade in dangerous drugs.” S. Rep. No. 98-225, p. 191 (1983).<footnotemark>13</footnotemark> It characterized the forfeiture of real property as “a powerful deterrent.” <em>Id., </em>at 195. See also Joint House-Senate Explanation of Senate Amendment to Titles II and III of the Psychotropic Substances Act of 1978, 124 Cong. Rec. 34671 (1978) (noting “the penal nature of forfeiture statutes”).</p>
<p id="b662-6">The Government argues that §§ 881(a)(4) and (a)(7) are not punitive but, rather, should be considered remedial in two respects. First, they remove the “instruments” of the drug trade “thereby protecting the community from the threat of continued drug dealing.” Brief for United States 32. Second, the forfeited assets serve to compensate the Government for the expense of law enforcement activity and for its expenditure on societal problems such as urban blight, drug addiction, and other health concerns resulting from the drug trade. <em>Id., </em>at 25, 32.</p>
<p id="b663-4"><page-number citation-index="1" label="621">*621</page-number>In our view, neither argument withstands scrutiny. Concededly, we have recognized that the forfeiture of contraband itself may be characterized as remedial because it removes dangerous or illegal items from society. See <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#364" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 364</a></span> (1984). The Court, however, previously has rejected government’s attempt to extend that reasoning to conveyances used to transport illegal liquor. See <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#699" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 699</a></span> (1965). In that case it noted: “There is nothing even remotely criminal in possessing an automobile.” <em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">Ibid.</a></span> </em>The same, without question, is true of the properties involved here, and the Government’s attempt to characterize these properties as “instruments” of the drug trade must meet the same fate as Pennsylvania’s effort to characterize the 1958 Plymouth sedan as “contraband.”</p>
<p id="b663-5">The Government’s second argument about the remedial nature of this forfeiture is no more persuasive. We previously have upheld the forfeiture of goods involved in customs violations as “a reasonable form of liquidated damages.” <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 237</a></span> (1972). But the dramatic variations in the value of conveyances and real property forfeitable under §§ 881(a)(4) and (a)(7) undercut any similar argument with respect to those provisions. The Court made this very point in <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span>: </em>The “forfeiture of property . . . [is] a penalty that ha[s] absolutely no correlation to any damages sustained by society or to the cost of enforcing the law.” <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#254" aria-description="Citation for case: United States v. Ward">448 U. S., at 254</a></span>.</p>
<p id="b663-6">Fundamentally, even assuming that §§ 881(a)(4) and (a)(7) serve some remedial purpose, the Government’s argument must fail. “[A] civil sanction that cannot fairly be said <em>solely </em>to serve a remedial purpose, but rather can only be explained as also serving either retributive or deterrent purposes, is punishment, as we have come to understand the term.” <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span> (emphasis added). In light of the historical understanding of forfeiture as punishment, the <page-number citation-index="1" label="622">*622</page-number>clear focus of §§ 881(a)(4) and (a)(7) on the culpability of the owner, and the evidence that Congress understood those provisions as serving to deter and to punish, we cannot conclude that forfeiture under §§ 881(a)(4) and (a)(7) serves solely a remedial purpose.<footnotemark>14</footnotemark> We therefore conclude that forfeiture under these provisions constitutes “payment to a sovereign as punishment for some offense,” <em>Browning-Ferris, </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#265" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 265</a></span>, and, as such, is subject to the limitations of the Eighth Amendment’s Excessive Fines Clause.</p>
<p id="b664-5">V</p>
<p id="b664-6">Austin asks that we establish a multifactor test for determining whether a forfeiture is constitutionally “excessive.” See Brief for Petitioner 46-48. We decline that invitation. Although the Court of Appeals opined that “the government is exacting too high a penalty in relation to the offense committed,” 964 F. 2d, at 818, it had no occasion to consider what factors should inform such a decision because it thought it was foreclosed from engaging in the inquiry. Prudence dictates that we allow the lower courts to consider that question <page-number citation-index="1" label="623">*623</page-number>in the first instance. See <em>Yee </em>v. <em>Escondido, </em><span class="citation" data-id="9432511"><a href="/opinion/112719/yee-v-city-of-escondido/#538" aria-description="Citation for case: Yee v. City of Escondido">503 U. S. 519, 538</a></span> (1992).<footnotemark>15</footnotemark></p>
<p id="b665-5">The judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b665-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b647-7"> These statutes provide for the forfeiture of:</p>
<blockquote id="b647-8">“(4) All conveyances, including aircraft, vehicles, or vessels, which are used, or are intended for use, to transport, or in any manner to facilitate the transportation, sale, receipt, possession, or conceálment of [controlled substances, their raw materials, and equipment used in their manufacture and distribution]</blockquote>
<blockquote id="b647-9">“(7) All real property, including any right, title, and interest (including any leasehold interest) in the whole of any lot or tract of land and any appurtenances or improvements, which is used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of, a violation of this subchapter punishable by more than one year’s imprisonment. ..</blockquote>
<p id="b647-10">Each provision has an “innocent owner” exception. See §§ 881(a)(4)(C) and (a)(7).</p>
</footnote>
<footnote label="2">
<p id="b647-11"> “Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.” U. S. Const., Arndt. 8.</p>
</footnote>
<footnote label="3">
<p id="b649-9"> In <em>Browning-Ferris, </em>we left open the question whether the Excessive Fines Clause applies to <em>qui tam </em>actions in which a private party brings suit in the name of the United States and shares in the proceeds. See <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#276" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 276, n. 21</a></span>. Because the instant suit was prosecuted by the United States and because Austin’s property was forfeited to the United States, we have no occasion to address that question here.</p>
</footnote>
<footnote label="4">
<p id="b650-6"> As a general matter, this Court’s decisions applying constitutional protections to civil forfeiture proceedings have adhered to this distinction between provisions that are limited to criminal proceedings and provisions that are not. Thus, the Court has held that the Fourth Amendment’s protection against unreasonable searches and seizures applies in forfeiture proceedings, see <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#696" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 696</a></span> (1965); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 634</a></span> (1886), but that the Sixth Amendment’s Confrontation Clause does not, see <em>United States </em>v. <em>Zucker, </em><span class="citation" data-id="94399"><a href="/opinion/94399/united-states-v-zucker/#480" aria-description="Citation for case: United States v. Zucker">161 U. S. 475, 480-482</a></span> (1896). It has also held that the due process requirement that guilt in a criminal proceeding be proved beyond a reasonable doubt, see <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970), does not apply to civil forfeiture proceedings. See <em>Lilienthal’s Tobacco </em>v. <em>United States, </em><span class="citation" data-id="89785"><a href="/opinion/89785/lilienthals-tobacco-v-united-states/#271" aria-description="Citation for case: Lilienthal&#x27;s Tobacco v. United States">97 U. S. 237, 271-272</a></span> (1878).</p>
<p id="b650-7">The Double Jeopardy Clause has been held not to apply in civil forfeiture proceedings, but only in cases where the forfeiture could properly be characterized as remedial. See <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#364" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 364</a></span> (1984); <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 237</a></span> (1972); see generally <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#446" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 446-449</a></span> (1989) (Double Jeopardy Clause prohibits second sanction that may not fairly be characterized as remedial). Conversely, the Fifth Amendment’s Self-Incrimination Clause, which is textually limited to “criminal case[s],” has been applied in civil forfeiture proceedings, but only where the forfeiture statute had made the culpability of the owner relevant, see <em>United States </em>v. <em>United States Coin &amp; Currency, </em><span class="citation" data-id="9424510"><a href="/opinion/108303/united-states-v-united-states-coin-currency/#721" aria-description="Citation for case: United States v. United States Coin &amp; Currency">401 U. S. 715, 721-722</a></span> (1971), or where the owner faced the possibility of subsequent criminal proceedings, see <em>Boyd, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S., at 634</a></span>; see also <em>United States </em>v. <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#253" aria-description="Citation for case: United States v. Ward">448 U. S. 242, 253-254</a></span> (1980) (discussing <em>Boyd).</em></p>
<p id="b650-8">And, of course, even those protections associated with criminal cases may apply to a civil forfeiture proceeding if it is so punitive that the proceeding must reasonably be considered criminal. See <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144</a></span> (1963); <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward, supra.</a></span></em></p>
</footnote>
<footnote label="5">
<p id="b651-6"> In <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977), we concluded that the omission of any reference to criminal cases in § 10 was without substantive significance in light of the preservation of a similar reference to criminal cases in the preamble to the English Bill of Rights. <em>Id., </em>at 665. This reference in the preamble, however, related only to excessive bail. See 1 W. &amp; M., 2d Sess., ch. 2, 3 Stat. at Large 440 (1689). Moreover, the preamble appears designed to catalog the misdeeds of James II, see <em>ibid., </em>rather than to define the scope of the substantive rights set out in subsequent sections.</p>
</footnote>
<footnote label="6">
<p id="b652-6"> For this reason, the United States’ reliance on <em>Kennedy </em>v. <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez</a></span> </em>and <em>United States </em>v. <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span> </em>is misplaced. The question in those cases was whether a nominally civil penalty should be reclassified as criminal and the safeguards that attend a criminal prosecution should be required. See <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#167" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S., at 167, 184</a></span>; <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S., at 248</a></span>. In addressing the separate question whether punishment is being imposed, the Court has not employed the tests articulated in <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez</a></span> </em>and <em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/" aria-description="Citation for case: United States v. Ward">Ward</a></span>. </em>See, <em>e. g., United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#447" aria-description="Citation for case: United States v. Halper">490 U. S., at 447</a></span>. Since in this case we deal only with the question whether the Eighth Amendment’s Excessive Fines Clause applies, we need not address the application of those tests.</p>
</footnote>
<footnote label="7">
<p id="b656-9"> Dictionaries of the time confirm that “fine” was understood to include “forfeiture” and vice versa. See 1 T. Sheridan, A General Dictionary of the English Language (1780) (unpaginated) (defining “fine” as: “A mulct, a pecuniary punishment; penalty; forfeit, money paid for any exemption or liberty”); J. Walker, A Critical Pronouncing Dictionary (1791) (unpaginated) (same); 1 Sheridan, <em>supra </em>(defining “forfeiture” as: “The act of forfeiting; the thing forfeited, a mulct, a fine”); Walker, <em>supra </em>(same); J. Kersey, A New English Dictionary (1702) (unpaginated) (defining “forfeit” as: “default, fine, or penalty”).</p>
</footnote>
<footnote label="8">
<p id="b657-7"> In <em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">Peisch</a></span>, </em>the removal of the goods from the custody of the revenue officer occurred not by theft or robbery, but pursuant to a writ of replevin issued by a state court. See <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#360" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">4 Cranch, at 360</a></span>. Thus, <em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">Peisch</a></span> </em>stands for the general principle that “the law is not understood to forfeit the property of owners or consignees, on account of the misconduct of mere strangers, over whom such owners or consignees could have no control.” <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#365" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Id., </em>at 365</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b657-8"> The Government relies heavily on this fiction. See Brief for United States 18. We do not understand the Government to rely separately on the technical distinction between proceedings <em>in rem </em>and proceedings <em>in personam, </em>but we note that any such reliance would be misplaced. “The fictions of <em>in rem </em>forfeiture were developed primarily to expand the reach of the courts,” <em>Republic Nat. Bank of Miami </em>v. <em>United States, </em><span class="citation" data-id="9432701"><a href="/opinion/112797/republic-national-bank-of-miami-v-united-states/#87" aria-description="Citation for case: Republic National Bank of Miami v. United States">506 U. S. <page-number citation-index="1" label="616">*616</page-number>80, 87</a></span> (1992), which, particularly in admiralty proceedings, might have lacked <em>in personam </em>jurisdiction over the owner of the property. See also <em>Harmony </em>v. <em>United States, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#233" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210, 233</a></span> (1844). As is discussed in the text, forfeiture proceedings historically have been understood as imposing punishment despite their <em>in rem </em>nature.</p>
</footnote>
<footnote label="10">
<p id="b659-7"> Because the forfeiture provisions at issue here exempt “innocent owners,” we again have no occasion to decide in this case whether it would comport with due process to forfeit the property of a truly innocent owner.</p>
</footnote>
<footnote label="11">
<p id="b660-7"> In the criminal context, we have permitted punishment in the absence of conscious wrongdoing, so long as the defendant was not “ ‘powerless’ to prevent or correct the violation.” <em>United States </em>v. <em>Park, </em><span class="citation" data-id="9426096"><a href="/opinion/109264/united-states-v-park/#673" aria-description="Citation for case: United States v. Park">421 U. S. 658, 673</a></span> (1975) (corporate officer strictly liable under the Food, Drug, and Cosmetic Act). There is nothing inconsistent, therefore, in viewing forfeiture as punishment even though the forfeiture is occasioned by the acts of a person other than the owner.</p>
</footnote>
<footnote label="12">
<p id="b660-8"> The doubts that Justice Scalia, see <em>post, </em>at 625-627, and Justice Kennedy, see <em>post, </em>at 629, express with regard to the historical understanding of forfeiture as punishment appear to stem from a misunder<page-number citation-index="1" label="619">*619</page-number>standing of the relevant question. Under <em>United States </em>v. <em>Halper, </em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S. 435, 448</a></span> (1989), the question is whether forfeiture serves <em>in part </em>to punish, and one need not exclude the possibility that forfeiture serves other purposes to reach that conclusion.</p>
</footnote>
<footnote label="13">
<p id="b662-7"> Although the United States omits any reference to this legislative history in its brief in the present case, it quoted the same passage with approval in its brief in <em>United States </em>v. <em>Parcel of Rumson, N. J., Land, </em><span class="citation" data-id="9432740"><a href="/opinion/112823/united-states-v-parcel-of-rumson-nj-land/" aria-description="Citation for case: United States v. Parcel of Rumson, NJ, Land">507 U. S. 111</a></span> (1993). See Brief for United States, O. T. 1992, No. 91-781, pp. 41-42.</p>
</footnote>
<footnote label="14">
<p id="b664-7"> In <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span>, </em>we focused on whether “the sanction as applied in the individual case serves the goals of punishment.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#448" aria-description="Citation for case: United States v. Halper">490 U. S., at 448</a></span>. In this case, however, it makes sense to focus on §§ 881(a)(4) and (a)(7) as a whole. <em><span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/" aria-description="Citation for case: United States v. Halper">Halper</a></span> </em>involved a small, fixed-penalty provision, which “in the ordinary case . . . can be said to do no more than make the Government whole.” <span class="citation" data-id="9431670"><a href="/opinion/112259/united-states-v-halper/#449" aria-description="Citation for case: United States v. Halper"><em>Id., </em>at 449</a></span>. The value of the conveyances and real property forfeitable under §§ 881(a)(4) and (a)(7), on the other hand, can vary so dramatically that any relationship between the Government’s actual costs and the amount of the sanction is merely coincidental. See <em>Ward, </em><span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#254" aria-description="Citation for case: United States v. Ward">448 U. S., at 254</a></span>. Furthermore, as we have seen, forfeiture statutes historically have been understood as serving not simply remedial goals but also those of punishment and deterrence. Finally, it appears to make little practical difference whether the Excessive Fines Clause applies to all forfeitures under §§ 881(a)(4) and (a)(7) or only to those that cannot be characterized as purely remedial. The Clause prohibits only the imposition of “excessive” fines, and a fine that serves purely remedial purposes cannot be considered “excessive” in any event.</p>
</footnote>
<footnote label="15">
<p id="b665-11"> Justice Scalia suggests that the sole measure of an <em>in rem </em>forfeiture’s excessiveness is the relationship between the forfeited property and the offense. See <em>post, </em>at 627-628. We do not rule out the possibility that the connection between the property and the offense may be relevant, but our decision today in no way limits the Court of Appeals from considering other factors in determining whether the forfeiture of Austin’s property was excessive.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Bailey v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Bailey v. United States"
type: case
citation: "568 U.S. 186 (2013)"
parallel_cite: "133 S. Ct. 1031; 185 L. Ed. 2d 19"
neutral_cite: 2013 U.S. LEXIS 1075
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-02-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-02-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Bailey v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/820749/bailey-v-united-states/"
  cluster_id: 820749
  opinion_id: 9502775
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
related: ["[[Michigan v. Summers]]", "[[Illinois v. McArthur]]", "[[Terry v. Ohio]]"]
aliases: ["Bailey v. US"]
tags: ["case", "fourth-amendment", "detention", "search-warrant", "securing-the-scene"]
holding: "The detention authority recognized in Michigan v. Summers is limited to the immediate vicinity of the premises to be searched; it does…"
lake:
  record_id: Bailey v. United States
  status: verified
  projected_at: 2026-07-09
---

# Bailey v. United States

*568 U.S. 186 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant to search a basement apartment for a handgun. Before executing it, surveillance officers saw Bailey and another man leave the apartment by car. Officers followed and stopped them roughly a mile away, detained Bailey, patted him down, and drove him back to the apartment. The search turned up a gun and drugs, and a key in Bailey's possession opened the apartment door. The detention was justified below under [[Michigan v. Summers]], which allows detaining occupants while a search warrant is executed.

## Issue
Whether the *[[Michigan v. Summers|Summers]]* authority to detain occupants incident to the execution of a search warrant extends to a former occupant who has already left and is stopped away from the immediate vicinity of the premises.

## Rule
No — the *[[Michigan v. Summers|Summers]]* detention authority is spatially limited. "A spatial constraint defined by the immediate vicinity of the premises to be searched is therefore required for detentions incident to the execution of a search warrant." — 568 U.S. at 201 (slip op., at 13). ^pin-201

The interests *[[Michigan v. Summers|Summers]]* serves (officer safety, orderly completion of the search, preventing flight) do not reach a former occupant who has departed: that flight-prevention interest "does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched." — [*Id.* at 199](https://www.courtlistener.com/opinion/820749/bailey-v-united-states/#:~:text=does%20not%20independently%20justify%20detention) (slip op., at 11). ^pin-199

## Application
Bailey was stopped about a mile from the apartment, well outside its immediate vicinity, after he had already left (apparently unaware of the impending search). Because he was not within the immediate vicinity, the *[[Michigan v. Summers|Summers]]* rule did not authorize his detention; absent that categorical authority, the officers would have needed probable cause to arrest or reasonable suspicion to make a *[[Terry v. Ohio|Terry]]* stop.

## Conclusion
The detention was not authorized by *[[Michigan v. Summers|Summers]]*; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to consider whether the stop could be justified on other grounds (e.g., *[[Terry v. Ohio|Terry]]*).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Bailey*. *Bailey* **limits** [[Michigan v. Summers]] by confining the categorical, suspicionless detention authority to the immediate vicinity of the premises being searched.

## Appears on
- [[Securing the Scene]] — *Key — Progeny / Refinement*

## Sources
- *Bailey v. United States*, 568 U.S. 186 (2013) — https://www.courtlistener.com/opinion/820749/bailey-v-united-states/ — pinpoints: 199, 201 (CL carries the slip opinion; cited at slip op. 11, 13).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "459676fa5e72cbd7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "568 U.S. 186 (2013)", "court": "U.S. Supreme Court", "neutral_cite": "2013 U.S. LEXIS 1075", "official_citation_present": true, "parallel_cite": "133 S. Ct. 1031; 185 L. Ed. 2d 19", "title": "Bailey v. United States", "year": "2013"}}
{"assertion_id": "0d7f9e42601e365e", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (scene-securing overlap)", "title": "Bailey v. United States"}}
{"assertion_id": "4d8869a6a066ccc1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The detention authority recognized in Michigan v. Summers is limited to the immediate vicinity of the premises to be searched; it does…", "title": "Bailey v. United States"}}
{"assertion_id": "53052c7219369066", "dimension": "support", "kind": "home_role", "locator": {"home": "Detention and Search of Persons at the Scene"}, "payload": {"home": "Detention and Search of Persons at the Scene", "role": "Key — Progeny / Refinement", "title": "Bailey v. United States"}}
{"assertion_id": "11bb3bb34c905e51", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bailey v. United States"}}
{"assertion_id": "ee060dd2d8146861", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2013-02-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Bailey v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Bailey v. United States", "varies_by_point": "false"}}
```

### lake record — Bailey v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bailey v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Bailey v. United States",
    "case_name_short": "Bailey",
    "case_name_full": "Bailey v. United States",
    "input_case_name": "Bailey v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-02-19",
    "year": 2013,
    "docket": null,
    "cluster_id": 820749,
    "lead_opinion_id": 9502775,
    "sibling_ids": [
      820749,
      9502775,
      9502776,
      9502777
    ],
    "absolute_url": "/opinion/820749/bailey-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8412656,
        "score": 10,
        "case_name": "Bailey v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "568 U.S. 186",
      "volume": "568",
      "reporter": "U.S.",
      "page": "186",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "133 S. Ct. 1031",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 19",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "19",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 1075",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1031",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 19",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "19",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 1075",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "568 U.S. 186",
        "volume": "568",
        "reporter": "U.S.",
        "page": "186",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "568 U.S. 186",
    "official_selection": {
      "court_class": "scotus",
      "selected": "568 U.S. 186",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-201",
      "page": null,
      "quote": "--- # Bailey v. United States *568 U.S. 186 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search a basement apartment for a handgun. Before executing it, surveillance officers saw Bailey and another man leave the apartment by car. Officers followed and stopped them roughly a mile away, detained Bailey, patted him down, and drove him back to the apartment. The search turned up a gun and drugs, and a key in Bailey's possession opened the apartment door. The detention was justified below under [[Michigan v. Summers]], which allows detaining occupants while a search warrant is executed. ## Issue Whether the *Summers* authority to detain occupants incident to the execution of a search warrant extends to a former occupant who has already left and is stopped away from the immediate vicinity of the premises. ## Rule No \u2014 the *Summers* detention authority is spatially limited.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-199",
      "page": null,
      "quote": "does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched.",
      "star_marker": "199",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 29407,
      "fragment": "#:~:text=does%20not%20independently%20justify%20detention",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-02-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Bailey v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Muldrow",
          "cluster_id": 4448772,
          "cite": [
            "2017 Ohio 8839",
            "100 N.E.3d 1093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
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
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathan Albert Leal v. State",
          "cluster_id": 2751234,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane1_negative"
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
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaun J. Matz v. Rodney Klotka",
          "cluster_id": 2739950,
          "cite": [
            "769 F.3d 517",
            "2014 U.S. App. LEXIS 19074",
            "2014 WL 4960311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Americans for Prosperity Foundation v. Bonta",
          "cluster_id": 4896549,
          "cite": [
            "594 U.S. 595",
            "210 L. Ed. 2d 716",
            "141 S. Ct. 2373"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Antoine D. Watts(074556)",
          "cluster_id": 3159265,
          "cite": [
            "223 N.J. 503",
            "126 A.3d 1216",
            "2015 N.J. LEXIS 1239"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "C. B. v. City of Sonora",
          "cluster_id": 2743611,
          "cite": [
            "769 F.3d 1005",
            "89 Fed. R. Serv. 3d 1624",
            "2014 U.S. App. LEXIS 19757",
            "2014 WL 5151632"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bailey",
          "cluster_id": 2654019,
          "cite": [
            "743 F.3d 322",
            "2014 WL 657932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eric Brodie",
          "cluster_id": 2653533,
          "cite": [
            "408 U.S. App. D.C. 326",
            "742 F.3d 1058",
            "2014 WL 593264",
            "2014 U.S. App. LEXIS 2874"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 4759018,
          "cite": [
            "961 F.3d 181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hackney",
          "cluster_id": 3218181,
          "cite": [
            "2016 Ohio 4609"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Delade v. John Cargan",
          "cluster_id": 4778175,
          "cite": [
            "972 F.3d 207"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jack Bruce Folk",
          "cluster_id": 2678192,
          "cite": [
            "754 F.3d 905",
            "2014 WL 2611272",
            "2014 U.S. App. LEXIS 10929"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregorio Perez Cruz v. William Barr",
          "cluster_id": 4629270,
          "cite": [
            "926 F.3d 1128"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Isaiah Woodson, Jr.",
          "cluster_id": 6459262,
          "cite": [
            "30 F.4th 1295"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ryan Moderson v. City of Neenah",
          "cluster_id": 10581758,
          "cite": [
            "137 F.4th 611"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Furlow v. Jon Belmar",
          "cluster_id": 8436813,
          "cite": [
            "52 F.4th 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Karamanoglu v. Town of Yarmouth",
          "cluster_id": 5178962,
          "cite": [
            "15 F.4th 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Moorer v. City of Chicago",
          "cluster_id": 9473951,
          "cite": [
            "92 F.4th 715"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Lewis",
          "cluster_id": 4412774,
          "cite": [
            "864 F.3d 937",
            "2017 WL 3186308",
            "2017 U.S. App. LEXIS 13583"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chacker v. JPMorgan Chase Bank, N.A.",
          "cluster_id": 6239907,
          "cite": [
            "237 Cal. Rptr. 3d 921",
            "27 Cal. App. 5th 351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mason",
          "cluster_id": 4299107,
          "cite": [
            "2016 Ohio 7081"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wilson",
          "cluster_id": 4576198,
          "cite": [
            "821 S.E.2d 811",
            "371 N.C. 920"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kaul",
          "cluster_id": 4374844,
          "cite": [
            "2017 ND 56",
            "891 N.W.2d 352",
            "2017 N.D. LEXIS 56",
            "2017 WL 968845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Bailey v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 95,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 95,
        "triage_read": 8,
        "triage_snippet_classified": 87
      },
      "lane2_top_cited": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zJnM9NDMzMjI4MCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28820749+OR+9502775+OR+9502776+OR+9502777%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(820749 OR 9502775 OR 9502776 OR 9502777)",
    "indexed_citing_opinions": 122,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 820749,
        "count": 76,
        "count_source": "search"
      },
      {
        "opinion_id": 9502775,
        "count": 46,
        "count_source": "search"
      },
      {
        "opinion_id": 9502776,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9502777,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/bailey-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MDk1OSZzPTY0NTkyNjImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28820749+OR+9502775+OR+9502776+OR+9502777%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 820749,
        "cited_id": 27226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 145728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 183973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 220356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 565019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 618288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820749,
        "cited_id": 2531019,
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
    "date_created": "2026-07-04T19:16:10Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:20:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:16:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Bailey v. United States

```
<opinion type="majority">
<author id="b407-5">Justice Kennedy</author>
<p id="AJ">delivered the opinion of the Court.</p>
<p id="b407-6">The Fourth Amendment guarantees the right to be free from unreasonable searches and seizures. A search may be of a person, a thing, or a place. So too a seizure may be of a person, a thing, or even a place. A search or a seizure may occur singly or in combination, and in differing sequence. In some cases the validity of one determines the validity of the other. The instant case involves the search of a place (an apartment dwelling) and the seizure of a person. But here, though it is acknowledged that the search was lawful,.it does not follow that the seizure was lawful as well. The seizure of the person is quite in question. The issue to be resolved is whether the seizure of the person was reasonable when he was stopped and detained at some distance away from the premises to be searched when the only justification for <page-number citation-index="1" label="190">*190</page-number>the detention was to ensure the safety and efficacy of the search.</p>
<p id="b408-5">I</p>
<p id="b408-6">A</p>
<p id="b408-7">At 8:45 p.m. on July 28, 2005, local police obtained a warrant to search a residence for a .380-caliber handgun. The residence was a basement apartment at 103 Lake Drive, in Wyandanch, New York. A confidential informant had told police he observed the gun when he was at the apartment to purchase drugs from “a heavy set black male with short hair” known as “Polo.” App. 16-26. As the search unit began preparations for executing the warrant, two officers, Detectives Richard Sneider and Richard Gorbecki, were conducting surveillance in an unmarked car outside the residence. About 9:56 p.m., Sneider and Gorbecki observed two men—later identified as petitioner Chunon Bailey and Bryant Middleton—leave the gated area above the basement apartment and enter a car parked in the driveway. Both matched the general physical description of “Polo” provided by the informant. There was no indication that the men were aware of the officers’ presence or had any knowledge of the impending search. The detectives watched the car leave the driveway. They waited for it to go a few hundred yards down the street and followed. The detectives informed the search team of their intent to follow and detain the departing occupants. The search team then executed the search warrant at the apartment.</p>
<p id="b408-8">Detectives Sneider and Gorbecki tailed Bailey’s car for about a mile—and for about five minutes—before pulling the vehicle over in a parking lot by a fire station. They ordered Bailey and Middleton out of the car and did a patdown search of both men. The officers found no weapons but discovered a ring of keys in Bailey’s pocket. Bailey identified himself and said he was coming from his home at 103 Lake Drive. His driver’s license, however, showed his address as Bay-<page-number citation-index="1" label="191">*191</page-number>shore, New York, the town where the confidential informant told the police the suspect, “Polo,” used to live. <em>Id., </em>at 89. Bailey’s passenger, Middleton, said Bailey was giving him a ride home and confirmed they were coming from Bailey’s residence at 103 Lake Drive. The officers put both men in handcuffs. When Bailey asked why, Gorbecki stated that they were being detained incident to the execution of a search warrant at 103 Lake Drive. Bailey responded: “I don’t live there. Anything you find there ain’t mine, and I’m not cooperating with your investigation.” <em>Id., </em>at 57, 77.</p>
<p id="Amr">The detectives called for a patrol cár to take Bailey and Middleton back’ to the Lake Drive apartment. Detective Sneider drove the unmarked car back, while Detective Gor-becki used Bailey’s set of keys to drive Bailey’s car back to the search scene. By the time the group returned to 103 Lake Drive, the search team had discovered a gun and drugs in plain view inside the apartment. Bailey and Middleton were placed under arrest, and Bailey’s keys were seized incident to the arrest. Officers later discovered that one of Bailey’s keys opened the door of the basement apartment.</p>
<p id="b409-6">B</p>
<p id="b409-7">Bailey was charged with three federal offenses: possession of cocaine with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and (b)(1)(B)(iii); possession of a firearm by a felon, in violation of <span class="citation no-link">18 U. S. C. § 922</span>(g)(1); and possession of a firearm in furtherance of a drug-trafficking offense, in violation of § 924(c)(1)(A)(i). At trial Bailey moved to suppress the apartment key and the statements he made when stopped by Detectives Sneider and Gorbecki. That evidence, Bailey argued, derived from an unreasonable seizure. After an evidentiary hearing the United States District Court for the Eastern District of New York denied the motion to suppress. The District Court held that Bailey’s detention was permissible under <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), as a detention incident to the execution of <page-number citation-index="1" label="192">*192</page-number>a search warrant. In the alternative, it held that Bailey’s detention was lawful as an investigatory detention supported by reasonable suspicion under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). After a trial the jury found Bailey guilty on all three counts.</p>
<p id="b410-6">The Court of Appeals for the Second Circuit ruled that Bailey’s detention was proper and affirmed denial of the suppression motion. It interpreted this Court’s decision in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to “authoriz[e] law enforcement to detain the occupant of premises subject to a valid search warrant when that person is seen leaving those premises and the detention is effected <em>as soon as reasonably practicable.” </em><span class="citation" data-id="220356"><a href="/opinion/220356/united-states-v-bailey/#208" aria-description="Citation for case: United States v. Bailey">652 F. 3d 197, 208</a></span> (2011). Having found Bailey’s detention justified under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court of Appeals did not address the District Court’s alternative holding that the stop was permitted under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b410-7">The Federal Courts of Appeals have reached differing conclusions as to whether <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>justifies the detention of occupants beyond the immediate vicinity of the premises covered by a search warrant. This Court granted certiorari to address the question. <span class="citation multiple-matches"><a href="/c/U.%20S./566/1033/">566 U. S. 1033</a></span> (2012).</p>
<p id="pAa9">H—i</p>
<p id="b410-3">The Fourth Amendment, applicable through the- Four- ' teenth Amendment to the States, provides: “The right of the people to be secure in their persons ... against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause . . . particularly describing the place to be searched, and the persons or things to be seized.” This Court has stated “the general rule that Fourth Amendment seizures are ‘reasonable’ only if based on probable cause” to believe that the individual has committed a crime. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213</a></span> (1979). The standard of probable cause, with “roots that are deep in our history,” <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959), “represent[s] the accumulated wisdom of precedent and ex<page-number citation-index="1" label="193">*193</page-number>perience as to the minimum justification necessary to make the kind of intrusion involved in an arrest ‘reasonable’ under the Fourth Amendment.” <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 208</a></span>.</p>
<p id="b411-5">Within the framework of these fundamental rules there is some latitude for police to detain where “the intrusion on the citizen’s privacy ‘was so much less severe’ than that involved in a traditional arrest that ‘the opposing interests in crime prevention and detection and in the police officer’s safety’ could support the seizure as reasonable.” <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers, supra,</a></span> </em>at 697-698 (quoting <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York"><em>Dunaway, supra, </em>at 209</a></span>); see also <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span> (holding that a police officer who has reasonable suspicion of criminal activity may conduct a brief investigative stop).</p>
<p id="b411-6">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court defined an important category of cases in which detention is allowed without probable cause to arrest for a crime. It permitted officers executing a search warrant “to detain the occupants of the premises while a proper search is conducted.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 705</a></span>. The rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>extends further than some earlier exceptions because it does not require law enforcement to have particular suspicion that an individual is involved in criminal activity or poses a specific danger to the officers. <em>Muehler </em>v. <em>Mena, </em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U. S. 93</a></span> (2005). In <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span>, </em>applying the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court stated: “An officer’s authority to detain incident to a search is categorical; it does not depend on the ‘quantum of proof justifying detention or the extent of the intrusion to be imposed by the seizure.’ ” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U. S., at 98</a></span> (quoting <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers"><em>Summers, supra, </em>at 705, n. 19</a></span>). The rule, announced in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>allows detention incident to the execution of a search warrant “because the character of the additional intrusion caused by detention is slight and because the justifications for detention are substantial.” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#98" aria-description="Citation for case: Muehler v. Mena"><em>Muehler, supra, </em>at 98</a></span>.</p>
<p id="b411-7">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>and later cases, the occupants detained were found within or immediately outside a residence at the moment the police officers executed the search warrant. In <page-number citation-index="1" label="194">*194</page-number><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the defendant was detained on a walk leading down from the front steps of the house. See Tr. of Oral Arg. in O. T. 1980, No. 79-1794, pp. 41-42; see also <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#96" aria-description="Citation for case: Muehler v. Mena"><em>Muehler, supra, </em>at 96</a></span> (detention of occupant in adjoining garage); <em>Los Angeles County </em>v. <em>Rettele, </em><span class="citation" data-id="9435063"><a href="/opinion/145728/los-angeles-county-california-v-rettele/#611" aria-description="Citation for case: Los Angeles County, California v. Rettele">550 U. S. 609, 611</a></span> (2007) <em>(per curiam) </em>(detention of occupants in bedroom). Here, however, petitioner left the apartment before the search began; and the police officers waited to detain him until he was almost a mile away. The issue is whether the reasoning in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>can justify detentions beyond the immediate vicinity of the premises being searched. An exception to the Fourth Amendment rule prohibiting detention absent probable cause must not diverge from its purpose and rationale. See <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality opinion) (“The scope of the detention must be carefully tailored to its underlying justification”)- It is necessary, then, to discuss the reasons for the rule explained in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to determine if its rationale extends to a detention like the one here.</p>
<p id="b412-5">A</p>
<p id="b412-6">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court recognized three important law enforcement interests that, taken together, justify the detention of an occupant who is on the premises during the execution of a search warrant: officer safety, facilitating the completion of the search, and preventing flight. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702-703</a></span>.</p>
<p id="b412-7">1</p>
<p id="b412-8">The first interest identified in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was “the interest in minimizing the risk of harm to the officers.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702</a></span>. There the Court held that “the execution of a warrant to search for narcotics is the kind of transaction that may give rise to sudden violence or frantic efforts to conceal or destroy evidence,” and “[t]he risk of harm to both the police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702-703</a></span>.</p>
<p id="b413-3"><page-number citation-index="1" label="195">*195</page-number>When law enforcement officers execute a search warrant, safety considerations require that they secure the premises, which may include detaining current occupants. By taking “unquestioned command of. the situation,” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers"><em>id., </em>at 703</a></span>, the officers can search without fear that occupants, who are on the premises and able to observe the course of the search, will become disruptive, dangerous, or otherwise frustrate the search.</p>
<p id="b413-4">After <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>this Court decided <em>Muehler </em>v. <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Mena</a></span>. </em>The reasoning and conclusions in <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span> </em>in applying the <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>rule go quite far in allowing seizure and detention of persons to accommodate the necessities of a search. There, the person detained and held in handcuffs was not suspected of the criminal activity being investigated; but, the Court held, she could be detained nonetheless, to secure the premises while the search was underway. The “safety risk inherent in executing a search warrant for weapons was sufficient to justify the use of handcuffs, [and] the need to detain multiple occupants made the use of handcuffs all the more reasonable.” <span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/#100" aria-description="Citation for case: Muehler v. Mena">544 U. S., at 100</a></span>. While the Court in <em><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">Muehler</a></span> </em>did remand for consideration of whether the detention there—alleged to have been two or three hours—was necessary in light of all the circumstances, the fact that so prolonged a detention indeed might have been permitted illustrates the far-reaching authority the police have when the detention is made at the scene of the search. This in turn counsels caution before extending the power to detain persons stopped or apprehended away from the premises where the search is being conducted.</p>
<p id="b413-5">It is likely, indeed almost inevitable in the case of a resident, that an occupant will return to the premises at some point; and this might occur when the officers are still conducting the search. Officers can and do mitigate that risk, however, by taking routine precautions, for instance by erecting barricades or posting someone on the perimeter or at the door. In the instant case Bailey had left the premises, <page-number citation-index="1" label="196">*196</page-number>apparently without knowledge of the search. He posed little risk to the officers at the scene. If Bailey had rushed back to his apartment, the police could have apprehended and detained him under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>. </em>There is no established principle, however, that allows the arrest of anyone away from the premises who is likely to return.</p>
<p id="b414-5">The risk, furthermore, that someone could return home during the execution of a search warrant is not limited to occupants who depart shortly before the start of a search. The risk that a resident might return home, either for reasons unrelated to the search or after being alerted by someone at the scene, exists whether he left five minutes or five hours earlier. Unexpected arrivals by occupants or other persons accustomed to visiting the premises might occur in many instances. Were police to have the authority to detain those persons away from the premises, the authority to detain incident to the execution of a search warrant would reach beyond the rationale of ensuring the integrity of the search by detaining those who are in fact on the scene.</p>
<p id="b414-6">The Court of Appeals relied on an additional safety consideration. It concluded that limiting the application of the authority to detain to the immediate vicinity would put law enforcement officers in a dilemma. They would have to choose between detaining an individual immediately (and risk alerting occupants still inside) or allowing the individual to leave (and risk not being able to arrest him later if incriminating evidence were discovered). <span class="citation" data-id="220356"><a href="/opinion/220356/united-states-v-bailey/#205" aria-description="Citation for case: United States v. Bailey">652 F. 3d, at 205-206</a></span>. Although the danger of alerting occupants who remain inside may be of real concern in some instances, as in the case when a no-knock warrant has been issued, this safety rationale rests on the false premise that a detention must take place. If the officers find that it would be dangerous to detain a departing individual in front of a residence, they are not required to stop him. And, where there are grounds to believe the departing occupant is dangerous, or involved in criminal activity, police will generally not need <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to <page-number citation-index="1" label="197">*197</page-number>detain him at least for brief questioning, as they can rely instead on <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</em></p>
<p id="b415-5">The risk that a departing occupant might notice the police surveillance and alert others still inside the residence is also an insufficient safety rationale to justify expanding the existing categorical authority to detain so that it extends beyond the immediate vicinity of the premises to be searched. If extended in this way the rationale would justify detaining anyone in the neighborhood who could alert occupants that the police are outside, all without individualized suspicion of criminal activity or connection to the residence to be •searched. This possibility demonstrates why it is necessary to confine the <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>rule to those who are present when and where the search is being conducted.</p>
<p id="b415-6">2</p>
<p id="b415-7">The second law enforcement interest relied on in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was that “the orderly completion of the search may be facilitated if the occupants of the premises are present.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 703</a></span>. This interest in efficiency derives from distinct, but related, concerns.</p>
<p id="b415-8">If occupants are permitted to wander around the premises, there is the potential for interference with the execution of the search warrant. They can hide or destroy evidence, seek to distract the officers, or simply get'in the way. Those risks are not presented by an occupant who departs beforehand. So, in this case, after Bailey drove away from the Lake Drive apartment, he was not a threat to the proper execution of the search. Had he returned, officers would have been free to detain him at that point. A general interest in avoiding obstruction of a search, however, cannot justify detention beyond the vicinity of the premises to be searched.</p>
<p id="b415-9"><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>also noted that occupants can assist the officers. Under the reasoning in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the occupants’ “self-interest may induce them to open locked doors or locked con<page-number citation-index="1" label="198">*198</page-number>tainers to avoid the use of force that is not only damaging to property but may also delay the completion of the task at hand.” <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Ibid.</a></span> </em>This justification must be confined to those persons who are on site and so in a position, when detained, to at once observe the progression of the search; and it would have no limiting principle were it to be applied to persons beyond the premises of the search. Here, it appears the police officers decided to wait until Bailey had left the vicinity of the search before detaining him. In any event it later became clear to the officers that Bailey did not wish to cooperate. See App. 57, 77 (“I don’t live there. Anything you find there ain’t mine, and I’m not cooperating with your investigation”). And, by the time the officers brought Bailey back to the apartment, the search team had discovered contraband. Bailey’s detention thus served no purpose in ensuring the efficient completion of the search.</p>
<p id="b416-5">a</p>
<p id="b416-6">The third law enforcement interest addressed in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>was the “the legitimate law enforcement interest in preventing flight in the event that incriminating evidence is found.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 702</a></span>. The proper interpretation of this language, in the context of <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>and in the broader context of the reasonableness standard that must govern and inform the detention incident to a search, is that the police can prohibit an occupant from leaving the scene of the search. As with the other interests identified in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>this justification serves to preserve the integrity of the search by controlling those persons who are on the scene. If police officers are concerned about flight, and have to keep close supervision of occupants who are not restrained, they might rush the search, causing unnecessary damage to property or compromising its careful execution. Allowing officers to secure the scene by detaining those present also prevents the search from being impeded by occupants leaving with the evidence being sought or the means to find it.</p>
<p id="b417-4"><page-number citation-index="1" label="199">*199</page-number>The concern over flight is not because of the danger of flight itself but because of the damage that potential flight can cause to the integrity of the search. This interest does not independently justify detention of an occupant beyond the immediate vicinity of the premises to be searched. The need to prevent flight, if unbounded, might be used to argue for detention, while a search is underway, of any regular occupant regardless of his or her location at the time of the search. If not circumscribed, the rationale of preventing flight would justify, for instance, detaining a suspect who is 10 miles away, ready to board a plane. The interest in preventing escape from police cannot extend this far without undermining the usual rules for arrest based on probable cause or a brief stop for questioning under standards derived from <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>Even if the detention of a former occupant away from the premises could facilitate a later arrest should incriminating evidence be discovered, “the mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment.” <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978).</p>
<p id="b417-5">In sum, of the three law enforcement interests identified to justify the detention in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>none applies with the same or similar force to the detention of recent occupants beyond the immediate vicinity of the premises to be searched. Any of the individual interests is also insufficient, on its own, to justify an expansion of the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to permit the detention of a former occupant, wherever he may be found away from the scene of the search. This would give officers too much discretion. The categorical authority to detain incident to the execution of a search warrant must be limited to the immediate vicinity of the premises to be searched.</p>
<p id="b417-6">B</p>
<p id="b417-7">In <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span>, </em>the Court recognized the authority to detain occupants incident to the execution of a search warrant not only in light of the law enforcement interests at stake but <page-number citation-index="1" label="200">*200</page-number>also because the intrusion on personal liberty was limited. The Court held detention of a current occupant “represents only an incremental intrusion on personal liberty when the search of a home has been authorized by a valid warrant.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#703" aria-description="Citation for case: Michigan v. Summers">452 U. S., at 703</a></span>. Because the detention occurs in the individual’s own home, “it could add only minimally to the public stigma associated with the search itself and would involve neither the inconvenience nor the indignity associated with a compelled visit to the police station.” <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 702</a></span>.</p>
<p id="b418-5">Where officers arrest an individual away from his home, however, there is an additional level of intrusiveness. A public detention, even if merely incident to a search, will resemble a full-fledged arrest. As demonstrated here, detention beyond the immediate vicinity can involve an initial detention away from the scene and a second detention at the residence. In between, the individual will suffer the additional indignity of a compelled transfer back to the premises, giving all the appearances of an arrest. The detention here was more intrusive than a usual detention at the search scene. Bailey’s car was stopped; he was ordered to step out and was detained in full public view; he was handcuffed, transported in a marked patrol car, and detained further outside the apartment. These facts illustrate that detention away from a premises where police are already present often will be more intrusive than detentions at the scene.</p>
<p id="b418-6">C</p>
<p id="b418-7"><em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>recognized that a rule permitting the detention of occupants on the premises during the execution of a search warrant, even absent individualized suspicion, was reasonable and necessary in light of the law enforcement interests in conducting a safe and efficient search. Because this exception grants substantial authority to police officers to detain outside of the traditional rules of the Fourth Amendment, it must be circumscribed.</p>
<p id="b419-4"><page-number citation-index="1" label="201">*201</page-number>A spatial constraint defined by the immediate vicinity of the premises to be searched is therefore required for detentions incident to the execution of a séarch warrant. The police action permitted here—the .search of a residence—has a spatial dimension, and so a spatial or geographical boundary can be used to determine the area within which both the search and detention incident to that search may occur. Limiting the rule in <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to the area in which an occupant poses a real threat to the safe and efficient execution of a search warrant ensures that the scope of the detention incident to a search is confined to its underlying justification. Once an occupant is beyond the immediate vicinity of the premises to be searched, the search-related law enforcement interests are diminished and the. intrusiveness of the detention is more severe.</p>
<p id="b419-5">Here, petitioner was detained at a point beyond any reasonable understanding of the immediate vicinity of the premises in question; and so this case presents neither the necessity nor the occasion to further define the meaning of immediate vicinity. In closer cases courts can consider a number of factors to determine whether an occupant was detained within the immediate vicinity of the premises to be searched, including the lawful limits of the premises, whether the occupant was within the line of sight of his dwelling, the ease of reentry from the occupant’s location, and other relevant factors.</p>
<p id="b419-6">Confining an officer’s authority to detain under <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>to the immediate vicinity of a premises to be searched is a proper limit because it accords with the rationale of the rule. The rule adopted by the Court of Appeals here, allowing detentions of a departed occupant “as soon as reasonably practicable,” departs from the spatial limit that is necessary to confine the rule in light of the substantial intrusions on the liberty of those detained. Because detention is justified by the interests in executing a safe and efficient search, the decision to detain must be acted upon at the scene of the <page-number citation-index="1" label="202">*202</page-number>search and not at a later time in a more remote place. If officers elect to defer the detention until the suspect or departing occupant leaves the immediate vicinity, the lawfulness of detention is controlled by other standards, including, of course, a brief stop for questioning based on reasonable suspicion under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>or an arrest based on probable cause. A suspect’s particular actions in leaving the scene, including whether he appears to be armed or fleeing with the evidence sought, and any information the officers acquire from those who are conducting the search, including information that incriminating evidence has been discovered, will bear, of course, on the lawfulness of a later stop or detention. For example, had the search team radioed Detectives Sneider and Gorbecki about the gun and drugs discovered in the Lake Drive apartment as the officers stopped Bailey and Middleton, this may have provided them with probable cause for an arrest.</p>
<p id="b420-5">Ill</p>
<p id="b420-6">Detentions incident to the execution of a search warrant are reasonable under the Fourth Amendment because the limited intrusion on personal liberty is outweighed by the special law enforcement interests at stake. Once an individual has left the immediate vicinity of a premises to be searched, however, detentions must be justified by some other rationale. In this respect it must be noted that the District Court, as an alternative ruling, held that stopping petitioner was lawful under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>This opinion expresses no view on that issue. It will be open, on remand, for the Court of Appeals to address the matter and to determine whether, assuming the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop was valid, it yielded information that justified the detention the officers then imposed.</p>
<p id="b420-7">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b420-8">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/Banks v. Dretke.md  (`case`, 5 assertions)

### content_page

```
---
title: "Banks v. Dretke"
type: case
citation: ""
parallel_cite: "540 U.S. 668; 124 S. Ct. 1256; 157 L. Ed. 2d 1166; 72 U.S.L.W. 4193; 17 Fla. L. Weekly Fed. S 153"
neutral_cite: 2004 U.S. LEXIS 1621
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-02-24
docket: 02-8286
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Banks v. Dretke
  varies_by_point: false
  scope_note: "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131165/banks-v-dretke/"
  cluster_id: 131165
  opinion_id: 131165
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Strickler v. Greene]]", "[[Giglio v. United States]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]", "[[Napue v. Illinois]]"]
aliases: []
tags: ["case", "brady", "giglio", "impeachment-evidence", "informant", "prosecutorial-misconduct", "due-process"]
holding: "A Brady violation occurred where the State withheld that a key prosecution witness was a paid police informant and affirmatively represented it had disclosed everything; a defendant who reasonably relies on the prosecution's representations does not forfeit the claim by failing to discover the concealed evidence — 'prosecutor may hide, defendant must seek' is not tenable."
lake:
  record_id: Banks v. Dretke
  status: verified
  projected_at: 2026-07-06
---

# Banks v. Dretke

*540 U.S. 668 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Delma Banks was convicted of capital murder and sentenced to death in Texas. Two key prosecution witnesses, Robert Farr and Charles Cook, helped secure the conviction and death sentence. Farr — who supplied much of the evidence that Banks would commit future violence — was in fact a paid police informant, and the State had also withheld a transcript of a pretrial interview in which Cook's testimony was coached. Throughout trial and state postconviction proceedings the prosecution represented that it had disclosed everything and even denied that Farr was an informant. Banks raised the suppressed-evidence claims on federal [[Common Legal Terms#habeas-corpus|habeas]].

## Issue
Whether Banks established a Brady violation as to Farr's concealed informant status — and whether his failure, in state proceedings, to prove what the State had hidden barred federal [[Common Legal Terms#habeas-corpus|habeas]] relief.

## Rule
The Court reiterated *[[Brady v. Maryland|Brady]]*'s rule and the three-part test from [[Strickler v. Greene]]: a *[[Brady v. Maryland|Brady]]* "prosecutorial misconduct claim" has three essential components — "The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." — 540 U.S. at 691 (quoting *Strickler*, 527 U.S. at 281–282). ^pin-691

A defendant need not police the prosecution's honesty. "A rule thus declaring 'prosecutor may hide, defendant must seek,' is not tenable in a system constitutionally bound to accord defendants due process." — 540 U.S. at 696. ^pin-696

Where the State elects to call an informant as a witness, "[n]othing in *Roviaro*, or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion." — 540 U.S. at 698. ^pin-698

## Application
Farr was a paid informant and a key witness at both the guilt and penalty phases of Banks's capital trial, so his concealed status was favorable impeachment evidence; the State suppressed it, even affirmatively denying he was an informant; and the suppression prejudiced Banks at sentencing. Because the prosecution represented at trial and in postconviction that it had held nothing back, "[i]t was not incumbent on Banks to prove these representations false; rather, Banks was entitled to treat the prosecutor's submissions as truthful." His failure to obtain investigative assistance or to prove the concealment earlier therefore did not bar the claim — the State's own concealment supplied the "cause," and the same facts established the *[[Brady v. Maryland|Brady]]* prejudice. The Court reversed the dismissal of the Farr claim and the denial of a certificate of appealability on the Cook claim.

## Conclusion
Reversed in relevant part. Banks established (or was entitled to develop) a *[[Brady v. Maryland|Brady]]* violation as to Farr's concealed informant status; a defendant's reasonable reliance on the prosecution's representations excuses a failure to uncover the suppressed evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Ginsburg, J.; Thomas, J., joined in part by Scalia, J., concurring in part and dissenting in part).
- *Banks* sits in the [[Brady v. Maryland]] / [[Giglio v. United States]] impeachment-disclosure line and applies the [[Strickler v. Greene]] three-component framework and the materiality logic of [[Kyles v. Whitley]] and [[United States v. Bagley]]. It is the leading rejection of a "due diligence" defense to suppression. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Banks v. Dretke*, 540 U.S. 668 (2004) — https://www.courtlistener.com/opinion/131165/banks-v-dretke/ — pinpoints: 691, 696, 698.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b2bd6437cfae09f0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 1621", "official_citation_present": false, "parallel_cite": "540 U.S. 668; 124 S. Ct. 1256; 157 L. Ed. 2d 1166; 72 U.S.L.W. 4193; 17 Fla. L. Weekly Fed. S 153", "title": "Banks v. Dretke", "year": "2004"}}
{"assertion_id": "4f7d9266066381e9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A Brady violation occurred where the State withheld that a key prosecution witness was a paid police informant and affirmatively represented it had disclosed everything; a defendant who reasonably relies on the prosecution's representations does not forfeit the claim by failing to discover the concealed evidence — 'prosecutor may hide, defendant must seek' is not tenable.", "title": "Banks v. Dretke"}}
{"assertion_id": "80999aa0042a590d", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Banks v. Dretke"}}
{"assertion_id": "af6795fbad8e1eb0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Banks v. Dretke"}}
{"assertion_id": "b067a79c858d1f18", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Banks v. Dretke", "field_i_validity": "good_law", "scope_note": "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim.", "title": "Banks v. Dretke", "varies_by_point": "false"}}
```

### lake record — Banks v. Dretke

```json
{
  "schema_version": "s2.v1",
  "record_id": "Banks v. Dretke",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Banks v. Dretke",
    "case_name_short": "Banks",
    "case_name_full": "Banks v. Dretke, Director, Texas Department of Criminal Justice, Correctional Institutions Division",
    "input_case_name": "Banks v. Dretke",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-02-24",
    "year": 2004,
    "docket": "02-8286",
    "cluster_id": 131165,
    "lead_opinion_id": 131165,
    "sibling_ids": [
      131165,
      9434551,
      9434552
    ],
    "absolute_url": "/opinion/131165/banks-v-dretke/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "540 U.S. 668",
        "volume": "540",
        "reporter": "U.S.",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1256",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1166",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4193",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4193",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 153",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 1621",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1621",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 668",
        "volume": "540",
        "reporter": "U.S.",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1256",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1166",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 1621",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1621",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4193",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4193",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 153",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "153",
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
      "id": "pin-691",
      "page": null,
      "quote": "--- # Banks v. Dretke *540 U.S. 668 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Delma Banks was convicted of capital murder and sentenced to death in Texas. Two key prosecution witnesses, Robert Farr and Charles Cook, helped secure the conviction and death sentence. Farr \u2014 who supplied much of the evidence that Banks would commit future violence \u2014 was in fact a paid police informant, and the State had also withheld a transcript of a pretrial interview in which Cook's testimony was coached. Throughout trial and state postconviction proceedings the prosecution represented that it had disclosed everything and even denied that Farr was an informant. Banks raised the suppressed-evidence claims on federal habeas. ## Issue Whether Banks established a Brady violation as to Farr's concealed informant status \u2014 and whether his failure, in state proceedings, to prove what the State had hidden barred federal habeas relief. ## Rule The Court reiterated *Brady*'s rule and the three-part test from [[Strickler v. Greene]]: a *Brady*",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-696",
      "page": null,
      "quote": "A rule thus declaring 'prosecutor may hide, defendant must seek,' is not tenable in a system constitutionally bound to accord defendants due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-698",
      "page": null,
      "quote": "[n]othing in *Roviaro*, or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Banks v. Dretke",
    "varies_by_point": false,
    "scope_note": "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anthony Juniper v. David Zook",
          "cluster_id": 4443845,
          "cite": [
            "876 F.3d 551"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joshua Frost v. Ron Van Boening",
          "cluster_id": 3187283,
          "cite": [
            "818 F.3d 469",
            "2016 WL 1085228",
            "2016 U.S. App. LEXIS 5077"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Randall Amado v. Terri Gonzalez",
          "cluster_id": 2683349,
          "cite": [
            "758 F.3d 1119",
            "2014 U.S. App. LEXIS 13710",
            "2014 WL 3377340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson",
          "cluster_id": 2659519,
          "cite": [
            "59 F. Supp. 3d 15",
            "2014 U.S. Dist. LEXIS 17008",
            "2014 WL 535461"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson",
          "cluster_id": 2659864,
          "cite": [
            "979 F. Supp. 2d 123",
            "2013 WL 5778318",
            "2013 U.S. Dist. LEXIS 153420"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timothy Hennis v. Frank Hemlick",
          "cluster_id": 621017,
          "cite": [
            "666 F.3d 270",
            "2012 WL 120054",
            "2012 U.S. App. LEXIS 923"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesse Gonzalez v. Robert Wong",
          "cluster_id": 618469,
          "cite": [
            "667 F.3d 965",
            "2011 U.S. App. LEXIS 24191",
            "2011 WL 6061514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Almada",
          "cluster_id": 177469,
          "cite": [
            "640 F.3d 931",
            "2011 WL 941606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mayle v. Felix",
          "cluster_id": 799989,
          "cite": [
            "162 L. Ed. 2d 582",
            "125 S. Ct. 2562",
            "545 U.S. 644",
            "2005 U.S. LEXIS 5016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
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
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodman v. Praxair, Inc.",
          "cluster_id": 1426951,
          "cite": [
            "494 F.3d 458",
            "68 Fed. R. Serv. 3d 850",
            "2007 U.S. App. LEXIS 17631",
            "2007 WL 2121724"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo, United States of America v. Leonard A. Pelullo",
          "cluster_id": 789362,
          "cite": [
            "399 F.3d 197",
            "2005 WL 433589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lambert v. Blackwell",
          "cluster_id": 3013731,
          "cite": [
            "387 F.3d 210"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhoades v. State",
          "cluster_id": 874869,
          "cite": [
            "220 P.3d 1066",
            "148 Idaho 247",
            "2009 Ida. LEXIS 195"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Switzer",
          "cluster_id": 206098,
          "cite": [
            "179 L. Ed. 2d 233",
            "131 S. Ct. 1289",
            "562 U.S. 521",
            "2011 U.S. LEXIS 1905",
            "2011 D.A.R. 3506"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herbert Whitlock v. Charles Bruegge",
          "cluster_id": 801194,
          "cite": [
            "682 F.3d 567",
            "2012 WL 1939906",
            "2012 U.S. App. LEXIS 10825"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chenault",
          "cluster_id": 2710712,
          "cite": [
            "495 Mich. 142",
            "845 N.W.2d 731",
            "2014 Mich. LEXIS 601"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ketterer",
          "cluster_id": 2478526,
          "cite": [
            "2010 OH 3831",
            "126 Ohio St. 3d 448",
            "935 N.E.2d 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Wogenstahl v. Betty Mitchell",
          "cluster_id": 621975,
          "cite": [
            "668 F.3d 307",
            "2012 WL 310819",
            "2012 U.S. App. LEXIS 1905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ketterer",
          "cluster_id": 2691519,
          "cite": [
            "2010 Ohio 3831"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zambrano",
          "cluster_id": 2517801,
          "cite": [
            "163 P.3d 4",
            "63 Cal. Rptr. 3d 297",
            "41 Cal. 4th 1082",
            "2007 Cal. LEXIS 8079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anton E. Barker v. Gary Fleming",
          "cluster_id": 791948,
          "cite": [
            "423 F.3d 1085",
            "2005 U.S. App. LEXIS 19372",
            "5 Cal. Daily Op. Serv. 8151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harm v. State",
          "cluster_id": 1893606,
          "cite": [
            "183 S.W.3d 403",
            "2006 Tex. Crim. App. LEXIS 117",
            "2006 WL 168374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Joseph, Petitioner-Appellant/cross-Appellee v. Ralph Coyle, Warden, Respondent-Appellee/cross-Appellant",
          "cluster_id": 796039,
          "cite": [
            "469 F.3d 441",
            "2006 U.S. App. LEXIS 27697",
            "2006 WL 3250935"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Crow",
          "cluster_id": 4899382,
          "cite": [
            "4 F.4th 982"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Woods v. Stephen Sinclair",
          "cluster_id": 2720496,
          "cite": [
            "764 F.3d 1109",
            "2014 U.S. App. LEXIS 16386",
            "2014 WL 4179917"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Adams Hovey v. Robert L. Ayers, Jr., Acting Warden, California State Prison at San Quentin",
          "cluster_id": 795328,
          "cite": [
            "458 F.3d 892",
            "2006 WL 2325130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Byron Mitchell",
          "cluster_id": 785864,
          "cite": [
            "365 F.3d 215",
            "2004 U.S. App. LEXIS 8474",
            "2004 WL 908359"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lambert v. Blackwell",
          "cluster_id": 788147,
          "cite": [
            "387 F.3d 210",
            "2004 U.S. App. LEXIS 21176"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Socha v. Gary Boughton",
          "cluster_id": 2718114,
          "cite": [
            "763 F.3d 674",
            "2014 WL 3953932",
            "2014 U.S. App. LEXIS 15646"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Barton v. Warden, Southern Ohio Correctional Facility",
          "cluster_id": 2801073,
          "cite": [
            "786 F.3d 450",
            "2015 U.S. App. LEXIS 8020",
            "2015 WL 2262762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131165 OR 9434551 OR 9434552) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjg0MDc2ODAwMDAwJnM9MTc1MTI2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28131165+OR+9434551+OR+9434552%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(131165 OR 9434551 OR 9434552)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzYmcz0xMDQwNTUwJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28131165+OR+9434551+OR+9434552%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131165 OR 9434551 OR 9434552)",
        "reviewed": 31,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 31,
        "triage_read": 2,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131165 OR 9434551 OR 9434552)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131165,
        "count": 390,
        "count_source": "search"
      },
      {
        "opinion_id": 9434551,
        "count": 79,
        "count_source": "search"
      },
      {
        "opinion_id": 9434552,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1115,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/banks-v-dretke.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MTE0MDUmcz05NDg0MjQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28131165+OR+9434551+OR+9434552%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131165,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 106997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 110662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 122258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1571252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1624564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1637408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 2467197,
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
    "date_created": "2026-07-04T19:20:23Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:26:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Banks v. Dretke

```
<div>
<center><b><span class="citation" data-id="9434551"><a href="/opinion/131165/banks-v-dretke/" aria-description="Citation for case: Banks v. Dretke">540 U.S. 668</a></span> (2004)</b></center>
<center><h1>BANKS<br>
v.<br>
DRETKE, DIRECTOR, TEXAS DEPARTMENT OF CRIMINAL JUSTICE, CORRECTIONAL INSTITUTIONS DIVISION.</h1></center>
<center>No. 02-8286.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 8, 2003.</center>
<center>Decided February 24, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><span class="star-pagination">*669</span> <span class="star-pagination">*670</span> <span class="star-pagination">*671</span> <span class="star-pagination">*672</span> <span class="star-pagination">*673</span> <span class="star-pagination">*674</span> GINSBURG, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and STEVENS, O'CONNOR, KENNEDY, SOUTER, and BREYER, JJ., joined, and in which SCALIA and THOMAS, JJ., joined as to Part III. THOMAS, J., filed an opinion concurring in part and dissenting in part, in which SCALIA, J., joined, <i>post,</i> p. 706.</p>
<p><i>George H. Kendall</i> argued the cause for petitioner. With him on the briefs were <i>Elaine R. Jones, Janai S. Nelson, Miriam Gohara,</i> and <i>Clifton L. Holmes.</i></p>
<p><i>Gena Bunn,</i> Assistant Attorney General of Texas, argued the cause for respondent. With her on the brief were <i>Greg Abbott,</i> Attorney General, <i>Barry R. McBee,</i> First Assistant Attorney General, <i>Jay Kimbrough,</i> Deputy Attorney General, and <i>Edward L. Marshall</i> and <i>Katherine D. Hayes,</i> Assistant Attorneys General.<sup>[*]</sup></p>
<p>JUSTICE [[author]]GINSBURG[[/author]] delivered the opinion of the Court.</p>
<p>Petitioner Delma Banks, Jr., was convicted of capital murder and sentenced to death. Prior to trial, the State advised <span class="star-pagination">*675</span> Banks's attorney there would be no need to litigate discovery issues, representing: "[W]e will, without the necessity of motions[,] provide you with all discovery to which you are entitled." App. 361, n. 1; App. to Pet. for Cert. A4 (both sources' internal quotation marks omitted). Despite that undertaking, the State withheld evidence that would have allowed Banks to discredit two essential prosecution witnesses. The State did not disclose that one of those witnesses was a paid police informant, nor did it disclose a pretrial transcript revealing that the other witness' trial testimony had been intensively coached by prosecutors and law enforcement officers.</p>
<p>Furthermore, the prosecution raised no red flag when the informant testified, untruthfully, that he never gave the police any statement and, indeed, had not talked to any police officer about the case until a few days before the trial. Instead of correcting the informant's false statements, the prosecutor told the jury that the witness "ha[d] been open and honest with you in every way," App. 140, and that his testimony was of the "utmost significance," <i>id.,</i> at 146. Similarly, the prosecution allowed the other key witness to convey, untruthfully, that his testimony was entirely unrehearsed. Through direct appeal and state collateral review proceedings, the State continued to hold secret the key witnesses' links to the police and allowed their false statements to stand uncorrected.</p>
<p>Ultimately, through discovery and an evidentiary hearing authorized in a federal habeas corpus proceeding, the long-suppressed evidence came to light. The District Court granted Banks relief from the death penalty, but the Court of Appeals reversed. In the latter court's judgment, Banks had documented his claims of prosecutorial misconduct too late and in the wrong forum; therefore he did not qualify for federal-court relief. We reverse that judgment. When police or prosecutors conceal significant exculpatory or impeaching <span class="star-pagination">*676</span> material in the State's possession, it is ordinarily incumbent on the State to set the record straight.</p>
<p></p>
<h2>I</h2>
<p>On April 14, 1980, police found the corpse of 16-year-old Richard Whitehead in Pocket Park, east of Nash, Texas, a town in the vicinity of Texarkana. <i>Id.,</i> at 8, 141.<sup>[1]</sup> A preliminary autopsy revealed that Whitehead had been shot three times. <i>Id.,</i> at 10. Bowie County Deputy Sheriff Willie Huff, lead investigator of the death, learned from two witnesses that Whitehead had been in the company of petitioner, 21-year-old Delma Banks, Jr., late on the evening of April 11. <i>Id.,</i> at 11-15, 144; <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (Tex. Crim. App. 1982) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/904/">464 U. S. 904</a></span> (1983). On April 23, Huff received a call from a confidential informant reporting that "Banks was coming to Dallas to meet an individual and get a weapon." App. 15. That evening, Huff and other officers followed Banks to South Dallas, where Banks visited a residence. <i>Ibid.;</i> Brief for Petitioner 3. Police stopped Banks's vehicle en route from Dallas, found a handgun in the car, and arrested the car's occupants. App. 16. Returning to the Dallas residence Banks had visited, Huff encountered and interviewed Charles Cook and recovered a second gun, a weapon Cook said Banks had left with him several days earlier. <i>Ibid.</i> Tests later identified the second gun as the Whitehead murder weapon. <i>Id.,</i> at 17.</p>
<p>In a May 21, 1980, pretrial hearing, Banks's counsel sought information from Huff concerning the confidential informant who told Huff that Banks would be driving to Dallas. <i>Id.,</i> at 21. Huff was unresponsive. <i>Ibid.</i> Any information that might reveal the identity of the informant, the prosecution <span class="star-pagination">*677</span> urged, was privileged. <i>Id.,</i> at 23. The trial court sustained the State's objection. <i>Id.,</i> at 24. Several weeks later, in a July 7, 1980, letter, the prosecution advised Banks's counsel that "[the State] will, without necessity of motions provide you with all discovery to which you are entitled." <i>Id.,</i> at 361, n. 1; App. to Pet. for Cert. A4 (both sources' internal quotation marks omitted).</p>
<p>The guilt phase of Banks's trial spanned two days in September 1980. See Brief for Petitioner 2; App. to Pet. for Cert. C3. Witnesses testified to seeing Banks and Whitehead together on April 11 in Whitehead's green Mustang, and to hearing gunshots in Pocket Park at 4 a.m. on April 12. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d, at 131</a></span>. Charles Cook testified that Banks arrived in Dallas in a green Mustang at about 8:15 a.m. on April 12, and stayed with Cook until April 14. App. 42-43, 47-53. Cook gave the following account of Banks's visit. On the morning of his arrival, Banks had blood on his leg and told Cook "he [had] got into it on the highway with a white boy." <i>Id.,</i> at 44. That night, Banks confessed to having "kill[ed] the white boy for the hell of it and take[n] his car and come to Dallas." <i>Id.,</i> at 48. During their ensuing conversation, Cook first noticed that "[Banks] had a pistol." <i>Id.,</i> at 49. Two days later, Banks left Dallas by bus. <i>Id.,</i> at 52-53. The next day, Cook abandoned the Mustang in West Dallas and sold Banks's gun to a neighbor. <i>Id.,</i> at 54. Cook further testified that, shortly before the police arrived at his residence to question him, Banks had revisited him and requested the gun. <i>Id.,</i> at 57.</p>
<p>On cross-examination, Cook three times represented that he had not talked to anyone about his testimony. <i>Id.,</i> at 59. In fact, however, Cook had at least one "pretrial practice sessio[n]" at which Huff and prosecutors intensively coached Cook for his appearance on the stand at Banks's trial. <i>Id.,</i> at 325, ¶ 10, 381-390; Joint Lodging Material 1-36 (transcript of pretrial preparatory session). The prosecution allowed Cook's misstatements to stand uncorrected. In its guilt-phase <span class="star-pagination">*678</span> summation, the prosecution told the jury "Cook brought you absolute truth." App. 84.</p>
<p>In addition to Cook, Robert Farr was a key witness for the prosecution. Corroborating parts of Cook's account, Farr testified to traveling to Dallas with Banks to retrieve Banks's gun. <i>Id.,</i> at 34-35. On cross-examination, defense counsel asked Farr whether he had "ever taken any money from some police officers," or "give[n] any police officers a statement." <i>Id.,</i> at 37-38. Farr answered no to both questions; he asserted emphatically that police officers had not promised him anything and that he had "talked to no one about this [case]" until a few days before trial. <i>Ibid.</i> These answers were untrue, but the State did not correct them. Farr was the paid informant who told Deputy Sheriff Huff that Banks would travel to Dallas in search of a gun. <i>Id.,</i> at 329; App. to Pet. for Cert. A4, A9. In a 1999 affidavit, Farr explained:</p>
<blockquote>"I assumed that if I did not help [Huff] with his investigation of Delma that he would have me arrested for drug charges. That's why I agreed to help [Huff]. I was afraid that if I didn't help him, I would be arrested. . . .</blockquote>
<blockquote>"Willie Huff asked me to help him find Delma's gun. I told [Huff] that he would have to pay me money right away for my help on the case. I think altogether he gave me about $200.00 for helping him. He paid me some of the money before I set Delma up. He paid me the rest after Delma was arrested and charged with murder. . . .</blockquote>
<blockquote>"In order to help Willie Huff, I had to set Delma up. I told Delma that I wanted to rob a pharmacy to get drugs and that I needed his gun to do it. I did not really plan to commit a robbery but I told Delma this so that he would give me his gun. . . . I convinced Delma to drive to Dallas with me to get the gun." App. 442-443, ¶¶ 6-8.</blockquote>
<p><span class="star-pagination">*679</span> The defense presented no evidence. App. to Pet. for Cert. A6. Banks was convicted of murder committed in the course of a robbery, in violation of <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(2) (1974). See App. to Pet. for Cert. C3.<sup>[2]</sup></p>
<p>The penalty phase ran its course the next day. <i><span class="citation no-link">Ibid.</span></i> Governed by the Texas statutory capital murder scheme applicable in 1980, the jury decided Banks's sentence by answering three "special issues." App. 142-143.<sup>[3]</sup> "If the jury unanimously answer[ed] `yes' to each issue submitted, the trial court [would be obliged to] sentence the defendant to death." <i>Penry</i> v. <i>Lynaugh,</i> <span class="citation" data-id="9842108"><a href="/opinion/112325/penry-v-lynaugh/#310" aria-description="Citation for case: Penry v. Lynaugh">492 U. S. 302, 310</a></span> (1989) (construing Texas' sentencing scheme); Tex. Code Crim. Proc. Ann., Arts. 37.071(c)-(e) (Vernon Supp. 1980). The critical question at the penalty phase in Banks's case was: "Do you find from the evidence beyond a reasonable doubt that there is a probability that the defendant, Delma Banks, Jr., would commit criminal acts of violence that would constitute a continuing threat to society?" App. 143 (internal quotation marks omitted).</p>
<p>On this question, the State offered two witnesses, Vetrano Jefferson and Robert Farr. <i>Id.,</i> at 104-113. Jefferson testified that, in early April 1980, Banks had struck him across <span class="star-pagination">*680</span> the face with a gun and threatened to kill him. <i>Id.,</i> at 104-106. Farr's testimony focused once more on the trip to Dallas to fetch Banks's gun. The gun was needed, Farr asserted, because "[w]e [Farr and Banks] were going to pull some robberies." <i>Id.,</i> at 108. According to Farr, Banks "said he would take care of it" if "there was any trouble during these burglaries." <i>Id.,</i> at 109. When the prosecution asked: "How did [Banks] say he would take care of it?" Farr responded: "[Banks] didn't go into any specifics, but he said it would be taken care of." <i>Ibid.</i></p>
<p>On cross-examination, defense counsel twice asked whether Farr had told Deputy Sheriff Huff of the Dallas trip. <i>Ibid.</i> The State remained silent as Farr twice perjuriously testified: "No, I did not." <i>Ibid.</i> Banks's counsel also inquired whether Farr had previously attempted to obtain prescription drugs by fraud, and, "up tight over that," would "testify to anything anybody want[ed] to hear." <i>Id.,</i> at 110. Farr first responded: "Can you prove it?" <i>Ibid.</i> Instructed by the court to answer defense counsel's questions, Farr again said: "No, I did not. . . ." <i>Ibid.</i></p>
<p>Two defense witnesses impeached Farr, but were, in turn, impeached themselves. James Kelley testified to Farr's attempts to obtain drugs by fraud; the prosecution impeached Kelley by eliciting his close relationship to Banks's girl-friend. <i>Id.,</i> at 124-129. Later, Kelley admitted to being drunk while on the stand. App. to Pet. for Cert. A13. Former Arkansas police officer Gary Owen testified that Farr, as a police informant in Arkansas, had given false information; the prosecution impeached Owen by bringing out his pending application for employment by defense counsel's private investigator. App. 129-131.</p>
<p>Banks's parents and acquaintances testified that Banks was a "respectful, churchgoing young man." App. to Pet. for Cert. A7; App. 137-139. Thereafter, Banks took the stand. He affirmed that he had "never before been convicted <span class="star-pagination">*681</span> of a felony." <i>Id.,</i> at 134.<sup>[4]</sup> Banks admitted striking Vetrano Jefferson in April 1980, and traveling to Dallas to obtain a gun in late April 1980. <i>Id.,</i> at 134-136. He denied, however, any intent to participate in robberies, asserting that Farr alone had planned to commit them. <i>Id.,</i> at 136-137. The prosecution suggested on cross-examination that Banks had been willing "to supply [Farr] the means and possible death weapon in an armed robbery case." <i>Id.,</i> at 137. Banks conceded as much. <i>Ibid.</i></p>
<p>During summation, the prosecution intimated that Banks had not been wholly truthful in this regard, suggesting that "a man doesn't travel two hundred miles, or whatever the distance is from here [Texarkana] to Dallas, Texas, to supply a person with a weapon." <i>Id.,</i> at 143. The State homed in on Farr's testimony that Banks said he would "take care" of any trouble arising during the robbery:</p>
<blockquote>"[Farr] said, `Man, you know, what i[f] there's trouble?' And [Banks] says, `Don't worry about it. I'll take care of it.' I think that speaks for itself, and I think you know what that means. . . . I submit to you beyond a reasonable doubt that the State has again met its burden of proof, and that the answer to question number two [propensity to commit violent criminal acts] should also be yes." <i>Id.,</i> at 140, 144. See also <i>id.,</i> at 146-147.</blockquote>
<p>Urging Farr's credibility, the prosecution called the jury's attention to Farr's admission, at trial, that he used narcotics. <i>Id.,</i> at 36, 140. Just as Farr had been truthful about his drug use, the prosecution suggested, he was also "open and honest with [the jury] in every way" in his penalty-phase testimony. <i>Id.,</i> at 140. Farr's testimony, the prosecution emphasized, was "of the utmost significance" because it <span class="star-pagination">*682</span> showed "[Banks] is a danger to friends and strangers, alike." <i>Id.,</i> at 146. Banks's effort to impeach Farr was ineffective, the prosecution further urged, because defense witness "Kelley kn[ew] nothing about the murder," and defense witness Owen "wish[ed] to please his future employers." <i>Id.,</i> at 148.</p>
<p>The jury answered yes to the three special issues, and the judge sentenced Banks to death. The Texas Court of Criminal Appeals denied Banks's direct appeal. <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#135" aria-description="Citation for case: Banks v. State">643 S. W. 2d, at 135</a></span>. Banks's first two state postconviction motions raised issues not implicated here; both were denied. <i>Ex parte Banks,</i> No. 13568-01 (Tex. Crim. App. 1984); <i>Ex parte Banks,</i> <span class="citation" data-id="9660579"><a href="/opinion/1624564/ex-parte-banks/#540" aria-description="Citation for case: Ex Parte Banks">769 S. W. 2d 539, 540</a></span> (Tex. Crim. App. 1989).</p>
<p>Banks's third state postconviction motion, filed January 13, 1992, presented questions later advanced in federal court and reiterated in the petition now before us. App. 150. Banks alleged "upon information and belief" that "the prosecution knowingly failed to turn over exculpatory evidence as required by [<i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963)]";<sup>[5]</sup> the withheld evidence, Banks asserted, "would have revealed Robert Farr as a police informant and Mr. Banks' arrest as a set-up." App. 180, ¶ 114 (internal quotation marks omitted). In support of this third state-court postconviction plea, Banks attached an unsigned affidavit from his girlfriend, Farr's sister-in-law Demetra Jefferson, which stated that Farr "was well-connected to law enforcement people," and consequently managed to stay out of "trouble" for illegally obtaining prescription drugs. <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#195" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 195, ¶ 7</a></span>. Banks alleged as well that during the guilt phase of his trial, the State deliberately withheld information "critical to the jury's assessment of Cook's credibility," including the "generous <span class="star-pagination">*683</span> `deal' [Cook had] cut with the prosecutors." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#152" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 152, ¶ 2, 180, ¶ 114</a></span>.<sup>[6]</sup></p>
<p>The State's reply to Banks's pleading, filed October 6, 1992, "denie[d] each and every allegation of fact made by [Banks], except those supported by official court records and those specifically admitted." <i>Id.,</i> at 234; Tr. of Oral Arg. 32. "[N]othing was kept secret from the defense," the State represented. App. 234. While the reply specifically asserted that the State had made "no deal with Cook," <i>ibid.,</i> the State said nothing specific about Farr. Affidavits from Deputy Sheriff Huff and prosecutors accompanied the reply. <i>Id.,</i> at 241-243. The affiants denied any "deal, secret or otherwise, with Charles Cook," but they, too, like the State's pleading they supported, remained silent about Farr. <i>Ibid.</i></p>
<p>In February and July 1993 orders, the state postconviction court rejected Banks's claims. App. to Pet. for Cert. E1-E9, G1-G7. The court found that "there was no agreement between the State and the witness Charles Cook," but made no findings concerning Farr. <i>Id.,</i> at G2. In a January 10, 1996, one-page <i>per curiam</i> order, the Texas Court of Criminal Appeals upheld the lower court's disposition of Banks's motion. <i>Id.,</i> at D1.</p>
<p>On March 7, 1996, Banks filed the instant petition for a writ of habeas corpus in the United States District Court for the Eastern District of Texas. App. 248. He alleged multiple violations of his federal constitutional rights. App. to Pet. for Cert. C5-C7. Relevant here, Banks reasserted that the State had withheld material exculpatory evidence <span class="star-pagination">*684</span> "reveal[ing] Robert Farr as a police informant and Mr. Banks' arrest as a set-up." App. 260, ¶ 152 (internal quotation marks omitted). Banks also asserted that the State had concealed "Cook's enormous incentive to testify in a manner favorable to the [prosecution]." <i>Id.,</i> at 260, ¶ 153; App. to Pet. for Cert. C6-C7.<sup>[7]</sup> In June 1998, Banks moved for discovery and an evidentiary hearing to gain information from the State on the roles played and trial testimony provided by Farr and Cook. App. 262-266, 282-283, 286. The superintending Magistrate Judge allowed limited discovery regarding Cook, but found insufficient justification for inquiries concerning Farr. <i>Id.,</i> at 294-295.</p>
<p>Banks renewed his discovery and evidentiary hearing requests in February 1999. <i>Id.,</i> at 2, 300-331. This time, he proffered affidavits from both Farr and Cook to back up his claims that, as to each of these two key witnesses, the prosecution had wrongly withheld crucial exculpatory and impeaching evidence. <i>Id.,</i> at 322-331. Farr's affidavit affirmed that Farr had "set Delma up" by proposing the drive to Dallas and informing Deputy Sheriff Huff of the trip. <i>Id.,</i> at 329, ¶ 8, 442-443, ¶ 8; <i>supra,</i> at 678. Accounting for his unavailability earlier, Farr stated that less than a year after the Banks trial, he had left Texarkana, first for Oklahoma, then for California, because his police-informant work endangered his life. App. 330-331, 444; Pet. for Cert. 27, n. 12. Cook recalled that in preparation for his Banks trial testimony, he had participated in "three or four . . . practice sessions" at which prosecutors told him to testify "as they wanted [him] to, and that [he] would spend the rest of [his] life in prison if [he] did not." App. 325, ¶¶ 10-11.</p>
<p>On March 4, 1999, the Magistrate Judge issued an order establishing issues for an evidentiary hearing, <i>id.,</i> at 340, 346, at which she would consider Banks's claims that the State had withheld "crucial exculpatory and impeaching evidence" <span class="star-pagination">*685</span> concerning "two of the [S]tate's essential witnesses, Charles Cook and Robert Farr." <i>Id.,</i> at 340, 345 (internal quotation marks omitted). In anticipation of the hearing, the Magistrate Judge ordered disclosure of the Bowie County District Attorney's files. Brief for Petitioner 37-38; Tr. of June 7-8, 1999, Federal Evidentiary Hearing (ED Tex.), p. 30 (hereinafter Federal Evidentiary Hearing).</p>
<p>One item lodged in the District Attorney's files, turned over to Banks pursuant to the Magistrate Judge's disclosure order, was a 74-page transcript of a Cook interrogation. App. to Pet. for Cert. A10. The interrogation, conducted by Bowie County law enforcement officials and prosecutors, occurred in September 1980, shortly before the Banks trial. <i>Ibid.</i> The transcript revealed that the State's representatives had closely rehearsed Cook's testimony. In particular, the officials told Cook how to reconcile his testimony with affidavits to which he had earlier subscribed recounting Banks's visits to Dallas. See, <i>e. g.,</i> Joint Lodging Material 24 ("Your [April 1980] statement is obviously screwed up."); <i>id.,</i> at 26 ("[T]he way this statement should read is that. . . ."); <i>id.,</i> at 32 ("[L]et me tell you how this is going to work."); <i>id.,</i> at 36 ("That's not in your [earlier] statement."). Although the transcript did not bear on Banks's claim that the prosecution had a deal with Cook, it provided compelling evidence that Cook's testimony had been tutored by Banks's prosecutors. Without objection at the hearing, the Magistrate Judge admitted the September 1980 transcript into evidence. Brief for Petitioner 39; Federal Evidentiary Hearing 75-76.</p>
<p>Testifying at the evidentiary hearing, Deputy Sheriff Huff acknowledged, for the first time, that Farr was an informant and that he had been paid $200 for his involvement in the case. App. to Pet. for Cert. C43. As to Cook, a Banks trial prosecutor testified, in line with the State's consistent position, that no deal had been offered to gain Cook's trial testimony. <i>Id.,</i> at C45; Federal Evidentiary Hearing 52-53. <span class="star-pagination">*686</span> Defense counsel questioned the prosecutor about the September 1980 transcript, calling attention to discrepancies between the transcript and Cook's statements at trial. <i>Id.,</i> at 65-68. In a posthearing brief and again in proposed findings of fact and conclusions of law, Banks emphasized the suppression of the September 1980 transcript, noting the prosecution's obligation to disclose material, exculpatory evidence, and the assurance in this case that Banks would receive "all [the] discovery to which [Banks was] entitled." App. 360-361, and n. 1, 378-379 (internal quotation marks omitted); <i>supra,</i> at 677.</p>
<p>In a May 11, 2000, report and recommendation, the Magistrate Judge recommended a writ of habeas corpus with respect to Banks's death sentence, but not his conviction. App. to Pet. for Cert. C54. "[T]he State's failure to disclose Farr's informant status, coupled with trial counsel's dismal performance during the punishment phase," the Magistrate Judge concluded, "undermined the reliability of the jury's verdict regarding punishment." <i>Id.,</i> at C44. Finding no convincing evidence of a deal between the State and Cook, however, she recommended that the guilt-phase verdict remain undisturbed. <i>Id.,</i> at C46.</p>
<p>Banks moved to alter or amend the Magistrate Judge's report on the ground that it left unresolved a fully aired question, <i>i. e.,</i> whether Banks's rights were violated by the State's failure to disclose to the defense the prosecution's eve-of-trial interrogation of Cook. App. 398. That interrogation, Banks observed, could not be reconciled with Cook's insistence at trial that he had talked to no one about his testimony. <i>Id.,</i> at 400, n. 17; see <i>supra,</i> at 677.</p>
<p>The District Court adopted the Magistrate Judge's report and denied Banks's motion to amend the report. App. to Pet. for Cert. B6; App. 421-424. Concerning the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim, the District Court recognized that Banks had filed his federal petition in 1996, three years before he became aware of the September 1980 <span class="star-pagination">*687</span> transcript. App. 422-423. When the transcript surfaced in response to the Magistrate Judge's 1999 disclosure order, Banks raised that newly discovered, long withheld document in his proposed findings of fact and conclusions of law and, again, in his objections to the Magistrate Judge's report. <i>Id.,</i> at 423. The District Court concluded, however, that Banks had not properly pleaded a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim predicated on the withheld Cook rehearsal transcript. App. 422. When that <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim came to light, the District Court reasoned, Banks should have moved to amend or supplement his 1996 federal habeas petition specifically to include the 1999 discovery as a basis for relief. App. 423. Banks urged that a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim based on the September 1980 transcript had been aired by implied consent; under Federal Rule of Civil Procedure 15(b), he contended, the claim should have been treated as if raised in the pleadings. App. 433.<sup>[8]</sup> Banks sought, and the District Court denied, a certificate of appealability on this question. <i>Id.,</i> at 433, 436.</p>
<p>In an August 20, 2003, unpublished <i>per curiam</i> opinion, the Court of Appeals for the Fifth Circuit reversed the judgment of the District Court to the extent that it granted relief on the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and denied a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. App. to Pet. for Cert. A2, judgt. order reported at <span class="citation no-link">48 Fed. Appx. 104</span> (2002).<sup>[9]</sup> The <span class="star-pagination">*688</span> Court of Appeals observed that in his 1992 state-court postconviction application, Banks had not endeavored to develop the facts underpinning the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. App to Pet. for Cert. A19-A20. For that reason, the court held, the evidentiary proceeding ordered by the Magistrate Judge was unwarranted. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Ibid.</a></span></i> The Court of Appeals expressed no doubt that the prosecution had suppressed, prior to the federal habeas proceeding, Farr's informant status and his part in the fateful trip to Dallas. But Banks was not appropriately diligent in pursuing his state-court application, the Court of Appeals maintained. In the Fifth Circuit's view, Banks should have at that time attempted to locate Farr and question him; similarly, he should have asked to interview Deputy Sheriff Huff and other officers involved in investigating the crime. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A19, A22. If such efforts had proved unavailing, the Court of Appeals suggested, Banks might have applied to the state court for assistance. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A19. Banks's lack of diligence in pursuing his 1992 state-court plea, the Court of Appeals concluded, rendered the evidence uncovered in the federal habeas proceeding procedurally barred. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A22-A23.</p>
<p>In any event, the Fifth Circuit further concluded, Farr's status as an informant was not "materia[l]" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes. App. to Pet. for Cert. A32-A33. Banks had impeached Farr at trial by bringing out that he had been a police informant in Arkansas, and an unreliable one at that. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A28, A32-A33; <i>supra,</i> at 680. Moreover, the Court of Appeals said, other witnesses had corroborated much of Farr's testimony against Banks. App. to Pet. for Cert. A32. Notably, Banks himself had acknowledged his willingness to get a gun for Farr's use in robberies. <i>Ibid.</i> In addition, the Fifth Circuit observed, the Magistrate Judge had relied on the cumulative effect of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> error and the ineffectiveness of Banks's counsel at the penalty phase. App. to Pet. for Cert. A44. Banks himself, however, had not urged that position; he had argued <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and ineffective assistance of <span class="star-pagination">*689</span> counsel discretely, not cumulatively. App. to Pet. for Cert. A46-A47. Finally, in accord with the District Court, the Court of Appeals apparently regarded Rule 15(b) as inapplicable in habeas proceedings. App. to Pet. for Cert. A51-A52. The Fifth Circuit accordingly denied a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim. App. to Pet. for Cert. A52, A78.</p>
<p>With an execution date set for March 12, 2003, Banks applied to this Court for a writ of certiorari, presenting four issues: the tenability of his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim; a penalty-phase ineffective-assistance-of-counsel claim; the question whether, as to the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim, a certificate of appealability was wrongly denied; and a claim of improper exclusion of minority jurors in violation of <i>Swain</i> v. <i>Alabama,</i> <span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">380 U. S. 202</a></span> (1965). Pet. for Cert. 23-24. We stayed Banks's execution on March 12, 2003, <span class="citation multiple-matches"><a href="/c/U.%20S./538/917/">538 U. S. 917</a></span>, and, on April 21, 2003, granted his petition on all questions other than his <i><span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">Swain</a></span></i> claim. <span class="citation multiple-matches"><a href="/c/U.%20S./538/977/">538 U. S. 977</a></span>. We now reverse the Court of Appeals' judgment dismissing Banks's Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and that Court's denial of a certificate of appealability on his Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.<sup>[10]</sup></p>
<p></p>
<h2>II</h2>
<p>We note, initially, that Banks's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims arose under the regime in place prior to the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>. Turning to the tenability of those claims, we consider first Banks's Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim as it trains on his death sentence, see App. to Pet. for Cert. B6 (District Court granted habeas solely with respect to the capital sentence), and next, Banks's Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<p></p>
<h2>
<span class="star-pagination">*690</span> A</h2>
<p>To pursue habeas corpus relief in federal court, Banks first had to exhaust "the remedies available in the courts of the State." <span class="citation no-link">28 U. S. C. § 2254</span>(b) (1994 ed.); see <i>Rose</i> v. <i>Lundy,</i> <span class="citation" data-id="9428690"><a href="/opinion/110662/rose-v-lundy/#520" aria-description="Citation for case: Rose v. Lundy">455 U. S. 509, 520</a></span> (1982). Banks alleged in his January 1992 state-court application for a writ of habeas corpus that the prosecution knowingly failed to turn over exculpatory evidence involving Farr in violation of Banks's due process rights. App. 180. Banks thus satisfied the exhaustion requirement as to the legal ground for his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.<sup>[11]</sup></p>
<p>In state postconviction court, however, Banks failed to produce evidence establishing that Farr had served as a police informant in this case. As support for his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, Banks appended to his state-court application only Demetra Jefferson's hardly probative statement that Farr "was well-connected to law enforcement people." App. 195, ¶ 7; see <i>supra,</i> at 682. In the federal habeas forum, therefore, it was incumbent on Banks to show that he was not barred, by reason of the anterior state proceedings, from producing evidence to substantiate his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. Banks "[would be] entitled to an evidentiary hearing [in federal court] if he [could] show cause for his failure to develop the <span class="star-pagination">*691</span> facts in state-court proceedings and actual prejudice resulting from that failure." <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#11" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1, 11</a></span> (1992).</p>
<p><i>Brady,</i> we reiterate, held that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. We set out in <i>Strickler</i> v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263, 281-282</a></span> (1999), the three components or essential elements of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> prosecutorial misconduct claim: "The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 281-282</a></span>. "[C]ause and prejudice" in this case "parallel two of the three components of the alleged <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation itself." <i>Id.,</i> at 282. Corresponding to the second <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (evidence suppressed by the State), a petitioner shows "cause" when the reason for his failure to develop facts in state-court proceedings was the State's suppression of the relevant evidence; coincident with the third <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (prejudice), prejudice within the compass of the "cause and prejudice" requirement exists when the suppressed evidence is "material" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#282" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 282</a></span>. As to the first <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (evidence favorable to the accused), beyond genuine debate, the suppressed evidence relevant here, Farr's paid informant status, qualifies as evidence advantageous to Banks. See App. to Pet. for Cert. A26 (Court of Appeals' recognition that "Farr's being a paid informant would certainly be favorable to Banks in attacking Farr's testimony"). Thus, if Banks succeeds in demonstrating "cause and prejudice," he will at the same time succeed in establishing the elements of his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> death penalty due process claim.</p>
<p></p>
<h2>
<span class="star-pagination">*692</span> B</h2>
<p>Our determination as to "cause" for Banks's failure to develop the facts in state-court proceedings is informed by <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>.</i><sup>[12]</sup> In that case, Virginia prosecutors told the petitioner, prior to trial, that "the prosecutor's files were open to the petitioner's counsel," thus "there was no need for a formal <i>[Brady]</i> motion." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#276" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 276</a></span>, n. 14 (quoting App. in <i>Strickler</i> v. <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Greene</a></span>,</i> O. T. 1998, No. 98-5864, pp. 212-213 (brackets in original)). The prosecution file given to the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner, however, did not include several documents prepared by an "importan[t]" prosecution witness, recounting the witness' initial difficulty recalling the events to which she testified at the petitioner's trial. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#273" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 273-275, 290</a></span>. Those absent-from-the-file documents could have been used to impeach the witness. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#273" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 273</a></span>. In state-court postconviction proceedings, the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner had unsuccessfully urged ineffective assistance of trial counsel based on counsel's failure to move, pretrial, for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. Answering that plea, the State asserted that a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> motion would have been superfluous, for the prosecution had maintained an open file policy pursuant to which it had disclosed all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#276" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 276, n. 14, 278</a></span>.</p>
<p>This Court determined that in the federal habeas proceedings, the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner had shown cause for his failure to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state court. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>. Three factors accounted for that determination:</p>
<blockquote>"(a) the prosecution withheld exculpatory evidence; (b) petitioner reasonably relied on the prosecution's open file policy as fulfilling the prosecution's duty to disclose such evidence; and (c) the [State] confirmed petitioner's reliance on the open file policy by asserting during state <span class="star-pagination">*693</span> habeas proceedings that petitioner had already received everything known to the government." <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Ibid.</a></span></i> (internal quotation marks omitted).<sup>[13]</sup></blockquote>
<p>This case is congruent with <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> in all three respects. First, the State knew of, but kept back, Farr's arrangement with Deputy Sheriff Huff. App. to Pet. for Cert. C43; Tr. of Oral Arg. 33; cf. <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 437</a></span> (1995) (prosecutors are responsible for "any favorable evidence known to the others acting on the government's behalf in the case, including the police"). Second, the State asserted, on the eve of trial, that it would disclose all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. App. 361, n. 1; see <i>supra,</i> at 677. As <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> instructs, Banks cannot be faulted for relying on that representation. See <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#283" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 283-284</a></span> (an "open file policy" is one factor that "explain[s] why trial counsel did not advance [a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>] claim").</p>
<p>Third, in his January 1992 state habeas application, Banks asserted that Farr was a police informant and Banks's arrest, "a set-up." App. 180, ¶ 114 (internal quotation marks omitted). In its answer, the State denied Banks's assertion. <i>Id.,</i> at 234; see <i>supra,</i> at 683. The State thereby "confirmed" Banks's reliance on the prosecution's representation that it had fully disclosed all relevant information its file contained. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>; see <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 284</a></span> (state habeas counsel, as well as trial counsel, could reasonably rely on the State's representations). In short, because the State persisted in hiding Farr's informant status and misleadingly represented that it had complied in full with its <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> disclosure obligations, Banks had cause for failing to investigate, in state postconviction proceedings, Farr's connections to Deputy Sheriff Huff.</p>
<p><span class="star-pagination">*694</span> On the question of "cause," moreover, Banks's case is stronger than was the petitioner's in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> in a notable respect. As a prosecution witness in the guilt and penalty phases of Banks's trial, Farr repeatedly misrepresented his dealings with police; each time Farr responded untruthfully, the prosecution allowed his testimony to stand uncorrected. See <i>supra,</i> at 678-680. Farr denied taking money from or being promised anything by police officers, App. 37; he twice denied speaking with police officers, <i>id.,</i> at 38, and twice denied informing Deputy Sheriff Huff about Banks's trip to Dallas, <i>id.,</i> at 109. It has long been established that the prosecution's "deliberate deception of a court and jurors by the presentation of known false evidence is incompatible with rudimentary demands of justice." <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#153" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 153</a></span> (1972) (quoting <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935) <i>(per curiam)</i> (internal quotation marks omitted)). If it was reasonable for Banks to rely on the prosecution's full disclosure representation, it was also appropriate for Banks to assume that his prosecutors would not stoop to improper litigation conduct to advance prospects for gaining a conviction. See <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935); <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 284</a></span>.<sup>[14]</sup></p>
<p>The State presents three main arguments for distinguishing <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> on the issue of "cause," two of them endorsed <span class="star-pagination">*695</span> by the Court of Appeals. Brief for Respondent 15-20; App. to Pet. for Cert. A19, A22-A23; see <i>supra,</i> at 687-688. We conclude that none of these arguments accounts adequately for the State's concealment and misrepresentation regarding Farr's link to Deputy Sheriff Huff. The State first suggests that Banks's failure, during state postconviction proceedings, to "attempt to locate Farr and ascertain his true status," or to "interview the investigating officers, such as Deputy Huff, to ascertain Farr's status," undermines a finding of cause; the Fifth Circuit agreed. App. to Pet. for Cert. A22; Brief for Respondent 18-20. In the State's view, "[t]he question [of cause] revolves around Banks's conduct," particularly his lack of appropriate diligence in pursuing the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim before resorting to federal court. Brief for Respondent 14.<sup>[15]</sup></p>
<p>We rejected a similar argument in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>.</i> There, the State contended that examination of a witness' trial testimony, alongside a letter the witness published in a local newspaper, should have alerted the petitioner to the existence of undisclosed interviews of the witness by the police. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 284</a></span>, and n. 26. We found this contention insubstantial. In light of the State's open file policy, we noted, "it is especially unlikely that counsel would have suspected that additional impeaching evidence was being withheld." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#285" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 285</a></span>. Our decisions lend no support to the notion that defendants must scavenge for hints of undisclosed <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material when the prosecution represents that all such material has been disclosed. As we observed in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> defense counsel has no "procedural obligation to assert constitutional error on the basis of mere suspicion that some prosecutorial <span class="star-pagination">*696</span> misstep may have occurred." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#286" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 286-287</a></span>. The "cause" inquiry, we have also observed, turns on events or circumstances "external to the defense." <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#222" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214, 222</a></span> (1988) (quoting <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S. 478, 488</a></span> (1986)).</p>
<p>The State here nevertheless urges, in effect, that "the prosecution can lie and conceal and the prisoner still has the burden to . . . discover the evidence," Tr. of Oral Arg. 35, so long as the "potential existence" of a prosecutorial misconduct claim might have been detected, <i>id.,</i> at 36. A rule thus declaring "prosecutor may hide, defendant must seek," is not tenable in a system constitutionally bound to accord defendants due process. "Ordinarily, we presume that public officials have properly discharged their official duties." <i>Bracy</i> v. <i>Gramley,</i> <span class="citation" data-id="118123"><a href="/opinion/118123/bracy-v-gramley/#909" aria-description="Citation for case: Bracy v. Gramley">520 U. S. 899, 909</a></span> (1997) (quoting <i>United States</i> v. <i>Chemical Foundation, Inc.,</i> <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#14" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 14-15</a></span> (1926) (internal quotation marks omitted)). We have several times underscored the "special role played by the American prosecutor in the search for truth in criminal trials." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 281</a></span>; accord, <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#439" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 439-440</a></span>; <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#675" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 675, n. 6</a></span> (1985); <i>Berger,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S., at 88</a></span>. See also <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#484" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 484</a></span> (1928) (Brandeis, J., dissenting). Courts, litigants, and juries properly anticipate that "obligations [to refrain from improper methods to secure a conviction] . . . plainly rest[ing] upon the prosecuting attorney, will be faithfully observed." <i>Berger,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S., at 88</a></span>. Prosecutors' dishonest conduct or unwarranted concealment should attract no judicial approbation. See <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#440" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 440</a></span> ("The prudence of the careful prosecutor should not . . . be discouraged.").</p>
<p>The State's second argument is a variant of the first. Specifically, the State argues, and the Court of Appeals accepted, that Banks cannot show cause because in the 1992 state-court postconviction proceedings, he failed to move for investigative assistance enabling him to inquire into Farr's <span class="star-pagination">*697</span> police connections, connections he then alleged, but failed to prove. Brief for Respondent 15-16; App. to Pet. for Cert. A19; see 1977 Tex. Gen. Laws ch. 789, § 2(d) (as amended) (instructing postconviction court to "designat[e] the issues of fact to be resolved," and giving the court discretion to "order affidavits, depositions, interrogatories, and hearings"). Armed in 1992 only with Demetra Jefferson's declaration that Farr was "well-connected to law enforcement people," App. 195, ¶ 7; see <i>supra,</i> at 682, Banks had little to proffer in support of a request for assistance from the state postconviction court. We assign no overriding significance to Banks's failure to invoke state-court assistance to which he had no clear entitlement. Cf. <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#286" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 286</a></span> ("Proper respect for state procedures counsels against a requirement that all possible claims be raised in state collateral proceedings, even when no known facts support them.").<sup>[16]</sup></p>
<p>Finally, relying on <i>Roviaro</i> v. <i>United States,</i> <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957), the State asserts that "disclosure [of an informant's identity] is not automatic," and, "[c]onsequently, it was Banks's duty to move for disclosure of otherwise privileged material." Brief for Respondent 17-18, n. 15. We need not linger over this argument. The issue of evidentiary law in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span></i> was whether (or when) the Government is obliged to reveal the identity of an undercover informer the Government does <i>not</i> call as a trial witness. <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#55" aria-description="Citation for case: Roviaro v. United States">353 U. S., at 55-56</a></span>. The Court there stated that no privilege obtains "[w]here the disclosure of an informer's identity, or of the contents of his communication, is relevant and helpful to the defense of an accused." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#60" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 60-61</a></span>. Accordingly, even though the informer in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span></i> did not testify, we held that disclosure <span class="star-pagination">*698</span> of his identity was necessary because he could have "amplif[ied] or contradict[ed] the testimony of government witnesses." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#64" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 64</a></span>.</p>
<p>Here, the State elected to call Farr as a witness. Indeed, he was a key witness at both guilt and punishment phases of Banks's capital trial. Farr's status as a paid informant was unquestionably "relevant"; similarly beyond doubt, disclosure of Farr's status would have been "helpful to [Banks's] defense." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#60" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 60-61</a></span>. Nothing in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span>,</i> or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion.</p>
<p>In summary, Banks's prosecutors represented at trial and in state postconviction proceedings that the State had held nothing back. Moreover, in state postconviction court, the State's pleading denied that Farr was an informant. App. 234; <i>supra,</i> at 683. It was not incumbent on Banks to prove these representations false; rather, Banks was entitled to treat the prosecutor's submissions as truthful. Accordingly, Banks has shown cause for failing to present evidence in state court capable of substantiating his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<p></p>
<h2>C</h2>
<p>Unless suppressed evidence is "material for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes, [its] suppression [does] not give rise to sufficient prejudice to overcome [a] procedural default." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#282" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 282</a></span> (internal quotation marks omitted). Our touchstone on materiality is <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419</a></span> (1995). <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span></i> instructed that the materiality standard for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims is met when "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 435</a></span>. See also <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>id.,</i> at 434-435</a></span> ("A defendant need not demonstrate that after discounting the inculpatory evidence in light of the undisclosed evidence, there would not have been enough left <span class="star-pagination">*699</span> to convict."); accord, <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#290" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 290</a></span>. In short, Banks must show a "reasonable probability of a different result." <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span> (internal quotation marks omitted) (citing <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U. S., at 678</a></span>).</p>
<p>As the State acknowledged at oral argument, Farr was "paid for a critical role in the scenario that led to the indictment." Tr. of Oral Arg. 34. Farr's declaration, presented to the federal habeas court, asserts that Farr, not Banks, initiated the proposal to obtain a gun to facilitate the commission of robberies. See App. 442-443, ¶¶ 7-8; <i>supra,</i> at 678. Had Farr not instigated, upon Deputy Sheriff Huff's request, the Dallas excursion to fetch Banks's gun, the prosecution would have had slim, if any, evidence that Banks planned to "continue" committing violent acts. App. 147.<sup>[17]</sup> Farr's admission of his instigating role, moreover, would have dampened the prosecution's zeal in urging the jury to bear in mind Banks's "planning and acquisition of a gun to commit robbery," or Banks's "planned violence." <i>Ibid.;</i> see Tr. of Oral Arg. 50.<sup>[18]</sup></p>
<p><span class="star-pagination">*700</span> Because Banks had no criminal record, Farr's testimony about Banks's propensity to commit violent acts was crucial to the prosecution. Without that testimony, the State could not have underscored, as it did three times in the penalty phase, that Banks would use the gun fetched in Dallas to "take care" of trouble arising during the robberies. App. 140, 144, 146-147; see <i>supra,</i> at 681. The stress placed by the prosecution on this part of Farr's testimony, uncorroborated by any other witness, belies the State's suggestion that "Farr's testimony was adequately corroborated." Brief for Respondent 22-25. The prosecution's penalty-phase summation, moreover, left no doubt about the importance the State attached to Farr's testimony. What Farr told the jury, the prosecution urged, was "of the utmost significance" to show "[Banks] is a danger to friends and strangers, alike." App. 146.</p>
<p>In <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>, although the Court found "cause" for the petitioner's procedural default of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, it found the requisite "prejudice" absent, <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#292" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 292-296</a></span>. Regarding "prejudice," the contrast between <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> and Banks's case is marked. The witness whose impeachment was at issue in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> gave testimony that was in the main cumulative, <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#292" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 292</a></span>, and hardly significant <span class="star-pagination">*701</span> to one of the "two predicates for capital murder: [armed] robbery," <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#294" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 294</a></span>. Other evidence in the record, the Court found, provided strong support for the conviction even if the witness' testimony had been excluded entirely: Unlike the Banks prosecution, in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> "considerable forensic and other physical evidence link[ed] [the defendant] to the crime" and supported the capital murder conviction. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#293" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 293</a></span>. Most tellingly, the witness' testimony in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> "did not relate to [the petitioner's] eligibility for the death sentence"; it "was not relied upon by the prosecution at all during its closing argument at the penalty phase." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#295" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 295</a></span>. In contrast, Farr's testimony was the centerpiece of Banks's prosecution's penalty-phase case.</p>
<p>Farr's trial testimony, critical at the penalty phase, was cast in large doubt by the declaration Banks ultimately obtained from Farr and introduced in the federal habeas proceeding. See <i>supra,</i> at 678, 684. In the guilt phase of Banks's trial, Farr had acknowledged his narcotics use. App. 36. In the penalty phase, Banks's counsel asked Farr if, "drawn up tight over" previous drug-related activity, he would "testify to anything anybody want[ed] to hear"; Farr denied this. <i>Id.,</i> at 110; <i>supra,</i> at 680. Farr's declaration supporting Banks's federal habeas petition, however, vividly contradicts that denial: "I assumed that if I did not help [Huff] . . . he would have me arrested for drug charges." App. 442, ¶ 6. Had jurors known of Farr's continuing interest in obtaining Deputy Sheriff Huff's favor, in addition to his receipt of funds to "set [Banks] up," <i>id.,</i> at 442, ¶ 7, they might well have distrusted Farr's testimony, and, insofar as it was uncorroborated, disregarded it.</p>
<p>The jury, moreover, did not benefit from customary, truth-promoting precautions that generally accompany the testimony of informants. This Court has long recognized the "serious questions of credibility" informers pose. <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#757" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 757</a></span> (1952). See also Trott, Words of Warning for Prosecutors Using Criminals as Witnesses, <span class="star-pagination">*702</span> 47 Hastings L. J. 1381, 1385 (1996) ("Jurors suspect [informants'] motives from the moment they hear about them in a case, and they frequently disregard their testimony altogether as highly untrustworthy and unreliable. . . ."). We have therefore allowed defendants "broad latitude to probe [informants'] credibility by cross-examination" and have counseled submission of the credibility issue to the jury "with careful instructions." <i>On Lee,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#757" aria-description="Citation for case: On Lee v. United States">343 U. S., at 757</a></span>; accord, <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#311" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 311-312</a></span> (1966). See also 1A K. O'Malley, J. Grenig, &amp; W. Lee, Federal Jury Practice and Instructions, Criminal § 15.02 (5th ed. 2000) (jury instructions from the First, Fifth, Sixth, Seventh, Eighth, Ninth, and Eleventh Circuits on special caution appropriate in assessing informant testimony).</p>
<p>The State argues that "Farr was heavily impeached [at trial]," rendering his informant status "merely cumulative." Tr. of Oral Arg. 49; see Brief for Respondent 26-28; <i>post,</i> at 709, n. 3. The record suggests otherwise. Neither witness called to impeach Farr gave evidence directly relevant to Farr's part in Banks's trial. App. 124-133; <i>id.,</i> at 129 (prosecutor noted that Kelley lacked "personal knowledge with regard to this case on trial"). The impeaching witnesses, Kelley and Owen, moreover, were themselves impeached, as the prosecution stressed on summation. See <i>id.,</i> at 141, 148; <i>supra,</i> at 680, 682. Further, the prosecution turned to its advantage remaining impeachment evidence concerning Farr's drug use. On summation, the prosecution suggested that Farr's admission "that he used dope, that he shot," demonstrated that Farr had been "open and honest with [the jury] in every way." App. 140; <i>supra,</i> at 681.</p>
<p>At least as to the penalty phase, in sum, one can hardly be confident that Banks received a fair trial, given the jury's ignorance of Farr's true role in the investigation and trial of the case. See <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span> ("The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in <span class="star-pagination">*703</span> its absence he received a fair trial, understood as a trial resulting in a verdict worthy of confidence."). On the record before us, one could not plausibly deny the existence of the requisite "reasonable probability of a different result" had the suppressed information been disclosed to the defense. <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Ibid.</a></span></i> (internal quotation marks omitted) (citing <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U. S., at 678</a></span>); <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#290" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 290</a></span>. Accordingly, as to the suppression of Farr's informant status and its bearing on "the reliability of the jury's verdict regarding punishment," App. to Pet. for Cert. C44; <i>supra,</i> at 686, all three elements of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim are satisfied.</p>
<p></p>
<h2>III</h2>
<p>Both the District Court and the Court of Appeals denied Banks a certificate of appealability with regard to his Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, which rested on the prosecution's suppression of the September 1980 Cook interrogation transcript. App. 422-423; App. to Pet. for Cert. A52, A78; <i>supra,</i> at 687, 689. See also Joint Lodging Material 1-36. The District Court and the Fifth Circuit concluded that Banks had not properly pleaded this claim because he had not sought leave to amend his petition, but had stated the claim only in other submissions, <i>i. e.,</i> in his proposed findings of fact and conclusions of law, and, again, in his objections to the Magistrate Judge's report. App. 422-423, 432-433; App. to Pet. for Cert. A51-A52; <i>supra,</i> at 687, 689. Banks contended, unsuccessfully, that evidence substantiating the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim had been aired before the Magistrate Judge; therefore the claim should have been treated as if raised in the pleadings, as Federal Rule of Civil Procedure 15(b) instructs. See App. to Pet. for Cert. A51-A52; <i>supra,</i> at 687, n. 8 (setting out text of Rule 15(b)). The Fifth Circuit stated its position on this point somewhat obliquely, but appears to have viewed Rule 15(b) as inapplicable in habeas proceedings; the State now concedes, however, that the question whether Rule 15(b) extends to habeas proceedings is one "jurists of reason would <span class="star-pagination">*704</span> find . . . debatable." Compare App. to Pet. for Cert. A52 (quoting <i>Slack</i> v. <i>McDaniel,</i> <span class="citation" data-id="9433937"><a href="/opinion/118359/slack-v-mcdaniel/#484" aria-description="Citation for case: Slack v. McDaniel">529 U. S. 473, 484</a></span> (2000)), with Tr. of Oral Arg. 45-46. We conclude that a certificate of appealability should have issued.</p>
<p>We have twice before referenced Rule 15(b)'s application in federal habeas proceedings. In <i>Harris</i> v. <i>Nelson,</i> <span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/#294" aria-description="Citation for case: Harris v. Nelson">394 U. S. 286, 294, n. 5</a></span> (1969), we noted that Rule 15(b)'s use in habeas proceedings is "noncontroversial." In <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 696</a></span>, and n. 7 (1993), we similarly assumed Rule 15(b)'s application to habeas petitions. There, however, the District Court had granted a writ of habeas corpus on a claim neither pleaded, considered at "an evidentiary hearing," nor "even argu[ed]" by the parties. <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#695" aria-description="Citation for case: Withrow v. Williams"><i>Id.,</i> at 695</a></span>. Given those circumstances, we held that there had been no trial of the claim by implied consent; the respondent warden, we observed, "was manifestly prejudiced by the District Court's failure to afford her an opportunity to present evidence bearing on th[e] claim's resolution." <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams"><i>Id.,</i> at 696</a></span>. Here, in contrast, the issue of the undisclosed Cook interrogation transcript was indeed aired before the Magistrate Judge and the transcript itself was admitted into evidence without objection. See <i>supra,</i> at 685.<sup>[19]</sup></p>
<p>The Court of Appeals found no authority for equating "an evidentiary hearing . . . with a trial" for Rule 15(b) purposes. App. to Pet. for Cert. A52. We see no reason why an evidentiary hearing should not qualify so long as the respondent gave "any sort of consent" and had a full and fair "opportunity <span class="star-pagination">*705</span> to present evidence bearing on th[e] claim's resolution." <i>Withrow,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams">507 U. S., at 696</a></span>. Nor do we find convincing the Fifth Circuit's view that applying Rule 15(b) in habeas proceedings would undermine the State's exhaustion and procedural default defenses. <i><span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/" aria-description="Citation for case: Withrow v. Williams">Ibid.</a></span></i> Under pre-AEDPA law, there was no inconsistency between Rule 15(b) and those defenses. That is doubtless why this Court's pre-AEDPA cases assumed Rule 15(b)'s application in habeas proceedings. See <i>ibid.; </i><i>Harris,</i> <span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/#294" aria-description="Citation for case: Harris v. Nelson">394 U. S., at 294, n. 5</a></span>.<sup>[20]</sup> We note in this regard that, while AEDPA forbids a finding that exhaustion has been waived unless the State expressly waives the requirement, <span class="citation no-link">28 U. S. C. § 2254</span>(b)(3), under pre-AEDPA law, exhaustion and procedural default defenses could be waived based on the State's litigation conduct. See <i>Gray</i> v. <i>Netherland,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#166" aria-description="Citation for case: Gray v. Netherland">518 U. S. 152, 166</a></span> (1996) (failure to raise procedural default in federal habeas court means the defense is lost); <i>Granberry</i> v. <i>Greer,</i> <span class="citation" data-id="111862"><a href="/opinion/111862/granberry-v-greer/#135" aria-description="Citation for case: Granberry v. Greer">481 U. S. 129, 135</a></span> (1987) ("if a full trial has been held in the district court and it is evident that a miscarriage of justice has occurred, it may . . . be appropriate for the court of appeals to hold that the nonexhaustion defense has been waived").</p>
<p>To obtain a certificate of appealability, a prisoner must "demonstrat[e] that jurists of reason could disagree with the district court's resolution of his constitutional claims or that jurists could conclude the issues presented are adequate to deserve encouragement to proceed further." <i>Miller-El</i> v. <i>Cockrell,</i> <span class="citation" data-id="9434356"><a href="/opinion/122258/miller-el-v-cockrell/#327" aria-description="Citation for case: Miller-El v. Cockrell">537 U. S. 322, 327</a></span> (2003). At least as to the application of Rule 15(b), this case surely fits that description. A certificate of appealability, therefore, should have issued.</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, the judgment of the United States Court of Appeals for the Fifth Circuit is reversed, and the <span class="star-pagination">*706</span> case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE THOMAS, with whom JUSTICE SCALIA joins, concurring in part and dissenting in part.</p>
<p>I join Part III of the Court's opinion, and respectfully dissent from Part II, which holds that Banks' claim under <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), relating to the nondisclosure of evidence that Farr accepted money from a police officer during the course of the investigation, warrants habeas relief. Although I find it to be a very close question, I cannot conclude that the nondisclosure of Farr's informant status was prejudicial under <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419</a></span> (1995), and <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[1]</sup></p>
<p>To demonstrate prejudice, Banks must show that "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 435</a></span>. The undisclosed material consisted of evidence that "Willie Huff asked [Farr] to help him find [Banks'] gun," and that Huff "gave [Farr] about $200.00 for helping him." App. 442 (Farr Declaration). Banks contends that if Farr's receipt of $200 from Huff had been revealed to the defense, there would have been a "reasonable probability," <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 434</a></span>, that the jury would not have found "beyond a reasonable doubt that there <span class="star-pagination">*707</span> [was] a probability that the defendant, Delma Banks, Jr., would commit criminal acts of violence that would constitute a continuing threat to society." App. 143 (the second special issue presented to the jury) (internal quotation marks omitted).</p>
<p>I do not believe that there is a reasonable probability that the jury would have altered its finding. The jury was presented with the facts of a horrible crime. Banks, after meeting the victim, Richard Whitehead, a 16-year-old boy who had the misfortune of owning a car that Banks wanted, decided "to kill the person for the hell of it" and take his car. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (Tex. Crim. App. 1982) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/904/">464 U. S. 904</a></span> (1983). Banks proceeded to shoot Whitehead three times, twice in the head and once in the upper back. Banks fired one of the shots only 18 to 24 inches away from Whitehead. The jury was thus presented with evidence showing that Banks, apparently on a whim, executed Whitehead simply to get his car.</p>
<p>The jury was also presented with evidence, in the form of Banks' own testimony, that he was willing to abet another individual in obtaining a gun, with the full knowledge that this gun would aid future armed robberies. The colloquy between a prosecuting attorney and Banks makes it clear what Banks thought he was doing:</p>
<blockquote>"Q: You were going to supply him [Farr] your gun so he could do armed robberies?</blockquote>
<blockquote>"A: No, not supply him my gun. A gun.</blockquote>
<blockquote>"Q: In other words you didn't care if it was yours or whose, but you were going to be the man who got the gun to do armed robberies. Is that correct?</blockquote>
<blockquote>"A: He was going to do it.</blockquote>
<blockquote>"Q: I understand, but you were going to supply him the means and possible death weapon in an armed robbery case. Is that correct?</blockquote>
<blockquote>"A: Yes." App. 137 (cross-examination of Banks).</blockquote>
<p><span class="star-pagination">*708</span> Accordingly, the jury was also presented with Banks' willingness to assist others in committing deadly crimes. Indeed, the prosecution referenced this very fact at one point during its closing argument in its attempt to convince the jury that Banks posed a threat to commit violent acts in the future:</p>
<blockquote>"The testimony of Vetrano Jefferson and Robert Farr is of the utmost significance. Vetrano brought before you the scar on his face, put there by Delma Banks. . . . He also corroborates or supports the testimony of Robert Farr. You don't have to believe just Robert in order to find that Delma went to Dallas to get a pistol so that <i>somebody could do some robberies.</i> Marcus Jefferson told you that, too." <i>Id.,</i> at 146 (emphasis added).<sup>[2]</sup></blockquote>
<p>The jury also heard testimony that Banks had violently pistol-whipped and threatened to kill his brother-in-law one week before the murder. Banks now claims that this evidence should be discounted because his trial counsel failed to uncover that the brother-in-law was "responsible for the fight." Brief for Petitioner 33. But even if it is appropriate to mix-and-match the prejudice analysis of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and the claim under <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668</a></span> (1984) (rather than to evaluate them independently, as distinct potential constitutional violations), Banks' response was vastly disproportional to his brother-in-law's actions.</p>
<p>In sum, the jury knew that Banks had murdered a 16-year-old on a whim, had violently attacked and threatened a relative shortly before the murder, and was willing to assist another individual in committing armed robberies by providing the "means and possible death weapon" for these robberies. App. 137. Even if the jury were to discredit entirely <span class="star-pagination">*709</span> Farr's testimony that Banks was planning more robberies,<sup>[3]</sup> in all likelihood the jury still would have found "beyond a reasonable doubt" that there "[was] a probability that [Banks] would commit criminal acts of violence that would constitute a continuing threat to society." <i>Id.,</i> at 143 (internal quotation marks omitted). The randomness and wantonness of the murder would perhaps, standing alone, mandate such a finding. Accordingly, I cannot find that the nondisclosure of the evidence was prejudicial.</p>
<p>Because Banks cannot show prejudice, I do not resolve whether he has cause to excuse his failure to present his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> evidence in state court, <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#11" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1, 11-12</a></span> (1992). But there are reasons to doubt the Court's conclusion that Banks can show cause. For instance, the Court concludes that "[t]his case is congruent with <i>Strickler</i> [v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263</a></span> (1999)]," <i>ante,</i> at 693, relying in part on the State's general denial of all of Banks' factual allegations contained in his January 1992 state habeas application. But, in the relevant state postconviction proceeding in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> the State alleged that the petitioner had already received "`<i>everything</i> known to the government,'" a statement that federal habeas proceedings established was clearly not true. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span> (emphasis added). In the instant case, the particular allegation raised in Banks' state habeas application and denied by the State was that "the <span class="star-pagination">*710</span> prosecution <i>knowingly</i> failed to turn over exculpatory evidence <i>as required by </i><i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span> (1963)." App. 180 (emphasis added). The State, then, could have been denying only that the prosecution <i>knowingly</i> failed to turn over the evidence (there is, incidentally, very little evidence in the record tending to show that any prosecutor had actual knowledge of Huff's payment to Farr). Or, the State could have been denying only that it had failed to turn over evidence <i>in violation of</i> Brady, <i>i. e.,</i> that any evidence the prosecution did not turn over was not material (a position advanced by the State throughout the federal habeas process), see <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene"><i>Strickler, supra,</i> at 281</a></span> ("[S]trictly speaking, there is never a real `<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict"). Either way, <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> does not clearly control, and the Court's reliance on it is less than compelling.</p>
<p>Because of the Court's disposition of Banks' Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, it does not address his claim of ineffective assistance of counsel, concluding that "any relief he could obtain on that claim would be cumulative." <i>Ante,</i> at 689, n. 10. As I would affirm the Court of Appeals on the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, I briefly discuss this ineffective-assistance claim. Although I find the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim a close call, I do not find this to be so as to the ineffective-assistance claim. Banks comes nowhere close to satisfying the prejudice prong of <i>Strickland</i> v. <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Washington, supra</a></span></i><i>.</i> The conclusory and uncorroborated claims of some level of physical abuse, the allegations that a bad skin condition negatively affected his childhood development, the evidence that he was a slow learner and possessed a willingness to please others, and the claim that Banks' brother-in-law was responsible for his own pistol-whipping and receipt of a death threat, are so unpersuasive that there is no reasonable probability that the jury would have come to the opposite conclusion with respect to the future <span class="star-pagination">*711</span> dangerousness special issue, even if presented with this evidence.</p>
<p>I therefore conclude that the Court of Appeals did not err when it denied relief to Banks based on his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and his <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span></i> claim. I would reverse the Court of Appeals only insofar as it did not grant a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for William G. Broaddus et al. by <i>William F. Sheehan;</i> and for John J. Gibbons et al. by <i>Peter Buscemi</i> and <i>Brooke Clagett.</i>
</p>
<p><i>A. P. Carlton, Jr., Lynn R. Coleman,</i> and <i>Matthew W. S. Estes</i> filed a brief for the American Bar Association as <i>amicus curiae.</i></p>
<p>[1]  Although a police officer testified Whitehead's body was found on April 14, App. 8, the Texas Court of Criminal Appeals stated the body was discovered on April 15. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (1982) (en banc).</p>
<p>[2]  "A person commits an offense if he commits murder . . . and . . . the person intentionally commits the murder in the course of committing or attempting to commit kidnapping, burglary, robbery, aggravated rape, or arson." <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(2) (1974).</p>
<p>[3]  As set forth in Texas law, the three special issues were:
</p>
<p>"(1) whether the conduct of the defendant that caused the death of the deceased was committed deliberately and with the reasonable expectation that the death of the deceased or another would result;</p>
<p>"(2) whether there is a probability that the defendant would commit criminal acts of violence that would constitute a continuing threat to society; and</p>
<p>"(3) if raised by the evidence, whether the conduct of the defendant in killing the deceased was unreasonable in response to the provocation, if any, by the deceased." Tex. Code Crim. Proc. Ann., Arts. 37.071(b)(1)-(3) (Vernon Supp. 1980).</p>
<p>[4]  Banks, in fact, had no criminal record at all. App. 255, ¶ 115; App. to Pet. for Cert. C23. He also "had no history of violence or alcohol abuse and seemed to possess a self-control that would suggest no particular risk of future violence." <i><span class="citation no-link">Ibid.</span></i></p>
<p>[5]  <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963), held that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution."</p>
<p>[6]  Banks also alleged ineffective assistance of counsel at both the guilt and penalty phases; insufficient evidence on the second penalty-phase special issue (Banks's propensity to commit violent criminal acts); and the exclusion of minority jurors in violation of <i>Swain</i> v. <i>Alabama,</i> <span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">380 U. S. 202</a></span> (1965). App. to Pet. for Cert. C5-C7. Banks filed two further state postconviction motions; both were denied. Brief for Respondent 6-7, nn. 6 and 7 (citing <i>Ex parte Banks,</i> No. 13568-03 (Tex. Crim. App. 1993) <i>(per curiam),</i> and <i>Ex parte Banks,</i> No. 13568-06 (Tex. Crim. App.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./538/990/">538 U. S. 990</a></span> (2003)).</p>
<p>[7]  We hereinafter refer to these claims as the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims respectively. See <i>supra,</i> at 682, n. 5.</p>
<p>[8]  Federal Rule of Civil Procedure 15(b) provides: "When issues not raised by the pleadings are tried by express or implied consent of the parties, they shall be treated in all respects as if they had been raised in the pleadings. Such amendment of the pleadings as may be necessary to cause them to conform to the evidence and to raise these issues may be made upon motion of any party at any time. . . ." Rule 11 of the Rules Governing Section 2254 Cases in the United States District Courts provides that the Federal Rules of Civil Procedure apply "to the extent that they are not inconsistent with [habeas] rules."</p>
<p>[9]  The Fifth Circuit noted correctly that under <i>Lindh</i> v. <i>Murphy,</i> <span class="citation" data-id="9433497"><a href="/opinion/118135/lindh-v-murphy/#336" aria-description="Citation for case: Lindh v. Murphy">521 U. S. 320, 336-337</a></span> (1997), the standards of the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>, do not apply to Banks's petition. See App. to Pet. for Cert. A14-A15.</p>
<p>[10]  Our disposition of the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, and our conclusion that a writ of habeas corpus should issue with respect to the death sentence, render it unnecessary to address Banks's claim of ineffective assistance of counsel at the penalty phase; any relief he could obtain on that claim would be cumulative.</p>
<p>[11]  Banks's federal habeas petition, the Court of Appeals said, stated a claim, only under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> that material exculpatory or impeachment evidence had been suppressed, not a claim under <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), that the prosecution had failed to correct Farr's false testimony. App. to Pet. for Cert. A29-A32; App. 259-260. In its view, the Court of Appeals explained, a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim is distinct from a <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span></i> claim, App. to Pet. for Cert. A30; thus the two did not fit under one umbrella. But cf. <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#679" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 679-680, n. 8</a></span> (1985); <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U.S. 97, 103-104</a></span> (1976). On brief, the parties debate the issue. Brief for Petitioner 23-25; Brief for Respondent 21-22, n. 21. Because we conclude that Banks qualifies for relief under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> we need not decide whether a <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span></i> claim, to warrant adjudication, must be separately pleaded.</p>
<p>[12]  Surprisingly, the Court of Appeals' <i>per curiam</i> opinion did not refer to <i>Strickler</i> v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263</a></span> (1999), the controlling precedent on the issue of "cause." App. to Pet. for Cert. A15-A33.</p>
<p>[13]  We left open the question "whether any one or two of these factors would be sufficient to constitute cause." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>. We need not decide that question today.</p>
<p>[14]  In addition, Banks could have expected disclosure of Farr's informant status as a matter of state law if Farr in fact acted in that capacity. Under Texas law applicable at the time of Banks's trial, the State had an obligation to disclose the identity of an informant when "the informant . . . was present at the time of the offense or arrest . . . [or] was otherwise shown to be a material witness to the transaction. . . ." <i>Kemner</i> v. <i>State,</i> <span class="citation" data-id="9654256"><a href="/opinion/1571252/kemner-v-state/#408" aria-description="Citation for case: Kemner v. State">589 S. W. 2d 403, 408</a></span> (Tex. Crim. App. 1979) (quoting <i>Carmouche</i> v. <i>State,</i> <span class="citation" data-id="9779100"><a href="/opinion/2467197/carmouche-v-state/#703" aria-description="Citation for case: Carmouche v. State">540 S. W. 2d 701, 703</a></span> (Tex. Crim. App. 1976)); cf. Tex. Rule Evid. 508(c)(1) (2003) ("No privilege exists [for the identity of an informer] . . . if the informer appears as a witness for the public entity."). Farr was present when Banks was arrested. App. 443, ¶ 10. Further, as the prosecution noted in its penalty-phase summation, Farr's testimony was not only material, but "of the utmost significance." <i>Id.,</i> at 146.</p>
<p>[15]  The Court of Appeals also stated that, because "the State did not respond" to Banks's "Farr-was-an-informant contention" in its answer to the January 1992 state habeas application, Banks should have "further investigate[d]." App. to Pet. for Cert. A22. The Fifth Circuit's error in this regard is apparent. As earlier recounted, see <i>supra,</i> at 683, the State's answer indeed did deny Banks's allegation.</p>
<p>[16]  Furthermore, rather than conceding the need for factual development of the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state postconviction court, the State asserted that Banks's prosecutorial misconduct claims were meritless and procedurally barred in that tribunal. App. 234, 240. Having taken that position in 1992, the State can hardly fault Banks now for failing earlier to request assistance the State certainly would have opposed.</p>
<p>[17]  It bears reiteration here that Banks had no criminal record, <i>id.,</i> at 255, ¶ 115, "no history of violence or alcohol abuse," nothing indicative of "[any] particular risk of future violence." App. to Pet. for Cert. C23.
</p>
<p>It also appears that the remaining prosecution witness in the penalty phase, Vetrano Jefferson, had omitted crucial details from his 1980 testimony. In his September 1980 testimony, Vetrano Jefferson said that Banks had struck him with a pistol in early April 1980. App. 104-105; <i>supra,</i> at 679-680. In the federal habeas proceeding, Vetrano Jefferson elaborated that he, not Banks, had initiated that incident by making "disrespectful comments" about Demetra Jefferson, Banks's girlfriend. App. 337, ¶ 4. Vetrano Jefferson recounted that he "grew angry" when Banks objected to the comments, and only then did a fight ensue, in the course of which Banks struck Vetrano Jefferson. <i>Ibid.</i></p>
<p>[18]  On brief and at oral argument, the State suggests that "the damaging evidence was Banks's willing abetment of Farr's commission of a violent crime, <i>not</i> Banks's own intent to commit such an act." Brief for Respondent 25 (emphasis in original); Tr. of Oral Arg. 50. See also <i>post,</i> at 707-708 (THOMAS, J., concurring in part and dissenting in part). In the penalty-phase summation, however, the prosecution highlighted Banks's propensity to commit violent criminal acts, see App. 140, 144, 146-147, not his facilitation of others' criminal acts, see <i>id.,</i> at 141 ("[Banks] says, `I thought I would give [the gun] to them so they could do the robberies.' I don't believe you [the jury] believe that."); <i>id.,</i> at 143 ("a man doesn't travel two hundred miles . . . to supply [another] person with a weapon"). The special issue the prosecution addressed focused on what acts Banks would commit, not what harms he might facilitate: "Do you find from the evidence beyond a reasonable doubt that there is a probability that the defendant, Delma Banks, Jr., would <i>commit</i> criminal acts of violence that would constitute a continuing threat to society?" <i>Ibid.</i> (internal quotation marks omitted and emphasis added). It is therefore unsurprising that the prosecution did not rest on Banks's facilitation of others' criminal acts in urging the jury to answer the second special issue (propensity to commit violent criminal acts) in the affirmative.</p>
<p>[19]  See Federal Evidentiary Hearing 56-73. Examining one of Banks's prosecutors, counsel for Banks twice asked if Cook had been "instructed. . . on how to testify." <i>Id.,</i> at 56. See also <i>id.,</i> at 63-64 ("Texarkana law enforcement did not instruct Mr. Cook how to testify in this case. Is that your testimony today?"). To show that Cook had been coached, Banks's counsel called attention to discrepancies between portions of the September 1980 transcript and Cook's trial testimony. <i>Id.,</i> at 65-68. Concluding his examination, Banks's counsel emphasized the prosecution's duty to disclose the September 1980 transcript once Cook, while on the stand, stated that he had not been coached. <i>Id.,</i> at 73-74; App. 59; <i>supra,</i> at 677.</p>
<p>[20]  Banks's case provides no occasion to consider Rule 15(b)'s application under the AEDPA regime.</p>
<p>[1]  I do not address the possible application of the standard enunciated in <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), since I agree with the Court of Appeals that the issue was not properly raised below, and since addressing this issue would go beyond the question on which certiorari was granted. See Brief for Petitioner (i) (stating the question presented as whether "the Fifth Circuit commit[ted] legal error in rejecting Banks' <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim  that the prosecution suppressed material witness impeachment evidence that prejudiced him in the penalty phase of his trial  on the grounds that: . . . the suppressed evidence was immaterial to Banks' death sentence").</p>
<p>[2]  Admittedly, the prosecution used more of its closing argument trying to convince the jury to believe Farr's testimony that Banks himself was planning more robberies. See <i>ante,</i> at 699-700, n. 18. This fact is one of the reasons I find the materiality question to be a close one.</p>
<p>[3]  It is quite possible that the jury already discredited this aspect of Farr's testimony. The jury knew, from the testimony of witnesses James Kelley and Officer Gary Owen, that Farr was generally dishonest, as it heard how he had lied about getting into an altercation with a doctor over false prescriptions, and had lied about his status as an informant for an Arkansas officer in other cases. The Court suggests that the witnesses providing this information were themselves "impeached." <i>Ante,</i> at 702. At best, though, they were only slightly impeached. The prosecution merely intimated that Owen was slanting his testimony in the hopes of being hired by the defense counsel's private investigator, App. 131, and that Kelley was doing the same as he was a "friend of [Banks'] family," <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#141" aria-description="Citation for case: Brady v. Maryland"><i>id.,</i> at 141</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Beckwith v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Beckwith v. United States"
type: case
citation: "425 U.S. 341 (1976)"
parallel_cite: "96 S. Ct. 1612; 48 L. Ed. 2d 1; 37 A.F.T.R.2d (RIA) 1232"
neutral_cite: 1976 U.S. LEXIS 147
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-21
docket: 74-1243
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Beckwith v. United States
  varies_by_point: false
  scope_note: "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview — even of a criminal-investigation target in a private home — requires no Miranda warnings."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109430/beckwith-v-united-states/"
  cluster_id: 109430
  opinion_id: 9426365
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Orozco v. Texas]]", "[[Mathis v. United States (1968)]]", "[[Oregon v. Mathiason]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "focus", "irs", "noncustodial-interrogation"]
holding: "Miranda warnings are required by custody, not by the fact that an investigation has 'focused' on the suspect; a noncustodial interview by IRS special agents — even of a person who is the target of a criminal tax investigation, conducted in a private home — does not trigger Miranda."
lake:
  record_id: Beckwith v. United States
  status: verified
  projected_at: 2026-07-06
---

# Beckwith v. United States

*425 U.S. 341 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two special agents of the IRS Intelligence Division — the unit assigned only when there is some indication of criminal tax fraud — met Beckwith at about 8 a.m. in a private home where he occasionally stayed. They were invited in, identified themselves, said they investigate criminal tax violations, and told him they were investigating his income-tax liability for 1966–71. The senior agent read a partial advisement (that the Fifth Amendment barred compelling his answers, that anything he said could be used against him, and that he could seek an attorney before responding) but not full [[Miranda and Custodial Interrogation|Miranda warnings]]. The roughly three-hour interview was "friendly" and "relaxed," and Beckwith was neither arrested nor detained; he later supplied records. He moved to suppress, arguing that because he was the "focus" of a criminal investigation the encounter was the functional equivalent of custody.

## Issue
Whether a noncustodial interview by IRS special agents investigating potential criminal tax violations requires [[Miranda and Custodial Interrogation|Miranda warnings]] because the taxpayer is the "focus" of the investigation.

## Rule
No — Miranda turns on custody, not investigative focus. In its decisions after *[[Miranda v. Arizona|Miranda]]* "the Court specifically stressed that it was the *custodial* nature of the interrogation which triggered the necessity for adherence to the specific requirements of its *Miranda* holding." — 425 U.S. at 346 (citing [[Orozco v. Texas]] and [[Mathis v. United States (1968)]]). ^pin-346

"'It was the compulsive aspect of custodial interrogation, and not the strength or content of the government's suspicions at the time the questioning was conducted, which led the court to impose the *Miranda* requirements with regard to custodial questioning.'" — *Id.* at 346–347 (quoting *United States v. Caiello*, 420 F.2d 471, 473 (CA2 1969)). ^pin-347

*[[Miranda v. Arizona|Miranda]]* "implicitly defined 'focus' . . . as 'questioning initiated by law enforcement officers *after* a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.'" — *Id.* at 347 (quoting *Miranda*, 384 U.S. at 444).

## Application
"Although the 'focus' of an investigation may indeed have been on Beckwith at the time of the interview in the sense that it was his tax liability which was under scrutiny, he hardly found himself in the custodial situation described by the *Miranda* Court as the basis for its holding." The friendly, noncustodial home interview lacked the inherently coercive, police-dominated elements that *[[Miranda v. Arizona|Miranda]]* addressed; that the interview may have been the "starting point" for prosecution did not convert it into custody. No full [[Miranda and Custodial Interrogation|Miranda warnings]] were required, and the statements were admissible.

## Conclusion
A noncustodial interview does not require [[Miranda and Custodial Interrogation|Miranda warnings]] merely because the suspect is the focus of a criminal investigation; the judgment of conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Beckwith* fixes **custody** (not focus) as the Miranda trigger in the [[Miranda v. Arizona]] line, distinguishing [[Mathis v. United States (1968)]] (Miranda applies to an IRS interview of a person *in custody*) and harmonizing with the noncustodial station-house interview in [[Oregon v. Mathiason]] and the in-home custody of [[Orozco v. Texas]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Beckwith v. United States*, 425 U.S. 341 (1976) — https://www.courtlistener.com/opinion/109430/beckwith-v-united-states/ — pinpoints: 346, 347.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee3336f1b22e3704", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "425 U.S. 341 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 147", "official_citation_present": true, "parallel_cite": "96 S. Ct. 1612; 48 L. Ed. 2d 1; 37 A.F.T.R.2d (RIA) 1232", "title": "Beckwith v. United States", "year": "1976"}}
{"assertion_id": "2e46188e21688982", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Miranda warnings are required by custody, not by the fact that an investigation has 'focused' on the suspect; a noncustodial interview by IRS special agents — even of a person who is the target of a criminal tax investigation, conducted in a private home — does not trigger Miranda.", "title": "Beckwith v. United States"}}
{"assertion_id": "71e982b6edf1e224", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Beckwith v. United States"}}
{"assertion_id": "4cc8f3ddfdd067cb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-04-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Beckwith v. United States", "field_i_validity": "good_law", "scope_note": "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview — even of a criminal-investigation target in a private home — requires no Miranda warnings.", "title": "Beckwith v. United States", "varies_by_point": "false"}}
{"assertion_id": "e5c310efb4585a1e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Beckwith v. United States"}}
```

### lake record — Beckwith v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Beckwith v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Beckwith v. United States",
    "case_name_short": "Beckwith",
    "case_name_full": "Beckwith v. United States",
    "input_case_name": "Beckwith v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-21",
    "year": 1976,
    "docket": "74-1243",
    "cluster_id": 109430,
    "lead_opinion_id": 9426365,
    "sibling_ids": [
      109430,
      9426365,
      9426366,
      9426367
    ],
    "absolute_url": "/opinion/109430/beckwith-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 341",
      "volume": "425",
      "reporter": "U.S.",
      "page": "341",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1612",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 1",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1232",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 147",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 341",
        "volume": "425",
        "reporter": "U.S.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1612",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 1",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 147",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1232",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 341",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 341",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-346",
      "page": null,
      "quote": "of the investigation. ## Rule No \u2014 Miranda turns on custody, not investigative focus. In its decisions after *Miranda*",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-347",
      "page": null,
      "quote": "'It was the compulsive aspect of custodial interrogation, and not the strength or content of the government's suspicions at the time the questioning was conducted, which led the court to impose the *Miranda* requirements with regard to custodial questioning.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Beckwith v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview \u2014 even of a criminal-investigation target in a private home \u2014 requires no Miranda warnings.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. John Noehl and Analise Noehl",
          "cluster_id": 10618700,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lawrence Samuel Jr. v. State",
          "cluster_id": 3130658,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Charles",
          "cluster_id": 1563356,
          "cite": [
            "16 So. 3d 1166",
            "2009 La. LEXIS 2354",
            "2009 WL 2838411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Edward Uzenski",
          "cluster_id": 792949,
          "cite": [
            "434 F.3d 690",
            "69 Fed. R. Serv. 274",
            "2006 U.S. App. LEXIS 827",
            "2006 WL 73632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkerson, Ray Mitchell",
          "cluster_id": 2936737,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "White v. State",
          "cluster_id": 1777867,
          "cite": [
            "931 S.W.2d 736",
            "1996 Tex. App. LEXIS 4445",
            "1996 WL 580988"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Beheler",
          "cluster_id": 111023,
          "cite": [
            "77 L. Ed. 2d 1275",
            "103 S. Ct. 3517",
            "463 U.S. 1121",
            "1983 U.S. LEXIS 114",
            "51 U.S.L.W. 3934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1653372,
          "cite": [
            "836 S.W.2d 530",
            "1992 Tenn. LEXIS 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. State",
          "cluster_id": 1749178,
          "cite": [
            "306 S.W.3d 274",
            "2009 Tex. Crim. App. LEXIS 1441",
            "2009 WL 3365652"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Commonwealth",
          "cluster_id": 1227505,
          "cite": [
            "307 S.E.2d 864",
            "226 Va. 31",
            "1983 Va. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Matheny",
          "cluster_id": 2637091,
          "cite": [
            "46 P.3d 453",
            "2002 WL 1009210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Washington",
          "cluster_id": 109659,
          "cite": [
            "52 L. Ed. 2d 238",
            "97 S. Ct. 1814",
            "431 U.S. 181",
            "1977 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. State",
          "cluster_id": 2437346,
          "cite": [
            "712 S.W.2d 499",
            "1986 Tex. Crim. App. LEXIS 1275"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcus T. Baumann v. United States",
          "cluster_id": 410430,
          "cite": [
            "692 F.2d 565",
            "1982 U.S. App. LEXIS 24530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Chalan, Jr.",
          "cluster_id": 483901,
          "cite": [
            "812 F.2d 1302",
            "1987 U.S. App. LEXIS 2758",
            "22 Fed. R. Serv. 1200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shiflet v. State",
          "cluster_id": 1745641,
          "cite": [
            "732 S.W.2d 622",
            "1985 Tex. Crim. App. LEXIS 1718"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John E. Kenny, Trenton P. Oelberg, and William L. Parker, Defendants",
          "cluster_id": 389261,
          "cite": [
            "645 F.2d 1323"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Joseph, Petitioner-Appellant/cross-Appellee v. Ralph Coyle, Warden, Respondent-Appellee/cross-Appellant",
          "cluster_id": 796039,
          "cite": [
            "469 F.3d 441",
            "2006 U.S. App. LEXIS 27697",
            "2006 WL 3250935"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1655134,
          "cite": [
            "740 S.W.2d 779",
            "1987 Tex. Crim. App. LEXIS 671",
            "1987 WL 1000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meek v. State",
          "cluster_id": 1577494,
          "cite": [
            "790 S.W.2d 618",
            "1990 Tex. Crim. App. LEXIS 84",
            "1990 WL 67493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MTQ1NzkyMDAwMDAmcz0xNTMwMTI4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODImcz0xOTAwMzU2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 1,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
    "indexed_citing_opinions": 706,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109430,
        "count": 649,
        "count_source": "search"
      },
      {
        "opinion_id": 9426365,
        "count": 77,
        "count_source": "search"
      },
      {
        "opinion_id": 9426366,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426367,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1005,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/beckwith-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUzNTI5ODgmcz00Mzc4NTI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109430,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 281129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 281735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 285855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 288179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 289616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 292827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 294195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 294580,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 299047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 310330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 322550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 325001,
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
    "date_created": "2026-07-04T19:27:30Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:33:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Beckwith v. United States

```
<opinion type="majority">
<author id="b411-12">Mr. Chief Justice Burger</author>
<p id="AtZ">delivered the opinion of the Court.</p>
<p id="b411-13">The important issue presented in this case is whether a special agent of the Internal Revenue Service, investigating potential criminal income tax violations, must, in <page-number citation-index="1" label="342">*342</page-number>an interview with a taxpayer, not in custody, give the warnings called for by this Court’s decision in <em>Miranda </em>v. Arizona, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). We granted certiorari to resolve the conflict between the holding of the Court of Appeals in this case, which is consistent with the weight of authority on the issue,<footnotemark>1</footnotemark> and the position adopted by the United States Court of Appeals for the Seventh Circuit.<footnotemark>2</footnotemark></p>
<p id="b412-5">The District Court conducted a thorough inquiry into the facts surrounding the interview of petitioner before ruling on his motion to suppress the statements at issue. After a considerable amount of investigation, two special agents of the Intelligence Division of the Internal Revenue Service met with petitioner in a private home where petitioner occasionally stayed. The senior agent testified that they went to see petitioner at this private residence at 8 a. m. in order to spare petitioner the possible embarrassment of being interviewed at his place of employment which opened at 10 a. m. Upon their arrival, they identified themselves to the person answering the door and asked to speak to petitioner. The agents were invited into the house and, when petitioner entered the room where they were waiting, they introduced them<page-number citation-index="1" label="343">*343</page-number>selves and, according to the testimony of the senior agent, Beckwith then excused himself for a period in excess of five minutes, to finish dressing.<footnotemark>3</footnotemark> Petitioner then sat down at the dining room table with the agents; they presented their credentials and stated they were attached to the Intelligence Division and that one of their functions was to investigate the possibility of criminal tax fraud. They then informed petitioner that they were assigned to investigate his federal income tax liability for the years 1966 through 1971. The senior agent then read to petitioner from a printed card the following:</p>
<blockquote id="b413-5">“As a special agent, one of my functions is to investigate the possibility of criminal violations of the Internal Revenue laws, and related offenses.</blockquote>
<blockquote id="b413-6">“Under the Fifth Amendment to the Constitution of the United States, I cannot compel you to answer any questions or to submit any information if such answers or information might tend to incriminate you in any way. I also advise you that anything which you say and any information which you submit may be used against you in any criminal proceeding which may be undertaken. I advise you further that you may, if you wish, seek the assistance of an attorney before responding.” App. 65-66.</blockquote>
<p id="b413-7">Petitioner acknowledged that he understood his rights. The agents then interviewed him until about 11 o’clock. The agents described the conversation as “friendly” and “relaxed.” The petitioner noted that the agents did not “press” him on any question he could not or chose not to answer.</p>
<p id="b413-8">Prior to the conclusion of the interview, the senior agent requested that petitioner permit the agents to <page-number citation-index="1" label="344">*344</page-number>inspect certain records. Petitioner indicated that they were at his place of employment. The agents asked if they could meet him there later. Having traveled separately from petitioner, the agents met petitioner approximately 45 minutes later and the senior agent advised the petitioner that he was not required to furnish any books or records; petitioner, however, supplied the books to the agents.</p>
<p id="b414-5">Prior to trial, petitioner moved to suppress all statements he made to the agents or evidence derived from those statements on the ground that petitioner had not been given the warnings mandated by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The District Court ruled that he was entitled to such warnings “when the court finds as a fact that there were custodial circumstances.” The District Judge went on to find that “on this record . . . there is no evidence whatsoever of any such situation.” The Court of Appeals affirmed the judgment of conviction. 166 U. S. App. D. C. 361, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d 741</a></span> (1975). It noted that the reasoning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was based “in crucial part” on whether the suspect “has been taken into custody or otherwise deprived of his freedom in any significant way,” <em>id., </em>at 362, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#742" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 742</a></span>, citing <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 477</a></span>; and agreed with the District Court that “Beckwith was neither arrested nor detained against his will.” 166 U. S. App. D. C., at 362, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#742" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 742</a></span>. We agree with the analysis of the Court of Appeals<footnotemark>4</footnotemark> and, therefore, affirm its judgment.</p>
<p id="b414-6">Petitioner contends that the “entire starting point” for the criminal prosecution brought against him was secured from his own statements and disclosures during the interview with the Internal Revenue agents from the <page-number citation-index="1" label="345">*345</page-number>Intelligence Division. He correctly points out that cases are assigned to the Intelligence Division only when there is some indication of criminal fraud and that, especially since tax offenses rarely result in pretrial custody, the taxpayer is clearly the “focus” of a criminal investigation when a matter is assigned to the Intelligence Division. Given the complexity of the tax structure and the confusion on the part of taxpayers between the civil and criminal function of the Internal Revenue Service, such a confrontation, argues petitioner, places the taxpayer under “psychological restraints” which are the functional, and, therefore, the legal, equivalent of custody. In short we agree with Chief Judge Bazelon, speaking for a unanimous Court of Appeals, that</p>
<blockquote id="b415-5">“[t]he major thrust of Beckwith’s argument is that the principle of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em>Mathis </em>[<footnotemark>5</footnotemark>] should be extended to cover interrogation in non-custodial circumstances after a police investigation has focused on the suspect.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b415-6">With the Court of Appeals, we “are not impressed with this argument in the abstract nor as applied to the particular facts of Beckwith’s interrogation.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>It goes far beyond the reasons for that holding and such an extension of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements would cut this Court’s holding in that case completely loose from its own explicitly stated rationale. The narrow issue before the Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was presented very precisely in the opening paragraph of that opinion — “the admissibility of statements obtained from an individual who is subjected to <em>custodial </em>police interrogation.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 439</a></span>.<footnotemark>6</footnotemark> (Emphasis supplied.) The Court concluded <page-number citation-index="1" label="346">*346</page-number>that compulsion is “inherent in custodial surroundings,” <footnotemark>7</footnotemark> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 458</a></span>, and, consequently, that special safeguards were required in the case of “incommunicado interrogation of individuals in a police-dominated atmosphere, resulting in self-incriminating statements without full warnings of constitutional rights.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 445</a></span>. In subsequent decisions, the Court specifically stressed that it was the <em>custodial </em>nature of the interrogation which triggered the necessity for adherence to the specific requirements of its <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding. <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969); <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968). See generally <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 247</a></span> (1973).</p>
<p id="b416-5">Petitioner’s argument that he was placed in the functional, and, therefore, legal, equivalent of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>situation asks us now to ignore completely that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was grounded squarely in the Court’s explicit and detailed assessment of the peculiar “nature and setting of . . . in-custody interrogation,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445</a></span>. That Courts of Appeals have so read <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is suggested by Chief Judge Lumbard in <em>United States </em>v. <em>Caiello, </em><span class="citation" data-id="9455181"><a href="/opinion/287949/united-states-v-richard-v-caiello/#473" aria-description="Citation for case: United States v. Richard v. Caiello">420 F. 2d 471, 473</a></span> (CA2 1969):</p>
<blockquote id="b416-6">“ Tt was the compulsive aspect of custodial interrogation, and not the strength or content of the government’s suspicions at the time the questioning was conducted, which led the court to impose the <page-number citation-index="1" label="347">*347</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements with regard to custodial questioning.' ”</blockquote>
<p id="b417-6"><em>Mathis </em>v. <em>United States, supra, </em>directly supports this conclusion in holding that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements are applicable to interviews with Internal Revenue agents concerning tax liability, <em>when the subject is in custody; </em>the Court thus squarely grounded its holding on the custodial aspects of the situation, not the subject matter of the interview.<footnotemark>8</footnotemark></p>
<p id="b417-7">An interview with Government agents in a situation such as the one shown by this record simply does not present the elements which the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court found so inherently coercive as to require its holding. Although the “focus” of an investigation may indeed have been on Beckwith at the time of the interview in the sense that it was his tax liability which was under scrutiny, he hardly found himself in the custodial situation described by the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court as the basis for its holding. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>implicitly defined “focus,” for its purposes, as “questioning initiated by law enforcement officers <em>after </em>a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. (Emphasis supplied.) It may well be true, as petitioner contends, that the “starting point” for the criminal prosecution was the information obtained from petitioner and the records exhibited by him. But this amounts to no more than saying that a tax return signed by a taxpayer can be the “starting point” for a prosecution.</p>
<p id="b417-8">We recognize, of course, that noncustodial interrogation might possibly in some situations, by virtue of some <page-number citation-index="1" label="348">*348</page-number>special circumstances, ,be characterized as one where “the behavior of . . . law enforcement officials was such as to overbear petitioner's will to resist and bring about confessions not freely self-determined-” <em>Rogers </em>v. <em>Richmond, </em><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#544" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 544</a></span> (1961). When such a claim is raised, it is the duty of an appellate court, including this Court, “to examine the entire record and make an independent determination of the ultimate issue of- voluntariness." <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741-742</a></span> (1966). Proof that some kind of warnings were given or that none were given would be relevant evidence only on the issue of whether the questioning was in fact coercive. <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969); <em>Davis </em>v. <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina"><em>North Carolina, supra, </em>at 740-741</a></span>. In the present case, however, as Chief Judge Bazelon noted, “[t]he entire interview was free of coercion,” 166 U. S. App. D. C., at 363, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#743" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 743</a></span> (footnote omitted).</p>
<p id="b418-6">Accordingly, the judgment of the Court of Appeals is</p>
<p id="b418-7">
<em>Affirmed.</em>
</p>
<p id="b418-8">Me. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b412-6"> See, <em>e. g., Taglianetti </em>v. <em>United States, </em><span class="citation" data-id="281129"><a href="/opinion/281129/louis-j-taglianetti-v-united-states/#566" aria-description="Citation for case: Louis J. Taglianetti v. United States">398 F. 2d 558, 566</a></span> (CA1 1968), aff'd on another ground, <span class="citation" data-id="107880"><a href="/opinion/107880/taglianetti-v-united-states/" aria-description="Citation for case: Taglianetti v. United States">394 U. S. 316</a></span> (1969); <em>United States </em>v. <em>Mackiewicz, </em><span class="citation" data-id="9453948"><a href="/opinion/281735/united-states-v-walter-p-mackiewicz-and-florence-b-mackiewicz/#221" aria-description="Citation for case: United States v. Walter P. MacKiewicz and Florence B....">401 F. 2d 219, 221-222</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./393/923/">393 U. S. 923</a></span> (1968); <em>United States </em>v. <em>Jaskiewicz, </em><span class="citation" data-id="292827"><a href="/opinion/292827/united-states-v-frank-a-jaskiewicz/#417" aria-description="Citation for case: United States v. Frank A. Jaskiewicz">433 F. 2d 415, 417-420</a></span> (CA3 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/1021/">400 U. S. 1021</a></span> (1971); <em>United States </em>v. <em>Browney, </em><span class="citation" data-id="9455236"><a href="/opinion/288179/united-states-v-hilton-g-browney/#51" aria-description="Citation for case: United States v. Hilton G. Browney">421 F. 2d 48, 51-52</a></span> (CA4 1970); <em>United States </em>v. <em>Prudden, </em><span class="citation" data-id="9455504"><a href="/opinion/289616/united-states-v-horton-r-prudden/#1027" aria-description="Citation for case: United States v. Horton R. Prudden">424 F. 2d 1021, 1027-1031</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/831/">400 U. S. 831</a></span> (1970); <em>United States </em>v. <em>Stribling, </em><span class="citation" data-id="9456470"><a href="/opinion/294580/united-states-v-george-y-stribling/#771" aria-description="Citation for case: United States v. George Y. Stribling">437 F. 2d 765, 771</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./402/973/">402 U. S. 973</a></span> (1971); <em>United States v. MacLeod, 436 F. </em>2d 947, 950 (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./402/907/">402 U. S. 907</a></span> (1971); <em>United States </em>v. <em>Robson, </em><span class="citation" data-id="310330"><a href="/opinion/310330/united-states-v-walter-c-robson/#16" aria-description="Citation for case: United States v. Walter C. Robson">477 F. 2d 13, 16</a></span> (CA9 1973); <em>Hensley </em>v. <em>United </em>States, <span class="citation" data-id="283275"><a href="/opinion/283275/eugene-v-hensley-v-united-states/#484" aria-description="Citation for case: Eugene v. Hensley v. United States">406 F. 2d 481, 484</a></span> (CA10 1968); but cf. <em>United States </em>v. <em>Lockyer, </em><span class="citation" data-id="299047"><a href="/opinion/299047/united-states-v-ralph-lockyer/#422" aria-description="Citation for case: United States v. Ralph Lockyer">448 F. 2d 417, 422</a></span> (CA10 1971).</p>
</footnote>
<footnote label="2">
<p id="b412-7"> <em>United States </em>v. <em>Dickerson, </em><span class="citation" data-id="9454740"><a href="/opinion/285855/united-states-v-albert-dickerson/" aria-description="Citation for case: United States v. Albert Dickerson">413 F. 2d 1111</a></span> (1969).</p>
</footnote>
<footnote label="3">
<p id="b413-9"> Petitioner claimed at the suppression hearing that he was fully-dressed when he first met the agents. The District Court did not explicitly resolve this conflict in testimony.</p>
</footnote>
<footnote label="4">
<p id="b414-7"> On petition for writ of certiorari to this Court, Beckwith does not challenge the further holding of the Court of Appeals that, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>question aside, the “entire interview was free of coercion,” 166 U. S. App. D. C., at 363, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#743" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 <em>F. </em>2d, at 743</a></span> (footnote omitted).</p>
</footnote>
<footnote label="5">
<p id="b415-7"><em> Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968).</p>
</footnote>
<footnote label="6">
<p id="b415-8"> The Court also stated: “The constitutional issue we decide . . . is the admissibility of statements obtained from a defendant questioned while in custody or otherwise deprived of his freedom of action <page-number citation-index="1" label="346">*346</page-number>in any significant way.” 384 U. S., at 445. The Court specifically defined “custodial interrogation” to mean “questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his <em>freedom </em>of action in any significant way.” <em>Id., </em>at 444.</p>
</footnote>
<footnote label="7">
<p id="b416-12"> The Court gave great weight to contemporaneous police manuals and concluded that custodial interrogation was “psychologically . . . oriented,” <em>id., </em>at 448, and that the principal psychological factor contributing to successful interrogation was isolating the suspect in unfamiliar surroundings “for no purpose other than to subjugate the individual to the will of his examiner.” <em>Id., </em>at 457.</p>
</footnote>
<footnote label="8">
<p id="b417-9"> Four Members of the Court joined Mr. Justice Black; the dissenters regarded <em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span> </em>as an extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>largely because the custody and the interrogation were in no way related and because a prisoner interrogated in prison was not in unfamiliar surroundings.</p>
</footnote>
</opinion>
```

---
