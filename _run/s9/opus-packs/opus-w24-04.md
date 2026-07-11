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

## GROUP: _overhaul2/lake/cases/united-states-v-davis--4881258.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e171de5cb7956a9f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-davis--4881258"}, "payload": {"all": [{"cite": "997 F.3d 191", "page": "191", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "997"}], "display": "997 F.3d 191", "official": {"cite": "997 F.3d 191", "page": "191", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "997"}, "official_selection_present": true, "record_id": "united-states-v-davis--4881258"}}
{"assertion_id": "4f4a4baa4292ba3b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-davis--4881258"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-davis--4881258", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-davis--4881258

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-davis--4881258",
  "stub": true,
  "status": "folded-alias",
  "identity": {
    "case_name": "United States v. Howard Davis",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Davis",
    "court": "4th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2021-05-07",
    "year": 2021,
    "docket": "19-4930",
    "cluster_id": 4881258,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": "/opinion/4881258/united-states-v-howard-davis/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "997 F.3d 191",
      "volume": "997",
      "reporter": "F.3d",
      "page": "191",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "997 F.3d 191",
        "volume": "997",
        "reporter": "F.3d",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "997 F.3d 191",
    "official_selection": {
      "court_class": "coa",
      "selected": "997 F.3d 191",
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
    "date_created": "2026-07-07T18:18:48Z",
    "date_modified": "2026-07-07T21:05:51Z",
    "warnings": [
      "folded-alias: subsumed into United States v. Howard Davis (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:18:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:18:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:18:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---

## GROUP: _overhaul2/lake/cases/united-states-v-di-re--104490.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4015fe74c449f333", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-di-re--104490"}, "payload": {"all": [{"cite": "332 U.S. 581", "page": "581", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "332"}, {"cite": "68 S. Ct. 222", "page": "222", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "68"}, {"cite": "92 L. Ed. 2d 210", "page": "210", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "1948 U.S. LEXIS 2667", "page": "2667", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1948"}], "display": null, "official": null, "official_selection_present": false, "record_id": "united-states-v-di-re--104490"}}
{"assertion_id": "ba4589bc8d23791f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-di-re--104490"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-di-re--104490", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-di-re--104490

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-di-re--104490",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Di Re",
    "case_name_short": "",
    "case_name_full": "UNITED STATES v. Di RE",
    "input_case_name": "United States v. Di Re",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1948-01-19",
    "year": 1948,
    "docket": null,
    "cluster_id": 104490,
    "lead_opinion_id": 104490,
    "sibling_ids": [],
    "absolute_url": "/opinion/104490/united-states-v-di-re/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "332 U.S. 581",
        "volume": "332",
        "reporter": "U.S.",
        "page": "581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 222",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 210",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1948 U.S. LEXIS 2667",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2667",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "332 U.S. 581",
        "volume": "332",
        "reporter": "U.S.",
        "page": "581",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 222",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 210",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1948 U.S. LEXIS 2667",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2667",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:51:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:51:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:51:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:51:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-di-re--104490

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b652-11">
  Me. Justice Jackson
 </author>
<p id="Acn">
  delivered the opinion of the Court.
 </p>
<p id="b652-12">
  Michael Di Re was convicted on a charge of knowingly possessing counterfeit gasoline ration coupons in violation of § 301 of the Second War Powers Act, 1942.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The decisive evidence was that obtained by search of his person, after he was arrested without a warrant of any kind. The Circuit Court of Appeals, Second Circuit, considered that any question as to the timeliness of his objection to this evidence was eliminated by its disposition on its merits by the District Court, and, one judge dissenting, it held both his search and arrest to have been illegal.
  <span citation-index="1" class="star-pagination" label="583"> 
   *583
   </span>
  The Government was granted certiorari,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  raising no question other than the correctness of the holding by the Court of Appeals that the evidence was the fruit of an illegal arrest and search.
 </p>
<p id="b653-5">
  An investigator for the Office of Price Administration was informed by one Reed that he was to buy counterfeit gasoline ration coupons from a certain Buttitta at a named place in the City of Buffalo, New York. The investigator and a detective from the Buffalo Police Department trailed Buttitta’s car and finally came upon it parked at the appointed place. They went to the car and found the informer Reed, the only occupant of the rear seat, holding in his hand two gasoline ration coupons which later proved to be counterfeit. Reed, on being asked, said he obtained them from Buttitta, who was sitting in the driver’s seat. Beside Buttitta sat Di Re. All three were taken into custody, “frisked” to make sure they had no weapons and were then taken to the police station. Here Di Re complied with a direction to put the contents of his pockets on a table. Two gasoline and several fuel oil ration coupons were laid out. He said he had found them in the street. About two hours later, after questioning, he was “booked” and thoroughly searched. One hundred inventory gasoline ration coupons were found in an envelope concealed between his shirt and underwear. These, as well as the gasoline coupons earlier disclosed, proved to be counterfeit. Their introduction as evidence, over the objection of the defendant, was held by the court below to require reversal of the conviction.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b653-6">
  I.
 </p>
<p id="b653-7">
  The Government now defends the search upon alternative grounds: 1, that search of Di Re was justified as
  <span citation-index="1" class="star-pagination" label="584"> 
   *584
   </span>
  incident to a lawful arrest; 2, that search of his person was justified as incident to search of a vehicle reasonably believed to be carrying contraband. We consider the second ground first.
 </p>
<p id="b654-5">
  The claim is that officers have the right, without a warrant, to search any car which they have reasonable cause to believe carries contraband, and incidentally may search any occupant of such car when the contraband sought is of a character that might be concealed on the person. This contention calls, first, for a determination as to whether the circumstances gave a right to search this car.
 </p>
<p id="b654-6">
  The belief that an automobile is more vulnerable to search without warrant than is other property has its source in the decision of
  <em>
   Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>. That search was made and its validity was upheld under the search and seizure provisions enacted for enforcement of the National Prohibition Act and of that Act alone. Transportation of liquor in violation of that Act subjected first the liquor, and then the vehicle in which it was found, to seizure and confiscation, and the person “in charge thereof” to arrest.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  The Court reviewed
  <span citation-index="1" class="star-pagination" label="585"> 
   *585
   </span>
  the legislative history of enforcement legislation and concluded (at p. 147), “The intent of Congress to make a distinction between the necessity for a search warrant in the searching of private dwellings and in that of automobiles and other road vehicles in
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  the enforcement of the Prohibition Act is thus clearly established by the legislative history of the Stanley Amendment. Is such a distinction consistent with the Fourth Amendment? We think that it is. The Fourth Amendment does not denounce all searches or seizures, but only such as are unreasonable.” The progeny of the
  <em>
   <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
  </em>
  case likewise dealt with searches and seizures under this Act.
  <em>
   Husty
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span>.
 </p>
<p id="b655-5">
  Obviously the Court should be reluctant to decide that a search thus authorized by Congress was unreasonable and that the Act was therefore unconstitutional. In view of the strong presumption of constitutionality due to an Act of Congress, especially when it turns on what is “reasonable,” the
  <em>
   <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
  </em>
  decision falls short of establishing a doctrine that, without such legislation, automobiles nonetheless are subject to search without warrant in enforcement of all federal statutes. This Court has never yet said so. The most that can be said is that some of the language by which the Court justified the search and seizure legislation in the
  <em>
   <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
  </em>
  case might be used to make a distinction between what is a reasonable search as applied to an automobile and as applied to a residence or fixed premises, even in absence of legislation.
 </p>
<p id="b655-6">
  We need not decide whether, without such Congressional authorization as was found controlling in the Car
  <span citation-index="1" class="star-pagination" label="586"> 
   *586
   </span>
<em>
   roll
  </em>
  case, any automobile is subject to search without warrant on reasonable cause to believe it contains contraband. In the case before us there appears to have been no search of the car itself. No one on the spot seems to have thought there was cause for searching it, or that it was subject to forfeiture. The nature of ration tickets, the contraband involved, was not such that a car would be necessary or advantageous in carrying them except as an incident of carrying the person. When the question of admissibility of this evidence arose in the trial court, counsel for the Government made no claim that there had been search or cause for search of the car. No question of fact concerning such a claim has been resolved by the trial court or the jury.
 </p>
<p id="b656-4">
  Assuming, however, without deciding, that there was reasonable cause for searching the car, did it confer an incidental right to search Di Re? It is admitted by the Government that there is no authority to that effect, either in the statute or in precedent decision of this Court, but we are asked to extend the assumed right of car search to include the person of occupants because “common sense demands that such right exist in a case such as this where the contraband sought is a small article which could easily be concealed on the person.”
 </p>
<p id="b656-5">
  This argument points up the different relation of the automobile to the crime in the
  <em>
   <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
  </em>
  case than in the one before us. An automobile, as was there pointed out, was an almost indispensable instrumentality in large-scale violation of the National Prohibition Act, and the car itself therefore was treated somewhat as an offender and became contraband. But even the National Prohibition Act did not direct the arrest of all occupants but only of the person in charge of the offending vehicle, though there is better reason to assume that no passenger in a car loaded with liquor would remain innocent of knowledge
  <span citation-index="1" class="star-pagination" label="587"> 
   *587
   </span>
  of the car's cargo than to assume that a passenger must know what pieces of paper are carried in the pockets of the driver.
 </p>
<p id="b657-5">
  The Government says it would not contend that, armed with a search warrant for a residence only, it could search all persons found in it. But an occupant of a house could be used to conceal this contraband on his person quite as readily as can an occupant of a car. Necessity, an argument advanced in support of this search, would seem as strong a reason for searching guests of a house for which a search warrant had issued as for search of guests in a car for which none had been issued. By a parity of reasoning with that on which the Government disclaims the right to search occupants of a house, we suppose the Government would not contend that if it had a valid search warrant for the car only it could search the occupants as an incident to its execution. How then could we say that the right to search a car without a warrant confers greater latitude to search occupants than a search by warrant would permit?
 </p>
<p id="b657-6">
  We see no ground for expanding the ruling in the
  <em>
   <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
  </em>
  case to justify this arrest and search as incident to the search of a car. We are not convinced that a person, by mere presence in a suspected car, loses immunities from search of his person to which he would otherwise be entitled.
 </p>
<p id="b657-7">
  II.
 </p>
<p id="b657-8">
  The other ground on which the Government defended the search of Di Re, and the only one on which it relied at the trial, is that the officers justifiably arrested him and that this conferred a right to search his person. If he was lawfully arrested, it is not questioned that the ensuing search was permissible. Hence we must examine the circumstances and the law of arrest.
 </p>
<p id="b658-4">
<span citation-index="1" class="star-pagination" label="588"> 
   *588
   </span>
  Some members of this Court rest their conclusion that the arrest was invalid on § 180 of the New York Code of Criminal Procedure which requires an officer making an arrest without a warrant to inform the suspect of the cause of arrest, except when it is made during commission of the crime or when in pursuit after an escape.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  This question was first raised from the Bench during argument in this Court. Di Re did not assert this ground of invalidity at the trial. Had he done so the Government might have met it with proof of circumstances which in themselves would show that Di Re had been effectively informed, even if the circumstances fell short of establishing the statutory exception. The proceedings below did not develop the facts concerning Di Re’s arrest in connection with this requirement. Inasmuch as the issue would lead to exploration of the law as to waiver when the defense was not raised in either court below, or indeed by the petition here, and as to applicability of the statute if, as the Government contends, lack of express declaration was unnecessary because circumstances supplied the required information, we do not undertake to determine on this record whether Di Re’s arrest satisfied this provision of the New York law.
 </p>
<p id="b658-5">
  The arrest was challenged in the courts below on the ground that it violated another provision of New York law which was considered to be controlling on the subject. The court below assumed that the arresting officer, a state officer, derived his authority to arrest Buttitta and Reed, although it was for a federal crime, from
  <span citation-index="1" class="star-pagination" label="589"> 
   *589
   </span>
  § 177 of the New York Code of Criminal Procedure, and also considered the legality of the arrest of Di Re .under paragraph 3 thereof.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  In this Court the Government originally argued that the arrest was authorized under both paragraphs 2 and 3 of the state law, but in a supplemental brief the Government withdraws the suggestion “that the arrest of respondent can be justified under subsection 2 of Section 177 of the New York Code of Criminal Procedure.” Instead, it now urges that “the validity of an arrest without a warrant for a federal crime is a matter of federal law to be determined by a uniform rule applicable in all federal courts.”
 </p>
<p id="b659-5">
  We believe, however, that in absence of an applicable federal statute the law of the state where an arrest without warrant takes place determines its validity. By one of the earliest acts of Congress, the principle of which is still retained, the arrest by judicial process for a federal offense must be “agreeably to the usual mode of process against offenders in such state.”
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  There is no reason to
  <span citation-index="1" class="star-pagination" label="590"> 
   *590
   </span>
  believe that state law is not an equally appropriate standard by which to test arrests without warrant, except in those cases where Congress has enacted a federal rule. Indeed the enactment of a federal rule in some specific cases seems to imply the absence of any general federal law of arrest.
 </p>
<p id="b660-5">
  Turning to the Acts of Congress to find a rule for arrest without warrant, we find none which controls such a case as we have here and none that purports to create a general rule on the subject. If we were to try to find or fashion a federal rule for arrest without warrant, it appears that the federal legislative materials are meager, inconsistent and inconclusive. Federal Bureau of Investigation officers are authorized only “to make arrests without warrant for felonies which have been committed and which are cognizable under the laws of the United States, in cases where the person making the arrest has reasonable grounds to believe that the person so arrested is guilty of such felony and where there is a likelihood of the person escaping before a warrant can be obtained for his arrest, but the person arrested shall be immediately taken before a committing officer.”
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  However, marshals and their deputies “shall have the power to make arrests without warrant for any offense against the laws of the United States committed in their presence or for any felony cognizable under the laws of the United States in cases where such felony has in fact been or is being committed and they have reasonable grounds to believe that the person to be arrested has committed or is committing it,”
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  and they are also given the same powers as sheriffs in the same state may have, by law, in executing the laws thereof.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b660-6">
  In denouncing unlawful search by federal officers as a misdemeanor, Congress provided that it should not
  <span citation-index="1" class="star-pagination" label="591"> 
   *591
   </span>
  apply to one “arresting or attempting to arrest any person committing or attempting to commit an offense in the presence of such officer, agent, or employee, or who has committed, or who is suspected on reasonable grounds of having committed, a felony.”
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Thus the legislative sources, while yielding some common provisions, also contain many inconsistencies. No act of Congress lays down a general federal rule for arrest without warrant for federal offenses. None purports to supersede state law. And none applies to this arrest which, while for a federal offense, was made by a state officer accompanied by federal officers who had no power of arrest. Therefore the New York statute provides the standard by which this arrest must stand or fall.
 </p>
<p id="b661-5">
  Since, under that law, any valid arrest of Di Re, if for a misdemeanor must be for one committed in the arresting officer’s presence, and if for a felony must be for one which the officer had reasonable grounds to believe the suspect had committed, we seek to learn for what offense this man was taken into custody. The arresting officer testified that he did not tell Di Re what he was being arrested for. After he was taken to the station he was “booked,” but the record does not show upon what charge. He was later indicted for the misdemeanor of knowingly possessing counterfeit gasoline ration coupons in violation of Ration Order No. 5 (c) of the Office of Price Administrator. But on appeal the Government suggested the arrest may be defended as one for a felony because probable grounds existed for believing him guilty of the felony of conspiracy under § 37 of the Criminal Code,
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  and in this Court for the first time it suggests that there were grounds for arrest on a charge of possessing a known counterfeit writing with intent to utter it as true for the
  <span citation-index="1" class="star-pagination" label="592"> 
   *592
   </span>
  purpose of defrauding the United States, a felony under § 28 of the Criminal Code.
  <a class="footnote" href="#fn14" id="fn14_ref">
   14
  </a>
</p>
<p id="b662-5">
  Assuming, without deciding, that an arrest without a warrant on a charge not communicated at the time may later be justified if the arresting officer’s knowledge gave probable grounds to believe any felony found in the statute books had been committed, we are brought to the inquiry whether the circumstances at that time afforded such grounds.
 </p>
<p id="b662-6">
  The Government now concedes that the only person who committed a possible misdemeanor in the open presence of the officer was Reed, the Government informer who was found visibly possessing the coupons. Of course, as to Buttitta they had previous information that he was to sell such coupons to Reed, and Reed gave information that he had done so. But the officer had no such information as to Di Re. All they had was his presence, and if his presence was not enough to make a case for arrest for a misdemeanor, it is hard to see how it was enough for the felony of violating § 28 of the Criminal Code.
 </p>
<p id="b662-7">
  The relevant difference between Ration Order 5 (c) and § 28 of the Criminal Code is that the former declares mere possession of a counterfeit coupon an offense, while the latter defines a felony which consists not merely of possession but also of knowledge of the instrument’s counterfeit character, and also of intent to utter it as true. It is admitted that at the time of the arrest the officers had no information implicating Di Re and no information pointing to possession of any coupons, unless his presence in the car warranted that inference. Of course they had no information hinting further at the knowledge and intent required as elements of the felony under the statute.
 </p>
<p id="b663-4">
<span citation-index="1" class="star-pagination" label="593"> 
   *593
   </span>
  III.
 </p>
<p id="b663-5">
  The Government’s defense of the arrest relies most heavily on the conspiracy ground. In view of Reed’s character as an informer, it is questionable whether a conspiracy is shown. But if the presence of Di Re in the car did not authorize an inference of participation in the Buttitta-Reed sale, it fails to support the inference of any felony at all.
 </p>
<p id="b663-6">
  There is no evidence that it is a fact or that the officers had any information indicating that Di Re was in the car when Reed obtained ration coupons from Buttitta, and none that he heard or took part in any conversation on the subject. Reed, the informer, certainly knew it if any part of his transaction was in Di Re’s presence. But he was not called as a witness by the Government, nor shown to be unavailable, and we must assume that his testimony would not have been helpful in bringing guilty knowledge home to Di Re.
 </p>
<p id="b663-7">
  An inference of participation in conspiracy does not seem to be sustained by the facts peculiar to this case. The argument that one who “accompanies a criminal to a crime rendezvous” cannot be assumed to be a bystander, forceful enough in some circumstances, is farfetched when the meeting is not secretive or in a suspicious hide-out but in broad daylight, in plain sight of passers-by, in a public street of a large city, and where the alleged substantive crime is one which does not necessarily involve any act visibly criminal. If Di Re had witnessed the passing of papers from hand to hand, it would not follow that he knew they were ration coupons, and if he saw that they were ration coupons, it would not follow that he would know them to be counterfeit. Indeed it appeared at the trial to require an expert to establish that fact. Presumptions of guilt are not lightly to be indulged from mere meetings.
 </p>
<p id="b664-4">
<span citation-index="1" class="star-pagination" label="594"> 
   *594
   </span>
  Moreover, whatever suspicion might result from Di Re’s mere presence seems diminished, if not destroyed, when Reed, present as the informer, pointed out Buttitta, and Buttitta only, as a guilty party. No reason appears to doubt that Reed willingly would involve Di Re if the nature of the transaction permitted. Yet he did not incriminate Di Re. Any inference that everyone on the scene of a crime is a party to it must disappear if the Government informer singles out the guilty person.
 </p>
<p id="b664-5">
  IV.
 </p>
<p id="b664-6">
  The Government also makes, and several times repeats, an argument to the effect that the officers could infer probable cause from the fact that Di Re did not protest his arrest, did not at once assert his innocence, and silently accepted the command to go along to the police station. One has an undoubted right to resist an unlawful arrest, and courts will uphold the right of resistance in proper cases. But courts will hardly penalize failure to display a spirit of resistance or to hold futile debates on legal issues in the public highway with an officer of the law. A layman may not find it expedient to hazard resistance on his own judgment of the law at a time when he cannot know what information, correct or incorrect, the officers may be acting upon. It is likely to end in fruitless and unseemly controversy in a public street, if not in an additional charge of resisting an officer. If the officers believed they had probable cause for his arrest on a felony charge, it is not to be supposed that they would have been dissuaded by his profession of innocence.
 </p>
<p id="b664-7">
  It is the right of one placed under arrest to submit to custody and to reserve his defenses for the neutral tribunals erected by the law for the purpose of judging his case. An inference of probable cause from a failure to engage in discussion of the merits of the charge with arresting
  <span citation-index="1" class="star-pagination" label="595"> 
   *595
   </span>
  officers is unwarranted. Probable cause cannot be found from submissiveness, and the presumption of innocence is not lost or impaired by neglect to argue with a policeman. It is the officer’s responsibility to know what he is arresting for, and why, and one in the unhappy plight of being taken into custody is not required to test the legality of the arrest before the officer who is making it.
 </p>
<p id="b665-4">
  The Government’s last resort in support of the arrest is to reason from the fruits of the search to the conclusion that the officer’s knowledge at the time gave them grounds for it. We have had frequent occasion to point out that a search is not to be made legal by what it turns up.
  <a class="footnote" href="#fn15" id="fn15_ref">
   15
  </a>
  In law it is good or bad when it starts and does not change character from its success.
 </p>
<p id="b665-5">
  V.
 </p>
<p id="b665-6">
  We meet in this case, as in many, the appeal to necessity. It is said that if such arrests and searches cannot be made, law enforcement will be more difficult and uncertain. But the forefathers, after consulting the lessons of history, designed our Constitution to place obstacles in the way of a too permeating police surveillance, which they seemed to think was a greater danger to a free people than the escape of some criminals from punishment. Taking the law as it has been given to us, this arrest and search were beyond the lawful authority of those who executed them. The conviction based on evidence so obtained cannot stand.
 </p>
<p id="b665-7">
<em>
   Affirmed.
  </em>
</p>
<judges id="b665-8">
  The Chief Justice and Mr. Justice Black dissent.
 </judges>















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b652-13">
   50 U. S. C. App. (Supp. V, 1946), § 633.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b653-8">
   331U. S. 800.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b653-9">
   <span class="citation" data-id="9653316"><a href="/opinion/1565918/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">159 F. 2d 818</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b654-7">
   Section 26, Title II of the National Prohibition Act provided in part as follows: “When . . . any officer of the law shall discover any person in the act of transporting in violation of the law, intoxicating liquors in any wagon, buggy, automobile, water or air craft, or other vehicle, it shall be his duty to seize any and all intoxicating liquors found therein being transported contrary to law. Whenever intoxicating liquors transported or possessed illegally shall be seized by an officer he shall take possession of the vehicle and team or automobile, boat, air or water craft, or any other conveyance, and shall arrest any person in charge thereof. . . .” In the
   <em>
    <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>
   </em>
   case it was said (<span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#155" aria-description="Citation for case: Carroll v. United States">267 U. S. at 155</a></span>) that this section was intended “to reach and destroy the forbidden liquor in transportation and the provisions for forfeiture of the vehicle and the arrest of the transporter were incidental”; and (<span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. at 158</a></span>) “the right to search and the validity of the seizure are not dependent on the right to arrest. They are
   <span citation-index="1" class="star-pagination" label="585"> 
    *585
    </span>
   dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law. The seizure in such a proceeding comes before the arrest as Section 26 indicates . . . .”
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b655-11">
   This word “in” is erroneously printed “is” in the case as reported.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b658-6">
   Section 180 provides:
  </p>
<p id="b658-7">
   “When arresting a person without a warrant the officer must inform him of the authority of the officer and the cause of the arrest, except when the person arrested is in the actual commission of a crime, or is pursued immediately after an escape.”
  </p>
<p id="b658-8">
   See also
   <em>
    People
   </em>
   v.
   <em>
    Marendi,
   </em>
   <span class="citation" data-id="3600752"><a href="/opinion/3618293/people-v-marendi/#610" aria-description="Citation for case: People v. . Marendi">213 N. Y. 600, 610</a></span>, <span class="citation" data-id="3600752"><a href="/opinion/3618293/people-v-marendi/#1061" aria-description="Citation for case: People v. . Marendi">107 N. E. 1058, 1061</a></span>. Cf.
   <em>
    John Bad Elk
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529</a></span>;
   <em>
    Christie
   </em>
   v.
   <em>
    Leachinsky,
   </em>
   [1947] 1 All Eng. 567.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b659-6">
   Section 177 of the New York Code of Criminal Procedure provides :
  </p>
<p id="b659-7">
   “A peace officer may, without a warrant, arrest a person,
  </p>
<p id="b659-8">
   “1. For a crime, committed or attempted in his presence;
  </p>
<p id="b659-9">
<em>
    “2.
   </em>
   When the person arrested has committed a felony, although not in his presence;
  </p>
<p id="b659-10">
   “3. When a felony has in fact been committed, and he has reasonable cause for believing the person to be arrested to have committed it.”
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b659-11">
   The Act of September 24, 1789 (Ch. 20, §33, <span class="citation no-link">1 Stat. 91</span>), concerning arrest with warrant, provided: “That for any crime or offence against the United States, the offender may, by any justice or judge of the United States, or by any justice of the peace, or other magistrate of any of the United States where he may be found agreeably to the usual mode of process against offenders in such state, and at the expense of the United States, be arrested, and imprisoned or bailed, as the case may be, for trial before such court of the United States as by this act has cognizance of the offence.” This provision has remained substantially similar to this day. <span class="citation no-link">18 U. S. C. § 591</span>. See also 1 Ops. Atty. Gen. 85, 86.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b660-7">
   <span class="citation no-link">48 Stat. 1008</span>, <span class="citation no-link">49 Stat. 77</span>, <span class="citation no-link">5 U. S. C. § 300</span> (a).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b660-8">
   <span class="citation no-link">49 Stat. 378</span>, <span class="citation no-link">28 U. S. C. § 504</span> (a).
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b660-9">
   <span class="citation no-link">1 Stat. 425</span>, <span class="citation no-link">12 Stat. 282</span>, <span class="citation no-link">28 U. S. C. § 504</span>.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b661-6">
   <span class="citation no-link">49 Stat. 877</span>, <span class="citation no-link">18 U. S. C. § 53</span> (a).
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b661-7">
   <span class="citation no-link">18 U. S. C. § 88</span>.
  </p>
</div><div class="footnote" id="fn14" label="14">
<a class="footnote" href="#fn14_ref">
   14
  </a>
<p id="b662-8">
   U. S. C. § 72.
  </p>
</div><div class="footnote" id="fn15" label="15">
<a class="footnote" href="#fn15_ref">
   15
  </a>
<p id="b665-9">
   See, for example,
   <em>
    Byars
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-eatherton--328838.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5a1c5d4fac71e136", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-eatherton--328838"}, "payload": {"all": [{"cite": "519 F.2d 603", "page": "603", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "519"}, {"cite": "89 L.R.R.M. (BNA) 2976", "page": "2976", "reporter": "L.R.R.M. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "89"}, {"cite": "1975 U.S. App. LEXIS 13604", "page": "13604", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1975"}], "display": "519 F.2d 603", "official": {"cite": "519 F.2d 603", "page": "603", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "519"}, "official_selection_present": true, "record_id": "united-states-v-eatherton--328838"}}
{"assertion_id": "581224e2363ec3f2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-eatherton--328838"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-eatherton--328838", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-eatherton--328838

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-eatherton--328838",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Gilbert Joseph Eatherton",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Appellee, v. Gilbert Joseph EATHERTON, Defendant-Appellant",
    "input_case_name": "United States v. Eatherton",
    "court": "U.S. Court of Appeals, 1st Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca1",
    "state": null,
    "date_decided": null,
    "year": 1975,
    "docket": null,
    "cluster_id": 328838,
    "lead_opinion_id": 328838,
    "sibling_ids": [],
    "absolute_url": "/opinion/328838/united-states-v-gilbert-joseph-eatherton/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "519 F.2d 603",
      "volume": "519",
      "reporter": "F.2d",
      "page": "603",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 L.R.R.M. (BNA) 2976",
        "volume": "89",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2976",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. App. LEXIS 13604",
        "volume": "1975",
        "reporter": "U.S. App. LEXIS",
        "page": "13604",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "519 F.2d 603",
        "volume": "519",
        "reporter": "F.2d",
        "page": "603",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L.R.R.M. (BNA) 2976",
        "volume": "89",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2976",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. App. LEXIS 13604",
        "volume": "1975",
        "reporter": "U.S. App. LEXIS",
        "page": "13604",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "519 F.2d 603",
    "official_selection": {
      "court_class": "coa",
      "selected": "519 F.2d 603",
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
    "date_created": "2026-07-06T13:13:43Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:13:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:13:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:13:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-eatherton--328838

```
<?xml version="1.0" encoding="utf-8"?>
<opinion data-order="10" data-type="opinion" id="x999-1" type="majority">
<author id="b669-9">
  LEVIN H. CAMPBELL, Circuit Judge.
 </author>
<p id="b669-10">
  At approximately 1:00 p. m. on March 25, 1974, three men entered the Suburban National Bank in Arlington, Massachusetts. The men were armed, and were similarly dressed. Each was wearing a dark (described by witnesses as black or navy blue) knit ski mask which effectively obscured his facial features. In the space of a few minutes they had robbed the bank of $10,443.81, and exited from the bank. An assistant cashier testified to seeing the men fleeing in the direction of Churchill Avenue.
 </p>
<p id="b669-11">
  Another prosecution witness testified that at approximately this same time he was driving his car up Churchill Avenue when he observed a “silver” automobile suddenly emerge from a driveway behind the bank, make an abrupt turn into the avenue, run the corner stop sign, and then disappear down Churchill Avenue traveling at a high rate of speed. A car fitting this description, subsequently ascertained to have been stolen, was discovered soon after the robbery parked on a residential street approximately four blocks from the bank.
 </p>
<p id="b669-12">
  The robbers departed the area of the crime without being apprehended. No clues were found at the scene or in the abandoned car, and because of the masks worn in the bank the eyewitnesses to the robbery were of no help in identifying the perpetrators of the crime. Police located two witnesses who were outside the bank around the time of the robbery and had seen three men who were probably the robbers. These witnesses gave the law enforcement officials information leading them to conclude that appellant, Gilbert Joseph Eatherton, was one of those men. He was subsequently arrested and on April 4, 1974, was indicted by a grand jury for the armed robbery of the Suburban National Bank in violation of <span class="citation no-link">18 U.S.C. §§ 2113</span>(a) &amp; (d).
 </p>
<p id="b669-14">
  Identity was the principal issue at Ea-therton’s jury trial. He offered several alibi witnesses in an attempt to show that he could not have been in Arlington at the time of the robbery. Some doubt was cast upon their testimony, however, by cross-examination and by two rebuttal witnesses presented by the Government. The jury evidently chose to disbelieve appellant’s alibi. Upon its verdict of guilty a judgment of conviction was entered, and he was sentenced to 18 years’ imprisonment. In this appeal he presents four claims: that his identification was the result of impermissible police suggestion, that physical evidence introduced by the prosecution was the fruit of an unreasonable search, that the trial court abused its discretion in admitting this evidence even if it was not unconstitutionally obtained, and that the court’s charge to the jury was improper.
 </p>
<p id="b669-15">
  I
 </p>
<p id="b669-16">
  Inquiry by the Arlington Police and the Federal Bureau of Investigation (FBI) at the house before which the silver vehicle was discovered led to Miss Janet Leak, a high school senior, who was the principal eye witness at appellant’s trial. The officers learned that Miss Leak had observed the three men who had been in the silver gray automobile. She told the officers that while walking down Churchill Avenue at about 1:00 p. m. she had seen the large silver car traveling unusually fast and followed by a small green car. When she began walking down Lincoln street towards her home she observed that these two vehicles were parked in front of her house. As she approached her home the three occupants of these cars got out and then
  <span citation-index="1" class="star-pagination" label="606"> 
   *606
   </span>
  all three entered the silver auto. Leak passed within several feet of these three individuals and testified that she had them in her view for about a minute. She also stated that she had obtained a better view of the individual in the front passenger seat than of the two others.
 </p>
<p id="b670-4">
  At their request Leak accompanied two FBI agents to the bank to see if she could aid them in identifying the men. In the bank, approximately an hour after the robbery, Miss Leak was shown a green album containing a number of photographs of adult males. The album, which had been prepared by the FBI, bore on its front cover the small, taped-on legend, “Bank Robbery Suspect Photographs.”
 </p>
<p id="b670-5">
  Leak was asked to look through this album to determine if any of the pictures looked familiar or if she could identify any of the three men she had observed. On her first time through this book she indicated two to four “possibilities” to the agents but made no positive identification of any photograph. One of the photos which she indicated was a possibility, identified only as number 14 in the album, was that of appellant.
 </p>
<p id="b670-6">
  Two of the FBI agents then discussed the “possibles” which Leak had indicated. One of these agents, who was evidently familiar with many of the men whose photographs appeared in the album, “eliminated” all the possibles save appellant. This conversation was held approximately six feet from where Leak was sitting with another agent and an Arlington police officer, but, according to the testimony of one of the conver-sants, was conducted sufficiently
  <em>
   sotto voce
  </em>
  to prevent Leak from overhearing.
 </p>
<p id="b670-7">
  The agents requested that Leak again go through the photo album in an attempt to obtain a “suspect.” On this last time through Leak selected only one picture — appellant’s.
 </p>
<p id="b670-9">
  On the afternoon of the robbery a young man, Michael Gookin, and his companion were walking down Churchill Avenue alongside the Suburban National Bank. Bookin’s attention was attracted by three men approaching the bank wearing navy blue ski hats, and he also observed a vehicle left running in a driveway nearby. He passed within about seven yards of the men, and although their somewhat unusual headgear for such a warm day had stimulated his attention, he did not take a close look at any of them.
 </p>
<p id="b670-10">
  Later in the day Gookin learned some of the facts surrounding the robbery of the bank and contacted the Arlington Police in the belief that his observations might be of some help in solving the crime. That evening he and his companion were taken to the Massachusetts Bureau of Identification by Arlington police officers. His companion proved of no assistance in identifying the men, apparently because she had only barely observed them as they passed. Gookin, however, was able to give a general description of two of the men and had sufficient recollection of one to be able to assemble an ident-a-kit facial composite of that individual with the assistance of an officer from the Bureau of Identification.
 </p>
<p id="b670-11">
  Gookin was then requested to look through several drawers of photographs corresponding roughly to the description he had given. At some point after Goo-kin had looked through a substantial number of these photos
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  the Arlington police officers present learned that appellant — presumably on the basis of Leak’s earlier identification — had become a suspect in the crime. They obtained a color photograph from Bureau files and showed it to Gookin, inquiring whether he thought it looked like one of the men he had seen. Gookin replied that he thought it did, but that he wasn’t sure.
 </p>
<p id="b671-4">
<span citation-index="1" class="star-pagination" label="607"> 
   *607
   </span>
  Gookin was then shown a spread of seven to eight photos which included a black and white copy of the portrait of appellant he had just been asked about. He noted that fact to the officers. After he had completed his examination of this spread he was told that earlier in the day another witness had identified the individual in that photo. While he later indicated that this information had reassured him, he held to the opinion that he would have to see the man in person before he could make any positive identification.
 </p>
<p id="b671-5">
  The next day, March 26, both Leak and Gookin were exposed to further investigatory attempts to identify the men they had seen in the vicinity of the bank. They were separately brought to the Boston Municipal Court, Leak by Arlington police officers and Gookin by FBI agents, in the expectation that appellant would be there in regard to another matter. The law enforcement officials apparently intended to arrange some sort of opportunity for them to observe appellant in person, but when they reached the courthouse Eatherton had departed. At some point Leak and Gookin were alone together in a corridor for a short time, and, according to Gookin’s testimony at trial, “probably” discussed their respective attempted identifications of the men they had seen.
 </p>
<p id="b671-6">
  Surrounding this failed attempt to effect some sort of confrontation with appellant, both witnesses were again shown photo displays and asked whether they could identify anyone. On the way to the BMC Leak was shown the composite, prepared by Gookin the previous evening, as well as a seven photo spread which contained a copy of the same photo of appellant which she had seen in the green FBI album the previous day. Leak again selected this photo as one of the men she had seen.
 </p>
<p id="b671-10">
  Gookin, after the BMC visit, was taken to FBI headquarters where he was shown a spread of eight photographs. The results of that attempt at identification are not clear,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  but the jury was told only that Gookin had again been unable to identify anyone. He was also shown the green album, without result.
 </p>
<p id="b671-11">
  In the course of the continuing investigation of the robbery both Gookin and Leak were shown photographic spreads on several other occasions. On March 28, Leak was shown the same seven photo spread which had been displayed to her two days before, and she again selected appellant’s picture. On March 81, she was presented a nine picture spread, but she again identified only the photo of Eatherton, which she had by that time seen at least three to five times. On April 3, prior to appearing before the grand jury, Leak was shown an entirely new spread of eight photographs by the Assistant United States Attorney. She failed to select a picture of appellant included in that group. Before the grand jury she was again shown the green album and repeated her selection of photo number 14 — Gilbert Eatherton. She may also have been shown the album on one occasion several months after her grand jury appearance, but this is not clear from the testimony. In any event, she saw no photographs in any form for at least two months prior to the trial.
 </p>
<p id="b671-12">
  Gookin was shown a photo
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  of Eather-ton on March 28 by the Arlington police, who asked whether it was of the man he had seen. He indicated his belief that it was. Gookin also apparently was shown
  <span citation-index="1" class="star-pagination" label="608"> 
   *608
   </span>
  the green photo album and some photo spreads containing appellant’s picture on several other occasions, but his testimony at the voir dire was very confused on these points. It can be generalized that on some occasions he selected appellant’s picture from such displays, and that he was sometimes told that others had formed the opinion that appellant was one of the robbers. It does not affirmatively appear that Gookin ever positively identified appellant’s photo as the image of one of the men he had seen near the bank — as opposed to merely selecting the same photo he had previously been shown on numerous occasions.
 </p>
<p id="b672-4">
  At the trial Leak positively identified appellant as one of the three men she had seen on the day of the robbery. Gookin, however, when called to the stand did not make a positive identification. When asked to look around the courtroom to see if there was anyone he could point to as having been near the bank on March 25, he stated that he could not: “Some are very similar, but I am not certain.” When pressed he pointed to appellant as someone who ap-: peared “very similar” to one of the men he had seen.
 </p>
<p id="b672-5">
  Appellant argues that the admission of the Leak and Gookin testimony was error. He contends that the identification procedures used prior to the trial were “so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification.”
  <em>
   Simmons v. United States,
  </em>
  <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U.S. 377, 384</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#971" aria-description="Citation for case: Simmons v. United States">88 S.Ct. 967, 971</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L.Ed.2d 1247</a></span> (1968). After an extensive voir dire hearing on appellant’s motion to suppress the anticipated in-eourt identifications on the basis of
  <em>
   <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,
  </em>
  the district court denied the motion as to both witnesses. Correctly adopting the “totality of the circumstances” standard for reviewing this claim, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U.S. at 383</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#970" aria-description="Citation for case: Simmons v. United States">88 S.Ct. at 970</a></span>;
  <em>
   see Stovall v. Denno,
  </em>
  <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U.S. 293</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S.Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L.Ed.2d 1199</a></span> (1967), the court concluded that the photographic identification procedures had not exceeded the
  <em>
   <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>
  </em>
  limitation. We think this ruling was not erroneous.
 </p>
<p id="b672-8">
  As to the witness Leak, the district court found — based primarily upon her own testimony — that she had received “no suggestion whatsoever when she looked through the FBI album,” and that her initial selection of appellant’s picture from the album had been an independent decision made without difficulty on her part. As these findings are supported in the record, they effectively dispose of the claim that Leak’s initial selection of appellant’s photo as that of one of the men she had seen near the bank was the product of impermissible suggestion. More troublesome, however, are her repeated exposures to photo displays containing the same picture she had previously identified. While there may have been sound investigatory reasons for some of these,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  the practice is obviously subject to abuse. If the witness’ initial selection of a photograph is somewhat equivocal or may have been influenced by suggestive procedures — albeit not ones of a magnitude which, standing alone, would require the suppression of an in-court identification— subsequent repetitive exercises which do little more than test the witness’ ability to again select that photograph are likely to have the effect of fixing that image in the witness’ mind with a corresponding blurring of the image actually perceived at the crime.
  <em>
   Cf. United States v. Workman,
  </em>
  <span class="citation" data-id="306992"><a href="/opinion/306992/united-states-v-pearlie-donald-workman/#153" aria-description="Citation for case: United States v. Pearlie Donald Workman">470 F.2d 151, 153</a></span> (4th Cir. 1972);
  <em>
   Kimbrough v. Cox,
  </em>
  <span class="citation" data-id="297282"><a href="/opinion/297282/willie-kimbrough-v-j-d-cox-superintendent-virginia-state-penitentiary/#10" aria-description="Citation for case: Willie Kimbrough v. J. D. Cox, Superintendent Virginia...">444 F.2d 8, 10-11</a></span> (4th Cir. 1971).
 </p>
<p id="b672-9">
  The district court made no specific finding on the effect of these procedures
  <span citation-index="1" class="star-pagination" label="609"> 
   *609
   </span>
  upon Leak’s ability to identify Eatherton. But in view of its findings on the independence and strength of her initial selection, we conclude that the repeated display of appellant’s photo did not impermissibly prejudice him. Leak had received a good opportunity to see one of the men, at close range and in good light, only a few hours before viewing the album,
  <em>
   cf. Neil v. Biggers,
  </em>
  <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188, 199-200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S.Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L.Ed.2d 401</a></span> (1972);
  <em>
   Allen v. Moore,
  </em>
  <span class="citation" data-id="300900"><a href="/opinion/300900/fred-b-allen-v-robert-moore-superintendent-etc-richard-w-balukonis/#974" aria-description="Citation for case: Fred B. Allen v. Robert Moore, Superintendent, Etc.,...">453 F.2d 970, 974</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./406/969/">406 U.S. 969</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./92/2422/">92 S.Ct. 2422</a></span>, <span class="citation no-link">32 L.Ed.2d 668</span> (1972), and had concluded that appellant’s photo was that of this man. There is no evidence that her subsequent reselections of this photo were other than cumulative reassertions of the original decision. We do not believe that they presented the “very substantial likelihood of irreparable misidentification” requiring suppression of Leak’s identification.
  <em>
   See United States v. DeLeo,
  </em>
  <span class="citation" data-id="288700"><a href="/opinion/288700/united-states-v-ralph-f-deleo/#497" aria-description="Citation for case: United States v. Ralph F. Deleo">422 F.2d 487, 497</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./397/1037/">397 U.S. 1037</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./90/1355/">90 S.Ct. 1355</a></span>, <span class="citation no-link">25 L.Ed.2d 648</span> (1970).
 </p>
<p id="b673-5">
  The totality of the circumstances regarding Gookin, as the district court recognized, present an aggregate which is closer to the line. In Gookin’s case the danger of supplanting his recollection with the image in the photograph was real.
  <em>
   Cf. Foster v. California,
  </em>
  <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U.S. 440</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">89 S.Ct. 1127</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">22 L.Ed.2d 402</a></span> (1969). However, Gookin never succumbed to the temptation to overstate his memory of the man he saw. He adhered to the position that he could not be sure that appellant was one of the men, and at the trial he identified Eatherton only as similar to that man. We see no realistic possibility that irreparable misidentification could. have been the result of the questionable procedures followed, the qualified nature of the identification itself providing a persuasive indication that the police conduct was without significant effect.
 </p>
<p id="b673-11">
  II
 </p>
<p id="b673-12">
  On the morning of March 27, two FBI agents were waiting in the vicinity of an address in Everett, Massachusetts, where they believed appellant might be. They were aware that an application was being made to obtain a warrant for Eath-erton’s arrest, and their orders were to locate him, presumably so that the warrant when obtained could be expeditiously effected. While they were waiting, however, they received information that Eatherton was in the vicinity but that he appeared to be fleeing or in preparation for flight. The agents quickly located him a few blocks away and decided to arrest him. Appellant does not dispute that the agents possessed probable cause to arrest.
 </p>
<p id="b673-13">
  The agents saw Eatherton on the street and called for him to come over to their car. He did so, carrying a briefcase which was in his hand when they first observed him. When he came close to the vehicle the agents told him he was under arrest, instructed him to drop the briefcase and spread eagle on the ■ ground. Eatherton complied, and the agents thoroughly frisked him, then handcuffed him behind his back and placed him in the car. The agents then picked up the briefcase and opened it. Inside they found, among other items, a loaded .38 caliber revolver and three brown ski masks. They inventoried and marked for identification all the contents of the briefcase, which were subsequently admitted into evidence over appellant’s objection.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b673-14">
  Appellant argues that opening and examining the briefcase was an unreasonable search under the fourth
  <span citation-index="1" class="star-pagination" label="610"> 
   *610
   </span>
  amendment and that the fruits of that search, the contents of the briefcase, should have been suppressed. As noted earlier, he does not dispute that there was probable cause to arrest, and he concedes that the agents could have seized the briefcase consonant with the fourth amendment. Indeed, he argues that they should have done so. But, in his view, after obtaining custody of the case, the agents then should have obtained a search warrant before investigating its contents. He stresses that any urgency to inspect the interior of the briefcase was completely removed once he had been subdued and the case removed from his possession and beyond his possible reach. From this he argues that we should strike a balance which maximizes protection of his asserted expectation of privacy in the briefcase and require that judicial permission be sought before it can be opened.
 </p>
<p id="b674-4">
  Appellant’s approach to balancing fourth amendment values is not without some logical cogency.
  <em>
   See United States v. Soriano,
  </em>
  <span class="citation" data-id="9459698"><a href="/opinion/312707/united-states-v-rafael-soriano/" aria-description="Citation for case: United States v. Rafael Soriano">482 F.2d 469</a></span> (5th Cir. 1973);
  <em>
   Braceo v. Reed,
  </em>
  17 Crim.L.Rep. 2198 (D.Ore. May 13, 1975). However, we think the rule he seeks is without support in the cases. The strongest Supreme Court decision for the position espoused by appellant would seem to be
  <em>
   Chimel v. California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U.S. 752</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969). Yet that opinion cited, with apparent approval,
  <em>
   Draper v. United States,
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U.S. 307</a></span>, <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">79 S.Ct. 329</a></span>, <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">3 L.Ed.2d 327</a></span> (1959), in which a search virtually identical to that at issue here was upheld. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U.S. at 760</a></span> n. 4, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>. Several court of appeals decisions applying
  <em>
   Chimel
  </em>
  had little apparent difficulty upholding searches identical to that contested here.
  <em>
   United States v. Maynard,
  </em>
  <span class="citation" data-id="295485"><a href="/opinion/295485/united-states-v-bob-maynard/" aria-description="Citation for case: United States v. Bob Maynard">439 F.2d 1086</a></span> (9th Cir. 1971);
  <em>
   United States v. Mehciz,
  </em>
  <span class="citation" data-id="9456437"><a href="/opinion/294420/united-states-v-jesse-vance-mehciz/" aria-description="Citation for case: United States v. Jesse Vance Mehciz">437 F.2d 145</a></span> (9th Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./402/974/">402 U.S. 974</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./91/1663/">91 S.Ct. 1663</a></span>, <span class="citation" data-id="8975722"><a href="/opinion/8983775/atlantic-coast-line-railroad-v-united-states/" aria-description="Citation for case: Atlantic Coast Line Railroad v. United States">29 L.Ed.2d 139</a></span> (1971);
  <em>
   United States ex rel. Muhammad v. Mancusi,
  </em>
  <span class="citation" data-id="8883856"><a href="/opinion/8897234/united-states-ex-rel-muhammad-v-mancusi/" aria-description="Citation for case: United States ex rel. Muhammad v. Mancusi">432 F.2d 1046</a></span> (2d Cir. 1970),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./402/911/">402 U.S. 911</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./91/1391/">91 S.Ct. 1391</a></span>, <span class="citation no-link">28 L.Ed.2d 653</span> (1971). And in light of the Court’s most recent pronouncements on the fourth amendment,
  <em>
   United States v. Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U.S. 218</a></span>, <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">94 S.Ct. 467</a></span>, <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">38 L.Ed.2d 427</a></span> (1973);
  <em>
   Gustafson v. Florida,
  </em>
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/" aria-description="Citation for case: Gustafson v. Florida">414 U.S. 260</a></span>, <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/" aria-description="Citation for case: Gustafson v. Florida">94 S.Ct. 488</a></span>, <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/" aria-description="Citation for case: Gustafson v. Florida">38 L.Ed.2d 456</a></span> (1973);
  <em>
   United States v. Edwards,
  </em>
  <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">415 U.S. 800</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">94 S.Ct. 1234</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">39 L.Ed.2d 771</a></span> (1974), we do not believe that appellant’s suggested balance can be sustained.
 </p>
<p id="b674-6">
  The line which he attempts to draw placing the briefcase beyond the search of his “person” which
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>
  </em>
  and
  <em>
   Gus-tafson
  </em>
  expressly approve is one requiring gossamer distinctions. There is no indication that the result in those cases would have been any different had the cigarette packages been in the defendants’ hands rather than in their pockets or if they had been dropped to the ground in response to police command. While a briefcase may be a different order of container from a cigarette box, it is not easy to rest a principled articulation of the reach of the fourth amendment upon the distinction.
  <em>
   Cf. United States v. Micheli,
  </em>
  <span class="citation" data-id="9460030"><a href="/opinion/314831/united-states-v-frederick-m-micheli/" aria-description="Citation for case: United States v. Frederick M. Micheli">487 F.2d 429</a></span> (1st Cir. 1973). Justice Marshall made an argument not unlike that of appellant in his dissent to
  <em>
   Gustafson
  </em>
  and
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#256" aria-description="Citation for case: United States v. Edwards">415 U.S. at 256-59</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">94 S.Ct. 1234</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">39 L.Ed.2d 771</a></span> (Marshall, J., dissenting), but while that position may have analytical appeal,
  <em>
   see The Supreme Court, 1973 Term,
  </em>
  88 Harv.L.Rev. 41, 187 (1974), it does not presently represent the law. In
  <em>
   <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">Edwards</a></span>
  </em>
  the Court, after noting that the courts of appeals have generally permitted searches of both “the person and the property in his immediate possession,” <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#803" aria-description="Citation for case: United States v. Edwards">415 U.S. at 803</a></span>, 94 S.Ct. at 1237, stated:
 </p>
<blockquote id="AIEA">
  “Indeed, it is difficult to perceive what is unreasonable about the police examining and holding as evidence those personal effects of the accused that they already have in their lawful custody as the result of a lawful arrest.”
 </blockquote>
<p id="AZ6">
<em>
   Id.
  </em>
  at 806, 94 S.Ct. at 1238. These observations were in the context of searches in the station house after an arrest. However, there can be little doubt that they apply equally to searches in the field immediately incident to the arrest. Appellant has conceded the agents properly seized the briefcase as an incident to
  <span citation-index="1" class="star-pagination" label="611"> 
   *611
   </span>
  his arrest. At that point any expectation of privacy which he held with regard to the briefcase was taken out of
 </p>
<blockquote id="b675-5">
  “the realm of protection from police interest in weapons, means of escape, and evidence.”
 </blockquote>
<p id="b675-8">
<em>
   United States v. DeLeo, supra
  </em>
  at 493,
  <em>
   quoted with approval in Edwards,
  </em>
  <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#808" aria-description="Citation for case: United States v. Edwards">415 U.S. at 808-09</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">94 S.Ct. 1234</a></span>, <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/" aria-description="Citation for case: United States v. Edwards">39 L.Ed.2d 771</a></span>.
 </p>
<p id="b675-9">
  Ill
 </p>
<p id="b675-10">
  We discuss appellant’s final two claims together. He contends that the admission into evidence of the contents of the briefcase allowed the jury impermissibly to convict him because they believed that he was engaged in other crimes or that he was a dangerous person, rather than for the specific violations with which he was charged. In his brief he readily concedes that, “Innocent people do not carry three ski masks with a loaded gun.” However, he argues that unless these objects could be specifically tied to the robbery of the Arlington bank, they were too prejudicial for the jury to be permitted to consider them. Having failed to persuade the trial court that the items should be excluded, he then sought a charge instructing the jurors that they could not speculate concerning either the defendant’s character or reputation or the use of these items if it was found that they were not used in the bank robbery. Since the brown masks were not the same as the navy blue or black ones described by witnesses, and there was nothing to tie this revolver to the handguns used at the Suburban National Bank, this charge would have been tantamount to directing the jury that the objects should be disregarded altogether. The district court declined to give the requested instruction.
 </p>
<p id="b675-11">
  On the issue of admissibility, there is some dispute as to whether appellant properly raised this ground of objection in the trial court, but assuming the claim is properly before us, we find it without merit.
 </p>
<p id="b675-12">
  The evidence may have suggested that appellant was in the business of armed robbery. If its only value was to show appellant’s bad character or other criminal activity, it would be inadmissible under familiar principles. But it tended also to prove that he was one of the robbers in question, and as this court said in
  <em>
   Green v. United States,
  </em>
  <span class="citation" data-id="1484817"><a href="/opinion/1484817/green-v-united-states/#543" aria-description="Citation for case: Green v. United States">176 F.2d 541, 543</a></span> (1st Cir. 1949), “[I]t is . . . clear that [evidence] otherwise relevant is not rendered inadmissible merely because its tendency is to prove the commission of some other crime.”
  <em>
   Cf. United States v. Hopkinson,
  </em>
  <span class="citation" data-id="317281"><a href="/opinion/317281/united-states-v-mark-hopkinson/#1043" aria-description="Citation for case: United States v. Mark Hopkinson">492 F.2d 1041, 1043</a></span> (1st Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./417/968/">417 U.S. 968</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./94/3171/">94 S.Ct. 3171</a></span>, <span class="citation no-link">41 L.Ed.2d 1139</span> (1974). The test of admissibility requires balancing the prejudicial potential of the evidence against its probative value, and that task is committed primarily to the trial court. See
  <em>
   United States v. Brettholz,
  </em>
  <span class="citation" data-id="313664"><a href="/opinion/313664/united-states-v-james-brettholz-and-milton-santiago/#487" aria-description="Citation for case: United States v. James Brettholz and Milton Santiago">485 F.2d 483, 487</a></span> (2d Cir. 1973),
  <em>
   cert. denied sub nom., Santiago v. United States,
  </em>
  <span class="citation" data-id="8989582"><a href="/opinion/8997205/santiago-v-united-states/" aria-description="Citation for case: Santiago v. United States">415 U.S. 976</a></span>, <span class="citation" data-id="8989582"><a href="/opinion/8997205/santiago-v-united-states/" aria-description="Citation for case: Santiago v. United States">94 S.Ct. 1561</a></span>, <span class="citation no-link">39 L.Ed.2d 871</span> (1974);
  <em>
   United States v. Ravich,
  </em>
  <span class="citation" data-id="288484"><a href="/opinion/288484/united-states-v-ronald-raymond-ravich-and-edward-mcconnell/#1203" aria-description="Citation for case: United States v. Ronald Raymond Ravich and Edward McConnell">421 F.2d 1196, 1203-05</a></span> (2d Cir.),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./400/834/">400 U.S. 834</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./91/69/">91 S.Ct. 69</a></span>, <span class="citation no-link">27 L.Ed.2d 66</span> (1970);
  <em>
   cf.
  </em>
  Fed.R.Evid. 401-03, 404(b). The gun and three ski masks introduced at Eatherton’s trial corresponded to functionally similar accessories used a few days before in the Arlington robbery. Even if not used in that robbery, the number and character of the items tended logically to associate appellant with that particular crime.
  <span class="citation" data-id="1484817"><a href="/opinion/1484817/green-v-united-states/#543" aria-description="Citation for case: Green v. United States"><em>
   See Green, supra
  </em>
  at 543</a></span>,
  <em>
   quoting from Bracey v. United States,
  </em>
  <span class="citation" data-id="1551231"><a href="/opinion/1551231/bracey-v-united-states/" aria-description="Citation for case: Bracey v. United States">79 U.S.App.D.C. 23</a></span>, <span class="citation" data-id="1551231"><a href="/opinion/1551231/bracey-v-united-states/#87" aria-description="Citation for case: Bracey v. United States">142 F.2d 85, 87-88</a></span> (1944). Like much relevant circumstantial evidence, the objects do not, by themselves, establish guilt beyond a reasonable doubt. But like the discovery of an army uniform in the wardrobe of one suspected of committing a crime in which one of the participants wore such a uniform, the evidence in question enhanced the probability of guilt, and, combined with other evidence such as Miss Leak’s identification, was plainly probative. The point of which the jury could properly take notice is not that innocent people do not carry
  <span citation-index="1" class="star-pagination" label="612"> 
   *612
   </span>
  the particular combination of items, but rather that the bundle of implements is distinctive enough to support the Government’s argument that appellant was one of the individuals making use of very similar instruments several days earlier. The court did not abuse its discretion in admitting the items.
 </p>
<p id="b676-4">
  With regard to the contents of the briefcase the trial court instructed the jurors:
 </p>
<blockquote id="b676-5">
  “The Court charges you that you may also consider physical evidence which has been admitted during the trial. As with testimonial evidence, you may accept or reject such physical evidence as probative of the crime charged.
 </blockquote>
<blockquote id="b676-6">
  If you find that the ski masks and/or the gun which were allegedly in the defendant’s possession at the time of his arrest were not the mask and/or the gun used in the robbery of the Suburban National Bank of Arlington on March 25, 1974, you may not speculate concerning the defendant’s character or reputation.
 </blockquote>
<blockquote id="b676-7">
  You may, however, give such weight to it as you deem proper, that is, to the physical evidence. You may give such weight to it as you deem proper in light of all the evidence in the case.
 </blockquote>
<blockquote id="b676-8">
  You may, of course, convict the defendant only if you find beyond a reasonable doubt that he is guilty of the crime charged, . . . the robbery of the Suburban National Bank of Arlington on March 25, 1974.”
 </blockquote>
<p id="b676-10">
  In addition to appealing from the court’s refusal to give the instructions which he submitted, appellant argues that the portion of the charge contained in the third paragraph of the above excerpt somehow gave the jury too much leeway in deciding what inferences could be drawn from the items in the briefcase. He contends that the charge given, to which he seasonably objected, Fed. R.Crim.P. 30, was so ambiguous and misleading as to confuse and prejudice the jury. However, the court quite properly warned the jurors against using the evidence to infer guilt from character. It could be appropriately used in conjunction with other evidence to identify appellant as one of the three robbers, and, if the jurors adhered to the instructions, this was how it was used. We find no error in the instruction, which was an apt one in the circumstances.
 </p>
<p id="b676-12">
  IV
 </p>
<p id="b676-13">
  That disposes of all the issues raised by the parties. A further matter requires our attention, however. The double conviction and sentences under the Bank Robbery Act, <span class="citation no-link">18 U.S.C. §§ 2113</span>(a) and (d), for a single crime constitute plain error under
  <em>
   O’Clair v. United States,
  </em>
  <span class="citation" data-id="307220"><a href="/opinion/307220/dickie-r-oclair-v-united-states/" aria-description="Citation for case: Dickie R. O&#x27;Clair v. United States">470 F.2d 1199</a></span> (1st Cir. 1972),
  <em>
   cert. denied,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.S./412/921/">412 U.S. 921</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/2741/">93 S.Ct. 2741</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/37/148/">37 L.Ed.2d 148</a></span> (1973). We vacate the judgment in its present form and remand to the district court for entry of a new judgment embodying the conviction and sentence under Count 2 only.
 </p>
<p id="b676-14">
<em>
   So ordered.
  </em>
</p>





<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b670-8">
   . The Bureau of Identification officer’s testimony, based on the average content of each drawer, would lead one to conclude that Goo-kin had viewed in the vicinity of 800 photographs, while Gookin testified that it seemed to him that he had gone through only about 70-75.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b671-7">
   . At the suppression hearing two FBI agents testified that Gookin had picked out appellant’s picture from this spread as one of the men he had seen near the bank. Gookin, however, was uncertain whether he had done so, and at the trial testified that he had been unable to pick out anyone. The two agents did not testify at the trial regarding Gookin’s alleged identification of appellant from this photo spread.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b671-13">
   . There is some conflict in the testimony offered at the suppression hearing, unresolved by any specific finding of the court, as to whether Gookin was shown a spread containing appellant’s photograph or merely the single photo.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b672-6">
   . For example, Inspector O’Brien of the Arlington police testified at the suppression hearing that the nine photo spread he had shown Leak on March 31, included photographs of a number of individuals known to have previously associated with Eatherton. O’Brien hoped that this display might lead to an identification of the other two men involved in the robbery. While this may have been sound police practice, we do not perceive the necessity for including appellant’s already selected photo in this spread, especially in view of the fact that he was already in custody.
   <em>
    Cf. United States v. Fowler,
   </em>
   <span class="citation" data-id="295201"><a href="/opinion/295201/united-states-v-rodney-merle-fowler/#134" aria-description="Citation for case: United States v. Rodney Merle Fowler">439 F.2d 133, 134</a></span> (9th Cir. 1971).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b673-6">
   . The items found in the briefcase and introduced into evidence consisted of:
  </p>
<blockquote id="b673-7">
   “One .38 caliber Smith and Wesson revolver loaded with 6 rounds of high velocity, cavity-nose ammunition;
  </blockquote>
<blockquote id="b673-8">
   One Sears and Roebuck Craftsman dent puller;
  </blockquote>
<blockquote id="b673-15">
   Three brown ski masks;
  </blockquote>
<blockquote id="b673-16">
   One pair of gray slacks;
  </blockquote>
<blockquote id="b673-17">
   Two boxes of sheet metal screws;
  </blockquote>
<blockquote id="b673-18">
   One pair of leather gloves;
  </blockquote>
<blockquote id="b673-19">
   One pair of black shoes;
  </blockquote>
<blockquote id="b673-20">
   One screwdriver.”
  </blockquote>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/united-states-v-gratkowski--4765051.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cd2dd437dfb267ed", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "united-states-v-gratkowski--4765051"}, "payload": {"all": [{"cite": "964 F.3d 307", "page": "307", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "964"}], "display": "964 F.3d 307", "official": {"cite": "964 F.3d 307", "page": "307", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "964"}, "official_selection_present": true, "record_id": "united-states-v-gratkowski--4765051"}}
{"assertion_id": "0403a669be7be524", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "united-states-v-gratkowski--4765051"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "united-states-v-gratkowski--4765051", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — united-states-v-gratkowski--4765051

```json
{
  "schema_version": "s2.v1",
  "record_id": "united-states-v-gratkowski--4765051",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "United States v. Richard Gratkowski",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Gratkowski",
    "court": "U.S. Court of Appeals, 5th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca5",
    "state": null,
    "date_decided": null,
    "year": 2020,
    "docket": "No. 19-50492",
    "cluster_id": 4765051,
    "lead_opinion_id": 4545398,
    "sibling_ids": [],
    "absolute_url": "/opinion/4765051/united-states-v-richard-gratkowski/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "964 F.3d 307",
      "volume": "964",
      "reporter": "F.3d",
      "page": "307",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "964 F.3d 307",
        "volume": "964",
        "reporter": "F.3d",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "964 F.3d 307",
    "official_selection": {
      "court_class": "coa",
      "selected": "964 F.3d 307",
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
    "date_created": "2026-07-06T13:11:53Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:12:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:12:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:12:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — united-states-v-gratkowski--4765051

```
      Case: 19-50492     Document: 00515473290        Page: 1   Date Filed: 06/30/2020




              IN THE UNITED STATES COURT OF APPEALS
                       FOR THE FIFTH CIRCUIT
                                                                      United States Court of Appeals
                                                                               Fifth Circuit

                                                                             FILED
                                       No. 19-50492                      June 30, 2020
                                                                        Lyle W. Cayce
UNITED STATES OF AMERICA,                                                    Clerk


                Plaintiff - Appellee

v.

RICHARD NIKOLAI GRATKOWSKI,

                Defendant - Appellant




                    Appeal from the United States District Court
                         for the Western District of Texas


Before STEWART, DENNIS, and HAYNES, Circuit Judges.
HAYNES, Circuit Judge:
          Richard Gratkowski appeals the district court’s denial of his motion to
suppress evidence obtained through a search warrant. We AFFIRM.
                                 I.     Background
     A.       Factual Background
          Gratkowski became the subject of a federal investigation when federal
agents began investigating a child-pornography website (the “Website”). 1 To




        The actual name of the Website remained confidential during the district court
          1

proceedings in light of an ongoing investigation. We continue to use this generic name.
    Case: 19-50492       Document: 00515473290     Page: 2   Date Filed: 06/30/2020



                                   No. 19-50492
download material from the Website, some users, like Gratkowski, paid the
Website in Bitcoin.
      Bitcoin is a type of virtual currency. Each Bitcoin user has at least one
“address,” similar to a bank account number, that is a long string of letters
and numbers.      Bitcoin users send Bitcoin to other users through these
addresses using a private key function that authorizes the payments. To
conduct Bitcoin transactions, Bitcoin users must either download Bitcoin’s
specialized software or use a virtual currency exchange, such as the one used
here, called Coinbase.
      When a Bitcoin user transfers Bitcoin to another address, the sender
transmits a transaction announcement on Bitcoin’s public network, known as
a blockchain. 2 The Bitcoin blockchain contains only the sender’s address, the
receiver’s address, and the amount of Bitcoin transferred. The owners of the
addresses are anonymous on the Bitcoin blockchain, but it is possible to
discover the owner of a Bitcoin address by analyzing the blockchain.
      For example, when an organization creates multiple Bitcoin addresses,
it will often combine its Bitcoin addresses into a separate, central Bitcoin
address (i.e., a “cluster”).   It is possible to identify a “cluster” of Bitcoin
addresses held by one organization by analyzing the Bitcoin blockchain’s
transaction history. Open source tools and private software products can be
used to analyze a transaction.




      2  Blockchain is a technological advancement that permits members in a shared
network to “record a history of transactions on an immutable ledger.” See Ashley N.
Longman, Note, The Future of Blockchain: As Technology Spreads, It May Warrant More
Privacy Protection for Information Stored with Blockchain, 23 N.C. BANKING INST. 111,
118–19 (2019) (citing Brittany Manchisi, What is Blockchain Technology?, BLOCKCHAIN
PULSE:          IBM          BLOCKCHAIN            BLOG (July          31,     2018),
https://www.ibm.com/blogs/blockchain/2018/07/what-is-blockchain-technology/).
                                         2
    Case: 19-50492     Document: 00515473290     Page: 3   Date Filed: 06/30/2020



                                  No. 19-50492
   B.     Procedural History
        Federal agents used an outside service to analyze the publicly viewable
Bitcoin blockchain and identify a cluster of Bitcoin addresses controlled by
the Website. Once they identified the Website’s Bitcoin addresses, agents
served a grand jury subpoena on Coinbase—rather than seeking and
obtaining a warrant—for all information on the Coinbase customers whose
accounts had sent Bitcoin to any of the addresses in the Website’s cluster.
Coinbase identified Gratkowski as one of these customers.             With this
information, agents obtained a search warrant for Gratkowski’s house. At
his house, agents found a hard drive containing child pornography, and
Gratkowski admitted to being a Website customer.
        The Government charged Gratkowski with one count of receiving child
pornography and one count of accessing websites with intent to view child
pornography. Gratkowski moved to suppress the evidence obtained through
the warrant, arguing that the subpoena to Coinbase and the blockchain
analysis violated the Fourth Amendment.          The district court denied the
motion.      Gratkowski entered a conditional guilty plea to both counts,
reserving the right to appeal the denial of his motion to suppress.     After the
district court issued its final judgment, Gratkowski timely appealed.
                         II.   Standard of Review
        In reviewing “a district court’s ruling on a motion to suppress, we
review questions of law de novo and factual findings for clear error.” United
States v. Ganzer, 922 F.3d 579, 583 (5th Cir.), cert. denied, 140 S. Ct. 276
(2019) (mem.) (internal quotation marks and citation omitted).          “We will
uphold a district court’s denial of a suppression motion if there is any
reasonable view of the evidence to support [the denial].”          Id. (internal
quotation marks and citation omitted).


                                       3
     Case: 19-50492       Document: 00515473290         Page: 4    Date Filed: 06/30/2020



                                        No. 19-50492
                                 III.    Discussion
        Gratkowski presents the novel question of whether an individual has a
Fourth Amendment privacy interest in the records of their Bitcoin
transactions. 3 For the Government to have infringed upon an individual’s
Fourth Amendment protection against unreasonable searches, the person
must have had a “reasonable expectation of privacy” in the items at issue.
United States v. Jones, 565 U.S. 400, 406 (2012).                 Under the third-party
doctrine, a person generally “has no legitimate expectation of privacy in
information he voluntarily turns over to third parties.” Smith v. Maryland,
442 U.S. 735, 743–44 (1979). But relying on Carpenter v. United States, 138
S. Ct. 2206, 2217 (2018), which limited the applicability of the third-party
doctrine in the context of cell phones, Gratkowski argues that the
Government violated his reasonable expectation of privacy in the records of
his Bitcoin transactions on (1) Bitcoin’s public blockchain and (2) Coinbase.
In that regard, Gratkowski argues that the district court erred in denying his
suppression motion. We hold that it did not.
   A.       The Third-Party Doctrine
        Applying the third-party doctrine, the Supreme Court in United States
v. Miller held that bank records were not subject to Fourth Amendment
protections. 425 U.S. 435, 439–40 (1976). The Court concluded that the bank
records were “not confidential communications but negotiable instruments,”
which “contain[ed] only information voluntarily conveyed to the banks and


        3So far, we have found only two other federal district courts (and no circuit courts)
that have addressed the issue of whether an individual has a privacy interest in the records
of their Bitcoin transactions on a virtual currency exchange. See Zietzke v. United States
(Zietzke II), No. 19-cv-03761, 2020 WL 264394 (N.D. Cal. Jan. 17, 2020); Zietzke v. United
States (Zietzke I), 426 F. Supp. 3d 758 (W.D. Wash. 2019). In each case, the district court
held that the defendant did not have a privacy interest in their Bitcoin transaction records
because the transactions were shared with a third party, the virtual currency exchange.
Zietzke II, 2020 WL 264394, at *13; Zietzke I, 426 F. Supp. 3d at 768-69.
                                             4
    Case: 19-50492    Document: 00515473290    Page: 5   Date Filed: 06/30/2020



                                No. 19-50492
exposed to their employees in the ordinary course of business.” Id. at 442. It
recognized that in enacting the Bank Secrecy Act, Congress assumed that
individuals lacked “any legitimate expectation of privacy concerning the
information kept in bank records.” Id. at 442–43 (noting that the express
purpose of the Act was “to require records to be maintained because they
‘have a high degree of usefulness in criminal tax, and regulatory
investigations and proceedings’” (quoting 12 U.S.C. § 1829b(a)(1)).
      The Court has also held that the third-party doctrine applies to
telephone call logs. Smith, 442 U.S. at 742–44. It held that individuals had
no privacy interest in the telephone numbers they dialed because people
generally do not have any actual expectation of such privacy and “voluntarily
convey[]” the dialed numbers to the phone company by placing a call. Id.
      However, the Supreme Court recently concluded differently in the
context of cell phones. See Carpenter, 138 S. Ct. at 2217. In Carpenter, the
Court held that individuals had a privacy interest in their cell phone location
records, known as cell-site location information (“CSLI”), despite the records
being held by a third party. Id. In discussing the third-party doctrine, the
Court noted that the sole act of sharing did not eliminate an individual’s
privacy interest. Id. at 2219. Rather, the Court considered (1) “the nature of
the particular documents sought,” which includes whether the sought
information was limited and meant to be confidential, and (2) the
voluntariness of the exposure.      Id. at 2219–20 (internal citation and
quotation marks omitted).
      Regarding the nature of the information sought, the Court noted that
“telephone call logs reveal little in the way of identifying information” and
that checks are “not confidential communications but negotiable instruments
. . . used in commercial transactions.” Id. at 2219 (internal quotation marks
and citations omitted).     Unlike telephone call and bank records, CSLI
                                      5
    Case: 19-50492      Document: 00515473290      Page: 6   Date Filed: 06/30/2020



                                    No. 19-50492
provides    officers   with   “an   all-encompassing    record   of   the   holder’s
whereabouts” and “provides an intimate window into a person’s life, revealing
not only [an individual’s] particular movements, but through them [their]
familial, political, professional, religious, and sexual associations.”      Id. at
2217 (internal quotation marks and citation omitted). Because individuals
“compulsively carry cell phones with them all the time[,]” cell phones have
become “almost a feature of human anatomy.” Id. at 2218 (internal quotation
marks and citation omitted). Thus, the Court held that CSLI “implicate[d]
privacy concerns far beyond those considered in Smith and Miller.” Id. at
2220.
        As for the voluntary exposure component, the Court noted that CSLI
was not voluntarily shared information for two reasons. First, “cell phones
and the services they provide are such a pervasive and insistent part of daily
life that carrying one is indispensable to participation in modern society.” Id.
(internal quotation marks and citation omitted).         Second, CSLI does not
require “any affirmative act on the part of the user.” Id. So long as the user
has their cell phone on, a third party receives CSLI. Id.
   B.      Gratkowski’s Reasonable Expectation of Privacy in his
           Information on the Bitcoin Blockchain
        Gratkowski cites Carpenter to support his argument that he had a
privacy interest in the information held in the Bitcoin blockchain. But the
information on Bitcoin’s blockchain is far more analogous to the bank records
in Miller and the telephone call logs in Smith than the CSLI in Carpenter.
        The nature of the information on the Bitcoin blockchain and the
voluntariness of the exposure weigh heavily against finding a privacy interest
in an individual’s information on the Bitcoin blockchain.             The Bitcoin
blockchain records (1) the amount of Bitcoin transferred, (2) the Bitcoin
address of the sending party, and (3) the Bitcoin address of the receiving

                                         6
     Case: 19-50492        Document: 00515473290        Page: 7     Date Filed: 06/30/2020



                                       No. 19-50492
party. The information is limited. Moreover, transacting through Bitcoin is
not “a pervasive [or] insistent part of daily life,” 4 and transferring and
receiving Bitcoin requires an “affirmative act” by the Bitcoin address holder.
See Carpenter, 138 S. Ct. at 2220 (internal citation and quotation marks
omitted).
       Further, Bitcoin users are unlikely to expect that the information
published on the Bitcoin blockchain will be kept private, thus undercutting
their claim of a “legitimate expectation of privacy.” See Smith, 442 U.S. at
743. Granted, they enjoy a greater degree of privacy than those who use
other money-transfer means, but it is well known that each Bitcoin
transaction is recorded in a publicly available blockchain. 5               Every Bitcoin
user has access to the public Bitcoin blockchain and can see every Bitcoin
address and its respective transfers. Due to this publicity, it is possible to
determine the identities of Bitcoin address owners by analyzing the
blockchain. 6 Gratkowski thus lacked a privacy interest in his information on
the Bitcoin blockchain. 7




       4  Unlike cell phones that are ubiquitous, Gratkowski points to nothing that suggests
Bitcoin is central to most people’s daily lives.
       5  See Satoshi Nakamoto, Bitcoin: A Peer-to-Peer Electronic Cash System 2 (2008),
https://bitcoin.org/bitcoin.pdf [hereinafter Nakamoto] (stating that Bitcoin transactions will
be verified with a public system that records Bitcoin transaction histories).
       6   See id. at 6.
       7  Because we hold that there is no privacy interest in information stored in the
Bitcoin blockchain, Gratkowski’s argument—that the federal agents’ method of using a
“powerful and sophisticated software” to analyze the Bitcoin blockchain intruded into a
constitutionally protected area and violated the Fourth Amendment—lacks merit. There is
no intrusion into a constitutionally protected area because there is no constitutional privacy
interest in the information on the blockchain.
                                              7
    Case: 19-50492     Document: 00515473290     Page: 8   Date Filed: 06/30/2020



                                 No. 19-50492
   C.      Gratkowski’s Reasonable Expectation of Privacy in his
           Bitcoin Transactions on Coinbase
        Gratkowski again cites Carpenter to support his argument that he had
a reasonable expectation of privacy in the Coinbase records that documented
his Bitcoin transactions. Like the Blockchain, we hold that the Coinbase
records are more akin to the bank records in Miller than the CSLI in
Carpenter.
        Coinbase is a financial institution, a virtual currency exchange, that
provides Bitcoin users with a method for transferring Bitcoin.         The main
difference between Coinbase and traditional banks, which were at issue in
Miller, is that Coinbase deals with virtual currency while traditional banks
deal with physical currency. But both are subject to the Bank Secrecy Act as
regulated financial institutions. See Miller, 425 U.S. at 440–41. Both keep
records of customer identities and currency transactions. See id. at 437–38.
        In that regard, the nature of the information and the voluntariness of
the exposure weigh heavily against finding a privacy interest in Coinbase
records.    See Carpenter, 138 S. Ct. at 2219.     First, Coinbase records are
limited. Having access to Coinbase records does not provide agents with “an
intimate window into a person’s life”; it provides only information about a
person’s virtual currency transactions. See id. at 2217. Second, transacting
Bitcoin through Coinbase or other virtual currency exchange institutions
requires an “affirmative act on part of the user.” See id. at 2220. Bitcoin
users have the option to maintain a high level of privacy by transacting
without a third-party intermediary. But that requires technical expertise, so
Bitcoin users may elect to sacrifice some privacy by transacting through an
intermediary such as Coinbase. Gratkowski thus lacked a privacy interest in
the records of his Bitcoin transactions on Coinbase.



                                       8
     Case: 19-50492       Document: 00515473290         Page: 9     Date Filed: 06/30/2020



                                       No. 19-50492
                                 IV.     Conclusion
       For the foregoing reasons, we AFFIRM the district court’s denial of
Gratkowski’s motion to suppress. 8




       8 Even if the Supreme Court were to extend Carpenter to Bitcoin transactions in the
future, we would still affirm the district court in this case because the good-faith exception
applies to bar suppression. United States v. Molina-Isidoro, 884 F.3d 287, 290 (5th Cir.
2018) (this exception applies when the agents “acted with the objectively reasonable belief
that their actions did not violate the Fourth Amendment”). Gratkowski was arrested in
January of 2018 before Carpenter was decided and, of course, no court had applied such
reasoning to Bitcoin transactions at that time. Thus, in such a circumstance, we would
agree with the district court’s holding that the agents “had no way to know, prior to
Carpenter, that there could be a reasonable expectation of privacy in records like the ones
obtained here.”
                                              9

```

---
