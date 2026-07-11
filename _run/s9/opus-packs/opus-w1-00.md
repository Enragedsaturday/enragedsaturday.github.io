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

## GROUP: _overhaul2/lake/cases/A Quantity of Copies of Books v. Kansas.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: A Quantity of Copies of Books v. Kansas
type: case
citation: "378 U.S. 205 (1964)"
parallel_cite: "84 S. Ct. 1723; 12 L. Ed. 2d 809"
neutral_cite: 1964 U.S. LEXIS 823
court: U.S.
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-22
docket: 449
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
  opinion_url: "https://www.courtlistener.com/opinion/106878/a-quantity-of-copies-of-books-v-kansas/"
  cluster_id: 106878
  opinion_id: null
  identity_checked: true
lake:
  record_id: A Quantity of Copies of Books v. Kansas
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Historical / origin
related:
  - "[[Stanford v. Texas]]"
  - "[[The Warrant Requirement]]"
tags:
  - case
  - fourth-amendment
  - first-amendment
  - warrant-requirement
  - seizure
  - obscenity
  - prior-restraint
  - historical
holding: "Seizing every copy of allegedly obscene books under a warrant issued on an ex parte finding, with no prior adversary hearing on obscenity, is constitutionally deficient — expressive material may not be swept up in a general seizure without the heightened, hearing-first warrant procedure the First and Fourteenth Amendments require."
---

# A Quantity of Copies of Books v. Kansas

*378 U.S. 205 (1964)* (No. 449) · Supreme Court of the United States · **Historical** · Treatment: **Historical — foundational origin (⚪ unverified, pending S9)**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 106878 → 378 U.S. 205, decided 1964-06-22; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
A Kansas prosecutor presented a judge with seven allegedly obscene novels. On that [[Common Legal Terms#ex-parte|ex parte]] showing, the judge issued a warrant, and the sheriff seized 1,715 copies of 31 titles from a wholesale distributor (P-K News Service) — all before any hearing on whether the books were in fact obscene. The distributor moved to quash and return the books, arguing that the mass seizure of presumptively protected expression, without a prior adversary hearing, was unconstitutional.

## Issue
Whether a warrant authorizing the seizure of all copies of books, issued without a prior adversary hearing on the question of obscenity, satisfies the constitutional constraints on searches and seizures of expressive material.

## Rule
Building on *[[Marcus v. Search Warrant|Marcus v. Search Warrant of Property]]* (1961), the plurality (Brennan, J.) held that expressive material demands a warrant procedure sensitive to First Amendment values: the judge may not authorize a wholesale seizure that functions as a prior restraint without first affording the party an adversary hearing on obscenity. "We therefore conclude that in not first affording P-K an adversary hearing, the procedure leading to the seizure order was constitutionally deficient." — 378 U.S. at 211. ^pin-211

## Application
The vice was procedural: the seizure took a large inventory of books out of circulation on nothing more than a judge's [[Common Legal Terms#ex-parte|ex parte]] look at a handful of them, suppressing the distribution of material that had not been — and might never be — adjudicated obscene. Ordinary probable cause to believe an item is contraband is not enough when the item is a book; the Constitution requires a hearing before, not after, the expression is seized en masse.

## Conclusion
The judgment of the Supreme Court of Kansas was **reversed**; the seizure procedure was constitutionally deficient. Brennan, J., announced the judgment of the Court in a [[Common Legal Terms#plurality-opinion|plurality opinion]].

## Treatment & subsequent history
**Historical — a foundational origin, not overruled.** *A Quantity of Books* is an early anchor of the rule that seizing expressive material requires a warrant procedure more protective than the ordinary probable-cause showing — a prior adversary hearing or prompt judicial superintendence rather than a discretionary sweep. The doctrine it helped originate was refined the same decade and after in the *[[Marcus v. Search Warrant|Marcus]]*–*[[Stanford v. Texas|Stanford]]*–*[[Heller v. New York|Heller]]*–*[[Roaden v. Kentucky|Roaden]]* line, which governs today. It is rendered here as **history** — a doctrinal antecedent — because its treatment has not been machine-verified.

*Status note (⚪):* authored from a CourtListener-verified identity stub; renders under the ⚪ banner until S9 promotion. The successor pages *[[Marcus v. Search Warrant]]* and *[[Roaden v. Kentucky]]* are not yet in the corpus (queued in later authoring waves); they are named in plain text here to avoid dangling links.

## Appears on
- [[Particularity]] — *Historical / origin*

## Sources
- [*A Quantity of Copies of Books v. Kansas*, 378 U.S. 205 (1964)](https://www.courtlistener.com/opinion/106878/a-quantity-of-copies-of-books-v-kansas/) — pinpoint: 211 (plurality; Brennan, J.); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8e82c6d2728ed716", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "A Quantity of Copies of Books v. Kansas"}, "payload": {"all": [{"cite": "378 U.S. 205", "page": "205", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "378"}, {"cite": "84 S. Ct. 1723", "page": "1723", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "12 L. Ed. 2d 809", "page": "809", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "12"}, {"cite": "1964 U.S. LEXIS 823", "page": "823", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "378 U.S. 205", "official": {"cite": "378 U.S. 205", "page": "205", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "378"}, "official_selection_present": true, "record_id": "A Quantity of Copies of Books v. Kansas"}}
{"assertion_id": "db26fed4b64b7242", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "A Quantity of Copies of Books v. Kansas"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "A Quantity of Copies of Books v. Kansas", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — A Quantity of Copies of Books v. Kansas

```json
{
  "schema_version": "s2.v1",
  "record_id": "A Quantity of Copies of Books v. Kansas",
  "status": "under_review",
  "identity": {
    "case_name": "A Quantity of Copies of Books v. Kansas",
    "case_name_short": "Copies of Books",
    "case_name_full": "A QUANTITY OF COPIES OF BOOKS Et Al. v. KANSAS",
    "input_case_name": "Quantity of Copies of Books v. Kansas",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-22",
    "year": 1964,
    "docket": "449",
    "cluster_id": 106878,
    "lead_opinion_id": 9422858,
    "sibling_ids": [],
    "absolute_url": "/opinion/106878/a-quantity-of-copies-of-books-v-kansas/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 205",
      "volume": "378",
      "reporter": "U.S.",
      "page": "205",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1723",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 809",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 823",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 205",
        "volume": "378",
        "reporter": "U.S.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1723",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 809",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "809",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 823",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "823",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 205",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 205",
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
    "date_created": "2026-07-07T13:26:03Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:26:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "quantity-of-copies-of-books-v-kansas--106878",
      "to_record_id": "A Quantity of Copies of Books v. Kansas",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — A Quantity of Copies of Books v. Kansas

```
<opinion type="majority">
<author id="b236-9">Mr. Justice Brennan</author>
<p id="A4UH">announced the judgment of the Court and delivered an opinion in which</p>
<judges id="Ada">The Chief Justice, Mr. Justice White, and Mr. Justice Goldberg join.</judges>
<p id="b236-10">Under a Kansas statute authorizing the seizure of allegedly obscene books before an adversary determina<page-number citation-index="1" label="207">*207</page-number>tion of their obscenity and, after that determination, their destruction by burning or otherwise,<footnotemark>1</footnotemark> the Attorney General of Kansas obtained an order from the District Court of Geary County directing the sheriff of the county to seize and impound, pending hearing, copies of certain <page-number citation-index="1" label="208">*208</page-number>paperback novels at the place of business of P-K News Service, Junction City, Kansas. After hearing, the court entered a second order directing the sheriff to destroy the 1,715 copies of 31 novels which had been seized. The Kansas Supreme Court held that the procedures met constitutional requirements and affirmed the District Court’s order. <span class="citation" data-id="2610549"><a href="/opinion/2610549/state-v-a-quantity-of-copies-of-books/" aria-description="Citation for case: State v. a Quantity of Copies of Books">191 Kan. 13</a></span>, <span class="citation" data-id="2610549"><a href="/opinion/2610549/state-v-a-quantity-of-copies-of-books/" aria-description="Citation for case: State v. a Quantity of Copies of Books">379 P. 2d 254</a></span>. Probable jurisdiction was noted, <span class="citation multiple-matches"><a href="/c/U.%20S./375/919/">375 U. S. 919</a></span>. We conclude that the procedures followed in issuing the warrant for the seizure of the books, and authorizing their impounding pending hearing, were constitutionally insufficient because they did not adequately safeguard against the suppression of nonobscene books. For this reason we think the judgment must be reversed. Therefore we do not reach, and intimate no view upon, the appellants’ contention that the Kansas courts erred in holding that the novels are obscene.</p>
<p id="b238-5">Section 4 of the Kansas statute requires the filing of a verified Information stating only that “upon information and belief . . . there is [an] . . . obscene book . . . located within his county.” The State Attorney General went further, however, and filed an Information identifying by title 59 novels, and stating that “each of said books [has] been published as 'This is an original Nightstand Book.’ ” He also filed with the Information copies of seven novels published under that caption, six of which were named by title in the Information; particular passages in the seven novels were marked with penciled notations or slips of paper. Although also not expressly required by the statute, the district judge, on application of the Attorney General, conducted a 45-min-ute <em>ex parte </em>inquiry during which he “scrutinized” the seven books; at the conclusion of this examination, he stated for the record that they “appear to be obscene literature as defined” under the Kansas statute “and give this Court reasonable grounds to believe that any paper-<page-number citation-index="1" label="209">*209</page-number>backed publication carrying the following: 'This is an original Night Stand book’ would fall within the same category . . . He issued a warrant which authorized the sheriff to seize only the particular novels identified by title in the Information. When the warrant was executed on the date it was issued, only 31 of the titles were found on P-K’s premises. All copies of such titles, however, 1,715 books in all, were seized and impounded. At the hearing held 10 days later pursuant to a notice included in the warrant, P-K made a motion to quash the Information and the warrant on the ground, among others, that the procedure preceding the seizure was constitutionally deficient. The claim was that by failing first to afford P-K a hearing on the question whether the books were obscene, the procedure “operates as a prior restraint on the circulation and dissemination of books” in violation of the constitutional restrictions against abridgment of freedom of speech and press. The motion was denied, and following a final hearing held about seven weeks after the seizure (the hearing date was continued on motion of P-K), the court held that all 31 novels were obscene and ordered the sheriff to stand ready to destroy the 1,715 copies on further order.</p>
<p id="b239-4">The steps taken beyond the express requirements of the statute were thought by the Attorney General to be necessary under our decision in <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>, decided a few weeks before the Information was filed. <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>involved a proceeding under a strikingly similar Missouri search and seizure statute and implementing rule of court. See <span class="citation multiple-matches"><a href="/c/U.%20S./367/719/">367 U. S. 719</a></span>, at notes 2, 3. In <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>the warrant gave the police virtually unlimited authority to seize any publications which they considered to be obscene, and was issued on a verified complaint lacking any specific description of the publications to be seized, and without prior submission of any publications whatever to the judge issuing the warrant. <page-number citation-index="1" label="210">*210</page-number>We reversed a judgment directing the destruction of the copies of 100 publications held to be obscene, holding that, even assuming that they were obscene, the procedures leading to their condemnation were constitutionally deficient for lack of safeguards to prevent suppression of nonobscene publications protected by the Constitution.</p>
<p id="b240-5">It is our view that since the warrant here authorized the sheriff to seize all copies of the specified titles, and since P-K was not afforded a hearing on the question of the obscenity even of' the seven novels before the warrant issued, the procedure was likewise constitutionally deficient.<footnotemark>2</footnotemark> This is the teaching of <em>Kingsley Books, Inc., </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S. 436</a></span>. See <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>at pp. 734-738. The New York injunctive procedure there sustained does not afford <em>ex parte </em>relief but postpones all injunctive relief until “both sides have had an opportunity to be heard.” <em>Tenney </em>v. <em>Liberty News Distributors, </em>13 App. Div. 2d 770, 215 N. Y. S. 2d 663, 664. In <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>we explicitly said that <em>Kingsley Books </em>“does not support the proposition that the State may impose the extensive restraints imposed here on the distribution of these publications prior to an adversary proceeding on the issue of obscenity, irrespective of whether or not the material is legally obscene.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#735" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 735-736</a></span>. A seizure of all copies of the named titles is indeed more repressive than an injunction preventing further sale of the books. State regulation of obscenity must “conform to procedures that will ensure against the curtailment of constitutionally protected expression, which is often separated from obscenity only by a dim and uncertain line.” <em>Bantam Books, Inc., </em>v. <em>Sullivan, </em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/#66" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">372 U. S. 58, 66</a></span>; the Constitution requires a procedure “designed to focus searchingly on the question of obscenity,” <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>p. 732. We therefore <page-number citation-index="1" label="211">*211</page-number>conclude that in not first affording P-K an adversary hearing, the procedure leading to the seizure order was constitutionally deficient. What we said of the Missouri procedure, <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#736" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>id., </em>at 736-737</a></span>, also fits the Kansas procedure employed to remove these books from circulation:</p>
<blockquote id="b241-4">“. . . there is no doubt that an effective restraint— indeed the most effective restraint possible — was imposed prior to hearing on the circulation of the publications in this case, because all copies on which the [sheriff] could lay [his] hands were physically removed . . . from the premises of the wholesale distributor. An opportunity ... to circulate the [books] . . . and then raise the claim of nonob-scenity by way of defense to a prosecution for doing so was never afforded these appellants because the copies they possessed were taken away. Their ability to circulate their publications was left to the chance of securing other copies, themselves subject to mass seizure under other such warrants. The public’s opportunity to obtain the publications was thus determined by the distributor’s readiness and ability to outwit the police by obtaining and selling other copies before they in turn could be seized. In addition to its unseemliness, we do not believe that this kind of enforced competition affords a reasonable likelihood that nonobscene publications, entitled to constitutional protection, will reach the public. A distributor may have every reason to believe that a publication is constitutionally protected and will be so held after judicial hearing, but his belief is unavailing as against the contrary <em>[ex </em>parte] judgment [pursuant to which the sheriff] . . . seizes it from him.”</blockquote>
<p id="b241-5">It is no answer to say that obscene books are contraband, and that consequently the standards governing searches and seizures of allegedly obscene books should <page-number citation-index="1" label="212">*212</page-number>not differ from those applied with respect to narcotics, gambling paraphernalia and other contraband. We rejected that proposition in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>. </em>We said, <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 730</a></span>-731:</p>
<blockquote id="b242-4">“The Missouri Supreme Court’s assimilation of obscene literature to gambling paraphernalia or other contraband for purposes of search and seizure does not therefore answer the appellants’ constitutional claim, but merely restates the issue whether obscenity may be treated in the same way. The authority to the police officers under the warrants issued in this case, broadly to seize ‘obscene . . . publications,’ poses problems not raised by the warrants to seize ‘gambling implements’ and ‘all intoxicating liquors’ involved in the cases cited by the Missouri Supreme Court. 334 S. W. 2d, at 125. For the use of these warrants implicates questions whether the procedures leading to their issuance and surrounding their execution were adequate to avoid suppression of constitutionally protected publications. ‘. . . [T]he line between speech unconditionally guaranteed and speech which may legitimately be regulated, suppressed, or punished is finely drawn. . . . The separation of legitimate from illegitimate speech calls for . . . sensitive tools . . . .’ <em>Speiser </em>v. <em>Randall, </em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525</a></span>. It follows that, under the Fourteenth Amendment, a State is not free to adopt whatever procedures it pleases for dealing with obscenity as here involved without regard to the possible consequences for constitutionally protected speech.”</blockquote>
<p id="b242-5">See also <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#152" aria-description="Citation for case: Smith v. California">361 U. S. 147, 152-153</a></span>.</p>
<p id="b242-6">Nor is the order under review saved because, after all 1,715 copies were seized and removed from circulation, P-K News Service was afforded a full hearing on the <page-number citation-index="1" label="213">*213</page-number>question of the obscenity of the novels. For if seizure of books precedes an adversary, determination of their obscenity, there is danger of abridgment of the right of the public in a free society to unobstructed circulation of non-obscene books. <em>Bantam Books </em>v. <em><span class="citation" data-id="9422525"><a href="/opinion/106530/bantam-books-inc-v-sullivan/" aria-description="Citation for case: Bantam Books, Inc. v. Sullivan">Sullivan, supra;</a></span> Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>; <em>Marcus </em>v. <em>Search <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Warrant, supra;</a></span> Smith </em>v. <em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/" aria-description="Citation for case: Smith v. California">California, supra.</a></span> </em>Here, as in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span>, </em>“since a violation of the Fourteenth Amendment infected the proceedings, in order to vindicate appellants’ constitutional rights” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#738" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 738</a></span>, the judgment resting on a finding of obscenity must be reversed.</p>
<p id="b243-4">
<em>Reversed.</em>
</p>
<p id="b243-5">Opinion of</p>
<author id="A12">Mr. Justice Black,</author>
<judges id="AgG">with whom Mr. Justice Douglas joins.</judges>
<p id="b243-6">The Kansas State Court judgment here under review orders that 1,715 copies of 31 novels be burned or otherwise destroyed. This book-burning judgment was based upon findings by the trial judge that “the core [of the books] would seem to be that of sex, with the plot, if any, being subservient thereto,” that the “dominant purpose [of the books] was calculated to effectively incite sexual desires” and that “they would have this effect on the average person residing in this community . . . .” Relying on these findings and this Court’s holding in <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>, the trial court held that the books “are not entitled to the . . . protection” of the First- Amendment to the Constitution. The State Supreme Court affirmed on the same grounds.</p>
<p id="b243-7">This Court now reverses. I concur in the judgment of reversal but do not find it necessary to consider the procedural questions. Compare <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#738" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 738</a></span> (concurring opinion). The Kansas courts may have been right to rely upon the Court’s <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>holding in ordering these books burned or <page-number citation-index="1" label="214">*214</page-number>otherwise destroyed. For reasons stated in the <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>case in a dissent by Mr. Justice Douglas, 354 U. S., at 508, in which I joined, I think the <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>case was wrongly decided. It is my belief, as stated in that dissent by Mr. Justice Douglas, in my concurring opinions in <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#155" aria-description="Citation for case: Smith v. California">361 U. S. 147, 155</a></span>, and <em>Kingsley International Pictures Corp. </em>v. <em>Regents, </em><span class="citation" data-id="9421871"><a href="/opinion/105937/kingsley-international-pictures-corp-v-regents-of-the-university/#690" aria-description="Citation for case: Kingsley International Pictures Corp. v. Regents of the...">360 U. S. 684, 690</a></span>, and in my dissent in <em>Beauharnais </em>v. <em>Illinois, </em><span class="citation" data-id="9420729"><a href="/opinion/105001/beauharnais-v-illinois/#267" aria-description="Citation for case: Beauharnais v. Illinois">343 U. S. 250, 267</a></span>, which Mr. Justice Douglas joined, that the Kansas statute ordering the burning of these books is in plain violation of the unequivocal prohibition of the First Amendment, made applicable to the States by the Fourteenth, against “abridging the freedom of speech, or of the press.”</p>
<p id="b244-4">Because of my belief that both <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>and <em>Beau-harnais </em>draw blueprints showing how to avoid the First Amendment’s guarantee of freedoms of speech and press, I would overrule both those cases as well as reverse the judgment here.</p>
<footnote label="1">
<p id="b237-4"> The statute is Kan. Gen. Stat. §21-1102 <em>et seq. </em>(Supp. 1961). Section 1 of Kan. Laws 1961, c. 186 (§ 21-1102), constitutes the selling or distribution of obscene materials (obscenity is defined in § 1 (b)) a criminal misdemeanor punishable by fine or imprisonment or both. Section 4 (§ 21 — 1102c) provides for the search and seizure procedure here involved:</p>
<blockquote id="b237-5">“Whenever any district, county, common pleas, or city court judge or justice of the peace shall receive an information or complaint, signed and verified upon information and belief by the county attorney or the attorney general, stating there is any prohibited lewd, lascivious or obscene book, magazine, newspaper, writing, pamphlet, ballad, printed paper, print, picture, motion pictures, drawing, photograph, publication or other thing, as set out in section 1 [21-1102] (a) of this act, located within his county, it shall be the duty of such judge to forthwith issue his search warrant directed to the sheriff or any other duly constituted peace officer to seize and bring before said judge or justice such a prohibited item or items. Any peace officer seizing such item or items as hereinbefore described shall leave a copy of such warrant with any manager, servant, employee or other person appearing or acting in the capacity of exercising any control over the premises where such item or items are found or, if no person is there found, such warrant may be posted by said peace officer in a conspicuous place upon the premises where found and said warrant shall serve as notice to all interested persons of a hearing to be had at a time not less than ten (10) days after such seizure. At such hearing, the judge or justice issuing the warrant shall determine whether or not the item or items so seized and brought before him pursuant to said warrant were kept upon the premises where found in violation of any of the provisions of this act. If he shall so find, he shall order such item or items to be destroyed by the sheriff or any duly constituted peace officer by burning or otherwise, at such time as such judge shall order, and satisfactory return thereof made to him: <em>Provided, however, </em>Such item or items shall not be destroyed so long as they may be needed as evidence in any criminal prosecution.”</blockquote>
</footnote>
<footnote label="2">
<p id="b240-6"> P-K News Service also asserts that its constitutional right against unreasonable searches and seizures was violated. The result here makes it unnecessary to pass upon this contention.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Adams v. Williams.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Adams v. Williams"
type: case
citation: "407 U.S. 143 (1972)"
parallel_cite: "92 S. Ct. 1921; 32 L. Ed. 2d 612"
neutral_cite: 1972 U.S. LEXIS 2206
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-06-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Adams v. Williams
  varies_by_point: false
  scope_note: "Good law. A tip from a known, face-to-face informant carries enough indicia of reliability to justify a Terry stop and protective frisk; reasonable suspicion need not rest on the officer's personal observation. The anonymous-tip line (Alabama v. White, Florida v. J.L., Navarette) develops the contrast but does not disturb Adams."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108571/adams-v-williams/"
  cluster_id: 108571
  opinion_id: 108571
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Progeny"
  - page: "[[Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Alabama v. White]]", "[[Florida v. J.L.]]", "[[Navarette v. California]]", "[[Draper v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion", "informant", "frisk"]
holding: "A tip from a known, face-to-face informant can supply the reasonable suspicion needed for a Terry stop and protective frisk; reasonable suspicion may rest on reliable information supplied by another, not only the officer's own observation."
lake:
  record_id: Adams v. Williams
  status: verified
  projected_at: 2026-07-09
---

# Adams v. Williams

*407 U.S. 143 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At about 2:15 a.m., Sergeant Connolly was on patrol in a high-crime area when a person known to him personally, who had given him information before, approached his cruiser and told him that a man seated in a nearby car was carrying narcotics and had a gun at his waist. Connolly approached the car and asked Williams to open the door; instead Williams rolled down the window. Connolly reached into the car to the spot at Williams's waistband the informant had described and removed a loaded revolver. Williams was arrested; a search incident to the arrest produced heroin. He was convicted of unlawful possession of the handgun and of the heroin and challenged the stop and frisk.

## Issue
Whether reasonable suspicion for a *[[Terry v. Ohio|Terry]]* stop and protective frisk may be based on a known informant's tip rather than the officer's own observation, and whether reaching to the place the informant identified to remove a weapon was a reasonable protective search.

## Rule
Yes. Reasonable suspicion can rest on a reliable informant's tip, not only on the officer's personal observation: "the information carried enough indicia of reliability to justify the officer's forcible stop of Williams." — 407 U.S. at 147. ^pin-147

"Informants' tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability. One simple rule will not cover every situation. . . . But in some situations — for example, when the victim of a street crime seeks immediate police aid and gives a description of his assailant, or when a credible informant warns of a specific impending crime — the subtleties of the hearsay rule should not thwart an appropriate police response." — *Id.* at 147. ^pin-147b

A protective reach for the reported weapon is reasonable: "Under these circumstances the policeman's action in reaching to the spot where the gun was thought to be hidden constituted a limited intrusion designed to insure his safety, and we conclude that it was reasonable." — [*Id.* at 148](https://www.courtlistener.com/opinion/108571/adams-v-williams/#:~:text=Under%20these%20circumstances%20the%20policeman%27s). ^pin-148

## Application
The informant was known to Connolly personally, had supplied information in the past, came forward in person to give immediately verifiable information, and under Connecticut law could have been arrested for a false complaint — so although the unverified tip might not have supported a warrant, it carried enough reliability to justify a forcible stop. Investigating a man reported to be armed, sitting alone in a car in a high-crime area at 2:15 a.m., Connolly had ample reason to fear for his safety; when Williams rolled down the window instead of stepping out, Connolly's reach to the waistband the informant identified was a reasonable, limited protective intrusion. Finding the loaded gun exactly where predicted then supplied probable cause to arrest Williams, making the search incident to that arrest — which produced the heroin — lawful.

## Conclusion
The stop, the protective seizure of the gun, and the search incident to the resulting arrest were all reasonable; the loaded gun and heroin were admissible and the judgment for Williams was reversed. A known informant's reliable tip can furnish reasonable suspicion for a *[[Terry v. Ohio|Terry]]* stop and frisk.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Adams* extends [[Terry v. Ohio]] to tip-based reasonable suspicion. Its emphasis on the *known* informant is the foil for the anonymous-tip cases: [[Alabama v. White]] (anonymous tip needs predictive corroboration), [[Florida v. J.L.]] (bare anonymous gun tip insufficient), and [[Navarette v. California]] (anonymous 911 tip with indicia of reliability sufficient).

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Progeny*
- [[Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Adams v. Williams*, 407 U.S. 143 (1972) — https://www.courtlistener.com/opinion/108571/adams-v-williams/ — pinpoints: 147, 148.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "964ca2e36d385b03", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Adams v. Williams"}, "payload": {"all": [{"cite": "407 U.S. 143", "page": "143", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "407"}, {"cite": "92 S. Ct. 1921", "page": "1921", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "32 L. Ed. 2d 612", "page": "612", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "32"}, {"cite": "1972 U.S. LEXIS 2206", "page": "2206", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "407 U.S. 143", "official": {"cite": "407 U.S. 143", "page": "143", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "407"}, "official_selection_present": true, "record_id": "Adams v. Williams"}}
{"assertion_id": "1efa6bd3173c006d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-147", "record_id": "Adams v. Williams"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-147", "pinpoint_status": "slip-only", "quote": "--- # Adams v. Williams *407 U.S. 143 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At about 2:15 a.m., Sergeant Connolly was on patrol in a high-crime area when a person known to him personally, who had given him information before, approached his cruiser and told him that a man seated in a nearby car was carrying narcotics and had a gun at his waist. Connolly approached the car and asked Williams to open the door; instead Williams rolled down the window. Connolly reached into the car to the spot at Williams's waistband the informant had described and removed a loaded revolver. Williams was arrested; a search incident to the arrest produced heroin. He was convicted of unlawful possession of the handgun and of the heroin and challenged the stop and frisk. ## Issue Whether reasonable suspicion for a *Terry* stop and protective frisk may be based on a known informant's tip rather than the officer's own observation, and whether reaching to the place the informant identified to remove a weapon was a reasonable protective search. ## Rule Yes. Reasonable suspicion can rest on a reliable informant's tip, not only on the officer's personal observation:", "quote_fidelity": "mismatch", "record_id": "Adams v. Williams", "star_marker": null}}
{"assertion_id": "ac75836a2634af88", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-148", "record_id": "Adams v. Williams"}, "payload": {"fragment": "#:~:text=Under%20these%20circumstances%20the%20policeman%27s", "page": null, "pin_id": "pin-148", "pinpoint_status": "star-verified", "quote": "Under these circumstances the policeman's action in reaching to the spot where the gun was thought to be hidden constituted a limited intrusion designed to insure his safety, and we conclude that it was reasonable.", "quote_fidelity": "matched", "record_id": "Adams v. Williams", "star_marker": "148"}}
{"assertion_id": "f323dec337358090", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-147b", "record_id": "Adams v. Williams"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-147b", "pinpoint_status": "slip-only", "quote": "Informants' tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability. One simple rule will not cover every situation. . . . But in some situations — for example, when the victim of a street crime seeks immediate police aid and gives a description of his assailant, or when a credible informant warns of a specific impending crime — the subtleties of the hearsay rule should not thwart an appropriate police response.", "quote_fidelity": "mismatch", "record_id": "Adams v. Williams", "star_marker": null}}
{"assertion_id": "ddd39a911888ffe3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Adams v. Williams"}, "payload": {"as_of_content": "1972-06-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Adams v. Williams", "scope_note": "Good law. A tip from a known, face-to-face informant carries enough indicia of reliability to justify a Terry stop and protective frisk; reasonable suspicion need not rest on the officer's personal observation. The anonymous-tip line (Alabama v. White, Florida v. J.L., Navarette) develops the contrast but does not disturb Adams.", "varies_by_point": false}}
```

### lake record — Adams v. Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "Adams v. Williams",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Adams v. Williams",
    "case_name_short": "Adams",
    "case_name_full": "Adams, Warden v. Williams",
    "input_case_name": "Adams v. Williams",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-06-12",
    "year": 1972,
    "docket": null,
    "cluster_id": 108571,
    "lead_opinion_id": 108571,
    "sibling_ids": [
      108571,
      9424935,
      9424936,
      9424937,
      9424938
    ],
    "absolute_url": "/opinion/108571/adams-v-williams/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8987525,
        "score": 10,
        "case_name": "Adams v. Williams"
      },
      {
        "cluster_id": 8987276,
        "score": 10,
        "case_name": "Adams v. Williams"
      },
      {
        "cluster_id": 8986252,
        "score": 10,
        "case_name": "Adams v. Williams"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "407 U.S. 143",
      "volume": "407",
      "reporter": "U.S.",
      "page": "143",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 1921",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 612",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 2206",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "2206",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "407 U.S. 143",
        "volume": "407",
        "reporter": "U.S.",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 1921",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 612",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 2206",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "2206",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "407 U.S. 143",
    "official_selection": {
      "court_class": "scotus",
      "selected": "407 U.S. 143",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-147",
      "page": null,
      "quote": "--- # Adams v. Williams *407 U.S. 143 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At about 2:15 a.m., Sergeant Connolly was on patrol in a high-crime area when a person known to him personally, who had given him information before, approached his cruiser and told him that a man seated in a nearby car was carrying narcotics and had a gun at his waist. Connolly approached the car and asked Williams to open the door; instead Williams rolled down the window. Connolly reached into the car to the spot at Williams's waistband the informant had described and removed a loaded revolver. Williams was arrested; a search incident to the arrest produced heroin. He was convicted of unlawful possession of the handgun and of the heroin and challenged the stop and frisk. ## Issue Whether reasonable suspicion for a *Terry* stop and protective frisk may be based on a known informant's tip rather than the officer's own observation, and whether reaching to the place the informant identified to remove a weapon was a reasonable protective search. ## Rule Yes. Reasonable suspicion can rest on a reliable informant's tip, not only on the officer's personal observation:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-147b",
      "page": null,
      "quote": "Informants' tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability. One simple rule will not cover every situation. . . . But in some situations \u2014 for example, when the victim of a street crime seeks immediate police aid and gives a description of his assailant, or when a credible informant warns of a specific impending crime \u2014 the subtleties of the hearsay rule should not thwart an appropriate police response.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-148",
      "page": null,
      "quote": "Under these circumstances the policeman's action in reaching to the spot where the gun was thought to be hidden constituted a limited intrusion designed to insure his safety, and we conclude that it was reasonable.",
      "star_marker": "148",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11530,
      "fragment": "#:~:text=Under%20these%20circumstances%20the%20policeman%27s",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Adams v. Williams",
    "varies_by_point": false,
    "scope_note": "Good law. A tip from a known, face-to-face informant carries enough indicia of reliability to justify a Terry stop and protective frisk; reasonable suspicion need not rest on the officer's personal observation. The anonymous-tip line (Alabama v. White, Florida v. J.L., Navarette) develops the contrast but does not disturb Adams.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People of the State of Colorado, In the Interest of T.J.W., Juvenile-Appellee L.C.W. and D.W. and Concerning",
          "cluster_id": 10871666,
          "cite": [
            "2026 CO 38"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kopp v. State",
          "cluster_id": 10864408,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stone",
          "cluster_id": 10780071,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 10770653,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tower",
          "cluster_id": 10759279,
          "cite": [
            "2025 Ohio 5593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Swanson v. State",
          "cluster_id": 10758425,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Wesley Hollingsworth v. Commonwealth of Virginia",
          "cluster_id": 10741964,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota, Respondent, vs. Matthew Sam Mitchell, Appellant",
          "cluster_id": 10696233,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lewis, A., Aplt.",
          "cluster_id": 10677596,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Scerba",
          "cluster_id": 10650412,
          "cite": [
            "2025 Ohio 2791"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wilson",
          "cluster_id": 10636220,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wolfe",
          "cluster_id": 10604482,
          "cite": [
            "2025 Ohio 2096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 10589223,
          "cite": [
            "2025 Ohio 1537"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pullom",
          "cluster_id": 10582017,
          "cite": [
            "2025 Ohio 1700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Buckingham",
          "cluster_id": 10581986,
          "cite": [
            "2025 Ohio 1688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 10517584,
          "cite": [
            "2025 Ohio 1539"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shannon",
          "cluster_id": 10373759,
          "cite": [
            "2025 Ohio 1224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dasahn Crowder",
          "cluster_id": 10363504,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Gibson, T.",
          "cluster_id": 10358162,
          "cite": [
            "2025 Pa. Super. 65"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hylton v. District of Columbia",
          "cluster_id": 10352120,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Duane Gary Underwood, II",
          "cluster_id": 10340565,
          "cite": [
            "129 F.4th 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanders",
          "cluster_id": 10329396,
          "cite": [
            "2025 Ohio 411"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McKenzie",
          "cluster_id": 10318233,
          "cite": [
            "2025 Ohio 150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re A.M.J.",
          "cluster_id": 10295535,
          "cite": [
            "2024 Ohio 5889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stollings",
          "cluster_id": 10293438,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barnes",
          "cluster_id": 10293080,
          "cite": [
            "2024 Ohio 5865"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dyson",
          "cluster_id": 10284857,
          "cite": [
            "2024 Ohio 5591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 10276151,
          "cite": [
            "2024 Ohio 4770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Swanson",
          "cluster_id": 10007955,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Melissa Trevino v. the State of Texas",
          "cluster_id": 10008832,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Napoleao Pires",
          "cluster_id": 9997524,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Michael Gene Wiskowski",
          "cluster_id": 9576066,
          "cite": [
            "2024 WI 23"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Michael Gene Wiskowski",
          "cluster_id": 9567763,
          "cite": [
            "2024 WI 23"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shaw",
          "cluster_id": 9507576,
          "cite": [
            "2024 Ohio 2022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Antonio Demetrius Adkisson a/k/a Antonio Demetrius Turner, Jr. - DISSENT",
          "cluster_id": 9487427,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 9484217,
          "cite": [
            "237 N.E.3d 948",
            "2024 Ohio 943"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Savannah Marie Scarborough v. the State of Texas",
          "cluster_id": 9480115,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wells",
          "cluster_id": 9469432,
          "cite": [
            "2024 Ohio 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Villarreal v. City of Laredo",
          "cluster_id": 9468368,
          "cite": [
            "94 F.4th 374"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Dobson, J., Aplt.",
          "cluster_id": 9458062,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Jason Scott Klein",
          "cluster_id": 10631102,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 9441433,
          "cite": [
            "229 N.E.3d 172",
            "2023 Ohio 4126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Houston",
          "cluster_id": 9439762,
          "cite": [
            "2023 Ohio 4101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Narce v. Mervilus",
          "cluster_id": 9436102,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jackson, K., Aplt.",
          "cluster_id": 9429771,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jackson, K., Aplt.",
          "cluster_id": 9429770,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Escobedo",
          "cluster_id": 9430770,
          "cite": [
            "224 N.E.3d 1274",
            "2023 Ohio 3410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lozano",
          "cluster_id": 9427519,
          "cite": [
            "226 N.E.3d 1246",
            "2023 IL 128609"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 9425749,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timothy Davis, Sr. v. City of Apopka",
          "cluster_id": 9422919,
          "cite": [
            "78 F.4th 1326"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phillip Alexander Duty v. State of Alaska",
          "cluster_id": 9409154,
          "cite": [
            "532 P.3d 742"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Oliver",
          "cluster_id": 9397810,
          "cite": [
            "214 N.E.3d 624",
            "2023 Ohio 1550"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Thornton",
          "cluster_id": 9395271,
          "cite": [
            "213 N.E.3d 808",
            "2023 Ohio 1404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hall-Johnson",
          "cluster_id": 8245698,
          "cite": [
            "2022 Ohio 3512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Timothy Barclift",
          "cluster_id": 8244189,
          "cite": [
            "282 A.3d 607",
            "2022 ME 50"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Claudell Turner",
          "cluster_id": 7858037,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayon",
          "cluster_id": 7854147,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barcus",
          "cluster_id": 6681080,
          "cite": [
            "2022 Ohio 2491"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 6623468,
          "cite": [
            "40 F.4th 339"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dazhan McCallister",
          "cluster_id": 6622139,
          "cite": [
            "39 F.4th 368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ayon",
          "cluster_id": 6621924,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Huntley",
          "cluster_id": 6620233,
          "cite": [
            "513 P.3d 1141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 6481332,
          "cite": [
            "2022 Ohio 2161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re: D.D.",
          "cluster_id": 10048705,
          "cite": [
            "479 Md. 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re: D.D.",
          "cluster_id": 6479680,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ferguson, III",
          "cluster_id": 6473582,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathan Russell Shook v. the State of Texas",
          "cluster_id": 6472617,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wharton",
          "cluster_id": 6470917,
          "cite": [
            "510 P.3d 682",
            "170 Idaho 329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Kha Len Richard Price-Williams",
          "cluster_id": 6461978,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kent",
          "cluster_id": 6452197,
          "cite": [
            "2022 Ohio 834"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 7454472,
          "cite": [
            "26 F.4th 627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Buster",
          "cluster_id": 6444299,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bingman v. United States",
          "cluster_id": 6245901,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 6236798,
          "cite": [
            "183 N.E.3d 611",
            "2022 Ohio 91"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 5306903,
          "cite": [
            "454 Ill. Dec. 624",
            "190 N.E.3d 224",
            "2021 IL 125954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guerrero",
          "cluster_id": 5303613,
          "cite": [
            "19 F.4th 547"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricardo Villa v. the State of Texas",
          "cluster_id": 5302956,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Interest of: T.W.; Apl: T.W.",
          "cluster_id": 10278823,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "the State of Texas v. Georgia Donnell",
          "cluster_id": 5173560,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wyatt",
          "cluster_id": 5093140,
          "cite": [
            "2021 Ohio 3146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Allen",
          "cluster_id": 5090790,
          "cite": [
            "2021 Ohio 3047"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Newman v. United States",
          "cluster_id": 5091720,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "FUENTES v. STATE",
          "cluster_id": 5307680,
          "cite": [
            "517 P.3d 971",
            "2021 OK CR 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maximo Gondres-Medrano",
          "cluster_id": 4898417,
          "cite": [
            "3 F.4th 708"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tidwell (Slip Opinion)",
          "cluster_id": 4894377,
          "cite": [
            "165 Ohio St. 3d 57",
            "175 N.E.3d 527",
            "2021 Ohio 2072"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howard",
          "cluster_id": 4886187,
          "cite": [
            "2021 Ohio 1792"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Brown",
          "cluster_id": 4882342,
          "cite": [
            "996 F.3d 998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bass",
          "cluster_id": 4881990,
          "cite": [
            "996 F.3d 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Juan Antonio Gutierrez v. State",
          "cluster_id": 4876118,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Cloud",
          "cluster_id": 4872727,
          "cite": [
            "994 F.3d 233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reagan v. Idaho Transportation Department",
          "cluster_id": 10732814,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yoder",
          "cluster_id": 4858742,
          "cite": [
            "2021 Ohio 496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Otoniel Decanini-Hernandez",
          "cluster_id": 4857008,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 4853848,
          "cite": [
            "2019 IL App (1st) 170803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tracy Todd Adrian",
          "cluster_id": 4853916,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Freeman v. State",
          "cluster_id": 5313799,
          "cite": [
            "245 A.3d 164",
            "249 Md. App. 269"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Calvin Dibrell v. City of Knoxville, Tenn.",
          "cluster_id": 4846329,
          "cite": [
            "984 F.3d 1156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lonnie Gene Kinnett v. State",
          "cluster_id": 4843169,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4838065,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4837847,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael D. Johnson v. State of Indiana",
          "cluster_id": 4834676,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hansard",
          "cluster_id": 4835582,
          "cite": [
            "2020 Ohio 5528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4820971,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mallory",
          "cluster_id": 4794674,
          "cite": [
            "160 N.E.3d 399",
            "2020 Ohio 4848"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Toddrey Willie Bruce",
          "cluster_id": 4794438,
          "cite": [
            "977 F.3d 1112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morrison v. Horseshoe Casino",
          "cluster_id": 4776888,
          "cite": [
            "157 N.E.3d 406",
            "2020 Ohio 4131"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ellis",
          "cluster_id": 4772243,
          "cite": [
            "2020 Ohio 3910"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aaron Emile McArthur v. Commonwealth of Virginia",
          "cluster_id": 4771110,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re D.L.",
          "cluster_id": 4832659,
          "cite": [
            "2018 IL App (1st) 171764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Eymann",
          "cluster_id": 4760956,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Eymann",
          "cluster_id": 4760946,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Arrington, W.",
          "cluster_id": 10315555,
          "cite": [
            "233 A.3d 910",
            "2020 Pa. Super. 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Arrington, W.",
          "cluster_id": 4759745,
          "cite": [
            "2020 Pa. Super. 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 4750440,
          "cite": [
            "154 N.E.3d 387",
            "2020 Ohio 2742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gerald Allen Spikes v. State",
          "cluster_id": 4747272,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Zadeh",
          "cluster_id": 10021010,
          "cite": [
            "226 A.3d 463",
            "468 Md. 124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hoang Thanh Dang v. State",
          "cluster_id": 4741688,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Thornton",
          "cluster_id": 9504236,
          "cite": [
            "170 N.E.3d 123",
            "446 Ill. Dec. 297",
            "2020 IL App (1st) 170753"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 4729465,
          "cite": [
            "2020 Ohio 619"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nolen",
          "cluster_id": 4696266,
          "cite": [
            "2020 Ohio 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Dollard v. Gary Whisenand",
          "cluster_id": 4690360,
          "cite": [
            "946 F.3d 342"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Dollard v. Gary Whisenand",
          "cluster_id": 4690001,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ronald Vierk v. Gary Whisenand",
          "cluster_id": 4690000,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ronald Vierk v. Gary Whisenand",
          "cluster_id": 4689841,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phipps",
          "cluster_id": 10733097,
          "cite": [
            "166 Idaho 1",
            "454 P.3d 1084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Kari Lee Fogg",
          "cluster_id": 4689069,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dozier v. United States",
          "cluster_id": 4685444,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dozier v. United States",
          "cluster_id": 4684945,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dozier v. United States",
          "cluster_id": 4684387,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re J.C.",
          "cluster_id": 4681481,
          "cite": [
            "2019 Ohio 4815"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tidwell",
          "cluster_id": 4675183,
          "cite": [
            "2019 Ohio 4493"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Aaron Mims v. State",
          "cluster_id": 4664361,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shelly Ioane v. Jean Noll",
          "cluster_id": 4662528,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanderson",
          "cluster_id": 4659008,
          "cite": [
            "2019 Ohio 3589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christopher Lewis Roth v. State",
          "cluster_id": 4657067,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Klase",
          "cluster_id": 4655386,
          "cite": [
            "2019 Ohio 3392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Arrizabalaga",
          "cluster_id": 4643311,
          "cite": [
            "447 P.3d 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Holmes",
          "cluster_id": 4635398,
          "cite": [
            "2019 IL App (1st) 160987"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625131,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625130,
          "cite": [
            "208 A.3d 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antoine Richmond",
          "cluster_id": 4619114,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antoine Richmond",
          "cluster_id": 4619085,
          "cite": [
            "924 F.3d 404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Portillo-Saravia",
          "cluster_id": 7335834,
          "cite": [
            "379 F. Supp. 3d 600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hairston (Slip Opinion)",
          "cluster_id": 4615930,
          "cite": [
            "2019 Ohio 1622",
            "126 N.E.3d 1132",
            "156 Ohio St. 3d 363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cummins",
          "cluster_id": 4612084,
          "cite": [
            "2019 Ohio 1496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre Cherry",
          "cluster_id": 4607955,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre Cherry",
          "cluster_id": 4607774,
          "cite": [
            "920 F.3d 1126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 4603580,
          "cite": [
            "203 A.3d 1233",
            "331 Conn. 239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Smith",
          "cluster_id": 4586041,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Daniel Andrew Ralicki v. State",
          "cluster_id": 4585027,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Temarco Pope, Jr.",
          "cluster_id": 4571610,
          "cite": [
            "910 F.3d 413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Hester",
          "cluster_id": 4568875,
          "cite": [
            "910 F.3d 78"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Luther",
          "cluster_id": 4552852,
          "cite": [
            "2018 Ohio 4568",
            "123 N.E.3d 296"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robyn Kaye Tanton v. State",
          "cluster_id": 4551555,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Donald Ray King v. State",
          "cluster_id": 4549914,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Calvin Lindsey v. Vince Macias",
          "cluster_id": 4546462,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Calvin Lindsey v. Vince Macias",
          "cluster_id": 4546314,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fausto Lopez",
          "cluster_id": 4545359,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fausto Lopez",
          "cluster_id": 4545246,
          "cite": [
            "907 F.3d 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shelly Ioane v. Jean Noll",
          "cluster_id": 4533737,
          "cite": [
            "939 F.3d 945",
            "903 F.3d 929"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Laster",
          "cluster_id": 4533341,
          "cite": [
            "2018 Ohio 3601"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Olagbemiro",
          "cluster_id": 4532502,
          "cite": [
            "2018 Ohio 3540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lenzy",
          "cluster_id": 4531151,
          "cite": [
            "2018 Ohio 3485"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hemingway",
          "cluster_id": 4511381,
          "cite": [
            "192 A.3d 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nicholson",
          "cluster_id": 4505529,
          "cite": [
            "813 S.E.2d 840",
            "371 N.C. 284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gates",
          "cluster_id": 10688465,
          "cite": [
            "31 N.Y.3d 1028",
            "2018 NY Slip Op 03096"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gates",
          "cluster_id": 7173630,
          "cite": [
            "99 N.E.3d 861",
            "31 N.Y.3d 1028",
            "75 N.Y.S.3d 468"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Everett Miles v. United States",
          "cluster_id": 4484257,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Everett Miles v. United States",
          "cluster_id": 4482035,
          "cite": [
            "181 A.3d 633"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Paul Johnson, Jr.",
          "cluster_id": 4480008,
          "cite": [
            "885 F.3d 1313"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pamela Sue Wolfe v. State",
          "cluster_id": 4474671,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rafael De Los Santos v. State",
          "cluster_id": 4468933,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Tyreke H.",
          "cluster_id": 4465187,
          "cite": [
            "2017 IL App (1st) 170406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Trice",
          "cluster_id": 4458299,
          "cite": [
            "2018 Ohio 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Stanley",
          "cluster_id": 4450785,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sizer v. State",
          "cluster_id": 4446705,
          "cite": [
            "174 A.3d 326",
            "456 Md. 350"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Stanley",
          "cluster_id": 6239232,
          "cite": [
            "226 Cal. Rptr. 3d 291",
            "18 Cal. App. 5th 398"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schreiner v. Hodge",
          "cluster_id": 4441833,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eversole",
          "cluster_id": 4440680,
          "cite": [
            "2017 Ohio 8436"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hamilton",
          "cluster_id": 4433424,
          "cite": [
            "2017 Ohio 8140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Imani",
          "cluster_id": 4432643,
          "cite": [
            "2017 Ohio 8113",
            "98 N.E.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Nicholson",
          "cluster_id": 4427100,
          "cite": [
            "805 S.E.2d 348",
            "255 N.C. App. 665",
            "2017 N.C. App. LEXIS 769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Belin",
          "cluster_id": 4420810,
          "cite": [
            "868 F.3d 43",
            "2017 WL 3599066",
            "2017 U.S. App. LEXIS 15992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michele Hall v. District of Columbia",
          "cluster_id": 4418006,
          "cite": [
            "867 F.3d 138",
            "2017 WL 3443060",
            "2017 U.S. App. LEXIS 14888"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ewing",
          "cluster_id": 4417944,
          "cite": [
            "2017 Ohio 7194",
            "95 N.E.3d 1112"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pickett",
          "cluster_id": 4409162,
          "cite": [
            "2017 Ohio 5830",
            "94 N.E.3d 1046"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 4405370,
          "cite": [
            "2017 Ohio 5613",
            "94 N.E.3d 194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 4404068,
          "cite": [
            "2017 Ohio 5527",
            "92 N.E.3d 1256"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stanley",
          "cluster_id": 4396236,
          "cite": [
            "2017 SD 32",
            "896 N.W.2d 669",
            "2017 S.D. LEXIS 66",
            "2017 WL 2376527"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wheeler",
          "cluster_id": 4394879,
          "cite": [
            "2017 Ohio 4013"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Denishio Johnson v. Curt Vanderkooi",
          "cluster_id": 4394299,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Denishio Johnson v. Curt Vanderkooi",
          "cluster_id": 4393974,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Pinner v. State of Indiana",
          "cluster_id": 4390020,
          "cite": [
            "74 N.E.3d 226",
            "2017 WL 1900295",
            "2017 Ind. LEXIS 354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Reyes-Valenzuela",
          "cluster_id": 4385739,
          "cite": [
            "2017 CO 31",
            "392 P.3d 520",
            "2017 WL 1450113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan P. Jackson v. United States",
          "cluster_id": 4382813,
          "cite": [
            "157 A.3d 1259",
            "2017 WL 1373326",
            "2017 D.C. App. LEXIS 81"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stanage",
          "cluster_id": 4381186,
          "cite": [
            "2017 SD 12",
            "893 N.W.2d 522",
            "2017 S.D. 12",
            "2017 S.D. LEXIS 33",
            "2017 WL 1281421"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
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
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Adams v. Williams:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108571 OR 9424935 OR 9424936 OR 9424937 OR 9424938) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkxMzUwNDAwMDAwJnM9NDM4MTE4NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108571+OR+9424935+OR+9424936+OR+9424937+OR+9424938%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 198
      },
      "lane2_top_cited": {
        "query": "cites:(108571 OR 9424935 OR 9424936 OR 9424937 OR 9424938)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTkmcz0xMDg4OTQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108571+OR+9424935+OR+9424936+OR+9424937+OR+9424938%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(108571 OR 9424935 OR 9424936 OR 9424937 OR 9424938)",
        "reviewed": 65,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 65,
        "triage_read": 1,
        "triage_snippet_classified": 64
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108571 OR 9424935 OR 9424936 OR 9424937 OR 9424938)",
    "indexed_citing_opinions": 3297,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108571,
        "count": 3006,
        "count_source": "search"
      },
      {
        "opinion_id": 9424935,
        "count": 385,
        "count_source": "search"
      },
      {
        "opinion_id": 9424936,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424937,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424938,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5121,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/adams-v-williams.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjU2ODcmcz0xMDM1ODE2MiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108571+OR+9424935+OR+9424936+OR+9424937+OR+9424938%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108571,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 103203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 289453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 293975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 296170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 299230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 1158944,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 1559595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 2084121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 2084189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108571,
        "cited_id": 2614276,
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
    "date_created": "2026-07-04T15:30:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T15:30:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T15:30:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T15:53:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T15:30:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Adams v. Williams

```
<div>
<center><b><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span> (1972)</b></center>
<center><h1>ADAMS, WARDEN<br>
v.<br>
WILLIAMS.</h1></center>
<center>No. 70-283.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 10, 1972.</center>
<center>Decided June 12, 1972.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Donald A. Browne</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Edward F. Hennessey</i> argued the cause and filed a brief for respondent.</p>
<p><span class="star-pagination">*144</span> Briefs of <i>amici curiae</i> urging reversal were filed by <i>Solicitor General Griswold, Assistant Attorney General Petersen,</i> and <i>Beatrice Rosenberg</i> for the United States; by <i>Frank S. Hogan, pro se, Michael R. Juviler,</i> and <i>Herman Kaufman</i> for the District Attorney of New York County; and by <i>Frank G. Carrington, Jr., Alan S. Ganz, Wayne W. Schmidt,</i> and <i>Glen R. Murphy</i> for Americans for Effective Law Enforcement, Inc., et al.</p>
<p><i>Burt Neuborne</i> and <i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae.</i></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Respondent Robert Williams was convicted in a Connecticut state court of illegal possession of a handgun found during a "stop and frisk," as well as of possession of heroin that was found during a full search incident to his weapons arrest. After respondent's conviction was affirmed by the Supreme Court of Connecticut, <span class="citation" data-id="1559595"><a href="/opinion/1559595/state-v-williams/" aria-description="Citation for case: State v. Williams">157 Conn. 114</a></span>, <span class="citation" data-id="1559595"><a href="/opinion/1559595/state-v-williams/" aria-description="Citation for case: State v. Williams">249 A. 2d 245</a></span> (1968), this Court denied certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./395/927/">395 U. S. 927</a></span> (1969). Williams' petition for federal habeas corpus relief was denied by the District Court and by a divided panel of the Second Circuit, <span class="citation" data-id="9456354"><a href="/opinion/293975/robert-williams-v-frederick-e-adams-warden-connecticut-state-prison/" aria-description="Citation for case: Robert Williams v. Frederick E. Adams, Warden,...">436 F. 2d 30</a></span> (1970), but on rehearing <i>en banc</i> the Court of Appeals granted relief. <span class="citation" data-id="9456793"><a href="/opinion/296170/robert-williams-v-frederick-e-adams-warden-connecticut-state-prison/" aria-description="Citation for case: Robert Williams v. Frederick E. Adams, Warden,...">441 F. 2d 394</a></span> (1971). That court held that evidence introduced at Williams' trial had been obtained by an unlawful search of his person and car, and thus the state court judgments of conviction should be set aside. Since we conclude that the policeman's actions here conformed to the standards this Court laid down in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), we reverse.</p>
<p>Police Sgt. John Connolly was alone early in the morning on car patrol duty in a high-crime area of Bridgeport, Connecticut. At approximately 2:15 a.m. a person known to Sgt. Connolly approached his cruiser <span class="star-pagination">*145</span> and informed him that an individual seated in a nearby vehicle was carrying narcotics and had a gun at his waist.</p>
<p>After calling for assistance on his car radio, Sgt. Connolly approached the vehicle to investigate the informant's report. Connolly tapped on the car window and asked the occupant, Robert Williams, to open the door. When Williams rolled down the window instead, the sergeant reached into the car and removed a fully loaded revolver from Williams' waistband. The gun had not been visible to Connolly from outside the car, but it was in precisely the place indicated by the informant. Williams was then arrested by Connolly for unlawful possession of the pistol. A search incident to that arrest was conducted after other officers arrived. They found substantial quantities of heroin on Williams' person and in the car, and they found a machete and a second revolver hidden in the automobile.</p>
<p>Respondent contends that the initial seizure of his pistol, upon which rested the later search and seizure of other weapons and narcotics, was not justified by the informant's tip to Sgt. Connolly. He claims that absent a more reliable informant, or some corroboration of the tip, the policeman's actions were unreasonable under the standards set forth in <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>.</i></p>
<p>In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> this Court recognized that "a police officer may in appropriate circumstances and in an appropriate manner approach a person for purposes of investigating possibly criminal behavior even though there is no probable cause to make an arrest." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 22</a></span>. The Fourth Amendment does not require a policeman who lacks the precise level of information necessary for probable cause to arrest to simply shrug his shoulders and allow a crime to occur or a criminal to escape. On the contrary, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> recognizes that it may be the essence of good police work to adopt an intermediate response. <span class="star-pagination">*146</span> See <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#23" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 23</a></span>. A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21-22</a></span>; see <i>Gaines</i> v. <i>Craven,</i> <span class="citation" data-id="299230"><a href="/opinion/299230/larry-d-gaines-v-walter-e-craven/" aria-description="Citation for case: Larry D. Gaines v. Walter E. Craven">448 F. 2d 1236</a></span> (CA9 1971); <i>United States</i> v. <i>Unverzagt,</i> <span class="citation" data-id="289453"><a href="/opinion/289453/united-states-v-cloyd-l-unverzagt/" aria-description="Citation for case: United States v. Cloyd L. Unverzagt">424 F. 2d 396</a></span> (CA8 1970).</p>
<p>The Court recognized in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> that the policeman making a reasonable investigatory stop should not be denied the opportunity to protect himself from attack by a hostile suspect. "When an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous to the officer or to others," he may conduct a limited protective search for concealed weapons. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24</a></span>. The purpose of this limited search is not to discover evidence of crime, but to allow the officer to pursue his investigation without fear of violence, and thus the frisk for weapons might be equally necessary and reasonable, whether or not carrying a concealed weapon violated any applicable state law. So long as the officer is entitled to make a forcible stop,<sup>[1]</sup> and has reason to believe that the suspect is armed and dangerous, he may conduct a weapons search limited in scope to this protective purpose. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 30</a></span>.</p>
<p>Applying these principles to the present case, we believe that Sgt. Connolly acted justifiably in responding to his informant's tip. The informant was known to him personally and had provided him with information in the past. This is a stronger case than obtains in the case of an anonymous telephone tip. The informant here came forward personally to give information that was immediately verifiable at the scene. Indeed, under <span class="star-pagination">*147</span> Connecticut law, the informant might have been subject to immediate arrest for making a false complaint had Sgt. Connolly's investigation proved the tip incorrect.<sup>[2]</sup> Thus, while the Court's decisions indicate that this informant's unverified tip may have been insufficient for a narcotics arrest or search warrant, see, <i>e. g., </i><i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), the information carried enough indicia of reliability to justify the officer's forcible stop of Williams.</p>
<p>In reaching this conclusion, we reject respondent's argument that reasonable cause for a stop and frisk can only be based on the officer's personal observation, rather than on information supplied by another person. Informants' tips, like all other clues and evidence coming to a policeman on the scene, may vary greatly in their value and reliability. One simple rule will not cover every situation. Some tips, completely lacking in indicia of reliability, would either warrant no police response or require further investigation before a forcible stop of a suspect would be authorized. But in some situationsfor example, when the victim of a street crime seeks immediate police aid and gives a description of his assailant, or when a credible informant warns of a specific impending crimethe subtleties of the hearsay rule should not thwart an appropriate police response.</p>
<p>While properly investigating the activity of a person who was reported to be carrying narcotics and a concealed weapon and who was sitting alone in a car in a high-crime area at 2:15 in the morning, Sgt. Connolly <span class="star-pagination">*148</span> had ample reason to fear for his safety.<sup>[3]</sup> When Williams rolled down his window, rather than complying with the policeman's request to step out of the car so that his movements could more easily be seen, the revolver allegedly at Williams' waist became an even greater threat. Under these circumstances the policeman's action in reaching to the spot where the gun was thought to be hidden constituted a limited intrusion designed to insure his safety, and we conclude that it was reasonable. The loaded gun seized as a result of this intrusion was therefore admissible at Williams' trial. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 30</a></span>.</p>
<p>Once Sgt. Connolly had found the gun precisely where the informant had predicted, probable cause existed to arrest Williams for unlawful possession of the weapon. Probable cause to arrest depends "upon whether, at the moment the arrest was made . . . the facts and circumstances within [the arresting officers'] knowledge and of which they had reasonably trustworthy information were sufficient to warrant a prudent man in believing that the [suspect] had committed or was committing an offense." <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964). In the present case the policeman found Williams in possession of a gun in precisely the place predicted by the informant. This tended to corroborate the reliability of the informant's further report of narcotics and, together with the surrounding circumstances, certainly suggested no lawful explanation for possession of the <span class="star-pagination">*149</span> gun. Probable cause does not require the same type of specific evidence of each element of the offense as would be needed to support a conviction. See <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#311" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 311-312</a></span> (1959). Rather, the court will evaluate generally the circumstances at the time of the arrest to decide if the officer had probable cause for his action:</p>
<blockquote>"In dealing with probable cause, however, as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949).</blockquote>
<p>See also <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#177" aria-description="Citation for case: Brinegar v. United States"><i>id.,</i> at 177</a></span>. Under the circumstances surrounding Williams' possession of the gun seized by Sgt. Connolly, the arrest on the weapons charge was supported by probable cause, and the search of his person and of the car incident to that arrest was lawful. See <i>Brinegar</i> v. <i>United States, supra</i><i>; </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). The fruits of the search were therefore properly admitted at William's trial, and the Court of Appeals erred in reaching a contrary conclusion.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE MARSHALL concurs, dissenting.</p>
<p>My views have been stated in substance by Judge Friendly, dissenting, in the Court of Appeals. <span class="citation" data-id="9456354"><a href="/opinion/293975/robert-williams-v-frederick-e-adams-warden-connecticut-state-prison/#35" aria-description="Citation for case: Robert Williams v. Frederick E. Adams, Warden,...">436 F. 2d 30, 35</a></span>. Connecticut allows its citizens to carry weapons, concealed or otherwise, at will, provided they have a permit. Conn. Gen. Stat. Rev. §§ 29-35, 29-38. Connecticut law gives its police no authority to frisk a person for a permit. Yet the arrest was for illegal possession of a gun. The only basis for that arrest was the informer's <span class="star-pagination">*150</span> tip on the narcotics. Can it be said that a man in possession of narcotics will not have a permit for his gun? Is that why the arrest for possession of a gun in the free-and-easy State of Connecticut becomes constitutional?</p>
<p>The police problem is an acute one not because of the Fourth Amendment, but because of the ease with which anyone can acquire a pistol. A powerful lobby dins into the ears of our citizenry that these gun purchases are constitutional rights protected by the Second Amendment, which reads, "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."</p>
<p>There is under our decisions no reason why stiff state laws governing the purchase and possession of pistols may not be enacted. There is no reason why pistols may not be barred from anyone with a police record. There is no reason why a State may not require a purchaser of a pistol to pass a psychiatric test. There is no reason why all pistols should not be barred to everyone except the police.</p>
<p>The leading case is <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="103203"><a href="/opinion/103203/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">307 U. S. 174</a></span>, upholding a federal law making criminal the shipment in interstate commerce of a sawed-off shotgun. The law was upheld, there being no evidence that a sawed-off shotgun had "some reasonable relationship to the preservation or efficiency of a well regulated militia." <span class="citation" data-id="103203"><a href="/opinion/103203/united-states-v-miller/#178" aria-description="Citation for case: United States v. Miller"><i>Id.,</i> at 178</a></span>. The Second Amendment, it was held, "must be interpreted and applied" with the view of maintaining a "militia."</p>
<blockquote>"The Militia which the States were expected to maintain and train is set in contrast with Troops which they were forbidden to keep without the consent of Congress. The sentiment of the time strongly disfavored standing armies; the common view was that adequate defense of country and laws could be <span class="star-pagination">*151</span> secured through the Militiacivilians primarily, soldiers on occasion." <span class="citation" data-id="103203"><a href="/opinion/103203/united-states-v-miller/#178" aria-description="Citation for case: United States v. Miller"><i>Id.,</i> at 178-179</a></span>.</blockquote>
<p>Critics say that proposals like this water down the Second Amendment. Our decisions belie that argument, for the Second Amendment, as noted, was designed to keep alive the militia. But if watering-down is the mood of the day, I would prefer to water down the Second rather than the Fourth Amendment. I share with Judge Friendly a concern that the easy extension of <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, to "possessory offenses" is a serious intrusion on Fourth Amendment safeguards. "If it is to be extended to the latter at all, this should be only where observation by the officer himself or well authenticated information shows `that criminal activity may be afoot.' " <span class="citation" data-id="9456354"><a href="/opinion/293975/robert-williams-v-frederick-e-adams-warden-connecticut-state-prison/#39" aria-description="Citation for case: Robert Williams v. Frederick E. Adams, Warden,...">436 F. 2d, at 39</a></span>, quoting <i>Terry</i> v. <i>Ohio, supra,</i> at 30.</p>
<p>MR. JUSTICE BRENNAN, dissenting.</p>
<p>The crucial question on which this case turns, as the Court concedes, is whether, there being no contention that Williams acted voluntarily in rolling down the window of his car, the State had shown sufficient cause to justify Sgt. Connolly's "forcible" stop. I would affirm, believing, for the following reasons stated by Judge, now Chief Judge, Friendly, dissenting, <span class="citation" data-id="9456354"><a href="/opinion/293975/robert-williams-v-frederick-e-adams-warden-connecticut-state-prison/#38" aria-description="Citation for case: Robert Williams v. Frederick E. Adams, Warden,...">436 F. 2d 30, 38-39</a></span>, that the State did not make that showing:</p>
<blockquote>"To begin, I have the gravest hesitancy in extending [<i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968)] to crimes like the possession of narcotics . . . . There is too much danger that, instead of the stop being the object and the protective frisk an incident thereto, the reverse will be true. Against that we have here the added fact of the report that Williams had a gun on his person. . . . [But] Connecticut allows its citizens to carry weapons, concealed or <span class="star-pagination">*152</span> otherwise, at will, provided only they have a permit, <span class="citation no-link">Conn. Gen. Stat. §§ 29-35</span> and 29-38, and gives its police officers no special authority to stop for the purpose of determining whether the citizen has one. . . .</blockquote>
<blockquote>"If I am wrong in thinking that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> should not be applied at all to mere possessory offenses, . . . I would not find the combination of Officer Connolly's almost meaningless observation and the tip in this case to be sufficient justification for the intrusion. The tip suffered from a threefold defect, with each fold compounding the others. The informer was unnamed, he was not shown to have been reliable with respect to guns or narcotics, and he gave no information which demonstrated personal knowledge orwhat is worsecould not readily have been manufactured by the officer after the event. To my mind, it has not been sufficiently recognized that the difference between this sort of tip and the accurate prediction of an unusual event is as important on the latter score as on the former. [In <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959),] Narcotics Agent Marsh would hardly have been at the Denver Station at the exact moment of the arrival of the train Draper had taken from Chicago unless <i>someone</i> had told him <i>something</i> important, although the agent might later have embroidered the details to fit the observed facts. . . . There is no such guarantee of a patrolling officer's veracity when he testifies to a `tip' from an unnamed informer saying no more than that the officer will find a gun and narcotics on a man across the street, as he later does. If the state wishes to rely on a tip of that nature to validate a stop and frisk, revelation of the name of the informer or demonstration that his name is unknown and could <span class="star-pagination">*153</span> not reasonably have been ascertained should be the price.</blockquote>
<blockquote>"Terry v. Ohio was intended to free a police officer from the rigidity of a rule that would prevent his doing anything to a man reasonably suspected of being about to commit or having just committed a crime of violence, no matter how grave the problem or impelling the need for swift action, unless the officer had what a court would later determine to be probable cause for arrest. It was meant for the serious cases of imminent danger or of harm recently perpetrated to persons or property, not the conventional ones of possessory offenses. If it is to be extended to the latter at all, this should be only where observation by the officer himself or well authenticated information shows `that criminal activity may be afoot.' <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 30</a></span>. . . . I greatly fear that if the [contrary view] should be followed, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> will have opened the sluicegates for serious and unintended erosion of the protection of the Fourth Amendment."</blockquote>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE DOUGLAS joins, dissenting.</p>
<p>Four years have passed since we decided <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and its companion cases, <i>Sibron</i> v. <i>New York</i> and <i>Peters</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968). They were the first cases in which this Court explicitly recognized the concept of "stop and frisk" and squarely held that police officers may, under appropriate circumstances, stop and frisk persons suspected of criminal activity even though there is less than probable cause for an arrest. This case marks our first opportunity to give some flesh to the bones of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> <span class="star-pagination">*154</span> <i>et al.</i> Unfortunately, the flesh provided by today's decision cannot possibly be made to fit on <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>'s skeletal framework.</p>
<p>"[T]he most basic constitutional rule in this area is that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions.' The exceptions are `jealously and carefully drawn,' and there must be `a showing by those who seek exemption . . . that the exigencies of the situation made that course imperative.' `[T]he burden is on those seeking the exemption to show the need for it.' " <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span> (1971). In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> we said that "we do not retreat from our holdings that the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure." 392 U. S., at 20. Yet, we upheld the stop and frisk in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> because we recognized that the realities of on-the-street law enforcement require an officer to act at times on the basis of strong evidence, short of probable cause, that criminal activity is taking place and that the criminal is armed and dangerous. Hence, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stands only for the proposition that police officers have a "narrowly drawn authority to . . . search for weapons" without a warrant. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 27</a></span>.</p>
<p>In today's decision the Court ignores the fact that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> begrudgingly accepted the necessity for creating an exception from the warrant requirement of the Fourth Amendment and treats this case as if warrantless searches were the rule rather than the "narrowly drawn" exception. This decision betrays the careful balance that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> sought to strike between a citizen's right to privacy and his government's responsibility for effective law enforcement and expands the concept of warrantless <span class="star-pagination">*155</span> searches far beyond anything heretofore recognized as legitimate. I dissent.</p>
<p></p>
<h2>I</h2>
<p>A. The Court's opinion states the facts and I repeat only those that appear to me to be relevant to the Fourth Amendment issues presented.</p>
<p>Respondent was sitting on the passenger side of the front seat of a car parked on the street in a "high crime area" in Bridgeport, Connecticut, at 2:15 a. m. when a police officer approached his car. During a conversation that had just taken place nearby, the officer was told by an informant that respondent had narcotics on his person and that he had a gun in his waistband. The officer saw that the motor was not running, that respondent was seated peacefully in the car, and that there was no indication that he was about to leave the scene. After the officer asked respondent to open the door, respondent rolled down his window instead and the officer reached into the car and pulled a gun from respondent's waistband. The officer immediately placed respondent under arrest for carrying the weapon and searched him, finding heroin in his coat. More heroin was found in a later search of the automobile. Respondent moved to suppress both the gun and the heroin prior to trial. His motion was denied and he was convicted of possessing both items.</p>
<p>B. The Court erroneously attempts to describe the search for the gun as a protective search incident to a reasonable investigatory stop. But, as in <i>Terry, Sibron</i> and <i>Peters, supra,</i> there is no occasion in this case to determine whether or not police officers have a right to seize and to restrain a citizen in order to interrogate him. The facts are clear that the officer intended to make the search as soon as he approached the respondent. He asked no questions; he made no investigation; he simply searched. <span class="star-pagination">*156</span> There was nothing apart from the information supplied by the informant to cause the officer to search. Our inquiry must focus, therefore, as it did in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> on whether the officer had sufficient facts from which he could reasonably infer that respondent was not only engaging in illegal activity, but also that he was armed and dangerous. The focus falls on the informant.</p>
<p>The only information that the informant had previously given the officer involved homosexual conduct in the local railroad station. The following colloquy took place between respondent's counsel and the officer at the hearing on respondent's motion to suppress the evidence that had been seized from him.</p>
<blockquote>"Q. Now, with respect to the information that was given you about homosexuals in the Bridgeport Police Station [<i>sic</i>], did that lead to an arrest? A. No.</blockquote>
<blockquote>"Q. An arrest was not made. A. No. There was no substantiating evidence.</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. There was no substantiating evidence? A. No.</blockquote>
<blockquote>"Q. And what do you mean by that? A. I didn't have occasion to witness these individuals committing any crime of any nature.</blockquote>
<blockquote>"Q. In other words, after this person gave you the information, you checked for corroboration before you made an arrest. Is that right? A. Well, I checked to determine the possibility of homo-sexual activity.</blockquote>
<blockquote>"Q. And since an arrest was made, I take it you didn't find any substantiating information. A. I'm sorry counselor, you say since an arrest was made.</blockquote>
<blockquote>"Q. Was not made. Since an arrest was not made, I presume you didn't find any substantiating information. A. No.</blockquote>
<blockquote>
<span class="star-pagination">*157</span> "Q. So that, you don't recall any other specific information given you about the commission of crimes by this informant. A. No.</blockquote>
<blockquote>"Q. And you still thought this person was reliable. A. Yes."<sup>[1]</sup></blockquote>
<p>Were we asked to determine whether the information supplied by the informant was sufficient to provide probable cause for an arrest and search, rather than a stop and frisk, there can be no doubt that we would hold that it was insufficient. This Court has squarely held that a search and seizure cannot be justified on the basis of conclusory allegations of an unnamed informant who is allegedly credible. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964). In the recent case of <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), Mr. Justice Harlan made it plain beyond any doubt that where police rely on an informant to make a search and seizure, they must know that the informant is generally trustworthy and that he has obtained his information in a reliable way. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#417" aria-description="Citation for case: Spinelli v. United States"><i>Id.,</i> at 417</a></span>. Since the testimony of the arresting officer in the instant case patently fails to demonstrate that the informant was known to be trustworthy and since it is also clear that the officer had no idea of the source of the informant's "knowledge," a search and seizure would have been illegal.</p>
<p>Assuming, <i>arguendo,</i> that this case truly involves, not an arrest and a search incident thereto, but a stop and frisk,<sup>[2]</sup> we must decide whether or not the information possessed by the officer justified this interference with respondent's liberty. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> our only case to actually <span class="star-pagination">*158</span> uphold a stop and frisk,<sup>[3]</sup> is not directly in point, because the police officer in that case acted on the basis of his own personal observations. No informant was involved. But the rationale of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> is still controlling, and it requires that we condemn the conduct of the police officer in encountering the respondent.</p>
<p><i>Terry</i> did not hold that whenever a policeman has a hunch that a citizen is engaging in criminal activity, he may engage in a stop and frisk. It held that if police officers want to stop and frisk, they must have specific facts from which they can reasonably infer that an individual is engaged in criminal activity and is armed and dangerous.<sup>[4]</sup> It was central to our decision in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> that the police officer acted on the basis of his own personal observations and that he carefully scrutinized the conduct of his suspects before interfering with them in any way. When we legitimated the conduct of the officer in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> we did so because of the substantial <i>reliability</i> of the information on which the officer based his decision to act.</p>
<p>If the Court does not ignore the care with which we examined the knowledge possessed by the officer in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> when he acted, then I cannot see how the actions of the officer in this case can be upheld. The Court explains what the officer knew about respondent before accosting him. But what is more significant is what he did not know. With respect to the scene generally, the officer had no idea how long respondent had been in the car, how long the car had been parked, or to whom the car belonged. With respect to the gun,<sup>[5]</sup> the officer did not <span class="star-pagination">*159</span> know if or when the informant had ever seen the gun, or whether the gun was carried legally, as Connecticut law permitted, or illegally.<sup>[6]</sup> And with respect to the narcotics, the officer did not know what kind of narcotics respondent allegedly had, whether they were legally or illegally possessed, what the basis of the informant's knowledge was, or even whether the informant was capable of distinguishing narcotics from other substances.<sup>[7]</sup></p>
<p>Unable to answer any of these questions, the officer nevertheless determined that it was necessary to intrude on respondent's liberty. I believe that his determination was totally unreasonable. As I read <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> an officer may act on the basis of <i>reliable</i> information short of probable cause to make a stop, and ultimately a frisk, if necessary; but the officer may not use unreliable, unsubstantiated, conclusory hearsay to justify an invasion of liberty. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> never meant to approve the kind of knee-jerk police reaction that we have before us in this case.</p>
<p>Even assuming that the officer had some legitimate reason for relying on the informant, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> requires, before any stop and frisk is made, that the reliable information in the officer's possession demonstrate that the suspect is both armed and <i>dangerous.</i><sup>[8]</sup> The fact remains that <span class="star-pagination">*160</span> Connecticut specifically authorizes persons to carry guns so long as they have a permit. Thus, there was no reason for the officer to infer from anything that the informant said that the respondent was dangerous. His frisk was, therefore, illegal under <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i></p>
<p></p>
<h2>II</h2>
<p>Even if I could agree with the Court that the stop and frisk in this case was proper, I could not go further and sustain the arrest and the subsequent searches. It takes probable cause to justify an arrest and search and seizure incident thereto. Probable cause means that the "facts and circumstances before the officer are such as to warrant a man of prudence and caution in believing that the offence has been committed . . . ." <i>Stacey</i> v. <i>Emery,</i> <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (1878). "[G]ood faith is not enough to constitute probable cause." <i>Director General</i> v. <i>Kastenbaum,</i> <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/#28" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25, 28</a></span> (1923).</p>
<p>Once the officer seized the gun from respondent, it is uncontradicted that he did not ask whether respondent had a license to carry it, or whether respondent carried it for any other legal reason under Connecticut law. Rather, the officer placed him under arrest immediately and hastened to search his person. Since Connecticut has not made it illegal for private citizens to carry guns, there is nothing in the facts of this case to warrant a man "of prudence and caution" to believe that any offense had been committed merely because respondent had a gun on his person.<sup>[9]</sup> Any implication that respondent's silence <span class="star-pagination">*161</span> was some sort of a tacit admission of guilt would be utterly absurd.</p>
<p>It is simply not reasonable to expect someone to protest that he is not acting illegally before he is told that he is suspected of criminal activity. It would have been a simple matter for the officer to ask whether respondent had a permit, but he chose not to do so. In making this choice, he clearly violated the Fourth Amendment.</p>
<p>This case marks a departure from the mainstream of our Fourth Amendment cases. In <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948), for example, the arresting officer had an informant's tip and actually smelled opium coming from a room. This Court still found the arrest unlawful. And in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>, we found that there was no probable cause even where an informant's information was corroborated by personal observation. If there was no probable cause in those cases, I find it impossible to understand how there can be probable cause in this case.</p>
<p></p>
<h2>III</h2>
<p>MR. JUSTICE DOUGLAS was the sole dissenter in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>.</i> He warned of the "powerful hydraulic pressures throughout our history that bear heavily on the Court to water down constitutional guarantees . . . ." 392 U. S., at 39. While I took the position then that we were not watering down rights, but were hesitantly and cautiously striking a necessary balance between the rights of American citizens to be free from government intrusion into their <span class="star-pagination">*162</span> privacy and their government's urgent need for a narrow exception to the warrant requirement of the Fourth Amendment, today's decision demonstrates just how prescient MR. JUSTICE DOUGLAS was.</p>
<p>It seems that the delicate balance that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> struck was simply too delicate, too susceptible to the "hydraulic pressures" of the day. As a result of today's decision, the balance struck in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> is now heavily weighted in favor of the government. And the Fourth Amendment, which was included in the Bill of Rights to prevent the kind of arbitrary and oppressive police action involved herein, is dealt a serious blow. Today's decision invokes the specter of a society in which innocent citizens may be stopped, searched, and arrested at the whim of police officers who have only the slightest suspicion of improper conduct.</p>
<h2>NOTES</h2>
<p>[1]  Petitioner does not contend that Williams acted voluntarily in rolling down the window of his car.</p>
<p>[2]  Section 53-168 of the Connecticut General Statutes, in force at the time of these events, provided that a "person who knowingly makes to any police officer . . . a false report or a false complaint alleging that a crime or crimes have been committed" is guilty of a misdemeanor.</p>
<p>[3]  Figures reported by the Federal Bureau of Investigation indicate that 125 policemen were murdered in 1971, with all but five of them having been killed by gunshot wounds. Federal Bureau of Investigation Law Enforcement Bulletin, Feb. 1972, p. 33. According to one study, approximately 30% of police shootings occurred when a police officer approached a suspect seated in an automobile. Bristow, Police Officer ShootingsA Tactical Evaluation, 54 J. Crim. L. C. &amp; P. S. 93 (1963).</p>
<p>[1]  App. 96-97.</p>
<p>[2]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), makes it clear that a stop and frisk is a search and seizure within the meaning of the Fourth Amendment. When I use the term stop and frisk herein, I merely intend to emphasize that it is, as <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> held, a lesser intrusion than a full-scale search and seizure.</p>
<p>[3]  In <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968), the Court held that the action of the policeman could not be justified as a stop and frisk. In <i>Peters</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968), the Court sustained the validity of a search and seizure by holding that it was incident to a legal arrest.</p>
<p>[4]  <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span>; <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#64" aria-description="Citation for case: Sibron v. New York">392 U. S., at 64</a></span>.</p>
<p>[5]  The fact that the respondent carried his gun in a high-crime area is irrelevant. In such areas it is more probable than not that citizens would be more likely to carry weapons authorized by the State to protect themselves.</p>
<p>[6]  See Conn. Gen. Stat. Rev. § 29-35.</p>
<p>[7]  Connecticut permits possession of certain narcotics under specified circumstances<i>e. g.,</i> pursuant to a doctor's prescription. See Conn. Gen. Stat. Rev. §§ 19-443, 19-456 (c), 19-481.</p>
<p>[8]  The Court virtually ignores the requirement that the suspect be dangerous, as well as armed. Other courts have followed <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> more closely. See, <i>e. g., </i><i>Commonwealth</i> v. <i>Bourke,</i> <span class="citation" data-id="2084121"><a href="/opinion/2084121/commonwealth-v-bourke/#323" aria-description="Citation for case: Commonwealth v. Bourke">218 Pa. Super. 320, 323</a></span>, <span class="citation" data-id="2084121"><a href="/opinion/2084121/commonwealth-v-bourke/#427" aria-description="Citation for case: Commonwealth v. Bourke">280 A. 2d 425, 427</a></span> (1971); <i>Commonwealth</i> v. <i>Clarke,</i> <span class="citation" data-id="2084189"><a href="/opinion/2084189/commonwealth-v-clarke/#343" aria-description="Citation for case: Commonwealth v. Clarke">219 Pa. Super. 340, 343</a></span>, <span class="citation" data-id="2084189"><a href="/opinion/2084189/commonwealth-v-clarke/#663" aria-description="Citation for case: Commonwealth v. Clarke">280 A. 2d 662, 663</a></span> (1971); <i>Finley</i> v. <i>People,</i> <span class="citation" data-id="2614276"><a href="/opinion/2614276/finley-v-people/" aria-description="Citation for case: Finley v. People">176 Colo. 1</a></span>, <span class="citation" data-id="2614276"><a href="/opinion/2614276/finley-v-people/" aria-description="Citation for case: Finley v. People">488 P. 2d 883</a></span> (1971). See also <i>State</i> v. <i>Goudy,</i> <span class="citation" data-id="9541135"><a href="/opinion/1158944/state-v-goudy/#505" aria-description="Citation for case: State v. Goudy">52 Haw. 497, 505</a></span>, <span class="citation" data-id="9541135"><a href="/opinion/1158944/state-v-goudy/#805" aria-description="Citation for case: State v. Goudy">479 P. 2d 800, 805</a></span> (1971) (Abe, J., dissenting).</p>
<p>[9]  The Court appears to rely on the fact that the existence of the gun corroborated the information supplied to the officer by the informant. It cannot be disputed that there is minimal corroboration here, but the fact remains that the officer still lacked any knowledge that respondent had done anything illegal. Since carrying a gun is not <i>per se</i> illegal in Connecticut, the fact that respondent carried a gun is no more relevant to probable cause than the fact that his shirt may have been blue, or that he was wearing a jacket. Moreover, the fact that the informant can identify a gun on sight does not indicate an ability to do the same with narcotics. The corroboration of this one fact is a far cry from the corroboration that the Court found sufficient to sustain an arrest in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Agnello v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Agnello v. United States"
type: case
citation: "269 U.S. 20 (1925)"
parallel_cite: "46 S. Ct. 4; 70 L. Ed. 145; 51 A.L.R. 409"
neutral_cite: 1925 U.S. LEXIS 2
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1925
date_decided: 1925-10-12
docket: 6
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1925-10-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Agnello v. United States
  varies_by_point: false
  scope_note: "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100711/agnello-v-united-states/"
  cluster_id: 100711
  opinion_id: 100711
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Historical / Foundational"
related: ["[[Chimel v. California]]", "[[Go-Bart Importing Co. v. United States]]", "[[Weeks v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "home", "historical", "warrant-requirement"]
holding: "A search incident to arrest reaches the arrestee's person and the place where the arrest is made, but does not extend to a separate house blocks away that is entered and searched without a warrant after the arrest is complete and the suspects are in custody elsewhere."
lake:
  record_id: Agnello v. United States
  status: verified
  projected_at: 2026-07-06
---

# Agnello v. United States

*269 U.S. 20 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal revenue agents watched a cocaine sale at Alba's house and, when it was consummated, rushed in and arrested the defendants there, seizing cocaine on the table and on Frank Agnello's person. While some agents took the defendants to the station, others went — without a search warrant — to Frank Agnello's home several blocks away, searched his bedroom, and found a can of cocaine. That can was ultimately admitted against him.

## Issue
Whether the warrantless search of the arrestee's home, several blocks from the place of arrest and after he was in custody elsewhere, can be justified as a [[Search Incident to Arrest|search incident to arrest]].

## Rule
A [[Search Incident to Arrest|search incident to arrest]] is real but bounded to the arrest scene: "The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted." — 269 U.S. at 30. ^pin-30

But it does not reach a separate home: "But the right does not extend to other places. Frank Agnello's house was several blocks distant from Alba's house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests." — *Id.* at 30–31. ^pin-30a

## Application
The arrests and the searches and seizures at Alba's house — where the arrests occurred — were not questioned. But Agnello's house was blocks away; by the time agents entered and searched it without a warrant, the sale was over and the defendants were already in custody at or en route to the station. Nothing about the arrest justified that separate, later search, so the can of cocaine found in his bedroom was the product of an unreasonable warrantless search.

## Conclusion
Reversed. The warrantless search of Agnello's distant home could not be sustained as incident to the arrest; the evidence should have been excluded. *Agnello* fixes an early geographic and temporal limit on [[Search Incident to Arrest|search incident to arrest]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The limit survives and is consistent with the modern boundary drawn in [[Chimel v. California]] (SITA confined to the arrestee's person and the area within immediate control); it is companion to [[Go-Bart Importing Co. v. United States]] (no general exploratory search) and builds on [[Weeks v. United States]].

## Appears on
- [[SIA Persons]] — *Key — Historical / Foundational*

## Sources
- *Agnello v. United States*, 269 U.S. 20 (1925) — https://www.courtlistener.com/opinion/100711/agnello-v-united-states/ — pinpoints: 30, 31.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c2eba011975f1476", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Agnello v. United States"}, "payload": {"all": [{"cite": "269 U.S. 20", "page": "20", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "269"}, {"cite": "46 S. Ct. 4", "page": "4", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "46"}, {"cite": "70 L. Ed. 145", "page": "145", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "70"}, {"cite": "1925 U.S. LEXIS 2", "page": "2", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1925"}, {"cite": "51 A.L.R. 409", "page": "409", "reporter": "A.L.R.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "269 U.S. 20", "official": {"cite": "269 U.S. 20", "page": "20", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "269"}, "official_selection_present": true, "record_id": "Agnello v. United States"}}
{"assertion_id": "42ed07ef6d07ad81", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-30a", "record_id": "Agnello v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-30a", "pinpoint_status": "slip-only", "quote": "But the right does not extend to other places. Frank Agnello's house was several blocks distant from Alba's house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests.", "quote_fidelity": "mismatch", "record_id": "Agnello v. United States", "star_marker": null}}
{"assertion_id": "d09ac545bd23db24", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-30", "record_id": "Agnello v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-30", "pinpoint_status": "slip-only", "quote": "--- # Agnello v. United States *269 U.S. 20 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal revenue agents watched a cocaine sale at Alba's house and, when it was consummated, rushed in and arrested the defendants there, seizing cocaine on the table and on Frank Agnello's person. While some agents took the defendants to the station, others went — without a search warrant — to Frank Agnello's home several blocks away, searched his bedroom, and found a can of cocaine. That can was ultimately admitted against him. ## Issue Whether the warrantless search of the arrestee's home, several blocks from the place of arrest and after he was in custody elsewhere, can be justified as a search incident to arrest. ## Rule A search incident to arrest is real but bounded to the arrest scene:", "quote_fidelity": "mismatch", "record_id": "Agnello v. United States", "star_marker": null}}
{"assertion_id": "2e386f188c75b5f6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Agnello v. United States"}, "payload": {"as_of_content": "1925-10-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Agnello v. United States", "scope_note": "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California.", "varies_by_point": false}}
```

### lake record — Agnello v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Agnello v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Agnello v. United States",
    "case_name_short": "Agnello",
    "case_name_full": "AGNELLO Et Al. v. UNITED STATES",
    "input_case_name": "Agnello v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1925-10-12",
    "year": 1925,
    "docket": "6",
    "cluster_id": 100711,
    "lead_opinion_id": 100711,
    "sibling_ids": [
      100711
    ],
    "absolute_url": "/opinion/100711/agnello-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "269 U.S. 20",
      "volume": "269",
      "reporter": "U.S.",
      "page": "20",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "46 S. Ct. 4",
        "volume": "46",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 L. Ed. 145",
        "volume": "70",
        "reporter": "L. Ed.",
        "page": "145",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 A.L.R. 409",
        "volume": "51",
        "reporter": "A.L.R.",
        "page": "409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1925 U.S. LEXIS 2",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "269 U.S. 20",
        "volume": "269",
        "reporter": "U.S.",
        "page": "20",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "46 S. Ct. 4",
        "volume": "46",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "70 L. Ed. 145",
        "volume": "70",
        "reporter": "L. Ed.",
        "page": "145",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1925 U.S. LEXIS 2",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "2",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 A.L.R. 409",
        "volume": "51",
        "reporter": "A.L.R.",
        "page": "409",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "269 U.S. 20",
    "official_selection": {
      "court_class": "scotus",
      "selected": "269 U.S. 20",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-30",
      "page": null,
      "quote": "--- # Agnello v. United States *269 U.S. 20 (1925)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal revenue agents watched a cocaine sale at Alba's house and, when it was consummated, rushed in and arrested the defendants there, seizing cocaine on the table and on Frank Agnello's person. While some agents took the defendants to the station, others went \u2014 without a search warrant \u2014 to Frank Agnello's home several blocks away, searched his bedroom, and found a can of cocaine. That can was ultimately admitted against him. ## Issue Whether the warrantless search of the arrestee's home, several blocks from the place of arrest and after he was in custody elsewhere, can be justified as a search incident to arrest. ## Rule A search incident to arrest is real but bounded to the arrest scene:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-30a",
      "page": null,
      "quote": "But the right does not extend to other places. Frank Agnello's house was several blocks distant from Alba's house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1925-10-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Agnello v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational early limit on search incident to arrest; the rule that a SITA does not reach a separate home away from the arrest survives and is consistent with Chimel v. California.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Leonard",
          "cluster_id": 10789713,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camper",
          "cluster_id": 9454678,
          "cite": [
            "232 N.E.3d 419",
            "2023 Ohio 4673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Dragoo & Assocs., Inc.",
          "cluster_id": 9439763,
          "cite": [
            "229 N.E.3d 140",
            "2023 Ohio 4103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Renee Michelle Parady v. Commonwealth of Virginia",
          "cluster_id": 9411484,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 5290146,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hannah Marie Kilby",
          "cluster_id": 4893115,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Manuel Garcia",
          "cluster_id": 10109643,
          "cite": [
            "951 N.W.2d 631",
            "394 Wis. 2d 743",
            "2020 WI App 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whittington v. State",
          "cluster_id": 10021170,
          "cite": [
            "230 A.3d 148",
            "246 Md. App. 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4672578,
          "cite": [
            "2019 COA 159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 10048657,
          "cite": [
            "465 Md. 311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 4647520,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jessica M. Randall",
          "cluster_id": 4635900,
          "cite": [
            "930 N.W.2d 223",
            "2019 WI 80",
            "387 Wis. 2d 744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mayfield",
          "cluster_id": 4588394,
          "cite": [
            "434 P.3d 58",
            "192 Wash. 2d 871"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Corona",
          "cluster_id": 5310101,
          "cite": [
            "2018 UT App 154",
            "436 P.3d 174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 4433423,
          "cite": [
            "2017 Ohio 8141",
            "98 N.E.3d 1257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gutierrez-Hernandez v. State",
          "cluster_id": 4409141,
          "cite": [
            "221 So. 3d 792",
            "2017 Fla. App. LEXIS 10099",
            "2017 WL 2989013"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4408481,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4407393,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vincent Milewski v. Town of Dover",
          "cluster_id": 4407039,
          "cite": [
            "377 Wis. 2d 38",
            "2017 WI 79",
            "899 N.W.2d 303",
            "2017 WL 2883925",
            "2017 Wisc. LEXIS 396"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Leslie",
          "cluster_id": 4389764,
          "cite": [
            "477 Mass. 48",
            "76 N.E.3d 978"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. DAVID D. LEWIS",
          "cluster_id": 4281856,
          "cite": [
            "147 A.3d 236",
            "2016 D.C. App. LEXIS 369",
            "2016 WL 5539892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Int. of: I.M.S., a Minor",
          "cluster_id": 2898309,
          "cite": [
            "124 A.3d 311",
            "2015 Pa. Super. 188",
            "2015 Pa. Super. LEXIS 514"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington v. Heath T. Wisdom",
          "cluster_id": 2801822,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paselk, Ex Parte Carol",
          "cluster_id": 4262512,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Beatrice v. Meints",
          "cluster_id": 2757932,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Littell",
          "cluster_id": 2744514,
          "cite": [
            "2014 Ohio 4654"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Q. Gales v. State of Mississippi",
          "cluster_id": 2741345,
          "cite": [
            "153 So. 3d 632",
            "2014 Miss. LEXIS 501",
            "2014 WL 5035944"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended October 15, 2014 State of Iowa v. Justin Dean Short",
          "cluster_id": 4472150,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Dean Short",
          "cluster_id": 2687558,
          "cite": [
            "851 N.W.2d 474",
            "2014 WL 3537029",
            "2014 Iowa Sup. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gentle",
          "cluster_id": 6589626,
          "cite": [
            "80 Mass. App. Ct. 243",
            "952 N.E.2d 426",
            "2011 Mass. App. LEXIS 1134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harding",
          "cluster_id": 2550601,
          "cite": [
            "9 A.3d 547",
            "196 Md. App. 384",
            "2010 Md. App. LEXIS 182"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Marshall",
          "cluster_id": 2273474,
          "cite": [
            "319 S.W.3d 352",
            "2010 Ky. LEXIS 182",
            "2010 WL 3374171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 149658,
          "cite": [
            "609 F.3d 495",
            "2010 U.S. App. LEXIS 13200",
            "2010 WL 2574123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Belote v. State",
          "cluster_id": 1912680,
          "cite": [
            "981 A.2d 1247",
            "411 Md. 104",
            "2009 Md. LEXIS 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tatman",
          "cluster_id": 2482593,
          "cite": [
            "615 F. Supp. 2d 664",
            "2008 U.S. Dist. LEXIS 106022",
            "2008 WL 5431163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keith",
          "cluster_id": 3965884,
          "cite": [
            "178 Ohio App. 3d 46",
            "2008 Ohio 4326",
            "896 N.E.2d 764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith, 07-Ca-47 (7-25-2008)",
          "cluster_id": 4015581,
          "cite": [
            "2008 Ohio 3717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanders",
          "cluster_id": 1873366,
          "cite": [
            "2008 WI 85",
            "752 N.W.2d 713",
            "311 Wis. 2d 257",
            "2008 Wisc. LEXIS 336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sharpe",
          "cluster_id": 3971545,
          "cite": [
            "174 Ohio App. 3d 498",
            "2008 Ohio 267",
            "882 N.E.2d 960"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gray",
          "cluster_id": 2968497,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joshua Brent Gray, United States of America v. Terrence A. Askew",
          "cluster_id": 798157,
          "cite": [
            "491 F.3d 138",
            "2007 U.S. App. LEXIS 15760",
            "2007 WL 1881194"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Warren",
          "cluster_id": 1800687,
          "cite": [
            "949 So. 2d 1215",
            "2007 WL 530029"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sherman",
          "cluster_id": 1129307,
          "cite": [
            "931 So. 2d 286",
            "2006 WL 860652"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carvalho",
          "cluster_id": 1925493,
          "cite": [
            "892 A.2d 140",
            "2006 R.I. LEXIS 29",
            "2006 WL 537913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eckel",
          "cluster_id": 2112994,
          "cite": [
            "888 A.2d 1266",
            "185 N.J. 523",
            "2006 N.J. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 2639057,
          "cite": [
            "85 P.3d 887"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carpenter, Sheila",
          "cluster_id": 2971092,
          "cite": [
            "360 F.3d 591",
            "2004 WL 419906"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carpenter",
          "cluster_id": 785340,
          "cite": [
            "360 F.3d 591",
            "2004 U.S. App. LEXIS 4435"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spencer v. City of Bay City",
          "cluster_id": 2331528,
          "cite": [
            "292 F. Supp. 2d 932",
            "2003 U.S. Dist. LEXIS 21242",
            "2003 WL 22801139"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dunnuck v. State",
          "cluster_id": 1469197,
          "cite": [
            "786 A.2d 695",
            "367 Md. 198",
            "2001 Md. LEXIS 943"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gilley",
          "cluster_id": 4282804,
          "cite": [
            "56 M.J. 113",
            "2001 CAAF LEXIS 1378",
            "2001 WL 1441832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mason v. Wrightson",
          "cluster_id": 2206253,
          "cite": [
            "109 A.2d 128",
            "205 Md. 481"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 2269214,
          "cite": [
            "92 A.2d 743",
            "200 Md. 569"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Funkhouser",
          "cluster_id": 2386458,
          "cite": [
            "782 A.2d 387",
            "140 Md. App. 696",
            "2001 Md. App. LEXIS 161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parker",
          "cluster_id": 1401702,
          "cite": [
            "987 P.2d 73"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Matthews",
          "cluster_id": 4282934,
          "cite": [
            "53 M.J. 465",
            "2000 CAAF LEXIS 950",
            "2000 WL 1239211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moyer v. Commonwealth",
          "cluster_id": 1065604,
          "cite": [
            "531 S.E.2d 580",
            "33 Va. App. 8",
            "2000 Va. App. LEXIS 557"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moyer v. Commonwealth",
          "cluster_id": 1238318,
          "cite": [
            "520 S.E.2d 371",
            "30 Va. App. 744",
            "1999 Va. App. LEXIS 596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Longcore",
          "cluster_id": 2209414,
          "cite": [
            "593 N.W.2d 412",
            "226 Wis. 2d 1",
            "1999 Wisc. App. LEXIS 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glasco v. Commonwealth",
          "cluster_id": 1059787,
          "cite": [
            "513 S.E.2d 137",
            "257 Va. 433",
            "1999 Va. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wagoner",
          "cluster_id": 2609356,
          "cite": [
            "966 P.2d 176",
            "126 N.M. 9",
            "1998 NMCA 124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pierce v. Smith",
          "cluster_id": 12443,
          "cite": [
            "117 F.3d 866",
            "13 I.E.R. Cas. (BNA) 8",
            "1997 U.S. App. LEXIS 17907",
            "1997 WL 395259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Titus v. State",
          "cluster_id": 1728813,
          "cite": [
            "696 So. 2d 1257",
            "1997 WL 360959"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Accardi",
          "cluster_id": 3136153,
          "cite": [
            "284 Ill. App. 3d 31"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 2194990,
          "cite": [
            "676 N.E.2d 755",
            "1997 WL 33862"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kristopher Roth v. State",
          "cluster_id": 2859172,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roth v. State",
          "cluster_id": 1723172,
          "cite": [
            "917 S.W.2d 292",
            "1995 Tex. App. LEXIS 3296",
            "1995 WL 675583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stubbs",
          "cluster_id": 883728,
          "cite": [
            "892 P.2d 547",
            "270 Mont. 364",
            "52 State Rptr. 232",
            "1995 Mont. LEXIS 50"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pierce",
          "cluster_id": 2009627,
          "cite": [
            "642 A.2d 947",
            "136 N.J. 184",
            "1994 N.J. LEXIS 495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chun Yen Chiu",
          "cluster_id": 2008300,
          "cite": [
            "857 F. Supp. 353",
            "1993 U.S. Dist. LEXIS 20112",
            "1993 WL 721298"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkes v. United States",
          "cluster_id": 2329036,
          "cite": [
            "631 A.2d 880",
            "1993 D.C. App. LEXIS 233",
            "1993 WL 375307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Miller",
          "cluster_id": 7906180,
          "cite": [
            "29 Conn. App. 207",
            "614 A.2d 1229",
            "1992 Conn. App. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mullins",
          "cluster_id": 6080465,
          "cite": [
            "179 A.D.2d 48",
            "582 N.Y.S.2d 810",
            "1992 N.Y. App. Div. LEXIS 5279"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fairchild",
          "cluster_id": 1424081,
          "cite": [
            "829 P.2d 550",
            "121 Idaho 960",
            "1992 Ida. App. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Six Hundred Thirty-Nine Thousand Five Hundred and Fifty-Eight Dollars ($639,558) in United States Currency",
          "cluster_id": 577094,
          "cite": [
            "955 F.2d 712",
            "293 U.S. App. D.C. 384",
            "1992 U.S. App. LEXIS 1433",
            "1992 WL 18289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rivera",
          "cluster_id": 8708533,
          "cite": [
            "762 F. Supp. 49",
            "1991 U.S. Dist. LEXIS 4014",
            "1991 WL 60088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gordon v. State",
          "cluster_id": 1638510,
          "cite": [
            "801 S.W.2d 899",
            "1990 Tex. Crim. App. LEXIS 203",
            "1990 WL 199137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garcia",
          "cluster_id": 2437892,
          "cite": [
            "794 S.W.2d 472",
            "1990 WL 83587"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. O'DELL",
          "cluster_id": 1435360,
          "cite": [
            "576 A.2d 425",
            "1990 R.I. LEXIS 118",
            "1990 WL 79415"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camilleri",
          "cluster_id": 2143661,
          "cite": [
            "220 Cal. App. 3d 1199",
            "269 Cal. Rptr. 862",
            "1990 Cal. App. LEXIS 550"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Roundtree",
          "cluster_id": 1874558,
          "cite": [
            "694 F. Supp. 1230",
            "1988 WL 96725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crosby v. Commonwealth",
          "cluster_id": 1225752,
          "cite": [
            "367 S.E.2d 730",
            "6 Va. App. 193",
            "4 Va. Law Rep. 2341",
            "1988 Va. App. LEXIS 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Malik",
          "cluster_id": 1533332,
          "cite": [
            "534 A.2d 27",
            "221 N.J. Super. 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brunelle",
          "cluster_id": 1533148,
          "cite": [
            "534 A.2d 198",
            "148 Vt. 347",
            "1987 Vt. LEXIS 513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reed Wayne Hamilton v. Crispus Nix, Warden, and Attorney General of the State of Iowa",
          "cluster_id": 481691,
          "cite": [
            "809 F.2d 463",
            "1987 U.S. App. LEXIS 938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cathey",
          "cluster_id": 1658376,
          "cite": [
            "493 So. 2d 842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Voelkel v. State",
          "cluster_id": 2461220,
          "cite": [
            "717 S.W.2d 314",
            "1986 Tex. Crim. App. LEXIS 1274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Collins v. United States",
          "cluster_id": 2265688,
          "cite": [
            "491 A.2d 480"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kao",
          "cluster_id": 878927,
          "cite": [
            "697 P.2d 903",
            "215 Mont. 277"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph Joseph Palumbo",
          "cluster_id": 440435,
          "cite": [
            "742 F.2d 656",
            "1984 U.S. App. LEXIS 18582"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ortiz",
          "cluster_id": 1159713,
          "cite": [
            "683 P.2d 822",
            "67 Haw. 181",
            "1984 Haw. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "LeMasters v. People",
          "cluster_id": 1216986,
          "cite": [
            "678 P.2d 538",
            "1984 Colo. LEXIS 501"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ringer",
          "cluster_id": 1248379,
          "cite": [
            "674 P.2d 1240",
            "100 Wash. 2d 686",
            "1983 Wash. LEXIS 1922"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stackhouse v. State",
          "cluster_id": 2275066,
          "cite": [
            "468 A.2d 333",
            "298 Md. 203",
            "1983 Md. LEXIS 341"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dickson",
          "cluster_id": 2163530,
          "cite": [
            "144 Cal. App. 3d 1046",
            "192 Cal. Rptr. 897",
            "1983 Cal. App. LEXIS 1897"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lopez-Mendoza v. Immigration & Naturalization Service",
          "cluster_id": 8927000,
          "cite": [
            "705 F.2d 1059",
            "1983 U.S. App. LEXIS 28584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Castaneda v. State",
          "cluster_id": 5234027,
          "cite": [
            "650 S.W.2d 211",
            "1983 Tex. App. LEXIS 4340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell v. State",
          "cluster_id": 2456197,
          "cite": [
            "644 S.W.2d 554"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Calegar",
          "cluster_id": 1178435,
          "cite": [
            "661 P.2d 311",
            "104 Idaho 526",
            "1983 Ida. LEXIS 420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Golden v. State",
          "cluster_id": 1647005,
          "cite": [
            "429 So. 2d 45"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Caraher",
          "cluster_id": 1188275,
          "cite": [
            "653 P.2d 942",
            "293 Or. 741",
            "1982 Ore. LEXIS 1190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Duncan v. State",
          "cluster_id": 1518530,
          "cite": [
            "639 S.W.2d 314",
            "1982 Tex. Crim. App. LEXIS 1108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America Ex Rel. Ronald Doss v. Lou v. Brewer, Warden",
          "cluster_id": 407609,
          "cite": [
            "685 F.2d 1003"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Bradley",
          "cluster_id": 2119659,
          "cite": [
            "132 Cal. App. 3d 737",
            "183 Cal. Rptr. 434",
            "1982 Cal. App. LEXIS 1657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heumiller",
          "cluster_id": 1641433,
          "cite": [
            "317 N.W.2d 126",
            "1982 S.D. LEXIS 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Capps",
          "cluster_id": 1222613,
          "cite": [
            "641 P.2d 484",
            "97 N.M. 453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Congeni",
          "cluster_id": 3937272,
          "cite": [
            "445 N.E.2d 698",
            "3 Ohio App. 3d 392",
            "3 Ohio B. 457",
            "1981 Ohio App. LEXIS 10078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Evans",
          "cluster_id": 1899913,
          "cite": [
            "438 A.2d 340",
            "181 N.J. Super. 455"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Roberts",
          "cluster_id": 1502467,
          "cite": [
            "434 A.2d 257",
            "1981 R.I. LEXIS 1258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Henighan v. United States",
          "cluster_id": 2280122,
          "cite": [
            "433 A.2d 1059",
            "1981 D.C. App. LEXIS 315"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Parkhurst v. State",
          "cluster_id": 2605745,
          "cite": [
            "628 P.2d 1369",
            "1981 Wyo. LEXIS 347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Hernandez",
          "cluster_id": 389504,
          "cite": [
            "646 F.2d 970",
            "8 Fed. R. Serv. 794",
            "1981 U.S. App. LEXIS 12727"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Griffin",
          "cluster_id": 2613893,
          "cite": [
            "626 P.2d 478",
            "1981 Utah LEXIS 723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Donelson",
          "cluster_id": 2172888,
          "cite": [
            "302 N.W.2d 125",
            "1981 Iowa Sup. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Luz-Estella Alvarez-Porras, Jose Garcia-Perez, and Roberto Colon-Diaz",
          "cluster_id": 388070,
          "cite": [
            "643 F.2d 54",
            "8 Fed. R. Serv. 242",
            "1981 U.S. App. LEXIS 20295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ross v. Stahl",
          "cluster_id": 1512993,
          "cite": [
            "502 F. Supp. 107",
            "7 Fed. R. Serv. 1306",
            "1980 U.S. Dist. LEXIS 14639"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Spies",
          "cluster_id": 1242066,
          "cite": [
            "615 P.2d 710",
            "200 Colo. 434",
            "1980 Colo. LEXIS 709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Havens",
          "cluster_id": 110267,
          "cite": [
            "64 L. Ed. 2d 559",
            "100 S. Ct. 1912",
            "446 U.S. 620",
            "1980 U.S. LEXIS 103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christian v. State",
          "cluster_id": 1566358,
          "cite": [
            "592 S.W.2d 625",
            "1980 Tex. Crim. App. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heitman",
          "cluster_id": 1571293,
          "cite": [
            "589 S.W.2d 249",
            "1979 Mo. LEXIS 338"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Seidl",
          "cluster_id": 2263801,
          "cite": [
            "479 F. Supp. 771",
            "1979 U.S. Dist. LEXIS 8741"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Emmett Hoffman",
          "cluster_id": 370457,
          "cite": [
            "607 F.2d 280",
            "1979 U.S. App. LEXIS 10927"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ibn-Tamas v. United States",
          "cluster_id": 1910611,
          "cite": [
            "407 A.2d 626",
            "1979 D.C. App. LEXIS 457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Knox v. State",
          "cluster_id": 1632971,
          "cite": [
            "586 S.W.2d 504",
            "1979 Tex. Crim. App. LEXIS 1650"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. State",
          "cluster_id": 1510190,
          "cite": [
            "588 S.W.2d 348",
            "1979 Tex. Crim. App. LEXIS 1616"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Federici",
          "cluster_id": 1973144,
          "cite": [
            "179 Conn. 46",
            "425 A.2d 916",
            "1979 Conn. LEXIS 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Stanley",
          "cluster_id": 2082590,
          "cite": [
            "401 A.2d 1166",
            "265 Pa. Super. 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Seiss",
          "cluster_id": 1497008,
          "cite": [
            "402 A.2d 972",
            "168 N.J. Super. 269"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Anthony Hickey, United States v. William Lloyd Ferreira",
          "cluster_id": 365612,
          "cite": [
            "596 F.2d 1082",
            "1979 U.S. App. LEXIS 15297"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Erb, Mark C. Perschbacher, John E. Lavell, Michael S. Mosley",
          "cluster_id": 365526,
          "cite": [
            "596 F.2d 412",
            "1979 U.S. App. LEXIS 15624"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. J. Lee Havens",
          "cluster_id": 363621,
          "cite": [
            "592 F.2d 848",
            "1979 U.S. App. LEXIS 15634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Forsythe",
          "cluster_id": 364657,
          "cite": [
            "594 F.2d 947"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cadena",
          "cluster_id": 360399,
          "cite": [
            "585 F.2d 1252"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wise",
          "cluster_id": 5683261,
          "cite": [
            "46 N.Y.2d 321",
            "385 N.E.2d 1262",
            "413 N.Y.S.2d 334",
            "14 A.L.R. 4th 666",
            "1978 N.Y. LEXIS 2422"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garle A. Whitson",
          "cluster_id": 361132,
          "cite": [
            "587 F.2d 948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Warren",
          "cluster_id": 1417762,
          "cite": [
            "589 P.2d 1338",
            "121 Ariz. 306",
            "1978 Ariz. App. LEXIS 719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cadena",
          "cluster_id": 8919342,
          "cite": [
            "585 F.2d 1252",
            "1979 A.M.C. 1934"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brenneman v. State",
          "cluster_id": 1773897,
          "cite": [
            "573 S.W.2d 47",
            "264 Ark. 460",
            "1978 Ark. LEXIS 2141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Saundra Prescott",
          "cluster_id": 358848,
          "cite": [
            "581 F.2d 1343",
            "1978 U.S. App. LEXIS 9041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1225463,
          "cite": [
            "246 S.E.2d 780",
            "295 N.C. 488",
            "1978 N.C. LEXIS 1015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silo",
          "cluster_id": 2073312,
          "cite": [
            "389 A.2d 62",
            "480 Pa. 15",
            "1978 Pa. LEXIS 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Payton",
          "cluster_id": 5683033,
          "cite": [
            "45 N.Y.2d 300",
            "408 N.Y.S.2d 395",
            "1978 N.Y. LEXIS 2144",
            "380 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parkinson",
          "cluster_id": 2073303,
          "cite": [
            "389 A.2d 1",
            "1978 Me. LEXIS 770"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Means",
          "cluster_id": 876687,
          "cite": [
            "581 P.2d 406",
            "177 Mont. 193",
            "1978 Mont. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Providence Journal Co. v. Federal Bureau of Investigation",
          "cluster_id": 2093217,
          "cite": [
            "460 F. Supp. 762",
            "27 Fed. R. Serv. 2d 143",
            "1978 U.S. Dist. LEXIS 17769"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ward v. United States",
          "cluster_id": 1935714,
          "cite": [
            "386 A.2d 1180",
            "1978 D.C. App. LEXIS 375"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maxwell",
          "cluster_id": 2147794,
          "cite": [
            "78 Cal. App. 3d 124",
            "144 Cal. Rptr. 95",
            "1978 Cal. App. LEXIS 1289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Volpicelli v. Salamack",
          "cluster_id": 1620955,
          "cite": [
            "447 F. Supp. 652",
            "1978 U.S. Dist. LEXIS 19416"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shaw",
          "cluster_id": 2388761,
          "cite": [
            "383 A.2d 496",
            "476 Pa. 543",
            "1978 Pa. LEXIS 840"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Peterson v. State",
          "cluster_id": 1468214,
          "cite": [
            "379 A.2d 164",
            "281 Md. 309",
            "1977 Md. LEXIS 595"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stinchfield v. State",
          "cluster_id": 2056758,
          "cite": [
            "367 N.E.2d 1150",
            "174 Ind. App. 423",
            "1977 Ind. App. LEXIS 992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Isaacks v. State",
          "cluster_id": 1927176,
          "cite": [
            "350 So. 2d 1340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. George Moss and American Identification Products",
          "cluster_id": 349228,
          "cite": [
            "562 F.2d 155",
            "14 Collier Bankr. Cas. 2d 279",
            "1977 U.S. App. LEXIS 11674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Crawl",
          "cluster_id": 1892052,
          "cite": [
            "257 N.W.2d 86",
            "401 Mich. 1",
            "1977 Mich. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Courtney Batts",
          "cluster_id": 347031,
          "cite": [
            "558 F.2d 513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kidd",
          "cluster_id": 2168949,
          "cite": [
            "375 A.2d 1105",
            "281 Md. 32",
            "1977 Md. LEXIS 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perez",
          "cluster_id": 1817744,
          "cite": [
            "440 F. Supp. 272",
            "1977 U.S. Dist. LEXIS 16266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John R. James, Jr.",
          "cluster_id": 345567,
          "cite": [
            "555 F.2d 992",
            "181 U.S. App. D.C. 55",
            "1 Fed. R. Serv. 895",
            "1977 U.S. App. LEXIS 13953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Monahan",
          "cluster_id": 2229181,
          "cite": [
            "251 N.W.2d 421",
            "76 Wis. 2d 387",
            "261 N.W.2d 421",
            "1977 Wisc. LEXIS 1362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. John D. Ehrlichman",
          "cluster_id": 341470,
          "cite": [
            "546 F.2d 910",
            "178 U.S. App. D.C. 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cravero",
          "cluster_id": 340675,
          "cite": [
            "545 F.2d 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Tyler",
          "cluster_id": 1273756,
          "cite": [
            "250 N.W.2d 467",
            "399 Mich. 564"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carroll D. Ford. United States of America v. Wesley Dessaso A/K/A Wesley Dessaso, Jr. United States of America v. Steve F. Dacosta. United States of America v. Daniel Haile, Jr. United States of America v. Melvin E. Smith",
          "cluster_id": 344771,
          "cite": [
            "553 F.2d 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1722607,
          "cite": [
            "249 N.W.2d 693",
            "399 Mich. 350",
            "1976 Mich. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wolgemuth",
          "cluster_id": 2245378,
          "cite": [
            "356 N.E.2d 1139",
            "43 Ill. App. 3d 335",
            "1 Ill. Dec. 857",
            "1976 Ill. App. LEXIS 3294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfred B. Diggs",
          "cluster_id": 340058,
          "cite": [
            "544 F.2d 116",
            "1976 U.S. App. LEXIS 7361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cravero",
          "cluster_id": 8912462,
          "cite": [
            "545 F.2d 406",
            "2 Fed. R. Serv. 223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph Mariani",
          "cluster_id": 338326,
          "cite": [
            "539 F.2d 915",
            "1976 U.S. App. LEXIS 7955"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glover v. State",
          "cluster_id": 1296375,
          "cite": [
            "227 S.E.2d 921",
            "139 Ga. App. 162",
            "1976 Ga. App. LEXIS 1719"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. COOPER",
          "cluster_id": 1538291,
          "cite": [
            "240 Pa. Super. 477",
            "362 A.2d 1041",
            "1976 Pa. Super. LEXIS 1937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 5946417,
          "cite": [
            "52 A.D.2d 32",
            "382 N.Y.S.2d 399",
            "1976 N.Y. App. Div. LEXIS 11525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 1774097,
          "cite": [
            "572 S.W.2d 507",
            "1976 Tex. Crim. App. LEXIS 1210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Disbrow",
          "cluster_id": 1185789,
          "cite": [
            "545 P.2d 272",
            "16 Cal. 3d 101",
            "127 Cal. Rptr. 360",
            "1976 Cal. LEXIS 210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Diaz",
          "cluster_id": 6354097,
          "cite": [
            "85 Misc. 2d 41",
            "1975 N.Y. Misc. LEXIS 3274",
            "376 N.Y.S.2d 849"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane1_negative"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glasser v. United States",
          "cluster_id": 103597,
          "cite": [
            "315 U.S. 60",
            "62 S. Ct. 457",
            "86 L. Ed. 680",
            "1942 U.S. LEXIS 979"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 106022,
          "cite": [
            "4 L. Ed. 2d 697",
            "80 S. Ct. 725",
            "362 U.S. 257",
            "1960 U.S. LEXIS 1413",
            "78 A.L.R. 2d 233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Draper v. United States",
          "cluster_id": 105820,
          "cite": [
            "3 L. Ed. 2d 327",
            "79 S. Ct. 329",
            "358 U.S. 307",
            "1959 U.S. LEXIS 1607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
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
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston v. United States",
          "cluster_id": 106771,
          "cite": [
            "11 L. Ed. 2d 777",
            "84 S. Ct. 881",
            "376 U.S. 364",
            "1964 U.S. LEXIS 1578"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Agnello v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100711) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODY4ODMyMDAwMDAmcz02MzU0MDk3JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100711%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 194
      },
      "lane2_top_cited": {
        "query": "cites:(100711)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDIzJnM9MTA1MTg4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28100711%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(100711)",
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
    "complete_query": "cites:(100711)",
    "indexed_citing_opinions": 1070,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100711,
        "count": 1070,
        "count_source": "search"
      }
    ],
    "citation_count": 1597,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/agnello-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU0NzM2NDImcz00NDA4NDgxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28100711%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100711,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 94272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100711,
        "cited_id": 3502705,
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
    "date_created": "2026-07-04T15:53:16Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T16:18:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T15:53:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Agnello v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion data-order="23" data-type="opinion" id="x999-1" type="majority">
<author id="b79-9">
  Mr. Justice Butler
 </author>
<p id="AG">
  delivered the opinion of the Court.
 </p>
<p id="b79-10">
  Thomas Agnello, Frank Agnello, Stephen Alba, Antonio Centorino and Thomas Pace were indicted in the District Court, Eastern District of New York, under § 37, Criminal Code, c. 321, <span class="citation no-link">35 Stat. 1088</span>, 1096, for a conspiracy to violate the Harrison Act, c. 1, <span class="citation no-link">38 Stat. 785</span>, as amended by
  <span citation-index="1" class="star-pagination" label="28"> 
   *28
   </span>
  • §§1006, 1007, 1008 of the Revenue Act of 1918, c. 18, <span class="citation no-link">40 Stat. 1057,1130</span>. The indictment charges that defendants conspired together to sell cocaine without having registered with the Collector of Internal Revenue and without having paid the prescribed tax. The overt acts charged are that defendants had cocaine in their possession, solicited'the sale of it, met in the home of defendant Alba at---.l-38 Union Street, Brooklyn, and made arrangéments ■ for the purpose of selling it, brought ,a large quantity of it to that place, and sold it in violation of the Act. The jury found defendants guilty. Each was sentenced to serve two years in the penitentiary and to pay a fine of $5,000. The Circuit Court of Appeals affirmed the judgment. <span class="citation" data-id="8831130"><a href="/opinion/8845856/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">290 Fed. 671</a></span>.
 </p>
<p id="b80-5">
  The evidence introduced by the Government was sufficient to warrant a finding of the following facts: Pasquale Napolitano and Nunzio Dispenza, employed by government revenue agents for that purpose, went to the home of Alba, Saturday, January 14, 1922, and there offered to buy. narcotics from Alba and Centorino. Alba gave them some samples. They arranged to come again on Monday following. They returned at the time agreed. Six revenue agents and a city policeman followed them and remained oh watch outside. Alba left the house and returned with Centorino. They did not then produce any drug. After discussion and the refusal of Napolitano' and Dispenza to go to Centorino’s house to get the drug, Centorino went to fetch it. He was followed by some of the agents. He first went to his own house, 172 Columbia Street; thence to 167 Columbia Street, — one part of which was a grocery store belonging to Pace and Thomas Agnello, and another part of which, connected with the grocery store, was the home of Frank Agnello and Pace. In a short time, Centorino, Pace and the Agnellos came out of the last mentioned place, and all went to Alba’s house. Looking through the windows, those on watch saw
  <span citation-index="1" class="star-pagination" label="29"> 
   *29
   </span>
  Frank Agnello produce a number of small packages for delivery to Napolitano and saw the latter hand over money to Alba. Upon the apparent consummation of the sale, the agents rushed in and arrested all the defendants. They found some of the packages on the table where the. transaction took place and found others in the pockets of Frank Agnello. All contained cocaine. On searching Alba, they found the money given him by Napolitano.
 </p>
<p id="b81-6">
  And as a part of its case in chief, the Government offered testimony tending to show .that, while some of the revenue agents were taking the defendants to the police station, the others and the city policeman went to the home of Centorino and searched it but did not find any narcotics; that they then went to 167 Columbia Street and searched it, and in Frank Agnello’s bedroom found a can of cocaine which was produced and offered in evidence. The evidence w,as excluded on the ground that the search and seizure were made without a search warrant. In defense, Centorino and others gave testimony to the effect that the packages of cocaine which were brought to arid seized in Alba’s house at the time of the arrests had been furnished to Centorino by Dispenza to induce an ap - parent sale of cocaine to Napolitano, that is, to incite crime or acts having the appearance of crime, for the purpose of entrapping and punishing defendants. Centorino testified that, after leaving Napolitano and Dispenza with Alba at the latter’s home, he went to his own house and got the packages of cocaine which had been given him by Dispenza and took them to 167 Columbia Street, and there gave them to Frank Agnello to be taken to Alba’s house. Frank Agnello testified on direct examination that he received the packages from Centorino but that he did not know their contents, and that he would not have carried them if he had known that they contained cocaine or narcotics. On cross examination, he said that he had never seen narcotics. Then, notwithstanding objection
  <span citation-index="1" class="star-pagination" label="30"> 
   *30
   </span>
  by defendants, the prosecuting attorney produced the can of cocaine which the Government claimed was seized in Agnello’s bedroom and asked him whether he had ever seen it. He said he had not, and specifically stated he had never seen it in his house. In rebuttal, over objec-. tions of defendants, the Government was permitted to put in the evidence of the search and seizure of the can of cocaine in Frank Agnello’s room, which theretofore had been offered and excluded.
 </p>
<p id="b82-4">
  The case involves the questions whether search of the house of Frank’ Agnello and seizure of the cocaine there found, without a search warrant, violated the Fourth Amendment, and whether the admission of evidence of such search and seizure violated the Fifth Amendment. The Fourth Amendment is: “The.right of the people to be secure in their persons, houses; papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” The provision of the Fifth Amend-. ment invoked is this: “No person . . . shall be compelled in any criminal case to be a witness against himself:”
 </p>
<p id="b82-5">
  The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as. its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>;
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>. The legality of the arrests or of the searches and seizures made at the home of Alba is not questioned. Such searches and seizures naturally and usually appertain to and attend such arrests. But the right does not extend to other places. Frank Agnello’s
  <span citation-index="1" class="star-pagination" label="31"> 
   *31
   </span>
  house was several blocks distant from Alba’s house, where the arrest was made. When it was entered and searched, the conspiracy was ended and the defendants were under arrest and in custody elsewhere. That search cannot be sustained as an incident of the arrests. See
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 391</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   Conway,
  </em>
  <span class="citation" data-id="3502705"><a href="/opinion/3532274/people-v-conway/" aria-description="Citation for case: People v. Conway">225 Mich. 152</a></span>;
  <em>
   Gamble
  </em>
  v.
  <em>
   Keyes,
  </em>
  35 S. D. 645, 650.
 </p>
<p id="b83-6">
  Under the Harrison Act (§ 8; § 1 as amended by § 1006) it is unlawful for any person who has not registered and paid a special tax, to have cocaine in his possession, and all unstamped packages of such drug found in his possession are subject to forfeiture. We assume, as contended by the Government, that defendants obtained from Frank Agnello’s house the cocaine that was taken to Alba’s house and there seized; that, the can of cocaine which later was found in Agnello’s house was unlawfully in his control and subject to seizure, and that it was a part of the cocaine which was the subject matter of the conspiracy.
 </p>
<p id="b83-7">
  The Government cites
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra;
  </em>
  but it does not support the search and seizure complained of. That case involved the legality of a search of an automobile and the seizure of intoxicating liquors being transported therein in violation of the National Prohibition Act. The search and seizure were made by prohibition agents without a warrant. After referencé to various acts of Congress relating to the seizure of contraband goods, the court said (p. 153):
  <em>
   “
  </em>
  We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a
  <span citation-index="1" class="star-pagination" label="32"> 
   *32
   </span>
  search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.” It was held that,
  <em>
   “
  </em>
  The facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient in themselves to warrant a man of reasonable caution in the belief that intoxicating liquor was being' transported in the automobile which they stopped and searched.” (p. 162.) And on that ground the court held the search and seizure without warrant justified.
 </p>
<p id="b84-6">
  While the question has never been directly decided by this court, it has always been assumed that one’s house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest therein:
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624</a></span>,
  <em>
   et seq.,
  </em>
  630;
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  393;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  391;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#308" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 308</a></span>. The protection of the Fourth Amendment extends to all equally, — to those justly suspected or accused, as well as to the innocent. The search of a private dwelling without a warrant is in itself unreasonable and abhorrent to our laws. Congress has never passed an act purporting to authorize the search of a house without a warrant. On the other hand, special limitations have been set about the obtaining of search warrants for that purpose. Thus, the National Prohibition Act, approved October 28, 1919, c. 85, Tit. II, § 25, <span class="citation no-link">41 Stat. 305</span>, 315-, provides that no search warrant shall issue to search any private dwelling occupied as such unless it is being used for the unlawful sale of intoxicating liquor or is in part used for business purposes, such as store, shop, saloon, restaurant, hotel or boarding house. And later, to the end that government employees without a warrant shall not invade the homes of the people and violate the priva
  <span citation-index="1" class="star-pagination" label="33"> 
   *33
   </span>
  cies of life, Congress made it a criminal offense, punishable by heavy penalties, for any officer, agent or employee of the United States engaged in the enforcement of any law to search a private dwelling house without a warrant directing such search. Act of November 23, 1921, c. 134, § 6, <span class="citation no-link">42 Stat. 222</span>, 223. Safeguards similar to the Fourth Amendment are deemed necessary and have been provided in the. constitution or laws of every State of the Union.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  We think there is no state statute authorizing the search of a house without a warrant; and, in a number of state laws recently enacted for the enforcement of prohibition in respect of intoxicating liquors, there are provisions similar to- those in § 25 of the National Prohibition Act. Save in certain cases as incident to arrest, there is no sanction in the decisions of the courts, federal or state, for the search of a private dwelling house without a warrant. Absence of any judicial approval is persuasive authority that it is unlawful. See
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington,
  </em>
  19 Howard’s State Trials, 1030, 1066. Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause. See
  <em>
   Temperani
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9335965"><a href="/opinion/9340620/temperani-v-united-states/" aria-description="Citation for case: Temperani v. United States">299 Fed. 365</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Rembert,
  </em>
  <span class="citation" data-id="8827993"><a href="/opinion/8842783/united-states-v-rembert/#1000" aria-description="Citation for case: United States v. Rembert">284 Fed. 996, 1000</a></span>;
  <em>
   Connelly
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8822127"><a href="/opinion/8837062/connelly-v-united-states/" aria-description="Citation for case: Connelly v. United States">275 Fed. 509</a></span>;
  <em>
   McClurg
  </em>
  v.
  <em>
   Brenton,
  </em>
  <span class="citation" data-id="7110885"><a href="/opinion/7199636/mcclurg-v-brenton/#372" aria-description="Citation for case: McClurg v. Brenton">123 Ia. 368, 372</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   Margolis,
  </em>
  <span class="citation" data-id="7951962"><a href="/opinion/7998119/people-v-margolis/" aria-description="Citation for case: People v. Margolis">220 Mich. 431</a></span>;
  <em>
   Childers
  </em>
  v.
  <em>
   Commonwealth,
  </em>
  <span class="citation" data-id="7148020"><a href="/opinion/7235601/childers-v-commonwealth/" aria-description="Citation for case: Childers v. Commonwealth">198 Ky. 848</a></span>;
  <em>
   State
  </em>
  v.
  <em>
   Warfield,
  </em>
  <span class="citation" data-id="8194400"><a href="/opinion/8230088/state-v-warfield/" aria-description="Citation for case: State v. Warfield">184 Wis. 56</a></span>. The search of Frank Agnello’s house and seizure of the can of cocaine violated the Fourth Amendment.
 </p>
<p id="b85-6">
  It' is well settled that, when properly invoked, the Fifth Amendment protects every person from incrimination by
  <span citation-index="1" class="star-pagination" label="34"> 
   *34
   </span>
  the use of evidence obtained through search or seizure made in violation of his rights under the Fourth Amendment.
  <em>
   Boyd v. United States, supra,
  </em>
  630,
  <em>
   et seq.; Weeks
  </em>
  v.
  <em>
   United States, supra,
  </em>
  398;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  391, 392;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, supra,
  </em>
  306;
  <em>
   Amos
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#316" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 316</a></span>. The Government contends that, even if the search and seizure were unlawful, the evidence was admissible because no application on behálf of defendant was made to the court for the return of the can of cocaine. The reason for such application, where required, is that the court will not pause in ,a criminal case to determine collateral issues as to how the evidence was obtained. See
  <em>
   Adams v. New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#594" aria-description="Citation for case: Adams v. New York">192 U. S. 585, 594</a></span>, affirming <span class="citation multiple-matches"><a href="/c/N.%20Y./176/351/">176 N. Y. 351</a></span>. But in this case, the facts disclosing that the search and- seizure violated the Fourth Amendment were not in controversy.. They were shown by the examination of the witness called to give the evidence. There was no search warrant; and from the first, the position of the Government has been that none was necessary. In substance, Frank Agnello testified that he never had possession of the can of cocaine and never saw it until it was produced in court. Thére is nothing to show that, in advance of its offer in evidence, he knew that the Government claimed it had searched his house and found cocaine there, or that the prosecutor intended to introduce evidence of any search or seizure. It would be unreasonable to hold that he was bound to apply for the return of an article which he maintained he never had. Where, by uncontroverted facts, it appears that a search ,and seizure were made in violation of the Fourth Amendment, there is no reason why one whose rights have been so violated and who is sought to be incriminated by evidence so obtained, may not invoke protection of the Fifth Amendment immediately and without any application for the return of the thing seized. “A rule of practice must not be allowed for any technical reason to prevail over
  <span citation-index="1" class="star-pagination" label="35"> 
   *35
   </span>
  a constitutional right.”
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, supra,
  </em>
  313. And the contention that the evidence of the search and seizure was admissible in rebuttal is without merit. In his direct examination, Agnello was not asked and did not testify concerning the can of cocaine. In cross-examination, in answer to; a question permitted over his objection, he said he had never seen it. He did nothing to waive his constitutional protection or to justify cross-examination in respect of the evidence claimed to have been obtained by the search. As said in
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, supra,
  </em>
  392, “ The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be. used at all.” The admission of evidence obtained by the search and seizure was error and prejudicial to the substantial rights of Frank Agnello. The judgment against him must be set aside and a new trial awarded.
 </p>
<p id="b87-6">
  But the judgment against the other defendants may stand. The introduction of the evidence of the search and seizure did not transgress their constitutional rights. And it was not prejudicial error against them. The possession by Frank Agnello of the can of cocaine which was seized tended to show guilty knowledge and criminal intent on his part; but it was not submitted as attributable to the other defendants. During the summing up of the case to the jury by the prosecuting attorney, the court distinctly ^ indicated that the evidence was admissible only against Frank Agnello. The other defendants did not request any instruction to the jury in reference to the matter, and they do not contend that any erroneous instruction was given.
  <em>
   Isaacs
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94272"><a href="/opinion/94272/isaacs-v-united-states/#491" aria-description="Citation for case: Isaacs v. United States">159 U. S. 487, 491</a></span>.
 </p>
<p id="b87-7">
  The packages of-cocaine seized at-Alba’s house were carried to'that place by Frank Agnello. He did this at the instance of Centorino; and in his behalf it is claimed he acted innocently and without knowledge of the con
  <span citation-index="1" class="star-pagination" label="36"> 
   *36
   </span>
  tents of the package. The evidence of the search and seizure made in his house tended to show that he knew what he was doing and was a willing participant in the conspiracy charged. But so far as concerns the other defendants, it is immaterial whether he acted innocently and without knowledge of the contents of the package or knowingly to effect the object of the conspiracy. In either case, his act would be equally chargeable to his codefendants. They are not entitled to a new trial. See
  <em>
   Rossi
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8824066"><a href="/opinion/8838959/rossi-v-united-states/#354" aria-description="Citation for case: Rossi v. United States">278 Fed. 349, 354</a></span>;
  <em>
   Belfi
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8812898"><a href="/opinion/8828045/belfi-v-united-states/#828" aria-description="Citation for case: Belfi v. United States">259 Fed. 822, 828</a></span>;
  <em>
   Feder et al.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8811695"><a href="/opinion/8826870/feder-v-united-states/" aria-description="Citation for case: Feder v. United States">257 Fed. 694</a></span>;
  <em>
   Browne
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8760616"><a href="/opinion/8776964/browne-v-united-states/#13" aria-description="Citation for case: Browne v. United States">145 Fed. 1, 13</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Cohn,
  </em>
  <span class="citation" data-id="8753798"><a href="/opinion/8770268/united-states-v-cohn/#626" aria-description="Citation for case: United States v. Cohn">128 Fed. 615, 626</a></span>.
 </p>
<judges id="b88-5">
<em>
   Judgment against Frank Agnello reversed; judgment against other defendants affirmed.
  </em>
</judges>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b85-7">
   See p. 1268, Index Digest of State Constitutions (prepared for New York State Constitutional Convention Commission, 1915); also § 8, c. 7, Consolidated Laws, New York, as amended by L. 1923, c. 80.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Aguilar v. Texas.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Aguilar v. Texas"
type: case
citation: "378 U.S. 108 (1964)"
parallel_cite: "84 S. Ct. 1509; 12 L. Ed. 2d 723"
neutral_cite: 1964 U.S. LEXIS 994
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1964-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Aguilar v. Texas
  varies_by_point: false
  scope_note: "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106865/aguilar-v-texas/"
  cluster_id: 106865
  opinion_id: 106865
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Anchor"
related: ["[[Illinois v. Gates]]", "[[Spinelli v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "historical"]
holding: "A magistrate may issue a warrant on an informant's hearsay only if the affidavit shows **(1) the informant's basis of knowledge** (how…"
lake:
  record_id: Aguilar v. Texas
  status: verified
  projected_at: 2026-07-09
---

# Aguilar v. Texas

*378 U.S. 108 (1964)* · U.S. Supreme Court · **Historical** · Treatment: **abrogated** *(as of 2026-06-30)* — abrogated by [[Illinois v. Gates]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Houston officers obtained a warrant to search for narcotics on an affidavit that recited only that the affiants "have received reliable information from a credible person and do believe" that narcotics were being kept at the premises. The affidavit gave no underlying facts — neither how the informant knew nor why he was believed. The warrant issued and evidence was seized and used to convict.

## Issue
Whether an affidavit resting solely on an informant's tip — stated as a conclusion, without underlying facts showing the informant's basis of knowledge or his credibility — can support a magistrate's finding of probable cause.

## Rule
No. An affidavit may rest on hearsay, but the magistrate must be given the underlying facts behind both the informant's knowledge and his reliability. The "magistrate must be informed of some of the underlying circumstances from which the informant concluded that the narcotics were where he claimed they were, and some of the underlying circumstances from which the officer concluded that the informant . . . was 'credible' or his information 'reliable.'" — 378 U.S. at 114. ^pin-114

Otherwise the probable-cause inference is drawn not "by a neutral and detached magistrate," as the Constitution requires, "but instead, by a police officer 'engaged in the often competitive enterprise of ferreting out crime.'" — [*Id.* at 115](https://www.courtlistener.com/opinion/106865/aguilar-v-texas/#:~:text=by%20a%20neutral%20and%20detached%20magistrate%2C). ^pin-115

## Application
The affidavit here was a bare conclusion: it offered the magistrate no underlying circumstances showing how the informant learned that narcotics were on the premises, and none showing why the informant was credible or his information reliable. On these facts the magistrate could only accept the informant's "suspicion," "belief," or "mere conclusion" without question, so the warrant lacked a sufficient basis and should not have issued.

## Conclusion
The search warrant was invalid for want of probable cause; the judgment resting on the seized evidence was reversed.

## Treatment & subsequent history
- **Status:** abrogated *(as of 2026-06-30)* — **Historical** (tier 6).
- The rigid two-prong "basis of knowledge" + "veracity" framework of *Aguilar* (with [[Spinelli v. United States]]) was **abandoned by [[Illinois v. Gates]]** (1983) in favor of a **totality-of-the-circumstances** test. Under *[[Illinois v. Gates|Gates]]*, the informant's basis of knowledge and veracity remain relevant considerations but are no longer independent, dispositive requirements.

## Appears on
- [[Probable Cause]] — *Key — Anchor*

## Sources
- *Aguilar v. Texas*, 378 U.S. 108 (1964) — https://www.courtlistener.com/opinion/106865/aguilar-v-texas/ — pinpoints: 114, 115.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8ebfada09b7c96d1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Aguilar v. Texas"}, "payload": {"all": [{"cite": "378 U.S. 108", "page": "108", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "378"}, {"cite": "84 S. Ct. 1509", "page": "1509", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "12 L. Ed. 2d 723", "page": "723", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "12"}, {"cite": "1964 U.S. LEXIS 994", "page": "994", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "378 U.S. 108", "official": {"cite": "378 U.S. 108", "page": "108", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "378"}, "official_selection_present": true, "record_id": "Aguilar v. Texas"}}
{"assertion_id": "8534798cbe5fd59b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-114", "record_id": "Aguilar v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-114", "pinpoint_status": "slip-only", "quote": "that narcotics were being kept at the premises. The affidavit gave no underlying facts — neither how the informant knew nor why he was believed. The warrant issued and evidence was seized and used to convict. ## Issue Whether an affidavit resting solely on an informant's tip — stated as a conclusion, without underlying facts showing the informant's basis of knowledge or his credibility — can support a magistrate's finding of probable cause. ## Rule No. An affidavit may rest on hearsay, but the magistrate must be given the underlying facts behind both the informant's knowledge and his reliability. The", "quote_fidelity": "mismatch", "record_id": "Aguilar v. Texas", "star_marker": null}}
{"assertion_id": "f93885eb2cad5a74", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-115", "record_id": "Aguilar v. Texas"}, "payload": {"fragment": "#:~:text=by%20a%20neutral%20and%20detached%20magistrate%2C", "page": null, "pin_id": "pin-115", "pinpoint_status": "star-verified", "quote": "by a neutral and detached magistrate,", "quote_fidelity": "matched", "record_id": "Aguilar v. Texas", "star_marker": "115"}}
{"assertion_id": "9b7a962c648a07fd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Aguilar v. Texas"}, "payload": {"as_of_content": "1964-06-15", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Aguilar v. Texas", "scope_note": "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).", "varies_by_point": false}}
```

### lake record — Aguilar v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Aguilar v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Aguilar v. Texas",
    "case_name_short": "Aguilar",
    "case_name_full": "Aguilar v. Texas",
    "input_case_name": "Aguilar v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-15",
    "year": 1964,
    "docket": null,
    "cluster_id": 106865,
    "lead_opinion_id": 106865,
    "sibling_ids": [
      106865,
      9422845,
      9422846,
      9422847
    ],
    "absolute_url": "/opinion/106865/aguilar-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 108",
      "volume": "378",
      "reporter": "U.S.",
      "page": "108",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1509",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1509",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 723",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 994",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "994",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 108",
        "volume": "378",
        "reporter": "U.S.",
        "page": "108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1509",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1509",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 723",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 994",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "994",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 108",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 108",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "that narcotics were being kept at the premises. The affidavit gave no underlying facts \u2014 neither how the informant knew nor why he was believed. The warrant issued and evidence was seized and used to convict. ## Issue Whether an affidavit resting solely on an informant's tip \u2014 stated as a conclusion, without underlying facts showing the informant's basis of knowledge or his credibility \u2014 can support a magistrate's finding of probable cause. ## Rule No. An affidavit may rest on hearsay, but the magistrate must be given the underlying facts behind both the informant's knowledge and his reliability. The",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-115",
      "page": null,
      "quote": "by a neutral and detached magistrate,",
      "star_marker": "115",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13622,
      "fragment": "#:~:text=by%20a%20neutral%20and%20detached%20magistrate%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1964-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Aguilar v. Texas",
    "varies_by_point": false,
    "scope_note": "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": "462 U.S. 213",
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:abrogated"
      },
      {
        "citing_case": {
          "name": "In re Grijalva; Judith del Cuadro-Zimmerman",
          "cluster_id": 10847130,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mercer",
          "cluster_id": 10803481,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Leighton R.",
          "cluster_id": 10742062,
          "cite": [
            "2025 NY Slip Op 06534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luis Morales",
          "cluster_id": 10734924,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "FRASER, MARIAN v. the State of Texas",
          "cluster_id": 10667479,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wilson",
          "cluster_id": 10664712,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Silva",
          "cluster_id": 10640306,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Brandon Tylor Mulac",
          "cluster_id": 10633329,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 10582111,
          "cite": [
            "2025 NY Slip Op 25109"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ball v. New York State Dept. of Health",
          "cluster_id": 10379926,
          "cite": [
            "2025 NY Slip Op 25090"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shannon",
          "cluster_id": 10373759,
          "cite": [
            "2025 Ohio 1224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington, V. Tommy Darren Tyson",
          "cluster_id": 10339068,
          "cite": [
            "564 P.3d 248"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. S. CHRISTOPHER M. BOYER / COMMONWEALTH v. S. ROMUALD BERNAUD",
          "cluster_id": 10642653,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antwone Miguel Sanders",
          "cluster_id": 9986839,
          "cite": [
            "106 F.4th 455"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Todd Michael Glover v. the State of Texas",
          "cluster_id": 9509712,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Todd Michael Glover v. the State of Texas",
          "cluster_id": 9509711,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Willie Locust",
          "cluster_id": 9455816,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 9452598,
          "cite": [
            "2023 Ohio 4565"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 9448572,
          "cite": [
            "2023 Ohio 4344"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Roosevelt Randolph",
          "cluster_id": 10612306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grace",
          "cluster_id": 9433421,
          "cite": [
            "2023 Ohio 3781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Leonidas Lewis",
          "cluster_id": 9424185,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Joyette",
          "cluster_id": 9419192,
          "cite": [
            "219 A.D.3d 628",
            "194 N.Y.S.3d 287",
            "2023 NY Slip Op 04216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Tito Rene Scott",
          "cluster_id": 9403530,
          "cite": [
            "530 P.3d 1178",
            "97 Arizona Cases Digest 31"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Donald Ehrhardt III v. State of Mississippi",
          "cluster_id": 10628852,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Michael Figueroa",
          "cluster_id": 10642568,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guardado",
          "cluster_id": 9391153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Collins",
          "cluster_id": 9381212,
          "cite": [
            "2023 Ohio 646"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Schubert",
          "cluster_id": 9354069,
          "cite": [
            "219 N.E.3d 916",
            "171 Ohio St. 3d 617",
            "2022 Ohio 4604"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 9353082,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 8509871,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 8436709,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. PIERRE A. SERTYL.",
          "cluster_id": 10271855,
          "cite": [
            "101 Mass. App. Ct. 836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morton",
          "cluster_id": 7859188,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. BRITTANY WESTGATE.",
          "cluster_id": 10271879,
          "cite": [
            "101 Mass. App. Ct. 548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Baldwin, John Wesley",
          "cluster_id": 6468832,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. CRISTOBAL RODRIGUEZ.",
          "cluster_id": 10271920,
          "cite": [
            "101 Mass. App. Ct. 54"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 6465711,
          "cite": [
            "167 N.Y.S.3d 542",
            "205 A.D.3d 737",
            "2022 NY Slip Op 03010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Bracy",
          "cluster_id": 6452507,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jumaev",
          "cluster_id": 5305647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jumaev",
          "cluster_id": 5304277,
          "cite": [
            "20 F.4th 518"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siegel",
          "cluster_id": 5302012,
          "cite": [
            "180 N.E.3d 574",
            "2021 Ohio 4208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mortel",
          "cluster_id": 4901591,
          "cite": [
            "152 N.Y.S.3d 68",
            "197 A.D.3d 196",
            "2021 NY Slip Op 04498"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maximo Gondres-Medrano",
          "cluster_id": 4898417,
          "cite": [
            "3 F.4th 708"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siler",
          "cluster_id": 4879520,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siler",
          "cluster_id": 4877161,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 6248596,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 4876573,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Salvas",
          "cluster_id": 4869523,
          "cite": [
            "149 Haw. 152",
            "483 P.3d 312"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mayhew",
          "cluster_id": 4867625,
          "cite": [
            "145 N.Y.S.3d 202",
            "192 A.D.3d 1391",
            "2021 NY Slip Op 01807"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richard Dale Griffin v. State",
          "cluster_id": 4843483,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samer Abdalla",
          "cluster_id": 4780505,
          "cite": [
            "972 F.3d 838"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Nettles",
          "cluster_id": 4778561,
          "cite": [
            "186 A.D.3d 861",
            "128 N.Y.S.3d 610",
            "2020 NY Slip Op 04776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Burn v. United States",
          "cluster_id": 4776810,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Gary Campbell",
          "cluster_id": 4771571,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ward, III",
          "cluster_id": 4771237,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ward, III",
          "cluster_id": 4770977,
          "cite": [
            "967 F.3d 550"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Wesley Ryder",
          "cluster_id": 4764454,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacIas",
          "cluster_id": 4763635,
          "cite": [
            "249 Ariz. 335",
            "469 P.3d 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stubbs",
          "cluster_id": 4763578,
          "cite": [
            "2020 Ohio 3464"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Oki",
          "cluster_id": 4759146,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Costa",
          "cluster_id": 4744366,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Marmon",
          "cluster_id": 10133414,
          "cite": [
            "303 Or. App. 469",
            "463 P.3d 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thompson v. State",
          "cluster_id": 10021199,
          "cite": [
            "226 A.3d 871",
            "245 Md. App. 450"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Gilbert",
          "cluster_id": 4734622,
          "cite": [
            "952 F.3d 759"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dibble (Slip Opinion)",
          "cluster_id": 4728568,
          "cite": [
            "150 N.E.3d 912",
            "159 Ohio St. 3d 322",
            "2020 Ohio 546"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4690114,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dunbar",
          "cluster_id": 4688211,
          "cite": [
            "2019 NY Slip Op 9018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Charles Edward Johnson v. State",
          "cluster_id": 4666476,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Manzo",
          "cluster_id": 4658488,
          "cite": [
            "2018 IL 122761"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Robert Jason Allison",
          "cluster_id": 4657477,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrews v. District of Columbia",
          "cluster_id": 4648603,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4625269,
          "cite": [
            "925 F.3d 305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Henderson",
          "cluster_id": 4622068,
          "cite": [
            "2019 Ohio 1974"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 4617416,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 4612731,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Valentine v. State",
          "cluster_id": 4601787,
          "cite": [
            "207 A.3d 566"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ferreira",
          "cluster_id": 4601010,
          "cite": [
            "119 N.E.3d 278",
            "481 Mass. 641"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kent Taderro Bailey, Jr. v. State of Indiana (mem. dec.)",
          "cluster_id": 4580461,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cintron",
          "cluster_id": 7178110,
          "cite": [
            "119 N.E.3d 357",
            "94 Mass. App. Ct. 1115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4548401,
          "cite": [
            "113 N.E.3d 429"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silva",
          "cluster_id": 7177073,
          "cite": [
            "113 N.E.3d 400"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Manuel, C.",
          "cluster_id": 4529555,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Manuel",
          "cluster_id": 4529554,
          "cite": [
            "194 A.3d 1076"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Monteiro",
          "cluster_id": 4512544,
          "cite": [
            "103 N.E.3d 1230",
            "93 Mass. App. Ct. 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4511817,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4511298,
          "cite": [
            "893 F.3d 846"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Richard Lebron Madden, Sr.",
          "cluster_id": 4504038,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon McGrath v. State of Indiana",
          "cluster_id": 4494172,
          "cite": [
            "95 N.E.3d 522"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Decarvalho",
          "cluster_id": 7174850,
          "cite": [
            "103 N.E.3d 771",
            "93 Mass. App. Ct. 1106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4476634,
          "cite": [
            "96 N.E.3d 719",
            "93 Mass. App. Ct. 6"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Manha",
          "cluster_id": 4473484,
          "cite": [
            "91 N.E.3d 669",
            "479 Mass. 44"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sanchez",
          "cluster_id": 4455867,
          "cite": [
            "2017 NY Slip Op 8899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sanchez",
          "cluster_id": 4453920,
          "cite": [
            "2017 NY Slip Op 8899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luna",
          "cluster_id": 4449164,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Rodney Paul Starnes, II",
          "cluster_id": 4447496,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. (And",
          "cluster_id": 7171453,
          "cite": [
            "94 N.E.3d 435",
            "92 Mass. App. Ct. 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ezra Griffith",
          "cluster_id": 4419946,
          "cite": [
            "867 F.3d 1265",
            "2017 WL 3568288",
            "2017 U.S. App. LEXIS 15636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 4406528,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Anthony Youngs",
          "cluster_id": 4405941,
          "cite": [
            "199 Wash. App. 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Dominique Greer",
          "cluster_id": 4392274,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lucy Caitlin Alford and Jeremie Alford",
          "cluster_id": 4392026,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Darius Lamarr Franklin",
          "cluster_id": 4391006,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Braden",
          "cluster_id": 4387920,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joppy v. State",
          "cluster_id": 4386883,
          "cite": [
            "158 A.3d 1112",
            "232 Md. App. 510",
            "2017 WL 1508235",
            "2017 Md. App. LEXIS 420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan P. Jackson v. United States",
          "cluster_id": 4382813,
          "cite": [
            "157 A.3d 1259",
            "2017 WL 1373326",
            "2017 D.C. App. LEXIS 81"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jerry Lewis Tuttle",
          "cluster_id": 4380976,
          "cite": [
            "515 S.W.3d 282",
            "2017 WL 1246855",
            "2017 Tenn. LEXIS 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Douglas Smith",
          "cluster_id": 4375166,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camel",
          "cluster_id": 4369470,
          "cite": [
            "8 Cal. App. 5th 989",
            "214 Cal. Rptr. 3d 531",
            "2017 Cal. App. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kono",
          "cluster_id": 4333305,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kono",
          "cluster_id": 4333306,
          "cite": [
            "152 A.3d 1",
            "324 Conn. 80",
            "2016 Conn. LEXIS 396"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perez",
          "cluster_id": 4314370,
          "cite": [
            "90 Mass. App. Ct. 548"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Laurie Lynn Welch and Roland John Welch",
          "cluster_id": 4312164,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delgado v. City of New York",
          "cluster_id": 4260335,
          "cite": [
            "144 A.D.3d 46",
            "38 N.Y.S.3d 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keenan",
          "cluster_id": 4249780,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keenan",
          "cluster_id": 4249294,
          "cite": [
            "304 Kan. 986",
            "377 P.3d 439",
            "2016 Kan. LEXIS 440"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rauf v. State",
          "cluster_id": 4243712,
          "cite": [
            "145 A.3d 430",
            "2016 Del. LEXIS 419",
            "2016 WL 4224252"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Braden",
          "cluster_id": 4242137,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moore v. State",
          "cluster_id": 3207660,
          "cite": [
            "372 P.3d 922",
            "2016 Alas. App. LEXIS 101",
            "2016 WL 3033860"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. William Gary Mosley",
          "cluster_id": 3172337,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Valadez, Alvin Jr.",
          "cluster_id": 4295917,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Donna Marie Chartrand",
          "cluster_id": 3008533,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Vernon Elliott Lockhart",
          "cluster_id": 2898080,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ramos",
          "cluster_id": 2827409,
          "cite": [
            "88 Mass. App. Ct. 68"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Darryl L. Bryant",
          "cluster_id": 2818139,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Z. U. E.",
          "cluster_id": 2817762,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Veloz",
          "cluster_id": 7313876,
          "cite": [
            "109 F. Supp. 3d 305",
            "2015 WL 3540808"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Freeman",
          "cluster_id": 2805220,
          "cite": [
            "87 Mass. App. Ct. 448"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perez",
          "cluster_id": 2793890,
          "cite": [
            "87 Mass. App. Ct. 278"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robinson, Timothy Lee",
          "cluster_id": 4265214,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gonzales, Rodolfo v. State",
          "cluster_id": 4264446,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Gregory Robinson, Sr.",
          "cluster_id": 2779601,
          "cite": [
            "454 S.W.3d 428",
            "2015 Mo. App. LEXIS 154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Long",
          "cluster_id": 2763468,
          "cite": [
            "774 F.3d 653",
            "2014 U.S. App. LEXIS 24169",
            "2014 WL 7240718"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman (Slip Opinion)",
          "cluster_id": 2747812,
          "cite": [
            "2014 Ohio 4795",
            "141 Ohio St. 3d 428",
            "25 N.E.3d 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 2741338,
          "cite": [
            "230 Cal. App. 4th 490",
            "178 Cal. Rptr. 3d 649",
            "2014 Cal. App. LEXIS 903"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Andrew Davis Saggers",
          "cluster_id": 2717177,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cuong Phu Le",
          "cluster_id": 2984353,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Michael A. Talley",
          "cluster_id": 2651055,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Z.E.",
          "cluster_id": 2648374,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ollivier",
          "cluster_id": 2620563,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ollivier",
          "cluster_id": 2620490,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. William Lance Walker",
          "cluster_id": 1044056,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jeffrey Kristopher King and Kasey Lynn King",
          "cluster_id": 1044089,
          "cite": [
            "437 S.W.3d 856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Tawana Lea Davis",
          "cluster_id": 1039839,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Betts",
          "cluster_id": 1043601,
          "cite": [
            "194 Vt. 212",
            "2013 VT 53",
            "75 A.3d 629",
            "2013 WL 3957591",
            "2013 Vt. LEXIS 56"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Stephen Baker",
          "cluster_id": 1044492,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Michael T. Shelby",
          "cluster_id": 1044601,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Kenneth Hubanks",
          "cluster_id": 1044648,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arturo Castellanos",
          "cluster_id": 873156,
          "cite": [
            "716 F.3d 828",
            "2013 WL 2321976",
            "2013 U.S. App. LEXIS 10797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Clagon",
          "cluster_id": 6580704,
          "cite": [
            "465 Mass. 1004",
            "987 N.E.2d 554",
            "2013 WL 1878923",
            "2013 Mass. LEXIS 325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Cayetano Ramirez",
          "cluster_id": 1044752,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948506,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948505,
          "cite": [
            "403 S.W.3d 867",
            "2013 Tex. Crim. App. LEXIS 531",
            "2013 WL 1136522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Montoya",
          "cluster_id": 6580607,
          "cite": [
            "464 Mass. 566",
            "984 N.E.2d 793",
            "2013 WL 951128",
            "2013 Mass. LEXIS 45"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "David Evans v. Patrick Baker",
          "cluster_id": 813710,
          "cite": [
            "703 F.3d 636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tapia",
          "cluster_id": 6580545,
          "cite": [
            "463 Mass. 721",
            "978 N.E.2d 534",
            "2012 Mass. LEXIS 1060"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Travis Kinte Echols",
          "cluster_id": 1043929,
          "cite": [
            "382 S.W.3d 266",
            "2012 Tenn. LEXIS 738"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Madrid",
          "cluster_id": 8721843,
          "cite": [
            "916 F. Supp. 2d 730",
            "2012 WL 6771011",
            "2012 U.S. Dist. LEXIS 183606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Duarte, Gilbert",
          "cluster_id": 2946139,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Duarte, Gilbert",
          "cluster_id": 2946138,
          "cite": [
            "389 S.W.3d 349",
            "2012 WL 3965824",
            "2012 Tex. Crim. App. LEXIS 1180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mendes",
          "cluster_id": 6580522,
          "cite": [
            "463 Mass. 353",
            "974 N.E.2d 606",
            "2012 WL 3797614",
            "2012 Mass. LEXIS 829"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Patrick Stout v. State of Tennessee",
          "cluster_id": 1046186,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Haidle",
          "cluster_id": 891753,
          "cite": [
            "2012 NMSC 33",
            "2 N.M. 491",
            "2012 NMSC 033"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eldridge",
          "cluster_id": 2697621,
          "cite": [
            "2012 Ohio 3747"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barbosa",
          "cluster_id": 6580509,
          "cite": [
            "463 Mass. 116",
            "972 N.E.2d 987",
            "2012 WL 3139732",
            "2012 Mass. LEXIS 689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armijo v. Perales",
          "cluster_id": 805666,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jerome Sidney Barrett",
          "cluster_id": 1046423,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Voustianiouk",
          "cluster_id": 804162,
          "cite": [
            "685 F.3d 206",
            "2012 WL 2849655",
            "2012 U.S. App. LEXIS 14317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Freeman v. Kadien",
          "cluster_id": 803571,
          "cite": [
            "684 F.3d 30",
            "2012 U.S. App. LEXIS 13674",
            "2012 WL 2551092"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Guy Alvin Williamson",
          "cluster_id": 1043952,
          "cite": [
            "368 S.W.3d 468",
            "2012 WL 1950275",
            "2012 Tenn. LEXIS 380"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santiago",
          "cluster_id": 8358036,
          "cite": [
            "30 Mass. L. Rptr. 81"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Blane v. Commonwealth",
          "cluster_id": 2547964,
          "cite": [
            "364 S.W.3d 140",
            "2012 Ky. LEXIS 54",
            "2012 WL 1450212"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lyons",
          "cluster_id": 2500041,
          "cite": [
            "275 P.3d 314",
            "174 Wash. 2d 354"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 2504396,
          "cite": [
            "727 S.E.2d 322",
            "220 N.C. App. 1",
            "2012 WL 1293800",
            "2012 N.C. App. LEXIS 510"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Branzburg v. Hayes",
          "cluster_id": 108611,
          "cite": [
            "33 L. Ed. 2d 626",
            "92 S. Ct. 2646",
            "408 U.S. 665",
            "1972 U.S. LEXIS 132",
            "24 Rad. Reg. 2d (P & F) 2125",
            "1 Media L. Rep. (BNA) 2617"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiteley v. Warden, Wyoming State Penitentiary",
          "cluster_id": 108297,
          "cite": [
            "28 L. Ed. 2d 306",
            "91 S. Ct. 1031",
            "401 U.S. 560",
            "1971 U.S. LEXIS 65",
            "58 Ohio Op. 2d 434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 108379,
          "cite": [
            "29 L. Ed. 2d 723",
            "91 S. Ct. 2075",
            "403 U.S. 573",
            "1971 U.S. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzM0NjIwODAwMDAwJnM9MjUwNDM5NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 180
      },
      "lane2_top_cited": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NDgmcz0xMDY5NjQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
        "reviewed": 36,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 36,
        "triage_read": 0,
        "triage_snippet_classified": 36
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
    "indexed_citing_opinions": 5035,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106865,
        "count": 4539,
        "count_source": "search"
      },
      {
        "opinion_id": 9422845,
        "count": 629,
        "count_source": "search"
      },
      {
        "opinion_id": 9422846,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422847,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7290,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/aguilar-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjgzNTUmcz05OTg2ODM5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106865,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 100996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 241734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 251313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 255849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 259614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 260180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 1183044,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 2417960,
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
    "date_created": "2026-07-04T16:18:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: abrogated -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Aguilar v. Texas

```
<div>
<center><b><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U.S. 108</a></span> (1964)</b></center>
<center><h1>AGUILAR<br>
v.<br>
TEXAS.</h1></center>
<center>No. 548.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 25-26, 1964.</center>
<center>Decided June 15, 1964.</center>
CERTIORARI TO THE COURT OF CRIMINAL APPEALS OF TEXAS.
<p><i>Clyde W. Woody</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Carl E. F. Dally</i> argued the cause for respondent. With him on the brief were <i>Waggoner Carr,</i> Attorney General of Texas, and <i>Gilbert J. Pena,</i> Assistant Attorney General.</p>
<p><span class="star-pagination">*109</span> MR. JUSTICE GOLDBERG delivered the opinion of the Court.</p>
<p>This case presents questions concerning the constitutional requirements for obtaining a state search warrant.</p>
<p>Two Houston police officers applied to a local Justice of the Peace for a warrant to search for narcotics in petitioner's home. In support of their application, the officers submitted an affidavit which, in relevant part, recited that:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin, marijuana, barbiturates and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law."<sup>[1]</sup></blockquote>
<p>The search warrant was issued.</p>
<p>In executing the warrant, the local police, along with federal officers, announced at petitioner's door that they <span class="star-pagination">*110</span> were police with a warrant. Upon hearing a commotion within the house, the officers forced their way into the house and seized petitioner in the act of attempting to dispose of a packet of narcotics.</p>
<p>At his trial in the state court, petitioner, through his attorney, objected to the introduction of evidence obtained as a result of the execution of the warrant. The objections were overruled and the evidence admitted. Petitioner was convicted of illegal possession of heroin and sentenced to serve 20 years in the state penitentiary.<sup>[2]</sup> On appeal to the Texas Court of Criminal Appeals, the conviction was affirmed, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">172 Tex. Cr. R. 629</a></span>, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">362 S. W. 2d 111</a></span>, affirmance upheld on rehearing, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">172 Tex. Cr. R. 631</a></span>, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">362 S. W. 2d 112</a></span>. We granted a writ of certiorari to consider the important constitutional questions involved. <span class="citation multiple-matches"><a href="/c/U.%20S./375/812/">375 U. S. 812</a></span>.</p>
<p>In <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, we held that the Fourth "Amendment's proscriptions are enforced against the States through the Fourteenth Amendment," and that "the standard of reasonableness is the same under the Fourth and Fourteenth Amendments." <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California"><i>Id.,</i> at 33</a></span>. Although <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> involved a search without a warrant, that case must certainly be read as holding that the standard for obtaining a search warrant is likewise "the same under the Fourth and Fourteenth Amendments."</p>
<p>An evaluation of the constitutionality of a search warrant should begin with the rule that "the informed and deliberate determinations of magistrates empowered to issue warrants . . . are to be preferred over the hurried action <span class="star-pagination">*111</span> of officers . . . who may happen to make arrests." <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>. The reasons for this rule go to the foundations of the Fourth Amendment. A contrary rule "that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. Under such a rule "resort to [warrants] would ultimately be discouraged." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270</a></span>. Thus, when a search is based upon a magistrate's, rather than a police officer's, determination of probable cause, the reviewing courts will accept evidence of a less "judicially competent or persuasive character than would have justified an officer in acting on his own without a warrant," <i>ibid.,</i> and will sustain the judicial determination so long as "there was substantial basis for [the magistrate] to conclude that narcotics were probably present . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 271</a></span>. As so well stated by Mr. Justice Jackson:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States, supra,</i> at 13-14.</blockquote>
<p>Although the reviewing court will pay substantial deference to judicial determinations of probable cause, the court must still insist that the magistrate perform his "neutral and detached" function and not serve merely as a rubber stamp for the police.</p>
<p><span class="star-pagination">*112</span> In <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>, a warrant was issued upon the sworn allegation that the affiant "has cause to suspect and does believe" that certain merchandise was in a specified location. <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#44" aria-description="Citation for case: Nathanson v. United States"><i>Id.,</i> at 44</a></span>. The Court, noting that the affidavit "went upon a mere affirmation of suspicion and belief <i>without any statement of adequate supporting facts,</i>" <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States"><i>id.,</i> at 46</a></span> (emphasis added), announced the following rule:</p>
<blockquote>"Under the Fourth Amendment, an officer may not properly issue a warrant to search a private dwelling unless he can find probable cause therefor from <i>facts or circumstances</i> presented to him under oath or affirmation. Mere affirmance of belief or suspicion is not enough." <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States"><i>Id.,</i> at 47</a></span>. (Emphasis added.)</blockquote>
<p>The Court, in <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>, applied this rule to an affidavit similar to that relied upon here.<sup>[3]</sup> Affiant in that case swore that petitioner "did receive, conceal, etc., narcotic drugs . . . with knowledge of unlawful importation . . . ." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#481" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 481</a></span>. The Court announced the guiding principles to be:</p>
<blockquote>"that the inferences from the facts which lead to the complaint `[must] be drawn by a neutral and detached <span class="star-pagination">*113</span> magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.' <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. The purpose of the complaint, then, is to enable the appropriate magistrate . . . to determine whether the `probable cause' required to support a warrant exists. The Commissioner must judge for himself the persuasiveness of the facts relied on by a complaining officer to show probable cause. He should not accept without question the complainant's mere conclusion . . . ." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 486</a></span>.</blockquote>
<p>The Court, applying these principles to the complaint in that case, stated that:</p>
<blockquote>"it is clear that it does not pass muster because it does not provide any basis for the Commissioner's determination . . . that probable cause existed. The complaint contains no affirmative allegation that the affiant spoke with personal knowledge of the matters contained therein; it does not indicate any sources for the complainant's belief; and it does not set forth any other sufficient basis upon which a finding of probable cause could be made." <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Ibid.</a></span></i>
</blockquote>
<p>The vice in the present affidavit is at least as great as in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>.</i> Here the "mere conclusion" that petitioner possessed narcotics was not even that of the affiant himself; it was that of an unidentified informant. The affidavit here not only "contains no affirmative allegation that the affiant spoke with personal knowledge of the matters contained therein," it does not even contain an "affirmative allegation" that the affiant's unidentified source "spoke with personal knowledge." For all that appears, the source here merely suspected, believed or concluded that there were narcotics in petitioner's <span class="star-pagination">*114</span> possession.<sup>[4]</sup> The magistrate here certainly could not "judge for himself the persuasiveness of the facts relied on . . . to show probable cause." He necessarily accepted "without question" the informant's "suspicion," "belief" or "mere conclusion."</p>
<p>Although an affidavit may be based on hearsay information and need not reflect the direct personal observations of the affiant, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, the magistrate must be informed of some of the underlying circumstances from which the informant concluded that the narcotics were where he claimed they were, and some of the underlying circumstances from which the officer concluded that the informant, whose identity need not be disclosed, see <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span>, was "credible" or his information "reliable."<sup>[5]</sup> Otherwise, <span class="star-pagination">*115</span> "the inferences from the facts which lead to the complaint" will be drawn not "by a neutral and detached magistrate," as the Constitution requires, but instead, by a police officer "engaged in the often competitive enterprise of ferreting out crime," <i>Giordenello</i> v. <i>United States, supra,</i> at 486; <i>Johnson</i> v. <i>United States, supra,</i> at 14, or, as in this case, by an unidentified informant.</p>
<p>We conclude, therefore, that the search warrant should not have been issued because the affidavit did not provide a sufficient basis for a finding of probable cause and that <span class="star-pagination">*116</span> the evidence obtained as a result of the search warrant was inadmissible in petitioner's trial.</p>
<p>The judgment of the Texas Court of Criminal Appeals is reversed and the case remanded for proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>But for <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, I would have voted to affirm the judgment of the Texas court. Given <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> I cannot escape the conclusion that to do so would tend to "relax Fourth Amendment standards . . . in derogation of law enforcement standards in the <i>federal</i> system . . ." (my concurring opinion in <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#45" aria-description="Citation for case: Ker v. California"><i>Ker, supra,</i> at 45-46</a></span>, emphasis added). Contrary to what is suggested in the dissenting opinion of my Brother CLARK in the present case (<i>post,</i> p. 118, note 1), the standards laid down in <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>, did in my view reflect constitutional requirements. Being unwilling to relax those standards for federal prosecutions, I concur in the opinion of the Court.</p>
<p>MR. JUSTICE CLARK, whom MR. JUSTICE BLACK and MR. JUSTICE STEWART join, dissenting.</p>
<p>First, it is well to point out the information upon which the search warrant in question was based: About January 1, 1960, Officers Strickland and Rogers from the narcotics division of the Houston Police Department received reliable information from a credible person that petitioner Aguilar had heroin and other narcotic drugs and narcotic paraphernalia in his possession at his residence, 509 Pinckney Street, Houston, Texas; after receiving this information the officers, the record indicates, kept the premises of petitioner under surveillance for about a week.</p>
<p>On January 8, 1960, the two officers applied for a search warrant and executed an affidavit before a justice <span class="star-pagination">*117</span> of the peace in which they alleged under oath that petitioner's residence at 509 Pinckney Street "is a place where we each have reason to believe and do believe that [Aguilar] . . . has in his possession therein narcotic drugs . . . for the purpose of the unlawful sale thereof, and where such narcotic drugs are unlawfully sold." In addition and in support of their belief, the officers included in the affidavit the further allegation that they "have received reliable information from a credible person and do believe that heroin . . . and other narcotics and narcotic paraphernalia are being kept at . . . [petitioner's] premises for the purpose of sale and use contrary to the provisions of the law."</p>
<p>Upon executing the warrant issued on the strength of this affidavit, the officers knocked on the door of Aguilar's house. Someone inside asked who was there and the officers replied that they were police and that they had a search warrant. At this they heard someone "scuffle and start to run inside of the house." The officers entered and pursued the petitioner, who ran into a back bathroom. Petitioner threw a packet of heroin into the commode, but an officer retrieved the packet before it could be flushed down the drain.</p>
<p></p>
<h2>I.</h2>
<p>At trial petitioner objected to the introduction into evidence of the heroin obtained through execution of the search warrant on the ground that the affidavit was "nothing more than hearsay." The Court holds the affidavit insufficient and sets aside the conviction on the basis of two cases, neither of which is controlling.</p>
<p>First is <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). In that case the affidavit stated that the affiant had "cause to suspect and [did] believe that certain merchandise" was in the premises described. There was nothing in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>,</i> either in the affidavit or in the other proof introduced at trial, to suggest that any facts <span class="star-pagination">*118</span> had been brought out to support a reasonable belief or even a suspicion. Accordingly, the Court held that "[m]ere affirmance of belief or suspicion is not enough." At 47. But in Fourth Amendment cases findings of reasonableness or of probable cause necessarily rest on the facts and circumstances of each particular case. In <i>Aguilar,</i> the affidavit was based not only on "affirmance of belief" but in addition upon <i>"reliable information from a credible person"</i> plus a week's surveillance by the affiants. (Emphasis supplied.) <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is, therefore, <i>not</i> apposite.</p>
<p>The second case the Court relies on is <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). There the affidavit alleged that "Giordenello did receive, conceal, etc., narcotic drugs, to-wit: heroin hydrochloride with knowledge of unlawful importation . . . ." The opinion of the Court, by MR. JUSTICE HARLAN, after discussing Rules 3 and 4 of the Federal Rules of Criminal Procedure, held that the defect in the complaint was that it "does not provide any basis for the Commissioner's determination under Rule 4 that probable cause existed." At 486. The dissent in the case, in commenting on the Court's holding that the complaint was invalid, said: "The Court does not strike down this complaint directly on the Fourth Amendment, but merely on an extension of Rule 4." At 491. Since <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was a federal case, decided under our supervisory powers (Rules 3 and 4 of the Federal Rules of Criminal Procedure), it does not control here.<sup>[1]</sup> As we said in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963), "the demands of our federal system compel us to distinguish between evidence held inadmissible because of our supervisory powers over federal courts and <span class="star-pagination">*119</span> that held inadmissible because prohibited by the United States Constitution."</p>
<p>Even if <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was rested on the Constitution, it would not be controlling here because of the significant differences in the facts of the two cases. In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> the Court said: "The complaint . . . does not indicate any sources for the complainant's belief; and it does not set forth any <i>other</i> sufficient basis upon which a finding of probable cause could be made." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 486</a></span>. (Emphasis supplied.) Here, in Aguilar's case, the affidavit did allege a source for the complainant's belief. <i>i. e.,</i> "reliable information from a credible person . . . that heroin . . . and other narcotics . . . are being kept" in petitioner's premises "for the purpose of sale and use contrary to the provisions of the law." This takes the affidavit here entirely outside the <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> holding. In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> no source of information was stated, whereas here there was a reliable one. The affidavit thus shows "probable cause" within the meaning of the Fourth Amendment, as that Amendment was interpreted by this Court in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), where it was contended that the information given by an informant to an officer was inadmissible because it was hearsay. The Court in <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> held that petitioner was "entirely in error. <i>Brinegar</i> v. <i>United States</i> . . . has settled the question the other way." At 311. In the following year this was reaffirmed in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960): "We conclude therefore that hearsay may be the basis for a warrant."<sup>[2]</sup><span class="star-pagination">*120</span> Furthermore, in the case of <i>Rugendorf</i> v. <i>United States</i><i>,</i> decided only this Term, we held an affidavit good based on information that an informer had seen certain furs in Rugendorf's basement. <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span>. In the <i>Aguilar</i> affidavit the informer told the officers that narcotics were actually "kept at the above described premises for the purpose of sale . . . ." The Court seems to hold that what the informer says is the test of his reliability. I submit that this has nothing to do with it. The officer's experience with the informer is the test and here the two officers swore that the informer was credible and the information reliable. At the hearing on the motion to supress Officer Strickland testified that he delayed getting the search warrant for a week in order to "set up surveillance on the house." The informant's statement, Officer Strickland said, was "the first information" received and was only "some of" that which supported the application for the warrant. The totality of the circumstances upon which the officer relied is certainly pertinent to the validity of the warrant. See the use of such testimony in <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Giordenello, supra,</i> at 485, 486</a></span>. And, just as in that case, there is nothing in the record here to show what the officers verbally told the magistrate. The surveillance of Aguilar's house, which is confirmed by the State's brief, apparently gave the officers further evidence upon which they based their personal belief. Hence the affidavit here is a far cry from "suspicion" or "affirmance of belief." It was based on reliable information from a credible informant plus personal surveillance by the officers.</p>
<p>Furthermore, the Courts of Appeals have often approved affidavits similar to the one here. See, <i>e. g., </i><i>United States</i> v. <i>Eisner,</i> <span class="citation" data-id="255849"><a href="/opinion/255849/united-states-v-samson-eisner/" aria-description="Citation for case: United States v. Samson Eisner">297 F. 2d 595</a></span> (C. A. 6th Cir.); <i>Evans</i> v. <i>United States,</i> <span class="citation" data-id="241734"><a href="/opinion/241734/add-evans-v-united-states/" aria-description="Citation for case: Add Evans v. United States">242 F. 2d 534</a></span> (C. A. 6th Cir.); <i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="251313"><a href="/opinion/251313/united-states-v-rene-ramirez/#715" aria-description="Citation for case: United States v. Rene Ramirez">279 F. 2d 712, 715</a></span> (C. A. 2d Cir.) (dictum); and <i>United States</i> v. <i>Meeks,</i> 313 F. 2d 464 <span class="star-pagination">*121</span> (C. A. 6th Cir.). We denied certiorari in <i>Eisner,</i> <span class="citation" data-id="8943324"><a href="/opinion/8952478/eisner-v-united-states/" aria-description="Citation for case: Eisner v. United States">369 U. S. 859</a></span>, although the affidavit there stated only that "[i]nformation has been obtained by S. A. Clifford Anderson . . . which he believes to be reliable . . . ," <span class="citation" data-id="255849"><a href="/opinion/255849/united-states-v-samson-eisner/#596" aria-description="Citation for case: United States v. Samson Eisner">297 F. 2d, at 596</a></span>, and in <i>Evans,</i> <span class="citation" data-id="8931711"><a href="/opinion/8941251/evans-v-united-states/" aria-description="Citation for case: Evans v. United States">353 U. S. 976</a></span>, where the affiant was a man who "came to the headquarters of the federal liquor law enforcement officers and stated that he wished to give information . . . ," <span class="citation" data-id="241734"><a href="/opinion/241734/add-evans-v-united-states/#535" aria-description="Citation for case: Add Evans v. United States">242 F. 2d, at 535</a></span>.</p>
<p>In summary, the information must be more than mere wholly unsupported suspicion but less than "would justify condemnation," as Chief Justice Marshall said in <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813). As Chief Justice Taft said in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925): Probable cause exists where "the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] . . . sufficient in themselves to warrant a man of reasonable caution in the belief that" an offense has been or is being committed. And as Mr. Justice Rutledge so well stated in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949):</p>
<blockquote>"These long-prevailing standards seek to safeguard citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime. They also seek to give fair leeway for enforcing the law in the community's protection. Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability. The rule of probable cause is a practical, nontechnical conception affording the best compromise that has been found for accommodating these often opposing interests. <span class="star-pagination">*122</span> Requiring more would unduly hamper law enforcement. To allow less would be to leave law-abiding citizens at the mercy of the officers' whim or caprice."</blockquote>
<p>Believing that the Court has substituted a rigid, academic formula for the unrigid standards of reasonableness and "probable cause" laid down by the Fourth Amendment itselfa substitution of technicality for practicality and believing that the Court's holding will tend to obstruct the administration of criminal justice throughout the country, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  The record does not reveal, nor is it claimed, that any other information was brought to the attention of the Justice of the Peace. It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>; 79 C. J. S. 872 (collecting cases). In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> the Government pointed out that the officer who obtained the warrant "had kept petitioner under surveillance for about one month prior to the arrest." The Court of course ignored this evidence, since it had not been brought to the magistrate's attention. The fact that the police may have kept petitioner's house under surveillance is thus completely irrelevant in this case, for, in applying for the warrant, the police did not mention any surveillance. Moreover, there is no evidence in the record that a surveillance was actually set up on petitioner's house. Officer Strickland merely testified that "we <i>wanted to</i> set up surveillance on the house." If the fact and results of such a surveillance had been appropriately presented to the magistrate, this would, of course, present an entirely different case.</p>
<p>[2]  Petitioner was also indicted on charges of conspiring to violate the federal narcotics laws, Act of February 9, 1909, c. 100, <span class="citation no-link">35 Stat. 614</span>, § 2, as amended, <span class="citation no-link">21 U. S. C. § 174</span>; Internal Revenue Code of 1954, § 7237 (b), as amended, <span class="citation no-link">26 U. S. C. § 7237</span> (b). He was found not guilty by the jury. His codefendants were found guilty and their convictions affirmed on appeal. <i>Garcia</i> v. <i>United States,</i> <span class="citation" data-id="260180"><a href="/opinion/260180/anthony-garcia-v-united-states/" aria-description="Citation for case: Anthony Garcia v. United States">315 F. 2d 679</a></span>.</p>
<p>[3]  In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> although this Court construed the requirement of "probable cause" contained in Rule 4 of the Federal Rules of Criminal Procedure, it did so "in light of the constitutional" requirement of probable cause which that Rule implements. <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 485</a></span>. The case also involved an arrest warrant rather than a search warrant, but the Court said: "The language of the Fourth Amendment, that `. . . no Warrants shall issue, but upon probable cause . . .' of course applies to arrest as well as search warrants." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 485-486</a></span>. See <i>Ex parte Burford,</i> <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span>; <i>McGrain</i> v. <i>Daugherty,</i> <span class="citation" data-id="100996"><a href="/opinion/100996/mcgrain-v-daugherty/#154" aria-description="Citation for case: McGrain v. Daugherty">273 U. S. 135, 154-157</a></span>. The principles announced in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> derived, therefore, fore, from the Fourth Amendment, and not from our supervisory power. Compare <i>Jencks</i> v. <i>United States,</i> <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>. Accordingly, under <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, they may properly guide our determination of "probable cause" under the Fourteenth Amendment.</p>
<p>[4]  To approve this affidavit would open the door to easy circumvention of the rule announced in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>.</i> A police officer who arrived at the "suspicion," "belief" or "mere conclusion" that narcotics were in someone's possession could not obtain a warrant. But he could convey this conclusion to another police officer, who could then secure the warrant by swearing that he had "received reliable information from a credible person" that the narcotics were in someone's possession.</p>
<p>[5]  Such an affidavit was sustained by this Court in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>. The affidavit in that case reads as follows:
</p>
<p>"Affidavit in Support of a U. S. Commissioners Search Warrant for Premises 1436 Meridian Place, N. W., Washington, D. C., apartment 36, including window spaces of said apartment. Occupied by Cecil Jones and Earline Richardson.</p>
<p>"In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [<i>sic</i>] in the above mentioned places. The last time being August 20, 1957.</p>
<p>"Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.</p>
<p>"This same information, regarding the illicit narcotic traffic, conducted by Cecil Jones and Earline Richardson, has been given to the undersigned and to other officers of the narcotic squad by other sources of information.</p>
<p>"Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [<i>sic</i>] in the above apartment by Cecil Jones and Earline Richardson.</p>
<p>"Det. Thomas Didone, Jr., Narcotic Squad, MPDC.</p>
<p>"Subscribed and sworn to before me this 21 day of August, 1957.</p>
<p>"James F. Splain, U. S. Commissioner, D. C." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 267-268, n. 2</a></span>.</p>
<p>Compare, <i>e. g., </i><i>Hernandez</i> v. <i>People,</i> ___ Colo. ___, <span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/" aria-description="Citation for case: Hernandez v. People">385 P. 2d 996</a></span>, where the Supreme Court of Colorado, accepting a confession of error by the State Attorney General, held that a search warrant similar to the one here in issue violated the Fourth Amendment. The court said:</p>
<p>"Before the issuing magistrate can properly perform his official function he must be apprised of the underlying facts and circumstances which show that there is probable cause . . . ." <i><span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/" aria-description="Citation for case: Hernandez v. People">Id.,</a></span></i> at ___, <span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/#999" aria-description="Citation for case: Hernandez v. People">385 P. 2d, at 999</a></span>.</p>
<p>[1]  MR. JUSTICE BLACK, who joined the Court's opinion in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> joins this dissent on the basis of his belief that <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was based on Rule 4 and not on the less exacting requirements of the Fourth Amendment.</p>
<p>[2]  The affidavit in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> was more detailed, including a statement of where the heroin might be found, <i>viz.,</i> "on their person, under a pillow, on a dresser or on a window ledge in said apartment." But this detail adds nothing to the reliability of the information furnished. Likewise, the allegation in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that the informer had "on previous occasion" given information "which was correct" was contained in substance in the <i>Aguilar</i> affidavit.</p>

</div>
```

---
