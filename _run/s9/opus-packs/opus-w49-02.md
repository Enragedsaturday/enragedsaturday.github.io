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

## GROUP: content/cases/Robbins v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: Robbins v. California
type: case
citation: "453 U.S. 420 (1981)"
parallel_cite: "101 S. Ct. 2841; 69 L. Ed. 2d 744"
neutral_cite: 1981 U.S. LEXIS 132
court: U.S.
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-07-01
docket: 80-148
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
  opinion_url: "https://www.courtlistener.com/opinion/110558/robbins-v-california/"
  cluster_id: 110558
  opinion_id: null
  identity_checked: true
lake:
  record_id: Robbins v. California
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Automobile Exception]]"
    role: Historical / origin
related:
  - "[[United States v. Ross]]"
  - "[[California v. Acevedo]]"
  - "[[United States v. Chadwick]]"
  - "[[Arkansas v. Sanders]]"
tags:
  - case
  - fourth-amendment
  - automobile-exception
  - containers
  - warrant-requirement
  - overruled
  - historical
holding: "A closed, opaque container found during the lawful search of an automobile may not be opened without a warrant even where police have probable cause — a bright-line container rule the Court overruled one Term later in United States v. Ross (1982)."
---

# Robbins v. California

*453 U.S. 420 (1981)* (No. 80-148) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[United States v. Ross]] (1982)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 110558 → 453 U.S. 420, decided 1981-07-01; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Highway patrol officers stopped Robbins for erratic driving, smelled marihuana, and searched his station wagon. In a recessed luggage compartment they found two packages wrapped in opaque green plastic; they unwrapped them without a warrant and found bricks of marihuana. The California courts upheld the search, and Robbins argued that the closed, opaque packages were entitled to Fourth Amendment protection notwithstanding the lawful search of the car.

## Issue
Whether police who are lawfully searching an automobile may open a closed, opaque container found inside without first obtaining a warrant.

## Rule
The plurality (Stewart, J.) extended *[[United States v. Chadwick|Chadwick]]* and *[[Arkansas v. Sanders|Sanders]]* to any closed container: a piece of luggage or wrapped package found in a car is protected to the same degree as one found anywhere else, and the automobile exception does not reach it. "We reaffirm today that such a container may not be opened without a warrant, even if it is found during the course of the lawful search of an automobile." — 453 U.S. at 428. ^pin-428

## Application
The plurality announced a [[Common Legal Terms#bright-line-rule|bright-line rule]]: absent a recognized exception, a closed, opaque container's contents are shielded from a warrantless search regardless of the container's size or shape. Because no exception applied, the officers should have secured the packages and obtained a warrant; opening them on the roadside violated the Fourth and Fourteenth Amendments.

## Conclusion
The judgment of the California Court of Appeal was **reversed**. Stewart, J., announced the judgment of the Court in a [[Common Legal Terms#plurality-opinion|plurality opinion]].

## Treatment & subsequent history
**Overruled by [[United States v. Ross]] (1982).** *Robbins*'s bright-line container rule survived barely a year. In *[[United States v. Ross|Ross]]* the Court held that when police have probable cause to search a lawfully stopped vehicle, that authority extends to every part of the car and any container within it that might conceal the object of the search — rejecting *Robbins*. *[[California v. Acevedo]]* (1991) then completed the shift, unifying the container rule and overruling *[[Arkansas v. Sanders]]* as well.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. Preserved as **history**, never as live law.

## Appears on
- [[Automobile Exception]] — *Historical / origin*

## Sources
- [*Robbins v. California*, 453 U.S. 420 (1981)](https://www.courtlistener.com/opinion/110558/robbins-v-california/) — pinpoint: 428 (plurality; Stewart, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *United States v. Ross*, 456 U.S. 798 (1982) (successor page: [[United States v. Ross]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ede0d65fc1a53b0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "453 U.S. 420 (1981)", "court": "U.S.", "neutral_cite": "1981 U.S. LEXIS 132", "official_citation_present": true, "parallel_cite": "101 S. Ct. 2841; 69 L. Ed. 2d 744", "title": "Robbins v. California", "year": "1981"}}
{"assertion_id": "240be1eb35509f0c", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Historical / origin", "title": "Robbins v. California"}}
{"assertion_id": "486cb66acb12032f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A closed, opaque container found during the lawful search of an automobile may not be opened without a warrant even where police have probable cause — a bright-line container rule the Court overruled one Term later in United States v. Ross (1982).", "title": "Robbins v. California"}}
{"assertion_id": "9179aa19c3216cae", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Robbins v. California", "varies_by_point": "false"}}
{"assertion_id": "9c235909196caa71", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Robbins v. California"}}
```

### lake record — Robbins v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Robbins v. California",
  "status": "under_review",
  "identity": {
    "case_name": "Robbins v. California",
    "case_name_short": "Robbins",
    "case_name_full": "Robbins v. California",
    "input_case_name": "Robbins v. California",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-07-01",
    "year": 1981,
    "docket": "80-148",
    "cluster_id": 110558,
    "lead_opinion_id": 9428483,
    "sibling_ids": [],
    "absolute_url": "/opinion/110558/robbins-v-california/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "453 U.S. 420",
      "volume": "453",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 2841",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 744",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 132",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "453 U.S. 420",
        "volume": "453",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 2841",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "2841",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 2d 744",
        "volume": "69",
        "reporter": "L. Ed. 2d",
        "page": "744",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 132",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "453 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "453 U.S. 420",
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
    "date_created": "2026-07-07T13:28:16Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:28:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "robbins-v-california--110558",
      "to_record_id": "Robbins v. California",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Robbins v. California

```
<opinion type="majority">
<author id="b464-4"><page-number citation-index="1" label="422">*422</page-number>Justice Stewart</author>
<p id="A74">announced the judgment of the Court and delivered an opinion, in which Justice Brennan, Justice White, and Justice Marshall joined.</p>
<p id="b464-5">I</p>
<p id="b464-6">On the early morning of January 5, 1975, California Highway Patrol officers stopped the petitioner’s car — a 1966 Chevrolet station wagon — because he had been driving erratically. He got out of his vehicle and walked towards the patrol car. When one of the officers asked him for his driver’s license and the station wagon’s registration, he fumbled with his wallet. When the petitioner opened the car door to get out the registration, the officers smelled marihuana smoke. One of the officers patted down the petitioner, and discovered a vial of liquid. The officer then searched the passenger compartment of the car, and found marihuana as well as equipment for using it.</p>
<p id="b464-7">After putting the petitioner in the patrol car, the officers opened the tailgate of the station wagon, located a handle set flush in the deck, and lifted it up to uncover a recessed luggage compartment. In the compartment were a totebag and two packages wrapped in green opaque plastic.<footnotemark>1</footnotemark> The police unwrapped the packages; each one contained 15 pounds of marihuana.</p>
<p id="b464-8">The petitioner was charged with various drug offenses, his pretrial motion to suppress the evidence found when the <page-number citation-index="1" label="423">*423</page-number>packages were unwrapped was denied, and a jury convicted him. In an unpublished opinion, the California Court of Appeal affirmed the judgment in all relevant respects. This Court granted a writ of certiorari, vacated the Court of Appeal’s judgment, and remanded the case for further consideration in light of <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>. <span class="citation multiple-matches"><a href="/c/U.%20S./443/903/">443 U. S. 903</a></span>. On remand, the Court of Appeal again found the warrantless opening of the packages constitutionally permissible, since the trial court “could reasonably [have] conclude [d] that the contents of the packages could have been inferred from their outward appearance, so that appellant could not have held a reasonable expectation of privacy with respect to the contents.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d 34, 40</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr. 780, 783</a></span>. Because of continuing uncertainty as to whether closed containers found during a lawful warrantless search of an automobile may themselves be searched without a warrant, this Court granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./449/1109/">449 U. S. 1109</a></span>.</p>
<p id="b465-5">II</p>
<p id="b465-6">The Fourth Amendment to the Constitution, which is made applicable to the States through the Fourteenth Amendment, establishes “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” This Court has held that a search is <em>per se </em>unreasonable, and thus violates the Fourth Amendment, if the police making the search have not first secured from a neutral magistrate a warrant that satisfies the terms of the Warrant Clause of the Fourth Amendment. See, <em>e. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. Although the Court has identified some exceptions to this warrant requirement, the Court has emphasized that these exceptions are “few,” “specifically established,” and “well-delineated.” <em>Katz </em>v. <em>United States, supra, </em>at 357.</p>
<p id="b465-7">Among these exceptions is the so-called “automobile exception.” See <em>Colorado </em>v. <em>Bannister, </em><span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1</a></span>. In <em>Carroll </em><page-number citation-index="1" label="424">*424</page-number>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, the Court held that a search warrant is unnecessary “where there is probable cause to search an automobile stopped on the highway; the car is movable, the occupants are alerted, and the car’s contents may never be found again if a warrant must be obtained.” <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span>. In recent years, we have twice been confronted with the suggestion that this “automobile exception” somehow justifies the warrantless search of a closed container found inside an automobile. Each time, the Court has refused to accept the suggestion.</p>
<p id="b466-5">In <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span>, the Government argued in part that luggage is analogous to motor vehicles for Fourth Amendment purposes, and that the “automobile exception” should thus be extended to encompass closed pieces of luggage. The Court rejected the analogy and insisted that the exception is confined to the special and possibly unique circumstances which were the occasion of its genesis. First, the Court said that “[o]ur treatment of automobiles has been based in part on their inherent mobility, which often makes obtaining a judicial warrant impracticable.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Id., </em>at 12</a></span>. While both cars and luggage may be “mobile,” luggage itself may be brought and kept under the control of the police.</p>
<p id="b466-6">Second, the Court acknowledged that “inherent mobility” cannot alone justify the automobile exception, since the Court has sometimes approved warrantless searches in which the automobile’s mobility was irrelevant. See <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span>; <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span>. The automobile exception, the Court said, is thus also supported by “the diminished expectation of privacy which surrounds the automobile” and which arises from the facts that a car is used for transportation and not as a residence or a repository of personal effects, that a car’s occupants and contents travel in plain view, and that automobiles are necessarily highly regulated by government. <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 12-13</a></span>. No such dimin<page-number citation-index="1" label="425">*425</page-number>ished expectation of privacy characterizes luggage; on the contrary, luggage typically is a repository of personal effects, the contents of closed pieces of luggage are hidden from view, and luggage is not generally subject to state regulation.</p>
<p id="b467-5">In <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span>, the State of Arkansas argued that the “automobile exception” should be extended to allow the warrantless search of everything found in an automobile during a lawful warrantless search of the vehicle itself. The Court rejected this argument for much the same reason it had rejected the Government’s argument in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>. </em>Pointing out, first, that “[o]nce police have seized a suitcase, as they did here, the extent of its mobility is in no way affected by the place from which it was taken,” the Court said that there generally “is no greater need for war-rantless searches of luggage taken from automobiles than of luggage taken from other places.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#763" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 763-764</a></span>. Second, the Court saw no reason to believe that the privacy expectation in a closed piece of luggage taken from a car is necessarily less than the privacy expectation in closed pieces of luggage found elsewhere.</p>
<p id="b467-6">In the present case, the Court once again encounters the argument — made in the Government’s brief as <em>amicus </em>curiae— that the contents of a closed container carried in a vehicle are somehow not fully protected by the Fourth Amendment. But this argument is inconsistent with the Court’s decisions in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>and <em>Sanders. </em>Those cases made clear, if it was not clear before, that a closed piece of luggage found in a lawfully searched car is constitutionally protected to the same extent as are closed pieces of luggage found anywhere else.</p>
<p id="b467-7">The .respondent, however, proposes that the <em>nature </em>of a container may diminish the constitutional protection to which it otherwise would be entitled — that the Fourth Amendment protects only containers commonly used to transport “personal effects.” By personal effects the respondent means property worn on or carried about the person or having some intimate relation to the person. In taking this position, the <page-number citation-index="1" label="426">*426</page-number>respondent relies on numerous opinions that have drawn a distinction between pieces of sturdy luggage, like suitcases, and flimsier containers, like cardboard boxes. Compare, <em>e. g., United States </em>v. Benson, <span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336</a></span> (CA8 1980) (leather totebag); <em>United States </em>v. <em>Miller, </em><span class="citation" data-id="371228"><a href="/opinion/371228/united-states-v-clifford-jerome-miller-and-kathelyn-vandraiss-miller/" aria-description="Citation for case: United States v. Clifford Jerome Miller and Kathelyn...">608 F. 2d 1089</a></span> (CA5 1979) (plastic portfolio); <em>United States </em>v. <em>Presler, </em><span class="citation" data-id="372532"><a href="/opinion/372532/united-states-v-lee-alton-presler-aka-robert-ray-presler-aka-robert/" aria-description="Citation for case: United States v. Lee Alton Presler, A/K/A Robert Ray...">610 F. 2d 1206</a></span> (CA4 1979) <em>(briefcase); United States </em>v. <em>Meier, </em><span class="citation" data-id="368269"><a href="/opinion/368269/united-states-v-paul-william-meier/" aria-description="Citation for case: United States v. Paul William Meier">602 F. 2d 253</a></span> (CA10 1979) (backpack); <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9465310"><a href="/opinion/361214/united-states-v-dennis-michael-johnson-and-stephen-arthur-baldwin/" aria-description="Citation for case: United States v. Dennis Michael Johnson, and Stephen...">588 F. 2d 147</a></span> (CA5 1979) <em>(duffelbag); United States </em>v. <em>Stevie, </em><span class="citation" data-id="9465095"><a href="/opinion/359034/united-states-v-robert-charles-stevie-united-states-of-america-v-raymond/" aria-description="Citation for case: United States v. Robert Charles Stevie, United States of...">582 F. 2d 1175</a></span> (CA8 1978), with <em>United States </em>v. <em>Mannino, </em><span class="citation" data-id="384549"><a href="/opinion/384549/united-states-v-paul-mannino/" aria-description="Citation for case: United States v. Paul Mannino">635 F. 2d 110</a></span> (CA2 1980) (plastic bag inside paper bag); <em>United States </em>v. <em>Goshorn, </em><span class="citation" data-id="381355"><a href="/opinion/381355/united-states-v-arthur-k-goshorn/#699" aria-description="Citation for case: United States v. Arthur K. Goshorn">628 F. 2d 697, 699</a></span> (CA1 1980) (“([t]wo plastic bags, further in three brown paper bags, further in two clear plastic bags’ ”); <em>United States </em>v. <em>Gooch, </em><span class="citation" data-id="9465960"><a href="/opinion/368494/united-states-v-william-daniel-gooch-jr/" aria-description="Citation for case: United States v. William Daniel Gooch, Jr.">603 F. 2d 122</a></span> (CA10 1979) (plastic bag); <em>United States </em>v. <em>Mackey, </em><span class="citation" data-id="9466932"><a href="/opinion/380505/united-states-v-osborne-mackey/" aria-description="Citation for case: United States v. Osborne MacKey">626 F. 2d 684</a></span> (CA9 1980) (paper bag); <em>United States </em>v. <em>Neumann, </em><span class="citation" data-id="360237"><a href="/opinion/360237/united-states-v-bradley-raymond-neumann/" aria-description="Citation for case: United States v. Bradley Raymond Neumann">585 F. 2d 355</a></span> (CA8 1978) (cardboard box).</p>
<p id="b468-5">The respondent’s argument cannot prevail for at least two reasons. First, it has no basis in the language or meaning of the Fourth Amendment. That Amendment protects people and their effects, and it protects those effects whether they are “personal” or “impersonal.” The contents of Chadwick’s footlocker and Sanders’ suitcase were immune from a warrantless search because they had been placed within a closed, opaque container and because Chadwick and Sanders had thereby reasonably “manifested an expectation that the contents would remain free from public examination.” <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 11</a></span>. Once placed within such a container, a diary and a dishpan are equally protected by the Fourth Amendment.</p>
<p id="b468-6">Second, even if one wished to import such a distinction into the Fourth Amendment, it is difficult if not impossible to perceive any objective criteria by which that task might be accomplished. What one person may put into a suitcase, another may put into a paper bag. <em>United States </em>v. <em>Ross, </em><page-number citation-index="1" label="427">*427</page-number>210 U. S. App. D. C. 342, <span class="citation" data-id="9468224"><a href="/opinion/392944/united-states-v-albert-ross-jr/" aria-description="Citation for case: United States v. Albert Ross, Jr.">655 F. 2d 1159</a></span> (1981) (en banc). And as the disparate results in the decided cases indicate, no court, no constable, no citizen, can sensibly be asked to distinguish the relative “privacy interests” in a closed suitcase, briefcase, portfolio, duffelbag, or box.</p>
<p id="b469-5">The respondent protests that footnote 13 of the <em>Sanders </em>opinion says that “[n]ot all containers and packages found by police during the course of a search will deserve the full protection of the Fourth Amendment.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764, n. 13</a></span>. But the exceptions listed in the succeeding sentences of the footnote are the very model of exceptions which prove the rule: “Thus, some containers (for example a kit of burglar tools or a gun case) by their very nature cannot support any reasonable expectation of privacy because their contents can be inferred from their outward appearance. Similarly, in some cases the contents of a package will be open to ‘plain view/ thereby obviating the need for a warrant.” <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders"><em>Id., </em>at 764-765, n. 13</a></span>. The second of these exceptions obviously refers to items in a container that is not closed. The first exception is likewise little more than another variation of the “plain view” exception, since, if the distinctive configuration of a container proclaims its contents, the contents cannot fairly be said to have been removed from a searching officer’s view. The same would be true, of course, if the container were transparent, or otherwise clearly revealed its contents. In short, the negative implication of footnote 13 of the <em>Sanders </em>opinion is that, unless the container is such that its contents may be said to be in plain view, those contents are fully protected by the Fourth Amendment.</p>
<p id="b469-6">The California Court of Appeal believed that the packages in the present case fell directly within the second exception described in this footnote, since “[a]ny experienced observer could have inferred from the appearance of the packages that they contained bricks of marijuana.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d, at 40</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 783</a></span>. The only evidence the court <page-number citation-index="1" label="428">*428</page-number>cited to support this proposition was the testimony of one of the officers who arrested the petitioner. When asked whether there was anything about “these two plastic wrapped green blocks which attracted your attention,” the officer replied, somewhat obscurely:</p>
<blockquote id="b470-5">“A. I had previous knowledge of transportation of such blocks. Normally contraband is wrapped this way, merely hearsay. I had never seen them before.</blockquote>
<blockquote id="b470-6">“Q. You had heard contraband was packaged this way?</blockquote>
<blockquote id="b470-7">“A. Yes.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#40" aria-description="Citation for case: People v. Robbins"><em>Id., </em>at 40, n. 2</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#783" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 783, n. 4</a></span>.</blockquote>
<p id="b470-8">This vague testimony certainly did not establish that marihuana is ordinarily “packaged this way.” Expectations of privacy are established by general social norms, and to fall within the second exception of the footnote in question a container must so clearly announce its contents, whether by its distinctive configuration, its transparency, or otherwise, that its contents are obvious to an observer. If indeed a green plastic wrapping reliably indicates that a package could only contain marihuana, that fact was not shown by the evidence of record in this case.<footnotemark>2</footnotemark></p>
<p id="b470-9">Although the two bricks of marihuana were discovered during a lawful search of the petitioner’s car, they were inside a closed, opaque container. We reaffirm today that such a container may not be opened without a warrant, even if it is found during the course of the lawful search of an automobile. Since the respondent does not allege the presence of any circumstances that would constitute a valid exception <page-number citation-index="1" label="429">*429</page-number>to this general rule,<footnotemark>3</footnotemark> it is clear that the opening of the closed containers without a search warrant violated the Fourth and Fourteenth Amendments. Accordingly, the judgment of the California Court of Appeal is reversed.</p>
<p id="b471-5">
<em>It is so ordered.</em>
</p>
<p id="b471-6">The Chief Justice concurs in the judgment.</p>
<footnote label="1">
<p id="b464-9"><em> ‘■A </em>photograph was made of one of the packages, and it was later described as follows:</p>
<blockquote id="b464-10">“The package visible in the photograph is apparently wrapped or boxed in an opaque material covered by an outer wrapping of transparent, cellophane-type plastic. (The photograph is not in color, and the ‘green’ plastic cannot be seen at all.) Both wrappings are sealed on the outside with at least one strip of opaque tape. As thus wrapped and sealed, the package roughly resembles an oversized, extra-long cigar box with slightly rounded corners and edges. It bears no legend or other written indicia supporting any inference concerning its contents.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#44" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d 34, 44</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#785" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr. 780, 785</a></span> (Rattigan, J., dissenting).</blockquote>
</footnote>
<footnote label="2">
<p id="b470-10"> As Judge Rattigan wrote in his dissenting opinion in the California Court of Appeal: “For all that I see, it could contain books, stationery, canned goods, or any number of other wholly innocuous items which might be heavy in weight. In fact, it bears a remarkable resemblance to an unlabelled carton of emergency highway flares that I bought from a store shelf and have carried in the trunk of my own automobile.” <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#44" aria-description="Citation for case: People v. Robbins">103 Cal. App. 3d, at 44</a></span>, <span class="citation" data-id="9721438"><a href="/opinion/2121440/people-v-robbins/#785" aria-description="Citation for case: People v. Robbins">162 Cal. Rptr., at 785</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b471-9"> In particular, it is not argued that the opening of the packages was incident to a lawful custodial arrest. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. See <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764, n. 11</a></span>. Further, the respondent does not argue that the petitioner consented to the opening of the packages.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Rochin v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: Rochin v. California
type: case
citation: "342 U.S. 165 (1952)"
parallel_cite: "72 S. Ct. 205; 96 L. Ed. 2d 183; 25 A.L.R. 2d 1396; 96 L. Ed. 183"
neutral_cite: 1952 U.S. LEXIS 2576
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1952
date_decided: 1952-01-02
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/104943/rochin-v-california/"
  cluster_id: 104943
  opinion_id: null
  identity_checked: true
lake:
  record_id: Rochin v. California
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Common Law Origins]]"
    role: Historical / origin
related:
  - "[[Common Law Origins]]"
  - "[[Wolf v. Colorado]]"
  - "[[Mapp v. Ohio]]"
  - "[[Schmerber v. California]]"
  - "[[County of Sacramento v. Lewis]]"
tags:
  - case
  - fourteenth-amendment
  - due-process
  - shocks-the-conscience
  - historical
  - bodily-intrusion
  - origin
holding: "Where police unlawfully broke into the defendant's home and, to recover capsules he had swallowed, forcibly pumped his stomach against his will, admitting the resulting evidence violated the Due Process Clause of the Fourteenth Amendment: government methods that 'shock the conscience' — conduct too close to the rack and the screw — offend fundamental fairness, and a state conviction obtained by them cannot stand."
aliases:
  - Rochin v. California
  - "Rochin v. California (1952)"
---

# Rochin v. California

*342 U.S. 165 (1952)* (No. 83) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Historical origin (⚪ unverified, pending S9)**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the historical framing below is authored orientation, not machine-certified. special: history-render — rendered as a foundational ORIGIN (role: Historical / origin) per PRACTICES §7: the "shocks the conscience" due-process principle is NOT overruled, but Rochin's function as the vehicle for excluding physical evidence from state prosecutions was a pre-incorporation stopgap later overtaken by Mapp v. Ohio. Identity cluster 104943 → combined opinion 104943 (Frankfurter, J.; 342 U.S. 165, decided Jan. 2, 1952). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*172`). S9 promotes. -->

## Background
Acting on "some information" that Rochin was selling narcotics, three Los Angeles County deputies entered his home and forced open his bedroom door. Seeing two capsules on a nightstand, they demanded to know whose they were; Rochin swallowed them. The deputies jumped on him and tried to force the capsules out of his mouth, and when that failed they handcuffed him and took him to a hospital, where a doctor forced an emetic through a tube into his stomach against his will. The induced vomiting produced two capsules containing morphine. Those capsules were the chief evidence at Rochin's trial for narcotics possession; he was convicted, and the California courts affirmed even while finding the officers had unlawfully broken in and assaulted him.

## Issue
Whether admitting evidence that police obtained by breaking into a suspect's home and forcibly pumping his stomach violates the Due Process Clause of the Fourteenth Amendment.

## Rule
Because at the time the Fourth Amendment's exclusionary rule did not yet bind the States, the Court measured the police conduct against the Fourteenth Amendment's guarantee of fundamental fairness, holding that some government methods are so brutal that a conviction resting on their fruits cannot stand: "This is conduct that shocks the conscience. Illegally breaking into the privacy of the petitioner, the struggle to open his mouth and remove what was there, the forcible extraction of his stomach's contents—this course of proceeding by agents of government to obtain evidence is bound to offend even hardened sensibilities. They are methods too close to the rack and the screw to permit of constitutional differentiation." — 342 U.S. at 172. ^pin-172

## Application
The Court treated coerced physical evidence like a coerced confession: due process is not indifferent to the means by which otherwise relevant and credible evidence is obtained, and forcibly extracting the contents of a person's stomach was of a piece with the coercion the Court had long forbidden. The standard was deliberately open-textured — convictions may not be secured by methods that offend a sense of justice, and applied here to the deputies' violent, warrantless invasion of Rochin's body. His conviction therefore could not stand.

## Conclusion
The judgment of the California District Court of Appeal was **reversed**. Frankfurter, J., delivered the opinion of the Court; Black and Douglas, JJ., concurred separately, objecting that the "shocks the conscience" standard was too subjective and that the Self-Incrimination Clause supplied a firmer ground.

## Treatment & subsequent history
**Status: Unverified — rendered as a historical origin.** This page is authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Rochin* is preserved here as a **historical origin**, and it is neither overruled nor disguised — but its role has two distinct threads that must be kept apart:

- **Still good law (the due-process principle).** The "shocks the conscience" test for egregious executive conduct survives as the standard for substantive due process, expressly **reaffirmed** in *[[County of Sacramento v. Lewis]]* (1998). On that point *Rochin* remains live authority.
- **Superseded in function (as a search-and-seizure remedy).** *Rochin* arose in the narrow window after *[[Wolf v. Colorado]]* (1949) applied the Fourth Amendment to the States but declined to impose the exclusionary rule; due process was then the only lever against the worst police intrusions. That stopgap was **overtaken** when *[[Mapp v. Ohio]]* (1961) incorporated the Fourth Amendment exclusionary rule against the States, and forced bodily intrusions were thereafter analyzed under the Fourth Amendment in *[[Schmerber v. California]]* (1966). Modern suppression of such evidence runs through the Fourth Amendment, not *Rochin*'s due-process route.

Teach *Rochin* as the origin point of the "shocks the conscience" doctrine and as a marker of the pre-incorporation era — an antecedent to the modern Fourth Amendment framework, not a current search-and-seizure remedy.

## Appears on
- [[Common Law Origins]] — *Historical / origin*

## Sources
- [*Rochin v. California*, 342 U.S. 165 (1952)](https://www.courtlistener.com/opinion/104943/rochin-v-california/) — pinpoint: 172 (Frankfurter, J., for the Court; the CL opinion text carries the reporter star `*172` immediately before the quoted "shocks the conscience" passage). Rule quote string-matched to the CL opinion text 2026-07-07 (the em-dash in "stomach's contents—this course" is reproduced from the source).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b3ee222467c6e59c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "342 U.S. 165 (1952)", "court": "U.S. Supreme Court", "neutral_cite": "1952 U.S. LEXIS 2576", "official_citation_present": true, "parallel_cite": "72 S. Ct. 205; 96 L. Ed. 2d 183; 25 A.L.R. 2d 1396; 96 L. Ed. 183", "title": "Rochin v. California", "year": "1952"}}
{"assertion_id": "b18f6f8484fa46e2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where police unlawfully broke into the defendant's home and, to recover capsules he had swallowed, forcibly pumped his stomach against his will, admitting the resulting evidence violated the Due Process Clause of the Fourteenth Amendment: government methods that 'shock the conscience' — conduct too close to the rack and the screw — offend fundamental fairness, and a state conviction obtained by them cannot stand.", "title": "Rochin v. California"}}
{"assertion_id": "b693ff2e580175e4", "dimension": "support", "kind": "home_role", "locator": {"home": "Common Law Origins"}, "payload": {"home": "Common Law Origins", "role": "Historical / origin", "title": "Rochin v. California"}}
{"assertion_id": "46d474dd596a3f3e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rochin v. California"}}
{"assertion_id": "98f633818cfc7b91", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Rochin v. California", "varies_by_point": "false"}}
```

### lake record — Rochin v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rochin v. California",
  "status": "under_review",
  "identity": {
    "case_name": "Rochin v. California",
    "case_name_short": "Rochin",
    "case_name_full": "Rochin v. California",
    "input_case_name": "Rochin v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1952-01-02",
    "year": 1952,
    "docket": null,
    "cluster_id": 104943,
    "lead_opinion_id": 9420649,
    "sibling_ids": [],
    "absolute_url": "/opinion/104943/rochin-v-california/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "342 U.S. 165",
      "volume": "342",
      "reporter": "U.S.",
      "page": "165",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "72 S. Ct. 205",
        "volume": "72",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 183",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 A.L.R. 2d 1396",
        "volume": "25",
        "reporter": "A.L.R. 2d",
        "page": "1396",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 183",
        "volume": "96",
        "reporter": "L. Ed.",
        "page": "183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1952 U.S. LEXIS 2576",
        "volume": "1952",
        "reporter": "U.S. LEXIS",
        "page": "2576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "342 U.S. 165",
        "volume": "342",
        "reporter": "U.S.",
        "page": "165",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 S. Ct. 205",
        "volume": "72",
        "reporter": "S. Ct.",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 2d 183",
        "volume": "96",
        "reporter": "L. Ed. 2d",
        "page": "183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1952 U.S. LEXIS 2576",
        "volume": "1952",
        "reporter": "U.S. LEXIS",
        "page": "2576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 A.L.R. 2d 1396",
        "volume": "25",
        "reporter": "A.L.R. 2d",
        "page": "1396",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 L. Ed. 183",
        "volume": "96",
        "reporter": "L. Ed.",
        "page": "183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "342 U.S. 165",
    "official_selection": {
      "court_class": "scotus",
      "selected": "342 U.S. 165",
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
    "date_created": "2026-07-06T13:47:12Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "rochin-v-california--104943",
      "to_record_id": "Rochin v. California",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Rochin v. California

```
<opinion type="majority">
<author id="b242-3"><page-number citation-index="1" label="166">*166</page-number>Mr. Justice Frankfurter</author>
<p id="Aq1">delivered the opinion of the Court.</p>
<p id="b242-4">- Having “some information that [the petitioner here] was selling narcotics,” three deputy sheriffs of the County of Los Angeles, on the morning of July 1, 1949, made for the two-story dwelling house in which Rochin lived with his mother, commonrlaw wife, brothers and sisters. Finding,the outside door open, they entered and then forced open the door to Rochin’s room, on the second floor. Inside they found petitioner sitting partly dressed on the side of the bed, upon which his wife was lying. On a “night stand” beside the bed the deputies spied two capsules. When asked “Whose stuff is this?” Rochin seized the capsules and put them in his mouth. A struggle ensued, in the course of which the three officers “jumped upon him” and attempted to extract, the capsules. The force they applied proved unavailing against Rochin’s resistance. He was handcuffed and taken to a hospital.' At the direction of one of the officers a doctor forced an emetic solution through a tube into Rochin’s stomach against his will. This “stomach pumping” produced vomiting. In the vomited matter were found two capsules which proved to contain morphine.</p>
<p id="b242-5">Rochin was brought to trial before a California Superior Court, sitting without a jury, on the charge of possessing “a preparation of morphine” in violation of the California Health and Safety Code, 1947, § 11,500. Rochin was convicted and sentenced to sixty days’ imprisonment. The chief evidence against him was the two capsules. They were admitted over petitioner’s objection, although the means of obtaining them was frankly set forth in the testimony by one of,the deputies, substantially as here narrated.</p>
<p id="b242-6">On appeal, the District Court of Appeal affirmed the Conviction, despite the finding that the officers “were <page-number citation-index="1" label="167">*167</page-number>guilty of unlawfully breaking into and entering defendant’s room and were guilty of unlawfully assaulting and battering defendant while in the room,” and “were guilty of unlawfully assaulting, battering, torturing and falsely imprisoning the defendant at the alleged hospital.” <span class="citation" data-id="9625880"><a href="/opinion/1419886/people-v-rochin/#143" aria-description="Citation for case: People v. Rochin">101 Cal. App. 2d 140, 143</a></span>, <span class="citation" data-id="9625880"><a href="/opinion/1419886/people-v-rochin/#3" aria-description="Citation for case: People v. Rochin">225 P. 2d 1, 3</a></span>. One of the three judges, while finding that “the record in this case reveals a shocking series of violations of constitutional rights,” concurred only because he felt bound by decisions of his Supreme Court. These, he asserted, “have been looked upon by law enforcement officers as an encouragement, if not an invitation, to the commission of such lawless acts.” <em><span class="citation" data-id="9625880"><a href="/opinion/1419886/people-v-rochin/" aria-description="Citation for case: People v. Rochin">Ibid.</a></span> </em>The Supreme Court of California denied without opinion Rochin’s petition for a hearing.<footnotemark>1</footnotemark> Two justices dissented from this denial, and in doing so expressed themselves thus: “. . . a conviction which rests upon evidence of incriminating objects obtained from the body of the accused by physical abuse is as invalid as a conviction which rests upon a verbal confession extracted from him by such abuse. . . . Had the- evidence forced from the defendant’s lips consisted of an oral confession that he illegally possessed a drug ... he would have the protection of the rule of law which excludes coerced confessions from evidence. But because the evidence forced from his lips consisted of real objects the People of this state are permitted to base a conviction upon it. [We] find no valid ground of distinction between a verbal confession extracted by physical abuse and a confession wrested from defendant’s body by physical abuse.” <span class="citation multiple-matches"><a href="/c/Cal.%20App.%202d/101/143/">101 Cal. App. 2d 143</a></span>, 149-150, <span class="citation no-link">225 P. 2d 913</span>, 917-918.</p>
<p id="b244-3"><page-number citation-index="1" label="168">*168</page-number>This Court granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./341/939/">341 U. S. 939</a></span>, because a serious question is raised as to the limitations which the Due Process Clause of the Fourteenth Amendment imposes on the conduct of criminal proceedings by the States.</p>
<p id="b244-4">In our federal system the administration of criminal justice is predominantly committed to the care of the States. The power to define crimes belongs to Congress only as an appropriate means of carrying into execution its limited grant of legislative powers. U. S. Const., Art. I, § 8, cl. 18. Broadly speaking, crimes in the United States are what the laws of the individual States, make them, subject to the limitations of Art. I, § 10, cl. 1, in the original Constitution, prohibiting bills of attainder and <em>ex post jacto </em>laws, and of the Thirteenth and Fourteenth Amendments.</p>
<p id="b244-5">These limitations, in the main, concern not restrictions upon the powers of the States to define crime, except in the restricted area where federal authority has pre-empted the field, but restrictions upon the manner in which the States may enforce their penal codes. Accordingly, in reviewing a State criminal conviction under a claim of right guaranteed by the Due Process Clause of the Fourteenth Amendment, from which is derived the most far-reaching and most frequent federal basis of challenging State criminal justice, “we must be deeply mindful of the responsibilities of the States for the enforcement of criminal laws, and exercise with due humility our merely negative function in subjecting convictions from state courts to the very narrow scrutiny which the Due Process Clause of the Fourteenth Amendment authorizes.” <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#412" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 412, 418</a></span>. Due process of law, “itself a historical product,” <em>Jackman </em>v. <em>Rosenbaum Co., </em><span class="citation" data-id="100034"><a href="/opinion/100034/jackman-v-rosenbaum-co/#31" aria-description="Citation for case: Jackman v. Rosenbaum Co.">260 U. S. 22, 31</a></span>, is not to be turned into a destructive dogma against the States in the .administration of their systems of criminal justice.</p>
<p id="b245-3"><page-number citation-index="1" label="169">*169</page-number>However, this Court too has its responsibility. Regard for the requirements of the Due Process Clause “inescapably imposes upon this Court an exercise of judgment upon the whole course of the proceedings [resulting in a conviction] in order to ascertain whether they offend those canons of decency and fairness which express the notions of justice of English-speaking peoples even toward those charged with the most heinous offenses.” <em>Malinski </em>v. <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#416" aria-description="Citation for case: Malinski v. New York"><em>New York, supra, </em>at 416-417</a></span>. These standards of justice are not authoritatively formulated anywhere as though they were specifics. Due process of law is a summarized constitutional guarantee of respect for those personal immunities which, as Mr. Justice Cardozo twice wrote for the Court, are “so rooted in the traditions and conscience of our people as to be ranked as fundamental,” <em>Snyder </em>v. <em>Massachusetts, </em><span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>, or are “implicit in the concept of ordered liberty.” <em>Palko </em>v. <em>Connecticut, </em><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325</a></span>.<footnotemark>2</footnotemark></p>
<p id="b245-4">The Court’s function in the observance of this settled conception of the Due Process Clause does, not leave us without adequate guides in subjecting State criminal procedures to constitutional judgment. In dealing not with the machinery of government but with human rights, the absence of formal exactitude, or want of fixity of meaning, is not an unusual or even regrettable attribute of constitutional provisions. Words being symbols do not speak without a gloss. On the one hand the gloss may be the deposit of history, whereby a term gains technical content. Thus the requirements of the Sixth and Seventh Amendments for trial by jury in the federal <page-number citation-index="1" label="170">*170</page-number>courts have a rigid meaning. No changes or chances can alter the content of the verbal symbol of “jury” — a body of twelve men who must reach a unanimous conclusion if the verdict is to go against the defendant.<footnotemark>3</footnotemark> On the other hand, the gloss of some of the verbal symbols of the Constitution does not give them a fixed technical content. It exacts a continuing process of application.</p>
<p id="b246-4">When the gloss has thus not been fixed but is a function of the process of judgment, the judgment is bound to fall differently at different times and differently at the same time through different judges. Even more specific provisions, such as the guaranty of freedom of speech and the detailed protection against unreasonable searches and seizures, have inevitably evoked as sharp divisions in this Court as the least specific and most comprehensive protection of liberties, the Due Process Clause.</p>
<p id="b246-5">The vague contours of the Due Process Clause do not leave judges at large.<footnotemark>4</footnotemark> We may not draw on our merely personal and private notions and disregard the limits that bind judges in their judicial function. Even though the concept of due process of law is not final and fixed, these limits are derived from considerations that are fused in' the whole nature of our judicial process. See Cardozo, <page-number citation-index="1" label="171">*171</page-number>The Nature of the Judicial Process; The Growth of the Law; The Paradoxes of Legal Science. These are considerations deeply rooted in reason and in the compelling traditions of .the legal profession. The Due Process Clause places upon this Court the duty of exercising a judgment, within the narrow confines of judicial power in reviewing State convictions, upon interests of society pushing in opposite directions.</p>
<p id="b247-4">Due process of law thus conceived is not to be derided as resort to a revival of “natural law.” <footnotemark>5</footnotemark> To believe that this judicial exercise of judgment could be avoided by freezing “due process of law” at some fixed stage of time or thought is to suggest that the most important aspect of constitutional adjudication is a function for inanimate machines and not for judges, for whom the independence safeguarded by Article III of the Constitution was designed and who are presumably guided by established standards of judicial behavior. Even cybernetics has not yet made that haughty claim. To practice the requisite detachment and to achieve sufficient objectivity no doubt demands of judges the habit of self-discipline and self-criticism, incertitude that one’s own views are incontestable and alert tolerance toward views-not shared. But <page-number citation-index="1" label="172">*172</page-number>these are precisely the presuppositions of our judicial process.. They are precisely the qualities society has a right to expect from those entrusted with ultimate judicial power.</p>
<p id="b248-4">Restraints on our jurisdiction are self-imposed only in the sense that there is from our decisions no immediate appeal short of impeachment or constitutional amendment. But that does not make due process of law a matter of judicial caprice. The faculties of the Due Process Clause may be indefinite and vague, but the mode of their ascertainment is not self-willed. In each case “due process of law” requires an evaluation based on a. disinterested inquiry pursued in the spirit of science, on a balanced order of facts exactly and fairly stated, on the detached consideration of conflicting claims, see <em>Hudson County Water Co. </em>v. <em>McCarter, </em><span class="citation" data-id="96834"><a href="/opinion/96834/hudson-county-water-co-v-mccarter/#355" aria-description="Citation for case: Hudson County Water Co. v. McCarter">209 U. S. 349, 355</a></span>, on a judgment not <em>ad hoc </em>and episodic but duly mindful of reconciling the needs both of continuity and of change in a progressive society.</p>
<p id="b248-5">Applying these general considerations to the circumstances of the present case, we are compelled to conclude that the proceedings by which this conviction was obtained do more than offend some fastidious squeamishness or private sentimentalism about combatting crime too energetically. This is conduct that shocks the conscience. Illegally breaking into the privacy of the petitioner, the struggle to open his mouth and remove what was there, the forcible extraction of his stomach’s contents — this course of proceeding by agents of government to obtain evidence is bound to offend even hardened sensibilities. They are methods too close to the rack and the screw to permit of constitutional differentiation.</p>
<p id="b248-6">It has long since ceased to be true that due process of law is heedless of the means by which otherwise'relevant and credible evidence is obtained. This was not true even before the series of recent cases enforced the constitutional principle that the States may not base convictions upon <page-number citation-index="1" label="173">*173</page-number>confessions, however much verified, obtained by ®0®r« cion. These decisions are not arbitrary exceptions to the comprehensive right of States to fashion their own rules of evidence for criminal trials. They are not sports in our constitutional law but applications of a general principle. They are only instances of the general requirement that States in their prosecutions respect certain decencies of civilized conduct. Due process of law, as a historic and generative principle, precludes defining, and thereby confining, these standards of conduct more precisély than to say that convictions cannot be brought about by methods that offend “a sense of justice.” See Mr. Chief Justice Hughes, speaking for a unanimous Court in <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 285-286</a></span>. It would be a stultification of the responsibility which the course of constitutional history has cast upon this Court to hold that in order to convict a man the police cannot extract by force what is in his mind but can extract what is in his stomach.<footnotemark>6</footnotemark></p>
<p id="b249-5">To attempt in this case to distinguish what lawyers call “real evidence” from verbal evidence is to ignore the reasons for excluding coerced confessions. Use of involuntary verbal confessions in State criminal trials is constitutionally obnoxious not only because of their unreliability. They are inadmissible under the Due Process Clause even though statements contained in them may be independently established as true. Coerced confessions offend the community’s sense of fair play and decency. So here, to sanction the brutal conduct which naturally enough was condemned by the court whose judgment is before us, would be to afford brutality the cloak of law. Nothing <page-number citation-index="1" label="174">*174</page-number>would be more calculated to discredit law and thereby to brutalize the temper of a society.</p>
<p id="b250-6">In deciding this case we do not heedlessly bring into question decisions in many States dealing with essentially different, even if related, problems. We therefore put to one side cases which have arisen in the State courts through use of modern methods and devices for discovering wrongdoers and bringing them to book. It does not fairly represent these decisions to suggest that they legalize force so brutal and so offensive to human dignity in securing evidence from a suspect as is revealed by this record. Indeed the California Supreme Court has not sanctioned this mode of securing a conviction. It merely exercised its discretion to decline a review of the conviction. All the California judges who have expressed themselves in this case have condemned the conduct in the strongest language.</p>
<p id="b250-7">We are not unmindful that hypothetical situations can be conjured up, shading imperceptibly from the circumstances of this case and by gradations producing practical differences despite seemingly logical extensions. But the Constitution is “intended to preserve practical and substantial rights, not to maintain theories.” <em>Davis </em>v. <em>Mills, </em><span class="citation" data-id="96108"><a href="/opinion/96108/davis-v-mills/#457" aria-description="Citation for case: Davis v. Mills">194 U. S. 451, 457</a></span>.</p>
<p id="b250-8">On the facts of this case the’ conviction of the petitioner has been obtained by methods that offend the Due Process Clause. The judgment below must be</p>
<p id="b250-9">
<em>Reversed.</em>
</p>
<judges id="b250-10">Mr. Justice Minton took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b243-4"> The petition for a hearing is addressed to the discretion of the California Supreme Court and a denial has apparently the same significance as the denial of certiorari in this Court. Cal. Const., Art. VI, §§ 4, 4c; “Rules on Appeal,” Rules 28, 29, <span class="citation no-link">36 Cal. 2d 24</span>-25 (1951). See <span class="citation no-link">3 Stan. L. Rev. 243</span>-269 (1951).</p>
</footnote>
<footnote label="2">
<p id="b245-5"> What is here summarized was deemed by a majority of the Court, in <em>Malinski </em>v. <em>New York, </em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>, 412 and 438, to be “the controlling principles upon which' this Court reviews on constitutional grounds a.state court conviction for crime.” They have been applied by this Court many times, long before and since the <em><span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">Malinski</a></span> </em>case.</p>
</footnote>
<footnote label="3">
<p id="b246-6"> This is the federal jury required constitutionally although England and at least half of the States have in some civil cases juries which are composed of less than 12 or whose verdict may be less than unanimous. See County Courts Act, 1934, 24 &amp; 25 Geo. V, c. 53, § 93; Arizona State Legislative Bureau, Legislative Briefs No. 4, Grand and Petit Juries in the United States, v-vi (Feb. 15, 1940); The Council of State Governments, The Book of the States, 1950-1951, 515.</p>
</footnote>
<footnote label="4">
<p id="b246-8"> Burke’s observations' on the method of ascertaining law by judges are pertinent:</p>
<p id="b246-9">“Your committee do not find any positive law which binds the judges of the courts in Westminster-hall publicly to give a reasoned opinion from the bench, in support of their judgment upon matters that are stated before them. But the course- hath prevailed from <page-number citation-index="1" label="171">*171</page-number>the oldest times. It hath been so general and so uniform, that it must be considered as the law of the land.” Report of the Committee of Managers on the Causes of the Duration of Mr. Hastings’s Trial, 4 Speeches of Edmund Burke (1816) 200-201.</p>
<p id="b247-6">And Burke had an answer for those who argue that the liberty of the citizen cannot be- adequately protected by the flexible conception of due process of law:</p>
<p id="b247-8">"... the English jurisprudence has not any other sure foundation, nor consequently the lives and properties of the subject any sure hold, but in the maxims, rules, and principles, and juridical traditionary line of decisions . . . .” <em>Id., </em>at 201.</p>
</footnote>
<footnote label="5">
<p id="b247-9"> Morris R. Cohen, “Jus Naturale Redivivum,” 25 Philosophical Review 761 (1916), and “Natural Rights and Positive Law,” Reason and Nature (1931), 401-426; F. Pollock, “The History of the Law of Nature,” Essays in the Law (1922), 31-79.</p>
</footnote>
<footnote label="6">
<p id="b249-6"> As to the difference between the privilege against self-crimination protected, in federal prosecutions, under the. Fifth Amendment, and the limitations which the Due Process Clause of the Fourteenth Amendment imposes upon the States against the use of coerced confessions, see <em>Brown </em>v. <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi"><em>Mississippi, supra, </em>at 285</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Rogers v. Richmond.md  (`case`, 5 assertions)

### content_page

```
---
title: "Rogers v. Richmond"
type: case
citation: "365 U.S. 534 (1961)"
parallel_cite: "81 S. Ct. 735; 5 L. Ed. 2d 760"
neutral_cite: 1961 U.S. LEXIS 1494
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-03-20
docket: 40
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-03-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rogers v. Richmond
  varies_by_point: false
  scope_note: "Good law; the foundational statement that confession voluntariness is measured by coercion alone, with complete disregard of the confession's probable truth or reliability."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106192/rogers-v-richmond/"
  cluster_id: 106192
  opinion_id: 106192
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Spano v. New York]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "coercion"]
holding: "A confession's admissibility under the Due Process Clause turns solely on whether police coercion overbore the suspect's will; the confession's probable truth or reliability is constitutionally irrelevant, and a voluntariness standard that takes reliability into account is invalid."
lake:
  record_id: Rogers v. Richmond
  status: verified
  projected_at: 2026-07-06
---

# Rogers v. Richmond

*365 U.S. 534 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Rogers was convicted of first-degree murder in Connecticut, his conviction resting in significant part on confessions obtained during sustained police interrogation — questioning during which officers told Rogers they were about to bring his wife in for questioning. In ruling the confessions admissible, the state trial judge (affirmed by the Supreme Court of Errors) applied a voluntariness standard that took into account the probable truth or falsity — the reliability — of the confessions. Rogers sought federal [[Common Legal Terms#habeas-corpus|habeas corpus]].

## Issue
Whether a confession's admissibility under the Due Process Clause may be judged by a standard that takes into account the probable truth or reliability of the confession.

## Rule
No. Voluntariness is measured by coercion alone, never by reliability. "[C]onvictions following the admission into evidence of confessions which are involuntary, *i.e.*, the product of coercion, either physical or psychological, cannot stand. This is so not because such confessions are unlikely to be true but because the methods used to extract them offend an underlying principle in the enforcement of our criminal law: that ours is an accusatorial and not an inquisitorial system." — 365 U.S. at 540–541. ^pin-540

The inquiry must therefore disregard the confession's truth entirely: "The attention of the trial judge should have been focused, for purposes of the Federal Constitution, on the question whether the behavior of the State's law enforcement officials was such as to overbear petitioner's will to resist and bring about confessions not freely self-determined—a question to be answered with complete disregard of whether or not petitioner in fact spoke the truth." — *Id.* at 544. ^pin-544

## Application
The Connecticut courts had answered the admissibility question "by reference to a legal standard which took into account the circumstance of probable truth or falsity." Because that standard injected reliability into an inquiry that the Due Process Clause confines to whether coercion overbore Rogers's will, the standard was constitutionally invalid, and the conviction obtained under it could not stand. The Court did not itself decide whether Rogers's confessions were in fact voluntary; the error was the use of the wrong standard.

## Conclusion
A voluntariness standard that takes the confession's reliability into account is invalid under the Fourteenth Amendment. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] for application of the correct, coercion-only standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Rogers* refines the due-process confession line rooted in [[Brown v. Mississippi]] and [[Chambers v. Florida]], isolating coercion (not reliability) as the constitutional test — the same psychological-coercion concern later developed in [[Spano v. New York]]. The requirement that there be coercive police activity at all was later underscored in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Rogers v. Richmond*, 365 U.S. 534 (1961) — https://www.courtlistener.com/opinion/106192/rogers-v-richmond/ — pinpoints: 540–541, 544.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e8abab053ed4a186", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "365 U.S. 534 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 1494", "official_citation_present": true, "parallel_cite": "81 S. Ct. 735; 5 L. Ed. 2d 760", "title": "Rogers v. Richmond", "year": "1961"}}
{"assertion_id": "806716094f06961d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession's admissibility under the Due Process Clause turns solely on whether police coercion overbore the suspect's will; the confession's probable truth or reliability is constitutionally irrelevant, and a voluntariness standard that takes reliability into account is invalid.", "title": "Rogers v. Richmond"}}
{"assertion_id": "c73a5c1814cdbf18", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Rogers v. Richmond"}}
{"assertion_id": "84b466bf21c1fd0a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1961-03-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Rogers v. Richmond", "field_i_validity": "good_law", "scope_note": "Good law; the foundational statement that confession voluntariness is measured by coercion alone, with complete disregard of the confession's probable truth or reliability.", "title": "Rogers v. Richmond", "varies_by_point": "false"}}
{"assertion_id": "8e610038e5b0f86f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rogers v. Richmond"}}
```

### lake record — Rogers v. Richmond

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rogers v. Richmond",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rogers v. Richmond",
    "case_name_short": "Richmond",
    "case_name_full": "Rogers v. Richmond, Warden",
    "input_case_name": "Rogers v. Richmond",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-03-20",
    "year": 1961,
    "docket": "40",
    "cluster_id": 106192,
    "lead_opinion_id": 106192,
    "sibling_ids": [
      106192,
      9422147,
      9422148
    ],
    "absolute_url": "/opinion/106192/rogers-v-richmond/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 534",
      "volume": "365",
      "reporter": "U.S.",
      "page": "534",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 735",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 760",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "760",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1494",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1494",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 534",
        "volume": "365",
        "reporter": "U.S.",
        "page": "534",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 735",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 760",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "760",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1494",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1494",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 534",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 534",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-540",
      "page": null,
      "quote": "--- # Rogers v. Richmond *365 U.S. 534 (1961)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Rogers was convicted of first-degree murder in Connecticut, his conviction resting in significant part on confessions obtained during sustained police interrogation \u2014 questioning during which officers told Rogers they were about to bring his wife in for questioning. In ruling the confessions admissible, the state trial judge (affirmed by the Supreme Court of Errors) applied a voluntariness standard that took into account the probable truth or falsity \u2014 the reliability \u2014 of the confessions. Rogers sought federal habeas corpus. ## Issue Whether a confession's admissibility under the Due Process Clause may be judged by a standard that takes into account the probable truth or reliability of the confession. ## Rule No. Voluntariness is measured by coercion alone, never by reliability.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-544",
      "page": null,
      "quote": "The attention of the trial judge should have been focused, for purposes of the Federal Constitution, on the question whether the behavior of the State's law enforcement officials was such as to overbear petitioner's will to resist and bring about confessions not freely self-determined\u2014a question to be answered with complete disregard of whether or not petitioner in fact spoke the truth.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-03-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rogers v. Richmond",
    "varies_by_point": false,
    "scope_note": "Good law; the foundational statement that confession voluntariness is measured by coercion alone, with complete disregard of the confession's probable truth or reliability.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Amended September 20, 2016 State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 4472001,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 3218790,
          "cite": [
            "882 N.W.2d 68",
            "2016 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane1_negative"
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
        "journal_ref": "Rogers v. Richmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fernandez-Torres \u2013 (",
          "cluster_id": 2745409,
          "cite": [
            "50 Kan. App. 2d 1069",
            "337 P.3d 691"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Osvaldo Estrada Torres v. State",
          "cluster_id": 3102296,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basciano",
          "cluster_id": 2470094,
          "cite": [
            "763 F. Supp. 2d 303",
            "2011 U.S. Dist. LEXIS 2901",
            "2011 WL 114865"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane1_negative"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re GAULT",
          "cluster_id": 107439,
          "cite": [
            "18 L. Ed. 2d 527",
            "87 S. Ct. 1428",
            "387 U.S. 1",
            "1967 U.S. LEXIS 1478",
            "40 Ohio Op. 2d 378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Townsend v. Sain",
          "cluster_id": 106544,
          "cite": [
            "9 L. Ed. 2d 770",
            "83 S. Ct. 745",
            "372 U.S. 293",
            "1963 U.S. LEXIS 1941"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pate v. Robinson",
          "cluster_id": 107184,
          "cite": [
            "15 L. Ed. 2d 815",
            "86 S. Ct. 836",
            "383 U.S. 375",
            "1966 U.S. LEXIS 2113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hilton v. Braunskill",
          "cluster_id": 111892,
          "cite": [
            "95 L. Ed. 2d 724",
            "107 S. Ct. 2113",
            "481 U.S. 770",
            "1987 U.S. LEXIS 2258",
            "55 U.S.L.W. 4672",
            "7 Fed. R. Serv. 3d 1149"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Murray",
          "cluster_id": 111728,
          "cite": [
            "91 L. Ed. 2d 434",
            "106 S. Ct. 2661",
            "477 U.S. 527",
            "1986 U.S. LEXIS 67",
            "54 U.S.L.W. 4833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
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
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Texas",
          "cluster_id": 107342,
          "cite": [
            "17 L. Ed. 2d 606",
            "87 S. Ct. 648",
            "385 U.S. 554",
            "1967 U.S. LEXIS 2453"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haynes v. Washington",
          "cluster_id": 106625,
          "cite": [
            "10 L. Ed. 2d 513",
            "83 S. Ct. 1336",
            "373 U.S. 503",
            "1963 U.S. LEXIS 1439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rogers v. Richmond:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106192 OR 9422147 OR 9422148) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDI4ODUxMjAwMDAwJnM9MTA3NDE0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106192+OR+9422147+OR+9422148%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106192 OR 9422147 OR 9422148)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MzImcz0xMDc4NzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106192+OR+9422147+OR+9422148%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106192 OR 9422147 OR 9422148)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106192 OR 9422147 OR 9422148)",
    "indexed_citing_opinions": 946,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106192,
        "count": 872,
        "count_source": "search"
      },
      {
        "opinion_id": 9422147,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9422148,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1414,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rogers-v-richmond.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1NzMwMzImcz01MzQzNjU1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106192+OR+9422147+OR+9422148%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106192,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 105726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 106017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 249138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 1931233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 1931753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 2078219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 2206154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 2281960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3317814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3318457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3318540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3318798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3319000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3319048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106192,
        "cited_id": 3321240,
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
    "date_created": "2026-07-05T17:44:18Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:44:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:44:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:44:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rogers v. Richmond

```
<div>
<center><b><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U.S. 534</a></span> (1961)</b></center>
<center><h1>ROGERS<br>
v.<br>
RICHMOND, WARDEN.</h1></center>
<center>No. 40.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 8-9, 1960.</center>
<center>Decided March 20, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Louis H. Pollak</i> and <i>Jacob D. Zeldes</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Abraham S. Ullman,</i> State's Attorney for Connecticut, and <i>Robert C. Zampano</i> argued the cause for respondent. With them on the brief was <i>Arthur T. Gorman,</i> Assistant State's Attorney.</p>
<p>MR. JUSTICE FRANKFURTER delivered the opinion of the Court.</p>
<p>This case has a long history. It must be told with some particularity in order to unravel issues ensnarled in protracted litigation in both state and federal courts, turning essentially on the admissibility of confessions.</p>
<p><span class="star-pagination">*535</span> <i>The Trial.</i>Petitioner was found guilty of murder by a jury in the Superior Court, New Haven County, Connecticut. The undisputed evidence leading to the conviction may be briefly told. On January 9, 1954, New Haven, Connecticut, police arrested petitioner on charges of committing attempted robbery and other crimes on that day at a local hotel. At the time of his arrest petitioner had in his possession a revolver. Subsequent ballistic tests tended to show that this weapon, which had been reported stolen from the home of petitioner's nephew, was used in a fatal shooting during a liquor store robbery in West Haven, Connecticut, on November 21, 1953, the same day its disappearance was discovered.</p>
<p>Petitioner was lodged in the New Haven County Jail pending trial on the charges that prompted his arrest. On January 30, 1954, he was transported without court order from the jail to the office of the State's Attorney for questioning in connection with the West Haven killing. The interrogation commenced at approximately 2 p.m. of that day and continued throughout the afternoon and evening. During the interrogation petitioner was allowed to smoke, was brought a sandwich and coffee, and was at no time subjected to violence or threat of violence.</p>
<p>After petitioner had been intermittently questioned without success by a team of at least three police officers from 2 p. m. to 8 p. m., New Haven Assistant Chief of Police Eagan was called in to conduct the investigation. When petitioner persisted in his denial that he had done the shooting, Chief Eagan pretended, in petitioner's hearing, to place a telephone call to police officers, directing them to stand in readiness to bring in petitioner's wife for questioning. After the passage of approximately one hour, during which petitioner remained silent, Chief Eagan indicated that he was about to have petitioner's wife taken into custody. At this point petitioner <span class="star-pagination">*536</span> announced his willingness to confess and did confess in a statement which was taken down in shorthand by an official court reporter.</p>
<p>The following morning the Coroner of New Haven County issued an order that petitioner be held incommunicado at the jail. When a lawyer associated with counsel whom petitioner had previously retained to defend him on the attempted robbery charge called at the jail to see petitioner, he was turned away on the authority of the Coroner's order. Petitioner was then transported to the County Court House for interrogation by the Coroner, who had been informed of his confession of the previous night. There he was put on oath to tell the truth but warned that he might refuse to say anything further and advised that he might obtain the assistance of counsel. Petitioner again confessed to the shooting in a statement recorded by the same official court reporter.</p>
<p>Petitioner's defense at the trial was directed toward discrediting the confessions as the product of coercion. In accordance with Connecticut practice, see, <i>e. g., </i><i>State</i> v. <i>Willis,</i> <span class="citation" data-id="6584340"><a href="/opinion/6704212/state-v-willis/" aria-description="Citation for case: State v. Willis">71 Conn. 293</a></span>, <span class="citation" data-id="6584340"><a href="/opinion/6704212/state-v-willis/" aria-description="Citation for case: State v. Willis">41 A. 820</a></span>; <i>State</i> v. <i>Guastamachio,</i> <span class="citation" data-id="1931233"><a href="/opinion/1931233/state-v-guastamachio/" aria-description="Citation for case: State v. Guastamachio">137 Conn. 179</a></span>, <span class="citation" data-id="1931233"><a href="/opinion/1931233/state-v-guastamachio/" aria-description="Citation for case: State v. Guastamachio">75 A. 2d 429</a></span>, the trial judge heard the evidence bearing on admissibility of the confessions without the jury present. At this hearing petitioner testified that shortly after the commencement of the interrogation he asked to see a lawyer but was never permitted to do so. He also testified, with reference to Chief Eagan's pretense of bringing petitioner's wife in for questioning, that this move took the form of a threat to do so unless he confessed and that in making this threat Chief Eagan told him that he would be "less than a man" if he failed to confess and thereby caused her to be taken into custody. According to petitioner his wife suffered from arthritis, and he confessed to spare her being transported to the scene of the interrogation.</p>
<p><span class="star-pagination">*537</span> The State met petitioner's account with the testimony of Chief Eagan. He testified that petitioner made no request to see a lawyer during his presence in the room. However, it will be recalled that Chief Eagan did not arrive until the questioning had run a course of six hours and that petitioner claimed to have requested counsel during that period. Chief Eagan also denied that he had framed his remarks about bringing petitioner's wife in for questioning as a threat or that he had suggested that petitioner would be "less than a man," etc.</p>
<p>On the basis of the evidence summarized, the trial judge concluded that the confessions were voluntary and allowed them to go to the jury for consideration of the weight to be given them under all the circumstances that led to them. Conviction of petitioner for murder followed.</p>
<p><i>Review by the Connecticut Supreme Court.</i>On appeal, the Supreme Court of Errors of Connecticut, finding no error in the trial judge's admission of the confessions, affirmed the conviction, <i>State</i> v. <i>Rogers,</i> <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/" aria-description="Citation for case: State v. Rogers">143 Conn. 167</a></span>, <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/" aria-description="Citation for case: State v. Rogers">120 A. 2d 409</a></span>.</p>
<p><i>First Federal Habeas Corpus Proceeding.</i>In August of 1956, after satisfying the rule of <i>Darr</i> v. <i>Burford,</i> <span class="citation" data-id="9420460"><a href="/opinion/104779/darr-v-burford/" aria-description="Citation for case: Darr v. Burford">339 U. S. 200</a></span>, petitioner sought a federal writ of habeas corpus, basically on the ground that since the confessions were secured under circumstances rendering them constitutionally inadmissible, he was denied due process of law under the Fourteenth Amendment. The United States District Court for the District of Connecticut held a hearing based on the evidence offered by the parties. This evidence included excerpts from the record of the state proceedings as well as testimony of petitioner and various state officials. Neither petitioner nor respondent submitted the entire transcript of the state proceedings and the district judge did not call for it. Petitioner again testified that before he confessed he had requested an opportunity <span class="star-pagination">*538</span> to confer with his lawyer. His testimony was flatly contradicted by three police officers called by the State's Attorney, none of whom had testified at the trial.</p>
<p>On the testimony before him, the district judge made findings which differed from those of the state trial judge in several important respects. He accepted petitioner's testimony that during the police interrogation he had asked to see his lawyer before he yielded to Chief Eagan's efforts to have him confess. He also found that the confession before the Coroner was the product of fear that repudiation of the earlier confession would lead the police to take his wife and foster children into custody. Accordingly, he concluded that "The confessions were the result of pressure overcoming Rogers' powers of resistance and were not voluntary on his part." <i>United States ex rel. Rogers</i> v. <i>Cummings,</i> <span class="citation" data-id="8725093"><a href="/opinion/8741840/united-states-ex-rel-rogers-v-cummings/#665" aria-description="Citation for case: United States ex rel. Rogers v. Cummings">154 F. Supp. 663, 665</a></span>. He therefore set aside the judgment of conviction.</p>
<p><i>First Court of Appeals Review.</i>On appeal, the United States Court of Appeals for the Second Circuit vacated the District Court's judgment, finding that it was error to hold a hearing <i>de novo</i> on issues of basic evidentiary fact that had been considered and adjudicated by the state courts. Relying on <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>, the Court of Appeals concluded that the district judge should have called for the entire state record before reaching his decision. It held</p>
<blockquote>"that in the case now before us the nature of the issues presented and proper regard for the delicate balance of federal-state relationships required the District Judge to obtain and examine the State proceedings. . . . Only on an adequate state record can the District Court determine if a vital flaw exists which warrants correction by extrinsic evidence." <i>United States ex rel. Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9446051"><a href="/opinion/244398/united-states-ex-rel-harold-d-rogers-relator-appellee-v-mark-s/#810" aria-description="Citation for case: United States Ex Rel. Harold D. Rogers, Relator-Appellee...">252 F. 2d 807, 810, 811</a></span>.</blockquote>
<p><span class="star-pagination">*539</span> The Court of Appeals remanded the case to the District Court with the following instructions:</p>
<blockquote>"Unless the judge below shall find in the record thus before him material which he deems to constitute `vital flaws' and `unusual circumstances' within the meaning of Brown v. Allen, we hold that he should make the necessary constitutional determinations exclusively on the basis of the historical facts as found by the State trial court." <span class="citation" data-id="9446051"><a href="/opinion/244398/united-states-ex-rel-harold-d-rogers-relator-appellee-v-mark-s/#811" aria-description="Citation for case: United States Ex Rel. Harold D. Rogers, Relator-Appellee...">252 F. 2d, at 811</a></span>.</blockquote>
<p><i>Certiorari Proceeding.</i>The petitioner sought certiorari here and we denied the petition with this <i>per curiam</i> opinion:</p>
<blockquote>"The petition for writ of certiorari is denied. We read the opinion of the Court of Appeals as holding that while the District Judge may, unless he finds a vital flaw in the State Court proceedings, accept the determination in such proceedings, he need not deem such determination binding, and may take testimony. See <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 506</a></span>, <i>et seq.</i>" <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="105726"><a href="/opinion/105726/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">357 U. S. 220</a></span>.</blockquote>
<p><i>Second Federal Habeas Corpus Proceeding.</i>On remand, the district judge had before him the entire transcript of the state proceedings and on the basis of it dismissed the petition. <i>United States ex rel. Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="8729568"><a href="/opinion/8746305/united-states-ex-rel-rogers-v-richmond/" aria-description="Citation for case: United States ex rel. Rogers v. Richmond">178 F. Supp. 69</a></span>. While he adhered to his belief in petitioner's testimony in the first habeas corpus hearing, he now considered himself obliged to accept the state court's "Findings," rather than his own, on all points of historical fact "unless some vital flaw or unusual circumstance exists or some other basis appears for consideration of testimony outside the record." <span class="citation" data-id="8729568"><a href="/opinion/8746305/united-states-ex-rel-rogers-v-richmond/#71" aria-description="Citation for case: United States ex rel. Rogers v. Richmond">178 F. Supp., at 71-72</a></span>. The district judge found no such "flaw" or "circumstance" to permit retrial of the issue of the voluntariness of the confessions. He thus stated his position:</p>
<blockquote>"The issue of whether request for counsel was made and the issue of voluntary character of the confessions <span class="star-pagination">*540</span> were fully and conscientiously tried by an experienced judge. Subsequent disagreement with his weighing of essentially similar evidence is not in itself sufficient under the limitations now imposed in the interest of proper balance in our dual court system, to permit consideration of the matter heard at the trial of the issue de novo here." <span class="citation" data-id="8729568"><a href="/opinion/8746305/united-states-ex-rel-rogers-v-richmond/#73" aria-description="Citation for case: United States ex rel. Rogers v. Richmond">178 F. Supp., at 73</a></span>.</blockquote>
<p>On this basis the district judge could not find that the confessions were the product of coercion.</p>
<p><i>Second Court of Appeals Review.</i>The Court of Appeals for the Second Circuit affirmed this judgment, one judge dissenting. <i>United States ex rel. Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9447054"><a href="/opinion/249138/united-states-ex-rel-harold-d-rogers-relator-appellant-v-mark-s/" aria-description="Citation for case: United States Ex Rel. Harold D. Rogers, Relator-Appellant...">271 F. 2d 364</a></span>. The court held that the district judge was correct in restricting himself to the state court's "Findings" regarding petitioner's request to see his lawyer before confessing, and agreed with him that the facts in the record did not justify the conclusion that petitioner's confessions were not voluntary.</p>
<p>Because issues concerning the appropriate procedure for dealing with petitions for federal habeas corpus in relation to state convictions were urged, we brought the case here. <span class="citation multiple-matches"><a href="/c/U.%20S./361/959/">361 U. S. 959</a></span>.</p>
<p>A critical analysis of the Connecticut proceedings leads to disposition of the case on a more immediate issue. For it compels the conclusion that the trial judge in admitting the confessions as "voluntary," and the Supreme Court of Errors in affirming the conviction into which the confessions entered, failed to apply the standard demanded by the Due Process Clause of the Fourteenth Amendment for determining the admissibility of a confession.</p>
<p>Our decisions under that Amendment have made clear that convictions following the admission into evidence of confessions which are involuntary, <i>i. e.,</i> the product of coercion, either physical or psychological, cannot stand. This is so not because such confessions are unlikely to be <span class="star-pagination">*541</span> true but because the methods used to extract them offend an underlying principle in the enforcement of our criminal law: that ours is an accusatorial and not an inquisitorial systema system in which the State must establish guilt by evidence independently and freely secured and may not by coercion prove its charge against an accused out of his own mouth. See <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span>; <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172-174</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 320-321</a></span>; <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206-207</a></span>. And see <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54-55</a></span>. To be sure, confessions cruelly extorted may be and have been, to an unascertained extent, found to be untrustworthy. But the constitutional principle of excluding confessions that are not voluntary does not rest on this consideration. Indeed, in many of the cases in which the command of the Due Process Clause has compelled us to reverse state convictions involving the use of confessions obtained by impermissible methods, independent corroborating evidence left little doubt of the truth of what the defendant had confessed. Despite such verification, confessions were found to be the product of constitutionally impermissible methods in their inducement. Since a defendant had been subjected to pressures to which, under our accusatorial system, an accused should not be subjected, we were constrained to find that the procedures leading to his conviction had failed to afford him that due process of law which the Fourteenth Amendment guarantees.</p>
<p>In the present case, while the trial judge ruled that each of petitioner's confessions was "freely and voluntarily made and accordingly was admissible in evidence," he reached that conclusion on the basis of considerations that undermine its validity. He found that the pretense of bringing petitioner's wife in for questioning "had no tendency to produce a confession that was not in accord <span class="star-pagination">*542</span> with the truth." Again, in his charge to the jury, he thus enunciated the reasoning which had guided him in admitting the confessions for its consideration:</p>
<blockquote>"No confession or admission of an accused is admissible in evidence unless made freely and voluntarily and not under the influence of promises or threats. The fact that a confession was procured by the employment of some artifice or deception does not exclude the confession if it was not calculated, that is to say, if the artifice or deception was not calculated to procure an untrue statement. The motive of a person in confessing is of no importance provided the particular confession does not result from threats, fear or promises made by persons in actual or seeming authority. The object of evidence is to get at the truth, and a trick or device which has no tendency to produce a confession except one in accordance with the truth does not render the confession inadmissible . . . . The rules which surround the use of a confession are designed and put into operation because of the desire expressed in the law that the confession, if used, be probably a true confession."</blockquote>
<p>The same viewthat the probable reliability of a confession is a circumstance of weight in determining its voluntariness entered the opinion of the Supreme Court of Errors of Connecticut in sustaining the trial judge's admission of the confession:</p>
<blockquote>"If we concede that this [petitioner's claims of illegal removal from jail and incommunicado detention] was all true and that such conduct was unlawful, it does not, standing alone, render the defendant's confessions inadmissible. The question is whether, under these and other circumstances of the case, that conduct induced the defendant to confess falsely that he <span class="star-pagination">*543</span> had committed the crime being investigated. Unless it did, it cannot be said that its illegality vitiated his confessions." <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#173" aria-description="Citation for case: State v. Rogers">143 Conn., at 173</a></span>; <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#412" aria-description="Citation for case: State v. Rogers">120 A. 2d, at 412</a></span>.</blockquote>
<p>And again:</p>
<blockquote>"Proper court authorization should have been secured before the defendant was removed from the jail. There is nothing about his illegal removal, however, to demonstrate that he was thereby forced to make an untrue statement. The same can be said concerning the refusal to admit counsel to see the defendant on the morning of January 31 before he was brought before the coroner." <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#173" aria-description="Citation for case: State v. Rogers">143 Conn., at 173-174</a></span>; <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#412" aria-description="Citation for case: State v. Rogers">120 A. 2d, at 412</a></span>.</blockquote>
<p>Concerning the feigned phone call that petitioner's wife be brought in to headquarters, the Supreme Court concluded:</p>
<blockquote>"Here again, the question for the court to decide was whether this conduct induced the defendant to make an involuntary and hence untrue statement." <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#174" aria-description="Citation for case: State v. Rogers">143 Conn., at 174</a></span>; <span class="citation" data-id="9712232"><a href="/opinion/2078219/state-v-rogers/#412" aria-description="Citation for case: State v. Rogers">120 A. 2d, at 412</a></span>.</blockquote>
<p>From a fair reading of these expressions, we cannot but conclude that the question whether Rogers' confessions were admissible into evidence was answered by reference to a legal standard which took into account the circumstance of probable truth or falsity.<sup>[1]</sup> And this is not a <span class="star-pagination">*544</span> permissible standard under the Due Process Clause of the Fourteenth Amendment. The attention of the trial judge should have been focused, for purposes of the Federal Constitution, on the question whether the behavior of the State's law enforcement officials was such as to overbear petitioner's will to resist and bring about confessions not freely self-determineda question to be answered with complete disregard of whether or not petitioner in fact spoke the truth. The employment instead, by the trial judge and the Supreme Court of Errors, of a standard infected by the inclusion of references to probable reliability resulted in a constitutionally invalid conviction, pursuant to which Rogers is now detained "in violation of the Constitution."<sup>[2]</sup> A defendant has the right to be <span class="star-pagination">*545</span> tried according to the substantive and procedural due process requirements of the Fourteenth Amendment. This means that a vital confession, such as is involved in this case, may go to the jury only if it is subjected to screening in accordance with correct constitutional standards. To the extent that in the trial of Rogers evidence was allowed to go to the jury on the basis of standards that departed from constitutional requirements, to that extent he was unconstitutionally tried and the conviction was vitiated by error of constitutional dimension.<sup>[3]</sup></p>
<p>It is not for this Court, any more than for a Federal District Court, in habeas corpus proceedings, to make an independent appraisal of the legal significance of facts gleaned from the record after such a conviction. We are barred from speculatingit would be an irrational processabout the weight attributed to the impermissible consideration of truth and falsity which, entering into the Connecticut trial court's deliberations concerning the admissibility of the confessions, may well have distorted, by putting in improper perspective, even its findings of historical fact. Any consideration of this "reliability" element was constitutionally precluded, precisely because the force which it carried with the trial judge cannot be known.</p>
<p>As a matter of abstract logic it is arguable that Rogers may not have been deprived of a constitutional right, nor held in custody in violation of the Constitution, within <span class="citation no-link">28 U. S. C. § 2241</span> (c) (3), solely because the Connecticut trial court applied an impermissible constitutional standard <span class="star-pagination">*546</span> in admitting his confessionthat Rogers was not so deprived, or so held, unless "in fact" his confession was coerced, a "fact" to be ascertained from the state record on direct review here, or <i>de novo</i> by a federal district judge in habeas corpus proceedings. Such a view ignores both the volatile and amorphous character of "fact" as fact is found by courts, and the distributive functions of the dual judicial system in our federalism for the finding of fact and the application of law to fact. In coerced confession cases coming directly to this Court from the highest court of a State in which review may be had, we look for "fact" to the undisputed, the uncontested evidence of record. See <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#50" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 50-52</a></span>. This is all that we may look to, in the absence of detailed state-court findings of historical fact, because this Court cannot sit as a trial tribunal to hear and assess the credibility of witnesses. Of course, so-called facts and their constitutional significance may be so blended that they cannot be severed in consideration. And in any event, there must be a foundation in fact for the legal result. See <i>Thompson</i> v. <i>Louisville,</i> <span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U. S. 199</a></span>. With due regard to these considerations, it would be manifestly unfair, and afford niggardly protection for federal constitutional rights, were we to sustain a state conviction in which the trial judge or trial jurywhichever is charged by state law with the duty of finding fact pertinent to a claim of coercionpasses upon that claim under an erroneous standard of constitutional law.<sup>[4]</sup> In such a case, to look <span class="star-pagination">*547</span> to the wholly undisputed evidence, in the event conflicting evidence is presented, would deprive the state criminal defendant of the benefit of whatever credit his testimony might have been given by the state judge or the state jury, had the judge or jury employed a proper legal standard. Nor, in a case where specific findings are made concerning the allegedly coercive circumstances, can those findings be fairly looked to for the "facts," since findings of fact may often be (to what extent, in a particular case, cannot be known) influenced by what the finder is looking for. Historical facts "found" in the perspective framed by an erroneous legal standard cannot plausibly be expected to furnish the basis for correct conclusions if and merely because a correct standard is later applied to them.</p>
<p>Of course, where the issue of coercion is raised not on direct review in this Court but by petition for habeas corpus in a Federal District Court, one alternative method of proceeding impossible on direct review is available. The District Court might conceivably hold a hearing <i>de novo</i> on the issue of coercion. But such a procedure would neither adequately protect the federal rights of state criminal defendants nor duly take account of the large leeway which must be left to the States in their administration of their own criminal justice. A state defendant should have the opportunity to have all issues which may be determinative of his guilt tried by a state judge or a state jury under appropriate state procedures <span class="star-pagination">*548</span> which conform to the requirements of the Fourteenth Amendment. Where he has not had that opportunity he should not be required to establish in a Federal District Court, before a federal district judge who must consider the issue of the voluntariness of the confession in a certain abstraction from the whole, living complex of a criminal trial, and perhaps many years after the occurrence of the events surrounding the confession, facts establishing coercion. On the other hand, the State, too, has a weighty interest in having valid federal constitutional criteria applied in the administration of its criminal law by its own courts and juries. To require a federal judge exercising habeas corpus jurisdiction to attempt to combine within himself the proper functions of judge and jury in a state trialto ask him to approximate the sympathies of the defendant's peers or to make the rulings which the state trial judge might make, within the exercise of his discretion concerning the admission of evidence at the borderline of constitutional permissibilityis potentially to prejudice state defendants claiming federal rights and to pre-empt functions that belong to state machinery in the administration of state criminal law.</p>
<p>In view, therefore, of the constitutionally inadequate test applied by the Connecticut courts for determining whether the confessions were voluntarily given, we need not, on this record, consider whether the circumstances of the interrogation and the manner in which it was pressed barred admissibility of the confessions as a matter of federal law.<sup>[5]</sup> In the case before us, the state trial court <span class="star-pagination">*549</span> misconstrued the applicable law of the Constitution and was sustained in doing so by Connecticut's Supreme Court. It was error for the court below to affirm the District Court's denial of petitioner's application for habeas corpus. The case is remanded to the Court of Appeals to be held in order to give the State opportunity to retry petitioner, in light of this opinion, within a reasonable time. In default thereof the petitioner is to be discharged.</p>
<p><i>Reversed.</i></p>
<h2>NOTES</h2>
<p>[1]  We find support for this conclusion in a line of Connecticut cases, some of which are cited by the Supreme Court of Errors in <i>Rogers.</i> See <i>State</i> v. <i>Willis,</i> <span class="citation" data-id="6584340"><a href="/opinion/6704212/state-v-willis/#307" aria-description="Citation for case: State v. Willis">71 Conn. 293, 307-312</a></span>, <span class="citation" data-id="6584340"><a href="/opinion/6704212/state-v-willis/#824" aria-description="Citation for case: State v. Willis">41 A. 820, 824-826</a></span>; <i>State</i> v. <i>Cross,</i> <span class="citation" data-id="3319048"><a href="/opinion/3323766/state-v-cross/#727" aria-description="Citation for case: State v. Cross">72 Conn. 722, 727</a></span>, <span class="citation" data-id="3319048"><a href="/opinion/3323766/state-v-cross/#150" aria-description="Citation for case: State v. Cross">46 A. 148, 150</a></span>; <i>State</i> v. <i>DiBattista,</i> <span class="citation" data-id="3317814"><a href="/opinion/3322574/state-v-dibattista/#563" aria-description="Citation for case: State v. Dibattista">110 Conn. 549, 563</a></span>, <span class="citation" data-id="3317814"><a href="/opinion/3322574/state-v-dibattista/#669" aria-description="Citation for case: State v. Dibattista">148 A. 664, 669</a></span>; <i>State</i> v. <i>Palko,</i> <span class="citation" data-id="3318540"><a href="/opinion/3323275/state-v-palko/#680" aria-description="Citation for case: State v. Palko">121 Conn. 669, 680</a></span>, <span class="citation" data-id="3318540"><a href="/opinion/3323275/state-v-palko/#662" aria-description="Citation for case: State v. Palko">186 A. 657, 662</a></span>; <i>State</i> v. <i>Tomassi,</i> <span class="citation" data-id="1931753"><a href="/opinion/1931753/state-v-tomassi/#127" aria-description="Citation for case: State v. Tomassi">137 Conn. 113, 127-128</a></span>, <span class="citation" data-id="1931753"><a href="/opinion/1931753/state-v-tomassi/#74" aria-description="Citation for case: State v. Tomassi">75 A. 2d 67, 74</a></span>; <i>State</i> v. <i>Guastamachio,</i> <span class="citation" data-id="1931233"><a href="/opinion/1931233/state-v-guastamachio/#182" aria-description="Citation for case: State v. Guastamachio">137 Conn. 179, 182</a></span>, <span class="citation" data-id="1931233"><a href="/opinion/1931233/state-v-guastamachio/#431" aria-description="Citation for case: State v. Guastamachio">75 A. 2d 429, 431</a></span>; <i>State</i> v. <i>Lorain,</i> <span class="citation" data-id="2206154"><a href="/opinion/2206154/state-v-lorain/#700" aria-description="Citation for case: State v. Lorain">141 Conn. 694, 700</a></span>, <span class="citation" data-id="2206154"><a href="/opinion/2206154/state-v-lorain/#507" aria-description="Citation for case: State v. Lorain">109 A. 2d 504, 507</a></span>. But see <i>State</i> v. <i>Wakefield,</i> <span class="citation" data-id="3319000"><a href="/opinion/3323719/state-v-wakefield/" aria-description="Citation for case: State v. Wakefield">88 Conn. 164</a></span>, <span class="citation" data-id="3319000"><a href="/opinion/3323719/state-v-wakefield/" aria-description="Citation for case: State v. Wakefield">90 A. 230</a></span>; <i>State</i> v. <i>Castelli,</i> <span class="citation" data-id="3318457"><a href="/opinion/3323195/state-v-castelli/" aria-description="Citation for case: State v. Castelli">92 Conn. 58</a></span>, <span class="citation" data-id="3318457"><a href="/opinion/3323195/state-v-castelli/" aria-description="Citation for case: State v. Castelli">101 A. 476</a></span>; <i>State</i> v. <i>Zukauskas,</i> <span class="citation" data-id="3318798"><a href="/opinion/3323526/state-v-zukauskas/" aria-description="Citation for case: State v. Zukauskas">132 Conn. 450</a></span>, <span class="citation" data-id="3318798"><a href="/opinion/3323526/state-v-zukauskas/" aria-description="Citation for case: State v. Zukauskas">45 A. 2d 289</a></span>; <i>State</i> v. <i>Buteau,</i> <span class="citation" data-id="3321240"><a href="/opinion/3325864/state-v-buteau/" aria-description="Citation for case: State v. Buteau">136 Conn. 113</a></span>, <span class="citation" data-id="3321240"><a href="/opinion/3325864/state-v-buteau/" aria-description="Citation for case: State v. Buteau">68 A. 2d 681</a></span>; <i>State</i> v. <i>Malm,</i> <span class="citation" data-id="2281960"><a href="/opinion/2281960/state-v-malm/" aria-description="Citation for case: State v. Malm">142 Conn. 113</a></span>, <span class="citation" data-id="2281960"><a href="/opinion/2281960/state-v-malm/" aria-description="Citation for case: State v. Malm">111 A. 2d 685</a></span>, containing no reference to a "truth-falsity" test. Connecticut case law regarding the admissibility of confessions allegedly secured under circumstances which render them involuntary, or by means of promises, "artifices," "deception" or illegal police practices not amounting to coercion, is not free from uncertainty. We need not now endeavor to ascertain the extent to which, or the circumstances under which, Connecticut courts generally look to reliability as the criterion, alone or in conjunction with other criteria, of admissibility. If petitioner in the present case has been convicted through the use of a constitutionally impermissible standard, it is indifferent that Connecticut law, in its operation in other cases, may be unimpeachable. What that law does reveal of relevance here is that conceptions of probable truth or probable falsity have had and appear still to have a place in the reasoning of Connecticut judges in classes of cases having similarities to <i>Rogers</i> and relied on therein. Without meaning to consider the validity of such reasoning, under the Fourteenth Amendment, in any applications but the one now before us, we do derive from its currency in a continuing line of Connecticut decisions confirmation of our conclusion that the language of the trial judge and of the Supreme Court of Errors in the <i>Rogers</i> case is not the product of mere verbal inadvertence or unreflective phraseology, but an accurate embodiment of the mode of reasoning which led to holding that petitioner's confessions were admissible as "voluntary."</p>
<p>[2]  <span class="citation no-link">28 U. S. C. § 2241</span> (c) (3).</p>
<p>[3]  Determination of the admissibility of confessions is, of course, a matter of local procedure. But whether the question of admissibility is left to the jury or is determinable by the trial judge, it must be determined according to constitutional standards satisfying the Due Process Clause of the Fourteenth Amendment. If the question of admissibility is left to the jury, they must not be misdirected by wrong constitutional standards; if the question is decided by the trial judge, he must not misdirect himself.</p>
<p>[4]  A different question was implicitly presented in <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>. In that case the trial judge permitted the confessions to go to the jury under instructions which told it to disregard them if it found that they were not voluntarily made, and which adequately defined the "voluntariness" required by due process. See <i>Lyons</i> v. <i>Oklahoma,</i> <span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/#601" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596, 601</a></span>. Thus, there was no flaw in the verdict as rendered. An erroneous legal standard for determining the admissibility of allegedly coerced confessions was interjected into the proceeding only at the level of the Supreme Court of California. Had the State Supreme Court, under similar circumstances reversed the conviction, not on the basis of local law but solely by reason of a misinterpretation of this Court's principles governing coerced confessions, and had the case been brought here for review on certiorari, the jury's verdict would have had to be reinstated. In any event, the question presented in <i><span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">Stroble</a></span></i> was not faced squarely, and in illuminating isolation, in that case. Compare <i>Lee</i> v. <i>Mississippi,</i> <span class="citation" data-id="104497"><a href="/opinion/104497/lee-v-mississippi/" aria-description="Citation for case: Lee v. Mississippi">332 U. S. 742</a></span>, with <i><span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">Stroble</a></span>.</i></p>
<p>[5]  We do not deal in this case with a situation in which the record taking all of petitioner's evidence, and the inferences reasonably to be drawn from it, in the light most favorable to himnevertheless fails to make out a claim of coercion. Since the issue of voluntariness might fairly have gone either way on the whole of the testimony, petitioner has clearly been prejudiced by the application of an erroneous standard to his federal claim by the state trial judge in allowing the confessions to go to the jury.</p>

</div>
```

---

## GROUP: content/cases/Rothgery v. Gillespie County.md  (`case`, 5 assertions)

### content_page

```
---
title: "Rothgery v. Gillespie County"
type: case
citation: ""
parallel_cite: "554 U.S. 191; 128 S. Ct. 2578; 171 L. Ed. 2d 366; 21 Fla. L. Weekly Fed. S 429; 76 U.S.L.W. 4520"
neutral_cite: 2008 U.S. LEXIS 5057
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2008
date_decided: 2008-06-23
docket: 07-440
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2008-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rothgery v. Gillespie County
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145785/rothgery-v-gillespie-county/"
  cluster_id: 145785
  opinion_id: 145785
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brewer v. Williams]]", "[[Patterson v. Illinois]]", "[[Kirby v. Illinois]]", "[[Michigan v. Jackson]]", "[[Montejo v. Louisiana]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "attachment", "initial-appearance"]
holding: "A criminal defendant's initial appearance before a magistrate, where he learns the charge against him and his liberty is restricted,…"
lake:
  record_id: Rothgery v. Gillespie County
  status: verified
  projected_at: 2026-07-06
---

# Rothgery v. Gillespie County

*554 U.S. 191 (2008)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Rothgery was arrested as a felon in possession of a firearm (the record was mistaken; he had no felony). At a Texas "article 15.17" hearing, a magistrate informed him of the accusation and committed him to jail in lieu of bail. He repeatedly requested appointed counsel but received none for about six months, until after indictment; with counsel, the charge was dismissed. He sued the county under § 1983, contending the right to counsel had attached at the initial appearance.

## Issue
Whether the Sixth Amendment right to counsel attaches at a defendant's initial appearance before a magistrate, even if no prosecutor was aware of or involved in the arrest or hearing.

## Rule
Attachment occurs at the initial appearance and does not require a prosecutor's involvement. "[A] criminal defendant's initial appearance before a judicial officer, where he learns the charge against him and his liberty is subject to restriction, marks the start of adversary judicial proceedings that trigger attachment of the Sixth Amendment right to counsel." — 554 U.S. at 213. ^pin-213

## Application
Rothgery's article 15.17 hearing — where he learned the charge and his liberty was restricted by commitment to jail in lieu of bail — marked the initiation of adversary judicial proceedings, so his Sixth Amendment right to counsel attached at that point regardless of whether any prosecutor was aware of or involved in the case. The Fifth Circuit erred in holding that a prosecutor's involvement was required for attachment. (The Court's holding was narrow and did not decide whether the six-month delay caused a remediable violation.)

## Conclusion
The right to counsel attached at Rothgery's initial appearance; the Fifth Circuit's judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Rothgery* reaffirms the attachment rule of [[Brewer v. Williams]]/[[Kirby v. Illinois]] and fixes attachment at the initial appearance.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Rothgery v. Gillespie County*, 554 U.S. 191 (2008) — https://www.courtlistener.com/opinion/145785/rothgery-v-gillespie-county/ — pinpoint: 213.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "09c41f2f1d15a9a1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2008 U.S. LEXIS 5057", "official_citation_present": false, "parallel_cite": "554 U.S. 191; 128 S. Ct. 2578; 171 L. Ed. 2d 366; 21 Fla. L. Weekly Fed. S 429; 76 U.S.L.W. 4520", "title": "Rothgery v. Gillespie County", "year": "2008"}}
{"assertion_id": "0757daa4c653cb96", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Rothgery v. Gillespie County"}}
{"assertion_id": "4262db41eae190d1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A criminal defendant's initial appearance before a magistrate, where he learns the charge against him and his liberty is restricted,…", "title": "Rothgery v. Gillespie County"}}
{"assertion_id": "50e7d951d2a2a104", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rothgery v. Gillespie County"}}
{"assertion_id": "d0a4a1c51aca3247", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2008-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Rothgery v. Gillespie County", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Rothgery v. Gillespie County", "varies_by_point": "false"}}
```

### lake record — Rothgery v. Gillespie County

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rothgery v. Gillespie County",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rothgery v. Gillespie County",
    "case_name_short": "Rothgery",
    "case_name_full": "Rothgery v. Gillespie County, Texas",
    "input_case_name": "Rothgery v. Gillespie County",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2008-06-23",
    "year": 2008,
    "docket": "07-440",
    "cluster_id": 145785,
    "lead_opinion_id": 145785,
    "sibling_ids": [
      145785,
      9435183,
      9435184,
      9435185,
      9435186
    ],
    "absolute_url": "/opinion/145785/rothgery-v-gillespie-county/",
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
        "cite": "554 U.S. 191",
        "volume": "554",
        "reporter": "U.S.",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 S. Ct. 2578",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "2578",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "171 L. Ed. 2d 366",
        "volume": "171",
        "reporter": "L. Ed. 2d",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 Fla. L. Weekly Fed. S 429",
        "volume": "21",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "429",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 U.S.L.W. 4520",
        "volume": "76",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. LEXIS 5057",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "5057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "554 U.S. 191",
        "volume": "554",
        "reporter": "U.S.",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 S. Ct. 2578",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "2578",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "171 L. Ed. 2d 366",
        "volume": "171",
        "reporter": "L. Ed. 2d",
        "page": "366",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. LEXIS 5057",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "5057",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 Fla. L. Weekly Fed. S 429",
        "volume": "21",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "429",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "76 U.S.L.W. 4520",
        "volume": "76",
        "reporter": "U.S.L.W.",
        "page": "4520",
        "type": 4,
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
      "id": "pin-213",
      "page": null,
      "quote": "hearing, a magistrate informed him of the accusation and committed him to jail in lieu of bail. He repeatedly requested appointed counsel but received none for about six months, until after indictment; with counsel, the charge was dismissed. He sued the county under \u00a7 1983, contending the right to counsel had attached at the initial appearance. ## Issue Whether the Sixth Amendment right to counsel attaches at a defendant's initial appearance before a magistrate, even if no prosecutor was aware of or involved in the arrest or hearing. ## Rule Attachment occurs at the initial appearance and does not require a prosecutor's involvement.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2008-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rothgery v. Gillespie County",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Scott",
          "cluster_id": 4834608,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
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
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
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
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended August 11, 2017 Roberto Morales Diaz v. State of Iowa",
          "cluster_id": 4471928,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended June 15, 2017 Roberto Morales Diaz v. State of Iowa",
          "cluster_id": 4400500,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended June 12, 2017 Roberto Morales Diaz v. State of Iowa",
          "cluster_id": 4399483,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roberto Morales Diaz v. State of Iowa",
          "cluster_id": 4398775,
          "cite": [
            "896 N.W.2d 723",
            "2017 WL 2491640",
            "2017 Iowa Sup. LEXIS 63"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Neary-French",
          "cluster_id": 4247088,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
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
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shawn Rice",
          "cluster_id": 2772299,
          "cite": [
            "776 F.3d 1021",
            "2015 WL 265459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basciano",
          "cluster_id": 2470094,
          "cite": [
            "763 F. Supp. 2d 303",
            "2011 U.S. Dist. LEXIS 2901",
            "2011 WL 114865"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kerry Heckman, on Behalf of Themselves and All Other Persons Similarly Situated v. Williamson County",
          "cluster_id": 895412,
          "cite": [
            "369 S.W.3d 137",
            "55 Tex. Sup. Ct. J. 803",
            "2012 WL 2052813",
            "2012 Tex. LEXIS 462"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haymond",
          "cluster_id": 4632951,
          "cite": [
            "588 U.S. 634",
            "139 S. Ct. 2369",
            "204 L. Ed. 2d 897",
            "2019 U.S. LEXIS 4398"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Collins",
          "cluster_id": 2518032,
          "cite": [
            "232 P.3d 32",
            "49 Cal. 4th 175",
            "110 Cal. Rptr. 3d 384",
            "2010 Cal. LEXIS 5032"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colavita",
          "cluster_id": 1917344,
          "cite": [
            "993 A.2d 874",
            "606 Pa. 1",
            "2010 Pa. LEXIS 939"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. White",
          "cluster_id": 3135667,
          "cite": [
            "2011 IL 109689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis (Slip Opinion)",
          "cluster_id": 4723868,
          "cite": [
            "146 N.E.3d 560",
            "159 Ohio St. 3d 31",
            "2020 Ohio 309"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gordon",
          "cluster_id": 855331,
          "cite": [
            "710 F.3d 1124",
            "2013 WL 1010540",
            "2013 U.S. App. LEXIS 5251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pecina, Alfredo Leyva",
          "cluster_id": 2947167,
          "cite": [
            "361 S.W.3d 68",
            "2012 WL 204293",
            "2012 Tex. Crim. App. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas Maslonka v. Bonita Hoffner",
          "cluster_id": 4526295,
          "cite": [
            "900 F.3d 269"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Garey",
          "cluster_id": 78113,
          "cite": [
            "540 F.3d 1253",
            "2008 WL 3850284"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Philmore v. McNeil",
          "cluster_id": 78417,
          "cite": [
            "575 F.3d 1251",
            "2009 U.S. App. LEXIS 17051",
            "2009 WL 2181682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Thompkins, J v. Randy Pfist",
          "cluster_id": 810674,
          "cite": [
            "698 F.3d 976",
            "2012 WL 5200352",
            "2012 U.S. App. LEXIS 22005"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Watson v. United States",
          "cluster_id": 4413795,
          "cite": [
            "865 F.3d 123",
            "2017 WL 3221270",
            "2017 U.S. App. LEXIS 13805"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott Schmidt v. Brian Foster",
          "cluster_id": 4575498,
          "cite": [
            "911 F.3d 469"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hurrell-Harring v. State",
          "cluster_id": 2478385,
          "cite": [
            "930 N.E.2d 217",
            "15 N.Y.3d 8",
            "904 N.Y.S.2d 296"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 5302486,
          "cite": [
            "499 P.3d 282",
            "287 Cal. Rptr. 3d 2",
            "12 Cal. 5th 367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lucarelli",
          "cluster_id": 2293664,
          "cite": [
            "971 A.2d 1173",
            "601 Pa. 185",
            "2009 Pa. LEXIS 933"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stein",
          "cluster_id": 1440930,
          "cite": [
            "541 F.3d 130",
            "102 A.F.T.R.2d (RIA) 6023",
            "2008 U.S. App. LEXIS 18524",
            "2008 WL 3982104"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daves v. Dallas County",
          "cluster_id": 5450527,
          "cite": [
            "22 F.4th 522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Scheffert",
          "cluster_id": 1896310,
          "cite": [
            "778 N.W.2d 733",
            "279 Neb. 479"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander Michael Roy",
          "cluster_id": 4386230,
          "cite": [
            "855 F.3d 1133",
            "2017 WL 1488331",
            "2017 U.S. App. LEXIS 7354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rothgery v. Gillespie County:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145785 OR 9435183 OR 9435184 OR 9435185 OR 9435186) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMzMDE0NDAwMDAwJnM9MTI4MzQwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145785+OR+9435183+OR+9435184+OR+9435185+OR+9435186%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(145785 OR 9435183 OR 9435184 OR 9435185 OR 9435186)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMiZzPTczMTIwMzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145785+OR+9435183+OR+9435184+OR+9435185+OR+9435186%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145785 OR 9435183 OR 9435184 OR 9435185 OR 9435186)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145785 OR 9435183 OR 9435184 OR 9435185 OR 9435186)",
    "indexed_citing_opinions": 239,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145785,
        "count": 182,
        "count_source": "search"
      },
      {
        "opinion_id": 9435183,
        "count": 63,
        "count_source": "search"
      },
      {
        "opinion_id": 9435184,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435185,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435186,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 444,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rothgery-v-gillespie-county.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MzUxNzQmcz0xMDYzMDYyMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145785+OR+9435183+OR+9435184+OR+9435185+OR+9435186%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145785,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 93540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 112080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 112780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 118130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 118318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 118417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 380338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 381821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 798163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1093220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1177598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1211338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1257249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1396275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1488407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1493658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1686940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1765959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 1960321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 2358414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 2362080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145785,
        "cited_id": 2511642,
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
    "date_created": "2026-07-05T17:47:15Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:52:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:47:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rothgery v. Gillespie County

```
(Slip Opinion)              OCTOBER TERM, 2007                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

         ROTHGERY v. GILLESPIE COUNTY, TEXAS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

      No. 07–440.      Argued March 17, 2008—Decided June 23, 2008
Texas police relied on erroneous information that petitioner Rothgery
  had a previous felony conviction to arrest him as a felon in possession
  of a firearm. The officers brought Rothgery before a magistrate
  judge, as required by state law, for a so-called “article 15.17 hearing,”
  at which the Fourth Amendment probable-cause determination was
  made, bail was set, and Rothgery was formally apprised of the accu-
  sation against him. After the hearing, the magistrate judge commit-
  ted Rothgery to jail, and he was released after posting a surety bond.
  Rothgery had no money for a lawyer and made several unheeded oral
  and written requests for appointed counsel. He was subsequently in-
  dicted and rearrested, his bail was increased, and he was jailed when
  he could not post the bail. Subsequently, Rothgery was assigned a
  lawyer, who assembled the paperwork that prompted the indict-
  ment’s dismissal.
     Rothgery then brought this 42 U. S. C. §1983 action against re-
  spondent County, claiming that if it had provided him a lawyer
  within a reasonable time after the article 15.17 hearing, he would not
  have been indicted, rearrested, or jailed. He asserts that the
  County’s unwritten policy of denying appointed counsel to indigent
  defendants out on bond until an indictment is entered violates his
  Sixth Amendment right to counsel. The District Court granted the
  County summary judgment, and the Fifth Circuit affirmed, consider-
  ing itself bound by Circuit precedent to the effect that the right to
  counsel did not attach at the article 15.17 hearing because the rele-
  vant prosecutors were not aware of, or involved in, Rothgery’s arrest
  or appearance at the hearing, and there was no indication that the of-
  ficer at Rothgery’s appearance had any power to commit the State to
  prosecute without a prosecutor’s knowledge or involvement.
2                ROTHGERY v. GILLESPIE COUNTY

                                Syllabus

Held: A criminal defendant’s initial appearance before a magistrate
 judge, where he learns the charge against him and his liberty is sub-
 ject to restriction, marks the initiation of adversary judicial proceed-
 ings that trigger attachment of the Sixth Amendment right to coun-
 sel. Attachment does not also require that a prosecutor (as distinct
 from a police officer) be aware of that initial proceeding or involved in
 its conduct. Pp. 5–20.
    (a) Texas’s article 15.17 hearing marks the point of attachment,
 with the consequent state obligation to appoint counsel within a rea-
 sonable time once a request for assistance is made. This Court has
 twice held that the right to counsel attaches at the initial appearance
 before a judicial officer at which a defendant is told of the formal ac-
 cusation against him and restrictions are imposed on his liberty. See
 Michigan v. Jackson, 475 U. S. 625, 629, n. 3; Brewer v. Williams,
 430 U. S. 387, 398–399. Rothgery’s hearing was an initial appear-
 ance: he was taken before a magistrate judge, informed of the formal
 accusation against him, and sent to jail until he posted bail. Thus,
 Brewer and Jackson control. Pp. 5–10.
    (b) In McNeil v. Wisconsin, 501 U. S. 171, 180–181, the Court reaf-
 firmed that “[t]he Sixth Amendment right to counsel attaches at the
 first formal proceeding against an accused,” and observed that “in
 most States . . . free counsel is made available at that time.” That
 observation remains true today. The overwhelming consensus prac-
 tice conforms to the rule that the first formal proceeding is the point
 of attachment. The Court is advised without contradiction that not
 only the Federal Government, including the District of Columbia, but
 43 States take the first step toward appointing counsel before, at, or
 just after initial appearance. To the extent the remaining 7 States
 have been denying appointed counsel at that time, they are a distinct
 minority. Pp. 10–12.
    (c) Neither the Fifth Circuit nor the County offers an acceptable
 justification for the minority practice. Pp. 12–19.
       (1) The Fifth Circuit found the determining factor to be that no
 prosecutor was aware of Rothgery’s article 15.17 hearing or involved
 in it. This prosecutorial awareness standard is wrong. Neither
 Brewer nor Jackson said a word about the prosecutor’s involvement
 as a relevant fact, much less a controlling one. Those cases left no
 room for the factual enquiry the Circuit would require, and with good
 reason: an attachment rule that turned on determining the moment
 of a prosecutor’s first involvement would be “wholly unworkable and
 impossible to administer,” Escobedo v. Illinois, 378 U. S. 478, 496.
 The Fifth Circuit derived its rule from the statement, in Kirby v. Illi-
 nois, 406 U. S. 682, 689, that the right to counsel attaches when the
 government has “committed itself to prosecute.” But what counts as
                      Cite as: 554 U. S. ____ (2008)                     3

                                 Syllabus

  such a commitment is an issue of federal law unaffected by alloca-
  tions of power among state officials under state law, cf. Moran v.
  Burbine, 475 U. S. 412, 429, n. 3, and under the federal standard, an
  accusation filed with a judicial officer is sufficiently formal, and the
  government’s commitment to prosecute it sufficiently concrete, when
  the accusation prompts arraignment and restrictions on the accused’s
  liberty, see, e.g., Kirby, supra, at 689. Pp. 12–15.
       (2) The County relies on United States v. Gouveia, 467 U. S. 180,
  in arguing that in considering the initial appearance’s significance,
  this Court must ignore prejudice to a defendant’s pretrial liberty, it
  being the concern, not of the right to counsel, but of the speedy-trial
  right and the Fourth Amendment. But the County’s suggestion that
  Fifth Amendment protections at the early stage obviate attachment
  of the Sixth Amendment right at initial appearance was refuted by
  Jackson, 475 U. S., at 629, n. 3. And since the Court is not asked to
  extend the right to counsel to a point earlier than formal judicial pro-
  ceedings (as in Gouveia), but to defer it to those proceedings in which
  a prosecutor is involved, Gouveia does not speak to the question at is-
  sue. Pp. 15–17.
       (3) The County’s third tack gets it no further. Stipulating that
  the properly formulated test is whether the State has objectively
  committed itself to prosecute, the County says that prosecutorial in-
  volvement is but one form of evidence of such commitment and that
  others include (1) the filing of formal charges or the holding of an ad-
  versarial preliminary hearing to determine probable cause to file
  such charges, and (2) a court appearance following arrest on an in-
  dictment. Either version runs up against Brewer and Jackson: an
  initial appearance following a charge signifies a sufficient commit-
  ment to prosecute regardless of a prosecutor’s participation, indict-
  ment, information, or what the County calls a “formal” complaint.
  The County’s assertions that Brewer and Jackson are “vague” and
  thus of limited, if any, precedential value are wrong. Although the
  Court in those cases saw no need for lengthy disquisitions on the ini-
  tial appearance’s significance, that was because it found the attach-
  ment issue an easy one. See, e.g., Brewer, supra, at 399. Pp. 17–19.
491 F. 3d 293, vacated and remanded.

   SOUTER, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and STEVENS, SCALIA, KENNEDY, GINSBURG, BREYER, and ALITO,
JJ., joined. ROBERTS, C. J., filed a concurring opinion, in which SCALIA,
J., joined. ALITO, J., filed a concurring opinion, in which ROBERTS, C. J.,
and SCALIA, J., joined. THOMAS, J., filed a dissenting opinion.
                         Cite as: 554 U. S. ____ (2008)                              1

                              Opinion of the Court

      NOTICE: This opinion is subject to formal revision before publication in the
      preliminary print of the United States Reports. Readers are requested to
      notify the Reporter of Decisions, Supreme Court of the United States, Wash-
      ington, D. C. 20543, of any typographical or other formal errors, in order
      that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                    No. 07–440
                                    _________________


 WALTER A. ROTHGERY, PETITIONER v. GILLESPIE
               COUNTY, TEXAS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                                  [June 23, 2008]

  JUSTICE SOUTER delivered the opinion of the Court.
  This Court has held that the right to counsel guaranteed
by the Sixth Amendment applies at the first appearance
before a judicial officer at which a defendant is told of the
formal accusation against him and restrictions are im-
posed on his liberty. See Brewer v. Williams, 430 U. S.
387, 398–399 (1977); Michigan v. Jackson, 475 U. S. 625,
629, n. 3 (1986). The question here is whether attachment
of the right also requires that a public prosecutor (as
distinct from a police officer) be aware of that initial pro-
ceeding or involved in its conduct. We hold that it does
not.
                             I

                             A

  Although petitioner Walter Rothgery has never been
convicted of a felony,1 a criminal background check dis-
closed an erroneous record that he had been, and on July
——————
   1 “[F]elony charges . . . had been dismissed after Rothgery completed

a diversionary program, and both sides agree that [he] did not have a
felony conviction.” 491 F. 3d 293, 294 (CA5 2007) (case below).
2                ROTHGERY v. GILLESPIE COUNTY

                          Opinion of the Court

15, 2002, Texas police officers relied on this record to
arrest him as a felon in possession of a firearm. The offi-
cers lacked a warrant, and so promptly brought Rothgery
before a magistrate judge, as required by Tex. Crim. Proc.
Code Ann., Art. 14.06(a) (West Supp. 2007).2 Texas law
has no formal label for this initial appearance before a
magistrate, see 41 G. Dix & R. Dawson, Texas Practice
Series: Criminal Practice and Procedure §15.01 (2d ed.
2001), which is sometimes called the “article 15.17 hear-
ing,” see, e.g., Kirk v. State, 199 S. W. 3d 467, 476–477
(Tex. App. 2006); it combines the Fourth Amendment’s
required probable-cause determination3 with the setting of
bail, and is the point at which the arrestee is formally
apprised of the accusation against him, see Tex. Crim.
Proc. Code Ann., Art. 15.17(a).
   Rothgery’s article 15.17 hearing followed routine. The
arresting officer submitted a sworn “Affidavit Of Probable
Cause” that described the facts supporting the arrest and
“charge[d] that . . . Rothgery . . . commit[ted] the offense of
unlawful possession of a firearm by a felon—3rd degree
felony [Tex. Penal Code Ann. §46.04],” App. to Pet. for
Cert. 33a. After reviewing the affidavit, the magistrate
judge “determined that probable cause existed for the
——————
    2Aseparate article of the Texas Code of Criminal Procedure requires
prompt presentment in the case of arrests under warrant as well. See
Art. 15.17(a) (West Supp. 2007). Whether the arrest is under warrant
or warrantless, article 15.17 details the procedures a magistrate judge
must follow upon presentment. See Art. 14.06(a) (in cases of war-
rantless arrest, “[t]he magistrate shall immediately perform the duties
described in Article 15.17 of this Code”).
  3 See Gerstein v. Pugh, 420 U. S. 103, 113–114 (1975) (“[A] police-

man’s on-the-scene assessment of probable cause provides legal justifi-
cation for arresting a person suspected of crime, and for a brief period
of detention to take the administrative steps incident to arrest[,] . . . .
[but] the Fourth Amendment requires a judicial determination of
probable cause as a prerequisite to extended restraint of liberty follow-
ing arrest”).
                     Cite as: 554 U. S. ____ (2008)                   3

                         Opinion of the Court

arrest.” Id., at 34a. The magistrate judge informed Roth-
gery of the accusation, set his bail at $5,000, and commit-
ted him to jail, from which he was released after posting a
surety bond. The bond, which the Gillespie County deputy
sheriff signed, stated that “Rothgery stands charged by
complaint duly filed . . . with the offense of a . . . felony, to
wit: Unlawful Possession of a Firearm by a Felon.” Id., at
39a. The release was conditioned on the defendant’s
personal appearance in trial court “for any and all subse-
quent proceedings that may be had relative to the said
charge in the course of the criminal action based on said
charge.” Ibid.
  Rothgery had no money for a lawyer and made several
oral and written requests for appointed counsel,4 which
went unheeded.5 The following January, he was indicted
by a Texas grand jury for unlawful possession of a firearm
by a felon, resulting in rearrest the next day, and an order
increasing bail to $15,000. When he could not post it, he
was put in jail and remained there for three weeks.
  On January 23, 2003, six months after the article 15.17
hearing, Rothgery was finally assigned a lawyer, who
promptly obtained a bail reduction (so Rothgery could get
out of jail), and assembled the paperwork confirming that
Rothgery had never been convicted of a felony. Counsel
relayed this information to the district attorney, who in
turn filed a motion to dismiss the indictment, which was
granted.

——————
  4 Because respondent Gillespie County obtained summary judgment

in the current case, we accept as true that Rothgery made multiple
requests.
  5 Rothgery also requested counsel at the article 15.17 hearing itself,

but the magistrate judge informed him that the appointment of counsel
would delay setting bail (and hence his release from jail). Given the
choice of proceeding without counsel or remaining in custody, Rothgery
waived the right to have appointed counsel present at the hearing. See
491 F. 3d, at 295, n. 2.
4                ROTHGERY v. GILLESPIE COUNTY

                          Opinion of the Court

                              B
   Rothgery then brought this 42 U. S. C. §1983 action
against respondent Gillespie County, claiming that if the
County had provided a lawyer within a reasonable time
after the article 15.17 hearing, he would not have been
indicted, rearrested, or jailed for three weeks.         The
County’s failure is said to be owing to its unwritten policy
of denying appointed counsel to indigent defendants out
on bond until at least the entry of an information or in-
dictment.6 Rothgery sees this policy as violating his Sixth
Amendment right to counsel.7
   The District Court granted summary judgment to the
County, see 413 F. Supp. 2d 806, 807 (WD Tex. 2006), and
the Court of Appeals affirmed, see 491 F. 3d 293, 294 (CA5
2007). The Court of Appeals felt itself bound by Circuit
precedent, see id., at 296–297 (citing Lomax v. Alabama,
629 F. 2d 413 (CA5 1980), and McGee v. Estelle, 625 F. 2d
1206 (CA5 1980)), to the effect that the Sixth Amendment
right to counsel did not attach at the article 15.17 hearing,
because “the relevant prosecutors were not aware of or
involved in Rothgery’s arrest or appearance before the
magistrate on July 16, 2002,” and “[t]here is also no indi-
cation that the officer who filed the probable cause affida-
vit at Rothgery’s appearance had any power to commit the
state to prosecute without the knowledge or involvement
of a prosecutor,” 491 F. 3d, at 297.
——————
    6 Rothgerydoes not challenge the County’s written policy for ap-
pointment of counsel, but argues that the County was not following
that policy in practice. See 413 F. Supp. 2d 806, 809–810 (WD Tex.
2006).
  7 Such a policy, if proven, arguably would also be in violation of Texas

state law, which appears to require appointment of counsel for indigent
defendants released from custody, at the latest, when the “first court
appearance” is made. See Tex. Crim. Proc. Code Ann., Art. 1.051(j).
See also Brief for Texas Association of Counties et al. as Amici Curiae
13 (asserting that Rothgery “was statutorily entitled to the appoint-
ment of counsel within three days after having requested it”).
                     Cite as: 554 U. S. ____ (2008)                    5

                          Opinion of the Court

  We granted certiorari, 552 U. S. ___ (2007), and now
vacate and remand.
                              II
   The Sixth Amendment right of the “accused” to assis-
tance of counsel in “all criminal prosecutions”8 is limited
by its terms: “it does not attach until a prosecution is
commenced.” McNeil v. Wisconsin, 501 U. S. 171, 175
(1991); see also Moran v. Burbine, 475 U. S. 412, 430
(1986). We have, for purposes of the right to counsel,
pegged commencement to “ ‘the initiation of adversary
judicial criminal proceedings—whether by way of formal
charge, preliminary hearing, indictment, information, or
arraignment,’ ” United States v. Gouveia, 467 U. S. 180,
188 (1984) (quoting Kirby v. Illinois, 406 U. S. 682, 689
(1972) (plurality opinion)). The rule is not “mere formal-
ism,” but a recognition of the point at which “the govern-
ment has committed itself to prosecute,” “the adverse
positions of government and defendant have solidified,”
and the accused “finds himself faced with the prosecutorial
forces of organized society, and immersed in the intricacies
of substantive and procedural criminal law.” Kirby, supra,
at 689. The issue is whether Texas’s article 15.17 hearing
marks that point, with the consequent state obligation to
appoint counsel within a reasonable time once a request
for assistance is made.
                               A
  When the Court of Appeals said no, because no prosecu-
tor was aware of Rothgery’s article 15.17 hearing or in-
volved in it, the court effectively focused not on the start of
adversarial judicial proceedings, but on the activities and
knowledge of a particular state official who was presuma-
——————
  8 The Sixth Amendment provides that “[i]n all criminal prosecutions,

the accused shall enjoy the right . . . to have the Assistance of Counsel
for his defence.”
6                ROTHGERY v. GILLESPIE COUNTY

                          Opinion of the Court

bly otherwise occupied. This was error.
  As the Court of Appeals recognized, see 491 F. 3d, at
298, we have twice held that the right to counsel attaches
at the initial appearance before a judicial officer, see
Jackson, 475 U. S., at 629, n. 3; Brewer 430 U. S., at 399.
This first time before a court, also known as the “ ‘prelimi-
nary arraignment’ ” or “ ‘arraignment on the complaint,’ ”
see 1 W. LaFave, J. Israel, N. King, & O. Kerr, Criminal
Procedure §1.4(g), p. 135 (3d ed. 2007), is generally the
hearing at which “the magistrate informs the defendant of
the charge in the complaint, and of various rights in fur-
ther proceedings,” and “determine[s] the conditions for
pretrial release,” ibid. Texas’s article 15.17 hearing is an
initial appearance: Rothgery was taken before a magis-
trate judge, informed of the formal accusation against
him, and sent to jail until he posted bail. See supra, at 2–
3.9 Brewer and Jackson control.
  The Brewer defendant surrendered to the police after a
warrant was out for his arrest on a charge of abduction.
——————
  9 The Court of Appeals did not resolve whether the arresting officer’s

formal accusation would count as a “formal complaint” under Texas
state law. See 491 F. 3d, at 298–300 (noting the confusion in the Texas
state courts). But it rightly acknowledged (albeit in considering the
separate question whether the complaint was a “formal charge”) that
the constitutional significance of judicial proceedings cannot be allowed
to founder on the vagaries of state criminal law, lest the attachment
rule be rendered utterly “vague and unpredictable.” Virginia v. Moore,
553 U. S. ___, ___ (2008) (slip op., at 10). See 491 F. 3d, at 300 (“[W]e
are reluctant to rely on the formalistic question of whether the affidavit
here would be considered a ‘complaint’ or its functional equivalent
under Texas case law and Article 15.04 of the Texas Code of Criminal
Procedures—a question to which the answer is itself uncertain. In-
stead, we must look to the specific circumstances of this case and the
nature of the affidavit filed at Rothgery’s appearance before the magis-
trate” (footnote omitted)). What counts is that the complaint filed with
the magistrate judge accused Rothgery of committing a particular
crime and prompted the judicial officer to take legal action in response
(here, to set the terms of bail and order the defendant locked up).
                      Cite as: 554 U. S. ____ (2008)                      7

                           Opinion of the Court

He was then “arraigned before a judge . . . on the out-
standing arrest warrant,” and at the arraignment, “[t]he
judge advised him of his Miranda [v. Arizona, 384 U. S.
436 (1966)] rights and committed him to jail.” Brewer, 430
U. S., at 391. After this preliminary arraignment, and
before an indictment on the abduction charge had been
handed up, police elicited incriminating admissions that
ultimately led to an indictment for first-degree murder.
Because neither of the defendant’s lawyers had been
present when the statements were obtained, the Court
found it “clear” that the defendant “was deprived of . . . the
right to the assistance of counsel.” Id., at 397–398. In
plain terms, the Court said that “[t]here can be no doubt
in the present case that judicial proceedings had been
initiated” before the defendant made the incriminating
statements. Id., at 399. Although it noted that the State
had conceded the issue, the Court nevertheless held that
the defendant’s right had clearly attached for the reason
that “[a] warrant had been issued for his arrest, he had
been arraigned on that warrant before a judge in a . . .
courtroom, and he had been committed by the court to
confinement in jail.” Ibid.10
——————
  10 The dissent says that “Brewer’s attachment holding is indisputably

no longer good law” because “we have subsequently held that the Sixth
Amendment right to counsel is ‘ “offense specific,” ’ ” post, at 13 (opinion
of THOMAS, J.) (quoting Texas v. Cobb, 532 U. S. 162, 164 (2001)), i.e.,
that it does not “exten[d] to crimes that are ‘factually related’ to those
that have actually been charged,” Cobb, supra, at 167. It is true that
Brewer appears to have assumed that attachment of the right with
respect to the abduction charge should prompt attachment for the
murder charge as well. But the accuracy of the dissent’s assertion ends
there, for nothing in Cobb’s conclusion that the right is offense specific
casts doubt on Brewer’s separate, emphatic holding that the initial
appearance marks the point at which the right attaches. Nor does
Cobb reflect, as the dissent suggests, see post, at 14, a more general
disapproval of our opinion in Brewer. While Brewer failed even to
acknowledge the issue of offense specificity, it spoke clearly and force-
fully about attachment. Cobb merely declined to follow Brewer’s
8                 ROTHGERY v. GILLESPIE COUNTY

                           Opinion of the Court

   In Jackson, the Court was asked to revisit the question
whether the right to counsel attaches at the initial ap-
pearance, and we had no more trouble answering it the
second time around. Jackson was actually two consoli-
dated cases, and although the State conceded that respon-
dent Jackson’s arraignment “represented the initiation of
formal legal proceedings,” 475 U. S., at 629, n. 3, it argued
that the same was not true for respondent Bladel. In
briefing us, the State explained that “[i]n Michigan, any
person charged with a felony, after arrest, must be
brought before a Magistrate or District Court Judge with-
out unnecessary delay for his initial arraignment.” Brief
for Petitioner in Michigan v. Bladel, O. T. 1985, No. 84–
1539, p. 24. The State noted that “[w]hile [Bladel] had
been arraigned . . . , there is also a second arraignment in
Michigan procedure . . . , at which time defendant has his
first opportunity to enter a plea in a court with jurisdic-
tion to render a final decision in a felony case.” Id., at 25.
The State contended that only the latter proceeding, the
“arraignment on the information or indictment,” Y.
Kamisar, W. LaFave, J. Israel, & N. King, Modern Crimi-
nal Procedure 28 (9th ed. 1999) (emphasis deleted), should
trigger the Sixth Amendment right.11 “The defendant’s
——————
unmentioned assumption, and thus it lends no support to the dissent’s
claim that we should ignore what Brewer explicitly said.
  11 The State continued to press this contention at oral argument. See

Tr. of Oral Arg. in Michigan v. Jackson, O. T. 1985, No. 84–1531 etc., p.
4 (“[T]he Michigan Supreme Court held that if a defendant, while at his
initial appearance before a magistrate who has no jurisdiction to accept
a final plea in the case, whose only job is ministerial, in other words to
advise a defendant of the charge against him, set bond if bond is
appropriate, and to advise him of his right to counsel and to get the
administrative process going if he’s indigent, the Michigan Supreme
Court said if the defendant asked for appointed counsel at that stage,
the police are forevermore precluded from initiating interrogation of
that defendant”); id., at 8 (“First of all, as a practical matter, at least in
our courts, the police are rarely present for arraignment, for this type of
                     Cite as: 554 U. S. ____ (2008)                    9

                          Opinion of the Court

rights,” the State insisted, “are fully protected in the
context of custodial interrogation between initial arraign-
ment and preliminary examination by the Fifth Amend-
ment right to counsel” and by the preliminary examina-
tion itself.12 See Bladel Brief, supra, at 26.
   We flatly rejected the distinction between initial ar-
raignment and arraignment on the indictment, the State’s
argument being “untenable” in light of the “clear language
in our decisions about the significance of arraignment.”
Jackson, supra, at 629, n. 3. The conclusion was driven by
the same considerations the Court had endorsed in
Brewer: by the time a defendant is brought before a judi-
cial officer, is informed of a formally lodged accusation,
and has restrictions imposed on his liberty in aid of the
prosecution, the State’s relationship with the defendant
has become solidly adversarial. And that is just as true
when the proceeding comes before the indictment (in the
case of the initial arraignment on a formal complaint) as
when it comes after it (at an arraignment on an indict-
ment).13 See Coleman v. Alabama, 399 U. S. 1, 8 (1970)
——————
an arraignment, for an initial appearance, I guess we should use the
terminology. . . . The prosecutor is not there for initial appearance. We
have people brought through a tunnel. A court officer picks them up.
They take them down and the judge goes through this procedure. . . .
There is typically nobody from our side, if you will, there to see what’s
going on”).
  12 The preliminary examination is a preindictment stage at which the

defendant is allowed to test the prosecution’s evidence against him, and
to try to dissuade the prosecutor from seeking an indictment. See
Coleman v. Alabama, 399 U. S. 1 (1970). In Texas, the defendant is
notified of his right to a preliminary hearing, which in Texas is called
an “examining trial,” at the article 15.17 hearing. See Tex. Crim. Proc.
Code Ann., Art. 15.17(a). The examining trial in Texas is optional only,
and the defendant must affirmatively request it. See Reply Brief for
Petitioner 25.
  13 The County, in its brief to this Court, suggests that although

Brewer and Jackson spoke of attachment at the initial appearance, the
cases might actually have turned on some unmentioned fact. As to
10               ROTHGERY v. GILLESPIE COUNTY

                          Opinion of the Court

(plurality opinion) (right to counsel applies at preindict-
ment preliminary hearing at which the “sole purposes . . .
are to determine whether there is sufficient evidence
against the accused to warrant presenting his case to the
grand jury, and, if so, to fix bail if the offense is bailable”);
cf. Owen v. State, 596 So. 2d 985, 989, n. 7 (Fla. 1992)
(“The term ‘arraign’ simply means to be called before a
court officer and charged with a crime”).
                              B
   Our latest look at the significance of the initial appear-
ance was McNeil, 501 U. S. 171, which is no help to the
County. In McNeil the State had conceded that the right
to counsel attached at the first appearance before a county
court commissioner, who set bail and scheduled a prelimi-
nary examination. See id., at 173; see also id., at 175 (“It
is undisputed, and we accept for purposes of the present
case, that at the time petitioner provided the incriminat-
ing statements at issue, his Sixth Amendment right had
attached . . .”). But we did more than just accept the
concession; we went on to reaffirm that “[t]he Sixth
Amendment right to counsel attaches at the first formal
proceeding against an accused,” and observed that “in
——————
Brewer, the County speculates that an information might have been
filed before the defendant’s initial appearance. See Brief for Respon-
dent 34–36. But as Rothgery points out, the initial appearance in
Brewer was made in municipal court, and a felony information could
not have been filed there. See Reply Brief for Petitioner 11. As to
Jackson, the County suggests that the Court might have viewed Michi-
gan’s initial arraignment as a significant proceeding only because the
defendant could make a statement at that hearing, and because re-
spondent Bladel did in fact purport to enter a plea of not guilty. See
Brief for Respondent 36–37. But this attempt to explain Jackson as a
narrow holding is impossible to square with Jackson’s sweeping rejec-
tion of the State’s claims. It is further undermined by the fact that the
magistrate judge in Bladel’s case, like the one in Texas’s article 15.17
hearing, had no jurisdiction to accept a plea of guilty to a felony charge.
See Reply Brief for Petitioner 11–12.
                     Cite as: 554 U. S. ____ (2008)                   11

                          Opinion of the Court

most States, at least with respect to serious offenses, free
counsel is made available at that time . . . .” Id., at 180–
181.
  That was 17 years ago, the same is true today, and the
overwhelming consensus practice conforms to the rule that
the first formal proceeding is the point of attachment. We
are advised without contradiction that not only the Fed-
eral Government, including the District of Columbia, but
43 States take the first step toward appointing counsel
“before, at, or just after initial appearance.” App. to Brief
for National Association of Criminal Defense Lawyers as
Amicus Curiae 1a; see id., at 1a–7a (listing jurisdictions);14
——————
  14 The 43 States are these: (1) Alaska: see Alaska Stat. §18.85.100
(2006); Alaska Rule Crim. Proc. 5 (Lexis 2006–2007); (2) Arizona: see
Ariz. Rules Crim. Proc. 4.2, 6.1 (West Supp. 2007), (West 1998); (3)
Arkansas: see Ark. Rule Crim. Proc. 8.2 (2006); Bradford v. State, 325
Ark. 278, 927 S. W. 2d 329 (1996); (4) California: see Cal. Penal Code
§§858, 859 (West Supp. 2008); In re Johnson, 62 Cal. 2d 325, 329–330,
398 P. 2d 420, 422–423 (1965); (5) Connecticut: see Conn. Gen. Stat.
§54–1b (2005); Conn. Super. Ct. Crim. Rules §§37–1, 37–3, 37–6 (West
2008); State v. Pierre, 277 Conn. 42, 95–96, 890 A. 2d 474, 507 (2006);
(6) Delaware: see Del. Code Ann., Tit. 29, §4604 (2003); Del. Super. Ct.
Crim. Rules 5, 44 (2008); Deputy v. State, 500 A. 2d 581 (Del. 1985); (7)
Florida: see Fla. Rule Crim. Proc. 3.111 (West 2007); (8) Georgia: see
Ga. Code Ann. §§17–4–26 (2004), 17–12–23 (Supp. 2007); O’Kelley v.
State, 278 Ga. 564, 604 S. E. 2d 509 (2004); (9) Hawaii: see Haw. Rev.
Stat. §§802–1, 803–9 (1993); (10) Idaho: see Idaho Crim. Rules 5, 44
(Lexis 2007); Idaho Code §19–852 (Lexis 2004); (11) Illinois: see Ill.
Comp. Stat., ch. 725, §5/109–1 (2006); (12) Indiana: see Ind. Code §§35–
33–7–5, 35–33–7–6 (West 2004); (13) Iowa: see Iowa Rules Crim. Proc.
§§2.2, 2.28 (West 2008); (14) Kentucky: see Ky. Rule Crim. Proc. §3.05
(Lexis 2008); (15) Louisiana: see La. Code Crim. Proc. Ann., Art 230.1
(West Supp. 2008); (16) Maine: see Me. Rule Crim. Proc. 5C (West
2007); (17) Maryland: see Md. Ann. Code, Art. 27A, §4 (Lexis Supp.
2007); Md. Rule 4–214 (Lexis 2008); McCarter v. State, 363 Md. 705,
770 A. 2d 195 (2001); (18) Massachusetts: see Mass. Rule Crim. Proc. 7
(West 2006); (19) Michigan: see Mich. Rules Crim. Proc 6.005 (West
2008); (20) Minnesota: see Minn. Rules Crim. Proc. 5.01, 5.02 (2006);
(21) Mississippi: see Jimpson v. State, 532 So. 2d 985 (Miss. 1988); (22)
Missouri: see Mo. Rev. Stat. §600.048 (2000); (23) Montana: see Mont.
12               ROTHGERY v. GILLESPIE COUNTY

                          Opinion of the Court

see also Brief for American Bar Association as Amicus
Curiae 5–8 (describing the ABA’s position for the past 40
years that counsel should be appointed “certainly no later
than the accused’s initial appearance before a judicial
officer”). And even in the remaining 7 States (Alabama,
Colorado, Kansas, Oklahoma, South Carolina, Texas, and
Virginia) the practice is not free of ambiguity. See App. to
Brief for National Association of Criminal Defense Law-
yers as Amicus Curiae 5a–7a (suggesting that the practice
in Alabama, Kansas, South Carolina, and Virginia might
actually be consistent with the majority approach); see
also n. 7, supra. In any event, to the extent these States
have been denying appointed counsel on the heels of the
first appearance, they are a distinct minority.
                            C
  The only question is whether there may be some argu-
able justification for the minority practice. Neither the
——————
Code Ann. §46–8–101 (2007); (24) Nebraska: see Neb. Rev. Stat. §29–
3902 (1995); (25) Nevada: see Nev. Rev. Stat. §178.397 (2007); (26) New
Hampshire: see N. H. Rev. Stat. Ann. §604–A:3 (2001); (27) New
Jersey: see N. J. Rule Crim. Proc. 3:4–2 (West 2008); State v. Tucker,
137 N. J. 259, 645 A. 2d 111 (1994); (28) New Mexico: see N. M. Stat.
Ann. §31–16–3 (2000); (29) New York: see N. Y. Crim. Proc. Law Ann.
§180.10 (West 2007); (30) North Carolina: see N. C. Gen. Stat. Ann.
§7A–451 (Lexis 2007); (31) North Dakota: see N. D. Rules Crim. Proc. 5,
44 (Lexis 2008–2009); (32) Ohio: see Ohio Rules Crim. Proc. 5, 44 (Lexis
2006); (33) Oregon: see Ore. Rev. Stat. §§135.010, 135.040, 135.050
(2007); (34) Pennsylvania: see Pa. Rules Crim. Proc. 122, 519 (West
2008); (35) Rhode Island: see R. I. Dist. Ct. Rules Crim. Proc. 5, 44
(2007); (36) South Dakota: see S. D. Rule Crim. Proc. §23A–40–6 (2007);
(37) Tennessee: see Tenn. Rule Crim. Proc. 44 (2007); (38) Utah: see
Utah Code Ann. §77–32–302 (Lexis Supp. 2007); (39) Vermont: see Vt.
Stat. Ann., Tit. 13, §5234 (1998); Vt. Rules Crim. Proc. 5, 44 (2003); (40)
Washington: see Wash. Super. Ct. Crim. Rule 3.1 (West 2008); (41)
West Virginia: see W. Va. Code Ann. §50–4–3 (Lexis 2000); State v.
Barrow, 178 W. Va. 406, 359 S. E. 2d 844 (1987); (42) Wisconsin: see
Wis. Stat. §967.06 (2003–2004); (43) Wyoming: see Wyo. Stat. Ann. §7–
6–105 (2007); Wyo. Rules Crim. Proc. 5, 44 (2007).
                 Cite as: 554 U. S. ____ (2008)           13

                     Opinion of the Court

Court of Appeals in its opinion, nor the County in its
briefing to us, has offered an acceptable one.
                              1
  The Court of Appeals thought Brewer and Jackson could
be distinguished on the ground that “neither case ad-
dressed the issue of prosecutorial involvement,” and the
cases were thus “neutral on the point,” 491 F. 3d, at 298.
With Brewer and Jackson distinguished, the court then
found itself bound by Circuit precedent that “ ‘an adver-
sary criminal proceeding has not begun in a case where
the prosecution officers are unaware of either the charges
or the arrest.’ ” See 491 F. 3d, at 297 (quoting McGee v.
Estelle, 625 F. 3d 1206, 1208 (CA5 1980)). Under this
standard of prosecutorial awareness, attachment depends
not on whether a first appearance has begun adversary
judicial proceedings, but on whether the prosecutor had a
hand in starting it. That standard is wrong.
  Neither Brewer nor Jackson said a word about the
prosecutor’s involvement as a relevant fact, much less a
controlling one. Those cases left no room for the factual
enquiry the Court of Appeals would require, and with good
reason: an attachment rule that turned on determining
the moment of a prosecutor’s first involvement would be
“wholly unworkable and impossible to administer,” Esco-
bedo v. Illinois, 378 U. S. 478, 496 (1964) (White, J., dis-
senting), guaranteed to bog the courts down in prying
enquiries into the communication between police (who are
routinely present at defendants’ first appearances) and the
State’s attorneys (who are not), see Brief for Petitioner 39–
41. And it would have the practical effect of resting at-
tachment on such absurd distinctions as the day of the
month an arrest is made, see Brief for Brennan Center of
Justice et al. as Amici Curiae 10 (explaining that “jails
may be required to report their arrestees to county prose-
cutor offices on particular days” (citing Tex. Crim. Proc.
14            ROTHGERY v. GILLESPIE COUNTY

                      Opinion of the Court

Code Ann., Art. 2.19)); or “the sophistication, or lack
thereof, of a jurisdiction’s computer intake system,” Brief
for Brennan Center, supra, at 11; see also id., at 10–12
(noting that only “[s]ome Texas counties . . . have com-
puter systems that provide arrest and detention informa-
tion simultaneously to prosecutors, law enforcement offi-
cers, jail personnel, and clerks. Prosecutors in these
jurisdictions use the systems to prescreen cases early in
the process before an initial appearance” (citing D. Carmi-
chael, M. Gilbert, & M. Voloudakis, Texas A&M U., Public
Policy Research Inst., Evaluating the Impact of Direct
Electronic Filing in Criminal Cases: Closing the Paper
Trap 2–3 (2006), online at http://www.courts.state.tx.
us/tfid/pdf/FinalReport7-12-06wackn.pdf (as visited June
19, 2008, and available in Clerk of Court’s case file))).
   It is not that the Court of Appeals believed that any
such regime would be desirable, but it thought originally
that its rule was implied by this Court’s statement that
the right attaches when the government has “committed
itself to prosecute.” Kirby, 406 U. S., at 689. The Court of
Appeals reasoned that because “the decision not to prose-
cute is the quintessential function of a prosecutor” under
Texas law, 491 F. 3d, at 297 (internal quotation marks
omitted), the State could not commit itself to prosecution
until the prosecutor signaled that it had.
   But what counts as a commitment to prosecute is an
issue of federal law unaffected by allocations of power
among state officials under a State’s law, cf. Moran, 475
U. S., at 429, n. 3 (“[T]he type of circumstances that would
give rise to the right would certainly have a federal defini-
tion”), and under the federal standard, an accusation filed
with a judicial officer is sufficiently formal, and the gov-
ernment’s commitment to prosecute it sufficiently con-
crete, when the accusation prompts arraignment and
restrictions on the accused’s liberty to facilitate the prose-
cution, see Jackson, 475 U. S., at 629, n. 3; Brewer, 430
                  Cite as: 554 U. S. ____ (2008)           15

                      Opinion of the Court

U. S., at 399; Kirby, supra, at 689; see also n. 9, supra.
From that point on, the defendant is “faced with the
prosecutorial forces of organized society, and immersed in
the intricacies of substantive and procedural criminal law”
that define his capacity and control his actual ability to
defend himself against a formal accusation that he is a
criminal. Kirby, supra, at 689. By that point, it is too late
to wonder whether he is “accused” within the meaning of
the Sixth Amendment, and it makes no practical sense to
deny it. See Grano, Rhode Island v. Innis: A Need to
Reconsider the Constitutional Premises Underlying the
Law of Confessions, 17 Am. Crim. L. Rev. 1, 31 (1979)
(“[I]t would defy common sense to say that a criminal
prosecution has not commenced against a defendant who,
perhaps incarcerated and unable to afford judicially im-
posed bail, awaits preliminary examination on the author-
ity of a charging document filed by the prosecutor, less
typically by the police, and approved by a court of law”
(internal quotation marks omitted)). All of this is equally
true whether the machinery of prosecution was turned on
by the local police or the state attorney general. In this
case, for example, Rothgery alleges that after the initial
appearance, he was “unable to find any employment for
wages” because “all of the potential employers he con-
tacted knew or learned of the criminal charge pending
against him.” Original Complaint in No. 1:04–CV–00456–
LY (WD Tex., July 15, 2004), p. 5. One may assume that
those potential employers would still have declined to
make job offers if advised that the county prosecutor had
not filed the complaint.
                              2
  The County resists this logic with the argument that in
considering the significance of the initial appearance, we
must ignore prejudice to a defendant’s pretrial liberty,
reasoning that it is the concern, not of the right to counsel,
16            ROTHGERY v. GILLESPIE COUNTY

                     Opinion of the Court

but of the speedy-trial right and the Fourth Amendment.
See Brief for Respondent 47–51. And it cites Gouveia, 467
U. S. 180, in support of its contention. See Brief for Re-
spondent 49; see also Brief for Texas et al. as Amici Curiae
8–9. We think the County’s reliance on Gouveia is mis-
placed, and its argument mistaken.
   The defendants in Gouveia were prison inmates, sus-
pected of murder, who had been placed in an administra-
tive detention unit and denied counsel up until an indict-
ment was filed. Although no formal judicial proceedings
had taken place prior to the indictment, see 467 U. S., at
185, the defendants argued that their administrative
detention should be treated as an accusation for purposes
of the right to counsel because the government was ac-
tively investigating the crimes. We recognized that “be-
cause an inmate suspected of a crime is already in prison,
the prosecution may have little incentive promptly to
bring formal charges against him, and that the resulting
preindictment delay may be particularly prejudicial to the
inmate,” id., at 192, but we noted that statutes of limita-
tion and protections of the Fifth Amendment guarded
against delay, and that there was no basis for “depart[ing]
from our traditional interpretation of the Sixth Amend-
ment right to counsel in order to provide additional protec-
tions for [the inmates],” ibid.
   Gouveia’s holding that the Sixth Amendment right to
counsel had not attached has no application here. For one
thing, Gouveia does not affect the conclusion we reaf-
firmed two years later in Jackson, that bringing a defen-
dant before a court for initial appearance signals a suffi-
cient commitment to prosecute and marks the start of
adversary judicial proceedings. (Indeed, Jackson refutes
the County’s argument that Fifth Amendment protections
at the early stage obviate attachment of the Sixth Amend-
ment right at initial appearance. See supra, at 8–9.) And
since we are not asked to extend the right to counsel to a
                  Cite as: 554 U. S. ____ (2008)           17

                      Opinion of the Court

point earlier than formal judicial proceedings (as in Gou-
veia), but to defer it to those proceedings in which a prose-
cutor is involved, Gouveia does not speak to the question
before us.
  The County also tries to downplay the significance of the
initial appearance by saying that an attachment rule
unqualified by prosecutorial involvement would lead to the
conclusion “that the State has statutorily committed to
prosecute every suspect arrested by the police,” given that
“state law requires [an article 15.17 hearing] for every
arrestee.” Brief for Respondent 24 (emphasis in original).
The answer, though, is that the State has done just that,
subject to the option to change its official mind later. The
State may rethink its commitment at any point: it may
choose not to seek indictment in a felony case, say, or the
prosecutor may enter nolle prosequi after the case gets to
the jury room. But without a change of position, a defen-
dant subject to accusation after initial appearance is
headed for trial and needs to get a lawyer working,
whether to attempt to avoid that trial or to be ready with
a defense when the trial date arrives.
                              3
    A third tack on the County’s part, slightly different from
the one taken by the Fifth Circuit, gets it no further. The
County stipulates that “the properly formulated test is not
. . . merely whether prosecutors have had any involvement
in the case whatsoever, but instead whether the State has
objectively committed itself to prosecute.” Id., at 31. It
then informs us that “[p]rosecutorial involvement is
merely one form of evidence of such commitment.” Ibid.
Other sufficient evidentiary indications are variously
described: first (expansively) as “the filing of formal
charges . . . by information, indictment or formal com-
plaint, or the holding of an adversarial preliminary hear-
ing to determine probable cause to file such charges,” ibid.
18            ROTHGERY v. GILLESPIE COUNTY

                      Opinion of the Court

(citing Kirby, 406 U. S., at 689); then (restrictively) as a
court appearance following “arrest . . . on an indictment or
information,” Brief for Respondent 32. Either version, in
any event, runs up against Brewer and Jackson: an initial
appearance following a charge signifies a sufficient com-
mitment to prosecute regardless of a prosecutor’s partici-
pation, indictment, information, or what the County calls
a “formal” complaint.
   So the County is reduced to taking aim at those cases.
Brewer and Jackson, we are told, are “vague” and thus of
“limited, if any, precedential value.” Brief for Respondent
33, 35; see also id., at 32, n. 13 (asserting that Brewer and
Jackson “neither provide nor apply an analytical frame-
work for determining attachment”). And, according to the
County, our cases (Brewer and Jackson aside) actually
establish a “general rule that the right to counsel attaches
at the point that [what the County calls] formal charges
are filed,” Brief for Respondent 19, with exceptions al-
lowed only in the case of “a very limited set of specific
preindictment situations,” id., at 23. The County suggests
that the latter category should be limited to those appear-
ances at which the aid of counsel is urgent and “ ‘the dan-
gers to the accused of proceeding without counsel’ ” are
great. Id., at 28 (quoting Patterson v. Illinois, 487 U. S.
285, 298 (1988)). Texas’s article 15.17 hearing should not
count as one of those situations, the County says, because
it is not of critical significance, since it “allows no presen-
tation of witness testimony and provides no opportunity to
expose weaknesses in the government’s evidence, create a
basis for later impeachment, or even engage in basic dis-
covery.” Brief for Respondent 29.
   We think the County is wrong both about the clarity of
our cases and the substance that we find clear. Certainly
it is true that the Court in Brewer and Jackson saw no
need for lengthy disquisitions on the significance of the
initial appearance, but that was because it found the
                     Cite as: 554 U. S. ____ (2008)                   19

                          Opinion of the Court

attachment issue an easy one. The Court’s conclusions
were not vague; Brewer expressed “no doubt” that the
right to counsel attached at the initial appearance, 430
U. S., at 399, and Jackson said that the opposite result
would be “untenable,” 475 U. S., at 629, n. 3.
  If, indeed, the County had simply taken the cases at face
value, it would have avoided the mistake of merging the
attachment question (whether formal judicial proceedings
have begun) with the distinct “critical stage” question
(whether counsel must be present at a postattachment
proceeding unless the right to assistance is validly
waived). Attachment occurs when the government has
used the judicial machinery to signal a commitment to
prosecute as spelled out in Brewer and Jackson. Once
attachment occurs, the accused at least15 is entitled to the
presence of appointed counsel during any “critical stage” of
the postattachment proceedings; what makes a stage
critical is what shows the need for counsel’s presence.16
Thus, counsel must be appointed within a reasonable time
after attachment to allow for adequate representation at
any critical stage before trial, as well as at trial itself.
  The County thus makes an analytical mistake in its
assumption that attachment necessarily requires the
occurrence or imminence of a critical stage. See Brief for
Respondent 28–30. On the contrary, it is irrelevant to
attachment that the presence of counsel at an article 15.17
——————
  15 We do not here purport to set out the scope of an individual’s post-
attachment right to the presence of counsel. It is enough for present
purposes to highlight that the enquiry into that right is a different one
from the attachment analysis.
  16 The cases have defined critical stages as proceedings between an

individual and agents of the State (whether “formal or informal, in
court or out,” see United States v. Wade, 388 U. S. 218, 226 (1967)) that
amount to “trial-like confrontations,” at which counsel would help the
accused “in coping with legal problems or . . . meeting his adversary,”
United States v. Ash, 413 U. S. 300, 312–313 (1973); see also Massiah v.
United States, 377 U. S. 201 (1964).
20              ROTHGERY v. GILLESPIE COUNTY

                         Opinion of the Court

hearing, say, may not be critical, just as it is irrelevant
that counsel’s presence may not be critical when a prose-
cutor walks over to the trial court to file an information.
As we said in Jackson, “[t]he question whether arraign-
ment signals the initiation of adversary judicial proceed-
ings . . . is distinct from the question whether the ar-
raignment itself is a critical stage requiring the presence
of counsel.” 475 U. S., at 630, n. 3. Texas’s article 15.17
hearing plainly signals attachment, even if it is not itself a
critical stage.17
                            III
   Our holding is narrow. We do not decide whether the 6-
month delay in appointment of counsel resulted in preju-
dice to Rothgery’s Sixth Amendment rights, and have no
occasion to consider what standards should apply in decid-
ing this. We merely reaffirm what we have held before
and what an overwhelming majority of American jurisdic-
tions understand in practice: a criminal defendant’s initial
appearance before a judicial officer, where he learns the
charge against him and his liberty is subject to restriction,
marks the start of adversary judicial proceedings that
trigger attachment of the Sixth Amendment right to coun-
sel. Because the Fifth Circuit came to a different conclu-
sion on this threshold issue, its judgment is vacated, and
the case is remanded for further proceedings consistent
with this opinion.
                                            It is so ordered.




——————
  17 The dissent likewise anticipates an issue distinct from attachment

when it claims Rothgery has suffered no harm the Sixth Amendment
recognizes. Post, at 18. Whether the right has been violated and
whether Rothgery has suffered cognizable harm are separate questions
from when the right attaches, the sole question before us.
                 Cite as: 554 U. S. ____ (2008)           1

                  ROBERTS, C. J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–440
                         _________________


 WALTER A. ROTHGERY, PETITIONER v. GILLESPIE
               COUNTY, TEXAS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                        [June 23, 2008]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE SCALIA
joins, concurring.
   JUSTICE THOMAS’s analysis of the present issue is com-
pelling, but I believe the result here is controlled by
Brewer v. Williams, 430 U. S. 387 (1977), and Michigan v.
Jackson, 475 U. S. 625 (1986). A sufficient case has not
been made for revisiting those precedents, and accordingly
I join the Court’s opinion.
   I also join JUSTICE ALITO’s concurrence, which correctly
distinguishes between the time the right to counsel at-
taches and the circumstances under which counsel must
be provided.
                  Cite as: 554 U. S. ____ (2008)            1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 07–440
                          _________________


 WALTER A. ROTHGERY, PETITIONER v. GILLESPIE
               COUNTY, TEXAS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                         [June 23, 2008]

   JUSTICE ALITO, with whom THE CHIEF JUSTICE and
JUSTICE SCALIA join, concurring.
   I join the Court’s opinion because I do not understand it
to hold that a defendant is entitled to the assistance of
appointed counsel as soon as his Sixth Amendment right
attaches. As I interpret our precedents, the term “attach-
ment” signifies nothing more than the beginning of the
defendant’s prosecution. It does not mark the beginning of
a substantive entitlement to the assistance of counsel. I
write separately to elaborate on my understanding of the
term “attachment” and its relationship to the Amend-
ment’s substantive guarantee of “the Assistance of Coun-
sel for [the] defence.”
   The Sixth Amendment provides in pertinent part that
“[i]n all criminal prosecutions, the accused shall enjoy the
right . . . to have the Assistance of Counsel for his de-
fence.” The Amendment thus defines the scope of the
right to counsel in three ways: It provides who may assert
the right (“the accused”); when the right may be asserted
(“[i]n all criminal prosecutions”); and what the right guar-
antees (“the right . . . to have the Assistance of Counsel for
his defence”).
   It is in the context of interpreting the Amendment’s
answer to the second of these questions—when the right
may be asserted—that we have spoken of the right “at-
2             ROTHGERY v. GILLESPIE COUNTY

                     ALITO, J., concurring

taching.” In Kirby v. Illinois, 406 U. S. 682, 688 (1972), a
plurality of the Court explained that “a person’s Sixth and
Fourteenth Amendment right to counsel attaches only at
or after the time that adversary judicial proceedings have
been initiated against him.” A majority of the Court
elaborated on that explanation in Moore v. Illinois, 434
U. S. 220 (1977):
       “In Kirby v. Illinois, the plurality opinion made
    clear that the right to counsel announced in Wade and
    Gilbert attaches only to corporeal identifications con-
    ducted at or after the initiation of adversary judicial
    criminal proceedings—whether by way of formal
    charge, preliminary hearing, indictment, information,
    or arraignment. This is so because the initiation of
    such proceedings marks the commencement of the
    ‘criminal prosecutions’ to which alone the explicit
    guarantees of the Sixth Amendment are applicable.
    Thus, in Kirby the plurality held that the prosecu-
    tion’s evidence of a robbery victim’s one-on-one sta-
    tionhouse identification of an uncounseled suspect
    shortly after the suspect’s arrest was admissible be-
    cause adversary judicial criminal proceedings had not
    yet been initiated.” Id., at 226–227 (internal quota-
    tion marks and citations omitted).
When we wrote in Kirby and Moore that the Sixth
Amendment right had “attached,” we evidently meant
nothing more than that a “criminal prosecutio[n]” had
begun. Our cases have generally used the term in that
narrow fashion. See Texas v. Cobb, 532 U. S. 162, 167
(2001) (internal quotation marks omitted); McNeil v.
Wisconsin, 501 U. S. 171, 175 (1991); Michigan v. Harvey,
494 U. S. 344, 353 (1990); Satterwhite v. Texas, 486 U. S.
249, 254–255 (1988); Michigan v. Jackson, 475 U. S. 625,
629, and n. 3 (1986); Moran v. Burbine, 475 U. S. 412, 428
(1986); United States v. Gouveia, 467 U. S. 180, 188
                 Cite as: 554 U. S. ____ (2008)           3

                     ALITO, J., concurring

(1984); Edwards v. Arizona, 451 U. S. 477, 480, n. 7
(1981); Doggett v. United States, 505 U. S. 647, 663, n. 2
(1992) (THOMAS, J., dissenting); Patterson v. Illinois, 487
U. S. 285, 303–304 (1988) (STEVENS, J., dissenting);
United States v. Ash, 413 U. S. 300, 322 (1973) (Stewart,
J., concurring in judgment). But see Estelle v. Smith, 451
U. S. 454, 469 (1981) (“[W]e have held that the right to
counsel granted by the Sixth Amendment means that a
person is entitled to the help of a lawyer at or after the
time that adversary judicial proceedings have been initi-
ated against him . . .” (internal quotation marks omitted));
Brewer v. Williams, 430 U. S. 387, 398 (1977) (“[T]he right
to counsel granted by the Sixth and Fourteenth Amend-
ments means at least that a person is entitled to the help
of a lawyer at or after the time that judicial proceedings
have been initiated against him . . .”).
   Because pretrial criminal procedures vary substantially
from jurisdiction to jurisdiction, there is room for dis-
agreement about when a “prosecution” begins for Sixth
Amendment purposes. As the Court, notes, however, we
have previously held that “arraignments” that were func-
tionally indistinguishable from the Texas magistration
marked the point at which the Sixth Amendment right to
counsel “attached.” See ante, at 6 (discussing Jackson,
supra, and Brewer, supra).
   It does not follow, however, and I do not understand the
Court to hold, that the county had an obligation to appoint
an attorney to represent petitioner within some specified
period after his magistration. To so hold, the Court would
need to do more than conclude that petitioner’s criminal
prosecution had begun. It would also need to conclude
that the assistance of counsel in the wake of a Texas
magistration is part of the substantive guarantee of the
Sixth Amendment. That question lies beyond our reach,
petitioner having never sought our review of it. See Pet.
for Cert. i (inviting us to decide whether the Fifth Circuit
4             ROTHGERY v. GILLESPIE COUNTY

                     ALITO, J., concurring

erred in concluding “that adversary judicial proceedings
. . . had not commenced, and petitioner’s Sixth Amend-
ment rights had not attached”). To recall the framework
laid out earlier, we have been asked to address only the
when question, not the what question. Whereas the tem-
poral scope of the right is defined by the words “[i]n all
criminal prosecutions,” the right’s substantive guarantee
flows from a different textual font: the words “Assistance
of Counsel for his defence.”
    In interpreting this latter phrase, we have held that
“defence” means defense at trial, not defense in relation to
other objectives that may be important to the accused.
See Gouveia, supra, at 190 (“[T]he right to counsel exists
to protect the accused during trial-type confrontations
with the prosecutor . . .”); Ash, supra, at 309 (“[T]he core
purpose of the counsel guarantee was to assure ‘Assis-
tance’ at trial . . .”). We have thus rejected the argument
that the Sixth Amendment entitles the criminal defendant
to the assistance of appointed counsel at a probable cause
hearing. See Gerstein v. Pugh, 420 U. S. 103, 122–123
(1975) (observing that the Fourth Amendment hearing “is
addressed only to pretrial custody” and has an insubstan-
tial effect on the defendant’s trial rights). More generally,
we have rejected the notion that the right to counsel enti-
tles the defendant to a “preindictment private investiga-
tor.” Gouveia, supra, at 191.
    At the same time, we have recognized that certain pre-
trial events may so prejudice the outcome of the defen-
dant’s prosecution that, as a practical matter, the defen-
dant must be represented at those events in order to enjoy
genuinely effective assistance at trial. See, e.g., Ash,
supra, at 309–310; United States v. Wade, 388 U. S. 218,
226 (1967). Thus, we have held that an indigent defen-
dant is entitled to the assistance of appointed counsel at a
preliminary hearing if “substantial prejudice . . . inheres
in the . . . confrontation” and “counsel [may] help avoid
                  Cite as: 554 U. S. ____ (2008)            5

                      ALITO, J., concurring

that prejudice.” Coleman v. Alabama, 399 U. S. 1, 9
(1970) (plurality opinion) (internal quotation marks omit-
ted); see also White v. Maryland, 373 U. S. 59, 60 (1963)
(per curiam). We have also held that the assistance of
counsel is guaranteed at a pretrial lineup, since “the con-
frontation compelled by the State between the accused and
the victim or witnesses to a crime to elicit identification
evidence is peculiarly riddled with innumerable dangers
and variable factors which might seriously, even crucially,
derogate from a fair trial.” Wade, supra, at 228. Other
“critical stages” of the prosecution include pretrial interro-
gation, a pretrial psychiatric exam, and certain kinds of
arraignments. See Harvey, 494 U. S., at 358, n. 4; Estelle,
supra, at 470–471; Coleman, supra, at 7–8 (plurality
opinion).
   Weaving together these strands of authority, I interpret
the Sixth Amendment to require the appointment of coun-
sel only after the defendant’s prosecution has begun, and
then only as necessary to guarantee the defendant effec-
tive assistance at trial. Cf. McNeil, 501 U. S., at 177–178
(“The purpose of the Sixth Amendment counsel guaran-
tee—and hence the purpose of invoking it—is to protec[t]
the unaided layman at critical confrontations with his
expert adversary, the government, after the adverse posi-
tions of government and defendant have solidified with
respect to a particular alleged crime” (emphasis and al-
teration in original; internal quotation marks omitted)). It
follows that defendants in Texas will not necessarily be
entitled to the assistance of counsel within some specified
period after their magistrations. See ante, at 19 (opinion
of the Court) (pointing out the “analytical mistake” of
assuming “that attachment necessarily requires the occur-
rence or imminence of a critical stage”). Texas counties
need only appoint counsel as far in advance of trial, and as
far in advance of any pretrial “critical stage,” as necessary
to guarantee effective assistance at trial.         Cf. ibid.
6             ROTHGERY v. GILLESPIE COUNTY

                     ALITO, J., concurring

(“[C]ounsel must be appointed within a reasonable time
after attachment to allow for adequate representation at
any critical stage before trial, as well as at trial itself”
(emphasis added)).
   The Court expresses no opinion on whether Gillespie
County satisfied that obligation in this case. Petitioner
has asked us to decide only the limited question whether
his magistration marked the beginning of his “criminal
prosecutio[n]” within the meaning of the Sixth Amend-
ment. Because I agree with the Court’s resolution of that
limited question, I join its opinion in full.
                 Cite as: 554 U. S. ____ (2008)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 07–440
                         _________________


 WALTER A. ROTHGERY, PETITIONER v. GILLESPIE
               COUNTY, TEXAS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                        [June 23, 2008]

  JUSTICE THOMAS, dissenting.
  The Court holds today—for the first time after plenary
consideration of the question—that a criminal prosecution
begins, and that the Sixth Amendment right to counsel
therefore attaches, when an individual who has been
placed under arrest makes an initial appearance before a
magistrate for a probable-cause determination and the
setting of bail. Because the Court’s holding is not sup-
ported by the original meaning of the Sixth Amendment or
any reasonable interpretation of our precedents, I respect-
fully dissent.
                              I
   The Sixth Amendment provides that “[i]n all criminal
prosecutions, the accused shall enjoy the right . . . to have
the Assistance of Counsel for his defence.” The text of the
Sixth Amendment thus makes clear that the right to
counsel arises only upon initiation of a “criminal prosecu-
tio[n].” For that reason, the Court has repeatedly stressed
that the Sixth Amendment right to counsel “does not
attach until a prosecution is commenced.” McNeil v.
Wisconsin, 501 U. S. 171, 175 (1991); see also United
States v. Gouveia, 467 U. S. 180, 188 (1984) (“[T]he literal
language of the Amendment . . . requires the existence of
both a ‘criminal prosecutio[n]’ and an ‘accused’ ”). Echoing
2             ROTHGERY v. GILLESPIE COUNTY

                     THOMAS, J., dissenting

this refrain, the Court today reiterates that “[t]he Sixth
Amendment right of the ‘accused’ to assistance of counsel
in ‘all criminal prosecutions’ is limited by its terms.” Ante,
at 5 (footnote omitted).
  Given the Court’s repeated insistence that the right to
counsel is textually limited to “criminal prosecutions,” one
would expect the Court’s jurisprudence in this area to be
grounded in an understanding of what those words meant
when the Sixth Amendment was adopted. Inexplicably,
however, neither today’s decision nor any of the other
numerous decisions in which the Court has construed the
right to counsel has attempted to discern the original
meaning of “criminal prosecutio[n].” I think it appropriate
to examine what a “criminal prosecutio[n]” would have
been understood to entail by those who adopted the Sixth
Amendment.
                             A
  There is no better place to begin than with Blackstone,
“whose works constituted the preeminent authority on
English law for the founding generation.” Alden v. Maine,
527 U. S. 706, 715 (1999). Blackstone devoted more than
100 pages of his Commentaries on the Laws of England to
a discussion of the “regular and ordinary method of pro-
ceeding in the courts of criminal jurisdiction.” 4 W. Black-
stone, Commentaries *289 (hereinafter Blackstone).
  At the outset of his discussion, Blackstone organized the
various stages of a criminal proceeding “under twelve
general heads, following each other in a progressive or-
der.” Ibid. The first six relate to pretrial events: “1. Ar-
rest; 2. Commitment and bail; 3. Prosecution; 4. Process; 5.
Arraignment, and it’s incidents; 6. Plea, and issue.” Ibid.
(emphasis added). Thus, the first significant fact is that
Blackstone did not describe the entire criminal process as
a “prosecution,” but rather listed prosecution as the third
step in a list of successive stages. For a more complete
                 Cite as: 554 U. S. ____ (2008)            3

                    THOMAS, J., dissenting

understanding of what Blackstone meant by “prosecution,”
however, we must turn to chapter 23, entitled “Of the
Several Modes of Prosecution.” Id., at *301. There, Black-
stone explained that—after arrest and examination by a
justice of the peace to determine whether a suspect should
be discharged, committed to prison, or admitted to bail,
id., at *296—the “next step towards the punishment of
offenders is their prosecution, or the manner of their for-
mal accusation,” id., at *301 (emphasis added).
   Blackstone thus provides a definition of “prosecution”:
the manner of an offender’s “formal accusation.” The
modifier “formal” is significant because it distinguishes
“prosecution” from earlier stages of the process involving a
different kind of accusation: the allegation of criminal
conduct necessary to justify arrest and detention. Black-
stone’s discussion of arrest, commitment, and bail makes
clear that a person could not be arrested and detained
without a “charge” or “accusation,” i.e., an allegation,
supported by probable cause, that the person had commit-
ted a crime. See id., at *289–*300. But the accusation
justifying arrest and detention was clearly preliminary to
the “formal accusation” that Blackstone identified with
“prosecution.” See id., at *290, *318.
   By “formal accusation,” Blackstone meant, in most
cases, “indictment, the most usual and effectual means of
prosecution.” Id., at *302. Blackstone defined an “indict-
ment” as “a written accusation of one or more persons of a
crime or misdemeanor, preferred to, and presented upon
oath by, a grand jury.” Ibid. (emphasis deleted). If the
grand jury was “satisfied of the truth of the accusation,” it
endorsed the indictment, id., at *305–*306, which was
then “publicly delivered into court,” id., at *306, “after-
wards to be tried and determined,” id., at *303, “before an
officer having power to punish the [charged] offence,” 2 T.
Cunningham, A New and Complete Law Dictionary (2d ed.
1771).
4             ROTHGERY v. GILLESPIE COUNTY

                    THOMAS, J., dissenting

   In addition to indictment, Blackstone identified two
other “methods of prosecution at the suit of the king.” 4
Blackstone *312. The first was presentment, which, like
an indictment, was a grand jury’s formal accusation “of an
offence, inquirable in the Court where it [was] presented.”
5 G. Jacob, The Law-Dictionary 278–279 (1811). The
principal difference was that the accusation arose from
“the notice taken by a grand jury of any offence from their
own knowledge or observation” rather than from a “bill of
indictment laid before them.” 4 Blackstone *301. The
second was information, “the only species of proceeding at
the suit of the king, without a previous indictment or
presentment by a grand jury.” Id., at *308. After an
information was filed, it was “tried,” id., at *309, in the
same way as an indictment: “The same notice was given,
the same process was issued, the same pleas were allowed,
the same trial by jury was had, the same judgment was
given by the same judges, as if the prosecution had origi-
nally been by indictment,” id., at *310.
   From the foregoing, the basic elements of a criminal
“prosecution” emerge with reasonable clarity. “Prosecu-
tion,” as Blackstone used the term, referred to “instituting
a criminal suit,” id., at *309, by filing a formal charging
document—an indictment, presentment, or information—
upon which the defendant was to be tried in a court with
power to punish the alleged offense. And, significantly,
Blackstone’s usage appears to have accorded with the
ordinary meaning of the term. See 2 N. Webster, An
American Dictionary of the English Language (1828)
(defining “prosecution” as “[t]he institution or commence-
ment and continuance of a criminal suit; the process of
exhibiting formal charges against an offender before a
legal tribunal, and pursuing them to final judgment,” and
noting that “[p]rosecutions may be by presentment, infor-
mation or indictment”).
                  Cite as: 554 U. S. ____ (2008)              5

                      THOMAS, J., dissenting

                               B
  With Blackstone as our guide, it is significant that the
Framers used the words “criminal prosecutions” in the
Sixth Amendment rather than some other formulation
such as “criminal proceedings” or “criminal cases.” In-
deed, elsewhere in the Bill of Rights we find just such an
alternative formulation: In contrast to the Sixth Amend-
ment, the Fifth Amendment refers to “criminal case[s].”
U. S. Const., Amdt. 5 (“No person . . . shall be compelled in
any criminal case to be a witness against himself”).
  In Counselman v. Hitchcock, 142 U. S. 547 (1892), the
Court indicated that the difference in phraseology was not
accidental. There the Court held that the Fifth Amend-
ment right not to be compelled to be a witness against
oneself “in any criminal case” could be invoked by a wit-
ness testifying before a grand jury. The Court rejected the
argument that there could be no “criminal case” prior to
indictment, reasoning that a “criminal case” under the
Fifth Amendment is much broader than a “criminal prose-
cutio[n]” under the Sixth Amendment. Id., at 563.
  The following Term, the Court construed the phrase
“criminal prosecution” in a statutory context, and this
time the Court squarely held that a “prosecution” does not
encompass preindictment stages of the criminal process.
In Virginia v. Paul, 148 U. S. 107 (1893), the Court con-
sidered Revised Statute §643, which authorized removal to
federal court of any “ ‘criminal prosecution’ ” “ ‘commenced
in any court of a State’ ” against a federal officer. Id., at
115. The respondent, a deputy marshal, had been ar-
rested by Virginia authorities on a warrant for murder
and was held in county jail awaiting his appearance before
a justice of the peace “with a view to a commitment to
await the action of the grand jury.” Id., at 118. He filed a
petition for removal of “ ‘said cause’ ” to federal court. Ibid.
The question before the Court was whether a “ ‘criminal
prosecution’ ” had “ ‘commenced’ ” within the meaning of
6             ROTHGERY v. GILLESPIE COUNTY

                     THOMAS, J., dissenting

the statute at the time the respondent filed his removal
petition.
   The Court held that a criminal prosecution had not com-
menced, and that removal was therefore not authorized by
the terms of the statute. The Court noted that under Vir-
ginia law murder could be prosecuted only “by indictment
found in the county court,” and that “a justice of the peace,
upon a previous complaint, [could] do no more than to
examine whether there [was] good cause for believing that
the accused [was] guilty, and to commit him for trial before
the court having jurisdiction of the offence.” Ibid. Accord-
ingly, where “no indictment was found, or other action
taken, in the county court,” there was as yet no “ ‘criminal
prosecution.’ ” Id., at 119. The appearance before the jus-
tice of the peace did not qualify as a “prosecution”:
    “Proceedings before a magistrate to commit a person
    to jail, or to hold him to bail, in order to secure his ap-
    pearance to answer for a crime or offence which the
    magistrate has no jurisdiction himself to try, before
    the court in which he may be prosecuted and tried,
    are but preliminary to the prosecution, and are no
    more a commencement of the prosecution, than is an
    arrest by an officer without a warrant for a felony
    committed in his presence.” Ibid.
                             C
   The foregoing historical summary is strong evidence
that the term “criminal prosecutio[n]” in the Sixth
Amendment refers to the commencement of a criminal suit
by filing formal charges in a court with jurisdiction to try
and punish the defendant. And on this understanding of
the Sixth Amendment, it is clear that petitioner’s initial
appearance before the magistrate did not commence a
“criminal prosecutio[n].” No formal charges had been
filed. The only document submitted to the magistrate was
the arresting officer’s affidavit of probable cause. The
                 Cite as: 554 U. S. ____ (2008)           7

                    THOMAS, J., dissenting

officer stated that he “ha[d] good reason to believe” that
petitioner was a felon and had been “walking around [an]
RV park with a gun belt on, carrying a pistol, handcuffs,
mace spray, extra bullets and a knife.” App. to Pet. for
Cert. 33a. The officer therefore “charge[d]” that petitioner
had “commit[ted] the offense of unlawful possession of a
firearm by a felon—3rd degree felony.” Ibid. The magis-
trate certified that he had examined the affidavit and
“determined that probable cause existed for the arrest of
the individual accused therein.” Id., at 34a. Later that
day, petitioner was released on bail, and did not hear from
the State again until he was indicted six months later.
   The affidavit of probable cause clearly was not the type
of formal accusation Blackstone identified with the com-
mencement of a criminal “prosecution.” Rather, it was the
preliminary accusation necessary to justify arrest and
detention—stages of the criminal process that Blackstone
placed before prosecution. The affidavit was not a plead-
ing that instituted a criminal prosecution, such as an
indictment, presentment, or information; and the magis-
trate to whom it was presented had no jurisdiction to try
and convict petitioner for the felony offense charged
therein. See Teal v. State, 230 S. W. 3d 172, 174 (Tex.
Crim. App. 2007) (“The Texas Constitution requires that,
unless waived by the defendant, the State must obtain a
grand jury indictment in a felony case”); Tex. Crim. Proc.
Code Ann., Arts. 4.05, 4.11(a) (West 2005). That is most
assuredly why the magistrate informed petitioner that
charges “will be filed” in district court. App. to Pet. for
Cert. 35a (emphasis added).
   The original meaning of the Sixth Amendment, then,
cuts decisively against the Court’s conclusion that peti-
tioner’s right to counsel attached at his initial appearance
before the magistrate. But we are not writing on a blank
slate: This Court has a substantial body of more recent
precedent construing the Sixth Amendment right to coun-
8               ROTHGERY v. GILLESPIE COUNTY

                       THOMAS, J., dissenting

sel.
                             II
   As the Court notes, our cases have “pegged commence-
ment” of a criminal prosecution, ante, at 5, to “the initia-
tion of adversary judicial criminal proceedings—whether
by way of formal charge, preliminary hearing, indictment,
information, or arraignment,” Kirby v. Illinois, 406 U. S.
682, 689 (1972) (plurality opinion). The Court has re-
peated this formulation in virtually every right-to-counsel
case decided since Kirby. Because Kirby’s formulation of
the attachment test has been accorded such precedential
significance, it is important to determine precisely what
Kirby said:
          “In a line of constitutional cases in this Court stem-
       ming back to the Court’s landmark opinion in Powell
       v. Alabama, 287 U. S. 45 [(1932)], it has been firmly
       established that a person’s Sixth and Fourteenth
       Amendment right to counsel attaches only at or after
       the time that adversary judicial proceedings have
       been initiated against him. See Powell v. Alabama,
       supra; Johnson v. Zerbst, 304 U. S. 458 [(1938)]; Ham-
       ilton v. Alabama, 368 U. S. 52 [(1961)]; Gideon v.
       Wainwright, 372 U. S. 335 [(1963)]; White v. Mary-
       land, 373 U. S. 59 [(1963) (per curiam)]; Massiah v.
       United States, 377 U. S. 201 [(1964)]; United States v.
       Wade, 388 U. S. 218 [(1967)]; Gilbert v. California,
       388 U. S. 263 [(1967)]; Coleman v. Alabama, 399 U. S.
       1 [(1970)].
          “This is not to say that a defendant in a criminal
       case has a constitutional right to counsel only at the
       trial itself. The Powell case makes clear that the right
       attaches at the time of arraignment, and the Court
       has recently held that it exists also at the time of a
       preliminary hearing. Coleman v. Alabama, supra.
       But the point is that, while members of the Court
                 Cite as: 554 U. S. ____ (2008)            9

                    THOMAS, J., dissenting

    have differed as to existence of the right to counsel in
    the contexts of some of the above cases, all of those
    cases have involved points of time at or after the ini-
    tiation of adversary judicial criminal proceedings—
    whether by way of formal charge, preliminary hear-
    ing, indictment, information, or arraignment.” Id., at
    688–689 (footnote omitted).
   It is noteworthy that Kirby did not purport to announce
anything new; rather, it simply catalogued what the Court
had previously held. And the point of the plurality’s dis-
cussion was that the criminal process contains stages
prior to commencement of a criminal prosecution. The
holding of the case was that the right to counsel did not
apply at a station house lineup that took place “before the
defendant had been indicted or otherwise formally charged
with any criminal offense.” Id., at 684.
   Kirby gave five examples of events that initiate “adver-
sary judicial criminal proceedings”: formal charge, pre-
liminary hearing, indictment, information, and arraign-
ment. None of these supports the result the Court reaches
today. I will apply them seriatim. No indictment or in-
formation had been filed when petitioner appeared before
the magistrate. Nor was there any other formal charge.
Although the plurality in Kirby did not define “formal
charge,” there is no reason to believe it would have in-
cluded an affidavit of probable cause in that category.
None of the cases on which it relied stood for that proposi-
tion. Indeed, all of them—with the exception of White v.
Maryland, 373 U. S. 59 (1963) (per curiam), and Coleman
v. Alabama, 399 U. S. 1 (1970)—involved postindictment
proceedings. See Powell v. Alabama, 287 U. S. 45, 49
(1932) (postindictment arraignment); Johnson v. Zerbst,
304 U. S. 458, 460 (1938) (trial); Hamilton v. Alabama,
368 U. S. 52, 53, n. 3 (1961) (postindictment arraignment);
Gideon v. Wainwright, 372 U. S. 335, 337 (1963) (trial);
10            ROTHGERY v. GILLESPIE COUNTY

                    THOMAS, J., dissenting

Massiah v. United States, 377 U. S. 201 (1964) (postin-
dictment interrogation); United States v. Wade, 388 U. S.
218, 219–220 (1967) (postindictment lineup); Gilbert v.
California, 388 U. S. 263, 269 (1967) (postindictment
lineup).
   Nor was petitioner’s initial appearance a preliminary
hearing. The comparable proceeding in Texas is called an
“examining trial.” See ante, at 9, n. 12. More importantly,
petitioner’s initial appearance was unlike the preliminary
hearings that were held to constitute “critical stages” in
White and Coleman, because it did not involve entry of a
plea, cf. White, supra, at 60, and was nonadversarial, cf.
Coleman, supra, at 9. There was no prosecutor present,
there were no witnesses to cross-examine, there was no
case to discover, and the result of the proceeding was not
to bind petitioner over to the grand jury or the trial court.
   Finally, petitioner’s initial appearance was not what
Kirby described as an “arraignment.” An arraignment, in
its traditional and usual sense, is a postindictment pro-
ceeding at which the defendant enters a plea. See, e.g.,
W. LaFave, J. Israel, & N. King, Criminal Procedure
§1.3(n), p. 19 (4th ed. 2004); 4 Blackstone *322. Although
the word “arraignment” is sometimes used to describe an
initial appearance before a magistrate, see LaFave, supra,
§1.3(j), at 16, that is not what Kirby meant when it said
that the right to counsel attaches at an “arraignment.”
Rather, it meant the traditional, postindictment arraign-
ment where the defendant enters a plea. This would be
the most reasonable assumption even if there were noth-
ing else to go on, since that is the primary meaning of the
word, especially when used unmodified.
   But there is no need to assume. Kirby purported to
describe only what the Court had already held, and none
of the cases Kirby cited involved an initial appearance.
Only two of the cases involved arraignments, and both
were postindictment arraignments at which the defendant
                    Cite as: 554 U. S. ____ (2008)                  11

                        THOMAS, J., dissenting

entered a plea. Hamilton, supra, at 53, n. 3; Powell, 287
U. S., at 49. And the considerations that drove the Court’s
analysis in those cases are not present here. See id., at 57
(emphasizing that “from the time of their arraignment
until the beginning of their trial, when consultation, thor-
oughgoing investigation and preparation were vitally
important, the defendants did not have the aid of coun-
sel”); Hamilton, supra, at 53–55 (emphasizing that the
defendant entered a plea and was required to raise or
waive certain defenses). Kirby’s inclusion of “arraign-
ment” in the list of adversary judicial proceedings that
trigger the right to counsel thus provides no support for
the view that the right to counsel attaches at an initial
appearance before a magistrate.
                            III
   It is clear that when Kirby was decided in 1972 there
was no precedent in this Court for the conclusion that a
criminal prosecution begins, and the right to counsel
therefore attaches, at an initial appearance before a mag-
istrate. The Court concludes, however, that two subse-
quent decisions—Brewer v. Williams, 430 U. S. 387 (1977),
and Michigan v. Jackson, 475 U. S. 625 (1986)—stand for
that proposition. Those decisions, which relied almost
exclusively on Kirby, cannot bear the weight the Court
puts on them.1
   In Brewer, the defendant challenged his conviction for
murdering a 10-year-old girl on the ground that his Sixth
——————
  1 The Court also relies on McNeil v. Wisconsin, 501 U. S. 171 (1991),

to support its assertion that the right to counsel attaches upon an
initial appearance before a magistrate. Ante, at 10–11. But in McNeil,
the Court expressed no view whatsoever on the attachment issue.
Rather, it noted that the issue was “undisputed,” and “accept[ed] for
purposes of the present case, that . . . [the defendant’s] Sixth Amend-
ment right had attached.” 501 U. S., at 175. We do not ordinarily give
weight to assumptions made in prior cases about matters that were not
in dispute.
12            ROTHGERY v. GILLESPIE COUNTY

                     THOMAS, J., dissenting

Amendment right to counsel had been violated when
detectives elicited incriminating statements from him
while transporting him from Davenport, Iowa, where he
had been arrested on a warrant for abduction and “ar-
raigned before a judge . . . on the outstanding arrest war-
rant,” to Des Moines, where he was to be tried. 430 U. S.,
at 390–391. The principal issue was whether the defen-
dant had waived his right to have counsel present during
police questioning when he voluntarily engaged one of the
detectives in a “wide-ranging conversation.” Id., at 392.
He subsequently agreed to lead the detectives to the girl’s
body in response to the so-called “ ‘Christian burial
speech,’ ” in which one of the detectives told the defendant
that “ ‘the parents of this little girl should be entitled to a
Christian burial for the little girl who was snatched away
from them on Christmas [E]ve and murdered.’ ” Id., at
392–393. Not surprisingly, the parties vigorously disputed
the waiver issue, and it sharply divided the Court.
   In contrast, the question whether the defendant’s right
to counsel had attached was neither raised in the courts
below nor disputed before this Court. Nonetheless, the
Court, after quoting Kirby’s formulation of the test, offered
its conclusory observations:
       “There can be no doubt in the present case that ju-
     dicial proceedings had been initiated against Williams
     before the start of the automobile ride from Davenport
     to Des Moines. A warrant had been issued for his ar-
     rest, he had been arraigned on that warrant before a
     judge in a Davenport courtroom, and he had been
     committed by the court to confinement in jail. The
     State does not contend otherwise.” 430 U. S., at 399.
    Brewer’s cursory treatment of the attachment issue
demonstrates precisely why, when “an issue [is] not ad-
dressed by the parties,” it is “imprudent of us to address it
. . . with any pretense of settling it for all time.” Metro-
                 Cite as: 554 U. S. ____ (2008)           13

                    THOMAS, J., dissenting

politan Stevedore Co. v. Rambo, 521 U. S. 121, 136 (1997).
As an initial matter, the Court’s discussion of the facts
reveals little about what happened at the proceeding.
There is no indication, for example, whether it was adver-
sarial or whether the defendant was required to enter a
plea or raise or waive any defenses—facts that earlier
cases such as Hamilton, White, and Coleman had found
significant.
   Even assuming, however, that the arraignment in
Brewer was functionally identical to the initial appearance
here, Brewer offered no reasoning for its conclusion that
the right to counsel attached at such a proceeding. One is
left with the distinct impression that the Court simply saw
the word “arraignment” in Kirby’s attachment test and
concluded that the right must have attached because the
defendant had been “arraigned.” There is no indication
that Brewer considered the difference between an ar-
raignment on a warrant and an arraignment at which the
defendant pleads to the indictment.
   The Court finds it significant that Brewer expressed “ ‘no
doubt’ ” that the right had attached. Ante, at 19 (quoting
430 U. S., at 399). There was no need for a “lengthy dis-
quisitio[n],” the Court says, because Brewer purportedly
“found the attachment issue an easy one.” Ante, at 18–19.
What the Court neglects to mention is that Brewer’s at-
tachment holding is indisputably no longer good law. That
is because we have subsequently held that the Sixth
Amendment right to counsel is “offense specific,” meaning
that it attaches only to those offenses for which the defen-
dant has been formally charged, and not to “other offenses
‘closely related factually’ to the charged offense.” Texas v.
Cobb, 532 U. S. 162, 164 (2001). Because the defendant in
Brewer had been arraigned only on the abduction warrant,
there is no doubt that, under Cobb, his right to counsel
had not yet attached with respect to the murder charges
that were subsequently brought. See 532 U. S., at 184
14            ROTHGERY v. GILLESPIE COUNTY

                     THOMAS, J., dissenting

(BREYER, J., dissenting) (noting that under the majority’s
rule, “[the defendant’s] murder conviction should have
remained undisturbed”). But the Court in Cobb did not
consider itself bound by Brewer’s implicit holding on the
attachment question. See 532 U. S., at 169 (“Constitu-
tional rights are not defined by inferences from opinions
which did not address the question at issue”). And here,
as in Cobb, Brewer did not address the fact that the ar-
raignment on the warrant was not the same type of ar-
raignment at which the right to counsel had previously
been held to attach, and the parties did not argue the
question. Brewer is thus entitled to no more precedential
weight here than it was in Cobb.
   Nor does Jackson control. In Jackson, as in Brewer, the
attachment issue was secondary. The question presented
was “not whether respondents had a right to counsel at
their postarraignment, custodial interrogations,” 475
U. S., at 629, but “whether respondents validly waived
their right to counsel,” id., at 630. And, as in Brewer, the
Court’s waiver holding was vigorously disputed. See 475
U. S., at 637–642 (Rehnquist, J., dissenting); see also
Cobb, supra, at 174–177 (KENNEDY, J., concurring) (ques-
tioning Jackson’s vitality). Unlike in Brewer, however, the
attachment question was at least contested in Jackson—
but barely. With respect to respondent Jackson, the State
conceded the issue. Jackson, supra, at 629, n. 3. And with
respect to respondent Bladel, the State had conceded the
issue below, see People v. Bladel, 421 Mich. 39, 77, 365
N. W. 2d 56, 74 (1984) (Boyle, J., dissenting), and raised it
for the first time before this Court, devoting only three
pages of its brief to the question, see Brief for Petitioner in
Michigan v. Bladel, O. T. 1985, No. 84–1539, pp. 24–26.
   The Court disposed of the issue in a footnote. See Jack-
son, supra, at 629–630, n. 3. As in Brewer, the Court did
not describe the nature of the proceeding. It stated only
that the respondents were “arraigned.” 475 U. S., at 627–
                     Cite as: 554 U. S. ____ (2008)                    15

                         THOMAS, J., dissenting

628. The Court phrased the question presented in terms
of “arraignment,” id., at 626 (“The question presented by
these two cases is whether the same rule applies to a
defendant who has been formally charged with a crime
and who has requested appointment of counsel at his
arraignment”), and repeated the words “arraignment” or
“postarraignment” no fewer than 35 times in the course of
its opinion.
   There is no way to know from the Court’s opinion in
Jackson whether the arraignment at issue there was the
same type of arraignment at which the right to counsel
had been held to attach in Powell and Hamilton. Only
upon examination of the parties’ briefs does it become
clear that the proceeding was in fact an initial appearance.
But Jackson did not even acknowledge, much less “flatly
rejec[t] the distinction between initial arraignment and
arraignment on the indictment.” Ante, at 9. Instead, it
offered one sentence of analysis—“In view of the clear
language in our decisions about the significance of ar-
raignment, the State’s argument is untenable”—followed
by a string citation to four cases, each of which quoted
Kirby. 475 U. S., at 629–630, n. 3. For emphasis, the
Court italicized the words “or arraignment” in Kirby’s
attachment test. 475 U. S., at 629, n. 3 (internal quotation
marks omitted).
   The only rule that can be derived from the face of the
opinion in Jackson is that if a proceeding is called an
“arraignment,” the right to counsel attaches.2 That rule
——————
  2 The  Court asserts that Jackson’s “conclusion was driven by the
same considerations the Court had endorsed in Brewer,” namely, that
“by the time a defendant is brought before a judicial officer, is informed
of a formally lodged accusation, and has restrictions imposed on his
liberty in aid of the prosecution, the State’s relationship with the
defendant has become solidly adversarial.” Ante, at 9. But Jackson
said nothing of the sort.
     Moreover, even looking behind the opinion, Jackson does not sup-
16              ROTHGERY v. GILLESPIE COUNTY

                        THOMAS, J., dissenting

would not govern this case because petitioner’s initial
appearance was not called an “arraignment” (the parties
refer to it as a “magistration”). And that would, in any
case, be a silly rule. The Sixth Amendment consequences
of a proceeding should turn on the substance of what
happens there, not on what the State chooses to call it.
But the Court in Jackson did not focus on the substantive
distinction between an initial arraignment and an ar-
raignment on the indictment. Instead, the Court simply
cited Kirby and left it at that. In these circumstances, I
would recognize Jackson for what it was—a cursory
treatment of an issue that was not the primary focus of
the Court’s opinion. Surely Jackson’s footnote must yield
to our reasoned precedents.
   And our reasoned precedents provide no support for the
conclusion that the right to counsel attaches at an initial
appearance before a magistrate. Kirby explained why the
right attaches “after the initiation of adversary judicial
criminal proceedings”:
       “The initiation of judicial criminal proceedings is far
     from a mere formalism. It is the starting point of our
——————
port the result the Court reaches today. Respondent Bladel entered a
“not guilty” plea at his arraignment, see Brief for Petitioner in Michi-
gan v. Bladel, O. T. 1985, No. 84–1539, p. 4, and both Hamilton v.
Alabama, 368 U. S. 52 (1961), and White v. Maryland, 373 U. S. 59
(1963) (per curiam), had already held that a defendant has a right to
counsel when he enters a plea. The Court suggests that this fact is
irrelevant because the magistrate in Bladel’s case “had no jurisdiction
to accept a plea of guilty to a felony charge.” Ante, at 10, n. 13. But
that distinction does not appear in either Hamilton or White. See
Hamilton, supra, at 55 (“Only the presence of counsel could have
enabled this accused to know all the defenses available to him and to
plead intelligently”); White, supra, at 60 (“[P]etitioner entered a plea
before the magistrate and that plea was taken at a time when he had
no counsel”). Thus, the most that Jackson can possibly be made to
stand for is that the right to counsel attaches at an initial appearance
where the defendant enters a plea. And that rule would not govern this
case because petitioner did not enter a plea at his initial appearance.
                 Cite as: 554 U. S. ____ (2008)           17

                    THOMAS, J., dissenting

    whole system of adversary criminal justice. For it is
    only then that the government has committed itself to
    prosecute, and only then that the adverse positions of
    government and defendant have solidified. It is then
    that a defendant finds himself faced with the prosecu-
    torial forces of organized society, and immersed in the
    intricacies of substantive and procedural criminal law.
    It is this point, therefore, that marks the commence-
    ment of the ‘criminal prosecutions’ to which alone the
    explicit guarantees of the Sixth Amendment are ap-
    plicable.” 406 U. S., at 689–690 (plurality opinion).
  None of these defining characteristics of a “criminal
prosecution” applies to petitioner’s initial appearance
before the magistrate. The initial appearance was not an
“adversary” proceeding, and petitioner was not “faced with
the prosecutorial forces of organized society.” Instead, he
stood in front of a “little glass window,” filled out various
forms, and was read his Miranda rights. Brief for Re-
spondent 5. The State had not committed itself to prose-
cute—only a prosecutor may file felony charges in Texas,
see Tex. Code Ann., Crim. Proc. Arts. 2.01, 2.02 (West
2005), and there is no evidence that any prosecutor was
even aware of petitioner’s arrest or appearance. The
adverse positions of government and defendant had not
yet solidified—the State’s prosecutorial officers had not
yet decided whether to press charges and, if so, which
charges to press. And petitioner was not immersed in the
intricacies of substantive and procedural criminal law—
shortly after the proceeding he was free on bail, and no
further proceedings occurred until six months later when
he was indicted.
  Moreover, the Court’s holding that the right to counsel
attaches at an initial appearance is untethered from any
interest that we have heretofore associated with the right
to counsel. The Court has repeatedly emphasized that
18            ROTHGERY v. GILLESPIE COUNTY

                     THOMAS, J., dissenting

“[t]he purpose of the constitutional guaranty of a right to
counsel is to protect an accused from conviction resulting
from his own ignorance of his legal and constitutional
rights.” Johnson, 304 U. S., at 465. The “core purpose” of
the right, the Court has said, is to “assure ‘Assistance’ at
trial, when the accused [is] confronted with both the intri-
cacies of the law and the advocacy of the public prosecu-
tor.” United States v. Ash, 413 U. S. 300, 309 (1973). The
Court has extended the right to counsel to pretrial events
only when the absence of counsel would derogate from the
defendant’s right to a fair trial. See, e.g., Wade, 388 U. S.,
at 227.
   Neither petitioner nor the Court identifies any way in
which petitioner’s ability to receive a fair trial was under-
mined by the absence of counsel during the period between
his initial appearance and his indictment. Nothing during
that period exposed petitioner to the risk that he would be
convicted as the result of ignorance of his rights. Instead,
the gravamen of petitioner’s complaint is that if counsel
had been appointed earlier, he would have been able to
stave off indictment by convincing the prosecutor that
petitioner was not guilty of the crime alleged. But the
Sixth Amendment protects against the risk of erroneous
conviction, not the risk of unwarranted prosecution. See
Gouveia, 467 U. S., at 191 (rejecting the notion that the
“purpose of the right to counsel is to provide a defendant
with a preindictment private investigator”).
   Petitioner argues that the right to counsel is implicated
here because restrictions were imposed on his liberty
when he was required to post bail. But we have never
suggested that the accused’s right to the assistance of
counsel “for his defence” entails a right to use counsel as a
sword to contest pretrial detention. To the contrary, we
have flatly rejected that notion, reasoning that a defen-
dant’s liberty interests are protected by other constitu-
tional guarantees. See id., at 190 (“While the right to
                  Cite as: 554 U. S. ____ (2008)           19

                     THOMAS, J., dissenting

counsel exists to protect the accused during trial-type
confrontations with the prosecutor, the speedy trial right
exists primarily to protect an individual’s liberty interest,”
including the interest in reducing the “ ‘impairment of
liberty imposed on an accused while released on bail’ ”).
                           IV
  In sum, neither the original meaning of the Sixth
Amendment right to counsel nor our precedents interpret-
ing the scope of that right supports the Court’s holding
that the right attaches at an initial appearance before a
magistrate. Because I would affirm the judgment below, I
respectfully dissent.

```

---
