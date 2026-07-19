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

## GROUP: content/cases/United States v. Lee.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Lee
type: case
citation: "274 U.S. 559 (1927)"
parallel_cite: "47 S. Ct. 746; 71 L. Ed. 1202"
neutral_cite: 1927 U.S. LEXIS 52
court: U.S.
court_level: scotus
circuit: ca6
year: 1927
date_decided: 1927-05-31
docket: 540
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
  opinion_url: "https://www.courtlistener.com/opinion/101118/united-states-v-lee/"
  cluster_id: 101118
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Lee
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Fourth Amendment Recalibration]]"
    role: Key
related:
  - "[[Fourth Amendment Recalibration]]"
  - "[[Kyllo v. United States]]"
  - "[[Hester v. United States]]"
  - "[[Carroll v. United States]]"
tags:
  - case
  - fourth-amendment
  - search
  - sense-enhancement
  - open-view
  - prohibition
  - coast-guard
  - scotus
holding: "The Supreme Court held that a Coast Guard officer's use of a searchlight to illuminate the deck of a suspected rum-runner on the high seas was not a Fourth Amendment search — it merely revealed what was already in open view, comparable to using a marine glass or field glass — and, more broadly, that the Coast Guard could board, search, and seize an American vessel and arrest those aboard on the high seas beyond the twelve-mile limit on probable cause of a revenue-law violation; the Court of Appeals' contrary judgment was reversed."
---

# United States v. Lee

*274 U.S. 559 (1927)* (No. 540) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 101118 → opinion 101118 (274 U.S. 559, decided 1927-05-31); Rule quote star-matched to the U.S. Reports pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In February 1925, during Prohibition, the boatswain of a Coast Guard patrol boat followed a motor boat registered to Lee out of Gloucester harbor and, after losing her in a fog, found her about twenty-four miles from land in a region commonly spoken of as Rum Row, lying alongside the schooner *L'Homme* with seventy-one cases of grain alcohol aboard. The boatswain "put a searchlight on her," ordered the three men to raise their hands, boarded, found the alcohol, arrested Lee and his associates, and took the boat and liquor to Boston. Lee was convicted of conspiring to violate the Tariff Act of 1922 and the National Prohibition Act. The Court of Appeals [[Reading and Citing Cases#vacated|vacated]] the conviction, holding that the Coast Guard could not search American vessels on the high seas more than twelve miles out and that the evidence was the fruit of an illegal search under *[[Weeks v. United States|Weeks]]*.

## Issue
Whether the Coast Guard's boarding, search, and seizure of an American vessel on the high seas beyond the twelve-mile limit — and in particular the boatswain's use of a searchlight to observe the vessel's deck — violated the Fourth Amendment, so that the resulting evidence had to be excluded.

## Rule
The Coast Guard may seize an American vessel on the high seas beyond the twelve-mile limit, and board and search it and arrest those aboard, when there is probable cause to believe the revenue laws are being violated — authority the Court analogized to the warrantless automobile search upheld in *[[Carroll v. United States|Carroll]]*. And illuminating what is already exposed to view is not a search: because no exploration below decks or under hatches was shown and the liquor was on deck, discovered before boarding, the boatswain's use of a searchlight worked no Fourth Amendment intrusion — "Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution." — 274 U.S. at 563. ^pin-563

## Application
There was probable cause to believe Lee's vessel was violating the revenue laws — a registered motor boat meeting a schooner on Rum Row with seventy-one cases of alcohol aboard — so the search and seizure of the vessel and the arrest of those aboard were lawful, and the deputy surveyor's later examination of the cases in Boston was independently authorized. As to the searchlight, the Court treated it as mere observation of what was in open view: it revealed only the deck and what lay upon it, no different in kind from using a field glass, and so fell outside the Fourth Amendment. A later trespass, if any, did not render inadmissible knowledge already lawfully obtained.

## Conclusion
**Reversed** — the Court of Appeals' judgment vacating the conviction was set aside, the evidence having been lawfully obtained. Justice Brandeis delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Lee*'s enduring contribution to the Fourth Amendment's recalibration arc is the **sense-enhancement seed**: illuminating what is already exposed with a searchlight — like a field or marine glass — is not a search. That open-view/enhanced-observation line runs forward to *[[Kyllo v. United States|Kyllo]]*, which draws the boundary at technology "not in general public use" used to reveal the interior of a home. Read *Lee* on the "expands government power" side of the timeline, a Prohibition-era decision fitting the Amendment to new maritime enforcement.

## Appears on
- [[Fourth Amendment Recalibration]] — *Key*

## Sources
- [*United States v. Lee*, 274 U.S. 559 (1927)](https://www.courtlistener.com/opinion/101118/united-states-v-lee/) — pinpoint: 563 (searchlight-is-not-a-search holding; the CL opinion text carries U.S. Reports star pagination, so the pin is reporter-style). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a172b865c0d77f4d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "274 U.S. 559 (1927)", "court": "U.S.", "neutral_cite": "1927 U.S. LEXIS 52", "official_citation_present": true, "parallel_cite": "47 S. Ct. 746; 71 L. Ed. 1202", "title": "United States v. Lee", "year": "1927"}}
{"assertion_id": "008e6c54f1ed0969", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Supreme Court held that a Coast Guard officer's use of a searchlight to illuminate the deck of a suspected rum-runner on the high seas was not a Fourth Amendment search — it merely revealed what was already in open view, comparable to using a marine glass or field glass — and, more broadly, that the Coast Guard could board, search, and seize an American vessel and arrest those aboard on the high seas beyond the twelve-mile limit on probable cause of a revenue-law violation; the Court of Appeals' contrary judgment was reversed.", "title": "United States v. Lee"}}
{"assertion_id": "711e1187f1149a30", "dimension": "support", "kind": "home_role", "locator": {"home": "Fourth Amendment Recalibration"}, "payload": {"home": "Fourth Amendment Recalibration", "role": "Key", "title": "United States v. Lee"}}
{"assertion_id": "c27bb7b63f201586", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Lee", "varies_by_point": "false"}}
{"assertion_id": "c430f404d0b9ede0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Lee"}}
```

### lake record — United States v. Lee

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lee",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Lee",
    "case_name_short": "",
    "case_name_full": "United States v. Lee",
    "input_case_name": "United States v. Lee",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": "ca6",
    "state": null,
    "date_decided": "1927-05-31",
    "year": 1927,
    "docket": "540",
    "cluster_id": 101118,
    "lead_opinion_id": 101118,
    "sibling_ids": [],
    "absolute_url": "/opinion/101118/united-states-v-lee/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "274 U.S. 559",
      "volume": "274",
      "reporter": "U.S.",
      "page": "559",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "47 S. Ct. 746",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 1202",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1927 U.S. LEXIS 52",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "52",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "274 U.S. 559",
        "volume": "274",
        "reporter": "U.S.",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 S. Ct. 746",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 1202",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1927 U.S. LEXIS 52",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "52",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "274 U.S. 559",
    "official_selection": {
      "court_class": "scotus",
      "selected": "274 U.S. 559",
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
    "date_created": "2026-07-07T18:18:50Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-lee--101118",
      "to_record_id": "United States v. Lee",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Lee

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b618-5">
  Mr. Justice Brandéis
 </author>
<p id="A7V">
  delivered the opinion of the Court.
 </p>
<p id="AqW">
  In the federal court for Massachusetts, Lee and two others, all apparently American citizens, were indicted for conspiring within the United States to violate §§ 591 and 593 of the Tariff Act of 1922, c. 356, <span class="citation no-link">42 Stat. 858</span>, 981, 982, and § 3 of the National Prohibition Act, October 28, 1919, c. 85, Title II, <span class="citation no-link">41 Stat. 305</span>, 308. The defendants pleaded not guilty. Lee and one other were convicted. Lee sued out a writ of error. The Court of Appeals (one judge dissenting) vacated the judgment on the ground that evidence had been admitted which was obtained by an illegal search. and seizure. 14 F. (2d) 400. This Court granted a writ of certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./273/686/">273 U. S. 686</a></span>.
 </p>
<p id="b618-7">
  On the afternoon of February 16, 1925, the. boatswain of a Coast Guard patrol boat saw a motor boat of the numbered type proceed in a southeasterly direction from Gloucester harbor. He followed her at a distance of 500 yards, lost sight of her after sundown, apparently in a fog, at a point about 20 miles east of Boston Light, and discovered her later alongside the schooner
  <em>
   L’Homme
  </em>
  in a region commonly spoken of as Rum Row, at a point 24 miles from land. On board the motor boat were Lee, two associates, and 71 cases of grain alcohol. The boatswain arrested thé three men, seized the motor boat, and took her with them and the liquor to Boston. There this indictment was found. It does not appear that the Government instituted proceedihgs to forfeit; either the motor boat or the. liquor. The motor boat, which had a length of about 30 feet-,- was registered in Lee’s name.
 </p>
<p id="b618-8">
  The boatswain testified that when he discovered the motor boat alongside the
  <em>
   L’Homme:
  </em>
</p>
<blockquote id="A7v-">
<span citation-index="1" class="star-pagination" label="561"> 
   *561
   </span>
  “ I put a searchlight on her and told those aboard the motor boat to put. up their hands. In the boat I found the three defendants, McNeil, Yieria, and Lee. I hooked the boat over and found a number of cansí of alcohol on board it. I searched the defendants for weapons and found none. I put two of my men on board the motor boat and took the boat and the defendants to Boston.”
 </blockquote>
<p id="Aei">
  The liquor does not appear to have been put in evidence. The deputy surveyor of the port testified that, upon the motor boat’s arrival in Boston, he examined the cases on board and found that they contained alcohol, 95 degrees proof.; and that Lee, when interrogated, said: “ I ran the engine, and the first thing I knew I was alongside a schooner. I did not see any cases on our boat until captured by the revenue cutter.” The testimony of the deputy surveyor as to what he found on the, motor boat, and that of the boatswain as to what he found upon his examination of the motor boat at the time of his command to those on board to throw up their hands, was admitted over Lee’s objection and subject to exception duly made.
 </p>
<p id="b619-6">
  . The Court of Appeals, expressing disagreement with the conclusion reached in
  <em>
   The Underwriter,
  </em>
  13 F. (2d) 433, held that the Coast Guard is not authorized to visit and search American vessels on the high seas more than twelve miles from the coast; that the seizure there made was without authority; that it was illegal, since it did not appear that the Government had ratified it by the institution of legal proceedings to enforce ^e forfeiture; that the search and seizure having been illegal, knowledge gained as a result of the illegal search could not be put ^ evidence,
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  232 U. S.. 383; and that the testimony of the deputy surveyor and of the boatswain was wrongly admitted.
 </p>
<p id="b620-4">
<span citation-index="1" class="star-pagination" label="562"> 
   *562
   </span>
  The Government contends that the Coast Guard has authority to visit, search and seize an American vessel on the high seas beyond the twelve-mile limit when probable cause exists to believe that our law is being violated; that it has authority also to arrest persons on such vessel who there is reason to believe are engaged in committing a felony; that here probable cause was shown that the crime, a felony, was being committed; that if any search, within the meaning of the Constitution, was made of the motor boat before she reached port, it was valid as an incident of a lawful arrest of persons who the officer had reasonable cause to believe were engaged in committing a felony; that the constitutional prohibition against search and seizure without a warrant is not applicable to this small motor boat which does not appear to have been used as a place of residence; and that it does not appear that any search was, in fact, made before the motor boat was examined in Boston by the deputy surveyor, within the territorial limits of the - United States, where search is clearly valid.
 </p>
<p id="b620-5">
  In the main the contentions of the Government are in our opinion well founded. Officers of the Coast Guard .are authorized, by virtue of Revised Statutes, § 3072, to seize on the high seas beyond the twelve-mile limit an American vessel subject to forfeiture for violation of any law respecting the revenue.
  <em>
   Maul
  </em>
  v.
  <em>
   United States [The
  </em>
  Underwriter],
  <em>
   ante,
  </em>
  p. 501. From that power it is fairly to be inferred that, they are likewise authorized to board and search such vessels when there is probable cause to believe them subject to seizure for violation of revenue laws, and to arrest persons thereon engaged in such violation. Compare
  <em>
   Ford
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101041"><a href="/opinion/101041/ford-v-united-states/#609" aria-description="Citation for case: Ford v. United States">273 U. S. 593, 609-616</a></span>. The authority asserted is not as broad as the belligerent right to visit and search even without probable
  <span citation-index="1" class="star-pagination" label="563"> 
   *563
   </span>
  cause. Compare.
  <em>
   The Marianna Flora,
  </em>
  <span class="citation" data-id="85480"><a href="/opinion/85480/the-marianna-flora/#42" aria-description="Citation for case: The Marianna Flora">11 Wheat. 1, 42</a></span>. In the case at bar, there was probable cause to believe that our revenue laws were being violated by an American vessel and the persons thereon, in such manner as to render the vessel subject to forfeiture. Under such circumstances, search and seizure of the vessel, and arrest of the persons thereon, by the Coast Guard on the high seas is lawful, as like search and seizure, of an automobile, and arrest of the persons therein, by - prohibition officers on land is lawful. Compare
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span>. As the Coast Guard was authorized to seize the motor boat, the search of her by the deputy surveyor within the territory of the United States was, in any event, authorized under § 581 of the Tariff Act of 1922. The failure of the Government to institute thereafter proceedings for forfeiture of the motor boat and the liquor did not, by retroaction, render illegal either the seizure or the search.
 </p>
<p id="b621-6">
  Moreover search, if any, of the motor boat at sea did not violate the Constitution, for it was made by the boatswain as an incident of a lawful arrest.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>. But no search on the high seas is shown. The testimony of the boatswain shows that he used a searchlight. It is not shown that there was any exploration below decks or under hatches. For aught that appears, the cases of liquor were on deck and, like the defendants, were discovered before the motor boat was boarded. Such use of a searchlight is comparable to the use of a marine glass or a field glass. It is not prohibited by the Constitution. Compare
  <em>
   Hester
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>. A later trespass by the officers, if any, did not render inadmissible in evidence knowledge legally, obtained.
  <em>
   McGuire
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/" aria-description="Citation for case: McGuire v. United States">273 U. S. 95</a></span>.
 </p>
<p id="b621-7">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Liddell.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Liddell
type: case
citation: "517 F.3d 1007 (2008)"
parallel_cite: ""
neutral_cite: "2008 U.S. App. LEXIS 4012; 2008 WL 482410"
court: 8th Cir.
court_level: coa
circuit: ca8
year: 2008
date_decided: ""
docket: 07-1337
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/1461978/united-states-v-liddell/"
  cluster_id: 1461978
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Liddell
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: Key
related:
  - "[[Miranda and Custodial Interrogation]]"
  - "[[New York v. Quarles]]"
  - "[[Miranda v. Arizona]]"
tags:
  - case
  - fifth-amendment
  - miranda
  - custodial-interrogation
  - public-safety-exception
  - quarles
  - eighth-circuit
holding: "The Eighth Circuit held that an un-Mirandized, in-custody question to a secured arrestee — 'Is there anything else in there we need to know about?' after officers found a concealed revolver in his car — fell within New York v. Quarles's public-safety exception to Miranda, because the risk that officers might mishandle other unknown weapons while searching a vehicle incident to a late-night arrest is an objectively reasonable public-safety concern; the incriminating statement was admissible and the felon-in-possession conviction affirmed."
---

# United States v. Liddell

*517 F.3d 1007 (8th Cir. 2008)* (No. 07-1337) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 1461978 → majority opinion 1461978 (517 F.3d 1007, decided 2008-02-25, Loken, C.J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
At about 12:45 a.m., Officer Adney stopped Antonio Liddell's car for a loud-music violation and arrested him after learning he was barred from driving in Iowa. A pat-down turned up marijuana, cash, and two cell phones, and Adney handcuffed Liddell in the patrol car. Officer Melvin, searching the car incident to the arrest, found an unloaded .38 revolver under the front seat and asked whether Liddell had been thoroughly searched. Adney then removed Liddell and asked whether there was anything else in the car they needed to know about; Melvin added, "That's gonna hurt us?" Liddell laughed and answered that he knew it was there but it was not his, before saying there were no other weapons. Charged as a felon in possession, Liddell entered a conditional guilty plea after the district court denied suppression of that statement. The government conceded he was in custody and had not received *[[Miranda v. Arizona|Miranda]]* warnings.

## Issue
Whether Liddell's un-Mirandized, in-custody statement was admissible under the public-safety exception to *[[Miranda v. Arizona|Miranda]]* recognized in *[[New York v. Quarles]]* — even though the revolver had already been found and Liddell was handcuffed and under the officers' control when the question was asked.

## Rule
The public-safety exception applies, under an **objective** standard that does not turn on the officers' subjective motivation, when "police officers ask questions reasonably prompted by a concern for the public safety." Applying that standard, the Eighth Circuit held that the danger posed by other, unlocated weapons during a search justifies a limited question to a secured arrestee: "Our prior cases recognized that the risk of police officers being injured by the mishandling of unknown firearms or drug paraphernalia provides a sufficient public safety basis to ask a suspect who has been arrested and secured whether there are weapons or contraband in a car or apartment that the police are about to search." — 517 F.3d at 1009–10. ^pin-1009

## Application
Liddell argued the exception could not apply because the revolver had been found, he was handcuffed and controlled by two officers, and no bystanders could have accessed the car. The court rejected that: discovering one concealed firearm gave the officers an objectively reasonable concern that other, possibly loaded weapons were in the vehicle they were about to search incident to a late-night arrest, which could cause harm to an officer who happened upon them unexpectedly or mishandled them. Because the officers had no way to know the .38 was the only weapon, the question about anything else in the car was reasonably prompted by public-safety concern rather than designed solely to elicit testimony, so Liddell's incriminating answer was admissible despite the absence of *[[Miranda v. Arizona|Miranda]]* warnings.

## Conclusion
**Affirmed.** Chief Judge Loken wrote for the court (Loken, C.J.; Gruender and Benton, JJ.). Judge Gruender concurred separately, questioning whether the circuit's public-safety cases had drifted from *[[New York v. Quarles|Quarles]]*'s tethering of the exception to genuine [[Exigent Circumstances and Hot Pursuit|exigent circumstances]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Liddell* is a workhorse Eighth Circuit application of the *[[New York v. Quarles|Quarles]]* **public-safety exception** to *[[Miranda v. Arizona|Miranda]]*: after finding one weapon, officers may ask a secured suspect about other weapons or contraband in a space they are about to search, because mishandling an unknown firearm is an objectively reasonable safety risk. Note the internal tension flagged by Judge Gruender's [[Common Legal Terms#concurring-opinion|concurrence]] — whether that application still requires the [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] *[[New York v. Quarles|Quarles]]* demanded.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key*

## Sources
- [*United States v. Liddell*, 517 F.3d 1007 (8th Cir. 2008)](https://www.courtlistener.com/opinion/1461978/united-states-v-liddell/) — pinpoint: 1009–10 (public-safety-exception applied holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a69abbee5f81f544", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "517 F.3d 1007 (2008)", "court": "8th Cir.", "neutral_cite": "2008 U.S. App. LEXIS 4012; 2008 WL 482410", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Liddell", "year": "2008"}}
{"assertion_id": "0f2f61cbeb28bb6c", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key", "title": "United States v. Liddell"}}
{"assertion_id": "798abfc15ce8fa97", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Eighth Circuit held that an un-Mirandized, in-custody question to a secured arrestee — 'Is there anything else in there we need to know about?' after officers found a concealed revolver in his car — fell within New York v. Quarles's public-safety exception to Miranda, because the risk that officers might mishandle other unknown weapons while searching a vehicle incident to a late-night arrest is an objectively reasonable public-safety concern; the incriminating statement was admissible and the felon-in-possession conviction affirmed.", "title": "United States v. Liddell"}}
{"assertion_id": "ccc171c3383b7d99", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Liddell", "varies_by_point": "false"}}
{"assertion_id": "ef8e3c1510bf8b98", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Liddell"}}
```

### lake record — United States v. Liddell

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Liddell",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Liddell",
    "case_name_short": "Liddell",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Antonio Ray LIDDELL, Defendant-Appellant",
    "input_case_name": "United States v. Liddell",
    "court": "8th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": null,
    "year": 2008,
    "docket": "07-1337",
    "cluster_id": 1461978,
    "lead_opinion_id": 9634236,
    "sibling_ids": [],
    "absolute_url": "/opinion/1461978/united-states-v-liddell/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 F.3d 1007",
      "volume": "517",
      "reporter": "F.3d",
      "page": "1007",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. App. LEXIS 4012",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "4012",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 482410",
        "volume": "2008",
        "reporter": "WL",
        "page": "482410",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 F.3d 1007",
        "volume": "517",
        "reporter": "F.3d",
        "page": "1007",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. App. LEXIS 4012",
        "volume": "2008",
        "reporter": "U.S. App. LEXIS",
        "page": "4012",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 WL 482410",
        "volume": "2008",
        "reporter": "WL",
        "page": "482410",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 F.3d 1007",
    "official_selection": {
      "court_class": "coa",
      "selected": "517 F.3d 1007",
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
    "date_created": "2026-07-07T01:39:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-liddell--1461978",
      "to_record_id": "United States v. Liddell",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Liddell

```
<opinion type="majority">
<author id="b1026-7">LOKEN, Chief Judge.</author>
<p id="b1026-8">Antonio Ray Liddell pleaded guilty to being a felon in possession of a firearm in violation of <span class="citation no-link">18 U.S.C. §§ 922</span>(g)(1) and 924(a)(2). As permitted by a condition in his plea agreement, Liddell now appeals the denial of his motion to suppress a post-arrest statement made without the warnings required by <em>Miranda v. Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S.Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L.Ed.2d 694</a></span> (1966). We agree with the district court<footnotemark>1</footnotemark> that the arresting officers’ in-custody questioning fell within the public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>established in <em>New York v. Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U.S. 649</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">81 L.Ed.2d 550</a></span> (1984). Accordingly, we affirm.</p>
<p id="b1026-11">The following facts are undisputed. At approximately 12:45 a.m., Police Officer Michael Adney stopped a car driven by Liddell for a loud music violation. Adney arrested Liddell when a check revealed that he was barred from driving in Iowa. After the arrest, a pat-down search uncovered a bag of marijuana, $183 in cash, and two cell phones. Adney handcuffed Lid-dell and placed him in the patrol car. Meanwhile, Police Officer Jon Melvin arrived to assist and began to search Lid-dell’s car incident to the arrest. When Melvin discovered an unloaded .38 caliber revolver under the front seat, he showed the gun to Adney and asked whether Lid-dell’s person had been thoroughly searched after the arrest.</p>
<p id="b1026-12">Adney removed Liddell from the patrol car and asked, referring to Liddell’s ear, “Is there anything else in there we need to know about?” Melvin added, “That’s gonna hurt us?” Adney repeated, “That’s gonna hurt us? Since we found the pistol already.” Liddell laughed and said, “I knew it was there but ... it’s not mine,” before telling the officers there were no other weapons in his car. Melvin completed the search of the car, finding .38 caliber ammunition and rolling papers used to make marijuana cigarettes.</p>
<p id="b1026-13">Charged with unlawful possession of the firearm and with unrelated drug offenses, Liddell entered a conditional plea of guilty to the felon-in-possession charge after the district court denied a motion to suppress his highly incriminating statement that he knew the .38 revolver was under the front seat of his car. In the district court and on appeal, the government conceded that Liddell was in custody and had not been given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings at the time the officers asked the question <page-number citation-index="1" label="1009">*1009</page-number>that elicited this incriminating statement. Thus, the issue is whether the statement is admissible under the public safety exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>as articulated by the Supreme Court in <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span> </em>and applied by this court in <em>United States v. Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d 945</a></span> (8th Cir.1999), and <em>United States v. Luker, </em><span class="citation" data-id="9497692"><a href="/opinion/788993/united-states-v-tony-john-luker/" aria-description="Citation for case: United States v. Tony John Luker">395 F.3d 830</a></span> (8th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./546/831/">546 U.S. 831</a></span>,<span class="citation multiple-matches"><a href="/c/S.Ct./126/52/">126 S.Ct. 52</a></span>,<span class="citation" data-id="9247905"><a href="/opinion/9253089/ramirez-v-dretke/" aria-description="Citation for case: Ramirez v. Dretke">163 L.Ed.2d 82</a></span> (2005). “Whether facts support an exception to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirement is a question of law” that we review <em>de novo. United States v. Lackey, 384 </em>F.3d 1224, 1226 (10th Cir.), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./540/997/">540 U.S. 997</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./124/502/">124 S.Ct. 502</a></span>, <span class="citation no-link">157 L.Ed.2d 399</span> (2003); <em>accord United States v. Talley, </em><span class="citation" data-id="775984"><a href="/opinion/775984/united-states-v-curtis-talley/#561" aria-description="Citation for case: United States v. Curtis Talley">275 F.3d 560, 561</a></span> (6th Cir.2001).</p>
<p id="b1027-11">In <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span>, </em>the Supreme Court held that “there is a ‘public safety’ exception to the requirement that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be given before a suspect’s answers may be admitted into evidence.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#655" aria-description="Citation for case: New York v. Quarles">467 U.S. at 655</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>. In this context, protection of the public safety includes protection of the police officers themselves. <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Id.</a></span> </em>at 658 n. 7, 659, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>. The exception does not depend upon the subjective motivation of the questioning officers. Instead, the Court adopted an objective standard: the exception applies when “police officers ask questions reasonably prompted by a concern for the public safety.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#656" aria-description="Citation for case: New York v. Quarles"><em>Id. </em>at 656</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, quoted in <em>Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/#953" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953</a></span>. It does not apply to “questions designed solely to elicit testimonial evidence from a suspect.” <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#659" aria-description="Citation for case: New York v. Quarles">467 U.S. at 659</a></span>, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>.<footnotemark>2</footnotemark></p>
<p id="b1027-13">Liddell argues that the public safety exception does not apply because, at the time the officers asked the question that prompted his incriminating admission, “there was no longer an objective reasonable need to protect the police or the public from any immediate danger” because the revolver had been found, Liddell was handcuffed and under the control of the two officers, and there were no passengers or nearby members of the public who could have accessed or been harmed by the contents of Liddell’s car. The district court rejected this contention, explaining:</p>
<blockquote id="Aj">The discovery of a firearm hidden in a vehicle would lead an officer to have an objectively reasonable concern that other, possibly loaded, firearms may also be in the vehicle which could cause harm to an officer if they were to happen upon them unexpectedly or mishandle them in some way. The accidental discovery of additional weapons poses a threat to officer safety and at the time the officers conducted their limited questioning of [Liddell], given the information then known to them, it was reasonable for the officers to believe this threat existed. There was no way for Officer Melvin or Officer Adney to know that the firearm found under the driver’s seat was ultimately the only weapon or dangerous device located inside of the vehicle.</blockquote>
<p id="b1027-7">The district court’s analysis is consistent with this court’s controlling precedents. Our prior cases recognized that the risk of police officers being injured by the mishandling of unknown firearms or drug par<page-number citation-index="1" label="1010">*1010</page-number>aphernalia provides a sufficient public safety basis to ask a suspect who has been arrested and secured whether there are weapons or contraband in a car or apartment that the police are about to search. <em>See Luker, </em><span class="citation" data-id="9497692"><a href="/opinion/788993/united-states-v-tony-john-luker/#832" aria-description="Citation for case: United States v. Tony John Luker">395 F.3d at 832</a></span> (public safety exception applied to post-arrest question whether there was anything in intoxicated driver’s car the police should know about); <em>Williams, </em><span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/#953" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953-54</a></span> (public safety exception applied to post-arrest question, “is there anything we need to be aware of’ in the suspect’s apartment, because the police “could not have known whether other hazardous weapons were present ... that could cause them harm if they happened upon them unexpectedly or mishandled them in some way”). Accord <em>Lackey, </em>334 F.3d at 1227-28; <em>contra United States v. Williams, </em><span class="citation" data-id="797465"><a href="/opinion/797465/united-states-v-patrick-williams/#428" aria-description="Citation for case: United States v. Patrick Williams">483 F.3d 425, 428</a></span> (6th Cir.2007). Here, when the officers found Liddell’s concealed .38 caliber revolver, they had good reason to be concerned that additional weapons might pose a threat to their safety when they searched Liddell’s car incident to a late-night arrest.</p>
<p id="b1028-4">The judgment of the district court is affirmed.</p>
<footnote label="1">
<p id="b1026-9">. The HONORABLE JAMES E. GRITZNER, United Slates District Judge for the Southern District of Iowa.</p>
</footnote>
<footnote label="2">
<p id="b1027-2">. Because this is an objective standard, and because police officers must react spontaneously to situations posing a threat to public safety, the public safety exception does not turn on the specific form of questions asked. <em>See </em>Williams, <span class="citation" data-id="764955"><a href="/opinion/764955/united-states-v-tonnie-franklin-williams/" aria-description="Citation for case: United States v. Tonnie Franklin Williams">181 F.3d at 953</a></span> n. 13; <em>United States v. Newton, </em><span class="citation" data-id="786350"><a href="/opinion/786350/united-states-v-sewn-newton/" aria-description="Citation for case: United States v. Sewn Newton">369 F.3d 659</a></span>, 678-79 &amp; n. 8 (2d Cir.2004). There can be no doubt that tVu» nmactinn nncpH hv flip nffirprQ in this rncp was sufficiently focused on public safety to trigger the public safety exception. By contrast, the Court explained in <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U.S. at 659</a></span> n. 8, <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">104 S.Ct. 2626</a></span>, the post-arrest questioning without <em>Miranda </em>warnings in <em>Or-ozco v. Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#325" aria-description="Citation for case: Orozco v. Texas">394 U.S. 324, 325-26</a></span>, <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">89 S.Ct. 1095</a></span>, <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">22 L.Ed.2d 311</a></span> (1969), was "clearly investigatory."</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Loera.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Loera
type: case
citation: "923 F.3d 907 (2019)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2019
date_decided: 2019-05-13
docket: 17-2087
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4619076/united-states-v-loera/"
  cluster_id: 4619076
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Loera
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Plain View Doctrine]]"
    role: Key
related:
  - "[[Plain View Doctrine]]"
  - "[[Horton v. California]]"
  - "[[Riley v. California]]"
  - "[[United States v. Ganias]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - computer-search
  - particularity
  - plain-view
  - scope-of-search
  - tenth-circuit
holding: "The Tenth Circuit held that the Fourth Amendment does not require officers executing an electronic-search warrant to stop when they discover evidence of a different, out-of-scope crime, so long as their search remains directed at uncovering the evidence the warrant specifies; agents who found child pornography while searching Loera's devices for computer-fraud evidence could continue the authorized search, and — having obtained a second, pornography-specific warrant to search for that evidence — the denial of suppression was affirmed."
---

# United States v. Loera

*923 F.3d 907 (10th Cir. 2019)* (No. 17-2087) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4619076 → opinion 4396329 (923 F.3d 907, decided 2019-05-13, Ebel, J.); Rule quote star-matched to the F.3d reporter pagination in the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In 2012 the FBI investigated Jason Loera for illegally intercepting e-mails meant for New Mexico Governor Susana Martinez and her staff — computer fraud under 18 U.S.C. §§ 2511 and 1030. Agents obtained a warrant to search Loera's home for evidence of that offense, including on electronic storage media. Executing it, agents previewing his CDs discovered child pornography on four discs; they continued their authorized search for computer-fraud evidence (Search 1), then seized a number of devices along with the four CDs. A week later, one agent reopened the CDs he knew contained pornography to describe several images in an affidavit for a **second** warrant to search all the seized devices for child pornography (Search 2); a magistrate issued it and the agents found more. Charged with receipt of child pornography, Loera moved to suppress the evidence from each search; the district court denied the motion, and he entered a conditional guilty plea preserving the appeal.

## Issue
Whether the Fourth Amendment required the agents to stop their authorized computer-fraud search of Loera's electronic devices once they discovered child pornography that lay outside the first warrant's scope — and whether the evidence had to be suppressed.

## Rule
When officers execute a particular warrant to search an electronic device for evidence of one crime and come across evidence of a different, ongoing crime, they need not abandon the authorized search, provided it stays trained on the warrant's specified evidence: "We hold, among other things, that the Fourth Amendment does not require police officers to stop executing an electronic search warrant when they discover evidence of an ongoing crime outside the scope of the warrant, so long as their search remains directed at uncovering evidence specified in that warrant." — 923 F.3d at 911. ^pin-911

## Application
Because the agents' continued examination of Loera's CDs and devices remained directed at uncovering the computer-fraud evidence the first warrant specified — rather than becoming a roving, exploratory hunt for the pornography they had glimpsed — they were not required to stop when they encountered the out-of-scope child pornography. To actually search the seized devices *for* that pornography, the agents did the constitutionally required thing: they obtained a **second**, pornography-specific warrant before conducting that search. On those facts the court affirmed the denial of Loera's motion to suppress the evidence seized in each search.

## Conclusion
**Affirmed** — the denial of suppression stands. Judge Ebel wrote for the court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Loera* is an important digital-search-scope authority for the **plain-view / anti-exploratory-search** frontier: an officer who lawfully searches a device for one crime's evidence may keep going when other-crime evidence surfaces, so long as the search stays tethered to the warrant's targets — but to search *for* the newly discovered offense, a fresh warrant is required. Pair it with *[[United States v. Ganias|Ganias]]* on digital over-seizure and *[[Coolidge v. New Hampshire|Coolidge]]*'s bar on using plain view to run a general exploratory search from one object to another.

## Appears on
- [[Plain View Doctrine]] — *Key*

## Sources
- [*United States v. Loera*, 923 F.3d 907 (10th Cir. 2019)](https://www.courtlistener.com/opinion/4619076/united-states-v-loera/) — pinpoint: 911 (the electronic-search-need-not-stop holding; the CL opinion text star-paginates the F.3d reporter). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "89238dbe9821380e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "923 F.3d 907 (2019)", "court": "10th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Loera", "year": "2019"}}
{"assertion_id": "3f31117eed8d7503", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key", "title": "United States v. Loera"}}
{"assertion_id": "9dfd75465d0cde8f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Tenth Circuit held that the Fourth Amendment does not require officers executing an electronic-search warrant to stop when they discover evidence of a different, out-of-scope crime, so long as their search remains directed at uncovering the evidence the warrant specifies; agents who found child pornography while searching Loera's devices for computer-fraud evidence could continue the authorized search, and — having obtained a second, pornography-specific warrant to search for that evidence — the denial of suppression was affirmed.", "title": "United States v. Loera"}}
{"assertion_id": "6de48352f6c2ae6a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Loera", "varies_by_point": "false"}}
{"assertion_id": "ace15048b12c840d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Loera"}}
```

### lake record — United States v. Loera

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Loera",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Loera",
    "case_name_short": "Loera",
    "case_name_full": "UNITED STATES of America Plaintiff - Appellee, v. Jason LOERA, Defendant - Appellant.",
    "input_case_name": "United States v. Loera",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2019-05-13",
    "year": 2019,
    "docket": "17-2087",
    "cluster_id": 4619076,
    "lead_opinion_id": 4396329,
    "sibling_ids": [],
    "absolute_url": "/opinion/4619076/united-states-v-loera/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "923 F.3d 907",
      "volume": "923",
      "reporter": "F.3d",
      "page": "907",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "923 F.3d 907",
        "volume": "923",
        "reporter": "F.3d",
        "page": "907",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "923 F.3d 907",
    "official_selection": {
      "court_class": "coa",
      "selected": "923 F.3d 907",
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
    "date_created": "2026-07-07T18:18:30Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-loera--4619076",
      "to_record_id": "United States v. Loera",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Loera

```
                                                                                FILED
                                                                    United States Court of Appeals
                                      PUBLISH                               Tenth Circuit

                       UNITED STATES COURT OF APPEALS                       May 13, 2019

                                                                        Elisabeth A. Shumaker
                            FOR THE TENTH CIRCUIT                           Clerk of Court
                        _________________________________

 UNITED STATES OF AMERICA

       Plaintiff - Appellee,

 v.                                                         No. 17-2180

 JASON LOERA,

       Defendant - Appellant.
                      _________________________________

                     Appeal from the United States District Court
                            for the District of New Mexico
                           (D.C. No. 1:13-CR-01876-JB-1)
                       _________________________________

Jerry A. Walz, Walz and Associates, P.C., Albuquerque, New Mexico for Defendant-
Appellant.

Kristopher N. Houghton, Assistant United States Attorney (John C. Anderson, United
States Attorney, with him on the brief), Albuquerque, New Mexico for Plaintiff-
Appellee.
                        _________________________________

Before LUCERO, EBEL, and PHILLIPS, Circuit Judges.
                  _________________________________

EBEL, Circuit Judge.
                        _________________________________

      This appeal requires us to apply Fourth Amendment principles to a situation

where a police officer executing a warrant to search an electronic storage device for

evidence of one crime discovers evidence of other criminal activity. Here, while
executing a warrant to search Jason Loera’s home for evidence of computer fraud,

FBI agents discovered child pornography on four of Loera’s CDs. Despite

discovering the pornography, the agents continued their search for evidence of

computer fraud—one agent continued to search the CDs that were found to contain

some child pornography and a second agent searched other electronic devices

belonging to Loera, not including those particular CDs (Search 1). After the agents

finished their on-site search, they seized a number of electronic devices that appeared

to contain evidence of computer fraud, plus the four CDs that were found to contain

child pornography, and then brought the seized items back to their office. One week

later, one of the agents reopened the CDs that he knew contained some child

pornography so that he could describe a few pornographic images in an affidavit

requesting a (second) warrant to search all of the seized electronic devices for child

pornography (Search 2). A magistrate judge issued the warrant, and, upon executing

it through two searches, the agents found more child pornography.

      In the subsequent prosecution against him for possessing child pornography,

Loera filed a motion to suppress the evidence seized pursuant to each search, arguing

that the searches violated the Fourth Amendment. On denial of his motion, Loera

pled guilty to receipt of child pornography but preserved his right to appeal that

denial. Exercising jurisdiction under 28 U.S.C. § 1291, we affirm the denial of

Loera’s motion to suppress. We hold, among other things, that the Fourth

Amendment does not require police officers to stop executing an electronic search

warrant when they discover evidence of an ongoing crime outside the scope of the

                                           2
warrant, so long as their search remains directed at uncovering evidence specified in

that warrant.

                                  I.   BACKGROUND

       This case involves several police searches governed by the Fourth

Amendment. The Fourth Amendment protects “the right of the people to be secure in

their persons, houses, papers, and effects, against unreasonable searches and

seizures.” U.S. Const. amend. IV. Generally, for a search to be reasonable, it must

be authorized by a warrant that “particularly” describes “the place to be searched, and

the persons or things to be seized.” U.S. Const. amend. IV. Once officers obtain a

sufficiently particular warrant, they must execute it according to the warrant’s terms.

Horton v. California, 496 U.S. 128, 140 (1990). The following undisputed facts

explain how the warrant-based searches in this case arose.

       In 2012, the FBI began investigating Jason Loera for illegally intercepting e-

mails intended for then-sitting New Mexico Governor Susana Martinez and her staff

in violation of 18 U.S.C. § 2511 (illegal interception) and 18 U.S.C. § 1030

(computer fraud) [collectively, “computer fraud”]. As part of that investigation

(more details of which can be found in the district court’s opinion United States v.

Loera, 59 F. Supp. 3d 1089, 1095–1108 (D.N.M. 2014)), FBI agents applied for and

received a warrant to search Loera’s residence for computer fraud, including any

such evidence residing on electronic devices or storage media (“the first warrant”).

       The first warrant authorized FBI agents to search and seize, in relevant part,

“All records, in any form, relating to violations of [computer fraud], involving Jason

                                             3
Loera.” ROA Vol. I at 37. The warrant defined the terms “records” and “information”

as including: “all of the foregoing items of evidence in whatever forms and by whatever

means they may have been created or stored, including any form of computer or

electronic storage (such as hard disks or other media that can store data).” Id. at 39. In a

separate provision, the warrant sought “Any computers, cell phones, and/or electronic

media that could have been used as a means to commit the offenses described on the

warrant.” Id. at 87. Finally, for any electronic device, whether it was used to commit the

offenses or simply had relevant records stored on it, the warrant permitted the agents to

search and seize evidence of who used, owned, or controlled the device, such as

“configuration files . . . documents, browsing history . . . photographs, and

correspondence . . . .” Id. at 38.

   A. The First Search

       On November 20, 2012, FBI agents including Agent Aaron Cravens and

Special Agent Brian Nishida executed the first search warrant. They discovered a

large volume of electronic media in Loera’s residence, including CDs, DVDs, laptop

computers, external hard drives, a USB flash drive, an iPhone, and an iPad. Cravens

and Nishida were responsible for “previewing” the CDs at Loera’s residence to

ensure that the FBI seized only those CDs that contained information relevant to the

authorized investigation. ROA Vol. II at 53, 58. The two agents split up the CDs

between themselves and searched them separately.

       Cravens tried to view the files of the first CD using a program called FTK

Imager, which would have allowed Cravens to limit his search to a particular type of

                                             4
file, for example, only image, text, or audio files. However, the program did not

work. Consequently, Cravens opened the CD on a computer and used the “thumbnail

view” to preview the files stored on it, meaning, he saw small images of the files, the

file names, and the file types in a vertical list that he had to scroll through to see in

its entirety. Although Cravens believed he had authority under the first warrant to view

the entire contents of the CD, Cravens used the thumbnail-image view to fast-track his

search. He would scroll past irrelevant files but “click[] on anything that didn’t appear

correct, or any documents” to open them. Id. at 92. While Cravens was “scrolling

down through the images or files . . . on the CDs, [he] found what looked like a nude

child.” Id. at 60. He opened the file to confirm that it was an image of child

pornography. After determining that it was, Cravens ejected the CD from his

computer, set it aside, and alerted Agent Nishida and the FBI agent in charge of

Loera’s case. Then, Cravens searched the rest of the CDs assigned to him for

evidence of computer fraud. Cravens later found a child pornography image on a

second CD. Just as he did with the first, Cravens set the CD aside after discovering the

illegal images and did not open any other files on that CD.

       Agent Nishida took a different approach to his search. He previewed the files

on his assigned CDs using the “details view” of Windows Explorer, meaning that he

saw a list of files, file names, and last-modified dates of those files, but not pictures

associated with the files. Id. at 157. For his search of the CDs, or “triage,” as he called

it, Nishida would open two or three files on each CD and then determine from that

sample whether the CD should be seized pursuant to the warrant. Id. at 160. If Nishida

                                             5
found something he believed might be responsive to the warrant in the files that he

sampled, he would set the CD aside to be reviewed off-site. As he was sampling files,

Nishida found child pornography on two CDs. Unlike Cravens, Nishida did not cease his

search of those CDs after discovering child pornography; he continued sampling files on

the CDs to determine if they contained information that was responsive to the warrant.

       The FBI seized thirteen CDs in total from Loera’s residence: four contained child

pornography images and nine contained evidence of computer fraud.1 In addition to the

thirteen CDs, the FBI seized computers, external hard drives, an iPhone, and an iPad.

    B. The Second Search

       One week later, on November 27, 2012, Cravens decided to apply for a search

warrant to search the items seized from Loera’s residence for child pornography.

Cravens wanted to include in his warrant affidavit a detailed description of one child

pornography image from each of the four CDs on which he and Nishida had found child

pornography during their on-site preview. Consequently, Cravens opened each of the

four CDs, viewing several images on each, to find child pornography images that he

could accurately describe. Viewing the photos and drafting the affidavit took a total of

two-and-a-half hours. However, Cravens testified before the district court that he did not

spend “anywhere near the two-and-a-half hours” actually looking at photos on the CDs.

Id. at 74-75.



1
 There is no indication in the record whether the four CDs that contained child
pornography also contained evidence responsive to the warrant. However, Loera does
not challenge the FBI’s seizure of those CDs pursuant to the first warrant.
                                             6
       Cravens’ affidavit included two sections. In Section I, Cravens described his

training and experience with computers and child pornography. In Section II, Cravens

explained the details of the FBI’s investigation of Loera that led to the agent’s discovery

of child pornography on the CDs in Loera’s residence. In particular, paragraph 21

described in general terms how Cravens discovered the child pornography:

       21. In the process of executing this warrant, an FBI certified computer
       forensic examiner and a computer analysis response team (CART)
       technician previewed the loose media located during the search (e.g.,
       thumb drives, CD-Rs, DVD-Rs, memory cards, etc.) for evidence
       relevant to the original unrelated investigation. During the preview, the
       examiners identified four writable CDs which appeared to contain
       images of child pornography. The CDs were seized and placed in the
       evidence control room at the local FBI office.

ROA Vol. I at 120. In paragraph 23, Cravens explained that on November 27, 2012,

he “reviewed the four CDs . . . that were believed to contain child pornography,” id.

at 121, and that “[d]uring the review of the CDs, [he] observed multiple pictures of

children many of which are in various states of dress,” id. Then, in paragraphs

24-27, Cravens provided a detailed description of one image from each CD that

depicted a minor engaged in sexually explicit conduct. Cravens’ descriptions

included the apparent age of the minor and the conduct depicted. On November 29,

2012, based on Cravens’ affidavit, a federal magistrate judge approved a warrant to

search the thirteen CDs and six other electronic devices that were seized from Loera’s

residence for child pornography (“the second warrant”).




                                             7
   C. Searches Pursuant to the Second Warrant

      Agent Nishida executed the second warrant on two separate dates. In December

2012, Nishida searched Loera’s laptop pursuant to both the first and second warrants,

looking for evidence of computer fraud and child pornography. He discovered more than

730 child pornography images on Loera’s laptop. In April 2013, Nishida searched the

four CDs seized from Loera’s residence for child pornography pursuant to the second

warrant. He discovered approximately 330 images and two movies of child pornography

on those CDs.

   D. Proceedings Below

      A federal grand jury indicted Loera on several counts of possessing child

pornography that implicated the images found on both his laptop and his CDs. Loera

filed a motion to suppress that child pornography evidence, and the district court

denied the motion. Loera filed a motion for reconsideration, which the district court

also denied. Following that denial, Loera pled guilty to one count of knowingly

receiving child pornography in violation of 18 U.S.C. §§ 2252(a)(2), 2252(b)(1), and

2256, pursuant to a plea agreement, but he reserved the right to appeal the denial of

his motions.

      On appeal, Loera argues that the district court should have suppressed the

child pornography evidence discovered during the first search, the second search, and

the searches conducted pursuant to the second warrant because, according to Loera,

each search was unlawful. Loera argues that the first search exceeded the scope of

the first warrant, the second search exceeded the scope of the first warrant, and the

                                            8
last two searches, while authorized by the second warrant, were unlawful because

that warrant was invalid. Additionally, Loera maintains that none of the exceptions

to the warrant requirement apply to the searches in this case. We conclude that the

first search was lawful, but we agree with Loera that the remaining searches were

unlawful. Nevertheless, we AFFIRM the district court’s denial of Loera’s motion to

suppress and motion to reconsider under the inevitable discovery doctrine.

                                  II.   DISCUSSION

   A. Standard of Review

       “When reviewing the district court’s denial of a motion to suppress, we view

the evidence in the light most favorable to the government and accept the district

court’s factual findings unless they are clearly erroneous,” United States v. Grimmett,

439 F.3d 1263, 1268 (10th Cir. 2006), but “[t]he ultimate question of reasonableness

under the Fourth Amendment is a legal conclusion that we review de novo.” Id.

Accordingly, de novo review applies to the issues we address in this opinion,

including, the scope of a search warrant, United States v. Angelos, 433 F.3d 738, 745

(10th Cir. 2006), the sufficiency of a search warrant, United States v. Danhauer, 229

F.3d 1002, 1005 (10th Cir. 2000), the applicability of the good-faith exception, id.,

and the applicability of the inevitable discovery doctrine, United States v. Christy, 739

F.3d 534, 540 (10th Cir. 2014).

   B. Validity of the Government’s Application for the First Warrant

       First, Loera argues that the FBI agents obtained the initial warrant to search

his residence for evidence of computer fraud as a pretext to search instead for

                                            9
evidence of child pornography. The district court disagreed, finding that the sole

purpose of the first search was to uncover evidence of computer fraud. We affirm

that conclusion.

      Loera’s pretext argument is based on a statement that Agent Nishida made in a

report dated February 28, 2013, three months after the first and second searches were

conducted. In that report, Nishida wrote:

      On November 14, 2012, SA Michael Boady requested that the above
      listed specimen or specimens be examined for evidence of intercepting a
      communication. For example, e-mail messages to or from the domain
      Susanna2010.com. In addition, SA Boady requested that the evidence
      also be examined for evidence of child pornography possession and
      receipt.

ROA Vol. II at 191–92. Loera argues that this report proves that on November 14,

2012, six days before the first search, Agent Nishida received instructions to search

Loera’s home and effects for evidence of child pornography.

      The district court made explicit factual findings to the contrary, which are

supported by the record. First, the district court found that, had the FBI agents had

suspicions that Loera possessed child pornography, agents would have included that

information in their application for the first warrant. Second, Agent Nishida testified

at the suppression hearing that the February 2013 report summarized two separate

instructions from SA Boady: on November 14, 2012, Boady instructed Nishida to

search for evidence of interception, and, later, Boady instructed Nishida to search for

evidence of child pornography. Finally, both Cravens and Nishida testified at the

suppression hearing that the purpose of the November 20 search was only to uncover


                                            10
evidence of computer fraud, and the district court credited that testimony. Each of

these facts supports the district court’s determination that the agents conducted the

first search solely to look for evidence of computer fraud. And we are unpersuaded

by Loera’s only evidence of pretext, the report written three months after the

allegedly pretextual search.2

       Thus, we conclude the FBI agents had no pretextual motivations for obtaining

the first warrant, and we affirm the district on this issue.

    C. Reasonableness of the First and Second Searches

       Next, we determine that the first search of Loera’s residence was reasonable

because it was directed solely at uncovering the items specified in the first warrant

both before and after the officers discovered the child pornography evidence.

However, we conclude that the second search was unreasonable because it was

directed at uncovering evidence of child pornography.

    1. Relevant legal principles

       The Fourth Amendment provides:

       The right of the people to be secure in their persons, houses, papers, and
       effects, against unreasonable searches and seizures, shall not be
       violated, and no Warrants shall issue, but upon probable cause,
       supported by Oath or affirmation, and particularly describing the place
       to be searched, and the persons or things to be seized.




2
 Alternatively, even if the agents had an additional motive for conducting the first
search, that argument would fail as a matter of law under Whren v. United States,
517 U.S. 806, 813 (1996).
                                            11
U.S. Const. amend. IV. It is now well-recognized that “the ultimate touchstone of

the Fourth Amendment is ‘reasonableness.’” Brigham City v. Stuart, 547 U.S. 398,

403 (2006). “[R]easonableness generally requires the obtaining of a judicial

warrant,” Riley v. California, 134 S.Ct. 2473, 2482 (2014), subject to only a few

exceptions. The warrant must “particularly” describe “the place to be searched, and

the persons or things to be seized,” U.S. Const. amend. IV.

      However, obtaining a sufficiently particular warrant is just the first step to

conducting a reasonable search. The officers tasked with executing a sufficiently

particular warrant must conduct their search “strictly within the bounds set by the

warrant.” Bivens v. Six Unknown Named Agents of Fed. Bureau of Narcotics, 403

U.S. 388, 395 n.7 (1971) (quoting Marron, 275 U.S. at 196). The Supreme Court has

held that, “[i]f the scope of [a] search exceeds that permitted by the terms of a validly

issued warrant . . . the subsequent seizure [of evidence] is unconstitutional without

more.” Horton v. California, 496 U.S. 128, 140 (1990).

      Determining whether a search exceeds the scope of its authorizing warrant is,

like most inquiries under the Fourth Amendment, an exercise in reasonableness

assessed on a case-by-case basis. Dalia v. United States, 441 U.S. 238, 258 (1979)

(holding that the manner of a search is subject to “later judicial review as to its

reasonableness”). The general Fourth Amendment rule is that investigators executing

a warrant can look anywhere where evidence described in the warrant might

conceivably be located. United States v. Ross, 456 U.S. 798, 824 (1982). For

example:

                                           12
       Just as probable cause to believe that a stolen lawnmower may be found in
       a garage will not support a warrant to search an upstairs bedroom, probable
       cause to believe that undocumented aliens are being transported in a van
       will not justify a warrantless search of a suitcase. Probable cause to believe
       that a container placed in the trunk of a taxi contains contraband or
       evidence does not justify a search of the entire cab.

Id. This limitation works well in the physical-search context to ensure that searches

pursuant to warrants remain narrowly tailored, but it is less effective in the electronic-

search context where searches confront what one commentator has called the “needle-in-

a-haystack” problem. Orin S. Kerr, Digital Evidence and the New Criminal

Procedure, 105 Colum. L. Rev. 279, 301 (2005). Given the enormous amount of data

that computers can store and the infinite places within a computer that electronic

evidence might conceivably be located, the traditional rule risks allowing unlimited

electronic searches.

       To deal with this problem, rather than focusing our analysis of the

reasonableness of an electronic search on “what” a particular warrant permitted the

government agents to search (i.e., “a computer” or “a hard drive”), we have focused

on “how” the agents carried out the search, that is, the reasonableness of the search

method the government employed. See United States v. Burgess, 576 F.3d 1078

(10th Cir. 2009); United States v. Walser, 275 F.3d 981 (10th Cir. 2001); United

States v. Carey, 172 F.3d 1268 (10th Cir. 1999). Our electronic search precedents

demonstrate a shift away from considering what digital location was searched and

toward considering whether the forensic steps of the search process were reasonably

directed at uncovering the evidence specified in the search warrant. Shifting our


                                             13
focus in this way is necessary in the electronic search context because search

warrants typically contain few—if any—restrictions on where within a computer or

other electronic storage device the government is permitted to search. See United

States v. Christie, 717 F.3d 1156, 1165 (10th Cir. 2013) (holding that, so long as an

electronic search warrant requires the government to “direct all of its search efforts”

toward evidence relating to a specific crime, the warrant is sufficiently particular,

even where it permits the government to search a “computer” for “all records”

relating to the crimes of “murder, neglect, and abuse”). Because it is “unrealistic to

expect a warrant prospectively [to] restrict the scope of a search by directory,

filename or extension or to attempt to structure search methods,” Burgess, 576 F.3d

at 1093 (alteration added), our ex post assessment of the propriety of a government

search is essential to ensuring that the Fourth Amendment’s protections are realized

in this context. Our precedent of Carey, Burgess, and Walser, to which we turn next,

are instructive as to what constitutes a reasonable electronic search pursuant to a

valid warrant.

      Carey is the only case in which we invalidated an electronic search for

exceeding the scope of its authorizing warrant. See 172 F.3d at 1276. There, a

police officer obtained a warrant to search files on the defendant’s computer for

evidence “pertaining to the sale and distribution of controlled substances.” Id. at

1270. Prior to searching the computer, the officer first viewed the computer’s file

directory, which showed numerous “JPG” files with sexually suggestive titles. Id.

During his search, the officer came across a number of files that he did not recognize

                                           14
and that he was unable to view on the computer that he was using. Id. at 1271. To

view the files, the officer downloaded them onto a separate disk, inserted that disk

into another computer, and then was immediately able to view a “JPG file” that

depicted child pornography. Id. Rather than navigating away from the

nonresponsive material, the officer “downloaded approximately two hundred forty-

four” more JPG files and then transferred them to nineteen disks, viewing five to

seven images on each disk to determine that they all contained child pornography.

Id. The whole process took about five hours. Id. at 1273. After he had catalogued

the child pornography images in this manner, he then “returned” to his “original task

of looking for evidence of drug transactions.” Id. at 1271.

      The Carey court held that this was an unlawful, general exploratory search

because, although it was permissible for the officer to open the first JPG file to see if

it was responsive to the warrant, id. at 1273 n.4, his opening of the remaining files

exceeded the bounds of the authorizing warrant, id. at 1276. The Carey court’s

holding turned on four facts: (1) the officer spent five hours, a significant amount of

time, specifically perusing the trove of nonresponsive material, id. at 1273; (2) the

nonresponsive files were characteristically distinct and set apart from the other files

on the computer (such that they could have been avoided) because each file was

labeled “JPG,” many had sexually suggestive titles, and the officer had to download

them to open them, id. at 1274; (3) the officer did not discover the files inadvertently

(at least after his first look), id. at 1273; and (4) a more narrowly tailored search was

possible—the officer could have gone back to searching for drug-related documents

                                           15
much sooner than he did, id. at 1273. Importantly, we did not condemn the officer’s

decision to return to searching for drug-related documents after discovering the child

pornography, but, instead, we condemned his “temporar[y] abandon[ment]” of the

original search to conduct a “five hour search of the child pornography files.” Id. at

1273.

        Next, we turn to Walser and Burgess, both of which upheld electronic searches

in which the investigator discovered incriminating, nonresponsive material while

executing a search warrant but then navigated away from it. In United States v.

Walser, the police obtained a warrant to search the defendant’s hotel room for

electronically stored records of “evidence of the possession of controlled

substances.” 275 F.3d 981, 983–84 (10th Cir. 2001). A police officer searched the

room pursuant to the warrant and found a laptop and a digital camera. Id. at 984.

The agent seized the laptop, removed it from the hotel room, and then conducted a

drug-specific search of the laptop, looking for “ledgers of drug transactions or images

of drug use.” Id. In order to find those things, the agent employed a particularized

search method that “selectively proceeded to the ‘Microsoft Works’ sub-folder on the

premise that[,] because Works is a spreadsheet program, that folder would be most

likely to contain records relating to the business of drug trafficking.” Id. at 986. It

was while searching the contents of the Works folder that the officer came across a

file labeled “bstfit.avi” and opened it. Id. at 984. When he viewed the contents, he

discovered that the file contained child pornography images. Id. at 986–87. He then

immediately ceased his search. Id.

                                           16
       We upheld the officer’s search as reasonable because we determined that, by

using a particularized search method, the officer avoided conducting the kind of

“sweeping, comprehensive search of a computer’s hard drive” that Carey prohibited.

Id. at 986. The defendant in Walser argued that the agent exceeded the scope of the

warrant by opening the “AVI file,” a video file, because “it could not possibly have

contained the type of evidence the [a]gent was authorized to search for, namely,

records of drug transactions or still images of drug use.” Id. at 987. We rejected that

argument by interpreting Carey to excuse an officer’s discovery of child pornography

during a search for “relevant records in places where such records might logically be

found” so long as the officer does not conduct a supervening search specifically

directed at finding pornography evidence. Id. at 986. Applying that rule, we held in

Walser that the officer’s opening the “bstfit.avi” file was permissible because (1) he

was looking in a folder that was “most likely to contain records relating to the

business of drug trafficking” when he opened it, and (2) he did not conduct an

intervening search directly focused on child pornography like the agent in Carey. Id.

Based on those facts, we concluded that the “search was reasonable and within the

parameters of the search warrant” and that the evidence found as a result of it did not

need to be suppressed. Id. at 987.

       Finally, in United States v. Burgess, 576 F.3d 1078 (10th Cir. 2009), we again

upheld an electronic search that uncovered evidence of child pornography as

reasonable and within the scope of its authorizing warrant. There, police obtained a

warrant to search a motorhome for, among other things, “computer records” that

                                            17
would tend to show “conspiracy to sell drugs.” Id. at 1083. The warrant

incorporated the affidavit on which it was based, which stated that the affiant “knows

that persons involved in trafficking or the use of narcotics often keep photographs of

coconspirators or photographs of illegal narcotics in their vehicle.” Id.

      Based on the warrant, officers searched two hard drives and a laptop found in

the motorhome. Id. An agent searched one of the hard drives by using a program

called EnCase, which copies the contents of a hard drive over to a computer to

prevent file corruption. Id. at 1083–84. EnCase allows an investigator to “preview”

reduced-sized photos of each image file as they are being copied. Id. at 1084, 1094.

The agent took advantage of this feature and viewed each image file on the hard drive

as it was being copied. Id. at 1084. After viewing 200-300 digital images, mostly

personal photos, the agent saw an image that looked like child sexual exploitation.

Id. He then closed the preview program and sought a warrant to search all of the

defendant’s electronic storage devices for evidence of child pornography. Id. Upon

conducting that search, the agent found more than one hundred thousand illegal

images. Id.

      The defendant asked the district court to suppress the child pornography

evidence because, he argued, the agent’s use of the “preview” program exceeded the

scope of the warrant because he did not employ a particularized search method like

the agent in Walser but instead looked through each image file contained on the hard

drive. We determined that the agent’s use of the “preview” program was reasonable

and did not exceed the scope of the warrant for two reasons. First, we noted that,

                                          18
because the warrant did not expressly limit the file types that the agent was allowed

to search, for example, by limiting the search to text files (.doc, .wpd, .txt, etc.), the

agent was well within the scope of the warrant when he decided to view all of the

image files on the hard drive using the preview program. Id. at 1092. Second, we

determined that there was no reasonable way for the agent to conduct a more

narrowly tailored search because, when the object of a search is likely to be an image

file, as it was in Burgess, “there may be no practical substitute for actually looking in

many (perhaps all) folders and sometimes at the documents contained within those

folders.” Id. at 1094.

       Reading these cases together, we determine that four features of the

unconstitutional search in Carey demonstrate that it was unreasonably directed at

uncovering evidence of child pornography, rather than directed at the evidence

specified in the warrant, and distinguish it from the reasonable searches in Walser

and Burgess: (1) the length of time the searching officer spent looking at the

incriminating, nonresponsive evidence (five hours in Carey versus less than one

minute in Walser and Burgess); (2) the fact that the nonresponsive files were set apart

from the responsive files saved on the storage device (JPG files downloaded onto

separate disks in Carey versus generic files intermingled all in one place in Burgess);

(3) the manner in which the evidence was discovered (purposefully in Carey versus

inadvertently in Walser and Burgess);3 and (4) the breadth of the search method


3
 We acknowledge that in Horton v. California, 496 U.S. 128, 130 (1990), the
Supreme Court held that, in physical searches, “even though inadvertence is a
                                            19
employed (the wide detour in Carey versus the narrowly tailored search in Walser).

Contrary to Loera’s assertion, these cases do not require that officers stop searching

upon discovering evidence of a crime outside the scope of the warrant. Such a rule

would prohibit what the Fourth Amendment expressly permits—reasonable searches

based upon a warrant supported by probable cause. We have never required that.

      This conclusion brings us in line with every circuit that has confronted this

issue. See United States v. Stabile, 633 F.3d 219, 240 (3d Cir. 2011) (upholding

denial of motion to suppress where officers continued warrant-authorized search of

the defendant’s computer for financial crimes after discovering child pornography);

United States v. Williams, 592 F.3d 511, 521–24 (4th Cir. 2010) (upholding search

where the officer continued his warrant-authorized search of the defendant’s

computer for evidence of “making threats and computer harassment” after

discovering child pornography); United States v. Miranda, 325 F.App’x 858, 859–60

(11th Cir. 2009) (per curiam) (unpublished) (upholding search where officer

continued his warrant-authorized search for evidence of counterfeit software after

discovering child pornography); United States v. Wong, 334 F.3d 831, 834 (9th Cir.


characteristic of most legitimate ‘plain view’ seizures, it is not a necessary
condition.” However, because Carey, Walser, and Burgess, each of which succeeded
Horton in time, considered the subjective intentions of the searching officers where
that information was available, we continue to include inadvertence as a factor to
consider when deciding whether an electronic search fell within the scope of its
authorizing warrant or outside of it. The fundamental differences between electronic
searches and physical searches, including the fact that electronic search warrants are
less likely prospectively to restrict the scope of the search, justify our inclusion of
that factor. See Horton, 496 U.S. at 139 (abandoning inadvertence as a necessary
condition for a legitimate plain view seizure).
                                          20
2003) (upholding denial of motion to suppress where the officer continued his

warrant-authorized search of the defendant’s computer for, among other things,

“[a]ny maps, receipts, or writings, depicting Churchill County Nevada” after

discovering child pornography).

       Although officers do not have to stop executing a search warrant when they

run across evidence outside the warrant’s scope, they must nevertheless reasonably

direct their search toward evidence specified in the warrant. What that looks like

depends on the particular facts of a given case. Narrowly tailored search methods

that begin looking “in the most obvious places and [then] progressively move from the

obvious to the obscure,” Burgess, 576 F.3d at 1094, should be used where possible but

are not necessary in every case. In cases like this one, where the electronic storage

device is not well-organized and the most practical way to search it is through an item-

by-item review, “there may be no practical substitute for actually looking in many

(perhaps all) folders and sometimes at the documents contained within those folders.”

Id. In such a case, however, the searching officer must respond appropriately to what

he or she sees. The reasonableness of a search evolves as the search progresses and

as the searching officer learns more about the files on the device that he or she is

searching.

       An analogy to the physical realm is helpful here. Imagine a warrant authorizes

police officers to search a “residence” for evidence of “firearms and ammunition.”

Under that warrant, it would be reasonable for a police officer to search the medicine

cabinet in the bathroom for a minute or two to see if a small gun or ammunition is

                                            21
hidden there, however, it would be unreasonable for the officer to spend two hours

reading the labels on each bottle of medicine in the cabinet. On the other hand, if the

warrant had authorized the officer to search the residence for evidence of “illegal

drug trafficking and manufacture,” an intensive search of the medicine cabinet would

be reasonable. In both cases, the medicine cabinet is fair game to search, but the

intensity level of the permitted search differs depending on the evidence to be seized.

The same is true for electronic searches. While in some cases many (perhaps all)

electronic areas of a computer will be fair game to search, the level of intensity that

officers are permitted to spend searching those areas will differ depending on

whether the area appears to contain responsive material. This is true even when

officers come across evidence of incriminating, nonresponsive material. In all cases,

the ultimate test is the one mandated by the Fourth Amendment: whether the search

was “reasonable” under the circumstances. In the case of a computer search,

“reasonableness” requires officers to take into account the flexibility of computers

and the multiple configurations to which they may be adapted. As the computer

search continues and as the executing officer obtains more information about how a

suspect used his computer, that too may inform the reasonableness of the continuing

search.

       We now apply these principles to the November 20 and 27 searches conducted

in this case.




                                           22
   2. November 20 search was reasonable

      Loera argues that, although the first warrant permitted the FBI agents to search his

CDs for evidence of computer fraud, the officers’ search exceeded the scope of the first

warrant when they continued searching after discovering evidence of child pornography.

We disagree. The searches that Agent Cravens and Agent Nishida each conducted of

Loera’s CDs on November 20 were reasonable and conducted within the scope of the

first warrant because at all times each was reasonably directed at discovering evidence of

computer fraud. Therefore, the first search did not violate the Fourth Amendment and

thus did not warrant suppression of the evidence discovered during that search.

      The agents’ searches on November 20 resemble the searches in Walser and

Burgess more than they resemble the search in Carey, both before and after they

discovered the child pornography evidence. First, both agents here spent very little

time looking at the child pornography images they discovered. They noticed them,

alerted a supervisor, and then moved on to the rest of the images on the same CD (in

Nishida’s case), or the other CDs (in Cravens’ case), looking for evidence of

computer fraud. Both responses were reasonable because, as mentioned above, the

agents were not required to stop searching altogether. And both responses

demonstrate an effort to navigate away from the nonresponsive material and toward

files that they believed were more likely to contain material responsive to the

warrant. Second, the files on the CDs that the agents previewed were not

characteristically distinct or set apart from the other files, in contrast to Carey. Agent

Cravens testified that, when he put a CD into his computer to see the files that it

                                            23
contained, the computer pulled up a generic list of those files. The record does not

indicate that there were any folders or distinctive titles setting clearly apart the

nonresponsive child pornography files from the other files on the disk. Loera bears

the burden of proof on his suppression motion, and he has offered no evidence on this

point. Third, the agents discovered the child pornography files inadvertently on

November 20. Fourth, both agents’ search methods were reasonably narrow under

the circumstances, considering the fact that the CDs did not seem particularly

organized. Given that the warrant permitted the agents to search the CDs for

“photographs,” “documents,” and “configuration files,” it was reasonable for Nishida and

Cravens to search all file types on the CDs (image, video, and text) for evidence of

computer fraud rather than to narrow that search to one particular file type. The agents’

searches on November 20 were reasonable because they fell within the scope of the

first warrant both before and after they discovered the child pornography evidence. We

reverse the district court’s ruling to the contrary.

   3. November 27 search was unreasonable

       Loera also argues that Agent Cravens’ subsequent search on November 27,

2012, of the four seized CDs that contained child pornography violated the Fourth

Amendment because Cravens was “[i]ntentionally searching for evidence of a crime

outside the scope of the [f]irst [w]arrant prior to obtaining a new warrant.” Aplt. Br. 29.

In making this argument, Loera accepts that the first warrant permitted the government to

seize the four CDs that were found to contain some child pornography and to search them

for evidence of computer fraud. Therefore, Loera challenges Cravens’ November 27

                                              24
search only for exceeding that permission. Accordingly, we confine our analysis to

whether the second search exceeded the scope of the first warrant. The district court

concluded that it did and that neither exigent circumstances nor any other exception to

the warrant requirement justified that search. We agree and conclude that the district

court correctly excised the evidence obtained during the November 27th search from

Cravens’ affidavit for the second warrant. Several of the district court’s factual findings

support that result.

       The district court found that “Cravens was not searching for evidence of

electronic fraud” on November 27 but instead was searching for child pornography.

Dist. Ct. Op. at 144. The district court based this finding on Cravens’ testimony at the

suppression hearing that he reopened Loera’s CDs on November 27 specifically “[t]o

write a description of an image on the disc” so that he could “obtain a second warrant

for child pornography.” ROA Vol. II at 72. That admission is the most probative

fact in the record that Cravens’ search was directed at finding child pornography.

The district court also found that Cravens had the four CDs for a total of two-and-a-

half hours that day, during which time he searched the CDs and drafted the second

affidavit. Although the record does not indicate how long Cravens searched the CDs,

he testified at the suppression hearing that he looked at several images on each CD—

“more than just a couple” but “[m]ost likely less than a dozen.” ROA Vol. II at 143.

Whatever the amount of time, Cravens’ devoted it exclusively to nonresponsive

material. Rather than navigate away from the child pornography images when he found

them, Cravens explicitly navigated toward such images. Based on these findings, we

                                             25
agree with the district court that, in contrast with the agents’ searches on November

20, Agent Cravens’ search on November 27 was unreasonable because it was directed

at uncovering evidence of child pornography.

       The government argues that two exceptions save Cravens’ search from

violating the Fourth Amendment: the plain view doctrine and the foregone-

conclusion exception. We disagree. For its plain view argument, the government

asserts that the law permitted Agent Cravens to take a “second look” at the child

pornography images on Loera’s CDs because members of the FBI had already seen

the images in plain view during a lawful search, and, therefore, his “second look”

was no further invasion of Loera’s privacy than the initial, lawful viewing. The

government points to a Fourth Circuit case, United States v. Jackson, 131 F.3d 1105

(4th Cir. 1997), where a law enforcement officer had consent to search a residence for a

fugitive. Id. at 1107. While looking for the fugitive in the basement, the officer observed

some suspicious metal items on the floor. Id. He did not pause to examine those items at

that time, but he instead proceeded to finish his sweep for the fugitive. Id. Once

finished, he went back to take a closer look at the objects on the floor, this time

recognizing them as drug paraphernalia. Id. More officers arrived and took a look at the

paraphernalia, eventually using the presence of those items to obtain a search warrant for

the house, which uncovered a gun and large quantities of drugs. Id. at 1108. That further

search was held to have been constitutional under the plain-view doctrine. Id.

       There are too many factual distinctions between Jackson and this case to permit

Cravens’ second look under the plain view doctrine. First, as government counsel

                                             26
admitted at oral argument, there is no evidence in the record that Cravens looked at the

same photos on November 27 that the officers viewed on November 20. Second, seven

days elapsed between the first and second searches in this case, not a matter of minutes.

Third, Cravens’ “second look” led him to peruse more than just the child pornography

images, so we cannot say that the November 27 search did not cause a further invasion

of Loera’s privacy. The plain view doctrine permits the warrantless seizure of

evidence of criminal activity when police officers observe the evidence during a

lawful search. United States v. Naugle, 997 F.2d 819, 822 (10th Cir. 1993). That

doctrine cannot be used to justify Cravens’ November 27 search.

       The government also argues that Cravens’ “second look” was justified under

what it has termed the “foregone-conclusion exception” to the warrant requirement.

This doctrine comes from several of our plain view cases where we have permitted

the warrantless search of containers in plain view whose contents “are a foregone

conclusion” because the container is “not closed,” “transparent,” or, if it is closed,

“its ‘distinctive configuration . . . proclaims its contents’” nonetheless. United States

v. Corral, 970 F.2d 719, 725 (10th Cir. 1992). We have also held that the doctrine

applies “where the police have already seen the contents of a seized container prior to

conducting the search, [because] there is no significant additional invasion of privacy

involved in searching the container.” Id. at 725. We reject this argument for the

same reasons as the government’s plain view argument. Here, Cravens knew to a

near certainty that the seized and re-searched CDs contained some child pornography,

but he had no idea what else they contained. And, again, there is no evidence that

                                            27
Cravens had previously seen the child pornography images that he viewed on

November 27.

       Thus, Cravens’ November 27 search was unlawful because it exceeded the scope

of the first warrant and none of the exceptions to the warrant requirement apply.

   D. Reasonableness of the Searches Conducted Under the Second Warrant

       Additionally, Loera argues that the child pornography evidence that Agent

Nishida discovered when he executed the second warrant should have been

suppressed because the second warrant was not supported by probable cause and no

exceptions to the warrant requirement apply. We agree that the second warrant was

not supported by probable cause and that the good faith exception is inapplicable

here. However, the inevitable discovery doctrine supports the district court’s denial

of Loera’s motion to suppress, and we affirm on that basis.

   1. Second warrant was not supported by probable cause

       We review whether a magistrate properly issued a search warrant by determining

whether there was a “substantial basis” for probable cause in the affidavit submitted in

support of the warrant. Illinois v. Gates, 462 U.S. 213, 236 (1983). Because we find

that the November 27 search was unlawful, we must excise from the affidavit that

Cravens filed in support of the second warrant all of the descriptions of child

pornography that he unlawfully obtained during the second search and then

determine whether “there was probable cause absent that information.” United States

v. Sims, 428 F.3d 945, 954 (10th Cir. 2005). The district court determined that the



                                            28
second warrant remained supported by probable cause without the tainted

descriptions. We disagree.

       While “probable cause does not demand the certainty we associate with formal

trials,” Gates, 462 U.S. at 246, “[s]ufficient information must be presented to the

magistrate to allow that official to determine probable cause; his action cannot be a mere

ratification of the bare conclusions of others,” id. at 239 (emphasis added). For example,

“[a] sworn statement of an affiant that ‘he has cause to suspect and does believe that’

liquor illegally brought into the United States is located on certain premises” is not

sufficient to support a finding that probable cause exists to search the premises. Id.

       The child pornography descriptions that Agent Cravens obtained during the

unlawful second search appear in paragraphs 24-27 of Cravens’ affidavit. Once we

excise those descriptions, all that remains substantively is Cravens statement that,

“During the preview, the examiners identified four writable CDs which appeared to

contain images of child pornography.” ROA Vol. I at 120. This sentence does not

support a finding of probable cause.

       In United States v. Pavulak, the Third Circuit reviewed an affidavit to support

a warrant to search for child pornography that contained language very similar to the

bare-bones description left in the affidavit in our case, 700 F.3d 651, 661 (3d Cir.

2012). The warrant affidavit in Pavulak stated that an informant had seen the

defendant “viewing child pornography” of females “between 16 and 18 years old,”

without providing any further details about what the images depicted. Id. at 657.

The Third Circuit held that the affidavit lacked probable cause because it did not

                                             29
allow the magistrate judge “to independently evaluate whether the contents of the

alleged images [met] the legal definition of child pornography.” Id. at 661. We find

that analysis persuasive here. Agent Cravens’ remaining statement that the CDs

“appeared to contain images of child pornography” provides no detailed description

of what the images depicted such that a magistrate could independently assess

whether the images meet the legal definition of child pornography. ROA Vol. I at

120.

       Therefore, the affidavit supporting the second warrant lacked probable cause

absent the tainted information. We reverse the district court’s contrary conclusion.

   2. Good-faith exception inapplicable to these facts

       Next, we consider whether the good faith exception to the exclusionary rule

from United States v. Leon, 468 U.S. 897, 918 (1984), applies when police execute a

search warrant that is based on information obtained through an unlawful predicate

search. Disagreeing with the district court, we conclude that it does not. The

Supreme Court’s opinion in Leon and our opinion in United States v. Scales, 903

F.2d 765, 768 (10th Cir. 1990), dictate that the good faith exception does not apply in

a case like the one before us because the illegality at issue stems from unlawful

police conduct, rather than magistrate error, and therefore the deterrence purposes of

the Fourth Amendment are best served by applying the exclusionary rule.

       In United States v. Leon, the Supreme Court modified the exclusionary rule

“so as not to bar the use in the prosecution’s case in chief of evidence obtained by

officers acting in reasonable reliance on a search warrant issued by a detached and

                                          30
neutral magistrate but ultimately found to be unsupported by probable cause,” 468

U.S. at 900. The Court reasoned that the purpose of the exclusionary rule is to deter

police misconduct and in such a case “there is no police illegality and thus nothing to

deter.” Id. at 920. In this circuit, “Leon’s good faith exception applies only narrowly,

and ordinarily only when an officer relies, in an objectively reasonable manner, on a

mistake made by someone other than the officer.” United States v. Cos, 498 F.3d 1115,

1132 (10th Cir. 2007) (declining to apply good faith exception to warrantless search of

apartment where officers mistakenly believed the person that consented to the search had

the authority to do so); United States v. Herrera, 444 F.3d 1238, 1251 (10th Cir. 2006)

(declining to apply good faith exception to state trooper who conducted a warrantless

inspection of a truck based on the officer’s mistaken belief the truck was a commercial

vehicle subject to such inspection). Thus, Leon is inapplicable here where the

mistake—the unconstitutional second search—was the fault of the officer, not the

magistrate.

      We considered whether Leon applied to a warrant affidavit based on tainted

evidence in Scales, 903 F.2d at 768. There, we held that Leon did not apply to

excuse a law enforcement officer’s reliance on a search warrant where the facts in the

warrant affidavit were obtained through an unlawful predicate seizure. In that case,

DEA agents seized a suitcase that they believed contained drugs. Id. at 767. Then,

they took the suitcase to a drug-sniffing canine team that signaled the suitcase did

contain drugs. Id. Finally, after having had the suitcase in their possession for

twenty-four hours, the agents applied for and obtained a warrant to search the

                                            31
suitcase based on the probable cause provided by the canine alert. Id. Upon

conducting the search, the agents discovered more than 2,000 grams of cocaine in the

suitcase. Id. The defendant moved to suppress the cocaine evidence, arguing that the

agents’ initial seizure of the suitcase was unlawful because it was unsupported by

probable cause. Id. at 767.

      The district court in Scales denied the motion, finding that, even if the seizure

of the suitcase was unlawful, the good faith exception ratified the agents’ behavior.

Id. We reversed, holding that Leon was inapplicable “[b]ecause the DEA agents

were not acting in reliance on a search warrant when they seized the luggage and held

it for more than twenty-four hours.” Id. at 768. Our holding was informed by the

reasoning in Leon that “Penalizing the officer for the magistrate’s error, rather than

his [or her] own, cannot logically contribute to the deterrence of Fourth Amendment

violations.” Id. at 768 (quoting Leon, 468 U.S. at 921) (alteration in original).

Because the contraposition is also true—that penalizing an officer for his or her own

error does contribute to deterrence—we determined that the exclusionary rule must

apply to the agents’ unlawful pre-warrant seizure of the suitcase. Id.

      Scales and Leon control our outcome here. Cravens conducted an unlawful

search of Loera’s CDs on November 27 in the absence of a warrant. He included the

tainted fruit that he uncovered during that search in the affidavit that he submitted in

support of the second warrant. Cravens’ warrant affidavit was facially valid, and

therefore the magistrate did not error by issuing a warrant based upon it. Instead, the

constitutional error came from Agent Cravens.

                                           32
      The government argues that Cravens acted in good faith because he

“transparently informed the magistrate judge of the steps he had taken to obtain the

descriptions he included in his affidavit.” Aple. Br. at 40. Cravens’ affidavit

provided some information about the first search. It explained that, while executing

the first search warrant, the FBI agents identified four CDs that contained child

pornography and seized them. Then, Cravens wrote:

      On November 27, 2012, the writer, an FBI certified CART Technician,
      reviewed the four CDs, each of which are designated in attachment A,
      that were believed to contain child pornography. During the review of
      the CDs, the writer observed multiple pictures of children many of
      which are in various state of dress including the following images . . . .

ROA Vol. I at 50. However, that information was not sufficient to allow the

magistrate to determine the constitutionality of the second search such that the

magistrate can be said to have endorsed Cravens’ pre-warrant conduct. Furthermore,

even if it was, that would not affect our outcome. Tenth Circuit precedent dictates

that the good faith exception does not apply at all when a warrant affidavit is based

on tainted evidence from a prior, unlawful search.

      Four other circuits have likewise concluded that Leon is inapplicable when an

officer executes in good faith a search warrant that is based on unlawfully-obtained

evidence. United States v. Scott, 731 F.3d 659, 664 (7th Cir. 2013) (holding that

evidence discovered pursuant to a warrant based on illegally-obtained evidence will

be inadmissible unless other, untainted information in the affidavit establishes

probable cause); United States v. Mowatt, 513 F.3d 395, 405 (4th Cir. 2008) (holding

that “Leon only prohibits penalizing officers for their good-faith reliance on

                                          33
magistrates’ probable cause determinations” and that the exclusionary rule operates

to penalize officers for any unconstitutional conduct preceding a magistrate’s

involvement); United States v. McGough, 412 F.3d 1232 (11th Cir. 2005) (refusing

to apply good faith exception where an unlawful entry into the defendant’s apartment

led to the officer’s request for a search warrant); United States v. Vasey, 834 F.2d

782, 789 (9th Cir. 1987) (holding that good faith exception did not apply to a warrant

that was based on information obtained in an illegal warrantless search because “[t]he

constitutional error was made by the officer . . ., not by the magistrate”). At least two

commentators support this analysis as well. See Wayne R. LaFave, Search &

Seizure: A Treatise on the Fourth Amendment § 1.3(f) (5th ed. 2016) (explaining

that, because courts rarely require affiants to prove that they obtained the evidence

listed in an affidavit lawfully, “there is no reason why that process should, via Leon,

shield that activity from full scrutiny at the suppression hearing”); Craig M.

Bradley, The “Good Faith Exception” Cases: Reasonable Exercise in Futility, 60 Ind.

L.J. 287, 302 (1985) (quoting Leon, 468 U.S. at 914) (“When the magistrate issued

the warrant, he did not endorse past activity; he only authorized future activity. . . .

[T]he function of the magistrate is to determine ‘whether a particular affidavit

establishes probable cause,’ not whether the methods used to obtain the information

in that affidavit were legal.”).

       However, five other circuits have concluded that the good faith exception can

apply where an affidavit supporting a search warrant is tainted by illegally-obtained

evidence in at least some limited circumstances. Three of those circuits apply the

                                            34
good faith exception if the predicate search, although ultimately determined to be

unlawful, was arguably lawful under the binding precedent in effect at the time of the

search. United States v Bain, 874 F.3d 1, 22–23 (1st Cir. 2017) (applying good faith

exception because binding precedent did not “clearly classify” as unlawful the

conduct that invalidated the predicate search); United States v. Hopkins, 824 F.3d

726 (8th Cir. 2016) (applying good faith exception because the reasonableness of the

illegal predicate search was “close enough to the line of validity” to make an

officer’s belief in the validity of the warrant objectively reasonable); United States v.

Holley, 831 F.3d 322, 326–27 (5th Cir. 2016) (also applying “close enough to the

line of validity” test). Two other circuits apply the good faith exception in these

types of cases when (1) the predicate search was arguably reasonable and (2) the

warrant affidavit truthfully conveyed the circumstances of the illegal predicate search

to the magistrate judge. United States v. McClain, 444 F.3d 556, 566 (6th Cir. 2005)

(applying Leon because the reasonableness of the predicate search was a close call

and the warrant affidavit “fully disclosed” the circumstances surrounding the initial

warrantless search); United States v. Thomas, 757 F.2d 1359 (2d Cir. 1985) (applying

good faith exception because officer’s affidavit fully described the unlawful, pre-

warrant canine sniff that supplied probable cause for the warrant and there was

“nothing more the officer could have or should have done” to be sure his search was

legal). We cannot read Leon or Scales to support the rules adopted by these courts.

When a magistrate issues a warrant based on illegally obtained evidence, typically the

manner in which the affidavit evidence is obtained is not before the magistrate, and the

                                            35
magistrate is not asked explicitly to endorse the evidence-gathering procedure. Even

though some disclosure of the evidence-gathering technique may have occurred, that is

not ordinarily the focus of an application for a warrant. Thus, we are unwilling to read a

warrant as ratifying the information-gathering process of a search that preceded it. In any

event, we are bound by Scales, which appears to us to have been correctly decided.

       Therefore, the district court erred by finding that the good faith doctrine applied to

the searches Agent Nishida conducted in execution of the second warrant.

   3. Inevitable discovery doctrine supports denial of Loera’s motion

       Finally, we consider whether the government would have inevitably discovered

the child pornography evidence on Loera’s electronic devices. Loera argues that, because

there was no probable cause to support the second warrant, all evidence discovered as a

result of the execution of the second warrant should have been suppressed. The issue

before us, then, is whether the FBI agents would have inevitably discovered the roughly

330 child pornography images on Loera’s CDs and 730 child pornography images on

Loera’s laptop that Nishida found when he executed the second warrant. We conclude

that they would have. Accordingly, we affirm the district court’s denial of Loera’s

motion to suppress.

       When evidence is obtained in violation of the Fourth Amendment, that

evidence need not be suppressed if agents inevitably would have discovered it

through lawful means independent from the unconstitutional search. United States v.

Christy, 739 F.3d 534, 540 (10th Cir. 2014). The government is required to prove by a

preponderance of the evidence that the unlawfully-obtained evidence would have been

                                             36
discovered through lawful means. Id. The “lawful means” need not be a second,

independent investigation. Id. Rather, the inevitable discovery doctrine will apply if

there was “one line of investigation that would have led inevitably to the obtaining of a

search warrant by independent lawful means but was halted prematurely by a search

subsequently contended to be illegal.” Id. (citations omitted). The key to applying this

doctrine is to place the government officers in the “same positions they would have

been in had the impermissible conduct not taken place,” and, from that vantage point,

to ask whether the government would have inevitably discovered the evidence

lawfully. Nix v. Williams, 467 U.S. 431, 447 (1984).

       Here, the district court’s supportable findings demonstrate by a preponderance of

the evidence that the FBI would have inevitably discovered the child pornography

evidence on Loera’s electronic devices through lawful means independent from Agent

Cravens’ unlawful second search. On November 26 (the day before the second search),

the government lawfully had in its possession Loera’s computers, external hard drives,

iPhone, iPad, and thirteen CDs (nine without child pornography and four with child

pornography).4 The government had the authority under the first warrant to search

Loera’s electronic devices—most importantly his laptop and CDs—for evidence of

computer fraud. The district court issued an explicit factual finding that, had the

second warrant never been obtained, Agent Nishida would “have searched [Loera’s



4
  As mentioned above, although Loera challenges the first search of these four CDs,
he does not separately challenge their seizure were we to determine, as we have, that
the first search was constitutional.
                                            37
laptop] for evidence of electronic mail hijacking and computer fraud pursuant to the

[f]irst [w]arrant.” Dist. Ct. Op. at 24. The district court further found that, as part of

that search, lawfully conducted pursuant to the parameters of the first warrant, Agent

Nishida would have searched the electronic folders where he discovered child

pornography when he executed the second warrant, including, the “My Documents”

folder, the “Bookmarks” tab of Loera’s internet browser, and a folder saved on the

Desktop titled “Allmyfiles.txt.” Id. at 24–25. The district court also accepted

Nishida’s statement that, had he found child pornography images on the laptop

during a search conducted solely pursuant to the first warrant, he would have “alerted

the case agent so that [he] could get a search warrant for child pornography.” Id. at

25.

      The laptop, including the specific files referenced above, contained over 730

images and 40 movies involving child pornography. Id. at 24. To take one specific

example, the “Allmyfiles.txt” file, which the district court found Nishida would have

lawfully opened pursuant to the first warrant, contained files called “Spycam 9yr

Undress.” Id. Such information would have been sufficient to establish probable

cause to support a warrant to search all of the electronic devices belonging to Loera

that the government had in its possession, including the four CDs that Agent Cravens

searched unlawfully on November 27. That fact, combined with Agent Nishida’s

indication that he would have sought a warrant, allows us to conclude that the

inevitable discovery doctrine applies in this case such that the evidence discovered

pursuant to the second warrant did not need to be suppressed.

                                            38
                             III.   CONCLUSION

      For the foregoing reasons, we AFFIRM the orders of the district court denying

the defendant’s motion to suppress and motion for reconsideration.




                                         39

```

---

## GROUP: content/cases/United States v. Lundin.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Lundin"
type: case
citation: "817 F.3d 1151 (2016)"
parallel_cite: ""
neutral_cite: "2016 WL 1104851; 2016 U.S. App. LEXIS 5236"
court: "U.S. Court of Appeals, 9th Circuit"
court_level: coa
circuit: 9th
year: 2016
date_decided: 2016-03-22
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2016-03-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Lundin
  varies_by_point: false
  scope_note: "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/"
  cluster_id: 3187682
  opinion_id: 3187625
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Illustrates a circuit split"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Florida v. Jardines]]", "[[Kentucky v. King]]", "[[Oliver v. United States]]", "[[United States v. Carloss]]", "[[United States v. Walker]]"]
aliases: ["United States v. Eric Lundin", "United States v. Lundin (9th Cir. 2016)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "implied-license", "curtilage", "arrest", "ninth-circuit"]
holding: "The knock-and-talk implied license is bounded by both time and purpose: a pre-dawn (around 4:00 a.m.) knock, undertaken with the intent to arrest the occupant rather than to ask questions, exceeds the customary license — so the exception does not apply and the porch knock (and the search it precipitated) violated the Fourth Amendment."
lake:
  record_id: United States v. Lundin
  status: verified
  projected_at: 2026-07-09
---

# United States v. Lundin

*817 F.3d 1151 (9th Cir. 2016)* · U.S. Court of Appeals, 9th Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Susan Hinds reported that Eric Lundin had assaulted and briefly kidnapped her, deputies issued a be-on-the-lookout and a request for Lundin's warrantless arrest. Around 4:00 a.m. on April 23, 2013, three officers approached Lundin's home — without an arrest warrant or a search warrant — came onto his front porch, and knocked with the intent of arresting him. From the porch they heard crashing noises from the backyard, ran to the back, ordered Lundin out of the fenced-in yard, and arrested him. Officers then searched the home and patio and found two handguns in open view. The district court suppressed the handguns as the fruit of an illegal search, and the United States appealed.

## Issue
Whether the "knock and talk" exception authorized officers to enter the [[Curtilage|curtilage]] and knock on the front door at 4:00 a.m. with the intent to arrest the occupant, where the knock precipitated the noises the officers then used to justify a warrantless search.

## Rule
The [[Knock and Talk|knock-and-talk]] exception is "coterminous with th[e] implicit license" to approach and knock, and the court held the officers exceeded that license "[f]or two reasons." First, time: "unexpected visitors are customarily expected to knock on the front door of a home only during normal waking hours," and here the officers "knocked on Lundin's door around 4:00 a.m. without evidence that Lundin generally accepted visitors at that hour, and without a reason for knocking that a resident would ordinarily accept as sufficiently weighty to justify the disturbance." — 817 F.3d at 1159. ^pin-1159

Second, purpose: "the scope of a license is often limited to a specific purpose," the customary license "is generally limited to the 'purpose of asking questions of the occupants,'" and "[o]fficers who knock on the door of a home for other purposes generally exceed the scope of the customary license and therefore do not qualify for the 'knock and talk' exception." — [*Id.*](https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/#:~:text=the%20scope%20of%20a%20license) ^pin-1159a

After *[[Florida v. Jardines|Jardines]]*, "the 'knock and talk' exception depends at least in part on an officer's subjective intent," and the court held: "The 'knock and talk' exception to the warrant requirement does not apply when officers encroach upon the curtilage of a home with the intent to arrest the occupant." — 817 F.3d at 1160. ^pin-1160

## Application
The front porch is the "classic exemplar" of [[Curtilage|curtilage]], so the officers' presence there and their knock were a presumptively unreasonable search unless licensed. They were not: the approach occurred around 4:00 a.m., outside normal waking hours and without any reason a resident would accept as justifying so early a disturbance, and the district court found the officers' clear purpose was to arrest Lundin, not to ask questions. Because the knock exceeded the customary license on both the time and purpose dimensions, the [[Knock and Talk|knock-and-talk]] exception did not apply; and since the officers' own unlawful knock caused the crashing noises, they could not rely on those noises as [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] to justify the ensuing warrantless search.

## Conclusion
The officers exceeded the implied license, so the porch knock was an unlawful search and the search it precipitated was illegal; the Ninth Circuit affirmed suppression of the handguns.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- *Lundin* applies [[Florida v. Jardines]] to hold the implied license is limited by **time** and **purpose**, and that an officer's intent to arrest takes the approach outside the [[Knock and Talk|knock-and-talk]] exception — making the officer's subjective purpose relevant, an approach that divides the circuits. It also invokes [[Kentucky v. King]]'s rule that police may not rely on [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] they create through their own Fourth Amendment violation. Contrast [[United States v. Walker]] (11th Cir.), upholding a pre-dawn knock and talk on its facts, and [[United States v. Carloss]] (10th Cir.) on what conduct withdraws the license.

## Appears on
- [[Knock and Talk]] — *Illustrates a circuit split*
- [[Curtilage]] — *Related (cross-doctrine)*

## Sources
- *United States v. Lundin*, 817 F.3d 1151 (9th Cir. 2016) — https://www.courtlistener.com/opinion/3187682/united-states-v-eric-lundin/ — pinpoints: 1159, 1160.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ed13fc2d625b0e0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "817 F.3d 1151 (2016)", "court": "U.S. Court of Appeals, 9th Circuit", "neutral_cite": "2016 WL 1104851; 2016 U.S. App. LEXIS 5236", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Lundin", "year": "2016"}}
{"assertion_id": "0feb7e750e0b3d67", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Illustrates a circuit split", "title": "United States v. Lundin"}}
{"assertion_id": "18f461e9eb5a56b5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The knock-and-talk implied license is bounded by both time and purpose: a pre-dawn (around 4:00 a.m.) knock, undertaken with the intent to arrest the occupant rather than to ask questions, exceeds the customary license — so the exception does not apply and the porch knock (and the search it precipitated) violated the Fourth Amendment.", "title": "United States v. Lundin"}}
{"assertion_id": "e37eb8be1d7b17fd", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "United States v. Lundin"}}
{"assertion_id": "5063cff478da2535", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2016-03-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Lundin", "field_i_validity": "good_law", "scope_note": "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception.", "title": "United States v. Lundin", "varies_by_point": "false"}}
{"assertion_id": "8d6976a08634bc24", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "United States v. Lundin"}}
```

### lake record — United States v. Lundin

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Lundin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Eric Lundin",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Eric Eugene LUNDIN, AKA Whitey, Defendant-Appellee",
    "input_case_name": "United States v. Lundin",
    "court": "U.S. Court of Appeals, 9th Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2016-03-22",
    "year": 2016,
    "docket": null,
    "cluster_id": 3187682,
    "lead_opinion_id": 3187625,
    "sibling_ids": [
      3187625
    ],
    "absolute_url": "/opinion/3187682/united-states-v-eric-lundin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "817 F.3d 1151",
      "volume": "817",
      "reporter": "F.3d",
      "page": "1151",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2016 WL 1104851",
        "volume": "2016",
        "reporter": "WL",
        "page": "1104851",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 5236",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "5236",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "817 F.3d 1151",
        "volume": "817",
        "reporter": "F.3d",
        "page": "1151",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 1104851",
        "volume": "2016",
        "reporter": "WL",
        "page": "1104851",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. App. LEXIS 5236",
        "volume": "2016",
        "reporter": "U.S. App. LEXIS",
        "page": "5236",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "817 F.3d 1151",
    "official_selection": {
      "court_class": "coa",
      "selected": "817 F.3d 1151",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1159",
      "page": null,
      "quote": "exception authorized officers to enter the curtilage and knock on the front door at 4:00 a.m. with the intent to arrest the occupant, where the knock precipitated the noises the officers then used to justify a warrantless search. ## Rule The knock-and-talk exception is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1159a",
      "page": null,
      "quote": "the scope of a license is often limited to a specific purpose,",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 19208,
      "fragment": "#:~:text=the%20scope%20of%20a%20license",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1160",
      "page": null,
      "quote": "the 'knock and talk' exception depends at least in part on an officer's subjective intent,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-03-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Lundin",
    "varies_by_point": false,
    "scope_note": "Good law. Holds the knock-and-talk implied license is bounded by time and purpose, and that an officer's intent to arrest defeats the exception.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Andre Staggers",
          "cluster_id": 4759755,
          "cite": [
            "961 F.3d 745"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Aaron Holmes, Jr.",
          "cluster_id": 10273168,
          "cite": [
            "121 F.4th 727"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Esqueda",
          "cluster_id": 9451359,
          "cite": [
            "88 F.4th 818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Escobar",
          "cluster_id": 7330094,
          "cite": [
            "309 F. Supp. 3d 778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brett Parkins",
          "cluster_id": 9475415,
          "cite": [
            "92 F.4th 882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brett Parkins",
          "cluster_id": 9475001,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Hylton, Jr.",
          "cluster_id": 6458860,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murchison v. County of Tehama",
          "cluster_id": 5178968,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Lundin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3187625) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(3187625)",
        "reviewed": 9,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(3187625)",
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
    "complete_query": "cites:(3187625)",
    "indexed_citing_opinions": 9,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3187625,
        "count": 9,
        "count_source": "search"
      }
    ],
    "citation_count": 68,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-lundin.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 9,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3187625,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 380517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 461076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 475484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 691388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 706974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 755893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 770197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 771671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 782687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 801335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1348637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1382743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3187625,
        "cited_id": 1447779,
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
    "date_created": "2026-07-06T01:24:15Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:26:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:24:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Lundin

```
                FOR PUBLICATION

  UNITED STATES COURT OF APPEALS
       FOR THE NINTH CIRCUIT


UNITED STATES OF AMERICA,                No. 14-10365
               Plaintiff-Appellant,
                                           D.C. No.
                 v.                     4:13-cr-00402-
                                            JST-1
ERIC EUGENE LUNDIN, AKA
Whitey,
              Defendant-Appellee.           OPINION


      Appeal from the United States District Court
        for the Northern District of California
        Jon S. Tigar, District Judge, Presiding

               Argued and Submitted
    September 18, 2015—San Francisco, California

                 Filed March 22, 2016

    Before: William A. Fletcher, Marsha S. Berzon,
          and Carlos T. Bea, Circuit Judges.

             Opinion by Judge W. Fletcher
2                  UNITED STATES V. LUNDIN

                           SUMMARY*


                          Criminal Law

    In an interlocutory appeal by the government, the panel
affirmed the district court’s order suppressing handguns
seized from the defendant’s home, and remanded for further
proceedings.

    The panel held that the warrantless search of the
defendant’s home was not justified by exigent circumstances.
The panel explained that the “knock and talk” exception to
the warrant requirement does not apply when officers
encroach upon the curtilage of a home with the intent to arrest
the occupant. The panel saw no reason to disturb the district
court’s finding that the officers’ purpose in knocking on the
defendant’s door at 4:00 a.m., in response to a deputy’s
request that the defendant be arrested, was to find and arrest
him. The panel held that the officers therefore violated the
defendant’s Fourth Amendment right to be free from
unlawful searches when they stood on his porch and knocked
on his front door. Since this unconstitutional conduct caused
the allegedly exigent circumstance— crashing noises in the
backyard—the panel concluded that that circumstance cannot
justify the search resulting in the seizure of the handguns.

    The panel held that the warrantless search was not
justified as a protective sweep, because the officers lacked a
reasonable ground for believing that there was a danger that
would have justified the sweep of the defendant’s home.

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
                 UNITED STATES V. LUNDIN                     3

    The panel held that the inevitable discovery exception to
the exclusionary rule does not apply, because the officers
knew they had probable cause to arrest the defendant but
failed to obtain any warrant before coming onto his porch and
knocking on his door with the intention of arresting him.


                         COUNSEL

Barbara J. Valliere (argued), Chief, Appellate Division, and
Melinda Haag, United States Attorney, San Francisco,
California, for Plaintiff-Appellant.

Geoffrey A. Hansen (argued), Chief Assistant Federal Public
Defender, Steven G. Kalar, Federal Public Defender, and
Steven J. Koeninger, Research and Writing Attorney, San
Francisco, California, for Defendant-Appellee.


                         OPINION

W. FLETCHER, Circuit Judge:

    Around 4:00 a.m. on April 23, 2013, three northern
California law enforcement officers approached Defendant
Eric Lundin’s home without either an arrest warrant or a
search warrant. They came onto his front porch and knocked
on his door with the intent of arresting him. From the front
porch where they were standing, the officers heard crashing
noises coming from the back of the house. They ran to the
back, ordered Lundin to come out of the fenced-in backyard,
and arrested him. After putting Lundin in a patrol car, several
officers briefly searched Lundin’s home, including the back
patio where they found two handguns in open view. The
4                UNITED STATES V. LUNDIN

district court suppressed the handguns as the result of an
illegal search. The United States appeals. We hold that the
officers violated the Fourth Amendment when they knocked
on the door at 4:00 a.m. without a warrant with the intent of
arresting Lundin, and that the immediately ensuing search
was illegal. We therefore affirm.

                        I. Background

    At 12:24 a.m. on April 23, 2013, Deputy Sheriff Scott
Aponte of the Humboldt County Sheriff’s Office (“HCSO”)
was dispatched to the Mad River Community Hospital to
interview Susan Hinds, a 63-year-old patient who claimed she
had been kidnapped several hours earlier. In a tape-recorded
statement, Hinds told Deputy Aponte that sometime after
8:00 p.m. on April 22, shortly after her son, Joseph Miller,
had left to go to the store, Eric “Whitey” Lundin knocked on
the door of her mobile home. When Hinds opened the door,
Lundin grabbed her by the neck, forced his way inside, and
accused Miller of stealing marijuana from him.

    Hinds told Deputy Aponte that, once inside the mobile
home, Lundin took two firearms from his pockets — a
compact silver handgun and a large black handgun. He then
took out a bottle of pills and forced Hinds to ingest one of the
pills. He described the pills to Hinds as “methadone” and
told her that they were the easiest way to overdose. After
forcing Hinds to ingest the pill, Lundin broke her television
by striking it with one of the handguns. Lundin then pressed
the black handgun against Hinds’s temple and forced her to
call Miller to tell him to come home. When the call ended,
Lundin snatched Hinds’s cell phone and threw it across the
room.
                 UNITED STATES V. LUNDIN                    5

    Hinds told Deputy Aponte that Lundin repeatedly said
that she was going to die and that, as a member of the
Mongols motorcycle gang, he does not “leave witnesses.”
Lundin received two calls on his cell phone while still at the
mobile home. Hinds heard him say during one of the calls,
“I’m taking care of it. I’ve got her right here on the couch.”

     Hinds said that Lundin then forced her into his Dodge
truck. They passed Miller as they drove out of the mobile
home park. Lundin told Hinds, “Wave good-bye to your son.
You’ll never see him again.” During the drive, Lundin forced
Hinds to ingest two more pills and pointed out locations
where he could safely dispose of her body. Lundin then
spoke with Miller on his cell phone and accused Miller of
stealing his marijuana. After ending the call with Miller,
Lundin told Hinds that he no longer believed Miller had
stolen his marijuana. Lundin drove Hinds back to her mobile
home, told her that he only meant to scare her, and warned
her not to call the police. He told her that he would buy her
a new television. Hinds had been in the truck a total of about
fifteen minutes.

    After concluding the interview with Hinds at the hospital,
Deputy Aponte interviewed Miller, who had come to the
hospital to see his mother. Miller told Aponte that Hinds had
called him while he was at the grocery store and had told him
to come home immediately. When he returned, the mobile
home was in disarray, and the television was broken. Miller
then called Lundin on his cell phone. Miller recounted to
Aponte that Lundin had accused him of stealing marijuana
and had told him that Lundin was going to send his “Mongol
brothers” to get Miller. After concluding the interview with
Miller, Aponte visited Hinds’s mobile home to photograph
the damage.
6                UNITED STATES V. LUNDIN

    Deputy Aponte asked dispatch to issue a “Be On the Look
Out” (“BOLO”) for Lundin and a request for Lundin’s arrest
under California Penal Code § 836. Section 836 authorizes
a warrantless arrest when there is probable cause to believe a
suspect has committed a felony. However, § 836 does not —
because it may not — authorize a warrantless arrest of a
suspect in his own home. Payton v. New York, 445 U.S. 573,
589–90 (1980). Aponte believed there was probable cause to
arrest Lundin for burglary, false imprisonment, kidnapping,
vandalism, brandishing a firearm, administering a drug to
commit a felony, administering a controlled substance, and
battery. HCSO dispatch issued the BOLO and arrest request
just before 2:00 a.m.

    Upon receiving the BOLO and arrest request, Arcata
Police Department (“APD”) Officer Matthew O’Donovan
used vehicle registration files to determine Lundin’s address.
O’Donovan then drove to Lundin’s home. When he arrived,
he saw a vehicle matching the description of Lundin’s Dodge
truck parked in the driveway and saw that lights were on
inside the house. O’Donovan called for backup. APD
Officer Jeremiah Kasinger, APD Sergeant Keith Altizer, and
HCSO Deputy Matthew Tomlin responded to the call,
arriving just before 4:00 a.m.

    Officer O’Donovan wrote in a declaration that he, Officer
Kasinger, and Deputy Tomlin approached Lundin’s front
door. O’Donovan wrote that without identifying themselves
they stood on the porch, knocked loudly, waited thirty
seconds for an answer, and then knocked more loudly. After
the second knock, the officers heard several loud crashing
noises coming from the back of the house. The officers ran
to the back of the house and heard someone moving around
in the backyard. The officers identified themselves and
                 UNITED STATES V. LUNDIN                     7

ordered Lundin “to put his hands in the air and come out
slowly.” When Lundin did so, Tomlin handcuffed him and
placed him in a patrol car.

    Officers O’Donovan and Kasinger then searched Lundin’s
backyard and patio, which were enclosed by a high fence.
They also searched inside the house. At the end of the search,
O’Donovan saw on the patio, in open view and within arm’s
reach of a common walkway, a clear plastic freezer bag
containing a silver revolver and a black semiautomatic
handgun. The bag was lying admidst a number of five-gallon
buckets that had been knocked over. The crashing noises
heard by the officers had likely been the buckets falling over.
O’Donovan notified Deputy Tomlin that he had found a bag
containing handguns, which Tomlin then photographed and
seized. When Deputy Aponte arrived, he confirmed that the
handguns matched Hinds’s description of the guns used
during the earlier incident. Aponte then advised Lundin of
his Miranda rights.

    On the morning of April 24, HCSO Deputy Todd Fulton
prepared an affidavit, statement of probable cause, and an
application for a warrant to search Lundin’s home. The
statement of probable case described Hinds’s report to
Deputy Aponte and stated, inter alia, that two firearms had
been located during the arrest at Lundin’s residence. A
California magistrate judge approved the warrant. At about
10:30 a.m. that morning, state and federal law enforcement
officers executed the warrant and seized numerous items from
inside the house, including guns, cell phones, a prescription
pill bottle for methadone, computers and hard drives, and
various Mongols paraphernalia.
8                UNITED STATES V. LUNDIN

    On June 20, Lundin was charged with being a felon in
possession of a firearm and ammunition in violation of
18 U.S.C. § 922(g)(1). Lundin moved to suppress the
evidence obtained from the patio and inside the house, as well
as statements he had made before he was read his Miranda
rights. Lundin contended that the two handguns seized from
the patio on April 23 should be suppressed as the fruits of an
unreasonable warrantless search, that the evidence seized
from his house on April 24 should be suppressed as the fruits
of an invalid search warrant, and that the pre-warning
information elicited by officers should be suppressed under
Miranda. On June 26, the district court suppressed the two
handguns seized on the patio. It otherwise denied Lundin’s
motion.

    On July 24, a grand jury returned a superseding
indictment charging Lundin with kidnapping in aid of
racketeering (18 U.S.C. § 1959(a)(1)), assault in aid of
racketeering (18 U.S.C. § 1959(a)(3)), kidnapping (18 U.S.C.
§ 1201(a)(1)), possession with intent to distribute and
manufacture marijuana (21 U.S.C. §§ 841(a)(1), (b)(1)(C)),
use or possession of a firearm in furtherance of a crime of
violence or a drug trafficking crime (18 U.S.C. § 924(c)(1)),
and being a felon in possession of a firearm (18 U.S.C.
§ 922(g)(1)). On July 25, after Lundin was arraigned on new
charges, the government timely took an interlocutory appeal
under 18 U.S.C. § 3731.

                  II. Standard of Review

    “Whether the exclusionary rule applies to a given case is
reviewed de novo, while the underlying factual findings are
reviewed for clear error.” United States v. Perea-Rey,
680 F.3d 1179, 1183 (9th Cir. 2012) (citation omitted). “We
                 UNITED STATES V. LUNDIN                     9

review the district court’s application of the inevitable
discovery doctrine for clear error because, although it is a
mixed question of law and fact, it is essentially a factual
inquiry.” United States v. Reilly, 224 F.3d 986, 994 (9th Cir.
2000); see United States v. Ruckes, 586 F.3d 713, 716 (9th
Cir. 2009); United States v. Lang, 149 F.3d 1044, 1048 (9th
Cir. 1998).

                       III. Discussion

    The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures . . . .” U.S. Const.
amend. IV. “At [its] very core stands the right of a [person]
to retreat into his own home and there be free from
unreasonable governmental intrusion.” Silverman v. United
States, 365 U.S. 505, 511 (1961). “[S]earches and seizures
inside a home without a warrant are,” therefore,
“presumptively unreasonable.” Payton, 445 U.S. at 586.
Evidence derived from an illegal search cannot “constitute
proof against the victim of the search.” Wong Sun v. United
States, 371 U.S. 471, 484 (1963).

    It is undisputed that the officers seized the two handguns
during a warrantless search of Lundin’s home. The handguns
are therefore the product of a presumptively unreasonable
search. To avoid suppression of the handguns, the
government must demonstrate that either an exception to the
warrant requirement or an exception to the exclusionary rule
applies. The government argues that the warrantless search
of Lundin’s home was justified either due to exigent
circumstances or as a protective sweep. In the alternative, the
government contends the handguns are admissible under the
10               UNITED STATES V. LUNDIN

inevitable discovery exception to the exclusionary rule. We
agree with the district court that these arguments fail.

                 A. Exigent Circumstances

    Law enforcement officers may conduct a warrantless
search of a home when “the exigencies of the situation make
the needs of law enforcement so compelling that [a]
warrantless search is objectively reasonable under the Fourth
Amendment.” Kentucky v. King, 563 U.S. 452, 460 (2011)
(alteration in original) (citation omitted). However, exigent
circumstances cannot justify a warrantless search when the
police “create the exigency by engaging . . . in conduct that
violates the Fourth Amendment.” Id. at 462.

    The officers in this case had no reason other than the
crashing noises coming from the backyard to believe that
there were exigent circumstances justifying a warrantless
search of Lundin’s home. However, the evidence shows that
the officers’ knock at Lundin’s front door caused him to make
the crashing noises. Thus, to show that exigent circumstances
justified the warrantless search, the government must show
that the officers lawfully stood on Lundin’s front porch and
knocked on his door.

    The area “immediately surrounding and associated with
the home” — the “curtilage” — is treated as “part of [the]
home itself for Fourth Amendment purposes.” Oliver v.
United States, 466 U.S. 170, 180 (1984). Like searches and
seizures inside the home itself, “searches and seizures in the
curtilage without a warrant are also presumptively
unreasonable.” Perea-Rey, 680 F.3d at 1184. The
presumption against warrantless searches and seizures “would
be of little practical value if the State’s agents could stand in
                 UNITED STATES V. LUNDIN                    11

a home’s porch or side garden and trawl for evidence with
impunity.” Florida v. Jardines, 569 U.S. —, —, 133 S. Ct.
1409, 1414 (2013).

    A government agent conducts a “search” within the
meaning of the Fourth Amendment when the agent infringes
“an expectation of privacy that society is prepared to consider
reasonable,” United States v. Jacobsen, 466 U.S. 109, 113
(1984), or “physically occupie[s] private property for the
purpose of obtaining information.” United States v. Jones,
565 U.S. —, —, 132 S. Ct. 945, 949 (2012). It is undisputed
that the officers physically occupied the curtilage of Lundin’s
home when they stood on the front porch and knocked on his
door. Indeed, the front porch of a home is the “classic
exemplar” of curtilage. Jardines, 133 S. Ct. at 1415. The
district court concluded that the officers’ clear purpose was
to determine whether Lundin was home and, if so, to arrest
him. Thus, the officers’ presence on Lundin’s front porch
and their knock at his door constituted a presumptively
unreasonable search.

    The government contends that the officers were permitted
to knock on Lundin’s door under the so-called “knock and
talk” exception to the warrant requirement, which permits law
enforcement officers to “‘encroach upon the curtilage of a
home for the purpose of asking questions of the occupants.’”
Perea-Rey, 680 F.3d at 1187 (quoting United States v.
Hammett, 236 F.3d 1054, 1059 (9th Cir. 2001)). The “knock
and talk” exception resembles to some degree the exception
for consensual searches. The relevant “consent” in a “knock
and talk” case is implied from the custom of treating the
“knocker on the front door” as an invitation (i.e., license) to
approach the home and knock. Jardines, 133 S. Ct. at 1415
(citation omitted). The scope of the exception is coterminous
12               UNITED STATES V. LUNDIN

with this implicit license. Stated otherwise, to qualify for the
exception, the government must demonstrate that the officers
conformed to “‘the habits of the country,’” id. (quoting
McKee v. Gratz, 260 U.S. 127, 136 (1922) (Holmes, J.)), by
doing “‘no more than any private citizen might do,’” id. at
1416 (quoting King, 563 U.S. at 469). In the typical case, if
the police do not have a warrant they may “approach the
home by the front path, knock promptly, wait briefly to be
received, and then (absent invitation to linger longer) leave.”
Id. at 1415. For two reasons, we agree with the district court
that the officers exceeded the scope of the customary license
to approach a home and knock.

    First, unexpected visitors are customarily expected to
knock on the front door of a home only during normal waking
hours. This does not mean that the “knock and talk”
exception never applies when officers knock on the door of
a home in the early morning. In some circumstances, an early
morning visit may be “consistent with an attempt to initiate
consensual contact with the occupants of the home.” Perea-
Rey, 680 F.3d at 1188. For example, officers may have
reason to believe that the resident in question generally
expects strangers on his porch early in the morning —
perhaps he sells fresh croissants out of his home. Or the
officers may have a reason for knocking that a resident would
ordinarily regard as important enough to warrant an early
morning disturbance — perhaps a fox has gotten into the
resident’s henhouse. Here, however, the officers knocked on
Lundin’s door around 4:00 a.m. without evidence that Lundin
generally accepted visitors at that hour, and without a reason
for knocking that a resident would ordinarily accept as
sufficiently weighty to justify the disturbance. Indeed, the
officers here acted for a purpose that virtually no resident
would willingly accept.
                 UNITED STATES V. LUNDIN                      13

    Second, the scope of a license is often limited to a specific
purpose, Jardines, 133 S. Ct. at 1416, and the customary
license to approach a home and knock is generally limited to
the “purpose of asking questions of the occupants,” Perea-
Rey, 680 F.3d at 1187 (citation omitted). Officers who knock
on the door of a home for other purposes generally exceed the
scope of the customary license and therefore do not qualify
for the “knock and talk” exception.

     “Reasonableness” under the Fourth Amendment “is
predominantly an objective inquiry.” Ashcroft v. al-Kidd,
563 U.S. 731, —, 131 S. Ct. 2074, 2080 (2011) (citation
omitted). A court’s task is usually to determine only
“whether the circumstances, viewed objectively, justify [the
challenged] action.” Id. (alteration in original) (citation
omitted). However, the Supreme Court has recognized
several “limited exception[s]” to this general rule, where
“actual motivations” matter. Id. (alteration in original)
(citation omitted). For example, police do not need a judicial
warrant or probable cause to conduct a search or seizure that
is justified by “special needs,” see, e.g., Vernonia Sch. Dist.
47J v. Acton, 515 U.S. 646, 665 (1995) (deterring drug use in
public schools), or to conduct an administrative inspection,
see, e.g., Michigan v. Clifford, 464 U.S. 287, 294 (1984)
(authorizing fire inspection).

    Before Jardines, it was not clear whether the proper
application of the “knock and talk” exception is an entirely
objective inquiry, or whether, as in special-needs-search and
administrative-inspection cases, the actual motivation of the
officers matters. The Court answered the question in
Jardines, explaining that the scope of the license to approach
a home and knock “is limited not only to a particular area but
also to a specific purpose.” 133 S. Ct. at 1416 (emphasis
14               UNITED STATES V. LUNDIN

added). That is, the application of the “knock and talk”
exception ultimately “depends upon whether the officers
ha[ve] an implied license to enter the [curtilage], which in
turn depends upon the purpose for which they enter[].” Id. at
1417 (emphasis added). After Jardines, it is clear that, like
the special-needs and administrative-inspection exceptions,
the “knock and talk” exception depends at least in part on an
officer’s subjective intent.

    The “knock and talk” exception to the warrant
requirement does not apply when officers encroach upon the
curtilage of a home with the intent to arrest the occupant.
Just as “the background social norms that invite a visitor to
the front door do not invite him there to conduct a search,” id.
at 1416, those norms also do not invite a visitor there to arrest
the occupant. We do not hold that an officer may never
conduct a “knock and talk” when he or she has probable
cause to arrest a resident but does not have an arrest warrant.
An officer does not violate the Fourth Amendment by
approaching a home at a reasonable hour and knocking on the
front door with the intent merely to ask the resident questions,
even if the officer has probable cause to arrest the resident.

    In this case, however, Deputy Aponte had asked dispatch
to broadcast a request that Lundin be arrested. The officers
who arrived at Lundin’s home were responding to that
request. Rather than obtain a warrant or wait for a time of
day when strangers might ordinarily visit, the officers
approached Lundin’s door at about 4:00 a.m. without a
warrant, immediately after they arrived at his home. Based
on this evidence, the district court found, as a matter of fact,
that the officers’ purpose in knocking on Lundin’s door was
to find and arrest him, and we see no reason to disturb that
finding. Thus, the officers violated Lundin’s Fourth
                 UNITED STATES V. LUNDIN                     15

Amendment right to be free from unlawful searches when
they stood on his porch and knocked on his front door. And
since this unconstitutional conduct caused the allegedly
exigent circumstance — the crashing noises in the backyard
— that circumstance cannot justify the search resulting in the
seizure of the two handguns.

     We note that our decision in United States v. Vaneaton,
49 F.3d 1423 (9th Cir. 1995), may be on infirm ground after
Jardines. In Vaneaton, officers had probable cause to arrest
the defendant for receiving stolen property and for violating
his parole, and they had reason to believe that he was staying
at the Rainbow Motel. Id. at 1425. The officers approached
the defendant’s motel room, knocked on the door, and
arrested him when he opened the door. Id. Our opinion did
not expressly note the officers’ purpose in knocking on the
defendant’s door, but it is fairly clear from our description of
the facts that they intended to arrest him. Although the
defendant was standing inside the doorway of his room, we
held that the officers lawfully arrested him because he
“‘voluntarily exposed himself to warrantless arrest’ by freely
opening the door of his motel room to the police.” Id. at 1426
(quoting United States v. Johnson, 626 F.2d 753, 757 (9th
Cir. 1980)).

    Unlike the officers in Jardines and in this case, the
officers in Vaneaton were standing in the common space of
a motel when they knocked, rather than in the curtilage of a
home. We therefore have no need to overrule Vaneaton. See
Miller v. Gammie, 335 F.3d 889, 899–900 (9th Cir. 2003) (en
banc) (holding that “a three-judge panel is free to reexamine
the holding of a prior panel” when the Supreme Court has
“undercut the theory or reasoning underlying the prior circuit
precedent in such a way that the cases are clearly
16               UNITED STATES V. LUNDIN

irreconcilable”). Whether Vaneaton remains good law after
Jardines is therefore a question for another case and another
day.

                    B. Protective Sweep

    The protective sweep doctrine authorizes “quick and
limited” warrantless inspections “of those spaces where a
person may be found” when “there are articulable facts
which, taken together with the rational inferences from those
facts, would warrant a reasonably prudent officer in believing
that the area to be swept harbor[ed] an individual posing a
danger to those on the arrest scene.” United States v. Lemus,
582 F.3d 958, 962 (9th Cir. 2009) (citation omitted)
(alteration in original). In this case, the officers had no
“reasonable, articulable suspicion” that anyone other than
Lundin was present at his residence. Maryland v. Buie,
494 U.S. 325, 336 (1990). Thus, the only plausible threat to
the safety of those on the scene was Lundin himself. By the
time the officers conducted the sweep of Lundin’s home,
however, he had already been handcuffed and placed in a
police vehicle. Thus, the officers lacked a reasonable ground
for believing that there was a danger that would have justified
the sweep of Lundin’s home.

                  C. Inevitable Discovery

     The inevitable discovery exception does not apply when
officers have probable cause to apply for a warrant but simply
fail to do so. See United States v. Mejia, 69 F.3d 309, 320
(9th Cir. 1995); United States v. Echegoyen, 799 F.2d 1271,
1280 n.7 (9th Cir. 1986). The government erroneously
suggests our decision in United States v. Merriweather,
777 F.2d 503 (9th Cir. 1985), holds to the contrary.
                 UNITED STATES V. LUNDIN                    17

    In Merriweather, federal agents performed a lawful
protective sweep of a motel room incident to an arrest.
During the sweep, an agent unlawfully searched the inside of
a toilet tank and found money hidden there. Id. at 505. The
police then obtained a search warrant for the motel room
without relying on the discovery of the money, and officers
who were unaware of the money executed the search warrant
and found it. Id. We held that the money was admissible. In
our opinion, we inaccurately characterized our decision as an
application of the “inevitable discovery doctrine.” Id. at 506.
Our decision in Merriweather is, instead, properly
characterized as an application of the independent source
doctrine. Unlike the inevitable discovery doctrine, which
asks whether evidence “would have” been discovered by
lawful means rather than by means of the illegal search, Nix
v. Williams, 467 U.S. 431, 447 (1984) (emphasis added), the
independent source doctrine asks whether the evidence
actually was “obtained independently from activities
untainted by the initial illegality.” Murray v. United States,
487 U.S. 533, 537 (1988).

    The two doctrines are, of course, related. See id. at 539
(“The inevitable discovery doctrine, with its distinct
requirements, is in reality an extrapolation from the
independent source doctrine.”). But the distinction between
the two doctrines is important because they create different
incentives. We do not apply the inevitable discovery doctrine
to warrantless searches where probable cause existed and a
warrant could therefore have been obtained because “[i]f
evidence were admitted notwithstanding the officers’
unexcused failure to obtain a warrant, simply because
probable cause existed, then there would never be any reason
for officers to seek a warrant.” Mejia, 69 F.3d at 320. Thus,
“to excuse the failure to obtain a warrant merely because the
18               UNITED STATES V. LUNDIN

officers had probable cause and could have inevitably
obtained a warrant would completely obviate the warrant
requirement of the fourth amendment.” United States v.
Young, 573 F.3d 711, 723 (9th Cir. 2009) (citation omitted).
Put differently, allowing the government to claim
admissibility under the inevitable discovery doctrine when
officers have probable cause to obtain a warrant but fail to do
so would encourage officers never to bother to obtain a
warrant.

    The independent source rule, by contrast, does not create
this incentive. As the Supreme Court has explained, a
rational officer who already has probable cause to obtain a
search warrant will ordinarily not enter the premises without
a warrant because “his action would add to the normal burden
of convincing a magistrate that there is probable cause the
much more onerous burden of convincing a trial court that no
information gained from the illegal entry affected either the
law enforcement officers’ decision to seek a warrant or the
magistrate’s decision to grant it.” Murray, 487 U.S. at 540.

    The officers here knew they had probable cause to arrest
Lundin. Deputy Aponte received corroborated information
from two witnesses that hours earlier Lundin had committed
numerous violent felonies. Aponte therefore requested
Lundin’s arrest under California Penal Code § 836.
However, the officers who arrived at Lundin’s home had no
right, absent an arrest warrant, to arrest Lundin in his home,
or, absent a search warrant, to search his home. Payton,
445 U.S. at 589–90. The officers nonetheless failed to obtain
any warrant before coming onto Lundin’s porch and knocking
on his door with the intention of arresting him. Thus, the
district court correctly held that the inevitable discovery
exception to the exclusionary rule does not apply. Indeed, it
                UNITED STATES V. LUNDIN                   19

would have erred had it held to the contrary. See Reilly,
224 F.3d at 995 (“[T]he district court committed clear error
in applying the inevitable discovery doctrine based on the
agents’ actual but unexercised opportunity to secure a search
warrant.”).

                        Conclusion

   For the foregoing reasons, we affirm the district court’s
grant of Lundin’s motion to suppress the two handguns seized
from Lundin’s home on April 23. We remand for further
proceedings.

   AFFIRMED.

```

---
