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

## GROUP: content/cases/United States v. Bajakajian.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Bajakajian
type: case
citation: "524 U.S. 321 (1998)"
parallel_cite: "118 S. Ct. 2028; 141 L. Ed. 2d 314"
neutral_cite: 1998 U.S. LEXIS 4172
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-06-22
docket: No. 96-1487
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
  opinion_url: "https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/"
  cluster_id: 118234
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Bajakajian
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[Austin v. United States]]"
  - "[[Timbs v. Indiana]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - proportionality
  - currency-reporting
  - punishment
holding: "Requiring forfeiture of the entire $357,144 that the defendant willfully failed to report when transporting currency out of the United States violated the Eighth Amendment's Excessive Fines Clause; a punitive forfeiture is unconstitutionally excessive if the amount forfeited is grossly disproportional to the gravity of the defendant's offense."
aliases:
  - United States v. Bajakajian
  - "United States v. Bajakajian (1998)"
---

# United States v. Bajakajian

*524 U.S. 321 (1998)* (No. 96-1487) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 118234 → combined opinion 118234 (Thomas, J.; 524 U.S. 321, argued Nov. 4, 1997, decided June 22, 1998). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*335` follows the quoted holding, which sits on page 334). S9 promotes. -->

## Background
On June 9, 1994, Hosep Bajakajian and his family were at Los Angeles International Airport waiting to fly to Italy, bound ultimately for Cyprus. Customs inspectors using currency-detecting dogs found cash in the family's baggage; questioned, Bajakajian understated the amount, but a search turned up $357,144 in all. Federal law required travelers to report transporting more than $10,000 out of the country, and 18 U.S.C. § 982(a)(1) directs forfeiture of any property involved in a willful violation. Bajakajian pleaded guilty to the failure-to-report count and had a bench trial on forfeiture. The District Court found the money was not tied to any other crime and was being carried to repay a lawful debt, and that full forfeiture would be "grossly disproportionate" and unconstitutional; it ordered forfeiture of only $15,000 plus a $5,000 fine and probation. The Ninth Circuit affirmed, and the Government sought full forfeiture.

## Issue
Whether forfeiture of the entire $357,144 that the defendant failed to report — a sanction the Court treated as at least partly punitive — would violate the Excessive Fines Clause of the Eighth Amendment.

## Rule
Because the § 982(a)(1) forfeiture functioned as punishment for the reporting offense, it was a "fine" within the Excessive Fines Clause; the Court then supplied the excessiveness standard it had left open in *[[Austin v. United States|Austin]]*. Drawing on the Clause's text and history and on the deference owed to legislative judgments about penalties, the Court adopted a proportionality test: "We now hold that a punitive forfeiture violates the Excessive Fines Clause if it is grossly disproportional to the gravity of a defendant's offense." — 524 U.S. at 334. ^pin-334

## Application
Applying that standard, full forfeiture failed it. Bajakajian's crime was solely a reporting offense: it was lawful to carry the currency abroad so long as he declared it, the money had no connection to any other illegality, and the harm to the Government from the non-report was minimal. Against that, a $357,144 forfeiture dwarfed the $5,000 Guidelines fine by orders of magnitude and bore no articulable correlation to any injury the Government suffered. The Court therefore concluded the forfeiture was grossly disproportional to the gravity of the offense and unconstitutional.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **affirmed**. Thomas, J., delivered the opinion of the Court (Stevens, Souter, Ginsburg, and Breyer, JJ., joined). Kennedy, J., filed a [[Common Legal Terms#dissenting-opinion|dissent]], joined by Rehnquist, C.J., and O'Connor and Scalia, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Bajakajian* is the excessiveness *standard* in the forfeiture line: *[[Austin v. United States]]* (1993) established that punitive civil forfeitures are subject to the Excessive Fines Clause but reserved the test; *Bajakajian* supplies it ("grossly disproportional"); and *[[Timbs v. Indiana]]* (2019) makes the Clause enforceable against the States. It is also the Court's first decision actually striking a federal economic sanction as an excessive fine. Teach it as the operative proportionality rule for challenging a forfeiture as excessive.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. Bajakajian*, 524 U.S. 321 (1998)](https://www.courtlistener.com/opinion/118234/united-states-v-bajakajian/) — pinpoint: 334 (Thomas, J., for the Court; the CL opinion text places the quoted "grossly disproportional" holding immediately before the reporter star `*335`, i.e., on page 334). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "49581263feab821c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "524 U.S. 321 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 4172", "official_citation_present": true, "parallel_cite": "118 S. Ct. 2028; 141 L. Ed. 2d 314", "title": "United States v. Bajakajian", "year": "1998"}}
{"assertion_id": "432b151a7ad65349", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Requiring forfeiture of the entire $357,144 that the defendant willfully failed to report when transporting currency out of the United States violated the Eighth Amendment's Excessive Fines Clause; a punitive forfeiture is unconstitutionally excessive if the amount forfeited is grossly disproportional to the gravity of the defendant's offense.", "title": "United States v. Bajakajian"}}
{"assertion_id": "d133e357e7a123ab", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Anchor", "title": "United States v. Bajakajian"}}
{"assertion_id": "48cce5d8a1cdfed1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Bajakajian", "varies_by_point": "false"}}
{"assertion_id": "a9a49cc4649ecc50", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Bajakajian"}}
```

### lake record — United States v. Bajakajian

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Bajakajian",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Bajakajian",
    "case_name_short": "Bajakajian",
    "case_name_full": "United States v. Bajakajian",
    "input_case_name": "United States v. Bajakajian",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-06-22",
    "year": 1998,
    "docket": "No. 96-1487",
    "cluster_id": 118234,
    "lead_opinion_id": 9433683,
    "sibling_ids": [],
    "absolute_url": "/opinion/118234/united-states-v-bajakajian/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "524 U.S. 321",
      "volume": "524",
      "reporter": "U.S.",
      "page": "321",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "524 U.S. 321",
        "volume": "524",
        "reporter": "U.S.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 2028",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "2028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 L. Ed. 2d 314",
        "volume": "141",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 4172",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "4172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "524 U.S. 321",
    "official_selection": {
      "court_class": "scotus",
      "selected": "524 U.S. 321",
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
    "date_created": "2026-07-06T13:16:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-bajakajian--118234",
      "to_record_id": "United States v. Bajakajian",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Bajakajian

```
<opinion type="majority">
<author id="b368-7">Justice Thomas</author>
<p id="AmP">delivered the opinion of the Court.</p>
<p id="b368-8">Respondent Hosep Bajakajian attempted to leave the United States without reporting, as required by federal law, that he was transporting more than $10,000 in currency. Federal law also provides that a person convicted of willfully violating this reporting requirement shall forfeit to the Government “any property . . . involved in such offense.” <span class="citation no-link">18 U. S. C. § 982</span>(a)(1). The question in this case is whether forfeiture of the entire $857,144 that respondent failed to declare would violate the Excessive Fines Clause of the Eighth Amendment. We hold that it would, because full forfeiture of respondent’s currency would be grossly disproportional to the gravity of his offense.</p>
<p id="b368-9">I</p>
<p id="b368-10">On June 9,1994, respondent, his wife, and his two daughters were waiting at Los Angeles International Airport to board a flight to Italy; their final destination was Cyprus. Using dogs trained to detect currency by its smell, customs inspectors discovered some $230,000 in cash in the Bajakaji-ans’ checked baggage. A customs inspector approached respondent and his wife and told them that they were required to report all money in excess of $10,000 in their possession or in their baggage. Respondent said that he had $8,000 and <page-number citation-index="1" label="325">*325</page-number>that his wife had another $7,000, but that the family had no additional currency to declare. A search of their carry-on bags, purse, and wallet revealed more cash; in all, customs inspectors found $357,144. The currency was seized and respondent was taken into custody.</p>
<p id="b369-5">A federal grand jury indicted respondent on three counts. Count One charged him with failing to report, as required by 31U. S. C. § 5316(a)(1)(A),<footnotemark>1</footnotemark> that he was transporting more than $10,000 outside the United States, and with doing so “willfully,” in violation of § 5322(a).<footnotemark>2</footnotemark> Count Two charged him with making a false material statement to the United States Customs Service, in violation of <span class="citation no-link">18 U. S. C. § 1001</span>. Count Three sought forfeiture of the $357,144 pursuant to <span class="citation no-link">18 U. S. C. § 982</span>(a)(1), which provides:</p>
<blockquote id="b369-6">“The court, in imposing sentence on a person convicted of an offense in violation of section . . . 5316, . . . shall order that the person forfeit to the United States any property, real or personal, involved in such offense, or any property traceable to such property.” <span class="citation no-link">18 U. S. C. § 982</span>(a)(1).</blockquote>
<p id="b369-7">Respondent pleaded guilty to the failure to report in Count One; the Government agreed to dismiss the false statement charge in Count Two; and respondent elected to have a bench trial on the forfeiture in Count Three. After the bench trial, the District Court found that the entire $357,144 was subject to forfeiture because it was “involved <page-number citation-index="1" label="326">*326</page-number>in” the offense. <em><span class="citation no-link">Ibid.</span> </em>The court also found that the funds were not connected to any other crime and that respondent was transporting the money to repay a lawful debt. Tr. 61-62 (Jan. 19,1995). The District Court further found that respondent had failed to report that he was taking the currency out of the United States because of fear stemming from “cultural differences”: Respondent, who had grown up as a member of the Armenian minority in Syria, had a “distrust for the Government.” <span class="citation no-link"><em>Id., </em>at 63</span>; see Tr. of Oral Arg. 30.</p>
<p id="b370-5">Although § 982(a)(1) directs sentencing courts to impose full forfeiture, the District Court concluded that such forfeiture would be “extraordinarily harsh” and “grossly disproportionate to the offense in question,” and that it would therefore violate the Excessive Fines Clause. Tr. 63. The court instead ordered forfeiture of $15,000, in addition to a sentence of three years of probation and a fine of $5,000 — the maximum fine under the Sentencing Guidelines — because the court believed that the maximum Guidelines fine was “too little” and that a $15,000 forfeiture would “make up for what I think a reasonable fine should be.” <em>Ibid.</em></p>
<p id="b370-6">The United States appealed, seeking full forfeiture of respondent’s currency as provided in § 982(a)(1). The Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d 334</a></span> (1996). Applying Circuit precedent, the court held that, to satisfy the Excessive Fines Clause, a forfeiture must fulfill two conditions: The property forfeited must be an “instrumentality” of the crime committed, and the value of the property must be proportional to the culpability of the owner. <em><span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">Id.,</a></span> </em>at 336 (citing <em>United States </em>v. <em>Real Property Located in El Dorado County, </em><span class="citation" data-id="6935354"><a href="/opinion/7033061/united-states-v-real-property-located-in-el-dorado-county-at-6380-little/#982" aria-description="Citation for case: United States v. Real Property Located in El Dorado...">59 F. 3d 974, 982</a></span> (CA9 1995)). A majority of the panel determined that the currency was not an “instrumentality” of the crime of failure to report because “ ‘[t]he crime [in a currency reporting offense] is the withholding of information, . . . not the possession or the transportation of the money.’ ” <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d, at 337</a></span> (quoting <em>United States </em>v. <em>$69,292 </em><page-number citation-index="1" label="327">*327</page-number><em>in United States Currency, </em><span class="citation multiple-matches"><a href="/c/F.%203d/62/1161/">62 F. 3d 1161</a></span>, 1167 (CA9 1995)). The majority therefore held that § 982(a)(1) could never satisfy the Excessive Fines Clause in cases involving forfeitures of currency and that it was unnecessary to apply the “proportionality” prong of the test. Although the panel majority concluded that the Excessive Fines Clause did not permit forfeiture of <em>any </em>of the unreported currency, it held that it lacked jurisdiction to set the $15,000 forfeiture aside because respondent had not cross-appealed to challenge that forfeiture. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#338" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d, at 338</a></span>.</p>
<p id="b371-6">Judge Wallace concurred in the result. He viewed respondent’s currency as an instrumentality of the crime because “without the currency, there can be no offense,” <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#339" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>id., </em>at 339</a></span>, and he criticized the majority for “striking] down a portion of” the statute, <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#338" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>id., </em>at 338</a></span>. He nonetheless agreed that full forfeiture would violate the Excessive Fines Clause in respondent’s case, based upon the “proportionality” prong of the Ninth Circuit test. Finding no clear error in the District Court’s factual findings, he concluded that the reduced forfeiture of $15,000 was proportional to respondent’s culpability. <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#339" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe..."><em>Id., </em>at 339-340</a></span>.</p>
<p id="b371-7">Because the Court of Appeals’ holding — that the forfeiture ordered by § 982(a)(1) was <em>per se </em>unconstitutional in cases of currency forfeiture — invalidated a portion of an Act of Congress, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./520/1239/">520 U. S. 1239</a></span> (1997).</p>
<p id="b371-8">hH h-4</p>
<p id="b371-3">The Eighth Amendment provides: “Excessive hail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.” U. S. Const., Arndt. 8. This Court has had little occasion to interpret, and has never actually applied, the Excessive Fines Clause. We have, however, explained that at the time the Constitution was adopted, “the word ‘fine’ was understood to mean a payment to a sovereign as punishment for some offense.” <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, </em><page-number citation-index="1" label="328">*328</page-number><em>Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#265" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S. 257, 265</a></span> (1989). The Excessive Fines Clause thus “limits the government’s power to extract payments, whether in cash or in kind, ‘as punishment for some offense.’ ” <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#609" aria-description="Citation for case: Austin v. United States">509 U. S. 602, 609-610</a></span> (1998) (emphasis deleted). Forfeitures — payments in kind— are thus “fines” if they constitute punishment for an offense.</p>
<p id="b372-5">We have little trouble concluding that the forfeiture of currency ordered by § 982(a)(1) constitutes punishment. The statute directs a court to order forfeiture as an additional sanction when “imposing sentence on a person convicted of” a willful violation of §5316’s reporting requirement. The forfeiture is thus imposed at the culmination of a criminal proceeding and requires conviction of an underlying felony, and it cannot be imposed upon an innocent owner of unreported currency, but only upon a person who has himself been convicted of a §5316 reporting violation.<footnotemark>3</footnotemark> Cf. <em>id., </em>at 619 (holding forfeiture to be a “fine” in part because the forfeiture statute “expressly provide[d] an ‘innocent owner’ defense” and thus “look[ed] . .. like punishment”).</p>
<p id="b373-4"><page-number citation-index="1" label="329">*329</page-number>The United States argues, however, that the forfeiture of currency under § 982(a)(1) “also serves important remedial purposes.” Brief for United States 20. The Government asserts that it has “an overriding sovereign interest in controlling what property leaves and enters the country.” <em>Ibid. </em>It claims that full forfeiture of unreported currency supports that interest by serving to “dete[r] illicit movements of cash” and aiding in providing the Government with “valuable information to investigate and detect criminal activities associated with that cash.” <em>Id., </em>at 21. Deterrence, however, has traditionally been viewed as a goal of punishment, and forfeiture of the currency here does not serve the remedial purpose of compensating the Government for a loss. See Black’s Law Dictionary 1293 (6th ed. 1990) (“[R]emedial action” is one “brought to obtain compensation or indemnity”); <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232</a></span> (1972) <em>(per curiam) </em>(monetary penalty provides “a reasonable form of liquidated damages,” <span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States"><em>id., </em>at 237</a></span>, to the Government and is thus a “remedial” sanction because it compensates Government for lost revenues). Although the Government has asserted a loss of information regarding the amount of currency leaving the country, that loss would not be remedied by the Government’s confiscation of respondent’s $357,144.<footnotemark>4</footnotemark></p>
<p id="b373-5">The United States also argues that the forfeiture mandated by § 982(a)(1) is constitutional because it falls within a class of historic forfeitures of property tainted by crime. See Brief for United States 16 (citing, <em>inter alia, The Pal</em><page-number citation-index="1" label="330">*330</page-number><em>myra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#13" aria-description="Citation for case: The Palmyra">12 Wheat. 1, 13</a></span> (1827) (forfeiture of ship); <em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#400" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395, 400-401</a></span> (1878) (forfeiture of distillery)). In so doing, the Government relies upon a series of cases involving traditional civil <em>in rem </em>forfeitures that are inapposite because such forfeitures were historically considered nonpunitive.</p>
<p id="b374-5">The theory behind such forfeitures was the fiction that the action was directed against “guilty property,” rather than against the offender himself.<footnotemark>5</footnotemark> See, <em>e. g., Various Items of Personal Property </em>v. <em>United States, </em><span class="citation" data-id="101673"><a href="/opinion/101673/various-items-of-personal-property-v-united-states/#581" aria-description="Citation for case: Various Items of Personal Property v. United States">282 U. S. 577, 581</a></span> (1931) (“[I]t is the property which is proceeded against, and, by resort to a legal fiction, held guilty and condemned as though it were conscious instead of inanimate and insentient”); see also R. Waples, Proceedings In Rem 13, 205-209 (1882). Historically, the conduct of the property owner was irrelevant; indeed, the owner of forfeited property could be entirely innocent of any crime. See, <em>e. g., Origet </em>v. <em>United States, </em><span class="citation" data-id="92190"><a href="/opinion/92190/origet-v-united-states/#246" aria-description="Citation for case: Origet v. United States">125 U. S. 240, 246</a></span> (1888) (“[T]he merchandise is to be forfeited irrespective of any criminal prosecution. . . . The person punished for the offence may be an entirely different person from the owner of the merchandise, or any person interested in it. The forfeiture of the goods of the principal can form no part of the personal punishment of his agent”). As Justice Story explained:</p>
<blockquote id="b374-6">“The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing; and this, whether the offence be <em>malum prohibitum, </em>or <page-number citation-index="1" label="331">*331</page-number><em>malum, in se. . . . </em>[T]he practice has been, and so this Court understand the law to be, that the proceeding <em>in rem </em>stands independent of, and wholly unaffected by any criminal proceeding <em>in personam” The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra">12 Wheat., at 14-15</a></span>.</blockquote>
<p id="b375-5">Traditional <em>in rem </em>forfeitures were thus not considered punishment against the individual for an offense. See <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra"><em>id., </em>at 14</a></span>; <em>Dobbins’s Distillery </em>v. <em>United States, supra, </em>at 401; <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas">272 U. S. 465, 467-468</a></span> (1926); <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663, 683-684</a></span> (1974); <em>Taylor </em>v. <em>United States, </em><span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#210" aria-description="Citation for case: Taylor v. United States">3 How. 197, 210</a></span> (1845) (opinion of Story, J.) (laws providing for <em>in rem </em>forfeiture of goods imported in violation of customs laws, although in one sense “imposing a penalty or forfeiture[,] . . . truly deserve to be called, remedial”); see also <em>United States </em>v. <em>Ursery, </em><span class="citation" data-id="9433350"><a href="/opinion/118052/united-states-v-ursery/#293" aria-description="Citation for case: United States v. Ursery">518 U. S. 267, 293</a></span> (1996) (Kennedy, J., concurring) (“[Cjivil <em>in rem </em>forfeiture is not punishment of the wrongdoer for his criminal offense”). Because they were viewed as nonpunitive, such forfeitures traditionally were considered to occupy a place outside the domain of the Excessive Fines Clause. Recognizing the nonpunitive character of such proceedings, we have held that the Double Jeopardy Clause does not bar the institution of a civil, <em>in rem </em>forfeiture action after the criminal conviction of the defendant. See <span class="citation" data-id="9433350"><a href="/opinion/118052/united-states-v-ursery/#278" aria-description="Citation for case: United States v. Ursery"><em>id., </em>at 278</a></span>.<footnotemark>6</footnotemark></p>
<p id="b375-6">The forfeiture in this case does not bear any of the hallmarks of traditional civil <em>in rem </em>forfeitures. The Govern<page-number citation-index="1" label="332">*332</page-number>ment has not proceeded against the currency itself, but has instead sought and obtained a criminal conviction of respondent personally. The forfeiture serves no remedial purpose, is designed to punish the offender, and cannot be imposed upon innocent owners.</p>
<p id="b376-5">Section 982(a)(1) thus descends not from historic <em>in rem </em>forfeitures of guilty property, but from a different historical tradition: that of <em>in personam, </em>criminal forfeitures. Such forfeitures have historically been treated as punitive, being part of the punishment imposed for felonies and treason in the Middle Ages and at common law. See W. McKeehnie, Magna Carta 337-339 (2d ed. 1958); 2 F. Pollock &amp; F. Mait-land, The History of English Law 460-466 (2d ed. 1909). Although <em>in personam </em>criminal forfeitures were well established in England at the time of the founding, they were rejected altogether in the laws of this country until very recently.<footnotemark>7</footnotemark></p>
<p id="b377-4"><page-number citation-index="1" label="333">*333</page-number>The Government specifically contends that the forfeiture of respondent’s currency is constitutional because it involves an “instrumentality” of respondent’s crime.<footnotemark>8</footnotemark> According to the Government, the unreported cash is an instrumentality because it “does not merely facilitate a violation of law,” but is “ ‘the very <em>sine qua non </em>of the crime.’ ” Brief for United States 20 (quoting <em>United States </em>v. <em>United States Currency in the Amount of One Hundred Forty-Five Thousand, One Hundred Thirty-Nine Dollars, </em><span class="citation" data-id="6929952"><a href="/opinion/7028172/united-states-v-united-states-currency-in-the-amount-of-one-hundred/#75" aria-description="Citation for case: United States v. United States Currency in the Amount of...">18 F. 3d 73, 75</a></span> (CA2), cert. denied <em>sub nom. Etim </em>v. <em>United States, </em><span class="citation" data-id="9138302"><a href="/opinion/9143616/etim-v-united-states/" aria-description="Citation for case: Etim v. United States">513 U. S. 815</a></span> (1994)). The Government reasons that “there would be no violation at all without the exportation (or attempted exportation) of the cash.” Brief for United States 20.</p>
<p id="b377-5">Acceptance of the Government’s argument would require us to expand the traditional understanding of instrumentality forfeitures. This we decline to do. Instrumentalities historically have been treated as a form of “guilty property” that can be forfeited in civil <em>in rem </em>proceedings. In this ease, however, the Government has sought to punish respondent by proceeding against him criminally, <em>in personam, </em>rather than proceeding <em>in rem </em>against the currency. It is therefore irrelevant whether respondent’s currency is an instrumentality; the forfeiture is punitive, and the test for <page-number citation-index="1" label="334">*334</page-number>the excessiveness of a punitive forfeiture involves solely a proportionality determination. See <em>infra </em>this page and 335-337.<footnotemark>9</footnotemark></p>
<p id="b378-5">Ill</p>
<p id="b378-6">Because the forfeiture of respondent’s currency constitutes punishment and is thus a “fine” within the meaning of the Excessive Fines Clause, we now turn to the question whether it is “excessive.”</p>
<p id="b378-7">A</p>
<p id="b378-8">The touchstone of the constitutional inquiry under the Excessive Fines Clause is the principle of proportionality: The amount of the forfeiture must bear some relationship to the gravity of the offense that it is designed to punish. See <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#622" aria-description="Citation for case: Austin v. United States">509 U. S., at 622-623</a></span> (noting Court of Appeals’ statement that “ ‘the government is exacting too high a penalty in relation to the offense committed’ ”); <em>Alexander </em>v. <em>United States, </em><span class="citation" data-id="9432887"><a href="/opinion/112902/alexander-v-united-states/#559" aria-description="Citation for case: Alexander v. United States">509 U. S. 544, 559</a></span> (1993) (“It is in the light of the extensive criminal activities which petitioner apparently conducted ... that the question whether the forfeiture was ‘excessive’ must be considered”). Until today, however, we have not articulated a standard for determining whether a punitive forfeiture is constitutionally excessive. We now hold that a punitive forfeiture violates the Excessive Fines Clause if it is grossly disproportional to the gravity of a defendant’s offense.</p>
<p id="b379-4"><page-number citation-index="1" label="335">*335</page-number>The text and history of the Excessive Fines Clause demonstrate the centrality of proportionality to the excessiveness inquiry; nonetheless, they provide little guidance as to how disproportional a punitive forfeiture must be to the gravity of an offense in order to be “excessive.” Excessive means surpassing the usual, the proper, or a normal measure of proportion. See 1 N. Webster, American Dictionary of the English Language (1828) (defining excessive as “beyond the common measure or proportion”); S. Johnson, A Dictionary of the English Language 680 (4th ed. 1778) (“[bjeyond the common proportion”). The constitutional question that we address, however, is just how proportional to a criminal offense a fine must be, and the text of the Excessive Fines Clause does not answer it.</p>
<p id="b379-5">Nor does its history. The Clause was little discussed in the First Congress and the debates over the ratification of the Bill of Rights. As we have previously noted, the Clause was taken verbatim from the English Bill of Rights of 1689. See <em>Browning-Ferris Industries of Vt., Inc. </em>v. <em>Kelco Disposal, Inc., </em><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#266" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U. S., at 266-267</a></span>. That document’s prohibition against excessive fines was a reaction to the abuses of the Ring’s judges during the reigns of the Stuarts, <span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/#267" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco..."><em>id., </em>at 267</a></span>, but the fines that those judges imposed were described contemporaneously only in the most general terms. See <em>Earl of Devonshire’s Case, </em>11 State Tr. 1367, 1372 (H. L. 1689) (fine of £30,000 “excessive and exorbitant, against Magna Charta, the common right of the subject, and the law of the land”). Similarly, Magna Charta — which the Stuart judges were accused of subverting — required only that amercements (the medieval predecessors of fines) should be proportioned to the offense and that they should not deprive a wrongdoer of his livelihood:</p>
<blockquote id="b379-6">“A Free-man shall not be amerced for a small fault, but after the manner of the fault; and for a great fault after the greatness thereof, saving to him his contenement; (2) and a Merchant likewise, saving to him his <page-number citation-index="1" label="336">*336</page-number>merchandise; (3) and any other’s villain than ours shall be likewise amerced, saving his wainage.” Magna Charta, 9 Hen. Ill, ch. 14 (1225), 1 Stat. at Large 6-7 (1762 ed.).</blockquote>
<p id="b380-5">None of these sources suggests how disproportional to the gravity of an offense a fine must be in order to be deemed constitutionally excessive.</p>
<p id="b380-6">We must therefore rely on other considerations in deriving a constitutional exeessiveness standard, and there are two that we find particularly relevant. The first, which we have emphasized in our cases interpreting the Cruel and Unusual Punishments Clause, is that judgments about the appropriate punishment for an offense belong in the first instance to the legislature. See, <em>e. g., Solem </em>v. <em>Helm, </em><span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#290" aria-description="Citation for case: Solem v. Helm">463 U. S. 277, 290</a></span> (1983) (“Reviewing courts . . . should grant substantial deference to the broad authority that legislatures necessarily possess in determining the types and limits of punishments for crimes”); see also <em>Gore </em>v. <em>United States, </em><span class="citation" data-id="9421677"><a href="/opinion/105742/gore-v-united-states/#393" aria-description="Citation for case: Gore v. United States">357 U. S. 386, 393</a></span> (1958) (“Whatever views may be entertained regarding severity of punishment,... these are peculiarly questions of legislative policy”). The second is that any judicial determination regarding the gravity of a particular criminal offense will be inherently imprecise. Both of these principles counsel against requiring strict proportionality between the amount of a punitive forfeiture and the gravity of a criminal offense, and we therefore adopt the standard of gross dispro-portionality articulated in our Cruel and Unusual Punishments Clause precedents. See, <em>e. g., Solem </em>v. <span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#288" aria-description="Citation for case: Solem v. Helm"><em>Helm, supra, </em>at 288</a></span>; <em>Rummel </em>v. <em>Estelle, </em><span class="citation" data-id="9427823"><a href="/opinion/110223/rummel-v-estelle/#271" aria-description="Citation for case: Rummel v. Estelle">445 U. S. 263, 271</a></span> (1980).</p>
<p id="b380-7">In applying this standard, the district courts in the first instance, and the courts of appeals, reviewing the proportionality determination <em>de </em>novo,<footnotemark>10</footnotemark> must compare the amount <page-number citation-index="1" label="337">*337</page-number>of the forfeiture to the gravity of the defendant’s offense. If the amount of the forfeiture is grossly disproportional to the gravity of the defendant’s offense, it is unconstitutional.</p>
<p id="b381-5">B</p>
<p id="b381-6">Under this standard, the forfeiture of respondent’s entire $357,144 would violate the Excessive Pines Clause.<footnotemark>11</footnotemark> Respondent’s crime was solely a reporting offense. It was permissible to transport the currency out of the country so long as he reported it. Section 982(a)(1) orders currency to be forfeited for a “willful” violation of the reporting requirement. Thus, the essence of respondent’s crime is a willful failure to report the removal of currency from the United States.<footnotemark>12</footnotemark> Furthermore, as the District Court found, re<page-number citation-index="1" label="338">*338</page-number>spondent’s violation was unrelated to any other illegal activities. The money was the proceeds of legal activity and was to be used to repay a lawful debt. Whatever his other vices, respondent does not fit into the class of persons for whom the statute was principally designed: He is not a money launderer, a drug trafficker, or a tax evader.<footnotemark>13</footnotemark> See Brief for United States 2-3. And under the Sentencing Guidelines, the maximum sentence that could have been imposed on respondent was six months, while the maximum fine was $5,000. App. to Pet. for Cert. 17a (transcript of District Court sentencing hearing); United States Sentencing Commission, Guidelines Manual §5(e)1.2, Sentencing Table <page-number citation-index="1" label="339">*339</page-number>(Nov. 1994). Such penalties confirm a minimal level of culpability.<footnotemark>14</footnotemark></p>
<p id="b383-5">The harm that respondent caused was also minimal. Failure to report his currency affected only one party, the Government, and in a relatively minor way. There was no fraud on the United States, and respondent caused no loss to the public fisc. Had his crime gone undetected, the Government would have been deprived only of the information that $357,144 had left the country. The Government and the dissent contend that there is a correlation between the amount forfeited and the harm that the Government would have suffered had the crime gone undetected. See Brief for United States 30 (forfeiture is “perfectly calibrated”); <em>post, </em>at 344 (“a fine calibrated with this accuracy”). We disagree. There is no inherent proportionality in such a forfeiture. It is impossible to conclude, for example, that the harm respondent caused is anywhere near 30 times greater than that caused by a hypothetical drug dealer who willfully fails to report taking $12,000 out of the country in order to purchase drugs.</p>
<p id="b383-6">Comparing the gravity of respondent’s crime with the $357,144 forfeiture the Government seeks, we conclude that such a forfeiture would be grossly disproportional to the <page-number citation-index="1" label="340">*340</page-number>gravity of his offense.<footnotemark>15</footnotemark> It is larger than the $5,000 fine imposed by the District Court by many orders of magnitude, and it bears no articulable correlation to any injury suffered by the Government.</p>
<p id="b384-5">C</p>
<p id="b384-6">Finally, we must reject the contention that the proportionality of full forfeiture is demonstrated by the fact that the First Congress enacted statutes requiring full forfeiture of goods involved in customs offenses or the payment of monetary penalties proportioned to the goods’ value. It is argued that the enactment of these statutes at roughly the same time that the Eighth Amendment was ratified suggests that full forfeiture, in the customs context at least, is a proportional punishment. The early customs statutes, however, do not support such a conclusion because, unlike § 982(a)(1), the type of forfeiture that they imposed was not considered punishment for a criminal offense.</p>
<p id="b384-7">Certain of the early customs statutes required the forfeiture of goods imported in violation of the customs laws, and, in some instances, the vessels carrying them as well. See, <em>e. g., </em>Act of Aug. 4, 1790, § 27, <span class="citation no-link">1 Stat. 163</span> (goods unladen without a permit from the collector). These forfeitures, however, were civil <em>in rent, </em>forfeitures, in which the Government proceeded against the property itself on the theory that it was guilty, not against a criminal defendant. See, <em>e. g., Harford </em>v. <em>United States, </em><span class="citation" data-id="85061"><a href="/opinion/85061/harford-v-united-states/" aria-description="Citation for case: Harford v. United States">8 Cranch 109</a></span> (1814) (goods unladen without a permit); <em>Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#340" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 340</a></span> (1813) (same). Such forfeitures sought to vindicate the Government’s underlying property right in customs duties, and like other traditional <em>in rem </em>forfeitures, they were not considered at the founding to be punishment for an offense. See <em>supra, </em>at 330-331. They therefore indicate <page-number citation-index="1" label="341">*341</page-number>nothing about the proportionality of the punitive forfeiture at issue here. See <em>supra, </em>at 330-332.<footnotemark>16</footnotemark></p>
<p id="b385-5">Other statutes, however, imposed monetary "forfeitures” proportioned to the value of the goods involved. See, <em>e, g., </em>Act of July 31, 1789, §22, <span class="citation no-link">1 Stat. 42</span> (if an importer, “with design to defraud the revenue,” did not invoice his goods at their actual cost at the place of export, “all such goods, wares or merchandise, or the value thereof... shall be forfeited”); §25, <em>id., </em>at 43 (any person concealing or purchasing goods, knowing they were liable to seizure for violation of the customs laws, was liable to “forfeit and pay a sum double the value of the goods so concealed or purchased”); see also Act of Aug. 4, 1790, §§10, 14, 22, <em>id., </em>at 156, 158, 161. Similar statutes were passed in later Congresses. See, <em>e. g., </em>Act of Mar. 2,1799, §§24, 28, 45, 46, 66, 69, 79, 84, <em>id., </em>at 646, 648, 661, 662, 677, 678, 687, 694; Act of Mar. 3,1823, ch. 58, §1, <span class="citation no-link">3 Stat. 781</span>.</p>
<p id="b385-6">These “forfeitures” were similarly not considered punishments for criminal offenses. This Court so recognized in <em>Stockwell </em>v. <em>United States, </em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">13 Wall. 531</a></span> (1871), a ease interpreting a statute that, like the Act of July 31,1789, provided that a person who had concealed goods liable to seizure for customs violations should “forfeit and pay a sum double the amount or value of the goods.” Act of Mar. 3, 1823, eh. 58, §2, <span class="citation no-link">3 Stat. 781</span>-782. The <em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">Stockwell</a></span> </em>Court rejected the de<page-number citation-index="1" label="342">*342</page-number>fendant’s contention that this provision was “penal,” stating instead that it was “fully as remedial in its character, designed as plainly to secure [the] rights [of the Government], as are the statutes rendering importers liable to duties.” <span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#546" aria-description="Citation for case: Stockwell v. United States">13 Wall., at 546</a></span>. The Court reasoned:</p>
<blockquote id="b386-5">“When foreign merchandise, subject to duties, is imported into the country, the act of importation imposes on the importer the obligation to pay the legal charges. Besides this the goods themselves, if the duties be not paid, are subject to seizure .... Every act, therefore, which interferes with the right of the government to seize and appropriate the property which has been forfeited to it... is a wrong to property rights, and is a fit subject for indemnity.” <em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/" aria-description="Citation for case: Stockwell v. United States">Ibid.</a></span></em></blockquote>
<p id="b386-6">Significantly, the fact that the forfeiture was a multiple of the value of the goods did not alter the Court’s conclusion:</p>
<blockquote id="b386-7">“The act of abstracting goods illegally imported, receiving, concealing, or buying them, interposes difficulties in the way of a government seizure, and impairs, therefore, the value of the government right. It is, then, hardly accurate to say that the only loss the government can sustain from concealing the goods liable to seizure is their single value.... Double the value may not be more than complete indemnity.” <span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#546" aria-description="Citation for case: Stockwell v. United States"><em>Id., </em>at 546-547</a></span>.</blockquote>
<p id="b386-8">The early monetary forfeitures, therefore, were considered not as punishment for an offense, but rather as serving the remedial purpose of reimbursing the Government for the losses accruing from the evasion of customs duties.<footnotemark>17</footnotemark> They <page-number citation-index="1" label="343">*343</page-number>were thus no different in purpose and effect than the <em>in rem </em>forfeitures of the goods to whose value they were proportioned.<footnotemark>18</footnotemark> Cf. <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S., at 237</a></span> (customs statute requiring the forfeiture of undeclared goods concealed in baggage and imposing a monetary penalty equal to the value of the goods imposed a “remedial, rather than [a] punitive sanctio[n]”).<footnotemark>19</footnotemark> By contrast, <page-number citation-index="1" label="344">*344</page-number>the full forfeiture mandated by § 982(a)(1) in this case serves no remedial purpose; it is clearly punishment. The customs statutes enacted by the First Congress, therefore, in no way suggest that § 982(a)(l)’s currency forfeiture is constitutionally proportional.</p>
<p id="b388-8">* * *</p>
<p id="b388-9">For the foregoing reasons, the full forfeiture of respondent’s currency would violate the Excessive Fines Clause. The judgment of the Court of Appeals is</p>
<p id="b388-10">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b369-8"> The statutory reporting requirement provides:</p>
<p id="b369-9">“[A] person or an agent or bailee of the person shall file a report... when the person, agent, or bailee knowingly—</p>
<p id="b369-10">“(1) transports, is about to transport, or has transported, monetary instruments of more than $10,000 at one time—</p>
<p id="b369-11">“(A) from a place in the United States to or through a place outside the United States ....” <span class="citation no-link">31 U. S. C. § 5316</span>(a).</p>
</footnote>
<footnote label="2">
<p id="b369-12"> Section 5322(a) provides: “A person willfully violating this subchapter ... shall be fined not more than $250,000, or imprisoned for not more than five years, or both.”</p>
</footnote>
<footnote label="3">
<p id="b372-6"> Although the currency reporting statute provides that “a person or an agent or bailee of the person shall file a report,” <span class="citation no-link">31 U. S. C. § 5316</span>(a), the statute ordering the criminal forfeiture of unreported currency provides that “[t]he court, in imposing sentence on a person convicted of” failure to file the required report, “shall order that the person forfeit to the United States” any property “involved in” or “traceable to” the offense, 18 U. S. G. § 982(a)(1). The combined effect of these two statutes is that an owner of unreported currency is not subject to criminal forfeiture if his agent or bailee is the one who fails to file the required report, because such an owner could not be convicted of the reporting offense. The United States endorsed this interpretation at oral argument in tins case. See Tr. of Oral Arg. 24-25.</p>
<p id="b372-7">For this reason, the dissent's speculation about the effect of today’s holding on “kingpins” and “cash couriers” is misplaced. See <em>post, </em>at 352, 354. Section 982(a)(l)’s criminal <em>in personam </em>forfeiture reaches only currency owned by someone who himself commits a reporting crime. It is unlikely that the Government, in the course of criminally indicting and prosecuting a cash courier, would not bother to investigate the source and true ownership of unreported funds.</p>
</footnote>
<footnote label="4">
<p id="b373-6"><em> </em>We do not suggest that merely because the forfeiture of respondent’s currency in this case would not serve a remedial purpose, other forfeitures may be classified as lionpunitive (and thus not “fines”) if they serve some remedial purpose as well as being punishment for an offense. Even if the Government were correct in claiming that the forfeiture of respondent’s currency is remedial in some way, the forfeiture would still be punitive in part. (The Government concedes ás much.) This is sufficient to bring the forfeiture within the purview of the Excessive Fines Glause. See <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#621" aria-description="Citation for case: Austin v. United States">509 U. S. 602, 621-622</a></span> (1993).</p>
</footnote>
<footnote label="5">
<p id="b374-7"> The “guilty property” theory behind <em>in rem </em>forfeiture can be traced to the Bible, which describes property being sacrificed to God as a means of atoning for an offense. See Exodus 21:28. In medieval Europe and at common law, this concept evolved into the law of deodand, in which offending property was condemned and confiscated by the church or the Crown in remediation for the harm it had caused. See 1 M. Hale, Pleas of the Crown 420-424 (1st Am. ed. 1847); 1 W. Blackstone, Commentaries on the Laws of England 290-292 (1765); O. Holmes, The Common Law 10-13, 23-27 (M. Howe ed. 1963).</p>
</footnote>
<footnote label="6">
<p id="b375-7"> It does not follow, of course, that all modem civil <em>in rem </em>forfeitures are nonpunitive and thus beyond the coverage of the Excessive Fines Clause. Because some recent federal forfeiture laws have blurred the traditional distinction between civil <em>in rem </em>and criminal <em>in -personam </em>forfeiture, we have held that a modern statutory forfeiture is a “fine” for Eighth Amendment purposes if it constitutes punishment even in part, regardless of whether the proceeding is styled <em>in rem </em>or <em>in personam. </em>See <em>Austin </em>v. <em>United States, supra, </em>at 621-622 (although labeled <em>in rem, </em>civil forfeiture of real property used “to facilitate” the commission of drug crimes was punitive in part and thus subject to review under the Excessive Fines Clause).</p>
</footnote>
<footnote label="7">
<p id="b376-6"> The First Congress explicitly rejected <em>in personam </em>forfeitures as punishments for federal crimes, see Act of Apr. 30, 1790, ch. 9, §24, <span class="citation no-link">1 Stat. 117</span> (“[NJo conviction or judgment.. . shall work corruption of blood, or any forfeiture of estate”), and Congress reenacted this ban several times over the course of two centuries. See Rev. Stat. § 5326 (1875); Act of Mar. 4, 1909, ch. 321, §341, <span class="citation no-link">35 Stat. 1159</span>; Act of June 25,1948, ch. 645, §3563, <span class="citation no-link">62 Stat. 837</span>, codified at <span class="citation no-link">18 U. S. C. § 3563</span> (1982 ed.); repealed effective Nov. 1,1987, <span class="citation no-link">Pub. L. 98-473, 98</span> Stat. 1987.</p>
<p id="b376-7">It was only in 1970 that Congress resurrected the English common law of punitive forfeiture to combat organized crime and major drug trafficking. See Organized Crime Control Act of 1970, <span class="citation no-link">18 U. S. C. § 1963</span>, and Comprehensive Drug Abuse Prevention and Control Act of 1970, <span class="citation no-link">21 U. S. C. § 848</span>(a). In providing for this mode of punishment, which had long been unused in this country, the Senate Judiciary Committee acknowledged that “criminal forfeiture... represents an innovative attempt to call on our common law heritage to meet an essentially modern problem.” S. Rep. No. 91-617, p. 79 (1969). Indeed, it was not until 1992 that Congress provided for the criminal forfeiture of currency at issue here. See <span class="citation no-link">18 U.S.C. § 982</span>(a).</p>
</footnote>
<footnote label="8">
<p id="b377-6"> Although the term “instrumentality” is of recent vintage, see <em>Austin </em>v. <em>United States, </em>509 U. S., at 627-628 (Scalia, J., concurring in part and concurring in judgment), it fairly characterizes property that historically was subject to forfeiture because it was the actual means by which an offense was committed. See <em>infra </em>this page; see, <em>e. g., J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#508" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505, 508-510</a></span> (1921). “Instrumentality” forfeitures have historically been limited to the property actually used to commit an offense and no more. See <em>Austin </em>v. <em>United States, supra, </em>at 627-628 (Scalia, J., concurring in part and concurring in judgment). A forfeiture that reaches beyond this strict historical limitation is <em>ipso facto </em>punitive and therefore subject to review under the Excessive Fines Clause.</p>
</footnote>
<footnote label="9">
<p id="b378-9"> The currency in question is not an instrumentality in any event. The Court of Appeals reasoned that the existence of the currency as a “precondition” to the reporting requirement did not make it an “instrumentality” of the offense. See <span class="citation" data-id="9489168"><a href="/opinion/718371/united-states-v-hosep-krikor-bajakajian-aka-joe-bajakajian/#337" aria-description="Citation for case: United States v. Hosep Krikor Bajakajian, Aka: Joe...">84 F. 3d 334, 337</a></span> (CA9 1996). We agree; the currency is merely the subject of the crime of failure to report. Cash in a suitcase does not facilitate the commission of that crime as, for example, an automobile facilitates the transportation of goods concealed to avoid taxes. See, <em>e. g., J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, supra, </em>at 508. In the latter instance, the property is the actual means by which the criminal act is committed. See Black’s Law Dictionary 801 (6th ed. 1990) (“Instrumentality” is “[slomething by which an end is achieved; a means, medium, agency”).</p>
</footnote>
<footnote label="10">
<p id="b380-8"> At oral argument, respondent urged that a district court’s determination of excessiveness should be reviewed by an appellate court for abuse of discretion. See Tr. of Oral Arg. 32. We cannot accept this submission. The factual findings made by the district courts in conducting the exces-<page-number citation-index="1" label="337">*337</page-number>siveness inquiry, of course, must be accepted unless dearly erroneous. See <em>Anderson </em>v. <em>Bessemer City, </em><span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#574" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U. S. 564, 574-575</a></span> (1985). But the question whether a fine is constitutionally excessive calls for the application of a constitutional standard to the facts of a particular ease, and in this context <em>de novo </em>review of that question is appropriate. See <em>Ornelas </em>v. <em>United States, </em><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/#697" aria-description="Citation for case: Ornelas v. United States">517 U. S. 690, 697</a></span> (1996).</p>
</footnote>
<footnote label="11">
<p id="b381-8"> The only question before this Court is whether the full forfeiture of respondent’s $357,144 as directed by § 982(a)(1) is constitutional under the Excessive Fines Clause. We hold that it is not. The Government petitioned for certiorari seeking full forfeiture, and we reject that request. Our holding that full forfeiture would be excessive reflects no judgment that "a forfeiture of even $15,001 would have suffered from a gross disproportion,” nor does it “affir[m] the reduced $15,000 forfeiture on <em>de novo </em>review.” <em>Post, </em>at 349. Those issues are simply not before us. Nor, indeed, do we address in <em>any </em>respect the validity of the forfeiture ordered by the District Court, including whether a court may disregard the terms of a statute that commands full forfeiture: As noted, <em>supra, </em>at 327, respondent did not cross-appeal the $15,000 forfeiture ordered by the District Court. The Court of Appeals thus declined to address the $15,000 forfeiture, and that question is not properly presented here either.</p>
</footnote>
<footnote label="12">
<p id="b381-9"> Contrary to the dissent’s contention, the nature of the nonreporting offense in this case was not altered by respondent’s “lies” or by the “suspicious circumstances” surrounding his transportation of his currency. See <em>post, </em>at 352-353. A single willful failure to declare the currency constitutes the crime, the gravity of which is not exacerbated or mitigated by <page-number citation-index="1" label="338">*338</page-number>‘Tablets]” that respondent told one month, or six months, later. See <em>post, </em>at 352. The Government indicted respondent under <span class="citation no-link">18 U. S. C. § 1001</span> for “lying,” but that separate count did not form the basis of the nonreporting offense for which § 982(a)(1) orders forfeiture.</p>
<p id="AQCi">Further, the District Court’s finding that respondent’s lies stemmed from a fear of the Government because of “cultural differences,” <em>supra, </em>at 326, does not mitigate the gravity of his offense. We reject the dissent’s contention that this finding was a “patronizing excuse” that “demeans millions of law-abiding American immigrants by suggesting they cannot be expected to be as truthful as every other citizen.” <em>Post, </em>at 353. We are confident that the District Court concurred in the dissent’s incontrovertible proposition that “[e]ach American, regardless of culture or ethnicity, is equal before the law.” <em>Ibid. </em>The District Court did nothing whatsoever to imply that “cultural differences” excuse lying, but rather made this finding in the context of establishing that respondent’s willful failure to report the currency was unrelated to any other crime — a finding highly relevant to the determination of the gravity of respondent’s offense. The dissent’s charge of ethnic paternalism on the part of the District Court finds no support in the record, nor is there any indication that the District Court’s factual finding that respondent “distrust[ed]... the Government,” see <em>supra, </em>at 326, was clearly erroneous.</p>
</footnote>
<footnote label="13">
<p id="b382-7"> Nor, contrary to the dissent’s repeated assertion, see <em>post, </em>at 344,346-351,354,356, is respondent a “smuggl[er].” Respondent owed no customs duties to the Government, and it was perfectly legal for him to possess the $357,144 in cash and to remove it from the United States. His crime was simply failing to report the wholly legal act of transporting his currency.</p>
</footnote>
<footnote label="14">
<p id="b383-7"> In considering an offense’s gravity, the other penalties that the Legislature has authorised are certainly relevant evidence. Here, as the Government and the dissent stress, Congress authorized a maximum fine of $250,000 plus five years’ imprisonment for willfully violating the statutory reporting requirement, and this suggests that it did not view the reporting offense as a trivial one. That the maximum fine and Guideline sentence to which respondent was subject were but a fraction of the penalties authorized, however, undercuts any argument based solely on the statute, because they show that respondent's culpability relative to other potential violators of the reporting provision — tax evaders, drug kingpins, or money launderers, for example — is small indeed. This disproportion is telling notwithstanding the fact that a separate Guideline provision permits forfeiture if mandated by statute, see <em>post, </em>at 350-351. That Guideline, moreover, cannot override the constitutional requirement of proportionality review.</p>
</footnote>
<footnote label="15">
<p id="b384-8"> Respondent does not argue that his wealth or income are relevant to the proportionality determination or that full forfeiture would deprive him of his livelihood, see <em>supra, </em>at 335-336, and -the District Court made no factual findings in this respect.</p>
</footnote>
<footnote label="16">
<p id="b385-7"> The nonpumtive nature of these early forfeitures was not lost on the Department of Justice, in commenting on the punitive forfeiture provisions of the Organized Crime Control Act of 1970:</p>
<p id="b385-8">‘“The concept of forfeiture as a criminal penalty which is embodied in this provision differs from other presently existing forfeiture provisions under Federal statutes where the proceeding is <em>in rem </em>against the property and the thing which is declared unlawful under the statute, or which is used for an unlawful purpose, or in connection with the prohibited property or transaction, is considered the offender, <em>and the forfeiture is no 'part of the punishment for the criminal offense. Examples of such forfeiture provisions are those contained in the customs, narcotics, and revenue laws.’” </em>S. Rep. No. 91-617, p. 79 (1969) (emphasis added).</p>
</footnote>
<footnote label="17">
<p id="b386-9"> In each of the statutes from the early Congresses cited by the dissent, the activities giving' rise to the monetary forfeitures, if undetected, were likely to cause the Government losses in customs revenue. The forfeiture imposed by the Acts of Aug. 4,1790, and Mar. 2,1799, was not simply for "transferring goods from one ship to another,” <em>post, </em>at 346, but rather for doing so “before such ship . . . shall come to the proper place for the discharge of her cargo . . . and be there duly authorized by the proper officer or officers of the customs to unlade” the goods, see <span class="citation no-link">1 Stat. 157</span>, <page-number citation-index="1" label="343">*343</page-number>158, 648, whereupon duties would be assessed. Similarly, the forfeiture imposed by the Act of Mar. 3, 1823, was for failing to deliver the ship’s manifest of cargo — which was to list “merchandise subject to duty” — to the collector of customs. See Act of Mar. 2,1821, §1, <span class="citation no-link">3 Stat. 616</span>; Act of Mar. 3,1823, §1, <em>id., </em>at 781. And the “invoices” that if “false” gave rise to the forfeiture imposed by the Act of Mar. 3,1863, were to include the value or quantity of any dutiable goods. § 1,<span class="citation no-link">12 Stat. 737</span>-738.</p>
</footnote>
<footnote label="18">
<p id="b387-6"> The nonpunitive nature of the monetary forfeitures was also reflected in their procedure: like traditional <em>in rem, </em>forfeitures, they were brought as civil actions, and as such are distinguishable from the punitive criminal fine at issue here. Instead of instituting an information of libel <em>in rem </em>against the goods, see, <em>e. g., Locke </em>v. <em>United States, </em><span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch 339</a></span> (1813), the Government filed “a civil action of debt” against the person from whom it sought payment. See, <em>e. g., Stockwell </em>v. <em>United States, </em><span class="citation" data-id="9416849"><a href="/opinion/88491/stockwell-v-united-states/#541" aria-description="Citation for case: Stockwell v. United States">13 Wall. 531, 541-542</a></span> (1871). In both England and the United States, an action of debt was used to recover import duties owed the Government, being “the general remedy for the recovery of all sums certain, whether the legal liability arise from contract, or be created by a statute. And the remedy as well lies for the government itself, as for a citizen.” <em>United States </em>v. <em>Lyman, </em><span class="citation" data-id="8639012"><a href="/opinion/8659157/united-states-v-lyman/#1030" aria-description="Citation for case: United States v. Lyman">26 F. Cas. 1024, 1030</a></span> (No. 15,647) (CC Mass. 1818) (Story, C. J.). Thus suits for the payment of monetary forfeitures were viewed no differently than suits for the customs duties themselves.</p>
</footnote>
<footnote label="19">
<p id="b387-7"> <em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">One Lot Emerald Cut Stones</a></span> </em>differs from this case in the most fundamental respect. We concluded that the forfeiture provision in <em>Emerald Cut Stones </em>was entirely remedial and thus nonpunitive, primarily because it “provide[d] a reasonable form of liquidated damages” to the Government. <span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#237" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S., at 237</a></span>. The additional fact that such a remedial forfeiture also “selves to reimburse the Government for investigation and enforcement expenses,” <em>ibid.; </em>see <em>post, </em>at 346, is essentially meaningless, because even a clearly punitive criminal fine or forfeiture could be said in some measure to reimburse for criminal enforcement and investigation. Contrary to the dissent’s assertion, this certainly does not mean that the forfeiture in this case — which, as the dissent acknowledges, see <em>post, </em>at 344 (respondent’s forfeiture is a “fine”); <em>post, </em>at 353 (§ 982(a)(1) imposes a <page-number citation-index="1" label="344">*344</page-number>“punishment”), is dearly punitive — “would have to [be treated) as nonpu-nitive,” <em>post, </em>at 346.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Blue.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Blue
type: case
citation: "384 U.S. 251 (1966)"
parallel_cite: "86 S. Ct. 1416; 16 L. Ed. 2d 510; 17 A.F.T.R.2d (RIA) 1032"
neutral_cite: 1966 U.S. LEXIS 2952
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-05-23
docket: No. 531
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
  opinion_url: "https://www.courtlistener.com/opinion/107238/united-states-v-blue/"
  cluster_id: 107238
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Blue
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Mapp v. Ohio]]"
  - "[[United States v. Calandra]]"
tags:
  - case
  - fifth-amendment
  - exclusionary-rule
  - self-incrimination
  - indictment
  - remedy
holding: "Dismissal of an indictment is not the remedy for the Government's allegedly unconstitutional acquisition of evidence; even assuming the Government obtained incriminating evidence in violation of the Fifth Amendment privilege against self-incrimination, the defendant is entitled at most to suppress that evidence and its fruits if the Government seeks to use them at trial — the exclusionary remedy does not extend to barring the prosecution altogether."
aliases:
  - United States v. Blue
  - "United States v. Blue (1966)"
---

# United States v. Blue

*384 U.S. 251 (1966)* (No. 531) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 107238 → combined opinion 107238 (Harlan, J.; 384 U.S. 251, argued Apr. 18-19, 1966, decided May 23, 1966). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*255`). On-read identity note: the CL opinion text attributes the opinion to Justice Harlan (not the Chief Justice). S9 promotes. -->

## Background
The Internal Revenue Service told Ben Blue he might be prosecuted for tax evasion, then made jeopardy assessments against him, his wife, and his wholly owned corporation, seized their assets, recorded tax liens, and issued statutory deficiency notices giving Blue 90 days to petition the Tax Court. Blue filed Tax Court petitions contesting the deficiencies. More than a year later the Government indicted him for willfully evading income taxes and filing false corporate returns. Blue moved to dismiss the indictment, arguing that the jeopardy-assessment and Tax Court process had compelled him to incriminate himself; the District Court dismissed the indictment on that ground, and the Government appealed directly to the Supreme Court.

## Issue
Whether an indictment must be dismissed because the Government allegedly compelled the defendant to give incriminating evidence in violation of the Fifth Amendment, or whether the defendant's remedy is limited to suppressing that evidence at trial.

## Rule
Assuming without deciding that a Fifth Amendment violation had occurred, the Court held that dismissal was the wrong remedy — the appropriate response to unconstitutionally obtained evidence is exclusion, not immunity from prosecution: "Even if we assume that the Government did acquire incriminating evidence in violation of the Fifth Amendment, Blue would at most be entitled to suppress the evidence and its fruits if they were sought to be used against him at trial." — 384 U.S. at 255. ^pin-255

## Application
The Court explained that its exclusionary-rule precedents implicitly assume the remedy does not extend to barring the prosecution altogether. Ending the prosecution entirely might add a marginal increment to the interests the exclusionary rule serves, but it would exact an intolerable cost by letting a defendant escape trial rather than merely keeping tainted evidence out of it. Blue's protection, if any, lay in suppression motions and evidentiary objections at trial — not in dismissal of the indictment. Because the District Court had dismissed rather than left those remedies for trial, its judgment could not stand.

## Conclusion
The judgment of the District Court was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]], leaving Blue free to pursue his Fifth Amendment claim through motions to suppress and objections to evidence. Harlan, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Blue* is an exclusionary-rule anchor for the *scope of the remedy*: the sanction for an unconstitutional acquisition of evidence is suppression at trial, not dismissal of the indictment or a bar to prosecution. Teach it with the grand-jury and cost-benefit cases — *[[United States v. Calandra]]* and *[[Mapp v. Ohio]]* — as marking the outer boundary of what the exclusionary rule remedies.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*United States v. Blue*, 384 U.S. 251 (1966)](https://www.courtlistener.com/opinion/107238/united-states-v-blue/) — pinpoint: 255 (Harlan, J., for the Court; in the CL opinion text the quoted holding falls between the reporter stars `*255` and `*256`, i.e., on page 255). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f754eb8470925d5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "384 U.S. 251 (1966)", "court": "U.S. Supreme Court", "neutral_cite": "1966 U.S. LEXIS 2952", "official_citation_present": true, "parallel_cite": "86 S. Ct. 1416; 16 L. Ed. 2d 510; 17 A.F.T.R.2d (RIA) 1032", "title": "United States v. Blue", "year": "1966"}}
{"assertion_id": "35480d80c05f0e57", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Dismissal of an indictment is not the remedy for the Government's allegedly unconstitutional acquisition of evidence; even assuming the Government obtained incriminating evidence in violation of the Fifth Amendment privilege against self-incrimination, the defendant is entitled at most to suppress that evidence and its fruits if the Government seeks to use them at trial — the exclusionary remedy does not extend to barring the prosecution altogether.", "title": "United States v. Blue"}}
{"assertion_id": "7bd7ee2954e79cbd", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Anchor", "title": "United States v. Blue"}}
{"assertion_id": "6d7e6a3a6cf7f3d5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Blue"}}
{"assertion_id": "7e53a25bd9f894cd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Blue", "varies_by_point": "false"}}
```

### lake record — United States v. Blue

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Blue",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Blue",
    "case_name_short": "Blue",
    "case_name_full": "United States v. Blue",
    "input_case_name": "United States v. Blue",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-05-23",
    "year": 1966,
    "docket": "No. 531",
    "cluster_id": 107238,
    "lead_opinion_id": 107238,
    "sibling_ids": [],
    "absolute_url": "/opinion/107238/united-states-v-blue/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 251",
      "volume": "384",
      "reporter": "U.S.",
      "page": "251",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1416",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 510",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 A.F.T.R.2d (RIA) 1032",
        "volume": "17",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1032",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2952",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2952",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 251",
        "volume": "384",
        "reporter": "U.S.",
        "page": "251",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1416",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 510",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2952",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2952",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 A.F.T.R.2d (RIA) 1032",
        "volume": "17",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1032",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 251",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 251",
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
    "date_created": "2026-07-06T13:43:06Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-blue--107238",
      "to_record_id": "United States v. Blue",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Blue

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b350-7">
  Mr. Justice Harlan
 </author>
<p id="AEj">
  delivered the opinion of the Court.
 </p>
<p id="b350-8">
  In 1962 the appellee, Ben Blue, was informed by the Internal Revenue Service that he might be criminally prosecuted for violation of the federal income tax laws. The following year the Service made jeopardy assessments against Blue, his wife, and his wholly owned corporation for tax liability for the years 1958 to 1960 inclusive; the known assets of all three were seized and tax liens recorded. Internal Revenue Code of 1954, §§ 6321-6323, 6331, 6861. Statutory notices were then issued giving Blue 90 days within which to file petitions if he wished to contest the proposed deficiencies in the Tax Court, I. R. C. §6213, and Blue filed petitions setting forth his position and alleging errors in the Commissioner’s determination of deficiencies. More than a year later the Government initiated the present criminal case by a six-count indictment charging Blue with wilfully attempting to evade personal income taxes for the years 1958 through 1960 and with filing false returns for his corporation during the same years. I. R. C. §§ 7201, 7206 (1).
 </p>
<p id="b350-9">
  Blue filed a pretrial motion seeking dismissal of the indictment on several grounds. After a hearing the District Court granted the motion. The court stated orally that because of the jeopardy assessment and Tax Court proceeding Blue “has been compelled and will be compelled to come forward on the same matters as are con
  <span citation-index="1" class="star-pagination" label="253"> 
   *253
   </span>
  cerned in this criminal case, to testify against himself . ...”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The Government filed a notice of appeal and the case was docketed in the Court of Appeals for the Ninth Circuit. Determining that the District Court had sustained a “motion in bar, when the defendant has not been put in jeopardy” so that a direct appeal lay to this Court,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  the Court of Appeals certified the case to us, <span class="citation" data-id="268997"><a href="/opinion/268997/united-states-v-ben-blue/" aria-description="Citation for case: United States v. Ben Blue">350 F. 2d 267</a></span>, and we postponed jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./382/971/">382 U. S. 971</a></span>. We agree that this Court has jurisdiction over the appeal and, on the merits, reverse the decision of the District Court.
 </p>
<p id="b351-5">
  Since Blue had not yet been brought to trial and put in jeopardy when dismissal occurred, see
  <em>
   United States
  </em>
  v. Celestine, <span class="citation" data-id="97114"><a href="/opinion/97114/united-states-v-celestine/#283" aria-description="Citation for case: United States v. Celestine">215 U. S. 278, 283</a></span>, our jurisdiction under the statute is secure if the motion sustained by the District Court was a motion in bar. See,
  <em>
   supra,
  </em>
  n. 2. This in
  <span citation-index="1" class="star-pagination" label="254"> 
   *254
   </span>
  turn depends on “the effect of the ruling sought to be reviewed,”
  <em>
   United States
  </em>
  v.
  <em>
   Hark,
  </em>
  <span class="citation" data-id="9419414"><a href="/opinion/103909/united-states-v-hark/#536" aria-description="Citation for case: United States v. Hark">320 U. S. 531, 536</a></span>, and not on how the pleading is styled or on whether it is ultimately sustained on appeal. Like the Court of Appeals, we take the dismissal in this case as a ruling that absent reversal on review future prosecution of Blue on the pending counts is forever barred. While there are slight ambiguities in language, the District Court’s dismissal was grounded in what it found to be past compulsory self-incrimination and in its apparent belief that this mischief could not be undone save by turning back the clock through ending the prosecution.
 </p>
<p id="b352-6">
  Because the dismissal by its own force would “end the cause and exculpate the defendant,”
  <em>
   United States
  </em>
  v.
  <em>
   Hark,
  </em>
  <span class="citation" data-id="9419414"><a href="/opinion/103909/united-states-v-hark/#536" aria-description="Citation for case: United States v. Hark">320 U. S., at 536</a></span>, rather than merely abate the prosecution on account of some normally curable defect, one requisite of a motion in bar is met. Whether it is a further requisite that the motion introduce “new matter” in the fashion of a plea by way of confession and avoidance need not here be decided. See
  <em>
   United States
  </em>
  v.
  <em>
   Mersky,
  </em>
  <span class="citation" data-id="105997"><a href="/opinion/105997/united-states-v-mersky/#441" aria-description="Citation for case: United States v. Mersky">361 U. S. 431, 441, 453</a></span> (separate opinions disagreeing on this point). For in this instance Blue unquestionably relied on new matter in alleging self-incrimination, so the motion qualifies even under the more stringent definition. Thus under either view of a motion in bar taken in
  <em>
   <span class="citation" data-id="105997"><a href="/opinion/105997/united-states-v-mersky/" aria-description="Citation for case: United States v. Mersky">Mersky</a></span>,
  </em>
  this case qualifies for direct review. Our conclusion on the jurisdictional issue is further supported by two analogous decisions of this Court treating claims of
  <em>
   statutory
  </em>
  immunity as pleas in bar which permitted direct appeal.
  <em>
   United States
  </em>
  v.
  <em>
   Hoffman,
  </em>
  <span class="citation" data-id="9420215"><a href="/opinion/104586/united-states-v-hoffman/" aria-description="Citation for case: United States v. Hoffman">335 U. S. 77</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Monia,
  </em>
  <span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/" aria-description="Citation for case: United States v. Monia">317 U. S. 424</a></span>.
 </p>
<p id="b352-7">
  On the merits of the case, we do not believe that the District Court should have dismissed the indictment. The Government has argued that the statements made by Blue in his Tax Court petitions were no more than
  <span citation-index="1" class="star-pagination" label="255"> 
   *255
   </span>
  successive denials of the alleged underpayments and do not constitute incriminating evidence. The Government has also intimated that by merely providing the occasion for the filing of Blue’s petitions in fulfilling its statutory duty to make jeopardy assessments and send deficiency notices, it ought not be regarded as compelling the taxpayer to incriminate himself within the meaning of the Fifth Amendment. There is no need, however, to consider these or other contentions that may point in the same direction.
 </p>
<p id="b353-5">
  Even if we assume that the Government did acquire incriminating evidence in violation of the Fifth Amendment, Blue would at most be entitled to suppress the evidence and its fruits if they were sought to be used against him at trial.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  While the general common-law practice is to admit evidence despite its illegal origins, this Court in a number of areas has recognized or developed exclusionary rules where evidence has been gained in violation of the accused’s rights under the Constitution, federal statutes, or federal rules of procedure.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>;
  <em>
   Rogers
  </em>
  v.
  <em>
   Richmond,
  </em>
  <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>;
  <em>
   Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>;
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>;
  <em>
   Mallory
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span>. Our numerous precedents ordering the exclusion of such illegally obtained evidence assume implicitly that the remedy does not extend to barring the prosecution altogether. So drastic a step might advance marginally some of the ends served by exclusionary rules, but it would also increase to an intolerable degree interference with the public interest in having the guilty brought to book.
 </p>
<p id="b354-3">
<span citation-index="1" class="star-pagination" label="256"> 
   *256
   </span>
  We remand this case to the District Court to proceed on the merits, leaving Blue free to pursue his Fifth Amendment claim through motions to suppress and objections to evidence. It is not entirely clear from Blue’s brief and argument whether he seeks to sustain the dismissal below on other grounds that the District Court did not accept. See,
  <em>
   supra,
  </em>
  n. 1. Putting to one side jurisdictional difficulties this course might encounter under the direct-review statute,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  we believe it is fairer to all to regard no other grounds as presented, thus reserving to Blue the opportunity to articulate them plainly and support them by the record.
 </p>
<p id="b354-4">
<em>
   Reversed and remanded.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b351-6">
   The court stated that it based the dismissal “on that ground alone.” It rejected a claim that the seizure of property and recording of tax liens had prevented Blue from preparing an adequate defense by depleting his resources. It did not expressly consider Blue’s claim that there is an administrative practice of making no assessments in advance of criminal proceedings and that failure to extend the policy to him was a denial of due process.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b351-7">
   <span class="citation no-link">18 U. S. C. §3731</span> (1964 ed.) provides in part:
  </p>
<blockquote id="b351-8">
   “An appeal may be taken by and on behalf of the United States from the district courts direct to the Supreme Court of the United States in all criminal cases in the following instances:
  </blockquote>
<blockquote id="b351-9">
   “From the decision or judgment sustaining a motion in bar, when the defendant has not been put in jeopardy.
  </blockquote>
<blockquote id="b351-10">
   “If an appeal shall be taken pursuant to this section to any court of appeals which, in the opinion of such court, should have been taken directly to the Supreme Court of the United States, such court shall certify the case to the Supreme Court of the United States, which shall thereupon have jurisdiction to hear and determine the case to the same extent as if an appeal had been taken directly to that Court.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b353-6">
   It does not seem to be contended that tainted evidence was presented to the grand jury; but in any event our precedents indicate this would not be a basis for abating the prosecution pending a new indictment, let alone barring it altogether. See
   <em>
    Costello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421237"><a href="/opinion/105355/costello-v-united-states/" aria-description="Citation for case: Costello v. United States">350 U. S. 359</a></span>;
   <em>
    Lawn
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421531"><a href="/opinion/105609/lawn-v-united-states/" aria-description="Citation for case: Lawn v. United States">355 U. S. 339</a></span>; 8 Wigmore, Evidence § 2184a, at 40 (McNaughton rev. 1961).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b354-5">
   See Stern &amp; Gressman, Supreme Court Practice §2-11, at 31-33 (1962); Friedenthal, Government Appeals in Federal Criminal Cases, <span class="citation no-link">12 Stan. L. Rev. 71</span>, 97-100 (1959).
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/United States v. Caceres.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Caceres
type: case
citation: "440 U.S. 741 (1979)"
parallel_cite: "99 S. Ct. 1465; 59 L. Ed. 2d 733"
neutral_cite: 1979 U.S. LEXIS 83
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-04-13
docket: No. 76-1309
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
  opinion_url: "https://www.courtlistener.com/opinion/110049/united-states-v-caceres/"
  cluster_id: 110049
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Caceres
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Stone v. Powell]]"
  - "[[United States v. Calandra]]"
  - "[[United States v. Janis]]"
  - "[[United States v. Leon]]"
tags:
  - case
  - fourth-amendment
  - exclusionary-rule
  - agency-regulations
  - consensual-monitoring
  - deterrence
holding: "Evidence obtained in violation of an executive agency's internal regulations — here, IRS rules requiring prior authorization for consensual electronic monitoring — need not be excluded from a criminal trial where the agent's conduct violated neither the Constitution nor a federal statute; because the exclusionary rule rests on deterring constitutional violations, it lends no support to suppression for a mere regulatory breach, and the Court declined to adopt any rigid rule excluding all evidence obtained through such a violation."
aliases:
  - United States v. Caceres
  - "United States v. Caceres (1979)"
---

# United States v. Caceres

*440 U.S. 741 (1979)* (No. 76-1309) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110049 → combined opinion 110049 (Stevens, J.; 440 U.S. 741, argued Jan. 8-9, 1979, decided Apr. 2, 1979). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*755`). S9 promotes. -->

## Background
While being audited, respondent Caceres offered a bribe to IRS Agent Yee. The IRS monitored and recorded three face-to-face conversations between them using a radio transmitter concealed on Yee. IRS regulations (the IRS Manual) prohibited such "consensual electronic surveillance" unless prior authorization was obtained through several layers of agency and, in some cases, Justice Department approval. Caceres moved to suppress the recordings because the required authorizations had not been properly secured. The District Court suppressed all three; the Ninth Circuit reversed as to the third tape (authorization was adequate) but agreed that the first two, made without proper authorization, had to be excluded. The Government sought review of that exclusion.

## Issue
Whether evidence obtained in violation of an agency's own internal regulations — regulations not required by the Constitution or by statute — must be excluded from the defendant's criminal trial.

## Rule
The Court began from the premise that neither the Constitution nor any Act of Congress required prior approval for consensual monitoring; only the IRS's self-imposed regulations were violated. Because the exclusionary rule exists to deter *constitutional* violations, it had no purchase where no constitutional right was infringed: "In view of our conclusion that none of respondent's constitutional rights has been violated here, either by the actual recording or by the agency violation of its own regulations, our precedents enforcing the exclusionary rule to deter constitutional violations provide no support for the rule's application in this case." — 440 U.S. at 755. ^pin-755

## Application
The Court declined to adopt any rigid rule excluding all evidence obtained through a regulatory violation. Forcing suppression for every departure from an agency's internal rules would take from the Executive its primary responsibility to fashion remedies for its own regulations — and might perversely lead agencies to write fewer or weaker rules, leaving the public *less* protected. Nor did a case-by-case approach favor suppression here, where the violation was neither deliberate nor prejudicial and did not affect any constitutional or statutory right. It was better, the Court reasoned, to have protective regulations like the IRS Manual's and tolerate occasional lapses than to discourage agencies from adopting such rules at all.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed**. Stevens, J., delivered the opinion of the Court. Marshall, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Brennan, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Caceres* anchors an outer limit of the exclusionary rule: suppression is a remedy for constitutional (and some statutory) violations, not for an agency's failure to follow its own internal procedures. It belongs with the deterrence-and-cost line — *[[Stone v. Powell]]*, *[[United States v. Calandra]]*, *[[United States v. Janis]]*, and *[[United States v. Leon]]* — that ties suppression to whether excluding evidence will meaningfully deter the violation of constitutional rights.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*United States v. Caceres*, 440 U.S. 741 (1979)](https://www.courtlistener.com/opinion/110049/united-states-v-caceres/) — pinpoint: 755 (Stevens, J., for the Court; the CL opinion text carries the reporter star `*755` immediately before the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4a333084245b46f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "440 U.S. 741 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 83", "official_citation_present": true, "parallel_cite": "99 S. Ct. 1465; 59 L. Ed. 2d 733", "title": "United States v. Caceres", "year": "1979"}}
{"assertion_id": "60b2368dc7c2544a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Evidence obtained in violation of an executive agency's internal regulations — here, IRS rules requiring prior authorization for consensual electronic monitoring — need not be excluded from a criminal trial where the agent's conduct violated neither the Constitution nor a federal statute; because the exclusionary rule rests on deterring constitutional violations, it lends no support to suppression for a mere regulatory breach, and the Court declined to adopt any rigid rule excluding all evidence obtained through such a violation.", "title": "United States v. Caceres"}}
{"assertion_id": "a8ffb05231543ef4", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Anchor", "title": "United States v. Caceres"}}
{"assertion_id": "6c138aa5040e56e6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Caceres", "varies_by_point": "false"}}
{"assertion_id": "e6577e264f2e4e7a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Caceres"}}
```

### lake record — United States v. Caceres

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Caceres",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Caceres",
    "case_name_short": "Caceres",
    "case_name_full": "United States v. Caceres",
    "input_case_name": "United States v. Caceres",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-13",
    "year": 1979,
    "docket": "No. 76-1309",
    "cluster_id": 110049,
    "lead_opinion_id": 9427514,
    "sibling_ids": [],
    "absolute_url": "/opinion/110049/united-states-v-caceres/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "440 U.S. 741",
      "volume": "440",
      "reporter": "U.S.",
      "page": "741",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1465",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 733",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 83",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "440 U.S. 741",
        "volume": "440",
        "reporter": "U.S.",
        "page": "741",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1465",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 733",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 83",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "440 U.S. 741",
    "official_selection": {
      "court_class": "scotus",
      "selected": "440 U.S. 741",
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
    "date_created": "2026-07-06T13:42:49Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-caceres--110049",
      "to_record_id": "United States v. Caceres",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Caceres

```
<opinion type="majority">
<author id="b813-5">Mr. Justice Stevens</author>
<p id="At5b">delivered the opinion of the Court.</p>
<p id="b813-6">The question we granted certiorari to decide is whether evidence obtained in violation of Internal Revenue Service (IRS) regulations may be admitted at the criminal trial of a taxpayer accused of bribing an IRS agent. <span class="citation multiple-matches"><a href="/c/U.%20S./436/943/">436 U. S. 943</a></span> (1978).</p>
<p id="b813-7">Unbeknown to respondent, three of his face-to-face conversations with IRS Agent Yee were monitored by means of a radio transmitter concealed on Yee’s person. Respondent moved to suppress tape recordings of the three conversations on the ground that the authorizations required by IRS regulations had not been secured. The District Court granted the motion. The Court of Appeals for the Ninth Circuit reversed as to the third tape; it concluded that adequate authorization had been obtained.<footnotemark>1</footnotemark> As to the first two tapes, however, the Court of Appeals agreed with the District Court both that the IRS regulations had not been followed and that exclusion of the recordings was therefore required. It is the latter conclusion that is at issue here.</p>
<p id="b813-8">The Government argues that exclusion of probative evidence in a criminal trial is an inappropriate sanction for violation of an executive department’s regulations. In this case, moreover, it argues that suppression is especially inappropriate because the violation of the regulation was neither deliberate nor prejudicial, and did not affect any constitu<page-number citation-index="1" label="744">*744</page-number>tional or statutory rights. We agree that suppression should not have been ordered in this case, and therefore reverse the judgment of the Court of Appeals.</p>
<p id="b814-5">I</p>
<p id="b814-6">Neither the Constitution nor any Act of Congress requires that official approval be secured before conversations are overheard or recorded by Government agents with the consent of one of the conversants.<footnotemark>2</footnotemark> Such “consensual electronic surveillance” between taxpayers and IRS agents is, however, prohibited by IRS regulations unless appropriate prior authorization is obtained.<footnotemark>3</footnotemark></p>
<p id="b814-7">The IRS Manual sets forth in detail the procedures to be followed in obtaining such approvals.<footnotemark>4</footnotemark> For all types of re<page-number citation-index="1" label="745">*745</page-number>quests the regulations require an explanation of the reasons for the proposal, the type of equipment to be used; the names of the persons involved, and the duration of the proposed monitoring.</p>
<p id="b815-5">Approval by as many as three different levels of authority may be required, depending on the kind of surveillance that is contemplated and the circumstances of the request. Telephone conversations may be monitored with the approval of an Assistant Regional Inspector of the Internal Security Division. Such advance approval may be requested and given verbally, although the authorization must subsequently be <page-number citation-index="1" label="746">*746</page-number>confirmed in writing. The monitoring of nontelephone conversations requires approval at the national as well as the regional level. In emergency situations, the Director, or Acting Director, Internal Security Division, or the Assistant Commissioner (Inspection) may authorize the recording. If there is at least 48 hours in which to obtain approval, a signed request must also be submitted to the Attorney General of the United States, or a designated Assistant Attorney General, by the Director or Acting Director of the Internal Security Division.</p>
<p id="b816-5">II</p>
<p id="b816-6">On March 14, 1974, Agent Yee met with respondent and his wife in connection with an audit of their 1971 income tax returns. After Mrs. Caceres left the meeting, respondent offered Yee a “personal settlement” of $500 in exchange for a favorable resolution of the audit. When he returned to the IRS office, Yee reported the offer to his superiors and prepared an affidavit describing it.<footnotemark>5</footnotemark></p>
<p id="b816-7">The record reflects no further discussion of the offer until January 1975. It does indicate, however, that one telephone conversation between Yee and respondent, on March 21, 1974, was recorded with authorization,<footnotemark>6</footnotemark> and that authority was also obtained to monitor face-to-face conversations with respondent from time to time during the period between March and September 1974.<footnotemark>7</footnotemark> Yee continued to work on the <page-number citation-index="1" label="747">*747</page-number>audit of respondent’s records throughout this period, but his meetings, until January 1975, were with Mrs. Caceres and the Cacereses’ accountant.<footnotemark>8</footnotemark></p>
<p id="b817-5">On January 27, 1975, Yee had a meeting with respondent that was not recorded. According to Yee’s affidavit,<footnotemark>9</footnotemark> the meeting proceeded in two stages. First, he discussed his calculations with respondent, Mrs. Caceres, and their accountant. When respondent and his wife asked for an additional week to check their records, Yee told them it would be necessary to sign an extension becau'se the statute of limitations would otherwise expire soon. Respondent stated that he would have to consult his attorney before signing any extension, and would call Yee with his decision later that day.</p>
<p id="b817-6">Yee then left the office to return to his car. He was followed by respondent, who revived the subject of a “personal settlement.” This time, respondent indicated that he had $500 that he would give Yee immediately, with an additional $500 to be paid when the matter was finally settled. Yee refused the offer, but at respondent’s insistence, eventually stated that he might consider it.</p>
<p id="b817-7">In subsequent conversations initiated by Agent Yee, all of which were monitored,<footnotemark>10</footnotemark> respondent indicated that he was not prepared for another meeting with Yee. .Finally, in a conversation on January 30 at 5:15 p. m., respondent agreed to a meeting the following day at 2 p. m. At 8:15 a. m. on the <page-number citation-index="1" label="748">*748</page-number>31st, the Regional Inspector in San Francisco telephoned the Director of Internal Security in Washington and obtained emergency approval for the use of electronic equipment to monitor the meeting that afternoon. On the same day, a written request for authority to monitor face-to-face conversations for a period of 30 days was initiated and, in due course, forwarded to Washington for submission to the Department of Justice.</p>
<p id="b818-5">At the meeting on the 31st, respondent gave Yee $500 and promised to give him an additional $500 when he received a notice from IRS showing his deficiency at an amount upon which he and Yee had agreed. As in all his future meetings with respondent, Yee wore a concealed radio transmitter which allowed other agents to monitor and record their conversation.</p>
<p id="b818-6">Yee next called respondent on February 5 and arranged a meeting for the next day to review the audit agreement. Because the Department of Justice had not yet acted on, or perhaps even received, the request for a 30-day authorization, the Regional Inspector again requested and obtained emergency approval to monitor the meeting with respondent. At the February 6 meeting, respondent renewed his promise to pay an additional $500 in connection with the 1971 return, and also offered Yee another $2,000 for help in settling his 1973 and 1974 returns.</p>
<p id="b818-7">On February 11, a Deputy Assistant Attorney General approved the request for authority to monitor Yee’s conversations with respondent for 30 days. The approval was received in time to cover a meeting held that day at which Yee was paid the additional $500. Because the 30-day period did not commence until February 11, however, no approval from the Department of Justice was ever obtained for the earlier monitorings of January 31 and February 6.</p>
<p id="b818-8">The District Court and the Court of Appeals both held that the two earlier meetings had not been monitored in accordance with IRS regulations, since Justice Department approval had <page-number citation-index="1" label="749">*749</page-number>not been secured. The courts recognized that such approval is not required, by the terms of the regulations, in “emergency situations” when less than 48 hours is available to secure authorization. They recognized, too, that in each instance, less than 48 hours did exist between the time the IRS initiated its request for monitoring approval and the time of the scheduled meeting with Yee. But the courts concluded that neither meeting fell within the emergency provision of the regulations because the exigencies were the product of “government-created scheduling problems.” <footnotemark>11</footnotemark></p>
<p id="b819-5">The Government does not challenge that conclusion. We are therefore presented with the question whether the tape recordings, and the testimony of the agents who monitored the January 31 and February 6 conversations, should be excluded because of the violation of the IRS regulations.</p>
<p id="b819-6">Ill</p>
<p id="b819-7">A court’s duty to enforce an agency regulation is most evident when compliance with the regulation is mandated by the Constitution or federal law. In <em>Bridges </em>v. <em>Wixon, </em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#152" aria-description="Citation for case: Bridges v. Wixon">326 U. S. 135, 152-153</a></span>, for example, this Court held invalid a deportation ordered on the basis of statements which did not comply with the Immigration Service’s rules requiring signatures and oaths, finding that the rules were designed “to afford [the alien] due process of law” by providing “safeguards against essentially unfair procedures.” <footnotemark>12</footnotemark></p>
<p id="b819-8">In this case, however, unlike <em>Bridges </em>v. <em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/" aria-description="Citation for case: Bridges v. Wixon">Wixon</a></span>, </em>the agency was not required by the Constitution or by statute to adopt any particular procedures or rules before engaging in con<page-number citation-index="1" label="750">*750</page-number>sensual monitoring and recording. While Title III of the Omnibus Crime Control and Safe Streets Act of 1968, 18 IT. S. C. § 2510 <em>et seq., </em>regulates electronic surveillance conducted without the consent of either party to a conversation, federal statutes impose no restrictions on recording a conversation with the consent of one of the conversants.</p>
<p id="b820-5">Nor does the Constitution protect the privacy of individuals in respondent’s position. In <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 439</a></span>, we held that the Fourth Amendment provided no protection to an individual against the recording of his statements by the IRS agent to whom he was speaking. In doing so, we repudiated any suggestion that the defendant had a “constitutional right to rely on possible flaws in the agent’s memory, or to challenge the agent’s credibility without being beset by corroborating evidence that is not susceptible of impeachment,” concluding instead that “the risk that petitioner took in offering a bribe to [the IRS agent] fairly included the risk that the offer would be accurately reproduced in court, whether by faultless memory or mechanical recording.” The same analysis was applied in <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span>, to consensual monitoring and recording by means of a transmitter concealed on an informant’s person, even though the defendant did not know that he was speaking with a Government agent:</p>
<blockquote id="b820-6">“Concededly a police agent who conceals his police connections may write down for official use his conversations with a defendant and testify concerning them, without a warrant authorizing his encounters with the defendant and without otherwise violating the latter’s Fourth Amendment rights. <em>Hoffa </em>v. <em>United States, </em>385 U. S., at 300-303. For constitutional purposes, no different result is required if the agent instead of immediately reporting and transcribing his conversations with defendant, either (1) simultaneously records them with electronic equipment which he is carrying on his person, <page-number citation-index="1" label="751">*751</page-number><em>Lopez </em>v. <em>United States, supra; </em>(2) or carries radio equipment which simultaneously transmits the conversations either to recording equipment located elsewhere or to other agents monitoring the transmitting frequency. <em>On Lee </em>v. <em>United States, </em>[<span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>]. If the conduct and revelations of an agent operating without electronic equipment do not invade the defendant’s constitutionally justifiable expectations of privacy, neither does a simultaneous recording of the same conversations made by the agent or by others from transmissions received from the agent to whom the defendant is talking and whose trustworthiness the defendant necessarily risks.” <em>United States </em>v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White"><em>White, supra, </em>at 751</a></span> (opinion of White, J.).<footnotemark>13</footnotemark></blockquote>
<p id="b821-5">Our decisions in <em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">Lopez</a></span> </em>and <em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">White</a></span> </em>demonstrate that the IRS was not required by the Constitution to adopt these regulations.<footnotemark>14</footnotemark> It is equally clear that the violations of agency regu<page-number citation-index="1" label="752">*752</page-number>lations disclosed by this record do not raise any constitutional questions.</p>
<p id="b822-5">It is true, of course, that respondent’s conversations were monitored without the approval of the Department of Justice, whereas the conversations of others in a similar position would, assuming the IRS generally follows its regulations, be recorded only with Justice Department approval. But this difference does not even arguably amount to a denial of equal protection. No claim is, or reasonably could be, made that if the IRS had more promptly addressed this request to the Department of Justice, it would have been denied. As a result, any inconsistency of which respondent might complain is purely one of form, with no discernible effect in this case on the action taken by the agency and its treatment of respondent.</p>
<p id="b822-6">Moreover, the failure to secure Justice Department authorization, while conceded here to be a violation of the IRS regulations, was attributable to the fact that the IRS officials responsible for administration of the relevant regulations, both in San Francisco and Washington, construed the situation as an emergency within the meaning of those regulations. Their construction of their own regulations, even if erroneous, was not obviously so. That kind of error by an executive agency in interpreting its own regulations surely does not raise any constitutional questions.</p>
<p id="b822-7">Nor is this a case in which the Due Process Clause is implicated because an individual has reasonably relied on agency <page-number citation-index="1" label="753">*753</page-number>regulations promulgated for his guidance or benefit and has suffered substantially because of their violation by the agency.<footnotemark>15</footnotemark> Respondent cannot reasonably contend that he relied on the regulation, or that its breach had any effect on his conduct. He did not know that his conversations with Yee were being recorded without proper authority.' He was, of course, prejudiced in the sense that he would be better off if all monitoring had been postponed until after the Deputy Assistant Attorney General’s approval was obtained on February 11, 1975, but precisely the same prejudice would have ensued if the approval had been issued more promptly. For the record makes it perfectly clear that a delay in processing the request, rather than any doubt about its propriety or sufficiency, was the sole reason why advance authorization was not obtained before February 11.</p>
<p id="b823-5">Finally, the Administrative Procedure Act<footnotemark>16</footnotemark> provides no grounds for judicial enforcement of the regulation violated in this case. The APA authorizes judicial review and invalidation of agency action that is arbitrary, capricious, an abuse of discretion, or not in accordance with law, as well as action <page-number citation-index="1" label="754">*754</page-number>taken “without observance of procedure required by law.” <footnotemark>17</footnotemark> Agency violations of their own regulations, whether or not also in violation of the Constitution, may well be inconsistent with the standards of agency action which the APA directs the courts .to enforce.<footnotemark>18</footnotemark> Indeed, some of our most important decisions holding agencies bound by their regulations have been in cases originally brought under the APA.<footnotemark>19</footnotemark></p>
<p id="b824-4">But this is not an APA case, and the remedy sought is not invalidation of the agency action. Rather, we are dealing with a criminal prosecution in which respondent seeks judicial enforcement of the agency regulations by means of the exclusionary rule. That rule has primarily rested on the judgment that the importance of deterring police conduct that may invade the constitutional rights of individuals throughout the community outweighs the importance of securing the conviction of the specific defendant on trial.<footnotemark>20</footnotemark> In view of our <page-number citation-index="1" label="755">*755</page-number>conclusion that none of respondent’s constitutional rights has been violated here, either by the actual recording or by the agency violation of its own regulations, our precedents enforcing the exclusionary rule to deter constitutional violations provide no support for the rule’s application in this case.<footnotemark>21</footnotemark></p>
<p id="b825-5">IY</p>
<p id="b825-6">Respondent argues that the regulations concerning electronic eavesdropping, even though not required by the Constitution or by statute, are of such importance in safeguarding the privacy of the citizenry that a rigid exclusionary rule should be applied to all evidence obtained in violation of any of their provisions. We do not doubt the importance of these rules. Nevertheless, without pausing to evaluate the Government’s challenge to our power to do so,<footnotemark>22</footnotemark> we decline to adopt any rigid rule requiring federal courts to exclude any evidence obtained as a result of a violation of these rules.</p>
<p id="b825-7">Regulations governing the conduct of criminal investigations are generally considered desirable, and may well provide more valuable protection to the public at large than the deterrence flowing from the occasional exclusion of items of evidence in criminal trials.<footnotemark>23</footnotemark> Although we do not suggest that a suppression order in this case would cause the IRS to abandon or modify its electronic surveillance regulations, we cannot ignore the possibility that a rigid application of an exclusionary rule to every regulatory violation could have a serious <page-number citation-index="1" label="756">*756</page-number>deterrent impact on the formulation of additional standards to govern prosecutorial and police procedures.<footnotemark>24</footnotemark> Here, the Executive itself has provided for internal sanctions in cases of knowing violations of the electronic-surveillance regulations<footnotemark>25</footnotemark> To go beyond that, and require exclusion in every case, would take away from the Executive Department the primary responsibility for fashioning the appropriate remedy for the violation of its regulations. But since the content, and indeed the existence, of the regulations would remain, within the Executive’s sole authority, the result might well be fewer and less protective regulations. In the long run, it is far better to have rules like those contained in the IRS Manual, and to tolerate occasional erroneous administration of the kind displayed by this record, than either to have no rules except those mandated by statute, or to have them framed in a mere precatory form.</p>
<p id="b826-5">Nor can we accept respondent’s further argument that even without a rigid rule of exclusion, his is a case in which evidence secured in violation of the agency regulation should be excluded on the basis of a more limited, individualized approach. Quite the contrary, this case exemplifies those situations in which evidence would <em>not </em>be excluded if a case-by-case approach were applied. The two conversations at issue here were recorded with the approval of the IRS officials in San Francisco and Washington. In an emergency situa<page-number citation-index="1" label="757">*757</page-number>tion, which the agents thought was present, this approval would have been sufficient. The agency action, while later found to be in violation of the regulations, nonetheless reflected a reasonable, good-faith attempt to comply in a situation in which no one questions that monitoring was appropriate and would have certainly received Justice Department authorization, had the request been received more promptly. In these circumstances, there is simply no reason why a court should exercise whatever discretion it may have to exclude evidence obtained in violation of the regulations.</p>
<p id="b827-5">The judgment of the Court of Appeals is</p>
<p id="b827-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b813-9"> <span class="citation" data-id="340826"><a href="/opinion/340826/united-states-v-alfredo-l-caceres/" aria-description="Citation for case: United States v. Alfredo L. Caceres">545 F. 2d 1182</a></span> (1976). The District Court suppressed evidence relating to the third conversation as well on the ground that the approval of a <em>Deputy </em>Assistant Attorney General was not sufficient to comply with the regulations. The Court of Appeals disagreed, concluding that the Attorney General’s authority to approve such monitoring could be delegated not only to Assistant Attorneys General, as provided specifically in the regulation, but also to their deputies. That conclusion is not at issue here.</p>
</footnote>
<footnote label="2">
<p id="b814-8"> See <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S. 745, 752</a></span> (plurality opinion); <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; <span class="citation no-link">18 U. S. C. §2511</span> (2) (c); <em>infra, </em>at 749-751.</p>
</footnote>
<footnote label="3">
<p id="b814-9"> The IRS regulations were drafted to conform to the requirements of the Attorney General’s October 16, 1972, Memorandum to the Heads of Executive Departments and Agencies. The memorandum mandates Justice Department approval for all consensual monitoring of nontelephone conversations by federal departments and agencies. The only exceptions are if less than 48 hours is available to secure approval or if exigent circumstances preclude requests for advance authorization from the Justice Department; in such cases, monitoring may be instituted under the authorization of the head of the department or agency, or other officials designated by him.</p>
</footnote>
<footnote label="4">
<p id="b814-10"> Paragraph 652.22 of the IRS Manual (in effect Sept. 1975) provides in pertinent part:</p>
<p id="b814-11">“(1) The monitoring of non-telephone conversations with the consent of one party requires the advance authorization of the Attorney General or any designated Assistant Attorney General. Requests for such authority may be signed by the Director, Internal Security Division, or, in his/her absence, the Acting Director. This authority cannot be redelegated. These same officials may authorize temporary emergency monitoring when exigent circumstances preclude requesting the authorization of the Attorney General in advance. If the Director, Internal Security Division, <page-number citation-index="1" label="745">*745</page-number>cannot be reached, the Assistant Commissioner (Inspection) may grant emergency approval. This authority cannot be redelegated.</p>
<p id="A2g">“(2) Written approval of the Attorney General must be requested 48 hours prior to the use of mechanical, electronic or other devices to overhear, transmit or record a non-telephone private conversation with the permission of one party to the conversation. . . . Any requests being telefaxed into the National Office should be submitted four days prior to the anticipated equipment use. . . .</p>
<p id="ANx">“(3) [A request] must be signed and submitted by the Regional Inspector or Chief, Investigations Branch, to the Director, Internal Security Division. Such requests will contain [reason for such proposed use; type of equipment to be used; names of persons involved; proposed location of equipment; duration of proposed use (limited to 30 days from proposed beginning date); and manner or method of installation] ....</p>
<p id="AA_j">“(6) When emergency situations occur, the Director or Acting Director, Internal Security Division, or the Assistant Commissioner (Inspection) will be contacted to grant emergency approval to monitor. This emergency approval authority cannot be redelegated. . . . Emergency authorization pursuant to this exception will not be given where the requesting official has in excess of 48 hours to obtain written advance approval from the Attorney General.</p>
<p id="AJo">“(7) If, at the time the emergency approval request is submitted, it is desired that approval for use of electronic equipment be given for an extended period, this should be indicated on the [appropriate form]. The Director, in addition to reporting his authorization for emergency use to the Attorney General, will also request approval for the Use of Electronic Equipment for the duration of that period specified by the requestor.”</p>
</footnote>
<footnote label="5">
<p id="b816-8"> App. 20, 23-24, 46.</p>
</footnote>
<footnote label="6">
<p id="b816-9"> <em>Id,., </em>at 25-27, 46.</p>
</footnote>
<footnote label="7">
<p id="b816-10"> Requests for authorization to use electronic equipment to monitor nontelephone conversations are made on a form (No. 5177) that requires disclosure of the dates of previous authorizations. The form dated January 31, 1975, App. 63, is termed an extension, and reports prior authorizations dated March 25, April 24, May 24, June 27, July 23, and August 29, 1974. Under the regulations, a single authorization may cover a period of up to 30 days; the intervals between the dates of prior authorizations in this case are consistent with successive 30-day authorizations, although this has not been established by any evidence called to our attention.</p>
</footnote>
<footnote label="8">
<p id="b817-8"> Yee had one follow-up conversation with respondent later in March, which was not monitored. From that point until January 1975, he had no further contact with respondent. App. to Pet. for Cert. 16a (opinion and order of the District Court); App. 21-22,</p>
</footnote>
<footnote label="9">
<p id="b817-9"><span class="citation no-link"><em> Id., </em>at 65-67</span>.</p>
</footnote>
<footnote label="10">
<p id="b817-10"> In the District Court, respondent moved to suppress evidence relating to these telephone conversations on the grounds that the monitoring had not been properly authorized. The District Court rejected that challenge, concluding that the applicable IRS regulations had been followed with respect to these conversations. App. to Pet. for Cert. 16a-17a. That ruling is not at issue here.</p>
</footnote>
<footnote label="11">
<p id="b819-9"> 545 E. 2d, at 1187. See also App. to Pet. for Cert. 20a (opinion of District Court) (“the only 'emergency’ was created wholly by the I. R. S.”).</p>
</footnote>
<footnote label="12">
<p id="b819-10"> See also <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#155" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149, 155</a></span> (Court assumed that “one under investigation with a view to deportation is legally entitled to insist upon the observance of rules promulgated by the Secretary pursuant to law”).</p>
</footnote>
<footnote label="13">
<p id="b821-6"> Mr. Justice White further stated:</p>
<p id="b821-7">“Nor should we be too ready to erect constitutional barriers to relevant and probative evidence which is also accurate and reliable. An electronic recording will many times produce a more reliable rendition of what a defendant has said than will the unaided memory of a police agent. It may also be that with the recording in existence it is less likely that the informant will change his mind, less chance that threat or injury will suppress unfavorable evidence and less chance that cross-examination will confound the testimony. Considerations like these obviously do not favor the defendant, but we are not prepared to hold that a defendant who has no constitutional right to exclude the informer’s unaided testimony nevertheless has a Fourth Amendment privilege against a more accurate version of the events in question.” <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#753" aria-description="Citation for case: United States v. White">401 U. S., at 753</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b821-8"> It does not necessarily follow, however, as a matter of either logic or law, that the agency had no duty to obey them. “Where the rights of individuals are affected, it is incumbent upon agencies to follow their own procedures. This is so even where the internal procedures are possibly more rigorous than otherwise would be required.” <em>Morton </em>v. <em>Ruiz, </em><span class="citation" data-id="108969"><a href="/opinion/108969/morton-v-ruiz/#235" aria-description="Citation for case: Morton v. Ruiz">415 U. S. 199, 235</a></span>. See, <em>e. g., United States ex rel. Accardi </em>v. <em>Shaughnessy, </em><span class="citation" data-id="9421054"><a href="/opinion/105205/united-states-ex-rel-accardi-v-shaughnessy/" aria-description="Citation for case: United States Ex Rel. Accardi v. Shaughnessy">347 U. S. 260</a></span> (holding habeas corpus relief proper where Government regulations “with the force and effect of law” governing the procedure to be foEowed in processing and passing upon an alien’s application for suspen<page-number citation-index="1" label="752">*752</page-number>sion of deportation were not followed); <em>Service </em>v. <em>Dulles, </em><span class="citation" data-id="105539"><a href="/opinion/105539/service-v-dulles/" aria-description="Citation for case: Service v. Dulles">354 U. S. 363</a></span> (invalidating Secretary of State’s dismissal of an employee where regulations requiring approval of the Deputy Undersecretary and consultation of full record were not satisfied); <em>Vitarelli </em>v. <em>Seaton, </em><span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/" aria-description="Citation for case: Vitarelli v. Seaton">359 U. S. 535</a></span> (invalidating dismissal of Interior Department employee where regulations governing hearing procedures for national security dismissals were not followed). See also <em>Yellin </em>v. <em>United States, </em><span class="citation" data-id="9422642"><a href="/opinion/106654/yellin-v-united-states/" aria-description="Citation for case: Yellin v. United States">374 U. S. 109</a></span> (reversing contempt conviction where congressional committee had not complied with its rules requiring it to consider a witness’ request to be heard in executive session).</p>
</footnote>
<footnote label="15">
<p id="b823-6"> In <em>Raley </em>v. <em>Ohio, </em><span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#437" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 437-438</a></span>, we held that due process precluded the conviction of individuals for refusing to answer questions asked by a state investigating commission which itself had erroneously provided assurances, express or implied, that the defendants had a privilege under state law to refuse to answer. And in <em>Cox </em>v. <em>Louisiana, </em><span class="citation" data-id="9422938"><a href="/opinion/106968/cox-v-louisiana/" aria-description="Citation for case: Cox v. Louisiana">379 U. S. 559</a></span>, the Court held that an individual could not be punished for demonstrating “near” a courthouse where the highest police officials of the city had advised the demonstrators that they could meet where they did without violating the statutory proscription against demonstrations “near” the courthouse. Cf. <em>Arizona Grocery Co. </em>v. <em>Atchison, T. &amp; S. F. R. Co., </em><span class="citation" data-id="101832"><a href="/opinion/101832/arizona-grocery-co-v-atchison-topeka-santa-fe-railway-co/" aria-description="Citation for case: Arizona Grocery Co. v. Atchison, Topeka &amp; Santa Fe...">284 U. S. 370</a></span> (holding invalid Interstate Commerce Commission's retroactive application of new rate); <em>Columbia Broadcasting System, Inc. </em>v. <em>United States, </em><span class="citation" data-id="9419254"><a href="/opinion/103691/columbia-broadcasting-system-inc-v-united-states/#422" aria-description="Citation for case: Columbia Broadcasting System, Inc. v. United States">316 U. S. 407, 422</a></span> (agency regulations on which individuals are “-entitled to rely” bind agency and are therefore ripe for judicial review). The underlying rationale of the foregoing cases is plainly inapplicable here.</p>
</footnote>
<footnote label="16">
<p id="b823-7"> The Act was originally passed in 1946, <span class="citation no-link">60 Stat. 237</span>, and is codified at <span class="citation no-link">5 U. S. C. § 551</span> <em>et seq. </em>and § 701 <em>et seq.</em></p>
</footnote>
<footnote label="17">
<p id="b824-5"> <span class="citation no-link">5 U. S. C. § 706</span>.</p>
</footnote>
<footnote label="18">
<p id="b824-6"> Cf. <em>Board of Curators, Univ. of Mo. </em>v. <em>Horowitz, </em><span class="citation" data-id="9427086"><a href="/opinion/109809/board-of-curators-of-the-university-of-missouri-v-horowitz/" aria-description="Citation for case: Board of Curators of the University of Missouri v. Horowitz">435 U. S. 78</a></span>, 92 n. 8; <em>Vitarelli </em>v. <span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/#547" aria-description="Citation for case: Vitarelli v. Seaton"><em>Seaton, supra, </em>at 547</a></span> (Frankfurter, J., concurring in part and dissenting in part) (“This judicially evolved rule of administrative law is now firmly established and, if I may add, rightly so. He that takes the procedural sword shall perish with that sword”).</p>
<p id="b824-7">Even as a matter of administrative law, however, it seems clear that agencies are not required, at the risk of invalidation of their action, to follow all of their rules, even those properly classified as “internal.” In <em>American Farm Lines </em>v. <em>Black Ball Freight Service, </em><span class="citation" data-id="9424239"><a href="/opinion/108117/american-farm-lines-v-black-ball-freight-service/#538" aria-description="Citation for case: American Farm Lines v. Black Ball Freight Service">397 U. S. 532, 538</a></span>, for example, ICC rules requiring certain information to be included in applications had not been followed. This Court rejected the argument that the agency action was therefore invalid, concluding that the Commission was “entitled to a measure of discretion in administering its own procedural rules in such a manner as it deems necessary to resolve quickly and correctly urgent transportation problems.”</p>
</footnote>
<footnote label="19">
<p id="b824-8"> See App. in <em>Service </em>v. <em><span class="citation" data-id="105539"><a href="/opinion/105539/service-v-dulles/" aria-description="Citation for case: Service v. Dulles">Dulles</a></span>, </em>O. T. 1956, No. 407, p. 40; App. in <em>Vitarelli </em>v. <em><span class="citation" data-id="9421811"><a href="/opinion/105892/vitarelli-v-seaton/" aria-description="Citation for case: Vitarelli v. Seaton">Seaton</a></span>, </em>O. T. 1958, No. 101, p. 7. The complaints in both of these cases invoked <span class="citation no-link">5 U. S. C. § 1009</span> (1964 ed.), the then-applicable APA judicial-review provision.</p>
</footnote>
<footnote label="20">
<p id="b824-9"> See <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#633" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 633, 636-637</a></span>; <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span>; <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span>.</p>
</footnote>
<footnote label="21">
<p id="b825-8"> Since no statute was violated by the recording of respondent’s conversations, this Court’s decision in <em>Miller </em>v. <em>United States, </em><span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, is likewise inapplicable.</p>
</footnote>
<footnote label="22">
<p id="b825-9"> The Government argues that Fed. Rule Evid. 402 and <span class="citation no-link">18 U. S. C. § 3501</span> prohibited the Court of Appeals from exercising whatever supervisory power it might otherwise have to suppress evidence of respondent’s statements to Yee. Brief for United States 42.</p>
</footnote>
<footnote label="23">
<p id="b825-10"> See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 416-428 (1974); McGowan, Rule-Making and the Police, <span class="citation no-link">70 Mich. L. Rev. 659</span> (1972).</p>
</footnote>
<footnote label="24">
<p id="b826-6"> See F. Cooper, Administrative Agencies and the Courts 289-290 (1951) (“[T]oo rigid an application of the doctrine prohibiting disregard of procedural rules would encourage the tendency of some agencies to proceed almost without rules. The doctrine should not be pressed so far as to induce agencies to adopt the protective device of promulgating procedural rules so vague in nature as to make it impossible to show a violation of the rules”).</p>
</footnote>
<footnote label="25">
<p id="b826-7"> See IRS Manual ¶ 652.1 (3) (in effect Sept. 1975) (“Any employee who knowingly violates or in any way knowingly countenances violation of this policy will be subject to disciplinary action and may be removed from the Service”).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Classic.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Classic"
type: case
citation: "313 U.S. 299 (1941)"
parallel_cite: "61 S. Ct. 1031; 85 L. Ed. 1368"
neutral_cite: 1941 U.S. LEXIS 601
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1941
date_decided: 1941-10-13
docket: 618
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1941-05-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Classic
  varies_by_point: false
  scope_note: "The 'under color of' state law definition remains the governing test; adopted for § 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103531/united-states-v-classic/"
  cluster_id: 103531
  opinion_id: 103531
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Monroe v. Pape]]", "[[Screws v. United States]]"]
aliases: []
tags: ["case", "section-1983", "color-of-law", "section-242", "civil-rights", "state-action"]
holding: "Misuse of power possessed by virtue of state law and made possible only because the wrongdoer is clothed with state authority is action taken 'under color of' state law — the anchor color-of-law definition later applied to § 1983."
lake:
  record_id: United States v. Classic
  status: verified
  projected_at: 2026-07-06
---

# United States v. Classic

*313 U.S. 299 (1941)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Louisiana election commissioners were indicted under the federal criminal civil-rights statutes (then §§ 19 and 20 of the Criminal Code, now 18 U.S.C. §§ 241–242) for willfully altering and falsely counting ballots cast in a Democratic primary election for a seat in the U.S. House of Representatives. They moved to dismiss, arguing both that the right to vote in a primary was not constitutionally protected and that, as election officials, they had not acted "under color of" state law.

## Issue
Whether officials who misuse authority conferred on them by state law act "under color of" state law for purposes of the federal civil-rights statutes (and whether the right to vote in a primary is constitutionally protected).

## Rule
Officials who abuse power held by virtue of their state office act under [[Section 1983 Liability and Qualified Immunity|color of state law]]. "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law." — 313 U.S. at 326. ^pin-326

The Court also held that the constitutionally protected right to choose a Representative includes the right to vote in a primary that is an integral part of the election machinery, so the commissioners' fraud deprived voters of a federally secured right.

## Application
The commissioners' acts — altering and falsely certifying the ballot count — were done "in the course of their performance of duties under the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election." Because they could commit the fraud only because they were clothed with the authority of state election law, their misuse of that authority was action "under color of" state law, and it deprived the voters of a right secured by the Constitution.

## Conclusion
Reversed in relevant part. Misuse of state-conferred power is action under [[Section 1983 Liability and Qualified Immunity|color of state law]], and the indictment stated an offense; the color-of-law definition announced here became the foundational test for state action under the civil-rights statutes.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Classic*'s "under color of" definition is the anchor later carried into criminal civil-rights enforcement in [[Screws v. United States]] and expressly adopted for civil § 1983 liability in [[Monroe v. Pape]]; it remains the governing color-of-law formulation. (*Classic* also overruled *Grovey v. Townsend* on the primary-voting question.) No negative treatment of the color-of-law holding.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *United States v. Classic*, 313 U.S. 299 (1941) — https://www.courtlistener.com/opinion/103531/united-states-v-classic/ — pinpoint: 326 (CL stores a paragraph-numbered format without star pages; page per official U.S. Reports citation).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "546ce0557d79007c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "313 U.S. 299 (1941)", "court": "U.S. Supreme Court", "neutral_cite": "1941 U.S. LEXIS 601", "official_citation_present": true, "parallel_cite": "61 S. Ct. 1031; 85 L. Ed. 1368", "title": "United States v. Classic", "year": "1941"}}
{"assertion_id": "2987cbfd5069d190", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Key — Anchor", "title": "United States v. Classic"}}
{"assertion_id": "9ccb8f8e60d99891", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Misuse of power possessed by virtue of state law and made possible only because the wrongdoer is clothed with state authority is action taken 'under color of' state law — the anchor color-of-law definition later applied to § 1983.", "title": "United States v. Classic"}}
{"assertion_id": "51cb9f4da6c30d3f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Classic"}}
{"assertion_id": "e4c033f2ebd7fe57", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1941-05-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Classic", "field_i_validity": "good_law", "scope_note": "The 'under color of' state law definition remains the governing test; adopted for § 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)", "title": "United States v. Classic", "varies_by_point": "false"}}
```

### lake record — United States v. Classic

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Classic",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Classic",
    "case_name_short": "Classic",
    "case_name_full": "UNITED STATES v. CLASSIC Et Al.",
    "input_case_name": "United States v. Classic",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1941-10-13",
    "year": 1941,
    "docket": "618",
    "cluster_id": 103531,
    "lead_opinion_id": 103531,
    "sibling_ids": [
      103531,
      9419158,
      9419159
    ],
    "absolute_url": "/opinion/103531/united-states-v-classic/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "313 U.S. 299",
      "volume": "313",
      "reporter": "U.S.",
      "page": "299",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "61 S. Ct. 1031",
        "volume": "61",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 1368",
        "volume": "85",
        "reporter": "L. Ed.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1941 U.S. LEXIS 601",
        "volume": "1941",
        "reporter": "U.S. LEXIS",
        "page": "601",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "313 U.S. 299",
        "volume": "313",
        "reporter": "U.S.",
        "page": "299",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 S. Ct. 1031",
        "volume": "61",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 1368",
        "volume": "85",
        "reporter": "L. Ed.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1941 U.S. LEXIS 601",
        "volume": "1941",
        "reporter": "U.S. LEXIS",
        "page": "601",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "313 U.S. 299",
    "official_selection": {
      "court_class": "scotus",
      "selected": "313 U.S. 299",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "state law for purposes of the federal civil-rights statutes (and whether the right to vote in a primary is constitutionally protected). ## Rule Officials who abuse power held by virtue of their state office act under color of state law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1941-05-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Classic",
    "varies_by_point": false,
    "scope_note": "The 'under color of' state law definition remains the governing test; adopted for \u00a7 1983 in Monroe v. Pape. (Classic overruled Grovey v. Townsend on the primary-voting point.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Dustin Myers v. Murry Bowman",
          "cluster_id": 857864,
          "cite": [
            "713 F.3d 1319",
            "2013 WL 1442055",
            "2013 U.S. App. LEXIS 7216",
            "24 Fla. L. Weekly Fed. C 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Constitutionality of the D.C. House Voting Rights Act of 2009",
          "cluster_id": 6236943,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellee-Cross-Appellant v. Eva C. Temple, Appellant-Cross-Appellee",
          "cluster_id": 794242,
          "cite": [
            "447 F.3d 130",
            "97 A.F.T.R.2d (RIA) 2265",
            "2006 U.S. App. LEXIS 10885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tobin",
          "cluster_id": 10699401,
          "cite": [
            "2005 DNH 161"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roberto Hernandez Miranda v. Clark County, Nevada Morgan Harris Thomas Rigsby",
          "cluster_id": 776499,
          "cite": [
            "279 F.3d 1102",
            "2002 Cal. Daily Op. Serv. 1289",
            "2002 Daily Journal DAR 1628",
            "2002 U.S. App. LEXIS 2004",
            "2002 WL 193029"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mentavlos v. Anderson",
          "cluster_id": 2967409,
          "cite": [
            "249 F.3d 301",
            "2001 WL 475936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "West v. Atkins",
          "cluster_id": 112116,
          "cite": [
            "101 L. Ed. 2d 40",
            "108 S. Ct. 2250",
            "487 U.S. 42",
            "1988 U.S. LEXIS 2744",
            "56 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adickes v. S. H. Kress & Co.",
          "cluster_id": 108153,
          "cite": [
            "26 L. Ed. 2d 142",
            "90 S. Ct. 1598",
            "398 U.S. 144",
            "1970 U.S. LEXIS 31"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scheuer v. Rhodes",
          "cluster_id": 109009,
          "cite": [
            "40 L. Ed. 2d 90",
            "94 S. Ct. 1683",
            "416 U.S. 232",
            "1974 U.S. LEXIS 126",
            "71 Ohio Op. 2d 474"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. Carr",
          "cluster_id": 106366,
          "cite": [
            "7 L. Ed. 2d 663",
            "82 S. Ct. 691",
            "369 U.S. 186",
            "1962 U.S. LEXIS 1567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buckley v. Valeo",
          "cluster_id": 109380,
          "cite": [
            "46 L. Ed. 2d 659",
            "96 S. Ct. 612",
            "424 U.S. 1",
            "1976 U.S. LEXIS 16"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lugar v. Edmondson Oil Co.",
          "cluster_id": 110766,
          "cite": [
            "73 L. Ed. 2d 482",
            "102 S. Ct. 2744",
            "457 U.S. 922",
            "1982 U.S. LEXIS 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reynolds v. Sims",
          "cluster_id": 106850,
          "cite": [
            "12 L. Ed. 2d 506",
            "84 S. Ct. 1362",
            "377 U.S. 533",
            "1964 U.S. LEXIS 1002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Shea v. Littleton",
          "cluster_id": 108906,
          "cite": [
            "38 L. Ed. 2d 674",
            "94 S. Ct. 669",
            "414 U.S. 488",
            "1974 U.S. LEXIS 41"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Breckenridge",
          "cluster_id": 108362,
          "cite": [
            "29 L. Ed. 2d 338",
            "91 S. Ct. 1790",
            "403 U.S. 88",
            "1971 U.S. LEXIS 3774",
            "3 Empl. Prac. Dec. (CCH) 8284",
            "9 Fair Empl. Prac. Cas. (BNA) 1196"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jett v. Dallas Independent School District",
          "cluster_id": 112313,
          "cite": [
            "105 L. Ed. 2d 598",
            "109 S. Ct. 2702",
            "491 U.S. 701",
            "1989 U.S. LEXIS 3130",
            "57 U.S.L.W. 4858",
            "50 Fair Empl. Prac. Cas. (BNA) 27",
            "50 Empl. Prac. Dec. (CCH) 39,070"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owen v. City of Independence",
          "cluster_id": 110236,
          "cite": [
            "63 L. Ed. 2d 673",
            "100 S. Ct. 1398",
            "445 U.S. 622",
            "1980 U.S. LEXIS 14"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rendell-Baker v. Kohn",
          "cluster_id": 110764,
          "cite": [
            "73 L. Ed. 2d 418",
            "102 S. Ct. 2764",
            "457 U.S. 830",
            "1982 U.S. LEXIS 43"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davidson v. Cannon",
          "cluster_id": 111556,
          "cite": [
            "88 L. Ed. 2d 677",
            "106 S. Ct. 668",
            "474 U.S. 344",
            "1986 U.S. LEXIS 44",
            "54 U.S.L.W. 4095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Sparks",
          "cluster_id": 110353,
          "cite": [
            "66 L. Ed. 2d 185",
            "101 S. Ct. 183",
            "449 U.S. 24",
            "1980 U.S. LEXIS 9",
            "49 U.S.L.W. 4001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Youngstown Sheet & Tube Co. v. Sawyer",
          "cluster_id": 105018,
          "cite": [
            "96 L. Ed. 2d 1153",
            "72 S. Ct. 863",
            "343 U.S. 579",
            "1952 U.S. LEXIS 2625",
            "62 Ohio Law. Abs. 417",
            "96 L. Ed. 1153",
            "26 A.L.R. 2d 1378",
            "47 Ohio Op. 430",
            "30 L.R.R.M. (BNA) 2172",
            "1952 Trade Cas. (CCH) 67,293"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Classic:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103531 OR 9419158 OR 9419159) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NDExNTUyMDAwMDAmcz0yMzM2MzE4JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103531+OR+9419158+OR+9419159%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(103531 OR 9419158 OR 9419159)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDYmcz0xMTIyMDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103531+OR+9419158+OR+9419159%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103531 OR 9419158 OR 9419159)",
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
    "complete_query": "cites:(103531 OR 9419158 OR 9419159)",
    "indexed_citing_opinions": 1016,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103531,
        "count": 930,
        "count_source": "search"
      },
      {
        "opinion_id": 9419158,
        "count": 116,
        "count_source": "search"
      },
      {
        "opinion_id": 9419159,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2093,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-classic.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NTcxNTQmcz05NDkzNTU4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103531+OR+9419158+OR+9419159%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103531,
        "cited_id": 84968,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 88998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 89266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 90042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 92299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 92761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 93413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 94602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 95887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97691,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 97928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 98985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99495,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 99796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 102874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 103462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 1087873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103531,
        "cited_id": 2620807,
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
    "date_created": "2026-07-05T23:09:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:13:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:09:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Classic (truncated)

```
<p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">61 S.Ct. 1031</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">85 L.Ed. 1368</a></span></p>
    <p class="parties">UNITED STATES<br>v.<br>CLASSIC et al.</p>
    <p class="docket">No. 618.</p>
    <p class="date">Argued April 7, 1941.</p>
    <p class="date">Decided May 26, 1941.</p>
    <p class="date">Rehearing Denied Oct. 13, 1941.</p>
    <div class="prelims">
      <p class="indent">[Syllabus from pages 299-301 intentionally omitted]</p>
      <p class="indent">Messrs. Robert H. Jackson, Atty. Gen., and Herbert Wechsler, of Washington, D.C., for appellant.</p>
      <p class="indent">[Argument of Counsel from pages 301-303 intentionally omitted]</p>
      <p class="indent">Mr. Warren O. Coleman, of New Orleans, La., for appellees.</p>
      <p class="indent">[Argument of Counsel from Pages 304-306 intentionally omitted]</p>
      <p class="indent">Mr. Justice STONE, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">Two counts of an indictment found in a federal district court charged that appellees, Commissioners of Elections, conducting a primary election under Louisiana law, to nominate a candidate of the Democratic Party for representative in Congress, willfully altered and falsely counted and certified the ballots of voters cast in the primary election. The questions for decision are whether the right of qualified voters to vote in the Louisiana primary and to have their ballots counted is a right 'secured * * * by the Constitution' within the meaning of &#167;&#167; 19 and 20 of the Criminal Code, and whether the acts of appellees charged in the indictment violate those sections.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">On September 25, 1940, appellees were indicted in the District Court for Eastern Louisiana for violations of &#167;&#167; 19 and 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. &#167;&#167; 51</span>, 52, <span class="citation no-link">18 U.S.C.A. &#167; 51</span>, 52. The first count of the indictment alleged that a primary election was held on September 10, 1940, for the purpose of nominating a candidate of the Democratic Party for the office of Representative in Congress for the Second Congressional District of Louisiana, to be chosen at an election to be held on November 10th; that in that district nomination as a candidate of the Democratic Party is and always has been equivalent to an election; that appellees were Commissioners of Election, selected in accordance with the Louisiana law to conduct the primary in the Second Precinct of the Tenth Ward of New Orleans, in which there were five hundred and thirty-seven citizens and qualified voters.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The charge based on these allegations, was that the appellees conspired with each other and with others unknown, to injure and oppress citizens in the free exercise and enjoyment of rights and privileges secured to them by the Constitution and Laws of the United States, namely, (1) the right of qualified voters who cast their ballots in the primary election to have their ballots counted as cast for the candidate of their choice, and (2) the right of the candidates to run for the office of Congressman and to have the votes in favor of their nomination counted as cast. The overt acts alleged were that the appellees altered eighty-three ballots cast for one candidate and fourteen cast for another, marking and counting them as votes for a third candidate, and that they falsely certified the number of votes cast for the respective candidates to the chairman of the Second Congressional District Committee.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">The second count, repeating the allegations of fact already detailed, charged that the appellees, as Commissioners of Election willfully and under color of law subjected registered voters at the pr mary who were inhabitants of Louisiana to the deprivation of rights, privileges and immunities secured and protected by the Constitution and Laws of the United States, namely their right to cast their votes for the candidates of their choice and to have their votes counted as cast. It further charged that this deprivation was effected by the willful failure and refusal of defendants to count the votes as cast, by their alteration of the ballots, and by their false certification of the number of votes cast for the respective candidates in the manner already indicated.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">The District Court sustained a demurrer to counts 1 and 2 on the ground that &#167;&#167; 19 and 20 of the Criminal Code under which the indictment was drawn do not apply to the state of facts disclosed by the indictment and that, if applied to those facts, &#167;&#167; 19 and 20 are without constitutional sanction, citing United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#488" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476, 488, 489</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#411" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407, 411, 412</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>; Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>. The case comes here on direct appeal from the District Court under the provisions of the Criminal Appeals Act, Judicial Code, &#167; 238, <span class="citation no-link">18 U.S.C. &#167; 682</span>, <span class="citation no-link">18 U.S.C.A. &#167; 682</span>, <span class="citation no-link">28 U.S.C. &#167; 345</span>, <span class="citation no-link">28 U.S.C.A. &#167; 345</span>, which authorize an appeal by the United States from a decision or judgment sustaining a demurrer to an indictment where the decision or judgment is 'based upon the invalidity, or construction of the statute upon which the indictment is founded'.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Upon such an appeal our review is confined to the questions of statutory construction and validity decided by the District Court. United States v. Patten, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">226 U.S. 525</a></span>, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">33 S.Ct. 141</a></span>, <span class="citation" data-id="9418228"><a href="/opinion/97744/united-states-v-patten/" aria-description="Citation for case: United States v. Patten">57 L.Ed. 333</a></span>, 44 L.R.A.,N.S., 325; United States v. Birdsall, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/#230" aria-description="Citation for case: United States v. Birdsall">233 U.S. 223, 230</a></span>, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/#514" aria-description="Citation for case: United States v. Birdsall">34 S.Ct. 512, 514</a></span>, <span class="citation" data-id="98150"><a href="/opinion/98150/united-states-v-birdsall/" aria-description="Citation for case: United States v. Birdsall">58 L.Ed. 930</a></span>; United States v. Borden Co., <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/#192" aria-description="Citation for case: United States v. Borden Co.">308 U.S. 188, 192, 193</a></span>, <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/#185" aria-description="Citation for case: United States v. Borden Co.">60 S.Ct. 182, 185</a></span>, <span class="citation" data-id="103246"><a href="/opinion/103246/united-states-v-borden-co/" aria-description="Citation for case: United States v. Borden Co.">84 L.Ed. 181</a></span>. Hence, we do not pass upon various arguments advanced by appellees as to the sufficiency and construction of the indictment.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">Section 19 of the Criminal Code condemns as a criminal offense any conspiracy to injure a citizen in the exercise 'of any right or privilege secured to him by the Constitution or laws of the United States'. Section 20 makes it a penal offense for anyone who, 'acting under color of any law' 'willfully subjects, or causes to be subjected, any inhabitant of any State * * * to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States'. The Government argues that the right of a qualified voter in a Louisiana congressional primary election to have his vote counted as cast is a right secured by Article I, &#167;&#167; 2 and 4 of the Constitution, and that a conspiracy to deprive the citizen of that right is a violation of &#167; 19, and also that the willful action of appellees as state officials, in falsely counting the ballots at the primary election and in falsely certifying the count, deprived qualified voters of that right and of the equal protection of the laws guaranteed by the Fourteenth Amendment, all in violation of &#167; 20 of the Criminal Code.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Article I, &#167; 2 of the Constitution, commands that 'The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the qualifications requisite for Electors of the most numerous Branch of the State Legislature'. By &#167; 4 of the same article 'The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators'. Such right as is secured by the Constitution to qualified voters to choose members of the House of Representatives is thus to be exercised in conformity to the requirements of state law subject to the restrictions prescribed by &#167; 2 and to the authority conferred on Congress by &#167; 4, to regulate  he times, places and manner of holding elections for representatives.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">We look then to the statutes of Louisiana here involved to ascertain the nature of the right which under the constitutional mandate they define and confer on the voter and the effect upon its exercise of the acts with which appellees are charged, all with the view to determining, first, whether the right or privilege is one secured by the Constitution of the United States, second, whether the effect under the state statute of appellee's alleged acts is such that they operate to injure or oppress citizens in the exercise of that right within the meaning of &#167; 19 and to deprive inhabitants of the state of that right within the meaning of &#167; 20, and finally, whether &#167;&#167; 19 and 20 respectively are in other respects applicable to the alleged acts of appellees.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">Pursuant to the authority given by &#167; 2 of Article I of the Constitution, and subject to the legislative power of Congress under &#167; 4 of Article I, and other pertinent provisions of the Constitution, the states are given, and in fact exercise a wide discretion in the formulation of a system for the choice by the people of representatives in Congress. In common with many other states Louisiana has exercised that discretion by setting up machinery for the effective choice of party candidates for representative in Congress by primary elections and by its laws it eliminates or seriously restricts the candidacy at the general election of all those who are defeated at the primary. All political parties, which are defined as those that have cast at least 5 per cent of the total vote at specified preceding elections, are required to nominate their candidates for representative by direct primary elections. Louisiana Act No. 46, Regular Session, 1940, &#167;&#167; 1 and 3.</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The primary is conducted by the state at public expense. Act No. 46, supra, &#167; 35. The primary, as is the general election, is subject to numerous statutory regulations as to the time, place and manner of conducting the election, including provisions to insure that the ballots cast at the primary are correctly counted, and the results of the count correctly recorded and certified to the Secretary of State, whose duty it is to place the names of the successful candidates of each party on the official ballot.<a class="footnote" href="#fn1" id="fn1_ref">1</a> The Secretary of State is prohibited from placing on the official ballot the name of any person as a candidate for any political party not nominated in accordance with the provisions of the Act. Act 46, &#167; 1.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">One whose name does not appear on the primary ballot, if otherwise eligible to become a candidate at the general election, may do so in either of two ways, by filing nomination papers with the requisite number of signatures or by having his name 'written in' on the ballot on the final election. Louisiana Act No. 224, Regular Session 1940, &#167;&#167; 50, 73. Section 87 of Act No. 46 provides 'No one who participates in the primary election of any political party shall have the right to participate in any primary election of any other political party, with a view of nominating opposing candidates, nor shall he be permitted to sign any nomination papers for  ny opposing candidate or candidates; nor shall he be permitted to be himself a candidate in opposition to any one nominated at or through a primary election in which he took part'.</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">Section 15 of Article VIII of the Constitution of Louisiana as amended by Act 80 of 1934, provides that 'no person whose name is not authorized to be printed on the official ballot, as the nominee of a political party or as an independent candidate, shall be considered a candidate,' unless he shall file in the appropriate office at least ten days before the general election a statement containing the correct name under which he is to be voted for and containing the further statement that he is willing and consents to be voted for for that office. The article also provides that 'no commissioners of election shall count a ballot as cast for any person whose name is not printed on the ballot or who does not become a candidate in the foregoing manner'. Applying these provisions the Louisiana Court of Appeals for the Parish of Orleans has held in Serpas v. Trebucq, <span class="citation" data-id="3473908"><a href="/opinion/3474685/serpas-v-trebucq/" aria-description="Citation for case: Serpas v. Trebucq">1 So.2d 346</a></span>, decided April 7, 1941, rehearing denied with opinion April 21, 1941, <span class="citation" data-id="3473283"><a href="/opinion/3474110/serpas-v-trebucq/" aria-description="Citation for case: Serpas v. Trebucq">1 So.2d 705</a></span>, that an unsuccessful candidate at the primary may not offer himself as a candidate at a general election, and that votes for him may not lawfully be written into the ballot or counted at such an election.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">The right to vote for a representative in Congress at the general election is, as a matter of law, thus restricted to the successful party candidate at the primary, to those not candidates at the primary who file nomination papers, and those whose names may be lawfully written into the ballot by the electors. Even if, as appellees argue, contrary to the decision in Serpas v. Trebucq, supra, voters may lawfully write into their ballots, cast at the general election, the name of a candidate rejected at the primary and have their ballots counted, the practical operation of the primary law in otherwise excluding from the ballot on the general election the names of candidates rejected at the primary is such as to impose serious restrictions upon the choice of candidates by the voters save by voting at the primary election. In fact, as alleged in the indictment, the practical operation of the primary in Louisiana, is and has been since the primary election was established in 1900 to secure the election of the Democratic primary nominee for the Second Congressional District of Louisiana.<a class="footnote" href="#fn2" id="fn2_ref">2</a></p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Interference with the right to vote in the Congressional primary in the Second Congressional District for the choice of Democratic candidate for Congress is thus as a matter of law and in fact an interference with the effective choice of the voters at the only stage of the election procedure when their choice is of significance, since it is at the only stage when such interference could have any practical effect on the ultimate result, the choice of the Congressman to represent the district. The primary in Louisiana is an integral part of the procedure for the popular choice of Congressman. The right of qualified voters to vote at the Congressional primary in Louisiana and to have their ballots counted is thus the right to participate in that choice.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">We come then to the question whether that right is one secured by the Constitution. Section 2 of Article I commands that Congressmen shall be chosen by the people of the several states by electors, the qualifications of which it prescribes. The right of the people to choose, whatever its appropriate constitutional limitations, where in other respects it is defined, and the mode of its exercise is prescribed by state action in conformity to the Cons itution, is a right established and guaranteed by the Constitution and hence is one secured by it to those citizens and inhabitants of the state entitled to exercise the right. Ex parte Yarbrough (The Ku-Klux Cases), <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 651</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">4 S.Ct. 152</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">238 U.S. 383</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>. And see Hague v. C.I.O., <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#508" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496, 508, 513, 526, 527, 529</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#960" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954, 960, 963, 969, 970</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span>, giving the same interpretation to the like phrase 'rights' 'secured by the Constitution' appearing in &#167; 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span>, <span class="citation no-link">8 U.S.C.A. &#167; 43</span>. While, in a loose sense, the right to vote for representatives in Congress is sometimes spoken of as a right derived from the states, see, Minor v. Happersett, <span class="citation" data-id="88998"><a href="/opinion/88998/minor-v-happersett/#170" aria-description="Citation for case: Minor v. Happersett">21 Wall. 162, 170</a></span>, <span class="citation" data-id="88998"><a href="/opinion/88998/minor-v-happersett/" aria-description="Citation for case: Minor v. Happersett">22 L.Ed. 627</a></span>; United States v. Reese, <span class="citation" data-id="9417037"><a href="/opinion/89266/united-states-v-reese/#217" aria-description="Citation for case: United States v. REESE">92 U.S. 214, 217, 218</a></span>, <span class="citation no-link">23 L.Ed. 563</span>; McPherson v. Blacker, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/#38" aria-description="Citation for case: McPherson v. Blacker">146 U.S. 1, 38, 39</a></span>, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/#11" aria-description="Citation for case: McPherson v. Blacker">13 S.Ct. 3, 11, 12</a></span>, <span class="citation" data-id="93413"><a href="/opinion/93413/mcpherson-v-blacker/" aria-description="Citation for case: McPherson v. Blacker">36 L.Ed. 869</a></span>; Breedlove v. Suttles, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/#283" aria-description="Citation for case: Breedlove v. Suttles">302 U.S. 277, 283</a></span>, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/#207" aria-description="Citation for case: Breedlove v. Suttles">58 S.Ct. 205, 207</a></span>, <span class="citation" data-id="102874"><a href="/opinion/102874/breedlove-v-suttles/" aria-description="Citation for case: Breedlove v. Suttles">82 L.Ed. 252</a></span>, this statement is true only in the sense that the states are authorized by the Constitution, to legislate on the subject as provided by &#167; 2 of Art. I, to the extent that Congress has not restricted state action by the exercise of its powers to regulate elections under &#167; 4 and its more general power under Article I, &#167; 8, clause 18 of the Constitution 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers'. See Ex parte Siebold, <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">100 U.S. 371</a></span>, <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">25 L.Ed. 717</a></span>; Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#664" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 663, 664</a></span>, <span class="citation no-link">4 S.Ct. 158</span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; Swafford v. Templeton, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">185 U.S. 487</a></span>, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">22 S.Ct. 783</a></span>, <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">46 L.Ed. 1005</a></span>; Wiley v. Sinkler, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/#64" aria-description="Citation for case: Wiley v. Sinkler">179 U.S. 58, 64</a></span>, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/#20" aria-description="Citation for case: Wiley v. Sinkler">21 S.Ct. 17, 20</a></span>, <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/" aria-description="Citation for case: Wiley v. Sinkler">45 L.Ed. 84</a></span>.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">Obviously included within the right to choose, secured by the Constitution, is the right of qualified voters within a state to cast their ballots and have them counted at Congressional elections. This Court has consistently held that this is a right secured by the Constitution. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> Wiley v. <span class="citation" data-id="95333"><a href="/opinion/95333/wiley-v-sinkler/" aria-description="Citation for case: Wiley v. Sinkler">Sinkler, supra;</a></span> Swafford v. <span class="citation" data-id="95662"><a href="/opinion/95662/swafford-v-templeton/" aria-description="Citation for case: Swafford v. Templeton">Templeton, supra;</a></span> United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra;</a></span> see Ex parte <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">Siebold, supra;</a></span> In re Coy, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">127 U.S. 731</a></span>, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">8 S.Ct. 1263</a></span>, <span class="citation" data-id="9417493"><a href="/opinion/92299/in-re-coy/" aria-description="Citation for case: In Re Coy">32 L.Ed. 274</a></span>; Logan v. United States, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">12 S.Ct. 617</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">36 L.Ed. 429</a></span>. And since the constitutional command is without restriction or limitation, the right unlike those guaranteed by the Fourteenth and Fifteenth Amendments, is secured against the action of individuals as well as of states. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> Logan v. United States, supra.</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">But we are now concerned with the question whether the right to choose at a primary election, a candidate for election as representative, is embraced in the right to choose representatives secured by Article I, &#167; 2. We may assume that the framers of the Constitution in adopting that section, did not have specifically in mind the selection and elimination of candidates for Congress by the direct primary any more than they contemplated the application of the commerce clause to interstate telephone, telegraph and wireless communication which are concededly within it. But in determining whether a provision of the Constitution applies to a new subject matter, it is of little significance that it is one with which the framers were not familiar. For in setting up an enduring framework of government they undertook to carry out for the indefinite future and in all the vicissitudes of the changing affairs of men, those fundamental purposes which the instrument itself discloses. Hence we read its words, not as we read legislative codes which are subject to continuous revision with the changing course of events, but as the revelation of the great purposes which were intended to be achieved by the Constitution as a continuing instrument of government. Cf. Davidson v. New Orleans, <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">96 U.S. 97</a></span>, <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/" aria-description="Citation for case: Davidson v. New Orleans">24 L.Ed. 616</a></span>; Brown v. Walker, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#595" aria-description="Citation for case: Brown v. Walker">161 U.S. 591, 595</a></span>, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#646" aria-description="Citation for case: Brown v. Walker">16 S.Ct. 644, 646</a></span>, <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">40 L.Ed. 819</a></span>; Robertson v. Baldwin, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/#281" aria-description="Citation for case: Robertson v. Baldwin">165 U.S. 275, 281, 282</a></span>, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/#328" aria-description="Citation for case: Robertson v. Baldwin">17 S.Ct. 326, 328, 329</a></span>, <span class="citation" data-id="9417756"><a href="/opinion/94602/robertson-v-baldwin/" aria-description="Citation for case: Robertson v. Baldwin">41 L.Ed. 715</a></span>. If we r member that 'it is a Constitution we are expounding', we cannot rightly prefer, of the possible meanings of its words, that which will defeat rather than effectuate the Constitutional purpose.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">That the free choice by the people of representatives in Congress, subject only to the restrictions to be found in &#167;&#167; 2 and 4 of Article I and elsewhere in the Constitution, was one of the great purposes of our Constitutional scheme of government cannot be doubted. We cannot regard it as any the less the constitutional purpose or its words as any the less guarantying the integrity of that choice when a state, exercising its privilege in the absence of Congressional action, changes the mode of choice from a single step, a general election, to two, of which the first is the choice at a primary of those candidates from whom, as a second step, the representative in Congress is to be chosen at the election.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">Nor can we say that that choice which the Constitution protects is restricted to the second step because &#167; 4 of Article I, as a means of securing a free choice of representatives by the people, has authorized Congress to regulate the manner of elections, without making any mention of primary elections. For we think that the authority of Congress, given by &#167; 4, includes the authority to regulate primary elections when, as in this case, they are a step in the exercise by the people of their choice of representatives in Congress. The point whether the power conferred by &#167; 4 includes in any circumstances the power to regulate primary elections was reserved in United States v. <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra,</a></span> <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 487</a></span>, <span class="citation no-link">37 S.Ct. 411</span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>. In Newberry v. United States, supra, four Justices of this Court were of opinion that the term 'elections' in &#167; 4 of Article I did not embrace a primary election since that procedure was unknown to the framers. A fifth Justice who with them pronounced the judgment of the Court, was of opinion that a primary, held under a law enacted before the adoption of the Seventeenth Amendment, for the nomination of candidates for Senator, was not an election within the meaning of &#167; 4 of Article I of the Constitution, presumably because the choice of the primary imposed no legal restrictions on the election of Senators by the state legislatures to which their election had been committed by Article I, &#167; 3. The remaining four Justices were of the opinion that a primary election for the choice of candidates for Senator or Representative were elections subject to regulation by Congress within the meaning of &#167; 4 of Article I. The question then has not been prejudged by any decision of this Court.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">To decide it we turn to the words of the Constitution read in their historical setting as revealing the purpose of its framers, and in search for admissible meanings of its words which, in the circumstances of their application, will effectuate those purposes. As we have said, a dominant purpose of &#167; 2, so far as the selection of representatives in Congress is concerned, was to secure to the people the right to choose representatives by the designated electors, that is to say, by some form of election. Cf. the Seventeenth Amendment as to popular 'election' of Senators. From time immemorial an election to public office has been in point of substance no more and no less than the expression by qualified electors of their choice of candidates.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">Long before the adoption of the Constitution the form and mode of that expression had changed from time to time. There is no historical warrant for supposing that the framers were under the illusion that the method of effecting the choice of the electors would never change or that if it did, the change was for that reason to be permitted to defeat the right of the people to choose representatives for Congress which the Constitution had guaranteed. The right to participate in the choice of representatives for Congress includes, as we have said, the right to cast a ballot and to have it counted at the general el ction whether for the successful candidate or not. Where the state law has made the primary an integral part of the procedure of choice, or where in fact the primary effectively controls the choice, the right of the elector to have his ballot counted at the primary, is likewise included in the right protected by Article I, &#167; 2. And this right of participation is protected just as is the right to vote at the election, where the primary is by law made an integral part of the election machinery, whether the voter exercises his right in a party primary which invariably, sometimes or never determines the ultimate choice of the representative. Here, even apart from the circumstance that the Louisiana primary is made by law an integral part of the procedure of choice, the right to choose a representative is in fact controlled by the primary because, as is alleged in the indictment, the choice of candidates at the Democratic primary determines the choice of the elected representative. Moreover, we cannot close our eyes to the fact already mentioned that the practical influence of the choice of candidates at the primary may be so great as to affect profoundly the choice at the general election even though there is no effective legal prohibition upon the rejection at the election of the choice made at the primary and may thus operate to deprive the voter of his constitutional right of choice. This was noted and extensively commented upon by the concurring Justices in Newberry v. United States, supra, 256 U.S. 263&#8212;269, 285, 287, <span class="citation no-link">41 S.Ct. 476</span> 478, 484, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Unless the constitutional protection of the integrity of 'elections' extends to primary elections, Congress is left powerless to effect the constitutional purpose, and the popular choice of representatives is stripped of its constitutional protection save only as Congress, by taking over the control of state elections, may exclude from them the influence of the state primaries.<a class="footnote" href="#fn3" id="fn3_ref">3</a> Such an expedient would end that state autonomy with respect to elections which the Constitution contemplated that Congress should be free to leave undisturbed, subject only to such minimum regulation as it should find necessary to insure the freedom and integrity of the choice. Words, especially those of a constitution, are not to be read with such stultifying narrowness. The words of &#167;&#167; 2 and 4 of Article I, read in the sense which is plainly permissible and in the light of the constitutional purpose, require us to hold that a primary election which involves a necessary step in the choice of candidates for election as representatives in Congress, and which in the circumstances of this case controls that choice, is an election within the meaning of the constitutional provision and is subject to congressional regulation as to the manner of holding it.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Not only does &#167; 4 of Article I authorize Congress to regulate the manner of holding elections, but by Article I, &#167; 8, Clause 18, Congress is given authority 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.' This provision leaves to the Congress the choice of means by which its constitutional powers are to be carried into execution. 'L t the end be legitimate, let it be within the scope of the constitution, and all means which are appropriate, which are plainly adapted to that end, which are not prohibited, but consist with the letter and spirit of the constitution, are constitutional'. McCulloch v. Maryland, <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/#421" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 Wheat. 316, 421</a></span>, <span class="citation" data-id="85272"><a href="/opinion/85272/mculloch-v-state-of-maryland/" aria-description="Citation for case: M&#x27;culloch v. State of Maryland">4 L.Ed. 579</a></span>. That principle has been consistently adhered to and liberally applied, and extends to the congressional power by appropriate legislation to safeguard the right of choice by the people of representatives in Congress secured by &#167; 2 of Article I. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#658" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 657, 658</a></span>, <span class="citation no-link">4 S.Ct. 154</span>, 155, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>; cf. Second Employers' Liability Cases, (Mondou v. New York, N.H. &amp; H.R. Co.), <span class="citation" data-id="98132"><a href="/opinion/98132/miller-v-united-states/#49" aria-description="Citation for case: Miller v. United States">233 U.S. 1, 49</a></span>, <span class="citation" data-id="8142543"><a href="/opinion/8180624/mondou-v-new-york-new-haven-hartford-railroad/#174" aria-description="Citation for case: Mondou v. New York, New Haven &amp; Hartford Railroad">32 S.Ct. 169, 174</a></span>, <span class="citation" data-id="2620807"><a href="/opinion/2620807/second-employersliability-cases/" aria-description="Citation for case: Second Employers&#x27;liability Cases">56 L.Ed. 327</a></span>, 38 L.R.A.,N.S., 44; Houston &amp; Texas Ry. Co. v. United States, <span class="citation" data-id="98232"><a href="/opinion/98232/houston-east-west-texas-railway-co-v-united-states/#350" aria-description="Citation for case: Houston, East &amp; West Texas Railway Co. v. United States">234 U.S. 342, 350, 355</a></span>, <span class="citation" data-id="98232"><a href="/opinion/98232/houston-east-west-texas-railway-co-v-united-states/#835" aria-description="Citation for case: Houston, East &amp; West Texas Railway Co. v. United States">34 S.Ct. 833, 835, 838</a></span>, <span class="citation no-link">58 L.Ed. 341</span>; Wilson v. New et al., <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/#346" aria-description="Citation for case: Wilson v. New">243 U.S. 332, 346, 347</a></span>, <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/#301" aria-description="Citation for case: Wilson v. New">37 S.Ct. 298, 301</a></span>, <span class="citation" data-id="9418322"><a href="/opinion/98903/wilson-v-new/" aria-description="Citation for case: Wilson v. New">61 L.Ed. 755</a></span>, L.R.A.1917E, 938, Ann.Cas.1918A, 1024; First National Bank v. Union Trust Company, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/#419" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">244 U.S. 416, 419</a></span>, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/#735" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">37 S.Ct. 734, 735</a></span>, <span class="citation" data-id="9418334"><a href="/opinion/98985/first-national-bank-v-fellows-ex-rel-union-trust-co/" aria-description="Citation for case: First National Bank v. Fellows Ex Rel. Union Trust Co.">61 L.Ed. 1233</a></span>, L.R.A.1918C, 283, Ann.Cas.1918D, 1169; Selective Draft Cases, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/#381" aria-description="Citation for case: Selective Draft Law Cases">245 U.S. 366, 381</a></span>, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/#162" aria-description="Citation for case: Selective Draft Law Cases">38 S.Ct. 159, 162</a></span>, <span class="citation" data-id="99053"><a href="/opinion/99053/selective-draft-law-cases/" aria-description="Citation for case: Selective Draft Law Cases">62 L.Ed. 349</a></span>, L.R.A.1918C, 361, Ann.Cas.1918B, 856; United States v. Ferger et al., <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/#205" aria-description="Citation for case: United States v. Ferger">250 U.S. 199, 205</a></span>, <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/#446" aria-description="Citation for case: United States v. Ferger">39 S.Ct. 445, 446</a></span>, <span class="citation" data-id="99412"><a href="/opinion/99412/united-states-v-ferger/" aria-description="Citation for case: United States v. Ferger">63 L.Ed. 936</a></span>; Hamilton v. Kentucky Distilleries Co., <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/#155" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">251 U.S. 146, 155, 163</a></span>, <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/#107" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">40 S.Ct. 106, 107, 110</a></span>, <span class="citation" data-id="99481"><a href="/opinion/99481/hamilton-v-kentucky-distilleries-warehouse-co/" aria-description="Citation for case: Hamilton v. Kentucky Distilleries &amp; Warehouse Co.">64 L.Ed. 194</a></span>; Jacob Ruppert v. Caffey, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">251 U.S. 264</a></span>, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">40 S.Ct. 141</a></span>, <span class="citation" data-id="99495"><a href="/opinion/99495/jacob-ruppert-v-caffey/" aria-description="Citation for case: Jacob Ruppert v. Caffey">64 L.Ed. 260</a></span>; Smith v. Kansas City Title &amp; Trust Co., <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">255 U.S. 180</a></span>, <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">41 S.Ct. 243</a></span>, <span class="citation" data-id="9418449"><a href="/opinion/99730/smith-v-kansas-city-title-trust-co/" aria-description="Citation for case: Smith v. Kansas City Title &amp; Trust Co.">65 L.Ed. 577</a></span>; United States v. Darby, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">312 U.S. 100</a></span>, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">61 S.Ct. 451</a></span>, 85 L.Ed. &#8212;-, <span class="citation no-link">132 A.L.R. 1430</span>, decided February 3, 1941, and cases cited.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">There remains the question whether &#167;&#167; 19 and 20 are an exercise of the congressional authority applicable to the acts with which appellees are charged in the indictment. Section 19 makes it a crime to conspire to 'injure' or 'oppress' any citizen 'in the free exercise * * * of any right or privilege secured to him by the Constitution'.<a class="footnote" href="#fn4" id="fn4_ref">4</a> In Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> and in United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra,</a></span> as we have seen, it was held that the right to vote in a congressional election is a right secured by the Constitution, and that a conspiracy to prevent the citizen from voting or to prevent the official count of his ballot when cast, is a conspiracy to injure and oppress the citizen in the free exercise of a right secured by the Constitution within the meaning of &#167; 19. In reaching this conclusion the Court found no uncertainty or ambiguity in the statutory language, obviously devised to protect the citizen 'in the free exercise * * * of any right or privilege secured to him by the Constitution', and concerned itself with the question whether the right to participate in choosing a representative is so secured.<a class="footnote" href="#fn5" id="fn5_ref">5</a> Such is our function here. Conspiracy to prevent the official count of a citizen's ballot, held in United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra,</a></span> to be a violation of &#167; 19 in the case of a congressional election, is equally a conspiracy to injure and oppress the citizen when the ballots are cast in a primary election prerequisite to the choice of party candidates for a congressional election. In both cases the right infringed is one secured by the Constitution. The injury suffered by the citizen in the exercise of the right is an injury which the statute describes and to which it applies in the one case as in the other.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">The suggestion that &#167; 19, concededly applicable to conspiracies to deprive electors of their votes at congressional elections, is not sufficiently specific to be deemed applicable to primary elections, will hardly bear examination. Section 19 speaks neither of elections nor of primaries. In unambiguous language it protects 'any right or privilege secured * * * by the Constitution', a phrase which as we have seen extends to the right of the voter to have his vote counted in both the general election and in the primary election, where the latter is a part of the election machinery, as well as to numerous other constitutional rights which are wholly unrelated to the choice of a representative in Congress. United States v. Waddell, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">112 U.S. 76</a></span>, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">5 S.Ct. 35</a></span>, <span class="citation" data-id="91179"><a href="/opinion/91179/united-states-v-waddell/" aria-description="Citation for case: United States v. Waddell">28 L.Ed. 673</a></span>; Logan v. United States, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">12 S.Ct. 617</a></span>, <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">36 L.Ed. 429</a></span>; In re Quarles, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">158 U.S. 532</a></span>, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">15 S.Ct. 959</a></span>, <span class="citation" data-id="94235"><a href="/opinion/94235/in-re-quarles-and-butler/" aria-description="Citation for case: In Re Quarles and Butler">39 L.Ed. 1080</a></span>; Motes v. United States, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">178 U.S. 458</a></span>, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">20 S.Ct. 993</a></span>, <span class="citation" data-id="95317"><a href="/opinion/95317/motes-v-united-states/" aria-description="Citation for case: Motes v. United States">44 L.Ed. 1150</a></span>; Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124.</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">In the face of the broad language of the statute, we are pointed to no principle of statutory construction and to no significant legislative history which could be thought to sanction our saying that the statute applies any the less to primaries than to elections, where in one as in the other it is the same constitutional right which is infringed. It does not avail to attempt to distinguish the protection afforded by &#167; 1 of the Civil Rights Act of 1871,<a class="footnote" href="#fn6" id="fn6_ref">6</a> to the right to participate in primary as well as general elections, secured to all citizens by the Constitution, see Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124; Nixon v. Herndon, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">273 U.S. 536</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">47 S.Ct. 446</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">71 L.Ed. 759</a></span>; Nixon v. Condon, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">286 U.S. 73</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">52 S.Ct. 484</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">76 L.Ed. 984</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">88 A.L.R. 458</a></span>; Lane v. Wilson, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">307 U.S. 268</a></span>, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">59 S.Ct. 872</a></span>, <span class="citation" data-id="103213"><a href="/opinion/103213/lane-v-wilson/" aria-description="Citation for case: Lane v. Wilson">83 L.Ed. 1281</a></span>, on the ground that in those cases the injured citizens were Negroes whose rights were clearly protected by the Fourteenth Amendment. At least since Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra,</a></span> and no member of the Court seems ever to have questioned it, the right to participate in the choice of representatives in Congress has been recognized as a right protected by Art. I, &#167;&#167; 2 and 4 of the Constitution.<a class="footnote" href="#fn7" id="fn7_ref">7</a> Differences of opinion have arisen as to the effect of the primary in particular cases on the choice of representatives. But we are troubled by no such doubt here. Hence, the right to participate through the primary in the choice of representatives in Congress&#8212;a right clearly secured by the Constitution&#8212;is within the words and purpose of &#167; 19 in the same manner and to the same extent as the right to vote at the general election. United States v. <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">Mosley, supra.</a></span> It is no extension of the criminal statute, as it was not of the civil statute in Nixon v. <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">Herndon, supra,</a></span> to find a violation of it in a new method of interference with the right which its words protect. For it is the constitutional right, regardless of the method of interference, which is the subject of the statute and which in precise terms it protects from injury and oppression.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">It is hardly the performance of the judicial function to construe a statute, which in terms protects a right secured by the Constitution, here the right to choose a representative in Congress, as applying to an election whose only function is to ratify a choice already made at the primary but as having no application to the primary which is the only effective means of choice. To withdraw from the scope of the statute, an effective interference with the constitutional right of choice, because other wholly different situations not now before us may not be found to involve such an interference, cf. United States v. Bathgate, <span class="citation" data-id="1087873"><a href="/opinion/1087873/united-states-v-bathgate/" aria-description="Citation for case: United States v. Bathgate">246 U.S. 220</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">38 S.Ct. 269</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>; United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, is to say that acts plainly within the statute should be deemed to be without it because other hypothetical cases may later be found not to infringe the constitutional right with which alone the statute is concerned.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">If a right secured by the Constitution may be infringed by the corrupt failure to include the vote at a primary in the official count, it is not significant that the primary, like the voting machine, was unknown when &#167; 19 was adopted.<a class="footnote" href="#fn8" id="fn8_ref">8</a> Abuse of either may infringe the right and therefore violate &#167; 19. See United States v. Pleva, 2 Cir., <span class="citation" data-id="9639102"><a href="/opinion/1488148/united-states-v-pleva/#530" aria-description="Citation for case: United States v. Pleva">66 F.2d 529, 530</a></span>; cf. Browder v. United States, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/" aria-description="Citation for case: Browder v. United States">312 U.S. 335</a></span>, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/" aria-description="Citation for case: Browder v. United States">61 S.Ct. 599</a></span>, 85 L.Ed. &#8212;-. Nor does the fact that in circumstances not here present there may be difficulty in determining whether the primary so affects the right of the choice as to bring it within the constitutional protection, afford any ground for doubting the construction and application of the statute once the constitutional question is resolved. That difficulty is inherent in the judicial administration of every federal criminal statute, for none, whatever its terms, can be applied beyond the reach of the congressional power which the Constitution confers. Standard Sanitary Mfg. Co. v. United States, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">226 U.S. 20</a></span>, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">33 S.Ct. 9</a></span>, <span class="citation" data-id="97691"><a href="/opinion/97691/standard-sanitary-manufacturing-co-v-united-states/" aria-description="Citation for case: Standard Sanitary Manufacturing Co. v. United States">57 L.Ed. 107</a></span>; Hoke v. United States, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">227 U.S. 308</a></span>, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">33 S.Ct. 281</a></span>, <span class="citation" data-id="97782"><a href="/opinion/97782/hoke-economides-v-united-states/" aria-description="Citation for case: Hoke &amp; Economides v. United States">57 L.Ed. 523</a></span>, 43 L.R.A.,N.S., 906, Ann.Cas.1913E, 905; Nash v. United States, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">229 U.S. 373</a></span>, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">33 S.Ct. 780</a></span>, <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/" aria-description="Citation for case: Nash v. United States">57 L.Ed. 1232</a></span>; United States v. Freeman, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">239 U.S. 117</a></span>, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">36 S.Ct. 32</a></span>, <span class="citation" data-id="98558"><a href="/opinion/98558/united-states-v-freeman/" aria-description="Citation for case: United States v. Freeman">60 L.Ed. 172</a></span>; United States v. F. W. Darby, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">312 U.S. 100</a></span>, <span class="citation" data-id="103442"><a href="/opinion/103442/united-states-v-darby/" aria-description="Citation for case: United States v. Darby">61 S.Ct. 451</a></span>, 85 L.Ed. &#8212;-, <span class="citation no-link">132 A.L.R. 1430</span>, decided February 3, 1941.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">The right of the voters at the primary to have their votes counted is, as we have stated, a right or privilege secured by the Constitution, and to this &#167; 20 also gives protection.<a class="footnote" href="#fn9" id="fn9_ref">9</a> The alleged acts of appellees were committed in the course of their performance of duties unde  the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election. Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law. Ex parte Virginia, <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339, 346</a></span>, <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">25 L.Ed. 676</a></span>; Home Telephone &amp; Telegraph Co. v. Los Angeles, <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#287" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U.S. 278, 287</a></span>, et seq., <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/#314" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">33 S.Ct. 312, 314</a></span>, <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">57 L.Ed. 510</a></span>; Hague v. C.I.O., <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#507" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">307 U.S. 496, 507, 519</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/#960" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">59 S.Ct. 954, 960, 965</a></span>, <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">83 L.Ed. 1423</a></span>; cf. <span class="citation" data-id="9419051"><a href="/opinion/103226/haguer-v-committee-for-industrial-organization/" aria-description="Citation for case: Haguer v. Committee for Industrial Organization">Id.,</a></span> 3 Cir., <span class="citation" data-id="9640063"><a href="/opinion/1494037/hague-v-committee-for-industrial-organization/#790" aria-description="Citation for case: Hague v. Committee for Industrial Organization">101 F.2d 774, 790</a></span>. Here the acts of appellees infringed the constitutional right and deprived the voters of the benefit of it within the meaning of &#167; 20, unless by its terms its application is restricted to deprivations 'on account of (an) inhabitant being an alien, or by reason of his color, or race'.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">The last clause of &#167; 20 protects inhabitants of a state from being subjected to different punishments, pains or penalties by reason of alienage, color or race, than are prescribed for the punishment of citizens. That the qualification with respect to alienage, color and race, refers only to differences in punishment and not to deprivations of any rights or privileges secured by the Constitution, is evidenced by the structure of the section and the necessities of the practical application of its provisions. The qualification as to alienage, color and race, is a parenthetical phrase in the clause penalizing different punishments 'than are prescribed for * * * citizens' and in the common use of language could refer only to the subject matter of the clause and not to that of the earlier one relating to the deprivation of rights to which it makes no reference in terms.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">Moreover the prohibited differences of punishment on account of alienage, color or race, are those referable to prescribed punishments which are to be compared with those prescribed for citizens. A standard is thus set up applicable to differences in prescribed punishments on account of alienage, color or race, which it would be difficult if not impossible to apply to the willful deprivations of constitutional rights or privileges, in order to determine whether they are on account of alienage, color or race. We think that &#167; 20 authorizes the punishment of two different offenses. The one is willfully subjecting any inhabitant to the deprivation of rights secured by the Constitution; the other is willfully subjecting any inhabitant to different punishments on account of his color or race, than are prescribed for the punishment of citizens. The meager legislative history of the section supports this conclusion.<a class="footnote" href="#fn10" id="fn10_ref">10</a></p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">So interpreted &#167; 20 applies to deprivation of the constitutional rights of qualified voters to choose representatives in Congress. The generality of the section made applicable as it is to deprivations of any constitutional right, does not obscure its meaning or impair its force within the scope of its application, which is restricted by its terms to deprivations which are willfully inflicted by those acting under color of any law, statute and the like.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">We do not discuss the application of &#167; 20 to deprivations of the right to equal protection of the laws guaranteed by the Fourteenth Amendment, a point apparently raised and discussed for the first time in the Government's brief in this Court. The point was not specially considered or decided by the court below, and has not been assigned as error by the Government. Since the indictment on its face does not purport to charge a deprivation of equal protection to voters or candidates, we are not called upon to construe the indictment in order to raise a question of statutory validity or construction which we are alone authorized to review upon this appeal.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">Reversed.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">The Chief Justice took no part in the consideration or decision of this case.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">Mr. Justice DOUGLAS, dissenting.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">Free and honest elections are the very foundation of our republican form of government. Hence any attempt to defile the sanctity of the ballot cannot be viewed with equanimity. As stated by Mr. Justice Miller in Ex parte Yarbrough (The Ku-Klux Cases), <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#666" aria-description="Citation for case: Ex Parte Yarbrough">110 U.S. 651, 666</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/#159" aria-description="Citation for case: Ex Parte Yarbrough">4 S.Ct. 152, 159</a></span>, <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">28 L.Ed. 274</a></span>, 'the temptations to control these elections by violence and by corruption' have been a constant source of danger in the history of all republics. The acts here charged, if proven, are of a kind which carries that threat and are highly offensive. Since they corrupt the process of Congressional elections, they transcend mere local concern and extend a contaminating influence into the national domain.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">I think Congress has ample power to deal with them. That is to say I disagree with Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>, to the extent that it holds that Congress has no power to control primary elections. Art. I, &#167; 2 of the Constitution provides that 'The House of Representatives shall be composed of Members chosen every second Year by the People of the several States.' Art. I, &#167; 4 provides that 'The Times, Places and Manner of holding Elections for Senators and Representatives, shall be prescribed in each State by the Legislature thereof; but the Congress may at any time by Law make or alter such Regulations, except as to the Places of chusing Senators.' And Art. I, &#167; 8, clause 18 gives Congress the power 'To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.' Those sections are an arsenal of power ample to protect Congressional elections from any and all forms of pollution. The fact that a particular form of pollution has only an indirect effect on the final election is immaterial. The fact that it occurs in a primary election or nominating convention is likewise irrelevant. The important consideration is that the Constitution should be interpreted broadly so as to give to the representatives of a free people abundant power to deal with all the exigencies of the electoral process. It means that the Constitution should be read so as to give Congress an expansive implied power to place beyond the pale acts which, in their direct or indirect effect, impair the integrity of Congressional elections. For when corruption enters, the election is no longer free, the choice of the people is affected. To hold that Congress is powerless to control these primaries would indeed be a narrow construction of the Constitution inconsistent with the view that that instrument of government was designed not only for contemporary needs but for the vicissitudes of time.</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">So I agree with most of the views expressed in the opinion of the Court. And it is with diffidence that I dissent from the result there reached.</p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">The disagreement centers on the meaning of &#167; 19 of the Criminal Code which protects every right secured by the Constitution. The right to vote at a final Congressional election and the right to have one's vote counted in such an election have been held to be protected by &#167; 19. Ex parte <span class="citation" data-id="91064"><a href="/opinion/91064/ex-parte-yarbrough/" aria-description="Citation for case: Ex Parte Yarbrough">Yarbrough, supra;</a></span> United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">238 U.S. 383</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>. Yet I do not think that the principles of those cases should be, or properly can be, extended to primary elections. To sustain this indictment we must so extend them. But when we do, we enter perilous territory.</p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">We enter perilous territory because, as stated in United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#485" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476, 485</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/#410" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407, 410</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, there is no common law offense against the United States; 'the legislative authority of the Union must first make an act a crime, affix a punishment to it, and declare the Court that shall have jurisdiction of the offence.' United States v. Hudson, <span class="citation" data-id="84968"><a href="/opinion/84968/the-united-states-v-hudson-and-goodwin/#34" aria-description="Citation for case: The United States v. Hudson and Goodwin">7 Cranch 32, 34</a></span>, <span class="citation" data-id="84968"><a href="/opinion/84968/the-united-states-v-hudson-and-goodwin/" aria-description="Citation for case: The United States v. Hudson and Goodwin">3 L.Ed. 259</a></span>. If a person is to be convicted of a crime, the offense must be clearly and plainly embraced within the statute. As stated by Chief Justice Marshall in United States v. Wiltberger, <span class="citation" data-id="6607979"><a href="/opinion/6726712/united-states-v-wiltberger/#105" aria-description="Citation for case: United States v. Wiltberger">5 Wheat. 76, 105</a></span>, <span class="citation" data-id="6607979"><a href="/opinion/6726712/united-states-v-wiltberger/" aria-description="Citation for case: United States v. Wiltberger">5 L.Ed. 37</a></span>, 'probability is not a guide which a court, in construing a penal statute, can safely take.' It is one thing to allow wide and generous scope to the express and implied powers of Congress; it is distinctly another to read into the vague and general language of an act of Congress specifications of crimes. We should ever be mindful that 'before a man can be punished, his case must be plainly and unmistakably within the statute.' United States v. Lacher, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/#628" aria-description="Citation for case: United States v. Lacher">134 U.S. 624, 628</a></span>, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/#626" aria-description="Citation for case: United States v. Lacher">10 S.Ct. 625, 626</a></span>, <span class="citation" data-id="92761"><a href="/opinion/92761/united-states-v-lacher/" aria-description="Citation for case: United States v. Lacher">33 L.Ed. 1080</a></span>. That admonition is reemphasized here by the fact that &#167; 19 imposes not only a fine of $5,000 and ten years in prison but also makes him who is convicted 'ineligible to any office, or place of honor, profit, or trust created by the Constitution or laws of the United States.' It is not enough for us to find in the vague penumbra of a statute some offense about which Congress could have legislated and then to particularize it as a crime because it is highly offensive. Cf. James v. Bowman, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">190 U.S. 127</a></span>, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">23 S.Ct. 678</a></span>, <span class="citation" data-id="95887"><a href="/opinion/95887/james-v-bowman/" aria-description="Citation for case: James v. Bowman">47 L.Ed. 979</a></span>. Civil liberties are too dear to permit conviction for crimes which are only implied and which can be spelled out only by adding inference to inference.</p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">Sec. 19 does not purport to be an exercise by Congress of its power to regulate primaries. It merely penalizes conspiracies 'to injure, oppress, threaten, or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States'. Thus, it does no more than refer us to the Constitution<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> for the purpose of determining whether or not the right to vote in a primary is there secured. Hence we must do more than find in the Constitution the power of Congress to afford that protection. We must find that protection on the face of the Constitution itself. That is to say, we must in view of the wording of &#167; 19 read the relevant provisions of the Constitution for the purposes of this case through the window of a criminal statute.</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p class="indent">There can be put to one side cases where state election officials deprive negro citizens of their right to vote at a general election (Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124), or at a primary. Nixon v. Herndon, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">273 U.S. 536</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">47 S.Ct. 446</a></span>, <span class="citation" data-id="101032"><a href="/opinion/101032/nixon-v-herndon/" aria-description="Citation for case: Nixon v. Herndon">71 L.Ed. 759</a></span>; Nixon v. Condon, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">286 U.S. 73</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">52 S.Ct. 484</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">76 L.Ed. 984</a></span>, <span class="citation" data-id="9841924"><a href="/opinion/101911/nixon-v-condon/" aria-description="Citation for case: Nixon v. Condon">88 A.L.R. 458</a></span>. Discrimination on the basis of race or color is plainly outlawed by the Fourteenth Amendment. Since the constitutional mandate is plain, there is no reason why &#167; 19 or &#167; 20 should not be applicable. But the situation here is quite different. When we turn to the constitutional provisions relevant to this case we find no such unambiguous mandate.</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent">Art. I, &#167; 4 specifies the machinery whereby the times, places and manner of holding elections shall be established and controlled. Art. I, &#167; 2 provides that representatives shall be 'chosen' by the people. But for purposes of the criminal law as contrasted to the interpretation of the Constitution as the source of the implied power of Congress, I do not  hink that those provisions in absence of specific legislation by Congress protect the primary election or the nominating convention. While they protect the right to vote and the right to have one's vote counted at the final election as held in the Yarbrough and Mosley cases, they certainly do not per se extend to all acts which is their indirect or incidental effect restrain, restrict, or interfere with that choice. Bribery of voters at a general election certainly is an interference with that freedom of choice. It is a corruptive influence which for its impact on the election process is as intimate and direct as the acts charged in this indictment. And Congress has ample power to deal with it. But this Court in United States v. Bathgate, <span class="citation" data-id="1087873"><a href="/opinion/1087873/united-states-v-bathgate/" aria-description="Citation for case: United States v. Bathgate">246 U.S. 220</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">38 S.Ct. 269</a></span>, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>, by a unanimous vote, held that conspiracies to bribe voters at a general election were not covered by &#167; 19. While the conclusion in that case may be reconciled with the results in the Yarbrough and Mosley cases on the ground that the right to vote at a general election is personal while the bribery of voters only indirectly affects that personal right, that distinction is not of aid here. For the failure to count votes cast at a primary has by the same token only an indirect effect on the voting at the general election. In terms of causal effect tampering with the primary vote may be as important on the outcome of the general election as bribery of voters at the general election itself. Certainly from the viewpoint of the individual voter there is as much a dilution of his vote in the one case as in the other. So, in light of the Mosley and Bathgate cases, the test under &#167; 19 is not whether the acts in question constitute an interference with the effective choice of the voters. It is whether the voters are deprived of their votes in the general election. Such a test comports with the standards for construction of a criminal law, since it restricts &#167; 19 to protection of the rights plainly and directly guaranteed by the Constitution. Any other test entails an inquiry into the indirect or incidental effect on the general election of the acts done. But in view of the generality of the words employed such a test would be incompatible with the criteria appropriate for a criminal case.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The Mosley case, in my view, went to the verge when it held that &#167; 19 and the relevant constitutional provisions made it a crime to fail to count votes cast at a general election. That Congress intended &#167; 19 to have that effect was none too clear. The dissenting opinion of Mr. Justice Lamar in that case points out that &#167; 19 was originally part of the Enforcement Act of May 31, 1870, c. 114, &#167; 6, <span class="citation no-link">16 Stat. 140</span>. Under another section of that act (&#167; 4), which was repealed by the Act of February 8, 1894 (<span class="citation no-link">28 Stat. 36</span>) the crime charged in the Mosley case would have been punishable by a fine of not less than $500 and imprisonment for 12 months.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> Under &#167; 19 it carried, as it still does, a penalty of $5000 and ten years in prison. The Committee Report (H.Rep. No. 18, 53d Cong., 1st Sess.) which recommended the repeal of other sections clearly indicated an intent to remove the hand of the Federal Government from such elections and to restore their conduct and policing to the states. As the Report stated (p. 7): 'Let every trace of the reconstruction measures be wiped from the statute books; let the States of this great Union understand that the elections are in their own hands, and if there be fraud, coercion, or force used they will be the first to feel it. Responding to a universal sentiment throughout the country for greater purity in elections many of our States have enacted laws to protect the voter and to purify the ballot. These, under the guidance of State officers, have worked efficiently, satisfactorily, and beneficently; and if these Federal statutes are repealed that sentiment will receive an impetus which, if the cause still exists, will carry such enactments in every State in the Union.' I  view of this broad, comprehensive program of repeal it is not easy to conclude that the general language of &#167; 19 which was not repealed not only continued in effect much which had been repealed but also upped the penalties for certain offenses which had been explicitly covered by one of the repealed sections. Mr. Justice Holmes, writing for the majority in the Mosley case, found in the legislative and historical setting of &#167; 19 and in its revised form a Congressional interpretation which, if &#167; 19 were taken at its face value, was thought to afford voters in final Congressional elections general protection. And that view is a tenable one since &#167; 19 originally was part of an Act regulating general elections and since the acts charged had a direct rather than an indirect effect on the right to vote at a general election.</p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">But as stated by a unanimous court in United States v. <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra,</a></span> 243 U.S. page 486, 37 S.Ct. page 411, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>, the Mosley case 'falls far short' of making &#167; 19 'applicable to the conduct of a state nominating primary'. Indeed, Mr. Justice Holmes, the author of the Mosley opinion, joined with Mr. Justice McReynolds in the Newberry case in his view that Congress had no authority under Art. I, &#167; 4 of the Constitution of legislate on primaries. When &#167; 19 was part of the Act of May 31, 1870, it certainly would never have been contended that it embraced primaries, for they were hardly known at that time.<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a> It is true that 'even a criminal statute embraces everything which subsequently falls within its scope.' Browder v. United States, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/#340" aria-description="Citation for case: Browder v. United States">312 U.S. 335, 340</a></span>, <span class="citation" data-id="103462"><a href="/opinion/103462/browder-v-united-states/#602" aria-description="Citation for case: Browder v. United States">61 S.Ct. 599, 602</a></span>, 85 L.Ed. &#8212;-. Yet the attempt to bring under &#167; 19 offenses 'committed in the conduct of primary elections or nominating caucuses or conventions' was rejected in the Gradwell case, where this Court said that in absence of legislation by Congress on the subject of primaries it is not for the courts 'to attempt to supply it by stretching old statutes to new uses, to which they are not adapted and for which they were not intended. * * * the section of the Criminal Code relied upon, originally enacted for the protection of the civil rights of the then lately enfranchised negro, cannot be extended so as to make it an agency for enforcing a state primary law.' 243 U.S. pages 488, 489, 37 S.Ct. page 411, 412, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>. The fact that primaries were hardly known when &#167; 19 was enacted, the fact that it was part of a legislative program governing general elections not primary elections, the fact that it has been in nowise implemented by legislation directed at primaries give credence to the unanimous view in the Gradwell case that &#167; 19 has not by the mere passage of time taken on a new and broadened meaning. At least it seems plain that the difficulties of applying the historical reason adduced by Mr. Justice Holmes in the Mosley case to bring general elections within &#167; 19 are so great in case of primaries that we have left the safety zone of interpretation of criminal statutes when we sustain this indictment. It is one thing to say, as in the Mosley case, that Congress was legislating as respects general elections when it passed &#167; 19. That was the fact. It is qu te another thing to say that Congress by leaving &#167; 19 unmolested for some seventy years has legislated unwittingly on primaries. Sec. 19 was never part of an act of Congress directed towards primaries. That was not its original frame of reference. Therefore, unlike the Mosley case, it cannot be said here that &#167; 19 still covers primaries because it was once an integral part of primary legislation.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">Furthermore, the fact that Congress has legislated only sparingly and at infrequent intervals even on the subject of general elections (United States v <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">Gradwell, supra)</a></span> should make us hesitate to conclude that by mere inaction Congress has taken the greater step, entered the field of primaries, and gone further than any announced legislative program has indicated. The acts here charged constitute crimes under the Louisiana statute. La.Act No. 46, Reg.Sess.1940, &#167; 89. In absence of specific Congressional action we should assume that Congress has left the control of primaries and nominating conventions to the states&#8212;an assumption plainly in line with the Committee Report, quoted above, recommending the repeal of portions of the Enforcement Act of May 31, 1870 so as to place the details of elections in state hands. There is no ground for inference in subsequent legislative history that Congress has departed from that policy by superimposing its own primary penal law on the primary penal laws of the states. Rather, Congress has been fairly consistent in recognizing state autonomy in the field of elections. To be sure, it has occasionally legislated on primaries.<a class="footnote" href="#fn4-1" id="fn4-1_ref">4</a> But even when dealing specifically with the nominating process, it has never made acts of the kind here in question a crime. In this connection it should be noted that the bill which became the Hatch Act, <span class="citation no-link">53 Stat. 1147</span>, <span class="citation no-link">18 U.S.C. &#167; 61</span> et seq., <span class="citation no-link">18 U.S.C.A. &#167; 61</span> et seq., contained a section which made it unlawful 'for any person to intimidate, threaten, or coerce, or to attempt to intimidate, threaten, or coerce, any other person for the purpose of interfering with the right of such other person to vote or to vote as he may choose, or of causing such other person to vote for or not to vote for any candidate for the nomination of any party as its candidate' for various federal offices including representatives 'at any primary or nominating convention held solely or in part' for that purpose. This was stricken in the Senate. 84 Cong.Rec., pt. 4, 76th Cong., 1st Sess., p. 4191. That section would have extended the same protection to the primary and nominating convention as &#167; 1 of the Hatch Act<a class="footnote" href="#fn5-1" id="fn5-1_ref">5</a> extends to the general election. The Senate, however, refused to do so. Yet this Court now holds that &#167; 19 has protected the primary vote all along and that it covers conspiracies to do the precise thing on which Congress refused to legislate in 1939. The hesitation on the part of Congress through the years to enter the primary field, its refusal to do so<a class="footnote" href="#fn6-1" id="fn6-1_ref">6</a> in 1939, and the restricted scope of such primary laws as it has passed should be ample evidence that this Court is legislating when it takes the initiative in extending &#167; 19 to primaries.</p>
    </div>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">We should adhere to the strict construction given to &#167; 19 by a unanimous court in United States v. Bathgate, supra, 246 U.S. page 226, 38 S.Ct. page 271, <span class="citation" data-id="99111"><a href="/opinion/99111/united-states-v-bathgate-same-v-burckhauser-same-v-coons-same-v-farrell/" aria-description="Citation for case: United States v. Bathgate Same v. Burckhauser Same v....">62 L.Ed. 676</a></span>, where it was said: 'Section 19, Criminal Code * * *, of course, now has the same meaning as when first enacted * * * and considering the policy of Congress not to interfere with elections within a state except by clear and specific provisions, together with the rule respecting construction of criminal statutes, we cannot think it was intended to apply to conspiracies to bribe voters.' That leads to the conclusion that &#167; 19 and the relevant constitutional provisions should be read so as to exclude all acts which do not have the direct effect of depriving voters of their right to vote at general elections. That view has received tacit recognition by Congress. For the history of legislation governing Federal elections shows that the occasional Acts of Congress<a class="footnote" href="#fn7-1" id="fn7-1_ref">7</a> on the subject have been primarily directed towards supplying detailed regulations designed to protect the individual's constitutional right to vote against pollution and corruption. Those laws, the latest of which is &#167; 1 of the Hatch Act, are ample recognition by Congress itself that specific legislation is necessary in order to protect the electoral process against the wide variety of acts which in their indirect or incidental effect interfere with the voter's freedom of choice and corrupt the electoral process. They are evidence that detailed regulations are essential in order to reach acts which do not directly interfere with the voting privilege. They are inconsistent with the notions in the opinion of the Court that the Constitution unaided by definite supplementary legislation protects the methods by which party candidates are nominated.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">That &#167; 19 lacks the requisite specificity necessary for inclusion of acts which interfere with the nomination of party candidates is reemphasized by the test here employed. The opinion of the Court stresses, as does the indictment, that the winner of the Democratic primary in Louisiana invariably carries the general election. It is also emphasized that a candidate defeated in the Louisiana primaries cannot be a candidate at the general election. Hence, it is argued that interference with the right to vote in such a primary is 'as a matter of law and in fact an interference with the effective choice of the voters at the only stage of the election procedure when their choice is of significance,' and that the 'primary in Louisiana is an integral part of the procedure for the popular choice' of representatives. By that means the Gradwell case is apparently distinguished. But I do not think it is a valid distinction for the purposes of this case.</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">One of the indictments in the Gradwell case charged that the defendants conspired to procure one thousand unqualified persons to vote in a West Virginia primary for the nomination of a United States Senator.  his Court, by a unanimous vote, affirmed the judgment which sustained a demurrer to that indictment. The Court specifically reserved the question as to whether a 'primary shall be treated as an election within the meaning of the Constitution'. But it went on to say that even assuming it were, certain 'strikingly unusual features' of the particular primary precluded such a holding in that case. It noted that candidates of certain parties were excluded from the primary and that even candidates who were defeated at the primary could on certain conditions be nominated for the general election. It therefore concluded that whatever power Congress might have to control such primaries, it had not done so by &#167; 19.</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p class="indent">If the Gradwell case is to survive, as I think it should, we have therefore this rather curious situation. Primaries in states where the winner invariably carries the general election are protected by &#167; 19 and the Constitution, even though such primaries are not by law an integral part of the election process. Primaries in states where the successful candidate never wins, seldom wins, or may not win in the general election are not so protected, unless perchance state law makes such primaries an integral part of the election process. Congress having a broad control over primaries might conceivably draw such distinctions in a penal code. But for us to draw them under &#167; 19 is quite another matter. For we must go outside the statute, examine local law and local customs, and then on the basis of the legal or practical importance of a particular primary interpret the vague language of &#167; 19 in the light of the significance of the acts done. The result is to make refined and nice distinctions which Congress certainly has not made, to create unevenness in the application of &#167; 19 among the various states, and to make the existence of a crime depend, not on the plain meaning of words employed interpreted in light of the legislative history of the statute, but on the result of research into local law or local practices. Unless Congress has explicitly made a crime dependent on such facts, we should not undertake to do so. Such procedure does not comport with the strict standards essential for the interpretation of a criminal law. The necessity of resorting to such a circuitous route is sufficient evidence to me that we are performing a legislative function in finding here a definition of a crime which will sustain this indictment. A crime, no matter how offensive, should not be spelled out from such vague inferences.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">Mr. Justice BLACK and Mr. Justice MURPHY join in this dissent.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> The ballots are printed at public expense, &#167; 35 of Act No. 46, Regular Session, 1940, are furnished by the Secretary of State, &#167; 36 in a form prescribed by statute, &#167; 37. Close supervision of the delivery of the ballots to the election commissioners is prescribed, &#167;&#167; 43&#8212;46. The polling places are required to be equipped to secure secrecy, &#167;&#167; 48&#8212;50; &#167;&#167; 54&#8212;57. The selection of election commissioners is prescribed, &#167; 61 and their duties detailed. The commissioners must swear to conduct the election impartially, &#167; 64 and are subject to punishment for deliberately falsifying the returns or destroying the lists and ballots, &#167;&#167; 98, 99. They must identify by certificate the ballot boxes used, &#167; 67, keep a triplicate list of voters, &#167; 68, publicly canvass the return, &#167; 74 and certify the same to the Secretary of State, &#167; 75.</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> For a discussion of the practical effect of the primary in controlling or restricting election of candidates at general elections, see, Hasbrouck, Party Government in the House of Representatives (1927) 172, 176, 177; Merriam and Overacker, Primary Elections (1928) 267&#8212;269; Stoney, Suffrage in the South; 29 Survey Graphic, 163, 164.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> Congress has recognized the effect of primaries on the free exercise of the right to choose the representatives, for it has inquired into frauds at primaries as well as at the general elections in judging the 'Elections, Returns, and Qualifications of its own Members', Art. I, &#167; 5. See Grace v. Whaley, H. Rept. No. 158, 63d Cong., 2d Sess.; Peddy v. Mayfield, S.Rept. No. 973, 68th Cong., 2d Sess.; Wilson v. Vare, S.Rept. No. 1858, 70th Cong., 2d Sess., S.Rept. No. 47, 71st Cong. 2d Sess., and S.Res. 111, 71st Cong., 2d Sess.</p>
        <p>See also Investigation of Campaign Expenditures in the 1940 Campaign, S.Rept. No. 47, 77th Cong., 1st Sess., p. 48 et seq.</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> Section 19 of the Criminal Code, U.S.C., Title 18, Sec. 51, <span class="citation no-link">18 U.S.C.A. &#167; 51</span>:</p>
        <p>'If two or more persons conspire to injure, oppress, threaten, or intimidate any citizen in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States, or because of his having so exercised the same, or if two or more persons go in disguise on the highway, or on the premises of another, with intent to prevent or hinder his free exercise or enjoyment of any right or privilege so secured, they shall be fined n t more than $5,000 and imprisoned not more than ten years, and shall, moreover, be thereafter ineligible to any office, or place of honor, profit, or trust created by the Constitution or laws of the United States.' (R.S. &#167; 5508; Mar. 4, 1909, c. 321, &#167; 19, <span class="citation no-link">35 Stat. 1092</span>).</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> In United States v. Mosley, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#386" aria-description="Citation for case: United States v. Mosley">238 U.S. 383, 386</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#905" aria-description="Citation for case: United States v. Mosley">35 S.Ct. 904, 905</a></span>, <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/" aria-description="Citation for case: United States v. Mosley">59 L.Ed. 1355</a></span>, the Court thought that 'Manifestly the words are broad enough to cover the case', it canvassed at length the objections that &#167; 19 was never intended to apply to crimes against the franchise, and the other contention, which it also rejected, that &#167; 19 had been repealed or so restricted as not to apply to offenses of that class. It is unnecessary to repeat that discussion here.</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> Section 1 now reads, <span class="citation no-link">8 U.S.C. &#167; 43</span>, <span class="citation no-link">8 U.S.C.A. &#167; 43</span>: 'Every person who, under color of any statute, ordinance, re ulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.'</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> See e.g. Guinn v. United States, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">238 U.S. 347</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">35 S.Ct. 926</a></span>, <span class="citation" data-id="98516"><a href="/opinion/98516/guinn-v-united-states/" aria-description="Citation for case: Guinn v. United States">59 L.Ed. 1340</a></span>, L.R.A.1916A, 1124; United States v. O'Toole, D.C., <span class="citation" data-id="8800997"><a href="/opinion/8816481/united-states-v-otoole/" aria-description="Citation for case: United States v. O&#x27;Toole">236 F. 993</a></span>, affirmed, United States v. Gradwell, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">243 U.S. 476</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">37 S.Ct. 407</a></span>, <span class="citation" data-id="98915"><a href="/opinion/98915/united-states-v-gradwell/" aria-description="Citation for case: United States v. Gradwell">61 L.Ed. 857</a></span>; Aczel v. United States, 7 Cir., <span class="citation" data-id="8799368"><a href="/opinion/8814892/aczel-v-united-states/" aria-description="Citation for case: Aczel v. United States">232 F. 652</a></span>; Felix v. United States, 5 Cir., <span class="citation" data-id="8778884"><a href="/opinion/8794848/felix-v-united-states/" aria-description="Citation for case: Felix v. United States">186 F. 685</a></span>; Karem v. United States, 6 Cir., <span class="citation" data-id="8750159"><a href="/opinion/8766689/karem-v-united-states/" aria-description="Citation for case: Karem v. United States">121 F. 250</a></span>, <span class="citation" data-id="8750159"><a href="/opinion/8766689/karem-v-united-states/" aria-description="Citation for case: Karem v. United States">61 L.R.A. 437</a></span>; Walker v. United States, 8 Cir., <span class="citation" data-id="1542868"><a href="/opinion/1542868/walker-v-united-states/" aria-description="Citation for case: Walker v. United States">93 F.2d 383</a></span>; Luteran v. United States, 8 Cir., <span class="citation" data-id="1542708"><a href="/opinion/1542708/luteran-v-united-states/" aria-description="Citation for case: Luteran v. United States">93 F.2d 395</a></span>.</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> No conclusion is to be drawn from the failure of the Hatch Act, <span class="citation no-link">53 Stat. 1147</span>, <span class="citation no-link">18 U.S.C. &#167; 61</span> et seq., <span class="citation no-link">18 U.S.C.A. &#167; 61</span> et seq., to enlarge &#167; 19 by provisions specifically applicable to primaries. Its failure to deal with the subject seems to be attributable to constitutional doubts, stimulated by Newberry v. United States, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">256 U.S. 232</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">41 S.Ct. 469</a></span>, <span class="citation" data-id="9418460"><a href="/opinion/99796/newberry-v-united-states/" aria-description="Citation for case: Newberry v. United States">65 L.Ed. 913</a></span>, which are here resolved. See 84 Cong.Rec., 76th Cong., 1st Sess., p. 4191; cf. Investigation of Campaign Expenditures in the 1940 Campaign, S.Rept. No. 47, 77th Cong., 1st Sess., p. 48.</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> Section 20 of the Criminal Code, U.S.C., Title 18, Sec. 52, <span class="citation no-link">18 U.S.C.A. &#167; 52</span>:</p>
        <p>'Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects, or causes to be subjected, any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be find not more than $1,000, or imprisoned not more than one year, or both.' (R.S. &#167; 5510; Mar. 4, 1909, c. 321, &#167; 20, <span class="citation no-link">35 Stat. 1092</span>).</p>
      </div>
      <div class="footnote" id="fn10">
        <a class="footnote" href="#fn10_ref">10</a>
        <p> The precursor of &#167; 20 was &#167; 2 of the Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, which reads:</p>
        <p>'That any person who, under color of any law, statute, ordinance, regulation, or custom, shall subject, or cause to be subjected, any inhabitant of any State or Territory to the deprivation of any right secured or protected by this act, or to different punishment, pains, or penalties on account of such person having at any time been held in a condition of slavery or involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, or by reason of his color or race, than is prescribed for the punishment of white persons, shall be deemed guilty of a misdemeanor, and, on conviction, shall be punished by fine * * *.'</p>
        <p>This section, so far as now material, was in substance the same as &#167; 20 except that the qualifying reference to differences in punishment made no mention of alienage, the reference being to 'different punishment * * * on account of such person having at any time been held in a condition of slavery or involuntary servitude'.</p>
        <p>Senator Trumbull, the putative author of S. 61, 39th Cong., 1st Sess., the Civil Rights Bill of 1866, and Chairman of the Senate Judiciary Committee which reported the bill, in explaining it stated that the bill was 'to protect all persons in the United States in their civil rights and furnishes the means of their vindication. * * *' Cong.Globe, 39th Cong., 1st Sess., p. 211. He also declared, 'The bill applies to white men as well as black men'. Cong.Globe, 39th Cong., 1st Sess., p. 599. Opponents of the bill agreed with this construction of the first clause of the section, declaring that it referred to the deprivation of constitutional rights of all inhabitants of the states of every race and color. Pp. 598, 601.</p>
        <p>On February 24, 1870, Senator Stewart of Nevada, introduced S. 365, 41st Cong., 2d Sess., &#167; 2 of which read:</p>
        <p>'That any person who under color of any law, statute, ordinance, regulation or custom shall subject, or cause to be subjected any inhabitant or any State or Territory to the deprivation of any rights secured or protected by this act, or to different punishment, pains, or penalties on account of such person being an alien, or by reason of his color or race, than is prescribed for the punishment of white persons, shall be deemed guilty of a misdemeanor. * * *'</p>
        <p>In explaining the bill he declared, Cong. Globe, 41st Cong., 2d Sess., p. 1536, that the purpose of the bill was to extend its benefits to aliens, saying, 'It extends the operation of the Civil Rights Bill, which is well known in the Senate and to the country, to all persons within the jurisdiction of the United States.' The Committee reported out a substitute bill to H.R. 1293, to which S. 365 was added as an amendment. As so amended the bill when adopted became the present &#167; 20 of the Criminal Code which read exactly as did &#167; 2 of the Civil Rights Act, except that the word 'aliens' was added and the word 'citizens' was substituted for the phrase 'white persons'.</p>
        <p>While the legislative history indicates that the immediate occasion for the adoption of &#167; 20, like the Fourteenth Amendment itself, was the more adequate 

[...TRUNCATED 5773 of 125773 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
